# ops unixcoder status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unixcoder_status_check_20260516T072740_result.json`
- **Structured JSON:** [`884ba6d888f8da64a2c3.json`](../../sessions/88/884ba6d888f8da64a2c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 修复完成。汇报：

## 状态总结

| 项目 | 状态 |
|------|------|
| **PID 149872** | 已死（中间子进程） |
| **父脚本 PID 149863** | 存活，运行 1h24m，`run_unixcoder_3strategies_s42.sh` |
| **当前训练 PID 154017** | 存活，`embedding_distance_s42`，34min |
| **GPU** | cuda:0，13550 MiB |

## 3-strategy 进度

| Strategy | 状态 | 最佳 R@1 | val_loss |
|----------|------|----------|----------|
| random_s42 | ✅ 完成 | 0.5534 | 0.4592 |
| embedding_distance_s42 | 🔄 运行中 step 600/1414 | 0.5497 | 0.4466 |
| dataflow_aware_s42 | ⏳ 排队 | - | - |

## Registry 修复

- `unixcoder-3strat-s42`: PREPARING → **RUNNING** ✅
- `unixcoder_3strat_s42`: 保留 DONE/failed（可能是早期失败尝试，不动）

---
