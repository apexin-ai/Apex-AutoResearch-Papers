# experiment alfworld seed3 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_alfworld-seed3-v2_20260520T170757_result.json`
- **Structured JSON:** [`0696aacdce4b62a1fead.json`](../../sessions/06/0696aacdce4b62a1fead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training is starting up successfully:

- **Seed format**: ✅ `seed: {train: 42, val: 123}` — correctly resolved
- **Ray**: ✅ Local Ray instance started (dashboard at 127.0.0.1:8266)
- **Config**: ✅ All parameters correct (episode-level, full context window, 2 GPUs)
- **No errors**: Only benign warnings (conda, gym deprecation, Hydra defaults)

**Summary**:
- `exp029_seed3_v2` submitted on westd-47453 cuda:0,1, PID 991448
- Fixed seed format from bare `seed=42` → `seed.train=42 seed.val=123`
- Checkpoints → `/root/autodl-tmp/checkpoints/exp029-seed3/`
- W&B experiment name: `exp029-seed3-episode-level`
- 15 training steps, 12h timeout

---
