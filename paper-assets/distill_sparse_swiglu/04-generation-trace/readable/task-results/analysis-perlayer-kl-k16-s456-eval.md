# analysis perlayer kl k16 s456 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k16_s456_eval_20260523T135453_result.json`
- **Structured JSON:** [`38f2da248182c1e19510.json`](../../sessions/38/38f2da248182c1e19510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。K=16 s456 vs s42 对比：

| Metric | s456 | s42 | Δ |
|--------|------|-----|---|
| WikiText-2 PPL ↓ | **8.6550** | 8.6737 | -0.0187 |
| ARC-c acc_norm ↑ | **0.4155** | 0.4104 | +0.0051 |
| WinoGrande acc ↑ | **0.6946** | 0.6843 | +0.0103 |
| MMLU acc ↑ | 0.3873 | **0.4403** | -0.0530 |
| GSM8K exact_match ↑ | 0.0766 | **0.0811** | -0.0045 |
| HellaSwag acc_norm ↑ | **0.7015** | 0.6963 | +0.0052 |
| PIQA acc_norm ↑ | 0.7437 | **0.7590** | -0.0153 |

PPL、ARC-c、WinoGrande、HellaSwag 四项 s456 略优于 s42；MMLU 下降 5.3pp 较显著，PIQA 和 GSM8K 小幅下降。两个 seed 间 MMLU 波动较大，其余指标基本一致。

---
