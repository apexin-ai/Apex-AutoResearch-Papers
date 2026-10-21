# ops check qwen eval results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_qwen_eval_results_20260516T113115_result.json`
- **Structured JSON:** [`98f3da024590667dfbe2.json`](../../sessions/98/98f3da024590667dfbe2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 结果（已完成）

| 模型 | GSM8K Accuracy | 正确/总数 | stderr | avg_len |
|------|---------------|-----------|--------|---------|
| **RASP (20% prune)** | **72.50%** | 145/200 | ±3.16% | 121.8 |
| **Standard (20% prune)** | **71.00%** | 142/200 | ±3.21% | 127.7 |

RASP 比 Standard 高 1.5pp，但在 stderr 范围内，差异不显著。两者 eos_rate 均为 100%，无截断。

## SFT 25% 进度

| 任务 | GPU | 进度 | 速度 | 预计剩余 |
|------|-----|------|------|---------|
| **sft_rasp_25** | cuda:2 | 502/1870 (27%) | ~1.12 it/s | ~20min |
| **sft_standard_25** | cuda:3 | 465/1870 (25%) | ~1.13 it/s | ~21min |

两个 25% SFT 任务均在正常训练中，loss ~0.70，epoch ~0.5，预计约 20 分钟后完成第一轮。

---
