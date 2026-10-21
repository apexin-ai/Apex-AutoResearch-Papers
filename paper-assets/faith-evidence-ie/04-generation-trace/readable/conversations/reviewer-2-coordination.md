# Reviewer 2 coordination

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 304
- **Recorded user turns:** 8
- **Tool calls:** 144
- **Original source:** `logs/chats/feishu_group_oc_186574e43a82a9df336fe62a846a7b52_reviewer_2.jsonl`
- **Structured JSON:** [`14d24408cb2225d5c1e0.json`](../../sessions/14/14d24408cb2225d5c1e0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-18T06:48:47.558939+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 2（新颖性、完整性与呈现质量）

### Venue 信息
- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references/appendix
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind，禁止 self-identification
- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读

### 论文路径
`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）

### 你的审查侧重：新颖性、完整性与呈现质量

请重点审查以下方面：

1. **新颖性与贡献定位**
   - 核心贡献（decoupling spectrum、evidence tax、RSFT+CED）的新颖性如何？
   - 是否存在已有工作解决了类似问题但论文未讨论？
   - RSFT 本身是已有方法（STaR/RAFT 变体），论文对 "what's new" 的界定是否清晰？
   - EDCR 作为 metric 的新颖性和通用性如何？

2. **Related Work 覆盖与定位**
   - 是否遗漏重要的相关工作？特别关注：
     - 其他 LLM-based DocRE + evidence 的方法
     - Multi-objective RL 中的类似 decoupling 现象
     - NLI-based evidence evaluation 的其他工作
   - 与已有方法的比较是否公平和完整？
   - 引用是否充足？（当前 32 篇，EMNLP long paper 通常 40-60 篇）

3. **写作质量**
   - Abstract 是否在 30 秒内传达论文价值？
   - Introduction 叙事线是否连贯？
   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、黑名单词汇）？
   - 专有名词是否首次出现时有定义？
   - 段落过渡是否自然？

4. **格式合规**
   - 正文是否在 8 页内？（需要编译确认或目测估计）
   - Limitations section 是否在 references 前且内容充实？
   - 当前 Limitations 在 references 后（`\appendix` 之前有 `\bibliography`）——这是否符合 ARR 要求？
   - 缺少 Responsible NLP Checklist 和 Ethics Statement——这是否构成 desk reject 风险？
   - 参考文献格式是否符合 ACL 标准？bib 条目是否完整（注意 author 字段有 "and others" 和 "{Anonymous}"）？

5. **图表质量**
   - Figure 和 Table 的信息密度是否足够？
   - Caption 是否自包含？
   - 表格格式是否统一（小数精度、加粗/下划线规则）？

6. **叙事统一性**
   - Abstract → Introduction → Method → Experiments → Analysis → Conclusion 主线是否一致？
   - 是否存在 "Introduction 讲故事 A，Method 做故事 B" 的问题？

请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-18T06:48:57.553367+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-18T06:48:57.654682+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_2_2b5124f3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T06:48:57.705456+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T06:48:57.756480+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T06:49:00.870935+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 7 · 2026-05-18T06:49:01.222849+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T06:49:01.373709+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 9 · 2026-05-18T06:49:01.424342+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T06:49:04.538115+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T06:49:04.991206+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T06:49:04.991676+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T06:49:05.443965+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T06:49:05.494679+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T06:49:05.897404+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T06:49:05.948062+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T06:49:06.651702+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T06:49:06.702532+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T06:49:06.853751+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T06:49:06.854122+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T06:49:07.758345+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T06:49:07.758746+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T06:49:08.261162+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task for LLMs and compare three post-training paradigms across 85+ configurations. RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic, DPO gradual, RSFT none; EDCR $\rho = -0.965$), and the cost of joint evidence production follows a non-monotonic pattern across scales (+8pp at 1.7B, $-$7.5pp at 4B, near zero at 8B). RSFT with CED scoring yields +4.92pp Ign-F1 at 4B (four-seed mean); our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT (50.51) at a fraction of the cost.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T06:49:08.261615+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T06:49:08.763838+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T06:49:08.764278+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T06:49:08.965862+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T06:49:08.966551+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T06:49:09.017271+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T06:49:16.103401+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T06:49:16.154041+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T06:49:19.320132+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T06:49:19.773256+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form dimensions soundness excitement reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form dimensions soundness excitement reproducibility"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T06:49:26.486530+00:00_

Web search results for query: "EMNLP 2026 ARR review form dimensions soundness excitement reproducibility"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"PrivateNLP@ACL 2026","url":"https://sites.google.com/view/privatenlp2026/"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum","url":"https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"}]

Based on the search results, here's what I found about the ARR review form dimensions for EMNLP 2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

The review form includes the following dimensions:

1. **Soundness**: Reviewers assess whether the paper is sufficiently sound and thorough, whether it clearly states scientific claims and provides adequate support for them, and for experimental papers consider the depth and/or breadth of the research questions investigated, technical soundness of experiments, and methodological validity of evaluation.

2. **Ex
…[truncated 996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6713
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T06:49:26.539536+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the web search results, here is information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified
…[truncated 1352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7219
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T06:49:31.261718+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their scales (1-5 etc.), and exact descriptions for each score level. I need the full soundness scale, excitement scale, overall assessment scale, and any other scored dimensions like reproducibility, limitations, confidence. Include all text for each rating level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their scales (1-5 etc.), and exact descriptions for each score level. I need the full soundness scale, excitement scale, overall assessment scale, and any other scored dimensions like reproducibility, limitations, confidence. Include all text for each rating level."
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T06:49:33.673467+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines. I need: 1) What dimensions reviewers must score on, 2) The scoring scales and what each level means, 3) Any specific instructions about what constitutes a good review, 4) Requirements for limitations section, ethics, responsible NLP checklist. Give me the full details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines. I need: 1) What dimensions reviewers must score on, 2) The scoring scales and what each level means, 3) Any specific instructions about what constitutes a good review, 4) Requirements for limitations section, ethics, responsible NLP checklist. Give me the full details."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T06:49:40.100774+00:00_

# ARR Reviewer Guidelines: Scoring and Requirements

## Scoring Dimensions

As of February 2025, reviewers provide three distinct scores:

1. **Soundness**: Technical validity and methodological rigor
2. **Excitement**: Personal interest and subjective appeal (orthogonal to soundness)
3. **Overall Recommendation**: Composite assessment for venue suitability

The guidelines note that "soundness scores must be justified by the text of the review" and low scores without sufficient justification indicate the review doesn't faithfully explain the recommendation.

## Scoring Scales and Levels

The document does not specify explicit numerical scales or detailed level definitions. However, it clarifies that:

- Papers must be "sufficiently sound and reproducible" for main conferences and Findings
- A paper can receive low excitement but still merit acceptance due to impact potential
- Confidence scores indicate reviewer uncertainty about specific aspects

## Good Review Characteristics

Strong reviews must be:

- **Specific**: Identify exact issues with citations, line numbers, or references rather than vague criticisms
- **Professional and neutral**: Written "as if you would like to get yourself" without sarcasm or dismissiveness
- **Justified**: Explain reasoning for scores clearly
- **Responsive**: Acknowledge author responses during discussion periods

## Limitations Section Requirement

Papers must include a limitations section. The guidelines explicitly state limitations should not automatically be listed as weaknesses—reviewers must justify why acknowledged limitations invalidate the work.

## Ethics and Responsible NLP Checklist

Authors must complete the Responsible NLP checklist. Reviewers should assess whether responses are reasonable. Starting December 2024, egregious violations (blanket "yes" answers without justification) may qualify for desk rejection, though minor omissions are excused.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6427
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T06:49:41.406839+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Reviewer Confidence (1-5 Scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something..."
- **3**: "Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general..."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points..."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Soundness (1-5 Scale with Half-Points)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice..."
- **3**: "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support..."
- **2**: "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## Excitement (1-5 Scale with Half-Points)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend its presentation..."
- **3**: "Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others..."

## Overall Assessment (1-5 Scale with Half-Points)

…[truncated 2599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10145
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T06:49:50.403887+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements: page limits, limitations section placement, ethics statement requirements, responsible NLP checklist requirements, anonymization rules, appendix rules, template requirements. I need to know: 1) Is a Limitations section required? Where should it go? 2) Is a Responsible NLP Checklist required? 3) Is an Ethics Statement required? 4) What happens if these are missing (desk reject?)? 5) Any other formatting requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission requirements: page limits, limitations section placement, ethics statement requirements, responsible NLP checklist requirements, anonymization rules, appendix rules, template requirements. I need to know: 1) Is a Limitations section required? Where should it go? 2) Is a Responsible NLP Checklist required? 3) Is an Ethics Statement required? 4) What happens if these are missing (desk reject?)? 5) Any other formatting requirements."
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T06:49:54.775284+00:00_

# EMNLP 2026 Submission Requirements

Based on the provided content, here's what I found:

## Page Limits
- **Long papers:** 8 pages (9 pages for camera-ready to address reviewer feedback)
- **Short papers:** 4 pages (5 pages for camera-ready)

## Key Requirements Referenced

The call states that submissions must follow "all of the ARR submission requirements," including specific policies on:
- Anonymization (two-way anonymized review)
- Limitations sections
- Responsible NLP research checklist
- Ethics policies
- Writing assistance guidelines

## What the Document Specifies

The page **does not provide detailed specifications** for where the Limitations section should be placed, whether the Responsible NLP Checklist is mandatory, or consequences for missing elements. Instead, it directs authors to consult:

1. The ARR CFP (https://aclrollingreview.org/cfp) for comprehensive submission details
2. The responsible NLP research checklist (https://aclrollingreview.org/responsibleNLPresearch)
3. ACL's Publication Ethics Policy
4. ARR's Ethics Policy

## What Cannot Be Determined from This Document

This page does not specify:
- Exact placement of Limitations sections
- Whether Responsible NLP Checklist completion is required vs. optional
- Desk rejection procedures for missing sections
- Complete formatting requirements

**Recommendation:** Consult the linked ARR CFP and ACL policy pages for granular submission details not covered here.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4371
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-18T06:49:59.195451+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract ALL submission requirements about: 1) Limitations section - is it mandatory? where should it go (before or after references)? does it count toward page limit? 2) Responsible NLP Research Checklist - is it mandatory? what happens if missing? 3) Ethics Statement - required? 4) Any desk reject criteria. 5) Page limits for long/short papers. 6) Anonymization requirements. 7) Appendix rules."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract ALL submission requirements about: 1) Limitations section - is it mandatory? where should it go (before or after references)? does it count toward page limit? 2) Responsible NLP Research Checklist - is it mandatory? what happens if missing? 3) Ethics Statement - required? 4) Any desk reject criteria. 5) Page limits for long/short papers. 6) Anonymization requirements. 7) Appendix rules."
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T06:50:05.476493+00:00_

# ARR Submission Requirements Summary

## 1) Limitations Section
**Mandatory.** Must appear in a dedicated section titled "Limitations" at the end of the paper, before references. Does not count toward page limit. Papers without this section will be desk rejected. The section should only discuss limitations of presented work, not introduce new methods or results.

## 2) Responsible NLP Research Checklist
**Mandatory.** Authors must complete this as part of submission. Incorrect, incomplete, or misleading information can result in desk rejection. The checklist content is used during review, and metadata fields remain editable for 48 hours after the submission deadline.

## 3) Ethics Statement
**Encouraged, not strictly required.** Authors are required to honor the ACL Code of Ethics. An optional section on "Ethical considerations" is recommended at the paper's end and does not count toward the page limit. Papers may be rejected on ethical grounds if authors violate the code or inadequately address concerns.

## 4) Desk Rejection Criteria
Papers face desk rejection for:
- Format and anonymity violations
- Dual submissions
- Self-plagiarism or significant content overlap
- Missing limitations section
- Exceeding length requirements
- Incorrect/incomplete responsible checklist filings
- Resubmission policy violations
- Missing author registration or review duties (as of May 2025)
- Prompt injection attempts to manipulate machine readers

## 5) Page Limits
- **Long papers:** up to 8 pages of content, unlimited references and post-conclusion space
- **Short papers:** up to 4 pages of content, unlimited references and post-conclusion space

## 6) Anonymization Requirements
Papers must exclude author names and affiliations. Self-references revealing identity (e.g., "We previously showed") must be rewritten in third person. Supplementary materials and repository links must be anonymized. Non-compliant submissions face desk rejection.

## 7) Appendix Rules
Appendices follow t
…[truncated 270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6281
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T06:50:49.854169+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-18T06:50:50.256787+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T06:50:50.759500+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T06:50:51.212141+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T06:50:51.413616+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T06:50:51.464355+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex:8:CED operates effectively at the response level for both RSFT selection and inference-time reranking, but fails at sentence-level granularity: filtering individual evidence sentences by NLI score reduces Evi-F1 by 7.7pp (Recall $-$20pp), as it disrupts co-reference chains across evidence sentences. This suggests that evidence quality is a holistic response property rather than a per-sentence attribute.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex:12:First, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-18T06:50:56.071560+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "highlighting|demonstrating|showcasing|leveraging|facilitating|utilizing",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "highlighting|demonstrating|showcasing|leveraging|facilitating|utilizing",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-18T06:50:56.470828+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:141:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 399
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-18T06:50:56.974085+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|It is worth noting|Notably",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|It is worth noting|Notably",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-18T06:50:57.928452+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-18T06:50:58.280468+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "delve|leverage|myriad|plethora|paradigm shift|in the realm of",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "delve|leverage|myriad|plethora|paradigm shift|in the realm of",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-18T06:50:58.331323+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-18T06:51:01.645818+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "and others|Anonymous",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "and others|Anonymous",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T06:51:01.696461+00:00_

3:  author    = {{Anonymous}},
11:  author    = {Xu and others},
19:  author  = {Dai, Runpeng and Zheng, Tong and others},
43:  author  = {Jin, Hangzhan and others},
139:  author    = {{Anonymous}},
155:  author  = {Ito, Taishu and others},
171:  author  = {Liu, Shih-Yang and others},
179:  author    = {Liu, Zichen and others},
187:  author  = {Yu, Qiying and others},
203:  author  = {Chen, Xiwen and others},
219:  author    = {Wang, Yutao and others},
226:  author  = {Wang, Yuxuan and others},
234:  author  = {Zhang, Xiao and others},
242:  author    = {Tang, Yunhao and others},
250:  author  = {Wang, Chenghao and others},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-18T06:51:14.258670+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 59 · 2026-05-18T06:51:14.259176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-18T06:54:19.753717+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见 — Round 1\n\n**论文**: \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 新颖性、完整性与呈现质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验覆盖广但 EDCR 存在定义循环问题，RSFT 训练数据量存在自相矛盾（9,042 vs 2,718），部分结论仅单 seed |\n| Excitement | 3/5 | Scale-dependent evidence tax 有意思，decoupling spectrum 有实用价值，但 CED≈flat-NLI 削弱了方法贡献 |\n| Reproducibility | 3/5 | 超参数详细，但仅 dev set 结果、部分 seed 不足、\"pre-D076 evaluation protocol\" 未解释 |\n| Confidence | 4/5 | 熟悉 DocRE 和 LLM post-training 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环\n\n- 具体位置：Section 3.5 (Eq. 2), Section 6 Analysis 第 1 段\n- 问题：EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。论文声称 \"elevated EDCR signals problematic decoupling\"，但 EDCR 的分母就是 Rel-Recall，它测量的不是独立于提取质量的 \"decoupling\"，而是 Rel-Recall 低时的数学必然结果。\n- 为什么影响接收：EDCR 是论文四项贡献之一（Contribution 2），也是 decoupling spectrum 叙事的核心量化工具。如果指标本身有循环性问题，整个 spectrum 分析的说服力大打折扣。\n- 建议修改方向：(1) 在 N=6 个方法配置上 ρ=-0.965 的统计意义有限（p 值应报告）；(2) 需要提供 EDCR 相对于简单替代指标（如 Evi-F1 - Rel-F1 差值、或 Evi-Recall_TP 本身）的增量诊断价值；(3) 对 EDCR 的分母效应做敏感性分析——当 Rel-Recall 大于某阈值时，EDCR 的诊断能力是否仍然成立？\n\n**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献\n\n- 具体位置：Section 3.4 末段, Section 6 Ablation, Appendix Table 5\n- 问题：论文将 CED 列为核心贡献之一（\"NLI-based Contrastive Evidence Discrimination scoring function\"），但消融实验显示 CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp（0.4563 vs 0.4561），在统计上无法区分。论文承认 \"CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection\"，并将 CED 的优势归结为 \"interpretable per-triple discrimination scores\"，但论文正文中从未展示这一可解释性如何被实际利用（Qualitative Analysis 中的 Case 3 展示的是 EDCR，不是 CED）。\n- 为什么影响接收：当论文自身的消融否定了 CED 相对于 flat-NLI 的量化优势时，将 CED 作为独立贡献（Contribution 4 中的 \"NLI-based CED scoring\"）是过度声称。审稿人会质疑：如果去掉 contrastive 项，结果一样，那真正的贡献到底是什么？\n- 建议修改方向：(1) 诚实地将 CED 降级为 \"一种可选的评分函数\"，将真正的贡献定位为 \"NLI-based quality filtering for RSFT\" 而非 CED 本身；(2) 如果要保留 CED 作为贡献，需要展示 contrastive 项在某些场景下确实优于 flat-NLI（例如在 entity-dense 文档中、或在特定困难关系类型上）。\n\n**N3** [critical] RSFT 训练数据量存在明确的数值矛盾\n\n- 具体位置：Section 3.3 RSFT 段 vs Appendix Table 4\n- 问题：Section 3.3 明确写道 \"From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3% acceptance rate)\"。但 Appendix Table 4 的 RSFT 行显示 \"Training samples: 2,718\"。如果 k=1（每个文档选最好的 1 个输出），最多得到约 3,053 个样本（=训练文档数），不可能是 9,042。9,042 ≈ 3,027 × 3，更像 k=3 的结果。而 2,718 < 3,053，说明部分文档被完全过滤，与 k=1 一致。这两个数字（9,042 vs 2,718）有 3.3 倍差距且不可调和。\n- 为什么影响接收：训练数据量是 RSFT 方法的核心参数，直接影响实验可复现性。如果读者无法确定实际使用了多少训练数据，方法描述的可信度受损。\n- 建议修改方向：检查并统一这两个数字，解释差异来源。如果存在额外的过滤步骤，需在方法部分明确描述。\n\n**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交\n\n- 具体位置：Section 4.1 Metrics 末尾, Section 7 Limitations\n- 问题：所有实验均在 DocRED dev set 上报告，test set 提交标注为 \"pending\"。DocRED 是一个有公开 leaderboard 的 benchmark，dev set 和 test set 的分布可能不同。Limitations 虽然承认了这一点，但对于 EMNLP 长文来说，完全缺少 test set 结果是一个重大缺陷。\n- 为什么影响接收：审稿人无法验证方法在 held-out 数据上的泛化能力。如果 RSFT 的 4-seed 结果全部来自 dev set 上的调优，存在过拟合风险。\n- 建议修改方向：在投稿前提交至少 Qwen3-4B SFT baseline 和 RSFT CED 的 test set 结果。如果 test set 提交受限，应在论文中详细解释原因。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 指标格式严重不一致\n\n- 具体位置：Table 1, 2, 3, 5, 6（所有主要表格）\n- 问题：同一表格中，Ign-F1 以百分比格式呈现（39.74），Rel-F1 以小数呈现（0.4049），Evi-F1 又以百分比呈现（79.86）。Ign-F1 39.74 和 Rel-F1 0.4049（≈40.49%）是同一量级的指标，但格式完全不同，极易造成误读。EDCR 0.6982 和 Evi-F1 79.86 并列时，读者需要额外心智负担判断哪个是比例哪个是百分比。\n- 建议：全表统一为百分比格式或全统一为小数格式。\n\n**W2** [warning] 引用数量偏低且多条 bib 条目不完整\n\n- 具体位置：references.bib 全文\n- 问题：(1) 总计 32 篇引用，EMNLP long paper 通常 40-60 篇。(2) 15/32 条 bib 条目使用 \"and others\" 代替完整作者列表（如 `chen2025docksrag`, `dai2025r1re`, `jin2025rl_panacea`, `ito2025mogrpo`, `liu2026gdpo`, `liu2025drgrpo`, `yu2025dapo`, `chen2025dragrpo`, `wang2025rear`, `wang2025relprior`, `zhang2025glidre`, `tang2025rsftppo`, `wang2025rullm`）。(3) 两条使用 `{Anonymous}` 作为作者（`autore2024`, `zhao2025egrpo`）。ACL style 要求完整作者列表，\"and others\" 不是标准 BibTeX 用法（应为 \"and others\" → 实际作者名 or 至少 \"and others\" 需改为完整列表）。`autore2024` 有真实作者（Xue et al.），不应标记为 Anonymous。\n- 建议：补全所有作者列表，将 Anonymous 替换为真实作者信息（如果已发表）。\n\n**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑\n\n- 具体位置：Section 4.4, Table 3\n- 问题：1.7B 模型从 evidence generation 中获得 +8.04pp 的收益，论文将其归因于 \"implicit regularization, forcing the model to attend to supporting context rather than memorizing surface-level patterns\"。但：(1) 这一解释是推测性的，无实验支撑（例如 attention pattern 分析、memorization 指标）；(2) Limitations 承认 1.7B 有 44.4% 的 repetitive pattern 问题，这可能严重混淆 evidence benefit 的测量——如果 no-evidence 模型在 1.7B 下更容易产生重复输出，Ign-F1 下降可能是重复导致的，而非 evidence 的正面效应；(3) \"fair evaluation subset\" 上的 +6.2pp 仅一句话带过，未给出 subset 定义和完整数据。\n- 建议：(1) 详细定义 \"fair evaluation subset\"，将完整结果放入正文或附录表格；(2) 分析 1.7B no-evidence 模型的 repetition rate，排除重复输出对 Ign-F1 差异的贡献；(3) 对 \"implicit regularization\" 假说提供至少一个定量证据。\n\n**W4** [warning] Multi-seed 覆盖不均匀\n\n- 具体位置：Table 3 (scaling), Appendix Table 6 (cross_detail)\n- 问题：4B 的 RSFT 有 4-seed 均值 (sd=0.49)，但 1.7B、8B、LLaMA-3.1-8B 均为单 seed（Appendix Table 6 caption 确认 \"single seed for other scales\"）。LLaMA 有第二个 seed（s43: 56.19，在 Appendix 文字中提到），但 Qwen3-1.7B 和 Qwen3-8B 的 RSFT 增益（+2.64, +3.82）基于单次运行。考虑到 4B 上 4 个 seed 的范围为 44.16-45.12（接近 1pp），单 seed 结果的 RSFT 增益可信度有限。\n- 建议：至少在 1.7B 和 8B 上报告 2-seed 结果，或在论文中明确标注哪些数字基于单 seed 并讨论 variance 风险。\n\n**W5** [warning] Related Work 缺少重要相关方向\n\n- 具体位置：Section 2\n- 问题：\n  (1) **Multi-task learning / task interference**: 论文的核心发现——extraction 和 evidence 在梯度优化中竞争——与 multi-task learning 中的 negative transfer / gradient conflict 文献直接相关（如 Standley et al. 2020 \"Which Tasks Should Be Learned Together\"; Yu et al. 2020 \"Gradient Surgery for Multi-Task Learning\"）。这些工作提供了理论框架来解释为什么 GRPO 导致 decoupling，但论文完全未讨论。\n  (2) **Self-consistency / majority voting**: RSFT 的 \"sample N, select best\" 与 Wang et al. 2023 \"Self-Consistency Improves Chain of Thought Reasoning\" 在方法论上高度相似。论文引用了 STaR 和 RAFT，但未提及 self-consistency 这一更广泛的范式。\n  (3) 缺少与 encoder-based evidence 方法的直接数值比较。论文提到 \"our best joint Evi-F1 (0.36) falls below supervised DREEAM (54.01%)\"（Section 4.6），但这一比较被放在最后一段轻描淡写处理，且未出现在任何表格中。读者无法快速评估 LLM-based 方法与 encoder-based 方法的整体差距。\n- 建议：(1) 增加一段讨论 multi-task learning 中 task interference 的文献并建立联系；(2) 引用 self-consistency；(3) 在 main results 或 generalization 中增加一个表格，直接与 SAIS/DREEAM/EIDER 做 head-to-head 对比（即使在不同模型架构下）。\n\n**W6** [warning] \"pre-D076 evaluation protocol\" 未解释\n\n- 具体位置：Table 2 脚注, Section 4.3 DPO 段\n- 问题：DPO 3-epoch 结果标注为 \"Pre-D076 evaluation protocol\"，但论文从未解释 D076 是什么、pre-D076 和当前 protocol 有何差异、为什么仍将这些不可比较的结果纳入 Table 2。如果评估协议不同，这些数字是否应该出现在同一个表中？\n- 建议：要么解释 D076 并量化 protocol 差异的影响，要么将 DPO 3ep 结果移至附录并在正文中明确说明不可直接比较。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Per-relation EDCR 图的 caption 与正文不一致**: Figure 5 caption 说 \"93 relation types\"，Analysis 正文说 \"76 relation types with ≥5 evaluation samples\"，DocRED 标注的是 96 relation types。三个数字互相矛盾。\n2. **Abstract 偏长且数据密集**: 当前 Abstract 约 230 words，\"Three findings emerge\" 之后的三段各带具体数字，读起来像实验结果摘要而非叙事。建议压缩 Finding 3 中的具体数字，保留趋势描述。\n3. **Contribution 列表中 \"85+ experiments\" 的计算方式未交代**: 85+ 如何计算？是 (方法×模型×seed×数据集) 的组合数？读者无法验证。\n4. **Section 4.5 Evidence Strategy Comparison 中的 \"CED reranking at inference time\"**: 这一方法在 Method 部分没有描述，突然出现在实验中。应在 Method 中至少用一段描述 inference-time reranking 的流程。\n5. **Appendix 中 GRPO dynamics Figure 3 引用了 \"G=4 QLoRA\" 和 \"G=8 bf16\" 但 caption 说 \"(a) Relation F1 across checkpoints\"**: 无法从当前文本判断图中各曲线是否有 legend 标注。\n\n---\n\n## 主要优势\n\n1. **实验规模和系统性**: 跨 4 个模型规模、2 个模型家族、2 个数据集、3 个优化范式的对比在 LLM-based DocRE 领域是罕见的。85+ 配置的覆盖面使得结论比单模型/单方法的工作更可信。\n\n2. **Scale-dependent evidence tax 是真正有意思的发现**: 1.7B 受益、4B 受损、8B 中性的非单调模式打破了 \"evidence 一定损害 extraction\" 的简单假设。即使 1.7B 的具体解释需要加强，这一经验发现本身对后续研究有指导意义。\n\n3. **问题定义有价值**: 将 evidence-grounded DocRE 形式化为 LLM 的结构化生成任务，并系统研究 evidence 生产的代价，是一个有意义的问题定义。现有 LLM-based DocRE 工作确实忽略了 evidence 生成。\n\n4. **Decoupling spectrum 的诊断价值**: 尽管 EDCR 的定义有循环性问题，GRPO catastrophic collapse 的定性发现（模型放弃正确关系类型转而生成自由文本标签）是有实践意义的警示，对计划在 IE 任务上使用 GRPO 的研究者有直接参考价值。\n\n5. **写作质量整体良好**: 无 em-dash，无过度 AI 写作标志词，段落过渡自然，叙事主线基本统一。Limitations section 位置正确（references 之前），内容诚实。\n\n6. **RSFT 的 \"discrete selection avoids gradient-based trade-off\" 洞察有一般性意义**: 这一观察超越了 DocRE 任务本身，对所有多目标 LLM post-training 场景有参考价值。\n\n---\n\n## 叙事统一性评估\n\nAbstract → Introduction → Method → Experiments → Analysis → Conclusion 的主线基本一致：都围绕 \"evidence generation 的代价及其与优化方法的关系\" 展开。未发现 \"Introduction 讲故事 A，Method 做故事 B\" 的问题。\n\n但存在一个轻微的叙事张力：Introduction 将 CED 作为关键创新之一推介（Contribution 4），但 Analysis 中的消融显示 CED ≈ flat-NLI。这使得 Introduction 的 framing 与 Analysis 的结论存在落差。建议在 Introduction 中更诚实地定位 CED（作为评分选择的一种实现，而非核心创新）。\n\n---\n\n## 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | ⚠️ 无法编译确认 | 从 section 数量和内容密度看，8 页可能紧张但未明显超限 |\n| Limitations 位置 | ✅ | 在 `\\bibliography` 之前，符合 ARR 要求 |\n| Double-blind | ✅ | `\\author{Anonymous}`，`[review]` option |\n| Responsible NLP Checklist | ❌ 缺失 | 论文 .tex 中未见，也未在附录中出现。如果仅通过 OpenReview 提交则无问题，但需确认 |\n| Ethics Statement | ⚠️ 缺失 | ARR 鼓励但不强制 |\n| 参考文献格式 | ❌ 有问题 | 15/32 条 \"and others\"，2 条 Anonymous（见 W2） |\n\n---\n\n## 缺失引用建议\n\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together in Multi-Task Learning?\" — task interference\n2. Yu et al. (2020) \"Gradient Surgery for Multi-Task Learning\" — gradient conflict\n3. Wang et al. (2023) \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\" — sample-then-select paradigm\n4. 建议补充 2-3 篇 encoder-based DocRE 近年工作以增加引用密度\n",
  "reviewer_id": "2",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见 — Round 1\n\n**论文**: \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 新颖性、完整性与呈现质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验覆盖广但 EDCR 存在定义循环问题，RSFT 训练数据量存在自相矛盾（9,042 vs 2,718），部分结论仅单 seed |\n| Excitement | 3/5 | Scale-dependent evidence tax 有意思，decoupling spectrum 有实用价值，但 CED≈flat-NLI 削弱了方法贡献 |\n| Reproducibility | 3/5 | 超参数详细，但仅 dev set 结果、部分 seed 不足、\"pre-D076 evaluation protocol\" 未解释 |\n| Confidence | 4/5 | 熟悉 DocRE 和 LLM post-training 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环\n\n- 具体位置：Section 3.5 (Eq. 2), Section 6 Analysis 第 1 段\n- 问题：EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。论文声称 \"elevated EDCR signals problematic decoupling\"，但 EDCR 的分母就是 Rel-Recall，它测量的不是独立于提取质量的 \"decoupling\"，而是 Rel-Recall 低时的数学必然结果。\n- 为什么影响接收：EDCR 是论文四项贡献之一（Contribution 2），也是 decoupling spectrum 叙事的核心量化工具。如果指标本身有循环性问题，整个 spectrum 分析的说服力大打折扣。\n- 建议修改方向：(1) 在 N=6 个方法配置上 ρ=-0.965 的统计意义有限（p 值应报告）；(2) 需要提供 EDCR 相对于简单替代指标（如 Evi-F1 - Rel-F1 差值、或 Evi-Recall_TP 本身）的增量诊断价值；(3) 对 EDCR 的分母效应做敏感性分析——当 Rel-Recall 大于某阈值时，EDCR 的诊断能力是否仍然成立？\n\n**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献\n\n- 具体位置：Section 3.4 末段, Section 6 Ablation, Appendix Table 5\n- 问题：论文将 CED 列为核心贡献之一（\"NLI-based Contrastive Evidence Discrimination scoring function\"），但消融实验显示 CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp（0.4563 vs 0.4561），在统计上无法区分。论文承认 \"CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection\"，并将 CED 的优势归结为 \"interpretable per-triple discrimination scores\"，但论文正文中从未展示这一可解释性如何被实际利用（Qualitative Analysis 中的 Case 3 展示的是 EDCR，不是 CED）。\n- 为什么影响接收：当论文自身的消融否定了 CED 相对于 flat-NLI 的量化优势时，将 CED 作为独立贡献（Contribution 4 中的 \"NLI-based CED scoring\"）是过度声称。审稿人会质疑：如果去掉 contrastive 项，结果一样，那真正的贡献到底是什么？\n- 建议修改方向：(1) 诚实地将 CED 降级为 \"一种可选的评分函数\"，将真正的贡献定位为 \"NLI-based quality filtering for RSFT\" 而非 CED 本身；(2) 如果要保留 CED 作为贡献，需要展示 contrastive 项在某些场景下确实优于 flat-NLI（例如在 entity-dense 文档中、或在特定困难关系类型上）。\n\n**N3** [critical] RSFT 训练数据量存在明确的数值矛盾\n\n- 具体位置：Section 3.3 RSFT 段 vs Appendix Table 4\n- 问题：Section 3.3 明确写道 \"From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3% acceptance rate)\"。但 Appendix Table 4 的 RSFT 行显示 \"Training samples: 2,718\"。如果 k=1（每个文档选最好的 1 个输出），最多得到约 3,053 个样本（=训练文档数），不可能是 9,042。9,042 ≈ 3,027 × 3，更像 k=3 的结果。而 2,718 < 3,053，说明部分文档被完全过滤，与 k=1 一致。这两个数字（9,042 vs 2,718）有 3.3 倍差距且不可调和。\n- 为什么影响接收：训练数据量是 RSFT 方法的核心参数，直接影响实验可复现性。如果读者无法确定实际使用了多少训练数据，方法描述的可信度受损。\n- 建议修改方向：检查并统一这两个数字，解释差异来源。如果存在额外的过滤步骤，需在方法部分明确描述。\n\n**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交\n\n- 具体位置：Section 4.1 Metrics 末尾, Section 7 Limitations\n- 问题：所有实验均在 DocRED dev set 上报告，test set 提交标注为 \"pending\"。DocRED 是一个有公开 leaderboard 的 benchmark，dev set 和 test set 的分布可能不同。Limitations 虽然承认了这一点，但对于 EMNLP 长文来说，完全缺少 test set 结果是一个重大缺陷。\n- 为什么影响接收：审稿人无法验证方法在 held-out 数据上的泛化能力。如果 RSFT 的 4-seed 结果全部来自 dev set 上的调优，存在过拟合风险。\n- 建议修改方向：在投稿前提交至少 Qwen3-4B SFT baseline 和 RSFT CED 的 test set 结果。如果 test set 提交受限，应在论文中详细解释原因。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 指标格式严重不一致\n\n- 具体位置：Table 1, 2, 3, 5, 6（所有主要表格）\n- 问题：同一表格中，Ign-F1 以百分比格式呈现（39.74），Rel-F1 以小数呈现（0.4049），Evi-F1 又以百分比呈现（79.86）。Ign-F1 39.74 和 Rel-F1 0.4049（≈40.49%）是同一量级的指标，但格式完全不同，极易造成误读。EDCR 0.6982 和 Evi-F1 79.86 并列时，读者需要额外心智负担判断哪个是比例哪个是百分比。\n- 建议：全表统一为百分比格式或全统一为小数格式。\n\n**W2** [warning] 引用数量偏低且多条 bib 条目不完整\n\n- 具体位置：references.bib 全文\n- 问题：(1) 总计 32 篇引用，EMNLP long paper 通常 40-60 篇。(2) 15/32 条 bib 条目使用 \"and others\" 代替完整作者列表（如 `chen2025docksrag`, `dai2025r1re`, `jin2025rl_panacea`, `ito2025mogrpo`, `liu2026gdpo`, `liu2025drgrpo`, `yu2025dapo`, `chen2025dragrpo`, `wang2025rear`, `wang2025relprior`, `zhang2025glidre`, `tang2025rsftppo`, `wang2025rullm`）。(3) 两条使用 `{Anonymous}` 作为作者（`autore2024`, `zhao2025egrpo`）。ACL style 要求完整作者列表，\"and others\" 不是标准 BibTeX 用法（应为 \"and others\" → 实际作者名 or 至少 \"and others\" 需改为完整列表）。`autore2024` 有真实作者（Xue et al.），不应标记为 Anonymous。\n- 建议：补全所有作者列表，将 Anonymous 替换为真实作者信息（如果已发表）。\n\n**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑\n\n- 具体位置：Section 4.4, Table 3\n- 问题：1.7B 模型从 evidence generation 中获得 +8.04pp 的收益，论文将其归因于 \"implicit regularization, forcing the model to attend to supporting context rather than memorizing surface-level patterns\"。但：(1) 这一解释是推测性的，无实验支撑（例如 attention pattern 分析、memorization 指标）；(2) Limitations 承认 1.7B 有 44.4% 的 repetitive pattern 问题，这可能严重混淆 evidence benefit 的测量——如果 no-evidence 模型在 1.7B 下更容易产生重复输出，Ign-F1 下降可能是重复导致的，而非 evidence 的正面效应；(3) \"fair evaluation subset\" 上的 +6.2pp 仅一句话带过，未给出 subset 定义和完整数据。\n- 建议：(1) 详细定义 \"fair evaluation subset\"，将完整结果放入正文或附录表格；(2) 分析 1.7B no-evidence 模型的 repetition rate，排除重复输出对 Ign-F1 差异的贡献；(3) 对 \"implicit regularization\" 假说提供至少一个定量证据。\n\n**W4** [warning] Multi-seed 覆盖不均匀\n\n- 具体位置：Table 3 (scaling), Appendix Table 6 (cross_detail)\n- 问题：4B 的 RSFT 有 4-seed 均值 (sd=0.49)，但 1.7B、8B、LLaMA-3.1-8B 均为单 seed（Appendix Table 6 caption 确认 \"single seed for other scales\"）。LLaMA 有第二个 seed（s43: 56.19，在 Appendix 文字中提到），但 Qwen3-1.7B 和 Qwen3-8B 的 RSFT 增益（+2.64, +3.82）基于单次运行。考虑到 4B 上 4 个 seed 的范围为 44.16-45.12（接近 1pp），单 seed 结果的 RSFT 增益可信度有限。\n- 建议：至少在 1.7B 和 8B 上报告 2-seed 结果，或在论文中明确标注哪些数字基于单 seed 并讨论 variance 风险。\n\n**W5** [warning] Related Work 缺少重要相关方向\n\n- 具体位置：Section 2\n- 问题：\n  (1) **Multi-task learning / task interference**: 论文的核心发现——extraction 和 evidence 在梯度优化中竞争——与 multi-task learning 中的 negative transfer / gradient conflict 文献直接相关（如 Standley et al. 2020 \"Which Tasks Should Be Learned Together\"; Yu et al. 2020 \"Gradient Surgery for Multi-Task Learning\"）。这些工作提供了理论框架来解释为什么 GRPO 导致 decoupling，但论文完全未讨论。\n  (2) **Self-consistency / majority voting**: RSFT 的 \"sample N, select best\" 与 Wang et al. 2023 \"Self-Consistency Improves Chain of Thought Reasoning\" 在方法论上高度相似。论文引用了 STaR 和 RAFT，但未提及 self-consistency 这一更广泛的范式。\n  (3) 缺少与 encoder-based evidence 方法的直接数值比较。论文提到 \"our best joint Evi-F1 (0.36) falls below supervised DREEAM (54.01%)\"（Section 4.6），但这一比较被放在最后一段轻描淡写处理，且未出现在任何表格中。读者无法快速评估 LLM-based 方法与 encoder-based 方法的整体差距。\n- 建议：(1) 增加一段讨论 multi-task learning 中 task interference 的文献并建立联系；(2) 引用 self-consistency；(3) 在 main results 或 generalization 中增加一个表格，直接与 SAIS/DREEAM/EIDER 做 head-to-head 对比（即使在不同模型架构下）。\n\n**W6** [warning] \"pre-D076 evaluation protocol\" 未解释\n\n- 具体位置：Table 2 脚注, Section 4.3 DPO 段\n- 问题：DPO 3-epoch 结果标注为 \"Pre-D076 evaluation protocol\"，但论文从未解释 D076 是什么、pre-D076 和当前 protocol 有何差异、为什么仍将这些不可比较的结果纳入 Table 2。如果评估协议不同，这些数字是否应该出现在同一个表中？\n- 建议：要么解释 D076 并量化 protocol 差异的影响，要么将 DPO 3ep 结果移至附录并在正文中明确说明不可直接比较。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Per-relation EDCR 图的 caption 与正文不一致**: Figure 5 caption 说 \"93 relation types\"，Analysis 正文说 \"76 relation types with ≥5 evaluation samples\"，DocRED 标注的是 96 relation types。三个数字互相矛盾。\n2. **Abstract 偏长且数据密集**: 当前 Abstract 约 230 words，\"Three findings emerge\" 之后的三段各带具体数字，读起来像实验结果摘要而非叙事。建议压缩 Finding 3 中的具体数字，保留趋势描述。\n3. **Contribution 列表中 \"85+ experiments\" 的计算方式未交代**: 85+ 如何计算？是 (方法×模型×seed×数据集) 的组合数？读者无法验证。\n4. **Section 4.5 Evidence Strategy Comparison 中的 \"CED reranking at inference time\"**: 这一方法在 Method 部分没有描述，突然出现在实验中。应在 Method 中至少用一段描述 inference-time reranking 的流程。\n5. **Appendix 中 GRPO dynamics Figure 3 引用了 \"G=4 QLoRA\" 和 \"G=8 bf16\" 但 caption 说 \"(a) Relation F1 across checkpoints\"**: 无法从当前文本判断图中各曲线是否有 legend 标注。\n\n---\n\n## 主要优势\n\n1. **实验规模和系统性**: 跨 4 个模型规模、2 个模型家族、2 个数据集、3 个优化范式的对比在 LLM-based DocRE 领域是罕见的。85+ 配置的覆盖面使得结论比单模型/单方法的工作更可信。\n\n2. **Scale-dependent evidence tax 是真正有意思的发现**: 1.7B 受益、4B 受损、8B 中性的非单调模式打破了 \"evidence 一定损害 extraction\" 的简单假设。即使 1.7B 的具体解释需要加强，这一经验发现本身对后续研究有指导意义。\n\n3. **问题定义有价值**: 将 evidence-grounded DocRE 形式化为 LLM 的结构化生成任务，并系统研究 evidence 生产的代价，是一个有意义的问题定义。现有 LLM-based DocRE 工作确实忽略了 evidence 生成。\n\n4. **Decoupling spectrum 的诊断价值**: 尽管 EDCR 的定义有循环性问题，GRPO catastrophic collapse 的定性发现（模型放弃正确关系类型转而生成自由文本标签）是有实践意义的警示，对计划在 IE 任务上使用 GRPO 的研究者有直接参考价值。\n\n5. **写作质量整体良好**: 无 em-dash，无过度 AI 写作标志词，段落过渡自然，叙事主线基本统一。Limitations section 位置正确（references 之前），内容诚实。\n\n6. **RSFT 的 \"discrete selection avoids gradient-based trade-off\" 洞察有一般性意义**: 这一观察超越了 DocRE 任务本身，对所有多目标 LLM post-training 场景有参考价值。\n\n---\n\n## 叙事统一性评估\n\nAbstract → Introduction → Method → Experiments → Analysis → Conclusion 的主线基本一致：都围绕 \"evidence generation 的代价及其与优化方法的关系\" 展开。未发现 \"Introduction 讲故事 A，Method 做故事 B\" 的问题。\n\n但存在一个轻微的叙事张力：Introduction 将 CED 作为关键创新之一推介（Contribution 4），但 Analysis 中的消融显示 CED ≈ flat-NLI。这使得 Introduction 的 framing 与 Analysis 的结论存在落差。建议在 Introduction 中更诚实地定位 CED（作为评分选择的一种实现，而非核心创新）。\n\n---\n\n## 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | ⚠️ 无法编译确认 | 从 section 数量和内容密度看，8 页可能紧张但未明显超限 |\n| Limitations 位置 | ✅ | 在 `\\bibliography` 之前，符合 ARR 要求 |\n| Double-blind | ✅ | `\\author{Anonymous}`，`[review]` option |\n| Responsible NLP Checklist | ❌ 缺失 | 论文 .tex 中未见，也未在附录中出现。如果仅通过 OpenReview 提交则无问题，但需确认 |\n| Ethics Statement | ⚠️ 缺失 | ARR 鼓励但不强制 |\n| 参考文献格式 | ❌ 有问题 | 15/32 条 \"and others\"，2 条 Anonymous（见 W2） |\n\n---\n\n## 缺失引用建议\n\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together in Multi-Task Learning?\" — task interference\n2. Yu et al. (2020) \"Gradient Surgery for Multi-Task Learning\" — gradient conflict\n3. Wang et al. (2023) \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\" — sample-then-select paradigm\n4. 建议补充 2-3 篇 encoder-based DocRE 近年工作以增加引用密度\n",
    "reviewer_id": "2",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-18T06:54:24.023040+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4269
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-18T06:54:34.008304+00:00_

审稿意见已提交。

**总结**: Overall 3.0 (Findings)。主要 Must-Fix 问题四项：(1) EDCR 与 Rel-F1 的相关性存在定义循环——分母就是 Rel-Recall，高相关性部分是数学构造而非经验发现；(2) CED 与 flat-NLI 的消融差距仅 0.02pp，论文自身的实验否定了 CED 作为独立贡献的合理性；(3) RSFT 训练数据量在方法部分（9,042）和附录超参表（2,718）之间存在 3.3 倍的不可调和矛盾；(4) 全部结果仅在 dev set 上报告。

实验规模和 scale-dependent evidence tax 的发现是论文的核心价值。写作质量整体良好，无明显 AI 痕迹，叙事主线统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 63 · 2026-05-18T06:55:36.647632+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
---

# Reviewer 1 审稿意见 — Round 1

**Overall**: 3.0 (Findings)
**一句话总结**: 研究问题有价值、实验覆盖面广，但核心 claim 的统计支撑不足，多个关键实验存在混淆变量，且全部结果仅在 dev set 上报告。

## Must-Fix 问题

**N1** [critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果推断

- GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了两个变量：量化精度和 group size。论文将 catastrophic collapse 归因于 "4-bit quantization constrains the effective parameter space"，但无法排除 G=4 vs G=8 的影响。
- Introduction 第 29-30 行声称 "QLoRA acts as a catastrophic amplifier" 是因果性 claim，但实验设计无法支撑。
- 建议：补充 GRPO bf16 G=4 和 GRPO QLoRA G=8 实验；或将因果性表述降级。

**N2** [critical] 全部结果仅在 dev set 上报告，test set 结果缺失

- 85+ configurations 的系统性实证研究没有任何 test set 结果。DocRED test set 有公开 leaderboard（CodaLab），提交是标准做法。
- 建议：至少对 main results 提交 test set 评估。

**N3** [critical] SFT baseline 缺少多 seed 方差，+4.92pp 改进缺乏统计显著性检验

- RSFT CED 有 4-seed 均值 44.66±0.49，但 SFT baseline 仅单 seed (39.74)。没有 SFT 方差无法判断 +4.92pp 是否显著。全文无统计显著性检验。
- 建议：SFT 补充 3+ seeds，进行 paired bootstrap 或 t-test。

**N4** [critical] "Non-monotonic" scaling pattern 仅基于 3 个数据点，over-interpreted

- 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28）无法区分 non-monotonic pattern 与噪声。1.7B 的 +8.04 有替代解释（44.4% repetition → no-evidence 被人为压低）。Abstract 的 "+8pp" 在正文被修正为 "+6.2 on fair subset"，fair subset 细节缺失。
- 建议：增加中间规模点；详细报告 fair evaluation subset；对 repetition 做 controlled analysis；或将 claim 降级。

## Should-Fix 问题

**W1** [warning] EDCR 方法级相关性 (ρ=-0.965) 仅基于 6 个数据点
- n=6 时 power 极低，GRPO QLoRA 是极端 outlier，DPO 3ep 用了不同评估 protocol。
- 建议：报告去掉 outlier 后的相关性；统一评估 protocol。

**W2** [warning] "1.7B RSFT matches 8B SFT" claim 基于单 seed，差异仅 0.01pp
- 50.50 vs 50.51，均为单 seed。任何合理方差远超 0.01pp。
- 建议：补充多 seed 结果或将 "matches" 改为 "approaches"。

**W3** [warning] CED 与 flat-NLI 差异仅 0.02pp，contrastive component 的贡献未被证明
- flat-NLI 仅 2 seeds。论文没有实验展示 interpretability 的实际价值。
- 建议：补充 flat-NLI seeds；或诚实报告 contrastive 可能不必要。

**W4** [warning] Baseline 对比不完整
- 缺少与 SAIS/DREEAM/EIDER 的直接对比；缺少与 AutoRE/LMRC 的抽取性能对比；post-hoc 仅测 BM25。
- 建议：增加 encoder-based 和 LLM-based baseline 数字。

**W5** [warning] RSFT ablation 缺少 random selection baseline
- 无法确定改进来自 quality-based selection 还是 sampling diversity。
- 建议：增加 random-k=1 baseline。

**W6** [warning] GRPO/DPO 超参数探索不足
- GRPO 仅 KL=0.01，DPO 仅 β=0.1。
- 建议：至少测试 KL ∈ {0.001, 0.01, 0.1}，β ∈ {0.01, 0.1, 0.5}。

## 缺失引用
- Multi-task learning / auxiliary loss 文献（Ruder 2017, Fifty et al. 2021）
- Chain-of-thought / rationale generation 忠实性文献（Lanham et al. 2023）
- KGC/知识图谱补全相关工作

## 主要优势
1. 研究问题重要且定位精准
2. 实验覆盖面广
3. Decoupling spectrum 概念有启发性
4. RSFT 效果稳定（4-seed, 跨数据集, 跨模型家族）
5. 写作质量较好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-18T06:57:14.089506+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: GRPO 实验混淆变量**\n\n同意这是本文最严重的实验设计缺陷之一。GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了量化精度和 group size 两个变量。Section 4.3 第 1 段将 catastrophic collapse 归因于 \"4-bit quantization constrains the effective parameter space, forcing the reward signal to optimize whichever sub-task yields easier gradient progress\"，但无法排除 G=4 vs G=8 的影响。Introduction 第 30 行 \"QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause\" 是一个未经控制实验验证的因果性声明。\n\n补充：这一混淆变量问题进一步削弱了 \"decoupling spectrum\" 叙事的说服力。如果 GRPO 的 catastrophic collapse 实际上由 G=4（样本数不足以估计可靠 advantage）导致而非量化精度，那么 spectrum 的排序逻辑（\"RL optimization pressure correlates with decoupling severity\"）就需要重新审视。GRPO bf16 G=8 的 EDCR (0.6318) 实际上比 SFT baseline (0.6982) 更低（Table 2），这意味着去除 QLoRA 的极端案例后，GRPO 并未展现明显 decoupling，反而可能是三种方法中耦合最好的。这与论文的核心叙事 \"GRPO > DPO > RSFT in decoupling severity\" 矛盾。\n\n**[AGREE] R1-N2: 全部结果仅在 dev set 上报告**\n\n完全同意。我在自己的 N4 中也将此列为 critical 问题。DocRED test set 通过 CodaLab 提交是社区标准做法。对于一篇声称 \"85+ configurations\" 系统性实证研究的 EMNLP long paper，完全缺少 test set 结果是不可接受的。\n\n**[AGREE] R1-N3: SFT baseline 缺少多 seed 方差**\n\n同意，这是我遗漏的一个重要问题。+4.92pp 是论文最核心的效果数字（出现在 Abstract、Introduction Contribution 4、Table 1、Conclusion），但 SFT baseline 39.74 仅单 seed。如果 SFT 本身有 ±1pp 的方差（在 LLM fine-tuning 中完全正常），实际改进可能在 +2.9pp 到 +6.9pp 之间，这对论文价值的判断有本质差别。\n\n补充：Table 5 (Appendix) 显示 RSFT CED k=1 的 4 个 seed 范围为 44.16-45.12（range=0.96pp），说明该任务的 seed 方差并非可忽略。SFT 作为 RSFT 的 base model，其方差应至少与 RSFT 在同一量级。不报告 SFT 方差使得所有基于 \"SFT vs RSFT\" 差值的结论（包括 evidence tax、RSFT gain）都缺乏统计基础。\n\n**[AGREE] R1-N4: \"Non-monotonic\" scaling pattern 基于 3 个数据点**\n\n同意核心批评——3 个规模点不足以建立 \"non-monotonic pattern\" 这样强的 claim。我在自己的 W3 中从 1.7B 解释角度质疑了这一发现，但 R1 的表述更精准：即使 3 个点的值完全准确，3 点也无法区分 non-monotonic pattern 与两段独立趋势。\n\n补充两点：\n1. R1 指出 Abstract \"+8pp\" 与正文 \"fair subset +6.2pp\" 的不一致。这不仅是数字问题——如果 fair evaluation 后效果缩水 22%（8.04 → 6.2），说明 raw number 受评估方式影响很大，论文应在 Abstract 中使用更保守的数字。\n2. Table 3 中 Qwen3-1.7B SFT w/ evi 为 47.86 而 No-evi 为 39.82。但同一 table 中 Qwen3-4B 的关系是 SFT w/ evi 39.74 < No-evi 47.21。1.7B with evidence (47.86) 竟然高于 4B with evidence (39.74)，这一反直觉结果暗示 1.7B 和 4B 的训练可能在某些方面不等价（例如训练 convergence 不同、hyperparameter 对不同 scale 的适配度不同），而非单纯的 scale effect。论文未对此做任何讨论。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: EDCR 方法级相关性 ρ=-0.965 仅基于 n=6**\n\n完全同意，且这一问题与我的 N1（EDCR 定义循环性）相互加强。n=6 时 Spearman 相关的 critical value 很高（α=0.05 时需 |ρ|>0.886），即使 ρ=-0.965 在统计上接近显著，去掉 GRPO QLoRA 这个极端 outlier 后（n=5），相关性几乎肯定不再显著。再加上 DPO 3ep 使用了不同评估 protocol（Table 2 脚注），实际可比的数据点仅 4 个。在 4 个数据点上报告 ρ=-0.965 并将其作为 EDCR 有效性的核心证据（Section 6 第 1 段）是明显的 over-claim。\n\n**[AGREE] R1-W2: \"1.7B RSFT matches 8B SFT\" 基于单 seed**\n\n完全同意。50.50 vs 50.51 的 0.01pp 差异远小于合理方差。这一 claim 出现在 Abstract 第 14 行、Introduction Contribution 4、Section 4.4 末段、Conclusion。将其写为 \"matches\" 而非 \"approaches\" 是 over-claim。我补充一个角度：即使多 seed 后均值确实接近，这一比较跨越了不同 model size 和不同 base model capability——1.7B with evidence (47.86) 的 SFT 起点远高于 4B with evidence (39.74)，说明 Qwen3-1.7B 可能在 DocRE 任务上有异常优势（或 4B 有异常劣势），\"1.7B matches 8B\" 可能反映的是 Qwen3 系列特定 scale 的特性而非 RSFT 的通用能力。\n\n**[AGREE] R1-W3: CED vs flat-NLI 差异仅 0.02pp**\n\n完全同意。我在自己的 N2 中将此列为 critical 问题。R1 补充了 flat-NLI 仅 2 seeds 的问题，进一步削弱了比较的可靠性。论文应诚实报告 contrastive 组件在 RSFT selection 中可能不必要。\n\n**[AGREE] R1-W4: Baseline 对比不完整**\n\n同意。我在 W5 中从 Related Work 角度提出了类似问题。缺少与 SAIS/DREEAM/EIDER 的直接表格化对比是一个明显的疏漏。虽然 encoder-based 和 LLM-based 方法不完全 comparable（不同 backbone），但至少应在一个表格中并列呈现 evidence quality（Evi-F1）和 extraction quality（Rel-F1/Ign-F1），让读者自行判断 LLM-based evidence-grounded extraction 相对于 encoder-based 方法的整体位置。Section 4.6 末段的文字提及 \"our best joint Evi-F1 (0.36) falls below supervised DREEAM (54.01%)\"，但这一关键比较被埋在文字中，不在任何表格中。\n\n**[REBUT] R1-W5: RSFT ablation 缺少 random selection baseline**\n\n部分不同意。R1 认为缺少 random-k=1 baseline 使得 \"无法确定改进来自 quality-based selection 还是 sampling diversity\"。但论文在 Table 5 中报告了 RSFT CED k=3 (Ign-F1 43.64) vs k=1 (44.66)。k=3 使用了 3 倍数据量但效果更差，这已经间接回答了 \"更多 diversity 不等于更好\"。同时，RSFT 的训练数据来自 SFT 模型的采样输出，k=1 选最好的和 random k=1 选随机的之间的差异就是 data quality 的差异——如果 random k=1 与原始 SFT 训练数据等价（均为无 selection 的监督学习），那 SFT baseline 本身就是近似的 \"no quality selection\" baseline。\n\n不过，R1 的建议仍有价值：一个 explicit random-k=1 baseline（从 8 个候选中随机选 1 个）可以更干净地控制 \"training on self-generated data\" 这一因素，因为 SFT baseline 训练在 gold data 上而 RSFT 训练在 model-generated data 上，data source 不同。建议作者补充。\n\n**[AGREE] R1-W6: GRPO/DPO 超参数探索不足**\n\n同意，但认为严重程度可降一级。论文的核心论点是不同优化范式之间的结构性差异（gradient-based vs selection-based），而非任一方法的最优配置。如果 GRPO 在 KL=0.001 下不出现 collapse，或 DPO 在 β=0.5 下不出现 gradual decay，那 \"decoupling spectrum\" 叙事就会被根本否定。因此 R1 的建议虽然工作量大，但确实是验证核心 claim 所必需的。至少应测试 1-2 个替代超参数配置。\n\n---\n\n## 缺失引用\n\n**[AGREE]** R1 建议的 multi-task learning 文献（Ruder 2017, Fifty et al. 2021）与我建议的（Standley et al. 2020, Yu et al. 2020）覆盖同一缺口。论文的核心发现——extraction 和 evidence 在梯度优化中竞争——本质上是 multi-task learning 中 negative transfer 的一个实例，不引用这一成熟文献是明显疏漏。\n\n**[AGREE]** Chain-of-thought faithfulness 文献（Lanham et al. 2023）也是相关缺失——evidence generation 可以被视为一种 task-specific rationale generation，其忠实性问题与 CoT faithfulness 直接相关。\n\n---\n\n## 总结\n\nR1 的 4 个 Must-Fix 中我全部同意，其中 N1（混淆变量）和 N3（SFT 缺 multi-seed）是我自己审稿中未充分强调的问题。R1-N1 对 decoupling spectrum 的质疑比我的 N1（EDCR 循环性）更具打击力：如果 GRPO bf16 G=8 的 EDCR (0.6318) 比 SFT (0.6982) 还低，那去除 QLoRA 极端案例后，spectrum 的核心叙事就站不住了。\n\n综合两位 reviewer 的意见，论文的核心问题集中在：\n1. **统计严谨性不足**：SFT 单 seed、n=6 相关性、3 点 non-monotonic claim、单 seed cross-scale 比较\n2. **混淆变量**：GRPO 的 quantization vs group size、1.7B 的 repetition vs evidence benefit\n3. **贡献声明过度**：CED ≈ flat-NLI、EDCR 循环性、\"matches\" vs \"approaches\"\n4. **Dev-only 结果**\n\n维持我的 Overall 3.0 (Findings) 评分。如果 N1-N4 + R1-N1/N3 得到充分解决，有潜力升至 3.5。\n",
  "reviewer_id": "2",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: GRPO 实验混淆变量**\n\n同意这是本文最严重的实验设计缺陷之一。GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了量化精度和 group size 两个变量。Section 4.3 第 1 段将 catastrophic collapse 归因于 \"4-bit quantization constrains the effective parameter space, forcing the reward signal to optimize whichever sub-task yields easier gradient progress\"，但无法排除 G=4 vs G=8 的影响。Introduction 第 30 行 \"QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause\" 是一个未经控制实验验证的因果性声明。\n\n补充：这一混淆变量问题进一步削弱了 \"decoupling spectrum\" 叙事的说服力。如果 GRPO 的 catastrophic collapse 实际上由 G=4（样本数不足以估计可靠 advantage）导致而非量化精度，那么 spectrum 的排序逻辑（\"RL optimization pressure correlates with decoupling severity\"）就需要重新审视。GRPO bf16 G=8 的 EDCR (0.6318) 实际上比 SFT baseline (0.6982) 更低（Table 2），这意味着去除 QLoRA 的极端案例后，GRPO 并未展现明显 decoupling，反而可能是三种方法中耦合最好的。这与论文的核心叙事 \"GRPO > DPO > RSFT in decoupling severity\" 矛盾。\n\n**[AGREE] R1-N2: 全部结果仅在 dev set 上报告**\n\n完全同意。我在自己的 N4 中也将此列为 critical 问题。DocRED test set 通过 CodaLab 提交是社区标准做法。对于一篇声称 \"85+ configurations\" 系统性实证研究的 EMNLP long paper，完全缺少 test set 结果是不可接受的。\n\n**[AGREE] R1-N3: SFT baseline 缺少多 seed 方差**\n\n同意，这是我遗漏的一个重要问题。+4.92pp 是论文最核心的效果数字（出现在 Abstract、Introduction Contribution 4、Table 1、Conclusion），但 SFT baseline 39.74 仅单 seed。如果 SFT 本身有 ±1pp 的方差（在 LLM fine-tuning 中完全正常），实际改进可能在 +2.9pp 到 +6.9pp 之间，这对论文价值的判断有本质差别。\n\n补充：Table 5 (Appendix) 显示 RSFT CED k=1 的 4 个 seed 范围为 44.16-45.12（range=0.96pp），说明该任务的 seed 方差并非可忽略。SFT 作为 RSFT 的 base model，其方差应至少与 RSFT 在同一量级。不报告 SFT 方差使得所有基于 \"SFT vs RSFT\" 差值的结论（包括 evidence tax、RSFT gain）都缺乏统计基础。\n\n**[AGREE] R1-N4: \"Non-monotonic\" scaling pattern 基于 3 个数据点**\n\n同意核心批评——3 个规模点不足以建立 \"non-monotonic pattern\" 这样强的 claim。我在自己的 W3 中从 1.7B 解释角度质疑了这一发现，但 R1 的表述更精准：即使 3 个点的值完全准确，3 点也无法区分 non-monotonic pattern 与两段独立趋势。\n\n补充两点：\n1. R1 指出 Abstract \"+8pp\" 与正文 \"fair subset +6.2pp\" 的不一致。这不仅是数字问题——如果 fair evaluation 后效果缩水 22%（8.04 → 6.2），说明 raw number 受评估方式影响很大，论文应在 Abstract 中使用更保守的数字。\n2. Table 3 中 Qwen3-1.7B SFT w/ evi 为 47.86 而 No-evi 为 39.82。但同一 table 中 Qwen3-4B 的关系是 SFT w/ evi 39.74 < No-evi 47.21。1.7B with evidence (47.86) 竟然高于 4B with evidence (39.74)，这一反直觉结果暗示 1.7B 和 4B 的训练可能在某些方面不等价（例如训练 convergence 不同、hyperparameter 对不同 scale 的适配度不同），而非单纯的 scale effect。论文未对此做任何讨论。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: EDCR 方法级相关性 ρ=-0.965 仅基于 n=6**\n\n完全同意，且这一问题与我的 N1（EDCR 定义循环性）相互加强。n=6 时 Spearman 相关的 critical value 很高（α=0.05 时需 |ρ|>0.886），即使 ρ=-0.965 在统计上接近显著，去掉 GRPO QLoRA 这个极端 outlier 后（n=5），相关性几乎肯定不再显著。再加上 DPO 3ep 使用了不同评估 protocol（Table 2 脚注），实际可比的数据点仅 4 个。在 4 个数据点上报告 ρ=-0.965 并将其作为 EDCR 有效性的核心证据（Section 6 第 1 段）是明显的 over-claim。\n\n**[AGREE] R1-W2: \"1.7B RSFT matches 8B SFT\" 基于单 seed**\n\n完全同意。50.50 vs 50.51 的 0.01pp 差异远小于合理方差。这一 claim 出现在 Abstract 第 14 行、Introduction Contribution 4、Section 4.4 末段、Conclusion。将其写为 \"matches\" 而非 \"approaches\" 是 over-claim。我补充一个角度：即使多 seed 后均值确实接近，这一比较跨越了不同 model size 和不同 base model capability——1.7B with evidence (47.86) 的 SFT 起点远高于 4B with evidence (39.74)，说明 Qwen3-1.7B 可能在 DocRE 任务上有异常优势（或 4B 有异常劣势），\"1.7B matches 8B\" 可能反映的是 Qwen3 系列特定 scale 的特性而非 RSFT 的通用能力。\n\n**[AGREE] R1-W3: CED vs flat-NLI 差异仅 0.02pp**\n\n完全同意。我在自己的 N2 中将此列为 critical 问题。R1 补充了 flat-NLI 仅 2 seeds 的问题，进一步削弱了比较的可靠性。论文应诚实报告 contrastive 组件在 RSFT selection 中可能不必要。\n\n**[AGREE] R1-W4: Baseline 对比不完整**\n\n同意。我在 W5 中从 Related Work 角度提出了类似问题。缺少与 SAIS/DREEAM/EIDER 的直接表格化对比是一个明显的疏漏。虽然 encoder-based 和 LLM-based 方法不完全 comparable（不同 backbone），但至少应在一个表格中并列呈现 evidence quality（Evi-F1）和 extraction quality（Rel-F1/Ign-F1），让读者自行判断 LLM-based evidence-grounded extraction 相对于 encoder-based 方法的整体位置。Section 4.6 末段的文字提及 \"our best joint Evi-F1 (0.36) falls below supervised DREEAM (54.01%)\"，但这一关键比较被埋在文字中，不在任何表格中。\n\n**[REBUT] R1-W5: RSFT ablation 缺少 random selection baseline**\n\n部分不同意。R1 认为缺少 random-k=1 baseline 使得 \"无法确定改进来自 quality-based selection 还是 sampling diversity\"。但论文在 Table 5 中报告了 RSFT CED k=3 (Ign-F1 43.64) vs k=1 (44.66)。k=3 使用了 3 倍数据量但效果更差，这已经间接回答了 \"更多 diversity 不等于更好\"。同时，RSFT 的训练数据来自 SFT 模型的采样输出，k=1 选最好的和 random k=1 选随机的之间的差异就是 data quality 的差异——如果 random k=1 与原始 SFT 训练数据等价（均为无 selection 的监督学习），那 SFT baseline 本身就是近似的 \"no quality selection\" baseline。\n\n不过，R1 的建议仍有价值：一个 explicit random-k=1 baseline（从 8 个候选中随机选 1 个）可以更干净地控制 \"training on self-generated data\" 这一因素，因为 SFT baseline 训练在 gold data 上而 RSFT 训练在 model-generated data 上，data source 不同。建议作者补充。\n\n**[AGREE] R1-W6: GRPO/DPO 超参数探索不足**\n\n同意，但认为严重程度可降一级。论文的核心论点是不同优化范式之间的结构性差异（gradient-based vs selection-based），而非任一方法的最优配置。如果 GRPO 在 KL=0.001 下不出现 collapse，或 DPO 在 β=0.5 下不出现 gradual decay，那 \"decoupling spectrum\" 叙事就会被根本否定。因此 R1 的建议虽然工作量大，但确实是验证核心 claim 所必需的。至少应测试 1-2 个替代超参数配置。\n\n---\n\n## 缺失引用\n\n**[AGREE]** R1 建议的 multi-task learning 文献（Ruder 2017, Fifty et al. 2021）与我建议的（Standley et al. 2020, Yu et al. 2020）覆盖同一缺口。论文的核心发现——extraction 和 evidence 在梯度优化中竞争——本质上是 multi-task learning 中 negative transfer 的一个实例，不引用这一成熟文献是明显疏漏。\n\n**[AGREE]** Chain-of-thought faithfulness 文献（Lanham et al. 2023）也是相关缺失——evidence generation 可以被视为一种 task-specific rationale generation，其忠实性问题与 CoT faithfulness 直接相关。\n\n---\n\n## 总结\n\nR1 的 4 个 Must-Fix 中我全部同意，其中 N1（混淆变量）和 N3（SFT 缺 multi-seed）是我自己审稿中未充分强调的问题。R1-N1 对 decoupling spectrum 的质疑比我的 N1（EDCR 循环性）更具打击力：如果 GRPO bf16 G=8 的 EDCR (0.6318) 比 SFT (0.6982) 还低，那去除 QLoRA 极端案例后，spectrum 的核心叙事就站不住了。\n\n综合两位 reviewer 的意见，论文的核心问题集中在：\n1. **统计严谨性不足**：SFT 单 seed、n=6 相关性、3 点 non-monotonic claim、单 seed cross-scale 比较\n2. **混淆变量**：GRPO 的 quantization vs group size、1.7B 的 repetition vs evidence benefit\n3. **贡献声明过度**：CED ≈ flat-NLI、EDCR 循环性、\"matches\" vs \"approaches\"\n4. **Dev-only 结果**\n\n维持我的 Overall 3.0 (Findings) 评分。如果 N1-N4 + R1-N1/N3 得到充分解决，有潜力升至 3.5。\n",
    "reviewer_id": "2",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T06:57:18.713460+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4623
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-18T06:57:26.041969+00:00_

交叉回应已提交。

要点总结：R1 的 4 个 Must-Fix 全部 [AGREE]，唯一 [REBUT] 的是 W5（random selection baseline），因为 k=3 vs k=1 的消融和 SFT baseline 已部分回答了 data quality vs diversity 的问题，但仍建议补充 explicit random-k=1。我补充了 R1 未发现的额外证据：GRPO bf16 的 EDCR (0.6318) 实际低于 SFT (0.6982)，说明去除 QLoRA 极端案例后 spectrum 叙事可能不成立；1.7B SFT w/evi (47.86) > 4B SFT w/evi (39.74) 这一反直觉结果暗示 scale effect 可能被 model-specific 因素混淆。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---

## Round 3

70 recorded events

### User

_source line 67 · 2026-05-23T00:52:17.474808+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。

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

1. **贡献原创性**：
   - Contribution 1（evidence tax is scale-dependent）：这是一个实验观察，不是方法创新。是否足够构成独立贡献？
   - Contribution 2（decoupling spectrum）：GRPO/DPO/RSFT 表现不同是一个经验发现。EDCR 是新指标，但定义简单（ratio of two recalls）——是否足够 novel？
   - Contribution 3（RSFT variance compression）：RSFT 本身不是新方法（论文承认 "well-established"），应用于 DocRE + CED scoring 是否足够新颖？
   - 整体：论文更像 empirical study + scaling analysis，还是有实质性方法贡献？对 EMNLP 来说是否足够？

2. **Related Work 覆盖**：
   - DocRE 领域是否有遗漏的重要工作？特别是 2024-2025 的 LLM-based DocRE 方法。
   - RSFT/rejection sampling 在其他 NLP 任务的应用是否充分讨论？
   - Multi-objective RL 和 reward hacking 的文献是否充分？
   - NLI-based evaluation 在 IE 领域的先驱工作是否覆盖？
   - 搜索最新相关工作，检查是否有遗漏。

3. **论文结构与叙事**：
   - Abstract 是否准确反映论文内容？是否过度声明？
   - Introduction 的 "gap" 叙事（accurate extractors have no evidence, evidence-capable methods are not competitive）是否有力？
   - Method section 是否清晰？CED 和 EDCR 各自的角色是否容易理解？
   - Experiments 结构是否合理？主实验、scaling、ablation 的安排是否自然？
   - Analysis section 是否提供了超越 experiments 的洞察？
   - Conclusion 是否恰当总结？是否有过度声明？

4. **格式合规检查**：
   - 正文是否在 8 页以内？
   - Limitations section 是否存在且内容适当？
   - Ethics statement 是否存在？
   - 匿名是否完整（无作者信息泄露、无 self-reference）？
   - 引用格式是否使用 natbib？
   - 表格/图片质量是否达到出版标准？
   - ARR Responsible NLP Checklist 是否在 OpenReview form 中（而非 PDF 中）？

5. **写作质量**：
   - 技术写作是否清晰、准确？
   - 是否有语法/拼写错误？
   - 数字引用是否一致（论文中的数字是否与表格一致）？
   - 是否有 AI 写作风格的痕迹（过度使用特定短语模式）？

6. **Limitations 评估**：
   - 论文的 limitations section 是否诚实覆盖了真正的限制？
   - 是否有未提及的重要限制？

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-23T00:52:28.696484+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-23T00:52:28.748083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-23T00:52:34.772637+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
  "project": "faith-evidence-ie",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
    "project": "faith-evidence-ie",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-23T00:52:35.728485+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-23T00:52:35.981002+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM document-level relation extraction 2024 2025 recent work"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM document-level relation extraction 2024 2025 recent work"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-23T00:52:36.132045+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 543.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.3}, {\"page\": 10, \"pa
…[truncated 427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1359
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-23T00:52:43.076299+00:00_

Web search results for query: "LLM document-level relation extraction 2024 2025 recent work"

Links: [{"title":"(PDF) LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/383428854_LLM_with_Relation_Classifier_for_Document-Level_Relation_Extraction"},{"title":"[2408.13889] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v2"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/pdf/2408.13889"},{"title":"SyRACT: zero-shot biomedical document-level relation extraction with synergistic RAG and CoT | Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bioinformatics/article/41/7/btaf356/8169328"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-demos.20/"},{"title":"Data and text mining SyRACT: zero-shot biomedical document-level relation","url":"https://academic.oup.com/bioinformatics/article-pdf/41/7/btaf356/63528032/btaf356.pdf"}]

Based on the search results, here are some recent developments in LLM-based document-level relation extraction (DocRE) for 2024-2025:

## Key Recent Work

**LLM with Relation Classifier Approach:**
Despite their advancement, LLM-based methods still lag behind traditional approaches in document-level relation extraction, with LLMs' dispersion of attention on entity pairs without relations identified as a primary factor. A recent solution significantly outperforms recent LLM-based DocRE models and narrows the performance gap with state-of-the-art BERT-based models.

**AutoRE System (2024):**
The AutoRE system introduces an RH
…[truncated 842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7095
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-23T00:52:43.127694+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the web search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Guidelines

Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The ARR metareview score was changed in February 2025 to be more aligned with reviewer scores. Like with reviews, the score should be backed up by the meta-review text. The new options include: 5 = Consid
…[truncated 380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7399
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-23T00:52:50.606990+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
  "project": "faith-evidence-ie",
  "pages": "11-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
    "project": "faith-evidence-ie",
    "pages": "11-17",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-23T00:52:52.523059+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 117.3}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1916
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-23T00:52:52.573658+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions (soundness, excitement, overall assessment), their scales, and detailed descriptions of each score level. Include any guidance on what constitutes a strong vs weak paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions (soundness, excitement, overall assessment), their scales, and detailed descriptions of each score level. Include any guidance on what constitutes a strong vs weak paper."
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-23T00:52:53.579637+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-23T00:52:54.186370+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-23T00:52:54.940152+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-23T00:52:54.992423+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-23T00:52:55.797051+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-23T00:52:55.797565+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-23T00:52:56.201461+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2015
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-23T00:52:57.359370+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2366
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-23T00:52:58.317117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2519
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-23T00:52:58.418605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2621
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-23T00:52:58.469249+00:00_

# ARR Review Form Criteria and Scoring

Based on the guidelines provided, ARR uses **three primary scoring dimensions** for reviews (as of February 2025):

## Scoring Dimensions

**1. Soundness**
This evaluates technical rigor and validity. Scores must be justified by the review text—"low soundness scores without sufficient justification" indicate problematic reviews. Reviewers should assess methodology, proofs, argumentation, and experimental design.

**2. Excitement**
This reflects subjective personal interest, orthogonal to soundness. A reviewer might find work technically sound yet personally unexciting, or vice versa. This dimension captures individual taste preferences.

**3. Overall Assessment**
A composite recommendation considering soundness, excitement, novelty, and impact together. Papers can merit acceptance despite low personal excitement if they offer significant contributions (e.g., "improvements in efficiency" or "high-quality resource").

## Key Guidance on Strong vs. Weak Papers

**Strong papers demonstrate:**
- Clear research questions advancing the field's knowledge
- Appropriate methodology for their claims
- Sufficient evidence supporting their contributions
- Technical soundness and reproducibility details

**Weak papers exhibit:**
- Unclear contributions or overscoped claims
- Methodological flaws or incomplete proofs
- Insufficient justification for design choices
- Missing critical information for reproducibility

The guidelines emphasize that reviewers must avoid common biases—criticizing work for lacking SOTA results, using simple methods, or appearing "surprising"—as these don't necessarily indicate weakness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5895
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-23T00:53:06.409448+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-23T00:53:07.013066+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-23T00:53:07.315634+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-23T00:53:07.316148+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-23T00:53:08.220965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1207
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-23T00:53:08.221780+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-23T00:53:08.322473+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-23T00:53:08.824951+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-23T00:53:09.228135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-23T00:53:09.279912+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-23T00:53:09.685915+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-23T00:53:09.786814+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-23T00:53:10.595618+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1315
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-23T00:53:10.596926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-23T00:53:10.697712+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-23T00:53:11.314413+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-23T00:53:11.504809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-23T00:53:11.505287+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-23T00:53:12.410535+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1096
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-23T00:53:12.612116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1106
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-23T00:53:20.699068+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-23T00:53:21.212247+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-23T00:53:21.614872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 915
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-23T00:53:21.616698+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-23T00:53:21.617275+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "rejection sampling fine-tuning NLP language model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "rejection sampling fine-tuning NLP language model 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-23T00:53:22.571341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRPO DPO reinforcement learning NLP information extraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRPO DPO reinforcement learning NLP information extraction 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-23T00:53:22.827624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NLI natural language inference evaluation information extraction faithfulness 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NLI natural language inference evaluation information extraction faithfulness 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-23T00:53:28.700679+00:00_

Web search results for query: "rejection sampling fine-tuning NLP language model 2024 2025"

Links: [{"title":"Rejection Fine-Tuning (RFT)","url":"https://www.emergentmind.com/topics/rejection-fine-tuning-rft"},{"title":"Breaking the Attention Trap in Code LLMs: A Rejection ...","url":"https://aclanthology.org/2025.findings-emnlp.592.pdf"},{"title":"Improving negative rejection ability in language models: A review of fine-tuned LLMs, RAG, and RAFT | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00334-6"},{"title":"[Literature Review] RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models","url":"https://www.themoonlight.io/en/review/rs-dpo-a-hybrid-rejection-sampling-and-direct-preference-optimization-method-for-alignment-of-large-language-models"},{"title":"Min-p, Max Exaggeration: A Critical Analysis of Min-p Sampling in Language Models","url":"https://arxiv.org/pdf/2506.13681"},{"title":"Rejection Sampling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/09-rejection-sampling"},{"title":"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning","url":"https://arxiv.org/pdf/2602.04391"},{"title":"Statistical Rejection Sampling Improves Preference Optimization | OpenReview","url":"https://openreview.net/forum?id=xbjSwwrQOe"}]

Based on the search results, here's what I found about rejection sampling for fine-tuning NLP language models in 2024-2025:

## Recent Developments in Rejection Sampling Fine-Tuning (RFT)

**Core Methodology:**
Rejection sampling is a widely adopted method where a teacher model generates multiple candidate trajectories for a given problem, retaining only those with correct final answers, followed by rejection sampling fine-tuning (RFT) which performs supervised training on this filtered set of correct trajectories.

**Recent Innovations (2024-20
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7083
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-23T00:53:29.303890+00:00_

Web search results for query: "GRPO DPO reinforcement learning NLP information extraction 2024 2025"

Links: [{"title":"The best NLP papers of 2025 - The best NLP papers","url":"https://thebestnlppapers.com/"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"A Guide to Reinforcement Learning Post-Training for LLMs: PPO, DPO, GRPO, and Beyond","url":"https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms"},{"title":"Can GRPO Help LLMs Transcend Their Pretraining Origin?","url":"https://arxiv.org/pdf/2510.15990"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"}]

Based on the search results, here's what I found about GRPO, DPO, reinforcement learning, and NLP in 2024-2025:

## GRPO (Group Relative Policy Optimization)

GRPO has become a dominant approach to advancing reasoning capabilities of Large Language Models, powered by reinforcement learning with verifiable rewards. GRPO is an unbiased optimization method that improves token efficiency while maintaining reasoning performance.

GRPO was introduced in 2024 and used successfully to train DeepSeek-R1 models for promoting reasoning capabilities of LLMs using verifiable or binary rewards. This approach is credited with state-of-the-art performance in complex reasoning domains, such as math problem-solving and programming.

## DPO (Direct Preference Optimization)

DPO doesn't use a separate Reward Model neural network, but instead extracts the optimal reward directly from the preference data. Preference Optimization aligns the model with human values and preferences, where DPO and its variants operate.

## Recent Developments (2025-2026)

DAPO (ByteDance/Tsinghua, 2025) tackles the sp
…[truncated 447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6732
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-23T00:53:30.659423+00:00_

Web search results for query: "NLI natural language inference evaluation information extraction faithfulness 2024 2025"

Links: [{"title":"Natural Language Inference (NLI)","url":"https://www.emergentmind.com/topics/natural-language-inference-nli"},{"title":"SemEval 2024 Task 2: Safe Biomedical Natural Language Inference for Clinical Trials | ACL Member Portal","url":"https://www.aclweb.org/portal/content/semeval-2024-task-2-safe-biomedical-natural-language-inference-clinical-trials-2"},{"title":"Natural Language Inference - Complete Guide | AI Wiki","url":"https://artificial-intelligence-wiki.com/natural-language-processing/nlp-tasks-and-applications/natural-language-inference/"},{"title":"SemEval-2024 Task 2: Safe Biomedical Natural Language Inference for Clinical Trials","url":"https://arxiv.org/html/2404.04963v1"},{"title":"With a Little Push, NLI Models can Robustly and Efficiently Predict   Faithfulness","url":"https://arxiv.org/pdf/2305.16819"},{"title":"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks - ACL Anthology","url":"https://aclanthology.org/2024.eacl-long.102/"},{"title":"SEME at SemEval-2024 Task 2: Comparing Masked and Generative Language   Models on Natural Language Inference for Clinical Trials","url":"https://arxiv.org/pdf/2404.03977"},{"title":"Natural Language Inference - Practical Guide 2025 | ShadeCoder","url":"https://www.shadecoder.com/topics/natural-language-inference-a-comprehensive-guide-for-2025"}]

I've found relevant information about NLI, evaluation, and faithfulness from 2024-2025. Here are the key findings:

## Natural Language Inference Evaluation & Faithfulness (2024-2025)

**Clinical Domain Applications:**
SemEval 2024 Task 2 explored models' ability in textual entailment using breast cancer Clinical Trial Reports, focusing on aspects like numerical reasoning and domain-specific vocabulary, with the goal of analyzing models' robustness, consistency, and faithfulness in reaso
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7831
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-23T00:53:35.329139+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "evidence-grounded relation extraction faithfulness verification 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "evidence-grounded relation extraction faithfulness verification 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-23T00:53:36.333207+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-objective reward hacking reinforcement learning language model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-objective reward hacking reinforcement learning language model 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-23T00:53:36.835364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocRED Re-DocRED LLM 2025 2026 new methods benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocRED Re-DocRED LLM 2025 2026 new methods benchmark"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-23T00:53:42.282660+00:00_

Web search results for query: "evidence-grounded relation extraction faithfulness verification 2024 2025"

Links: [{"title":"Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking","url":"https://www.mdpi.com/2073-431X/15/3/178"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Extracting or Guessing? Improving Faithfulness of Event Temporal   Relation Extraction","url":"https://arxiv.org/pdf/2210.04992"},{"title":"Aman's AI Journal • Primers • Factuality in LLMs","url":"https://aman.ai/primers/ai/factuality-in-LLMs/"},{"title":"Enhancing Relation Extraction via Supervised Rationale Verification and   Feedback","url":"https://arxiv.org/pdf/2412.07289"},{"title":"Read it Twice: Towards Faithfully Interpretable Fact Verification by   Revisiting Evidence","url":"https://arxiv.org/pdf/2305.03507"}]

Here are the search results for "evidence-grounded relation extraction faithfulness verification 2024 2025":

The search returned several relevant papers and resources on this topic:

1. **Grounded Knowledge Graph Extraction via LLMs** - A recent framework (March 2026) proposes that if all three elements of a triplet can be independently traced back to the source text through hierarchical matching, then the triplet is highly likely to be faithful.

2. **ACL 2025 Proceedings** - ACL 2025 includes an accepted paper on "ODDA: An OODA-Driven Diverse Data Augmentation Framework for Low-Resource Relation Extraction", along with other papers on verification and reasoning.

3. **Enhancing Relation Extraction via Supervised Rationale Verification** - A recent study (2024) focuses on exploring the verification and feedback mechanism of LLMs for relation extraction, specifically examining whether the relation prediction of LLMs is biased by verifying the rationale and providing feedback for correction.

4. **Faithfulness in Event Temporal Relation Extraction** - Research has ex
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6953
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-23T00:53:44.141213+00:00_

Web search results for query: "multi-objective reward hacking reinforcement learning language model 2024 2025"

Links: [{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://arxiv.org/html/2509.15557v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Reward Modeling in Reinforcement Learning | Apolo AI Launchpad - Secure, Industry-Tailored AI Tools for Regulated Enterprises","url":"https://www.apolo.us/blog-posts/reward-modeling-in-reinforcement-learning"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/pdf/2602.18037"},{"title":"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR","url":"https://arxiv.org/pdf/2603.07084"}]

Here are the key findings from the web search on multi-objective reward hacking in reinforcement learning for language models in 2024-2025:

## Reward Hacking in Language Model RL

Reward hacking occurs when a reinforcement learning (RL) agent exploits flaws or ambiguities in the reward function to achieve high rewards, without genuinely learning or completing the intended task. With the rise of language models generalizing to a broad spectrum of tasks and RLHF becomes a de facto method for alignment training, reward hacking in RL training of language models has become a critical practical challenge.

## Manifestations in Reasoning Models

Common manifestations of reward hacking reported in the literature include reasoning without solving, using too few or overly short steps, producing meaningless repetitions or ex
…[truncated 1199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7808
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-23T00:53:44.599059+00:00_

Web search results for query: "DocRED Re-DocRED LLM 2025 2026 new methods benchmark"

Links: [{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889"},{"title":"GitHub - tonytan48/Re-DocRED","url":"https://github.com/tonytan48/Re-DocRED"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"},{"title":"tonytan48/Re-DocRED · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tonytan48/Re-DocRED"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"Revisiting DocRED -- Addressing the False Negative Problem in Relation   Extraction","url":"https://arxiv.org/pdf/2205.12696"},{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/pdf/2511.08143"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/pdf/2408.13889"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/pdf/1906.06127"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v3"}]

Based on the search results, here's what I found about DocRED, Re-DocRED, and recent LLM-based methods in document-level relation extraction:

## Datasets

DocRED is a widely used benchmark for document-level relation extraction. However, the DocRED dataset contains a significant percentage of false negative examples (incomplete annotation). To address this, researchers revised 4,053 documents in the DocRED dataset and released this as the Re-DocRED dataset. The Re-DocRED Dataset resolved the incompleteness problem by supplementing relation triples, addressed logical inconsistencies in DocRED, and correc
…[truncated 1018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7763
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-23T00:58:16.334378+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SummaC NLI faithfulness inconsistency detection summarization Laban 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SummaC NLI faithfulness inconsistency detection summarization Laban 2022"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-23T00:58:17.138029+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Enhancing Relation Extraction via Supervised Rationale Verification\" 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Enhancing Relation Extraction via Supervised Rationale Verification\" 2024 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-23T00:58:21.455007+00:00_

Web search results for query: "SummaC NLI faithfulness inconsistency detection summarization Laban 2022"

Links: [{"title":"(PDF) SummaC : Re-Visiting NLI-based Models for Inconsistency Detection in Summarization","url":"https://www.researchgate.net/publication/358553684_SummaC_Re-Visiting_NLI-based_Models_for_Inconsistency_Detection_in_Summarization"},{"title":"SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00453/109470/SummaC-Re-Visiting-NLI-based-Models-for"},{"title":"SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization - ACL Anthology","url":"https://aclanthology.org/2022.tacl-1.10/"},{"title":"SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization","url":"https://scite.ai/reports/summac-re-visiting-nli-based-models-for-5GEpA4rV"},{"title":"[PDF] SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SummaC:-Re-Visiting-NLI-based-Models-for-Detection-Laban-Schnabel/ee1ef7b70dc34adcc90c42cc28168165ea56501f"},{"title":"GitHub - tingofurro/summac: Codebase, data and models for the SummaC paper in TACL · GitHub","url":"https://github.com/tingofurro/summac"},{"title":"[2111.09525] SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization","url":"https://arxiv.org/abs/2111.09525"},{"title":"Paper Review - SUMMAC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization | Liyan Tang","url":"https://www.tangliyan.com/blog/posts/summac/"}]

Based on the search results, here's what I found about SummaC:

SummaC is research by Laban et al. (2022) that addresses the problem of using NLI models for inconsistency detection in summarization. The work found that past approaches suffered from a mismatch in input granulari
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5120
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-23T00:58:23.011346+00:00_

Web search results for query: ""Enhancing Relation Extraction via Supervised Rationale Verification" 2024 arxiv"

Links: [{"title":"[2412.07289] Enhancing Relation Extraction via Supervised Rationale Verification and Feedback","url":"https://arxiv.org/abs/2412.07289"},{"title":"[Literature Review] Enhancing Relation Extraction via Supervised Rationale Verification and Feedback","url":"https://www.themoonlight.io/en/review/enhancing-relation-extraction-via-supervised-rationale-verification-and-feedback"},{"title":"Enhancing Relation Extraction","url":"https://arxiv.org/pdf/2412.07289"},{"title":"Enhancing Relation Extraction via Supervised Rationale Verification and Feedback","url":"https://arxiv.org/html/2412.07289v1"},{"title":"Enhancing Relation Extraction via Supervised Rationale Verification and Feedback | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34631"},{"title":"dblp: Enhancing Relation Extraction via Supervised Rationale Verification and Feedback.","url":"https://dblp1.uni-trier.de/rec/conf/aaai/0002MZXRQ25.html"},{"title":"Enhancing Relation Extraction via Supervised Rationale ...","url":"https://powerdrill.ai/discover/discover-Enhancing-Relation-Extraction-cm4kdkyiw5kp807ltdqfr9iom"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Enhancing Relation Extraction via Supervised Rationale Verification and Feedback"

**arxiv Details:** arXiv paper 2412.07289, submitted December 10, 2024

**Authors:** Yongqi Li, Xin Miao, Shen Zhou, Mayi Xu, Yuyang Ren, Tieyun Qian

**Overview:**
Despite the rapid progress in automated feedback methods for large language models (LLMs), these methods cannot be well applied to relation extraction (RE) due to their designated feedback objectives and correction manner. The paper proposes a novel automated feedback framework for RE with a rationale supervisor to verify the rationale and provide re-selected demonstrations 
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5873
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-23T00:58:36.573130+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 131 · 2026-05-23T00:58:36.624425+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-23T00:58:40.599160+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-23T00:58:40.700184+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-23T01:01:25.653016+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（新颖性 + 完整性）\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n### Summary（2-3句）\n\n本文研究 LLM-based DocRE 中证据生成的代价（\"evidence tax\"），比较 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3 (1.7B/4B/8B/14B) 和 LLaMA-3.1-8B 上的表现。主要发现：evidence tax 是规模依赖的（1.7B 时证据有益，4B 近似中性），GRPO 导致灾难性抽取-证据解耦而 RSFT 通过离散选择避免解耦，RSFT 将训练方差压缩 4.6–31 倍。论文提出 CED（基于 NLI 的证据评分函数）和 EDCR（Evidence-Decoupling Ratio）作为分析工具。\n\n---\n\n### Strengths（逐条）\n\n**S1. 系统性的多因子实验设计。** 三种优化范式 × 四个 Qwen3 规模 + 一个 cross-family 验证（LLaMA-3.1-8B） × 两个数据集（DocRED + Re-DocRED），coverage 在 LLM-based DocRE 工作中属上乘。controlled evaluation subset（Appendix D）和 matched@2048 协议的设计体现了对实验混淆因素的认真处理。\n\n**S2. CED 评分函数设计合理。** 通过 NLI 模型构建 contrastive premises（Section 3.4），区分\"证据确实支持关系\"和\"仅实体共现\"。contrastive formulation 的消融（Appendix B）确认了设计必要性——flat-NLI baseline 虽可产生 comparable RSFT 结果，但 contrastive formulation 在 per-triple discrimination 上更优。\n\n**S3. RSFT 方差压缩具有实际价值。** 4B 训练方差从 3.80pp（SFT）降至 0.51pp（RSFT CED），对需要可重复部署的场景有直接意义。1.7B RSFT（51.19 Ign-F1, std 0.09pp）超过 8B SFT（50.19, std 3.22pp），Cohen's d=2.58，为小模型+质量过滤的部署策略提供了有力经验依据。\n\n**S4. 分析层次丰富。** per-relation EDCR 分析（Figure 4，93 个关系类型的分布）、训练动态可视化（Figure 3，GRPO 崩溃轨迹）、定性案例分析（Section M，三类 EDCR 诊断案例）从统计、过程、实例三层支持核心论点。Table 14 的 evidence citation comparison 尤其有说服力。\n\n**S5. 写作质量高。** \"evidence tax\" 概念定义清晰并贯穿全文，decoupling spectrum 的叙事框架使三种方法的对比一目了然。Abstract 中给出的关键数字均可在正文中追溯。\n\n---\n\n### Weaknesses（逐条）\n\n**W1 [CRITICAL] 方法论原创性不足——三个贡献均为经验观察**\n\n论文的三个 claim 逐一审视：\n- **C1**（evidence tax 规模依赖）：对 4 个规模点的实验观察，不是方法创新。\n- **C2**（decoupling spectrum）：GRPO/DPO/RSFT 表现不同本质上反映了 gradient-based optimization vs. selection-based filtering 的已知根本差异——前者可 exploit multi-objective reward landscape，后者天然避免这一问题。EDCR 是两个 recall 的简单比值（公式 2），定义本身缺乏技术深度。\n- **C3**（RSFT 方差压缩）：RSFT 论文明确承认是 \"well-established\"（Section 3.3），应用于 DocRE + CED scoring 的组合虽然有效，但方法贡献有限。\n\nCED 基于现有 NLI 模型（DeBERTa-v3-large），EDCR 是两个 recall 的比值。这些分析工具有用，但作为独立贡献偏弱。整体定位更接近 **empirical study with analytical tools**。对 EMNLP main conference 而言，需要更强的方法创新性。\n\n**W2 [MAJOR] Scaling claim 的数据基础偏弱**\n\n\"Scale-dependent evidence tax\" 作为第一贡献，在 Qwen3 家族内仅有 4 个规模点（1.7B, 4B, 8B, 14B——其中 14B 仅为 validation），cross-family 仅 1 个点（LLaMA-3.1-8B）。4 个点不足以可靠区分线性、对数、阶梯等 scaling pattern。\n\n更重要的是，不同规模的数据呈现非单调性：1.7B RSFT（51.19 Ign-F1）超过 4B RSFT（44.82, Table 1），甚至超过 8B SFT（50.19）。论文在 Section 4.4 和 Appendix D 讨论了 truncation rate 差异和 matched@2048 协议，但主文中不同规模的数字是否全部来自同一 evaluation protocol 不够清晰——读者需要翻阅 Appendix 才能理解数字间的关系。建议在 Table 1 旁或 Section 4 开头明确列出所有规模在同一协议下的对比表。\n\n**W3 [MAJOR] GRPO 崩溃分析缺乏机制深度**\n\nSection 4.3 对 GRPO QLoRA catastrophic collapse 的分析停留在现象描述层面（\"extraction collapses to Rel-F1 1.41, Evi-F1 rises to 85.04\"），未提供机制解释。这本质上是 multi-objective reward hacking 的一个实例——optimizer 发现牺牲 extraction accuracy 可以最大化 evidence-weighted reward。论文未：\n1. 连接到 reward hacking 文献（如 Weng 2024 综述; Fu et al. 2025 的 reward shaping 原则）\n2. 探讨简单缓解策略（reward clipping, 不同 KL 系数如 0.1/0.5, reward normalization）是否能避免 collapse\n3. 分析 full-precision GRPO 也部分避免 collapse 是否仅因为梯度精度差异\n\n如果 GRPO collapse 仅在 β=0.01 的 QLoRA 设置下发生，这更像是超参数/精度问题而非方法本质差异，\"decoupling spectrum\" 的框架就不够稳固。\n\n**W4 [MINOR] Related Work 存在遗漏**\n\n以下近期相关工作未被引用或讨论：\n1. **LMRC**（Li & Zhang, 2024; arXiv 2408.13889）——LLM with Relation Classifier for DocRE，针对 LLM 注意力分散问题，在 LLM-based DocRE 中表现突出，应在 Section 2 LLM-based DocRE 部分讨论。\n2. **RelPrior**（Huang et al., 2025; arXiv 2511.08143）——\"Relation as a Prior\" 范式，claim 超越现有 LLM-based DocRE 方法。\n3. **SummaC**（Laban et al., 2022, TACL）——NLI-based faithfulness evaluation 的先驱工作，CED 的设计理念（sentence-level NLI scoring 用于 faithfulness 判断）与之直接相关，应在 Section 3.4 讨论设计动机时引用。\n4. **Rationale Verification for RE**（Li et al., 2024; AAAI 2025, arXiv 2412.07289）——使用 rationale supervisor 验证 LLM 的 RE 推理，与本文的 evidence verification 主题高度相关。\n\n**W5 [MINOR] CED 对外部 NLI 模型的 sensitivity analysis 不足**\n\nCED 评分完全取决于 NLI 模型能力。论文仅在 Appendix B 比较了 DeBERTa-v3-large vs. v3-base（差异\"可忽略\"），但：\n- 未测试其他 NLI 模型家族（如生成式 NLI 模型）\n- 未分析 NLI 模型在 DocRE 领域的 out-of-distribution 行为——DocRE 中的证据句往往包含多个实体和复杂共指，与标准 NLI 训练分布差异较大\n- 若 NLI 模型对某些 relation type 存在系统性偏差，EDCR 诊断可能产生误导性结论\n\n**W6 [MINOR] Limitations section 遗漏了若干重要限制**\n\nLimitations（Section 7）覆盖面尚可但遗漏：\n- DocRED 的证据标注已知不完整（Re-DocRED 论文已指出），这对 CED/EDCR 基于 gold evidence 的计算可靠性有直接影响\n- 三种方法的计算成本差异未提及——GRPO 需要 G 个 candidate generation + value estimation，DPO 需要 preference pair 构建，RSFT 需要 N=5 采样 + CED scoring，公平对比应包含 cost analysis\n- 仅评估 DocRE 一种 IE 任务，findings 是否 generalize 到 NER、事件抽取等未讨论\n\n---\n\n### Questions（需要作者澄清的）\n\n**Q1.** Abstract 中 1.7B RSFT 的 51.19 Ign-F1 与 Table 1 中 4B RSFT CED 的 44.82 使用的是同一 evaluation protocol 吗？如果不同（如 matched@2048 vs. standard dev-set），请在主文中明确标注每个数字的 evaluation protocol，避免读者跨表对比时产生困惑。\n\n**Q2.** GRPO collapse 是否在其他 KL 系数（如 0.1, 0.5）或不使用 QLoRA（full-precision）时依然发生？Section 4.3 提到 full-precision GRPO \"avoids extreme decoupling\"（EDCR 0.6797），那么 QLoRA 的量化精度损失是否是 collapse 的主要原因而非 GRPO 方法本身？\n\n**Q3.** EDCR 与 Rel-F1 的负相关（ρ=−0.93, Section 5）是在仅 7 个 method configurations 上计算的。n=7 的 Spearman 相关有较大的 sampling variability——bootstrap 95% CI 是多少？是否在不同 seed 下稳定？\n\n**Q4.** CED contrastive premise 中收集的 \"entity-sharing negatives\"（Section 3.4）是否包含了实际成立但未被标注的关系（即 DocRED 的 false negatives）？Re-DocRED 标注密度是 DocRED 的 2.82×，这意味着 DocRED 上大量 \"negative\" 其实是 false negative，会如何影响 CED score 的可靠性？\n\n**Q5.** RSFT 的 N=5 candidates 是如何选择的？如果增加到 N=50 或 100（更接近 best-of-N scaling），解耦行为是否会改变？论文对 RSFT \"avoids decoupling\" 的机制解释（Section F, \"discrete selection\"）在 N→∞ 的极限下是否依然成立？\n\n**Q6.** Table 12 的 encoder-based comparison 显示 TP-only Evi-F1 超过 80%，但 joint Evi-F1 仅 54.15。论文 claim \"when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods\"——但 joint evaluation 的巨大 gap（54.15 vs. encoder 的更高值）说明 LLM 方法的主要瓶颈不在 evidence quality 而在 extraction precision。这是否削弱了论文对 \"evidence-grounded extraction\" 实用性的 claim？\n\n---\n\n### Missing References\n\n1. Li, X., & Zhang, M. (2024). LLM with Relation Classifier for Document-Level Relation Extraction. arXiv:2408.13889. — 重要的 LLM-based DocRE baseline\n2. Huang, N., et al. (2025). Relation as a Prior for LLM-based Document-level Relation Extraction. arXiv:2511.08143. — 最新 LLM-based DocRE 范式\n3. Laban, P., et al. (2022). SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization. TACL. — CED 设计理念的先驱\n4. Li, Y., et al. (2025). Enhancing Relation Extraction via Supervised Rationale Verification and Feedback. AAAI 2025. — RE 中的 rationale verification\n5. Reward hacking 相关文献（如 Weng 2024 综述）——GRPO collapse 分析的理论背景\n\n---\n\n### Overall Assessment\n\n## 总体评分\n**Overall**: 3.0（Findings — 可被 Findings 接收）\n**一句话总结**: 设计良好的 empirical study，实验覆盖面和分析深度出色，但三个核心贡献均为经验观察，缺乏足以进入 main conference 的方法创新性。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计扎实，controlled evaluation 和多 seed 验证体现严谨性；但 scaling claim 基于有限数据点，GRPO collapse 的机制分析不足，不同规模数字的 evaluation protocol 对应关系不够清晰 |\n| Excitement | 2.5/5 | Evidence tax 概念有趣，RSFT 方差压缩对实践有价值；但方法组件（CED/EDCR/RSFT 应用）各自偏简单，无显著方法创新，核心 insight（selection-based > gradient-based for multi-objective）在 RL 社区不算新颖 |\n| Reproducibility | 4/5 | 超参数详细列出（Appendix A），声明将 release code and outputs，多 seed 实验设计好；但 CED 依赖特定 NLI 模型版本，未提供 CED scoring 的独立复现指南 |\n| Overall | 3.0/5 | Findings 水平——经验发现有社区参考价值，但缺乏 main conference 所需的方法创新深度 |\n\n**置信度**: 4/5 — 对 DocRE 和 LLM post-training 方法较为熟悉\n\n**理由**: 本文是一项覆盖面广、分析深入的 empirical study。Evidence tax 的规模依赖性发现和 RSFT 方差压缩的实践价值是真实的贡献。但论文的定位困境在于：三个核心贡献均为经验观察（不是方法创新），分析工具（CED = NLI scoring, EDCR = recall ratio）定义简单，RSFT 本身不是新方法。\"Decoupling spectrum\" 框架虽然叙事有力，但深层机制（为什么 gradient methods 解耦、selection methods 不解耦）在 multi-objective optimization 文献中已有大量讨论（reward hacking, Goodhart's Law），本文未充分连接。\n\n建议以 Findings 接收，但需要以下修改：\n1. **弱化 scaling claim 表述**或增加更多规模点/模型家族——当前 4 个 Qwen3 点 + 1 个 LLaMA 点不足以 claim \"scale-dependent\" 作为一个 general 结论\n2. **深化 GRPO collapse 的机制分析**——连接 reward hacking 文献，测试不同 KL 系数/精度，区分\"方法问题\"和\"超参数问题\"\n3. **主文中统一 evaluation protocol 的展示**——当前不同规模的数字散布在主文、appendix、不同 evaluation 设置中，读者追溯困难\n4. **补充 missing references**（至少 LMRC 和 SummaC）",
  "reviewer_id": "2",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（新颖性 + 完整性）\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n### Summary（2-3句）\n\n本文研究 LLM-based DocRE 中证据生成的代价（\"evidence tax\"），比较 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3 (1.7B/4B/8B/14B) 和 LLaMA-3.1-8B 上的表现。主要发现：evidence tax 是规模依赖的（1.7B 时证据有益，4B 近似中性），GRPO 导致灾难性抽取-证据解耦而 RSFT 通过离散选择避免解耦，RSFT 将训练方差压缩 4.6–31 倍。论文提出 CED（基于 NLI 的证据评分函数）和 EDCR（Evidence-Decoupling Ratio）作为分析工具。\n\n---\n\n### Strengths（逐条）\n\n**S1. 系统性的多因子实验设计。** 三种优化范式 × 四个 Qwen3 规模 + 一个 cross-family 验证（LLaMA-3.1-8B） × 两个数据集（DocRED + Re-DocRED），coverage 在 LLM-based DocRE 工作中属上乘。controlled evaluation subset（Appendix D）和 matched@2048 协议的设计体现了对实验混淆因素的认真处理。\n\n**S2. CED 评分函数设计合理。** 通过 NLI 模型构建 contrastive premises（Section 3.4），区分\"证据确实支持关系\"和\"仅实体共现\"。contrastive formulation 的消融（Appendix B）确认了设计必要性——flat-NLI baseline 虽可产生 comparable RSFT 结果，但 contrastive formulation 在 per-triple discrimination 上更优。\n\n**S3. RSFT 方差压缩具有实际价值。** 4B 训练方差从 3.80pp（SFT）降至 0.51pp（RSFT CED），对需要可重复部署的场景有直接意义。1.7B RSFT（51.19 Ign-F1, std 0.09pp）超过 8B SFT（50.19, std 3.22pp），Cohen's d=2.58，为小模型+质量过滤的部署策略提供了有力经验依据。\n\n**S4. 分析层次丰富。** per-relation EDCR 分析（Figure 4，93 个关系类型的分布）、训练动态可视化（Figure 3，GRPO 崩溃轨迹）、定性案例分析（Section M，三类 EDCR 诊断案例）从统计、过程、实例三层支持核心论点。Table 14 的 evidence citation comparison 尤其有说服力。\n\n**S5. 写作质量高。** \"evidence tax\" 概念定义清晰并贯穿全文，decoupling spectrum 的叙事框架使三种方法的对比一目了然。Abstract 中给出的关键数字均可在正文中追溯。\n\n---\n\n### Weaknesses（逐条）\n\n**W1 [CRITICAL] 方法论原创性不足——三个贡献均为经验观察**\n\n论文的三个 claim 逐一审视：\n- **C1**（evidence tax 规模依赖）：对 4 个规模点的实验观察，不是方法创新。\n- **C2**（decoupling spectrum）：GRPO/DPO/RSFT 表现不同本质上反映了 gradient-based optimization vs. selection-based filtering 的已知根本差异——前者可 exploit multi-objective reward landscape，后者天然避免这一问题。EDCR 是两个 recall 的简单比值（公式 2），定义本身缺乏技术深度。\n- **C3**（RSFT 方差压缩）：RSFT 论文明确承认是 \"well-established\"（Section 3.3），应用于 DocRE + CED scoring 的组合虽然有效，但方法贡献有限。\n\nCED 基于现有 NLI 模型（DeBERTa-v3-large），EDCR 是两个 recall 的比值。这些分析工具有用，但作为独立贡献偏弱。整体定位更接近 **empirical study with analytical tools**。对 EMNLP main conference 而言，需要更强的方法创新性。\n\n**W2 [MAJOR] Scaling claim 的数据基础偏弱**\n\n\"Scale-dependent evidence tax\" 作为第一贡献，在 Qwen3 家族内仅有 4 个规模点（1.7B, 4B, 8B, 14B——其中 14B 仅为 validation），cross-family 仅 1 个点（LLaMA-3.1-8B）。4 个点不足以可靠区分线性、对数、阶梯等 scaling pattern。\n\n更重要的是，不同规模的数据呈现非单调性：1.7B RSFT（51.19 Ign-F1）超过 4B RSFT（44.82, Table 1），甚至超过 8B SFT（50.19）。论文在 Section 4.4 和 Appendix D 讨论了 truncation rate 差异和 matched@2048 协议，但主文中不同规模的数字是否全部来自同一 evaluation protocol 不够清晰——读者需要翻阅 Appendix 才能理解数字间的关系。建议在 Table 1 旁或 Section 4 开头明确列出所有规模在同一协议下的对比表。\n\n**W3 [MAJOR] GRPO 崩溃分析缺乏机制深度**\n\nSection 4.3 对 GRPO QLoRA catastrophic collapse 的分析停留在现象描述层面（\"extraction collapses to Rel-F1 1.41, Evi-F1 rises to 85.04\"），未提供机制解释。这本质上是 multi-objective reward hacking 的一个实例——optimizer 发现牺牲 extraction accuracy 可以最大化 evidence-weighted reward。论文未：\n1. 连接到 reward hacking 文献（如 Weng 2024 综述; Fu et al. 2025 的 reward shaping 原则）\n2. 探讨简单缓解策略（reward clipping, 不同 KL 系数如 0.1/0.5, reward normalization）是否能避免 collapse\n3. 分析 full-precision GRPO 也部分避免 collapse 是否仅因为梯度精度差异\n\n如果 GRPO collapse 仅在 β=0.01 的 QLoRA 设置下发生，这更像是超参数/精度问题而非方法本质差异，\"decoupling spectrum\" 的框架就不够稳固。\n\n**W4 [MINOR] Related Work 存在遗漏**\n\n以下近期相关工作未被引用或讨论：\n1. **LMRC**（Li & Zhang, 2024; arXiv 2408.13889）——LLM with Relation Classifier for DocRE，针对 LLM 注意力分散问题，在 LLM-based DocRE 中表现突出，应在 Section 2 LLM-based DocRE 部分讨论。\n2. **RelPrior**（Huang et al., 2025; arXiv 2511.08143）——\"Relation as a Prior\" 范式，claim 超越现有 LLM-based DocRE 方法。\n3. **SummaC**（Laban et al., 2022, TACL）——NLI-based faithfulness evaluation 的先驱工作，CED 的设计理念（sentence-level NLI scoring 用于 faithfulness 判断）与之直接相关，应在 Section 3.4 讨论设计动机时引用。\n4. **Rationale Verification for RE**（Li et al., 2024; AAAI 2025, arXiv 2412.07289）——使用 rationale supervisor 验证 LLM 的 RE 推理，与本文的 evidence verification 主题高度相关。\n\n**W5 [MINOR] CED 对外部 NLI 模型的 sensitivity analysis 不足**\n\nCED 评分完全取决于 NLI 模型能力。论文仅在 Appendix B 比较了 DeBERTa-v3-large vs. v3-base（差异\"可忽略\"），但：\n- 未测试其他 NLI 模型家族（如生成式 NLI 模型）\n- 未分析 NLI 模型在 DocRE 领域的 out-of-distribution 行为——DocRE 中的证据句往往包含多个实体和复杂共指，与标准 NLI 训练分布差异较大\n- 若 NLI 模型对某些 relation type 存在系统性偏差，EDCR 诊断可能产生误导性结论\n\n**W6 [MINOR] Limitations section 遗漏了若干重要限制**\n\nLimitations（Section 7）覆盖面尚可但遗漏：\n- DocRED 的证据标注已知不完整（Re-DocRED 论文已指出），这对 CED/EDCR 基于 gold evidence 的计算可靠性有直接影响\n- 三种方法的计算成本差异未提及——GRPO 需要 G 个 candidate generation + value estimation，DPO 需要 preference pair 构建，RSFT 需要 N=5 采样 + CED scoring，公平对比应包含 cost analysis\n- 仅评估 DocRE 一种 IE 任务，findings 是否 generalize 到 NER、事件抽取等未讨论\n\n---\n\n### Questions（需要作者澄清的）\n\n**Q1.** Abstract 中 1.7B RSFT 的 51.19 Ign-F1 与 Table 1 中 4B RSFT CED 的 44.82 使用的是同一 evaluation protocol 吗？如果不同（如 matched@2048 vs. standard dev-set），请在主文中明确标注每个数字的 evaluation protocol，避免读者跨表对比时产生困惑。\n\n**Q2.** GRPO collapse 是否在其他 KL 系数（如 0.1, 0.5）或不使用 QLoRA（full-precision）时依然发生？Section 4.3 提到 full-precision GRPO \"avoids extreme decoupling\"（EDCR 0.6797），那么 QLoRA 的量化精度损失是否是 collapse 的主要原因而非 GRPO 方法本身？\n\n**Q3.** EDCR 与 Rel-F1 的负相关（ρ=−0.93, Section 5）是在仅 7 个 method configurations 上计算的。n=7 的 Spearman 相关有较大的 sampling variability——bootstrap 95% CI 是多少？是否在不同 seed 下稳定？\n\n**Q4.** CED contrastive premise 中收集的 \"entity-sharing negatives\"（Section 3.4）是否包含了实际成立但未被标注的关系（即 DocRED 的 false negatives）？Re-DocRED 标注密度是 DocRED 的 2.82×，这意味着 DocRED 上大量 \"negative\" 其实是 false negative，会如何影响 CED score 的可靠性？\n\n**Q5.** RSFT 的 N=5 candidates 是如何选择的？如果增加到 N=50 或 100（更接近 best-of-N scaling），解耦行为是否会改变？论文对 RSFT \"avoids decoupling\" 的机制解释（Section F, \"discrete selection\"）在 N→∞ 的极限下是否依然成立？\n\n**Q6.** Table 12 的 encoder-based comparison 显示 TP-only Evi-F1 超过 80%，但 joint Evi-F1 仅 54.15。论文 claim \"when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods\"——但 joint evaluation 的巨大 gap（54.15 vs. encoder 的更高值）说明 LLM 方法的主要瓶颈不在 evidence quality 而在 extraction precision。这是否削弱了论文对 \"evidence-grounded extraction\" 实用性的 claim？\n\n---\n\n### Missing References\n\n1. Li, X., & Zhang, M. (2024). LLM with Relation Classifier for Document-Level Relation Extraction. arXiv:2408.13889. — 重要的 LLM-based DocRE baseline\n2. Huang, N., et al. (2025). Relation as a Prior for LLM-based Document-level Relation Extraction. arXiv:2511.08143. — 最新 LLM-based DocRE 范式\n3. Laban, P., et al. (2022). SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization. TACL. — CED 设计理念的先驱\n4. Li, Y., et al. (2025). Enhancing Relation Extraction via Supervised Rationale Verification and Feedback. AAAI 2025. — RE 中的 rationale verification\n5. Reward hacking 相关文献（如 Weng 2024 综述）——GRPO collapse 分析的理论背景\n\n---\n\n### Overall Assessment\n\n## 总体评分\n**Overall**: 3.0（Findings — 可被 Findings 接收）\n**一句话总结**: 设计良好的 empirical study，实验覆盖面和分析深度出色，但三个核心贡献均为经验观察，缺乏足以进入 main conference 的方法创新性。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计扎实，controlled evaluation 和多 seed 验证体现严谨性；但 scaling claim 基于有限数据点，GRPO collapse 的机制分析不足，不同规模数字的 evaluation protocol 对应关系不够清晰 |\n| Excitement | 2.5/5 | Evidence tax 概念有趣，RSFT 方差压缩对实践有价值；但方法组件（CED/EDCR/RSFT 应用）各自偏简单，无显著方法创新，核心 insight（selection-based > gradient-based for multi-objective）在 RL 社区不算新颖 |\n| Reproducibility | 4/5 | 超参数详细列出（Appendix A），声明将 release code and outputs，多 seed 实验设计好；但 CED 依赖特定 NLI 模型版本，未提供 CED scoring 的独立复现指南 |\n| Overall | 3.0/5 | Findings 水平——经验发现有社区参考价值，但缺乏 main conference 所需的方法创新深度 |\n\n**置信度**: 4/5 — 对 DocRE 和 LLM post-training 方法较为熟悉\n\n**理由**: 本文是一项覆盖面广、分析深入的 empirical study。Evidence tax 的规模依赖性发现和 RSFT 方差压缩的实践价值是真实的贡献。但论文的定位困境在于：三个核心贡献均为经验观察（不是方法创新），分析工具（CED = NLI scoring, EDCR = recall ratio）定义简单，RSFT 本身不是新方法。\"Decoupling spectrum\" 框架虽然叙事有力，但深层机制（为什么 gradient methods 解耦、selection methods 不解耦）在 multi-objective optimization 文献中已有大量讨论（reward hacking, Goodhart's Law），本文未充分连接。\n\n建议以 Findings 接收，但需要以下修改：\n1. **弱化 scaling claim 表述**或增加更多规模点/模型家族——当前 4 个 Qwen3 点 + 1 个 LLaMA 点不足以 claim \"scale-dependent\" 作为一个 general 结论\n2. **深化 GRPO collapse 的机制分析**——连接 reward hacking 文献，测试不同 KL 系数/精度，区分\"方法问题\"和\"超参数问题\"\n3. **主文中统一 evaluation protocol 的展示**——当前不同规模的数字散布在主文、appendix、不同 evaluation 设置中，读者追溯困难\n4. **补充 missing references**（至少 LMRC 和 SummaC）",
    "reviewer_id": "2",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-23T01:01:29.516089+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3863
}
```

</details>

---

### Assistant

_source line 136 · 2026-05-23T01:01:38.617283+00:00_

审稿意见已提交给 Review Director。

核心判断：**Overall 3.0（Findings）**。

主要发现：
- **方法原创性不足**是最关键问题——CED/EDCR/RSFT 应用三个组件各自偏简单，三个贡献均为经验观察
- **Scaling claim 数据基础偏弱**——仅 4 个 Qwen3 规模点 + 1 个 cross-family 点
- **GRPO collapse 分析停留在现象层面**，未连接 reward hacking 文献，未区分"方法本质"与"超参数/精度问题"
- 实验设计和分析深度是论文的强项，RSFT 方差压缩（4.6–31×）和 1.7B 超过 8B SFT 的发现具有实践价值
- Related work 遗漏 LMRC、RelPrior、SummaC 等相关工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---

## Round 4

4 recorded events

### User

_source line 137 · 2026-05-23T01:02:24.372207+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

### Summary
本文将 evidence-grounded DocRE 形式化为结构化生成任务，系统比较了三种 post-SFT 优化范式（GRPO、DPO、RSFT）在 evidence 生成与 relation extraction 之间的 trade-off。核心发现包括：(1) evidence tax 是 scale-dependent 的（1.7B 有益、4B+ 中性）；(2) 梯度优化方法导致 extraction-evidence decoupling，离散选择方法（RSFT）可避免；(3) RSFT 通过 CED-based 样本选择压缩训练方差。论文覆盖面广（1.7B-14B，Qwen3/LLaMA 两个 model family），分析视角有启发性，但多处统计推断基础薄弱。

### Strengths
S1. 问题定位精准且实用——evidence grounding 是 LLM-based IE 部署的真实痛点。
S2. Decoupling spectrum 概念有分析价值——从优化机制角度解释不同范式表现差异。
S3. 跨尺度+跨 model family 的实验覆盖（1.7B-14B Qwen3 + LLaMA-3.1-8B + Re-DocRED）。
S4. 对自身局限的透明度——主动承认 EDCR 缺乏 human judgment 验证、variance 基于 3 seeds 等。
S5. 定性分析具体有用——三个 case study 展示了 EDCR 的诊断价值。

### Weaknesses
W1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础。置信区间极宽（σ 的 95% CI 约 [0.52s, 6.29s]），Cohen's d=2.58 的标准误约 1.2-1.5。声称"31× compression"在统计上无法从 n=3 可靠估计。建议增加到 5-10 seeds 或降级为 observation。

W2 [CRITICAL] — EDCR 的 shared-component 问题使 cross-method 相关性不可靠。EDCR = (TP_evi × G) / TP²，TP 同时出现在分子和分母，构造机械性负相关。n=7 极小，GRPO QLoRA 极端点可能主导相关性。建议移除极端点后重算、用 partial correlation 控制 TP。

W3 [MAJOR] — CED contrastive formulation 增量价值不足。CED vs flat-NLI 的 Rel-F1 差仅 0.02pp，在 noise level 以内。减法操作缺乏理论动机。论文自己承认 contrastive "not essential"。

W4 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol 影响 decoupling spectrum 可比性。Footnote 1 提到"earlier evaluation protocol"但未充分说明差异。

W5 [MAJOR] — SFT vs RSFT variance 测量来源不同（full training vs fixed-base fine-tuning），RSFT variance 天然更小，直接比较不公平。

W6 [MAJOR] — Dev→Test 20pp drop 解释不够充分，14B RSFT test 上低于 SFT 0.37pp。

W7 [MINOR] — 与 encoder baseline 的比较选择性呈现指标（强调 TP-only Evi-F1 >80%，淡化 Ign-F1 差距 16-18pp）。

W8 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比。

W9 [MINOR] — 4B retrained checkpoint 的 dev 差距 0.35pp 可能影响 evidence tax 分析。

### Overall: 3.5（Borderline Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-23T01:04:28.959509+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R1-S1**: 问题定位精准。Evidence grounding 确实是 LLM-based IE 部署的真实痛点，论文 Introduction 中 \"accurate extractors have no evidence, evidence-capable methods are not competitive\" 的 gap 叙事准确。我在自己的审稿中也认可这一点（我的 S1）。\n\n**[AGREE] R1-S2**: Decoupling spectrum 作为分析框架有价值。补充一点：我认为这个框架虽然叙事有力，但机制解释不够深入——gradient-based 方法 exploit multi-objective reward landscape 导致解耦，这在 RL/reward hacking 文献中已有大量讨论，论文未充分连接（我的 W3/CRITICAL 中已指出）。\n\n**[AGREE] R1-S3**: 跨尺度+跨 model family 覆盖在同类工作中确实属上乘。但我对 scaling claim 的数据基础有保留——4 个 Qwen3 点 + 1 个 LLaMA 点是否足以 claim \"scale-dependent\" 作为 general 结论（我的 W2/MAJOR）。\n\n**[AGREE] R1-S4**: 透明度确实值得肯定。Section 7 (Limitations) 主动承认了 EDCR 缺 human validation、variance 基于少量 seeds、CED 依赖外部 NLI 模型等，这在论文写作中是好的实践。\n\n**[AGREE] R1-S5**: Section M 的三个 case study（date_of_birth EDCR 0.119, head_of_government 0.956, notable_work 0.613）确实展示了 EDCR 作为 per-relation diagnostic 的实际价值，是论文分析中的亮点。\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1 (n=3 seeds 统计基础)**: 这是我自己审稿中未充分强调的重要问题。n=3 的方差估计确实统计基础薄弱：\n- χ² 分布下，σ 的 95% CI 约 [0.52s, 6.29s]（R1 的估计正确）\n- \"31× compression\" 这个具体倍数在 n=3 下不可靠——真实压缩率可能在 5×-100× 之间\n- Cohen's d=2.58 的标准误约 1.2-1.5（R1 正确），CI 极宽\n\n论文在 Abstract 中高度强调此结果（\"compresses training variance 4.6-31×\"），但统计基础不匹配这一强调程度。建议：要么增加 seeds 到 5-10 个，要么将 claim 降级为定性观察（\"RSFT substantially reduces variance\"），不给出具体倍数。\n\n**[AGREE] R1-W2 (EDCR shared-component 问题)**: R1 的数学分析精确。EDCR = (TP_evi × G) / TP²，TP 同时出现在分子和分母，确实构造了与 Rel-F1（也是 TP 的函数）的机械性负相关。\n\n进一步补充：\n- n=7 configurations 中，GRPO QLoRA（Rel-F1 ≈ 1.41, EDCR 0.9876）是一个极端 outlier。移除此点后，remaining 6 个 configurations 的 ρ 可能大幅变化\n- 论文 claim \"EDCR validates EDCR's diagnostic utility\"（Section 5），但如果相关性主要由 mechanical construction + outlier 驱动，这个 validation 就不成立\n\nR1 建议的 partial correlation（控制 TP）和 remove-outlier sensitivity analysis 是恰当的修复方案。\n\n**[AGREE] R1-W3 (CED contrastive 增量价值)**: Appendix B 的数据确实显示 CED vs flat-NLI 的 Rel-F1 差仅 0.02pp，论文自己也承认 contrastive formulation \"not essential for data selection quality\"。我在自己的审稿中也指出 CED 作为独立贡献偏弱（我的 W1/CRITICAL）。\n\n补充：论文的辩护角度是 CED 在 \"per-triple discrimination scores\" 上更优——但如果这个优势不能传导到下游 RSFT 性能，其实际价值存疑。\n\n**[AGREE] R1-W4 (DPO 3-epoch evaluation protocol 差异)**: Footnote 1 提到 DPO 3-epoch 使用 \"earlier evaluation protocol\" 但未详细说明差异，这确实影响 decoupling spectrum 的可比性。如果 DPO 5-epoch 和 DPO 3-epoch 在不同 protocol 下评估，Table 2 的 severity 排序可能不完全可靠。建议作者在 revision 中统一所有 configurations 的 evaluation protocol 或明确标注差异。\n\n**[AGREE] R1-W5 (SFT vs RSFT variance 来源不同)**: 这是一个精细但重要的统计观点：\n- SFT variance = 随机初始化 + 训练随机性 + 数据顺序\n- RSFT variance = 固定 SFT base 上的 RSFT 训练随机性\n\n这两者测量不同层面的变异性。RSFT 起点固定，天然 variance 更小。\"31× compression\" 可能更多反映了固定起点的效果，而非 RSFT 方法本身的优势。\n\n不过，从实践部署角度看：如果用户的 workflow 是 \"train SFT → apply RSFT\"，那么 RSFT 步骤引入的额外方差确实很小。论文的实践 claim（RSFT 使部署更可预测）仍然成立，但应更精确地描述方差来源。\n\n**[REBUT] R1-W6 (Dev→Test 20pp drop)**: 这个 weakness 的严重性我认为 R1 略有高估。\n\n论文在 Section 4.4（page 7）和 Section 7（Limitations）中已经给出了合理解释：Re-DocRED 标注密度是 DocRED 的 2.82×（更多 gold triples per document），exact-match evaluation 对 generative model 的 surface-form 差异更为敏感。更重要的是，**method ranking 在 test set 上完全保持**（Spearman ρ=1.0, Section 7），说明 absolute performance drop 不影响 relative comparison 的有效性。\n\n但 R1 指出的 \"14B RSFT test 上低于 SFT 0.37pp\" 值得关注。从 Table 9（page 14）可以看到，这个反转虽然幅度小（0.37pp），但如果 RSFT 的 advantage 在更大规模上消失，这对论文的 scaling narrative 是一个隐患。建议作者在 revision 中分析 14B 反转是否在统计意义上显著。\n\n**[AGREE] R1-W7 (Encoder baseline 选择性呈现)**: Table 12（page 15）确实选择性地强调了 LLM 方法的优势指标（TP-only Evi-F1 > 80%）而淡化了 Ign-F1 gap（16-18pp）。论文的辩护（\"closing this gap requires improving extraction precision\"）是合理的方向性说明，但不改变当前 LLM 方法在 absolute performance 上的劣势。建议在 Discussion 中更 balanced 地呈现。\n\n**[AGREE] R1-W8 (缺少 LLM-based RE 直接对比)**: 与我的 W4 一致。论文未引用或对比 LMRC（Li & Zhang, 2024）、RelPrior（Huang et al., 2025）等近期 LLM-based DocRE 方法。虽然这些方法不一定做 evidence extraction，但 extraction performance 的对比对 situating 论文贡献至关重要。\n\n**[AGREE] R1-W9 (4B retrained checkpoint 差距)**: Minor issue，0.35pp 差距在 SFT 3.80pp std 的噪声范围内，不太可能实质影响 evidence tax 分析。同意这是 minor。\n\n---\n\n### 综合评价\n\nR1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于我对 **方法论原创性** 的评价更低（我的 W1/CRITICAL）：论文的三个贡献均为经验观察，方法组件（CED、EDCR、RSFT 应用）各自偏简单。R1 的审稿更侧重实验设计和统计严谨性，在这些方面发现了我未充分强调的重要问题（特别是 W1 的 n=3 统计基础和 W5 的方差来源差异）。\n\n综合两份审稿，我认为：\n- **论文质量下限**：实验覆盖面和分析深度确实在同类工作中属上乘（双方一致认可）\n- **论文质量上限受限于**：(1) 方法原创性不足（我的 W1）；(2) 关键统计声明基础薄弱（R1 的 W1/W2）；(3) GRPO collapse 机制分析不足（我的 W3）\n- **建议定位**：3.0-3.5 之间，Findings 接收是合理的；进入 main conference 需要显著加强方法创新或统计严谨性\n\nR1 的 W1（n=3 seeds）和 W2（EDCR shared-component）是我认为最需要作者在 revision 中 address 的问题，因为这些直接影响论文核心 claim 的可信度。",
  "reviewer_id": "2",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R1-S1**: 问题定位精准。Evidence grounding 确实是 LLM-based IE 部署的真实痛点，论文 Introduction 中 \"accurate extractors have no evidence, evidence-capable methods are not competitive\" 的 gap 叙事准确。我在自己的审稿中也认可这一点（我的 S1）。\n\n**[AGREE] R1-S2**: Decoupling spectrum 作为分析框架有价值。补充一点：我认为这个框架虽然叙事有力，但机制解释不够深入——gradient-based 方法 exploit multi-objective reward landscape 导致解耦，这在 RL/reward hacking 文献中已有大量讨论，论文未充分连接（我的 W3/CRITICAL 中已指出）。\n\n**[AGREE] R1-S3**: 跨尺度+跨 model family 覆盖在同类工作中确实属上乘。但我对 scaling claim 的数据基础有保留——4 个 Qwen3 点 + 1 个 LLaMA 点是否足以 claim \"scale-dependent\" 作为 general 结论（我的 W2/MAJOR）。\n\n**[AGREE] R1-S4**: 透明度确实值得肯定。Section 7 (Limitations) 主动承认了 EDCR 缺 human validation、variance 基于少量 seeds、CED 依赖外部 NLI 模型等，这在论文写作中是好的实践。\n\n**[AGREE] R1-S5**: Section M 的三个 case study（date_of_birth EDCR 0.119, head_of_government 0.956, notable_work 0.613）确实展示了 EDCR 作为 per-relation diagnostic 的实际价值，是论文分析中的亮点。\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1 (n=3 seeds 统计基础)**: 这是我自己审稿中未充分强调的重要问题。n=3 的方差估计确实统计基础薄弱：\n- χ² 分布下，σ 的 95% CI 约 [0.52s, 6.29s]（R1 的估计正确）\n- \"31× compression\" 这个具体倍数在 n=3 下不可靠——真实压缩率可能在 5×-100× 之间\n- Cohen's d=2.58 的标准误约 1.2-1.5（R1 正确），CI 极宽\n\n论文在 Abstract 中高度强调此结果（\"compresses training variance 4.6-31×\"），但统计基础不匹配这一强调程度。建议：要么增加 seeds 到 5-10 个，要么将 claim 降级为定性观察（\"RSFT substantially reduces variance\"），不给出具体倍数。\n\n**[AGREE] R1-W2 (EDCR shared-component 问题)**: R1 的数学分析精确。EDCR = (TP_evi × G) / TP²，TP 同时出现在分子和分母，确实构造了与 Rel-F1（也是 TP 的函数）的机械性负相关。\n\n进一步补充：\n- n=7 configurations 中，GRPO QLoRA（Rel-F1 ≈ 1.41, EDCR 0.9876）是一个极端 outlier。移除此点后，remaining 6 个 configurations 的 ρ 可能大幅变化\n- 论文 claim \"EDCR validates EDCR's diagnostic utility\"（Section 5），但如果相关性主要由 mechanical construction + outlier 驱动，这个 validation 就不成立\n\nR1 建议的 partial correlation（控制 TP）和 remove-outlier sensitivity analysis 是恰当的修复方案。\n\n**[AGREE] R1-W3 (CED contrastive 增量价值)**: Appendix B 的数据确实显示 CED vs flat-NLI 的 Rel-F1 差仅 0.02pp，论文自己也承认 contrastive formulation \"not essential for data selection quality\"。我在自己的审稿中也指出 CED 作为独立贡献偏弱（我的 W1/CRITICAL）。\n\n补充：论文的辩护角度是 CED 在 \"per-triple discrimination scores\" 上更优——但如果这个优势不能传导到下游 RSFT 性能，其实际价值存疑。\n\n**[AGREE] R1-W4 (DPO 3-epoch evaluation protocol 差异)**: Footnote 1 提到 DPO 3-epoch 使用 \"earlier evaluation protocol\" 但未详细说明差异，这确实影响 decoupling spectrum 的可比性。如果 DPO 5-epoch 和 DPO 3-epoch 在不同 protocol 下评估，Table 2 的 severity 排序可能不完全可靠。建议作者在 revision 中统一所有 configurations 的 evaluation protocol 或明确标注差异。\n\n**[AGREE] R1-W5 (SFT vs RSFT variance 来源不同)**: 这是一个精细但重要的统计观点：\n- SFT variance = 随机初始化 + 训练随机性 + 数据顺序\n- RSFT variance = 固定 SFT base 上的 RSFT 训练随机性\n\n这两者测量不同层面的变异性。RSFT 起点固定，天然 variance 更小。\"31× compression\" 可能更多反映了固定起点的效果，而非 RSFT 方法本身的优势。\n\n不过，从实践部署角度看：如果用户的 workflow 是 \"train SFT → apply RSFT\"，那么 RSFT 步骤引入的额外方差确实很小。论文的实践 claim（RSFT 使部署更可预测）仍然成立，但应更精确地描述方差来源。\n\n**[REBUT] R1-W6 (Dev→Test 20pp drop)**: 这个 weakness 的严重性我认为 R1 略有高估。\n\n论文在 Section 4.4（page 7）和 Section 7（Limitations）中已经给出了合理解释：Re-DocRED 标注密度是 DocRED 的 2.82×（更多 gold triples per document），exact-match evaluation 对 generative model 的 surface-form 差异更为敏感。更重要的是，**method ranking 在 test set 上完全保持**（Spearman ρ=1.0, Section 7），说明 absolute performance drop 不影响 relative comparison 的有效性。\n\n但 R1 指出的 \"14B RSFT test 上低于 SFT 0.37pp\" 值得关注。从 Table 9（page 14）可以看到，这个反转虽然幅度小（0.37pp），但如果 RSFT 的 advantage 在更大规模上消失，这对论文的 scaling narrative 是一个隐患。建议作者在 revision 中分析 14B 反转是否在统计意义上显著。\n\n**[AGREE] R1-W7 (Encoder baseline 选择性呈现)**: Table 12（page 15）确实选择性地强调了 LLM 方法的优势指标（TP-only Evi-F1 > 80%）而淡化了 Ign-F1 gap（16-18pp）。论文的辩护（\"closing this gap requires improving extraction precision\"）是合理的方向性说明，但不改变当前 LLM 方法在 absolute performance 上的劣势。建议在 Discussion 中更 balanced 地呈现。\n\n**[AGREE] R1-W8 (缺少 LLM-based RE 直接对比)**: 与我的 W4 一致。论文未引用或对比 LMRC（Li & Zhang, 2024）、RelPrior（Huang et al., 2025）等近期 LLM-based DocRE 方法。虽然这些方法不一定做 evidence extraction，但 extraction performance 的对比对 situating 论文贡献至关重要。\n\n**[AGREE] R1-W9 (4B retrained checkpoint 差距)**: Minor issue，0.35pp 差距在 SFT 3.80pp std 的噪声范围内，不太可能实质影响 evidence tax 分析。同意这是 minor。\n\n---\n\n### 综合评价\n\nR1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于我对 **方法论原创性** 的评价更低（我的 W1/CRITICAL）：论文的三个贡献均为经验观察，方法组件（CED、EDCR、RSFT 应用）各自偏简单。R1 的审稿更侧重实验设计和统计严谨性，在这些方面发现了我未充分强调的重要问题（特别是 W1 的 n=3 统计基础和 W5 的方差来源差异）。\n\n综合两份审稿，我认为：\n- **论文质量下限**：实验覆盖面和分析深度确实在同类工作中属上乘（双方一致认可）\n- **论文质量上限受限于**：(1) 方法原创性不足（我的 W1）；(2) 关键统计声明基础薄弱（R1 的 W1/W2）；(3) GRPO collapse 机制分析不足（我的 W3）\n- **建议定位**：3.0-3.5 之间，Findings 接收是合理的；进入 main conference 需要显著加强方法创新或统计严谨性\n\nR1 的 W1（n=3 seeds）和 W2（EDCR shared-component）是我认为最需要作者在 revision 中 address 的问题，因为这些直接影响论文核心 claim 的可信度。",
    "reviewer_id": "2",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-23T01:04:32.725278+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3765
}
```

</details>

---

### Assistant

_source line 140 · 2026-05-23T01:04:43.823612+00:00_

交叉回应已提交。

对 R1 的 9 个 Weaknesses 中，我 AGREE 了 8 条，REBUT 了 1 条（W6 Dev→Test drop 严重性被高估——method ranking 完全保持，Spearman ρ=1.0）。R1 提出的 n=3 统计基础（W1）和 EDCR shared-component 问题（W2）是我自己审稿中未充分强调的重要问题，已在交叉回应中补充认可。综合两份审稿，建议 3.0-3.5 区间，Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---

## Round 5

100 recorded events

### User

_source line 141 · 2026-05-24T22:53:44.155538+00:00_

[Round 3 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 相关工作 + 写作质量**。

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
1. **贡献定位与新颖性**：三个 contributions 均为 empirical observations（evidence tax scale-dependent, gradient decoupling spectrum, RSFT variance compression）——这对 EMNLP 长文是否足够？empirical study 定位是否清晰？是否存在 method-innovation 过度暗示？CED 作为 scoring function 的定位——是工具还是贡献？
2. **相关工作覆盖**：检查以下领域覆盖是否完整——(a) LLM-based DocRE（AutoRE, LMRC, GLiDRE, RelPrior, Ru-LLM, DocKS-RAG）是否有遗漏？(b) Evidence faithfulness（SummaC, DRIFT, SRVF, EvidenceRL）是否充分？(c) RSFT/rejection sampling（STaR, RFT, RAFT, RSFT≈PPO, RIFT, TrajFusion）是否完整？(d) RL for structured generation 的最新工作（R1-RE, REAR, DAPO, Dr.GRPO, μ-GRPO, Tree-GRPO, MO-GRPO, GDPO）是否覆盖？(e) 是否有重要相关工作被遗漏——用 web search 验证
3. **写作质量与可读性**：abstract 是否 ≤200 words？叙事线是否清晰（gap → formalization → comparison → findings）？Table/Figure 密度和信息价值是否合适？Appendix 是否组织良好？
4. **格式合规检查**：(a) 正文是否 ≤8 页？(b) Limitations 是否存在且 ≤1 页？(c) 匿名是否完整（无作者信息泄露）？(d) 参考文献格式是否一致（natbib/acl_natbib.bst）？(e) 是否有 ethical considerations？
5. **完整性审查**：实验覆盖是否充分？五个模型规模（1.7B/4B/8B/14B + LLaMA-8B）是否形成完整 scaling picture？两个数据集（DocRED + Re-DocRED）是否足以支持 generalization 声明？test set evaluation 是否充分？
6. **Claim-evidence 对齐**：每个主要声明是否都有充分的实验支持？abstract 中的数字是否与正文/表格一致？

请完整阅读论文（main.tex 所有 sections + appendix），给出结构化审稿意见（Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment + 置信度 + 分数）。对每个 Weakness 标注严重程度（CRITICAL / MAJOR / MINOR）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-24T22:53:55.132920+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-24T22:53:55.233749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-24T22:53:58.449595+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-24T22:53:58.955358+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-24T22:53:59.006606+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-24T22:54:06.067829+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Here are the key findings from the ACL Rolling Review (ARR) 2025-2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Area Chair Meta-Review Scoring
The ARR metareview score has changed in February 2025 to be more aligned with reviewer scores. Like with reviews, the score should be backed up by the meta-review text. The new options are: 5 = Consider for Award (up to top 2.
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7618
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-24T22:54:10.603294+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, score scales (1-5 for each dimension), and any specific instructions for reviewers about how to score papers. Include all scoring rubrics and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, score scales (1-5 for each dimension), and any specific instructions for reviewers about how to score papers. Include all scoring rubrics and what each score means."
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-24T22:54:11.210064+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-24T22:54:11.564574+00:00_

1	\begin{abstract}
2	Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, creating a gap between extraction performance and output verifiability. We formalize evidence-grounded DocRE as structured generation and compare Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax---extraction cost of generating evidence---is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with Natural Language Inference (NLI)-based scoring avoids decoupling entirely through output filtering rather than gradient pressure. RSFT consistently reduces training seed variance (complete pairwise seed separation on LLaMA, Cohen's $d{=}2.58$; non-overlapping $\chi^2$ confidence intervals at 1.7B). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all evaluated scales (Spearman $\rho{=}1.0$).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-24T22:54:11.565125+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-24T22:54:11.967570+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-24T22:54:11.967950+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-24T22:54:12.068557+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-24T22:54:16.510014+00:00_

# ARR Review Form Scoring Dimensions

Based on the ARR Reviewer Guidelines, the review form includes **three scoring dimensions**:

## Scoring Dimensions

1. **Soundness** - Assesses technical validity and methodological rigor. The guidelines emphasize that "soundness scores must be justified by the text of the review" (section I3). Low soundness scores without clear justification indicate the review lacks fidelity to the recommendation.

2. **Excitement** - Reflects the reviewer's personal interest and enthusiasm. This dimension is explicitly "orthogonal to the assessment of the soundness of the paper," allowing reviewers to distinguish between objectively sound work and subjectively engaging research.

3. **Overall Recommendation** - A composite assessment combining soundness, excitement, novelty, and potential impact. The guidelines note this reflects "your assessment of soundness, excitement, and also other factors like novelty and impact."

## Key Scoring Instruction

The guidelines do not specify explicit numeric scales (1-5) in the provided content. However, they establish that reviewers must ensure scores align with review justifications. As stated: "low soundness scores without sufficient justification" signal problematic reviewing, suggesting reviewers should provide evidence-based scoring.

The framework emphasizes that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," establishing quality thresholds rather than fixed numerical rubrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5906
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-24T22:54:19.611404+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-24T22:54:19.956720+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 345
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-24T22:54:19.957338+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-24T22:54:20.242113+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 284
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-24T22:54:20.242653+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-24T22:54:20.299729+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-24T22:54:25.226610+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-24T22:54:25.378442+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-24T22:54:25.378899+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-24T22:54:25.732027+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-24T22:54:30.910466+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-24T22:54:31.058608+00:00_

1	@inproceedings{autore2024,
2	  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},
3	  author    = {Xue, Lilong and Zhang, Dan and Dong, Yuxiao and Tang, Jie},
4	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2403.14888}
7	}
8	
9	@inproceedings{chen2025docksrag,
10	  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},
11	  author    = {Xu, Xiaolong and Zhou, Yibo and Xiang, Haolong and Li, Xiaoyong and Zhang, Xuyun and Qi, Lianyong and Dou, Wanchun},
12	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
13	  year      = {2025},
14	  url       = {https://proceedings.mlr.press/v267/xu25am.html}
15	}
16	
17	@article{dai2025r1re,
18	  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},
19	  author  = {Dai, Runpeng and Zheng, Tong and Yang, Run and Yu, Kaixian and Zhu, Hongtu},
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
41	@article{li2026qurl,
42	 
…[truncated 19203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 148
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-24T22:54:38.610935+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 169 · 2026-05-24T22:54:39.265523+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM document-level relation extraction evidence grounding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM document-level relation extraction evidence grounding 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-24T22:54:39.870477+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 620.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.9}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1259
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-24T22:54:52.873441+00:00_

Web search results for query: "LLM document-level relation extraction evidence grounding 2025 2026"

Links: [{"title":"PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A | Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/full/10.1145/3772318.3791101"},{"title":"What Is LLM Grounding? Definition, Examples & FutureAGI Guide (2026)","url":"https://futureagi.com/glossary/llm-grounding/"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/pdf/2408.13889"},{"title":"PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A","url":"https://arxiv.org/html/2602.21045v1"},{"title":"Semi-automatic Data Enhancement for Document-Level Relation Extraction   with Distant Supervision from Large Language Models","url":"https://arxiv.org/pdf/2311.07314"}]

Based on the search results, here are recent developments in LLM document-level relation extraction with evidence grounding:

## Key Research Areas

**Document-Level Relation Extraction (DocRE) with LLMs:**
Large language models have emerged as a promising avenue for advancing document-level relation extraction due to their robust semantic comprehension and extensive pre-training across various fields. LLMs enable accomplishing tasks in a more interpretable manner through their textual output and in-context learning abilities.

However, the performance of LLM-based methods still falls short of traditional approaches, with a key issue being the construction of an exhaustive set of potential entity pairs (candidate space), where only a small subset expresses relations, leading to a significant imbalance.

**Evidence Grounding and Provenance:**
Recent work addresses grounding by linking claims to evidence sources. A three-stage pipeline consists of: offline paper-level extraction of claims and evidence for a source document corpus, real-time answer-leve
…[truncated 629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 13607
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-24T22:54:55.985410+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-24T22:54:56.940265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-24T22:54:56.940692+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-24T22:54:57.493370+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-24T22:54:58.047791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-24T22:54:58.050456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 557
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-24T22:54:58.101060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "rejection sampling fine-tuning structured information extraction GRPO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "rejection sampling fine-tuning structured information extraction GRPO 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-24T22:55:06.931640+00:00_

Web search results for query: "rejection sampling fine-tuning structured information extraction GRPO 2025 2026"

Links: [{"title":"Rejection Sampling Fine-Tuning","url":"https://www.emergentmind.com/topics/rejection-sampling-fine-tuning"},{"title":"Fine-tuning a reasoning model with GRPO for passport data extraction","url":"https://rabiloo.com/blog/fine-tuning-a-reasoning-model-with-grpo-for-passport-data-extraction"},{"title":"Rejection Sampling Fine-Tuning (RFT)","url":"https://www.emergentmind.com/topics/rejection-sampling-fine-tuning-rft"},{"title":"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning","url":"https://arxiv.org/pdf/2602.04391"},{"title":"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce","url":"https://arxiv.org/pdf/2504.11343"},{"title":"Low-Resource Fine-Tuning for Multi-Task Structured Information Extraction with a Billion-Parameter Instruction-Tuned Model","url":"https://arxiv.org/pdf/2509.08381"},{"title":"Rejection Sampling Based Fine Tuning Secretly Performs PPO | OpenReview","url":"https://openreview.net/forum?id=yQ2UivKlir"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"}]

I found relevant search results on these topics. Here's what the research shows:

## Rejection Sampling Fine-Tuning (RFT)

Rejection Sampling Fine-Tuning (RFT) refers to methodologies that systematically enhance the efficacy, efficiency, and applicability of rejection sampling in statistical inference, generative modeling, and large-scale machine learning, introducing data augmentations, adaptive mechanisms, statistical optimization, and algorithmic improvements to realize more robust and resource-efficient sampling and learning.

In rejection sampling, a teacher model generates multiple candidate trajectories for a given problem, retaining only those wi
…[truncated 1271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8830
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-24T22:55:26.420470+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

### Tool call

_source line 181 · 2026-05-24T22:55:27.174885+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement overall assessment score scale 1 to 5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement overall assessment score scale 1 to 5"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-24T22:55:27.829286+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.0}, {\"
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1408
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-24T22:55:34.523978+00:00_

Web search results for query: "ACL ARR review form soundness excitement overall assessment score scale 1 to 5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"}]

Based on the search results, here's what I found about the ACL ARR review form scoring scales:

## Three Core Review Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score (1-5 Scale)

The soundness scale includes: 5 = Excellent: This study is one of the most thorough I have seen, given its type; 4 = Strong: This study provides sufficient support for all of its claims. The soundness scores must be justified by the text of the review.

## Excitement Score (1-5 Scale)

For excitement: 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference; 4 = Exciting: I would mention t
…[truncated 587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7349
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-24T22:55:40.302285+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, ALL score levels with their descriptions, and ALL required fields. Include the exact score options for soundness, excitement, and overall assessment with their full rubric descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, ALL score levels with their descriptions, and ALL required fields. Include the exact score options for soundness, excitement, and overall assessment with their full rubric descriptions."
  }
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-24T22:55:40.705054+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-24T22:55:40.856073+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_2_2b5124f3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-24T22:55:46.833526+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Review Sections

**Paper Summary**: Authors describe the work's topic to prevent misunderstandings.

**Summary of Strengths**: Identifies reasons for publication, including "novel and useful methodology, insightful empirical results" and clear organization.

**Summary of Weaknesses**: Lists concerns prioritizing other papers, with numbered items for author responses.

**Comments/Suggestions/Typos**: Additional improvement feedback.

## Scoring Dimensions

### Reviewer Confidence
- 5 = Positive evaluation; careful reading and familiarity with related work
- 4 = Quite sure; important points checked carefully
- 3 = Pretty sure; general area knowledge but incomplete detail verification
- 2 = Willing to defend; likely missed details or unsure about novelty
- 1 = Outside expertise or very difficult to understand

### Soundness
- 5 = Excellent; among the most thorough studies reviewed
- 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1 (incremental scale)
- 1 = Major issues; insufficiently thorough or irrelevant to ACL

### Excitement
- 5 = Highly exciting; would recommend to others
- 4 = Exciting; would mention to others
- 3 = Interesting; might mention points
- 2 = Potentially interesting; limited personal resonance
- 1 = Not exciting; limited community relevance

### Overall Assessment
- 5 = Consider for Award (top 2.5%)
- 4.5 = Borderline Award
- 4 = Conference acceptance
- 3.5 = Borderline Conference
- 3 = Findings acceptance
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## Additional Required Fields

- Best paper justification (for award considerations)
- Limitations and societal impact assessment
- Ethical concerns review
- Needs ethics review determination
- Reproducibility rating (1-5 scale)
- Datasets value assessment (1-5 scale)
- Software value assessment (1-5 scale)
- Author identity knowledge (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6531
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-24T22:55:49.395342+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-24T22:55:49.496061+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_2_2b5124f3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-24T22:55:49.847485+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-24T22:55:50.805553+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_2_2b5124f3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-24T22:55:50.806007+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-24T22:55:51.006806+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_2_2b5124f3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-24T22:55:51.007307+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-24T22:55:51.057800+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_2_2b5124f3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-24T22:55:55.640421+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-24T22:55:55.892612+00:00_

submitted_p10.png
submitted_p11.png
submitted_p12.png
submitted_p13.png
submitted_p14.png
submitted_p15.png
submitted_p16.png
submitted_p17.png
submitted_p18.png
submitted_p19.png
submitted_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-24T22:56:04.932292+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
  "pages": "1-8",
  "project": "faith-evidence-ie",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf",
    "pages": "1-8",
    "project": "faith-evidence-ie",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-24T22:56:06.519723+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 620.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.9}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1587
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-24T22:56:10.076171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-24T22:56:10.783467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-24T22:56:11.940903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-24T22:56:11.994171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1917
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-24T22:56:11.994685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-24T22:56:13.053730+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images_main/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-24T22:56:14.062483+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3279
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-24T22:56:14.669783+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2728
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-24T22:56:14.926292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2931
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-24T22:56:15.027963+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1974
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-24T22:56:22.105437+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-24T22:56:23.111548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-24T22:56:23.313420+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-24T22:56:23.517416+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-24T22:56:23.871609+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-24T22:56:24.125090+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-24T22:56:25.398585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1881
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-24T22:56:25.973329+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2101
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-24T22:56:31.437384+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-24T22:56:32.530131+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-24T22:56:32.891074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1453
}
```

