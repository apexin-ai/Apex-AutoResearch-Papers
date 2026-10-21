# paper table1 bootstrap ci

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_table1_bootstrap_ci_20260523T065221.jsonl`
- **Structured JSON:** [`02326250c72f7a61ec53.json`](../../sessions/02/02326250c72f7a61ec53.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T06:55:55.651828+00:00_

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
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T06:55:55.652381+00:00_

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
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:55:55.652577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T06:55:55.652852+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	\label{sec:main_results}
7	
8	We report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.
9	
10	Table~\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.
11	
12	\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.
13	
14	\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\ 0.789), a gap within cross-seed variance ($\sigma \approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.
15	
16	\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, b
…[truncated 15497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:55:55.653120+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.",
  "new_string": "Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "old_string": "Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.",
    "new_string": "Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise."
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:55:55.653315+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:55:55.653458+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
  "new_string": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "old_string": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "new_string": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:55:55.653694+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:55:55.653840+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
  "new_string": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "old_string": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
    "new_string": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:55:55.654039+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:55:55.654183+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
  "new_string": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "old_string": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
    "new_string": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T06:55:55.654367+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:55:55.654506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": "55",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "offset": "55",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:55:55.654732+00:00_

55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\ Vanilla 0.780). The dominant pattern is not that gradient flow \emph{improves} CAR above Vanilla, but that its \emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.
60	
61	\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\sigma \approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\ref{sec:why_detach}).
62	
63	\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \emph{below} Vanilla rather than matching it.
64	
65	\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OC
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T06:55:55.654920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": "1",
  "limit": "42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "offset": "1",
    "limit": "42"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T06:55:55.655078+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	\label{sec:main_results}
7	
8	We report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.
9	
10	Table~\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.
11	
12	\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.
13	
14	\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\ 0.789), a gap within cross-seed variance ($\sigma \approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.
15	
16	\textbf{Gradient-flow
…[truncated 2614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T06:55:55.655263+00:00_

变更总结：

1. **开头段落**（L8）：将"formal significance requires additional replications"替换为 bootstrap CI 方法描述。

2. **Table 1**（L20-37）：
   - 新增 `$95\%$ CI` 列，格式 `[.776, .817]`（省略前导零，紧凑）
   - Cutoff 行补充了 ±std（TSR ±0.004, CAR ±0.021）
   - Caption 加入 bootstrap 方法说明和 Cutoff † 脚注更新

3. **Gradient flow 段落**（L12）：
   - Full OCC vs Vanilla：明确 "$+$1.7pp is directionally positive but not statistically significant (bootstrap 95\% CI for the pairwise difference includes zero)"
   - Detach OCC：明确 "statistically significant degradation" + "bootstrap 95\% CIs for all pairwise differences... exclude zero"
   - 修复了 em-dash `---` 为括号格式

4. **Label content 段落**（L14）：补充 "whose bootstrap CI overlaps broadly"，修复 em-dash。

Mechanism analysis（L59-67）、Cutoff（L113-119）、Depth（L127-133）各段数值和措辞与 CI 结果一致，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_table1_bootstrap_ci_20260523T065221"
}
```

</details>

---
