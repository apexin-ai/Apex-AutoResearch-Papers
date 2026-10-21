# paper writing

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_20260522T185827.jsonl`
- **Structured JSON:** [`a7bc0ed73502f42cde8b.json`](../../sessions/a7/a7bc0ed73502f42cde8b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-22T19:02:12.552432+00:00_

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
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T19:02:12.552995+00:00_

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
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T19:02:12.553185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T19:02:12.553380+00:00_

1	\section{Experimental Methodology}
2	\label{sec:experiments}
3	
4	\subsection{Models and Panel Construction}
5	
6	We select 15 LLM judges spanning 6 provider families and 3 capability tiers, listed in Table~\ref{tab:models}. Nine models are accessed via the OpenRouter API; six open-weight models are served locally using vLLM~0.21.0 with AWQ INT4 quantization on an NVIDIA RTX~6000 (96\,GB). API models are assigned to \emph{frontier}, \emph{mid-tier}, or \emph{lightweight} tiers following the provider capability classification; all six local models fall into the lightweight tier, as INT4 quantization substantially reduces judge accuracy on the pairwise judgment task (Table~\ref{tab:models}). All panels consist of $K{=}3$ judges with majority-vote threshold $t{=}2$. Exhaustive enumeration yields $\binom{15}{3} = 455$ unique panels, covering every combination of families and tiers. Each panel evaluates all benchmark items under all attack types, producing a complete panel $\times$ item $\times$ attack tensor.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\begin{tabular}{lllccc}
12	\toprule
13	\textbf{Model} & \textbf{Family} & \textbf{Tier} & \textbf{Deploy} & \textbf{MMLU} & \textbf{ARC} \\
14	\midrule
15	gpt-5.5              & OpenAI    & frontier    & API   & .957 & .983 \\
16	gemini-3.1-pro-preview & Google  & frontier    & API   & .955 & .987 \\
17	claude-opus-4-6       & Anthropic & frontier   & API   & .890 & .987 \\
18	\addlinespace
19	gemini-3.5-flash      & Google    & mid-tier   & API   & .968 & 1.00$^\dagger$ \\
20	gpt-4.1               & OpenAI    & mid-tier   & API   & .837 & .967 \\
21	claude-sonnet-4-6     & Anthropic & mid-tier   & API   & .810 & .953 \\
22	\addlinespace
23	gpt-4.1-mini          & OpenAI    & lightweight & API  & .800 & .963 \\
24	gpt-4.1-nano          & OpenAI    & lightweight & API  & .633 & .853 \\
25	claude-3-haiku        & Anthropic & lightweight & API  & .767 & .450 \\
26	mistral-large (123B)  & Mistral   & lightweight & local
…[truncated 7008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T19:02:12.553533+00:00_

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
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T19:02:12.553726+00:00_

1	\section{Introduction}
2	
3	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work revealed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing on an implicit analogy to Byzantine fault tolerance (BFT), where majority voting among $n$ independent nodes tolerates up to $f < n/3$ faulty members \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reinforces this assumption, reporting that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
4	
5	Yet the evidence for diversity as a causal defense mechanism is weaker than it appears. The observed ASR reduction in multi-judge panels \citep{almasoud2026security} conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of the strongest members. No existing work disentangles these contributions. The theoretical justification rests on similarly uncertain ground: the strong data-processing inequality (SDPI) bounds joint failure in terms of effective independence, but assumes non-adaptive faults. BFT guarantees tolerate arbitrary failures up to a threshold count, yet do not model adversaries that observe panel composition and strategically select attacks \citep{schneier2000secrets}. When the threat shifts from random noise to adaptive manipulation, the assumptions underlying the diversity defense no longer hold.
6	
7	Adding more diverse judges to an evaluation panel predominantly increases, rather than decreases, vulnerability to adversaria
…[truncated 2671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T19:02:12.553902+00:00_

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
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T19:02:12.554063+00:00_

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
…[truncated 2937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T19:02:12.554230+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/ 2>/dev/null",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/ 2>/dev/null",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T19:02:12.554350+00:00_

acl.sty
acl_natbib.bst
analysis.tex
conclusion.tex
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
methodology.tex
references.bib
related_work.tex
results.tex
threat_model.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T19:02:12.554471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T19:02:12.554617+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	% [Main dual vulnerability driver results — to be written when P0 dominance analysis is finalized]
5	
6	\subsection{Aggregation Rules Modulate the Diversity Channel}
7	\label{sec:aggregation}
8	
9	The dual vulnerability driver effect varies substantially across aggregation methods. Table~\ref{tab:aggregation} reports regression results for each method across all 12 conditions.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\begin{tabular}{lcccc}
15	\toprule
16	\textbf{Method} & \textbf{$\eta_{\max}$ sig} & \textbf{$K_{\mathrm{eff}}$ sig} & \textbf{$K_{\mathrm{eff}}$ $\beta$ dir.} & \textbf{$R^2$} \\
17	\midrule
18	Threshold       & 12/12 & 11/12 & 10+/1$-$  & 0.890 \\
19	Majority        & 11/12 & 8/12  & 7+/1$-$   & 0.298 \\
20	Weighted        & 9/12  & 9/12  & 9+/0$-$   & 0.284 \\
21	Bayesian        & 9/12  & 7/12  & 1+/6$-$   & 0.104 \\
22	\bottomrule
23	\end{tabular}
24	\caption{Aggregation method comparison (15 models, 455 panels, log-log canonical spec). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Methods are ordered by $R^2$ to highlight the vulnerability gradient from threshold (most predictable) to Bayesian (least).}
25	\label{tab:aggregation}
26	\end{table}
27	
28	Four patterns emerge. First, the aggregation methods form a clear vulnerability gradient: threshold voting ($R^2{=}0.890$) makes panel composition almost perfectly predictive of attack success, while Bayesian calibration ($R^2{=}0.104$) compresses the ASR distribution so that compositional factors explain little variance. Second, Bayesian calibration reverses the diversity channel: $K_{\mathrm{eff}}$ significance rises from 8/12 (majority) to 7/12, but the coefficient direction flips from predominantly positive (7+/1$-$) to predominantly negative (1+/6$-$), meaning diversity shifts from harmful to largely protective under proper reliability calibration. Bayesian also partially weakens $\eta_{\ma
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T19:02:12.554888+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex",
  "content": "\\subsection{Dual Vulnerability Drivers}\n\\label{sec:dual_drivers}\n\nTable~\\ref{tab:dominance} reports the log-log regression results (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels constructed from the 15 judges in Table~\\ref{tab:models}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Attack} & $\\boldsymbol{\\eta_{\\max}}$ & $\\boldsymbol{K_{\\mathrm{eff}}}$ & \\textbf{Dom.} \\\\\n\\midrule\nMMLU & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\\\\nMMLU & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\\\\nMMLU & Score manip.   & $+^{*}$ & n.s.    & $\\eta$ \\\\\nMMLU & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\\\\nMMLU & Position bias  & $+^{*}$ & n.s.    & $\\eta$ \\\\\nMMLU & Authority bias & $+^{*}$ & n.s.    & $\\eta$ \\\\\n\\addlinespace\nARC  & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\\\\nARC  & Sycophancy     & $+^{*}$ & $-^{*}$ & Co \\\\\nARC  & Score manip.   & $+^{*}$ & $+^{*}$ & Co \\\\\nARC  & Verbosity      & $+^{*}$ & n.s.    & $\\eta$ \\\\\nARC  & Position bias  & n.s.    & $+^{*}$ & $K$ \\\\\nARC  & Authority bias & $+^{*}$ & $+^{*}$ & Co \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Standardized regression coefficients for $\\eta_{\\max}$ and $K_{\\mathrm{eff}}$ across 12 conditions (455 panels, log-log OLS). $+^{*}$/$-^{*}$: FDR-significant positive/negative (Benjamini--Hochberg, $q < 0.05$); n.s.: not significant. Dom.\\ column: $\\eta$ = $\\eta_{\\max}$ sole dominant, $K$ = $K_{\\mathrm{eff}}$ sole dominant, Co = co-dominant \\citep{budescu1993dominance}.}\n\\label{tab:dominance}\n\\end{table}\n\nThe weakest-link vulnerability $\\eta_{\\max}$ is the more consistent predictor, reaching FDR significance in 11 of 12 conditions. The sole exception is ARC $\\times$ position bias ($p = 0.909$). This near-universal significance confirms the prediction of Theorem~\\ref{thm:monotonicity}: the most vulnerable panel member is the primary channel through which adaptive attacks succeed.\n\nPanel diversity $K_{\\mathrm{eff}}$ is associated with \\emph{higher} ASR in 7 of 12 conditions (FDR-corrected positive $\\hat{\\beta}_{\\mathrm{std}}$), not significant in 4 conditions (MMLU $\\times$ \\{score manipulation, position bias, authority bias\\} and ARC $\\times$ verbosity), and significantly \\emph{negative} in 1 condition (ARC $\\times$ sycophancy, $\\hat{\\beta}_{\\mathrm{std}} = -0.192$, FDR $p = 0.010$). The 7-to-1 ratio of positive to negative significant effects establishes that diversity predominantly increases vulnerability under adaptive attack, counter to the non-adaptive prediction of the SDPI bound (\\S\\ref{sec:threat_model}).\n\nThe ARC $\\times$ sycophancy exception reveals the mechanism boundary predicted by the reversal analysis. Sycophancy exploits a cognitive bias shared across judge architectures: the tendency to favor agreeable, self-consistent responses. When the attack targets a bias common to all panel members, diverse judges dilute each other's susceptibility rather than expose distinct weaknesses for the adversary to exploit. This is the one regime where the BFT analogy holds, because faults are correlated across judges and diversity provides genuine protection.\n\nDominance analysis \\citep{budescu1993dominance} decomposes $R^2$ to assess each predictor's independent contribution (Table~\\ref{tab:dominance}, rightmost column). The relative importance of the two drivers is condition-dependent: $\\eta_{\\max}$ is the sole dominant predictor in 4 conditions, both predictors are co-dominant in 7, and $K_{\\mathrm{eff}}$ alone dominates in 1 (ARC $\\times$ position bias, where $\\eta_{\\max}$ is not significant). Neither predictor uniformly dominates the other, consistent with the threat model's prediction that the two vulnerability channels operate through distinct mechanisms (\\S\\ref{sec:threat_model}).\n\nThe correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ ($r = 0.70$) raises a confound concern: the positive diversity coefficient might merely proxy for weakest-link vulnerability. Dominance analysis addresses this directly, as $K_{\\mathrm{eff}}$ retains independent predictive power beyond $\\eta_{\\max}$ in 8 of 12 conditions (7 positive, 1 negative). The negative exception itself disproves pure confounding. If the $K_{\\mathrm{eff}}$ effect were entirely mediated by $\\eta_{\\max}$, the coefficient would be uniformly non-negative across conditions. The sign reversal in ARC $\\times$ sycophancy indicates that $K_{\\mathrm{eff}}$ captures a distinct mechanism that operates independently of the weakest-link channel.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex",
    "content": "\\subsection{Dual Vulnerability Drivers}\n\\label{sec:dual_drivers}\n\nTable~\\ref{tab:dominance} reports the log-log regression results (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels constructed from the 15 judges in Table~\\ref{tab:models}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Attack} & $\\boldsymbol{\\eta_{\\max}}$ & $\\boldsymbol{K_{\\mathrm{eff}}}$ & \\textbf{Dom.} \\\\\n\\midrule\nMMLU & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\\\\nMMLU & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\\\\nMMLU & Score manip.   & $+^{*}$ & n.s.    & $\\eta$ \\\\\nMMLU & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\\\\nMMLU & Position bias  & $+^{*}$ & n.s.    & $\\eta$ \\\\\nMMLU & Authority bias & $+^{*}$ & n.s.    & $\\eta$ \\\\\n\\addlinespace\nARC  & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\\\\nARC  & Sycophancy     & $+^{*}$ & $-^{*}$ & Co \\\\\nARC  & Score manip.   & $+^{*}$ & $+^{*}$ & Co \\\\\nARC  & Verbosity      & $+^{*}$ & n.s.    & $\\eta$ \\\\\nARC  & Position bias  & n.s.    & $+^{*}$ & $K$ \\\\\nARC  & Authority bias & $+^{*}$ & $+^{*}$ & Co \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Standardized regression coefficients for $\\eta_{\\max}$ and $K_{\\mathrm{eff}}$ across 12 conditions (455 panels, log-log OLS). $+^{*}$/$-^{*}$: FDR-significant positive/negative (Benjamini--Hochberg, $q < 0.05$); n.s.: not significant. Dom.\\ column: $\\eta$ = $\\eta_{\\max}$ sole dominant, $K$ = $K_{\\mathrm{eff}}$ sole dominant, Co = co-dominant \\citep{budescu1993dominance}.}\n\\label{tab:dominance}\n\\end{table}\n\nThe weakest-link vulnerability $\\eta_{\\max}$ is the more consistent predictor, reaching FDR significance in 11 of 12 conditions. The sole exception is ARC $\\times$ position bias ($p = 0.909$). This near-universal significance confirms the prediction of Theorem~\\ref{thm:monotonicity}: the most vulnerable panel member is the primary channel through which adaptive attacks succeed.\n\nPanel diversity $K_{\\mathrm{eff}}$ is associated with \\emph{higher} ASR in 7 of 12 conditions (FDR-corrected positive $\\hat{\\beta}_{\\mathrm{std}}$), not significant in 4 conditions (MMLU $\\times$ \\{score manipulation, position bias, authority bias\\} and ARC $\\times$ verbosity), and significantly \\emph{negative} in 1 condition (ARC $\\times$ sycophancy, $\\hat{\\beta}_{\\mathrm{std}} = -0.192$, FDR $p = 0.010$). The 7-to-1 ratio of positive to negative significant effects establishes that diversity predominantly increases vulnerability under adaptive attack, counter to the non-adaptive prediction of the SDPI bound (\\S\\ref{sec:threat_model}).\n\nThe ARC $\\times$ sycophancy exception reveals the mechanism boundary predicted by the reversal analysis. Sycophancy exploits a cognitive bias shared across judge architectures: the tendency to favor agreeable, self-consistent responses. When the attack targets a bias common to all panel members, diverse judges dilute each other's susceptibility rather than expose distinct weaknesses for the adversary to exploit. This is the one regime where the BFT analogy holds, because faults are correlated across judges and diversity provides genuine protection.\n\nDominance analysis \\citep{budescu1993dominance} decomposes $R^2$ to assess each predictor's independent contribution (Table~\\ref{tab:dominance}, rightmost column). The relative importance of the two drivers is condition-dependent: $\\eta_{\\max}$ is the sole dominant predictor in 4 conditions, both predictors are co-dominant in 7, and $K_{\\mathrm{eff}}$ alone dominates in 1 (ARC $\\times$ position bias, where $\\eta_{\\max}$ is not significant). Neither predictor uniformly dominates the other, consistent with the threat model's prediction that the two vulnerability channels operate through distinct mechanisms (\\S\\ref{sec:threat_model}).\n\nThe correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ ($r = 0.70$) raises a confound concern: the positive diversity coefficient might merely proxy for weakest-link vulnerability. Dominance analysis addresses this directly, as $K_{\\mathrm{eff}}$ retains independent predictive power beyond $\\eta_{\\max}$ in 8 of 12 conditions (7 positive, 1 negative). The negative exception itself disproves pure confounding. If the $K_{\\mathrm{eff}}$ effect were entirely mediated by $\\eta_{\\max}$, the coefficient would be uniformly non-negative across conditions. The sign reversal in ARC $\\times$ sycophancy indicates that $K_{\\mathrm{eff}}$ captures a distinct mechanism that operates independently of the weakest-link channel.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T19:02:12.555074+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T19:02:12.555219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex",
  "description": "Count words in output file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex",
    "description": "Count words in output file"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T19:02:12.555342+00:00_

585 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T19:02:12.555464+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex; grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex; echo \"---\"; grep -c \"Furthermore\\|Moreover\\|Additionally\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex; echo \"---\"; grep -c \"leverage\\|utilize\\|delve\\|facilitate\\|myriad\\|plethora\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex",
  "description": "Check for style violations (em-dash, en-dash, AI words)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex; grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex; echo \"---\"; grep -c \"Furthermore\\|Moreover\\|Additionally\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex; echo \"---\"; grep -c \"leverage\\|utilize\\|delve\\|facilitate\\|myriad\\|plethora\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex",
    "description": "Check for style violations (em-dash, en-dash, AI words)"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T19:02:12.555604+00:00_

---
0
---
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T19:02:12.555747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing[.,;]\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex | grep -v \"\\\\\\\\begin\\|\\\\\\\\end\\|label\\|midrule\\|toprule\\|bottomrule\\|spacing\\|string\\|testing\\|ordering\"",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing[.,;]\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results_main.tex | grep -v \"\\\\\\\\begin\\|\\\\\\\\end\\|label\\|midrule\\|toprule\\|bottomrule\\|spacing\\|string\\|testing\\|ordering\"",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T19:02:12.555866+00:00_

40:The correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ ($r = 0.70$) raises a confound concern: the positive diversity coefficient might merely proxy for weakest-link vulnerability. Dominance analysis addresses this directly, as $K_{\mathrm{eff}}$ retains independent predictive power beyond $\eta_{\max}$ in 8 of 12 conditions (7 positive, 1 negative). The negative exception itself disproves pure confounding. If the $K_{\mathrm{eff}}$ effect were entirely mediated by $\eta_{\max}$, the coefficient would be uniformly non-negative across conditions. The sign reversal in ARC $\times$ sycophancy indicates that $K_{\mathrm{eff}}$ captures a distinct mechanism that operates independently of the weakest-link channel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T185827",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T19:02:12.556039+00:00_

No style violations. The "confounding" match is a noun, not a trailing participial phrase.

Numbers consistency check against Introduction and Methodology:
- $K_\text{eff}$ significant: 7 positive + 1 negative = 8/12 total (matches aggregation table's Majority row: 8/12)
- $\eta_\text{max}$ significant: 11/12 (matches both Introduction and aggregation table)
- Dominance split: 4/7/1 (matches Introduction exactly)
- arc $\times$ sycophancy: $\hat{\beta}_\text{std} = -0.192$ (unique to this section, consistent with "significantly negative in 1")

File written to `docs/paper/results_main.tex`. ~400 words of prose plus a compact 12-row Table 2 (`tab:dominance`) showing significance directions and dominance classification for all conditions. Follows the 5-point narrative arc: $\eta_\text{max}$ consistency, $K_\text{eff}$ predominantly harmful, sycophancy exception as mechanism boundary, dominance analysis, confound resolution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260522T185827"
}
```

</details>

---
