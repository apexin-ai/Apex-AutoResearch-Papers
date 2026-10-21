# 评估代码状态报告

## 评估脚本

| 文件 | 状态 | 说明 |
|------|------|------|
| `evaluation/eval_pipeline.py` | 已存在 | 三轴评估：perplexity（sliding-window）、lm-eval-harness（hellaswag, mmlu）、生成多样性（Self-BLEU, Distinct-n） |
| `evaluation/compare_results.py` | 已存在 | 跨 seed 汇总 + MVP pass/fail 判定（adaptive >= 90% grid-best 改善量） |

两个文件均有完整 docstring 说明用途、输入输出。无需新建。

## Adaptive 方法实现状态

**已实现**。`training/pretrain_weighted.py` 支持 `--weighting_method adaptive`：
- L143-149: 调用 `find_optimal_b(q_scores, tau, n_min)` -> `compute_sample_weights` -> 加权 loss
- 同时记录 `alpha_eff`、`ess`、`b` 等 step-level 指标
- 依赖 `weighting/alpha_eff.py`（已存在，含 `compute_alpha_eff`, `compute_ess`, `compute_sample_weights`, `find_optimal_b`）

## 已有模型 Checkpoints

| 目录 | 状态 |
|------|------|
| `output/models/uniform_seed42` | 有 |
| `output/models/uniform_seed123` | 有 |
| `output/models/uniform_seed456` | 有 |
| `output/models/grid_b0_5_seed42` | 有 |
| `output/models/grid_b*_seed{123,456}` | 缺失 |
| `output/models/adaptive_seed*` | 缺失 |

## 数据

- `data/mixed_data.jsonl` — 963MB (~371K docs)
- `data/scored_data.jsonl` — 975MB (~371K docs, 含 q_score)

## 问题与依赖

- **无代码缺失或依赖问题**：eval_pipeline.py、compare_results.py、pretrain_weighted.py 均完整
- **训练缺口**：grid-b 只跑了 b=0.5/seed42 一组，其余 grid-b 组合和所有 adaptive 组合尚未训练。评估前需先完成这些训练
- `compare_results.py` 的 grid_b 值列表为 `[0.5, 1.0, 1.5, 2.0, 3.0, 5.0]`，seeds 为 `[42, 123, 456]`，共需 6x3=18 个 grid 训练 + 3 个 adaptive 训练
