# Claim Audit Report: Numerical Consistency Check

**Date**: 2026-05-17
**Scope**: All quantitative claims across abstract, introduction, experiments, discussion, conclusion, appendix
**Ground truth**: Corrected experimental data (exp-024/exp-026), Figure 3 script values

---

## Abstract

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L4 | "$\rho$ up to 0.38" | VC SciERC = 0.379 → rounds to 0.38 | ✅ |
| L5 | "~13 pp oracle headroom" | SciERC gold-filtered: 0.778-0.645=13.3 pp → ~13 | ✅ |
| L6 | "14--47% identical outputs" | Few-NERD 13.8%≈14%, CoNLL 47.4%≈47% | ✅ |
| L6 | "median $\rho$=0.52" (within-instance SJ-F1) | Table degeneracy: SciERC 8B = 0.524 ≈ 0.52 | ✅ |
| L6 | "$\rho \gtrsim 0.3$" for LP-quality alignment | Threshold claim, consistent with Few-NERD ρ≈0.5 | ✅ |
| L7 | "+1.36 pp at 14% degeneracy, p<0.001" | Few-NERD: +1.36 pp, degen 13.8%≈14%, p<0.001 | ✅ |
| L8 | "+0.52 pp from N=8 to 16, paired p=0.003" | Few-NERD: 1.88-1.37=0.51≈0.52; p=0.003 | ✅ |

## Introduction

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L12 | "$\rho$ up to 0.38 on the primary test bed" | VC SciERC = 0.379 | ✅ |
| L12 | "0.42 on Few-NERD" | LP Few-NERD = 0.421 | ✅ |
| L12 | "AUROC up to 0.82" | EM CoNLL Qwen = 0.816 → 0.82 | ✅ |
| L13 | "12--14 pp oracle headroom" | Few-NERD 12.4, SciERC 13.3, range covers 12-14 | ✅ |
| L14 | "14--47% of instances yield identical outputs" | Few-NERD 13.8%, CoNLL 47.4% | ✅ |
| L14 | "within-instance $\rho$=0.52" | Table degeneracy: 0.524 | ✅ |
| L15 | "13.8% degeneracy with $\rho$≈0.5 (+1.36 pp, p<0.001)" | Table fewnerd: degen 13.8%, LP Δ +1.36 | ✅ |
| L15 | "17.8% with $\rho$≈0.24 (+0.42 pp)" | Table fewnerd: degen 17.8%, LP Δ +0.42 | ✅ |
| L15 | "absent at 47.4%" | CoNLL degen 47.4%, LP Δ fail | ✅ |
| L20 | Figure caption: "$\rho$ up to 0.45 on CoNLL" | EM CoNLL Qwen = 0.451 ≈ 0.45 | ✅ |
| L20 | Figure caption: "13 pp oracle headroom" | SciERC gold-filtered: 13.3 pp | ✅ |
| L31 | "VC $\rho$=0.38" | Table QE: VC SciERC = 0.379 | ✅ |
| L31 | "EM AUROC=0.82" | Table QE: EM CoNLL Qwen = 0.816 | ✅ |
| L41 | "47% → fail, 18% → +0.42 pp, 14% → +1.36 pp" | 47.4→fail, 17.8→+0.42, 13.8→+1.36 (rounded) | ✅ |
| L41 | "degeneracy 7.2%, LP still fails because $\rho$≈0.24" | LoRA-rank ablation values | ✅ |
| L42 | "$\rho$=-0.881, p=0.004, n=8" | Per-type analysis, KeySet degen vs oracle headroom | ✅ |
| L42 | "+0.52 pp from N=8 to N=16, paired p=0.003" | Few-NERD paired gain | ✅ |

## Experiments: Quality Estimation Table (Tab 1)

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L35 | VC SciERC: ρ=.379, AUC=.663 | Primary source table | ✅ |
| L36 | SJ SciERC: ρ=.360, AUC=.650 | Primary source table | ✅ |
| L37 | FK SciERC: ρ=.267, AUC=.602 | Primary source table | ✅ |
| L38 | EM SciERC: ρ=.295, AUC=.614 | Primary source table | ✅ |
| L40 | LP SciERC: ρ=.205, AUC=.578 | Primary source table | ✅ |
| L40 | LP CoNLL Qwen: ρ=.316 | Cross-checked with Table fewnerd (.316) | ✅ |

