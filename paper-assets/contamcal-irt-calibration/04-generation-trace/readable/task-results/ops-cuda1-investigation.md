# ops cuda1 investigation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1-investigation_20260515T175925_result.json`
- **Structured JSON:** [`ffcce66f845fb390d9c3.json`](../../sessions/ff/ffcce66f845fb390d9c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## 报告

### 1. cuda:1 冲突 — 不存在冲突

PID 593740 和 593745 是**同一个 v2 实验的进程树**：
- 593740 (bash wrapper) → 593744 (timeout/bash) → 593745 (python 训练进程)
- 只有 593745 占用 GPU 显存 (13332 MiB)
- **无需 kill 任何进程**

### 2. 全 GPU 训练进度

| GPU | 实验 | Step/Total | 进度 | 速度 | 预估剩余 | 状态 |
|-----|------|-----------|------|------|---------|------|
| 0 | sft_3B_d100_s123_a32_v2 | 1238/4159 | 30% | ~4.2s/it | ~3h27m | 正常 |
| 1 | sft_3B_d100_s42_a32_v2 | 1284/4159 | 31% | ~4.0s/it | ~3h10m | 正常 |
| 2 | eval_3B_d005_s123_aligned | GSM8K 1249/1319 | 94% | ~8s/it | GSM8K ~9min，后续还有 arc_challenge+humaneval | 运行中 |
| 3 | eval_3B_d025_s123_aligned | HumanEval 117/164 | 71% | ~7.4s/it | ~6min（最后一个 benchmark） | 即将完成 |
| 4 | sft_3B_d000_v3 (s42) | 869/3125 | 28% | ~4.9s/it | ~3h04m | 正常 |
| 4 | compute_signals d005_s42 gsm8k | 刚启动(1min) | - | - | - | 新任务，与 d000 共享 GPU |
| 5 | sft_3B_d025_v3_s42 | 1532/3384 | 45% | ~5.0s/it | ~2h34m | 正常 |

### 3. 异常

- **GPU 4 双进程共享**：PID 601354 已死亡，被新进程 PID 605267 (compute_signals d005_s42) 替换（576 MiB）。d000 v3 训练 + signal 计算同时跑在 GPU 4，可能互相拖慢。
- **d025 v3 无 ~/runs/ 日志**：此进程直接启动（非 agent framework wrapper），日志在 checkpoint 目录 `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/train.log`。
- **旧 d025 s42 a32 OOM 崩溃**：`exp_001_sft_3B_d025_s42_a32.log` 显示 `torch.OutOfMemoryError`，EXIT_CODE=1，已死。
- **d005 eval libnvJitLink.so.13 警告**：`OSError: libnvJitLink.so.13 cannot open shared object file`，但 eval 继续运行未受影响。
- **所有 SFT 训练 loss 正常**（1.0-1.3 范围），无 loss 爆炸或 NaN。

---
