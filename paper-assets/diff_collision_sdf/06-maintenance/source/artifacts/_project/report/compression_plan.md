# CoRL → ICRA Compression Plan

Generated: 2026-05-29

## Budget Overview

| Metric | CoRL (current) | ICRA target | Delta |
|--------|---------------|-------------|-------|
| Format | Single-column, 8pp main | Dual-column, 6–8pp (TBD) | ~30–50% text reduction |
| Main text words | ~3,187 | ~2,000–2,500 | −700–1,200 words |
| Tables (main) | 7 | 4–5 | −2–3 tables |
| Figures (main) | 5 | 3–4 | −1–2 figures |
| Appendix | 8pp (3,652 words, 12 sections) | **None** (ICRA forbids) | All → supplementary or cut |

Dual-column 8 pages ≈ single-column 5.3 pages of text. Current 8 single-column pages need ~33% cut even with 8-page ICRA limit.

---

## Section-by-Section Plan

### Abstract (abstract.tex) — 117 words
**Action: KEEP AS-IS**
- 117 words fits IEEE's ~150-word abstract limit
- Content is venue-neutral, no changes needed

### Introduction (introduction.tex) — 556 words, 2 figures
**Action: COMPRESS ~30% → ~400 words**

| Element | Decision | Rationale |
|---------|----------|-----------|
| fig_overview (figure*) | **KEEP** — 2-column spanning overview | Core visual summary of all 3 claims |
| fig1_teaser | **CUT or MERGE** into fig_overview | Redundant with overview panel (a); saves 1 figure slot |
| Para 1 (background) | Compress ~20% | Tighten setup, cut one citation |
| 3 claim paragraphs | Compress ~30% | Remove redundant detail already in section headers |
| Contribution list | **CUT** — replace with 1-sentence pointer | "We make three contributions (§III–V)" saves ~80 words |

Estimated saving: **~150 words + 1 figure**

### Related Work (related_work.tex) — 440 words, 5 paragraphs
**Action: COMPRESS ~35% → ~290 words**

| Element | Decision | Rationale |
|---------|----------|-----------|
| ¶1 VLA Models | Compress to 2 sentences | Background, not core |
| ¶2 Safety in Robot Learning | Keep, compress ~20% | Positions our work |
| ¶3 SDF in Robotics | **COMPRESS ~50%** | Keep only full-body SDF refs (RDF, CDF) that support our argument |
| ¶4 SDF integration pathways | **COMPRESS ~40%** | 3 pathways → 1 concise sentence per pathway |
| ¶5 Evaluation Metrics | Compress ~20% | Keep dfCAR motivation |

Estimated saving: **~150 words**

### Method / Experimental Setup (method.tex) — 521 words, 1 table, 2 equations
**Action: COMPRESS ~25% → ~390 words**

| Element | Decision | Rationale |
|---------|----------|-----------|
| §3.1 Benchmark and Models | Compress ~30% | Cut detailed 4-task description; keep model families + episode counts |
| tab:configurations | **KEEP** — tighten caption | Core reference table |
| §3.2 dfCAR (eq:car_f) | KEEP | Core metric contribution |
| §3.3 SDF Aux Training (eq:total_loss) | Compress ~30% | Phase 1/2 detail → 1 sentence; MLP architecture → supplementary |
| Oracle setup paragraph | Compress ~40% | 1 sentence: "We also test GT oracle refinement (§V)" |

Estimated saving: **~130 words**

### Claim 1: Action Collapse (claim1.tex) — 365 words, 1 table, 2 figures
**Action: COMPRESS ~25% → ~280 words**

| Element | Decision | Rationale |
|---------|----------|-----------|
| tab:fake_safety | **KEEP** | Core evidence table |
| fig3_scatter_and_oracle | **KEEP** — dual-panel figure | Left panel = Claim 1 evidence, right = Claim 2 |
| fig2_displacement | **MOVE TO SUPPLEMENTARY** | Distribution detail; main text references it but histogram is supplementary-grade |
| Threshold robustness ¶ | Compress ~50% | "τ_d robust across [2,200]mm (supplementary)" — cut bimodal discussion |

Estimated saving: **~85 words + 1 figure**

### Claim 2: EE-Only SDF Fails (claim2.tex) — 317 words, 1 table
**Action: COMPRESS ~20% → ~250 words**

| Element | Decision | Rationale |
|---------|----------|-----------|
| tab:oracle | **KEEP** | Core evidence |
| Per-task analysis ¶ | Compress ~30% | Keep mechanism insight, cut specific numbers per task → "see supplementary" |
| Pi0.5 cross-validation ¶ | Compress to 1 sentence | Currently 2 sentences; keep conclusion only |

Estimated saving: **~65 words**

Already the most concise section. Minimal cuts needed.

### Claim 3: Avoidance Source (claim3.tex) — 688 words, 3 tables, 1 figure
**Action: COMPRESS ~40% → ~400 words** (largest cut)

