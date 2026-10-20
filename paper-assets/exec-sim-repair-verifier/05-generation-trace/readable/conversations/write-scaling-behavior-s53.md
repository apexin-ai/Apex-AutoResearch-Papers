# write scaling behavior s53

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_write_scaling-behavior-s53_20260522T191829.jsonl`
- **Structured JSON:** [`95c812285fc1def91a38.json`](../../sessions/95/95c812285fc1def91a38.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-22T19:26:53.389577+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T19:26:53.389984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T19:26:53.390184+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T19:26:53.390389+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_framing.md\", \"content\": \"# Paper Framing — exec-sim-repair-verifier\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Deadline: ARR May 25, 2026\\n\\n## Framing Evolution\\n- **D116 (2026-05-16)**: Pivoted from \\\"CLS scales where generation fails\\\" (advocacy) to \\\"The Formulation Design Space for Neural Code Verification\\\" (empirical characterization)\\n- **D155 (2026-05-20)**: DeepSeek repo-level data confirms CWM collapse is **complexity-dependent** (both models collapse at repo-level), NOT tokenizer-specific. Original D116 claim \\\"Qwen 93% vs DeepSeek 11.8%\\\" was function-level only; repo-level shows DeepSeek CWM also 51-74% unparseable.\\n- **N4 Reframe**: Function-level equivalence elevated to headline finding; phase transition (func→repo divergence) as differentiating contribution.\\n\\n## Core Claims (current — post D155/N4 Reframe)\\n\\n1. **Formulation Equivalence at Function-Level**: CLS, CWM, and TRAJ achieve statistically equivalent accuracy at function-level across two model families (≤1.3pp gap, TOST p=0.007). Per-test CLS provides diagnostic granularity (which tests fail) at comparable accuracy with 217× throughput over CWM, though downstream re-repair benefit is unvalidated (n=44, p=0.42).\\n\\n2. **Phase Transition: Complexity-Dependent Divergence**: Formulations diverge 19-26pp at repo-level, driven by CWM format collapse (51-74% unparseable outputs, 0% truncation). Direction consistent across both model families; magnitude varies (Qwen3 74% unparseable vs DeepSeek 51% at matched seq_length). This is NOT tokenizer-specific — both models collapse when outputs are long and structured.\\n\\n3. **Error Complementarity**: CLS and CWM exhibit partial complementarity from different fail-bias degrees (CLS 56.5% FP, CWM 70.3% FP), yielding oracle ensemble 90.63% (+2.80pp over be
…[truncated 3591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T19:26:53.390554+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "filters": "{'conclusion': 'success'}",
  "fields": "['exp_id', 'metrics', 'hypothesis', 'spec', 'conclusion', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "filters": "{'conclusion': 'success'}",
    "fields": "['exp_id', 'metrics', 'hypothesis', 'spec', 'conclusion', 'status']"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T19:26:53.390691+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T19:26:53.390849+00:00_

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
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T19:26:53.391963+00:00_

Error: result (182,100 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/d6df5a11-fc7a-466c-8c43-88fa599de0b2/tool-results/mcp-agent-ml-research-read_registry-1779477529550.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/d6df5a11-fc7a-466c-8c43-88fa599de0b2/tool-results/mcp-agent-ml-research-read_registry-1779477529550.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T19:26:53.392254+00:00_

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
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T19:26:53.392429+00:00_

docs/paper/method.tex
docs/paper/checklist.tex
docs/paper/abstract.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Glob",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T19:26:53.392586+00:00_

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
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T19:26:53.392869+00:00_

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
…[truncated 20991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T19:26:53.393043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/skills/projects/exec-sim-repair-verifier/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/skills/projects/exec-sim-repair-verifier/distilled-writing.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T19:26:53.393341+00:00_

1	# Distilled Writing: Code Verification & LLM Program Repair
2	
3	8 deep-read papers (ICLR/NeurIPS/EMNLP/ACL 2016-2025).
4	
5	## Story Types
6	
7	**"突破局限型" dominates (5/8)**: S*, SWE-bench, SWE-bench Verified, QLoRA, SQuAD. Alternatives: "化繁为简" (LoRA), "跨界迁移" (SWE-agent: HCI→ACI), "统一框架" (BART: subsumes BERT+GPT).
8	- **Support**: 8/8 | **Confidence**: High
9	
10	## Hook Strategies
11	
12	**"Shocking number"** strongest: SWE-bench "a mere 1.96%", QLoRA "99.3% of ChatGPT on one GPU", SQuAD "51% vs 86.8%". **Cross-size leapfrog**: S* "7B > 32B by 10.1%". **Pain point**: LoRA "350GB → 35MB". **Example walkthrough**: SQuAD opens with specific QA making reader experience the task.
13	- **Support**: 6/8 | **Confidence**: High
14	
15	## Intro Structure
16	
17	**5-6 paragraphs**: P1=context+gap, P2=limitations, P3=method, P4=results preview, P5=contributions (3-4 items). Dataset papers use tighter 4-para. QLoRA: 8 contributions layered (3 techniques + system + models + study + analysis + open-source).
18	- **Support**: 8/8 | **Confidence**: High
19	
20	## Figure 1
21	
22	Three patterns: **method overview** (LoRA, BART, SWE-agent: 3/8), **problem illustration** (SWE-bench, SWE-bench Verified, SQuAD: 3/8), **teaser/motivation** (S*, QLoRA: 2/8). 2-3 panels, minimal decoration, color for semantics. BART's three-panel comparison is strongest — visually proves subsumption.
23	- **Confidence**: High
24	
25	## Results = Tables; Analysis = Figures
26	
27	**ALL 8 use tables for main results.** BART has zero result figures. Figures for: scaling (line), behavior (stacked bar/pie), qualitative examples. **Table norms**: rows=methods by_category (5/8), bold best (8/8), 5-9 baselines, single-run (6/8). LoRA's "Trainable Params" column alongside accuracy effective for efficiency arguments.
28	- **Support**: 8/8 | **Confidence**: High
29	
30	## Ablation Style
31	
32	**Full numbers (7/8)** over checkmark grids. Each table varies ONE dimension. BART places ablation (Table 1) BEFORE main res
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T19:26:53.393497+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/d6df5a11-fc7a-466c-8c43-88fa599de0b2/tool-results/mcp-agent-ml-research-read_registry-1779477529550.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result.get('experiments', result) if isinstance(result, dict) else result\n# Find scaling-related experiments\nfor exp in (exps if isinstance(exps, list) else [exps]):\n    exp_id = exp.get('exp_id', '')\n    hypothesis = str(exp.get('hypothesis', ''))\n    spec = exp.get('spec', {})\n    metrics = exp.get('metrics', {})\n    # Look for 4B, 8B, 14B, scaling related\n    text = json.dumps(exp).lower()\n    if any(k in text for k in ['4b', '8b', '14b', 'scal', 'cls_func', 'cls_repo', 'cwm_func', 'cwm_repo', 'traj_func', 'traj_repo']):\n        print(f'=== {exp_id} ===')\n        print(f'  hypothesis: {hypothesis[:200]}')\n        print(f'  spec: {json.dumps(spec)[:300]}')\n        print(f'  metrics: {json.dumps(metrics)[:400]}')\n        print()\n\" 2>&1 | head -300",
  "description": "Filter registry for scaling-related experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/d6df5a11-fc7a-466c-8c43-88fa599de0b2/tool-results/mcp-agent-ml-research-read_registry-1779477529550.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result.get('experiments', result) if isinstance(result, dict) else result\n# Find scaling-related experiments\nfor exp in (exps if isinstance(exps, list) else [exps]):\n    exp_id = exp.get('exp_id', '')\n    hypothesis = str(exp.get('hypothesis', ''))\n    spec = exp.get('spec', {})\n    metrics = exp.get('metrics', {})\n    # Look for 4B, 8B, 14B, scaling related\n    text = json.dumps(exp).lower()\n    if any(k in text for k in ['4b', '8b', '14b', 'scal', 'cls_func', 'cls_repo', 'cwm_func', 'cwm_repo', 'traj_func', 'traj_repo']):\n        print(f'=== {exp_id} ===')\n        print(f'  hypothesis: {hypothesis[:200]}')\n        print(f'  spec: {json.dumps(spec)[:300]}')\n        print(f'  metrics: {json.dumps(metrics)[:400]}')\n        print()\n\" 2>&1 | head -300",
    "description": "Filter registry for scaling-related experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T19:26:53.393629+00:00_

===  ===
  hypothesis: 
  spec: {}
  metrics: {}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T19:26:53.393822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T19:26:53.393989+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\graphicspath{{../../artifacts/}}
21	
22	% Lists
23	\usepackage{enumitem}
24	
25	% Custom commands
26	\newcommand{\cls}{\textsc{Cls}}
27	\newcommand{\cwm}{\textsc{Cwm}}
28	\newcommand{\traj}{\textsc{Traj}}
29	\newcommand{\fone}{F\textsubscript{1}}
30	\newcommand{\pp}{\,\text{pp}}
31	\newcommand{\tbd}{\textsc{tbd}}
32	
33	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
46	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
47	\label{fig:reformulation}
48	\end{figure*}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
57	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 18--26\pp{} with \cwm{} falling below majority baseline.}
58	\label{fig:scaling_gap}
59	\end{figure}
60	
61	
62	\input{related_work}
63	
64	\input{conclusion}
65
…[truncated 105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T19:26:53.394335+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "old_string": "% Graphics\n\\usepackage{graphicx}",
  "new_string": "% Graphics\n\\usepackage{graphicx}\n\\usepackage{xcolor}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "old_string": "% Graphics\n\\usepackage{graphicx}",
    "new_string": "% Graphics\n\\usepackage{graphicx}\n\\usepackage{xcolor}"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T19:26:53.394502+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T19:26:53.394631+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "old_string": "\\newcommand{\\tbd}{\\textsc{tbd}}",
  "new_string": "\\newcommand{\\tbd}{\\textsc{tbd}}\n\\newcommand{\\placeholder}[1]{{\\color{red}\\texttt{[#1]}}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "old_string": "\\newcommand{\\tbd}{\\textsc{tbd}}",
    "new_string": "\\newcommand{\\tbd}{\\textsc{tbd}}\n\\newcommand{\\placeholder}[1]{{\\color{red}\\texttt{[#1]}}}"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T19:26:53.394792+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T19:26:53.395025+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B and 8B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B and 8B (Qwen3, seeds 42/123, full bfloat16 precision). \\cls{} and \\traj{} scale positively; \\cwm{} does not. \\cwm{} scaling comparison is exploratory ($n{=}2$ seeds per size).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{Mean} & \\textbf{$\\Delta$ 4B$\\to$8B} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & \\textbf{88.68} & \\multirow{2}{*}{+1.27} \\\\\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & \\textbf{89.94} & \\\\\n\\midrule\n\\cwm{} & 4B & 87.51 & 87.20 & \\underline{87.36} & \\multirow{2}{*}{$-$0.03} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 87.33 & \\\\\n\\midrule\n\\traj{} & 4B & 85.66 & 85.47 & 85.57 & \\multirow{2}{*}{+2.13} \\\\\n\\traj{} & 8B & 87.60 & 87.79 & \\underline{87.70} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\n\\cwm{} flat scaling ($-$0.03\\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \\emph{cannot} benefit from scale. At function level, outputs are short status strings (e.g., ``PASS'' or brief error messages) and format compliance is near-perfect; at repo level, output complexity increases substantially, and the same generation bottleneck manifests as format collapse patterns we examine in \\S\\ref{sec:repo}. \\traj{} also shows no scaling benefit at repo level (72.92\\% at both 4B and 8B); only \\cls{} scales positively across both complexity levels.",
  "new_string": "\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B, 8B, and 14B (Qwen3, seeds 42/123, bfloat16). $\\Delta$: change from previous size. \\cwm{} comparison is exploratory ($n{=}2$ seeds per size).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{Mean} & \\textbf{$\\Delta$} \\\\\n\\midrule\n\\multirow{3}{*}{\\cls{}} & 4B & 87.83 & 89.52 & \\textbf{88.68} & --- \\\\\n & 8B & \\textbf{90.48} & 89.40 & \\textbf{89.94} & +1.27 \\\\\n & 14B & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} \\\\ % TODO: fill after 14B CLS experiment\n\\midrule\n\\multirow{3}{*}{\\cwm{}} & 4B & 87.51 & 87.20 & \\underline{87.36} & --- \\\\\n & 8B & 87.67 & 86.98 & 87.33 & $-$0.03 \\\\\n & 14B & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} \\\\ % TODO: fill after 14B CWM experiment\n\\midrule\n\\multirow{3}{*}{\\traj{}} & 4B & 85.66 & 85.47 & 85.57 & --- \\\\\n & 8B & 87.60 & 87.79 & \\underline{87.70} & +2.13 \\\\\n & 14B & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} \\\\ % TODO: fill after 14B TRAJ experiment\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\n% TODO: fill after 14B experiment\n% Replace \\placeholder{} with actual numbers from 14B evaluation.\n% Narrative depends on outcome:\n%   - CLS continues scaling → three-point consistency; classification robust across sizes\n%   - CWM remains flat → generation stagnation persists at 14B\n%   - CWM recovers → reframe as delayed scaling onset for generation\n%   - CLS-CWM gap widens → divergent trajectories; strengthen practical recommendation\n%   - CLS-CWM gap narrows → scaling partially compensates for formulation choice\n%   - TRAJ overtakes CWM → trajectory scoring as efficient middle ground\n%   - Update Figure~\\ref{fig:scaling_gap} with 14B data point\nAt 14B, \\cls{} reaches \\placeholder{14B-CLS-ACC}\\% (\\placeholder{14B-CLS-DELTA}\\pp{} from 8B), \\cwm{} reaches \\placeholder{14B-CWM-ACC}\\% (\\placeholder{14B-CWM-DELTA}\\pp{}), and \\traj{} reaches \\placeholder{14B-TRAJ-ACC}\\% (\\placeholder{14B-TRAJ-DELTA}\\pp{}). The \\cls{}--\\cwm{} gap \\placeholder{14B-GAP-TREND} from 2.62\\pp{} at 8B to \\placeholder{14B-CLS-CWM-GAP}\\pp{} at 14B. \\placeholder{14B-SCALING-TAKEAWAY}\n\n\\cwm{} flat scaling ($-$0.03\\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \\emph{cannot} benefit from scale. At function level, outputs are short status strings (e.g., ``PASS'' or brief error messages) and format compliance is near-perfect; at repo level, output complexity increases substantially, and the same generation bottleneck manifests as format collapse patterns we examine in \\S\\ref{sec:repo}. \\traj{} also shows no scaling benefit at repo level (72.92\\% at both 4B and 8B); only \\cls{} scales positively across both complexity levels."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B and 8B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B and 8B (Qwen3, seeds 42/123, full bfloat16 precision). \\cls{} and \\traj{} scale positively; \\cwm{} does not. \\cwm{} scaling comparison is exploratory ($n{=}2$ seeds per size).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{Mean} & \\textbf{$\\Delta$ 4B$\\to$8B} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & \\textbf{88.68} & \\multirow{2}{*}{+1.27} \\\\\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & \\textbf{89.94} & \\\\\n\\midrule\n\\cwm{} & 4B & 87.51 & 87.20 & \\underline{87.36} & \\multirow{2}{*}{$-$0.03} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 87.33 & \\\\\n\\midrule\n\\traj{} & 4B & 85.66 & 85.47 & 85.57 & \\multirow{2}{*}{+2.13} \\\\\n\\traj{} & 8B & 87.60 & 87.79 & \\underline{87.70} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\n\\cwm{} flat scaling ($-$0.03\\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \\emph{cannot} benefit from scale. At function level, outputs are short status strings (e.g., ``PASS'' or brief error messages) and format compliance is near-perfect; at repo level, output complexity increases substantially, and the same generation bottleneck manifests as format collapse patterns we examine in \\S\\ref{sec:repo}. \\traj{} also shows no scaling benefit at repo level (72.92\\% at both 4B and 8B); only \\cls{} scales positively across both complexity levels.",
    "new_string": "\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B, 8B, and 14B (Qwen3, seeds 42/123, bfloat16). $\\Delta$: change from previous size. \\cwm{} comparison is exploratory ($n{=}2$ seeds per size).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{Mean} & \\textbf{$\\Delta$} \\\\\n\\midrule\n\\multirow{3}{*}{\\cls{}} & 4B & 87.83 & 89.52 & \\textbf{88.68} & --- \\\\\n & 8B & \\textbf{90.48} & 89.40 & \\textbf{89.94} & +1.27 \\\\\n & 14B & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} \\\\ % TODO: fill after 14B CLS experiment\n\\midrule\n\\multirow{3}{*}{\\cwm{}} & 4B & 87.51 & 87.20 & \\underline{87.36} & --- \\\\\n & 8B & 87.67 & 86.98 & 87.33 & $-$0.03 \\\\\n & 14B & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} \\\\ % TODO: fill after 14B CWM experiment\n\\midrule\n\\multirow{3}{*}{\\traj{}} & 4B & 85.66 & 85.47 & 85.57 & --- \\\\\n & 8B & 87.60 & 87.79 & \\underline{87.70} & +2.13 \\\\\n & 14B & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} & \\placeholder{tbd} \\\\ % TODO: fill after 14B TRAJ experiment\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\n% TODO: fill after 14B experiment\n% Replace \\placeholder{} with actual numbers from 14B evaluation.\n% Narrative depends on outcome:\n%   - CLS continues scaling → three-point consistency; classification robust across sizes\n%   - CWM remains flat → generation stagnation persists at 14B\n%   - CWM recovers → reframe as delayed scaling onset for generation\n%   - CLS-CWM gap widens → divergent trajectories; strengthen practical recommendation\n%   - CLS-CWM gap narrows → scaling partially compensates for formulation choice\n%   - TRAJ overtakes CWM → trajectory scoring as efficient middle ground\n%   - Update Figure~\\ref{fig:scaling_gap} with 14B data point\nAt 14B, \\cls{} reaches \\placeholder{14B-CLS-ACC}\\% (\\placeholder{14B-CLS-DELTA}\\pp{} from 8B), \\cwm{} reaches \\placeholder{14B-CWM-ACC}\\% (\\placeholder{14B-CWM-DELTA}\\pp{}), and \\traj{} reaches \\placeholder{14B-TRAJ-ACC}\\% (\\placeholder{14B-TRAJ-DELTA}\\pp{}). The \\cls{}--\\cwm{} gap \\placeholder{14B-GAP-TREND} from 2.62\\pp{} at 8B to \\placeholder{14B-CLS-CWM-GAP}\\pp{} at 14B. \\placeholder{14B-SCALING-TAKEAWAY}\n\n\\cwm{} flat scaling ($-$0.03\\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \\emph{cannot} benefit from scale. At function level, outputs are short status strings (e.g., ``PASS'' or brief error messages) and format compliance is near-perfect; at repo level, output complexity increases substantially, and the same generation bottleneck manifests as format collapse patterns we examine in \\S\\ref{sec:repo}. \\traj{} also shows no scaling benefit at repo level (72.92\\% at both 4B and 8B); only \\cls{} scales positively across both complexity levels."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T19:26:53.395412+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T19:26:53.395625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "offset": "62",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "offset": "62",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T19:26:53.395818+00:00_

62	
63	\subsection{Scaling Behavior}
64	\label{sec:scaling}
65	
66	Beyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).
67	
68	\begin{table}[t]
69	\centering
70	\small
71	\caption{Model-size scaling: accuracy (\%) at 4B, 8B, and 14B (Qwen3, seeds 42/123, bfloat16). $\Delta$: change from previous size. \cwm{} comparison is exploratory ($n{=}2$ seeds per size).}
72	\label{tab:scaling}
73	\setlength{\tabcolsep}{4pt}
74	\begin{tabular}{llcccc}
75	\toprule
76	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{Mean} & \textbf{$\Delta$} \\
77	\midrule
78	\multirow{3}{*}{\cls{}} & 4B & 87.83 & 89.52 & \textbf{88.68} & --- \\
79	 & 8B & \textbf{90.48} & 89.40 & \textbf{89.94} & +1.27 \\
80	 & 14B & \placeholder{tbd} & \placeholder{tbd} & \placeholder{tbd} & \placeholder{tbd} \\ % TODO: fill after 14B CLS experiment
81	\midrule
82	\multirow{3}{*}{\cwm{}} & 4B & 87.51 & 87.20 & \underline{87.36} & --- \\
83	 & 8B & 87.67 & 86.98 & 87.33 & $-$0.03 \\
84	 & 14B & \placeholder{tbd} & \placeholder{tbd} & \placeholder{tbd} & \placeholder{tbd} \\ % TODO: fill after 14B CWM experiment
85	\midrule
86	\multirow{3}{*}{\traj{}} & 4B & 85.66 & 85.47 & 85.57 & --- \\
87	 & 8B & 87.60 & 87.79 & \underline{87.70} & +2.13 \\
88	 & 14B & \placeholder{tbd} & \placeholder{tbd} & \placeholder{tbd} & \placeholder{tbd} \\ % TODO: fill after 14B TRAJ experiment
89	\bottomrule
90	\end{tabular}
91	\end{table}
92	
93	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +2.13\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed supers
…[truncated 1965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T19:26:53.395985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T19:26:53.396130+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\usepackage{xcolor}
21	\graphicspath{{../../artifacts/}}
22	
23	% Lists
24	\usepackage{enumitem}
25	
26	% Custom commands
27	\newcommand{\cls}{\textsc{Cls}}
28	\newcommand{\cwm}{\textsc{Cwm}}
29	\newcommand{\traj}{\textsc{Traj}}
30	\newcommand{\fone}{F\textsubscript{1}}
31	\newcommand{\pp}{\,\text{pp}}
32	\newcommand{\tbd}{\textsc{tbd}}
33	\newcommand{\placeholder}[1]{{\color{red}\texttt{[#1]}}}
34	
35	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
36	\author{Anonymous}
37	
38	\begin{document}
39	\maketitle
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_scaling-behavior-s53_20260522T191829",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-22T19:26:53.396301+00:00_

改动完成。总结：

**main.tex**: 添加了 `\usepackage{xcolor}` 和 `\newcommand{\placeholder}` 命令。

**experiments.tex §5.3**:
- **表格**：从 2 行/方法（multirow×2）改为 3 行/方法（multirow×3），每个方法的 14B 行用 `\placeholder{tbd}` 占位，行尾 TODO 标注对应实验
- **列头**：`$\Delta$ 4B$\to$8B` 简化为 `$\Delta$`（适配多级 delta）
- **新增 14B 叙事段**（L95-105）：句子骨架写好（CLS/CWM/TRAJ 各一个 `\placeholder{ACC}` + `\placeholder{DELTA}`，gap trend 和 takeaway 各一个占位），上方 TODO 注释列出 6 种叙事分支（CWM flat / CWM recovers / gap widens / gap narrows 等），14B 数据出来后按实际结果选择填充
- **现有 4B→8B 分析和 CWM caveat 段**保持不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_write_scaling-behavior-s53_20260522T191829"
}
```

</details>

---
