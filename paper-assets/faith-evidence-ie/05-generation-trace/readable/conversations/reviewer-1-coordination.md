# Reviewer 1 coordination

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 320
- **Recorded user turns:** 8
- **Tool calls:** 152
- **Original source:** `logs/chats/feishu_group_oc_186574e43a82a9df336fe62a846a7b52_reviewer_1.jsonl`
- **Structured JSON:** [`aa13b180b6c957eca8ce.json`](../../sessions/aa/aa13b180b6c957eca8ce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-18T06:48:33.000402+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1（方法与实验严谨性）

### Venue 信息
- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references/appendix
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind，禁止 self-identification
- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读

### 论文路径
`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）

### 你的审查侧重：方法与实验严谨性

请重点审查以下方面：

1. **方法设计**
   - Task formulation (§3.1) 是否合理？Evidence-grounded DocRE 的形式化定义是否严谨？
   - CED scoring function (§3.4) 设计是否合理？NLI-based 对比打分的假设是否成立？
   - EDCR metric (§3.5) 的定义和解释是否存在漏洞？

2. **实验设计与统计可靠性**
   - "85+ configurations" 的声称是否可验证？
   - 主要 claim 的统计支撑是否充分？（seed 数量、variance 报告、显著性检验）
   - Baseline 选择是否公平？是否遗漏关键 baseline？
   - Evaluation protocol 是否标准？只使用 dev set 是否构成重大局限？

3. **Claims 与证据对齐**
   - 三个核心 finding（decoupling spectrum、scale-dependent tax、RSFT effectiveness）是否都有充分的实验支撑？
   - Claim 的强度是否与证据匹配？是否存在过度声称（overclaim）？
   - 因果性 vs 相关性：论文的因果推断是否合理？

4. **消融与分析完整性**
   - RSFT ablation（CED vs flat-NLI, k=1 vs k=3）是否充分？
   - GRPO/DPO 的配置空间是否充分探索？（例如不同 KL 系数、不同 LoRA rank）
   - Scale analysis 只有 3-4 个数据点，non-monotonic pattern 的 claim 是否 over-interpreted？

5. **可复现性**
   - Hyperparameters 是否完整报告？
   - 数据处理 pipeline 是否可复现？

请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-18T06:48:42.256809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-18T06:48:42.458251+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T06:48:42.458638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T06:48:42.509179+00:00_

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
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/analysis}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T06:48:45.171672+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T06:48:45.624080+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T06:48:45.825438+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T06:48:45.926286+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T06:48:49.396110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T06:48:49.900218+00:00_

1	\begin{abstract}
2	
3	Large Language Model (LLM) based Document-level Relation Extraction (DocRE) methods now match or exceed encoder baselines in extraction accuracy, yet they produce bare relation triplets without identifying the sentences that support each prediction.
4	In deployment contexts such as clinical knowledge bases and legal due-diligence systems, users cannot verify predictions without manually locating textual evidence across multi-page documents.
5	Encoder-based evidence methods (SAIS, DREEAM) can produce supporting sentences but trail LLM approaches in accuracy. The community therefore faces a gap between extractive precision and output verifiability.
6	
7	We formalize evidence-grounded DocRE as a structured generation task and conduct a systematic comparison of three post-training optimization paradigms: Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT).
8	Our study spans 85+ experimental configurations across four model scales (1.7B to 8B parameters), two model families, and two datasets.
9	We introduce the Evidence-Decoupling Ratio (EDCR) diagnostic and a Contrastive Evidence Discrimination (CED) scoring function for sample selection.
10	
11	Three findings emerge.
12	First, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.
13	Second, the cost of evidence production is scale-dependent and non-monotonic: at 1.7B parameters evidence provides a +8pp Ign-F1 benefit, at 4B it imposes a $-$7.5pp penalty, and at 8B the cost approaches zero.
14	Third, RSFT with CED scoring is the only effective route: it achieves +4.92pp Ign-F1 over supervised fine-tuning at 4B scale (four-seed mean), and our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT performance (50.51).
15	
16	\end{abstract}
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T06:48:49.900837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T06:48:50.354571+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition for end-to-end extraction, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy.
6	Yet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \emph{which sentences} in the document support each prediction.
7	In deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.
8	
9	The absence of verifiable evidence creates a practical bottleneck.
10	Relation extraction outputs are consumed downstream by knowledge graph construction and human decision workflows.
11	When a system predicts that a drug interacts with a gene, or that a contract clause implies a liability, practitioners must trace each prediction back to source text before acting on it.
12	Without machine-generated evidence, this verification requires exhaustive manual review of the input document for every predicted relation.
13	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
14	Both improve extraction quality \emph{and} produce evidence annotations.
15	However, encoder methods now trail LLM-bas
…[truncated 4907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T06:48:50.355090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T06:48:50.857599+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without evidence.
15	The critical distinction lies in computational nature: in SAIS and DREEAM, evidence
…[truncated 4221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T06:48:50.858115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T06:48:51.310536+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.
8	
9	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
10	
11	
12	\subsection{Supervised Fine-Tuning Baseline}
13	\label{sec:sft}
14	
15	We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output 
…[truncated 7862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T06:48:51.311031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T06:48:51.763387+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	We report five metrics. \textbf{Ign-F1} is the primary DocRED metric that ignores triples appearing in the training set, matching the official leaderboard protocol. \textbf{Rel-F1} measures relation extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence sentence F1 conditioned on correctly predicted triples, reflecting evidence quality independent of extraction errors. \textbf{Evi-F1 (joint)} includes false-positive and false-negative triples in the denominator following the DREEAM protocol~\citep{ma2023dreeam}, enabling cross-method evidence comparison. \textbf{EDCR} (Evidence-Decoupling Rati
…[truncated 10016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T06:48:51.814125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T06:48:52.216307+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{EDCR as a diagnostic.}
5	EDCR (\S\ref{sec:edcr}) correlates strongly with extraction quality at the method level: Spearman $\rho = -0.965$ between EDCR and Rel-F1 (Table~\ref{tab:spectrum}), with GRPO QLoRA at 0.9876, SFT at 0.6982, and RSFT at 0.6503. At the per-relation level, EDCR correlates with Rel-F1 ($\rho = -0.793$) but is independent of Evi-F1 ($\rho = -0.064$), confirming extraction-evidence decoupling across relation types (Appendix~\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection prevents trading extraction for evidence quality (Appendix~\ref{sec:rsft_theory}). We provide qualitative examples of these phenomena in Appendix~\ref{sec:qualitative}.
6	
7	\paragraph{CED granularity.}
8	CED operates effectively at the response level for both RSFT selection and inference-time reranking, but fails at sentence-level granularity: filtering individual evidence sentences by NLI score reduces Evi-F1 by 7.7pp (Recall $-$20pp), as it disrupts co-reference chains across evidence sentences. This suggests that evidence quality is a holistic response property rather than a per-sentence attribute.
9	
10	\paragraph{Ablation.}
11	CED and flat-NLI produce comparable performance (Rel-F1 0.4563 vs.\ 0.4561); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\times$ fewer examples (Appendix~\ref{sec:ablation_full}).
12	
13	\paragraph{Practical implications.}
14	Our findings suggest three guidelines for practitioners seeking evidence-grounded IE: (1) avoid online RL for multi-objective generation tasks where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity; (3) consider CED reranking at inference for deployment scenarios requiring both high extraction accuracy and evidence quality.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T06:48:52.216982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T06:48:53.171686+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task for LLMs and compare three post-training paradigms across 85+ configurations. RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic, DPO gradual, RSFT none; EDCR $\rho = -0.965$), and the cost of joint evidence production follows a non-monotonic pattern across scales (+8pp at 1.7B, $-$7.5pp at 4B, near zero at 8B). RSFT with CED scoring yields +4.92pp Ign-F1 at 4B (four-seed mean); our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT (50.51) at a fraction of the cost.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T06:48:53.172060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T06:48:53.626052+00:00_

1	\section{Limitations}
2	
3	All results use the DocRED development set; test set submission is pending. Exact-match F1 penalizes surface-form-different entity mentions~\citep{wan2024genres}, likely underestimating absolute extraction capability, though relative comparisons remain valid.
4	
5	We evaluate one algorithm per RL family (GRPO, DPO); other algorithms may yield different results. CED scoring depends on an external NLI model, and the RSFT ablation uses limited seeds (four for CED, two for flat-NLI). The evidence tax pattern observed up to 8B may not extrapolate to larger scales. At 1.7B scale, 44.4\% of outputs exhibit repetitive patterns (vs.\ negligible at 4B+); small models may require decoding-time interventions (e.g., repetition penalty) for reliable deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T06:48:53.676979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T06:48:53.828670+00:00_

1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to attention projections. SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	Base model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\
16	LoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\
17	LoRA $\alpha$ & 128 & 128 & 128 & 128 & 128 \\
18	Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
19	Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
20	Epochs & 3 & 3 & -- & -- & 1, 3\textsuperscript{$\star$} \\
21	Max steps & -- & -- & 100 & 100 & -- \\
22	Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
24	Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
25	Group size $G$ & -- & -- & 4 & 8 & -- \\
26	KL coefficient & -- & -- & 0.01 & 0.01 & -- \\
27	$\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\
28	Candidates $N$ & -- & 8 & -- & -- & 8 \\
29	Top-$k$ selection & -- & 1 & -- & -- & -- \\
30	Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
31	Scoring function & -- & CED & CED & CED & CED \\
32	\bottomrule
33	\end{tabular}
34	\vspace{1mm}
35	{\raggedright\footnotesize \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction tra
…[truncated 14481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T06:48:53.829214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T06:48:53.881666+00:00_

1	@inproceedings{autore2024,
2	  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},
3	  author    = {{Anonymous}},
4	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2403.14888}
7	}
8	
9	@inproceedings{chen2025docksrag,
10	  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},
11	  author    = {Xu and others},
12	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
13	  year      = {2025},
14	  url       = {https://proceedings.mlr.press/v267/xu25am.html}
15	}
16	
17	@article{dai2025r1re,
18	  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},
19	  author  = {Dai, Runpeng and Zheng, Tong and others},
20	  journal = {arXiv preprint arXiv:2507.04642},
21	  year    = {2025},
22	  url     = {https://arxiv.org/abs/2507.04642}
23	}
24	
25	@inproceedings{gao2023scaling,
26	  title     = {Scaling Laws for Reward Model Overoptimization},
27	  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},
28	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
29	  year      = {2023},
30	  url       = {https://arxiv.org/abs/2210.10760}
31	}
32	
33	@inproceedings{hu2022lora,
34	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
35	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
36	  booktitle = {International Conference on Learning Representations},
37	  year      = {2022},
38	  url       = {https://arxiv.org/abs/2106.09685}
39	}
40	
41	@article{jin2025rl_panacea,
42	  title   = {{RL} Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for {LLMs}},
43	  author  = {Jin, Hangzhan and others},
44	
…[truncated 10416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T06:48:58.326766+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
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

_source line 31 · 2026-05-18T06:48:58.377520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T06:49:02.199132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T06:49:02.500938+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form dimensions soundness novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form dimensions soundness novelty"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T06:49:08.630857+00:00_

Web search results for query: "EMNLP 2026 ARR review form dimensions soundness novelty"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum","url":"https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/authors.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/authors.md"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"}]

Based on the search results, here's what I found about the ARR review form dimensions for EMNLP 2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

Regarding the specific dimensions:

**Soundness**: Reviewers evaluate whether the paper is sufficiently sound and thorough, whether it clearly states scientific claims and provides adequate support for them, and consider the depth and/or breadth of research questions investigated, te
…[truncated 817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6129
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T06:49:09.937154+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the web search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scores and Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justi
…[truncated 1451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7738
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T06:49:12.900605+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T06:49:12.951426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T06:49:16.775666+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), and the description of each score level. Include soundness, excitement, overall assessment, reproducibility, and any other scored dimensions. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), and the description of each score level. Include soundness, excitement, overall assessment, reproducibility, and any other scored dimensions. Be exhaustive."
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T06:49:18.033574+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to assess soundness, excitement, novelty, significance, and any specific instructions about scoring. Include all rubric details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to assess soundness, excitement, novelty, significance, and any specific instructions about scoring. Include all rubric details."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T06:49:25.167898+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Dimensions

ARR reviewers assess papers using three primary scores:

1. **Soundness**: Technical correctness and methodological rigor. Per guidelines, "The _soundness_ scores must be justified by the text of the review." Low soundness scores require explicit justification in the review text.

2. **Excitement**: Personal interest and engagement with the work. This reflects subjective preferences independent of technical quality and "do not necessarily come with explicit reasons."

3. **Overall Assessment**: Composite recommendation reflecting soundness, excitement, novelty, and potential impact. Papers must be "sufficiently sound and reproducible" for acceptance consideration.

## Key Evaluation Principles

**Adjust Expectations**: Reviewers should read papers twice—first for research question and contribution scope, then for technical depth. This prevents bias toward prototype papers in one's subfield.

**Be Specific**: Criticism must cite concrete issues. Generic statements like "missing relevant references" should instead name specific works.

**Avoid Common Biases**: Guidelines flag 17 heuristics (H1-H17) that lead to problematic rejections, including dismissing "unsurprising" results, rejecting negative findings, or demanding unnecessarily complex solutions.

**Check NLP-Specific Issues**: Reviewers should identify methodological problems (M1-M5), artifact sourcing concerns (T1-T2), experimental issues (R1-R5), and general problems (G1-G5).

## Special Requirements

- Justify all scores with review text
- Maintain professional, neutral tone
- Address author responses substantively during discussion
- For resubmissions, focus on whether previous concerns were adequately addressed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7134
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T06:49:27.105463+00:00_

# ARR Review Form Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: Could be considered for an outstanding paper award."
- **4.5**: "Borderline Award"
- **4**: "Conference: Could be accepted to an *ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1.5**: "Resubmit after next cycle: Needs substantial revisions that cannot be completed qui
…[truncated 1631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10329
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-18T06:50:39.813101+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
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

_source line 43 · 2026-05-18T06:50:39.864118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T06:50:42.929263+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "projects/faith-evidence-ie/docs/paper",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "projects/faith-evidence-ie/docs/paper",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-18T06:50:42.980015+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/projects/faith-evidence-ie/docs/paper\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T06:50:45.596369+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "docs/paper",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "docs/paper",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T06:51:16.382847+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 40, \"total_citations\": 54, \"unique_cited_keys\": 33, \"orphan_bib\": 7, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 22, \"online_not_found\": 13, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"APA:83\", \"Aho:72\", \"Ando2005\", \"Chandra:81\", \"Gusfield:97\", \"andrew2007scalable\", \"rasooli-tetrault-2015\"], \"missing_bib\": [], \"orphan_count\": 7, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"autore2024\", \"type\": \"inproceedings\", \"title\": \"AutoRE: Document-Level Relation Extraction with Large Language Models\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"chen2025docksrag\", \"type\": \"inproceedings\", \"title\": \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\", \"authors\": \"Xu and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning\"}, {\"key\": \"dai2025r1re\", \"type\": \"article\", \"title\": \"R1-RE: Cross-Domain Relation Extraction with RLVR\", \"authors\": \"Dai, Runpeng and Zheng, Tong and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.04642\"}, {\"key\": \"gao2023scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"authors\": \"Gao, Leo and Schulman, John and Hilton, Jacob\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"jin2025rl_panacea\", 
…[truncated 30466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 30786
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T06:51:25.025109+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T06:51:25.075878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-18T06:53:43.133902+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见 — 方法与实验严谨性\n\n**论文**: \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference Long Paper (ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 研究问题有价值、实验覆盖面广，但核心 claim 的统计支撑不足，多个关键实验存在混淆变量，且全部结果仅在 dev set 上报告，距离 Main Conference 的标准有明显差距。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim（decoupling spectrum、non-monotonic scaling）的实验设计存在混淆变量，统计检验缺失，EDCR 方法级相关性仅基于 6 个数据点 |\n| Excitement | 3.5/5 | 研究问题（LLM 时代 DocRE 的证据可验证性 vs 抽取精度权衡）切中实际需求，decoupling spectrum 概念有启发性 |\n| Overall Assessment | 3.0/5 | 适合 Findings；需补充统计检验、解混淆 GRPO 实验、增加 test set 结果方可达 Conference 水平 |\n| Reproducibility | 3/5 | 超参数基本报告完整，但 prompt template、entity mention 处理细节缺失；NLI 模型指定但 CED 聚合公式的细节不完整 |\n| Reviewer Confidence | 4/5 | 熟悉 DocRE、RL alignment、NLI-based evaluation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果推断\n\n- 具体位置：§4.3 Table 2；§3.3 GRPO paragraph\n- 问题：GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了**两个变量**：量化精度和 group size。论文将 catastrophic collapse 归因于\"4-bit quantization constrains the effective parameter space\"（§4.3 第二段），但无法排除 G=4 vs G=8 的影响。需要至少两个额外实验点：GRPO QLoRA G=8 和 GRPO bf16 G=4，才能解耦 quantization 和 group size 的效果。\n- 为什么影响接收：Decoupling spectrum 是论文的第一核心贡献（Contribution 2），如果 GRPO catastrophic collapse 的归因不成立，整个 spectrum 叙事的因果链就断了。论文在 Introduction 第 29-30 行明确声称\"QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause\"，这是一个因果性 claim，但实验设计无法支撑。\n- 建议修改方向：补充 GRPO bf16 G=4 和 GRPO QLoRA G=8 实验；或将因果性表述降级为观察性表述（\"we observe that the combination of QLoRA and smaller group size correlates with...\"）。\n\n**N2** [critical] 全部结果仅在 dev set 上报告，test set 结果缺失\n\n- 具体位置：§4.1 Metrics 段最后一句 \"All primary results use the development set; test set submission is pending\"；Limitations §7 第一句\n- 问题：对于一篇声称\"85+ experimental configurations\"的系统性实证研究，没有任何 test set 结果是严重缺陷。DocRED test set 有公开 leaderboard（CodaLab），提交并获取结果是标准做法。Dev set 可能导致超参数间接过拟合，尤其在多轮实验迭代中。\n- 为什么影响接收：ARR soundness 标准要求\"sufficient support for all of its claims\"。论文在 Abstract 和 Introduction 中的数字（+4.92pp, 50.50 vs 50.51 等）全部基于 dev set，不能视为最终性能指标。审稿人无法判断这些结论是否在 test set 上成立。\n- 建议修改方向：至少对 main results（Table 1 的 SFT / RSFT CED）和 scaling results（Table 3）提交 DocRED test set 评估。如果 test set 结果与 dev set 有较大偏差，需要更新叙事。\n\n**N3** [critical] SFT baseline 缺少多 seed 方差，+4.92pp 改进缺乏统计显著性检验\n\n- 具体位置：Table 1；§4.2 第一段\n- 问题：RSFT CED 报告了 4-seed 均值 44.66±0.49，但 SFT baseline 仅有单 seed 结果 (39.74)。没有 SFT 的方差估计，无法判断 +4.92pp 的改进是否统计显著。假设 SFT 方差与 RSFT 类似（~0.49），+4.92pp 很可能显著；但 SFT 可能有更大方差（因为没有 CED 筛选的稳定化效果）。论文全文没有进行任何统计显著性检验（t-test、bootstrap、paired permutation test）。\n- 为什么影响接收：这是论文的核心数字（出现在 Abstract、Introduction Contribution 4、Conclusion），如果不具备统计意义，所有下游结论都不可靠。\n- 建议修改方向：(1) 对 SFT baseline 补充至少 3 个 seed 的结果；(2) 对所有主要对比进行 paired bootstrap 或 t-test；(3) 报告 p-value 和 confidence interval。\n\n**N4** [critical] \"Non-monotonic\" scaling pattern 仅基于 3 个数据点，over-interpreted\n\n- 具体位置：§4.4 Table 3；Introduction 第 31-33 行；Abstract 第 13 行\n- 问题：Scale-dependent evidence tax 的 non-monotonic claim 基于 Qwen3 的 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28）。3 个点无法区分 non-monotonic pattern 与噪声或单点异常。特别是 1.7B 的 +8.04pp \"benefit\" 有严重的替代解释：论文自己在 Limitations 中承认\"44.4% of outputs exhibit repetitive patterns\"（§7 第 5 句），说明 1.7B 模型的 no-evidence 输出质量可能因 repetition 而被人为压低，evidence generation 的\"benefit\"可能仅仅是因为它迫使模型产生更长、更结构化的输出从而减少重复。此外，Abstract 中声称的\"+8pp Ign-F1 benefit\"在正文 §4.4 中被修正为\"On a fair evaluation subset... this benefit is +6.2 points\"，但这个 fair subset 的细节几乎没有交代。\n- 为什么影响接收：Scale-dependent evidence tax 是 Contribution 3，也是论文标题中\"Scaling\"一词的核心支撑。如果 non-monotonic claim 不成立，论文的独特贡献大幅缩水。\n- 建议修改方向：(1) 增加至少 1 个中间规模点（如 Qwen3-2.5B 或其他 ~3B 模型）验证 non-monotonicity；(2) 详细报告 1.7B \"fair evaluation subset\" 的构建方法和完整结果；(3) 对 1.7B 的 repetition 问题做 controlled analysis（如加 repetition penalty 后重新测 no-evidence baseline）；(4) 或将 claim 降级为\"observed pattern across three scales\"而非\"non-monotonic\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] EDCR 方法级相关性 (ρ=-0.965) 仅基于 6 个数据点，统计意义存疑\n\n- 具体位置：§3.5 第 64 行；§6 Analysis 第一段；Table 2\n- 问题：Table 2 共 6 行（GRPO QLoRA, GRPO bf16, DPO 1ep, DPO 3ep, SFT, RSFT），Spearman ρ=-0.965 在 n=6 时 critical value at α=0.05 约为 0.886，因此虽然统计显著但 power 极低，且结果对单个点高度敏感。GRPO QLoRA 是一个极端 outlier（EDCR=0.9876, Rel-F1=0.0138），移除该点后相关性可能大幅下降。此外，DPO 3-epoch 使用了\"pre-D076 evaluation protocol\"（Table 2 footnote），与其他行不在同一评估标准下，进一步削弱相关性分析的可比性。\n- 建议：(1) 报告去掉 GRPO QLoRA outlier 后的相关性；(2) 要么统一评估 protocol，要么将 DPO 3ep 从相关性计算中移除并标注清楚；(3) 考虑增加更多实验配置（如不同 KL coefficient 的 GRPO、不同 β 的 DPO）来增强样本量。\n\n**W2** [warning] \"1.7B RSFT matches 8B SFT\" claim 基于单 seed，差异仅 0.01pp\n\n- 具体位置：§4.4 Table 3 最后一句；Introduction Contribution 4；Abstract 第 14 行\n- 问题：1.7B RSFT (50.50) vs 8B SFT (50.51) 差异 0.01pp，两者均为单 seed 结果（Table 8 caption：\"single seed for other scales\"）。在没有方差估计的情况下，声称\"matches\"在统计上没有意义。任何合理的 seed variance 都远超 0.01pp。这个 claim 在 Abstract 和 Introduction 中被重复强调，但证据极弱。\n- 建议：补充 1.7B RSFT 和 8B SFT 各 3-4 seeds 的结果，报告 confidence interval；或将 claim 改为\"approaches\"而非\"matches\"。\n\n**W3** [warning] CED 与 flat-NLI 差异仅 0.02pp，contrastive component 的贡献未被证明\n\n- 具体位置：§3.4 最后一段；§6 Ablation 段；Appendix Table 6\n- 问题：CED (Rel-F1 0.4563) vs flat-NLI (0.4561)，差异 0.02pp，且 flat-NLI 仅有 2 seeds（Appendix §8）。论文承认\"CED and flat-NLI produce comparable RSFT outcomes\"但仍将 CED 作为默认选择，理由是\"interpretable per-triple discrimination scores\"。然而论文没有任何实验展示这种 interpretability 带来的实际价值。CED 的 contrastive component 增加了方法复杂度但没有带来可测量的改进，这削弱了 CED 作为方法贡献的意义。\n- 建议：(1) flat-NLI 补充到 4 seeds 以做公平对比；(2) 如果差异仍不显著，诚实报告 contrastive component 可能不是必要的；(3) 或提供 case study 展示 CED 的 per-triple discrimination 在实际 error analysis 中如何优于 flat-NLI。\n\n**W4** [warning] Baseline 对比不完整，缺少关键参照系\n\n- 具体位置：§4.2 Table 1；§4.6 最后一段\n- 问题：(1) 缺少与 encoder-based evidence methods (SAIS, DREEAM, EIDER) 在相同 evaluation protocol 下的直接对比。论文在 §4.6 提到 DREEAM 的 joint Evi-F1 为 54.01%，而本文最佳为 ~36%，但这个对比被放在 Appendix 中一笔带过。(2) 缺少与其他 LLM-based DocRE 方法（AutoRE、LMRC 等，均在 Related Work 中讨论）的抽取性能对比。(3) Post-hoc evidence 仅测试了 BM25，没有测试更强的 learned retriever。\n- 建议：在 main results 中增加 SAIS/DREEAM 的数字作为参照（即使不同 protocol，也应在 Table 中注明并讨论差距来源）；增加至少一个 LLM-based DocRE baseline 的抽取性能对比。\n\n**W5** [warning] RSFT ablation 缺少 random selection baseline\n\n- 具体位置：§6 Ablation 段；Appendix §8\n- 问题：RSFT 消融比较了 CED vs flat-NLI 和 k=1 vs k=3，但缺少一个关键 baseline：random selection（从 8 个 candidate 中随机选 1 个作为训练数据）。没有这个 baseline，无法确定 RSFT 的改进是来自\"quality-based selection\"还是简单的\"data augmentation + selection\"效应（即使随机选择也可能因为 sampling diversity 带来改进）。\n- 建议：增加 random-k=1 baseline；如果 random 也有不错的改进，那 CED scoring 的贡献需要重新评估。\n\n**W6** [warning] GRPO/DPO 超参数探索不足\n\n- 具体位置：§3.3；Appendix Table 5\n- 问题：GRPO 仅测试 KL=0.01，DPO 仅测试 β=0.1。在 RL/preference optimization 文献中，KL 系数和 β 对 reward hacking 和 performance tradeoff 有显著影响（Gao et al., 2023; Moskovitz et al., 2024 均被论文引用）。如果 GRPO 在更大 KL penalty 下不 collapse，或 DPO 在更小 β 下不 degrade，decoupling spectrum 的结论需要修改。\n- 建议：至少对 GRPO 测试 KL ∈ {0.001, 0.01, 0.1} 和 DPO 测试 β ∈ {0.01, 0.1, 0.5}，或承认当前结论受限于特定超参数设置。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 格式不一致：Rel-F1 使用小数 (0.4049)，Evi-F1 使用百分比 (79.86)，EDCR 使用小数 (0.6982)。全表应统一。\n- Appendix 中有 7 个 orphan bib entries（Aho:72, APA:83, Ando2005, Chandra:81, Gusfield:97, andrew2007scalable, rasooli-tetrault-2015），疑似 ACL 模板遗留，应清理。\n- 引用 `autore2024` 的作者标注为 \"Anonymous\"，但该论文已正式发表（ACL 2024 System Demos），第一作者为 Xue 等人，应更新。类似地，`zhao2025egrpo`（E-GRPO）也标注 Anonymous。\n- 引用 `wang2025relprior`、`zhang2025glidre`、`hu2025reinforcepp`、`wang2025rear` 的第一作者与 OpenAlex 记录不匹配，需核实。\n- Appendix §14 Figure 4 caption 说\"93 relation types\"，但正文 §14 第一句说\"76 relation types with ≥5 evaluation samples\"，而 §4.1 说 DocRED 有 96 relation types。三个数字互相矛盾。\n- §4.3 DPO 3-epoch 的脚注提到\"pre-D076 evaluation protocol\"，未解释 D076 是什么。内部编号不应出现在投稿论文中。\n- §4.4 提到\"fair evaluation subset\"但未给出构建方法、样本量和完整结果。\n- RSFT 的 training samples 为 2,718（Table 5），但 §3.3 说\"9,042 training examples (37.3% acceptance rate)\"，数字不一致（9,042 × 37.3% ≠ 2,718；24,216 → 9,042 是 ~37.3%，但 Table 5 报告 2,718 training samples）。需要解释 9,042 candidates 如何变成 2,718 training samples。\n\n---\n\n## 主要优势\n\n1. **研究问题重要且定位精准**：LLM-based DocRE 缺乏 evidence grounding 是一个真实的实用性瓶颈，论文清晰地识别了 encoder-based evidence methods（SAIS/DREEAM）与 LLM-based extraction accuracy 之间的 gap（§1 第 16 行），问题动机有说服力。\n\n2. **实验覆盖面广**：跨 4 个模型规模、2 个模型家族、2 个数据集、3 种优化范式的系统性比较在 DocRE 文献中确实罕见。即使个别实验的统计严谨性不足，这种横向覆盖本身也有参考价值。\n\n3. **Decoupling spectrum 概念有启发性**：将 GRPO/DPO/RSFT 按 decoupling 严重程度排序的视角（Table 2）直观且有助于理解多目标生成任务中不同优化策略的行为差异。如果混淆变量问题得到修复，这将是一个有洞察力的贡献。\n\n4. **RSFT 效果稳定**：4-seed 结果方差较低（±0.49），跨数据集（DocRED +4.92pp, Re-DocRED +4.86pp）和跨模型家族（LLaMA +1.74pp）的改进模式一致（§4.6），说明 rejection sampling approach 的鲁棒性。\n\n5. **写作质量较好**：论文叙事结构清晰（问题→形式化→方法→实验→分析），Related Work 做了有效的 positioning（§2 区分了 encoder-based evidence 与 LLM-based generation 的结构性差异），不是简单的论文罗列。\n\n---\n\n## 缺失引用\n\n- **KGC/知识图谱补全视角**：论文讨论了 DocRE 但未引用知识图谱构建相关工作，考虑到 Introduction 明确提到\"knowledge graph construction\"作为下游应用。\n- **Multi-task learning / auxiliary loss 文献**：Evidence generation 作为辅助任务与 extraction 竞争 capacity 的分析框架，应引用 multi-task learning 的经典分析（如 Ruder 2017, Fifty et al. 2021 \"Efficiently Identifying Task Groupings for Multi-Task Learning\"）。\n- **Chain-of-thought / rationale generation**：Evidence generation 在概念上类似 CoT rationale generation，相关的 faithful reasoning 文献（如 Lanham et al. 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\"）可以丰富讨论。\n\n---\n\n## 总结\n\n论文提出了一个有价值的研究问题，实验覆盖面令人印象深刻。但在方法论严谨性上有明显短板：核心实验存在未解耦的混淆变量（N1），全部结果缺少 test set 验证（N2），主要 claim 缺乏统计检验（N3），scaling claim 的数据点不足（N4）。这些问题的共同效果是：论文的 claim 强度系统性地超过了实验证据的支撑力度。如果能补充 test set 结果、解耦 GRPO 实验、增加统计检验，本文有潜力达到 Conference 水平。当前状态建议 Findings。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见 — 方法与实验严谨性\n\n**论文**: \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference Long Paper (ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 研究问题有价值、实验覆盖面广，但核心 claim 的统计支撑不足，多个关键实验存在混淆变量，且全部结果仅在 dev set 上报告，距离 Main Conference 的标准有明显差距。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim（decoupling spectrum、non-monotonic scaling）的实验设计存在混淆变量，统计检验缺失，EDCR 方法级相关性仅基于 6 个数据点 |\n| Excitement | 3.5/5 | 研究问题（LLM 时代 DocRE 的证据可验证性 vs 抽取精度权衡）切中实际需求，decoupling spectrum 概念有启发性 |\n| Overall Assessment | 3.0/5 | 适合 Findings；需补充统计检验、解混淆 GRPO 实验、增加 test set 结果方可达 Conference 水平 |\n| Reproducibility | 3/5 | 超参数基本报告完整，但 prompt template、entity mention 处理细节缺失；NLI 模型指定但 CED 聚合公式的细节不完整 |\n| Reviewer Confidence | 4/5 | 熟悉 DocRE、RL alignment、NLI-based evaluation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果推断\n\n- 具体位置：§4.3 Table 2；§3.3 GRPO paragraph\n- 问题：GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了**两个变量**：量化精度和 group size。论文将 catastrophic collapse 归因于\"4-bit quantization constrains the effective parameter space\"（§4.3 第二段），但无法排除 G=4 vs G=8 的影响。需要至少两个额外实验点：GRPO QLoRA G=8 和 GRPO bf16 G=4，才能解耦 quantization 和 group size 的效果。\n- 为什么影响接收：Decoupling spectrum 是论文的第一核心贡献（Contribution 2），如果 GRPO catastrophic collapse 的归因不成立，整个 spectrum 叙事的因果链就断了。论文在 Introduction 第 29-30 行明确声称\"QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause\"，这是一个因果性 claim，但实验设计无法支撑。\n- 建议修改方向：补充 GRPO bf16 G=4 和 GRPO QLoRA G=8 实验；或将因果性表述降级为观察性表述（\"we observe that the combination of QLoRA and smaller group size correlates with...\"）。\n\n**N2** [critical] 全部结果仅在 dev set 上报告，test set 结果缺失\n\n- 具体位置：§4.1 Metrics 段最后一句 \"All primary results use the development set; test set submission is pending\"；Limitations §7 第一句\n- 问题：对于一篇声称\"85+ experimental configurations\"的系统性实证研究，没有任何 test set 结果是严重缺陷。DocRED test set 有公开 leaderboard（CodaLab），提交并获取结果是标准做法。Dev set 可能导致超参数间接过拟合，尤其在多轮实验迭代中。\n- 为什么影响接收：ARR soundness 标准要求\"sufficient support for all of its claims\"。论文在 Abstract 和 Introduction 中的数字（+4.92pp, 50.50 vs 50.51 等）全部基于 dev set，不能视为最终性能指标。审稿人无法判断这些结论是否在 test set 上成立。\n- 建议修改方向：至少对 main results（Table 1 的 SFT / RSFT CED）和 scaling results（Table 3）提交 DocRED test set 评估。如果 test set 结果与 dev set 有较大偏差，需要更新叙事。\n\n**N3** [critical] SFT baseline 缺少多 seed 方差，+4.92pp 改进缺乏统计显著性检验\n\n- 具体位置：Table 1；§4.2 第一段\n- 问题：RSFT CED 报告了 4-seed 均值 44.66±0.49，但 SFT baseline 仅有单 seed 结果 (39.74)。没有 SFT 的方差估计，无法判断 +4.92pp 的改进是否统计显著。假设 SFT 方差与 RSFT 类似（~0.49），+4.92pp 很可能显著；但 SFT 可能有更大方差（因为没有 CED 筛选的稳定化效果）。论文全文没有进行任何统计显著性检验（t-test、bootstrap、paired permutation test）。\n- 为什么影响接收：这是论文的核心数字（出现在 Abstract、Introduction Contribution 4、Conclusion），如果不具备统计意义，所有下游结论都不可靠。\n- 建议修改方向：(1) 对 SFT baseline 补充至少 3 个 seed 的结果；(2) 对所有主要对比进行 paired bootstrap 或 t-test；(3) 报告 p-value 和 confidence interval。\n\n**N4** [critical] \"Non-monotonic\" scaling pattern 仅基于 3 个数据点，over-interpreted\n\n- 具体位置：§4.4 Table 3；Introduction 第 31-33 行；Abstract 第 13 行\n- 问题：Scale-dependent evidence tax 的 non-monotonic claim 基于 Qwen3 的 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28）。3 个点无法区分 non-monotonic pattern 与噪声或单点异常。特别是 1.7B 的 +8.04pp \"benefit\" 有严重的替代解释：论文自己在 Limitations 中承认\"44.4% of outputs exhibit repetitive patterns\"（§7 第 5 句），说明 1.7B 模型的 no-evidence 输出质量可能因 repetition 而被人为压低，evidence generation 的\"benefit\"可能仅仅是因为它迫使模型产生更长、更结构化的输出从而减少重复。此外，Abstract 中声称的\"+8pp Ign-F1 benefit\"在正文 §4.4 中被修正为\"On a fair evaluation subset... this benefit is +6.2 points\"，但这个 fair subset 的细节几乎没有交代。\n- 为什么影响接收：Scale-dependent evidence tax 是 Contribution 3，也是论文标题中\"Scaling\"一词的核心支撑。如果 non-monotonic claim 不成立，论文的独特贡献大幅缩水。\n- 建议修改方向：(1) 增加至少 1 个中间规模点（如 Qwen3-2.5B 或其他 ~3B 模型）验证 non-monotonicity；(2) 详细报告 1.7B \"fair evaluation subset\" 的构建方法和完整结果；(3) 对 1.7B 的 repetition 问题做 controlled analysis（如加 repetition penalty 后重新测 no-evidence baseline）；(4) 或将 claim 降级为\"observed pattern across three scales\"而非\"non-monotonic\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] EDCR 方法级相关性 (ρ=-0.965) 仅基于 6 个数据点，统计意义存疑\n\n- 具体位置：§3.5 第 64 行；§6 Analysis 第一段；Table 2\n- 问题：Table 2 共 6 行（GRPO QLoRA, GRPO bf16, DPO 1ep, DPO 3ep, SFT, RSFT），Spearman ρ=-0.965 在 n=6 时 critical value at α=0.05 约为 0.886，因此虽然统计显著但 power 极低，且结果对单个点高度敏感。GRPO QLoRA 是一个极端 outlier（EDCR=0.9876, Rel-F1=0.0138），移除该点后相关性可能大幅下降。此外，DPO 3-epoch 使用了\"pre-D076 evaluation protocol\"（Table 2 footnote），与其他行不在同一评估标准下，进一步削弱相关性分析的可比性。\n- 建议：(1) 报告去掉 GRPO QLoRA outlier 后的相关性；(2) 要么统一评估 protocol，要么将 DPO 3ep 从相关性计算中移除并标注清楚；(3) 考虑增加更多实验配置（如不同 KL coefficient 的 GRPO、不同 β 的 DPO）来增强样本量。\n\n**W2** [warning] \"1.7B RSFT matches 8B SFT\" claim 基于单 seed，差异仅 0.01pp\n\n- 具体位置：§4.4 Table 3 最后一句；Introduction Contribution 4；Abstract 第 14 行\n- 问题：1.7B RSFT (50.50) vs 8B SFT (50.51) 差异 0.01pp，两者均为单 seed 结果（Table 8 caption：\"single seed for other scales\"）。在没有方差估计的情况下，声称\"matches\"在统计上没有意义。任何合理的 seed variance 都远超 0.01pp。这个 claim 在 Abstract 和 Introduction 中被重复强调，但证据极弱。\n- 建议：补充 1.7B RSFT 和 8B SFT 各 3-4 seeds 的结果，报告 confidence interval；或将 claim 改为\"approaches\"而非\"matches\"。\n\n**W3** [warning] CED 与 flat-NLI 差异仅 0.02pp，contrastive component 的贡献未被证明\n\n- 具体位置：§3.4 最后一段；§6 Ablation 段；Appendix Table 6\n- 问题：CED (Rel-F1 0.4563) vs flat-NLI (0.4561)，差异 0.02pp，且 flat-NLI 仅有 2 seeds（Appendix §8）。论文承认\"CED and flat-NLI produce comparable RSFT outcomes\"但仍将 CED 作为默认选择，理由是\"interpretable per-triple discrimination scores\"。然而论文没有任何实验展示这种 interpretability 带来的实际价值。CED 的 contrastive component 增加了方法复杂度但没有带来可测量的改进，这削弱了 CED 作为方法贡献的意义。\n- 建议：(1) flat-NLI 补充到 4 seeds 以做公平对比；(2) 如果差异仍不显著，诚实报告 contrastive component 可能不是必要的；(3) 或提供 case study 展示 CED 的 per-triple discrimination 在实际 error analysis 中如何优于 flat-NLI。\n\n**W4** [warning] Baseline 对比不完整，缺少关键参照系\n\n- 具体位置：§4.2 Table 1；§4.6 最后一段\n- 问题：(1) 缺少与 encoder-based evidence methods (SAIS, DREEAM, EIDER) 在相同 evaluation protocol 下的直接对比。论文在 §4.6 提到 DREEAM 的 joint Evi-F1 为 54.01%，而本文最佳为 ~36%，但这个对比被放在 Appendix 中一笔带过。(2) 缺少与其他 LLM-based DocRE 方法（AutoRE、LMRC 等，均在 Related Work 中讨论）的抽取性能对比。(3) Post-hoc evidence 仅测试了 BM25，没有测试更强的 learned retriever。\n- 建议：在 main results 中增加 SAIS/DREEAM 的数字作为参照（即使不同 protocol，也应在 Table 中注明并讨论差距来源）；增加至少一个 LLM-based DocRE baseline 的抽取性能对比。\n\n**W5** [warning] RSFT ablation 缺少 random selection baseline\n\n- 具体位置：§6 Ablation 段；Appendix §8\n- 问题：RSFT 消融比较了 CED vs flat-NLI 和 k=1 vs k=3，但缺少一个关键 baseline：random selection（从 8 个 candidate 中随机选 1 个作为训练数据）。没有这个 baseline，无法确定 RSFT 的改进是来自\"quality-based selection\"还是简单的\"data augmentation + selection\"效应（即使随机选择也可能因为 sampling diversity 带来改进）。\n- 建议：增加 random-k=1 baseline；如果 random 也有不错的改进，那 CED scoring 的贡献需要重新评估。\n\n**W6** [warning] GRPO/DPO 超参数探索不足\n\n- 具体位置：§3.3；Appendix Table 5\n- 问题：GRPO 仅测试 KL=0.01，DPO 仅测试 β=0.1。在 RL/preference optimization 文献中，KL 系数和 β 对 reward hacking 和 performance tradeoff 有显著影响（Gao et al., 2023; Moskovitz et al., 2024 均被论文引用）。如果 GRPO 在更大 KL penalty 下不 collapse，或 DPO 在更小 β 下不 degrade，decoupling spectrum 的结论需要修改。\n- 建议：至少对 GRPO 测试 KL ∈ {0.001, 0.01, 0.1} 和 DPO 测试 β ∈ {0.01, 0.1, 0.5}，或承认当前结论受限于特定超参数设置。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 格式不一致：Rel-F1 使用小数 (0.4049)，Evi-F1 使用百分比 (79.86)，EDCR 使用小数 (0.6982)。全表应统一。\n- Appendix 中有 7 个 orphan bib entries（Aho:72, APA:83, Ando2005, Chandra:81, Gusfield:97, andrew2007scalable, rasooli-tetrault-2015），疑似 ACL 模板遗留，应清理。\n- 引用 `autore2024` 的作者标注为 \"Anonymous\"，但该论文已正式发表（ACL 2024 System Demos），第一作者为 Xue 等人，应更新。类似地，`zhao2025egrpo`（E-GRPO）也标注 Anonymous。\n- 引用 `wang2025relprior`、`zhang2025glidre`、`hu2025reinforcepp`、`wang2025rear` 的第一作者与 OpenAlex 记录不匹配，需核实。\n- Appendix §14 Figure 4 caption 说\"93 relation types\"，但正文 §14 第一句说\"76 relation types with ≥5 evaluation samples\"，而 §4.1 说 DocRED 有 96 relation types。三个数字互相矛盾。\n- §4.3 DPO 3-epoch 的脚注提到\"pre-D076 evaluation protocol\"，未解释 D076 是什么。内部编号不应出现在投稿论文中。\n- §4.4 提到\"fair evaluation subset\"但未给出构建方法、样本量和完整结果。\n- RSFT 的 training samples 为 2,718（Table 5），但 §3.3 说\"9,042 training examples (37.3% acceptance rate)\"，数字不一致（9,042 × 37.3% ≠ 2,718；24,216 → 9,042 是 ~37.3%，但 Table 5 报告 2,718 training samples）。需要解释 9,042 candidates 如何变成 2,718 training samples。\n\n---\n\n## 主要优势\n\n1. **研究问题重要且定位精准**：LLM-based DocRE 缺乏 evidence grounding 是一个真实的实用性瓶颈，论文清晰地识别了 encoder-based evidence methods（SAIS/DREEAM）与 LLM-based extraction accuracy 之间的 gap（§1 第 16 行），问题动机有说服力。\n\n2. **实验覆盖面广**：跨 4 个模型规模、2 个模型家族、2 个数据集、3 种优化范式的系统性比较在 DocRE 文献中确实罕见。即使个别实验的统计严谨性不足，这种横向覆盖本身也有参考价值。\n\n3. **Decoupling spectrum 概念有启发性**：将 GRPO/DPO/RSFT 按 decoupling 严重程度排序的视角（Table 2）直观且有助于理解多目标生成任务中不同优化策略的行为差异。如果混淆变量问题得到修复，这将是一个有洞察力的贡献。\n\n4. **RSFT 效果稳定**：4-seed 结果方差较低（±0.49），跨数据集（DocRED +4.92pp, Re-DocRED +4.86pp）和跨模型家族（LLaMA +1.74pp）的改进模式一致（§4.6），说明 rejection sampling approach 的鲁棒性。\n\n5. **写作质量较好**：论文叙事结构清晰（问题→形式化→方法→实验→分析），Related Work 做了有效的 positioning（§2 区分了 encoder-based evidence 与 LLM-based generation 的结构性差异），不是简单的论文罗列。\n\n---\n\n## 缺失引用\n\n- **KGC/知识图谱补全视角**：论文讨论了 DocRE 但未引用知识图谱构建相关工作，考虑到 Introduction 明确提到\"knowledge graph construction\"作为下游应用。\n- **Multi-task learning / auxiliary loss 文献**：Evidence generation 作为辅助任务与 extraction 竞争 capacity 的分析框架，应引用 multi-task learning 的经典分析（如 Ruder 2017, Fifty et al. 2021 \"Efficiently Identifying Task Groupings for Multi-Task Learning\"）。\n- **Chain-of-thought / rationale generation**：Evidence generation 在概念上类似 CoT rationale generation，相关的 faithful reasoning 文献（如 Lanham et al. 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\"）可以丰富讨论。\n\n---\n\n## 总结\n\n论文提出了一个有价值的研究问题，实验覆盖面令人印象深刻。但在方法论严谨性上有明显短板：核心实验存在未解耦的混淆变量（N1），全部结果缺少 test set 验证（N2），主要 claim 缺乏统计检验（N3），scaling claim 的数据点不足（N4）。这些问题的共同效果是：论文的 claim 强度系统性地超过了实验证据的支撑力度。如果能补充 test set 结果、解耦 GRPO 实验、增加统计检验，本文有潜力达到 Conference 水平。当前状态建议 Findings。",
    "reviewer_id": "1",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-18T06:53:47.657729+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4523
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-18T06:53:57.434511+00:00_

审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.0 (Findings)** 的评分。论文研究问题有价值、实验覆盖面广，但存在 4 个 critical 问题：

1. **N1**: GRPO 实验同时改变量化精度和 group size，无法支撑 decoupling spectrum 的因果归因
2. **N2**: 全部结果仅在 dev set 上，缺少 test set 验证
3. **N3**: SFT baseline 无多 seed 方差，+4.92pp 改进未做显著性检验
4. **N4**: Non-monotonic scaling pattern 仅 3 个数据点，1.7B 的"benefit"有 repetition artifact 的替代解释

还有 6 个 should-fix 问题（EDCR 样本量不足、1.7B-vs-8B 单 seed claim、CED vs flat-NLI 无差异、baseline 不完整、缺 random selection ablation、GRPO/DPO 超参数探索不足）。核心判断：**claim 强度系统性超过证据支撑力度**，需补充实验后可升级至 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 53 · 2026-05-18T06:55:04.375969+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

# Reviewer 2 审稿意见 — Round 1

**Overall**: 3.0 (Findings)
**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。

## Must-Fix 问题

**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环

- EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。
- 建议：(1) 报告 p 值；(2) 提供 EDCR 相对于简单替代指标的增量诊断价值；(3) 对分母效应做敏感性分析。

**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献

- CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp。论文承认 "CED's contrastive design does not substantially outperform simpler NLI scoring"，但仍将 CED 作为独立贡献。消融否定了 CED 的量化优势。
- 建议：将 CED 降级为可选评分函数，将贡献定位为 "NLI-based quality filtering for RSFT"。

**N3** [critical] RSFT 训练数据量存在明确的数值矛盾

- Section 3.3 说 "9,042 training examples (37.3% acceptance rate)"，Appendix Table 4 说 "Training samples: 2,718"。9,042 vs 2,718 有 3.3 倍差距且不可调和。
- 建议：检查并统一这两个数字。

**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交

- 所有实验均在 DocRED dev set 上报告，test set 提交为 "pending"。

## Should-Fix 问题

**W1** [warning] 指标格式严重不一致
- Ign-F1 百分比格式（39.74），Rel-F1 小数格式（0.4049），Evi-F1 百分比（79.86）。

**W2** [warning] 引用数量偏低且多条 bib 条目不完整
- 32 篇引用（EMNLP long paper 通常 40-60 篇），15/32 条 "and others"，2 条 Anonymous。

**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑
- "implicit regularization" 解释是推测性的，无实验支撑；"fair evaluation subset" 未详细定义。

**W4** [warning] Multi-seed 覆盖不均匀
- 4B 有 4-seed，1.7B/8B/LLaMA 为单 seed 或 2 seed。

**W5** [warning] Related Work 缺少重要相关方向
- 缺少 multi-task learning / task interference 文献、self-consistency 范式、与 encoder-based 方法的直接数值比较。

**W6** [warning] "pre-D076 evaluation protocol" 未解释

## 缺失引用
1. Standley et al. (2020) "Which Tasks Should Be Learned Together in Multi-Task Learning?"
2. Yu et al. (2020) "Gradient Surgery for Multi-Task Learning"
3. Wang et al. (2023) "Self-Consistency Improves Chain of Thought Reasoning in Language Models"

## 主要优势
1. 实验规模和系统性
2. Scale-dependent evidence tax 是有意思的发现
3. 问题定义有价值
4. Decoupling spectrum 的诊断价值
5. 写作质量整体良好
6. RSFT "discrete selection avoids gradient-based trade-off" 洞察有一般性意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-18T06:56:42.057524+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: EDCR 与 Rel-F1 的定义循环性**\n\n同意，且我认为 R2 在此点上的分析比我自己的审稿更精确。我在 R1-W1 中指出了 n=6 样本量和 GRPO QLoRA outlier 的问题，但 R2 抓住了更根本的缺陷：EDCR 的分母包含 Rel-Recall，而 Rel-F1 本身是 Rel-Recall 和 Rel-Precision 的调和平均。ρ=-0.965 的相关性在数学上被定义关系部分预设了，不完全是经验发现。\n\n补充证据：§3.5 第 62-63 行的 EDCR 解释案例恰好说明了这个问题。论文说\"A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high Evi-Recall_TP and low Rel-Recall, yielding a high EDCR\"。这本质上是在说：当 Rel-Recall 低时 EDCR 高。而 Rel-Recall 低自然对应 Rel-F1 低（在 precision 不极端变化的情况下）。因此 EDCR 与 Rel-F1 的负相关性部分是 tautological 的。\n\n进一步地，论文在 §6 声称 per-relation EDCR 与 Evi-F1 独立（ρ=-0.064, p=0.58），将此作为\"evidence quality and extraction ability are fully decoupled across relation types\"的证据（Appendix §14）。但\"不显著相关\"不等于\"fully decoupled\"，这是一个经典的\"absence of evidence ≠ evidence of absence\"错误，尤其在 76 个 relation types 中可能存在 power 不足的情况。\n\nR2 的三条建议（报告 p 值、增量诊断价值、敏感性分析）均合理。我补充建议：作者应在去除 GRPO QLoRA 极端点后重新计算相关性，并展示 EDCR 相对于更简单替代指标（如 Evi-F1 - Rel-F1 差值）是否提供额外诊断信息。\n\n**[AGREE] R2-N2: CED 与 flat-NLI 几乎无差异**\n\n完全同意，与我的 R1-W3 一致。论文的消融数据（Appendix §8）自己否定了 CED contrastive component 的量化贡献：CED Rel-F1 0.4563 vs flat-NLI 0.4561，差距 0.02pp。flat-NLI 仅有 2 seeds，但即便如此，0.02pp 的差距在任何合理的 variance 下都不可能显著。\n\nR2 的建议（将贡献定位为 \"NLI-based quality filtering for RSFT\"）比论文当前的表述更准确。论文在 §3.4 最后一段承认了这一点（\"CED and flat-NLI produce comparable RSFT outcomes\"），但 Introduction Contribution 列表仍然将 CED 作为独立贡献（Contribution 4: \"RSFT with NLI-based CED scoring\"）。叙事与数据之间存在张力。\n\n补充：§6 Analysis 的 \"CED granularity\" 段提到 sentence-level CED filtering 失败（Evi-F1 下降 7.7pp），这虽然是有趣的负面发现，但并不证明 CED 优于 flat-NLI，只说明 evidence 质量是 response-level 属性。这个发现对 CED 和 flat-NLI 同样适用。\n\n**[AGREE] R2-N3: RSFT 训练数据量数值矛盾**\n\n同意。我在小问题中也标记了这个不一致。详细分析矛盾：\n\n- §3.3 RSFT 段（method.tex 第 30 行）：N=8 candidates per document, top-k=1, \"From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3% acceptance rate)\"\n- Appendix Table 5（appendix.tex 第 30 行）：Training samples = 2,718\n- DocRED 有 3,053 training documents（§4.1）\n\n数学核实：\n- 24,216 / 8 = 3,027 documents（与 3,053 接近，可能有些文档生成失败）\n- k=1 selection：应产生 ≤3,027 examples（每文档最多 1 个）\n- 9,042 / 3,027 ≈ 3.0，暗示实际使用了 k=3 而非 k=1\n- 2,718 < 3,027，可能是加了额外的 quality threshold 过滤\n\n这三个数字（9,042 / 2,718 / k=1 from 3,053 docs）互相矛盾，且无法通过合理解释调和。至少存在一处错误。这不仅是格式问题，它影响可复现性：研究者无法确定 RSFT 的实际训练数据规模。\n\n**[AGREE] R2-N4: 仅 Dev Set 结果**\n\n完全同意，与我的 R1-N2 一致。不再赘述。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 指标格式不一致**\n\n同意。我在小问题中也指出了这一点。Table 1 中 Ign-F1 = 39.74（百分比）、Rel-F1 = 0.4049（小数）、Evi-F1 = 79.86（百分比）混用确实造成阅读困难。补充一点：这种不一致贯穿全文，不仅限于 Table 1——Table 2、Table 3、Appendix Tables 均存在同样问题。\n\n**[AGREE] R2-W2: 引用数量偏低且 bib 条目不完整**\n\n部分同意。引用验证结果显示：33 unique cited keys，其中 7 条 orphan entries（ACL 模板遗留），5 条作者信息与 OpenAlex 不匹配（autore2024 标注 Anonymous 但实际第一作者为 Xue；wang2025relprior 第一作者应为 Pi 而非 Wang；zhang2025glidre 第一作者应为 Armingaud 而非 Zhang；hu2025reinforcepp 第一作者应为 Jian 而非 Hu；wang2025rear 第一作者应为 Luo 而非 Wang）。这些作者错误是实质性问题，需要修正。\n\n关于引用数量，33 篇确实偏低但不算致命——关键在于覆盖度而非数量。我在 R1 审稿中也指出了缺失的相关方向（multi-task learning、CoT faithful reasoning），R2 的缺失引用建议（Standley et al. 2020, Yu et al. 2020, Wang et al. 2023）合理。\n\n**[AGREE] R2-W3: 1.7B Evidence Benefit 解释缺乏支撑**\n\n强烈同意。这与我的 R1-N4 核心观点一致。\"Implicit regularization\" 是一个未经检验的假说（§4.4 第 93 行：\"We hypothesize that...\"），论文没有提供任何实验来区分 regularization 效应和 repetition-reduction 效应。Limitations 承认 1.7B 有 44.4% repetitive outputs（§7），这是一个已知的严重干扰因素。\"Fair evaluation subset\" 在 §4.4 中仅一句提及（\"On a fair evaluation subset that controls for output format effects, this benefit is +6.2 points\"），无任何细节。\n\n**[AGREE] R2-W4: Multi-seed 覆盖不均匀**\n\n同意。Appendix Table 8 caption 明确说\"single seed for other scales\"。4B 有 4 seeds，但 1.7B、8B、LLaMA-8B 均为单 seed。这意味着 Table 3 的 scaling analysis（论文 Contribution 3）中，4 行数据有 3 行基于单次实验。特别是 1.7B RSFT (50.50) 和 8B SFT (50.51) 的\"matches\"claim（我在 R1-W2 中详细分析）完全无统计意义。\n\n**[AGREE] R2-W5: Related Work 缺少重要相关方向**\n\n同意。论文的核心发现（evidence 和 extraction 在 gradient-based optimization 下竞争 capacity）本质上是一个 multi-task learning / task interference 问题，但 Related Work 没有引用 MTL 文献。这是一个显著遗漏，因为 MTL 文献中关于 task gradient conflict 的分析（如 R2 推荐的 Yu et al. 2020 \"Gradient Surgery\"）直接解释了为什么 GRPO/DPO 出现 decoupling 而 RSFT 不会。\n\n我在 R1 缺失引用中也指出了类似问题，补充推荐了 Ruder (2017) 和 Fifty et al. (2021) 作为 MTL 基础文献，以及 Lanham et al. (2023) 作为 faithful reasoning 文献。\n\n**[AGREE] R2-W6: \"pre-D076 evaluation protocol\" 未解释**\n\n同意，与我的小问题一致。Table 2 脚注中的 \"D076\" 是内部实验编号，在投稿论文中不应出现。更重要的是，DPO 3-epoch 使用了不同的 evaluation protocol 但被纳入了 decoupling spectrum 的相关性分析（Table 2），这污染了 ρ=-0.965 的计算。如果该数据点不可比，应从 spectrum 分析中移除或单独标注。\n\n---\n\n### 关于 R2 缺失引用的补充\n\nR2 推荐的三篇引用均合理：\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together\" — 直接相关于 evidence 和 extraction 作为两个 task 的 grouping/interference 分析\n2. Yu et al. (2020) \"Gradient Surgery\" — 解释了为什么 gradient-based methods (GRPO/DPO) 在多目标下失败而 selection-based methods (RSFT) 不会\n3. Wang et al. (2023) \"Self-Consistency\" — RSFT 的 sample-and-select 策略与 self-consistency 的 sample-and-vote 在概念上相近\n\n---\n\n### R1 与 R2 评分对比\n\n| 维度 | R1 | R2 | 差异说明 |\n|------|----|----|----------|\n| Soundness | 2.5 | 2.5 | 一致 |\n| Excitement | 3.5 | 3.0 | R1 认为问题定位稍好，但差异不大 |\n| Overall | 3.0 | 3.0 | 一致：Findings |\n| Reproducibility | 3 | 2.5 | R2 因数据不一致 (N3) 打分更低，合理 |\n\n**总体判断**：R2 的审稿与 R1 在核心问题上高度一致（dev-set-only、统计不足、CED 贡献存疑）。R2 在 EDCR 定义循环性（N1）和数据不一致（N3）上的分析比 R1 更尖锐。两份审稿共同指向同一个结论：论文 claim 强度系统性超过证据支撑力度，当前状态适合 Findings。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: EDCR 与 Rel-F1 的定义循环性**\n\n同意，且我认为 R2 在此点上的分析比我自己的审稿更精确。我在 R1-W1 中指出了 n=6 样本量和 GRPO QLoRA outlier 的问题，但 R2 抓住了更根本的缺陷：EDCR 的分母包含 Rel-Recall，而 Rel-F1 本身是 Rel-Recall 和 Rel-Precision 的调和平均。ρ=-0.965 的相关性在数学上被定义关系部分预设了，不完全是经验发现。\n\n补充证据：§3.5 第 62-63 行的 EDCR 解释案例恰好说明了这个问题。论文说\"A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high Evi-Recall_TP and low Rel-Recall, yielding a high EDCR\"。这本质上是在说：当 Rel-Recall 低时 EDCR 高。而 Rel-Recall 低自然对应 Rel-F1 低（在 precision 不极端变化的情况下）。因此 EDCR 与 Rel-F1 的负相关性部分是 tautological 的。\n\n进一步地，论文在 §6 声称 per-relation EDCR 与 Evi-F1 独立（ρ=-0.064, p=0.58），将此作为\"evidence quality and extraction ability are fully decoupled across relation types\"的证据（Appendix §14）。但\"不显著相关\"不等于\"fully decoupled\"，这是一个经典的\"absence of evidence ≠ evidence of absence\"错误，尤其在 76 个 relation types 中可能存在 power 不足的情况。\n\nR2 的三条建议（报告 p 值、增量诊断价值、敏感性分析）均合理。我补充建议：作者应在去除 GRPO QLoRA 极端点后重新计算相关性，并展示 EDCR 相对于更简单替代指标（如 Evi-F1 - Rel-F1 差值）是否提供额外诊断信息。\n\n**[AGREE] R2-N2: CED 与 flat-NLI 几乎无差异**\n\n完全同意，与我的 R1-W3 一致。论文的消融数据（Appendix §8）自己否定了 CED contrastive component 的量化贡献：CED Rel-F1 0.4563 vs flat-NLI 0.4561，差距 0.02pp。flat-NLI 仅有 2 seeds，但即便如此，0.02pp 的差距在任何合理的 variance 下都不可能显著。\n\nR2 的建议（将贡献定位为 \"NLI-based quality filtering for RSFT\"）比论文当前的表述更准确。论文在 §3.4 最后一段承认了这一点（\"CED and flat-NLI produce comparable RSFT outcomes\"），但 Introduction Contribution 列表仍然将 CED 作为独立贡献（Contribution 4: \"RSFT with NLI-based CED scoring\"）。叙事与数据之间存在张力。\n\n补充：§6 Analysis 的 \"CED granularity\" 段提到 sentence-level CED filtering 失败（Evi-F1 下降 7.7pp），这虽然是有趣的负面发现，但并不证明 CED 优于 flat-NLI，只说明 evidence 质量是 response-level 属性。这个发现对 CED 和 flat-NLI 同样适用。\n\n**[AGREE] R2-N3: RSFT 训练数据量数值矛盾**\n\n同意。我在小问题中也标记了这个不一致。详细分析矛盾：\n\n- §3.3 RSFT 段（method.tex 第 30 行）：N=8 candidates per document, top-k=1, \"From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3% acceptance rate)\"\n- Appendix Table 5（appendix.tex 第 30 行）：Training samples = 2,718\n- DocRED 有 3,053 training documents（§4.1）\n\n数学核实：\n- 24,216 / 8 = 3,027 documents（与 3,053 接近，可能有些文档生成失败）\n- k=1 selection：应产生 ≤3,027 examples（每文档最多 1 个）\n- 9,042 / 3,027 ≈ 3.0，暗示实际使用了 k=3 而非 k=1\n- 2,718 < 3,027，可能是加了额外的 quality threshold 过滤\n\n这三个数字（9,042 / 2,718 / k=1 from 3,053 docs）互相矛盾，且无法通过合理解释调和。至少存在一处错误。这不仅是格式问题，它影响可复现性：研究者无法确定 RSFT 的实际训练数据规模。\n\n**[AGREE] R2-N4: 仅 Dev Set 结果**\n\n完全同意，与我的 R1-N2 一致。不再赘述。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 指标格式不一致**\n\n同意。我在小问题中也指出了这一点。Table 1 中 Ign-F1 = 39.74（百分比）、Rel-F1 = 0.4049（小数）、Evi-F1 = 79.86（百分比）混用确实造成阅读困难。补充一点：这种不一致贯穿全文，不仅限于 Table 1——Table 2、Table 3、Appendix Tables 均存在同样问题。\n\n**[AGREE] R2-W2: 引用数量偏低且 bib 条目不完整**\n\n部分同意。引用验证结果显示：33 unique cited keys，其中 7 条 orphan entries（ACL 模板遗留），5 条作者信息与 OpenAlex 不匹配（autore2024 标注 Anonymous 但实际第一作者为 Xue；wang2025relprior 第一作者应为 Pi 而非 Wang；zhang2025glidre 第一作者应为 Armingaud 而非 Zhang；hu2025reinforcepp 第一作者应为 Jian 而非 Hu；wang2025rear 第一作者应为 Luo 而非 Wang）。这些作者错误是实质性问题，需要修正。\n\n关于引用数量，33 篇确实偏低但不算致命——关键在于覆盖度而非数量。我在 R1 审稿中也指出了缺失的相关方向（multi-task learning、CoT faithful reasoning），R2 的缺失引用建议（Standley et al. 2020, Yu et al. 2020, Wang et al. 2023）合理。\n\n**[AGREE] R2-W3: 1.7B Evidence Benefit 解释缺乏支撑**\n\n强烈同意。这与我的 R1-N4 核心观点一致。\"Implicit regularization\" 是一个未经检验的假说（§4.4 第 93 行：\"We hypothesize that...\"），论文没有提供任何实验来区分 regularization 效应和 repetition-reduction 效应。Limitations 承认 1.7B 有 44.4% repetitive outputs（§7），这是一个已知的严重干扰因素。\"Fair evaluation subset\" 在 §4.4 中仅一句提及（\"On a fair evaluation subset that controls for output format effects, this benefit is +6.2 points\"），无任何细节。\n\n**[AGREE] R2-W4: Multi-seed 覆盖不均匀**\n\n同意。Appendix Table 8 caption 明确说\"single seed for other scales\"。4B 有 4 seeds，但 1.7B、8B、LLaMA-8B 均为单 seed。这意味着 Table 3 的 scaling analysis（论文 Contribution 3）中，4 行数据有 3 行基于单次实验。特别是 1.7B RSFT (50.50) 和 8B SFT (50.51) 的\"matches\"claim（我在 R1-W2 中详细分析）完全无统计意义。\n\n**[AGREE] R2-W5: Related Work 缺少重要相关方向**\n\n同意。论文的核心发现（evidence 和 extraction 在 gradient-based optimization 下竞争 capacity）本质上是一个 multi-task learning / task interference 问题，但 Related Work 没有引用 MTL 文献。这是一个显著遗漏，因为 MTL 文献中关于 task gradient conflict 的分析（如 R2 推荐的 Yu et al. 2020 \"Gradient Surgery\"）直接解释了为什么 GRPO/DPO 出现 decoupling 而 RSFT 不会。\n\n我在 R1 缺失引用中也指出了类似问题，补充推荐了 Ruder (2017) 和 Fifty et al. (2021) 作为 MTL 基础文献，以及 Lanham et al. (2023) 作为 faithful reasoning 文献。\n\n**[AGREE] R2-W6: \"pre-D076 evaluation protocol\" 未解释**\n\n同意，与我的小问题一致。Table 2 脚注中的 \"D076\" 是内部实验编号，在投稿论文中不应出现。更重要的是，DPO 3-epoch 使用了不同的 evaluation protocol 但被纳入了 decoupling spectrum 的相关性分析（Table 2），这污染了 ρ=-0.965 的计算。如果该数据点不可比，应从 spectrum 分析中移除或单独标注。\n\n---\n\n### 关于 R2 缺失引用的补充\n\nR2 推荐的三篇引用均合理：\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together\" — 直接相关于 evidence 和 extraction 作为两个 task 的 grouping/interference 分析\n2. Yu et al. (2020) \"Gradient Surgery\" — 解释了为什么 gradient-based methods (GRPO/DPO) 在多目标下失败而 selection-based methods (RSFT) 不会\n3. Wang et al. (2023) \"Self-Consistency\" — RSFT 的 sample-and-select 策略与 self-consistency 的 sample-and-vote 在概念上相近\n\n---\n\n### R1 与 R2 评分对比\n\n| 维度 | R1 | R2 | 差异说明 |\n|------|----|----|----------|\n| Soundness | 2.5 | 2.5 | 一致 |\n| Excitement | 3.5 | 3.0 | R1 认为问题定位稍好，但差异不大 |\n| Overall | 3.0 | 3.0 | 一致：Findings |\n| Reproducibility | 3 | 2.5 | R2 因数据不一致 (N3) 打分更低，合理 |\n\n**总体判断**：R2 的审稿与 R1 在核心问题上高度一致（dev-set-only、统计不足、CED 贡献存疑）。R2 在 EDCR 定义循环性（N1）和数据不一致（N3）上的分析比 R1 更尖锐。两份审稿共同指向同一个结论：论文 claim 强度系统性超过证据支撑力度，当前状态适合 Findings。",
    "reviewer_id": "1",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-18T06:56:46.177565+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4120
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-18T06:56:53.096810+00:00_

交叉回应已提交。R2 的 4 个 Must-Fix 和 6 个 Should-Fix 全部标记为 [AGREE]，主要原因：

- **N1 (EDCR 循环性)**：R2 比我更精准地指出了 Rel-Recall 同时出现在 EDCR 分母和 Rel-F1 中的 tautological 问题
- **N2 (CED≈flat-NLI)**：与我的 R1-W3 一致，0.02pp 差异无统计意义
- **N3 (9,042 vs 2,718)**：数学上不可调和的矛盾，影响可复现性
- **N4 (dev-set-only)**：与我的 R1-N2 一致

两份审稿在 Overall 3.0 (Findings) 上完全一致，核心问题高度重叠：claim 强度超过证据支撑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---

## Round 3

54 recorded events

### User

_source line 57 · 2026-05-23T00:51:55.453354+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## 论文信息
- **标题**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction
- **路径**: projects/faith-evidence-ie/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf
- **目标 Venue**: EMNLP 2026（通过 ARR 统一审稿）
- **截止日期**: 2026-07-15（commitment deadline）

## Venue 要求
- ARR 统一审稿，Main/Findings 不分开投稿
- Long paper: 正文 8 页限制，参考文献不限
- Mandatory limitations + optional ethics statement 不计入页数
- Double-blind 匿名审稿
- ACL 模板
- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查重点

1. **CED 评分函数（Section 3.4）的严谨性**：
   - CED = p⁺ − max_j p⁻_j 这个公式是否合理？正向 NLI 分数和负向 NLI 分数的组合是否有理论依据？
   - Document-level CED 加权方式（只有正确 triple 贡献 CED）是否引入循环依赖——用 gold label 选择 triple 来评估 scoring function？
   - CED 与 flat-NLI 效果几乎一样（Rel-F1 差 0.02pp），这是否说明 contrastive formulation 的价值有限？

2. **EDCR 指标（Section 3.5）的统计有效性**：
   - EDCR = Evi-Recall_TP / Rel-Recall，分子分母共享 Rel-Recall 相关成分。论文声称 cross-method 相关性 (ρ=−0.89, n=7) 但 n=7 样本量极小，p=0.007 在多重比较下是否可靠？
   - Per-relation 相关性 (ρ=−0.79, n=76) 是否也存在共享成分问题？
   - EDCR 作为新指标是否有充分验证（论文也承认缺乏 human judgment 验证）？

3. **方差压缩声明的统计基础**：
   - "4.6–31× variance compression" 声明基于 3 个 seed 的 std 比较。n=3 的方差估计极不稳定——3 个观测值的标准差置信区间是多少？
   - SFT 和 RSFT 测的是不同来源的方差（SFT: 完整训练的 seed 方差；RSFT: 固定基础上的微调方差），直接比较是否公平？论文承认了这一点但仍做了强声明。
   - Cohen's d=2.58 是从 n=3 计算的——小样本 effect size 估计是否可信？

4. **实验控制与公平性**：
   - GRPO QLoRA 使用 4-bit 量化 G=4，GRPO bf16 使用 G=8——变量未隔离（精度和 group size 同时变化），collapse 到底是量化还是 group size 导致的？
   - DPO 3-epoch 用的是 "earlier evaluation protocol"，这个差异对 decoupling spectrum 的可比性影响多大？
   - Evidence tax 在不同 scale 使用不同 seed（1.7B 用 s42, 4B 用 Method B s44），控制变量是否充分？
   - 4B retrained checkpoint 用于 test（原始不可用），dev 性能 "comparable"（43.88 vs 44.23）但有 0.35pp 差距，是否影响结论？

5. **Test set 结果的可靠性**：
   - Dev 到 test 有 ~20pp drop，论文归因于 annotation density 2.82×。但这个 drop 是否太大，是否有过拟合 dev set 的嫌疑？
   - 14B RSFT 在 test 上反而低于 SFT（−0.37pp），但论文解释为 "truncation rate" 不同——这个解释是否充分？

6. **基线比较的公平性**：
   - 与 encoder methods (ATLOP, SAIS, DREEAM) 的对比：Ign-F1 差距 16-18pp（encoder ~62, LLM ~45），论文只强调 TP-only Evi-F1 >80%——这是否是 cherry-picking 指标？
   - 没有与其他 LLM-based RE 方法（AutoRE, LMRC 等）的直接数值对比。

请按以下格式输出审稿意见：
### Summary（2-3句）
### Strengths（逐条）
### Weaknesses（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）
### Questions（需要作者澄清的）
### Missing References（如有）
### Overall Assessment（评分 + 置信度 + 理由）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-23T00:52:11.111562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-23T00:52:12.417199+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1305
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-23T00:52:12.568331+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-23T00:52:12.618988+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-23T00:52:19.658862+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-23T00:52:21.572932+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
  "pages": "1-10",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
    "pages": "1-10",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-23T00:52:27.816560+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that par
…[truncated 1262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8157
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-23T00:52:29.226946+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 543.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.3}, {\"page\": 10, \"pa
…[truncated 427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7654
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-23T00:52:37.871689+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. List every field name, its description, and the scoring options (e.g., 1-5 scale with labels). Focus on: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other scoring dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. List every field name, its description, and the scoring options (e.g., 1-5 scale with labels). Focus on: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other scoring dimensions."
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-23T00:52:38.829440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-23T00:52:39.231210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-23T00:52:39.738080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-23T00:52:39.738554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-23T00:52:40.241429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-23T00:52:40.952794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1721
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-23T00:52:40.955312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-23T00:52:41.167522+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1428
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-23T00:52:41.725279+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1483
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-23T00:52:41.976940+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1021
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-23T00:52:45.492124+00:00_

# ACL Rolling Review Form Fields and Scoring Dimensions

## Primary Scoring Dimensions

**Reviewer Confidence**
- Scale: 1-5
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure"
- 3 = "Pretty sure, but there's a chance I missed something"
- 2 = "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1 = "Not my area, or paper is very hard to understand"

**Soundness**
- Scale: 1-5 (with .5 increments)
- 5 = "Excellent: This study is one of the most thorough I have seen"
- 4 = "Strong: This study provides sufficient support for all of its claims"
- 3 = "Acceptable: This study provides sufficient support for its main claims"
- 2 = "Poor: Some of the main claims are not sufficiently supported"
- 1 = "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement**
- Scale: 1-5 (with .5 increments)
- 5 = "Highly Exciting: I would recommend this paper to others"
- 4 = "Exciting: I would mention this paper to others"
- 3 = "Interesting: I might mention some points of this paper"
- 2 = "Potentially Interesting: does not resonate with me, but it might with others"
- 1 = "Not Exciting: does not resonate with me"

**Overall Assessment**
- Scale: 1-5 (with .5 increments)
- 5 = "Consider for Award"
- 4 = "Conference"
- 3 = "Findings"
- 2 = "Resubmit next cycle"
- 1 = "Do not resubmit"

**Reproducibility**
- Scale: 1-5
- 5 = "They could easily reproduce the results"
- 4 = "They could mostly reproduce the results"
- 3 = "They could reproduce with some difficulty"
- 2 = "They would be hard pressed to reproduce"
- 1 = "They would not be able to reproduce"

**Datasets**
- Scale: 1-5
- 5 = "Enabling"
- 4 = "Useful"
- 3 = "Potentially useful"
- 2 = "Documentary"
- 1 = "No usable datasets submitted"

**Software**
- Scale: 1-5
- 5 = "Enabling"
- 4 = "Useful"
- 3 = "Potentially useful"
- 2 = "Documentary"
- 1 = "No usable software released"

## Narrative Sections

- Paper Summary
- Summary of Strengths
- Summar
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7620
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-23T00:52:51.869851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-23T00:52:52.724137+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-23T00:52:52.875227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-23T00:52:53.380563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-23T00:52:53.835461+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-23T00:52:53.835945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-23T00:52:55.145711+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1765
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-23T00:52:55.349468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-23T00:52:55.851723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2015
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-23T00:52:56.355838+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
  "pages": "11-17",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
    "pages": "11-17",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-23T00:52:56.709339+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-23T00:52:58.167699+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 117.3}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1811
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-23T00:53:02.636439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-23T00:53:03.139802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-23T00:53:03.340872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-23T00:53:03.542028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-23T00:53:03.994570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-23T00:53:04.999985+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1659
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-23T00:53:05.000767+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1458
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-23T00:53:05.001548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-23T00:53:05.152899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-23T00:53:05.407499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-23T00:53:05.762485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-23T00:53:05.915478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-23T00:53:06.168478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1015
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-23T00:53:06.370150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 962
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-23T00:57:41.679523+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026 (ACL ARR)\n\n---\n\n### Summary（2-3句）\n\n本文将 evidence-grounded DocRE 形式化为结构化生成任务，系统比较了三种 post-SFT 优化范式（GRPO、DPO、RSFT）在 evidence 生成与 relation extraction 之间的 trade-off。核心发现包括：(1) evidence tax 是 scale-dependent 的（1.7B 有益、4B+ 中性）；(2) 梯度优化方法导致 extraction-evidence decoupling，离散选择方法（RSFT）可避免；(3) RSFT 通过 CED-based 样本选择压缩训练方差。论文覆盖面广（1.7B-14B，Qwen3/LLaMA 两个 model family），分析视角有启发性，但多处统计推断基础薄弱。\n\n---\n\n### Strengths\n\n**S1. 问题定位精准且实用。** Evidence grounding 是 LLM-based IE 部署中的真实痛点——临床知识库、法律尽调等场景需要可溯源的抽取结果。论文清晰地指出 encoder 方法（SAIS、DREEAM）和 LLM 方法在 evidence 处理上的结构性差异（分类 vs. 生成），这一 framing 具有 community 价值。\n\n**S2. Decoupling spectrum 概念有分析价值。** 将 GRPO collapse、GRPO mild decoupling、DPO gradual decay、RSFT no decoupling 组织为一个连续谱（Table 2, Figure 1），从优化机制角度（gradient pressure vs. discrete selection）解释了为什么不同范式表现不同。这种分析视角比简单报告\"方法 A 比方法 B 好\"更有洞察力。\n\n**S3. 跨尺度 + 跨 model family 的实验覆盖。** 1.7B/4B/8B/14B（Qwen3）+ LLaMA-3.1-8B 的五模型覆盖，加上 Re-DocRED 的 cross-dataset 验证（Table 9-10），在同类工作中覆盖面较好。\n\n**S4. 对自身局限的透明度。** 论文主动承认了多项局限：EDCR 缺乏 human judgment 验证、variance 估计基于 3 seeds、SFT vs RSFT variance 测量的不同来源（Section 7）。这种透明度值得肯定，但承认局限不等于解决了它们。\n\n**S5. 定性分析具体有用。** Section M 的三个 case study（evidence quality、GRPO format gaming、per-relation EDCR diagnostics）用具体例子展示了 EDCR 指标的诊断价值，比如 `date_of_birth` (EDCR=0.119) vs `head_of_government` (EDCR=0.936) 的对比。\n\n---\n\n### Weaknesses\n\n**W1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础。**\n\n论文的第三个核心贡献是 \"RSFT compresses training variance 4.6–31×\"（Abstract, Section 4.3），并给出 Cohen's d=2.58。但这些都基于 3 个 seed 的 std 比较。\n\n- **置信区间极宽**：n=3 时方差估计的自由度 df=2。根据 χ² 分布，σ 的 95% CI 约为 [0.52s, 6.29s]——即真实 σ 可能比估计值大 6 倍或小 2 倍。当两组各 n=3 时，方差比的 F(2,2) 分布的 95% CI 跨越数个数量级。声称 \"31× compression\" 在统计上几乎无法从 n=3 中可靠估计。\n- **Cohen's d=2.58 不可信**：小样本 effect size 的抽样分布极宽，n=3 时 d 的标准误约为 1.2-1.5，95% CI 覆盖从接近 0 到 >5 的范围。论文不应将其作为核心声明呈现。\n- **建议**：至少增加到 5-10 seeds（尤其对 1.7B 这样训练成本低的尺度可行），或将方差压缩声明从 contribution 降级为 observation，并报告 bootstrap CI。\n\n**W2 [CRITICAL] — EDCR 的 shared-component 问题使 cross-method 相关性不可靠。**\n\nEDCR = Evi-Recall_TP / Rel-Recall。展开：\n\nEvi-Recall_TP = TP_evi / TP，Rel-Recall = TP / G（G 为 gold triples 总数）\n\n因此 EDCR = (TP_evi × G) / TP²\n\nTP 同时出现在分子和分母中。当一个方法找到更多正确 relation（TP↑），Rel-Recall 机械性增大（EDCR 分母↑），而新增 TP 如果 evidence 质量较低则 Evi-Recall_TP 下降（EDCR 分子↓）。这构造了一个**机械性负相关**——即使 evidence 能力和 extraction 能力完全独立，EDCR 也会随 Rel-Recall 增加而降低。\n\n- 论文声称 cross-method ρ=−0.89 (n=7, p=0.007)（Section 5），但 n=7 极小，一个 outlier（如 GRPO QLoRA collapse 的极端点 EDCR=0.9876）可能主导相关性。移除该点后相关性是否仍然显著？\n- Per-relation ρ=−0.79 (n=76) 面临同样的 shared-component 问题，因为 per-relation EDCR 结构相同。\n- **建议**：(1) 报告移除 GRPO QLoRA extreme point 后的 cross-method 相关性；(2) 用 permutation test 或 partial correlation 控制 TP 的共享效应；(3) 展示 EDCR 与 Evi-F1（不含 shared component）的对比来证明 EDCR 的增量诊断价值。\n\n**W3 [MAJOR] — CED contrastive formulation 的增量价值不足。**\n\nSection 3.4 引入 CED = p⁺ − max_j p⁻_j 作为 contrastive evidence discrimination score。但 Appendix B 的消融显示 CED vs flat-NLI（仅用 p⁺）在 RSFT 中的 Rel-F1 差异仅 0.02pp（45.63 vs 45.61）。\n\n- 减法操作（p⁺ − max_j p⁻_j）缺乏理论动机：为什么是差值而非比值（p⁺/max p⁻_j）或 log-ratio？论文仅说 \"This formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities\"（Section 3.4），但没有解释为什么减法最优。\n- 0.02pp 的差异在 noise level 以内（3-seed std 约 0.09pp），contrastive 组件对下游无实质影响。\n- 论文说 \"confirming that the contrastive formulation is not essential for data selection quality\"（Section 3.4 末段），这实际上削弱了 CED 作为方法贡献的分量。\n- **建议**：降低 CED 的 novelty claim，或提供 CED 在更困难场景（如 long-tail relation types、entity-dense documents）中优于 flat-NLI 的证据。\n\n**W4 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol 影响 decoupling spectrum 的可比性。**\n\nFootnote 1（page 6）提到 \"DPO 3-epoch results use an earlier evaluation protocol, included for trend analysis\"。但 Table 2 将 DPO 3-epoch 与其他方法并列在同一个 decoupling spectrum 表中，读者容易将其视为直接可比的数据点。\n\n- Decoupling spectrum（Section 4.3, Figure 1）是本文的核心分析框架之一。如果其中一个数据点（DPO 3-epoch）来自不同 protocol，整个 spectrum 的可靠性受质疑。\n- \"Earlier evaluation protocol\" 具体差异是什么？这会如何影响 Rel-F1 和 Evi-F1 的计算？论文未充分说明。\n- **建议**：在相同 protocol 下重跑 DPO 3-epoch 评估，或在 Table 2 中明确标注并从 spectrum 分析中排除。\n\n**W5 [MAJOR] — SFT vs RSFT variance 测量的不同来源使得直接比较不公平。**\n\nSFT 的 variance 来自 3 个独立 full training runs（不同 seed），RSFT 的 variance 来自在固定 SFT base 上的 fine-tuning（不同 seed）。这测量的是不同层次的随机性：\n\n- SFT variance = 数据打乱 + 初始化 + 训练动态的综合方差\n- RSFT variance = 候选样本选择 + fine-tuning 的方差（base model 固定）\n\nRSFT 的方差天然更小，因为大部分随机性被 base model 吸收了。论文在 Section 7 承认了这一点（\"RSFT reflects additional fine-tuning from a fixed base\"），但仍在 Abstract 和 Contribution 中将 \"4.6–31× variance compression\" 作为核心声明。\n\n- 公平比较应是：从相同 3 个 SFT checkpoint 分别做 RSFT，报告端到端方差（而非仅 RSFT 阶段方差）。\n- 或至少将此作为 observation 而非 contribution 呈现，明确说明这是不同方差来源的比较。\n\n**W6 [MAJOR] — Dev→Test 20pp drop 的解释不够充分。**\n\nTable 9 显示 Ign-F1 从 dev ~45 降到 test ~25-28（约 18-20pp drop）。论文归因于 Re-DocRED test set 的 annotation density 是 dev 的 2.82×。\n\n- 2.82× 的 annotation density 差异确实会增加 recall 难度，但 20pp drop 的幅度仍然令人担忧。是否有 dev set overfitting 的可能？例如，hyperparameter tuning 和 model selection 都在 dev 上进行。\n- 14B RSFT 在 test 上低于 SFT 0.37pp（Table 9 注释），论文解释为 \"truncation rate\" 差异。但如果 RSFT 的优势在 test 上消失甚至反转，这是否意味着 RSFT 的 gain 不够 robust？\n- **建议**：报告 test set 上的完整 decoupling 分析（不仅是 Ign-F1），展示 dev 上观察到的 pattern 是否在 test 上 replicate。\n\n**W7 [MINOR] — 与 encoder baseline 的比较选择性呈现指标。**\n\nTable 12（Appendix）显示 encoder 方法（ATLOP、SAIS、DREEAM）的 Ign-F1 约 62，而 LLM 方法约 45，差距 16-18pp。论文在主文中主要强调 TP-only Evi-F1（>80%）和 EDCR 优势，未充分讨论这一巨大性能差距的含义。\n\n- 论文第 7 页最后一段提到 \"encoder methods achieve substantially higher extraction performance (Rel-F1 60-63 vs. our 45-56)\"，但将其归因于 \"architecture-specific optimization for the classification formulation\"，篇幅很少。\n- 对于 deployment 场景的用户，Ign-F1 45 vs 62 是一个实质性差距。论文应更充分讨论 LLM-based 方法何时值得这一性能牺牲。\n\n**W8 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比。**\n\nRelated Work（Section 2）讨论了 AutoRE (Xue et al., 2024)、GildRE、ReLLM 等 LLM-based 方法，但 Table 12 仅对比 encoder 方法。虽然这些方法可能不产 evidence，但至少可以在 Rel-F1 上直接比较。\n\n**W9 [MINOR] — 4B retrained checkpoint 的 dev performance 差距 0.35pp 可能影响 evidence tax 分析。**\n\nSection 4.1 提到原始 4B checkpoint 不可用，retrained version 的 dev Ign-F1 为 43.88 vs 原始 44.23（差 0.35pp）。0.35pp 虽然看似小，但论文在 evidence tax 分析中关注的差异也在 0.25-0.47pp 量级（Section 4.4, Appendix E），这意味着 checkpoint 差异可能与被分析的效应大小可比。\n\n---\n\n### Questions（需要作者澄清）\n\n**Q1.** Cross-method EDCR 相关性 (ρ=−0.89, n=7) 中，移除 GRPO QLoRA collapse 的极端数据点后，ρ 和 p-value 变为多少？\n\n**Q2.** RSFT variance 声明中的 \"4.6–31×\" 区间对应哪些具体 scale？请提供每个 scale 的 SFT std 和 RSFT std 的 95% CI（基于 χ² 分布）。\n\n**Q3.** DPO 3-epoch 的 \"earlier evaluation protocol\" 与当前 protocol 的具体差异是什么？是 max_new_tokens、format-compliant intersection 筛选规则、还是其他？\n\n**Q4.** 关于 evidence tax（Section 4.4, Appendix E）：Qwen3-1.7B 的 training-time evidence tax（约 −5.19±5.25pp）方差极大——这是否意味着 evidence tax 的 direction 在 1.7B 上也不稳定？\n\n**Q5.** CED 的减法公式 (p⁺ − max p⁻_j) 是否尝试过其他组合方式（ratio、log-ratio、learned combination）？如何确定减法是最佳选择？\n\n**Q6.** Table 2 中 GRPO bf16 G=4 和 G=8 的 Rel-F1 分别是多少？论文是否可以明确隔离 group size vs precision 对 collapse 的独立贡献？\n\n---\n\n### Missing References\n\n- 未发现明显遗漏的关键引用。Related Work 覆盖了 DocRE（DocRED, ATLOP, DREEAM）、LLM-based IE（AutoRE, GildRE）、RL alignment（GRPO, DPO, RAFT）、evidence faithfulness（StAR）等主要线索。\n- 可考虑引用 Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\" 作为 LLM-based RE 的综述性参考（如未引用）。\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 论文提出了有价值的分析框架（evidence tax、decoupling spectrum、EDCR），实验覆盖面广，但核心统计声明（variance compression、EDCR correlation）的推断基础薄弱，需要加固。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法（CED、RSFT）合理，但多处统计推断基础薄弱：n=3 的 variance claim、EDCR shared-component、CED 增量价值不足。方法假设总体成立但验证不够严格 |\n| Excitement | 3.5/5 | Evidence tax 和 decoupling spectrum 概念有新意且对社区有启发价值；RSFT 本身是标准 rejection sampling，方法创新有限；分析型贡献 > 方法型贡献 |\n| Reproducibility | 4/5 | Hyperparameters 详尽（Table 4, Appendix A），数据集公开（DocRED），CED 依赖外部 NLI model（DeBERTa-v3-large）有明确说明。代码承诺开源。唯一扣分：CED scoring 需要特定 NLI model 的 prompt 格式细节 |\n| Confidence | 4/5 | Quite sure. 论文的核心领域（DocRE、LLM fine-tuning、RL alignment）在我的专业范围内，统计方法论的问题是明确可判断的 |\n\n### 最终判断\n\n本文的分析视角（evidence 不是 free lunch，优化范式决定 decoupling 程度）对 LLM-based IE 社区有实质价值。但三个核心贡献中：\n1. **Evidence tax**（扎实）——scale-dependent 的发现有 cross-family 验证支撑\n2. **Decoupling spectrum + EDCR**（中等）——概念好但 EDCR 的统计验证有结构性缺陷\n3. **Variance compression**（薄弱）——n=3 的统计基础无法支撑量化声明\n\n如果 W1（variance claim 的统计基础）和 W2（EDCR shared-component）能得到实质性回应（如增加 seeds、提供 partial correlation），可上调至 4.0（Conference）。目前判断为 3.5（Borderline Conference），主要因为统计方法论的不足削弱了本应很强的 empirical story。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026 (ACL ARR)\n\n---\n\n### Summary（2-3句）\n\n本文将 evidence-grounded DocRE 形式化为结构化生成任务，系统比较了三种 post-SFT 优化范式（GRPO、DPO、RSFT）在 evidence 生成与 relation extraction 之间的 trade-off。核心发现包括：(1) evidence tax 是 scale-dependent 的（1.7B 有益、4B+ 中性）；(2) 梯度优化方法导致 extraction-evidence decoupling，离散选择方法（RSFT）可避免；(3) RSFT 通过 CED-based 样本选择压缩训练方差。论文覆盖面广（1.7B-14B，Qwen3/LLaMA 两个 model family），分析视角有启发性，但多处统计推断基础薄弱。\n\n---\n\n### Strengths\n\n**S1. 问题定位精准且实用。** Evidence grounding 是 LLM-based IE 部署中的真实痛点——临床知识库、法律尽调等场景需要可溯源的抽取结果。论文清晰地指出 encoder 方法（SAIS、DREEAM）和 LLM 方法在 evidence 处理上的结构性差异（分类 vs. 生成），这一 framing 具有 community 价值。\n\n**S2. Decoupling spectrum 概念有分析价值。** 将 GRPO collapse、GRPO mild decoupling、DPO gradual decay、RSFT no decoupling 组织为一个连续谱（Table 2, Figure 1），从优化机制角度（gradient pressure vs. discrete selection）解释了为什么不同范式表现不同。这种分析视角比简单报告\"方法 A 比方法 B 好\"更有洞察力。\n\n**S3. 跨尺度 + 跨 model family 的实验覆盖。** 1.7B/4B/8B/14B（Qwen3）+ LLaMA-3.1-8B 的五模型覆盖，加上 Re-DocRED 的 cross-dataset 验证（Table 9-10），在同类工作中覆盖面较好。\n\n**S4. 对自身局限的透明度。** 论文主动承认了多项局限：EDCR 缺乏 human judgment 验证、variance 估计基于 3 seeds、SFT vs RSFT variance 测量的不同来源（Section 7）。这种透明度值得肯定，但承认局限不等于解决了它们。\n\n**S5. 定性分析具体有用。** Section M 的三个 case study（evidence quality、GRPO format gaming、per-relation EDCR diagnostics）用具体例子展示了 EDCR 指标的诊断价值，比如 `date_of_birth` (EDCR=0.119) vs `head_of_government` (EDCR=0.936) 的对比。\n\n---\n\n### Weaknesses\n\n**W1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础。**\n\n论文的第三个核心贡献是 \"RSFT compresses training variance 4.6–31×\"（Abstract, Section 4.3），并给出 Cohen's d=2.58。但这些都基于 3 个 seed 的 std 比较。\n\n- **置信区间极宽**：n=3 时方差估计的自由度 df=2。根据 χ² 分布，σ 的 95% CI 约为 [0.52s, 6.29s]——即真实 σ 可能比估计值大 6 倍或小 2 倍。当两组各 n=3 时，方差比的 F(2,2) 分布的 95% CI 跨越数个数量级。声称 \"31× compression\" 在统计上几乎无法从 n=3 中可靠估计。\n- **Cohen's d=2.58 不可信**：小样本 effect size 的抽样分布极宽，n=3 时 d 的标准误约为 1.2-1.5，95% CI 覆盖从接近 0 到 >5 的范围。论文不应将其作为核心声明呈现。\n- **建议**：至少增加到 5-10 seeds（尤其对 1.7B 这样训练成本低的尺度可行），或将方差压缩声明从 contribution 降级为 observation，并报告 bootstrap CI。\n\n**W2 [CRITICAL] — EDCR 的 shared-component 问题使 cross-method 相关性不可靠。**\n\nEDCR = Evi-Recall_TP / Rel-Recall。展开：\n\nEvi-Recall_TP = TP_evi / TP，Rel-Recall = TP / G（G 为 gold triples 总数）\n\n因此 EDCR = (TP_evi × G) / TP²\n\nTP 同时出现在分子和分母中。当一个方法找到更多正确 relation（TP↑），Rel-Recall 机械性增大（EDCR 分母↑），而新增 TP 如果 evidence 质量较低则 Evi-Recall_TP 下降（EDCR 分子↓）。这构造了一个**机械性负相关**——即使 evidence 能力和 extraction 能力完全独立，EDCR 也会随 Rel-Recall 增加而降低。\n\n- 论文声称 cross-method ρ=−0.89 (n=7, p=0.007)（Section 5），但 n=7 极小，一个 outlier（如 GRPO QLoRA collapse 的极端点 EDCR=0.9876）可能主导相关性。移除该点后相关性是否仍然显著？\n- Per-relation ρ=−0.79 (n=76) 面临同样的 shared-component 问题，因为 per-relation EDCR 结构相同。\n- **建议**：(1) 报告移除 GRPO QLoRA extreme point 后的 cross-method 相关性；(2) 用 permutation test 或 partial correlation 控制 TP 的共享效应；(3) 展示 EDCR 与 Evi-F1（不含 shared component）的对比来证明 EDCR 的增量诊断价值。\n\n**W3 [MAJOR] — CED contrastive formulation 的增量价值不足。**\n\nSection 3.4 引入 CED = p⁺ − max_j p⁻_j 作为 contrastive evidence discrimination score。但 Appendix B 的消融显示 CED vs flat-NLI（仅用 p⁺）在 RSFT 中的 Rel-F1 差异仅 0.02pp（45.63 vs 45.61）。\n\n- 减法操作（p⁺ − max_j p⁻_j）缺乏理论动机：为什么是差值而非比值（p⁺/max p⁻_j）或 log-ratio？论文仅说 \"This formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities\"（Section 3.4），但没有解释为什么减法最优。\n- 0.02pp 的差异在 noise level 以内（3-seed std 约 0.09pp），contrastive 组件对下游无实质影响。\n- 论文说 \"confirming that the contrastive formulation is not essential for data selection quality\"（Section 3.4 末段），这实际上削弱了 CED 作为方法贡献的分量。\n- **建议**：降低 CED 的 novelty claim，或提供 CED 在更困难场景（如 long-tail relation types、entity-dense documents）中优于 flat-NLI 的证据。\n\n**W4 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol 影响 decoupling spectrum 的可比性。**\n\nFootnote 1（page 6）提到 \"DPO 3-epoch results use an earlier evaluation protocol, included for trend analysis\"。但 Table 2 将 DPO 3-epoch 与其他方法并列在同一个 decoupling spectrum 表中，读者容易将其视为直接可比的数据点。\n\n- Decoupling spectrum（Section 4.3, Figure 1）是本文的核心分析框架之一。如果其中一个数据点（DPO 3-epoch）来自不同 protocol，整个 spectrum 的可靠性受质疑。\n- \"Earlier evaluation protocol\" 具体差异是什么？这会如何影响 Rel-F1 和 Evi-F1 的计算？论文未充分说明。\n- **建议**：在相同 protocol 下重跑 DPO 3-epoch 评估，或在 Table 2 中明确标注并从 spectrum 分析中排除。\n\n**W5 [MAJOR] — SFT vs RSFT variance 测量的不同来源使得直接比较不公平。**\n\nSFT 的 variance 来自 3 个独立 full training runs（不同 seed），RSFT 的 variance 来自在固定 SFT base 上的 fine-tuning（不同 seed）。这测量的是不同层次的随机性：\n\n- SFT variance = 数据打乱 + 初始化 + 训练动态的综合方差\n- RSFT variance = 候选样本选择 + fine-tuning 的方差（base model 固定）\n\nRSFT 的方差天然更小，因为大部分随机性被 base model 吸收了。论文在 Section 7 承认了这一点（\"RSFT reflects additional fine-tuning from a fixed base\"），但仍在 Abstract 和 Contribution 中将 \"4.6–31× variance compression\" 作为核心声明。\n\n- 公平比较应是：从相同 3 个 SFT checkpoint 分别做 RSFT，报告端到端方差（而非仅 RSFT 阶段方差）。\n- 或至少将此作为 observation 而非 contribution 呈现，明确说明这是不同方差来源的比较。\n\n**W6 [MAJOR] — Dev→Test 20pp drop 的解释不够充分。**\n\nTable 9 显示 Ign-F1 从 dev ~45 降到 test ~25-28（约 18-20pp drop）。论文归因于 Re-DocRED test set 的 annotation density 是 dev 的 2.82×。\n\n- 2.82× 的 annotation density 差异确实会增加 recall 难度，但 20pp drop 的幅度仍然令人担忧。是否有 dev set overfitting 的可能？例如，hyperparameter tuning 和 model selection 都在 dev 上进行。\n- 14B RSFT 在 test 上低于 SFT 0.37pp（Table 9 注释），论文解释为 \"truncation rate\" 差异。但如果 RSFT 的优势在 test 上消失甚至反转，这是否意味着 RSFT 的 gain 不够 robust？\n- **建议**：报告 test set 上的完整 decoupling 分析（不仅是 Ign-F1），展示 dev 上观察到的 pattern 是否在 test 上 replicate。\n\n**W7 [MINOR] — 与 encoder baseline 的比较选择性呈现指标。**\n\nTable 12（Appendix）显示 encoder 方法（ATLOP、SAIS、DREEAM）的 Ign-F1 约 62，而 LLM 方法约 45，差距 16-18pp。论文在主文中主要强调 TP-only Evi-F1（>80%）和 EDCR 优势，未充分讨论这一巨大性能差距的含义。\n\n- 论文第 7 页最后一段提到 \"encoder methods achieve substantially higher extraction performance (Rel-F1 60-63 vs. our 45-56)\"，但将其归因于 \"architecture-specific optimization for the classification formulation\"，篇幅很少。\n- 对于 deployment 场景的用户，Ign-F1 45 vs 62 是一个实质性差距。论文应更充分讨论 LLM-based 方法何时值得这一性能牺牲。\n\n**W8 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比。**\n\nRelated Work（Section 2）讨论了 AutoRE (Xue et al., 2024)、GildRE、ReLLM 等 LLM-based 方法，但 Table 12 仅对比 encoder 方法。虽然这些方法可能不产 evidence，但至少可以在 Rel-F1 上直接比较。\n\n**W9 [MINOR] — 4B retrained checkpoint 的 dev performance 差距 0.35pp 可能影响 evidence tax 分析。**\n\nSection 4.1 提到原始 4B checkpoint 不可用，retrained version 的 dev Ign-F1 为 43.88 vs 原始 44.23（差 0.35pp）。0.35pp 虽然看似小，但论文在 evidence tax 分析中关注的差异也在 0.25-0.47pp 量级（Section 4.4, Appendix E），这意味着 checkpoint 差异可能与被分析的效应大小可比。\n\n---\n\n### Questions（需要作者澄清）\n\n**Q1.** Cross-method EDCR 相关性 (ρ=−0.89, n=7) 中，移除 GRPO QLoRA collapse 的极端数据点后，ρ 和 p-value 变为多少？\n\n**Q2.** RSFT variance 声明中的 \"4.6–31×\" 区间对应哪些具体 scale？请提供每个 scale 的 SFT std 和 RSFT std 的 95% CI（基于 χ² 分布）。\n\n**Q3.** DPO 3-epoch 的 \"earlier evaluation protocol\" 与当前 protocol 的具体差异是什么？是 max_new_tokens、format-compliant intersection 筛选规则、还是其他？\n\n**Q4.** 关于 evidence tax（Section 4.4, Appendix E）：Qwen3-1.7B 的 training-time evidence tax（约 −5.19±5.25pp）方差极大——这是否意味着 evidence tax 的 direction 在 1.7B 上也不稳定？\n\n**Q5.** CED 的减法公式 (p⁺ − max p⁻_j) 是否尝试过其他组合方式（ratio、log-ratio、learned combination）？如何确定减法是最佳选择？\n\n**Q6.** Table 2 中 GRPO bf16 G=4 和 G=8 的 Rel-F1 分别是多少？论文是否可以明确隔离 group size vs precision 对 collapse 的独立贡献？\n\n---\n\n### Missing References\n\n- 未发现明显遗漏的关键引用。Related Work 覆盖了 DocRE（DocRED, ATLOP, DREEAM）、LLM-based IE（AutoRE, GildRE）、RL alignment（GRPO, DPO, RAFT）、evidence faithfulness（StAR）等主要线索。\n- 可考虑引用 Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\" 作为 LLM-based RE 的综述性参考（如未引用）。\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 论文提出了有价值的分析框架（evidence tax、decoupling spectrum、EDCR），实验覆盖面广，但核心统计声明（variance compression、EDCR correlation）的推断基础薄弱，需要加固。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法（CED、RSFT）合理，但多处统计推断基础薄弱：n=3 的 variance claim、EDCR shared-component、CED 增量价值不足。方法假设总体成立但验证不够严格 |\n| Excitement | 3.5/5 | Evidence tax 和 decoupling spectrum 概念有新意且对社区有启发价值；RSFT 本身是标准 rejection sampling，方法创新有限；分析型贡献 > 方法型贡献 |\n| Reproducibility | 4/5 | Hyperparameters 详尽（Table 4, Appendix A），数据集公开（DocRED），CED 依赖外部 NLI model（DeBERTa-v3-large）有明确说明。代码承诺开源。唯一扣分：CED scoring 需要特定 NLI model 的 prompt 格式细节 |\n| Confidence | 4/5 | Quite sure. 论文的核心领域（DocRE、LLM fine-tuning、RL alignment）在我的专业范围内，统计方法论的问题是明确可判断的 |\n\n### 最终判断\n\n本文的分析视角（evidence 不是 free lunch，优化范式决定 decoupling 程度）对 LLM-based IE 社区有实质价值。但三个核心贡献中：\n1. **Evidence tax**（扎实）——scale-dependent 的发现有 cross-family 验证支撑\n2. **Decoupling spectrum + EDCR**（中等）——概念好但 EDCR 的统计验证有结构性缺陷\n3. **Variance compression**（薄弱）——n=3 的统计基础无法支撑量化声明\n\n如果 W1（variance claim 的统计基础）和 W2（EDCR shared-component）能得到实质性回应（如增加 seeds、提供 partial correlation），可上调至 4.0（Conference）。目前判断为 3.5（Borderline Conference），主要因为统计方法论的不足削弱了本应很强的 empirical story。",
    "reviewer_id": "1",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-23T00:57:45.504030+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3824
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-23T00:57:50.082852+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-23T00:57:50.133582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-23T00:57:54.190020+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-23T00:57:54.240934+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 110 · 2026-05-23T00:58:01.528096+00:00_

审稿完成。核心判断：

- **Overall 3.5（Borderline Conference）**
- 2 个 CRITICAL 问题：n=3 的方差压缩声明统计基础不足（W1）；EDCR 指标存在 shared-component 机械性负相关（W2）
- 3 个 MAJOR 问题：CED contrastive 增量仅 0.02pp（W3）；DPO 3-epoch 用不同 evaluation protocol 影响 spectrum 可比性（W4）；SFT vs RSFT variance 测量不同来源（W5）
- 如果 W1+W2 能实质性回应（增加 seeds、提供 partial correlation），可上调至 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---

## Round 4

20 recorded events

### User

_source line 111 · 2026-05-23T01:02:53.998696+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（新颖性 + 完整性）

### Summary
本文研究 LLM-based DocRE 中证据生成的代价（"evidence tax"），比较 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3 (1.7B/4B/8B/14B) 和 LLaMA-3.1-8B 上的表现。主要发现：evidence tax 是规模依赖的（1.7B 时证据有益，4B 近似中性），GRPO 导致灾难性抽取-证据解耦而 RSFT 通过离散选择避免解耦，RSFT 将训练方差压缩 4.6–31 倍。论文提出 CED 和 EDCR 作为分析工具。

### Strengths
S1. 系统性多因子实验设计——三种范式 × 四个规模 + cross-family + 两个数据集。
S2. CED 评分函数设计合理——contrastive formulation 区分"证据支持关系"和"仅实体共现"。
S3. RSFT 方差压缩具有实际价值——1.7B RSFT 超过 8B SFT，Cohen's d=2.58。
S4. 分析层次丰富——per-relation EDCR、训练动态可视化、定性案例分析。
S5. 写作质量高——"evidence tax" 概念清晰，decoupling spectrum 叙事框架清晰。

### Weaknesses
W1 [CRITICAL] — 方法论原创性不足。三个贡献均为经验观察：C1 是实验观察不是方法创新；C2（decoupling spectrum）反映 gradient-based vs selection-based 的已知差异，EDCR 定义简单；C3（RSFT）论文自己承认是 "well-established"。整体定位更接近 empirical study with analytical tools，对 EMNLP main conference 需要更强方法创新性。

W2 [MAJOR] — Scaling claim 数据基础偏弱。仅 4 个 Qwen3 规模点 + 1 个 LLaMA 点，不足以可靠区分 scaling pattern。不同规模数字是否来自同一 evaluation protocol 不够清晰。

W3 [MAJOR] — GRPO 崩溃分析缺乏机制深度。停留在现象描述，未连接 reward hacking 文献，未探讨缓解策略（不同 KL 系数、reward normalization），未分析 full-precision 避免 collapse 是否仅因精度差异。如果 collapse 仅在 QLoRA 设置下发生，"decoupling spectrum" 框架不够稳固。

W4 [MINOR] — Related Work 遗漏：LMRC (Li & Zhang, 2024)、RelPrior (Huang et al., 2025)、SummaC (Laban et al., 2022)、Rationale Verification for RE (Li et al., 2025)。

W5 [MINOR] — CED 对外部 NLI 模型的 sensitivity analysis 不足——未测试其他 NLI 模型家族，未分析 DocRE 领域的 OOD 行为。

W6 [MINOR] — Limitations 遗漏：DocRED 证据标注不完整对 CED/EDCR 的影响、三种方法的计算成本差异、仅评估 DocRE 一种 IE 任务。

### Overall: 3.0（Findings）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-23T01:03:20.842402+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
  "pages": "1-8",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
    "pages": "1-8",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-23T01:03:21.948980+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 543.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.8}], \"total_pages\": 17, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1106
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-23T01:03:25.514353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-23T01:03:25.867469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-23T01:03:26.724848+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-23T01:03:26.725210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-23T01:03:26.926806+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-23T01:03:27.329214+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-23T01:03:34.763398+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
  "pages": "10-13",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
    "pages": "10-13",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-23T01:03:35.267576+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 591.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.7}], \"total_pages\": 17, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-23T01:03:38.839266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-23T01:03:39.242937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-23T01:03:39.444857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-23T01:03:39.798551+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-23T01:05:35.684389+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1: 系统性多因子实验设计。**\n同意。三种范式 × 四个规模 + cross-family + 两个数据集的覆盖面在同类工作中较好。我在自己的审稿中也将此列为优势（R1-S3）。\n\n**[REBUT] R2-S2: CED 评分函数设计合理。**\n部分不同意。CED 的 contrastive 动机（区分真 evidence vs 仅 entity co-occurrence）在**概念**上合理，但 Appendix B 的消融结果（Table 5）显示 CED vs flat-NLI（仅用正向 p⁺）的 Rel-F1 差异仅 0.02pp（45.63 vs 45.61），在 3-seed noise level（std ≈ 0.09pp）之内。论文自己在 Section 3.4 末段承认 \"the contrastive formulation is not essential for data selection quality\"。因此 R2 将 CED 的 contrastive formulation 列为 strength 过于宽松——这更接近一个**未被验证有实质增量的设计选择**。\n\n**[REBUT] R2-S3: RSFT 方差压缩具有实际价值。**\n强烈不同意将 Cohen's d=2.58 列为优势。这正是我 R1-W1 标注为 [CRITICAL] 的问题：\n\n- n=3 时方差估计的 95% CI 为 [0.52s, 6.29s]（基于 χ²(2) 分布），\"4.6–31× compression\" 和 d=2.58 在统计上不可靠\n- SFT 和 RSFT 测量的是不同来源的方差（R1-W5），直接比较不公平\n- \"1.7B RSFT 超过 8B SFT\" 这个 claim 有实际价值，但不应用 effect size 包装——直接报告均值差和 CI 更诚实\n\nR2 在自己的 Weakness 中未对此提出任何质疑，这是其审稿的一个盲区。\n\n**[AGREE] R2-S4: 分析层次丰富。**\n同意。Per-relation EDCR（Figure 4）、训练动态（Figure 3）和 qualitative analysis（Section M）从不同角度展示了 decoupling 现象。我在 R1-S5 也肯定了这一点。\n\n**[AGREE] R2-S5: 写作质量高。**\n同意。\"Evidence tax\" 概念和 decoupling spectrum 叙事框架确实清晰易懂，帮助读者快速抓住核心 message。\n\n---\n\n### Weaknesses 回应\n\n**[REBUT] R2-W1: 方法论原创性不足。**\n部分不同意。R2 的判断——\"三个贡献均为经验观察\"——有道理但过于笼统。需区分：\n\n1. **C1（Evidence tax）**：确实是 empirical observation，但 scale-dependent evidence tax 是一个有实际部署价值的发现，cross-family validation（LLaMA-3.1-8B，Appendix H-I）增强了其可信度。好的 empirical finding 在 EMNLP 有先例。\n2. **C2（Decoupling spectrum + EDCR）**：R2 说 \"反映 gradient-based vs selection-based 的已知差异\"——但这过度简化了。GRPO bf16 G=4 和 G=8 都避免 catastrophic collapse 而 QLoRA 不行（Table 2），这说明 decoupling 不是简单的 gradient vs selection 二分法，而是受 precision、capacity 等因素调制。这一观察是新的。EDCR 定义虽简单，但简单不等于无价值——问题是其统计验证不充分（我的 R1-W2）。\n3. **C3（RSFT）**：同意不是方法创新，论文也不应将其包装为创新。论文的贡献更准确地说是 RSFT **在 evidence-grounded DocRE 上的应用与分析**。\n\n总体判断：这篇论文更接近\"strong empirical study\"而非\"method paper\"。对于 EMNLP，如果 empirical findings 足够扎实且有 community impact，3.5-4.0 是合理分数。**但前提是统计基础要牢固——这恰恰是论文的短板**（R1-W1, R1-W2）。R2 把原创性不足标为 [CRITICAL]，我认为应为 [MAJOR]——真正 critical 的是统计方法论的薄弱。\n\n**[REBUT] R2-W2: Scaling claim 数据基础偏弱。**\n部分不同意。\n\n- 论文并未声称建立 scaling law（需要拟合幂律等参数模型），而是观察 scaling trend。4 个 Qwen3 点（1.7B/4B/8B/14B）+ LLaMA-3.1-8B 作为 cross-family validation，对于 trend observation 是合理的。\n- R2 说 \"不同规模数字是否来自同一 evaluation protocol 不够清晰\"——论文在 Section 4.1 和 Appendix C 说明了 matched@2048 fair evaluation protocol（max_new_tokens=2048, format-compliant intersection），并明确标注 DPO 3-epoch 使用了 earlier protocol（Footnote 1）。这个信息是存在的，虽然可以更显眼。\n- 真正的问题不是数据点数量，而是每个数据点只有 3 seeds，使得 scale 间的差异难以从噪声中区分（R1-W1）。\n\n**[AGREE] R2-W3: GRPO 崩溃分析缺乏机制深度。**\n同意这是一个实质性弱点，但补充两点：\n\n1. **精度 vs group size 的隔离实际上已部分完成**：Table 2 包含 GRPO bf16 G=4 和 GRPO bf16 G=8 两行，两者均避免 catastrophic collapse，而 QLoRA G=4 collapse。这隔离了 precision 作为 collapse 的主要因素。R2 称 \"未分析 full-precision 避免 collapse 是否仅因精度差异\" 不完全准确——数据在 Table 2 中，但**论文的文字分析确实停留在现象层面**，未深入探讨为什么 4-bit quantization 特别容易导致 reward hacking（例如，量化损失是否使 policy 更容易找到 degenerate shortcuts）。\n2. 同意缺乏 KL 系数消融和 reward normalization 测试。GRPO 的超参数空间很大（Table 4 显示仅测试了 G=4 和 G=8，β 值未报告消融），论文对此的 coverage 不足以支撑对 GRPO 的一般性结论。\n3. 但 R2 的推论——\"如果 collapse 仅在 QLoRA 下发生，decoupling spectrum 不够稳固\"——过于绝对。Table 2 的 GRPO bf16 行显示 **mild decoupling**（EDCR 低于 SFT baseline），只是程度不到 catastrophe。Spectrum 中 GRPO 仍然比 RSFT 有更多 decoupling，只是 severity 被 precision 调制。\n\n**[AGREE] R2-W4: Related Work 遗漏。**\n部分同意。SummaC (Laban et al., 2022) 作为 NLI-based faithfulness metric 的先驱，与 CED 的设计逻辑直接相关，应当引用。LMRC (Li & Zhang, 2024) 如果涉及 LLM-based RE，也应对比。其余两篇（RelPrior, Rationale Verification）需确认具体相关性。\n\n**[AGREE] R2-W5: CED 对外部 NLI 模型的 sensitivity analysis 不足。**\n同意。CED 依赖 DeBERTa-v3-large 的 NLI 输出。论文仅在 Appendix B 测试了 v3-base（Table 5 脚注 \"CED filtering is robust to NLI model capacity\"），但：\n\n- 仅测试了同一家族（DeBERTa）的两个大小，不算真正的 sensitivity analysis\n- DocRED 的 evidence 是 Wikipedia 段落的句子级引用，与标准 NLI 训练数据（如 MNLI）有领域差异，OOD 行为未被分析\n- 这对 CED 的实用性主张（Section 6 \"CED as a domain-specific quality filter\"）是一个实际威胁\n\n**[AGREE] R2-W6: Limitations 遗漏。**\n同意所有三点遗漏应在 Limitations 中讨论：\n\n1. **DocRED 证据标注不完整**：已知 DocRED 的 evidence annotation 不完整（部分 triple 缺少标注或标注不全）。CED 计算负例时依赖 \"not in the predicted evidence set\" 的句子，如果 gold evidence 本身不完整，negative samples 可能包含实际为正的 evidence，影响 CED 分数的可靠性。\n2. **计算成本差异**：Table 4 显示 RSFT 训练样本约 3000（1.7B），远少于 GRPO（3,053 documents × N=5 candidates = ~15K），但 RSFT 还需 SFT inference + NLI scoring 的前置成本，论文未报告端到端 wall-clock time 对比。\n3. **仅 DocRE 一种 IE 任务**：evidence grounding 的 insight 是否迁移到 NER、EE 等其他 IE 任务未被讨论。\n\n---\n\n### 对 R2 Overall Assessment（3.0, Findings）的评价\n\nR2 给 3.0 的主要依据是方法论原创性不足（R2-W1）。我认为这一判断方向正确但不是论文的最大问题——**统计方法论的薄弱**（n=3 variance claims、EDCR shared-component）才是更实质的 concern，而 R2 在这方面未做深入分析（甚至将 Cohen's d=2.58 列为 strength）。\n\n我的评分 3.5（Borderline Conference），高于 R2 的 3.0，理由是：\n- 论文的分析框架（evidence tax、decoupling spectrum）对社区有启发价值，即使不是严格的方法创新\n- 跨尺度 + 跨 model family 的实验覆盖在同类工作中属上乘\n- 但统计基础的问题阻止我给 4.0\n\n如果作者能回应 R1-W1（增加 seeds 或降级 variance claim）和 R1-W2（EDCR shared-component 的 partial correlation 分析），我愿意上调至 4.0。R2 关注的原创性问题在 rebuttal 中较难根本解决，但如果统计基础加固，empirical study 的定位可以更有说服力。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1: 系统性多因子实验设计。**\n同意。三种范式 × 四个规模 + cross-family + 两个数据集的覆盖面在同类工作中较好。我在自己的审稿中也将此列为优势（R1-S3）。\n\n**[REBUT] R2-S2: CED 评分函数设计合理。**\n部分不同意。CED 的 contrastive 动机（区分真 evidence vs 仅 entity co-occurrence）在**概念**上合理，但 Appendix B 的消融结果（Table 5）显示 CED vs flat-NLI（仅用正向 p⁺）的 Rel-F1 差异仅 0.02pp（45.63 vs 45.61），在 3-seed noise level（std ≈ 0.09pp）之内。论文自己在 Section 3.4 末段承认 \"the contrastive formulation is not essential for data selection quality\"。因此 R2 将 CED 的 contrastive formulation 列为 strength 过于宽松——这更接近一个**未被验证有实质增量的设计选择**。\n\n**[REBUT] R2-S3: RSFT 方差压缩具有实际价值。**\n强烈不同意将 Cohen's d=2.58 列为优势。这正是我 R1-W1 标注为 [CRITICAL] 的问题：\n\n- n=3 时方差估计的 95% CI 为 [0.52s, 6.29s]（基于 χ²(2) 分布），\"4.6–31× compression\" 和 d=2.58 在统计上不可靠\n- SFT 和 RSFT 测量的是不同来源的方差（R1-W5），直接比较不公平\n- \"1.7B RSFT 超过 8B SFT\" 这个 claim 有实际价值，但不应用 effect size 包装——直接报告均值差和 CI 更诚实\n\nR2 在自己的 Weakness 中未对此提出任何质疑，这是其审稿的一个盲区。\n\n**[AGREE] R2-S4: 分析层次丰富。**\n同意。Per-relation EDCR（Figure 4）、训练动态（Figure 3）和 qualitative analysis（Section M）从不同角度展示了 decoupling 现象。我在 R1-S5 也肯定了这一点。\n\n**[AGREE] R2-S5: 写作质量高。**\n同意。\"Evidence tax\" 概念和 decoupling spectrum 叙事框架确实清晰易懂，帮助读者快速抓住核心 message。\n\n---\n\n### Weaknesses 回应\n\n**[REBUT] R2-W1: 方法论原创性不足。**\n部分不同意。R2 的判断——\"三个贡献均为经验观察\"——有道理但过于笼统。需区分：\n\n1. **C1（Evidence tax）**：确实是 empirical observation，但 scale-dependent evidence tax 是一个有实际部署价值的发现，cross-family validation（LLaMA-3.1-8B，Appendix H-I）增强了其可信度。好的 empirical finding 在 EMNLP 有先例。\n2. **C2（Decoupling spectrum + EDCR）**：R2 说 \"反映 gradient-based vs selection-based 的已知差异\"——但这过度简化了。GRPO bf16 G=4 和 G=8 都避免 catastrophic collapse 而 QLoRA 不行（Table 2），这说明 decoupling 不是简单的 gradient vs selection 二分法，而是受 precision、capacity 等因素调制。这一观察是新的。EDCR 定义虽简单，但简单不等于无价值——问题是其统计验证不充分（我的 R1-W2）。\n3. **C3（RSFT）**：同意不是方法创新，论文也不应将其包装为创新。论文的贡献更准确地说是 RSFT **在 evidence-grounded DocRE 上的应用与分析**。\n\n总体判断：这篇论文更接近\"strong empirical study\"而非\"method paper\"。对于 EMNLP，如果 empirical findings 足够扎实且有 community impact，3.5-4.0 是合理分数。**但前提是统计基础要牢固——这恰恰是论文的短板**（R1-W1, R1-W2）。R2 把原创性不足标为 [CRITICAL]，我认为应为 [MAJOR]——真正 critical 的是统计方法论的薄弱。\n\n**[REBUT] R2-W2: Scaling claim 数据基础偏弱。**\n部分不同意。\n\n- 论文并未声称建立 scaling law（需要拟合幂律等参数模型），而是观察 scaling trend。4 个 Qwen3 点（1.7B/4B/8B/14B）+ LLaMA-3.1-8B 作为 cross-family validation，对于 trend observation 是合理的。\n- R2 说 \"不同规模数字是否来自同一 evaluation protocol 不够清晰\"——论文在 Section 4.1 和 Appendix C 说明了 matched@2048 fair evaluation protocol（max_new_tokens=2048, format-compliant intersection），并明确标注 DPO 3-epoch 使用了 earlier protocol（Footnote 1）。这个信息是存在的，虽然可以更显眼。\n- 真正的问题不是数据点数量，而是每个数据点只有 3 seeds，使得 scale 间的差异难以从噪声中区分（R1-W1）。\n\n**[AGREE] R2-W3: GRPO 崩溃分析缺乏机制深度。**\n同意这是一个实质性弱点，但补充两点：\n\n1. **精度 vs group size 的隔离实际上已部分完成**：Table 2 包含 GRPO bf16 G=4 和 GRPO bf16 G=8 两行，两者均避免 catastrophic collapse，而 QLoRA G=4 collapse。这隔离了 precision 作为 collapse 的主要因素。R2 称 \"未分析 full-precision 避免 collapse 是否仅因精度差异\" 不完全准确——数据在 Table 2 中，但**论文的文字分析确实停留在现象层面**，未深入探讨为什么 4-bit quantization 特别容易导致 reward hacking（例如，量化损失是否使 policy 更容易找到 degenerate shortcuts）。\n2. 同意缺乏 KL 系数消融和 reward normalization 测试。GRPO 的超参数空间很大（Table 4 显示仅测试了 G=4 和 G=8，β 值未报告消融），论文对此的 coverage 不足以支撑对 GRPO 的一般性结论。\n3. 但 R2 的推论——\"如果 collapse 仅在 QLoRA 下发生，decoupling spectrum 不够稳固\"——过于绝对。Table 2 的 GRPO bf16 行显示 **mild decoupling**（EDCR 低于 SFT baseline），只是程度不到 catastrophe。Spectrum 中 GRPO 仍然比 RSFT 有更多 decoupling，只是 severity 被 precision 调制。\n\n**[AGREE] R2-W4: Related Work 遗漏。**\n部分同意。SummaC (Laban et al., 2022) 作为 NLI-based faithfulness metric 的先驱，与 CED 的设计逻辑直接相关，应当引用。LMRC (Li & Zhang, 2024) 如果涉及 LLM-based RE，也应对比。其余两篇（RelPrior, Rationale Verification）需确认具体相关性。\n\n**[AGREE] R2-W5: CED 对外部 NLI 模型的 sensitivity analysis 不足。**\n同意。CED 依赖 DeBERTa-v3-large 的 NLI 输出。论文仅在 Appendix B 测试了 v3-base（Table 5 脚注 \"CED filtering is robust to NLI model capacity\"），但：\n\n- 仅测试了同一家族（DeBERTa）的两个大小，不算真正的 sensitivity analysis\n- DocRED 的 evidence 是 Wikipedia 段落的句子级引用，与标准 NLI 训练数据（如 MNLI）有领域差异，OOD 行为未被分析\n- 这对 CED 的实用性主张（Section 6 \"CED as a domain-specific quality filter\"）是一个实际威胁\n\n**[AGREE] R2-W6: Limitations 遗漏。**\n同意所有三点遗漏应在 Limitations 中讨论：\n\n1. **DocRED 证据标注不完整**：已知 DocRED 的 evidence annotation 不完整（部分 triple 缺少标注或标注不全）。CED 计算负例时依赖 \"not in the predicted evidence set\" 的句子，如果 gold evidence 本身不完整，negative samples 可能包含实际为正的 evidence，影响 CED 分数的可靠性。\n2. **计算成本差异**：Table 4 显示 RSFT 训练样本约 3000（1.7B），远少于 GRPO（3,053 documents × N=5 candidates = ~15K），但 RSFT 还需 SFT inference + NLI scoring 的前置成本，论文未报告端到端 wall-clock time 对比。\n3. **仅 DocRE 一种 IE 任务**：evidence grounding 的 insight 是否迁移到 NER、EE 等其他 IE 任务未被讨论。\n\n---\n\n### 对 R2 Overall Assessment（3.0, Findings）的评价\n\nR2 给 3.0 的主要依据是方法论原创性不足（R2-W1）。我认为这一判断方向正确但不是论文的最大问题——**统计方法论的薄弱**（n=3 variance claims、EDCR shared-component）才是更实质的 concern，而 R2 在这方面未做深入分析（甚至将 Cohen's d=2.58 列为 strength）。\n\n我的评分 3.5（Borderline Conference），高于 R2 的 3.0，理由是：\n- 论文的分析框架（evidence tax、decoupling spectrum）对社区有启发价值，即使不是严格的方法创新\n- 跨尺度 + 跨 model family 的实验覆盖在同类工作中属上乘\n- 但统计基础的问题阻止我给 4.0\n\n如果作者能回应 R1-W1（增加 seeds 或降级 variance claim）和 R1-W2（EDCR shared-component 的 partial correlation 分析），我愿意上调至 4.0。R2 关注的原创性问题在 rebuttal 中较难根本解决，但如果统计基础加固，empirical study 的定位可以更有说服力。",
    "reviewer_id": "1",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-23T01:05:39.400517+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3716
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-23T01:05:47.719614+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-23T01:05:47.770370+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 130 · 2026-05-23T01:05:56.981221+00:00_

逐条回应已提交给 Director。核心立场：

- **R2-S2（CED 设计合理）和 R2-S3（variance compression 价值）**被反驳——CED contrastive 组件仅贡献 0.02pp（Appendix B），Cohen's d=2.58 基于 n=3 不可靠
- **R2-W1（原创性不足）**部分反驳——真正 critical 的不是原创性而是统计方法论薄弱，R2 在这方面存在盲区
- **R2-W3（GRPO 分析缺深度）**同意但补充：Table 2 实际已隔离 precision vs group size，只是文字分析停留在现象层面
- 维持 3.5 评分，高于 R2 的 3.0，因为分析框架有社区价值，但受限于统计基础

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---

## Round 5

110 recorded events

### User

_source line 131 · 2026-05-24T22:53:24.151718+00:00_

[Round 3 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计声明**。

## 论文信息
- 标题：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction
- 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf`

## Venue 要求（EMNLP 2026 通过 ARR）
- 正文 ≤ 8 页 + 无限参考文献
- Limitations 必填（≤1 页，不计入页数限制）
- Double-blind 匿名审稿
- ACL 模板（`\usepackage[review]{acl}`）
- Long/Short 走同一审稿系统
- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重
1. **EDCR 指标有效性**：EDCR 与 Rel-F1 共享 TP 组分，cross-method ρ 是否有 mechanical correlation 问题？partial correlation 是否充分控制了 shared component？per-relation 分析（n=76）是否足够独立？permutation test 是否令人信服？
2. **Variance compression 统计可靠性**：n=3 seeds 下的方差压缩声明——χ² CI、Cohen's d、sign test 是否足够支撑"consistently reduces"的结论？95% CI 宽度是否令人担忧？
3. **Evidence tax 因果推断**：1.7B evidence tax 为负（beneficial）——implicit regularization 假说是否有足够证据？matched@2048 fair subset 方法是否充分控制了 confounds？4B/8B near-neutral tax 的 n=3 是否足以排除噪声？
4. **GRPO/DPO 实验设计**：GRPO 只测了 KL=0.01，DPO 只测了 β=0.1——hyperparameter exploration 是否充分？QLoRA vs bf16 的 confound（quantization precision vs group size）是否充分隔离？DPO checkpoint 重建是否引入了方法论问题？
5. **RSFT 机制解释**：paper 称 discrete selection "cannot exploit the trade-off"——这是结构性论证还是需要实证验证？random selection baseline（41.14 vs 44.66）能否证明 CED scoring 而非 selection 本身驱动改进？
6. **Test set evaluation**：~20pp dev-test gap 归因于 annotation density（2.82×）——是否令人信服？14B RSFT test 出现 reversal（Δ=-0.37pp）——如何解释？

请完整阅读论文（main.tex 所有 sections + appendix），给出结构化审稿意见（Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment + 置信度 + 分数）。对每个 Weakness 标注严重程度（CRITICAL / MAJOR / MINOR）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-24T22:53:39.213964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-24T22:53:39.315507+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-24T22:53:49.317443+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-24T22:53:49.490135+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 172
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-24T22:53:59.752067+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/*review*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-24T22:53:59.902968+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-24T22:54:09.688446+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*.md",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/*.md",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-24T22:54:10.246835+00:00_

/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/dependencies.md
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/SKILL.md
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/other-tools.md
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/streaming.md
/home/ubuntu/agent-ml-research/skills/global/academic-writer.skill.md
/home/ubuntu/agent-ml-research/skills/global/code-survey.skill.md
/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md
/home/ubuntu/agent-ml-research/skills/global/dataset-discovery.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-reviewer-synthesis.skill.md
/home/ubuntu/agent-ml-research/skills/global/data-snapshot.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-key.skill.md
/home/ubuntu/agent-ml-research/skills/global/distill-session.skill.md
/home/ubuntu/agent-ml-research/skills/global/elastic-gpu.skill.md
/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md
/home/ubuntu/agent-ml-research/skills/global/first-project-entry.skill.md
/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-generation.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-proposal.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-cloud-rental.skill.md
/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-claude-pool.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md
/home/ubuntu/agent-ml-research/skills/global/novelty-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/narrative-animation.skill.md
/home/ubuntu/agent-ml-research/
…[truncated 4494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 558
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-24T22:54:20.186758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-24T22:54:20.251670+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 64
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-24T22:54:26.083943+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-24T22:54:26.134712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-24T22:54:30.859785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-24T22:54:32.833569+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
  "pages": "1-8",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
    "pages": "1-8",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-24T22:54:33.485918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-24T22:54:39.768506+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here is information about ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Reviewer Responsibilities and Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements. The ARR peer review guidelines are a work-in-progress and will be updated as ARR evolves. Before starting an a
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8908
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-24T22:54:41.131947+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 620.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.9}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8298
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-24T22:54:41.132495+00:00_

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
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7646
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-24T22:54:45.907965+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form soundness excitement overall assessment scoring rubric 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form soundness excitement overall assessment scoring rubric 2025"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-24T22:54:46.309735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-24T22:54:49.224969+00:00_

1	\begin{abstract}
2	Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, creating a gap between extraction performance and output verifiability. We formalize evidence-grounded DocRE as structured generation and compare Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax---extraction cost of generating evidence---is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with Natural Language Inference (NLI)-based scoring avoids decoupling entirely through output filtering rather than gradient pressure. RSFT consistently reduces training seed variance (complete pairwise seed separation on LLaMA, Cohen's $d{=}2.58$; non-overlapping $\chi^2$ confidence intervals at 1.7B). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all evaluated scales (Spearman $\rho{=}1.0$).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2915
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-24T22:54:49.375977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-24T22:54:49.426764+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	Without evidence, a clinician reviewing a ten-page case report must manually locate the sentences that support each extracted drug interaction---a bottleneck that undermines trust in automated extraction.
7	
8	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
9	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
10	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
11	
12	This gap reflects a structural difference.
13	In encoder methods, evidence retrieval is classification that regularizes the encoder at negligible cost; in LLM-based DocRE, evidence requires the model to \emph{generate} additional output tokens per triple, increasing output length and decoding complexity.
14	The na\"{i}ve expectation is that this generation cost always harms extraction accuracy.
15	Our experiments show this expectation is wrong.
16	The evidence tax is not a fixed penalt
…[truncated 2313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-24T22:54:49.527676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-24T22:54:49.542902+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Document-Level Relation Extraction}
5	\label{sec:rw_docre}
6	
7	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
8	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
9	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding with localized context pooling, and graph-based methods such as GAIN \citep{zeng2020gain} model inter-sentence reasoning through heterogeneous mention-level and entity-level graphs.
10	
11	A parallel thread incorporates sentence-level evidence into these architectures.
12	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
13	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
14	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
15	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
16	
17	Recent work has recast DocRE for large language models.
18	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge
…[truncated 4295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 15
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-24T22:54:49.543332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-24T22:54:49.551988+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
7	\vspace{-2mm}
8	\caption{Evidence-grounded DocRE produces relation triples with supporting sentence indices, unlike standard DocRE which outputs bare triples. RSFT selects the top-$k$ of $N$ CED-scored candidates per document for fine-tuning.}
9	\label{fig:overview}
10	\end{figure*}
11	
12	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
13	\label{sec:task}
14	
15	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
16	
17	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sent
…[truncated 9504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-24T22:54:49.559640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-24T22:54:49.611220+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate on DocRED~\citep{yao2019docred} (3,053 training / 998 dev documents, 96 relation types) with Re-DocRED~\citep{tan2022redocred} for cross-dataset validation. Our primary model is Qwen3-4B; we also train Qwen3-1.7B, 8B, and 14B to study scale effects, with LLaMA-3.1-8B for cross-family validation. All models use LoRA~\citep{hu2022lora} ($r{=}64$, $\alpha{=}128$) with structured output jointly producing triples and evidence. RSFT selects the top-$k{=}1$ of $N{=}8$ samples by CED score (\S\ref{sec:ced}); GRPO uses group sizes $G{=}4$ (QLoRA) and $G{=}8$ (bf16); DPO constructs preference pairs from CED-ranked outputs. We report Ign-F1 (primary; ignores training-set triples), Rel-F1, Evi-F1 (TP-only and joint per DREEAM protocol~\citep{ma2023dreeam}), and EDCR (\S\ref{sec:edcr}). Detailed hyperparameters appear in the Appendix.
8	
9	
10	\subsection{Main Results}
11	\label{sec:main_results}
12	
13	Table~\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.
14	
15	RSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\ 79.61) and coupling tightens (EDCR 0.6487 vs.\ 0.6797). Per-seed results appear in Appendix~\ref{sec:ablation_full}.
16	
17	\begin{table}[t]
18	\centering
19	\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\pm$ std$^{(\text{seeds})}$; other metrics are same-seed means. Best \textbf{bold}; best evidence-generating \underline{underlined}. Per-seed: Appendix~\ref{tab:ablation_full}.}
20	\label{tab:main}
21	\small
22	\resiz
…[truncated 9856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-24T22:54:49.611678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-24T22:54:49.690404+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task and compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax is not a fixed penalty but a landscape shaped by capacity, optimization paradigm, and data quality filtering.
5	RSFT improves mean extraction across all tested scales and reduces training variance at every evaluated configuration; a 1.7B RSFT model approaches 8B SFT performance at 4.7$\times$ fewer parameters. Future work should investigate targeted evidence rewards during gradient-based training and extend evaluation to non-Wikipedia domains.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 78
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-24T22:54:49.690903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-24T22:54:50.161176+00:00_

1	\section{Limitations}
2	
3	\paragraph{Data and architecture scope.}
4	We evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia; cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia, a limitation shared by all prior evidence-aware work (SAIS, DREEAM, EIDER).
5	Evidence tax patterns span two model families (Qwen3, LLaMA) with single hyperparameter settings per RL method; other architectures, scales beyond 14B, or alternative KL coefficients may produce different decoupling behaviors.
6	
7	\paragraph{CED scoring sensitivity.}
8	CED scoring operates at the document level using an external NLI model (DeBERTa-v3); sensitivity to other NLI model families is unexplored, and sentence-level CED filtering disrupts co-reference chains (Evi-F1 $-$7.7pp).
9	
10	\paragraph{RSFT mechanistic explanation.}
11	Our explanation for why RSFT avoids decoupling---that discrete selection cannot exploit the extraction--evidence trade-off---is structural rather than empirical. We have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both. Disentangling these factors would require controlled experiments with fixed training data quality but varied selection mechanisms.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 470
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-24T22:54:50.161570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-24T22:54:50.413503+00:00_

1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B with LoRA. A dash indicates non-applicable parameters. \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (\S\ref{sec:spectrum}).}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{l@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	\multicolumn{6}{l}{\textit{Model \& Adapter}} \\
16	\quad LoRA rank $r$ / $\alpha$ & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 \\
17	\quad Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
18	\midrule
19	\multicolumn{6}{l}{\textit{Optimization}} \\
20	\quad Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
21	\quad Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
22	\quad Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	\quad Epochs / Max steps & 3 / -- & 3 / -- & -- / 100 & -- / 100 & 1, 3\textsuperscript{$\star$} / -- \\
24	\midrule
25	\multicolumn{6}{l}{\textit{RL / Selection}} \\
26	\quad Group size $G$ & -- & -- & 4 & 8 & -- \\
27	\quad KL coeff.\ / $\beta$ & -- & -- & 0.01 & 0.01 & 0.1 \\
28	\quad Candidates $N$ / Top-$k$ & -- & 8 / 1 & -- & -- & 8 / -- \\
29	\midrule
30	\multicolumn{6}{l}{\textit{Data}} \\
31	\quad Max new tokens & 1024 & 1024 & 1024 &
…[truncated 40825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-24T22:54:55.684463+00:00_

Web search results for query: "ACL Rolling Review review form soundness excitement overall assessment scoring rubric 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) review form scoring system for 2025:

## Three-Score System (February 2025 onwards)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

The soundness score evaluates whether the paper is 
…[truncated 1172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9776
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-24T22:55:01.359771+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-24T22:55:01.398294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 38
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-24T22:55:03.312793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-24T22:55:04.119452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-24T22:55:04.320688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-24T22:55:04.779457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-24T22:55:05.136268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 815
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-24T22:55:05.136853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-24T22:55:06.145322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1365
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-24T22:55:06.196434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-24T22:55:06.653417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-24T22:55:07.008131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1871
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-24T22:55:07.210422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-24T22:55:07.616415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-24T22:55:08.525609+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2329
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-24T22:55:09.684311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3030
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-24T22:55:09.842921+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2226
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-24T22:55:09.995752+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2785
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-24T22:55:18.329633+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form scoring rubric. I need the exact scoring scales for: 1) Soundness (what each score 1-5 means), 2) Excitement (what each score 1-5 means), 3) Overall Assessment (what each score 1-5 means), 4) Any other scored dimensions like Reproducibility, Confidence, etc. Give me the full text of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form scoring rubric. I need the exact scoring scales for: 1) Soundness (what each score 1-5 means), 2) Excitement (what each score 1-5 means), 3) Overall Assessment (what each score 1-5 means), 4) Any other scored dimensions like Reproducibility, Confidence, etc. Give me the full text of each score level."
  }
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-24T22:55:20.390525+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
  "pages": "9-19",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
    "pages": "9-19",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-24T22:55:29.293397+00:00_

# ACL Rolling Review Form Scoring Rubrics

## 1) Soundness

- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 2) Excitement

- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others and/or attend if time permits."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 3) Overall Assessment

- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4**: "Conference: I think this paper could be accepted to an ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1**: "Do not resubmit: This paper has to be fully redone, or it is not relevant."

## 4) Reviewer Confidence

- **5**: "Positive that my evaluation is correct. I read the paper very carefully."
- **4**: "Quite sure. It's unlikely, though conceivable, that I missed something."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed details."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is an educated guess."

## 5) Reproducibility

- **5**: "They could easily reproduce the results."
- **4**: "They
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10963
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-24T22:55:31.402948+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.0}, {\"
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 11012
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-24T22:55:35.427894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-24T22:55:36.231029+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-24T22:55:36.231475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-24T22:55:36.733372+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-24T22:55:36.733716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-24T22:55:36.784129+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-24T22:55:37.187427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-24T22:55:38.143564+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-24T22:55:38.244513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-24T22:55:38.645942+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-24T22:55:38.646313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-24T22:55:39.097930+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-24T22:55:39.098325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-24T22:55:39.549989+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-24T22:55:39.550407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-24T22:55:40.503681+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-24T22:55:40.654787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-24T22:55:40.957032+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-24T22:55:40.957479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-24T22:55:41.108164+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-24T22:55:41.309255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-24T22:55:41.410069+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-24T22:55:46.080401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if PDF images directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if PDF images directory exists"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-24T22:55:46.331457+00:00_

DIR_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-24T22:55:51.207258+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
  "pages": "9-19",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
    "pages": "9-19",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-24T22:55:52.512627+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.0}, {\"
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1305
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-24T22:55:55.223385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-24T22:55:55.629445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-24T22:55:56.536507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-24T22:55:56.537560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-24T22:55:56.538072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 221 · 2026-05-24T22:55:57.041627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-24T22:55:57.496221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-24T22:55:57.496732+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-24T22:55:57.949863+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-24T22:55:57.950330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-24T22:55:58.904917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-24T22:55:58.905981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-24T22:55:58.956476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-24T22:55:59.458370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-24T22:55:59.910593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-24T22:55:59.911032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-24T22:56:00.366799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-24T22:56:00.367661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-24T22:56:01.123167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1212
}
```

</details>

---

### Tool call

_source line 235 · 2026-05-24T22:56:01.123629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-24T22:56:01.225094+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-24T22:56:01.577859+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-24T23:01:23.874546+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见 — Round 3 (方法严谨性 + 实验设计 + 统计声明)\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026 via ARR\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 系统性实验设计和新颖观察（scale-dependent evidence tax, decoupling spectrum）是有价值的贡献，但多个核心声明的统计证据不足（n=3 方差、单 seed 税率、GRPO 混淆变量），且 14B test reversal 削弱了泛化性论述。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有方向性支持但统计证据薄弱：方差压缩 n=3 + CI 重叠 3/4 scales；evidence tax threshold 依赖 n=1 seeds；GRPO 实验存在未隔离的混淆变量 |\n| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 是有趣的新观察；但实际影响受限于 Wikipedia-only 数据集和 RSFT 对 evidence quality 无改善 |\n| Reproducibility | 4/5 | Appendix 详尽（hyperparameters, per-seed results, error analysis），但 CED 实现细节（hypothesis verbalization template）未完整给出 |\n| Confidence | 4/5 | 我仔细阅读了全文及附录，此领域在我的专业范围内 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [CRITICAL] GRPO QLoRA vs bf16 实验存在未隔离的混淆变量\n\n- 具体位置：Section 4.3, Table 13 (Appendix I)\n- 问题：Paper 将 GRPO catastrophic collapse 归因于 \"quantization precision rather than group size as the primary factor\"（Section 4.3），但两个配置同时改变了 **两个** 变量：quantization（NF4 4-bit vs bf16）**和** group size（G=4 vs G=8）。没有控制实验（QLoRA G=8 或 bf16 G=4）来隔离这两个因素。\n- 为什么影响接收：Decoupling spectrum 是本文核心贡献之一。如果 catastrophic collapse 是由 G=4（过小的 group size 导致高 variance advantage estimates）而非 quantization 造成的，则整个 \"quantization-constrained precision\" 叙事需要修改。Paper 引用了 \\citet{li2026qurl} 的 quantized-actor divergence 来支持 quantization 解释，但这是一个没有控制实验支撑的类比。\n- 建议修改方向：（1）增加 bf16 G=4 实验以隔离 group size 效应；或（2）将结论从 \"quantization precision...as the primary factor\" 降级为 \"quantization and/or group size\"，承认无法区分两个因素。\n\n**N2** [CRITICAL] 方差压缩声明的统计证据不足（n=3 seeds）\n\n- 具体位置：Section 4.4, Table 6 (Appendix D), Abstract\n- 问题：\n  - 4/4 scales 中仅 1.7B 的 χ² CI 不重叠（SFT lower 1.45 > RSFT upper 0.54）。其余 3 个 scale 的 CI 均重叠。\n  - Sign test p=0.0625（one-sided），不满足 α=0.05 显著性水平。Paper 自己说 \"underpowered\"。\n  - Cohen's d 在 4B 仅为 0.46（small effect）。\n  - Abstract 中 \"consistently reduces training seed variance\" 和 \"complete pairwise seed separation on LLaMA, Cohen's d=2.58; non-overlapping χ² confidence intervals at 1.7B\" 选择性报告了最强结果（cherry-picking）。\n- 为什么影响接收：这是本文三大 contribution 之一。\"Consistently reduces\" 在统计上不成立——方向一致但缺乏统计显著性。n=3 的 χ² CI 宽度极大（例如 SFT 4B: [1.98, 23.89]），几乎没有 discriminative power。\n- 建议修改方向：（1）将 \"consistently reduces\" 改为 \"shows a consistent directional pattern with statistical significance only at the 1.7B scale\"；（2）Abstract 中展示全景而非选择最强结果；（3）增加 seeds 数量（至少 n=5）以获得有意义的 CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [MAJOR] Evidence tax 因果推断——implicit regularization 假说证据不足\n\n- 具体位置：Section 4.4, Appendix E (Table 7), Introduction\n- 问题：1.7B evidence tax 为负（-5.63pp），paper 提出 \"implicit regularization hypothesis\"——evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition。但 Table 16 (Appendix N) 显示 1.7B with-evidence 模型只生成 25.5k predictions vs no-evidence 的 44.6k（1.75×差异）。这意味着有一个更简单的替代解释：evidence 格式使每个 triple 的 output 更长，从而限制了总 prediction 数量，机械性地减少了 duplication 和 FP，提高了 precision-heavy 指标（Ign-F1）。Paper 说 \"partly through halving output duplication\"（Introduction），但未量化这个 mechanical 效应与 \"真正的 regularization\" 效应的相对贡献。\n- 建议：（1）在 matched prediction count 条件下重新计算 evidence tax（例如，将 no-evidence 模型的 predictions 截断到与 evidence 模型相同的数量，再比较 Ign-F1）；（2）或者将 \"implicit regularization\" 降级为 \"output constraint effect\" 并明确承认无法区分因果机制。\n\n**W2** [MAJOR] GRPO/DPO 超参数探索不足\n\n- 具体位置：Section 3.3, Table 3 (Appendix A)\n- 问题：GRPO 只测试了 KL=0.01，DPO 只测试了 β=0.1。这些是默认值但可能不适合 evidence-grounded DocRE 的 multi-objective setting。DPO 1-epoch 的 Rel-F1 就已从 SFT 的 44.39 暴跌到 33.37（-11pp），这在 DPO 文献中是异常大的 degradation，更可能是 β 选择不当而非 DPO 的固有限制。如果 β=0.01 或 β=0.5 能维持更好的 extraction，则 \"DPO gradual degradation\" 的结论不成立。\n- 为什么重要：Decoupling spectrum（GRPO catastrophic → DPO gradual → RSFT none）是本文核心贡献。如果 GRPO/DPO 端是因为超参数选择不当而非方法论限制，则 spectrum 的概括性被严重削弱。\n- 建议：至少对 DPO β ∈ {0.01, 0.1, 0.5} 和 GRPO KL ∈ {0.001, 0.01, 0.1} 做 sensitivity analysis。\n\n**W3** [MAJOR] 14B test-set reversal 削弱泛化性\n\n- 具体位置：Section 4.6, Table 9 (Appendix H)\n- 问题：14B RSFT 在 dev 上 +3.44pp，但在 Re-DocRED test 上 Δ=-0.37pp（reversal）。Paper 的解释是 SFT 的 50.6% truncation rate 使其生成更多 candidate triples 以匹配 test set 的 2.82× 更密集的 annotation。这个解释实际上暗示了一个更深的问题：RSFT 通过 selection 偏好 compact outputs，这在 annotation-sparse 的 dev set 上有利（precision > recall），但在 annotation-dense 的 test set 上不利（需要更高 recall）。如果 RSFT 的改进部分来自匹配 dev set 的 annotation density，则其泛化性存疑。\n- 建议：（1）分析 RSFT vs SFT 的 prediction count 和 precision/recall trade-off，明确 RSFT 的改进是来自更好的 extraction quality 还是更保守的 prediction strategy；（2）在不同 annotation density 条件下评估 RSFT。\n\n**W4** [MAJOR] EDCR 与 Rel-F1 的 mechanical correlation 未被 partial correlation 充分控制\n\n- 具体位置：Section 3.5, Appendix L\n- 问题：EDCR = Σ|E_pred \\ E_gold| / Σ|E_pred|。当模型产生 false-positive triples 时，这些 triple 的所有 evidence 都计入 numerator（因为 E_gold 为空）。FP triples 同时降低 Rel-F1。所以 EDCR 和 Rel-F1 通过 FP triples（extraction precision）共享因果路径。Paper 的 partial correlation 控制的是 Evi-Recall_TP，但 shared component 是通过 extraction precision/FP rate，不是 evidence recall。正确的控制变量应是 precision 或 FP rate。\n  - Per-relation 分析（n=76）部分缓解了这个问题，但各 relation type 的数据来自相同 documents，不完全独立。Permutation test 假设一定程度的独立性，可能过于乐观。\n- 建议：（1）在 partial correlation 中控制 per-relation precision 而非 Evi-Recall_TP；（2）讨论 per-relation 数据点的 non-independence（shared documents）对 permutation test 的影响。\n\n**W5** [MAJOR] RSFT 的 \"cannot exploit the trade-off\" 论证是结构性的而非实证的\n\n- 具体位置：Section 2.3 (Related Work), Appendix G\n- 问题：Paper 声称 \"discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods discover\"。这在逻辑上是合理的（RSFT 不微分 reward signal），但 paper 自己在 Limitations 中承认这是 \"structural rather than empirical\"。缺少的关键实验是：固定 training data quality 但改变 selection mechanism（例如用 Rel-F1-only scoring 或 Evi-F1-only scoring 做 RSFT），看是否出现 decoupling。如果 Rel-F1-only RSFT 也不 decouple，则 \"discrete selection\" 解释成立；如果它 decouples（牺牲 evidence），则 CED 的 joint scoring 才是关键而非 selection 机制本身。\n- 此外，random selection baseline（41.14 Ign-F1）的比较基准是 SFT s42（39.74，最弱 seed）。对比 SFT 3-seed mean（43.58），random RSFT 实际上 **更差**（-2.44pp），仅 CED RSFT 有改善。这说明 \"selection 本身\" 的贡献可能为负，CED scoring 才是驱动因素。\n- 建议：（1）增加 Rel-F1-only RSFT 和 Evi-F1-only RSFT 实验；（2）random baseline 应对比 SFT multi-seed mean 而非最弱 seed。\n\n---\n\n## 小问题（不影响接收）\n\n**M1** [MINOR] 页数边界情况：Main text（Sections 1-5, 含 Conclusion）略微超出 page 8 进入 page 9 顶部（约 8-10 行）。Limitations 和 References 不计入页数限制，但 Conclusion 计入。建议压缩 Discussion (4.7) 或 Conclusion (5) 以严格控制在 8 页内。\n\n**M2** [MINOR] Decoupling spectrum 仅在 Qwen3-4B 上验证。未在其他 scale 或 LLaMA 上测试 GRPO/DPO，无法确认 spectrum 是否在不同 capacity/architecture 下 hold。\n\n**M3** [MINOR] Table 1 (Main Results) 的 SFT no-evidence 仅报告 s42 单个 seed（47.21），而 SFT with-evidence 报告 3-seed mean（43.58±3.80）。最强 SFT seed（s43: 47.34）超过 RSFT mean（44.82），使 \"RSFT improves over SFT\" 的结论取决于 seed 选择。建议为 no-evidence SFT 也报告 multi-seed 结果。\n\n**M4** [MINOR] CED hypothesis verbalization 的具体 template（\"$e_h$ has relation $r$ with $e_t$\"）对不同 relation type 可能有不同的自然程度。未讨论 verbalization template 对 NLI 评分的 sensitivity。\n\n**M5** [MINOR] 4B 的 training-time evidence tax 报告为 \"+0.25±0.47pp, n=3\"，但 inference-time tax（同一 RSFT model with/without evidence）报告为 \"+0.94\"（Table 2）。这两种 tax 的定义不同（training-time: 不同模型; inference-time: 同一模型不同输出格式），但 paper 在不同位置混用时没有足够清晰地区分。\n\n---\n\n## 主要优势\n\n1. **系统性实验覆盖**：3 optimization paradigms × 4+ model scales × 2 model families × 2 datasets × multiple seeds，在 LLM-based IE 领域是罕见的覆盖广度。\n2. **Novel observations**：Scale-dependent evidence tax（1.7B beneficial, ≥4B neutral）和 decoupling spectrum 是有价值的经验发现，即使统计证据需要加强。\n3. **透明度高**：Paper 主动讨论了 EDCR mechanical correlation、variance CI overlap、RSFT mechanistic caveat 等 limitations，显示出作者的诚实态度。\n4. **实用价值**：1.7B RSFT（51.19 Ign-F1, std 0.09pp）接近 8B SFT（50.19, std 3.23pp）在 4.7× 更少参数下，对部署有实际意义。\n5. **Thorough appendix**：11 个 appendix sections 提供了详尽的 ablation、error analysis、qualitative examples，极大增强了可重复性。\n6. **RSFT 对 evidence-grounded DocRE 的成功应用**：虽然 RSFT 本身不是新方法，但将其应用于 evidence-grounded IE 并用 CED 作为 domain-specific filter 是合理且有效的。\n\n---\n\n## Missing References\n\n未发现明显遗漏的关键参考文献。Related Work 覆盖了 DocRE（ATLOP, GAIN, SAIS, DREEAM, EIDER, AutoRE 等）、RL for structured generation（GRPO, DPO, PPO 及其变体）、和 evidence faithfulness（NLI-based scoring, STaR, RAFT）三个主要方向。\n\n---\n\n## 总结\n\n本文提出了一个 well-structured 的研究问题并进行了系统性实验。Scale-dependent evidence tax 和 decoupling spectrum 是有价值的概念贡献。但核心统计声明（variance compression、evidence tax threshold、decoupling spectrum universality）的证据基础较薄——n=3 seeds、single hyperparameter settings、confounded GRPO comparison——使得 Contribution 2 和 3 的结论强度显著超过了实验证据的支撑力。14B test reversal 进一步提示 RSFT 的改进可能部分依赖于 dev/test annotation density 的匹配。建议在 rebuttal 中：（1）增加 GRPO bf16 G=4 控制实验；（2）对 DPO β 做 sensitivity analysis；（3）将方差压缩 claim 降级到与统计证据匹配的强度。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见 — Round 3 (方法严谨性 + 实验设计 + 统计声明)\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026 via ARR\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 系统性实验设计和新颖观察（scale-dependent evidence tax, decoupling spectrum）是有价值的贡献，但多个核心声明的统计证据不足（n=3 方差、单 seed 税率、GRPO 混淆变量），且 14B test reversal 削弱了泛化性论述。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有方向性支持但统计证据薄弱：方差压缩 n=3 + CI 重叠 3/4 scales；evidence tax threshold 依赖 n=1 seeds；GRPO 实验存在未隔离的混淆变量 |\n| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 是有趣的新观察；但实际影响受限于 Wikipedia-only 数据集和 RSFT 对 evidence quality 无改善 |\n| Reproducibility | 4/5 | Appendix 详尽（hyperparameters, per-seed results, error analysis），但 CED 实现细节（hypothesis verbalization template）未完整给出 |\n| Confidence | 4/5 | 我仔细阅读了全文及附录，此领域在我的专业范围内 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [CRITICAL] GRPO QLoRA vs bf16 实验存在未隔离的混淆变量\n\n- 具体位置：Section 4.3, Table 13 (Appendix I)\n- 问题：Paper 将 GRPO catastrophic collapse 归因于 \"quantization precision rather than group size as the primary factor\"（Section 4.3），但两个配置同时改变了 **两个** 变量：quantization（NF4 4-bit vs bf16）**和** group size（G=4 vs G=8）。没有控制实验（QLoRA G=8 或 bf16 G=4）来隔离这两个因素。\n- 为什么影响接收：Decoupling spectrum 是本文核心贡献之一。如果 catastrophic collapse 是由 G=4（过小的 group size 导致高 variance advantage estimates）而非 quantization 造成的，则整个 \"quantization-constrained precision\" 叙事需要修改。Paper 引用了 \\citet{li2026qurl} 的 quantized-actor divergence 来支持 quantization 解释，但这是一个没有控制实验支撑的类比。\n- 建议修改方向：（1）增加 bf16 G=4 实验以隔离 group size 效应；或（2）将结论从 \"quantization precision...as the primary factor\" 降级为 \"quantization and/or group size\"，承认无法区分两个因素。\n\n**N2** [CRITICAL] 方差压缩声明的统计证据不足（n=3 seeds）\n\n- 具体位置：Section 4.4, Table 6 (Appendix D), Abstract\n- 问题：\n  - 4/4 scales 中仅 1.7B 的 χ² CI 不重叠（SFT lower 1.45 > RSFT upper 0.54）。其余 3 个 scale 的 CI 均重叠。\n  - Sign test p=0.0625（one-sided），不满足 α=0.05 显著性水平。Paper 自己说 \"underpowered\"。\n  - Cohen's d 在 4B 仅为 0.46（small effect）。\n  - Abstract 中 \"consistently reduces training seed variance\" 和 \"complete pairwise seed separation on LLaMA, Cohen's d=2.58; non-overlapping χ² confidence intervals at 1.7B\" 选择性报告了最强结果（cherry-picking）。\n- 为什么影响接收：这是本文三大 contribution 之一。\"Consistently reduces\" 在统计上不成立——方向一致但缺乏统计显著性。n=3 的 χ² CI 宽度极大（例如 SFT 4B: [1.98, 23.89]），几乎没有 discriminative power。\n- 建议修改方向：（1）将 \"consistently reduces\" 改为 \"shows a consistent directional pattern with statistical significance only at the 1.7B scale\"；（2）Abstract 中展示全景而非选择最强结果；（3）增加 seeds 数量（至少 n=5）以获得有意义的 CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [MAJOR] Evidence tax 因果推断——implicit regularization 假说证据不足\n\n- 具体位置：Section 4.4, Appendix E (Table 7), Introduction\n- 问题：1.7B evidence tax 为负（-5.63pp），paper 提出 \"implicit regularization hypothesis\"——evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition。但 Table 16 (Appendix N) 显示 1.7B with-evidence 模型只生成 25.5k predictions vs no-evidence 的 44.6k（1.75×差异）。这意味着有一个更简单的替代解释：evidence 格式使每个 triple 的 output 更长，从而限制了总 prediction 数量，机械性地减少了 duplication 和 FP，提高了 precision-heavy 指标（Ign-F1）。Paper 说 \"partly through halving output duplication\"（Introduction），但未量化这个 mechanical 效应与 \"真正的 regularization\" 效应的相对贡献。\n- 建议：（1）在 matched prediction count 条件下重新计算 evidence tax（例如，将 no-evidence 模型的 predictions 截断到与 evidence 模型相同的数量，再比较 Ign-F1）；（2）或者将 \"implicit regularization\" 降级为 \"output constraint effect\" 并明确承认无法区分因果机制。\n\n**W2** [MAJOR] GRPO/DPO 超参数探索不足\n\n- 具体位置：Section 3.3, Table 3 (Appendix A)\n- 问题：GRPO 只测试了 KL=0.01，DPO 只测试了 β=0.1。这些是默认值但可能不适合 evidence-grounded DocRE 的 multi-objective setting。DPO 1-epoch 的 Rel-F1 就已从 SFT 的 44.39 暴跌到 33.37（-11pp），这在 DPO 文献中是异常大的 degradation，更可能是 β 选择不当而非 DPO 的固有限制。如果 β=0.01 或 β=0.5 能维持更好的 extraction，则 \"DPO gradual degradation\" 的结论不成立。\n- 为什么重要：Decoupling spectrum（GRPO catastrophic → DPO gradual → RSFT none）是本文核心贡献。如果 GRPO/DPO 端是因为超参数选择不当而非方法论限制，则 spectrum 的概括性被严重削弱。\n- 建议：至少对 DPO β ∈ {0.01, 0.1, 0.5} 和 GRPO KL ∈ {0.001, 0.01, 0.1} 做 sensitivity analysis。\n\n**W3** [MAJOR] 14B test-set reversal 削弱泛化性\n\n- 具体位置：Section 4.6, Table 9 (Appendix H)\n- 问题：14B RSFT 在 dev 上 +3.44pp，但在 Re-DocRED test 上 Δ=-0.37pp（reversal）。Paper 的解释是 SFT 的 50.6% truncation rate 使其生成更多 candidate triples 以匹配 test set 的 2.82× 更密集的 annotation。这个解释实际上暗示了一个更深的问题：RSFT 通过 selection 偏好 compact outputs，这在 annotation-sparse 的 dev set 上有利（precision > recall），但在 annotation-dense 的 test set 上不利（需要更高 recall）。如果 RSFT 的改进部分来自匹配 dev set 的 annotation density，则其泛化性存疑。\n- 建议：（1）分析 RSFT vs SFT 的 prediction count 和 precision/recall trade-off，明确 RSFT 的改进是来自更好的 extraction quality 还是更保守的 prediction strategy；（2）在不同 annotation density 条件下评估 RSFT。\n\n**W4** [MAJOR] EDCR 与 Rel-F1 的 mechanical correlation 未被 partial correlation 充分控制\n\n- 具体位置：Section 3.5, Appendix L\n- 问题：EDCR = Σ|E_pred \\ E_gold| / Σ|E_pred|。当模型产生 false-positive triples 时，这些 triple 的所有 evidence 都计入 numerator（因为 E_gold 为空）。FP triples 同时降低 Rel-F1。所以 EDCR 和 Rel-F1 通过 FP triples（extraction precision）共享因果路径。Paper 的 partial correlation 控制的是 Evi-Recall_TP，但 shared component 是通过 extraction precision/FP rate，不是 evidence recall。正确的控制变量应是 precision 或 FP rate。\n  - Per-relation 分析（n=76）部分缓解了这个问题，但各 relation type 的数据来自相同 documents，不完全独立。Permutation test 假设一定程度的独立性，可能过于乐观。\n- 建议：（1）在 partial correlation 中控制 per-relation precision 而非 Evi-Recall_TP；（2）讨论 per-relation 数据点的 non-independence（shared documents）对 permutation test 的影响。\n\n**W5** [MAJOR] RSFT 的 \"cannot exploit the trade-off\" 论证是结构性的而非实证的\n\n- 具体位置：Section 2.3 (Related Work), Appendix G\n- 问题：Paper 声称 \"discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods discover\"。这在逻辑上是合理的（RSFT 不微分 reward signal），但 paper 自己在 Limitations 中承认这是 \"structural rather than empirical\"。缺少的关键实验是：固定 training data quality 但改变 selection mechanism（例如用 Rel-F1-only scoring 或 Evi-F1-only scoring 做 RSFT），看是否出现 decoupling。如果 Rel-F1-only RSFT 也不 decouple，则 \"discrete selection\" 解释成立；如果它 decouples（牺牲 evidence），则 CED 的 joint scoring 才是关键而非 selection 机制本身。\n- 此外，random selection baseline（41.14 Ign-F1）的比较基准是 SFT s42（39.74，最弱 seed）。对比 SFT 3-seed mean（43.58），random RSFT 实际上 **更差**（-2.44pp），仅 CED RSFT 有改善。这说明 \"selection 本身\" 的贡献可能为负，CED scoring 才是驱动因素。\n- 建议：（1）增加 Rel-F1-only RSFT 和 Evi-F1-only RSFT 实验；（2）random baseline 应对比 SFT multi-seed mean 而非最弱 seed。\n\n---\n\n## 小问题（不影响接收）\n\n**M1** [MINOR] 页数边界情况：Main text（Sections 1-5, 含 Conclusion）略微超出 page 8 进入 page 9 顶部（约 8-10 行）。Limitations 和 References 不计入页数限制，但 Conclusion 计入。建议压缩 Discussion (4.7) 或 Conclusion (5) 以严格控制在 8 页内。\n\n**M2** [MINOR] Decoupling spectrum 仅在 Qwen3-4B 上验证。未在其他 scale 或 LLaMA 上测试 GRPO/DPO，无法确认 spectrum 是否在不同 capacity/architecture 下 hold。\n\n**M3** [MINOR] Table 1 (Main Results) 的 SFT no-evidence 仅报告 s42 单个 seed（47.21），而 SFT with-evidence 报告 3-seed mean（43.58±3.80）。最强 SFT seed（s43: 47.34）超过 RSFT mean（44.82），使 \"RSFT improves over SFT\" 的结论取决于 seed 选择。建议为 no-evidence SFT 也报告 multi-seed 结果。\n\n**M4** [MINOR] CED hypothesis verbalization 的具体 template（\"$e_h$ has relation $r$ with $e_t$\"）对不同 relation type 可能有不同的自然程度。未讨论 verbalization template 对 NLI 评分的 sensitivity。\n\n**M5** [MINOR] 4B 的 training-time evidence tax 报告为 \"+0.25±0.47pp, n=3\"，但 inference-time tax（同一 RSFT model with/without evidence）报告为 \"+0.94\"（Table 2）。这两种 tax 的定义不同（training-time: 不同模型; inference-time: 同一模型不同输出格式），但 paper 在不同位置混用时没有足够清晰地区分。\n\n---\n\n## 主要优势\n\n1. **系统性实验覆盖**：3 optimization paradigms × 4+ model scales × 2 model families × 2 datasets × multiple seeds，在 LLM-based IE 领域是罕见的覆盖广度。\n2. **Novel observations**：Scale-dependent evidence tax（1.7B beneficial, ≥4B neutral）和 decoupling spectrum 是有价值的经验发现，即使统计证据需要加强。\n3. **透明度高**：Paper 主动讨论了 EDCR mechanical correlation、variance CI overlap、RSFT mechanistic caveat 等 limitations，显示出作者的诚实态度。\n4. **实用价值**：1.7B RSFT（51.19 Ign-F1, std 0.09pp）接近 8B SFT（50.19, std 3.23pp）在 4.7× 更少参数下，对部署有实际意义。\n5. **Thorough appendix**：11 个 appendix sections 提供了详尽的 ablation、error analysis、qualitative examples，极大增强了可重复性。\n6. **RSFT 对 evidence-grounded DocRE 的成功应用**：虽然 RSFT 本身不是新方法，但将其应用于 evidence-grounded IE 并用 CED 作为 domain-specific filter 是合理且有效的。\n\n---\n\n## Missing References\n\n未发现明显遗漏的关键参考文献。Related Work 覆盖了 DocRE（ATLOP, GAIN, SAIS, DREEAM, EIDER, AutoRE 等）、RL for structured generation（GRPO, DPO, PPO 及其变体）、和 evidence faithfulness（NLI-based scoring, STaR, RAFT）三个主要方向。\n\n---\n\n## 总结\n\n本文提出了一个 well-structured 的研究问题并进行了系统性实验。Scale-dependent evidence tax 和 decoupling spectrum 是有价值的概念贡献。但核心统计声明（variance compression、evidence tax threshold、decoupling spectrum universality）的证据基础较薄——n=3 seeds、single hyperparameter settings、confounded GRPO comparison——使得 Contribution 2 和 3 的结论强度显著超过了实验证据的支撑力。14B test reversal 进一步提示 RSFT 的改进可能部分依赖于 dev/test annotation density 的匹配。建议在 rebuttal 中：（1）增加 GRPO bf16 G=4 控制实验；（2）对 DPO β 做 sensitivity analysis；（3）将方差压缩 claim 降级到与统计证据匹配的强度。",
    "reviewer_id": "1",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-24T23:01:27.641047+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---

### Assistant

_source line 240 · 2026-05-24T23:01:37.191939+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference），Soundness 3/5，Excitement 3/5。

识别了 2 个 Critical 问题（GRPO QLoRA/bf16 混淆变量未隔离；n=3 方差压缩声明过强）、5 个 Major 问题（evidence tax 因果推断不足；GRPO/DPO 超参数探索有限；14B test reversal；EDCR mechanical correlation 控制不当；RSFT 结构性论证缺乏实证验证）、5 个 Minor 问题（页数边界、spectrum 仅在 4B 验证、baseline seed 选择、CED template sensitivity、tax 定义混用）。同时肯定了论文在系统性覆盖、透明度和实用价值方面的优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---

## Round 6

2 recorded events

### User

_source line 241 · 2026-05-24T23:03:50.656388+00:00_

[Round 3 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告

**Overall**: 3.5 (Borderline Conference)

### 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计总体严谨，多 scale/family/dataset 交叉验证充分；但 DPO 仅测试单一 β=0.1，variance 比较方法论存在可比性问题，14B 仅 1-2 seed |
| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 作为 empirical findings 有启发性，但缺乏方法论创新；CED 的 ablation 自证其无必要（vs flat-NLI 差 0.02pp） |
| Reproducibility | 4/5 | 超参数完整报告（Table 3/Appendix A），LoRA 配置清晰，per-seed 结果透明；但未提供代码/数据链接 |
| Confidence | 4/5 | 熟悉 DocRE 和 LLM RL 文献，仔细阅读了全文和附录 |

### Must-Fix 问题

**N1** [CRITICAL] 贡献定位模糊：empirical study 却暗示 method innovation
- 三个 contribution 均为 empirical observation。RSFT 是已有框架，论文自己承认"the contribution of RSFT in our setting is not the framework itself"（§3.3 末）。CED 被 ablation 自我否定——flat-NLI 与 CED RSFT 的 Rel-F1 差异仅 0.02pp（§4.7, Appendix B Table 4），contrastive 部分实质上无用。但论文 framing 仍然暗示方法创新（"We formalize...", "we propose the Evidence-Decoupling Ratio"）。
- 建议：明确定位为 empirical study；将 CED 降级为 "scoring tool" 而非 "proposed method"；强调 findings 的独立价值。

**N2** [MAJOR] Abstract 超过 200 words
- 经计算约 205 words，超过 EMNLP 2026 ARR 的 200-word 硬限制。Abstract 过于密集，塞入大量数字。
- 建议：删减具体数字，聚焦 what you found + why it matters。

**N3** [MAJOR] 正文可能超过 8 页
- §4.7 末尾和 §5 Conclusion 位于第 9 页。主体正文超出 8 页限制约 0.1-0.2 页。
- 建议：压缩 Discussion 或移 Figure/Table 入 Appendix。

### Should-Fix 问题

**W1** [MAJOR] DPO 评估配置不足
- DPO 仅测试 β=0.1。1-epoch Rel-F1 即暴跌至 33.37（SFT 44.39），可能是 β 不当导致的 artifact。
- 建议：至少测试 2-3 个 β 值。

**W2** [MAJOR] RSFT 与 SFT variance 比较方法论
- RSFT variance 来自固定 SFT model 再 sampling-then-retraining，天然压缩 variance。所有 RSFT 实验似乎从同一 SFT model 出发，不是公平比较。
- 建议：报告从多个 SFT seed 出发做 RSFT 的 variance。

**W3** [WARNING] 14B 评估不充分
- 14B SFT 仅 1 seed，RSFT 仅 2 seed。Test set 上 14B RSFT 反而下降 0.37pp。

**W4** [WARNING] Evidence quality 未被 RSFT 改善
- RSFT 改善 extraction 但 evidence quality 不变（<0.4pp）。CED 优于 random 可能主要来自 extraction quality filtering。

**W5** [WARNING] 缺少 DocRED 官方 test set 评测
- 仅在 Re-DocRED test set 上做了 test evaluation，未使用 DocRED CodaLab leaderboard。

### 小问题
- M1: Evidence tax 方向约定不一致
- M2: Bibliography key-name 不匹配（chen2025docksrag 第一作者 Xu 等）
- M3: §4.5 仅一段，BM25 k=2 未 justify
- M4: EDCR cross-method ρ 数值不一致（§3.5 ρ=−0.89 vs §4.7 ρ=−0.96）
- M5: GRPO bf16 vs QLoRA effective batch size 差异未讨论

### Missing References
- DeepSeek-R1（GRPO flagship 成功案例，论文仅引用 DeepSeekMath）
- ReST（Gulcehre et al., 2023, Reinforced Self-Training）

### 主要优势
1. 实验设计全面且透明
2. Scale-dependent evidence tax 是非平凡发现
3. Decoupling spectrum 提供有用分析框架
4. RSFT 实际价值清晰
5. 写作质量整体良好

---

请对以上每一条逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 242 · 2026-05-24T23:06:57.016377+00:00_

以下是我对 Reviewer 2 各条意见的逐条回应。

---

### Must-Fix 问题

**[AGREE] R2-N1: 贡献定位模糊——empirical study 却暗示 method innovation**

同意 R2 的观察。Paper 的三个 contribution（Introduction enumerated list）均为 empirical findings，而非方法论创新：(1) evidence tax 是 scale-dependent 的——观察；(2) gradient pressure 导致 decoupling——观察 + EDCR 诊断工具；(3) RSFT reduces variance——观察。Paper 在 §3.3 末明确承认 "the contribution of RSFT in our setting is not the framework itself"，且 Appendix B Table 4 的 ablation 证实 CED 与 flat-NLI 仅差 0.02pp Rel-F1，contrastive 组件实质无效。论文用 "We formalize..." 和 "we propose EDCR" 的措辞确实暗示了方法创新。

**补充**：但我认为严重程度应为 MAJOR 而非 CRITICAL。Empirical study 在 *ACL 有明确的接收空间（多个 best paper 是 empirical studies），关键是 findings 是否足够 non-trivial。重新定位为 empirical study + diagnostic tool 并不需要大幅重写，而是 framing 调整。

---

**[AGREE] R2-N2: Abstract 超过 200 words**

我没有精确计数，但 abstract 信息密度极高，包含大量具体数字（-5.63pp、+0.25±0.47pp、Cohen's d=2.58、4.7× 等）。即使精确字数在 200 ± 5 的边界，也应主动压缩以避免 desk reject 风险。EMNLP 2026 CLAUDE.md 明确标注 "abstract 不要超过 200 words" 为硬约束。

---

**[AGREE] R2-N3: 正文可能超过 8 页**

与我在 M1 中标注的问题一致。PDF 页面 9 顶部包含 §4.7 Discussion 末尾和 §5 Conclusion（约 8-10 行正文），之后才是 Limitations 和 References。主体正文（Sections 1-5）确实略超 8 页。但我将此评为 MINOR——溢出量很小（<0.2 页），压缩 Discussion 或将 Figure 4/5 移入 Appendix 即可解决。R2 评为 MAJOR 偏重。

---

### Should-Fix 问题

**[AGREE] R2-W1: DPO 评估配置不足**

与我的 W2 完全一致。DPO 1-epoch Rel-F1 从 44.39 暴跌至 33.37（-11pp），这在 DPO 文献中是异常大的 degradation。单一 β=0.1 无法区分"DPO 固有限制"和"超参数不当"。需要至少 β ∈ {0.01, 0.1, 0.5} 的 sensitivity analysis 才能支撑 "DPO gradual degradation" 结论。

---

**[AGREE] R2-W2: RSFT 与 SFT variance 比较方法论存在可比性问题**

这是我自己 review 中遗漏的重要问题。Paper §3.3 描述 RSFT 流程："the SFT model generates N=8 candidate outputs per training document"（单数 "the SFT model"），暗示所有 RSFT seeds 从**同一个** SFT checkpoint 出发。如果是这样，SFT variance 包含 LoRA 初始化的全流程方差，而 RSFT variance 仅包含第二阶段微调的方差——两者测量的是不同层级的随机性。Paper 在 §4.2 提到 "though these reflect different sources of variation (Section 4.4)"，但 abstract 和 contribution 3 中的 "RSFT consistently reduces training seed variance" 并未传达这个关键 caveat。这显著削弱了 Contribution 3 的可信度。

**补充**：如果每个 RSFT seed（s42/s43/s44/s45）分别从对应的 SFT seed 出发生成 candidates 并训练，则比较更公平。但 paper 未明确说明这一点，且 RSFT training samples 固定为 2,718（Table 3），暗示共用同一 candidate pool。

---

**[AGREE] R2-W3: 14B 评估不充分**

与我的 W3 一致。14B SFT 仅 1 seed（Table 2 footnote），RSFT 仅 2 seeds。在 test set 上出现 reversal（Δ=-0.37pp, Table 9 Appendix H），但没有足够 seeds 来判断这是噪声还是系统性效应。14B 被定位为 "validation" 而非 "fully evaluated"（Introduction: "three fully evaluated scales (1.7B, 4B, 8B) with 14B validation"），这是合理的框架设计，但 test reversal 仍然值得更多 seeds 来验证。

---

**[AGREE] R2-W4: Evidence quality 未被 RSFT 改善**

Paper 自己在 Appendix K 中承认 "evidence quality is unchanged (Δ < 0.4pp)"，§4.7 中也明确指出 "RSFT improves what the model extracts but not how well it grounds extractions"。R2 的延伸推论——CED 优于 random 可能主要来自 extraction quality filtering——也有 textual support：CED document-level score "weights by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit"（§3.4）。这意味着 CED 的 selection 信号同时包含 extraction quality 和 evidence quality，前者可能是主要驱动力。

---

**[REBUT] R2-W5: 缺少 DocRED 官方 test set 评测**

部分不同意。DocRED 官方 test set 通过 CodaLab 提交，但 CodaLab leaderboard 不评估 evidence 指标——它只报 Ign-F1 和 F1。本文的核心贡献关于 evidence-extraction interaction，DocRED test 无法评估这些维度。此外，Re-DocRED test set 是对 DocRED 的重新标注，annotation quality 更高（修复了 DocRED 中 ~20% 的 missing annotations），是更严格的评估。Paper 使用 Re-DocRED test 并报告了完整的 5-model comparison（Table 9, Appendix H），这是合理的评估策略。

但我同意，为了与先前工作（ATLOP, SAIS, DREEAM）的可比性，报告 DocRED test 的 Ign-F1 仍然有价值。这应是 MINOR 建议而非 WARNING。

---

### 小问题

**[REBUT] R2-M1: Evidence tax 方向约定不一致**

我检查了论文中所有 evidence tax 的定义：
- Table 2 footnote: "Tax = no-evi − with-evi; positive = cost"
- §4.4: "Ign-F1(no-evidence) − Ign-F1(with-evidence)"
- Table 8 (Appendix F): "Tax = no-evi − with-evi; positive = cost"
- Table 10 (Appendix H): "Tax = no-evi − with-evi; negative = benefit"
- Table 11 (Appendix H): "Tax = no-evi − with-evi; positive = cost"
- Figure 7 caption: "Negative values indicate evidence benefits extraction"

数学定义完全一致。R2 可能指的是语义上的混淆——将 benefit 称为 "negative tax" 确实不直觉，但这是 naming awkwardness 而非 inconsistency。

---

**[AGREE] R2-M2: Bibliography key-name 不匹配**

无法直接验证（需要检查 references.bib），但 R2 如果确认 chen2025docksrag 的第一作者实际是 Xu 等人，则 bib key 有误导性。应检查并修正。

---

**[AGREE] R2-M3: §4.5 仅一段，BM25 k=2 未 justify**

Section 4.5（Evidence Strategy Comparison）确实过于简略。BM25 的 k=2 选择缺乏 justification。作为 evidence strategy 的主要对比实验，至少应讨论 k 的选择依据或提供 k 的 sensitivity。

---

**[AGREE] R2-M4: EDCR cross-method ρ 数值不一致**

这是一个真实的数值不一致。§3.5 报告 cross-method ρ=−0.89（n=7, p=0.007），§4.7 报告 ρ=−0.96（n=7, p<0.001），Appendix L 报告 raw ρ=−0.9643（n=7）。三个位置声称相同的 n=7 但给出不同的 ρ 值。可能的解释：§3.5 使用 3-seed mean per method，而 Appendix L 使用不同聚合方式。但论文未解释这一差异。**这是一个需要修正的错误**。

---

**[AGREE] R2-M5: GRPO bf16 vs QLoRA effective batch size 差异未讨论**

Table 3 显示 QLoRA (batch=4, grad_accum=16, G=4) vs bf16 (batch=8, grad_accum=4, G=8)。Effective input batch: 64 vs 32。虽然总 response 数量可能相同（256 vs 256），每步看到的 unique input documents 数量不同（64 vs 32），这影响 gradient estimation quality。这是 GRPO 实验中另一个未控制的变量，进一步削弱了将 collapse 归因于 quantization 的结论。与我的 N1 中指出的 confound 一致。

---

### Missing References

**[AGREE] DeepSeek-R1**：作为 GRPO 最成功的应用案例，仅引用 DeepSeekMath（GRPO 原论文）而遗漏 DeepSeek-R1 确实是一个明显的 gap。

**[AGREE] ReST (Gulcehre et al., 2023)**：作为 rejection sampling 在 LLM training 中的重要工作（在 STaR 和 RFT 之间），与 RSFT 直接相关，应该被引用。

---

### 总结

R2 的 12 个具体问题中，我 **[AGREE] 10 条**，**[REBUT] 2 条**（M1 evidence tax 方向约定实际一致；W5 缺少 DocRED test 的严重性被高估）。

R2 最有价值的独特贡献是 **W2（RSFT vs SFT variance 可比性）**——如果所有 RSFT 从同一 SFT checkpoint 出发，Contribution 3 的统计比较在方法论上不成立。这一点我自己的 review 中遗漏了，是对我 N2 的重要补充。

我与 R2 在 Overall 评分上一致（3.5 Borderline Conference）。核心判断相同：有价值的 empirical findings，但统计证据和实验设计存在多个可修复但当前未修复的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---

## Round 7

60 recorded events

### User

_source line 243 · 2026-05-25T22:31:07.589406+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。

## Venue 信息
- **目标**: EMNLP 2026（ARR May 2026 cycle）
- **截止**: 2026-05-25
- **格式**: ACL 模板 [review]，Long paper 正文严格 8 页，参考文献不限
- **Limitations**: 必须，conclusion 之后，不计入页数
- **匿名**: Double-blind
- **会议**: Budapest, Hungary, 2026-10-24 ~ 10-29

## 论文路径
- main.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf`

## 你的审查侧重

请重点审查以下方面：

1. **EDCR 指标设计与验证**：
   - EDCR 公式的合理性——分子分母共享 TP 组件导致的机械负相关是否充分讨论？
   - per-relation 验证 (n=76, ρ=-0.79) 的统计效力是否足够？
   - partial correlation 和 permutation test 是否正确控制了 confound？

2. **CED 评分方法论**：
   - NLI-based scoring 的局限性：只用了 DeBERTa-v3-base，sensitivity analysis 充分吗？
   - CED vs flat-NLI 仅差 0.02pp，contrastive formulation 的附加价值是什么？

3. **实验控制与 confound**：
   - GRPO QLoRA vs bf16 对比：quantization 和 precision 之外是否有其他未控制的变量？（lr 不同？）
   - DPO β=0.1 单一设定，spectrum 结论的稳健性？
   - RSFT 共享 SFT checkpoint 导致 variance 比较不公平（SFT = full randomness, RSFT = fixed-base）

4. **统计严谨性**：
   - n=3 seeds 的统计效力（sign test p=0.0625 不显著）
   - evidence tax 的 CI 是否 cross zero？
   - 1.7B 的 s42 是最强 seed (+3.22pp above mean)，是否影响 tax 估计？

5. **Scaling claim**：
   - 4 个 Qwen3 scale + 1 个 LLaMA，"scale-dependent" 结论需要多少数据点？
   - 14B 仅 1 seed SFT baseline，可靠性？
   - test-set 14B RSFT advantage 消失（Δ=-0.37pp），如何解释？

6. **页数合规**：
   - 18 页 PDF，正文是否超过 8 页？（EMNLP 2026 严格 8 页，超页 = desk reject）

请按 Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment 的结构输出审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-25T22:31:21.253021+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-25T22:31:21.353845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-25T22:31:24.817941+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
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

_source line 247 · 2026-05-25T22:31:24.869430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-25T22:31:30.651363+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-25T22:31:30.702094+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
  "pages": "1-10",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
    "pages": "1-10",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 250 · 2026-05-25T22:31:39.347519+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes reviewers may find the work sound, but not something that is interesting for them personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Guidelines

All papers recommended for Findings or main conference are expected to be sound and reproducible. The ACs should mostly follow the soundness assessment of the reviewers when they 
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8696
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-25T22:31:42.366501+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 623.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 647.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.1}, {\"page\": 10, \"pa
…[truncated 427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 11664
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-25T22:31:48.350007+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form 2025 soundness excitement scoring 1-5 scale criteria details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form 2025 soundness excitement scoring 1-5 scale criteria details"
  }
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-25T22:31:48.854418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-25T22:31:49.358494+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-25T22:31:50.064685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-25T22:31:50.216419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-25T22:31:50.267727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-25T22:31:50.871781+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-25T22:31:57.008985+00:00_

Web search results for query: "ACL Rolling Review reviewer form 2025 soundness excitement scoring 1-5 scale criteria details"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, here are the details about the ACL Rolling Review (ARR) 2025 reviewer form scoring criteria:

## Three Scoring Components

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Scoring (1-5 Scale)

The soundness assessment evaluates whether the paper is sufficiently sound and thorough, clearly states scientific claims and provides adequate support. For experimental papers, reviewers consider the depth and/or breadth of research questions, technical soundness of experiments, and methodological validity 
…[truncated 1580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8658
}
```

</details>

---

### Tool call

_source line 260 · 2026-05-25T22:32:03.640444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 261 · 2026-05-25T22:32:03.995058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-25T22:32:04.552064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-25T22:32:05.119814+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1479
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-25T22:32:05.125379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 265 · 2026-05-25T22:32:06.267055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-25T22:32:06.470198+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2475
}
```

</details>

---

### Tool call

_source line 267 · 2026-05-25T22:32:06.623458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-25T22:32:06.926013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2373
}
```

</details>

---

### Tool call

_source line 269 · 2026-05-25T22:32:06.926498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 270 · 2026-05-25T22:32:07.179729+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2054
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-25T22:32:07.988113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1721
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-25T22:32:08.342878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1719
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-25T22:32:08.444200+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1517
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-25T22:32:15.171384+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
  "pages": "11-18",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
    "pages": "11-18",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-25T22:32:16.178280+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 377.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.5}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 411.5}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metad
…[truncated 12 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1006
}
```

</details>

---

### Tool call

_source line 276 · 2026-05-25T22:32:19.798480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 277 · 2026-05-25T22:32:20.355465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-25T22:32:21.213465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---

### Tool call

_source line 279 · 2026-05-25T22:32:21.213942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 280 · 2026-05-25T22:32:22.075557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1720
}
```

</details>

---

### Tool call

_source line 281 · 2026-05-25T22:32:22.076008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-25T22:32:22.226782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool result

_source line 283 · 2026-05-25T22:32:22.681829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1467
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-25T22:32:22.686026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool call

_source line 285 · 2026-05-25T22:32:23.643995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-25T22:32:24.298222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-25T22:32:24.855457+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2628
}
```

</details>

---

### Tool result

_source line 288 · 2026-05-25T22:32:24.861816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2785
}
```

</details>

---

### Tool result

_source line 289 · 2026-05-25T22:32:26.119113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3433
}
```

</details>

---

### Tool result

_source line 290 · 2026-05-25T22:32:26.576814+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2278
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-25T22:32:26.879836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3235
}
```

</details>

---

### Tool call

_source line 292 · 2026-05-25T22:32:31.800009+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-25T22:32:31.900926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-25T22:32:45.432415+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scale points (1-5), and detailed descriptions for each score level. Include soundness, excitement, overall assessment, reproducibility, and any other dimensions. I need the exact wording for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scale points (1-5), and detailed descriptions for each score level. Include soundness, excitement, overall assessment, reproducibility, and any other dimensions. I need the exact wording for each score level."
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-25T22:32:51.459356+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully."
- 3: "Pretty sure, but there's a chance I missed something."
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand."

## Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims."
- 3: "Acceptable: This study provides sufficient support for its main claims."
- 2: "Poor: Some of the main claims are not sufficiently supported."
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale: 1-5 (with .5 increments)**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper to others"
- 2: "Potentially Interesting: this paper does not resonate with me"
- 1: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: Consider for Award
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Reproducibility
**Scale: 1-5**
- 5: "They could easily reproduce the results."
- 4: "They could mostly reproduce the results"
- 3: "They could reproduce the results with some difficulty."
- 2: "They would be hard pressed to reproduce the results"
- 1: "They would not be able to reproduce the results"

## Datasets & Software
**Scale: 1-5**
- 5: Enabling
- 4: Useful
- 3: Potentially useful
- 2: Documentary
- 1: No usable release

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6026
}
```

</details>

---

### Tool call

_source line 296 · 2026-05-25T22:37:11.528691+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 = Borderline Conference\n**一句话总结**: 研究问题重要且实验覆盖面广，EDCR 指标设计新颖且验证较充分，但核心 claim（evidence tax 规模依赖性）的统计支撑不足（n=3, CI 跨零），加上 CED 对比设计未带来可衡量收益（0.02pp）以及部分实验 confound 未隔离，削弱了结论的可靠性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 主要 claims 有实验支撑但关键效应的 CI 跨零（evidence tax @ n=3），GRPO 实验存在 lr-quantization confound，DPO 仅单一 β=0.1 |\n| Excitement | 3.5/5 | 研究问题（extraction-evidence trade-off）重要且 under-explored，EDCR 诊断指标有实用价值，但 RSFT 作为方法贡献偏 incremental |\n| Reproducibility | 4/5 | 代码和数据承诺公开，超参数表格完整（Table 4），实验设置描述充分，但部分配置细节（如 GRPO bf16 lr）不够透明 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文和全部附录，DocRE 和 RL alignment 方法论在我的审查范围内 |\n\n---\n\n## 主要优势\n\n**S1. 研究问题定义精准，实用价值高。** 论文准确识别了 LLM-based DocRE 中 evidence grounding 的代价问题——现有方法要么不产出 evidence，要么假设 evidence 免费。将 evidence-extraction trade-off 作为一个显式的研究对象是一个有价值的 framing（Section 1, contributions 1-3）。\n\n**S2. EDCR 指标设计巧妙且验证充分。** EDCR（Eq. 2）作为 extraction-evidence decoupling 的诊断工具，概念清晰且有实际用途。Appendix L 的验证非常充分：partial correlation 控制 TP 后相关性仅下降 0.15%（ρ: -0.8541 → -0.8551），10,000 次 permutation test 确认 p<0.0001，per-relation 分析（n=76, ρ=-0.79）与 cross-method 分析（n=17）一致。这是论文最扎实的贡献。\n\n**S3. 三范式系统对比框架有参考价值。** 将 GRPO、DPO、RSFT 统一在同一 SFT baseline、同一评估协议下对比，并用 Table 1 清晰概括三者的信号类型和训练机制差异，对 practitioner 选择后训练策略有直接指导意义。\n\n**S4. 跨模型家族和跨规模验证增强了发现的可推广性。** 在 4 个 Qwen3 规模（1.7B-14B）和 LLaMA-3.1-8B 上的交叉验证（Table 3, Appendix H）显示 RSFT 的核心模式在不同架构上一致。\n\n**S5. 附录质量高。** 14 个附录覆盖了消融、统计验证、error decomposition、定性分析等，显示了严谨的研究态度。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] n=3 seeds 的统计效力不足以支撑核心 claim\n- 具体位置：Section 4.4, Table 7 (Appendix D), Section 4.2\n- 问题：论文承认 \"CI crosses zero at n=3\"（p.7），但仍在 abstract 和 contributions 中将 evidence tax 描述为已确立的现象（\"We observe a scale-dependent evidence tax\"）。对于 3 个 seeds：\n  - Sign test 最小 p-value = 0.0625，无法达到任何常规显著性水平\n  - Table 7 的 95% CI 均极宽，多个配置的 RSFT gain CI 确实跨零\n  - 1.7B 的 s42 是最强 seed（+3.22pp above mean），在 n=3 中有 disproportionate influence\n- 为什么影响接收：evidence tax 的 scale-dependency 是论文三大贡献之一（Contribution 1），如果统计上无法排除 zero effect，则该贡献被严重削弱。\n- 建议修改方向：(a) 增加到 n≥5 seeds，至少在 1.7B 和 4B 这两个关键规模上；(b) 如果计算资源有限，将语言从 \"observe\" 改为 \"preliminary evidence suggests\"，并在 abstract 中明确 CI 跨零的事实；(c) 考虑 bootstrap CI 以更好利用有限样本。\n\n**N2** [critical] GRPO 实验中 quantization 与 learning rate 的 confound 未隔离\n- 具体位置：Section 4.3, Table 4 (Appendix A)\n- 问题：GRPO QLoRA（4-bit）和 GRPO bf16 两个配置之间，除了 precision 差异外，Table 4 显示它们的 learning rate、batch size 等超参可能不同。论文将 QLoRA 的 catastrophic collapse（Rel-F1: 1.38）归因于 quantization-induced divergence，并引用 Li et al. (2026)。但如果 lr 也不同，collapse 可能是 lr 过大 + quantization 的联合效应，而非单独的 quantization 问题。论文虽提供了 bf16 G=1 的补充实验（Rel-F1 28.73），但这只控制了 group size，未控制 lr。\n- 为什么影响接收：GRPO catastrophic collapse 是 \"decoupling spectrum\" 叙事的锚点。如果 collapse 的归因不准确，整个 spectrum 框架的可信度降低。\n- 建议修改方向：(a) 在 Table 4 中明确列出 GRPO QLoRA 和 bf16 的完整超参数（尤其 lr、warmup、scheduler）；(b) 做一组 matched-lr 对比（QLoRA lr = bf16 lr）以隔离 quantization 的纯效应；(c) 如无法补充实验，在讨论中明确承认 lr 是 potential confound。\n\n**N3** [critical] DPO 仅测试 β=0.1，\"spectrum\" 结论缺乏支撑\n- 具体位置：Section 4.3（DPO 段落），Table 2\n- 问题：论文将 GRPO（catastrophic）→ DPO（gradual）→ RSFT（stable）描述为一个 \"decoupling spectrum\"（Section 4.3 标题即为 \"Evidence-Extraction Decoupling Spectrum\"）。但 DPO 只测试了 β=0.1 这一个 KL penalty 系数。β 是 DPO 中控制偏离 reference policy 程度的关键超参——小 β 意味着更激进的优化，大 β 更保守。不同 β 下 DPO 的 decoupling 行为可能截然不同：\n  - β=0.5 或 β=1.0 时 DPO 可能表现得更接近 RSFT（保守优化）\n  - β=0.01 时可能更接近 GRPO collapse\n  论文对此完全没有讨论。\n- 为什么影响接收：单一 β 下的 DPO 表现无法支撑 \"DPO 天然位于 spectrum 中间\" 的结论。这可能只是 β=0.1 的特定行为，而非 DPO 方法的固有属性。\n- 建议修改方向：(a) 至少测试 β ∈ {0.01, 0.1, 0.5} 三个点，展示 DPO 在 spectrum 上的位移；(b) 如无法补充实验，大幅弱化 spectrum 叙事，改为 \"under our specific configuration, DPO shows intermediate behavior\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] CED 对比设计的附加价值不明确\n- 具体位置：Section 3.4, Section 4.7\n- 问题：Section 3.4 用了大量篇幅设计 CED 的 contrastive formulation（正样本 vs. entity-sharing distractor），但 Section 4.7 承认 \"CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp)\"。0.02pp 的差异在 n=3 的实验方差范围内是 noise。论文采用 CED 而非 flat-NLI 的理由是 \"per-triple discrimination supports interpretable error analysis\"——但这个解释性优势在正文中没有充分展示（仅 Appendix M 的 3 个 case study 间接涉及）。\n- 建议：(a) 诚实地在 Section 3.4 中前置说明 contrastive formulation 不影响选择质量，主要价值在于可解释性；(b) 削减 Section 3.4 篇幅，将节省的空间用于强化统计分析（如 N1 所建议的更多 seeds）。\n\n**W2** [warning] 14B 仅 1 seed SFT baseline，scaling claim 不可靠\n- 具体位置：Table 3, Section 4.6\n- 问题：Table 3 脚注显示 14B 的 SFT baseline 仅有 1 个 seed（\"1 seed remaining checkpoint\"），而 RSFT 有 3 seeds。这使得 14B 的 evidence tax 估计完全依赖单一数据点，没有任何方差信息。同时，在 test set 上 14B RSFT advantage 消失（Δ=-0.37pp），论文解释为 \"noise or evaluation sensitivity\"（Section 4.4），但无法用 1-seed baseline 来判断这是否是 noise。\n- 建议：补充至少 2 个 14B SFT seeds，或在 scaling discussion 中将 14B 结果标记为 preliminary。\n\n**W3** [warning] RSFT 共享 SFT checkpoint 导致方差比较不公平\n- 具体位置：Section 3.2, Section 4.4, Table 7\n- 问题：SFT 从不同 random seeds 从头训练，variance 包括初始化 + 训练全过程的随机性。RSFT 从同一 SFT checkpoint 出发做 rejection sampling + fine-tuning，variance 仅包括 sampling + fine-tuning 阶段。论文在 Section 4.4 承认 \"SFT reflects full training runs... RSFT reflects additional fine-tuning from a fixed base\"，但没有讨论这对 variance comparison 的 implication——Table 7 中 RSFT 的更窄 CI 可能部分是设计 artifact 而非方法优势。\n- 建议：在讨论 RSFT variance reduction 时明确说明 shared initialization 是一个 contributing factor，区分 \"RSFT 方法本身减少了方差\" 和 \"fixed base 的设计选择减少了方差\"。\n\n**W4** [warning] Test-set evidence tax 在 8B 出现反转，解释不充分\n- 具体位置：Section 4.4（p.7），Table 11 (Appendix F), Figure 6\n- 问题：在 8B 规模上，test set 的 evidence tax 反转为负值（benefit 而非 cost），论文解释为 \"the 8B test tax (−1.17pp) shows slight variations from its near-neutral dev counterpart (+0.04pp)\"。但这个反转恰好发生在 RSFT test-set advantage 也消失的规模上，暗示 test-set 的分布可能与 dev 有系统性差异。Figure 6 也显示 8B 处 SFT 和 RSFT 的 bar 图出现交叉。论文未讨论 dev-test distribution shift 是否是系统性问题。\n- 建议：(a) 报告 dev 和 test 的 document length、relation density 等统计差异；(b) 在 14B 上也检查 test-set tax 以确认是否规模相关。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 第一句 \"Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) methods have surpassed encoder baselines in extraction accuracy\" 缺少引用支撑，建议加上具体 benchmark 和 reference。\n- **M2**: Figure 4 的 y 轴标签（Rel-F1 和 Evi-F1）在打印时可能因规模压缩而难以辨认，建议增大字号。\n- **M3**: Section 2.3 \"Evidence Faithfulness and Rejection Sampling\" 标题暗示 rejection sampling 是关于 faithfulness 的已有工作，但实际引用的 STAR、scaling laws 等工作并非专门针对 evidence faithfulness，标题略有误导。\n- **M4**: Limitations section 提到 \"we have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both\"——这是一个重要的 ablation gap，建议在 future work 中更突出。\n\n---\n\n## Questions to Authors\n\n**Q1**: EDCR 公式中，对于 false-positive triples（无 gold evidence），所有 cited evidence 自动计为 distractor。能否报告 EDCR 仅在 TP triples 上计算的变体结果？这可以分离 \"extraction error\" 和 \"genuine evidence misalignment\" 两个来源。\n\n**Q2**: CED 使用 DeBERTa-v3-base。Appendix B 报告替换为 v3-large 仅差 0.10pp。但是否测试过完全不同的 NLI 架构（如 RoBERTa-large-mnli）或 prompt-based NLI（如用 GPT-4 做 NLI 判断）？如果 CED 对 NLI 模型选择高度 robust，应该明确说明；如果不 robust，这是一个方法论风险。\n\n**Q3**: RSFT 的 top-k=1 selection 策略是否尝试过 k>1？k=1 是最激进的过滤，k=3 或 k=5 可能保留更多多样性同时仍保持质量过滤。这对理解 RSFT 的 \"discrete selection\" 优势机制很重要。\n\n**Q4**: DPO preference pairs 的构造中，最高 CED score 为 preferred，最低为 rejected。如果用 Evi-F1 而非 CED 来构造 preference pairs，DPO 的 decoupling 行为是否变化？这可以区分 DPO 的固有 decoupling tendency 和 CED 信号质量的 contribution。\n\n---\n\n## Missing References\n\n- **Xu et al. (2024) \"Towards Faithful Document-Level Relation Extraction\"** — 如果该工作存在且直接研究 DocRE faithfulness，应被讨论。\n- **DPO β sensitivity** 方面的工作，如 Rafailov et al. (2024) 关于 β 选择对 DPO 行为影响的分析，可以支撑或对比本文的 DPO 实验设计选择。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 = Borderline Conference\n**一句话总结**: 研究问题重要且实验覆盖面广，EDCR 指标设计新颖且验证较充分，但核心 claim（evidence tax 规模依赖性）的统计支撑不足（n=3, CI 跨零），加上 CED 对比设计未带来可衡量收益（0.02pp）以及部分实验 confound 未隔离，削弱了结论的可靠性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 主要 claims 有实验支撑但关键效应的 CI 跨零（evidence tax @ n=3），GRPO 实验存在 lr-quantization confound，DPO 仅单一 β=0.1 |\n| Excitement | 3.5/5 | 研究问题（extraction-evidence trade-off）重要且 under-explored，EDCR 诊断指标有实用价值，但 RSFT 作为方法贡献偏 incremental |\n| Reproducibility | 4/5 | 代码和数据承诺公开，超参数表格完整（Table 4），实验设置描述充分，但部分配置细节（如 GRPO bf16 lr）不够透明 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文和全部附录，DocRE 和 RL alignment 方法论在我的审查范围内 |\n\n---\n\n## 主要优势\n\n**S1. 研究问题定义精准，实用价值高。** 论文准确识别了 LLM-based DocRE 中 evidence grounding 的代价问题——现有方法要么不产出 evidence，要么假设 evidence 免费。将 evidence-extraction trade-off 作为一个显式的研究对象是一个有价值的 framing（Section 1, contributions 1-3）。\n\n**S2. EDCR 指标设计巧妙且验证充分。** EDCR（Eq. 2）作为 extraction-evidence decoupling 的诊断工具，概念清晰且有实际用途。Appendix L 的验证非常充分：partial correlation 控制 TP 后相关性仅下降 0.15%（ρ: -0.8541 → -0.8551），10,000 次 permutation test 确认 p<0.0001，per-relation 分析（n=76, ρ=-0.79）与 cross-method 分析（n=17）一致。这是论文最扎实的贡献。\n\n**S3. 三范式系统对比框架有参考价值。** 将 GRPO、DPO、RSFT 统一在同一 SFT baseline、同一评估协议下对比，并用 Table 1 清晰概括三者的信号类型和训练机制差异，对 practitioner 选择后训练策略有直接指导意义。\n\n**S4. 跨模型家族和跨规模验证增强了发现的可推广性。** 在 4 个 Qwen3 规模（1.7B-14B）和 LLaMA-3.1-8B 上的交叉验证（Table 3, Appendix H）显示 RSFT 的核心模式在不同架构上一致。\n\n**S5. 附录质量高。** 14 个附录覆盖了消融、统计验证、error decomposition、定性分析等，显示了严谨的研究态度。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] n=3 seeds 的统计效力不足以支撑核心 claim\n- 具体位置：Section 4.4, Table 7 (Appendix D), Section 4.2\n- 问题：论文承认 \"CI crosses zero at n=3\"（p.7），但仍在 abstract 和 contributions 中将 evidence tax 描述为已确立的现象（\"We observe a scale-dependent evidence tax\"）。对于 3 个 seeds：\n  - Sign test 最小 p-value = 0.0625，无法达到任何常规显著性水平\n  - Table 7 的 95% CI 均极宽，多个配置的 RSFT gain CI 确实跨零\n  - 1.7B 的 s42 是最强 seed（+3.22pp above mean），在 n=3 中有 disproportionate influence\n- 为什么影响接收：evidence tax 的 scale-dependency 是论文三大贡献之一（Contribution 1），如果统计上无法排除 zero effect，则该贡献被严重削弱。\n- 建议修改方向：(a) 增加到 n≥5 seeds，至少在 1.7B 和 4B 这两个关键规模上；(b) 如果计算资源有限，将语言从 \"observe\" 改为 \"preliminary evidence suggests\"，并在 abstract 中明确 CI 跨零的事实；(c) 考虑 bootstrap CI 以更好利用有限样本。\n\n**N2** [critical] GRPO 实验中 quantization 与 learning rate 的 confound 未隔离\n- 具体位置：Section 4.3, Table 4 (Appendix A)\n- 问题：GRPO QLoRA（4-bit）和 GRPO bf16 两个配置之间，除了 precision 差异外，Table 4 显示它们的 learning rate、batch size 等超参可能不同。论文将 QLoRA 的 catastrophic collapse（Rel-F1: 1.38）归因于 quantization-induced divergence，并引用 Li et al. (2026)。但如果 lr 也不同，collapse 可能是 lr 过大 + quantization 的联合效应，而非单独的 quantization 问题。论文虽提供了 bf16 G=1 的补充实验（Rel-F1 28.73），但这只控制了 group size，未控制 lr。\n- 为什么影响接收：GRPO catastrophic collapse 是 \"decoupling spectrum\" 叙事的锚点。如果 collapse 的归因不准确，整个 spectrum 框架的可信度降低。\n- 建议修改方向：(a) 在 Table 4 中明确列出 GRPO QLoRA 和 bf16 的完整超参数（尤其 lr、warmup、scheduler）；(b) 做一组 matched-lr 对比（QLoRA lr = bf16 lr）以隔离 quantization 的纯效应；(c) 如无法补充实验，在讨论中明确承认 lr 是 potential confound。\n\n**N3** [critical] DPO 仅测试 β=0.1，\"spectrum\" 结论缺乏支撑\n- 具体位置：Section 4.3（DPO 段落），Table 2\n- 问题：论文将 GRPO（catastrophic）→ DPO（gradual）→ RSFT（stable）描述为一个 \"decoupling spectrum\"（Section 4.3 标题即为 \"Evidence-Extraction Decoupling Spectrum\"）。但 DPO 只测试了 β=0.1 这一个 KL penalty 系数。β 是 DPO 中控制偏离 reference policy 程度的关键超参——小 β 意味着更激进的优化，大 β 更保守。不同 β 下 DPO 的 decoupling 行为可能截然不同：\n  - β=0.5 或 β=1.0 时 DPO 可能表现得更接近 RSFT（保守优化）\n  - β=0.01 时可能更接近 GRPO collapse\n  论文对此完全没有讨论。\n- 为什么影响接收：单一 β 下的 DPO 表现无法支撑 \"DPO 天然位于 spectrum 中间\" 的结论。这可能只是 β=0.1 的特定行为，而非 DPO 方法的固有属性。\n- 建议修改方向：(a) 至少测试 β ∈ {0.01, 0.1, 0.5} 三个点，展示 DPO 在 spectrum 上的位移；(b) 如无法补充实验，大幅弱化 spectrum 叙事，改为 \"under our specific configuration, DPO shows intermediate behavior\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] CED 对比设计的附加价值不明确\n- 具体位置：Section 3.4, Section 4.7\n- 问题：Section 3.4 用了大量篇幅设计 CED 的 contrastive formulation（正样本 vs. entity-sharing distractor），但 Section 4.7 承认 \"CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp)\"。0.02pp 的差异在 n=3 的实验方差范围内是 noise。论文采用 CED 而非 flat-NLI 的理由是 \"per-triple discrimination supports interpretable error analysis\"——但这个解释性优势在正文中没有充分展示（仅 Appendix M 的 3 个 case study 间接涉及）。\n- 建议：(a) 诚实地在 Section 3.4 中前置说明 contrastive formulation 不影响选择质量，主要价值在于可解释性；(b) 削减 Section 3.4 篇幅，将节省的空间用于强化统计分析（如 N1 所建议的更多 seeds）。\n\n**W2** [warning] 14B 仅 1 seed SFT baseline，scaling claim 不可靠\n- 具体位置：Table 3, Section 4.6\n- 问题：Table 3 脚注显示 14B 的 SFT baseline 仅有 1 个 seed（\"1 seed remaining checkpoint\"），而 RSFT 有 3 seeds。这使得 14B 的 evidence tax 估计完全依赖单一数据点，没有任何方差信息。同时，在 test set 上 14B RSFT advantage 消失（Δ=-0.37pp），论文解释为 \"noise or evaluation sensitivity\"（Section 4.4），但无法用 1-seed baseline 来判断这是否是 noise。\n- 建议：补充至少 2 个 14B SFT seeds，或在 scaling discussion 中将 14B 结果标记为 preliminary。\n\n**W3** [warning] RSFT 共享 SFT checkpoint 导致方差比较不公平\n- 具体位置：Section 3.2, Section 4.4, Table 7\n- 问题：SFT 从不同 random seeds 从头训练，variance 包括初始化 + 训练全过程的随机性。RSFT 从同一 SFT checkpoint 出发做 rejection sampling + fine-tuning，variance 仅包括 sampling + fine-tuning 阶段。论文在 Section 4.4 承认 \"SFT reflects full training runs... RSFT reflects additional fine-tuning from a fixed base\"，但没有讨论这对 variance comparison 的 implication——Table 7 中 RSFT 的更窄 CI 可能部分是设计 artifact 而非方法优势。\n- 建议：在讨论 RSFT variance reduction 时明确说明 shared initialization 是一个 contributing factor，区分 \"RSFT 方法本身减少了方差\" 和 \"fixed base 的设计选择减少了方差\"。\n\n**W4** [warning] Test-set evidence tax 在 8B 出现反转，解释不充分\n- 具体位置：Section 4.4（p.7），Table 11 (Appendix F), Figure 6\n- 问题：在 8B 规模上，test set 的 evidence tax 反转为负值（benefit 而非 cost），论文解释为 \"the 8B test tax (−1.17pp) shows slight variations from its near-neutral dev counterpart (+0.04pp)\"。但这个反转恰好发生在 RSFT test-set advantage 也消失的规模上，暗示 test-set 的分布可能与 dev 有系统性差异。Figure 6 也显示 8B 处 SFT 和 RSFT 的 bar 图出现交叉。论文未讨论 dev-test distribution shift 是否是系统性问题。\n- 建议：(a) 报告 dev 和 test 的 document length、relation density 等统计差异；(b) 在 14B 上也检查 test-set tax 以确认是否规模相关。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 第一句 \"Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) methods have surpassed encoder baselines in extraction accuracy\" 缺少引用支撑，建议加上具体 benchmark 和 reference。\n- **M2**: Figure 4 的 y 轴标签（Rel-F1 和 Evi-F1）在打印时可能因规模压缩而难以辨认，建议增大字号。\n- **M3**: Section 2.3 \"Evidence Faithfulness and Rejection Sampling\" 标题暗示 rejection sampling 是关于 faithfulness 的已有工作，但实际引用的 STAR、scaling laws 等工作并非专门针对 evidence faithfulness，标题略有误导。\n- **M4**: Limitations section 提到 \"we have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both\"——这是一个重要的 ablation gap，建议在 future work 中更突出。\n\n---\n\n## Questions to Authors\n\n**Q1**: EDCR 公式中，对于 false-positive triples（无 gold evidence），所有 cited evidence 自动计为 distractor。能否报告 EDCR 仅在 TP triples 上计算的变体结果？这可以分离 \"extraction error\" 和 \"genuine evidence misalignment\" 两个来源。\n\n**Q2**: CED 使用 DeBERTa-v3-base。Appendix B 报告替换为 v3-large 仅差 0.10pp。但是否测试过完全不同的 NLI 架构（如 RoBERTa-large-mnli）或 prompt-based NLI（如用 GPT-4 做 NLI 判断）？如果 CED 对 NLI 模型选择高度 robust，应该明确说明；如果不 robust，这是一个方法论风险。\n\n**Q3**: RSFT 的 top-k=1 selection 策略是否尝试过 k>1？k=1 是最激进的过滤，k=3 或 k=5 可能保留更多多样性同时仍保持质量过滤。这对理解 RSFT 的 \"discrete selection\" 优势机制很重要。\n\n**Q4**: DPO preference pairs 的构造中，最高 CED score 为 preferred，最低为 rejected。如果用 Evi-F1 而非 CED 来构造 preference pairs，DPO 的 decoupling 行为是否变化？这可以区分 DPO 的固有 decoupling tendency 和 CED 信号质量的 contribution。\n\n---\n\n## Missing References\n\n- **Xu et al. (2024) \"Towards Faithful Document-Level Relation Extraction\"** — 如果该工作存在且直接研究 DocRE faithfulness，应被讨论。\n- **DPO β sensitivity** 方面的工作，如 Rafailov et al. (2024) 关于 β 选择对 DPO 行为影响的分析，可以支撑或对比本文的 DPO 实验设计选择。",
    "reviewer_id": "1",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 297 · 2026-05-25T22:37:15.445408+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---

### Tool call

_source line 298 · 2026-05-25T22:37:20.375944+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 299 · 2026-05-25T22:37:20.426716+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 300 · 2026-05-25T22:37:25.097134+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 301 · 2026-05-25T22:37:25.147814+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 302 · 2026-05-25T22:37:37.086132+00:00_

Round 1 审稿完成。总结：

- **Overall: 3.5（Borderline Conference）**
- **Soundness: 3.0** — n=3 seeds 的 CI 跨零削弱 evidence tax 核心 claim；GRPO 实验有 lr-quantization confound；DPO 仅 β=0.1 不足以支撑 spectrum 结论
- **Excitement: 3.5** — 研究问题有实用价值，EDCR 指标设计新颖且验证充分，但 RSFT 方法贡献偏 incremental

**3 个 Must-Fix**：(N1) 统计效力不足，需增加 seeds 或弱化 claim 语言；(N2) GRPO QLoRA vs bf16 需隔离 lr confound；(N3) DPO 需测试多个 β 值或弱化 spectrum 叙事

**4 个 Should-Fix**：CED 0.02pp 附加价值不明确、14B 单 seed baseline、RSFT 共享 checkpoint 的方差比较不公平、8B test-set tax 反转解释不充分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---

## Round 8

18 recorded events

### User

_source line 303 · 2026-05-25T22:40:28.809047+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见

**Overall: 3.5 (Borderline Conference)**
**Soundness: 3.5/5 | Excitement: 3.0/5 | Reproducibility: 4/5 | Confidence: 4/5**

### 主要优势
1. 实验规模高水平（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture）
2. 研究问题定义清晰——extraction-evidence trade-off 有真实痛点
3. EDCR 的 per-relation 诊断价值（Figure 8, Appendix L）
4. Error decomposition 分析有深度（Appendix K, Table 15）
5. Cross-architecture 泛化一致性强
6. Qualitative analysis 信息量高（Appendix M）

### Must-Fix
**N1** [critical] 核心新颖性不足——
(1) RSFT = STaR + CED 筛选，是 engineering contribution 非 methodological innovation
(2) CED vs flat-NLI 仅差 0.02pp，contrastive formulation "not essential"
(3) EDCR 是简单比率（1 − precision(evidence|relation)），需跨 backbone 验证
(4) Evidence tax 主要来自 truncation/duplication（Appendix K），非 evidence 固有代价——应区分 "truncation-induced tax" 和 "information-interference tax"

**N2** [critical] 优化超参数探索不充分——DPO 仅 β=0.1，GRPO 仅 G=8，RSFT 仅 k=1，无超参数敏感性分析支撑 "gradient methods inherently decouple" 归因。

**N3** [critical] Conclusion 过于简短（~60 words, 3 句话）——缺 broader implications、future directions、connection to wider literature。对 empirical study 而言 Conclusion 是 reviewer 判断工作意义的关键段落。

### Should-Fix
**W1** Related Work 遗漏 MTL / gradient conflict 文献（PCGrad Yu et al. 2020, Reward overoptimization Gao et al. 2023）。
**W2** EDCR 与 CED 共享 NLI backbone，存在 circular dependency 风险——需跨 backbone 稳定性验证。
**W3** §4.4 信息密度过高——scaling pattern、variance、cross-arch 堆叠在 1.5 页内，建议拆分。
**W4** "Evidence tax" 术语 framing 反直觉——negative tax = benefit 不自然，建议改 "evidence delta/impact"。
**W5** Re-DocRED test 20pp drop 归因于 annotation density，但解释不充分——是否意味模型在 sparse-annotation 下基本失效？

### Minor
M1: Table 2 caption 缩写未展开。M2: "co-optimization"/"joint optimization" 未统一。M3: Appendix E 的 matched@2048 定义应移入正文。M4: Figure 4 dual y-axis 可能视觉误导。

### Missing References
1. Yu et al. (2020, NeurIPS) "Gradient Surgery for Multi-Task Learning"
2. Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization"
3. Maynez et al. (2020, ACL) "On Faithfulness and Factuality in Abstractive Summarization"
4. Rashkin et al. (2023, TACL) "Measuring Attribution in NLG Models"

### Questions
Q1: RoBERTa-large-MNLI 替换 EDCR NLI backbone 后 correlation 是否稳定？
Q2: Truncation 对 evidence tax 贡献多大？non-truncated outputs 的 1.7B tax 是否仍存在？
Q3: DPO β=0.01 和 β=0.5 的 EDCR？
Q4: RSFT k>1 效果？
Q5: 14B cross-seed variance 异常高是否暗示 evidence tax 在更大规模不稳定？

---

请逐条回应以上每个要点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 304 · 2026-05-25T22:41:55.538453+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
  "pages": "5,8,12,13,16",
  "project": "faith-evidence-ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
    "pages": "5,8,12,13,16",
    "project": "faith-evidence-ie",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 305 · 2026-05-25T22:41:56.292468+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 377.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.3}], \"total_pages\": 18, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 754
}
```

</details>

---

### Tool call

_source line 306 · 2026-05-25T22:42:03.973574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 307 · 2026-05-25T22:42:04.425740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 308 · 2026-05-25T22:42:05.384042+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---

### Tool result

_source line 309 · 2026-05-25T22:42:05.385858+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---

### Tool call

_source line 310 · 2026-05-25T22:42:05.386291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 311 · 2026-05-25T22:42:05.841380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 312 · 2026-05-25T22:42:05.842417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool call

_source line 313 · 2026-05-25T22:42:06.244467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 314 · 2026-05-25T22:42:06.446936+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---

### Tool result

_source line 315 · 2026-05-25T22:42:07.002426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---

### Tool call

_source line 316 · 2026-05-25T22:44:22.614397+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with nuance] R2-N1(1): RSFT = STaR + CED，是 engineering contribution**\n同意 RSFT 本身不是方法论创新——rejection sampling fine-tuning 和 NLI-based scoring 都是已有技术。但论文的主要贡献定位是 empirical study（extraction-evidence trade-off 的系统刻画），RSFT 是三个范式之一而非核心方法贡献。问题在于 Contribution 3 的措辞（\"RSFT improves extraction without decoupling\"）确实将 RSFT 包装得过于像 method contribution。建议作者将 RSFT 的角色明确为 \"empirical finding: discrete selection avoids decoupling\" 而非暗示方法新颖性。\n\n**[AGREE] R2-N1(2): CED vs flat-NLI 仅差 0.02pp**\n完全同意。我在自己的 W1 中也标记了这一问题。Section 3.4 投入了大量篇幅设计 contrastive formulation，但 Section 4.7 自己承认 \"the contrastive formulation is not essential for data selection quality\"。这是论文中 effort-vs-payoff 最失衡的部分。\n\n**[REBUT] R2-N1(3): EDCR 需跨 backbone 验证**\nR2 的前提有误。EDCR（Eq. 2, Section 3.5）的定义是 Σ|E_i^pred \\ E_i^gold| / Σ|E_i^pred|——纯粹比较模型预测的 evidence sentences 与 gold annotations，**不使用任何 NLI model**。EDCR 是 annotation-based 的诊断指标，与 NLI backbone 完全无关。R2 可能将 EDCR 与 CED（Section 3.4, 使用 DeBERTa-v3-base NLI）混淆了。因此\"跨 backbone 验证\"这一要求对 EDCR 不适用。EDCR 的验证在 Appendix L 中通过 partial correlation、permutation test 和 per-relation 分析完成，且这些验证同样不依赖 NLI backbone。\n\n**[AGREE, 这是本轮最有力的批评之一] R2-N1(4): Evidence tax 主要来自 truncation/duplication**\n强烈同意。这是 R2 审稿中最锐利的洞察。论文自己在 Appendix E（Table 9）提供了关键证据：在 matched@2048 fair evaluation 控制了 truncation 率后，1.7B 的 evidence tax **反转为 -5.63pp（beneficial）**，≥4B 近似中性（+0.25±0.47pp）。Appendix K（Table 15）的 error decomposition 进一步确认 truncation FN 是 RSFT 改进的首要机制（1.7B: +811 truncation FN reduction, −275%）。\n\n这意味着：**论文 abstract 和 Contribution 1 中宣称的 \"scale-dependent evidence tax\" 在 1.7B（效应最显著的规模）实质上是 truncation artifact 而非 evidence 固有代价。** 当控制 output format compliance 后，evidence grounding 在 1.7B 是有益的。论文将 truncation-mediated 的格式限制效应包装为 \"evidence tax\" 是 framing 上的过度简化。\n\n建议作者在正文中引入 \"truncation-induced tax\" 和 \"information-interference tax\" 的区分（如 R2 所建议），并将 Appendix E 的关键发现（matched@2048 结果）提升到正文 Section 4.4。\n\n**[AGREE] R2-N2: 超参数探索不充分**\n同意。我在自己的 N3 中已标记 DPO β=0.1 单一设定的问题。R2 进一步指出 GRPO G=8 和 RSFT k=1 也是单点配置，使得 \"gradient methods inherently decouple\" 的归因缺乏超参数敏感性支撑。特别是：\n- DPO β 直接控制偏离 reference policy 的力度，不同 β 下 decoupling 行为可能质变\n- RSFT k=1 是最激进的过滤策略，k=3 或 k=5 可能有不同的 extraction-evidence balance\n缺少这些消融，论文无法区分 \"方法固有属性\" 和 \"特定超参下的行为\"。\n\n**[REBUT] R2-N3: Conclusion 过于简短 → 应降级为 Should-Fix**\n不同意将此列为 Must-Fix/critical。Section 5 确实只有约 60 words，但：\n1. ARR review form 的 soundness 和 excitement 评分标准中不包含 \"conclusion 长度\" 维度\n2. 论文的 broader implications 和 future directions 已在 Section 4.7 Discussion 中讨论（EDCR 的诊断价值、evidence generation 的推理时间影响、inference overhead analysis reference to Appendix N）\n3. Limitations section（p.9）覆盖了 scope、CED sensitivity、RSFT 机制解耦等反思\n\n简短 conclusion 是写作风格偏好，不是 soundness 缺陷。我同意可以适当扩充（加 2-3 句 future directions），但这不应影响接收决定。建议降为 Should-Fix。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 遗漏 MTL/gradient conflict 文献**\n同意。论文在 Section 4.3 详细讨论了 gradient pressure 导致 evidence-extraction decoupling，这本质上是一个 multi-task gradient conflict 问题。PCGrad（Yu et al. 2020）提出了梯度手术来解决任务间梯度冲突，直接相关。Gao et al. 2023 的 reward overoptimization scaling laws 与 GRPO 的 collapse 行为也有理论联系。这些引用的缺失使得 Related Work 2.2 的理论基础显得薄弱。\n\n**[REBUT] R2-W2: EDCR 与 CED 共享 NLI backbone，circular dependency**\n如 N1(3) 的回应所述，这是事实性错误。EDCR（Eq. 2）完全不使用 NLI——它是 gold annotation vs. predicted evidence 的集合差运算。CED（Section 3.4）使用 DeBERTa-v3-base NLI 进行 training data selection。两者没有共享组件，不存在 circular dependency。\n\n具体地：\n- **CED** 在训练阶段使用：SFT model → sample N outputs → CED(NLI) scores → select top-k → fine-tune\n- **EDCR** 在评估阶段使用：trained model → predict on test set → compare E_pred vs E_gold → compute ratio\n两个指标在 pipeline 中的位置完全不同（训练 vs. 评估），输入也不同（NLI logits vs. gold labels）。\n\n**[AGREE] R2-W3: §4.4 信息密度过高**\n同意。Section 4.4 在约 1.5 页内叠加了 evidence tax 定义、scale-dependency、CI 分析、cross-seed variance、cross-architecture validation、inference-time tax 等多个层面。尤其 evidence tax 的 CI 跨零这个关键 caveat 容易被淹没在密集文本中。建议拆分为 §4.4 Evidence Tax（含 CI 讨论）和 §4.5 Cross-Scale and Cross-Architecture Patterns。\n\n**[REBUT] R2-W4: \"Evidence tax\" 术语不直观**\n不同意。\"Tax\" 在经济学和 CS 中是标准隐喻，表示附加特性的代价（如 \"abstraction tax\"、\"safety tax\"）。Negative tax = benefit 符合直觉——如果你的 \"税\" 算出来是负的，你就是在赚钱而不是亏钱。\"Evidence delta\" 是方向中性的，丢失了论文核心叙事中 \"evidence 有代价\" 的预设检验框架。\"Impact\" 优于 \"delta\" 但不如 \"tax\" 精准。该术语选择是合理的。\n\n**[AGREE] R2-W5: Re-DocRED test 20pp drop 解释不充分**\n同意。论文将 Re-DocRED test 的大幅性能下降归因于 annotation density 差异（Section 4.6 提到 \"annotation density\"），但没有提供定量支撑（如 dev vs. test 的 average relations per document、evidence sentence coverage 等统计对比）。这个 drop 如果是系统性的，暗示模型对 annotation density 高度敏感，这对实际部署有重要 implication。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1**: Table 2 caption 确实有缩写未展开（如 \"sd\" 在脚注说明但不够显眼）。\n**[AGREE] R2-M2**: \"co-optimization\" 和 \"joint optimization\" 术语未统一，应选定一个。\n**[AGREE] R2-M3**: matched@2048 的定义在 Appendix E，但 Section 4.4 引用时读者需翻到附录才能理解。鉴于 matched@2048 对理解 evidence tax 至关重要（见 N1(4)），至少应在正文加一句定义。\n**[AGREE] R2-M4**: Figure 4 dual y-axis 确实存在视觉误导风险——Rel-F1（40-55 range）和 Evi-F1（0-90 range）共用图面时，Rel-F1 的微小变化被放大。建议改为并排子图。\n\n---\n\n### Missing References\n\n**[AGREE] Yu et al. 2020 PCGrad**: 直接相关，如 W1 所述。\n**[AGREE] Gao et al. 2023 Reward Overoptimization Scaling Laws**: 与 GRPO collapse 现象有理论联系。\n**[REBUT] Maynez et al. 2020**: 该工作研究 abstractive summarization 的 faithfulness，与 DocRE 的 evidence grounding 问题关联较远。论文已引用了更相关的 faithfulness 文献（Laban et al. 2022, Zhang et al. 2024 在 NLI-based faithfulness evaluation 领域）。\n**[AGREE] Rashkin et al. 2023**: Attribution in NLG 与本文的 evidence citation 框架有概念对应关系，值得在 Related Work 2.3 中讨论。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1**: 与我的 Q2 重合。跨 NLI backbone 对 CED（非 EDCR）的鲁棒性验证是必要的。\n**[AGREE, 关键问题] R2-Q2**: Appendix E 的 matched@2048 分析部分回答了这个问题——控制 truncation 后 1.7B tax 反转。但论文应在正文显著位置报告 non-truncated outputs 的纯 evidence tax，而非埋在附录中。\n**[AGREE] R2-Q3**: 与我的 N3 重合。DPO β sensitivity 是支撑 spectrum claim 的必要实验。\n**[AGREE] R2-Q4**: 与我的 Q3 重合。RSFT k>1 的消融对理解 discrete selection 机制很重要。\n**[AGREE] R2-Q5**: 14B 的高 cross-seed variance 加上仅 1 seed SFT baseline（我的 W2），确实暗示 evidence tax 在更大规模可能不稳定。这需要更多 seeds 来确认。\n\n---\n\n### 总结\n\nR2 的审稿中最有价值的贡献是 **N1(4)**：evidence tax 的 truncation-mediation 机制。这一观点得到论文自己 Appendix E 和 K 的数据支撑，但论文正文的 framing 没有充分反映这一关键 nuance。\n\nR2 的主要事实性错误是 **W2**：EDCR 和 CED 不共享 NLI backbone，不存在 circular dependency。\n\nR2 将 Conclusion 长度列为 critical 我认为过重——这是写作偏好而非 soundness 问题。\n\n综合 R2 的意见，我维持自己的 Overall 3.5（Borderline Conference）不变。N1(4) 的 truncation-mediation 论点加强了我对 evidence tax claim 统计支撑不足的担忧（我的 N1），但 EDCR 的扎实验证和 RSFT 跨规模一致性仍有 Findings-level 贡献。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with nuance] R2-N1(1): RSFT = STaR + CED，是 engineering contribution**\n同意 RSFT 本身不是方法论创新——rejection sampling fine-tuning 和 NLI-based scoring 都是已有技术。但论文的主要贡献定位是 empirical study（extraction-evidence trade-off 的系统刻画），RSFT 是三个范式之一而非核心方法贡献。问题在于 Contribution 3 的措辞（\"RSFT improves extraction without decoupling\"）确实将 RSFT 包装得过于像 method contribution。建议作者将 RSFT 的角色明确为 \"empirical finding: discrete selection avoids decoupling\" 而非暗示方法新颖性。\n\n**[AGREE] R2-N1(2): CED vs flat-NLI 仅差 0.02pp**\n完全同意。我在自己的 W1 中也标记了这一问题。Section 3.4 投入了大量篇幅设计 contrastive formulation，但 Section 4.7 自己承认 \"the contrastive formulation is not essential for data selection quality\"。这是论文中 effort-vs-payoff 最失衡的部分。\n\n**[REBUT] R2-N1(3): EDCR 需跨 backbone 验证**\nR2 的前提有误。EDCR（Eq. 2, Section 3.5）的定义是 Σ|E_i^pred \\ E_i^gold| / Σ|E_i^pred|——纯粹比较模型预测的 evidence sentences 与 gold annotations，**不使用任何 NLI model**。EDCR 是 annotation-based 的诊断指标，与 NLI backbone 完全无关。R2 可能将 EDCR 与 CED（Section 3.4, 使用 DeBERTa-v3-base NLI）混淆了。因此\"跨 backbone 验证\"这一要求对 EDCR 不适用。EDCR 的验证在 Appendix L 中通过 partial correlation、permutation test 和 per-relation 分析完成，且这些验证同样不依赖 NLI backbone。\n\n**[AGREE, 这是本轮最有力的批评之一] R2-N1(4): Evidence tax 主要来自 truncation/duplication**\n强烈同意。这是 R2 审稿中最锐利的洞察。论文自己在 Appendix E（Table 9）提供了关键证据：在 matched@2048 fair evaluation 控制了 truncation 率后，1.7B 的 evidence tax **反转为 -5.63pp（beneficial）**，≥4B 近似中性（+0.25±0.47pp）。Appendix K（Table 15）的 error decomposition 进一步确认 truncation FN 是 RSFT 改进的首要机制（1.7B: +811 truncation FN reduction, −275%）。\n\n这意味着：**论文 abstract 和 Contribution 1 中宣称的 \"scale-dependent evidence tax\" 在 1.7B（效应最显著的规模）实质上是 truncation artifact 而非 evidence 固有代价。** 当控制 output format compliance 后，evidence grounding 在 1.7B 是有益的。论文将 truncation-mediated 的格式限制效应包装为 \"evidence tax\" 是 framing 上的过度简化。\n\n建议作者在正文中引入 \"truncation-induced tax\" 和 \"information-interference tax\" 的区分（如 R2 所建议），并将 Appendix E 的关键发现（matched@2048 结果）提升到正文 Section 4.4。\n\n**[AGREE] R2-N2: 超参数探索不充分**\n同意。我在自己的 N3 中已标记 DPO β=0.1 单一设定的问题。R2 进一步指出 GRPO G=8 和 RSFT k=1 也是单点配置，使得 \"gradient methods inherently decouple\" 的归因缺乏超参数敏感性支撑。特别是：\n- DPO β 直接控制偏离 reference policy 的力度，不同 β 下 decoupling 行为可能质变\n- RSFT k=1 是最激进的过滤策略，k=3 或 k=5 可能有不同的 extraction-evidence balance\n缺少这些消融，论文无法区分 \"方法固有属性\" 和 \"特定超参下的行为\"。\n\n**[REBUT] R2-N3: Conclusion 过于简短 → 应降级为 Should-Fix**\n不同意将此列为 Must-Fix/critical。Section 5 确实只有约 60 words，但：\n1. ARR review form 的 soundness 和 excitement 评分标准中不包含 \"conclusion 长度\" 维度\n2. 论文的 broader implications 和 future directions 已在 Section 4.7 Discussion 中讨论（EDCR 的诊断价值、evidence generation 的推理时间影响、inference overhead analysis reference to Appendix N）\n3. Limitations section（p.9）覆盖了 scope、CED sensitivity、RSFT 机制解耦等反思\n\n简短 conclusion 是写作风格偏好，不是 soundness 缺陷。我同意可以适当扩充（加 2-3 句 future directions），但这不应影响接收决定。建议降为 Should-Fix。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 遗漏 MTL/gradient conflict 文献**\n同意。论文在 Section 4.3 详细讨论了 gradient pressure 导致 evidence-extraction decoupling，这本质上是一个 multi-task gradient conflict 问题。PCGrad（Yu et al. 2020）提出了梯度手术来解决任务间梯度冲突，直接相关。Gao et al. 2023 的 reward overoptimization scaling laws 与 GRPO 的 collapse 行为也有理论联系。这些引用的缺失使得 Related Work 2.2 的理论基础显得薄弱。\n\n**[REBUT] R2-W2: EDCR 与 CED 共享 NLI backbone，circular dependency**\n如 N1(3) 的回应所述，这是事实性错误。EDCR（Eq. 2）完全不使用 NLI——它是 gold annotation vs. predicted evidence 的集合差运算。CED（Section 3.4）使用 DeBERTa-v3-base NLI 进行 training data selection。两者没有共享组件，不存在 circular dependency。\n\n具体地：\n- **CED** 在训练阶段使用：SFT model → sample N outputs → CED(NLI) scores → select top-k → fine-tune\n- **EDCR** 在评估阶段使用：trained model → predict on test set → compare E_pred vs E_gold → compute ratio\n两个指标在 pipeline 中的位置完全不同（训练 vs. 评估），输入也不同（NLI logits vs. gold labels）。\n\n**[AGREE] R2-W3: §4.4 信息密度过高**\n同意。Section 4.4 在约 1.5 页内叠加了 evidence tax 定义、scale-dependency、CI 分析、cross-seed variance、cross-architecture validation、inference-time tax 等多个层面。尤其 evidence tax 的 CI 跨零这个关键 caveat 容易被淹没在密集文本中。建议拆分为 §4.4 Evidence Tax（含 CI 讨论）和 §4.5 Cross-Scale and Cross-Architecture Patterns。\n\n**[REBUT] R2-W4: \"Evidence tax\" 术语不直观**\n不同意。\"Tax\" 在经济学和 CS 中是标准隐喻，表示附加特性的代价（如 \"abstraction tax\"、\"safety tax\"）。Negative tax = benefit 符合直觉——如果你的 \"税\" 算出来是负的，你就是在赚钱而不是亏钱。\"Evidence delta\" 是方向中性的，丢失了论文核心叙事中 \"evidence 有代价\" 的预设检验框架。\"Impact\" 优于 \"delta\" 但不如 \"tax\" 精准。该术语选择是合理的。\n\n**[AGREE] R2-W5: Re-DocRED test 20pp drop 解释不充分**\n同意。论文将 Re-DocRED test 的大幅性能下降归因于 annotation density 差异（Section 4.6 提到 \"annotation density\"），但没有提供定量支撑（如 dev vs. test 的 average relations per document、evidence sentence coverage 等统计对比）。这个 drop 如果是系统性的，暗示模型对 annotation density 高度敏感，这对实际部署有重要 implication。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1**: Table 2 caption 确实有缩写未展开（如 \"sd\" 在脚注说明但不够显眼）。\n**[AGREE] R2-M2**: \"co-optimization\" 和 \"joint optimization\" 术语未统一，应选定一个。\n**[AGREE] R2-M3**: matched@2048 的定义在 Appendix E，但 Section 4.4 引用时读者需翻到附录才能理解。鉴于 matched@2048 对理解 evidence tax 至关重要（见 N1(4)），至少应在正文加一句定义。\n**[AGREE] R2-M4**: Figure 4 dual y-axis 确实存在视觉误导风险——Rel-F1（40-55 range）和 Evi-F1（0-90 range）共用图面时，Rel-F1 的微小变化被放大。建议改为并排子图。\n\n---\n\n### Missing References\n\n**[AGREE] Yu et al. 2020 PCGrad**: 直接相关，如 W1 所述。\n**[AGREE] Gao et al. 2023 Reward Overoptimization Scaling Laws**: 与 GRPO collapse 现象有理论联系。\n**[REBUT] Maynez et al. 2020**: 该工作研究 abstractive summarization 的 faithfulness，与 DocRE 的 evidence grounding 问题关联较远。论文已引用了更相关的 faithfulness 文献（Laban et al. 2022, Zhang et al. 2024 在 NLI-based faithfulness evaluation 领域）。\n**[AGREE] Rashkin et al. 2023**: Attribution in NLG 与本文的 evidence citation 框架有概念对应关系，值得在 Related Work 2.3 中讨论。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1**: 与我的 Q2 重合。跨 NLI backbone 对 CED（非 EDCR）的鲁棒性验证是必要的。\n**[AGREE, 关键问题] R2-Q2**: Appendix E 的 matched@2048 分析部分回答了这个问题——控制 truncation 后 1.7B tax 反转。但论文应在正文显著位置报告 non-truncated outputs 的纯 evidence tax，而非埋在附录中。\n**[AGREE] R2-Q3**: 与我的 N3 重合。DPO β sensitivity 是支撑 spectrum claim 的必要实验。\n**[AGREE] R2-Q4**: 与我的 Q3 重合。RSFT k>1 的消融对理解 discrete selection 机制很重要。\n**[AGREE] R2-Q5**: 14B 的高 cross-seed variance 加上仅 1 seed SFT baseline（我的 W2），确实暗示 evidence tax 在更大规模可能不稳定。这需要更多 seeds 来确认。\n\n---\n\n### 总结\n\nR2 的审稿中最有价值的贡献是 **N1(4)**：evidence tax 的 truncation-mediation 机制。这一观点得到论文自己 Appendix E 和 K 的数据支撑，但论文正文的 framing 没有充分反映这一关键 nuance。\n\nR2 的主要事实性错误是 **W2**：EDCR 和 CED 不共享 NLI backbone，不存在 circular dependency。\n\nR2 将 Conclusion 长度列为 critical 我认为过重——这是写作偏好而非 soundness 问题。\n\n综合 R2 的意见，我维持自己的 Overall 3.5（Borderline Conference）不变。N1(4) 的 truncation-mediation 论点加强了我对 evidence tax claim 统计支撑不足的担忧（我的 N1），但 EDCR 的扎实验证和 RSFT 跨规模一致性仍有 Findings-level 贡献。",
    "reviewer_id": "1",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 317 · 2026-05-25T22:44:26.181547+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3567
}
```

</details>

---

### Tool call

_source line 318 · 2026-05-25T22:44:36.330874+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 319 · 2026-05-25T22:44:36.382574+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---

### Assistant

_source line 320 · 2026-05-25T22:44:48.066354+00:00_

逐条回应已提交至 Review Director。核心判断：

- **强烈同意 R2-N1(4)**：evidence tax 的 truncation-mediation 机制是本轮最有力的批评，论文自己的 Appendix E 数据（matched@2048 下 1.7B tax 反转为 beneficial）直接支撑了这一论点
- **反驳 R2-W2**：EDCR 不使用 NLI backbone（纯 gold annotation 比较），R2 混淆了 EDCR 和 CED
- **反驳 R2-N3**：Conclusion 长度是写作偏好，不应列为 critical
- 其余 Must-Fix（N1(1)(2), N2）和大部分 Should-Fix/Minor 均同意
- 维持 Overall 3.5 不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1"
}
```

</details>

---
