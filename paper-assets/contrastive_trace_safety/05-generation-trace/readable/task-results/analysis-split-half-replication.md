# analysis split half replication

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_split_half_replication_20260519T113523_result.json`
- **Structured JSON:** [`49abd4c852eb2db3a7c8.json`](../../sessions/49/49abd4c852eb2db3a7c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here are the results against the 4 key checkpoints:

---

## Split-Half Layer Selection Replication (OT-7B) — Results

**Setup**: 228 traces → 114 + 114, seed=42, W=1 sweep, W=3 final probes, liblinear

### Checkpoint 1: Shallow vs Deep Metric Disagreement
**Both halves replicate the disagreement pattern.**

| Metric | Half 1 | Half 2 | Zone |
|--------|--------|--------|------|
| ba | L22 | L24 | both deep |
| precision | L22 | L24 | both deep |
| fpr | L11 | L22 | both deep |
| crossing_rate | L0 | L0 | both shallow |
| composite | L0 | L0 | both shallow |

### Checkpoint 2: crossing_rate/composite select shallow?
**Yes.** Both halves select L0 for both crossing_rate and composite. Perfect agreement (|diff|=0).

### Checkpoint 3: precision/FPR select deep?
**Yes.** Precision selects L22/L24 (both deep, |diff|=2). FPR selects L11/L22 (both deep, |diff|=11 — wider spread but still both >= L8).

### Checkpoint 4: HS vs Text ΔPrecision same direction?
**Yes.** Both halves show HS > Text:

| | L_prec | HS_prec | Text_prec | ΔPrec | ΔBA | ΔFPR |
|---|---|---|---|---|---|---|
| Half 1 | L22 | 0.4159 | 0.2350 | **+0.181** | +0.069 | -0.198 |
| Half 2 | L24 | 0.5726 | 0.2234 | **+0.349** | +0.185 | -0.214 |

### Agreement Summary (all True)
- `cr_composite_both_shallow`: **True**
- `threshold_both_deep`: **True**
- `delta_precision_same_direction`: **True**
- `delta_ba_same_direction`: **True**

### Key Observations
1. The metric disagreement pattern is **fully replicable** across independent halves
2. Half 2 shows stronger HS advantage (ΔPrec=+0.35 vs +0.18), suggesting the effect is robust and possibly conservative in the full dataset
3. The shallow/deep split is clean: crossing_rate and composite always prefer L0 (early detection), while precision-based metrics prefer L22-L24 (accuracy-focused)
4. Elapsed: 1455s (~24 min), CPU-only

Output files on server:
- `artifacts/split_half_replication/split_half_results.json` (16KB)
- `artifacts/split_half_replication/report.txt`

---
