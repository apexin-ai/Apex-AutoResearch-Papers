# research paper plan

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_research_paper-plan_20260515T032552.jsonl`
- **Structured JSON:** [`89cb07ee7aff61533107.json`](../../sessions/89/89cb07ee7aff61533107.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T03:29:13.532299+00:00_

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
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T03:29:13.532879+00:00_

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
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T03:29:13.533059+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T03:29:13.533195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T03:29:13.533335+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T03:29:13.533556+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- Primary: AAAI 2027 (deadline: August 2, 2026)\\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **differential depth response**: **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **distributional shape features** (entropy_std, tail_decay) remain near-stationary. This differential response is consistent with recursive generation inducing a **location shift** in the NLL distribution — the text becomes progressively more predictable (mean shifts) while the functional form of the distribution is preserved (shape is invariant). The genuine novelty is not the drift/stationarity split per se (which follows from location-shift properties), but: (a) the **task formulation** (ordinal depth estimation beyond binary detection), (b) **empirical validation** across 5 generators / 3 model families showing this pattern is robust, (c) the practical consequence that combining both feature types yields **complementary signal** for depth classification (macro-F1 0.80 cross-generator, 0.77 cross-family).\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\\n\\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Depth-dependent features exhibit differential response: central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with dep
…[truncated 10455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T03:29:13.533737+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T03:29:13.533916+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md\", \"content\": \"# gen-depth-fingerprint — Memory\\n\\n## 关键发现\\n\\n### MVP-001 结果（2026-05-14）\\n- **PASS**: macro-F1=0.8408 (阈值 0.45), binary F1=0.8653 (阈值 0.65)\\n- 词汇多样性特征（hapax_ratio, ttr）区分力最强，feature importance 分别 0.30 和 0.17\\n- entropy_mean 是最强的模型级特征（importance 0.22）\\n- tail_decay 区分力最弱（importance 0.057），但仍统计显著\\n- gen-0 几乎完美分离（F1=0.95），gen-1 vs gen-2+ 有一定混淆（45 个 gen-2+ 误判为 gen-1）\\n- 深度衰减 17.4%：部分 continuation 产生空文本导致链条中断（995→822 from depth 0→4）\\n\\n### plan-001-fix 结果（2026-05-14）\\n- **Feature Complementarity 确认**: full(0.82) > surface(0.76) > reference(0.72)，bootstrap CI 不重叠\\n- **Dual Dynamics**: H2 drift 特征（entropy_mean, ttr, hapax_ratio）+ H1 stationary 特征（tail_decay, entropy_std, entropy_max）\\n- **Effect size 递减**: 漂移减速，gen-1→gen-2 entropy 跃迁最大\\n- **PPL 单调递减**: median 13.50→4.96→3.00→2.07→1.72，退化样本 <1%\\n\\n### plan-002 跨模型特征分析（2026-05-14）\\n- **Dual Dynamics 跨 5 个生成器全部成立**：H2 drift（entropy_mean↓1.40~1.65, ttr↓0.39~0.45, hapax↓0.38~0.43）方向一致\\n- **tail_decay 无区分力**：~-0.0023 恒定，跨深度跨模型不变\\n- **depth=0 时模型间无差异**（跨模型 std<0.002）——seed text 统计特性是模型无关的\\n- **衰减速率与模型规模相关**：pythia-1b↓1.65 > pythia-2.8b↓1.49 → 更大模型退化更慢（但非严格单调）\\n\\n### plan-002-eval 跨生成器分类（2026-05-14）\\n- **Leave-one-generator-out avg macro-F1 = 0.8037**，跨架构高度可迁移\\n- **Leave-one-family-out Δ = +0.0107**，Pythia vs 非 Pythia 几乎无差异\\n- **Feature complementarity 在跨生成器设置下确认**（McNemar p≈0）：full(0.80) > ref(0.75) > surf(0.75)\\n- **Permutation importance**: hapax_ratio(0.289) > ttr(0.168) > entropy_mean(0.160)，与 MVP 排序一致\\n- **entropy_std 结论：H1 near-stationary**，drift 仅 0.12（entropy_mean 的 1/12.5），去掉后 F1 仅降 0.005\\n\\n### plan-013 文本长度混淆控制（2026-05-14）\\n- **长度不是混淆因素**（三重证据）：\\n  1. 长度-深度相关性弱（|ρ|<0.14）\\n  2. 归一化 TTR/hapax 趋势不仅保留，ρ 绝对值反而增大\\n  3. 长度匹配分类器 F1 上升 +0.041\\n- **短文本更容易 dropout**（所有模型一致）——dropout 与生成质量相关，非随机\\n\\n### plan-003 跨家族参考模型验证（2026-05-15）\\
…[truncated 3253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T03:29:13.534068+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T03:29:13.535342+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan-014\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:12:01.909Z\", \"updated_at\": \"2026-05-15T03:25:14.290Z\", \"hypothesis\": \"大模型生成器：Qwen3-8B-Base (7B+) 的 continuation 链是否展现同样的 depth dynamics\", \"spec\": {\"command\": \"nohup /root/miniconda3/bin/python generate_chain.py --model-name qwen3-8b --model-path /root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base/ --input data/openwebtext_seeds.jsonl --shard-id 0 --num-shards 1 --device cuda:0 > /tmp/gen_large_model.log 2>&1 &\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 134817, \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 996, \"model_name\": \"Qwen3-8B-Base\", \"seed\": \"all\", \"log_path\": \"/tmp/gen_large_model.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-8b/generations_shard0.jsonl\", \"output_path\": \"data/qwen3-8b/generations_shard0.jsonl\", \"estimated_duration_h\": 4, \"model_params\": \"8.2B\", \"fp16_vram_gb\": 16.1}, \"notes\": \"2026-05-15 03:24: 修正诊断——之前报告的\\\"416行/87% skip\\\"是误判。真实情况：输出文件 inode 被删除，磁盘上只保留旧 416 行，但进程已实际写入 3362+ 行（~728 seeds, ~4.5 records/seed）。Worker 已从 /proc/134823/fd/50 恢复数据到 generations_shard0_recovered.jsonl，并启动 watchdog PID 163595 持续同步。进程 728/996 seeds (73%), ETA ~1h。预计最终 ~4500 行。\"}, \"plan-005\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:24:02.435Z\", \"updated_at\": \"2026-05-15T03:24:06.625Z\", \"hypothesis\": \"Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts\"}, \"plan-004-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:45:17.861Z\", \"updated_at\": \"2026-05-15T03:13:12.246Z\", \"hypothesis\": \"Downstream utility (retry): depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——5 variants × 3 seeds，输出到数据盘\", \"spec\": {\"command\
…[truncated 44122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T03:29:13.535634+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T03:29:13.536167+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml\", \"content\": \"# Literature Map for gen-depth-fingerprint\\n# 递归 LLM 生成链深度指纹识别\\n# Updated: 2026-05-15\\n# Categories: detection, model-collapse, data-quality, stylometry,\\n#             iterative-generation, watermarking, vocabulary-diversity,\\n#             membership-inference, ood-detection, survey\\n# Total: 39 papers\\n\\n##############################################################################\\n# 1. Perplexity-based / Zero-shot Detection\\n##############################################################################\\n\\n- id: detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Mitchell et al.\\\"\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  arxiv: \\\"2301.11305\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\\\"\\n  key_finding: \\\"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\\\"\\n\\n- id: gltr\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: \\\"Gehrmann et al.\\\"\\n  year: 2019\\n  venue: \\\"ACL 2019\\\"\\n  arxiv: \\\"1906.04043\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\\\"\\n  key_finding: \\\"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\\\"\\n\\n- id: dna_gpt\\n  title: \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\"\\n  authors: \\\"Yang et al.\\\"\\n  year: 2024\\n  venue: \\\"ICLR 2024\\\"\\n  arxiv: \\\"2305.17359\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\\\"\\n  key_finding: \\\"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\\\"\\n\\n- id: binoculars\\n  tit
…[truncated 17256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T03:29:13.536746+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "writing_plan.yaml",
  "content": "# Writing Plan — gen-depth-fingerprint\n# Depth Fingerprinting of Recursive LLM Generation Chains\n# Created: 2026-05-15\n\n##############################################################################\n# 1. Submission Target\n##############################################################################\n\nsubmission:\n  primary:\n    venue: AAAI 2027\n    deadline: 2026-08-02\n    page_limit: \"7 pages + 1 refs + unlimited appendix\"\n    template: aaai.sty\n    special_requirements:\n      - strict style compliance\n      - no modification of .sty\n  stretch:\n    venue: EMNLP 2026 ARR\n    deadline: 2026-05-25\n    page_limit: \"8 pages (long) + unlimited appendix\"\n    template: acl.sty\n    special_requirements:\n      - Limitations section (mandatory)\n      - Ethics Statement\n    scope_note: \"minimal — RQ1 (depth discriminability) + baseline comparison only\"\n  fallback:\n    - venue: ICLR 2027\n      deadline: 2026-09-24\n    - venue: NAACL 2027 ARR\n      deadline: 2026-10-16\n\n##############################################################################\n# 2. One-Sentence Contribution\n##############################################################################\n\none_sentence: >\n  We formulate ordinal depth estimation for recursive LLM generation chains,\n  showing that distributional features exhibit differential depth response\n  (central-tendency drifts, shape remains stationary), yielding a 7-feature\n  ensemble that reliably classifies generation depth (LOGO F1=0.80) across\n  5 generators / 3 model families.\n\n##############################################################################\n# 3. Claim-Evidence Map\n##############################################################################\n\nclaims:\n  C1_depth_discriminability:\n    claim: >\n      Distributional features under a held-out reference model classify\n      generation depth (gen-0/gen-1/gen-2+) with macro-F1 significantly\n      above chance, generalizing across unseen generators.\n    evidence:\n      - exp_id: plan-002-eval\n        metric: \"LOGO avg macro-F1 = 0.8037\"\n      - exp_id: plan-002-eval\n        metric: \"Leave-one-family-out Δ = +0.0107 (Pythia vs non-Pythia)\"\n      - exp_id: plan-015-v2\n        metric: \"Bootstrap CI [0.786, 0.799], p<0.001 vs all baselines\"\n      - exp_id: plan-013\n        metric: \"Length not a confound (|ρ|<0.14, normalized trends preserved)\"\n    tables: [Table 1, Table 2]\n    figures: [Fig 2, Fig 3]\n\n  C2_differential_response:\n    claim: >\n      Central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift\n      monotonically with depth; shape features (entropy_std, tail_decay) remain\n      near-stationary. Full 7-feature set significantly outperforms surface-only\n      and reference-only subsets.\n    evidence:\n      - exp_id: plan-001-fix\n        metric: \"full(0.82) > surface(0.76) > reference(0.72), CI non-overlapping\"\n      - exp_id: plan-002\n        metric: \"Drift direction consistent across all 5 generators\"\n      - exp_id: plan-002-eval\n        metric: \"full(0.80) > ref(0.75) = surf(0.75), McNemar p≈0\"\n      - exp_id: plan-003\n        metric: \"3 cross-family ref models: LOGO F1 0.80-0.82, drift direction consistent\"\n    tables: [Table 2]\n    figures: [Fig 1]\n\n  C3_downstream_negative:\n    claim: >\n      Depth-aware data curation does NOT improve downstream CLM quality.\n      Data quantity dominates depth composition. Depth fingerprinting is\n      diagnostic, not curative.\n    status: NEGATIVE FINDING — report honestly\n    evidence:\n      - exp_id: plan-004-v2\n        metric: \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\"\n      - exp_id: plan-004-v2\n        metric: \"15/15 runs, cross-seed variance <0.002\"\n    tables: [Table 3]\n    figures: [Fig 4]\n    framing_note: >\n      DO NOT hide or spin. Frame as: \"We tested whether depth-aware curation\n      improves downstream quality. It does not. The primary determinant is data\n      quantity, not depth composition. This positions depth fingerprinting as a\n      diagnostic tool for provenance characterization, not a curative tool for\n      data selection.\"\n\n##############################################################################\n# 4. Paper Outline\n##############################################################################\n\noutline:\n  abstract:\n    length: \"~200 words\"\n    structure: \"five-sentence method (Farquhar)\"\n    key_points:\n      - \"We formulate ordinal depth estimation beyond binary detection\"\n      - \"Why hard: existing detectors offer only real-vs-synthetic, no depth signal\"\n      - \"How: 7 distributional features exhibiting differential depth response\"\n      - \"Evidence: LOGO F1=0.80 across 5 generators / 3 families, p<0.001 vs baselines\"\n      - \"Honest negative: depth-aware curation does not improve downstream quality\"\n    headline_note: >\n      The paper_framing.md headline template contains \"Z% downstream\" placeholder.\n      UPDATE to negative-finding wording: \"...however, depth-aware data curation\n      does not improve downstream model quality over random subsampling,\n      positioning depth estimation as a diagnostic rather than curative tool.\"\n    reviewer_concerns_covered: []\n\n  introduction:\n    length: \"~1.5 pages\"\n    key_points:\n      - \"Problem: web data increasingly contains recursive LLM-generated text of unknown provenance depth\"\n      - \"Gap: binary detectors cannot distinguish gen-1 from gen-2+, forcing all-or-nothing filtering\"\n      - \"Our formulation: ordinal depth estimation as a new task (genuinely novel)\"\n      - \"Core finding: differential depth response — level/diversity features drift, shape features are stationary\"\n      - \"Practical consequence: 7-feature ensemble LOGO F1=0.80, reliable across unknown generators\"\n      - \"Honest reporting: downstream curation does not benefit (diagnostic, not curative)\"\n      - \"Contributions list (3 items matching the 3 claims)\"\n    evidence:\n      - exp_id: plan-015-v2  # headline numbers\n      - exp_id: plan-002-eval  # LOGO result\n    reviewer_concerns_covered: [RC8]\n    notes:\n      - \"Must explicitly state contribution is empirical/conceptual, not methodological (D006+D007)\"\n      - \"Connect to OOD detection literature in framing paragraph (RC8)\"\n      - \"Do NOT overclaim 'dual dynamics' — use 'differential depth response' (D007)\"\n\n  related_work:\n    length: \"~1 page\"\n    organization: # see literature_strategy section below\n      - subsection: \"AI-Generated Text Detection\"\n        papers: [detectgpt, gltr, dna_gpt, binoculars, fast_detectgpt, ld_score, intrinsic_dimension, diveye, generator_barrier, feat_aug_transformer, reliable_detection, paraphrase_evades, detection_possibilities, grover, release_strategies, jawahar_survey]\n        angle: \"Binary detection only — no depth estimation capability. Single-score baselines show high cross-generator variance.\"\n      - subsection: \"Model Collapse and Iterative Generation\"\n        papers: [self_consuming_mad, curse_of_recursion, strong_model_collapse, model_collapse_avoidable, broken_telephone, markovian_chains]\n        angle: \"Training-loop collapse theory; iterative generation distortion. We study inference-chain depth without retraining.\"\n      - subsection: \"Vocabulary Diversity and Stylometry\"\n        papers: [curious_decline, writing_diversity, nucleus_sampling, mapping_llm_science, monitoring_ai_review, stamatatos_survey, koppel_authorship, uchendu_attribution]\n        angle: \"Diversity decline documented but not used for depth estimation. Our surface features are stylometric in nature.\"\n      - subsection: \"Data Quality and Provenance\"\n        papers: [dsir, qurating, ccnet, watermark_llm, synthid_text, aaronson_watermark, chainwash, min_k_percent, ood_baseline]\n        angle: \"Quality scoring/watermarking for data curation. Depth fingerprint complements these as provenance signal.\"\n    reviewer_concerns_covered: [RC1, RC8]\n\n  method:\n    length: \"~1.5 pages\"\n    subsections:\n      - name: \"Task Formulation\"\n        content: \"Ordinal depth estimation: given text x, predict depth class {gen-0, gen-1, gen-2+}\"\n        length: \"~0.25 page\"\n      - name: \"Generation Chain Construction\"\n        content: \"5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B), 3 families, ~1000 seeds × 5 depths, continuation prompt, temp=0.7/top_p=0.9/max_tokens=256\"\n        evidence: [mvp-001, plan-002]\n        length: \"~0.25 page\"\n      - name: \"Feature Extraction\"\n        content: \"7 features: 4 reference-model (entropy_mean/std/max, tail_decay) + 3 surface (TTR, hapax_ratio, entropy_min). Reference model = Pythia-410M.\"\n        length: \"~0.5 page\"\n      - name: \"Evaluation Protocol\"\n        content: \"Leave-one-generator-out (LOGO) cross-validation. XGBoost classifier. Bootstrap CI (n=1000). McNemar test for feature ablation.\"\n        length: \"~0.5 page\"\n    reviewer_concerns_covered: [RC2, RC4, RC6]\n\n  results:\n    length: \"~2 pages\"\n    subsections:\n      - name: \"Depth Classification Performance (C1)\"\n        content: \"LOGO F1=0.80, per-generator breakdown, family-out Δ=+0.01. Gen-0 near-perfect (F1=0.95), gen-1 vs gen-2+ harder.\"\n        evidence: [plan-002-eval, plan-015-v2]\n        tables: [Table 1]\n        figures: [Fig 2]\n        length: \"~0.5 page\"\n      - name: \"Differential Depth Response (C2)\"\n        content: \"Feature drift patterns. entropy_mean/TTR/hapax drift monotonically. entropy_std/tail_decay near-stationary. Feature complementarity: full > surface = reference.\"\n        evidence: [plan-001-fix, plan-002, plan-003]\n        tables: [Table 2]\n        figures: [Fig 1]\n        length: \"~0.5 page\"\n      - name: \"Comparison with Detection Baselines\"\n        content: \"7-feature vs Avg-LogProb (+3.9pp, p<0.001), FastDetectGPT (+6.7pp), LD-Score, Binoculars. Key advantage: tight CI vs high variance of single detectors.\"\n        evidence: [plan-015-v2]\n        figures: [Fig 3]\n        length: \"~0.5 page\"\n      - name: \"Downstream Utility — Negative Finding (C3)\"\n        content: \"Depth-aware curation does not improve CLM quality. all(2.335) < size_matched(2.367) < depth01(2.387). Quantity dominates composition. Diagnostic not curative.\"\n        evidence: [plan-004-v2]\n        tables: [Table 3]\n        figures: [Fig 4]\n        length: \"~0.5 page\"\n    reviewer_concerns_covered: [RC1, RC2, RC10, RC11]\n\n  discussion:\n    length: \"~0.5 page\"\n    key_points:\n      - \"Why shape features are stationary: determined by sampling mechanism and architecture, invariant to input content drift (speculative, explicitly flagged)\"\n      - \"Practical implications: risk-stratified data curation (flag gen-2+ for review, keep gen-1)\"\n      - \"Honest framing of C3: negative finding has positive information value — rules out depth-based filtering as curation strategy\"\n      - \"Connection to model collapse literature: inference chains show similar distributional drift without retraining\"\n    reviewer_concerns_covered: [RC3, RC8]\n\n  limitations:\n    length: \"~0.25 page (mandatory for EMNLP; good practice for AAAI)\"\n    items:\n      - \"All generators ≤2.8B (plan-014 pending for 7B+); frontier models may compress depth signal\"\n      - \"Single prompt type (continuation); elaboration/rewriting chains not yet tested (plan-005 pending)\"\n      - \"Lab-constructed single-model chains; real web contamination involves diverse generators per step\"\n      - \"Negative downstream result tested on CLM only; other downstream tasks not evaluated\"\n      - \"3-class granularity; finer-grained depth may be possible for non-paraphrastic chains\"\n    reviewer_concerns_covered: [RC3, RC4, RC5, RC6, RC9]\n\n  conclusion:\n    length: \"~0.25 page\"\n    key_points:\n      - \"Restate contributions: task formulation, empirical characterization, honest negative on downstream\"\n      - \"Report realistic performance range (0.57-0.82 depending on conditions)\"\n      - \"Future work: frontier-scale generators, mixed-generator chains, prompt type diversity\"\n\n##############################################################################\n# 5. Figure Plan\n##############################################################################\n\nfigures:\n  fig1_differential_response:\n    title: \"Differential Depth Response of Distributional Features\"\n    type: \"multi-panel line plot (2×2 or 1×4)\"\n    data_source: plan-002 (features_all_models.csv)\n    content:\n      - \"Panel A: entropy_mean vs depth (5 generators, monotonic drift)\"\n      - \"Panel B: TTR or hapax_ratio vs depth (monotonic drift)\"\n      - \"Panel C: entropy_std vs depth (near-stationary)\"\n      - \"Panel D: tail_decay vs depth (near-stationary)\"\n    notes: \"Error bands = bootstrap 95% CI. Color-code by generator. This is the signature figure — spend time on it.\"\n    placement: \"Results §5.2\"\n    evidence: [plan-001-fix, plan-002]\n\n  fig2_logo_performance:\n    title: \"Leave-One-Generator-Out Classification Performance\"\n    type: \"grouped bar chart or radar\"\n    data_source: plan-002-eval (cross_generator_results.json)\n    content:\n      - \"Per held-out generator macro-F1 with CI\"\n      - \"Horizontal line at overall LOGO mean (0.80)\"\n      - \"Optional: per-class (gen-0/gen-1/gen-2+) breakdown\"\n    placement: \"Results §5.1\"\n    evidence: [plan-002-eval]\n\n  fig3_baseline_comparison:\n    title: \"Comparison with Single-Detector Baselines\"\n    type: \"forest plot or dot-with-CI\"\n    data_source: plan-015-v2 (detector_baseline_results.json)\n    content:\n      - \"7-feature ensemble: 0.798 [0.786, 0.799]\"\n      - \"Avg-LogProb: 0.765 [0.616, 0.820]\"\n      - \"LD-Score: 0.721 [0.588, 0.770]\"\n      - \"FastDetectGPT: 0.627 [0.511, 0.762]\"\n      - \"Binoculars: 0.579 [0.405, 0.664]\"\n    notes: \"Key message: ensemble has tight CI, single detectors have wide CI. Reliability advantage, not just mean.\"\n    placement: \"Results §5.3\"\n    evidence: [plan-015-v2]\n\n  fig4_downstream_negative:\n    title: \"Downstream CLM Perplexity by Data Curation Strategy\"\n    type: \"bar chart with error bars\"\n    data_source: plan-004-v2\n    content:\n      - \"5 variants: all / size_matched / depth01 / binary_filtered / depth0_only\"\n      - \"Y-axis: eval perplexity\"\n      - \"Error bars: 3-seed variance\"\n      - \"Annotation: data count per variant\"\n    notes: \"Frame as honest negative. Title should not hide the negative result.\"\n    placement: \"Results §5.4\"\n    evidence: [plan-004-v2]\n\n##############################################################################\n# 6. Table Plan\n##############################################################################\n\ntables:\n  table1_logo_results:\n    title: \"Leave-One-Generator-Out Depth Classification Results\"\n    placement: \"Results §5.1\"\n    columns: [\"Held-out Generator\", \"Family\", \"Params\", \"Macro-F1\", \"95% CI\"]\n    rows:\n      - [\"Pythia-2.8B\", \"Pythia\", \"2.8B\", \"—\", \"—\"]  # fill from data\n      - [\"Pythia-1B\", \"Pythia\", \"1.0B\", \"0.851\", \"—\"]\n      - [\"OLMo-2-1B\", \"OLMo\", \"1.5B\", \"0.752\", \"—\"]\n      - [\"Qwen3-1.7B\", \"Qwen\", \"1.7B\", \"—\", \"—\"]\n      - [\"Qwen3-0.6B\", \"Qwen\", \"0.6B\", \"—\", \"—\"]\n      - [\"**Average**\", \"\", \"\", \"**0.804**\", \"[0.786, 0.799]\"]\n    footer: \"Family-out Δ = +0.011 (Pythia-held-out vs non-Pythia-held-out)\"\n    evidence: [plan-002-eval, plan-015-v2]\n    notes: \"Fill exact per-generator CIs from bootstrap data\"\n\n  table2_feature_ablation:\n    title: \"Feature Group Ablation and Complementarity\"\n    placement: \"Results §5.2\"\n    columns: [\"Feature Set\", \"Features\", \"LOGO F1\", \"95% CI\", \"McNemar p\"]\n    rows:\n      - [\"Full (7 features)\", \"all\", \"0.804\", \"[0.786, 0.799]\", \"—\"]\n      - [\"Surface only\", \"TTR, hapax_ratio, entropy_min\", \"0.747\", \"—\", \"< 0.001\"]\n      - [\"Reference only\", \"entropy_mean/std/max, tail_decay\", \"0.754\", \"—\", \"< 0.001\"]\n    footer: \"Permutation importance: hapax_ratio(0.289) > ttr(0.168) > entropy_mean(0.160)\"\n    evidence: [plan-002-eval, plan-001-fix]\n\n  table3_downstream:\n    title: \"Downstream CLM Fine-tuning by Depth Curation Strategy\"\n    placement: \"Results §5.4\"\n    columns: [\"Curation Strategy\", \"Train Size\", \"Eval PPL (mean±std)\", \"Δ vs size_matched\"]\n    rows:\n      - [\"All depths (no filter)\", \"12,299\", \"2.335 ± 0.000\", \"-0.032\"]\n      - [\"Size-matched random\", \"3,951\", \"2.367 ± 0.000\", \"baseline\"]\n      - [\"Depth 0+1 only\", \"3,951\", \"2.387 ± 0.001\", \"+0.020\"]\n      - [\"Binary filtered\", \"3,951\", \"2.389 ± 0.000\", \"+0.022\"]\n      - [\"Depth 0 only\", \"797\", \"2.681 ± 0.001\", \"+0.314\"]\n    footer: >\n      OLMo-2-0425-1B, 3 seeds. Size-matched is the proper control.\n      Depth-aware curation does not outperform random subsampling at equal data count.\n    evidence: [plan-004-v2]\n\n  table4_cross_ref:\n    title: \"Cross-Family Reference Model Validation\"\n    placement: \"Appendix (or Results §5.2 if space)\"\n    columns: [\"Reference Model\", \"Family\", \"Params\", \"LOGO F1\", \"Entropy Drift Range\"]\n    rows:\n      - [\"Pythia-410M\", \"Pythia\", \"410M\", \"0.803\", \"[-1.19, -1.40]\"]\n      - [\"OLMo-2-1B\", \"OLMo\", \"1.5B\", \"0.807\", \"[-0.61, -0.91]\"]\n      - [\"Qwen3-0.6B\", \"Qwen\", \"0.6B\", \"0.816\", \"[-0.96, -1.35]\"]\n    footer: \"Drift direction consistent across all reference models; magnitude varies.\"\n    evidence: [plan-003]\n\n##############################################################################\n# 7. Literature Strategy\n##############################################################################\n\nliterature:\n  total_papers: 39\n  organization:\n    perplexity_detection:\n      papers: 16\n      key_refs: [detectgpt, fast_detectgpt, binoculars, ld_score, diveye, generator_barrier]\n      positioning: \"Binary detection paradigm. No depth estimation. High cross-generator variance when repurposed as ordinal predictors.\"\n    model_collapse:\n      papers: 4\n      key_refs: [curse_of_recursion, strong_model_collapse, self_consuming_mad]\n      positioning: \"Training-loop collapse. We study inference chains without retraining — distributional drift without model parameter change.\"\n    iterative_generation:\n      papers: 2\n      key_refs: [broken_telephone, markovian_chains]\n      positioning: \"Most directly related. broken_telephone: paraphrasing/translation chains. markovian_chains: convergence theory. We: non-paraphrastic continuation chains + depth estimation task.\"\n    vocabulary_diversity:\n      papers: 5\n      key_refs: [curious_decline, writing_diversity, nucleus_sampling]\n      positioning: \"Diversity decline documented in training loops. We show it appears in inference chains too and use it for depth classification.\"\n    stylometry:\n      papers: 3\n      key_refs: [stamatatos_survey, uchendu_attribution]\n      positioning: \"Feature set is essentially stylometric. We extend from source attribution to depth estimation.\"\n    data_quality:\n      papers: 3\n      key_refs: [dsir, qurating]\n      positioning: \"Data scoring/selection. Depth fingerprint as complementary provenance signal.\"\n    watermarking:\n      papers: 4\n      key_refs: [watermark_llm, chainwash]\n      positioning: \"Active signal embedding. We: passive post-hoc detection without watermark. chainwash motivates depth-aware approach — watermarks decay over generation steps.\"\n    membership_inference:\n      papers: 1\n      key_refs: [min_k_percent]\n      positioning: \"Probability distribution analysis for membership; we analyze for depth.\"\n    ood_detection:\n      papers: 1\n      key_refs: [ood_baseline]\n      positioning: \"Reference-model entropy features are functionally NLL-based OOD scores. Explicitly acknowledge this connection (RC8).\"\n\n##############################################################################\n# 8. Writing Order & Dependencies\n##############################################################################\n\nwriting_order:\n  phase1_skeleton:\n    deadline: \"2026-05-20\"\n    tasks:\n      - section: \"Results (§5)\"\n        reason: \"Anchor claims to evidence first. Numbers drive the narrative.\"\n        dependencies: []\n        priority: 1\n      - section: \"Method (§4)\"\n        reason: \"Experimental setup needed to interpret results.\"\n        dependencies: []\n        priority: 2\n      - section: \"Figures (all 4)\"\n        reason: \"Figures convey results more effectively than text. Generate early.\"\n        dependencies: [\"Results\"]\n        priority: 1\n\n  phase2_narrative:\n    deadline: \"2026-06-01\"\n    tasks:\n      - section: \"Introduction (§1)\"\n        reason: \"Story spine. Requires stable results to write convincingly.\"\n        dependencies: [\"Results\"]\n        priority: 1\n      - section: \"Related Work (§2)\"\n        reason: \"Positioning depends on knowing exact claims.\"\n        dependencies: [\"Introduction\"]\n        priority: 2\n      - section: \"Discussion + Limitations (§6)\"\n        reason: \"Interprets results, addresses reviewer concerns.\"\n        dependencies: [\"Results\"]\n        priority: 2\n\n  phase3_polish:\n    deadline: \"2026-06-15\"\n    tasks:\n      - section: \"Abstract\"\n        reason: \"Last written, first read. Needs stable claims.\"\n        dependencies: [\"Introduction\", \"Results\", \"Discussion\"]\n        priority: 1\n      - section: \"Conclusion\"\n        reason: \"Mirror of abstract with forward-looking additions.\"\n        dependencies: [\"Abstract\"]\n        priority: 2\n      - section: \"Title\"\n        reason: \"After all claims are finalized.\"\n        dependencies: [\"Abstract\"]\n        priority: 3\n\n  phase4_submission:\n    deadline: \"2026-07-15\"\n    tasks:\n      - \"Citation verification (reference-audit skill)\"\n      - \"Page limit compliance (7+1 for AAAI)\"\n      - \"Anonymization check\"\n      - \"Appendix organization (cross-ref table, length analysis, per-generator details)\"\n      - \"Paper checklist / Ethics statement\"\n\n##############################################################################\n# 9. Reviewer Concern Coverage Matrix\n##############################################################################\n\nreviewer_coverage:\n  RC1_vocabulary_impoverishment:\n    sections: [related_work, results]\n    evidence: [plan-002-eval]\n    response: \"Feature complementarity proven: full(0.80) > surface(0.75) = ref(0.75). Two groups capture different signal.\"\n\n  RC2_generalize_beyond_pythia:\n    sections: [method, results]\n    evidence: [plan-002, plan-002-eval, plan-003]\n    response: \"5 generators / 3 families. LOGO F1=0.80, family-out Δ=+0.01. Cross-family ref models all work.\"\n\n  RC3_three_class_sufficient:\n    sections: [discussion, limitations]\n    evidence: []\n    response: \"Attractor theory bounds paraphrasing to ~3 classes. Non-paraphrastic chains may support finer granularity — acknowledged as future work.\"\n\n  RC4_realistic_chains:\n    sections: [method, limitations]\n    evidence: [plan-002]\n    response: \"5 generators across 3 families tested. Mixed-generator chains acknowledged as limitation.\"\n\n  RC5_human_editing:\n    sections: [limitations]\n    evidence: []\n    response: \"Not tested. Acknowledged as limitation. Robustness to editing is future work.\"\n\n  RC6_ecological_validity:\n    sections: [method, limitations]\n    evidence: [mvp-001]\n    response: \"Wikipedia seeds across domains. Single prompt type (continuation); multi-prompt pending (plan-005).\"\n\n  RC7_ld_score_prediction:\n    sections: [results]\n    evidence: [plan-015-v2]\n    response: \"LD-Score confirmed as level feature (LOGO F1=0.72, Spearman=0.79). Pre-registered prediction validated.\"\n\n  RC8_ood_detection_features:\n    sections: [introduction, related_work, discussion]\n    evidence: []\n    response: \"Explicitly acknowledge reference-model entropy = NLL-based OOD score. Contribution is task formulation + empirical characterization, not features themselves.\"\n\n  RC9_scale:\n    sections: [limitations]\n    evidence: [plan-014]  # RUNNING\n    response: \"All generators ≤2.8B. plan-014 (Qwen3-8B) in progress. Results pending.\"\n    status: \"PENDING — update when plan-014 completes\"\n\n  RC10_length_confound:\n    sections: [results]\n    evidence: [plan-013]\n    response: \"Triple evidence: weak correlation (|ρ|<0.14), normalized trends preserved, length-matched F1 +0.041.\"\n\n  RC11_downstream_single_run:\n    sections: [results]\n    evidence: [plan-004-v2]\n    response: \"15 runs (5 variants × 3 seeds), cross-seed variance <0.002. OLMo-2-1B avoids reference model circularity.\"\n\n##############################################################################\n# 10. Pending Experiments & Writing Blockers\n##############################################################################\n\npending:\n  plan-014:\n    status: RUNNING\n    description: \"Qwen3-8B-Base (7B+ generator) — scale generalization test\"\n    impact_on_paper: \"Results in Limitations or Results depending on outcome\"\n    blocker: false  # paper can ship without it, but strengthens RC9 response\n\n  plan-005:\n    status: PREPARING\n    description: \"Prompt type comparison (continuation vs elaboration vs inspired_rewriting)\"\n    impact_on_paper: \"Addresses RC6 ecological validity\"\n    blocker: false  # acknowledged as limitation if not completed\n\n##############################################################################\n# 11. Framing Discipline Reminders (from D006+D007)\n##############################################################################\n\nframing_rules:\n  - \"Use 'differential depth response', NOT 'dual dynamics' or 'H1/H2'\"\n  - \"Contribution is empirical/conceptual, NOT methodological\"\n  - \"Do NOT call drift/stationarity split a 'discovery' — it follows from location-shift properties\"\n  - \"Report realistic performance range (0.57-0.82) in abstract/conclusion, not just best-case\"\n  - \"Consider 'distributional depth profiling' instead of 'distributional fingerprinting'\"\n  - \"R² on 5 aggregated depth means is meaningless — use individual-level Spearman ρ with bootstrap CI\"\n  - \"Headline template 'Z% downstream' → REPLACE with negative-finding wording\"\n  - \"Explicitly connect to OOD detection + perplexity-based detection literature\"\n  - \"Provide speculative theoretical motivation for shape stationarity\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "writing_plan.yaml",
    "content": "# Writing Plan — gen-depth-fingerprint\n# Depth Fingerprinting of Recursive LLM Generation Chains\n# Created: 2026-05-15\n\n##############################################################################\n# 1. Submission Target\n##############################################################################\n\nsubmission:\n  primary:\n    venue: AAAI 2027\n    deadline: 2026-08-02\n    page_limit: \"7 pages + 1 refs + unlimited appendix\"\n    template: aaai.sty\n    special_requirements:\n      - strict style compliance\n      - no modification of .sty\n  stretch:\n    venue: EMNLP 2026 ARR\n    deadline: 2026-05-25\n    page_limit: \"8 pages (long) + unlimited appendix\"\n    template: acl.sty\n    special_requirements:\n      - Limitations section (mandatory)\n      - Ethics Statement\n    scope_note: \"minimal — RQ1 (depth discriminability) + baseline comparison only\"\n  fallback:\n    - venue: ICLR 2027\n      deadline: 2026-09-24\n    - venue: NAACL 2027 ARR\n      deadline: 2026-10-16\n\n##############################################################################\n# 2. One-Sentence Contribution\n##############################################################################\n\none_sentence: >\n  We formulate ordinal depth estimation for recursive LLM generation chains,\n  showing that distributional features exhibit differential depth response\n  (central-tendency drifts, shape remains stationary), yielding a 7-feature\n  ensemble that reliably classifies generation depth (LOGO F1=0.80) across\n  5 generators / 3 model families.\n\n##############################################################################\n# 3. Claim-Evidence Map\n##############################################################################\n\nclaims:\n  C1_depth_discriminability:\n    claim: >\n      Distributional features under a held-out reference model classify\n      generation depth (gen-0/gen-1/gen-2+) with macro-F1 significantly\n      above chance, generalizing across unseen generators.\n    evidence:\n      - exp_id: plan-002-eval\n        metric: \"LOGO avg macro-F1 = 0.8037\"\n      - exp_id: plan-002-eval\n        metric: \"Leave-one-family-out Δ = +0.0107 (Pythia vs non-Pythia)\"\n      - exp_id: plan-015-v2\n        metric: \"Bootstrap CI [0.786, 0.799], p<0.001 vs all baselines\"\n      - exp_id: plan-013\n        metric: \"Length not a confound (|ρ|<0.14, normalized trends preserved)\"\n    tables: [Table 1, Table 2]\n    figures: [Fig 2, Fig 3]\n\n  C2_differential_response:\n    claim: >\n      Central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift\n      monotonically with depth; shape features (entropy_std, tail_decay) remain\n      near-stationary. Full 7-feature set significantly outperforms surface-only\n      and reference-only subsets.\n    evidence:\n      - exp_id: plan-001-fix\n        metric: \"full(0.82) > surface(0.76) > reference(0.72), CI non-overlapping\"\n      - exp_id: plan-002\n        metric: \"Drift direction consistent across all 5 generators\"\n      - exp_id: plan-002-eval\n        metric: \"full(0.80) > ref(0.75) = surf(0.75), McNemar p≈0\"\n      - exp_id: plan-003\n        metric: \"3 cross-family ref models: LOGO F1 0.80-0.82, drift direction consistent\"\n    tables: [Table 2]\n    figures: [Fig 1]\n\n  C3_downstream_negative:\n    claim: >\n      Depth-aware data curation does NOT improve downstream CLM quality.\n      Data quantity dominates depth composition. Depth fingerprinting is\n      diagnostic, not curative.\n    status: NEGATIVE FINDING — report honestly\n    evidence:\n      - exp_id: plan-004-v2\n        metric: \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\"\n      - exp_id: plan-004-v2\n        metric: \"15/15 runs, cross-seed variance <0.002\"\n    tables: [Table 3]\n    figures: [Fig 4]\n    framing_note: >\n      DO NOT hide or spin. Frame as: \"We tested whether depth-aware curation\n      improves downstream quality. It does not. The primary determinant is data\n      quantity, not depth composition. This positions depth fingerprinting as a\n      diagnostic tool for provenance characterization, not a curative tool for\n      data selection.\"\n\n##############################################################################\n# 4. Paper Outline\n##############################################################################\n\noutline:\n  abstract:\n    length: \"~200 words\"\n    structure: \"five-sentence method (Farquhar)\"\n    key_points:\n      - \"We formulate ordinal depth estimation beyond binary detection\"\n      - \"Why hard: existing detectors offer only real-vs-synthetic, no depth signal\"\n      - \"How: 7 distributional features exhibiting differential depth response\"\n      - \"Evidence: LOGO F1=0.80 across 5 generators / 3 families, p<0.001 vs baselines\"\n      - \"Honest negative: depth-aware curation does not improve downstream quality\"\n    headline_note: >\n      The paper_framing.md headline template contains \"Z% downstream\" placeholder.\n      UPDATE to negative-finding wording: \"...however, depth-aware data curation\n      does not improve downstream model quality over random subsampling,\n      positioning depth estimation as a diagnostic rather than curative tool.\"\n    reviewer_concerns_covered: []\n\n  introduction:\n    length: \"~1.5 pages\"\n    key_points:\n      - \"Problem: web data increasingly contains recursive LLM-generated text of unknown provenance depth\"\n      - \"Gap: binary detectors cannot distinguish gen-1 from gen-2+, forcing all-or-nothing filtering\"\n      - \"Our formulation: ordinal depth estimation as a new task (genuinely novel)\"\n      - \"Core finding: differential depth response — level/diversity features drift, shape features are stationary\"\n      - \"Practical consequence: 7-feature ensemble LOGO F1=0.80, reliable across unknown generators\"\n      - \"Honest reporting: downstream curation does not benefit (diagnostic, not curative)\"\n      - \"Contributions list (3 items matching the 3 claims)\"\n    evidence:\n      - exp_id: plan-015-v2  # headline numbers\n      - exp_id: plan-002-eval  # LOGO result\n    reviewer_concerns_covered: [RC8]\n    notes:\n      - \"Must explicitly state contribution is empirical/conceptual, not methodological (D006+D007)\"\n      - \"Connect to OOD detection literature in framing paragraph (RC8)\"\n      - \"Do NOT overclaim 'dual dynamics' — use 'differential depth response' (D007)\"\n\n  related_work:\n    length: \"~1 page\"\n    organization: # see literature_strategy section below\n      - subsection: \"AI-Generated Text Detection\"\n        papers: [detectgpt, gltr, dna_gpt, binoculars, fast_detectgpt, ld_score, intrinsic_dimension, diveye, generator_barrier, feat_aug_transformer, reliable_detection, paraphrase_evades, detection_possibilities, grover, release_strategies, jawahar_survey]\n        angle: \"Binary detection only — no depth estimation capability. Single-score baselines show high cross-generator variance.\"\n      - subsection: \"Model Collapse and Iterative Generation\"\n        papers: [self_consuming_mad, curse_of_recursion, strong_model_collapse, model_collapse_avoidable, broken_telephone, markovian_chains]\n        angle: \"Training-loop collapse theory; iterative generation distortion. We study inference-chain depth without retraining.\"\n      - subsection: \"Vocabulary Diversity and Stylometry\"\n        papers: [curious_decline, writing_diversity, nucleus_sampling, mapping_llm_science, monitoring_ai_review, stamatatos_survey, koppel_authorship, uchendu_attribution]\n        angle: \"Diversity decline documented but not used for depth estimation. Our surface features are stylometric in nature.\"\n      - subsection: \"Data Quality and Provenance\"\n        papers: [dsir, qurating, ccnet, watermark_llm, synthid_text, aaronson_watermark, chainwash, min_k_percent, ood_baseline]\n        angle: \"Quality scoring/watermarking for data curation. Depth fingerprint complements these as provenance signal.\"\n    reviewer_concerns_covered: [RC1, RC8]\n\n  method:\n    length: \"~1.5 pages\"\n    subsections:\n      - name: \"Task Formulation\"\n        content: \"Ordinal depth estimation: given text x, predict depth class {gen-0, gen-1, gen-2+}\"\n        length: \"~0.25 page\"\n      - name: \"Generation Chain Construction\"\n        content: \"5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B), 3 families, ~1000 seeds × 5 depths, continuation prompt, temp=0.7/top_p=0.9/max_tokens=256\"\n        evidence: [mvp-001, plan-002]\n        length: \"~0.25 page\"\n      - name: \"Feature Extraction\"\n        content: \"7 features: 4 reference-model (entropy_mean/std/max, tail_decay) + 3 surface (TTR, hapax_ratio, entropy_min). Reference model = Pythia-410M.\"\n        length: \"~0.5 page\"\n      - name: \"Evaluation Protocol\"\n        content: \"Leave-one-generator-out (LOGO) cross-validation. XGBoost classifier. Bootstrap CI (n=1000). McNemar test for feature ablation.\"\n        length: \"~0.5 page\"\n    reviewer_concerns_covered: [RC2, RC4, RC6]\n\n  results:\n    length: \"~2 pages\"\n    subsections:\n      - name: \"Depth Classification Performance (C1)\"\n        content: \"LOGO F1=0.80, per-generator breakdown, family-out Δ=+0.01. Gen-0 near-perfect (F1=0.95), gen-1 vs gen-2+ harder.\"\n        evidence: [plan-002-eval, plan-015-v2]\n        tables: [Table 1]\n        figures: [Fig 2]\n        length: \"~0.5 page\"\n      - name: \"Differential Depth Response (C2)\"\n        content: \"Feature drift patterns. entropy_mean/TTR/hapax drift monotonically. entropy_std/tail_decay near-stationary. Feature complementarity: full > surface = reference.\"\n        evidence: [plan-001-fix, plan-002, plan-003]\n        tables: [Table 2]\n        figures: [Fig 1]\n        length: \"~0.5 page\"\n      - name: \"Comparison with Detection Baselines\"\n        content: \"7-feature vs Avg-LogProb (+3.9pp, p<0.001), FastDetectGPT (+6.7pp), LD-Score, Binoculars. Key advantage: tight CI vs high variance of single detectors.\"\n        evidence: [plan-015-v2]\n        figures: [Fig 3]\n        length: \"~0.5 page\"\n      - name: \"Downstream Utility — Negative Finding (C3)\"\n        content: \"Depth-aware curation does not improve CLM quality. all(2.335) < size_matched(2.367) < depth01(2.387). Quantity dominates composition. Diagnostic not curative.\"\n        evidence: [plan-004-v2]\n        tables: [Table 3]\n        figures: [Fig 4]\n        length: \"~0.5 page\"\n    reviewer_concerns_covered: [RC1, RC2, RC10, RC11]\n\n  discussion:\n    length: \"~0.5 page\"\n    key_points:\n      - \"Why shape features are stationary: determined by sampling mechanism and architecture, invariant to input content drift (speculative, explicitly flagged)\"\n      - \"Practical implications: risk-stratified data curation (flag gen-2+ for review, keep gen-1)\"\n      - \"Honest framing of C3: negative finding has positive information value — rules out depth-based filtering as curation strategy\"\n      - \"Connection to model collapse literature: inference chains show similar distributional drift without retraining\"\n    reviewer_concerns_covered: [RC3, RC8]\n\n  limitations:\n    length: \"~0.25 page (mandatory for EMNLP; good practice for AAAI)\"\n    items:\n      - \"All generators ≤2.8B (plan-014 pending for 7B+); frontier models may compress depth signal\"\n      - \"Single prompt type (continuation); elaboration/rewriting chains not yet tested (plan-005 pending)\"\n      - \"Lab-constructed single-model chains; real web contamination involves diverse generators per step\"\n      - \"Negative downstream result tested on CLM only; other downstream tasks not evaluated\"\n      - \"3-class granularity; finer-grained depth may be possible for non-paraphrastic chains\"\n    reviewer_concerns_covered: [RC3, RC4, RC5, RC6, RC9]\n\n  conclusion:\n    length: \"~0.25 page\"\n    key_points:\n      - \"Restate contributions: task formulation, empirical characterization, honest negative on downstream\"\n      - \"Report realistic performance range (0.57-0.82 depending on conditions)\"\n      - \"Future work: frontier-scale generators, mixed-generator chains, prompt type diversity\"\n\n##############################################################################\n# 5. Figure Plan\n##############################################################################\n\nfigures:\n  fig1_differential_response:\n    title: \"Differential Depth Response of Distributional Features\"\n    type: \"multi-panel line plot (2×2 or 1×4)\"\n    data_source: plan-002 (features_all_models.csv)\n    content:\n      - \"Panel A: entropy_mean vs depth (5 generators, monotonic drift)\"\n      - \"Panel B: TTR or hapax_ratio vs depth (monotonic drift)\"\n      - \"Panel C: entropy_std vs depth (near-stationary)\"\n      - \"Panel D: tail_decay vs depth (near-stationary)\"\n    notes: \"Error bands = bootstrap 95% CI. Color-code by generator. This is the signature figure — spend time on it.\"\n    placement: \"Results §5.2\"\n    evidence: [plan-001-fix, plan-002]\n\n  fig2_logo_performance:\n    title: \"Leave-One-Generator-Out Classification Performance\"\n    type: \"grouped bar chart or radar\"\n    data_source: plan-002-eval (cross_generator_results.json)\n    content:\n      - \"Per held-out generator macro-F1 with CI\"\n      - \"Horizontal line at overall LOGO mean (0.80)\"\n      - \"Optional: per-class (gen-0/gen-1/gen-2+) breakdown\"\n    placement: \"Results §5.1\"\n    evidence: [plan-002-eval]\n\n  fig3_baseline_comparison:\n    title: \"Comparison with Single-Detector Baselines\"\n    type: \"forest plot or dot-with-CI\"\n    data_source: plan-015-v2 (detector_baseline_results.json)\n    content:\n      - \"7-feature ensemble: 0.798 [0.786, 0.799]\"\n      - \"Avg-LogProb: 0.765 [0.616, 0.820]\"\n      - \"LD-Score: 0.721 [0.588, 0.770]\"\n      - \"FastDetectGPT: 0.627 [0.511, 0.762]\"\n      - \"Binoculars: 0.579 [0.405, 0.664]\"\n    notes: \"Key message: ensemble has tight CI, single detectors have wide CI. Reliability advantage, not just mean.\"\n    placement: \"Results §5.3\"\n    evidence: [plan-015-v2]\n\n  fig4_downstream_negative:\n    title: \"Downstream CLM Perplexity by Data Curation Strategy\"\n    type: \"bar chart with error bars\"\n    data_source: plan-004-v2\n    content:\n      - \"5 variants: all / size_matched / depth01 / binary_filtered / depth0_only\"\n      - \"Y-axis: eval perplexity\"\n      - \"Error bars: 3-seed variance\"\n      - \"Annotation: data count per variant\"\n    notes: \"Frame as honest negative. Title should not hide the negative result.\"\n    placement: \"Results §5.4\"\n    evidence: [plan-004-v2]\n\n##############################################################################\n# 6. Table Plan\n##############################################################################\n\ntables:\n  table1_logo_results:\n    title: \"Leave-One-Generator-Out Depth Classification Results\"\n    placement: \"Results §5.1\"\n    columns: [\"Held-out Generator\", \"Family\", \"Params\", \"Macro-F1\", \"95% CI\"]\n    rows:\n      - [\"Pythia-2.8B\", \"Pythia\", \"2.8B\", \"—\", \"—\"]  # fill from data\n      - [\"Pythia-1B\", \"Pythia\", \"1.0B\", \"0.851\", \"—\"]\n      - [\"OLMo-2-1B\", \"OLMo\", \"1.5B\", \"0.752\", \"—\"]\n      - [\"Qwen3-1.7B\", \"Qwen\", \"1.7B\", \"—\", \"—\"]\n      - [\"Qwen3-0.6B\", \"Qwen\", \"0.6B\", \"—\", \"—\"]\n      - [\"**Average**\", \"\", \"\", \"**0.804**\", \"[0.786, 0.799]\"]\n    footer: \"Family-out Δ = +0.011 (Pythia-held-out vs non-Pythia-held-out)\"\n    evidence: [plan-002-eval, plan-015-v2]\n    notes: \"Fill exact per-generator CIs from bootstrap data\"\n\n  table2_feature_ablation:\n    title: \"Feature Group Ablation and Complementarity\"\n    placement: \"Results §5.2\"\n    columns: [\"Feature Set\", \"Features\", \"LOGO F1\", \"95% CI\", \"McNemar p\"]\n    rows:\n      - [\"Full (7 features)\", \"all\", \"0.804\", \"[0.786, 0.799]\", \"—\"]\n      - [\"Surface only\", \"TTR, hapax_ratio, entropy_min\", \"0.747\", \"—\", \"< 0.001\"]\n      - [\"Reference only\", \"entropy_mean/std/max, tail_decay\", \"0.754\", \"—\", \"< 0.001\"]\n    footer: \"Permutation importance: hapax_ratio(0.289) > ttr(0.168) > entropy_mean(0.160)\"\n    evidence: [plan-002-eval, plan-001-fix]\n\n  table3_downstream:\n    title: \"Downstream CLM Fine-tuning by Depth Curation Strategy\"\n    placement: \"Results §5.4\"\n    columns: [\"Curation Strategy\", \"Train Size\", \"Eval PPL (mean±std)\", \"Δ vs size_matched\"]\n    rows:\n      - [\"All depths (no filter)\", \"12,299\", \"2.335 ± 0.000\", \"-0.032\"]\n      - [\"Size-matched random\", \"3,951\", \"2.367 ± 0.000\", \"baseline\"]\n      - [\"Depth 0+1 only\", \"3,951\", \"2.387 ± 0.001\", \"+0.020\"]\n      - [\"Binary filtered\", \"3,951\", \"2.389 ± 0.000\", \"+0.022\"]\n      - [\"Depth 0 only\", \"797\", \"2.681 ± 0.001\", \"+0.314\"]\n    footer: >\n      OLMo-2-0425-1B, 3 seeds. Size-matched is the proper control.\n      Depth-aware curation does not outperform random subsampling at equal data count.\n    evidence: [plan-004-v2]\n\n  table4_cross_ref:\n    title: \"Cross-Family Reference Model Validation\"\n    placement: \"Appendix (or Results §5.2 if space)\"\n    columns: [\"Reference Model\", \"Family\", \"Params\", \"LOGO F1\", \"Entropy Drift Range\"]\n    rows:\n      - [\"Pythia-410M\", \"Pythia\", \"410M\", \"0.803\", \"[-1.19, -1.40]\"]\n      - [\"OLMo-2-1B\", \"OLMo\", \"1.5B\", \"0.807\", \"[-0.61, -0.91]\"]\n      - [\"Qwen3-0.6B\", \"Qwen\", \"0.6B\", \"0.816\", \"[-0.96, -1.35]\"]\n    footer: \"Drift direction consistent across all reference models; magnitude varies.\"\n    evidence: [plan-003]\n\n##############################################################################\n# 7. Literature Strategy\n##############################################################################\n\nliterature:\n  total_papers: 39\n  organization:\n    perplexity_detection:\n      papers: 16\n      key_refs: [detectgpt, fast_detectgpt, binoculars, ld_score, diveye, generator_barrier]\n      positioning: \"Binary detection paradigm. No depth estimation. High cross-generator variance when repurposed as ordinal predictors.\"\n    model_collapse:\n      papers: 4\n      key_refs: [curse_of_recursion, strong_model_collapse, self_consuming_mad]\n      positioning: \"Training-loop collapse. We study inference chains without retraining — distributional drift without model parameter change.\"\n    iterative_generation:\n      papers: 2\n      key_refs: [broken_telephone, markovian_chains]\n      positioning: \"Most directly related. broken_telephone: paraphrasing/translation chains. markovian_chains: convergence theory. We: non-paraphrastic continuation chains + depth estimation task.\"\n    vocabulary_diversity:\n      papers: 5\n      key_refs: [curious_decline, writing_diversity, nucleus_sampling]\n      positioning: \"Diversity decline documented in training loops. We show it appears in inference chains too and use it for depth classification.\"\n    stylometry:\n      papers: 3\n      key_refs: [stamatatos_survey, uchendu_attribution]\n      positioning: \"Feature set is essentially stylometric. We extend from source attribution to depth estimation.\"\n    data_quality:\n      papers: 3\n      key_refs: [dsir, qurating]\n      positioning: \"Data scoring/selection. Depth fingerprint as complementary provenance signal.\"\n    watermarking:\n      papers: 4\n      key_refs: [watermark_llm, chainwash]\n      positioning: \"Active signal embedding. We: passive post-hoc detection without watermark. chainwash motivates depth-aware approach — watermarks decay over generation steps.\"\n    membership_inference:\n      papers: 1\n      key_refs: [min_k_percent]\n      positioning: \"Probability distribution analysis for membership; we analyze for depth.\"\n    ood_detection:\n      papers: 1\n      key_refs: [ood_baseline]\n      positioning: \"Reference-model entropy features are functionally NLL-based OOD scores. Explicitly acknowledge this connection (RC8).\"\n\n##############################################################################\n# 8. Writing Order & Dependencies\n##############################################################################\n\nwriting_order:\n  phase1_skeleton:\n    deadline: \"2026-05-20\"\n    tasks:\n      - section: \"Results (§5)\"\n        reason: \"Anchor claims to evidence first. Numbers drive the narrative.\"\n        dependencies: []\n        priority: 1\n      - section: \"Method (§4)\"\n        reason: \"Experimental setup needed to interpret results.\"\n        dependencies: []\n        priority: 2\n      - section: \"Figures (all 4)\"\n        reason: \"Figures convey results more effectively than text. Generate early.\"\n        dependencies: [\"Results\"]\n        priority: 1\n\n  phase2_narrative:\n    deadline: \"2026-06-01\"\n    tasks:\n      - section: \"Introduction (§1)\"\n        reason: \"Story spine. Requires stable results to write convincingly.\"\n        dependencies: [\"Results\"]\n        priority: 1\n      - section: \"Related Work (§2)\"\n        reason: \"Positioning depends on knowing exact claims.\"\n        dependencies: [\"Introduction\"]\n        priority: 2\n      - section: \"Discussion + Limitations (§6)\"\n        reason: \"Interprets results, addresses reviewer concerns.\"\n        dependencies: [\"Results\"]\n        priority: 2\n\n  phase3_polish:\n    deadline: \"2026-06-15\"\n    tasks:\n      - section: \"Abstract\"\n        reason: \"Last written, first read. Needs stable claims.\"\n        dependencies: [\"Introduction\", \"Results\", \"Discussion\"]\n        priority: 1\n      - section: \"Conclusion\"\n        reason: \"Mirror of abstract with forward-looking additions.\"\n        dependencies: [\"Abstract\"]\n        priority: 2\n      - section: \"Title\"\n        reason: \"After all claims are finalized.\"\n        dependencies: [\"Abstract\"]\n        priority: 3\n\n  phase4_submission:\n    deadline: \"2026-07-15\"\n    tasks:\n      - \"Citation verification (reference-audit skill)\"\n      - \"Page limit compliance (7+1 for AAAI)\"\n      - \"Anonymization check\"\n      - \"Appendix organization (cross-ref table, length analysis, per-generator details)\"\n      - \"Paper checklist / Ethics statement\"\n\n##############################################################################\n# 9. Reviewer Concern Coverage Matrix\n##############################################################################\n\nreviewer_coverage:\n  RC1_vocabulary_impoverishment:\n    sections: [related_work, results]\n    evidence: [plan-002-eval]\n    response: \"Feature complementarity proven: full(0.80) > surface(0.75) = ref(0.75). Two groups capture different signal.\"\n\n  RC2_generalize_beyond_pythia:\n    sections: [method, results]\n    evidence: [plan-002, plan-002-eval, plan-003]\n    response: \"5 generators / 3 families. LOGO F1=0.80, family-out Δ=+0.01. Cross-family ref models all work.\"\n\n  RC3_three_class_sufficient:\n    sections: [discussion, limitations]\n    evidence: []\n    response: \"Attractor theory bounds paraphrasing to ~3 classes. Non-paraphrastic chains may support finer granularity — acknowledged as future work.\"\n\n  RC4_realistic_chains:\n    sections: [method, limitations]\n    evidence: [plan-002]\n    response: \"5 generators across 3 families tested. Mixed-generator chains acknowledged as limitation.\"\n\n  RC5_human_editing:\n    sections: [limitations]\n    evidence: []\n    response: \"Not tested. Acknowledged as limitation. Robustness to editing is future work.\"\n\n  RC6_ecological_validity:\n    sections: [method, limitations]\n    evidence: [mvp-001]\n    response: \"Wikipedia seeds across domains. Single prompt type (continuation); multi-prompt pending (plan-005).\"\n\n  RC7_ld_score_prediction:\n    sections: [results]\n    evidence: [plan-015-v2]\n    response: \"LD-Score confirmed as level feature (LOGO F1=0.72, Spearman=0.79). Pre-registered prediction validated.\"\n\n  RC8_ood_detection_features:\n    sections: [introduction, related_work, discussion]\n    evidence: []\n    response: \"Explicitly acknowledge reference-model entropy = NLL-based OOD score. Contribution is task formulation + empirical characterization, not features themselves.\"\n\n  RC9_scale:\n    sections: [limitations]\n    evidence: [plan-014]  # RUNNING\n    response: \"All generators ≤2.8B. plan-014 (Qwen3-8B) in progress. Results pending.\"\n    status: \"PENDING — update when plan-014 completes\"\n\n  RC10_length_confound:\n    sections: [results]\n    evidence: [plan-013]\n    response: \"Triple evidence: weak correlation (|ρ|<0.14), normalized trends preserved, length-matched F1 +0.041.\"\n\n  RC11_downstream_single_run:\n    sections: [results]\n    evidence: [plan-004-v2]\n    response: \"15 runs (5 variants × 3 seeds), cross-seed variance <0.002. OLMo-2-1B avoids reference model circularity.\"\n\n##############################################################################\n# 10. Pending Experiments & Writing Blockers\n##############################################################################\n\npending:\n  plan-014:\n    status: RUNNING\n    description: \"Qwen3-8B-Base (7B+ generator) — scale generalization test\"\n    impact_on_paper: \"Results in Limitations or Results depending on outcome\"\n    blocker: false  # paper can ship without it, but strengthens RC9 response\n\n  plan-005:\n    status: PREPARING\n    description: \"Prompt type comparison (continuation vs elaboration vs inspired_rewriting)\"\n    impact_on_paper: \"Addresses RC6 ecological validity\"\n    blocker: false  # acknowledged as limitation if not completed\n\n##############################################################################\n# 11. Framing Discipline Reminders (from D006+D007)\n##############################################################################\n\nframing_rules:\n  - \"Use 'differential depth response', NOT 'dual dynamics' or 'H1/H2'\"\n  - \"Contribution is empirical/conceptual, NOT methodological\"\n  - \"Do NOT call drift/stationarity split a 'discovery' — it follows from location-shift properties\"\n  - \"Report realistic performance range (0.57-0.82) in abstract/conclusion, not just best-case\"\n  - \"Consider 'distributional depth profiling' instead of 'distributional fingerprinting'\"\n  - \"R² on 5 aggregated depth means is meaningless — use individual-level Spearman ρ with bootstrap CI\"\n  - \"Headline template 'Z% downstream' → REPLACE with negative-finding wording\"\n  - \"Explicitly connect to OOD detection + perplexity-based detection literature\"\n  - \"Provide speculative theoretical motivation for shape stationarity\"\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T03:29:13.537353+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-plan_20260515T032552",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T03:29:13.537619+00:00_

`writing_plan.yaml` 已创建，覆盖：

- **3 个 Claim 的 evidence mapping**（含 C3 negative finding 的 honest reporting 框架）
- **6 个 section 的 outline**，每个标注篇幅、对应 exp_id、reviewer concern 覆盖
- **4 张图**：differential response 多面板图、LOGO 柱状图、baseline 对比森林图、downstream 负面结果图
- **4 张表**：LOGO 分生成器结果、feature ablation、downstream 5 variants、cross-ref 验证
- **39 篇文献分 9 类**的 related work 组织策略
- **4 阶段写作顺序**：Results+Figures → Intro+RW → Abstract+Title → 投前检查
- **11 个 RC 的覆盖矩阵**，标注每个 concern 在哪个 section 回应、用什么 evidence
- **headline template 的 "Z% downstream" 已标记为需更新为 negative finding 措辞**
- **2 个 pending 实验**（plan-014 scale、plan-005 prompt type）标记为 non-blocker

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper-plan_20260515T032552"
}
```

</details>

---
