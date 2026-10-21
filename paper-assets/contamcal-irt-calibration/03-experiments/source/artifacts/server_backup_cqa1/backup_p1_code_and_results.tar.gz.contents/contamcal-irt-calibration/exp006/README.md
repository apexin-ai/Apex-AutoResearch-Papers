# exp-006: IRT Calibration + 7 Baselines

Core experiment for ContamCal. Fits 4PL+γ IRT model to estimate contamination-adjusted benchmark scores, compares against 7 baselines.

## Dependencies

```
cmdstanpy, numpy, scipy
```

Stan models (pre-compiled): `../stan_models/contam_irt_4pl_simple.stan`, `contam_irt_2pl_gamma.stan`, `vanilla_4pl.stan`

## Data Flow

```
exp-001 eval_results/        →  response matrix (N_models × N_items)
exp-002/003 exposure_scores  →  exposure matrix (per-item τ × dosage)
                                        ↓
                              run_exp006.py (pipeline)
                             ┌──────────┴──────────┐
                    run_irt_calibration.py    baselines.py (B0-B6)
                             └──────────┬──────────┘
                                        ↓
                            evaluate_calibration.py
                                        ↓
                          {benchmark}_evaluation.json + .tex
```

## Quick Start

```bash
# Dry-run (synthetic data, no Stan)
python exp006/run_all_baselines.py --dry-run --skip-stan

# Full pipeline (per-benchmark IRT + baselines + evaluation)
python exp006/run_exp006.py \
    --eval-dir /root/autodl-tmp/exp001/eval_results \
    --exposure-file /path/to/exposure_scores.json \
    --output-dir /root/autodl-tmp/exp006/results

# With joint fitting ablation
python exp006/run_exp006.py --joint-fit \
    --eval-dir /root/autodl-tmp/exp001/eval_results \
    --output-dir /root/autodl-tmp/exp006/results

# Dry-run of full pipeline (truncated items, skip Stan baselines)
python exp006/run_exp006.py --dry-run --skip-stan --max-items 20 \
    --output-dir /tmp/exp006_test
```

## Scripts

| File | Purpose |
|------|---------|
| `run_exp006.py` | End-to-end pipeline: IRT + baselines + evaluation |
| `run_irt_calibration.py` | Standalone IRT fitting (per-benchmark or direct matrix) |
| `joint_fit.py` | Joint fitting ablation (shared global γ across benchmarks) |
| `baselines.py` | 7 baseline methods with unified `BaselineMethod.fit()` interface |
| `evaluate_calibration.py` | 8 evaluation metrics + LaTeX/text table output |
| `run_all_baselines.py` | Standalone baseline runner with synthetic data support |
| `run_irt_stan.py` | Alternative Stan-only IRT runner |

## Baselines

| ID | Method | Description |
|----|--------|-------------|
| B0 | Raw | No adjustment (anchor) |
| B1 | Remove-and-rescore | Drop items with exposure > p75, rescore |
| B2 | Single-signal 2PL+γ | Simplified IRT (no c/d) with contamination covariate |
| B3 | Vanilla 4PL | Standard IRT without γ |
| B4 | Linear regression | Regress accuracy on mean exposure + bootstrap CI |
| B5 | Emperor's mitigation | Rephrasing / exposure-weighted downweighting |
| B6 | DCR fuzzy inference | Xu et al. (EMNLP 2025) adapted |

## Evaluation Metrics

1. **MAE** — mean absolute error (calibrated vs ground-truth clean scores)
2. **ECE** — expected calibration error (binned)
3. **MCE** — maximum calibration error
4. **Brier Score** — mean squared error
5. **Coverage** — fraction of GT within 50/80/95% CIs
6. **Sharpness** — mean CI width (lower is better, conditional on coverage)
7. **Kendall τ** — rank correlation preservation
8. **Dose-response** — γ posterior: sign, magnitude, CI excludes zero

## Design Decisions

- **D011**: CmdStanPy Bayesian inference (NUTS)
- **D013**: Simple IRT model only (ME model deprecated)
- **D016**: Min-K++ reference = 0% dosage fine-tuned model
- **D018**: 3B GSM8K excluded from dose-response analysis

## Output Structure

```
output_dir/
├── exp006_results.json          # combined results
├── {benchmark}/
│   ├── 4pl_gamma_results.json   # IRT fit results
│   ├── baselines.json           # all baseline results
│   ├── evaluation.json          # all metrics
│   └── evaluation.tex           # LaTeX table
└── joint_fit/                   # (with --joint-fit)
    └── joint_fit_results.json
```
