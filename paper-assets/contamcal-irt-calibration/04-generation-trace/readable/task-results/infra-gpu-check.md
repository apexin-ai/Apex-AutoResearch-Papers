# infra gpu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check_20260516T033703_result.json`
- **Structured JSON:** [`5e9563405b24fe451dba.json`](../../sessions/5e/5e9563405b24fe451dba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 (2026-05-16 11:37 UTC)

### cuda:0 — IDLE
- 显存: 0 MiB / 24564 MiB, 0% util
- 无进程

### cuda:1 — ACTIVE
- 显存: 8985 MiB / 24564 MiB, 68% util
- PID **676497** | tmux: `exp_001_eval_3B_d000_s42_a32_batch`
- 命令: `evaluate.py` — Qwen2.5-3B_d000_s42 aligned eval (mmlu/gsm8k/arc/humaneval)
- 进度: **GSM8K 52% (687/1319)**, ~1h28m elapsed, ETA ~1h25m
- 注: 任务提到的 PID 676487 是 parent shell，676497 是实际 python 进程

### cuda:2 — ACTIVE
- 显存: 8985 MiB / 24564 MiB, 67% util
- PID **679190** | tmux: `exp_001_eval_3B_d005_s42_a32_batch`
- 命令: `evaluate.py` — Qwen2.5-3B_d005_s42 aligned eval (mmlu/gsm8k/arc/humaneval)
- 进度: **GSM8K 43% (573/1319)**, ~1h14m elapsed, ETA ~1h40m
- 注: 任务提到的 PID 679180 是 parent shell，679190 是实际 python 进程

### cuda:3 — ACTIVE
- 显存: 8985 MiB / 24564 MiB, 71% util
- PID **687347** | tmux: `exp_001_eval_3B_d100_s42_a32_batch`
- 命令: `evaluate.py` — Qwen2.5-3B_d100_a32_s42_v3 aligned eval (mmlu/gsm8k/arc/humaneval)
- 进度: **GSM8K 15% (203/1319)**, ~25min elapsed, ETA ~2h18m
- 注: 这是 batch 命令，aligned eval 完成后还会跑 para_aligned eval

### cuda:4 — ACTIVE
- 显存: 6873 MiB / 24564 MiB, 65% util
- PID **689315** | tmux: `exp_002_signals_3B_v9`
- 命令: `compute_signals.py` — Qwen2.5-3B_d100_a32_s123, signal **s4** (mmlu)
- 进度: **Self-critique chunk [1000:2000] 16% (79/500)**, chunk 1 [0:1000] 已完成，共 3 chunks（14042 items）
- 注: 这是 3B 信号任务，不是之前担心的未授权进程

### cuda:5 — ACTIVE
- 显存: 2187 MiB / 24564 MiB, 27% util
- PID **687036** | tmux: `exp002_05B_s123_v2`
- 命令: `compute_signals.py` — Qwen2.5-0.5B_d000_s123, signal **all** (mmlu)
- 进度: **Self-critique chunk [2000:3000] 81% (405/500)**

### 其他 tmux sessions（无 GPU 占用）
- `exp_001_sft_0pct_05B` — May 12 创建的旧 SFT 任务，已完成，无 GPU 进程
- `exp_001_eval_3B_d100_v2_para_aligned` — 空闲 shell（显示 AutoDL 欢迎页），无 GPU 进程

### 总结
- **cuda:0 空闲**，可用于新任务
- cuda:1~3 跑 3B eval（d000/d005/d100），cuda:3 还需最久（~4.5h 含 para_aligned）
- cuda:4 跑 3B d100_a32_s123 信号 s4
- cuda:5 跑 0.5B d000_s123 信号 all，接近完成当前 chunk

---
