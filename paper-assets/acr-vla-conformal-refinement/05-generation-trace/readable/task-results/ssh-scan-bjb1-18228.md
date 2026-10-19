# ssh scan bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-bjb1-18228_20260520T024104_result.json`
- **Structured JSON:** [`3c7d97b6b393ac8cf700.json`](../../sessions/3c/3c7d97b6b393ac8cf700.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 状态扫描结果

### GPU 状态 (4× GPU, 24GB each)

| GPU | 利用率 | 显存 | PID | 进程 |
|-----|--------|------|-----|------|
| 0 | 21% | 2376/24564 MiB | 200697 | `evaluate.py --mode vla_only --benchmark object --seed 49 --K 1` |
| 1 | 22% | 3560/24564 MiB | 211897 | `evaluate.py --mode vla_only --benchmark spatial --seed 50 --K 1` |
| 2 | 25% | 2071/24564 MiB | 201265 | `evaluate.py --mode crm_obs_only --benchmark spatial --seed 47 --K 10 --max_correction_norm 0.2` |
| 3 | 23% | 1961/24564 MiB | 196349 | `evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark object --seed 43` |

### 实验进度 (每个 benchmark 10 个 task)

| GPU | 实验 | 输出文件 | 已完成 task | 进度 |
|-----|------|----------|-------------|------|
| 0 | vla_only object seed49 | `eval_object_vla_only_seed49.json` | 7/10 | ~70% |
| 1 | vla_only spatial seed50 | `eval_spatial_vla_only_seed50.json` | 5/10 | ~50% |
| 2 | crm_obs_only spatial seed47 | `eval_spatial_obs_only_norm02_seed47.json` | 8/10 | ~80% |
| 3 | **adaptive_k p50 seed43** | `eval_adaptive_k_p50_seed43.json` | 8/10 | ~80% |

### adaptive-k JSON 输出

**尚未生成**。`eval_adaptive_k_p50_seed43.json` 不存在——实验仍在运行（8/10 tasks 完成），JSON 在所有 task 跑完后才写入。

### 其他 sweep 实验

**未发现** p50-seed42、p75-seed42、p75-seed43 等其他 sweep 进程。当前只有 p50-seed43 一个 adaptive-k 实验在跑。

### logs 目录已有 JSON（最近的）

| 文件 | 时间 |
|------|------|
| `eval_long_vla_only_seed48.json` | May 20 07:14 |
| `eval_object_vla_only_seed50.json` | May 20 07:12 |
| `eval_long_obs_only_norm02_seed46.json` | May 20 07:10 |
| `eval_long_obs_only_norm02_seed45.json` | May 20 05:58 |
| `eval_object_vla_only_seed48.json` | May 20 05:55 |
| `eval_goal_obs_only_norm02_seed42.json` | May 20 05:20 |
| `eval_goal_obs_only_norm02_seed43.json` | May 20 05:13 |

所有 4 张 GPU 都在跑实验，预计 GPU 2 和 GPU 3 的实验（各 8/10）会先完成。

---
