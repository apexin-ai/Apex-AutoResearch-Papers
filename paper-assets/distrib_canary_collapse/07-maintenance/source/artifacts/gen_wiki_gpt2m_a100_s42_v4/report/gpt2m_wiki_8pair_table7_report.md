# GPT-2-medium WikiText-103 8-Pair Table 7 Analysis

**Experiment**: gen_wiki_gpt2m_a100_s42_v4
**Model**: gpt2-medium (355M)
**Dataset**: wikitext103_5k, alpha=1.0, seed=42
**Generations**: 11 (gen0-gen10), 5000 steps/gen
**Parameters**: n_perm=5000, xcorr_lag=5, granger_lag=1

## Table 7 Row

| Naive | Diff | Thresh | PG_fwd | PG_rev | TY | K>=4 |
|-------|------|--------|--------|--------|-----|------|
| 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 |

## Per-Pair Detail

| Pair | Naive | Diff(FDR) | Thresh | TY | PG_fwd | PG_rev | K |
|------|-------|-----------|--------|-----|--------|--------|---|
| ent->ppl | Y (p=0.0199) | Y (q=0.0016) | Y (L=7) | N (p=0.9998) | N (p=0.4989) | N (p=0.1820) | 3/5 |
| ent->d1 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | N (p=0.1160) | Y (p=0.0006) | N (p=0.0964) | 4/5 |
| ent->d2 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | Y (p=0.0017) | Y (p=0.0020) | N (p=0.1052) | 5/5 |
| ent->d3 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | Y (p=0.0000) | Y (p=0.0024) | N (p=0.1062) | 5/5 |
| ece->ppl | Y (p=0.0076) | Y (q=0.0029) | Y (L=6) | N (p=0.2254) | N (p=0.8796) | N (p=0.6107) | 3/5 |
| ece->d1 | Y (p=0.0000) | Y (q=0.0007) | Y (L=1) | Y (p=0.0000) | Y (p=0.0006) | Y (p=0.0032) | 5/5 |
| ece->d2 | Y (p=0.0000) | Y (q=0.0000) | Y (L=1) | Y (p=0.0000) | Y (p=0.0010) | Y (p=0.0160) | 5/5 |
| ece->d3 | Y (p=0.0000) | Y (q=0.0000) | Y (L=1) | Y (p=0.0000) | Y (p=0.0010) | Y (p=0.0084) | 5/5 |

## Drift Analysis (gen0 -> gen10)

| Metric | Gen0 | Gen10 | Change% |
|--------|------|-------|---------|
| token_entropy | 3.5714 | 0.4794 | -86.6% |
| ece | 0.0112 | 0.5216 | +4571.9% |
| perplexity | 32.63 | 16520.55 | +50527.6% |
| distinct_1 | 0.1044 | 0.0918 | -12.1% |
| distinct_2 | 0.5483 | 0.4717 | -14.0% |
| distinct_3 | 0.8441 | 0.7394 | -12.4% |
| self_bleu | 0.0094 | 0.0119 | +25.9% |
| effective_rank | 2.3722 | 25.0018 | +953.9% |
| mauve | 0.0315 | 0.0339 | +7.9% |

## Comparison with Other Conditions

| Row | Naive | Diff | Thresh | PG fwd | PG rev | TY | K>=4 |
|-----|-------|------|--------|--------|--------|-----|------|
| Baseline (Pythia-410M) | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 4/8 | 6/8 |
| **GPT-2m (355M)** | **8/8** | **8/8** | **8/8** | **6/8** | **3/8** | **5/8** | **6/8** |
| OPT-1.3B | 8/8 | 6/8 | 8/8 | 6/8 | 2/8 | 6/8 | 6/8 |
| Pythia-1.4B s42 | 7/8 | 6/8 | 8/8 | 5/8 | 0/8 | 0/8 | 5/8 |
| C4 s42 | 8/8 | 6/8 | 8/8 | 6/8 | 3/8 | 3/8 | 6/8 |

## Key Findings

1. **K>=4 = 6/8**: Strong consensus, matching Baseline and OPT-1.3B level. GPT-2m confirms canary-downstream causal signal generalizes across architectures.
2. **Naive/Diff/Thresh all 8/8**: Perfect detection on correlation-based and threshold methods, consistent with strong monotonic degradation trends.
3. **PG_fwd = 6/8, PG_rev = 3/8**: Correct asymmetry (forward > reverse), confirming directional causality from canary to downstream.
4. **TY = 5/8**: Higher than Baseline (4/8), driven by ece->d1/d2/d3 and ent->d2/d3 pairs. The two ppl pairs fail TY (p=0.9998 and 0.2254), consistent with perplexity's delayed onset (L=6-7) reducing TY power.
5. **Perplexity explosion**: +50527.6% drift (32.6 -> 16520.5), the most extreme among all conditions, indicating severe model collapse in GPT-2m.
6. **Token entropy collapse**: -86.6% (3.57 -> 0.48), more severe than typical Pythia experiments, suggesting GPT-2m is more susceptible to distributional narrowing.

## JSON Output
Full per-pair results saved to: `/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/analysis/gpt2m_8pair_table7.json`
