# analysis bootstrap s42 westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-s42-westd_20260519T165008_result.json`
- **Structured JSON:** [`385f66a7ed25b2e8d247.json`](../../sessions/38/385f66a7ed25b2e8d247.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 benchmark 都完成了。汇总核心结果：

---

## MMLU Bootstrap (B=10000, 14042 items)

| Model | Baseline | Δ(d100−d000) | Pattern | Stability | Delta 95% CI |
|---|---|---|---|---|---|
| Phi-4 14.7B | 76.44% | −0.17pp | Immune | **100.0%** | [−0.60, +0.26] |
| Qwen2.5-14B | 69.44% | −9.37pp | U-collapse | **100.0%** | [−10.04, −8.70] |
| Qwen2.5-7B | 66.11% | −1.78pp | V-recovery | **99.6%** | [−2.36, −1.22] |
| Gemma-2 9B | 61.86% | +3.76pp | Benefit | **76.6%** | [+3.18, +4.33] |
| OLMo-2 7B | 53.79% | +3.21pp | Benefit-sat | **100.0%** | [+2.73, +3.71] |

**Benefit/Harm Threshold**: 64.7% (95% CI: [64.0, 65.4])，10000/10000 crossings valid。

## ARC Challenge Bootstrap (B=10000, 1172 items)

| Model | Baseline | Δ(d100−d000) | Pattern | Stability | Delta 95% CI |
|---|---|---|---|---|---|
| Phi-4 14.7B | 92.06% | +0.60pp | Immune | **81.2%** | [−0.26, +1.45] |
| Qwen2.5-14B | 91.04% | −2.56pp | V-recovery | **96.3%** | [−3.67, −1.54] |
| Qwen2.5-7B | 87.88% | −2.90pp | V-recovery | **95.8%** | [−4.18, −1.62] |
| Gemma-2 9B | 86.01% | −1.19pp | V-recovery | **62.7%** | [−2.47, +0.09] |
| OLMo-2 7B | 76.11% | +3.92pp | Benefit-sat | **53.3%** | [+2.39, +5.46] |

**Benefit/Harm Threshold**: 83.6% (95% CI: [80.7, 85.9])，10000/10000 crossings valid。

## 关键发现

- **MMLU 分类非常稳定**：4/5 模型 stability ≥99.6%，Gemma-2 较低（76.6%）因其 delta CI 上下界都在 +3~+4pp，靠近 Benefit/Benefit-sat 边界但远离 Immune。
- **ARC 稳定性明显低于 MMLU**：item 数仅 1172（vs 14042），bootstrap 方差更大。OLMo-2 仅 53.3% stable，Gemma-2 62.7%——这两个模型的 ARC profile 分类不够 robust。
- **Threshold CI 很紧**：MMLU ~64% 基线附近的模型从 benefit 转 harm，仅 ±0.7pp 宽度；ARC threshold 更高（~84%）但 CI 较宽（±2.6pp）。
- 产出文件在 `/root/contamcal-irt-calibration/analysis/results/`：2 个 JSON + 4 个 PNG 图表。

---
