# analysis exp013 cross transfer prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp013_cross_transfer_prep_20260513T064047_result.json`
- **Structured JSON:** [`b134502f4ea1c7c080e1.json`](../../sessions/b1/b134502f4ea1c7c080e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，dry-run 通过。

**注意**：任务描述中的数据路径有误。实际 features.csv 位置：
- Qwen-rewrite: `data/features.csv`
- Pythia: `data_exp001_pythia/features.csv`
- OLMo: `data_exp002_olmo/features.csv`
- Qwen-cont: `data_exp017_qwen_cont/features.csv`

脚本已使用正确路径作为默认值。

**脚本功能**：
- 4×4 transfer matrix，对角线用 5-fold GroupKFold CV，非对角线用全量 train→test
- OBD-LightGBM 参数与 exp-010 一致（200 trees, depth=6, lr=0.05）
- 4 个指标：accuracy, MAE, Kendall τ_b, mean pairwise AUC
- 输出 JSON + CSV + 格式化打印 + transfer retention 比率
- 支持 `--data_dirs` / `--labels` / `--out_dir` / `--seed` 参数

---
