# monitor westd cuda0 ckpt1000 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-cuda0-ckpt1000-status_20260515T010714_result.json`
- **Structured JSON:** [`8978e8849815e10af869.json`](../../sessions/89/8978e8849815e10af869.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## seetacloud-westd-4x5090 状态

### cuda:0 — eval_repo_cls.py 正在运行

| 项目 | 值 |
|------|-----|
| PID | 310119 |
| 启动时间 | 09:03（约4分钟前） |
| GPU 显存 | 19232 MiB / 32607 MiB |
| GPU 利用率 | 99% |
| 进度 | **1270 / 9335**（~13.6%） |
| running_acc | **88.0%** |
| 速率 | ~1 sample/s |
| 预计剩余 | ~2.2 小时 |

参数：`--checkpoint_dir checkpoint-1000 --split val --max_seq_length 8192 --batch_size 1`

### 其他 GPU

| GPU | PID | 任务 |
|-----|-----|------|
| cuda:1 | 295794 | train_repo_verifier 8B s42 resume（从 ckpt-600 继续） |
| cuda:2 | 266816 | train_repo_verifier 8B seed42 v2（从 ckpt-3000 继续） |
| cuda:3 | 266449 | train_repo_verifier 8B seed123（从 ckpt-3000 继续） |

---

## home-1x5090 状态

### 4B v5 ckpt-4400 eval — 正在运行

| 项目 | 值 |
|------|-----|
| PID | 3193462 |
| 运行时间 | **21分30秒** |
| GPU 显存 | 31718 MiB / 32607 MiB |
| GPU 利用率 | 100%，温度 85°C |
| 命令 | `eval_repo_cls.py --checkpoint_dir checkpoint-4400 --split val --max_seq_length 5120` |
| 输出目录 | `results/repo_cls_v5_ckpt4400_val5120` |

日志文件未找到标准路径（可能直接输出到 stdout 或 nohup.out），但进程活跃、GPU 满载，eval 在正常运行。

---
