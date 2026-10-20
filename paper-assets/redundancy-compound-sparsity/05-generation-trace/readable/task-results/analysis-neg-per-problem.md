# analysis neg per problem

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_neg-per-problem_20260512T002135_result.json`
- **Structured JSON:** [`7a51b779aa8282cc74ca.json`](../../sessions/7a/7a51b779aa8282cc74ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

### Per-Problem 异质性分析

**V2 (20 easy)**: r = 0.1428 ± 0.0238, 范围 [0.078, 0.183]
**V3 (5 hard)**: r = 0.1496 ± 0.0218, 范围 [0.116, 0.182]

**关键发现**:

1. **无异常值** — 全部 25 题 r < 0.2，没有任何题目 r > 0.3。效应 across-the-board 一致地弱。

2. **r vs CoT 长度** — V2 中 corr = 0.44 (p=0.051)，边缘显著；V3 中无相关 (corr = -0.11)；合并后 corr = 0.29 (p=0.17) 不显著。Longer CoT 没有稳定地带来更高 r。

3. **V2 vs V3 无显著差异** — Mann-Whitney U = 45, p = 0.77。Hard 题和 easy 题的 r 分布没有统计学差异，尽管 V3 mean 略高 0.007。

4. **V2 最低 r = 0.078**（prob 8: "8 人圆桌排列"，最短 CoT 698 tokens），**最高 r = 0.183**（prob 17: "袋中取球"，仅 748 tokens）—— 两个极端都是短 CoT，说明 CoT 长度不是决定性因素。

**结论**: redundancy-surprisal 的弱正相关是同质的，不存在被个别 problem 拉低或拉高的情况。

输出文件已保存到 `results/mvp/analysis/`:
- `per_problem_scatter.pdf` — 散点图 + 回归线
- `per_problem_box.pdf` — V2 vs V3 箱线图
- `per_problem_analysis.md` — 完整数据表和分析

---
