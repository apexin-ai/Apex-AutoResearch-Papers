# code baseline battery 009

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_battery_009_20260514T230042_result.json`
- **Structured JSON:** [`513d7b0a431b3dd5cfbc.json`](../../sessions/51/513d7b0a431b3dd5cfbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All baselines verified. Here's the summary:

**`src/baselines.py` (966 lines) — deployed and validated on server**

| # | Method | Type | 4-class Acc | Notes |
|---|--------|------|-------------|-------|
| 1 | PPL Regression (single) | Feature | 25.1% | mean_ppl only, lower bound |
| 2 | PPL Regression (multi) | Feature | 62.2% | 19-dim OLS |
| 3 | CE-MLP | Feature | 74.9% | DCOL ablation (5 epochs) |
| 4 | CORAL | Feature | 53.7% | Ordinal regression (5 epochs, needs more) |
| 5 | DivEye (XGBoost) | Feature | **78.2%** | 14 diversity features |
| 6 | Random Forest | Feature | **78.1%** | 19-dim, matches main method |
| 7 | Logistic Regression | Feature | 75.0% | 19-dim |
| 8 | Zero-shot LLM | Text | — | Code ready, needs API key |

Key features:
- Unified CLI: `python src/baselines.py --method &lt;name> --features_path data/features_all.jsonl`
- `--data_path` alias works
- `--method all` runs all feature-based baselines
- `--method zeroshot --data_dirs data/ --provider claude` for LLM baseline
- Consistent output: 4-class acc, 3-class acc, MAE, pairwise AUC, confusion matrix, per-class recall with 95% CI

---
