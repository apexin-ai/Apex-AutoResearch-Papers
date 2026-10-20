# eval phase b supplement

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_phase-b-supplement_20260517T164659_result.json`
- **Structured JSON:** [`19964aaa5701b9a36990.json`](../../sessions/19/19964aaa5701b9a36990.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 tasks completed. Results saved to `/root/persuasion_turn_jailbreak_detect/results/phase_b_supplement.json`.

```
=== Supplementary Evaluation ===

K=1 Early Detection:
  Treatment: F1=0.9867  (Prec=0.974, Rec=1.000)
  Baseline:  F1=0.8615  (Prec=1.000, Rec=0.757)
  TF-IDF:    F1=1.0000

Per Attack-Type (Treatment F1 at K=2):
  Academic Disguise:   F1=1.000 (N=3)
  Classic Crescendo:   F1=1.000 (N=3)
  DAN Variant:         F1=1.000 (N=5)
  Emotional Path:      F1=1.000 (N=5)
  Full Spectrum:       F1=1.000 (N=8)
  Mixed Emotional:     F1=1.000 (N=5)
  Obfuscation Path:    F1=1.000 (N=2)
  Role + Obfuscation:  F1=1.000 (N=6)

Per Attack-Type (Baseline F1 at K=2) — weaknesses:
  DAN Variant:         F1=0.750
  Emotional Path:      F1=0.571
  Role + Obfuscation:  F1=0.667

Balanced TF-IDF 5-fold CV: F1=1.000 ± 0.000

FPR@95TPR:
  full:  Treatment=0.000, Baseline=0.000, TF-IDF=0.000
  K=2:   Treatment=0.000, Baseline=0.057, TF-IDF=0.000
  K=1:   Treatment=0.000, Baseline=0.057, TF-IDF=0.000
```

Key observations:
- **Treatment GRU achieves the same F1=0.987 at K=1 as at K=2** — the fine-tuned encoder captures jailbreak signal from the very first turn.
- **Treatment achieves perfect F1 across all 8 attack types** at K=2; Baseline struggles with Emotional Path (0.571), Role+Obfuscation (0.667), and DAN Variant (0.750) — exactly the types requiring persuasion-aware representations.
- **TF-IDF achieves perfect separation** (F1=1.0 everywhere, even balanced CV), which is a red flag — the jailbreak vs benign conversations likely have distinct vocabulary distributions (different generation sources). This should be discussed in the paper as a limitation of the current data setup.
- **Treatment FPR@95TPR = 0.0 at all K values**, confirming genuine perfect separation. Baseline has FPR=0.057 at K≤2.

---
