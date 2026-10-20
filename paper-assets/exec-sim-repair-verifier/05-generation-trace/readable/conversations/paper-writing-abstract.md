# paper writing abstract

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_writing_abstract_20260515T095317.jsonl`
- **Structured JSON:** [`4d42df2b51c0b897e462.json`](../../sessions/4d/4d42df2b51c0b897e462.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T09:54:52.329503+00:00_

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
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T09:54:52.330473+00:00_

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
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T09:54:52.330703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T09:54:52.330919+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair faces a granularity--accuracy tradeoff: generation-based approaches (Code World Models) predict execution output strings but suffer from token-budget exhaustion and string-value prediction errors as code complexity grows, while trajectory-level verifiers provide binary patch verdicts but discard per-test diagnostic information.
3	%
4	We reformulate execution simulation from open-ended output generation to per-test binary pass/fail classification, and systematically compare classification (\cls{}), generation (\cwm{}), and trajectory-level formulations at controlled model sizes.
5	%
6	On function-level benchmarks, \cls{} and \cwm{} achieve near-equivalent accuracy (88.43\% vs.\ 87.19\%, 5 seeds, gap 1.24\pp{}); at 8B parameters the gap widens (raw 2.43\pp{}; bootstrap mean 2.26\pp{}, $p{=}0.0066$), with \cwm{} failing to benefit from increased capacity. Per-test \cls{} matches trajectory-level accuracy (TOST equivalence $p{=}0.007$, $\pm$2\pp{} margin) while providing free diagnostic granularity---which specific tests fail. Oracle analysis on SWE-bench Verified shows this per-test advantage concentrates in instances with two or more failing tests (31\% of instances, contributing 55\% of total advantage), and an oracle ensemble of \cls{} and \cwm{} reaches 90.63\% accuracy. At repository level, the gap amplifies substantially (76.92\% vs.\ 66.60\%, single seed): \cwm{} falls below majority baseline due to 75\% unparseable outputs from format non-compliance despite sufficient token budget, while \cls{} remains robust (1.3\% unparseable).
7	%
8	These results support classification as a promising alternative to generation-based execution simulation, with an advantage that grows with code complexity---from modest at function level to critical at repository level.
9	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T09:54:52.331242+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
  "content": "\\begin{abstract}\nExecution-free verification for LLM-based code repair faces a granularity--accuracy tradeoff: generation-based approaches (Code World Models) predict execution output strings but suffer from token-budget exhaustion, string-value prediction errors, and format compliance collapse as code complexity grows, while trajectory-level verifiers provide binary patch verdicts but discard per-test diagnostic information.\n%\nWe reformulate execution simulation from open-ended output generation to per-test binary pass/fail classification, and systematically compare classification (\\cls{}), generation (\\cwm{}), and trajectory-level formulations at controlled model sizes.\n%\nOn function-level benchmarks, \\cls{} and \\cwm{} achieve near-equivalent accuracy at 4B parameters (88.43\\% vs.\\ 87.19\\%, 5 seeds, gap 1.24\\pp{}). At 8B the gap widens to 2.43\\pp{} (bootstrap mean 2.26\\pp{}, $p{=}0.0066$, 3 seeds), with \\cwm{} failing to benefit from scaling (\\cls{} +0.96\\pp{} vs.\\ \\cwm{} $-$0.27\\pp{}, 4B$\\to$8B). Per-test \\cls{} matches trajectory-level accuracy (TOST equivalence $p{=}0.007$, $\\pm$2\\pp{} margin) while providing free diagnostic granularity---which specific tests fail. Oracle analysis on SWE-bench Verified shows this advantage concentrates in instances with $\\geq$2 failing tests (31\\% of instances, 55\\% of total advantage); an oracle ensemble reaches 90.63\\%. At repository level, the gap amplifies to 25.59\\pp{} (83.63\\% vs.\\ 58.04\\%, 4B, single seed), with \\cwm{} falling ${\\sim}$14\\pp{} below majority baseline (72.96\\%). Format non-compliance produces 53.7--67.2\\% unparseable \\cwm{} outputs, and even parseable outputs score only 42--43\\%---below random chance---while \\cls{} remains robust with 0\\% unparseable.\n%\nThese results support classification as a promising alternative to generation-based execution simulation, with an advantage that grows with code complexity---from modest at function level to critical at repository level.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
    "content": "\\begin{abstract}\nExecution-free verification for LLM-based code repair faces a granularity--accuracy tradeoff: generation-based approaches (Code World Models) predict execution output strings but suffer from token-budget exhaustion, string-value prediction errors, and format compliance collapse as code complexity grows, while trajectory-level verifiers provide binary patch verdicts but discard per-test diagnostic information.\n%\nWe reformulate execution simulation from open-ended output generation to per-test binary pass/fail classification, and systematically compare classification (\\cls{}), generation (\\cwm{}), and trajectory-level formulations at controlled model sizes.\n%\nOn function-level benchmarks, \\cls{} and \\cwm{} achieve near-equivalent accuracy at 4B parameters (88.43\\% vs.\\ 87.19\\%, 5 seeds, gap 1.24\\pp{}). At 8B the gap widens to 2.43\\pp{} (bootstrap mean 2.26\\pp{}, $p{=}0.0066$, 3 seeds), with \\cwm{} failing to benefit from scaling (\\cls{} +0.96\\pp{} vs.\\ \\cwm{} $-$0.27\\pp{}, 4B$\\to$8B). Per-test \\cls{} matches trajectory-level accuracy (TOST equivalence $p{=}0.007$, $\\pm$2\\pp{} margin) while providing free diagnostic granularity---which specific tests fail. Oracle analysis on SWE-bench Verified shows this advantage concentrates in instances with $\\geq$2 failing tests (31\\% of instances, 55\\% of total advantage); an oracle ensemble reaches 90.63\\%. At repository level, the gap amplifies to 25.59\\pp{} (83.63\\% vs.\\ 58.04\\%, 4B, single seed), with \\cwm{} falling ${\\sim}$14\\pp{} below majority baseline (72.96\\%). Format non-compliance produces 53.7--67.2\\% unparseable \\cwm{} outputs, and even parseable outputs score only 42--43\\%---below random chance---while \\cls{} remains robust with 0\\% unparseable.\n%\nThese results support classification as a promising alternative to generation-based execution simulation, with an advantage that grows with code complexity---from modest at function level to critical at repository level.\n\\end{abstract}\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T09:54:52.331455+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T09:54:52.331599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T09:54:52.331740+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair faces a granularity--accuracy tradeoff: generation-based approaches (Code World Models) predict execution output strings but suffer from token-budget exhaustion, string-value prediction errors, and format compliance collapse as code complexity grows, while trajectory-level verifiers provide binary patch verdicts but discard per-test diagnostic information.
3	%
4	We reformulate execution simulation from open-ended output generation to per-test binary pass/fail classification, and systematically compare classification (\cls{}), generation (\cwm{}), and trajectory-level formulations at controlled model sizes.
5	%
6	On function-level benchmarks, \cls{} and \cwm{} achieve near-equivalent accuracy at 4B parameters (88.43\% vs.\ 87.19\%, 5 seeds, gap 1.24\pp{}). At 8B the gap widens to 2.43\pp{} (bootstrap mean 2.26\pp{}, $p{=}0.0066$, 3 seeds), with \cwm{} failing to benefit from scaling (\cls{} +0.96\pp{} vs.\ \cwm{} $-$0.27\pp{}, 4B$\to$8B). Per-test \cls{} matches trajectory-level accuracy (TOST equivalence $p{=}0.007$, $\pm$2\pp{} margin) while providing free diagnostic granularity---which specific tests fail. Oracle analysis on SWE-bench Verified shows this advantage concentrates in instances with $\geq$2 failing tests (31\% of instances, 55\% of total advantage); an oracle ensemble reaches 90.63\%. At repository level, the gap amplifies to 25.59\pp{} (83.63\% vs.\ 58.04\%, 4B, single seed), with \cwm{} falling ${\sim}$14\pp{} below majority baseline (72.96\%). Format non-compliance produces 53.7--67.2\% unparseable \cwm{} outputs, and even parseable outputs score only 42--43\%---below random chance---while \cls{} remains robust with 0\% unparseable.
7	%
8	These results support classification as a promising alternative to generation-based execution simulation, with an advantage that grows with code complexity---from modest at function level to critical at repository level.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260515T095317",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T09:54:52.332000+00:00_

已写入。主要变更：

- **三个 failure modes**：加入 format compliance collapse
- **Repo-level 数字全部更新**：25.59pp gap (83.63% vs 58.04%, 4B, single seed)，~14pp below majority baseline (72.96%)，unparseable 53.7–67.2%，parseable-only 42–43%，CLS 0% unparseable
- **Scaling evidence 加入**：CLS +0.96pp vs CWM −0.27pp (4B→8B)
- **Cross-size 省略**，节省 word budget
- C2/C3 数字不变，function-level 数字不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_20260515T095317"
}
```

</details>

---
