# paper writing related work

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260517T170247.jsonl`
- **Structured JSON:** [`ff44c6f7a3264718a653.json`](../../sessions/ff/ff44c6f7a3264718a653.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-17T17:05:28.571895+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T17:05:28.572272+00:00_

docs/paper/acl-style/acl_lualatex.tex
docs/paper/acl-style/acl_latex.tex
docs/paper/main.tex
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:05:28.572453+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:05:28.572610+00:00_

docs/paper/acl-style/.git/description
docs/paper/acl-style/.git/hooks/applypatch-msg.sample
docs/paper/acl-style/.git/hooks/post-update.sample
docs/paper/acl-style/.git/hooks/pre-rebase.sample
docs/paper/acl-style/.git/hooks/pre-receive.sample
docs/paper/acl-style/.git/hooks/update.sample
docs/paper/acl-style/.git/hooks/commit-msg.sample
docs/paper/acl-style/.git/hooks/pre-applypatch.sample
docs/paper/acl-style/.git/hooks/pre-commit.sample
docs/paper/acl-style/.git/hooks/pre-push.sample
docs/paper/acl-style/.git/hooks/push-to-checkout.sample
docs/paper/acl-style/.git/hooks/pre-merge-commit.sample
docs/paper/acl-style/.git/hooks/sendemail-validate.sample
docs/paper/acl-style/.git/hooks/prepare-commit-msg.sample
docs/paper/acl-style/.git/hooks/fsmonitor-watchman.sample
docs/paper/acl-style/.git/info/exclude
docs/paper/acl-style/.git/shallow
docs/paper/acl-style/.git/objects/pack/pack-318a42012d9bccf84541e32464a1b84e874c3fdb.pack
docs/paper/acl-style/.git/objects/pack/pack-318a42012d9bccf84541e32464a1b84e874c3fdb.idx
docs/paper/acl-style/.git/objects/pack/pack-318a42012d9bccf84541e32464a1b84e874c3fdb.rev
docs/paper/acl-style/.git/packed-refs
docs/paper/acl-style/.git/refs/remotes/origin/HEAD
docs/paper/acl-style/.git/logs/refs/remotes/origin/HEAD
docs/paper/acl-style/.git/HEAD
docs/paper/acl-style/.git/logs/HEAD
docs/paper/acl-style/.git/logs/refs/heads/master
docs/paper/acl-style/.git/refs/heads/master
docs/paper/acl-style/.git/config
docs/paper/acl-style/README.md
docs/paper/acl-style/acl.sty
docs/paper/acl-style/formatting.md
docs/paper/acl-style/.git/index
docs/paper/acl-style/custom.bib
docs/paper/acl-style/anthology.bib.txt
docs/paper/acl-style/acl_lualatex.tex
docs/paper/acl-style/acl_natbib.bst
docs/paper/acl-style/acl_latex.tex
docs/paper/main.tex
docs/paper/acl.sty
docs/paper/acl_natbib.bst
docs/paper/references.bib
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:05:28.572795+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:05:28.572995+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{wan2024genres} recast DocRE as constrained generation, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
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
15	However, encoder methods now trail LLM-based approaches in extraction a
…[truncated 4770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:05:28.573157+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:05:28.573324+00:00_

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
38	\bibliographystyle{acl_natbib}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:05:28.573462+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:05:28.573581+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:05:28.573725+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:05:28.573907+00:00_

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
…[truncated 7698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:05:28.574065+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:05:28.574298+00:00_

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
…[truncated 13778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:05:28.574590+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\nDocument-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.\nDocRED \\citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.\nATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction, and KD-DocRE \\citep{tan2022redocred} applied knowledge distillation to bridge the teacher-student performance gap.\nA parallel thread incorporates sentence-level evidence into these architectures.\nSAIS \\citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.\nDREEAM \\citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.\nEIDER \\citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.\nIn all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.\nRecent work has recast DocRE for large language models.\n\\citet{wan2024genres} reformulate extraction as constrained generation with entity-aware decoding.\n\\citet{xu2024lmrc} frame it as multi-choice reading comprehension, which restricts outputs to predefined options and reduces the generation burden.\n\\citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge to ground predictions in document context.\nThese methods match or surpass encoder baselines in extraction accuracy but produce bare triplets without evidence.\nThe critical distinction between encoder and generative evidence lies in their computational nature.\nIn SAIS and DREEAM, evidence retrieval is a classification task that regularizes the encoder and improves extraction without increasing output length.\nIn LLM-based DocRE, evidence production requires additional output tokens for each predicted triple, and this generation burden competes with the extraction objective for model capacity.\nThis asymmetry explains why evidence ``helps'' in encoder methods but can ``hurt'' in generative ones: the two paradigms operate on fundamentally different forms of evidence integration.\n\nGroup Relative Policy Optimization (GRPO), introduced by \\citet{shao2024deepseekmath}, computes advantages within groups of sampled outputs to eliminate the need for a separate value network.\nRecent applications have extended GRPO to structured information extraction: E-GRPO \\citep{zhao2025egrpo} incorporates entity-aware rewards for named entity recognition, and R1-RE \\citep{dai2025r1re} applies reinforcement learning with verifiable rewards to relation extraction.\nDirect Preference Optimization \\citep{rafailov2023direct} reformulates RLHF as implicit reward maximization through preference pairs, without explicit reward models.\nRecent analyses argue that RL fine-tuning does not cause catastrophic forgetting of pre-trained knowledge \\citep{jin2025rl_panacea}.\nOur findings are compatible with this conclusion but address a distinct phenomenon.\nThe decoupling we observe is an intra-task multi-objective trade-off where extraction and evidence generation compete for model capacity within a single task, rather than knowledge loss across separate tasks.\nThe mild decoupling under bf16 GRPO confirms this interpretation: the model retains its extraction capability but shifts resource allocation under evidence reward pressure.\nReward overoptimization, where proxy reward scores increase while true performance degrades, is a known risk in RLHF \\citep{gao2023scaling}.\nConstrained RLHF has been proposed to mitigate this effect in multi-objective settings \\citep{moskovitz2024constrained}.\nOur decoupling spectrum represents a new instance of intra-task reward overoptimization, where evidence rewards crowd out extraction quality.\nQLoRA compounds this problem: the quantized parameter space constrains effective capacity, and the divergence between quantized and full-precision actors grows over extended training, which amplifies the underlying multi-objective conflict.\n\n\\citet{zelikman2022star} introduced STaR, an iterative self-improvement method that trains language models on their own correct outputs and bootstraps with rationale augmentation for initially incorrect problems.\nSubsequent work has extended this framework to mathematical reasoning, code generation, and instruction following.\nOur RSFT procedure is a single-round variant: the model samples multiple candidate outputs per input, a quality filter selects the best response, and the model trains on the filtered set without iteration.\nThe contribution of RSFT in our setting is not the self-training framework, which is well-established, but its application to evidence-grounded DocRE with CED/NLI scoring as a domain-specific quality filter.\nThis application reveals a structural advantage of discrete output selection over gradient-based optimization for multi-output tasks.\nBecause RSFT selects complete outputs rather than differentiating through a reward signal, it cannot exploit the extraction-evidence trade-off that GRPO and DPO discover through gradient updates.\nThe filtering mechanism inherently preserves joint quality: it retains outputs that are simultaneously good at extraction and evidence production, rather than allowing one objective to dominate the other.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\nDocument-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.\nDocRED \\citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.\nATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction, and KD-DocRE \\citep{tan2022redocred} applied knowledge distillation to bridge the teacher-student performance gap.\nA parallel thread incorporates sentence-level evidence into these architectures.\nSAIS \\citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.\nDREEAM \\citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.\nEIDER \\citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.\nIn all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.\nRecent work has recast DocRE for large language models.\n\\citet{wan2024genres} reformulate extraction as constrained generation with entity-aware decoding.\n\\citet{xu2024lmrc} frame it as multi-choice reading comprehension, which restricts outputs to predefined options and reduces the generation burden.\n\\citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge to ground predictions in document context.\nThese methods match or surpass encoder baselines in extraction accuracy but produce bare triplets without evidence.\nThe critical distinction between encoder and generative evidence lies in their computational nature.\nIn SAIS and DREEAM, evidence retrieval is a classification task that regularizes the encoder and improves extraction without increasing output length.\nIn LLM-based DocRE, evidence production requires additional output tokens for each predicted triple, and this generation burden competes with the extraction objective for model capacity.\nThis asymmetry explains why evidence ``helps'' in encoder methods but can ``hurt'' in generative ones: the two paradigms operate on fundamentally different forms of evidence integration.\n\nGroup Relative Policy Optimization (GRPO), introduced by \\citet{shao2024deepseekmath}, computes advantages within groups of sampled outputs to eliminate the need for a separate value network.\nRecent applications have extended GRPO to structured information extraction: E-GRPO \\citep{zhao2025egrpo} incorporates entity-aware rewards for named entity recognition, and R1-RE \\citep{dai2025r1re} applies reinforcement learning with verifiable rewards to relation extraction.\nDirect Preference Optimization \\citep{rafailov2023direct} reformulates RLHF as implicit reward maximization through preference pairs, without explicit reward models.\nRecent analyses argue that RL fine-tuning does not cause catastrophic forgetting of pre-trained knowledge \\citep{jin2025rl_panacea}.\nOur findings are compatible with this conclusion but address a distinct phenomenon.\nThe decoupling we observe is an intra-task multi-objective trade-off where extraction and evidence generation compete for model capacity within a single task, rather than knowledge loss across separate tasks.\nThe mild decoupling under bf16 GRPO confirms this interpretation: the model retains its extraction capability but shifts resource allocation under evidence reward pressure.\nReward overoptimization, where proxy reward scores increase while true performance degrades, is a known risk in RLHF \\citep{gao2023scaling}.\nConstrained RLHF has been proposed to mitigate this effect in multi-objective settings \\citep{moskovitz2024constrained}.\nOur decoupling spectrum represents a new instance of intra-task reward overoptimization, where evidence rewards crowd out extraction quality.\nQLoRA compounds this problem: the quantized parameter space constrains effective capacity, and the divergence between quantized and full-precision actors grows over extended training, which amplifies the underlying multi-objective conflict.\n\n\\citet{zelikman2022star} introduced STaR, an iterative self-improvement method that trains language models on their own correct outputs and bootstraps with rationale augmentation for initially incorrect problems.\nSubsequent work has extended this framework to mathematical reasoning, code generation, and instruction following.\nOur RSFT procedure is a single-round variant: the model samples multiple candidate outputs per input, a quality filter selects the best response, and the model trains on the filtered set without iteration.\nThe contribution of RSFT in our setting is not the self-training framework, which is well-established, but its application to evidence-grounded DocRE with CED/NLI scoring as a domain-specific quality filter.\nThis application reveals a structural advantage of discrete output selection over gradient-based optimization for multi-output tasks.\nBecause RSFT selects complete outputs rather than differentiating through a reward signal, it cannot exploit the extraction-evidence trade-off that GRPO and DPO discover through gradient updates.\nThe filtering mechanism inherently preserves joint quality: it retains outputs that are simultaneously good at extraction and evidence production, rather than allowing one objective to dominate the other.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T17:05:28.574791+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:05:28.574940+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T17:05:28.575069+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T17:05:28.575189+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T17:05:28.575337+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T17:05:28.575456+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T17:05:28.575583+00:00_

13:\citet{wan2024genres} reformulate extraction as constrained generation with entity-aware decoding.
32:QLoRA compounds this problem: the quantized parameter space constrains effective capacity, and the divergence between quantized and full-precision actors grows over extended training, which amplifies the underlying multi-objective conflict.
35:Subsequent work has extended this framework to mathematical reasoning, code generation, and instruction following.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T170247",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T17:05:28.575810+00:00_

All clean. The `ing` matches are nouns (decoding, training, following), not participial phrase endings.

Written to `docs/paper/sections/related_work.tex`. Three thematic paragraphs (~680 words total):
- **P1** (~300w): Encoder DocRE (DocRED, ATLOP, KD-DocRE) → evidence in encoders (SAIS, DREEAM, EIDER as classification) → LLM DocRE (GenRES, LMRC, DocKS-RAG) → key distinction: classification evidence regularizes; generative evidence costs capacity
- **P2** (~220w): GRPO + structured IE extensions (E-GRPO, R1-RE) → DPO → RL forgetting debate (our decoupling is intra-task trade-off, not inter-task forgetting) → reward overoptimization (Gao, Moskovitz) → QLoRA amplification
- **P3** (~160w): STaR → RSFT as single-round variant → honest positioning (novelty is CED/NLI filter for DocRE, not framework) → structural advantage of discrete selection over gradient optimization

17 unique citations, 0 dashes, 0 -ing phrase endings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260517T170247"
}
```

</details>

---
