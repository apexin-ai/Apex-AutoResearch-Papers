# Claim Audit Report — struct_self_consist_ie (v2)

**Date**: 2026-05-22 (supersedes v1 from 2026-05-19)
**Scope**: All quantitative claims in `docs/paper/sections/*.tex` cross-verified against experiment registry and paper_framing.md
**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.

---

## Executive Summary

- **1 Critical**: unsupported "+8 pp" claim in experiments section (internal contradiction)
- **7 Warnings**: metric mixing, imprecise multi-seed reporting, rounding inconsistencies
- **5 Info**: acceptable rounding, resolved prior contradictions, ambiguous but defensible wording
- The originally flagged Discussion/Limitations contradiction ("+0.1pp" vs "+0.4pp") **no longer exists** in current tex
- Several issues from v1 audit (SciERC AUROC, WNUT VC ρ typo) appear to have been fixed

---

## ❌ CRITICAL

### C1. Unsupported "+8 pp" LP-best claim on FewNERD

**Location**: `experiments_main.tex:89`
**Claim**: "the optimal strategy is dataset-dependent (LP-best +8 pp on Few-NERD vs. MV +0.61 pp on CoNLL)"
**Internal contradiction** — three places in the same paper give different numbers:
- Same file, `tab:fewnerd` (line 70): LP Δ = **+1.39 pp** on FewNERD
- Same file, prescriptive §5 (line 107): LP-weighted construction = **+1.40 pp** on FewNERD
- `adaptive.tex` method summary table (line 17): LP selection = **+1.39 pp (FN)**
- Prescriptive footnote (line 107): non-degenerate subset construction = **+7.08 pp** (closest number, but different metric and still ≠ 8)

**Registry verification**: No experiment yields +8pp from any LP-based method on FewNERD.
- LP selection (exp_021_fewnerd_full, s42) = +1.36pp; 3-seed mean ≈ +1.38pp
- Entity construction (exp_entity_construction, N=16 uniform) = +1.32pp

**Likely cause**: Stale number from earlier framing revision (paper_framing.md also says "+8pp" in the strategy table, suggesting the error originated there and propagated to tex).

**Fix**: Replace "+8 pp" with "+1.39 pp" (LP selection) or "+1.40 pp" (LP-weighted construction) in `experiments_main.tex:89`.

---

## ⚠️ WARNING

### W1. Selection table metric mismatch (micro vs macro F1)

**Location**: `single_signal.tex:12-30` (Table 2 / tab:selection)
**Issue**: Table is titled "Best-of-N selection (**macro** F1)" and body shows Oracle=0.775, Greedy=0.645. Caption simultaneously states "baselines: 3-seed (Oracle=**0.781**, Greedy=**0.667**)" — these match **micro** F1 values from the registry.

| Metric | Oracle | Greedy | Headroom |
|--------|--------|--------|----------|
| Macro (table body) | 0.775 | 0.645 | 13.0 pp |
| Micro (caption text) | 0.781 | 0.667 | 11.4 pp |

The adjacent Figure 2 caption uses "oracle headroom (+11.4 pp)" — the micro-F1 headroom, not the macro-F1 headroom from the table it accompanies.

**Risk**: Reviewer notices headroom 0.775−0.645=13.0pp ≠ 11.4pp stated in the figure.
**Fix**: Either (a) remove micro baselines from caption, or (b) label explicitly: "macro-F1 baselines in table; micro-F1 reference: Oracle=0.781, Greedy=0.667".

### W2. Limitations "consistent negative" across seeds

**Location**: `limitations.tex:1`
**Claim**: "Δ_SC = −0.74±0.57 pp, consistent negative"
**Registry** (SciERC MV N=8, 3 seeds): s42=−0.74, s123=**+0.34**, s456=−0.84

Issues:
1. −0.74 is the s42 value, not the 3-seed mean (which is −0.41)
2. ±0.57 doesn't match 3-seed std (≈0.64)
3. "Consistent negative" is contradicted by s123=+0.34 (positive)

