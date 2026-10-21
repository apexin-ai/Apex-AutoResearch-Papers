# research bootstrap jackknife check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bootstrap_jackknife_check_20260522T115334_result.json`
- **Structured JSON:** [`0d3d88b379353b629cc6.json`](../../sessions/0d/0d3d88b379353b629cc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are clear. Here's the summary:

---

## 1. 论文中 Bootstrap vs Jackknife 对比的位置

**两处**都有写入：

- **`docs/paper/appendix.tex:13`** — Appendix A 的完整段落：
  > **CI method comparison.** Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates ~127 unique items per 200-item resample) does not materially distort interval estimates. Stratified resampling by subject (10 subjects × 20 items) produces CIs within 4% of simple item-level bootstrap...

- **`docs/paper/sections/experiments.tex:142`** — §4.6 Robustness Checks 中的简述：
  > **CI method**: bootstrap and jackknife confidence intervals agree closely (width ratio 0.96–1.04 across components).

## 2. 数字与数据一致性

论文引用的 "width ratio 0.96–1.04" 与 worker 分析结果（`worker_analysis_bootstrap_vs_jackknife_20260521T040103_result.json`）完全一致：

| Component | Boot CI width | Jack CI width | Ratio |
|---|---|---|---|
| item_id | 10.02 | 10.33 | 0.97 |
| residual | 5.12 | 5.26 | 0.97 |
| seed:item_id | 2.40 | 2.37 | 1.01 |
| prompt_template:item_id | 2.33 | 2.23 | **1.04** |
| temperature:item_id | 0.94 | 0.98 | **0.96** |

范围确实是 [0.96, 1.04]，数字可追溯。

## 3. 数据 Artifact

- **服务器端**：worker result 显示结果保存到 `results/analysis/bootstrap_vs_jackknife.json`（服务器路径），SSH 当前无法访问验证。
- **本地 artifacts/**：无已注册的 bootstrap_vs_jackknife artifact（不在 `manifest.yaml` 中）。数据来源仅可追溯到 worker log 的 result JSON。

## 4. 是否需要额外工作

**不需要**。Bootstrap vs jackknife 对比已完整写入论文（appendix 详细版 + main text 摘要版），数字与分析结果一致。唯一的小问题是数据文件未注册到本地 artifact manifest，但 worker result JSON 提供了完整的可追溯性。

---