</details>

---

### Tool call

_source line 221 · 2026-05-24T22:56:32.943437+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-24T22:56:33.458460+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-24T22:56:34.461312+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1931
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-24T22:56:36.361558+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3418
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-24T22:56:36.710995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3252
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-24T22:56:43.012446+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-24T22:56:43.465174+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-24T22:56:43.968111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-24T22:56:44.069000+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-24T22:56:44.421354+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-24T22:56:44.624356+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-24T22:59:18.906747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper && cat sections/abstract.tex | sed 's/\\\\begin{abstract}//;s/\\\\end{abstract}//;s/\\\\[a-zA-Z]*{[^}]*}//g;s/\\\\[a-zA-Z]*//g;s/[{}$~]//g;s/---/ /g;s/--/ /g;s/  */ /g' | tr -s '[:space:]' '\\n' | grep -v '^$' | wc -l",
  "description": "Count abstract words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper && cat sections/abstract.tex | sed 's/\\\\begin{abstract}//;s/\\\\end{abstract}//;s/\\\\[a-zA-Z]*{[^}]*}//g;s/\\\\[a-zA-Z]*//g;s/[{}$~]//g;s/---/ /g;s/--/ /g;s/  */ /g' | tr -s '[:space:]' '\\n' | grep -v '^$' | wc -l",
    "description": "Count abstract words"
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-24T22:59:19.007574+00:00_

