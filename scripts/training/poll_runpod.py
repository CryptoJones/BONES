#!/usr/bin/env python3
"""Poll RunPod pod status for BONES training."""

import json
import subprocess
import sys
import time

import requests

POD_ID = ""  # set when pod is created


def get_key() -> str:
    try:
        return subprocess.check_output(["pass", "show", "runpod/api-key"], text=True).strip()
    except Exception:
        return sys.argv[1] if len(sys.argv) > 1 else ""


def query(q: str, key: str) -> dict:
    resp = requests.post(
        "https://api.runpod.io/graphql",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"query": q},
        timeout=30,
    )
    return resp.json()


def main():
    if not POD_ID:
        print("Set POD_ID at the top of this script before running.", file=sys.stderr)
        sys.exit(1)

    key = get_key()
    q = """{ pod(input: {podId: "%s"}) {
        desiredStatus
        runtime {
            uptimeInSeconds
            ports { ip publicPort privatePort type }
        }
        latestTelemetry { cpuUtilization memoryUtilization }
    } }""" % POD_ID

    print(f"Polling BONES pod {POD_ID} (Ctrl-C to stop)...\n")
    while True:
        d = query(q, key)
        if "data" not in d:
            print(f"API error: {d}", file=sys.stderr)
            time.sleep(30)
            continue
        pod = d["data"]["pod"]
        if pod is None:
            print("Pod not found.")
            break
        rt = pod.get("runtime") or {}
        telem = pod.get("latestTelemetry") or {}
        uptime = rt.get("uptimeInSeconds", 0)
        ports = [(p["publicPort"], p["privatePort"]) for p in (rt.get("ports") or [])]
        cpu = telem.get("cpuUtilization", "?")
        mem = telem.get("memoryUtilization", "?")
        status = pod.get("desiredStatus", "?")
        print(f"status={status}  uptime={uptime}s  cpu={cpu}%  mem={mem}%  ports={ports}")
        time.sleep(30)


if __name__ == "__main__":
    main()
