# Table 7 MISSING_3SIGMA Fix: 4 Experiments K-Value Correction

**Date**: 2026-05-20
**Data source**: `westd-17855:results/analysis/3sigma_recompute_d105_17855.json` (3/4 experiments) + manual 3σ recompute (Pythia-410M s43)
**Cross-validation**: scale_69b algorithm reproduced 2/8 matching JSON exactly

---

## 1. Pythia-6.9B s42 — threshold_3σ = 2/8 (was 8/8 at 2σ)

| pair | naive_fwd | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|----------|-----------|-----------|-----|---|
| te→d1 | F | F | **F** | T | F | **1** |
| te→d2 | F | F | **F** | T | T | **2** |
| te→d3 | T | F | **F** | T | T | **3** |
| te→mauve | T | F | **T** | F | T | **3** |
| ece→d1 | F | F | **F** | T | F | **1** |
| ece→d2 | F | F | **F** | T | F | **1** |
| ece→d3 | F | F | **F** | T | T | **2** |
| ece→mauve | T | F | **T** | T | F | **3** |

**K≥3 = 3/8, K≥4 = 0/8**

3σ onset detail: only mauve downstream breaches 3σ (onset gen 6); distinct_1/2/3 never reach 3σ.

---

## 2. Qwen3.5-0.8B s42 — threshold_3σ = 0/8 (was 8/8 at 2σ)

| pair | naive_fwd | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|----------|-----------|-----------|-----|---|
| te→d1 | T | F | **F** | T | F | **2** |
| te→d2 | T | F | **F** | T | T | **3** |
| te→d3 | T | F | **F** | T | F | **2** |
| te→mauve | T | F | **F** | T | T | **3** |
| ece→d1 | F | F | **F** | T | T | **2** |
| ece→d2 | F | F | **F** | T | T | **2** |
| ece→d3 | F | F | **F** | T | T | **2** |
| ece→mauve | F | T | **F** | T | T | **3** |

**K≥3 = 3/8, K≥4 = 0/8**

3σ onset detail: no downstream metric breaches 3σ for any pair.

---

## 3. Padding-410M s42 — threshold_3σ = 0/8 (was 8/8 at 2σ)

| pair | naive_fwd | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|----------|-----------|-----------|-----|---|
| te→d1 | F | F | **F** | T | T | **2** |
| te→d2 | F | F | **F** | T | T | **2** |
| te→d3 | F | F | **F** | T | T | **2** |
| te→mauve | F | F | **F** | F | F | **0** |
| ece→d1 | F | F | **F** | T | T | **2** |
| ece→d2 | F | F | **F** | T | T | **2** |
| ece→d3 | F | F | **F** | T | T | **2** |
| ece→mauve | F | F | **F** | F | F | **0** |

**K≥3 = 0/8, K≥4 = 0/8**

3σ onset detail: no downstream metric breaches 3σ; padding variant has weaker signal than standard 410M.

---

## 4. Pythia-410M s43 — threshold_3σ = 0/8 (was 8/8 at 2σ)

**Note**: Task stated "D105: threshold_3σ = 2/8" but that value was from the D105 recompute of **s42** (`generalize_pythia410m_wiki_a100_s42`). s43 was not in the 3sigma_recompute JSON; recomputed here using identical algorithm (cross-validated against scale_69b).

| pair | naive_fwd | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|----------|-----------|-----------|-----|---|
| te→d1 | F | F | **F** | T | T | **2** |
| te→d2 | F | F | **F** | T | T | **2** |
| te→d3 | F | F | **F** | T | T | **2** |
| te→mauve | F | F | **F** | F | F | **0** |
| ece→d1 | F | F | **F** | T | T | **2** |
| ece→d2 | F | F | **F** | T | T | **2** |
| ece→d3 | F | F | **F** | T | T | **2** |
| ece→mauve | F | F | **F** | F | F | **0** |

**K≥3 = 0/8, K≥4 = 0/8**

3σ onset detail: canary onsets exist (te gen 2, ece gen 4) but no downstream breaches 3σ.

---

## Summary: 2σ Fallback vs True 3σ

| # | Model | Seed | thresh_3σ | K≥3 (2σ fb → 3σ) | K≥4 (2σ fb → 3σ) | Δ K≥3 |
|---|-------|------|-----------|-------------------|-------------------|-------|
| 1 | Pythia-6.9B | s42 | 2/8 | 5/8 → **3/8** | 1/8 → **0/8** | −2 |
| 2 | Qwen3.5-0.8B | s42 | 0/8 | 8/8 → **3/8** | 3/8 → **0/8** | −5 |
| 6 | Padding-410M | s42 | 0/8 | 6/8 → **0/8** | 0/8 → **0/8** | −6 |
| 8 | Pythia-410M | s43 | 0/8 | 6/8 → **0/8** | 0/8 → **0/8** | −6 |

### Impact

- **Qwen3.5-0.8B** drops most dramatically: K≥3 from 8/8 to 3/8 (the 2σ threshold was the only thing keeping 5 pairs above K≥3)
- **Padding-410M** and **Pythia-410M s43** collapse to K≥3=0/8: all 6 non-mauve pairs had K=3 only because thresh=T at 2σ gave exactly the third vote alongside permG+TY; removing it drops all to K=2
- **Pythia-6.9B** retains K≥3=3/8 because it has diverse vote sources (naive_fwd=3/8, TY=4/8) and 2 pairs still pass at 3σ (mauve downstream breaches 3σ)
- All 4 experiments now have K≥4=0/8

### Audit note on Pythia-6.9B ece→mauve

The original audit (table7_d105_d111_unified_audit.md line 29) listed K=2 for ece→mauve, but the votes are naive_fwd=T + diff_fwd=F + thresh_3σ=T* + permG_fdr=T + TY=F = 3. This was a calculation error in the audit (did not affect the audit summary since it was already counted in K≥3=5/8 with the 2σ value, but the per-pair K was misstated).
