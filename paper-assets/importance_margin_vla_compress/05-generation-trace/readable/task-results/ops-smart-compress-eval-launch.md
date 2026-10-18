# ops smart compress eval launch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_smart_compress_eval_launch_20260518T001322_result.json`
- **Structured JSON:** [`6ad36b3735ae0476d22b.json`](../../sessions/6a/6ad36b3735ae0476d22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both eval processes are alive and running. Here's the full report:

---

## Smart Compression Training (cqa1-33015)

| Model | Status | Final Step | Train Loss | Eval Loss | Checkpoint |
|-------|--------|-----------|------------|-----------|------------|
| **M=32** | **Complete** | 99999/100000 | 0.110 | 0.052 | `checkpoints/smart_compress_m32/checkpoint.pt` (1.5GB) |
| **M=64** | **Complete** | 99999/100000 | 0.045 | 0.062 | `checkpoints/smart_compress_m64/checkpoint.pt` (1.5GB) |

- Training duration: ~6.5h each (01:38 → 08:28)
- Speed: 4.1 steps/sec
- Config: `smart_compress.yaml` (M=32), `smart_compress_m64.yaml` (M=64)

## LIBERO-Object Eval (cqa1-33015) — Just Launched

| Model | PID | GPU | Log | Output |
|-------|-----|-----|-----|--------|
| M=32 | **363256** | GPU 0 | `eval_M32.log` | `eval_results/smart_compress_m32_object.json` |
| M=64 | **364255** | GPU 1 | `eval_M64.log` | `eval_results/smart_compress_m64_object.json` |

- 10 tasks x 50 episodes = 500 total per model
- Early episodes on Task 0 are all FAIL for both — may need monitoring

## OpenVLA k=0.7 Eval (westd-27271)

- PID **755666** alive
- Progress: Task 2/10 starting (Task 1 complete: **SR=0.740**, 37/50)
- Speed: ~2.0 eps/min → ETA ~3.7h remaining for 9 tasks
- Mode: random_prune, k=0.7, 50 episodes/task

---
