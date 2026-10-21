# ops scan bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scan-bjb2-40593_20260518T195507_result.json`
- **Structured JSON:** [`8cb325170e59871f01d7.json`](../../sessions/8c/8cb325170e59871f01d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-40593 服务器状态

### GPU 状态
| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 13% | 4232 MiB | 24564 MiB |

GPU 处于**忙碌状态**（有进程占用，利用率低是因为 evaluate.py 在 rollout 间歇）。

### 正在运行的实验
| tmux session | 实验 | 状态 |
|---|---|---|
| `eval-scalar-seed45-r2` | `crm_scalar`, seed=45, K=10, norm=0.1 | 运行中，正在评估 `salad_dressing` 任务（最后几个 task） |

最近输出显示 alphabet_soup 0/10, cream_cheese 0/10, salad_dressing 1/10，看起来接近完成。

### 已完成的实验
| 文件 | Mode | SR |
|---|---|---|
| `eval_object_random_selection_seed42` | random_selection | **13%** |
| `eval_object_vla_only_seed44` | vla_only | **10%** |
| `eval_object_obs_only` | crm_obs_only | **19%** |
| `eval_mag_obsonly_norm003` | crm_obs_only | **34%** |

### 空闲 GPU slot
**无**。当前 GPU 被 scalar-seed45-r2 占用。该实验看起来接近尾声（已跑到后面的 task），预计不久后释放。obs_only-norm02-seed48-r2 未在此服务器上运行。

---
