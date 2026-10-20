# Reviewer 2 coordination — Part 2 of 2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/4b/4b53966e97d3abe72ec6.json)

## Round 11

### User

_source line 467 · 2026-05-15T12:39:36.619097+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文（审查侧重：方法严谨性 + 实验设计 + 统计有效性，Overall 3.0/5）。

请逐条回应每个 Must-Fix 和 Should-Fix 问题：用 `[AGREE]` 表示同意并说明理由，或 `[REBUT]` 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 的 Must-Fix 问题：

**N1** [critical] G 指标定义在论文内部不一致，导致数值差异高达 5–35 倍
- Eq. (2) 定义 per-problem G^(i) 的 median（median of ratios），Appendix B Table 4 使用 ratio of medians。s=0.15 时差异 69 vs 7.5（9.2 倍）。当 II_high ≈ 0 时 per-problem G^(i) 会爆炸。

**N2** [critical] 仅测试一种 importance 评分方法，却对"importance-based eviction"做类别性结论
- 论文使用 position-normalized cumulative attention mass，但结论泛化为"importance-based eviction"整个类别。Discussion 声称 "broad applicability" 基于 H2O/SnapKV/PyramidKV 共享 attention-mass 评分，但这些方法的具体实现差异很大。

**N3** [critical] 唯一的严重性指标是 perplexity，无下游任务准确率验证
- 与你的 N1 一致。II 基于 perplexity ratio，MATH-500 的实际任务指标是 problem-level accuracy。

### Reviewer 1 的 Should-Fix 问题：

**W1** [warning] "Cross-model replication" 实际是同架构复现，非独立验证
- 两个主要模型共享 Qwen2ForCausalLM 架构，Section 5.4 标题容易误导。

**W2** [warning] LLaMA n=49 的统计证据混乱
- s=0.15 CI 排除零但 Wilcoxon 不显著；s=0.30 CI 包含零但 Wilcoxon 显著。未解释为何不运行 n=500。

**W3** [warning] Bonferroni k=4 的 family 分组可能过于宽松
- 44 个检验分为多个 family 各用 k=4，BH-FDR 部分缓解。

**W4** [warning] 43:1 mean/median ratio 暗示极端离群值未分析
- 可能来自特定类型数学题或 phase segmentation 边界效应。

**W5** [warning] Pilot mitigation 失败但 Conclusion 仍说 "motivate phase-aware sparsity allocation"
- 从 failed pilot 到 "motivate" 的跳跃过大。

### Reviewer 1 的小问题：
- Table 2 中 Qwen s=0.15 II_high = -0.000 负号是 numerical artifact
- Figure 1 用 n=50 vs main results 用 n=496
- Section 5.3 中 1.498 vs Table 2 中 1.514 数值不一致
- 3 个 bib 条目在 OpenAlex 中未找到

---

请对以上每条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-15T12:40:23.502887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": "78",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "offset": "78",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-15T12:40:23.956390+00:00_

78	\subsection{Phase-Strategy Crossover}
79	\label{sec:crossover}
80	
81	For DeepSeek, a strategy ranking reversal emerges at all four sparsity levels ($n{=}496$): at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.498$---a $2.7{\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\times}$ to $4.0{\times}$ across $s \in \{0.15, 0.20, 0.25, 0.30\}$. Qwen does not exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.109$; low $1.043$ vs.\ $1.770$), indicating that the ranking reversal is model-dependent. Full crossover analysis appears in Appendix~\ref{app:crossover-details}. % exp_id: n500_unified_final, crossover_all_sparsity.csv; DS s025: imp_low/rand_low=3.971/1.498=2.65; QW no crossover
82	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-15T12:40:24.459002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": "8",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "offset": "8",
    "limit": "12"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-15T12:40:24.911505+00:00_