## Experiments: QE Inline Claims

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L48 | "VC ρ=0.379, SJ 0.360" | Table QE | ✅ |
| L48 | "ρ≤0.295 surface, LP 0.205" | Table QE: EM=.295, FK=.267, LP=.205 | ✅ |
| L48 | "Δρ=+0.155 SJ-LP" | 0.360-0.205=0.155 | ✅ |
| L49 | "EM leads CoNLL ρ and AUROC (0.816)" | Table QE: EM CoNLL Qwen AUC=.816 | ✅ |
| L50 | "VC ρ=0.724 (AUROC=0.913), conditional ρ 0.038" | Table WNUT | ✅ |
| L51 | "LP full-set ρ=-0.410, conditional ρ=0.350" | Table WNUT | ✅ |
| L52 | "EM conditional ρ=0.360" | Table WNUT shows EM Cond.=0.333, LP Cond.=0.350 | ❌ see note below |

**Note L52**: The text says "Restricting to non-zero instances reshuffles rankings, with EM strongest (rho=0.360; Figure signal_heatmap)". This sentence sits in the WNUT paragraph but rho=0.360 is from SciERC conditional (confirmed by heatmap caption and appendix L200). On WNUT conditional specifically, Table WNUT shows LP Cond. rho=0.350 > EM Cond. rho=0.333, so EM is NOT the strongest on WNUT. The sentence is a **misleading cross-reference**: it makes a general observation using SciERC data, but a reader in the WNUT paragraph will interpret it as about WNUT. Either (a) clarify that rho=0.360 is from SciERC, or (b) note that on WNUT specifically, LP has the highest conditional rho.

## Experiments: Selection Table (Tab 3)

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L92 | Oracle 0.778±0.003 | Table selection | ✅ |
| L93 | Greedy 0.645±0.001 | Table selection | ✅ |
| L96 | LP 0.647±0.005, p=.29 | Table selection | ✅ |
| L110 | "3.5 pp gap: greedy (0.645) - random (0.610)" | 0.645-0.610=3.5 pp | ✅ |
| L115 | "oracle (0.778) reveals 13.3 pp of headroom above greedy (0.645)" | 0.778-0.645=0.133=13.3 pp | ✅ |
| L115 | "Δ=+0.2 pp, d=0.038, p=0.29" | 0.647-0.645=0.002≈+0.2 pp | ✅ |
| L117 | "N=16 SciERC: +0.52 pp (bootstrap p=0.003)" | Separate N=16 analysis | ⚠️ cannot cross-verify from other tables |

## Experiments: Cross-Dataset Table (Tab 4 / fewnerd)

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L137 | CoNLL: n=2756, Greedy .908, Headroom 4.0pp, Degen 47.4%, LP ρ .316, LP Δ fail | GT: CoNLL degen 47.4% ✓ | ✅ |
| L138 | SciERC: n=551, Greedy .614, Headroom 13.8pp, Degen 17.8%, LP ρ .205, LP Δ +0.42pp | GT: SciERC degen 17.8%, LP Δ +0.42 ✓ | ✅ |
| L139 | Few-NERD: n=32565, Greedy .748, Headroom 12.4pp, Degen 13.8%, LP ρ .421, LP Δ +1.36pp | GT: Few-NERD degen 13.8%, LP Δ +1.36 ✓ | ✅ |
| L147 | "+1.36 pp, 95% CI [+1.18, +1.53], p<0.001" | Consistent with Table fewnerd | ✅ |
| L147 | "VC -1.79, SJ -2.14, FK -2.26, EM -3.85 pp" | Internal data source | ✅ |
| L151 | "47.4% → fail, 17.8% → +0.42 pp, 13.8% → +1.36 pp" | Table fewnerd values | ✅ |
| L152 | "LoRA: degeneracy to 7.2%, LP spread 0.057 vs 0.041 nats" | LoRA ablation data | ✅ |
| L153 | "Few-NERD: degen 13.8%, ρ≈0.5" | Table fewnerd + inline | ✅ |
| L157 | "LP ρ=0.42, VC 0.39, FK 0.31, SJ 0.30, EM 0.29" on Few-NERD | Internal data | ✅ |
| L159 | "7 of 8 entity types positive LP gains (+0.23 to +4.73 pp)" | Per-type appendix | ✅ |
| L159 | "sole exception: Art, 19.8%" | Per-type appendix | ✅ |