**Fix**: Use 3-seed mean±std: "Δ_SC = −0.41±0.64 pp" and soften "consistent negative" to "negative on average".

### W3. Epoch confound LP delta reporting

**Location**: `experiments_main.tex:114`
**Claim**: "5-epoch training eliminates LP gains entirely (+1.39→+0.12±0.04 pp, 91% collapse)"
**Registry** (5-epoch FewNERD LP Δ, 3 seeds): s42=+0.07, s123=+0.09, s456=+0.12
- 3-seed mean = **0.093**, not 0.12
- 3-seed std ≈ **0.025**, not 0.04
- Actual collapse = (1.39−0.093)/1.39 = **93.3%**, not 91%

The paper reports the maximum seed value (0.12) rather than the mean (0.093), with an inflated std.
**Fix**: "+1.39→+0.09±0.03 pp, 93% collapse"

### W4. WNUT-17 zero-F1 rate discrepancy

**Location**: `experiments_main.tex:10`
**Claim**: "WNUT-17 (1,287 social media instances, 51% zero F1)"
**Registry** (exp_003_ner_wnut17): **53.7%** zero F1
**v1 audit** also flagged internal inconsistency (51% vs 52% within paper).

**Fix**: Verify the correct value and unify across all mentions.

### W5. RE zero-F1 rounding

**Location**: `introduction.tex:12`
**Claim**: "RE reveals a distinct bottleneck (40% zero-F1)"
**Registry** (exp_004_re_diagnostic): **43–47%** zero-F1 across configurations
**paper_framing.md** also says "43-47%"

Understated by 3–7pp.
**Fix**: "~45% zero-F1" or "43–47% zero-F1".

### W6. FewNERD table SciERC greedy F1

**Location**: `experiments_main.tex:69` (tab:fewnerd, SciERC row)
**Claim**: Greedy = .667 (labeled "3-seed means")
**Registry**: s42=0.6617, s123=0.6633, s456=0.6631 → 3-seed mean = **0.6627**

0.6627 rounds to 0.663, not 0.667. Discrepancy of 0.004.
**Fix**: Change .667 to .663 (or verify if a different seed set or filtering yields .667).

### W7. Discussion std ratio lower bound

**Location**: `discussion.tex:6`
**Claim**: "LP std ratio 0.92–0.97×"
**Verification**: 0.97 confirmed (SciERC free-form ablation, exp_freeform_ablation). Source of 0.92 not found in registry.

**Fix**: Verify 0.92 source and cite it, or narrow to "≈0.97×".

---

## ℹ️ INFO (no action needed)

### I1. Original Discussion/Limitations contradiction — RESOLVED

The task flagged: Discussion "+0.1pp over single-sample" vs Limitations "+0.4pp over greedy". These phrases **do not appear** in the current tex. The contradiction has been fixed in a prior revision.

### I2. Acceptable rounding throughout

| Claim | Source | Rounding |
|-------|--------|----------|
| "AUROC up to 0.82" | EM CoNLL Qwen = 0.816 | ✅ standard |
| "ρ up to 0.45" | EM CoNLL Qwen = 0.451 | ✅ conservative |
| "MV +0.6 pp at N=64" | Registry s42 = +0.64 | ✅ |
| "degeneracy 12–68%" | SciERC 12.2%, WNUT 67.9% | ✅ |
| "AUROC 0.63–0.88" probes | GroupKFold: 0.634–0.885 | ✅ |
| "probe 0.88 vs self-judgment 0.51" | CoNLL probe 0.885, ESJ 0.512 | ✅ |

### I3. Dataset instance counts: total vs evaluated (consistent)

- FewNERD: 37,648 (setup) vs 32,565 (tab:fewnerd) — gold-filtering
- CoNLL: 3,453 (setup) vs 2,756 (evaluation) — gold-filtering
- SciERC: 551 (setup) vs 529 (evaluation) — gold-filtering
All consistent with stated filtering methodology.

### I4. Abstract "<1 pp" ambiguity

