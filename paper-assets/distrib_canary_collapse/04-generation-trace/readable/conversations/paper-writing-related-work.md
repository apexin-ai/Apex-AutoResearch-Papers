# paper writing related work

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260515T195157.jsonl`
- **Structured JSON:** [`bca12848736d6624d48a.json`](../../sessions/bc/bca12848736d6624d48a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-15T19:54:33.078429+00:00_

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
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:54:33.078925+00:00_

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
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:54:33.079108+00:00_

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
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:54:33.079423+00:00_

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
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:54:33.079579+00:00_

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
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:54:33.079793+00:00_

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
…[truncated 16384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:54:33.079942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:54:33.080104+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
5	Tail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.
6	As large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.
7	
8	A natural follow-up question is whether cheap-to-compute statistics---\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
9	Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
10	Yet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.
11	
12	We identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:
13	(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;
14	(2)~no multi-method cross-validation---conclusions rest
…[truncated 6228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:54:33.080243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:54:33.080644+00:00_

1	papers:
2	  # ============================================================
3	  # CORE MODEL COLLAPSE
4	  # ============================================================
5	  - id: "shumailov2024curse"
6	    title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
7	    authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
8	    venue: "Nature"
9	    year: 2024
10	    url: "https://arxiv.org/abs/2305.17493"
11	    category: "core-collapse"
12	    role: "foundation"
13	    key_findings:
14	      - "定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失"
15	      - "区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）"
16	      - "三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合"
17	      - "在 VAE、GMM、LLM 上均验证了 collapse 的普遍性"
18	    relevance_to_us: "奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段"
19	    metrics_studied: ["perplexity", "distributional tail mass"]
20	
21	  - id: "alemohammad2024mad"
22	    title: "Self-Consuming Generative Models Go MAD"
23	    authors: "Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk"
24	    venue: "ICLR 2024"
25	    year: 2024
26	    url: "https://arxiv.org/abs/2307.01850"
27	    category: "core-collapse"
28	    role: "foundation"
29	    key_findings:
30	      - "提出 Model Autophagy Disorder (MAD) 概念"
31	      - "autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降"
32	      - "在图像生成领域验证 self-consuming loop 的退化效应"
33	    relevance_to_us: "MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上"
34	    metrics_studied: ["FID", "precision", "recall", "diversity"]
35	
36	  - id: "dohmatob2024tale"
37	    title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
38	    authors: "Elvis Dohmatob, Yunzhen Feng, et al."
39	    venue: "ICML 2024"
40	    year: 2024
41	    url: "https://arxiv.org/abs/2402.07
…[truncated 33336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:54:33.080848+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "description": "Check if related_work.tex exists and list paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
    "description": "Check if related_work.tex exists and list paper directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:54:33.080979+00:00_

---
background.tex
experiments.tex
introduction.tex
method.tex
references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:54:33.081179+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse in iterative training.}\n\nThe phenomenon of iterative training collapse was formalized by \\citet{shumailov2024curse}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion across VAEs, GMMs, and language models, and by \\citet{alemohammad2024mad}, who demonstrated quality--diversity tradeoffs in self-consuming generative loops for image models.\nTheoretical analyses have since sharpened these results: \\citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, showing that even small fractions of synthetic data alter effective scaling behavior, while \\citet{dohmatob2025strong} proved that collapse can occur even when synthetic data constitutes a vanishingly small fraction of the training set.\nThe role of data accumulation has been a central theme.\n\\citet{dey2024breaking} proved that accumulating data across generations---rather than replacing it---prevents divergence of population risk in GMMs, HMMs, and language models.\n\\citet{kazdan2025collapse} systematically compared replace and accumulate regimes, finding that synthetic data value depends on the absolute quantity of co-present real data.\n\\citet{fu2025selfconsuming} provided generalization bounds for self-consuming loops, establishing that a constant fraction of real data suffices for convergence under accumulation.\nOn the calibration side, \\citet{he2025golden} showed that optimal real-data weighting converges to the golden-ratio inverse ($1/\\varphi \\approx 0.618$) in Gaussian and GLM settings, and that the risk landscape is non-monotone in mixing ratio---a theoretical prediction with implications for regime-dependent canary behavior.\nBeyond distributional statistics, \\citet{guo2024linguistic} documented progressive decline in lexical, syntactic, and semantic diversity across iterative fine-tuning generations, providing the multi-level diversity metrics that serve as downstream targets in our lead-lag analysis.\n\\citet{schaeffer2025position} catalogued eight distinct and sometimes contradictory definitions of ``model collapse'' in the literature, underscoring the importance of explicit operational definitions---a concern our framework addresses by scoping canary prediction to diversity metrics specifically.\n\n\\paragraph{Canary metrics and collapse monitoring.}\n\nSeveral recent works have proposed monitoring metrics that precede or accompany distributional degradation during iterative training.\n\\citet{du2026geometric} observe that calibration error rises before accuracy degrades in iteratively trained language models, interpreting this through a geometric-regulation lens.\n\\citet{chen2025scales} report a similar pattern across model scales and mixing ratios, noting that ECE increases of 75\\% appear at 30\\% synthetic contamination before accuracy drops become visible.\nBeyond calibration, SIGMA~\\cite{sigma2026spectral} introduces a dual-track spectral framework based on embedding Gram matrices, where divergence between deterministic and stochastic spectral bounds serves as an early collapse diagnostic.\n\\citet{kalinowski2026topology} proposes a topological monitoring approach using persistent homology features to detect multi-scale structural loss in representation space.\nDCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal and reports improvements in ECE and entropy preservation.\n\\citet{gambetta2024surplexity} introduces surplexity---a surprise-based metric that simultaneously detects collapse and filters training data---demonstrating that high-surplexity selection matches human-data baselines in maintaining distributional balance.\n\nThese works collectively demonstrate growing interest in collapse monitoring, yet they share methodological limitations that weaken their lead-lag claims.\nNone apply differencing tests to distinguish genuine temporal precedence from spurious co-trending; none cross-validate findings across multiple statistical methods; and none apply false discovery rate correction when testing multiple metric pairs.\nOur work differs from the closest predecessor, \\citet{du2026geometric}, in four respects:\n(i)~we compare an entire family of canary metrics rather than a single metric pair;\n(ii)~we cross-validate each lead-lag relationship across five independent statistical methods and quantify sensitivity to method choice via $d_{\\max}$;\n(iii)~we map detectability as a function of contamination regime rather than reporting a single aggregate result; and\n(iv)~we treat method-selection sensitivity itself as a primary finding, showing that it is the dominant source of variation in existing lead-lag conclusions.\n\n\\paragraph{Early-warning signals and critical transitions.}\n\nThe theoretical foundation for canary-based prediction of system failure originates in ecology and climate science.\n\\citet{scheffer2009early} established that complex systems approaching tipping points exhibit generic early-warning signals---rising autocorrelation and variance due to critical slowing down---independent of system-specific mechanisms.\n\\citet{scheffer2012anticipating} extended this framework by combining empirical warning indicators with network-architecture analysis, arguing that structural and statistical signals together improve anticipatory power.\nCrucially, \\citet{boettiger2012limits} quantified the statistical detection limits of these signals, showing that early-warning power is often negligible in short time series---a constraint directly relevant to iterative training, where the number of generations (typically 5--20) is far smaller than typical ecological datasets.\n\\citet{truong2025entropy} connects entropy collapse to critical transitions, characterizing it as a first-order phase transition with universality classes that determine whether classical early-warning signals retain predictive power.\nThe model collapse literature has not yet imported these methodological tools: existing canary studies neither frame their claims in terms of detection power under finite samples nor test whether observed lead-lag patterns survive the short-series constraints that \\citet{boettiger2012limits} identified as fundamental.\n\n\\paragraph{Lead-lag methodology.}\n\nGranger causality~\\cite{granger1969investigating} provides the standard econometric framework for testing whether one time series improves prediction of another beyond its own history.\n\\citet{shojaie2022granger} review classical and modern extensions, including VAR-based tests, kernel methods, and neural approaches for nonlinear dependencies.\nA key practical issue is non-stationarity: standard Granger tests applied to integrated (unit-root) series produce inflated rejection rates.\nThe Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.\nDespite wide use in economics and neuroscience, these methods are largely absent from the machine learning literature on iterative training.\nExisting canary studies rely on visual inspection or naive cross-correlation, which cannot distinguish genuine temporal precedence from shared non-stationary trends.\nOur framework applies five complementary methods---cross-correlation, standard Granger, Toda--Yamamoto, permutation Granger, and first-differenced regression---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse in iterative training.}\n\nThe phenomenon of iterative training collapse was formalized by \\citet{shumailov2024curse}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion across VAEs, GMMs, and language models, and by \\citet{alemohammad2024mad}, who demonstrated quality--diversity tradeoffs in self-consuming generative loops for image models.\nTheoretical analyses have since sharpened these results: \\citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, showing that even small fractions of synthetic data alter effective scaling behavior, while \\citet{dohmatob2025strong} proved that collapse can occur even when synthetic data constitutes a vanishingly small fraction of the training set.\nThe role of data accumulation has been a central theme.\n\\citet{dey2024breaking} proved that accumulating data across generations---rather than replacing it---prevents divergence of population risk in GMMs, HMMs, and language models.\n\\citet{kazdan2025collapse} systematically compared replace and accumulate regimes, finding that synthetic data value depends on the absolute quantity of co-present real data.\n\\citet{fu2025selfconsuming} provided generalization bounds for self-consuming loops, establishing that a constant fraction of real data suffices for convergence under accumulation.\nOn the calibration side, \\citet{he2025golden} showed that optimal real-data weighting converges to the golden-ratio inverse ($1/\\varphi \\approx 0.618$) in Gaussian and GLM settings, and that the risk landscape is non-monotone in mixing ratio---a theoretical prediction with implications for regime-dependent canary behavior.\nBeyond distributional statistics, \\citet{guo2024linguistic} documented progressive decline in lexical, syntactic, and semantic diversity across iterative fine-tuning generations, providing the multi-level diversity metrics that serve as downstream targets in our lead-lag analysis.\n\\citet{schaeffer2025position} catalogued eight distinct and sometimes contradictory definitions of ``model collapse'' in the literature, underscoring the importance of explicit operational definitions---a concern our framework addresses by scoping canary prediction to diversity metrics specifically.\n\n\\paragraph{Canary metrics and collapse monitoring.}\n\nSeveral recent works have proposed monitoring metrics that precede or accompany distributional degradation during iterative training.\n\\citet{du2026geometric} observe that calibration error rises before accuracy degrades in iteratively trained language models, interpreting this through a geometric-regulation lens.\n\\citet{chen2025scales} report a similar pattern across model scales and mixing ratios, noting that ECE increases of 75\\% appear at 30\\% synthetic contamination before accuracy drops become visible.\nBeyond calibration, SIGMA~\\cite{sigma2026spectral} introduces a dual-track spectral framework based on embedding Gram matrices, where divergence between deterministic and stochastic spectral bounds serves as an early collapse diagnostic.\n\\citet{kalinowski2026topology} proposes a topological monitoring approach using persistent homology features to detect multi-scale structural loss in representation space.\nDCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal and reports improvements in ECE and entropy preservation.\n\\citet{gambetta2024surplexity} introduces surplexity---a surprise-based metric that simultaneously detects collapse and filters training data---demonstrating that high-surplexity selection matches human-data baselines in maintaining distributional balance.\n\nThese works collectively demonstrate growing interest in collapse monitoring, yet they share methodological limitations that weaken their lead-lag claims.\nNone apply differencing tests to distinguish genuine temporal precedence from spurious co-trending; none cross-validate findings across multiple statistical methods; and none apply false discovery rate correction when testing multiple metric pairs.\nOur work differs from the closest predecessor, \\citet{du2026geometric}, in four respects:\n(i)~we compare an entire family of canary metrics rather than a single metric pair;\n(ii)~we cross-validate each lead-lag relationship across five independent statistical methods and quantify sensitivity to method choice via $d_{\\max}$;\n(iii)~we map detectability as a function of contamination regime rather than reporting a single aggregate result; and\n(iv)~we treat method-selection sensitivity itself as a primary finding, showing that it is the dominant source of variation in existing lead-lag conclusions.\n\n\\paragraph{Early-warning signals and critical transitions.}\n\nThe theoretical foundation for canary-based prediction of system failure originates in ecology and climate science.\n\\citet{scheffer2009early} established that complex systems approaching tipping points exhibit generic early-warning signals---rising autocorrelation and variance due to critical slowing down---independent of system-specific mechanisms.\n\\citet{scheffer2012anticipating} extended this framework by combining empirical warning indicators with network-architecture analysis, arguing that structural and statistical signals together improve anticipatory power.\nCrucially, \\citet{boettiger2012limits} quantified the statistical detection limits of these signals, showing that early-warning power is often negligible in short time series---a constraint directly relevant to iterative training, where the number of generations (typically 5--20) is far smaller than typical ecological datasets.\n\\citet{truong2025entropy} connects entropy collapse to critical transitions, characterizing it as a first-order phase transition with universality classes that determine whether classical early-warning signals retain predictive power.\nThe model collapse literature has not yet imported these methodological tools: existing canary studies neither frame their claims in terms of detection power under finite samples nor test whether observed lead-lag patterns survive the short-series constraints that \\citet{boettiger2012limits} identified as fundamental.\n\n\\paragraph{Lead-lag methodology.}\n\nGranger causality~\\cite{granger1969investigating} provides the standard econometric framework for testing whether one time series improves prediction of another beyond its own history.\n\\citet{shojaie2022granger} review classical and modern extensions, including VAR-based tests, kernel methods, and neural approaches for nonlinear dependencies.\nA key practical issue is non-stationarity: standard Granger tests applied to integrated (unit-root) series produce inflated rejection rates.\nThe Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.\nDespite wide use in economics and neuroscience, these methods are largely absent from the machine learning literature on iterative training.\nExisting canary studies rely on visual inspection or naive cross-correlation, which cannot distinguish genuine temporal precedence from shared non-stationary trends.\nOur framework applies five complementary methods---cross-correlation, standard Granger, Toda--Yamamoto, permutation Granger, and first-differenced regression---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:54:33.081398+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:54:33.081536+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper && echo \"=== 1. label check ===\" && grep -c 'label{sec:related_work}' related_work.tex && echo \"=== 2. all cite keys ===\" && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u && echo \"=== 3. verify keys in bib ===\" && for key in $(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//'); do grep -q \"$key\" references.bib && echo \"OK: $key\" || echo \"MISSING: $key\"; done && echo \"=== 4. forbidden phrases ===\" && grep -iE 'consistently outperforms|state-of-the-art|state of the art' related_work.tex || echo \"None found\" && grep -P '\\bsignificantly\\b' related_work.tex || echo \"No bare 'significantly'\" && echo \"=== 5. Du et al. 4 distinctions ===\" && grep -c '(i)' related_work.tex && grep -c '(ii)' related_work.tex && grep -c '(iii)' related_work.tex && grep -c '(iv)' related_work.tex && echo \"=== 6. word count ===\" && wc -w related_work.tex && echo \"=== 7. unique new cites (not in intro) ===\" && comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u) <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' introduction.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u)",
  "description": "Verify related_work.tex against all checklist items"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper && echo \"=== 1. label check ===\" && grep -c 'label{sec:related_work}' related_work.tex && echo \"=== 2. all cite keys ===\" && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u && echo \"=== 3. verify keys in bib ===\" && for key in $(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//'); do grep -q \"$key\" references.bib && echo \"OK: $key\" || echo \"MISSING: $key\"; done && echo \"=== 4. forbidden phrases ===\" && grep -iE 'consistently outperforms|state-of-the-art|state of the art' related_work.tex || echo \"None found\" && grep -P '\\bsignificantly\\b' related_work.tex || echo \"No bare 'significantly'\" && echo \"=== 5. Du et al. 4 distinctions ===\" && grep -c '(i)' related_work.tex && grep -c '(ii)' related_work.tex && grep -c '(iii)' related_work.tex && grep -c '(iv)' related_work.tex && echo \"=== 6. word count ===\" && wc -w related_work.tex && echo \"=== 7. unique new cites (not in intro) ===\" && comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u) <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' introduction.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u)",
    "description": "Verify related_work.tex against all checklist items"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:54:33.081678+00:00_

=== 1. label check ===
1
=== 2. all cite keys ===
alemohammad2024mad
boettiger2012limits
chen2025scales
dces2026counter
dey2024breaking
dohmatob2024tale
dohmatob2025strong
du2026geometric
fu2025selfconsuming
gambetta2024surplexity
granger1969investigating
guo2024linguistic
he2025golden
kalinowski2026topology
kazdan2025collapse
schaeffer2025position
scheffer2009early
scheffer2012anticipating
shojaie2022granger
shumailov2024curse
sigma2026spectral
truong2025entropy
=== 3. verify keys in bib ===
OK: shumailov2024curse
OK: alemohammad2024mad
OK: dohmatob2024tale
OK: dohmatob2025strong
OK: dey2024breaking
OK: kazdan2025collapse
OK: fu2025selfconsuming
OK: he2025golden
OK: guo2024linguistic
OK: schaeffer2025position
OK: du2026geometric
OK: chen2025scales
OK: sigma2026spectral
OK: kalinowski2026topology
OK: dces2026counter
OK: gambetta2024surplexity
OK: du2026geometric
OK: scheffer2009early
OK: scheffer2012anticipating
OK: boettiger2012limits
OK: truong2025entropy
OK: boettiger2012limits
OK: granger1969investigating
OK: shojaie2022granger
=== 4. forbidden phrases ===
None found
No bare 'significantly'
=== 5. Du et al. 4 distinctions ===
1
1
1
1
=== 6. word count ===
900 related_work.tex
=== 7. unique new cites (not in intro) ===
chen2025scales
dey2024breaking
dohmatob2024tale
dohmatob2025strong
fu2025selfconsuming
gambetta2024surplexity
granger1969investigating
guo2024linguistic
he2025golden
kalinowski2026topology
kazdan2025collapse
schaeffer2025position
truong2025entropy

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T195157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T19:54:33.081837+00:00_

All checks pass:

1. `\label{sec:related_work}` present
2. All 22 `\cite` keys verified in `references.bib` — zero missing
3. No forbidden phrases ("consistently outperforms", "state-of-the-art", bare "significantly")
4. Du et al. 4-point distinction (i)–(iv) all present
5. Word count: 900
6. 13 new citations introduced (not already in Introduction), well within budget

Section written to `docs/paper/related_work.tex` with 4 `\paragraph{}` blocks as specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260515T195157"
}
```

</details>

---
