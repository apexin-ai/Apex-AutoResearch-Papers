# code exp004 analysis prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004_analysis_prep_20260515T123648_result.json`
- **Structured JSON:** [`26f625a9c35929746a90.json`](../../sessions/26/26f625a9c35929746a90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到服务器，`--help` 验证通过。

**`scripts/exp004_analyze.py`** 功能：
- **Pairwise AUC**: 0v1~4v5，LightGBM OBD 5-fold CV（参数与现有 pipeline 一致），每对 bootstrap 1000 次算 95% CI
- **K\*(θ=0.60)**: CI lower bound ≥ θ 的最大连续 depth pair index + 1
- **K\*(θ) sweep**: θ = 0.55, 0.60, 0.65, 0.70
- **Ordinal**: 6-class MAE + accuracy，Top-5 feature importance
- **Baseline 对比**: 并排输出 7B vs 4 个 ≤1.5B baseline 的 pairwise AUC
- **Paired difference test**: 7B vs Qwen-1.5B(cont) 和 Qwen-1.5B(rewrite) 在 1v2 上的 bootstrap 差异显著性检验
- **输出**: `artifacts/exp004_7b_analysis.json` + 终端 summary table

exp-004 完成后直接运行 `python scripts/exp004_analyze.py` 即可。

---