197
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_2_2b5124f3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-24T22:59:28.789431+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper && python3 -c \"\nimport re\nwith open('sections/abstract.tex') as f:\n    text = f.read()\n# Remove LaTeX begin/end\ntext = re.sub(r'\\\\\\\\begin\\{abstract\\}', '', text)\ntext = re.sub(r'\\\\\\\\end\\{abstract\\}', '', text)\n# Remove LaTeX commands but keep their arguments\ntext = re.sub(r'\\\\\\\\texttt\\{([^}]*)\\}', r'\\1', text)\ntext = re.sub(r'\\\\\\\\emph\\{([^}]*)\\}', r'\\1', text)\ntext = re.sub(r'\\\\\\\\citet\\{[^}]*\\}', '', text)\ntext = re.sub(r'\\\\\\\\citep\\{[^}]*\\}', '', text)\n# Remove math mode content but keep readable parts\ntext = re.sub(r'\\\\$[^$]*\\\\$', ' NUM ', text)\n# Remove remaining LaTeX commands\ntext = re.sub(r'\\\\\\\\[a-zA-Z]+', '', text)\ntext = re.sub(r'[{}]', '', text)\n# Clean up\ntext = re.sub(r'\\\\s+', ' ', text).strip()\nwords = text.split()\nprint(f'Word count: {len(words)}')\nprint(f'Text: {text[:500]}...')\n\"\n",
  "description": "Count abstract words more accurately"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper && python3 -c \"\nimport re\nwith open('sections/abstract.tex') as f:\n    text = f.read()\n# Remove LaTeX begin/end\ntext = re.sub(r'\\\\\\\\begin\\{abstract\\}', '', text)\ntext = re.sub(r'\\\\\\\\end\\{abstract\\}', '', text)\n# Remove LaTeX commands but keep their arguments\ntext = re.sub(r'\\\\\\\\texttt\\{([^}]*)\\}', r'\\1', text)\ntext = re.sub(r'\\\\\\\\emph\\{([^}]*)\\}', r'\\1', text)\ntext = re.sub(r'\\\\\\\\citet\\{[^}]*\\}', '', text)\ntext = re.sub(r'\\\\\\\\citep\\{[^}]*\\}', '', text)\n# Remove math mode content but keep readable parts\ntext = re.sub(r'\\\\$[^$]*\\\\$', ' NUM ', text)\n# Remove remaining LaTeX commands\ntext = re.sub(r'\\\\\\\\[a-zA-Z]+', '', text)\ntext = re.sub(r'[{}]', '', text)\n# Clean up\ntext = re.sub(r'\\\\s+', ' ', text).strip()\nwords = text.split()\nprint(f'Word count: {len(words)}')\nprint(f'Text: {text[:500]}...')\n\"\n",
    "description": "Count abstract words more accurately"
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-24T22:59:28.840157+00:00_

