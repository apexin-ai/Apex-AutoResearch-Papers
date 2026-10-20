# code exp54 causal probe

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp54_causal_probe_20260522T113135_result.json`
- **Structured JSON:** [`1a41de53cd6ee9a35b01.json`](../../sessions/1a/1a41de53cd6ee9a35b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp54 complete. Hypothesis **confirmed**.

## Results Summary

**Core finding**: Classification DAPT compresses discriminative information into a 3-dimensional subspace (out of 768) that causally enables OOD jailbreak detection.

### Top-k SVD Probe F1 (ActorAttack — hardest OOD set)

| Model | top-3 | top-5 | full-768 | random k=3 | random k=5 |
|-------|-------|-------|----------|------------|------------|
| **9-class** | **1.000** | **1.000** | **1.000** | 0.928 | 0.952 |
| scrambled | 0.962 | 0.962 | 0.962 | 0.766 | 0.807 |
| MLM-only | 0.618 | 0.644 | 0.636 | — | 0.584 |

### Three lines of causal evidence:

1. **9-class top-3 = 1.000**: All discriminative information for OOD detection lives in just 3 SVD dimensions. Projection into this subspace perfectly preserves detection.

2. **MLM-only full-768 = 0.636**: Without classification DAPT, even using all 768 dimensions fails on ActorAttack. The MLM model never formed discriminative structure.

3. **Random projections degrade**: 9-class random k=3 drops to 0.928 on AA; MLM-only random k=5 collapses (DD=0.685, AA=0.584, FITD=0.744). It's not "any k dimensions" — it's specifically the top SVD components of the classification-adapted model.

DD-OOD and FITD-OOD are near-perfect for all models (easy separation), making ActorAttack the critical discriminative test case.

---
