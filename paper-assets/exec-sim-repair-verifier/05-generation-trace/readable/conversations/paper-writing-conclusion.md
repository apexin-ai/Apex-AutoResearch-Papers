# paper writing conclusion

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_writing_conclusion_20260515T100823.jsonl`
- **Structured JSON:** [`1e1d010717bacabd8505.json`](../../sessions/1e/1e1d010717bacabd8505.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T10:09:23.988411+00:00_

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
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T10:09:23.989347+00:00_

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
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T10:09:23.989839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T10:09:23.990036+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification, and characterized when this reformulation provides an advantage. At function level, \cls{} and \cwm{} are near-equivalent (gap 1.24\pp{}, 5 seeds), confirming that generation is adequate when outputs are short and structurally simple. At 8B, the gap widens (raw 2.43\pp{}; bootstrap mean 2.26\pp{}, $p = 0.0066$, 3 matched seeds): \cls{} gains +0.99\pp{} while \cwm{} loses $-$0.27\pp{}, indicating that additional capacity benefits classification but not generation---consistent with the string-prediction bottleneck hypothesis. Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST $p = 0.007$, $\pm$2\pp{} margin) while providing diagnostic per-test signals at no accuracy cost. Oracle analysis on SWE-bench Verified reveals that the per-test advantage concentrates in instances with $T \geq 2$ F2P tests (31\% of instances, contributing 55\% of total advantage), establishing a practical decision boundary: per-test verification adds value only when multiple F2P tests are present.
5	
6	At repo level on SWE-bench Verified, the gap amplifies substantially to 10.32\pp{} (single seed): \cwm{} falls below majority baseline (66.60\% vs.\ 72.96\%) due to 75\% unparseable outputs from format non-compliance despite sufficient token budget, while \cls{} achieves 76.92\% with only 1.3\% unparseable. This provides empirical evidence that the generation formulation faces substantial challenges at repository scale.
7	
8	\paragraph{Limitations.}
9	The function-level near-equivalence (1.24\pp{}) limits practical \cls{} advantage at that scale. Repo-level results are currently from a single seed; multi-seed replication is in progress. All experiments use a single model family (Qwen3); scaling behavior may differ across architectures. The oracle ana
…[truncated 661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T10:09:23.990265+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification, and characterized when this reformulation provides an advantage. At function level, \\cls{} and \\cwm{} are near-equivalent (gap 1.24\\pp{}, 5 seeds), confirming that generation is adequate when outputs are short and structurally simple. At 8B, the gap widens (raw 2.43\\pp{}; bootstrap mean 2.26\\pp{}, $p = 0.0066$, 3 matched seeds): \\cls{} gains +0.96\\pp{} while \\cwm{} loses $-$0.27\\pp{}, indicating that additional capacity benefits classification but not generation---consistent with the generation bottleneck hypothesis. Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST $p = 0.007$, $\\pm$2\\pp{} margin) while providing diagnostic per-test signals at no accuracy cost. Oracle analysis on SWE-bench Verified reveals that the per-test advantage concentrates in instances with $T \\geq 2$ F2P tests (31\\% of instances, contributing 55\\% of total advantage), establishing a practical decision boundary: per-test verification adds value only when multiple F2P tests are present.\n\nAt repo level on SWE-bench Verified, the gap amplifies to 25.59\\pp{} in same-size 4B--4B comparison (single seed): \\cwm{} falls to 58.04\\%, roughly 14\\pp{} below the majority baseline (72.96\\%), while \\cls{} reaches 83.63\\% with 0\\% unparseable outputs. \\cwm{} exhibits format compliance collapse---53.7--67.2\\% of outputs are unparseable across seeds despite sufficient token budget---and even among parseable outputs, accuracy is 42--43\\%, below random chance. The generation formulation thus suffers a compounding failure at repository scale: format non-compliance discards the majority of predictions, and the surviving predictions are themselves unreliable.\n\n\\paragraph{Limitations.}\nThe function-level near-equivalence (1.24\\pp{}) limits practical \\cls{} advantage at that scale. Repo-level same-size comparison (4B--4B) rests on a single seed; 8B--8B awaits \\cwm{} 8B training completion. All experiments use a single model family (Qwen3); scaling behavior may differ across architectures. Val/test distribution shift---zero problem overlap and mutation type composition shift---may affect generalization estimates. The oracle analysis assumes ground-truth test labels; real-world advantage is upper-bounded by classifier accuracy. No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements. P2P regression rates (${\\sim}$1\\% mean) are too low for per-test P2P signals to be useful---diagnostic advantage is limited to the F2P dimension.\n\n\\paragraph{Future work.}\n\\cls{}--\\cwm{} error complementarity motivates ensemble verification routing by predicted output complexity. Per-test failure signals enable diagnostic re-repair: localizing faults from per-test verdicts rather than discarding failed patches. Multi-model validation and integration with test-time scaling systems (best-of-$N$ with per-test reranking) are natural next steps.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification, and characterized when this reformulation provides an advantage. At function level, \\cls{} and \\cwm{} are near-equivalent (gap 1.24\\pp{}, 5 seeds), confirming that generation is adequate when outputs are short and structurally simple. At 8B, the gap widens (raw 2.43\\pp{}; bootstrap mean 2.26\\pp{}, $p = 0.0066$, 3 matched seeds): \\cls{} gains +0.96\\pp{} while \\cwm{} loses $-$0.27\\pp{}, indicating that additional capacity benefits classification but not generation---consistent with the generation bottleneck hypothesis. Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST $p = 0.007$, $\\pm$2\\pp{} margin) while providing diagnostic per-test signals at no accuracy cost. Oracle analysis on SWE-bench Verified reveals that the per-test advantage concentrates in instances with $T \\geq 2$ F2P tests (31\\% of instances, contributing 55\\% of total advantage), establishing a practical decision boundary: per-test verification adds value only when multiple F2P tests are present.\n\nAt repo level on SWE-bench Verified, the gap amplifies to 25.59\\pp{} in same-size 4B--4B comparison (single seed): \\cwm{} falls to 58.04\\%, roughly 14\\pp{} below the majority baseline (72.96\\%), while \\cls{} reaches 83.63\\% with 0\\% unparseable outputs. \\cwm{} exhibits format compliance collapse---53.7--67.2\\% of outputs are unparseable across seeds despite sufficient token budget---and even among parseable outputs, accuracy is 42--43\\%, below random chance. The generation formulation thus suffers a compounding failure at repository scale: format non-compliance discards the majority of predictions, and the surviving predictions are themselves unreliable.\n\n\\paragraph{Limitations.}\nThe function-level near-equivalence (1.24\\pp{}) limits practical \\cls{} advantage at that scale. Repo-level same-size comparison (4B--4B) rests on a single seed; 8B--8B awaits \\cwm{} 8B training completion. All experiments use a single model family (Qwen3); scaling behavior may differ across architectures. Val/test distribution shift---zero problem overlap and mutation type composition shift---may affect generalization estimates. The oracle analysis assumes ground-truth test labels; real-world advantage is upper-bounded by classifier accuracy. No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements. P2P regression rates (${\\sim}$1\\% mean) are too low for per-test P2P signals to be useful---diagnostic advantage is limited to the F2P dimension.\n\n\\paragraph{Future work.}\n\\cls{}--\\cwm{} error complementarity motivates ensemble verification routing by predicted output complexity. Per-test failure signals enable diagnostic re-repair: localizing faults from per-test verdicts rather than discarding failed patches. Multi-model validation and integration with test-time scaling systems (best-of-$N$ with per-test reranking) are natural next steps.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T10:09:23.990667+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T10:09:23.990977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T10:09:23.991218+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification, and characterized when this reformulation provides an advantage. At function level, \cls{} and \cwm{} are near-equivalent (gap 1.24\pp{}, 5 seeds), confirming that generation is adequate when outputs are short and structurally simple. At 8B, the gap widens (raw 2.43\pp{}; bootstrap mean 2.26\pp{}, $p = 0.0066$, 3 matched seeds): \cls{} gains +0.96\pp{} while \cwm{} loses $-$0.27\pp{}, indicating that additional capacity benefits classification but not generation---consistent with the generation bottleneck hypothesis. Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST $p = 0.007$, $\pm$2\pp{} margin) while providing diagnostic per-test signals at no accuracy cost. Oracle analysis on SWE-bench Verified reveals that the per-test advantage concentrates in instances with $T \geq 2$ F2P tests (31\% of instances, contributing 55\% of total advantage), establishing a practical decision boundary: per-test verification adds value only when multiple F2P tests are present.
5	
6	At repo level on SWE-bench Verified, the gap amplifies to 25.59\pp{} in same-size 4B--4B comparison (single seed): \cwm{} falls to 58.04\%, roughly 14\pp{} below the majority baseline (72.96\%), while \cls{} reaches 83.63\% with 0\% unparseable outputs. \cwm{} exhibits format compliance collapse---53.7--67.2\% of outputs are unparseable across seeds despite sufficient token budget---and even among parseable outputs, accuracy is 42--43\%, below random chance. The generation formulation thus suffers a compounding failure at repository scale: format non-compliance discards the majority of predictions, and the surviving predictions are themselves unreliable.
7	
8	\paragraph{Limitations.}
9	The function-level near-equivalence (1.24\pp{}) limits practical \cls{} 
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260515T100823",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T10:09:23.991441+00:00_

已写入。变更汇总：

**第一段**：+0.99→+0.96pp，"string-prediction bottleneck"→"generation bottleneck"

**第二段**（全面重写）：gap 25.59pp，CWM 58.04%（低于 majority ~14pp），CLS 83.63%/0% unparseable，引入 "format compliance collapse" 命名，新增 parseable-only 42–43% below random chance，compounding failure 论述

**Limitations**：single seed 限定改为 4B-4B 具体说明 + 8B-8B 待训练；新增 val/test distribution shift；新增 no downstream re-repair experiment

**Future work**：未改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_conclusion_20260515T100823"
}
```

</details>

---
