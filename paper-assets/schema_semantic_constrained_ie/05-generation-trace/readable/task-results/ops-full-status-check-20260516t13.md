# ops full status check 20260516T13

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_check_20260516T13_20260516T131245_result.json`
- **Structured JSON:** [`0e6e66c9285b8d2bf23f.json`](../../sessions/0e/0e6e66c9285b8d2bf23f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

```
=== westd-16980 ===
GPU utilization: [gpu0: 0%, gpu1: 87%]
GPU memory: [gpu0: 0/98GB, gpu1: 17/98GB]

w8_llama_docred_ft_semantic_only: 170/998 (17%) [PID 361202 alive, running 40min]
DocRED latency benchmark: ✅ completed (100 samples each)

  grammar_compile_time: 0.044s
  unconstrained:  mean=21.023s
  grammar_only:   mean=21.366s  (+1.63%)
  semantic_only:  mean=21.912s  (+4.23%)
  full_s1:        mean=22.147s  (+5.35%)

=== westd-21461 ===
GPU utilization: [gpu0: 86%, gpu1: 82%]
GPU memory: [gpu0: 19/98GB, gpu1: 19/98GB]

w8_qwen_docred_ft_grammar_only:  642/998 (64%) [PID 18555 alive, running 3h45m]
w8_qwen_docred_ft_semantic_only: 494/998 (49%) [PID 20035 alive, running 3h04m]
```

DocRED latency benchmark 结果很理想——grammar_only 仅 1.63% overhead，semantic_only 4.23%，full (grammar+semantic) 5.35%。比 SciERC 的 overhead 低很多，说明在长文本场景下约束解码的相对开销更小。

---
