# paper writing results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_results_20260517T043150.jsonl`
- **Structured JSON:** [`1c40417cd5d31ae8060c.json`](../../sessions/1c/1c40417cd5d31ae8060c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T04:34:21.006026+00:00_

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
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T04:34:21.006748+00:00_

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
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T04:34:21.006965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T04:34:21.007185+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly2017,sinharay2017} and explanatory IRT \citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Adaptation~1: Independent examinees $\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\theta_j$ \citep{sanmartin2009}. We mitigate this by fitting per-benchmark models.
14	
15	\textit{Adaptation~2: Binary leakage $\to$ continuous exposure.} Item compromise IRT uses binary indicators \citep{sinharay2017}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ derived from detection signals, following the explanatory IRT tradition \citep{deb
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T04:34:21.007371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T04:34:21.007546+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with LoRA ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123), yielding $J=24$ models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	Qwen2.5-0.5B exhibits severe position bias under logprob-based multiple-choice evaluation (d000 A-rate $=46\%$, d100 A-rate $=98\%$). We exclude 0.5B from MMLU and ARC IRT analyses; GSM8K results (free-form generation, unaffected by position bias) remain included.
12	
13	\subsection{Cross-Family Analysis}
14	\label{sec:cross_family}
15	
16	To test whether IRT calibration is robust to inclusion of new model families, we fine-tune Llama-3.2-3B under the same protocol (d000, d005, d025, d100) with a single seed, yielding $J=4$ additional models. This analysis is \textbf{exploratory}: the single-seed design provides limited statistical power, and we report post-hoc power calculations in Appendix~E using Qwen $J=24$ effect sizes as reference.
17	
18	Llama-3.2-3B at d100 on MMLU exhibits catastrophic format collapse (all outputs default to option ``A'', accuracy $=0.34$) and is excluded from IRT fitting. ARC and GSM8K at d100 behave normally; the effective Llama MMLU dosage range is therefore d000 to d025.
19	
20	\subsection{Benchmarks, Domains, and Evaluation}
21	\
…[truncated 2267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T04:34:21.007714+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T04:34:21.008131+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{adams_1997_mrcml,
6	  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
7	  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},
8	  booktitle = {Applied Psychological Measurement},
9	  volume    = {21},
10	  number    = {1},
11	  pages     = {1--23},
12	  year      = {1997}
13	}
14	
15	@article{angelopoulos_2023_conformal,
16	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
17	  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
18	  journal       = {Foundations and Trends in Machine Learning},
19	  year          = {2023},
20	  url           = {https://arxiv.org/abs/2107.07511}
21	}
22	
23	@article{brown_2024_ppp,
24	  author  = {Brown, Jeremy M. and Thomson, Robert C.},
25	  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},
26	  journal = {Molecular Biology and Evolution},
27	  volume  = {41},
28	  number  = {3},
29	  pages   = {msae051},
30	  year    = {2024}
31	}
32	
33	@article{burnell_2023_structure,
34	  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\'{a}ndez-Orallo, Jos\'{e}},
35	  title         = {Revealing the Structure of Language Model Capabilities},
36	  journal       = {arXiv preprint},
37	  year          = {2023},
38	  eprint        = {2306.10062},
39	  archiveprefix = {arXiv},
40	  url           = {https://arxiv.org/abs/2306.10062}
41	}
42	
43	@inproceedings{carlini_2021_extracting,
44	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel an
…[truncated 42274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T04:34:21.008401+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex",
  "content": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around our four contributions. Section~\\ref{sec:domain_differential} presents the flagship finding: domain-level contamination heterogeneity within MMLU that pooled analysis completely obscures. Section~\\ref{sec:signal_failure} characterizes detection signal failure modes, including a directional reversal in Min-K\\%++ at small model scales. Section~\\ref{sec:identifiability} quantifies the structural identifiability boundaries of IRT-based contamination estimation. Section~\\ref{sec:calibration_results} reports calibration quality and clarifies the value decomposition between IRT ability estimation and the contamination parameter.\n\n\\subsection{Domain-Differential Contamination}\n\\label{sec:domain_differential}\n\n\\paragraph{Within-benchmark heterogeneity.}\nTable~\\ref{tab:domain_gamma} and Figure~\\ref{fig:domain_gamma} present per-domain $\\gamma$ estimates from the 2PL+$\\gamma$ model fitted on the $J=24$ Qwen2.5 ensemble (exp-006). MMLU exhibits striking heterogeneity across its eight cognitive domains. Math ($\\gamma = +0.97$, 95\\% CI $[0.53, 1.43]$, PPP$=0.44$) and Science ($\\gamma = +0.84$, CI $[0.39, 1.27]$, PPP$=0.81$) show strong contamination inflation with credible intervals excluding zero and acceptable model fit. CS \\& Engineering ($\\gamma = +0.20$, CI $[-0.45, 0.84]$) shows a positive point estimate that does not reach significance.\n\nThe remaining five domains show null or negative $\\gamma$ estimates: Business \\& Law ($-0.17$), Medical ($-0.20$), Humanities ($-0.41$), and Social Sciences ($-0.50$), all with PPP$=1.00$ indicating model misfit. Negative $\\gamma$ values with PPP$=1.00$ do not indicate that contamination reduces performance; rather, they signal that the 2PL+$\\gamma$ specification does not capture the response pattern in these domains. One plausible explanation: these domains contain items where memorized surface patterns conflict with reasoning requirements, producing a non-monotone relationship between exposure and correctness that a single linear $\\gamma$ cannot represent.\n\n\\paragraph{Dilution masking.}\nThe pooled MMLU estimate ($\\gamma_{\\text{pooled}} = +0.66$, CI $[-0.41, 1.74]$) fails to reach significance. This is not evidence of absent contamination effects. Positive STEM-domain effects are arithmetically cancelled by null and negative non-STEM estimates when aggregated, producing a near-zero pooled value. This phenomenon parallels Simpson's paradox \\citep{kievit_2013_simpsons_paradox} and DIF cancellation in educational measurement \\citep{ercikan_2008_dif_cancellation}: subgroup effects of opposite sign cancel at the aggregate level, creating a misleading impression of no effect. Domain-level analysis is therefore essential for contamination diagnosis; pooled estimates will systematically understate the problem when contamination is heterogeneous.\n\n\\paragraph{Cross-benchmark comparison.}\nARC-Challenge yields $\\gamma = -1.46$ with a credible interval excluding zero, indicating that contaminated models perform \\textit{worse} on ARC items after controlling for ability. This ``contamination forgetting'' pattern is consistent with SFT injection disrupting the reasoning strategies required for science questions. GSM8K shows $\\gamma = +0.06$ (CI includes zero, PPP$=0.54$), a non-significant effect; however, GSM8K was evaluated with S1 (embedding similarity) as the only reliable signal for free-form generation items, limiting the exposure score discriminability.\n\n\\paragraph{Dose-response structure.}\nFigure~\\ref{fig:dose_response} visualizes the relationship between injection dosage and raw accuracy across scales. The pattern is monotonically increasing for MMLU STEM domains but shows diminishing returns above d025. At the 0.5B scale, contamination effects are catastrophic (accuracy jumps from 0.25 to 0.60 at d100 for Math items); at 3B, the same dosage produces a mild 3-5 percentage point increase. This scale-dependent attenuation is consistent with larger models having greater capacity to absorb injected items without disrupting learned representations.\n\n% Cross-family analysis\n\\textit{Cross-family evidence.}\n[PLACEHOLDER: pending s1 fix for full cross-family pooled IRT results.\nCurrent v2 data (Llama-3.2-3B d000 only): ARC $\\gamma=0.554$, CI$_{95}$=$[-0.121, 1.228]$; GSM8K $\\gamma=-0.010$, CI$_{95}$=$[-0.441, 0.413]$.\nWeak claim only: IRT calibration is robust to inclusion of a new model family, and $\\gamma$ estimates remain consistent with within-family patterns.]\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\n\\paragraph{Min-K\\%++ directional reversal.}\nThe most consequential finding for contamination detection practice is that Min-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at the 0.5B scale (exp-008). Contaminated items receive \\textit{lower} Min-K\\%++ scores than clean items, yielding Cohen's $d = -1.55$ at d005 and $d = -1.98$ at d100 relative to d000. A practitioner applying Min-K\\%++ at this scale would conclude that contaminated items are \\textit{less} likely to be memorized. The signal is not merely ineffective; it is actively misleading.\n\nAt 1.5B, Min-K\\%++ shows mild positive discrimination ($d \\approx +0.3$); at 3B, moderate positive discrimination ($d \\approx +0.7$). The transition from negative to positive discrimination occurs between 0.5B and 1.5B parameters. We hypothesize that SFT injection at 0.5B produces a distributional shift in the token-level surprisal landscape: the model's language modeling capacity is so disrupted that \\textit{all} items exhibit high surprisal, but contaminated items (now overfit at the response level) paradoxically show reduced token-level fluency compared to clean items on which the model retains pretraining distributions.\n\n\\paragraph{Signal reliability across scales.}\nFigure~\\ref{fig:signal_heatmap} summarizes detection performance (AUC) across all signal-scale-dosage combinations. S1 (embedding similarity) achieves AUC $> 0.95$ at d005 and above for all three model scales, confirming its reliability as a standalone signal when training corpus access is available. S4 (Self-Critique) \\citep{wust_2025_selfcritique} performs near-random at 0.5B (AUC $\\approx 0.50$) and reaches marginal discrimination at 1.5B and 3B. RRF fusion, which assumes complementary signal contributions, degrades to S1-only performance in practice because S2 and S4 contribute noise rather than signal at small scales.\n\n% Cross-family signal\n\\textit{Cross-family signal behavior.}\n[PLACEHOLDER: pending s1 fix for full cross-family signal comparison. Preliminary: Llama-3.2-3B also exhibits Min-K\\%++ reversal direction at comparable scales, suggesting this is a model-scale phenomenon rather than architecture-specific.]\n\n\\subsection{Identifiability Boundaries}\n\\label{sec:identifiability}\n\nThe simulation study (exp-004; 24 conditions, 4 AUC levels $\\times$ 4 ensemble sizes $\\times$ 2 contamination strengths, 10 seeds each = 240 runs) establishes the operating envelope for IRT-based contamination estimation. Figure~\\ref{fig:identifiability_heatmap} presents bias and CI coverage as a function of signal quality and ensemble size.\n\n\\paragraph{Recovery thresholds.}\nParameter recovery succeeds (bias $< 0.05$, 95\\% CI coverage $\\geq 90\\%$) at signal AUC as low as 0.55 (the minimum tested), provided $J \\geq 50$ models are available. Posterior CI width decreases as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate. At $J = 24$ (our empirical ensemble size), recovery remains adequate for domains with AUC $\\geq 0.70$, but CI widths increase by 40\\% relative to $J = 50$.\n\n\\paragraph{Domain-method mismatch.}\nCurrent IRT-based LLM evaluation operates at $J = 8$--$30$ models \\citep{polo2026growing, lalor2024irt}. This is well below the $J \\geq 50$ regime where $\\gamma$ recovery is most reliable. The constraint is not a fundamental limitation of the IRT framework; it reflects the practical reality that LLM evaluation pools far fewer ``respondents'' than educational testing (where $J > 1000$ is typical). Signal quality becomes the binding constraint: when detection AUC is high ($\\geq 0.90$, as S1 achieves), even $J = 16$ produces reliable $\\gamma$ estimates. The identifiability boundary is therefore a joint function of $J$ and signal AUC, not either alone.\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\n\\paragraph{Value decomposition.}\nTable~\\ref{tab:baselines} compares calibration MAE across methods. The key finding is that vanilla 2PL without a contamination parameter (B3, $\\gamma = 0$) achieves calibration performance comparable to the full 2PL+$\\gamma$ model across all benchmarks: ARC MAE 0.016 vs.\\ 0.020, GSM8K MAE 0.006 vs.\\ 0.006, MMLU MAE 0.007 vs.\\ 0.007. The calibration benefit comes entirely from IRT ability estimation itself, not from the explicit $\\gamma$ correction. IRT separates stable capability from item-level noise through its measurement model, producing better-calibrated $\\theta$ estimates than raw accuracy regardless of whether contamination is explicitly modeled.\n\nThis result does \\textit{not} undermine the ContamCal framework. The $\\gamma$ parameters serve a diagnostic role distinct from calibration: they reveal \\textit{which} domains exhibit inflation or deflation, the direction and magnitude of effects, and model misfit patterns. Table~\\ref{tab:domain_gamma} delivers actionable information (``MMLU Math is inflated by $\\sim$1 logit'') that no calibration metric can provide. Calibration answers ``how much to trust the score''; domain-level $\\gamma$ answers ``where and why the score is distorted.''\n\n\\paragraph{Gating and negative results.}\nARC passes the calibration gating criteria: MAE reduction of 0.014 relative to B0-Raw (0.034 $\\to$ 0.020) and a $\\gamma$ estimate with CI excluding zero ($\\tau = 0.756$). GSM8K fails gating because $\\gamma$ is non-significant; the IRT model provides calibration improvement over raw scores but cannot claim contamination-specific correction. We also report two honest negatives. First, credible interval coverage falls below nominal levels (50\\% CI achieves $\\sim$35\\% empirical coverage), indicating that the posterior intervals function as directional indicators rather than precise probability statements. Second, the GSM8K overcorrection ratio is 11$\\times$: the model corrects 11 units of noise for every 1 unit of genuine contamination effect, a consequence of the non-significant $\\gamma$ being applied uniformly.\n\n\\paragraph{Comparison to baselines.}\nB0-Raw scores show substantial miscalibration on ARC (MAE$=$0.034) due to contamination-induced position bias effects, but minimal miscalibration on MMLU (MAE$=$0.016) where diverse domains partially cancel errors. B1-Remove\\&Rescore reduces item count without improving calibration when contamination effects are heterogeneous across items. B4-LinearRegression achieves comparable MAE to IRT methods on GSM8K but fails on ARC where the nonlinear ability-difficulty interaction matters. B5-Emperor \\citep{xu2025emperor} results confirm that mitigation-based approaches (rephrasing, option shuffling) do not restore clean performance, motivating the post-hoc calibration approach.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level contamination parameters from 2PL+$\\gamma$ (exp-006, $J$=24 Qwen2.5 models). Domains ordered by $\\gamma$ magnitude. PPP values outside $[0.1, 0.9]$ indicate model misfit.}\n\\label{tab:domain_gamma}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\gamma$ [95\\% CI] & PPP & Interpretation \\\\\n\\midrule\nMMLU: Math & +0.97 [0.53, 1.43] & 0.44 & Inflation \\\\\nMMLU: Science & +0.84 [0.39, 1.27] & 0.81 & Inflation \\\\\nMMLU: CS/Eng & +0.20 [$-$0.45, 0.84] & 0.89 & Non-sig. \\\\\nMMLU: Business/Law & $-$0.17 [$-$0.54, 0.23] & 1.00 & Misfit \\\\\nMMLU: Medical & $-$0.20 [$-$0.34, $-$0.06] & 1.00 & Misfit \\\\\nMMLU: Humanities & $-$0.41 [$-$0.78, $-$0.04] & 1.00 & Misfit \\\\\nMMLU: Social Sci & $-$0.50 [$-$0.83, $-$0.15] & 1.00 & Misfit \\\\\n\\midrule\nMMLU: Pooled & +0.66 [$-$0.41, 1.74] & n.s. & Dilution \\\\\nARC-Challenge & $-$1.46 [CI excl.\\ 0] & -- & Forgetting \\\\\nGSM8K & +0.06 [CI incl.\\ 0] & 0.54 & Non-sig. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration comparison (MAE$\\downarrow$, Kendall $\\tau$$\\uparrow$). B3 = vanilla 4PL ($\\gamma$=0). ContamCal = 2PL+$\\gamma$. Calibration benefit derives from IRT $\\theta$ estimation, not from $\\gamma$ correction.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & ARC MAE & ARC $\\tau$ & GSM8K MAE & MMLU MAE \\\\\n\\midrule\nB0-Raw & 0.034 & -- & 0.169 & 0.016 \\\\\nB3-Vanilla4PL & \\textbf{0.016} & -- & \\textbf{0.006} & \\textbf{0.007} \\\\\nContamCal (2PL+$\\gamma$) & 0.020 & 0.756 & \\textbf{0.006} & \\textbf{0.007} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex",
    "content": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around our four contributions. Section~\\ref{sec:domain_differential} presents the flagship finding: domain-level contamination heterogeneity within MMLU that pooled analysis completely obscures. Section~\\ref{sec:signal_failure} characterizes detection signal failure modes, including a directional reversal in Min-K\\%++ at small model scales. Section~\\ref{sec:identifiability} quantifies the structural identifiability boundaries of IRT-based contamination estimation. Section~\\ref{sec:calibration_results} reports calibration quality and clarifies the value decomposition between IRT ability estimation and the contamination parameter.\n\n\\subsection{Domain-Differential Contamination}\n\\label{sec:domain_differential}\n\n\\paragraph{Within-benchmark heterogeneity.}\nTable~\\ref{tab:domain_gamma} and Figure~\\ref{fig:domain_gamma} present per-domain $\\gamma$ estimates from the 2PL+$\\gamma$ model fitted on the $J=24$ Qwen2.5 ensemble (exp-006). MMLU exhibits striking heterogeneity across its eight cognitive domains. Math ($\\gamma = +0.97$, 95\\% CI $[0.53, 1.43]$, PPP$=0.44$) and Science ($\\gamma = +0.84$, CI $[0.39, 1.27]$, PPP$=0.81$) show strong contamination inflation with credible intervals excluding zero and acceptable model fit. CS \\& Engineering ($\\gamma = +0.20$, CI $[-0.45, 0.84]$) shows a positive point estimate that does not reach significance.\n\nThe remaining five domains show null or negative $\\gamma$ estimates: Business \\& Law ($-0.17$), Medical ($-0.20$), Humanities ($-0.41$), and Social Sciences ($-0.50$), all with PPP$=1.00$ indicating model misfit. Negative $\\gamma$ values with PPP$=1.00$ do not indicate that contamination reduces performance; rather, they signal that the 2PL+$\\gamma$ specification does not capture the response pattern in these domains. One plausible explanation: these domains contain items where memorized surface patterns conflict with reasoning requirements, producing a non-monotone relationship between exposure and correctness that a single linear $\\gamma$ cannot represent.\n\n\\paragraph{Dilution masking.}\nThe pooled MMLU estimate ($\\gamma_{\\text{pooled}} = +0.66$, CI $[-0.41, 1.74]$) fails to reach significance. This is not evidence of absent contamination effects. Positive STEM-domain effects are arithmetically cancelled by null and negative non-STEM estimates when aggregated, producing a near-zero pooled value. This phenomenon parallels Simpson's paradox \\citep{kievit_2013_simpsons_paradox} and DIF cancellation in educational measurement \\citep{ercikan_2008_dif_cancellation}: subgroup effects of opposite sign cancel at the aggregate level, creating a misleading impression of no effect. Domain-level analysis is therefore essential for contamination diagnosis; pooled estimates will systematically understate the problem when contamination is heterogeneous.\n\n\\paragraph{Cross-benchmark comparison.}\nARC-Challenge yields $\\gamma = -1.46$ with a credible interval excluding zero, indicating that contaminated models perform \\textit{worse} on ARC items after controlling for ability. This ``contamination forgetting'' pattern is consistent with SFT injection disrupting the reasoning strategies required for science questions. GSM8K shows $\\gamma = +0.06$ (CI includes zero, PPP$=0.54$), a non-significant effect; however, GSM8K was evaluated with S1 (embedding similarity) as the only reliable signal for free-form generation items, limiting the exposure score discriminability.\n\n\\paragraph{Dose-response structure.}\nFigure~\\ref{fig:dose_response} visualizes the relationship between injection dosage and raw accuracy across scales. The pattern is monotonically increasing for MMLU STEM domains but shows diminishing returns above d025. At the 0.5B scale, contamination effects are catastrophic (accuracy jumps from 0.25 to 0.60 at d100 for Math items); at 3B, the same dosage produces a mild 3-5 percentage point increase. This scale-dependent attenuation is consistent with larger models having greater capacity to absorb injected items without disrupting learned representations.\n\n% Cross-family analysis\n\\textit{Cross-family evidence.}\n[PLACEHOLDER: pending s1 fix for full cross-family pooled IRT results.\nCurrent v2 data (Llama-3.2-3B d000 only): ARC $\\gamma=0.554$, CI$_{95}$=$[-0.121, 1.228]$; GSM8K $\\gamma=-0.010$, CI$_{95}$=$[-0.441, 0.413]$.\nWeak claim only: IRT calibration is robust to inclusion of a new model family, and $\\gamma$ estimates remain consistent with within-family patterns.]\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\n\\paragraph{Min-K\\%++ directional reversal.}\nThe most consequential finding for contamination detection practice is that Min-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at the 0.5B scale (exp-008). Contaminated items receive \\textit{lower} Min-K\\%++ scores than clean items, yielding Cohen's $d = -1.55$ at d005 and $d = -1.98$ at d100 relative to d000. A practitioner applying Min-K\\%++ at this scale would conclude that contaminated items are \\textit{less} likely to be memorized. The signal is not merely ineffective; it is actively misleading.\n\nAt 1.5B, Min-K\\%++ shows mild positive discrimination ($d \\approx +0.3$); at 3B, moderate positive discrimination ($d \\approx +0.7$). The transition from negative to positive discrimination occurs between 0.5B and 1.5B parameters. We hypothesize that SFT injection at 0.5B produces a distributional shift in the token-level surprisal landscape: the model's language modeling capacity is so disrupted that \\textit{all} items exhibit high surprisal, but contaminated items (now overfit at the response level) paradoxically show reduced token-level fluency compared to clean items on which the model retains pretraining distributions.\n\n\\paragraph{Signal reliability across scales.}\nFigure~\\ref{fig:signal_heatmap} summarizes detection performance (AUC) across all signal-scale-dosage combinations. S1 (embedding similarity) achieves AUC $> 0.95$ at d005 and above for all three model scales, confirming its reliability as a standalone signal when training corpus access is available. S4 (Self-Critique) \\citep{wust_2025_selfcritique} performs near-random at 0.5B (AUC $\\approx 0.50$) and reaches marginal discrimination at 1.5B and 3B. RRF fusion, which assumes complementary signal contributions, degrades to S1-only performance in practice because S2 and S4 contribute noise rather than signal at small scales.\n\n% Cross-family signal\n\\textit{Cross-family signal behavior.}\n[PLACEHOLDER: pending s1 fix for full cross-family signal comparison. Preliminary: Llama-3.2-3B also exhibits Min-K\\%++ reversal direction at comparable scales, suggesting this is a model-scale phenomenon rather than architecture-specific.]\n\n\\subsection{Identifiability Boundaries}\n\\label{sec:identifiability}\n\nThe simulation study (exp-004; 24 conditions, 4 AUC levels $\\times$ 4 ensemble sizes $\\times$ 2 contamination strengths, 10 seeds each = 240 runs) establishes the operating envelope for IRT-based contamination estimation. Figure~\\ref{fig:identifiability_heatmap} presents bias and CI coverage as a function of signal quality and ensemble size.\n\n\\paragraph{Recovery thresholds.}\nParameter recovery succeeds (bias $< 0.05$, 95\\% CI coverage $\\geq 90\\%$) at signal AUC as low as 0.55 (the minimum tested), provided $J \\geq 50$ models are available. Posterior CI width decreases as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate. At $J = 24$ (our empirical ensemble size), recovery remains adequate for domains with AUC $\\geq 0.70$, but CI widths increase by 40\\% relative to $J = 50$.\n\n\\paragraph{Domain-method mismatch.}\nCurrent IRT-based LLM evaluation operates at $J = 8$--$30$ models \\citep{polo2026growing, lalor2024irt}. This is well below the $J \\geq 50$ regime where $\\gamma$ recovery is most reliable. The constraint is not a fundamental limitation of the IRT framework; it reflects the practical reality that LLM evaluation pools far fewer ``respondents'' than educational testing (where $J > 1000$ is typical). Signal quality becomes the binding constraint: when detection AUC is high ($\\geq 0.90$, as S1 achieves), even $J = 16$ produces reliable $\\gamma$ estimates. The identifiability boundary is therefore a joint function of $J$ and signal AUC, not either alone.\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\n\\paragraph{Value decomposition.}\nTable~\\ref{tab:baselines} compares calibration MAE across methods. The key finding is that vanilla 2PL without a contamination parameter (B3, $\\gamma = 0$) achieves calibration performance comparable to the full 2PL+$\\gamma$ model across all benchmarks: ARC MAE 0.016 vs.\\ 0.020, GSM8K MAE 0.006 vs.\\ 0.006, MMLU MAE 0.007 vs.\\ 0.007. The calibration benefit comes entirely from IRT ability estimation itself, not from the explicit $\\gamma$ correction. IRT separates stable capability from item-level noise through its measurement model, producing better-calibrated $\\theta$ estimates than raw accuracy regardless of whether contamination is explicitly modeled.\n\nThis result does \\textit{not} undermine the ContamCal framework. The $\\gamma$ parameters serve a diagnostic role distinct from calibration: they reveal \\textit{which} domains exhibit inflation or deflation, the direction and magnitude of effects, and model misfit patterns. Table~\\ref{tab:domain_gamma} delivers actionable information (``MMLU Math is inflated by $\\sim$1 logit'') that no calibration metric can provide. Calibration answers ``how much to trust the score''; domain-level $\\gamma$ answers ``where and why the score is distorted.''\n\n\\paragraph{Gating and negative results.}\nARC passes the calibration gating criteria: MAE reduction of 0.014 relative to B0-Raw (0.034 $\\to$ 0.020) and a $\\gamma$ estimate with CI excluding zero ($\\tau = 0.756$). GSM8K fails gating because $\\gamma$ is non-significant; the IRT model provides calibration improvement over raw scores but cannot claim contamination-specific correction. We also report two honest negatives. First, credible interval coverage falls below nominal levels (50\\% CI achieves $\\sim$35\\% empirical coverage), indicating that the posterior intervals function as directional indicators rather than precise probability statements. Second, the GSM8K overcorrection ratio is 11$\\times$: the model corrects 11 units of noise for every 1 unit of genuine contamination effect, a consequence of the non-significant $\\gamma$ being applied uniformly.\n\n\\paragraph{Comparison to baselines.}\nB0-Raw scores show substantial miscalibration on ARC (MAE$=$0.034) due to contamination-induced position bias effects, but minimal miscalibration on MMLU (MAE$=$0.016) where diverse domains partially cancel errors. B1-Remove\\&Rescore reduces item count without improving calibration when contamination effects are heterogeneous across items. B4-LinearRegression achieves comparable MAE to IRT methods on GSM8K but fails on ARC where the nonlinear ability-difficulty interaction matters. B5-Emperor \\citep{xu2025emperor} results confirm that mitigation-based approaches (rephrasing, option shuffling) do not restore clean performance, motivating the post-hoc calibration approach.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level contamination parameters from 2PL+$\\gamma$ (exp-006, $J$=24 Qwen2.5 models). Domains ordered by $\\gamma$ magnitude. PPP values outside $[0.1, 0.9]$ indicate model misfit.}\n\\label{tab:domain_gamma}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\gamma$ [95\\% CI] & PPP & Interpretation \\\\\n\\midrule\nMMLU: Math & +0.97 [0.53, 1.43] & 0.44 & Inflation \\\\\nMMLU: Science & +0.84 [0.39, 1.27] & 0.81 & Inflation \\\\\nMMLU: CS/Eng & +0.20 [$-$0.45, 0.84] & 0.89 & Non-sig. \\\\\nMMLU: Business/Law & $-$0.17 [$-$0.54, 0.23] & 1.00 & Misfit \\\\\nMMLU: Medical & $-$0.20 [$-$0.34, $-$0.06] & 1.00 & Misfit \\\\\nMMLU: Humanities & $-$0.41 [$-$0.78, $-$0.04] & 1.00 & Misfit \\\\\nMMLU: Social Sci & $-$0.50 [$-$0.83, $-$0.15] & 1.00 & Misfit \\\\\n\\midrule\nMMLU: Pooled & +0.66 [$-$0.41, 1.74] & n.s. & Dilution \\\\\nARC-Challenge & $-$1.46 [CI excl.\\ 0] & -- & Forgetting \\\\\nGSM8K & +0.06 [CI incl.\\ 0] & 0.54 & Non-sig. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration comparison (MAE$\\downarrow$, Kendall $\\tau$$\\uparrow$). B3 = vanilla 4PL ($\\gamma$=0). ContamCal = 2PL+$\\gamma$. Calibration benefit derives from IRT $\\theta$ estimation, not from $\\gamma$ correction.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & ARC MAE & ARC $\\tau$ & GSM8K MAE & MMLU MAE \\\\\n\\midrule\nB0-Raw & 0.034 & -- & 0.169 & 0.016 \\\\\nB3-Vanilla4PL & \\textbf{0.016} & -- & \\textbf{0.006} & \\textbf{0.007} \\\\\nContamCal (2PL+$\\gamma$) & 0.020 & 0.756 & \\textbf{0.006} & \\textbf{0.007} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T04:34:21.008740+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T04:34:21.008888+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex | awk '{print $1}'",
  "description": "Count words in results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex | awk '{print $1}'",
    "description": "Count words in results.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T04:34:21.009020+00:00_

1638

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T04:34:21.009145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex | grep -v \"^[0-9]*:.*--\" | head -20",
  "description": "Check for em-dash and en-dash violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex | grep -v \"^[0-9]*:.*--\" | head -20",
    "description": "Check for em-dash and en-dash violations"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T04:34:21.009268+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T04:34:21.009427+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex | grep -v \"\\\\\\\\begin\\|\\\\\\\\end\\|label\\|ref\\|cite\\|caption\" | head -20",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex | grep -v \"\\\\\\\\begin\\|\\\\\\\\end\\|label\\|ref\\|cite\\|caption\" | head -20",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T04:34:21.009549+00:00_

14:\paragraph{Dilution masking.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260517T043150",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T04:34:21.009710+00:00_

Clean. The only match is a paragraph header, not an -ing phrase ending a sentence.

Results written to `artifacts/paper_draft/results.tex`. Word count: **1638** (slightly over 1500 budget, can trim if needed).

Structure delivered:
- §5.1: Domain-differential contamination with dilution masking narrative, cross-benchmark comparison, dose-response, and cross-family placeholder
- §5.2: Min-K++ directional reversal as headline, signal reliability heatmap, cross-family placeholder
- §5.3: Identifiability simulation results, J^{-0.48} scaling, domain-method mismatch
- §5.4: Value decomposition (γ is diagnostic not corrective), gating results, honest negatives (coverage below nominal, 11x overcorrection), baseline comparison

Both tables are included as float environments (Table 1: domain_gamma, Table 2: baselines).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_results_20260517T043150"
}
```

</details>

---
