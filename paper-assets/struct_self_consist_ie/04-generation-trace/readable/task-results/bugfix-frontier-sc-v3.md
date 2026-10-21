# bugfix frontier sc v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_frontier_sc_v3_20260520T220547_result.json`
- **Structured JSON:** [`593ff6c97c9866132dae.json`](../../sessions/59/593ff6c97c9866132dae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 bug 已修复。现在检查 OPENROUTER_API_KEY。

环境变量 `OPENROUTER_API_KEY` 为空。在 worker 日志中找到旧 key `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`，但这是 TUM 代理的 key（`http://47.94.22.126/v1`），任务说该代理已耗尽余额。OpenRouter 原生 key 通常以 `sk-or-` 开头。

**停止并报告**：没有可用的 OpenRouter API key。需要你提供一个有效的 `OPENROUTER_API_KEY`（格式 `sk-or-...`），或者确认旧的 TUM key 是否可以直接用于 `https://openrouter.ai/api/v1`。

### 已完成
- Bug 1 修复：`entity_set()` 传参改为 `.get("entities", [])`（3 处）
- Bug 2 修复：`parse_response()` 增加嵌套 JSON string 容错（data 和 entities 字段）
- Bug 3 修复：`API_BASE_URL` 默认值改为 `https://openrouter.ai/api/v1`
- 旧进程 PID 1509955 已死，无需 kill
- output 目录无 checkpoint（只有 instance_ids.json）

### 待提供
- 有效的 `OPENROUTER_API_KEY`，提供后可继续 smoke test 和全量实验

---