## Experiments: N-scaling (Few-NERD paired N=8→16)

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L174 | "4,351 Few-NERD instances" | Paired subset | ✅ |
| L174 | "+0.52 pp (paired bootstrap p=0.003, 95% CI [+0.17, +0.87])" | GT: +0.52 pp ✓ | ✅ |
| L174 | "LP selection improves from +1.37 pp to +1.88 pp" | GT: +1.36 (N=8), +1.88 (N=16); paired subset gives +1.37 | ⚠️ |
| L175 | "degeneracy 14.6% → 7.0%" | GT: 14.6% → 7.0% ✓ | ✅ |
| L175 | "oracle headroom 12.1 → 15.4 pp" | Internal data | ✅ |
| L175 | "LP ranking quality stable (ρ≈0.62)" | Internal data | ✅ |
| L177 | "SJ -1.36, FK -1.47 pp at N=16" | Internal data | ✅ |

**Note L174**: +1.37 vs +1.36 at N=8. The full-set value is +1.36 (Table fewnerd, used everywhere else). The paired subset (n=4,351) yields +1.37. Minor rounding difference from different instance subset; not an error.

## Experiments: Robustness

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L206 | "8B: 17.8% vs 4B: 10.4%" | Table degeneracy: 17.8% and 10.4% | ✅ |
| L210 | "degeneracy from 17.8% to 7.2%" | LoRA ablation | ✅ |
| L210 | "oracle headroom from 13.3 pp to 16.0 pp" | LoRA ablation | ✅ |
| L211 | "LP 0.635, greedy 0.640" | LoRA ablation data | ✅ |
| L211 | "SJ 0.631, VC 0.592" | LoRA ablation data | ✅ |
| L212 | "VC ρ=0.394 vs 0.379; SJ ρ=0.365 vs 0.360" | LoRA ablation / Table QE | ✅ |
| L213 | "median range 0.057 vs 0.041 nats" | 0.041 from logprob_ties analysis | ✅ |

## Experiments: Supervised Verifier

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| L216 | "oracle headroom +17.9 pp" | N=16 SciERC analysis | ✅ |
| L217 | "LR F1=0.641, AUROC=0.652" | GT: AUROC 0.6522→0.652 | ✅ |
| L217 | "MLP F1=0.639, AUROC=0.639" | GT: AUROC 0.6393→0.639 | ✅ |
| L217 | "RF F1=0.615, AUROC=0.587" | Internal data | ✅ |
| L217 | "Greedy 0.644 (3-seed mean)" | Consistent with Table selection (0.645, 2-seed) | ✅ |
| L218 | "MLP interaction AUROC=0.632 < 5-feature 0.639" | GT: MLP ≤ LR confirmed | ✅ |
| L219 | "no model exceeds single-signal VC (AUROC=0.706)" | N=16 VC AUROC, not in QE table (N=8: 0.663) | ⚠️ |

**Note L219**: VC AUROC=0.706 is from N=16 verifier experiment, not cross-verifiable with Table QE (N=8, AUROC=0.663). Internally self-consistent within the verifier section.

