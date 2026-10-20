# pipeline s46 and 8b full

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_s46-and-8b-full_20260522T021547_result.json`
- **Structured JSON:** [`59fc0466d71d5ab4f97b.json`](../../sessions/59/59fc0466d71d5ab4f97b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Phase 1 完成，总结：**

| 项目 | 状态 |
|------|------|
| 残留进程 | 无，GPU 空闲 |
| s45 checkpoint | 已清理 |
| s46 配置 | 已存在且正确（seed=46, K=4, 1000步, `data/train_500_seed42.jsonl`） |
| s46 训练 | 已启动，tmux=`exec-only-s46-1000step`，GPU 8233MiB |
| s46 预计耗时 | ~6.5h（23.6s/step），约北京时间 16:45 完成 |
| 8B dry-run 配置 | 已创建 `grpo_exec_only_8b_dryrun.yaml`（2步） |
| 8B 正式配置 | 已创建 `grpo_exec_only_8b_s42.yaml`（500步, save_total_limit=1） |
| 磁盘 | 148GB free |

**排队：** s46 完成 → eval + classify → 8B dry-run → 8B 正式训练。20 分钟后自动轮询。

---
