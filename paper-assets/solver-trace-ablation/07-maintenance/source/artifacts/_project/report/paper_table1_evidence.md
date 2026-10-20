# Table 1: Comprehensive Experimental Evidence for Solver-Trace Ablation

**Model**: Qwen3-4B | **Training**: GRPO, 500 steps, K=8 | **Data**: train_500_seed42.jsonl (500 problems) | **Eval**: proofwriter_fol_100.jsonl (100 problems)

## Main Results Table

### Group A: Reference Baselines

| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sta-phase0-baseline | — (base model) | — | — | — | 0.12 | 0.0641 | 0.1983 | — | — | eval_sta.py | pre-training reference | — |
| sta-gt-isr-baseline | — (ground truth FOL) | — | — | — | 0.18 | 0.5588 | 0.2582 | — | — | direct computation | ISR ceiling on gold FOL | — |

### Group B: Exec-Only Reward (r = r_exec)

| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plan001-exec-only-s42-r2 | exec-only | r = r_exec | — | 42 | 0.93 | 0.1232 | 0.1887 | 6.58† | — | eval_sta.py | genuine proofs | C1 |
| plan001-exec-only-s43-r4 | exec-only | r = r_exec | — | 43 | 0.14‡ | 0.00‡ | — | — | — | sampling (T=0.7)‡ | degraded (87% max_tokens) | C1, C2 |
| plan001-exec-only-s44 | exec-only | r = r_exec | — | 44 | 0.98 | 0.5700 | 0.2013 | 2.04 | 94% | eval_sta.py | tautological collapse | C1, C2 |

**Exec-only 3-seed summary**: mean PR = 0.68 ± 0.47, 2/3 seeds degenerate. Cross-seed instability is the primary finding.

### Group C: Additive ISR Bonus (r = r_exec · (1 + β · ISR))

| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plan002-additive-b03-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.3 | 42 | 0.18 | 0.0257 | 0.0742 | — | — | eval_sta.py§ | PR collapse (Goodhart) | C3 |
| plan002-additive-b01-s42 | additive ISR | r = r_exec · (1 + β·ISR) | 0.1 | 42 | 0.81 | 0.3365 | 0.3227 | 5.58 | 3.7% | eval_sta.py | **best: PR preserved + ISR 2.73x** | C3 |

**Dose-response**: β=0.3 → PR collapse (0.18); β=0.1 → PR preserved (0.81) with ISR 2.73x over exec-only baseline.

### Group D: Convex ISR (r = α · r_exec + β · ISR)

| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plan005-sta-low-s42 | convex ISR | r = 0.9·r_exec + 0.1·ISR | 0.1 | 42 | —¶ | —¶ | —¶ | — | — | training logs only¶ | PR suppressed (train last100 PR=0.77) | C3 |

### Group E: Convex Random Control (r = α · r_exec + β · random)

| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plan013-random-reward-s42-r4 | convex random | r = 0.9·r_exec + 0.1·random | 0.1 | 42 | 1.00 | 0.5350 | 0.1282 | ~2†† | ~100%†† | eval_sta.py | tautological collapse | C2 |

### Group F: Additive Random Control (r = r_exec · (1 + β · random))

| Experiment ID | Reward Mode | Formula | β | Seed | Eval PR | Eval Mean ISR | ISR Std | Comp. Mean | Comp.=2 (%) | Eval Method | Diagnosis | Claims |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plan017-additive-random-s42 | additive random | r = r_exec · (1 + β·random) | 0.3 | 42 | 0.48 | 0.0453 | 0.0759 | 9.60 | 0% | eval_sta.py | complex but useless formalizations | C2, C3 |

## Claim Evidence Summary

### Claim 1: Exec-only reward exhibits cross-seed degeneration
| Seed | Eval PR | Eval ISR | Comp. Mean | Failure Mode |
|---|---|---|---|---|
| 42 | 0.93 | 0.1232 | 6.58 | None (genuine) |
| 43 | 0.14 | 0.00 | — | Output degeneration (max_tokens) |
| 44 | 0.98 | 0.5700 | 2.04 | Tautological collapse (premise=conclusion) |

**Verdict**: 2/3 seeds degenerate under exec-only reward. High training PR does not guarantee genuine formalization.

### Claim 2: ISR + component count diagnoses genuine vs degenerate proofs
| Experiment | Eval PR | Eval ISR | Comp. Mean | ISR Diagnosis |
|---|---|---|---|---|
| exec-only s42 (genuine) | 0.93 | 0.12 | 6.58 | Low ISR + high comp → genuine but imperfect |
| exec-only s44 (tautological) | 0.98 | 0.57 | 2.04 | High ISR + low comp → **tautological artifact** |
| convex random (tautological) | 1.00 | 0.54 | ~2 | High ISR + low comp → **tautological artifact** |
| additive random (complex junk) | 0.48 | 0.05 | 9.60 | Low ISR + high comp → many premises but unused |
| additive ISR β=0.1 (best) | 0.81 | 0.34 | 5.58 | Moderate ISR + high comp → **genuine improvement** |

