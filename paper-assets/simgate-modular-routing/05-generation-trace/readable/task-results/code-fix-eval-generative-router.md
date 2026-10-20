# code fix eval generative router

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-generative-router_20260514T073837_result.json`
- **Structured JSON:** [`85238ad08141c514fb3c.json`](../../sessions/85/85238ad08141c514fb3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成并验证通过。

**已完成：**

**任务 1 — GenerativeRouter 推理路径：**
- L276: `GenerativeRouter` 类，使用 `AutoModelForCausalLM` + LoRA adapter
- 使用 `GENERATIVE_SYSTEM_PROMPT`（与 `format_implicit_data.py` 一致）构造 chat-template prompt
- `predict_step()`: 生成输出，检查 `[SIMULATE]` 前缀 → deterministic，否则 → internal
- `predict_episode()`: 对所有 step 做 majority vote，返回与 `TrainedRouter` 相同的 `(decision, confidence, detail_dict)` 接口
- L758: `--router_type` 参数（`classification` / `generative`），根据类型选择 Router 类

**任务 2 — Fallback 偏差修复：**
- L524: fallback 时 `logger.warning` 输出触发的 episode key
- L495: `fallback_count` 计数器
- L553-560: 计算 `fallback_rate`，写入 metrics，>10% 打印 WARNING
- L669-676: `print_summary` 中输出 fallback 统计

**验证结果：**
- 语法检查 `SYNTAX OK`
- `--help` 输出包含 `--router_type {classification,generative}`
- 原有 `TrainedRouter` 代码未改动

---
