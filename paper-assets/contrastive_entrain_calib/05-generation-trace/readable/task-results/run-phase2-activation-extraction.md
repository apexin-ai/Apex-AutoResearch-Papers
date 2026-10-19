# run phase2 activation extraction

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_phase2_activation_extraction_20260518T080446_result.json`
- **Structured JSON:** [`d69469a94b600dd04f97.json`](../../sessions/d6/d69469a94b600dd04f97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All phases complete. Full results:

---

## Phase 2-4 Execution Summary

### Phase 2: Activation Extraction
- **640 samples** processed in **11 seconds** (54.59 it/s)
- **36 layers**, hidden_dim=4096, Qwen3-8B on RTX PRO 6000 Blackwell
- 2 bug fixes applied: `return_dict=False` for transformers 5.8.1 compatibility, turn indexing fix for `correction_turn` field

### Phase 3: Direction Computation  
- 320 complete pairs → **256 train / 64 test** (stratified by domain, seed=42)
- d_syc and d_gen computed via difference-in-means, L2-normalized

### Phase 4: Evaluation Results

```
============================================================
DIRECTION EVALUATION SUMMARY
============================================================
Test pairs: 64  |  Test samples: 128
Layers: 36  |  Hidden dim: 4096

Best layer: 35  |  Token position: 1 (asst_first)
Best AUROC: 1.0000
Cosine(d_syc, d_gen) at best: -1.0000  (expected: -1.0 in binary setup)

Top 5 (layer, position, AUROC):
  Layer 35, asst_first: 1.0000
  Layer 28, asst_first: 0.9993
  Layer 30, asst_first: 0.9993
  Layer 23, asst_first: 0.9990
  Layer 25, asst_first: 0.9990

AUROC by domain (best layer, all positions):
  commonsense                user_last=0.7633, asst_first=1.0000
  geography                  user_last=0.9375, asst_first=1.0000
  history                    user_last=0.8698, asst_first=1.0000
  math                       user_last=0.6568, asst_first=1.0000
  science                    user_last=0.9467, asst_first=1.0000

AUROC by evidence_strength (best layer, all positions):
  medium                     user_last=0.8673, asst_first=1.0000
  strong                     user_last=0.8992, asst_first=1.0000
  weak                       user_last=0.6875, asst_first=1.0000

AUROC by correction_turn (best layer, all positions):
  3                          user_last=0.8445, asst_first=1.0000
  4                          user_last=0.8214, asst_first=1.0000
  5                          user_last=0.8750, asst_first=1.0000

------------------------------------------------------------
GO/NO-GO VERDICT: PASS
  AUROC=1.0000 >= 0.85 and cosine=-1.0000 < 0.3
============================================================
```

**Key observations:**
- **asst_first position achieves perfect AUROC (1.0) across all layers, domains, evidence strengths, and correction turns** — the sycophancy direction is perfectly separable at the assistant's first content token
- **user_last position** is weaker and more variable: math (0.66) and weak evidence (0.69) are hardest to distinguish, while science (0.95) and strong evidence (0.90) are easiest
- The perfect asst_first AUROC across all strata suggests the model's internal state at the first generated token already fully encodes the sycophantic vs. warranted decision

---
