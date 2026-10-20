# ops gpu status d026

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_d026_20260514T201815_result.json`
- **Structured JSON:** [`d4bcda765f11804c239c.json`](../../sessions/d4/d4bcda765f11804c239c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 全景

| GPU | 显存 | 利用率 | 任务 | 已运行 | 状态 |
|-----|------|--------|------|--------|------|
| **0** | 4.9/24.6 GB | 69% | `compute_signals.py` — 1.5B_d000_s42, gsm8k (embedding+minkpp+selfcritique) | 3m31s | 运行中，mmlu 信号已完成，gsm8k 进行中 |
| **1** | 21.7/24.6 GB | 100% | `train_sft.py` — **0.5B_d100_s123** (lr=2e-4, lora-r=16, lora-alpha=32) | 1m33s | 刚启动，lora_adapter 目录为空 |
| **2** | 0 GB | 0% | — | — | **空闲** |
| **3** | 13.3/24.6 GB | 29% | `train_sft.py` — **3B_d100_s42** (lr=5e-5, lora-alpha=16) | 1h55m | 运行中 |
| **4** | 5.9/24.6 GB | 54% | `evaluate.py` — **1.5B_d025_s42_aligned** (mmlu/gsm8k/arc/humaneval) | 1h53m | 运行中，eval_results 目录仍为空 |
| **5** | 0 GB | 0% | — | — | **空闲** |

**可用 GPU: 2, 5**

---

## seed=123 Checkpoints

| Checkpoint | 状态 |
|-----------|------|
| `Qwen2.5-0.5B_d000_s123` | 已完成（有 lora_adapter + eval 结果） |
| `Qwen2.5-1.5B_d000_s123` | 已完成（有 lora_adapter + eval 结果） |
| `Qwen2.5-3B_d000_s123` | 已完成（有 lora_adapter + eval 结果） |
| `Qwen2.5-0.5B_d100_s123` | **训练中**（GPU 1，刚启动 ~2min） |

s123 系列目前仅有 d000 三个模型完成，d100 仅 0.5B 在训练。

---

## 3B d000 v2 SFT (GPU 5)

`Qwen2.5-3B_d000_v2_s42` — **已完成**（05-15 03:45 写入 lora_adapter + train_config.json），GPU 5 已释放。

---

## exp-004 / exp-005

`/root/autodl-tmp/exp004/` 和 `/root/autodl-tmp/exp005/` **均不存在**，服务器上无相关进程。这两个实验未在此服务器上运行。

---
