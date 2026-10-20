# analysis r11 sbert process kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-sbert-process-kappa_20260521T114112_result.json`
- **Structured JSON:** [`49c009127fb15f32349e.json`](../../sessions/49/49c009127fb15f32349e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Metric | Value |
|--------|-------|
| TF-IDF mean cosine sim | **0.7429** ± 0.0803 |
| SBERT mean cosine sim | **0.9066** ± 0.0265 |
| Answer Fleiss' κ | **0.5501** |

SBERT similarity (0.91) 比 TF-IDF (0.74) 更高，两者都远超 answer-level κ (0.55)。使用语义 embedding 不仅不削弱结论，反而强化了 process-level consensus 的发现——CoT 推理过程在语义层面的一致性甚至高于词汇层面。

注：TF-IDF 值 (0.74) 略高于论文中的 0.69，可能因为论文数据包含了更多条件/模型的平均值，而此处仅分析了 Mistral-7B FOLIO-204 单个设置。Answer κ (0.55) 也略高于论文的 0.46，同样可能因为子集差异。核心结论不变：SBERT >> Answer κ。

---
