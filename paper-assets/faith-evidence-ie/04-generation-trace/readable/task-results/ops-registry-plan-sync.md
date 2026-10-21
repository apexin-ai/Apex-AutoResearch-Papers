# ops registry plan sync

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_plan_sync_20260519T221007_result.json`
- **Structured JSON:** [`fdee87c7b9c85e7a4712.json`](../../sessions/fd/fdee87c7b9c85e7a4712.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### Part 1: Registry 补全

| 新建 registry | exp_id | status | conclusion |
|---|---|---|---|
| plan_020 | `plan_020_mechanistic_analysis` | DONE | success |
| plan_021 | `plan_021_deep_error_analysis` | DONE | success |

### Part 2: experiment_plan.yaml 同步

**所有 31 个条目均新增了 `status` 字段**（之前没有此字段），与 registry 对齐：

| status | 数量 | 条目 |
|---|---|---|
| done | 25 | plan_001-009, 011-012, 014-016, 019-021, mvp1/sft/rsft/grpo, w3/d112/w18 |
| running | 2 | plan_010 (nli_large_ablation), plan_017 (14b_rsft_generate) |
| planned | 3 | plan_018, plan_022, plan_023 (无 registry) |
| cancelled | 1 | plan_013 (D104 取消) |

**plan_020/021 额外修改**: `registry_id` 从 `null` 更新为新创建的 exp_id。

**无不一致**：所有有 registry_id 的条目，其 registry 状态与预期匹配。

---
