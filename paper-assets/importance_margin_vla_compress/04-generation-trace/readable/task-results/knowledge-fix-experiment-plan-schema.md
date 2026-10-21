# knowledge fix experiment plan schema

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_fix_experiment_plan_schema_20260519T204654_result.json`
- **Structured JSON:** [`1dbe31a492a81a0d1f46.json`](../../sessions/1d/1dbe31a492a81a0d1f46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

YAML 格式验证通过。6 个 plan entries，共 67 个 exp_id 关联，所有必需字段（`plan_id`, `claim`, `description`, `status`, `exp_ids`）完整。

转换完成：`claims` 嵌套结构 → `experiments` 扁平列表，保留了所有实验关联信息和 claim 映射。`compute_coverage_matrix` 现在应能正确解析。

---
