# analysis r13 ba layer modality

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r13_ba_layer_modality_20260518T143902_result.json`
- **Structured JSON:** [`a0076fe576a05b5ba9c2.json`](../../sessions/a0/a0076fe576a05b5ba9c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here's the summary:

## R13: BA-Selected Layers HS vs Text Modality Comparison

**BA-optimal layers** (threshold-free, pure balanced accuracy selection):
- R1-8B: L12 | OT-7B: L9 | R1-32B: L47 (LOO) | QwQ-32B: L30 (LOO)

**Result: HS > Text on all 4 models, all 4 metrics (16/16 HB-corrected p < 0.05)**

| Model | BA-L | HS Prec | Text Prec | dPrec | p_adj | HS FPR | Text FPR | dFPR | p_adj | HS BA | Text BA | dBA | p_adj | HS AUC | Text AUC | dAUC | p_adj | HB |
|-------|------|---------|-----------|-------|-------|--------|----------|------|-------|-------|---------|-----|-------|--------|----------|------|-------|----|
| R1-8B | L12 | .767 | .589 | +.178 | .004 | .121 | .250 | -.129 | .004 | .777 | .699 | +.078 | .004 | .945 | .852 | +.093 | .004 | Y |
| OT-7B | L9 | .532 | .277 | +.254 | .004 | .125 | .318 | -.193 | .004 | .756 | .639 | +.117 | .004 | .881 | .733 | +.148 | .004 | Y |
| R1-32B | L47 | .628 | .491 | +.137 | .004 | .249 | .480 | -.231 | .004 | .758 | .609 | +.149 | .004 | .932 | .722 | +.211 | .004 | Y |
| QwQ-32B | L30 | .668 | .489 | +.180 | .006 | .196 | .276 | -.080 | .041 | .796 | .648 | +.148 | .004 | .896 | .722 | +.173 | .004 | Y |

**Interpretation**: HS advantage is robust across layers and metrics. Even when layers are selected purely by BA (threshold-free), HS probes significantly outperform text probes on precision, FPR, BA, and AUROC for all 4 models. This eliminates metric circularity as a concern. Weakest signal: QwQ FPR (adj_p=0.041), all other 15 tests p <= 0.006.

Results saved to `artifacts/r13_ba_layer_modality/results.json` on server and registered as artifact.

---
