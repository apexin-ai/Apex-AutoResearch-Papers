# write s53 baseline narrative

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_write_s53-baseline-narrative_20260522T211425.jsonl`
- **Structured JSON:** [`8182bdeb478a0a01aaa0.json`](../../sessions/81/8182bdeb478a0a01aaa0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-22T21:15:52.089895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T21:15:52.090424+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency chec
…[truncated 22462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T21:15:52.090647+00:00_

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
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T21:15:52.091111+00:00_

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
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T21:15:52.091386+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "0-shot & 8B (Qwen3) & 1 & 68.70 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\\\",
  "new_string": "0-shot & 8B (Qwen3) & 1 & 68.70 \\\\\n0-shot & 14B (Qwen3) & 1 & 66.24 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "0-shot & 8B (Qwen3) & 1 & 68.70 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\\\",
    "new_string": "0-shot & 8B (Qwen3) & 1 & 68.70 \\\\\n0-shot & 14B (Qwen3) & 1 & 66.24 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T21:15:52.091642+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T21:15:52.091787+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\",
  "new_string": "3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\\\\n3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\",
    "new_string": "3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\\\\n3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T21:15:52.092056+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T21:15:52.092227+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "At 14B, \\cls{} reaches \\placeholder{14B-CLS-ACC}\\% (\\placeholder{14B-CLS-DELTA}\\pp{} from 8B), \\cwm{} reaches \\placeholder{14B-CWM-ACC}\\% (\\placeholder{14B-CWM-DELTA}\\pp{}), and \\traj{} reaches \\placeholder{14B-TRAJ-ACC}\\% (\\placeholder{14B-TRAJ-DELTA}\\pp{}). The \\cls{}--\\cwm{} gap \\placeholder{14B-GAP-TREND} from 2.62\\pp{} at 8B to \\placeholder{14B-CLS-CWM-GAP}\\pp{} at 14B. \\placeholder{14B-SCALING-TAKEAWAY}\n\n\\cwm{} flat scaling",
  "new_string": "At 14B, \\cls{} reaches \\placeholder{14B-CLS-ACC}\\% (\\placeholder{14B-CLS-DELTA}\\pp{} from 8B), \\cwm{} reaches \\placeholder{14B-CWM-ACC}\\% (\\placeholder{14B-CWM-DELTA}\\pp{}), and \\traj{} reaches \\placeholder{14B-TRAJ-ACC}\\% (\\placeholder{14B-TRAJ-DELTA}\\pp{}). The \\cls{}--\\cwm{} gap \\placeholder{14B-GAP-TREND} from 2.62\\pp{} at 8B to \\placeholder{14B-CLS-CWM-GAP}\\pp{} at 14B. \\placeholder{14B-SCALING-TAKEAWAY}\n\n\\paragraph{Baseline scaling.} Prompting baselines exhibit a mixed pattern at 14B. In the 3-shot setting, Qwen3-14B (73.12\\%) outperforms Qwen3-8B (68.78\\%) by 4.34\\pp{}, consistent with the expected benefit of increased capacity for in-context learning. In contrast, 14B 0-shot accuracy (66.24\\%) falls 2.46\\pp{} below 8B (68.70\\%); this reversal may reflect differences in instruction tuning between the two model sizes rather than a capacity limitation, and we do not draw strong conclusions from it. Regardless of prompting strategy, the best prompting result (14B 3-shot, 73.12\\%) remains 16.82\\pp{} below fine-tuned \\cls{} at 8B (89.94\\%, Table~\\ref{tab:main_results}), confirming that model scaling alone does not substitute for task-specific fine-tuning at function level.\n\n\\cwm{} flat scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "At 14B, \\cls{} reaches \\placeholder{14B-CLS-ACC}\\% (\\placeholder{14B-CLS-DELTA}\\pp{} from 8B), \\cwm{} reaches \\placeholder{14B-CWM-ACC}\\% (\\placeholder{14B-CWM-DELTA}\\pp{}), and \\traj{} reaches \\placeholder{14B-TRAJ-ACC}\\% (\\placeholder{14B-TRAJ-DELTA}\\pp{}). The \\cls{}--\\cwm{} gap \\placeholder{14B-GAP-TREND} from 2.62\\pp{} at 8B to \\placeholder{14B-CLS-CWM-GAP}\\pp{} at 14B. \\placeholder{14B-SCALING-TAKEAWAY}\n\n\\cwm{} flat scaling",
    "new_string": "At 14B, \\cls{} reaches \\placeholder{14B-CLS-ACC}\\% (\\placeholder{14B-CLS-DELTA}\\pp{} from 8B), \\cwm{} reaches \\placeholder{14B-CWM-ACC}\\% (\\placeholder{14B-CWM-DELTA}\\pp{}), and \\traj{} reaches \\placeholder{14B-TRAJ-ACC}\\% (\\placeholder{14B-TRAJ-DELTA}\\pp{}). The \\cls{}--\\cwm{} gap \\placeholder{14B-GAP-TREND} from 2.62\\pp{} at 8B to \\placeholder{14B-CLS-CWM-GAP}\\pp{} at 14B. \\placeholder{14B-SCALING-TAKEAWAY}\n\n\\paragraph{Baseline scaling.} Prompting baselines exhibit a mixed pattern at 14B. In the 3-shot setting, Qwen3-14B (73.12\\%) outperforms Qwen3-8B (68.78\\%) by 4.34\\pp{}, consistent with the expected benefit of increased capacity for in-context learning. In contrast, 14B 0-shot accuracy (66.24\\%) falls 2.46\\pp{} below 8B (68.70\\%); this reversal may reflect differences in instruction tuning between the two model sizes rather than a capacity limitation, and we do not draw strong conclusions from it. Regardless of prompting strategy, the best prompting result (14B 3-shot, 73.12\\%) remains 16.82\\pp{} below fine-tuned \\cls{} at 8B (89.94\\%, Table~\\ref{tab:main_results}), confirming that model scaling alone does not substitute for task-specific fine-tuning at function level.\n\n\\cwm{} flat scaling"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T21:15:52.092480+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T21:15:52.092634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "offset": "44",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "offset": "44",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T21:15:52.092785+00:00_

44	\traj{} (fine-tuned) & 6.7B & 2 & 84.16 $\pm$ 1.30 \\
45	\midrule
46	\multicolumn{4}{l}{\emph{Prompting baselines}} \\
47	0-shot & 8B (Qwen3) & 1 & 68.70 \\
48	0-shot & 14B (Qwen3) & 1 & 66.24 \\
49	0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\
50	ZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\
51	ZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\
52	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
53	3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\
54	3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\
55	3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\
56	\midrule
57	Majority (pass) & --- & --- & 51.75 \\
58	\bottomrule
59	\end{tabular}}
60	\end{table}
61	
62	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). DeepSeek-Coder-6.7B shows: \cls{} 86.85\%, \cwm{} 86.83\%, \traj{} 84.16\%. The \cls{}--\cwm{} gap (0.02--1.24\pp{}) is within seed noise in both families. However, the \cls{}--\traj{} gap is model-dependent: $<$1\pp{} on Qwen3 but 2.69\pp{} on DeepSeek-Coder, exceeding the $\pm$2\pp{} equivalence margin (\S\ref{sec:equivalence}). \cls{} and \cwm{} are robustly equivalent; \traj{} parity is model-contingent. Zero-shot baselines (Tables~\ref{tab:main_results} and~\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\to$fine-tuned gains of 35--36\pp{}) and that formulation choice matters only at repo level (\cls{} outperforms \cwm{} by 18--26\pp{}).
63	
64	
65	\subsection{Scaling Behavior}
66	\label{sec:scaling}
67	
68	Beyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T21:15:52.092960+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "offset": "100",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "offset": "100",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T21:15:52.093136+00:00_

100	%   - CLS continues scaling → three-point consistency; classification robust across sizes
101	%   - CWM remains flat → generation stagnation persists at 14B
102	%   - CWM recovers → reframe as delayed scaling onset for generation
103	%   - CLS-CWM gap widens → divergent trajectories; strengthen practical recommendation
104	%   - CLS-CWM gap narrows → scaling partially compensates for formulation choice
105	%   - TRAJ overtakes CWM → trajectory scoring as efficient middle ground
106	%   - Update Figure~\ref{fig:scaling_gap} with 14B data point
107	At 14B, \cls{} reaches \placeholder{14B-CLS-ACC}\% (\placeholder{14B-CLS-DELTA}\pp{} from 8B), \cwm{} reaches \placeholder{14B-CWM-ACC}\% (\placeholder{14B-CWM-DELTA}\pp{}), and \traj{} reaches \placeholder{14B-TRAJ-ACC}\% (\placeholder{14B-TRAJ-DELTA}\pp{}). The \cls{}--\cwm{} gap \placeholder{14B-GAP-TREND} from 2.62\pp{} at 8B to \placeholder{14B-CLS-CWM-GAP}\pp{} at 14B. \placeholder{14B-SCALING-TAKEAWAY}
108	
109	\paragraph{Baseline scaling.} Prompting baselines exhibit a mixed pattern at 14B. In the 3-shot setting, Qwen3-14B (73.12\%) outperforms Qwen3-8B (68.78\%) by 4.34\pp{}, consistent with the expected benefit of increased capacity for in-context learning. In contrast, 14B 0-shot accuracy (66.24\%) falls 2.46\pp{} below 8B (68.70\%); this reversal may reflect differences in instruction tuning between the two model sizes rather than a capacity limitation, and we do not draw strong conclusions from it. Regardless of prompting strategy, the best prompting result (14B 3-shot, 73.12\%) remains 16.82\pp{} below fine-tuned \cls{} at 8B (89.94\%, Table~\ref{tab:main_results}), confirming that model scaling alone does not substitute for task-specific fine-tuning at function level.
110	
111	\cwm{} flat scaling ($-$0.03\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \emph{cannot} benefit from scale. At function level, outputs are short status s
…[truncated 3241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_s53-baseline-narrative_20260522T211425",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-22T21:15:52.093321+00:00_

三处修改已完成：

1. **Table 1** 新增两行 14B baseline 数据（0-shot 66.24%, 3-shot ICL 73.12%），分别插在对应方法组内 8B 和 DeepSeek 之间
2. **§5.3** 新增 `\paragraph{Baseline scaling.}` 段落（line 109），覆盖三个要点：
   - 3-shot 14B > 8B (+4.34pp)，scale 在 few-shot 有效
   - 0-shot 14B < 8B (-2.46pp)，措辞审慎归因于 instruction tuning 差异
   - 最优 baseline (73.12%) 仍低于 fine-tuned CLS 8B (89.94%) 16.82pp，scale 不能替代 fine-tuning

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_write_s53-baseline-narrative_20260522T211425"
}
```

</details>

---
