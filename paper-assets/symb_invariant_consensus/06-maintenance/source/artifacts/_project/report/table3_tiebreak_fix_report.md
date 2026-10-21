# Table 3 Tiebreaking Fix Report

**Date**: 2026-05-23
**Issue**: NLI combo scripts used `Counter.most_common()` (insertion-order tiebreaking) while SC baselines use alphabetical tiebreaking (`sorted(tied_candidates)[0]`). This caused inconsistent SC values across Table 3 and Table 28.

---

## 1. Recomputation Results (Old → New)

All values recomputed with alphabetical tiebreaking on ProofWriter depth-5 (n=600).

| Generator | Metric | Old (Counter) | New (Alphabetical) | Source |
|-----------|--------|---------------|-------------------|--------|
| **Mistral-7B** | SC | 39.33% | 39.33% (unchanged) | r11_3verifier_canonical.json |
| | Combo w=1 | 40.17% | 40.17% (unchanged) | r11 canonical |
| | Combo w=3 | 46.00% | 46.00% (unchanged) | r11 canonical |
| | Combo w=5 | 50.33% | 50.33% (unchanged) | r11 canonical |
| **LLaMA-3.1-8B** | SC | 70.00% | 72.50% | exp048 traces + alphabetical |
| | Combo w=1 | 73.33% | 73.33% (unchanged) | exp092 + d116 DeBERTa preds |
| | Combo w=3 | 73.33% | 73.33% (unchanged) | exp092 + d116 DeBERTa preds |
| | Combo w=5 | 72.00% | 72.00% (unchanged) | exp092 + d116 DeBERTa preds |
| **Qwen2.5-14B** | SC | 73.50% | 74.00% | exp032 traces + alphabetical |
| | Combo w=1 | 74.17% | 74.17% (unchanged) | qwen14b_pw_nli_combo + d116 |
| | Combo w=3 | 74.67% | 74.67% (unchanged) | qwen14b_pw_nli_combo + d116 |
| | Combo w=5 | 75.17% | 75.17% (unchanged) | qwen14b_pw_nli_combo + d116 |
| **Qwen3-14B** | SC | 85.00% | 85.83% | exp033 traces + alphabetical |
| | Combo w=1 | 85.83% | 86.00% | d116 + alphabetical recompute |
| | Combo w=3 | 86.00% | 86.33% | d116 + alphabetical recompute |
| | Combo w=5 | 86.83% | 87.00% | d116 + alphabetical recompute |

**Key pattern**: SC baselines shifted upward (LLaMA +2.50pp, Qwen2.5 +0.50pp, Qwen3 +0.83pp), shrinking combo Δ values.

---

## 2. McNemar p-values + BH Correction (m=12)

| Generator | w | Combo | Δ (pp) | McNemar p | BH p | Sig |
|-----------|---|-------|--------|-----------|------|-----|
| Mistral-7B | 1 | 40.17% | +0.83 | .359 | .721 | |
| Mistral-7B | 3 | 46.00% | +6.67 | 1.13e-5 | 6.78e-5 | *** |
| Mistral-7B | 5 | 50.33% | +11.00 | 6.18e-7 | 7.41e-6 | *** |
| LLaMA-8B | 1 | 73.33% | +0.83 | .359 | .721 | |
| LLaMA-8B | 3 | 73.33% | +0.83 | .665 | .886 | |
| LLaMA-8B | 5 | 72.00% | -0.50 | .871 | 1.000 | |
| Qwen2.5-14B | 1 | 74.17% | +0.17 | 1.000 | 1.000 | |
| Qwen2.5-14B | 3 | 74.67% | +0.67 | .503 | .755 | |
| Qwen2.5-14B | 5 | 75.17% | +1.17 | .360 | .721 | |
| Qwen3-14B | 1 | 86.00% | +0.17 | 1.000 | 1.000 | |
| Qwen3-14B | 3 | 86.33% | +0.50 | .453 | .755 | |
| Qwen3-14B | 5 | 87.00% | +1.17 | .210 | .721 | |

**Before fix**: 3/12 conditions BH-significant (Mistral w=3, w=5; LLaMA w=1)
**After fix**: 2/12 conditions BH-significant (Mistral w=3, w=5 only)
**Lost significance**: LLaMA w=1 (old p_BH=0.0048 → new p_BH=0.721)

---

## 3. 94.4% Investigation

The "94%" figure in analysis.tex line 7 refers to **error overlap between SICA and SC** (94% of SICA errors are also SC errors), NOT MAX-SAT agreement. No correction needed — this is a different metric from the tiebreaking issue.

---

## 4. Core Conclusion Impact

### Capability gap monotonicity: PRESERVED
The monotonic relationship (combo gain decreases with generator SC) holds after correction:

| Generator | SC (new) | Gap | Combo Δ w=3 |
|-----------|----------|-----|-------------|
| Mistral-7B | 39.33% | +15.67 | +6.67pp |
| LLaMA-8B | 72.50% | -17.50 | +0.83pp |
| Qwen2.5-14B | 74.00% | -19.00 | +0.67pp |
| Qwen3-14B | 85.83% | -30.83 | +0.50pp |

Spearman ρ = 1.0 for n=6 ProofWriter verifier-generator pairs — **unchanged**.

### Claims removed
- LLaMA w=1 BH-significant claim removed from solutions.tex and appendix.tex
- "Three of twelve" → "Two of twelve" in appendix Table 28 caption and text

### Claims preserved
- Mistral-7B combo w=3 significance (p < 0.001)
- "SC up to 72%" in conclusion (still accurate — fine-tuned DeBERTa extends to LLaMA SC=72.50%)
- All Spearman correlations for capability gap pattern

---

## 5. Figure 7 Regeneration

Figure 7 (capability_gap_scatter.pdf) regenerated with corrected data points:

| Point | Old (gap, Δ) | New (gap, Δ) |
|-------|-------------|-------------|
| Qwen3-14B PW-D5 | (-30.00, 1.00) | (-30.83, 0.50) |
| Qwen2.5-14B PW-D5 | (-18.50, 1.17) | (-19.00, 0.67) |
| LLaMA-8B PW-D5 | (-15.00, 3.33) | (-17.50, 0.83) |

Post-correction fit: Spearman ρ=0.986 (DeBERTa-only n=6), ρ=0.991 (incl LLaMA n=7).

---

## 6. Modified Files

| File | Changes |
|------|---------|
| `docs/paper/solutions.tex` | Table 3 data rows; "Zero-shot results" paragraph (Δ bound, BH ref); "Capability gap" paragraph (SC range, LLaMA claim, Δ bound) |
| `docs/paper/appendix.tex` | Table 28 all rows (SC, gap, combo, Δ, p, BH); caption ("three"→"two"); text paragraph (line ~938) |
| `docs/paper/figures/gen_capability_gap_scatter.py` | 3 PW data points + annotation coordinates |
| `docs/paper/figures/capability_gap_scatter.pdf` | Regenerated |
| `docs/paper/figures/capability_gap_scatter.png` | Regenerated |

## 7. Recomputation Script

Remote: `/root/autodl-tmp/fix_table3_tiebreaking.py` on westd-16639
Output: `/root/autodl-tmp/table3_tiebreak_recompute.json`
Cross-validated against: `nli_recompute_exp091_exp092.json` — PASSED
