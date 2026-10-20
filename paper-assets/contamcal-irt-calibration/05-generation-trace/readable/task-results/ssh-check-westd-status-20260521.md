# ssh check westd status 20260521

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_status_20260521_20260521T073305_result.json`
- **Structured JSON:** [`245de0e7d521cfda950b.json`](../../sessions/24/245de0e7d521cfda950b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个目录都是空的（size=6 表示只有目录本身）。汇总如下：

---

## westd-29999 状态

### GPU 占用（4× NVIDIA RTX PRO 6000 Blackwell, 98GB each）

| GPU | PID | 显存 | 利用率 | 启动时间 | 任务 |
|-----|-----|------|--------|---------|------|
| 0 | 492703 | 20.3GB | 91% | 15:13 (~20min) | **gemma-2-9b d000_s0** GSM8K eval |
| 1 | 481803 | 32.7GB | 93% | 14:03 (~1.5h) | **Qwen2.5-14B d100_s0** GSM8K eval ← 目标实验 |
| 2 | 492186 | 32.7GB | 93% | 15:12 (~21min) | **Qwen2.5-14B d050_s0** GSM8K eval |
| 3 | 493644 | 31.7GB | 100% | 15:13 (~20min) | **phi-4 d000_s0** GSM8K eval |

### eval_qwen14b_d100_gsm8k_s0 状态
- **进程正在运行**：PID 481803，GPU 1，已运行约 1.5 小时
- **输出目录** `/results/gsm8k_eval/qwen14b/d100_s0/` 已创建但为空（尚未写出结果）
- 已完成的 qwen14b dosage：d000_s0、d005_s0、d025_s0（均在 13:37-13:40 完成）

---

## cqa1-21977 状态

- **GPU**：1× RTX 4090D (24GB)，完全空闲（0MB 占用，0% 利用率）
- **无运行中的 Python 进程**

---
