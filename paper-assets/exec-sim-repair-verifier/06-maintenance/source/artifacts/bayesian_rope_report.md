# Bayesian ROPE Equivalence Analysis

**Date:** 2026-05-22  
**Model:** Qwen3-4B, 5 seeds (42/123/456/789/0)  
**ROPE interval:** ±2 percentage points (matching TOST SESOI)  
**Method:** Bayesian paired t-test with Jeffreys prior; marginal posterior μ | data ~ t(n−1, x̄, s/√n)

## Results

### CLS vs CWM (per-test level)

| Metric | Value |
|--------|-------|
| Mean diff (CLS − CWM) | +1.048 pp |
| SD | 0.765 pp |
| 95% HDI | [+0.10, +2.00] pp |
| P(μ ∈ ROPE) | **0.975** |
| P(μ > +2pp) | 0.025 |
| P(μ < −2pp) | 0.000 |
| **Decision (P(ROPE) > 0.9)** | **Equivalence supported** |
| **Decision (Kruschke HDI)** | **Accept equivalence** (95% HDI entirely inside ROPE) |

### CLS vs TRAJ (per-test level)

| Metric | Value |
|--------|-------|
| Mean diff (CLS − TRAJ) | +1.934 pp |
| SD | 1.279 pp |
| 95% HDI | [+0.35, +3.52] pp |
| P(μ ∈ ROPE) | **0.542** |
| P(μ > +2pp) | 0.457 |
| P(μ < −2pp) | 0.001 |
| **Decision (P(ROPE))** | **Inconclusive** |
| **Decision (Kruschke HDI)** | **Undecided** (95% HDI extends beyond ROPE) |

### CLS vs TRAJ (variant-level, matching TOST data source)

| Metric | Value |
|--------|-------|
| Mean diff (CLS − TRAJ) | −0.486 pp |
| SD | 1.219 pp |
| 95% HDI | [−2.00, +1.03] pp |
| P(μ ∈ ROPE) | **0.970** |
| P(μ > +2pp) | 0.005 |
| P(μ < −2pp) | 0.025 |
| **Decision (P(ROPE) > 0.9)** | **Equivalence supported** |
| **Decision (Kruschke HDI)** | **Accept equivalence** (95% HDI entirely inside ROPE) |

### Sensitivity: ROPE = ±1.5pp

| Comparison | P(ROPE) | Decision |
|-----------|---------|----------|
| CLS–CWM (per-test) | 0.871 | Inconclusive (borderline) |
| CLS–TRAJ (per-test) | 0.243 | Inconclusive |
| CLS–TRAJ (variant) | 0.921 | Equivalence supported |

## Concordance with TOST

| Comparison | TOST p (±2pp) | Holm-adj. | Bayesian P(ROPE) | Agreement |
|-----------|--------------|-----------|------------------|-----------|
| CLS–CWM | 0.007 | 0.028 ✓ | 0.975 | Both confirm equivalence |
| CLS–TRAJ | 0.025 | 0.075 ✗ | 0.542 (per-test) / 0.970 (variant) | Both inconclusive at per-test level; variant level shows equivalence in both paradigms |

## Interpretation

The per-test level CLS–TRAJ discrepancy (P(ROPE)=0.54) reflects that CLS shows a systematic +1.93pp per-test advantage over TRAJ, driven by seed 123 (CLS 89.52% vs TRAJ 85.47%, Δ=4.05pp). At variant level, this gap shrinks to −0.49pp because CLS's all-pass aggregation penalizes variant accuracy while TRAJ predicts variants directly. The two levels tell complementary stories: CLS is better per-test but equivalent per-variant.

## Paper Text (for §5.2 or Appendix)

> **Bayesian ROPE analysis.** To complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired t-test with Jeffreys prior (Kruschke, 2013, 2018). The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For CLS--CWM, the posterior probability within the $\pm$2pp ROPE is $P(\text{ROPE}) = 0.975$, and the 95\% highest density interval (HDI = $[{+}0.10, {+}2.00]$\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For CLS--TRAJ at per-test level, $P(\text{ROPE}) = 0.542$ (inconclusive; 95\% HDI $= [{+}0.35, {+}3.52]$\,pp extends beyond the ROPE), consistent with the TOST non-confirmation after Holm correction ($p_{\text{adj}} = 0.075$). At variant level, CLS--TRAJ equivalence is supported ($P(\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\,pp), reflecting the smaller variant-level gap ($-0.49$\,pp mean). The Bayesian analysis corroborates the TOST conclusions: CLS--CWM equivalence is robust, while CLS--TRAJ parity depends on the aggregation level.

## Citation

- Kruschke, J. K. (2013). Bayesian estimation supersedes the t test. *Journal of Experimental Psychology: General*, 142(2), 573–603.
- Kruschke, J. K. (2018). Rejecting or accepting parameter values in Bayesian estimation. *Advances in Methods and Practices in Psychological Science*, 1(2), 270–280.

```bibtex
@article{kruschke2013bayesian,
  title={Bayesian estimation supersedes the t test},
  author={Kruschke, John K},
  journal={Journal of Experimental Psychology: General},
  volume={142},
  number={2},
  pages={573--603},
  year={2013},
  publisher={American Psychological Association}
}

@article{kruschke2018rejecting,
  title={Rejecting or accepting parameter values in {B}ayesian estimation},
  author={Kruschke, John K},
  journal={Advances in Methods and Practices in Psychological Science},
  volume={1},
  number={2},
  pages={270--280},
  year={2018},
  publisher={SAGE Publications}
}
```

## Data Source

- Per-test accuracies: Table 1 per-seed values (seeds 42/123 verified from Table 2; seeds 456/789/0 from experiment registry)
- Variant-level CLS–TRAJ gaps: `tost_margin_sweep_cls_traj.json` (same data used for paper TOST)
- Analysis script: `bayesian_rope.py` on server
- Raw results: `artifacts/bayesian_rope_results.json` on server
