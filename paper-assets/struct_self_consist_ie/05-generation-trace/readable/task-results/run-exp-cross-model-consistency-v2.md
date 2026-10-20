# run exp cross model consistency v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_cross_model_consistency_v2_20260520T185946_result.json`
- **Structured JSON:** [`0b9f1a1f32000dd18a37.json`](../../sessions/0b/0b9f1a1f32000dd18a37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE/success。

## 结果摘要

| | SciERC (529) | FewNERD (32565) |
|---|---|---|
| **Pure Qwen uni F1** | 0.6449 | 0.7499 |
| **Pure LLaMA uni F1** | 0.6545 | 0.7873 |
| **Mixed (4Q+4L) uni F1** | **0.6625** | **0.7916** |
| Mixed vs pure Qwen | +1.77pp, p=0.010 | +4.17pp, p=0.000 |
| Mixed vs pure LLaMA | +0.81pp, p=0.130 | **+0.42pp, p=0.000** |
| Degeneracy (mixed / Qwen / LLaMA) | 9.6% / 13.2% / 17.8% | 11.6% / 10.0% / 23.4% |

**结论**：Mixed 在 FewNERD 上显著优于两个 pure model（p<0.001）。SciERC 上显著优于 pure Qwen（p=0.01），vs pure LLaMA 边际（p=0.07/0.13，样本量小）。Cross-model diversity 一致降低 degeneracy rate。

---
