## GSM8K 16-Condition Summary Table (D080 bugfix applied)

Server paths:
- CSV: `/root/autodl-tmp/pacs/analysis_output/gsm8k_16conditions_fixed.csv`
- JSON: `/root/autodl-tmp/pacs/analysis_output/gsm8k_16conditions_fixed.json`
- Script: `/root/autodl-tmp/pacs/aggregate_gsm8k_fixed.py`

| Model | Strategy | Sparsity | II_low | II_high | Gradient | CI_low | CI_high | p_value | n_valid | Flag |
|-------|----------|----------|--------|---------|----------|--------|---------|---------|---------|------|
| DeepSeek | importance | s015 | 0.6893 | -0.0171 | 0.7064 | 0.1230 | 1.6524 | 0.0020 | 50 | |
| DeepSeek | importance | s020 | 2.1499 | -0.0303 | 2.1802 | 0.5124 | 5.1792 | 0.0000 | 50 | |
| DeepSeek | importance | s025 | 9.8379 | 0.0321 | 9.8058 | 3.0609 | 18.4279 | 0.0000 | 50 | extreme_outliers: 2 |
| DeepSeek | importance | s030 | 0.7310 | 0.1235 | 0.6075 | -24.7103 | 18.1595 | 0.4247 | 50 | extreme_outliers: 3 |
| DeepSeek | random | s015 | 0.0256 | 0.0659 | -0.0404 | -0.7492 | 0.6090 | 0.5348 | 50 | |
| DeepSeek | random | s020 | -2.5483 | 0.4676 | -3.0159 | -17.8820 | 6.9114 | 0.5969 | 50 | extreme_outliers: 2 |
| DeepSeek | random | s025 | 4.9854 | 2.3428 | 2.6426 | -27.2073 | 28.2993 | 0.3889 | 50 | extreme_outliers: 3 |
| DeepSeek | random | s030 | 20.5437 | 6.9055 | 13.6382 | -50.3336 | 83.6989 | 0.3267 | 50 | extreme_outliers: 4 |
| Qwen | importance | s015 | 0.0173 | -0.0133 | 0.0306 | -0.0290 | 0.0870 | 0.1528 | 50 | |
| Qwen | importance | s020 | 0.0953 | 0.0045 | 0.0907 | -0.2252 | 0.3295 | 0.2364 | 50 | |
| Qwen | importance | s025 | 1.1869 | 0.0421 | 1.1448 | 0.6296 | 1.6406 | 0.0000 | 50 | |
| Qwen | importance | s030 | 4.7403 | 0.1198 | 4.6205 | 2.8928 | 6.8474 | 0.0000 | 50 | |
| Qwen | random | s015 | 1.3759 | 2.9512 | -1.5753 | -4.6357 | 0.0822 | 0.9173 | 50 | |
| Qwen | random | s020 | 9.3337 | 4.4539 | 4.8799 | -3.8505 | 18.3533 | 0.2383 | 50 | extreme_outliers: 1 |
| Qwen | random | s025 | 16.5676 | 5.4653 | 11.1023 | -3.6626 | 32.4726 | 0.1169 | 50 | extreme_outliers: 2 |
| Qwen | random | s030 | 102.1617 | 9.2335 | 92.9283 | 3.7458 | 260.3278 | 0.0001 | 50 | data_quality_issue (QW truncation) |
