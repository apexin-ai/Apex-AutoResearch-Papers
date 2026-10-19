# ops gpu check urgent v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-urgent-v2_20260516T091431_result.json`
- **Structured JSON:** [`45c42f61d29e47e886a6.json`](../../sessions/45/45c42f61d29e47e886a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
cuda:0: idle (0 MiB / 97887 MiB, 0% util)
cuda:1: idle (0 MiB / 97887 MiB, 0% util)

## d030_kl40_uniform
状态: completed (train 1000 steps + benchmark_eval, EXIT_CODE=0)
Metrics:
| 指标 | 值 |
|------|-----|
| wikitext2_ppl | 8.3627 |
| arc_challenge_acc_norm | 0.4181 |
| winogrande_acc | 0.6717 |
| mmlu_acc | **0.3068** |
| gsm8k_exact_match | 0.0394 |
| actual_sparsity | 0.398 |

Registry: 已更新 (DONE)

## bench_kl30_uniform
状态: completed (eval only, EXIT_CODE=0)
Metrics:
| 指标 | 值 |
|------|-----|
| wikitext2_ppl | 8.8157 |
| arc_challenge_acc_norm | 0.4078 |
| winogrande_acc | 0.6859 |
| mmlu_acc | **0.4061** |
| gsm8k_exact_match | 0.0735 |
| actual_sparsity | 0.300 |

Registry: 已��新 (DONE)

---

**关键发现**: 40% sparsity (d030_kl40_uniform) 的 MMLU 从 30% 的 40.61% 骤降到 30.68%（接近 random guess 25%），确认 allocation 修复的 threshold 在 30%-40% 之间。两张 GPU 均已空闲，可提交下一批实验。

---
