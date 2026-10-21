# ops status check 3exp

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_3exp_20260518T151203_result.json`
- **Structured JSON:** [`194bb3d7f5cd53875fb4.json`](../../sessions/19/194bb3d7f5cd53875fb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实验状态汇报

### 实验 1: pythia_seed43_001 (gpu-6000pro-2 cuda:1) — **已完成**

完成时间：`2026-05-18 22:48:28 CST`

**summary.json 完整结果：**

| 指标 | 值 |
|---|---|
| **4-class accuracy** | **0.7884** |
| **95% CI** | [0.7813, 0.7952] |
| **d1 vs d2 AUC** | 0.8759 |
| delta vs baseline | +0.0064 (baseline 0.782) |

**Per-class recall：**

| d0 | d1 | d2 | d3 |
|---|---|---|---|
| 0.992 | 0.8248 | 0.5882 | 0.7486 |

**5-fold accuracies：** 0.8015, 0.7855, 0.786, 0.7932, 0.7758

**Top features：** var_surprisal, p90_ppl, mean_ppl, var_ppl, mean_surprisal

GPU 1 已释放（0 MiB / 0% util）。

---

### 实验 2: qwen25_14b_scale_002 (gpu-6000pro-2 cuda:0) — **运行中**

tmux session 名: `qwen25_14b_scale`

**当前阶段：Phase 3.3b — d3 生成**（pipeline 约第 7/8 步）
- d2 LoRA 训练已完成：train_loss=0.2223, 3 epochs, runtime=2329s
- d3 生成进度：**2765 / 5000 samples = 55.3%**
- 生成速率：~13.8 samples/min（从 19:53 开始）
- **预计剩余 d3 生成时间：~2.7 小时**
- d3 生成后还需：feature extraction + classifier training + eval

GPU 0: 32385 MiB / 88% util（PID 806751）

**注意：** `~/runs/recursive_gen_depth_est/qwen25_14b_scale_002.log` 内容是 5/17 的模型下载失败日志（aria2 SSL 错误），不是当前实验日志。实际进度在 tmux pane 中。

---

### 实验 3: qwen25_14b_scale_003 (westd-48862 cuda:0) — **运行中**

**当前阶段：Phase 3.3b — d3 生成**（pipeline 约第 7/8 步）
- d2 LoRA 训练已完成：train_loss=0.2141, 3 epochs, runtime=2422s
- d3 生成进度：**667 / 5000 samples = 13.3%**
- 生成速率：~13.3 samples/min（从 22:23 开始）
- **预计剩余 d3 生成时间：~5.4 小时**
- d3 生成后还需：feature extraction + classifier training + eval

GPU 0: 32381 MiB / 92% util（PID 20700）

tmux pane 输出为空白（进度条在 \r 覆盖），但日志和文件写入均正常。

---

### GPU 总览

| 服务器 | GPU 0 | GPU 1 |
|---|---|---|
| gpu-6000pro-2 | 32385 MiB / 88% (qwen_002) | **空闲** |
| westd-48862 | 32381 MiB / 92% (qwen_003) | **空闲** |

---

### 总结

- **pythia_seed43_001**：已完成，4-class acc = 0.7884，d2 recall 偏低 (0.5882)
- **qwen25_14b_scale_002**：d3 生成 55%，预计 ~2.7h 后完成生成，之后还有 eval 步骤
- **qwen25_14b_scale_003**：d3 生成 13%，预计 ~5.4h 后完成生成，比 002 晚启动约 2.5h
- gpu-6000pro-2 的 GPU 1 空闲可用

---
