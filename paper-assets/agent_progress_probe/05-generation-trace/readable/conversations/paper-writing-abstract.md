# paper writing abstract

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_paper_writing_abstract_20260514T224905.jsonl`
- **Structured JSON:** [`4f18f16242f3c9afc556.json`](../../sessions/4f/4f18f16242f3c9afc556.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-14T22:50:51.901142+00:00_

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
  "session": "worker_paper_writing_abstract_20260514T224905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T22:50:51.901734+00:00_

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
  "session": "worker_paper_writing_abstract_20260514T224905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T22:50:51.901942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260514T224905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T22:50:51.902103+00:00_

1	% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)
2	\begin{abstract}
3	LLM agents deployed on long-horizon software engineering tasks frequently \emph{stagnate}---producing diverse yet collectively unproductive action sequences that evade simple loop detectors.
4	Detecting this failure mode is critical for enabling timely interventions, yet it remains unclear what information is needed: does identifying subtle agent stagnation require semantic understanding, or do simpler structural patterns suffice?
5	We present a systematic empirical study addressing this question through weak supervision over trajectories of two architecturally distinct agents, SWE-Agent (54,809 windows, 28.5\% stagnation) and OpenHands (150,652 windows, 6.6\% stagnation).
6	Our central finding is that stagnation signals are fundamentally structural: 30 hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 in-domain and 0.967 cross-agent macro-F1, surpassing a GRU embedding probe (0.906 in-domain, 0.751 with full fine-tuning) by up to 21.6 percentage points and an LLM-as-judge baseline (0.663) by 33.3 pp, while requiring no GPU and running in under 5\,ms per window.
7	This structural advantage is encoder-agnostic: three embedding backbones all yield probe F1 above 0.90.
8	We further characterize labeling function temporal dynamics, revealing agent-specific roles: command repetition leads stagnation by 1.87 steps on SWE-Agent but reverses to lagging on OpenHands, where removing it improves probe F1 by 17.6\,pp.
9	Despite these well-characterized temporal patterns, three temporal label models---time-varying weights, HMM, and lag-aware HMM---all fail to improve over majority vote, a negative result we trace to low inter-LF conflict in the current 3-function regime.
10	Our findings redirect agent monitoring from costly representation learning toward lightweight structural approaches.
11	\end{abstract}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260514T224905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T22:50:51.902354+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex",
  "content": "% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\nLLM-based agents deployed on software engineering tasks frequently exhibit semantic stagnation---executing diverse yet collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges. No systematic study has investigated what signals carry stagnation information or whether detection requires semantic understanding.\n\nWe address this gap through a systematic empirical study using a weak supervision pipeline (3 labeling functions + majority vote) over 205K+ windows from two architecturally distinct SE agents, SWE-Agent and OpenHands. We compare 30 hand-crafted structural features, a GRU-based neural embedding probe, and an LLM-as-judge baseline.\n\nOur central finding is that stagnation signals are fundamentally structural: 30 features---command repetition rates, file operation counts, edit distances---achieve RF 0.9951 in-domain and GB 0.9674 cross-agent macro-F1, surpassing the neural probe (0.9055) and LLM-as-judge (0.6625) by wide margins. In-domain evaluation reflects circular agreement with LF-derived silver labels; cross-agent transfer and a pending gold set provide non-circular validation. Structural features are also extremely data-efficient, achieving $>$0.987 macro-F1 at just 10\\% training data.\n\nAnalysis of labeling function temporal dynamics reveals agent-specific roles: command repetition leads stagnation by 1.87 steps on SWE-Agent but reverses on OpenHands, where removing it improves fine-tuned F1 by 17.6 percentage points. Labeling functions validated on one agent can become adversarial on another.\n\nDespite these well-characterized temporal patterns, three temporal label models (time-varying weights, HMM, lag-aware HMM) fail to improve over majority vote---a negative result we attribute to insufficient inter-LF conflict in the 3-function regime.\n\n\\goldset{Gold set validation (650 windows) pending.}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260514T224905",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex",
    "content": "% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\nLLM-based agents deployed on software engineering tasks frequently exhibit semantic stagnation---executing diverse yet collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges. No systematic study has investigated what signals carry stagnation information or whether detection requires semantic understanding.\n\nWe address this gap through a systematic empirical study using a weak supervision pipeline (3 labeling functions + majority vote) over 205K+ windows from two architecturally distinct SE agents, SWE-Agent and OpenHands. We compare 30 hand-crafted structural features, a GRU-based neural embedding probe, and an LLM-as-judge baseline.\n\nOur central finding is that stagnation signals are fundamentally structural: 30 features---command repetition rates, file operation counts, edit distances---achieve RF 0.9951 in-domain and GB 0.9674 cross-agent macro-F1, surpassing the neural probe (0.9055) and LLM-as-judge (0.6625) by wide margins. In-domain evaluation reflects circular agreement with LF-derived silver labels; cross-agent transfer and a pending gold set provide non-circular validation. Structural features are also extremely data-efficient, achieving $>$0.987 macro-F1 at just 10\\% training data.\n\nAnalysis of labeling function temporal dynamics reveals agent-specific roles: command repetition leads stagnation by 1.87 steps on SWE-Agent but reverses on OpenHands, where removing it improves fine-tuned F1 by 17.6 percentage points. Labeling functions validated on one agent can become adversarial on another.\n\nDespite these well-characterized temporal patterns, three temporal label models (time-varying weights, HMM, lag-aware HMM) fail to improve over majority vote---a negative result we attribute to insufficient inter-LF conflict in the 3-function regime.\n\n\\goldset{Gold set validation (650 windows) pending.}\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T22:50:51.902533+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260514T224905",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-14T22:50:51.902734+00:00_

Word count verification:

| Section | Target | Actual |
|---------|--------|--------|
| Problem | ~40 | 42 |
| Approach | ~50 | 46 |
| Finding 1 (Structural) | ~60 | 73 |
| Finding 2 (LF Dynamics) | ~50 | 43 |
| Finding 3 (TLM Negative) | ~30 | 33 |
| **Total** | **≤250** | **237** |

Constraints met:
- No "significantly", "state-of-the-art", "consistently outperforms"
- Circular evaluation caveat present ("In-domain evaluation reflects circular agreement with LF-derived silver labels")
- All numbers exact match (0.9951, 0.9674, 0.9055, 0.6625, 205K+, 1.87, 17.6pp, >0.987, 10%)
- No `\begin{abstract}` / `\end{abstract}`
- `\goldset` placeholder at end
- 237 words, under 250 limit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_20260514T224905"
}
```

</details>

---
