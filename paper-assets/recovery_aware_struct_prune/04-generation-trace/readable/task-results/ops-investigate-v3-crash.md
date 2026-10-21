# ops investigate v3 crash

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate_v3_crash_20260519T134836_result.json`
- **Structured JSON:** [`56f0e4243b950896d945.json`](../../sessions/56/56f0e4243b950896d945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/v3_crash_investigation.md`。

**结论：正常完成，非 crash。**

- pass_at_1 = 13.41%（22/164）
- 根因：eval 脚本未写 sentinel 文件，reconcile 误报
- median_response_length = 2048 说明大量样本被截断，模型在生成代码前输出了长段思考文本，耗尽 token budget

---
