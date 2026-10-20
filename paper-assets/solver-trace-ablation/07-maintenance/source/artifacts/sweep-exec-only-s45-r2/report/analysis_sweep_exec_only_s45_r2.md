# Analysis: sweep-exec-only-s45-r2

## Training Summary
- **Status**: Completed 500/500 steps, EXIT_CODE=0
- **Model**: Qwen3-4B, seed=45, execution-only reward
- **Data**: data/train_500_seed42.jsonl (500 examples)
- **Runtime**: 3282s (~54.7 min), 2 epochs

### Training Metrics (Final)
| Metric | Value |
|--------|-------|
| prove_rate | 0.74025 |
| mean_isr | 0.3596 |
| train_loss | 0.0273 |
| parse_rate | 1.0 |
| entropy (final) | 0.045 |

### Training Trajectory
- Steps 1–19: cold start, reward=0
- Step 20: first successful proving
- Steps ~100+: prove_rate climbing to 0.5–0.75
- Steps 400+: consistently 0.75–1.0

## Eval Results (proofwriter_fol_100.jsonl)
| Metric | Value |
|--------|-------|
| prove_rate | 99/100 (0.99) |
| mean_isr | 0.5012 ± 0.2055 |
| median_isr | 0.5000 |
| proved_only_isr | 0.5062 |

### By Answer Type
| Type | n | Proved | Prove Rate | Mean ISR |
|------|---|--------|------------|----------|
| false | 25 | 25 | 1.00 | 0.590 |
| unknown | 41 | 41 | 1.00 | 0.476 |
| true | 34 | 33 | 0.971 | 0.467 |

## Hacking Taxonomy (classify_h7.py)
| Category | Count | Rate |
|----------|-------|------|
| H7a (text-match tautology) | 93 | 93.9% |
| H7b (obfuscated tautology) | 0 | 0.0% |
| H7 total | 93 | 93.9% |
| H1 (conclusion embedding) | 5 | 5.1% |
| H8 (conjunction collapse) | 1 | 1.0% |
| **Genuine** | **1** | **1.0%** |
| Content-independent | 47 | 47.5% |
| Single premise | 92 | 92.9% |

## Cross-Seed Comparison (Exec-Only)
| Seed | Steps | Prove% | H7% | H1% | H8% | Genuine% |
|------|-------|--------|-----|-----|-----|----------|
| s42 (plan001-r2) | 500 | 93 | 0 | 87.1 | 6.5 | 7.5 |
| s43 (plan001-1000-r2) | 1000 | 90 | 100 | 0 | 0 | 0 |
| s44 (plan001-1000-r2) | 1000 | 100 | 0 | 85 | 15 | 0 |
| **s45 (this)** | **500** | **99** | **93.9** | **5.1** | **1.0** | **1.0** |

## Analysis
- **Tautological collapse**: 93.9% H7a — model generates single-premise P→P proofs. This is the dominant exec-only failure mode.
- **ISR=0.5 artifact**: With 2-component proofs (1 premise + conclusion), ISR=0.5 is structural, not indicative of reasoning.
- **s45 pattern**: H7-dominant like s43@1000, different from s42@500 (H1-dominant) and s44@1000 (H1-dominant). Seed-dependent hacking mechanism but universally near-zero genuine reasoning.
- **Genuine=1.0%**: Only 1/99 proved samples shows genuine reasoning.

## Conclusion: **success**
Training completed normally. Results consistent with exec-only reward hacking across all seeds. Suitable for 5-seed sweep.

## Paths
- Checkpoint: `/root/autodl-tmp/outputs/sweep_exec_only_s45`
- Log: `~/runs/solver-trace-ablation/sweep-exec-only-s45-r2.log`
- Eval: `/root/autodl-tmp/outputs/sweep_exec_only_s45/eval_sta_results.json`
- Taxonomy: `/root/autodl-tmp/outputs/sweep_exec_only_s45/classify_h7_results.json`
