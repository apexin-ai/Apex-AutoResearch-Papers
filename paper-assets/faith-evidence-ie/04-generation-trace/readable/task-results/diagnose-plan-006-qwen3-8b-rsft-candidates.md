# diagnose plan 006 qwen3 8b rsft candidates

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_006_qwen3_8b_rsft_candidates_20260517T015305_result.json`
- **Structured JSON:** [`54f8399fc6f08c19364b.json`](../../sessions/54/54f8399fc6f08c19364b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告在 `artifacts/diagnose_8b_timeout.md`。

核心结论：**8B 完成了 89%（2701/3027），因 12h timeout 不够被 kill。** progress.json 已保存断点，推荐直接重提交同样命令（timeout 设 4h），脚本会自动跳过已完成的 2701 docs，只跑剩余 326 个（预估 1h43m）。

---
