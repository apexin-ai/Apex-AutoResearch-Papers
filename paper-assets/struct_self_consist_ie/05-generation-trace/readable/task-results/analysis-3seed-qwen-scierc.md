# analysis 3seed qwen scierc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed_qwen_scierc_20260515T051603_result.json`
- **Structured JSON:** [`ca8dd0ff8b9963c1c159.json`](../../sessions/ca/ca8dd0ff8b9963c1c159.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON saved. Here's the summary:

### NER — Qwen/SciERC 3-seed (42, 123, 456)

| Signal | Spearman ρ | AUROC |
|---|---|---|
| Voting Confidence | **0.3861 ± 0.0187** | **0.6968 ± 0.0098** |
| Soft Jaccard | 0.3641 ± 0.0179 | 0.6841 ± 0.0090 |
| Exact Match | 0.3071 ± 0.0076 | 0.6606 ± 0.0103 |
| Fleiss' Kappa | 0.2536 ± 0.0157 | 0.6177 ± 0.0092 |
| Log-probability | 0.2167 ± 0.0125 | 0.6134 ± 0.0015 |

### RE — Qwen/SciERC 3-seed (42, 123, 456)

| Signal | Spearman ρ | AUROC |
|---|---|---|
| Voting Confidence | **0.3088 ± 0.0244** | **0.6581 ± 0.0095** |
| Log-probability | 0.2970 ± 0.0218 | 0.6471 ± 0.0188 |
| Fleiss' Kappa | 0.2903 ± 0.0121 | 0.6493 ± 0.0031 |
| Soft Jaccard | 0.2485 ± 0.0015 | 0.6270 ± 0.0054 |
| Exact Match | 0.1353 ± 0.0157 | 0.5625 ± 0.0128 |

Results saved to `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/qwen_scierc_3seed_summary.json`. Sanity-checked against report.json (seed 42 NER) — all 4 reference values match exactly. Cross-seed standard deviations are tight (σ < 0.025), indicating stable signals. Voting Confidence ranks #1 on both subtasks by ρ.

---
