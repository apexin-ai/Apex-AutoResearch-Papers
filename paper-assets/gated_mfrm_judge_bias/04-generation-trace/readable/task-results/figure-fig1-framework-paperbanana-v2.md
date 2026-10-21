# figure fig1 framework paperbanana v2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1-framework-paperbanana-v2_20260524T163756_result.json`
- **Structured JSON:** [`9e49101a5f9384f9a5bb.json`](../../sessions/9e/9e49101a5f9384f9a5bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件：**
- `figures/paper/fig1_framework_v2.png` (3.9 MB, 2752×1536, 300 DPI)
- `figures/paper/fig1_framework_v2.pdf`

**LaTeX 更新：** `method.tex` 第 8 行已改为 `fig1_framework_v2`

**内容完整性核查（32/32 通过）：**
- Panel (a): Bias Correction / Contamination Adjustment boxes, OVB pill with confounding arrows, d_j↔c_n·e_i annotation, red ✗ + biased estimates
- Panel (b) Stage 1: MFRM formula, Y_nij input, θ̂/b̂/d̂ outputs, NUTS sampler
- Panel (b) Stage 2: Reference Anchoring 75%/gpt-4-0314, Cross-Model Agreement 25%/z-score, Identifiability (Thm. 1), LogProber optional, ê_i fixed externally
- Panel (b) Stage 3: G-MFRM formula with c_n·e_i, σ_c~HalfNormal(1), c_n=c_n^raw·σ_c, Warm-start arrow, ê_i fixed arrow, θ̃_n/ĉ_n/d̂_j/b̂_i outputs with sublabels, NUTS + hierarchical priors
- Green ✓ Corrected estimates

---