Exit code 1
/bin/bash: line 1: ^$: arithmetic syntax error: operand expected (error token is "^$")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-24T22:59:35.616748+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport re\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex') as f:\n    text = f.read()\ntext = re.sub(r'\\\\begin\\{abstract\\}', '', text)\ntext = re.sub(r'\\\\end\\{abstract\\}', '', text)\ntext = re.sub(r'\\\\texttt\\{[^}]*\\}', 'TOKEN', text)\ntext = re.sub(r'\\\\emph\\{([^}]*)\\}', r'\\1', text)\ntext = re.sub(r'\\\\citet\\{[^}]*\\}', '', text)\ntext = re.sub(r'\\\\citep\\{[^}]*\\}', '', text)\n# Replace math with single placeholder\ntext = re.sub(r'\\$[^$]+\\$', ' NUM ', text)\ntext = re.sub(r'\\\\[a-zA-Z]+', '', text)\ntext = re.sub(r'[{}]', '', text)\ntext = re.sub(r'---', ' ', text)\ntext = re.sub(r'--', ' ', text)\ntext = re.sub(r'\\s+', ' ', text).strip()\nwords = [w for w in text.split() if w]\nprint(f'Word count: {len(words)}')\nPYEOF",
  "description": "Count abstract words accurately"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport re\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex') as f:\n    text = f.read()\ntext = re.sub(r'\\\\begin\\{abstract\\}', '', text)\ntext = re.sub(r'\\\\end\\{abstract\\}', '', text)\ntext = re.sub(r'\\\\texttt\\{[^}]*\\}', 'TOKEN', text)\ntext = re.sub(r'\\\\emph\\{([^}]*)\\}', r'\\1', text)\ntext = re.sub(r'\\\\citet\\{[^}]*\\}', '', text)\ntext = re.sub(r'\\\\citep\\{[^}]*\\}', '', text)\n# Replace math with single placeholder\ntext = re.sub(r'\\$[^$]+\\$', ' NUM ', text)\ntext = re.sub(r'\\\\[a-zA-Z]+', '', text)\ntext = re.sub(r'[{}]', '', text)\ntext = re.sub(r'---', ' ', text)\ntext = re.sub(r'--', ' ', text)\ntext = re.sub(r'\\s+', ' ', text).strip()\nwords = [w for w in text.split() if w]\nprint(f'Word count: {len(words)}')\nPYEOF",
    "description": "Count abstract words accurately"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-24T22:59:35.667474+00:00_

