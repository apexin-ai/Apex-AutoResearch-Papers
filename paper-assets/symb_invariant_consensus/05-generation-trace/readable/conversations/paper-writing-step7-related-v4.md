# paper writing step7 related v4

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_step7_related_v4_20260523T041124.jsonl`
- **Structured JSON:** [`01335f0357f578e643da.json`](../../sessions/01/01335f0357f578e643da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T04:14:12.332094+00:00_

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
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T04:14:12.332748+00:00_

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
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T04:14:12.333021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T04:14:12.333209+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-Consistency and extensions.}
6	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early; \citet{byerly2026selfconsistency} further analyze SC's limitations in mathematical reasoning. The Condorcet Jury Theorem \citep{condorcet1785} guarantees convergence under independent voting; \citet{ladha1992correlated} show correlated voters reduce effective ensemble size. Our $K_\text{eff}$ adapts Fleiss' $\kappa$ from ensemble diversity theory \citep{kuncheva2003measures, brown2005diversity}, explaining the plateau: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:results}). \citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \citet{kuai2026independent} propose BEI and CIG for cross-model independence auditing, complementary to our within-model process-$\kappa$. Symbolic confirmation bias is distinct from CoT unfaithfulness \citep{turpin2024language} and CoT-level confirmation bias \citep{wan2025unveiling, jhaveri2026failing}: the latter concern whether reasoning reflects actual computation, while symbolic confirmation bias concerns whether \emph{self-extracted formal constraints} mirror the model's answer distribution.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning and test-time verification.}
10	We distinguish three paradigms: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} translates problems into formal specifications before answering (LINC documents ${\sim}$40\% translation
…[truncated 2613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T04:14:12.333388+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sec:pipeline|d-separation|causal-dag|C \\\\perp|information bottleneck",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sec:pipeline|d-separation|causal-dag|C \\\\perp|information bottleneck",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T04:14:12.333541+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-91-  {$C \!\perp\! Y \mid A$};
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-92-\end{tikzpicture}
docs/paper/analysis.tex:93:\caption{Causal DAG of the self-extraction pipeline. All information about ground truth $Y$ reaching constraints $C$ is mediated by answer $A$ ($C \perp Y \mid A$; Proposition~1, Part~\textit{ii}), making self-verification inherently answer-biased.}
docs/paper/analysis.tex:94:\label{fig:causal-dag}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-95-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-96-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex-4-\subsection{SICA Pipeline}
docs/paper/method.tex:5:\label{sec:pipeline}
docs/paper/method.tex-6-\label{sec:condorcet}
docs/paper/method.tex-7-\label{sec:effective-k}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-5-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-6-\looseness=-1
docs/paper/introduction.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-9-\looseness=-1
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-267-\@LN{193}{2}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-268-\@writefile{toc}{\contentsl
…[truncated 1739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T04:14:12.333715+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sec:confirmation-bias|Proposition.?1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sec:confirmation-bias|Proposition.?1",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T04:14:12.333846+00:00_

5:\label{sec:confirmation-bias}
11:\textbf{Proposition 1} \textit{(Symbolic Confirmation Bias is Structural).}\;%
93:\caption{Causal DAG of the self-extraction pipeline. All information about ground truth $Y$ reaching constraints $C$ is mediated by answer $A$ ($C \perp Y \mid A$; Proposition~1, Part~\textit{ii}), making self-verification inherently answer-biased.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T04:14:12.334006+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex | sort",
  "description": "Extract all citation keys from related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex | sort",
    "description": "Extract all citation keys from related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T04:14:12.334137+00:00_

\citep{chen2024usc}
\citep{chen2025sets}
\citep{cobbe2021gsm8k, lightman2024prm, wang2024mathshepherd}
\citep{condorcet1785}
\citep{dhuliawala2023chainofverification}
\citep{gao2023pal, chen2023program, lyu2023faithful}
\citep{gou2024critic}
\citep{guo2025deepseekr1, qwen2024qwq}
\citep{kuncheva2003measures, brown2005diversity}
\citep{li2023diverse}
\citep{liang2023encouraging, du2023improving}
\citep{lifshitz2025mav}
\citep{madaan2023selfrefine}
\citep{olausson2023linc, amonkar2025realitycheck}
\citep{pan2023logiclm, olausson2023linc, ye2024satlm}
\citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}
\citep{snell2025scaling}
\citep{taubenfeld2025cisc}
\citep{toh2024notallvotes}
\citep{turpin2024language}
\citep{wan2024rasc, kim2026reasc}
\citep{wan2025unveiling, jhaveri2026failing}
\citep{wang2023sc}
\citep{weng2023selfverification}
\citep{yao2023tree}
\citep{zhu2025vericot}
\citet{amonkar2025realitycheck}
\citet{byerly2026selfconsistency}
\citet{chan2026position}
\citet{huang2024selfcorrect}
\citet{kim2025correlated}
\citet{kuai2026independent}
\citet{ladha1992correlated}
\citet{loo2025reevaluating}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T04:14:12.334378+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\looseness=-1\n\\paragraph{Self-consistency and ensemble theory.}\nSelf-consistency (SC) selects the most frequent answer across chain-of-thought traces \\citep{wang2023sc}. Extensions address free-form generation \\citep{chen2024usc}, confidence weighting \\citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \\citep{li2023diverse}, program-based vote filtering \\citep{toh2024notallvotes}, and reasoning-aware filtering \\citep{wan2024rasc, kim2026reasc}. SC gains plateau early \\citep{loo2025reevaluating}, particularly in mathematical reasoning \\citep{byerly2026selfconsistency}. The Condorcet Jury Theorem \\citep{condorcet1785} guarantees majority-vote convergence under independent voting; \\citet{ladha1992correlated} show correlated voters reduce effective ensemble size. Our $K_\\text{eff}$ adapts Fleiss' $\\kappa$ from ensemble diversity theory \\citep{kuncheva2003measures, brown2005diversity} to quantify this compression (\\S\\ref{sec:pipeline}). \\citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \\citet{kuai2026independent} propose cross-model independence auditing, complementary to our within-model process-$\\kappa$. Symbolic confirmation bias is distinct from CoT unfaithfulness \\citep{turpin2024language} and CoT-level confirmation bias \\citep{wan2025unveiling, jhaveri2026failing}: the latter concern whether reasoning reflects actual computation, while symbolic confirmation bias concerns whether self-extracted formal constraints mirror the model's answer distribution.\n\n\\looseness=-1\n\\paragraph{Neuro-symbolic reasoning.}\nWe distinguish three paradigms: \\emph{specification-generation} \\citep{pan2023logiclm, olausson2023linc, ye2024satlm} translates problems into formal specifications before answering; \\emph{program-generation} \\citep{gao2023pal, chen2023program, lyu2023faithful} produces executable code; both formalize \\emph{before} answer generation. \\emph{Trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\\S\\ref{sec:confirmation-bias}). Recent extensions expand these paradigms with symbolic planning, logic agents, and verified reasoning \\citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \\citet{amonkar2025realitycheck} show formalization quality degrades with problem complexity; \\citet{chan2026position} argue logical soundness alone is unreliable for neurosymbolic verification. Prior studies \\citep{olausson2023linc, amonkar2025realitycheck} note high formalization error rates but treat them as quality problems; we show the errors are \\emph{systematically biased} toward the model's answer. Proposition~1 establishes that self-extracted constraints are d-separated from ground truth given the answer ($C \\perp Y \\mid A$; Figure~\\ref{fig:causal-dag}), making self-verification an information bottleneck. \\citet{huang2024selfcorrect} prove LLMs cannot self-correct in natural language without external feedback; we extend this to formal verification, showing that provably sound solvers add no information beyond majority voting when constraints are self-extracted.\n\n\\looseness=-1\n\\paragraph{Test-time compute and self-verification.}\nScaling test-time compute via additional traces \\citep{snell2025scaling}, structured search \\citep{yao2023tree}, or extended reasoning \\citep{guo2025deepseekr1, qwen2024qwq} faces the same correlation challenge when traces share a single model's biases. Trained verifiers \\citep{cobbe2021gsm8k, lightman2024prm, wang2024mathshepherd} sidestep this with external reward signals. Multi-agent debate \\citep{liang2023encouraging, du2023improving}, self-verification \\citep{weng2023selfverification}, chain-of-verification \\citep{dhuliawala2023chainofverification}, self-refinement \\citep{madaan2023selfrefine}, tool-augmented critique \\citep{gou2024critic}, formal CoT verification \\citep{zhu2025vericot}, trained verification signals \\citep{chen2025sets}, and multi-agent verification \\citep{lifshitz2025mav} report gains, but none tests self-extracted constraints under formal solvers. We find the bottleneck lies in constraint extraction, not verification: self-extracted constraints inherit the model's bias regardless of solver soundness (\\S\\ref{sec:confirmation-bias}). Oracle controls confirm the verification mechanism itself is sound (Appendix~\\ref{app:oracle}).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\looseness=-1\n\\paragraph{Self-consistency and ensemble theory.}\nSelf-consistency (SC) selects the most frequent answer across chain-of-thought traces \\citep{wang2023sc}. Extensions address free-form generation \\citep{chen2024usc}, confidence weighting \\citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \\citep{li2023diverse}, program-based vote filtering \\citep{toh2024notallvotes}, and reasoning-aware filtering \\citep{wan2024rasc, kim2026reasc}. SC gains plateau early \\citep{loo2025reevaluating}, particularly in mathematical reasoning \\citep{byerly2026selfconsistency}. The Condorcet Jury Theorem \\citep{condorcet1785} guarantees majority-vote convergence under independent voting; \\citet{ladha1992correlated} show correlated voters reduce effective ensemble size. Our $K_\\text{eff}$ adapts Fleiss' $\\kappa$ from ensemble diversity theory \\citep{kuncheva2003measures, brown2005diversity} to quantify this compression (\\S\\ref{sec:pipeline}). \\citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \\citet{kuai2026independent} propose cross-model independence auditing, complementary to our within-model process-$\\kappa$. Symbolic confirmation bias is distinct from CoT unfaithfulness \\citep{turpin2024language} and CoT-level confirmation bias \\citep{wan2025unveiling, jhaveri2026failing}: the latter concern whether reasoning reflects actual computation, while symbolic confirmation bias concerns whether self-extracted formal constraints mirror the model's answer distribution.\n\n\\looseness=-1\n\\paragraph{Neuro-symbolic reasoning.}\nWe distinguish three paradigms: \\emph{specification-generation} \\citep{pan2023logiclm, olausson2023linc, ye2024satlm} translates problems into formal specifications before answering; \\emph{program-generation} \\citep{gao2023pal, chen2023program, lyu2023faithful} produces executable code; both formalize \\emph{before} answer generation. \\emph{Trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\\S\\ref{sec:confirmation-bias}). Recent extensions expand these paradigms with symbolic planning, logic agents, and verified reasoning \\citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \\citet{amonkar2025realitycheck} show formalization quality degrades with problem complexity; \\citet{chan2026position} argue logical soundness alone is unreliable for neurosymbolic verification. Prior studies \\citep{olausson2023linc, amonkar2025realitycheck} note high formalization error rates but treat them as quality problems; we show the errors are \\emph{systematically biased} toward the model's answer. Proposition~1 establishes that self-extracted constraints are d-separated from ground truth given the answer ($C \\perp Y \\mid A$; Figure~\\ref{fig:causal-dag}), making self-verification an information bottleneck. \\citet{huang2024selfcorrect} prove LLMs cannot self-correct in natural language without external feedback; we extend this to formal verification, showing that provably sound solvers add no information beyond majority voting when constraints are self-extracted.\n\n\\looseness=-1\n\\paragraph{Test-time compute and self-verification.}\nScaling test-time compute via additional traces \\citep{snell2025scaling}, structured search \\citep{yao2023tree}, or extended reasoning \\citep{guo2025deepseekr1, qwen2024qwq} faces the same correlation challenge when traces share a single model's biases. Trained verifiers \\citep{cobbe2021gsm8k, lightman2024prm, wang2024mathshepherd} sidestep this with external reward signals. Multi-agent debate \\citep{liang2023encouraging, du2023improving}, self-verification \\citep{weng2023selfverification}, chain-of-verification \\citep{dhuliawala2023chainofverification}, self-refinement \\citep{madaan2023selfrefine}, tool-augmented critique \\citep{gou2024critic}, formal CoT verification \\citep{zhu2025vericot}, trained verification signals \\citep{chen2025sets}, and multi-agent verification \\citep{lifshitz2025mav} report gains, but none tests self-extracted constraints under formal solvers. We find the bottleneck lies in constraint extraction, not verification: self-extracted constraints inherit the model's bias regardless of solver soundness (\\S\\ref{sec:confirmation-bias}). Oracle controls confirm the verification mechanism itself is sound (Appendix~\\ref{app:oracle}).\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T04:14:12.334613+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T04:14:12.334762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T04:14:12.334931+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions address free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating}, particularly in mathematical reasoning \citep{byerly2026selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independent voting; \citet{ladha1992correlated} show correlated voters reduce effective ensemble size. Our $K_\text{eff}$ adapts Fleiss' $\kappa$ from ensemble diversity theory \citep{kuncheva2003measures, brown2005diversity} to quantify this compression (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \citet{kuai2026independent} propose cross-model independence auditing, complementary to our within-model process-$\kappa$. Symbolic confirmation bias is distinct from CoT unfaithfulness \citep{turpin2024language} and CoT-level confirmation bias \citep{wan2025unveiling, jhaveri2026failing}: the latter concern whether reasoning reflects actual computation, while symbolic confirmation bias concerns whether self-extracted formal constraints mirror the model's answer distribution.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	We distinguish three paradigms: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} translates problems into formal specifications before answering; \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} produces executable code; both formalize \emph{before} answer generation. \emph{Trace-extract
…[truncated 2452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T04:14:12.335094+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && echo \"=== Paragraph count ===\" && grep -c '\\\\paragraph' related_work.tex && echo \"=== SCB check ===\" && grep -n 'SCB' related_work.tex || echo \"No SCB found\" && echo \"=== Em-dash check ===\" && grep -n '—' related_work.tex || echo \"No em-dash found\" && echo \"=== En-dash check (non-range) ===\" && grep -n ' – ' related_work.tex || echo \"No en-dash found\" && echo \"=== Word count (approximate) ===\" && cat related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/%.*//g' | wc -w && echo \"=== Citation keys in new file ===\" && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//; s/}//; s/ //g' | sort -u",
  "description": "Verify paragraph count, no SCB, no em-dash, word count, and citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && echo \"=== Paragraph count ===\" && grep -c '\\\\paragraph' related_work.tex && echo \"=== SCB check ===\" && grep -n 'SCB' related_work.tex || echo \"No SCB found\" && echo \"=== Em-dash check ===\" && grep -n '—' related_work.tex || echo \"No em-dash found\" && echo \"=== En-dash check (non-range) ===\" && grep -n ' – ' related_work.tex || echo \"No en-dash found\" && echo \"=== Word count (approximate) ===\" && cat related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/%.*//g' | wc -w && echo \"=== Citation keys in new file ===\" && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//; s/}//; s/ //g' | sort -u",
    "description": "Verify paragraph count, no SCB, no em-dash, word count, and citation keys"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T04:14:12.335247+00:00_

=== Paragraph count ===
3
=== SCB check ===
No SCB found
=== Em-dash check ===
No em-dash found
=== En-dash check (non-range) ===
No en-dash found
=== Word count (approximate) ===
354
=== Citation keys in new file ===
amonkar2025realitycheck
brown2005diversity
byerly2026selfconsistency
chan2026position
chen2023program
chen2024usc
chen2025sets
cobbe2021gsm8k
condorcet1785
dhuliawala2023chainofverification
du2023improving
gao2023pal
gou2024critic
guo2025deepseekr1
huang2024selfcorrect
jhaveri2026failing
kim2025correlated
kim2026reasc
kuai2026independent
kuncheva2003measures
ladha1992correlated
li2023diverse
li2025aristotle
liang2023encouraging
lifshitz2025mav
lightman2024prm
loo2025reevaluating
luo2025logicagent
lyu2023faithful
madaan2023selfrefine
miya2025eidoku
olausson2023linc
pan2023logiclm
qwen2024qwq
ryu2025clover
singh2026verge
snell2025scaling
taubenfeld2025cisc
toh2024notallvotes
turpin2024language
wan2024rasc
wan2025unveiling
wang2023sc
wang2024mathshepherd
wang2025fover
weng2023selfverification
xu2026dylos
yao2023tree
ye2024satlm
zhu2025vericot

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T04:14:12.335445+00:00_

All checks pass:

1. **3 \paragraph segments** — confirmed
2. **No "SCB"** — confirmed
3. **All 50 citation keys preserved** — confirmed (matched against original)
4. **Positioning merged into paragraph 2 end** — Proposition 1 d-separation argument + huang2024selfcorrect distinction included; BR/p-value numbers removed
5. **Word count ~494 rendered** (354 text-only + ~140 from rendered citations) — within ≤550 budget
6. **No em-dash** — confirmed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_step7_related_v4_20260523T041124"
}
```

</details>

---