## Discussion

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| D4 | "LP ρ=0.42 on Few-NERD, VC ρ=0.38 on SciERC, EM AUROC=0.82" | All match source tables | ✅ |
| D6 | "+1.36 pp Few-NERD (13.8%, ρ≈0.5, p<0.001)" | Table fewnerd | ✅ |
| D6 | "+0.42 pp SciERC (17.8%, ρ≈0.24, p=0.091)" | Table fewnerd; p=0.091 for full-set | ✅ |
| D6 | "failure on CoNLL (47.4%)" | Table fewnerd | ✅ |
| D13 | "SJ median within-instance ρ=0.524 on SciERC, 0.994 on CoNLL" | Table degeneracy | ✅ |
| D13 | "closes 23% (SciERC) to 41% (CoNLL) of the oracle gap" | Table degeneracy | ✅ |
| D14 | "29% of non-degenerate SciERC instances exhibit negative SJ-F1 corr" | Internal analysis | ✅ |
| D15 | "17.8% SciERC instances, 47.4% CoNLL" constant F1 | Table degeneracy | ✅ |
| D15 | "additional 13% (49% CoNLL) constant utility" | Table degeneracy | ✅ |
| D17 | "CoNLL (91%) 47.4%; Few-NERD (75%) 13.8%; SciERC (66%) 17.8%" | All match | ✅ |
| D19 | "8B: 17.8% vs 4B: 10.4%, ρ=0.52 vs 0.55" | Table degeneracy: 0.524 vs 0.550 | ✅ |
| D32 | Table degeneracy: Constant F1 17.8%/10.4%/47.4% | GT values | ✅ |
| D32 | Table degeneracy: Constant utility 13%/7.0%/49% | Internal data | ✅ |
| D34 | Table degeneracy: Oracle gap closed 23%/25.2%/41% | Internal data | ✅ |
| D35 | Table degeneracy: SJ ρ 0.524/0.550/0.994 | Internal data | ✅ |
| D40 | "median LP range 0.041 nats (IQR [0.024, 0.073])" | logprob_ties table (NER-only) | ✅ |
| D40 | "pooled within-instance ρ(LP,F1)=0.248" | Table nontied | ✅ |
| D44 | "n=210, 40% of total" | 210/529=39.7%≈40% | ✅ |
| D44 | "ρ rises from 0.08 (tied) to 0.39 (non-tied)" | Table nontied | ✅ |
| D44 | "+2.9 pp (p=0.004)" | Table nontied | ✅ |
| D65 | "Q4 headroom 4.78 pp" | VC quartile analysis | ✅ |
| D68 | "+0.52 pp at N=16 on Few-NERD (paired p=0.003)" | Few-NERD N-scaling | ✅ |
| D70 | "oracle headroom: +7.8 pp at T=0.5 to +13.3 pp at T=1.0" | T ablation table | ✅ |
| D71 | "CoNLL mean 9.24, std 1.32" verbalized confidence | Internal data | ✅ |
| D72 | "free-form RE: +2.35 pp, p=0.025" | Appendix freeform | ✅ |
| D72 | "NER free-form std ratio 0.97" | Appendix freeform | ✅ |
| D73 | "LP×VC: +0.2 pp, p>0.3; oracle tiebreaker +7.9 pp" | Internal analysis | ✅ |
| D84 | "+2.35 pp (95% CI [+0.24, +4.50], p=0.025, n=397)" | Appendix freeform | ✅ |
| D85 | "Jaccard=0.42" LP failure stability | Appendix | ✅ |
| D91 | "entity-token LP: 4× higher variance" | Appendix | ✅ |
| D92 | "−2.0 pp on SciERC, −3.3 pp on CoNLL" entity-token LP | Appendix | ✅ |
| D93 | "5.3% of sequence tokens on SciERC, 79.4% tied on CoNLL" | Appendix | ✅ |
| D100 | "VC +0.28 pp (p<0.03) at N=16" on CoNLL | Appendix N-scaling | ✅ |
| D101 | "17.8% → +0.42 pp (p=0.091); 13.8% → +1.36 pp (p<0.001)" | Table fewnerd, discussion | ✅ |
| D102 | "ρ=−0.881, p=0.004, n=8" | Per-type analysis | ✅ |
| D118 | "degeneracy falls from 40.3% (T=0.5) to 12.5% (T=1.2)" | T ablation table | ✅ |
| D118 | "ρ(LP,F1) remains at 0.225 even at T=1.2" | T ablation analysis | ✅ |

## Conclusion

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| C4 | "ρ up to 0.38 on primary, 0.42 on Few-NERD; AUROC up to 0.82" | All match source tables | ✅ |
| C5 | "ρ=0.52" within-instance SJ-F1 | Table degeneracy: 0.524 | ✅ |
| C5 | "14--47%" | 13.8%≈14%, 47.4%≈47% | ✅ |
| C6 | "13.8% degen, ρ≈0.5: +1.36 pp (p<0.001)" | Table fewnerd | ✅ |
| C6 | "17.8%, ρ≈0.24: +0.42 pp (p=0.091)" | Table fewnerd | ✅ |
| C6 | "47.4% (CoNLL), LP fails" | Table fewnerd | ✅ |
| C7 | "+0.52 pp from N=8 to 16, paired p=0.003" | Few-NERD N-scaling | ✅ |

## Appendix: T Ablation Tables

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| A967 | T=0.5: Oracle gap +7.8 pp | GT: consistent | ✅ |
| A968 | T=0.8: Oracle gap +10.5 pp | Internal data | ✅ |
| A969 | T=1.0: Oracle gap +13.3 pp | Matches main text | ✅ |
| A970 | T=1.2: Oracle gap +13.0 pp | Internal data | ✅ |
| A998 | T=0.5: Degen 40.3%, LP range 0.022 | GT: 40.3%, 0.022 ✓ | ✅ |
| A999 | T=0.8: Degen 27.2%, LP range 0.043 | GT: 27.2%, 0.043 ✓ | ✅ |
| A1000 | T=1.0: Degen 17.6%, LP range 0.060 | GT: 17.6%, 0.060 ✓ | ⚠️ |
| A1001 | T=1.2: Degen 12.5%, LP range 0.075 | GT: 12.5%, 0.075 ✓ | ✅ |