| Element | Decision | Rationale |
|---------|----------|-----------|
| tab:avoidance_source | **KEEP** | Core evidence table |
| tab:ssr | **MOVE TO SUPPLEMENTARY** | Supporting analysis, not core claim |
| tab:spatial_bowl | **MOVE TO SUPPLEMENTARY** | Cross-scene validation = robustness check, not primary evidence |
| fig:lambda_and_fingerprint | **KEEP** | Fingerprint plot is key visual evidence |
| ¶ CAR-TSR tradeoff (§tsr_collapse) | **COMPRESS to 2 sentences** | Currently 3 sentences + table reference. Cut to: "Fine-tuning reduces TSR by ~20pp due to distributional shift, not paralysis. The SSR/TSR ratio increases (supplementary), confirming safer execution among completing episodes." |
| ¶ Dose-response (§lambda_high) | **COMPRESS ~50%** | Keep: λ=0.1 result, p=0.155, MDE. Cut: alternative null constructions, binding constraint discussion |
| ¶ Cross-scene validation | **CUT** from main text | Single-seed, one scene — weak evidence. Table already moved to supplementary |

Estimated saving: **~290 words + 2 tables**

### Conclusion + Limitations (discussion.tex) — 183 words
**Action: COMPRESS ~20% → ~150 words**

| Element | Decision | Rationale |
|---------|----------|-----------|
| Conclusion ¶ | Keep, compress ~15% | Already concise |
| Limitations ¶ | **MERGE into Conclusion** as final 2 sentences | ICRA doesn't require separate Limitations section; keep key caveats (sim-only, seed count) |

Estimated saving: **~35 words**

---

## Appendix → Supplementary Mapping

ICRA forbids appendix. All 12 CoRL appendix sections must be handled:

| Appendix Section | CoRL | ICRA Action |
|------------------|------|-------------|
| A.1 Multi-Seed Results | tab:multiseed_full | → Supplementary PDF |
| A.2 Displacement Distribution | 1 sentence | → CUT (trivial) |
| A.3 Threshold Sensitivity | 2 tables | → Supplementary PDF |
| A.4 Per-Task TSR Breakdown | 1 table | → Supplementary PDF |
| A.5 Per-Task CAR Breakdown | 1 table + text | → Supplementary PDF |
| A.6 SSR Analysis | 1 sentence | → CUT (tab:ssr in supplementary covers this) |
| A.7 Per-Task Oracle Analysis | 2 tables + text | → Supplementary PDF |
| A.8 Null Distribution | Detailed stats | → Supplementary PDF (critical for rebuttal) |
| A.9 Stepwise Checkpoint | 1 table | → Supplementary PDF |
| A.10 Oracle Details | 3 paragraphs | → Supplementary PDF |
| A.11 Cross-Scene Validation | 1 sentence | → CUT |
| A.12 Eval Seed Robustness | 2 tables | → Supplementary PDF |
| A.13 Training Details | Hyperparams + schedule | **→ Method section** (compress to 1 paragraph) |
| A.14 TSR Collapse Mechanism | Analysis paragraph | → Supplementary PDF |

**Net: 10 sections → supplementary PDF, 2 sections cut, 1 section absorbed into main text.**

---

## Figure Plan for Dual-Column

| Figure | CoRL | ICRA | Notes |
|--------|------|------|-------|
| fig_overview (figure*) | Full-width overview | **KEEP as figure*** | 2-column spanning; may need panel resize |
| fig1_teaser | Column-width | **CUT** | Redundant with overview panel (a) |
| fig2_displacement | 0.85 column-width | **→ Supplementary** | Histogram detail |
| fig3_scatter_and_oracle | Column-width dual-panel | **KEEP** | Both panels serve Claims 1+2 |
| fig5_lambda_and_fingerprint | Column-width dual-panel | **KEEP** | Core Claim 3 evidence |

**Net: 5 figures → 3 figures (+ 1 in supplementary)**

---

## Table Plan

| Table | CoRL | ICRA | Notes |
|-------|------|------|-------|
| tab:configurations | Method | **KEEP** | Core reference |
| tab:fake_safety | Claim 1 | **KEEP** | Core evidence |
| tab:oracle | Claim 2 | **KEEP** | Core evidence |
| tab:avoidance_source | Claim 3 | **KEEP** | Core evidence |
| tab:ssr | Claim 3 | **→ Supplementary** | Supporting |
| tab:spatial_bowl | Claim 3 | **→ Supplementary** | Cross-scene robustness |

**Net: 7 tables → 4 tables (+ 2 in supplementary, 1 cut)**

Counting tab:ssr as cut from main since Claim 3 SSR paragraph will reference supplementary.

---

## Estimated Word Budget (ICRA 8-page dual-column)

| Section | Target Words | Tables | Figures |
|---------|-------------|--------|---------|
| Abstract | 117 | 0 | 0 |
| Introduction | 400 | 0 | 1 (figure*) |
| Related Work | 290 | 0 | 0 |
| Method | 390 | 1 | 0 |
| Claim 1 | 280 | 1 | 1 |
| Claim 2 | 250 | 1 | 0 |
| Claim 3 | 400 | 1 | 1 |
| Conclusion | 150 | 0 | 0 |
| **Total** | **~2,277** | **4** | **3** |

This fits comfortably in 6 dual-column pages with references on pages 7–8.

---

## Execution Priority

1. **Template migration** (skeleton done ✅) — fill content section by section
2. **Figure adaptation** — resize for dual-column, test figure* placement
3. **Table adaptation** — IEEEtran table formatting (may need `\resizebox` for wide tables)
4. **Supplementary PDF** — compile cut content into standalone supplementary
5. **Final polish** — IEEE reference style, author block, copyright notice
