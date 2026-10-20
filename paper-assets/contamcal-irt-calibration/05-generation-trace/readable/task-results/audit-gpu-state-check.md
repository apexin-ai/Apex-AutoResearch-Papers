# audit gpu state check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_state_check_20260516T152649_result.json`
- **Structured JSON:** [`c05497c424dc63724cae.json`](../../sessions/c0/c05497c424dc63724cae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### GPU 状态 (6× RTX 4090 D, 24GB)

| GPU | 显存占用 | GPU利用率 | 状态 | 进程 |
|-----|---------|-----------|------|------|
| **0** | 0 MiB | 0% | **空闲** | — |
| **1** | 8313 MiB | 82% | 占用 | PID 800570 - `evaluate.py` Llama-3.2-3B_d000_s42 aligned eval (mmlu/gsm8k/arc/humaneval) |
| **2** | 1511 MiB | 37% | 占用 | PID 797754 - `evaluate.py` Qwen2.5-0.5B-Instruct (mmlu/gsm8k/humaneval) |
| **3** | 17853 MiB | 100% | 占用 | PID 801766 - `train_sft.py` Llama-3.2-3B d025_s42 (lr=5e-5, alpha=32 implied) |
| **4** | 8313 MiB | 85% | 占用 | PID 796493 - `evaluate.py` Llama-3.2-3B_d000_s42 aligned eval (重复任务，同 GPU1) |
| **5** | 0 MiB | 0% | **空闲** | — |

### 活跃进程详情

| PID | GPU | 任务 | 启动时间 | 运行时长 |
|-----|-----|------|---------|---------|
| 801766 | cuda:3 | SFT Llama-3.2-3B d025_s42 | 23:07 | ~20min |
| 800570 | cuda:1 | Eval Llama-3.2-3B_d000_s42_aligned | 23:01 | ~25min |
| 797754 | cuda:2 | Eval Qwen2.5-0.5B-Instruct | 22:41 | ~35min |
| 796493 | cuda:4 | Eval Llama-3.2-3B_d000_s42_aligned | 22:37 | ~50min |

### tmux sessions
tmux 命令被 read-only 模式阻止，无法检查。

### 两个 RUNNING 实验状态

- **exp_001_sft_llama32_3B_d025_s42**: **有实际进程** — PID 801766 在 GPU 3 上训练中，日志 `exp_001_sft_llama32_3B_d025_s42.log` 最后更新 23:27（持续写入）
- **exp_001_eval_05B_instruct**: **有实际进程** — PID 797754 在 GPU 2 上跑 Qwen2.5-0.5B-Instruct 评估

### 最近 5 个日志（按更新时间）

1. `exp_001_sft_llama32_3B_d025_s42.log` — 23:27 (活跃)
2. `exp_001_eval_llama32_3B_d000_s42_v2.log` — 23:27 (活跃)
3. `exp_002_signals_15B_s123_batch.log` — 20:42
4. `signals_05B_s123_v2.log` — 20:19
5. `signals_05B_s123_batch.log` — 19:01

### 注意事项

1. **GPU 1 和 GPU 4 跑了同一个 eval 任务**（Llama-3.2-3B_d000_s42_aligned），可能是重复提交
2. 有 8 个 `contam_irt_2pl_` **僵尸进程**（状态 Z, defunct），不占资源但应清理
3. 有 2 个 modelscope 下载进程（PID 752362, 700982）仍在后台挂着，占内存但无 GPU
4. GPU 0 和 GPU 5 完全空闲，可用于新任务

---
