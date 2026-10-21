# analysis fdr correction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fdr_correction_20260517T195613_result.json`
- **Structured JSON:** [`891387a392bb9b586738.json`](../../sessions/89/891387a392bb9b586738.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All four analyses complete. Here are the results:

---

## FDR Correction Results (Benjamini-Hochberg, Wilcoxon signed-rank, 10 tasks paired, 33 layers L0-L32)

### 1. RSA trained vs untrained (image_mean)

**25/33 layers significant after FDR (q<0.05)**

| Significant | L1-L21, L29-L32 |
|---|---|
| **Not significant** | **L0, L22-L28** |

| Layer | mean_diff | p_raw | q_fdr | sig |
|-------|-----------|-------|-------|-----|
| L0 | 0.0000 | 1.000000 | 1.000000 | |
| L1 | 0.0412 | 0.009766 | 0.013428 | * |
| L2-L15 | 0.05-0.08 | 0.001953 | 0.004958 | ** |
| L16-L20 | 0.05-0.06 | 0.003906 | 0.005859 | ** |
| L21 | 0.0472 | 0.009766 | 0.013428 | * |
| L22-L28 | -0.03 to 0.02 | 0.049-0.922 | 0.060-0.951 | |
| L29 | -0.0483 | 0.037109 | 0.048984 | * |
| L30-L32 | -0.10 to -0.12 | 0.003906 | 0.005859 | ** |

Early-mid layers (L1-L21): trained > untrained. Late layers (L29-L32): untrained > trained (negative diff, but still significant difference).

### 2. RSA trained vs untrained (last_preaction)

**0/33 layers significant after FDR (q<0.05)**

No layer survives correction. Closest: L1 (p_raw=0.0059, q=0.081) and L13 (p_raw=0.0059, q=0.081).

### 3. Probe R² trained vs untrained (image_mean)

**30/33 layers significant after FDR (q<0.05)**

| Significant | L1-L27, L29-L30, L32 |
|---|---|
| **Not significant** | **L0, L28, L31** |

Nearly all layers show significant trained vs untrained difference. Most at q=0.0026 level.

### 4. Probe R² trained vs untrained (last_preaction)

**29/33 layers significant after FDR (q<0.05)**

| Significant | L1, L4-L31 |
|---|---|
| **Not significant** | **L0, L2, L3, L32** |

Massive effects at mid-late layers (L12-L22 show mean_diff ~0.95-1.00 in R²).

---

**Summary**: RSA image_mean and both Probe readouts show robust trained-vs-untrained differences surviving FDR correction across most layers. RSA last_preaction shows no significant differences after correction.

---
