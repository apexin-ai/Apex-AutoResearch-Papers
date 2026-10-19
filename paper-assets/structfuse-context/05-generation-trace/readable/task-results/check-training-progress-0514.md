# check training progress 0514

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_progress_0514_20260514T080329_result.json`
- **Structured JSON:** [`ceef0803fc1af27c39d0.json`](../../sessions/ce/ceef0803fc1af27c39d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. m2_full_qwen random_s42 (PID 73558, cuda:0)

| 指标 | 值 |
|------|-----|
| 当前 step | **3500 / 4242** (82.5%, epoch 3) |
| 最新 train loss | 0.0658 |
| 最佳 eval (step 2500) | val_loss=0.5264, recall@1=0.527, recall@5=0.956 |
| 运行时间 | 14h24m (从 01:39 开始) |
| 速度 | ~243 steps/h |
| 预计完成 | **~19:05 CST 今天**（剩余 742 steps, ~3h） |

### 2. m2_full_starcoder random_s42 (PID 76627, cuda:1)

| 指标 | 值 |
|------|-----|
| 当前 step | **2500 / 4242** (58.9%, epoch 2) |
| 最新 train loss | 0.2170 |
| 最佳 eval (step 1500) | val_loss=0.6528, recall@1=0.449, recall@5=0.906 |
| 运行时间 | 13h33m (从 02:30 开始) |
| 速度 | ~184 steps/h |
| 预计完成 | **~01:30 CST 明天**（剩余 1742 steps, ~9.5h） |

### 3. GPU 状态

| GPU | 型号 | 利用率 | 显存 | 温度 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Blackwell | **100%** | 51.6 / 97.9 GB | 73°C |
| 1 | RTX PRO 6000 Blackwell | **100%** | 55.2 / 97.9 GB | 74°C |

### 4. s43 自动启动：**否**

当前 s42 是**手动启动**的（直接 `python train.py --num-epochs 3`），不是通过 launcher 脚本。s42 完成后不会自动启动 s43。

launcher 脚本（`run_m2_full_qwen.sh` / `run_m2_full_starcoder.sh`）确实有 seed 循环（42→43→44）× 3 strategies 的 9-run 结构，且 `--num-epochs 2`。但脚本**未在运行**，不会触发后续 runs。需要手动启动 s43。

### 5. m1_reextract_v2 CodeQL 提取

| 指标 | 值 |
|------|-----|
| 启动时间 | 03:59 CST 今天（12h 前） |
| 总 groups | 82（28276 instances, 4 workers） |
| 已启动 groups | **46 / 82**（56%） |
| 已完成 groups | ~42（4 个正在处理中） |
| 当前处理 | iterative/dvc, pyutils/line_profiler, mozillazg/python-pinyin, gruns/icecream |
| 原始估计 | ~60h（4 workers） |
| 按当前速率估计 | 总计 ~21h，**剩余 ~9-10h**（但剩余 36 groups 的 instance 数量不确定，可能更长） |

---
