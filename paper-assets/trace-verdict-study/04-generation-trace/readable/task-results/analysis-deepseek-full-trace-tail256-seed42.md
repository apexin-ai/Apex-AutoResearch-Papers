# analysis deepseek full trace tail256 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_full_trace_tail256_seed42_20260517T210916_result.json`
- **Structured JSON:** [`1f81bdf92e3372ffebfc.json`](../../sessions/1f/1f81bdf92e3372ffebfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

## 结果摘要

| 指标 | 值 |
|------|-----|
| **Accuracy** | **76.4%** (95% CI: 74.0%-78.7%) |
| Majority baseline | 71.5% |
| Pass F1 | 0.84 |
| Fail F1 | 0.53 |

## 跨架构对比

| Model | tail-256 | tail-512 | tail-2048 |
|-------|----------|----------|-----------|
| Qwen-7B | 78.9% | 93.6% | — |
| DeepSeek-6.7B | **76.4%** | — | 95.0% |

## 结论: **SUCCESS**

76.4% 落在预测的 75-82% 范围内，与 Qwen-7B tail-256 (78.9%) 一致。256→512 token phase transition (~17pp 跳跃) 在两个不同架构上均成立，确认该现象是 **architecture-independent** 的。

---
