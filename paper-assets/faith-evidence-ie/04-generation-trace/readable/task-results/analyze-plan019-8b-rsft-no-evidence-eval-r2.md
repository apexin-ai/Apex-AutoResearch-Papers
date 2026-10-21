# analyze plan019 8b rsft no evidence eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan019_8b_rsft_no_evidence_eval_r2_20260519T170942_result.json`
- **Structured JSON:** [`2d038c2af65cd7fb0bfc.json`](../../sessions/2d/2d038c2af65cd7fb0bfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
ign_f1: 0.5336
f1: 0.5530
ign_precision: 0.5061
ign_recall: 0.5643
precision: 0.5324
recall: 0.5753
format_compliance_rate: 100.0%
truncated_rate: 310/985 (31.5%)
n_predictions: 20605
n_total: 985
evi_f1_joint (DREEAM): 0.0411
evi_f1 (TP-only): 0.0652
edcr: 0.6207
no_evidence: true (confirmed in config)
seed: 42
wandb_run_id: none

evidence_tax (vs s42 with-evidence 0.5376): -0.40pp
evidence_tax (vs mean with-evidence 0.5414): -0.78pp
conclusion: negative — evidence helps 8B, no positive evidence tax

comparison:
  8B:  no-evi 0.5336 vs with-evi 0.5414 (mean) → tax = -0.78pp (evidence slightly helps)
  1.7B: no-evi 0.4352 vs with-evi 0.5122       → tax = -7.70pp (evidence strongly helps)
```

Evidence acts as CoT for 8B too, but the effect is ~10x smaller than 1.7B. The "evidence tax" hypothesis is not supported — evidence generation helps RE performance at both scales, with diminishing benefit as model size increases. This is consistent with larger models having stronger internal reasoning that partially substitutes for explicit evidence chain-of-thought.

Note: evi_f1 metrics are near-zero as expected (only 30/985 docs produced any evidence fields), confirming `--no_evidence` was correctly applied.

---
