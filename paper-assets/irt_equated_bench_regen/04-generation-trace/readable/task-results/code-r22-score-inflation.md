# code r22 score inflation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r22_score_inflation_20260523T081520_result.json`
- **Structured JSON:** [`2c15700e381a59d23d27.json`](../../sessions/2c/2c15700e381a59d23d27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。关键发现总结：

**Score shift**: 移除 3918 个 DIF-C 项目后，所有模型分数上升（DIF-C 项目平均更难），但 cohort 间存在显著差异：
- 2023 cohort: +2.35 pp
- 2024 cohort: +2.06 pp
- **差异**: 2024 模型从 DIF 项目中相对多获益 0.29 pp（Cohen's d = 0.31, p < 1e-10）

**Ranking impact**: 整体 ρ = 0.9965（高度保留），但个体模型位移剧烈：
- 2024 cohort 平均排名下降 73 位（DIF 项目人为抬升了排名）
- 极端案例位移达 ±849 位
- DIF 受益者（排名下降最多）: 12/20 来自 2024 cohort，集中在 phi-3 和 llama-3 家族
- DIF 受害者（排名上升最多）: 18/20 来自 other cohort，主要是 7B mistral merges

**Rank displacement 直方图**是最有说服力的可视化——2024 cohort 有明显的左偏重尾（大量模型排名下降 200-800 位），而 2023 分布集中在零附近。

所有输出在 `artifacts/score_inflation_analysis/`：3 个 PDF 图、4 个 CSV、分析脚本和报告。

---
