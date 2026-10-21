# Cross-Architecture 14B Table Prep Memo

## 1. 当前论文中 14B 表格位置

**Table `\ref{tab:14b}`** — `experiments.tex` lines 231–248

- 段落标题: `\paragraph{Scale Generalization: Qwen-2.5-14B.}` (line 226)
- Label: `\label{sec:14b}` (line 227)
- Caption: "Qwen-2.5-14B at 30% sparsity (global top-k allocation)"

## 2. 已有 global_topk 数据汇总 (table 当前内容)

| Method | PPL | ARC-c | WG | MMLU | GSM8K |
|--------|-----|-------|-----|------|-------|
| Dense | 5.19 | 67.58 | 81.06 | 79.77 | 87.57 |
| KL (Ours) | **7.62** | 57.17 | 72.06 | 63.72 | 48.82 |
| TEAL vanilla | 8.73 | 56.83 | 72.69 | 71.83 | 49.51 |
| BCE | 8.76 | **57.59** | **72.61** | 71.67 | 53.07 |

**核心问题**: KL PPL 最优 (7.62 vs 8.73/8.76), 但 MMLU 最差 (63.72 vs 71.83/71.67), 差 8pp。

## 3. Uniform 数据到位后需更新的位置

### 3.1 Table `tab:14b` (lines 231–248)

当前 line 245 有 commented-out row:
```latex
% KL uniform & TBD & TBD & TBD & TBD & TBD \\ % exp_id: qwen14b_kl30_uniform (running, ~3-4h)
```
需要: 取消注释, 填入 5 个数值。

### 3.2 叙事段落 (lines 226–229)

当前文字:
> "Table~\ref{tab:14b} evaluates on Qwen-2.5-14B at 30%: KL achieves PPL 7.62 (1.47× dense, matching the 8B ratio), while TEAL (8.73) and BCE (8.76) are 14–15% worse."

需要: 加入 uniform 结果的描述, 并根据 MMLU 结果调整 narrative。

### 3.3 Table caption (line 233)

当前 caption 说 "global top-k allocation"。如果加入 uniform row, 需要修改 caption 说明包含两种 allocation。

### 3.4 可能影响的其他位置

- `paper_framing.md` Claim 4 (Reviewer Concern #4): 当前写 "KL PPL=7.62 (1.47× dense ratio, identical to 8B's 1.47×)" — 如果 uniform MMLU 好, 加强 claim; 否则需 hedge
- Table `tab:phase` (lines 153–179): 当前只有 8B 数据, 考虑是否在 appendix 加 14B phase analysis
- `\S\ref{sec:scaling}` 的 Three Operating Regions 段落 (line 192): 引用了 `\S\ref{sec:cross_arch}` 说 "consistent on both 7–8B models" — 14B uniform 数据可强化或弱化此 claim

## 4. 两种情景的叙事调整方案

### 情景 A: Uniform KL MMLU > 70% (allocation 是根因)

**诊断**: 14B 和 8B 一样, global top-k 的 late-layer starvation 在更大模型上对 knowledge-intensive tasks (MMLU) 伤害更大。Uniform allocation 修复了这个问题。

**叙事调整**:

1. **Tab:14b caption 改为**: "Qwen-2.5-14B at 30% sparsity. KL uniform is recommended for deployment (consistent with 8B findings, Table~\ref{tab:phase})."

2. **Line 226–229 改写**:
   > "Table~\ref{tab:14b} evaluates on Qwen-2.5-14B at 30% sparsity. Under global allocation, KL achieves the best PPL (7.62, 1.47× dense) but MMLU degrades to 63.7% due to late-layer starvation amplified at larger scale. Uniform allocation restores MMLU to [X]% while maintaining competitive PPL [Y], replicating the 8B finding that allocation strategy, not predictor quality, determines downstream preservation at moderate sparsity."

3. **Strengthened claim**: 加入 `\S\ref{sec:scaling}` 的 phase transition narrative, 说 14B confirms the budget-surplus regime pattern at larger scale — uniform 是 correct operating point。

4. **额外加分**: 如果 uniform KL 同时 PPL 也不差 (类似 8B 的 8.82 vs 8.98), 可以 bold 更多 columns, 强化 "uniform dominates Pareto frontier at 30%"。

### 情景 B: Uniform KL MMLU 仍 ~63% (KL 在 14B 有结构性问题)

**诊断**: 问题不在 allocation, 而在 KL objective 本身。KL 优化 output distribution, 可能过度拟合 PPL-relevant tokens 而忽略 MMLU 需要的 knowledge neurons。14B 模型 knowledge 更集中, KL 的 mode-covering 不够精确。

**叙事调整**:

1. **弱化 claim, 不回避**:
   > "At 14B scale, KL maintains its PPL advantage (7.62 vs 8.73) and the 1.47× dense ratio generalizes exactly. However, MMLU drops to 63.7% under both allocation strategies, while magnitude-based methods (TEAL/BCE) preserve 71%+. This suggests a scale-dependent dissociation: output-distribution fidelity (PPL) does not guarantee knowledge preservation at larger scales where factual knowledge is more concentrated in specific neuron subsets."

2. **重新定位 14B 的 contribution**:
   - PPL generalization 仍是 positive signal (ratio 精确匹配)
   - BCE native allocation collapse (6.4% sparsity) 仍然成立 — "gradient insufficiency generalizes"
   - MMLU gap 作为 limitation/future work: "Combining KL's distributional objective with targeted knowledge-neuron preservation remains open"

3. **Table 呈现**: 不要 bold MMLU column for any sparse method (都比 dense 差很多), 把 narrative focus 放在 PPL 和 "no compensation needed" 上。

4. **Abstract/Introduction 调整**: 避免任何暗示 "KL 在所有 metrics 上 dominate" 的措辞。改为 "KL eliminates compensation while achieving best perplexity across scales (8B, 14B); downstream preservation is allocation-dependent at moderate sparsity."

5. **Discussion 加段**: "The PPL-MMLU dissociation at 14B suggests distributional fidelity is necessary but not sufficient for knowledge-intensive tasks at scale, pointing to hybrid objectives as a promising direction."

## 5. 优先级行动项

| Priority | Action | Trigger |
|----------|--------|---------|
| P0 | uniform 结果到位后填入 tab:14b line 245 | 实验完成 |
| P1 | 根据 MMLU 结果选择情景 A/B, 改写 lines 226–229 | 数据确认 |
| P2 | 更新 tab:14b caption (line 233) | 同上 |
| P3 | 检查 sec:scaling line 192 的 cross-arch reference 是否需修改 | 同上 |
| P4 | 如情景 B, 在 limitations.tex 加入 scale-dependent dissociation 段 | 情景 B 确认 |
