# paper writing related work

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260518T102014_result.json`
- **Structured JSON:** [`881becac70b3c84cb5e9.json`](../../sessions/88/881becac70b3c84cb5e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File written. Summary of changes:

**Structure**: 4 subsections → 3 subsections
- **VLA Robustness** (~0.4 page): Training-time (SRPO, RobustVLA, DiG-Flow, TT-VLA) and inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) methods, with A2C2 positioned as closest concurrent work via threefold comparison
- **Residual Policy Learning** (~0.3 page): Silver 2018, TRANSIC, PLD, DRC; magnitude control as underexplored axis; ACR-VLA's supervised L2 loss vs RL distinction
- **Inference-Time Compute Scaling** (~0.3 page): Snell et al., RoVer, DA-SIP; ACR-VLA's K-value curve as embodied AI instantiation

**D058 corrections applied**:
- All references to "Mahalanobis scoring" and "conformal selection" removed from ACR-VLA's selection description → replaced with "L2 argmin" / "candidate closest to the sample mean by L2 distance"
- Removed "Conformal Prediction in Robotics" standalone section entirely
- Removed "Uncertainty Quantification for VLAs" standalone section entirely
- Conformal features mentioned only once, as perdof ablation (line 24)
- No claim that ACR-VLA "builds upon" CGS

**Style compliance**: zero em-dashes, zero explanatory en-dashes, zero -ing participial phrase endings, zero blacklisted AI words.

---
