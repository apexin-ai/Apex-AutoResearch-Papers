# ops progress check all 20260516T112

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress_check_all_20260516T112_20260516T111427_result.json`
- **Structured JSON:** [`a1deddec75cde63075b7.json`](../../sessions/a1/a1deddec75cde63075b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-16980 ===
w8_llama_docred_ft_grammar_only: 717/998 (71.8%) — 运行中
DocRED latency benchmark: ✅ 已完成 — 结果文件 /tmp/latency_benchmark_results.json 已生成
  • unconstrained vs grammar_only: +0.0435s (+1.7%), p<0.000001
  • unconstrained vs semantic_only: +0.0316s (+1.2%), p<0.000001
  • unconstrained vs full_s1: +0.0609s (+2.3%), p<0.000001

=== westd-21461 ===
w8_qwen_docred_ft_grammar_only: 313/998 (31.4%) — 运行中
w8_qwen_docred_ft_semantic_only: 188/998 (18.8%) — 运行中
```

Latency benchmark 已完成，约束解码的额外开销很小（grammar_only +1.7%, semantic_only +1.2%, full_s1 +2.3%），统计显著但实际影响微乎其微。三个推理任务均在正常运行中。

---
