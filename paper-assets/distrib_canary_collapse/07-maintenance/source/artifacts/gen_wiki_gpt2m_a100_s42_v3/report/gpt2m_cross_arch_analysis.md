# GPT-2-medium Cross-Architecture Validation (gen_wiki_gpt2m_a100_s42_v3)

## Setup
- Model: gpt2-medium (355M params) | Baseline: Pythia-410m
- Data: wikitext103_5k, α=1.0, seed=42, 10 generations, 5000 steps/gen
- Training time: 10.12h on A100

## Drift Analysis (gen0 → gen10)

| Metric | Gen 0 | Gen 10 | GPT-2m Drift | Pythia-410m Drift | Direction Match |
|--------|-------|--------|-------------|-------------------|-----------------|
| token_entropy | 3.5714 | 0.4822 | **-86.5%** | -60.5% | ✓ (stronger) |
| ece | 0.0112 | 0.5185 | **+4544%** | +3762% | ✓ (stronger) |
| perplexity | 32.63 | 14616.6 | **+44693%** | +3624% | ✓ (12x more) |
| distinct_1 | 0.1044 | 0.0914 | **-12.4%** | -28.3% | ✓ (weaker) |
| distinct_2 | 0.5483 | 0.4675 | **-14.7%** | -35.2% | ✓ (weaker) |
| distinct_3 | 0.8441 | 0.7368 | **-12.7%** | -31.6% | ✓ (weaker) |
| effective_rank | 2.372 | 26.737 | +1027% | N/A | — |
| mauve | 0.0315 | 0.0316 | +0.4% | N/A | — |

## Cross-Correlation Analysis
- **14/16 canary→downstream pairs peak at lag=0** (contemporaneous, no lead-lag)
- 2 pairs (entropy→ppl, self_bleu→ppl) peak at lag=-1, marginal difference from lag=0
- Raw Pearson |r| range: 0.62–0.97, all p<0.05
- **Same lag-0 dominance pattern as Pythia** — naive cross-correlation inflates spurious causality

## Permutation Granger Causality (first-differenced, 5000 permutations)

### Significant (p<0.05)
- token_entropy → distinct_1: F=1271.3, p=0.002
- token_entropy → distinct_2: F=299.4, p=0.002
- token_entropy → distinct_3: F=141.5, p=0.003
- ece → distinct_1: F=436.6, p=0.001
- ece → distinct_2: F=142.2, p=0.002
- ece → distinct_3: F=90.5, p=0.003

### Non-significant
- All canary → perplexity (entropy marginal p=0.059)
- All effective_rank → downstream (p>0.08)
- All self_bleu → downstream (p>0.88, zero predictive signal)

## Key Findings
1. **Collapse direction universally matches**: All 6 core metrics degrade in the same direction as Pythia-410m
2. **Calibration/perplexity collapse more severe**: GPT-2m entropy drops 86.5% (vs 60.5%), ppl explodes 447x (vs 36x)
3. **Diversity loss milder**: GPT-2m distinct_n drops 12-15% (vs 28-35% Pythia) — larger model retains more lexical variety even under collapse
4. **Cross-correlation lag-0 dominance confirmed**: same methodological pitfall as Pythia
5. **Granger selectivity**: entropy/ece genuinely lead diversity loss; but Granger→ppl fails (co-trending without temporal lead); self_bleu saturates early and has zero Granger signal

## Conclusion: SUCCESS
Method sensitivity patterns generalize from Pythia-410m to GPT-2-medium. The core methodological pitfalls (inflated cross-correlation from non-stationary co-trending, Granger selectivity depending on metric pair choice) are architecture-independent.
