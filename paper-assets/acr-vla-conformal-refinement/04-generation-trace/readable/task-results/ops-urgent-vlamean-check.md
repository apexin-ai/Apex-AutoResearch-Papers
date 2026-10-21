# ops urgent vlamean check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-vlamean-check_20260515T140505_result.json`
- **Structured JSON:** [`19765a212f0ce3a2f975.json`](../../sessions/19/19765a212f0ce3a2f975.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### cuda:5 上的进程
**PID 18814** — `evaluate.py --mode vla_only --baseline_mode mean --benchmark object --n_rollouts 10 --K 10`
- 即 **eval-vla-mean-object**，确认就是 Registry 记录的那个实验
- PID 18808 是父 shell，18814 是实际 Python 进程
- VRAM 占用：2356 MiB

### VLA-mean 进度
**正在跑，进度 8/10 tasks**（已完成 7 个 task，第 8 个 `pick_up_the_milk` 在跑 rollout 5/10）

已完成 tasks 的成功率：
| Task | 成功率 |
|------|--------|
| alphabet_soup | 0/10 (0%) |
| cream_cheese | 0/10 (0%) |
| salad_dressing | 1/10 (10%) |
| bbq_sauce | 3/10 (30%) |
| ketchup | 1/10 (10%) |
| tomato_sauce | 1/10 (10%) |
| butter | 0/10 (0%) |
| milk | 进行中 (2/5 so far) |

### 全卡进程映射（6x RTX 4090）

| GPU | PID | 实验 | VRAM |
|-----|-----|------|------|
| 0 | 9659 | reconvla (object, K=10) | 1887 MiB |
| 1 | 11116 | crm_perdof (object, K=10) | 1923 MiB |
| 2 | 13806 | crm_obs_only (norm=0.1, K=10) | 1923 MiB |
| 3 | 14012 | crm_scalar (object, K=10) | 1923 MiB |
| 4 | 44270 | crm_obs_only (norm=0.2, K=10) | 2856 MiB |
| 5 | 18814 | **vla_mean** (object, K=10) | 2356 MiB |

6 张卡全满，都在跑 object benchmark 的不同 mode evaluation。

---
