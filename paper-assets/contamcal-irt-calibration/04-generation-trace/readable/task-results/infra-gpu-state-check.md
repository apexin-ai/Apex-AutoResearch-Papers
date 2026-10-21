# infra gpu state check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-state-check_20260515T231852_result.json`
- **Structured JSON:** [`05a4ff8e67738e7567ac.json`](../../sessions/05/05a4ff8e67738e7567ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. GPU 进程映射

| GPU | 显存占用 | 利用率 | PID | 实验 | 运行时间 |
|-----|---------|--------|-----|------|---------|
| **0** | 23258/24564 MiB | 100% | 642763 | eval_3B_d100_s123_a32_batch (GSM8K 34%) | 1h43m |
| **0** | — | — | 643167 | sft_3B_d005_s42_a32 (42%) | 1h41m |
| **1** | 13341/24564 MiB | 22% | 628668 | sft_3B_d100_s42_a32_v3 (64%) | 3h07m |
| **2** | 6891/24564 MiB | 60% | 652259 | signals_3B_v7 (d005_s123, selfcritique mmlu 2%) | 14m |
| **3** | 18686/24564 MiB | 95% | 654561 | **⚠️ 未注册** compute_signals d000_v2_s42/gsm8k/s4 | 3m |
| **3** | — | — | 655069 | **⚠️ 未注册** sft_3B_d025_a32_s42 | 1m |
| **4** | 7535/24564 MiB | 57% | 648627 | signals_3B_v5 (d100_s42/mmlu 运行中) | 3h35m |
| **5** | 18665/24564 MiB | 38% | 633041 | sft_3B_d000_s42_a32 (79%) | 2h47m |

### 2. 空闲 GPU
**无** — 全部 6 张 GPU 在用。

### 3. 信号完成度

**0.5B / 1.5B** — 全部完成 (4 dose × 3 bench × 所有信号类型)

**3B** (部分完成):

| 条件 | mmlu | gsm8k | arc_challenge |
|------|------|-------|---------------|
| d000_v2_s42 | emb+minkpp+constat ✓ | emb+minkpp+constat ✓, **s4 运行中** (cuda:3) | emb+minkpp+constat ✓ |
| d005_s42 | emb+minkpp ✓ | emb+minkpp ✓ | emb+minkpp+selfcritique+merged ✓ |
| d025_v3_s42 | emb+minkpp ✓ | emb+minkpp ✓ | emb+minkpp ✓ |
| d025_s42 | selfcritique+merged ✓ | — | — |
| d100_s42 | emb+minkpp ✓ | — | — |
| d005_s123 | emb+minkpp ✓, **selfcritique 2%** (cuda:2) | — | — |

### 4. eval batch (d100_s123, cuda:0)
**未完成** — 第一轮 aligned eval 正在跑 GSM8K (456/1319, 34%, ~10.7s/it)。GSM8K 完成后还需跑 para_aligned 第二轮。预计 GSM8K 剩余 ~2.5h，总完成 ~5-6h。

### 5. d000_s123 checkpoint
**存在** — adapter_model.safetensors (119MB) + 完整配置文件。

### 6. SFT 训练进度

| 实验 | GPU | 进度 | 速率 | 预计剩余 |
|------|-----|------|------|---------|
| d000_s42 | cuda:5 | 2483/3125 (79%) | ~4.0s/step | **~43m** |
| d100_s42_v3 | cuda:1 | 2680/4159 (64%) | ~4.2s/step | **~1h42m** |
| d005_s42 | cuda:0 | 1319/3177 (42%) | ~4.8s/step | **~2h28m** |
| ⚠️ d025_a32_s42 | cuda:3 | 刚启动 (1m) | — | 未知 |

### ⚠️ 警告：cuda:3 有两个未注册进程

- **PID 654561**: compute_signals d000_v2_s42/gsm8k/s4 (selfcritique)，运行 3 分钟
- **PID 655069**: SFT d025_a32_s42，运行 1 分钟

两个进程共享 cuda:3 (合计 ~18.7GB)，来源不明（可能是其他 session 或 auto-loop 触发）。违反 C001/C003。需确认是否为合法任务，否则建议 kill。

---