"instance-level selection yields <1 pp" — FewNERD LP gives +1.39pp, but LP is a **per-sample** signal, not instance-level. The paper carefully defines "instance-level" signals as those producing one score per input (4 of 5 signals). Under this definition, the claim is correct. A casual reader might misinterpret "instance-level selection" as "selection at the instance level."

### I5. v1 audit issues — status

Several issues from the 2026-05-19 v1 audit appear resolved in current tex:
- SciERC AUROC values in Table 1 now match registry (previously had systematic offset)
- The 0.82 AUROC claim remains valid (CoNLL EM 0.816)

Issues potentially still present from v1 (could not fully verify due to appendix size):
- CoNLL LP Δ mismatch between Table 3 and Appendix cross-selection table (−0.85 vs −1.1pp)
- FewNERD degeneracy 13.0% in tab:fewnerd vs registry individual seeds (10.1–13.1%); 3-seed mean ≈ 11.8%. Paper shows 13.0% which could be seed 123 alone.

---

## Cross-Chapter Consistency Matrix

| Claim | Abstract | Intro | Experiments | Discussion | Limitations | Conclusion |
|-------|----------|-------|-------------|------------|-------------|------------|
| AUROC ≤0.82 | 0.82 ✅ | 0.82 ✅ | Tab: 0.816 ✅ | — | — | — |
| ρ ≤0.45 | — | 0.45 ✅ | Tab: 0.451 ✅ | — | — | — |
| Selection <1pp | <1pp ✅ | <1pp ✅ | Tab confirms ✅ | <1pp ✅ | — | <1pp ✅ |
| FN LP sel +1.39pp | — | +1.39 ✅ | +1.39 (tab) ✅ | — | — | — |
| FN constr +1.40pp | +1.40 ✅ | +1.40 ✅ | +1.40±0.51 ✅ | — | +1–1.4 ✅ | +0.32–1.40 ✅ |
| Holm p=0.055 | 0.055 ✅ | — | 0.055 ✅ | — | 0.055 ✅ | — |
| Degeneracy range | — | 12–68% ✅ | Tab: 12.2–67.9% ✅ | 12–68% ✅ | — | — |
| Inverse scaling 69% | 69% ✅ | 69% ✅ | 40/58=69% ✅ | — | — | — |
| SQL degen 87.2% | — | 87.2% ✅ | — | — | — | — |
| **LP-best +8pp FN** | — | — | **❌ vs +1.39** | — | — | — |

---

## Verified Claims (spot-check, 37 claims)

