## α_crit Entity Selection Bound

### Main Table (T=1.0, 3-seed micro-F1 averages, seeds 42/123/456)

| Dataset | π_MV | α_crit | α_obs | Gap (α − α_crit) | Δ_SC (pp) | Degeneracy | Bound Predicts | Empirical |
|---------|------|--------|-------|-------------------|-----------|------------|----------------|-----------|
| FewNERD | 0.7849 | 0.6459 | 0.6405 | −0.0054 | **−0.63** | 9.2% | No | **No** ✓ |
| CoNLL   | 0.9136 | 0.8409 | 0.8716 | +0.0306 | **+0.17** | 59.1% | Yes | **Yes** ✓ |
| SciERC  | 0.6695 | 0.5033 | 0.6087 | +0.1055 | **+0.37** | 8.2% | Yes | **Yes** ✓ |

- **π_MV**: Entity-level majority voting micro-F1 (threshold ≥ N/2 samples)
- **α_obs**: Mean individual sample F1 (`sample_f1_mean`, macro-averaged over instances)
- **Δ_SC**: MV micro-F1 − greedy micro-F1 (positive = SC aggregation wins)
- **Degeneracy**: Fraction of instances with identical entity sets across all n=8 samples
- **All metrics use micro-F1** (aggregate TP/FP/FN then compute F1), correcting the greedy_macro_f1 bug in prior version

### Detailed Baselines (micro-F1)

| Dataset | Greedy | MV | Oracle | Headroom |
|---------|--------|----|--------|----------|
| FewNERD | 0.7912 | 0.7849 | 0.8869 | 9.57 pp |
| CoNLL   | 0.9119 | 0.9136 | 0.9532 | 4.13 pp |
| SciERC  | 0.6659 | 0.6695 | 0.8064 | 14.05 pp |

### Derivation

```
α_crit = π_MV / (2 − π_MV)
```

- When α > α_crit: SC aggregation should improve over individual samples
- When α < α_crit: SC aggregation hurts (information loss exceeds agreement gain)

### Key Finding: α_crit Bound Correctly Predicts MV Direction

With micro-F1 evaluation, the α_crit bound correctly predicts the direction of entity-level MV for all three datasets:

1. **FewNERD** (α_obs < α_crit by 0.005): Bound predicts MV should not help → confirmed, MV loses 0.63pp. The margin is razor-thin, consistent with MV's near-parity with greedy.

2. **CoNLL** (α_obs > α_crit by 0.031): Bound predicts MV should help → confirmed, MV gains 0.17pp. However, degeneracy-adjusted bound α_crit_eff = 0.8409/(1−0.591) = 2.06 > 1.0 still predicts failure, yet MV marginally succeeds. The high degeneracy (59%) means most of MV's "success" comes from correctly copying degenerate instances.

3. **SciERC** (α_obs > α_crit by 0.106): Bound predicts MV should help → confirmed, MV gains 0.37pp. Largest gap between α_obs and α_crit, consistent with largest MV improvement.

**Implication**: Entity-level MV is not universally broken for structured NER—it is roughly at parity with greedy (±0.6pp). The prior finding of large MV degradation (−1.4 to −9.2pp) was an artifact of macro-F1 evaluation, which over-weights instances with few entities where MV tends to produce empty outputs. The real limitation is that MV provides negligible improvement despite substantial oracle headroom (4–14pp), motivating sample-level selection which preserves span consistency.

### Old vs New Comparison (macro-F1 bug impact)

| Dataset | Metric | Old (macro-F1) | New (micro-F1) | Δ |
|---------|--------|---------------|----------------|---|
| FewNERD | Greedy | 0.7482 | 0.7912 | +4.3pp |
| FewNERD | MV | 0.6561 | 0.7849 | +12.9pp |
| FewNERD | Δ_SC | −9.21pp | −0.63pp | +8.6pp |
| CoNLL | Greedy | 0.9075 | 0.9119 | +0.4pp |
| CoNLL | MV | 0.8938 | 0.9136 | +2.0pp |
| CoNLL | Δ_SC | −1.37pp | +0.17pp | **sign flip** |
| SciERC | Greedy | 0.6441 | 0.6659 | +2.2pp |
| SciERC | MV | 0.6138 | 0.6695 | +5.6pp |
| SciERC | Δ_SC | −3.03pp | +0.37pp | **sign flip** |

### Data Sources

- FewNERD: 3 seeds (42, 123, 456), n=32,565 instances (gold-non-empty), Qwen3-8B-FT N=8 T=1.0
  - seed 42: `exp_021_inference/samples.jsonl` → greedy=0.7910, mv=0.7841, oracle=0.8854, degen=10.0%
  - seed 123: `exp_021_fewnerd_n8_seed123/samples.jsonl` → greedy=0.7912, mv=0.7848, oracle=0.8897, degen=9.3%
  - seed 456: `exp_021_fewnerd_n8_seed456/samples.jsonl` → greedy=0.7914, mv=0.7857, oracle=0.8855, degen=8.2%
- CoNLL: 3 seeds (42, 123, 456), n=2,756 instances (gold-non-empty), N=8 T=1.0
  - seed 42: `exp002_conll2003/samples.jsonl` → greedy=0.9123, mv=0.9129, oracle=0.9543, degen=56.7%
  - seed 123: `exp_002_conll_n8_seed123/samples.jsonl` → greedy=0.9119, mv=0.9157, oracle=0.9543, degen=60.4%
  - seed 456: `exp_002_conll_n8_seed456/samples.jsonl` → greedy=0.9115, mv=0.9121, oracle=0.9509, degen=60.3%
- SciERC: 3 seeds (42, 123, 456), n=529 instances (gold-non-empty), N=8 T=1.0
  - seed 42: `exp_012_rerun_1024/samples.jsonl` → greedy=0.6663, mv=0.6719, oracle=0.7808, degen=11.2%
  - seed 123: `exp_001_seed123_v2/samples.jsonl` → greedy=0.6651, mv=0.6660, oracle=0.8179, degen=7.2%
  - seed 456: `exp_001_seed456_v2/samples.jsonl` → greedy=0.6663, mv=0.6707, oracle=0.8206, degen=6.2%
- Recomputed 2026-05-21 via `recompute_alpha_crit.py` with micro-F1 (aggregate TP/FP/FN)
- Entity match: exact (text, type, start, end) tuple match
- MV threshold: entity included if it appears in ≥ N/2 = 4 of 8 samples
