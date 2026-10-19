# ops collect uniform v2 final v3

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-uniform-v2-final-v3_20260518T134730_result.json`
- **Structured JSON:** [`57b62aed792625098f27.json`](../../sessions/57/57b62aed792625098f27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

| 指标 | s123 | s456 |
|------|------|------|
| wikitext2_ppl | 8.8186 | 8.8284 |
| arc_challenge_acc_norm | 0.4710 | 0.4505 |
| winogrande_acc | 0.6961 | 0.6953 |
| mmlu_acc | 0.3763 | 0.3727 |
| gsm8k_exact_match | 0.0705 | 0.0705 |

两个 seed 的 WikiText2 PPL 非常接近（8.82 ± 0.005），WinoGrande 和 GSM8K 几乎一致，ARC-Challenge 有约 2% 的 seed 间波动。结果已写入 `artifacts/kl30_uniform_v2_results.json`，两个实验的 registry 均已更新为 DONE/success 并录入 metrics。

---
