# research reference audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 0
- **Tool calls:** 36
- **Original source:** `logs/chats/worker_research_reference_audit_20260514T185731.jsonl`
- **Structured JSON:** [`9aceec40c242468b696e.json`](../../sessions/9a/9aceec40c242468b696e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

73 recorded events

### Tool call

_source line 1 · 2026-05-14T19:02:02.382903+00:00_

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
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T19:02:02.383514+00:00_

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
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T19:02:02.383708+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T19:02:02.383888+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T19:02:02.384023+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,WebSearch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,WebSearch",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T19:02:02.384147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T19:02:02.384292+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T19:02:02.384526+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 (D056 c5b gate_failed→future work; c3_llama success→C8 confirmed) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。C3 crossover 现象的 LLaMA 架构验证已完成（c3_llama）：qualitative direction consistent（importance phase gradient d_z~1.0），但 strategy × phase 交互弱于 Qwen2 架构，random eviction 在 LLaMA 上也显示非平凡 phase gradient（D060）。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-str
…[truncated 8996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T19:02:02.384702+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:02:02.384831+00:00_

artifacts/_project/paper/methodology.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:02:02.384953+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T19:02:02.385067+00:00_

artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T19:02:02.385207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:02:02.385398+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{compression-ordering-2025,
13	    title   = {A Systematic Study of Compression Ordering for Large Language Models},
14	    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},
15	    journal = {arXiv preprint arXiv:2511.19495},
16	    year    = {2025},
17	    url     = {https://arxiv.org/abs/2511.19495},
18	}
19	
20	@article{decision-repr-transition-2026,
21	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
22	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
23	    journal = {arXiv preprint arXiv:2605.07271},
24	    year    = {2026},
25	    url     = {https://arxiv.org/abs/2605.07271},
26	}
27	
28	@article{deepseek-r1-2025,
29	    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},
30	    author  = {{DeepSeek-AI}},
31	    journal = {Nature},
32	    volume  = {645},
33	    pages   = {633--638},
34	    year    = {2025},
35	    doi     = {10.1038/s41586-025-08636-z},
36	}
37	
38	@inproceedings{defensivekv-iclr2026,
39	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
40	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
41	    booktitle = {International Conference on Learning Representations},
42	    year      = {2026},
43	    url       = {https://arxiv.org/abs/2510.13334
…[truncated 11353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T19:02:02.385576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T19:02:02.385708+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{background}
34	\input{methodology}
35	\input{results}
36	\input{analysis}
37	\input{discussion}
38	\input{conclusion}
39	
40	\bibliography{references}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\appendix
46	\input{appendix}
47	\input{appendix_moved}
48	\input{appendix_disc_analysis}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T19:02:02.385859+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T19:02:02.385998+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T19:02:02.386141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T19:02:02.386283+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 1823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T19:02:02.386436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T19:02:02.386583+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	Lethe~\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.
18	These methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mech
…[truncated 726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T19:02:02.386726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T19:02:02.386870+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T19:02:02.387012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T19:02:02.387145+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All confidence intervals and significance tests use 
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T19:02:02.387374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T19:02:02.387687+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{
…[truncated 7921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T19:02:02.387937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T19:02:02.388149+00:00_

1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T19:02:02.388349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T19:02:02.388573+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability. Extended discussion in Appendix~\ref{app:extended-discussion}.
9	
10	\paragraph{Architecture-dependent magnitude.}
11	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) confirms the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---while revealing that
…[truncated 465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T19:02:02.388783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T19:02:02.388966+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with consistent qualitative trend at $\sim$1/40 the magnitude. Discrimination collapse provides a robust mechanistic explanation confirmed across both models.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T19:02:02.389355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T19:02:02.389569+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) extends the findings beyond the Qwen2 architecture, but the qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T19:02:02.389764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T19:02:02.389971+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T19:02:02.390178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T19:02:02.390502+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 11098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T19:02:02.390726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T19:02:02.390986+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architectu
…[truncated 6354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T19:02:02.391209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T19:02:02.391400+00:00_

1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T19:02:02.391711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparK Query-Aware Unstructured Sparsity Recoverable KV Cache Channel Pruning arxiv 2508.15212"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparK Query-Aware Unstructured Sparsity Recoverable KV Cache Channel Pruning arxiv 2508.15212"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T19:02:02.391914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ThinKV Thought-Adaptive KV Cache Compression Efficient Reasoning Models arxiv 2510.01290"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ThinKV Thought-Adaptive KV Cache Compression Efficient Reasoning Models arxiv 2510.01290"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T19:02:02.396473+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-R1 Incentivizing Reasoning Capability LLMs Reinforcement Learning Nature 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-R1 Incentivizing Reasoning Capability LLMs Reinforcement Learning Nature 2025"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T19:02:02.396663+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lethe Layer Time Adaptive KV Cache Pruning Reasoning-Intensive LLM Serving AAAI 2026 arxiv 2511.06029"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lethe Layer Time Adaptive KV Cache Pruning Reasoning-Intensive LLM Serving AAAI 2026 arxiv 2511.06029"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T19:02:02.396818+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Phase transitions in large language model compression\" npj Artificial Intelligence 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Phase transitions in large language model compression\" npj Artificial Intelligence 2026"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T19:02:02.396941+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RetentiveKV State-Space Memory Uncertainty-Aware Multimodal KV Cache Eviction arxiv 2605.04075"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RetentiveKV State-Space Memory Uncertainty-Aware Multimodal KV Cache Eviction arxiv 2605.04075"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T19:02:02.397058+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRASPrune Global Gating Budgeted Structured Pruning LLM arxiv 2604.19398 ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRASPrune Global Gating Budgeted Structured Pruning LLM arxiv 2604.19398 ACL 2026"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T19:02:02.397170+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyramidKV Dynamic KV Cache Compression Pyramidal Information Funneling 2406.02069 published venue 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyramidKV Dynamic KV Cache Compression Pyramidal Information Funneling 2406.02069 published venue 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T19:02:02.397333+00:00_

Web search results for query: "SparK Query-Aware Unstructured Sparsity Recoverable KV Cache Channel Pruning arxiv 2508.15212"

Links: [{"title":"[2508.15212] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/abs/2508.15212"},{"title":"SPARK: Query-Aware Unstructured Sparsity with","url":"https://arxiv.org/pdf/2508.15212"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/html/2508.15212"},{"title":"GitHub - Xnhyacinth/SparK: [AAAI 2026] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://github.com/Xnhyacinth/SparK"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning - haebom","url":"https://haebom.dev/daily_arxiv?tl=en&post=dk58wg2e67jr3mnqevxz"},{"title":"Computation and Language 2025","url":"https://www.arxiv.org/list/cs.CL/2025?skip=11125&show=2000"},{"title":"Learnable Permutation for Structured Sparsity on Transformer Models","url":"https://arxiv.org/html/2601.22980v1"},{"title":"[Literature Review] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://www.themoonlight.io/en/review/spark-query-aware-unstructured-sparsity-with-recoverable-kv-cache-channel-pruning"},{"title":"PocketLLM: Ultimate Compression of Large Language Models via Meta Networks","url":"https://arxiv.org/html/2511.17637v1"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=7650&show=25"}]

I found the paper! Here's what I discovered:

## SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning

Long-context inference in large language models (LLMs) is increasingly constrained by the KV cache bottleneck: memory usage grows linearly with sequence length, while attention computation scales quadratically.

### Key Contribution

SparK is a training-free plug-and-play method tha
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T19:02:02.397594+00:00_

Web search results for query: "ThinKV Thought-Adaptive KV Cache Compression Efficient Reasoning Models arxiv 2510.01290"

Links: [{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.01290"},{"title":"THINKV: THOUGHT-ADAPTIVE KV CACHE COM- PRESSION FOR EFFICIENT REASONING MODELS","url":"https://arxiv.org/pdf/2510.01290v1"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/new?skip=75&show=250"},{"title":"(PDF) ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://www.researchgate.net/publication/396142746_ThinKV_Thought-Adaptive_KV_Cache_Compression_for_Efficient_Reasoning_Models"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"Thought-Adaptive KV Cache Compression","url":"https://www.emergentmind.com/topics/thought-adaptive-kv-cache-compression"},{"title":"ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://iclr.cc/virtual/2026/oral/10009981"}]

I found the paper you're looking for. Here's a summary of ThinKV:

## ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models

ThinKV is a thought-adaptive KV cache compression framework that applies a hybrid quantization-eviction strategy, assigning token precision by thought importance and progressively evicting tokens from less critical thoughts as reasoni
…[truncated 1006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T19:02:02.397864+00:00_

Web search results for query: "DeepSeek-R1 Incentivizing Reasoning Capability LLMs Reinforcement Learning Nature 2025"

Links: [{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through ...","url":"https://pubmed.ncbi.nlm.nih.gov/40962978/"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2501.12948"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://www.researchgate.net/publication/388317525_DeepSeek-R1_Incentivizing_Reasoning_Capability_in_LLMs_via_Reinforcement_Learning"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning · Pablo Stafforini","url":"https://stafforini.com/works/deepseek-ai-2025-deepseek-r-1-incentivizing/"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs ...","url":"https://arxiv.org/pdf/2501.12948"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12443585/"},{"title":"Paper page - DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://huggingface.co/papers/2501.12948"}]

I found comprehensive information about DeepSeek-R1. Here are the key findings:

## Overview

DeepSeek-R1 demonstrates that the reasoning abilities of large language models can be incentivized through pure reinforcement learning, removing the need for human-annotated demonstrations.

## Key Innovation

The
…[truncated 1081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T19:02:02.398053+00:00_

Web search results for query: ""Phase transitions in large language model compression" npj Artificial Intelligence 2026"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"Phase transitions in large language model compression – DOAJ","url":"https://doaj.org/article/06b2d6b18f08424a9f7778c269597d3c"},{"title":"GitHub - whucs21Mzy/Model-Phase-Transitions: Navigating Model Phase Transitions to Enable Extreme Lossless Compression: A Perspective","url":"https://github.com/whucs21Mzy/Model-Phase-Transitions"},{"title":"Phase transitions in large language models ..","url":"https://www.hyper-exponential.com/p/phase-transitions-in-large-language"},{"title":"Lossless data compression by large models | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01033-7"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Phase transitions in AI-human interaction networks: statistics, computation, and probabilistic modeling","url":"https://arxiv.org/html/2505.02879v1"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"A Survey on Model Compression for Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00704/125482/A-Survey-on-Model-Compression-for-Large-Language"},{"title":"Algorithmic Phase Transitions in Language Models:","url":"https://arxiv.org/pdf/2412.07386"}]

I found the paper you're looking for! Here are the key findings from the search:

## Paper Overview

Large Language Models exhibit Model Phase Transitions: performance collapses beyond critical compression thr
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T19:02:02.398250+00:00_

Web search results for query: "Lethe Layer Time Adaptive KV Cache Pruning Reasoning-Intensive LLM Serving AAAI 2026 arxiv 2511.06029"

Links: [{"title":"[2511.06029] Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/abs/2511.06029"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive","url":"https://www.arxiv.org/pdf/2511.06029"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/html/2511.06029v1"},{"title":"(PDF) Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://www.researchgate.net/publication/397479742_Lethe_Layer-_and_Time-Adaptive_KV_Cache_Pruning_for_Reasoning-Intensive_LLM_Serving"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"[2604.24647] DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference","url":"https://arxiv.org/abs/2604.24647"},{"title":"Online Scheduling for LLM Inference with KV Cache Constraints","url":"https://arxiv.org/html/2502.07115v2"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"},{"title":"[PDF] Lethe: Layer- and Time-Adaptive KV Cache Pruning ...","url":"https://www.semanticscholar.org/paper/Lethe:-Layer-and-Time-Adaptive-KV-Cache-Pruning-for-Zeng-Zhao/ce7628e9428ec7a94005d237f06a814c45a5f9ee"},{"title":"LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/html/2510.09665v2"}]

Based on the web search results, here's information about the paper:

## Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving

Lethe is a dynamic KV cache management framework that introduces adaptivity along both the spatial and temporal dimensions of decoding.

### Problem Context
…[truncated 1669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T19:02:02.398481+00:00_

Web search results for query: "PyramidKV Dynamic KV Cache Compression Pyramidal Information Funneling 2406.02069 published venue 2025 2026"

Links: [{"title":"[2406.02069] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/html/2406.02069v1"},{"title":"Paper page - PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://huggingface.co/papers/2406.02069"},{"title":"[2406.02069v1] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v1"},{"title":"[2406.02069v3] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v3"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | OpenReview","url":"https://openreview.net/forum?id=ayi7qezU87"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | alphaXiv","url":"https://www.alphaxiv.org/abs/2406.02069"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | Request PDF","url":"https://www.researchgate.net/publication/381158444_PyramidKV_Dynamic_KV_Cache_Compression_based_on_Pyramidal_Information_Funneling?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbCwic3ViUGFnZSI6bnVsbH19"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"[Literature Review] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://www.themoonlight.io/en/review/pyramidkv-dynamic-kv-cache-compression-based-on-pyramidal-information-funneling"}]

Based on the search results
…[truncated 1546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T19:02:02.398681+00:00_

Web search results for query: "RetentiveKV State-Space Memory Uncertainty-Aware Multimodal KV Cache Eviction arxiv 2605.04075"

Links: [{"title":"[2605.04075] RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/abs/2605.04075"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"},{"title":"Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference","url":"https://arxiv.org/html/2604.26968"},{"title":"[2605.07234] Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/abs/2605.07234"},{"title":"Stateful KV Cache Management for LLMs: Balancing Space, Time, Accuracy, and Positional Fidelity","url":"https://arxiv.org/html/2511.04686"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression","url":"https://arxiv.org/html/2605.11478"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

## RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction

RetentiveKV addresses computational efficiency and memory consumption challenges in Multimodal Large Language Models caused by the expansion of visual KV cache when processing long visual contexts.

### Key Problems Addressed

The paper identifies two key issues with existing KV cache co
…[truncated 1653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T19:02:02.398880+00:00_

Web search results for query: "GRASPrune Global Gating Budgeted Structured Pruning LLM arxiv 2604.19398 ACL 2026"

Links: [{"title":"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2604.19398"},{"title":"[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2604.19398"},{"title":"GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub","url":"https://github.com/ZiY-Wang/GRASPrune"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/pdf/2603.13418"},{"title":"[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://arxiv.org/abs/2305.11627"},{"title":"[2603.13418] GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.13418"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"GitHub - horseee/LLM-Pruner: [NeurIPS 2023] LLM-Pruner: On the Structural Pruning of Large Language Models. Support Llama-3/3.1, Llama-2, LLaMA, BLOOM, Vicuna, Baichuan, TinyLlama, etc. · GitHub","url":"https://github.com/horseee/LLM-Pruner"},{"title":"From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models","url":"https://arxiv.org/html/2510.18030"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/401447462_LLM-Pruner_On_the_Structural_Pruning_of_Large_Language_Models"}]

Based on the search results, I found comprehensive information about GRASPrune. Here's what I found:

## GRASPrune: Overview

GRASPrune is a structured pruning framework applied after pretraining that jointly prunes FFN channels and KV head g
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T19:02:02.399126+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-R1 Nature DOI 10.1038/s41586-025-08636-z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-R1 Nature DOI 10.1038/s41586-025-08636-z"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-14T19:02:02.399257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SLiM One-shot Quantization Sparsity Low-rank LLM Weight Compression ICML 2025 arxiv 2410.09615"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SLiM One-shot Quantization Sparsity Low-rank LLM Weight Compression ICML 2025 arxiv 2410.09615"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T19:02:02.399376+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyramidKV Dynamic KV Cache Compression accepted conference ACL EMNLP NeurIPS 2025 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyramidKV Dynamic KV Cache Compression accepted conference ACL EMNLP NeurIPS 2025 venue"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-14T19:02:02.399542+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lethe Layer Time Adaptive KV Cache Pruning AAAI 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lethe Layer Time Adaptive KV Cache Pruning AAAI 2026 accepted"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-14T19:02:02.399712+00:00_

Web search results for query: "DeepSeek-R1 Nature DOI 10.1038/s41586-025-08636-z"

Links: [{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through ...","url":"https://pubmed.ncbi.nlm.nih.gov/40962978/"},{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/deepseek-r1"},{"title":"Secrets of DeepSeek AI model revealed in landmark paper","url":"https://www.nature.com/articles/d41586-025-03015-6"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning","url":"https://ideas.repec.org/a/nat/nature/v645y2025i8081d10.1038_s41586-025-09422-z.html"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2501.12948"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through ...","url":"https://www.zotero.org/groups/2365201/wmd-design/items/itemKey/6F652VJG"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"}]

Based on the search results, I found information about the DeepSeek-R1 Nature publication. However, I should note that the DOI you provided (10.1038/s41586-025-08636-z) appears to differ slightly from the actual publication DOI.

The peer-reviewed Nature article on DeepSeek-R1 is authored by Guo, D., Yang, D., Zhang, H. and others, titled "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning" and was published in Nature volume 645, pages 633-638 (2025). The correct DOI appears to be 10.1038/s41586-025-09422-z.

The paper demonstrates that the reasoning abilities of 
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T19:02:02.399910+00:00_

Web search results for query: "PyramidKV Dynamic KV Cache Compression accepted conference ACL EMNLP NeurIPS 2025 venue"

Links: [{"title":"[2406.02069] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | OpenReview","url":"https://openreview.net/forum?id=jZVNmDiU86"},{"title":"DynamicKV: Task-Aware Adaptive KV Cache Compression ...","url":"https://aclanthology.org/2025.findings-emnlp.426.pdf"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/html/2406.02069v1"},{"title":"DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.426/"},{"title":"Achieving More Consistent KV Cache Eviction via Pseudo ...","url":"https://aclanthology.org/2025.emnlp-main.1732.pdf"},{"title":"PyramidKV","url":"https://zefan-cai.github.io/PyramidKV.github.io/"},{"title":"NeurIPS Poster ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://neurips.cc/virtual/2025/poster/120181"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/pyramidkv-dynamic-kv-cache-compression-based-on-pyramidal-information-funneling/"}]

Based on the search results, I can provide you with information about PyramidKV:

## PyramidKV Publication Status

PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling, by Zefan Cai and colleagues, was published on Arxiv 2024. 

The paper does not appear to have been accepted
…[truncated 1049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T19:02:02.400107+00:00_

Web search results for query: "SLiM One-shot Quantization Sparsity Low-rank LLM Weight Compression ICML 2025 arxiv 2410.09615"

Links: [{"title":"[2410.09615] SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/abs/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank ...","url":"https://arxiv.org/pdf/2410.09615"},{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/html/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241009615M/abstract"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | alphaXiv","url":"https://www.alphaxiv.org/abs/2410.09615"},{"title":"GitHub - Paramathic/slim: SLiM: One-shot Quantized Sparse Plus Low-rank Approximation of LLMs (ICML 2025) · GitHub","url":"https://github.com/Mohammad-Mozaffari/slim"},{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"},{"title":"SLiM : One-shot Quantized Sparse Plus Low-rank Approximation of LLMs","url":"https://arxiv.org/html/2410.09615v1"},{"title":"[Literature Review] SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://www.themoonlight.io/en/review/slim-one-shot-quantization-and-sparsity-with-low-rank-approximation-for-llm-weight-compression"}]

Based on the search results, here's what I found about the paper:

## SLiM: One-shot Quantizati
…[truncated 1482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T19:02:02.400280+00:00_

Web search results for query: "Lethe Layer Time Adaptive KV Cache Pruning AAAI 2026 accepted"

Links: [{"title":"[2511.06029] Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/abs/2511.06029"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive","url":"https://www.arxiv.org/pdf/2511.06029"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/html/2511.06029v1"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40036/43997"},{"title":"(PDF) Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://www.researchgate.net/publication/397479742_Lethe_Layer-_and_Time-Adaptive_KV_Cache_Pruning_for_Reasoning-Intensive_LLM_Serving"},{"title":"[PDF] Lethe: Layer- and Time-Adaptive KV Cache Pruning ...","url":"https://www.semanticscholar.org/paper/Lethe:-Layer-and-Time-Adaptive-KV-Cache-Pruning-for-Zeng-Zhao/ce7628e9428ec7a94005d237f06a814c45a5f9ee"},{"title":"Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference","url":"https://arxiv.org/html/2601.07667"},{"title":"Caching and Reuse Optimizations","url":"https://www.aussieai.com/research/caching"},{"title":"SPARK: Query-Aware Unstructured Sparsity with","url":"https://arxiv.org/pdf/2508.15212"},{"title":"[2601.07667] Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference","url":"https://arxiv.org/abs/2601.07667"}]

Based on the search results, I found information about the Lethe paper on Layer- and Time-Adaptive KV Cache Pruning:

Lethe is a dynamic KV cache management framework that introduces adaptivity along both the spatial and temporal dimensions of decoding. Along the spatial dimension, Lethe performs layerwise sparsity-aware allocation, assigning token pruning budgets to each transformer layer based
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T19:02:02.400547+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/reference_audit_report.md",
  "content": "# Reference Audit Report — Phase-Gated Compound Sparse\n\n**Date**: 2026-05-14\n**Paper**: \"Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\"\n**Bib file**: `artifacts/_project/paper/references.bib`\n**Tex files**: 14 files in `artifacts/_project/paper/`\n\n---\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Bib entries | 31 |\n| Unique citation keys used in .tex | 26 |\n| Orphan entries (bib only, not cited) | 5 |\n| Missing entries (cited but not in bib) | 0 |\n| WebSearch-verified references | 8 |\n| Issues found | 7 |\n\n---\n\n## Issues\n\n### Critical (1)\n\n#### 1. `deepseek-r1-2025` — Wrong DOI\n\n**Current bib**: `doi = {10.1038/s41586-025-08636-z}`\n**Correct DOI**: `10.1038/s41586-025-09422-z`\n\nThe DOI in the bib file does not resolve to the DeepSeek-R1 Nature article. The correct DOI is confirmed via Nature, PubMed (PMID 40962978), and RePEc.\n\n**Action**: Replace DOI with `10.1038/s41586-025-09422-z`.\n\n---\n\n### Warning (3)\n\n#### 2. `deepseek-r1-2025` — Title mismatch (arXiv vs Nature)\n\n**Current bib title**: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n**Nature published title**: \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\"\n\nSince the bib cites the Nature version (journal = Nature, volume = 645, pages = 633–638), the title should match the published version.\n\n**Action**: Update title to Nature published version, or keep arXiv title and add a note. Recommended: use Nature title since journal/volume/pages point to Nature.\n\n#### 3. `deepseek-r1-2025` — Author field\n\n**Current**: `author = {{DeepSeek-AI}}`\n**Nature version**: Individual authors listed (Guo, D., Yang, D., Zhang, H., et al.)\n\nUsing the collective name is common for arXiv versions but Nature lists individual authors. Since journal=Nature, consider using individual authors.\n\n**Action**: Update to individual author list per the Nature publication, or keep `{DeepSeek-AI}` if brevity is preferred (acceptable but non-standard for Nature citations).\n\n#### 4. Five orphan bib entries (not cited in any .tex file)\n\n| Key | Title |\n|-----|-------|\n| `compression-ordering-2025` | A Systematic Study of Compression Ordering for Large Language Models |\n| `mustafar-neurips2025` | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning |\n| `obcache-2025` | OBCache: Optimal Brain KV Cache Pruning |\n| `pagedeviction-eacl2026` | PagedEviction: Structured Block-wise KV Cache Pruning |\n| `raas-acl2025` | RaaS: Reasoning-Aware Attention Sparsity |\n\nThese entries exist in `references.bib` but are not referenced by any `\\cite{}` in the paper. They will not appear in the bibliography but add clutter.\n\n**Action**: Remove orphan entries, or cite them in Related Work if relevant.\n\n---\n\n### Info (3)\n\n#### 5. `pyramidkv-2024` — Potentially published but listed as arXiv\n\nThe bib lists PyramidKV as `@article` (arXiv preprint, 2024). OpenReview submissions exist (IDs: `jZVNmDiU86`, `ayi7qezU87`), suggesting it may have been accepted at a venue. No confirmed acceptance found in search results as of May 2026.\n\n**Action**: Verify whether PyramidKV has been formally published; if so, update entry type and venue.\n\n#### 6. Papers mentioned in `paper_framing.md` but absent from bib/tex\n\nThe paper framing document (RC5, RC6 sections) identifies the following papers as important for positioning but they are **not** cited in the current paper:\n\n| Paper | arXiv ID | Relevance per framing |\n|-------|----------|----------------------|\n| Physics of KV Cache Compression | 2603.01426 | Single-axis phase transition vs our phase-dependent gradient |\n| HIES (importance score collapse) | 2510.13832 | Independent evidence for discrimination collapse mechanism |\n| R-KV (reasoning KV compression) | 2505.24133 | Task-specific method, different goal (optimization vs understanding) |\n\nThese are listed in the framing as positioning references for anticipated reviewer concerns RC5 and RC6, but the Related Work section does not include them.\n\n**Action**: Consider adding these to Related Work §2 if the framing analysis is still current, especially HIES (supports the discrimination collapse mechanism) and Physics of KV Cache Compression (closest related work per framing).\n\n#### 7. DOI field inconsistency\n\nOnly `deepseek-r1-2025` has a `doi` field. Other published-at-venue entries (e.g., `h2o-neurips2023`, `snapkv-neurips2024`, `slim-icml2025`) lack DOI. This is minor — arXiv URLs are generally sufficient — but adding DOIs for published proceedings would improve discoverability.\n\n**Action**: Optional. Add DOI for published venue papers if available.\n\n---\n\n## WebSearch Verification Results\n\n| Bib Key | Claimed Venue | Verified | Notes |\n|---------|---------------|----------|-------|\n| `spark-aaai2026` | AAAI 2026 | **Yes** | GitHub confirms \"[AAAI 2026]\" |\n| `thinkv-iclr2026` | ICLR 2026 | **Yes** | ICLR 2026 Oral confirmed |\n| `deepseek-r1-2025` | Nature 645, 633–638 | **Yes** | Volume/pages match; DOI incorrect (see #1) |\n| `lethe-aaai2026` | AAAI 2026 | **Yes** | AAAI proceedings link confirmed |\n| `phase-transition-compression-2026` | npj AI 2026 | **Yes** | Nature.com article confirmed |\n| `retentivekv-2026` | arXiv 2605.04075 | **Yes** | arXiv page exists |\n| `graspune-acl2026` | ACL 2026 | **Yes** | GitHub confirms \"ACL 2026 Main\" |\n| `slim-icml2025` | ICML 2025 | **Yes** | ICML poster page + NVIDIA Research confirmed |\n\nNo hallucinated references detected. All 8 sampled references are real papers with matching titles and authors.\n\n---\n\n## Cross-Reference Matrix\n\nAll 26 citation keys used in .tex files have corresponding bib entries:\n\n| Citation Key | Used In |\n|-------------|---------|\n| `kwon-sosp2023` | introduction |\n| `pope-mlsys2023` | introduction |\n| `voita-acl2019` | introduction, background, appendix |\n| `michel-neurips2019` | introduction, background, appendix |\n| `snapkv-neurips2024` | introduction, related_work, discussion |\n| `adakv-neurips2025` | introduction, related_work |\n| `spark-aaai2026` | introduction, related_work, background, appendix |\n| `slim-icml2025` | introduction, related_work |\n| `unicomp-2026` | introduction, related_work |\n| `phase-transition-compression-2026` | introduction, related_work |\n| `decision-repr-transition-2026` | introduction, related_work |\n| `sparse-frontier-2025` | introduction, related_work |\n| `thinkv-iclr2026` | introduction, related_work, background |\n| `greedy-bias-kvcache-2026` | introduction, related_work |\n| `retentivekv-2026` | introduction, related_work |\n| `lethe-aaai2026` | introduction, related_work |\n| `graspune-acl2026` | related_work, background |\n| `defensivekv-iclr2026` | related_work, background, appendix |\n| `nacl-acl2024` | related_work, background |\n| `doing-more-with-less-2026` | related_work |\n| `deepseek-r1-2025` | methodology |\n| `qwen25-2024` | methodology |\n| `math500-neurips2021` | methodology |\n| `efron-1993` | methodology |\n| `h2o-neurips2023` | discussion |\n| `pyramidkv-2024` | discussion |\n\n---\n\n## Bib Entry Completeness\n\nAll 31 bib entries have: title, author, year. Format breakdown:\n\n| Type | Count | Required fields present |\n|------|-------|------------------------|\n| @inproceedings | 18 | All have booktitle |\n| @article | 12 | All have journal |\n| @book | 1 | Has publisher |\n\nNo entries are missing critical fields (title, author, year, venue).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/reference_audit_report.md",
    "content": "# Reference Audit Report — Phase-Gated Compound Sparse\n\n**Date**: 2026-05-14\n**Paper**: \"Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\"\n**Bib file**: `artifacts/_project/paper/references.bib`\n**Tex files**: 14 files in `artifacts/_project/paper/`\n\n---\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Bib entries | 31 |\n| Unique citation keys used in .tex | 26 |\n| Orphan entries (bib only, not cited) | 5 |\n| Missing entries (cited but not in bib) | 0 |\n| WebSearch-verified references | 8 |\n| Issues found | 7 |\n\n---\n\n## Issues\n\n### Critical (1)\n\n#### 1. `deepseek-r1-2025` — Wrong DOI\n\n**Current bib**: `doi = {10.1038/s41586-025-08636-z}`\n**Correct DOI**: `10.1038/s41586-025-09422-z`\n\nThe DOI in the bib file does not resolve to the DeepSeek-R1 Nature article. The correct DOI is confirmed via Nature, PubMed (PMID 40962978), and RePEc.\n\n**Action**: Replace DOI with `10.1038/s41586-025-09422-z`.\n\n---\n\n### Warning (3)\n\n#### 2. `deepseek-r1-2025` — Title mismatch (arXiv vs Nature)\n\n**Current bib title**: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n**Nature published title**: \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\"\n\nSince the bib cites the Nature version (journal = Nature, volume = 645, pages = 633–638), the title should match the published version.\n\n**Action**: Update title to Nature published version, or keep arXiv title and add a note. Recommended: use Nature title since journal/volume/pages point to Nature.\n\n#### 3. `deepseek-r1-2025` — Author field\n\n**Current**: `author = {{DeepSeek-AI}}`\n**Nature version**: Individual authors listed (Guo, D., Yang, D., Zhang, H., et al.)\n\nUsing the collective name is common for arXiv versions but Nature lists individual authors. Since journal=Nature, consider using individual authors.\n\n**Action**: Update to individual author list per the Nature publication, or keep `{DeepSeek-AI}` if brevity is preferred (acceptable but non-standard for Nature citations).\n\n#### 4. Five orphan bib entries (not cited in any .tex file)\n\n| Key | Title |\n|-----|-------|\n| `compression-ordering-2025` | A Systematic Study of Compression Ordering for Large Language Models |\n| `mustafar-neurips2025` | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning |\n| `obcache-2025` | OBCache: Optimal Brain KV Cache Pruning |\n| `pagedeviction-eacl2026` | PagedEviction: Structured Block-wise KV Cache Pruning |\n| `raas-acl2025` | RaaS: Reasoning-Aware Attention Sparsity |\n\nThese entries exist in `references.bib` but are not referenced by any `\\cite{}` in the paper. They will not appear in the bibliography but add clutter.\n\n**Action**: Remove orphan entries, or cite them in Related Work if relevant.\n\n---\n\n### Info (3)\n\n#### 5. `pyramidkv-2024` — Potentially published but listed as arXiv\n\nThe bib lists PyramidKV as `@article` (arXiv preprint, 2024). OpenReview submissions exist (IDs: `jZVNmDiU86`, `ayi7qezU87`), suggesting it may have been accepted at a venue. No confirmed acceptance found in search results as of May 2026.\n\n**Action**: Verify whether PyramidKV has been formally published; if so, update entry type and venue.\n\n#### 6. Papers mentioned in `paper_framing.md` but absent from bib/tex\n\nThe paper framing document (RC5, RC6 sections) identifies the following papers as important for positioning but they are **not** cited in the current paper:\n\n| Paper | arXiv ID | Relevance per framing |\n|-------|----------|----------------------|\n| Physics of KV Cache Compression | 2603.01426 | Single-axis phase transition vs our phase-dependent gradient |\n| HIES (importance score collapse) | 2510.13832 | Independent evidence for discrimination collapse mechanism |\n| R-KV (reasoning KV compression) | 2505.24133 | Task-specific method, different goal (optimization vs understanding) |\n\nThese are listed in the framing as positioning references for anticipated reviewer concerns RC5 and RC6, but the Related Work section does not include them.\n\n**Action**: Consider adding these to Related Work §2 if the framing analysis is still current, especially HIES (supports the discrimination collapse mechanism) and Physics of KV Cache Compression (closest related work per framing).\n\n#### 7. DOI field inconsistency\n\nOnly `deepseek-r1-2025` has a `doi` field. Other published-at-venue entries (e.g., `h2o-neurips2023`, `snapkv-neurips2024`, `slim-icml2025`) lack DOI. This is minor — arXiv URLs are generally sufficient — but adding DOIs for published proceedings would improve discoverability.\n\n**Action**: Optional. Add DOI for published venue papers if available.\n\n---\n\n## WebSearch Verification Results\n\n| Bib Key | Claimed Venue | Verified | Notes |\n|---------|---------------|----------|-------|\n| `spark-aaai2026` | AAAI 2026 | **Yes** | GitHub confirms \"[AAAI 2026]\" |\n| `thinkv-iclr2026` | ICLR 2026 | **Yes** | ICLR 2026 Oral confirmed |\n| `deepseek-r1-2025` | Nature 645, 633–638 | **Yes** | Volume/pages match; DOI incorrect (see #1) |\n| `lethe-aaai2026` | AAAI 2026 | **Yes** | AAAI proceedings link confirmed |\n| `phase-transition-compression-2026` | npj AI 2026 | **Yes** | Nature.com article confirmed |\n| `retentivekv-2026` | arXiv 2605.04075 | **Yes** | arXiv page exists |\n| `graspune-acl2026` | ACL 2026 | **Yes** | GitHub confirms \"ACL 2026 Main\" |\n| `slim-icml2025` | ICML 2025 | **Yes** | ICML poster page + NVIDIA Research confirmed |\n\nNo hallucinated references detected. All 8 sampled references are real papers with matching titles and authors.\n\n---\n\n## Cross-Reference Matrix\n\nAll 26 citation keys used in .tex files have corresponding bib entries:\n\n| Citation Key | Used In |\n|-------------|---------|\n| `kwon-sosp2023` | introduction |\n| `pope-mlsys2023` | introduction |\n| `voita-acl2019` | introduction, background, appendix |\n| `michel-neurips2019` | introduction, background, appendix |\n| `snapkv-neurips2024` | introduction, related_work, discussion |\n| `adakv-neurips2025` | introduction, related_work |\n| `spark-aaai2026` | introduction, related_work, background, appendix |\n| `slim-icml2025` | introduction, related_work |\n| `unicomp-2026` | introduction, related_work |\n| `phase-transition-compression-2026` | introduction, related_work |\n| `decision-repr-transition-2026` | introduction, related_work |\n| `sparse-frontier-2025` | introduction, related_work |\n| `thinkv-iclr2026` | introduction, related_work, background |\n| `greedy-bias-kvcache-2026` | introduction, related_work |\n| `retentivekv-2026` | introduction, related_work |\n| `lethe-aaai2026` | introduction, related_work |\n| `graspune-acl2026` | related_work, background |\n| `defensivekv-iclr2026` | related_work, background, appendix |\n| `nacl-acl2024` | related_work, background |\n| `doing-more-with-less-2026` | related_work |\n| `deepseek-r1-2025` | methodology |\n| `qwen25-2024` | methodology |\n| `math500-neurips2021` | methodology |\n| `efron-1993` | methodology |\n| `h2o-neurips2023` | discussion |\n| `pyramidkv-2024` | discussion |\n\n---\n\n## Bib Entry Completeness\n\nAll 31 bib entries have: title, author, year. Format breakdown:\n\n| Type | Count | Required fields present |\n|------|-------|------------------------|\n| @inproceedings | 18 | All have booktitle |\n| @article | 12 | All have journal |\n| @book | 1 | Has publisher |\n\nNo entries are missing critical fields (title, author, year, venue).\n"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T19:02:02.400792+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/reference_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T19:02:02.400928+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Reference Audit Report",
  "type": "report",
  "description": "Full citation audit for the phase-gated-compound-sparse paper: cross-reference check, orphan detection, WebSearch verification of 8 key references, DOI validation. Found 1 critical (wrong DOI), 3 warnings (title/author mismatch, orphan entries), 3 info items.",
  "project": "phase-gated-compound-sparse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/reference_audit_report.md",
  "tags": "['reference-audit', 'submission', 'quality']",
  "skill": "reference-audit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Reference Audit Report",
    "type": "report",
    "description": "Full citation audit for the phase-gated-compound-sparse paper: cross-reference check, orphan detection, WebSearch verification of 8 key references, DOI validation. Found 1 critical (wrong DOI), 3 warnings (title/author mismatch, orphan entries), 3 info items.",
    "project": "phase-gated-compound-sparse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/reference_audit_report.md",
    "tags": "['reference-audit', 'submission', 'quality']",
    "skill": "reference-audit"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T19:02:02.401075+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_8090b2\", \"name\": \"Reference Audit Report\", \"type\": \"report\", \"description\": \"Full citation audit for the phase-gated-compound-sparse paper: cross-reference check, orphan detection, WebSearch verification of 8 key references, DOI validation. Found 1 critical (wrong DOI), 3 warnings (title/author mismatch, orphan entries), 3 info items.\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/report/reference_audit_report.md\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"reference-audit\", \"created_at\": \"2026-05-14T19:01:46.219186+00:00\", \"tags\": [\"reference-audit\", \"submission\", \"quality\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_audit_20260514T185731",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-14T19:02:02.401239+00:00_

审计完成。结果如下：

**总计**: 31 条 bib 条目，26 条被正文引用，8 条经 WebSearch 验证真实性（全部通过，无幻觉引用）。

**发现 7 个问题**：

| 严重度 | 数量 | 概要 |
|--------|------|------|
| Critical | 1 | `deepseek-r1-2025` DOI 错误：bib 中 `10.1038/s41586-025-08636-z`，正确应为 `10.1038/s41586-025-09422-z` |
| Warning | 3 | (1) 同条目 Nature 标题与 bib 标题不一致；(2) author 用 `{DeepSeek-AI}` 但 Nature 列出个人作者；(3) 5 个 orphan bib 条目未被引用 |
| Info | 3 | (1) PyramidKV 可能已发表但仍标为 arXiv；(2) paper_framing 提到的 3 篇定位参考文献（Physics of KV Cache Compression / HIES / R-KV）未出现在 Related Work 中；(3) DOI 字段不一致 |

**最优先修复**：`deepseek-r1-2025` 的 DOI 需立即更正，否则读者/审稿人点击 DOI 链接无法到达正确论文。

报告已写入 `artifacts/reference_audit_report.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_reference_audit_20260514T185731"
}
```

</details>

---
