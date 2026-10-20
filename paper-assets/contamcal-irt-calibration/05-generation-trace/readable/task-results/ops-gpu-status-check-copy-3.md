# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260514T102311_result.json`
- **Structured JSON:** [`4d73e9670b7e25563bc5.json`](../../sessions/4d/4d73e9670b7e25563bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览

| GPU | 显存使用 | PID | 进程 | 启动时间 |
|-----|---------|-----|------|---------|
| 0 | 2769/24564 MiB | 346944 | exp_002: `compute_signals.py` Qwen2.5-0.5B_d000_s42/gsm8k | 18:22 |
| 1 | 5857/24564 MiB | 336765 | exp_001 eval: `evaluate.py` Qwen2.5-1.5B_d000_s42 (mmlu/gsm8k/arc/humaneval, aligned) | 17:18 |
| 2 | 3695/24564 MiB | 332221 | exp_001 eval: `evaluate.py` Qwen2.5-0.5B_d000_s42 (mmlu/gsm8k/arc/humaneval, aligned) | 16:39 |
| 3 | 13341/24564 MiB | 319555 | exp_001 SFT: `train_sft.py` Qwen2.5-3B_d100_s42 | 14:55 |
| **4** | **21818/24564 MiB** | **335351** | **exp_001 SFT: `train_sft.py` Qwen2.5-3B_d005_s42** | **17:11** |
| 5 | 8985/24564 MiB | 342940 | exp_001 eval: `evaluate.py` Qwen2.5-3B_d000_s42 (mmlu/gsm8k/arc/humaneval, aligned) | 17:52 |

## 重点回答

- **cuda:4**：被占用。PID 335351，`train_sft.py` 训练 Qwen2.5-3B_d005_s42，显存 21.8GB/24.5GB，`CUDA_VISIBLE_DEVICES=4` 确认。
- **exp_001_sft_d005_3B (PID 335346)**：PID 335346 是启动 wrapper（bash），实际训练进程是 PID 335351，运行在 **cuda:4**。
- **exp_002_signals_05B (PID 346325)**：正在 cuda:0 上运行。任务 1/9 (mmlu) 失败，当前在跑 2/9 (gsm8k)。子进程 PID 346944。

---
