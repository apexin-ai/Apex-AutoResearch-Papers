# paper writing abstract reframe

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_writing_abstract_reframe_20260521T015810.jsonl`
- **Structured JSON:** [`a142f80a49959edda0ce.json`](../../sessions/a1/a142f80a49959edda0ce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-21T02:00:36.799101+00:00_

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
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T02:00:36.799773+00:00_

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
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:00:36.799990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T02:00:36.800187+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with selection or aggregation---yields large gains on discrete-answer reasoning and code generation, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where standard aggregation mechanisms break down.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks across fine-tuned 4B\textendash 8B and zero-shot 72B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We identify a diagnostic cascade---instance degeneracy sets the ceiling on improvement, oracle headroom determines the opportunity, and LP compression limits exploitation---that persists under our 72B zero-shot configuration, providing, to our knowledge, the first systematic characterization of when test-time scaling succeeds or fails for NER and similar set-valued extraction tasks.
7	The diagnostic motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD (Holm-adjusted $p{=}0.006$, construction family $k{=}10$) and $+1.02$\,pp on SciERC ($p{=}0.004$, $p_{\text{adj}}{=}0.20$) under fine-tuning. Construction and LP selection are complementary, governed by LP-quality alignment; a degeneracy decomposition confirms that SC gain vanishes when degeneracy exceeds 70\%.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T02:00:36.800478+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "old_string": "\\begin{abstract}\nTest-time compute scaling---repeated sampling with selection or aggregation---yields large gains on discrete-answer reasoning and code generation, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where standard aggregation mechanisms break down.\nWe evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks across fine-tuned 4B\\textendash 8B and zero-shot 72B models.\nAll signals achieve reliable QE ($\\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage).\nFor instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \\textbf{correlation-selection gap}).\nWe identify a diagnostic cascade---instance degeneracy sets the ceiling on improvement, oracle headroom determines the opportunity, and LP compression limits exploitation---that persists under our 72B zero-shot configuration, providing, to our knowledge, the first systematic characterization of when test-time scaling succeeds or fails for NER and similar set-valued extraction tasks.\nThe diagnostic motivates entity-level \\textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\\,pp on Few-NERD (Holm-adjusted $p{=}0.006$, construction family $k{=}10$) and $+1.02$\\,pp on SciERC ($p{=}0.004$, $p_{\\text{adj}}{=}0.20$) under fine-tuning. Construction and LP selection are complementary, governed by LP-quality alignment; a degeneracy decomposition confirms that SC gain vanishes when degeneracy exceeds 70\\%.\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nTest-time compute scaling through repeated sampling yields large gains on discrete-answer reasoning and code generation, yet for structured information extraction (IE), where outputs are entity sets with partial overlap, a persistent gap separates quality estimation from sample selection.\nWe ask whether entity-level agreement signals can bridge this gap.\nAcross seven methods spanning self-judgment, self-refinement, latent consistency, heterogeneous verification, adaptive budgeting, distillation, and supervised classification, we find that no entity-level agreement signal reliably improves selection for named entity recognition (NER), relation extraction (RE), or Text-to-SQL.\nThe failure is systematic: all signals yield null or negative selection gains on four RE benchmarks and SQL parsing (87.2\\% output degeneracy).\nA temperature ablation reveals agreement becomes actively misleading under elevated sampling (conditional $\\rho{=}{-}0.048$ on Few-NERD), and a mechanistic probe identifies a gap between hidden-state frequency agreement (area under the ROC curve [AUROC] 0.87) and prompt-based self-evaluation (AUROC 0.51), an introspection boundary that surface agreement cannot cross.\nThese negative results delineate where self-consistency (SC) does succeed for IE: through paths that bypass entity-level agreement.\nLog-probability selection improves F1 by $+1.39$\\,pp on Few-NERD (Holm-adjusted $p{=}0.019$), entity-level construction via weighted voting gains $+1.02$\\textendash$1.40$\\,pp, and cross-model ensembles add $+0.42$\\,pp.\nEach exploits sequence-level or cross-model signals rather than entity-level self-verification.\nA degeneracy decomposition confirms SC gain vanishes once output degeneracy exceeds 70\\%.\n\\end{abstract}\n%% REFRAME: scope precision + empirical exhaustion methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "old_string": "\\begin{abstract}\nTest-time compute scaling---repeated sampling with selection or aggregation---yields large gains on discrete-answer reasoning and code generation, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where standard aggregation mechanisms break down.\nWe evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks across fine-tuned 4B\\textendash 8B and zero-shot 72B models.\nAll signals achieve reliable QE ($\\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage).\nFor instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \\textbf{correlation-selection gap}).\nWe identify a diagnostic cascade---instance degeneracy sets the ceiling on improvement, oracle headroom determines the opportunity, and LP compression limits exploitation---that persists under our 72B zero-shot configuration, providing, to our knowledge, the first systematic characterization of when test-time scaling succeeds or fails for NER and similar set-valued extraction tasks.\nThe diagnostic motivates entity-level \\textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\\,pp on Few-NERD (Holm-adjusted $p{=}0.006$, construction family $k{=}10$) and $+1.02$\\,pp on SciERC ($p{=}0.004$, $p_{\\text{adj}}{=}0.20$) under fine-tuning. Construction and LP selection are complementary, governed by LP-quality alignment; a degeneracy decomposition confirms that SC gain vanishes when degeneracy exceeds 70\\%.\n\\end{abstract}",
    "new_string": "\\begin{abstract}\nTest-time compute scaling through repeated sampling yields large gains on discrete-answer reasoning and code generation, yet for structured information extraction (IE), where outputs are entity sets with partial overlap, a persistent gap separates quality estimation from sample selection.\nWe ask whether entity-level agreement signals can bridge this gap.\nAcross seven methods spanning self-judgment, self-refinement, latent consistency, heterogeneous verification, adaptive budgeting, distillation, and supervised classification, we find that no entity-level agreement signal reliably improves selection for named entity recognition (NER), relation extraction (RE), or Text-to-SQL.\nThe failure is systematic: all signals yield null or negative selection gains on four RE benchmarks and SQL parsing (87.2\\% output degeneracy).\nA temperature ablation reveals agreement becomes actively misleading under elevated sampling (conditional $\\rho{=}{-}0.048$ on Few-NERD), and a mechanistic probe identifies a gap between hidden-state frequency agreement (area under the ROC curve [AUROC] 0.87) and prompt-based self-evaluation (AUROC 0.51), an introspection boundary that surface agreement cannot cross.\nThese negative results delineate where self-consistency (SC) does succeed for IE: through paths that bypass entity-level agreement.\nLog-probability selection improves F1 by $+1.39$\\,pp on Few-NERD (Holm-adjusted $p{=}0.019$), entity-level construction via weighted voting gains $+1.02$\\textendash$1.40$\\,pp, and cross-model ensembles add $+0.42$\\,pp.\nEach exploits sequence-level or cross-model signals rather than entity-level self-verification.\nA degeneracy decomposition confirms SC gain vanishes once output degeneracy exceeds 70\\%.\n\\end{abstract}\n%% REFRAME: scope precision + empirical exhaustion methodology"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T02:00:36.800684+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:00:36.800846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T02:00:36.801009+00:00_

1	\begin{abstract}
2	Test-time compute scaling through repeated sampling yields large gains on discrete-answer reasoning and code generation, yet for structured information extraction (IE), where outputs are entity sets with partial overlap, a persistent gap separates quality estimation from sample selection.
3	We ask whether entity-level agreement signals can bridge this gap.
4	Across seven methods spanning self-judgment, self-refinement, latent consistency, heterogeneous verification, adaptive budgeting, distillation, and supervised classification, we find that no entity-level agreement signal reliably improves selection for named entity recognition (NER), relation extraction (RE), or Text-to-SQL.
5	The failure is systematic: all signals yield null or negative selection gains on four RE benchmarks and SQL parsing (87.2\% output degeneracy).
6	A temperature ablation reveals agreement becomes actively misleading under elevated sampling (conditional $\rho{=}{-}0.048$ on Few-NERD), and a mechanistic probe identifies a gap between hidden-state frequency agreement (area under the ROC curve [AUROC] 0.87) and prompt-based self-evaluation (AUROC 0.51), an introspection boundary that surface agreement cannot cross.
7	These negative results delineate where self-consistency (SC) does succeed for IE: through paths that bypass entity-level agreement.
8	Log-probability selection improves F1 by $+1.39$\,pp on Few-NERD (Holm-adjusted $p{=}0.019$), entity-level construction via weighted voting gains $+1.02$\textendash$1.40$\,pp, and cross-model ensembles add $+0.42$\,pp.
9	Each exploits sequence-level or cross-model signals rather than entity-level self-verification.
10	A degeneracy decomposition confirms SC gain vanishes once output degeneracy exceeds 70\%.
11	\end{abstract}
12	%% REFRAME: scope precision + empirical exhaustion methodology
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_reframe_20260521T015810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-21T02:00:36.801314+00:00_

Abstract 已重写完成。~215 words，满足 ≤250 限制。

核心变化：
- **Scope 精确化**：从 "SC doesn't work for structured IE" 收窄到 "entity-level agreement signals cannot bridge the QE-selection gap"
- **4 项核心证据全部覆盖**：7 methods exhaustive (line 4), T-ablation ρ=-0.048 (line 6), cross-task RE+SQL 87.2% degeneracy (line 5), mechanistic probe AUROC 0.87 vs 0.51 (line 6)
- **Escape routes 作为正面证据**：LP selection +1.39pp, construction +1.02–1.40pp, cross-model +0.42pp (line 8)，每条都绕过了 entity-level agreement
- **无破折号**，无 AI 写作标志词，所有缩写首次出现均已定义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_reframe_20260521T015810"
}
```

</details>

---