Word count: 205

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-24T23:02:50.008778+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 一篇实验设计扎实的 empirical study，scale-dependent evidence tax 和 decoupling spectrum 发现有价值，但方法论贡献有限（CED ≈ flat-NLI，RSFT 为已知框架），且存在格式微瑕（abstract 超 200 words、正文疑似溢出 8 页）。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计总体严谨，多 scale/family/dataset 交叉验证充分；但 DPO 仅测试单一 β=0.1，variance 比较方法论存在可比性问题，14B 仅 1-2 seed |\n| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 作为 empirical findings 有启发性，但缺乏方法论创新；CED 的 ablation 自证其无必要（vs flat-NLI 差 0.02pp） |\n| Reproducibility | 4/5 | 超参数完整报告（Table 3/Appendix A），LoRA 配置清晰，per-seed 结果透明；但未提供代码/数据链接 |\n| Confidence | 4/5 | 熟悉 DocRE 和 LLM RL 文献，仔细阅读了全文和附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [CRITICAL] 贡献定位模糊：empirical study 却暗示 method innovation\n- 具体位置：Section 1 (Introduction), 三个 contributions (p2)\n- 问题：三个 contribution 均为 empirical observation（evidence tax scale-dependent, gradient decoupling spectrum, RSFT variance compression）。RSFT 是已有框架（STaR/RFT/RAFT），论文自己承认\"the contribution of RSFT in our setting is not the framework itself\"（§3.3 末）。CED 作为 scoring function 被 ablation 自我否定——flat-NLI 与 CED RSFT 的 Rel-F1 差异仅 0.02pp（§4.7, Appendix B Table 4），contrastive 部分实质上无用。但论文 framing 仍然暗示方法创新（\"We formalize...\", \"we propose the Evidence-Decoupling Ratio\"），造成读者对 contribution type 的误判。\n- 为什么影响接收：EMNLP 长文需要 clear contribution positioning。Empirical study 可以被接收，但需要明确定位为\"an empirical investigation of...\"而非混合 method-and-finding 叙事。当前 framing 可能让 reviewer/AC 认为方法创新不足，而忽视 empirical findings 的真正价值。\n- 建议修改方向：(1) 将 paper 明确定位为 empirical study/benchmark study；(2) 将 CED 降级为 \"scoring tool\" 而非 \"proposed method\"，因为 ablation 已经证明 flat-NLI 等价；(3) 强调 findings 本身的独立价值（scale-dependent tax 是挑战既有假设的，decoupling spectrum 是新的分析框架）。\n\n**N2** [MAJOR] Abstract 超过 200 words\n- 具体位置：Abstract (p1)\n- 问题：经计算 abstract 约 205 words（去除 LaTeX 后），超过 EMNLP 2026 ARR 的 200-word 硬限制。Abstract 过于密集，塞入了大量数字（−5.63pp, +0.25±0.47pp, Cohen's d=2.58, 51.19, 50.19, 4.7×, Spearman ρ=1.0 等），降低可读性。\n- 为什么影响接收：格式违规可能导致 desk reject 或 reviewer 负面印象。\n- 建议修改方向：删减具体数字（保留 1-2 个关键数字即可），将 statistical detail 移入正文。Abstract 应聚焦 what you found + why it matters，而非 how much exactly。\n\n**N3** [MAJOR] 正文可能超过 8 页\n- 具体位置：PDF p8-p9\n- 问题：从 PDF 视觉检查，Section 4.7 (Discussion) 的末尾文本和 Section 5 (Conclusion) 均位于第 9 页。即主体正文（§1-§5）超出 8 页限制约 0.1-0.2 页。Limitations 和 References 不计入页数，但 Conclusion 计入。\n- 为什么影响接收：8 页是硬限制，超页可能导致 desk reject。\n- 建议修改方向：压缩 Discussion（当前 §4.7 内容部分与 Appendix 重复）或将部分 Figure/Table 移入 Appendix 以腾出空间。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [MAJOR] DPO 评估配置不足\n- 具体位置：§4.3 (Decoupling Spectrum), Table 13 (Appendix I)\n- 问题：DPO 仅测试了 β=0.1 一个配置（Table 3）。在 β=0.1 下 DPO 1-epoch Rel-F1 即暴跌至 33.37（SFT baseline 44.39），3-epoch 进一步降至 31.45。这个极端 degradation 可能是 β 选择不当导致的 artifact，而非 DPO 在 structured generation 中的固有缺陷。不同的 β 值（如 0.01 或 0.5）可能产生完全不同的 decoupling 行为。论文将此现象上升为\"DPO gradual degradation\"作为 decoupling spectrum 的核心 evidence，但 single-configuration 结论的 generalizability 存疑。\n- 建议：至少测试 2-3 个 β 值以验证 degradation 趋势的 robustness，或在 Limitations 中明确承认这一限制。\n\n**W2** [MAJOR] RSFT 与 SFT variance 比较方法论\n- 具体位置：§4.4, Figure 5, Table 6 (Appendix D)\n- 问题：论文承认 RSFT 和 SFT 的 variance \"reflect different sources of variation\"（§4.2），但在 abstract 和全文中仍以\"RSFT consistently reduces training variance\"作为核心贡献之一。SFT variance 来自独立训练 seed 的差异；RSFT variance 来自先固定一个 SFT model 再从其 8 个候选中选 top-1 后重新训练。RSFT 的 sampling-then-retraining 流程天然会压缩 variance——它本质上是对 SFT output distribution 做了平均化处理。Compression ratio（如 1.7B 的 32.6×）的实际意义需要更审慎的解读。\n- 建议：(1) 更明确地讨论 variance 来源差异；(2) 考虑报告从多个不同 SFT seed 出发做 RSFT 的 variance（目前所有 RSFT 实验似乎都从同一个 SFT model 出发），这才是公平比较。\n\n**W3** [WARNING] 14B 评估不充分\n- 具体位置：Table 2 (§4.4), Table 9 (Appendix H)\n- 问题：14B SFT 仅 1 个 seed，RSFT 仅 2 个 seed。在 test set 上 14B RSFT 相比 SFT 反而下降 0.37pp（Table 9），这与其他 scale 的趋势不一致。论文标题和 abstract 频繁使用\"across scales\"和\"consistently\"等措辞，但 14B 的证据薄弱。\n- 建议：要么增加 14B seeds，要么在 claims 中更谨慎地限定为\"three fully evaluated scales\"（论文部分地方已经这样做了，但不一致）。\n\n**W4** [WARNING] Evidence quality 未被 RSFT 改善\n- 具体位置：§4.7 (Discussion), Table 14 (Appendix K)\n- 问题：Error analysis 明确显示 RSFT 改善了 extraction（truncation FN -22%, hallucinated FP -8%, duplicates -20%）但 evidence quality 几乎不变（<0.4pp across all scales）。论文诚实地承认\"RSFT improves what the model extracts but not how well it grounds extractions\"，但这与 CED scoring 的 design motivation（基于 evidence faithfulness 做 data selection）存在张力。如果 CED 的 evidence 信号没有传导到模型行为，CED 相比 random selection 的优势主要来自 extraction quality filtering 而非 evidence quality filtering。\n- 建议：在 Discussion 中更深入分析这一 disconnect——为什么 CED 中的 evidence 信号无法改善 evidence quality？这是否意味着 evidence 能力主要由 SFT 阶段决定，post-training 只能改善 extraction？\n\n**W5** [WARNING] 缺少 DocRED 官方 test set 评测\n- 具体位置：§4.6 (Generalization)\n- 问题：论文仅在 Re-DocRED test set 上做了 test evaluation，未使用 DocRED 官方 test set（CodaLab leaderboard）。DocRED test set 是该领域的标准评测基准，大多数 prior work（ATLOP, SAIS, DREEAM, AutoRE, RelPrior）都在此报告结果。缺少此评测限制了与 prior work 的直接对比。\n- 建议：补充 DocRED test set 结果，或在 Limitations 中明确说明未使用的原因。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Evidence tax 方向约定不一致——Table 2 脚注定义\"positive = cost\"，但 Figure 7 caption 说\"negative values indicate evidence benefits extraction\"，Section 4.4 中\"$-$5.63pp\"表示 benefit。建议统一方向约定并在首次出现时明确定义。\n\n- **M2**: Bibliography key-name 不匹配——`chen2025docksrag`（第一作者 Xu）、`xu2024lmrc`（第一作者 Li）、`wang2025rear`（第一作者 Luo）、`wang2025relprior`（第一作者 Pi）、`wang2025rullm`（第一作者 Zhang）。虽然不影响渲染输出，但暗示 bib 管理粗糙。另外 `wang2025rullm` 使用 `journal = {NLPCC 2025}` 应为 `booktitle`。`wang2025rear` 无 URL。\n\n- **M3**: Section 4.5 (Evidence Strategy Comparison) 仅一段，与其作为独立 subsection 不如合并到 Discussion。BM25 baseline 的 $k=2$ 选择未 justify。\n\n- **M4**: EDCR 的 cross-method correlation（§3.5, ρ=−0.89 但 §4.7 报告 ρ=−0.96, n=7）数值不一致——§3.5 报告 $\\rho=-0.89, n=7, p=0.007$，而 §4.7 和 Appendix I 报告 $\\rho=-0.96, n=7, p<0.001$。需要统一或解释差异（可能是不同 seed aggregation 方式）。\n\n- **M5**: Table 3 hyperparameters 中 GRPO bf16 的 batch size 为 8，gradient accumulation 为 4，effective batch size 应为 32，但与 GRPO QLoRA（batch 4 × grad_accum 16 = 64）差异显著。这个差异的影响未讨论。\n\n---\n\n## Missing References 检查\n\n已覆盖的关键工作（确认完整）：\n- LLM-based DocRE: AutoRE ✓, LMRC ✓, GLiDRE ✓, RelPrior ✓, Ru-LLM ✓, DocKS-RAG ✓\n- Evidence faithfulness: SummaC ✓, DRIFT ✓, SRVF ✓, EvidenceRL ✓, InFuse ✓\n- RSFT/rejection sampling: STaR ✓, RFT ✓, RAFT ✓, RSFT≈PPO ✓, RIFT ✓, TrajFusion ✓\n- RL for structured generation: R1-RE ✓, REAR ✓, DAPO ✓, Dr.GRPO ✓, μ-GRPO ✓, Tree-GRPO ✓, MO-GRPO ✓, GDPO ✓\n\n可能遗漏的相关工作：\n1. **DeepSeek-R1** (DeepSeek-AI et al., 2025) — GRPO 最成功的应用实例，论文仅引用了 DeepSeekMath（原始 GRPO 论文），但未提及 DeepSeek-R1。鉴于 GRPO 是论文中三个方法之一且展示了 catastrophic failure，引用 GRPO 的 flagship 成功案例有助于平衡叙事。\n2. **ReST** (Gulcehre et al., 2023, \"Reinforced Self-Training\") — RSFT 的近亲方法，在 iterative self-improvement 文献中具有里程碑地位，但未被引用。\n\nRelated work 覆盖总体评价：**良好**。上述遗漏不构成重大缺失，但补充后会使 positioning 更完整。\n\n---\n\n## 主要优势\n\n1. **实验设计全面且透明**：5 个模型规模 × 2 个 model family × 2 个数据集 × 多方法对比，per-seed 结果完整报告，few papers 在 DocRE 领域达到这一实验覆盖度。Appendix 内容详实（error analysis, per-relation EDCR, qualitative examples, inference efficiency），体现了严谨的实验态度。\n\n2. **Scale-dependent evidence tax 是非平凡发现**：1.7B 从 evidence 中获益（−5.63pp，通过减少 duplication）而 ≥4B 近似中性——这一 finding 挑战了\"evidence generation always costs accuracy\"的朴素假设，且 mechanistic explanation（implicit regularization via output structure constraint, Table 7）具有说服力。\n\n3. **Decoupling spectrum 提供了有用的分析框架**：GRPO catastrophic → DPO gradual → RSFT none 的 continuum 直观地总结了不同 optimization paradigm 在 multi-objective structured generation 中的行为差异。GRPO QLoRA 的 catastrophic collapse（Rel-F1 降至 1.38，Evi-F1 仍有 85.04）是一个令人印象深刻的 negative result。\n\n4. **RSFT 的实际价值清晰**：1.7B RSFT（51.19 Ign-F1, std 0.09pp）接近 8B SFT（50.19, std 3.23pp），在 4.7× fewer parameters 下实现部署效率——这对资源受限场景有直接的 practical implication。\n\n5. **写作质量整体良好**：叙事线清晰（gap → formalization → comparison → findings），technique 解释准确，Figure/Table 信息密度高但可读。§3.5 EDCR 定义和 §3.4 CED 公式表述清晰。\n\n---\n\n## Claim-Evidence 对齐检查\n\n| Claim (Abstract/Intro) | 证据位置 | 对齐状态 |\n|---|---|---|\n| \"beneficial at 1.7B (−5.63pp)\" | Table 8 (Appendix F), matched@2048 | ✓ 一致 |\n| \"approximately neutral at ≥4B (+0.25±0.47pp)\" | Table 8, three-seed mean | ✓ 一致 |\n| \"GRPO catastrophic\" | Table 13, Rel-F1=1.38 | ✓ 一致 |\n| \"Cohen's d=2.58\" | Table 6, LLaMA-3.1-8B | ✓ 一致（注意 abstract 说 \"on LLaMA\"） |\n| \"1.7B RSFT approaches 8B SFT (51.19 vs 50.19)\" | Table 2 | ✓ 一致 |\n| \"Spearman ρ=1.0\" | §4.6, Table 9 | ✓ 一致 |\n| \"RSFT consistently reduces training variance\" | Figure 5, Table 6 | ⚠ 方向一致但可比性存疑（W2） |\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文 ≤8 页 | ⚠ 疑似超页 | §4.7 末尾 + §5 Conclusion 溢出至 p9 |\n| Abstract ≤200 words | ✗ ~205 words | 需删减 |\n| Limitations 存在 | ✓ | §6, 约 0.5 页，覆盖 3 点 |\n| 匿名 | ✓ | \"Anonymous ACL submission\", 无信息泄露 |\n| ACL 模板 [review] | ✓ | `\\usepackage[review]{acl}` |\n| 参考文献格式 | ⚠ | 大部分一致，个别条目有问题（M2） |\n| Ethical considerations | ✓ | Appendix O: AI assistants 使用声明 |\n\n---\n\n**总结**：这是一篇实验功底扎实的 empirical study，核心 findings（scale-dependent tax, decoupling spectrum）对 evidence-grounded IE 社区有价值。主要短板是 (1) 方法论创新有限且 CED 被自己的 ablation 否定了独特性，(2) 格式问题需修正，(3) DPO 单配置和 RSFT variance 比较方法需加强。建议定位为 Findings 论文或在 contribution framing 上做调整后冲击 main conference。",
  "reviewer_id": "2",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 一篇实验设计扎实的 empirical study，scale-dependent evidence tax 和 decoupling spectrum 发现有价值，但方法论贡献有限（CED ≈ flat-NLI，RSFT 为已知框架），且存在格式微瑕（abstract 超 200 words、正文疑似溢出 8 页）。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计总体严谨，多 scale/family/dataset 交叉验证充分；但 DPO 仅测试单一 β=0.1，variance 比较方法论存在可比性问题，14B 仅 1-2 seed |\n| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 作为 empirical findings 有启发性，但缺乏方法论创新；CED 的 ablation 自证其无必要（vs flat-NLI 差 0.02pp） |\n| Reproducibility | 4/5 | 超参数完整报告（Table 3/Appendix A），LoRA 配置清晰，per-seed 结果透明；但未提供代码/数据链接 |\n| Confidence | 4/5 | 熟悉 DocRE 和 LLM RL 文献，仔细阅读了全文和附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [CRITICAL] 贡献定位模糊：empirical study 却暗示 method innovation\n- 具体位置：Section 1 (Introduction), 三个 contributions (p2)\n- 问题：三个 contribution 均为 empirical observation（evidence tax scale-dependent, gradient decoupling spectrum, RSFT variance compression）。RSFT 是已有框架（STaR/RFT/RAFT），论文自己承认\"the contribution of RSFT in our setting is not the framework itself\"（§3.3 末）。CED 作为 scoring function 被 ablation 自我否定——flat-NLI 与 CED RSFT 的 Rel-F1 差异仅 0.02pp（§4.7, Appendix B Table 4），contrastive 部分实质上无用。但论文 framing 仍然暗示方法创新（\"We formalize...\", \"we propose the Evidence-Decoupling Ratio\"），造成读者对 contribution type 的误判。\n- 为什么影响接收：EMNLP 长文需要 clear contribution positioning。Empirical study 可以被接收，但需要明确定位为\"an empirical investigation of...\"而非混合 method-and-finding 叙事。当前 framing 可能让 reviewer/AC 认为方法创新不足，而忽视 empirical findings 的真正价值。\n- 建议修改方向：(1) 将 paper 明确定位为 empirical study/benchmark study；(2) 将 CED 降级为 \"scoring tool\" 而非 \"proposed method\"，因为 ablation 已经证明 flat-NLI 等价；(3) 强调 findings 本身的独立价值（scale-dependent tax 是挑战既有假设的，decoupling spectrum 是新的分析框架）。\n\n**N2** [MAJOR] Abstract 超过 200 words\n- 具体位置：Abstract (p1)\n- 问题：经计算 abstract 约 205 words（去除 LaTeX 后），超过 EMNLP 2026 ARR 的 200-word 硬限制。Abstract 过于密集，塞入了大量数字（−5.63pp, +0.25±0.47pp, Cohen's d=2.58, 51.19, 50.19, 4.7×, Spearman ρ=1.0 等），降低可读性。\n- 为什么影响接收：格式违规可能导致 desk reject 或 reviewer 负面印象。\n- 建议修改方向：删减具体数字（保留 1-2 个关键数字即可），将 statistical detail 移入正文。Abstract 应聚焦 what you found + why it matters，而非 how much exactly。\n\n**N3** [MAJOR] 正文可能超过 8 页\n- 具体位置：PDF p8-p9\n- 问题：从 PDF 视觉检查，Section 4.7 (Discussion) 的末尾文本和 Section 5 (Conclusion) 均位于第 9 页。即主体正文（§1-§5）超出 8 页限制约 0.1-0.2 页。Limitations 和 References 不计入页数，但 Conclusion 计入。\n- 为什么影响接收：8 页是硬限制，超页可能导致 desk reject。\n- 建议修改方向：压缩 Discussion（当前 §4.7 内容部分与 Appendix 重复）或将部分 Figure/Table 移入 Appendix 以腾出空间。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [MAJOR] DPO 评估配置不足\n- 具体位置：§4.3 (Decoupling Spectrum), Table 13 (Appendix I)\n- 问题：DPO 仅测试了 β=0.1 一个配置（Table 3）。在 β=0.1 下 DPO 1-epoch Rel-F1 即暴跌至 33.37（SFT baseline 44.39），3-epoch 进一步降至 31.45。这个极端 degradation 可能是 β 选择不当导致的 artifact，而非 DPO 在 structured generation 中的固有缺陷。不同的 β 值（如 0.01 或 0.5）可能产生完全不同的 decoupling 行为。论文将此现象上升为\"DPO gradual degradation\"作为 decoupling spectrum 的核心 evidence，但 single-configuration 结论的 generalizability 存疑。\n- 建议：至少测试 2-3 个 β 值以验证 degradation 趋势的 robustness，或在 Limitations 中明确承认这一限制。\n\n**W2** [MAJOR] RSFT 与 SFT variance 比较方法论\n- 具体位置：§4.4, Figure 5, Table 6 (Appendix D)\n- 问题：论文承认 RSFT 和 SFT 的 variance \"reflect different sources of variation\"（§4.2），但在 abstract 和全文中仍以\"RSFT consistently reduces training variance\"作为核心贡献之一。SFT variance 来自独立训练 seed 的差异；RSFT variance 来自先固定一个 SFT model 再从其 8 个候选中选 top-1 后重新训练。RSFT 的 sampling-then-retraining 流程天然会压缩 variance——它本质上是对 SFT output distribution 做了平均化处理。Compression ratio（如 1.7B 的 32.6×）的实际意义需要更审慎的解读。\n- 建议：(1) 更明确地讨论 variance 来源差异；(2) 考虑报告从多个不同 SFT seed 出发做 RSFT 的 variance（目前所有 RSFT 实验似乎都从同一个 SFT model 出发），这才是公平比较。\n\n**W3** [WARNING] 14B 评估不充分\n- 具体位置：Table 2 (§4.4), Table 9 (Appendix H)\n- 问题：14B SFT 仅 1 个 seed，RSFT 仅 2 个 seed。在 test set 上 14B RSFT 相比 SFT 反而下降 0.37pp（Table 9），这与其他 scale 的趋势不一致。论文标题和 abstract 频繁使用\"across scales\"和\"consistently\"等措辞，但 14B 的证据薄弱。\n- 建议：要么增加 14B seeds，要么在 claims 中更谨慎地限定为\"three fully evaluated scales\"（论文部分地方已经这样做了，但不一致）。\n\n**W4** [WARNING] Evidence quality 未被 RSFT 改善\n- 具体位置：§4.7 (Discussion), Table 14 (Appendix K)\n- 问题：Error analysis 明确显示 RSFT 改善了 extraction（truncation FN -22%, hallucinated FP -8%, duplicates -20%）但 evidence quality 几乎不变（<0.4pp across all scales）。论文诚实地承认\"RSFT improves what the model extracts but not how well it grounds extractions\"，但这与 CED scoring 的 design motivation（基于 evidence faithfulness 做 data selection）存在张力。如果 CED 的 evidence 信号没有传导到模型行为，CED 相比 random selection 的优势主要来自 extraction quality filtering 而非 evidence quality filtering。\n- 建议：在 Discussion 中更深入分析这一 disconnect——为什么 CED 中的 evidence 信号无法改善 evidence quality？这是否意味着 evidence 能力主要由 SFT 阶段决定，post-training 只能改善 extraction？\n\n**W5** [WARNING] 缺少 DocRED 官方 test set 评测\n- 具体位置：§4.6 (Generalization)\n- 问题：论文仅在 Re-DocRED test set 上做了 test evaluation，未使用 DocRED 官方 test set（CodaLab leaderboard）。DocRED test set 是该领域的标准评测基准，大多数 prior work（ATLOP, SAIS, DREEAM, AutoRE, RelPrior）都在此报告结果。缺少此评测限制了与 prior work 的直接对比。\n- 建议：补充 DocRED test set 结果，或在 Limitations 中明确说明未使用的原因。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Evidence tax 方向约定不一致——Table 2 脚注定义\"positive = cost\"，但 Figure 7 caption 说\"negative values indicate evidence benefits extraction\"，Section 4.4 中\"$-$5.63pp\"表示 benefit。建议统一方向约定并在首次出现时明确定义。\n\n- **M2**: Bibliography key-name 不匹配——`chen2025docksrag`（第一作者 Xu）、`xu2024lmrc`（第一作者 Li）、`wang2025rear`（第一作者 Luo）、`wang2025relprior`（第一作者 Pi）、`wang2025rullm`（第一作者 Zhang）。虽然不影响渲染输出，但暗示 bib 管理粗糙。另外 `wang2025rullm` 使用 `journal = {NLPCC 2025}` 应为 `booktitle`。`wang2025rear` 无 URL。\n\n- **M3**: Section 4.5 (Evidence Strategy Comparison) 仅一段，与其作为独立 subsection 不如合并到 Discussion。BM25 baseline 的 $k=2$ 选择未 justify。\n\n- **M4**: EDCR 的 cross-method correlation（§3.5, ρ=−0.89 但 §4.7 报告 ρ=−0.96, n=7）数值不一致——§3.5 报告 $\\rho=-0.89, n=7, p=0.007$，而 §4.7 和 Appendix I 报告 $\\rho=-0.96, n=7, p<0.001$。需要统一或解释差异（可能是不同 seed aggregation 方式）。\n\n- **M5**: Table 3 hyperparameters 中 GRPO bf16 的 batch size 为 8，gradient accumulation 为 4，effective batch size 应为 32，但与 GRPO QLoRA（batch 4 × grad_accum 16 = 64）差异显著。这个差异的影响未讨论。\n\n---\n\n## Missing References 检查\n\n已覆盖的关键工作（确认完整）：\n- LLM-based DocRE: AutoRE ✓, LMRC ✓, GLiDRE ✓, RelPrior ✓, Ru-LLM ✓, DocKS-RAG ✓\n- Evidence faithfulness: SummaC ✓, DRIFT ✓, SRVF ✓, EvidenceRL ✓, InFuse ✓\n- RSFT/rejection sampling: STaR ✓, RFT ✓, RAFT ✓, RSFT≈PPO ✓, RIFT ✓, TrajFusion ✓\n- RL for structured generation: R1-RE ✓, REAR ✓, DAPO ✓, Dr.GRPO ✓, μ-GRPO ✓, Tree-GRPO ✓, MO-GRPO ✓, GDPO ✓\n\n可能遗漏的相关工作：\n1. **DeepSeek-R1** (DeepSeek-AI et al., 2025) — GRPO 最成功的应用实例，论文仅引用了 DeepSeekMath（原始 GRPO 论文），但未提及 DeepSeek-R1。鉴于 GRPO 是论文中三个方法之一且展示了 catastrophic failure，引用 GRPO 的 flagship 成功案例有助于平衡叙事。\n2. **ReST** (Gulcehre et al., 2023, \"Reinforced Self-Training\") — RSFT 的近亲方法，在 iterative self-improvement 文献中具有里程碑地位，但未被引用。\n\nRelated work 覆盖总体评价：**良好**。上述遗漏不构成重大缺失，但补充后会使 positioning 更完整。\n\n---\n\n## 主要优势\n\n1. **实验设计全面且透明**：5 个模型规模 × 2 个 model family × 2 个数据集 × 多方法对比，per-seed 结果完整报告，few papers 在 DocRE 领域达到这一实验覆盖度。Appendix 内容详实（error analysis, per-relation EDCR, qualitative examples, inference efficiency），体现了严谨的实验态度。\n\n2. **Scale-dependent evidence tax 是非平凡发现**：1.7B 从 evidence 中获益（−5.63pp，通过减少 duplication）而 ≥4B 近似中性——这一 finding 挑战了\"evidence generation always costs accuracy\"的朴素假设，且 mechanistic explanation（implicit regularization via output structure constraint, Table 7）具有说服力。\n\n3. **Decoupling spectrum 提供了有用的分析框架**：GRPO catastrophic → DPO gradual → RSFT none 的 continuum 直观地总结了不同 optimization paradigm 在 multi-objective structured generation 中的行为差异。GRPO QLoRA 的 catastrophic collapse（Rel-F1 降至 1.38，Evi-F1 仍有 85.04）是一个令人印象深刻的 negative result。\n\n4. **RSFT 的实际价值清晰**：1.7B RSFT（51.19 Ign-F1, std 0.09pp）接近 8B SFT（50.19, std 3.23pp），在 4.7× fewer parameters 下实现部署效率——这对资源受限场景有直接的 practical implication。\n\n5. **写作质量整体良好**：叙事线清晰（gap → formalization → comparison → findings），technique 解释准确，Figure/Table 信息密度高但可读。§3.5 EDCR 定义和 §3.4 CED 公式表述清晰。\n\n---\n\n## Claim-Evidence 对齐检查\n\n| Claim (Abstract/Intro) | 证据位置 | 对齐状态 |\n|---|---|---|\n| \"beneficial at 1.7B (−5.63pp)\" | Table 8 (Appendix F), matched@2048 | ✓ 一致 |\n| \"approximately neutral at ≥4B (+0.25±0.47pp)\" | Table 8, three-seed mean | ✓ 一致 |\n| \"GRPO catastrophic\" | Table 13, Rel-F1=1.38 | ✓ 一致 |\n| \"Cohen's d=2.58\" | Table 6, LLaMA-3.1-8B | ✓ 一致（注意 abstract 说 \"on LLaMA\"） |\n| \"1.7B RSFT approaches 8B SFT (51.19 vs 50.19)\" | Table 2 | ✓ 一致 |\n| \"Spearman ρ=1.0\" | §4.6, Table 9 | ✓ 一致 |\n| \"RSFT consistently reduces training variance\" | Figure 5, Table 6 | ⚠ 方向一致但可比性存疑（W2） |\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文 ≤8 页 | ⚠ 疑似超页 | §4.7 末尾 + §5 Conclusion 溢出至 p9 |\n| Abstract ≤200 words | ✗ ~205 words | 需删减 |\n| Limitations 存在 | ✓ | §6, 约 0.5 页，覆盖 3 点 |\n| 匿名 | ✓ | \"Anonymous ACL submission\", 无信息泄露 |\n| ACL 模板 [review] | ✓ | `\\usepackage[review]{acl}` |\n| 参考文献格式 | ⚠ | 大部分一致，个别条目有问题（M2） |\n| Ethical considerations | ✓ | Appendix O: AI assistants 使用声明 |\n\n---\n\n**总结**：这是一篇实验功底扎实的 empirical study，核心 findings（scale-dependent tax, decoupling spectrum）对 evidence-grounded IE 社区有价值。主要短板是 (1) 方法论创新有限且 CED 被自己的 ablation 否定了独特性，(2) 格式问题需修正，(3) DPO 单配置和 RSFT variance 比较方法需加强。建议定位为 Findings 论文或在 contribution framing 上做调整后冲击 main conference。",
    "reviewer_id": "2",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-24T23:02:53.725194+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3716
}
```

</details>

---

### Assistant

_source line 240 · 2026-05-24T23:03:07.461835+00:00_

审稿报告已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。

主要发现：
- **3 个 Must-Fix**：贡献定位模糊（empirical study 但暗示 method innovation，CED 被自己的 ablation 否定）、abstract 超 200 words (~205)、正文疑似溢出 8 页
- **5 个 Should-Fix**：DPO 仅测试单一 β=0.1、RSFT vs SFT variance 可比性存疑、14B 仅 1-2 seed、evidence quality 未被 RSFT 改善、缺少 DocRED 官方 test set
- **5 个 Minor**：evidence tax 方向约定不一致、bib key-name 不匹配、§4.5 篇幅过短、EDCR correlation 数值不一致（§3.5 vs §4.7）、GRPO batch size 差异未讨论
- **Missing references**：DeepSeek-R1、ReST（非重大遗漏）
- **Claim-evidence 对齐**：数字均可验证，总体一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---

## Round 6

2 recorded events

### User

_source line 241 · 2026-05-24T23:04:22.105257+00:00_

[Round 3 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿报告

**Overall**: 3.5 (Borderline Conference)
**Soundness 3/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5**

### Must-Fix 问题

**N1** [CRITICAL] GRPO QLoRA vs bf16 实验存在未隔离的混淆变量
- 两个配置同时改变了 quantization（NF4 4-bit vs bf16）**和** group size（G=4 vs G=8）。没有控制实验（QLoRA G=8 或 bf16 G=4）来隔离这两个因素。
- Paper 将 collapse 归因于 "quantization precision rather than group size as the primary factor"（§4.3），但这是没有控制实验支撑的归因。
- 建议：增加 bf16 G=4 实验，或将结论降级为 "quantization and/or group size"。

**N2** [CRITICAL] 方差压缩声明的统计证据不足（n=3 seeds）
- 4/4 scales 中仅 1.7B 的 χ² CI 不重叠。Sign test p=0.0625，不满足 α=0.05。Cohen's d 在 4B 仅为 0.46。
- Abstract 选择性报告最强结果（cherry-picking）。
- 建议：将 "consistently reduces" 改为 "shows a consistent directional pattern with statistical significance only at 1.7B"；增加 seeds。

### Should-Fix 问题

**W1** [MAJOR] Evidence tax 因果推断——implicit regularization 假说证据不足
- 1.7B evidence 模型只生成 25.5k vs no-evidence 44.6k predictions。更简单的替代解释：evidence 格式限制总 prediction 数量，机械性减少 duplication/FP。
- 建议：在 matched prediction count 下重新计算 tax，或降级为 "output constraint effect"。

**W2** [MAJOR] GRPO/DPO 超参数探索不足
- GRPO 只测 KL=0.01，DPO 只测 β=0.1。DPO 1-epoch Rel-F1 暴跌 -11pp 可能是 β 不当。
- 建议：至少 β ∈ {0.01, 0.1, 0.5}, KL ∈ {0.001, 0.01, 0.1}。

**W3** [MAJOR] 14B test-set reversal 削弱泛化性
- 14B RSFT dev +3.44pp，test Δ=-0.37pp。RSFT 可能偏好 compact outputs，在 annotation-sparse dev 上有利但 annotation-dense test 上不利。
- 建议：分析 precision/recall trade-off。

**W4** [MAJOR] EDCR 与 Rel-F1 的 mechanical correlation 未被 partial correlation 充分控制
- FP triples 同时影响 EDCR numerator 和 Rel-F1，正确控制变量应是 precision/FP rate 而非 Evi-Recall_TP。Per-relation 数据来自相同 documents，不完全独立。
- 建议：控制 per-relation precision；讨论 non-independence。

**W5** [MAJOR] RSFT 的 "cannot exploit the trade-off" 论证是结构性的而非实证的
- 缺少 Rel-F1-only 或 Evi-F1-only RSFT 实验来验证。Random selection（41.14）对比 SFT mean（43.58）实际更差，说明 selection 本身贡献可能为负。
- 建议：增加 single-objective RSFT 实验；random baseline 应对比 SFT multi-seed mean。

### 小问题
- M1: 正文可能超 8 页（§5 溢出至 p9）
- M2: Decoupling spectrum 仅在 4B 验证
- M3: SFT no-evidence 仅 s42 单 seed
- M4: CED hypothesis verbalization template sensitivity 未讨论
- M5: Training-time vs inference-time tax 定义混用

### 主要优势
1. 系统性实验覆盖（3 paradigms × 4+ scales × 2 families × 2 datasets × multiple seeds）
2. Novel observations（scale-dependent tax, decoupling spectrum）
3. 透明度高（主动讨论 limitations）
4. 实用价值（1.7B RSFT ≈ 8B SFT at 4.7× fewer params）
5. Thorough appendix（11 sections）
6. RSFT + CED 组合在 evidence-grounded DocRE 中的有效应用

### Missing References
未发现明显遗漏。

---

请对以上每一条逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Assistant

_source line 242 · 2026-05-24T23:06:34.745289+00:00_

逐条回应 Reviewer 1 的审稿意见。

---

## 交叉回应：Reviewer 2 对 Reviewer 1

### Must-Fix 问题

**[AGREE] R1-N1: GRPO QLoRA vs bf16 存在未隔离的混淆变量**

同意这是一个实验设计缺陷。Table 3 明确显示 QLoRA G=4 和 bf16 G=8 同时改变了两个变量（quantization + group size），§4.3 的归因"confirming quantization precision rather than group size as the primary factor"缺乏控制实验支撑。论文引用 QuRL (Li et al., 2026) 的 quantized-actor divergence 提供了间接旁证，但这不能替代直接的消融实验。建议至少增加 bf16 G=4 或 QLoRA G=8 中的一组。若计算资源有限，应将结论降级为"quantization and/or group size"。

---

**[AGREE] R1-N2: 方差压缩声明的统计证据不足**

同意。我在自己的审稿中也标注了类似问题（我的 W2）。核心数据来自 Table 6 (Appendix D)：仅 1.7B 的 χ² CI 不重叠（SFT lower bound 1.45pp > RSFT upper bound 0.54pp），其余 3 个 scale 均重叠；sign test p=0.0625 不满足 α=0.05；4B Cohen's d=0.46 属于 small effect。论文自身的脚注已承认"underpowered"，但 abstract 仍以"RSFT consistently reduces training seed variance"作为第三条 contribution，且选择性报告了 LLaMA 的 Cohen's d=2.58 和 1.7B 的 non-overlapping CI——这确实构成 cherry-picking。

补充一个我的独立观察（我的 W2）：RSFT 和 SFT 的 variance 来源不同。SFT variance 是独立训练 seed 的差异；RSFT 从固定 SFT model 出发做 sampling + retraining，天然压缩了上游 variance。论文 §4.2 承认"these reflect different sources of variation"，但后续 claims 未贯彻这一限定。

---

### Should-Fix 问题

**[AGREE] R1-W1: Implicit regularization 假说证据不足**

同意更简约的解释是 output constraint effect。Table 7 (Appendix E) 显示 1.7B evidence model 生成 25.5k predictions vs no-evidence 44.6k（1.75× 差异），duplication rate 从 60.5% 降至 33.0%。这更直接地解释为：evidence 格式占用 token budget → 模型物理上只能生成更少 triples → 更少的 FP 和 duplicates → 更高的 precision。将此称为"implicit regularization"暗示模型内部表征发生了改善，但现有证据无法区分"模型学到了更好的表征"和"模型只是被迫生成更少output"。

不过，我补充一个细节：Appendix E 的 matched@2048 fair evaluation（971/985 documents）在相同 max_new_tokens 下仍然观察到 −5.63pp benefit。如果纯粹是 token budget constraint，那么在 @2048 下（evidence model 不再受限于 1024 tokens）这个 benefit 应该减弱。论文未充分讨论这一点，但它对纯 output constraint 解释构成了部分挑战。建议论文区分讨论这两种机制的贡献。

---

**[AGREE] R1-W2: GRPO/DPO 超参数探索不足**

强烈同意。我在自己的审稿中提出了相同问题（我的 W1）。DPO β=0.1 下 1-epoch Rel-F1 暴跌至 33.37（从 SFT 44.39），降幅达 11pp——在 DPO 文献中这种程度的 degradation 通常指向超参数不当而非方法固有缺陷。Decoupling spectrum 的"DPO gradual degradation"结论建立在单一 β 值上，generalizability 成问题。GRPO KL=0.01 同理。

---

**[AGREE] R1-W3: 14B test-set reversal**

同意。我同样标注了此问题（我的 W3）。补充 Reviewer 1 的分析：Table 9 (Appendix H) 显示 14B SFT truncation rate 50.6% vs RSFT 仅 13.4%。在 annotation-dense test set (34.7 triples/doc vs dev 12.3) 下，higher truncation = longer outputs = more candidate triples to match，SFT 的高 truncation rate 反而可能在 recall-heavy 场景中有利。论文对此的解释（§H, "the SFT model's 50.6% truncation rate implies longer outputs"）方向正确但分析不充分——应该分解为 precision 和 recall 的独立变化来验证。

---

**[REBUT] R1-W4: EDCR mechanical correlation 未被充分控制**

部分反驳。Reviewer 1 关于 FP 同时驱动 EDCR 和 Rel-F1 的 concern 在 cross-method 层面是成立的——这也是论文自己承认的（§3.5："Because EDCR is mechanically influenced by false-positive triples...this correlation should be interpreted as a diagnostic pattern rather than an independent discovery"）。

但 Reviewer 1 对 per-relation analysis 的质疑（"来自相同 documents，不完全独立"）过于严格。Per-relation EDCR（§I, Appendix I）在同一模型配置内按 relation type 分组计算，ρ=−0.79 (n=76, p<0.001) 且与 Evi-F1 正交（ρ=−0.06, p=0.58）。这一分析的关键优势是：per-relation 级别不存在 cross-method 层面的 shared-component concern——同一模型的所有 relation types 共享相同的整体 FP 倾向，但不同 relation types 的 FP 率是独立变化的。论文还报告了 10,000-iteration permutation test (p<0.0001)，这在统计上是充分的。

建议论文增加 per-relation precision 作为额外控制变量的 partial correlation（Reviewer 1 的具体建议），但现有 per-relation evidence 已经提供了 reasonable validation。将此问题的严重性从 MAJOR 降级为 WARNING 更合适。

---

**[AGREE] R1-W5: RSFT "cannot exploit trade-off" 论证缺乏实证**

同意核心观点：§G (Appendix G) 的论证完全是 structural/logical 的（"because the selection is discrete...there is no gradient pathway"），缺少实证验证。Single-objective RSFT（仅按 Rel-F1 或仅按 Evi-F1 选择）是一个 natural 且 computationally cheap 的实验，能直接测试"CED 的 joint scoring 是否是 RSFT 保持 coupling 的关键因素"。

但在 random selection 解读上部分反驳 Reviewer 1 的说法。Reviewer 1 说"Random selection（41.14）对比 SFT mean（43.58）实际更差，说明 selection 本身贡献可能为负"——这里的 baseline 选择有误。Random RSFT 从 SFT s42（39.74）出发，应与 SFT s42 比较（+1.40pp），而非与 SFT three-seed mean（43.58）比较。SFT mean 高是因为 s43（43.65）和 s44（47.34）远强于 s42；用 multi-seed mean 作 baseline 会将 RSFT 不使用的 seed 的性能纳入比较，不公平。正确解读是：random selection 贡献 +1.40pp（来自 retraining on own outputs 的一般 benefit），CED scoring 在此基础上再贡献 +3.52pp。

---

### 小问题

**[AGREE] R1-M1: 正文超 8 页** — 我同样标注了此问题（我的 N3）。§4.7 末尾和 §5 Conclusion 溢出至 p9。

**[AGREE] R1-M2: Decoupling spectrum 仅在 4B 验证** — 合理 concern。GRPO/DPO 实验仅在 4B scale 做了，无法确认 spectrum 在其他 scale 是否保持。不过考虑到 GRPO/DPO 训练的计算成本，single-scale 验证作为 initial evidence 可以接受，应在 Limitations 中声明。

**[AGREE] R1-M3: SFT no-evidence 仅 s42 单 seed** — 部分同意。Table 8 (Appendix F) 显示 4B training-time tax 使用了 three-seed mean (+0.25±0.47pp)，是充分的。但 1.7B 和 8B 均为单 seed (s42)，且 1.7B 的 s42 是 SFT 最强 seed（论文自己承认"s42 is the strongest SFT seed, +3.22pp above three-seed mean"），可能放大了 evidence tax benefit。

**[AGREE] R1-M4: CED hypothesis verbalization template sensitivity** — 我未在自己的审稿中提到此点，但认为有效。CED 依赖 NLI 模型对"$e_h$ has relation $r$ with $e_t$"的 entailment 判断，不同 verbalization 模板（如"$e_h$'s $r$ is $e_t$"或更自然的表述）可能产生不同的 CED scores。论文未讨论 template sensitivity。不过，考虑到 CED vs flat-NLI 差异仅 0.02pp（Table 4, Appendix B），CED 的 fine-grained scoring 本身贡献有限，template sensitivity 对最终结果的影响可能也有限。

**[AGREE] R1-M5: Training-time vs inference-time tax 定义混用** — 我在自己的审稿中也指出了 evidence tax 方向约定不一致（我的 M1）。Table 2 脚注定义"positive = cost"，Figure 7 caption 说"negative = benefit"，Appendix F Table 8 又说"positive = cost"——方向一致但正负 convention 的首次出现位置较晚，增加认知负担。

---

### 对 Reviewer 1 优势评价的回应

Reviewer 1 列出的 6 条优势与我的评估高度一致。补充一点：Reviewer 1 提到"RSFT + CED 组合在 evidence-grounded DocRE 中的有效应用"——我对此持保留态度，因为 CED 被 ablation 证明与 flat-NLI 等价（Rel-F1 差 0.02pp, Table 4），CED 的独特贡献主要在 interpretability（per-triple discrimination scores for error analysis）而非 data selection quality。

---

### 总结

与 Reviewer 1 的评分一致（Overall 3.5 Borderline Conference, Soundness 3-3.5, Excitement 3）。两位 reviewer 在以下核心问题上达成共识：
1. **GRPO/DPO 超参数探索不足**（R1-W2 = R2-W1）
2. **14B 证据薄弱**（R1-W3 = R2-W3）
3. **正文超页**（R1-M1 = R2-N3）
4. **方差压缩统计不足**（R1-N2 ≈ R2-W2）

唯一实质分歧在 R1-W4（EDCR mechanical correlation）——我认为 per-relation analysis 已提供了 adequate validation，严重性应为 WARNING 而非 MAJOR。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---

## Round 7

58 recorded events

### User

_source line 243 · 2026-05-25T22:31:25.836404+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**审查。

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

1. **新颖性评估**：
   - 三个 contribution 的新颖性：(1) scale-dependent evidence tax, (2) decoupling spectrum + EDCR, (3) RSFT avoids decoupling
   - 论文自我定位为 empirical study 而非 method innovation——这够 EMNLP main/findings 吗？
   - RSFT 不是新方法（STaR 2022），CED 不是独立贡献（vs flat-NLI 仅 0.02pp）——核心新颖性在哪？
   - EDCR 作为诊断指标的价值 vs 简单地报告 Evi-F1
   - "Evidence is not uniformly harmful" 这个发现的影响力——之前文献有无类似结论？

2. **Related Work 覆盖**：
   - DocRE 领域覆盖是否充分？是否遗漏重要工作？
   - RL for structured generation 文献是否 up to date？
   - Evidence faithfulness 文献链是否完整？
   - 是否有 multi-task learning / task interference 相关文献遗漏？

3. **写作质量**：
   - Abstract 是否准确反映论文核心发现？有无夸大？
   - Introduction 的叙事是否清晰——从 gap 到 contribution 的逻辑链
   - §4.4 (scaling) 信息密度是否过高？段落长度是否合理？
   - Conclusion 是否过短？（当前仅 2 行）
   - 术语一致性：evidence tax 的 sign convention 是否全文一致？
   - Figure/Table caption 是否 self-contained？

4. **格式合规**：
   - 18 页 PDF：正文 vs Limitations vs References vs Appendix 的页数分布
   - 匿名合规：是否有泄露作者身份的信息？
   - Abstract 字数（~181 words，需 ≤200）
   - 引用格式是否一致（natbib）？
   - Appendix 结构和编号是否规范？

5. **完整性**：
   - Limitations 是否充分？遗漏了什么？
   - 是否有未解释的异常结果？（如 14B test-set reversal、4B evidence tax inconsistency）
   - Re-DocRED test 20pp drop 的解释是否足够？
   - DPO 只测了 β=0.1，这个限制是否充分讨论？

请按 Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment 的结构输出审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-25T22:31:35.122283+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 245 · 2026-05-25T22:31:35.223034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-25T22:31:39.607014+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
  "project": "faith-evidence-ie",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
    "project": "faith-evidence-ie",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 247 · 2026-05-25T22:31:39.909148+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 248 · 2026-05-25T22:31:42.572865+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 623.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 647.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.1}, {\"page\": 10, \"pa
…[truncated 427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2965
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-25T22:31:42.573358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 2664
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-25T22:31:46.086913+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 251 · 2026-05-25T22:31:46.440423+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-25T22:31:46.895585+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-25T22:31:47.805015+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1718
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-25T22:31:47.806143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1365
}
```

