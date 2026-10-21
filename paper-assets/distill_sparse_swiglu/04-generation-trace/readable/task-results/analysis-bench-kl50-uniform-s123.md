# analysis bench kl50 uniform s123

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bench_kl50_uniform_s123_20260516T153059_result.json`
- **Structured JSON:** [`2834acc483809bf3e90e.json`](../../sessions/28/2834acc483809bf3e90e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果
- wikitext2_ppl: **11.83**
- arc_challenge_acc: **0.3515** (acc_norm)
- winogrande_acc: **0.6298**
- mmlu_acc: **0.2751**
- gsm8k_acc: **0.0235**
- wandb_run_id: 无（日志中无 wandb 记录）
- 是否正常完成: 是（EXIT_CODE=0）
- 异常/警告: `fatal: not a git repository` (无影响)

## 分析

**Uniform allocation 未解决 downstream 崩溃问题。** 50% sparsity 下 uniform 分配的表现：

| 指标 | Dense baseline | KL50 uniform (本次) | 问题 |
|------|---------------|-------------------|------|
| WikiText-2 PPL | 6.13 | 11.83 | +93% 劣化 |
| ARC-Challenge | ~0.53 | 0.3515 | 严重下降 |
| WinoGrande | ~0.74 | 0.6298 | 明显下降 |
| MMLU | ~0.65 | 0.2751 | ≈随机（崩溃） |
| GSM8K | ~0.46 | 0.0235 | 崩溃（2.4%） |

MMLU 和 GSM8K 仍然崩溃到随机水平，与之前全局 top-k 的问题一致。说明 50% sparsity 对 LLaMA-3.1-8B 来说过于激进——不论是 global 还是 uniform 分配策略都无法保住 downstream 能力。PPL 从 6.13 涨到 11.83 进一步印证模型容量被严重削减。

---
