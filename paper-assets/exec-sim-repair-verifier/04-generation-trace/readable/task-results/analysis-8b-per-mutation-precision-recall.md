# analysis 8b per mutation precision recall

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8b-per-mutation-precision-recall_20260516T014054_result.json`
- **Structured JSON:** [`324a31ccb48e3243cabd.json`](../../sessions/32/324a31ccb48e3243cabd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。纯 CPU 任务，**cuda:0 空闲可分配**。

## Per-mutation-type 8B vs 4B 对比

**配置差异**: 8B = Qwen3-8B ckpt-3600, seq=8192 | 4B = Qwen3-4B ckpt-600, seq=2048

### Fail 类检测（诊断能力核心指标）

| mutation_type | N | 8B P(fail) | 8B R(fail) | 8B F1(fail) | 4B P(fail) | 4B R(fail) | 4B F1(fail) | ΔF1 |
|---|---|---|---|---|---|---|---|---|
| gold | 4633 | — | — | — | — | — | — | — |
| operator_swap | 3357 | 90.62 | 69.65 | 78.76 | 74.31 | 77.70 | 75.97 | **+2.79** |
| boundary_removal | 1049 | 64.10 | 20.42 | 30.98 | 60.89 | 82.68 | 70.13 | **-39.15** |
| return_value | 562 | 97.85 | 57.59 | 72.51 | 73.06 | 83.23 | 77.81 | **-5.30** |
| off_by_one | 183 | 85.71 | 66.67 | 75.00 | 45.00 | 66.67 | 53.73 | **+21.27** |

### 总体指标（Accuracy / F1 macro）

| mutation_type | N | 8B Acc | 4B Acc | ΔAcc | 8B F1mac | 4B F1mac | ΔF1mac |
|---|---|---|---|---|---|---|---|
| gold | 4633 | 96.24 | 82.80 | **+13.44** | 49.05 | 45.30 | +3.75 |
| operator_swap | 3357 | 81.38 | 75.63 | **+5.75** | 81.09 | 75.63 | **+5.46** |
| boundary_removal | 1049 | 46.90 | 58.91 | **-12.01** | 43.92 | 52.16 | **-8.24** |
| return_value | 562 | 75.44 | 73.31 | +2.13 | 75.16 | 72.16 | +3.00 |
| off_by_one | 183 | 86.89 | 66.12 | **+20.77** | 83.06 | 63.50 | **+19.56** |

### 关键发现

**支持 Claim 2 的**: 
- **off_by_one**: 8B F1mac +19.56pp，最大提升，说明更大模型更擅长捕捉细微的 off-by-one 错误
- **operator_swap**: 8B F1mac +5.46pp，最大类别（n=3357），稳定提升
- **gold**: 8B accuracy +13.44pp，正确 patch 识别率显著提高

**不利于 Claim 2 的**:
- **boundary_removal**: 8B F1mac -8.24pp，fail recall 从 82.68% 暴跌至 20.42%。8B 几乎把所有 boundary_removal mutation 都判成 pass，严重漏检
- **return_value**: fail F1 -5.30pp，8B fail recall 也偏低（57.59% vs 83.23%）

**模式**: 8B 整体 pass bias 更强——在 gold 上受益（更准），但在 boundary_removal/return_value 上导致漏检 mutation。这可能与 seq_len 差异（8192 vs 2048）有关，更长 context 可能让模型倾向于认为 patch 是对的。

**建议**: Claim 2 需要 nuanced framing——scaling 在 operator_swap 和 off_by_one 上有效，但 boundary_removal 是明显的 failure mode，论文中需要讨论这个 pass bias trade-off。

---
