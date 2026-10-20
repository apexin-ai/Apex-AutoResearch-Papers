# Pythia-410M Generalization Experiment Analysis

**Experiment**: pythia410m_wiki_a100_s42
**Model**: EleutherAI/pythia-410m | **Dataset**: wikitext-103-v1 | **Alpha**: 1.0 | **Seed**: 42
**Generations**: 10 (gen_0 to gen_10) | **Status**: complete
**Analysis timestamp**: 2026-05-17T19:28:28

---

## Drift Summary (gen_0 → gen_9)

| Metric         | gen_0     | gen_9      | Drift %     |
|----------------|-----------|------------|-------------|
| distinct_1     | 0.0982    | 0.0720     | **-26.69%** |
| distinct_2     | 0.5178    | 0.3497     | **-32.46%** |
| distinct_3     | 0.8127    | 0.5835     | **-28.20%** |
| token_entropy  | 3.2342    | 1.2390     | **-61.69%** |
| ece            | 0.0108    | 0.4169     | **+3758.85%** |
| perplexity     | 26.9490   | 934.9594   | **+3369.37%** |

Severe model collapse: entropy drops 62%, diversity drops 27-32%, ECE and perplexity explode 34-38x.

---

## 5-Method Causal Analysis (5000 permutations)

### Per-Pair Vote Summary

| Pair                          | NaiveP | DiffXC | ThreshO | TodaY | PermG | Consensus |
|-------------------------------|--------|--------|---------|-------|-------|-----------|
| token_entropy→perplexity      | sig    | sig    | sig     | —     | —     | 3/5       |
| token_entropy→distinct_1      | sig    | sig    | sig     | sig   | sig   | **5/5**   |
| token_entropy→distinct_2      | sig    | sig    | sig     | sig   | sig   | **5/5**   |
| token_entropy→distinct_3      | sig    | sig    | sig     | sig   | sig   | **5/5**   |
| self_bleu→perplexity          | sig    | sig    | sig     | sig   | sig   | **5/5**   |
| self_bleu→distinct_1          | sig    | sig    | —       | —     | —     | 2/5       |
| self_bleu→distinct_2          | sig    | sig    | —       | —     | —     | 2/5       |
| self_bleu→distinct_3          | sig    | sig    | sig     | —     | —     | 3/5       |
| ece→perplexity                | sig    | sig    | sig     | —     | —     | 3/5       |
| ece→distinct_1                | sig    | sig    | sig     | sig   | sig   | **5/5**   |
| ece→distinct_2                | sig    | sig    | sig     | sig   | sig   | **5/5**   |
| ece→distinct_3                | sig    | sig    | sig     | sig   | sig   | **5/5**   |
| effective_rank→perplexity     | —      | sig    | —       | —     | —     | 1/5       |
| effective_rank→distinct_1     | sig    | sig    | —       | —     | sig   | 3/5       |
| effective_rank→distinct_2     | sig    | sig    | —       | —     | sig   | 3/5       |
| effective_rank→distinct_3     | sig    | sig    | —       | —     | sig   | 3/5       |

### Per-Method Sig Counts

| Method              | Sig / Total | Rate   |
|---------------------|-------------|--------|
| naive_pearson       | 15/16       | 93.8%  |
| differenced_xcorr   | 16/16       | 100.0% |
| threshold_onset     | 11/16       | 68.8%  |
| toda_yamamoto       | 8/16        | 50.0%  |
| permutation_granger | 10/16       | 62.5%  |
| **Total**           | **58/80**   | **72.5%** |

### Consensus Distribution

| Threshold   | Pair Count |
|-------------|------------|
| Consensus ≥ 5 | 7/16    |
| Consensus ≥ 4 | 7/16    |
| Consensus ≥ 3 | 13/16   |
| Consensus < 3 | 3/16    |

### PermG Detail

- PermG sig: 10/16 pairs (62.5%)
- Strong canary→downstream signal for: token_entropy→distinct_*, self_bleu→perplexity, ece→distinct_*, effective_rank→distinct_*
- Weak/not sig: all canary→perplexity pairs except self_bleu, and all self_bleu→distinct_* pairs

---

## VERSION A Assessment

Adapted criteria (original assumes 8 pairs, actual has 16):
- **PermG fwd sig**: 10/16 (62.5%) — exceeds 50% threshold
- **Consensus ≥ 4**: 7/16 (43.8%)
- **Consensus ≥ 3**: 13/16 (81.3%)

The 7 strongest pairs (5/5 consensus) are: token_entropy→distinct_{1,2,3}, self_bleu→perplexity, ece→distinct_{1,2,3}. These show unambiguous causal signal from canary metrics to downstream quality degradation.

**Conclusion**: Pythia-410M on WikiText-103 confirms the canary collapse pattern observed in GPT-2 Medium experiments. The model shows severe collapse (entropy -62%, perplexity +34x) with strong multi-method causal evidence (72.5% overall sig rate, 7/16 pairs with unanimous 5/5 consensus).