</details>

---

### Tool call

_source line 255 · 2026-05-25T22:31:47.808620+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-25T22:31:48.313060+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1417
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-25T22:31:48.313512+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-25T22:31:48.665870+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---

### Tool call

_source line 259 · 2026-05-25T22:31:48.666454+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-25T22:31:49.221227+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-25T22:31:55.663535+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Main vs Findings papers, the main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

The review scoring options include:
- 5 = Consider for Award: papers that could be conside
…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6997
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-25T22:32:00.694742+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-25T22:32:01.700754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-25T22:32:01.701291+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 265 · 2026-05-25T22:32:02.205420+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-25T22:32:02.760946+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---

### Tool call

_source line 267 · 2026-05-25T22:32:02.761469+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-25T22:32:03.617664+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---

### Tool result

_source line 269 · 2026-05-25T22:32:03.618965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-25T22:32:03.619352+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool call

_source line 271 · 2026-05-25T22:32:04.122859+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 272 · 2026-05-25T22:32:04.174430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-25T22:32:04.682487+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1063
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-25T22:32:11.517800+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions/criteria, their scoring scales, and descriptions. I need the exact dimensions reviewers are asked to score on."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions/criteria, their scoring scales, and descriptions. I need the exact dimensions reviewers are asked to score on."
  }
}
```

</details>

---

### Tool call

_source line 275 · 2026-05-25T22:32:13.274903+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
  "project": "faith-evidence-ie",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
    "project": "faith-evidence-ie",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 276 · 2026-05-25T22:32:16.090544+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Evaluation Criteria

**1. Reviewer Confidence** (1-5 scale)
"Positive that my evaluation is correct" (5) to "Not my area, or paper is very hard to understand" (1)

**2. Soundness** (1-5 scale with half-point increments)
"Excellent: This study is one of the most thorough" (5) to "Major Issues: This study is not yet sufficiently thorough to warrant publication" (1)

**3. Excitement** (1-5 scale with half-point increments)
"Highly Exciting: I would recommend this paper to others" (5) to "Not Exciting: this paper does not resonate with me" (1)

**4. Overall Assessment** (1-5 scale with half-point increments)
"Consider for Award" (5) to "Do not resubmit: This paper has to be fully redone" (1)

## Additional Evaluation Areas

**5. Reproducibility** (1-5 scale)
"They could easily reproduce the results" (5) to "They would not be able to reproduce the results" (1)

**6. Datasets** (1-5 scale)
"Enabling: The newly released datasets should affect other people's choice" (5) to "No usable datasets submitted" (1)

**7. Software** (1-5 scale)
"Enabling: The newly released software should affect other people's choice" (5) to "No usable software released" (1)

**8. Author Identity Knowledge** (1-5 scale)
"I know/can guess at least one author's name" (5) to "I do not have even an educated guess" (1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4572
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-25T22:32:17.145013+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 377.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.5}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 411.5}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metad
…[truncated 12 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3870
}
```

