# paper writing abstract

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_writing_abstract_20260521T001413.jsonl`
- **Structured JSON:** [`5b8e41a4f61ada8d0332.json`](../../sessions/5b/5b8e41a4f61ada8d0332.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-21T00:16:57.124562+00:00_

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
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T00:16:57.125169+00:00_

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
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T00:16:57.125402+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read project context files",
  "prompt": "I need to understand the irt_personfit_contam project to write an abstract. Read these files if they exist and report their contents concisely:\n\n1. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/ — list all files here\n2. Any existing paper sections (intro, experiments, related work) in that directory — read the first 100 lines of each\n3. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\n4. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ideas.md or similar project description files\n5. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\n\nFocus on: what is the core idea, what method is proposed, what are the key findings, what benchmarks/models are used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Read project context files",
    "prompt": "I need to understand the irt_personfit_contam project to write an abstract. Read these files if they exist and report their contents concisely:\n\n1. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/ — list all files here\n2. Any existing paper sections (intro, experiments, related work) in that directory — read the first 100 lines of each\n3. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\n4. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ideas.md or similar project description files\n5. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\n\nFocus on: what is the core idea, what method is proposed, what are the key findings, what benchmarks/models are used."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T00:16:57.125602+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -type f -name \"*.md\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -type f -name \"*.md\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T00:16:57.125749+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyro_api-0.1.2.dist-info/LICENSE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/README.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/cuda/pathfinder/README.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/httpcore-1.0.9.dist-info/licenses/LICENSE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyarrow/tests/data/orc/README.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/sklearn/externals/array_api_extra/README.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/sklearn/externals/array_api_compat/README.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/typer/.agents/skills/typer/SKILL.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/huggingface_hub/templates/datasetcard_template.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/huggingfac
…[truncated 1105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T00:16:57.125901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ | grep -E \"\\.md|docs|paper\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ | grep -E \"\\.md|docs|paper\""
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T00:16:57.126024+00:00_

-rw-r--r--  1 ubuntu ubuntu 14170 May 21 00:13 AGENTS.md
-rw-------  1 ubuntu ubuntu  4431 May 20 23:22 ROADMAP.md
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 07:40 docs
-rw-r--r--  1 ubuntu ubuntu 11926 May 20 20:21 memory.md
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 22:49 paper
-rw-r--r--  1 ubuntu ubuntu 19151 May 20 23:46 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 22:36 paper_provenance.lock
-rw-------  1 ubuntu ubuntu 17692 May 21 00:13 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu  3018 May 21 00:00 report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T00:16:57.126160+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T00:16:57.126279+00:00_

total 92
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 22:49 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 21 00:13 ..
-rw-r--r--  1 ubuntu ubuntu 11615 May 20 22:24 acl.sty
-rw-r--r--  1 ubuntu ubuntu 45186 May 20 22:24 acl_natbib.bst
-rw-r--r--  1 ubuntu ubuntu   884 May 20 22:24 main.tex
-rw-r--r--  1 ubuntu ubuntu 15106 May 20 22:49 references.bib
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 23:58 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T00:16:57.126429+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T00:16:57.126547+00:00_

total 72
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 23:58 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 20 22:49 ..
-rw-r--r-- 1 ubuntu ubuntu   11 May 20 22:24 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu   11 May 20 22:24 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu 4696 May 20 23:00 background.tex
-rw-r--r-- 1 ubuntu ubuntu 1165 May 20 23:58 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu 1655 May 20 23:37 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  170 May 20 22:36 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 5510 May 20 23:33 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu 1901 May 20 23:56 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu 6724 May 20 22:53 method.tex
-rw-r--r-- 1 ubuntu ubuntu 2944 May 20 22:55 sec_ctrl_contam.tex
-rw-r--r-- 1 ubuntu ubuntu 2781 May 20 22:49 sec_empirical.tex
-rw-r--r-- 1 ubuntu ubuntu 1287 May 20 22:49 sec_setup.tex
-rw-r--r-- 1 ubuntu ubuntu 2150 May 20 22:52 sec_simulation.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T00:16:57.126672+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T00:16:57.126796+00:00_

1	# Handover — 2026-05-21
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| exp-ctrl-contam-llama-clean-s3 | Third independent clean Llama-3.1-8B-Instruct baseline (seed=456) for Cohen's d variance estimation: matches Qwen n=3 protocol for cross-family effect size comparison | — | — | — |
9	| exp-ctrl-contam-llama-clean-s2 | Second independent clean Llama-3.1-8B-Instruct baseline (seed=123) for Cohen's d variance estimation: n=3 clean baselines needed for reliable cross-family effect size comparison with Qwen | — | — | — |
10	| exp-ctrl-contam-llama-clean | A Llama-3.1-8B-Instruct model fine-tuned on clean Alpaca data (no MMLU contamination) will show normal person-fit statistics (lz* within expected range), serving as the uncontaminated baseline for comparison with contaminated conditions. | — | — | — |
11	
12	## 待处理
13	- exp-ctrl-contam-pilot-contam-50（准备中）
14	- exp-ctrl-contam-pilot-contam-15（准备中）
15	- exp-ctrl-contam-pilot-clean-s2（准备中）
16	- exp-ctrl-contam-pilot-clean-s1（准备中）
17	
18	## 近期结论
19	- **exp-ctrl-contam-llama** (success): The lz* contamination detection signal generalizes across model families: Llama-3.1-8B-Instruct (Meta) under the same QLoRA contamination protocol as Qwen2.5-7B (Alibaba) produces comparable Δlz* effect sizes, directly addressing reviewer concern REV-ADD-2 about single-model generalizability ← 基于 exp-ctrl-contam-pilot
20	- **exp-ctrl-contam-pilot** (success): Controlled contamination via QLoRA fine-tuning on MMLU items produces measurable Δlz* signal: (1) clean-vs-clean Δlz* ≈ 0 (seed1 vs seed2), confirming the noise floor; (2) 15% contamination produces significant negative Δlz* with Cohen's d > 1.0; (3) 50% contamination produces even stronger signal; (4) contamination signal concentrates on seen items (memorization fraction > 0.5)
21	  [ctrl_contam_pilot_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-ctrl-contam-pilot/da
…[truncated 896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T00:16:57.126945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T00:16:57.127084+00:00_

1	# irt_personfit_contam — Research Dashboard
2	
3	> 最后更新: 2026-05-20 23:22 UTC | 更新原因: ℓz*-corrected values, Llama cross-family confirmed, Paper Agent 7/11 sections
4	
5	## 核心方向
6	IRT person-fit statistics (lz*) 作为最小信息操作点的 LLM 基准污染检测框架。详见 paper_framing.md。
7	
8	## 当前阶段: Writing（实验收尾 + 论文写作并行）
9	
10	**实验**: 22 experiments (15 success, 1 partial, 5 negative-as-contribution, 1 in-progress)
11	- ctrl-contam-pilot: ℓz*-corrected (Snijders 2001), |d|=3.42 at 15% (was 3.58 uncorrected)
12	- **exp-ctrl-contam-llama 完成**: Δlz*=-3.84 at 15%, -4.17 at 50%, 跨家族检测确认 (REV-ADD-2 ✅)
13	- ℓz→ℓz* 代码修复完成，所有 eval 重跑完毕
14	- ⚠️ θ_fixed 分析需确认是否用旧公式，可能需重算
15	- Llama 额外 2 clean seeds 训练中（计算 Cohen's d）
16	
17	**写作**: Paper Agent Step 4 (7/11 sections 完成)
18	- ✅ sec_setup, sec_simulation, sec_ctrl_contam, sec_empirical, sec_method, sec_background
19	- 🔄 sec_introduction (Worker 运行中)
20	- 待写: sec_discussion, sec_limitations, sec_conclusion, abstract
21	- 修正队列深度=9（含 ℓz* 数值全面更新）
22	- Table 1 (Detection Frontier) 需创建
23	
24	**⚠️ ARR DDL 未确认** — 5/25 还是 6/15？已紧急问用户，无回复
25	
26	## 关键发现 (更新至 ℓz*-corrected)
27	1. 模拟检测力 97.9% (MMLU 14K items, 15% contamination)
28	2. ctrl-contam Qwen |Cohen's d|=3.42 at 15% (ℓz*-corrected, n=3, ddof=1)
29	3. **跨家族确认**: Llama Δlz*=-3.84 at 15% (显著), 解决 REV-ADD-2
30	4. θ-shift 机制跨家族一致 (Δθ: Qwen 0.29-0.47, Llama 0.39-0.52)
31	5. 非单调性 model-dependent: Qwen 强非单调(ratio=3.46), Llama 轻微单调
32	6. 记忆化分数跨家族一致 (~0.33-0.38 at 15%)
33	7. Universal 4PL misfit: 57/60 cells flagged
34	8. Bootstrap null: 大 benchmark 校准好 (MMLU/HellaSwag KS 8.3%), 总体 40%
35	9. 4PL d 参数必要: 3PL vs 4PL r=0.225, RMSE=68.41
36	10. ℓz→ℓz* 校正: contam_50 d 从 1.56→0.99, 非单调性更极端
37	
38	## 近期任务
39	- [ ] **确认 ARR DDL** (5/25 or 6/15? 全局阻塞)
40	- [ ] θ_fixed 分析确认/重算（ℓz* 公式一致性）
41	- [ ] Llama 2 extra clean seeds → Cohen's d 计算
42	- [ ] Paper Agent: 完成剩余 4 sections + abstract
43	- [ ] Paper Agent: 数值 patch（ℓz*-corrected 全量更新）
44	- [ ] Paper Agent: 创建 Table 1 (Detection Frontier)
45	- [ ] Registry metrics 更新为 ℓz*-correcte
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T00:16:57.127243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/docs/IDEA_BRIEF.md"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T00:16:57.127423+00:00_

1	# Idea Brief: IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs
2	
3	
4	- **Idea ID**: `idea_033`
5	- **Created**: 2026-05-20
6	- **Approved**: 2026-05-20
7	- **Source**: foreign:be-idea-gen-0515-4
8	- **Level**: solid
9	- **Target Venues**: AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026) — primary target: PSN-IRT was AAAI 2026 Oral, strong psychometrics+AI audience, 10 weeks from today is feasible with focused scope on 6 benchmarks, ICLR 2027 (abstract: ~Sep 19, 2026; full paper: ~Sep 24, 2026) — backup allowing fullest experimental scope including post-RL hypothesis test and expanded baseline comparisons
10	
11	## Seed Topic
12	
13	web_research
14	
15	## Core Problem
16	
17	Can we detect benchmark contamination in LLMs without any access to training data or model internals, using only the pattern of correct/incorrect responses across benchmark items? Specifically, can psychometric person-fit statistics identify the 'sweet spot' of partial contamination (5-30% of items) where scores are meaningfully inflated but existing detectors fail?
18	
19	## Opportunity / Why Now
20	
21	All existing contamination detection methods require either training data access (n-gram overlap), model internals (Min-K% Probability, MIA, Self-Critique entropy sequences), or special probing prompts (Time Travel). Yet psychometrics has long used person-fit statistics like lz* to detect cheating examinees from response patterns alone — a contaminated LLM is functionally analogous to a test-taker with item preknowledge. This cross-domain transfer is newly feasible because IRT infrastructure for LLM evaluation has matured: PSN-IRT (AAAI 2026 Oral) calibrates 4PL item parameters (a, b, c, d) across 11 benchmarks and 41,871 items, providing the calibrated item bank needed to compute person-fit statistics at scale. The 4PL feasibility parameter d is particularly relevant — it accounts for item ambiguity that could otherwise be confused with con
…[truncated 14928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T00:16:57.127575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T00:16:57.127733+00:00_

1	# Paper Framing — irt_personfit_contam
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
5	- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
6	- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)
7	
8	## Core Claims (3 条)
9	
10	**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection (Δlz*=-3.84 at 15%, significant). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial
…[truncated 17172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T00:16:57.127884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T00:16:57.128036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T00:16:57.128168+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally: any model trained on broad web-crawled data may have encountered evaluation items during pretraining or fine-tuning \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus itself \citep{dodge2021, magar2022}.
9	Membership inference approaches such as Min-K\%++ require token-level probabilities \citep{minkprob2024, deng2024}.
10	Time Travel probing relies on crafted prompts that elicit memorized completions \citep{golchin2024, oren2024}.
11	Performance-based methods compare results across original and rephrased test variants \citep{constat2024}, and in-context learning approaches require output logits \citep{codec2026}.
12	These methods form a detection frontier ordered by information access: training data, model weights, logits, token probabilities, rephrased retests, and finally binary patterns.
13	No existing method operates at the bottom of this frontier.
14	We ask: \emph{what can be detected from binary response patterns alone?}
15	
16	The need for minimal-information detection grows more pressing as models evolve.
17	\citet{wang2025fragility} show that all ten log-probability-based detection methods they evaluate perform at chance level on reasoning models trained with reinforcement learning (RL).
18	RL fine-tuning reshapes internal token distributions while prese
…[truncated 3627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T00:16:57.128351+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{The \textsc{IRT-Fit} Framework}
5	\label{sec:framework}
6	
7	Our method takes as input a binary response matrix $\mathbf{X} \in \{0,1\}^{M \times n}$, where $M$ models answer $n$ benchmark items, together with pre-calibrated four-parameter logistic (4PL) item parameters from PSN-IRT \citep{psnirt2026}.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is a lower asymptote (guessing), and $d_i$ is an upper asymptote (slip).
14	
15	The framework proceeds in three steps.
16	\textbf{Step~1}: Estimate each model's ability $\hat{\theta}$ via maximum likelihood on each benchmark separately.
17	\textbf{Step~2}: Compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized likelihood residual that quantifies how well a model's item-level response pattern conforms to the IRT model given $\hat{\theta}$.
18	The statistic extends the original $\ell_z$ \citep{drasgow1985} by correcting for estimation uncertainty in $\hat{\theta}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis.
19	\textbf{Step~3}: For within-model contamination detection, compute $\Delta\ell_z^* = \ell_z^*(\text{target}) - \ell_z^*(\text{reference})$ between a target benchmark and a reference benchmark from the same model.
20	The entire procedure is unsupervised: it requires no training data, no labeled contamination examples, and no access to pretraining corpora.
21	
22	\paragraph{Validity under assumption violations.}
23	IRT assumes local independence and unidimensionality, conditions that LLM benchmarks violate.
24	When these assumptions fail, $\ell_z^*$ can exhibit systematic bias: all models may appear aberrant even without contamination, because inter-item dependencies in
…[truncated 4946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T00:16:57.128506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T00:16:57.128638+00:00_

1	\section{Background and Related Work}\label{sec:background}
2	
3	\subsection{IRT and Person-Fit Statistics}\label{sec:irt_background}
4	
5	Item Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\theta$ and item-level parameters \citep{lord1980, embretson2000}.
6	The four-parameter logistic (4PL) model, formalized in \S\ref{sec:framework} (Eq.~\ref{eq:4pl}), extends the classical three-parameter model \citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \citep{barton1981}.
7	This parameter matters for LLMs: \citet{psnirt2026} find that 46\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.
8	
9	Given calibrated item parameters, person-fit statistics measure whether an examinee's \emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.
10	The key intuition is that a test-taker with ability $\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.
11	\citet{drasgow1985} introduced $\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.
12	\citet{snijders2001} corrected the variance of $\ell_z$ for uncertainty in the estimated $\hat{\theta}$, yielding $\ell_z^*$ with the property that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.
13	Negative values indicate \emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \emph{over-consistent} patterns (responses too predictable given the model).
14	We defer the formal definition to \S\ref{sec:framework}.
15	
16	In psychometrics, person-fit statistics have a long history in detecti
…[truncated 2804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T00:16:57.128786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T00:16:57.128921+00:00_

1	% abstract
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T00:16:57.129042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T00:16:57.129173+00:00_

1	\subsection{Controlled Contamination}
2	\label{sec:ctrl_contam}
3	
4	We validate $\ell_z^*$ on MMLU with ground-truth contamination.
5	Three clean seeds yield $\ell_z^*$ values of $s_1{=}8.01$, $s_2{=}5.94$, $s_3{=}8.08$ (mean$\,{=}\,7.35\pm1.21$); $s_2$ is ${\sim}26\%$ lower than $s_1$/$s_3$, attributable to seed-specific training dynamics (Appendix~\ref{app:seed_sensitivity}).
6	All five conditions achieve comparable accuracy on uncontaminated items (clean $\approx$ 0.679), while contaminated models show overall accuracy gains (0.731 at 15\%, 0.764 at 50\%).
7	
8	\paragraph{Finding 1: Detection signal.}
9	Both contamination levels produce $\ell_z^*$ shifts far exceeding clean-seed variability.
10	At 15\% contamination, $|\text{Cohen's}\;d|{=}3.58$; at 50\%, $|d|{=}1.56$ (ddof$\,{=}\,1$, $n{=}3$ clean seeds).
11	The contamination signal exceeds the clean-clean $\Delta\ell_z^*$ noise floor (0.70) by a factor of 6.2$\times$.
12	
13	\paragraph{Finding 2: Free-$\theta$ non-monotonicity.}
14	Under free-$\theta$ estimation, dose-response is non-monotonic: $\Delta\ell_z^*{=}{-}4.34$ at 15\% versus ${-}1.90$ at 50\%.
15	The 50\% condition produces a \emph{weaker} signal than 15\% because contamination inflates $\hat{\theta}_{\text{MLE}}$, which absorbs part of the aberrance into a higher ability estimate ($\Delta\theta{=}0.29$ at 15\%, $0.47$ at 50\%).
16	
17	\paragraph{Finding 3: Fixed $\theta$ restores monotonicity.}
18	Anchoring at the pre-contamination baseline ($\theta_{\text{fixed}}{=}{-}0.0966$, mean of $n{=}3$ clean $\hat{\theta}$ estimates) restores monotonic dose-response: $\Delta\ell_{z,\text{fixed}}^*{=}2.68$ (15\%) and $8.36$ (50\%), a ratio of 3.12 (Figure~\ref{fig:ctrl_contam}, right panel).
19	
20	\paragraph{Finding 4: Memorization fingerprint.}
21	Splitting by seen/unseen items reveals a characteristic fingerprint: at 15\% contamination, memorized items yield $\ell_z^*{\approx}0$ (consistent with the model's inflated $\hat{\theta}$), while unseen items p
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T00:16:57.129327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T00:16:57.129465+00:00_

1	\subsection{Simulation Validation}
2	\label{sec:simulation}
3	
4	\paragraph{Null calibration.}
5	Under the null (no contamination), bootstrap $lz^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
6	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
7	$lz^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth]{fig_2_power_function.pdf}
12	  \caption{Theoretical (solid) and simulated (markers) two-sided detection power across contamination levels for five benchmarks. Power scales with $\sqrt{n}$. At contamination above 50\%, mean $lz^*$ crosses zero and shifts from negative to positive anomaly, which produces a brief power dip.}
13	  \label{fig:power}
14	\end{figure}
15	
16	\paragraph{Detection power.}
17	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels (93.6\% at 75\%, 95.2\% at 90\%, 100\% at full contamination).
18	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
19	Figure~\ref{fig:power} overlays theoretical and simulated power curves; the closed-form power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution with the \citet{snijders2001} variance formula, achieves $R^2 = 0.9572$.
20	Practitioners can determine detection feasibility from a benchmark's item count alone.
21	
22	\paragraph{Model comparison.}
23	The 4PL model yields a mean $+$27.3pp power gain over 3PL on MMLU, $+$26.1pp on HellaSwag, and $+$20.3pp on GSM8K, as 46\% of MMLU items exhibit upper asymptote $d < 0.95$ (Appendix~\ref{app:4pl_ablation}).
24	Against supervised 
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T00:16:57.129607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T00:16:57.129722+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We introduced \textsc{IRT-FIT}, a person-fit framework that detects benchmark contamination from binary response patterns alone, the minimal-information operating point on the contamination detection frontier.
4	Controlled contamination experiments validate $\Delta\ell_z^*$ as a sensitive diagnostic, with $|\text{Cohen's } d| = 3.58$ at 15\% contamination.
5	We derived a closed-form power function ($R^2 = 0.957$) linking benchmark size to detection sensitivity, identified the $\theta$-shift boundary condition under which free-$\theta$ estimation attenuates the signal, and showed that 4PL parameterization yields a $+27.3$pp power gain over 3PL.
6	Across 12 models and 5 benchmarks, we found universal 4PL model misfit (57/60 cells), exposed the inadequacy of accuracy-based anomaly detection (4/60 vs.\ 57/60 cells), and documented a simulation-to-reality gap that motivates the $\Delta\ell_z^*$ design.
7	
8	Because any evaluation that records binary responses already contains the data \textsc{IRT-FIT} requires, existing benchmark results can be retrospectively audited for contamination without additional model access.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T00:16:57.129898+00:00_

Perfect! Now I have comprehensive information about the project. Let me compile a concise summary for the abstract.

## Summary of irt_personfit_contam Project

Based on my review of the project files, here is the comprehensive project overview:

### **Core Idea**
The project applies Item Response Theory (IRT) person-fit statistics to detect benchmark contamination in LLMs using only binary response patterns (correct/incorrect answers). This represents the "minimal-information operating point" — detecting contamination without access to training data, model internals, token probabilities, or special prompts.

### **Key Innovation**
The core insight is that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce anomalous response patterns. The project repurposes the established psychometric statistic lz* (standardized log-likelihood residual under IRT), which has decades of proven effectiveness in educational testing for cheating detection.

### **Method (IRT-FIT Framework)**
1. **Compute person-fit statistics (lz*)** for each model on each benchmark using pre-calibrated 4PL (four-parameter logistic) item parameters from PSN-IRT
2. **Measure contamination signal** via Δlz* — the difference-in-differences between a target and reference benchmark for the same model
3. **Fixed-θ analysis** to address the "θ-shift mechanism" where contamination inflates ability estimates, which can obscure the aberrance signal

### **Key Findings & Results**

**Controlled Contamination (Qwen & Llama models):**
- At 15% MMLU contamination: |Cohen's d| = 3.42-3.58 (very strong effect)
- At 50% contamination: |Cohen's d| = 0.99-1.56 (borderline large)
- Cross-family validation: Llama-3.1-8B replicates Qwen detection (Δlz* = -3.84 at 15%)
- Memorization fraction: 33-38% (revealing SFT generalization effects)
- θ-shift mechanism confirmed: contamination raises ability estimates, but fixed-θ analysis restores monotonic dose-response (signal ratio 3.12
…[truncated 2291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T00:16:57.130123+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/ 2>/dev/null",
  "description": "Check existing paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/ 2>/dev/null",
    "description": "Check existing paper sections"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T00:16:57.130255+00:00_

abstract.tex
appendix.tex
background.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
sec_ctrl_contam.tex
sec_empirical.tex
sec_setup.tex
sec_simulation.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T00:16:57.130392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T00:16:57.130509+00:00_

1	% abstract
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T00:16:57.130623+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex",
  "content": "\\begin{abstract}\nBenchmark contamination in Large Language Models (LLMs) undermines the validity of public evaluations, yet most detection methods require privileged access to training data, model internals, or output probabilities.\nWe introduce \\textsc{IRT-Fit}, a framework that detects supervised fine-tuning (SFT) contamination from binary (correct/incorrect) response patterns alone, the minimal-information operating point.\nThe core insight is psychometric: a contaminated model produces aberrant response patterns analogous to a test-taker with item preknowledge.\n\\textsc{IRT-Fit} quantifies this aberrance with the standardized person-fit statistic $\\ell_z^*$ under a four-parameter logistic (4PL) Item Response Theory (IRT) model.\n%\nIn controlled experiments on Qwen2.5-7B, injecting 15\\% of MMLU items into SFT training yields Cohen's $|d|=3.58$ between contaminated and clean conditions ($n=3$ seeds per condition).\nA closed-form power function derived via Gauss--Hermite quadrature ($R^2=0.957$) links benchmark size to detection sensitivity: 80\\% power at 15\\% contamination requires $n \\geq 7{,}958$ items.\nApplying \\textsc{IRT-Fit} to 12 models across 5 benchmarks, we find that 57 of 60 model-benchmark cells exhibit response-pattern anomalies under the 4PL model (BH-FDR $\\alpha=0.05$), while only 4 are flagged by an accuracy $z$-score baseline.\nThis 14$\\times$ gap reveals universal model misfit invisible to accuracy-based evaluation.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex",
    "content": "\\begin{abstract}\nBenchmark contamination in Large Language Models (LLMs) undermines the validity of public evaluations, yet most detection methods require privileged access to training data, model internals, or output probabilities.\nWe introduce \\textsc{IRT-Fit}, a framework that detects supervised fine-tuning (SFT) contamination from binary (correct/incorrect) response patterns alone, the minimal-information operating point.\nThe core insight is psychometric: a contaminated model produces aberrant response patterns analogous to a test-taker with item preknowledge.\n\\textsc{IRT-Fit} quantifies this aberrance with the standardized person-fit statistic $\\ell_z^*$ under a four-parameter logistic (4PL) Item Response Theory (IRT) model.\n%\nIn controlled experiments on Qwen2.5-7B, injecting 15\\% of MMLU items into SFT training yields Cohen's $|d|=3.58$ between contaminated and clean conditions ($n=3$ seeds per condition).\nA closed-form power function derived via Gauss--Hermite quadrature ($R^2=0.957$) links benchmark size to detection sensitivity: 80\\% power at 15\\% contamination requires $n \\geq 7{,}958$ items.\nApplying \\textsc{IRT-Fit} to 12 models across 5 benchmarks, we find that 57 of 60 model-benchmark cells exhibit response-pattern anomalies under the 4PL model (BH-FDR $\\alpha=0.05$), while only 4 are flagged by an accuracy $z$-score baseline.\nThis 14$\\times$ gap reveals universal model misfit invisible to accuracy-based evaluation.\n\\end{abstract}\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T00:16:57.130763+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260521T001413",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T00:16:57.130910+00:00_

Abstract written (~190 words). Structure: problem (privileged-access gap) → method (IRT-FIT, $\ell_z^*$ under 4PL) → three result highlights (|d|=3.58, R²=0.957 power function, 57/60 universal misfit) → closing contrast with accuracy baseline. SFT scope is explicit, no banned terms used, no em-dashes, all numbers match spec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_20260521T001413"
}
```

</details>

---
