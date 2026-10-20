# code fix formatter field

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-formatter-field_20260514T082659_result.json`
- **Structured JSON:** [`fec5c5407ee90f483d84.json`](../../sessions/fe/fec5c5407ee90f483d84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**结果**：
- 实际轨迹数据使用 `task_desc` 字段，`task_description` 不存在
- 已修复服务器端 `/root/autodl-tmp/tax_error_inject_agent/data/formatter.py` 和本地副本，兼容两种字段名
- formatter 输出的 SFT 数据第一轮对话正确包含任务描述（如 "Move pump bottle to back of toilet."）

---
