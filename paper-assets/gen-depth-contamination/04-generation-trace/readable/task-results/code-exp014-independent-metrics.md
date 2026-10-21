# code exp014 independent metrics

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp014_independent_metrics_20260525T065633_result.json`
- **Structured JSON:** [`ecdec45d8dfea755d416.json`](../../sessions/ec/ecdec45d8dfea755d416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。任务 `exp_014_independent_metrics` 在 tmux session 中运行，会自动等待 v2 产出 `cc_predictions.csv` 后再开始计算。

**已完成的工作：**

1. **`scripts/exp014_independent_metrics.py`**（372行）— 计算 6 个与 OBD 15D 特征完全独立的质量指标：
   - GPT-2 Large PPL（774M，非 Qwen scorer）
   - MTLD + HD-D（lexical_diversity 库）
   - 3-gram / 4-gram 重复率
   - Zipf 系数
   - MAUVE by depth bin（vs depth-0）
   - 支持断点续跑（检查已有列）
   - 每算完一个指标就增量保存

2. **`scripts/exp014_independent_analysis.py`**（500行）— 独立相关性分析：
   - Spearman ρ + Kendall τ + Bonferroni 校正（α=0.05/6=0.0083）
   - Bootstrap CI（1000 resamples）
   - 分层分析（depth bin 0/1/2/3+，含 mean/median/std/IQR）
   - Kruskal-Wallis + Mann-Whitney U + Cliff's delta
   - Length-controlled（按文本长度 quartile 分层做 correlation）
   - OBD 特征 sanity check（明确标注 "overlaps with OBD feature, reported as sanity check only"）
   - 可视化：violin plot (2x3 grid) + depth 分布直方图 + MAUVE bar chart

3. **提交方式** — 由于 v2 还在运行，使用独立 exp_id `exp_014_independent_metrics`，包含等待逻辑：循环检测 `cc_predictions.csv` 存在后再启动。输出保存到 `results/exp014_v2/independent_analysis_results.json`。

---
