# analysis reference audit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_reference_audit_20260522T042955.jsonl`
- **Structured JSON:** [`0cbe65fc6996febbfce8.json`](../../sessions/0c/0cbe65fc6996febbfce8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-22T04:39:44.848193+00:00_

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
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T04:39:44.848894+00:00_

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
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T04:39:44.849083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T04:39:44.849347+00:00_

1	% ============================================================
2	% Layer Importance
3	% ============================================================
4	
5	@inproceedings{gromov2024deeper,
6	  author    = {Gromov and others},
7	  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},
8	  booktitle = {International Conference on Learning Representations},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2403.17887}
11	}
12	
13	@article{men2024shortgpt,
14	  author  = {Men and others},
15	  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},
16	  journal = {arXiv preprint arXiv:2403.03853},
17	  year    = {2024},
18	  url     = {https://arxiv.org/abs/2403.03853}
19	}
20	
21	@inproceedings{sun2025curse,
22	  author    = {Sun and others},
23	  title     = {{The Curse of Depth in Large Language Models}},
24	  booktitle = {Advances in Neural Information Processing Systems},
25	  year      = {2025},
26	  url       = {https://arxiv.org/abs/2502.05795}
27	}
28	
29	@article{anonymous2024reassessing,
30	  author  = {{Anonymous}},
31	  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},
32	  journal = {arXiv preprint arXiv:2411.15558},
33	  year    = {2024},
34	  url     = {https://arxiv.org/abs/2411.15558}
35	}
36	
37	@inproceedings{fan2020layerdrop,
38	  author    = {Fan and others},
39	  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},
40	  booktitle = {International Conference on Learning Representations},
41	  year      = {2020},
42	  url       = {https://arxiv.org/abs/1909.11556}
43	}
44	
45	% ============================================================
46	% Multi-Turn Attention
47	% ============================================================
48	
49	@article{dongre2026attention,
50	  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},
51	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interac
…[truncated 14015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T04:39:44.849622+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__verify_references",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__verify_references",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T04:39:44.849772+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T04:39:44.849901+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T04:39:44.850049+00:00_

paper/sections/analysis.tex:22:[Omitted long matching line]
paper/sections/analysis.tex:39:[Omitted long matching line]
paper/sections/analysis.tex:53:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:7:ReZero \citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \citep{fan2020layerdrop}, Mixture-of-Depths \citep{raposo2024mixture}, FlexiDepth \citep{luo2025flexidepth}, and CALM \citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.
paper/sections/related_work.tex:10:[Omitted long matching line]
paper/sections/related_work.tex:13:GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.
paper/sections/related_work.tex:16:[Omitted long matching line]
paper/sections/experiments.tex:8:[Omitted long matching line]
paper/sections/experiments.tex:14:[Omitted long matching line]
paper/sections/experiments.tex:21:\caption{Five-way comparison on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All four fine-tuned variants converge to within 0.75\,pp on GAR-ours; PPL is indistinguishable. GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
paper/sections/discussion.tex:5:[Omitted long matching line]
paper/sections/discussion.tex:9:TRC analysis (\S\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence
…[truncated 1504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T04:39:44.850202+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T04:39:44.850800+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 91, \"total_citations\": 46, \"unique_cited_keys\": 22, \"orphan_bib\": 24, \"missing_bib\": 0, \"duplicate_keys\": 45, \"online_verified\": 33, \"online_not_found\": 3, \"online_mismatch\": 10, \"online_error\": 0, \"online_checked\": 46, \"online_total\": 46, \"online_verified_by_doi\": 0, \"online_verified_by_arxiv\": 20, \"online_verified_by_search\": 13}, \"cross_check\": {\"orphan_bib\": [\"anonymous2024reassessing\", \"anonymous2025style\", \"belrose2023tuned\", \"chen2023positional\", \"chiang2024arena\", \"dubois2024alpacaeval\", \"elhage2021framework\", \"elhage2022superposition\", \"gromov2024deeper\", \"han2024lminfinite\", \"ildiz2024markov\", \"lawson2025skip\", \"lin2024wildbench\", \"liu2023lost\", \"makkuva2025markov\", \"men2024shortgpt\", \"peng2024yarn\", \"press2022alibi\", \"sirdeshmukh2025multichallenge\", \"sun2025curse\", \"wang2018skipnet\", \"yu2023residual\", \"zhang2019fixup\", \"zheng2023mtbench\"], \"missing_bib\": [], \"orphan_count\": 24, \"missing_count\": 0}, \"bib_problems\": [{\"key\": \"gromov2024deeper\", \"type\": \"inproceedings\", \"title\": \"The Unreasonable Ineffectiveness of the Deeper Layers\", \"authors\": \"Gromov and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"men2024shortgpt\", \"type\": \"article\", \"title\": \"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\", \"authors\": \"Men and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"sun2025curse\", \"type\": \"inproceedings\", \"title\": \"The Curse of Depth in Large Language Models\", \"authors\": \"Sun and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2024reassessing\", \"type\": \"article\", \"title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"fan2020layerdrop\", \"type\": \"inproceed
…[truncated 27475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T04:39:44.851050+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T04:39:44.851323+00:00_

paper/sections/references.bib
paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T04:39:44.851536+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\bibliography\\{|\\\\addbibresource",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\bibliography\\{|\\\\addbibresource",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T04:39:44.851789+00:00_

paper/main.tex:38:\bibliography{references}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T04:39:44.852079+00:00_

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
  "session": "worker_analysis_reference_audit_20260522T042955",
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

_source line 16 · 2026-05-22T04:39:44.852245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T04:39:44.852384+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LayerDrop \"Reducing Transformer Depth on Demand with Structured Dropout\" Fan 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LayerDrop \"Reducing Transformer Depth on Demand with Structured Dropout\" Fan 2020"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T04:39:44.852554+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FlexiDepth \"Adaptive Layer-skipping in Pre-trained LLMs\" Luo 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FlexiDepth \"Adaptive Layer-skipping in Pre-trained LLMs\" Luo 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T04:39:44.852678+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Mathematical Framework for Transformer Circuits\" Elhage Anthropic 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Mathematical Framework for Transformer Circuits\" Elhage Anthropic 2021"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T04:39:44.852795+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Exploring the Residual Stream of Transformers\" arXiv 2312.12141"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Exploring the Residual Stream of Transformers\" arXiv 2312.12141"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T04:39:44.852907+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Quantifying Exposure Bias for Neural Language Generation\" He 2019 arXiv 1905.10617"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Quantifying Exposure Bias for Neural Language Generation\" He 2019 arXiv 1905.10617"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T04:39:44.853019+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLMs Get Lost In Multi-Turn Conversation\" 2025 arXiv first author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLMs Get Lost In Multi-Turn Conversation\" 2025 arXiv first author"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T04:39:44.853400+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Found in the Middle: Calibrating Positional Attention Bias\" first author 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Found in the Middle: Calibrating Positional Attention Bias\" first author 2024"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T04:39:44.853656+00:00_

Web search results for query: "LayerDrop "Reducing Transformer Depth on Demand with Structured Dropout" Fan 2020"

Links: [{"title":"LayerDrop: Reducing Transformer Depth on Demand | SERP AI","url":"https://serp.ai/posts/layerdrop/"},{"title":"[1909.11556] Reducing Transformer Depth on Demand with Structured Dropout","url":"https://arxiv.org/abs/1909.11556"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout | Request PDF","url":"https://www.researchgate.net/publication/336056561_Reducing_Transformer_Depth_on_Demand_with_Structured_Dropout"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout","url":"https://papertalk.org/papertalks/4168"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout | OpenReview","url":"https://openreview.net/forum?id=SylO2yStDr"},{"title":"Paper page - Reducing Transformer Depth on Demand with Structured Dropout","url":"https://huggingface.co/papers/1909.11556"},{"title":"REDUCING TRANSFORMER DEPTH ON DEMAND WITH STRUCTURED DROPOUT Angela Fan","url":"https://arxiv.org/pdf/1909.11556"},{"title":"ICLR: Reducing Transformer Depth on Demand with Structured Dropout","url":"https://iclr.cc/virtual_2020/poster_SylO2yStDr.html"},{"title":"Dropout layers, not weights or nodes! \"LayerDrop\" proposal | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/dropout/LayerDrop"}]

I found several comprehensive sources about the LayerDrop paper. Here's what the search results show:

## Overview

LayerDrop is a form of structured dropout which has a regularization effect during training and allows for efficient pruning at inference time. The paper was published at the ICLR 2020 virtual conference.

## Key Findings

The technique enables selecting sub-networks of any depth from one large network without having to finetune them and with limited impact on performance. LayerDrop applies structured dropout directly to the Transform
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T04:39:44.853904+00:00_

Web search results for query: "FlexiDepth "Adaptive Layer-skipping in Pre-trained LLMs" Luo 2025 arXiv"

Links: [{"title":"[2503.23798] Adaptive Layer-skipping in Pre-trained LLMs","url":"https://arxiv.org/abs/2503.23798"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs - Paper Reading","url":"http://paperreading.club/page?id=296091"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs Xuan Luo, Weizhi Wang, Xifeng Yan","url":"https://arxiv.org/pdf/2503.23798"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs","url":"https://arxiv.org/html/2503.23798v1"},{"title":"GitHub - luoxuan-cs/Flexidepth: The official repo for the paper \"Adaptive Layer-skipping in Pre-trained LLMs\" · GitHub","url":"https://github.com/luoxuan-cs/Flexidepth"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs - Xuan Luo","url":"https://luoxuan-cs.github.io/flexidepth/"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs","url":"https://openreview.net/pdf?id=Gu0XSax2YS"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs | OpenReview","url":"https://openreview.net/forum?id=Gu0XSax2YS"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adaptive-layer-skipping-pre-trained-llms"},{"title":"Adaptive Inference in Pre-trained LLMs Layer-skipping","url":"https://sites.cs.ucsb.edu/~xyan/presentation/Colm2025_Adaptive.pdf"}]

I found comprehensive information about the FlexiDepth paper. Here's what the search revealed:

## Overview

FlexiDepth is a method that dynamically adjusts the number of Transformer layers used in text generation by incorporating a plug-in router and adapter, enabling adaptive computation in LLMs without modifying their original parameters.

## Key Results

Applied to Llama-3-8B, it skips 8 out of 32 layers while maintaining full benchmark performance.

## Main Findings

Computational demands in LLMs significantly vary based on token type, with generating repetitive tokens or fixed
…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T04:39:44.854114+00:00_

Web search results for query: ""A Mathematical Framework for Transformer Circuits" Elhage Anthropic 2021"

Links: [{"title":"Transformer Circuits: A Mathematical Framework","url":"https://studylib.net/doc/27496897/transformer-circui...--1-"},{"title":"Arxiv Dives - A Mathematical Framework for Transformer Circuits - Part 1","url":"https://ghost.oxen.ai/arxiv-dives-a-mathematical-framework-for-transformer-circuits/"},{"title":"Studypool Homework Help - A mathematical framework for transformer circuits","url":"https://www.studypool.com/documents/43042208/a-mathematical-framework-for-transformer-circuits"},{"title":"JongGeun Lee, Jungwoo Yang, Haesung Pyun A Mathematical Framework","url":"https://jungwooyang.com/assets/files/framework-transformer-circuits.pdf"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://www.scribd.com/document/866284321/A-Mathematical-Framework-for-Transformer-Circuits"},{"title":"1 Introduction","url":"https://arxiv.org/html/2402.02619v3"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://transformer-circuits.pub/2021/framework/index.html"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual   Decomposition","url":"https://arxiv.org/pdf/2407.00886"},{"title":"A Mathematical Framework for Transformer Circuits \\ Anthropic","url":"https://www.anthropic.com/research/a-mathematical-framework-for-transformer-circuits"}]

Based on the search results, I found information about this paper:

The paper "A Mathematical Framework for Transformer Circuits" was authored by Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah from Anthropic and was published on December 22, 2021.

Th
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-22T04:39:44.854293+00:00_

Web search results for query: ""LLMs Get Lost In Multi-Turn Conversation" 2025 arXiv first author"

Links: [{"title":"[2505.06120v1] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120v1"},{"title":"[2505.06120] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120"},{"title":"Why LLMs Fail in Multi-Turn Conversations and a Simple Fix","url":"https://www.keywordsai.co/blog/how-to-fix-it-when-llms-get-lost-in-multi-turn-conversation"},{"title":"[PDF] LLMs Get Lost In Multi-Turn Conversation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLMs-Get-Lost-In-Multi-Turn-Conversation-Laban-Hayashi/bb5d81576c113f0b16234fd0db4238a4281c8388"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/html/2602.07338v1"},{"title":"[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/abs/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"}]

Based on the search results, the first author of the 2025 arXiv paper "LLMs Get Lost In Multi-Turn Conversation" is Philippe Laban. The paper was submitted on May 9, 2025 with arXiv ID 2505.06120.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T04:39:44.854514+00:00_

Web search results for query: ""Exploring the Residual Stream of Transformers" arXiv 2312.12141"

Links: [{"title":"Exploring the Residual Stream of Transformers - Paper Reading","url":"https://paperreading.club/page?id=200769"},{"title":"[2312.12141v1] Exploring the Residual Stream of Transformers","url":"https://arxiv.org/abs/2312.12141v1"},{"title":"Exploring the Residual Stream of Transformers","url":"https://arxiv.org/html/2312.12141v1"},{"title":"Exploring the Residual Stream of Transformers | Zendy","url":"https://zendy.io/pdf-viewer/2312.12141"},{"title":"Exploring the Residual Stream of Transformers for Mechanistic Interpretability — Explained | by Zeping Yu | Medium","url":"https://medium.com/@zepingyu/123-cb62513f5d50"},{"title":"Transformers represent belief state geometry in their residual stream","url":"https://arxiv.org/pdf/2405.15943"},{"title":"Residual Streams in Transformer Models","url":"https://retr0sushi04.netlify.app/blogs/residualstreamsblog/residualstreams"},{"title":"Patterns and Messages - Part 5 - The Residual Stream · Chris McCormick","url":"https://mccormickml.com/2025/02/20/patterns-and-messages-part-5-the-residual-stream/"},{"title":"Residual Matrix Transformers: Scaling the Size of the Residual Stream","url":"https://arxiv.org/pdf/2506.22696"},{"title":"Characterizing stable regions in the residual stream of LLMs","url":"https://arxiv.org/pdf/2409.17113"}]

Based on the search results, here's what I found about the paper "Exploring the Residual Stream of Transformers" (arXiv 2312.12141):

## Overview

The paper was submitted on December 19, 2023, and authored by Zeping Yu, Kailai Yang, Zhiwei Liu, and Sophia Ananiadou.

## Research Focus

The paper explores the residual stream of transformers to increase the interpretability. The authors address the challenge of locating models' important parameters storing the knowledge for predicting the next word, and whether these parameters are stored on the same layer/module or different ones.

…[truncated 550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T04:39:44.854708+00:00_

Web search results for query: ""Quantifying Exposure Bias for Neural Language Generation" He 2019 arXiv 1905.10617"

Links: [{"title":"[1905.10617v1] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v1"},{"title":"[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v4"},{"title":"Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/pdf/1905.10617v4"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Exposure-Bias-for-Neural-Language-He-Zhang/cbb1a1a80d26043867bb8bf2b7227c9139710ee5"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Request PDF","url":"https://www.researchgate.net/publication/333418764_Quantifying_Exposure_Bias_for_Neural_Language_Generation"},{"title":"Quantifying Exposure Bias for Neural Language Generation | OpenReview","url":"https://openreview.net/forum?id=rJg2fTNtwr"},{"title":"[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://arxiv.org/abs/1905.10617"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error","url":"https://arxiv.org/pdf/2204.01171"},{"title":"Quantifying Exposure Bias for Neural Language Generation - Paper Detail","url":"https://deeplearn.org/arxiv/127105/quantifying-exposure-bias-for-neural-language-generation"},{"title":"Rethinking Exposure Bias In Language Modeling","url":"https://arxiv.org/pdf/1910.11235"}]

I found the paper you were looking for. Here's what the search results show about this work:

"Quantifying Exposure Bias for Neural Language Generation" by He et al. (2019) addresses the exposure bias problem, which refers to the training-inference discrepancy caused by teacher forcing in maximum likelihood estimation (MLE) training for recurrent neural network la
…[truncated 689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T04:39:44.854898+00:00_

Web search results for query: ""Found in the Middle: Calibrating Positional Attention Bias" first author 2024"

Links: [{"title":"[2406.16008] Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/abs/2406.16008"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/found-middle-calibrating-positional-attention-bias-improves"},{"title":"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.890/"},{"title":"Paper page - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://huggingface.co/papers/2406.16008"},{"title":"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization | Request PDF","url":"https://www.researchgate.net/publication/384206851_Found_in_the_middle_Calibrating_Positional_Attention_Bias_Improves_Long_Context_Utilization"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long-Context RAG - Beancount.io","url":"https://beancount.io/bean-labs/research-logs/2026/07/02/found-in-the-middle-calibrating-positional-attention-bias"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/html/2406.16008v2"},{"title":"Found in the Middle: Calibrating Positional Attention Bias","url":"https://arxiv.org/pdf/2406.16008"}]

Based on the search results, I found the paper you're looking for:

**Title:** Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization

**First Author:** Cheng-Yu Hsieh

**Publication Details:** The paper was published in Findings of the Association for Computational Linguistics: ACL 2024, and it was posted on arXiv on June 23, 2024
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T04:39:44.855084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Confident Adaptive Language Modeling\" Schuster 2022 arXiv NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Confident Adaptive Language Modeling\" Schuster 2022 arXiv NeurIPS"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T04:39:44.855216+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Efficient Streaming Language Models with Attention Sinks\" Xiao 2024 arXiv 2309.17453"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Efficient Streaming Language Models with Attention Sinks\" Xiao 2024 arXiv 2309.17453"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T04:39:44.855501+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Extending Context Window of Large Language Models via Positional Interpolation\" Chen 2023 arXiv 2306.15595"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Extending Context Window of Large Language Models via Positional Interpolation\" Chen 2023 arXiv 2306.15595"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T04:39:44.855711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Style Amnesia\" \"Speaking Style Degradation\" \"Multi-Turn Spoken Language Models\" arXiv 2512"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Style Amnesia\" \"Speaking Style Degradation\" \"Multi-Turn Spoken Language Models\" arXiv 2512"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T04:39:44.855845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Llama 3 Herd of Models\" Grattafiori 2024 arXiv 2407.21783"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Llama 3 Herd of Models\" Grattafiori 2024 arXiv 2407.21783"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T04:39:44.855973+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Reassessing Layer Pruning in LLMs: New Insights and Methods\" arXiv 2411.15558 author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Reassessing Layer Pruning in LLMs: New Insights and Methods\" arXiv 2411.15558 author"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T04:39:44.856106+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"When Attention Closes\" Dongre 2026 arXiv 2605.12922 \"Multi-Turn\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"When Attention Closes\" Dongre 2026 arXiv 2605.12922 \"Multi-Turn\""
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T04:39:44.856254+00:00_

Web search results for query: ""Efficient Streaming Language Models with Attention Sinks" Xiao 2024 arXiv 2309.17453"

Links: [{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/html/2309.17453v4"},{"title":"[2309.17453v2] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453v2"},{"title":"[2309.17453v3] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453v3"},{"title":"[2309.17453v4] Efficient Streaming Language Models with Attention Sinks","url":"http://arxiv.org/abs/2309.17453v4"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"},{"title":"Efficient Streaming Language Models with Attention Sinks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230917453X/abstract"}]

I've found the paper you're searching for. Here are the key details:

**Paper Information:**
- **Title:** Efficient Streaming Language Models with Attention Sinks
- **Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis
- **ArXiv ID:** 2309.17453
- **Latest Version:** v4 (April 7, 2024)
- **Submitted:** September 29, 2023

**Main Focus:**
The paper addresses deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected. 

**Key Challenges Addressed:**
Firstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory. Secondly, popular LLMs cannot generalize to longer texts than the training sequence length.

**Proposed Solution:**
StreamingLLM is an efficient framework that enables LLMs trained with a finite length
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T04:39:44.856444+00:00_

Web search results for query: ""Confident Adaptive Language Modeling" Schuster 2022 arXiv NeurIPS"

Links: [{"title":"Confident Adaptive Language Modeling","url":"https://papers.neurips.cc/paper_files/paper/2022/file/6fac9e316a4ae75ea244ddcef1982c71-Paper-Conference.pdf"},{"title":"Confident Adaptive Language Modeling","url":"https://arxiv.org/pdf/2207.07061"},{"title":"[2207.07061] Confident Adaptive Language Modeling","url":"https://arxiv.org/abs/2207.07061"},{"title":"Confident Adaptive Language Modeling | Request PDF","url":"https://www.researchgate.net/publication/362011497_Confident_Adaptive_Language_Modeling"},{"title":"Accelerating text generation with Confident Adaptive Language Modeling (CALM)","url":"https://research.google/blog/accelerating-text-generation-with-confident-adaptive-language-modeling-calm/"},{"title":"Confident adaptive language modeling | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3601539"},{"title":"Confident Adaptive Language Modeling | OpenReview","url":"https://openreview.net/forum?id=uLYc4L3C81A"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Confident Adaptive Language Modeling" was presented at NeurIPS 2022

**Authors:** Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, and Donald Metzler

**arXiv ID:** The paper is available as arXiv paper 2207.07061

**Overview:** The paper introduces Confident Adaptive Language Modeling (CALM), a framework for dynamically allocating different amounts of compute per input and generation timestep. The method is motivated by the intuition that some next word predictions are easier than others, and CALM dynamically distributes computational effort across generation timesteps, generating text faster while preserving output quality by selectively allocating more computational resources only to harder predictions.

The paper addresses key c
…[truncated 238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T04:39:44.856631+00:00_

Web search results for query: ""Extending Context Window of Large Language Models via Positional Interpolation" Chen 2023 arXiv 2306.15595"

Links: [{"title":"GitHub - Math1019/Extend_Context_Window_Position_Interpolation: An overview of the Extending Context Window of Large Language Models via Positional Interpolation paper","url":"https://github.com/Math1019/Extend_Context_Window_Position_Interpolation"},{"title":"[2306.15595] Extending Context Window of Large Language Models via Positional Interpolation","url":"https://arxiv.org/abs/2306.15595"},{"title":"[PDF] Extending Context Window of Large Language Models via Positional Interpolation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Extending-Context-Window-of-Large-Language-Models-Chen-Wong/f5afaccfe90268485a9961c5771ec5e71e9b806c"},{"title":"(PDF) Extending Context Window of Large Language Models via Positional Interpolation","url":"https://www.researchgate.net/publication/371909431_Extending_Context_Window_of_Large_Language_Models_via_Positional_Interpolation"},{"title":"[2306.15595] Extending Context Window of Large Language Models via Position Interpolation","url":"https://ar5iv.labs.arxiv.org/html/2306.15595"},{"title":"Extending Context Window of Large Language Models via Position Interpolation","url":"https://arxiv.org/html/2306.15595"},{"title":"Paper page - Extending Context Window of Large Language Models via Positional Interpolation","url":"https://huggingface.co/papers/2306.15595"},{"title":"EXTENDING CONTEXT WINDOW OF LARGE LAN- GUAGE MODELS VIA POSITION INTERPOLATION","url":"https://arxiv.org/pdf/2306.15595"}]

I found the paper! Here's what I discovered about "Extending Context Window of Large Language Models via Positional Interpolation":

**Paper Details:**
- Authors: Chen, S., Wong, S., Chen, L., & Tian, Y.
- Published: June 27, 2023 (arXiv:2306.15595)
- All authors are from Meta Platforms Inc.

**Main Contribution:**
The paper presents Position Interpolation (PI) that exten
…[truncated 965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T04:39:44.856791+00:00_

Web search results for query: ""Reassessing Layer Pruning in LLMs: New Insights and Methods" arXiv 2411.15558 author"

Links: [{"title":"[2411.15558v1] Reassessing Layer Pruning in LLMs: New Insights and Methods","url":"https://arxiv.org/abs/2411.15558v1"},{"title":"[2411.15558] Reassessing Layer Pruning in LLMs: New Insights and Methods","url":"https://arxiv.org/abs/2411.15558"},{"title":"Computer Science Nov 2024","url":"https://arxiv.org/list/cs/2024-11?skip=6800&show=500"},{"title":"Work in Progress REASSESSING LAYER PRUNING IN LLMS: NEW INSIGHTS AND METHODS","url":"https://arxiv.org/pdf/2411.15558"},{"title":"Machine Learning Nov 2024","url":"https://www.arxiv.org/list/cs.LG/2024-11?skip=1225&show=250"},{"title":"Common-token Optimized Model Pruning Across Channels ...","url":"https://arxiv.org/pdf/2509.06836"},{"title":"Reassessing Layer Pruning in LLMs: New Insights and Methods | Request PDF","url":"https://www.researchgate.net/publication/386112944_Reassessing_Layer_Pruning_in_LLMs_New_Insights_and_Methods"}]

Based on the search results, I found the paper "Reassessing Layer Pruning in LLMs: New Insights and Methods" (arXiv 2411.15558). 

The authors of this paper are: Yao Lu, Hao Cheng, Yujie Fang, Zeyu Wang, Jiaheng Wei, Dongwei Xu, Qi Xuan, Xiaoniu Yang, and Zhaowei Zhu.

The paper was published on November 23, 2024, and addresses best practices for layer pruning in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T04:39:44.856953+00:00_

Web search results for query: ""Style Amnesia" "Speaking Style Degradation" "Multi-Turn Spoken Language Models" arXiv 2512"

Links: [{"title":"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.23578"},{"title":"[2512.23578] Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models","url":"https://arxiv.org/abs/2512.23578"},{"title":"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models","url":"https://arxiv.org/pdf/2512.23578"},{"title":"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models","url":"https://arxiv.org/html/2512.23578v3"},{"title":"StyleBench: Evaluating Speech Language Models on Conversational Speaking Style Control","url":"https://arxiv.org/pdf/2603.07599"}]

Based on the search results, I found the paper you're looking for:

"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models" is authored by Yu-Xiang Lin, Cheng-Han Chiang, and Hung-yi Lee from National Taiwan University.

The paper demonstrates that when spoken language models (SLMs) are instructed to speak in a specific speaking style at the beginning of a multi-turn conversation, they cannot maintain the required speaking styles after several turns of interaction. The researchers focus on paralinguistic speaking styles, including emotion, accent, volume, and speaking speed.

The research evaluates three proprietary and two open-source SLMs, showing that none of these models can maintain a consistent speaking style when instructed to do so. However, explicitly asking the model to recall the style instruction can partially mitigate style amnesia.

The paper is available on arXiv with identifier 2512.23578 and was published in early January 2026.


REMINDER: You MUST include 
…[truncated 73 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-22T04:39:44.857206+00:00_

Web search results for query: ""The Llama 3 Herd of Models" Grattafiori 2024 arXiv 2407.21783"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://arxiv.org/pdf/2407.21783"}]

I found the paper you're looking for! Here's what I found:

**"The Llama 3 Herd of Models"** by Aaron Grattafiori and 558 other authors (arXiv 2407.21783) is a research paper about Meta's Llama 3 language models.

Key details about the paper:

- **Release date:** The paper was submitted on July 31, 2024, with the latest version (v3) revised on November 23, 2024
- **Main contribution:** The paper presents a new set of foundation models called Llama 3, a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.

- **Model specifications:** The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.

- **Performance:** Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.

- **Additional capabilities:** The paper also presents the results of experiments in which we integrate image, video, and speec
…[truncated 425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T04:39:44.857678+00:00_

Web search results for query: ""When Attention Closes" Dongre 2026 arXiv 2605.12922 "Multi-Turn""

Links: [{"title":"[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/abs/2605.12922"},{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"LoopServe: An Adaptive Dual-phase LLM Inference Acceleration System for Multi-Turn Dialogues","url":"https://arxiv.org/pdf/2507.13681"},{"title":"Evaluating and Improving Context Attention Distribution on Multi-Turn   Response Generation using Self-Contained Distractions","url":"https://arxiv.org/pdf/2211.04943"},{"title":"A Static and Dynamic Attention Framework for Multi Turn Dialogue   Generation","url":"https://arxiv.org/pdf/2410.20766"}]

Based on the search results, I found the paper you're looking for:

"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction" is an arXiv paper (2605.12922) submitted on May 13, 2026, authored by Vardhan Dongre and 5 other authors.

The paper addresses how large language models can follow complex instructions in a single turn, yet over long multi-turn interactions they often lose the thread of instructions, persona, and rules. The authors propose a channel-transition account: goal-defining tokens become less accessible through attention, while goal-related information may persist in residual representations.

They introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens, and combine it with sliding-window ablations and residual-stream probes. Across architectures, the transition yields qualitatively distinct failure modes: some models preserve goal-conditioned behavior at vanishing attention, others fail despite decodable residual goal information, and the layer at which this encoding emerges varies from 2 to 27.


REMINDER: You MUST include the sources above in your respo
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T04:39:44.857936+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "0",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "0",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T04:39:44.858109+00:00_

paper/sections/analysis.tex:22:[Omitted long matching line]
paper/sections/analysis.tex:39:[Omitted long matching line]
paper/sections/analysis.tex:53:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:7:ReZero \citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \citep{fan2020layerdrop}, Mixture-of-Depths \citep{raposo2024mixture}, FlexiDepth \citep{luo2025flexidepth}, and CALM \citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.
paper/sections/related_work.tex:10:[Omitted long matching line]
paper/sections/related_work.tex:13:GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.
paper/sections/related_work.tex:16:[Omitted long matching line]
paper/sections/experiments.tex:8:[Omitted long matching line]
paper/sections/experiments.tex:14:[Omitted long matching line]
paper/sections/experiments.tex:21:\caption{Five-way comparison on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All four fine-tuned variants converge to within 0.75\,pp on GAR-ours; PPL is indistinguishable. GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
paper/sections/discussion.tex:5:[Omitted long matching line]
paper/sections/discussion.tex:9:TRC analysis (\S\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence
…[truncated 1504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T04:39:44.858274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T04:39:44.858574+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step causal chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through a causal exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resultin
…[truncated 7976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T04:39:44.858762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T04:39:44.858931+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual updat
…[truncated 4682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T04:39:44.859077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T04:39:44.859226+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{levy2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Residual gating and adaptive depth.}
7	ReZero \citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \citep{fan2020layerdrop}, Mixture-of-Depths \citep{raposo2024mixture}, FlexiDepth \citep{luo2025flexidepth}, and CALM \citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.
8	
9	\paragraph{Attention manipulation.}
10	StreamingLLM \citep{xiao2024streaming} identified attention sinks and proposed anchor token retention; \citet{ko2024found} showed positio
…[truncated 2134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T04:39:44.859389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T04:39:44.859579+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is the proximal cause (\S\ref{subsec:steering}).
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36). GAR-Dongre also rises (0.019$\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: $\beta$\,=\,5 achieves the strongest GAR recovery but incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (PPL +9\%). Scheduled sampling incurs no fluency cost but requires retraining. A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR\,=\,0.418 (gap 1.20$\times$), versus 5\% seed variance in standard ThreadGate training, suggesting that early scheduled sampling exposure---before the model consolidates teacher-forced attention patterns---may further compress the gap; systematic schedule ablation is deferred.
6	
7	\paragraph{Instruction retention under steering.} Across 18 system-prompt constraint types, $\beta$\,=\,3 steering increases content constraint compliance by +23.8\,pp (GAR-compliance $r$\,=\,0.200, $p$\,=\,0.007; McNemar $p$\,=\,0.077), providing exploratory evidence for downstream benefit pending multi-model confirmation.
8	
9	TRC analysis (\S\ref{subsec:mechanism-specificity}) confirm
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T04:39:44.859735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T04:39:44.859883+00:00_

1	\section{Background}\label{sec:background}
2	
3	\paragraph{Goal Attention Ratio.}
4	Multi-turn instruction-following models receive a system prompt that specifies the task objective. We denote the token subsequence corresponding to the task specification within this system prompt as the \emph{goal tokens} $\mathcal{G}$, excluding formatting markers and role tags. \citet{dongre2026attention} introduced the Goal Attention Ratio (GAR) to quantify how much attention a model allocates to these goal tokens during response generation. Given a model with $L$ layers and $H$ attention heads, GAR at conversation turn $\tau$ is
5	\begin{equation}\label{eq:gar}
6	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
7	\end{equation}
8	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$. This definition averages attention to goal tokens over all response positions, all layers, and all heads.
9	
10	\paragraph{Two GAR variants.}
11	We distinguish two measurement variants throughout this paper. \textbf{GAR-Dongre} refers to the original definition in Equation~\ref{eq:gar}, which averages over the full response token set $\mathcal{R}_\tau$. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
12	\begin{equation}\label{eq:gar-ours}
13	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
14	\end{equation}
15	where $t_\tau$ is the index of the last token in the assistant response at turn $\tau$. The last token is the position at which the model conditions its next generation step, so attention patterns at this position most directly reflect the information the model draws upon for continuation. We use GAR-ours as the optimiz
…[truncated 532 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reference_audit_20260522T042955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-22T04:39:44.860181+00:00_

所有数据收集完毕。下面是审计报告。

---

## 引用审计报告

**总数**: 46 条 bib 条目（22 条被引用，24 条 orphan）  
**真实性**: 22/22 被引用条目均为真实论文  
**格式问题**: 5 条需修复  
**结构问题**: 1 个重复 bib 文件

---

### A. 真实性验证

所有 22 条被引用条目通过 WebSearch 验证为真实论文，无幻觉引用。

OpenAlex 报告 3 条 `not_found`，均为索引问题而非真实性问题：

| Key | 原因 |
|-----|------|
| `fan2020layerdrop` | Fan, Grave, Joulin. ICLR 2020. OpenAlex 索引缺失，论文真实 |
| `luo2025flexidepth` | Xuan Luo et al. arXiv 2503.23798. OpenAlex 未收录，论文真实 |
| `elhage2021framework` | Elhage et al. Anthropic blog post，非正式论文，不在 OpenAlex 中 |

---

### B. 需修复的错误（5 条）

**1. [severity: critical] `levy2025lost` — 第一作者错误**
- bib 写 `Levy and others`，实际第一作者是 **Philippe Laban**
- 修复: `author = {Laban and others}`

**2. [severity: critical] `ko2024found` — 第一作者错误**
- bib 写 `Ko and others`，实际第一作者是 **Cheng-Yu Hsieh**
- 修复: `author = {Hsieh and others}`

**3. [severity: warning] `anonymous2024reassessing` — 应使用真实作者**
- 论文已公开，第一作者是 Yao Lu
- 修复: `author = {Lu and others}`

**4. [severity: warning] `anonymous2025style` — 应使用真实作者**
- 论文已公开，第一作者是 Yu-Xiang Lin
- 修复: `author = {Lin and others}`

**5. [severity: warning] `grattafiori2024llama3` — author 字段异常 + 缺 URL**
- `author = {Grattafiori and 1 others}` 中 `1 others` 非标准
- 修复: `author = {Grattafiori and others}`, 补 `url = {https://arxiv.org/abs/2407.21783}`

---

### C. 格式一致性

**Author 格式不统一**：部分条目列全部作者（如 `Bengio and Vinyals and Jaitly and Shazeer`），部分用 `Last and others`。建议统一为其中一种风格。当前引用的 22 条中：
- 全部作者列表: bengio2015scheduled, ranzato2016sequence, lamb2016professor, leblond2018searnn, he2019exposure, yu2020pcgrad, chen2018gradnorm, liu2021cagrad, navon2022nash, bachlechner2021rezero, dongre2026attention
- `and others` 缩写: 其余 11 条

**`he2019exposure` arXiv 标题变更**：arXiv 1905.10617 最新版标题改为 "Exposure Bias versus Self-Recovery..."，bib 中使用 v1 标题。如论文引用的是 v1 内容则可保留，否则建议更新。

---

### D. 完整性

**Missing（引用了但 bib 没有）**: 0 条

**Orphan（bib 有但未引用）**: 24 条

| 分类 | 条目 |
|------|------|
| Layer Importance | gromov2024deeper, men2024shortgpt, sun2025curse, anonymous2024reassessing |
| Multi-Turn | liu2023lost, anonymous2025style |
| Residual Gating | wang2018skipnet, lawson2025skip |
| Attention Manipulation | press2022alibi, chen2023positional, peng2024yarn, han2024lminfinite |
| Theoretical | elhage2021framework, elhage2022superposition, belrose2023tuned, yu2023residual, makkuva2025markov, ildiz2024markov |
| Benchmarks | zheng2023mtbench, chiang2024arena, dubois2024alpacaeval, lin2024wildbench, sirdeshmukh2025multichallenge |
| Residual Scaling | zhang2019fixup |

建议：删除 orphan 条目，或在正文中补充引用。

**重复 bib 文件**: `paper/sections/references.bib` 是 `paper/references.bib` 的副本。`main.tex` 只引用后者。建议删除 `paper/sections/references.bib` 以避免维护不一致。

---

### E. 修复优先级

1. **立即修复**: `levy2025lost` 和 `ko2024found` 的第一作者错误（reviewer 一查即发现）
2. **应修复**: anonymous 条目替换为真实作者、`grattafiori2024llama3` 格式修正
3. **建议修复**: 清理 24 条 orphan 条目、统一 author 格式、删除重复 bib 文件

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_reference_audit_20260522T042955"
}
```

</details>

---
