# analysis em exact match freq

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_em_exact_match_freq_20260515T044235_result.json`
- **Structured JSON:** [`20f57b3395de956feb62.json`](../../sessions/20/20f57b3395de956feb62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `review_round2/em_exact_match_freq.json`。

EM pair 频率远非 "negligible"：

| Config | N | Mean EM% | Inst w/ EM% | Global EM% |
|--------|---|----------|-------------|------------|
| qwen_scierc | 529 | 42.45% | 96.8% | 42.4% |
| llama_scierc | 529 | 49.26% | 98.9% | 49.3% |
| qwen_conll | 2756 | 78.35% | 99.6% | 78.3% |
| llama_conll | 2756 | 94.90% | 100.0% | 94.9% |
| wnut17 | 689 | 77.43% | 100.0% | 77.4% |

EM pairs 实际非常频繁，几乎所有 instance 都存在至少一对 exact match。CoNLL/WNUT 上 EM rate 尤其高（77-95%），SciERC 上也有 42-49%。论文中 "probability of exact match negligible" 的说法需要修正——reviewer 的质疑是有道理的。

---
