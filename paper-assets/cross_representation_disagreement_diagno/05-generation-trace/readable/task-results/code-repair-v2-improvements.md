# code repair v2 improvements

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repair_v2_improvements_20260515T065725_result.json`
- **Structured JSON:** [`54603ee22bcb772bc143.json`](../../sessions/54/54603ee22bcb772bc143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。总结：

**改动 1（行 109-115）— error_side=both 跳过 targeted**
- 检测 `other_verdict != ground_truth`，即对方也错了
- 此时对方 verdict 不能做参考信号，直接委托给 `blind_regeneration`
- 无需修改 pipeline.py：信息已经在 `targeted_repair` 的参数里

**改动 2（行 159-171）— Unknown fallback**
- targeted repair 输出 "Unknown" 时，判定为 overcorrection（模型被"你错了"吓退）
- 中止 targeted，剩余轮次 fallback 到 `blind_regeneration`
- `round_num` 做偏移以保持全局轮次编号连续

两项改动向后兼容：函数签名不变，输出数据结构不变。语法检查和 import 验证均通过。

---
