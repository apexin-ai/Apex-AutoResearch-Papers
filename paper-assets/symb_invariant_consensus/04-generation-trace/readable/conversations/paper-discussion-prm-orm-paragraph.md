# paper discussion prm orm paragraph

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_discussion-prm-orm-paragraph_20260525T053441.jsonl`
- **Structured JSON:** [`25b33770566010915705.json`](../../sessions/25/25b33770566010915705.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-25T05:36:21.557348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T05:36:21.557846+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	\label{sec:conclusion}
4	\enlargethispage{\baselineskip}
5	
6	\looseness=-1
7	Our central finding is that formal verification's value depends on the \emph{independence} of its inputs, not the soundness of its logic. SICA reduces to majority vote under source-attribution scoring (Observation~1), and 27 training-free variants fail to escape; symbolic confirmation bias holds across nine models (7B to frontier). Three zero-cost diagnostics predict failure from a $K{=}12$ pilot (\S\ref{sec:diagnostic-framework}); cross-architecture verification escapes the bottleneck only when the verifier exceeds generator accuracy (\S\ref{sec:cross-arch}), suggesting \emph{architectural diversity} over scale. Our DPI bound $I(C;Y) \leq I(T;Y)$ further explains why trained verifiers \citep{lightman2024prm,wang2024mathshepherd} succeed (they break the $M{\to}T{\to}A{\to}C$ chain with external signal) and why same-model scaling saturates at $K_\text{eff}$.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T05:36:21.558136+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cobbe|math.shepherd|grace|verifier.*math|khalifa",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "output_mode": "content",
  "-i": "True",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cobbe|math.shepherd|grace|verifier.*math|khalifa",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "output_mode": "content",
    "-i": "True",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T05:36:21.558319+00:00_

173-
174-%%% Verification and Reranking %%%
175-
176:@article{cobbe2021gsm8k,
177:  title={Training Verifiers to Solve Math Word Problems},
178:  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
179-  journal={arXiv preprint arXiv:2110.14168},
180-  year={2021}
181-}
182-
183-@inproceedings{lightman2024prm,
184-  title={Let's Verify Step by Step},
185:  author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
186-  booktitle={ICLR},
187-  year={2024}
188-}
189-
190-@inproceedings{wang2024mathshepherd,
191:  title={Math-Shepherd: Verify and Reinforce {LLM}s Step-by-step without Human Annotations},
192-  author={Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, R.X. and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Y. and Sui, Zhifang},
193-  booktitle={ACL},
194-  year={2024}
195-}
196-
197:@inproceedings{khalifa2023grace,
198:  title={{GRACE}: Discriminator-Guided Chain-of-Thought Reasoning},
199:  author={Khalifa, Muhammad and Logeswaran, Lajanugen and Lee, Moontae and Lee, Honglak and Wang, Lu},
200-  booktitle={Findings of EMNLP},
201-  year={2023}
202-}
--
474-%%% Programs-as-Verifiers %%%
475-
476-@article{toh2024notallvotes,
477:  title={Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning},
478-  author={Toh, Vernon Y.H. and Ghosal, Deepanway and Poria, Soujanya},
479-  journal={arXiv preprint arXiv:2410.12608},
480-  year={2024}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T05:36:21.558470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T05:36:21.558701+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer, a persistent empirical property of zero-shot self-extraction pipelines, not a cognitive bias analogy. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer (bias ratio $4.97\times$; Table~\ref{tab:cross-model-bias}), and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on ${\geq}99\%$ of problems across all weight settings $\alpha$ (Table~\ref{tab:alpha-ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting.
8	
9	\looseness=-1 Crucially, BR $> 1$ is not an independent finding but a corollary of the degeneration identified in Observation~1: under source-attribution scoring, constraint weight is proportional to trace count, so the majority answer necessarily receives more support. A permutation null model, randomizing constraint--answer associations while preserving per-trace counts (1{,}000 permutations), confirms this: $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($\text{BR}_\text{excess} \approx 0$; $p > 0.7$) across all tested conditions. As a zero-cost diagnostic, BR quantifies the degree of extraction degeneration (how completely constraints collapse to majority-vote equivalents), not an independent theoretical contribution. On problems where SC is correct, constraints still track the majority ($\text{BR}_\text{correct}$ $1.29$--$3.64\times$), confirming that self-extracted constraints reflect distributional frequency rather than logical validity.
10	
11	\looseness=-1 The pattern generalizes across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb} 
…[truncated 9954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T05:36:21.558870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T05:36:21.559125+00:00_

1	\section{Escaping the Bottleneck}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Motivation.}
6	\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\S\ref{sec:remediation}). We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, can escape the DPI bound $I(C;Y) \leq I(T;Y)$.
7	
8	\paragraph{Method.}
9	\looseness=-1 We use DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli} for Natural Language Inference (NLI), to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
10	
11	\paragraph{Zero-shot results.}
12	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +1.47$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.
13	
14	\paragraph{Capability gap.}
15	\looseness=-1 Across 108 conditions (three NLI architectures, four generators, three domains), gain decreases monotonically with generator accuracy, a preliminary \emph{capability-gap pattern} ($\rho = 1.0$, $p = 0.003$; exploratory, $n{=}6$ limits statistical confidence; Figure~\ref{fig:capability-gap}). Based on six data points, this pattern requires validation on larger generator pools. All significant gains concentrate below the verifier's standalone accuracy; on ProofWriter ($n{=}600$; Table~\ref{tab:cross_generator_nli}), only Mistral-7B (SC below De
…[truncated 1241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T05:36:21.559443+00:00_

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
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T05:36:21.560142+00:00_

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
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T05:36:21.560511+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
  "old_string": "Our DPI bound $I(C;Y) \\leq I(T;Y)$ further explains why trained verifiers \\citep{lightman2024prm,wang2024mathshepherd} succeed (they break the $M{\\to}T{\\to}A{\\to}C$ chain with external signal) and why same-model scaling saturates at $K_\\text{eff}$.",
  "new_string": "Our DPI bound $I(C;Y) \\leq I(T;Y)$ further explains why trained verifiers \\citep{lightman2024prm,wang2024mathshepherd} succeed (they break the $M{\\to}T{\\to}A{\\to}C$ chain with external signal) and why same-model scaling saturates at $K_\\text{eff}$.\n\n\\looseness=-1\nThe connection to learned verification merits elaboration. Outcome reward models \\citep{cobbe2021gsm8k} and process reward models \\citep{lightman2024prm,wang2024mathshepherd} overcome the DPI bottleneck because training on annotated correctness labels introduces a verification signal conditionally independent of the generator's trace distribution. A trained verifier $V$ satisfies $V \\not\\perp Y \\mid T$ through its training objective, not through the chain $M{\\to}T{\\to}A{\\to}C$; its mutual information $I(V(T); Y)$ can therefore exceed $I(A; Y)$. Discriminator-guided decoding \\citep{khalifa2023grace} achieves a similar effect by training a separate model to score reasoning paths. Our cross-architecture NLI escape (\\S\\ref{sec:cross-arch}) instantiates this principle without task-specific training: DeBERTa's NLI capability, acquired from a structurally independent distribution, provides the requisite independence zero-shot, yielding $+6.67$\\,pp where same-model extraction degrades.\n\n\\looseness=-1\nThese observations suggest a spectrum ordered by strength of external signal. Self-extraction injects none and is bounded by $I(T;Y)$; PRM with dense step-level supervision can approach oracle verification. Our diagnostic framework and NLI escape occupy an intermediate position, requiring no task-specific annotation yet providing corrective signal when a capability gap exists. A natural next step is lightweight trained verification: a small model fine-tuned on modest annotation could combine the accessibility of zero-shot methods with the information-theoretic advantages of learned verifiers, extending the escape region beyond the capability-gap constraint of \\S\\ref{sec:cross-arch}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
    "old_string": "Our DPI bound $I(C;Y) \\leq I(T;Y)$ further explains why trained verifiers \\citep{lightman2024prm,wang2024mathshepherd} succeed (they break the $M{\\to}T{\\to}A{\\to}C$ chain with external signal) and why same-model scaling saturates at $K_\\text{eff}$.",
    "new_string": "Our DPI bound $I(C;Y) \\leq I(T;Y)$ further explains why trained verifiers \\citep{lightman2024prm,wang2024mathshepherd} succeed (they break the $M{\\to}T{\\to}A{\\to}C$ chain with external signal) and why same-model scaling saturates at $K_\\text{eff}$.\n\n\\looseness=-1\nThe connection to learned verification merits elaboration. Outcome reward models \\citep{cobbe2021gsm8k} and process reward models \\citep{lightman2024prm,wang2024mathshepherd} overcome the DPI bottleneck because training on annotated correctness labels introduces a verification signal conditionally independent of the generator's trace distribution. A trained verifier $V$ satisfies $V \\not\\perp Y \\mid T$ through its training objective, not through the chain $M{\\to}T{\\to}A{\\to}C$; its mutual information $I(V(T); Y)$ can therefore exceed $I(A; Y)$. Discriminator-guided decoding \\citep{khalifa2023grace} achieves a similar effect by training a separate model to score reasoning paths. Our cross-architecture NLI escape (\\S\\ref{sec:cross-arch}) instantiates this principle without task-specific training: DeBERTa's NLI capability, acquired from a structurally independent distribution, provides the requisite independence zero-shot, yielding $+6.67$\\,pp where same-model extraction degrades.\n\n\\looseness=-1\nThese observations suggest a spectrum ordered by strength of external signal. Self-extraction injects none and is bounded by $I(T;Y)$; PRM with dense step-level supervision can approach oracle verification. Our diagnostic framework and NLI escape occupy an intermediate position, requiring no task-specific annotation yet providing corrective signal when a capability gap exists. A natural next step is lightweight trained verification: a small model fine-tuned on modest annotation could combine the accessibility of zero-shot methods with the information-theoretic advantages of learned verifiers, extending the escape region beyond the capability-gap constraint of \\S\\ref{sec:cross-arch}."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T05:36:21.560755+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T05:36:21.561122+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|error|Output written\"",
  "description": "Compile LaTeX to check for errors",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|error|Output written\"",
    "description": "Compile LaTeX to check for errors",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T05:36:21.561286+00:00_

Output written on main.pdf (30 pages, 3944672 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-25T05:36:21.561455+00:00_

编译成功，无错误。

最终 discussion.tex 新增两段（~195 words）：
1. **PRM/ORM 机制段**：解释 trained verifier 通过训练目标引入条件独立的验证信号，打破 M→T→A→C chain，使 $I(V(T);Y)$ 突破 $I(A;Y)$ 上界。引用了 `cobbe2021gsm8k`（ORM 开创工作）和 `khalifa2023grace`（discriminator-guided decoding）。将本文 cross-arch NLI escape 定位为同一原理的 zero-shot 实例。
2. **验证策略谱段**：从 self-extraction（无外部信号）到 PRM（密集监督）的连续谱，本文方法居中间。指向 lightweight trained verification 作为未来方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_discussion-prm-orm-paragraph_20260525T053441"
}
```

</details>

---
