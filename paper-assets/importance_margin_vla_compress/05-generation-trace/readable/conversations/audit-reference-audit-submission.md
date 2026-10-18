# audit reference audit submission

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/chats/worker_audit_reference_audit_submission_20260528T170501.jsonl`
- **Structured JSON:** [`14aa6b0e4883a9f99060.json`](../../sessions/14/14aa6b0e4883a9f99060.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

69 recorded events

### Tool call

_source line 1 · 2026-05-28T17:10:43.584094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/reference-audit.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T17:10:43.584832+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T17:10:43.584988+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T17:10:43.585118+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T17:10:43.585294+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T17:10:43.585422+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T17:10:43.585567+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T17:10:43.585687+00:00_

artifacts/corl_template/corl_2026_template_submission/example.bib
artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.bib
artifacts/_project/paper/new_references_8papers.bib
artifacts/new_references_8papers.bib
artifacts/missing_citations_4papers.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T17:10:43.585804+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T17:10:43.585939+00:00_

artifacts/corl_template/corl_2026_template_submission/example.tex
artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260516T075046/best/paper.tex
artifacts/dream_reports/dream_20260516T075046/median/paper.tex
artifacts/dream_reports/dream_20260516T075046/worst/paper.tex
docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
artifacts/_project/paper/results_draft.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
artifacts/dream_reports/dream_20260520T155932/best/paper.tex
artifacts/dream_reports/dream_20260520T155932/median/paper.tex
artifacts/dream_reports/dream_20260520T155932/worst/paper.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
docs/paper/discussion.tex
artifacts/dream_reports/dream_20260525T050917/best/paper.tex
artifacts/dream_reports/dream_20260525T050917/median/paper.tex
artifacts/dream_reports/dream_20260525T050917/worst/paper.tex
artifacts/_project/paper/tab_model_properties_56d5eb.tex
artifacts/_project/paper/tab_model_properties.tex
artifacts/tab_model_properties.tex
artifacts/_project/paper/tab_main_results_8f3985.tex
artifacts/_project/paper/tab_main_results.tex
artifacts/tab_main_results.tex
docs/paper/analysis.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/main.tex
docs/paper/experiments.tex

…[truncated 21 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T17:10:43.586087+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/reference-audit*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/reference-audit*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T17:10:43.586258+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T17:10:43.586401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/",
  "description": "List project root directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/",
    "description": "List project root directory"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T17:10:43.586554+00:00_

total 4192
drwxr-xr-x 12 ubuntu ubuntu    4096 May 28 17:05 .
drwxrwxr-x  5 ubuntu ubuntu    4096 May 15 12:52 ..
drwxr-xr-x  3 ubuntu ubuntu    4096 May 15 09:39 .claude
-rw-------  1 ubuntu ubuntu       0 May 19 13:50 .registry_g6b180tc.tmp
drwxr-xr-x  6 ubuntu ubuntu    4096 May 28 13:30 .venv
-rw-r--r--  1 ubuntu ubuntu   13525 May 28 17:04 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu       0 May 15 11:09 ROADMAP.lock
-rw-------  1 ubuntu ubuntu    3744 May 28 14:44 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu      90 May 28 16:09 _last_visual_review.json
-rw-r--r--  1 ubuntu ubuntu       0 May 24 08:40 _paper_figure.lock
-rw-r--r--  1 ubuntu ubuntu   32016 May 24 08:49 _paper_figure_result.json
-rw-r--r--  1 ubuntu ubuntu   23587 May 17 10:25 analyze_attention.py
-rw-r--r--  1 ubuntu ubuntu    9329 May 18 00:59 analyze_openvla_attention_entropy.py
-rw-r--r--  1 ubuntu ubuntu   17204 May 20 07:02 analyze_openvla_oft.py
drwxr-xr-x 36 ubuntu ubuntu   12288 May 28 16:19 artifacts
drwxr-xr-x  2 ubuntu ubuntu  532480 May 28 16:46 checkpoints
-rw-r--r--  1 ubuntu ubuntu       0 May 19 12:50 constraints.lock
-rw-------  1 ubuntu ubuntu    2554 May 28 12:02 constraints.yaml
-rw-r--r--  1 ubuntu ubuntu  167398 May 25 12:24 crossover_heatmap_check.png
-rw-r--r--  1 ubuntu ubuntu  190457 May 25 12:30 crossover_heatmap_v2.png
-rw-r--r--  1 ubuntu ubuntu  118520 May 25 12:24 cv_scatter_check.png
-rw-r--r--  1 ubuntu ubuntu  135338 May 25 12:30 cv_scatter_v2.png
-rw-r--r--  1 ubuntu ubuntu       0 May 15 11:09 decisions.lock
-rw-------  1 ubuntu ubuntu  272734 May 28 03:33 decisions.yaml
-rw-r--r--  1 ubuntu ubuntu  400997 May 25 12:24 disruption_curve_check.png
-rw-r--r--  1 ubuntu ubuntu  377460 May 25 12:30 disruption_curve_v2.png
drwxr-xr-x  4 ubuntu ubuntu    4096 May 28 15:50 docs
-rwxr-xr-x  1 ubuntu ubuntu       0 May 15 11:06 dream_registry.lock
-rw-------  1 ubuntu ubuntu    5094 May 25 06:35 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu    5099 May 25 06:35 dream_registry.yam
…[truncated 1526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T17:10:43.586726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T17:10:43.587023+00:00_

1	---
2	name: reference-audit
3	description: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。
4	scope: global
5	tags:
6	- workflow
7	- submission
8	- writing
9	- quality
10	priority: 6
11	version: 2
12	roles:
13	- agent
14	- paper_agent
15	- review_reviewer
16	- worker
17	---
18	
19	# 引用验证与审计（Reference Audit）
20	
21	## 核心原则
22	
23	**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。
24	
25	## 触发条件
26	
27	- 写论文时添加引用
28	- Review Reviewer 审查论文引用质量
29	- 提交前最终检查
30	- 发现可疑引用（年份不对、作者不存在、找不到原文）
31	
32	## 验证流程
33	
34	### 1. 单条引用验证（写论文时）
35	
36	每次需要引用时：
37	
38	1. **WebSearch 查找**：搜索论文标题 + 第一作者
39	2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`
40	3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue
41	4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式
42	5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中
43	
44	### 2. 全文引用审计（批量检查）
45	
46	**Step 1：调用 `verify_references(paper_dir)`**
47	
48	这是首选方式。该工具自动完成：
49	- 解析所有 .bib 文件，提取结构化条目
50	- 解析所有 .tex 文件，提取 `\cite{}`/`\citep{}`/`\citet{}` 引用
51	- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）
52	- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）
53	
54	如果只需快速离线检查，传 `skip_online=True`。
55	
56	**Step 2：人工复核工具报告中的问题条目**
57	
58	重点关注：
59	- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证
60	- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本
61	- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错
62	- `orphan_bib` — .bib 中有但正文未引用，清理或补引用
63	
64	**Step 3：语义验证**（优先级排序）
65	1. 首先验证 Introduction 和 Related Work 中的高频引用
66	2. 然后验证 Method 中支撑技术 claim 的引用
67	3. 最后验证其余引用
68	
69	对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。
70	
71	### 3. 验证失败处理
72	
73	**找不到论文时**：
74	1. 检查拼写——标题或作者名是否有误？
75	2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）
76	3. 标记为 `[CITATION NEEDED]`
77	4. 明确告知——说明哪条引用无法验证
78	
79	**信息不匹配时**：
80	1. 确认是否找对了论文
81	2. 检查版本——preprint vs published 版本
82	3. 用最准确的版本更新信息
83	
84	**绝不做的事**：
85	- 从记忆生成 BibTeX——AI 生成引用 40% 错误率
86	- 跳过验证步骤
87	- 假设论文存在
88	- 对无法验证的引用不做标记
…[truncated 888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T17:10:43.587222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T17:10:43.587512+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% Attention Analysis
8	% ============================================================
9	
10	@inproceedings{abnar2020quantifying,
11	  title={Quantifying Attention Flow in Transformers},
12	  author={Abnar, Samira and Zuidema, Willem},
13	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
14	  pages={4190--4197},
15	  year={2020},
16	}
17	
18	% ============================================================
19	% VLA Token Compression (concurrent work)
20	% ============================================================
21	
22	@article{gao2025compressorvla,
23	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
24	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
25	  journal={arXiv preprint arXiv:2511.18950},
26	  year={2025},
27	  eprint={2511.18950},
28	  archivePrefix={arXiv}
29	}
30	
31	@article{wang2025specprunevla,
32	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
33	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
34	  journal={arXiv preprint arXiv:2509.05614},
35	  year={2025},
36	  eprint={2509.05614},
37	  archivePrefix={arXiv}
38	}
39	
40	@inproceedings{jiang2026lightvla,
41	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
42	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
43	  booktitle={Proceedings of the IEEE International Confe
…[truncated 23702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T17:10:43.587671+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T17:10:43.587811+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{0pt}
20	
21	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{abstract}
27	
28	\keywords{vision-language-action models, token pruning, robot learning}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T17:10:43.587971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T17:10:43.588105+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across five VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns ($20{\times}$ from Object to Goal). A zero-mask ablation isolates the mechanism: zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T17:10:43.588282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T17:10:43.588431+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%). Apply the same reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a ViT encoder feeding tokens through a connector into a language model backbone; the critical difference is the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and extends to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture, implicitly assuming pruning transfers across designs.
15	
16	Yet current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.
17	
18	We present an empirical study of VLA 
…[truncated 1579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T17:10:43.588576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T17:10:43.588710+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, and Compressor-VLA~\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Vision connectors.}
11	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T17:10:43.588953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T17:10:43.589118+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-
…[truncated 3154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T17:10:43.589296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T17:10:43.589486+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
8	
9	Four models are evaluated in closed-loop control: $\pi_{0.5}$~\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$, 128 tokens, CV$\,{=}\,$0.314). Two additional models ($\pi_{0}$~\cite{black2024pi0}, OFT~\cite{kim2025openoft}) are analyzed via offline metrics only. Table~\ref{tab:model_properties} summarizes all six architectures. We prune at $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, reporting mean success rate (SR) over 500 episodes.
10	
11	\subsection{Two-Axis Framework Overview}
12	\label{sec:two_axis}
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
17	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
18	\label{fig:pruning_overview}
19	\end{figure}
20	
21	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
22	
23	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. L2 maintains ${\geq}$98.0\% through $k{=}0.85$, while
…[truncated 7861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-28T17:10:43.589637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T17:10:43.589769+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector---L2 leads on $\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\ref{app:extended_discussion}). The V-shaped random recovery on $\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\approx}0.9$, recovering as surviving positions become approximately uniform.
6	
7	Connector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity ($20{\times}$ from Object to Goal). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.
8	
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-28T17:10:43.589938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T17:10:43.590084+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	All evaluations use LIBERO simulation; no sim-to-real evidence is provided. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing full causal isolation of the connector effect. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. Most conditions use a single seed; $\pi_{0.5}$ Long uses five-seed means ($n{=}5$, s.d.\ ${\leq}$2.7\,pp). \textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T17:10:43.590245+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T17:10:43.590439+00:00_

File content (26916 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T17:10:43.590598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-28T17:10:43.590942+00:00_

1	\appendix
2	
3	\section{Full Pruning Results}
4	\label{app:full_results}
5	
6	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
7	
8	\begin{table*}[ht]
9	\centering
10	\footnotesize
11	\caption{Full closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
12	\label{tab:full_results}
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llccccc}
15	\toprule
16	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
17	\midrule
18	\multirow{4}{*}{$\pi_{0.5}$}
19	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
20	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
21	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
22	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
23	\midrule
24	\multirow{4}{*}{X-VLA}
25	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
26	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
27	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
28	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
29	\midrule
30	\multirow{4}{*}{OpenVLA}
31	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
32	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\texts
…[truncated 37517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-28T17:10:43.591098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "500"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-28T17:10:43.591440+00:00_

500	\toprule
501	$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\pm$ Std \\
502	\midrule
503	32 & 61.6 & 59.2 & 59.6 & 60.1 $\pm$ 1.3 \\
504	64 & 61.6 & 60.0 & 64.4 & 62.0 $\pm$ 2.3 \\
505	96 & 52.6 & 58.2 & 52.8 & 54.5 $\pm$ 3.2 \\
506	128 & 59.8 & 54.0 & 60.2 & 58.0 $\pm$ 3.5 \\
507	\bottomrule
508	\end{tabular}
509	\end{table}
510	
511	
512	\section{VTR Full Results}
513	\label{app:vtr_full}
514	
515	\begin{table}[ht]
516	\centering
517	\small
518	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (passthrough) within 1.1\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}
519	\label{tab:vtr_results}
520	\begin{tabular}{lccr}
521	\toprule
522	Configuration & $M$ & Compression & SR (\%) \\
523	\midrule
524	\textit{SmolVLA-Base (LoRA)} & 128 & 0\% & 44.8 \\
525	\textit{SmolVLA official} & 128 & 0\% & 59.2 \\
526	\textit{Baseline control (+100K steps)} & 128 & 0\% & 45.0 \\
527	\textit{Hard pruning (any $k$)} & -- & 5--50\% & 0.0 \\
528	\midrule
529	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
530	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
531	Cross-attn VTR & 64 & 50\% & \textbf{62.0 $\pm$ 2.2} \\
532	Cross-attn VTR & 96 & 25\% & 54.5 $\pm$ 3.2 \\
533	Cross-attn VTR & 128 & 0\% & 58.0 $\pm$ 3.5 \\
534	\midrule
535	MLP adapter ($\sim$22M) & 32 & 75\% & 63.4 $\pm$ 2.6 \\
536	\bottomrule
537	\end{tabular}
538	\end{table}
539	
540	
541	\section{Full VTR Ablation}
542	\label{app:smart_compress_full}
543	
544	Table~\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \in \{32, 64, 128\}$ all achieve $\sim$60\% SR, exceeding the 44.8\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-test). Only at $M = 16$ (87.5
…[truncated 37321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-28T17:10:43.591659+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-28T17:10:43.591849+00:00_

&lt;persisted-output>
Output too large (20.9KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/d2069fe8-704e-4de3-95db-332caead068e/tool-results/toolu_01MiARPrYdXdYiQqC94RZC3L.txt

Preview (first 2KB):
docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
docs/paper/related_work.tex:8:[Omitted long matching line]
docs/paper/related_work.tex:11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
docs/paper/experiments.tex:7:We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
docs/paper/experiments.tex:9:[Omitted long matching line]
docs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
docs/paper/background.tex:12:SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organ
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-28T17:10:43.591994+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\nocite",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\nocite",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T17:10:43.592122+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-28T17:10:43.592264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/d2069fe8-704e-4de3-95db-332caead068e/tool-results/toolu_01MiARPrYdXdYiQqC94RZC3L.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/d2069fe8-704e-4de3-95db-332caead068e/tool-results/toolu_01MiARPrYdXdYiQqC94RZC3L.txt"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T17:10:43.592481+00:00_

1	docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
2	docs/paper/related_work.tex:8:[Omitted long matching line]
3	docs/paper/related_work.tex:11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
4	docs/paper/experiments.tex:7:We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
5	docs/paper/experiments.tex:9:[Omitted long matching line]
6	docs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
7	docs/paper/background.tex:12:SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
8	docs/paper/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
9	docs/paper/background.tex:36:The Qwen2
…[truncated 19659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-28T17:10:43.592694+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-28T17:10:43.592824+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-28T17:10:43.592962+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Token Merging Your ViT But Faster Bolya ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Token Merging Your ViT But Faster Bolya ICLR 2023"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-28T17:10:43.593080+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA Open-Source Vision-Language-Action Model Kim Pertsch Karamcheti CoRL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA Open-Source Vision-Language-Action Model Kim Pertsch Karamcheti CoRL 2024"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-28T17:10:43.593216+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi 0.5 Vision-Language-Action Model Open-World Generalization Black Brown 2025 arXiv 2504.16054"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi 0.5 Vision-Language-Action Model Open-World Generalization Black Brown 2025 arXiv 2504.16054"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-28T17:10:43.593339+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA Soft-Prompted Transformer Scalable Cross-Embodiment Zheng ICLR 2026 arXiv 2510.10274"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA Soft-Prompted Transformer Scalable Cross-Embodiment Zheng ICLR 2026 arXiv 2510.10274"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-28T17:10:43.593450+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA Vision-Language-Action Model Affordable Efficient Robotics Shukor 2025 arXiv 2506.01844"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA Vision-Language-Action Model Affordable Efficient Robotics Shukor 2025 arXiv 2506.01844"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-28T17:10:43.593588+00:00_

Web search results for query: "Token Merging Your ViT But Faster Bolya ICLR 2023"

Links: [{"title":"Token Merging: Your ViT but Faster","url":"https://github.com/facebookresearch/ToMe"},{"title":"Token Merging: Your ViT But Faster | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2be6dab5547a2706612e5e346ab0b2fe9/hassanpour71"},{"title":"Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER","url":"https://arxiv.org/pdf/2210.09461"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv-export1.library.cornell.edu/abs/2210.09461"},{"title":"Representation Learning Breakthroughs Every ML Engineer Should Know: Token Merging: Your ViT, but Faster | by Ruben Broekx | Superlinear | Medium","url":"https://medium.com/superlinear-eu-blog/representation-learning-breakthroughs-token-merging-your-vit-but-faster-e3f88f25d6d1"},{"title":"Token Merging: Your ViT But Faster | OpenReview","url":"https://openreview.net/forum?id=JroZRaRw7Eu"},{"title":"ICLR Oral Token Merging: Your ViT But Faster","url":"https://iclr.cc/virtual/2023/oral/12533"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv.org/abs/2210.09461"},{"title":"dbolya/tomesd - Token Merging for Stable Diffusion","url":"https://github.com/dbolya/tomesd"},{"title":"Training-Free Acceleration of ViTs with Delayed Spatial Merging","url":"https://arxiv.org/pdf/2303.02331"}]

Based on the search results, here's what I found about "Token Merging: Your ViT But Faster":

## Overview

This is a paper by Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenhofer, and Judy Hoffman, published at ICLR 2023.

## Key Innovation

The paper introduces Token Merging (ToMe), a simple method to increase the throughput of existing ViT models without needing to train. ToMe gradually combines similar tokens in a transformer using a general and light-weight matching algorithm that is as fast as pruning while being more accurate.

## Perf
…[truncated 672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-28T17:10:43.593755+00:00_

Web search results for query: "OpenVLA Open-Source Vision-Language-Action Model Kim Pertsch Karamcheti CoRL 2024"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"}]

Based on the search results, here's what I found about OpenVLA:

## Overview

OpenVLA is an open-source vision-language-action model developed by Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, and other researchers from Stanford University, UC Berkeley, Toyota Research Institute, Google DeepMind, Physical Intelligence, and MIT. The paper was published in the Proceedings of The 8th Conference on Robot Learning (CoRL 2025).

## Training and Data

The model was trained on a curated dataset of 970k robot manipulation trajectories from the Open X-Embodiment (OpenX) dataset. 
…[truncated 741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-28T17:10:43.593926+00:00_

Web search results for query: "pi 0.5 Vision-Language-Action Model Open-World Generalization Black Brown 2025 arXiv 2504.16054"

Links: [{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"},{"title":"[2504.16054v1] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054v1"},{"title":"$\\pi_0.5$: a Vision-Language-Action Model with Open-World Generalization","url":"https://proceedings.mlr.press/v305/black25a.html"},{"title":"[PDF] π0.5: a Vision-Language-Action Model with Open-World Generalization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/%CF%800.5:-a-Vision-Language-Action-Model-with-Intelligence-Black/1e2a82ef5e0325a26ca0344c4f8c256c52fae7ec"},{"title":"π0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/pdf/2504.16054"},{"title":"(PDF) \\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.researchgate.net/publication/391019295_pi_05_a_Vision-Language-Action_Model_with_Open-World_Generalization"},{"title":"$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.emergentmind.com/papers/2504.16054"},{"title":"$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250416054I/abstract"},{"title":"Paper page - π_{0.5}: a Vision-Language-Action Model with Open-World Generalization","url":"https://huggingface.co/papers/2504.16054"}]

Based on the search results, I found the paper you're looking for:

π₀.₅ is a Vision-Language-Action Model with Open-World Generalization, submitted to arXiv on April 22, 2025 (arXiv:2504.16054), authored by researchers from Physical Intelligence including Kevin Black and Noah Brown, among 35 other authors.

π₀.₅ is a new model based on π₀ that uses co-training on heterogeneous tasks to 
…[truncated 617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T17:10:43.594096+00:00_

Web search results for query: "SmolVLA Vision-Language-Action Model Affordable Efficient Robotics Shukor 2025 arXiv 2506.01844"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"[2506.01844v1] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844v1"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"}]

I found the research paper you're looking for! Here's what I found:

SmolVLA is a small, efficient, and community-driven vision-language-action (VLA) model that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.

The paper addresses a key problem in robotics research: existi
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T17:10:43.594296+00:00_

Web search results for query: "X-VLA Soft-Prompted Transformer Scalable Cross-Embodiment Zheng ICLR 2026 arXiv 2510.10274"

Links: [{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model [Quick Review]","url":"https://liner.com/review/xvla-softprompted-transformer-as-scalable-crossembodiment-visionlanguageaction-model"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"[PDF] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/X-VLA:-Soft-Prompted-Transformer-as-Scalable-Model-Zheng-Li/9855c60d2ecdcf7edc4622ecd004f0db147fc22b"},{"title":"X-VLA/evaluation/robotwin-2.0/README.md at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/evaluation/robotwin-2.0/README.md"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=kt51kZH4aG"},{"title":"ICLR Poster X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://iclr.cc/virtual/2026/poster/10007740"},{"title":"X-VLA/evaluation/calvin/README.md at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/evaluation/calvin/README.md"},{"title":"[2510.10274] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/abs/2510.10274"},{"title":"(PDF) X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://www.researchgate.net/publication/396462440_X-VLA_Soft-Prompted_Transformer_as_Scalable_Cross-Embodiment_Vision-Language-Action_Model"}]

I found comprehensive information about the X-VLA paper. Here's what I discovered:

#
…[truncated 1686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-28T17:10:43.594540+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LightVLA \"The Better You Learn The Smarter You Prune\" differentiable token pruning VLA ICRA arXiv 2509.12594"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LightVLA \"The Better You Learn The Smarter You Prune\" differentiable token pruning VLA ICRA arXiv 2509.12594"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-28T17:10:43.594685+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FastV \"Image is Worth 1/2 Tokens After Layer 2\" Chen ECCV 2024 visual token pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FastV \"Image is Worth 1/2 Tokens After Layer 2\" Chen ECCV 2024 visual token pruning"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-28T17:10:43.594834+00:00_

Web search results for query: "LightVLA "The Better You Learn The Smarter You Prune" differentiable token pruning VLA ICRA arXiv 2509.12594"

Links: [{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"AI Bites | YouTube Channel on X: \"LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by https://t.co/bE0Zv0mb0c\" / X","url":"https://x.com/ai_bites/status/1970481721163313156"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"}]

I found detailed information about LightVLA from arXiv 2509.12594. Here's a summary:

## LightVLA: Eff
…[truncated 1552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-28T17:10:43.595007+00:00_

Web search results for query: "FastV "Image is Worth 1/2 Tokens After Layer 2" Chen ECCV 2024 visual token pruning"

Links: [{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"GitHub - MachineLearningSystem/24ECCV-FastV: [ECCV 2024] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/MachineLearningSystem/24ECCV-FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-73004-7_2"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"},{"title":"ECCV Poster An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://eccv.ecva.net/virtual/2024/poster/2009"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"}]

I found comprehensive information about the FastV paper. Here's what the search revealed:

## FastV: An Im
…[truncated 1357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-28T17:10:43.595218+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-28T17:10:43.595355+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-28T17:10:43.595498+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/reference_audit_report.md",
  "content": "# Reference Audit Report\n\n**Paper**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility\"\n**Target**: CoRL 2026\n**Audit date**: 2026-05-28\n**Bib file**: `docs/paper/references.bib`\n**Compiled tex files**: main.tex → abstract, introduction, related_work, method, experiments, conclusion, limitations, appendix\n\n---\n\n## Summary Statistics\n\n| Metric | Count |\n|--------|-------|\n| Total bib entries | 62 |\n| Unique citations in compiled paper | 26 |\n| Missing citations (cited but no bib) | 0 |\n| Orphan bib entries (bib but not cited) | 36 |\n| Incomplete entries (cited) | 1 |\n| Author errors (cited) | 1 |\n| Venue updates needed | 1 |\n\n---\n\n## Verdict: CONDITIONAL PASS\n\nOne critical author error (`zheng2025xvla`) must be fixed before submission. One incomplete author list (`chen2024fastv`) and one outdated venue (`black2025pi05`) should also be corrected.\n\n---\n\n## Critical Issues\n\n### 1. [critical] `zheng2025xvla` — Wrong first author name\n\n- **Bib says**: `Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others`\n- **Actual** (per arXiv, GitHub, OpenReview, ICLR 2026 page): `Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and ...`\n- **Action**: Replace first author \"Yifu\" → \"Jinliang\"; reorder remaining authors to match the published version.\n\n---\n\n## Warnings\n\n### 2. [warning] `chen2024fastv` — Incomplete author list\n\n- **Bib says**: `Chen, Liang and others` (1 author + \"others\")\n- **Actual** (per arXiv 2403.06764, ECCV 2024): Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao\n- **Action**: Expand to at least first 3 authors.\n\n### 3. [warning] `black2025pi05` — Venue outdated (arXiv → CoRL 2025)\n\n- **Bib says**: `@article{...} journal={arXiv preprint arXiv:2504.16054}, year={2025}`\n- **Actual** (per PMLR v305): Published as conference paper at The 9th Conference on Robot Learning (CoRL), 2025.\n- **Action**: Update to `@inproceedings` with `booktitle={Proceedings of the 9th Conference on Robot Learning (CoRL)}`.\n\n### 4. [warning] 36 orphan bib entries\n\nThe following 36 entries exist in `references.bib` but are never cited in the compiled paper. They inflate the bib file and may confuse reviewers if `\\nocite{*}` is accidentally enabled.\n\n| # | Key | Title (abbrev) |\n|---|-----|----------------|\n| 1 | wang2025specprunevla | SpecPrune-VLA |\n| 2 | feng2026seewhatmatters | See What Matters (ICML 2026) |\n| 3 | zhang2025sparsevlm | SparseVLM |\n| 4 | khaki2025sparsevila | SparseVILA |\n| 5 | jabbour2025dontrun | Don't Run with Scissors |\n| 6 | li2024roboflamingo | RoboFlamingo |\n| 7 | brohan2023rt2 | RT-2 (Brohan) |\n| 8 | ghosh2024octo | Octo |\n| 9 | brohan2023rt1 | RT-1 |\n| 10 | alayrac2022flamingo | Flamingo |\n| 11 | chen2024internvl | InternVL |\n| 12 | jaegle2021perceiver | Perceiver |\n| 13 | oquab2023dinov2 | DINOv2 (2023 entry) |\n| 14 | zhai2023siglip | SigLIP |\n| 15 | yang2024qwen2 | Qwen2 |\n| 16 | lipman2023flow | Flow Matching |\n| 17 | li2024tokenpacker | TokenPacker |\n| 18 | wen2024tinyvla | TinyVLA |\n| 19 | ryoo2021tokenlearner | TokenLearner |\n| 20 | meng2022adavit | AdaViT |\n| 21 | chen2023sparsevit | SparseViT |\n| 22 | ye2025fitprune | Fit and Prune |\n| 23 | shi2024crossget | CrossGET |\n| 24 | zhang2024fastervlm | [CLS] Attention FasterVLM |\n| 25 | liu2024llava15 | LLaVA-1.5 |\n| 26 | chen2024internvl25 | InternVL 2.5 |\n| 27 | gao2024miniinternvl | Mini-InternVL |\n| 28 | zitkovich2023rt2 | RT-2 (Zitkovich) |\n| 29 | openxembodiment2024 | Open X-Embodiment |\n| 30 | zhang2023h2o | H2O |\n| 31 | xiao2024streamingllm | StreamingLLM |\n| 32 | mees2022calvin | CALVIN |\n| 33 | chi2023diffusionpolicy | Diffusion Policy |\n| 34 | zeng2023transformers_tsf | Are Transformers Effective for TSF |\n| 35 | bouthillier2024negative | Embracing Negative Results |\n| 36 | oquab2024dinov2 | DINOv2 (2024 entry) |\n\n**Note**: Some orphans (SigLIP, Qwen2, Flow Matching, DINOv2) are cited in non-compiled draft files (`background.tex`, `sections/introduction.tex`). If those sections were previously part of the paper, the references may have been left behind after restructuring.\n\n**Action**: Either cite these in the compiled paper or remove from `references.bib`.\n\n---\n\n## Info\n\n### 5. [info] Venue format inconsistency\n\nMinor inconsistency in booktitle formatting among cited entries:\n\n- **With \"Proceedings of...\" prefix**: `abnar2020quantifying` (\"Proceedings of the 58th Annual Meeting of the ACL\"), `jiang2026lightvla` (\"Proceedings of the IEEE...ICRA\"), `kim2024openvla` (\"Proceedings of the 8th CoRL\")\n- **Without prefix**: `bolya2023tome` (\"International Conference on Learning Representations (ICLR)\"), `chen2024fastv` (\"European Conference on Computer Vision (ECCV)\"), `rao2021dynamicvit` (\"Advances in Neural Information Processing Systems (NeurIPS)\")\n\nThis is cosmetic and depends on the bibliography style (`corlabbrvnat.bst`), but standardizing would be cleaner.\n\n### 6. [info] Duplicate orphan entries\n\n- `oquab2023dinov2` and `oquab2024dinov2` — same DINOv2 paper, different years (2023 as article vs 2024 as TMLR). Neither is cited.\n- `brohan2023rt2` and `zitkovich2023rt2` — same RT-2 paper, different first authors. Neither is cited.\n\n**Action**: Remove duplicates if cleaning orphans.\n\n---\n\n## Truthfulness Verification (7 references checked)\n\n| Key | Title match | Author match | Year match | Venue match | Status |\n|-----|-------------|--------------|------------|-------------|--------|\n| bolya2023tome | ✅ | ✅ | ✅ 2023 | ✅ ICLR 2023 (Oral) | **Verified** |\n| kim2024openvla | ✅ | ✅ | ✅ 2024 | ✅ CoRL 2024 | **Verified** |\n| black2025pi05 | ✅ | ✅ | ✅ 2025 | ⚠️ Now CoRL 2025, bib says arXiv | **Outdated venue** |\n| zheng2025xvla | ✅ | ❌ First author wrong | ✅ 2026 | ✅ ICLR 2026 | **Author error** |\n| shukor2025smolvla | ✅ | ✅ | ✅ 2025 | ✅ arXiv 2506.01844 | **Verified** |\n| jiang2026lightvla | ✅ | ✅ | ✅ 2026 | ✅ ICRA 2026 | **Verified** |\n| chen2024fastv | ✅ | ⚠️ Only 1/7 authors | ✅ 2024 | ✅ ECCV 2024 (Oral) | **Incomplete** |\n\nNo hallucinated citations detected. All 7 checked references correspond to real, published papers.\n\n---\n\n## Complete List of Cited References (26)\n\n| # | Key | Section(s) |\n|---|-----|-----------|\n| 1 | abnar2020quantifying | appendix |\n| 2 | black2024pi0 | introduction, method, experiments |\n| 3 | black2025pi05 | method, experiments |\n| 4 | bolya2023tome | introduction, related_work, appendix |\n| 5 | chen2024fastv | related_work |\n| 6 | cheng2026vlaiap | introduction, related_work |\n| 7 | gao2025compressorvla | related_work |\n| 8 | jiang2026lightvla | related_work |\n| 9 | kim2024openvla | introduction, method, experiments |\n| 10 | kim2025openoft | method, experiments |\n| 11 | lewis2020bart | method, appendix |\n| 12 | li2023blip2 | related_work |\n| 13 | li2024cogact | appendix |\n| 14 | liang2022evit | introduction, related_work |\n| 15 | liu2023libero | method, experiments |\n| 16 | liu2023llava | related_work |\n| 17 | liu2025vlapruner | introduction, related_work |\n| 18 | rao2021dynamicvit | introduction, related_work |\n| 19 | shang2024prumerge | related_work |\n| 20 | shi2016subpixel | related_work |\n| 21 | shukor2025smolvla | introduction, method, experiments |\n| 22 | su2024roformer | appendix |\n| 23 | xu2025vlacache | introduction, related_work |\n| 24 | yang2025efficientvla | introduction, related_work |\n| 25 | yin2022avit | related_work |\n| 26 | zheng2025xvla | introduction, method, experiments |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/reference_audit_report.md",
    "content": "# Reference Audit Report\n\n**Paper**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility\"\n**Target**: CoRL 2026\n**Audit date**: 2026-05-28\n**Bib file**: `docs/paper/references.bib`\n**Compiled tex files**: main.tex → abstract, introduction, related_work, method, experiments, conclusion, limitations, appendix\n\n---\n\n## Summary Statistics\n\n| Metric | Count |\n|--------|-------|\n| Total bib entries | 62 |\n| Unique citations in compiled paper | 26 |\n| Missing citations (cited but no bib) | 0 |\n| Orphan bib entries (bib but not cited) | 36 |\n| Incomplete entries (cited) | 1 |\n| Author errors (cited) | 1 |\n| Venue updates needed | 1 |\n\n---\n\n## Verdict: CONDITIONAL PASS\n\nOne critical author error (`zheng2025xvla`) must be fixed before submission. One incomplete author list (`chen2024fastv`) and one outdated venue (`black2025pi05`) should also be corrected.\n\n---\n\n## Critical Issues\n\n### 1. [critical] `zheng2025xvla` — Wrong first author name\n\n- **Bib says**: `Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others`\n- **Actual** (per arXiv, GitHub, OpenReview, ICLR 2026 page): `Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and ...`\n- **Action**: Replace first author \"Yifu\" → \"Jinliang\"; reorder remaining authors to match the published version.\n\n---\n\n## Warnings\n\n### 2. [warning] `chen2024fastv` — Incomplete author list\n\n- **Bib says**: `Chen, Liang and others` (1 author + \"others\")\n- **Actual** (per arXiv 2403.06764, ECCV 2024): Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao\n- **Action**: Expand to at least first 3 authors.\n\n### 3. [warning] `black2025pi05` — Venue outdated (arXiv → CoRL 2025)\n\n- **Bib says**: `@article{...} journal={arXiv preprint arXiv:2504.16054}, year={2025}`\n- **Actual** (per PMLR v305): Published as conference paper at The 9th Conference on Robot Learning (CoRL), 2025.\n- **Action**: Update to `@inproceedings` with `booktitle={Proceedings of the 9th Conference on Robot Learning (CoRL)}`.\n\n### 4. [warning] 36 orphan bib entries\n\nThe following 36 entries exist in `references.bib` but are never cited in the compiled paper. They inflate the bib file and may confuse reviewers if `\\nocite{*}` is accidentally enabled.\n\n| # | Key | Title (abbrev) |\n|---|-----|----------------|\n| 1 | wang2025specprunevla | SpecPrune-VLA |\n| 2 | feng2026seewhatmatters | See What Matters (ICML 2026) |\n| 3 | zhang2025sparsevlm | SparseVLM |\n| 4 | khaki2025sparsevila | SparseVILA |\n| 5 | jabbour2025dontrun | Don't Run with Scissors |\n| 6 | li2024roboflamingo | RoboFlamingo |\n| 7 | brohan2023rt2 | RT-2 (Brohan) |\n| 8 | ghosh2024octo | Octo |\n| 9 | brohan2023rt1 | RT-1 |\n| 10 | alayrac2022flamingo | Flamingo |\n| 11 | chen2024internvl | InternVL |\n| 12 | jaegle2021perceiver | Perceiver |\n| 13 | oquab2023dinov2 | DINOv2 (2023 entry) |\n| 14 | zhai2023siglip | SigLIP |\n| 15 | yang2024qwen2 | Qwen2 |\n| 16 | lipman2023flow | Flow Matching |\n| 17 | li2024tokenpacker | TokenPacker |\n| 18 | wen2024tinyvla | TinyVLA |\n| 19 | ryoo2021tokenlearner | TokenLearner |\n| 20 | meng2022adavit | AdaViT |\n| 21 | chen2023sparsevit | SparseViT |\n| 22 | ye2025fitprune | Fit and Prune |\n| 23 | shi2024crossget | CrossGET |\n| 24 | zhang2024fastervlm | [CLS] Attention FasterVLM |\n| 25 | liu2024llava15 | LLaVA-1.5 |\n| 26 | chen2024internvl25 | InternVL 2.5 |\n| 27 | gao2024miniinternvl | Mini-InternVL |\n| 28 | zitkovich2023rt2 | RT-2 (Zitkovich) |\n| 29 | openxembodiment2024 | Open X-Embodiment |\n| 30 | zhang2023h2o | H2O |\n| 31 | xiao2024streamingllm | StreamingLLM |\n| 32 | mees2022calvin | CALVIN |\n| 33 | chi2023diffusionpolicy | Diffusion Policy |\n| 34 | zeng2023transformers_tsf | Are Transformers Effective for TSF |\n| 35 | bouthillier2024negative | Embracing Negative Results |\n| 36 | oquab2024dinov2 | DINOv2 (2024 entry) |\n\n**Note**: Some orphans (SigLIP, Qwen2, Flow Matching, DINOv2) are cited in non-compiled draft files (`background.tex`, `sections/introduction.tex`). If those sections were previously part of the paper, the references may have been left behind after restructuring.\n\n**Action**: Either cite these in the compiled paper or remove from `references.bib`.\n\n---\n\n## Info\n\n### 5. [info] Venue format inconsistency\n\nMinor inconsistency in booktitle formatting among cited entries:\n\n- **With \"Proceedings of...\" prefix**: `abnar2020quantifying` (\"Proceedings of the 58th Annual Meeting of the ACL\"), `jiang2026lightvla` (\"Proceedings of the IEEE...ICRA\"), `kim2024openvla` (\"Proceedings of the 8th CoRL\")\n- **Without prefix**: `bolya2023tome` (\"International Conference on Learning Representations (ICLR)\"), `chen2024fastv` (\"European Conference on Computer Vision (ECCV)\"), `rao2021dynamicvit` (\"Advances in Neural Information Processing Systems (NeurIPS)\")\n\nThis is cosmetic and depends on the bibliography style (`corlabbrvnat.bst`), but standardizing would be cleaner.\n\n### 6. [info] Duplicate orphan entries\n\n- `oquab2023dinov2` and `oquab2024dinov2` — same DINOv2 paper, different years (2023 as article vs 2024 as TMLR). Neither is cited.\n- `brohan2023rt2` and `zitkovich2023rt2` — same RT-2 paper, different first authors. Neither is cited.\n\n**Action**: Remove duplicates if cleaning orphans.\n\n---\n\n## Truthfulness Verification (7 references checked)\n\n| Key | Title match | Author match | Year match | Venue match | Status |\n|-----|-------------|--------------|------------|-------------|--------|\n| bolya2023tome | ✅ | ✅ | ✅ 2023 | ✅ ICLR 2023 (Oral) | **Verified** |\n| kim2024openvla | ✅ | ✅ | ✅ 2024 | ✅ CoRL 2024 | **Verified** |\n| black2025pi05 | ✅ | ✅ | ✅ 2025 | ⚠️ Now CoRL 2025, bib says arXiv | **Outdated venue** |\n| zheng2025xvla | ✅ | ❌ First author wrong | ✅ 2026 | ✅ ICLR 2026 | **Author error** |\n| shukor2025smolvla | ✅ | ✅ | ✅ 2025 | ✅ arXiv 2506.01844 | **Verified** |\n| jiang2026lightvla | ✅ | ✅ | ✅ 2026 | ✅ ICRA 2026 | **Verified** |\n| chen2024fastv | ✅ | ⚠️ Only 1/7 authors | ✅ 2024 | ✅ ECCV 2024 (Oral) | **Incomplete** |\n\nNo hallucinated citations detected. All 7 checked references correspond to real, published papers.\n\n---\n\n## Complete List of Cited References (26)\n\n| # | Key | Section(s) |\n|---|-----|-----------|\n| 1 | abnar2020quantifying | appendix |\n| 2 | black2024pi0 | introduction, method, experiments |\n| 3 | black2025pi05 | method, experiments |\n| 4 | bolya2023tome | introduction, related_work, appendix |\n| 5 | chen2024fastv | related_work |\n| 6 | cheng2026vlaiap | introduction, related_work |\n| 7 | gao2025compressorvla | related_work |\n| 8 | jiang2026lightvla | related_work |\n| 9 | kim2024openvla | introduction, method, experiments |\n| 10 | kim2025openoft | method, experiments |\n| 11 | lewis2020bart | method, appendix |\n| 12 | li2023blip2 | related_work |\n| 13 | li2024cogact | appendix |\n| 14 | liang2022evit | introduction, related_work |\n| 15 | liu2023libero | method, experiments |\n| 16 | liu2023llava | related_work |\n| 17 | liu2025vlapruner | introduction, related_work |\n| 18 | rao2021dynamicvit | introduction, related_work |\n| 19 | shang2024prumerge | related_work |\n| 20 | shi2016subpixel | related_work |\n| 21 | shukor2025smolvla | introduction, method, experiments |\n| 22 | su2024roformer | appendix |\n| 23 | xu2025vlacache | introduction, related_work |\n| 24 | yang2025efficientvla | introduction, related_work |\n| 25 | yin2022avit | related_work |\n| 26 | zheng2025xvla | introduction, method, experiments |\n"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-28T17:10:43.595724+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/reference_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-28T17:10:43.595853+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reference_audit_report",
  "type": "report",
  "description": "CoRL 2026 submission reference audit: 62 bib entries, 26 cited, 36 orphans. 1 critical author error (zheng2025xvla), 1 incomplete author list (chen2024fastv), 1 outdated venue (black2025pi05). 7 references truth-checked, no hallucinations found. Verdict: CONDITIONAL PASS.",
  "project": "importance_margin_vla_compress",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/reference_audit_report.md",
  "tags": "['reference-audit', 'submission', 'corl2026']",
  "skill": "reference-audit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reference_audit_report",
    "type": "report",
    "description": "CoRL 2026 submission reference audit: 62 bib entries, 26 cited, 36 orphans. 1 critical author error (zheng2025xvla), 1 incomplete author list (chen2024fastv), 1 outdated venue (black2025pi05). 7 references truth-checked, no hallucinations found. Verdict: CONDITIONAL PASS.",
    "project": "importance_margin_vla_compress",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/reference_audit_report.md",
    "tags": "['reference-audit', 'submission', 'corl2026']",
    "skill": "reference-audit"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-28T17:10:43.596010+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260528_e705eb\", \"name\": \"reference_audit_report\", \"type\": \"report\", \"description\": \"CoRL 2026 submission reference audit: 62 bib entries, 26 cited, 36 orphans. 1 critical author error (zheng2025xvla), 1 incomplete author list (chen2024fastv), 1 outdated venue (black2025pi05). 7 references truth-checked, no hallucinations found. Verdict: CONDITIONAL PASS.\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/report/reference_audit_report.md\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"reference-audit\", \"created_at\": \"2026-05-28T17:10:35.659253+00:00\", \"tags\": [\"reference-audit\", \"submission\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_audit_submission_20260528T170501",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-28T17:10:43.596250+00:00_

**审计结果：CONDITIONAL PASS**

62 条 bib 条目，26 条被编译论文引用，36 条 orphan。无幻觉引用，无缺失引用。

须修复的问题：

1. **[critical] `zheng2025xvla`** — 第一作者名错误：bib 写 "Yifu Zheng"，实际为 "Jinliang Zheng"（已通过 arXiv、GitHub、ICLR 2026 页面确认）
2. **[warning] `chen2024fastv`** — 作者列表不完整，仅列 1/7 位作者
3. **[warning] `black2025pi05`** — 已在 CoRL 2025 发表（PMLR 305），bib 仍标记为 arXiv preprint
4. **[warning] 36 条 orphan 条目** — 未被引用，建议清理或补引用

报告已写入 `artifacts/reference_audit_report.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_reference_audit_submission_20260528T170501"
}
```

</details>

---
