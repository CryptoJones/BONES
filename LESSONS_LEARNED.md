# Lessons Learned — BONES Training

The full shared lessons learned for all Ronin 48 models lives in the Models repo:

**[Ronin48/Models — LESSONS_LEARNED.md](https://codeberg.org/Ronin48/Models/raw/branch/main/LESSONS_LEARNED.md)**

Read it before you start a training run. Errors #1–#22 are all there.

BONES-specific notes:
- Llama-3.3-70B uses 30 shards (~140 GB). **Minimum volume: 300 GB.** A 100 GB volume
  fills at shard 22/30. A 200 GB volume fills during checkpointing. See Error #8 and #20.
- Always set `volumeMountPath: "/workspace"` when deploying via API. See Error #21.

---

## Contributing

If you hit a new BONES-specific error, add it to the Models repo lessons learned so
everyone benefits. The people walking behind you will thank you.
