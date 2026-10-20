# code cost logging

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cost-logging_20260514T054508_result.json`
- **Structured JSON:** [`ffd95692776f0a2da681.json`](../../sessions/ff/ffd95692776f0a2da681.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改点已正确应用。

---

**修改汇总：**

1. **新增 `CostTracker` 类**（第 43 行）— 线程安全，含 `record()` 和 `summary()` 方法
2. **`play_episode()`**（第 198 行）— 增加 `cost_tracker` 参数；每次 API 成功响应后调用 `cost_tracker.record()`；返回值增加 `api_usage` 字典
3. **`run_episode()`**（第 354 行）— 解包 `cost_tracker`，传入 `play_episode()`；轨迹 JSON 增加 `api_usage` 字段（含错误情况的零值兜底）
4. **`main()`**（第 426-465 行）— 创建 `CostTracker`（日志路径与 `output_dir` 同级），通过 tasks 元组传递，结束时打印汇总

**验证结果：**
- `py_compile` 通过
- `--help` 正常输出

**定价配置：**
- `openai/gpt-5.2`: input $2.50/M tokens, output $10.00/M tokens（占位值，与 gpt-4o 相同）
- 如需调整实际定价，修改 `CostTracker.PRICING` 字典即可

---
