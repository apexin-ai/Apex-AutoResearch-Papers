# ssh westd full status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_full_status_check_20260522T162154_result.json`
- **Structured JSON:** [`2f91f0f5799ab1df2dd1.json`](../../sessions/2f/2f91f0f5799ab1df2dd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-32935 GPU 状态

| GPU | 实验 | PID | VRAM | GPU% | 进度 | 预计剩余 |
|-----|------|-----|------|------|------|---------|
| 0 | GSM8K seed123 v2 | 56283 | 26.2GB | 98% | **1030/1319 (78%)** | ~16min |
| 1 | MATH-500 α=2.0 | 57202 | 16.8GB | 99% | **110/500 (22%)** | ~5-7h |
| 2 | MATH-500 α=0.5 | 58276 | 16.7GB | 97% | **89/500 (18%)** | ~5-6h |
| 3 | MATH-500 α=4.0 | 58435 | 17.5GB | 99% | **85/500 (17%)** | ~5-8h |

全部 running，无结果文件。

**关键中间指标：**
- GSM8K seed123 v2: acc=52.40% @ 1000/1319 样本，eos_rate=99.40%，即将完成
- MATH-500 三组 α ablation 刚开始不久（17-22%），速度约 40-70s/it，预计还需 5-8 小时

---
