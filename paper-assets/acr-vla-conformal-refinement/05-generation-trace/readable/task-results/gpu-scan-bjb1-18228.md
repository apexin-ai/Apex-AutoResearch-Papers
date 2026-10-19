# gpu scan bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-scan_bjb1-18228_20260520T095114_result.json`
- **Structured JSON:** [`9b223a7033b2d1c3692b.json`](../../sessions/9b/9b223a7033b2d1c3692b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
SERVER: bjb1-18228
GPU_STATUS: 4x RTX 4090 (24GB each), CUDA 13.0, Driver 580.105.08
  GPU0: 1869MiB/24564MiB, 19%, 42°C (PID 308078)
  GPU1: 2025MiB/24564MiB, 25%, 41°C (PID 308350)
  GPU2: 2555MiB/24564MiB, 11%, 37°C (PID 308617)
  GPU3: 2145MiB/24564MiB, 48%, 57°C (PID 309210)

PID 308073: ALIVE | 01:48:14 | [KITCHEN_SCENE8_put_both_moka_pots_on_the_stove] success rate: 0.0% (0/10)
PID 308345: ALIVE | 01:48:10 | [pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 20.0% (2/10)
PID 308612: ALIVE | 01:48:07 | pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5
PID 309205: ALIVE | 01:48:04 | pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5
```

4 个评估进程全部存活，均已运行约 1 小时 48 分钟，log 持续输出 rollout 结果，正常运行中。

---
