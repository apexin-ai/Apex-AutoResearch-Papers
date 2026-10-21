# status gpu and tau07 check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_gpu_and_tau07_check_20260519T233140_result.json`
- **Structured JSON:** [`f13365cc0cdcd59d4a72.json`](../../sessions/f1/f13365cc0cdcd59d4a72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## GPU 状态（4× RTX PRO 6000 Blackwell, 96GB）

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| **cuda:0** | 561 MiB / 96 GB | 0% | `eval_ppl_ood.py` (adaptive_fromscratch_seed42 eval，PID 350265) |
| **cuda:1** | 53 GB / 96 GB | 98% | **tau07_seed123** 训练 (PID 344460) + eval 进程 |
| **cuda:2** | 47 GB / 96 GB | 68% | **tau07_seed456** 训练 (PID 344539) + eval 进程 |
| **cuda:3** | 47 GB / 96 GB | 74% | **tau07_seed42** 训练 (PID 345448) + eval 进程 |

PID 350265 是 `adaptive_fromscratch_seed42` 的 **eval 进程**（eval_ppl_ood.py），跨 4 张 GPU 运行但主要在 cuda:0，显存占用不大。

## adaptive_fromscratch_seed42

- **训练已完成** — `model.safetensors` 已保存 (1.19GB, 06:40)
- **Eval 正在运行** — eval_ppl_ood.py 在 cuda:0 上执行 3 个 eval set (holdout/openwebtext/wikipedia)
- cuda:0 训练进程已释放，但 eval 仍在占用

## τ=0.7 训练进度（max_steps = 6103）

| 实验 | GPU | 当前 step | 进度 | 预计剩余时间 |
|------|-----|----------|------|-------------|
| tau07_seed42 | cuda:3 | 4254 / 6103 | **69.7%** | ~70 min |
| tau07_seed123 | cuda:1 | 4424 / 6103 | **72.5%** | ~63 min |
| tau07_seed456 | cuda:2 | 4389 / 6103 | **71.9%** | ~65 min |

（预计时间基于 tmux session 创建时间 04:46-04:50 到当前 07:32 推算，约 26 steps/min）

## 可用 GPU

**目前没有完全空闲的 GPU。** cuda:0 显存占用最低（仅 561 MiB），eval 完成后即可用于新任务。cuda:1/2/3 需等 τ=0.7 训练完成（约 1h 后）才释放。

---
