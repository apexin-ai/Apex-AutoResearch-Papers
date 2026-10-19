# analyze perlayer kl k8 s123 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_perlayer_kl_k8_s123_eval_20260523T122132_result.json`
- **Structured JSON:** [`373723313c4a5a8bc058.json`](../../sessions/37/373723313c4a5a8bc058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总如下：

## perlayer_kl_k8_s123_eval 结果

| 指标 | K=8 s123 | K=8 s42 | Δ |
|------|----------|---------|---|
| WikiText-2 PPL | **9.0648** | 8.9704 | +0.094 |
| Sparsity | 0.298 | — | — |
| ARC-Challenge (norm) | 0.4155 | 0.4104 | +0.005 |
| WinoGrande | **0.6993** | 0.674 | **+0.025** |
| MMLU | 0.4042 | 0.398 | +0.006 |
| GSM8K | 0.0682 | 0.0561 | +0.012 |
| HellaSwag (norm) | **0.6997** | 0.6919 | +0.008 |
| PIQA (norm) | 0.7508 | 0.7612 | -0.010 |

- **无错误**，EXIT_CODE=0，耗时 3865s
- **无 W&B run ID**
- Checkpoint: `/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k8_s123/predictor_perlayer_kl_k4.pt`
- 结果 JSON: `/root/distill_sparse_swiglu/results/benchmark/perlayer_kl_k8_s123_eval/results.json`

两个 seed 间差异很小（PPL 差 ~0.1，downstream 各项波动 ≤2.5pp），s123 在 WinoGrande/GSM8K/HellaSwag 上略优于 s42，PIQA 略低。整体一致性好。

---