8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.498$---a $2.7{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.7{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.109$; low $1.043$ vs.\ $1.770$). % exp_id: crossover_all_sparsity.csv; DS reversal: diff_low/diff_high = 2.99, 2.83, 2.13, 1.66
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.7{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-15T12:40:25.313992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": "29",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "offset": "29",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-15T12:40:25.364809+00:00_

29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=}496$. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) increases from $7.5{\times}$ (95\% CI: $[4.1, 11.4]$) at $s{=}0.15$ to $79.8{\times}$ ($[63.3, 96.5]$) at $s{=}0.30$ under importance-based eviction, with all CIs excluding 1. Strong phase modulation is specific to importance-based eviction ($G{=}7.5$--$79.8{\times}$). Random eviction shows weak but statistically significant modulation at $s \geq 0.25$ ($G \approx 1.1$--$1.3$; CIs exclude 1), while at $s \leq 0.20$ the CIs span or touch 1. Figure~\ref{fig:hero} visualizes this contrast. % exp_id: n500_unified_final; G from table2_n500_full.csv
30	
31	\begin{table*}[t]
32	\centering
33	\small
34	\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta$: paired median difference with bootstrap 95\% CI ($B{=}10{,}000$). $G$: per-problem amplification ratio (Eq.~\ref{eq:gradient}) with bootstrap 95\% CI. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
35	\label{tab:main-results}
36	\begin{tabular}{@{}llcccc@{}}
37	\toprule
38	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $G$\; [95\% CI] \\
39	\midrule
40	\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
41	0.15 & Importance & 0.003 & 0.357 & 0.39\; $[0.35,\; 0.44]$ & $\mathbf{7.5}$\; $[4.1,\; 11.4]$ \\ % exp_id: n500_unified_final
42	0.15 & Random     & 0.083 & 0.090 & 0.01\; $[-0.02,\; 0.04]$ & 0.5\; $[0.4,\; 0.6]$ \\
43	\addlinespace
44	0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $\mathbf{17.9}$\; $[12.7,\; 26.3]$ \\
45	0.20 & Random     & 0.270 & 0.357 & 0.03\; $[-0.01,\; 0.08]$ & 0.8\; $[0.6,\; 0.9]$ \\
46	\addlinespace
47	0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $\mathb
…[truncated 119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-15T12:42:32.082090+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[AGREE] R1-N1: G 指标定义不一致（ratio of medians vs median of ratios）**\n\nR1 的观察是准确的。我核实了以下数值：\n- Table 2（§5.2, main results, n=496）：G = 7.5 [4.1, 11.4] at s=0.15 — **median of per-problem ratios**（Eq. 2）\n- Table 4（Appendix B, profiling, n=50）：G = 69 at s=0.15 — **ratio of medians**（caption 明确标注 \"$G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$\"）\n\n两种计算方式在 $\\mathrm{II}_{\\textit{high}} \\approx 0$ 时严重分歧。以 DeepSeek s=0.15 为例：$\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.003$（Table 2），ratio of medians = 0.357/0.003 ≈ 119，而 median of per-problem ratios = 7.5。差异来源是 per-problem $G^{(i)}$ 的分布极度右偏（部分 problem 的 $\\mathrm{II}_{\\textit{high}}^{(i)}$ 极小导致 ratio 爆炸，median 抑制了这些极端值）。\n\n论文虽在 Table 4 caption 中注明了差异，但这两个不同定义使用同一符号 $G$，且 Abstract 中的 \"$G$ of $7.5$--$79.8\\times$\" 与 Appendix 的 $69$--$274\\times$ 给读者造成混淆。更关键的是，**论文应统一使用一种 $G$ 定义**（建议全文使用 median of per-problem ratios + bootstrap CI，因其更 robust），或至少在首次出现时明确区分两种计算方式。\n\n补充我自己的 W5 的相关发现：Abstract 中 \"bootstrap 95% CI: [4.1, 96.5]\" 实际上是将四个 sparsity level 的 CI 端点拼接（4.1 来自 s=0.15 lower bound, 96.5 来自 s=0.30 upper bound），不是单一参数的 CI，属于统计呈现不规范。\n\n---\n\n**[AGREE] R1-N2: 单一 importance 评分方法不支持类别性结论**\n\nR1 的批评有道理。论文仅测试了 position-normalized cumulative attention mass（Eq. 3, Appendix A），但 Discussion §7 声称 \"Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H2O, SnapKV, PyramidKV), suggesting broad applicability\"。\n\n我部分同意并补充：\n1. **方向上**，discrimination collapse 机制（head pruning 压平 importance score 分布）在理论上适用于任何基于 attention mass 的评分，因为 head pruning 改变 attention 分布这一事实独立于具体评分公式。因此**定性方向**可能 generalizable。\n2. **定量上**，R1 正确指出 H2O（heavy-hitter 选择）、SnapKV（observation window 聚合）、PyramidKV（层级自适应 budget）的具体实现差异很大。不同聚合方式对 discrimination collapse 的敏感度可能不同。论文没有证据支持定量结论的泛化。\n3. 建议：将 \"broad applicability\" 改为 \"directionally consistent prediction for attention-mass-based methods\"，并明确标注这是一个未验证的推测。\n\n---\n\n**[AGREE] R1-N3: 缺少 downstream accuracy 验证**\n\n与我的 N1 完全一致。补充两点：\n\n1. **这个问题比 R1 描述的可能更严重**：PPL 是 per-token 指标，而 MATH-500 的评估单位是 problem-level accuracy（final answer 正确与否）。Low-sparsity phase 通常对应 exploratory reasoning（Abstract 所述），此 phase 的 token 对最终答案的贡献可能远低于 high-sparsity phase（structured computation）的 token。因此，即使 low-sparsity phase PPL 退化严重（$G \\gg 1$），如果退化集中在对 final answer 不关键的 reasoning trace 上，整体 accuracy 可能不受影响——这将从根本上改变论文的结论。\n\n2. **反过来说**，如果作者能展示 II 与 problem-level accuracy 之间存在显著相关（例如 high-II problems 更可能答错），这将**大幅增强论文的说服力**。这不需要新的实验，只需要在现有数据上做 regression analysis。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: \"Cross-model replication\" 标题具有误导性**\n\n§5.4 标题为 \"Cross-Model Replication\"，但 Appendix D 开头明确承认 \"Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA)\"。这实际上是 **cross-training-methodology replication**（distillation vs instruction tuning on same architecture），不是 cross-architecture。§5.5 才是 cross-architecture（LLaMA），但那里的证据很弱。\n\n建议将 §5.4 改为 \"Cross-Training Replication\" 或 \"Within-Architecture Replication\"，避免读者误以为是独立架构的验证。这与我自己的 N2 中 \"两个 Qwen2 模型共享 backbone，cross-model replication 的独立性有限\" 一致。\n\n---\n\n**[AGREE] R1-W2: LLaMA n=49 的统计证据混乱，且未解释为何不跑 n=500**\n\n两个层面的问题：\n\n1. **CI/Wilcoxon 不一致**：论文 footnote（§5.5）给出了合理的统计解释——percentile bootstrap CI 对尾部不敏感，Wilcoxon signed-rank 对尾部 outlier 更敏感。在 n=49 + heavy-tailed 条件下，两种方法的 power profile 不同。这个解释本身是正确的。\n\n2. **为何不跑 n=500？** 这是 R1 的关键追问，论文完全没有回应。如果资源允许在 DeepSeek 和 Qwen 上各跑 500 题，为什么 LLaMA 只跑了 49？可能的原因包括：(a) 计算资源限制（LLaMA-8B 比 Qwen-7B 稍大）；(b) n=49 已经显示效果很弱，作者判断跑更多也不会改变 \"preliminary\" 的定性结论。但论文应该明确说明原因，因为 49 这个数字暗示这是 profiling subset 的遗留而非有意设计。\n\n---\n\n**[REBUT] R1-W3: Bonferroni k=4 的 family 分组**\n\nR1 认为 k=4 \"可能过于宽松\"，我部分不同意。\n\n论文的 Bonferroni 分组策略是：每个 model × strategy 组合内，4 个 sparsity level 测试同一个 dose-response 假设。这在统计学上是合理的 family 定义——同一实验条件下对同一科学问题的多次检验。如果将所有 44 个检验放在一个 family（Bonferroni k=44），则过于保守。\n\n更重要的是，**论文已在 Appendix E（Table 5）报告了 BH-FDR correction across all 44 tests**。结果：所有 32 个 Bonferroni-significant 结果在 BH-FDR 下仍然 significant（§Appendix E: \"All Bonferroni-significant results remain significant under BH-FDR\"）。BH-FDR 额外恢复了 5 个 result，全部是 random eviction 的弱效应。\n\n因此，无论使用哪种 correction 策略，**核心结论（importance-based eviction 的 phase gradient）均不受影响**。R1 的担忧在技术上有道理，但实际影响为零。\n\n---\n\n**[AGREE] R1-W4: 43:1 mean/median ratio 的极端离群值未分析**\n\n§4 (methodology.tex line 18) 提到 \"mean/median ratios up to 43:1\"，Extended Limitations (Appendix G) 也提到。但论文从未分析这些极端 outlier 来自哪里。\n\n可能的来源：\n1. **Phase segmentation 边界效应**：非常短的 phase segment（接近 min_phase_length=10）可能产生 volatile PPL 估计。\n2. **特定题目类型**：某些数学领域（如 combinatorics 可能产生更长更复杂的 reasoning trace，放大了 compound sparsity 效应）。\n3. **Numerical artifacts**：bfloat16 精度在极端 softmax 值下的 noise。\n\n作者应至少做一个 outlier 分析：报告 top-10 outlier problems 的特征（subject area、sequence length、phase distribution），并验证去除 top-5% outlier 后主要结论是否稳健。这对论文的可信度很重要。\n\n---\n\n**[AGREE] R1-W5: Pilot failure 与 \"motivate\" 之间的 framing 跳跃**\n\n与我的 N3 完全一致。补充：\n\nConclusion §8 最后一句：\"These findings motivate phase-aware sparsity allocation for reasoning model deployment.\" 但 §7 Discussion 的 pilot 结果是：oracle recovery 18%（gate FAIL），heuristic 32%（CI 跨零）。从 failed pilot 直接跳到 \"motivate\" 在逻辑上不连贯。\n\nR1 和我在这个问题上的判断一致：论文应将 framing 从 \"motivate solution X\" 调整为 \"characterize phenomenon Y, which is a prerequisite for future solutions\"。这样既诚实又仍有贡献价值。\n\n---\n\n### 小问题回应\n\n**[AGREE] Table 2 中 Qwen s=0.15 $\\mathrm{II}_{\\textit{high}} = -0.000$**\n我也在小问题 M1 中指出了这个问题。这几乎确定是 numerical noise（bfloat16 精度下，PPL ratios 的微小偏差），但论文应在 footnote 或 text 中说明。\n\n**[AGREE] Figure 1 用 n=50 vs main results 用 n=496**\n我在小问题 M3 中也指出。Hero figure 应用 full-scale 数据，否则会让读者质疑为什么主图不用最好的数据。\n\n**[AGREE] §5.3 中 1.498 vs Table 2 中 1.514**\n我核实了具体数值：\n- Table 2（§5.2）：Random s=0.25, $\\widetilde{\\mathrm{II}}_{\\textit{low}} = 1.514$\n- §5.3 正文：\"$3.971$ vs.\\ $1.498$\"\n- Appendix C（appendix_moved.tex）：同样使用 \"$1.498$\"\n\n数值不一致（1.498 vs 1.514）。从 LaTeX 注释看，§5.3 引用 crossover_all_sparsity.csv，而 Table 2 引用 table2_n500_full.csv。两个 CSV 文件可能使用了略有不同的聚合方式。虽然差异很小（1.1%），但同一论文中对同一量的报告应一致。\n\n进一步发现：Qwen crossover 数值也有类似小不一致——§5.3/Appendix 报告 Qwen s=0.25 importance low 为 1.043，但 Table 2 为 1.053。同样量级的偏差。这暗示 crossover 分析可能使用了不同的 problem subset 或不同的聚合路径，需要作者澄清。\n\n**[AGREE] 3 个 bib 条目 OpenAlex 未找到**\n我的验证结果一致：defensivekv-iclr2026、hies-2025、phase-transition-compression-2026 未在 OpenAlex 中匹配。三者均有有效 arXiv URL。很可能是 OpenAlex 索引延迟，不是 fabricated references。\n\n---\n\n### 总结：与 Reviewer 1 的主要分歧和共识\n\n| 议题 | R1 | R2 | 一致性 |\n|------|-----|-----|--------|\n| G 指标不一致 (N1) | Critical | Agree, 补充 Abstract CI 拼接问题 | ✅ 一致 |\n| 单一 importance 方法 (N2) | Critical | Agree 定量层面; 定性方向可能 generalizable | ⚠️ 部分一致 |\n| 缺 accuracy (N3) | Critical | Agree, 补充 phase-accuracy 关系分析 | ✅ 一致 |\n| Cross-model 误导 (W1) | Warning | Agree | ✅ 一致 |\n| LLaMA n=49 (W2) | Warning | Agree; CI/Wilcoxon 解释合理但 n=49 原因缺失 | ✅ 一致 |\n| Bonferroni k=4 (W3) | Warning | **Rebut**: family 定义合理, BH-FDR 已验证 | ❌ 分歧 |\n| 43:1 outliers (W4) | Warning | Agree, 建议 outlier profiling | ✅ 一致 |\n| Pilot fail vs motivate (W5) | Warning | Agree, 应调整 framing | ✅ 一致 |\n\n**唯一分歧**在 W3（Bonferroni family 分组）：R1 认为 k=4 可能宽松，我认为 family 定义合理且 BH-FDR 已覆盖。这不影响任何核心结论。\n\n**两位 reviewer 共识**：最严重的三个问题是 (1) 缺少 downstream accuracy, (2) G 指标定义不一致, (3) generalizability 受限。这些是 author response 必须回应的核心问题。\n\n*Reviewer 2, 交叉回应完成。*",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[AGREE] R1-N1: G 指标定义不一致（ratio of medians vs median of ratios）**\n\nR1 的观察是准确的。我核实了以下数值：\n- Table 2（§5.2, main results, n=496）：G = 7.5 [4.1, 11.4] at s=0.15 — **median of per-problem ratios**（Eq. 2）\n- Table 4（Appendix B, profiling, n=50）：G = 69 at s=0.15 — **ratio of medians**（caption 明确标注 \"$G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$\"）\n\n两种计算方式在 $\\mathrm{II}_{\\textit{high}} \\approx 0$ 时严重分歧。以 DeepSeek s=0.15 为例：$\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.003$（Table 2），ratio of medians = 0.357/0.003 ≈ 119，而 median of per-problem ratios = 7.5。差异来源是 per-problem $G^{(i)}$ 的分布极度右偏（部分 problem 的 $\\mathrm{II}_{\\textit{high}}^{(i)}$ 极小导致 ratio 爆炸，median 抑制了这些极端值）。\n\n论文虽在 Table 4 caption 中注明了差异，但这两个不同定义使用同一符号 $G$，且 Abstract 中的 \"$G$ of $7.5$--$79.8\\times$\" 与 Appendix 的 $69$--$274\\times$ 给读者造成混淆。更关键的是，**论文应统一使用一种 $G$ 定义**（建议全文使用 median of per-problem ratios + bootstrap CI，因其更 robust），或至少在首次出现时明确区分两种计算方式。\n\n补充我自己的 W5 的相关发现：Abstract 中 \"bootstrap 95% CI: [4.1, 96.5]\" 实际上是将四个 sparsity level 的 CI 端点拼接（4.1 来自 s=0.15 lower bound, 96.5 来自 s=0.30 upper bound），不是单一参数的 CI，属于统计呈现不规范。\n\n---\n\n**[AGREE] R1-N2: 单一 importance 评分方法不支持类别性结论**\n\nR1 的批评有道理。论文仅测试了 position-normalized cumulative attention mass（Eq. 3, Appendix A），但 Discussion §7 声称 \"Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H2O, SnapKV, PyramidKV), suggesting broad applicability\"。\n\n我部分同意并补充：\n1. **方向上**，discrimination collapse 机制（head pruning 压平 importance score 分布）在理论上适用于任何基于 attention mass 的评分，因为 head pruning 改变 attention 分布这一事实独立于具体评分公式。因此**定性方向**可能 generalizable。\n2. **定量上**，R1 正确指出 H2O（heavy-hitter 选择）、SnapKV（observation window 聚合）、PyramidKV（层级自适应 budget）的具体实现差异很大。不同聚合方式对 discrimination collapse 的敏感度可能不同。论文没有证据支持定量结论的泛化。\n3. 建议：将 \"broad applicability\" 改为 \"directionally consistent prediction for attention-mass-based methods\"，并明确标注这是一个未验证的推测。\n\n---\n\n**[AGREE] R1-N3: 缺少 downstream accuracy 验证**\n\n与我的 N1 完全一致。补充两点：\n\n1. **这个问题比 R1 描述的可能更严重**：PPL 是 per-token 指标，而 MATH-500 的评估单位是 problem-level accuracy（final answer 正确与否）。Low-sparsity phase 通常对应 exploratory reasoning（Abstract 所述），此 phase 的 token 对最终答案的贡献可能远低于 high-sparsity phase（structured computation）的 token。因此，即使 low-sparsity phase PPL 退化严重（$G \\gg 1$），如果退化集中在对 final answer 不关键的 reasoning trace 上，整体 accuracy 可能不受影响——这将从根本上改变论文的结论。\n\n2. **反过来说**，如果作者能展示 II 与 problem-level accuracy 之间存在显著相关（例如 high-II problems 更可能答错），这将**大幅增强论文的说服力**。这不需要新的实验，只需要在现有数据上做 regression analysis。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: \"Cross-model replication\" 标题具有误导性**\n\n§5.4 标题为 \"Cross-Model Replication\"，但 Appendix D 开头明确承认 \"Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA)\"。这实际上是 **cross-training-methodology replication**（distillation vs instruction tuning on same architecture），不是 cross-architecture。§5.5 才是 cross-architecture（LLaMA），但那里的证据很弱。\n\n建议将 §5.4 改为 \"Cross-Training Replication\" 或 \"Within-Architecture Replication\"，避免读者误以为是独立架构的验证。这与我自己的 N2 中 \"两个 Qwen2 模型共享 backbone，cross-model replication 的独立性有限\" 一致。\n\n---\n\n**[AGREE] R1-W2: LLaMA n=49 的统计证据混乱，且未解释为何不跑 n=500**\n\n两个层面的问题：\n\n1. **CI/Wilcoxon 不一致**：论文 footnote（§5.5）给出了合理的统计解释——percentile bootstrap CI 对尾部不敏感，Wilcoxon signed-rank 对尾部 outlier 更敏感。在 n=49 + heavy-tailed 条件下，两种方法的 power profile 不同。这个解释本身是正确的。\n\n2. **为何不跑 n=500？** 这是 R1 的关键追问，论文完全没有回应。如果资源允许在 DeepSeek 和 Qwen 上各跑 500 题，为什么 LLaMA 只跑了 49？可能的原因包括：(a) 计算资源限制（LLaMA-8B 比 Qwen-7B 稍大）；(b) n=49 已经显示效果很弱，作者判断跑更多也不会改变 \"preliminary\" 的定性结论。但论文应该明确说明原因，因为 49 这个数字暗示这是 profiling subset 的遗留而非有意设计。\n\n---\n\n**[REBUT] R1-W3: Bonferroni k=4 的 family 分组**\n\nR1 认为 k=4 \"可能过于宽松\"，我部分不同意。\n\n论文的 Bonferroni 分组策略是：每个 model × strategy 组合内，4 个 sparsity level 测试同一个 dose-response 假设。这在统计学上是合理的 family 定义——同一实验条件下对同一科学问题的多次检验。如果将所有 44 个检验放在一个 family（Bonferroni k=44），则过于保守。\n\n更重要的是，**论文已在 Appendix E（Table 5）报告了 BH-FDR correction across all 44 tests**。结果：所有 32 个 Bonferroni-significant 结果在 BH-FDR 下仍然 significant（§Appendix E: \"All Bonferroni-significant results remain significant under BH-FDR\"）。BH-FDR 额外恢复了 5 个 result，全部是 random eviction 的弱效应。\n\n因此，无论使用哪种 correction 策略，**核心结论（importance-based eviction 的 phase gradient）均不受影响**。R1 的担忧在技术上有道理，但实际影响为零。\n\n---\n\n**[AGREE] R1-W4: 43:1 mean/median ratio 的极端离群值未分析**\n\n§4 (methodology.tex line 18) 提到 \"mean/median ratios up to 43:1\"，Extended Limitations (Appendix G) 也提到。但论文从未分析这些极端 outlier 来自哪里。\n\n可能的来源：\n1. **Phase segmentation 边界效应**：非常短的 phase segment（接近 min_phase_length=10）可能产生 volatile PPL 估计。\n2. **特定题目类型**：某些数学领域（如 combinatorics 可能产生更长更复杂的 reasoning trace，放大了 compound sparsity 效应）。\n3. **Numerical artifacts**：bfloat16 精度在极端 softmax 值下的 noise。\n\n作者应至少做一个 outlier 分析：报告 top-10 outlier problems 的特征（subject area、sequence length、phase distribution），并验证去除 top-5% outlier 后主要结论是否稳健。这对论文的可信度很重要。\n\n---\n\n**[AGREE] R1-W5: Pilot failure 与 \"motivate\" 之间的 framing 跳跃**\n\n与我的 N3 完全一致。补充：\n\nConclusion §8 最后一句：\"These findings motivate phase-aware sparsity allocation for reasoning model deployment.\" 但 §7 Discussion 的 pilot 结果是：oracle recovery 18%（gate FAIL），heuristic 32%（CI 跨零）。从 failed pilot 直接跳到 \"motivate\" 在逻辑上不连贯。\n\nR1 和我在这个问题上的判断一致：论文应将 framing 从 \"motivate solution X\" 调整为 \"characterize phenomenon Y, which is a prerequisite for future solutions\"。这样既诚实又仍有贡献价值。\n\n---\n\n### 小问题回应\n\n**[AGREE] Table 2 中 Qwen s=0.15 $\\mathrm{II}_{\\textit{high}} = -0.000$**\n我也在小问题 M1 中指出了这个问题。这几乎确定是 numerical noise（bfloat16 精度下，PPL ratios 的微小偏差），但论文应在 footnote 或 text 中说明。\n\n**[AGREE] Figure 1 用 n=50 vs main results 用 n=496**\n我在小问题 M3 中也指出。Hero figure 应用 full-scale 数据，否则会让读者质疑为什么主图不用最好的数据。\n\n**[AGREE] §5.3 中 1.498 vs Table 2 中 1.514**\n我核实了具体数值：\n- Table 2（§5.2）：Random s=0.25, $\\widetilde{\\mathrm{II}}_{\\textit{low}} = 1.514$\n- §5.3 正文：\"$3.971$ vs.\\ $1.498$\"\n- Appendix C（appendix_moved.tex）：同样使用 \"$1.498$\"\n\n数值不一致（1.498 vs 1.514）。从 LaTeX 注释看，§5.3 引用 crossover_all_sparsity.csv，而 Table 2 引用 table2_n500_full.csv。两个 CSV 文件可能使用了略有不同的聚合方式。虽然差异很小（1.1%），但同一论文中对同一量的报告应一致。\n\n进一步发现：Qwen crossover 数值也有类似小不一致——§5.3/Appendix 报告 Qwen s=0.25 importance low 为 1.043，但 Table 2 为 1.053。同样量级的偏差。这暗示 crossover 分析可能使用了不同的 problem subset 或不同的聚合路径，需要作者澄清。\n\n**[AGREE] 3 个 bib 条目 OpenAlex 未找到**\n我的验证结果一致：defensivekv-iclr2026、hies-2025、phase-transition-compression-2026 未在 OpenAlex 中匹配。三者均有有效 arXiv URL。很可能是 OpenAlex 索引延迟，不是 fabricated references。\n\n---\n\n### 总结：与 Reviewer 1 的主要分歧和共识\n\n| 议题 | R1 | R2 | 一致性 |\n|------|-----|-----|--------|\n| G 指标不一致 (N1) | Critical | Agree, 补充 Abstract CI 拼接问题 | ✅ 一致 |\n| 单一 importance 方法 (N2) | Critical | Agree 定量层面; 定性方向可能 generalizable | ⚠️ 部分一致 |\n| 缺 accuracy (N3) | Critical | Agree, 补充 phase-accuracy 关系分析 | ✅ 一致 |\n| Cross-model 误导 (W1) | Warning | Agree | ✅ 一致 |\n| LLaMA n=49 (W2) | Warning | Agree; CI/Wilcoxon 解释合理但 n=49 原因缺失 | ✅ 一致 |\n| Bonferroni k=4 (W3) | Warning | **Rebut**: family 定义合理, BH-FDR 已验证 | ❌ 分歧 |\n| 43:1 outliers (W4) | Warning | Agree, 建议 outlier profiling | ✅ 一致 |\n| Pilot fail vs motivate (W5) | Warning | Agree, 应调整 framing | ✅ 一致 |\n\n**唯一分歧**在 W3（Bonferroni family 分组）：R1 认为 k=4 可能宽松，我认为 family 定义合理且 BH-FDR 已覆盖。这不影响任何核心结论。\n\n**两位 reviewer 共识**：最严重的三个问题是 (1) 缺少 downstream accuracy, (2) G 指标定义不一致, (3) generalizability 受限。这些是 author response 必须回应的核心问题。\n\n*Reviewer 2, 交叉回应完成。*",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-15T12:42:36.416597+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4334
}
```

</details>

---


### Assistant

_source line 476 · 2026-05-15T12:42:41.497197+00:00_

交叉回应已提交给 Director。

核心结论：与 Reviewer 1 在 7/8 个问题上达成共识，唯一分歧在 Bonferroni family 分组（W3）——我认为 k=4 的 family 定义合理，且 BH-FDR 已验证核心结论不受影响。两位 reviewer 一致认为最严重的三个问题是：缺少 downstream accuracy 验证、G 指标定义不一致、generalizability 受限（单基准+单规模）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

64 recorded events


### User

_source line 477 · 2026-05-15T13:41:46.854786+00:00_

[Round 8 审稿请求]:
## Round 8 审稿任务 — Reviewer 2

### 你的侧重：新颖性 + 相关工作完整性 + 写作质量

### Venue 信息
- **EMNLP 2026 Main Conference**（通过 ACL Rolling Review 提交）
- **ARR deadline**: 2026-05-25
- **格式**: ACL style, 长文 8 页正文, double-blind
- **Limitations section**: 必须有，不计入页数
- **匿名规则**: double-blind，禁止透露作者身份

### 论文路径
`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`
（多文件结构：abstract.tex, introduction.tex, related_work.tex, background.tex, methodology.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex, appendix_moved.tex, appendix_disc_analysis.tex, appendix_robustness.tex）

### 论文概要
研究 compound sparsity（head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。自我定位为 diagnostic study——不提出 mitigation method，而是量化一个 previously unknown interaction effect。核心发现：(1) importance-based eviction 的 phase-dependent severity gradient (G=7.5x-79.8x)；(2) DeepSeek 上 strategy ranking crossover（model-dependent）；(3) discrimination collapse 作为 correlational mechanism。

### 审查重点
请严格审查以下方面：

1. **Novelty 评估**
   - "Phase-dependent compound severity" 这个发现的 novelty 程度如何？
   - 是否只是对 ThinKV (phase-aware) + HIES (score collapse) + sparse-frontier (strategy non-dominance) 已知结果的组合？Introduction 中 "linear combination of these insights would predict..." 的论证是否令人信服？
   - 作为纯 diagnostic study（无 mitigation method），contribution 是否足够支撑 EMNLP main conference 长文？
   - Pilot mitigation 实验 (18% oracle recovery, gate FAIL) 的价值——是否反而削弱了论文的贡献？

2. **Related Work 覆盖度**
   - compound compression 相关工作是否遗漏重要文献？
   - KV cache eviction 方向的 2025-2026 最新进展是否全面覆盖？
   - phase-aware inference 的文献是否有遗漏？
   - 请特别关注 2026 年的新工作：是否有与本文 claim 直接冲突或高度相关但未引用的工作？

3. **写作质量与清晰度**
   - Abstract 是否准确反映论文内容？是否有过度宣称？
   - Introduction 的 motivation 链是否逻辑通顺？
   - 论文自我定位为 "diagnostic study" 是否一致贯穿全文，还是有时滑向 method claim？
   - 符号定义的一致性和清晰度
   - 数字引用的准确性（text vs table 是否一致）
   - 论文的整体 narrative arc 是否清晰？

4. **Framing 问题**
   - "Severity gradient" 从 7.5x 到 79.8x 的 framing——这些数字的 practical significance 如何？
   - Crossover 被放在什么位置？鉴于它只在 DeepSeek 上出现，强调程度是否合适？
   - LLaMA cross-architecture 证据的 framing 是否恰当（"preliminary"/"suggestive" 的用词）？
   - "Discrimination collapse" 的命名——是否合理？是否容易与其他领域的概念混淆？

5. **Presentation 问题**
   - 图表是否清晰？Figure 1 是否有效传达核心信息？
   - 正文 vs 附录的内容分配是否合理？
   - 论文的结构组织是否适合 EMNLP 读者？

请按 EMNLP 标准给出完整审稿报告：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + confidence)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-15T13:41:53.510645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-15T13:41:54.365796+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-15T13:41:54.466824+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-15T13:41:54.518125+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-15T13:41:59.648558+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 483 · 2026-05-15T13:42:00.000600+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-15T13:42:00.453191+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-15T13:42:00.604543+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-15T13:42:00.605017+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-15T13:42:10.504396+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

I've found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

Reviewers should follow this workflow: (1) read the paper and get a first impression, (2) search for related work, not deliberately trying to find that particular submission.

If you are qualified to r
…[truncated 2238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10855
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-15T13:42:14.474649+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
  "description": "Find all tex and bib files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
    "description": "Find all tex and bib files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-15T13:42:15.027673+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifa
…[truncated 31 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-15T13:42:16.333981+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all rating dimensions, their scales (1-5, 1-6, etc.), and the exact descriptions for each score level. I need every field a reviewer must fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all rating dimensions, their scales (1-5, 1-6, etc.), and the exact descriptions for each score level. I need every field a reviewer must fill out."
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-15T13:42:24.710542+00:00_

# ACL Rolling Review Form - Complete Rating Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully..."
- 4: "Quite sure. I tried to check the important points carefully..."
- 3: "Pretty sure, but there's a chance I missed something..."
- 2: "Willing to defend my evaluation, but it is fairly likely..."
- 1: "Not my area, or paper is very hard to understand..."

## 2. **Soundness** (1-5 scale with half-point increments)
- 5: "Excellent: This study is one of the most thorough I have seen..."
- 4: "Strong: This study provides sufficient support for all claims..."
- 3: "Acceptable: This study provides sufficient support for its main claims..."
- 2: "Poor: Some of the main claims are not sufficiently supported..."
- 1: "Major Issues: This study is not yet sufficiently thorough..."

## 3. **Excitement** (1-5 scale with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others..."
- 4: "Exciting: I would mention this paper to others..."
- 3: "Interesting: I might mention some points..."
- 2: "Potentially Interesting: this paper does not resonate with me..."
- 1: "Not Exciting: this paper does not resonate with me..."

## 4. **Overall Assessment** (1-5 scale with half-point increments)
- 5: Consider for Award (top 2.5% papers)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## 5. **Reproducibility** (1-5 scale)
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty
- 2: Hard to reproduce
- 1: Cannot reproduce

## 6. **Datasets** (1-5 scale)
- 5: Enabling
- 4: Useful
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable datasets

## 7. **Software** (1-5 scale)
- 5: Enabling
- 4: Useful
- 3: Potentially useful
- 2: Documentary value only
- 1: 
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8376
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-15T13:42:28.330697+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-15T13:42:28.783260+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-15T13:42:28.783894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-15T13:42:29.254607+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios ($G$) from $7.5{\times}$ ($s{=}0.15$, 95\% CI $[4.1, 11.4]$) to $79.8{\times}$ ($s{=}0.30$, 95\% CI $[63.3, 96.5]$) across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We present discrimination collapse---head pruning flattening cumulative importance scores---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
9	These findings establish the phase-dependent nature of compound severity as a diagnostic foundation for future phase-aware 
…[truncated 44 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 470
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-15T13:42:29.255168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-15T13:42:29.713214+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 4062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-15T13:42:29.713804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-15T13:42:30.667943+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-15T13:42:30.668485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-15T13:42:31.170719+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\ref{app:mu
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-15T13:42:31.171164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-15T13:42:31.623357+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and p
…[truncated 2007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-15T13:42:31.624838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-15T13:42:32.077792+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n
…[truncated 10806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-15T13:42:32.078474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-15T13:42:32.982911+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	We present discrimination collapse as a \emph{correlational diagnostic} rather than a complete causal explanation. The consistent Gini decrease across all conditions provides a necessary background---aggregate attention concentration drops uniformly under head pruning regardless of eviction strategy (importance $\Delta\mathrm{Gini}$: $-0.030$ to $-0.081$; random $\Delta\mathrm{Gini}$: $-0.031$ to $-0.071$; ${<}10\%$ difference). However, severity diverges by $15$--$17{\times}$ between strategies despite near-identical Gini changes, indicating that concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity}: importance-based pruning systematically removes high-attention-score heads, disrupting the attention pattern structure that KV eviction relies on, while random pruning preserves more structural diversity. The quantitative gap between score-level changes ($6$--$16\%$ relative Gini reduction from a DeepSeek baseline of $\widetilde{\mathrm{Gini}} \approx 0.50$; Qwen baseline $\approx 0.57$) and outcome-level amplification ($G{=}7.5$--$79.8{\times}$) indicates additional nonlinear factors (e.g., cascading effects across layers) that warrant dedicated investigation.  % exp_id: c4_entropy; DS baseline Gini 0.496, QW 0.571; imp ΔGini -0.029 to -0.082, rand -0.031 to -0.071
5	
6	\subsection{Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Critically, random eviction shows near-identic
…[truncated 3082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-15T13:42:32.983477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-15T13:42:33.486238+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}7.5$--$79.8{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover on DeepSeek---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.021$ vs.\ $1.113$) and underperforms in low-sparsity phases ($3.971$ vs.\ $1.514$)---cannot be derived from single-axis entropy reasoning. % exp_id: crossover_all_sparsity.csv; DS s025 n=496 The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. We expect qualitatively similar behavior for other attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), as they share the property that head pruning alters the score distribution feeding into eviction decisions; however, quantitative magnitudes may differ given implementation-specific scoring mechanisms.
9	
10	\paragraph{Characterization as diagnostic signal.}
11	The primary value of the phase-dependent severity gradient is diagnostic ra
…[truncated 2928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-15T13:42:33.537057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-15T13:42:33.989506+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $7.5{\times}$ to $79.8{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover on DeepSeek at $s{=}0.25$---where importance-based eviction reverses ranking across phases ($2.6{\times}$ reversal)---demonstrates that no single strategy dominates uniformly; Qwen does not exhibit this crossover, indicating model dependence. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational diagnostic supported by both Qwen2-based models, with structural specificity of importance-based pruning as the key differentiator from random eviction---despite near-identical Gini drops ($<10\%$ difference), severity diverges by $15$--$17{\times}$.
5	These findings establish the phase-dependent nature of compound severity as a prerequisite and diagnostic foundation for future phase-aware mitigation strategies. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-15T13:42:33.989995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-15T13:42:34.442266+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggress
…[truncated 1882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-15T13:42:34.442901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-15T13:42:34.895285+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-15T13:42:34.946197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-15T13:42:35.851495+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.6)
5	% - Cross-architecture analysis with power analysis (from results §5.5)
6	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
7	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
8	
9	\section{Phase-Strategy Crossover Details}
10	\label{app:crossover-details}
11	
12	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). % exp_id: n500_unified_final, table2_n500_full.csv
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
17	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ hig
…[truncated 18930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-15T13:42:35.852006+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-15T13:42:36.354713+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$39{\times}$ weaker than importance-based, confirming that the dominant amplification is strategy-specific. % exp_id: n500_unified_final; DS rand s025 0.257 p=0.006, s030 0.510 p=0.006; QW rand s025 0.393, s030 0.913
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy s
…[truncated 4934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-15T13:42:36.355100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-15T13:42:36.656818+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-model random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-model Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-model random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings. % exp_id: n500_unified_final; source: supplementary_stats.json bh_fdr_correction
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based c
…[truncated 5777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-15T13:42:36.707662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-15T13:42:36.758735+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 12981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-15T13:42:42.890936+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound sparsity head pruning KV cache eviction interaction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound sparsity head pruning KV cache eviction interaction 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-15T13:42:43.343588+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "phase-aware KV cache compression reasoning models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "phase-aware KV cache compression reasoning models 2026"
  }
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-15T13:42:44.766654+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KV cache eviction mathematical reasoning LLM 2026 new methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KV cache eviction mathematical reasoning LLM 2026 new methods"
  }
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-15T13:42:46.329760+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-15T13:42:50.997837+00:00_

Web search results for query: "phase-aware KV cache compression reasoning models 2026"

Links: [{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.24133v1"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2jwAjomEDB"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2603.11504"},{"title":"[2505.24133] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/abs/2505.24133"},{"title":"[Feature Request] Per-phase KV cache quantization for reasoning models (DeepSeek-R1) · Issue #21679 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/21679"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"}]

Based on the search results, here's what I found about phase-aware KV cache compression for reasoning models in 2026:

## Key Research Developments

Phase-aware approaches propose different quantization strategies for the "thinking" phase versus the "answer" phase of
…[truncated 1528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7654
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-15T13:42:52.104051+00:00_

Web search results for query: "compound sparsity head pruning KV cache eviction interaction 2025 2026"

Links: [{"title":"KV Cache Pruning in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-pruning"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"},{"title":"THINNER KEY CACHE BY QUERY-DRIVEN PRUNING","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://aclanthology.org/2026.findings-eacl.168.pdf"},{"title":"SPARK: Query-Aware Unstructured Sparsity with","url":"https://arxiv.org/pdf/2508.15212"},{"title":"Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models","url":"https://arxiv.org/html/2602.02197v1"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/html/2508.15212v1"}]

I've found comprehensive research results on the topic of compound sparsity, head pruning, KV cache eviction, and their interactions in recent 2025-2026 literature. Here are the key findings:

## Recent Methods and Techniques

THINK (Thinner Key Cache by Query-Driven Pruning) pioneers investigation into sparsity within KV cache channels, discovering that the activated key cache is sparse for a given query, enabling channel pruning of
…[truncated 1656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9213
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-15T13:42:53.963658+00:00_

Web search results for query: "KV cache eviction mathematical reasoning LLM 2026 new methods"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"[2605.07234] Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/abs/2605.07234"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203v1"},{"title":"[2601.17668] Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://arxiv.org/abs/2601.17668"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://www.arxiv.org/pdf/2601.17668"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"Neural Garbage Collection: Efficient LM Memory Management","url":"https://www.emergentmind.com/papers/2604.18002"}]

Based on the search results, here's what the latest research shows about KV cache eviction for mathematical reasoning LLMs in 2026:

## New Methods and Approaches

**Reasoning-Aware Compression:** The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).


…[truncated 1522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9197
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-15T13:43:27.637396+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 35, \"total_citations\": 69, \"unique_cited_keys\": 35, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 25, \"online_not_found\": 5, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"doing-more-with-less-2026\", \"type\": \"article\", \"title\": \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\", \"authors\": \"Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.25098\"}, {\"key\": \"efron-1993\", \"ty
…[truncated 29121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 41307
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-15T13:43:32.492562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ForesightKV KV cache eviction reasoning models long-term contribution 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ForesightKV KV cache eviction reasoning models long-term contribution 2026"
  }
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-15T13:43:33.447451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"compound compression\" \"joint pruning\" quantization sparsity LLM interaction 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"compound compression\" \"joint pruning\" quantization sparsity LLM interaction 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-15T13:43:34.050763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "THINK thinner key cache query-driven pruning ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "THINK thinner key cache query-driven pruning ICLR 2025"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-15T13:43:38.982248+00:00_

Web search results for query: "ForesightKV KV cache eviction reasoning models long-term contribution 2026"

Links: [{"title":"[2602.03203] ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/abs/2602.03203"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | OpenReview","url":"https://openreview.net/forum?id=k5h29Qv7GN"},{"title":"FORESIGHTKV: OPTIMIZING KV CACHE EVICTION","url":"https://openreview.net/pdf/6957849ec917fb6c85af208e505300924f9aa93b.pdf"},{"title":"Paper page - LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://huggingface.co/papers/2603.10899"},{"title":"PaFu-KV: Past & Future-Informed Cache Policy","url":"https://www.emergentmind.com/topics/past-and-future-informed-kv-cache-policy-pafu-kv"},{"title":"Neural Garbage Collection: Efficient LM Memory Management","url":"https://www.emergentmind.com/papers/2604.18002"},{"title":"KV Cache Learning","url":"https://www.emergentmind.com/topics/kv-cache-learning"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899v1"}]

I found comprehensive information about ForesightKV. Here's what the search results reveal:

## Overview

ForesightKV is a training-based KV cache eviction framework that learns to predict which KV pairs to evict during long-text generations. While large language models have shown remarkable reasoning abilities by producing long reasoning traces, the key-value (KV) cache expands linearly as sequence length grows, incurring
…[truncated 1095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6489
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-15T13:43:41.141975+00:00_

Web search results for query: "THINK thinner key cache query-driven pruning ICLR 2025"

Links: [{"title":"THINNER KEY CACHE BY QUERY-DRIVEN PRUNING","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf"},{"title":"ThinK: Thinner Key Cache by Query-Driven Pruning | OpenReview","url":"https://openreview.net/forum?id=n0OtGl6VGb"},{"title":"GitHub - SalesforceAIResearch/ThinK: ThinK: Thinner Key Cache by Query-Driven Pruning","url":"https://github.com/SalesforceAIResearch/ThinK"},{"title":"[2407.21018] ThinK: Thinner Key Cache by Query-Driven Pruning","url":"https://arxiv.org/abs/2407.21018"},{"title":"[Literature Review] ThinK: Thinner Key Cache by Query-Driven Pruning","url":"https://www.themoonlight.io/en/review/think-thinner-key-cache-by-query-driven-pruning"},{"title":"[2407.21018v3] ThinK: Thinner Key Cache by Query-Driven Pruning","url":"https://arxiv.org/abs/2407.21018v3"},{"title":"ThinK: Thinner Key Cache by Query-Driven Pruning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/think-thinner-key-cache-by-query-driven"},{"title":"Paper page - ThinK: Thinner Key Cache by Query-Driven Pruning","url":"https://huggingface.co/papers/2407.21018"},{"title":"[2407.21018v2] ThinK: Thinner Key Cache by Query-Driven Pruning","url":"https://arxiv.org/abs/2407.21018v2"},{"title":"ThinK: Thinner Key Cache by Query-Driven Pruning - Paper Detail","url":"https://deeplearn.org/arxiv/513799/think:-thinner-key-cache-by-query-driven-pruning"}]

I found relevant results for your search. Here's what I found about THINK/ThinK:

## Overview

THINK is a novel query-dependent KV cache channel pruning method to reduce the memory usage of LLMs during inference. Published on January 22, 2025, this work was accepted as a spotlight paper at ICLR 2025.

## Problem and Approach

The paper identifies substantial redundancy in the channel dimension of the KV cache, as indicated by an uneven magnitude distribut
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7091
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-15T13:43:41.242970+00:00_

Web search results for query: ""compound compression" "joint pruning" quantization sparsity LLM interaction 2025 2026 arxiv"

Links: [{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.14569"},{"title":"[2302.07612] Towards Optimal Compression: Joint Pruning and Quantization","url":"https://ar5iv.labs.arxiv.org/html/2302.07612"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.18426"},{"title":"Semantic Retention and Extreme Compression in LLMs: Can We Have Both?","url":"https://arxiv.org/html/2505.07289v1"},{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"Large Language Model Compression with Global Rank and Sparsity Optimization","url":"https://arxiv.org/html/2505.03801"},{"title":"Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression","url":"https://arxiv.org/html/2502.16638v1"},{"title":"Compressing large language models by joint sparsification and quantization | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692743"},{"title":"[2603.18426] Prune-then-Quantize or Quantize-then-Prune? Understanding the Impact of Compression Order in Joint Model Compression","url":"https://arxiv.org/abs/2603.18426"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"}]

I've completed the web search for your query about compound compression, joint pruning, quantization, sparsity, and LLM interactions. Here are the key findings from 2025-2026 arxiv research:

## Key Research Papers Found:

**1. Joint Compression Methods:**
Joint model compression has emerged as a powerful strategy to achieve higher efficiency by combining multiple methods such as pruning and quantization, w
…[truncated 1648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7795
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-15T13:47:40.782207+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 8 审稿报告（新颖性 + 相关工作 + 写作质量）\n\n### 总体评分\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 方法论扎实的实证诊断研究，但核心发现的定性方向可从已有工作推导，定量贡献依赖 near-zero denominator 放大的 G 指标，pilot mitigation 失败反而削弱贡献。\n\n### ARR 维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法论扎实，但 \"3–39×\" 数字声明与数据不一致；G 指标受近零分母影响 |\n| Excitement | 2.5/5 | \"importance-based eviction 在 attention 分散的 phase 表现更差\"定性上可预测；缺乏可操作产出 |\n| Reproducibility | 4/5 | 实验设置详尽，承诺 release code，统计规范 |\n| Confidence | 4/5 | 熟悉 KV cache compression、attention head pruning 和 reasoning model 推理文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足：核心发现定性可预测，\"linear combination\" 论证为稻草人\n\n- 位置：Section 1 (Introduction), paragraph 3\n- 论文声称 \"a linear combination of these insights would predict that compound degradation either (i) uniformly amplifies, or (ii) follows the dominant single-axis pattern\"，然后用实际观察到的 severity gradient 反驳。但这构建了一个过弱的 null hypothesis——没有人会预期两个非线性交互的压缩轴产生 \"linear combination\"。ThinKV 已证明 attention 分散的 phase 对 eviction 更敏感；HIES 已证明重度剪枝下 importance score 区分力崩塌；compound setting 中这两效应叠加产生 phase-modulated severity 定性上可预期。论文真正贡献在于量化（G=7.5×–79.8×），但 G 指标因 II_high 接近零（Table 2: 0.003–0.038）而被人为放大。\n- 建议：(a) 改进 novelty argument，聚焦 crossover 和 dose-response 的不可预测性；(b) 在 headline claims 中同时报告 Δ（绝对差）和 G（比率）；(c) 明确讨论 G 的 near-zero denominator 放大效应。\n\n**N2** [critical] Pilot mitigation 实验削弱而非增强贡献\n\n- 位置：Section 7, paragraph 3 (pilot experiment)\n- Oracle phase-aware budget reallocation 仅恢复 18%（预注册 30% gate FAIL），heuristic 32% 但 CI span zero。论文 pitch \"severity gradient provides a natural signal for allocating compression budgets\"，但 pilot 直接反驳此声明。\n- 建议：要么移除 pilot（纯诊断论文无需 mitigation 尝试），要么深入分析失败原因并移至 Appendix。\n\n**N3** [critical] \"3–39×\" / \"15–39×\" 数字声明与数据不一致\n\n- 位置：Abstract, Section 5.1, Contribution item 1\n- 在 random 统计显著的条件（s≥0.25），实际比率为：DS 15.3–16.6×, QW 2.7–3.5×，跨模型范围 **2.7–17×**，非 \"3–39×\"。39× (≈0.39/0.01) 来自 DS s=0.15 但该条件 random Δ 非显著（CI spans zero）。将非显著条件比率纳入 \"where significant\" 声明是数字不一致。\n- 建议：修正为 \"3–17×\" 或准确区间。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Crossover 过度强调（仅 DeepSeek 出现，Qwen 不存在，model-dependent）\n\n**W2** [warning] LLaMA 跨架构证据过弱（n=49，~1/40 效应量，仅 1/4 sparsity 显著），建议正文压缩\n\n**W3** [warning] \"Discrimination collapse\" 命名可能与 ML 其他 collapse 概念混淆，建议改用 \"importance score flattening\"\n\n**W4** [warning] 缺少高相关性近期文献：ForesightKV (arXiv 2602.03203), ThinK (ICLR 2025), \"Prune-then-Quantize or Quantize-then-Prune?\" (ICLR 2026)\n\n**W5** [warning] 仅 perplexity 度量；Section 5.7 answer-region 分析（93.2% answer tokens 在 high-sparsity phase）暗示 practical significance 可能远低于 G 指标所示\n\n---\n\n### 小问题\n- Table 2 footnote: negative II 应报告为 ≈0\n- LaTeX 源码残留 `% exp_id:` 注释\n- LKV reference author = \"Anonymous\"\n- Table 3 caption 中 \"paired median difference\" vs \"difference of medians\" 概念需更清晰\n\n### 主要优势\n1. 统计方法论堪称典范（Bonferroni + BH-FDR、置换检验、JT dose-response、power analysis、winsorization）\n2. 多维度 robustness 验证（segmentation 粒度、min_phase_length、outlier、multiplicative null）\n3. Cross-model replication 增强可靠性（不同训练范式）\n4. Diagnostic study 自我定位一致，hedging 得当\n5. Random eviction 对照组设计精巧\n\n### 缺失引用\n| 论文 | 相关性 |\n|------|--------|\n| ForesightKV (2602.03203) | Reasoning-specific KV eviction with learned long-term importance |\n| ThinK (ICLR 2025) | Channel-level KV pruning compound compression |\n| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis |\n\n### Overall Assessment\nWeak Reject → Borderline Findings。实验执行质量高但核心发现新颖性有限。建议 (a) 修正数字不一致，(b) 重新 frame G 指标，(c) 减少 crossover/LLaMA 强调，(d) 补充缺失引用。适合 Findings track。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 8 审稿报告（新颖性 + 相关工作 + 写作质量）\n\n### 总体评分\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 方法论扎实的实证诊断研究，但核心发现的定性方向可从已有工作推导，定量贡献依赖 near-zero denominator 放大的 G 指标，pilot mitigation 失败反而削弱贡献。\n\n### ARR 维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法论扎实，但 \"3–39×\" 数字声明与数据不一致；G 指标受近零分母影响 |\n| Excitement | 2.5/5 | \"importance-based eviction 在 attention 分散的 phase 表现更差\"定性上可预测；缺乏可操作产出 |\n| Reproducibility | 4/5 | 实验设置详尽，承诺 release code，统计规范 |\n| Confidence | 4/5 | 熟悉 KV cache compression、attention head pruning 和 reasoning model 推理文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足：核心发现定性可预测，\"linear combination\" 论证为稻草人\n\n- 位置：Section 1 (Introduction), paragraph 3\n- 论文声称 \"a linear combination of these insights would predict that compound degradation either (i) uniformly amplifies, or (ii) follows the dominant single-axis pattern\"，然后用实际观察到的 severity gradient 反驳。但这构建了一个过弱的 null hypothesis——没有人会预期两个非线性交互的压缩轴产生 \"linear combination\"。ThinKV 已证明 attention 分散的 phase 对 eviction 更敏感；HIES 已证明重度剪枝下 importance score 区分力崩塌；compound setting 中这两效应叠加产生 phase-modulated severity 定性上可预期。论文真正贡献在于量化（G=7.5×–79.8×），但 G 指标因 II_high 接近零（Table 2: 0.003–0.038）而被人为放大。\n- 建议：(a) 改进 novelty argument，聚焦 crossover 和 dose-response 的不可预测性；(b) 在 headline claims 中同时报告 Δ（绝对差）和 G（比率）；(c) 明确讨论 G 的 near-zero denominator 放大效应。\n\n**N2** [critical] Pilot mitigation 实验削弱而非增强贡献\n\n- 位置：Section 7, paragraph 3 (pilot experiment)\n- Oracle phase-aware budget reallocation 仅恢复 18%（预注册 30% gate FAIL），heuristic 32% 但 CI span zero。论文 pitch \"severity gradient provides a natural signal for allocating compression budgets\"，但 pilot 直接反驳此声明。\n- 建议：要么移除 pilot（纯诊断论文无需 mitigation 尝试），要么深入分析失败原因并移至 Appendix。\n\n**N3** [critical] \"3–39×\" / \"15–39×\" 数字声明与数据不一致\n\n- 位置：Abstract, Section 5.1, Contribution item 1\n- 在 random 统计显著的条件（s≥0.25），实际比率为：DS 15.3–16.6×, QW 2.7–3.5×，跨模型范围 **2.7–17×**，非 \"3–39×\"。39× (≈0.39/0.01) 来自 DS s=0.15 但该条件 random Δ 非显著（CI spans zero）。将非显著条件比率纳入 \"where significant\" 声明是数字不一致。\n- 建议：修正为 \"3–17×\" 或准确区间。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Crossover 过度强调（仅 DeepSeek 出现，Qwen 不存在，model-dependent）\n\n**W2** [warning] LLaMA 跨架构证据过弱（n=49，~1/40 效应量，仅 1/4 sparsity 显著），建议正文压缩\n\n**W3** [warning] \"Discrimination collapse\" 命名可能与 ML 其他 collapse 概念混淆，建议改用 \"importance score flattening\"\n\n**W4** [warning] 缺少高相关性近期文献：ForesightKV (arXiv 2602.03203), ThinK (ICLR 2025), \"Prune-then-Quantize or Quantize-then-Prune?\" (ICLR 2026)\n\n**W5** [warning] 仅 perplexity 度量；Section 5.7 answer-region 分析（93.2% answer tokens 在 high-sparsity phase）暗示 practical significance 可能远低于 G 指标所示\n\n---\n\n### 小问题\n- Table 2 footnote: negative II 应报告为 ≈0\n- LaTeX 源码残留 `% exp_id:` 注释\n- LKV reference author = \"Anonymous\"\n- Table 3 caption 中 \"paired median difference\" vs \"difference of medians\" 概念需更清晰\n\n### 主要优势\n1. 统计方法论堪称典范（Bonferroni + BH-FDR、置换检验、JT dose-response、power analysis、winsorization）\n2. 多维度 robustness 验证（segmentation 粒度、min_phase_length、outlier、multiplicative null）\n3. Cross-model replication 增强可靠性（不同训练范式）\n4. Diagnostic study 自我定位一致，hedging 得当\n5. Random eviction 对照组设计精巧\n\n### 缺失引用\n| 论文 | 相关性 |\n|------|--------|\n| ForesightKV (2602.03203) | Reasoning-specific KV eviction with learned long-term importance |\n| ThinK (ICLR 2025) | Channel-level KV pruning compound compression |\n| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis |\n\n### Overall Assessment\nWeak Reject → Borderline Findings。实验执行质量高但核心发现新颖性有限。建议 (a) 修正数字不一致，(b) 重新 frame G 指标，(c) 减少 crossover/LLaMA 强调，(d) 补充缺失引用。适合 Findings track。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-15T13:47:44.866609+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4084
}
```

