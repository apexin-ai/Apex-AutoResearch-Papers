# ssh check calibration results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-calibration-results_20260520T032504_result.json`
- **Structured JSON:** [`aee2ab4803479c6f0e6e.json`](../../sessions/ae/aee2ab4803479c6f0e6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### CRM Magnitude Calibration（目标文件）: 未完成

两台服务器的 `crm_magnitude_calibration.json` 均**未产出**。

| 服务器 | Log 大小 | 进度 | GPU 状态 |
|--------|---------|------|---------|
| bjb2-28827 | 2883B (11:24) | 16/100 episodes (Task 2 ep 6/10) | GPU 5: 33%, 9.5GB — 可能仍在跑(输出缓冲) |
| bjb2-40593 | 459B (11:23) | 3/100 episodes (Task 1 run 3) | GPU 0: 12%, 8.6GB — 进度极慢或已停 |

### 已完成的 Calibration（bjb2-28827）

bjb2-28827 上有两个**已完成**的 calibration JSON（14,512 steps, 5 episodes × 10 tasks）:

#### `k2_l2_calibration.json` — 包含部分你要的相关性

| 相关性 | ρ | p-value | 判断 |
|--------|---|---------|------|
| **ρ(K2_L2_distance, K10_variance)** (sanity check) | **0.9979** | 0.0 | 近乎完美正相关，sanity check 通过 |
| ρ(K2_L2_distance, FMVD) | 0.0925 | 6.0e-29 | 极弱 |

K2_L2 分布: mean=0.0807, std=0.036, P50=0.075, P90=0.127

#### `fmvd_calibration.json`

| 相关性 | ρ | p-value | 判断 |
|--------|---|---------|------|
| ρ(FMVD, K10_variance) | 0.0825 | 2.3e-23 | 极弱（统计显著仅因 N 大） |

FMVD 分布: mean=0.055, std=0.040, P50=0.047, P90=0.094
K10_variance 分布: mean=0.00489, std=0.00564

### 缺失的相关性

你需要的 **ρ(K1_correction_magnitude, K10_variance)** 和 **ρ(K2_correction_magnitude, K10_variance)** 和 **ρ(K1_correction_magnitude, K2_L2_distance)** 都来自 CRM magnitude calibration 脚本，该脚本在两台服务器上都**未跑完**。

### Go/No-Go 初步判断

- Sanity check **通过**: K2_L2 ↔ K10_variance ρ=0.998，两种不确定性度量高度一致
- FMVD 作为不确定性代理**失败**: ρ≈0.08，几乎无预测力
- CRM correction magnitude 的关键相关性**待定**，需等 `crm_magnitude_calibration.json` 产出

是否需要我检查 bjb2-28827 上的 calibration 进程是否仍在运行，或重启/加速该脚本？

---
