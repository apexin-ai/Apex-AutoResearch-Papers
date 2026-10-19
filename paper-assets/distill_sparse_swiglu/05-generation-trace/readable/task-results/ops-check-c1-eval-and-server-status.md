# ops check c1 eval and server status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-c1-eval-and-server-status_20260519T013154_result.json`
- **Structured JSON:** [`ea3596933b26af070d4d.json`](../../sessions/ea/ea3596933b26af070d4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. westd-34887 GPU 占用
| GPU | 状态 | 显存 | 进程 |
|-----|------|------|------|
| cuda:0 | **100% util** | 49099/97887 MiB | PID 68690 (python) |
| cuda:1 | 空闲 | 0 MiB | - |

### 2. c1_ablation_30pct_eval_34887（当前进程）
- **状态：运行中** — tmux session 存活，PID 68680 存活
- 启动于 09:28，当前正在跑 MMLU (~81% loglikelihood requests)
- 已完成：PPL = 9.4463，ARC 已完成
- 待完成：MMLU 剩余 + GSM8K

### 3. c1_ablation_30pct_s42_eval_34887（前一轮 eval，已完成）
**同一 checkpoint，完整结果已出：**

| Metric | Value |
|--------|-------|
| **WikiText-2 PPL** | **9.4463** |
| ARC-Challenge acc | 0.3652 |
| ARC-Challenge acc_norm | **0.4027** |
| WinoGrande acc | **0.6740** |
| MMLU acc | **0.4229** |
| GSM8K exact_match | **0.0758** |

结果已保存至 `results/benchmark/c1_ablation_30pct_s42_eval/results.json`

### 4. c1_ablation_30pct_s42_v2（训练日志）
训练正常完成（925s），最终 BCE=0.0609，sparsity=0.303，agreement=0.975。但训练后内置 eval 因 `TypeError: get_eval_dataset() missing 1 required positional argument` 崩溃（已由独立 benchmark_eval.py 补救）。

### 5. BCE iso-compute checkpoint
**存在** — `/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/predictor_bce.pt`（145MB，May 16）

### 6. westd-41718
| GPU | 状态 |
|-----|------|
| cuda:0 | 空闲（0 MiB）|
| cuda:1 | 空闲（0 MiB）|

无 python 实验进程，仅 jupyter-lab + tensorboard 后台服务。

---

**关键结论：** C1@30% eval 结果已经在前一轮完整跑出。当前进程是重复 eval（同一 checkpoint + 同一参数），可以考虑终止以释放 GPU。两台机器共 3 块 GPU 空闲（34887 cuda:1 + 41718 cuda:0/1）。

---
