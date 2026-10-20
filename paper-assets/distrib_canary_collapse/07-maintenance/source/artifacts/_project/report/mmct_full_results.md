# MMCT Full Results Across All Completed Experiments

Generated: 2026-05-19
Data source: unified_5method (2-sigma threshold, Table 7 params: n_perm=5000, xcorr_lag=5, granger_lag=1, alpha=0.05)
Null baseline: 3 seeds x 8 pairs = 24 null observations from alpha=0.00

## Summary: FPR and Detection Rate by Alpha (Aggregated)

| Mode | FPR (a=0.00) | a0.10 | a0.25 | a0.50 | a0.60 | a0.75 |
|------|-------------|-------|-------|-------|-------|-------|
| uniform_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |
| uniform_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |
| weighted_pair_forward | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |
| weighted_pair_bidirectional | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |
| weighted_global_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |
| weighted_global_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0417 |

## Alpha Sweep: Per-Run Results (sig_pairs / 8 total)

| Condition | alpha | Model | Seed | unif_fwd | wpair_fwd | wglobal_fwd | unif_bidir | wpair_bidir | wglobal_bidir | Notes |
|-----------|-------|-------|------|----------|-----------|-------------|------------|-------------|---------------|-------|
| a000_s42 | 0.00 | Pythia-410M | 42 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |
| a000_s43 | 0.00 | Pythia-410M | 43 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |
| a000_s44 | 0.00 | Pythia-410M | 44 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |
| a010_s42 | 0.10 | Pythia-410M | 42 | 0/8 | 1/8 | 0/8 | 0/8 | 1/8 | 0/8 | NEW; single seed only (s43/s44 not available) |
| a025_s43 | 0.25 | Pythia-410M | 43 | 0/8 | 3/8 | 0/8 | 0/8 | 3/8 | 0/8 | |
| a025_s44 | 0.25 | Pythia-410M | 44 | 0/8 | 4/8 | 0/8 | 0/8 | 4/8 | 0/8 | |
| a050_s42 | 0.50 | Pythia-410M | 42 | 0/8 | 5/8 | 0/8 | 0/8 | 5/8 | 0/8 | |
| a050_s43 | 0.50 | Pythia-410M | 43 | 0/8 | 5/8 | 0/8 | 0/8 | 5/8 | 0/8 | |
| a050_s44 | 0.50 | Pythia-410M | 44 | 0/8 | 4/8 | 0/8 | 0/8 | 4/8 | 0/8 | |
| a060_s42_bf16 | 0.60 | Pythia-410M | 42 | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | bf16 precision; single seed |
| a075_s42 | 0.75 | Pythia-410M | 42 | 1/8 | 7/8 | 1/8 | 1/8 | 7/8 | 1/8 | |
| a075_s43 | 0.75 | Pythia-410M | 43 | 1/8 | 6/8 | 1/8 | 1/8 | 6/8 | 0/8 | |
| a075_s44 | 0.75 | Pythia-410M | 44 | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | |

## Table 7: Generalization Results (alpha=1.00, sig_pairs / 8 total)

| Condition | alpha | Model | Data | unif_fwd | wpair_fwd | wglobal_fwd | unif_bidir | wpair_bidir | wglobal_bidir | Notes |
|-----------|-------|-------|------|----------|-----------|-------------|------------|-------------|---------------|-------|
| Baseline | 1.00 | Pythia-410M | Wiki | 1/8 | 6/8 | 2/8 | 1/8 | 5/8 | 2/8 | |
| Arch: GPT-2m | 1.00 | GPT-2m | Wiki | 2/8 | 8/8 | 2/8 | 2/8 | 7/8 | 2/8 | Best wpair detection |
| Arch: OPT | 1.00 | OPT-1.3B | Wiki | 0/8 | 6/8 | 0/8 | 0/8 | 5/8 | 0/8 | |
| Scale: 1.4B s42 | 1.00 | Pythia-1.4B | Wiki | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | |
| Scale: 1.4B s43 | 1.00 | Pythia-1.4B | Wiki | 2/8 | 6/8 | 2/8 | 2/8 | 5/8 | 1/8 | |
| Domain: C4 s42 | 1.00 | Pythia-1B | C4 | 1/8 | 7/8 | 1/8 | 1/8 | 6/8 | 1/8 | |
| Domain: C4 s43 | 1.00 | Pythia-1B | C4 | 2/8 | 6/8 | 2/8 | 2/8 | 6/8 | 1/8 | |

## Missing Experiments (Not Available for MMCT)

| Condition | Reason |
|-----------|--------|
| a010_s43 | Experiment directory does not exist |
| a010_s44 | Experiment directory does not exist |
| a025_s42 | Experiment directory does not exist |
| gen_wiki_gpt2m_a100_s42_v4 | Directory does not exist; GPT-2m alpha=1.00 s42 covered via generalize/gpt2m_wiki_a100_s42 |
| gen_wiki_gpt2m_a100_s43 | Incomplete: only 3/11 generations, no all_metrics.json |

## Key Observations

1. **FPR = 0 across all modes**: No false positives at alpha=0.00 (0/24 in every mode).

2. **weighted_pair is the most sensitive mode**: Detection rates monotonically increase with alpha (0.125 at a0.10, 0.4375 at a0.25, 0.5833 at a0.50, 0.75 at a0.60, 0.7917 at a0.75). FPR remains zero.

3. **uniform and weighted_global are conservative**: Only detect at alpha>=0.75, and even then only 1-2/24 pairs.

4. **Bidirectional adds minimal filtering**: weighted_pair_bidirectional matches weighted_pair_forward exactly in the alpha sweep (the directional asymmetry filter rarely changes the call).

5. **Table 7 generalization**: weighted_pair_forward detects 6-8/8 pairs across all 7 conditions at alpha=1.00, confirming generalization across architectures (GPT-2m, OPT-1.3B), scales (410M to 1.4B), and domains (Wiki, C4).

6. **Dose-response monotonicity** (weighted_pair_forward pooled rates):
   - a0.00: 0.000
   - a0.10: 0.125
   - a0.25: 0.438
   - a0.50: 0.583
   - a0.60: 0.750
   - a0.75: 0.792
   - a1.00 (Table 7 avg): 0.813

## Source Files

- Full MMCT results JSON: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json`
- Null distribution: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/null_distribution_v2.json`
- FPR/FNR comparison: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/fpr_fnr_comparison_v2.md`
- Table 7 detail: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_table7.md`
- Per-condition unified data: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/unified_data/*.json`
