# Director coordination — Part 1 of 2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/58/584d2f2da6363b58e0dc.json)

## Round 1

## Round 1

64 recorded events


### User

_source line 1 · 2026-05-24T14:53:17.901758+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: clkc_mech_interp
- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-24T14:53:25.411838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-24T14:53:25.463045+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-24T14:53:31.186491+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-24T14:53:31.287194+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-24T14:53:37.360211+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-24T14:53:38.315057+00:00_

{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (78 个)\n\n- **comet_qwen_v6**: DONE (killed) — \n- **gemma_en_act_102**: DONE (success) — \n- **xnli_baseline_110**: DONE (negative) — \n- **comet_llama_v5**: DONE (killed) — \n- **comet_qwen_v5**: DONE (killed) — \n- **mvp_probe_llama_v1**: DONE (success) — \n- **mvp_probe_v1**: DONE (success) — \n- **comet_llama_v4**: PREPARING (killed) — \n- **comet_llama_v3**: PREPARING (killed) — \n- **comet_llama_v2**: PREPARING (killed) — \n- **comet_llama**: PREPARING (killed) — \n- **comet_qwen_v4**: PREPARING (killed) — \n- **comet_qwen_v3**: PREPARING (killed) — \n- **comet_qwen_v2**: PREPARING (killed) — \n- **comet_qwen**: PREPARING (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- gemma-steering-pickup（准备中）\n- llama31_en_activations（准备中）\n- qwen3_translate_zh（准备中）\n- collect_en_activations_qwen3_8b（准备中）\n- collect_en_activations_llama_v2（准备中）\n- translate_zh_llama_v2（准备中）\n- translate_zh_qwen（准备中）\n- collect_en_act_llama_v3（准备中）\n- collect_en_act_qwen_v2（准备中）\n- verify_qwen3_v2（准备中）\n- …另有 16 项\n\n## 近期结论\n- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L13_133** (negative): Qwen3-8B-Instruct L13 (36% depth) probe direction causally influences conflict resolution with matched-condition data (N≈200, high probe acc). L13 = L14 peak - 1, establishi
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-24T14:53:38.817305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-24T14:53:39.018558+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	\input{experiments}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\input{limitations}
42	
43	\appendix
44	
45	\section{Use of AI Assistants}
46	\label{app:ai-assistants}
47	
48	We used Claude (Anthropic) as an AI coding and writing assistant
49	throughout this work. Specifically:
50	\begin{itemize}
51	    \item \textbf{Code:} drafting experiment scripts, data-processing
52	    pipelines, and analysis utilities; debugging and refactoring.
53	    \item \textbf{Writing:} drafting and revising paper sections,
54	    polishing prose, and reformatting \LaTeX{}.
55	    \item \textbf{Literature:} summarizing related papers to inform
56	    related-work section.
57	\end{itemize}
58	
59	\section{Fine-Grained Causal Boundary Analysis}
60	\label{app:boundary}
61	
62	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
63	
64	\begin{table}[h]
65	\centering
66	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
67	\label{tab:boundary}
68	\small
69	\resizebox{\columnwidth}{!}{%
70	\begin{t
…[truncated 2623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-24T14:53:39.069291+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-24T14:53:39.120080+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md\", \"content\": \"# 关键研究发现\\n\\n## Causal Gradient Profile — 完整 6 层同条件数据 [2026-05-24]\\n\\n**核心发现**：同条件实验（N=201, probe acc ~85-92%）绘制出完整的因果梯度。Steering 效应 peak at L13，向深层平滑衰减，L28（detection peak）完全无效。\\n\\n| Layer | Depth | Probe Acc | Best α | Fisher p | Bonferroni sig | 效应 |\\n|-------|-------|-----------|--------|----------|----------------|------|\\n| L12 | 38% | 91.75% | +20 | 0.0853 | 0/6 ❌ | — |\\n| **L13** | **41%** | **90.00%** | **+10** | **0.0003** | **2/6** ✅✅ | **peak** |\\n| **L14** | **44%** | **91.75%** | **+10** | **0.0022** | **1/6** ✅ | strong |\\n| **L16** | **50%** | **91.50%** | **+10** | **0.005** | **1/6** ✅ | moderate |\\n| L18 | 56% | 90.75% | +5 | 0.0099 | 0/6 ❌ | marginal (差0.0016) |\\n| L28 | 88% | 85.25% | +10 | 0.284 | 0/6 ❌ | none |\\n\\n**Causal window = L13-L16（3层显著）**，L18 marginal，L12/L28 negative。窗口占 32 层模型的 ~12.5%。\\n\\n**p 值单调递增梯度**：0.0003 → 0.0022 → 0.005 → 0.0099 → 0.284。连续衰减而非 on/off。\\n\\n**Detection ≠ Decision 最终验证**：L28 是 detection peak（probe acc 最高），但 steering best p=0.284，完全无因果效应。高质量 probe 条件下解离依然稳健。\\n\\n**仅正向 α 有效**：所有显著效应来自 +5/+10，负向 α 全不显著。\\n\\n**L13 复现更强**：原始 p=0.0009 (N=136, 1α sig) → 新数据 p=0.0003 (N=201, 2α sig)。\\n\\n---\\n\\n## C2 不对称性非冲突特有 [2026-05-22, xnli_baseline_110]\\n\\n**核心发现**：~6pp ZH→EN > EN→ZH 不对称性在非冲突任务 XNLI 上同样存在，是模型的一般性跨语言属性，非冲突信号特有。\\n\\n| Model | XNLI asymmetry | Conflict asymmetry |\\n|-------|---------------|-------------------|\\n| Qwen | +6.72pp CI[2.36,11.73] ✓ | +5.95pp CI[-3.67,14.81] |\\n| Llama | +5.97pp CI[0.92,11.33] ✓ | +11.76pp CI[4.29,19.57] ✓ |\\n\\n**推导**：英语主导预训练 → EN 表征空间更\\\"标准\\\" → ZH→EN 迁移天然更好。C2 需 reframe：从 \\\"conflict-specific asymmetry\\\" 改为 \\\"conflict signals share general cross-lingual transfer pathways\\\"。\\n\\n---\\n\\n## Steering 因果效应是 Llama-specific [2026-05-22, 更新 2026-05-24]\\n\\n**核心发现**：Probe weight 方向的因果效应具有强模型特异性——仅 Llama L13-L16 
…[truncated 2638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-24T14:53:49.324383+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
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

_source line 13 · 2026-05-24T14:53:49.324913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-24T14:53:49.877012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-24T14:53:50.379215+00:00_

1	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine the model's answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT. Our analysis combines cross-lingual transfer, a non-conflict baseline on XNLI, confound exclusion for translation quality and token overlap, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals; it inherits from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: in Llama, the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with direct implications for probe-based intervention research.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-24T14:53:50.379594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-24T14:53:50.530420+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{brink2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe ac
…[truncated 3734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-24T14:53:50.530765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-24T14:53:50.581295+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, \citet{brink2026probing} localized factual associations via probing, \citet{pham2026where} traced intra-memory conflict pathways, and \citet{li2025taming} proposed conflict mitigation methods.
7	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
8	
9	\paragraph{Cross-lingual representations in multilingual models.}
10	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
11	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
12	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
13	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR benchmark), and \citet{ifergan2024beneath, xing2024evaluating}; our work provides a mechanistic account of why such asymmetries arise.
14	
15	\paragraph{Representation steering and causal intervention.}
16	\citet{li2023iti} introduced Inference-Time Intervention for
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-24T14:53:54.697507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-24T14:53:55.049217+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our pipeline proceeds from data construction through probing and steering, formalized below.
5	
6	\subsection{Task Formulation}
7	\label{sec:task}
8	
9	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
10	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
11	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
12	
13	\subsection{Data Construction}
14	\label{sec:data}
15	
16	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
17	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2024qwen25}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
18	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET \citep{rei2020comet} back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
19	
20	\subsection{Activation Extraction and Probing}
21	\label{sec:extraction}
22	
23	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
24	We record the model's answer and assign binary labels (contextual vs.\ parametric).
25	
26	\label{sec:pro
…[truncated 2768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-24T14:53:55.049578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-24T14:53:55.501638+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for al
…[truncated 13468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-24T14:53:55.602538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-24T14:53:55.955136+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Detection and decision occur at different layers.}
5	Our central mechanistic finding is a dissociation between where conflict signals become linearly readable and where they exert causal influence on model behavior.
6	In Llama, probe accuracy on EN$\to$EN peaks at layer~28 (88\% depth), yet representation steering succeeds only at layer~13 (41\% depth; Fisher $p = 0.002$), and all late-layer interventions produce no significant behavioral change ($p > 0.3$).
7	This dissociation has a cross-lingual counterpart: the Llama ZH$\to$ZH probe peaks at L13, the same layer where steering succeeds.
8	Mid-layers thus serve a dual role as the site of cross-lingual alignment \citep{muller2021first, wendler2024llamas} and the locus where conflict signals acquire causal force.
9	The EN$\to$EN peak at L28 is best understood as a diagnostic readout, a linearly readable trace of a decision that has already been made upstream.
10	A practical implication follows: the probe peak layer is not the causal layer, and intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site.
11	Cross-layer sweeps, as conducted here, are necessary to locate the true decision point.
12	Steering failed in both Qwen (L14, 39\%; $n = 131$, best $p = 0.785$) and Gemma (L17, 40\%; $n = 171$, best $p = 0.448$), with zero directional flips in both cases.
13	The Gemma result is particularly informative: its 88.9\% probe accuracy---the highest among all three models---rules out probe quality as a confound, since the direction that best separates conflict labels carries no causal influence despite being highly discriminative.
14	This establishes that the causal influence of the probe direction is architecture-specific, not a general property of mid-layer computation.
15	
16	\paragraph{Conflict signals are encoded in a general cross-lingual space.}
17	The ZH$\to$EN transfer advantage is consistent ac
…[truncated 4387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-24T14:53:56.005750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-24T14:53:56.457774+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	This work investigated whether knowledge conflict signals in multilingual LLMs are detectable across languages and whether detected signals causally influence conflict resolution.
5	Through residual stream probing on Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, we showed that conflict signals are linearly detectable both within and across languages, with balanced accuracies of 77.6\%, 75.0\%, and 76.2\% on English within-language detection and all cross-lingual transfer directions significantly exceeding chance (binomial $p < 0.001$).
6	The observed transfer asymmetry (ZH$\to$EN exceeding EN$\to$ZH by approximately 6--7~pp) is consistent across all three architectures and matches the XNLI non-conflict baseline in magnitude and direction for all models, establishing that this pattern reflects the general cross-lingual representational structure of English-dominant models rather than conflict-specific encoding.
7	
8	A central finding is the dissociation between detection and decision.
9	Probe accuracy peaks at late layers (L28, 88\% depth), but representation steering succeeds only at a mid-layer (L13, 41\% depth; Fisher $p = 0.002$), and all late-layer interventions fail.
10	This result demonstrates that linear detectability does not imply causal influence, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.
11	For probing-based intervention research, this dissociation implies that cross-layer sweeps are necessary to identify the computationally relevant site, as targeting the probe peak alone can miss the true decision point.
12	
13	Several directions remain open.
14	Steering failed in both Qwen (L14; $n = 131$, best $p = 0.785$) and Gemma (L17; $n = 171$, 88.9\% probe accuracy, best $p = 0.448$), with zero directional flips despite Gemma's probe accuracy exceeding Llama's, confirming that the causal influence of the probe direction is architecture-specific.
15	Futur
…[truncated 237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-24T14:53:56.458254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-24T14:53:57.162035+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese).
6	While the consistent patterns across three architecturally distinct models are encouraging, typologically diverse language pairs (e.g., English-German, English-Japanese) are needed to assess the generality of our findings.
7	Second, causal steering succeeded only in Llama at L13.
8	Gemma L17 steering failed despite the highest probe accuracy among all three models (88.9\%, $n = 171$), ruling out probe quality as a confound and constituting an informative negative that confirms the architecture-specificity of the effect.
9	Qwen L14 ($n = 131$, probe accuracy 71.0\%) was also negative with zero directional flips.
10	Third, the effective dataset size (966 to 1,590 samples per model after parametric knowledge verification) is constrained by the requirement that each model must correctly answer the question without context.
11	This verification step is necessary to ensure genuine knowledge conflicts, but it limits the statistical power of our analyses, particularly for stratified comparisons such as the COMET tercile ablation.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-24T14:53:57.363185+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-24T14:54:08.708919+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 ARR call for papers submission guidelines and author instructions:

## Key Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

### Important Deadlines
ARR submission deadline (long & short papers) May 25, 2026; Reviewer registration
…[truncated 2329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 11345
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-24T14:54:14.440583+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit template anonymization policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit template anonymization policy"
  }
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-24T14:54:14.842544+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-24T14:54:24.353147+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit template anonymization policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Now let me search for more specific information about page limits, template, and anonymization policy:

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics
…[truncated 2530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 9912
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-24T14:54:24.404295+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/decisions.yaml\", \"content\": \"_next_id: 20\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 12:00 UTC\\n  summary: MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性\\n  rationale: Track 1（探针迁移）是整个 3-track 研究的基础前提。如果残差流中无法检测冲突信号或跨语言完全不迁移，后续 SAE 分析和 steering\\n    均无意义。选 Qwen3-8B-Instruct 因 Qwen-Scope 提供 base SAE 便于后续 Track 2。选 EN+ZH 因语系距离大，若迁移成功则信号强。ConflictQA\\n    公开可用，无需等 CLEAR 数据。Pass/fail 标准参考 Brink et al. 单语 0.96 F1 和 Zhao et al. ~90% 探针精度。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 12:06 UTC\\n  summary: 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% conditional pass 定义、layer-wise\\n    量化标准、统计显著性要求（binomial p<0.01）、翻译 COMET gate（≥0.80）、FAIL→retry Llama 行动路径\\n  rationale: Reviewer 指出原 gate criteria 存在 ambiguous zone（70-79% 无定义）、layer-wise pattern\\n    逃逸条款过于模糊、ZH 60% 阈值缺统计锚定、翻译质量是迁移失败的混淆因素、FAIL 后行动未定义。全部采纳以确保 MVP 结论可靠。FAIL→retry\\n    on Llama 给予一次排除模型特异性的机会，两模型均 FAIL 才 kill。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 14:26 UTC\\n  summary: 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集\\n  rationale: Llama verify 保留率仅 33%（266/800 train），低于 300 阈值。ConflictQA 有 ~10K 条，扩至\\n    2000 可保证两模型各自 ≥300 有效样本。取消交集策略因为强制交集会进一步损失样本量，且跨模型对比不要求相同样本——各自 verified 集上报告相同指标即可，交集作为补充分析。20%\\n    标签翻转率确认了 M001 verify 步骤的必要性。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: triggered_decision\\n    result: verify 保留率 33%, 266 train / 70 test, 20% flip\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-21 19:17 UTC\\n  summary: Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨语言迁移不对称（ZH→EN 71.3% vs\\n    EN→ZH 59.6%），等 Qwen 结果做最终 verdict\\n  rationale: Llama 4 方向探针结果显示冲突信号可线性检测（所有方向 p < 0.01），但 EN→EN 未达 80% PASS 阈值（77.6%）。跨语言迁移存在但高度不对称：ZH→EN\\n    强迁移（71.3%），EN→ZH 弱迁移（59.6%，刚好低于 60% point 阈值但 p=9.7e-4 仍显著）。CONDITIONAL PASS 按\\n    D002 规则进入 EXTEND 评估。等 Qwen 跨模型
…[truncated 10908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9561
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-24T14:54:32.434250+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-24T14:54:32.886117+00:00_

-rw-r--r-- 1 ubuntu ubuntu 318958 May 24 14:12 /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-24T14:54:33.388221+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/clkc_mech_interp/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/clkc_mech_interp/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-prod42"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-24T14:54:33.840186+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-24T14:54:33.991185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-24T14:54:34.041835+00:00_

1	% References for Cross-Lingual Knowledge Conflict paper
2	% Auto-generated from literature_map.yaml
3	
4	@article{basu2026interpretability,
5	  author    = {Basu, S. and others},
6	  title     = {Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations},
7	  journal   = {arXiv preprint arXiv:2603.18353},
8	  year      = {2026},
9	  url       = {https://arxiv.org/abs/2603.18353}
10	}
11	
12	@article{brink2026probing,
13	  author    = {Brink, I. and Boer, A. and Ulmer, D.},
14	  title     = {Probing for Knowledge Attribution in Large Language Models},
15	  journal   = {arXiv preprint arXiv:2602.22787},
16	  year      = {2026},
17	  url       = {https://arxiv.org/abs/2602.22787}
18	}
19	
20	@inproceedings{ifergan2024beneath,
21	  author    = {Ifergan, M. and Choshen, L. and Aharoni, R. and Szpektor, I. and Abend, O.},
22	  title     = {Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in {LLMs}},
23	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
24	  year      = {2024},
25	  url       = {https://arxiv.org/abs/2408.10646}
26	}
27	
28	
29	@inproceedings{li2025taming,
30	  author    = {Li, G. and Chen, Y. and Tong, H.},
31	  title     = {Taming Knowledge Conflicts in Language Models},
32	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2503.10996}
35	}
36	
37	@article{pham2026where,
38	  author    = {Pham, M.V. and Borkakoty, H. and Hou, Y.},
39	  title     = {Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models},
40	  journal   = {arXiv preprint arXiv:2601.09445},
41	  year      = {2026},
42	  url       = {https://arxiv.org/abs/2601.09445}
43	}
44	
45	
46	@inproceedings{wang2025lost,
47	  author    = {Wang, M. and Adel, H. and Lange, L. and others},

…[truncated 2611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-24T14:54:37.705946+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-24T14:54:38.258598+00:00_

100	  url       = {https://arxiv.org/abs/2601.07041}
101	}
102	
103	@inproceedings{wu2020emerging,
104	  author    = {Wu, S. and Conneau, A. and Li, H. and Zettlemoyer, L. and Stoyanov, V.},
105	  title     = {Emerging Cross-lingual Structure in Pretrained Language Models},
106	  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)},
107	  year      = {2020},
108	  url       = {https://aclanthology.org/2020.acl-main.536/},
109	  doi       = {10.18653/v1/2020.acl-main.536}
110	}
111	
112	@inproceedings{wendler2024llamas,
113	  author    = {Wendler, C. and Veselovsky, V. and Monea, G. and West, R.},
114	  title     = {Do Llamas Work in {English}? On the Latent Language of Multilingual Transformers},
115	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
116	  year      = {2024},
117	  url       = {https://arxiv.org/abs/2402.10588}
118	}
119	
120	@inproceedings{muller2021first,
121	  author    = {Muller, B. and Elazar, Y. and Sagot, B. and Seddah, D.},
122	  title     = {First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual {BERT}},
123	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
124	  year      = {2021},
125	  url       = {https://aclanthology.org/2021.eacl-main.189/}
126	}
127	
128	@inproceedings{kargaran2024mexa,
129	  author    = {Kargaran, A.H. and Modarressi, A. and Nikeghbal, N. and Diesner, J. and Yvon, F. and Sch{\"u}tze, H.},
130	  title     = {{MEXA}: Multilingual Evaluation of {English}-Centric {LLMs} via Cross-Lingual Alignment},
131	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
132	  year      = {2024},
133	  url       = {https://arxiv.org/abs/2410.05873}
134	}
135	
136	@article{belinkov2022probing,
137	  author    = {Belinkov, Y.},
138	  title     = {Probing Classifiers: Promises, Shortcom
…[truncated 3836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-24T14:54:38.561036+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-24T14:54:39.269220+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_mvp_llama_phase_a_20260521T133704.log:231:[Omitted long matching line]
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-24T14:54:46.715138+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/agent"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-24T14:54:46.765991+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_director_647e2400.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-24T14:54:50.731750+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -name \"*.yaml\" -not -path \"*/logs/*\" -not -path \"*/.claude/*\" 2>/dev/null | head -20",
  "description": "Find yaml config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -name \"*.yaml\" -not -path \"*/logs/*\" -not -path \"*/.claude/*\" 2>/dev/null | head -20",
    "description": "Find yaml config files in project"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-24T14:54:50.932967+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/dream_registry.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/writing_plan.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/registry.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/mistakes.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/review_context.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/meta.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/review_context.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/native_functions.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/tags.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/derivatives.yaml
/home/ubuntu/.agent-ml-research-prod42/projec
…[truncated 578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-24T14:54:58.216727+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/registry.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/registry.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-24T14:54:58.518413+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-24T14:54:58.871161+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-prod42",
  "glob": "**/project*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-prod42",
    "glob": "**/project*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-24T14:54:58.971974+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-24T14:55:04.601551+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-24T14:55:04.652245+00:00_

NOT_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-24T14:55:28.701336+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "clkc_mech_interp",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "clkc_mech_interp",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-24T14:55:49.745592+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21044
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-24T14:55:49.999650+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查本文的**方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制, unlimited references, mandatory limitations section (不计入页数)\n- **模板**: ACL template with [review] option\n- **匿名规则**: Double-blind\n\n## 论文信息\n- **标题**: Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n- **论文路径**: projects/clkc_mech_interp/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **实验设计的合理性**：\n   - ConflictQA 数据集的使用是否合理？parametric knowledge verification 流程是否充分？\n   - 跨语言翻译流程（Qwen3-8B pipeline）是否引入 confound？COMET 验证是否充分？\n   - 三模型对比的公平性：样本量差异（Llama 1368 vs Qwen 966 vs Gemma 1590）是否影响结论？\n\n2. **统计方法**：\n   - Fisher's exact test + Bonferroni correction 的使用是否恰当？\n   - Bootstrap CI (n=2000) 是否足够？paired bootstrap 的实现是否正确？\n   - Steering 实验中 multiple comparison 的处理（k=10 alpha values, Bonferroni threshold 0.005）\n   - 单种子实验的可靠性（probing 结果）\n\n3. **因果推断的严谨性**：\n   - Representation steering 的方法论是否充分支持因果声明？\n   - Random direction control 是否是合适的对照？\n   - L13 成功 vs L28 失败的解释是否有 confounding factors？\n   - \"Detection ≠ Decision\" 的 claim 是否被数据充分支持？\n\n4. **跨模型泛化性**：\n   - Steering 仅在 Llama L13 成功，Qwen/Gemma 全部 negative——论文如何处理这个\"N=1 模型\"问题？\n   - Gemma 匹配条件重跑的 N=88 是否 underpowered？\n\n5. **Confound exclusion**：\n   - COMET tercile ablation 是否充分排除了翻译质量 confound？\n   - Token overlap analysis 是否全面？\n   - XNLI baseline comparison 的设计是否能充分支持 \"not conflict-specific\" 的结论？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分和简短理由"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查本文的**方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制, unlimited references, mandatory limitations section (不计入页数)\n- **模板**: ACL template with [review] option\n- **匿名规则**: Double-blind\n\n## 论文信息\n- **标题**: Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n- **论文路径**: projects/clkc_mech_interp/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **实验设计的合理性**：\n   - ConflictQA 数据集的使用是否合理？parametric knowledge verification 流程是否充分？\n   - 跨语言翻译流程（Qwen3-8B pipeline）是否引入 confound？COMET 验证是否充分？\n   - 三模型对比的公平性：样本量差异（Llama 1368 vs Qwen 966 vs Gemma 1590）是否影响结论？\n\n2. **统计方法**：\n   - Fisher's exact test + Bonferroni correction 的使用是否恰当？\n   - Bootstrap CI (n=2000) 是否足够？paired bootstrap 的实现是否正确？\n   - Steering 实验中 multiple comparison 的处理（k=10 alpha values, Bonferroni threshold 0.005）\n   - 单种子实验的可靠性（probing 结果）\n\n3. **因果推断的严谨性**：\n   - Representation steering 的方法论是否充分支持因果声明？\n   - Random direction control 是否是合适的对照？\n   - L13 成功 vs L28 失败的解释是否有 confounding factors？\n   - \"Detection ≠ Decision\" 的 claim 是否被数据充分支持？\n\n4. **跨模型泛化性**：\n   - Steering 仅在 Llama L13 成功，Qwen/Gemma 全部 negative——论文如何处理这个\"N=1 模型\"问题？\n   - Gemma 匹配条件重跑的 N=88 是否 underpowered？\n\n5. **Confound exclusion**：\n   - COMET tercile ablation 是否充分排除了翻译质量 confound？\n   - Token overlap analysis 是否全面？\n   - XNLI baseline comparison 的设计是否能充分支持 \"not conflict-specific\" 的结论？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分和简短理由"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-24T14:56:07.459626+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17459
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-24T14:56:07.610823+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查本文的**新颖性、学术贡献完整性、Related Work 覆盖度和写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制, unlimited references, mandatory limitations section (不计入页数)\n- **模板**: ACL template with [review] option\n- **匿名规则**: Double-blind\n\n## 论文信息\n- **标题**: Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n- **论文路径**: projects/clkc_mech_interp/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性和贡献评估**：\n   - 三个 claim 的独立新颖性：(1) 跨语言冲突可检测性+不对称性刻画, (2) Detection-Decision 层分离, (3) Confound exclusion pipeline\n   - 与现有工作的差异化：vs Zhao et al. 2024 (单语探针), vs Basu et al. 2026 (steering 失败), vs Wendler et al. 2024 (英语中心空间)\n   - \"Detection ≠ Decision\" 是否足够 novel 以支撑一篇 EMNLP long paper？\n   - Steering 仅在 Llama 一个模型成功——这个 contribution 的 generalizability 如何？\n\n2. **Related Work 完整性**：\n   - 是否遗漏了关键引用？特别是：\n     - Cross-lingual probing 的其他工作（如 Pires et al. 2019, Chi et al. 2020）\n     - Knowledge conflict resolution 的最新工作（2025-2026）\n     - Activation steering 的其他方法（activation patching, causal tracing, DAS）\n     - 多语言 LLM 内部表征的最新研究\n   - Related Work 的组织和覆盖是否平衡？\n\n3. **写作质量和清晰度**：\n   - Abstract 是否准确反映论文内容？是否在 200 words 限制内？\n   - Introduction 的 narrative flow 和 motivation 是否清晰？\n   - 论文结构是否合理？各节篇幅是否平衡？\n   - Figures 和 Tables 是否 self-contained、标注清晰？\n   - Limitations section 是否覆盖关键局限？\n\n4. **学术诚信和格式合规**：\n   - 匿名性检查：是否有 de-anonymization 风险？\n   - 引用格式是否正确、是否有 hallucinated citations？\n   - 页数是否符合 8 页限制？\n   - AI 使用声明是否符合 venue 要求？\n\n5. **论文 framing 和 positioning**：\n   - Title 是否准确反映内容？\n   - 论文是否 oversell（如将 Llama-specific 结果泛化为一般结论）或 undersell 其贡献？\n   - Conclusion 中的 future work 方向是否合理？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分和简短理由"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查本文的**新颖性、学术贡献完整性、Related Work 覆盖度和写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制, unlimited references, mandatory limitations section (不计入页数)\n- **模板**: ACL template with [review] option\n- **匿名规则**: Double-blind\n\n## 论文信息\n- **标题**: Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n- **论文路径**: projects/clkc_mech_interp/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性和贡献评估**：\n   - 三个 claim 的独立新颖性：(1) 跨语言冲突可检测性+不对称性刻画, (2) Detection-Decision 层分离, (3) Confound exclusion pipeline\n   - 与现有工作的差异化：vs Zhao et al. 2024 (单语探针), vs Basu et al. 2026 (steering 失败), vs Wendler et al. 2024 (英语中心空间)\n   - \"Detection ≠ Decision\" 是否足够 novel 以支撑一篇 EMNLP long paper？\n   - Steering 仅在 Llama 一个模型成功——这个 contribution 的 generalizability 如何？\n\n2. **Related Work 完整性**：\n   - 是否遗漏了关键引用？特别是：\n     - Cross-lingual probing 的其他工作（如 Pires et al. 2019, Chi et al. 2020）\n     - Knowledge conflict resolution 的最新工作（2025-2026）\n     - Activation steering 的其他方法（activation patching, causal tracing, DAS）\n     - 多语言 LLM 内部表征的最新研究\n   - Related Work 的组织和覆盖是否平衡？\n\n3. **写作质量和清晰度**：\n   - Abstract 是否准确反映论文内容？是否在 200 words 限制内？\n   - Introduction 的 narrative flow 和 motivation 是否清晰？\n   - 论文结构是否合理？各节篇幅是否平衡？\n   - Figures 和 Tables 是否 self-contained、标注清晰？\n   - Limitations section 是否覆盖关键局限？\n\n4. **学术诚信和格式合规**：\n   - 匿名性检查：是否有 de-anonymization 风险？\n   - 引用格式是否正确、是否有 hallucinated citations？\n   - 页数是否符合 8 页限制？\n   - AI 使用声明是否符合 venue 要求？\n\n5. **论文 framing 和 positioning**：\n   - Title 是否准确反映内容？\n   - 论文是否 oversell（如将 Llama-specific 结果泛化为一般结论）或 undersell 其贡献？\n   - Conclusion 中的 future work 方向是否合理？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分和简短理由"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-24T14:56:09.073247+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-24T14:56:21.144387+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 1 和 Reviewer 2 返回 Round 1 初审意见",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 1 和 Reviewer 2 返回 Round 1 初审意见",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-24T14:56:21.144895+00:00_

Next wakeup scheduled for 15:00:00 (in 219s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 64 · 2026-05-24T14:56:25.247738+00:00_

Reviewer 已全部启动，等待返回初审意见后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 65 · 2026-05-24T15:02:34.652096+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性、实验设计和统计分析）

### 总体评分

**Overall Assessment**: 3.5 — Borderline Conference

**一句话总结**: Probing 分析扎实且 confound exclusion 设计精心，但核心因果声明（Detection ≠ Decision）仅在单模型单层成立，多重比较校正方案存在争议，限制了结论的泛化性。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | Probing 实验设计合理，confound exclusion 系统化；但 steering 的多重比较校正不完整，"非冲突特异"声明缺乏正式等价性检验，单种子实验削弱可靠性 |
| Excitement | 3/5 | 问题重要且及时，XNLI baseline 对比有方法论启示；但 steering 仅 Llama 成功，核心因果发现的泛化性大打折扣 |
| Reproducibility | 3/5 | 提供了关键参数；但单种子、未公开代码/数据、probe 正则化系数未报告 |
| Reviewer Confidence | 4/5 | 熟悉 probing methodology、representation steering 和跨语言 NLP |

### Must-Fix 问题

**N1** [Critical] **Steering 实验的多重比较校正不完整，核心 p=0.002 可能不保真**
- 位置: Section 3.6, Section 4.6
- 主实验在 3 个层（L13, L18, L28）各测试 k=10 个 α 值，共 30 次检验。Bonferroni 仅在层内应用（0.05/10=0.005），未跨层校正。若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著。独立复现（N=201）缓解但非预注册。
- 建议: 明确说明为什么层间不需要校正（如预注册），或采用 FDR 校正，或报告完整 family-wise p 值。

**N2** [Critical] **因果声明的泛化性：N=1 模型问题**
- 位置: Abstract, Section 4.6 "Detection ≠ Decision", Discussion §5
- Steering 仅 Llama L13 成功，Qwen/Gemma 全部阴性（零翻转）。但论文框架性表述暗示这是 general principle。无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然。Gemma 88.9% probe accuracy 下零效应对 "probe direction = causal direction" 构成反证。
- 建议: 将 "Detection ≠ Decision" 限定为 Llama-specific，讨论 Qwen/Gemma 失败是否意味着因果结构可能非线性。

### Should-Fix 问题

**W1** [Major] 单种子实验——Table 1 所有结果基于单次 split，未报告多种子 mean ± std，peak layer 可能因 split 变化。

**W2** [Major] "非冲突特异"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验或 difference-in-differences 检验。

**W3** [Major] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），p=0.695/0.761 反映 power 不足而非无效应。Gemma 未报告。

**W4** [Major] 跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证。

**W5** [Minor] 翻译模型（Qwen3-8B）与实验对象重叠，未讨论此 confound。

**W6** [Minor] Table 3 caption "p < 0.05" 与正文 Bonferroni 阈值 0.005 不一致。

### Questions

Q1: Bonferroni 为什么按层而非按整个 steering 实验校正？是否有先验理由？
Q2: 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？
Q3: Gemma L21 cross-task transfer dip（0.730）与 alternating attention 架构的关系？
Q4: L13 和 L28 的 w_probe cosine similarity 是多少？
Q5: Qwen Δ_asym CI 包含零，如何支撑 "consistent across all three architectures"？

### Missing References
- Turner, Thacker, and Fry (2023): "Activation Addition"——steering 核心方法论文献
- Marks et al. (2024): "Geometry of Truth"——与跨任务 probe direction 共享分析直接相关

### 主要优势
- S1: 首次多架构/多语言知识冲突信号的系统性 probing 研究
- S2: Confound exclusion pipeline 设计周全（COMET/token overlap/XNLI/EN-DE）
- S3: XNLI baseline 对比有方法论启示价值
- S4: 对 negative results 的诚实处理（Gemma informative negative）
- S5: 独立复现（N=201）展示 causal gradient 空间精度
- S6: 写作清晰，结构完整

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-24T15:02:44.366264+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "120",
  "reason": "等待 Reviewer 2 返回 Round 1 初审意见",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "120",
    "reason": "等待 Reviewer 2 返回 Round 1 初审意见",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-24T15:02:44.366709+00:00_

Next wakeup scheduled for 15:05:00 (in 136s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-24T15:02:48.002474+00:00_

Reviewer 1 初审意见已收到。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 3

## Round 3

8 recorded events


### User

_source line 69 · 2026-05-24T15:02:49.086316+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations

### 总体评分

**Overall**: 3.0 / 5 — Findings
**一句话总结**: 方法论扎实、混淆排除设计巧妙，但核心 claim 之一（Detection ≠ Decision）仅在 1/3 模型上成立，跨语言扩展的新颖性相对于 Zhao et al. (2024) 较为增量，整体贡献不足以支撑 EMNLP 主会议 Long Paper。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 统计方法严谨（Bonferroni、paired bootstrap），混淆排除设计优秀；但核心因果 claim 仅基于 Llama 一个模型，single-seed probing，样本量偏小 |
| Excitement | 2.5 / 5 | 跨语言扩展较增量，不对称性发现可由已知 English-centric bias 预测；Detection ≠ Decision 有价值但 N=1 模型泛化性不足 |
| Overall Assessment | 3.0 / 5 | 适合 Findings track：方法论贡献有参考价值，但新颖性和结论强度不足以进入主会议 |
| Reproducibility | 3 / 5 | 方法描述详细但 single-seed、无代码/数据发布计划 |
| Confidence | 4 / 5 | 熟悉 cross-lingual probing、representation steering、knowledge conflict 等相关领域 |

---

### Must-Fix 问题

**N1** [Critical] Steering 仅在 Llama 成功，"Detection ≠ Decision" claim 的泛化性严重不足
- 位置：Section 4.6, Table 3, Section 5, Contributions bullet 2
- 论文最具新颖性的 claim（Detection-Decision Layer Dissociation）因果证据仅来自 Llama 一个模型。Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 0 flips) 均完全失败。一个仅在 1/3 模型上成立的因果发现难以支撑一般性结论。
- 建议：(a) 尝试 activation patching / DAS 等替代方法排除是 linear steering 本身的局限；(b) 明确降低 claim 强度；(c) 补充对 steering 失败的 mechanistic 解释。

**N2** [Critical] 新颖性增量性
- 位置：Contributions (Section 1), Section 4.2-4.3
- Contribution 1 是 Zhao et al. (2024) 的直接跨语言扩展；不对称性可从 Wendler et al. (2024) 和 Kargaran et al. (2024) 直接预测。Contribution 3（Confound Pipeline）虽有用但单独不足以支撑 long paper。三个 contributions = "增量扩展" + "N=1 case study" + "methodological toolkit"。

---

### Should-Fix 问题

**W1** [Major] Qwen3-8B 引用错误：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report (yang2024qwen25)。正确引用应为 arXiv:2505.09388。

**W2** [Major] 仅一个语言对 (EN-ZH) 但标题使用 "Cross-Lingual" 暗示一般性。EN-DE 仅在 confound exclusion 中简要提及。

**W3** [Major] Single-seed probing：所有结果基于单次种子训练，未考虑探针训练随机性。

**W4** [Minor] Related Work 遗漏：Pires et al. 2019, Chi et al. 2020, Meng et al. 2022 (activation patching), Geiger et al. 2024 (DAS)。

**W5** [Minor] 多个 bib 条目使用 "and others" 格式，作者信息不完整。

**W6** [Minor] Abstract 恰好 200 words，位于限制边界。

---

### 小问题
- "A suggestive MLP trend" 段不显著结果占过多篇幅，可移至 Appendix
- Table 3 中 Qwen/Gemma 行缺少具体 flip rates，与 Llama 行详细程度不一致
- Limitations 中 Gemma 88.9% 数字在正文中已多次重复

### Missing References
1. Pires et al. (2019) "How Multilingual is Multilingual BERT" — 跨语言 probing 开创性工作
2. Chi et al. (2020) "Finding Universal Grammatical Relations in Multilingual BERT"
3. Meng et al. (2022) "Locating and Editing Factual Associations in GPT" — activation patching 基础
4. Geiger et al. (2024) DAS — 替代因果干预方法
5. Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388) — 正确模型引用

### 主要优势
- S1: 混淆排除设计系统全面，为跨语言 probing 研究树立良好范式
- S2: 诚实报告负面结果（Qwen/Gemma steering 失败）
- S3: XNLI baseline 比较实验设计巧妙
- S4: 统计实践严谨（Bonferroni, paired bootstrap, 独立复制 N=201）
- S5: Discussion 部分有深度思考

---

[Reviewer 1 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：论文的 probing 分析（跨语言可检测性 + 方向不对称性 + confound exclusion）是扎实的，但两个 Critical 问题影响接收决定：(1) steering 实验的 Bonferroni 校正仅在层内而非跨层应用，导致 L13 p=0.002 在完整校正下可能不显著；(2) "Detection ≠ Decision" 作为论文核心贡献仅在 Llama 一个模型上成立，但论文的 framing 暗示其为 general principle。评分 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-24T15:03:08.273300+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n### Overall: 3.0 / 5 — Findings\n\n**N1** [Critical] Steering 仅在 Llama 成功，\"Detection ≠ Decision\" claim 的泛化性严重不足\n- 论文最具新颖性的 claim 因果证据仅来自 Llama 一个模型。Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 0 flips) 均完全失败。一个仅在 1/3 模型上成立的因果发现难以支撑一般性结论。\n- 建议：(a) 尝试 activation patching / DAS 等替代方法排除是 linear steering 本身的局限；(b) 明确降低 claim 强度；(c) 补充对 steering 失败的 mechanistic 解释。\n\n**N2** [Critical] 新颖性增量性\n- Contribution 1 是 Zhao et al. (2024) 的直接跨语言扩展；不对称性可从 Wendler et al. (2024) 和 Kargaran et al. (2024) 直接预测。Contribution 3（Confound Pipeline）虽有用但单独不足以支撑 long paper。三个 contributions = \"增量扩展\" + \"N=1 case study\" + \"methodological toolkit\"。\n\n**W1** [Major] Qwen3-8B 引用错误：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report (yang2024qwen25)。正确引用应为 arXiv:2505.09388。\n\n**W2** [Major] 仅一个语言对 (EN-ZH) 但标题使用 \"Cross-Lingual\" 暗示一般性。EN-DE 仅在 confound exclusion 中简要提及。\n\n**W3** [Major] Single-seed probing：所有结果基于单次种子训练，未考虑探针训练随机性。\n\n**W4** [Minor] Related Work 遗漏：Pires et al. 2019, Chi et al. 2020, Meng et al. 2022 (activation patching), Geiger et al. 2024 (DAS)。\n\n**W5** [Minor] 多个 bib 条目使用 \"and others\" 格式，作者信息不完整。\n\n**W6** [Minor] Abstract 恰好 200 words，位于限制边界。\n\n### Missing References\n1. Pires et al. (2019) \"How Multilingual is Multilingual BERT\"\n2. Chi et al. (2020) \"Finding Universal Grammatical Relations in Multilingual BERT\"\n3. Meng et al. (2022) \"Locating and Editing Factual Associations in GPT\"\n4. Geiger et al. (2024) DAS\n5. Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388)\n\n### 主要优势\n- S1: 混淆排除设计系统全面\n- S2: 诚实报告负面结果\n- S3: XNLI baseline 比较实验设计巧妙\n- S4: 统计实践严谨\n- S5: Discussion 部分有深度思考"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n### Overall: 3.0 / 5 — Findings\n\n**N1** [Critical] Steering 仅在 Llama 成功，\"Detection ≠ Decision\" claim 的泛化性严重不足\n- 论文最具新颖性的 claim 因果证据仅来自 Llama 一个模型。Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 0 flips) 均完全失败。一个仅在 1/3 模型上成立的因果发现难以支撑一般性结论。\n- 建议：(a) 尝试 activation patching / DAS 等替代方法排除是 linear steering 本身的局限；(b) 明确降低 claim 强度；(c) 补充对 steering 失败的 mechanistic 解释。\n\n**N2** [Critical] 新颖性增量性\n- Contribution 1 是 Zhao et al. (2024) 的直接跨语言扩展；不对称性可从 Wendler et al. (2024) 和 Kargaran et al. (2024) 直接预测。Contribution 3（Confound Pipeline）虽有用但单独不足以支撑 long paper。三个 contributions = \"增量扩展\" + \"N=1 case study\" + \"methodological toolkit\"。\n\n**W1** [Major] Qwen3-8B 引用错误：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report (yang2024qwen25)。正确引用应为 arXiv:2505.09388。\n\n**W2** [Major] 仅一个语言对 (EN-ZH) 但标题使用 \"Cross-Lingual\" 暗示一般性。EN-DE 仅在 confound exclusion 中简要提及。\n\n**W3** [Major] Single-seed probing：所有结果基于单次种子训练，未考虑探针训练随机性。\n\n**W4** [Minor] Related Work 遗漏：Pires et al. 2019, Chi et al. 2020, Meng et al. 2022 (activation patching), Geiger et al. 2024 (DAS)。\n\n**W5** [Minor] 多个 bib 条目使用 \"and others\" 格式，作者信息不完整。\n\n**W6** [Minor] Abstract 恰好 200 words，位于限制边界。\n\n### Missing References\n1. Pires et al. (2019) \"How Multilingual is Multilingual BERT\"\n2. Chi et al. (2020) \"Finding Universal Grammatical Relations in Multilingual BERT\"\n3. Meng et al. (2022) \"Locating and Editing Factual Associations in GPT\"\n4. Geiger et al. (2024) DAS\n5. Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388)\n\n### 主要优势\n- S1: 混淆排除设计系统全面\n- S2: 诚实报告负面结果\n- S3: XNLI baseline 比较实验设计巧妙\n- S4: 统计实践严谨\n- S5: Discussion 部分有深度思考"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-24T15:03:21.428586+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13155
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-24T15:03:21.583087+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n### Overall Assessment: 3.5 — Borderline Conference\n\n**N1** [Critical] Steering 实验的多重比较校正不完整，核心 p=0.002 可能不保真\n- 主实验在 3 个层（L13, L18, L28）各测试 k=10 个 α 值，共 30 次检验。Bonferroni 仅在层内应用（0.05/10=0.005），未跨层校正。若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著。独立复现（N=201）缓解但非预注册。\n- 建议: 明确说明为什么层间不需要校正（如预注册），或采用 FDR 校正，或报告完整 family-wise p 值。\n\n**N2** [Critical] 因果声明的泛化性：N=1 模型问题\n- Steering 仅 Llama L13 成功，Qwen/Gemma 全部阴性（零翻转）。但论文框架性表述暗示这是 general principle。无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然。Gemma 88.9% probe accuracy 下零效应对 \"probe direction = causal direction\" 构成反证。\n\n**W1** [Major] 单种子实验——Table 1 所有结果基于单次 split，未报告多种子 mean ± std，peak layer 可能因 split 变化。\n\n**W2** [Major] \"非冲突特异\"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验或 difference-in-differences 检验。\n\n**W3** [Major] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），p=0.695/0.761 反映 power 不足而非无效应。Gemma 未报告。\n\n**W4** [Major] 跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证。\n\n**W5** [Minor] 翻译模型（Qwen3-8B）与实验对象重叠，未讨论此 confound。\n\n**W6** [Minor] Table 3 caption \"p < 0.05\" 与正文 Bonferroni 阈值 0.005 不一致。\n\n### Questions\nQ1: Bonferroni 为什么按层而非按整个 steering 实验校正？\nQ2: 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？\nQ3: Gemma L21 cross-task transfer dip（0.730）与 alternating attention 架构的关系？\nQ4: L13 和 L28 的 w_probe cosine similarity 是多少？\nQ5: Qwen Δ_asym CI 包含零，如何支撑 \"consistent across all three architectures\"？\n\n### Missing References\n- Turner, Thacker, and Fry (2023): \"Activation Addition\"\n- Marks et al. (2024): \"Geometry of Truth\"\n\n### 主要优势\n- S1: 首次多架构/多语言知识冲突信号的系统性 probing 研究\n- S2: Confound exclusion pipeline 设计周全\n- S3: XNLI baseline 对比有方法论启示价值\n- S4: 对 negative results 的诚实处理\n- S5: 独立复现（N=201）展示 causal gradient 空间精度\n- S6: 写作清晰，结构完整"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n### Overall Assessment: 3.5 — Borderline Conference\n\n**N1** [Critical] Steering 实验的多重比较校正不完整，核心 p=0.002 可能不保真\n- 主实验在 3 个层（L13, L18, L28）各测试 k=10 个 α 值，共 30 次检验。Bonferroni 仅在层内应用（0.05/10=0.005），未跨层校正。若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著。独立复现（N=201）缓解但非预注册。\n- 建议: 明确说明为什么层间不需要校正（如预注册），或采用 FDR 校正，或报告完整 family-wise p 值。\n\n**N2** [Critical] 因果声明的泛化性：N=1 模型问题\n- Steering 仅 Llama L13 成功，Qwen/Gemma 全部阴性（零翻转）。但论文框架性表述暗示这是 general principle。无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然。Gemma 88.9% probe accuracy 下零效应对 \"probe direction = causal direction\" 构成反证。\n\n**W1** [Major] 单种子实验——Table 1 所有结果基于单次 split，未报告多种子 mean ± std，peak layer 可能因 split 变化。\n\n**W2** [Major] \"非冲突特异\"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验或 difference-in-differences 检验。\n\n**W3** [Major] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），p=0.695/0.761 反映 power 不足而非无效应。Gemma 未报告。\n\n**W4** [Major] 跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证。\n\n**W5** [Minor] 翻译模型（Qwen3-8B）与实验对象重叠，未讨论此 confound。\n\n**W6** [Minor] Table 3 caption \"p < 0.05\" 与正文 Bonferroni 阈值 0.005 不一致。\n\n### Questions\nQ1: Bonferroni 为什么按层而非按整个 steering 实验校正？\nQ2: 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？\nQ3: Gemma L21 cross-task transfer dip（0.730）与 alternating attention 架构的关系？\nQ4: L13 和 L28 的 w_probe cosine similarity 是多少？\nQ5: Qwen Δ_asym CI 包含零，如何支撑 \"consistent across all three architectures\"？\n\n### Missing References\n- Turner, Thacker, and Fry (2023): \"Activation Addition\"\n- Marks et al. (2024): \"Geometry of Truth\"\n\n### 主要优势\n- S1: 首次多架构/多语言知识冲突信号的系统性 probing 研究\n- S2: Confound exclusion pipeline 设计周全\n- S3: XNLI baseline 对比有方法论启示价值\n- S4: 对 negative results 的诚实处理\n- S5: 独立复现（N=201）展示 causal gradient 空间精度\n- S6: 写作清晰，结构完整"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-24T15:03:23.052257+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1469
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-24T15:03:35.423029+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "150",
  "reason": "等待 Reviewer 1 和 2 完成交叉分享回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "150",
    "reason": "等待 Reviewer 1 和 2 完成交叉分享回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-24T15:03:35.523838+00:00_

Next wakeup scheduled for 15:07:00 (in 205s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 76 · 2026-05-24T15:03:38.331718+00:00_

交叉分享已派发。两位 Reviewer 互相审阅对方意见并逐条回应 [AGREE]/[REBUT]。等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 77 · 2026-05-24T15:03:40.999634+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **Overall 3.0 / 5（Findings）**。核心判断依据：

1. **两个 Critical 问题**：Detection ≠ Decision 的因果证据仅在 Llama 1 个模型成立（N1）；整体新颖性相对于 Zhao et al. 2024 较增量（N2）
2. **三个 Major 问题**：Qwen3 引用错误（W1）、单一语言对（W2）、single-seed probing（W3）
3. **主要优势**：混淆排除 pipeline 设计优秀、统计实践严谨、负面结果诚实报告
4. **遗漏引用**：Pires 2019、Chi 2020、Meng 2022、Geiger 2024、Qwen3 正确引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-24T15:03:53.619636+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "120",
  "reason": "继续等待 Reviewer 1 和 2 的交叉分享 AGREE/REBUT 回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "120",
    "reason": "继续等待 Reviewer 1 和 2 的交叉分享 AGREE/REBUT 回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-24T15:03:53.670258+00:00_

Next wakeup scheduled for 15:06:00 (in 126s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-24T15:03:56.702593+00:00_

这是 Reviewer 2 原始审稿的确认摘要，交叉回应尚未返回。继续等待两位 Reviewer 的 [AGREE]/[REBUT] 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 5

## Round 5

4 recorded events


### User

_source line 81 · 2026-05-24T15:05:00.213081+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Must-Fix

[AGREE] R2-N1 (Steering 泛化性): 与我的 N2 一致。补充：R2 建议尝试 DAS 等替代方法是建设性的；但 R2 可能低估了 Gemma informative negative 的价值（Section 4.6, 88.9% probe accuracy 下零翻转排除了 probe quality confound）。

[REBUT] R2-N2 (新颖性增量): 部分不同意。(1) Contribution 1 不是 Zhao et al. (2024) 的简单扩展——方向不对称性 + XNLI 匹配是新发现，"可预测"≠"已验证"；(2) Contribution 3 不应独立评估，它是 Contribution 1 可靠性的支撑；(3) 但同意 Contribution 2 (N=1 因果) 偏弱。综合评估：novelty sufficient for Findings，可能 borderline Conference。

### Should-Fix

[AGREE] R2-W1 (Qwen3 引用错误): 事实性错误，必须更正。
[AGREE] R2-W2 (单语言对 vs 标题): 标题应加限定。
[AGREE] R2-W3 (Single-seed): 与我的 W1 一致。
[REBUT] R2-W4 (Related Work): 4篇中仅 Meng (2022) 和 Geiger (2024) DAS 应引用；Pires (2019) 和 Chi (2020) 非必要，论文已引用更直接的后续工作。
[AGREE] R2-W5 (Bib 格式): "and others" 截断需修复。
[REBUT] R2-W6 (Abstract 200 words): 200 words 完全合规，≤200 是硬限制，200 满足条件。

### Missing References
Meng (2022) 和 Geiger (2024) DAS: [AGREE] 应引用。
Pires (2019) 和 Chi (2020): [REBUT] 非必要。
Qwen3 Tech Report: [AGREE] 必须更正。

### 评分分歧
R2=3.0 vs R1=3.5。差异源自新颖性评估：我认为 Contribution 1+3 的组合具备独立方法论贡献，不应仅因 Contribution 2 的 N=1 问题降级。但若去掉 L13 阳性结果，同意应降至 2.5-3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-24T15:05:09.115909+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "90",
  "reason": "等待 Reviewer 2 对 Reviewer 1 的交叉回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "90",
    "reason": "等待 Reviewer 2 对 Reviewer 1 的交叉回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-24T15:05:09.266876+00:00_

Next wakeup scheduled for 15:07:00 (in 111s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 150
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-24T15:05:12.448942+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 85 · 2026-05-24T15:05:20.780474+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- R2 的 7 条意见中，我 **AGREE** 4 条（N1 steering 泛化性、W1 引用错误、W2 标题 scope、W3 单种子、W5 bib 格式）
- **REBUT** 3 条（N2 新颖性评估过严、W4 仅部分遗漏相关、W6 abstract 200 words 合规）
- Missing References 5 篇中认同 3 篇（Meng 2022、Geiger 2024 DAS、Qwen3 Tech Report），不认为 Pires 2019 和 Chi 2020 是必要引用
- 评分分歧 0.5 分（R1=3.5 vs R2=3.0），核心在于对 Contribution 1+3 组合价值的判断

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-24T15:05:31.845047+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "90",
  "reason": "等待 Reviewer 2 对 Reviewer 1 审稿意见的 AGREE/REBUT 回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "90",
    "reason": "等待 Reviewer 2 对 Reviewer 1 审稿意见的 AGREE/REBUT 回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: clkc_mech_interp\n- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-24T15:05:31.895691+00:00_

Next wakeup scheduled for 15:08:00 (in 148s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-24T15:05:34.625162+00:00_

Reviewer 1 交叉回应确认。仍在等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 7

## Round 7

10 recorded events


### User

_source line 89 · 2026-05-24T15:06:53.668496+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见

## 审查侧重：新颖性、学术贡献完整性、Related Work 覆盖度、写作质量

---

## 总体评分

**Overall**: 3.0 — Findings
**一句话总结**: 方法论设计扎实（confound exclusion pipeline + XNLI baseline），但核心贡献的新颖性有限（跨语言延伸 Zhao et al. 2024 + 已知 English-centric bias 的 re-confirmation），且最具新意的 Detection ≠ Decision 主张仅在 1/3 模型上成立，不足以支撑 EMNLP long paper 的 conference 级别。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论合理、统计实践整体规范，但核心因果声明基于 N=1 模型，single-seed split，confound exclusion 功效不足 |
| Excitement | 2.5/5 | 跨语言延伸和不对称性发现属 incremental；Detection ≠ Decision 有洞察但泛化性不足 |
| Reproducibility | 3/5 | 实验细节基本充足，但 single seed、无代码发布声明、翻译 pipeline 依赖特定模型版本 |
| Reviewer Confidence | 4/5 | 熟悉 cross-lingual probing、representation steering 和 knowledge conflict 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] 新颖性不足以支撑 EMNLP Long Paper
- 具体位置：Section 1（Contributions），全文
- 问题：三个 contribution 的独立新颖性均有限：
  - (1) 跨语言冲突可检测性+不对称性：是 Zhao et al. (2024) 从单语到跨语言的直接延伸。不对称性结果（ZH→EN > EN→ZH ~7pp）在 English-centric bias 已被 Wendler et al. (2024) 和 Kargaran et al. (2024) 充分记录的背景下，属 expected finding。论文本身也承认 "it inherits from the model's general multilingual structure"（Abstract），这实际上削弱了此 contribution 的新颖性。
  - (2) Detection-Decision 层分离：最有潜力的贡献，但仅在 Llama 一个模型上成立（Section 4.6）。Qwen 和 Gemma 均为零翻转（Table 3/5）。论文将其定性为 "architecture-specific"（Section 5），但这意味着该发现的 generalizability 极其有限。
  - (3) Confound exclusion pipeline：方法论贡献有价值，但作为独立 contribution 略显薄弱——本质上是 best practice checklist（COMET 分层 + token overlap + XNLI baseline），而非新方法。
- 为什么影响接收：对于 EMNLP long paper（非 Findings），至少需要一个 contribution 具有足够的 novelty 和 generalizability。当前最强贡献（Detection ≠ Decision）受限于 N=1 模型。
- 建议修改方向：(a) 增加至少一个非 Llama 模型的因果干预成功案例（或使用非线性干预方法如 activation patching），(b) 或将论文重新定位为 Findings-level 的实证研究，弱化因果声明。

**N2** [Critical] Qwen3 引用错误
- 具体位置：Section 4.1，references.bib 中 `yang2024qwen25`
- 问题：论文声称使用 "Qwen3-8B"（36 layers），但引用的是 Qwen2.5 Technical Report（arXiv:2412.15115）。Qwen3 Technical Report 于 2025 年 5 月发表（arXiv:2505.09388），是独立论文。这是明确的引用错误。Qwen3-8B（36 layers, 8.2B params）与 Qwen2.5-7B（28 layers）架构完全不同。
- 为什么影响接收：引用错误损害学术诚信，且审稿人无法验证模型规格是否正确。
- 建议修改方向：替换为正确的 Qwen3 引用 (Yang et al., 2025; arXiv:2505.09388)。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] Related Work 遗漏关键引用
- 具体位置：Section 2
- 问题：以下重要相关工作未被引用：
  - **Pires et al. (2019)** "How Multilingual is Multilingual BERT?"——cross-lingual probing 的奠基性工作，首次系统研究了零样本跨语言迁移，是 Section 2 第二段（cross-lingual representations）的直接前驱。
  - **Chi et al. (2020)** "Finding Universal Grammatical Relations in Multilingual BERT"——跨语言表征中共享子空间的 structural probing，与本文 cross-task language probe transfer（Section 5 第三段）直接相关。
  - **Meng et al. (2022)** "Locating and Editing Factual Associations in GPT"——causal tracing / activation patching 的奠基工作。论文在 Conclusion 中提到 activation patching 作为 future work，却未引用这一方法的原始论文。
  - **Geiger et al. (2024)** "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations"——DAS（Distributed Alignment Search）是 causal intervention 的重要替代方法，与 Section 2 第三段（representation steering and causal intervention）直接相关。
- 建议：在 Section 2 各对应段落补充上述引用，并讨论本文方法与 activation patching / DAS 的区别。

**W2** [Major] 论文存在 Oversell 倾向
- 具体位置：Title, Abstract, Section 1
- 问题：标题 "Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations" 暗示一般性结论，但实验仅覆盖一个语言对（EN-ZH）。EN-DE 数据仅在 Section 4.5 confound exclusion 中作为辅助分析出现，不构成主要实验。Abstract 中 "Conflict signals are linearly detectable across languages" 的表述未限定为 EN-ZH。Section 1 contributions 中 "the first evidence" 也有 oversell 嫌疑——Zhao et al. (2024) 已在单语中证明了可检测性，跨语言延伸是增量而非 "first"。
- 建议：(a) 标题和 abstract 中明确限定为 EN-ZH，(b) 将 "first evidence" 修改为 "first cross-lingual evidence"。

**W3** [Major] Bib 条目格式不规范
- 具体位置：references.bib
- 问题：多个 bib 条目使用 `and others` 代替完整作者列表（如 `{Basu, S. and others}`, `{Zhao, J. and others}`, `{Wang, M. and Adel, H. and Lange, L. and others}`）。ACL 模板要求完整作者列表或标准 `et al.` 格式。当前格式在编译后可能产生不规范的引用显示。
- 建议：补全所有作者列表，或至少列出前三位作者。

**W4** [Minor] 翻译模型与实验对象重叠（同意 R1-W5）
- 具体位置：Section 3.2, Section 4.1
- 问题：Qwen3-8B 同时用作翻译模型和实验对象。翻译输出可能对 Qwen 的 representation space 存在系统性偏好，导致 Qwen 的跨语言 probe transfer 结果受到 confound。论文未讨论此问题。
- 建议：在 Limitations 中讨论，或额外使用独立翻译模型（如 NLLB）验证 Qwen 子集结果的鲁棒性。

**W5** [Minor] Abstract 恰好 200 words
- 具体位置：Abstract
- 问题：经计算（去除 LaTeX 命令后），abstract 恰好 200 words，处于 EMNLP 2026 限制的临界值。不同的 word count 工具可能给出略有不同的结果。建议留出安全余量。
- 建议：精简至 190 words 以下。

---

## 小问题（不影响接收）

- Figure 1 的三个子图使用相同的 y 轴范围，但 Gemma 有 42 层（x 轴范围更大），导致视觉上的密度不一致，建议统一按 relative depth (%) 为 x 轴。
- Section 5 "A suggestive MLP trend" 段落提出了 MLP sublayer 的观察但 CI 包含零——这种 "suggestive" 表述在审稿中容易被视为 cherry-picking，建议删除或移至 appendix。
- Discussion Section 5 "Direct evidence for a shared cross-lingual subspace" 中 cross-task probe transfer 实验（conflict→XNLI 达到 0.96+）是重要结果，但仅出现在 Discussion 中而非 Experiments，结构安排不佳。

---

## 主要优势

- **S1**: Confound exclusion pipeline（COMET tercile + token overlap + XNLI baseline）设计周全，对未来跨语言 probing 研究有方法论参考价值。
- **S2**: XNLI baseline 对比是巧妙的实验设计——用同一 pipeline 对比非冲突任务，为 "不对称性非冲突特异" 提供了有力证据。
- **S3**: Negative results 的诚实报告（Qwen/Gemma steering 失败）值得赞赏，避免了 publication bias。
- **S4**: 独立复现（N=201, Appendix B）展示了 L13 周围的 causal gradient 空间精度，增强了 Llama 结果的可信度。
- **S5**: 写作整体清晰，论文结构合理，Discussion 中对结果的解读比较审慎（如 "architecture-specific" 限定）。

---

## 对 Reviewer 1 意见的逐条回应

### Must-Fix

[AGREE] R1-N1: Bonferroni 跨层校正问题
同意这是一个合理的统计关切。论文 Method Section 3.6 明确将 Bonferroni 校正范围定义为 "per model as an independent family"，但实际在 Llama 上测试了 3 个层 × 10 个 α，共 30 次比较。正方向 p=0.002 在 0.05/30≈0.00167 阈值下确实不再显著。不过有两个缓解因素：(a) 负方向 p < 0.001 仍然存活完整的 family-wise 校正；(b) 独立复现（N=201, Appendix B Table 4）在 L13 获得 p < 0.001。整体结论仍然成立，但作者应明确报告完整 family-wise p 值或采用 FDR 校正，并解释为何未使用 Holm-Bonferroni 等更精细的方法。

[AGREE] R1-N2: N=1 模型因果声明
完全同意。这是本文最核心的局限。论文 Discussion 中确实限定为 "architecture-specific"（Section 5 第一段），但 Abstract 和 Introduction 中的 framing 仍然偏向一般性结论（如 "A dissociation emerges between detection and decision"，未加限定词）。Gemma 88.9% probe accuracy 下零因果效应（Table 5）是对 "probe direction = causal direction" 假设的强力反证。建议 Abstract 和 Introduction 的相关表述显式加上 "in Llama" 限定。

### Should-Fix

[AGREE] R1-W1: 单种子实验
同意。Table 1 所有结果基于 single train/test split，peak layer 位置和准确率可能因 split 不同而变化。对于探测研究，至少报告 3-5 个种子的 mean ± std 是标准实践（Belinkov, 2022 中有讨论）。

[AGREE] R1-W2: CI 重叠不等于等价性检验
同意。论文声称 conflict asymmetry "matches" XNLI baseline（Section 4.4），但仅基于 CI 重叠。CI 重叠是必要条件但非充分条件。正式的 TOST 等价性检验或 difference-in-differences 分析会更 rigorous。当前论据在技术上只能支持 "未能拒绝两者不同" 的弱结论，而非 "两者等价"。

[AGREE] R1-W3: COMET tercile 功效不足
同意，且补充一点：Gemma 的 COMET 分析缺失（Table 2 仅报告 Qwen 和 Llama），这是一个遗漏。每 tercile 64-91 样本的 Fisher exact test 功效很低，p=0.695/0.761 无法区分 "无效应" 和 "功效不足以检测效应"。建议至少报告效应量和功效分析。

[AGREE] R1-W4: 跨模型不同样本子集
同意这是一个关切，但补充：这在一定程度上是实验设计的固有约束——必须排除模型无法正确回答参数知识的样本。建议在 Limitations 中讨论，并报告三个模型样本集的重叠度。

[AGREE] R1-W5: 翻译模型与实验对象重叠
同意，已在我的 W4 中独立提出。

[AGREE] R1-W6: Table 3 caption 与 Bonferroni 阈值不一致
同意。Table 3 caption 说 "Significant results (p < 0.05) in bold"（我在 PDF 中确认），但正文 Section 3.6 和 4.6 明确使用 Bonferroni 校正阈值 0.005。这是一个明显的不一致，应统一为 Bonferroni 校正后的阈值。

### Questions

Q1: 我同意 R1 的关切。论文应解释为何选择层内而非全实验范围的校正。一个合理的论据是 "每层是一个独立假设（此层是否有因果效应）"，但这需要在论文中显式陈述。

Q2: 独立复现的时序很重要。论文 Section 4.6 的措辞（"An independent replication with separately sampled data"）暗示是事后进行的。如果是 post-hoc，应明确声明，这不影响结果的有效性但影响统计解读。

Q3: 有意义的问题。Gemma-2 使用 alternating local/global attention architecture，L21 的 cross-task transfer dip（0.730, Section 5 第三段）可能与此有关。论文未深入探讨。

Q4: 同意这是一个重要的缺失分析。L13 和 L28 的 w_probe cosine similarity 可以帮助理解 Detection ≠ Decision 的机制——如果两个方向正交，说明模型在不同层编码不同信息；如果高度相似，说明同一信息在不同层的因果地位不同。

Q5: 同意。Qwen Δ_asym CI 为 [-0.6, 13.7]，包含零。论文 Section 4.3 承认 "While the Qwen CI marginally includes zero"，但后续表述（如 Section 5 "consistent across all three architectures"）忽略了此细节。建议改为 "consistent in direction across all three architectures, though the Qwen effect does not reach significance"。

### Missing References

[AGREE] Turner et al. (2023) "Activation Addition"——与 Section 2 第三段（representation steering）和 Section 3.6 直接相关。ActAdd 是 ITI (Li et al., 2023) 之外的主要 steering 方法，应被讨论。

[AGREE] Marks & Tegmark (2024) "The Geometry of Truth"——与本文的线性 probing + causal intervention 范式直接相关。该工作同样发现线性 probe 方向具有因果效应（通过 mass-mean probing），是 "Detection = Decision" 的正面案例，与本文的 Llama L13 结果呼应，与 Qwen/Gemma 失败形成对比。

**Reviewer 2 补充的 Missing References**（R1 未提及）：
- **Pires et al. (2019)** "How Multilingual is Multilingual BERT?"——cross-lingual probing 奠基工作
- **Chi et al. (2020)** "Finding Universal Grammatical Relations in Multilingual BERT"——跨语言共享子空间的 structural probing
- **Meng et al. (2022)** "Locating and Editing Factual Associations in GPT"——causal tracing 的奠基论文，论文在 Conclusion 中提到 activation patching 却未引用
- **Geiger et al. (2024)** "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations"——DAS 方法，causal intervention 的重要替代

---

## Reviewer 2 独立发现的额外问题（R1 未覆盖）

1. **[Critical] Qwen3 引用错误**（我的 N2）：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report，这是事实错误。
2. **[Major] 论文 framing oversell**（我的 W2）：标题和 abstract 的一般性表述超出了 EN-ZH 单一语言对的实验范围。
3. **[Major] Bib 条目格式问题**（我的 W3）：多个条目使用非标准 "and others" 格式。
4. **[Major] Related Work 遗漏多项关键引用**（我的 W1）：Pires 2019、Chi 2020、Meng 2022、Geiger 2024。
5. **[Minor] 重要实验结果（cross-task probe transfer）放在 Discussion 而非 Experiments**。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-24T15:07:25.170496+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-24T15:07:25.221316+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T14:55:32.153980+00:00\", \"completed_at\": \"2026-05-24T14:57:52.369868+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页全为纯文本，无任何 display item（figure/table/equation）。审稿人直到第 4 页才看到第一个视觉锚点（Figure 1）。对于实证为主的论文，建议在第 1-2 页添加 pipeline overview 图或核心结果 teaser，帮助审稿人快速建立认知框架\"}, {\"severity\": \"warning\", \"dimension\": \"page 7-8\", \"message\": \"连续 2 页纯文本（Discussion + Conclusion + Limitations），无任何 display item 穿插。Discussion 部分可考虑加入一个总结性 figure 或 comparison table 打破视觉单调\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Figure 1 为单栏宽度（约 3.3 inch）内含 3 列子图（Llama/Qwen/Gemma），每个子图极窄。轴标签、tick label、legend 字号明显小于正文 70%，打印后可读性差。建议改为 figure*（双栏全宽）或减少子图数量\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页仅 2 个 figure + 3 个 table = 5 个 display items（0.625/页）。对于实证驱动论文偏少（通常 5-8 个），视觉密度不足。可考虑将 Appendix Table 4/5 中的关键结果提升至正文，或为 confound exclusion pipeline（§3.5）添加流程图\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 caption 基本自包含（说明了线型含义、星号标记、垂直标注），但未明确说明 y 轴\\\"越高越好\\\"或 balanced accuracy 的基线水平（chance = 50%），对不熟悉该指标的审稿人不够友好\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 使用灰色带标注 ±5pp equivalence zone，设计合理。但数据点仅 6 个（3 模型 × 2 任务），图表信息密度较低，可考虑合并为 Table 1 的一部分或用 grouped bar chart 增加信息量\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，小数精度一致（1 位小数），格式规范。脚注解释 Δ_asym 定义清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 和 Table 3 格式统一，booktabs 风格，显著性标注清晰（p 值 + Bonferroni 校正标记）。Table 3 较宽但未溢出栏宽\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，符合 ACL 匿名提交格式。无拥挤感\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"\\\"A Use of AI Assistants\\\" 节出现在 Limitations 之后、References 之前，位置合理\"}, {\"sever
…[truncated 465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-24T15:07:25.372203+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-24T15:07:25.524044+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-24T15:08:32.602265+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "clkc_mech_interp",
  "issues_yaml": "issues:\n- id: \"R1-N1\"\n  summary: \"Steering 实验 Bonferroni 校正仅层内应用，未跨层校正（30次比较），L13 正方向 p=0.002 在完整校正下不显著\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。独立复现(N=201) p<0.001 和负方向 p<0.001 部分缓解，但需明确报告 family-wise p 值\"\n  action_items:\n    - round: 1\n      action: \"明确说明层间不校正的理由或采用 FDR/Holm-Bonferroni 校正，报告完整 family-wise p 值\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 一个模型成立（N=1），Qwen/Gemma 零翻转，泛化性严重不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致认为这是论文最核心局限。R2 建议尝试 DAS/activation patching 或降低 claim 强度。R1 指出 Gemma 88.9% probe acc 下零效应构成反证\"\n  action_items:\n    - round: 1\n      action: \"Abstract/Intro 中 Detection≠Decision 表述加 'in Llama' 限定；讨论 steering 失败是否反映非线性因果结构\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Qwen3-8B 引用错误：引用了 Qwen2.5 Technical Report (arXiv:2412.15115) 而非 Qwen3 (arXiv:2505.09388)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误，R1 AGREE 必须更正\"\n  action_items:\n    - round: 1\n      action: \"替换 references.bib 中 yang2024qwen25 为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"单种子实验：所有 probing 结果基于单次 train/test split，未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。Peak layer 位置和准确率可能因 split 不同而变化\"\n  action_items:\n    - round: 1\n      action: \"报告 3-5 个种子的 mean±std，或至少讨论为何单种子足够\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"非冲突特异声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE。CI 重叠是必要非充分条件。当前仅支持'未能拒绝两者不同'的弱结论\"\n  action_items:\n    - round: 1\n      action: \"补充 TOST 或 difference-in-differences 检验，或弱化'matches'表述\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 分析统计功效不足（每 tercile 64-91 样本），Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE 并补充 Gemma 缺失。p=0.695/0.761 无法区分无效应和功效不足\"\n  action_items:\n    - round: 1\n      action: \"报告效应量和功效分析；补充 Gemma COMET 结果\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"标题和 Abstract 使用 Cross-Lingual 暗示一般性，但实验仅覆盖 EN-ZH 一个语言对\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加限定。EN-DE 仅在 confound exclusion 中简要使用\"\n  action_items:\n    - round: 1\n      action: \"标题和 abstract 限定为 EN-ZH，或扩展为更多语言对\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE 但指出是实验设计固有约束。建议在 Limitations 讨论并报告重叠度\"\n  action_items:\n    - round: 1\n      action: \"报告三模型样本集重叠度，在 Limitations 讨论影响\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Related Work 遗漏关键引用：Meng 2022, Geiger 2024, Turner 2023, Marks 2024\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意 Meng 和 Geiger 必须引用，Turner 和 Marks 也应引用。对 Pires 2019/Chi 2020 有分歧（R1 认为非必要）\"\n  action_items:\n    - round: 1\n      action: \"至少补充 Meng 2022, Geiger 2024, Turner 2023, Marks 2024 引用\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Bib 条目使用非标准 'and others' 格式，作者信息不完整\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE。ACL 模板要求完整作者列表\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目作者列表\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 (Qwen3-8B) 与实验对象重叠，未讨论 confound\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。翻译输出可能对 Qwen 的 representation space 有系统性偏好\"\n  action_items:\n    - round: 1\n      action: \"在 Limitations 讨论，或用独立翻译模型验证 Qwen 子集\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 'p<0.05' 与正文 Bonferroni 阈值 0.005 不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE。应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一 Table 3 caption 显著性阈值描述\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "clkc_mech_interp",
    "issues_yaml": "issues:\n- id: \"R1-N1\"\n  summary: \"Steering 实验 Bonferroni 校正仅层内应用，未跨层校正（30次比较），L13 正方向 p=0.002 在完整校正下不显著\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。独立复现(N=201) p<0.001 和负方向 p<0.001 部分缓解，但需明确报告 family-wise p 值\"\n  action_items:\n    - round: 1\n      action: \"明确说明层间不校正的理由或采用 FDR/Holm-Bonferroni 校正，报告完整 family-wise p 值\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 一个模型成立（N=1），Qwen/Gemma 零翻转，泛化性严重不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致认为这是论文最核心局限。R2 建议尝试 DAS/activation patching 或降低 claim 强度。R1 指出 Gemma 88.9% probe acc 下零效应构成反证\"\n  action_items:\n    - round: 1\n      action: \"Abstract/Intro 中 Detection≠Decision 表述加 'in Llama' 限定；讨论 steering 失败是否反映非线性因果结构\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Qwen3-8B 引用错误：引用了 Qwen2.5 Technical Report (arXiv:2412.15115) 而非 Qwen3 (arXiv:2505.09388)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误，R1 AGREE 必须更正\"\n  action_items:\n    - round: 1\n      action: \"替换 references.bib 中 yang2024qwen25 为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"单种子实验：所有 probing 结果基于单次 train/test split，未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。Peak layer 位置和准确率可能因 split 不同而变化\"\n  action_items:\n    - round: 1\n      action: \"报告 3-5 个种子的 mean±std，或至少讨论为何单种子足够\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"非冲突特异声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE。CI 重叠是必要非充分条件。当前仅支持'未能拒绝两者不同'的弱结论\"\n  action_items:\n    - round: 1\n      action: \"补充 TOST 或 difference-in-differences 检验，或弱化'matches'表述\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 分析统计功效不足（每 tercile 64-91 样本），Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE 并补充 Gemma 缺失。p=0.695/0.761 无法区分无效应和功效不足\"\n  action_items:\n    - round: 1\n      action: \"报告效应量和功效分析；补充 Gemma COMET 结果\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"标题和 Abstract 使用 Cross-Lingual 暗示一般性，但实验仅覆盖 EN-ZH 一个语言对\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加限定。EN-DE 仅在 confound exclusion 中简要使用\"\n  action_items:\n    - round: 1\n      action: \"标题和 abstract 限定为 EN-ZH，或扩展为更多语言对\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE 但指出是实验设计固有约束。建议在 Limitations 讨论并报告重叠度\"\n  action_items:\n    - round: 1\n      action: \"报告三模型样本集重叠度，在 Limitations 讨论影响\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Related Work 遗漏关键引用：Meng 2022, Geiger 2024, Turner 2023, Marks 2024\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意 Meng 和 Geiger 必须引用，Turner 和 Marks 也应引用。对 Pires 2019/Chi 2020 有分歧（R1 认为非必要）\"\n  action_items:\n    - round: 1\n      action: \"至少补充 Meng 2022, Geiger 2024, Turner 2023, Marks 2024 引用\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Bib 条目使用非标准 'and others' 格式，作者信息不完整\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE。ACL 模板要求完整作者列表\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目作者列表\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 (Qwen3-8B) 与实验对象重叠，未讨论 confound\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。翻译输出可能对 Qwen 的 representation space 有系统性偏好\"\n  action_items:\n    - round: 1\n      action: \"在 Limitations 讨论，或用独立翻译模型验证 Qwen 子集\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 'p<0.05' 与正文 Bonferroni 阈值 0.005 不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE。应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一 Table 3 caption 显著性阈值描述\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-24T15:08:32.703136+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml\", \"bytes\": 5810}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-24T15:10:04.768299+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review\n**审稿模式**: Fresh (Round 1)\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/完整性/写作）\n\n---\n\n## Summary\n\n本文研究多语言 LLM 中跨语言知识冲突信号的可检测性和因果相关性。通过 Llama-3.1-8B-Instruct、Qwen3-8B 和 Gemma-2-9B-IT 三个模型的残差流 probing，发现冲突信号可跨语言线性检测，ZH→EN 迁移优于 EN→ZH 约 7pp，且该不对称性与 XNLI 非冲突基线匹配（非冲突特异性）。Representation steering 在 Llama L13（41% depth）成功（Fisher p=0.002），但在 L28（probe peak, 88%）及 Qwen/Gemma 中均失败，揭示 Detection ≠ Decision 层分离。\n\n---\n\n## Strengths\n\n- **S1**: 首次多架构/多语言知识冲突信号的系统性 probing 研究，填补了 Zhao et al. (2024) 单语工作到跨语言的空白\n- **S2**: Confound exclusion pipeline 设计周全（COMET tercile + token overlap + XNLI baseline + EN-DE 对照），为跨语言 probing 树立方法论范式\n- **S3**: XNLI baseline 对比实验设计巧妙——用同一 pipeline 证明不对称性非冲突特异性\n- **S4**: 对 negative results 的诚实处理（Qwen/Gemma steering 零翻转），避免 publication bias\n- **S5**: 独立复现（N=201, Appendix B）展示 L13 周围因果梯度的空间精度，增强结果可信度\n- **S6**: 写作清晰，Discussion 中对结果的解读审慎（\"architecture-specific\" 限定）\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n- **W-C1** [共识] **Detection ≠ Decision 因果声明泛化性严重不足（N=1 模型）**\n  - Steering 仅 Llama L13 成功，Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 88.9% probe acc, 0 flips) 全部失败\n  - Gemma 高 probe accuracy 下零效应构成对 \"probe direction = causal direction\" 的强力反证\n  - Abstract/Introduction 的 framing 暗示 general principle（\"A dissociation emerges between detection and decision\" 未加模型限定）\n  - 无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然\n\n- **W-C2** [共识] **Steering 实验多重比较校正不完整**\n  - 主实验在 3 层 × 10 α = 30 次检验，Bonferroni 仅层内应用（0.05/10=0.005）\n  - 若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著\n  - 独立复现 p<0.001 和负方向 p<0.001 部分缓解，但缺乏明确的 family definition 说明\n\n- **W-C3** [共识] **Qwen3-8B 引用错误**\n  - 论文使用 Qwen3-8B（36 layers）但引用 Qwen2.5 Technical Report (arXiv:2412.15115)\n  - 正确引用应为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)\n\n### Major（影响评分）\n\n- **W-M1** [共识] 单种子实验：所有 probing 结果基于单次 split，未报告多种子 mean±std\n- **W-M2** [共识] \"非冲突特异\"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验\n- **W-M3** [共识] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），Gemma 未报告\n- **W-M4** [共识] 标题和 Abstract 使用 \"Cross-Lingual\" 暗示一般性，实验仅覆盖 EN-ZH\n- **W-M5** [共识] Related Work 遗漏关键引用：Meng et al. (2022), Geiger et al. (2024), Turner et al. (2023), Marks et al. (2024)\n- **W-M6** [共识] Bib 条目多处使用非标准 \"and others\" 格式\n- **W-M7** [共识] 跨模型比较在不同样本子集上进行，未报告重叠度\n\n### Minor\n\n- **W-m1** [共识] 翻译模型 (Qwen3-8B) 与实验对象重叠，未讨论 confound\n- **W-m2** [共识] Table 3 caption \"p<0.05\" 与正文 Bonferroni 阈值 0.005 不一致\n- **W-m3** [R2] Qwen Δ_asym CI 包含零 [-0.6, 13.7]，\"consistent across all three architectures\" 表述过强\n- **W-m4** [R2] Cross-task probe transfer 重要实验结果放在 Discussion 而非 Experiments，结构不佳\n- **W-m5** [R2] \"A suggestive MLP trend\" 段 CI 含零，\"suggestive\" 表述有 cherry-picking 风险\n\n---\n\n## Reviewer Consensus\n\n以下问题双方一致（标注 [AGREE]）：\n1. Detection ≠ Decision 的 N=1 模型局限是论文最核心缺陷\n2. Bonferroni 校正 family definition 需明确，虽独立复现部分缓解\n3. Qwen3 引用必须更正\n4. 单种子实验不足，至少需讨论其影响\n5. CI 重叠 ≠ 等价性检验\n6. Confound exclusion pipeline 是论文最大方法论贡献\n7. 论文对 negative results 的诚实处理值得赞赏\n\n---\n\n## Reviewer Divergence\n\n| 议题 | R1 立场 | R2 立场 | 影响 |\n|------|---------|---------|------|\n| 新颖性评估 | C1+C3 组合有独立方法论贡献，sufficient for borderline conference (3.5) | 整体增量（Zhao 2024 延伸 + N=1 case study + toolkit），仅 Findings (3.0) | 评分差 0.5 |\n| Pires 2019 / Chi 2020 | 非必要引用，论文已引更直接后续工作 | 作为跨语言 probing 奠基工作应引用 | Minor |\n| Abstract 200 words | 完全合规（≤200 是硬限制） | 建议精简至 190 以下留安全余量 | Negligible |\n\n---\n\n## Questions（需作者澄清）\n\n1. Bonferroni 为什么按层而非按整个 steering 实验校正？是否有先验假设？\n2. 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？若是 post-hoc 应明确声明\n3. Gemma L21 cross-task transfer dip (0.730) 与 alternating attention 架构的关系？\n4. L13 和 L28 的 w_probe cosine similarity 是多少？\n5. Qwen Δ_asym CI 包含零，如何支撑 \"consistent across all three architectures\"？\n6. 翻译模型与实验对象重叠对 Qwen 结果的潜在影响？\n\n---\n\n## Missing References\n\n**双方共识必须补充：**\n- Meng et al. (2022) \"Locating and Editing Factual Associations in GPT\" — activation patching 奠基\n- Geiger et al. (2024) \"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations\" — DAS 替代因果方法\n- Turner, Thacker, and Fry (2023) \"Activation Addition\" — steering 核心方法论\n- Marks & Tegmark (2024) \"The Geometry of Truth\" — 线性 probe 因果效应正面案例\n- Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388) — 正确模型引用\n\n**R2 建议（R1 部分反对）：**\n- Pires et al. (2019) \"How Multilingual is Multilingual BERT?\" — 跨语言 probing 奠基\n- Chi et al. (2020) \"Finding Universal Grammatical Relations in Multilingual BERT\" — 跨语言共享子空间\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未启用外部审稿配置）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warning, 10 info）。主要发现：\n\n**Warnings:**\n1. 前 3 页纯文本无 display item，审稿人到第 4 页才看到第一个视觉锚点（Figure 1）。建议第 1-2 页添加 pipeline overview 图\n2. 第 7-8 页（Discussion+Conclusion+Limitations）连续纯文本无 display item 穿插\n3. Figure 1 为单栏内含 3 列子图，轴标签字号小于正文 70%，打印可读性差。建议改为 figure*（双栏全宽）\n\n**Info:**\n- 主文 8 页仅 5 个 display items（0.625/页），对实证论文偏少\n- Figure 1 caption 未说明 y 轴基线水平（chance=50%）\n- Figure 2 仅 6 个数据点，信息密度较低\n- 无 margin 溢出、LaTeX 渲染错误或排版缺陷\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n\n**置信度: 4/5**\n\n**理由:**\n\n本文方法论设计扎实，confound exclusion pipeline 有示范价值，统计实践整体规范，对 negative results 的诚实处理值得赞赏。然而：\n\n1. 最具新颖性的贡献（Detection ≠ Decision 层分离）仅在 Llama 一个模型上有因果证据，泛化性不足以支撑一般性结论\n2. 其余贡献（跨语言可检测性、不对称性刻画）相对于已有工作属增量扩展，不对称性本身可从 English-centric bias 文献预测\n3. 多重比较校正方案需更严格说明\n4. 单种子实验、CI 重叠代替等价检验等方法论问题削弱结论强度\n\n论文适合 **Findings track**：方法论贡献有参考价值，实证结果可靠，但核心新颖性和结论的泛化性不足以进入主会议。若能补充非 Llama 模型的因果干预成功案例（如通过 activation patching 或 DAS），或显著加强统计分析（多种子、正式等价检验），可重新评估 Conference 级别。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"A dissociation emerges between detection and decision\" — 应加 \"in Llama\" 限定\n- \"the first evidence that knowledge conflict signals are linearly detectable across languages\" — 改为 \"the first cross-lingual evidence\"，Zhao et al. (2024) 已有单语证据\n\n### Section 2 (Related Work)\n- 第三段 (Representation steering) 缺失 Turner et al. (2023) Activation Addition 和 Marks et al. (2024) Geometry of Truth\n- 提到 activation patching 作为 future work 但未引用 Meng et al. (2022) 原始论文\n\n### Section 3 (Method)\n- §3.6: \"Bonferroni correction applied per model as an independent family\" — 需解释为何不按 [层×α] 全 family 校正\n- §3.6: Bonferroni threshold = 0.005（k=10）需与 Table 3 caption \"p<0.05\" 统一\n\n### Section 4 (Experiments)\n- §4.3: Qwen CI [-0.6, 13.7] 包含零，\"consistent across all three architectures\" 应改为 \"consistent in direction\"\n- §4.5: COMET tercile Fisher test 应报告效应量和功效分析\n- §4.6: Table 3 中 Qwen/Gemma 行缺具体 flip rates，信息密度不对称\n\n### Section 5 (Discussion)\n- Cross-task probe transfer 实验是重要结果，放在 Discussion 结构不佳，应在 Experiments 中报告\n- \"A suggestive MLP trend\" 段建议移至 Appendix\n\n### References\n- yang2024qwen25 → 替换为 Qwen3 Technical Report (2505.09388)\n- 多个条目 \"and others\" 格式需补全\n- 补充 Meng 2022, Geiger 2024, Turner 2023, Marks 2024",
  "project": "clkc_mech_interp",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review\n**审稿模式**: Fresh (Round 1)\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/完整性/写作）\n\n---\n\n## Summary\n\n本文研究多语言 LLM 中跨语言知识冲突信号的可检测性和因果相关性。通过 Llama-3.1-8B-Instruct、Qwen3-8B 和 Gemma-2-9B-IT 三个模型的残差流 probing，发现冲突信号可跨语言线性检测，ZH→EN 迁移优于 EN→ZH 约 7pp，且该不对称性与 XNLI 非冲突基线匹配（非冲突特异性）。Representation steering 在 Llama L13（41% depth）成功（Fisher p=0.002），但在 L28（probe peak, 88%）及 Qwen/Gemma 中均失败，揭示 Detection ≠ Decision 层分离。\n\n---\n\n## Strengths\n\n- **S1**: 首次多架构/多语言知识冲突信号的系统性 probing 研究，填补了 Zhao et al. (2024) 单语工作到跨语言的空白\n- **S2**: Confound exclusion pipeline 设计周全（COMET tercile + token overlap + XNLI baseline + EN-DE 对照），为跨语言 probing 树立方法论范式\n- **S3**: XNLI baseline 对比实验设计巧妙——用同一 pipeline 证明不对称性非冲突特异性\n- **S4**: 对 negative results 的诚实处理（Qwen/Gemma steering 零翻转），避免 publication bias\n- **S5**: 独立复现（N=201, Appendix B）展示 L13 周围因果梯度的空间精度，增强结果可信度\n- **S6**: 写作清晰，Discussion 中对结果的解读审慎（\"architecture-specific\" 限定）\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n- **W-C1** [共识] **Detection ≠ Decision 因果声明泛化性严重不足（N=1 模型）**\n  - Steering 仅 Llama L13 成功，Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 88.9% probe acc, 0 flips) 全部失败\n  - Gemma 高 probe accuracy 下零效应构成对 \"probe direction = causal direction\" 的强力反证\n  - Abstract/Introduction 的 framing 暗示 general principle（\"A dissociation emerges between detection and decision\" 未加模型限定）\n  - 无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然\n\n- **W-C2** [共识] **Steering 实验多重比较校正不完整**\n  - 主实验在 3 层 × 10 α = 30 次检验，Bonferroni 仅层内应用（0.05/10=0.005）\n  - 若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著\n  - 独立复现 p<0.001 和负方向 p<0.001 部分缓解，但缺乏明确的 family definition 说明\n\n- **W-C3** [共识] **Qwen3-8B 引用错误**\n  - 论文使用 Qwen3-8B（36 layers）但引用 Qwen2.5 Technical Report (arXiv:2412.15115)\n  - 正确引用应为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)\n\n### Major（影响评分）\n\n- **W-M1** [共识] 单种子实验：所有 probing 结果基于单次 split，未报告多种子 mean±std\n- **W-M2** [共识] \"非冲突特异\"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验\n- **W-M3** [共识] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），Gemma 未报告\n- **W-M4** [共识] 标题和 Abstract 使用 \"Cross-Lingual\" 暗示一般性，实验仅覆盖 EN-ZH\n- **W-M5** [共识] Related Work 遗漏关键引用：Meng et al. (2022), Geiger et al. (2024), Turner et al. (2023), Marks et al. (2024)\n- **W-M6** [共识] Bib 条目多处使用非标准 \"and others\" 格式\n- **W-M7** [共识] 跨模型比较在不同样本子集上进行，未报告重叠度\n\n### Minor\n\n- **W-m1** [共识] 翻译模型 (Qwen3-8B) 与实验对象重叠，未讨论 confound\n- **W-m2** [共识] Table 3 caption \"p<0.05\" 与正文 Bonferroni 阈值 0.005 不一致\n- **W-m3** [R2] Qwen Δ_asym CI 包含零 [-0.6, 13.7]，\"consistent across all three architectures\" 表述过强\n- **W-m4** [R2] Cross-task probe transfer 重要实验结果放在 Discussion 而非 Experiments，结构不佳\n- **W-m5** [R2] \"A suggestive MLP trend\" 段 CI 含零，\"suggestive\" 表述有 cherry-picking 风险\n\n---\n\n## Reviewer Consensus\n\n以下问题双方一致（标注 [AGREE]）：\n1. Detection ≠ Decision 的 N=1 模型局限是论文最核心缺陷\n2. Bonferroni 校正 family definition 需明确，虽独立复现部分缓解\n3. Qwen3 引用必须更正\n4. 单种子实验不足，至少需讨论其影响\n5. CI 重叠 ≠ 等价性检验\n6. Confound exclusion pipeline 是论文最大方法论贡献\n7. 论文对 negative results 的诚实处理值得赞赏\n\n---\n\n## Reviewer Divergence\n\n| 议题 | R1 立场 | R2 立场 | 影响 |\n|------|---------|---------|------|\n| 新颖性评估 | C1+C3 组合有独立方法论贡献，sufficient for borderline conference (3.5) | 整体增量（Zhao 2024 延伸 + N=1 case study + toolkit），仅 Findings (3.0) | 评分差 0.5 |\n| Pires 2019 / Chi 2020 | 非必要引用，论文已引更直接后续工作 | 作为跨语言 probing 奠基工作应引用 | Minor |\n| Abstract 200 words | 完全合规（≤200 是硬限制） | 建议精简至 190 以下留安全余量 | Negligible |\n\n---\n\n## Questions（需作者澄清）\n\n1. Bonferroni 为什么按层而非按整个 steering 实验校正？是否有先验假设？\n2. 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？若是 post-hoc 应明确声明\n3. Gemma L21 cross-task transfer dip (0.730) 与 alternating attention 架构的关系？\n4. L13 和 L28 的 w_probe cosine similarity 是多少？\n5. Qwen Δ_asym CI 包含零，如何支撑 \"consistent across all three architectures\"？\n6. 翻译模型与实验对象重叠对 Qwen 结果的潜在影响？\n\n---\n\n## Missing References\n\n**双方共识必须补充：**\n- Meng et al. (2022) \"Locating and Editing Factual Associations in GPT\" — activation patching 奠基\n- Geiger et al. (2024) \"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations\" — DAS 替代因果方法\n- Turner, Thacker, and Fry (2023) \"Activation Addition\" — steering 核心方法论\n- Marks & Tegmark (2024) \"The Geometry of Truth\" — 线性 probe 因果效应正面案例\n- Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388) — 正确模型引用\n\n**R2 建议（R1 部分反对）：**\n- Pires et al. (2019) \"How Multilingual is Multilingual BERT?\" — 跨语言 probing 奠基\n- Chi et al. (2020) \"Finding Universal Grammatical Relations in Multilingual BERT\" — 跨语言共享子空间\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未启用外部审稿配置）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warning, 10 info）。主要发现：\n\n**Warnings:**\n1. 前 3 页纯文本无 display item，审稿人到第 4 页才看到第一个视觉锚点（Figure 1）。建议第 1-2 页添加 pipeline overview 图\n2. 第 7-8 页（Discussion+Conclusion+Limitations）连续纯文本无 display item 穿插\n3. Figure 1 为单栏内含 3 列子图，轴标签字号小于正文 70%，打印可读性差。建议改为 figure*（双栏全宽）\n\n**Info:**\n- 主文 8 页仅 5 个 display items（0.625/页），对实证论文偏少\n- Figure 1 caption 未说明 y 轴基线水平（chance=50%）\n- Figure 2 仅 6 个数据点，信息密度较低\n- 无 margin 溢出、LaTeX 渲染错误或排版缺陷\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n\n**置信度: 4/5**\n\n**理由:**\n\n本文方法论设计扎实，confound exclusion pipeline 有示范价值，统计实践整体规范，对 negative results 的诚实处理值得赞赏。然而：\n\n1. 最具新颖性的贡献（Detection ≠ Decision 层分离）仅在 Llama 一个模型上有因果证据，泛化性不足以支撑一般性结论\n2. 其余贡献（跨语言可检测性、不对称性刻画）相对于已有工作属增量扩展，不对称性本身可从 English-centric bias 文献预测\n3. 多重比较校正方案需更严格说明\n4. 单种子实验、CI 重叠代替等价检验等方法论问题削弱结论强度\n\n论文适合 **Findings track**：方法论贡献有参考价值，实证结果可靠，但核心新颖性和结论的泛化性不足以进入主会议。若能补充非 Llama 模型的因果干预成功案例（如通过 activation patching 或 DAS），或显著加强统计分析（多种子、正式等价检验），可重新评估 Conference 级别。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"A dissociation emerges between detection and decision\" — 应加 \"in Llama\" 限定\n- \"the first evidence that knowledge conflict signals are linearly detectable across languages\" — 改为 \"the first cross-lingual evidence\"，Zhao et al. (2024) 已有单语证据\n\n### Section 2 (Related Work)\n- 第三段 (Representation steering) 缺失 Turner et al. (2023) Activation Addition 和 Marks et al. (2024) Geometry of Truth\n- 提到 activation patching 作为 future work 但未引用 Meng et al. (2022) 原始论文\n\n### Section 3 (Method)\n- §3.6: \"Bonferroni correction applied per model as an independent family\" — 需解释为何不按 [层×α] 全 family 校正\n- §3.6: Bonferroni threshold = 0.005（k=10）需与 Table 3 caption \"p<0.05\" 统一\n\n### Section 4 (Experiments)\n- §4.3: Qwen CI [-0.6, 13.7] 包含零，\"consistent across all three architectures\" 应改为 \"consistent in direction\"\n- §4.5: COMET tercile Fisher test 应报告效应量和功效分析\n- §4.6: Table 3 中 Qwen/Gemma 行缺具体 flip rates，信息密度不对称\n\n### Section 5 (Discussion)\n- Cross-task probe transfer 实验是重要结果，放在 Discussion 结构不佳，应在 Experiments 中报告\n- \"A suggestive MLP trend\" 段建议移至 Appendix\n\n### References\n- yang2024qwen25 → 替换为 Qwen3 Technical Report (2505.09388)\n- 多个条目 \"and others\" 格式需补全\n- 补充 Meng 2022, Geiger 2024, Turner 2023, Marks 2024",
    "project": "clkc_mech_interp",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-24T15:10:08.891783+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6951eb3869a0070e3ae607ab60c90dad:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4123
}
```

</details>

---


### Assistant

_source line 98 · 2026-05-24T15:10:16.827441+00:00_

审稿报告已投递。

**圆桌审稿完成摘要：**

- **Overall: 3.0 (Findings)**
- **3 个 Critical**: (1) Detection≠Decision 仅 Llama 成立（N=1 泛化性不足）；(2) Bonferroni 校正 family definition 不完整；(3) Qwen3 引用错误
- **7 个 Major**: 单种子、缺 TOST 等价检验、COMET 功效不足、标题 oversell、遗漏关键引用、Bib 格式、跨模型不同子集
- **核心判断**: 方法论扎实（confound exclusion pipeline 有范式价值），但最具新颖性的因果贡献受限于单模型，其余贡献相对增量。适合 Findings track，不足以进入主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 99 · 2026-05-24T15:10:19.431697+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：
- **Overall: 3.0 (Findings)**，核心问题是新颖性有限（incremental extension of Zhao et al. 2024）和因果声明仅基于 1/3 模型
- 对 R1 的 6 个 Must-Fix/Should-Fix 全部 **[AGREE]**，补充了 4 个 R1 未覆盖的问题：Qwen3 引用错误（Critical）、标题/abstract oversell、bib 格式、Related Work 遗漏（Pires 2019, Chi 2020, Meng 2022, Geiger 2024）
- R1 给 3.5（Borderline Conference），我给 3.0（Findings）——主要分歧在于我认为新颖性问题比 R1 评估的更严重

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 100 · 2026-05-24T15:10:30.115166+00:00_

审稿报告已投递完成。

**圆桌审稿总结：**
- **Overall Score: 3.0 (Findings)**
- R1: 3.5 (Borderline Conference) / R2: 3.0 (Findings)
- 3 个 Critical issues（N=1 因果泛化、Bonferroni 校正、Qwen3 引用错误）
- 7 个 Major issues（单种子、TOST 缺失、COMET 功效、标题 oversell、遗漏引用、bib 格式、样本不重叠）
- Issue Tracker 已同步 12 条 issue 至 `review_issues.yaml`
- 视觉审查完成（3 warnings），外部审稿未启用

报告已自动送达 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 9

## Round 9

72 recorded events


### User

_source line 101 · 2026-05-24T16:28:19.703199+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: clkc_mech_interp
- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-24T16:28:28.006239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-24T16:28:28.110155+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-24T16:28:37.560317+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-24T16:28:37.610994+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-24T16:28:47.100041+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-24T16:28:47.200935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-24T16:28:55.537270+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-24T16:28:56.490944+00:00_

{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (78 个)\n\n- **comet_qwen_v6**: DONE (killed) — \n- **gemma_en_act_102**: DONE (success) — \n- **xnli_baseline_110**: DONE (negative) — \n- **comet_llama_v5**: DONE (killed) — \n- **comet_qwen_v5**: DONE (killed) — \n- **mvp_probe_llama_v1**: DONE (success) — \n- **mvp_probe_v1**: DONE (success) — \n- **comet_llama_v4**: PREPARING (killed) — \n- **comet_llama_v3**: PREPARING (killed) — \n- **comet_llama_v2**: PREPARING (killed) — \n- **comet_llama**: PREPARING (killed) — \n- **comet_qwen_v4**: PREPARING (killed) — \n- **comet_qwen_v3**: PREPARING (killed) — \n- **comet_qwen_v2**: PREPARING (killed) — \n- **comet_qwen**: PREPARING (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- gemma-steering-pickup（准备中）\n- llama31_en_activations（准备中）\n- qwen3_translate_zh（准备中）\n- collect_en_activations_qwen3_8b（准备中）\n- collect_en_activations_llama_v2（准备中）\n- translate_zh_llama_v2（准备中）\n- translate_zh_qwen（准备中）\n- collect_en_act_llama_v3（准备中）\n- collect_en_act_qwen_v2（准备中）\n- verify_qwen3_v2（准备中）\n- …另有 16 项\n\n## 近期结论\n- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L13_133** (negative): Qwen3-8B-Instruct L13 (36% depth) probe direction causally influences conflict resolution with matched-condition data (N≈200, high probe acc). L13 = L14 peak - 1, establishi
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-24T16:28:56.993246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-24T16:28:57.495714+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	\input{experiments}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\input{limitations}
42	
43	\appendix
44	
45	\section{Use of AI Assistants}
46	\label{app:ai-assistants}
47	
48	We used Claude (Anthropic) as an AI coding and writing assistant
49	throughout this work. Specifically:
50	\begin{itemize}
51	    \item \textbf{Code:} drafting experiment scripts, data-processing
52	    pipelines, and analysis utilities; debugging and refactoring.
53	    \item \textbf{Writing:} drafting and revising paper sections,
54	    polishing prose, and reformatting \LaTeX{}.
55	    \item \textbf{Literature:} summarizing related papers to inform
56	    related-work section.
57	\end{itemize}
58	
59	\section{Fine-Grained Causal Boundary Analysis}
60	\label{app:boundary}
61	
62	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
63	
64	\begin{table}[h]
65	\centering
66	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
67	\label{tab:boundary}
68	\small
69	\resizebox{\columnwidth}{!}{%
70	\begin{t
…[truncated 578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-24T16:28:57.496272+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
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

_source line 113 · 2026-05-24T16:28:57.596980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-24T16:29:04.523024+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-24T16:29:06.129643+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-24T16:29:06.782739+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-24T16:29:10.547562+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the key information about EMNLP 2026 call for papers and ARR submission:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.
…[truncated 964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 6024
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-24T16:29:10.598271+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'clkc_mech_interp'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4468
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-24T16:29:10.598643+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/acl_latex.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-24T16:29:22.091674+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit formatting template double blind site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit formatting template double blind site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-24T16:29:22.594241+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission guidelines anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission guidelines anonymity policy"
  }
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-24T16:29:22.695052+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-24T16:29:27.816149+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit formatting template double blind site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

Based on the search results from the EMNLP 2026 website, I found information about author guidelines including double-blind review requirements. Here's what I found:

## Double-Blind Review

The reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers and reviews on ARR.

## Industry Track Page Limits and Formatting

For the Industry Track papers, authors are invited to submit original, full-length papers with a maximum of 6 pages. Industry Track submissions must neither include the authors' names nor their affiliations to maintain anonymity.

Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations", which should be included at the end of the paper before the references and will not count toward the page
…[truncated 742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 5724
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-24T16:29:28.923083+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission guidelines anonymity policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/authors.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/authors.md"}]

Based on the search results, here's information about ACL Rolling Review 2026 May submission guidelines and the anonymity policy:

## Anonymity Requirements

Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided.

## Anonymity Period Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity perio
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 6328
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-24T16:29:29.126136+00:00_

{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (78 个)\n\n- **comet_qwen_v6**: DONE (killed) — \n- **gemma_en_act_102**: DONE (success) — \n- **xnli_baseline_110**: DONE (negative) — \n- **comet_llama_v5**: DONE (killed) — \n- **comet_qwen_v5**: DONE (killed) — \n- **mvp_probe_llama_v1**: DONE (success) — \n- **mvp_probe_v1**: DONE (success) — \n- **comet_llama_v4**: PREPARING (killed) — \n- **comet_llama_v3**: PREPARING (killed) — \n- **comet_llama_v2**: PREPARING (killed) — \n- **comet_llama**: PREPARING (killed) — \n- **comet_qwen_v4**: PREPARING (killed) — \n- **comet_qwen_v3**: PREPARING (killed) — \n- **comet_qwen_v2**: PREPARING (killed) — \n- **comet_qwen**: PREPARING (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- gemma-steering-pickup（准备中）\n- llama31_en_activations（准备中）\n- qwen3_translate_zh（准备中）\n- collect_en_activations_qwen3_8b（准备中）\n- collect_en_activations_llama_v2（准备中）\n- translate_zh_llama_v2（准备中）\n- translate_zh_qwen（准备中）\n- collect_en_act_llama_v3（准备中）\n- collect_en_act_qwen_v2（准备中）\n- verify_qwen3_v2（准备中）\n- …另有 16 项\n\n## 近期结论\n- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L13_133** (negative): Qwen3-8B-Instruct L13 (36% depth) probe direction causally influences conflict resolution with matched-condition data (N≈200, high probe acc). L13 = L14 peak - 1, establishi
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 6431
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-24T16:29:39.125994+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-24T16:29:39.176623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-24T16:29:43.695113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-24T16:29:44.096922+00:00_

1	When multilingual large language models (LLMs) encounter conflicting information across languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English--Chinese conflicts. Our analysis combines cross-lingual transfer, XNLI non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry is consistent with the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals, inheriting from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with implications for probe-based intervention research.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-24T16:29:44.197868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-24T16:29:44.650089+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{brink2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe ac
…[truncated 3750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-24T16:29:44.801185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-24T16:29:45.103010+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, \citet{brink2026probing} localized factual associations via probing, \citet{pham2026where} traced intra-memory conflict pathways, and \citet{li2025taming} proposed conflict mitigation methods.
7	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
8	
9	\paragraph{Cross-lingual representations in multilingual models.}
10	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
11	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
12	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
13	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR benchmark), and \citet{ifergan2024beneath, xing2024evaluating}; our work provides a mechanistic account of why such asymmetries arise.
14	
15	\paragraph{Representation steering and causal intervention.}
16	\citet{li2023iti} introduced Inference-Time Intervention for
…[truncated 1185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-24T16:29:45.103393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-24T16:29:45.956992+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our pipeline proceeds from data construction through probing and steering, formalized below.
5	
6	\subsection{Task Formulation}
7	\label{sec:task}
8	
9	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
10	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
11	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
12	
13	\subsection{Data Construction}
14	\label{sec:data}
15	
16	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
17	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2025qwen3}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
18	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET \citep{rei2020comet} back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
19	
20	\subsection{Activation Extraction and Probing}
21	\label{sec:extraction}
22	
23	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
24	We record the model's answer and assign binary labels (contextual vs.\ parametric).
25	
26	\label{sec:prob
…[truncated 2948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-24T16:29:46.108119+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/agent/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/agent/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-24T16:29:46.309839+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-24T16:29:52.433294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-24T16:29:52.835489+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for all
…[truncated 14341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-24T16:29:52.835883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-24T16:29:53.356559+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Detection and decision occur at different layers.}
5	Our central mechanistic finding is a dissociation between where conflict signals become linearly readable and where they exert causal influence on model behavior.
6	In Llama, probe accuracy on EN$\to$EN peaks at layer~28 (88\% depth), yet representation steering succeeds only at layer~13 (41\% depth; Fisher $p = 0.002$), and all late-layer interventions produce no significant behavioral change ($p > 0.3$).
7	This dissociation has a cross-lingual counterpart: the Llama ZH$\to$ZH probe peaks at L13, the same layer where steering succeeds.
8	Mid-layers thus serve a dual role as the site of cross-lingual alignment \citep{muller2021first, wendler2024llamas} and the locus where conflict signals acquire causal force.
9	The EN$\to$EN peak at L28 is best understood as a diagnostic readout, a linearly readable trace of a decision that has already been made upstream.
10	A practical implication follows: the probe peak layer is not the causal layer, and intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site.
11	Cross-layer sweeps, as conducted here, are necessary to locate the true decision point.
12	Steering failed in both Qwen (L14, 39\%; $n = 131$, best $p = 0.785$) and Gemma (L17, 40\%; $n = 171$, best $p = 0.448$), with zero directional flips in both cases.
13	The Gemma result is particularly informative: its 88.9\% probe accuracy---the highest among all three models---rules out probe quality as a confound, since the direction that best separates conflict labels carries no causal influence despite being highly discriminative.
14	This establishes that the causal influence of the probe direction is architecture-dependent, not a general property of mid-layer computation.
15	
16	\paragraph{Conflict signals are encoded in a general cross-lingual space.}
17	The ZH$\to$EN transfer advantage is consistent a
…[truncated 4458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 520
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-24T16:29:53.357059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-24T16:29:53.808979+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	This work investigated whether knowledge conflict signals in multilingual LLMs are detectable across languages and whether detected signals causally influence conflict resolution.
5	Through residual stream probing on Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, we showed that conflict signals are linearly detectable both within and across languages, with balanced accuracies of 77.6\%, 75.0\%, and 76.2\% on English within-language detection and all cross-lingual transfer directions significantly exceeding chance (binomial $p < 0.001$).
6	The observed transfer asymmetry (ZH$\to$EN exceeding EN$\to$ZH by approximately 6--7~pp) is consistent across all three architectures and is consistent with the XNLI non-conflict baseline in magnitude and direction for all models, establishing that this pattern reflects the general cross-lingual representational structure of English-dominant models rather than conflict-specific encoding.
7	
8	A central finding is the dissociation between detection and decision.
9	Probe accuracy peaks at late layers (L28, 88\% depth), but representation steering succeeds only at a mid-layer (L13, 41\% depth; Fisher $p = 0.002$), and all late-layer interventions fail.
10	This result demonstrates that linear detectability does not imply causal influence, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.
11	For probing-based intervention research, this dissociation implies that cross-layer sweeps are necessary to identify the computationally relevant site, as targeting the probe peak alone can miss the true decision point.
12	
13	Several directions remain open.
14	Steering failed in both Qwen (L14; $n = 131$, best $p = 0.785$) and Gemma (L17; $n = 171$, 88.9\% probe accuracy, best $p = 0.448$), with zero directional flips despite Gemma's probe accuracy exceeding Llama's, confirming that the causal influence of the probe direction is architecture-specifi
…[truncated 165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-24T16:29:53.809515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-24T16:29:54.763024+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese).
6	While the consistent patterns across three architecturally distinct models are encouraging, typologically diverse language pairs (e.g., English-German, English-Japanese) are needed to assess the generality of our findings.
7	Second, causal steering succeeded only in Llama at L13.
8	Gemma L17 steering failed despite the highest probe accuracy among all three models (88.9\%, $n = 171$), ruling out probe quality as a confound and constituting an informative negative that confirms the architecture-specificity of the effect.
9	Qwen L14 ($n = 131$, probe accuracy 71.0\%) was also negative with zero directional flips.
10	Third, the effective dataset size (966 to 1,590 samples per model after parametric knowledge verification) is constrained by the requirement that each model must correctly answer the question without context.
11	This verification step is necessary to ensure genuine knowledge conflicts, but it limits the statistical power of our analyses, particularly for stratified comparisons such as the COMET tercile ablation.
12	Fourth, all probing results are based on a single train/test split; while bootstrap confidence intervals capture sampling variability within this split, future work should verify stability across multiple random seeds.
13	Fifth, Qwen3-8B serves as both the translation model and an experimental subject; while the COMET-based quality control and the Llama/Gemma cross-validation mitigate this concern, a fully independent translation model would strengthen the Qwen-specific results.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-24T16:29:55.015182+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-24T16:29:55.367826+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-24T16:30:00.998158+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42 -maxdepth 3 -name \"*.yaml\" -path \"*/clkc_mech_interp/*\" 2>/dev/null | head -20",
  "description": "Find config files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-prod42 -maxdepth 3 -name \"*.yaml\" -path \"*/clkc_mech_interp/*\" 2>/dev/null | head -20",
    "description": "Find config files in project directory"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-24T16:30:01.401314+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/dream_registry.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/writing_plan.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/registry.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/mistakes.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/decisions.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-24T16:30:01.453076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "offset": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "offset": "80"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-24T16:30:01.556082+00:00_

80	\bottomrule
81	\end{tabular}%
82	}
83	\end{table}
84	
85	\section{Matched-Condition Steering Results}
86	\label{app:steering_config}
87	
88	Table~\ref{tab:steering_config} reports steering results under matched conditions: all three architectures are tested at comparable relative depths (${\sim}$36--43\%) using the same probe training methodology and six $\alpha$ values in $[-20, +20]$.
89	Despite the highest probe accuracy among the three models (88--89\%), Gemma produces zero directional flips, ruling out probe quality as a confound for the Llama-specific positive result.
90	The full Llama causal gradient ($N = 201$) is in Appendix~\ref{app:boundary}.
91	
92	\begin{table}[h]
93	\centering
94	\caption{Matched-condition steering results. Probe: EN$\to$EN balanced accuracy at the target layer. Best $p$: minimum Fisher exact $p$-value across six tested $\alpha$ values. Bonf.: $\alpha$ values surviving Bonferroni correction out of 6. Flips: total directional transitions (p$\to$c $+$ c$\to$p).$^{\dagger}$}
95	\label{tab:steering_config}
96	\small
97	\begin{tabular}{lcrccc}
98	\toprule
99	Layer & Depth & Probe (\%) & Best $p$ & Bonf. & Flips \\
100	\midrule
101	\multicolumn{6}{l}{\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\
102	\textbf{L13} & \textbf{41\%} & \textbf{76.1} & $\mathbf{<0.001}$ & \textbf{2/6} & \textbf{9} \\
103	\midrule
104	\multicolumn{6}{l}{\textit{Qwen3-8B ($N = 131$; 36 layers)}} \\
105	L13 & 36\% & 71.8 & 0.168 & 0/6 & 0 \\
106	L14 & 39\% & 71.0 & 0.785 & 0/6 & 0 \\
107	L15 & 42\% & 72.9 & 0.617 & 0/6 & 0 \\
108	\midrule
109	\multicolumn{6}{l}{\textit{Gemma-2-9B-IT ($N = 171$; 42 layers)$^{\dagger}$}} \\
110	L16 & 38\% & 88.0 & 0.067 & 0/6 & 0 \\
111	L17 & 40\% & 88.9 & 0.448 & 0/6 & 0 \\
112	L18 & 43\% & 89.5 & 0.219 & 0/6 & 0 \\
113	\bottomrule
114	\end{tabular}
115	\begin{flushleft}
116	\footnotesize $^{\dagger}$ Gemma v2: re-run after correcting a label assignment bug in v1 data preparation.
117	\end{flushleft}
118	\end{table}
119	
…[truncated 59 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-24T16:30:08.939152+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ 2>/dev/null | head -10",
  "description": "Check if external review is configured"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ 2>/dev/null | head -10",
    "description": "Check if external review is configured"
  }
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-24T16:30:09.896262+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-24T16:30:11.105267+00:00_

issues:
- id: "R1-N1"
  summary: "Steering 实验 Bonferroni 校正仅层内应用，未跨层校正（30次比较），L13 正方向 p=0.002 在完整校正下不显著"
  category: experiment
  severity: critical
  status: open
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "R1 提出，R2 AGREE。独立复现(N=201) p<0.001 和负方向 p<0.001 部分缓解，但需明确报告 family-wise p 值"
  action_items:
    - round: 1
      action: "明确说明层间不校正的理由或采用 FDR/Holm-Bonferroni 校正，报告完整 family-wise p 值"
      assigned_to: author
      status: pending
  resolution: ""
  resolution_round: null

- id: "R1-N2"
  summary: "Detection ≠ Decision 因果声明仅在 Llama 一个模型成立（N=1），Qwen/Gemma 零翻转，泛化性严重不足"
  category: method
  severity: critical
  status: open
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "双方一致认为这是论文最核心局限。R2 建议尝试 DAS/activation patching 或降低 claim 强度。R1 指出 Gemma 88.9% probe acc 下零效应构成反证"
  action_items:
    - round: 1
      action: "Abstract/Intro 中 Detection≠Decision 表述加 'in Llama' 限定；讨论 steering 失败是否反映非线性因果结构"
      assigned_to: author
      status: pending
  resolution: ""
  resolution_round: null

- id: "R2-N2"
  summary: "Qwen3-8B 引用错误：引用了 Qwen2.5 Technical Report (arXiv:2412.15115) 而非 Qwen3 (arXiv:2505.09388)"
  category: format
  severity: critical
  status: open
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [2, 1]
      note: "事实性引用错误，R1 AGREE 必须更正"
  action_items:
    - round: 1
      action: "替换 references.bib 中 yang2024qwen25 为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)"
      assigned_to: author
      status: pending
  resolution: ""
  resolution_round: null

- id: "R1-W1"
  summary: "单种子实验：所有 probing 结果基于单次 train/test split，未报告多种子 mean±std"
  category: experiment
  severity: warning
  status: open
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "双方一致。Peak layer 位置和准确率可能因 split 不同而变化"
  action_items:
    - round: 1
      action: 
…[truncated 3809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-24T16:30:11.261942+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/workers/worker_infra_mvp_llama_phase_a_20260521T133704.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01JXNDTgqfthmRsw6qjWF5Zj","type":"tool_result","content":"Found 133 files\n/home/ubuntu/agent-ml-research/core/mcp_server.py\n/home/ubuntu/agent-ml-research/core/tools/paper_audit.py\n/home/ubuntu/agent-ml-research/core/agents/message_router.py\n/home/ubuntu/agent-ml-research/core/approvals/hooks.py\n/home/ubuntu/agent-ml-research/core/agents/command_help.py\n/home/ubuntu/agent-ml-research/core/writing/figure_check.py\n/home/ubuntu/agent-ml-research/core/writing/overleaf_sync.py\n/home/ubuntu/agent-ml-research/core/writing/table_generator.py\n/home/ubuntu/agent-ml-research/core/writing/template_manager.py\n/home/ubuntu/agent-ml-research/core/writing/types.py\n/home/ubuntu/agent-ml-research/core/tools/worker.py\n/home/ubuntu/agent-ml-research/core/tools/roadmap.py\n/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py\n/home/ubuntu/agent-ml-research/core/tools/ssh.py\n/home/ubuntu/agent-ml-research/core/tools/paper_checklist.py\n/home/ubuntu/agent-ml-research/core/tools/paper_consistency.py\n/home/ubuntu/agent-ml-research/core/tools/project_config.py\n/home/ubuntu/agent-ml-research/core/tools/project_setup.py\n/home/ubuntu/agent-ml-research/core/tools/registry.py\n/home/ubuntu/agent-ml-research/core/tools/report_facts.py\n/home/ubuntu/agent-ml-research/core/tools/feishu_group.py\n/home/ubuntu/agent-ml-research/core/tools/gpu_monitor.py\n/home/ubuntu/agent-ml-research/core/tools/literature.py\n/home/ubuntu/agent-ml-research/core/tools/paper_audit_card.py\n/home/ubuntu/agent-ml-research/core/tools/experiment_matrix.py\n/home/ubuntu/agent-ml-research/core/tools/experiment_plan.py\n/home/ubuntu/agent-ml-research/core/tools/feishu.py\n/home/ubuntu/agent-ml-research/core/tools/distill_card.py\n/home/ubuntu/agent-ml-research/core/tools/dream_runner.py\n/home/ubuntu/ag
…[truncated 16384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 2322
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-24T16:30:11.317544+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check existing review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-24T16:30:11.619210+00:00_

round_1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-24T16:30:11.669956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-24T16:30:11.721223+00:00_

1	% References for Cross-Lingual Knowledge Conflict paper
2	
3	@article{basu2026interpretability,
4	  author    = {Basu, Sanjay and Patel, Sadiq Y. and Sheth, Parth and Muralidharan, Bhairavi and Elamaran, Namrata and Kinra, Aakriti and Morgan, John and Batniji, Rajaie},
5	  title     = {Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations},
6	  journal   = {arXiv preprint arXiv:2603.18353},
7	  year      = {2026},
8	  url       = {https://arxiv.org/abs/2603.18353}
9	}
10	
11	@article{brink2026probing,
12	  author    = {Brink, I. and Boer, A. and Ulmer, D.},
13	  title     = {Probing for Knowledge Attribution in Large Language Models},
14	  journal   = {arXiv preprint arXiv:2602.22787},
15	  year      = {2026},
16	  url       = {https://arxiv.org/abs/2602.22787}
17	}
18	
19	@inproceedings{ifergan2024beneath,
20	  author    = {Ifergan, Matan and Choshen, Leshem and Aharoni, Roee and Szpektor, Idan and Abend, Omri},
21	  title     = {Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in {LLMs}},
22	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
23	  year      = {2024},
24	  url       = {https://arxiv.org/abs/2408.10646}
25	}
26	
27	
28	@inproceedings{li2025taming,
29	  author    = {Li, Gaotang and Chen, Yufei and Tong, Hanghang},
30	  title     = {Taming Knowledge Conflicts in Language Models},
31	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
32	  year      = {2025},
33	  url       = {https://arxiv.org/abs/2503.10996}
34	}
35	
36	@article{pham2026where,
37	  author    = {Pham, Minh Vu and Borkakoty, Hrishav and Hou, Yufang},
38	  title     = {Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models},
39	  journal   = {arXiv preprint arXiv:2601.09445},
40	  year      = {2026},
41	  url       = {https://arxiv.org
…[truncated 8539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-24T16:30:50.008158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
  "offset": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
    "offset": "200"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-24T16:30:51.113051+00:00_

200	
201	@article{grattafiori2024llama,
202	  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aieleen and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela and Goyal, Anirudh and Hartshorn, Anthony and Yang, Aobo and Mber, Ariel and Bai, Chao and others},
203	  title     = {The {Llama} 3 Herd of Models},
204	  journal   = {arXiv preprint arXiv:2407.21783},
205	  year      = {2024},
206	  url       = {https://arxiv.org/abs/2407.21783}
207	}
208	
209	@article{yang2025qwen3,
210	  author    = {Yang, An and Li, Anfeng and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Gao, Chang and Huang, Chengen and Lv, Chenxu and others},
211	  title     = {Qwen3 Technical Report},
212	  journal   = {arXiv preprint arXiv:2505.09388},
213	  year      = {2025},
214	  url       = {https://arxiv.org/abs/2505.09388}
215	}
216	
217	@article{team2024gemma,
218	  author    = {{Gemma Team} and Rivi{\`e}re, Morgane and Pathak, Shreya and Sessa, Pier Giuseppe and Hardin, Cassidy and Bhupatiraju, Surya and Hussenot, L{\'e}onard and Mesnard, Thomas and Shahriari, Bobak and Ram{\'e}, Alexandre and others},
219	  title     = {Gemma 2: Improving Open Language Models at a Practical Size},
220	  journal   = {arXiv preprint arXiv:2408.00118},
221	  year      = {2024},
222	  url       = {https://arxiv.org/abs/2408.00118}
223	}
224	
225	% New entries for W-M5 and W-C2
226	
227	@inproceedings{meng2022locating,
228	  author    = {Meng, Kevin and Bau, David and Andonian, Alex and Belinkov, Yonatan},
229	  title     = {Locating and Editing Factual Associations in {GPT}},
230	  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},
231	  year      = {2022},
232	  url       = {https://arxiv.org/abs/2202.05262}
233	}
234	
235	@article{turner2023activation,
236	  author    = {Turner, Alexander Matt and Thiergart, Lisa and Udell, David and Leech, 
…[truncated 1237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-24T16:30:51.163690+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf 2>/dev/null || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf 2>/dev/null || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-24T16:30:51.366168+00:00_

-rw-r--r-- 1 ubuntu ubuntu 326808 May 24 15:34 /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-24T16:32:02.817615+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "clkc_mech_interp",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页，参考文献不限，Limitations 必选不计入页数\n- **匿名**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源文件: `projects/clkc_mech_interp/docs/paper/main.tex`（各 section 通过 `\\input{}` 引入）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n\n研究跨语言知识冲突信号在多语言 LLM 内部表征中的检测和因果影响。在 Llama-3.1-8B-Instruct、Qwen3-8B 和 Gemma-2-9B-IT 三个模型上进行 residual stream probing，发现：\n1. 冲突信号可跨语言线性检测\n2. ZH→EN 迁移优于 EN→ZH 约 7pp，与 XNLI 非冲突基线一致\n3. 在 Llama 中存在 detection-decision 层分离：probe 峰值在 L28 (88% depth)，但 steering 仅在 L13 (41% depth) 有因果效应\n4. Qwen 和 Gemma steering 无显著效果\n\n## 你的审查重点\n\n请重点审查以下方面：\n\n1. **Probing pipeline 设计**：logistic regression probe 的训练/测试分割是否合理？单种子设计的风险？Balanced accuracy 作为指标是否充分？\n2. **Steering 实验的因果推断**：Fisher exact test + Bonferroni 校正的应用是否正确？校正范围是否充分（层内 vs 跨层）？flip rate 作为因果效应的度量是否合适？\n3. **多重比较问题**：论文在多个层、多个 alpha 值上测试——family-wise error rate 控制是否充分？\n4. **Confound exclusion pipeline**：COMET tercile 分析和 token overlap 分析的统计功效是否足够？能否真正排除混淆变量？\n5. **XNLI baseline 比较**：CI 重叠作为 \"非冲突特异\" 的论据是否充分？是否需要 formal equivalence testing？论文中的 TOST 检验是否正确执行？\n6. **跨模型比较的有效性**：三个模型使用不同样本子集（Llama 1368, Qwen 966, Gemma 1590），这对比较的公平性有何影响？\n7. **因果声明的泛化性**：Detection ≠ Decision 仅在 Llama 一个模型成立，Qwen/Gemma 零翻转——标题和 abstract 的 claim 是否过度泛化？\n8. **独立复现**：Appendix 的 boundary-mapping replication (N=201) 是否真正独立？数据采样和实验条件是否充分描述？\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 排序：Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment（含评分和置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "clkc_mech_interp",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页，参考文献不限，Limitations 必选不计入页数\n- **匿名**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源文件: `projects/clkc_mech_interp/docs/paper/main.tex`（各 section 通过 `\\input{}` 引入）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n\n研究跨语言知识冲突信号在多语言 LLM 内部表征中的检测和因果影响。在 Llama-3.1-8B-Instruct、Qwen3-8B 和 Gemma-2-9B-IT 三个模型上进行 residual stream probing，发现：\n1. 冲突信号可跨语言线性检测\n2. ZH→EN 迁移优于 EN→ZH 约 7pp，与 XNLI 非冲突基线一致\n3. 在 Llama 中存在 detection-decision 层分离：probe 峰值在 L28 (88% depth)，但 steering 仅在 L13 (41% depth) 有因果效应\n4. Qwen 和 Gemma steering 无显著效果\n\n## 你的审查重点\n\n请重点审查以下方面：\n\n1. **Probing pipeline 设计**：logistic regression probe 的训练/测试分割是否合理？单种子设计的风险？Balanced accuracy 作为指标是否充分？\n2. **Steering 实验的因果推断**：Fisher exact test + Bonferroni 校正的应用是否正确？校正范围是否充分（层内 vs 跨层）？flip rate 作为因果效应的度量是否合适？\n3. **多重比较问题**：论文在多个层、多个 alpha 值上测试——family-wise error rate 控制是否充分？\n4. **Confound exclusion pipeline**：COMET tercile 分析和 token overlap 分析的统计功效是否足够？能否真正排除混淆变量？\n5. **XNLI baseline 比较**：CI 重叠作为 \"非冲突特异\" 的论据是否充分？是否需要 formal equivalence testing？论文中的 TOST 检验是否正确执行？\n6. **跨模型比较的有效性**：三个模型使用不同样本子集（Llama 1368, Qwen 966, Gemma 1590），这对比较的公平性有何影响？\n7. **因果声明的泛化性**：Detection ≠ Decision 仅在 Llama 一个模型成立，Qwen/Gemma 零翻转——标题和 abstract 的 claim 是否过度泛化？\n8. **独立复现**：Appendix 的 boundary-mapping replication (N=201) 是否真正独立？数据采样和实验条件是否充分描述？\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 排序：Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment（含评分和置信度）"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-24T16:32:19.790011+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16972
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-24T16:32:20.344416+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "clkc_mech_interp",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页，参考文献不限，Limitations 必选不计入页数\n- **匿名**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源文件: `projects/clkc_mech_interp/docs/paper/main.tex`（各 section 通过 `\\input{}` 引入）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n\n研究跨语言知识冲突信号在多语言 LLM 内部表征中的检测和因果影响。三个模型（Llama/Qwen/Gemma）的 probing + steering 实验。核心发现：\n1. 冲突信号跨语言可检测，迁移存在方向不对称\n2. 不对称性与 XNLI 基线一致，非冲突特异\n3. Llama 中 probe 峰值层 ≠ 因果层（detection-decision dissociation）\n4. Qwen/Gemma steering 失败\n\n## 你的审查重点\n\n请重点审查以下方面：\n\n1. **Novelty 评估**：相对于 Zhao et al. 2024（单语 probing）和 Basu et al. 2026（detectability ≠ actionability），本文的增量贡献有多大？跨语言扩展是否足够 novel？\n2. **Contribution 定位**：三个 contribution 是否都得到充分的实验支撑？哪些是强 claim 哪些是弱 observation？\n3. **Related Work 覆盖度**：是否遗漏重要相关工作？特别是：\n   - 跨语言 probing / representation alignment 领域\n   - Knowledge conflict detection 领域\n   - Representation steering / activation engineering 领域\n   - 是否有 2025-2026 的新工作被遗漏？\n4. **Claim-Evidence 匹配**：\n   - 标题 \"Cross-Lingual\" 但仅测试 EN-ZH 一个语言对——是否过度泛化？\n   - Abstract 中的 claim 强度是否与实验结果匹配？\n   - \"Inherit Directional Asymmetries\" 这个表述是否被充分证明？\n5. **写作质量**：\n   - 论文结构是否清晰？\n   - 叙事逻辑是否连贯？\n   - 是否存在冗余或不必要的重复？\n   - 技术细节是否充分？\n6. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - 引用格式是否符合 ACL 标准？\n   - Bib 条目是否完整（注意 \"and others\" vs 完整作者列表）？\n   - Limitations section 是否恰当？\n   - Figure/Table 质量和引用是否正确？\n7. **缺失实验或分析**：\n   - 是否有明显应该做但没做的实验？\n   - 消融实验是否充分？\n   - 是否有替代解释未被排除？\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 排序：Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "clkc_mech_interp",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页，参考文献不限，Limitations 必选不计入页数\n- **匿名**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源文件: `projects/clkc_mech_interp/docs/paper/main.tex`（各 section 通过 `\\input{}` 引入）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n\n研究跨语言知识冲突信号在多语言 LLM 内部表征中的检测和因果影响。三个模型（Llama/Qwen/Gemma）的 probing + steering 实验。核心发现：\n1. 冲突信号跨语言可检测，迁移存在方向不对称\n2. 不对称性与 XNLI 基线一致，非冲突特异\n3. Llama 中 probe 峰值层 ≠ 因果层（detection-decision dissociation）\n4. Qwen/Gemma steering 失败\n\n## 你的审查重点\n\n请重点审查以下方面：\n\n1. **Novelty 评估**：相对于 Zhao et al. 2024（单语 probing）和 Basu et al. 2026（detectability ≠ actionability），本文的增量贡献有多大？跨语言扩展是否足够 novel？\n2. **Contribution 定位**：三个 contribution 是否都得到充分的实验支撑？哪些是强 claim 哪些是弱 observation？\n3. **Related Work 覆盖度**：是否遗漏重要相关工作？特别是：\n   - 跨语言 probing / representation alignment 领域\n   - Knowledge conflict detection 领域\n   - Representation steering / activation engineering 领域\n   - 是否有 2025-2026 的新工作被遗漏？\n4. **Claim-Evidence 匹配**：\n   - 标题 \"Cross-Lingual\" 但仅测试 EN-ZH 一个语言对——是否过度泛化？\n   - Abstract 中的 claim 强度是否与实验结果匹配？\n   - \"Inherit Directional Asymmetries\" 这个表述是否被充分证明？\n5. **写作质量**：\n   - 论文结构是否清晰？\n   - 叙事逻辑是否连贯？\n   - 是否存在冗余或不必要的重复？\n   - 技术细节是否充分？\n6. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - 引用格式是否符合 ACL 标准？\n   - Bib 条目是否完整（注意 \"and others\" vs 完整作者列表）？\n   - Limitations section 是否恰当？\n   - Figure/Table 质量和引用是否正确？\n7. **缺失实验或分析**：\n   - 是否有明显应该做但没做的实验？\n   - 消融实验是否充分？\n   - 是否有替代解释未被排除？\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 排序：Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-24T16:32:22.113006+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1768
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-24T16:32:22.113418+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "clkc_mech_interp",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "clkc_mech_interp",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool call

_source line 169 · 2026-05-24T16:32:22.166061+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-24T16:32:23.959867+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1846
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-24T16:32:24.010552+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1844
}
```

</details>

---


### Assistant

_source line 172 · 2026-05-24T16:32:33.727775+00:00_

**✅ 审稿启动完成**

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 统计分析） | 🟢 已派发 |
| Reviewer 2（新颖性 + 完整性 + 写作质量） | 🟢 已派发 |
| 视觉审查 Agent | 🟢 已启动（fire-and-forget） |
| 外部审稿（Stanford Agentic Reviewer） | ⚪ 未配置，跳过 |

等待两位 Reviewer 返回初审报告，随后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 173 · 2026-05-24T16:38:48.208538+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性 + 实验设计 + 统计分析

### 总体评分

**Overall Assessment**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5
**一句话总结**: 方法管线设计优于多数 probing 研究（含 confound exclusion 和 XNLI baseline），但因果发现仅在 1/3 模型成立、单种子设计低于当前标准、TOST 等价检验欠功效，削弱了两个核心贡献的说服力。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 主体方法合理，但单种子单 split 设计、TOST 欠功效却仍做等价结论、confound 分析缺 Gemma 数据构成方法论空缺 |
| Excitement | 3 / 5 | Detection ≠ Decision 分离是有趣的 mechanistic 发现，XNLI baseline 设计巧妙，但因果部分仅 Llama 成立，asymmetry inheritance 本身偏 incremental |
| Reproducibility | 3 / 5 | 单种子单 split，未公开代码/数据，bootstrap n=2000 偏低，Appendix 细节较充分但缺完整超参表 |

---

### Must-Fix 问题（3 个）

**N1** [critical] 单种子单 split 设计——bootstrap CI 不能替代 multi-seed 验证

- 具体位置：Section 3.3, Section 4.1, Limitations
- 问题：所有 probing 结果基于一次 80/20 stratified split，bootstrap CI（n=2,000）仅捕获 split 内采样变异性，而非 split 间变异性。Logistic regression probe 对训练集组成敏感，不同 split 可能导致 peak layer 位置和 Δ_asym 估计值的实质变化。当前 probing 文献的标准实践是 ≥3 个随机种子取平均。
- 为什么影响接收：Table 1 中所有数字（包括 Δ_asym 的 7.3/7.2/6.6 pp）以及 Figure 1 的 layer-wise 曲线可能不稳定。论文的核心声明（跨模型一致的 ~7pp 不对称性）依赖数值相似性。
- 建议：至少运行 5 个不同 train/test split 种子，报告均值 ± 标准差。

**N2** [critical] TOST 等价检验不显著，但结论按等价处理

- 具体位置：Section 4.4, line 94-95
- 问题：TOST（±2pp margin）三个模型均不显著（p=0.434, 0.366, 0.377），论文正确指出 SE≈4.37pp 导致 power 不足，但仍总结 "The asymmetry thus reflects a general cross-lingual property"。非显著 TOST = "数据不足以区分等价与非等价"，而非"效应等价"。±2pp margin 的选择亦缺乏 justification。
- 为什么影响接收：Contribution 1（asymmetry inheritance）是论文标题核心声明。如等价性未被严格建立，标题的"inherit"缺乏统计支撑。
- 建议：调整表述为 "is consistent with" 而非 "reflects/inherits"；justify margin 选择；或增大样本量。

**N3** [critical] 因果声明仅 Llama 1/3 模型成立——泛化性不足

- 具体位置：Contribution 2, Section 4.6, Table 3, Conclusion
- 问题：Steering 在 Qwen（n=131, best p=0.785, 0 flips）和 Gemma（n=171, best p=0.448, 0 flips）完全失败。论文将 detection-decision dissociation 列为三大贡献之一，但仅在 1/3 模型成立。Qwen/Gemma 的零效应有两种解释：(a) 无 detection-decision 分离，(b) 线性 steering 不足以揭示非线性因果结构。论文选择 (a) 但未充分排除 (b)。
- 建议：在 Discussion 讨论线性 steering 局限性作为替代解释；考虑降低 Contribution 2 的地位。

---

### Should-Fix 问题（6 个）

**W1** Confound exclusion 缺 Gemma 数据（Table 2 仅报告 Qwen 和 Llama，Gemma 有最大数据集 1590 样本）

**W2** Confound tercile 分析统计功效不足（每组仅 ~60-90 样本，Fisher exact test 的 p=0.695/0.761 不能解读为"无混淆"）。建议补充功效分析或改用连续回归。

**W3** 三个模型使用 ConflictQA 不同子集（Llama 1368, Qwen 966, Gemma 1590），自选择偏差影响跨模型比较公平性。建议报告数据集重叠比例。

**W4** Boundary-mapping replication（N=201）的"独立性"被夸大——相同模型/任务/方法/pipeline 下的重新采样是 validation 而非 replication。建议修改措辞。

**W5** Steering 实验中定向翻转绝对数极少（4 p→c, 5 c→p），n_test=136。建议报告 Cohen's h 或 odds ratio 作为效应量。

**W6** Qwen3-8B 翻译者-受试者双重角色——微妙偏差无法被 COMET 捕获。建议在独立翻译模型上验证 Qwen 结果。

---

### 小问题（5 个）

- M1: Bootstrap n=2000 偏低，建议 n=10000
- M2: EN-DE 对比分析细节不足（哪个模型？完整统计？）
- M3: Table 1 脚注关于 Δ_asym 计算方式应提前说明
- M4: 建议补充 AUROC 以便与 Basu et al. (2026) 直接比较
- M5: Abstract ~198 词，合规但无余量

---

### 主要优势

- S1: 方法管线完整性突出（probing + steering + confound exclusion + XNLI baseline + boundary replication）
- S2: XNLI baseline 比较设计巧妙，有方法论贡献价值
- S3: Detection ≠ Decision 分离对 probing-based intervention 社区有直接实践启示
- S4: 写作清晰，claim 限定总体准确
- S5: Confound exclusion pipeline 为跨语言 probing 研究提供可复用模板

---

### Questions for Authors

1. 不同随机种子下 Llama L13 steering 显著性是否稳定？
2. Gemma 的 COMET tercile 和 token overlap 结果？为什么 Table 2 省略？
3. 三个模型 ConflictQA 子集重叠比例？
4. Qwen/Gemma 是否尝试过非线性干预方法？
5. TOST ±2pp margin 选择依据？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 174 · 2026-05-24T16:38:57.363200+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 11

## Round 11

10 recorded events


### User

_source line 175 · 2026-05-24T16:38:59.928124+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：给出 **3.5/5 Borderline Conference**。三个 Must-Fix 问题——(1) 单种子设计不满足当前 probing 标准，(2) TOST 等价检验无功效却做了等价结论，(3) 因果发现仅 1/3 模型成立但被列为主要贡献。六个 Should-Fix 包括 Gemma confound 数据缺失、tercile 分析功效不足、跨模型样本自选择偏差等。论文的方法管线设计（confound exclusion + XNLI baseline + boundary replication）和 Detection ≠ Decision 发现本身是优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-24T16:39:22.784450+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-24T16:39:22.784942+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-24T16:39:25.144066+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-24T16:39:25.397125+00:00_

{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (78 个)\n\n- **comet_qwen_v6**: DONE (killed) — \n- **gemma_en_act_102**: DONE (success) — \n- **xnli_baseline_110**: DONE (negative) — \n- **comet_llama_v5**: DONE (killed) — \n- **comet_qwen_v5**: DONE (killed) — \n- **mvp_probe_llama_v1**: DONE (success) — \n- **mvp_probe_v1**: DONE (success) — \n- **comet_llama_v4**: PREPARING (killed) — \n- **comet_llama_v3**: PREPARING (killed) — \n- **comet_llama_v2**: PREPARING (killed) — \n- **comet_llama**: PREPARING (killed) — \n- **comet_qwen_v4**: PREPARING (killed) — \n- **comet_qwen_v3**: PREPARING (killed) — \n- **comet_qwen_v2**: PREPARING (killed) — \n- **comet_qwen**: PREPARING (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- gemma-steering-pickup（准备中）\n- llama31_en_activations（准备中）\n- qwen3_translate_zh（准备中）\n- collect_en_activations_qwen3_8b（准备中）\n- collect_en_activations_llama_v2（准备中）\n- translate_zh_llama_v2（准备中）\n- translate_zh_qwen（准备中）\n- collect_en_act_llama_v3（准备中）\n- collect_en_act_qwen_v2（准备中）\n- verify_qwen3_v2（准备中）\n- …另有 16 项\n\n## 近期结论\n- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L13_133** (negative): Qwen3-8B-Instruct L13 (36% depth) probe direction causally influences conflict resolution with matched-condition data (N≈200, high probe acc). L13 = L14 peak - 1, establishi
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-24T16:39:38.071180+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-24T16:39:38.172034+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-24T16:39:38.222688+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-24T16:39:38.273459+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T16:32:23.443827+00:00\", \"completed_at\": \"2026-05-24T16:34:54.689301+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-4\", \"message\": \"连续 4 页纯文本无任何 display item，审稿人第一印象阶段（前 2 分钟）仅看到文字墙。第一个 figure 直到 page 5 才出现。建议将 Figure 1 或一个方法概览图/pipeline 图前置到 page 2-3\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 1 + Table 1 + Figure 2 三个 display items 挤在同一页，视觉密度过高，与前 4 页的空旷形成不均匀节奏。建议将 Table 1 或 Figure 2 分散到 page 4 或 page 6\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 的线条在 solid/dashed 区分度尚可，但部分模型（如 MLP subgroup）的颜色在小尺寸下偏近，建议增加 marker shape 差异或加粗关键线条以提高可辨性\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 尺寸较小（约 1/4 栏宽），灰色置信区间带清晰，但 bar 标签字号偏小，建议略微放大或确保 ≥8pt\"}, {\"severity\": \"info\", \"dimension\": \"pages 5-7\", \"message\": \"Tables 1-3 均使用 booktabs 风格，最优值加粗，格式规范专业\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 布局合理，p 值和 \\\"n.s.\\\" 标注清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 3 有脚注标注（†），footnote 在表格底部清晰可见\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Appendix Tables 4-5 格式与正文表格一致，booktabs 风格，整洁\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-11\", \"message\": \"参考文献页排版正常，无 [?] 未解析引用，无溢出，格式统一\"}, {\"severity\": \"info\", \"dimension\": \"general\", \"message\": \"无 margin 溢出、无公式渲染错误、无 section heading 孤悬页底、页眉页脚符合 ACL 匿名投稿模板\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 184 · 2026-05-24T16:39:49.412818+00:00_

**圆桌审稿进度更新**

| 环节 | 状态 |
|------|------|
| Reviewer 1 初审 | ✅ 已完成（3.5 Borderline Conference） |
| Reviewer 2 初审 | ⏳ 等待中 |
| 视觉审查 | ✅ 已完成（2 warning, 0 critical） |
| 外部审稿 | 未请求 |

Reviewer 1 主要发现：3 个 Must-Fix（单种子设计、TOST 等价检验无功效、因果发现仅 1/3 模型成立却列为主要贡献）+ 6 个 Should-Fix。

等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 12

## Round 12

6 recorded events


### User

_source line 185 · 2026-05-24T16:39:50.918273+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告

**论文**: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*
**Venue**: EMNLP 2026 Long Paper (ARR May cycle)
**审查侧重**: 新颖性 + 完整性 + 写作质量
**审稿依据**: ACL ARR Review Form (Soundness / Excitement / Reproducibility / Overall Assessment)

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 方法论扎实的跨语言 probing 实证研究，但标题和 abstract 对证据的过度泛化（单语言对声称 "Cross-Lingual"、相关性包装为因果 "Inherit"、单模型发现推广为通用结论）削弱了贡献的可信度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 实验设计合理（probing + XNLI baseline + confound exclusion + steering），但多处 claim 超出证据支撑范围：标题因果措辞 "Inherit" 缺乏因果证据；steering 仅在 1/3 模型成功却推广为通用发现 |
| Excitement | 2.5/5 | 对 Zhao et al. 2024 的跨语言扩展属增量贡献；最有趣的 detection-decision dissociation 仅在 Llama 成立；XNLI baseline 比较方法论有价值但核心结论偏 negative（不对称性非冲突特异） |
| Reproducibility | 4/5 | 数据集（ConflictQA）、模型、probing 方法描述清晰；bootstrap 置信区间和 Bonferroni 校正规范；steering 的 σ 扫描范围和随机种子数明确 |
| Confidence | 4/5 | 熟悉 knowledge conflict detection、cross-lingual probing、representation steering 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **标题 "Cross-Lingual" 过度泛化：仅测试 EN-ZH 一个语言对**
- 具体位置：Title, Abstract, Section 1 (Introduction)
- 问题：标题使用 "Cross-Lingual" 暗示跨语言通用性，但实验仅涉及英语-中文一个语言对。英语和中文在类型学上差异极大（SVO vs. SVO 但书写系统、形态完全不同），在这一对上的发现无法直接推广到其他语言对（如 EN-DE、EN-JA、ZH-JA 等）。论文自身在 Limitations (p9) 承认 "We evaluate only one language pair (English-Chinese)"，但标题未作限定。
- 为什么影响接收：ACL ARR reviewer guidelines 明确要求 "Claims match evidence presented"。标题是论文最重要的 claim 载体，对单一语言对的结论使用无限定的 "Cross-Lingual" 构成 overclaiming。实际上，论文自己的 XNLI 数据引用了 Kargaran et al. (2024) 关于 "conflict resolution preferences vary by language pair" 的发现（p7 Discussion），说明语言对的选择确实影响结论的泛化性。
- 建议：(a) 将标题改为包含 "English-Chinese" 限定；(b) 或增加至少 1-2 个类型学不同的语言对（如 EN-DE 或 EN-JA）以支撑 "Cross-Lingual" 的泛化声称。

**N2** [critical] **"Inherit" 因果措辞缺乏因果证据**
- 具体位置：Title ("Inherit Directional Asymmetries"), Abstract ("inheriting from the model's general multilingual structure"), Section 4.4 (p5), Section 5 Discussion (p7)
- 问题：标题核心动词 "Inherit" 意味着因果关系——冲突信号的不对称性*因为*继承自通用跨语言表征而产生。但实际证据仅是相关性：冲突 probing 不对称性和 XNLI 非冲突 baseline 不对称性在量级和方向上一致（CI 重叠）。CI 重叠仅说明无法拒绝零假设（两者相同），不等于证明共享机制。论文未提供任何因果实验（如 ablation 去除 cross-lingual alignment 后观察冲突不对称性变化）来建立 "inheritance" 路径。
- 为什么影响接收：这不仅是措辞问题——"Inherit" 是论文的核心 narrative（三个 contribution 中的第一个）。如果降级为相关性观察，contribution 的实质性会显著降低。
- 建议：(a) 将 "Inherit" 替换为更弱的措辞如 "Mirror" 或 "Parallel"；(b) 在 Discussion 中明确区分相关性证据和因果 claim；(c) 或设计额外实验建立因果链（如在 representation alignment 被人工破坏的条件下检验冲突不对称性是否消失）。

**N3** [critical] **Steering 证据不足以支撑 detection-decision dissociation 作为通用发现**
- 具体位置：Abstract ("These findings demonstrate that linear detectability does not imply causal relevance"), Section 4.6 (p6-7, Table 3), Section 5 Discussion (p7)
- 问题：Steering 仅在 Llama L13 (41% depth) 产生显著因果效果（Fisher p = 0.002, Bonferroni 校正后）。Qwen (L14, n=131, best p = 0.785) 和 Gemma (L17, n=171, best p = 0.418) 在所有层均无显著 steering 效果（zero directional flips）。Detection-decision dissociation 因此是单模型发现，而非通用现象。然而 abstract 表述 "These findings demonstrate..." 暗示通用性。
- 为什么影响接收：将 n=1 模型的发现包装为 "demonstrate" 级别的结论，且列为三个 contribution 之一（"Detection-decision layer dissociation"），是 overclaiming。Qwen/Gemma 的 steering 全面失败更可能说明 probe-based steering 方法本身的局限性，而非 detection ≠ decision 的通用规律。
- 建议：(a) 将 abstract 中的 "demonstrate" 改为 "suggest" 或限定为 "in Llama"；(b) 在 contributions 列表中将此项从 contribution 降级为 observation；(c) 对 Qwen/Gemma steering 失败提供更深入的分析（见 W4）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **遗漏重要相关工作：跨语言 activation steering**
- 具体位置：Section 2 Related Work (p2-3)
- 问题：以下直接相关的近期工作未被引用：
  1. Pokharel, Agrawal & Nagar (2026). "Cross-Lingual Activation Steering for Multilingual Language Models." arXiv:2601.16390 (Jan 2026) — 提出跨语言 activation steering 方法 CLAS，直接涉及本文核心方法论（cross-lingual + steering），且发现 "effective transfer operates through functional divergence rather than strict alignment"，与本文的 XNLI baseline 发现形成对话。
  2. "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models." arXiv:2502.15639 (Feb 2025) — 分析模型干预对跨语言对齐的影响，直接相关于本文 Section 3.6 和 Section 5 的 steering 讨论。
- 建议：在 Related Work 的 "Representation steering and causal intervention" 段落中增加这些引用，并讨论本文 steering 结果与它们的异同。

**W2** [warning] **Contribution 2（detection-decision dissociation）缺乏泛化性**
- 具体位置：Section 1 contributions list (p2), Section 5 Discussion (p7)
- 问题：论文将 detection-decision dissociation 列为三个 contribution 之一，但这仅在 Llama 中观察到。在 Qwen 和 Gemma 中，既没有成功的 steering 也就无法验证是否存在 dissociation（不是 dissociation 不存在，而是 steering 方法本身失效了，无法区分）。
- 建议：明确表述 "在 Llama 中观察到 dissociation，Qwen/Gemma 由于 steering 方法失效无法验证"，而非暗示这是三个模型的共同发现。

**W3** [warning] **Confound exclusion pipeline 的局限性未充分讨论**
- 具体位置：Section 4.5 (p5-6, Table 2), Section 3.5
- 问题：
  (a) Translation quality confound：通过 COMET score 分层（Table 2）排除，但 Qwen 的 COMET tercile 分层显示 Δ = −1.7 pp (p = 0.061) 即翻译质量低的样本确实有影响但被忽略。Llama 的显著效果 (Δ = +1.7, p = 0.063 → 实际未达 0.05) 也接近边界。用 tercile 粗分层可能遗漏细粒度效应。
  (b) Token overlap confound：Pearson 相关分析（p5-6）显示 Llama 有 weak negative correlation (r = −0.15, p = 0.014)，这说明 overlap 确实与 probe accuracy 相关，仅靠 "weak" 的定性判断不足以排除。
  (c) 未考虑翻译过程引入的系统性实体表征偏差（如中文实体名的音译/意译选择）。
- 建议：在 Limitations 或 Discussion 中更明确地承认这些局限。

**W4** [warning] **对 Qwen/Gemma steering 失败的分析不足**
- 具体位置：Section 4.6 (p6-7), Section 5 Discussion (p7-8)
- 问题：Gemma 的 88.9% probe accuracy 是三个模型中最高的，但 steering 完全无效（zero directional flips）。论文正确指出这 "rules out probe quality as a confound"（p7），是一个 "informative negative"。但分析仅停留在 "the causal influence of the probe direction is architecture-dependent" 的结论层面，未提供 mechanistic 假设：为什么高精度 probe 方向在 steering 时无效？是否与这些模型的 residual stream 结构、attention pattern、或 layer normalization 实现有关？
- 建议：增加至少一段讨论，提出可检验的 mechanistic 假设。

**W5** [warning] **新颖性相对 Zhao et al. 2024 的增量贡献需更明确定位**
- 具体位置：Section 1 Introduction (p1-2), Section 2 Related Work (p2-3)
- 问题：Zhao et al. (2024) 已建立了 residual stream probing 检测知识冲突的框架。本文的主要创新是 (1) 跨语言扩展，(2) XNLI baseline 比较，(3) steering 实验。其中 (1) 是直接扩展，(3) 大部分失败。真正独特的贡献是 (2) XNLI baseline comparison 的方法论思路——但这本质上是一个 negative finding（不对称性非冲突特异）。论文应更坦诚地定位自己相对于 Zhao et al. 的增量幅度。
- 建议：在 Introduction 中更明确地 articulate "beyond Zhao et al., our unique methodological contribution is..."，而非通过三个并列的 contributions 暗示对等的创新量。

---

## 小问题（不影响接收）

1. **Abstract 措辞**: "Our analysis confronts cross-lingual transfer" — "confronts" 用词不常见，建议改为 "examines" 或 "addresses"。
2. **Figure 1 可读性**: 三个模型的 layer-wise probe accuracy 曲线（p5）在打印时较难辨认，特别是 dashed lines（MLP subspace probes）和 star markers。建议增大图幅或拆分为三个 subplot。
3. **Table 1 注释**: "Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies" — 这个重要注释放在 table 脚注中容易被忽略，建议在正文 Section 4.3 中显著提及。
4. **Section 3.2 数据过滤**: "filtering samples by querying each model without context and retaining only those answered correctly" — 这个过滤步骤可能引入选择偏差（只保留模型自信的知识），应在 Limitations 中提及。
5. **p3 "Bělohlavek 2022"**: Related Work 中 "Probing classifiers" 引用 Bellinkov 2022，请确认拼写。
6. **Appendix 结构**: Appendix A (Use of AI Assistants), B (Causal Boundary), C (Matched-Condition) 的安排合理，但 Appendix B 的 Table 4 和 Appendix C 的 Table 5 中部分数据对理解主文 claims 至关重要（如 Llama causal gradient 的精确层定位），考虑将关键结果提升到正文。
7. **References 格式**: 检查 arXiv preprint 引用是否已被会议接收（如 Zhao et al. 2024 已被 NeurIPS 接收，应更新引用格式）。

---

## 主要优势

1. **研究问题定位精准**: 将 mechanistic interpretability 和 multilingual NLP 的交叉领域具体化为一个清晰可检验的问题，不泛泛而谈。
2. **XNLI baseline 比较是方法论亮点**: 用非冲突跨语言任务的迁移不对称性作为控制条件，系统地检验冲突信号不对称性的特异性——这个 experimental design choice 值得社区借鉴，即使结论是 negative 的。
3. **诚实报告负面结果**: Qwen/Gemma steering 失败被完整报告而非隐藏，且 Gemma 的 "high detectability + zero steering effect" 被正确解读为 informative negative，体现了良好的科学态度。
4. **Confound exclusion 流程系统化**: 翻译质量分层 + token overlap 分析 + 非冲突 baseline 三重检查，虽然各环节有局限，但作为 pipeline 展示了对 probing 研究中 confound 的重视。
5. **三模型比较**: 在 Llama/Qwen/Gemma 三个架构上的一致性和差异性都提供了有价值的信息（尤其是一致的 detectability 和分化的 steerability）。

---

## 缺失的关键相关工作

| 引用 | 相关性 | 为什么应该引用 |
|------|--------|--------------|
| Pokharel et al. 2026 "Cross-Lingual Activation Steering" (arXiv:2601.16390) | 直接相关 | 跨语言 + steering，本文核心方法的最近相关工作 |
| "Steering into New Embedding Spaces" (arXiv:2502.15639, Feb 2025) | 直接相关 | 分析 cross-lingual alignment 在 model intervention 下的变化 |
| "Steering Knowledge Selection Behaviours in LLMs" (arXiv:2410.15999, Oct 2024) | 高度相关 | 专门研究知识选择行为的 steering，与本文 Section 3.6 直接对话 |

---

## Questions for Authors

1. XNLI baseline 和 conflict probing 的 CI 重叠是否能排除两者由不同机制产生但碰巧量级相近的可能？是否考虑过用 partial correlation 或 mediation analysis 进一步检验？
2. Qwen/Gemma steering 失败是否可能与 steering 方法本身（probe direction injection）在这些架构上的适用性有关，而非反映 detection-decision dissociation 的缺失？是否尝试过其他 steering 方法（如 Activation Addition, DAS）？
3. ConflictQA 数据集过滤后 Llama 保留 1,368 样本、Qwen 966、Gemma 1,590——模型间样本差异较大，是否会影响跨模型比较的公平性？
4. 翻译使用 Qwen3-SB，这与实验模型 Qwen3-8B 同系列——是否存在 translation model 偏好同系列模型 tokenization 的风险，从而影响 token overlap confound analysis？

---

## 总结

本文在跨语言知识冲突的 mechanistic interpretability 方向做了系统的实证探索，方法论设计（特别是 XNLI baseline 比较）有亮点，负面结果的诚实报告体现了良好的科学态度。但三个核心问题——标题对单语言对结果的过度泛化、相关性证据包装为因果 "Inherit"、以及单模型 steering 结果推广为通用 "demonstrate" ——构成了 claim-evidence 的系统性不匹配。建议：(1) 收窄标题和 abstract 的 claim 强度，(2) 补充 1-2 个额外语言对或将标题限定为 EN-ZH，(3) 将 detection-decision dissociation 定位为 Llama-specific observation 而非通用 contribution。修改后适合 Findings track 接收。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-24T16:40:29.580458+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个 Must-Fix 和 Should-Fix 问题用 `[AGREE]` 或 `[REBUT]` 回应，附简要理由。重点关注你们之间的分歧点。\n\n---\n\n以下是 Reviewer 2 的完整审稿：\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法论扎实的跨语言 probing 实证研究，但标题和 abstract 对证据的过度泛化（单语言对声称 \"Cross-Lingual\"、相关性包装为因果 \"Inherit\"、单模型发现推广为通用结论）削弱了贡献的可信度。\n\n### Must-Fix 问题\n\n**N1** [critical] **标题 \"Cross-Lingual\" 过度泛化：仅测试 EN-ZH 一个语言对**\n- 标题使用 \"Cross-Lingual\" 暗示跨语言通用性，但实验仅涉及英语-中文一个语言对。论文自身在 Limitations 承认这一点，但标题未作限定。ACL ARR 要求 claims match evidence。\n- 建议：标题加 \"English-Chinese\" 限定，或增加 1-2 个语言对。\n\n**N2** [critical] **\"Inherit\" 因果措辞缺乏因果证据**\n- 标题核心动词 \"Inherit\" 意味因果关系，但实际证据仅是 CI 重叠的相关性。未提供任何因果实验（如 ablation 去除 cross-lingual alignment 后观察变化）。\n- 建议：替换为 \"Mirror\" 或 \"Parallel\"，或设计因果实验。\n\n**N3** [critical] **Steering 证据不足以支撑 detection-decision dissociation 作为通用发现**\n- Steering 仅在 Llama L13 成功（Fisher p = 0.002），Qwen/Gemma 全面失败（zero directional flips）。但 abstract 用 \"demonstrate\" 暗示通用性。\n- 建议：限定为 \"in Llama\" 或降级为 observation。\n\n### Should-Fix 问题\n\n**W1** 遗漏重要相关工作：Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390)、\"Steering into New Embedding Spaces\" (arXiv:2502.15639)、\"Steering Knowledge Selection Behaviours\" (arXiv:2410.15999)\n\n**W2** Contribution 2（detection-decision dissociation）缺乏泛化性，仅在 Llama 观察到。\n\n**W3** Confound exclusion pipeline 局限性未充分讨论：Qwen COMET tercile Δ = −1.7 pp (p = 0.061) 接近边界；Llama token overlap weak negative correlation (r = −0.15, p = 0.014)。\n\n**W4** 对 Qwen/Gemma steering 失败的分析不足——高精度 probe 方向在 steering 时无效的 mechanistic 原因未讨论。\n\n**W5** 新颖性相对 Zhao et al. 2024 的增量贡献需更明确定位。\n\n### Questions for Authors\n1. XNLI 和 conflict probing 的 CI 重叠能否排除不同机制碰巧量级相近？\n2. Qwen/Gemma steering 失败是否可能是方法本身的局限而非反映 dissociation 缺失？\n3. 模型间样本差异（Llama 1368 / Qwen 966 / Gemma 1590）是否影响跨模型比较公平性？\n4. 翻译用 Qwen3-SB 与实验模型 Qwen3-8B 同系列，是否存在 tokenization 偏好风险？",
  "reviewer_id": "1",
  "project": "clkc_mech_interp",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个 Must-Fix 和 Should-Fix 问题用 `[AGREE]` 或 `[REBUT]` 回应，附简要理由。重点关注你们之间的分歧点。\n\n---\n\n以下是 Reviewer 2 的完整审稿：\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法论扎实的跨语言 probing 实证研究，但标题和 abstract 对证据的过度泛化（单语言对声称 \"Cross-Lingual\"、相关性包装为因果 \"Inherit\"、单模型发现推广为通用结论）削弱了贡献的可信度。\n\n### Must-Fix 问题\n\n**N1** [critical] **标题 \"Cross-Lingual\" 过度泛化：仅测试 EN-ZH 一个语言对**\n- 标题使用 \"Cross-Lingual\" 暗示跨语言通用性，但实验仅涉及英语-中文一个语言对。论文自身在 Limitations 承认这一点，但标题未作限定。ACL ARR 要求 claims match evidence。\n- 建议：标题加 \"English-Chinese\" 限定，或增加 1-2 个语言对。\n\n**N2** [critical] **\"Inherit\" 因果措辞缺乏因果证据**\n- 标题核心动词 \"Inherit\" 意味因果关系，但实际证据仅是 CI 重叠的相关性。未提供任何因果实验（如 ablation 去除 cross-lingual alignment 后观察变化）。\n- 建议：替换为 \"Mirror\" 或 \"Parallel\"，或设计因果实验。\n\n**N3** [critical] **Steering 证据不足以支撑 detection-decision dissociation 作为通用发现**\n- Steering 仅在 Llama L13 成功（Fisher p = 0.002），Qwen/Gemma 全面失败（zero directional flips）。但 abstract 用 \"demonstrate\" 暗示通用性。\n- 建议：限定为 \"in Llama\" 或降级为 observation。\n\n### Should-Fix 问题\n\n**W1** 遗漏重要相关工作：Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390)、\"Steering into New Embedding Spaces\" (arXiv:2502.15639)、\"Steering Knowledge Selection Behaviours\" (arXiv:2410.15999)\n\n**W2** Contribution 2（detection-decision dissociation）缺乏泛化性，仅在 Llama 观察到。\n\n**W3** Confound exclusion pipeline 局限性未充分讨论：Qwen COMET tercile Δ = −1.7 pp (p = 0.061) 接近边界；Llama token overlap weak negative correlation (r = −0.15, p = 0.014)。\n\n**W4** 对 Qwen/Gemma steering 失败的分析不足——高精度 probe 方向在 steering 时无效的 mechanistic 原因未讨论。\n\n**W5** 新颖性相对 Zhao et al. 2024 的增量贡献需更明确定位。\n\n### Questions for Authors\n1. XNLI 和 conflict probing 的 CI 重叠能否排除不同机制碰巧量级相近？\n2. Qwen/Gemma steering 失败是否可能是方法本身的局限而非反映 dissociation 缺失？\n3. 模型间样本差异（Llama 1368 / Qwen 966 / Gemma 1590）是否影响跨模型比较公平性？\n4. 翻译用 Qwen3-SB 与实验模型 Qwen3-8B 同系列，是否存在 tokenization 偏好风险？",
    "reviewer_id": "1",
    "project": "clkc_mech_interp",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-24T16:40:48.873050+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19292
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-24T16:40:49.277057+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个 Must-Fix 和 Should-Fix 问题用 `[AGREE]` 或 `[REBUT]` 回应，附简要理由。重点关注你们之间的分歧点。\n\n---\n\n以下是 Reviewer 1 的完整审稿：\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**M1** [critical] **单种子设计不满足当前 probing 标准**\n- 所有 probing 实验使用单一随机种子，不满足 Sellam et al. 2022 和 Dodge et al. 2020 建立的多种子标准。Bootstrap CI 仅量化采样不确定性，不覆盖训练随机性。\n- 建议：至少 5 个随机种子，报告均值±标准差。\n\n**M2** [critical] **TOST 等价检验无功效却做了等价结论**\n- Section 4.4 用 TOST 检验 conflict 和 XNLI 不对称性的等价性，但未报告统计功效（power）。在样本量有限时，TOST 不显著可能仅因检验功效不足，而非真正等价。\n- 建议：报告 power analysis，或改用 Bayesian equivalence testing（BF < 1/3 标准）。\n\n**M3** [critical] **因果发现仅 1/3 模型成立但被列为主要贡献**\n- Steering 仅在 Llama 成功，Qwen/Gemma 完全失败。但论文将 \"detection-decision layer dissociation\" 列为三个主要 contribution 之一，构成 overclaiming。\n- 建议：降级为 observation，或在 contribution 声明中限定为 Llama-specific。\n\n### Should-Fix 问题\n\n**S1** Gemma confound 分析数据缺失——Gemma 的 COMET tercile 分层和 token overlap 数据未报告。\n\n**S2** Tercile 分析功效不足——每个 tercile 仅 ~300-500 样本，可能检测不到 2-3pp 的效应。\n\n**S3** 跨模型样本自选择偏差——各模型用自身知识过滤样本（Llama 1368, Qwen 966, Gemma 1590），导致比较的不是同一组事实。\n\n**S4** Abstract 内部一致性——先说 \"shared multilingual representations, not conflict-specific mechanisms\" 又说 \"detectability does not imply causal relevance\"，逻辑跳跃过大。\n\n**S5** 因果边界 \"gradient\" 的统计验证不充分——Llama L13 steering 效果需要更系统的层扫描。\n\n**S6** 不对称性对称点的讨论缺失——Gemma 几乎对称（Δ_asym ~ 0）但论文未充分讨论。\n\n### Reviewer 1 的主要优势评价\n1. Confound exclusion + XNLI baseline + boundary replication 的方法管线\n2. Detection ≠ Decision 发现本身\n3. 三模型比较设计\n4. Bootstrap CI 和 Bonferroni 校正等统计规范\n5. 诚实报告负面结果",
  "reviewer_id": "2",
  "project": "clkc_mech_interp",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个 Must-Fix 和 Should-Fix 问题用 `[AGREE]` 或 `[REBUT]` 回应，附简要理由。重点关注你们之间的分歧点。\n\n---\n\n以下是 Reviewer 1 的完整审稿：\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**M1** [critical] **单种子设计不满足当前 probing 标准**\n- 所有 probing 实验使用单一随机种子，不满足 Sellam et al. 2022 和 Dodge et al. 2020 建立的多种子标准。Bootstrap CI 仅量化采样不确定性，不覆盖训练随机性。\n- 建议：至少 5 个随机种子，报告均值±标准差。\n\n**M2** [critical] **TOST 等价检验无功效却做了等价结论**\n- Section 4.4 用 TOST 检验 conflict 和 XNLI 不对称性的等价性，但未报告统计功效（power）。在样本量有限时，TOST 不显著可能仅因检验功效不足，而非真正等价。\n- 建议：报告 power analysis，或改用 Bayesian equivalence testing（BF < 1/3 标准）。\n\n**M3** [critical] **因果发现仅 1/3 模型成立但被列为主要贡献**\n- Steering 仅在 Llama 成功，Qwen/Gemma 完全失败。但论文将 \"detection-decision layer dissociation\" 列为三个主要 contribution 之一，构成 overclaiming。\n- 建议：降级为 observation，或在 contribution 声明中限定为 Llama-specific。\n\n### Should-Fix 问题\n\n**S1** Gemma confound 分析数据缺失——Gemma 的 COMET tercile 分层和 token overlap 数据未报告。\n\n**S2** Tercile 分析功效不足——每个 tercile 仅 ~300-500 样本，可能检测不到 2-3pp 的效应。\n\n**S3** 跨模型样本自选择偏差——各模型用自身知识过滤样本（Llama 1368, Qwen 966, Gemma 1590），导致比较的不是同一组事实。\n\n**S4** Abstract 内部一致性——先说 \"shared multilingual representations, not conflict-specific mechanisms\" 又说 \"detectability does not imply causal relevance\"，逻辑跳跃过大。\n\n**S5** 因果边界 \"gradient\" 的统计验证不充分——Llama L13 steering 效果需要更系统的层扫描。\n\n**S6** 不对称性对称点的讨论缺失——Gemma 几乎对称（Δ_asym ~ 0）但论文未充分讨论。\n\n### Reviewer 1 的主要优势评价\n1. Confound exclusion + XNLI baseline + boundary replication 的方法管线\n2. Detection ≠ Decision 发现本身\n3. 三模型比较设计\n4. Bootstrap CI 和 Bonferroni 校正等统计规范\n5. 诚实报告负面结果",
    "reviewer_id": "2",
    "project": "clkc_mech_interp",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-24T16:40:50.688938+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Assistant

_source line 190 · 2026-05-24T16:41:01.779126+00:00_

交叉分享已发送。两位 Reviewer 正在阅读对方的审稿意见并逐条回应。

**当前进度**：
- Round 1 初审：✅ 完成（R1: 3.5 Borderline Conference / R2: 3.0 Findings）
- 交叉分享：✅ 已派发，等待回应
- 外部审稿：未请求
- 视觉审查：✅ 已完成（2 warnings + 8 info，无 critical）

**两位 Reviewer 的主要共识**：
1. Steering 仅在 Llama 成功但被列为主要 contribution → overclaiming（R1-M3 ≈ R2-N3）
2. 方法管线（confound exclusion + XNLI baseline）是论文亮点
3. 诚实报告负面结果值得肯定

**主要分歧待交叉分享解决**：
- R2 强调标题 "Cross-Lingual" 和 "Inherit" 的 overclaiming（R1 未单独提出）
- R1 强调统计方法问题（单种子、TOST 功效），R2 未涉及
- 评分差距 0.5 分，需通过交叉回应收敛

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 191 · 2026-05-24T16:41:04.370365+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交至 Review Director。

核心判断：**Overall 3.0 (Findings)**。方法论设计有亮点（XNLI baseline 比较、三模型对比、confound exclusion pipeline），但存在三个系统性 claim-evidence 不匹配：

1. **标题 "Cross-Lingual" 仅测试 EN-ZH 一个语言对** — overclaiming
2. **"Inherit" 因果措辞仅有相关性证据**（CI 重叠 ≠ 因果链）
3. **Detection-decision dissociation 仅在 Llama 成立**，Qwen/Gemma steering 全面失败，但 abstract 用 "demonstrate" 推广为通用结论

另外标记了 3 个遗漏的直接相关工作（Pokharel et al. 2026 跨语言 activation steering 等）和若干 should-fix / minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 192 · 2026-05-24T16:41:16.181217+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 193 · 2026-05-24T16:42:32.497237+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

### Must-Fix

**[AGREE] R2-N1 (标题 "Cross-Lingual" 过度泛化)**: 同意。仅 EN-ZH 一个语言对，EN-DE 分析仅涉及 token overlap 非完整 pipeline。标题应加限定或增加语言对。

**[AGREE] R2-N2 ("Inherit" 因果措辞)**: 强烈同意。与我的 N2（TOST 不显著）直接相关。CI 重叠 + 方向一致仅是相关性，TOST 未通过。"Mirror"/"Parallel" 更准确。

**[AGREE] R2-N3 (Steering 泛化性不足)**: 完全同意，与我的 N3 一致。Abstract 用 "demonstrate" 过强。

### Should-Fix

**[REBUT] R2-W1 (遗漏相关工作)**: 部分反驳。论文 Related Work 已覆盖主要 steering 和跨语言文献。R2 列出的 3 篇论文需验证真实性和相关性，且应说明具体对比点。

**[AGREE] R2-W2 (Contribution 2 泛化性)**: 同意，与 N3 一致。

**[REBUT] R2-W3 (Confound 局限性)**: 同意一般性关切（与我的 W2 一致），但 **R2 引用数据有误**：R2 称 "Qwen COMET tercile Δ=−1.7pp (p=0.061)"——Table 2 实际为 Qwen Δ=−5.6pp, p=0.695；Llama Δ=+1.7pp, p=0.761。R2 将 Llama 的数值误归 Qwen，p 值也不对应论文任何数字。Token overlap p=0.014 实际为 p=0.012。问题是 power 不足，非"接近显著"。

**[AGREE] R2-W4 (Qwen/Gemma 失败 mechanistic 分析)**: 同意。论文应讨论可能原因（非线性机制、attention 架构差异、样本量限制）。

**[REBUT] R2-W5 (相对 Zhao 2024 增量)**: 部分反驳。Zhao 2024 是单模型单语言 probing。本文的 confound exclusion pipeline、XNLI baseline 设计、多模型 steering 比较具有独立方法论价值，非简单"换语言重跑"。

### 主要分歧

| 议题 | R1 | R2 | 性质 |
|------|----|----|------|
| 新颖性 | 方法论扩展有价值 (REBUT) | 增量 | 实质分歧 |
| 遗漏相关工作 | 需验证 (REBUT) | 列 3 篇 | 需澄清 |
| Confound 数据 | R2 数据有误 (REBUT) | Qwen Δ=−1.7pp | 事实性分歧 |
| Overall | 3.5 | 3.0 | R2 更严格 |

0.5 分差异来自新颖性判断。如果作者修复标题 framing + multi-seed，Soundness 可提升至 4/5，整体可达 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 194 · 2026-05-24T16:42:43.854314+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 15

## Round 15

14 recorded events


### User

_source line 195 · 2026-05-24T16:42:46.419688+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心判断：与 R2 在 3 个 Must-Fix 上完全一致（标题泛化、"Inherit" 因果措辞、steering 泛化性）。主要分歧在 Should-Fix 层面——R2 的 confound 数据引用有事实错误（Qwen/Llama 数值混淆），以及对 Zhao et al. 2024 增量性的判断（我认为 confound pipeline 和 XNLI baseline 有独立方法论价值，不应定性为增量）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-24T16:43:05.877790+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-24T16:43:05.978550+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-24T16:43:08.237611+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-24T16:43:08.288205+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-24T16:43:11.198906+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-24T16:43:11.301021+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-24T16:43:14.413302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-24T16:43:14.464151+00:00_

1	issues:
2	- id: "R1-N1"
3	  summary: "Steering 实验 Bonferroni 校正仅层内应用，未跨层校正（30次比较），L13 正方向 p=0.002 在完整校正下不显著"
4	  category: experiment
5	  severity: critical
6	  status: open
7	  first_raised_round: 1
8	  last_seen_round: 1
9	  mentions:
10	    - round: 1
11	      reviewers: [1, 2]
12	      note: "R1 提出，R2 AGREE。独立复现(N=201) p<0.001 和负方向 p<0.001 部分缓解，但需明确报告 family-wise p 值"
13	  action_items:
14	    - round: 1
15	      action: "明确说明层间不校正的理由或采用 FDR/Holm-Bonferroni 校正，报告完整 family-wise p 值"
16	      assigned_to: author
17	      status: pending
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: "R1-N2"
22	  summary: "Detection ≠ Decision 因果声明仅在 Llama 一个模型成立（N=1），Qwen/Gemma 零翻转，泛化性严重不足"
23	  category: method
24	  severity: critical
25	  status: open
26	  first_raised_round: 1
27	  last_seen_round: 1
28	  mentions:
29	    - round: 1
30	      reviewers: [1, 2]
31	      note: "双方一致认为这是论文最核心局限。R2 建议尝试 DAS/activation patching 或降低 claim 强度。R1 指出 Gemma 88.9% probe acc 下零效应构成反证"
32	  action_items:
33	    - round: 1
34	      action: "Abstract/Intro 中 Detection≠Decision 表述加 'in Llama' 限定；讨论 steering 失败是否反映非线性因果结构"
35	      assigned_to: author
36	      status: pending
37	  resolution: ""
38	  resolution_round: null
39	
40	- id: "R2-N2"
41	  summary: "Qwen3-8B 引用错误：引用了 Qwen2.5 Technical Report (arXiv:2412.15115) 而非 Qwen3 (arXiv:2505.09388)"
42	  category: format
43	  severity: critical
44	  status: open
45	  first_raised_round: 1
46	  last_seen_round: 1
47	  mentions:
48	    - round: 1
49	      reviewers: [2, 1]
50	      note: "事实性引用错误，R1 AGREE 必须更正"
51	  action_items:
52	    - round: 1
53	      action: "替换 references.bib 中 yang2024qwen25 为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)"
54	      assigned_to: author
55	      status: pending
56	  resolution: ""
57	  resolution_round: null
58	
59	- id: "R1-W1"
60	  summary: "单种子实验：所有 probing 结果基于单次 train/test split，未报告多种子 mean±std"
61	  category: experiment
62	  severity: warning
63	  status: open
64	  first_ra
…[truncated 4618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-24T16:47:35.954311+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "clkc_mech_interp",
  "issues_yaml": "issues:\n# === CRITICAL (Must-Fix) ===\n\n- id: \"R2-W2\"\n  summary: \"标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构成 overclaiming\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加限定。EN-DE 仅在 confound exclusion 中简要使用\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 升级为 Must-Fix N1，R1 交叉 AGREE。论文自身 Limitations 承认 only one language pair，且引用 Kargaran 2024 指出语言对影响结论泛化\"\n  action_items:\n    - round: 1\n      action: \"标题和 abstract 限定为 EN-ZH，或扩展为更多语言对\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MF-2\"\n  summary: \"标题 'Inherit' 因果措辞仅有 CI 重叠的相关性证据，缺乏因果实验\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 强烈 AGREE 并与 TOST 功效问题联动。CI 重叠≠共享机制，TOST 未报告 power\"\n  action_items:\n    - round: 2\n      action: \"Inherit→Mirror/Parallel；补充 power analysis 或 Bayesian equivalence testing\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立（N=1 模型），Qwen/Gemma 零翻转\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致认为最核心局限。Gemma 88.9% probe acc 下零效应构成反证\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 M3，R2 列为 N3，交叉中双方 AGREE。Abstract 'demonstrate' 暗示通用性构成 overclaiming\"\n  action_items:\n    - round: 1\n      action: \"Abstract/Intro 加 'in Llama' 限定；Contributions 降级为 observation\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING (Should-Fix) ===\n\n- id: \"R1-W1\"\n  summary: \"单种子实验：所有 probing 结果基于单次 train/test split，未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。Peak layer 位置和准确率可能因 split 变化\"\n    - round: 2\n      reviewers: [1]\n      note: \"R1 升级为 Must-Fix M1。R2 未单独列为 must-fix 但 Reproducibility 扣分\"\n  action_items:\n    - round: 1\n      action: \"报告 3-5 个种子的 mean±std\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"非冲突特异声明仅基于 CI 重叠，TOST 等价检验未报告功效\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CI 重叠是必要非充分条件\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix M2，与 MF-2 Inherit 措辞问题联动。R2 同意一般性关切\"\n  action_items:\n    - round: 1\n      action: \"补充 TOST power analysis 或 Bayesian equivalence testing (BF < 1/3)\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 分析统计功效不足（每 tercile 64-91 样本），Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"p=0.695/0.761 无法区分无效应和功效不足\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S2。R2 提出但引用数值有误（将 Llama 数据误归 Qwen），R1 交叉中纠正\"\n  action_items:\n    - round: 1\n      action: \"报告效应量和功效分析；补充 Gemma COMET 结果\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"SF-4\"\n  summary: \"Qwen/Gemma steering 失败缺乏 mechanistic 分析——高精度 probe 方向 steering 无效的原因未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出 W4，R1 交叉 AGREE。应讨论非线性因果结构、attention 架构差异等可能原因\"\n  action_items:\n    - round: 2\n      action: \"增加至少一段 mechanistic 假设讨论\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"建议报告重叠度并在 Limitations 讨论\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S3，R2 列为 Q3\"\n  action_items:\n    - round: 1\n      action: \"报告三模型样本集重叠度，在 Limitations 讨论影响\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"SF-6\"\n  summary: \"新颖性定位：相对 Zhao et al. 2024 的增量性判断存在 Reviewer 分歧\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 认为增量（W5），R1 REBUT——confound pipeline 和 XNLI baseline 有独立方法论价值。分歧未解决\"\n  action_items:\n    - round: 2\n      action: \"Introduction 中更明确 articulate 超越 Zhao 2024 的独特方法论贡献\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"SF-7\"\n  summary: \"遗漏跨语言 steering 相关工作：Pokharel 2026、arXiv:2502.15639、arXiv:2410.15999\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 列出 3 篇，R1 部分反驳——需先验证真实性和具体相关点\"\n  action_items:\n    - round: 2\n      action: \"验证引用真实性后补充，特别是 Pokharel 2026 跨语言 activation steering\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === INFO ===\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 (Qwen3-SB) 与实验对象 (Qwen3-8B) 同系列，可能引入 tokenization 偏好 confound\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"翻译输出可能对 Qwen 的 representation space 有系统性偏好\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 列为 Q4，R1 交叉中同意关切\"\n  action_items:\n    - round: 1\n      action: \"在 Limitations 讨论，或用独立翻译模型验证 Qwen 子集\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 'p<0.05' 与正文 Bonferroni 阈值 0.005 不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一 Table 3 caption 显著性阈值描述\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === R1 ISSUES POSSIBLY RESOLVED (not raised in R2) ===\n\n- id: \"R1-N1\"\n  summary: \"Steering Bonferroni 校正仅层内应用，未跨层校正\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"独立复现部分缓解，需明确报告 family-wise p 值\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未单独提出此问题，可能已在修订中处理或被 MF-3 steering 泛化性问题涵盖\"\n  action_items:\n    - round: 1\n      action: \"明确说明层间不校正的理由或采用 FDR/Holm-Bonferroni\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2-v1\"\n  summary: \"Qwen3-8B 引用错误：引用了 Qwen2.5 Technical Report 而非 Qwen3\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提出，可能已修复。需确认\"\n  action_items:\n    - round: 1\n      action: \"替换为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-v1\"\n  summary: \"Related Work 遗漏 Meng 2022, Geiger 2024, Turner 2023, Marks 2024\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意 Meng 和 Geiger 必须引用\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提出这批引用（R2 改为提出新的 3 篇），可能已补充\"\n  action_items:\n    - round: 1\n      action: \"补充 Meng 2022, Geiger 2024, Turner 2023, Marks 2024\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3-v1\"\n  summary: \"Bib 条目使用非标准 'and others' 格式\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"ACL 模板要求完整作者列表\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提出，可能已修复\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目作者列表\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "clkc_mech_interp",
    "issues_yaml": "issues:\n# === CRITICAL (Must-Fix) ===\n\n- id: \"R2-W2\"\n  summary: \"标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构成 overclaiming\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加限定。EN-DE 仅在 confound exclusion 中简要使用\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 升级为 Must-Fix N1，R1 交叉 AGREE。论文自身 Limitations 承认 only one language pair，且引用 Kargaran 2024 指出语言对影响结论泛化\"\n  action_items:\n    - round: 1\n      action: \"标题和 abstract 限定为 EN-ZH，或扩展为更多语言对\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MF-2\"\n  summary: \"标题 'Inherit' 因果措辞仅有 CI 重叠的相关性证据，缺乏因果实验\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 强烈 AGREE 并与 TOST 功效问题联动。CI 重叠≠共享机制，TOST 未报告 power\"\n  action_items:\n    - round: 2\n      action: \"Inherit→Mirror/Parallel；补充 power analysis 或 Bayesian equivalence testing\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立（N=1 模型），Qwen/Gemma 零翻转\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致认为最核心局限。Gemma 88.9% probe acc 下零效应构成反证\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 M3，R2 列为 N3，交叉中双方 AGREE。Abstract 'demonstrate' 暗示通用性构成 overclaiming\"\n  action_items:\n    - round: 1\n      action: \"Abstract/Intro 加 'in Llama' 限定；Contributions 降级为 observation\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING (Should-Fix) ===\n\n- id: \"R1-W1\"\n  summary: \"单种子实验：所有 probing 结果基于单次 train/test split，未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致。Peak layer 位置和准确率可能因 split 变化\"\n    - round: 2\n      reviewers: [1]\n      note: \"R1 升级为 Must-Fix M1。R2 未单独列为 must-fix 但 Reproducibility 扣分\"\n  action_items:\n    - round: 1\n      action: \"报告 3-5 个种子的 mean±std\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"非冲突特异声明仅基于 CI 重叠，TOST 等价检验未报告功效\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CI 重叠是必要非充分条件\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix M2，与 MF-2 Inherit 措辞问题联动。R2 同意一般性关切\"\n  action_items:\n    - round: 1\n      action: \"补充 TOST power analysis 或 Bayesian equivalence testing (BF < 1/3)\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 分析统计功效不足（每 tercile 64-91 样本），Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"p=0.695/0.761 无法区分无效应和功效不足\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S2。R2 提出但引用数值有误（将 Llama 数据误归 Qwen），R1 交叉中纠正\"\n  action_items:\n    - round: 1\n      action: \"报告效应量和功效分析；补充 Gemma COMET 结果\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"SF-4\"\n  summary: \"Qwen/Gemma steering 失败缺乏 mechanistic 分析——高精度 probe 方向 steering 无效的原因未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出 W4，R1 交叉 AGREE。应讨论非线性因果结构、attention 架构差异等可能原因\"\n  action_items:\n    - round: 2\n      action: \"增加至少一段 mechanistic 假设讨论\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"建议报告重叠度并在 Limitations 讨论\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S3，R2 列为 Q3\"\n  action_items:\n    - round: 1\n      action: \"报告三模型样本集重叠度，在 Limitations 讨论影响\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"SF-6\"\n  summary: \"新颖性定位：相对 Zhao et al. 2024 的增量性判断存在 Reviewer 分歧\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 认为增量（W5），R1 REBUT——confound pipeline 和 XNLI baseline 有独立方法论价值。分歧未解决\"\n  action_items:\n    - round: 2\n      action: \"Introduction 中更明确 articulate 超越 Zhao 2024 的独特方法论贡献\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"SF-7\"\n  summary: \"遗漏跨语言 steering 相关工作：Pokharel 2026、arXiv:2502.15639、arXiv:2410.15999\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 列出 3 篇，R1 部分反驳——需先验证真实性和具体相关点\"\n  action_items:\n    - round: 2\n      action: \"验证引用真实性后补充，特别是 Pokharel 2026 跨语言 activation steering\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === INFO ===\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 (Qwen3-SB) 与实验对象 (Qwen3-8B) 同系列，可能引入 tokenization 偏好 confound\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"翻译输出可能对 Qwen 的 representation space 有系统性偏好\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 列为 Q4，R1 交叉中同意关切\"\n  action_items:\n    - round: 1\n      action: \"在 Limitations 讨论，或用独立翻译模型验证 Qwen 子集\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 'p<0.05' 与正文 Bonferroni 阈值 0.005 不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一 Table 3 caption 显著性阈值描述\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === R1 ISSUES POSSIBLY RESOLVED (not raised in R2) ===\n\n- id: \"R1-N1\"\n  summary: \"Steering Bonferroni 校正仅层内应用，未跨层校正\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"独立复现部分缓解，需明确报告 family-wise p 值\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未单独提出此问题，可能已在修订中处理或被 MF-3 steering 泛化性问题涵盖\"\n  action_items:\n    - round: 1\n      action: \"明确说明层间不校正的理由或采用 FDR/Holm-Bonferroni\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2-v1\"\n  summary: \"Qwen3-8B 引用错误：引用了 Qwen2.5 Technical Report 而非 Qwen3\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提出，可能已修复。需确认\"\n  action_items:\n    - round: 1\n      action: \"替换为 Qwen3 Technical Report (Yang et al., 2025; arXiv:2505.09388)\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-v1\"\n  summary: \"Related Work 遗漏 Meng 2022, Geiger 2024, Turner 2023, Marks 2024\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意 Meng 和 Geiger 必须引用\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提出这批引用（R2 改为提出新的 3 篇），可能已补充\"\n  action_items:\n    - round: 1\n      action: \"补充 Meng 2022, Geiger 2024, Turner 2023, Marks 2024\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3-v1\"\n  summary: \"Bib 条目使用非标准 'and others' 格式\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"ACL 模板要求完整作者列表\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提出，可能已修复\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目作者列表\"\n      assigned_to: author\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-24T16:47:36.006047+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml\", \"bytes\": 8561}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-24T16:49:37.033068+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 圆桌审稿报告 — Round 2\n\n**论文**: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/写作质量)\n**流程**: Round 1 初审 + 交叉分享，一轮收敛\n\n---\n\n## Summary\n\n论文研究跨语言知识冲突在 LLM 内部表征中的 mechanistic 特征，在 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B-IT 三个模型上通过 residual stream probing 检测冲突信号，发现：(1) 三个模型均能线性检测冲突（peak accuracy 80-89%），且存在 EN→ZH 方向不对称性；(2) 该不对称性与非冲突 XNLI 任务的迁移不对称性在量级和方向上一致（CI 重叠）；(3) 仅 Llama L13 的 steering 实验产生显著因果效应，Qwen/Gemma 均为零效应。\n\n两位 Reviewer 在三个核心 Must-Fix 上完全一致，Should-Fix 层面有局部分歧（新颖性判断、遗漏引用验证）。\n\n---\n\n## Strengths\n\n1. **XNLI baseline 比较的方法论设计**：用非冲突跨语言任务作为控制条件检验不对称性的特异性，是论文最独特的方法论贡献。（R1, R2 一致）\n2. **诚实报告负面结果**：Qwen/Gemma steering 全面失败被完整报告，Gemma 高 probe accuracy + 零 steering 效应被正确解读为 informative negative。（R1, R2 一致）\n3. **Confound exclusion pipeline 系统化**：翻译质量分层 + token overlap 分析 + 非冲突 baseline 三重检查。（R1, R2 一致）\n4. **三模型比较**：一致的 detectability 和分化的 steerability 提供有价值的对比信息。（R1, R2 一致）\n5. **统计规范**：Bootstrap CI、Bonferroni 校正、效应量报告。（R1）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，双方完全共识）\n\n**MF-1** [critical] **标题 \"Cross-Lingual\" 过度泛化**\n实验仅覆盖 EN-ZH 一个语言对，但标题使用无限定的 \"Cross-Lingual\"。论文自身 Limitations 承认 \"only one language pair\"，且引用 Kargaran et al. (2024) 指出 conflict resolution preferences vary by language pair。标题是论文最重要的 claim 载体，单一语言对使用无限定泛化术语构成 overclaiming。\n- **R1**: AGREE | **R2**: 提出 → **共识**\n- 建议：标题加 \"English-Chinese\" 限定，或增加 1-2 个类型学不同的语言对。\n\n**MF-2** [critical] **\"Inherit\" 因果措辞仅有相关性证据**\n标题核心动词 \"Inherit\" 意味因果关系（冲突不对称性*因继承*通用跨语言结构而产生），但证据仅为 CI 重叠和方向一致的相关性。CI 重叠仅说明无法拒绝两者不同，不等于共享机制。论文未提供任何因果实验（如 ablation 破坏 cross-lingual alignment 后观察冲突不对称性变化）。R1 补充指出 TOST 等价检验未报告功效，进一步削弱等价声称。\n- **R1**: 强烈 AGREE（与 TOST 问题联动） | **R2**: 提出 → **共识**\n- 建议：替换为 \"Mirror\"/\"Parallel\"；补充 power analysis 或 Bayesian equivalence testing。\n\n**MF-3** [critical] **Detection-decision dissociation 仅 Llama 成立，不支持通用结论**\nSteering 仅在 Llama L13 产生显著因果效应（Fisher p = 0.002），Qwen（best p = 0.785）和 Gemma（best p = 0.418）在所有层均为零 directional flips。Abstract 使用 \"demonstrate\" 暗示通用性，且列为三大 contribution 之一。Gemma 88.9% probe accuracy 下的零效应尤其构成反证——排除 probe 质量作为 confound 后，steering 失败更可能反映方法局限性或架构依赖性。\n- **R1**: 提出 | **R2**: 提出 → **共识**（交叉中双方 AGREE）\n- 建议：Abstract/Intro 加 \"in Llama\" 限定；Contributions 列表中降级为 observation；增加 mechanistic 讨论。\n\n### Should-Fix（影响评分，存在部分分歧）\n\n**SF-1** [warning] **单种子实验设计**\n所有 probing 实验使用单一随机种子，不满足 Sellam et al. 2022 多种子标准。Bootstrap CI 仅量化采样不确定性，不覆盖训练随机性。\n- **R1**: Must-Fix 级别 | **R2**: 未单独列为 must-fix（Reproducibility 4/5）\n- 建议：至少 3-5 个种子，报告均值±标准差。\n\n**SF-2** [warning] **TOST 等价检验无 power analysis**\nSection 4.4 用 TOST 检验等价性但未报告统计功效。样本量有限时 TOST 不显著可能仅因功效不足。\n- **R1**: Must-Fix 级别 | **R2**: 同意一般性关切\n- 建议：补充 power analysis 或改用 Bayesian equivalence testing (BF < 1/3)。\n\n**SF-3** [warning] **Confound exclusion pipeline 局限性**\n(a) COMET tercile 分层每组仅 64-91 样本，功效不足以检测 2-3pp 效应；Gemma 数据未报告。(b) Llama token overlap 有 weak negative correlation (r = −0.15, p = 0.012)，仅靠 \"weak\" 定性判断不足以排除。(c) 翻译模型 Qwen3-SB 与实验对象 Qwen3-8B 同系列，可能引入 tokenization 偏好 confound。\n- **事实性澄清**：R1 交叉回应中指出 R2 将 Llama Δ=+1.7pp 误归为 Qwen，p 值也不对应论文数字。Table 2 实际为 Qwen Δ=−5.6pp, p=0.695；Llama Δ=+1.7pp, p=0.761。\n\n**SF-4** [warning] **Qwen/Gemma steering 失败缺乏 mechanistic 分析**\nGemma 88.9% probe accuracy 但 steering 零效应。论文仅结论 \"architecture-dependent\"，未讨论可能原因：非线性因果结构、residual stream 结构差异、attention pattern、layer normalization 实现差异等。\n- **R1**: AGREE | **R2**: 提出 → **共识**\n\n**SF-5** [warning] **跨模型样本自选择偏差**\n各模型用自身知识过滤样本（Llama 1368, Qwen 966, Gemma 1590），导致跨模型比较基于不同样本集。建议报告三模型样本集重叠度并在 Limitations 讨论。\n- **R1**: 提出 | **R2**: AGREE\n\n**SF-6** [warning/disputed] **新颖性相对 Zhao et al. 2024 的定位**\n- **R2**: 认为增量贡献——Zhao 已建立 probing 框架，本文主要是跨语言扩展 + 大部分失败的 steering\n- **R1**: REBUT——confound exclusion pipeline、XNLI baseline 设计、多模型比较有独立方法论价值\n- **分歧未解决**，两种判断均有道理。建议作者在 Introduction 中更明确 articulate 独特贡献。\n\n**SF-7** [warning] **遗漏相关工作**\nR2 指出遗漏 3 篇直接相关工作：Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390)、\"Steering into New Embedding Spaces\" (arXiv:2502.15639)、\"Steering Knowledge Selection Behaviours\" (arXiv:2410.15999)。R1 部分反驳，认为需先验证真实性和具体相关点。\n\n### Minor（不影响接收）\n\n1. Abstract \"confronts\" 用词不常见，建议改为 \"examines\"\n2. Figure 1 部分模型颜色在小尺寸下辨识度偏低，建议增加 marker shape 差异\n3. Table 1 注释（Δ_asym 定义）放在脚注中易被忽略，建议在正文 Section 4.3 显著提及\n4. Section 3.2 数据过滤可能引入选择偏差（只保留模型自信的知识），应在 Limitations 提及\n5. Appendix B/C 中部分关键数据考虑提升到正文\n6. 检查 arXiv preprint 引用是否已被会议接收并更新格式\n\n---\n\n## Questions for Authors\n\n1. CI 重叠能否排除冲突不对称性和 XNLI 不对称性由不同机制碰巧量级相近的可能？是否考虑过 partial correlation 或 mediation analysis？（R2）\n2. Qwen/Gemma steering 失败是否可能是 probe direction injection 方法本身在这些架构上的适用性问题？是否尝试过 Activation Addition、DAS 等替代方法？（R2）\n3. 模型间样本差异（1368/966/1590）对跨模型比较公平性的影响？（R2）\n4. 翻译模型 Qwen3-SB 与实验模型同系列的 tokenization 偏好风险？（R1, R2）\n5. 多种子实验下 peak layer 位置和不对称性量级是否稳定？（R1）\n6. Abstract 中 \"shared multilingual representations\" 和 \"detectability does not imply causal relevance\" 的逻辑衔接如何加强？（R1）\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 共识状态 |\n|------|------|----------|\n| Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390) | R2 | R1 待验证 |\n| \"Steering into New Embedding Spaces\" (arXiv:2502.15639) | R2 | R1 待验证 |\n| \"Steering Knowledge Selection Behaviours\" (arXiv:2410.15999) | R2 | R1 待验证 |\n\nRound 1 曾指出遗漏的 Meng 2022、Geiger 2024、Turner 2023、Marks 2024 在本轮未被再次提出，可能已补充。\n\n---\n\n## External Review\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：✅ 已完成（0 critical, 2 warning, 8 info）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Pages 1-4 | 连续 4 页纯文本无 display item，第一个 figure 到 page 5 才出现。建议将 Figure 1 或 pipeline 概览图前置到 page 2-3 |\n| ⚠️ warning | Page 5 | Figure 1 + Table 1 + Figure 2 三个 display item 挤在同一页，与前 4 页空旷形成不均匀节奏。建议分散到相邻页 |\n| ℹ️ info | Page 5 | Figure 1 部分模型颜色小尺寸下辨识度偏低 |\n| ℹ️ info | Page 5 | Figure 2 bar 标签字号偏小（建议 ≥8pt） |\n| ℹ️ info | Pages 5-7 | Tables 1-3 booktabs 风格规范专业 |\n| ℹ️ info | General | 无 margin 溢出、无公式渲染错误、页眉页脚符合 ACL 匿名投稿模板 |\n\n---\n\n## Overall Assessment\n\n| Reviewer | 分数 | 定位 |\n|----------|------|------|\n| R1 | 3.5 | Borderline Conference |\n| R2 | 3.0 | Findings |\n| **圆桌共识** | **3.0** | **Findings** |\n\n### 评分理由\n\n三个核心 Must-Fix 问题均为 claim-evidence 系统性不匹配，两位 Reviewer 完全一致：\n1. 标题 \"Cross-Lingual\" 泛化 vs. 单一语言对证据\n2. \"Inherit\" 因果措辞 vs. 相关性证据\n3. \"Demonstrate\" 通用结论 vs. 单模型 steering 成功\n\n这些不是表述瑕疵——它们直接影响论文的 contribution 定位和可信度。论文的方法论设计（XNLI baseline、confound exclusion pipeline、三模型比较）有独立价值，但当前 framing 将方法论优势包装为超出证据的结论。\n\n**0.5 分分歧来源**：R1 认为方法论扩展有独立价值，修复 framing + multi-seed 后可达 Conference；R2 认为即使修复，核心贡献仍为增量性（XNLI baseline 是 negative finding，steering 大部分失败）。\n\n### 修改路径\n\n收窄标题和 abstract claims → 补充多种子实验 → 增加 TOST power analysis → 将 detection-decision dissociation 限定为 Llama-specific observation → 修改后适合 Findings 接收。如增加语言对或因果实验则有望冲击 Conference。\n\n---\n\n## Detailed Comments\n\n### Framing 重构\n\n- 标题：加 \"English-Chinese\" 限定或改为 \"in English-Chinese Knowledge Conflicts\"\n- \"Inherit\" → \"Mirror\" 或 \"Parallel\"\n- Abstract \"demonstrate\" → \"suggest\" 或 \"observe in Llama\"\n- Contribution 3 从 \"Detection-decision layer dissociation\" 降级为 \"Llama-specific observation suggesting detection-decision dissociation\"\n\n### 统计补充\n\n- 多种子（≥3）probing 实验，报告 mean±std\n- TOST power analysis 或 Bayesian equivalence testing (BF < 1/3)\n- COMET tercile 效应量和功效分析\n- Gemma confound 分析数据补充\n\n### 讨论扩展\n\n- Qwen/Gemma steering 失败的 mechanistic 假设（非线性因果结构、attention 架构差异等）\n- 翻译模型重叠 confound 讨论\n- 跨模型样本集重叠度统计\n- 新颖性相对 Zhao et al. 2024 的明确定位\n\n### 与 Round 1 的比较\n\nRound 1 的 3 个 critical issue（Bonferroni 跨层校正、Detection≠Decision N=1、Qwen3 引用错误）中，后两者在本轮持续存在或演化（N=1 问题升级为更广泛的 framing 问题），Bonferroni 和引用错误未被本轮提出（可能已修复，需确认）。本轮新增 \"Cross-Lingual\" 标题泛化和 \"Inherit\" 因果措辞两个 critical 问题，聚焦于论文叙事层面的 claim-evidence 匹配。",
  "project": "clkc_mech_interp",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 圆桌审稿报告 — Round 2\n\n**论文**: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/写作质量)\n**流程**: Round 1 初审 + 交叉分享，一轮收敛\n\n---\n\n## Summary\n\n论文研究跨语言知识冲突在 LLM 内部表征中的 mechanistic 特征，在 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B-IT 三个模型上通过 residual stream probing 检测冲突信号，发现：(1) 三个模型均能线性检测冲突（peak accuracy 80-89%），且存在 EN→ZH 方向不对称性；(2) 该不对称性与非冲突 XNLI 任务的迁移不对称性在量级和方向上一致（CI 重叠）；(3) 仅 Llama L13 的 steering 实验产生显著因果效应，Qwen/Gemma 均为零效应。\n\n两位 Reviewer 在三个核心 Must-Fix 上完全一致，Should-Fix 层面有局部分歧（新颖性判断、遗漏引用验证）。\n\n---\n\n## Strengths\n\n1. **XNLI baseline 比较的方法论设计**：用非冲突跨语言任务作为控制条件检验不对称性的特异性，是论文最独特的方法论贡献。（R1, R2 一致）\n2. **诚实报告负面结果**：Qwen/Gemma steering 全面失败被完整报告，Gemma 高 probe accuracy + 零 steering 效应被正确解读为 informative negative。（R1, R2 一致）\n3. **Confound exclusion pipeline 系统化**：翻译质量分层 + token overlap 分析 + 非冲突 baseline 三重检查。（R1, R2 一致）\n4. **三模型比较**：一致的 detectability 和分化的 steerability 提供有价值的对比信息。（R1, R2 一致）\n5. **统计规范**：Bootstrap CI、Bonferroni 校正、效应量报告。（R1）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，双方完全共识）\n\n**MF-1** [critical] **标题 \"Cross-Lingual\" 过度泛化**\n实验仅覆盖 EN-ZH 一个语言对，但标题使用无限定的 \"Cross-Lingual\"。论文自身 Limitations 承认 \"only one language pair\"，且引用 Kargaran et al. (2024) 指出 conflict resolution preferences vary by language pair。标题是论文最重要的 claim 载体，单一语言对使用无限定泛化术语构成 overclaiming。\n- **R1**: AGREE | **R2**: 提出 → **共识**\n- 建议：标题加 \"English-Chinese\" 限定，或增加 1-2 个类型学不同的语言对。\n\n**MF-2** [critical] **\"Inherit\" 因果措辞仅有相关性证据**\n标题核心动词 \"Inherit\" 意味因果关系（冲突不对称性*因继承*通用跨语言结构而产生），但证据仅为 CI 重叠和方向一致的相关性。CI 重叠仅说明无法拒绝两者不同，不等于共享机制。论文未提供任何因果实验（如 ablation 破坏 cross-lingual alignment 后观察冲突不对称性变化）。R1 补充指出 TOST 等价检验未报告功效，进一步削弱等价声称。\n- **R1**: 强烈 AGREE（与 TOST 问题联动） | **R2**: 提出 → **共识**\n- 建议：替换为 \"Mirror\"/\"Parallel\"；补充 power analysis 或 Bayesian equivalence testing。\n\n**MF-3** [critical] **Detection-decision dissociation 仅 Llama 成立，不支持通用结论**\nSteering 仅在 Llama L13 产生显著因果效应（Fisher p = 0.002），Qwen（best p = 0.785）和 Gemma（best p = 0.418）在所有层均为零 directional flips。Abstract 使用 \"demonstrate\" 暗示通用性，且列为三大 contribution 之一。Gemma 88.9% probe accuracy 下的零效应尤其构成反证——排除 probe 质量作为 confound 后，steering 失败更可能反映方法局限性或架构依赖性。\n- **R1**: 提出 | **R2**: 提出 → **共识**（交叉中双方 AGREE）\n- 建议：Abstract/Intro 加 \"in Llama\" 限定；Contributions 列表中降级为 observation；增加 mechanistic 讨论。\n\n### Should-Fix（影响评分，存在部分分歧）\n\n**SF-1** [warning] **单种子实验设计**\n所有 probing 实验使用单一随机种子，不满足 Sellam et al. 2022 多种子标准。Bootstrap CI 仅量化采样不确定性，不覆盖训练随机性。\n- **R1**: Must-Fix 级别 | **R2**: 未单独列为 must-fix（Reproducibility 4/5）\n- 建议：至少 3-5 个种子，报告均值±标准差。\n\n**SF-2** [warning] **TOST 等价检验无 power analysis**\nSection 4.4 用 TOST 检验等价性但未报告统计功效。样本量有限时 TOST 不显著可能仅因功效不足。\n- **R1**: Must-Fix 级别 | **R2**: 同意一般性关切\n- 建议：补充 power analysis 或改用 Bayesian equivalence testing (BF < 1/3)。\n\n**SF-3** [warning] **Confound exclusion pipeline 局限性**\n(a) COMET tercile 分层每组仅 64-91 样本，功效不足以检测 2-3pp 效应；Gemma 数据未报告。(b) Llama token overlap 有 weak negative correlation (r = −0.15, p = 0.012)，仅靠 \"weak\" 定性判断不足以排除。(c) 翻译模型 Qwen3-SB 与实验对象 Qwen3-8B 同系列，可能引入 tokenization 偏好 confound。\n- **事实性澄清**：R1 交叉回应中指出 R2 将 Llama Δ=+1.7pp 误归为 Qwen，p 值也不对应论文数字。Table 2 实际为 Qwen Δ=−5.6pp, p=0.695；Llama Δ=+1.7pp, p=0.761。\n\n**SF-4** [warning] **Qwen/Gemma steering 失败缺乏 mechanistic 分析**\nGemma 88.9% probe accuracy 但 steering 零效应。论文仅结论 \"architecture-dependent\"，未讨论可能原因：非线性因果结构、residual stream 结构差异、attention pattern、layer normalization 实现差异等。\n- **R1**: AGREE | **R2**: 提出 → **共识**\n\n**SF-5** [warning] **跨模型样本自选择偏差**\n各模型用自身知识过滤样本（Llama 1368, Qwen 966, Gemma 1590），导致跨模型比较基于不同样本集。建议报告三模型样本集重叠度并在 Limitations 讨论。\n- **R1**: 提出 | **R2**: AGREE\n\n**SF-6** [warning/disputed] **新颖性相对 Zhao et al. 2024 的定位**\n- **R2**: 认为增量贡献——Zhao 已建立 probing 框架，本文主要是跨语言扩展 + 大部分失败的 steering\n- **R1**: REBUT——confound exclusion pipeline、XNLI baseline 设计、多模型比较有独立方法论价值\n- **分歧未解决**，两种判断均有道理。建议作者在 Introduction 中更明确 articulate 独特贡献。\n\n**SF-7** [warning] **遗漏相关工作**\nR2 指出遗漏 3 篇直接相关工作：Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390)、\"Steering into New Embedding Spaces\" (arXiv:2502.15639)、\"Steering Knowledge Selection Behaviours\" (arXiv:2410.15999)。R1 部分反驳，认为需先验证真实性和具体相关点。\n\n### Minor（不影响接收）\n\n1. Abstract \"confronts\" 用词不常见，建议改为 \"examines\"\n2. Figure 1 部分模型颜色在小尺寸下辨识度偏低，建议增加 marker shape 差异\n3. Table 1 注释（Δ_asym 定义）放在脚注中易被忽略，建议在正文 Section 4.3 显著提及\n4. Section 3.2 数据过滤可能引入选择偏差（只保留模型自信的知识），应在 Limitations 提及\n5. Appendix B/C 中部分关键数据考虑提升到正文\n6. 检查 arXiv preprint 引用是否已被会议接收并更新格式\n\n---\n\n## Questions for Authors\n\n1. CI 重叠能否排除冲突不对称性和 XNLI 不对称性由不同机制碰巧量级相近的可能？是否考虑过 partial correlation 或 mediation analysis？（R2）\n2. Qwen/Gemma steering 失败是否可能是 probe direction injection 方法本身在这些架构上的适用性问题？是否尝试过 Activation Addition、DAS 等替代方法？（R2）\n3. 模型间样本差异（1368/966/1590）对跨模型比较公平性的影响？（R2）\n4. 翻译模型 Qwen3-SB 与实验模型同系列的 tokenization 偏好风险？（R1, R2）\n5. 多种子实验下 peak layer 位置和不对称性量级是否稳定？（R1）\n6. Abstract 中 \"shared multilingual representations\" 和 \"detectability does not imply causal relevance\" 的逻辑衔接如何加强？（R1）\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 共识状态 |\n|------|------|----------|\n| Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390) | R2 | R1 待验证 |\n| \"Steering into New Embedding Spaces\" (arXiv:2502.15639) | R2 | R1 待验证 |\n| \"Steering Knowledge Selection Behaviours\" (arXiv:2410.15999) | R2 | R1 待验证 |\n\nRound 1 曾指出遗漏的 Meng 2022、Geiger 2024、Turner 2023、Marks 2024 在本轮未被再次提出，可能已补充。\n\n---\n\n## External Review\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：✅ 已完成（0 critical, 2 warning, 8 info）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Pages 1-4 | 连续 4 页纯文本无 display item，第一个 figure 到 page 5 才出现。建议将 Figure 1 或 pipeline 概览图前置到 page 2-3 |\n| ⚠️ warning | Page 5 | Figure 1 + Table 1 + Figure 2 三个 display item 挤在同一页，与前 4 页空旷形成不均匀节奏。建议分散到相邻页 |\n| ℹ️ info | Page 5 | Figure 1 部分模型颜色小尺寸下辨识度偏低 |\n| ℹ️ info | Page 5 | Figure 2 bar 标签字号偏小（建议 ≥8pt） |\n| ℹ️ info | Pages 5-7 | Tables 1-3 booktabs 风格规范专业 |\n| ℹ️ info | General | 无 margin 溢出、无公式渲染错误、页眉页脚符合 ACL 匿名投稿模板 |\n\n---\n\n## Overall Assessment\n\n| Reviewer | 分数 | 定位 |\n|----------|------|------|\n| R1 | 3.5 | Borderline Conference |\n| R2 | 3.0 | Findings |\n| **圆桌共识** | **3.0** | **Findings** |\n\n### 评分理由\n\n三个核心 Must-Fix 问题均为 claim-evidence 系统性不匹配，两位 Reviewer 完全一致：\n1. 标题 \"Cross-Lingual\" 泛化 vs. 单一语言对证据\n2. \"Inherit\" 因果措辞 vs. 相关性证据\n3. \"Demonstrate\" 通用结论 vs. 单模型 steering 成功\n\n这些不是表述瑕疵——它们直接影响论文的 contribution 定位和可信度。论文的方法论设计（XNLI baseline、confound exclusion pipeline、三模型比较）有独立价值，但当前 framing 将方法论优势包装为超出证据的结论。\n\n**0.5 分分歧来源**：R1 认为方法论扩展有独立价值，修复 framing + multi-seed 后可达 Conference；R2 认为即使修复，核心贡献仍为增量性（XNLI baseline 是 negative finding，steering 大部分失败）。\n\n### 修改路径\n\n收窄标题和 abstract claims → 补充多种子实验 → 增加 TOST power analysis → 将 detection-decision dissociation 限定为 Llama-specific observation → 修改后适合 Findings 接收。如增加语言对或因果实验则有望冲击 Conference。\n\n---\n\n## Detailed Comments\n\n### Framing 重构\n\n- 标题：加 \"English-Chinese\" 限定或改为 \"in English-Chinese Knowledge Conflicts\"\n- \"Inherit\" → \"Mirror\" 或 \"Parallel\"\n- Abstract \"demonstrate\" → \"suggest\" 或 \"observe in Llama\"\n- Contribution 3 从 \"Detection-decision layer dissociation\" 降级为 \"Llama-specific observation suggesting detection-decision dissociation\"\n\n### 统计补充\n\n- 多种子（≥3）probing 实验，报告 mean±std\n- TOST power analysis 或 Bayesian equivalence testing (BF < 1/3)\n- COMET tercile 效应量和功效分析\n- Gemma confound 分析数据补充\n\n### 讨论扩展\n\n- Qwen/Gemma steering 失败的 mechanistic 假设（非线性因果结构、attention 架构差异等）\n- 翻译模型重叠 confound 讨论\n- 跨模型样本集重叠度统计\n- 新颖性相对 Zhao et al. 2024 的明确定位\n\n### 与 Round 1 的比较\n\nRound 1 的 3 个 critical issue（Bonferroni 跨层校正、Detection≠Decision N=1、Qwen3 引用错误）中，后两者在本轮持续存在或演化（N=1 问题升级为更广泛的 framing 问题），Bonferroni 和引用错误未被本轮提出（可能已修复，需确认）。本轮新增 \"Cross-Lingual\" 标题泛化和 \"Inherit\" 因果措辞两个 critical 问题，聚焦于论文叙事层面的 claim-evidence 匹配。",
    "project": "clkc_mech_interp",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-24T16:49:41.702601+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6951eb3869a0070e3ae607ab60c90dad:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4669
}
```

</details>

---


### Assistant

_source line 208 · 2026-05-24T16:49:48.965062+00:00_

Round 2 审稿报告已投递。

**圆桌共识：3.0 / 5 (Findings)**

三个 Must-Fix 双方完全一致：
1. "Cross-Lingual" 标题泛化（仅 EN-ZH）
2. "Inherit" 因果措辞无因果证据
3. Detection-decision dissociation 仅 Llama 成立却推广为通用结论

R1 给 3.5（认为方法论有独立价值），R2 给 3.0（认为增量贡献）。分歧在新颖性判断，0.5 分差距。修改路径：收窄 framing + 多种子 + power analysis → Findings 可接收；增加语言对或因果实验 → 有望 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 209 · 2026-05-24T16:49:48.969564+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

## Must-Fix 问题回应

### [REBUT] R1-M1: 单种子设计不满足当前 probing 标准

Reviewer 1 的多种子要求对**神经网络 probe 完全正确**，但本文使用的是 **ℓ₁-regularized logistic regression**（Section 3.3, p3: "we train an ℓ₁-regularized logistic regression probe (Belinkov, 2022; Hewitt and Liang, 2019)"）。Logistic regression 是凸优化问题，给定相同数据其解唯一，不依赖随机初始化——Sellam et al. 2022 和 Dodge et al. 2020 的多种子标准针对的是非凸神经网络微调，不直接适用于凸 probe。

**但有一个 Reviewer 1 未明确指出但确实存在的相关问题**：论文使用单一 80/20 split（Section 3.2），bootstrap 覆盖的是给定 split 上的采样不确定性，不覆盖 split 本身的随机性。对凸 probe，正确的做法是 k-fold cross-validation 或多次 random split，而非多随机种子。这是一个 mild concern（不是 Must-Fix），因为 2000 次 bootstrap 已经提供了合理的 CI，且凸 probe 在同一 split 上结果稳定。

**结论**：M1 的诊断方向偏移——问题不在 "种子" 而在 "split"，且对凸 probe 的严重程度低于 Reviewer 1 的评估。建议降级为 Should-Fix。

---

### [AGREE] R1-M2: TOST 等价检验无功效却做了等价结论

完全同意。论文 Section 4.4 (p5) 明确使用了 TOST（±2 pp margin）并**自行承认功效不足**："Formal TOST equivalence tests (±2 pp margin) were non-significant for all three models (Llama p = 0.41, Qwen p = 0.366, Gemma p = 0.377), reflecting insufficient power (SE ≈ 4.37 pp) rather than meaningful differences."

这使得问题更加严重：论文明知 TOST 功效不足，却仍以 "point estimates fall within ±1.3 pp" 和 CI 重叠为依据推出 "the asymmetry thus reflects a general cross-lingual property" 的结论，并在标题中使用 "Inherit" 这一因果措辞。**自我承认统计证据不足后仍做等价声称，构成比简单遗漏更严重的方法论问题。**

我在自己的审稿中将此问题归入 N2（"Inherit" 因果措辞缺乏因果证据），Reviewer 1 的 M2 从统计检验角度提供了更精确的技术诊断。两者互补，共同构成 Must-Fix。

Reviewer 1 建议 Bayesian equivalence testing (BF < 1/3) 是合理的替代方案。

---

### [AGREE] R1-M3: 因果发现仅 1/3 模型成立但被列为主要贡献

完全同意，与我的 N3 一致。Detection-decision dissociation 仅在 Llama L13 成立（Fisher p = 0.002），Qwen (best p = 0.785) 和 Gemma (best p = 0.418) 均 zero directional flips。Abstract 的 "These findings demonstrate..." 和 contributions 列表将此作为通用发现是 overclaiming。

补充一点 Reviewer 1 未展开的角度：Qwen/Gemma 的 steering 全面失败也意味着我们**无法区分**这两个模型是 (a) 不存在 detection-decision dissociation，还是 (b) 存在 dissociation 但 probe-based steering 方法对这些架构无效。论文将 Gemma 解读为 "informative negative" (p7)，但实际上这个 negative 有两种不同的解释，论文只讨论了一种。

---

## Should-Fix 问题回应

### [AGREE] R1-S1: Gemma confound 分析数据缺失

确认 Table 2 (p6) 仅报告 Qwen 和 Llama 的 COMET tercile 和 token overlap 数据，Gemma 完全缺失。三个模型中 Gemma 的 probe accuracy 最高 (88.9%)，恰恰是最需要排除 confound 的模型。数据缺失无正当理由。

---

### [AGREE] R1-S2: Tercile 分析功效不足

同意。每个 tercile ~300-500 样本检测 2-3 pp 效应确实可能功效不足。Llama 的 COMET tercile Δ = +1.7 pp (p = 0.063) 和 Qwen 的 Δ = -1.7 pp (p = 0.061) 都在边界附近——这恰好说明样本量可能刚好不够检测到真实效应。用连续变量回归而非三等分会更稳健。

---

### [AGREE] R1-S3: 跨模型样本自选择偏差

同意，我在 Questions for Authors (Q3) 中也提出了同一问题。Llama 1368 / Qwen 966 / Gemma 1590 是各模型自身知识过滤后的不同子集，跨模型比较的可比性受到威胁。理想方案是取三个模型都能正确回答的交集子集做额外分析。

---

### [REBUT] R1-S4: Abstract 内部一致性——逻辑跳跃

不同意 Reviewer 1 对此的判断。Abstract 的两个核心发现在逻辑上是兼容且互补的：

1. "inheriting from the model's general multilingual structure rather than conflict-specific encoding" → 关于不对称性信号的**性质**（结构性的，非冲突特异的）
2. "linear detectability does not imply causal relevance" → 关于 detection 的**功能局限**（可检测不等于可操控）

这不是逻辑矛盾或跳跃，而是两个不同维度的发现：(1) 说 "什么"，(2) 说 "然后怎样"。可以同时成立：冲突信号的跨语言不对称性继承自通用结构（性质），且即使信号可检测也不能通过 steering 因果地影响决策（功能）。

**但 Reviewer 1 的直觉有合理内核**：Abstract 在这两个发现之间缺少一句过渡性解释来连接逻辑链。读者需要自行推断两者的关系。建议作者在 Abstract 中加一句桥接（如 "Beyond the nature of the asymmetry, we further examine whether detected signals carry causal weight"），但这属于写作润色而非逻辑缺陷。

---

### [REBUT] R1-S5: 因果边界 "gradient" 的统计验证不充分

部分不同意。Appendix B (p9, Table 4) 提供了独立的 causal boundary replication：使用独立样本 (N = 201) 和独立随机采样，扫描了 Llama 从 L10 到 L28 共 6 个层，确认 L13 显著 (p < 0.001) 且 L12 仍显著 (p = 0.0003)，而邻近层（L10, L18, L28）均不显著或 Bonferroni 后消失。这已经构成了合理的 boundary delineation。

主文 Table 3 (p7) 也在多个 depth 上测试了所有三个模型的 steering 效果。综合主文 + Appendix 的层扫描，验证的系统性在 probing 文献中属于合理水平。Reviewer 1 要求 "更系统的层扫描" 具体需要什么级别，没有明确——如果是每一层都扫描，那需要极大的 Bonferroni 校正代价。

**但我同意**一个相关点：论文声称 L13 是 "remarkably narrow causal window" (p6)，这个修饰语（"remarkably"）需要与其他 causal intervention 文献的 window 宽度对比才能成立，论文未提供这个对比。

---

### [AGREE] R1-S6: Gemma 不对称性对称点讨论缺失

同意。Table 1 显示 Gemma Δ_asym 接近 0（EN→ZH 和 ZH→EN 准确率几乎相同），而 Llama 和 Qwen 都有 ~7 pp 的 ZH→EN 优势。这是一个值得讨论的跨架构差异——Gemma 的对称性可能反映了其训练数据中英中分布更均衡，或其内部 representation alignment 机制不同。论文提及 Kargaran et al. (2024) 的 "conflict resolution preferences vary by language pair" 但未将其应用到解释 Gemma 的对称性。

---

## 分歧总结

| 条目 | 我的判断 | 与 R1 的差异 | 理由 |
|------|----------|------------|------|
| M1 | Should-Fix (非 Must-Fix) | 降级 | 凸 probe 不需要多种子；问题在 split 不在 seed |
| M2 | Must-Fix | 完全一致 | 自认功效不足仍做等价声称 |
| M3 | Must-Fix | 完全一致 | 与我的 N3 一致 |
| S1 | Should-Fix | 一致 | — |
| S2 | Should-Fix | 一致 | — |
| S3 | Should-Fix | 一致 | — |
| S4 | Minor (非 Should-Fix) | 降级 | 逻辑兼容但缺过渡句，是写作问题非逻辑问题 |
| S5 | Minor (非 Should-Fix) | 降级 | Appendix B 已提供合理层扫描 |
| S6 | Should-Fix | 一致 | — |

**关于 Overall Assessment**：Reviewer 1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差异主要来自我对新颖性的更严格评估——我认为单语言对的跨语言扩展 + 核心 XNLI 结论是 negative finding + steering 2/3 失败，整体增量贡献不足以支撑 Borderline Conference。Reviewer 1 可能更看重方法论管线（confound exclusion + boundary replication）的价值。我认为方法论管线有价值但不足以弥补 claim-evidence 的系统性不匹配。


---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

核心分歧点：
- **M1 降级**：凸 probe (logistic regression) 的解唯一，多种子要求不适用，问题在 data split 而非 seed，严重程度应为 Should-Fix
- **S4 降级**：Abstract 两个发现逻辑兼容（信号性质 vs. 功能局限），缺的是过渡句而非逻辑一致性
- **S5 降级**：Appendix B 已提供独立层扫描验证 (L10-L28, N=201)，验证系统性合理
- **Overall 分差**：我给 3.0 (Findings) vs R1 的 3.5 (Borderline Conference)，主要因为我对新颖性评估更严格——单语言对 + negative XNLI 结论 + 2/3 steering 失败的增量贡献不足以支撑 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 210 · 2026-05-24T16:50:32.735327+00:00_

Reviewer 2 的详细交叉回应已收到。审稿报告已在此前提交，核查 R2 交叉回应是否影响报告结论：

**R2 的关键 rebuttal：**

1. **M1（单种子）降级为 Should-Fix** — R2 指出论文使用的是凸优化的 ℓ₁-regularized logistic regression，解唯一，Sellam/Dodge 的多种子标准针对非凸神经网络不直接适用。问题在 data split 而非 seed。→ 报告中已将此项定为 SF-1 (Should-Fix)，与 R2 立场一致。

2. **S4（Abstract 逻辑）降级为 Minor** — R2 认为两个发现逻辑兼容（信号性质 vs. 功能局限），缺过渡句不是逻辑缺陷。→ 报告未将此列为独立 Should-Fix。

3. **S5（因果边界验证）降级为 Minor** — Appendix B 已提供独立层扫描 (L10-L28, N=201)。→ 报告未将此列为独立 Should-Fix。

4. **M2、M3 完全 AGREE** — 与报告一致。

**结论**：R2 的交叉回应与已提交报告的定位一致——3 个 Must-Fix 共识不变，SF-1 单种子问题已正确定为 Should-Fix 而非 Must-Fix。报告无需修订。

R2 补充了一个有价值的技术细节：凸 probe 的正确改进方向是 k-fold cross-validation 或多次 random split，而非多随机种子。此细节记录于此供 Research Director 参考。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 17

## Round 17

78 recorded events


### User

_source line 211 · 2026-05-25T04:15:52.096451+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: clkc_mech_interp
- 论文路径: projects/clkc_mech_interp/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-25T04:15:58.641989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-25T04:15:58.692980+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-25T04:16:02.358061+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-25T04:16:02.358493+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-25T04:16:08.749817+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-25T04:16:08.750285+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-25T04:16:11.953578+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-25T04:16:12.405982+00:00_

{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (78 个)\n\n- **comet_qwen_v6**: DONE (killed) — \n- **gemma_en_act_102**: DONE (success) — \n- **xnli_baseline_110**: DONE (negative) — \n- **comet_llama_v5**: DONE (killed) — \n- **comet_qwen_v5**: DONE (killed) — \n- **mvp_probe_llama_v1**: DONE (success) — \n- **mvp_probe_v1**: DONE (success) — \n- **comet_llama_v4**: PREPARING (killed) — \n- **comet_llama_v3**: PREPARING (killed) — \n- **comet_llama_v2**: PREPARING (killed) — \n- **comet_llama**: PREPARING (killed) — \n- **comet_qwen_v4**: PREPARING (killed) — \n- **comet_qwen_v3**: PREPARING (killed) — \n- **comet_qwen_v2**: PREPARING (killed) — \n- **comet_qwen**: PREPARING (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- gemma-steering-pickup（准备中）\n- llama31_en_activations（准备中）\n- qwen3_translate_zh（准备中）\n- collect_en_activations_qwen3_8b（准备中）\n- collect_en_activations_llama_v2（准备中）\n- translate_zh_llama_v2（准备中）\n- translate_zh_qwen（准备中）\n- collect_en_act_llama_v3（准备中）\n- collect_en_act_qwen_v2（准备中）\n- verify_qwen3_v2（准备中）\n- …另有 16 项\n\n## 近期结论\n- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L13_133** (negative): Qwen3-8B-Instruct L13 (36% depth) probe direction causally influences conflict resolution with matched-condition data (N≈200, high probe acc). L13 = L14 peak - 1, establishi
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-25T04:16:12.457277+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "memory.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "memory.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-25T04:16:12.559261+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md\", \"content\": \"# 关键研究发现\\n\\n## Causal Gradient Profile — 完整 6 层同条件数据 [2026-05-24]\\n\\n**核心发现**：同条件实验（N=201, probe acc ~85-92%）绘制出完整的因果梯度。Steering 效应 peak at L13，向深层平滑衰减，L28（detection peak）完全无效。\\n\\n| Layer | Depth | Probe Acc | Best α | Fisher p | Bonferroni sig | 效应 |\\n|-------|-------|-----------|--------|----------|----------------|------|\\n| L12 | 38% | 91.75% | +20 | 0.0853 | 0/6 ❌ | — |\\n| **L13** | **41%** | **90.00%** | **+10** | **0.0003** | **2/6** ✅✅ | **peak** |\\n| **L14** | **44%** | **91.75%** | **+10** | **0.0022** | **1/6** ✅ | strong |\\n| **L16** | **50%** | **91.50%** | **+10** | **0.005** | **1/6** ✅ | moderate |\\n| L18 | 56% | 90.75% | +5 | 0.0099 | 0/6 ❌ | marginal (差0.0016) |\\n| L28 | 88% | 85.25% | +10 | 0.284 | 0/6 ❌ | none |\\n\\n**Causal window = L13-L16（3层显著）**，L18 marginal，L12/L28 negative。窗口占 32 层模型的 ~12.5%。\\n\\n**p 值单调递增梯度**：0.0003 → 0.0022 → 0.005 → 0.0099 → 0.284。连续衰减而非 on/off。\\n\\n**Detection ≠ Decision 最终验证**：L28 是 detection peak（probe acc 最高），但 steering best p=0.284，完全无因果效应。高质量 probe 条件下解离依然稳健。\\n\\n**仅正向 α 有效**：所有显著效应来自 +5/+10，负向 α 全不显著。\\n\\n**L13 复现更强**：原始 p=0.0009 (N=136, 1α sig) → 新数据 p=0.0003 (N=201, 2α sig)。\\n\\n---\\n\\n## C2 不对称性非冲突特有 [2026-05-22, xnli_baseline_110]\\n\\n**核心发现**：~6pp ZH→EN > EN→ZH 不对称性在非冲突任务 XNLI 上同样存在，是模型的一般性跨语言属性，非冲突信号特有。\\n\\n| Model | XNLI asymmetry | Conflict asymmetry |\\n|-------|---------------|-------------------|\\n| Qwen | +6.72pp CI[2.36,11.73] ✓ | +5.95pp CI[-3.67,14.81] |\\n| Llama | +5.97pp CI[0.92,11.33] ✓ | +11.76pp CI[4.29,19.57] ✓ |\\n\\n**推导**：英语主导预训练 → EN 表征空间更\\\"标准\\\" → ZH→EN 迁移天然更好。C2 需 reframe：从 \\\"conflict-specific asymmetry\\\" 改为 \\\"conflict signals share general cross-lingual transfer pathways\\\"。\\n\\n---\\n\\n## Steering 因果效应是 Llama-specific [2026-05-22, 更新 2026-05-24]\\n\\n**核心发现**：Probe weight 方向的因果效应具有强模型特异性——仅 Llama L13-L16 
…[truncated 2638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-25T04:16:19.289999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-25T04:16:20.042670+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\title{English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	\input{experiments}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\input{limitations}
42	
43	\appendix
44	
45	\section{Use of AI Assistants}
46	\label{app:ai-assistants}
47	
48	We used Claude (Anthropic) as an AI coding and writing assistant
49	throughout this work. Specifically:
50	\begin{itemize}
51	    \item \textbf{Code:} drafting experiment scripts, data-processing
52	    pipelines, and analysis utilities; debugging and refactoring.
53	    \item \textbf{Writing:} drafting and revising paper sections,
54	    polishing prose, and reformatting \LaTeX{}.
55	    \item \textbf{Literature:} summarizing related papers to inform
56	    related-work section.
57	\end{itemize}
58	
59	\section{Fine-Grained Causal Boundary Analysis}
60	\label{app:boundary}
61	
62	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
63	
64	\begin{table}[h]
65	\centering
66	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
67	\label{tab:boundary}
68	\small
69	\resizebox{\columnwidth}{!}{%
70	\begin{tabular}{lcccccc}
71	\toprule
72
…[truncated 547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-25T04:16:20.094034+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-25T04:16:20.596402+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-25T04:16:26.119806+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission deadline author guidelines site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, I found some relevant information about EMNLP 2026, though the main call for papers fo
…[truncated 1351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 6025
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-25T04:16:26.922981+00:00_

Web search results for query: ""ACL Rolling Review" 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here is information about ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pa
…[truncated 969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 6326
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-25T04:16:32.396992+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the following for 2026: 1) All upcoming ARR submission deadlines (month/year cycles), 2) Page limits for long and short papers, 3) Format/template requirements, 4) Anonymity rules (double-blind?), 5) Appendix rules, 6) Any special requirements for EMNLP 2026 commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the following for 2026: 1) All upcoming ARR submission deadlines (month/year cycles), 2) Page limits for long and short papers, 3) Format/template requirements, 4) Anonymity rules (double-blind?), 5) Appendix rules, 6) Any special requirements for EMNLP 2026 commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-25T04:16:33.861300+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR reviewed paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR reviewed paper"
  }
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-25T04:16:34.614189+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "decisions.yaml",
  "max_chars": "4000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "decisions.yaml",
    "max_chars": "4000"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-25T04:16:37.425292+00:00_

# ARR 2026 Key Information

## 1) Upcoming Submission Deadlines
The document states ARR has "deadlines every two months" but does not specify the actual 2026 dates. You'll need to check the [Dates & Venues page](https://aclrollingreview.org/dates) for the specific 2026 cycle deadlines.

## 2) Page Limits
- **Long papers:** "up to eight (8) pages of content" plus unlimited references and limitations section
- **Short papers:** "up to four (4) pages of content" plus unlimited references and limitations section

## 3) Format/Template Requirements
Papers must use "the official ACL style template" available at the ACL GitHub repository and follow ACL author guidelines. The document specifies that "submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be rejected without review."

## 4) Anonymity Rules
ARR uses a two-way anonymized review system: "Papers must not include authors' names and affiliations." Self-citations must be rephrased (e.g., "Smith previously showed..." rather than "We previously showed..."). Supplementary materials must also be anonymized.

## 5) Appendix Rules
"Appendices should come after the references in the submitted pdf. They do not count towards the page limit" and must follow double-column formatting. Key technical content should appear in the main paper, not appendices.

## 6) EMNLP 2026 Commitment Deadline
The document does not provide specific information about EMNLP 2026 commitment deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebFetch",
  "elapsed_ms": 5028
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-25T04:16:38.128415+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR reviewed paper"

Links: [{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is the information about EMNLP 2026's commitment deadline for ARR-reviewed papers:

The EMNLP commitment deadline is August 2, 2026. This is the date by
…[truncated 498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 4267
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-25T04:16:38.129167+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/decisions.yaml\", \"content\": \"_next_id: 21\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 12:00 UTC\\n  summary: MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性\\n  rationale: Track 1（探针迁移）是整个 3-track 研究的基础前提。如果残差流中无法检测冲突信号或跨语言完全不迁移，后续 SAE 分析和 steering\\n    均无意义。选 Qwen3-8B-Instruct 因 Qwen-Scope 提供 base SAE 便于后续 Track 2。选 EN+ZH 因语系距离大，若迁移成功则信号强。ConflictQA\\n    公开可用，无需等 CLEAR 数据。Pass/fail 标准参考 Brink et al. 单语 0.96 F1 和 Zhao et al. ~90% 探针精度。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 12:06 UTC\\n  summary: 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% conditional pass 定义、layer-wise\\n    量化标准、统计显著性要求（binomial p<0.01）、翻译 COMET gate（≥0.80）、FAIL→retry Llama 行动路径\\n  rationale: Reviewer 指出原 gate criteria 存在 ambiguous zone（70-79% 无定义）、layer-wise pattern\\n    逃逸条款过于模糊、ZH 60% 阈值缺统计锚定、翻译质量是迁移失败的混淆因素、FAIL 后行动未定义。全部采纳以确保 MVP 结论可靠。FAIL→retry\\n    on Llama 给予一次排除模型特异性的机会，两模型均 FAIL 才 kill。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 14:26 UTC\\n  summary: 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集\\n  rationale: Llama verify 保留率仅 33%（266/800 train），低于 300 阈值。ConflictQA 有 ~10K 条，扩至\\n    2000 可保证两模型各自 ≥300 有效样本。取消交集策略因为强制交集会进一步损失样本量，且跨模型对比不要求相同样本——各自 verified 集上报告相同指标即可，交集作为补充分析。20%\\n    标签翻转率确认了 M001 verify 步骤的必要性。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: triggered_decision\\n    result: verify 保留率 33%, 266 train / 70 test, 20% flip\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-21 19:17 UTC\\n  summary: Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨语言迁移不对称（ZH→EN 71.3% vs\\n    EN→ZH 59.6%），等 Qwen 结果做最终 verdict\\n  rationale: Llama 4 方向探针结果显示冲突信号可线性检测（所有方向 p < 0.01），但 EN→EN 未达 80% PASS 阈值（77.6%）。跨语言迁移存在但高度不对称：ZH→EN\\n    强迁移（71.3%），EN→ZH 弱迁移（59.6%，刚好低于 60% point 阈值但 p=9.7e-4 仍显著）。CONDITIONAL PASS 按\\n    D002 规则进入 EXTEND 评估。等 Qwen 跨模型
…[truncated 2467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3514
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-25T04:16:44.305303+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract: 1) ARR submission deadline for EMNLP 2026, 2) Commitment deadline, 3) Page limits for long/short papers, 4) Template requirements, 5) Anonymity/double-blind rules, 6) Appendix rules, 7) Notification dates, 8) Any special formatting requirements, 9) Conference dates and location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract: 1) ARR submission deadline for EMNLP 2026, 2) Commitment deadline, 3) Page limits for long/short papers, 4) Template requirements, 5) Anonymity/double-blind rules, 6) Appendix rules, 7) Notification dates, 8) Any special formatting requirements, 9) Conference dates and location"
  }
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-25T04:16:46.320069+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract all ARR 2026 submission cycle deadlines (May, July, etc.) and their corresponding review/meta-review release dates. List each cycle with its submission deadline date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Extract all ARR 2026 submission cycle deadlines (May, July, etc.) and their corresponding review/meta-review release dates. List each cycle with its submission deadline date."
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-25T04:16:48.957842+00:00_

# EMNLP 2026 Submission Guidelines Summary

**1) ARR Submission Deadline**
"May 25, 2026" for long and short papers via ACL Rolling Review.

**2) Commitment Deadline**
"August 2, 2026" to commit reviewed articles to EMNLP 2026.

**3) Page Limits**
Long papers: 8 pages (up to 9 in final versions); short papers: 4 pages (up to 5 in final versions).

**4) Template Requirements**
The page references "ARR submission requirements" but directs authors to the ACL Rolling Review website for specific template details and formatting instructions.

**5) Anonymity/Double-Blind Rules**
The reviewing process maintains double-blindness: "Reviewers will not see authors, nor will authors see reviewers." However, there is no anonymity period requirement per ACL and ARR policies.

**6) Appendix Rules**
The document mentions "Optional Supplementary Materials (appendices, software and data)" but specific restrictions are contained in the linked ARR guidelines, not detailed here.

**7) Notification Dates**
Acceptance notification: "August 20, 2026"; camera-ready deadline: "September 20, 2026."

**8) Special Formatting Requirements**
The page directs readers to ARR's full submission guidelines for detailed formatting specifications.

**9) Conference Dates and Location**
"October 24 - 29, 2026" with location details not specified in this document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebFetch",
  "elapsed_ms": 4652
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-25T04:16:49.409963+00:00_

# ARR 2026 Submission Cycles and Deadlines

Based on the provided content, here are the ARR 2026 cycles with submission deadlines and corresponding review/meta-review dates:

**March 2026 Cycle**
- Submission: March 16
- Reviews due: April 20
- Meta-reviews release: May 21

**May 2026 Cycle**
- Submission: May 25
- Reviews due: June 29
- Meta-reviews release: July 30

**August 2026 Cycle**
- Submission: August 3
- Reviews due: TBA
- Meta-reviews release: TBA

**October 2026 Cycle**
- Submission: October 12
- Reviews due: TBA
- Meta-reviews release: TBA

The document notes that "in addition to submission and author response dates, the following action points are now listed, as non-compliance may result in desk rejection or sanctions," including reviewer registration deadlines for all authors and review submission deadlines with potential consequences for non-compliance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebFetch",
  "elapsed_ms": 3089
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-25T04:16:59.603119+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_checklist.yaml",
  "max_chars": "4000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "paper_checklist.yaml",
    "max_chars": "4000"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-25T04:17:00.959243+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'clkc_mech_interp'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-25T04:17:00.959689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-25T04:17:01.514640+00:00_

1	When multilingual large language models (LLMs) encounter conflicting information across languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry is consistent with the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals, mirroring the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-25T04:17:01.515028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-25T04:17:01.766233+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{brink2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe ac
…[truncated 4607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-25T04:17:01.766599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-25T04:17:01.817072+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, \citet{brink2026probing} localized factual associations via probing, \citet{pham2026where} traced intra-memory conflict pathways, and \citet{li2025taming} proposed conflict mitigation methods.
7	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
8	
9	\paragraph{Cross-lingual representations in multilingual models.}
10	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
11	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
12	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
13	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR cross-lingual conflict benchmark), and \citet{ifergan2024beneath, xing2024evaluating}; our work provides a mechanistic account of why such asymmetries arise.
14	
15	\paragraph{Representation steering and causal intervention.}
16	\citet{li2023iti} introduced Inferenc
…[truncated 1506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-25T04:17:05.538006+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-25T04:17:06.041214+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our pipeline proceeds from data construction through probing and steering, formalized below.
5	
6	\subsection{Task Formulation}
7	\label{sec:task}
8	
9	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
10	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
11	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
12	
13	\subsection{Data Construction}
14	\label{sec:data}
15	
16	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
17	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2025qwen3}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
18	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET (Crosslingual Optimized Metric for Evaluation of Translation; \citet{rei2020comet}) back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
19	
20	\subsection{Activation Extraction and Probing}
21	\label{sec:extraction}
22	
23	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
24	We record the model's answer and assign bin
…[truncated 3020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-25T04:17:06.092102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-25T04:17:06.545186+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	The three models were independently verified, yielding only 3.5\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\% (Llama $\cap$ Gemma) to 24.8\% (Gemma $\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.
14	
15	\paragraph{Translation.}
16	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
17	
18	\paragraph{Probing.}
19	For each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
20	We report balanced accuracy to account for class imbalance.
21	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
22	All activation extraction and steering exp
…[truncated 15405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-25T04:17:06.595997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-25T04:17:06.998017+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Causal influence is localized to L13 regardless of detection peak.}
5	In Llama, causal influence is consistently localized to layer~13 (41\% depth; Fisher $p = 0.002$), regardless of where detection accuracy peaks: EN$\to$EN detection peaks at L28 (88\% depth) while ZH$\to$ZH peaks at L13 itself, yet causal influence is found only at L13 in both cases, with all late-layer interventions producing no significant behavioral change ($p > 0.3$).
6	This layer coincides with the site of cross-lingual alignment identified in prior work \citep{muller2021first, wendler2024llamas}, suggesting that mid-layers serve a dual role in alignment and conflict resolution.
7	The detection signal at later layers is best understood as a diagnostic readout of a decision already made upstream.
8	A practical implication follows: intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site; cross-layer sweeps are necessary.
9	Steering failed in both Qwen (L14, 39\%; $n = 131$, best $p = 0.785$) and Gemma (L17, 40\%; $n = 171$, best $p = 0.448$), with zero directional flips in both cases.
10	The Gemma result is particularly informative: its 88.9\% probe accuracy, the highest among all three models, rules out probe quality as a confound, since the direction that best separates conflict labels carries no causal influence despite being highly discriminative.
11	This establishes that the causal influence of the probe direction is architecture-dependent, not a general property of mid-layer computation.
12	
13	\paragraph{Why does steering fail in Qwen and Gemma?}
14	Three mechanistic hypotheses merit consideration.
15	First, the causal pathway may be non-linear: the probe direction captures the dominant linear component of the conflict signal, but the actual causal structure may involve non-linear interactions that single-direction perturbation cannot address \citep{elhage2022toy}.

…[truncated 3728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-25T04:17:07.048824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-25T04:17:07.099557+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that knowledge conflict signals in multilingual LLMs are linearly detectable across languages (balanced accuracies 75.0--77.6\% within-language, all cross-lingual transfers above chance at $p < 0.001$) and that the transfer asymmetry (ZH$\to$EN exceeding EN$\to$ZH by ${\sim}$6--7~pp) is consistent with the XNLI non-conflict baseline across all three architectures, reflecting general cross-lingual structure rather than conflict-specific encoding.
5	
6	In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\% depth; Fisher $p = 0.002$) regardless of where detection accuracy peaks, and all late-layer interventions fail.
7	Linear detectability is neither sufficient nor predictive of causal relevance; cross-layer sweeps are necessary to identify the computationally relevant site.
8	
9	Steering failed in both Qwen and Gemma despite Gemma's 88.9\% probe accuracy, confirming that the causal influence of the probe direction is architecture-specific.
10	Future work should explore alternative intervention methods, diverse language pairs, and sparse autoencoder decomposition.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-25T04:17:07.702246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-25T04:17:07.803084+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.
6	Typologically diverse language pairs and alternative intervention methods are needed to assess generality.
7	Second, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, which retains only questions where the model confidently knows the ground truth and may bias toward well-represented knowledge; additionally, Qwen3-8B serves as both the translation model and an experimental subject, though COMET-based quality control and Llama/Gemma cross-validation mitigate this dual-role concern.
8	Third, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; while peak balanced accuracy remains stable across seeds (Llama $\pm$0.12\%, Gemma $\pm$1.32\%, Qwen $\pm$1.90\%), the specific peak layer can shift, and future work should verify stability across larger datasets to improve statistical power for stratified comparisons such as the COMET tercile ablation.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-25T04:17:21.557348+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-25T04:17:21.557789+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-25T04:17:25.374038+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/clkc_mech_interp/agent/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/clkc_mech_interp/agent/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-prod42"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-25T04:17:26.278012+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-25T04:17:26.481062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "offset": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "offset": "80"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-25T04:17:26.481445+00:00_

80	\bottomrule
81	\end{tabular}%
82	}
83	\end{table}
84	
85	\section{Seed Replication of L13 Steering}
86	\label{app:seed_replication}
87	
88	To verify that the L13 causal effect is not an artifact of a specific train/test split, we repeated the Llama L13 steering experiment with an independently trained probe (seed=123, different train/test split).
89	The causal effect fully replicates: $\alpha = +5$ ($p = 0.002$), $\alpha = +10$ ($p = 0.0005$), $\alpha = -10$ ($p = 0.0003$), $\alpha = +20$ ($p = 0.004$), with 4 of 6 configurations surviving Bonferroni correction (vs.\ 2/6 in the original).
90	The consistent positive-direction effect across independent probe training confirms that L13 causal localization is not an artifact of a specific train/test split.
91	
92	\section{Matched-Condition Steering Results}
93	\label{app:steering_config}
94	
95	Table~\ref{tab:steering_config} reports steering results under matched conditions: all three architectures are tested at comparable relative depths (${\sim}$36--43\%) using the same probe training methodology and six $\alpha$ values in $[-20, +20]$.
96	Despite the highest probe accuracy among the three models (88--89\%), Gemma produces zero directional flips, ruling out probe quality as a confound for the Llama-specific positive result.
97	The full Llama causal gradient ($N = 201$) is in Appendix~\ref{app:boundary}.
98	
99	\begin{table}[h]
100	\centering
101	\caption{Matched-condition steering results. Probe: EN$\to$EN balanced accuracy at the target layer. Best $p$: minimum Fisher exact $p$-value across six tested $\alpha$ values. Bonf.: $\alpha$ values surviving Bonferroni correction out of 6. Flips: total directional transitions (p$\to$c $+$ c$\to$p).$^{\dagger}$}
102	\label{tab:steering_config}
103	\small
104	\begin{tabular}{lcrccc}
105	\toprule
106	Layer & Depth & Probe (\%) & Best $p$ & Bonf. & Flips \\
107	\midrule
108	\multicolumn{6}{l}{\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\
109	\textbf{L13} & \textb
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-25T04:17:29.796479+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/clkc_mech_interp/**/config*",
  "path": "/home/ubuntu/.agent-ml-research-prod42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/clkc_mech_interp/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-prod42"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-25T04:17:29.947637+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pygments/lexers/configs.py
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pygments/lexers/__pycache__/configs.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pyarrow/config.pxi
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/config.h
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/python/config.h
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/util/config.h
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pyarrow/src/arrow/python/config.cc
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/python3.14/site-packages/pyarrow/src/arrow/python/config.h
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/.venv/lib/p
…[truncated 14703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-25T04:17:34.717306+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-25T04:17:35.269752+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-25T04:17:35.721874+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-prod42",
  "glob": "*/project_config*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-prod42",
    "glob": "*/project_config*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-25T04:17:35.873199+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-25T04:17:38.435040+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-prod42",
  "glob": "*.yaml",
  "output_mode": "files_with_matches",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-prod42",
    "glob": "*.yaml",
    "output_mode": "files_with_matches",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-25T04:17:38.536001+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-25T04:17:41.250031+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-prod42",
  "glob": "*.{yaml,yml,json,toml}",
  "output_mode": "files_with_matches",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-prod42",
    "glob": "*.{yaml,yml,json,toml}",
    "output_mode": "files_with_matches",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-25T04:17:41.452719+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-25T04:17:45.823491+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-25T04:17:46.024788+00:00_

{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (78 个)\n\n- **comet_qwen_v6**: DONE (killed) — \n- **gemma_en_act_102**: DONE (success) — \n- **xnli_baseline_110**: DONE (negative) — \n- **comet_llama_v5**: DONE (killed) — \n- **comet_qwen_v5**: DONE (killed) — \n- **mvp_probe_llama_v1**: DONE (success) — \n- **mvp_probe_v1**: DONE (success) — \n- **comet_llama_v4**: PREPARING (killed) — \n- **comet_llama_v3**: PREPARING (killed) — \n- **comet_llama_v2**: PREPARING (killed) — \n- **comet_llama**: PREPARING (killed) — \n- **comet_qwen_v4**: PREPARING (killed) — \n- **comet_qwen_v3**: PREPARING (killed) — \n- **comet_qwen_v2**: PREPARING (killed) — \n- **comet_qwen**: PREPARING (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- gemma-steering-pickup（准备中）\n- llama31_en_activations（准备中）\n- qwen3_translate_zh（准备中）\n- collect_en_activations_qwen3_8b（准备中）\n- collect_en_activations_llama_v2（准备中）\n- translate_zh_llama_v2（准备中）\n- translate_zh_qwen（准备中）\n- collect_en_act_llama_v3（准备中）\n- collect_en_act_qwen_v2（准备中）\n- verify_qwen3_v2（准备中）\n- …另有 16 项\n\n## 近期结论\n- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L13_133** (negative): Qwen3-8B-Instruct L13 (36% depth) probe direction causally influences conflict resolution with matched-condition data (N≈200, high probe acc). L13 = L14 peak - 1, establishi
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-25T04:17:53.312816+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" 2>/dev/null | grep -v '.venv' | grep -v '__pycache__' | head -30",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" 2>/dev/null | grep -v '.venv' | grep -v '__pycache__' | head -30",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-25T04:17:53.515051+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/wendler2024llamas.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/rei2020comet.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/li2023iti.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/conneau2018xnli.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/kialy2026universal.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/wu2020emerging.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/muller2021first.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/li2025taming.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/wang2025lost.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/zhao2024analysing.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/zhao2025steering.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/zhao2026when.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/xie2024adaptive.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/grattafiori2024llama.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/wong2026langfir.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/feng2026finegrained.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/team2026qwen.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/boer2026probing.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/xu2024knowledge.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/distill_tmp/kargaran2024mexa.yaml
/home/ubuntu/.agent-ml-research-prod42/proje
…[truncated 892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-25T04:17:57.430400+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42 -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -v '.venv' | grep -v '__pycache__' | grep -v 'distill_tmp' | grep -iE 'config|project|settings' | head -20",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-prod42 -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -v '.venv' | grep -v '__pycache__' | grep -v 'distill_tmp' | grep -iE 'config|project|settings' | head -20",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-25T04:17:57.481034+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/dream_registry.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/writing_plan.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/registry.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/mistakes.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/decisions.yaml
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-prod42/config/crons.yaml
/home/ubuntu/.agent-ml-research-prod42/config/approvals.yaml
/home/ubuntu/.agent-ml-research-prod42/config/backend.yaml
/home/ubuntu/.agent-ml-research-prod42/config/projects/clkc_mech_interp.yaml
/home/ubuntu/.agent-ml-research-prod42/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-prod42/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-prod42/config/feishu.yaml
/home/ubuntu/.agent-ml-research-prod42/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-prod42/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-25T04:17:59.940614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/config/projects/clkc_mech_interp.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/config/projects/clkc_mech_interp.yaml"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-25T04:18:00.091690+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	  - westd-14391:cuda:0
5	  gpu_ids:
6	  - cuda:0
7	  project_path: /root/clkc_mech_interp
8	  servers:
9	  - westd-14391
10	feishu:
11	  chat_id: oc_6951eb3869a0070e3ae607ab60c90dad
12	  check_references: false
13	  operational_chat_id: oc_c5d5712d42fa999cd11d5f120df2929d
14	  review_mode: fresh
15	  review_paper_path: projects/clkc_mech_interp/docs/paper/main.tex
16	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf
17	  review_round: 3
18	  review_supplementary_paths: ''
19	  submission_chat_id: oc_8b9aa92fafaf69b48d2c44b41c2fe9d9
20	project:
21	  created_at: '2026-05-21T11:57:57.565Z'
22	  description: 'Mechanistic Interpretability of Cross-Lingual Knowledge Conflicts:
23	    Probing, Sparse Feature Analysis, and Steering'
24	  name: clkc_mech_interp
25	  phase: research
26	  source_idea_id: idea_040
27	venue: emnlp-2026
28	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-25T04:18:00.092099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-25T04:18:00.192927+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	  - created_at: '2026-05-23T03:52:31Z'
25	    id: d66635
26	    text: 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section
27	  - created_at: '2026-05-23T11:42:30Z'
28	    id: 8a2af2
29	    text: abstract 不要超过 200 words
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-25T04:18:29.575323+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "clkc_mech_interp",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "clkc_mech_interp",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-25T04:18:52.997129+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23421
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-25T04:18:53.148118+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "clkc_mech_interp",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries\n- 论文路径：projects/clkc_mech_interp/docs/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf\n- 目标 venue：EMNLP 2026（ARR Long Paper）\n\n## Venue 要求\n- ARR 提交截止：2026-05-25\n- 正文 8 页限制 + 无限参考文献\n- Limitations 章节必须有，不计入页数\n- Double-blind 审稿\n- ACL 模板\n\n## 你的审查侧重\n\n请从以下维度严格评审：\n\n### 1. 探针方法论\n- Logistic regression probe 的选择是否合理？是否讨论了 probe complexity 与表征信息的关系（Hewitt & Liang 2019 selectivity concern）？\n- 单一 seed + bootstrap CI 是否足以支撑结论？论文承认单 split 局限但未做 cross-validation\n- Balanced accuracy 作为唯一指标是否充分？是否需要 AUROC 或其他指标？\n- Last-token aggregation 的选择是否充分论证？\n\n### 2. 统计分析\n- Fisher's exact test 用于 steering flip rate 对比是否合适？样本量（N=131-171）下的统计功效如何？\n- Bonferroni 校正的 family-wise 定义是否合理（per-layer k=10 vs 全局 30 tests）？\n- TOST 等价检验（±2pp margin）功效仅 1.4%——这是否削弱了\"mirror\"的核心主张？\n- Qwen 的 $\\Delta_{asym}$ CI 包含零——论文如何处理？\n\n### 3. 混淆因素排除\n- COMET tercile ablation 的功效分析（MDD=25.3pp）是否表明该分析无法排除翻译质量的影响？\n- Qwen3-8B 同时作为翻译模型和实验对象——这一双重角色的风险是否充分讨论？\n- Token overlap 分析仅使用 Jaccard similarity——是否存在更精细的词汇重叠度量？\n\n### 4. Steering 实验设计\n- $\\alpha$ 值的选择（±1, ±2, ±5, ±10, ±20）是否有理论依据？\n- Steering 仅在 Llama L13 成功，但论文标题暗示这是跨模型发现——这一张力如何评价？\n- Random control 的设计是否充分？是否应该使用其他方向（如其他层的 probe direction）作为对照？\n- \"Coherence collapse\" at α=+20 的处理是否充分？\n\n### 5. 可复现性\n- 代码/数据是否有可用性声明？\n- 实验细节是否足以复现（hyperparameters、random seeds、compute requirements）？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（按 severity: Must-Fix / Should-Fix / Minor 分级）→ Questions → 建议评分。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "clkc_mech_interp",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries\n- 论文路径：projects/clkc_mech_interp/docs/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf\n- 目标 venue：EMNLP 2026（ARR Long Paper）\n\n## Venue 要求\n- ARR 提交截止：2026-05-25\n- 正文 8 页限制 + 无限参考文献\n- Limitations 章节必须有，不计入页数\n- Double-blind 审稿\n- ACL 模板\n\n## 你的审查侧重\n\n请从以下维度严格评审：\n\n### 1. 探针方法论\n- Logistic regression probe 的选择是否合理？是否讨论了 probe complexity 与表征信息的关系（Hewitt & Liang 2019 selectivity concern）？\n- 单一 seed + bootstrap CI 是否足以支撑结论？论文承认单 split 局限但未做 cross-validation\n- Balanced accuracy 作为唯一指标是否充分？是否需要 AUROC 或其他指标？\n- Last-token aggregation 的选择是否充分论证？\n\n### 2. 统计分析\n- Fisher's exact test 用于 steering flip rate 对比是否合适？样本量（N=131-171）下的统计功效如何？\n- Bonferroni 校正的 family-wise 定义是否合理（per-layer k=10 vs 全局 30 tests）？\n- TOST 等价检验（±2pp margin）功效仅 1.4%——这是否削弱了\"mirror\"的核心主张？\n- Qwen 的 $\\Delta_{asym}$ CI 包含零——论文如何处理？\n\n### 3. 混淆因素排除\n- COMET tercile ablation 的功效分析（MDD=25.3pp）是否表明该分析无法排除翻译质量的影响？\n- Qwen3-8B 同时作为翻译模型和实验对象——这一双重角色的风险是否充分讨论？\n- Token overlap 分析仅使用 Jaccard similarity——是否存在更精细的词汇重叠度量？\n\n### 4. Steering 实验设计\n- $\\alpha$ 值的选择（±1, ±2, ±5, ±10, ±20）是否有理论依据？\n- Steering 仅在 Llama L13 成功，但论文标题暗示这是跨模型发现——这一张力如何评价？\n- Random control 的设计是否充分？是否应该使用其他方向（如其他层的 probe direction）作为对照？\n- \"Coherence collapse\" at α=+20 的处理是否充分？\n\n### 5. 可复现性\n- 代码/数据是否有可用性声明？\n- 实验细节是否足以复现（hyperparameters、random seeds、compute requirements）？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（按 severity: Must-Fix / Should-Fix / Minor 分级）→ Questions → 建议评分。"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-25T04:19:10.860916+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17712
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-25T04:19:11.018761+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "clkc_mech_interp",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries\n- 论文路径：projects/clkc_mech_interp/docs/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf\n- 目标 venue：EMNLP 2026（ARR Long Paper）\n\n## Venue 要求\n- ARR 提交截止：2026-05-25\n- 正文 8 页限制 + 无限参考文献\n- Limitations 章节必须有，不计入页数\n- Double-blind 审稿\n- ACL 模板\n\n## 你的审查侧重\n\n请从以下维度严格评审：\n\n### 1. 新颖性与贡献评估\n- 论文的三个 contributions 是否足以构成 EMNLP long paper 级别的贡献？\n- \"Detection ≠ Decision\" 这一发现在 Basu et al. 2026 已有类似结论——本文的增量贡献是什么？\n- 跨语言冲突信号的检测性（Contribution 1）是否属于\"expected result\"（已知冲突信号可检测 + 已知跨语言表征共享 → 跨语言冲突信号可检测）？\n- Steering 仅在一个模型的一个层有效——这是否足以支撑 Contribution 2 的 claim？\n\n### 2. 相关工作覆盖\n- 是否遗漏了关键相关工作？特别关注：\n  - 跨语言 mechanistic interpretability 的最新工作（2025-2026）\n  - Knowledge conflict 在多语言场景的行为研究\n  - Representation steering 的最新方法论进展\n  - Probing methodology 的批判性讨论（是否引用了 Belinkov 2022 survey？）\n- 引用是否全部真实存在？（特别注意 2026 年的引用）\n\n### 3. 写作质量\n- Abstract 是否在 200 words 以内（EMNLP 2026 要求）？\n- 论文叙事是否清晰连贯？Introduction 的 contribution list 与实验结果是否一致？\n- Discussion 是否过于 speculative（如三个 hypotheses for steering failure）？\n- Limitations 是否覆盖了关键弱点？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- 是否正确使用 ACL 模板（\\usepackage[review]{acl}）？\n- 匿名性：是否有任何去匿名化线索？\n- 图表质量：Figure 1, 2, 3 的信息密度和可读性\n- Table 格式是否符合 ACL 标准？\n\n### 5. 整体论文结构\n- 正面结果（probing）和负面结果（Qwen/Gemma steering failure）的比例是否平衡？\n- 论文是否过于 Llama-centric？三模型设计的预期价值是否充分实现？\n- Conclusion 是否过于保守或过于激进？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（按 severity: Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → 建议评分。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "clkc_mech_interp",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries\n- 论文路径：projects/clkc_mech_interp/docs/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf\n- 目标 venue：EMNLP 2026（ARR Long Paper）\n\n## Venue 要求\n- ARR 提交截止：2026-05-25\n- 正文 8 页限制 + 无限参考文献\n- Limitations 章节必须有，不计入页数\n- Double-blind 审稿\n- ACL 模板\n\n## 你的审查侧重\n\n请从以下维度严格评审：\n\n### 1. 新颖性与贡献评估\n- 论文的三个 contributions 是否足以构成 EMNLP long paper 级别的贡献？\n- \"Detection ≠ Decision\" 这一发现在 Basu et al. 2026 已有类似结论——本文的增量贡献是什么？\n- 跨语言冲突信号的检测性（Contribution 1）是否属于\"expected result\"（已知冲突信号可检测 + 已知跨语言表征共享 → 跨语言冲突信号可检测）？\n- Steering 仅在一个模型的一个层有效——这是否足以支撑 Contribution 2 的 claim？\n\n### 2. 相关工作覆盖\n- 是否遗漏了关键相关工作？特别关注：\n  - 跨语言 mechanistic interpretability 的最新工作（2025-2026）\n  - Knowledge conflict 在多语言场景的行为研究\n  - Representation steering 的最新方法论进展\n  - Probing methodology 的批判性讨论（是否引用了 Belinkov 2022 survey？）\n- 引用是否全部真实存在？（特别注意 2026 年的引用）\n\n### 3. 写作质量\n- Abstract 是否在 200 words 以内（EMNLP 2026 要求）？\n- 论文叙事是否清晰连贯？Introduction 的 contribution list 与实验结果是否一致？\n- Discussion 是否过于 speculative（如三个 hypotheses for steering failure）？\n- Limitations 是否覆盖了关键弱点？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- 是否正确使用 ACL 模板（\\usepackage[review]{acl}）？\n- 匿名性：是否有任何去匿名化线索？\n- 图表质量：Figure 1, 2, 3 的信息密度和可读性\n- Table 格式是否符合 ACL 标准？\n\n### 5. 整体论文结构\n- 正面结果（probing）和负面结果（Qwen/Gemma steering failure）的比例是否平衡？\n- 论文是否过于 Llama-centric？三模型设计的预期价值是否充分实现？\n- Conclusion 是否过于保守或过于激进？\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（按 severity: Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → 建议评分。"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-25T04:19:12.684198+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1665
}
```

</details>

---


### Assistant

_source line 288 · 2026-05-25T04:19:24.520399+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发，并行执行中
- **Reviewer 1**（方法严谨性）：已分配，审查探针方法论、统计分析、混淆因素排除、steering 实验设计
- **Reviewer 2**（新颖性与完整性）：已分配，审查贡献评估、相关工作、写作质量、格式合规

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 289 · 2026-05-25T04:24:32.305096+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 方法严谨性审查

## Paper Summary

本文研究多语言 LLM 在英中知识冲突场景下的内部表征机制。基于 ConflictQA 数据集，作者在三个模型架构（Llama-3.1-8B-Instruct、Qwen3-8B、Gemma-2-9B-IT）上训练 L2 正则化 logistic regression 探针，分析冲突信号的可检测性和跨语言迁移模式。核心发现：(1) 冲突信号在残差流中线性可分；(2) 中→英探针迁移比英→中高约 7pp，呈方向性不对称；(3) 该不对称与 XNLI 非冲突基线一致，暗示反映的是通用跨语言结构而非冲突特异性编码；(4) 因果干预（steering）仅在 Llama L13 成功；(5) 可检测性不蕴含因果影响。

## 主要优势

- **系统性强**：三个架构、四个迁移方向的完整 probing 矩阵，加上 XNLI 非冲突基线和三类混淆排除（COMET tercile、token overlap、XNLI），实验设计有层次感。
- **检测与因果的明确区分**：论文清晰地指出 probe accuracy ≠ causal relevance，并通过 steering 实验验证，发现仅 Llama L13 有因果效应。这一区分在 probing 文献中经常被忽略，值得肯定。
- **透明报告统计局限**：TOST 功效仅 1.4%、COMET 消融 MDD=25.3pp、Qwen Δ_asym CI 包含零——这些弱点均被主动报告，而非隐藏。
- **独立复制**（Appendix C）：用不同 seed（N=201）和不同 train/test split 复制了 L13 因果效应，增强了该特定发现的可信度。
- **Matched-condition steering**（Appendix D）：在 matched 条件下确认三个架构均表现出与主实验一致的方向，排除了 confound 驱动的虚假因果效应。

---

## 总体评分

**Overall**: 3.5（Borderline Conference）

**一句话总结**: 实验设计系统、统计报告透明，但核心 "mirror" 主张与统计证据之间存在显著张力——等价检验无功效、混淆排除无统计力、因果证据限于单模型。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要主张有支撑但关键统计检验（TOST、COMET 消融）功效不足，削弱核心等价主张 |
| Excitement | 3/5 | 跨语言冲突机制是有价值的方向，但发现偏向描述性、因果洞察有限 |
| Reproducibility | 3/5 | 超参数基本齐全，但缺乏明确的代码/数据开放声明，单 split 设计难以验证 |
| Confidence | 4/5 | 对探针方法论和统计分析有扎实理解，仔细审查了全文及附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题 "Mirror" 主张与 TOST 等价检验结果之间的根本张力

- 具体位置：Title、Section 4.4（Non-Conflict Baseline Comparison）、Figure 3
- 问题：论文标题宣称冲突信号 "mirror" 通用跨语言不对称，但支撑这一等价主张的正式统计检验（TOST，±2pp margin）功效仅 1.4%（Section 4.4："post-hoc power analysis shows only 1.4% power at this margin"）。达到 80% 功效需要 ±12.5pp margin，而观测到的 Δ_asym 本身才 ~7pp。这意味着 TOST 检验本质上是不可信息化的（uninformative）——它既无法支持等价，也无法否定等价。论文转而依赖 "CI 重叠"作为替代论据，但 CI 重叠不等同于等价检验（Schenker & Gentleman, 2001）。
- 为什么影响接收：标题中的核心主张（"mirror"）缺乏形式化统计支撑。如果 TOST 无功效且论文不提供替代的等价检验方法，则 "mirror" 从断言降级为观察性假说。这直接影响论文的 novelty claim 和 contribution scope。
- 建议修改方向：(a) 将标题从 "mirror" 改为更保守的措辞，如 "resemble" 或 "are consistent with"；(b) 或者，用更高 power 的等价检验方法（如 Bayesian equivalence testing with informative priors）提供正式证据；(c) 明确承认 "mirror" 是描述性观察而非统计结论。

**N2** [critical] COMET tercile 消融的 MDD=25.3pp 使翻译质量混淆排除本质上无效

- 具体位置：Section 4.5（Confound Exclusion — Translation quality）、Table 2
- 问题：论文用 COMET 分数将样本分为高/中/低质量三等分，比较 EN→ZH probe accuracy 在高 vs 低 tercile 之间的差异。但 80% 功效下的最小可检测差异（MDD）为 25.3pp（每 tercile 仅约 56 个样本）。观测到的不对称效应本身只有 ~7pp。这意味着即使翻译质量解释了全部 7pp 不对称，这一分析也检测不到。特别值得注意的是 Gemma 的 Δ=+10.3pp（Table 2）——虽然不显著（p=0.278），但这一效应大小本身已经接近观测到的主效应，却因为 underpowered 而被标记为"无显著影响"。
- 为什么影响接收：论文将此分析作为排除翻译质量混淆的主要证据（Section 4.5 第一段），但分析实际上无力排除任何合理大小的混淆效应。对于一篇以混淆排除为核心方法论贡献之一的论文，这一缺陷是实质性的。
- 建议修改方向：(a) 明确标注此分析为 underpowered 且不能作为排除翻译质量混淆的充分证据（目前的表述 "far exceeding observed effects" 容易让读者误解为是好消息）；(b) 考虑使用连续的 COMET 分数作为回归协变量（而非离散化 tercile），以提高统计功效；(c) 或者增加样本量使 tercile 分析有意义。

**N3** [critical] 因果证据限于单模型单层，与标题/摘要的跨模型叙事不匹配

- 具体位置：Section 4.6、Section 5（Discussion）、Table 3、Abstract
- 问题：Steering 仅在 Llama L13 产生显著因果效应（Fisher p=0.002），Qwen 和 Gemma 在所有层和所有 α 值上均无显著效应（Qwen: "best p=0.785"; Gemma: "best p=0.148"；Section 5 第 3 段）。论文标题和摘要的措辞（"We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT"）给读者的印象是三个模型产生了对等的发现，但因果层面的核心发现实际上只属于 Llama。
- 为什么影响接收：因果可干预性是论文超越纯相关性 probing 研究的关键差异化点。如果这一差异化点仅限于 3 个模型中的 1 个，则论文对 "跨模型一般性" 的暗示是误导性的。审稿人可能会质疑：Llama L13 的因果效应是否仅仅是架构特异性的巧合，而非可推广的机制性发现？
- 建议修改方向：(a) 在摘要和结论中更清晰地区分 "检测"（跨模型一致）和 "因果影响"（仅 Llama）的范围；(b) 讨论 Qwen/Gemma steering 失败的可能原因时（Section 5 "Why does steering fail" 已有初步讨论），提供更系统的分析——例如是否因为这些模型的冲突解决机制涉及非线性交互或分布在多层上；(c) 考虑用其他因果干预方法（如 causal mediation analysis、activation patching）在 Qwen/Gemma 上寻找因果证据。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 单一 train/test split 的探针结果缺乏 cross-validation 验证

- 具体位置：Section 3.3、Limitations
- 问题：所有 probing 结果基于单一 train/test split + bootstrap CI（n=2,000）。Bootstrap CI 量化的是给定 split 下的估计不确定性，但不解决 split 依赖性问题。如果该 split 恰好有利于某些方向的迁移，所有不对称结论都可能被影响。Appendix C 的独立复制仅覆盖 steering（N=201），不覆盖 probing 精度。论文在 Limitations 中承认 "all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability"，但未采取行动。
- 建议：报告 5-fold 或 10-fold cross-validation 的 probe accuracy，或至少在 3 个不同 random split 上复制主要 probing 结果（Table 1），以确认不对称方向和量级的稳定性。

**W2** [warning] Qwen3-8B 同时作为翻译模型和实验对象的双重角色风险未充分控制

- 具体位置：Section 3.2（Translation）、Limitations
- 问题：Qwen3-8B 用于将所有英文输入翻译为中文（Section 3.2），同时也是三个被探测的模型之一。如果 Qwen 的翻译输出系统性地偏向其自身的处理模式（例如倾向于生成它自己更容易 "理解" 的表述），那么 Qwen 上的探针结果可能存在自我增强偏差。论文在 Limitations 中提及此问题但仅以 "COMET-based quality control and Llama/Gemma cross-validation mitigate this dual-role concern" 一笔带过。然而 COMET 只衡量翻译的总体质量，不衡量翻译是否偏向 Qwen 的 tokenization 或内部表征偏好。
- 建议：(a) 使用另一个翻译模型（如 Google Translate API 或 NLLB）重新翻译一个子集，在 Qwen 上对比两组翻译的 probe accuracy 是否有显著差异；(b) 至少分析 Qwen 翻译的 self-BLEU 或其他指标，检查是否有系统性 "self-favoring" 模式。

**W3** [warning] Probe selectivity（Hewitt & Liang, 2019）未被正式评估

- 具体位置：Section 3.3
- 问题：论文引用了 Hewitt & Liang (2019)（在 Section 1 和 Section 3.3），但未计算其提出的 selectivity 指标——即 probe 在 control task 上的精度与目标 task 之间的差异。XNLI 基线（Section 3.5）部分承担了这一角色，但其设计目的不同（它测试的是 "不对称是否冲突特异" 而非 "probe 是否有选择性"）。一个高 probe accuracy 可能仅仅反映残差流的高维几何特性，而非真正的冲突信号编码。
- 建议：计算 control selectivity（例如用 random label 训练的 probe accuracy 作为基线），确认报告的 probe accuracy 显著高于 selectivity baseline。

**W4** [warning] Balanced accuracy 作为唯一探针性能指标不够充分

- 具体位置：Section 3.3、Table 1
- 问题：论文仅报告 balanced accuracy（Section 3.3: "We report balanced accuracy to account for class imbalance"）。对于二分类 probing 任务，AUROC 是更信息丰富的指标——它不依赖于阈值选择，能更好地反映表征中的信号强度。尤其是在跨语言迁移场景下，不同方向的 probe 可能具有不同的校准特性，仅看 balanced accuracy 可能遗漏重要信息。
- 建议：补充报告 AUROC（至少在附录中），确认不对称模式在不同指标下一致。

**W5** [warning] Steering 实验的 α 值选择缺乏理论依据

- 具体位置：Section 3.6
- 问题：论文扫描 α ∈ {±1, ±2, ±5, ±10, ±20}（Section 3.6），但未解释这些值为何合理。α=±20 导致 coherence collapse（Section 4.6 和 Appendix Table 4），而 α=±1 基本无效应。有效范围（α=±5 到 ±10）的选择看起来是事后确定的。此外，α 的绝对值依赖于 probe 方向向量的 norm，而不同层的 norm 不同——是否做了归一化处理？
- 建议：(a) 将 α 值相对于 probe direction 的 norm 归一化，报告 α/||w|| 以增强跨层可比性；(b) 讨论 α 选择的依据，或至少说明这是一个 grid search 并报告了所有结果（而非 cherry-picking）。

---

## 小问题（不影响接收）

- **M1**: Section 3.2 提到 "质量 validated by COMET"，但 COMET 的具体版本（wmt20-comet-da? wmt22-comet-da?）和阈值未在正文中说明（仅在 "quality-validated" 中一带而过）。应明确 COMET model ID 和筛选标准。
- **M2**: Token overlap 分析仅使用 Jaccard similarity（Section 4.5）。字符级或 BPE-aware 的重叠度量可能更准确地捕捉 tokenization 对跨语言迁移的影响。
- **M3**: 代码和数据的可用性声明不清晰。Section A（AI Use）提到使用了 Claude 辅助编码，但未说明代码/数据是否会公开。ARR 的 reproducibility 维度（M2）明确要求 "code/data availability plans"。
- **M4**: Random direction control（Section 3.6: "a random direction vector of equal norm"）是最低标准的控制。使用其他层的 probe direction 或 random subspace 中的方向作为额外对照，能更有力地排除 steering 效应是非特异性扰动的可能。
- **M5**: Figure 3 的灰色 ±2pp 等价区间在视觉上暗示 TOST 是有效的等价检验，但实际上 TOST 在该 margin 下几乎无功效。建议在图注中明确标注 TOST 功效不足，或移除该视觉元素以避免误导。

---

## Questions for Authors

1. 如果使用 5-fold cross-validation 替代单一 split，Δ_asym 的方向和量级是否稳定？是否有任何 fold 出现不对称方向翻转？
2. Qwen 和 Gemma 上 steering 失败——作者是否尝试过 activation patching 或其他因果干预方法？如果 steering 的失败是由于非线性交互，这些替代方法可能更适用。
3. COMET tercile 消融中 Gemma 的 Δ=+10.3pp 虽然不显著，但效应大小已接近主效应（~7pp）。作者如何解释这一数值？是否担心翻译质量可能在 Gemma 上部分解释了不对称？
4. 论文使用 last-token aggregation——是否评估过其他 aggregation 策略（如 mean pooling、attention-weighted）？不同语言的最后一个 token 可能承载不同信息量。
5. 对于 "mirror" 这一核心主张，作者能否提供一个 Bayesian equivalence testing 结果（例如 ROPE+HDI 方法），作为对 TOST 功效不足的补充？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 290 · 2026-05-25T04:24:43.381282+00:00_

Reviewer 1 审稿意见已收到。3 个 Must-Fix + 5 个 Should-Fix，评分 3.5（Borderline Conference）。核心问题集中在"mirror"主张的统计支撑不足、COMET 消融无统计力、因果证据仅限单模型。

等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 291 · 2026-05-25T04:24:56.083290+00:00_

[Reviewer 1 审稿结果]:
审稿完成。以下是核心结论摘要：

**Overall: 3.5（Borderline Conference）**

三个 Must-Fix 问题：

1. **"Mirror" 主张 vs TOST 功效 1.4%**：标题核心词 "mirror" 缺乏形式化统计支撑，等价检验本质上无信息量，建议改为 "resemble" 或提供 Bayesian equivalence testing。

2. **COMET tercile 消融 MDD=25.3pp**：主效应仅 ~7pp，但消融分析只能检测 >25pp 的混淆效应，翻译质量混淆实质上未被排除（Gemma Δ=+10.3pp 尤其值得注意）。

3. **因果证据仅限 Llama L13**：Qwen/Gemma steering 全部失败，但标题和摘要暗示跨模型一般性发现。

五个 Should-Fix：单 split 无 cross-validation、Qwen 双重角色、probe selectivity 未正式评估、缺 AUROC、α 值选择无理论依据。

论文实验设计系统性好、统计局限透明报告值得肯定，但 claims 与 evidence 之间的 calibration 需要调整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-25T04:25:03.418193+00:00_

Reviewer 1 审稿已收到，等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 20

## Round 20

6 recorded events


### User

_source line 293 · 2026-05-25T04:26:28.086274+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性与完整性

## 论文信息
- **标题**: English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries
- **Venue**: EMNLP 2026 (ARR Long Paper)
- **审查侧重**: 新颖性与贡献、相关工作覆盖、写作质量、格式合规、整体结构

---

## 总体评分

**Overall**: 3.0 — Findings（可被 Findings 接收）

**一句话总结**: 实验设计和统计方法扎实，但核心发现 "Detection ≠ Decision" 已由 Basu et al. (2026) 建立，跨语言可检测性属于预期结果，且 steering 正面结果仅来自 1/3 模型的 1 个层，新颖性和贡献量不足以支撑主会议 long paper。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论严谨（bootstrap CI、Bonferroni、TOST equivalence、confound exclusion），但 Contribution 2 的 claim 基于 1/3 模型正面结果略有过度 |
| **Excitement** | 2.5/5 | 核心 insight（detection ≠ causation）已有先行工作；跨语言扩展有价值但增量有限；大量负面结果降低了 impact |
| **Reproducibility** | 4/5 | 超参数、数据集分割、统计检验细节充分；GPU 型号和 seed 均有报告；独立复制实验是加分项 |
| **Reviewer Confidence** | 4/5 | 熟悉 probing、representation steering、cross-lingual representations 相关文献 |

---

## 主要优势

1. **统计严谨性突出。** Bootstrap paired CIs、Bonferroni 校正、TOST 等效性检验、Bayesian BF 分析，在 probing/steering 文献中这种统计水准少见。特别是 TOST 的 power analysis（80% power 需 ±12.5 pp margin）是诚实的自我批评。

2. **Confound exclusion pipeline 设计完善。** COMET tercile 分层 + token overlap Jaccard 分析 + EN-DE 对照 + XNLI non-conflict baseline，系统性排除了翻译质量和词汇重叠两个关键混淆变量。EN-DE 的 near-zero asymmetry（Jaccard 14.8% 但 Δ=+1.2 pp, n.s.）特别有说服力。

3. **负面结果的诚实报告。** Qwen 和 Gemma steering 失败的完整报告（包括 matched-condition Appendix Table 5），以及 Gemma 88.9% probe accuracy + zero flips 的对比，是强有力的 negative evidence。

4. **独立复制设计。** L13 steering 用不同 seed、不同 train/test split 独立复制（Appendix C），boundary analysis 用独立采样 N=201（Appendix B），提升了因果定位结论的可信度。

5. **XNLI baseline 比较方法论有价值。** 用非冲突语义任务的 probe transfer asymmetry 作为 baseline，这一方法论思路（"先确认 baseline asymmetry 再解读 task-specific 差异"）对后续跨语言 probing 工作有参考价值。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现 "Detection ≠ Decision" 的增量贡献不足
- **具体位置**: Introduction 第 18 行引用 Basu et al. (2026)；Discussion §5 "Relation to interpretability without actionability" 段
- **问题**: 论文的核心 insight——"probe accuracy 不意味着 causal relevance"——已由 Basu et al. (2026) 在临床 NLP 任务中建立（98.2% AUROC probe accuracy + steering 完全失败）。本文在 Discussion 中试图区分：mid-layer steering 在本文成功但在 Basu et al. 中失败，差异在于 layer selection。但这一区分是弱的：(a) 本文的 "成功" 仅限于 1/3 模型的 1 个层；(b) layer sweep 是方法论改进，不是新发现；(c) 2/3 模型的失败反而更接近 Basu et al. 的结论。论文需要更明确地阐述超越 Basu et al. 的具体贡献。
- **为什么影响接收**: 若核心 contribution 已被先行工作覆盖，论文的 novelty 不足以支撑 long paper。
- **建议修改方向**: 重新定位论文贡献——强调跨语言维度的独特性（如 asymmetry 的 baseline 归因），弱化 "detection ≠ decision" 作为独立 contribution。

**N2** [critical] Contribution 2 ("Architecture-dependent causal localization") 证据过弱
- **具体位置**: Introduction Contribution 2；§4.6 全节；Table 3；Appendix Table 5
- **问题**: 该 contribution 声称 "causal influence is consistently localized to L13 in Llama, while analogous steering in Qwen and Gemma yields no significant effect"。但实际证据是：3 个模型中只有 1 个（Llama）在 1 个层（L13）显示显著效果。这不是 "architecture-dependent causal localization"，而是 "我们在一个模型找到了正面结果，两个模型是 null"。关键问题：
  - Llama 的正面结果是否是 false positive？考虑到 multiple testing（3 models × 多个 layers × 10 α values），即使有 Bonferroni 校正，family-wise error rate 也需要跨模型评估。
  - "Architecture-dependent" 的 claim 需要解释 **为什么** 不同架构表现不同，而不仅仅是报告它们不同。Discussion 中三个 hypotheses（non-linear pathway、superposition、sandwich normalization）全部是 untested speculation。
- **为什么影响接收**: 核心 claim 的实验支撑不足以构成 EMNLP 级别贡献。
- **建议修改方向**: (1) 将 claim 降级为 "exploratory finding in Llama with null results in Qwen/Gemma"；(2) 提供至少一个 hypothesis 的初步验证（如 Gemma sandwich norm 的 ablation）；(3) 补充更多模型或更多层的 steering 结果。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Contribution 1（跨语言冲突可检测性）可能是 expected result
- **具体位置**: Introduction Contribution 1；§4.2-4.3
- **问题**: 推理链：(1) 知识冲突信号在单语言内可检测（Zhao et al., 2024）→ (2) 多语言模型有共享跨语言表征空间（Wu et al., 2020; Wendler et al., 2024）→ (3) 因此跨语言冲突信号可检测。这是一个相当直接的推论。此外，XNLI baseline 显示 asymmetry 不是冲突特异的——这意味着 Contribution 1 的核心发现是 "冲突信号的跨语言特性与通用跨语言特性无异"，本质上是一个 null result。
- **建议**: 更坦诚地讨论这一推理链的可预测性，并将 XNLI baseline 发现提升为更重要的贡献（"任何跨语言 probing 研究都必须先控制 baseline asymmetry" 是有实践价值的方法论建议）。

**W2** [warning] 论文过度 Llama-centric，三模型设计的价值未充分实现
- **具体位置**: 全文结构；§4.6 Causal Evidence；§5 Discussion
- **问题**: 三模型设计本应提供 cross-architecture validation，但实际结果是：probing 部分三个模型一致（这是好的），steering 部分 2/3 是 null。论文的核心叙事（detection ≠ decision + mid-layer causal locus）完全依赖 Llama。Qwen 和 Gemma 的主要作用是提供 negative evidence，但 negative evidence 本身不构成 positive contribution。
- **建议**: (1) 重新组织叙事——将 Llama 定位为 case study 而非通用结论；(2) 更深入分析 Qwen/Gemma 失败的原因，而非仅提供三个 untested hypotheses。

**W3** [warning] 遗漏关键相关工作
- **具体位置**: §2 Related Work
- **问题**: 以下相关工作未被讨论：
  - **Ravichander et al. (2021), "Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?"** — 直接探讨了 probing accuracy 是否意味着 task relevance 的问题，与本文核心论点高度相关。本文引用了 Hewitt & Liang (2019) 的 control task 思路，但漏掉了 Ravichander et al. 对 probing accuracy ≠ task relevance 的更直接论证。
  - **Gurgurov et al. (2026), "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark" (arXiv:2601.08331)** — 首个跨语言 steering benchmark，覆盖 32 语言，与本文的 cross-lingual steering 实验直接相关。
  - **Pimentel et al. (2020/2021)** 关于 information-theoretic probing 的理论框架，对 probing methodology 的讨论有补充价值。
- **建议**: 在 Related Work 中补充这些引用，特别是 Ravichander et al.，因为它直接强化了本文的论点。

**W4** [warning] Discussion 中三个 steering 失败 hypotheses 过于投机
- **具体位置**: §5 "Why does steering fail in Qwen and Gemma?" 段
- **问题**: 三个假设（non-linear causal pathway、residual stream superposition、architectural differences/sandwich normalization）全部未经验证。论文没有任何实验证据支持其中任何一个。虽然标注为 "merit consideration"，但在没有 ablation 或 diagnostic 的情况下，这些假设缺乏信息量——任何 steering 失败都可以用 "可能是 non-linear" 或 "可能是 superposition" 来解释。
- **建议**: (1) 删减到最有证据支持的一个假设；或 (2) 对至少一个假设提供初步 diagnostic（如用 non-linear probe 检验 hypothesis 1，或用 PCA 可视化检验 hypothesis 2）。

---

## 小问题（不影响接收）

- **M1**: Abstract 198 words（接近 200 上限），建议适度压缩以留出余量。
- **M2**: Table 1 注释 "Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies" 非常重要但容易被忽略，建议移入正文或用更醒目的方式呈现。
- **M3**: §4.5 Confound Exclusion 中 Gemma 的 COMET tercile 结果（Δ = +10.3 pp, p = 0.278）在 confound 方向，虽然不显著，但应在 Limitations 中更明确提及。
- **M4**: Figure 2（layer-wise probe accuracy）和 Figure 3（asymmetry forest plot）的信息密度适中。但 Figure 1（pipeline overview）信息量偏低——主要是流程描述，读正文即可获得相同信息。考虑替换为更有信息量的图（如 Llama L13 steering 前后的行为分布变化）。
- **M5**: Appendix A (Use of AI Assistants) 的格式符合 ACL 2024+ 的建议，但措辞非常简短，可考虑补充 AI 辅助的具体边界说明。
- **M6**: 论文引用 Marks & Tegmark (2024) 的 venue 写为 ICLR 2024，但该论文实际发表于 NeurIPS 2023（虽然 arXiv 版本 2023.10 发布），请核实。

---

## Questions to Authors

**Q1**: Llama L13 的 steering 效果是否在不同 prompt template 下稳定？当前实验是否只使用了一种 prompt format？如果 prompt 变化导致 steering 失效，这将进一步削弱 causal claim。

**Q2**: 为什么没有尝试 non-linear steering 方法（如 SAE-based steering，参考 Zhao et al. 2025 的 SpARE）？既然 Discussion 中自己提出了 "non-linear causal pathway" 假设，尝试 SAE steering 可以直接检验这一假设。

**Q3**: Qwen3-8B 同时作为翻译模型和实验模型——虽然 Limitations 提到了这一双重角色，但 Qwen 的 EN→ZH probe transfer accuracy 是三个模型中最高的（67.3%），这是否可能是 translation-model artifact（Qwen 生成的翻译与 Qwen 的内部表征自然更 aligned）？

**Q4**: TOST 等效性检验 power 极低（1.4%），Bayes factor 仅 1.5——是否考虑过这可能意味着 conflict 和 XNLI asymmetry 实际上不等效，只是当前数据不足以区分？标题中的 "Mirror" 一词暗示等效性，但统计证据并不支持这一强 claim。

---

## Missing References

1. **Ravichander, A., Belinkov, Y., & Hovy, E. (2021).** "Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?" — 直接论证 probing accuracy 不意味着 task relevance。
2. **Gurgurov, D. et al. (2026).** "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark." arXiv:2601.08331 — 首个跨语言 steering 标准化 benchmark。
3. **Pimentel, T. & Cotterell, R. (2021).** "A Bayesian Framework for Information-Theoretic Probing." EMNLP 2021 — probing 的 information-theoretic 理论基础。

---

## 建议评分汇总

| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 2.5/5 |
| Overall Assessment | 3.0 (Findings) |
| Reproducibility | 4/5 |
| Confidence | 4/5 |

**总结**: 这是一篇方法论上扎实、统计上严谨的实验论文。Confound exclusion pipeline 和 XNLI baseline 方法论有价值，负面结果报告诚实。但核心新颖性不足：(1) "detection ≠ decision" 已被 Basu et al. 建立；(2) 跨语言可检测性属于预期结果；(3) causal steering 正面结果过于局限（1/3 模型、1 个层）。建议接收至 Findings，但需要 reframe contributions 以更准确反映实际证据强度。主会议接收需要显著增强 causal evidence（更多模型、non-linear steering、或至少一个 failure hypothesis 的验证）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-25T04:27:03.045383+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "clkc_mech_interp",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 — 方法严谨性审查\n\n## Must-Fix 问题\n\n**N1** [critical] 标题 \"Mirror\" 主张与 TOST 等价检验结果之间的根本张力\n- 论文标题宣称冲突信号 \"mirror\" 通用跨语言不对称，但 TOST（±2pp margin）功效仅 1.4%。达到 80% 功效需要 ±12.5pp margin，而观测到的 Δ_asym 本身才 ~7pp。TOST 检验本质上是 uninformative。论文转而依赖 \"CI 重叠\" 作为替代论据，但 CI 重叠不等同于等价检验。\n- 建议：将 \"mirror\" 改为更保守的 \"resemble\" 或 \"are consistent with\"；或用更高 power 的等价检验方法提供正式证据。\n\n**N2** [critical] COMET tercile 消融的 MDD=25.3pp 使翻译质量混淆排除本质上无效\n- 80% 功效下 MDD=25.3pp，但主效应仅 ~7pp。即使翻译质量解释了全部不对称，分析也检测不到。Gemma Δ=+10.3pp（虽 p=0.278）效应大小接近主效应。\n- 建议：明确标注为 underpowered；考虑使用连续 COMET 分数作为回归协变量。\n\n**N3** [critical] 因果证据限于单模型单层，与标题/摘要的跨模型叙事不匹配\n- Steering 仅在 Llama L13 成功，Qwen/Gemma 全部失败。标题和摘要给人跨模型对等发现的印象，但因果证据实际只属于 Llama。\n- 建议：在摘要和结论中更清晰地区分 \"检测\"（跨模型一致）和 \"因果影响\"（仅 Llama）。\n\n## Should-Fix 问题\n\n**W1** [warning] 单一 train/test split 的探针结果缺乏 cross-validation 验证\n\n**W2** [warning] Qwen3-8B 同时作为翻译模型和实验对象的双重角色风险未充分控制\n\n**W3** [warning] Probe selectivity（Hewitt &amp; Liang, 2019）未被正式评估\n\n**W4** [warning] Balanced accuracy 作为唯一探针性能指标不够充分（缺 AUROC）\n\n**W5** [warning] Steering 实验的 α 值选择缺乏理论依据\n\n## 小问题\nM1: COMET 版本未说明\nM2: Token overlap 仅用 Jaccard\nM3: 代码/数据可用性声明不清\nM4: Random direction control 是最低标准\nM5: Figure 3 灰色 ±2pp 等价区间视觉暗示 TOST 有效，但实际功效不足\n\n## 总体评分：3.5（Borderline Conference）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "clkc_mech_interp",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 — 方法严谨性审查\n\n## Must-Fix 问题\n\n**N1** [critical] 标题 \"Mirror\" 主张与 TOST 等价检验结果之间的根本张力\n- 论文标题宣称冲突信号 \"mirror\" 通用跨语言不对称，但 TOST（±2pp margin）功效仅 1.4%。达到 80% 功效需要 ±12.5pp margin，而观测到的 Δ_asym 本身才 ~7pp。TOST 检验本质上是 uninformative。论文转而依赖 \"CI 重叠\" 作为替代论据，但 CI 重叠不等同于等价检验。\n- 建议：将 \"mirror\" 改为更保守的 \"resemble\" 或 \"are consistent with\"；或用更高 power 的等价检验方法提供正式证据。\n\n**N2** [critical] COMET tercile 消融的 MDD=25.3pp 使翻译质量混淆排除本质上无效\n- 80% 功效下 MDD=25.3pp，但主效应仅 ~7pp。即使翻译质量解释了全部不对称，分析也检测不到。Gemma Δ=+10.3pp（虽 p=0.278）效应大小接近主效应。\n- 建议：明确标注为 underpowered；考虑使用连续 COMET 分数作为回归协变量。\n\n**N3** [critical] 因果证据限于单模型单层，与标题/摘要的跨模型叙事不匹配\n- Steering 仅在 Llama L13 成功，Qwen/Gemma 全部失败。标题和摘要给人跨模型对等发现的印象，但因果证据实际只属于 Llama。\n- 建议：在摘要和结论中更清晰地区分 \"检测\"（跨模型一致）和 \"因果影响\"（仅 Llama）。\n\n## Should-Fix 问题\n\n**W1** [warning] 单一 train/test split 的探针结果缺乏 cross-validation 验证\n\n**W2** [warning] Qwen3-8B 同时作为翻译模型和实验对象的双重角色风险未充分控制\n\n**W3** [warning] Probe selectivity（Hewitt &amp; Liang, 2019）未被正式评估\n\n**W4** [warning] Balanced accuracy 作为唯一探针性能指标不够充分（缺 AUROC）\n\n**W5** [warning] Steering 实验的 α 值选择缺乏理论依据\n\n## 小问题\nM1: COMET 版本未说明\nM2: Token overlap 仅用 Jaccard\nM3: 代码/数据可用性声明不清\nM4: Random direction control 是最低标准\nM5: Figure 3 灰色 ±2pp 等价区间视觉暗示 TOST 有效，但实际功效不足\n\n## 总体评分：3.5（Borderline Conference）"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-25T04:27:24.909161+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21863
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-25T04:27:25.113606+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "clkc_mech_interp",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 — 新颖性与完整性审查\n\n## Must-Fix 问题\n\n**N1** [critical] 核心发现 \"Detection ≠ Decision\" 的增量贡献不足\n- \"probe accuracy 不意味着 causal relevance\" 已由 Basu et al. (2026) 在临床 NLP 任务中建立（98.2% AUROC + steering 完全失败）。本文的 \"成功\" 仅限于 1/3 模型的 1 个层；layer sweep 是方法论改进，不是新发现；2/3 模型的失败反而更接近 Basu et al. 的结论。\n- 建议：重新定位贡献——强调跨语言维度的独特性，弱化 \"detection ≠ decision\" 作为独立 contribution。\n\n**N2** [critical] Contribution 2 (\"Architecture-dependent causal localization\") 证据过弱\n- 3 个模型中只有 1 个（Llama）在 1 个层（L13）显示显著效果。这不是 \"architecture-dependent causal localization\"，而是 \"我们在一个模型找到了正面结果，两个模型是 null\"。Multiple testing 的 family-wise error rate 需要跨模型评估。Discussion 中三个 hypotheses 全部是 untested speculation。\n- 建议：将 claim 降级为 \"exploratory finding\"；或提供至少一个 hypothesis 的初步验证。\n\n## Should-Fix 问题\n\n**W1** [warning] Contribution 1（跨语言冲突可检测性）可能是 expected result\n- 推理链：单语言可检测 + 共享跨语言空间 → 跨语言可检测。这是一个相当直接的推论。XNLI baseline 表明不对称不是冲突特异的——本质上是 null result。\n\n**W2** [warning] 论文过度 Llama-centric，三模型设计的价值未充分实现\n- Probing 部分三模型一致（好），steering 部分 2/3 是 null。核心叙事完全依赖 Llama。\n\n**W3** [warning] 遗漏关键相关工作\n- Ravichander et al. (2021) \"Probing the Probing Paradigm\"\n- Gurgurov et al. (2026) \"CLaS-Bench: Cross-Lingual Steering Benchmark\"\n- Pimentel &amp; Cotterell (2021) information-theoretic probing\n\n**W4** [warning] Discussion 中三个 steering 失败 hypotheses 过于投机\n\n## 小问题\nM1: Abstract 198 words 接近上限\nM2: Table 1 注释重要但容易被忽略\nM3: Gemma COMET tercile Δ=+10.3pp 应在 Limitations 更明确提及\nM4: Figure 1 信息量偏低\nM5: Appendix A (AI Use) 措辞简短\nM6: Marks &amp; Tegmark (2024) venue 可能有误（ICLR 2024 vs NeurIPS 2023）\n\n## Missing References\n1. Ravichander et al. (2021) — probing accuracy ≠ task relevance\n2. Gurgurov et al. (2026) — CLaS-Bench cross-lingual steering benchmark\n3. Pimentel &amp; Cotterell (2021) — information-theoretic probing\n\n## 总体评分：3.0（Findings）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "clkc_mech_interp",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 — 新颖性与完整性审查\n\n## Must-Fix 问题\n\n**N1** [critical] 核心发现 \"Detection ≠ Decision\" 的增量贡献不足\n- \"probe accuracy 不意味着 causal relevance\" 已由 Basu et al. (2026) 在临床 NLP 任务中建立（98.2% AUROC + steering 完全失败）。本文的 \"成功\" 仅限于 1/3 模型的 1 个层；layer sweep 是方法论改进，不是新发现；2/3 模型的失败反而更接近 Basu et al. 的结论。\n- 建议：重新定位贡献——强调跨语言维度的独特性，弱化 \"detection ≠ decision\" 作为独立 contribution。\n\n**N2** [critical] Contribution 2 (\"Architecture-dependent causal localization\") 证据过弱\n- 3 个模型中只有 1 个（Llama）在 1 个层（L13）显示显著效果。这不是 \"architecture-dependent causal localization\"，而是 \"我们在一个模型找到了正面结果，两个模型是 null\"。Multiple testing 的 family-wise error rate 需要跨模型评估。Discussion 中三个 hypotheses 全部是 untested speculation。\n- 建议：将 claim 降级为 \"exploratory finding\"；或提供至少一个 hypothesis 的初步验证。\n\n## Should-Fix 问题\n\n**W1** [warning] Contribution 1（跨语言冲突可检测性）可能是 expected result\n- 推理链：单语言可检测 + 共享跨语言空间 → 跨语言可检测。这是一个相当直接的推论。XNLI baseline 表明不对称不是冲突特异的——本质上是 null result。\n\n**W2** [warning] 论文过度 Llama-centric，三模型设计的价值未充分实现\n- Probing 部分三模型一致（好），steering 部分 2/3 是 null。核心叙事完全依赖 Llama。\n\n**W3** [warning] 遗漏关键相关工作\n- Ravichander et al. (2021) \"Probing the Probing Paradigm\"\n- Gurgurov et al. (2026) \"CLaS-Bench: Cross-Lingual Steering Benchmark\"\n- Pimentel &amp; Cotterell (2021) information-theoretic probing\n\n**W4** [warning] Discussion 中三个 steering 失败 hypotheses 过于投机\n\n## 小问题\nM1: Abstract 198 words 接近上限\nM2: Table 1 注释重要但容易被忽略\nM3: Gemma COMET tercile Δ=+10.3pp 应在 Limitations 更明确提及\nM4: Figure 1 信息量偏低\nM5: Appendix A (AI Use) 措辞简短\nM6: Marks &amp; Tegmark (2024) venue 可能有误（ICLR 2024 vs NeurIPS 2023）\n\n## Missing References\n1. Ravichander et al. (2021) — probing accuracy ≠ task relevance\n2. Gurgurov et al. (2026) — CLaS-Bench cross-lingual steering benchmark\n3. Pimentel &amp; Cotterell (2021) — information-theoretic probing\n\n## 总体评分：3.0（Findings）"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-25T04:27:26.676037+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Assistant

_source line 298 · 2026-05-25T04:27:29.313604+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 299 · 2026-05-25T04:27:31.948484+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0（Findings 级别）。

核心判断：
- **Soundness 3.5**：方法论严谨，但 Contribution 2 的 claim 基于 1/3 模型正面结果有过度之嫌
- **Excitement 2.5**：核心 insight "detection ≠ decision" 已由 Basu et al. (2026) 建立，增量贡献有限
- 两个 Must-Fix：(1) 与 Basu et al. 的增量贡献需更明确阐述；(2) "Architecture-dependent causal localization" 证据过弱（1/3 模型、1 层）
- 四个 Should-Fix：跨语言可检测性为 expected result、论文过度 Llama-centric、遗漏关键相关工作（Ravichander 2021、CLaS-Bench 2026）、Discussion 假设过于投机
- 格式合规：正文 8 页 ✓、Abstract 198 词 ✓、`[review]` 模式 ✓、匿名 ✓、Limitations 章节 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 300 · 2026-05-25T04:27:37.441554+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 22

## Round 22

22 recorded events


### User

_source line 301 · 2026-05-25T04:29:18.278162+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### R1-N1: 标题 "Mirror" 主张与 TOST 等价检验功效不足

**[AGREE]** 同意这是论文的核心张力之一。

论文在 §4.4 承认 TOST 功效仅 1.4%（±2pp margin），需要 ±12.5pp margin 才能达到 80% power。Bayes factor BF₀₁ ≈ 1.5 也仅为 "directionally consistent but modest evidence"。论文随后转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但正如 R1 所指出，CI 重叠不等同于等价检验。

我在 Q4 中也提出了同样的问题。补充一点：标题中的 "Mirror" 是全文最强的等价性 claim，但论文在正文中的措辞更谨慎（"consistent with"），存在标题与正文之间的不一致。建议将标题改为 "... Are Consistent With General Cross-Lingual Asymmetries" 或类似表述。

### R1-N2: COMET tercile 消融 MDD=25.3pp 使混淆排除无效

**[REBUT]** 部分反驳——COMET tercile 分析确实 underpowered，但 "本质上无效" 的结论忽略了 confound exclusion pipeline 的多证据链设计。

论文的混淆排除不仅依赖 COMET tercile，而是一个三控制管线：
1. **COMET tercile**（§4.5 Table 2）：确实 underpowered（MDD=25.3pp），R1 此点正确。但 Qwen 方向相反（Δ = -5.6pp），Llama 接近零（Δ = +1.7pp），这两个模型的方向性证据已经不支持翻译质量混淆。
2. **Token overlap**（§4.5）：Jaccard 3-4%，Llama 有弱负相关（r = -0.15），方向与 confound hypothesis 相反。
3. **EN-DE 对照**（§5 "Typological distance" 段）：EN-DE Jaccard 14.8%（~4× EN-ZH），但 asymmetry 近零（Δ = +1.2pp, n.s.）。如果 token overlap 或翻译质量驱动 asymmetry，EN-DE 应该显示更大的 asymmetry，但事实相反。

R1 关于 Gemma Δ=+10.3pp 的观察有效——这是三个模型中唯一在 confound 方向的结果。但如 §4.5 所述，Gemma EN→ZH probe 在该层的 baseline accuracy 仅 58.8%（接近 chance），使该分析处于极低功效状态。

**建议**：同意 R1 的建议——(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 将 pipeline 的论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。

### R1-N3: 因果证据限于单模型单层

**[AGREE]** 完全同意，这也是我在 N2 中提出的核心问题。

摘要的叙事结构存在问题：前半段讲跨模型一致的 detectability 和 asymmetry，后半段讲 detection ≠ decision——但后者的正面证据仅来自 Llama L13。读者自然会将两部分理解为同等强度的跨模型发现，但实际不是。

摘要最后一句 "These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance" 确实做了区分，但这个区分出现在一个长摘要的最后，很容易被忽略。

补充 R1 的建议：Introduction 的三个 contributions 中，Contribution 2 写为 "Architecture-dependent causal localization"，这一措辞暗示了跨架构的系统性发现，但实际是 "Llama 有因果效应 + 其他两个没有"。建议改为 "Causal localization in Llama with negative evidence in Qwen and Gemma" 或类似更精确的表述。

---

## Should-Fix 问题

### R1-W1: 单一 train/test split 缺乏 cross-validation

**[AGREE]** 方向上同意，但严重性可略降。

论文在 Limitations 中报告了 cross-seed peak accuracy 稳定性：Llama ±0.12%, Gemma ±1.32%, Qwen ±1.90%。此外，L13 steering 有独立 seed 复制（Appendix C，seed=123，4/6 Bonferroni 显著 vs 原始 2/6）。这些提供了一定的稳健性证据。

但 R1 正确指出，正式的 k-fold cross-validation 未被执行。Bootstrap CI 捕获的是 within-split variability，不是 across-split variability。对于 probing 结论，cross-validation 是标准做法（Belinkov 2022 survey 即推荐），缺失构成方法论缺口。

### R1-W2: Qwen 双重角色

**[AGREE]** 同意这是一个需要更好控制的风险。

我在 Q3 中提出了同样的问题。Qwen EN→ZH transfer accuracy 是三模型最高的（67.3% vs Llama 59.6% vs Gemma 62.9%），虽然差距不大，但方向与 "Qwen 生成的翻译与 Qwen 内部表征自然更 aligned" 的假设一致。

论文的缓解措施（COMET 质量控制 + Llama/Gemma 交叉验证）部分有效，但最干净的控制应该是用独立翻译模型（如 GPT-4 或专用 MT 模型）重做翻译并对比。

### R1-W3: Probe selectivity 未正式评估

**[AGREE]** 这是一个有效的方法论缺口。

论文引用了 Hewitt & Liang (2019) 的 control task 思路（Introduction 第 17 行，Method §3.3），但未实际执行 control task 实验（如随机标签 baseline 或 selectivity 指标）。XNLI baseline 服务于不同目的（测试 asymmetry 的特异性，而非 probe 的 selectivity）。

补充：我在遗漏引用中也指出了 Ravichander et al. (2021) "Probing the Probing Paradigm"，该工作直接论证了 probing accuracy 不意味着 task relevance。本文的核心论点与其高度一致，但既未引用也未执行类似的 selectivity 评估。

### R1-W4: 缺少 AUROC

**[AGREE]** 同意这是一个合理的补充要求。

Balanced accuracy 在单一阈值下操作，AUROC 提供了阈值无关的全面评估。特别是对于 Gemma（88.9% balanced accuracy 但 zero steering flips），AUROC 可以帮助理解 probe 的判别能力是否真的如 balanced accuracy 所暗示的那样强。

但也要注意：balanced accuracy 已经是 class-imbalance-aware 的，且论文的核心论点（detection ≠ causation）不依赖于精确的 probe 性能数值——即使用 AUROC，Gemma 的判别能力大概率仍然很高，而 steering 仍然失败。因此，添加 AUROC 是 good practice，但不会改变核心结论。

### R1-W5: α 值选择缺乏理论依据

**[AGREE]** 同意。

§3.6 描述了 α ∈ {±20, ±10, ±5, ±2, ±1}（10 值）和简化的 {±20, ±10, ±5}（6 值），但未解释为何选择这些特定值。没有基于 probe weight norm、activation magnitude、或 signal-to-noise ratio 的规范化。这使得跨模型的 α 值不可直接比较——同一 α=10 在不同模型/层可能代表截然不同的扰动强度。

建议：用 probe weight 的 norm 或 residual stream 的标准差规范化 α，确保跨模型可比性。

---

## 小问题

**R1-M1 (COMET 版本)**: [AGREE] 需要标注具体版本号（如 wmt22-comet-da 或 Unbabel/wmt22-cometkiwi-da），因为不同版本评分不可比。

**R1-M2 (Token overlap 仅用 Jaccard)**: [AGREE] Jaccard 是粗粒度指标，character-level 或 subword overlap 可能更有信息量。但考虑到 EN-ZH 本身字符系统不同（Latin vs CJK），Jaccard 3-4% 已经足够说明 overlap 极低。

**R1-M3 (代码/数据可用性)**: [AGREE] 当前版本无可用性声明。double-blind 阶段可以用匿名链接。

**R1-M4 (Random direction control 是最低标准)**: [AGREE] 更强的 control 包括：(1) 不同任务的 probe direction（如 XNLI probe weight 用于 conflict steering）；(2) permuted labels 训练的 probe。

**R1-M5 (Figure 3 灰色带暗示 TOST 有效)**: [AGREE] 同意，±2pp 灰色带在视觉上暗示这是一个 meaningful equivalence zone，但 TOST 功效不支持这一暗示。建议删除灰色带或添加注释说明。

---

## 总结

R1 的审稿整体方法论导向，与我的新颖性/完整性评估互补。我们在三个核心问题上高度一致：

1. **"Mirror" claim 过强** — R1 从 TOST power 角度、我从标题-正文一致性角度，结论相同。
2. **因果证据过于局限** — 都认为 1/3 模型正面结果不足以支撑跨架构 claim。
3. **Confound exclusion 需要加强** — R1 聚焦 COMET tercile underpowered，我同意但认为整个 pipeline（包括 token overlap + EN-DE）提供了 converging evidence，总体结论仍可接受。

主要分歧在于 N2 的严重性：R1 认为 confound exclusion "本质上无效"，我认为虽然 COMET tercile 确实 underpowered，但多证据链设计（特别是 EN-DE 对照）部分弥补了这一缺陷。

R1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要来自我对新颖性的更严格评估——R1 未将 Basu et al. (2026) 的先行发现作为核心关注点，而我认为 "detection ≠ decision" 的 novelty 已被显著削弱。综合两份 review，我认为该论文处于 **3.0-3.5 区间**，Findings 接收是合理的，主会议接收需要实质性修改。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-25T04:30:16.822495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-25T04:30:18.230830+00:00_

0	---
1	name: review-director-session-start
2	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
3	priority: 9
4	scope: global
5	tags:
6	- workflow
7	- review
8	- session
9	version: 3
10	roles:
11	- review_director
12	---
13	
14	# Review Director Session 启动流程（圆桌会议模式）
15	
16	## 初始化
17	
18	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
19	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
20	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
21	4. 向用户简要汇报：
22	   - **投稿目标**：venue 和 deadline
23	   - **论文状态**：当前草稿位置和版本
24	   - **资料完整性**：提交的材料是否齐全
25	   - **下一步**：即将开始的圆桌审稿流程
26	
27	## 评审流程（收到论文提交后执行）
28	
29	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
30	
31	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
32	2. 确认目标投稿 venue（从提交消息中获取）
33	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
34	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
35	   - `"&lt;venue name> 2026 submission deadline"`
36	   - `"&lt;venue name> 2026 author guidelines"`
37	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
38	5. 提取当前版本的格式要求：
39	   - 页数限制（正文 / 附录 / 参考文献）
40	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
41	   - 匿名规则（double-blind / single-blind / open）
42	   - 附录规则（是否允许、是否参与审稿）
43	   - 引用格式（natbib / biblatex / 特定 .bst）
44	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
45	
46	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
47	
48	### Step 0.5 — 决定 Reviewer 编排
49	
50	根据 venue 类型和论文特点，决定：
51	- 需要几个 Reviewer（1-5 人）
52	- 每个 Reviewer 的审查侧重
53	
54	参考：
55	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
56	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
57	- **Workshop / 短文**：1 人（全面审查）
58	
59	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
60	
61	### Step 0.6 — 外部审稿线（与 Step 1 并行）
62	
63	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
64	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
65	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
66	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
67	- 如果到 Step
…[truncated 3284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-25T04:30:18.231289+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_visual_check_status,get_external_review_status,update_review_issues,submit_review_report_to_research_director,read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_visual_check_status,get_external_review_status,update_review_issues,submit_review_report_to_research_director,read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-25T04:30:18.281696+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-25T04:30:22.349033+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-25T04:30:22.349467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-25T04:30:26.768772+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-25T04:30:26.819496+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T04:18:33.251063+00:00\", \"completed_at\": \"2026-05-25T04:21:00.757513+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-4\", \"message\": \"连续 2 页纯文本（Related Work + Method 开头），无任何 figure/table/display equation 穿插。Method 3.1 的 Task Formulation 有行内公式但无 display math。建议将核心公式（如 probing formulation）提为 display equation 以打破视觉单调\"}, {\"severity\": \"warning\", \"dimension\": \"pages 7-8\", \"message\": \"Page 7 仅顶部有 Table 3，其余为纯文本；Page 8 整页纯文本（Discussion + Conclusion）。审稿人在此段可能疲劳。若有空间，可考虑将部分 discussion 中的定量对比以小型 inline figure 或 summary table 呈现\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 作为全宽 figure* 内容丰富（4 个子流程），图内标注文字字号偏小（估计 ~6-7pt），打印时可能边缘可读性下降。建议适当增大关键标注字号\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 的三个子图横向压缩，x 轴 tick label 密集。若有空间可考虑略增图宽或减少 tick 密度\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Abstract 段视觉上较长（估计接近 200 words 上限），排版无问题但审稿人第一眼可能觉得 dense\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段 + AI Use 段 + Appendix B/C/D 共处一页，内容紧凑但排版合理，未溢出\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-25T04:30:27.221627+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-25T04:30:27.573430+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-25T04:30:27.573768+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-25T04:30:27.624208+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-25T04:30:30.936753+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file project",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file project",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-25T04:30:31.037687+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-25T04:30:35.160261+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-25T04:30:35.211244+00:00_

1	issues:
2	# === CRITICAL (Must-Fix) — ALL RESOLVED ===
3	
4	- id: "R2-W2"
5	  summary: "标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构成 overclaiming"
6	  category: framing
7	  severity: critical
8	  status: resolved
9	  first_raised_round: 1
10	  last_seen_round: 2
11	  mentions:
12	    - round: 1
13	      reviewers: [2, 1]
14	      note: "R1 AGREE 标题应加限定"
15	    - round: 2
16	      reviewers: [1, 2]
17	      note: "R2 升级为 Must-Fix，R1 交叉 AGREE"
18	  action_items:
19	    - round: 2
20	      action: "标题改为 'English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries'"
21	      assigned_to: paper_agent
22	      status: done
23	  resolution: "Reviewer PASS: 标题准确限定实验范围，正文 cross-lingual 用法均为方法论描述"
24	  resolution_round: 3
25	
26	- id: "MF-2"
27	  summary: "标题 'Inherit' 因果措辞仅有 CI 重叠的相关性证据"
28	  category: framing
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 2
32	  last_seen_round: 2
33	  mentions:
34	    - round: 2
35	      reviewers: [2, 1]
36	      note: "R2 提出，R1 强烈 AGREE"
37	  action_items:
38	    - round: 2
39	      action: "Inherit→Mirror 全文替换 + TOST power + Bayesian BF"
40	      assigned_to: paper_agent
41	      status: done
42	  resolution: "Reviewer PASS: Mirror 准确反映 evidence 强度；TOST power(1.4%)+BF(1.5)+binomial(p=0.016) 三条证据链互补"
43	  resolution_round: 3
44	
45	- id: "R1-N2"
46	  summary: "Detection ≠ Decision 因果声明仅在 Llama 成立"
47	  category: method
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 1
51	  last_seen_round: 2
52	  mentions:
53	    - round: 1
54	      reviewers: [1, 2]
55	      note: "最核心局限"
56	    - round: 2
57	      reviewers: [1, 2]
58	      note: "升级为 MF-3"
59	  action_items:
60	    - round: 2
61	      action: "Reframe 为 architecture-dependent causal localization + seed=123 复现 + informative negatives"
62	      assigned_to: paper_agent
63	      status: done
64	  resolution: "Reviewer PASS: 'emerges' 措辞恰当，Contribution 2 accurately scoped。experiments.tex:165 数据错误已修复。"
65	  resolution_round:
…[truncated 7384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-25T04:32:53.449239+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "clkc_mech_interp",
  "issues_yaml": "issues:\n# === Round 3 NEW ISSUES ===\n\n- id: \"R3-N1\"\n  summary: \"标题 'Mirror' 等价性主张与 TOST 功效(1.4%)不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 提出 TOST power 角度，R2 AGREE 并补充标题-正文一致性问题。BF₀₁≈1.5 仅 modest evidence。建议改 Mirror→Consistent With\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"COMET tercile 消融 MDD=25.3pp 使混淆排除功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 认为'本质上无效'，R2 部分反驳——多证据链(token overlap+EN-DE对照)部分弥补。Gemma Δ=+10.3pp 方向不利。建议补充连续 COMET 回归分析\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"因果证据仅限 Llama L13 单模型单层，不足以支撑跨架构 claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"摘要叙事结构暗示跨模型等强度发现。Contribution 2 措辞 'Architecture-dependent causal localization' 过于模糊。建议改为 Causal localization in Llama with negative evidence in Qwen/Gemma\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"单一 train/test split 缺乏 k-fold cross-validation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Belinkov 2022 推荐 CV 为标准做法。cross-seed ±0.12-1.90% 提供部分稳健性但不替代 CV\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Qwen 同时作为翻译模型和实验对象的双重角色\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen EN→ZH transfer accuracy 最高(67.3%)，与 aligned 假设方向一致。最干净控制需独立翻译模型\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Probe selectivity 未正式评估（无 control task）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"引用 Hewitt & Liang 2019 但未执行。XNLI baseline 服务不同目的。缺 Ravichander 2021 引用\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"缺少 AUROC 阈值无关评估指标\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Balanced accuracy 单阈值。AUROC 对 Gemma(88.9% bal acc + zero steering)尤其有意义。不改变核心结论但为 good practice\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"Steering α 值选择缺乏理论依据和跨模型规范化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"α∈{±20,±10,±5,±2,±1} 无规范化。同一 α 在不同模型/层代表不同扰动强度。建议用 probe weight norm 或 residual stream std 规范化\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"COMET 版本号未标注\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"需标注具体版本如 wmt22-comet-da\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Token overlap 仅用 Jaccard 粗粒度指标\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"EN-ZH 字符系统不同使 3-4% 已足够说明极低 overlap，但 character-level 可更有信息量\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"无代码/数据可用性声明\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"double-blind 阶段可用匿名链接\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Random direction control 仅为最低标准，缺更强 control\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"更强 control: 不同任务 probe direction / permuted labels probe\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Figure 3 灰色带暗示 TOST 有效但功效不支持\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±2pp 灰色带在视觉上暗示 meaningful equivalence zone。建议删除或注释说明\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-NOV\"\n  summary: \"新颖性被 Basu et al. (2026) 先行发现削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 核心关注——detection≠decision 的 novelty 已被 Basu 部分 preempt。R1 未将其列为核心关注点。评分差异主因\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === PREVIOUSLY RESOLVED (Rounds 1-2) ===\n\n- id: \"R2-W2\"\n  summary: \"标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构成 overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加限定\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 升级为 Must-Fix，R1 交叉 AGREE\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 标题准确限定实验范围，正文 cross-lingual 用法均为方法论描述\"\n  resolution_round: 3\n\n- id: \"MF-2\"\n  summary: \"标题 'Inherit' 因果措辞仅有 CI 重叠的相关性证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 强烈 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Inherit→Mirror 全文替换 + TOST power + Bayesian BF\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Mirror 准确反映 evidence 强度；TOST power(1.4%)+BF(1.5)+binomial(p=0.016) 三条证据链互补\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"最核心局限\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 MF-3\"\n  action_items:\n    - round: 2\n      action: \"Reframe 为 architecture-dependent causal localization + seed=123 复现 + informative negatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 'emerges' 措辞恰当，Contribution 2 accurately scoped。experiments.tex:165 数据错误已修复。\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"单种子实验未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致\"\n    - round: 2\n      reviewers: [1]\n      note: \"R1 升级为 Must-Fix\"\n  action_items:\n    - round: 2\n      action: \"Limitations 报告 accuracy stability (±0.12-1.90%) + peak layer sensitivity; seed=123 steering 复现 (4/6 Bonf sig)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"多种子 accuracy 稳定性 + steering 复现数据已加入。Peak layer 变异诚实报告在 Limitations。\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"TOST 等价检验未报告功效\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CI 重叠是必要非充分条件\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"与 MF-2 联动\"\n  action_items:\n    - round: 2\n      action: \"TOST power=1.4% + BF₀₁≈1.5 加入 §4.3\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 表述准确传达 inconclusive but directionally supportive\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 功效不足 + Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"p=0.695/0.761 无法区分无效应和功效不足\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S2\"\n  action_items:\n    - round: 2\n      action: \"MDD=25.3pp + 方向性论证 + Gemma COMET (Δ=+10.3pp, p=0.278, inconclusive)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Gemma 措辞恰当（non-significant trend, near-chance baseline, inconclusive）\"\n  resolution_round: 3\n\n- id: \"SF-4\"\n  summary: \"Qwen/Gemma steering 失败缺乏 mechanistic 分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Discussion 新增 mechanistic 假设段落\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 三个假设合理，引用 Elhage 2022 + Templeton 2024 恰当\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行，未报告重叠度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"建议报告重叠度\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S3\"\n  action_items:\n    - round: 2\n      action: \"3.5% 三重重叠 + pairwise 加入 §4.1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 位置合理，framing 恰当 (independent replication)\"\n  resolution_round: 3\n\n- id: \"SF-6\"\n  summary: \"新颖性定位 vs Zhao et al. 2024\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 认为增量，R1 REBUT\"\n  action_items:\n    - round: 2\n      action: \"Intro 加入 5 点 novelty articulation\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 点独特贡献已加入 Introduction\"\n  resolution_round: 3\n\n- id: \"SF-7\"\n  summary: \"遗漏跨语言 steering 相关工作 3 篇\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 列出 3 篇\"\n  action_items:\n    - round: 2\n      action: \"WebSearch 验证后 5 篇新引用已加入\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 篇新引用全部 WebSearch 验证为真实并加入 Related Work\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 Qwen3-SB 与实验对象 Qwen3-8B 同系列\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"翻译输出可能对 Qwen 有系统性偏好\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 列为 Q4\"\n  action_items:\n    - round: 2\n      action: \"Limitations 讨论\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已在 Limitations 中讨论 Qwen dual role caveat\"\n  resolution_round: 3\n\n- id: \"R1-N1\"\n  summary: \"Steering Bonferroni 校正仅层内应用\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"独立复现部分缓解\"\n  action_items:\n    - round: 1\n      action: \"method.tex 增加 per-layer 独立假设说明 + full family 结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"method.tex + experiments.tex 修复，Round 2 未复发\"\n  resolution_round: 2\n\n- id: \"R2-N2-v1\"\n  summary: \"Qwen3-8B 引用错误\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误\"\n  action_items:\n    - round: 1\n      action: \"替换为 Qwen3 Technical Report\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"yang2024qwen25 → yang2025qwen3\"\n  resolution_round: 2\n\n- id: \"R2-W1-v1\"\n  summary: \"Related Work 遗漏 Meng/Geiger/Turner/Marks\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意必须引用\"\n  action_items:\n    - round: 1\n      action: \"补充 4 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全部 4 篇加入 Related Work\"\n  resolution_round: 2\n\n- id: \"R2-W3-v1\"\n  summary: \"Bib 'and others' 非标准格式\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"ACL 模板要求完整作者列表\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"所有 'and others' 替换为完整作者列表\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 阈值不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一为 p<0.005 (k=10)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"caption 统一为 Bonferroni-corrected p<0.005 (k=10)\"\n  resolution_round: 2\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "clkc_mech_interp",
    "issues_yaml": "issues:\n# === Round 3 NEW ISSUES ===\n\n- id: \"R3-N1\"\n  summary: \"标题 'Mirror' 等价性主张与 TOST 功效(1.4%)不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 提出 TOST power 角度，R2 AGREE 并补充标题-正文一致性问题。BF₀₁≈1.5 仅 modest evidence。建议改 Mirror→Consistent With\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"COMET tercile 消融 MDD=25.3pp 使混淆排除功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 认为'本质上无效'，R2 部分反驳——多证据链(token overlap+EN-DE对照)部分弥补。Gemma Δ=+10.3pp 方向不利。建议补充连续 COMET 回归分析\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"因果证据仅限 Llama L13 单模型单层，不足以支撑跨架构 claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"摘要叙事结构暗示跨模型等强度发现。Contribution 2 措辞 'Architecture-dependent causal localization' 过于模糊。建议改为 Causal localization in Llama with negative evidence in Qwen/Gemma\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"单一 train/test split 缺乏 k-fold cross-validation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Belinkov 2022 推荐 CV 为标准做法。cross-seed ±0.12-1.90% 提供部分稳健性但不替代 CV\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Qwen 同时作为翻译模型和实验对象的双重角色\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen EN→ZH transfer accuracy 最高(67.3%)，与 aligned 假设方向一致。最干净控制需独立翻译模型\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Probe selectivity 未正式评估（无 control task）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"引用 Hewitt & Liang 2019 但未执行。XNLI baseline 服务不同目的。缺 Ravichander 2021 引用\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"缺少 AUROC 阈值无关评估指标\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Balanced accuracy 单阈值。AUROC 对 Gemma(88.9% bal acc + zero steering)尤其有意义。不改变核心结论但为 good practice\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"Steering α 值选择缺乏理论依据和跨模型规范化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"α∈{±20,±10,±5,±2,±1} 无规范化。同一 α 在不同模型/层代表不同扰动强度。建议用 probe weight norm 或 residual stream std 规范化\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"COMET 版本号未标注\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"需标注具体版本如 wmt22-comet-da\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Token overlap 仅用 Jaccard 粗粒度指标\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"EN-ZH 字符系统不同使 3-4% 已足够说明极低 overlap，但 character-level 可更有信息量\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"无代码/数据可用性声明\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"double-blind 阶段可用匿名链接\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Random direction control 仅为最低标准，缺更强 control\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"更强 control: 不同任务 probe direction / permuted labels probe\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Figure 3 灰色带暗示 TOST 有效但功效不支持\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±2pp 灰色带在视觉上暗示 meaningful equivalence zone。建议删除或注释说明\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-NOV\"\n  summary: \"新颖性被 Basu et al. (2026) 先行发现削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 核心关注——detection≠decision 的 novelty 已被 Basu 部分 preempt。R1 未将其列为核心关注点。评分差异主因\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === PREVIOUSLY RESOLVED (Rounds 1-2) ===\n\n- id: \"R2-W2\"\n  summary: \"标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构成 overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加限定\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 升级为 Must-Fix，R1 交叉 AGREE\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 标题准确限定实验范围，正文 cross-lingual 用法均为方法论描述\"\n  resolution_round: 3\n\n- id: \"MF-2\"\n  summary: \"标题 'Inherit' 因果措辞仅有 CI 重叠的相关性证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 强烈 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Inherit→Mirror 全文替换 + TOST power + Bayesian BF\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Mirror 准确反映 evidence 强度；TOST power(1.4%)+BF(1.5)+binomial(p=0.016) 三条证据链互补\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"最核心局限\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 MF-3\"\n  action_items:\n    - round: 2\n      action: \"Reframe 为 architecture-dependent causal localization + seed=123 复现 + informative negatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 'emerges' 措辞恰当，Contribution 2 accurately scoped。experiments.tex:165 数据错误已修复。\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"单种子实验未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致\"\n    - round: 2\n      reviewers: [1]\n      note: \"R1 升级为 Must-Fix\"\n  action_items:\n    - round: 2\n      action: \"Limitations 报告 accuracy stability (±0.12-1.90%) + peak layer sensitivity; seed=123 steering 复现 (4/6 Bonf sig)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"多种子 accuracy 稳定性 + steering 复现数据已加入。Peak layer 变异诚实报告在 Limitations。\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"TOST 等价检验未报告功效\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CI 重叠是必要非充分条件\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"与 MF-2 联动\"\n  action_items:\n    - round: 2\n      action: \"TOST power=1.4% + BF₀₁≈1.5 加入 §4.3\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 表述准确传达 inconclusive but directionally supportive\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 功效不足 + Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"p=0.695/0.761 无法区分无效应和功效不足\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S2\"\n  action_items:\n    - round: 2\n      action: \"MDD=25.3pp + 方向性论证 + Gemma COMET (Δ=+10.3pp, p=0.278, inconclusive)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Gemma 措辞恰当（non-significant trend, near-chance baseline, inconclusive）\"\n  resolution_round: 3\n\n- id: \"SF-4\"\n  summary: \"Qwen/Gemma steering 失败缺乏 mechanistic 分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Discussion 新增 mechanistic 假设段落\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 三个假设合理，引用 Elhage 2022 + Templeton 2024 恰当\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行，未报告重叠度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"建议报告重叠度\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S3\"\n  action_items:\n    - round: 2\n      action: \"3.5% 三重重叠 + pairwise 加入 §4.1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 位置合理，framing 恰当 (independent replication)\"\n  resolution_round: 3\n\n- id: \"SF-6\"\n  summary: \"新颖性定位 vs Zhao et al. 2024\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 认为增量，R1 REBUT\"\n  action_items:\n    - round: 2\n      action: \"Intro 加入 5 点 novelty articulation\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 点独特贡献已加入 Introduction\"\n  resolution_round: 3\n\n- id: \"SF-7\"\n  summary: \"遗漏跨语言 steering 相关工作 3 篇\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 列出 3 篇\"\n  action_items:\n    - round: 2\n      action: \"WebSearch 验证后 5 篇新引用已加入\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 篇新引用全部 WebSearch 验证为真实并加入 Related Work\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 Qwen3-SB 与实验对象 Qwen3-8B 同系列\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"翻译输出可能对 Qwen 有系统性偏好\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 列为 Q4\"\n  action_items:\n    - round: 2\n      action: \"Limitations 讨论\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已在 Limitations 中讨论 Qwen dual role caveat\"\n  resolution_round: 3\n\n- id: \"R1-N1\"\n  summary: \"Steering Bonferroni 校正仅层内应用\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"独立复现部分缓解\"\n  action_items:\n    - round: 1\n      action: \"method.tex 增加 per-layer 独立假设说明 + full family 结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"method.tex + experiments.tex 修复，Round 2 未复发\"\n  resolution_round: 2\n\n- id: \"R2-N2-v1\"\n  summary: \"Qwen3-8B 引用错误\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误\"\n  action_items:\n    - round: 1\n      action: \"替换为 Qwen3 Technical Report\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"yang2024qwen25 → yang2025qwen3\"\n  resolution_round: 2\n\n- id: \"R2-W1-v1\"\n  summary: \"Related Work 遗漏 Meng/Geiger/Turner/Marks\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意必须引用\"\n  action_items:\n    - round: 1\n      action: \"补充 4 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全部 4 篇加入 Related Work\"\n  resolution_round: 2\n\n- id: \"R2-W3-v1\"\n  summary: \"Bib 'and others' 非标准格式\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"ACL 模板要求完整作者列表\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"所有 'and others' 替换为完整作者列表\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 阈值不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一为 p<0.005 (k=10)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"caption 统一为 Bonferroni-corrected p<0.005 (k=10)\"\n  resolution_round: 2\n"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-25T04:32:53.550302+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml\", \"bytes\": 13081}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-25T04:34:42.412019+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 3 审稿报告 — clkc_mech_interp\n\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**交叉回应**: 完成，收敛\n\n---\n\n## Summary\n\n本文研究 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B 中英-中知识冲突信号的线性可探测性与因果相关性。主要发现：(1) 三模型均存在可探测的冲突信号且方向 asymmetry 与已知跨语言能力差异一致；(2) 仅 Llama L13 的 steering 产生显著行为翻转，其他模型未成功——论证 detection ≠ causal relevance。论文经过前两轮审稿的实质性修改，当前版本在 framing 和统计严谨性上有明显进步，但仍存在等价性主张过强、因果证据范围有限、方法论缺口等问题。\n\n---\n\n## Strengths\n\n1. **研究问题有价值**：跨语言知识冲突的 mechanistic 分析是 timely 且重要的方向，连接了 multilingual NLP、knowledge editing 和 interpretability 三个社区。\n\n2. **\"Detection ≠ Decision\" 区分**：明确论证 probing accuracy 不意味着因果相关性，这是对 interpretability 社区的有用 methodological 贡献。Llama 正面结果 + Qwen/Gemma 负面结果的对比设计有说服力。\n\n3. **统计方法多样化**：TOST 等价检验 + Bayesian BF + binomial consistency test + bootstrap CI 的多证据链设计，比单一 p-value 更全面。论文诚实报告了 TOST 功效不足（1.4%），展示了良好的统计诚信。\n\n4. **多证据链混淆排除**：COMET tercile + token overlap + EN-DE typological distance 对照，逻辑结构合理，EN-DE 对照设计巧妙。\n\n5. **经过实质性修改**：相比前版本，Qwen3-8B 引用修正、多种子稳定性报告、mechanistic 假设段落、5 点 novelty articulation 等改进显著。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则不可接收）\n\n**[R3-N1] 标题 \"Mirror\" 等价性主张与统计证据不匹配** [R1 提出, R2 AGREE]\n\nTOST 功效仅 1.4%（需 ±12.5pp margin 才达 80% power），BF₀₁ ≈ 1.5 仅为 \"directionally consistent but modest\"。论文转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但 CI 重叠不等同于等价检验。标题中的 \"Mirror\" 是全文最强的等价性 claim，与正文 \"consistent with\" 的谨慎措辞不一致。Figure 3 的 ±2pp 灰色带在视觉上暗示 TOST 有效但功效不支持。\n\n**建议**：标题改为 \"... Are Consistent With General Cross-Lingual Asymmetries\"；删除或注释 Figure 3 灰色带。\n\n**[R3-N2] COMET tercile 消融 MDD=25.3pp 使该单项分析功效不足** [R1 提出, R2 部分反驳]\n\nMDD=25.3pp 意味着 COMET tercile 分析无法检测到小于 25pp 的真实效应。Gemma Δ=+10.3pp 方向与 confound hypothesis 一致但不显著。R2 反驳称多证据链（token overlap Jaccard 3-4% + EN-DE Δ=+1.2pp n.s.）部分弥补。\n\n**共识建议**：(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。\n\n**[R3-N3] 因果证据限于 Llama L13 单模型单层** [R1 提出, R2 AGREE]\n\n摘要叙事结构前半段跨模型发现 → 后半段因果区分，读者自然理解为同等强度。Contribution 2 \"Architecture-dependent causal localization\" 措辞暗示跨架构系统性发现，实际为 \"Llama 正面 + 其他两个负面\"。\n\n**建议**：Contribution 2 改为 \"Causal localization in Llama with negative evidence in Qwen and Gemma\"；摘要结构更早标注因果结论的范围。\n\n### Should-Fix（不修复降低论文质量但不阻止接收）\n\n**[R3-W1] 单一 train/test split 缺乏 cross-validation** [R1 提出, R2 AGREE]\n\nProbing 领域标准做法为 k-fold CV（Belinkov 2022）。Cross-seed ±0.12-1.90% 和 seed=123 steering 复现提供部分稳健性，但 bootstrap CI 捕获 within-split variability 而非 across-split variability。\n\n**[R3-W2] Qwen 双重角色** [R1 提出, R2 AGREE]\n\nQwen 同时作为翻译模型（生成 ZH 版本）和实验对象。Qwen EN→ZH transfer accuracy 最高（67.3%），方向与 \"翻译输出对 Qwen 自然更 aligned\" 一致。最干净控制需独立翻译模型。\n\n**[R3-W3] Probe selectivity 未正式评估** [R1 提出, R2 AGREE]\n\n引用 Hewitt & Liang (2019) control task 思路但未执行。XNLI baseline 服务不同目的（asymmetry 特异性）。缺少随机标签 baseline 或 selectivity 指标。与 Ravichander et al. (2021) \"Probing the Probing Paradigm\" 高度相关但未引用。\n\n**[R3-W4] 缺少 AUROC** [R1 提出, R2 AGREE]\n\nBalanced accuracy 在单一阈值下操作。AUROC 提供阈值无关评估，对 Gemma（88.9% balanced accuracy + zero steering flips）尤其有诊断价值。不改变核心结论但为方法论 good practice。\n\n**[R3-W5] α 值选择缺乏理论依据** [R1 提出, R2 AGREE]\n\nα ∈ {±20, ±10, ±5, ±2, ±1} 无规范化依据。同一 α=10 在不同模型/层代表不同扰动强度。应用 probe weight norm 或 residual stream std 规范化以确保跨模型可比性。\n\n**[R3-NOV] 新颖性被 Basu et al. (2026) 部分削弱** [R2 提出, R1 未列为核心关注]\n\n\"Detection ≠ decision\" 的核心 insight 已有先行文献。论文需更清晰定位自身相对于 Basu et al. 的增量贡献（跨语言 + 多模型对比 + asymmetry 分析）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. \"Mirror\" 等价性 claim 过强，证据仅支持 \"consistent with\"\n2. 因果证据（steering）仅 Llama L13，不足以支撑跨架构普遍性主张\n3. Probe selectivity 未正式评估是方法论缺口\n4. α 值应规范化\n5. 单一 split 不满足 probing 领域标准\n6. Qwen 双重角色需更好控制或更充分讨论\n7. 所有 minor issues (COMET 版本号/代码可用性/Figure 3 灰色带) 应修复\n\n## Reviewer Divergence [REBUT]\n\n1. **R3-N2 严重性**：R1 认为 COMET tercile \"本质上无效\" → Must-Fix 核心问题；R2 认为虽然 underpowered，但 token overlap + EN-DE 对照的多证据链设计部分弥补，整体 confound exclusion 仍可接受 → 应标注 underpowered 并转移论证重心而非从根本否定\n2. **新颖性评估**：R2 将 Basu et al. (2026) 视为显著削弱 novelty 的先行发现（导致其评分低 0.5 分）；R1 未将其作为核心关注点\n\n---\n\n## Questions for Authors\n\n1. 是否有计划用独立翻译模型（非 Qwen）重做翻译以排除 Qwen 双重角色混淆？\n2. 能否提供 AUROC 数值和 selectivity control task 结果（即使放在 Appendix）？\n3. α 值规范化后，Llama L13 的 steering 效果是否仍然显著？\n4. 连续 COMET score 作为回归变量与 probing accuracy 的关系如何？\n5. Basu et al. (2026) 的发现与本文的具体差异化贡献是什么（beyond 跨语言扩展）？\n\n---\n\n## Missing References\n\n1. **Ravichander et al. (2021)** \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\" — 直接论证 probing accuracy 不意味着 task relevance，与本文核心论点高度相关\n2. **Basu et al. (2026)** — 若论文已引用则需加强差异化讨论；若未引用则为重要遗漏\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~2.5 min)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Pages 3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 figure/table/display equation。建议将核心公式提为 display equation 打破视觉单调 |\n| ⚠️ Warning | Pages 7-8 | Page 7 仅顶部 Table 3，其余纯文本；Page 8 整页纯文本。建议部分 discussion 定量对比以 summary table 呈现 |\n| ℹ️ Info | Page 2 | Figure 1 图内标注文字偏小（~6-7pt），打印边缘可读性可能下降 |\n| ℹ️ Info | Page 5 | Figure 2 三子图横向压缩，x 轴 tick label 密集 |\n| ℹ️ Info | Page 1 | Abstract 视觉上较长（接近 200 words 上限） |\n| ℹ️ Info | Page 9 | Limitations + AI Use + Appendix 共处一页，紧凑但合理 |\n\n统计：0 critical, 2 warning, 4 info。整体排版质量可接受，无严重布局问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings（可被 Findings 接收）**\n\n| Reviewer | 评分 | 核心关注 |\n|----------|------|----------|\n| R1 | 3.5 (Borderline Conference) | 方法严谨性：TOST power / confound exclusion / CV |\n| R2 | 3.0 (Findings) | 新颖性：Basu et al. preemption + 方法论缺口 |\n\n**综合判断**：论文经过三轮修改后在 framing 和统计报告上有显著进步（前两轮所有 issue 已 resolved），研究问题有价值，实验设计整体合理。但当前版本仍有三个 Must-Fix 问题（Mirror overclaim、COMET underpowered、causal scope），五个 Should-Fix 方法论缺口，以及新颖性被先行文献部分削弱。\n\nFindings 接收是合理的——贡献足够但存在实质性改进空间。主会议接收需要：(1) 解决标题/framing 的等价性 overclaim；(2) 补充 AUROC + selectivity control；(3) 明确差异化 vs Basu et al.。\n\n**置信度**：高（双 Reviewer 高度一致，分歧仅在严重性程度而非方向）\n\n---\n\n## Detailed Comments\n\n### Abstract & Introduction\n- Abstract 最后一句对 Llama-only 的限定出现太晚，建议前移\n- Contribution 2 措辞需更精确地反映 \"一正两负\" 的结果模式\n- 需加强 vs Basu et al. (2026) 的差异化定位\n\n### Method (§3)\n- §3.3 引用 Hewitt & Liang 但未执行 → 读者期望被违反\n- §3.6 α 值选择无 justification，跨模型不可比\n- 建议添加 α 规范化公式（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）\n\n### Results (§4)\n- §4.4 TOST 功效 1.4% 的报告是好的实践，但结论部分仍倾向于 positive framing\n- §4.5 COMET tercile 应明确标注为 \"inconclusive due to low power\" 而非现有的偏中性表述\n- 建议添加 Table: AUROC alongside balanced accuracy\n\n### Discussion (§5)\n- Typological distance 段的 EN-DE 对照是 strongest confound evidence — 应更突出\n- Mechanistic 假设段落是好的补充，但与 Basu et al. 的关系未讨论\n\n### Limitations\n- Cross-seed 报告有效但不替代正式 CV\n- Qwen dual role caveat 可更 prominently 呈现（当前为最后一点）\n\n### Format\n- COMET 版本号缺失\n- 无代码/数据可用性声明\n- Figure 3 灰色带误导性",
  "project": "clkc_mech_interp",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 3 审稿报告 — clkc_mech_interp\n\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**交叉回应**: 完成，收敛\n\n---\n\n## Summary\n\n本文研究 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B 中英-中知识冲突信号的线性可探测性与因果相关性。主要发现：(1) 三模型均存在可探测的冲突信号且方向 asymmetry 与已知跨语言能力差异一致；(2) 仅 Llama L13 的 steering 产生显著行为翻转，其他模型未成功——论证 detection ≠ causal relevance。论文经过前两轮审稿的实质性修改，当前版本在 framing 和统计严谨性上有明显进步，但仍存在等价性主张过强、因果证据范围有限、方法论缺口等问题。\n\n---\n\n## Strengths\n\n1. **研究问题有价值**：跨语言知识冲突的 mechanistic 分析是 timely 且重要的方向，连接了 multilingual NLP、knowledge editing 和 interpretability 三个社区。\n\n2. **\"Detection ≠ Decision\" 区分**：明确论证 probing accuracy 不意味着因果相关性，这是对 interpretability 社区的有用 methodological 贡献。Llama 正面结果 + Qwen/Gemma 负面结果的对比设计有说服力。\n\n3. **统计方法多样化**：TOST 等价检验 + Bayesian BF + binomial consistency test + bootstrap CI 的多证据链设计，比单一 p-value 更全面。论文诚实报告了 TOST 功效不足（1.4%），展示了良好的统计诚信。\n\n4. **多证据链混淆排除**：COMET tercile + token overlap + EN-DE typological distance 对照，逻辑结构合理，EN-DE 对照设计巧妙。\n\n5. **经过实质性修改**：相比前版本，Qwen3-8B 引用修正、多种子稳定性报告、mechanistic 假设段落、5 点 novelty articulation 等改进显著。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则不可接收）\n\n**[R3-N1] 标题 \"Mirror\" 等价性主张与统计证据不匹配** [R1 提出, R2 AGREE]\n\nTOST 功效仅 1.4%（需 ±12.5pp margin 才达 80% power），BF₀₁ ≈ 1.5 仅为 \"directionally consistent but modest\"。论文转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但 CI 重叠不等同于等价检验。标题中的 \"Mirror\" 是全文最强的等价性 claim，与正文 \"consistent with\" 的谨慎措辞不一致。Figure 3 的 ±2pp 灰色带在视觉上暗示 TOST 有效但功效不支持。\n\n**建议**：标题改为 \"... Are Consistent With General Cross-Lingual Asymmetries\"；删除或注释 Figure 3 灰色带。\n\n**[R3-N2] COMET tercile 消融 MDD=25.3pp 使该单项分析功效不足** [R1 提出, R2 部分反驳]\n\nMDD=25.3pp 意味着 COMET tercile 分析无法检测到小于 25pp 的真实效应。Gemma Δ=+10.3pp 方向与 confound hypothesis 一致但不显著。R2 反驳称多证据链（token overlap Jaccard 3-4% + EN-DE Δ=+1.2pp n.s.）部分弥补。\n\n**共识建议**：(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。\n\n**[R3-N3] 因果证据限于 Llama L13 单模型单层** [R1 提出, R2 AGREE]\n\n摘要叙事结构前半段跨模型发现 → 后半段因果区分，读者自然理解为同等强度。Contribution 2 \"Architecture-dependent causal localization\" 措辞暗示跨架构系统性发现，实际为 \"Llama 正面 + 其他两个负面\"。\n\n**建议**：Contribution 2 改为 \"Causal localization in Llama with negative evidence in Qwen and Gemma\"；摘要结构更早标注因果结论的范围。\n\n### Should-Fix（不修复降低论文质量但不阻止接收）\n\n**[R3-W1] 单一 train/test split 缺乏 cross-validation** [R1 提出, R2 AGREE]\n\nProbing 领域标准做法为 k-fold CV（Belinkov 2022）。Cross-seed ±0.12-1.90% 和 seed=123 steering 复现提供部分稳健性，但 bootstrap CI 捕获 within-split variability 而非 across-split variability。\n\n**[R3-W2] Qwen 双重角色** [R1 提出, R2 AGREE]\n\nQwen 同时作为翻译模型（生成 ZH 版本）和实验对象。Qwen EN→ZH transfer accuracy 最高（67.3%），方向与 \"翻译输出对 Qwen 自然更 aligned\" 一致。最干净控制需独立翻译模型。\n\n**[R3-W3] Probe selectivity 未正式评估** [R1 提出, R2 AGREE]\n\n引用 Hewitt & Liang (2019) control task 思路但未执行。XNLI baseline 服务不同目的（asymmetry 特异性）。缺少随机标签 baseline 或 selectivity 指标。与 Ravichander et al. (2021) \"Probing the Probing Paradigm\" 高度相关但未引用。\n\n**[R3-W4] 缺少 AUROC** [R1 提出, R2 AGREE]\n\nBalanced accuracy 在单一阈值下操作。AUROC 提供阈值无关评估，对 Gemma（88.9% balanced accuracy + zero steering flips）尤其有诊断价值。不改变核心结论但为方法论 good practice。\n\n**[R3-W5] α 值选择缺乏理论依据** [R1 提出, R2 AGREE]\n\nα ∈ {±20, ±10, ±5, ±2, ±1} 无规范化依据。同一 α=10 在不同模型/层代表不同扰动强度。应用 probe weight norm 或 residual stream std 规范化以确保跨模型可比性。\n\n**[R3-NOV] 新颖性被 Basu et al. (2026) 部分削弱** [R2 提出, R1 未列为核心关注]\n\n\"Detection ≠ decision\" 的核心 insight 已有先行文献。论文需更清晰定位自身相对于 Basu et al. 的增量贡献（跨语言 + 多模型对比 + asymmetry 分析）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. \"Mirror\" 等价性 claim 过强，证据仅支持 \"consistent with\"\n2. 因果证据（steering）仅 Llama L13，不足以支撑跨架构普遍性主张\n3. Probe selectivity 未正式评估是方法论缺口\n4. α 值应规范化\n5. 单一 split 不满足 probing 领域标准\n6. Qwen 双重角色需更好控制或更充分讨论\n7. 所有 minor issues (COMET 版本号/代码可用性/Figure 3 灰色带) 应修复\n\n## Reviewer Divergence [REBUT]\n\n1. **R3-N2 严重性**：R1 认为 COMET tercile \"本质上无效\" → Must-Fix 核心问题；R2 认为虽然 underpowered，但 token overlap + EN-DE 对照的多证据链设计部分弥补，整体 confound exclusion 仍可接受 → 应标注 underpowered 并转移论证重心而非从根本否定\n2. **新颖性评估**：R2 将 Basu et al. (2026) 视为显著削弱 novelty 的先行发现（导致其评分低 0.5 分）；R1 未将其作为核心关注点\n\n---\n\n## Questions for Authors\n\n1. 是否有计划用独立翻译模型（非 Qwen）重做翻译以排除 Qwen 双重角色混淆？\n2. 能否提供 AUROC 数值和 selectivity control task 结果（即使放在 Appendix）？\n3. α 值规范化后，Llama L13 的 steering 效果是否仍然显著？\n4. 连续 COMET score 作为回归变量与 probing accuracy 的关系如何？\n5. Basu et al. (2026) 的发现与本文的具体差异化贡献是什么（beyond 跨语言扩展）？\n\n---\n\n## Missing References\n\n1. **Ravichander et al. (2021)** \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\" — 直接论证 probing accuracy 不意味着 task relevance，与本文核心论点高度相关\n2. **Basu et al. (2026)** — 若论文已引用则需加强差异化讨论；若未引用则为重要遗漏\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~2.5 min)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Pages 3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 figure/table/display equation。建议将核心公式提为 display equation 打破视觉单调 |\n| ⚠️ Warning | Pages 7-8 | Page 7 仅顶部 Table 3，其余纯文本；Page 8 整页纯文本。建议部分 discussion 定量对比以 summary table 呈现 |\n| ℹ️ Info | Page 2 | Figure 1 图内标注文字偏小（~6-7pt），打印边缘可读性可能下降 |\n| ℹ️ Info | Page 5 | Figure 2 三子图横向压缩，x 轴 tick label 密集 |\n| ℹ️ Info | Page 1 | Abstract 视觉上较长（接近 200 words 上限） |\n| ℹ️ Info | Page 9 | Limitations + AI Use + Appendix 共处一页，紧凑但合理 |\n\n统计：0 critical, 2 warning, 4 info。整体排版质量可接受，无严重布局问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings（可被 Findings 接收）**\n\n| Reviewer | 评分 | 核心关注 |\n|----------|------|----------|\n| R1 | 3.5 (Borderline Conference) | 方法严谨性：TOST power / confound exclusion / CV |\n| R2 | 3.0 (Findings) | 新颖性：Basu et al. preemption + 方法论缺口 |\n\n**综合判断**：论文经过三轮修改后在 framing 和统计报告上有显著进步（前两轮所有 issue 已 resolved），研究问题有价值，实验设计整体合理。但当前版本仍有三个 Must-Fix 问题（Mirror overclaim、COMET underpowered、causal scope），五个 Should-Fix 方法论缺口，以及新颖性被先行文献部分削弱。\n\nFindings 接收是合理的——贡献足够但存在实质性改进空间。主会议接收需要：(1) 解决标题/framing 的等价性 overclaim；(2) 补充 AUROC + selectivity control；(3) 明确差异化 vs Basu et al.。\n\n**置信度**：高（双 Reviewer 高度一致，分歧仅在严重性程度而非方向）\n\n---\n\n## Detailed Comments\n\n### Abstract & Introduction\n- Abstract 最后一句对 Llama-only 的限定出现太晚，建议前移\n- Contribution 2 措辞需更精确地反映 \"一正两负\" 的结果模式\n- 需加强 vs Basu et al. (2026) 的差异化定位\n\n### Method (§3)\n- §3.3 引用 Hewitt & Liang 但未执行 → 读者期望被违反\n- §3.6 α 值选择无 justification，跨模型不可比\n- 建议添加 α 规范化公式（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）\n\n### Results (§4)\n- §4.4 TOST 功效 1.4% 的报告是好的实践，但结论部分仍倾向于 positive framing\n- §4.5 COMET tercile 应明确标注为 \"inconclusive due to low power\" 而非现有的偏中性表述\n- 建议添加 Table: AUROC alongside balanced accuracy\n\n### Discussion (§5)\n- Typological distance 段的 EN-DE 对照是 strongest confound evidence — 应更突出\n- Mechanistic 假设段落是好的补充，但与 Basu et al. 的关系未讨论\n\n### Limitations\n- Cross-seed 报告有效但不替代正式 CV\n- Qwen dual role caveat 可更 prominently 呈现（当前为最后一点）\n\n### Format\n- COMET 版本号缺失\n- 无代码/数据可用性声明\n- Figure 3 灰色带误导性",
    "project": "clkc_mech_interp",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-25T04:34:46.685047+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6951eb3869a0070e3ae607ab60c90dad:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4273
}
```

</details>

---


### Assistant

_source line 322 · 2026-05-25T04:34:57.352565+00:00_

---

**Round 3 审稿报告已投递。**

**收敛结果**：双 Reviewer 在所有核心问题上达成一致，仅在 COMET tercile 严重性和新颖性评估上存在程度差异（非方向性分歧）。

**评分**：R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings) → 综合 **3.0 (Findings)**

**本轮新 issue 统计**：3 critical (open) + 6 warning (open) + 5 info (open)
**前轮 issue 状态**：全部 resolved，无复发

核心修改要求：
1. 标题 "Mirror" → "Consistent With"（等价性证据不足）
2. COMET tercile 标注 underpowered + 补充连续回归
3. Contribution 2 精确化因果 scope

报告已送达 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 23

## Round 23

14 recorded events


### User

_source line 323 · 2026-05-25T04:34:58.466214+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条交叉回应。

核心共识：R1-N1（Mirror claim 过强）、R1-N3（因果证据限于 Llama）两点完全同意。唯一分歧在 R1-N2——COMET tercile 确实 underpowered，但反驳了 "本质上无效" 的结论，因为 token overlap + EN-DE 对照提供了 converging evidence。综合两份 review，论文处于 3.0-3.5 区间。

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix 问题

**[AGREE] R2-N1: "Detection ≠ Decision" 增量贡献不足**

同意核心判断，但需补充两点 nuance。

同意理由：Basu et al. (2026) 已在单语临床 NLP 场景中建立了 "98.2% AUROC + steering 完全失败" 的范例。本文 Contribution 5（"detectability does not predict causal relevance"）确实是对已知原则的重复验证而非新发现。Section 1 第二段明确引用了 Basu et al. 的结论，这进一步表明作者自己也意识到这不是新洞察。

但需要区分两个层面：(a) 作为独立 contribution 的 "detection ≠ decision" 原则——确实增量有限；(b) 在跨语言场景下的具体实例化——引入了单语场景不存在的混淆因素（翻译质量、token overlap、语言不对称），因此实验设计有独立价值。建议作者将 Contribution 5 合并到 Contribution 2/4 中作为支撑证据，而非独立贡献点。

**[AGREE] R2-N2: Contribution 2 证据过弱**

强烈同意。这与我的 N3 一致。

补充发现：论文 Section 5 第三段对 Qwen/Gemma steering 失败给出三个假说（causal pathway 非线性、residual stream superposition、architectural differences），但三者均无任何初步验证。更严重的是，论文在 Page 2 将 "Architecture-dependent causal localization" 列为五个贡献之一，但 "architecture-dependent" 这一修饰语暗示了跨架构的系统性比较发现，而实际情况是：一个正面结果（Llama L13, p=0.002）加两个 null（Qwen best p=0.785, Gemma best p=0.148）。

R2 提出的修改建议合理——降级为 "exploratory finding" 或提供假说的初步验证。我补充建议：如果保留此贡献，至少需要对 Qwen/Gemma 进行更精细的因果分析（如 activation patching），而非仅依赖 steering 这一单一方法。Steering 失败可能反映方法局限而非模型缺乏因果结构。

---

## Should-Fix 问题

**[REBUT] R2-W1: 跨语言可检测性是 "expected result"**

R2 的推理链（"单语可检测 + 共享空间 → 跨语言可检测"）在直觉上合理，但过于简化，忽略了论文的关键实证贡献。

反驳证据：

1. **方向性不对称是非平凡的**：如果跨语言可检测性仅仅是共享空间的推论，那么预期应该是对称的迁移。但论文发现 ZH→EN 迁移比 EN→ZH 高约 7pp（Table 1: Δ_asym = +7.3pp for Llama [0.4, 14.0], +7.2pp for Qwen, +6.6pp for Gemma [1.9, 11.1]），且这一不对称跨三个架构方向一致。这不是 "expected" 的。

2. **XNLI 基线不是 "null result"**：R2 称 "XNLI baseline 表明不对称不是冲突特异的——本质上是 null result"。我不同意这一定性。XNLI 基线显示非冲突任务也存在相同方向的不对称（Section 4.4, Figure 3），这是一个**正面发现**——它将观测到的不对称归因到通用跨语言结构而非冲突编码的特异性。这一归因本身是有信息量的，排除了 "冲突信号有独特跨语言编码" 这一替代假说。

3. **共享空间不保证线性可分**：跨语言共享空间的存在不意味着任务相关信号在该空间中是线性可分的。信号可能以非线性方式编码，或被语言特异性噪声掩盖。实证验证仍有价值。

因此，虽然可检测性本身可能是预期的，但方向性不对称及其与通用跨语言结构的对应关系是论文的真正贡献，不能简单归为 "expected"。

**[AGREE] R2-W2: 过度 Llama-centric**

同意，与我的 N3 观点一致。Probing 三模型一致这一优势被 steering 的 Llama-only 叙事削弱。论文的主要叙事弧线（Abstract → Introduction → Discussion）在不经意间给出了三模型对等发现的印象，但 Section 5 的实质讨论几乎全部围绕 Llama L13 展开。

**[REBUT] R2-W3: 遗漏关键相关工作（部分同意、部分反驳）**

需要分开讨论三篇引用：

1. **Pimentel & Cotterell (2021)** — [AGREE]：information-theoretic probing 框架对本文的 probe methodology 讨论是相关的。论文使用线性 probe 但未讨论信息论替代框架，补充引用合理。

2. **Ravichander et al. (2021)** — [AGREE with caveat]：如果该论文确实讨论了 probing accuracy 与 task relevance 的脱节，则与本文主题相关。但建议 R2 确认此引用的准确性（标题、年份、venue），避免引入不存在的文献。

3. **Gurgurov et al. (2026) "CLaS-Bench"** — [REBUT]：这是一篇据称 2026 年的论文。在双盲审稿中，我无法验证此文献是否已公开发表或可获取。如果这是一篇尚未正式发表的 preprint，要求作者引用它的合理性取决于其公开时间是否早于本文投稿截止日。此外，如果 CLaS-Bench 确实是跨语言 steering 的 benchmark，本文的 steering 实验设计（基于 probe direction 注入）与 benchmark 评测是不同的研究取向——遗漏引用可能影响完整性但不影响方法论有效性。

**[AGREE] R2-W4: Discussion 假说过于投机**

同意。Section 5 "Why does steering fail in Qwen and Gemma?" 提出三个假说但全部 untested。学术论文中提出未验证假说本身是允许的，但当这些假说用于支撑一个被列为独立贡献的发现时（Contribution 2: "Architecture-dependent causal localization"），要求更高的证据标准是合理的。

建议：至少对假说 1（"causal pathway may involve non-linear interactions"）进行初步验证——例如检查 Qwen/Gemma 在 L13 附近的 probe direction 与 steering direction 之间的余弦相似度，或比较线性 vs 非线性 probe 的精度差异。

---

## 小问题

**[AGREE] R2-M1**: Abstract 198 words 确实接近 200-word 上限但在合规范围内，不构成问题。

**[AGREE] R2-M2**: Table 1 脚注（"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies"）确实重要但容易被忽略。建议移入正文 Section 4.3 的段落中。

**[AGREE] R2-M3**: Gemma COMET tercile Δ=+10.3pp 应在 Limitations 更明确讨论。这与我的 N2 一致——这一效应大小接近主效应（~7pp），在 Limitations 中仅被 COMET 分析的整体无显著性掩盖了。

**[REBUT] R2-M4**: Figure 1 信息量偏低——我不完全同意。Figure 1 作为 pipeline overview figure 承担的是导航功能而非信息密度。对于一篇方法流程较复杂的论文（data construction → probing → steering → confound exclusion），一个清晰的概览图有助于读者快速理解实验设计。不过同意可以在图中补充更多细节（如样本量、关键超参数）以提高信息密度。

**[AGREE] R2-M5**: AI Use 措辞简短，但 ARR 对此部分无字数要求，不构成格式问题。

**[AGREE] R2-M6**: Marks & Tegmark (2024) 的 venue 应由作者核实。引用准确性是基本要求。

---

## 对 R2 总体评分的看法

R2 给出 3.0（Findings）。结合我的评估（3.5, Borderline Conference），我认为合理区间在 3.0–3.5 之间。

R2 的核心论点——贡献增量性不足——有一定道理，但 R2 低估了方向性不对称发现和混淆排除管线的实验设计价值。如果作者能 (a) 将 "detection ≠ decision" 从独立贡献降级为支撑证据，(b) 将 "architecture-dependent causal localization" 降级为 exploratory finding，(c) 强化标题中 "mirror" 的统计支撑，论文的贡献定位会更诚实，也更有说服力。当前版本的主要问题不是工作质量差，而是 claims 的范围超出了证据的支撑范围。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1 (Detection≠Decision 增量不足)**: [AGREE]，但指出跨语言维度的混淆排除设计有独立价值，建议将其从独立贡献合并为支撑证据
- **R2-N2 (Causal localization 证据弱)**: [AGREE]，与我的 N3 一致，补充建议尝试 activation patching 等替代因果方法
- **R2-W1 (跨语言可检测是 expected)**: [REBUT]，方向性不对称（~7pp, 三模型一致）不可从 "共享空间" 直接推出；XNLI 基线是正面发现而非 null result
- **R2-W2 (Llama-centric)**: [AGREE]
- **R2-W3 (遗漏引用)**: 部分同意 Pimentel & Cotterell，反驳 Gurgurov et al. (2026) 的引用要求需先确认其公开可获取性
- **R2-W4 (投机假说)**: [AGREE]，建议至少提供一个假说的初步验证
- 总体评分区间 3.0–3.5，核心问题是 claims 范围超出证据支撑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-25T04:37:45.953088+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 3 审稿报告 — clkc_mech_interp\n\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**交叉回应**: 完成，收敛（1 轮交叉即达共识）\n\n---\n\n## Summary\n\n本文研究 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B 中英-中知识冲突信号的线性可探测性与因果相关性。主要发现：(1) 三模型均存在可探测的冲突信号且方向 asymmetry（ZH→EN 比 EN→ZH 高约 7pp）与已知跨语言能力差异一致；(2) 仅 Llama L13 的 steering 产生显著行为翻转，Qwen/Gemma 未成功——论证 detection ≠ causal relevance。论文经过前两轮审稿的实质性修改（前轮所有 issue 已 resolved），当前版本在 framing 和统计严谨性上有明显进步，但仍存在等价性主张过强、因果证据范围有限、贡献定位与证据强度不匹配等问题。\n\n---\n\n## Strengths\n\n1. **研究问题有价值**：跨语言知识冲突的 mechanistic 分析连接 multilingual NLP、knowledge editing 和 interpretability 三个社区，是 timely 且重要的方向。\n\n2. **方向性不对称是非平凡发现**：ZH→EN 迁移比 EN→ZH 高约 7pp，三模型方向一致（Llama +7.3pp [0.4, 14.0]，Qwen +7.2pp，Gemma +6.6pp [1.9, 11.1]）。这不能从 \"共享空间存在\" 直接推出——共享空间不保证对称迁移，不保证线性可分性。XNLI 基线显示非冲突任务也存在相同方向不对称，将观测归因到通用跨语言结构而非冲突特异编码——这是一个正面发现（排除了替代假说），而非 null result。\n\n3. **\"Detection ≠ Decision\" 区分**：Llama 正面结果 + Qwen/Gemma 负面结果的对比设计论证 probing accuracy 不意味着因果相关性。虽然原则已有先行文献（Basu et al. 2026），但跨语言场景引入的混淆排除设计有独立实验价值。\n\n4. **统计方法多样化**：TOST + Bayesian BF + binomial + bootstrap CI 多证据链，论文诚实报告 TOST 功效不足（1.4%），展示统计诚信。\n\n5. **多证据链混淆排除**：COMET tercile + token overlap (Jaccard 3-4%) + EN-DE 对照（Jaccard 14.8% 但 Δ=+1.2pp n.s.），EN-DE 对照设计巧妙且有力。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则不可接收）\n\n**[R3-N1] 标题 \"Mirror\" 等价性主张与统计证据不匹配** [R1 提出, R2 AGREE]\n\nTOST 功效仅 1.4%（需 ±12.5pp margin 才达 80% power），BF₀₁ ≈ 1.5 仅 \"directionally consistent but modest\"。论文转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但 CI 重叠不等同于等价检验。标题中 \"Mirror\" 是全文最强等价性 claim，与正文 \"consistent with\" 的谨慎措辞不一致。Figure 3 的 ±2pp 灰色带视觉暗示 TOST 有效但功效不支持。\n\n**建议**：标题改为 \"... Are Consistent With General Cross-Lingual Asymmetries\"；删除或注释 Figure 3 灰色带。\n\n**[R3-N2] COMET tercile 消融 MDD=25.3pp 功效不足** [R1 提出, R2 部分反驳]\n\nMDD=25.3pp 意味着该分析无法检测 <25pp 真实效应。Gemma Δ=+10.3pp 方向与 confound hypothesis 一致但不显著（应在 Limitations 更明确讨论，而非仅被整体无显著性掩盖）。R2 反驳称多证据链（token overlap + EN-DE 对照）部分弥补——特别是 EN-DE 对照：token overlap 4× 于 EN-ZH 但 asymmetry 近零，如果 overlap 驱动 asymmetry 应该在 EN-DE 更强但事实相反。\n\n**共识建议**：(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。\n\n**[R3-N3] 因果证据限于 Llama L13，贡献定位过强** [R1 提出, R2 AGREE]\n\nContribution 2 \"Architecture-dependent causal localization\" 暗示跨架构系统性比较发现，实际为一个正面结果（Llama L13, p=0.002）加两个 null（Qwen best p=0.785, Gemma best p=0.148）。Section 5 三个假说（非线性交互、superposition、架构差异）全部 untested。当假说用于支撑独立贡献时，证据标准需更高。\n\n**建议**：(1) Contribution 2 改为 \"Causal localization in Llama with negative evidence in Qwen and Gemma\"，降级为 exploratory finding；(2) 至少对一个假说提供初步验证（如 Qwen/Gemma L13 probe direction vs steering direction 余弦相似度，或线性 vs 非线性 probe 精度对比）；(3) 考虑 activation patching 等替代因果方法——steering 失败可能反映方法局限而非模型缺乏因果结构。\n\n### Should-Fix（不修复降低论文质量但不阻止接收）\n\n**[R3-W1] 单一 train/test split 缺乏 cross-validation** [R1 提出, R2 AGREE]\n\nProbing 领域标准做法为 k-fold CV（Belinkov 2022）。Cross-seed ±0.12-1.90% 和 seed=123 steering 复现提供部分稳健性，但 bootstrap CI 捕获 within-split variability 而非 across-split variability。\n\n**[R3-W2] Qwen 双重角色** [R1 提出, R2 AGREE]\n\nQwen 同时作为翻译模型和实验对象。Qwen EN→ZH transfer accuracy 最高（67.3%），方向与 \"翻译输出对 Qwen 自然更 aligned\" 一致。最干净控制需独立翻译模型。\n\n**[R3-W3] Probe selectivity 未正式评估** [R1 提出, R2 AGREE]\n\n引用 Hewitt & Liang (2019) control task 思路但未执行。缺少随机标签 baseline 或 selectivity 指标。与 Ravichander et al. (2021) \"Probing the Probing Paradigm\" 高度相关但未引用。\n\n**[R3-W4] 缺少 AUROC** [R1 提出, R2 AGREE]\n\nBalanced accuracy 在单一阈值下操作。AUROC 对 Gemma（88.9% bal acc + zero steering flips）尤其有诊断价值——帮助理解 probe 判别能力是否真如 bal acc 暗示的那样强。\n\n**[R3-W5] α 值选择缺乏理论依据** [R1 提出, R2 AGREE]\n\nα ∈ {±20, ±10, ±5, ±2, ±1} 无规范化。同一 α 在不同模型/层代表不同扰动强度。应用 probe weight norm 或 residual stream std 规范化（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）。\n\n**[R3-NOV] 新颖性被 Basu et al. (2026) 部分削弱** [R2 提出, R1 AGREE with nuance]\n\n\"Detection ≠ decision\" 原则作为独立贡献增量有限（Basu 2026 已建立 98.2% AUROC + steering 完全失败的先例）。但 R1 指出跨语言维度的混淆排除设计有独立价值。\n\n**建议**：将 Contribution 5 (\"detectability does not predict causal relevance\") 合并到 Contribution 2/4 中作为支撑证据，而非独立贡献点。保留跨语言实例化的实验设计价值，但不重复 claim 已知原则。\n\n**[R3-W6] Discussion 假说过于投机** [R2 提出, R1 AGREE]\n\n三个假说全部 untested。建议至少提供一个假说的初步验证——如检查 probe direction 与 residual stream 主成分的对齐度，或比较线性 vs 非线性 probe 精度差异。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. \"Mirror\" 等价性 claim 过强，证据仅支持 \"consistent with\"\n2. 因果证据（steering）仅 Llama L13，不足以支撑跨架构普遍性主张\n3. Contribution 2 应降级为 exploratory finding\n4. Contribution 5 应合并而非独立列出\n5. Probe selectivity 未正式评估是方法论缺口\n6. α 值应规范化\n7. 单一 split 不满足 probing 领域标准\n8. Qwen 双重角色需更好控制或更充分讨论\n9. Discussion 假说至少需一个初步验证\n10. 所有 minor issues (COMET 版本号/代码可用性/Figure 3 灰色带) 应修复\n\n## Reviewer Divergence [REBUT]\n\n1. **R3-N2 严重性**：R1 认为 COMET tercile \"本质上无效\"；R2 认为 token overlap + EN-DE 对照部分弥补，整体 confound exclusion 仍可接受。**Director 判断**：R2 的论证更有说服力——EN-DE 对照是独立的强证据，但 COMET tercile 本身确实应标注为 underpowered。\n\n2. **跨语言可检测性是否 \"expected\"**：R2 认为这是共享空间的自然推论，增量有限；R1 REBUT 指出方向性不对称（~7pp）不可直接推出，XNLI 基线是正面发现（归因到通用跨语言结构）而非 null result，共享空间不保证线性可分。**Director 判断**：R1 论证有力——asymmetry 确实是 non-trivial empirical finding，但论文需要更清晰地将 asymmetry（而非 detectability 本身）定位为核心贡献。\n\n3. **Gurgurov et al. (2026) 引用要求**：R2 列为遗漏引用；R1 质疑该文献在双盲截止前是否可公开获取。**Director 判断**：作者需验证该文献的公开时间线，如在投稿前可获取则应引用。\n\n---\n\n## Questions for Authors\n\n1. 是否有计划用独立翻译模型（非 Qwen）重做翻译以排除 Qwen 双重角色混淆？\n2. 能否提供 AUROC 数值和 selectivity control task 结果（即使放在 Appendix）？\n3. α 值规范化后，Llama L13 的 steering 效果是否仍然显著？\n4. 连续 COMET score 作为回归变量与 probing accuracy 的关系如何？\n5. Basu et al. (2026) 的发现与本文的具体差异化贡献是什么（beyond 跨语言扩展）？\n6. 能否对 Section 5 三个假说中至少一个提供初步验证数据？\n7. Qwen/Gemma steering 失败是否可能是方法局限（如 activation patching 是否会给出不同结论）？\n\n---\n\n## Missing References\n\n1. **Ravichander et al. (2021)** \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\" — 直接论证 probing accuracy 不意味着 task relevance，与本文核心论点高度相关\n2. **Pimentel & Cotterell (2021)** — information-theoretic probing 框架，与本文 probe methodology 讨论相关\n3. **Gurgurov et al. (2026) \"CLaS-Bench\"** — 跨语言 steering benchmark（需验证公开可获取性，若投稿前已公开则应引用）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~2.5 min)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Pages 3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 figure/table/display equation。建议将核心公式提为 display equation 打破视觉单调 |\n| ⚠️ Warning | Pages 7-8 | Page 7 仅顶部 Table 3，其余纯文本；Page 8 整页纯文本。建议部分 discussion 定量对比以 summary table 呈现 |\n| ℹ️ Info | Page 2 | Figure 1 图内标注文字偏小（~6-7pt），打印边缘可读性可能下降 |\n| ℹ️ Info | Page 5 | Figure 2 三子图横向压缩，x 轴 tick label 密集 |\n| ℹ️ Info | Page 1 | Abstract 视觉上较长（接近 200 words 上限） |\n| ℹ️ Info | Page 9 | Limitations + AI Use + Appendix 共处一页，紧凑但合理 |\n\n统计：0 critical, 2 warning, 4 info。整体排版质量可接受，无严重布局问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings（可被 Findings 接收）**\n\n| Reviewer | 评分 | 核心关注 |\n|----------|------|----------|\n| R1 | 3.5 (Borderline Conference) | 方法严谨性：TOST power / confound exclusion / CV；但认可 asymmetry 为 non-trivial 贡献 |\n| R2 | 3.0 (Findings) | 新颖性：Basu et al. preemption + 贡献定位过强 |\n\n**综合判断**：论文经过三轮修改后在 framing 和统计报告上有显著进步（前两轮所有 issue 已 resolved），研究问题有价值，实验设计整体合理。方向性不对称（~7pp, 三模型一致）是非平凡的实证贡献，混淆排除管线设计（特别是 EN-DE 对照）展示了实验功力。\n\n但当前版本的核心问题是 **claims 范围超出证据支撑**：(1) \"Mirror\" 标题暗示等价但 TOST 无功效；(2) Contribution 2 暗示跨架构系统性发现但实为 1 正 2 负；(3) Contribution 5 重复已知原则。如果作者将贡献重新定位为 \"(a) 跨语言冲突信号的方向性不对称 + (b) Llama 特异性因果定位 + (c) 混淆排除方法论\"，论文的贡献-证据匹配度会大幅改善。\n\nFindings 接收合理——贡献足够但存在实质性改进空间。主会议接收需要：(1) 解决标题/贡献的 overclaim；(2) 补充 AUROC + selectivity control + α 规范化；(3) 对至少一个 mechanistic 假说提供初步验证；(4) 明确差异化 vs Basu et al.。\n\n**置信度**：高（双 Reviewer 在核心问题上高度一致，分歧均在严重性程度而非方向）\n\n---\n\n## Detailed Comments\n\n### Abstract & Introduction\n- Abstract 最后一句对 Llama-only 的限定出现太晚，建议前移\n- Contribution 2 措辞需更精确反映 \"一正两负\" 结果模式\n- Contribution 5 建议合并到 Contribution 2/4 中\n- 需加强 vs Basu et al. (2026) 的差异化定位：跨语言混淆排除设计是增量价值所在\n\n### Method (§3)\n- §3.3 引用 Hewitt & Liang 但未执行 → 读者期望被违反\n- §3.6 α 值选择无 justification，跨模型不可比\n- 建议添加 α 规范化公式（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）\n\n### Results (§4)\n- §4.3 方向性不对称是最强贡献——建议更突出呈现而非仅作为 \"mirror\" 支撑\n- §4.4 TOST 功效 1.4% 报告是好实践，但结论部分仍倾向 positive framing\n- §4.5 COMET tercile 应明确标注 \"inconclusive due to low power\"；Gemma Δ=+10.3pp 不应被整体无显著性掩盖\n- 建议添加 Table: AUROC alongside balanced accuracy\n- Table 1 脚注 \"Δ_asym is the mean of paired bootstrap differences...\" 重要但容易被忽略，建议移入正文 §4.3\n\n### Discussion (§5)\n- EN-DE 对照是 strongest confound evidence — 应更突出\n- 三个 mechanistic 假说全部 untested → 至少验证一个（如余弦相似度或非线性 probe）\n- 与 Basu et al. 的关系未充分讨论\n\n### Limitations\n- Cross-seed 报告有效但不替代正式 CV\n- Qwen dual role caveat 可更 prominently 呈现\n- Gemma COMET Δ=+10.3pp 应在 Limitations 单独讨论而非被整体分析掩盖\n\n### Format & References\n- COMET 版本号缺失\n- 无代码/数据可用性声明\n- Figure 3 灰色带误导性\n- 补充 Ravichander et al. (2021)、Pimentel & Cotterell (2021)\n- 核实 Marks & Tegmark (2024) venue\n- 验证 Gurgurov et al. (2026) 公开可获取性后决定是否引用",
  "project": "clkc_mech_interp",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 3 审稿报告 — clkc_mech_interp\n\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**交叉回应**: 完成，收敛（1 轮交叉即达共识）\n\n---\n\n## Summary\n\n本文研究 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B 中英-中知识冲突信号的线性可探测性与因果相关性。主要发现：(1) 三模型均存在可探测的冲突信号且方向 asymmetry（ZH→EN 比 EN→ZH 高约 7pp）与已知跨语言能力差异一致；(2) 仅 Llama L13 的 steering 产生显著行为翻转，Qwen/Gemma 未成功——论证 detection ≠ causal relevance。论文经过前两轮审稿的实质性修改（前轮所有 issue 已 resolved），当前版本在 framing 和统计严谨性上有明显进步，但仍存在等价性主张过强、因果证据范围有限、贡献定位与证据强度不匹配等问题。\n\n---\n\n## Strengths\n\n1. **研究问题有价值**：跨语言知识冲突的 mechanistic 分析连接 multilingual NLP、knowledge editing 和 interpretability 三个社区，是 timely 且重要的方向。\n\n2. **方向性不对称是非平凡发现**：ZH→EN 迁移比 EN→ZH 高约 7pp，三模型方向一致（Llama +7.3pp [0.4, 14.0]，Qwen +7.2pp，Gemma +6.6pp [1.9, 11.1]）。这不能从 \"共享空间存在\" 直接推出——共享空间不保证对称迁移，不保证线性可分性。XNLI 基线显示非冲突任务也存在相同方向不对称，将观测归因到通用跨语言结构而非冲突特异编码——这是一个正面发现（排除了替代假说），而非 null result。\n\n3. **\"Detection ≠ Decision\" 区分**：Llama 正面结果 + Qwen/Gemma 负面结果的对比设计论证 probing accuracy 不意味着因果相关性。虽然原则已有先行文献（Basu et al. 2026），但跨语言场景引入的混淆排除设计有独立实验价值。\n\n4. **统计方法多样化**：TOST + Bayesian BF + binomial + bootstrap CI 多证据链，论文诚实报告 TOST 功效不足（1.4%），展示统计诚信。\n\n5. **多证据链混淆排除**：COMET tercile + token overlap (Jaccard 3-4%) + EN-DE 对照（Jaccard 14.8% 但 Δ=+1.2pp n.s.），EN-DE 对照设计巧妙且有力。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则不可接收）\n\n**[R3-N1] 标题 \"Mirror\" 等价性主张与统计证据不匹配** [R1 提出, R2 AGREE]\n\nTOST 功效仅 1.4%（需 ±12.5pp margin 才达 80% power），BF₀₁ ≈ 1.5 仅 \"directionally consistent but modest\"。论文转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但 CI 重叠不等同于等价检验。标题中 \"Mirror\" 是全文最强等价性 claim，与正文 \"consistent with\" 的谨慎措辞不一致。Figure 3 的 ±2pp 灰色带视觉暗示 TOST 有效但功效不支持。\n\n**建议**：标题改为 \"... Are Consistent With General Cross-Lingual Asymmetries\"；删除或注释 Figure 3 灰色带。\n\n**[R3-N2] COMET tercile 消融 MDD=25.3pp 功效不足** [R1 提出, R2 部分反驳]\n\nMDD=25.3pp 意味着该分析无法检测 <25pp 真实效应。Gemma Δ=+10.3pp 方向与 confound hypothesis 一致但不显著（应在 Limitations 更明确讨论，而非仅被整体无显著性掩盖）。R2 反驳称多证据链（token overlap + EN-DE 对照）部分弥补——特别是 EN-DE 对照：token overlap 4× 于 EN-ZH 但 asymmetry 近零，如果 overlap 驱动 asymmetry 应该在 EN-DE 更强但事实相反。\n\n**共识建议**：(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。\n\n**[R3-N3] 因果证据限于 Llama L13，贡献定位过强** [R1 提出, R2 AGREE]\n\nContribution 2 \"Architecture-dependent causal localization\" 暗示跨架构系统性比较发现，实际为一个正面结果（Llama L13, p=0.002）加两个 null（Qwen best p=0.785, Gemma best p=0.148）。Section 5 三个假说（非线性交互、superposition、架构差异）全部 untested。当假说用于支撑独立贡献时，证据标准需更高。\n\n**建议**：(1) Contribution 2 改为 \"Causal localization in Llama with negative evidence in Qwen and Gemma\"，降级为 exploratory finding；(2) 至少对一个假说提供初步验证（如 Qwen/Gemma L13 probe direction vs steering direction 余弦相似度，或线性 vs 非线性 probe 精度对比）；(3) 考虑 activation patching 等替代因果方法——steering 失败可能反映方法局限而非模型缺乏因果结构。\n\n### Should-Fix（不修复降低论文质量但不阻止接收）\n\n**[R3-W1] 单一 train/test split 缺乏 cross-validation** [R1 提出, R2 AGREE]\n\nProbing 领域标准做法为 k-fold CV（Belinkov 2022）。Cross-seed ±0.12-1.90% 和 seed=123 steering 复现提供部分稳健性，但 bootstrap CI 捕获 within-split variability 而非 across-split variability。\n\n**[R3-W2] Qwen 双重角色** [R1 提出, R2 AGREE]\n\nQwen 同时作为翻译模型和实验对象。Qwen EN→ZH transfer accuracy 最高（67.3%），方向与 \"翻译输出对 Qwen 自然更 aligned\" 一致。最干净控制需独立翻译模型。\n\n**[R3-W3] Probe selectivity 未正式评估** [R1 提出, R2 AGREE]\n\n引用 Hewitt & Liang (2019) control task 思路但未执行。缺少随机标签 baseline 或 selectivity 指标。与 Ravichander et al. (2021) \"Probing the Probing Paradigm\" 高度相关但未引用。\n\n**[R3-W4] 缺少 AUROC** [R1 提出, R2 AGREE]\n\nBalanced accuracy 在单一阈值下操作。AUROC 对 Gemma（88.9% bal acc + zero steering flips）尤其有诊断价值——帮助理解 probe 判别能力是否真如 bal acc 暗示的那样强。\n\n**[R3-W5] α 值选择缺乏理论依据** [R1 提出, R2 AGREE]\n\nα ∈ {±20, ±10, ±5, ±2, ±1} 无规范化。同一 α 在不同模型/层代表不同扰动强度。应用 probe weight norm 或 residual stream std 规范化（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）。\n\n**[R3-NOV] 新颖性被 Basu et al. (2026) 部分削弱** [R2 提出, R1 AGREE with nuance]\n\n\"Detection ≠ decision\" 原则作为独立贡献增量有限（Basu 2026 已建立 98.2% AUROC + steering 完全失败的先例）。但 R1 指出跨语言维度的混淆排除设计有独立价值。\n\n**建议**：将 Contribution 5 (\"detectability does not predict causal relevance\") 合并到 Contribution 2/4 中作为支撑证据，而非独立贡献点。保留跨语言实例化的实验设计价值，但不重复 claim 已知原则。\n\n**[R3-W6] Discussion 假说过于投机** [R2 提出, R1 AGREE]\n\n三个假说全部 untested。建议至少提供一个假说的初步验证——如检查 probe direction 与 residual stream 主成分的对齐度，或比较线性 vs 非线性 probe 精度差异。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. \"Mirror\" 等价性 claim 过强，证据仅支持 \"consistent with\"\n2. 因果证据（steering）仅 Llama L13，不足以支撑跨架构普遍性主张\n3. Contribution 2 应降级为 exploratory finding\n4. Contribution 5 应合并而非独立列出\n5. Probe selectivity 未正式评估是方法论缺口\n6. α 值应规范化\n7. 单一 split 不满足 probing 领域标准\n8. Qwen 双重角色需更好控制或更充分讨论\n9. Discussion 假说至少需一个初步验证\n10. 所有 minor issues (COMET 版本号/代码可用性/Figure 3 灰色带) 应修复\n\n## Reviewer Divergence [REBUT]\n\n1. **R3-N2 严重性**：R1 认为 COMET tercile \"本质上无效\"；R2 认为 token overlap + EN-DE 对照部分弥补，整体 confound exclusion 仍可接受。**Director 判断**：R2 的论证更有说服力——EN-DE 对照是独立的强证据，但 COMET tercile 本身确实应标注为 underpowered。\n\n2. **跨语言可检测性是否 \"expected\"**：R2 认为这是共享空间的自然推论，增量有限；R1 REBUT 指出方向性不对称（~7pp）不可直接推出，XNLI 基线是正面发现（归因到通用跨语言结构）而非 null result，共享空间不保证线性可分。**Director 判断**：R1 论证有力——asymmetry 确实是 non-trivial empirical finding，但论文需要更清晰地将 asymmetry（而非 detectability 本身）定位为核心贡献。\n\n3. **Gurgurov et al. (2026) 引用要求**：R2 列为遗漏引用；R1 质疑该文献在双盲截止前是否可公开获取。**Director 判断**：作者需验证该文献的公开时间线，如在投稿前可获取则应引用。\n\n---\n\n## Questions for Authors\n\n1. 是否有计划用独立翻译模型（非 Qwen）重做翻译以排除 Qwen 双重角色混淆？\n2. 能否提供 AUROC 数值和 selectivity control task 结果（即使放在 Appendix）？\n3. α 值规范化后，Llama L13 的 steering 效果是否仍然显著？\n4. 连续 COMET score 作为回归变量与 probing accuracy 的关系如何？\n5. Basu et al. (2026) 的发现与本文的具体差异化贡献是什么（beyond 跨语言扩展）？\n6. 能否对 Section 5 三个假说中至少一个提供初步验证数据？\n7. Qwen/Gemma steering 失败是否可能是方法局限（如 activation patching 是否会给出不同结论）？\n\n---\n\n## Missing References\n\n1. **Ravichander et al. (2021)** \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\" — 直接论证 probing accuracy 不意味着 task relevance，与本文核心论点高度相关\n2. **Pimentel & Cotterell (2021)** — information-theoretic probing 框架，与本文 probe methodology 讨论相关\n3. **Gurgurov et al. (2026) \"CLaS-Bench\"** — 跨语言 steering benchmark（需验证公开可获取性，若投稿前已公开则应引用）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~2.5 min)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Pages 3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 figure/table/display equation。建议将核心公式提为 display equation 打破视觉单调 |\n| ⚠️ Warning | Pages 7-8 | Page 7 仅顶部 Table 3，其余纯文本；Page 8 整页纯文本。建议部分 discussion 定量对比以 summary table 呈现 |\n| ℹ️ Info | Page 2 | Figure 1 图内标注文字偏小（~6-7pt），打印边缘可读性可能下降 |\n| ℹ️ Info | Page 5 | Figure 2 三子图横向压缩，x 轴 tick label 密集 |\n| ℹ️ Info | Page 1 | Abstract 视觉上较长（接近 200 words 上限） |\n| ℹ️ Info | Page 9 | Limitations + AI Use + Appendix 共处一页，紧凑但合理 |\n\n统计：0 critical, 2 warning, 4 info。整体排版质量可接受，无严重布局问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings（可被 Findings 接收）**\n\n| Reviewer | 评分 | 核心关注 |\n|----------|------|----------|\n| R1 | 3.5 (Borderline Conference) | 方法严谨性：TOST power / confound exclusion / CV；但认可 asymmetry 为 non-trivial 贡献 |\n| R2 | 3.0 (Findings) | 新颖性：Basu et al. preemption + 贡献定位过强 |\n\n**综合判断**：论文经过三轮修改后在 framing 和统计报告上有显著进步（前两轮所有 issue 已 resolved），研究问题有价值，实验设计整体合理。方向性不对称（~7pp, 三模型一致）是非平凡的实证贡献，混淆排除管线设计（特别是 EN-DE 对照）展示了实验功力。\n\n但当前版本的核心问题是 **claims 范围超出证据支撑**：(1) \"Mirror\" 标题暗示等价但 TOST 无功效；(2) Contribution 2 暗示跨架构系统性发现但实为 1 正 2 负；(3) Contribution 5 重复已知原则。如果作者将贡献重新定位为 \"(a) 跨语言冲突信号的方向性不对称 + (b) Llama 特异性因果定位 + (c) 混淆排除方法论\"，论文的贡献-证据匹配度会大幅改善。\n\nFindings 接收合理——贡献足够但存在实质性改进空间。主会议接收需要：(1) 解决标题/贡献的 overclaim；(2) 补充 AUROC + selectivity control + α 规范化；(3) 对至少一个 mechanistic 假说提供初步验证；(4) 明确差异化 vs Basu et al.。\n\n**置信度**：高（双 Reviewer 在核心问题上高度一致，分歧均在严重性程度而非方向）\n\n---\n\n## Detailed Comments\n\n### Abstract & Introduction\n- Abstract 最后一句对 Llama-only 的限定出现太晚，建议前移\n- Contribution 2 措辞需更精确反映 \"一正两负\" 结果模式\n- Contribution 5 建议合并到 Contribution 2/4 中\n- 需加强 vs Basu et al. (2026) 的差异化定位：跨语言混淆排除设计是增量价值所在\n\n### Method (§3)\n- §3.3 引用 Hewitt & Liang 但未执行 → 读者期望被违反\n- §3.6 α 值选择无 justification，跨模型不可比\n- 建议添加 α 规范化公式（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）\n\n### Results (§4)\n- §4.3 方向性不对称是最强贡献——建议更突出呈现而非仅作为 \"mirror\" 支撑\n- §4.4 TOST 功效 1.4% 报告是好实践，但结论部分仍倾向 positive framing\n- §4.5 COMET tercile 应明确标注 \"inconclusive due to low power\"；Gemma Δ=+10.3pp 不应被整体无显著性掩盖\n- 建议添加 Table: AUROC alongside balanced accuracy\n- Table 1 脚注 \"Δ_asym is the mean of paired bootstrap differences...\" 重要但容易被忽略，建议移入正文 §4.3\n\n### Discussion (§5)\n- EN-DE 对照是 strongest confound evidence — 应更突出\n- 三个 mechanistic 假说全部 untested → 至少验证一个（如余弦相似度或非线性 probe）\n- 与 Basu et al. 的关系未充分讨论\n\n### Limitations\n- Cross-seed 报告有效但不替代正式 CV\n- Qwen dual role caveat 可更 prominently 呈现\n- Gemma COMET Δ=+10.3pp 应在 Limitations 单独讨论而非被整体分析掩盖\n\n### Format & References\n- COMET 版本号缺失\n- 无代码/数据可用性声明\n- Figure 3 灰色带误导性\n- 补充 Ravichander et al. (2021)、Pimentel & Cotterell (2021)\n- 核实 Marks & Tegmark (2024) venue\n- 验证 Gurgurov et al. (2026) 公开可获取性后决定是否引用",
    "project": "clkc_mech_interp",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-25T04:37:50.131306+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6951eb3869a0070e3ae607ab60c90dad:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4178
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-25T04:38:02.786191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
  "offset": "0",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
    "offset": "0",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-25T04:38:02.886973+00:00_

0	issues:
1	# === Round 3 NEW ISSUES ===
2	
3	- id: "R3-N1"
4	  summary: "标题 'Mirror' 等价性主张与 TOST 功效(1.4%)不匹配"
5	  category: framing
6	  severity: critical
7	  status: open
8	  first_raised_round: 3
9	  last_seen_round: 3
10	  mentions:
11	    - round: 3
12	      reviewers: [1, 2]
13	      note: "R1 提出 TOST power 角度，R2 AGREE 并补充标题-正文一致性问题。BF₀₁≈1.5 仅 modest evidence。建议改 Mirror→Consistent With"
14	  action_items: []
15	  resolution: ""
16	  resolution_round: null
17	
18	- id: "R3-N2"
19	  summary: "COMET tercile 消融 MDD=25.3pp 使混淆排除功效不足"
20	  category: experiment
21	  severity: critical
22	  status: open
23	  first_raised_round: 3
24	  last_seen_round: 3
25	  mentions:
26	    - round: 3
27	      reviewers: [1, 2]
28	      note: "R1 认为'本质上无效'，R2 部分反驳——多证据链(token overlap+EN-DE对照)部分弥补。Gemma Δ=+10.3pp 方向不利。建议补充连续 COMET 回归分析"
29	  action_items: []
30	  resolution: ""
31	  resolution_round: null
32	
33	- id: "R3-N3"
34	  summary: "因果证据仅限 Llama L13 单模型单层，不足以支撑跨架构 claim"
35	  category: method
36	  severity: critical
37	  status: open
38	  first_raised_round: 3
39	  last_seen_round: 3
40	  mentions:
41	    - round: 3
42	      reviewers: [1, 2]
43	      note: "摘要叙事结构暗示跨模型等强度发现。Contribution 2 措辞 'Architecture-dependent causal localization' 过于模糊。建议改为 Causal localization in Llama with negative evidence in Qwen/Gemma"
44	  action_items: []
45	  resolution: ""
46	  resolution_round: null
47	
48	- id: "R3-W1"
49	  summary: "单一 train/test split 缺乏 k-fold cross-validation"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-25T04:38:07.519003+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
  "offset": "49",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
    "offset": "49",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-25T04:38:07.569639+00:00_

49	- id: "R3-W1"
50	  summary: "单一 train/test split 缺乏 k-fold cross-validation"
51	  category: method
52	  severity: warning
53	  status: open
54	  first_raised_round: 3
55	  last_seen_round: 3
56	  mentions:
57	    - round: 3
58	      reviewers: [1, 2]
59	      note: "Belinkov 2022 推荐 CV 为标准做法。cross-seed ±0.12-1.90% 提供部分稳健性但不替代 CV"
60	  action_items: []
61	  resolution: ""
62	  resolution_round: null
63	
64	- id: "R3-W2"
65	  summary: "Qwen 同时作为翻译模型和实验对象的双重角色"
66	  category: method
67	  severity: warning
68	  status: open
69	  first_raised_round: 3
70	  last_seen_round: 3
71	  mentions:
72	    - round: 3
73	      reviewers: [1, 2]
74	      note: "Qwen EN→ZH transfer accuracy 最高(67.3%)，与 aligned 假设方向一致。最干净控制需独立翻译模型"
75	  action_items: []
76	  resolution: ""
77	  resolution_round: null
78	
79	- id: "R3-W3"
80	  summary: "Probe selectivity 未正式评估（无 control task）"
81	  category: method
82	  severity: warning
83	  status: open
84	  first_raised_round: 3
85	  last_seen_round: 3
86	  mentions:
87	    - round: 3
88	      reviewers: [1, 2]
89	      note: "引用 Hewitt & Liang 2019 但未执行。XNLI baseline 服务不同目的。缺 Ravichander 2021 引用"
90	  action_items: []
91	  resolution: ""
92	  resolution_round: null
93	
94	- id: "R3-W4"
95	  summary: "缺少 AUROC 阈值无关评估指标"
96	  category: experiment
97	  severity: warning
98	  status: open
99	  first_raised_round: 3
100	  last_seen_round: 3
101	  mentions:
102	    - round: 3
103	      reviewers: [1, 2]
104	      note: "Balanced accuracy 单阈值。AUROC 对 Gemma(88.9% bal acc + zero steering)尤其有意义。不改变核心结论但为 good practice"
105	  action_items: []
106	  resolution: ""
107	  resolution_round: null
108	
109	- id: "R3-W5"
110	  summary: "Steering α 值选择缺乏理论依据和跨模型规范化"
111	  category: method
112	  severity: warning
113	  status: open
114	  first_raised_round: 3
115	  last_seen_round: 3
116	  mentions:
117	    - round: 3
118	      reviewers: [1, 2]
119	      note: "α∈{±20,±10,±5,±2,±1} 无规范化。同一 α 在不同模型/层代表不同扰动强度。建议用 probe weight norm 或 residual stream std 规范化"
120	  ac
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-25T04:38:11.234131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
  "offset": "148",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
    "offset": "148",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-25T04:38:11.286073+00:00_

148	      reviewers: [1, 2]
149	      note: "EN-ZH 字符系统不同使 3-4% 已足够说明极低 overlap，但 character-level 可更有信息量"
150	  action_items: []
151	  resolution: ""
152	  resolution_round: null
153	
154	- id: "R3-M3"
155	  summary: "无代码/数据可用性声明"
156	  category: format
157	  severity: info
158	  status: open
159	  first_raised_round: 3
160	  last_seen_round: 3
161	  mentions:
162	    - round: 3
163	      reviewers: [1, 2]
164	      note: "double-blind 阶段可用匿名链接"
165	  action_items: []
166	  resolution: ""
167	  resolution_round: null
168	
169	- id: "R3-M4"
170	  summary: "Random direction control 仅为最低标准，缺更强 control"
171	  category: method
172	  severity: info
173	  status: open
174	  first_raised_round: 3
175	  last_seen_round: 3
176	  mentions:
177	    - round: 3
178	      reviewers: [1, 2]
179	      note: "更强 control: 不同任务 probe direction / permuted labels probe"
180	  action_items: []
181	  resolution: ""
182	  resolution_round: null
183	
184	- id: "R3-M5"
185	  summary: "Figure 3 灰色带暗示 TOST 有效但功效不支持"
186	  category: writing
187	  severity: info
188	  status: open
189	  first_raised_round: 3
190	  last_seen_round: 3
191	  mentions:
192	    - round: 3
193	      reviewers: [1, 2]
194	      note: "±2pp 灰色带在视觉上暗示 meaningful equivalence zone。建议删除或注释说明"
195	  action_items: []
196	  resolution: ""
197	  resolution_round: null
198	
199	- id: "R3-NOV"
200	  summary: "新颖性被 Basu et al. (2026) 先行发现削弱"
201	  category: framing
202	  severity: warning
203	  status: open
204	  first_raised_round: 3
205	  last_seen_round: 3
206	  mentions:
207	    - round: 3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-25T04:38:20.727088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
  "offset": "206",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml",
    "offset": "206",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-25T04:38:20.727554+00:00_

206	  mentions:
207	    - round: 3
208	      reviewers: [2]
209	      note: "R2 核心关注——detection≠decision 的 novelty 已被 Basu 部分 preempt。R1 未将其列为核心关注点。评分差异主因"
210	  action_items: []
211	  resolution: ""
212	  resolution_round: null
213	
214	# === PREVIOUSLY RESOLVED (Rounds 1-2) ===
215	
216	- id: "R2-W2"
217	  summary: "标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构成 overclaiming"
218	  category: framing
219	  severity: critical
220	  status: resolved
221	  first_raised_round: 1
222	  last_seen_round: 2
223	  mentions:
224	    - round: 1
225	      reviewers: [2, 1]
226	      note: "R1 AGREE 标题应加限定"
227	    - round: 2
228	      reviewers: [1, 2]
229	      note: "R2 升级为 Must-Fix，R1 交叉 AGREE"
230	  action_items:
231	    - round: 2
232	      action: "标题改为 'English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries'"
233	      assigned_to: paper_agent
234	      status: done
235	  resolution: "Reviewer PASS: 标题准确限定实验范围，正文 cross-lingual 用法均为方法论描述"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-25T04:39:47.816080+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "clkc_mech_interp",
  "issues_yaml": "issues:\n# === Round 3 NEW ISSUES ===\n\n- id: \"R3-N1\"\n  summary: \"标题 'Mirror' 等价性��张与 TOST 功效(1.4%)不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 提出 TOST power 角度，R2 AGREE 并补充标题-正文一致性问题。BF₀₁≈1.5 仅 modest evidence。建议改 Mirror→Consistent With\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"COMET tercile 消融 MDD=25.3pp ��混淆排除功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 认为'本质上无效'，R2 部分反驳——多证据链(token overlap+EN-DE对照)部分弥补。Gemma Δ=+10.3pp 方向不利但 baseline near-chance。建议补充连续 COMET 回归 + 论证重心转向 EN-DE 对照\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"因果证据仅�� Llama L13 单模型单层，不足以支撑跨架构 claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Contribution 2 'Architecture-dependent causal localization' 暗示跨架构系统性发现，实为 1正2负。R1 补充：steering 失败可能反映方法局限而非模型缺乏因果结构，建议 activation patching 等替代方法\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"单一 train/test split 缺乏 k-fold cross-validation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Belinkov 2022 ��荐 CV 为标准做法。cross-seed ±0.12-1.90% 提供部分稳健性但不替代 CV\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Qwen 同时作为翻译模型和实验对象的双重角色\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen EN→ZH transfer accuracy 最高(67.3%)，与 aligned 假设方向一致。最干净控制需独立翻译模型\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Probe selectivity 未正式评估（无 control task）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"��用 Hewitt & Liang 2019 但未执行。XNLI baseline 服务不同目的。缺 Ravichander 2021 引用\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"缺少 AUROC 阈值无关评估指标\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Balanced accuracy 单阈值。AUROC 对 Gemma(88.9% bal acc + zero steering)尤其有意义\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"Steering α 值选择缺乏理论依据和跨模型规范化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"α∈{±20,±10,±5,±2,±1} 无规范化。建议 α_norm = α/||w_probe|| 或 α/std(h_l)\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Discussion 三个 mechanistic 假说全部 untested\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 AGREE。当假说支撑独立贡献(Contribution 2)时证据标准需更高。建议至少验证一个——如 probe direction 余弦相似度或线性 vs 非线性 probe 对比\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-NOV\"\n  summary: \"新颖性被 Basu et al. (2026) 先行发现削弱；Contribution 5 应合并\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 核心关注——detection≠decision 的 novelty 已被 Basu 部分 preempt(98.2% AUROC + steering失败)。R1 AGREE 但指出跨语言混淆排除设计有独立价值。共识：Contribution 5 应合并到 Contribution 2/4 作为支撑证据而非独立贡献\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"COMET 版本号未标注\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"需标注具体版本如 wmt22-comet-da\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Token overlap 仅用 Jaccard 粗粒���指标\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"EN-ZH 字符系统不同使 3-4% 已足够说明极低 overlap，但 character-level 可更有信息量\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"无代码/数据可用性声明\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"double-blind 阶段可用匿名链接\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Random direction control 仅为最低标准，缺更强 control\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"更强 control: 不同任务 probe direction / permuted labels probe\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Figure 3 灰色带暗示 TOST 有效但功效不支持\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±2pp 灰色带在视觉上暗示 meaningful equivalence zone。建议删除或注释说明\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === PREVIOUSLY RESOLVED (Rounds 1-2) ===\n\n- id: \"R2-W2\"\n  summary: \"标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构�� overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加���定\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 升级为 Must-Fix，R1 交叉 AGREE\"\n  action_items:\n    - round: 2\n      action: \"标题改�� 'English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 标题准确限定实验范围，正文 cross-lingual 用法均为方法论描述\"\n  resolution_round: 3\n\n- id: \"MF-2\"\n  summary: \"标题 'Inherit' 因果措辞仅有 CI 重叠的相关性证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 强烈 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Inherit→Mirror 全文替换 + TOST power + Bayesian BF\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Mirror 准确反映 evidence 强度；TOST power(1.4%)+BF(1.5)+binomial(p=0.016) 三条证据链互补\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"最核心局限\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 MF-3\"\n  action_items:\n    - round: 2\n      action: \"Reframe 为 architecture-dependent causal localization + seed=123 复现 + informative negatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 'emerges' 措辞恰当，Contribution 2 accurately scoped\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"单种子实验未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致\"\n    - round: 2\n      reviewers: [1]\n      note: \"R1 升级为 Must-Fix\"\n  action_items:\n    - round: 2\n      action: \"Limitations 报告 accuracy stability (±0.12-1.90%) + peak layer sensitivity; seed=123 steering 复现 (4/6 Bonf sig)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"多种子 accuracy 稳定性 + steering 复现数据已加入\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"TOST 等价检验未报告功效\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CI 重叠是必要非充分条件\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"与 MF-2 联动\"\n  action_items:\n    - round: 2\n      action: \"TOST power=1.4% + BF₀₁≈1.5 加入 §4.3\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 表述准确传达 inconclusive but directionally supportive\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 功效不足 + Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"p=0.695/0.761 无法区分无效应和功效不足\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S2\"\n  action_items:\n    - round: 2\n      action: \"MDD=25.3pp + 方向性论证 + Gemma COMET (Δ=+10.3pp, p=0.278, inconclusive)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Gemma 措辞恰当\"\n  resolution_round: 3\n\n- id: \"SF-4\"\n  summary: \"Qwen/Gemma steering 失败缺乏 mechanistic 分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Discussion 新增 mechanistic 假设段落\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"三个假设合理，引用 Elhage 2022 + Templeton 2024 恰当\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行，未报告重叠度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"建议报告重叠度\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S3\"\n  action_items:\n    - round: 2\n      action: \"3.5% 三重重叠 + pairwise 加入 §4.1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"位置合理，framing 恰当 (independent replication)\"\n  resolution_round: 3\n\n- id: \"SF-6\"\n  summary: \"新颖性定位 vs Zhao et al. 2024\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 认为增量，R1 REBUT\"\n  action_items:\n    - round: 2\n      action: \"Intro 加入 5 点 novelty articulation\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 点独特贡献已加入 Introduction\"\n  resolution_round: 3\n\n- id: \"SF-7\"\n  summary: \"遗漏跨语言 steering 相关工作 3 篇\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 列出 3 篇\"\n  action_items:\n    - round: 2\n      action: \"WebSearch 验证后 5 篇新引用已加入\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 篇新引用全部验证为真实并加入 Related Work\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 Qwen3-SB 与实验对象 Qwen3-8B 同系列\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"翻译输出可能对 Qwen 有系统性偏好\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 列为 Q4\"\n  action_items:\n    - round: 2\n      action: \"Limitations 讨论\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已在 Limitations 中讨论 Qwen dual role caveat\"\n  resolution_round: 3\n\n- id: \"R1-N1\"\n  summary: \"Steering Bonferroni 校正仅层内应用\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"独立复现部分缓解\"\n  action_items:\n    - round: 1\n      action: \"method.tex 增加 per-layer 独立假设说明 + full family 结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"method.tex + experiments.tex 修复，Round 2 未复发\"\n  resolution_round: 2\n\n- id: \"R2-N2-v1\"\n  summary: \"Qwen3-8B 引用错误\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误\"\n  action_items:\n    - round: 1\n      action: \"替换为 Qwen3 Technical Report\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"yang2024qwen25 → yang2025qwen3\"\n  resolution_round: 2\n\n- id: \"R2-W1-v1\"\n  summary: \"Related Work 遗漏 Meng/Geiger/Turner/Marks\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意必须引用\"\n  action_items:\n    - round: 1\n      action: \"补充 4 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全部 4 篇加入 Related Work\"\n  resolution_round: 2\n\n- id: \"R2-W3-v1\"\n  summary: \"Bib 'and others' 非标准格式\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"ACL 模板要求完整作者列表\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"所有 'and others' 替换为完整作者列表\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 阈值不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一为 p<0.005 (k=10)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"caption 统一为 Bonferroni-corrected p<0.005 (k=10)\"\n  resolution_round: 2\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "clkc_mech_interp",
    "issues_yaml": "issues:\n# === Round 3 NEW ISSUES ===\n\n- id: \"R3-N1\"\n  summary: \"标题 'Mirror' 等价性��张与 TOST 功效(1.4%)不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 提出 TOST power 角度，R2 AGREE 并补充标题-正文一致性问题。BF₀₁≈1.5 仅 modest evidence。建议改 Mirror→Consistent With\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"COMET tercile 消融 MDD=25.3pp ��混淆排除功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 认为'本质上无效'，R2 部分反驳——多证据链(token overlap+EN-DE对照)部分弥补。Gemma Δ=+10.3pp 方向不利但 baseline near-chance。建议补充连续 COMET 回归 + 论证重心转向 EN-DE 对照\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"因果证据仅�� Llama L13 单模型单层，不足以支撑跨架构 claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Contribution 2 'Architecture-dependent causal localization' 暗示跨架构系统性发现，实为 1正2负。R1 补充：steering 失败可能反映方法局限而非模型缺乏因果结构，建议 activation patching 等替代方法\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"单一 train/test split 缺乏 k-fold cross-validation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Belinkov 2022 ��荐 CV 为标准做法。cross-seed ±0.12-1.90% 提供部分稳健性但不替代 CV\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Qwen 同时作为翻译模型和实验对象的双重角色\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen EN→ZH transfer accuracy 最高(67.3%)，与 aligned 假设方向一致。最干净控制需独立翻译模型\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Probe selectivity 未正式评估（无 control task）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"��用 Hewitt & Liang 2019 但未执行。XNLI baseline 服务不同目的。缺 Ravichander 2021 引用\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"缺少 AUROC 阈值无关评估指标\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Balanced accuracy 单阈值。AUROC 对 Gemma(88.9% bal acc + zero steering)尤其有意义\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"Steering α 值选择缺乏理论依据和跨模型规范化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"α∈{±20,±10,±5,±2,±1} 无规范化。建议 α_norm = α/||w_probe|| 或 α/std(h_l)\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Discussion 三个 mechanistic 假说全部 untested\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 AGREE。当假说支撑独立贡献(Contribution 2)时证据标准需更高。建议至少验证一个——如 probe direction 余弦相似度或线性 vs 非线性 probe 对比\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-NOV\"\n  summary: \"新颖性被 Basu et al. (2026) 先行发现削弱；Contribution 5 应合并\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 核心关注——detection≠decision 的 novelty 已被 Basu 部分 preempt(98.2% AUROC + steering失败)。R1 AGREE 但指出跨语言混淆排除设计有独立价值。共识：Contribution 5 应合并到 Contribution 2/4 作为支撑证据而非独立贡献\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"COMET 版本号未标注\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"需标注具体版本如 wmt22-comet-da\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Token overlap 仅用 Jaccard 粗粒���指标\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"EN-ZH 字符系统不同使 3-4% 已足够说明极低 overlap，但 character-level 可更有信息量\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"无代码/数据可用性声明\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"double-blind 阶段可用匿名链接\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Random direction control 仅为最低标准，缺更强 control\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"更强 control: 不同任务 probe direction / permuted labels probe\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Figure 3 灰色带暗示 TOST 有效但功效不支持\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±2pp 灰色带在视觉上暗示 meaningful equivalence zone。建议删除或注释说明\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === PREVIOUSLY RESOLVED (Rounds 1-2) ===\n\n- id: \"R2-W2\"\n  summary: \"标题 'Cross-Lingual' 仅测试 EN-ZH 一个语言对，构�� overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 AGREE 标题应加���定\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 升级为 Must-Fix，R1 交叉 AGREE\"\n  action_items:\n    - round: 2\n      action: \"标题改�� 'English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 标题准确限定实验范围，正文 cross-lingual 用法均为方法论描述\"\n  resolution_round: 3\n\n- id: \"MF-2\"\n  summary: \"标题 'Inherit' 因果措辞仅有 CI 重叠的相关性证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 强烈 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Inherit→Mirror 全文替换 + TOST power + Bayesian BF\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Mirror 准确反映 evidence 强度；TOST power(1.4%)+BF(1.5)+binomial(p=0.016) 三条证据链互补\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"最核心局限\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 MF-3\"\n  action_items:\n    - round: 2\n      action: \"Reframe 为 architecture-dependent causal localization + seed=123 复现 + informative negatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 'emerges' 措辞恰当，Contribution 2 accurately scoped\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"单种子实验未报告多种子 mean±std\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致\"\n    - round: 2\n      reviewers: [1]\n      note: \"R1 升级为 Must-Fix\"\n  action_items:\n    - round: 2\n      action: \"Limitations 报告 accuracy stability (±0.12-1.90%) + peak layer sensitivity; seed=123 steering 复现 (4/6 Bonf sig)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"多种子 accuracy 稳定性 + steering 复现数据已加入\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"TOST 等价检验未报告功效\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CI 重叠是必要非充分条件\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"与 MF-2 联动\"\n  action_items:\n    - round: 2\n      action: \"TOST power=1.4% + BF₀₁≈1.5 加入 §4.3\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: 表述准确传达 inconclusive but directionally supportive\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"COMET tercile 功效不足 + Gemma 未报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"p=0.695/0.761 无法区分无效应和功效不足\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S2\"\n  action_items:\n    - round: 2\n      action: \"MDD=25.3pp + 方向性论证 + Gemma COMET (Δ=+10.3pp, p=0.278, inconclusive)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS: Gemma 措辞恰当\"\n  resolution_round: 3\n\n- id: \"SF-4\"\n  summary: \"Qwen/Gemma steering 失败缺乏 mechanistic 分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 提出，R1 AGREE\"\n  action_items:\n    - round: 2\n      action: \"Discussion 新增 mechanistic 假设段落\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"三个假设合理，引用 Elhage 2022 + Templeton 2024 恰当\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"跨模型比较在不同样本子集上进行，未报告重叠度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"建议报告重叠度\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 列为 S3\"\n  action_items:\n    - round: 2\n      action: \"3.5% 三重重叠 + pairwise 加入 §4.1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"位置合理，framing 恰当 (independent replication)\"\n  resolution_round: 3\n\n- id: \"SF-6\"\n  summary: \"新颖性定位 vs Zhao et al. 2024\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 认为增量，R1 REBUT\"\n  action_items:\n    - round: 2\n      action: \"Intro 加入 5 点 novelty articulation\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 点独特贡献已加入 Introduction\"\n  resolution_round: 3\n\n- id: \"SF-7\"\n  summary: \"遗漏跨语言 steering 相关工作 3 篇\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"R2 列出 3 篇\"\n  action_items:\n    - round: 2\n      action: \"WebSearch 验证后 5 篇新引用已加入\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 篇新引用全部验证为真实并加入 Related Work\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"翻译模型 Qwen3-SB 与实验对象 Qwen3-8B 同系列\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"翻译输出可能对 Qwen 有系统性偏好\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 列为 Q4\"\n  action_items:\n    - round: 2\n      action: \"Limitations 讨论\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已在 Limitations 中讨论 Qwen dual role caveat\"\n  resolution_round: 3\n\n- id: \"R1-N1\"\n  summary: \"Steering Bonferroni 校正仅层内应用\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"独立复现部分缓解\"\n  action_items:\n    - round: 1\n      action: \"method.tex 增加 per-layer 独立假设说明 + full family 结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"method.tex + experiments.tex 修复，Round 2 未复发\"\n  resolution_round: 2\n\n- id: \"R2-N2-v1\"\n  summary: \"Qwen3-8B 引用错误\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"事实性引用错误\"\n  action_items:\n    - round: 1\n      action: \"替换为 Qwen3 Technical Report\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"yang2024qwen25 → yang2025qwen3\"\n  resolution_round: 2\n\n- id: \"R2-W1-v1\"\n  summary: \"Related Work 遗漏 Meng/Geiger/Turner/Marks\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意必须引用\"\n  action_items:\n    - round: 1\n      action: \"补充 4 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全部 4 篇加入 Related Work\"\n  resolution_round: 2\n\n- id: \"R2-W3-v1\"\n  summary: \"Bib 'and others' 非标准格式\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"ACL 模板要求完整作者列表\"\n  action_items:\n    - round: 1\n      action: \"补全所有 bib 条目\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"所有 'and others' 替换为完整作者列表\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"Table 3 caption 阈值不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"应统一为 Bonferroni 校正后阈值\"\n  action_items:\n    - round: 1\n      action: \"统一为 p<0.005 (k=10)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"caption 统一为 Bonferroni-corrected p<0.005 (k=10)\"\n  resolution_round: 2\n"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-25T04:39:47.866958+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml\", \"bytes\": 13405}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 336 · 2026-05-25T04:39:59.338719+00:00_

Round 3 圆桌审稿完成。

**结果摘要**：
- **评分**：3.0 (Findings) — R1 给 3.5, R2 给 3.0
- **3 个 Must-Fix**：Mirror overclaim / COMET underpowered / 因果证据仅 Llama
- **7 个 Should-Fix**：CV 缺失 / Qwen 双重角色 / selectivity / AUROC / α 规范化 / 假说 untested / 新颖性定位
- **5 个 Info**：COMET 版本 / Jaccard 粗粒度 / 代码可用性 / control 强度 / Figure 3 灰色带
- **核心判断**：论文贡献有价值（方向性不对称 + 混淆排除设计），但 claims 范围系统性超出证据支撑。Findings 接收合理，主会议需实质修改。

报告已投递至 Research Director，issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 24

## Round 24

66 recorded events


### User

_source line 337 · 2026-05-25T21:13:00.848552+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: clkc_mech_interp
- 论文路径: projects/clkc_mech_interp/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-25T21:13:08.303234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-25T21:13:08.303914+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-25T21:13:12.620194+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-25T21:13:12.771194+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-25T21:13:17.288022+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-25T21:13:17.340228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-25T21:13:21.119014+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-25T21:13:22.023536+00:00_

{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (78 个)\n\n- **comet_qwen_v6**: DONE (killed) — \n- **gemma_en_act_102**: DONE (success) — \n- **xnli_baseline_110**: DONE (negative) — \n- **comet_llama_v5**: DONE (killed) — \n- **comet_qwen_v5**: DONE (killed) — \n- **mvp_probe_llama_v1**: DONE (success) — \n- **mvp_probe_v1**: DONE (success) — \n- **comet_llama_v4**: PREPARING (killed) — \n- **comet_llama_v3**: PREPARING (killed) — \n- **comet_llama_v2**: PREPARING (killed) — \n- **comet_llama**: PREPARING (killed) — \n- **comet_qwen_v4**: PREPARING (killed) — \n- **comet_qwen_v3**: PREPARING (killed) — \n- **comet_qwen_v2**: PREPARING (killed) — \n- **comet_qwen**: PREPARING (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- gemma-steering-pickup（准备中）\n- llama31_en_activations（准备中）\n- qwen3_translate_zh（准备中）\n- collect_en_activations_qwen3_8b（准备中）\n- collect_en_activations_llama_v2（准备中）\n- translate_zh_llama_v2（准备中）\n- translate_zh_qwen（准备中）\n- collect_en_act_llama_v3（准备中）\n- collect_en_act_qwen_v2（准备中）\n- verify_qwen3_v2（准备中）\n- …另有 16 项\n\n## 近期结论\n- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14\n- **steering_qwen_L13_133** (negative): Qwen3-8B-Instruct L13 (36% depth) probe direction causally influences conflict resolution with matched-condition data (N≈200, high probe acc). L13 = L14 peak - 1, establishi
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-25T21:13:22.225385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-25T21:13:22.275963+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_director_647e2400.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-25T21:13:27.046035+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-25T21:13:27.498204+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-25T21:13:27.548874+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-25T21:13:27.601029+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-25T21:13:32.070520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-25T21:13:32.121230+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{subcaption}
16	
17	\title{English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries}
18	
19	\author{Anonymous ACL submission}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	
30	\input{related_work}
31	
32	\input{method}
33	
34	\input{experiments}
35	
36	\input{discussion}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\appendix
45	
46	\section{Use of AI Assistants}
47	\label{app:ai-assistants}
48	
49	We used Claude (Anthropic) as an AI coding and writing assistant
50	throughout this work. Specifically:
51	\begin{itemize}
52	    \item \textbf{Code:} drafting experiment scripts, data-processing
53	    pipelines, and analysis utilities; debugging and refactoring.
54	    \item \textbf{Writing:} drafting and revising paper sections,
55	    polishing prose, and reformatting \LaTeX{}.
56	    \item \textbf{Literature:} summarizing related papers to inform
57	    related-work section.
58	\end{itemize}
59	
60	\section{Fine-Grained Causal Boundary Analysis}
61	\label{app:boundary}
62	
63	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
64	
65	\begin{table}[!t]
66	\centering
67	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
68	\label{tab:boundary}
69	\small
70	\resizebox{\columnwidth}{!}{%
71	\begin{tabular}
…[truncated 4525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-25T21:13:36.085778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "offset": "150",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "offset": "150",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-25T21:13:36.086185+00:00_

150	L13 & 36\% & 71.8 & 0.168 & 0/6 & 0 \\
151	L14 & 39\% & 71.0 & 0.785 & 0/6 & 0 \\
152	L15 & 42\% & 72.9 & 0.617 & 0/6 & 0 \\
153	\midrule
154	\multicolumn{6}{l}{\textit{Gemma-2-9B-IT ($N = 171$; 42 layers)$^{\dagger}$}} \\
155	L16 & 38\% & 88.0 & 0.067 & 0/6 & 0 \\
156	L17 & 40\% & 88.9 & 0.448 & 0/6 & 0 \\
157	L18 & 43\% & 89.5 & 0.219 & 0/6 & 0 \\
158	\bottomrule
159	\end{tabular}
160	\begin{flushleft}
161	\footnotesize $^{\dagger}$ Gemma: after correcting a label assignment error.
162	\end{flushleft}
163	\end{table}
164	
165	\end{document}
166	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-25T21:13:39.700987+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-25T21:13:39.752757+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/acl_latex.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-25T21:13:43.215475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-25T21:13:43.618181+00:00_

1	When multilingual large language models encounter conflicting information between languages, presentation language can determine the answer, but the internal mechanism remains unknown. We probe residual streams in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT on English--Chinese conflicts, combining cross-lingual transfer, XNLI non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across both languages, and cross-lingual transfer exhibits a directional asymmetry: Chinese-trained probes transfer to English ${\sim}$7 percentage points more accurately than the reverse, matching the XNLI baseline and consistent with general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal is broadly distributed across mid-to-upper layers, yet representation steering achieves causal influence only at a mid-layer (L13, 41\% depth) in Llama; analogous Qwen and Gemma steering yields no significant effect. These findings indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\footnote{Code and data are available at \url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-25T21:13:43.668900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-25T21:13:44.070881+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig1_hero.pdf}
7	\caption{Cross-lingual knowledge conflict in multilingual LLMs. When a context passage contradicts the model's parametric knowledge, the language of presentation (English vs.\ Chinese) can bias the answer toward different sources. We ask three questions: (1)~Is the conflict signal linearly detectable in the residual stream? (2)~Do probes transfer across languages, and is the transfer symmetric? (3)~Does detection imply causal influence on resolution?}
8	\label{fig:hero}
9	\end{figure*}
10	
11	When multilingual large language models (LLMs) encounter conflicting information between languages, the language of presentation can determine which answer the model produces \citep{zhao2026when}.
12	Yet the internal mechanism remains opaque: how does the model encode the conflict signal, can it be detected from internal representations, and does the detected signal causally influence resolution?
13	
14	Existing work on probing conflict signals has been limited to monolingual settings \citep{zhao2024analysing, brink2026probing}.
15	Extending cross-lingually introduces confounds (translation quality, token overlap, general transfer properties), and probing establishes correlation rather than causation \citep{hewitt2019designing}; \citet{basu2026interpretability} showed that near-perfect probe accuracy does not guarantee effective steering.
16	
17	Our work extends \citet{zhao2024analysing} in four directions: (1)~cross-lingual expansion from monolingual English to EN-ZH conflict probing; (2)~a systematic confound exclusion pipeline; (3)~the XNLI baseline revealing that asymmetry parallels general cross-lingual structure; and (4)~three-model causal intervention demonstrating that detectability does not predict causal relevance.
18	We combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gem
…[truncated 1987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-25T21:13:44.121463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-25T21:13:44.372870+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, and \citet{brink2026probing} localized factual associations via probing. More recently, \citet{pham2026where} traced intra-memory conflict pathways, while \citet{li2025taming} proposed conflict mitigation methods.
7	Information-theoretic approaches \citep{pimentel2021probing} offer complementary perspectives on probe expressiveness, and \citet{ravichander2021probing} raised concerns about whether probed information is task-relevant.
8	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
9	
10	\paragraph{Cross-lingual representations in multilingual models.}
11	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
12	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
13	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
14	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR cross-lingual conflic
…[truncated 1836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-25T21:13:44.373351+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-25T21:13:44.424232+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\vspace{-18pt}
7	\includegraphics[width=0.88\textwidth]{fig2_pipeline.pdf}
8	\vspace{-14pt}
9	\caption{Method overview. We construct parallel EN/ZH conflict data from ConflictQA with COMET-validated translations, extract per-layer residual stream representations, train logistic regression probes in four transfer directions (EN$\to$EN, ZH$\to$ZH, EN$\to$ZH, ZH$\to$EN), and apply confound exclusion controls before causal steering validation.}
10	\label{fig:pipeline}
11	\vspace{-20pt}
12	\end{figure*}
13	
14	Our pipeline proceeds from data construction through probing and steering (Figure~\ref{fig:pipeline}), formalized below.
15	
16	\subsection{Task Formulation}
17	\label{sec:task}
18	
19	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
20	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
21	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
22	
23	\subsection{Data Construction}
24	\label{sec:data}
25	
26	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
27	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2025qwen3}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
28	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET (Crosslingual Optimized Metric for Evaluation 
…[truncated 4969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-25T21:13:48.692839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-25T21:13:49.747505+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	The three models were independently verified, yielding only 3.5\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\% (Llama $\cap$ Gemma) to 24.8\% (Gemma $\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.
14	
15	\paragraph{Translation.}
16	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET (wmt22-comet-da; \citealt{rei2020comet}) back-translation scores.
17	
18	\paragraph{Probing.}
19	For each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
20	We report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\ref{app:auroc}.
21	All CIs are computed via bootstrap resam
…[truncated 15596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-25T21:13:49.748051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-25T21:13:50.300430+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Causal influence is localized to L13 regardless of detection peak.}
5	In Llama, causal influence is localized to L13 (41\% depth; Fisher $p < 0.001$), near but distinct from the linear probe peak (L15, 47\%) and MLP probe peak (L18, 56\%), with upper-layer interventions producing no significant change ($p > 0.3$; Figure~\ref{fig:dissociation}).
6	L13 coincides with cross-lingual alignment sites \citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.
7	The dissociation evidence is strongest for Gemma, where 88.9\% probe accuracy and 0.93 AUROC coexist with zero steering effects, ruling out probe quality as a confound; for Qwen, weaker probe performance (71.4\%) leaves the null result more ambiguous.
8	
9	\paragraph{Why does steering fail in Qwen and Gemma?}
10	Three hypotheses merit consideration: (1)~non-linear causal interactions \citep{elhage2022toy}, where MLP probes gain $+9.2$~pp over linear probes on conflict but $-0.5$~pp on XNLI; (2)~superposition \citep{templeton2024scaling}, where conflict and XNLI weight vectors are near-orthogonal yet cross-task language transfer is near-perfect; (3)~architectural differences, as Qwen and Gemma show mid-layer transfer dips absent in Llama.
11	Definitive validation requires activation patching \citep{meng2022locating}.
12	
13	\paragraph{Relation to prior work.}
14	The ZH$\to$EN advantage matches the XNLI baseline across all models, indicating that asymmetry piggybacks on general cross-lingual alignment \citep{zhao2026when, kargaran2024mexa, wendler2024llamas}.
15	\citet{basu2026interpretability} reported steering failure despite 98.2\% AUROC; our L13 succeeds because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture.
16	
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-25T21:13:50.300967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-25T21:13:50.451806+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that knowledge conflict signals are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\to$EN transfer advantage (${\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.
5	Causal intervention reveals a detection--decision dissociation: all three models detect conflict signals, yet only Llama yields significant steering at L13 ($p < 0.001$); Gemma fails despite 88.9\% probe accuracy, confirming detection alone is insufficient for mechanistic claims.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-25T21:13:50.452250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-25T21:13:50.502764+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.
6	Typologically diverse language pairs and alternative intervention methods are needed to assess generality.
7	Null steering results in Qwen and Gemma may reflect limitations of single-direction linear steering rather than absence of causal structure; alternative methods such as activation patching \citep{meng2022locating} may reveal non-linear causal pathways that our approach cannot detect.
8	Second, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, which retains only questions where the model confidently knows the ground truth and may bias toward well-represented knowledge; additionally, Qwen3-8B serves as both the translation model and an experimental subject, though COMET-based quality control mitigates this concern, and the fact that Llama and Gemma, architecturally independent of the translation model, show the same asymmetry pattern ($\Delta_{\text{asym}} = +7.3$ and $+6.6$~pp, respectively) provides cross-validation that the effect is not an artifact of Qwen-specific translation biases.
9	Third, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; while peak balanced accuracy remains stable across seeds (Llama $\pm$0.12\%, Gemma $\pm$1.32\%, Qwen $\pm$1.90\%), the specific peak layer can shift.
10	We acknowledge that $k$-fold cross-validation would provide stronger stability guarantees \citep{belinkov2022probing}; given that our core claims rest on cross-model consistency and directional patterns rather than exact accuracy values, the current cross-seed stability analysis provides partial mitigation, and we commit
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-25T21:13:57.660636+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
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

_source line 375 · 2026-05-25T21:13:57.811646+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-25T21:14:03.286001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-25T21:14:05.394019+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-25T21:14:05.444581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-25T21:14:10.564583+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, here's what I found about EMNLP 2026 call for papers submission guidelines with ARR:

## Key Submission Guidelines:

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR-Specific Policy:

For the ARR 2026 May cycle aligned with EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026—ARR submissions that do not select EMNLP 2026 during submission will no
…[truncated 620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 7278
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-25T21:14:16.486694+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind anonymity",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind anonymity",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-25T21:14:17.339819+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-25T21:14:31.251359+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind anonymity"

Links: [{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LM Playschool: Improving Language Models through Learning from Dialogue Interaction | ACL Member Portal","url":"https://www.aclweb.org/portal/content/lm-playschool-improving-language-models-through-learning-dialogue-game-interaction"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"}]

Now let me search more specifically for EMNLP 2026 main conference paper submission guidelines:

Links: [{"title":"Call for M
…[truncated 6201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "WebSearch",
  "elapsed_ms": 14764
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-25T21:14:31.252461+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/decisions.yaml\", \"content\": \"_next_id: 21\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 12:00 UTC\\n  summary: MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性\\n  rationale: Track 1（探针迁移）是整个 3-track 研究的基础前提。如果残差流中无法检测冲突信号或跨语言完全不迁移，后续 SAE 分析和 steering\\n    均无意义。选 Qwen3-8B-Instruct 因 Qwen-Scope 提供 base SAE 便于后续 Track 2。选 EN+ZH 因语系距离大，若迁移成功则信号强。ConflictQA\\n    公开可用，无需等 CLEAR 数据。Pass/fail 标准参考 Brink et al. 单语 0.96 F1 和 Zhao et al. ~90% 探针精度。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 12:06 UTC\\n  summary: 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% conditional pass 定义、layer-wise\\n    量化标准、统计显著性要求（binomial p<0.01）、翻译 COMET gate（≥0.80）、FAIL→retry Llama 行动路径\\n  rationale: Reviewer 指出原 gate criteria 存在 ambiguous zone（70-79% 无定义）、layer-wise pattern\\n    逃逸条款过于模糊、ZH 60% 阈值缺统计锚定、翻译质量是迁移失败的混淆因素、FAIL 后行动未定义。全部采纳以确保 MVP 结论可靠。FAIL→retry\\n    on Llama 给予一次排除模型特异性的机会，两模型均 FAIL 才 kill。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 14:26 UTC\\n  summary: 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集\\n  rationale: Llama verify 保留率仅 33%（266/800 train），低于 300 阈值。ConflictQA 有 ~10K 条，扩至\\n    2000 可保证两模型各自 ≥300 有效样本。取消交集策略因为强制交集会进一步损失样本量，且跨模型对比不要求相同样本——各自 verified 集上报告相同指标即可，交集作为补充分析。20%\\n    标签翻转率确认了 M001 verify 步骤的必要性。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: triggered_decision\\n    result: verify 保留率 33%, 266 train / 70 test, 20% flip\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-21 19:17 UTC\\n  summary: Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨语言迁移不对称（ZH→EN 71.3% vs\\n    EN→ZH 59.6%），等 Qwen 结果做最终 verdict\\n  rationale: Llama 4 方向探针结果显示冲突信号可线性检测（所有方向 p < 0.01），但 EN→EN 未达 80% PASS 阈值（77.6%）。跨语言迁移存在但高度不对称：ZH→EN\\n    强迁移（71.3%），EN→ZH 弱迁移（59.6%，刚好低于 60% point 阈值但 p=9.7e-4 仍显著）。CONDITIONAL PASS 按\\n    D002 规则进入 EXTEND 评估。等 Qwen 跨模型
…[truncated 10909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 13912
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-25T21:14:39.033548+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-25T21:14:39.084150+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-25T21:14:43.349296+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-25T21:14:43.801214+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'clkc_mech_interp'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-25T21:14:44.755144+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-25T21:14:45.107065+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-25T21:14:45.107506+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-25T21:14:45.208159+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.venv/lib/python3.14/site-packages/configs/config.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-25T21:14:49.073373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-25T21:14:49.575981+00:00_

1	issues:
2	# === Round 3 NEW ISSUES ===
3	
4	- id: "R3-N1"
5	  summary: "标题 'Mirror' 等价性主张与 TOST 功效(1.4%)不匹配"
6	  category: framing
7	  severity: critical
8	  status: in_progress
9	  first_raised_round: 3
10	  last_seen_round: 3
11	  mentions:
12	    - round: 3
13	      reviewers: [1, 2]
14	      note: "R1 提出 TOST power 角度，R2 AGREE 并补充标题-正文一致性问题。BF₀₁≈1.5 仅 modest evidence。建议改 Mirror→Consistent With"
15	  action_items:
16	    - round: 3
17	      action: "标题 Mirror→Consistent With + Figure 3 灰色带处理 + 全文 mirror→consistent with 替换"
18	      assigned_to: paper_agent
19	      status: done
20	  resolution: "标题改为 'Are Consistent With'，全文6处替换，Figure 3 caption 改为 exploratory equivalence margin。Reviewer 验证零 mirror 残留。"
21	  resolution_round: null
22	
23	- id: "R3-N2"
24	  summary: "COMET tercile 消融 MDD=25.3pp 混淆排除功效不足"
25	  category: experiment
26	  severity: critical
27	  status: in_progress
28	  first_raised_round: 3
29	  last_seen_round: 3
30	  mentions:
31	    - round: 3
32	      reviewers: [1, 2]
33	      note: "R1 认为'本质上无效'，R2 部分反驳——多证据链(token overlap+EN-DE对照)部分弥补"
34	  action_items:
35	    - round: 3
36	      action: "§4.5 重构：论证重心从 COMET tercile 转向 token overlap + EN-DE 对照；COMET 降为辅助证据"
37	      assigned_to: paper_agent
38	      status: done
39	  resolution: "§4.5 重构完成：Token overlap + EN-DE 控制为主论证，COMET tercile 降为辅助，MDD 限制明确标注。Reviewer 确认结构正确。"
40	  resolution_round: null
41	
42	- id: "R3-N3"
43	  summary: "因果证据仅限 Llama L13 单模型单层，不足以支撑跨架构 claim"
44	  category: method
45	  severity: critical
46	  status: in_progress
47	  first_raised_round: 3
48	  last_seen_round: 3
49	  mentions:
50	    - round: 3
51	      reviewers: [1, 2]
52	      note: "Contribution 2 暗示跨架构系统性发现，实为 1正2负"
53	  action_items:
54	    - round: 3
55	      action: "Contribution 2 重写限定为 Llama-specific + 三层解离证据 + Abstract 重构"
56	      assigned_to: paper_agent
57	      status: done
58	  resolution: "Contribution 3 改为 'Detection-decision dissociation in Llama-3.1-8B-Instruct'，三层解离(L28/L18/L13)写入，Abstract 限定。Rev
…[truncated 15057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-25T21:14:49.827627+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-25T21:14:52.595958+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:44:{"ts": "2026-05-24T14:54:38.561036+00:00", "role": "tool", "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review", "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp", "output_mode": "content"}}
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:45:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:50:{"ts": "2026-05-24T14:54:58.216727+00:00", "role": "tool", "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review|paperreview", "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/registry.yaml", "output_mode": "content"}}
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_director.jsonl:52:{"ts": "2026-05-24T14:54:58.871161+00:00", "role": "tool", "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review|paperreview", "path": "/home/ubuntu/.agent-ml-research-prod42", "glob": "**/project*.yaml", "output_mode": "content"}}
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/l
…[truncated 13426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "Grep",
  "elapsed_ms": 2768
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-25T21:15:16.219221+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "clkc_mech_interp",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "clkc_mech_interp",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-25T21:15:31.965688+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15746
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-25T21:15:32.016320+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ARR)\n- **Deadline**: 2026-06-15\n- **格式**: ACL 模板，Long paper 正文 8 页限制（references 不限），Limitations 必需且不计页数\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex`（各章节为独立 .tex 文件同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格评估：\n\n1. **统计有效性**：p 值校正是否恰当（Bonferroni）、CI 解释是否正确、bootstrap 方法是否合理、样本量是否充分支撑所述结论\n2. **因果声明**：steering 实验的因果推断是否成立、random control 是否充分、L13 单层单模型成功能否支撑\"detection≠decision\"这一跨模型 claim\n3. **实验设计**：confound exclusion 的逻辑链是否完整（COMET tercile 功效问题、token overlap、EN-DE 对照）、单 train/test split 的局限性\n4. **可重复性**：实验细节是否充分（超参、硬件、随机种子）、seed replication 是否充分验证\n5. **多重比较**：全文共多少假设检验，family-wise error rate 控制是否恰当\n\n请输出标准 ARR 审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: critical/warning/info)\n- Questions to Authors\n- Missing References (如有)\n- Overall Assessment (1-5 分，参照 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit)\n- Confidence (1-5)\n\n**严格评审，不留情面。**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ARR)\n- **Deadline**: 2026-06-15\n- **格式**: ACL 模板，Long paper 正文 8 页限制（references 不限），Limitations 必需且不计页数\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex`（各章节为独立 .tex 文件同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格评估：\n\n1. **统计有效性**：p 值校正是否恰当（Bonferroni）、CI 解释是否正确、bootstrap 方法是否合理、样本量是否充分支撑所述结论\n2. **因果声明**：steering 实验的因果推断是否成立、random control 是否充分、L13 单层单模型成功能否支撑\"detection≠decision\"这一跨模型 claim\n3. **实验设计**：confound exclusion 的逻辑链是否完整（COMET tercile 功效问题、token overlap、EN-DE 对照）、单 train/test split 的局限性\n4. **可重复性**：实验细节是否充分（超参、硬件、随机种子）、seed replication 是否充分验证\n5. **多重比较**：全文共多少假设检验，family-wise error rate 控制是否恰当\n\n请输出标准 ARR 审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: critical/warning/info)\n- Questions to Authors\n- Missing References (如有)\n- Overall Assessment (1-5 分，参照 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit)\n- Confidence (1-5)\n\n**严格评审，不留情面。**"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-25T21:15:45.915490+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13899
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-25T21:15:46.116750+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ARR)\n- **Deadline**: 2026-06-15\n- **格式**: ACL 模板，Long paper 正文 8 页限制（references 不限），Limitations 必需且不计页数\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex`（各章节为独立 .tex 文件同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格评估：\n\n1. **新颖性 (Novelty)**：\n   - 相对 Zhao et al. 2024（monolingual conflict probing）的增量是否足够？\n   - 相对 Basu et al. 2026（detection≠steering）的差异化是否清晰？\n   - \"asymmetry reflects general cross-lingual structure\" 是否构成独立 contribution 还是 null result repackaging？\n   - 四个 contribution 的权重是否均衡？\n\n2. **Related Work 覆盖**：\n   - 跨语言 steering 领域：Pokharel 2026, Sundar 2025, Gurgurov 2026 是否充分讨论？\n   - 知识冲突 taxonomy 和 mitigation 方向是否有重要遗漏？\n   - 信息论 probing 视角（Pimentel 2021, Ravichander 2021）是否充分整合？\n\n3. **叙事结构 (Narrative)**：\n   - Introduction 三个研究问题的设置是否 self-contained？\n   - 论文核心 claim 从 Abstract→Intro→Results→Discussion→Conclusion 是否一致？\n   - \"detection≠decision\" dissociation 作为核心卖点的叙事是否 convincing？\n\n4. **写作质量**：\n   - Abstract 是否在 200 words 以内？\n   - 是否存在 overclaiming（标题/Abstract vs 实际实验范围）？\n   - 图表是否 informative 且 self-contained？\n\n5. **格式合规**：\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否存在且位置正确？\n   - 匿名化是否完整（无 self-citation 泄露）？\n\n请输出标准 ARR 审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: critical/warning/info)\n- Questions to Authors\n- Missing References (如有)\n- Overall Assessment (1-5 分，参照 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit)\n- Confidence (1-5)\n\n**严格评审，不留情面。**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ARR)\n- **Deadline**: 2026-06-15\n- **格式**: ACL 模板，Long paper 正文 8 页限制（references 不限），Limitations 必需且不计页数\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex`（各章节为独立 .tex 文件同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格评估：\n\n1. **新颖性 (Novelty)**：\n   - 相对 Zhao et al. 2024（monolingual conflict probing）的增量是否足够？\n   - 相对 Basu et al. 2026（detection≠steering）的差异化是否清晰？\n   - \"asymmetry reflects general cross-lingual structure\" 是否构成独立 contribution 还是 null result repackaging？\n   - 四个 contribution 的权重是否均衡？\n\n2. **Related Work 覆盖**：\n   - 跨语言 steering 领域：Pokharel 2026, Sundar 2025, Gurgurov 2026 是否充分讨论？\n   - 知识冲突 taxonomy 和 mitigation 方向是否有重要遗漏？\n   - 信息论 probing 视角（Pimentel 2021, Ravichander 2021）是否充分整合？\n\n3. **叙事结构 (Narrative)**：\n   - Introduction 三个研究问题的设置是否 self-contained？\n   - 论文核心 claim 从 Abstract→Intro→Results→Discussion→Conclusion 是否一致？\n   - \"detection≠decision\" dissociation 作为核心卖点的叙事是否 convincing？\n\n4. **写作质量**：\n   - Abstract 是否在 200 words 以内？\n   - 是否存在 overclaiming（标题/Abstract vs 实际实验范围）？\n   - 图表是否 informative 且 self-contained？\n\n5. **格式合规**：\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否存在且位置正确？\n   - 匿名化是否完整（无 self-citation 泄露）？\n\n请输出标准 ARR 审稿格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: critical/warning/info)\n- Questions to Authors\n- Missing References (如有)\n- Overall Assessment (1-5 分，参照 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit)\n- Confidence (1-5)\n\n**严格评审，不留情面。**"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-25T21:15:47.627725+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 402 · 2026-05-25T21:15:53.702763+00:00_

Round 1 已启动：

- ✅ 视觉审查 Agent 已派发（并行执行，不阻塞）
- ✅ Reviewer 1（方法严谨性）已分配
- ✅ Reviewer 2（新颖性/完整性）已分配
- ❌ 外部审稿：未配置，跳过

等待两位 Reviewer 返回独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 403 · 2026-05-25T21:23:32.408016+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性与完整性

## Summary

本文将知识冲突信号的 probing 分析从单语（Zhao et al. 2024）扩展到跨语言（英-中）设置，使用三个 LLM（Llama-3.1-8B-Instruct、Qwen2.5-8B、Gemma-2-9B-IT）进行残差流探测、XNLI 非冲突基线对照、COMET 混淆因素排除和因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN 迁移优势约 7pp，与 XNLI 基线一致，反映一般跨语言结构而非冲突特异性；(3) 因果 steering 仅在 Llama L13（41% 深度）成功，Qwen/Gemma 无显著因果效应，表明检测不蕴含因果相关性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 方法论扎实（bootstrap CI、Bonferroni 校正、Fisher 精确检验），混淆因素控制设计优秀。但核心 claim（detection≠decision）仅 1/3 模型支持，单一 train/test split 影响可靠性 |
| Excitement | 2.5/5 | Probing 跨语言扩展属增量贡献；最具新颖性的 detection-decision dissociation 已被 Basu et al. 2026 在单语设置中建立；asymmetry 发现为 null result |
| Reproducibility | 4/5 | 提供匿名代码仓库，方法描述清晰，统计方法完整。单一 split 限制精确数值复现 |
| Overall Assessment | **3.0/5 (Findings)** | 方法论可靠、控制设计好，适合 Findings 发表。但新颖性不足以达到主会议水平——核心发现要么是增量扩展、要么是 null result、要么是弱支撑的 claim |
| Confidence | 4/5 | 熟悉 probing/steering/跨语言表征文献，仔细通读全文含 Appendix |

---

## Strengths

**S1. 混淆因素控制设计出色。** COMET 翻译质量分层 + XNLI 非冲突基线的组合是一个真正的方法论贡献（Section 3.5, 4.4-4.5）。用 XNLI 作为非冲突对照来区分冲突特异性 vs. 一般跨语言不对称性，思路清晰且可复用。

**S2. 多模型验证增强泛化性。** 三个架构差异显著的模型（Llama/Qwen/Gemma）在检测能力上一致，强化了"冲突信号线性可检测"这一结论的可信度（Table 1, Figure 3）。

**S3. 统计方法规范。** Bootstrap CI（n=2000）、Bonferroni 校正（l=10 to α values）、Fisher 精确检验、matched-condition 控制，统计实践达到 top-venue 标准。

**S4. 诚实报告负面结果。** Qwen/Gemma steering 失败（Table 3）、asymmetry 非冲突特异性（Section 4.4）——这些负面结果的如实报告值得肯定，优于很多只报积极结果的论文。

**S5. Seed replication 加强因果 claim。** Appendix C 用独立 seed 复现了 Llama L13 steering 效果（N=201, 独立 train/test split），排除了单次 split 偶然性的可能。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] "Detection ≠ Decision" 核心 claim 支撑不足，且与 Basu et al. (2026) 差异化不清晰。**
- 具体位置：Abstract、Section 4.6、Table 3、Figure 5-6、Discussion (Section 5)
- 问题：
  (a) Basu et al. (2026) 标题即为 "Interpretability without actionability"，在单语设置中已经建立了 detection-steering 的 dissociation。本文的跨语言扩展未能清晰阐述相比单语设置的增量发现——跨语言设置具体揭示了哪些单语分析无法观察到的现象？
  (b) Representation steering 仅在 Llama L13（41% depth）产生显著因果效应（flip rate 19.9% vs. 6.6% random, Fisher p=0.002）。Qwen 和 Gemma 在所有层均无显著效应。即 2/3 模型不支持任何因果影响。
  (c) 即使在 Llama 中，相邻的 L16（50% depth）已无显著效应（p>0.12），因果窗口极窄。这可能是精确定位，但也可能是 fragile/model-specific artifact。
  (d) 论文将"steering 在 2/3 模型失败"框架为支持 dissociation 叙事，但另一种同样合理的解释是：线性探针并未捕捉因果相关特征，steering 方法本身（单一方向线性干预）太粗糙。
- 为什么影响接收：这是论文最核心的叙事卖点。如果 dissociation 已被 Basu et al. 建立、且跨语言扩展未增加实质发现，则论文的核心新颖性大幅下降。
- 建议修改方向：(1) 在 Section 2 添加与 Basu et al. 2026 的逐点对比段落，明确本文的增量在哪里；(2) 诚实重新定位——从"我们发现 detection≠decision"改为"跨语言设置下 detection≠decision 模式与单语一致"；(3) 考虑使用 activation patching（而非仅 linear steering）来检验因果性，增强方法多样性。

**N2 [critical] "General Cross-Lingual Asymmetries" 泛化声称仅基于单一语言对。**
- 具体位置：标题、Abstract ("consistent with general multilingual structure")、Contribution 2、Section 4.3-4.4
- 问题：论文标题声称 "General Cross-Lingual Asymmetries"，但实验仅覆盖英-中一个语言对。英语和中文有特殊属性（高类型距离、训练数据中英语占比极高），从一个语言对推断"一般跨语言结构"在统计上等同于 N=1 的泛化。Section 3.5 提到了 EN-DE 的 XNLI 控制实验，但仅用于混淆因素检查，未作为第二语言对的完整探测实验。
- 为什么影响接收：标题和核心 claim 的 scope 与实验证据不匹配。Reviewer 和 AC 对 overclaiming 非常敏感。
- 建议修改方向：(1) 增加至少 1-2 个类型差异大的语言对（如 EN-DE、EN-JA 或 EN-AR）；(2) 或将标题修改为 "English-Chinese Knowledge Conflict Signals..."，并在全文中软化 "general" 相关表述。

**N3 [critical] Contribution 2（asymmetry = general structure）本质是 null result 被包装为正面贡献。**
- 具体位置：Page 1 贡献列表第 2 条、Section 4.3-4.4、Figure 4
- 问题：发现迁移不对称性与 XNLI 基线一致 ＝ 不对称性不是冲突特异的 ＝ 这是一个 null result。将"没有发现冲突特异不对称性"列为独立贡献，膨胀了贡献计数。这更适合作为 Contribution 1（跨语言可检测性）的分析组成部分——作为一个重要的控制结果，而非独立贡献。
- 为什么影响接收：四个贡献中如果一个是 null result、一个弱支撑（detection≠decision），实质上只有两个站得住的贡献（可检测性 + 混淆因素排除），且可检测性本身是增量扩展。整体贡献量偏薄。
- 建议修改方向：将 asymmetry 发现并入 Contribution 1 的讨论，重新组织为 3 个贡献。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] 四个贡献的权重严重不均衡。**
- 具体位置：Page 1 贡献列表
- 问题：逐条分析——
  - C1（跨语言可检测性）：Zhao et al. 2024 单语→跨语言的增量扩展，预期性强
  - C2（asymmetry = general structure）：null result（见 N3）
  - C3（detection-decision dissociation）：仅 1/3 模型支持，且 Basu et al. 2026 已建立单语版本（见 N1）
  - C4（混淆因素排除）：真正的方法论贡献，但偏 methodological
- 没有一个贡献具有足够独立支撑 conference-level impact 的力度。

**W2 [warning] 单一 train/test split，缺乏交叉验证。**
- 具体位置：Section 3.3、Limitations
- 问题：所有 probing 结果基于单次 80/20 随机分割。作者在 Limitations 中承诺 camera-ready 提供 5-fold CV，但当前版本的探测准确率数字无法排除 split 敏感性。Appendix C 的 seed replication 仅覆盖 steering，不覆盖 probing accuracy。
- 建议：在当前版本中至少报告 3-fold CV 的 mean±std。

**W3 [warning] Steering 分析样本量小、多重比较负担重。**
- 具体位置：Section 4.6、Table 3
- 问题：Matched-condition steering 使用 N=131-201。同时在 ~30 层 × 10 个 α 值 × 4 个方向上搜索，即使 Bonferroni 校正后，小样本下的统计功效（power）很低。这增加了 false negative（Qwen/Gemma）和 false positive（Llama L13）的风险。
- 建议：报告 power analysis，或增加 matched-condition 数据量。

**W4 [warning] 机制深度偏浅——定位偏 empirical probing，非 mechanistic interpretability。**
- 具体位置：全文
- 问题：论文定位于"mechanistic interpretability"（标题所属领域），但分析停留在残差流整体层面——标准 logistic regression 探针。没有 attention head 或 MLP 层面的分解，没有 circuit-level 分析，没有探究 probe 学到了什么具体特征。这更接近"empirical probing study"而非"mechanistic interpretability"。
- 建议：(1) 增加 attention vs. MLP contribution 的分解分析；或 (2) 在 Related Work / framing 中将论文重新定位为 "empirical cross-lingual probing study"。

**W5 [warning] Related Work 缺少跨语言知识编辑文献。**
- 具体位置：Section 2
- 问题：跨语言知识编辑（cross-lingual knowledge editing）是一个活跃的相关领域——ROME/MEMIT 在多语言模型中的编辑传播失败（如 "Editing Across Languages" survey, 2025; CLM-Bench, 2026）与本文发现的跨语言 probe 不对称性在机制上可能共享同一原因（语言特定的激活模式）。Section 2 完全未提及这一方向。
- 建议：增加一小段讨论跨语言知识编辑的传播失败现象，与本文的 asymmetry 发现建立联系。

**W6 [info] 缺少 Conclusion 章节。**
- 具体位置：Section 5 → Limitations，无 Section 6
- 问题：论文从 Discussion 直接跳到 Limitations，没有独立的 Conclusion。虽非格式违规，但缺少一个干净的叙事收尾，影响可读性。

---

## Questions to Authors

**Q1.** Basu et al. (2026) "Interpretability without actionability" 已在单语设置下论证 detection ≠ steering。本文的跨语言扩展具体揭示了哪些单语分析观察不到的现象？请明确阐述 incremental novelty。

**Q2.** Llama L13 steering 有效但 L16（仅 3 层之差）即无效（p>0.12）。是否测试了 L14 和 L15？如何解释这个极窄的因果窗口？

**Q3.** Section 3.5 已将 ConflictQA 翻译为德语作为 XNLI 控制。为何不将 EN-DE 作为第二语言对进行完整的 probing 实验，以直接支持"general cross-lingual"的 claim？

**Q4.** COMET 分层排除（Section 4.5）使用 tercile 阈值。结果对该阈值敏感度如何？quartile 或 median split 下结论是否一致？

**Q5.** Gemma 的 ConflictQA 正确回答率最低（966/1590），但探测准确率最高（EN→EN 88.9%）。这种背离是否暗示 probe 捕获的是任务无关的信号？

---

## Missing References

1. **跨语言知识编辑传播**: "Editing Across Languages: A Survey of Multilingual Knowledge Editing" (2025) 和 CLM-Bench (2026) 探讨了 ROME/MEMIT 在多语言中的传播失败——与本文的 asymmetry 发现机制上相关。
2. **跨语言知识编辑基准**: BMIKE-53 (53 语言知识编辑基准) 提供了跨语言知识操作的系统性证据。

（Director 指定的 Pokharel 2026、Sundar 2025、Gurgurov 2026、Pimentel 2021、Ravichander 2021 均已在论文中引用 ✓）

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文页数 ≤ 8 页 | ✓ Sections 1-5 在 pp.1-8 |
| Limitations section 存在 | ✓ p.9，正文后 references 前 |
| Limitations 不计入页数 | ✓ 在第 9 页 |
| Abstract ≤ 200 words | ✓ 约 164 words |
| Double-blind 匿名化 | ✓ "Anonymous ACL submission"，代码用 anonymous.4open.science |
| 自引泄露 | 未发现明显泄露 |
| ACL 模板 | ✓ 标准 ACL 格式 |

---

## 主要优势总结

- 混淆因素控制设计（COMET + XNLI）是可复用的方法论贡献
- 多模型一致的检测能力增强了泛化性
- 统计方法规范、负面结果诚实报告
- 代码公开、AI 辅助使用透明声明

## 总体评分

**Overall: 3.0/5 (Findings)**

**一句话总结**: 方法论扎实、控制设计好的跨语言 probing 研究，适合 Findings 发表，但核心新颖性不足以达到主会议水平——最有新意的 detection≠decision claim 仅 1/3 模型支持且已被 Basu et al. 2026 在单语中建立，"general cross-lingual" 的泛化声称仅基于单一语言对。

---

Sources:
- [ARR Review Form](https://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 404 · 2026-05-25T21:23:44.803885+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成独立初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 405 · 2026-05-25T21:23:48.368381+00:00_

[Reviewer 2 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，核心判断：

- **Overall: 3.0/5 (Findings)**
- **3 个 critical 问题**：(1) detection≠decision 核心 claim 仅 1/3 模型支持且与 Basu et al. 2026 差异化不清晰；(2) "General Cross-Lingual" 泛化声称仅基于英-中单一语言对；(3) asymmetry 发现是 null result 被包装为正面贡献
- **5 个 warning 问题**：贡献权重不均衡、单一 split 无 CV、steering 样本小、机制深度不足、缺少跨语言知识编辑文献
- **格式合规**：全部通过（8 页正文、Limitations 存在、Abstract ≤200 words、匿名化完整）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 406 · 2026-05-25T21:23:57.314189+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 27

## Round 27

6 recorded events
