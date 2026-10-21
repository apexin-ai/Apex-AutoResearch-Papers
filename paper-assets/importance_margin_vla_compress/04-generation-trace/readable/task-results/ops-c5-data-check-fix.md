# ops c5 data check fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c5_data_check_fix_20260519T204626_result.json`
- **Structured JSON:** [`d6c0812a9c1a712bdb58.json`](../../sessions/d6/d6c0812a9c1a712bdb58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认：Loaded 500 episodes from 10 files**。训练正在运行。

## 汇报

| 项目 | 状态 |
|------|------|
| **数据文件数量** | 10/10 (已补全) |
| **原缺失文件** | butter, milk, chocolate_pudding, orange_juice (4个) |
| **下载来源** | hf-mirror.com (yifengzhu-hf/LIBERO-datasets) |
| **操作** | kill 旧进程 (PID 43111, 仅 6 files/300 episodes) → 下载 4 缺失文件 → 重启训练 |
| **新训练** | PID 46032, tmux session `c5_roboflamingo_libero_object`, GPU cuda:0 |
| **数据确认** | **500 episodes from 10 files** (之前仅 ~300 episodes from 6 files) |
| **checkpoint 目录** | `/root/autodl-tmp/checkpoints/roboflamingo_libero_c5` |
| **日志** | `/root/autodl-tmp/RoboFlamingo/train_libero_object.log` |

---
