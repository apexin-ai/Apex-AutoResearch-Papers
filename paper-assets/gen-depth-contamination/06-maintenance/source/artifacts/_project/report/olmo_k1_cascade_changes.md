# OLMo K*=1 Cascade Update — Change Log

## Data Source
OLMo-1B C4 standardized pipeline rerun:
- K* changed from 2 → 1 (θ=0.60)
- 0v1 AUC: 0.9860 [0.9843, 0.9877], p=0.0001
- 1v2 AUC: 0.5080 [0.4962, 0.5188], p=0.0955
- 2v3 AUC: 0.4973 [0.4855, 0.5085], p=0.6894
- 3v4 AUC: 0.5024 [0.4905, 0.5134], p=0.3631
- 4v5 AUC: 0.4942 [0.4827, 0.5057], p=0.8357

## Changes by File

### experiments_c1.tex
| Location | Old | New |
|----------|-----|-----|
| Table 2 (tab:kstar_ci), OLMo 0v1 | .9970 | .9860 |
| Table 2, OLMo 1v2 | .6145 [.605,.625]* | .5080 [.496,.519] (no asterisk) |
| Table 2, OLMo 2v3 | .5496 [.540,.560] | .4973 [.486,.509] |
| Table 2, OLMo 3v4 | .5091 | .5024 |
| Table 2, OLMo 4v5 | .5045 | .4942 |
| Line 43 | 7/8 yield K*=2...Mistral-7B sole exception | 6/8 yield K*=2...OLMo-1B and Mistral-7B yield K*=1 |
| Line 55 (Fig caption) | All configurations yield K*=2 | Five of six yield K*=2; OLMo yields K*=1 |
| Line 46 | spread across models in continuation mode (Δ=3.9pp) | spread across K*=2 continuation models (Δ=4.3pp) |
| Line ~60 | unanimous K*=2 holds within θ∈[0.58,0.60] | five of six yield K*=2 within θ∈[0.51,0.61]; OLMo: K*=1 throughout |
| Line 97 | 15D features yield consistent K*=2 across all families | 15D features yield K*=2 for most families (OLMo: K*=1) |

### main.tex
| Location | Old | New |
|----------|-----|-----|
| Line 36 (abstract) | 7/8 configurations | 6/8 configurations |
| Line 38 (abstract) | 80--92% cross-model transfer | 80--100% cross-model transfer |
| Line 70 (limitations) | 7/8...Mistral-7B: K*=1 | 6/8...OLMo-1B, Mistral-7B: K*=1 |

### introduction.tex
| Location | Old | New |
|----------|-----|-----|
| Line 21 | 7/8 model configurations | 6/8 model configurations |
| Line 22 | 80--92% accuracy retention | 80--100% accuracy retention |

### conclusion.tex
| Location | Old | New |
|----------|-----|-----|
| Line 5 | 7/8 configurations | 6/8 configurations |
| Line 6 | 80--92% cross-model transfer | 80--100% cross-model transfer |

### discussion.tex
| Location | Old | New |
|----------|-----|-----|
| Line 20 | Pythia and OLMo match the 15D boundary at K*_neural=2 | Pythia and OLMo yield K*_neural=2 |
| Line 21 | 7/8 configurations K*≤2 | 6/8 configurations K*=2 |
| Line 34 | 7 yield K*=2; Mistral-7B sole sub-2 exception | 6 yield K*=2; OLMo-1B and Mistral-7B fall below θ |

### appendix.tex
| Location | Old | New |
|----------|-----|-----|
| Extended table (tab:kstar_ci_extended) caption | K*=2 confirmed across all conditions | K*=2 holds for 6/8 conditions |
| Extended table, OLMo 0v1 | .9970 | .9860 |
| Extended table, OLMo 1v2 | .6145 [.605,.625]* | .5080 [.496,.519] |
| Extended table, OLMo 2v3 | .5496 [.540,.560] | .4973 [.486,.509] |
| Extended table, OLMo 3v4 | .5091 | .5024 |
| Extended table, OLMo 4v5 | .5045 | .4942 |
| Exp-007 table (tab:s8_cv_folds) caption | except OLMo 3v4 and 4v5 | except OLMo 1v2 through 4v5 |
| Exp-007, OLMo 0v1 | .997 [.996,.998] | .986 [.984,.988] |
| Exp-007, OLMo 1v2 | .615 [.605,.625] | .508 [.496,.519] |
| Exp-007, OLMo 2v3 | .550 [.540,.560] | .497 [.486,.509] |
| Exp-007, OLMo 3v4 | .509 [.497,.520]† | .502 [.491,.513] |
| Exp-007, OLMo 4v5 | .505 [.493,.515]‡ | .494 [.483,.506] |
| Exp-007 footnote | †p=0.064; ‡p=0.232 | OLMo 1v2-4v5 p>0.09 |
| Table S13 (scorer sensitivity), OLMo self-score | 2 | 1 |

### appendix_extended.tex
| Location | Old | New |
|----------|-----|-----|
| Line 11 | 80--92% accuracy | 80--100% accuracy |
| Line 52 | 2 for Pythia and OLMo, matching the 15D boundary | 2 for Pythia and OLMo |
| Line 53 | 15D features yield K*=2 consistently across all three families | 15D features yield K*=2 for Pythia and Qwen; OLMo yields K*=1 |

## Compilation
- **Status**: Success
- **Total pages**: 20 (main body ~8 + references + appendix)
- **Overfull hbox warnings**: 11 (pre-existing, mostly in appendix tables)

## P3: Domain Ordering
- No "C4 = Code" or "domain ordering" text found in any .tex file. P3 not applicable.

## Not Changed (verified correct)
- Neural probe table (tab:neural_probe_crossmodel): K*_neural=2 for OLMo is correct (different measurement)
- Cross-model transfer matrix (tab:s1_transfer): accuracy numbers unchanged (different experiment)
- Feature ranking table (tab:top_features): rankings unchanged
- Domain K* table (tab:domain_kstar): only has Qwen/Pythia, no OLMo
- Method section model list: still lists OLMo-1B, no K* claim
- Appendix_extended line 6: "K*≤2 across all 8" remains correct (K*=1 is ≤2)

## Figures Needing Regeneration
- **fig2_auc_decay.pdf**: OLMo decay curve will show different shape (steep drop to ~0.50 at 1v2)
- **fig_kstar_theta.pdf** (if it exists): OLMo sensitivity curve needs updating