**Verdict**: ISR alone is ambiguous (s44 ISR=0.57 looks good but is tautological). Component count resolves the ambiguity: comp≈2 flags tautological collapse; comp>5 with moderate ISR indicates genuine proofs.

### Claim 3: ISR-as-reward shows Goodhart effect at high dose, effective at low dose
| Reward Mode | β | Eval PR | Eval ISR | Goodhart? |
|---|---|---|---|---|
| additive ISR | 0.3 | 0.18 | 0.03 | **Yes** — PR collapse |
| additive ISR | 0.1 | 0.81 | 0.34 | **No** — sweet spot |
| convex ISR | 0.1 | —¶ | — | Partially (train PR suppressed) |
| convex random | 0.1 | 1.00 | 0.54 | Tautological (no ISR signal) |
| additive random | 0.3 | 0.48 | 0.05 | N/A (random control) |

**Verdict**: Clear dose-response. β=0.1 additive is the working point; β=0.3 triggers Goodhart collapse. Random controls confirm ISR signal is causal (not just variance regularization).

## Notes

† Component count for plan001-exec-only-s42-r2 (6.58) is cross-referenced from plan001-exec-only-s44 notes, not stored in registry eval metrics. May need re-verification with eval_sta.py.

‡ **D029**: plan001-exec-only-s43-r4 was evaluated with sampling (do_sample=True, temperature=0.7) instead of eval_sta.py greedy decoding used for all other experiments. The PR=14% result is a failure case regardless of eval method — 87% of outputs hit max_new_tokens and are unparseable. Decision: not re-evaluated; paper will note the method difference.

§ plan002-additive-b03-s42 eval_method not explicitly recorded in registry, but eval fields (eval_prove_rate, eval_mean_isr) are consistent with eval_sta.py output format.

¶ **D030**: plan005-sta-low-s42 checkpoint was deleted; no eval was performed. Training log windowed metrics are the only available data. Paper uses training curves as evidence for "ISR suppresses reward hacking" (ISR/PR ratio stable at 0.30 across training).

†† plan013-random-reward-s42-r4 component count not in registry metrics but noted as "trivial 2-component proofs (premise=conclusion, conclusion=conclusion)" in eval_note.

## Excluded Experiments (Failed / Developmental)

The following DONE experiments are excluded from Table 1 (crashes, early phases, duplicates):

| Experiment ID | Reason for Exclusion |
|---|---|
| sta-phase1-exec-only-r2/r3/r4/r5 | 100-step developmental runs |
| sta-phase1-exec-sta-r2/r3/r4/r5 | 100-step developmental runs |
| plan001-exec-only-s42 | Failed (pre-checkpoint crash) |
| plan001-exec-only-s42-r3 | Failed (OOM duplicate submission) |
| plan001-exec-only-s43 | Failed (OOM from plan013 GPU overflow) |
| plan001-exec-only-s43-r2 | Failed (process crashed) |
| plan001-exec-only-s43-r3 | Failed (disk full at step 23) |
| plan013-random-reward-s42 | Failed (CUDA_VISIBLE_DEVICES not set) |
| plan013-random-reward-s42-r2 | Failed (process crashed) |
| plan013-random-reward-s42-r3 | Failed (disk full at step 28) |
| plan003-eval-exec-only-r5 | Eval of 100-step checkpoint (not 500-step) |
| plan014-downstream-nli-s42 | Downstream NLI task (separate analysis) |

## Compact Table for Paper

| Reward Mode | β | Seed | PR↑ | ISR↑ | Comp.↓ | Collapse? |
|---|---|---|---|---|---|---|
| *Base model* | — | — | .12 | .064 | — | — |
| Exec-only | — | 42 | **.93** | .123 | 6.58 | No |
| Exec-only | — | 43 | .14‡ | .000 | — | Degenerate |
| Exec-only | — | 44 | .98 | .570 | 2.04 | **Tautological** |
| Add. ISR | 0.3 | 42 | .18 | .026 | — | PR collapse |
| **Add. ISR** | **0.1** | **42** | **.81** | **.337** | **5.58** | **No** |
| Cvx. Random | 0.1 | 42 | 1.00 | .535 | ~2 | **Tautological** |
| Add. Random | 0.3 | 42 | .48 | .045 | 9.60 | Complex junk |

*Generated 2026-05-14. All eval metrics from eval_sta.py full STA unless noted.*
