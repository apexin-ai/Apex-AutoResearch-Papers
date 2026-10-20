# viz regen figures 1024

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_regen_figures_1024_20260514T233319_result.json`
- **Structured JSON:** [`690c374f9e38b9393c9b.json`](../../sessions/69/690c374f9e38b9393c9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个图表已生成并保存到本地 artifacts 目录：

**fig_selection_gap_1024.pdf** — 双轴图：Spearman ρ（柱）+ ΔF1 vs greedy（菱形线）。NER 中 LogProb 选择比 greedy 高 +0.6pp，SJ +0.1pp；RE 中所有方法 F1 均低于 greedy（SJ -1.9pp, VotConf -4.5pp, LogProb -0.9pp）。Oracle gap 分别为 +13.2pp 和 +18.1pp。

**fig_reliability_1024.pdf** — 校准曲线 + 分布直方图。NER 三个信号校准良好（ECE 0.069-0.096）；RE 中 Logprob 校准最差（ECE=0.339），Voting Conf 最好（ECE=0.109）。

注意：这里的 ECE 是 calibration ECE（confidence → mean F1 的偏差），与 `all_signals_5signal.json` 中的 binary ECE（0.453/0.353 等）定义不同——后者用 binary correctness 作为 accuracy。

---
