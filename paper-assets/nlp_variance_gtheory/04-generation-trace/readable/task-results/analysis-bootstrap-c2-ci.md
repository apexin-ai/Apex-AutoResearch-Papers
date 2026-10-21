# analysis bootstrap c2 ci

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-c2-ci_20260524T100425_result.json`
- **Structured JSON:** [`6db89c86fa84a7812f67.json`](../../sessions/6d/6db89c86fa84a7812f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Benchmark | Type | item-related% | 95% CI |
|-----------|------|--------------|--------|
| MMLU | MC | 68.1% | [65.2, 70.6] |
| ARC | MC | 71.6% | [67.1, 75.0] |
| HellaSwag | MC | 70.3% | [67.1, 72.7] |
| GSM8K | FF | 31.4% | [28.0, 34.4] |
| MATH | FF | 41.3% | [38.0, 44.2] |

**MC vs FF CI 不重叠**：MC 区间最低 65.2%，FF 区间最高 44.2%，间隔约 21 个百分点。MC benchmarks 的 item-related variance 显著高于 FF benchmarks。

---
