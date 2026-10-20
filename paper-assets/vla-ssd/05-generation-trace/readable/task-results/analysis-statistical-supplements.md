# analysis statistical supplements

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_statistical_supplements_20260520T174541_result.json`
- **Structured JSON:** [`64e364acfc213bd7912d.json`](../../sessions/64/64e364acfc213bd7912d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项分析全部完成，结果汇总：

---

### 任务 1: TOST 等价性检验
| 指标 | 值 |
|------|-----|
| OpenVLA peak | **L9**, mean R²=0.6372, std=0.0086, N=15 |
| Phi3V peak | **L11**, mean R²=0.6340, std=0.0089, N=15 |
| Δ (mean_diff) | **0.003253** |
| ε (bound) | 0.05 |
| p_TOST | **< 0.0001** |
| 90% CI | **[−0.0022, 0.0087]** — 完全落在 [−0.05, +0.05] 内 |
| 结论 | **equivalent** |
| 传统 t-test | t=1.016, p=0.318 (差异不显著) |

---

### 任务 2: Power Analysis
| 指标 | RSA | R² |
|------|-----|-----|
| Within-task SD | 0.0302 | 0.0258 |
| Δ of interest | 0.017 | 0.069 |
| Cohen's d | 0.5624 | 2.6785 |
| Power at N=10 | **0.356** | **1.000** |
| Min detectable Δ (N=10, d=0.996) | 0.0301 | 0.0257 |

RSA Δ=0.017 的 power 仅 0.36（underpowered），但 R² Δ=0.069 的 power 为 1.0（充足）。N=10 能可靠检出 Δ≥0.030 的 RSA 差异。

---

### 任务 3: Paired Cohen's d_z
| Comparison | d_z | N pairs |
|------------|-----|---------|
| RSA trained vs untrained (L12) | **0.5461** | 10 |
| L1 ablation dominant-24 vs baseline | **1.1673** | 10 |
| L1 ablation random-24 vs baseline | **1.8423 ± 0.33** | 30×10 |
| Dose-response 32v4 (MSE) | **1.7917** | 3 |
| Dose-response 32v4 (KL) | **3.1538** | 3 |
| RSA inst vs no_inst | **0.0563** (negligible) | 10 |
| Cross-arch OpenVLA L9 vs Phi3V L11 | **0.4772** (small-medium) | 15 |

所有文件已保存到 `/root/autodl-tmp/vla-ssd/results/statistical_supplements/`。

---
