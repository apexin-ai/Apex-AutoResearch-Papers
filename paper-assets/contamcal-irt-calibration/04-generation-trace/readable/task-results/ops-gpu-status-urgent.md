# ops gpu status urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-urgent_20260516T174821_result.json`
- **Structured JSON:** [`f43c2cf898851940eea6.json`](../../sessions/f4/f43c2cf898851940eea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | PID | 实验 | VRAM | Util% | 运行时间 | 状态 |
|-----|-----|------|------|-------|---------|------|
| 0 | — | — | 0 MiB | 0% | — | **空闲** |
| 1 | 807025 | evaluate.py Llama-3.2-3B_d000_s42 (gsm8k/arc/humaneval, aligned) | 6904 MiB | 80% | 02:14:44 | 运行中 |
| 2 | — | (PID 823705 刚启动 signals_1.5B_arc, CUDA_VISIBLE_DEVICES=2, 但 GPU 尚未分配显存) | 3 MiB | 0% | 00:04:32 | 启动中 |
| 3 | 822390 | evaluate.py Llama-3.2-3B_d025_s42 (mmlu/gsm8k/arc/humaneval, aligned) — PID 822385 wrapper→822390 子进程 | 8304 MiB | 0% | 00:15:10 | 运行中 |
| 4 | 810809 | compute_signals 1.5B-Instruct mmlu | 4242 MiB | 44% | 01:59:34 | 运行中 |
| 5 | 804791 | train_sft Llama-3.2-3B d100_s42 (声明 gpu 0 但实际跑在 GPU 5) | 20580 MiB | 100% | 02:17:17 | 运行中 |

**额外进程（非 GPU）：** PID 818742 — `run_mmlu_domain_gamma_n24.py` (CPU, 运行 45min)

**Dead PIDs：** 804570, 801766

**空闲 GPU：cuda:0** — 完全空闲可用。

**注意：** PID 804791 (SFT d100_s42) 命令行写 `--gpu 0` 但实际占用 GPU 5 (20580 MiB)，说明该训练脚本内部做了 GPU 选择或启动时未设 `CUDA_VISIBLE_DEVICES`，与 C004 约束相关但已在运行中，不影响当前调度。

---
