# analysis sj union normalizer

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sj_union_normalizer_20260515T201939_result.json`
- **Structured JSON:** [`3bedd5e7fdd1dbfe5cac.json`](../../sessions/3b/3bedd5e7fdd1dbfe5cac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SJ Normalizer Comparison (R8-W3)

| Dataset | Model | n | ρ(SJ_max) | ρ(SJ_union) | Δρ |
|---------|-------|---|-----------|-------------|-----|
| CoNLL NER | Qwen3-8B | 8 | 0.1222 | 0.1223 | -0.0001 |
| CoNLL NER | Qwen3-4B | 8 | 0.1597 | 0.1593 | +0.0004 |
| SciERC NER | Qwen3-8B | 8 | 0.3658 | 0.3694 | -0.0036 |
| SciERC NER | Qwen3-4B | 8 | 0.4269 | 0.4263 | +0.0006 |
| CoNLL NER | LLaMA-8B | 8 | 0.1752 | 0.1752 | -0.0000 |
| SciERC NER | LLaMA-8B | 8 | 0.3013 | 0.3040 | -0.0027 |

**Conclusion**: All |Δρ| < 0.01 (max = 0.0036). The choice of normalizer does not affect the ranking conclusion.

两种 normalizer 的 Spearman ρ 差异极小（最大 |Δρ| = 0.0036，出现在 SciERC/Qwen3-8B），6 组实验全部 < 0.004。结果和 JSON 已保存到 `output/review_round8/r8w3_sj_normalizer_comparison.json`。

---
