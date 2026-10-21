# code fix experiment plan registry ids

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-experiment-plan-registry-ids_20260514T063003_result.json`
- **Structured JSON:** [`5678d33223e5a746766c.json`](../../sessions/56/5678d33223e5a746766c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

补全完成。修改汇总：

| plan | 补全的 registry_id | 状态 |
|------|-------------------|------|
| plan_014 | `plan014-downstream-nli-s42` | DONE (negative) |
| plan_016 | `plan016-extended-1000-s42` | RUNNING |
| plan_017 | `plan017-additive-random-s42` | DONE (negative) |

修改后有 registry_id 的 plan：001, 002, 003, 005, 013, 014, 016, 017 = **8/17**（47.1%）。其余 9 个 plan（004, 006-012, 015）在 registry 中无对应实验，属于未启动状态，无需链接。

---
