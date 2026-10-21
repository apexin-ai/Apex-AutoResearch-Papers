# eval 1 7b uniform adaptive cuda01

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_1_7b_uniform_adaptive_cuda01_20260520T141318_result.json`
- **Structured JSON:** [`45a4238e21ca1c8657be.json`](../../sessions/45/45a4238e21ca1c8657be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## Eval Results: 1.7B Models (seed42, v5)

| Metric | uniform | adaptive | Δ |
|--------|---------|----------|---|
| **eval_ppl_holdout** | 13.28 | **13.27** | -0.01 |
| downstream_arc_easy_acc_norm | **0.7235** | 0.7176 | -0.006 |
| downstream_arc_challenge_acc_norm | 0.4334 | **0.4403** | +0.007 |
| downstream_hellaswag_acc_norm | 0.6107 | **0.6164** | +0.006 |
| downstream_piqa_acc_norm | 0.7432 | **0.7443** | +0.001 |
| downstream_winogrande_acc | **0.6172** | 0.6069 | -0.010 |
| **downstream_mean** | **0.6256** | 0.6251 | -0.0005 |

Holdout PPL 几乎相同（13.28 vs 13.27）。Downstream 上 adaptive 在 arc_challenge/hellaswag/piqa 略优，uniform 在 arc_easy/winogrande 略优，mean 差异 <0.001，基本持平。Registry 已更新。

---
