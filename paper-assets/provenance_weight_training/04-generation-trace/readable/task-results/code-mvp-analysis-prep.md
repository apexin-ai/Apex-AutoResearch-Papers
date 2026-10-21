# code mvp analysis prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-analysis-prep_20260514T202648_result.json`
- **Structured JSON:** [`7ab4d651ff2e4e114036.json`](../../sessions/7a/7ab4d651ff2e4e114036.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。注意 adaptive_fix 的 PPL ~22 是从 trainer_state.json 的 eval_loss 算出的（训练中间 checkpoint 的 inline eval，不是最终 holdout eval），所以数值偏高是预期的——训练还没跑完（5500/6103 步），且这个 eval_loss 是在训练数据子集上算的，不等于 holdout PPL。

grid_b seed42 的 5 个已完成实验也缺 eval_results.json，需要跑 `eval_perplexity.py`。

脚本已部署到 `/root/provenance_weight_training/analyze_mvp.py`，功能：
1. 训练状态检测（adaptive_fix 3 个还在训练，grid_b5.0_seed42 也在跑）
2. 从 eval_results.json / trainer_state.json 自动提取 PPL，标注数据来源
3. 对比表含 uniform/grid-b/adaptive_fix/adaptive_orig，带 vs_uniform 和 vs_grid_best 百分比
4. MVP 自动判定（当前因 adaptive_fix 未完成+未跑 holdout eval，数据不完整）
5. b* 轨迹分析：三个 seed 的 b* 均值 ~0.7，中位数 ~0，趋势 increasing，说明后期 b* 在增大

---
