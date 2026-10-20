# ops read all results fast

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-all-results-fast_20260521T153800_result.json`
- **Structured JSON:** [`f3aa1cf2c6c5833bc45a.json`](../../sessions/f3/f3aa1cf2c6c5833bc45a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== OLMo-2 RERUN ===
d000 mmlu: PARSE_ERR%
d000 arc: PARSE_ERR%
d005 mmlu: PARSE_ERR%
d005 arc: PARSE_ERR%
d025 mmlu: PARSE_ERR%
d025 arc: PARSE_ERR%
d050 mmlu: PARSE_ERR%
d050 arc: PARSE_ERR%
d100 mmlu: NOT_READY
d100 arc: NOT_READY
=== GSM8K ===
llama3 d000 gsm8k: PARSE_ERR%
llama3 d025 gsm8k: PARSE_ERR%
llama3 d100 gsm8k: PARSE_ERR%
=== GPU ===
0, 0 %, 0 MiB
1, 0 %, 0 MiB
2, 0 %, 0 MiB
3, 95 %, 16707 MiB
=== PROCS ===
   PID STAT     ELAPSED
GSM8K procs done
```

OLMo-2 d000-d050 和 GSM8K 三个都 PARSE_ERR（JSON key 不匹配），d100 mmlu/arc NOT_READY。GPU 3 活跃（95%, 16.7GB），其余空闲。GSM8K 三个进程已结束。

---
