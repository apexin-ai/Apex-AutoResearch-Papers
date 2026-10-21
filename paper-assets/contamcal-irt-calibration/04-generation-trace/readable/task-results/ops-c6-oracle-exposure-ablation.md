# ops c6 oracle exposure ablation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c6_oracle_exposure_ablation_20260517T145133_result.json`
- **Structured JSON:** [`f598a499567766bf633e.json`](../../sessions/f5/f598a499567766bf633e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## Oracle Exposure Ablation 结果

### MMLU (2000 items, 13 models)
| 指标 | 值 |
|------|-----|
| **γ** | **-0.0121** (sd=0.068) |
| 95% CI | [-0.145, 0.119] |
| CI excludes 0 | **No** |
| CAL MAE | 0.0106 |
| PPP | 0.4128 |
| Diagnostics | OK (Rhat=1.009, ESS=1085, 0 divergences) |
| Fit time | 502.5s |

### ARC Challenge (1172 items, 13 models)
| 指标 | 值 |
|------|-----|
| **γ** | **0.1176** (sd=0.097) |
| 95% CI | [-0.075, 0.306] |
| CI excludes 0 | **No** |
| CAL MAE | 0.0142 |
| PPP | 0.0305 |
| Diagnostics | OK (Rhat=1.007, ESS=1270, 0 divergences) |
| Fit time | 259.6s |

---

**关键发现**:
- **MMLU**: γ ≈ 0，oracle binary exposure 无法检测到显著的 contamination effect。95% CI 包含 0。
- **ARC**: γ = 0.12 (positive，pro-contamination 方向)，但 95% CI 仍包含 0，不显著。80% CI 的下界为 -0.007，接近显著。
- 两个 benchmark 的 diagnostics 均通过 (Rhat < 1.01, ESS > 400, 0 divergences)。
- MMLU γ 为负值（-0.012）可能因为 contamination effect 在 MMLU 上极小，被噪声淹没。
- ARC γ 方向正确（0.12 > 0），暗示 contaminated items 确实更容易，但效应不够强以 95% 水平排除 0。

产出路径: `/root/autodl-tmp/exp006/oracle_exposure_ablation/`

---