</details>

---


### Assistant

_source line 540 · 2026-05-15T13:47:53.363979+00:00_

审稿报告已提交给 Review Director。

核心结论：**2.5/5，Borderline Findings**。

三个 critical 问题：
1. **新颖性**——"compound severity is phase-dependent" 定性上可从 ThinKV + HIES 推导，"linear combination" 反驳论证是稻草人；G 指标因 near-zero denominator 被放大
2. **Pilot mitigation 失败**——oracle 仅恢复 18%（gate FAIL），反而削弱了 "diagnostic foundation for future mitigation" 的叙事
3. **数字不一致**——"3–39×" 声明混入了 random Δ 非显著条件的比率，实际应为 "3–17×"

五个 should-fix：crossover 过度强调（model-dependent）、LLaMA 证据太弱、"discrimination collapse" 命名易混淆、缺 ForesightKV/ThinK/Prune-then-Quantize 引用、纯 perplexity 评估且 answer shielding 暗示 practical significance 有限。

统计方法论和 robustness 验证是论文最大亮点，建议投 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

8 recorded events


### User

_source line 541 · 2026-05-15T13:54:49.239604+00:00_

[Round 8 审稿请求]:
## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

## Reviewer 1 — Round 8 审稿报告

**Overall**: 3/5 (Findings: could be accepted to Findings of the ACL)

### ARR 维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计框架严谨，但核心度量仅基于 PPL、单一基准，且 additive null 的论证不够充分 |
| Excitement | 3/5 | Phase-strategy interaction 和 crossover effect 有新意，但实际可操作性不清 |
| Reproducibility | 4/5 | 实验细节充分，承诺代码发布 |
| Confidence | 4/5 | 仔细阅读全文含全部 15 个 Appendix |

### Must-Fix 问题

**N1** [critical] Interaction Index 的 additive null 假设与论文自身论述存在内在矛盾
- 具体位置：Section 3, Eq. 1; Appendix B
- 问题：论文以"两个轴作用于不相交维度（structural vs. positional）"来正当化 additive null（II = r_c − r_a − r_k + 1）。但论文自身在 Section 3 明确指出 "head pruning alters the importance ranking used for eviction"，在 Section 6 详细分析 head pruning 如何通过 discrimination collapse 直接影响 KV eviction 的决策质量。这意味着两个压缩轴存在直接的因果耦合，并非"不相交"。Appendix B 的 multiplicative null 验证显示 G_mult ≈ 58–211（远高于 additive G = 7.5–79.8），两种 null 下的数值差异达 4–8×。
- 为什么影响接收：II 是论文所有定量结论的根基。如果 additive null 不合理，所有基于 II 的数字均失去可靠的解释基准。
- 建议：(1) 严格论证 additive null 的合理性；(2) 在主文本中并列报告两种 null 下的关键结果。

**N2** [critical] 单一基准测试 (MATH-500) 严重限制泛化性
- 具体位置：Section 4.1; Limitations
- 问题：论文所有定量结论仅基于 MATH-500 一个基准。论文标题中使用 "Mathematical Reasoning Models"（复数），暗示一般性。不同推理任务的 attention dynamics 可能截然不同。一个额外基准（哪怕是小规模）即可大幅增强可信度。

**N3** [critical] PPL 度量的 construct validity 问题：论文自身的 answer-region 分析反而削弱了核心叙事
- 具体位置：Section 5.7
- 问题：93.2% 的答案 token 落在 high-sparsity phase（G ≤ 1）；答案 token 的 PPL degradation 远低于推理痕迹 token。更准确的解读是：观察到的巨大 G 值集中在对最终答案影响最小的 phase 中。缺乏直接准确率测量使 "severity" 的实际含义悬而未决。
- 建议：(1) 在至少一个 sparsity level 上测量实际准确率变化；(2) 重新框定 severity gradient 的意义。

### Should-Fix 问题

**W1** [warning] "Cross-model replication" 实为同架构不同训练范式
- DeepSeek 和 Qwen 共享 Qwen2ForCausalLM，LLaMA (n=49) 效应量仅 ~1/40，暗示可能是 Qwen2 架构特有

**W2** [warning] Discrimination collapse 的解释力存在 order-of-magnitude 缺口
- Gini drop 差异 < 10% 对应 severity 差异 15–17×；entropy redistribution 仅 2/4 条件复现

**W3** [warning] Profiling subset (n=50) 与 full sample (n=496) 的 G 差异 3.5–9.2×
- 系统性下移未充分解释；对 LLaMA n=49 结果可靠性有启示

**W4** [warning] Phase segmentation 缺乏理论先验
- 纯数据驱动分割；attention sparsity 作为 phase proxy 的合理性未独立论证

**W5** [warning] Pilot mitigation experiment 未达预注册 gate，削弱实际应用叙事
- Oracle 仅恢复 18%（gate FAIL），质疑 severity gradient 作为 "natural signal" 的价值

**W6** [warning] Sparsity 范围窄 (s ∈ {0.15, 0.20, 0.25, 0.30})
- 仅 4 个数据点不足以可靠刻画 G(s) 的 functional form

### Questions for Authors
1. Additive vs. multiplicative null: 两种 null 下 G 差异 4–8×，作者如何论证读者应信赖 additive null？
2. Answer-region shielding: 93.2% 答案 token 在 G ≤ 1 phase，推理痕迹 PPL 退化会 cascade 到最终答案吗？
3. Profiling vs. full sample G discrepancy: n=50 G 比 n=496 G 高 3.5–9.2×，LLaMA n=49 是否同样高估？
4. Crossover model-dependence: 什么模型属性决定 crossover 是否出现？

### 引用检查
- 25/35 在线验证通过
- 5/35 未被索引（2025-2026 近期文献）
- 0 hallucinated references

### 小问题
- Abstract CI vs Table 2 CI 置信水平可能不同
- 正文可能超 8 页
- min_phase_length=10 缺乏直观动机
- Qwen mid-phase null rate 45.2% 限制三阶段分析完整性

### 主要优势
1. 统计方法论罕见严谨
2. 充分的稳健性检查体系
3. Crossover effect 新颖且反直觉
4. 诚实的 limitation 披露
5. 清晰的 diagnostic study 定位

### Missing References
- FlexGen (Sheng et al., 2023)
- PPL 与 accuracy 非线性关系的 formal analysis

### Overall Assessment
3/5，Findings level。增加额外基准 + 准确率数据可升至 main conference。

---

请逐条回应 Reviewer 1 的每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (1-4) 和小问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-15T13:55:28.584793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
  "offset": "34",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
    "offset": "34",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-15T13:55:29.036938+00:00_

34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-15T13:55:29.439012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": "22",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "offset": "22",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-15T13:55:29.590700+00:00_

