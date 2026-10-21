# ssh check westd 34887 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_34887_status_20260520T124806_result.json`
- **Structured JSON:** [`edb88a679851b3aea682.json`](../../sessions/ed/edb88a679851b3aea682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. GPU 占用

| GPU | 状态 | 显存 | 利用率 | 温度 |
|-----|------|------|--------|------|
| cuda:0 | **占用中** | 54025 / 97887 MiB | 100% | 76°C |
| cuda:1 | **空闲** | 3 / 97887 MiB | 0% | 28°C |

### 2. Python 进程

唯一的 python 训练进程（PID 212478）在 cuda:0 上运行 Mistral KL30 s123 训练。

### 3. Mistral KL30 s123 训练状态

- **进度**：Step **840/1000**（84%），约还剩 160 步
- **指标趋稳**：loss ~0.095, KL ~0.095, sparsity ~0.28-0.29, lambda=5000, constraint=0
- **Checkpoint 目录**：`checkpoints/mistral_kl30_s123/` 目前为空（尚未保存 checkpoint，应在训练结束时生成）
- **启动方式**：nohup（符合 C002 约束），训练完成后会自动链式运行 `benchmark_eval.py` 评估
- **日志**：`~/runs/distill_sparse_swiglu/mistral_kl30_s123.log`
- **预计还需**：按当前速率（~30分钟跑了840步），约 5-6 分钟完成训练，之后进入 eval 阶段

### 4. 40% Global Eval v2 结果

已完成（2026-05-20 18:53），LLaMA-3.1-8B, TEAL global_topk 40% sparsity：

| 指标 | 值 |
|------|-----|
| WikiText2 PPL | **10.14** |
| ARC-C (acc_norm) | 39.51% |
| WinoGrande | 67.48% |
| MMLU | 39.47% |
| GSM8K | 6.6% |
| HellaSwag (acc_norm) | 67.79% |
| PIQA (acc_norm) | 72.69% |

### 5. cuda:0 可用性

**cuda:0 当前不可用**。Mistral KL30 s123 训练正在使用，预计还需约 5-6 分钟完成训练 + eval 时间（eval 7 个 benchmark 通常需 30-60 分钟）。**cuda:1 空闲**，可以考虑在 cuda:1 上启动 Mistral s456。

---
