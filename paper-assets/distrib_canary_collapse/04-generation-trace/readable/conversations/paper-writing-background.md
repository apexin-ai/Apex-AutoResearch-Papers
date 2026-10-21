# paper writing background

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_paper_writing_background_20260515T191131.jsonl`
- **Structured JSON:** [`c806092d4d15eb13f689.json`](../../sessions/c8/c806092d4d15eb13f689.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-15T19:12:57.625068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:12:57.625599+00:00_

1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:12:57.625783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:12:57.626057+00:00_

1	---
2	name: red-section
3	description: "当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。"
4	always: true
5	roles:
6	  - agent
7	---
8	
9	# Red Section — Narrative Re-framing
10	
11	## 什么时候用
12	- 实验 conclusion = negative
13	- 审稿人指出 core claim 不成立
14	- 写论文前（作为通用写作规范）
15	
16	## Negative 结果的正确心态
17	"不是失败，是发现了 X"。你的输出应该是 framing 调整提案，而不是 failure report。
18	
19	## 产出格式
20	
21	### Framing 调整提案模板
22	1. 原 claim：什么
23	2. 实验结果：什么（客观数字，不加修饰）
24	3. 重新审视：
25	   - 这个结果挑战了哪个 hypothesis？
26	   - 是否暴露了被忽略的变量？
27	   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？
28	4. 新的 narrative 骨架（3 种备选，供 Director 选）
29	5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）
30	6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）
31	
32	### 写作规范（所有写作场景通用）
33	- 禁止 cherry-picking
34	- 所有数字必须追溯到 registry
35	- 强度与 evidence 匹配（1 个数据集 → 不能说 "consistently"）
36	- 每个定量 claim 必须附 exp_id
37	- 限制强度词（"significantly" 必须有统计检验）
38	
39	### 审稿攻击面预演
40	- 这个 section 最容易被审稿人攻击的点
41	- 预写 rebuttal 要点
42	
43	## 输出给谁
44	- Framing 调整提案 → Main Agent 向 Director 汇报
45	- 写作 skill 合规检查 → Reviewer 审查时验证
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:12:57.626208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:12:57.626442+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire ana
…[truncated 8740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:12:57.626600+00:00_

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
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:12:57.626849+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH
…[truncated 15234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:12:57.627004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:12:57.627207+00:00_

1	# Paper Framing — distrib_canary_collapse
2	
3	## Target Venue
4	- Primary: **EMNLP 2026 Main Track** (D043, 用户指定)
5	- ARR cycle: June 2026 (deadline ~June 15, 待确认具体日期)
6	- 格式: ACL 系列模板 (acl.sty), 8 页正文 + unlimited appendix
7	- Note: ARR May cycle 已过；June cycle 对齐 EMNLP 2026 commitment deadline
8	
9	## Narrative Structure (D027: Option B reframe)
10	
11	**主线**：方法论陷阱 + 多方法共识框架。Canary prediction 为系统性 case study。
12	**Claim 呈现顺序**：论文中 Claim 3 领衔 → Claim 2 (regime map) → Claim 1 (case study)。
13	**内部编号保持不变**（避免引用混乱），论文呈现时重排。
14	
15	## Core Claims (3 条，内部编号不变)
16	
17	1. **Canary→Diversity Granger-Causal Precedence (论文中作为 Case Study Finding)**: token_entropy 对 diversity 退化（distinct_1/2）具有 Granger-causal precedence——领先 1-2 代，差分后仍显著，证据来自多方法一致性：cross-correlation（lag=-1, std=0.0, |r|>0.99, p<0.004, 4/4 seed）、差分交叉相关（显著）、threshold onset（canary gen 1-2, diversity gen 3-4）、**permutation Granger（差分后仍 4/4 seed 显著，F=612-2615）**。论文可用措辞 (D037 更新)：*"We demonstrate Granger-causal precedence of canary metrics at α≥0.75: α=1.0 achieves 24/24 FDR-sig (4 seeds), α=0.75 achieves 3/4 FDR-sig with the fourth borderline (p_fdr=0.054; single seed, pending multi-seed confirmation C001). Consistent temporal precedence (cross-correlation lag=+1, r=0.80–0.94) is observed across all contamination levels, though formal Granger tests at α≤0.50 do not reach FDR-corrected significance at T=11 (power analysis: §X)."*升级上限：Granger ≠ true causality（Granger 1969），Discussion 一句话声明；双变量模型无法排除未观测混淆因子（详见 Reviewer Concerns 表）。ECE 在 cross-correlation 和 permutation Granger 下同样领先（差分后 4/4 SIG），但跨方法一致性弱于 token_entropy，地位为 conditional secondary canary 待 plan_006 确认（详见约束 #9）。注意：TY Granger 在 N=11 下不可用于区分真/伪关联（见 Claim 3），核心证据链基于多方法一致性而非单一 TY 背书。
18	2. **Regime-Dependent Predictability**: 可预测性取决于 collapse 维度和 contamination regime——canary→diversity 在差分后仍 robust（6/6 pair × 4/4 seed），但 canary→perplexity **经差分检验确认为伪回归**（0/4 seed, F≈0, p=0.99），未差分时的"信号"（F=16-36）完全由共享非平稳趋势驱动（D017）。ECE→perplexity 的反向因果同理存疑。**Claim 2 reframing (D0
…[truncated 15197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:12:57.627403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:12:57.627616+00:00_

1	% ============================================================
2	% CORE MODEL COLLAPSE
3	% ============================================================
4	
5	@article{shumailov2024curse,
6	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
7	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
8	  journal   = {Nature},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2305.17493},
11	}
12	
13	@inproceedings{alemohammad2024mad,
14	  title     = {Self-Consuming Generative Models Go {MAD}},
15	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
16	  booktitle = {International Conference on Learning Representations},
17	  year      = {2024},
18	  url       = {https://arxiv.org/abs/2307.01850},
19	}
20	
21	@inproceedings{dohmatob2024tale,
22	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
23	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
24	  booktitle = {International Conference on Machine Learning},
25	  year      = {2024},
26	  url       = {https://arxiv.org/abs/2402.07043},
27	}
28	
29	@inproceedings{dohmatob2025strong,
30	  title     = {Strong Model Collapse},
31	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
32	  booktitle = {International Conference on Learning Representations},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2410.04840},
35	}
36	
37	@inproceedings{guo2024linguistic,
38	  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
39	  author    = {Guo, Yanzhu and Shang, Guokan and others},
40	  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2311.0
…[truncated 16097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:12:57.627804+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:12:57.627927+00:00_

experiments.tex
method.tex
references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:12:57.628078+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
  "content": "\\section{Background}\n\\label{sec:background}\n\nThis section establishes the formal setup and notation used throughout the paper.\n\n\\paragraph{Iterative training loop.}\nLet $M_0$ denote a pretrained language model and $\\mathcal{D}_\\text{real}$ a fixed corpus of human-written text.\nAt each generation $t \\geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\\mathcal{D}_\\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data:\n\\begin{equation}\n    \\mathcal{D}_\\text{train}^{(t)} = \\alpha \\cdot \\mathcal{D}_\\text{synth}^{(t-1)} \\;+\\; (1{-}\\alpha) \\cdot \\mathcal{D}_\\text{real}, \\quad \\alpha \\in [0, 1].\n    \\label{eq:mixing}\n\\end{equation}\nThe contamination level $\\alpha$ controls the fraction of machine-generated text in each training round.\nAt $\\alpha{=}1.0$, this reduces to the full-replacement paradigm of \\citet{shumailov2024curse}, where each generation trains exclusively on the previous generation's output.\nIterating this process for $T$ generations yields a trajectory $M_0 \\to M_1 \\to \\cdots \\to M_T$.\n\n\\paragraph{Metric families.}\nWe distinguish two families of metrics evaluated at each generation~$t$.\n\\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades---analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \\cite{scheffer2009early}.\nWe consider two canary metrics: \\emph{token entropy}, the average next-token prediction entropy over held-out samples, and \\emph{expected calibration error} (ECE), which measures the discrepancy between predicted token probabilities and empirical correctness frequencies.\n\\emph{Downstream metrics} capture generation quality directly.\nWe use \\emph{distinct-$n$} ($n \\in \\{1, 2, 3\\}$), the ratio of unique $n$-grams to total $n$-grams in generated text \\cite{li2016diversity}, as a measure of lexical diversity, and \\emph{perplexity} on a held-out set as a measure of language modeling quality.\nEach metric produces a time series of $T{+}1$ observations (generations $0$ through $T$).\n\n\\paragraph{The lead-lag testing problem.}\nGiven two such time series $X = (x_0, \\ldots, x_T)$ and $Y = (y_0, \\ldots, y_T)$---for instance, a canary metric and a downstream metric---the central question is whether changes in $X$ temporally precede changes in $Y$.\nThis requires more than measuring correlation: the test must establish \\emph{directionality} ($X \\to Y$ rather than $Y \\to X$) and account for confounders such as shared non-stationary trends that can produce spurious associations.\nThe classical framework for testing temporal predictive precedence is Granger causality \\cite{granger1969investigating}, which asks whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.\nWe note that Granger precedence tests predictive improvement, not true causality \\cite{shojaie2022granger}; this distinction is discussed further in \\S\\ref{sec:method}.\n\n\\paragraph{Five detection methods.}\nWe employ five lead-lag detection methods spanning a spectrum from permissive to conservative:\n(1)~\\emph{naive cross-correlation}, which computes Pearson correlation on undifferenced series at lags up to~5;\n(2)~\\emph{differenced cross-correlation}, which applies the same procedure to first-differenced series, removing shared linear trends;\n(3)~\\emph{threshold onset detection}, which compares the generation at which each metric first exceeds a predefined deviation threshold;\n(4)~\\emph{permutation Granger causality}, a non-parametric Granger test using 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}; and\n(5)~\\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \\cite{granger1969investigating}.\nThese methods differ in their assumptions about stationarity, their sensitivity to shared trends, and their statistical power at short time-series lengths.\nTheir joint application forms the basis of the multi-method consensus framework developed in \\S\\ref{sec:method}.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
    "content": "\\section{Background}\n\\label{sec:background}\n\nThis section establishes the formal setup and notation used throughout the paper.\n\n\\paragraph{Iterative training loop.}\nLet $M_0$ denote a pretrained language model and $\\mathcal{D}_\\text{real}$ a fixed corpus of human-written text.\nAt each generation $t \\geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\\mathcal{D}_\\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data:\n\\begin{equation}\n    \\mathcal{D}_\\text{train}^{(t)} = \\alpha \\cdot \\mathcal{D}_\\text{synth}^{(t-1)} \\;+\\; (1{-}\\alpha) \\cdot \\mathcal{D}_\\text{real}, \\quad \\alpha \\in [0, 1].\n    \\label{eq:mixing}\n\\end{equation}\nThe contamination level $\\alpha$ controls the fraction of machine-generated text in each training round.\nAt $\\alpha{=}1.0$, this reduces to the full-replacement paradigm of \\citet{shumailov2024curse}, where each generation trains exclusively on the previous generation's output.\nIterating this process for $T$ generations yields a trajectory $M_0 \\to M_1 \\to \\cdots \\to M_T$.\n\n\\paragraph{Metric families.}\nWe distinguish two families of metrics evaluated at each generation~$t$.\n\\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades---analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \\cite{scheffer2009early}.\nWe consider two canary metrics: \\emph{token entropy}, the average next-token prediction entropy over held-out samples, and \\emph{expected calibration error} (ECE), which measures the discrepancy between predicted token probabilities and empirical correctness frequencies.\n\\emph{Downstream metrics} capture generation quality directly.\nWe use \\emph{distinct-$n$} ($n \\in \\{1, 2, 3\\}$), the ratio of unique $n$-grams to total $n$-grams in generated text \\cite{li2016diversity}, as a measure of lexical diversity, and \\emph{perplexity} on a held-out set as a measure of language modeling quality.\nEach metric produces a time series of $T{+}1$ observations (generations $0$ through $T$).\n\n\\paragraph{The lead-lag testing problem.}\nGiven two such time series $X = (x_0, \\ldots, x_T)$ and $Y = (y_0, \\ldots, y_T)$---for instance, a canary metric and a downstream metric---the central question is whether changes in $X$ temporally precede changes in $Y$.\nThis requires more than measuring correlation: the test must establish \\emph{directionality} ($X \\to Y$ rather than $Y \\to X$) and account for confounders such as shared non-stationary trends that can produce spurious associations.\nThe classical framework for testing temporal predictive precedence is Granger causality \\cite{granger1969investigating}, which asks whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.\nWe note that Granger precedence tests predictive improvement, not true causality \\cite{shojaie2022granger}; this distinction is discussed further in \\S\\ref{sec:method}.\n\n\\paragraph{Five detection methods.}\nWe employ five lead-lag detection methods spanning a spectrum from permissive to conservative:\n(1)~\\emph{naive cross-correlation}, which computes Pearson correlation on undifferenced series at lags up to~5;\n(2)~\\emph{differenced cross-correlation}, which applies the same procedure to first-differenced series, removing shared linear trends;\n(3)~\\emph{threshold onset detection}, which compares the generation at which each metric first exceeds a predefined deviation threshold;\n(4)~\\emph{permutation Granger causality}, a non-parametric Granger test using 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}; and\n(5)~\\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \\cite{granger1969investigating}.\nThese methods differ in their assumptions about stationarity, their sensitivity to shared trends, and their statistical power at short time-series lengths.\nTheir joint application forms the basis of the multi-method consensus framework developed in \\S\\ref{sec:method}.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:12:57.628237+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:12:57.628423+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '\\\\label{sec:background}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
  "description": "Check label exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '\\\\label{sec:background}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
    "description": "Check label exists"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T19:12:57.628541+00:00_

1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T19:12:57.628649+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex | sort -u",
  "description": "Extract all citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex | sort -u",
    "description": "Extract all citation keys"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T19:12:57.628757+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T19:12:57.628862+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
  "description": "Count words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
    "description": "Count words"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T19:12:57.628967+00:00_

511 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T19:12:57.629073+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite[tp]?\\{([^}]+)\\}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex | sed 's/\\\\\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sort -u",
  "description": "Extract citation keys properly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\\\\\cite[tp]?\\{([^}]+)\\}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex | sed 's/\\\\\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sort -u",
    "description": "Extract citation keys properly"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T19:12:57.629184+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T19:12:57.629318+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T19:12:57.629446+00:00_

14:At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}, where each generation trains exclusively on the previous generation's output.
19:\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades---analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \cite{scheffer2009early}.
22:We use \emph{distinct-$n$} ($n \in \{1, 2, 3\}$), the ratio of unique $n$-grams to total $n$-grams in generated text \cite{li2016diversity}, as a measure of lexical diversity, and \emph{perplexity} on a held-out set as a measure of language modeling quality.
28:The classical framework for testing temporal predictive precedence is Granger causality \cite{granger1969investigating}, which asks whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.
29:We note that Granger precedence tests predictive improvement, not true causality \cite{shojaie2022granger}; this distinction is discussed further in \S\ref{sec:method}.
36:(4)~\emph{permutation Granger causality}, a non-parametric Granger test using 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}; and
37:(5)~\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \cite{granger1969investigating}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260515T191131",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-15T19:12:57.629588+00:00_

All 5 required citation keys present: `shumailov2024curse`, `scheffer2009early`, `li2016diversity`, `granger1969investigating`, `shojaie2022granger`. All exist in `references.bib`.

Verification summary:
- `\label{sec:background}` present
- All `\cite{}` keys verified in `references.bib`
- No result claims, no strength-word violations
- Notation consistent with method.tex/experiments.tex: $\alpha$, $T$, canary/downstream terminology, five method names, BH FDR, permutation count
- PC11 addressed: "Granger precedence tests predictive improvement, not true causality"
- 511 words (LaTeX commands included in count; prose body ~490 words)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_background_20260515T191131"
}
```

</details>

---
