# Pythia-410M s42 α=1.0 — D111 Direction-Checked Data (All Pairs)

Source files (westd-19828):
- Primary: `/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/analysis/5method_leadlag.json` (8 pairs: distinct_1/2/3 + mauve, has `significant_fdr`)
- Supplementary: `/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/analysis/5method_leadlag_old_ppl.json` (8 pairs: distinct_1/2/3 + perplexity, has `significant_fdr`)
- Cross-ref: `/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/analysis/pythia410m_8pair_5method_analysis.json` (8 pairs, older format, no FDR for diff_xcorr but TY uses lower d_max)

Union: 10 unique pairs (2 canaries × 5 downstreams).

## D111 Rules Applied
- naive_fwd = `significant`=True AND `peak_lag` > 0 (strictly)
- diff_fwd = `significant_fdr`=True AND `peak_lag` > 0 (strictly)

## All-Pair Table

| # | pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | permG_fdr | TY_sig | TY_d_max | TY_df_resid |
|---|------|-----------|-----------|-----------|----------|--------------|----------|-----------|--------|----------|-------------|
| 1 | token_entropy→distinct_1 | -1 | T | **F** | -1 | T | **F** | T | F | 2 | 1 |
| 2 | token_entropy→distinct_2 | -1 | T | **F** | -2 | T | **F** | T | F | 2 | 1 |
| 3 | token_entropy→distinct_3 | -1 | T | **F** | -2 | T | **F** | T | F | 2 | 1 |
| 4 | token_entropy→perplexity | -5 | T | **F** | 5 | T | **T** | F | F | 2 | 1 |
| 5 | token_entropy→mauve | -3 | T | **F** | 5 | F | **F** | F | F | 2 | 1 |
| 6 | ece→distinct_1 | -2 | T | **F** | -1 | T | **F** | T | F | 2 | 1 |
| 7 | ece→distinct_2 | -1 | T | **F** | -1 | T | **F** | T | T | 2 | 1 |
| 8 | ece→distinct_3 | -1 | T | **F** | -1 | T | **F** | T | F | 2 | 1 |
| 9 | ece→perplexity | 4 | T | **T** | 1 | T | **T** | F | T | 2 | 1 |
| 10 | ece→mauve | 3 | T | **T** | 4 | F | **F** | F | F | 2 | 1 |

## Supplementary: 8pair file TY (lower d_max, higher df_resid)

| # | pair | TY_sig_8pair | TY_d_max_8pair | TY_df_resid_8pair |
|---|------|-------------|----------------|-------------------|
| 1 | token_entropy→distinct_1 | T | 0 | 7 |
| 2 | token_entropy→distinct_2 | T | 0 | 7 |
| 3 | token_entropy→distinct_3 | T | 0 | 7 |
| 4 | token_entropy→perplexity | F | 1 | 4 |
| 6 | ece→distinct_1 | T | 1 | 4 |
| 7 | ece→distinct_2 | F | 1 | 4 |
| 8 | ece→distinct_3 | F | 1 | 4 |
| 9 | ece→perplexity | F | 1 | 4 |

(Pairs 5, 10 not in 8pair file — mauve not included there)

## Summary
- Total pairs: 10
- naive_fwd (sig AND lag>0): **2/10** (ece→perplexity, ece→mauve)
- diff_fwd (sig_fdr AND lag>0): **2/10** (token_entropy→perplexity, ece→perplexity)
- permG_fdr significant: 6/10 (all distinct pairs)
- TY significant (leadlag d_max=2): 2/10 (ece→distinct_2, ece→perplexity)
- TY significant (8pair lower d_max): 4/8 (token_entropy→distinct_1/2/3, ece→distinct_1)

## Note on lag convention
All distinct pairs show peak_lag < 0 for both naive and diff xcorr, meaning the peak correlation occurs when the canary series is shifted to earlier time points relative to downstream — i.e., **canary changes precede downstream changes**. Under the strict D111 rule (lag > 0 = forward), these are classified as non-forward. However, the negative lag actually indicates the expected causal direction (canary leads downstream). The perplexity pairs show the opposite pattern (positive lags), which may reflect perplexity's different temporal dynamics compared to diversity metrics.