</details>

---

### Tool call

_source line 278 · 2026-05-25T22:32:20.010442+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 279 · 2026-05-25T22:32:20.311852+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool call

_source line 280 · 2026-05-25T22:32:21.422298+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-25T22:32:21.874987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1864
}
```

</details>

---

### Tool result

_source line 282 · 2026-05-25T22:32:21.879652+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1567
}
```

</details>

---

### Tool call

_source line 283 · 2026-05-25T22:32:21.880101+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-25T22:32:22.538831+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool call

_source line 285 · 2026-05-25T22:32:22.942557+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 286 · 2026-05-25T22:32:23.799898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2377
}
```

</details>

---

### Tool call

_source line 287 · 2026-05-25T22:32:23.800388+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool call

_source line 288 · 2026-05-25T22:32:24.053431+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 289 · 2026-05-25T22:32:24.711172+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2831
}
```

</details>

---

### Tool result

_source line 290 · 2026-05-25T22:32:26.222957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3684
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-25T22:32:26.530175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3587
}
```

</details>

---

### Tool result

_source line 292 · 2026-05-25T22:32:26.686163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2632
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-25T22:32:26.988717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3188
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-25T22:39:13.449178+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 实证方法论扎实、实验规模令人信服（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture），但三个 contribution 的原创性均偏弱——RSFT 是已有方法的应用、CED 相对 flat-NLI 提升微乎其微、EDCR 作为诊断指标缺乏充分验证——使论文更适合 Findings 而非主会议。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验覆盖广（3 paradigms × 4 scales × 3 seeds），但 DPO 仅测 β=0.1、GRPO 仅 G=8，核心 claim 的泛化性受限；EDCR 与 CED 共享 NLI backbone 存在循环依赖风险 |\n| Excitement | 3/5 | Evidence tax 的 scale-dependent landscape 是有价值的实证发现，但方法贡献有限：RSFT=STaR+CED 筛选，CED≈flat-NLI，EDCR 是简单比率 |\n| Reproducibility | 4/5 | 详细的超参数（Appendix A/Table 4）、匿名代码发布、3 seed 复现、跨架构验证 |\n| Reviewer Confidence | 4/5 | 熟悉 DocRE、LLM fine-tuning、RL for LLMs 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心新颖性不足以支撑主会议接收\n\n- 具体位置：§1 Contributions, §3.2 (RSFT), §3.3 (CED), §3.5 (EDCR)\n- 问题：\n  1. **RSFT 不是新方法**：论文明确承认 RSFT 建立在 STaR (Zelikman et al., 2022) 之上（§3.3 \"building on Self-Taught Reasoner\"）。其贡献在于将 STaR 应用到 evidence-grounded DocRE 并用 CED 做筛选——这是 engineering contribution 而非 methodological innovation。\n  2. **CED vs flat-NLI 差异微乎其微**：§3.4 末段自己承认 \"the contrastive formulation is not essential for data selection quality\"——mean Rel-F1 差异仅 0.02pp。如果去掉 contrastive 组分，CED 退化为简单的 NLI-based 打分，大幅削弱了 CED 作为独立贡献的地位。\n  3. **EDCR 是简单比率**：公式 (2) 定义 EDCR 为 distractor citation rate，本质上是 1 − precision(evidence|relation)。作为诊断指标，其独立价值需要更强的跨 backbone 验证（见 W2）。\n  4. **Evidence tax 的 framing 有误导性**：§4.4 和 Appendix K (Table 15) 的 error decomposition 表明小模型的 evidence tax 主要来自 truncation（截断）和 duplication（重复），而非 evidence 本身的 harmful effect。这意味着 \"evidence tax\" 本质上是 generation capacity bottleneck 的表现——模型无法可靠地生成足够长的结构化输出——而非 evidence 固有的代价。论文应清晰区分这两种来源。\n\n- 为什么影响接收：EMNLP main 要求 novelty + impact。论文诚实地定位为 empirical study，但三个 contribution 分别是：已有方法的应用、自证微效的组分、简单的诊断比率。核心 empirical finding（evidence tax 的 scale-dependence）如果剥离 truncation 因素后，剩余的 \"genuine evidence interference\" 有多大尚不清楚。\n\n- 建议修改方向：\n  (a) 坦诚降低 CED 的 contribution 权重，将重心放在 evidence tax landscape 的实证发现上\n  (b) 在 evidence tax 分析中明确区分 \"truncation-induced tax\"（随 capacity 自然消失）和 \"information-interference tax\"（extraction-evidence 真正的冲突）——Appendix K 的 error decomposition 已有素材，但未在正文中充分利用\n  (c) 对 EDCR 增加跨 NLI backbone 的稳定性 ablation\n\n**N2** [critical] 优化超参数探索不充分，削弱 decoupling spectrum 的泛化性\n\n- 具体位置：§3.3 (DPO β=0.1), §4.1 (GRPO G=8), Table 1\n- 问题：论文的核心 claim 之一是 \"gradient-based optimization (GRPO, DPO) causes extraction-evidence decoupling while RSFT avoids it\"（§1 Contribution 2, §3.5 验证）。但：\n  - DPO 仅测试了 β=0.1 这一个温度参数。DPO 的 β 直接控制策略偏离 reference policy 的程度——更低的 β（如 0.01）可能产生更保守的更新从而减少 decoupling，更高的 β（如 0.5）可能加剧。\n  - GRPO 仅测试了 G=8（group size）。更大的 G 提供更好的 advantage 估计，可能改善 extraction-evidence coupling。\n  - RSFT 使用 k=1（top-1 selection）。k>1 的效果未探索。\n  - 论文未提供任何超参数敏感性分析来支撑 \"gradient methods inherently decouple\" 这一归因。\n\n- 为什么影响接收：如果 decoupling 程度高度依赖超参数选择（例如特定 β 值恰好导致 extreme decoupling），则 \"decoupling spectrum\" 的方法论归因（Table 1 的定性分类）将从 \"fundamental property of gradient optimization\" 降级为 \"specific hyperparameter regime behavior\"。\n\n- 建议修改方向：至少对 DPO β ∈ {0.01, 0.1, 0.5} 做消融实验；或在正文（而非仅 Limitations）中明确讨论这一限制及其对结论泛化性的影响。\n\n**N3** [critical] Conclusion 过于简短，不符合 EMNLP 论文标准\n\n- 具体位置：Section 5, page 8（约 3 句话，~60 words）\n- 问题：Conclusion 完全未讨论：\n  - **Broader implications**：evidence tax 对 LLM-based IE 系统设计的启示——什么时候应该要求模型生成 evidence？\n  - **Future directions**：如何在更大规模（70B+）/ 更多 IE 任务（事件抽取、NER）上验证 evidence tax 现象？\n  - **Connection to wider literature**：gradient pressure vs discrete selection 的二分法是否适用于其他 structured generation 任务（如 code generation with explanations、math with proofs）？\n- 为什么影响接收：对于 empirical study，Conclusion 是 reviewer 形成对工作意义整体判断的关键段落。3 句话的 Conclusion 传递出 \"作者未充分思考工作 significance\" 的信号。\n- 建议修改方向：扩展至 8-12 句话，覆盖 key takeaways、implications for practitioners、和 future work。仍可保持在 8 页内（当前 page 8 有空间）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work 遗漏 multi-task learning / gradient conflict 文献\n\n- 具体位置：§2.1, §2.2\n- 问题：论文的核心发现是 gradient-based 优化导致 extraction 和 evidence 两个子任务 decouple。这本质上是 multi-task learning 中的 **negative transfer / gradient conflict** 问题，但论文仅在 §2.1 末尾简单提及 Ruder (2017)，缺少高度相关的文献：\n  - PCGrad (Yu et al., 2020, NeurIPS)：\"Gradient Surgery for Multi-Task Learning\"——直接处理 multi-task gradient conflict\n  - Reward overoptimization (Gao et al., 2023)：\"Scaling Laws for Reward Model Overoptimization\"——GRPO 的 catastrophic decoupling 可能与 reward hacking 相关\n  - 这些方法可能提供解决 decoupling 的替代路径（如对 extraction 和 evidence sub-objectives 分别计算 gradient 并做 projection），论文未讨论。\n- 建议：增加一段讨论 multi-task gradient conflict 文献，说明为什么这些方法在当前 setting 中不直接适用（或值得未来探索）。\n\n**W2** [warning] EDCR 与 CED 共享 NLI backbone，存在 circular dependency 风险\n\n- 具体位置：§3.4 CED definition (Equation 1), §3.5 EDCR definition (Equation 2)\n- 问题：CED 使用 DeBERTa-v3 NLI 模型对候选输出评分（用于 RSFT 数据筛选）；EDCR 同样基于 NLI 判断 cited evidence 是否为 distractor。两者共享相同的 NLI backbone。因此：\n  - EDCR 与 Rel-F1 的负相关（ρ=−0.79, §3.5）可能部分反映 NLI 模型的系统偏差\n  - 论文声称 EDCR \"independent of Evi-F1\"（ρ=−0.06），但这种独立性可能是 NLI 评估维度选择的产物\n  - 论文在 Appendix L 做了 partial correlation controlling for TP，但未做跨 NLI backbone 的稳定性验证\n- 建议：用至少一个替代 NLI 模型（如 RoBERTa-large-MNLI 或更新的模型）重新计算 EDCR，报告跨 backbone 的 rank correlation 稳定性。\n\n**W3** [warning] §4.4 信息密度过高，关键发现容易被忽略\n\n- 具体位置：§4.4 (pages 6-7)，约 1.5 页内覆盖 scaling pattern、variance analysis、cross-architecture validation、RSFT scaling behavior\n- 问题：密集堆积了大量数字（\"variance compression 32.6× at 1.7B, 7.5× at 4B, 6.5× at 8B\"、多个 Spearman ρ 值、confidence intervals、跨架构结果），读者难以区分 primary findings 和 supporting evidence。最重要的发现——evidence tax 的 scale-dependent reversal——淹没在统计细节中。\n- 建议：拆分为 \"4.4 Evidence Tax across Scales\" 和 \"4.5 Robustness and Variance\"，使用小标题组织各子发现。\n\n**W4** [warning] \"Evidence tax\" 术语 framing 与实际数据不完全匹配\n\n- 具体位置：Abstract (lines 8-11), §1 (page 2), §4.4 (page 6-7), Table 9 (page 13)\n- 问题：\n  - \"Tax\" 一词天然暗示 cost/负面效应，但实验显示 1.7B 时 evidence 实际是 **benefit**（tax < 0，即 −5.63pp）\n  - 论文用 sign convention \"positive = cost, negative = benefit\" 来化解，但这在直觉上反直觉——\"negative tax\" = benefit 不是自然的语义映射\n  - Figure 6 展示的是 Ign-F1 bar heights（非 tax 值本身），需要读者自行计算差值\n- 建议：考虑使用更中性的术语如 \"evidence delta\" 或 \"evidence impact\"，或至少在 Figure 6 中直接展示 tax 值（差值）而非原始 F1 分数。\n\n**W5** [warning] Re-DocRED test set ~20pp performance drop 的解释不充分\n\n- 具体位置：§4.6 (page 8), Table 10 (page 15)\n- 问题：Re-DocRED test 比 dev 低约 20pp，论文归因于 annotation density 差异（test 3.47 triples/doc vs dev 12.3）。但：\n  - 20pp 是极大的 gap——如果纯粹是 annotation density 导致，是否意味着模型在 sparse-annotation 场景下基本失效？\n  - 是否有 domain/entity distribution 差异的贡献？\n  - 这对论文 claim 的泛化性有什么影响？（如 evidence tax 在 sparse-annotation setting 下是否仍然成立？）\n- 建议：增加按 annotation density 分层的分析，或在 Limitations 中更详细讨论。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 caption 中 CED 和 EDCR 缩写首次出现未展开全称，需要读者回溯到 §3.4-3.5。建议在 caption 中加注全称。\n- **M2**: \"co-optimization\" 和 \"joint optimization\" 在正文中交替使用，建议统一术语。\n- **M3**: Appendix E (Controlled Evaluation Subset) 包含重要方法论信息（matched@2048 fair evaluation 的定义），这对理解 evidence tax 至关重要，考虑将核心定义移入正文或至少在正文中更明确地引用。\n- **M4**: Figure 4 的 dual y-axis（Rel-F1 和 Evi-F1）如果量级差异大，可能产生视觉误导。建议明确标注刻度或使用 normalized 展示。\n\n---\n\n## Missing References\n\n1. **Multi-task gradient conflict**: Yu et al. (2020, NeurIPS) \"Gradient Surgery for Multi-Task Learning\" — 直接相关于 extraction-evidence decoupling 的 gradient-level 解释和潜在解决方案\n2. **Reward overoptimization**: Gao et al. (2023) \"Scaling Laws for Reward Model Overoptimization\" — GRPO 的 catastrophic decoupling 可能是 reward hacking 的 structured-generation 实例\n3. **Faithfulness in generation**: Maynez et al. (2020, ACL) \"On Faithfulness and Factuality in Abstractive Summarization\" — evidence faithfulness 在 NLG 中的理论基础\n4. **Attribution measurement**: Rashkin et al. (2023, TACL) \"Measuring Attribution in Natural Language Generation Models\" — 与 EDCR 的 attribution-measurement 动机高度相关\n\n---\n\n## 主要优势\n\n1. **实验规模在 empirical study 中属高水平**：3 optimization paradigms × 4 model scales (1.7B, 4B, 8B, 14B) × 3 random seeds × 2 datasets (DocRED, Re-DocRED) × cross-architecture (Qwen2.5 + LLaMA-3.1)，实验矩阵覆盖全面\n2. **研究问题定义清晰**：evidence-grounded DocRE 中 extraction-evidence trade-off 的研究动机有真实痛点——当前 LLM-based 方法无法同时优化 extraction accuracy 和 evidence faithfulness\n3. **EDCR 的 per-relation 诊断价值**：Appendix L (Figure 8) 展示了 per-relation EDCR distribution，揭示了 aggregate metrics 不可见的 pattern——高 EDCR relations 倾向于需要 multi-hop 或 cross-sentence reasoning\n4. **Error decomposition 分析有深度**：Appendix K (Table 15) 将 RSFT 改进分解为 truncation reduction、hallucination reduction、duplication elimination 三个维度，为方法选择提供了 actionable 指导\n5. **Cross-architecture 泛化一致性强**：LLaMA-3.1-8B 与 Qwen2.5-8B 在 evidence tax pattern、RSFT gain、EDCR 趋势上均一致（Table 3, Appendix H）\n6. **Qualitative analysis 信息量高**：Appendix M 的三个 case study（evidence quality、GRPO format gaming、EDCR diagnostics）直观地支撑了定量发现\n\n---\n\n## Questions for Authors\n\nQ1: 如果用 RoBERTa-large-MNLI 替换 DeBERTa-v3 作为 EDCR 的 NLI backbone，EDCR 与 Rel-F1 的 correlation 是否稳定？这是验证 EDCR 作为 NLI-backbone-agnostic 诊断指标的关键实验。\n\nQ2: Evidence tax 在 Appendix K 分解后，truncation 贡献了多大比例？具体来说，如果只看 non-truncated outputs，1.7B 的 evidence tax 是否仍然存在？\n\nQ3: DPO β=0.01 和 β=0.5 下的 EDCR 是否仍显示 catastrophic decoupling？如果 β 影响大，Table 1 的定性分类需要附加条件。\n\nQ4: RSFT 在 k>1（如 top-3 selection）时表现如何？当前 k=1 可能过于 aggressive，更多候选可能提供 diversity 收益。\n\nQ5: 论文如何解释 14B 的 cross-seed variance 异常高（Appendix D, Table 7）——这是否暗示 evidence tax 在更大规模上不稳定？",
  "reviewer_id": "2",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 实证方法论扎实、实验规模令人信服（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture），但三个 contribution 的原创性均偏弱——RSFT 是已有方法的应用、CED 相对 flat-NLI 提升微乎其微、EDCR 作为诊断指标缺乏充分验证——使论文更适合 Findings 而非主会议。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验覆盖广（3 paradigms × 4 scales × 3 seeds），但 DPO 仅测 β=0.1、GRPO 仅 G=8，核心 claim 的泛化性受限；EDCR 与 CED 共享 NLI backbone 存在循环依赖风险 |\n| Excitement | 3/5 | Evidence tax 的 scale-dependent landscape 是有价值的实证发现，但方法贡献有限：RSFT=STaR+CED 筛选，CED≈flat-NLI，EDCR 是简单比率 |\n| Reproducibility | 4/5 | 详细的超参数（Appendix A/Table 4）、匿名代码发布、3 seed 复现、跨架构验证 |\n| Reviewer Confidence | 4/5 | 熟悉 DocRE、LLM fine-tuning、RL for LLMs 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心新颖性不足以支撑主会议接收\n\n- 具体位置：§1 Contributions, §3.2 (RSFT), §3.3 (CED), §3.5 (EDCR)\n- 问题：\n  1. **RSFT 不是新方法**：论文明确承认 RSFT 建立在 STaR (Zelikman et al., 2022) 之上（§3.3 \"building on Self-Taught Reasoner\"）。其贡献在于将 STaR 应用到 evidence-grounded DocRE 并用 CED 做筛选——这是 engineering contribution 而非 methodological innovation。\n  2. **CED vs flat-NLI 差异微乎其微**：§3.4 末段自己承认 \"the contrastive formulation is not essential for data selection quality\"——mean Rel-F1 差异仅 0.02pp。如果去掉 contrastive 组分，CED 退化为简单的 NLI-based 打分，大幅削弱了 CED 作为独立贡献的地位。\n  3. **EDCR 是简单比率**：公式 (2) 定义 EDCR 为 distractor citation rate，本质上是 1 − precision(evidence|relation)。作为诊断指标，其独立价值需要更强的跨 backbone 验证（见 W2）。\n  4. **Evidence tax 的 framing 有误导性**：§4.4 和 Appendix K (Table 15) 的 error decomposition 表明小模型的 evidence tax 主要来自 truncation（截断）和 duplication（重复），而非 evidence 本身的 harmful effect。这意味着 \"evidence tax\" 本质上是 generation capacity bottleneck 的表现——模型无法可靠地生成足够长的结构化输出——而非 evidence 固有的代价。论文应清晰区分这两种来源。\n\n- 为什么影响接收：EMNLP main 要求 novelty + impact。论文诚实地定位为 empirical study，但三个 contribution 分别是：已有方法的应用、自证微效的组分、简单的诊断比率。核心 empirical finding（evidence tax 的 scale-dependence）如果剥离 truncation 因素后，剩余的 \"genuine evidence interference\" 有多大尚不清楚。\n\n- 建议修改方向：\n  (a) 坦诚降低 CED 的 contribution 权重，将重心放在 evidence tax landscape 的实证发现上\n  (b) 在 evidence tax 分析中明确区分 \"truncation-induced tax\"（随 capacity 自然消失）和 \"information-interference tax\"（extraction-evidence 真正的冲突）——Appendix K 的 error decomposition 已有素材，但未在正文中充分利用\n  (c) 对 EDCR 增加跨 NLI backbone 的稳定性 ablation\n\n**N2** [critical] 优化超参数探索不充分，削弱 decoupling spectrum 的泛化性\n\n- 具体位置：§3.3 (DPO β=0.1), §4.1 (GRPO G=8), Table 1\n- 问题：论文的核心 claim 之一是 \"gradient-based optimization (GRPO, DPO) causes extraction-evidence decoupling while RSFT avoids it\"（§1 Contribution 2, §3.5 验证）。但：\n  - DPO 仅测试了 β=0.1 这一个温度参数。DPO 的 β 直接控制策略偏离 reference policy 的程度——更低的 β（如 0.01）可能产生更保守的更新从而减少 decoupling，更高的 β（如 0.5）可能加剧。\n  - GRPO 仅测试了 G=8（group size）。更大的 G 提供更好的 advantage 估计，可能改善 extraction-evidence coupling。\n  - RSFT 使用 k=1（top-1 selection）。k>1 的效果未探索。\n  - 论文未提供任何超参数敏感性分析来支撑 \"gradient methods inherently decouple\" 这一归因。\n\n- 为什么影响接收：如果 decoupling 程度高度依赖超参数选择（例如特定 β 值恰好导致 extreme decoupling），则 \"decoupling spectrum\" 的方法论归因（Table 1 的定性分类）将从 \"fundamental property of gradient optimization\" 降级为 \"specific hyperparameter regime behavior\"。\n\n- 建议修改方向：至少对 DPO β ∈ {0.01, 0.1, 0.5} 做消融实验；或在正文（而非仅 Limitations）中明确讨论这一限制及其对结论泛化性的影响。\n\n**N3** [critical] Conclusion 过于简短，不符合 EMNLP 论文标准\n\n- 具体位置：Section 5, page 8（约 3 句话，~60 words）\n- 问题：Conclusion 完全未讨论：\n  - **Broader implications**：evidence tax 对 LLM-based IE 系统设计的启示——什么时候应该要求模型生成 evidence？\n  - **Future directions**：如何在更大规模（70B+）/ 更多 IE 任务（事件抽取、NER）上验证 evidence tax 现象？\n  - **Connection to wider literature**：gradient pressure vs discrete selection 的二分法是否适用于其他 structured generation 任务（如 code generation with explanations、math with proofs）？\n- 为什么影响接收：对于 empirical study，Conclusion 是 reviewer 形成对工作意义整体判断的关键段落。3 句话的 Conclusion 传递出 \"作者未充分思考工作 significance\" 的信号。\n- 建议修改方向：扩展至 8-12 句话，覆盖 key takeaways、implications for practitioners、和 future work。仍可保持在 8 页内（当前 page 8 有空间）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work 遗漏 multi-task learning / gradient conflict 文献\n\n- 具体位置：§2.1, §2.2\n- 问题：论文的核心发现是 gradient-based 优化导致 extraction 和 evidence 两个子任务 decouple。这本质上是 multi-task learning 中的 **negative transfer / gradient conflict** 问题，但论文仅在 §2.1 末尾简单提及 Ruder (2017)，缺少高度相关的文献：\n  - PCGrad (Yu et al., 2020, NeurIPS)：\"Gradient Surgery for Multi-Task Learning\"——直接处理 multi-task gradient conflict\n  - Reward overoptimization (Gao et al., 2023)：\"Scaling Laws for Reward Model Overoptimization\"——GRPO 的 catastrophic decoupling 可能与 reward hacking 相关\n  - 这些方法可能提供解决 decoupling 的替代路径（如对 extraction 和 evidence sub-objectives 分别计算 gradient 并做 projection），论文未讨论。\n- 建议：增加一段讨论 multi-task gradient conflict 文献，说明为什么这些方法在当前 setting 中不直接适用（或值得未来探索）。\n\n**W2** [warning] EDCR 与 CED 共享 NLI backbone，存在 circular dependency 风险\n\n- 具体位置：§3.4 CED definition (Equation 1), §3.5 EDCR definition (Equation 2)\n- 问题：CED 使用 DeBERTa-v3 NLI 模型对候选输出评分（用于 RSFT 数据筛选）；EDCR 同样基于 NLI 判断 cited evidence 是否为 distractor。两者共享相同的 NLI backbone。因此：\n  - EDCR 与 Rel-F1 的负相关（ρ=−0.79, §3.5）可能部分反映 NLI 模型的系统偏差\n  - 论文声称 EDCR \"independent of Evi-F1\"（ρ=−0.06），但这种独立性可能是 NLI 评估维度选择的产物\n  - 论文在 Appendix L 做了 partial correlation controlling for TP，但未做跨 NLI backbone 的稳定性验证\n- 建议：用至少一个替代 NLI 模型（如 RoBERTa-large-MNLI 或更新的模型）重新计算 EDCR，报告跨 backbone 的 rank correlation 稳定性。\n\n**W3** [warning] §4.4 信息密度过高，关键发现容易被忽略\n\n- 具体位置：§4.4 (pages 6-7)，约 1.5 页内覆盖 scaling pattern、variance analysis、cross-architecture validation、RSFT scaling behavior\n- 问题：密集堆积了大量数字（\"variance compression 32.6× at 1.7B, 7.5× at 4B, 6.5× at 8B\"、多个 Spearman ρ 值、confidence intervals、跨架构结果），读者难以区分 primary findings 和 supporting evidence。最重要的发现——evidence tax 的 scale-dependent reversal——淹没在统计细节中。\n- 建议：拆分为 \"4.4 Evidence Tax across Scales\" 和 \"4.5 Robustness and Variance\"，使用小标题组织各子发现。\n\n**W4** [warning] \"Evidence tax\" 术语 framing 与实际数据不完全匹配\n\n- 具体位置：Abstract (lines 8-11), §1 (page 2), §4.4 (page 6-7), Table 9 (page 13)\n- 问题：\n  - \"Tax\" 一词天然暗示 cost/负面效应，但实验显示 1.7B 时 evidence 实际是 **benefit**（tax < 0，即 −5.63pp）\n  - 论文用 sign convention \"positive = cost, negative = benefit\" 来化解，但这在直觉上反直觉——\"negative tax\" = benefit 不是自然的语义映射\n  - Figure 6 展示的是 Ign-F1 bar heights（非 tax 值本身），需要读者自行计算差值\n- 建议：考虑使用更中性的术语如 \"evidence delta\" 或 \"evidence impact\"，或至少在 Figure 6 中直接展示 tax 值（差值）而非原始 F1 分数。\n\n**W5** [warning] Re-DocRED test set ~20pp performance drop 的解释不充分\n\n- 具体位置：§4.6 (page 8), Table 10 (page 15)\n- 问题：Re-DocRED test 比 dev 低约 20pp，论文归因于 annotation density 差异（test 3.47 triples/doc vs dev 12.3）。但：\n  - 20pp 是极大的 gap——如果纯粹是 annotation density 导致，是否意味着模型在 sparse-annotation 场景下基本失效？\n  - 是否有 domain/entity distribution 差异的贡献？\n  - 这对论文 claim 的泛化性有什么影响？（如 evidence tax 在 sparse-annotation setting 下是否仍然成立？）\n- 建议：增加按 annotation density 分层的分析，或在 Limitations 中更详细讨论。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 caption 中 CED 和 EDCR 缩写首次出现未展开全称，需要读者回溯到 §3.4-3.5。建议在 caption 中加注全称。\n- **M2**: \"co-optimization\" 和 \"joint optimization\" 在正文中交替使用，建议统一术语。\n- **M3**: Appendix E (Controlled Evaluation Subset) 包含重要方法论信息（matched@2048 fair evaluation 的定义），这对理解 evidence tax 至关重要，考虑将核心定义移入正文或至少在正文中更明确地引用。\n- **M4**: Figure 4 的 dual y-axis（Rel-F1 和 Evi-F1）如果量级差异大，可能产生视觉误导。建议明确标注刻度或使用 normalized 展示。\n\n---\n\n## Missing References\n\n1. **Multi-task gradient conflict**: Yu et al. (2020, NeurIPS) \"Gradient Surgery for Multi-Task Learning\" — 直接相关于 extraction-evidence decoupling 的 gradient-level 解释和潜在解决方案\n2. **Reward overoptimization**: Gao et al. (2023) \"Scaling Laws for Reward Model Overoptimization\" — GRPO 的 catastrophic decoupling 可能是 reward hacking 的 structured-generation 实例\n3. **Faithfulness in generation**: Maynez et al. (2020, ACL) \"On Faithfulness and Factuality in Abstractive Summarization\" — evidence faithfulness 在 NLG 中的理论基础\n4. **Attribution measurement**: Rashkin et al. (2023, TACL) \"Measuring Attribution in Natural Language Generation Models\" — 与 EDCR 的 attribution-measurement 动机高度相关\n\n---\n\n## 主要优势\n\n1. **实验规模在 empirical study 中属高水平**：3 optimization paradigms × 4 model scales (1.7B, 4B, 8B, 14B) × 3 random seeds × 2 datasets (DocRED, Re-DocRED) × cross-architecture (Qwen2.5 + LLaMA-3.1)，实验矩阵覆盖全面\n2. **研究问题定义清晰**：evidence-grounded DocRE 中 extraction-evidence trade-off 的研究动机有真实痛点——当前 LLM-based 方法无法同时优化 extraction accuracy 和 evidence faithfulness\n3. **EDCR 的 per-relation 诊断价值**：Appendix L (Figure 8) 展示了 per-relation EDCR distribution，揭示了 aggregate metrics 不可见的 pattern——高 EDCR relations 倾向于需要 multi-hop 或 cross-sentence reasoning\n4. **Error decomposition 分析有深度**：Appendix K (Table 15) 将 RSFT 改进分解为 truncation reduction、hallucination reduction、duplication elimination 三个维度，为方法选择提供了 actionable 指导\n5. **Cross-architecture 泛化一致性强**：LLaMA-3.1-8B 与 Qwen2.5-8B 在 evidence tax pattern、RSFT gain、EDCR 趋势上均一致（Table 3, Appendix H）\n6. **Qualitative analysis 信息量高**：Appendix M 的三个 case study（evidence quality、GRPO format gaming、EDCR diagnostics）直观地支撑了定量发现\n\n---\n\n## Questions for Authors\n\nQ1: 如果用 RoBERTa-large-MNLI 替换 DeBERTa-v3 作为 EDCR 的 NLI backbone，EDCR 与 Rel-F1 的 correlation 是否稳定？这是验证 EDCR 作为 NLI-backbone-agnostic 诊断指标的关键实验。\n\nQ2: Evidence tax 在 Appendix K 分解后，truncation 贡献了多大比例？具体来说，如果只看 non-truncated outputs，1.7B 的 evidence tax 是否仍然存在？\n\nQ3: DPO β=0.01 和 β=0.5 下的 EDCR 是否仍显示 catastrophic decoupling？如果 β 影响大，Table 1 的定性分类需要附加条件。\n\nQ4: RSFT 在 k>1（如 top-3 selection）时表现如何？当前 k=1 可能过于 aggressive，更多候选可能提供 diversity 收益。\n\nQ5: 论文如何解释 14B 的 cross-seed variance 异常高（Appendix D, Table 7）——这是否暗示 evidence tax 在更大规模上不稳定？",
    "reviewer_id": "2",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-25T22:39:17.266556+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3817
}
```

