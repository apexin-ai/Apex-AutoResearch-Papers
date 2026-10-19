# ssh scan bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-bjb2-40593_20260520T024110_result.json`
- **Structured JSON:** [`2d636c1e2ab1cdfe015b.json`](../../sessions/2d/2d636c1e2ab1cdfe015b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX 4090 D | 4066/24564 MiB (17%) | 15% |

### 运行中进程
- **PID 647880** (cuda:0): `evaluate.py --mode adaptive_k --adaptive_threshold 0.054959 --k_full 10 --benchmark object --seed 44 --n_rollouts 10 --output_file logs/eval_adaptive_k_p25_seed44.json`

### adaptive-k 进度 (eval-adaptive-k-p25-seed44)
正在 task 5/10 (`pick_up_the_ketchup`, rollout 5/10)，约 **45% 完成**。

已完成的 task 结果：
| Task | SR |
|------|-----|
| alphabet_soup | 0/10 |
| cream_cheese | 1/10 |
| salad_dressing | 1/10 |
| bbq_sauce | 4/10 |
| ketchup | 进行中 (0/5) |

### adaptive-k JSON 输出
**不存在** — `logs/eval_adaptive_k_*.json` 尚未生成，需等实验完成后才会写入。`logs/` 下也没有任何文件名含 "adaptive"。

### 最新已完成的 JSON 文件 (logs/)
| 文件 | 时间 | SR |
|------|------|-----|
| eval_object_vla_only_seed48.json | May 20 07:36 | **10%** (object, vla_only) |
| eval_spatial_obs_only_norm02_seed44.json | May 20 04:28 | **32%** (spatial, crm_obs_only) |
| eval_object_scalar_seed45_r2.json | May 19 19:40 | — |
| eval_object_random_selection_seed42.json | May 18 20:17 | — |

---
