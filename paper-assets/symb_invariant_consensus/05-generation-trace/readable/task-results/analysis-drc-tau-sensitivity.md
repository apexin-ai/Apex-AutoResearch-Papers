# analysis drc tau sensitivity

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_drc-tau-sensitivity_20260522T012940_result.json`
- **Structured JSON:** [`4692030b86bfa7ba815c.json`](../../sessions/46/4692030b86bfa7ba815c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已出。

## DRC τ Sensitivity 分析结果

### 数据源
- **exp033**: Mistral-7B / FOLIO-204 (204 problems, 12 traces each)
- **exp036**: Qwen2.5-14B / FOLIO-204 (204 problems)
- **exp032**: Qwen2.5-14B / ProofWriter-600 (600 problems)
- **Verifier 替代**: 无独立 NLI verifier 的 per-problem 预测数据，用 **SICA answer** 作为 verifier proxy

### Mistral-7B / FOLIO-204
| τ | Accuracy | Routed→V | SC Coverage | Δ vs SC |
|---|----------|----------|-------------|---------|
| 0.50 | 56.86% | 7.8% | 92.2% | +0.98pp |
| 0.60 | 58.82% | 27.0% | 73.0% | +2.94pp |
| **0.70** | **59.31%** | **38.2%** | **61.8%** | **+3.43pp** |
| 0.80 | 59.31% | 50.5% | 49.5% | +3.43pp |
| 0.90 | 59.31% | 68.1% | 31.9% | +3.43pp |
| 1.00 | 59.31% | 81.4% | 18.6% | +3.43pp |

SC baseline: 55.88% | SICA: 59.31%

### Qwen2.5-14B / FOLIO-204
| τ | Accuracy | Routed→V | SC Coverage | Δ vs SC |
|---|----------|----------|-------------|---------|
| 0.50 | 75.98% | 1.5% | 98.5% | -0.00pp |
| 0.60–0.80 | 75.98% | 10.8–23.0% | 77–89% | -0.00pp |
| 0.90–1.00 | 75.49% | 30.9–41.7% | 58–69% | -0.49pp |

SC baseline: 75.98% | SICA: 75.49%

### Qwen2.5-14B / ProofWriter-600
| τ | Accuracy | Routed→V | SC Coverage | Δ vs SC |
|---|----------|----------|-------------|---------|
| 0.50 | 73.50% | 1.5% | 98.5% | -0.50pp |
| 0.60 | 72.00% | 16.5% | 83.5% | -2.00pp |
| 1.00 | 71.50% | 63.2% | 36.8% | -2.50pp |

SC baseline: 74.00% | SICA: 71.50%

### Pareto 观察

1. **Mistral FOLIO 存在 sweet spot**: **τ=0.7** 是最优 Pareto 点——达到 SICA 满分 accuracy (+3.43pp vs SC)，仅 38.2% 被路由到 verifier。τ 更高不再提升 accuracy，只增加 routing cost。

2. **Qwen2.5 上 DRC 无效**: SC 本身已经接近/超过 SICA accuracy。Routing 到 SICA verifier 反而掉分。原因是 Qwen2.5 agreement 分布高度集中在 =1.0（FOLIO 58.3%，PW 36.8%），低 agreement 的 case 少，且 SICA 在这些 case 上并不比 SC 更准。

3. **结论**: DRC 在弱模型（Mistral-7B）上有效——高 disagreement 信号可靠地识别出 SC 错误的 case。强模型（Qwen2.5-14B）本身 agreement 就高，DRC 没有空间发挥。

结果已保存到 `/root/symb_invariant_consensus/results/drc_tau_sensitivity.json`。

---
