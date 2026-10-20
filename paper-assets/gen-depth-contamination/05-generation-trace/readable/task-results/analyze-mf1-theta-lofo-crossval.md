# analyze mf1 theta lofo crossval

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mf1-theta-lofo-crossval_20260518T153609_result.json`
- **Structured JSON:** [`24bc0f925d95957794d4.json`](../../sessions/24/24bc0f925d95957794d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results

**C4 LOFO (primary)**: 8/9 agreement (89%). θ=0.60 is not circular.

| Held-out | θ̂ | K* match |
|----------|------|---------|
| Pythia | 0.5914 | all Y |
| OLMo | 0.5914 | all Y |
| Qwen | 0.5725 | 4/5 Y (mvp_pilot → K*=3) |
| LLaMA | 0.5914 | Y |
| Mistral | 0.6004 | Y (K*=1 preserved) |

- Derived θ̂ range: **[0.5725, 0.6004]**, θ=0.60 falls within it
- Only mismatch: Qwen-1.5B-RW (rewrite mode), whose AUC₂ᵥ₃=0.5893 is the highest in the dataset and sits 0.011 below θ=0.60

**arXiv**: 6/6 (100%). θ=0.60 from C4 correctly predicts K*=3 for all non-OLMo models.

**Wikipedia**: 1/6 (17%). Formula breaks down due to OLMo's chance-level AUC deflating θ̂. This is a limitation of the gap formula in domains with heterogeneous K*, not of θ=0.60 itself.

Outputs:
- `artifacts/theta_crossval/theta_lofo_table.tex` (C4 table + combined 3-domain table)
- `artifacts/theta_crossval/summary.md` (full analysis with data sources)

---
