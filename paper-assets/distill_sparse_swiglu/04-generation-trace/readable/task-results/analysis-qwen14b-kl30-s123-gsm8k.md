# analysis qwen14b kl30 s123 gsm8k

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_kl30_s123_gsm8k_20260519T205339_result.json`
- **Structured JSON:** [`44cafe671bc2cc22e796.json`](../../sessions/44/44cafe671bc2cc22e796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据充分，汇总如下。

## 结果

**qwen14b_kl30_s123_gsm8k** — 已完成 (EXIT_CODE=0)

| 指标 | 值 |
|------|-----|
| gsm8k_exact_match (flexible) | **34.42%** (±1.31%) |
| gsm8k_exact_match (strict) | 34.34% (±1.31%) |
| actual sparsity (per-layer) | 0.285–0.301，均值 ~0.297 |
| 样本数 | 1319 |
| 运行时间 | 8842s (~2h27m) |
| W&B run ID | 无（benchmark eval 不上报 W&B） |
| 产出 | `/root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_s123_gsm8k/results.json` |

## 与已有数据对比

| 配置 | GSM8K exact_match | Sparsity |
|------|------------------|----------|
| **KL predictor s123** | **34.42%** | ~29.7% |
| TEAL@27.5% uniform | 57.09% | ~27.5% |
| Dense (无数据) | — | 0% |

**KL predictor 在 GSM8K 上比 TEAL@27.5% 低 22.67pp**，这是一个很大的退化。在其他 6 个 task 上 KL predictor 和 TEAL 差距较小（多数在 ±3pp 内），但 GSM8K（推理任务）退化严重。

## 其他 seed 状态

| 实验 | 状态 | 服务器 |
|------|------|--------|
| qwen14b_kl30_s42_gsm8k_v2 | RUNNING | westd-41718 |
| qwen14b_kl30_s456_gsm8k | RUNNING | westd-41718 |

## 建议 conclusion

**Negative**。KL predictor 在 GSM8K 上表现远差于 TEAL vanilla baseline（34.42% vs 57.09%，-22.67pp）。需等 s42/s456 完成后确认是否为系统性问题。如果三个 seed 一致，则 KL predictor 的 mask pattern 对推理类任务有实质性伤害，论文中 GSM8K 列需要谨慎处理。

---
