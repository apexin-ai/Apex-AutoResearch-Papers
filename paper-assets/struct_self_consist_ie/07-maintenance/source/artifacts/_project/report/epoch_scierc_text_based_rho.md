# tab:epoch_scierc -- Text-Based rho(LP, F1) Recomputation

## Method

Within-instance Spearman rho(LP, F1) computed with **text-based entity matching**: entity set = `{(text, type)}`.

This is consistent with tab:within_rho (appendix L648), which also uses text-based matching.
evaluation.py's span-based `(start, end, type)` matching is preserved for D146 conditional decomp F1 and is NOT used here.

Script: `code/compute_epoch_scierc_rho_textbased.py`

## Results (text-based)

| Epoch | median rho | mean rho | % positive | n_valid | n_total | LP delta (pp) |
|-------|-----------|---------|-----------|---------|---------|--------------|
| 3-epoch | **0.3192** | 0.2726 | 76.4% | 495 | 551 | -1.24 |
| 5-epoch | **0.2624** | 0.1791 | 64.1% | 435 | 551 | +0.64 |
| 10-epoch | **0.1116** | 0.0660 | 54.0% | 276 | 551 | +1.02 |

## Comparison: text-based vs span-based

| Epoch | Text-based median rho | Span-based median rho | Delta |
|-------|----------------------|----------------------|-------|
| 3-epoch | 0.3192 | 0.3172 | +0.0020 |
| 5-epoch | 0.2624 | 0.2474 | +0.0150 |
| 10-epoch | 0.1116 | 0.1201 | -0.0085 |

Differences are small (< 0.02). The monotonic trend (3-epoch > 5-epoch > 10-epoch) holds under both matching methods.

## Cross-table consistency check

- tab:within_rho (L648) reports 5-epoch SciERC rho = 0.262 (text-based)
- This recomputation: 5-epoch median rho = 0.2624, rounds to 0.262

**Confirmed consistent.**

## Data paths

- 3-epoch: `output/exp_029a_scierc_3epoch/samples.jsonl`
- 5-epoch: `output/exp_012_rerun_1024/samples.jsonl`
- 10-epoch: `output/exp_029b_scierc_10epoch/samples.jsonl`
- JSON output: `output/epoch_scierc_textbased_rho.json`
