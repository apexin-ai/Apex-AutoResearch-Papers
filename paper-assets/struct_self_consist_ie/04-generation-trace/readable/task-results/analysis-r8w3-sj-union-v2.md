# analysis r8w3 sj union v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8w3_sj_union_v2_20260515T215512_result.json`
- **Structured JSON:** [`a3afec279bdb66c1241c.json`](../../sessions/a3/a3afec279bdb66c1241c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Dataset | Model | n | ρ(SJ_max) | ρ(SJ_union) | Δρ | p_max | p_union |
|---------|-------|---|-----------|-------------|-----|-------|---------|
| CoNLL NER | Qwen3-8B | 2756 | 0.4357 | 0.4376 | -0.0019 | 4.71e-128 | 2.74e-129 |
| CoNLL NER | Qwen3-4B | 2756 | 0.4217 | 0.4212 | +0.0004 | 3.07e-119 | 5.64e-119 |
| SciERC NER | LLaMA-8B | 529 | 0.3630 | 0.3719 | -0.0089 | 6.41e-18 | 8.57e-19 |
| SciERC NER | Qwen3-4B | 529 | 0.4221 | 0.4234 | -0.0014 | 2.89e-24 | 1.98e-24 |

**验证通过**：所有 4 个实验的 ρ(SJ_max) 与 registry 参考值一致（最大偏差 0.0007）。SJ 实现和 consistency.py 完全一致（max_diff=0.0）。

**结论**：所有 |Δρ| < 0.01（最大 0.0089，出现在 SciERC LLaMA-8B）。分母选择 `max(|g_i|, |g_j|)` vs `|g_i ∪ g_j|` 对 Spearman ρ 的影响可忽略，不改变任何排序结论。

结果已保存到 `output/review_round8/r8w3_sj_union_v2.json`。

---
