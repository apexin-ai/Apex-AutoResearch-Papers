# paper prepare c4 patch framework

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prepare_c4_patch_framework_20260519T203331_result.json`
- **Structured JSON:** [`dcb3a30a747a3537b40d.json`](../../sessions/dc/dcb3a30a747a3537b40d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the complete inventory:

---

## experiments.tex

### 行 4: RQ1 描述
当前文本: `(1)~Do Tier~1 exception signals generalize across models?`
需要更新: 无需改动

### 行 27: Table 1 (cross_model) — loop_only 行
当前文本: `loop\_only & 86.05{\scriptsize$\pm$0.52} & --- & 77.06 & 81.26 \\`
需要更新: **三模型数据全在此行**。DeepSeek 81.26 待更新为实际三模型结果；CodeLlama 77.06 和 Qwen 86.05 已确认。

### 行 38: Table 1 脚注 — loop_only 三 seed 明细
当前文本: `Qwen-7B \texttt{loop\_only} 3 seeds: 85.63/85.88/86.64 (mean 86.05\%).`
需要更新: 无需改动（Qwen 数据）。可能需追加 DeepSeek/CodeLlama 的 seed 明细。

### 行 67: §3.2 ablation 开头段
当前文本: `\texttt{loop\_only} is evaluated across three models to test Tier~2 generalization (Table~\ref{tab:cross_model}).`
需要更新: 无需改动（定性描述）

### 行 68: Tier hierarchy 核心定义
当前文本: `Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B and reveals a two-tier hierarchy: Tier~1 (\texttt{exception\_only}) generalizes across all four models (${\geq}$99.33\%), while Tier~2 (\texttt{loop\_only}) is model-dependent.`
需要更新: 无需改动（定性描述）

### 行 72: Table 2 (ablation) caption — loop_only 三 seed 明细
当前文本: `$^\ddag$\texttt{loop\_only}: 3-seed mean 86.05\%$\pm$0.52 (85.63/85.88/86.64).`
需要更新: 无需改动（Qwen-7B only）

### 行 78: Table 2 header — Tier 列
当前文本: `\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\`
需要更新: 无需改动

### 行 84: Table 2 — loop_only 数据行
当前文本: `loop\_only & loop compression & 86.05$^\ddag$ & [83.97, 87.96] & 2 \\`
需要更新: 无需改动（Qwen-7B ablation table）

### 行 96: Tier 1 讨论段
当前文本: `Tier~1 signals are individually sufficient: \texttt{exception\_only} (99.83\%$\pm$0.00) exceeds VOTA...`
需要更新: 无需改动

### 行 98: **Tier 2 三模型对比 — 关键数据行**
当前文本: `Tier~2 \texttt{loop\_only} improves over \texttt{no\_trace} but is model-dependent: +10.92pp on Qwen-7B (86.05\%, 3-seed mean, $p{<}0.0001$), +7.90pp on DeepSeek (81.26\%, CI [79.08, 83.45]), but only +0.59pp on CodeLlama (77.06\%, not significant).`
需要更新: **DeepSeek 81.26% 和 +7.90pp 待更新**（三模型 loop_only 数据 patch 核心位置）。CodeLlama 77.06/+0.59pp 已确认 negative。

### 行 171: Calibration 段 — tier hierarchy 引用
当前文本: `Calibration mirrors the tier hierarchy...`
需要更新: 无需改动

---

## introduction.tex

### 行 30: C3 (Contribution 3) — Two-tier hierarchy
当前文本: `\item \textbf{Two-tier diagnostic hierarchy}: Tier~1 signals (exceptions, assertions) generalize across three models (${\geq}$99\%), while Tier~2 (loop compression) is model-dependent: Qwen +10.9pp, DeepSeek +7.9pp, CodeLlama +0.6pp over no trace (\S\ref{sec:ablation}).`
需要更新: **DeepSeek +7.9pp 待更新**（三模型结果确定后）。Qwen +10.9pp 和 CodeLlama +0.6pp 已确认。

---

## discussion.tex

### 行 25-27: Tier hierarchy and methodological implications
当前文本 (行26): `The two-tier structure (Tier~1 ${\geq}$99\% across models; Tier~2 = 77.1--86.1\%) suggests a fallback design: extract exception events first (median 150 tokens), resort to Tier~2 only when no exception is raised (model-dependent, +0.6--10.9pp over no-trace).`
需要更新: **Tier~2 range "77.1--86.1%" 和 "+0.6--10.9pp" 待更新**（取决于 DeepSeek 最终数值）

### 行 30-31: Density-robustness gradient
当前文本 (行30): `\texttt{loop\_only} spans 8.99pp (77.06--86.05\%), with lifts over \texttt{no\_trace} following a gradient (+10.9 $>$ +7.9 $>$ +0.6pp, the last not significant).`
需要更新: **"8.99pp"、"77.06--86.05%"、"+7.9" 待更新**

---

## conclusion.tex

### 行 4: loop 信号总结
当前文本: `while lower-density loop signals are model-dependent (+0.6--10.9pp)`
需要更新: **"+0.6--10.9pp" range 待更新**（取决于 DeepSeek 最终 lift）

---

## appendix.tex

### 行 21: Full results table — Loop Only / Qwen-7B
当前文本: `Loop Only & Qwen-2.5-7B & 86.05 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\`
需要更新: 无需改动（Qwen-7B 数据）。**此表没有 DeepSeek/CodeLlama 的 loop_only 行 — 可能需要新增。**

### 行 219: Per-seed table — loop_only
当前文本: `loop\_only & 85.63 & 85.88 & 86.64 & 86.05 $\pm$ 0.52 \\`
需要更新: 无需改动（Qwen-7B only）

### 行 533-535: Calibration discussion — Tier hierarchy
当前文本: `Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.`
需要更新: 无需改动

---

## 汇总：DeepSeek 结果到手后需要更新的位置

| # | 文件 | 行 | 需改内容 |
|---|------|-----|----------|
| 1 | experiments.tex | 27 | Table 1 loop_only DS-6.7B: `81.26` → 实际值 |
| 2 | experiments.tex | 98 | `+7.90pp on DeepSeek (81.26\%, CI [79.08, 83.45])` → 实际值 |
| 3 | introduction.tex | 30 | `DeepSeek +7.9pp` → 实际 lift |
| 4 | discussion.tex | 26 | `Tier~2 = 77.1--86.1\%` range 和 `+0.6--10.9pp` |
| 5 | discussion.tex | 30 | `8.99pp (77.06--86.05\%)` span 和 `+7.9` |
| 6 | conclusion.tex | 4 | `+0.6--10.9pp` range |

如果 DeepSeek loop_only 不再是 81.26%，还需检查 gradient 排序 (+10.9 > +7.9 > +0.6) 是否仍成立，以及 "not significant" 判断是否只对 CodeLlama 适用。

---
