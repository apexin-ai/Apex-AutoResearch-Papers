# paper writing introduction v4

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_introduction_v4_20260522T174330.jsonl`
- **Structured JSON:** [`f42326950f4bd52266ff.json`](../../sessions/f4/f42326950f4bd52266ff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-22T17:46:00.820515+00:00_

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
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T17:46:00.821089+00:00_

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
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T17:46:00.821282+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T17:46:00.821421+00:00_

docs/paper/introduction.tex
docs/paper/methodology.tex
docs/paper/results.tex
docs/paper/analysis.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/threat_model.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T17:46:00.821544+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T17:46:00.821678+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T17:46:00.821824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T17:46:00.821982+00:00_

1	\section{Threat Model and Problem Formulation}
2	
3	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \lceil K/2 \rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised with marginal failure probability $\eta_j(a) = \Pr(X_j^a = 1)$, where $X_j^a \in \{0,1\}$ denotes the failure indicator. We write $\eta_{\max} = \max_j \eta_j$ for the vulnerability of the weakest judge. The \emph{panel attack success rate} is $\mathrm{ASR}(\mathcal{P}, a) = \Pr\!\bigl(\sum_{j=1}^K X_j^a \geq t\bigr)$.
4	
5	To quantify diversity, we define the \emph{effective independence} $K_{\mathrm{eff}}$ directly from pairwise mutual information among judges:
6	\begin{equation}
7	\label{eq:keff}
8	K_{\mathrm{eff}} = \frac{1}{K}\sum_{i=1}^{K} \Bigl[1 + \sum_{j \neq i} \exp\!\bigl(-2 \cdot \mathrm{MI}(i,j)\bigr)\Bigr].
9	\end{equation}
10	This formulation computes effective independence from pairwise MI estimates without matrix decomposition, and is more stable for small panels ($K{=}3$). It ranges from $K_{\mathrm{eff}} \approx K$ when judges are nearly independent ($\mathrm{MI} \to 0$) to $K_{\mathrm{eff}} \approx 1$ when judges are highly correlated ($\mathrm{MI} \to \infty$). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\eta_{\mathrm{joint}} \leq \min(1,\; K_{\mathrm{eff}} \cdot \eta_{\max})$, suggesting that diversity should help---but this bound assumes non-adaptive faults.
11	
12	\begin{definition}[Adaptive Adversary]
13	\label{def:adversary}
14	An \emph{adaptive adversary} has full knowledge of the panel composition $\mathcal{P}$, the per-judge vulnerability profiles $\{\eta_j(\cdot)\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \arg\max_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}, a)$ to maximize the panel ASR, yielding $\mathrm{ASR}^*(\mathcal{P}) = \sup_{a 
…[truncated 2922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T17:46:00.822123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T17:46:00.822279+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Evaluation Biases.}
4	The use of large language models as automatic evaluators gained traction after \citet{zheng2023judging} introduced MT-Bench and Chatbot Arena, establishing LLM judges as scalable alternatives to human annotation. Subsequent work documented systematic failure modes: \citet{wang2023fair} showed that individual LLM judges exhibit position bias, verbosity preferences, and sycophancy, all of which compromise evaluation reliability. Multi-judge panels have been proposed to mitigate these biases by aggregating decisions across diverse models. A recent systematization of knowledge on LLM-judge security \cite{almasoud2026security} reports that 7-model committees reduce attack success rates to 10--19\%, down from 50--68\% for individual open-source judges. However, this empirical observation lacks a causal explanation: it does not disentangle whether the reduction stems from judge diversity per se or from the inclusion of individually robust models. We address precisely this gap, providing the first controlled analysis that separates the contributions of panel diversity and individual judge robustness under adaptive attack.
5	
6	\paragraph{Adversarial Robustness and Transferability.}
7	Adversarial vulnerability in neural networks was formalized by \citet{goodfellow2015adversarial}, who showed that imperceptible input perturbations can cause misclassification. A key property of such adversarial examples is transferability: \citet{papernot2016transferability} demonstrated that adversarial inputs crafted for one model frequently fool others, and \citet{papernot2017practical} exploited this for black-box attacks via substitute models. \citet{tramer2018ensemble} showed that ensemble adversarial training improves robustness but does not eliminate cross-model vulnerability, because transferred perturbations remain effective across architectures. In the LLM domain, prompt injection attacks \cite{greshake2
…[truncated 4321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T17:46:00.822418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T17:46:00.822670+00:00_

1	% Bibliography for cert_manip_resist_eval
2	% All entries verified via WebSearch on 2026-05-22
3	% ============================================================
4	
5	% ============================================================
6	% Part A: Papers from literature_map.yaml (12 papers)
7	% ============================================================
8	
9	@article{robertson2025stepwise,
10	  author    = {Robertson, Zachary and Koyejo, Sanmi},
11	  title     = {Let's Measure Information Step-by-Step: {LLM}-Based Evaluation Beyond Vibes},
12	  journal   = {arXiv preprint arXiv:2508.05469},
13	  year      = {2025},
14	  url       = {https://arxiv.org/abs/2508.05469},
15	  note      = {arXiv:2508.05469}
16	}
17	
18	@inproceedings{yang2026diversity,
19	  author    = {Yang, Yingxuan and Qu, Chengrui and Wen, Muning and Shi, Laixi and Wen, Ying and Zhang, Weinan and Wierman, Adam and Gu, Shangding},
20	  title     = {Understanding Agent Scaling in {LLM}-Based Multi-Agent Systems via Diversity},
21	  booktitle = {ICLR 2026 Workshop on AIMS},
22	  year      = {2026},
23	  url       = {https://arxiv.org/abs/2602.03794},
24	  note      = {arXiv:2602.03794}
25	}
26	
27	@article{turkmen2026ensemble,
28	  author    = {Turkmen, Yigit and Buyukates, Baturalp and Bastopcu, Melih},
29	  title     = {Don't Always Pick the Highest-Performing Model: An Information Theoretic View of {LLM} Ensemble Selection},
30	  journal   = {arXiv preprint arXiv:2602.08003},
31	  year      = {2026},
32	  url       = {https://arxiv.org/abs/2602.08003},
33	  note      = {arXiv:2602.08003}
34	}
35	
36	@inproceedings{kaneko2025bits,
37	  author    = {Kaneko, Masahiro and Baldwin, Timothy},
38	  title     = {Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against {LLMs}},
39	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
40	  year      = {2025},
41	  url       = {https://arxiv.org/abs/2510.17000},
42	  note      = {arXiv:2510.17000. Spotlight}
43	}
44	

…[truncated 12184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T17:46:00.822847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T17:46:00.822976+00:00_

1	\section{Introduction}
2	% [PLACEHOLDER — waiting for plan\_001 results]
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T17:46:00.823210+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\nMulti-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work revealed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing on an implicit analogy to Byzantine fault tolerance (BFT), where majority voting among $n$ independent nodes tolerates up to $f < n/3$ faulty members \\citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reinforces this assumption, reporting that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.\n\nYet the evidence for diversity as a causal defense mechanism is weaker than it appears. The observed ASR reduction in multi-judge panels \\citep{almasoud2026security} conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of the strongest members. No existing work disentangles these contributions. The theoretical justification rests on similarly uncertain ground: the strong data-processing inequality (SDPI) bounds joint failure in terms of effective independence, but assumes non-adaptive faults. BFT guarantees tolerate arbitrary failures up to a threshold count, yet do not model adversaries that observe panel composition and strategically select attacks \\citep{schneier2000secrets}. When the threat shifts from random noise to adaptive manipulation, the assumptions underlying the diversity defense no longer hold.\n\nAdding more diverse judges to an evaluation panel does not just fail to help; it actively makes the panel more vulnerable to adversarial manipulation. The reversal mechanism is straightforward. Under random faults, independent judges fail via uncorrelated events, and majority voting aggregates away individual errors. Under an adaptive adversary, the picture inverts: functionally diverse judges respond to different manipulation strategies, and an adversary who observes the panel can exploit judge-specific vulnerabilities across a broader space of attacks \\citep{goodfellow2015adversarial,papernot2016transferability}. Diversity ceases to provide mutual protection and instead expands the viable attack surface. We call this the \\emph{diversity trap}: the same property that reduces vulnerability under random faults increases it under strategic attack.\n\nControlled experiments across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks (MMLU, ARC) confirm this reversal across all 12 experimental conditions. Effective independence $K_{\\mathrm{eff}}$, a pairwise-MI-based diversity metric, shows a statistically significant positive association with panel attack success rate (FDR-corrected) in 12 out of 12 conditions in raw regression. After residualizing $K_{\\mathrm{eff}}$ against the maximum individual vulnerability $\\eta_{\\max}$ (VIF${=}1.00$), the diversity effect remains significant in 8 of 12 conditions, which confirms an independent predictive contribution beyond what individual robustness explains. The weakest-judge channel $\\eta_{\\max}$ is significant in 9 of 12 conditions. The two drivers exhibit condition-dependent dominance: $\\eta_{\\max}$ dominates under bias-based attacks, while $K_{\\mathrm{eff}}$ dominates under transferable attacks, including 2 conditions where $K_{\\mathrm{eff}}$ is the sole significant predictor.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Diversity trap and dual vulnerability drivers.} The first empirical quantification showing that panel diversity ($K_{\\mathrm{eff}}$) independently and positively predicts vulnerability under adaptive attack, across 15 models, 455 panels, and residualized analysis that isolates its contribution from individual judge robustness (\\S\\ref{sec:experiments}).\n\\item \\textbf{BFT reversal mechanism.} Formal and empirical demonstration of why diversity helps under random faults but hurts under adaptive adversaries, with condition-dependent importance patterns that reveal when each vulnerability channel dominates (\\S\\ref{sec:threat_model}, \\S\\ref{sec:analysis}).\n\\item \\textbf{Robustness-first panel design.} An actionable defense combining robustness screening with reliability-weighted aggregation that addresses both vulnerability channels (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\nMulti-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work revealed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing on an implicit analogy to Byzantine fault tolerance (BFT), where majority voting among $n$ independent nodes tolerates up to $f < n/3$ faulty members \\citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reinforces this assumption, reporting that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.\n\nYet the evidence for diversity as a causal defense mechanism is weaker than it appears. The observed ASR reduction in multi-judge panels \\citep{almasoud2026security} conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of the strongest members. No existing work disentangles these contributions. The theoretical justification rests on similarly uncertain ground: the strong data-processing inequality (SDPI) bounds joint failure in terms of effective independence, but assumes non-adaptive faults. BFT guarantees tolerate arbitrary failures up to a threshold count, yet do not model adversaries that observe panel composition and strategically select attacks \\citep{schneier2000secrets}. When the threat shifts from random noise to adaptive manipulation, the assumptions underlying the diversity defense no longer hold.\n\nAdding more diverse judges to an evaluation panel does not just fail to help; it actively makes the panel more vulnerable to adversarial manipulation. The reversal mechanism is straightforward. Under random faults, independent judges fail via uncorrelated events, and majority voting aggregates away individual errors. Under an adaptive adversary, the picture inverts: functionally diverse judges respond to different manipulation strategies, and an adversary who observes the panel can exploit judge-specific vulnerabilities across a broader space of attacks \\citep{goodfellow2015adversarial,papernot2016transferability}. Diversity ceases to provide mutual protection and instead expands the viable attack surface. We call this the \\emph{diversity trap}: the same property that reduces vulnerability under random faults increases it under strategic attack.\n\nControlled experiments across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks (MMLU, ARC) confirm this reversal across all 12 experimental conditions. Effective independence $K_{\\mathrm{eff}}$, a pairwise-MI-based diversity metric, shows a statistically significant positive association with panel attack success rate (FDR-corrected) in 12 out of 12 conditions in raw regression. After residualizing $K_{\\mathrm{eff}}$ against the maximum individual vulnerability $\\eta_{\\max}$ (VIF${=}1.00$), the diversity effect remains significant in 8 of 12 conditions, which confirms an independent predictive contribution beyond what individual robustness explains. The weakest-judge channel $\\eta_{\\max}$ is significant in 9 of 12 conditions. The two drivers exhibit condition-dependent dominance: $\\eta_{\\max}$ dominates under bias-based attacks, while $K_{\\mathrm{eff}}$ dominates under transferable attacks, including 2 conditions where $K_{\\mathrm{eff}}$ is the sole significant predictor.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Diversity trap and dual vulnerability drivers.} The first empirical quantification showing that panel diversity ($K_{\\mathrm{eff}}$) independently and positively predicts vulnerability under adaptive attack, across 15 models, 455 panels, and residualized analysis that isolates its contribution from individual judge robustness (\\S\\ref{sec:experiments}).\n\\item \\textbf{BFT reversal mechanism.} Formal and empirical demonstration of why diversity helps under random faults but hurts under adaptive adversaries, with condition-dependent importance patterns that reveal when each vulnerability channel dominates (\\S\\ref{sec:threat_model}, \\S\\ref{sec:analysis}).\n\\item \\textbf{Robustness-first panel design.} An actionable defense combining robustness screening with reliability-weighted aggregation that addresses both vulnerability channels (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T17:46:00.823421+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_v4_20260522T174330",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T17:46:00.823593+00:00_

Introduction 已写入 `docs/paper/introduction.tex`。~630 words，5段 + 贡献列表结构。

要点核查：
- 所有引用 key 均来自 `references.bib`
- 数字与 framing doc 一致（12/12, 8/12, 9/12, 15 models, 455 panels, VIF=1.00）
- 术语与 `threat_model.tex` 一致（$K_{\mathrm{eff}}$, $\eta_{\max}$, SDPI, adaptive adversary, reversal mechanism）
- 无 em-dash、无 -ing 短语结尾、无 AI 风格词、无 "In this paper"
- "significantly" 仅在 FDR 检验支撑下使用
- 贡献条目带 section 引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_v4_20260522T174330"
}
```

</details>

---
