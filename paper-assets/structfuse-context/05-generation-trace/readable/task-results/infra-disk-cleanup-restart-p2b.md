# infra disk cleanup restart p2b

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk_cleanup_restart_p2b_20260512T125741_result.json`
- **Structured JSON:** [`c94557a94d0e1885e182.json`](../../sessions/c9/c94557a94d0e1885e182.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| 磁盘清理 | dryrun (12G) + p2b_random_s42 (1.4G) 已删除，根分区 `/` 当前 9.2G/30G (31%) |
| 数据盘目录 | `/root/autodl-tmp/structfuse/checkpoints` 和 `wandb` 已创建，数据盘 87G 可用 |
| 脚本修改 | `CKPT_DIR` 已改为 `/root/autodl-tmp/structfuse/checkpoints` |
| 训练提交 | PID=99055, tmux session=`mvp_p2b_contrastive_training`, 已启动 run 1/9 (p2b_random_s42) |
| 日志 | `~/runs/structfuse-context/mvp_p2b_contrastive_training.log` |
| 超时 | 14 小时 |

---
