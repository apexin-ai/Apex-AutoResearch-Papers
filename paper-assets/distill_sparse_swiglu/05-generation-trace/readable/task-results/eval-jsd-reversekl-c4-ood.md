# eval jsd reverseKL c4 ood

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_jsd_reverseKL_c4_ood_20260517T080825_result.json`
- **Structured JSON:** [`99290b0bf2d95833dfdc.json`](../../sessions/99/99290b0bf2d95833dfdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个评估均完成。C4 validation (OOD) PPL 结果汇总：

| Condition | C4 PPL | Δ vs Dense |
|---|---|---|
| Dense | 9.21 | baseline |
| **Forward KL** | **18.40** | **+99.8%** |
| **Reverse KL** | **19.93** | **+116.4%** |
| **JSD** | **26.16** | **+184.0%** |
| TEAL | 38.75 | +320.8% |

排序：Forward KL > Reverse KL > JSD > TEAL。Forward KL 在 OOD 上泛化最好，JSD 退化较严重但仍大幅优于 TEAL。这与 in-distribution 的趋势一致，Forward KL 的 OOD 优势更加显著。

---
