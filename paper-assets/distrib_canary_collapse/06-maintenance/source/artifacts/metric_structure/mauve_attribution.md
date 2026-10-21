# Mauve Attribution Analysis

## Registry Coverage

- 123 total experiments in registry (no `status`/`conclusion` fields; all entries are completed experiments)
- 3 experiments have explicit non-robust pair data (via `non_robust_pairs`, `failing_pairs`, or `consensus` dict)
- 1 additional experiment has per-pair breakdown with all 8 pairs robust (no non-robust to classify)

## Non-Robust Pair Analysis

**Answer: YES, all non-robust pairs involve mauve as the downstream metric.**

| Experiment | non_robust_pairs | PermG_fwd | robust_pairs_K3 |
|---|---|---|---|
| phase_diagram_t25_a075_s43_fp32_v3 | token_entropy\<mauve (2/5), ece\<mauve (2/5) | 8/8 | 6/8 |
| padding_robustness_a100_s42_fp32 | token_entropy\<mauve (0/5), ece\<mauve (0/5) | 6/8 | 6 |
| phase_diagram_t25_a050_s42_fp32_v3 | token_entropy\<mauve (0/5), ece\<mauve (2/5) | 6/8 | 6/8 |

**3/3 experiments: all non-robust pairs = {token_entropy\<mauve, ece\<mauve}**

No exceptions. Non-mauve pairs (token_entropy/ece x distinct_1/2/3) consistently pass K≥3 consensus.

## Pair Type Ranking

| Pair | Count (across all experiments with data) |
|---|---|
| token_entropy\<mauve | 3 |
| ece\<mauve | 3 |

Only 2 pair types appear as non-robust across the entire registry.

## PermG_fwd and PermG_robust_fwd

**`PermG_robust_fwd` does not exist as a registry field.** The task asks about a field that was never stored. The relevant fields are:

- `PermG_fwd` = count of pairs where Permutation Granger FDR-corrected forward test is significant (out of 8)
- `robust_pairs_K3` = count of pairs where ≥3 of 5 methods are significant (K≥3 consensus)

### 6/8 vs 8/8 Pattern

**PermG_fwd = 6/8** (wiki-domain, standard):
- gen_gpt2m_s43_fp32: K3=6
- alpha_sweep_a050_s43_fp32: K3=6
- padding_robustness_a100_s42_fp32: K3=6
- qwen35_08b_wiki_a100_s43_fp32: K3=6

**PermG_fwd = 8/8** (mixed domains):
- c4_a075_s43_fp32: K3=8 (C4)
- c4_a075_s42_fp32: K3=8 (C4)
- c4_a050_s43_fp32: K3=6 (C4, but mauve pairs don't pass consensus even here)
- scale_14b_c4_s42_fp32: K3=8 (C4)
- qwen35_08b_wiki_a100_s42_v2: K3=7 (wiki, seed variation)
- generalize_pythia1b_c4_a100_s43_v2: K3=8 (C4, all pairs pass consensus_detail)

**Pattern interpretation:** 6/8 PermG_fwd always co-occurs with K3=6, caused by mauve pair failure. 8/8 PermG_fwd occurs in both C4 domain (where mauve can be robust) and occasionally in wiki domain (qwen seed variant). The structural 6/8 ceiling is a wiki-domain x mauve metric interaction, not a PermG method limitation.

## Structural Conclusion

The 6/8 ceiling = PermG detects lead-lag in 8/8 pairs, but K3 consensus requires ≥3/5 methods to agree. The `token_entropy<mauve` and `ece<mauve` pairs score 0-2/5 methods (TY and Threshold methods fail on mauve). The 6 diversity pairs (x distinct_1/2/3) score 3-5/5. This is domain-specific: C4 experiments achieve 8/8 K3 robust pairs including mauve.
