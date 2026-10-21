# ops gpu status quick

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-quick_20260514T115720_result.json`
- **Structured JSON:** [`0f1079568fc40c724b76.json`](../../sessions/0f/0f1079568fc40c724b76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态摘要

| GPU | PID | 任务 | 显存 | 运行时间 | 状态 |
|-----|-----|------|------|---------|------|
| **0** | 353390 | exp-002 `compute_signals` 0.5B_d000_s42 mmlu (embedding+minkpp+selfcritique) | 2.1G | 1h11m | 进行中，已产出 5 个 signal 文件 |
| **1** | 336765 | exp-001 eval 1.5B_d000_s42_**aligned** (mmlu/gsm8k/arc/humaneval) | 10.4G | 2h39m | 进行中，output 目录尚空 |
| **2** | 356787 | exp-001 eval 0.5B_d005_s42_**aligned** (mmlu/gsm8k/arc/humaneval) | 3.7G | 42m | 进行中，output 目录尚空 |
| **3** | 319555 | exp-001 train 3B_d100_s42 SFT | 13.3G | **5h02m** | **仍在训练，checkpoint 目录为空（尚未保存 lora_adapter）** |
| **4** | 335351 | exp-001 train 3B_d005_s42 SFT | 21.8G | 2h47m | checkpoint 已有 `lora_adapter/`，可能接近完成 |
| **5** | 342940 | exp-001 eval 3B_d000_s42_**aligned** (mmlu/gsm8k/arc/humaneval) | 9.0G | 2h06m | 进行中，output 目录尚空 |

**关注点**：
- **cuda:1** — 不是之前的 1.5B eval batch，而是新的 aligned 格式 eval。之前的任务应已完成。
- **cuda:3** — 3B d100 SFT 5 小时仍未产出 checkpoint，d100 数据量大（100% dosage），正常但偏慢。eval_3B_d100 tmux 还不会启动，因为训练未完成。
- **cuda:0 (exp-002)** — 正在跑 `compute_signals`，当前处理 mmlu benchmark 的 embedding/minkpp/selfcritique 信号。

---
