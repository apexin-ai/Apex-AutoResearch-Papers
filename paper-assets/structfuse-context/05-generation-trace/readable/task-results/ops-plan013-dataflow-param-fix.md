# ops plan013 dataflow param fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan013-dataflow-param-fix_20260513T090915_result.json`
- **Structured JSON:** [`c647982182de326fc475.json`](../../sessions/c6/c647982182de326fc475.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

auto_start 还在等待 PID 27234（embedding 任务）完成，尚未启动 dataflow retry 脚本。修复是及时的。

**汇报：**
- `run_plan013_dataflow_retry.sh` 第35行 `--num-train-epochs` 已修正为 `--num-epochs`
- 其他 `run_*.sh` 脚本无同样 bug
- auto_start (PID 38446) 仍在等 embedding 任务结束，尚未触发带 bug 的脚本，无需 kill 重启

---
