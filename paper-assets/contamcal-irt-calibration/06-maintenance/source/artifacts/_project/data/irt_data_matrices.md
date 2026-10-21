IRT 2PL+γ input data (seed=42, 5 families)

| Benchmark | Respondents | Items | Overall Acc |
|-----------|------------|-------|-------------|
| MMLU | 20 | 14,042 | 0.5279 |
| GSM8K | 16 | 1,319 | 0.4390 |
| ARC-Challenge | 21 | 1,172 | 0.6985 |
| HumanEval | 15 | 164 | 0.1163 |

Note: 21 respondents total (not 25) — some families have 4 dosages not 5.
MMLU missing Qwen-7B d000 (no mmlu eval data for that checkpoint).

Files per benchmark: response_matrix.csv, exposure_scores.csv, item_metadata.csv
Script: /root/contamcal-irt-calibration/analysis/irt_data/irt_data_prep.py