# gpu scan bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-scan_bjb1-32546_20260520T095121_result.json`
- **Structured JSON:** [`9cde44b4ec6ee2696e56.json`](../../sessions/9c/9cde44b4ec6ee2696e56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
SERVER: bjb1-32546
GPU_STATUS: 6x RTX 4090 (24GB each), CUDA 13.2
  GPU0: 0% util, 2MiB/24564MiB (idle)
  GPU1: 25% util, 2026MiB/24564MiB (PID 313749)
  GPU2: 24% util, 3086MiB/24564MiB (PID 314023)
  GPU3: 38% util, 2146MiB/24564MiB (PID 314619)
  GPU4: 29% util, 2477MiB/24564MiB (PID 314993)
  GPU5: 35% util, 2008MiB/24564MiB (PID 315482)

PID 681823: DEAD | no log file or exit record found
PID 313740: ALIVE | 01:30:32 | [pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 0.0% (0/10)
PID 314014: ALIVE | 01:30:27 | pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5
PID 314608: ALIVE | 01:30:22 | pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/10, success so far: 3/5
PID 314884: ALIVE | 01:30:17 | pick_up_the_milk_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5
PID 315473: ALIVE | 01:30:14 | [pick_up_the_milk_and_place_it_in_the_basket] success rate: 20.0% (2/10)
```

5 个进程存活且正常推进 eval rollouts（均运行约 1.5 小时）。PID 681823 已终止，无 log 文件和 exit record 残留，GPU 0 空闲。

---
