# check training status loop6

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_status_loop6_20260514T150013_result.json`
- **Structured JSON:** [`625728774557ec136bed.json`](../../sessions/62/625728774557ec136bed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/status_check_loop6.md`。

**摘要**：

| 任务 | 状态 | 进度 | 关键指标 |
|------|------|------|---------|
| **Qwen s43** (cuda:0) | RUNNING | ~950/2810 | R@1=0.5357 @500 |
| **StarCoder s42** (cuda:1) | RUNNING | 3700/4242 | best R@1=0.4604 @2500 |
| **m1_reextract_v2** | RUNNING | 71/82 groups started | 44,173 lines |

注意事项：
- **Qwen s43** 不是从 agent-ml tmux 启动的，日志在 `/root/runs/m2_full_qwen/random_s43.log`（非 `structfuse-context` 路径）
- **StarCoder s42** 预计 1-2 小时内完成，val_loss 已连续 5 次 eval 未改善，s43 会在 s42 结束后由 shell 脚本自动启动
- **Qwen s42** 已完成（best R@1=0.5527），Qwen 明显优于 StarCoder（0.55 vs 0.46）
- 磁盘空间充足（autodl-tmp 65GB, root 21GB）

---
