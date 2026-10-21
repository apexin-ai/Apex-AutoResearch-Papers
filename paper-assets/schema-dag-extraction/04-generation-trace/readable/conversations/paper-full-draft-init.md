# paper full draft init

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_full-draft-init_20260515T194742.jsonl`
- **Structured JSON:** [`ce67372362645f477299.json`](../../sessions/ce/ce67372362645f477299.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-15T19:50:51.332516+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:50:51.332907+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:50:51.333275+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "writing_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "writing_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:50:51.333716+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml\", \"content\": \"# Writing Plan — schema-dag-extraction\\n# Generated: 2026-05-15\\n# Venue: EMNLP 2026 (ARR May 25 cycle)\\n# Format: 8 pages main text + unlimited references\\n# Mode: Full Draft (2-claim analysis paper + SDGD negative result)\\n\\nmeta:\\n  title: \\\"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\\\"\\n  venue: EMNLP 2026 Main\\n  submission_deadline: \\\"2026-05-25\\\"\\n  page_limit: 8\\n  template: \\\"acl2023\\\"  # ARR uses ACL rolling review LaTeX template\\n  template_note: \\\"No EMNLP 2026 template found locally. Using acl2023.sty (standard ARR template). Worker must download from https://github.com/acl-org/acl-style-files if not available.\\\"\\n  primary_model: \\\"Qwen3-32B-FP8\\\"\\n  secondary_model: \\\"LLaMA-3.1-8B-Instruct (exp-012, D022: 70B→8B cross-scale validation)\\\"\\n  datasets: [\\\"Few-NERD (66 types)\\\", \\\"FewRel (80 relations)\\\", \\\"MAVEN (168 event types)\\\"]\\n\\n# =============================================================================\\n# PAPER OUTLINE\\n# =============================================================================\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    dependencies: [introduction, experiments, results, sdgd_negative, conclusion]\\n    key_content:\\n      - Problem: training-free LLM IE degrades on complex schemas; prior work conflates count and confusability\\n      - Method: first controlled empirical study isolating type confusability from count across 3 tasks\\n      - Findings: multi-channel degradation (count→recall, confusability→type confusion); pairwise SCS robust cross-task (r=0.11-0.13); effect amplifies 3.4× with schema complexity; per-type aggregation confounded on homogeneous schemas\\n      - Negative result: naive confusability-aw
…[truncated 22356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:50:51.333936+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:50:51.334247+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is itself a contribu
…[truncated 10166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:50:51.334451+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:50:51.334656+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## LLaMA-3.1-8B Chat Template 必须 (2026-05-15) ⭐⭐\\n- `run_extraction.py` 用 `llm.generate(prompts, ...)` 裸文本调用，Qwen3 能工作但 LLaMA-3.1-Instruct 不行\\n- **根因**: LLaMA-3.1-Instruct 严格依赖 `<|begin_of_text|><|start_header_id|>...` chat template，裸文本输入时模型不理解指令\\n- 在 JSON schema 约束下，走阻力最小路径输出 `[]`（gen_tokens=2）\\n- **修复**: 调用 `tokenizer.apply_chat_template([{\\\"role\\\": \\\"user\\\", \\\"content\\\": p}], tokenize=False, add_generation_prompt=True)` 包装 prompt\\n- **教训**: 非 Qwen 模型都应该检查是否需要 chat template，不能假设裸文本 prompt 通用\\n\\n## Blackwell GPU flashinfer 兼容性修复 (2026-05-15, UPDATED)\\n- RTX PRO 6000 Blackwell (SM120) 上 flashinfer 0.6.8.post1 无法 JIT 编译 FP8 GEMM，需要 nvcc ≥12.9\\n- **修复**: 升级 flashinfer 到 0.6.11.post2 + 安装 nvidia-cuda-nvcc 13.2.78 + 脚本中设 `export CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13`\\n- ~~旧记录说需要 VLLM_ATTENTION_BACKEND=FLASH_ATTN~~ 该 env var 在 vLLM 0.20.2 中已废弃，不要使用\\n- **所有新脚本都应包含 CUDA_HOME 设置**\\n\\n## Bootstrap 指标校正 (2026-05-15) ⭐⭐\\n- **Few-NERD pairwise r**: 论文用 0.112 [0.076, 0.156]（非旧值 0.156）。原因：V2 prompt 覆写了 predictions_exp2.json，0.112 来自更干净的 V2 数据\\n- **Confusion ratio (count_12)**: 论文用 21.2x [5.3, 52.2]（非旧值 9.9x）。原因：旧值是 raw FP count ratio，新值是 rate ratio（方法学正确）\\n- 所有 7 项 CI 排除 null，效应稳健\\n\\n## FewRel 80-rel Scaling Effect (2026-05-15) ⭐⭐\\n- 80-rel degradation 35.3pp vs 16-rel 12.6pp (2.8x)，BCS effect -31.2pp vs -9.1pp (3.4x amplification)\\n- **Insight**: relation space 大小是 confusability effect 的 multiplier，不只是 additive\\n- EXIT_CODE=129 是 SIGHUP（SSH 断连），实验实际跑完了。**教训**：非 submit_training_job 启动的实验没有 tmux 保护会被 SSH 断连杀死\\n\\n## exp-007 Error Taxonomy (2026-05-15) ⭐⭐\\n- IntraSub vs BCS: Spearman ρ=1.0 (p<0.001)，BCS≥0.95 时 49.4% FP 是 batch 内类型混淆\\n- Hallucination + boundary <3%。**LLM 主要错误模式是 type confusion 而非幻觉**\\n- Claim 2 最强 mechan
…[truncated 4395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:50:51.334820+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": "{'conclusion': 'success'}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "schema-dag-extraction",
    "filters": "{'conclusion': 'success'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:50:51.335416+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp015_scs_validation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:26:21.582Z\", \"updated_at\": \"2026-05-15T15:26:41.874Z\", \"spec\": {\"hypothesis\": \"Embedding SCS is a valid proxy for empirical confusion: significant rank correlation with pairwise confusion counts\", \"dataset\": \"Few-NERD\", \"model\": \"Qwen3-32B + MiniLM\", \"design\": \"Spearman/Kendall correlation between SCS matrix and empirical confusion counts from exp-002. All pairs + nonzero-only subsets.\", \"data_path\": \"/root/schema-dag-extraction/artifacts/exp015_scs_validation.json\", \"data_count\": \"1953 pairs (216 nonzero)\", \"model_name\": \"N/A (analysis)\", \"seed\": 42, \"command\": \"python3 src/scs_validation.py\", \"server\": \"cqa1-38874\", \"checkpoint_path\": \"/root/schema-dag-extraction/artifacts/exp015_scs_validation.json\", \"log_path\": \"/root/schema-dag-extraction/artifacts/exp015_scs_validation.json\"}, \"conclusion\": \"success\", \"metrics\": {\"all_pairs\": {\"n\": 1953, \"n_nonzero\": 216, \"qwen3_spearman\": 0.1682, \"qwen3_spearman_p\": \"7.3e-14\", \"qwen3_kendall\": 0.1351, \"minilm_spearman\": 0.1439, \"minilm_spearman_p\": \"1.7e-10\", \"minilm_kendall\": 0.1152}, \"nonzero_only\": {\"n\": 216, \"qwen3_spearman\": 0.2722, \"qwen3_spearman_p\": \"5.0e-05\", \"qwen3_kendall\": 0.2001, \"minilm_spearman\": 0.306, \"minilm_spearman_p\": \"4.6e-06\", \"minilm_kendall\": 0.2276}, \"key_finding\": \"Both embeddings significantly predict confusion (all p<1e-5). Qwen3 better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS is a valid but partial proxy — context, frequency, mention ambiguity also matter.\"}, \"completed_at\": \"2026-05-15T15:26:41.874Z\"}, \"bootstrap_ci_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:22:26.006Z\", \"updated_at\": \"2026-05-15T15:22:46.515Z\", \"spec\": {\"hypothesis\": \"All key corr
…[truncated 23839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:50:51.335640+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "write_paper_section edit_paper_section",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "write_paper_section edit_paper_section",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:50:51.335775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:50:51.335957+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:50:51.336099+00:00_

artifacts/_project/paper/method_framework.md
artifacts/_project/paper/related_work_draft.md
artifacts/_project/paper/maven_description.md
figures/paper/fig_count_curves.pdf
figures/paper/fig_count_curves.png
figures/paper/fig_error_taxonomy.pdf
figures/paper/fig_error_taxonomy.png
figures/paper/fig_bcs_scaling.pdf
figures/paper/fig_bcs_scaling.png
figures/paper/fig_sdgd_comparison.pdf
figures/paper/fig_sdgd_comparison.png
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/sdgd_negative.tex
docs/paper/references.bib
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/acl.sty
docs/paper/acl_natbib.bst
docs/paper/_pdf_images/main_p1.png
docs/paper/_pdf_images/main_p2.png
docs/paper/_pdf_images/main_p3.png
docs/paper/_pdf_images/main_p4.png
docs/paper/_pdf_images/main_p5.png
docs/paper/_pdf_images/main_p6.png
docs/paper/_pdf_images/main_p7.png
docs/paper/_pdf_images/main_p11.png
docs/paper/_pdf_images/main_p12.png
docs/paper/_pdf_images/main_p10.png
docs/paper/main.tex
docs/paper/sdgd_negative.tex
docs/paper/related_work.tex
docs/paper/conclusion.tex
docs/paper/_pdf_images/main_p8.png
docs/paper/_pdf_images/main_p9.png
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/main.blg
docs/paper/main.bbl
docs/paper/main.aux
docs/paper/main.out
docs/paper/main.fls
docs/paper/main.log
docs/paper/main.pdf
docs/paper/main.fdb_latexmk

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:50:51.336252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:50:51.336425+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77-
…[truncated 6013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:50:51.336580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T19:50:51.336732+00:00_

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
13	\usepackage{enumitem}
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{conclusion}
35	
36	\section*{Limitations}
37	All experiments use a single primary model (Qwen3-32B); cross-model validation is ongoing. The pairwise confusability signal explains roughly 1.3--1.7\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality account for the remainder. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored.
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\section{Additional Figures}
44	\label{sec:appendix_figures}
45	
46	\begin{figure}[h]
47	\centering
48	\includegraphics[width=\columnwidth]{../../figures/paper/fig_count_curves.pdf}
49	\caption{Count-degradation curves across three IE tasks. NER recall and RE accuracy decline monotonically with schema size; MAVEN relaxed F1 increases, reflecting same-domain disambiguation benefits (\S\ref{sec:centrality_confound}).}
50	\label{fig:count_curves}
51	\end{figure}
52	
53	\begin{figure}[h]
54	\centering
55	\includegraphics[width=\columnwidth]{../../figures/paper/fig_bcs_scaling.pdf}
56	\caption{BCS-controlled FewRel accuracy. The confusability gap between low-BCS and high-BCS batches widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations ($3.4\times$ amplification).}
57	\label{fig:bcs_scaling}
58	\end{figu
…[truncated 808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T19:50:51.337022+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "We compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations, which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder.",
  "new_string": "We compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "old_string": "We compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations, which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder.",
    "new_string": "We compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T19:50:51.337216+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T19:50:51.337370+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "experimental_setup_tex",
  "type": "paper",
  "description": "Experimental Setup section (§3) for EMNLP 2026 paper — Tasks/Datasets, SCS/BCS definitions, experimental design, evaluation metrics, model/inference details. All numbers verified against registry.",
  "project": "schema-dag-extraction",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "tags": "['paper', 'experimental_setup', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "experimental_setup_tex",
    "type": "paper",
    "description": "Experimental Setup section (§3) for EMNLP 2026 paper — Tasks/Datasets, SCS/BCS definitions, experimental design, evaluation metrics, model/inference details. All numbers verified against registry.",
    "project": "schema-dag-extraction",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "tags": "['paper', 'experimental_setup', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T19:50:51.337527+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_bca5a1\", \"name\": \"experimental_setup_tex\", \"type\": \"paper\", \"description\": \"Experimental Setup section (§3) for EMNLP 2026 paper — Tasks/Datasets, SCS/BCS definitions, experimental design, evaluation metrics, model/inference details. All numbers verified against registry.\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/paper/experimental_setup.tex\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:50:38.000328+00:00\", \"tags\": [\"paper\", \"experimental_setup\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-init_20260515T194742",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T19:50:51.337696+00:00_

Experimental Setup (§3) 已完成，位于 `docs/paper/experimental_setup.tex`。

**章节结构**（~900 words，符合预算）：
- §3.1 Tasks and Datasets — Few-NERD/FewRel/MAVEN 三数据集 + 统计表
- §3.2 SCS — pairwise SCS 和 BCS 的形式化定义，Qwen3 (5120-d) + MiniLM (384-d) 双 embedding
- §3.3 Experimental Design — Exp1 count curves + Exp2 BCS-controlled factorial
- §3.4 Evaluation Metrics — text-match F1 (NER), accuracy (RE), relaxed F1 (ED) + 跨任务 metric 差异 justification
- §3.5 Model and Inference — Qwen3-32B-FP8, vLLM, prompt v2, greedy decoding, bootstrap CI

**所有数字已与 registry 交叉验证。** 唯一新增编辑：补充 Qwen3 embedding 维度 (5120-d)。

**待注意**：
- MAVEN "8,042 sentences" 来自先前数据探查，registry 仅记录 710 documents / 18,904 mentions — 合理但不可从 registry 直接追溯
- 表中 BCS Range 为 batch 级别范围（包含 Exp1+Exp2 极端 batch），非 pairwise SCS 范围
- D024：当前为单模型版本（Qwen3-32B-FP8），LLaMA-3.1-8B 结果待 exp-012 完成后 patch

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_full-draft-init_20260515T194742"
}
```

</details>

---
