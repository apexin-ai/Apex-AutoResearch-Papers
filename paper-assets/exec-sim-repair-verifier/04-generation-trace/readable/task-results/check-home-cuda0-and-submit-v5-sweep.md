# check home cuda0 and submit v5 sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-cuda0-and-submit-v5-sweep_20260514T223640_result.json`
- **Structured JSON:** [`c9d29d1b577cf9f1892c.json`](../../sessions/c9/c9d29d1b577cf9f1892c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态清晰了。

## Home cuda:0 状态

**GPU**: cuda:0 100% 占用，31.7/32.6 GB 显存

**正在运行**: `v5-ckpt600 val@5120` eval（已跑 ~13 分钟）

**v5 checkpoints**: 600, 4000, 4200, 4400, 4600

**val@5120 sweep 进度**:
| Checkpoint | val@5120 | 状态 |
|---|---|---|
| ckpt-600 | `repo_cls_v5_ckpt600_val5120` | **运行中** |
| ckpt-4000 | — | 待跑 |
| ckpt-4200 | — | 待跑 |
| ckpt-4400 | — | 待跑 |
| ckpt-4600 | — | 待跑 |

已有的 `repo_cls_v5_ckpt4000/4200/4400/4600` 是之前非 val5120 的 eval 结果。

**不打断当前任务。** ckpt-600 完成后，按优先顺序下一个是 ckpt-4000。需要等 ckpt-600 跑完后再提交。要我设置一个定时检查，等 cuda:0 空闲后自动提交 ckpt-4000 吗？

---
