# deploy bjb2 24035 now

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-24035-now_20260526T172447_result.json`
- **Structured JSON:** [`8641645d715ed2ec997d.json`](../../sessions/86/8641645d715ed2ec997d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**部署中止（C001 违规）。** GPU 上正在运行另一个实验：

- **PID 83735**（已运行 25 分钟）：`evaluate.py --mode adaptive_conformal_crm --conformal_threshold 0.45 --benchmark spatial --seed 42`
- 显存占用：5926 MiB

需要等当前实验跑完后再部署 τ=0.15 Object 实验。

---
