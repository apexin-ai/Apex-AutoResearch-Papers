# code datagen validator

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_datagen_validator_20260518T045356_result.json`
- **Structured JSON:** [`2f9528f9ac94291de41c.json`](../../sessions/2f/2f9528f9ac94291de41c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入指定路径。覆盖全部 5 类检查：

1. **结构完整性** — JSON 解析、必填字段、枚举值、turn 数量与角色交替
2. **配对一致性** — pair_id 恰好 2 行、双 condition、Turn 1 / domain / ground_truth 一致
3. **分布统计** — domain/evidence/correction_turn/condition 分布 + 交叉分布，domain 不足 50 对或 turn=3 比例偏离时 warn
4. **LLM 抽样检查** — `--check-quality` 启用，调 Anthropic API 评估 ground_truth 正确性、错误答案合理性、施压自然度、对比有效性
5. **文本质量** — 空内容、重复 turn、turn 长度统计、模板痕迹检测

exit code: 0=PASS, 1=WARNING, 2=ERROR。

---
