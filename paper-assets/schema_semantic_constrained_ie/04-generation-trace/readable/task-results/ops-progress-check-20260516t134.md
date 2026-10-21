# ops progress check 20260516T134

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress_check_20260516T134_20260516T145835_result.json`
- **Structured JSON:** [`0c39b541db8fad4c9ec3.json`](../../sessions/0c/0c39b541db8fad4c9ec3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-16980 ===
w8_llama_docred_ft_semantic_only:
  PID: alive (2h26m, cuda:1)
  GPU util: 87%, 16.9/97.9 GB
  Progress: 582/998 (58.3%)
  Last log: [488/998] Peace on Earth/Little Drummer Boy: OK E=24 R=10 11.7s
  ETA: ~1.5h

=== westd-21461 ===
w8_qwen_docred_ft_grammar_only:
  PID: alive (5h31m, cuda:0)
  GPU util: 86%, 18.9/97.9 GB
  Progress: 943/998 (94.5%)
  Last log: [823/998] O'Shaughnessy Dam (Ohio): OK E=13 R=15 13.7s
  ETA: ~20min

w8_qwen_docred_ft_semantic_only:
  PID: alive (4h49m, cuda:1)
  GPU util: 85%, 18.9/97.9 GB
  Progress: 777/998 (77.9%)
  Last log: [656/998] Brazil–Pakistan relations: FAIL E=0 R=0 76.9s
  ETA: ~1.4h
```

三个实验都在正常运行。`grammar_only` 即将完成（~20min），另两个预计 1.5h 左右。

---