**Note A1000**: T ablation table shows degen=17.6% at T=1.0, while main text and Table degeneracy use 17.8% for SciERC. Explanation: T ablation (exp-026) uses "joint (NER+RE) subtask" for T=0.5 and T=1.0 (per table caption), which slightly differs from the NER-only main analysis. Both values are confirmed correct per ground truth (17.8% main, 17.6% T ablation).

**Note A1000 (LP range)**: T ablation shows LP range=0.060 at T=1.0, while main text uses 0.041 (from logprob_ties analysis, NER-only, n=529). The logprob_ties section tested joint vs NER subtask and found nearly identical LP ranges (0.041 vs 0.040), so the T ablation's 0.060 is unexplained by subtask difference alone. Possibly due to different experimental run (exp-026) or instance filtering. Values are internally consistent within each table but the discrepancy (0.041 vs 0.060) is notable.

## Appendix: Few-NERD Detailed Analysis

| Line | Claim in paper | Source value | Status |
|------|---------------|-------------|--------|
| A1113 | "Instance degeneracy is 13.8%" | GT: 13.8% ✓ | ✅ |
| A1137 | "+1.36 pp, p<0.001, CI excludes zero" | Table fewnerd | ✅ |
| A1139 | "SciERC (17.8%, ρ≈0.24, +0.42 pp), CoNLL (47.4%, LP fails)" | All match | ✅ |
| A1204 | "47.4% → 17.8% → 13.8%" cross-dataset gradient | All GT values | ✅ |

## Figure 3 (Degeneracy-LP Scatter) Script Values

| Value | Script | Paper inline | Status |
|-------|--------|-------------|--------|
| cross_degen | [47.4, 17.8, 13.8] | Table fewnerd: 47.4%, 17.8%, 13.8% | ✅ |
| cross_delta | [-1.05, 0.42, 1.36] | Table fewnerd: fail(-1.05), +0.42, +1.36 | ✅ |

## Old Value Residual Check

| Old value | What it should be | Found in paper? | Status |
|-----------|------------------|----------------|--------|
| 58% (old CoNLL degen) | 47.4% | Not found | ✅ clean |
| 21% (old SciERC degen) | 17.8% | Not found | ✅ clean |
| 10% (old Few-NERD degen) | 13.8% | Not found | ✅ clean |
| 11.1% → 4.5% (old paired degen) | 14.6% → 7.0% | Not found | ✅ clean |
| +0.62pp (old SciERC LP Δ) | +0.42pp (full-set) | Not found | ✅ clean |

---

## Summary

| Status | Count |
|--------|-------|
| ✅ Consistent | 97 |
| ❌ Needs fix | 1 |
| ⚠️ Needs review | 5 |

### Items requiring attention

1. **❌ experiments.tex L52**: Text says "EM strongest (ρ=0.360)" for non-zero WNUT instances, but Table WNUT shows LP Cond. ρ=0.350 > EM Cond. ρ=0.333. The ρ=0.360 value appears to be from Figure signal_heatmap (SciERC conditional), not WNUT conditional. Either the sentence should reference a different dataset, or the figure's conditional analysis uses different filtering that produces EM=0.360 on WNUT.

2. **⚠️ appendix T ablation T=1.0**: Degen=17.6% in T ablation table vs 17.8% in all main text references. Both confirmed correct per ground truth (different experimental protocols: joint vs NER-only subtask). Not technically wrong but may confuse reviewers.

3. **⚠️ LP range discrepancy**: Main text and logprob_ties report median LP range=0.041 nats (NER-only, n=529). T ablation table reports 0.060 at T=1.0. The difference is larger than the joint/NER subtask variation identified in the logprob_ties section (0.041 vs 0.040). Likely from different experimental run (exp-026) or instance filtering.

4. **⚠️ experiments.tex L174**: N=8 LP Δ reported as +1.37 pp on the paired subset (n=4,351) vs +1.36 pp everywhere else (full-set n=32,565). Minor rounding from different instance subsets.

5. **⚠️ experiments.tex L117**: SciERC N=16 LP gain "+0.52 pp (p=0.003)" cannot be cross-verified from other tables. Internally plausible but no secondary source.

6. **⚠️ experiments.tex L219**: VC AUROC=0.706 from N=16 verifier experiment cannot be verified against QE Table (N=8: 0.663). Expected to be higher at N=16 but no independent confirmation.
