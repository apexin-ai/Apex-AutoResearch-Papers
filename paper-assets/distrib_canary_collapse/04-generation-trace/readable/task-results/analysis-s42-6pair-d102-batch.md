# analysis s42 6pair d102 batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s42-6pair-d102-batch_20260524T003528_result.json`
- **Structured JSON:** [`086ae3ad6034091415f7.json`](../../sessions/08/086ae3ad6034091415f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All analysis complete. Here's the full report.

---

## Results: s42 1.4B 6-pair D102 Analysis

### Summary Table (PermG FDR forward)

| α | T=10 | T=15 | Cross-T |
|------|------|------|---------|
| 0.45 | 0/6 | 3/6 | +3 |
| 0.50 | 4/6 | 3/6 | -1 |
| 0.60 | 4/6 | 6/6 | +2 |
| 0.75 | 5/6 | **missing** | — |

### Robust pairs (K≥3/5)

| α | T=10 | T=15 |
|------|------|------|
| 0.45 | 0/6 | 3/6 |
| 0.50 | 2/6 | 1/6 |
| 0.60 | 0/6 | 4/6 |
| 0.75 | 0/6 | — |

All reverse PermG = 0/6 (good).

### Missing data
- **t15_a075_s42_fp32_14b**: no 1.4B directory exists on either server. Only 410M version found (`t15_a075_s42_fp32`).

### Step 7: Paper text flagged lines

**`appendix.tex:533`** — Most critical:
> Cross-$T$ improvement holds at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$; ...)

s42 shows $\alpha{=}0.45$: $0/6{\to}3/6$ (not 5/6). The 5/6 is from s43 data. When Table 17 is updated to s42 6-pair, this sentence needs updating. Also `$6/6{\to}3/6$` for α=0.50 — s42 shows 4/6→3/6 (not 6/6→3/6).

**`appendix.tex:534`**:
> ECE-based pairs achieve higher detection rates than entropy-based pairs (e.g., 3/3 vs 0/3 robust at $\alpha{=}0.50$, $T{=}15$)

s42 shows 1/3 vs 0/3 — directionally correct but smaller margin. If presenting s42 data, update to "1/3 vs 0/3".

**`appendix.tex:521`** — Uses 8-pair counts "s42: 4/8 fwd, 2/8 rev". On 6-pair: s42 = 4/6 fwd, 0/6 rev (reverse drops to 0 because MAUVE pairs likely carried reverse signal).

**`appendix.tex:524-525, 528`** — Use 8-pair notation ("/8"). If switching to unified 6-pair, these need denominator updates. Values remain directionally consistent (e.g., line 528 "both yield 3/8" → both yield 3/6).

### Artifacts saved
- 7 local JSON files: `artifacts/D102_14b_t{10,15}_a{045,050,060,075}_s42_fp32_14b_6pair.json`
- Summary: `artifacts/_project/s42_6pair_summary_20260524.md`

---
