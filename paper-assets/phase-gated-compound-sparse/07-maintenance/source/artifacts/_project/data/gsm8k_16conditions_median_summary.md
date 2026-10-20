## GSM8K 16-Condition Median-Based Summary (D080v2)

Server paths (westd-22162):
- CSV: `/root/autodl-tmp/pacs/analysis_output/gsm8k_16conditions_fixed.csv`
- JSON: `/root/autodl-tmp/pacs/analysis_output/gsm8k_16conditions_fixed.json`
- Script: `/root/autodl-tmp/pacs/aggregate_gsm8k_median.py`

### DS Importance (主证据, dose-response 严格单调)

| Sparsity | median_gradient | CI [2.5%, 97.5%] | wilcoxon_p |
|----------|----------------|-------------------|------------|
| s015 | +0.2409 | [0.0769, 0.4781] | 0.0003 |
| s020 | +0.7403 | [0.3139, 1.1186] | <0.0001 |
| s025 | +1.9915 | [0.9327, 2.8198] | <0.0001 |
| s030 | +4.6819 | [2.1211, 10.5566] | <0.0001 |

Note: DS imp s030 mean_gradient=0.607 (被负离群值拉低), median=4.68 — mean→median 修复的关键案例。

QW rand s030: flagged INVALID (valid_for_paper: false)
