# ssh b2 entity verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b2-entity-verifier_20260520T095520_result.json`
- **Structured JSON:** [`916db7661bfd32e0cb93.json`](../../sessions/91/916db7661bfd32e0cb93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. Here's the complete summary:

---

## B2 Entity-Level Verifier — Results

**Setup**: 28,140 instances across 13 configs (4 CoNLL, 4 SciERC, 5 FewNERD). 122,984 entity candidates (51.4% positive). Train on CoNLL+SciERC (44,486 entities), test on FewNERD (78,498 entities).

### Model Quality
| Metric | XGBoost | LightGBM |
|--------|---------|----------|
| 5-fold CV AUC (train) | 0.9273 ± 0.0027 | 0.9254 ± 0.0029 |
| Test AUC (FewNERD) | 0.8282 | 0.8335 |

Cross-dataset AUC drop (~0.10) is expected given different entity type distributions.

### Feature Importance (XGBoost gain)
1. **vc** (text-based vote count): 0.5296 — dominant feature
2. **agreement_count** (span-based): 0.2504 — second strongest
3. dataset_enc: 0.06, entity_type_enc: 0.027, lp_span: 0.025

As predicted, agreement/vote count features are by far the strongest signals.

### Baselines vs Verifier Paths (FewNERD test, micro F1)

| Method | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| Greedy | 0.7185 | 0.7463 | **0.7321** |
| MajVote(>50%) | 0.7652 | 0.6731 | 0.7162 |
| MajVote(>25%) | 0.6944 | 0.7605 | 0.7259 |
| **Path A (LGB, t=1.0)** | 0.7316 | 0.7356 | **0.7336** |
| Path B (XGB, ft=0.1) | 0.7671 | 0.6715 | 0.7162 |

### Key Findings
- **Path A (LGB) slightly beats greedy** (0.7336 vs 0.7321 F1), the only method to do so
- **Path B acts as a precision booster**: at ft=0.5 precision reaches 0.83 but recall drops to 0.46
- On training data, Path B with XGB (ft=0.5) achieves F1=0.8122, significantly above greedy (0.776) and MV (0.783) — the verifier works well in-domain
- The cross-dataset gap suggests the verifier learns some dataset-specific patterns

### Recommendation
- **Path A** is the recommended approach — it balances precision/recall and slightly exceeds greedy
- **Path B** is useful when high precision is needed (e.g., ft=0.3 gives P=0.79 R=0.60 F1=0.68)
- The verifier adds most value over greedy on 72B configs (ZS/FS), less on 7B FT where greedy is already strong

---
