# ops m2 pilot check and data transfer

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m2-pilot-check-and-data-transfer_20260513T043709_result.json`
- **Structured JSON:** [`51b263d7b428a98148a9.json`](../../sessions/51/51b263d7b428a98148a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 任务 A: m2_early_pilot 训练状态

**状态：random 策略卡住，embedding_distance 和 dataflow_aware 尚未开始**

PID 795791 仍在运行（已 2h45m），但日志最后更新于 12:37（约45分钟前），进程在 step 4000 后疑似卡住。

wrapper 脚本 `run_m2_pilot.sh` 顺序运行 random → embedding_distance → dataflow_aware，设了 `set -e`，当前仍卡在第一个策略 random。

**random 策略训练进度（CUDA_VISIBLE_DEVICES=4）：**

| eval step | val_loss | recall@1 | recall@5 | recall@10 |
|-----------|----------|----------|----------|-----------|
| 1500 | **0.5879** (best) | 0.4693 | 0.4693 | 0.4693 |
| 2000 | 0.7089 | 0.4398 | 0.4398 | 0.4398 |
| 2500 | 0.6961 | 0.4291 | 0.4291 | 0.4291 |
| 3000 | 0.7280 | 0.4104 | 0.4104 | 0.4104 |
| 3500 | 0.7022 | 0.4439 | 0.4439 | 0.4439 |

best checkpoint 已保存（6.2GB model.pt，step ~1500 时）。

**问题：**
1. **recall@1/5/10 全部相同** — eval 代码有 bug，recall@k 没有正确区分 k 值
2. **进程疑似卡死**：step 4000（epoch 3 最后一步）后无新日志，VmRSS 只有 2.7GB，wchan=0（CPU 活跃但无产出），可能在 final eval 或 model save 时 hang 住
3. **OOM 干扰**：另一个进程曾尝试在同一 GPU 上启动并 OOM 崩溃（GPU 0 共 23.5GB，795791 占 9.12GB + 该进程 13.41GB），可能导致 GPU 状态异常
4. **3个策略只跑了 1/3**：embedding_distance 和 dataflow_aware 均未启动

### 任务 B: SCP m2_pilot_data

**已跳过**。PID 795791 仍在运行（尽管可能卡住）。

m2_pilot_data 已确认：879MB，5个文件（train_random.jsonl 253M, train_embedding.jsonl 286M, train_dataflow.jsonl 250M, val.jsonl 90M, dataflow_graph.json 42M）。

### 建议操作

进程大概率卡住。需要你决定：是否 kill PID 795791 并重新启动训练（同时修复 recall@k eval bug）？

---
