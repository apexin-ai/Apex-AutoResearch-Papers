# infra p2b monitor setup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p2b_monitor_setup_20260512T123817_result.json`
- **Structured JSON:** [`a809619f8924c208df0c.json`](../../sessions/a8/a809619f8924c208df0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告如下：

## P2b 训练状态

### 进程状态：已崩溃

| 项目 | 详情 |
|------|------|
| **PID** | 92651 (python train.py) / 92646 (bash run_p2b_all.sh) — **均已退出** |
| **GPU** | cuda:4（崩溃前 99% 利用率，8084MiB） |
| **运行方式** | submit_training_job (job: p2b-all-9runs) |
| **进度** | Run 1/9 (p2b_random_s42)，**step 200 时崩溃** |
| **崩溃原因** | 根分区 100% 满（30G/30G，仅剩 2.4M），`torch.save` 写 checkpoint 失败 |

### 崩溃前训练指标（p2b_random_s42）

| Step | Loss | Val Loss | Recall@1 |
|------|------|----------|----------|
| 50 | 0.3609 | 0.3494 | 0.677 |
| 100 | 0.0913 | 0.1363 | 0.858 |
| 150 | 0.0101 | 0.0640 | 0.929 |
| 200 | 0.0000 | 0.0832 | 0.945 |

### 磁盘空间分析

| 路径 | 大小 | 说明 |
|------|------|------|
| `/root/structfuse/checkpoints/dryrun/` | **12G** | 旧 dryrun checkpoint，可清理 |
| `/root/structfuse/checkpoints/p2b_random_s42/` | 1.4G | 崩溃时写入的部分 checkpoint |
| `/root/structfuse/models/` | 7.1G | 基础模型 |
| 根分区总计 | 30G (100%) | 已满 |
| `/root/autodl-tmp/` | **112G 可用** | 数据盘，应把 checkpoints 存这里 |

### 日志文件

- 主日志: `/tmp/p2b_all_runs.log`
- Run 日志: `/tmp/p2b_p2b_random_s42.log`
- Job 日志: `~/runs/structfuse-context/p2b-all-9runs.log`

### 修复方案

1. 删除 `checkpoints/dryrun/`（12G）释放空间
2. 把 `--output-dir` 改到 `/root/autodl-tmp/structfuse/checkpoints/` 下
3. 删除损坏的 `p2b_random_s42/checkpoint-200/`
4. 重新启动 9-run 训练

需要我执行修复并重启训练吗？

---
