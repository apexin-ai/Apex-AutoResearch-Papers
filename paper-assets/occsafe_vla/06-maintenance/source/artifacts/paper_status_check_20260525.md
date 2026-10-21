# Paper Status Check — 2026-05-25

## Summary
- **Version**: v42, 14 pages (8 main + 2 refs + 4 appendix)
- **Coverage**: 23/24 claims covered (tier2: 23, tier3: 1)
- **Compilation**: Clean (0 errors, 5 minor warnings)
- **TODOs/Placeholders**: 0

---

## 1. Coverage Gap (1/24 uncovered)

**C158 (tier3)**: "OCC-CBF: future direction, learned barrier function h(z_occ, x_robot) >= 0 conditioned on occ encoder features, not yet implemented" (section: discussion, type: conceptual)

The discussion mentions "This training-time intervention complements runtime safety methods" as a single sentence but does **not** explicitly describe the OCC-CBF concept — a learned barrier function conditioned on occupancy encoder features. The conclusion lists "Open directions include generalization to other VLA architectures and benchmarks, dynamic obstacles, and real-world deployment" but omits OCC-CBF.

**To close this gap**: Add 1-2 sentences in the discussion or conclusion describing the OCC-CBF future direction (learned barrier using occ encoder features as a bridge to runtime safety), or deprecate C158 if the team considers this out of scope for the current paper.

---

## 2. Latest Results Coverage Check

| Result | In Paper? | Location |
|--------|-----------|----------|
| 2×2 factorial ANOVA p=0.025, η²=0.484 | ✅ | results.tex:46 (§4.2) |
| Same-seed gradient analysis (DINOv2 3.5× suppression, SigLIP 2.5× amplification) | ✅ | results.tex:80 (§4.3) |
| Dose-response 2-seed data (cutoff_25k, reverse_cutoff) | ✅ | results.tex:101 (§4.4), Table 1 |
| Full OCC+LN 3-seed (0.743±0.024) | ✅ | results.tex:31, Table 1 |
| CKA representation-behavior dissociation | ✅ | results.tex:89 (§4.3) |
| Cohen's f=0.969 (large effect) | ✅ | results.tex:46 |
| Simple effects not significant (BN p=0.052, LN p=0.26) | ✅ | results.tex:48 |

All key D042 results are incorporated.

---

## 3. LaTeX Compilation

**Status**: Compiles successfully with `latexmk -pdf`

**Output**: main.pdf — 14 pages, 340KB

**Warnings** (5 total, all minor):
| # | Type | Location | Severity |
|---|------|----------|----------|
| 1 | Underfull vbox (badness 2512) | p5-6 transition | Low — page break layout |
| 2 | Underfull vbox (badness 2762) | p6-7 transition | Low — page break layout |
| 3 | Float specifier `h` → `ht` | appendix (per-task table) | Low — LaTeX auto-adjusts |
| 4 | Float specifier `h` → `ht` | appendix (hyperparams table) | Low — LaTeX auto-adjusts |
| 5 | Float specifier `h` → `ht` | appendix (dose-response figure) | Low — LaTeX auto-adjusts |

**Errors**: 0

**Missing figures**: 0 (all 4 PDFs present: gradient_analysis_combined.pdf, cka_analysis.pdf, per_layer_combined.pdf, dose_response.pdf)

---

## 4. TODO/FIXME/Placeholder Scan

**Found**: 0

The `\todo` macro is defined in main.tex:14 but never invoked anywhere in the paper.

---

## 5. Provenance Note

C164 in paper_provenance.yaml states "20 rollouts per task" but the paper correctly says "50 rollouts per task per seed". This is a stale provenance entry, not a paper error.

---

## 6. Page Budget

- Main text (intro through conclusion): ~8 pages (within CoRL limit)
- References: ~2 pages
- Appendix: ~4 pages (unlimited per CoRL rules)
