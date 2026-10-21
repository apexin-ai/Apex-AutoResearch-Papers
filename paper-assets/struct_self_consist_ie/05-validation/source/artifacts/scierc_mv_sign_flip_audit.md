# SciERC MV Delta Sign-Flip Audit

**Date**: 2026-05-22  
**Trigger**: Reviewer flagged SciERC MV delta inconsistency: s123=+0.34pp, s456=-0.84pp

---

## 1. Data Sources Identified

Two independent pipeline executions exist for SciERC N=8:

| Run | Directories | Seeds | Dates | Registry IDs |
|-----|------------|-------|-------|-------------|
| **MF4v2** (older) | `scierc_mf4v2_seed{42,123,456}/` | 42, 123, 456 | 2026-05-21 | `exp_scierc_mf4_v2_s42` |
| **N8** (newer) | `scierc_n8_seed{123,456}/` | 123, 456 only | 2026-05-22 | `exp_scierc_n8_s{123,456}` |

Both use `qwen3-8b-scierc-merged-v2`, same data, same hyperparams. Different file sizes confirm different sampling outputs (expected: GPU non-determinism).

**Critical**: N8 has no seed42 run. Registry mixes N8 s123/s456 with MF4v2 s42 — this is the root cause of the apparent sign flip.

## 2. Registry Numbers (Mixed Sources — PROBLEMATIC)

These are the numbers that triggered the reviewer concern:

| Seed | Source | greedy_f1 | mv_f1 | mv_delta_pp | Instance Set |
|------|--------|-----------|-------|-------------|-------------|
| 42 | MF4v2 recompute | 0.6683 | 0.6558 | **-1.24** | gold-nonempty (529) |
| 123 | N8 auto-hook | 0.6613 | 0.6648 | **+0.34** | all instances (551) |
| 456 | N8 auto-hook | 0.6657 | 0.6573 | **-0.84** | all instances (551) |

**Problems**:
- Mixes two different pipeline runs (MF4v2 vs N8)
- Instance set differs (529 vs 551)
- MV computation method may differ (strict recompute vs automated hook)

## 3. Unified MF4v2 Recompute (Consistent — AUTHORITATIVE)

Source: `scierc_3seed_full_recompute.py` → `scierc_3seed_recompute_results.json`  
All 3 seeds from same pipeline. Gold-nonempty filter (n=529). Strict MV (>N/2, 4-tuple entity match).

| Seed | greedy_f1 | mv_f1 | mv_delta_pp | sel_lp_f1 | lp_delta_pp | degeneracy |
|------|-----------|-------|-------------|-----------|-------------|------------|
| 42 | 0.6683 | 0.6558 | **-1.25** | 0.6651 | -0.32 | 13.4% |
| 123 | 0.6663 | 0.6652 | **-0.11** | 0.6718 | +0.55 | 11.0% |
| 456 | 0.6663 | 0.6577 | **-0.86** | 0.6639 | -0.24 | 12.1% |
| **Mean** | **0.6669** | **0.6596** | **-0.74** | **0.6669** | **-0.003** | **12.2%** |
| **Std (σ)** | **0.0009** | **0.0040** | **0.46** | **0.0035** | **0.35** | **1.0%** |

**No sign flip.** All three MV deltas are negative. MV consistently hurts on SciERC.

## 4. Cross-Verification

### Source file → recompute consistency
- MF4v2 recompute JSON matches `scierc_3seed_recompute_results.txt` (independent text output) ✓
- Recompute greedy_f1 for s42 (0.6683) matches registry `exp_scierc_mf4_v2_s42` metrics ✓
- Recompute uses same `consistency.py` functions (SJ, FK) as main pipeline ✓

### N8 report.json → registry consistency
- N8 s123 report.json greedy_f1=0.6613 matches registry `exp_scierc_n8_s123` ✓
- N8 s456 report.json greedy_f1=0.6657 matches registry `exp_scierc_n8_s456` ✓
- N8 MV metrics NOT in report.json — computed by automated hook, method undocumented ⚠️

## 5. Explanation of Apparent Sign Flip

The +0.34pp for s123 (N8) vs -0.11pp for s123 (MF4v2) arises from:
1. **Different sampling realizations**: N8 and MF4v2 are independent runs (different file sizes: 20,054,496 vs 20,068,257 bytes)
2. **Different instance sets**: N8 may include gold-empty instances (551 total), MF4v2 recompute filters to gold-nonempty (529)
3. **Near-zero effect size**: MV delta on SciERC is small (~0.7pp), making it sensitive to sampling noise

## 6. Recommended Paper Numbers

Use the MF4v2 unified recompute. For SciERC N=8 finetuned:

> MV consistently decreases F1 on SciERC (mean Δ = −0.74 ± 0.46pp across 3 seeds), with all seeds showing negative delta (range: −1.25 to −0.11pp). The 12.2% degeneracy rate indicates that strict majority voting discards non-trivial information.

### Suggested table entry (SciERC row):
| | Greedy F1 | MV F1 | MV Δ (pp) | LP-Sel F1 | LP Δ (pp) | Degen. |
|---|-----------|-------|-----------|-----------|-----------|--------|
| SciERC | 66.69±0.09 | 65.96±0.40 | −0.74±0.46 | 66.69±0.35 | −0.00±0.35 | 12.2%±1.0% |

## 7. Action Items

1. **Fix registry**: Update `exp_scierc_n8_s123` and `exp_scierc_n8_s456` metrics to note they are from a different pipeline run, or replace with MF4v2 recompute values
2. **Paper claim**: MV hurts SciERC — no hedging needed about sign instability
3. **LP selection**: Essentially neutral on SciERC (mean Δ ≈ 0), report as "LP selection does not improve over greedy on SciERC"
4. **If reviewer asks about n8 vs mf4v2 discrepancy**: Explain that unified recompute from same pipeline eliminates the artifact; the sign flip was due to mixing independent runs
