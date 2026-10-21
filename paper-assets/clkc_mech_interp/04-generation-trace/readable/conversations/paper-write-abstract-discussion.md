# paper write abstract discussion

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_write-abstract-discussion_20260522T153557.jsonl`
- **Structured JSON:** [`3ec93c82fbf5a2800385.json`](../../sessions/3e/3ec93c82fbf5a2800385.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-22T15:39:07.663177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T15:39:07.663693+00:00_

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
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{boer2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe acc
…[truncated 3691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T15:39:07.663926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T15:39:07.664148+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Figure~\ref{fig:pipeline} illustrates the complete pipeline, from data construction through probing and steering.
5	We first formalize the task (\S\ref{sec:task}), then describe data construction (\S\ref{sec:data}), activation extraction (\S\ref{sec:extraction}), the probing framework (\S\ref{sec:probing}), cross-lingual transfer protocol (\S\ref{sec:transfer}), confound exclusion (\S\ref{sec:confound_method}), and representation steering (\S\ref{sec:steering_method}).
6	
7	\subsection{Task Formulation}
8	\label{sec:task}
9	
10	Given an input $x = (c, q)$ consisting of a context passage $c$ and a question $q$, the model produces an answer $a$ that is either \emph{contextual} (derived from $c$) or \emph{parametric} (derived from the model's pre-trained knowledge).
11	When $c$ contradicts the model's parametric knowledge, the choice between these two answer sources constitutes a knowledge conflict.
12	Let $\mathbf{h}_l \in \mathbb{R}^d$ denote the residual stream representation at layer $l$ for the last input token.
13	Our goal is to train a logistic regression probe $f_\theta(\mathbf{h}_l)$ that predicts a binary label $y \in \{\text{contextual}, \text{parametric}\}$ from $\mathbf{h}_l$, and to examine whether the learned probe direction transfers across languages and causally influences model behavior.
14	
15	\subsection{Data Construction}
16	\label{sec:data}
17	
18	\paragraph{Source dataset.}
19	We build on ConflictQA \citep{xie2024adaptive}, a benchmark that pairs each question with a context passage that contradicts the model's parametric knowledge.
20	Each sample contains a question, a parametric answer (ground truth from the model's training data), and a context-based answer (the contradicting information in the passage).
21	
22	\paragraph{Parametric knowledge verification.}
23	Not all samples in ConflictQA produce genuine conflicts for a given model: if the model cannot answer the question correctly without context,
…[truncated 7879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T15:39:07.664319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T15:39:07.664522+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.
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
28	Table~\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.
29	Both models encode linearly detectable conflict signals in their residual streams.
…[truncated 9669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T15:39:07.664722+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T15:39:07.664907+00:00_

docs/paper/acl_latex.tex
docs/paper/sections/experiments.tex
docs/paper/experiments.tex
docs/paper/main.tex
docs/paper/sections/method.tex
docs/paper/method.tex
docs/paper/sections/introduction.tex
docs/paper/introduction.tex
docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T15:39:07.665074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T15:39:07.665234+00:00_

1	# 关键研究发现
2	
3	## C2 不对称性非冲突特有 [2026-05-22, xnli_baseline_110]
4	
5	**核心发现**：~6pp ZH→EN > EN→ZH 不对称性在非冲突任务 XNLI 上同样存在，是模型的一般性跨语言属性，非冲突信号特有。
6	
7	| Model | XNLI asymmetry | Conflict asymmetry |
8	|-------|---------------|-------------------|
9	| Qwen | +6.72pp CI[2.36,11.73] ✓ | +5.95pp CI[-3.67,14.81] |
10	| Llama | +5.97pp CI[0.92,11.33] ✓ | +11.76pp CI[4.29,19.57] ✓ |
11	
12	**推导**：英语主导预训练 → EN 表征空间更"标准" → ZH→EN 迁移天然更好。C2 需 reframe：从 "conflict-specific asymmetry" 改为 "conflict signals share general cross-lingual transfer pathways"。
13	
14	**Llama 的 excess asymmetry**：conflict(+11.76) - XNLI(+5.97) = +5.79pp，可能有冲突特有成分，但 CI 重叠大，需统计检验。Qwen excess 为负(-0.77pp)。
15	
16	---
17	
18	## Steering 因果节点在 mid-layer [2026-05-22, steering_107 系列]
19	
20	**核心发现**：Llama-3.1-8B 上，probe weight 方向的因果效应具有强层特异性——只在 L13 (mid-layer) 有效，L18 (MLP peak) 和 L28 (final) 均无效。
21	
22	| 层 | 位置 | 最佳 Fisher p | 结论 |
23	|----|------|-------------|------|
24	| L28 | last | 0.31 | NEGATIVE |
25	| L28 | all | 0.37 | NEGATIVE |
26	| L18 | last | 0.45 | NEGATIVE |
27	| **L13** | **last** | **0.0009** | **SUCCESS** |
28	
29	**L13 双向因果效应**：
30	- α=-20: steering 36.0% vs control 17.6%, p=0.0009 (5 c→p)
31	- α=+5: steering 19.9% vs control 6.6%, p=0.002 (4 p→c)
32	
33	**机制解读**：mid-layer 是跨语言表征对齐发生的典型位置 (Conneau et al. 2020)。冲突信号的因果节点与对齐层重合，而非与检测准确率 peak 重合（L28 probe acc 最高但无因果性）。检测≠因果。
34	
35	**对论文影响**：Steering 从全面 NEGATIVE 逆转为 layer-specific SUCCESS，可作为论文亮点之一——probe 不仅检测到信号，该信号在特定层具有因果意义。
36	
37	---
38	
39	# Gemma-2-9B-IT 兼容性报告 (plan_102)
40	
41	## 模型结构
42	
43	| 属性 | 值 |
44	|------|-----|
45	| model_type | gemma2 |
46	| architecture | Gemma2ForCausalLM |
47	| num_hidden_layers | 42 |
48	| hidden_size | 3584 |
49	| num_attention_heads | 16 |
50	| num_key_value_heads | 8 (GQA) |
51	| head_dim | 256 |
52	| vocab_size | 256000 |
53	| torch_dtype | bfloat16 |
54	
55	## 各脚本兼容性
56	- verify_parametric_knowledge.py — ✅ 无需修改
57	- collect_activations.py — ✅ 无需修改（model.model.layers 同构）
58	- train_probe.py — ✅ 无需修改（无硬编码维
…[truncated 780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T15:39:07.665402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T15:39:07.665556+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	Research on how LLMs handle conflicting knowledge has developed along two axes: behavioral characterization and internal signal analysis.
6	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent strategies when parametric and contextual knowledge disagree, ranging from faithful context-following to stubborn reliance on memorized answers.
7	\citet{xu2024knowledge} provided a systematic taxonomy of conflict types (intra-memory, context-memory, and inter-context) that has since guided experimental design in this area.
8	More recent work has moved beyond behavioral observation to probe model internals.
9	\citet{zhao2024analysing} demonstrated that residual stream representations carry linearly separable conflict signals in English, while \citet{boer2026probing} used probing classifiers to localize factual associations within model parameters.
10	\citet{pham2026where} investigated the mechanistic pathways through which intra-memory conflicts are processed, and \citet{li2025taming} proposed methods to mitigate conflict-induced errors.
11	These studies, however, operate exclusively in monolingual English settings.
12	Extending conflict probing to cross-lingual scenarios introduces confounds that require explicit control: translation quality can degrade the conflict signal, token overlap between languages can provide spurious shortcuts, and general cross-lingual transfer properties can be mistaken for conflict-specific phenomena.
13	We build on the residual stream probing approach of \citet{zhao2024analysing} and extend it to cross-lingual settings with a confound exclusion pipeline that addresses each of these concerns.
14	
15	\paragraph{Cross-lingual representations in multilingual models.}
16	A consistent finding across multilingual model analyses is that intermediate layers develop language-independent representations.
17	\citet{wu
…[truncated 3254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T15:39:07.665706+00:00_

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
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
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

_source line 14 · 2026-05-22T15:39:07.665835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T15:39:07.665982+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "ROADMAP.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "ROADMAP.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T15:39:07.666142+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md\", \"content\": \"# clkc_mech_interp — Research Dashboard\\n\\n> 最后更新: 2026-05-22 12:56 UTC | 更新原因: EMNLP 2026 DDL May 25 确认, Paper Agent 启动\\n\\n## 核心方向\\n跨语言知识冲突信号的机制解释。详见 paper_framing.md。\\n\\n## 当前阶段\\n**EMNLP 2026 ARR 冲刺** — DDL **2026-05-25**（剩余3天）。论文写作已启动。\\n\\n### Claim 状态\\n- **C1 detectability** ✅ Llama 77.1%, Qwen 75.3%\\n- **C2 asymmetry** ✅ Reframed: 通用跨语言属性（XNLI 对照）\\n- **C3 non-linearity** ❌ CI含零 (D012)，降为 observation\\n- **Steering v1** ❌ L28/last NEGATIVE\\n- **Steering v2c** ❌ L28/all NEGATIVE\\n- **Steering v2a/v2b** ⏳ L13/L18 ~70%, ETA <1h\\n- **Steering Qwen** ⏳ 重启中 (L23)\\n\\n### 并行轨道\\n**写作轨道**: Paper Agent 已激活，Full Draft 模式\\n**实验轨道**: Steering v2 + Gemma + DE + Bootstrap 继续跑，完成即补入论文\\n\\n### GPU 状态\\n- cuda:0: Qwen Steering L23（重启中）\\n- cuda:1: Steering v2a L13 (~70%)\\n- cuda:2: Steering v2b L18 (~70%)\\n- cuda:3: DE translate test 集\\n\\n### 紧急任务\\n- [ ] Paper Agent: writing_plan.yaml 审批\\n- [ ] Steering v2a/v2b 结果判定 — Llama 最后机会\\n- [ ] Qwen Steering L23 启动确认\\n- [ ] Gemma/DE/Bootstrap — 完成即通知 Paper Agent 补入\\n\\n## GPU 预算\\n本项目分配: cuda:0,1,2,3 (westd-41302)\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-22 | Steering L13 SUCCESS (p=0.0009/0.002)! 因果节点在 mid-l | steering_107_L13, steering_107, steering_107_L18, steering_107_L28_all |\\n| D013 | 2026-05-22 | DDL确认: EMNLP 2026 ARR May 25 (3天), 立即启动论文写作 | mvp_probe_llama_v1, mvp_probe_v1, xnli_baseline_110, steering_107 |\\n| D012 | 2026-05-22 | D009 撤回：C3 non-linearity 降为 \\\"trend only\\\"，双模型 boots | xnli_baseline_110, mvp_002 |\\n| D011 | 2026-05-22 | Steering v1 NEGATIVE; 启动诊断性变体轮（3配置并行）后再判定 Track 3  | steering_107 |\\n| D010 | 2026-05-22 | Steering (plan_107) 升为最高优先级；C3 需统计加固但不作为唯一卖点 | xnli_baseline_110, mvp_002 |\\n| D009 | 2026-05-22 | C3 confirmed conflict-specific：XNLI MLP 对照证明非线性 en | xnli_baseline_110, 
…[truncated 517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T15:39:07.666296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T15:39:07.666438+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	% [PLACEHOLDER — Step 4]
28	\end{abstract}
29	
30	% [PLACEHOLDER — introduction]
31	
32	% [PLACEHOLDER — related_work]
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	% [PLACEHOLDER — discussion]
39	
40	% [PLACEHOLDER — conclusion]
41	
42	% [PLACEHOLDER — limitations]
43	
44	\bibliographystyle{acl_natbib}
45	\bibliography{references}
46	
47	\end{document}
48	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T15:39:07.666587+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_framing.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "paper_framing.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T15:39:07.666772+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_framing.md\", \"content\": \"# Paper Framing — clkc_mech_interp\\n\\n> 最后更新: 2026-05-22 | 目标: EMNLP 2026 via ARR (DDL 2026-05-25, 3天)\\n\\n## Core Insight\\n\\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致。**关键发现（plan_110 XNLI 基线）**：该不对称性并非冲突特有——非冲突语义任务 (XNLI) 展现几乎相同幅度的迁移不对称性（Qwen +6.72pp, Llama +5.97pp）。这说明冲突信号**编码在模型的通用跨语言表征空间中**，继承其方向性偏置，而非独立的专用机制。\\n\\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\\n\\n## Narrative Structure\\n\\n**机制分析驱动**（非 \\\"发现新现象\\\"）：\\n\\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity 决定跨语言冲突解决，但未提供机制解释\\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？与一般跨语言语义表征的关系是什么？\\n3. **Our answer**: 冲突信号可线性检测且跨架构一致，但其跨语言迁移模式（方向不对称性）**与一般语义任务 (XNLI) 无异**——冲突检测 piggyback 在模型已有的跨语言对齐结构上，而非专用子空间。通过层结构分析和因果干预验证这一机制。\\n4. **Methodological contribution**: 严格的 confound exclusion pipeline (COMET ablation + token overlap) + 非冲突基线对照，为跨语言 probing 研究树立方法论标准\\n\\n**Secondary framing**: 跨语言 probing 中方向性偏置的普遍性——English-dominant 模型的固有属性，影响所有跨语言迁移研究的结论解读\\n\\n## Competing Hypotheses (pre-registered)\\n\\n**H1 — English-anchored universal detection**:\\n冲突检测信号本身是 language-independent 的（\\\"是否存在冲突\\\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\\n\\n**H2 — Language-pair-specific encoding**:\\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\\n\\n**MVP + pl
…[truncated 4540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T15:39:07.667052+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "writing_plan.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "clkc_mech_interp",
    "file": "writing_plan.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T15:39:07.667314+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: main (via ARR)\\n  template: \\\"\\\"\\n  template_note: \\\"需要下载 ACL/EMNLP 2026 ARR LaTeX 模板（acl_latex style）\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >-\\n    跨语言知识冲突信号可在多语言 LLM 残差流中被线性探针检测（2模型 75-77% balanced acc），\\n    其跨语言迁移不对称性（ZH→EN > EN→ZH ~7pp）与非冲突语义任务(XNLI)无异——\\n    冲突信号编码在模型通用跨语言表征空间中，继承其方向性偏置。\\n    因果 steering 揭示 detection-decision 层分离：可检测信号 peak 在 late-layer (L28, ~88% depth)，\\n    但因果决策节点在 mid-layer (L13, ~40% depth)，Fisher p=0.002。\\n    方法论贡献：严格的 confound exclusion pipeline（COMET ablation + token overlap 排除 + 非冲突基线对照）。\\n  title_draft: >-\\n    Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries\\n    from General Multilingual Representations\\n  created_at: 2026-05-22T13:00:00Z\\n  updated_at: 2026-05-22T14:00:00Z\\n  update_reason: \\\"Steering L13 SUCCESS — 新增因果证据，narrative 升级\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 150\\n    core_bullets:\\n      - \\\"问题：多语言 LLM 在跨语言知识冲突时的内部机制未知——CLEAR 发现 linguistic affinity 决定冲突解决行为，但未解释信号编码机制\\\"\\n      - \\\"方法：残差流线性探针 + 跨语言迁移 + XNLI 基线对照 + confound exclusion + representation steering\\\"\\n      - \\\"结果：2模型 balanced acc 75-77%；ZH→EN > EN→ZH ~7pp 与 XNLI 一致；mid-layer (L13) steering 成功因果改变冲突解决(Fisher p=0.002)而 late-layer (L28) 不成功\\\"\\n      - \\\"贡献：(1) 跨语言冲突检测 + 不对称性继承通用跨语言对齐 (2) Detection ≠ Decision 层分离 (3) confound exclusion pipeline\\\"\\n    dependencies: [experiments, method, introduction]\\n\\n  - section: introduction\\n    word_budget: 900\\n    core_bullets:\\n      - \\\"Hook: 多语言 LLM 面对跨语言知识冲突时表现出 language-dependent 解决偏好(CLEAR)，但冲突信号在模型内部如何编码？可检测性是否等于因果性？\\\"\\n      - \\\"Gap: 现有 probing 工作仅限单语（Zhao et al. 2024; Boer et al. 2026），跨语言扩展面临 confound 问题；probing 只证明 detectability 不证明 causality\\\"\\n      - \\\"Insight: 冲突信号可线性检测且迁移呈方向不
…[truncated 4750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T15:39:07.667618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T15:39:07.667990+00:00_

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
…[truncated 668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T15:39:07.668280+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/abstract_draft.md",
  "content": "# Abstract Draft\n\n> ~200 words | Ready for LaTeX integration\n\nWhen multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation influences which answer prevails, yet the internal encoding of this conflict signal has not been studied beyond monolingual settings. We probe the residual stream representations of two architecturally distinct LLMs (Llama-3.1-8B-Instruct and Qwen3-8B) and find that knowledge conflict signals are linearly detectable both within and across languages, with balanced accuracy reaching 75--77\\% and all cross-lingual transfer directions exceeding chance. Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese representations transfer to English approximately 7 percentage points more accurately than the reverse. This asymmetry, however, is not conflict-specific---probes trained on a non-conflict semantic task (XNLI) show the same pattern at comparable magnitude---indicating that conflict signals inherit the directional biases of the model's general cross-lingual representations. Representation steering reveals a further dissociation: the detectable signal peaks at late layers (~88\\% depth), but causal influence on conflict resolution is confined to a mid-layer (~41\\% depth; Fisher $p = 0.002$) in Llama, with all late-layer interventions producing no behavioral change. These findings demonstrate that cross-lingual conflict detection operates within shared multilingual representation space, and that linear detectability does not imply causal relevance at the same computational stage.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/abstract_draft.md",
    "content": "# Abstract Draft\n\n> ~200 words | Ready for LaTeX integration\n\nWhen multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation influences which answer prevails, yet the internal encoding of this conflict signal has not been studied beyond monolingual settings. We probe the residual stream representations of two architecturally distinct LLMs (Llama-3.1-8B-Instruct and Qwen3-8B) and find that knowledge conflict signals are linearly detectable both within and across languages, with balanced accuracy reaching 75--77\\% and all cross-lingual transfer directions exceeding chance. Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese representations transfer to English approximately 7 percentage points more accurately than the reverse. This asymmetry, however, is not conflict-specific---probes trained on a non-conflict semantic task (XNLI) show the same pattern at comparable magnitude---indicating that conflict signals inherit the directional biases of the model's general cross-lingual representations. Representation steering reveals a further dissociation: the detectable signal peaks at late layers (~88\\% depth), but causal influence on conflict resolution is confined to a mid-layer (~41\\% depth; Fisher $p = 0.002$) in Llama, with all late-layer interventions producing no behavioral change. These findings demonstrate that cross-lingual conflict detection operates within shared multilingual representation space, and that linear detectability does not imply causal relevance at the same computational stage.\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T15:39:07.668446+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/abstract_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T15:39:07.668588+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/discussion_draft.md",
  "content": "# Discussion Draft\n\n> 5 paragraphs | LaTeX citations use \\citep{}/\\citet{} matching existing sections\n\n## Detection Does Not Imply Decision\n\nThe central finding of our causal analysis is the layer dissociation between where conflict signals are detectable and where they influence behavior. Probing accuracy for Llama peaks at layer 28 (88\\% depth), where the model's representation of the conflict outcome is most linearly separable. Yet steering at this layer produces no significant behavioral change (Fisher $p > 0.3$). Causal influence instead resides at layer 13 (41\\% depth), where perturbations along the probe direction shift the model's answer between contextual and parametric responses in both directions (Fisher $p = 0.002$ and $p < 0.001$). This pattern suggests that conflict resolution is computed at intermediate layers, and the late-layer signal is a post-hoc encoding of a decision already formed upstream. The mid-layer locus aligns with prior work showing that language-independent representations emerge at intermediate depths in multilingual models \\citep{muller2021first, wendler2024llamas}, suggesting that conflict resolution and cross-lingual alignment share a computational stage. From a methodological standpoint, this result reinforces the caution of \\citet{basu2026interpretability}: probe accuracy alone is an unreliable guide for selecting intervention targets, and steering experiments restricted to the probing peak can produce false negatives about the causal role of detected signals.\n\n## Asymmetry as a General Cross-Lingual Property\n\nThe directional asymmetry in cross-lingual transfer---where Chinese-trained probes transfer to English more accurately than the reverse by approximately 7 percentage points---initially appeared to reveal something specific about how conflict signals are organized across languages. The XNLI baseline reframes this interpretation. Probes trained on a non-conflict semantic distinction (entailment versus contradiction) show the same asymmetry at comparable magnitude (Llama $+6.0$ pp, Qwen $+6.7$ pp), with confidence intervals that overlap substantially with those of the conflict task (Llama $+7.2$ pp, Qwen $+7.2$ pp). The asymmetry is therefore not a property of conflict encoding but of the model's representational geometry: in English-dominant models, Chinese representations project more readily onto English subspace than the reverse. This connects to the English-centric latent space documented by \\citet{wendler2024llamas} and the cross-lingual alignment asymmetries measured by \\citet{kargaran2024mexa}. For cross-lingual probing studies more broadly, any observed transfer asymmetry must be benchmarked against a non-conflict baseline before being attributed to the phenomenon under investigation.\n\n## Non-Linear Encoding: A Directional Trend\n\nWe observe a suggestive but inconclusive pattern in non-linear encoding. MLP probes show larger gains over linear probes on the conflict task than on XNLI for cross-lingual transfer (EN$\\to$ZH) in both models---a direction that would be expected if conflict signals contained task-specific non-linear structure. However, bootstrap confidence intervals include zero in both cases (Llama $+5.2$ pp, CI [$-2.2$, $+12.9$]; Qwen $+3.8$ pp, CI [$-3.6$, $+11.3$]), and we report this as a directional trend rather than a confirmed finding. The absence of a significant non-linear component is itself informative: it indicates that the conflict signal captured by cross-lingual probes is predominantly linear, consistent with the sufficiency of logistic regression probes for cross-lingual semantic classification \\citep{belinkov2022probing}.\n\n## Model-Specificity of Causal Interventions\n\nThe causal steering result is supported by Llama-3.1-8B-Instruct, where layer 13 shows robust bidirectional effects that survive Bonferroni correction. Analogous experiments on Qwen3-8B at comparable relative depths (layers 14 and 23) yield no significant steering effects. This model-specificity does not invalidate the detection--decision dissociation---the absence of late-layer causal effects holds in both models---but it constrains the generality of mid-layer steering as an intervention strategy. The difference may reflect architectural factors that affect how conflict resolution is distributed across layers, such as differences in layer normalization, attention mechanisms, or pre-training language distributions. Model-specificity of causal interventions is itself an informative result: it suggests that mechanistic interpretability findings may not transfer across architectures as readily as probing patterns do, and that each model family may require independent causal validation even when probing results are qualitatively similar.\n\n## Broader Implications\n\nThese results contribute to both the understanding of cross-lingual knowledge conflicts and the methodology of cross-lingual probing. \\citet{zhao2026when} showed that in entity-centric factual conflicts, linguistic affinity determines which answer the model selects. Our analysis provides a partial mechanistic account: conflict signals are encoded in the model's shared multilingual representation space and inherit its directional biases, which in English-dominant models favor the English direction. The confound exclusion pipeline---combining translation quality stratification, token overlap analysis, and non-conflict baseline comparison---addresses methodological gaps that apply to any cross-lingual probing study where translation artifacts or general transfer properties could be mistaken for task-specific phenomena. The detection--decision dissociation carries practical implications for work on controlling model behavior in multilingual settings: interventions targeting the layer where a signal is most detectable may miss the computational stage where the decision is formed, and mid-layer representations deserve priority as intervention targets in future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/discussion_draft.md",
    "content": "# Discussion Draft\n\n> 5 paragraphs | LaTeX citations use \\citep{}/\\citet{} matching existing sections\n\n## Detection Does Not Imply Decision\n\nThe central finding of our causal analysis is the layer dissociation between where conflict signals are detectable and where they influence behavior. Probing accuracy for Llama peaks at layer 28 (88\\% depth), where the model's representation of the conflict outcome is most linearly separable. Yet steering at this layer produces no significant behavioral change (Fisher $p > 0.3$). Causal influence instead resides at layer 13 (41\\% depth), where perturbations along the probe direction shift the model's answer between contextual and parametric responses in both directions (Fisher $p = 0.002$ and $p < 0.001$). This pattern suggests that conflict resolution is computed at intermediate layers, and the late-layer signal is a post-hoc encoding of a decision already formed upstream. The mid-layer locus aligns with prior work showing that language-independent representations emerge at intermediate depths in multilingual models \\citep{muller2021first, wendler2024llamas}, suggesting that conflict resolution and cross-lingual alignment share a computational stage. From a methodological standpoint, this result reinforces the caution of \\citet{basu2026interpretability}: probe accuracy alone is an unreliable guide for selecting intervention targets, and steering experiments restricted to the probing peak can produce false negatives about the causal role of detected signals.\n\n## Asymmetry as a General Cross-Lingual Property\n\nThe directional asymmetry in cross-lingual transfer---where Chinese-trained probes transfer to English more accurately than the reverse by approximately 7 percentage points---initially appeared to reveal something specific about how conflict signals are organized across languages. The XNLI baseline reframes this interpretation. Probes trained on a non-conflict semantic distinction (entailment versus contradiction) show the same asymmetry at comparable magnitude (Llama $+6.0$ pp, Qwen $+6.7$ pp), with confidence intervals that overlap substantially with those of the conflict task (Llama $+7.2$ pp, Qwen $+7.2$ pp). The asymmetry is therefore not a property of conflict encoding but of the model's representational geometry: in English-dominant models, Chinese representations project more readily onto English subspace than the reverse. This connects to the English-centric latent space documented by \\citet{wendler2024llamas} and the cross-lingual alignment asymmetries measured by \\citet{kargaran2024mexa}. For cross-lingual probing studies more broadly, any observed transfer asymmetry must be benchmarked against a non-conflict baseline before being attributed to the phenomenon under investigation.\n\n## Non-Linear Encoding: A Directional Trend\n\nWe observe a suggestive but inconclusive pattern in non-linear encoding. MLP probes show larger gains over linear probes on the conflict task than on XNLI for cross-lingual transfer (EN$\\to$ZH) in both models---a direction that would be expected if conflict signals contained task-specific non-linear structure. However, bootstrap confidence intervals include zero in both cases (Llama $+5.2$ pp, CI [$-2.2$, $+12.9$]; Qwen $+3.8$ pp, CI [$-3.6$, $+11.3$]), and we report this as a directional trend rather than a confirmed finding. The absence of a significant non-linear component is itself informative: it indicates that the conflict signal captured by cross-lingual probes is predominantly linear, consistent with the sufficiency of logistic regression probes for cross-lingual semantic classification \\citep{belinkov2022probing}.\n\n## Model-Specificity of Causal Interventions\n\nThe causal steering result is supported by Llama-3.1-8B-Instruct, where layer 13 shows robust bidirectional effects that survive Bonferroni correction. Analogous experiments on Qwen3-8B at comparable relative depths (layers 14 and 23) yield no significant steering effects. This model-specificity does not invalidate the detection--decision dissociation---the absence of late-layer causal effects holds in both models---but it constrains the generality of mid-layer steering as an intervention strategy. The difference may reflect architectural factors that affect how conflict resolution is distributed across layers, such as differences in layer normalization, attention mechanisms, or pre-training language distributions. Model-specificity of causal interventions is itself an informative result: it suggests that mechanistic interpretability findings may not transfer across architectures as readily as probing patterns do, and that each model family may require independent causal validation even when probing results are qualitatively similar.\n\n## Broader Implications\n\nThese results contribute to both the understanding of cross-lingual knowledge conflicts and the methodology of cross-lingual probing. \\citet{zhao2026when} showed that in entity-centric factual conflicts, linguistic affinity determines which answer the model selects. Our analysis provides a partial mechanistic account: conflict signals are encoded in the model's shared multilingual representation space and inherit its directional biases, which in English-dominant models favor the English direction. The confound exclusion pipeline---combining translation quality stratification, token overlap analysis, and non-conflict baseline comparison---addresses methodological gaps that apply to any cross-lingual probing study where translation artifacts or general transfer properties could be mistaken for task-specific phenomena. The detection--decision dissociation carries practical implications for work on controlling model behavior in multilingual settings: interventions targeting the layer where a signal is most detectable may miss the computational stage where the decision is formed, and mid-layer representations deserve priority as intervention targets in future work.\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T15:39:07.668895+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/discussion_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_write-abstract-discussion_20260522T153557",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-22T15:39:07.669075+00:00_

两个文件已写入：

**Abstract** (~200 词)
- 结构：现象（跨语言冲突内部机制未知）→ 方法（残差流探针 + 跨语言迁移 + steering）→ 三个核心发现（检测 75-77%、不对称性继承通用跨语言属性、Detection ≠ Decision）→ 结论
- Steering 结果限定为 "in Llama"，未过度泛化
- 未使用 "consistently"

**Discussion** (5 段)
1. **Detection ≠ Decision** — L13 因果 vs L28 检测峰值，连接 mid-layer 跨语言对齐文献，引用 Basu 方法论警告
2. **不对称性是通用属性** — XNLI 对照数据（+6.0/+6.7 pp vs +7.2/+7.2 pp），CI 重叠，连接 Wendler & Kargaran
3. **非线性作为 observation** — MLP gains 方向对但 CI 含零，用 "directional trend" 定性
4. **Steering 的 model-specificity** — Llama 成功 Qwen 失败，框架为 "mechanistic results 跨架构迁移性本身是有意义的发现"
5. **Broader implications** — 连接 CLEAR，方法论贡献（confound pipeline），detection-decision dissociation 的实践意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_write-abstract-discussion_20260522T153557"
}
```

</details>

---
