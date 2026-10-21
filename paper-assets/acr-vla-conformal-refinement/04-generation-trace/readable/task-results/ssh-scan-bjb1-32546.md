# ssh scan bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-bjb1-32546_20260520T024100_result.json`
- **Structured JSON:** [`91fd887418ec8b3d578f.json`](../../sessions/91/91fd887418ec8b3d578f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 状态扫描结果

### GPU 状态 (6x RTX 4090)

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 0% | 2/24564 MiB | 空闲（tmux session `eval-adaptive-k-p75-seed44` 挂着但已完成） |
| 1 | 27% | 2072/24564 MiB | PID 171147 — `crm_obs_only`, spatial, seed48, K=10, norm0.2 |
| 2 | 0% | 2/24564 MiB | 空闲 |
| 3 | 22% | 1958/24564 MiB | PID 178892 — `vla_only`, spatial, seed47, K=1 |
| 4 | 0% | 2/24564 MiB | 空闲 |
| 5 | 0% | 2/24564 MiB | 空闲 |

### 正在运行的 evaluate.py 进程

1. **PID 171147** (cuda:1) — `crm_obs_only`, benchmark=spatial, seed=48, K=10, max_correction_norm=0.2, 输出 `eval_spatial_obs_only_norm02_seed48.json`，运行 ~1h21m
2. **PID 178892** (cuda:3) — `vla_only`, benchmark=spatial, seed=47, K=1, 输出 `eval_spatial_vla_only_seed47.json`，运行 ~1h02m

### Adaptive-K Sweep JSON 结果 (全部已完成)

| 文件 | SR | avg_K | fast_path_ratio | threshold | 时间 |
|------|-----|-------|-----------------|-----------|------|
| `eval_adaptive_k_p25_seed42.json` | **15%** | 4.80 | 65.0% | 0.054959 | 10:29 |
| `eval_adaptive_k_p50_seed44.json` | **14%** | 3.91 | 76.1% | 0.074855 | 10:23 |
| `eval_adaptive_k_p75_seed44.json` | **16%** | 3.02 | 87.2% | 0.098735 | 10:10 |
| `eval_adaptive_k_p90_seed42.json` | **12%** | 2.67 | 91.6% | 0.126512 | 10:15 |

### 关键观察

- 之前提到的 `eval-adaptive-k-p25-seed42` (cuda:5) 和 `eval-adaptive-k-p90-seed42` (cuda:4) 均已完成，GPU 已释放
- 4 个 adaptive-k sweep 全部跑完，SR 在 12%–16% 之间，随 threshold 增大（更激进的 fast path）SR 略降
- fast_path_ratio 从 p25 的 65% 提升到 p90 的 92%，但 avg_K 从 4.8 降到 2.67
- GPU 0/2/4/5 空闲，可用于新实验

---
