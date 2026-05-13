#!/usr/bin/env python3
"""Merge BONES LoRA adapter into base model weights for deployment."""

import argparse
from pathlib import Path

import torch
import yaml
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Merge BONES LoRA adapter into base weights")
    parser.add_argument("--config", default="configs/training_config.yaml")
    parser.add_argument("--adapter", help="Path to adapter (overrides config output_dir/final)")
    parser.add_argument("--output", default="output/bones-merged", help="Output path for merged model")
    args = parser.parse_args()

    config = load_config(args.config)
    base_model_name = config["model"]["name"]
    adapter_path = args.adapter or str(Path(config["training"]["output_dir"]) / "final")
    output_path = args.output

    print(f"Base model:   {base_model_name}")
    print(f"Adapter:      {adapter_path}")
    print(f"Output:       {output_path}")

    print("\nLoading base model...")
    model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.bfloat16,
        device_map={"": 0},
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)

    print("Loading adapter...")
    model = PeftModel.from_pretrained(model, adapter_path)

    print("Merging weights...")
    model = model.merge_and_unload()

    print(f"Saving merged model to {output_path}...")
    model.save_pretrained(output_path, safe_serialization=True)
    tokenizer.save_pretrained(output_path)

    print("Done. Upload to HuggingFace with:")
    print(f"  huggingface-cli upload Ronin48/bones {output_path}")


if __name__ == "__main__":
    main()