</details>

---

### Tool call

_source line 296 · 2026-05-25T22:39:21.489961+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
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

_source line 297 · 2026-05-25T22:39:21.540582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 298 · 2026-05-25T22:39:31.183615+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 299 · 2026-05-25T22:39:31.535316+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 351
}
```

</details>

---

### Assistant

_source line 300 · 2026-05-25T22:39:45.034442+00:00_

审稿意见已提交给 Review Director。

**总结**：Overall 3.5/5 (Borderline Conference)。实验规模在 empirical study 中属高水平（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture），但三个 Must-Fix 问题影响接收决定：

1. **N1 核心新颖性不足**——RSFT=STaR 应用、CED≈flat-NLI（仅差 0.02pp）、EDCR 是简单比率；且 evidence tax 在小模型上主要由 truncation 驱动（Appendix K），"tax" framing 有误导性
2. **N2 超参数探索不充分**——DPO 仅 β=0.1、GRPO 仅 G=8，decoupling 可能是特定超参数 regime 的行为而非 gradient optimization 的固有性质
3. **N3 Conclusion 仅 ~60 words**——缺少 broader implications 和 future directions

五个 Should-Fix（related work 遗漏 gradient conflict 文献、EDCR-CED circular dependency、§4.4 信息过载、terminology framing、Re-DocRED 20pp drop 解释不足）和四条 Missing References 一并列出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---

## Round 8

4 recorded events

### User

_source line 301 · 2026-05-25T22:40:08.794678+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见

**Overall: 3.5 (Borderline Conference)**
**Soundness: 3.0/5 | Excitement: 3.5/5 | Reproducibility: 4/5 | Confidence: 4/5**

### 主要优势
S1. 研究问题定义精准，实用价值高。
S2. EDCR 指标设计巧妙且验证充分（partial correlation 仅降 0.15%，permutation test p<0.0001，per-relation n=76 ρ=-0.79）。
S3. 三范式系统对比框架有参考价值（GRPO/DPO/RSFT 统一 baseline 和评估协议）。
S4. 跨模型家族和跨规模验证增强可推广性。
S5. 附录质量高（14 个附录覆盖消融、统计、error decomposition、定性分析）。

### Must-Fix
**N1** [critical] n=3 seeds 统计效力不足——sign test p=0.0625 不显著，CI 跨零，1.7B s42 是最强 seed (+3.22pp above mean) 有 disproportionate influence。建议增加 seeds 或弱化 claim 语言。

**N2** [critical] GRPO QLoRA vs bf16 存在 lr-quantization confound——lr、batch size 可能不同，collapse 可能是 lr 过大 + quantization 联合效应。bf16 G=4 补充实验仅控制 group size，未控制 lr。

**N3** [critical] DPO 仅 β=0.1，"spectrum" 结论缺乏支撑——不同 β 下行为可能截然不同（β=0.5 可能更接近 RSFT，β=0.01 可能更接近 GRPO collapse）。

### Should-Fix
**W1** CED contrastive 设计附加价值不明确（vs flat-NLI 仅 0.02pp）。
**W2** 14B 仅 1 seed SFT baseline，scaling claim 不可靠。
**W3** RSFT 共享 SFT checkpoint 导致方差比较不公平（SFT = full randomness, RSFT = fixed-base）。
**W4** Test-set evidence tax 在 8B 出现反转（dev +0.04pp → test -1.17pp），解释不充分。

### Minor
M1: Abstract 首句缺引用。M2: Figure 4 y轴字号。M3: §2.3 标题误导。M4: RSFT mechanistic explanation 应在 future work 突出。

### Questions
Q1: EDCR 仅在 TP triples 上计算的变体结果？
Q2: 是否测过 RoBERTa-large-MNLI 或 prompt-based NLI？
Q3: RSFT k>1 效果？（k=3 已在 Appendix B 测试，Ign-F1 下降 1.02pp）
Q4: DPO 用 Evi-F1 而非 CED 构造 preference pairs 的 decoupling 行为？

### Missing References
- Xu et al. (2024) "Towards Faithful Document-Level Relation Extraction"
- DPO β sensitivity 相关文献

---

请逐条回应以上每个要点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 302 · 2026-05-25T22:42:20.716539+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### 主要优势\n\n[AGREE] R1-S1: 研究问题定义精准。Evidence-grounded DocRE 中 extraction-evidence trade-off 确实是一个有实际意义的研究空缺。\n\n[AGREE] R1-S2: EDCR 验证充分。我在自己的审稿中也肯定了 EDCR 的 per-relation 诊断价值（Appendix L, Figure 8）。但我同时指出了 EDCR 与 CED 共享 NLI backbone 的 circular dependency 风险——R1 未提及此点（见我的 W2）。partial correlation 控制了 TP 但未控制 NLI backbone bias。\n\n[AGREE] R1-S3: 三范式统一对比框架确实有参考价值。Table 1 的定性分类清晰，统一了 baseline（共享 SFT checkpoint）和评估协议。\n\n[AGREE] R1-S4: 跨架构验证（Qwen2.5 + LLaMA-3.1-8B）增强可推广性。我在自己的优势部分也特别肯定了这一点。\n\n[AGREE] R1-S5: 附录质量高。14 个 appendix sections 涵盖面广，尤其 Appendix K (error decomposition) 和 Appendix M (qualitative analysis) 信息量高。\n\n---\n\n### Must-Fix\n\n[AGREE] R1-N1: n=3 seeds 统计效力不足\n\n同意这是关键方法论弱点。补充以下证据：\n\n1. **Appendix D (Table 7)** 的 95% CI 确实跨零：论文自己报告了置信区间。当 CI 跨零时，evidence tax 的方向性 claim 在统计上不显著。\n2. **我的补充关注**：不仅是 1.7B 的 s42 issue——14B 的 cross-seed variance 也异常高（Table 7 显示 14B CI 更宽），暗示 evidence tax 在更大规模上可能不稳定。\n3. **与 R1 的分歧**：R1 建议\"增加 seeds 或弱化 claim 语言\"。我认为增加 seeds 是理想方案但可能不现实（14B 训练成本高）；更可行的是在正文 §4.4 中用 hedging language 替代当前的断言式表述（如 \"the evidence tax reverses\" → \"our 3-seed estimates suggest the evidence tax may reverse\"）。\n\n[AGREE] R1-N2: GRPO QLoRA vs bf16 confound\n\n同意存在实验混淆。具体证据：\n\n1. **Table 4 (Appendix A)** 显示 GRPO 使用 QLoRA 4-bit quantization + r=64，而 SFT/RSFT 使用 full-precision LoRA。这不是 controlled comparison——quantization 本身可能影响 gradient landscape 的稳定性。\n2. **bf16 G=4 实验的局限**：论文在 Table 14 (Appendix) 提供了 bf16 补充实验，但 R1 正确指出它控制了 group size 而未控制 lr。GRPO collapse 可能是 lr × quantization 的交互效应，而非 GRPO 范式固有的 decoupling。\n3. **我的补充**：不过，DPO 也展示了 substantial decoupling（Table 2: Rel-F1 drops 33-37%，§4.2），且 DPO 使用 offline 数据无需 online sampling——这意味着 gradient-based optimization 导致 decoupling 的 claim 不完全依赖于 GRPO 的 QLoRA 设置。GRPO collapse 的 severity 可能被 confound 放大，但 decoupling 方向性可能仍成立。\n\n[AGREE] R1-N3: DPO β=0.1 单点实验\n\n完全同意，这也是我自己 Must-Fix N2 的核心观点。补充：\n\n1. DPO 的 β 直接控制 KL constraint 强度。β=0.1 是较小的值（弱约束），允许策略大幅偏离 reference——这可能 maximize decoupling。β=0.5 或 β=1.0 可能产生更保守的行为，减轻 decoupling。\n2. 论文的 \"decoupling spectrum\"（Table 1）将 DPO 定性归类为 \"Partial decoupling\"——但这个归类完全基于 β=0.1 的单点观测。如果 β=0.5 下 DPO 表现更像 RSFT（低 decoupling），Table 1 的框架就需要重大修正。\n3. **与 R1 一致**：R1 说 \"β=0.01 可能更接近 GRPO collapse\"——这是合理推测。低 β 意味着几乎无 KL 约束，策略可以任意偏移，更容易 exploit reward 导致 decoupling。\n\n---\n\n### Should-Fix\n\n[AGREE] R1-W1: CED contrastive 设计附加价值不明确\n\n完全同意。我在 Must-Fix N1 中将此列为核心新颖性不足的证据之一。§3.4 末段自己承认 \"the contrastive formulation is not essential\"——0.02pp 的差异在 3-seed variance 范围内不显著。CED 作为独立 contribution 不成立。\n\n[AGREE] R1-W2: 14B 仅 1 seed SFT baseline\n\n同意。14B 数据点对 scaling claim 至关重要（是最大规模），但只有 1 seed 的 SFT baseline 使得 evidence tax 的 estimation 在该规模上不可靠。Table 3 的 14B 行应标注 \"single seed\" 的 caveat。论文在 Table 3 脚注提到 \"14B shows dev-set sign reversal\"，但对 single-seed limitation 不够显眼。\n\n[REBUT] R1-W3: RSFT 共享 SFT checkpoint 导致方差比较不公平\n\n部分反驳。R1 的观点是：SFT 方差来自 full training randomness，RSFT 方差仅来自 post-SFT 阶段，两者不可比。但我认为这个比较有其合理性：\n\n1. **论文的 variance comparison 回答的是实际部署问题**：practitioners 关心的是 \"从头训练一个 SFT model\" vs \"从头训练 SFT 然后做 RSFT\" 的 end-to-end variance。后者包含 SFT 阶段的 randomness（论文用 3 个不同 SFT seed 初始化 RSFT），所以 RSFT 的 variance 确实包含了 SFT 阶段的变异。\n2. **但 R1 的核心关注仍然有效**：Table 7 (Appendix D) 的 variance compression ratio 可能被夸大——如果 RSFT 从 **同一个** SFT checkpoint 出发（论文在 §3.2 说 \"shared SFT initialization\"），那么 RSFT 的 cross-seed variance 确实不含 SFT 初始化 randomness。这是一个 **重要澄清点**：论文需要明确说明 RSFT 的 3 个 seeds 是 3 个不同 SFT seeds → 各自 RSFT，还是 1 个 SFT seed → 3 个 RSFT runs。\n3. **我的判断**：从 §4.4 \"RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B...\" 的措辞看，RSFT 的 3 seeds 似乎来自 **同一个** SFT checkpoint。如果如此，R1 的 concern 完全成立——variance compression ratio 被人为缩小，因为 RSFT 未经历 SFT 阶段的 randomness。建议论文补充 \"3 different SFT checkpoints → RSFT\" 的 variance 数据。\n\n[AGREE] R1-W4: Test-set evidence tax 在 8B 反转\n\n同意需要更好解释。我在自己的 W5 中也提出了类似关注（Re-DocRED test 20pp drop）。具体补充：\n\n1. Dev +0.04pp → test −1.17pp 的 sign reversal 在 n=3 seeds、CI 跨零的前提下（R1-N1），实际上 neither 方向是统计显著的。\n2. 但论文 §4.4 的叙述语气暗示 dev 和 test 的 pattern 是一致的——8B 的反转挑战了这一叙述。\n3. 可能解释：test set 的 entity/relation distribution 与 dev 不同，evidence 在某些 relation types 上更 costly。Appendix L 的 per-relation EDCR 分析如果能在 test set 上复现，可以 shed light。\n\n---\n\n### Minor\n\n[AGREE] R1-M1: Abstract 首句 \"surpasses encoder baselines\" 缺引用。应 cite 至少一个 LLM-based DocRE 工作（如 AutoRE 或 ReFiRE）来 substantiate。\n\n[AGREE] R1-M2: Figure 4 y-axis 字号偏小，在打印版本中可能难以辨认。\n\n[REBUT] R1-M3: §2.3 标题 \"Evidence Faithfulness and Rejection Sampling\" 不算误导。该 section 确实同时覆盖了 NLI-based faithfulness 评估方法（Laban et al., 2022; Zhang et al., 2024）和 rejection sampling/self-improvement 方法（STaR, DeepSeek-R1），并论述了两者的理论连接——RSFT 正是将 faithfulness evaluation 作为 rejection criterion。标题反映了 section 的两个主题及其连接。不过，为清晰起见，可改为 \"Evidence Faithfulness Evaluation and Rejection-Based Training\"。\n\n[AGREE] R1-M4: RSFT mechanistic explanation（当前在 Limitations 末段）应在 future work 中更突出。Limitations 提到 \"we have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit regularization through candidate diversity, or from both\"——这是一个值得独立段落讨论的 open question。\n\n---\n\n### Questions\n\nR1-Q1 (EDCR on TP-only triples): 有价值的诊断问题。当前 EDCR 在 all predicted triples 上计算（包含 FP triples），TP-only variant 可以隔离 \"evidence quality for correct predictions\" vs \"evidence quality overall\"。论文 Appendix L 的 partial correlation 部分控制了 TP，但未直接报告 TP-only EDCR 值。\n\nR1-Q2 (替代 NLI 模型): 这与我的 W2 (EDCR-CED circular dependency) 直接相关。我强烈支持此问题——跨 NLI backbone 验证是 EDCR 作为 robust 诊断指标的必要条件。\n\nR1-Q3 (RSFT k>1): R1 自己已注意到 Appendix B 报告了 k=3 结果（Ign-F1 下降 1.02pp）。这说明 top-1 selection 是 RSFT 性能的关键——更 aggressive 的筛选反而更好。这个结果支持了 RSFT \"quality over quantity\" 的设计哲学。\n\nR1-Q4 (DPO with Evi-F1 scoring): 有趣的实验设计问题。如果 DPO 用 Evi-F1（而非 CED）构造 preference pairs，reward signal 更直接 align with evidence quality，decoupling 可能减轻——这可以测试 \"DPO decoupling 是范式固有问题 vs reward signal 设计问题\"。\n\n---\n\n### Missing References\n\n[AGREE] Xu et al. (2024) \"Towards Faithful Document-Level Relation Extraction\": 标题直接相关，如果确实发表且未被引用，是显著遗漏。\n\n[AGREE] DPO β sensitivity 文献: 结合 R1-N3 和我的 N2，DPO 超参数敏感性的 prior work（如 Tunstall et al. 2023 的 DPO 消融）应被讨论。\n\n---\n\n### 综合评价\n\nR1 和 R2（本人）的审稿意见高度一致：\n\n**共识点**: (1) n=3 seeds 统计效力不足；(2) DPO β 单点实验削弱 decoupling spectrum claim；(3) CED vs flat-NLI 差异微乎其微；(4) 实验规模和附录质量高。\n\n**R2 补充的 R1 未覆盖的关键问题**: (1) EDCR-CED 共享 NLI backbone 的 circular dependency；(2) evidence tax 的 truncation-vs-interference 分解不充分；(3) Conclusion 过短；(4) multi-task gradient conflict 文献遗漏；(5) \"evidence tax\" 术语 framing 问题。\n\n**R1 提出的 R2 未覆盖的关键问题**: (1) GRPO QLoRA vs bf16 confound（N2）——这是我遗漏的有价值的 methodological concern；(2) RSFT 共享 SFT checkpoint 的 variance 比较公平性（W3）。\n\n**分歧**: 仅在 §2.3 标题是否误导（M3）和 W3（RSFT variance）上有细微分歧。\n\n**Overall 一致**: 两位 reviewer 均给出 3.5 (Borderline Conference)。论文的实证贡献扎实但方法新颖性不足，更适合 Findings track。",
  "reviewer_id": "2",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### 主要优势\n\n[AGREE] R1-S1: 研究问题定义精准。Evidence-grounded DocRE 中 extraction-evidence trade-off 确实是一个有实际意义的研究空缺。\n\n[AGREE] R1-S2: EDCR 验证充分。我在自己的审稿中也肯定了 EDCR 的 per-relation 诊断价值（Appendix L, Figure 8）。但我同时指出了 EDCR 与 CED 共享 NLI backbone 的 circular dependency 风险——R1 未提及此点（见我的 W2）。partial correlation 控制了 TP 但未控制 NLI backbone bias。\n\n[AGREE] R1-S3: 三范式统一对比框架确实有参考价值。Table 1 的定性分类清晰，统一了 baseline（共享 SFT checkpoint）和评估协议。\n\n[AGREE] R1-S4: 跨架构验证（Qwen2.5 + LLaMA-3.1-8B）增强可推广性。我在自己的优势部分也特别肯定了这一点。\n\n[AGREE] R1-S5: 附录质量高。14 个 appendix sections 涵盖面广，尤其 Appendix K (error decomposition) 和 Appendix M (qualitative analysis) 信息量高。\n\n---\n\n### Must-Fix\n\n[AGREE] R1-N1: n=3 seeds 统计效力不足\n\n同意这是关键方法论弱点。补充以下证据：\n\n1. **Appendix D (Table 7)** 的 95% CI 确实跨零：论文自己报告了置信区间。当 CI 跨零时，evidence tax 的方向性 claim 在统计上不显著。\n2. **我的补充关注**：不仅是 1.7B 的 s42 issue——14B 的 cross-seed variance 也异常高（Table 7 显示 14B CI 更宽），暗示 evidence tax 在更大规模上可能不稳定。\n3. **与 R1 的分歧**：R1 建议\"增加 seeds 或弱化 claim 语言\"。我认为增加 seeds 是理想方案但可能不现实（14B 训练成本高）；更可行的是在正文 §4.4 中用 hedging language 替代当前的断言式表述（如 \"the evidence tax reverses\" → \"our 3-seed estimates suggest the evidence tax may reverse\"）。\n\n[AGREE] R1-N2: GRPO QLoRA vs bf16 confound\n\n同意存在实验混淆。具体证据：\n\n1. **Table 4 (Appendix A)** 显示 GRPO 使用 QLoRA 4-bit quantization + r=64，而 SFT/RSFT 使用 full-precision LoRA。这不是 controlled comparison——quantization 本身可能影响 gradient landscape 的稳定性。\n2. **bf16 G=4 实验的局限**：论文在 Table 14 (Appendix) 提供了 bf16 补充实验，但 R1 正确指出它控制了 group size 而未控制 lr。GRPO collapse 可能是 lr × quantization 的交互效应，而非 GRPO 范式固有的 decoupling。\n3. **我的补充**：不过，DPO 也展示了 substantial decoupling（Table 2: Rel-F1 drops 33-37%，§4.2），且 DPO 使用 offline 数据无需 online sampling——这意味着 gradient-based optimization 导致 decoupling 的 claim 不完全依赖于 GRPO 的 QLoRA 设置。GRPO collapse 的 severity 可能被 confound 放大，但 decoupling 方向性可能仍成立。\n\n[AGREE] R1-N3: DPO β=0.1 单点实验\n\n完全同意，这也是我自己 Must-Fix N2 的核心观点。补充：\n\n1. DPO 的 β 直接控制 KL constraint 强度。β=0.1 是较小的值（弱约束），允许策略大幅偏离 reference——这可能 maximize decoupling。β=0.5 或 β=1.0 可能产生更保守的行为，减轻 decoupling。\n2. 论文的 \"decoupling spectrum\"（Table 1）将 DPO 定性归类为 \"Partial decoupling\"——但这个归类完全基于 β=0.1 的单点观测。如果 β=0.5 下 DPO 表现更像 RSFT（低 decoupling），Table 1 的框架就需要重大修正。\n3. **与 R1 一致**：R1 说 \"β=0.01 可能更接近 GRPO collapse\"——这是合理推测。低 β 意味着几乎无 KL 约束，策略可以任意偏移，更容易 exploit reward 导致 decoupling。\n\n---\n\n### Should-Fix\n\n[AGREE] R1-W1: CED contrastive 设计附加价值不明确\n\n完全同意。我在 Must-Fix N1 中将此列为核心新颖性不足的证据之一。§3.4 末段自己承认 \"the contrastive formulation is not essential\"——0.02pp 的差异在 3-seed variance 范围内不显著。CED 作为独立 contribution 不成立。\n\n[AGREE] R1-W2: 14B 仅 1 seed SFT baseline\n\n同意。14B 数据点对 scaling claim 至关重要（是最大规模），但只有 1 seed 的 SFT baseline 使得 evidence tax 的 estimation 在该规模上不可靠。Table 3 的 14B 行应标注 \"single seed\" 的 caveat。论文在 Table 3 脚注提到 \"14B shows dev-set sign reversal\"，但对 single-seed limitation 不够显眼。\n\n[REBUT] R1-W3: RSFT 共享 SFT checkpoint 导致方差比较不公平\n\n部分反驳。R1 的观点是：SFT 方差来自 full training randomness，RSFT 方差仅来自 post-SFT 阶段，两者不可比。但我认为这个比较有其合理性：\n\n1. **论文的 variance comparison 回答的是实际部署问题**：practitioners 关心的是 \"从头训练一个 SFT model\" vs \"从头训练 SFT 然后做 RSFT\" 的 end-to-end variance。后者包含 SFT 阶段的 randomness（论文用 3 个不同 SFT seed 初始化 RSFT），所以 RSFT 的 variance 确实包含了 SFT 阶段的变异。\n2. **但 R1 的核心关注仍然有效**：Table 7 (Appendix D) 的 variance compression ratio 可能被夸大——如果 RSFT 从 **同一个** SFT checkpoint 出发（论文在 §3.2 说 \"shared SFT initialization\"），那么 RSFT 的 cross-seed variance 确实不含 SFT 初始化 randomness。这是一个 **重要澄清点**：论文需要明确说明 RSFT 的 3 个 seeds 是 3 个不同 SFT seeds → 各自 RSFT，还是 1 个 SFT seed → 3 个 RSFT runs。\n3. **我的判断**：从 §4.4 \"RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B...\" 的措辞看，RSFT 的 3 seeds 似乎来自 **同一个** SFT checkpoint。如果如此，R1 的 concern 完全成立——variance compression ratio 被人为缩小，因为 RSFT 未经历 SFT 阶段的 randomness。建议论文补充 \"3 different SFT checkpoints → RSFT\" 的 variance 数据。\n\n[AGREE] R1-W4: Test-set evidence tax 在 8B 反转\n\n同意需要更好解释。我在自己的 W5 中也提出了类似关注（Re-DocRED test 20pp drop）。具体补充：\n\n1. Dev +0.04pp → test −1.17pp 的 sign reversal 在 n=3 seeds、CI 跨零的前提下（R1-N1），实际上 neither 方向是统计显著的。\n2. 但论文 §4.4 的叙述语气暗示 dev 和 test 的 pattern 是一致的——8B 的反转挑战了这一叙述。\n3. 可能解释：test set 的 entity/relation distribution 与 dev 不同，evidence 在某些 relation types 上更 costly。Appendix L 的 per-relation EDCR 分析如果能在 test set 上复现，可以 shed light。\n\n---\n\n### Minor\n\n[AGREE] R1-M1: Abstract 首句 \"surpasses encoder baselines\" 缺引用。应 cite 至少一个 LLM-based DocRE 工作（如 AutoRE 或 ReFiRE）来 substantiate。\n\n[AGREE] R1-M2: Figure 4 y-axis 字号偏小，在打印版本中可能难以辨认。\n\n[REBUT] R1-M3: §2.3 标题 \"Evidence Faithfulness and Rejection Sampling\" 不算误导。该 section 确实同时覆盖了 NLI-based faithfulness 评估方法（Laban et al., 2022; Zhang et al., 2024）和 rejection sampling/self-improvement 方法（STaR, DeepSeek-R1），并论述了两者的理论连接——RSFT 正是将 faithfulness evaluation 作为 rejection criterion。标题反映了 section 的两个主题及其连接。不过，为清晰起见，可改为 \"Evidence Faithfulness Evaluation and Rejection-Based Training\"。\n\n[AGREE] R1-M4: RSFT mechanistic explanation（当前在 Limitations 末段）应在 future work 中更突出。Limitations 提到 \"we have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit regularization through candidate diversity, or from both\"——这是一个值得独立段落讨论的 open question。\n\n---\n\n### Questions\n\nR1-Q1 (EDCR on TP-only triples): 有价值的诊断问题。当前 EDCR 在 all predicted triples 上计算（包含 FP triples），TP-only variant 可以隔离 \"evidence quality for correct predictions\" vs \"evidence quality overall\"。论文 Appendix L 的 partial correlation 部分控制了 TP，但未直接报告 TP-only EDCR 值。\n\nR1-Q2 (替代 NLI 模型): 这与我的 W2 (EDCR-CED circular dependency) 直接相关。我强烈支持此问题——跨 NLI backbone 验证是 EDCR 作为 robust 诊断指标的必要条件。\n\nR1-Q3 (RSFT k>1): R1 自己已注意到 Appendix B 报告了 k=3 结果（Ign-F1 下降 1.02pp）。这说明 top-1 selection 是 RSFT 性能的关键——更 aggressive 的筛选反而更好。这个结果支持了 RSFT \"quality over quantity\" 的设计哲学。\n\nR1-Q4 (DPO with Evi-F1 scoring): 有趣的实验设计问题。如果 DPO 用 Evi-F1（而非 CED）构造 preference pairs，reward signal 更直接 align with evidence quality，decoupling 可能减轻——这可以测试 \"DPO decoupling 是范式固有问题 vs reward signal 设计问题\"。\n\n---\n\n### Missing References\n\n[AGREE] Xu et al. (2024) \"Towards Faithful Document-Level Relation Extraction\": 标题直接相关，如果确实发表且未被引用，是显著遗漏。\n\n[AGREE] DPO β sensitivity 文献: 结合 R1-N3 和我的 N2，DPO 超参数敏感性的 prior work（如 Tunstall et al. 2023 的 DPO 消融）应被讨论。\n\n---\n\n### 综合评价\n\nR1 和 R2（本人）的审稿意见高度一致：\n\n**共识点**: (1) n=3 seeds 统计效力不足；(2) DPO β 单点实验削弱 decoupling spectrum claim；(3) CED vs flat-NLI 差异微乎其微；(4) 实验规模和附录质量高。\n\n**R2 补充的 R1 未覆盖的关键问题**: (1) EDCR-CED 共享 NLI backbone 的 circular dependency；(2) evidence tax 的 truncation-vs-interference 分解不充分；(3) Conclusion 过短；(4) multi-task gradient conflict 文献遗漏；(5) \"evidence tax\" 术语 framing 问题。\n\n**R1 提出的 R2 未覆盖的关键问题**: (1) GRPO QLoRA vs bf16 confound（N2）——这是我遗漏的有价值的 methodological concern；(2) RSFT 共享 SFT checkpoint 的 variance 比较公平性（W3）。\n\n**分歧**: 仅在 §2.3 标题是否误导（M3）和 W3（RSFT variance）上有细微分歧。\n\n**Overall 一致**: 两位 reviewer 均给出 3.5 (Borderline Conference)。论文的实证贡献扎实但方法新颖性不足，更适合 Findings track。",
    "reviewer_id": "2",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 303 · 2026-05-25T22:42:24.484055+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3767
}
```

</details>

---

### Assistant

_source line 304 · 2026-05-25T22:42:34.122592+00:00_

已完成对 Reviewer 1 所有要点的逐条回应并提交给 Director。

核心结论：R1 和 R2 意见高度一致（Overall 均 3.5），在 n=3 seeds 统计效力、DPO β 单点实验、CED 微效三个核心问题上完全共识。我对 R1 的 W3（RSFT variance 比较公平性）做了部分反驳——认为 end-to-end variance 比较有一定合理性，但同意需要澄清 RSFT seeds 是否来自同一 SFT checkpoint。R1 提出的 GRPO QLoRA confound (N2) 是我原始审稿中遗漏的有价值观点，已在回应中 acknowledge。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2"
}
```

</details>

---
