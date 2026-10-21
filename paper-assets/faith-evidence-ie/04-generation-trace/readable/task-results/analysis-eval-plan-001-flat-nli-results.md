# analysis eval plan 001 flat nli results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_plan_001_flat_nli_results_20260515T175932_result.json`
- **Structured JSON:** [`be14c6e7269dd51ac74e.json`](../../sessions/be/be14c6e7269dd51ac74e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。完整结果如下：

## flat-NLI RSFT Eval 结果

| Metric | flat-NLI | CED (3-seed mean) | SFT baseline | flat-NLI vs CED | flat-NLI vs SFT |
|--------|----------|-------------------|--------------|-----------------|-----------------|
| **rel_f1** | 0.4539 | 0.4596 | 0.4057 | **-0.57pp** | +4.82pp |
| **evi_f1** | 0.8043 | 0.8143 | 0.7979 | **-1.00pp** | +0.64pp |
| **edcr** | 0.6431 | ~0.6350 | 0.7118 | +0.81pp | -6.87pp |
| precision | 0.4671 | — | — | — | — |
| recall | 0.4414 | — | — | — | — |
| format_ok | 100% | — | — | — | — |
| truncated | 199/985 | ~170 | — | — | — |
| predictions | 15,294 | — | — | — | — |

## 关键对比分析

**flat-NLI ≈ CED，CED contrastive margin 对 RSFT filtering 无显著增益。**

- rel_f1 差距仅 0.57pp，在 CED 3-seed 标准差范围内（σ=0.0127）
- 更精确的 seed-matched 对比：flat-NLI seed=42 (0.4539) vs CED seed=42 (0.4449)，flat-NLI 反而**高 +0.90pp**
- evi_f1 差距 1.00pp，同样不显著

**论文影响**：CED 的 contrastive margin 在 RSFT data filtering 场景下不构成关键优势。论文对 CED 的 claim 应聚焦其在 **inference-time reranking**（rel_f1=0.4864, +2.68pp over RSFT mean）和 **GRPO reward signal** 上的价值，而非 RSFT filtering 的 scoring 方式差异。

---
