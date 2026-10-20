# paper writing related work

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260522T133542.jsonl`
- **Structured JSON:** [`5b92136e982c171b3c8f.json`](../../sessions/5b/5b92136e982c171b3c8f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-22T13:38:36.061631+00:00_

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
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:38:36.062314+00:00_

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
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:38:36.062567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T13:38:36.062762+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \emph{judge bias}, where different judges assign systematically different scores to the same response, and \emph{benchmark contamination}, where models achieve inflated scores on items encountered during training. Both problems have received sustained research attention, producing separate toolkits for bias calibration and contamination detection. These toolkits treat the two distortions as independent phenomena, a separation that reflects their origins in different research communities rather than any principled argument for independence. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion in estimated abilities undermines all three. Yet a practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of $0.221 \pm 0.038$, while joint estimation achieves $0.124 \pm 0.016$, a 43.8\% reduction (Wilcoxon $p < 10^{-6}$). The gap does not arise from estimation noise or algorithmic limitations of individual methods; it reflects structural confounding between judge bias and contamination that no sequential pipeline can resolve.
5	
6	Existing judge bias correction methods remove systematic differences across judges without modeling contamination. CyclicJudge \citep{cyclicjudge2026} uses round-robin pairing to cancel average bias through balanced exposure of model pairs to all judges, but treats all residual score variation as genuine abilit
…[truncated 5675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T13:38:36.062915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T13:38:36.063105+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and non-centered parameterization for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.
17	
18	We enforce non-negativity of $c_n$ through a hierarchical prior: $c_n = \sigma_c \cdot z_n$ with $z_n \sim \text{HalfNormal}(1.0)$ and $\sigma_c \sim \text{HalfNormal}(1.0)$, reflecting the assumption that contamination can only inflate scores. The remaining priors are $\theta_n \sim \mathcal{N}(0
…[truncated 9989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T13:38:36.063436+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T13:38:36.063602+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T13:38:36.063724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T13:38:36.063842+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T13:38:36.063958+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\citep?\\{",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\citep?\\{",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T13:38:36.064172+00:00_

docs/paper/acl.sty:190:\renewcommand\cite{\citep}  % to get "(Author Year)" with natbib
docs/paper/background.tex:4:The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
docs/paper/background.tex:13:[Omitted long matching line]
docs/paper/background.tex:26:Let the full model be $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$ and the short model omit the contamination term: $\tilde{\eta}_{nijk} = \tilde{\theta}_n - \tilde{b}_i - \tilde{d}_j - \tau_k$. By the omitted variable bias (OVB) formula \citep{angrist2009mostly},
docs/paper/background.tex:36:[Omitted long matching line]
docs/paper/introduction.tex:4:[Omitted long matching line]
docs/paper/introduction.tex:6:[Omitted long matching line]
docs/paper/introduction.tex:8:[Omitted long matching line]
docs/paper/introduction.tex:10:[Omitted long matching line]
docs/paper/method.tex:9:G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
docs/paper/method.tex:31:\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\theta_n, b_i, d_j, c_n)$ jointly via NUTS \citep{betancourt2015}. The priors are as specified in \S\ref{sec:model_spec}. For $c_n$, we adopt the non-centered parameterization (NCP) specified in \S\ref{sec:model_spec} to avoid the funnel geometry that arises when a scale parameter and its associated latent variables are sampled together:
docs/paper/method.tex:38:This reparameterization decouples the posterior correlation between $\sigma_c$ and $z_n$, enabling more efficient exploration of the posterior geo
…[truncated 1211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T13:38:36.064384+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '\\\\\\\\cite[pt]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/*.tex | sort -u",
  "description": "Extract all unique citation keys from paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '\\\\\\\\cite[pt]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/*.tex | sort -u",
    "description": "Extract all unique citation keys from paper"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T13:38:36.064583+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T13:38:36.064715+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/literature_map*",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/literature_map*",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T13:38:36.064832+00:00_

literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T13:38:36.064944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T13:38:36.065137+00:00_

1	meta:
2	  last_updated: "2026-05-21T16:40:00Z"
3	  total_papers: 12
4	categories:
5	  - key: "psychometric_foundation"
6	    name: "Psychometric & IRT Foundation"
7	    narrative: "Core psychometric models: DG-IRT gating mechanism for cheating detection, MFRM applied to LLM raters, and IRT-based LLM evaluation frameworks"
8	  - key: "judge_bias_correction"
9	    name: "Judge Bias Correction"
10	    narrative: "Methods for detecting and correcting systematic biases in LLM-as-a-judge evaluation pipelines"
11	  - key: "contamination_detection"
12	    name: "Contamination Detection & Adjustment"
13	    narrative: "Methods for detecting and quantifying benchmark contamination in LLM evaluation"
14	  - key: "unified_evaluation"
15	    name: "Unified Evaluation Frameworks"
16	    narrative: "Comprehensive LLM evaluation frameworks and benchmarks that combine multiple assessment dimensions"
17	papers:
18	  shu2013dgirt:
19	    title: "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise"
20	    authors:
21	      - "Shu, Z."
22	      - "Henson, R."
23	      - "Luecht, R."
24	    year: 2013
25	    venue: "Psychometrika"
26	    doi: "10.1007/s11336-012-9311-3"
27	    bibtex_key: "shu2013dgirt"
28	    category: "psychometric_foundation"
29	    role: "foundation"
30	    relevance: "Core methodological inspiration. DG-IRT decomposes observed performance into genuine ability and cheating-inflated components via a gating mechanism. G-MFRM adapts this gating logic from educational cheating to LLM benchmark contamination."
31	    verified: false
32	    added_by: "director"
33	    added_at: "2026-05-21T16:40:00Z"
34	
35	  wang2025mfrm_llm:
36	    title: "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model"
37	    authors:
38	      - "Wang, Y."
39	    year: 2025
40	    venue: "arXiv"
41	    arxiv_id: "2505.18486"
42	    bibtex_key: "wang2025mfrm_llm"
43	    category: "psychometric_foundation"
44	    role: "foundation"

…[truncated 6393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T13:38:36.065406+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Judge Bias in LLM Evaluation.}\nLLM-as-a-judge protocols introduce systematic scoring differences across judges, and several recent methods target this bias in isolation. CyclicJudge \\citep{cyclicjudge2026} eliminates average bias through round-robin judge assignment that ensures balanced exposure of model pairs to all judges, but treats all residual score variation as genuine ability signal and provides no per-item diagnostics. UDA \\citep{uda2026} learns a neural K-factor adjustment that reduces inter-judge standard deviation by 63.4\\%, yet the learned correction is a black-box transformation with no interpretable decomposition of the severity parameter and no mechanism for contamination effects. \\citet{fiedler2026bias_uncertainty} formalize judge variability through $J/\\Delta J$ diagnostics from classical test theory, identifying sign-reversal failure modes when calibration is shared across judges with heterogeneous severity profiles. These methods model only the judge bias facet: contamination-induced score inflation is absorbed into the estimated abilities, producing the directional bias characterized in Section~\\ref{sec:confounding}.\n\n\\paragraph{Contamination Detection and Adjustment.}\nA parallel line of work quantifies benchmark contamination at the item or model level without accounting for judge effects. ConStat \\citep{constat2024} compares target model performance against a reference model to estimate contamination effects ($r^2 = 0.94$ with true contamination in controlled settings), establishing a principled quantification framework that G-MFRM's Stage~2 builds upon for exposure estimation. DCR \\citep{dcr2025} adjusts scores on suspected leaked items through fuzzy inference rules, while LogProber \\citep{logprober2024} detects memorization signatures from token-level log-probabilities under gray-box access. Perplexity-based methods such as Min-K\\% \\citep{mink2024} offer a simpler detection signal, but ConStat demonstrates that perplexity approaches are fundamentally evadable. All of these methods assume a fixed or averaged rater, so judge severity differences can masquerade as contamination signals. G-MFRM integrates contamination as a gated facet within the measurement model, separating both sources of distortion jointly rather than in sequence.\n\n\\paragraph{Preference Leakage.}\n\\citet{preference_leakage2026} identify a distinct contamination pathway on the judge side: when a judge model evaluates responses from a model in its own family, the judge exhibits inflated preference (same-family preference leakage score $\\approx$ 8.9\\%, same-model $\\approx$ 23.6\\%). This judge-side contamination is complementary to the examinee-side contamination that G-MFRM targets, where the evaluated model has encountered benchmark items during training. The two phenomena operate at different points in the evaluation pipeline. G-MFRM's judge severity parameter $d_j$ can partially capture preference leakage effects when they manifest as systematic scoring differences across judges, though a full treatment would require judge-model interaction terms beyond the current specification.\n\n\\paragraph{IRT and MFRM for LLM Evaluation.}\nItem Response Theory (IRT) provides the psychometric foundation for principled ability estimation in LLM evaluation. \\citet{jiao2025mfrm_llm} apply the Many-Facet Rasch Model to compare ten LLM raters with human experts, demonstrating that MFRM separates judge severity from examinee ability in this context, though their model includes no contamination term. PSN-IRT \\citep{lin2025psnirt} extends IRT to a neural four-parameter logistic framework that scales to large item pools but operates without judge or contamination facets. In educational measurement, \\citet{uto2020generalized} show that generalized many-facet models with additional parameters remain identifiable under Hamiltonian Monte Carlo estimation, a result that supports the feasibility of G-MFRM's extended parameterization. The closest methodological antecedent is DG-IRT \\citep{shu2013dgirt}, which uses binary gating to detect item preknowledge in educational testing. G-MFRM extends DG-IRT in three respects: continuous rather than binary exposure, explicit judge severity as a nuisance facet, and externally estimated exposure with formal identifiability guarantees (\\S\\ref{sec:identifiability}).\n\nThe common gap across these four research threads is the absence of a unified measurement model for judge bias and contamination. G-MFRM bridges this gap through its gated multi-facet structure, eliminating the structural confounding that no sequential pipeline can resolve (\\S\\ref{sec:confounding}), while the staged estimation with fixed exposure maintains the identifiability properties of the underlying MFRM.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Judge Bias in LLM Evaluation.}\nLLM-as-a-judge protocols introduce systematic scoring differences across judges, and several recent methods target this bias in isolation. CyclicJudge \\citep{cyclicjudge2026} eliminates average bias through round-robin judge assignment that ensures balanced exposure of model pairs to all judges, but treats all residual score variation as genuine ability signal and provides no per-item diagnostics. UDA \\citep{uda2026} learns a neural K-factor adjustment that reduces inter-judge standard deviation by 63.4\\%, yet the learned correction is a black-box transformation with no interpretable decomposition of the severity parameter and no mechanism for contamination effects. \\citet{fiedler2026bias_uncertainty} formalize judge variability through $J/\\Delta J$ diagnostics from classical test theory, identifying sign-reversal failure modes when calibration is shared across judges with heterogeneous severity profiles. These methods model only the judge bias facet: contamination-induced score inflation is absorbed into the estimated abilities, producing the directional bias characterized in Section~\\ref{sec:confounding}.\n\n\\paragraph{Contamination Detection and Adjustment.}\nA parallel line of work quantifies benchmark contamination at the item or model level without accounting for judge effects. ConStat \\citep{constat2024} compares target model performance against a reference model to estimate contamination effects ($r^2 = 0.94$ with true contamination in controlled settings), establishing a principled quantification framework that G-MFRM's Stage~2 builds upon for exposure estimation. DCR \\citep{dcr2025} adjusts scores on suspected leaked items through fuzzy inference rules, while LogProber \\citep{logprober2024} detects memorization signatures from token-level log-probabilities under gray-box access. Perplexity-based methods such as Min-K\\% \\citep{mink2024} offer a simpler detection signal, but ConStat demonstrates that perplexity approaches are fundamentally evadable. All of these methods assume a fixed or averaged rater, so judge severity differences can masquerade as contamination signals. G-MFRM integrates contamination as a gated facet within the measurement model, separating both sources of distortion jointly rather than in sequence.\n\n\\paragraph{Preference Leakage.}\n\\citet{preference_leakage2026} identify a distinct contamination pathway on the judge side: when a judge model evaluates responses from a model in its own family, the judge exhibits inflated preference (same-family preference leakage score $\\approx$ 8.9\\%, same-model $\\approx$ 23.6\\%). This judge-side contamination is complementary to the examinee-side contamination that G-MFRM targets, where the evaluated model has encountered benchmark items during training. The two phenomena operate at different points in the evaluation pipeline. G-MFRM's judge severity parameter $d_j$ can partially capture preference leakage effects when they manifest as systematic scoring differences across judges, though a full treatment would require judge-model interaction terms beyond the current specification.\n\n\\paragraph{IRT and MFRM for LLM Evaluation.}\nItem Response Theory (IRT) provides the psychometric foundation for principled ability estimation in LLM evaluation. \\citet{jiao2025mfrm_llm} apply the Many-Facet Rasch Model to compare ten LLM raters with human experts, demonstrating that MFRM separates judge severity from examinee ability in this context, though their model includes no contamination term. PSN-IRT \\citep{lin2025psnirt} extends IRT to a neural four-parameter logistic framework that scales to large item pools but operates without judge or contamination facets. In educational measurement, \\citet{uto2020generalized} show that generalized many-facet models with additional parameters remain identifiable under Hamiltonian Monte Carlo estimation, a result that supports the feasibility of G-MFRM's extended parameterization. The closest methodological antecedent is DG-IRT \\citep{shu2013dgirt}, which uses binary gating to detect item preknowledge in educational testing. G-MFRM extends DG-IRT in three respects: continuous rather than binary exposure, explicit judge severity as a nuisance facet, and externally estimated exposure with formal identifiability guarantees (\\S\\ref{sec:identifiability}).\n\nThe common gap across these four research threads is the absence of a unified measurement model for judge bias and contamination. G-MFRM bridges this gap through its gated multi-facet structure, eliminating the structural confounding that no sequential pipeline can resolve (\\S\\ref{sec:confounding}), while the staged estimation with fixed exposure maintains the identifiability properties of the underlying MFRM.\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:38:36.065664+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:38:36.065981+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "file=\"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex\" && echo \"=== Word count ===\" && wc -w \"$file\" && echo \"=== Em-dash check ===\" && grep -n \"—\" \"$file\" || echo \"No em-dash found\" && echo \"=== En-dash check ===\" && grep -n \" – \" \"$file\" || echo \"No en-dash found\" && echo \"=== Furthermore/Moreover/Additionally ===\" && grep -niE \"furthermore|moreover|additionally\" \"$file\" || echo \"None found\" && echo \"=== leverage/utilize/delve ===\" && grep -niE \"leverage|utilize|delve\" \"$file\" || echo \"None found\" && echo \"=== To our knowledge ===\" && grep -ni \"to our knowledge\" \"$file\" || echo \"None found\" && echo \"=== -ing phrase endings ===\" && grep -nE \"ing[,.]?\\s*$\" \"$file\" || echo \"None found\"",
  "description": "Verify related_work.tex against writing hard rules"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Bash",
  "tool_args": {
    "command": "file=\"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex\" && echo \"=== Word count ===\" && wc -w \"$file\" && echo \"=== Em-dash check ===\" && grep -n \"—\" \"$file\" || echo \"No em-dash found\" && echo \"=== En-dash check ===\" && grep -n \" – \" \"$file\" || echo \"No en-dash found\" && echo \"=== Furthermore/Moreover/Additionally ===\" && grep -niE \"furthermore|moreover|additionally\" \"$file\" || echo \"None found\" && echo \"=== leverage/utilize/delve ===\" && grep -niE \"leverage|utilize|delve\" \"$file\" || echo \"None found\" && echo \"=== To our knowledge ===\" && grep -ni \"to our knowledge\" \"$file\" || echo \"None found\" && echo \"=== -ing phrase endings ===\" && grep -nE \"ing[,.]?\\s*$\" \"$file\" || echo \"None found\"",
    "description": "Verify related_work.tex against writing hard rules"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:38:36.066451+00:00_

=== Word count ===
600 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex
=== Em-dash check ===
No em-dash found
=== En-dash check ===
No en-dash found
=== Furthermore/Moreover/Additionally ===
None found
=== leverage/utilize/delve ===
None found
=== To our knowledge ===
None found
=== -ing phrase endings ===
None found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T133542",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-22T13:38:36.066634+00:00_

All checks pass. Written to `docs/paper/related_work.tex`: 600 words, 4 clusters + positioning paragraph. No em-dash, no en-dash, no banned words, no -ing endings, no contribution claims. Citation keys match those used in the introduction and literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260522T133542"
}
```

</details>

---
