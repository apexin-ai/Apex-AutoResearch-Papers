# ops progress check 20260516T114

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress_check_20260516T114_20260516T115330_result.json`
- **Structured JSON:** [`d2ffe91ccf14c90e4a82.json`](../../sessions/d2/d2ffe91ccf14c90e4a82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-16980 ===
w8_llama_docred_ft_grammar_only: 880/998 (88.2%) [PID 345222 alive, running 3h42m]
DocRED latency benchmark: PID 351214 alive (running 2h16m), 结果文件尚未生成，日志文件不存在

=== westd-21461 ===
w8_qwen_docred_ft_grammar_only: 409/998 (41.0%) [PID 18555 alive, running 2h25m]
w8_qwen_docred_ft_semantic_only: 294/998 (29.5%) [PID 20035 alive, running 1h44m]
```

所有进程均存活。westd-16980 上的 llama grammar_only 接近完成，预计再 ~30-40 分钟跑完。DocRED latency benchmark 仍在运行中但尚无输出文件。westd-21461 两个 qwen 任务还需较长时间。

---
