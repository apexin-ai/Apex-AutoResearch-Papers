# paper results tex streamline

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results-tex-streamline_20260517T104711_result.json`
- **Structured JSON:** [`feb8d7e4046ea2ee654e.json`](../../sessions/fe/feb8d7e4046ea2ee654e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All modifications are clean. The `---` instances in lines 109 and 114 are pre-existing (not in my modification scope). Let me report the changes.

---

## 变更报告

### 修改 1：Line 193 段落拆分+精简

**Old**: 一个巨型段落（~12 行），包含四条件解释 + 2/3 vs 3/3 vs 2/5 对比 + τ_mag 分析 + τ_vel 分析 + "raising τ_vel to 0.15 eliminates both FP" 表述。

**New**: 拆为两段。
- **段 A**（条件解释）：四条件含义不变，2/3 rule 浓缩为一句 "balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline"。3/3 vs 2/5 对比删除，替换为 `\footnote{...Appendix~\ref{sec:appendix_sensitivity}}`。
- **段 B**（threshold calibration）：τ_mag=0.49 maximizes J=0.714（保留）。τ_vel stable across [0.05, 0.18]（一句话）。**已删除** "raising τ_vel to 0.15 eliminates both false positives" 及其后续解释。

### 修改 2A：Line 151→157 桥接过渡

**Old**: RSSM fidelity 段落直接结束，下一行是 `\subsection{Online CIVO Detection}`，无过渡。

**New**: 在 RSSM fidelity 结论句末尾追加："Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline."

### 修改 2B：Lines 96-99 F3-F5 条件名称+数字

**Old**: "unexposed trained embedding (008a) maintains NVE $\leq 0.93\times$, frozen embedding (015b) never exceeds $0.47\times$, and removed embedding (008f) shows NVE $\leq 0.97\times$" — 用实验 ID 做标签，读者需翻表才能理解条件含义。

**New**: "trained embedding without multi-rate exposure (008a, NVE $= 0.93\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\times$) both remain well below the $1.5\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\times$" — 条件名称自解释，并显式引用 1.5× threshold。追加了 `(Figure~\ref{fig:factorial_grid})` 和 `(Figure~\ref{fig:dt_amplification})` 交叉引用到附录图。

**数字验证**: 0.93×（008a）和 0.97×（008f）与 Table 1 和 `paper_data_walker_walk_index` 一致。任务建议的 1.08× 在数据中不存在，未使用。

### 修改 3：Line 231 70K 段落精简

**Old**: 4 句话（~80 words），重复 "no FP below 70K / no TP above 70K" + 额外 caveat + 实操建议。

**New**: 2 句话（~40 words）：timing pattern 一句 + practical guideline 一句。

### 备注
Lines 109, 114 存在 pre-existing `---` em-dash（F6 段落和 caption），不在本次修改范围内。如需一并清理请告知。

---
