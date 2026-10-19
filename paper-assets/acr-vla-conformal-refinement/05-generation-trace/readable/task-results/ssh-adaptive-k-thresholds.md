# ssh adaptive k thresholds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_adaptive-k-thresholds_20260519T224008_result.json`
- **Structured JSON:** [`ac09b1e3cb09351078a7.json`](../../sessions/ac/ac09b1e3cb09351078a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. JSON 结构

| Top-level key | 内容 |
|---|---|
| `config` | benchmark="object", n_episodes=5, seed=42, n_steps_collected=14512, num_ode_steps=10 |
| `statistics` | 预计算的 fmvd/k10_variance/k2_l2 统计量 + 相关性 |
| `per_step_data` | 14512 条记录，每条含 step, task, episode, env_step, fmvd, k10_variance, k2_l2, episode_success |

### 2. K2_L2 百分位数（从原始数据独立验证，与 JSON 预计算一致）

| 百分位 | 值 |
|---|---|
| **P25** | 0.054959 |
| **P50** | 0.074855 |
| **P75** | 0.098735 |
| **P90** | 0.126512 |

### 3. 描述性统计

| 指标 | 值 |
|---|---|
| Mean | 0.080700 |
| Std | 0.036103 |
| Min | 0.018047 |
| Max | 0.403870 |
| N | 14512 |

### 4. JSON 中已有的额外信息

- `k2_l2_vs_k10_spearman_rho` = 0.997868（K2_L2 与 K10_variance 高度相关）
- `k2_l2_vs_fmvd_spearman_rho` = 0.092493（K2_L2 与 FMVD 弱相关）
- FMVD 百分位也有预计算：P25=0.027738, P50=0.046693, P75=0.070899, P90=0.093805

---
