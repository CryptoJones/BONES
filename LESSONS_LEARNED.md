# Lessons Learned — BONES Training

This document captures dependency conflicts, environment bugs, and hard-won fixes
encountered during BONES training runs. Read this before you start.

For issues common to all Ronin 48 models (RunPod environment, bitsandbytes, torchvision,
QLoRA dependency conflicts), see [ABBY's LESSONS_LEARNED.md](https://codeberg.org/Ronin48/ABBY/raw/branch/main/LESSONS_LEARNED.md) —
it has the most complete record of the first training run.

---

## BONES-Specific Notes

### Disk-Full Crash on First Training Run (2026-05-13)

BONES uses Llama-3.3-70B (30 shards, ~140 GB). The pod was launched with a **100 GB volume**.
It filled at shard 22/30 with `OSError: [Errno 28] No space left on device`. Training never
started. GPU stayed at 0%. The training monitor reported "waiting to start" for an hour.

**Minimum volume for BONES: 200 GB. Recommended: 300 GB.**

The monitor has since been fixed with pre-flight disk checks. See
[ABBY Error #20](https://codeberg.org/Ronin48/ABBY/raw/branch/main/LESSONS_LEARNED.md)
for the full incident writeup and fix details.

**If you see `GPU 0% | active=False` after 20+ minutes: SSH in. Do not assume it's still initializing.**

---

## Contributing

If you hit a new error and fix it, please add it here. The people walking behind
you will thank you.