22	\section{Profiling Subset Per-Phase Breakdown}
23	\label{app:profiling-subset}
24	
25	\begin{table*}[t]
26	\centering
27	\small
28	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). The main analysis ($n{=}496$) appears in Table~\ref{tab:main-results}. $G$ values in this table use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$), which differs from the primary per-problem definition in Eq.~\ref{eq:gradient}. At low sparsity ($s{=}0.15$), the two definitions diverge substantially ($7.5{\times}$ vs.\ $69{\times}$) because per-problem ratios are sensitive to near-zero $\mathrm{II}_{\textit{high}}$ values.}
29	\label{tab:profiling-subset}
30	\begin{tabular}{@{}llccccr@{}}
31	\toprule
32	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
33	\midrule
34	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
35	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
36	\addlinespace
37	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
38	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
39	\addlinespace
40	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
41	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
42	\addlinespace
43	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
44	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
45	\bottomrule
46	\end{tabular}
47	\end{table*}
48	
49	
50	\section{Cross-Model Replication Details}
51	\label{app:cross-model-details}
52	
53	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled compariso
…[truncated 1556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-15T13:57:25.898668+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条交叉回应\n\n### Must-Fix\n\n**[AGREE] R1-N1 (Additive null 矛盾)**: 论文自身的 causal coupling narrative（Section 3: \"head pruning alters the importance ranking\"; Section 6: discrimination collapse）与 \"disjoint dimensions\" 辩护矛盾。但严重性稍低于 R1 判断——两种 null 下定性结论一致（Appendix B），Δ 不受 null 选择影响。核心问题是 G 的 headline 数字缺乏可靠解释基准。建议主文并列报告两种 null 的 G，以 Δ 作为 primary metric。\n\n**[AGREE] R1-N2 (单一基准)**: 完全同意。MATH-500 一个基准不足以支撑标题中 \"Mathematical Reasoning Models\" 的泛化暗示。\n\n**[AGREE] R1-N3 (PPL construct validity)**: 强烈同意，与我的 W5 相互印证。93.2% answer tokens 在 G≈1 phase 意味着 severity gradient 的 practical significance 可能被系统性高估。至少需要一个 sparsity level 的 accuracy sanity check。\n\n### Should-Fix\n\n**[AGREE] R1-W1 (同架构)**: 同意应改称 \"cross-training-paradigm replication\"。LLaMA ~1/40 效应量暗示量化特征可能 Qwen2 特有。\n\n**[AGREE] R1-W2 (Discrimination collapse gap)**: 同意。Gini drop <10% vs severity 15-17× 的 order-of-magnitude gap 说明 discrimination collapse 是 necessary but not sufficient。\n\n**[REBUT] R1-W3 (Profiling vs full G discrepancy)**: R1 误读了数据。Table 5 (Appendix C) caption 已明确解释：profiling 表使用 **ratio-of-medians** 定义，main Table 2 使用 **median-of-per-problem-ratios** (Eq. 2)。3.5-9.2× 差异是统计量定义不同，不是 sample size artifact。当 II_high 接近零时两种定义自然大幅 diverge，论文 caption 已说明 \"At low sparsity (s=0.15), the two definitions diverge substantially (7.5× vs. 69×) because per-problem ratios are sensitive to near-zero II_high values.\" R1 的 Q3 (LLaMA 高估?) 也需重新审视——LLaMA 表 (Appendix D) 报告的是 Δ 和 CI 而非 G ratio。\n\n**[AGREE] R1-W4 (Phase segmentation 无理论先验)**: 部分同意。Tercile segmentation 纯数据驱动，但 robustness checks (Appendix G/H: quartile/quintile + mpl sensitivity) 部分缓解。问题更多是 interpretability 而非 validity。\n\n**[AGREE] R1-W5 (Pilot gate FAIL)**: 与我的 N2 一致。\n\n**[AGREE] R1-W6 (Sparsity 范围窄)**: 部分同意。4 点足以验证 monotonicity (JT test) 但不足以刻画 functional form。Scope limitation 而非 flaw。\n\n### Questions\n\n**Q1**: [AGREE] 应主文并列报告两种 null。\n**Q2**: [AGREE] 需 accuracy sanity check。\n**Q3**: [REBUT] G 定义不同所致，非 sample size artifact（见 W3 回应）。\n**Q4**: [AGREE] Crossover model-dependence 缺乏 explanatory hypothesis 是明显弱点。\n\n### 小问题\n- Abstract vs Table CI: [REBUT] 交叉核查一致。\n- 正文超页: [AGREE] 需确认。\n- mpl=10 动机: [AGREE] 应简述。\n- Qwen mid-phase null: [AGREE] 限制存在但处理合理。\n\n### Missing References\n- FlexGen: [REBUT] 是 offloading/scheduling 工作，非 compound sparsity interaction。\n- PPL-accuracy formal analysis: [AGREE] 应补充引用。\n\n### 两位 Reviewer 共识点\n1. PPL-only 度量 + answer-region shielding 削弱 practical significance（R1-N3 = R2-W5）\n2. Pilot mitigation gate FAIL 削弱 diagnostic value narrative（R1-W5 = R2-N2）\n3. Discrimination collapse 解释力不足（R1-W2 ≈ R2-W3 命名问题的深层原因）\n4. Crossover 的 model-dependence 需更好解释（R1-Q4 ≈ R2-W1）\n5. 统计方法论堪称典范（两位 Reviewer 均给 Soundness 3.5、Reproducibility 4）",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条交叉回应\n\n### Must-Fix\n\n**[AGREE] R1-N1 (Additive null 矛盾)**: 论文自身的 causal coupling narrative（Section 3: \"head pruning alters the importance ranking\"; Section 6: discrimination collapse）与 \"disjoint dimensions\" 辩护矛盾。但严重性稍低于 R1 判断——两种 null 下定性结论一致（Appendix B），Δ 不受 null 选择影响。核心问题是 G 的 headline 数字缺乏可靠解释基准。建议主文并列报告两种 null 的 G，以 Δ 作为 primary metric。\n\n**[AGREE] R1-N2 (单一基准)**: 完全同意。MATH-500 一个基准不足以支撑标题中 \"Mathematical Reasoning Models\" 的泛化暗示。\n\n**[AGREE] R1-N3 (PPL construct validity)**: 强烈同意，与我的 W5 相互印证。93.2% answer tokens 在 G≈1 phase 意味着 severity gradient 的 practical significance 可能被系统性高估。至少需要一个 sparsity level 的 accuracy sanity check。\n\n### Should-Fix\n\n**[AGREE] R1-W1 (同架构)**: 同意应改称 \"cross-training-paradigm replication\"。LLaMA ~1/40 效应量暗示量化特征可能 Qwen2 特有。\n\n**[AGREE] R1-W2 (Discrimination collapse gap)**: 同意。Gini drop <10% vs severity 15-17× 的 order-of-magnitude gap 说明 discrimination collapse 是 necessary but not sufficient。\n\n**[REBUT] R1-W3 (Profiling vs full G discrepancy)**: R1 误读了数据。Table 5 (Appendix C) caption 已明确解释：profiling 表使用 **ratio-of-medians** 定义，main Table 2 使用 **median-of-per-problem-ratios** (Eq. 2)。3.5-9.2× 差异是统计量定义不同，不是 sample size artifact。当 II_high 接近零时两种定义自然大幅 diverge，论文 caption 已说明 \"At low sparsity (s=0.15), the two definitions diverge substantially (7.5× vs. 69×) because per-problem ratios are sensitive to near-zero II_high values.\" R1 的 Q3 (LLaMA 高估?) 也需重新审视——LLaMA 表 (Appendix D) 报告的是 Δ 和 CI 而非 G ratio。\n\n**[AGREE] R1-W4 (Phase segmentation 无理论先验)**: 部分同意。Tercile segmentation 纯数据驱动，但 robustness checks (Appendix G/H: quartile/quintile + mpl sensitivity) 部分缓解。问题更多是 interpretability 而非 validity。\n\n**[AGREE] R1-W5 (Pilot gate FAIL)**: 与我的 N2 一致。\n\n**[AGREE] R1-W6 (Sparsity 范围窄)**: 部分同意。4 点足以验证 monotonicity (JT test) 但不足以刻画 functional form。Scope limitation 而非 flaw。\n\n### Questions\n\n**Q1**: [AGREE] 应主文并列报告两种 null。\n**Q2**: [AGREE] 需 accuracy sanity check。\n**Q3**: [REBUT] G 定义不同所致，非 sample size artifact（见 W3 回应）。\n**Q4**: [AGREE] Crossover model-dependence 缺乏 explanatory hypothesis 是明显弱点。\n\n### 小问题\n- Abstract vs Table CI: [REBUT] 交叉核查一致。\n- 正文超页: [AGREE] 需确认。\n- mpl=10 动机: [AGREE] 应简述。\n- Qwen mid-phase null: [AGREE] 限制存在但处理合理。\n\n### Missing References\n- FlexGen: [REBUT] 是 offloading/scheduling 工作，非 compound sparsity interaction。\n- PPL-accuracy formal analysis: [AGREE] 应补充引用。\n\n### 两位 Reviewer 共识点\n1. PPL-only 度量 + answer-region shielding 削弱 practical significance（R1-N3 = R2-W5）\n2. Pilot mitigation gate FAIL 削弱 diagnostic value narrative（R1-W5 = R2-N2）\n3. Discrimination collapse 解释力不足（R1-W2 ≈ R2-W3 命名问题的深层原因）\n4. Crossover 的 model-dependence 需更好解释（R1-Q4 ≈ R2-W1）\n5. 统计方法论堪称典范（两位 Reviewer 均给 Soundness 3.5、Reproducibility 4）",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-15T13:57:29.814273+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 548 · 2026-05-15T13:57:36.169552+00:00_

交叉回应已发送给 Review Director。

总结：对 R1 的 17 个具体观点，我给出 **12 个 [AGREE]**、**3 个 [REBUT]**、**2 个部分同意**。

核心分歧仅在 **W3（profiling vs full G discrepancy）**——R1 误读为 sample size artifact，实际是 G 统计量定义不同（ratio-of-medians vs median-of-ratios），Table 5 caption 已解释。以及 **FlexGen** 引用的相关性。

两位 Reviewer 的主要共识：PPL-only 度量 + answer shielding 削弱 practical significance、pilot mitigation gate FAIL、discrimination collapse 解释力 gap、crossover model-dependence 缺乏 hypothesis。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

50 recorded events


### User

_source line 549 · 2026-05-15T18:48:21.340666+00:00_

[Round 1 审稿请求]:
你负责 **新颖性 + Related Work + 格式** 方向的审稿。

**投稿信息：**
- 论文路径：`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, background.tex, methodology.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex, appendix_moved.tex, appendix_disc_analysis.tex, appendix_robustness.tex, references.bib）
- Venue：EMNLP 2026 Main Conference（ARR May 2026 cycle）
- Deadline：2026-05-25
- 格式：Long paper ≤ 8页正文，ACL 模板，double-blind
- Limitations section 必须有（不计入页数），否则 desk reject
- Double-blind：不可有作者自我引用暴露身份

**你的审查侧重：**

1. **Novelty 论证结构**
   - 论文定位为 "diagnostic study"，声称贡献是量化一个 previously unknown interaction effect。但 Introduction 承认 HIES 已发现 score collapse，ThinKV 已做 phase-aware eviction，sparse-frontier 已报告 strategy non-dominance——那么真正的 novelty 在哪？
   - 论文的 novelty 论证现在围绕 (a) strictly monotonic dose-response (JT z=33.7) 和 (b) strategy ranking crossover 展开。这两个 quantitative patterns 是否构成足够的 novelty 支撑 EMNLP long paper？
   - "Diagnostic study" 在 EMNLP 的接受率如何？是否需要更强的 actionable insight 或 method contribution？

2. **Related Work 覆盖度与准确性**
   - 逐一检查所有 references.bib 中的引用：venue、year、author 信息是否准确
   - 是否有重要的 missing references？特别关注：
     - 2025-2026 年 compound compression 新进展
     - Phase-aware reasoning 相关工作
     - 其他 importance score collapse / degeneration 现象的文献
   - LKV 引用——之前标记为 "Anonymous"，现在是否修复？

3. **Framing 合理性**
   - 标题 "Mathematical Reasoning Models" 用复数——实际测试了 2 个 Qwen2 架构模型 + 1 个 preliminary LLaMA。这个标题是否过度泛化？
   - "Cross-training-paradigm replication on same architecture"——DeepSeek 和 Qwen 共享 Qwen2ForCausalLM，论文将其定位为 "controlled comparison"。这个 framing 是否恰当？它究竟控制了什么变量？
   - Discussion 中 "could inform phase-aware budget allocation" + pilot 只恢复了 18%——diagnostic study 声称的实用价值是否被过度暗示？
   - Conclusion 中 "extending to code/science reasoning" 作为 future work——如果连 GSM8K（同属数学推理）都显示策略特异性形态不同，跨领域泛化的承诺是否过于乐观？

4. **写作质量**
   - Abstract 信息密度极高（含多个 CI、p-value、具体数值）——对审稿人和读者是否友好？是否应更多留空间给 high-level insight？
   - 论文是否存在内部数值不一致？（例如不同 section 对同一指标的引用是否一致）
   - 术语一致性：检查 "importance discrimination collapse" / "score discrimination collapse" / "importance discrimination flattening" 等变体是否统一
   - 是否残留内部追踪注释（如 `% exp_id:` 类 LaTeX 注释）？

5. **格式合规性（EMNLP/ARR 要求）**
   - ACL 模板正确使用？（`\usepackage[review]{acl}` ✓ 已确认）
   - 正文是否控制在 8 页以内？（需要估算：Section 1-8 + References + Limitations 的分布）
   - 匿名性：检查是否有 self-citation 暴露身份（如 "our previous work [XX]"、GitHub 链接、机构名称等）
   - Appendix 是否在 References 之后？（main.tex 中 appendix 在 bibliography 之后 ✓）
   - Acknowledgments 是否被省略？（double-blind 要求 ✓）
   - 引用格式是否一致？（natbib/\cite vs \citet vs \citep 混用？）

6. **Limitations section 评估**
   - 是否涵盖所有关键限制（scale, architecture, task, mechanism, metric）？
   - 是否有遗漏的重要限制？
   - 讨论深度是否充分？

请按以下格式输出审稿结果：
```
## Summary (2-3句)
## Strengths (逐条，S1/S2/...)
## Weaknesses (逐条，W1/W2/...，按 severity 排序：Must-Fix > Should-Fix > Minor)
## Questions (逐条，Q1/Q2/...)
## Missing References (如有)
## Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-15T18:48:30.235700+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-15T18:48:30.292683+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 56
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-15T18:48:34.944620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-15T18:48:35.497352+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-15T18:48:35.497861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 555 · 2026-05-15T18:48:36.100770+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-15T18:48:42.680014+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've found comprehensive information about ACL ARR 2025-2026 reviewer guidelines. Here's what the current guidelines include:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the 
…[truncated 1211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7182
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-15T18:49:18.732601+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 38, \"total_citations\": 72, \"unique_cited_keys\": 38, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 29, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"doing-more-with-less-2026\", \"type\": \"article\", \"title\": \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\", \"authors\": \"Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.25098\"}, {\"key\": \"efron-1993\", \"ty
…[truncated 31635 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 42631
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-15T18:49:26.016588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-15T18:49:26.519317+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios ($G$) from $7.5{\times}$ ($s{=}0.15$, 95\% CI $[4.1, 11.4]$) to $79.8{\times}$ ($s{=}0.30$, 95\% CI $[63.3, 96.5]$; additive null; multiplicative null preserves the gradient, $G_{\times}{=}21$--$64{\times}$) across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$17{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We present \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key d
…[truncated 184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-15T18:49:26.519765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-15T18:49:26.973276+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 4512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-15T18:49:26.973811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-15T18:49:27.476202+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	
12	\cite{kim2026pqqp} show that compression order (prune-then-quantize vs.\ quantize-then-prune) significantly affects joint quality, and their Progressive Intensity Hypothesis---that weaker perturbations should precede stronger ones---echoes our dose-response finding that interaction severity increases monotonically with sparsity.
13	
14	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
15	
16	\paragraph{KV cache eviction.}
17	Most methods rely on importance scoring whose reliability is increasingly questioned.
18	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher tha
…[truncated 3590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-15T18:49:27.476666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-15T18:49:28.481303+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null ($\mathrm{II} = 0$ under no interaction) as the primary formulation. Although the two sparsity axes are causally coupled---head pruni
…[truncated 2515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-15T18:49:28.481841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-15T18:49:28.532510+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-training-paradigm replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both
…[truncated 2031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-15T18:49:28.884542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-15T18:49:29.337008+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=}496$. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) increases from $7.5{\times}$ (95\% CI: $[4.1, 11.4]$) at $s{=}0.15$ to $79.8{\times}$ ($[63.3, 96.5]$) at $s{=}0.30$ under imp
…[truncated 11818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-15T18:49:29.337576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-15T18:49:29.840162+00:00_

1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Critically, random eviction shows near-identical Gini drops at matched sparsity (DeepSeek $s{=}0.25$: importance $-0.065$ vs.\ random $-0.060$; $s{=}0.30$: $-0.081$ vs.\ $-0.071$; Qwen: $-0.019$ to $-0.046$ for both strategies), confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not the eviction strategy. Yet importance-based severity is $15$--$17{\times}$ larger than random at matched sparsity---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades, while random eviction's decisions are score-independent.
10	
11	This pattern---\emph{importance discrimination collapse}---is consistent with importance-based eviction degenerating into noise-sensitive selection whe
…[truncated 2251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-15T18:49:29.840595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-15T18:49:30.768333+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. The severity gradient characterizes phase-dependent sensitivity patterns that could inform \emph{phase-aware} budget allocation. However, preliminary mitigation experiments (Appendix~\ref{app:pilot-mitigation}) yielded limited recovery (oracle 18\%), suggesting that severity signals alone are insufficient---additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We expect qualitatively similar behavior for other attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), though quantitative magnitudes may differ. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 927
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-15T18:49:30.768838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-15T18:49:31.247714+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$, with amplification ratios $G{=}7.5$--$79.8{\times}$. Random eviction is $3$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Importance discrimination collapse provides a correlational diagnostic: despite near-identical Gini drops, severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	These findings establish compound severity as phase-dependent, providing a diagnostic foundation for future phase-aware mitigation. Extending to code/science reasoning, causal validation of importance discrimination collapse, and characterizing asymmetric compound interactions are key next steps.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 478
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-15T18:49:31.248219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-15T18:49:31.851182+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	Our primary evaluation uses MATH-500; cross-benchmark validation on GSM8K (\S\ref{sec:cross-benchmark}) confirms the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant on GSM8K (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by 
…[truncated 2676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-15T18:49:32.756099+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring rubrics, and all rating scales (soundness, excitement, overall recommendation, confidence, etc.). Include the exact score descriptions for each level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring rubrics, and all rating scales (soundness, excitement, overall recommendation, confidence, etc.). Include the exact score descriptions for each level."
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-15T18:49:39.937063+00:00_

# ACL Rolling Review Form: Criteria and Rating Scales

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
- **5**: "Consider for Award: Could be considered for an outstanding paper award."
- **4**: "Conference: Could be accepted to an ACL conference."
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1**: "Do not resubmit: Has to be fully redone or is not relevant."

## Reproducibility
- **5**: "They could easily reproduce the results."
- **4**: "Could mostly reproduce results, with minor variations possible."
- **3**: "Could reproduce with difficulty due to underspecified parameters."
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7180
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-15T18:49:46.931616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-15T18:49:46.932205+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 2530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-15T18:49:47.915727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-15T18:49:48.318317+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.6)
5	% - Cross-architecture analysis with power analysis (from results §5.5)
6	% - Full entropy-importance discrimination collapse analysis with tables (from analysis §6)
7	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
8	
9	\section{Phase-Strategy Crossover Details}
10	\label{app:crossover-details}
11	
12	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
17	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, r
…[truncated 17955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-15T18:49:48.368985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-15T18:49:48.369678+00:00_

1	\section{Importance Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$).
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$17{\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \geq 0.25$), confirming that the dominant amplification is strategy-specific.
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentra
…[truncated 8825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-15T18:49:48.771210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-15T18:49:49.323724+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-training-paradigm random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-paradigm Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-training-paradigm random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings.
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based conditions remain significant at $p_{\text{Bonf}} < 10^
…[truncated 7450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-15T18:49:49.424719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-15T18:49:49.475693+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 14482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-15T18:51:11.615225+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "StreamingLLM attention sink KV cache eviction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "StreamingLLM attention sink KV cache eviction 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-15T18:51:12.168102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DuoAttention retrieval heads streaming heads KV cache compression 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DuoAttention retrieval heads streaming heads KV cache compression 2024"
  }
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-15T18:51:12.771221+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound compression pruning quantization interaction LLM 2025 2026 beyond UniComp SLiM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound compression pruning quantization interaction LLM 2025 2026 beyond UniComp SLiM"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-15T18:51:18.001283+00:00_

Web search results for query: "DuoAttention retrieval heads streaming heads KV cache compression 2024"

Links: [{"title":"DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads","url":"https://arxiv.org/html/2410.10819v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"DUOATTENTION: EFFICIENT LONG-CONTEXT LLM ...","url":"https://openreview.net/pdf?id=cFu7ze7xUm"},{"title":"Paper page - DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads","url":"https://huggingface.co/papers/2410.10819"},{"title":"DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads","url":"https://www.emergentmind.com/papers/2410.10819"},{"title":"DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads","url":"https://hanlab.mit.edu/projects/duo-attention"},{"title":"DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads | OpenReview","url":"https://openreview.net/forum?id=cFu7ze7xUm"},{"title":"RazorAttention: Efficient KV Cache Compression Through Retrieval Heads | OpenReview","url":"https://openreview.net/forum?id=tkiZQlL04w"},{"title":"Decoding Multi-Head Latent Attention (Part 1): The KV Cache Memory Bottleneck, Solved.","url":"https://vizuara.substack.com/p/decoding-multi-head-latent-attention"},{"title":"[2410.10819] DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads","url":"https://arxiv.org/abs/2410.10819"}]

I found comprehensive information about DuoAttention. Here's a summary of the search results:

## DuoAttention Overview

DuoAttention identifies two distinct types of attention heads: Retrieval Heads, which represent a fraction of the total and are crucial for processing long contexts requiring full attention across all tokens, and Streaming Heads—the majority of attention heads—which primarily focus on recent token
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5833
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-15T18:51:21.125140+00:00_

Web search results for query: "StreamingLLM attention sink KV cache eviction 2024 2025"

Links: [{"title":"GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub","url":"https://github.com/mit-han-lab/streaming-llm"},{"title":"StreamingLLM: Efficient Streaming for LLMs","url":"https://www.emergentmind.com/topics/streamingllm"},{"title":"Efficient Streaming Language Models with Attention Sinks | OpenReview","url":"https://openreview.net/forum?id=NG7sS51zVF"},{"title":"IN-CONTEXT KV-CACHE EVICTION FOR LLMS - OpenReview","url":"https://openreview.net/pdf?id=tvQNysCP7C"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://arxiv.org/html/2509.04377v1"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"In-context KV-Cache Eviction for LLMs via Attention-Gate","url":"https://arxiv.org/html/2410.12876v3"},{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"[2410.12876] In-context KV-Cache Eviction for LLMs via Attention-Gate","url":"https://arxiv.org/abs/2410.12876"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"}]

Based on the search results, here's a comprehensive overview of StreamingLLM, attention sinks, and KV cache eviction in 2024-2025:

## StreamingLLM Overview

StreamingLLM addresses two major challenges in deploying LLMs for streaming applications: caching previous tokens' Key and Value states consumes extensive memory, and popular LLMs cannot generalize to longer texts than the training sequence length.

## The Attention Sink Phenomenon

StreamingLLM identifies an interesting phenomenon where 
…[truncated 1737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9509
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-15T18:51:28.055688+00:00_

Web search results for query: "compound compression pruning quantization interaction LLM 2025 2026 beyond UniComp SLiM"

Links: [{"title":"4 LLM Compression Techniques to Make Models Smaller and Faster","url":"https://www.analyticsvidhya.com/blog/2025/09/llm-compression-techniques/"},{"title":"LLM Compression Techniques to Build Faster and Cheaper LLMs","url":"https://www.projectpro.io/article/llm-compression/1179"},{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"The Good, the Bad, and the Ugly: Cost-Efficient LLM Inference With Quantization, Pruning, and Distillation DLIT71489 | GTC 2025 | NVIDIA On-Demand","url":"https://www.nvidia.com/en-us/on-demand/session/gtc25-dlit71489/"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Combining Pruning and Quantization","url":"https://apxml.com/courses/llm-compression-acceleration/chapter-3-sophisticated-pruning-methodologies/integrating-pruning-quantization"},{"title":"A study and formal framework of the composability of LLM compression techniques","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-025-50814-1"},{"title":"Efficient Compressing and Tuning Methods for Large Language Models: A Systematic Literature Review | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3728636"},{"title":"A Systematic Study of Compression Ordering for Large Language Models","url":"https://arxiv.org/html/2511.19495"},{"title":"Balancing Accuracy and Efficiency: A Practical Guide to Model Compression in Production AI | by Andrea D'Agostino | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/a-comprehensive-guide-to-model-compression-6d4c51689c29"}]

Now let me search more specifically 
…[truncated 7519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 15284
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-15T18:54:35.590863+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿完成（新颖性 + Related Work + 格式）\n\n### Overall: Borderline (2-3), 建议 Findings track\n\n**Soundness 3/5 | Excitement 2/5 | Confidence 4/5**\n\n---\n\n### Must-Fix (3 issues)\n\n**W1 [critical] Novelty 不足以支撑 long paper。** Introduction 自己承认 HIES/ThinKV/Sparse Frontier 的组合可以 qualitatively predict phase-dependent compound degradation。论文的两个 \"novel\" quantitative patterns——strictly monotonic dose-response (JT z=33.7) 和 strategy ranking crossover——本质是 statistical confirmation of qualitatively expected interaction。Crossover 仅 DeepSeek 出现、Qwen 不出现（model-dependent），进一步削弱 generality。与 Voita (2019) / Michel (2019) 等 precedent diagnostic studies 相比，那些工作揭示了 counterintuitive findings（大量 heads 可被安全移除），本文的发现方向性不意外。建议补充 actionable method contribution 或大幅扩展覆盖面。\n\n**W2 [critical] 标题 \"Mathematical Reasoning Models\" 过度泛化。** 实测 2 个 Qwen2ForCausalLM 7B 模型 + 1 个 LlamaForCausalLM (n=49, interaction magnitude ~1/40, only s=0.30 significant after Bonferroni)。标题暗示跨模型泛化但证据不支持。建议限定 \"Qwen2-family\" 或 \"7B-scale\"。\n\n**W3 [critical] \"Cross-training-paradigm controlled comparison\" framing 不准确。** DeepSeek vs Qwen 除架构外，训练数据/tokens/teacher/hyperparameters 全部不同。\"Isolates the effect of training methodology\" 是因果性过度声称。应改为 \"cross-model replication within same architecture family\"。\n\n---\n\n### Should-Fix (5 issues)\n\n**W4** Phase segmentation 基于 dense model attention patterns（Appendix D Table 4 caption 明确写了），但 compression 会改变 attention distribution（论文自己 Section 6 分析了 redistribution）。存在 label-outcome coupling 问题。\n\n**W5** 全文仅 PPL，无 accuracy。Section 5.7 发现 93.2% answer tokens 在 high-sparsity phase (G≈1)，暗示 accuracy 可能不受影响——如果 accuracy 幸存，severity gradient 的实际意义大打折扣。\n\n**W6** Discussion 仍用 \"could inform phase-aware budget allocation\" framing，但 pilot mitigation 仅恢复 18%（低于 pre-registered 30% gate），CI 跨零。实用价值暗示与证据矛盾。\n\n**W7** CI inconsistency: Table 2 Qwen s=0.30 Δ CI = [2.80, 3.56] vs Table 3 = [2.78, 3.56]。数值差 0.02，但在强调统计严谨性的论文中不应出现。\n\n**W8** Missing key references: StreamingLLM (Xiao et al., ICLR 2024, KV cache 奠基工作) 和 DuoAttention (Xiao et al., 2024, retrieval/streaming head classification 与 importance discrimination collapse 直接互补)。\n\n---\n\n### Minor (4 issues)\n\n**M1** Abstract 信息密度过高（5 个 CI、4 个 p-value），首次阅读不友好。\n**M2** 术语有 \"importance discrimination collapse\" / \"score collapse\" / \"score distribution collapse toward uniformity\" 变体，需统一。\n**M3** appendix_moved.tex 和 references.bib 保留内部追踪注释。\n**M4** Conclusion 提 \"extending to code/science reasoning\" 但 GSM8K 已显示 benchmark 间形态差异大。\n\n---\n\n### Reference Verification\n\n- 38 entries, 29 verified, 4 not found in OpenAlex (recent 2025-2026 papers), 5 author name mismatches (mostly corporate/formatting)\n- LKV reference 已修复（不再 Anonymous）✓\n- 0 orphan / 0 missing bib entries ✓\n- 4 not-found entries (defensivekv-iclr2026, hies-2025, phase-transition-compression-2026, mustafar-neurips2025) 需 double-check venue 信息\n\n---\n\n### Strengths\n\nS1 统计方法论上乘（bootstrap/permutation/JT/BH-FDR/winsorization）\nS2 充分的 robustness analysis（segmentation/mpl/asymmetric/multiplicative null）\nS3 诚实的 limitations 和 effect calibration\nS4 清晰的 factorial experimental design\nS5 Importance discrimination collapse 分析有价值（Gini drop 相同但 severity 差 15-17×）",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿完成（新颖性 + Related Work + 格式）\n\n### Overall: Borderline (2-3), 建议 Findings track\n\n**Soundness 3/5 | Excitement 2/5 | Confidence 4/5**\n\n---\n\n### Must-Fix (3 issues)\n\n**W1 [critical] Novelty 不足以支撑 long paper。** Introduction 自己承认 HIES/ThinKV/Sparse Frontier 的组合可以 qualitatively predict phase-dependent compound degradation。论文的两个 \"novel\" quantitative patterns——strictly monotonic dose-response (JT z=33.7) 和 strategy ranking crossover——本质是 statistical confirmation of qualitatively expected interaction。Crossover 仅 DeepSeek 出现、Qwen 不出现（model-dependent），进一步削弱 generality。与 Voita (2019) / Michel (2019) 等 precedent diagnostic studies 相比，那些工作揭示了 counterintuitive findings（大量 heads 可被安全移除），本文的发现方向性不意外。建议补充 actionable method contribution 或大幅扩展覆盖面。\n\n**W2 [critical] 标题 \"Mathematical Reasoning Models\" 过度泛化。** 实测 2 个 Qwen2ForCausalLM 7B 模型 + 1 个 LlamaForCausalLM (n=49, interaction magnitude ~1/40, only s=0.30 significant after Bonferroni)。标题暗示跨模型泛化但证据不支持。建议限定 \"Qwen2-family\" 或 \"7B-scale\"。\n\n**W3 [critical] \"Cross-training-paradigm controlled comparison\" framing 不准确。** DeepSeek vs Qwen 除架构外，训练数据/tokens/teacher/hyperparameters 全部不同。\"Isolates the effect of training methodology\" 是因果性过度声称。应改为 \"cross-model replication within same architecture family\"。\n\n---\n\n### Should-Fix (5 issues)\n\n**W4** Phase segmentation 基于 dense model attention patterns（Appendix D Table 4 caption 明确写了），但 compression 会改变 attention distribution（论文自己 Section 6 分析了 redistribution）。存在 label-outcome coupling 问题。\n\n**W5** 全文仅 PPL，无 accuracy。Section 5.7 发现 93.2% answer tokens 在 high-sparsity phase (G≈1)，暗示 accuracy 可能不受影响——如果 accuracy 幸存，severity gradient 的实际意义大打折扣。\n\n**W6** Discussion 仍用 \"could inform phase-aware budget allocation\" framing，但 pilot mitigation 仅恢复 18%（低于 pre-registered 30% gate），CI 跨零。实用价值暗示与证据矛盾。\n\n**W7** CI inconsistency: Table 2 Qwen s=0.30 Δ CI = [2.80, 3.56] vs Table 3 = [2.78, 3.56]。数值差 0.02，但在强调统计严谨性的论文中不应出现。\n\n**W8** Missing key references: StreamingLLM (Xiao et al., ICLR 2024, KV cache 奠基工作) 和 DuoAttention (Xiao et al., 2024, retrieval/streaming head classification 与 importance discrimination collapse 直接互补)。\n\n---\n\n### Minor (4 issues)\n\n**M1** Abstract 信息密度过高（5 个 CI、4 个 p-value），首次阅读不友好。\n**M2** 术语有 \"importance discrimination collapse\" / \"score collapse\" / \"score distribution collapse toward uniformity\" 变体，需统一。\n**M3** appendix_moved.tex 和 references.bib 保留内部追踪注释。\n**M4** Conclusion 提 \"extending to code/science reasoning\" 但 GSM8K 已显示 benchmark 间形态差异大。\n\n---\n\n### Reference Verification\n\n- 38 entries, 29 verified, 4 not found in OpenAlex (recent 2025-2026 papers), 5 author name mismatches (mostly corporate/formatting)\n- LKV reference 已修复（不再 Anonymous）✓\n- 0 orphan / 0 missing bib entries ✓\n- 4 not-found entries (defensivekv-iclr2026, hies-2025, phase-transition-compression-2026, mustafar-neurips2025) 需 double-check venue 信息\n\n---\n\n### Strengths\n\nS1 统计方法论上乘（bootstrap/permutation/JT/BH-FDR/winsorization）\nS2 充分的 robustness analysis（segmentation/mpl/asymmetric/multiplicative null）\nS3 诚实的 limitations 和 effect calibration\nS4 清晰的 factorial experimental design\nS5 Importance discrimination collapse 分析有价值（Gini drop 相同但 severity 差 15-17×）",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-15T18:54:39.207652+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3616
}
```

</details>

---


### Assistant

_source line 598 · 2026-05-15T18:54:49.537603+00:00_

审稿完成，已汇报给 Director。

**审稿结论**: Borderline (2-3)，建议 Findings track 而非 Main Conference。

核心问题：
- **3 个 Must-Fix**: novelty 不足（量化已可预测的 interaction）、标题过度泛化（实测仅 Qwen2 family）、"controlled comparison" framing 不准确
- **5 个 Should-Fix**: dense-model phase segmentation 偏差、无 accuracy 验证、实用价值过度暗示、CI 不一致、缺少 StreamingLLM/DuoAttention 引用
- **4 个 Minor**: abstract 过密、术语变体、内部注释残留、future work 泛化过度

方法论层面（统计严谨性、robustness checks）是本文最强的部分；贡献层面（novelty 深度、experimental scope）是主要短板。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

4 recorded events


### User

_source line 599 · 2026-05-15T18:55:50.219638+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿报告（方法严谨性 + 实验设计）

### Summary
本文系统表征了 compound sparsity（head pruning + KV cache eviction 同时施加）在推理模型不同注意力稀疏度阶段中的退化严重性差异，发现 importance-based eviction 产生随稀疏度单调递增的 phase-strategy 交互效应（Δ: 0.39→8.48），而 random eviction 效应弱 3–17×。核心发现是一个诊断性结论（compound severity 是 phase-dependent 的），方法论上严格使用了 nonparametric 统计框架，但实际影响力受限于 93.2% 答案 token 落在高稀疏阶段（交互最小处）以及缺乏下游 accuracy 验证。

---

### Strengths

S1. 问题定位精准且填补明确空白
S2. 统计方法论高度严谨且异常透明（nonparametric bootstrap B=10,000, Wilcoxon/Mann-Whitney, Bonferroni, BH-FDR, JT test）
S3. 充分的 hedging 和自我批评
S4. 鲁棒性验证全面（6 个维度）
S5. Crossover 效应有洞察力

---

### Must-Fix

**W1 [critical] Phase segmentation 缺乏独立验证——核心 proxy 的有效性未建立**
- attention sparsity tercile segmentation 被用作推理阶段的 proxy，论文称 "operationalization choice" 并检查了 quartile/quintile robustness——但这不等于验证 attention sparsity 是否是 reasoning phase 的有效 proxy
- 低稀疏 = exploratory reasoning、高稀疏 = structured computation 的对应关系来自对 ThinKV 的引用，但 ThinKV 的分类基于 `&lt;think>` token 显式分隔符
- Qwen 45.2% mid-phase null rate 进一步质疑 proxy 在非 distillation 模型上的适用性
- 建议：(a) 用 DeepSeek `&lt;think>` token 做 ground-truth 验证；(b) 或重新 frame 为 "attention-sparsity-modulated"

**W2 [critical] Practical significance 存疑：93.2% 答案 token 天然屏蔽**
- 论文唯一论据是 "silent reasoning errors"，但无 accuracy-level 验证
- 建议：MATH-500 compound sparsity accuracy 评估

**W3 [critical] Multiplicative null 方法论与主分析不一致**
- 主分析 G 用 per-problem median of ratios；multiplicative null G_× 用 aggregate per-phase PPL ratios
- Table 7 已展示两种定义可差 10×
- 建议：per-problem 重新计算 G_×

---

### Should-Fix

**W4** Cross-architecture 证据过弱但标题暗示泛化（LLaMA n=49, ~1/40 effect, 仅 s=0.30 显著）
**W5** GSM8K n=50 功效不足（无 power analysis, Qwen 截断, random 全部非显著可能仅因功效不足）
**W6** Bonferroni family size 定义说明不足（k=4 per model×strategy）
**W7** Importance discrimination collapse 解释力被过度 frame（Gini drop 两策略几乎相同但 severity 差 15×）

---

### Minor

**W8** Spearman ρ=1.0 (n=4) 无增量信息
**W9** Table 2 Qwen s=0.15 G "n.d." 含义不清
**W10** Abstract 数字密度过高

---

### Questions

Q1 是否已做 sparsity-based vs `&lt;think>`-based segmentation 一致性分析？
Q2 Phase segmentation 在 dense model 上计算——compound sparsity 下 attention 分布是否一致？
Q3 Compound sparsity 对 MATH-500 accuracy 到底下降多少？
Q4 Pilot oracle 18% recovery——是否暗示 phase-aware 方向本身有误？
Q5 G per-problem 中 II_high ≤ 0 时如何处理？

---

### Overall: 3.0/5 — Findings-level accept, 置信度 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-15T18:58:03.062245+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n### 共识（7 项 AGREE）\n\n- **W1 Phase segmentation proxy validity**: AGREE。核心方法论缺陷。DeepSeek 有 `&lt;think>` token 可做 ground truth validation 但未做。我额外补充了 dense-model-based segmentation 的 label-outcome coupling 问题（Appendix D Table 4 caption 明确 segmentation 在 dense model 上计算，但 Section 6 分析了 pruning 后 attention redistribution）。\n- **W2 93.2% answer tokens shielding / no accuracy**: AGREE。跨 reviewer 共识。\n- **W3 Multiplicative null G_× 方法论不一致**: AGREE with nuance。确实不一致（per-problem vs aggregate），但 multiplicative null 是 robustness check 而非 primary result，且论文选 additive null 作为 primary 的理由合理。仍需修复以兑现 \"null-choice invariant\" 的声称。\n- **W4 Cross-architecture 证据弱**: AGREE。与我的 W2 一致。\n- **W5 GSM8K power**: AGREE with qualification。合理批评但论文有 indirect 支撑（within-MATH-500 task-complexity correlation）。\n- **W8 Spearman n=4**: AGREE。\n- **W10 Abstract 密度**: AGREE。\n\n### 反驳（3 项 REBUT）\n\n- **W6 Bonferroni family size**: REBUT。§4 par:stats 已说明 k=4 per model×strategy family 的逻辑，Appendix F BH-FDR 做了 k=44 global correction 作为 robustness check。是写作清晰度问题，非方法论错误。\n- **W7 Importance discrimination collapse 过度 frame**: REBUT。Section 6 开篇第一句即定位为 \"correlational diagnostics that do not fully explain\"，contribution 3 的 claim（necessary but not sufficient）与正文 hedging 一致。Structural specificity 有 quantitative evidence（Mann-Whitney p<10^{-28}, r=0.62–0.76）。\n- **W9 \"n.d.\" 不清**: REBUT。Table 2 脚注 † 已完整解释。建议改为 \"undef.\" 提升 readability。\n\n### 跨 Reviewer 共识性核心问题（3 个）\n\n1. Phase segmentation proxy validity + dense-model-based assignment\n2. Accuracy 验证缺失 vs 93.2% answer token shielding\n3. 标题泛化过度 vs 实际仅 Qwen2-family evidence\n\n### 我的独立补充\n\n- Discussion 对 practical value 的过度暗示（pilot 18% 但仍 \"could inform\"）\n- CI inconsistency Table 2 vs Table 3（Qwen s=0.30: 2.80 vs 2.78）\n- Missing references: StreamingLLM + DuoAttention\n- \"Cross-training-paradigm controlled comparison\" 因果性过度声称",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n### 共识（7 项 AGREE）\n\n- **W1 Phase segmentation proxy validity**: AGREE。核心方法论缺陷。DeepSeek 有 `&lt;think>` token 可做 ground truth validation 但未做。我额外补充了 dense-model-based segmentation 的 label-outcome coupling 问题（Appendix D Table 4 caption 明确 segmentation 在 dense model 上计算，但 Section 6 分析了 pruning 后 attention redistribution）。\n- **W2 93.2% answer tokens shielding / no accuracy**: AGREE。跨 reviewer 共识。\n- **W3 Multiplicative null G_× 方法论不一致**: AGREE with nuance。确实不一致（per-problem vs aggregate），但 multiplicative null 是 robustness check 而非 primary result，且论文选 additive null 作为 primary 的理由合理。仍需修复以兑现 \"null-choice invariant\" 的声称。\n- **W4 Cross-architecture 证据弱**: AGREE。与我的 W2 一致。\n- **W5 GSM8K power**: AGREE with qualification。合理批评但论文有 indirect 支撑（within-MATH-500 task-complexity correlation）。\n- **W8 Spearman n=4**: AGREE。\n- **W10 Abstract 密度**: AGREE。\n\n### 反驳（3 项 REBUT）\n\n- **W6 Bonferroni family size**: REBUT。§4 par:stats 已说明 k=4 per model×strategy family 的逻辑，Appendix F BH-FDR 做了 k=44 global correction 作为 robustness check。是写作清晰度问题，非方法论错误。\n- **W7 Importance discrimination collapse 过度 frame**: REBUT。Section 6 开篇第一句即定位为 \"correlational diagnostics that do not fully explain\"，contribution 3 的 claim（necessary but not sufficient）与正文 hedging 一致。Structural specificity 有 quantitative evidence（Mann-Whitney p<10^{-28}, r=0.62–0.76）。\n- **W9 \"n.d.\" 不清**: REBUT。Table 2 脚注 † 已完整解释。建议改为 \"undef.\" 提升 readability。\n\n### 跨 Reviewer 共识性核心问题（3 个）\n\n1. Phase segmentation proxy validity + dense-model-based assignment\n2. Accuracy 验证缺失 vs 93.2% answer token shielding\n3. 标题泛化过度 vs 实际仅 Qwen2-family evidence\n\n### 我的独立补充\n\n- Discussion 对 practical value 的过度暗示（pilot 18% 但仍 \"could inform\"）\n- CI inconsistency Table 2 vs Table 3（Qwen s=0.30: 2.80 vs 2.78）\n- Missing references: StreamingLLM + DuoAttention\n- \"Cross-training-paradigm controlled comparison\" 因果性过度声称",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-15T18:58:06.778075+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Assistant

_source line 602 · 2026-05-15T18:58:09.310367+00:00_

交叉回应已提交给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

62 recorded events


### User

_source line 603 · 2026-05-16T02:04:58.765351+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务：Reviewer 2（新颖性 + 完整性 + 相关工作 + 写作/格式）

### 论文信息
- **标题**: Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models
- **路径**: `projects/phase-gated-compound-sparse/paper/main.tex`（包含多个 \input 文件：abstract, introduction, related_work, background, methodology, results, analysis, discussion, conclusion, limitations, appendix, appendix_moved, appendix_disc_analysis, appendix_robustness）
- **目标 Venue**: EMNLP 2026 Main Conference
- **Deadline**: 2026-05-25（ARR May cycle）
- **格式**: ACL 模板，8 页正文限制（不含参考文献和附录），double-blind，mandatory Limitations section

### 你的审查侧重
请重点评估以下方面：

1. **新颖性 (Novelty)**
   - 这篇论文的核心 claim 是"compound sparsity severity is phase-dependent"——这在 ThinKV、Sparse Frontier、Phase Transition Compression 等已有工作之后是否足够新颖？
   - 论文自我定位为"diagnostic study"（引用 Voita/Michel），但 Voita/Michel 揭示的是反直觉发现（多数 heads 可删、attention 是否能被简单替代），而本文的核心发现（attention 稀疏的 phase 更脆弱）在直觉上可预期——统计量化是否构成足够的 contribution？
   - Crossover 是 model-dependent（只在 DeepSeek 上存在），能否作为核心 novelty anchor？
   - 对 EMNLP main conference 而言，这篇论文更适合 Main Conference 还是 Findings track？

2. **完整性 (Completeness)**
   - "Importance discrimination collapse" 作为 mechanism——Gini drop <10% 却解释 15-17× severity 差异，gap 是否过大？
   - Pilot mitigation（Appendix F）gate failed (18% < 30%)——是否削弱论文的 practical value narrative？
   - 缺少 inference throughput/latency 评估
   - 仅测试了一种 importance scoring method (cumulative attention mass)

3. **相关工作 (Related Work)**
   - 覆盖是否全面？是否有遗漏的关键文献？
   - 特别检查：compound compression、KV cache eviction、phase-aware inference 三个段落的引用是否完整
   - 检查 references.bib 中的条目：是否有 anonymous 条目、年份错误、venue 不对
   - 是否有幻觉引用（hallucinated citations）？

4. **写作质量与格式**
   - Abstract 信息密度是否过高？（数字、CI、p-value 太多？）
   - 正文是否超 8 页限制？（main.tex sections 1-8 + Limitations + Reproducibility）
   - 表格/图表标注是否清晰？
   - 术语一致性（"importance discrimination collapse" vs 其他变体）
   - LaTeX 源码中是否有残留内部注释？
   - 匿名规则是否完全遵守？

请输出完整审稿报告，格式：
- Summary（2-3 句）
- Strengths（逐条）
- Weaknesses（逐条，标注 severity: critical/warning/info）
- Questions for Authors
- Missing References
- Overall Assessment + Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-16T02:05:07.332108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-16T02:05:08.236662+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-16T02:05:08.238779+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-16T02:05:08.289338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-16T02:05:13.635785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-16T02:05:14.138393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-16T02:05:14.591004+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-16T02:05:14.691875+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-16T02:05:20.672318+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, an
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7036
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-16T02:05:20.672745+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 5980
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-16T02:05:24.390647+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-16T02:05:24.491648+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-16T02:05:25.670338+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any other fields reviewers must fill out. Include the exact wording of each criterion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any other fields reviewers must fill out. Include the exact wording of each criterion."
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-16T02:05:33.006731+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully..."
- 4: "Quite sure. I tried to check the important points carefully..."
- 3: "Pretty sure, but there's a chance I missed something..."
- 2: "Willing to defend my evaluation, but it is fairly likely..."
- 1: "Not my area, or paper is very hard to understand..."

**Soundness** (1-5 scale with half-point increments)
- 5: "Excellent: This study is one of the most thorough I have seen..."
- 4: "Strong: This study provides sufficient support for all claims..."
- 3: "Acceptable: This study provides sufficient support for main claims..."
- 2: "Poor: Some main claims not sufficiently supported..."
- 1: "Major Issues: This study is not yet sufficiently thorough..."

**Excitement** (1-5 scale with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others..."
- 4: "Exciting: I would mention this paper to others..."
- 3: "Interesting: I might mention some points to others..."
- 2: "Potentially Interesting: this paper does not resonate with me..."
- 1: "Not Exciting: this paper does not resonate with me..."

**Overall Assessment** (1-5 scale with half-point increments)
- 5: Consider for Award
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Open-Ended Sections

1. **Paper Summary** - describe paper topic and address misunderstandings
2. **Summary of Strengths** - major publication reasons
3. **Summary of Weaknesses** - concerns with numbered points
4. **Comments/Suggestions/Typos** - improvement suggestions
5. **Best Paper Justification** - required if award consideration given
6. **Limitations and Societal Impact** - adequacy assessment
7. **Ethical Concerns** - alignment with ACL Code of Ethics

#
…[truncated 276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7336
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-16T02:05:38.333817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-16T02:05:38.686567+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity Severity\\in 7B-Scale Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-16T02:05:38.838611+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-16T02:06:06.371284+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 40, \"total_citations\": 74, \"unique_cited_keys\": 40, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 4, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"streamingllm-iclr2024\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"duoattention-2024\", \"type\": \"article\", \"title\": \"DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads\", \"authors\": \"Xiao, Guangxuan and Tang, Jiaming and Zuo, Jingwei and Guo, Junxian and Yang, Sh...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2410.10819\"}, {\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-i
…[truncated 33213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 27532
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-16T02:06:15.437892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-16T02:06:15.889962+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios $G{=}7.5$--$79.8{\times}$ across reasoning phases in 7B-scale mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $3$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
6	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
7	We present \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
8	These findings establish the phase-dependent nature of compound severity as a diagnostic foundation for future phase-aware mitigation strategies.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-16T02:06:15.942655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-16T02:06:16.395155+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 3857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-16T02:06:16.395574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-16T02:06:16.797257+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	
12	\cite{kim2026pqqp} show that compression order (prune-then-quantize vs.\ quantize-then-prune) significantly affects joint quality, and their Progressive Intensity Hypothesis---that weaker perturbations should precede stronger ones---echoes our dose-response finding that interaction severity increases monotonically with sparsity.
13	
14	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
15	
16	\paragraph{KV cache eviction.}
17	StreamingLLM~\cite{streamingllm-iclr2024} establishes attention sinks as a foundational mechanism; DuoAttention~\cite{duoattention-2024} classifies heads into retrieval and streaming types, complementing our analysis of importance discrimination collapse (\S\ref{sec:discrimination-collapse-main}). Subsequent work i
…[truncated 2275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-16T02:06:16.797961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-16T02:06:16.848522+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-training-paradigm replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both
…[truncated 2014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-16T02:06:23.786878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-16T02:06:24.138504+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=}496$. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) increases from $7.5{\times}$ (95\% CI: $[4.1, 11.4]$) at $s{=}0.15$ to $79.8{\times}$ ($[63.3, 96.5]$) at $s{=}0.30$ under imp
…[truncated 12220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-16T02:06:24.189145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-16T02:06:24.641380+00:00_

1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), confirming that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compo
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-16T02:06:24.641918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-16T02:06:25.043585+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation (Appendix~\ref{app:pilot-mitigation}) achieved 18\% recovery, below the pre-registered 30\% gate, suggesting that effective phase-aware allocation requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We expect qualitatively similar behavior for other attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), though quantitative magnitudes may differ. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-16T02:06:25.094487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-16T02:06:25.145184+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$, with amplification ratios $G{=}7.5$--$79.8{\times}$. Random eviction is $3$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Importance discrimination collapse provides a correlational diagnostic: despite near-identical Gini drops, severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	These findings establish compound severity as phase-dependent, providing a diagnostic foundation for future phase-aware mitigation. Future work could explore whether these patterns generalize to other reasoning domains, provide causal validation of importance discrimination collapse, and systematically characterize asymmetric compound interactions.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-16T02:06:32.287898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-16T02:06:32.941136+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	Our primary evaluation uses MATH-500; cross-benchmark validation on GSM8K (\S\ref{sec:cross-benchmark}) confirms the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant on GSM8K (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by 
…[truncated 3213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-16T02:06:32.941719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-16T02:06:33.272961+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null as primary: it assumes $r_b = r_a + r_k - 1$ (compound loss equals sum of individual losses), the most conservative independence assu
…[truncated 2314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 331
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-16T02:06:33.273436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-16T02:06:33.728243+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 2530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-16T02:06:33.728785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-16T02:06:33.779552+00:00_

1	
2	\section{Phase-Strategy Crossover Details}
3	\label{app:crossover-details}
4	
5	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
10	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
11	\label{fig:crossover}
12	\end{figure}
13	
14	
15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). The main analysis ($n{=}496$) appears in Table~\ref{tab:main-results}. $G$ values in this table use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II
…[truncated 17518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-16T02:06:40.189496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-16T02:06:40.743048+00:00_

1	\section{Importance Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$).
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$17{\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \geq 0.25$), confirming that the dominant amplification is strategy-specific.
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentra
…[truncated 13583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-16T02:06:40.743596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-16T02:06:40.795905+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-training-paradigm random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-paradigm Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-training-paradigm random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings.
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based conditions remain significant at $p_{\text{Bonf}} < 10^
…[truncated 9862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-16T02:06:53.320256+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DefensiveKV\" KV cache eviction fragility ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DefensiveKV\" KV cache eviction fragility ICLR 2026"
  }
}
```

</details>

---


### Tool call

_source line 651 · 2026-05-16T02:06:54.326107+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"MUSTAFAR\" multi-stage transformer KV cache compression NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"MUSTAFAR\" multi-stage transformer KV cache compression NeurIPS 2025"
  }
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-16T02:06:54.980130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Entropy Meets Importance\" HIES head importance entropy score transformer pruning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Entropy Meets Importance\" HIES head importance entropy score transformer pruning 2025"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-16T02:06:59.818766+00:00_

Web search results for query: ""DefensiveKV" KV cache eviction fragility ICLR 2026"

Links: [{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION IN LLM INFERENCE","url":"https://arxiv.org/pdf/2510.13334"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION","url":"https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"},{"title":"(PDF) Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.researchgate.net/publication/396517805_Taming_the_Fragility_of_KV_Cache_Eviction_in_LLM_Inference"},{"title":"[PDF] Taming the Fragility of KV Cache Eviction in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Taming-the-Fragility-of-KV-Cache-Eviction-in-LLM-Feng-Guo/10b323b80b3f57a7f15d44eb5a72872a3adfbcb3"},{"title":"[Literature Review] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.themoonlight.io/en/review/taming-the-fragility-of-kv-cache-eviction-in-llm-inference"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.aimodels.fyi/papers/arxiv/taming-fragility-kv-cache-eviction-llm-inference"}]

I found comprehensive information about DefensiveKV. Here's what the search revealed:

## DefensiveKV: Taming the Fragility of KV Cache Eviction

DefensiveKV exposes the inherent fragility of stability assumptions in KV cache eviction methods and introduces defensive aggregat
…[truncated 1252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6498
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-16T02:07:01.433951+00:00_

Web search results for query: ""MUSTAFAR" multi-stage transformer KV cache compression NeurIPS 2025"

Links: [{"title":"NeurIPS Poster MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://neurips.cc/virtual/2025/poster/119320"},{"title":"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning ...","url":"https://neurips.cc/media/neurips-2025/Slides/119320.pdf"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v2"},{"title":"NeurIPS Poster Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://neurips.cc/virtual/2025/poster/119605"},{"title":"[2505.22913] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/abs/2505.22913"},{"title":"KV Cache Pruning in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-pruning"},{"title":"Efficient LLMs at Scale: My NeurIPS Week in KV Caches, Spec Decoding, and FP4","url":"https://kaitchup.substack.com/p/efficient-llms-at-scale-my-neurips"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"},{"title":"NeurIPS Poster KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://neurips.cc/virtual/2025/poster/118741"},{"title":"A Systematic Exploration of KV Cache Compression ...","url":"https://arxiv.org/pdf/2503.11816"}]

I found comprehensive information about MUSTAFAR. Here are the key findings:

## Overview

MUSTAFAR demonstrates that unstructured sparsity significantly improves KV cache compression for LLMs, enabling sparsity levels up to 70% without compromising accuracy or requiring fine-tuning. It conducts a systematic exploration of pruning strategies and finds per-token magnitude-based pruning as highly effective for both Key and Value caches under unstructured sparsity, surpassing prior structured p
…[truncated 1108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7107
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-16T02:07:02.189230+00:00_

Web search results for query: ""Entropy Meets Importance" HIES head importance entropy score transformer pruning 2025"

Links: [{"title":"[2510.13832] Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning","url":"https://arxiv.org/abs/2510.13832"},{"title":"(PDF) Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning","url":"https://www.researchgate.net/publication/396541457_Entropy_Meets_Importance_A_Unified_Head_Importance-Entropy_Score_for_Stable_and_Efficient_Transformer_Pruning"},{"title":"Entropy Meets Importance: A Unified Head Importance–Entropy Score for Stable and Efficient Transformer Pruning","url":"https://arxiv.org/html/2510.13832"},{"title":"A Unified Head Importance–Entropy Score for Stable and ...","url":"https://opt-ml.org/papers/2025/paper51.pdf"},{"title":"A Unified Head Importance-Entropy Score for Stable and ...","url":"https://arxiv.org/pdf/2510.13832"},{"title":"ENTROPY MEETS IMPORTANCE:AUNIFIED HEAD ...","url":"https://openreview.net/pdf/77c597d3ac85fdf6b61cfb7ca9e2147a40b3a85c.pdf"},{"title":"Head Pruning in Transformers","url":"https://www.emergentmind.com/topics/head-pruning"},{"title":"Entropy-Guided Head Importance for Token Pruning in Vision Transformers | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/10773618/10773627/10773748.pdf"},{"title":"heart-vit: hessian-guided efficient dynamic attention and ...","url":"https://arxiv.org/pdf/2512.20120"},{"title":"Token Pruning in Transformers","url":"https://www.emergentmind.com/topics/token-pruning-framework"}]

Based on the web search results, I found detailed information about the "Entropy Meets Importance" paper. Here's what the research covers:

## Overview

"Entropy Meets Importance" introduces HIES (Head Importance-Entropy Score), which integrates head importance scores with attention entropy, providing complementary evidence on per-head 
…[truncated 1394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7209
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-16T02:07:12.021432+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Phase transitions in large language model compression\" npj 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Phase transitions in large language model compression\" npj 2026"
  }
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-16T02:07:12.928453+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.22913",
  "prompt": "What is the exact title of this paper? Who are the authors? What venue was it published at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.22913",
    "prompt": "What is the exact title of this paper? Who are the authors? What venue was it published at?"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-16T02:07:15.140450+00:00_

# Paper Details

**Title:** "Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference"

**Authors:** Donghyeon Joo, Helya Hosseini, Ramyad Hadidi, and Bahar Asgari

**Venue:** NeurIPS 2025

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 2211
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-16T02:07:18.106999+00:00_

Web search results for query: ""Phase transitions in large language model compression" npj 2026"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"Phase transitions in large language model compression – DOAJ","url":"https://doaj.org/article/06b2d6b18f08424a9f7778c269597d3c"},{"title":"GitHub - whucs21Mzy/Model-Phase-Transitions: Navigating Model Phase Transitions to Enable Extreme Lossless Compression: A Perspective","url":"https://github.com/whucs21Mzy/Model-Phase-Transitions"},{"title":"Phase transitions in large language models ..","url":"https://www.hyper-exponential.com/p/phase-transitions-in-large-language"},{"title":"Phase Transitions in Large Language Models and the O(N) Model","url":"https://arxiv.org/pdf/2501.16241"},{"title":"Lossless data compression by large models | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01033-7"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"[Literature Review] Phase Transitions in Large Language Models and the $O(N)$ Model","url":"https://www.themoonlight.io/en/review/phase-transitions-in-large-language-models-and-the-on-model"},{"title":"[2511.12768] Evidence of Phase Transitions in Small Transformer-Based Language Models","url":"https://arxiv.org/abs/2511.12768"}]

Great! I found the research article you were looking for. Here are the key findings:

## Phase Transitions in Large Language Model Compression (npj 2026)

The paper argues that Large Language Models exhibit Model Phase Transitions: performance collapses beyond critical compression thresholds. The authors ana
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6085
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-16T02:07:49.176927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NeurIPS 2025 \"MUSTAFAR\" \"Joo\" \"Wonyong\" OR \"Donghyeon\" KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NeurIPS 2025 \"MUSTAFAR\" \"Joo\" \"Wonyong\" OR \"Donghyeon\" KV cache"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-16T02:07:55.761744+00:00_

Web search results for query: "NeurIPS 2025 "MUSTAFAR" "Joo" "Wonyong" OR "Donghyeon" KV cache"

Links: [{"title":"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning ...","url":"https://neurips.cc/media/neurips-2025/Slides/119320.pdf"},{"title":"NeurIPS Poster MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://neurips.cc/virtual/2025/poster/119320"},{"title":"[PDF] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mustafar:-Promoting-Unstructured-Sparsity-for-KV-in-Joo-Hosseini/643c287adfaccc9d5c06496c9711beb96b2b4d3c"},{"title":"Publications - Ramyad Hadidi","url":"https://ramyadhadidi.github.io/publications/"},{"title":"Donghyeon Joo's research works | University of Maryland, College Park and other places","url":"https://www.researchgate.net/scientific-contributions/Donghyeon-Joo-2284675131"},{"title":"Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference | Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture","url":"https://dl.acm.org/doi/full/10.1145/3725843.3756065"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"},{"title":"Donghyeon Joo","url":"https://dhjoo.info/"},{"title":"NeurIPS Poster SALS: Sparse Attention in Latent Space for KV Cache Compression","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115064"},{"title":"NeurIPS Poster R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120110"}]

I found relevant information about MUSTAFAR at NeurIPS 2025. Here are the search results:

## MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference

The paper was presented by Donghyeon Joo, Helya Hosseini, Ramyad Hadidi, and Bah
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6584
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-16T02:09:50.513808+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## 总体评分\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 统计工作严谨但核心发现的直觉可预期性削弱了 novelty，且关键引用存在严重伪造问题。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨、统计方法得当，但 mechanism 解释力不足（Gini<10% vs severity 15-17×），且 cross-architecture 证据薄弱 |\n| Excitement | 2/5 | 核心发现（attention 稀疏 phase 更脆弱）在直觉上可预期；crossover 仅 model-dependent；无 actionable mitigation |\n| Reproducibility | 4/5 | 详尽的统计报告、robustness checks、多种 segmentation 验证；但代码未公开（\"upon acceptance\"） |\n| Confidence | 4/5 | 熟悉 KV cache compression 和 attention pruning 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 引用 `mustafar-neurips2025` 标题和作者均为伪造\n\n- 具体位置：references.bib `mustafar-neurips2025` 条目；related_work.tex line 18\n- 问题：Bib 条目标题为 \"MUSTAFAR: Multi-Stage Transformer Architecture for Adaptive Reasoning with KV Cache Compression\"，作者为 \"Joo, Wonyong and Kim, Sungmin and Park, Sehyun and Yoo, Kang Min\"。实际论文标题为 \"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\"（Donghyeon Joo, Helya Hosseini, Ramyad Hadidi, Bahar Asgari; NeurIPS 2025）。标题完全编造、作者名全错、论文主题也对不上（实际是 unstructured sparsity pruning，非 \"learned budgets\"）。\n- 为什么影响接收：这是一个典型的 AI 生成幻觉引用——标题、作者、描述均为虚构。严重违反学术诚信；若真实 reviewer 发现此问题，极有可能一票否决。\n- 建议修改方向：(1) 修正为真实标题和作者；(2) 重新评估该引用在 \"learned budgets\" 语境下是否仍然恰当（实际内容是 unstructured sparsity，不是 learned budgets）；(3) 全面审查所有 bib 条目是否存在类似问题。\n\n**N2** [critical] Novelty 不足以支撑 Main Conference\n\n- 具体位置：全文；Introduction §1 line 22 自我定位为 \"diagnostic study\"\n- 问题：\n  - 核心 claim \"compound sparsity severity is phase-dependent\" 在 ThinKV (ICLR 2026) 已知 phase-dependent compression tolerance、Sparse Frontier (2025) 已知 no single strategy dominates across stages、Phase Transition Compression (npj 2026) 已知 joint safe region is intersection of per-dimension zones 之后，直觉上完全可预期。\n  - 论文自比 Voita/Michel 的\"diagnostic study\"传统，但 Voita/Michel 揭示的是**反直觉发现**（大多数 heads 可删无影响），而本文量化的是**符合直觉的预期**（attention 分散的阶段更脆弱）。\n  - Crossover 是唯一可能构成 novelty anchor 的发现，但仅在 DeepSeek 上存在、Qwen 不复现，且 LLaMA 证据极弱（n=49, ~1/40 magnitude），无法作为 generalizable contribution。\n  - 没有 mitigation 方法：pilot gate failed (18% < 30%)，进一步削弱 practical value。\n- 为什么影响接收：对 EMNLP Main 而言，pure characterization 需要揭示 surprising / counter-intuitive 发现或提供 actionable implications。本文的 findings 更适合 Findings track。\n- 建议修改方向：(1) 强化对为何该发现 non-trivial 的论证——仅知道 \"phase matters\" 不等于预测 7.5-79.8× 的量级和 monotonic dose-response；(2) 提供更强的 cross-architecture 证据；(3) 考虑投 Findings。\n\n**N3** [critical] Mechanism 解释力严重不足\n\n- 具体位置：Section 6 (Analysis), §6.1\n- 问题：论文承认 \"both strategies exhibit near-identical Gini drops (<10% difference), yet severity diverges by 15–17×\"。这意味着 importance discrimination collapse 作为 proposed mechanism，存在一个**数量级的解释缺口**。Gini 的 phase-dependence 被声称为 mechanism，但 low-sparsity phase 的 Gini drop 幅度论文未单独量化（只报了 aggregate），无法验证 \"collapse has maximum impact in low-sparsity phases\" 的 claim。\n  - Entropy redistribution 仅在 DeepSeek 上一致，Qwen 仅 2/4 replicates。\n  - 因果验证完全缺失（仅为 correlational）。\n- 为什么影响接收：一篇 diagnostic study 如果 mechanism 部分无法在数量上解释核心 observation，则其 explanatory contribution 大幅削弱。\n- 建议修改方向：(1) 报告 per-phase Gini delta（而非仅 aggregate）以验证 phase-dependence claim；(2) 明确讨论 \"structural specificity\" 能否弥补解释缺口；(3) 降低对 mechanism 解释力的宣称力度。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Cross-architecture 证据过于薄弱却占较大篇幅\n\n- 具体位置：Section 5.4 (§sec:cross-arch), Appendix G\n- 问题：LLaMA 实验 n=49、effect size ~1/40、仅 s=0.30 Bonferroni-corrected significant、power analysis 显示需要 n≥200 才达 0.80 power。本质上这个实验 underpowered 到无法得出有意义结论。但 abstract 和 intro 仍然说 \"exploratory cross-architecture evidence...suggesting the qualitative pattern may extend beyond Qwen2\"，给读者一种 generalization 正在建立的误导印象。\n- 建议：(1) 在 abstract 中删除 LLaMA 相关内容（或明确标注 \"inconclusive\"）；(2) 如果无法 run n≥200，应在正文 Limitations 中更前置地承认。\n\n**W2** [warning] Abstract 信息密度过高\n\n- 具体位置：abstract.tex\n- 问题：9 行 abstract 包含 $G=7.5$–$79.8×$, $\\Delta: 0.39 → 8.48$, $p \\ll 10^{-10}$, $n_{eff}=475$, $s ≥ 0.25$, CI 等大量数字。读者在 abstract 阶段难以消化这些细节。\n- 建议：保留 1-2 个关键数字（如 $G$ 范围），其余移入正文。Abstract 应传递 insight 而非统计细节。\n\n**W3** [warning] 正文可能超 8 页限制\n\n- 具体位置：main.tex sections 1-8 + Limitations + Reproducibility\n- 问题：主体包含 8 个 section（Introduction 到 Conclusion），加上 6 个 subsection 在 Results 中（每个含 table/figure），1 个 table 在 Analysis 中。以 ACL format 11pt、\\small tables 计算，Results 单独就可能占 2.5-3 页。Limitations 约 1.5 页。总计大概率超过 8 页正文限制。\n- 建议：合并 Section 7 (Discussion) 到 Section 8 (Conclusion)；将 §5.4 (Cross-Arch) 和 §5.5 (GSM8K) 完整移入 Appendix。\n\n**W4** [warning] 仅测试一种 importance scoring method\n\n- 具体位置：Section 4, §methodology line 11\n- 问题：KV importance 仅用 position-normalized cumulative attention mass。Discussion §7 声称 \"expect qualitatively similar behavior for H2O, SnapKV, PyramidKV\"，但无实验支撑。不同 scoring methods 可能有不同的 discrimination collapse dynamics。\n- 建议：至少补充一种替代 scoring method（如 H2O 的 heavy-hitter metric）的 spot check，或将泛化声明降级为 hypothesis。\n\n**W5** [warning] Pilot mitigation 失败但仍在正文保留\n\n- 具体位置：Section 7 (Discussion), Appendix §app:pilot-mitigation\n- 问题：Pre-registered gate 30% recovery, actual 18%, heuristic variant 32% 但 CI span zero. 这本质上是一个 negative result，但论文在 Discussion 中仍暗示 \"practical implications for deployment\"。失败的 mitigation 实际上削弱了 \"diagnostic foundation for future phase-aware mitigation\" 的 narrative。\n- 建议：诚实讨论为什么 mitigation failed，这本身可以是有价值的贡献；但不应在 framing 中暗示直接的 deployment value。\n\n**W6** [warning] 缺少 inference throughput/latency 评估\n\n- 具体位置：Limitations §limitations line 19-20\n- 问题：论文在 Limitations 中承认了这一点，但对于一篇关于 \"compound sparsity\" 的论文，完全没有 wall-clock time 的数据使得读者无法评估在实际场景中这些 severity patterns 的相对重要性。\n- 建议：补充至少一个 sparsity level 的 throughput/memory 对比，帮助读者理解 severity-efficiency tradeoff。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式/匿名**: `\\usepackage[review]{acl}` + `\\author{Anonymous}` 正确。未发现内部注释泄露或 deanonymization 信息。脚注提到 \"4× NVIDIA RTX PRO 6000 Blackwell 96GB GPUs\"——需确认此硬件不会间接 deanonymize（极少数实验室有此配置）。\n- **术语一致性**: \"importance discrimination collapse\" 在全文使用一致，无变体问题。\n- **Bib 年份小问题**: `streamingllm-iclr2024` 实际 arXiv 2023 / 会议 2024，可能有 year ambiguity；`adakv-neurips2025` 的 OpenAlex year 为 2024（arXiv 先发），bib 标注为会议年 2025，可接受。\n- **Table/Figure 标注**: 清晰且自含，Table 2 的 footnote 解释了 edge cases。\n\n---\n\n## Missing References\n\n1. **KVzip** (NeurIPS 2025): Query-Agnostic KV Cache Compression with Context Reconstruction — 高度相关的 KV compression work，related work 中未提及\n2. **ShadowKV** (2024): KV Cache in Shadows — long-context LLM 的 KV cache compression，相关但未引用\n3. **MiniCache** (2024): KV Cache Compression in Depth Dimension — 另一种 cache compression 方法\n4. **CritiPrefill** (2024): A Segment-Level Critique Framework for Knowledge Prefilling — 与 phase-aware inference 相关\n5. 论文大量引用 2025-2026 的 arXiv preprints，但遗漏了同期相关的 **HeadInter** (2025, head interaction patterns) 和 **TokenSelect** (2025, token-level selection)\n\n---\n\n## Questions for Authors\n\n1. 能否提供 per-phase 的 Gini delta 数据？aggregate Gini drop <10% 无法解释 15-17× severity divergence，per-phase 数据能否缩小这个 gap？\n2. Crossover 仅在 DeepSeek 上存在——作者是否有 mechanistic explanation 为什么 Qwen 不出现 crossover？是否与 training paradigm (distillation vs instruction tuning) 直接相关？\n3. 如果 importance discrimination collapse 是核心 mechanism，为什么不测试第二种 importance scoring method（如 H2O）来验证 mechanism 的 generality？\n4. LLaMA 实验的 ~1/40 effect size 是否暗示该现象主要是 Qwen2 architecture family 的特性而非 general phenomenon？\n5. 论文声称 \"diagnostic foundation for future phase-aware mitigation\"，但 pilot mitigation failed。作者是否有 insight 为什么 simple budget reallocation 不够？需要什么额外条件？\n\n---\n\n## 主要优势\n\n- **统计严谨性出色**: Nonparametric bootstrap + Wilcoxon + permutation test + Jonckheere-Terpstra + BH-FDR + 多种 robustness checks，远超该领域平均水平\n- **Robustness analysis 全面**: mpl sensitivity, segmentation granularity, asymmetric sparsity, outlier analysis, multiplicative null verification\n- **Honest self-assessment**: Limitations section 坦诚、详尽，正确标注了 exploratory/confirmatory 的区分\n- **Clean experimental design**: 对称 sparsity design 便于解读；additive/multiplicative null 对比增强可信度\n- **Replication across training paradigms**: 在同架构不同训练范式上的复现增加了 validity\n\n---\n\n## Overall Assessment\n\n**Score**: 2.5 — Borderline Findings\n\n**Rationale**: 论文的统计方法和实验执行质量高，但(1)核心发现的 novelty 不足以支撑 EMNLP Main——量化一个直觉可预期的现象不等于揭示新知识；(2)mechanism 存在数量级解释缺口；(3)MUSTAFAR 引用存在严重的标题/作者伪造问题，这是不可接受的学术诚信问题；(4)generalization 局限于 Qwen2 family，crossover 仅 model-specific。建议修正引用问题后投 Findings track。\n\n**Confidence**: 4/5",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## 总体评分\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 统计工作严谨但核心发现的直觉可预期性削弱了 novelty，且关键引用存在严重伪造问题。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨、统计方法得当，但 mechanism 解释力不足（Gini<10% vs severity 15-17×），且 cross-architecture 证据薄弱 |\n| Excitement | 2/5 | 核心发现（attention 稀疏 phase 更脆弱）在直觉上可预期；crossover 仅 model-dependent；无 actionable mitigation |\n| Reproducibility | 4/5 | 详尽的统计报告、robustness checks、多种 segmentation 验证；但代码未公开（\"upon acceptance\"） |\n| Confidence | 4/5 | 熟悉 KV cache compression 和 attention pruning 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 引用 `mustafar-neurips2025` 标题和作者均为伪造\n\n- 具体位置：references.bib `mustafar-neurips2025` 条目；related_work.tex line 18\n- 问题：Bib 条目标题为 \"MUSTAFAR: Multi-Stage Transformer Architecture for Adaptive Reasoning with KV Cache Compression\"，作者为 \"Joo, Wonyong and Kim, Sungmin and Park, Sehyun and Yoo, Kang Min\"。实际论文标题为 \"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\"（Donghyeon Joo, Helya Hosseini, Ramyad Hadidi, Bahar Asgari; NeurIPS 2025）。标题完全编造、作者名全错、论文主题也对不上（实际是 unstructured sparsity pruning，非 \"learned budgets\"）。\n- 为什么影响接收：这是一个典型的 AI 生成幻觉引用——标题、作者、描述均为虚构。严重违反学术诚信；若真实 reviewer 发现此问题，极有可能一票否决。\n- 建议修改方向：(1) 修正为真实标题和作者；(2) 重新评估该引用在 \"learned budgets\" 语境下是否仍然恰当（实际内容是 unstructured sparsity，不是 learned budgets）；(3) 全面审查所有 bib 条目是否存在类似问题。\n\n**N2** [critical] Novelty 不足以支撑 Main Conference\n\n- 具体位置：全文；Introduction §1 line 22 自我定位为 \"diagnostic study\"\n- 问题：\n  - 核心 claim \"compound sparsity severity is phase-dependent\" 在 ThinKV (ICLR 2026) 已知 phase-dependent compression tolerance、Sparse Frontier (2025) 已知 no single strategy dominates across stages、Phase Transition Compression (npj 2026) 已知 joint safe region is intersection of per-dimension zones 之后，直觉上完全可预期。\n  - 论文自比 Voita/Michel 的\"diagnostic study\"传统，但 Voita/Michel 揭示的是**反直觉发现**（大多数 heads 可删无影响），而本文量化的是**符合直觉的预期**（attention 分散的阶段更脆弱）。\n  - Crossover 是唯一可能构成 novelty anchor 的发现，但仅在 DeepSeek 上存在、Qwen 不复现，且 LLaMA 证据极弱（n=49, ~1/40 magnitude），无法作为 generalizable contribution。\n  - 没有 mitigation 方法：pilot gate failed (18% < 30%)，进一步削弱 practical value。\n- 为什么影响接收：对 EMNLP Main 而言，pure characterization 需要揭示 surprising / counter-intuitive 发现或提供 actionable implications。本文的 findings 更适合 Findings track。\n- 建议修改方向：(1) 强化对为何该发现 non-trivial 的论证——仅知道 \"phase matters\" 不等于预测 7.5-79.8× 的量级和 monotonic dose-response；(2) 提供更强的 cross-architecture 证据；(3) 考虑投 Findings。\n\n**N3** [critical] Mechanism 解释力严重不足\n\n- 具体位置：Section 6 (Analysis), §6.1\n- 问题：论文承认 \"both strategies exhibit near-identical Gini drops (<10% difference), yet severity diverges by 15–17×\"。这意味着 importance discrimination collapse 作为 proposed mechanism，存在一个**数量级的解释缺口**。Gini 的 phase-dependence 被声称为 mechanism，但 low-sparsity phase 的 Gini drop 幅度论文未单独量化（只报了 aggregate），无法验证 \"collapse has maximum impact in low-sparsity phases\" 的 claim。\n  - Entropy redistribution 仅在 DeepSeek 上一致，Qwen 仅 2/4 replicates。\n  - 因果验证完全缺失（仅为 correlational）。\n- 为什么影响接收：一篇 diagnostic study 如果 mechanism 部分无法在数量上解释核心 observation，则其 explanatory contribution 大幅削弱。\n- 建议修改方向：(1) 报告 per-phase Gini delta（而非仅 aggregate）以验证 phase-dependence claim；(2) 明确讨论 \"structural specificity\" 能否弥补解释缺口；(3) 降低对 mechanism 解释力的宣称力度。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Cross-architecture 证据过于薄弱却占较大篇幅\n\n- 具体位置：Section 5.4 (§sec:cross-arch), Appendix G\n- 问题：LLaMA 实验 n=49、effect size ~1/40、仅 s=0.30 Bonferroni-corrected significant、power analysis 显示需要 n≥200 才达 0.80 power。本质上这个实验 underpowered 到无法得出有意义结论。但 abstract 和 intro 仍然说 \"exploratory cross-architecture evidence...suggesting the qualitative pattern may extend beyond Qwen2\"，给读者一种 generalization 正在建立的误导印象。\n- 建议：(1) 在 abstract 中删除 LLaMA 相关内容（或明确标注 \"inconclusive\"）；(2) 如果无法 run n≥200，应在正文 Limitations 中更前置地承认。\n\n**W2** [warning] Abstract 信息密度过高\n\n- 具体位置：abstract.tex\n- 问题：9 行 abstract 包含 $G=7.5$–$79.8×$, $\\Delta: 0.39 → 8.48$, $p \\ll 10^{-10}$, $n_{eff}=475$, $s ≥ 0.25$, CI 等大量数字。读者在 abstract 阶段难以消化这些细节。\n- 建议：保留 1-2 个关键数字（如 $G$ 范围），其余移入正文。Abstract 应传递 insight 而非统计细节。\n\n**W3** [warning] 正文可能超 8 页限制\n\n- 具体位置：main.tex sections 1-8 + Limitations + Reproducibility\n- 问题：主体包含 8 个 section（Introduction 到 Conclusion），加上 6 个 subsection 在 Results 中（每个含 table/figure），1 个 table 在 Analysis 中。以 ACL format 11pt、\\small tables 计算，Results 单独就可能占 2.5-3 页。Limitations 约 1.5 页。总计大概率超过 8 页正文限制。\n- 建议：合并 Section 7 (Discussion) 到 Section 8 (Conclusion)；将 §5.4 (Cross-Arch) 和 §5.5 (GSM8K) 完整移入 Appendix。\n\n**W4** [warning] 仅测试一种 importance scoring method\n\n- 具体位置：Section 4, §methodology line 11\n- 问题：KV importance 仅用 position-normalized cumulative attention mass。Discussion §7 声称 \"expect qualitatively similar behavior for H2O, SnapKV, PyramidKV\"，但无实验支撑。不同 scoring methods 可能有不同的 discrimination collapse dynamics。\n- 建议：至少补充一种替代 scoring method（如 H2O 的 heavy-hitter metric）的 spot check，或将泛化声明降级为 hypothesis。\n\n**W5** [warning] Pilot mitigation 失败但仍在正文保留\n\n- 具体位置：Section 7 (Discussion), Appendix §app:pilot-mitigation\n- 问题：Pre-registered gate 30% recovery, actual 18%, heuristic variant 32% 但 CI span zero. 这本质上是一个 negative result，但论文在 Discussion 中仍暗示 \"practical implications for deployment\"。失败的 mitigation 实际上削弱了 \"diagnostic foundation for future phase-aware mitigation\" 的 narrative。\n- 建议：诚实讨论为什么 mitigation failed，这本身可以是有价值的贡献；但不应在 framing 中暗示直接的 deployment value。\n\n**W6** [warning] 缺少 inference throughput/latency 评估\n\n- 具体位置：Limitations §limitations line 19-20\n- 问题：论文在 Limitations 中承认了这一点，但对于一篇关于 \"compound sparsity\" 的论文，完全没有 wall-clock time 的数据使得读者无法评估在实际场景中这些 severity patterns 的相对重要性。\n- 建议：补充至少一个 sparsity level 的 throughput/memory 对比，帮助读者理解 severity-efficiency tradeoff。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式/匿名**: `\\usepackage[review]{acl}` + `\\author{Anonymous}` 正确。未发现内部注释泄露或 deanonymization 信息。脚注提到 \"4× NVIDIA RTX PRO 6000 Blackwell 96GB GPUs\"——需确认此硬件不会间接 deanonymize（极少数实验室有此配置）。\n- **术语一致性**: \"importance discrimination collapse\" 在全文使用一致，无变体问题。\n- **Bib 年份小问题**: `streamingllm-iclr2024` 实际 arXiv 2023 / 会议 2024，可能有 year ambiguity；`adakv-neurips2025` 的 OpenAlex year 为 2024（arXiv 先发），bib 标注为会议年 2025，可接受。\n- **Table/Figure 标注**: 清晰且自含，Table 2 的 footnote 解释了 edge cases。\n\n---\n\n## Missing References\n\n1. **KVzip** (NeurIPS 2025): Query-Agnostic KV Cache Compression with Context Reconstruction — 高度相关的 KV compression work，related work 中未提及\n2. **ShadowKV** (2024): KV Cache in Shadows — long-context LLM 的 KV cache compression，相关但未引用\n3. **MiniCache** (2024): KV Cache Compression in Depth Dimension — 另一种 cache compression 方法\n4. **CritiPrefill** (2024): A Segment-Level Critique Framework for Knowledge Prefilling — 与 phase-aware inference 相关\n5. 论文大量引用 2025-2026 的 arXiv preprints，但遗漏了同期相关的 **HeadInter** (2025, head interaction patterns) 和 **TokenSelect** (2025, token-level selection)\n\n---\n\n## Questions for Authors\n\n1. 能否提供 per-phase 的 Gini delta 数据？aggregate Gini drop <10% 无法解释 15-17× severity divergence，per-phase 数据能否缩小这个 gap？\n2. Crossover 仅在 DeepSeek 上存在——作者是否有 mechanistic explanation 为什么 Qwen 不出现 crossover？是否与 training paradigm (distillation vs instruction tuning) 直接相关？\n3. 如果 importance discrimination collapse 是核心 mechanism，为什么不测试第二种 importance scoring method（如 H2O）来验证 mechanism 的 generality？\n4. LLaMA 实验的 ~1/40 effect size 是否暗示该现象主要是 Qwen2 architecture family 的特性而非 general phenomenon？\n5. 论文声称 \"diagnostic foundation for future phase-aware mitigation\"，但 pilot mitigation failed。作者是否有 insight 为什么 simple budget reallocation 不够？需要什么额外条件？\n\n---\n\n## 主要优势\n\n- **统计严谨性出色**: Nonparametric bootstrap + Wilcoxon + permutation test + Jonckheere-Terpstra + BH-FDR + 多种 robustness checks，远超该领域平均水平\n- **Robustness analysis 全面**: mpl sensitivity, segmentation granularity, asymmetric sparsity, outlier analysis, multiplicative null verification\n- **Honest self-assessment**: Limitations section 坦诚、详尽，正确标注了 exploratory/confirmatory 的区分\n- **Clean experimental design**: 对称 sparsity design 便于解读；additive/multiplicative null 对比增强可信度\n- **Replication across training paradigms**: 在同架构不同训练范式上的复现增加了 validity\n\n---\n\n## Overall Assessment\n\n**Score**: 2.5 — Borderline Findings\n\n**Rationale**: 论文的统计方法和实验执行质量高，但(1)核心发现的 novelty 不足以支撑 EMNLP Main——量化一个直觉可预期的现象不等于揭示新知识；(2)mechanism 存在数量级解释缺口；(3)MUSTAFAR 引用存在严重的标题/作者伪造问题，这是不可接受的学术诚信问题；(4)generalization 局限于 Qwen2 family，crossover 仅 model-specific。建议修正引用问题后投 Findings track。\n\n**Confidence**: 4/5",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-16T02:09:54.536058+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4022
}
```

</details>

---


### Assistant

_source line 664 · 2026-05-16T02:10:02.914944+00:00_

审稿报告已提交给 Review Director。

**审稿核心判断**：评分 2.5（Borderline Findings）。

主要问题：
1. **引用伪造**（critical）：`mustafar-neurips2025` 标题和作者完全虚构，真实论文是关于 unstructured sparsity 而非 "learned budgets"
2. **Novelty 不足**：核心发现（低 sparsity phase 更脆弱）在 ThinKV/Sparse Frontier 之后直觉可预期；crossover 仅 model-specific
3. **Mechanism 解释缺口**：Gini drop <10% 无法解释 15-17× severity divergence
4. **Generalization 薄弱**：实质只在 Qwen2 family 上验证，LLaMA 证据 underpowered

统计执行质量是论文最大优势，建议修正后投 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 665 · 2026-05-16T02:15:45.080166+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

### 总体评分
**Overall**: 2/5 (Weak Reject — Resubmit with substantial revisions)

### Must-Fix 问题

**N1** [critical] "Cross-model replication" 实质是 cross-training-paradigm，不是 cross-architecture
- DeepSeek 和 Qwen 共享 Qwen2ForCausalLM backbone。Contribution 2 声称 "replicates across two Qwen2-architecture models"。唯一跨架构证据 LLaMA n=49，power 0.26-0.63，效应量小 40×。Table 8 中 bootstrap CI 和 Wilcoxon 在不同 sparsity level 上互相矛盾。

**N2** [critical] Phase segmentation 验证过于薄弱，存在 construct validity 隐患
- κ 验证仅 DeepSeek GSM8K n=48。Qwen 完全没有验证。MATH-500 也没有验证。
- 潜在循环论证：低稀疏度阶段 = 注意力分散 → eviction 对分散注意力伤害本来就大。
- Segmentation 仅检查了 tercile/quartile/quintile，没有 sliding window 等。

**N3** [critical] MUSTAFAR 引用标题伪造
- 实际标题为 "Promoting Unstructured Sparsity"，论文引用为 "Multi-Stage Transformer Architecture for Adaptive Reasoning"，首字母缩写展开完全虚构。

### Should-Fix 问题

**W1** [warning] 仅 4 个 sparsity level 不足以支撑 dose-response claim
- 4 点无法区分线性/指数/阶梯状关系。Figure 1 连续线连接离散点暗示未验证的连续关系。

**W2** [warning] G 指标两种定义差异巨大（7.5× vs 69×），解释不充分
- Per-problem G vs ratio-of-medians G 差异 3.4-5.6×，未充分解释原因。

**W3** [warning] PPL-based II 与下游 accuracy 之间的 construct validity gap
- 93.2% answer tokens 在 G≈1 区域。"Silent reasoning errors" 是推测。
- Accuracy degradation 在 s≤0.20 主要由 truncation 驱动。

**W4** [warning] Bonferroni correction 的 family 定义不一致
- 不同 section 的 family 独立定义，存在 multiplicity 问题。

**W5** [warning] Bootstrap CI 与 Wilcoxon test 在 LLaMA 上系统性矛盾

**W6** [warning] GSM8K cross-benchmark validation 缺少 power analysis
- n=50 无 power analysis。Qwen truncation 问题。DeepSeek language switching confound。

### Missing References
Sparse Sinkhorn Attention (Tay et al., 2020), CoT faithfulness (Lanham et al., 2023; Turpin et al., 2023), Wanda (Sun et al., 2024), SparseGPT (Frantar & Alistarh, 2023)

### Questions for Authors
1. Phase segmentation circularity: 如何区分 compound interaction 的 phase-dependence 和 individual effect 的 phase-dependence？
2. G 指标 II_high ≈ 0 时 denominator explosion 问题？
3. LLaMA 效应量差 40× 的原因？
4. Language switching confound 是否存在于 MATH-500？
5. 93.2% answer tokens 在 G≈1 区域——phase-aware mitigation 的价值何在？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-16T02:17:40.239342+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应：逐条回应 Reviewer 1 意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1**: \"Cross-model replication\" 实质是 cross-training-paradigm\n\n同意。论文 Introduction §1 Contribution 2 措辞为 \"replicates across two Qwen2-architecture models\"，这在技术上准确但具有误导性——共享 Qwen2ForCausalLM 的 28L/28H/4-group GQA backbone 意味着 attention pattern 的底层结构高度相似。真正的 cross-architecture 证据仅有 LLaMA n=49，效应量 ~1/40，且 Table 8 中 s=0.15 的 CI excludes zero 但 Wilcoxon p_Bonf=0.219（non-sig），而 s=0.30 CI spans zero 但 Wilcoxon p_Bonf=0.029（sig）——系统性矛盾。论文虽在 Appendix G footnote 解释了 CI/Wilcoxon 分歧（heavy-tailed + small n），但这恰恰说明 n=49 不足以支撑任何 cross-architecture claim。\n\n补充：我在自己的审稿中也标注了此问题（R2-W1），认为 abstract 中提及 LLaMA 证据给读者制造了 generalization 正在建立的误导印象。\n\n**[AGREE] R1-N2**: Phase segmentation 验证过于薄弱 + 潜在循环论证\n\n同意验证不足的判断。κ=0.887 仅来自 DeepSeek GSM8K n=48，在 Qwen 和主要 benchmark MATH-500 上完全缺乏验证（§app:think-validation 明确承认 \"Qwen does not produce explicit reasoning delimiters, precluding the same validation\"）。\n\n**但对 circularity 论点我部分保留**：Reviewer 1 指出 \"低稀疏度阶段 = 注意力分散 → eviction 对分散注意力伤害本来就大\" 是一个 tautological concern。我认为论文的 **crossover 发现**（§5.3）在一定程度上 breaks 这个 circularity：如果 phase-dependence 纯粹是 attention distribution 的直接机械后果，那么 importance-based 和 random eviction 应该表现相似（分散注意力对任何 eviction 策略都更脆弱）。但实际上 random eviction 的 phase gradient 比 importance-based 弱 15-17×（Table 1），且存在 strategy ranking reversal。这说明 phase-modulated severity 不仅仅是 attention distribution 的 trivial 后果，而是一个 strategy-specific interaction。\n\n不过，这个辩护仅在 Qwen2 family 上成立；在 LLaMA 上 random eviction 也有 non-trivial phase gradient (d_z: 0.35→0.44)，strategy contrast 大幅减弱——恰恰支持了 R1 的 concern 在某些架构上可能成立。\n\n**[AGREE] R1-N3**: MUSTAFAR 引用标题伪造\n\n完全同意。我在自己的审稿中也将此列为 N1 critical issue。标题 \"Multi-Stage Transformer Architecture for Adaptive Reasoning with KV Cache Compression\" 完全虚构——真实标题为 \"Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\"；作者名也全错（Wonyong Joo → Donghyeon Joo；其余共同作者全部不同）。这是不可接受的 fabricated citation。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1**: 4 个 sparsity levels 不足以确定 functional form\n\n同意。Jonckheere-Terpstra test 能确认 monotonicity，但 4 个离散点无法区分 linear/exponential/step-function/saturation 行为。Figure 1 用连续线连接 4 个点暗示了未经验证的平滑关系。论文 Limitations 中承认了 \"insufficient to characterize the functional form of G(s)\"（limitations.tex line 20），但这个限制应在 Results section 就明确说明，而非仅放在 Limitations 中。\n\n补充：从 Table 2 数据看（Δ: 0.39, 1.21, 3.99, 8.48），增长模式接近 exponential（每 0.05 步大约 ×3），但这只是 4 点的 pattern，等间距 sampling 无法排除 threshold 行为。\n\n**[REBUT] R1-W2**: G 指标两种定义差异巨大\n\n部分不同意 severity 判断。论文确实在 Table 5 caption 中解释了差异来源：\"per-problem ratios are sensitive to near-zero II_high values\"——当 II_high ≈ 0 时，per-problem ratio explodes。主文使用的是 per-problem median（Eq. 3, G=7.5×），而 Table 5 的 69× 是 ratio-of-medians（仅为 profiling subset reference）。\n\n关键是论文明确声明 Δ（paired median difference）为 primary metric，G 为 auxiliary（§4 line 18: \"the paired median difference Δ is primary\"）。因此 G 的两种定义差异虽大，但不影响核心结论（Δ 从 0.39 到 8.48 是 robust 且 definition-invariant 的）。\n\n我认为问题在于 **presentation**：abstract 和 intro 强调 \"G=7.5–79.8×\" 吸引眼球，但主文的 primary metric 其实是 Δ。如果 G 是 auxiliary，就不应该在 abstract 中占 headline 位置。\n\n**[AGREE] R1-W3**: PPL-based II 与 downstream accuracy 的 construct validity gap\n\n同意这是一个 gap，但认为论文在 §5.8 已做了 partial mitigation。具体而言：\n\n- 93.2% answer tokens 在 G≈1 区域——这确实暗示 phase-aware compression 对 answer quality 的直接影响有限。\n- \"Silent reasoning errors\" 是推测（论文用了 \"may\"），但 Qwen 的 accuracy 数据（truncation ≤4%, δ=-4 to -27pp; Table 10）确实证明存在非 truncation 驱动的 reasoning quality degradation。\n- DeepSeek s≤0.20 的 degradation 确实是 truncation-dominated（non-truncated accuracy 68-71% vs dense 88%），R1 的 criticism 在此范围内成立。\n\n总体而言，PPL-based severity 和 accuracy degradation 之间的 non-linear mapping（Qwen: gradual until cliff at s=0.30）削弱了 \"severity gradient → practical consequence\" 的直接 narrative。\n\n**[AGREE] R1-W4**: Bonferroni correction family 定义不一致\n\n同意存在 multiplicity 问题。论文的 Bonferroni 按 \"model×strategy combination, 4 sparsity levels\" 定义 k=4（§4 line 18），但实际上跨 model、跨 strategy、跨 sparsity 的比较形成了更大的 test family。Appendix §app:bh-fdr 的 BH-FDR across all 44 tests 确实 partially addresses 这一问题（all Bonferroni-significant results survive BH-FDR），但主文中 family 定义的不一致是一个 valid concern。\n\n对核心结论影响有限：即使用最保守的全局 Bonferroni（k=44），importance-based 的 p 值在 $10^{-10}$ 量级，仍然显著。问题主要存在于 random eviction 在 s=0.25 附近的 marginal cases。\n\n**[AGREE] R1-W5**: Bootstrap CI 与 Wilcoxon 在 LLaMA 上系统性矛盾\n\n同意。如前在 R1-N1 回应中所述，Table 8 的矛盾模式（s=0.15: CI excludes zero but Wilcoxon ns; s=0.30: CI spans zero but Wilcoxon sig）本质上说明 n=49 + heavy-tailed distribution 下两种方法的 power profile 不同。论文的 footnote 解释合理（percentile bootstrap 对 tail 不敏感，Wilcoxon 使用 signed ranks 对 tail 敏感），但这恰恰证明该 sample size 不足以产生一致结论。这个矛盾本身就应被解读为 \"evidence is inconclusive\"，而非论文目前的 \"partially confirms\"。\n\n**[REBUT] R1-W6**: GSM8K cross-benchmark validation 缺少 power analysis\n\n部分反驳。虽然 n=50 确实缺少 formal power analysis，但 DeepSeek importance-based eviction 在 GSM8K 上 all 4 sparsity levels 显著（p ≤ 0.0003, Wilcoxon; Table 12），effect size 足够大（Δ: 0.24→4.68）。对于 confirmatory replication，observed significance 本身就是 power 充足的后验证据。\n\n但对于 **random eviction 的 null results**，缺少 power analysis 确实是一个问题——无法区分 \"真的无效应\" 和 \"power 不足以检测弱效应\"。论文应为 random eviction 的 null results 提供 power analysis（或至少报告 detectable effect size at 0.80 power given n=50）。\n\nQwen truncation 和 DeepSeek language switching 确实是 confounds，论文也承认了前者（Table 13 注释）。\n\n---\n\n### Missing References 回应\n\n**[REBUT] Sparse Sinkhorn Attention (Tay et al., 2020)**: 该论文关于 learnable sparse attention patterns（training-time），与本文关注的 inference-time KV cache eviction / head pruning 是不同问题域。引用可选但非必需。\n\n**[AGREE] CoT faithfulness (Lanham et al., 2023; Turpin et al., 2023)**: 同意应引用。论文在 §5.7 提出 \"silent reasoning errors\" 概念（\"correct formatting with corrupted intermediate logic\"），这正是 CoT faithfulness 文献讨论的核心问题。不引用这些工作是一个疏漏。\n\n**[REBUT] Wanda (Sun et al., 2024) / SparseGPT (Frantar & Alistarh, 2023)**: 这些是 weight pruning methods（one-shot structured/unstructured pruning），与本文的 inference-time attention head pruning + KV cache eviction 是不同层面的 compression。Related work §2 paragraph 1 已引用了 compound compression 的相关文献（SLiM, UniComp, GRASPrune 等），这些更直接相关。Wanda/SparseGPT 属于 \"broader compression landscape\" 但不构成 missing critical reference。\n\n---\n\n### Questions for Authors 回应\n\n**Q1 (Phase segmentation circularity)**: 如上 R1-N2 回应所述，crossover 发现 partially 打破了 circularity——如果 phase-dependence 是纯机械后果，random 和 importance 应该相似。但 R1 的 concern 在 LLaMA 上部分成立（strategy contrast 减弱），说明 circularity 程度可能是 architecture-dependent。\n\n**Q2 (G denominator explosion)**: 论文用 per-problem median G 而非 per-problem mean G，且以 Δ 为 primary metric，合理地 mitigates 了 denominator 接近 0 时 ratio explosion 的问题。但 abstract/intro 仍 headline G 值，创造了一种 inflated impression。\n\n**Q3 (LLaMA 效应量差 40×)**: 论文未给出 mechanistic explanation。可能原因包括：(1) LlamaForCausalLM 的 head specialization 结构不同（RoPE implementation 差异、GQA group 数不同）；(2) DeepSeek-R1-Distill-Llama-8B 的 distillation 可能未充分继承 phase structure。论文应讨论这一点。\n\n**Q4 (Language switching)**: 论文报告 language switching 仅在 max_new_tokens=2048 下测量（Appendix §app:accuracy-details footnote），未在 MATH-500 primary analysis（也用 2048 tokens）下系统评估。应确认 PPL 计算是否受中文 token 影响。\n\n**Q5 (93.2% answer tokens in G≈1)**: 有效质疑。如果 severity 集中在 reasoning trace 而非 answer，且论文没有证明 trace degradation → answer quality degradation 的 causal path（仅有 correlational accuracy evidence），那么 \"diagnostic foundation for phase-aware mitigation\" 的 practical motivation 确实被削弱。论文的 Qwen accuracy data (truncation ≤4%) 提供了一些支撑，但 correlation ≠ per-phase causation。\n\n---\n\n### 总结\n\n与 Reviewer 1 的 3 个 Must-Fix 中，我完全同意 2 个（N1 cross-architecture, N3 MUSTAFAR），对 N2 (circularity) 部分同意但认为 crossover 发现提供了 partial defense。6 个 Should-Fix 中我同意 4 个（W1, W3, W4, W5），对 W2 和 W6 部分反驳。\n\n综合两位 reviewer 的意见，核心问题集中在：(1) novelty/excitement 不足；(2) generalization 局限于 Qwen2；(3) MUSTAFAR 引用伪造。建议 Findings track + 修正引用后重投。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应：逐条回应 Reviewer 1 意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1**: \"Cross-model replication\" 实质是 cross-training-paradigm\n\n同意。论文 Introduction §1 Contribution 2 措辞为 \"replicates across two Qwen2-architecture models\"，这在技术上准确但具有误导性——共享 Qwen2ForCausalLM 的 28L/28H/4-group GQA backbone 意味着 attention pattern 的底层结构高度相似。真正的 cross-architecture 证据仅有 LLaMA n=49，效应量 ~1/40，且 Table 8 中 s=0.15 的 CI excludes zero 但 Wilcoxon p_Bonf=0.219（non-sig），而 s=0.30 CI spans zero 但 Wilcoxon p_Bonf=0.029（sig）——系统性矛盾。论文虽在 Appendix G footnote 解释了 CI/Wilcoxon 分歧（heavy-tailed + small n），但这恰恰说明 n=49 不足以支撑任何 cross-architecture claim。\n\n补充：我在自己的审稿中也标注了此问题（R2-W1），认为 abstract 中提及 LLaMA 证据给读者制造了 generalization 正在建立的误导印象。\n\n**[AGREE] R1-N2**: Phase segmentation 验证过于薄弱 + 潜在循环论证\n\n同意验证不足的判断。κ=0.887 仅来自 DeepSeek GSM8K n=48，在 Qwen 和主要 benchmark MATH-500 上完全缺乏验证（§app:think-validation 明确承认 \"Qwen does not produce explicit reasoning delimiters, precluding the same validation\"）。\n\n**但对 circularity 论点我部分保留**：Reviewer 1 指出 \"低稀疏度阶段 = 注意力分散 → eviction 对分散注意力伤害本来就大\" 是一个 tautological concern。我认为论文的 **crossover 发现**（§5.3）在一定程度上 breaks 这个 circularity：如果 phase-dependence 纯粹是 attention distribution 的直接机械后果，那么 importance-based 和 random eviction 应该表现相似（分散注意力对任何 eviction 策略都更脆弱）。但实际上 random eviction 的 phase gradient 比 importance-based 弱 15-17×（Table 1），且存在 strategy ranking reversal。这说明 phase-modulated severity 不仅仅是 attention distribution 的 trivial 后果，而是一个 strategy-specific interaction。\n\n不过，这个辩护仅在 Qwen2 family 上成立；在 LLaMA 上 random eviction 也有 non-trivial phase gradient (d_z: 0.35→0.44)，strategy contrast 大幅减弱——恰恰支持了 R1 的 concern 在某些架构上可能成立。\n\n**[AGREE] R1-N3**: MUSTAFAR 引用标题伪造\n\n完全同意。我在自己的审稿中也将此列为 N1 critical issue。标题 \"Multi-Stage Transformer Architecture for Adaptive Reasoning with KV Cache Compression\" 完全虚构——真实标题为 \"Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\"；作者名也全错（Wonyong Joo → Donghyeon Joo；其余共同作者全部不同）。这是不可接受的 fabricated citation。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1**: 4 个 sparsity levels 不足以确定 functional form\n\n同意。Jonckheere-Terpstra test 能确认 monotonicity，但 4 个离散点无法区分 linear/exponential/step-function/saturation 行为。Figure 1 用连续线连接 4 个点暗示了未经验证的平滑关系。论文 Limitations 中承认了 \"insufficient to characterize the functional form of G(s)\"（limitations.tex line 20），但这个限制应在 Results section 就明确说明，而非仅放在 Limitations 中。\n\n补充：从 Table 2 数据看（Δ: 0.39, 1.21, 3.99, 8.48），增长模式接近 exponential（每 0.05 步大约 ×3），但这只是 4 点的 pattern，等间距 sampling 无法排除 threshold 行为。\n\n**[REBUT] R1-W2**: G 指标两种定义差异巨大\n\n部分不同意 severity 判断。论文确实在 Table 5 caption 中解释了差异来源：\"per-problem ratios are sensitive to near-zero II_high values\"——当 II_high ≈ 0 时，per-problem ratio explodes。主文使用的是 per-problem median（Eq. 3, G=7.5×），而 Table 5 的 69× 是 ratio-of-medians（仅为 profiling subset reference）。\n\n关键是论文明确声明 Δ（paired median difference）为 primary metric，G 为 auxiliary（§4 line 18: \"the paired median difference Δ is primary\"）。因此 G 的两种定义差异虽大，但不影响核心结论（Δ 从 0.39 到 8.48 是 robust 且 definition-invariant 的）。\n\n我认为问题在于 **presentation**：abstract 和 intro 强调 \"G=7.5–79.8×\" 吸引眼球，但主文的 primary metric 其实是 Δ。如果 G 是 auxiliary，就不应该在 abstract 中占 headline 位置。\n\n**[AGREE] R1-W3**: PPL-based II 与 downstream accuracy 的 construct validity gap\n\n同意这是一个 gap，但认为论文在 §5.8 已做了 partial mitigation。具体而言：\n\n- 93.2% answer tokens 在 G≈1 区域——这确实暗示 phase-aware compression 对 answer quality 的直接影响有限。\n- \"Silent reasoning errors\" 是推测（论文用了 \"may\"），但 Qwen 的 accuracy 数据（truncation ≤4%, δ=-4 to -27pp; Table 10）确实证明存在非 truncation 驱动的 reasoning quality degradation。\n- DeepSeek s≤0.20 的 degradation 确实是 truncation-dominated（non-truncated accuracy 68-71% vs dense 88%），R1 的 criticism 在此范围内成立。\n\n总体而言，PPL-based severity 和 accuracy degradation 之间的 non-linear mapping（Qwen: gradual until cliff at s=0.30）削弱了 \"severity gradient → practical consequence\" 的直接 narrative。\n\n**[AGREE] R1-W4**: Bonferroni correction family 定义不一致\n\n同意存在 multiplicity 问题。论文的 Bonferroni 按 \"model×strategy combination, 4 sparsity levels\" 定义 k=4（§4 line 18），但实际上跨 model、跨 strategy、跨 sparsity 的比较形成了更大的 test family。Appendix §app:bh-fdr 的 BH-FDR across all 44 tests 确实 partially addresses 这一问题（all Bonferroni-significant results survive BH-FDR），但主文中 family 定义的不一致是一个 valid concern。\n\n对核心结论影响有限：即使用最保守的全局 Bonferroni（k=44），importance-based 的 p 值在 $10^{-10}$ 量级，仍然显著。问题主要存在于 random eviction 在 s=0.25 附近的 marginal cases。\n\n**[AGREE] R1-W5**: Bootstrap CI 与 Wilcoxon 在 LLaMA 上系统性矛盾\n\n同意。如前在 R1-N1 回应中所述，Table 8 的矛盾模式（s=0.15: CI excludes zero but Wilcoxon ns; s=0.30: CI spans zero but Wilcoxon sig）本质上说明 n=49 + heavy-tailed distribution 下两种方法的 power profile 不同。论文的 footnote 解释合理（percentile bootstrap 对 tail 不敏感，Wilcoxon 使用 signed ranks 对 tail 敏感），但这恰恰证明该 sample size 不足以产生一致结论。这个矛盾本身就应被解读为 \"evidence is inconclusive\"，而非论文目前的 \"partially confirms\"。\n\n**[REBUT] R1-W6**: GSM8K cross-benchmark validation 缺少 power analysis\n\n部分反驳。虽然 n=50 确实缺少 formal power analysis，但 DeepSeek importance-based eviction 在 GSM8K 上 all 4 sparsity levels 显著（p ≤ 0.0003, Wilcoxon; Table 12），effect size 足够大（Δ: 0.24→4.68）。对于 confirmatory replication，observed significance 本身就是 power 充足的后验证据。\n\n但对于 **random eviction 的 null results**，缺少 power analysis 确实是一个问题——无法区分 \"真的无效应\" 和 \"power 不足以检测弱效应\"。论文应为 random eviction 的 null results 提供 power analysis（或至少报告 detectable effect size at 0.80 power given n=50）。\n\nQwen truncation 和 DeepSeek language switching 确实是 confounds，论文也承认了前者（Table 13 注释）。\n\n---\n\n### Missing References 回应\n\n**[REBUT] Sparse Sinkhorn Attention (Tay et al., 2020)**: 该论文关于 learnable sparse attention patterns（training-time），与本文关注的 inference-time KV cache eviction / head pruning 是不同问题域。引用可选但非必需。\n\n**[AGREE] CoT faithfulness (Lanham et al., 2023; Turpin et al., 2023)**: 同意应引用。论文在 §5.7 提出 \"silent reasoning errors\" 概念（\"correct formatting with corrupted intermediate logic\"），这正是 CoT faithfulness 文献讨论的核心问题。不引用这些工作是一个疏漏。\n\n**[REBUT] Wanda (Sun et al., 2024) / SparseGPT (Frantar & Alistarh, 2023)**: 这些是 weight pruning methods（one-shot structured/unstructured pruning），与本文的 inference-time attention head pruning + KV cache eviction 是不同层面的 compression。Related work §2 paragraph 1 已引用了 compound compression 的相关文献（SLiM, UniComp, GRASPrune 等），这些更直接相关。Wanda/SparseGPT 属于 \"broader compression landscape\" 但不构成 missing critical reference。\n\n---\n\n### Questions for Authors 回应\n\n**Q1 (Phase segmentation circularity)**: 如上 R1-N2 回应所述，crossover 发现 partially 打破了 circularity——如果 phase-dependence 是纯机械后果，random 和 importance 应该相似。但 R1 的 concern 在 LLaMA 上部分成立（strategy contrast 减弱），说明 circularity 程度可能是 architecture-dependent。\n\n**Q2 (G denominator explosion)**: 论文用 per-problem median G 而非 per-problem mean G，且以 Δ 为 primary metric，合理地 mitigates 了 denominator 接近 0 时 ratio explosion 的问题。但 abstract/intro 仍 headline G 值，创造了一种 inflated impression。\n\n**Q3 (LLaMA 效应量差 40×)**: 论文未给出 mechanistic explanation。可能原因包括：(1) LlamaForCausalLM 的 head specialization 结构不同（RoPE implementation 差异、GQA group 数不同）；(2) DeepSeek-R1-Distill-Llama-8B 的 distillation 可能未充分继承 phase structure。论文应讨论这一点。\n\n**Q4 (Language switching)**: 论文报告 language switching 仅在 max_new_tokens=2048 下测量（Appendix §app:accuracy-details footnote），未在 MATH-500 primary analysis（也用 2048 tokens）下系统评估。应确认 PPL 计算是否受中文 token 影响。\n\n**Q5 (93.2% answer tokens in G≈1)**: 有效质疑。如果 severity 集中在 reasoning trace 而非 answer，且论文没有证明 trace degradation → answer quality degradation 的 causal path（仅有 correlational accuracy evidence），那么 \"diagnostic foundation for phase-aware mitigation\" 的 practical motivation 确实被削弱。论文的 Qwen accuracy data (truncation ≤4%) 提供了一些支撑，但 correlation ≠ per-phase causation。\n\n---\n\n### 总结\n\n与 Reviewer 1 的 3 个 Must-Fix 中，我完全同意 2 个（N1 cross-architecture, N3 MUSTAFAR），对 N2 (circularity) 部分同意但认为 crossover 发现提供了 partial defense。6 个 Should-Fix 中我同意 4 个（W1, W3, W4, W5），对 W2 和 W6 部分反驳。\n\n综合两位 reviewer 的意见，核心问题集中在：(1) novelty/excitement 不足；(2) generalization 局限于 Qwen2；(3) MUSTAFAR 引用伪造。建议 Findings track + 修正引用后重投。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-16T02:17:44.278740+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4039
}
```

</details>

---


### Assistant

_source line 668 · 2026-05-16T02:17:52.524063+00:00_

交叉回应已提交。总结：

- **R1-N1 (cross-architecture)**: AGREE — 两个主模型共享 Qwen2 backbone，LLaMA 证据不足
- **R1-N2 (circularity)**: 部分 AGREE — 验证确实不足，但 crossover 发现能 partially 打破循环论证
- **R1-N3 (MUSTAFAR)**: AGREE — 与我自己的 N1 发现一致
- **R1-W1~W6**: 同意 4 个，对 W2 (G metric) 和 W6 (GSM8K power) 部分反驳

两位 reviewer 的核心共识：novelty 不够 Main Conference、generalization 局限于 Qwen2、MUSTAFAR 引用伪造不可接受。建议 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---
