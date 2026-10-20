# diagnose w7 qwen scierc ft grammar only

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w7_qwen_scierc_ft_grammar_only_20260516T064258_result.json`
- **Structured JSON:** [`9392385c1017be766913.json`](../../sessions/93/9392385c1017be766913.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：实验成功，监控误报。** 551 个样本全部正确处理，输出文件完整。cron 监控误判原因是 grammar_only 模式为纯 inference，不上报 W&B metrics，且进程正常退出后被当作"死亡"。

报告已写入 `artifacts/w7_qwen_grammar_only_failure_diagnosis.md`。

---
