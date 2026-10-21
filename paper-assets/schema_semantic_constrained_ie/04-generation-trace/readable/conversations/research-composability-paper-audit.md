# research composability paper audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/chats/worker_research_composability_paper_audit_20260516T021140.jsonl`
- **Structured JSON:** [`be2e5c8f54b893cf86eb.json`](../../sessions/be/be2e5c8f54b893cf86eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

69 recorded events

### Tool call

_source line 1 · 2026-05-16T02:16:43.958941+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_read_only",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_read_only",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:16:43.959418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:16:43.959620+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:16:43.960005+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026)\\n\\n## Title\\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\\n(D015: \\\"Near-Complete\\\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\\n\\n## Core Claims\\n\\n### Claim 1 (Empirical): Violation Landscape\\nLLM-based IE system
…[truncated 19275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:16:43.960187+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/schema_semantic_constrained_ie/paper -type f -name \"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "find /root/schema_semantic_constrained_ie/paper -type f -name \"*.tex\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T02:16:43.960323+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T02:16:43.960506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/abstract.tex\\n/root/schema_semantic_constrained_ie/paper/section7_conclusion_compressed.tex\\n/root/schema_semantic_constrained_ie/paper/section5_crossmodel_draft.tex\\n/root/schema_semantic_constrained_ie/paper/appendix_llama_per_relation.tex\\n/root/schema_semantic_constrained_ie/paper/main.tex\\n/root/schema_semantic_constrained_ie/paper/section1_introduction_draft.tex\\n/root/schema_semantic_constrained_ie/paper/section2_background.tex\\n/root/schema_semantic_constrained_ie/paper/section4_composition_draft.tex\\n/root/schema_semantic_constrained_ie/paper/section3_violation_landscape.tex\\n/root/schema_semantic_constrained_ie/paper/section6_related_work.tex\\n/root/schema_semantic_constrained_ie/paper/section3_method_draft.tex\\n/root/schema_semantic_constrained_ie/paper/section5_scierc_draft.tex\\n/root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex\\n/root/schema_semantic_constrained_ie/paper/appendix_related_work.tex\\n/root/schema_semantic_constrained_ie/paper/appendix_discussion.tex\\n/root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex\\n/root/schema_semantic_constrained_ie/paper/discussion_paragraphs.tex\\n/root/schema_semantic_constrained_ie/paper/discussion_paragraphs_cf83d1.tex\\n/root/schema_semantic_constrained_ie/paper/section5_scierc_draft_4796e8.tex\\n/root/schema_semantic_constrained_ie/paper/section5_docred_draft_9b84f1.tex\\n/root/schema_semantic_constrained_ie/paper/section7_conclusion.tex\\n/root/schema_semantic_constrained_ie/paper/section7_conclusion_550cbf.tex\\n/root/schema_semantic_constrained_ie/paper/abstract_fd4b26.tex\\n/root/schema_semantic_constrained_ie/paper/abstract_d3264e.tex\\n/root/schema_semantic_constrained_ie/paper/section6_relwork_additions.tex\\n/root/schema_semantic_constrained_ie/paper/section6_relwork_outline.tex\\n/root/schema_semantic_constrained_ie/paper/discussion_cf_fallback.tex\\n/root/
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:16:43.960766+00:00_

artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
artifacts/_project/paper/section6_relwork_additions.tex
artifacts/_project/paper/discussion_paragraphs.tex
artifacts/dream_reports/dream_20260514T205155/best/paper.tex
artifacts/dream_reports/dream_20260514T205155/median/paper.tex
artifacts/dream_reports/dream_20260514T205155/worst/paper.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section7_conclusion.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section7_conclusion_compressed.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:16:43.960968+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/section5_composability.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/section5_composability.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:16:43.961195+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t% Section 5 — Composability with Fine-Tuned Models\\n     2\\t% exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\\n     3\\t%          w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval\\n     4\\t\\n     5\\t\\\\subsection{Composability with Fine-Tuned Models}\\n     6\\t\\\\label{sec:composability-ft}\\n     7\\t\\n     8\\tThe cross-model validation in \\\\S\\\\ref{sec:cross-model} establishes that\\n     9\\tOntoCoDec generalizes across model families in the zero-shot regime.\\n    10\\tA complementary question is whether the same constraints remain useful\\n    11\\tafter task-specific fine-tuning, where the model has been trained to\\n    12\\temit ontology-conformant outputs and one might expect violations to\\n    13\\tdisappear on their own.\\n    14\\tWe test this by LoRA fine-tuning both Qwen3-8B and Llama-3.1-8B on\\n    15\\tSciERC and then evaluating each fine-tuned model with and without the\\n    16\\ttwo-layer constraints, yielding a 2$\\\\times$2 design per model family.\\n    17\\t\\n    18\\t\\\\begin{table}[t]\\n    19\\t\\\\centering\\n    20\\t\\\\small\\n    21\\t\\\\setlength{\\\\tabcolsep}{3.4pt}\\n    22\\t\\\\resizebox{\\\\columnwidth}{!}{%\\n    23\\t\\\\begin{tabular}{@{}lll rr rr@{}}\\n    24\\t\\\\toprule\\n    25\\t& & & \\\\multicolumn{2}{c}{\\\\textbf{Viol.~(\\\\%)}}\\n    26\\t& \\\\multicolumn{2}{c}{\\\\textbf{F1}} \\\\\\\\\\n    27\\t\\\\cmidrule(lr){4-5} \\\\cmidrule(l){6-7}\\n    28\\t\\\\textbf{Model} & \\\\textbf{Train} & \\\\textbf{Decode}\\n    29\\t  & DR\\\\,$\\\\downarrow$ & CF\\n    30\\t  & Rel.\\\\,$\\\\uparrow$ & Ent.\\\\,$\\\\uparrow$ \\\\\\\\\\n    31\\t\\\\midrule\\n    32\\t\\\\multirow{4}{*}{Qwen3-8B}\\n    33\\t  & Zero-shot & U   & 15.37 & 0.08 & 8.23 & 31.01 \\\\\\\\\\n    34\\t  & Zero-shot & S1  & \\\\textbf{0.93}  & 9.90 & 8.36 & 30.98 \\\\\\\\\\n    35\\t  & LoRA      & U   &  1.95 & 0
…[truncated 4379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:16:43.961350+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T02:16:43.961593+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t% =============================================================\\n     2\\t% Paper Tables Draft — Schema-Semantic Constrained IE\\n     3\\t% Generated from experiment registry, 2026-05-14\\n     4\\t% Model: Qwen3-8B (zero-shot), all percentages to 1 d.p.\\n     5\\t% =============================================================\\n     6\\t\\n     7\\t% ------------------------------------------------------------\\n     8\\t% Table 1: SciERC 5-way Ablation\\n     9\\t% ------------------------------------------------------------\\n    10\\t\\\\begin{table}[t]\\n    11\\t\\\\centering\\n    12\\t\\\\caption{Ablation study on SciERC test set (551 samples, Qwen3-8B zero-shot).\\n    13\\tDR = Domain/Range violation rate, RV = Relation Vocabulary violation rate,\\n    14\\tET = Entity Type violation rate, CF = Cross-Field consistency violation rate.\\n    15\\t$\\\\downarrow$: lower is better; $\\\\uparrow$: higher is better.\\n    16\\t$\\\\Delta$DR shows the absolute change (pp) relative to the unconstrained baseline.}\\n    17\\t\\\\label{tab:scierc-ablation}\\n    18\\t\\\\resizebox{\\\\columnwidth}{!}{%\\n    19\\t\\\\begin{tabular}{l cccc cc c}\\n    20\\t\\\\toprule\\n    21\\tMode & DR$\\\\downarrow$ & RV$\\\\downarrow$ & ET$\\\\downarrow$ & CF$\\\\downarrow$ & R-F1$\\\\uparrow$ & E-F1$\\\\uparrow$ & $\\\\Delta$DR (pp) \\\\\\\\\\n    22\\t\\\\midrule\\n    23\\tUnconstrained      & 15.4 & 1.4          & 0.4          & \\\\textbf{0.1} & 8.2          & 31.0          & ---                    \\\\\\\\\\n    24\\tGrammar-only       & 14.8 & \\\\textbf{0.0} & \\\\textbf{0.0} & \\\\textbf{0.1} & 8.2          & 31.0          & $-$0.5                 \\\\\\\\\\n    25\\tSemantic-only      & 11.7 & 1.5          & 0.4          & 2.7          & 8.2          & 31.0          & $-$3.7                 \\\\\\\\\\n    26\\tFull (S1)          & \\\\textbf{0.9} & \\\\textbf{0.0} & \\\\textbf{0.0} & 9.9  & \\\\textbf{
…[truncated 5536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:16:43.961778+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/abstract.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/abstract.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:16:43.961933+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\begin{abstract}\\n     2\\tLLM-based information extraction systems produce systematic ontology constraint violations during autoregressive generation.\\n     3\\tOn SciERC (7 relation types), 15.37\\\\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.46\\\\%---comparable rates governed by \\\\emph{constraint tightness} rather than ontology scale.\\n     4\\t%\\n     5\\tWe present \\\\textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:\\n     6\\t(1)~a \\\\emph{grammar layer} (XGrammar CFG) enforcing JSON structural validity and restricting entity/relation vocabularies to schema-defined values (ET, RV\\\\,$\\\\to$\\\\,0\\\\%); and\\n     7\\t(2)~a \\\\emph{semantic layer} enforcing domain/range constraints via a stateful entity registry and dynamic logit masking.\\n     8\\tThe grammar layer is an enabling prerequisite; the two compose via bitwise AND on token-level masks.\\n     9\\t%\\n    10\\tOn SciERC, \\\\textsc{OntoCoDec} reduces domain/range violations by 94\\\\% (15.37\\\\%\\\\,$\\\\to$\\\\,0.93\\\\%) while maintaining extraction F1 ({+}0.13pp, $p{=}0.58$).\\n    11\\tOn DocRED, violations decrease by 45--90\\\\% depending on the model, with significant relation F1 gains for both Qwen3-8B ({+}0.50pp, $p{<}0.001$) and Llama-3.1-8B ({+}0.29pp, $p{=}0.013$; DR$\\\\downarrow$90.2\\\\%).\\n    12\\t% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1\\n    13\\tThe dual-factor mechanism---tightness $\\\\times$ baseline violation rate---explains cross-dataset and cross-model DR reduction differences.\\n    14\\t\\\\end{abstract}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:16:43.962077+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/section1_introduction_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/section1_introduction_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:16:43.962250+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t% Section 1: Introduction (compressed, 669→~550 words)\\n     2\\t\\n     3\\t\\\\section{Introduction}\\n     4\\t\\\\label{sec:introduction}\\n     5\\t\\n     6\\tLarge language models are increasingly deployed for zero-shot information extraction~\\\\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.\\n     7\\tWe call such outputs \\\\emph{domain/range violations}---structurally valid triples that are ontologically invalid.\\n     8\\tIn a systematic study, we find violations are pervasive: 15.4\\\\% of triples on SciERC~\\\\cite{luan2018scierc} and 18.7\\\\% on DocRED~\\\\cite{yao2019docred}, driven by \\\\emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.\\n     9\\tRelations with tight constraints exhibit far higher rates (\\\\textsc{Compare}: 42.4\\\\%) than loosely constrained ones (\\\\textsc{Used-for}: 0.8\\\\%).\\n    10\\t\\n    11\\tExisting approaches leave a fundamental gap.\\n    12\\tSchema-informed prompting reduces violations by 62\\\\% on average but is per-relation unreliable---violations for \\\\textsc{Evaluate-for} actually \\\\emph{increase} by 5.8\\\\,pp.\\n    13\\tGrammar-constrained decoding~\\\\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.\\n    14\\tPost-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding.\\n    15\\tTraining-based approaches~\\\\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.\\n    16\\t\\n    17\\tWe propose \\\\textbf{OntoCoDec} (\\\\textbf{Onto}logy-\\\\textbf{Co}mpiled \\\\textbf{Dec}oding), a framework that compiles an IE ontology into two composabl
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T02:16:43.962396+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/section7_conclusion_compressed.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/section7_conclusion_compressed.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T02:16:43.962566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t% Section 7 — Discussion and Conclusion (compressed)\\n     2\\t% Full discussion paragraphs moved to Appendix B.\\n     3\\t\\n     4\\t\\\\paragraph{CF Severity.}\\n     5\\t% exp_ids: phase2_scierc_full_s1 (CF=9.90%), phase2_scierc_grammar_only (CF=0.08%),\\n     6\\t%          phase2_docred_full_s1 (CF=2.57%), llama_docred_full_s1 (CF=12.02%)\\n     7\\tDR violations produce ontologically invalid triples---a hard constraint failure that no downstream system can recover from.\\n     8\\tCF violations are qualitatively different: each individual triple remains type-valid with respect to its own relation's domain/range rules; only cross-triple consistency is broken when the same entity receives different types across relations.\\n     9\\tThe dominant conflict pattern---\\\\emph{Generic}$\\\\leftrightarrow$\\\\emph{OtherScientificTerm} (60 of 245 affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.\\n    10\\tAblation cleanly attributes CF to the semantic layer: grammar-only decoding yields CF\\\\,=\\\\,0.08\\\\%, matching the unconstrained baseline, while the full system reaches 9.90\\\\% on SciERC and 2.57\\\\% on DocRED (Qwen3-8B; 12.02\\\\% DocRED for Llama-3.1-8B), confirming that CF arises from per-relation independent enforcement where each relation's constraint mask is computed without access to type decisions made for other relations (extended analysis in Appendix~\\\\ref{app:discussion}).\\n    11\\t% exp_ids: phase2_scierc_grammar_only, phase2_docred_full_s1, llama_docred_full_s1\\n    12\\t\\n    13\\t\\\\paragraph{Dataset-Dependent F1 Impact.}\\n    14\\t% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),\\n    15\\t%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\\n    16\\tThe divergence in F1 significance between DocRED ($+$0.50\\\\,pp, $p < 0.00
…[truncated 1814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T02:16:43.962737+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/section5_crossmodel_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/section5_crossmodel_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T02:16:43.962950+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t% Section 5 — Cross-Model Validation (compressed, 830→~400 words)\\n     2\\t% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,\\n     3\\t%          phase2_docred_unconstrained, phase2_docred_full_s1,\\n     4\\t%          llama_scierc_unconstrained, llama_scierc_full_s1,\\n     5\\t%          llama_docred_unconstrained, llama_docred_full_s1\\n     6\\t\\n     7\\t\\\\subsection{Cross-Model Validation}\\n     8\\t\\\\label{sec:cross-model}\\n     9\\t\\n    10\\tWe replicate the full S1 configuration with Llama-3.1-8B-Instruct under identical prompts, decoding parameters, and evaluation.\\n    11\\tTable~\\\\ref{tab:cross-model} summarizes results alongside Qwen3-8B.\\n    12\\t\\n    13\\t\\\\begin{table}[t]\\n    14\\t\\\\centering\\n    15\\t\\\\small\\n    16\\t\\\\setlength{\\\\tabcolsep}{3.4pt}\\n    17\\t\\\\resizebox{\\\\columnwidth}{!}{%\\n    18\\t\\\\begin{tabular}{@{}ll rrrr rr@{}}\\n    19\\t\\\\toprule\\n    20\\t& & \\\\multicolumn{4}{c}{\\\\textbf{Violation Rates (\\\\%)}}\\n    21\\t& \\\\multicolumn{2}{c}{\\\\textbf{F1}} \\\\\\\\\\n    22\\t\\\\cmidrule(lr){3-6} \\\\cmidrule(l){7-8}\\n    23\\t\\\\textbf{Dataset} & \\\\textbf{Model}\\n    24\\t  & DR\\\\,$\\\\downarrow$ & RV\\\\,$\\\\downarrow$ & ET\\\\,$\\\\downarrow$ & CF\\n    25\\t  & Rel. & Ent. \\\\\\\\\\n    26\\t\\\\midrule\\n    27\\t\\\\multirow{4}{*}{SciERC}\\n    28\\t  & Qwen (U)  & 15.37 & 1.39 & 0.40 & 0.08 & 8.23 & 31.01 \\\\\\\\\\n    29\\t  & Qwen (S1) &  0.93 & 0    & 0    & 9.90 & 8.36 & 30.98 \\\\\\\\\\n    30\\t  \\\\cmidrule(l){2-8}\\n    31\\t  & Llama (U)  & 13.34 & 0.55 & 0    & 0.24 & 2.68 & 23.56 \\\\\\\\\\n    32\\t  & Llama (S1) &  0.08 & 0    & 0    & 6.56 & 2.54 & 23.49 \\\\\\\\\\n    33\\t\\\\midrule\\n    34\\t\\\\multirow{4}{*}{DocRED}\\n    35\\t  & Qwen (U)  & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 & 58.15 \\\\\\\\\\n    36\\t  & Qwen (S1) & 10.21 &  0.03 & 0    & 2.57 & 8.23 & 59.37 \\\\\
…[truncated 3674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T02:16:43.963137+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/appendix_discussion.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/appendix_discussion.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T02:16:43.963346+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t% Appendix B — Extended Discussion\\n     2\\t% Contains discussion paragraphs moved from the main text during compression.\\n     3\\t\\n     4\\t\\\\section{Extended Discussion}\\\\label{app:discussion}\\n     5\\t\\n     6\\t%%% Paragraph 1: Low F1 Practical Significance %%%\\n     7\\t% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),\\n     8\\t%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)\\n     9\\t\\n    10\\t\\\\paragraph{Practical Significance of Zero-Shot F1.}\\n    11\\tOur reported relation F1 of approximately 8\\\\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.\\n    12\\tFor reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\\\\% relation F1 with full training data~\\\\citep{zhong2021frustratingly,ye2022packed}.\\n    13\\tConstraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.\\n    14\\tWhen applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\\\\% DR on SciERC, 18.46\\\\% on DocRED).\\n    15\\t% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained\\n    16\\tIn our evaluation, F1 serves as a \\\\emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.\\n    17\\tThe contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.\\n    18\\t\\n    19\\t%%% Paragraph 4: Decoding-Time vs. Post-H
…[truncated 5130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T02:16:43.963497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat -n /root/schema_semantic_constrained_ie/paper/main.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat -n /root/schema_semantic_constrained_ie/paper/main.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T02:16:43.963736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\documentclass[11pt]{article}\\n     2\\t\\n     3\\t\\\\usepackage[review]{acl}\\n     4\\t\\n     5\\t\\\\usepackage{times}\\n     6\\t\\\\usepackage{latexsym}\\n     7\\t\\\\usepackage[T1]{fontenc}\\n     8\\t\\\\usepackage[utf8]{inputenc}\\n     9\\t\\\\usepackage{microtype}\\n    10\\t\\\\usepackage{graphicx}\\n    11\\t\\\\usepackage{booktabs}\\n    12\\t\\\\usepackage{multirow}\\n    13\\t\\\\usepackage{amsmath}\\n    14\\t\\\\usepackage{amssymb}\\n    15\\t\\\\usepackage{enumitem}\\n    16\\t\\\\usepackage{xcolor}\\n    17\\t\\n    18\\t\\\\title{OntoCoDec: Type-Valid Information Extraction\\\\\\\\via Compiled Ontology Constraints}\\n    19\\t\\n    20\\t\\\\author{Anonymous ACL submission}\\n    21\\t\\n    22\\t\\\\begin{document}\\n    23\\t\\\\maketitle\\n    24\\t\\n    25\\t% === Abstract ===\\n    26\\t\\\\input{abstract}\\n    27\\t\\n    28\\t% === §1 Introduction ===\\n    29\\t\\\\input{section1_introduction_draft}\\n    30\\t\\n    31\\t% === §2 Background ===\\n    32\\t\\\\input{section2_background}\\n    33\\t\\n    34\\t% === §3 Method ===\\n    35\\t\\\\input{section3_method_draft}\\n    36\\t\\n    37\\t% === §4 Constraint Composition ===\\n    38\\t\\\\section{Constraint Composition}\\n    39\\t\\\\label{sec:composition}\\n    40\\t\\\\input{section4_composition_draft}\\n    41\\t\\n    42\\t% === §5 Experiments ===\\n    43\\t\\\\section{Experiments}\\n    44\\t\\\\label{sec:experiments}\\n    45\\t\\n    46\\t\\\\subsection{Violation Landscape}\\n    47\\t\\\\input{section3_violation_landscape}\\n    48\\t\\n    49\\t\\\\input{section5_scierc_draft}\\n    50\\t\\\\input{section5_docred_draft}\\n    51\\t\\\\input{section5_crossmodel_draft}\\n    52\\t\\\\input{section5_composability}\\n    53\\t\\n    54\\t% === §6 Related Work ===\\n    55\\t\\\\input{section6_related_work}\\n    56\\t\\n    57\\t% === §7 Discussion and Conclusion ===\\n    58\\t\\\\section{Discussion a
…[truncated 2560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T02:16:43.963948+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n -i \"composab\\|fine-tun.*constrain\\|LoRA.*constrain\\|FT.*constrain\\|constrain.*fine-tun\\|constrain.*LoRA\\|constrain.*FT\\|tab:composab\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -n -i \"composab\\|fine-tun.*constrain\\|LoRA.*constrain\\|FT.*constrain\\|constrain.*fine-tun\\|constrain.*LoRA\\|constrain.*FT\\|tab:composab\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T02:16:43.964092+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:16:43.964217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn -i \"composab\\|tab:composab\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn -i \"composab\\|tab:composab\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T02:16:43.964342+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T02:16:43.964528+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"composab\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"composab\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T02:16:43.964754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/abstract.tex:5:We present \\\\textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:\\n/root/schema_semantic_constrained_ie/paper/main.tex:52:\\\\input{section5_composability}\\n/root/schema_semantic_constrained_ie/paper/main.tex:65:The semantic layer introduces cross-field consistency (CF) violations (up to 12.02\\\\%) under zero-shot prompting, a systematic consequence of per-relation independent enforcement that remains an open challenge; this rate falls to $\\\\leq$1.18\\\\% once the base model is LoRA fine-tuned (Table~\\\\ref{tab:composability}).\\n/root/schema_semantic_constrained_ie/paper/section1_introduction_draft.tex:17:We propose \\\\textbf{OntoCoDec} (\\\\textbf{Onto}logy-\\\\textbf{Co}mpiled \\\\textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.\\n/root/schema_semantic_constrained_ie/paper/section6_related_work.tex:20:OntoCoDec provides complementary \\\\emph{hard} enforcement that is training-free and composable with these methods.\\n/root/schema_semantic_constrained_ie/paper/appendix_related_work.tex:65:OntoCoDec provides \\\\emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these training-based approaches.\\n/root/schema_semantic_constrained_ie/paper/abstract_fd4b26.tex:9:We present \\\\textsc{OntoCoDec}, which automatically compiles IE ontology schemas into two composable constraint layers for autoregressive decoding:\\n/root/schema_semantic_constrained_ie/paper/abstract_d3264e.tex:9:We present \\\\textsc{OntoCoDec}, which automatically compiles IE ontology schemas into two composable constraint layers for autoregressive decoding:\\n/root/schema_semantic_constrained_ie/paper/section6_relwork_outline.tex:79:\\\\textbf{Distinction:} Training-based methods provi
…[truncated 1378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T02:16:43.964914+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"tab:composab\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"tab:composab\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T02:16:43.965052+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/main.tex:65:The semantic layer introduces cross-field consistency (CF) violations (up to 12.02\\\\%) under zero-shot prompting, a systematic consequence of per-relation independent enforcement that remains an open challenge; this rate falls to $\\\\leq$1.18\\\\% once the base model is LoRA fine-tuned (Table~\\\\ref{tab:composability}).\\n/root/schema_semantic_constrained_ie/paper/main.aux:680:\\\\newlabel{tab:composability}{{5}{7}{Composability with fine-tuning on SciERC (551 documents). U: unconstrained; S1: full two-layer decoding. LoRA $r{=}16$, $\\\\alpha {=}32$, all-linear targets, 3 epochs, effective batch 16. F1 $\\\\times $100. RV and ET are 0\\\\,\\\\% in every constrained row and are omitted for space.\\\\relax }{table.caption.39}{}}\\n/root/schema_semantic_constrained_ie/paper/section5_composability.tex:50:\\\\label{tab:composability}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T02:16:43.965188+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"composab\\|fine-tun\\|LoRA\\|DocRED.*fine\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -n \"composab\\|fine-tun\\|LoRA\\|DocRED.*fine\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T02:16:43.965313+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T02:16:43.965431+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"composab\\|fine-tun\\|DocRED.*LoRA\\|TBD\" /root/schema_semantic_constrained_ie/paper/section7_conclusion_compressed.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -n \"composab\\|fine-tun\\|DocRED.*LoRA\\|TBD\" /root/schema_semantic_constrained_ie/paper/section7_conclusion_compressed.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T02:16:43.965552+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T02:16:43.965699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"composab\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -n \"composab\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T02:16:43.965826+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"fine-tun\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -n \"fine-tun\" /root/schema_semantic_constrained_ie/paper/section5_docred_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T02:16:43.965942+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"TBD\" /root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -n \"TBD\" /root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T02:16:43.966059+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T02:16:43.966181+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T02:16:43.966296+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"DocRED.*fine-tun\\|fine-tun.*DocRED\\|DocRED.*LoRA\\|LoRA.*DocRED\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"DocRED.*fine-tun\\|fine-tun.*DocRED\\|DocRED.*LoRA\\|LoRA.*DocRED\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T02:16:43.966414+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"119:DocRED & 96 & 18.7 & 28.9 & 7.5 & \\\\textit{TBD} & \\\\textit{TBD} \\\\\\\\\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T02:16:43.966527+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T02:16:43.966653+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"DocRED.*LoRA\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"DocRED.*LoRA\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T02:16:43.966796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/main.tex:69:Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T02:16:43.966913+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"DocRED fine\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"DocRED fine\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T02:16:43.967031+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/main.tex:69:Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T02:16:43.967150+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"not reported\\|in progress\\|pending\\|still running\\|RUNNING\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"not reported\\|in progress\\|pending\\|still running\\|RUNNING\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T02:16:43.967267+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T02:16:43.967378+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"not reported\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"not reported\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T02:16:43.967493+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/main.tex:69:Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T02:16:43.967607+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"pending\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"pending\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T02:16:43.967747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/abstract.tex:11:On DocRED, violations decrease by 45--90\\\\% depending on the model, with significant relation F1 gains for both Qwen3-8B ({+}0.50pp, $p{<}0.001$) and Llama-3.1-8B ({+}0.29pp, $p{=}0.013$; DR$\\\\downarrow$90.2\\\\%).\\n/root/schema_semantic_constrained_ie/paper/appendix_related_work.tex:85:Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec substantially reduces violations (DR$\\\\downarrow$94\\\\% on SciERC, $\\\\downarrow$45--90\\\\% on DocRED depending on model).\\n/root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex:112:DocRED S1 results are pending (experiment in progress).}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T02:16:43.967869+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"RUNNING\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"RUNNING\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T02:16:43.967988+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex:128:DocRED S1 = \\\\texttt{phase2\\\\_docred\\\\_full\\\\_s1} (RUNNING).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T02:16:43.968108+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -rn \"TBD\" /root/schema_semantic_constrained_ie/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "grep -rn \"TBD\" /root/schema_semantic_constrained_ie/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T02:16:43.968226+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/paper/paper_tables_draft.tex:119:DocRED & 96 & 18.7 & 28.9 & 7.5 & \\\\textit{TBD} & \\\\textit{TBD} \\\\\\\\\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T02:16:43.968443+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "memory.md",
  "content": "# Composability 数字更新清单\n\n## 待 DocRED constrained eval 结果后更新\n\n依赖实验：`w5_qwen_docred_lora_constrained_eval` / `w5_llama_docred_lora_constrained_eval`（及对应的 unconstrained baseline `w5_qwen_docred_lora_unconstrained_eval` / `w5_llama_docred_lora_unconstrained_eval`）\n\n---\n\n### 1. [section5_composability.tex:18-51] Table 5 (tab:composability) — 仅含 SciERC，需加 DocRED 行\n\n- **当前值**: 8 行数据（2 models × {ZS, LoRA} × {U, S1}），全部 SciERC\n- **需要更新为**: 新增 DocRED 块（至少 4 行：2 models × {LoRA-U, LoRA-S1}；或 8 行含 ZS-DocRED 作对照）\n- **需要的数字**: DocRED FT-unconstrained DR/CF/R-F1/E-F1（两模型）、DocRED FT-S1 DR/CF/R-F1/E-F1（两模型）\n- **表格 caption (line 45-49)** 也需从 \"on SciERC (551 documents)\" 改为 \"on SciERC (551) and DocRED (998 documents)\"\n\n### 2. [section5_composability.tex:14-16] 实验描述 — SciERC-only 措辞\n\n- **当前值**: `\"We test this by LoRA fine-tuning both Qwen3-8B and Llama-3.1-8B on SciERC and then evaluating each fine-tuned model with and without the two-layer constraints\"`\n- **需要更新为**: \"...on SciERC and DocRED...\" 或分段描述两个数据集\n- **行号**: 14-16\n\n### 3. [section5_composability.tex:53-68] ¶ \"Fine-tuning does not eliminate violations\" — 所有数字仅 SciERC\n\n- **line 54-56**: `\"lifts relation F1 from 8.23 to 43.86 (Qwen) and from 2.68 to 45.45 (Llama)---a 35--43pp gain\"` — 需加 DocRED FT F1 数字\n- **line 58**: `\"residual domain/range violations persist at 1.95% (Qwen) and 1.11% (Llama)\"` — 需加 DocRED FT DR baseline\n- **line 60-62**: `\"Evaluate-for retains 13.1% DR for the fine-tuned Qwen model despite achieving zero on six of the other seven relations\"` — SciERC per-relation analysis，DocRED 是否有类似 tight-constraint relation 残留需分析\n- **整段策略**: 可扩展为 \"On SciERC, ... On DocRED, ...\" 两段式；或保留 SciERC 正文 + DocRED 表格引用\n\n### 4. [section5_composability.tex:70-86] ¶ \"Constraints compose with fine-tuning at no F1 cost\" — 所有数字仅 SciERC\n\n- **line 72-73**: `\"eliminates residual DR almost entirely (Qwen 1.95%→0.00%, Llama 1.11%→0.09%)\"` — 需加 DocRED FT-U→FT-S1 DR 变化\n- **line 73-74**: `\"relation F1 changes by less than 0.1pp (−0.09pp Qwen, +0.02pp Llama)\"` — 需加 DocRED R-F1 delta\n- **line 74-75**: `\"entity F1 is identical to the fine-tuned unconstrained baseline in both cases\"` — 需验证 DocRED 是否同样成立\n- **line 81-82**: `\"CF rate at the fine-tuned regime is also markedly lower (1.18% Qwen, 0.46% Llama vs. 9.90% and 6.56%)\"` — 需加 DocRED FT CF 数字\n- **整段需要判断**: DocRED FT+S1 是否同样 \"no F1 cost\"？如果 DocRED FT DR 残留更高（类似 ZS 模式），段落 claim 需 nuance\n\n### 5. [section5_composability.tex:88-98] ¶ \"Implication\" — 定性 claim，可能需强化或限定\n\n- **当前值**: 通用性 claim \"Fine-tuning and decoding-time enforcement are complementary, not substitutable\"\n- **需要更新为**: 如果 DocRED 结果一致，claim 可保持不变（evidence 更强）；如果 DocRED FT 消除了大部分 violations（DR→<0.5%），可能需 nuance \"constraints are most needed when FT data does not cover the full relation distribution\"\n- **无硬数字需替换**，但逻辑可能需调整\n\n### 6. [main.tex:65] Limitations — CF under fine-tuning 数字\n\n- **当前值**: `\"this rate falls to $\\leq$1.18\\% once the base model is LoRA fine-tuned (Table~\\ref{tab:composability})\"`\n- **需要更新为**: 如果 DocRED FT CF 更高，需改为 DocRED+SciERC 范围，如 `\"falls to X--1.18%\"`；如果 DocRED FT CF 也很低，可保持\n- **关键**: 当前 1.18% 是 SciERC Qwen FT S1 的 CF。DocRED ZS CF 本就更低（2.57% Qwen），FT 后可能更低——但需实验确认\n\n### 7. [main.tex:69] Limitations — \"DocRED fine-tuning is not reported\" 需删除\n\n- **当前值**: `\"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time).\"`\n- **需要更新为**: 删除 \"DocRED fine-tuning is not reported...\" 半句，改为 \"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings.\" 或类似表述\n- **line 69**: 这是 Limitations 中最显眼的\"缺失实验\"声明，必须在结果到手后第一时间修改\n\n### 8. [paper_tables_draft.tex:112,119,128] Table 4 (cross-dataset) — TBD 占位符\n\n- **line 119**: `DocRED & 96 & 18.7 & 28.9 & 7.5 & \\textit{TBD} & \\textit{TBD}`\n- **line 112**: caption 写 \"DocRED S1 results are pending (experiment in progress)\"\n- **line 128**: exp ID 注释写 \"(RUNNING)\"\n- **⚠️ 注意**: 此文件未被 main.tex `\\input`，是独立草稿。cross-model table (section5_crossmodel_draft.tex) 已有 DocRED ZS S1 数字。此文件可能已废弃，但仍应更新或标注弃用。\n\n### 9. [appendix_discussion.tex:13-17] ¶ \"Practical Significance\" — fine-tuning 泛指\n\n- **当前值**: `\"When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase 0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37% DR on SciERC, 18.46% on DocRED).\"`\n- **无需硬数字更新**（引用的是 Phase 0 ZS baseline），但如果添加 DocRED FT composability 数据，可在此段补充一句 DocRED FT 的 evidence\n- **优先级**: 低\n\n### 10. [section6_related_work.tex:20] & [appendix_related_work.tex:65] — \"composable\" 泛指\n\n- **当前值**: \"training-free and composable with these methods\" / \"composable with any of these training-based approaches\"\n- **无数字，无需更新**。DocRED FT 结果出来后这些 claim 的 evidence base 变强，但文本无需改动。\n- **优先级**: 无\n\n---\n\n## 更新优先级\n\n| 优先级 | 项目 | 原因 |\n|--------|------|------|\n| P0 | #1 Table 5 加 DocRED 行 | 核心数据表，composability claim 的直接 evidence |\n| P0 | #7 删除 \"DocRED not reported\" | Limitations 中的 gap 声明，有结果后必须删 |\n| P1 | #2 实验描述改 \"SciERC and DocRED\" | 与 Table 一致性 |\n| P1 | #4 \"no F1 cost\" 段加 DocRED 数字 | 核心 claim 的量化支撑 |\n| P1 | #3 \"FT does not eliminate violations\" 段 | 支持 claim 的 evidence 扩展 |\n| P1 | #6 Limitations CF 数字范围 | 准确性 |\n| P2 | #5 Implication 段 | 看结果决定是否调整 |\n| P2 | #8 paper_tables_draft.tex TBD | 已非编译文件，低优先级 |\n| P3 | #9 Appendix discussion | 可选补充 |\n| P3 | #10 Related work | 无需改动 |\n\n## 数据需求汇总\n\n从 DocRED FT 实验中需提取的数字（每个模型 × {unconstrained, S1}）：\n\n| 指标 | Qwen FT-U | Qwen FT-S1 | Llama FT-U | Llama FT-S1 |\n|------|-----------|------------|------------|-------------|\n| DR (%) | ? | ? | ? | ? |\n| RV (%) | ? | ? | ? | ? |\n| ET (%) | ? | ? | ? | ? |\n| CF (%) | ? | ? | ? | ? |\n| R-F1 (×100) | ? | ? | ? | ? |\n| E-F1 (×100) | ? | ? | ? | ? |\n| Parse failures | ? | ? | ? | ? |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "memory.md",
    "content": "# Composability 数字更新清单\n\n## 待 DocRED constrained eval 结果后更新\n\n依赖实验：`w5_qwen_docred_lora_constrained_eval` / `w5_llama_docred_lora_constrained_eval`（及对应的 unconstrained baseline `w5_qwen_docred_lora_unconstrained_eval` / `w5_llama_docred_lora_unconstrained_eval`）\n\n---\n\n### 1. [section5_composability.tex:18-51] Table 5 (tab:composability) — 仅含 SciERC，需加 DocRED 行\n\n- **当前值**: 8 行数据（2 models × {ZS, LoRA} × {U, S1}），全部 SciERC\n- **需要更新为**: 新增 DocRED 块（至少 4 行：2 models × {LoRA-U, LoRA-S1}；或 8 行含 ZS-DocRED 作对照）\n- **需要的数字**: DocRED FT-unconstrained DR/CF/R-F1/E-F1（两模型）、DocRED FT-S1 DR/CF/R-F1/E-F1（两模型）\n- **表格 caption (line 45-49)** 也需从 \"on SciERC (551 documents)\" 改为 \"on SciERC (551) and DocRED (998 documents)\"\n\n### 2. [section5_composability.tex:14-16] 实验描述 — SciERC-only 措辞\n\n- **当前值**: `\"We test this by LoRA fine-tuning both Qwen3-8B and Llama-3.1-8B on SciERC and then evaluating each fine-tuned model with and without the two-layer constraints\"`\n- **需要更新为**: \"...on SciERC and DocRED...\" 或分段描述两个数据集\n- **行号**: 14-16\n\n### 3. [section5_composability.tex:53-68] ¶ \"Fine-tuning does not eliminate violations\" — 所有数字仅 SciERC\n\n- **line 54-56**: `\"lifts relation F1 from 8.23 to 43.86 (Qwen) and from 2.68 to 45.45 (Llama)---a 35--43pp gain\"` — 需加 DocRED FT F1 数字\n- **line 58**: `\"residual domain/range violations persist at 1.95% (Qwen) and 1.11% (Llama)\"` — 需加 DocRED FT DR baseline\n- **line 60-62**: `\"Evaluate-for retains 13.1% DR for the fine-tuned Qwen model despite achieving zero on six of the other seven relations\"` — SciERC per-relation analysis，DocRED 是否有类似 tight-constraint relation 残留需分析\n- **整段策略**: 可扩展为 \"On SciERC, ... On DocRED, ...\" 两段式；或保留 SciERC 正文 + DocRED 表格引用\n\n### 4. [section5_composability.tex:70-86] ¶ \"Constraints compose with fine-tuning at no F1 cost\" — 所有数字仅 SciERC\n\n- **line 72-73**: `\"eliminates residual DR almost entirely (Qwen 1.95%→0.00%, Llama 1.11%→0.09%)\"` — 需加 DocRED FT-U→FT-S1 DR 变化\n- **line 73-74**: `\"relation F1 changes by less than 0.1pp (−0.09pp Qwen, +0.02pp Llama)\"` — 需加 DocRED R-F1 delta\n- **line 74-75**: `\"entity F1 is identical to the fine-tuned unconstrained baseline in both cases\"` — 需验证 DocRED 是否同样成立\n- **line 81-82**: `\"CF rate at the fine-tuned regime is also markedly lower (1.18% Qwen, 0.46% Llama vs. 9.90% and 6.56%)\"` — 需加 DocRED FT CF 数字\n- **整段需要判断**: DocRED FT+S1 是否同样 \"no F1 cost\"？如果 DocRED FT DR 残留更高（类似 ZS 模式），段落 claim 需 nuance\n\n### 5. [section5_composability.tex:88-98] ¶ \"Implication\" — 定性 claim，可能需强化或限定\n\n- **当前值**: 通用性 claim \"Fine-tuning and decoding-time enforcement are complementary, not substitutable\"\n- **需要更新为**: 如果 DocRED 结果一致，claim 可保持不变（evidence 更强）；如果 DocRED FT 消除了大部分 violations（DR→<0.5%），可能需 nuance \"constraints are most needed when FT data does not cover the full relation distribution\"\n- **无硬数字需替换**，但逻辑可能需调整\n\n### 6. [main.tex:65] Limitations — CF under fine-tuning 数字\n\n- **当前值**: `\"this rate falls to $\\leq$1.18\\% once the base model is LoRA fine-tuned (Table~\\ref{tab:composability})\"`\n- **需要更新为**: 如果 DocRED FT CF 更高，需改为 DocRED+SciERC 范围，如 `\"falls to X--1.18%\"`；如果 DocRED FT CF 也很低，可保持\n- **关键**: 当前 1.18% 是 SciERC Qwen FT S1 的 CF。DocRED ZS CF 本就更低（2.57% Qwen），FT 后可能更低——但需实验确认\n\n### 7. [main.tex:69] Limitations — \"DocRED fine-tuning is not reported\" 需删除\n\n- **当前值**: `\"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time).\"`\n- **需要更新为**: 删除 \"DocRED fine-tuning is not reported...\" 半句，改为 \"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings.\" 或类似表述\n- **line 69**: 这是 Limitations 中最显眼的\"缺失实验\"声明，必须在结果到手后第一时间修改\n\n### 8. [paper_tables_draft.tex:112,119,128] Table 4 (cross-dataset) — TBD 占位符\n\n- **line 119**: `DocRED & 96 & 18.7 & 28.9 & 7.5 & \\textit{TBD} & \\textit{TBD}`\n- **line 112**: caption 写 \"DocRED S1 results are pending (experiment in progress)\"\n- **line 128**: exp ID 注释写 \"(RUNNING)\"\n- **⚠️ 注意**: 此文件未被 main.tex `\\input`，是独立草稿。cross-model table (section5_crossmodel_draft.tex) 已有 DocRED ZS S1 数字。此文件可能已废弃，但仍应更新或标注弃用。\n\n### 9. [appendix_discussion.tex:13-17] ¶ \"Practical Significance\" — fine-tuning 泛指\n\n- **当前值**: `\"When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase 0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37% DR on SciERC, 18.46% on DocRED).\"`\n- **无需硬数字更新**（引用的是 Phase 0 ZS baseline），但如果添加 DocRED FT composability 数据，可在此段补充一句 DocRED FT 的 evidence\n- **优先级**: 低\n\n### 10. [section6_related_work.tex:20] & [appendix_related_work.tex:65] — \"composable\" 泛指\n\n- **当前值**: \"training-free and composable with these methods\" / \"composable with any of these training-based approaches\"\n- **无数字，无需更新**。DocRED FT 结果出来后这些 claim 的 evidence base 变强，但文本无需改动。\n- **优先级**: 无\n\n---\n\n## 更新优先级\n\n| 优先级 | 项目 | 原因 |\n|--------|------|------|\n| P0 | #1 Table 5 加 DocRED 行 | 核心数据表，composability claim 的直接 evidence |\n| P0 | #7 删除 \"DocRED not reported\" | Limitations 中的 gap 声明，有结果后必须删 |\n| P1 | #2 实验描述改 \"SciERC and DocRED\" | 与 Table 一致性 |\n| P1 | #4 \"no F1 cost\" 段加 DocRED 数字 | 核心 claim 的量化支撑 |\n| P1 | #3 \"FT does not eliminate violations\" 段 | 支持 claim 的 evidence 扩展 |\n| P1 | #6 Limitations CF 数字范围 | 准确性 |\n| P2 | #5 Implication 段 | 看结果决定是否调整 |\n| P2 | #8 paper_tables_draft.tex TBD | 已非编译文件，低优先级 |\n| P3 | #9 Appendix discussion | 可选补充 |\n| P3 | #10 Related work | 无需改动 |\n\n## 数据需求汇总\n\n从 DocRED FT 实验中需提取的数字（每个模型 × {unconstrained, S1}）：\n\n| 指标 | Qwen FT-U | Qwen FT-S1 | Llama FT-U | Llama FT-S1 |\n|------|-----------|------------|------------|-------------|\n| DR (%) | ? | ? | ? | ? |\n| RV (%) | ? | ? | ? | ? |\n| ET (%) | ? | ? | ? | ? |\n| CF (%) | ? | ? | ? | ? |\n| R-F1 (×100) | ? | ? | ? | ? |\n| E-F1 (×100) | ? | ? | ? | ? |\n| Parse failures | ? | ? | ? | ? |\n"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T02:16:43.968717+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T02:16:43.968893+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "memory.md",
  "max_chars": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "memory.md",
    "max_chars": "500"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T02:16:43.969041+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"content\": \"# Composability 数字更新清单\\n\\n## 待 DocRED constrained eval 结果后更新\\n\\n依赖实验：`w5_qwen_docred_lora_constrained_eval` / `w5_llama_docred_lora_constrained_eval`（及对应的 unconstrained baseline `w5_qwen_docred_lora_unconstrained_eval` / `w5_llama_docred_lora_unconstrained_eval`）\\n\\n---\\n\\n### 1. [section5_composability.tex:18-51] Table 5 (tab:composability) — 仅含 SciERC，需加 DocRED 行\\n\\n- **当前值**: 8 行数据（2 models × {ZS, LoRA} × {U, S1}），全部 SciERC\\n- **需要更新为**: 新增 DocRED 块（至少 4 行：2 models × {LoRA-U, LoRA-S1}；或 8 行含 ZS-DocRED 作\\n\\n... [截断: 省略 5324 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 5824, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T02:16:43.969189+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T02:16:43.969323+00:00_

_project
analyze_ontology_docred.py
cf_fallback_code_diff_analysis.md
compare_prompts.py
constrained_eval_readiness.md
cross_model_analysis_framework.md
d009_llama_prep.md
docred_full_s1_dr_root_cause_analysis.md
docred_lora_eval_commands.md
docred_phase2_ablation_analysis.md
docred_progress_check.md
dream_reports
dual_factor_analysis
impact_analysis.py
literature_docred_compare.md
literature_map.yaml
literature_survey_constrained_decoding_ie.md
literature_survey_ontology_constrained_ie.md
llama_docred_full_s1
llama_docred_full_s1_mt6144
llama_docred_maxtoken
llama_docred_per_relation_dr_analysis.md
llama_docred_unconstrained_mt6144
llama_submit_commands.md
manifest.yaml
method_invariant_notes.md
pair_based_enforcement_plan.md
paper_number_consistency_check.md
paper_results_summary.md
paper_writing_readiness.md
phase2_docred_full_s1
phase2_docred_semantic_only
rebuttal
reference_audit_relwork.md
reference_audit_results.md
related_work_survey.md
review_issues.yaml
review_reports
run_constrained_extraction.py
run_extraction_docred.py
runtime_benchmark.json
tightness_ablation
unified_et_dr_recalc.md
violation_checker_docred.py
w1_cf_fallback
w1_cf_fallback_pilot_detailed_analysis.md
w1_cf_fallback_scierc_pilot
w4_table1_v2
w5_docred_sft_data_gen
w5_llama_docred_lora_training
w5_llama_lora_scierc_constrained_eval
w5_lora_scierc_training

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T02:16:43.969478+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/composability_update_checklist.md",
  "content": "# Composability 数字更新清单\n\n## 待 DocRED constrained eval 结果后更新\n\n依赖实验：`w5_qwen_docred_lora_constrained_eval` / `w5_llama_docred_lora_constrained_eval`（及对应的 unconstrained baseline `w5_qwen_docred_lora_unconstrained_eval` / `w5_llama_docred_lora_unconstrained_eval`）\n\n---\n\n### 1. [section5_composability.tex:18-51] Table 5 (tab:composability) — 仅含 SciERC，需加 DocRED 行\n\n- **当前值**: 8 行数据（2 models × {ZS, LoRA} × {U, S1}），全部 SciERC\n- **需要更新为**: 新增 DocRED 块（至少 4 行：2 models × {LoRA-U, LoRA-S1}；或 8 行含 ZS-DocRED 作对照）\n- **需要的数字**: DocRED FT-unconstrained DR/CF/R-F1/E-F1（两模型）、DocRED FT-S1 DR/CF/R-F1/E-F1（两模型）\n- **表格 caption (line 45-49)** 也需从 \"on SciERC (551 documents)\" 改为 \"on SciERC (551) and DocRED (998 documents)\"\n- **占位符**: 无 TBD，但整个 DocRED 块缺失\n\n### 2. [section5_composability.tex:14-16] 实验描述 — SciERC-only 措辞\n\n- **当前值**: `\"We test this by LoRA fine-tuning both Qwen3-8B and Llama-3.1-8B on SciERC and then evaluating each fine-tuned model with and without the two-layer constraints\"`\n- **需要更新为**: \"...on SciERC and DocRED...\" 或分段描述两个数据集\n- **行号**: 14-16\n\n### 3. [section5_composability.tex:53-68] ¶ \"Fine-tuning does not eliminate violations\" — 所有数字仅 SciERC\n\n- **line 54-56**: `\"lifts relation F1 from 8.23 to 43.86 (Qwen) and from 2.68 to 45.45 (Llama)---a 35--43pp gain\"` — 需加 DocRED FT F1 数字\n- **line 58**: `\"residual domain/range violations persist at 1.95% (Qwen) and 1.11% (Llama)\"` — 需加 DocRED FT DR baseline\n- **line 60-62**: `\"Evaluate-for retains 13.1% DR for the fine-tuned Qwen model despite achieving zero on six of the other seven relations\"` — SciERC per-relation analysis；DocRED 是否有类似 tight-constraint relation 残留需分析\n- **整段策略**: 可扩展为 \"On SciERC, ... On DocRED, ...\" 两段式；或保留 SciERC 正文 + DocRED 表格引用\n\n### 4. [section5_composability.tex:70-86] ¶ \"Constraints compose at no F1 cost\" — 所有数字仅 SciERC\n\n- **line 72-73**: `\"eliminates residual DR almost entirely (Qwen 1.95%→0.00%, Llama 1.11%→0.09%)\"` — 需加 DocRED FT-U→FT-S1 DR 变化\n- **line 73-74**: `\"relation F1 changes by less than 0.1pp (−0.09pp Qwen, +0.02pp Llama)\"` — 需加 DocRED R-F1 delta\n- **line 74-75**: `\"entity F1 is identical to the fine-tuned unconstrained baseline in both cases\"` — 需验证 DocRED 是否同样成立\n- **line 81-82**: `\"CF rate at the fine-tuned regime is also markedly lower (1.18% Qwen, 0.46% Llama vs. 9.90% and 6.56%)\"` — 需加 DocRED FT CF 数字\n- **⚠️ 关键判断**: DocRED FT+S1 是否同样 \"no F1 cost\"？如果 DocRED FT DR 残留更高（类似 ZS 模式），段落 claim 需 nuance\n\n### 5. [section5_composability.tex:88-98] ¶ \"Implication\" — 定性 claim\n\n- **当前值**: 通用 claim \"Fine-tuning and decoding-time enforcement are complementary, not substitutable\"\n- **无硬数字需替换**，但如果 DocRED FT 消除了大部分 violations（DR→<0.5%），需 nuance \"constraints are most needed when FT data does not cover the full relation distribution\"\n- **优先级**: 看结果再定\n\n### 6. [main.tex:65] Limitations — CF under fine-tuning 数字\n\n- **当前值**: `\"this rate falls to $\\leq$1.18\\% once the base model is LoRA fine-tuned (Table~\\ref{tab:composability})\"`\n- **需要更新为**: 如果 DocRED FT CF 更高，需改为范围如 `\"falls to X--Y%\"`；如果也很低可保持\n- **关键**: 当前 1.18% 是 SciERC Qwen FT S1 的 CF\n\n### 7. [main.tex:69] Limitations — \"DocRED fine-tuning is not reported\" ⬅️ 必须删除\n\n- **当前值**: `\"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time).\"`\n- **需要更新为**: 删除 \"DocRED fine-tuning is not reported...\" 半句，改为 \"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings.\"\n- **这是 Limitations 中最显眼的\"缺失实验\"声明，有结果后必须第一时间修改**\n\n### 8. [paper_tables_draft.tex:112,119,128] Table 4 (cross-dataset) — TBD 占位符\n\n- **line 119**: `DocRED & 96 & 18.7 & 28.9 & 7.5 & \\textit{TBD} & \\textit{TBD}`\n- **line 112**: caption 写 \"DocRED S1 results are pending (experiment in progress)\"\n- **line 128**: exp ID 注释写 \"(RUNNING)\"\n- **⚠️ 此文件未被 main.tex \\input，是独立草稿。** cross-model table (section5_crossmodel_draft.tex) 已有 DocRED ZS S1 数字（Qwen DR=10.21, Llama DR=2.55）。此文件可清理或标注弃用。\n- **优先级**: 低（不影响编译产出）\n\n### 9. [appendix_discussion.tex:13-17] ¶ \"Practical Significance\" — fine-tuning 泛指\n\n- **当前值**: `\"When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary\"`\n- **无硬数字需更新**（引用的是 Phase 0 ZS baseline 15.37%/18.46%）\n- **可选**: 添加一句 DocRED FT evidence 强化论点\n- **优先级**: 低\n\n### 10. [section6_related_work.tex:20] & [appendix_related_work.tex:65] — \"composable\" 泛指\n\n- 无数字，无需更新。DocRED FT 结果出来后 evidence base 变强但文本不变。\n- **优先级**: 无\n\n---\n\n## 更新优先级\n\n| 优先级 | 项目 | 原因 |\n|--------|------|------|\n| **P0** | #1 Table 5 加 DocRED 行 | 核心数据表，composability claim 的直接 evidence |\n| **P0** | #7 删除 \"DocRED not reported\" | Limitations 中的 gap 声明，有结果后必须删 |\n| P1 | #2 实验描述改 \"SciERC and DocRED\" | 与 Table 一致性 |\n| P1 | #4 \"no F1 cost\" 段加 DocRED 数字 | 核心 claim 的量化支撑 |\n| P1 | #3 \"FT does not eliminate violations\" 段 | 支持 claim 的 evidence 扩展 |\n| P1 | #6 Limitations CF 数字范围 | 准确性 |\n| P2 | #5 Implication 段 | 看结果决定是否调整 |\n| P2 | #8 paper_tables_draft.tex TBD | 已非编译文件，低优先级 |\n| P3 | #9 Appendix discussion | 可选补充 |\n| P3 | #10 Related work | 无需改动 |\n\n## 数据需求汇总\n\n从 DocRED FT 实验中需提取的数字（每个模型 × {unconstrained, S1}）：\n\n| 指标 | Qwen FT-U | Qwen FT-S1 | Llama FT-U | Llama FT-S1 |\n|------|-----------|------------|------------|-------------|\n| DR (%) | ? | ? | ? | ? |\n| RV (%) | ? | ? | ? | ? |\n| ET (%) | ? | ? | ? | ? |\n| CF (%) | ? | ? | ? | ? |\n| R-F1 (×100) | ? | ? | ? | ? |\n| E-F1 (×100) | ? | ? | ? | ? |\n| Parse failures | ? | ? | ? | ? |\n\n## 注意事项\n\n- DocRED ZS 数据已在 cross-model table (section5_crossmodel_draft.tex) 中，composability table 如果要加 ZS-DocRED 行，直接从那里取（Qwen U: DR=18.46, R-F1=7.74, E-F1=58.15; Qwen S1: DR=10.21, R-F1=8.23, E-F1=59.37; Llama U: DR=26.07, R-F1=5.98, E-F1=55.65; Llama S1: DR=2.55, R-F1=6.27, E-F1=55.01）\n- DocRED FT 的 DR reduction 可能比 SciERC FT 更复杂：ZS baseline Qwen DR=10.21%（S1）vs SciERC 0.93%，如果 FT baseline DR 也更高，FT+S1 的残留 DR 也可能更高\n- DocRED ontology 有 96 relations，FT 可能无法覆盖所有 long-tail relation 的 type constraint，tight-constraint 残留分析需要类似 SciERC Evaluate-for 的 per-relation breakdown\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/composability_update_checklist.md",
    "content": "# Composability 数字更新清单\n\n## 待 DocRED constrained eval 结果后更新\n\n依赖实验：`w5_qwen_docred_lora_constrained_eval` / `w5_llama_docred_lora_constrained_eval`（及对应的 unconstrained baseline `w5_qwen_docred_lora_unconstrained_eval` / `w5_llama_docred_lora_unconstrained_eval`）\n\n---\n\n### 1. [section5_composability.tex:18-51] Table 5 (tab:composability) — 仅含 SciERC，需加 DocRED 行\n\n- **当前值**: 8 行数据（2 models × {ZS, LoRA} × {U, S1}），全部 SciERC\n- **需要更新为**: 新增 DocRED 块（至少 4 行：2 models × {LoRA-U, LoRA-S1}；或 8 行含 ZS-DocRED 作对照）\n- **需要的数字**: DocRED FT-unconstrained DR/CF/R-F1/E-F1（两模型）、DocRED FT-S1 DR/CF/R-F1/E-F1（两模型）\n- **表格 caption (line 45-49)** 也需从 \"on SciERC (551 documents)\" 改为 \"on SciERC (551) and DocRED (998 documents)\"\n- **占位符**: 无 TBD，但整个 DocRED 块缺失\n\n### 2. [section5_composability.tex:14-16] 实验描述 — SciERC-only 措辞\n\n- **当前值**: `\"We test this by LoRA fine-tuning both Qwen3-8B and Llama-3.1-8B on SciERC and then evaluating each fine-tuned model with and without the two-layer constraints\"`\n- **需要更新为**: \"...on SciERC and DocRED...\" 或分段描述两个数据集\n- **行号**: 14-16\n\n### 3. [section5_composability.tex:53-68] ¶ \"Fine-tuning does not eliminate violations\" — 所有数字仅 SciERC\n\n- **line 54-56**: `\"lifts relation F1 from 8.23 to 43.86 (Qwen) and from 2.68 to 45.45 (Llama)---a 35--43pp gain\"` — 需加 DocRED FT F1 数字\n- **line 58**: `\"residual domain/range violations persist at 1.95% (Qwen) and 1.11% (Llama)\"` — 需加 DocRED FT DR baseline\n- **line 60-62**: `\"Evaluate-for retains 13.1% DR for the fine-tuned Qwen model despite achieving zero on six of the other seven relations\"` — SciERC per-relation analysis；DocRED 是否有类似 tight-constraint relation 残留需分析\n- **整段策略**: 可扩展为 \"On SciERC, ... On DocRED, ...\" 两段式；或保留 SciERC 正文 + DocRED 表格引用\n\n### 4. [section5_composability.tex:70-86] ¶ \"Constraints compose at no F1 cost\" — 所有数字仅 SciERC\n\n- **line 72-73**: `\"eliminates residual DR almost entirely (Qwen 1.95%→0.00%, Llama 1.11%→0.09%)\"` — 需加 DocRED FT-U→FT-S1 DR 变化\n- **line 73-74**: `\"relation F1 changes by less than 0.1pp (−0.09pp Qwen, +0.02pp Llama)\"` — 需加 DocRED R-F1 delta\n- **line 74-75**: `\"entity F1 is identical to the fine-tuned unconstrained baseline in both cases\"` — 需验证 DocRED 是否同样成立\n- **line 81-82**: `\"CF rate at the fine-tuned regime is also markedly lower (1.18% Qwen, 0.46% Llama vs. 9.90% and 6.56%)\"` — 需加 DocRED FT CF 数字\n- **⚠️ 关键判断**: DocRED FT+S1 是否同样 \"no F1 cost\"？如果 DocRED FT DR 残留更高（类似 ZS 模式），段落 claim 需 nuance\n\n### 5. [section5_composability.tex:88-98] ¶ \"Implication\" — 定性 claim\n\n- **当前值**: 通用 claim \"Fine-tuning and decoding-time enforcement are complementary, not substitutable\"\n- **无硬数字需替换**，但如果 DocRED FT 消除了大部分 violations（DR→<0.5%），需 nuance \"constraints are most needed when FT data does not cover the full relation distribution\"\n- **优先级**: 看结果再定\n\n### 6. [main.tex:65] Limitations — CF under fine-tuning 数字\n\n- **当前值**: `\"this rate falls to $\\leq$1.18\\% once the base model is LoRA fine-tuned (Table~\\ref{tab:composability})\"`\n- **需要更新为**: 如果 DocRED FT CF 更高，需改为范围如 `\"falls to X--Y%\"`；如果也很低可保持\n- **关键**: 当前 1.18% 是 SciERC Qwen FT S1 的 CF\n\n### 7. [main.tex:69] Limitations — \"DocRED fine-tuning is not reported\" ⬅️ 必须删除\n\n- **当前值**: `\"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time).\"`\n- **需要更新为**: 删除 \"DocRED fine-tuning is not reported...\" 半句，改为 \"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings.\"\n- **这是 Limitations 中最显眼的\"缺失实验\"声明，有结果后必须第一时间修改**\n\n### 8. [paper_tables_draft.tex:112,119,128] Table 4 (cross-dataset) — TBD 占位符\n\n- **line 119**: `DocRED & 96 & 18.7 & 28.9 & 7.5 & \\textit{TBD} & \\textit{TBD}`\n- **line 112**: caption 写 \"DocRED S1 results are pending (experiment in progress)\"\n- **line 128**: exp ID 注释写 \"(RUNNING)\"\n- **⚠️ 此文件未被 main.tex \\input，是独立草稿。** cross-model table (section5_crossmodel_draft.tex) 已有 DocRED ZS S1 数字（Qwen DR=10.21, Llama DR=2.55）。此文件可清理或标注弃用。\n- **优先级**: 低（不影响编译产出）\n\n### 9. [appendix_discussion.tex:13-17] ¶ \"Practical Significance\" — fine-tuning 泛指\n\n- **当前值**: `\"When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary\"`\n- **无硬数字需更新**（引用的是 Phase 0 ZS baseline 15.37%/18.46%）\n- **可选**: 添加一句 DocRED FT evidence 强化论点\n- **优先级**: 低\n\n### 10. [section6_related_work.tex:20] & [appendix_related_work.tex:65] — \"composable\" 泛指\n\n- 无数字，无需更新。DocRED FT 结果出来后 evidence base 变强但文本不变。\n- **优先级**: 无\n\n---\n\n## 更新优先级\n\n| 优先级 | 项目 | 原因 |\n|--------|------|------|\n| **P0** | #1 Table 5 加 DocRED 行 | 核心数据表，composability claim 的直接 evidence |\n| **P0** | #7 删除 \"DocRED not reported\" | Limitations 中的 gap 声明，有结果后必须删 |\n| P1 | #2 实验描述改 \"SciERC and DocRED\" | 与 Table 一致性 |\n| P1 | #4 \"no F1 cost\" 段加 DocRED 数字 | 核心 claim 的量化支撑 |\n| P1 | #3 \"FT does not eliminate violations\" 段 | 支持 claim 的 evidence 扩展 |\n| P1 | #6 Limitations CF 数字范围 | 准确性 |\n| P2 | #5 Implication 段 | 看结果决定是否调整 |\n| P2 | #8 paper_tables_draft.tex TBD | 已非编译文件，低优先级 |\n| P3 | #9 Appendix discussion | 可选补充 |\n| P3 | #10 Related work | 无需改动 |\n\n## 数据需求汇总\n\n从 DocRED FT 实验中需提取的数字（每个模型 × {unconstrained, S1}）：\n\n| 指标 | Qwen FT-U | Qwen FT-S1 | Llama FT-U | Llama FT-S1 |\n|------|-----------|------------|------------|-------------|\n| DR (%) | ? | ? | ? | ? |\n| RV (%) | ? | ? | ? | ? |\n| ET (%) | ? | ? | ? | ? |\n| CF (%) | ? | ? | ? | ? |\n| R-F1 (×100) | ? | ? | ? | ? |\n| E-F1 (×100) | ? | ? | ? | ? |\n| Parse failures | ? | ? | ? | ? |\n\n## 注意事项\n\n- DocRED ZS 数据已在 cross-model table (section5_crossmodel_draft.tex) 中，composability table 如果要加 ZS-DocRED 行，直接从那里取（Qwen U: DR=18.46, R-F1=7.74, E-F1=58.15; Qwen S1: DR=10.21, R-F1=8.23, E-F1=59.37; Llama U: DR=26.07, R-F1=5.98, E-F1=55.65; Llama S1: DR=2.55, R-F1=6.27, E-F1=55.01）\n- DocRED FT 的 DR reduction 可能比 SciERC FT 更复杂：ZS baseline Qwen DR=10.21%（S1）vs SciERC 0.93%，如果 FT baseline DR 也更高，FT+S1 的残留 DR 也可能更高\n- DocRED ontology 有 96 relations，FT 可能无法覆盖所有 long-tail relation 的 type constraint，tight-constraint 残留分析需要类似 SciERC Evaluate-for 的 per-relation breakdown\n"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T02:16:43.969765+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/composability_update_checklist.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T02:16:43.969935+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "memory.md",
  "content": "# Project Memory\n\n## Composability Update Checklist\n- DocRED FT+constrained eval 完成后需更新的论文位置已整理，见 `artifacts/composability_update_checklist.md`\n- P0 项：Table 5 加 DocRED 行 + 删 Limitations 中 \"DocRED not reported\" 声明\n- P1 项：§5.5 正文三段加 DocRED 数字 + Limitations CF 数字范围\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "memory.md",
    "content": "# Project Memory\n\n## Composability Update Checklist\n- DocRED FT+constrained eval 完成后需更新的论文位置已整理，见 `artifacts/composability_update_checklist.md`\n- P0 项：Table 5 加 DocRED 行 + 删 Limitations 中 \"DocRED not reported\" 声明\n- P1 项：§5.5 正文三段加 DocRED 数字 + Limitations CF 数字范围\n"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T02:16:43.970074+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_composability_paper_audit_20260516T021140",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-16T02:16:43.970236+00:00_

清单已保存到 `artifacts/composability_update_checklist.md`。

**总结**：论文中涉及 composability（FT + OntoCoDec）且需要 DocRED constrained eval 数字后更新的位置共 **10 处**，分布在 4 个文件中：

| 优先级 | 位置 | 要点 |
|--------|------|------|
| **P0** | `section5_composability.tex:18-51` Table 5 | 整个 DocRED 块缺失，需加 4-8 行数据 |
| **P0** | `main.tex:69` Limitations | 删除 "DocRED fine-tuning is not reported" |
| P1 | `section5_composability.tex:14-16` | 实验描述从 "SciERC" 改为 "SciERC and DocRED" |
| P1 | `section5_composability.tex:53-68` | "FT does not eliminate violations" 段加 DocRED DR 数字 |
| P1 | `section5_composability.tex:70-86` | "no F1 cost" 段加 DocRED delta 数字 |
| P1 | `main.tex:65` | Limitations CF≤1.18% 可能需扩为范围 |
| P2 | `section5_composability.tex:88-98` | Implication 定性 claim，看结果定 |
| P2 | `paper_tables_draft.tex:119` | TBD 占位符（未编译，低优先级） |

另外 `abstract.tex` 和 `section1_introduction_draft.tex` 中的 "composable" 用法是描述层间组合，不涉及 FT composability 数字，**无需更新**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_composability_paper_audit_20260516T021140"
}
```

</details>

---