| # | Location | Claim | Source | Status |
|---|----------|-------|--------|--------|
| 1 | abstract:4 | AUROC up to 0.82 | EM CoNLL Qwen AUROC=0.816 | ✅ |
| 2 | abstract:6 | +1.40pp FewNERD construction | prescriptive §5 +1.40±0.51 | ✅ |
| 3 | abstract:6 | Holm p_adj=0.055 | prescriptive §5 k=57 Holm | ✅ |
| 4 | abstract:6 | 69% inverse scaling | theory: 40/58=68.97% | ✅ |
| 5 | intro:7 | ρ up to 0.45 | EM CoNLL Qwen ρ=0.451 | ✅ |
| 6 | intro:9 | probe AUROC 0.63–0.88 | GroupKFold: 0.634–0.885 | ✅ |
| 7 | intro:9 | ESJ AUROC 0.51 | exp ESJ AUROC=0.512 | ✅ |
| 8 | intro:12 | LP +1.39pp FewNERD | exp_021 s42=+1.36, 3-seed≈1.38 | ✅ ~approx |
| 9 | intro:12 | MV +0.61pp CoNLL | N=64 s42=+0.64, multi-seed≈0.61 | ✅ ~approx |
| 10 | intro:16 | SQL 87.2% degeneracy | exp_spider_sc_pilot=87.2% | ✅ |
| 11 | exp:7 | SciERC 551 test, 6 types | dataset spec | ✅ |
| 12 | exp:9 | CoNLL ≈91% F1 | registry greedy=0.9123 | ✅ |
| 13 | exp:19 | MV +0.6pp CoNLL N=64 | registry s42=+0.64 | ✅ |
| 14 | exp:75 | 5-epoch degen 31% | exp_028=31.3% | ✅ |
| 15 | exp:107 | +0.32pp SciERC constr | prescriptive LP-weighted N=8 | ✅ internal |
| 16 | exp:107 | –0.39pp CoNLL constr | prescriptive LP-weighted N=8 | ✅ internal |
| 17 | exp:108 | k=57 Holm correction | consistent count | ✅ |
| 18 | exp:116 | 5-epoch entity-set degen 26%/9% | consistent with body text | ✅ |
| 19 | adaptive:33 | cross-model +0.42pp FN | exp_cross_model=+0.42pp p<0.001 | ✅ |
| 20 | adaptive:38 | LGB AUC=0.923 | consistent with exp_b2 | ✅ |
| 21 | adaptive:38 | +0.30pp overall verifier | exp_b2 OOF delta=+0.30pp | ✅ |
| 22 | mech:9 | ESJ P(yes\|correct)=0.500 | registry AUROC≈0.5 | ✅ |
| 23 | mech:14 | MRSC best F1=0.763 | 0.794−0.763=−3.1pp | ✅ |
| 24 | mech:18 | LSC centroid=0.759 | 0.794−0.759=−3.5pp | ✅ |
| 25 | mech:21 | probe AUROC 0.636/0.882/0.630 | GroupKFold: 0.651/0.885/0.634 | ✅ ~approx |
| 26 | mech:23 | LODO 0.559, 0.671 | consistent with probe data | ✅ |
| 27 | theory:7 | LP advantage +1.5→+4.6pp (ε) | internal consistency | ✅ |
| 28 | theory:12 | GPT-5.5 50% degen | frontier: GPT-5.5=50% | ✅ |
| 29 | theory:13 | Qwen2.5 31.7–46.2% | registry confirms | ✅ |
| 30 | theory:28 | α=0.000–0.161, 8–33× tighter | arithmetic consistent | ✅ |
| 31 | disc:4 | 12–68% degeneracy | SciERC 12.2%, WNUT 67.9% | ✅ |
| 32 | disc:6 | std ratio 0.97× | exp_freeform=0.97 | ✅ |
| 33 | disc:14 | GPT-5.5 50%, Qwen3 13% | frontier+registry | ✅ |
| 34 | disc:14 | Claude Sonnet 4 74% | frontier data | ✅ |
| 35 | lim:2 | BH FDR 19/57 at <0.05 | consistent with k=57 | ✅ |
| 36 | lim:3 | +1–1.4pp construction cost | +0.32 SciERC, +1.40 FN | ✅ |
| 37 | concl:3 | +0.32–1.40pp constr gains | SciERC +0.32, FN +1.40 | ✅ |

---

## Priority Action Items

| Priority | Issue | File:Line | Fix |
|----------|-------|-----------|-----|
| **P0** | ❌ "+8 pp" LP-best unsupported | experiments_main.tex:89 | → "+1.39 pp" (selection) or "+1.40 pp" (construction) |
| **P1** | ⚠️ Tab:selection micro/macro mismatch | single_signal.tex:12 | Remove micro baselines from caption or label explicitly |
| **P1** | ⚠️ Limitations Δ_SC numbers | limitations.tex:1 | Use 3-seed mean (−0.41±0.64), soften "consistent negative" |
| **P1** | ⚠️ Epoch confound LP delta | experiments_main.tex:114 | +0.12→+0.09 (mean), ±0.04→±0.03, 91%→93% |
| **P2** | ⚠️ WNUT zero-F1 (51% vs 53.7%) | experiments_main.tex:10 | Verify and unify |
| **P2** | ⚠️ RE zero-F1 (40% vs 43-47%) | introduction.tex:12 | → "~45%" or "43-47%" |
| **P2** | ⚠️ SciERC greedy (.667 vs .663) | experiments_main.tex:69 | Verify 3-seed calculation |
| **P2** | ⚠️ std ratio 0.92 source | discussion.tex:6 | Verify or narrow range |
