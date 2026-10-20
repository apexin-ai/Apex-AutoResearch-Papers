# paper writing results reframe

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_results_reframe_20260520T105818.jsonl`
- **Structured JSON:** [`6b86a8c3235d18d11c9d.json`](../../sessions/6b/6b86a8c3235d18d11c9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-20T11:05:28.963649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T11:05:28.964243+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T11:05:28.964508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T11:05:28.965000+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across six contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:method_sensitivity}, \S\ref{sec:regime}, and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; $\alpha{=}0.10$ uses a single seed (42, preliminary).
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical s
…[truncated 52107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T11:05:28.965437+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T11:05:28.965601+00:00_

abstract.tex
appendix.tex
background.tex
conclusion.tex
discussion.tex
ethics.tex
experiments.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T11:05:28.965765+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
  "content": "\\subsection{Detection Phase Transition}\n\\label{sec:regime}\n\nDiversity collapse occurs at every contamination level: distinct-1 declines by $14.1\\%$ at $\\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\\pm}0.3\\%$ at $\\alpha{=}0.25$ (3-seed mean).\nDespite this ubiquitous degradation, causal detectability is sharply regime-dependent.\nPermutation Granger (PermG) tests find 0/8 canary$\\to$downstream pairs FDR-significant from $\\alpha{=}0.00$ through $\\alpha{=}0.45$, then jump to 6/8 at $\\alpha{=}0.50$ (2~fp32 seeds, consistent).\nThis transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\\alpha)^{10}$ yields $99.75\\%$ at $\\alpha{=}0.45$ versus $99.90\\%$ at $\\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.\nSigmoid regression across the 12-point $\\alpha$ grid quantifies this steep onset: $\\alpha_c = 0.476$ at $T{=}10$, steepness $k \\geq 200$, transition width $\\Delta\\alpha \\approx 0.02$, $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\\Delta\\mathrm{AIC} = 18.2$; Figure~\\ref{fig:phase_transition}).\nAt $\\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\\alpha_c$ at $T{=}10$ (\\S\\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.\nA specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.\n\nFirst-differencing scopes the canary claim precisely.\nCanary$\\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \\to 24/24$ across 4~seeds at $\\alpha{=}1.0$), while canary$\\to$perplexity collapses entirely ($F \\approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.\nAll canary claims are therefore scoped to diversity metrics only.\nAt $\\alpha{=}1.0$, 24/24 forward-direction pairs reach FDR significance with 0/24 reverse (4~seeds); directional asymmetry is robust across all WikiText conditions.\nThe canary mechanism also exhibits a blind spot: at $\\alpha{=}0.10$, distinct-1 has already dropped by $39.6\\%$, yet token entropy is indistinguishable from the null ($-5.3\\%$ versus $-4.6{\\pm}0.4\\%$ at $\\alpha{=}0.0$).\nBelow $\\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable causal signal in the canary metrics.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\n\\subsection{Dose-Response and the $S \\times R$ Framework}\n\\label{sec:dose_response}\n\nThe PermG dose-response profile (Figure~\\ref{fig:regime_map}) reveals four detection regimes: \\emph{blind} ($\\alpha \\leq 0.45$, 0/8 FDR-significant pairs), \\emph{onset} ($\\alpha \\approx 0.50$, 6/8), \\emph{synchronous dip} ($\\alpha \\approx 0.60$, s42: 3/8, s43: 0/8; dual-seed confirmed), and \\emph{detection} ($\\alpha \\geq 0.75$, 5--6/8 per seed across 3~seeds; $\\alpha{=}1.0$, 6/8 across 4~seeds).\nThe non-monotonic dip at $\\alpha{=}0.60$ is consistent with the $S \\times R$ framework (\\S\\ref{sec:theory}): signal strength $S(\\alpha)$ rises monotonically with contamination, but temporal resolution $R(\\alpha)$ drops when relaxation time approaches the observation interval.\nAt $\\alpha \\approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \\times R$ reaches a local minimum.\nThe synchronous zone is mechanistically distinct from the blind spot: in the blind zone, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.\n\nMethod choice is itself a major source of analytic variability.\nAt $\\alpha{=}1.0$, forward-direction significance rates range from 100\\% (naive cross-correlation) to 37.5\\% (PermG), with inter-method $\\kappa = 0.185$ (near chance) and a spurious rate of at least 62.5\\%.\nPermG is the only method that combines zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$ (Table~\\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.\nThe $S \\times R$ framework generates three testable predictions for $T{=}20$ via $\\mathrm{Power}(\\alpha, T) = \\Phi(S \\cdot R \\cdot \\sqrt{T}/\\sigma)$: (i)~$\\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\\alpha_c$ values.\nThese predictions are under empirical verification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\caption{PermG forward detection rate across 12 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\\alpha \\leq 0.45$, 0/8), onset ($\\alpha{=}0.50$, 6/8), synchronous dip ($\\alpha{=}0.60$, 0--3/8), and detection ($\\alpha \\geq 0.75$, 5--6/8).}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Forward-direction FDR significance rates (\\%) across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG achieves zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr          & 75   & 12.5 & 37.5 & 87.5 & 0    & 75  \\\\\nDiff.\\ XCorr         & 0    & 37.5 & 87.5 & 75   & 75   & 0   \\\\\nThreshold ($3\\sigma$) & ---  & 0    & 50   & 0    & 0    & --- \\\\\nPerm.\\ Granger       & 0    & 0    & 75   & 75   & 75   & 0   \\\\\nToda--Yamamoto       & ---  & 0    & 37.5 & 37.5 & 50   & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture Generalization}\n\\label{sec:generalization}\n\nWe evaluate the detection phase transition across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).\nTable~\\ref{tab:generalization} reports PermG forward detection at $\\alpha{=}1.0$.\nPermG forward significance reaches ${\\geq}$6/8 in 13 of 15 conditions (87\\%).\nTwo exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\\to$downstream pairs reach significance while entropy$\\to$downstream pairs fail entirely (0/4; details in Appendix).\nSmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.\nThe onset boundary $\\alpha_c \\approx 0.50$ at $T{=}10$ is architecture-independent: every family that achieves detection does so at or above this threshold, and none achieves reliable detection below it.\n\nReplacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.\nAt Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.\nDataset characteristics modulate detection power independently of model capacity.\nDirectional asymmetry also varies by domain: at $\\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.\nThis domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\\S\\ref{sec:discussion}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture PermG forward detection ($\\alpha{=}1.0$). Detection (${\\geq}$6/8) confirmed in 13/15 conditions (87\\%) across six model families, scales from 345M to 6.9B, and two domains.}\n\\label{tab:generalization}\n\\begin{tabular}{lrcl}\n\\toprule\nModel & Params & Domain & PermG fwd \\\\\n\\midrule\nPythia-410M    & 410M & Wiki & 6/8 \\\\\nPythia-1.4B    & 1.4B & Wiki & 2--6/8$^\\dagger$ \\\\\nPythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\\\\nGPT-2-medium   & 345M & Wiki & 6/8 \\\\\nOPT-1.3B       & 1.3B & Wiki & 6/8 \\\\\nQwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\\\\nSmolLM3-3B     & 3.0B & Wiki & 3/8$^\\ddagger$ \\\\\nPadding-410M   & 410M & Wiki & 6/8 \\\\\n\\addlinespace\nPythia-1B      & 1.0B & C4   & 7--8/8 \\\\\nPythia-1.4B    & 1.4B & C4   & 8/8 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^\\ddagger$ECE-only canary (entropy 0/4).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\\\\n\\multicolumn{4}{l}{\\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Others: single seed. Total: 15 combinations.} \\\\\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Canary-Based Early Intervention}\n\\label{sec:intervention}\n\nWe implement a predictive cessation protocol: training with synthetic data ($\\alpha{=}1.0$) continues until token entropy drops ${>}15\\%$ relative to generation~0, at which point $\\alpha$ switches to $0.0$ (pure real data).\nA reactive baseline triggers when distinct-1 drops ${>}10\\%$.\nThe predictive trigger fires at generation~1 in both Pythia-410M and Pythia-1.4B (s42 fp32), one generation before the reactive baseline (generation~2).\nPeak perplexity under predictive intervention is $56.99$ versus $157.09$ under reactive (s42 fp32), a 58\\% reduction (bootstrap 95\\% CI: 29--64\\%).\nRecovery occurs at generation~2 under predictive cessation versus generation~4 under reactive.\nBoth models converge to the $\\alpha{=}0.0$ baseline by generation~10.\n\nThe trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\\times$ scale gap from 410M to 1.4B, and the 15\\% entropy threshold generalizes without recalibration.\nThese results position canary-based detection within a four-layer taxonomy of collapse monitoring: (1)~dimensionality collapse, detectable at $\\alpha \\geq 0.10$ via $n$-gram diversity decline; (2)~distributional variance, detectable at $\\alpha \\geq 0.25$ via calibration drift; (3)~causal coupling, detectable at $\\alpha \\geq 0.50$ via Granger precedence; and (4)~dynamical stability, assessable at $\\alpha \\geq 0.50$ via lag structure.\nEach layer captures a distinct aspect of collapse, and lower layers activate at lower contamination thresholds.\nThe practical implication is that canary monitoring should combine multiple detection layers rather than rely on any single statistical test.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
    "content": "\\subsection{Detection Phase Transition}\n\\label{sec:regime}\n\nDiversity collapse occurs at every contamination level: distinct-1 declines by $14.1\\%$ at $\\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\\pm}0.3\\%$ at $\\alpha{=}0.25$ (3-seed mean).\nDespite this ubiquitous degradation, causal detectability is sharply regime-dependent.\nPermutation Granger (PermG) tests find 0/8 canary$\\to$downstream pairs FDR-significant from $\\alpha{=}0.00$ through $\\alpha{=}0.45$, then jump to 6/8 at $\\alpha{=}0.50$ (2~fp32 seeds, consistent).\nThis transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\\alpha)^{10}$ yields $99.75\\%$ at $\\alpha{=}0.45$ versus $99.90\\%$ at $\\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.\nSigmoid regression across the 12-point $\\alpha$ grid quantifies this steep onset: $\\alpha_c = 0.476$ at $T{=}10$, steepness $k \\geq 200$, transition width $\\Delta\\alpha \\approx 0.02$, $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\\Delta\\mathrm{AIC} = 18.2$; Figure~\\ref{fig:phase_transition}).\nAt $\\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\\alpha_c$ at $T{=}10$ (\\S\\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.\nA specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.\n\nFirst-differencing scopes the canary claim precisely.\nCanary$\\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \\to 24/24$ across 4~seeds at $\\alpha{=}1.0$), while canary$\\to$perplexity collapses entirely ($F \\approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.\nAll canary claims are therefore scoped to diversity metrics only.\nAt $\\alpha{=}1.0$, 24/24 forward-direction pairs reach FDR significance with 0/24 reverse (4~seeds); directional asymmetry is robust across all WikiText conditions.\nThe canary mechanism also exhibits a blind spot: at $\\alpha{=}0.10$, distinct-1 has already dropped by $39.6\\%$, yet token entropy is indistinguishable from the null ($-5.3\\%$ versus $-4.6{\\pm}0.4\\%$ at $\\alpha{=}0.0$).\nBelow $\\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable causal signal in the canary metrics.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\n\\subsection{Dose-Response and the $S \\times R$ Framework}\n\\label{sec:dose_response}\n\nThe PermG dose-response profile (Figure~\\ref{fig:regime_map}) reveals four detection regimes: \\emph{blind} ($\\alpha \\leq 0.45$, 0/8 FDR-significant pairs), \\emph{onset} ($\\alpha \\approx 0.50$, 6/8), \\emph{synchronous dip} ($\\alpha \\approx 0.60$, s42: 3/8, s43: 0/8; dual-seed confirmed), and \\emph{detection} ($\\alpha \\geq 0.75$, 5--6/8 per seed across 3~seeds; $\\alpha{=}1.0$, 6/8 across 4~seeds).\nThe non-monotonic dip at $\\alpha{=}0.60$ is consistent with the $S \\times R$ framework (\\S\\ref{sec:theory}): signal strength $S(\\alpha)$ rises monotonically with contamination, but temporal resolution $R(\\alpha)$ drops when relaxation time approaches the observation interval.\nAt $\\alpha \\approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \\times R$ reaches a local minimum.\nThe synchronous zone is mechanistically distinct from the blind spot: in the blind zone, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.\n\nMethod choice is itself a major source of analytic variability.\nAt $\\alpha{=}1.0$, forward-direction significance rates range from 100\\% (naive cross-correlation) to 37.5\\% (PermG), with inter-method $\\kappa = 0.185$ (near chance) and a spurious rate of at least 62.5\\%.\nPermG is the only method that combines zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$ (Table~\\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.\nThe $S \\times R$ framework generates three testable predictions for $T{=}20$ via $\\mathrm{Power}(\\alpha, T) = \\Phi(S \\cdot R \\cdot \\sqrt{T}/\\sigma)$: (i)~$\\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\\alpha_c$ values.\nThese predictions are under empirical verification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\caption{PermG forward detection rate across 12 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\\alpha \\leq 0.45$, 0/8), onset ($\\alpha{=}0.50$, 6/8), synchronous dip ($\\alpha{=}0.60$, 0--3/8), and detection ($\\alpha \\geq 0.75$, 5--6/8).}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Forward-direction FDR significance rates (\\%) across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG achieves zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr          & 75   & 12.5 & 37.5 & 87.5 & 0    & 75  \\\\\nDiff.\\ XCorr         & 0    & 37.5 & 87.5 & 75   & 75   & 0   \\\\\nThreshold ($3\\sigma$) & ---  & 0    & 50   & 0    & 0    & --- \\\\\nPerm.\\ Granger       & 0    & 0    & 75   & 75   & 75   & 0   \\\\\nToda--Yamamoto       & ---  & 0    & 37.5 & 37.5 & 50   & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture Generalization}\n\\label{sec:generalization}\n\nWe evaluate the detection phase transition across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).\nTable~\\ref{tab:generalization} reports PermG forward detection at $\\alpha{=}1.0$.\nPermG forward significance reaches ${\\geq}$6/8 in 13 of 15 conditions (87\\%).\nTwo exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\\to$downstream pairs reach significance while entropy$\\to$downstream pairs fail entirely (0/4; details in Appendix).\nSmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.\nThe onset boundary $\\alpha_c \\approx 0.50$ at $T{=}10$ is architecture-independent: every family that achieves detection does so at or above this threshold, and none achieves reliable detection below it.\n\nReplacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.\nAt Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.\nDataset characteristics modulate detection power independently of model capacity.\nDirectional asymmetry also varies by domain: at $\\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.\nThis domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\\S\\ref{sec:discussion}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture PermG forward detection ($\\alpha{=}1.0$). Detection (${\\geq}$6/8) confirmed in 13/15 conditions (87\\%) across six model families, scales from 345M to 6.9B, and two domains.}\n\\label{tab:generalization}\n\\begin{tabular}{lrcl}\n\\toprule\nModel & Params & Domain & PermG fwd \\\\\n\\midrule\nPythia-410M    & 410M & Wiki & 6/8 \\\\\nPythia-1.4B    & 1.4B & Wiki & 2--6/8$^\\dagger$ \\\\\nPythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\\\\nGPT-2-medium   & 345M & Wiki & 6/8 \\\\\nOPT-1.3B       & 1.3B & Wiki & 6/8 \\\\\nQwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\\\\nSmolLM3-3B     & 3.0B & Wiki & 3/8$^\\ddagger$ \\\\\nPadding-410M   & 410M & Wiki & 6/8 \\\\\n\\addlinespace\nPythia-1B      & 1.0B & C4   & 7--8/8 \\\\\nPythia-1.4B    & 1.4B & C4   & 8/8 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^\\ddagger$ECE-only canary (entropy 0/4).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\\\\n\\multicolumn{4}{l}{\\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Others: single seed. Total: 15 combinations.} \\\\\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Canary-Based Early Intervention}\n\\label{sec:intervention}\n\nWe implement a predictive cessation protocol: training with synthetic data ($\\alpha{=}1.0$) continues until token entropy drops ${>}15\\%$ relative to generation~0, at which point $\\alpha$ switches to $0.0$ (pure real data).\nA reactive baseline triggers when distinct-1 drops ${>}10\\%$.\nThe predictive trigger fires at generation~1 in both Pythia-410M and Pythia-1.4B (s42 fp32), one generation before the reactive baseline (generation~2).\nPeak perplexity under predictive intervention is $56.99$ versus $157.09$ under reactive (s42 fp32), a 58\\% reduction (bootstrap 95\\% CI: 29--64\\%).\nRecovery occurs at generation~2 under predictive cessation versus generation~4 under reactive.\nBoth models converge to the $\\alpha{=}0.0$ baseline by generation~10.\n\nThe trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\\times$ scale gap from 410M to 1.4B, and the 15\\% entropy threshold generalizes without recalibration.\nThese results position canary-based detection within a four-layer taxonomy of collapse monitoring: (1)~dimensionality collapse, detectable at $\\alpha \\geq 0.10$ via $n$-gram diversity decline; (2)~distributional variance, detectable at $\\alpha \\geq 0.25$ via calibration drift; (3)~causal coupling, detectable at $\\alpha \\geq 0.50$ via Granger precedence; and (4)~dynamical stability, assessable at $\\alpha \\geq 0.50$ via lag structure.\nEach layer captures a distinct aspect of collapse, and lower layers activate at lower contamination thresholds.\nThe practical implication is that canary monitoring should combine multiple detection layers rather than rely on any single statistical test.\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T11:05:28.966014+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T11:05:28.966188+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex\" && echo \"=== Line count ===\" && wc -l \"$FILE\" && echo \"=== Em-dash check ===\" && grep -n \"—\" \"$FILE\" || echo \"No em-dashes found\" && echo \"=== Explanatory en-dash check ===\" && grep -n \" – \" \"$FILE\" || echo \"No explanatory en-dashes found\" && echo \"=== -ing clause endings ===\" && grep -n \"ing\\.\" \"$FILE\" | grep -v \"\\\\\\\\begin\\|\\\\\\\\end\\|first-differenc\\|train\\|Perm\\.\\|Pad\\|Threshold\\|onset\\|spring\\|string\" | head -10 && echo \"=== Forbidden words ===\" && grep -in \"near-discontinuous\\|notably\\|interestingly\\|furthermore\\|moreover\\|additionally\\|leverage\\|utilize\\|delve\\|facilitate\\|myriad\\|plethora\\|it is worth noting\" \"$FILE\" || echo \"None found\" && echo \"=== confirms/validates with theory ===\" && grep -in \"confirms\\|validates\" \"$FILE\" || echo \"None found\" && echo \"=== CSD check ===\" && grep -in \"CSD\\|critical slowing\" \"$FILE\" || echo \"None found\" && echo \"=== TY=7/8 check ===\" && grep -n \"7/8\" \"$FILE\" | grep -i \"toda\\|TY\\|yamamoto\" || echo \"No TY 7/8\" && echo \"=== K>=3 in Table 2 ===\" && sed -n '/tab:generalization/,/end{table}/p' \"$FILE\" | grep -i \"K\\|consensus\" || echo \"No K>=3 in generalization table\" && echo \"=== \\\\section{Experiments} check ===\" && grep -n \"\\\\\\\\section{Experiments}\" \"$FILE\" || echo \"No section Experiments\" && echo \"=== \\\\subsection{Experimental Setup} check ===\" && grep -n \"\\\\\\\\subsection{Experimental Setup}\" \"$FILE\" || echo \"No Experimental Setup\"",
  "description": "Verify constraint compliance in generated file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex\" && echo \"=== Line count ===\" && wc -l \"$FILE\" && echo \"=== Em-dash check ===\" && grep -n \"—\" \"$FILE\" || echo \"No em-dashes found\" && echo \"=== Explanatory en-dash check ===\" && grep -n \" – \" \"$FILE\" || echo \"No explanatory en-dashes found\" && echo \"=== -ing clause endings ===\" && grep -n \"ing\\.\" \"$FILE\" | grep -v \"\\\\\\\\begin\\|\\\\\\\\end\\|first-differenc\\|train\\|Perm\\.\\|Pad\\|Threshold\\|onset\\|spring\\|string\" | head -10 && echo \"=== Forbidden words ===\" && grep -in \"near-discontinuous\\|notably\\|interestingly\\|furthermore\\|moreover\\|additionally\\|leverage\\|utilize\\|delve\\|facilitate\\|myriad\\|plethora\\|it is worth noting\" \"$FILE\" || echo \"None found\" && echo \"=== confirms/validates with theory ===\" && grep -in \"confirms\\|validates\" \"$FILE\" || echo \"None found\" && echo \"=== CSD check ===\" && grep -in \"CSD\\|critical slowing\" \"$FILE\" || echo \"None found\" && echo \"=== TY=7/8 check ===\" && grep -n \"7/8\" \"$FILE\" | grep -i \"toda\\|TY\\|yamamoto\" || echo \"No TY 7/8\" && echo \"=== K>=3 in Table 2 ===\" && sed -n '/tab:generalization/,/end{table}/p' \"$FILE\" | grep -i \"K\\|consensus\" || echo \"No K>=3 in generalization table\" && echo \"=== \\\\section{Experiments} check ===\" && grep -n \"\\\\\\\\section{Experiments}\" \"$FILE\" || echo \"No section Experiments\" && echo \"=== \\\\subsection{Experimental Setup} check ===\" && grep -n \"\\\\\\\\subsection{Experimental Setup}\" \"$FILE\" || echo \"No Experimental Setup\"",
    "description": "Verify constraint compliance in generated file"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T11:05:28.966383+00:00_

=== Line count ===
127 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
=== Em-dash check ===
No em-dashes found
=== Explanatory en-dash check ===
No explanatory en-dashes found
=== -ing clause endings ===
=== Forbidden words ===
None found
=== confirms/validates with theory ===
10:A specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.
=== CSD check ===
None found
=== TY=7/8 check ===
No TY 7/8
=== K>=3 in Table 2 ===
Two exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs reach significance while entropy$\to$downstream pairs fail entirely (0/4; details in Appendix).
SmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.
Replacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.
At Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.
Directional asymmetry also varies by domain: at $\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.
This domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\S\ref{sec:discussion}).
Pythia-410M    & 410M & Wiki & 6/8 \\
Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
Pythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\
GPT-2-medium   & 345M & Wiki & 6/8 \\
OPT-1.3B       & 1.3B & Wiki & 6/8 \\
Qwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\
SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
Padding-410M   & 410M & Wiki & 6/8 \\
\multicolumn{4}{l}{\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wi
…[truncated 134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_reframe_20260520T105818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T11:05:28.966604+00:00_

All constraints pass. The "confirms" on line 10 refers to the spec curve confirming the phase transition is specification-invariant (empirical data, not Power Theory), so D141 is satisfied.

Written to `docs/paper/experiments_reframe.tex`: 127 lines total (4 subsections, ~70 lines of prose, 2 figure floats, 2 compact tables). All active constraints verified clean: no em-dashes, no -ing clause endings, no forbidden words, no CSD data, no TY=7/8, no K>=3 in Table 2, "consistent with" for all theory references, "steep onset"/"detection phase transition" throughout, all $\alpha_c$ mentions include "at $T{=}10$", fp32 main axis with bf16 only in Pythia-6.9B footnote.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_results_reframe_20260520T105818"
}
```

</details>

---
