# code validate calibration v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_validate_calibration_v2_20260518T094636_result.json`
- **Structured JSON:** [`506df25cc029a6225719.json`](../../sessions/50/506df25cc029a6225719.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已生成，语法验证通过。

v1 → v2 主要变更：
- 条件名改为 `valid_correction` / `invalid_pressure`
- 必填字段：`pair_id`（替代 `id`）、新增 `wrong_answer`，移除 `correction_turn`
- 固定 3 turns，角色 user→assistant→user
- 配对检查新增 Turn 1/2 字符级一致、`wrong_answer` 一致
- Turn 3 长度差异 > 20% 触发 WARNING
- Confound 分析：Turn 1/2 差异 > 0 即 ERROR（应完全一致），Turn 3 差异 > 20% WARNING
- LLM 抽样检查适配新的 5 项评估标准

---
