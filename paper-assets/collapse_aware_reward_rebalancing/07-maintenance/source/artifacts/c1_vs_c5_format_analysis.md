# C1 vs C5 Format Diversity Analysis

**C1**: LoRA K=4, ArmoRM top-1 curated (`carr_quick_probe_03`)
**C5**: LoRA K=4, no curation baseline (`carr_baseline_no_curation_01`)

## Status

- C5 metrics: **COMPLETE**
- C1 metrics: **IN PROGRESS** (re-running on bjb2-23165 GPU 0, ETA ~18:00 CST May 17)
  - C1 data was overwritten by C5 baseline run (shared output dir). Re-generating to `outputs_lora_k4_curated/`.
  - Watcher script will auto-compute and save to `analysis/c1_c5_format_diversity.json` on completion.

## Results

| Metric | C1 Gen0 | C1 Gen2 | C5 Gen0 | C5 Gen2 | C1 delta | C5 delta |
|--------|---------|---------|---------|---------|----------|----------|
| opening_unique_ratio | — | — | 0.7532 | 0.4789 | — | -0.2743 |
| opening_entropy (bits) | — | — | 12.4257 | 11.6803 | — | -0.7454 |
| near_duplicate_start_rate | — | — | 0.3827 | 0.7489 | — | +0.3662 |
| per_response_ttr | — | — | 0.6828 | 0.6598 | — | -0.0230 |
| trigram_repetition_rate | — | — | 0.1739 | 0.2576 | — | +0.0837 |

## Metric Definitions

1. **opening_unique_ratio**: fraction of responses with unique 50-char prefix (higher = more diverse)
2. **opening_entropy**: Shannon entropy of first-10-token sequence distribution (bits; higher = more diverse)
3. **near_duplicate_start_rate**: fraction of responses whose 50-char prefix is shared with at least one other response (lower = more diverse)
4. **per_response_ttr**: mean type-token ratio per individual response (higher = richer vocabulary)
5. **trigram_repetition_rate**: fraction of distinct trigrams appearing >=2 times across corpus (lower = more diverse)

## C5 Observations

C5 (baseline, no curation) shows significant format collapse over 3 generations:
- Opening diversity drops 36% (0.753 → 0.479 unique ratio)
- Near-duplicate starts nearly double (38% → 75%)
- Trigram repetition increases +8.4pp
- Per-response vocabulary degrades mildly (-0.023 TTR)

This confirms baseline SFT self-improvement without curation already causes format collapse. The key question is whether C1 (reward curation) makes it worse or better.

## Data Paths (server bjb2-23165)

- C5: `/root/autodl-tmp/carr/outputs/gen_{0,2}/condition_0/generations.json`
- C1 (regenerating): `/root/autodl-tmp/carr/outputs_lora_k4_curated/gen_{0,2}/condition_0/generations.json`
- Combined metrics JSON: `/root/autodl-tmp/carr/analysis/c1_c5_format_diversity.json`
