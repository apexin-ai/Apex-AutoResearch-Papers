# diag qwen14b s123 eval oom

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen14b_s123_eval_oom_20260519T112652_result.json`
- **Structured JSON:** [`83364985d8bcaec1542f.json`](../../sessions/83/83364985d8bcaec1542f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. nvidia-smi

| GPU | PID | 显存占用 | GPU-Util | 温度 |
|-----|-----|---------|----------|------|
| 0 | 100842 (`s123_eval_v4`) | 63,904 MiB / 97,887 MiB | 0% (batch间隙) | 43°C |
| 1 | 100070 (`s456_eval_v2`) | 72,658 MiB / 97,887 MiB | 100% | 83°C |

### 2. 原始进程状态

- **PID 93142 / 93137** (`qwen14b_kl30_s123_eval`): **已死**，不在 ps 输出中
- **PID 93278** (`qwen14b_kl30_s456_eval`): **已死**

原始进程已被清理，GPU 显存已释放。

### 3. 当前运行的实验

**GPU 0 - `qwen14b_kl30_s123_eval_v4`** (PID 100842, 启动于 19:25 UTC):
- WikiText-2 PPL = **7.6607** (已完成)
- ARC-Challenge: 已完成
- 当前: MMLU loglikelihood **108/4687** (~2%)
- 状态: **正常推进中**

**GPU 1 - `qwen14b_kl30_s456_eval_v2`** (PID 100070, 启动于 19:21 UTC):
- WikiText-2 PPL = **7.6933** (已完成)
- ARC-Challenge, Winogrande, HellaSwag, PIQA: 全部已完成
- 当前: MMLU loglikelihood **3103/4687** (~66%)
- 状态: **正常推进中，接近完成**

### 4. 关键发现

两个新实验的 task list 都是 `wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu`，**已移除 GSM8K generate_until**。这正是避免 OOM 的正确做法（GSM8K 的 `generate_until` 在 14B 模型上显存需求远超 loglikelihood 任务）。

### 5. 采取的行动

**无需任何操作。** 问题已被先前介入解决：
- 原始 OOM 进程已死并释放显存
- 新版 eval (v4/v2) 已在两个 GPU 上正常运行
- 两个 GPU 无冲突，各跑一个实验

### 6. GPU 可用性

- GPU 0: **占用中**（s123_eval_v4 运行中，预计还需 ~40 分钟完成 MMLU）
- GPU 1: **占用中**（s456_eval_v2 运行中，MMLU 66%，预计 ~15 分钟完成）

---
