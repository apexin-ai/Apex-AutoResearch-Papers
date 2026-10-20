# Item Alignment Check: PSN-IRT vs v1 Leaderboard

## Conclusion

**Direct positional alignment does NOT work.** PSN-IRT and v1 leaderboard use different item orderings. Content-based matching achieves ~88% agreement for Mistral (best case), but the remaining ~12% discrepancy comes from both mapping ambiguity and genuine evaluation differences. PSN-IRT ran independent evaluations — it did not reuse v1 leaderboard data.

## Findings

### 1. Item Ordering

| Source | MMLU Ordering | Within-Subject |
|--------|--------------|----------------|
| PSN-IRT (combine.csv) | Raw MMLU canonical (cais/mmlu test, alphabetical by subject) | Dataset order |
| v1 Leaderboard | Alphabetical by subject | **Shuffled** |
| Raw MMLU (cais/mmlu) | Alphabetical by subject | Dataset order |

PSN-IRT follows the raw MMLU dataset's canonical ordering. v1 leaderboard shares the same subject grouping but shuffles items within each subject.

### 2. Match Rates

| Metric | Mistral-7B-Instruct-v0.1 | Vicuna-7B-v1.3 |
|--------|--------------------------|-----------------|
| PSN-IRT row | 6 | 10 |
| PSN-IRT MMLU accuracy | 0.5333 | 0.3913 |
| v1 MMLU accuracy | 0.5372 | 0.4719 |
| Accuracy gap | 0.004 (56 items) | 0.081 (1131 items) |
| Direct positional match | 54.56% (≈random) | — |
| After content reorder | **88.46%** | **72.48%** |
| Items mapped (of 14042) | 12068 | 12068 |

### 3. Mismatch Decomposition (Mistral)

- **1974 items (14%)**: Lost to deduplication (duplicate questions in raw MMLU prevent unambiguous mapping)
- **~56 items (0.4%)**: Genuine accuracy difference (v1 gets 56 more correct)
- **~1337 items (11.2%)**: Residual mismatch on mapped items, likely from different evaluation setups (prompt template, few-shot examples, random seed)

### 4. Vicuna Divergence

Vicuna shows 8% accuracy gap and only 72.5% match rate → PSN-IRT's Vicuna evaluation used a fundamentally different protocol than v1 leaderboard (possibly different prompt, different number of few-shot examples, or no normalization).

### 5. Content-Based Mapping

- 14042/14042 v1 items matched to raw MMLU (100% coverage)
- After deduplication: 12068 unique mappings (86% coverage)
- Mapping methods: 89% via first-50-char match, 11% via query-substring match
- Mapping file: `item_mapping.csv` (v1_position → raw_mmlu_position → psn_irt_mmlu_position)

## Recommendation

**Do NOT mix v1 leaderboard responses with PSN-IRT item parameters.** The ~12% response disagreement (even for the best-aligned model) would introduce substantial noise into IRT-based person-fit statistics.

Instead:
1. **Use PSN-IRT's own combine.csv** with PSN-IRT's own item parameters — they are internally consistent
2. **For v1 leaderboard models not in PSN-IRT**, either:
   - Re-estimate item parameters from v1 data using a separate IRT fitting
   - Use the content-based mapping with the caveat of ~12% noise
3. The item_mapping.csv can serve as a lookup table for future content-based alignment needs

## Files

| File | Description |
|------|-------------|
| `alignment_results.json` | Full quantitative results with per-subject breakdown |
| `item_mapping.csv` | v1 → raw MMLU → PSN-IRT position mapping (12477 mapped) |
| `alignment_report.md` | This report |
