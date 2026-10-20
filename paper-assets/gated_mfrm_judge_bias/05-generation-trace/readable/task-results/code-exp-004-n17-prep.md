# code exp 004 n17 prep

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-004-n17-prep_20260524T130122_result.json`
- **Structured JSON:** [`cdcf6e07d1b46f9cf0b2.json`](../../sessions/cd/cdcf6e07d1b46f9cf0b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出总结

### 1. 代码文件

| 文件 | 状态 |
|------|------|
| `exp004/baselines.py` | **复用** — 5 个 baseline 函数已 N-agnostic，无需修改 |
| `exp004/run_baselines_n17.py` | **新建** — N=17 runner，含 ARENA_ELO (18模型), ARENA_NAME_MAPPING, EXCLUDE_MODELS |
| `exp004/results_n17/results.json` | **新建** — 当前 7/9 judge 数据的结果 |

### 2. 5 个 Baseline 算法描述

1. **raw_average** — 每个模型的所有 judge 评分直接取平均 win rate，logit 变换后中心化。无任何 correction。
2. **cyclic_judge** — 先估计 judge severity `d_j = mean(y_j) - grand_mean`，从每条 observation 中减去 judge effect，再计算模型 win rate。等价于 CyclicJudge 的方差分解。
3. **cyclic_judge_discard** — 在 cyclic_judge 基础上，先丢弃 `e_i > 0.5` 的 high-exposure items，用剩余 items 做 judge severity correction。
4. **dcr_factor** — 每条 observation 按 `weight = 1 - e_i` 加权，contamination 高的 item 权重低。不处理 judge bias。
5. **preference_leakage** — 计算 per-(judge, model) bias `B_{j,m} = mean(y_{j,m}) - mean(y_{*,m})`，从每条 observation 减去对应 bias，再重新估计模型 ability。

### 3. 数据依赖分析

- **judgment_data_n17 可直接用**: exp003/judgment_data_n17 的 JSONL 格式与 data_loader 完全兼容
- **exposure_scores.csv 可直接复用**: exp002 的 exposure scores 覆盖了所有 224 个有效 items（317 in CSV → 224 matched）
- **无需额外预处理**: 不需要 prepare_n17_data.py，因为 judgment_data_n17 目录已经准备好
- **exp-020 兼容性**: exp-020 产出的 JSONL 格式（见 judgment_data_n17 样本）与 data_loader 兼容，新 judge 数据只需放入对应子目录

### 4. Dry-run 结果 (N=17, 7/9 judges)

| Baseline | Kendall-τ | Spearman-ρ | N_matched |
|----------|----------|-----------|-----------|
| raw_average | 0.8088 | 0.9240 | 17 |
| cyclic_judge | 0.8088 | 0.9240 | 17 |
| cyclic_judge_discard | 0.8088 | 0.9240 | 17 |
| dcr_factor | 0.8088 | 0.9240 | 17 |
| preference_leakage | 0.8088 | 0.9240 | 17 |

所有 baseline 产生完全相同的模型排名（τ 一致），与 N=8 结论一致。

### 5. N=17 就绪状态

exp-020 完成后还需要：

1. **等待 2 个 judge 完成数据采集**: `claude-opus-4.7-proxy` 和 `gpt-5.5-proxy`（当前 7/9）
2. **重新运行 prepare_n17_data.py** 更新 judgment_data_n17 的 symlinks（如果新数据放在不同位置）
3. **重新运行 baseline**: `python exp004/run_baselines_n17.py --judgment-dir exp003/judgment_data_n17 --exposure-csv exp002/results/exposure_scores.csv --output-dir exp004/results_n17`
4. **等待 exp-003 N=17 MCMC 完成** 后加 `--exp003-dir` 对比 G-MFRM joint τ

---
