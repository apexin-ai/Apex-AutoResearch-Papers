# paper writing method

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_writing_method_20260515T202140.jsonl`
- **Structured JSON:** [`db4c697560fc2146ccb4.json`](../../sessions/db/db4c697560fc2146ccb4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-15T20:24:33.899459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T20:24:33.900278+00:00_

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
…[truncated 2963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T20:24:33.900575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T20:24:33.901060+00:00_

1	---
2	name: red-section
3	description: "当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。"
4	always: true
5	roles:
6	  - agent
7	---
8	
9	# Red Section — Narrative Re-framing
10	
11	## 什么时候用
12	- 实验 conclusion = negative
13	- 审稿人指出 core claim 不成立
14	- 写论文前（作为通用写作规范）
15	
16	## Negative 结果的正确心态
17	"不是失败，是发现了 X"。你的输出应该是 framing 调整提案，而不是 failure report。
18	
19	## 产出格式
20	
21	### Framing 调整提案模板
22	1. 原 claim：什么
23	2. 实验结果：什么（客观数字，不加修饰）
24	3. 重新审视：
25	   - 这个结果挑战了哪个 hypothesis？
26	   - 是否暴露了被忽略的变量？
27	   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？
28	4. 新的 narrative 骨架（3 种备选，供 Director 选）
29	5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）
30	6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）
31	
32	### 写作规范（所有写作场景通用）
33	- 禁止 cherry-picking
34	- 所有数字必须追溯到 registry
35	- 强度与 evidence 匹配（1 个数据集 → 不能说 "consistently"）
36	- 每个定量 claim 必须附 exp_id
37	- 限制强度词（"significantly" 必须有统计检验）
38	
39	### 审稿攻击面预演
40	- 这个 section 最容易被审稿人攻击的点
41	- 预写 rebuttal 要点
42	
43	## 输出给谁
44	- Framing 调整提案 → Main Agent 向 Director 汇报
45	- 写作 skill 合规检查 → Reviewer 审查时验证
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T20:24:33.901325+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_registry,read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_registry,read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T20:24:33.901528+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:24:33.901750+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T20:24:33.901990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T20:24:33.902207+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "provenance_weight_training",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "provenance_weight_training",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T20:24:33.903008+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"grid_b_low_seed42_r2\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-15T20:19:36.129Z\", \"updated_at\": \"2026-05-15T20:20:14.302Z\", \"hypothesis\": \"Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. Confirms behavior in b<0.5 region — expect minimal reweighting effect and PPL close to uniform. Establishes that b=0.5 is already near the lower useful bound.\", \"parent\": \"grid_b_seed42_batch\"}, \"contamination_60_grid_b0_5_seed42\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-15T20:19:25.407Z\", \"updated_at\": \"2026-05-15T20:20:13.344Z\", \"hypothesis\": \"ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.\", \"parent\": \"grid_b0_5_seed456\"}, \"contamination_60_uniform_seed42\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-15T20:19:24.785Z\", \"updated_at\": \"2026-05-15T20:20:12.387Z\", \"hypothesis\": \"ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\", \"parent\": \"uniform_seed42\"}, \"contamination_60_seed42\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-15T20:12:18.751Z\", \"updated_at\": \"2026-05-15T20:12:29.051Z\", \"hypothesis\": \"ρ=0.6 contamination robustness test: adaptive weighting (τ=0.8, n_min=2) on higher contamination ratio data. Baseline adaptive_fix_seed42 (ρ=0.4) PPL=17.6527. Tests if adaptive method degrades gracefully as contamination increases from 0.4→0.6.\", \"parent\": \"adaptive_fix_seed42\", \"notes\": \"数据验证通过: scored_data_60.jsonl 371,499行/907MB, synthetic=222900/human=148599, actual ρ=0.6。q_score: mean=0.6243, std=0.3703, median=0.7753。字段: text/depth/source_model/prompt_tokens/generated_tokens/decoding/q_score。符号链接 scored_data_rho06.jsonl → scored_data_60.jsonl。配置基于 adaptive_fix_seed42，改 d
…[truncated 30963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T20:24:33.903289+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T20:24:33.903662+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 propor
…[truncated 10140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T20:24:33.903963+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "writing_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "writing_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T20:24:33.904521+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml\", \"content\": \"# Writing Plan — provenance_weight_training\\n# Generated: 2026-05-15\\n# Contract for downstream writing Workers\\n\\nvenue: EMNLP 2026 ARR May 25\\ndeadline: 2026-05-25\\npage_limit: 8 (+ unlimited appendix)\\n\\ntitle: \\\"Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\\\"\\n# 备选:\\n# - \\\"Dual-Constrained Adaptive Reweighting for Pretraining on Contaminated Web Corpora\\\"\\n# - \\\"How Much to Downweight? Principled Exponent Selection for Contamination-Aware Pretraining\\\"\\n\\nabstract_outline:\\n  - sentence_1: \\\"Web pretraining corpora contain 20–60% machine-generated text of unknown provenance, and naive training on such mixtures degrades model quality (model collapse).\\\"\\n  - sentence_2: \\\"Existing detect-and-reweight methods (Drayson et al., 2025) require per-model validation-based grid search over the weighting exponent b, which is expensive and fragile.\\\"\\n  - sentence_3: \\\"We propose a dual-constrained adaptive b* that jointly enforces a quality lower bound (α_eff ≥ τ) and a stability upper bound (ESS ≥ n_min), yielding the minimum intervention—the smallest b that achieves sufficient cleaning per batch, with zero validation cost.\\\"\\n  - sentence_4: \\\"On FineWeb with Qwen3-0.6B, adaptive b* matches grid-search-optimal performance within seed variance while eliminating 6× search cost, and outperforms both uniform training and the max-intervention (ESS-only) baseline.\\\"\\n\\n# ============================================================\\n# SECTIONS\\n# ============================================================\\n\\nsections:\\n\\n  introduction:\\n    target_pages: 1.0\\n    key_points:\\n      - \\\"Web corpora contamination is pervasive (20–60%) and growing; strong model collapse occurs even at low contamina
…[truncated 20970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T20:24:33.904817+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check main.tex and references",
  "subagent_type": "Explore",
  "prompt": "Find and read the main.tex file for the paper in /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/. I need to see:\n1. What LaTeX commands are defined (especially \\bstar, \\aeff, \\nmin, \\btau, \\bess and any theorem/proposition environments)\n2. What packages are loaded (especially algorithm-related packages)\n3. How the method section is included\n\nAlso check if references.bib exists and find the citation keys for: drayson2025detection, wang2026survive, vehtari2024psis (or similar keys). Report exact keys found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Agent",
  "tool_args": {
    "description": "Check main.tex and references",
    "subagent_type": "Explore",
    "prompt": "Find and read the main.tex file for the paper in /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/. I need to see:\n1. What LaTeX commands are defined (especially \\bstar, \\aeff, \\nmin, \\btau, \\bess and any theorem/proposition environments)\n2. What packages are loaded (especially algorithm-related packages)\n3. How the method section is included\n\nAlso check if references.bib exists and find the citation keys for: drayson2025detection, wang2026survive, vehtari2024psis (or similar keys). Report exact keys found."
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T20:24:33.905118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T20:24:33.905442+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{hyperref}
19	
20	\newtheorem{proposition}{Proposition}
21	\newtheorem{definition}{Definition}
22	
23	\newcommand{\bstar}{b^*}
24	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
25	\newcommand{\nmin}{n_{\min}}
26	\newcommand{\btau}{b_{\tau}}
27	\newcommand{\bess}{b_{\mathrm{ESS}}}
28	
29	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	\begin{abstract}
37	\input{sections/abstract}
38	\end{abstract}
39	
40	\section{Introduction}
41	\label{sec:intro}
42	\input{sections/introduction}
43	
44	\section{Related Work}
45	\label{sec:related}
46	\input{sections/related_work}
47	
48	\section{Method}
49	\label{sec:method}
50	\input{sections/method}
51	
52	\section{Experimental Setup}
53	\label{sec:experiments}
54	\input{sections/experiments}
55	
56	\section{Results}
57	\label{sec:results}
58	\input{sections/results}
59	
60	\section{Discussion}
61	\label{sec:discussion}
62	\input{sections/discussion}
63	
64	\section{Conclusion}
65	\label{sec:conclusion}
66	\input{sections/conclusion}
67	
68	\section*{Limitations}
69	\label{sec:limitations}
70	\input{sections/limitations}
71	
72	\bibliography{references}
73	\bibliographystyle{acl_natbib}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T20:24:33.905673+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/*.bib"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T20:24:33.905884+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T20:24:33.906108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T20:24:33.906338+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 3774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T20:24:33.906630+00:00_

Perfect! I found all the information you requested. Here's a comprehensive summary:

## Summary of main.tex Analysis

### LaTeX Commands Defined (Lines 23-27)
All the commands you asked about are defined:
- `\bstar` → `b^*`
- `\aeff` → `\alpha_{\mathrm{eff}}`
- `\nmin` → `n_{\min}`
- `\btau` → `b_{\tau}`
- `\bess` → `b_{\mathrm{ESS}}`

### Theorem/Proposition Environments (Lines 20-21)
- `\newtheorem{proposition}{Proposition}`
- `\newtheorem{definition}{Definition}`

### Loaded Packages (Lines 2-18)
Key algorithm-related packages:
- `algorithm` (line 13)
- `algorithmic` (line 14)

Other notable packages:
- acl (review style)
- amsmath, amssymb, amsthm (math)
- graphicx, xcolor, hyperref
- booktabs, multirow (tables)
- times, latexsym, fontenc, inputenc, microtype, inconsolata

### Method Section Inclusion (Lines 48-50)
```latex
\section{Method}
\label{sec:method}
\input{sections/method}
```

The method content is included via `\input{sections/method}`.

### Citation Keys Found in references.bib
All three citations you requested were found with exact keys:
1. **drayson2025detection** (line 4) - "Machine-Generated Text Detection Prevents Language Model Collapse"
2. **wang2026survive** (line 18) - "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training"
3. **vehtari2024psis** (line 41) - "Pareto Smoothed Importance Sampling"

The bibliography file contains 19 references total in alphabetical order by key, using `acl_natbib` style as specified in main.tex (line 73).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T20:24:33.906943+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if sections directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if sections directory exists"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T20:24:33.907177+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 15 20:19 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 15 20:20 ..
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 method.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu    0 May 15 20:19 results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T20:24:33.907393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T20:24:33.907600+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T20:24:33.907901+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex",
  "content": "% Method section — do not add \\section{Method} here (already in main.tex)\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\mathcal{D} = \\{x_1, \\dots, x_N\\}$ denote a pretraining corpus drawn from a mixture of human-written text $\\mathcal{D}_{\\text{real}}$ and machine-generated text $\\mathcal{D}_{\\text{synth}}$, with unknown mixing proportion.\nA pretrained detector assigns each sample a synthetic probability $q(x) \\in [0,1]$, where higher values indicate greater likelihood of machine origin.\nFollowing \\citet{drayson2025detection}, we define the sample weight as\n\\begin{equation}\n  w(x) = (1 - q(x))^b, \\quad b \\geq 0,\n  \\label{eq:weight}\n\\end{equation}\nwhere $b$ controls the strength of downweighting: $b=0$ recovers uniform training, while large $b$ aggressively suppresses samples with high $q(x)$.\n\n\\citet{drayson2025detection} treat $b$ as a hyperparameter selected via per-model validation grid search.\nThis is costly---their reported optima range from $b=1$ (SmolLM-1.7B) to $b=10$ (GPT-2 124M)---and requires a clean validation set that may not be available at web scale.\nWe seek instead to \\emph{derive} $b$ per batch from the detector scores alone, without validation.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual_constraint}\n\nWe introduce two batch-level diagnostics that together determine the operating point for $b$.\n\n\\paragraph{Effective real proportion.}\nGiven a batch $\\{x_1, \\dots, x_B\\}$ with binary provenance labels $r_i \\in \\{0,1\\}$ (available from the detector at training time via thresholding or, more generally, as soft labels), the \\emph{effective real proportion} under exponent $b$ is\n\\begin{equation}\n  \\aeff(b) \\;=\\; \\frac{\\sum_{i=1}^{B} w_i(b) \\cdot r_i}{\\sum_{i=1}^{B} w_i(b)},\n  \\label{eq:alpha_eff}\n\\end{equation}\nwhere $w_i(b) = (1 - q_i)^b$.\nIntuitively, $\\aeff$ measures the fraction of effective gradient signal attributable to real data after reweighting.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size \\citep{vehtari2024psis} quantifies the concentration of the weight distribution:\n\\begin{equation}\n  \\mathrm{ESS}(b) \\;=\\; \\frac{\\bigl(\\sum_{i=1}^{B} w_i(b)\\bigr)^2}{\\sum_{i=1}^{B} w_i(b)^2}.\n  \\label{eq:ess}\n\\end{equation}\n$\\mathrm{ESS}(b) = B$ when all weights are equal (uniform) and approaches $1$ when a single sample dominates.\n\nThe following monotonicity properties are central to our framework.\n\n\\begin{proposition}[Monotonicity of $\\aeff$]\n\\label{prop:alpha_mono}\n$\\aeff(b)$ is monotonically non-decreasing in $b$, and strictly increasing whenever the detector assigns different score distributions to real and synthetic samples.\n\\end{proposition}\n\n\\emph{Proof sketch.}\nLet $s_i = \\ln(1 - q_i) \\leq 0$. Then $\\frac{dw_i}{db} = w_i \\cdot s_i$, and the quotient rule gives\n\\begin{equation}\n  \\frac{d\\aeff}{db} = \\mathrm{Cov}_w(r,\\, s),\n  \\label{eq:dalpha}\n\\end{equation}\nwhere $\\mathrm{Cov}_w$ denotes the covariance under the normalized weight distribution $\\tilde{w}_i = w_i / \\sum_j w_j$.\nReal samples ($r_i = 1$) tend to have lower $q_i$, hence larger $s_i = \\ln(1-q_i)$; synthetic samples ($r_i = 0$) have higher $q_i$ and more negative $s_i$.\nThus $r$ and $s$ are positively correlated, giving $\\mathrm{Cov}_w(r, s) \\geq 0$ with equality only when the detector is uninformative. \\qed\n\n\\begin{proposition}[Monotonicity of ESS]\n\\label{prop:ess_mono}\n$\\mathrm{ESS}(b)$ is monotonically non-increasing in $b$ for $b \\geq 0$.\n\\end{proposition}\n\n\\emph{Proof sketch.}\nIncreasing $b$ multiplies each weight by $(1-q_i)^{\\Delta b}$, a factor that varies across samples.\nThis multiplicative rescaling increases the coefficient of variation of the weight distribution, which by the Cauchy--Schwarz characterization of ESS implies $\\mathrm{ESS}$ cannot increase. \\qed\n\n\\paragraph{Quality constraint.}\nWe require that the effective real proportion meets a threshold $\\tau \\in (0,1]$:\n\\begin{equation}\n  \\aeff(b) \\geq \\tau.\n  \\label{eq:quality_constraint}\n\\end{equation}\nBy Proposition~\\ref{prop:alpha_mono}, this defines a \\emph{lower bound} $\\btau = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}$: the minimum exponent needed to achieve the quality floor.\n\n\\paragraph{Stability constraint.}\nWe require that the effective sample size does not fall below a minimum $\\nmin$:\n\\begin{equation}\n  \\mathrm{ESS}(b) \\geq \\nmin.\n  \\label{eq:stability_constraint}\n\\end{equation}\nBy Proposition~\\ref{prop:ess_mono}, this defines an \\emph{upper bound} $\\bess = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq \\nmin\\}$: the maximum exponent that preserves sufficient effective samples.\n\n\\paragraph{Minimum intervention principle.}\nThe optimal exponent is\n\\begin{equation}\n  \\bstar = \\btau \\quad \\text{subject to} \\quad \\mathrm{ESS}(\\bstar) \\geq \\nmin.\n  \\label{eq:bstar}\n\\end{equation}\nThat is, $\\bstar$ is the \\emph{smallest} $b$ satisfying the quality floor, provided the stability ceiling is not violated.\nThe rationale is conservative: imagine a dial controlling decontamination strength.\n$\\aeff$ specifies the minimum setting for adequate cleaning; ESS specifies the maximum before gradient signal degrades.\nWe select the minimum effective setting---enough cleaning, no more---thereby preserving the largest possible effective sample size.\n\nThis contrasts with an ESS-only strategy that selects $b = \\bess$ (the \\emph{largest} feasible exponent), which maximizes cleaning at the cost of discarding useful gradient signal from borderline samples.\nWe term this the \\emph{maximum intervention} baseline and compare against it empirically in Section~\\ref{sec:results}.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{Per-Batch Adaptive Exponent Selection}\n\\label{alg:bstar}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch scores $\\{q_1, \\dots, q_B\\}$, labels $\\{r_1, \\dots, r_B\\}$, threshold $\\tau$, ESS floor $\\nmin$, tolerance $\\varepsilon$, maximum exponent $b_{\\max}$\n\\ENSURE Optimal exponent $\\bstar$\n\\STATE $x_i \\leftarrow 1 - q_i$ for all $i$\n\\IF{$\\aeff(0) \\geq \\tau$}\n  \\STATE \\textbf{return} $\\bstar = 0$ \\hfill $\\triangleright$ Already clean\n\\ENDIF\n\\STATE $b_{\\text{lo}} \\leftarrow 0,\\; b_{\\text{hi}} \\leftarrow b_{\\max}$ \\hfill $\\triangleright$ Bisection for $\\btau$\n\\WHILE{$b_{\\text{hi}} - b_{\\text{lo}} > \\varepsilon$}\n  \\STATE $b_{\\text{mid}} \\leftarrow (b_{\\text{lo}} + b_{\\text{hi}}) / 2$\n  \\IF{$\\aeff(b_{\\text{mid}}) \\geq \\tau$}\n    \\STATE $b_{\\text{hi}} \\leftarrow b_{\\text{mid}}$\n  \\ELSE\n    \\STATE $b_{\\text{lo}} \\leftarrow b_{\\text{mid}}$\n  \\ENDIF\n\\ENDWHILE\n\\STATE $\\btau \\leftarrow b_{\\text{hi}}$\n\\IF{$\\mathrm{ESS}(\\btau) \\geq \\nmin$}\n  \\STATE \\textbf{return} $\\bstar = \\btau$ \\hfill $\\triangleright$ Quality-binding regime\n\\ENDIF\n\\STATE Find $\\bess = \\sup\\{b : \\mathrm{ESS}(b) \\geq \\nmin\\}$ via bisection \\hfill $\\triangleright$ Stability-binding regime\n\\STATE \\textbf{return} $\\bstar = \\bess$\n\\end{algorithmic}\n\\end{algorithm}\n\nAlgorithm~\\ref{alg:bstar} solves for $\\bstar$ via bisection on $\\aeff$, exploiting its monotonicity (Proposition~\\ref{prop:alpha_mono}) to guarantee convergence.\nEach batch falls into one of three regimes:\n\\begin{enumerate}\n  \\item \\textbf{Already clean} ($\\aeff(0) \\geq \\tau$): the batch is sufficiently real-dominated without reweighting; $\\bstar = 0$.\n  \\item \\textbf{Quality-binding} ($\\btau < \\bess$): the quality constraint determines $\\bstar = \\btau$, and the stability constraint is satisfied with margin.\n  \\item \\textbf{Stability-binding} ($\\btau \\geq \\bess$): the quality threshold cannot be reached without violating the ESS floor; $\\bstar = \\bess$ is the best feasible compromise.\n\\end{enumerate}\n\n\\paragraph{Implementation.}\nWe apply $\\bstar$ through \\emph{loss reweighting}: the per-sample loss is multiplied by $w_i(\\bstar)$ before gradient accumulation, yielding continuous gradient scaling.\nThis differs from the sampling-importance-resampling (SIR) approach of \\citet{drayson2025detection}, which discretely resamples the batch.\nLoss reweighting avoids the variance introduced by discrete resampling and integrates naturally with standard training loops.\n\n\\paragraph{Complexity.}\nEach bisection requires $O(\\log(b_{\\max}/\\varepsilon))$ evaluations of $\\aeff$ or ESS, each costing $O(B)$ for a batch of size $B$.\nThe total overhead per batch is $O(B \\log(b_{\\max}/\\varepsilon))$, which is negligible compared to the forward and backward passes through the model.\nIn practice, with $b_{\\max} = 20$ and $\\varepsilon = 0.01$, this amounts to ${\\sim}11$ iterations per batch.\n\n\\subsection{Hyperparameter Selection}\n\\label{sec:hyperparams}\n\nThe framework introduces two hyperparameters, $\\tau$ and $\\nmin$, which replace the single but sensitive exponent $b$ of prior work.\n\n\\paragraph{Quality threshold $\\tau$.}\nThe convergence analysis of \\citet{wang2026survive} shows that training on a mixture with effective real proportion $\\alpha$ yields convergence rates that improve with $\\alpha$, providing theoretical motivation for enforcing $\\aeff \\geq \\tau$.\nWhile that analysis assumes a known mixing proportion, $\\tau$ serves as a practical proxy: it specifies the minimum acceptable real-data contribution per batch without requiring knowledge of the global contamination rate.\nEmpirically, we find a wide safe range $\\tau \\in [0.5, 0.8]$ in which all settings improve over uniform training (Section~\\ref{sec:results}), with $\\tau = 0.8$ as the default.\nThe key asymmetry is that $\\tau$ values below the optimum yield mild degradation (the method under-cleans), while values above it cause sharper degradation as $\\bstar$ inflates and over-suppresses borderline samples.\n\n\\paragraph{ESS floor $\\nmin$.}\nWe set $\\nmin = 2$ (i.e., $B/2$ for batch size $B=4$) as the default.\nThis ensures at least two samples' worth of effective gradient signal per batch.\nSetting $\\nmin = 1$ effectively removes the stability constraint and leads to extreme $\\bstar$ values (mean $b^* = 7.2$, with 46.7\\% of batches hitting $b_{\\max}$), degrading performance.\nSetting $\\nmin \\geq B$ forces $\\bstar = 0$ for all batches, recovering uniform training.\nIn practice, $\\nmin \\in \\{2, 3\\}$ yields stable results across seeds.\n\n\\paragraph{Comparison with fixed $b$.}\nBoth $\\tau$ and $\\nmin$ admit principled defaults that transfer across settings without per-model tuning.\nIn contrast, the fixed exponent $b$ in \\citet{drayson2025detection} is a sensitive hyperparameter: optimal values span an order of magnitude across model scales (GPT-2 124M: $b{=}10$; SmolLM-1.7B: $b{=}1$), and selecting $b$ requires a validation set and grid search costing up to $6{\\times}$ the training budget.\nOur adaptive $\\bstar$ eliminates this cost entirely.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex",
    "content": "% Method section — do not add \\section{Method} here (already in main.tex)\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\mathcal{D} = \\{x_1, \\dots, x_N\\}$ denote a pretraining corpus drawn from a mixture of human-written text $\\mathcal{D}_{\\text{real}}$ and machine-generated text $\\mathcal{D}_{\\text{synth}}$, with unknown mixing proportion.\nA pretrained detector assigns each sample a synthetic probability $q(x) \\in [0,1]$, where higher values indicate greater likelihood of machine origin.\nFollowing \\citet{drayson2025detection}, we define the sample weight as\n\\begin{equation}\n  w(x) = (1 - q(x))^b, \\quad b \\geq 0,\n  \\label{eq:weight}\n\\end{equation}\nwhere $b$ controls the strength of downweighting: $b=0$ recovers uniform training, while large $b$ aggressively suppresses samples with high $q(x)$.\n\n\\citet{drayson2025detection} treat $b$ as a hyperparameter selected via per-model validation grid search.\nThis is costly---their reported optima range from $b=1$ (SmolLM-1.7B) to $b=10$ (GPT-2 124M)---and requires a clean validation set that may not be available at web scale.\nWe seek instead to \\emph{derive} $b$ per batch from the detector scores alone, without validation.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual_constraint}\n\nWe introduce two batch-level diagnostics that together determine the operating point for $b$.\n\n\\paragraph{Effective real proportion.}\nGiven a batch $\\{x_1, \\dots, x_B\\}$ with binary provenance labels $r_i \\in \\{0,1\\}$ (available from the detector at training time via thresholding or, more generally, as soft labels), the \\emph{effective real proportion} under exponent $b$ is\n\\begin{equation}\n  \\aeff(b) \\;=\\; \\frac{\\sum_{i=1}^{B} w_i(b) \\cdot r_i}{\\sum_{i=1}^{B} w_i(b)},\n  \\label{eq:alpha_eff}\n\\end{equation}\nwhere $w_i(b) = (1 - q_i)^b$.\nIntuitively, $\\aeff$ measures the fraction of effective gradient signal attributable to real data after reweighting.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size \\citep{vehtari2024psis} quantifies the concentration of the weight distribution:\n\\begin{equation}\n  \\mathrm{ESS}(b) \\;=\\; \\frac{\\bigl(\\sum_{i=1}^{B} w_i(b)\\bigr)^2}{\\sum_{i=1}^{B} w_i(b)^2}.\n  \\label{eq:ess}\n\\end{equation}\n$\\mathrm{ESS}(b) = B$ when all weights are equal (uniform) and approaches $1$ when a single sample dominates.\n\nThe following monotonicity properties are central to our framework.\n\n\\begin{proposition}[Monotonicity of $\\aeff$]\n\\label{prop:alpha_mono}\n$\\aeff(b)$ is monotonically non-decreasing in $b$, and strictly increasing whenever the detector assigns different score distributions to real and synthetic samples.\n\\end{proposition}\n\n\\emph{Proof sketch.}\nLet $s_i = \\ln(1 - q_i) \\leq 0$. Then $\\frac{dw_i}{db} = w_i \\cdot s_i$, and the quotient rule gives\n\\begin{equation}\n  \\frac{d\\aeff}{db} = \\mathrm{Cov}_w(r,\\, s),\n  \\label{eq:dalpha}\n\\end{equation}\nwhere $\\mathrm{Cov}_w$ denotes the covariance under the normalized weight distribution $\\tilde{w}_i = w_i / \\sum_j w_j$.\nReal samples ($r_i = 1$) tend to have lower $q_i$, hence larger $s_i = \\ln(1-q_i)$; synthetic samples ($r_i = 0$) have higher $q_i$ and more negative $s_i$.\nThus $r$ and $s$ are positively correlated, giving $\\mathrm{Cov}_w(r, s) \\geq 0$ with equality only when the detector is uninformative. \\qed\n\n\\begin{proposition}[Monotonicity of ESS]\n\\label{prop:ess_mono}\n$\\mathrm{ESS}(b)$ is monotonically non-increasing in $b$ for $b \\geq 0$.\n\\end{proposition}\n\n\\emph{Proof sketch.}\nIncreasing $b$ multiplies each weight by $(1-q_i)^{\\Delta b}$, a factor that varies across samples.\nThis multiplicative rescaling increases the coefficient of variation of the weight distribution, which by the Cauchy--Schwarz characterization of ESS implies $\\mathrm{ESS}$ cannot increase. \\qed\n\n\\paragraph{Quality constraint.}\nWe require that the effective real proportion meets a threshold $\\tau \\in (0,1]$:\n\\begin{equation}\n  \\aeff(b) \\geq \\tau.\n  \\label{eq:quality_constraint}\n\\end{equation}\nBy Proposition~\\ref{prop:alpha_mono}, this defines a \\emph{lower bound} $\\btau = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}$: the minimum exponent needed to achieve the quality floor.\n\n\\paragraph{Stability constraint.}\nWe require that the effective sample size does not fall below a minimum $\\nmin$:\n\\begin{equation}\n  \\mathrm{ESS}(b) \\geq \\nmin.\n  \\label{eq:stability_constraint}\n\\end{equation}\nBy Proposition~\\ref{prop:ess_mono}, this defines an \\emph{upper bound} $\\bess = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq \\nmin\\}$: the maximum exponent that preserves sufficient effective samples.\n\n\\paragraph{Minimum intervention principle.}\nThe optimal exponent is\n\\begin{equation}\n  \\bstar = \\btau \\quad \\text{subject to} \\quad \\mathrm{ESS}(\\bstar) \\geq \\nmin.\n  \\label{eq:bstar}\n\\end{equation}\nThat is, $\\bstar$ is the \\emph{smallest} $b$ satisfying the quality floor, provided the stability ceiling is not violated.\nThe rationale is conservative: imagine a dial controlling decontamination strength.\n$\\aeff$ specifies the minimum setting for adequate cleaning; ESS specifies the maximum before gradient signal degrades.\nWe select the minimum effective setting---enough cleaning, no more---thereby preserving the largest possible effective sample size.\n\nThis contrasts with an ESS-only strategy that selects $b = \\bess$ (the \\emph{largest} feasible exponent), which maximizes cleaning at the cost of discarding useful gradient signal from borderline samples.\nWe term this the \\emph{maximum intervention} baseline and compare against it empirically in Section~\\ref{sec:results}.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{Per-Batch Adaptive Exponent Selection}\n\\label{alg:bstar}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch scores $\\{q_1, \\dots, q_B\\}$, labels $\\{r_1, \\dots, r_B\\}$, threshold $\\tau$, ESS floor $\\nmin$, tolerance $\\varepsilon$, maximum exponent $b_{\\max}$\n\\ENSURE Optimal exponent $\\bstar$\n\\STATE $x_i \\leftarrow 1 - q_i$ for all $i$\n\\IF{$\\aeff(0) \\geq \\tau$}\n  \\STATE \\textbf{return} $\\bstar = 0$ \\hfill $\\triangleright$ Already clean\n\\ENDIF\n\\STATE $b_{\\text{lo}} \\leftarrow 0,\\; b_{\\text{hi}} \\leftarrow b_{\\max}$ \\hfill $\\triangleright$ Bisection for $\\btau$\n\\WHILE{$b_{\\text{hi}} - b_{\\text{lo}} > \\varepsilon$}\n  \\STATE $b_{\\text{mid}} \\leftarrow (b_{\\text{lo}} + b_{\\text{hi}}) / 2$\n  \\IF{$\\aeff(b_{\\text{mid}}) \\geq \\tau$}\n    \\STATE $b_{\\text{hi}} \\leftarrow b_{\\text{mid}}$\n  \\ELSE\n    \\STATE $b_{\\text{lo}} \\leftarrow b_{\\text{mid}}$\n  \\ENDIF\n\\ENDWHILE\n\\STATE $\\btau \\leftarrow b_{\\text{hi}}$\n\\IF{$\\mathrm{ESS}(\\btau) \\geq \\nmin$}\n  \\STATE \\textbf{return} $\\bstar = \\btau$ \\hfill $\\triangleright$ Quality-binding regime\n\\ENDIF\n\\STATE Find $\\bess = \\sup\\{b : \\mathrm{ESS}(b) \\geq \\nmin\\}$ via bisection \\hfill $\\triangleright$ Stability-binding regime\n\\STATE \\textbf{return} $\\bstar = \\bess$\n\\end{algorithmic}\n\\end{algorithm}\n\nAlgorithm~\\ref{alg:bstar} solves for $\\bstar$ via bisection on $\\aeff$, exploiting its monotonicity (Proposition~\\ref{prop:alpha_mono}) to guarantee convergence.\nEach batch falls into one of three regimes:\n\\begin{enumerate}\n  \\item \\textbf{Already clean} ($\\aeff(0) \\geq \\tau$): the batch is sufficiently real-dominated without reweighting; $\\bstar = 0$.\n  \\item \\textbf{Quality-binding} ($\\btau < \\bess$): the quality constraint determines $\\bstar = \\btau$, and the stability constraint is satisfied with margin.\n  \\item \\textbf{Stability-binding} ($\\btau \\geq \\bess$): the quality threshold cannot be reached without violating the ESS floor; $\\bstar = \\bess$ is the best feasible compromise.\n\\end{enumerate}\n\n\\paragraph{Implementation.}\nWe apply $\\bstar$ through \\emph{loss reweighting}: the per-sample loss is multiplied by $w_i(\\bstar)$ before gradient accumulation, yielding continuous gradient scaling.\nThis differs from the sampling-importance-resampling (SIR) approach of \\citet{drayson2025detection}, which discretely resamples the batch.\nLoss reweighting avoids the variance introduced by discrete resampling and integrates naturally with standard training loops.\n\n\\paragraph{Complexity.}\nEach bisection requires $O(\\log(b_{\\max}/\\varepsilon))$ evaluations of $\\aeff$ or ESS, each costing $O(B)$ for a batch of size $B$.\nThe total overhead per batch is $O(B \\log(b_{\\max}/\\varepsilon))$, which is negligible compared to the forward and backward passes through the model.\nIn practice, with $b_{\\max} = 20$ and $\\varepsilon = 0.01$, this amounts to ${\\sim}11$ iterations per batch.\n\n\\subsection{Hyperparameter Selection}\n\\label{sec:hyperparams}\n\nThe framework introduces two hyperparameters, $\\tau$ and $\\nmin$, which replace the single but sensitive exponent $b$ of prior work.\n\n\\paragraph{Quality threshold $\\tau$.}\nThe convergence analysis of \\citet{wang2026survive} shows that training on a mixture with effective real proportion $\\alpha$ yields convergence rates that improve with $\\alpha$, providing theoretical motivation for enforcing $\\aeff \\geq \\tau$.\nWhile that analysis assumes a known mixing proportion, $\\tau$ serves as a practical proxy: it specifies the minimum acceptable real-data contribution per batch without requiring knowledge of the global contamination rate.\nEmpirically, we find a wide safe range $\\tau \\in [0.5, 0.8]$ in which all settings improve over uniform training (Section~\\ref{sec:results}), with $\\tau = 0.8$ as the default.\nThe key asymmetry is that $\\tau$ values below the optimum yield mild degradation (the method under-cleans), while values above it cause sharper degradation as $\\bstar$ inflates and over-suppresses borderline samples.\n\n\\paragraph{ESS floor $\\nmin$.}\nWe set $\\nmin = 2$ (i.e., $B/2$ for batch size $B=4$) as the default.\nThis ensures at least two samples' worth of effective gradient signal per batch.\nSetting $\\nmin = 1$ effectively removes the stability constraint and leads to extreme $\\bstar$ values (mean $b^* = 7.2$, with 46.7\\% of batches hitting $b_{\\max}$), degrading performance.\nSetting $\\nmin \\geq B$ forces $\\bstar = 0$ for all batches, recovering uniform training.\nIn practice, $\\nmin \\in \\{2, 3\\}$ yields stable results across seeds.\n\n\\paragraph{Comparison with fixed $b$.}\nBoth $\\tau$ and $\\nmin$ admit principled defaults that transfer across settings without per-model tuning.\nIn contrast, the fixed exponent $b$ in \\citet{drayson2025detection} is a sensitive hyperparameter: optimal values span an order of magnitude across model scales (GPT-2 124M: $b{=}10$; SmolLM-1.7B: $b{=}1$), and selecting $b$ requires a validation set and grid search costing up to $6{\\times}$ the training budget.\nOur adaptive $\\bstar$ eliminates this cost entirely.\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T20:24:33.908373+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260515T202140",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T20:24:33.908642+00:00_

Method section 已写入 `sections/method.tex`。结构：

- **3.1 Problem Setup** — 语料定义、加权公式 (cite Drayson)、目标
- **3.2 Dual-Constraint Framework** — α_eff 和 ESS 定义，Proposition 1 (α_eff 单调递增，proof via Cov_w(r, ln(1-q)))，Proposition 2 (ESS 单调递减)，quality/stability 约束，最小干预原则，与 ESS-only 的对比
- **3.3 Algorithm** — Algorithm 1 伪代码 (bisection)，三种 regime，loss reweighting vs SIR，复杂度分析
- **3.4 Hyperparameter Selection** — τ 的理论 motivation + empirical safe range [0.5, 0.8]，n_min 的默认值和边界行为，与 Drayson 固定 b 的对比

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260515T202140"
}
```

</details>

---
