# LOFO θ Validation — Updated with Gemma-2-2B

## Source Files (cqa1-22115)
- Script: /root/autodl-tmp/gen-depth-contamination/scripts/lofo_theta_validation.py
- Results: results/lofo_theta_validation/lofo_theta_results.json
- LaTeX: results/lofo_theta_validation/lofo_theta_table.tex

## Per-family K* at θ=0.60

| Family | K* | 1v2 ci_lower | margin |
|--------|-----|-------------|--------|
| Qwen-rw | 2 | 0.6859 | +0.086 |
| Pythia | 2 | 0.6454 | +0.045 |
| OLMo | 2 | 0.6045 | +0.005 |
| Qwen-cont | 2 | 0.6015 | +0.002 |
| Qwen-7B | 2 | 0.6080 | +0.008 |
| **Gemma-2B** | **1** | **0.5882** | **-0.012** |

## LOFO θ̂ Range

| Left-out | θ_low | θ_high | Width | θ̂(mid) | θ=0.60? |
|----------|-------|--------|-------|---------|---------|
| Qwen-rw | 0.5511 | 0.5882 | 0.0371 | 0.5696 | NO |
| Pythia | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| OLMo | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| Qwen-cont | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| Qwen-7B | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| **Gemma-2B** | 0.5795 | 0.6015 | 0.0220 | 0.5905 | **YES** |
| All 6 | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
