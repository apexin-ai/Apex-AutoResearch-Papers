# validate move vs put admissible

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_move-vs-put-admissible_20260514T154927_result.json`
- **Structured JSON:** [`54b1377d667e83a04e70.json`](../../sessions/54/54b1377d667e83a04e70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确。最后确认 RAGEN env.py 是否有 action 映射逻辑（已从之前读取的代码确认没有）。

## move vs put 验证结果

- **admissible_commands 包含 move: YES** — 15 seeds × 10 steps 中找到 8 个唯一 move 命令（如 `move candle 1 to countertop 1`）
- **admissible_commands 包含 put: NO** — 0 个 put 命令
- **RAGEN env.py 是否做 action 映射: NO** — `step()` 直接透传 action 给 alfworld，无任何替换逻辑
- **Expert data 格式: `move X to Y`** — 与 admissible_commands 格式一致，无 `put` 动作

**结论: 数据兼容。** Expert trajectory 中的 `move X to Y` 与 ALFWorld env 的 admissible_commands 格式完全匹配。不需要 move→put 后处理。

注意：虽然任务描述文本用 "put"（如 "Your task is to: put a handtowel in garbagecan"），但实际可执行的 admissible action 是 `move`，不是 `put`。

---
