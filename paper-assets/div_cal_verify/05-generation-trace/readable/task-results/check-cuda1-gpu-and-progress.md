# check cuda1 gpu and progress

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda1_gpu_and_progress_20260514T084558_result.json`
- **Structured JSON:** [`4bbcdd8ed3a11cd0c97d.json`](../../sessions/4b/4bbcdd8ed3a11cd0c97d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. cuda:1 进程

| 项目 | 值 |
|------|-----|
| PID | 462871 |
| 进程 | python3 run_mvp.py |
| 实验 | **medium_external_seed456** (`--method external_only --student_model gpt2-medium`) |
| 显存 | 28738 MiB |
| 启动时间 | 15:11 今天 |

命令行中 `--gpu_ids 0` 实际映射到物理 GPU 1（通过 CUDA_VISIBLE_DEVICES 实现）。

### 2. medium_external_seed456 — 未完成，正常运行中

已完成 gen 0-2，当前 **gen 3/7 step 2/5（数据选择阶段）**，gen_3/synthetic.pt 已于 16:39 生成。

| Gen | Loss | PPL | 耗时 |
|-----|------|-----|------|
| 0 | 1.3818 | 26.08 | 1438s |
| 1 | 0.7460 | 33.59 | 1591s |
| 2 | 0.4573 | 43.23 | 1449s |

- 进度：3/8 = **37.5%**
- 每 gen 约 25 min，剩余 5 gen → 预计还需 **~125 min（约 2 小时）**
- GPU-Util 为 0% 正常：当前在做 contriever embedding + 子模选择（CPU 密集操作）
- 注意：PPL 在上升（26→34→43），loss 在下降 — 可能出现过拟合迹象

### 3. auto_chain_cuda1

`/root/div_cal_verify/auto_cuda1_chain.log` **不存在**。链式触发 random50_seed456 **未配置/未触发**。

### 4. medium_uncurated_seed456 (cuda:0)

- 启动时间：16:30:31（运行约 16 分钟）
- 当前：**Gen 0/7, step 3/5（训练中）**
- 选了全部 974/974 样本（uncurated 不做筛选）
- 预计每 gen ~25 min，8 gen 总计 **~200 min（约 3.3h）**，预计 ~19:50 完成

### 5. 无需清理

两个进程均在正常运行中，无僵尸进程。cuda:1 的 PID 462871 无需处理。

---
