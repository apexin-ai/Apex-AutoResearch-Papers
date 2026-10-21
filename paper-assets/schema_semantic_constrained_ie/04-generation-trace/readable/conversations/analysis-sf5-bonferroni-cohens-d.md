# analysis sf5 bonferroni cohens d

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_analysis_sf5-bonferroni-cohens-d_20260523T041527.jsonl`
- **Structured JSON:** [`ea01c13a7d185780dd5a.json`](../../sessions/ea/ea01c13a7d185780dd5a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-23T04:22:36.411003+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T04:22:36.411368+00:00_

_pdf_images
abstract.tex
abstract_d3264e.tex
abstract_fd4b26.tex
acl.sty
acl_natbib.bst
appendix_70b_ablation.tex
appendix_beam_search.tex
appendix_case_studies.tex
appendix_discussion.tex
appendix_doc_length.tex
appendix_downstream_analysis.tex
appendix_full_ft.tex
appendix_high_kappa_analysis.tex
appendix_kappa_case_study.tex
appendix_llama_per_relation.tex
appendix_order_invariance.tex
appendix_power_analysis.tex
appendix_power_analysis_523cc9.tex
appendix_prompt_sensitivity.tex
appendix_prompts.tex
appendix_pumping_lemma.tex
appendix_related_work.tex
appendix_reproducibility.tex
appendix_sampling_table.tex
appendix_scalability.tex
appendix_tcr.tex
appendix_type_consensus.tex.archived
case_study_kappa_dr.tex
checklist.tex
discussion_paragraphs.tex
discussion_paragraphs_cf83d1.tex
error_analysis_cases.json
fig1_framework.tex
figures
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
new_citations.bib
ontocodec_paper_r10_final.pdf
ontocodec_paper_r9_final.pdf
p3_case_studies.tex
p3_case_studies_861a0d.tex
paper_tables_draft.tex
r12_fallback_cascade_text.txt
relwork_new_entries.bib
section1_introduction_draft.tex
section2_background.tex
section3_method_draft.tex
section3_violation_landscape.tex
section4_composition_draft.tex
section5_crossmodel_draft.tex
section5_docred_draft.tex
section5_docred_draft_9b84f1.tex
section5_runtime.tex
section5_scierc_draft.tex
section5_scierc_draft_4796e8.tex
section5_wikievents_draft.tex
section6_related_work.tex
section6_relwork_additions.tex
section6_relwork_outline.tex
section7_conclusion_550cbf_DEPRECATED.tex
section7_conclusion_DEPRECATED.tex
section7_conclusion_compressed.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T04:22:36.411557+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T04:22:36.411732+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T04:22:36.411899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T04:22:36.412054+00:00_

1	% Appendix: Statistical Power Analysis for WikiEvents n=20
2	% Addresses reviewer concern about WikiEvents FT statistical power.
3	% Include via \input{appendix_power_analysis} in the appendix.
4	
5	\paragraph{Statistical power across evaluation settings.}
6	\label{app:power-analysis-full}
7	Table~\ref{tab:power-analysis} reports bootstrap confidence interval width and minimum detectable effect (MDE) for F1 across evaluation settings (${\geq}$1{,}000 bootstrap resamples; MDE at 80\% power, $\alpha{=}0.05$, paired test, $\rho{=}0.9$).
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\begin{tabular}{lrrr}
13	\toprule
14	\textbf{Dataset} & \textbf{$n$} & \textbf{95\% CI (F1)} & \textbf{MDE (F1)} \\
15	\midrule
16	SciERC & 551 & $\pm$1.8\,pp & 1.2\,pp \\
17	DocRED & 998 & $\pm$0.8\,pp & 0.5\,pp \\
18	DocRED (70B) & 200 & $\pm$3.3\,pp & 2.1\,pp \\
19	WikiEvents & 20 & $\pm$3.0\,pp & 2.0\,pp \\
20	\bottomrule
21	\end{tabular}
22	\caption{Statistical precision by dataset size.
23	95\% CI: bootstrap confidence interval half-width for per-configuration F1.
24	MDE: minimum detectable F1 difference at 80\% power ($\alpha{=}0.05$, paired test, conservative $\rho{=}0.9$).
25	SciERC/DocRED: zero-shot Rel-F1; DocRED (70B): LoRA Rel-F1 (200-doc subset); WikiEvents: LoRA Arg-F1.}
26	\label{tab:power-analysis}
27	\end{table}
28	
29	WikiEvents' $n{=}20$ yields an Arg-F1 margin of error of $\pm$3.0\,pp---comparable to the 200-document DocRED subset ($\pm$3.3\,pp)---with MDE${\approx}$2.0\,pp.
30	However, the primary WikiEvents claims concern violation elimination, not F1 improvement: RoV drops from 8.8--38.3\% to exactly 0\% across both models (bootstrap 95\% CI $[0\%,\,0\%]$ vs.\ $[2.4\%,\,15.4\%]$ / $[25.4\%,\,46.7\%]$; power${\approx}$1.0).
31	The small test set limits detection of subtle F1 shifts, but complete elimination of schema violations is unambiguous at $n{=}20$; the primary evidence for F1 preservation rests on SciERC ($n{=}551$) and DocRED ($n{=}998$), where CIs are ${\
…[truncated 17 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T04:22:36.412213+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "find /root/autodl-tmp/ -name \"*bootstrap*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "find /root/autodl-tmp/ -name \"*bootstrap*\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T04:22:36.412341+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T04:22:36.412461+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T04:22:36.412614+00:00_

artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:34:% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:39:% exp_id: d012_bootstrap_ci
artifacts/_project/paper/appendix_reproducibility.tex:30:We therefore report single-run results without error bars; bootstrap confidence intervals (10{,}000 iterations) are provided for F1 metrics.
artifacts/_project/paper/appendix_reproducibility.tex:58:To verify that this subset provides sufficient statistical power, we conduct a bootstrap analysis using the full 998-document 8B LoRA results as a reference population.
artifacts/_project/paper/checklist.tex:53:\\ Yes. Bootstrap significance tests ($p$-values, 10{,}000 iterations) are reported for key comparisons (\S\ref{sec:scierc-results}, \S\ref{sec:docred-results}). Tables report F1, precision, recall, and violation rates across all configurations.
artifacts/_project/paper/appendix_power_analysis.tex:7:Table~\ref{tab:power-analysis} reports bootstrap confidence interval width and minimum detectable effect (MDE) for F1 across evaluation settings (${\geq}$1{,}000 bootstrap resamples; MDE at 80\% power, $\alpha{=}0.05$, paired test, $\rho{=}0.9$).
artifacts/_project/paper/appendix_power_analysis.tex:23:95\% CI: bootstrap confidence interval half-width for per-configuration F1.
artifacts/_project/paper/appendix_power_analysis.tex:30:However, the primary WikiEvents claims concern violation elimination, not F1 improvement: RoV drops from 8.8--38.3\% to exactly 0\% across both models (bootstrap 95\% CI $[0\%,\,0\%]$ vs.\ $[2.4\%,\,15.4\%]$ / $[25.4\%,\,46.7\%]$; power${\approx}$1.0).
artifacts/_project/paper/appendix_discussion.tex:153:% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
artifacts/_project/paper/appendix_discussion.tex:164:%%% Bootstrap CIs and Effect Sizes %%%
artifacts/_project/paper/appendix_discussion.tex:165:% exp_ids: bootstrap_ci_ft_composability,
…[truncated 2818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T04:22:36.412861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "153",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "153",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T04:22:36.413086+00:00_

153	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
154	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
155	
156	\paragraph{Dataset-Dependent F1 Impact.}
157	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
158	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
159	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
160	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp); F1 gain magnitude is proportional to baseline OOV rate.
161	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
162	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
163	
164	%%% Bootstrap CIs and Effect Sizes %%%
165	% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci
166	
167	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
168	\label{app:bootstrap-effect-sizes}
169	
170	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs (10{,}000 iterations, document-level resampling) for the fine-tuning composability results (Table~\ref{tab:composability}).
171	
172	\begin{table}[t]
173	\centering
174	\small
175	\setlength{\tabcolsep}{3pt}
176	\begin{tabular}{@{}ll rrr@{}}
177	\toprule
178	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{R-F1 (pp)} & \textbf{95\% CI} & $p$ \\
179	\midrule
180	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & 0.726 \\
181	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & 0.056 \\
182	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & 0.736 \\
183	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & 0.535 \\
184	\midr
…[truncated 2682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T04:22:36.413244+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "find /root/autodl-tmp/ -name \"*bootstrap*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "find /root/autodl-tmp/ -name \"*bootstrap*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T04:22:36.413374+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T04:22:36.413534+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/ -name \"*bootstrap*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "find /root/ -name \"*bootstrap*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T04:22:36.413721+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/schema_outputs/r12_wikievents_bootstrap.json\\n/root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/Setup.bootstrap\\n/root/miniconda3/lib/python3.12/importlib/__pycache__/_bootstrap.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/importlib/__pycache__/_bootstrap_external.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/importlib/_bootstrap.py\\n/root/miniconda3/lib/python3.12/importlib/_bootstrap_external.py\\n/root/miniconda3/lib/python3.12/site-packages/wandb/sdk/launch/builder/templates/_wandb_bootstrap.py\\n/root/miniconda3/lib/python3.12/site-packages/wandb/sdk/launch/builder/templates/__pycache__/_wandb_bootstrap.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/site-packages/tatsu/bootstrap.py\\n/root/miniconda3/lib/python3.12/site-packages/tatsu/__pycache__/bootstrap.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/site-packages/test/zzz_bootstrap/bootstrap_test.py\\n/root/miniconda3/lib/python3.12/site-packages/test/zzz_bootstrap/__pycache__/bootstrap_test.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/site-packages/textworld/render/tmpl/static/bootstrap.min.css\\n/root/miniconda3/lib/python3.12/site-packages/textworld/render/tmpl/static/js/bootstrap.min.js\\n/root/miniconda3/lib/python3.12/site-packages/nvidia/nvshmem/lib/nvshmem_bootstrap_mpi.so.3\\n/root/miniconda3/lib/python3.12/site-packages/nvidia/nvshmem/lib/nvshmem_bootstrap_pmi.so.3\\n/root/miniconda3/lib/python3.12/site-packages/nvidia/nvshmem/lib/nvshmem_bootstrap_pmi2.so.3\\n/root/miniconda3/lib/python3.12/site-packages/nvidia/nvshmem/lib/nvshmem_bootstrap_pmix.so.3\\n/root/miniconda3/lib/python3.12/site-packages/nvidia/nvshmem/lib/nvshmem_bootstrap_shmem.so.3\\n/root/miniconda3/lib/python3.12/site-packages/nvidia/nvshmem/lib/nvshmem_bootstrap_uid.so.3\\n/root/miniconda3/lib/python3.12/site-packages/maturin/bootstrap.py\\n/root/miniconda3/lib/pyt
…[truncated 2272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T04:22:36.413871+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/bootstrap*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/bootstrap*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T04:22:36.413991+00:00_

artifacts/_project/data/bootstrap_ci_results.json
artifacts/_project/report/bootstrap_crossval_report.md
artifacts/bootstrap_crossval_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T04:22:36.414107+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts",
  "glob": "*.json",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts",
    "glob": "*.json",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T04:22:36.414229+00:00_

Found 16 files
artifacts/dream_reports/dream_20260522T052642/worst/experiment_data.json
artifacts/dream_reports/dream_20260522T052642/median/experiment_data.json
artifacts/dream_reports/dream_20260522T052642/best/experiment_data.json
artifacts/_project/report/task_c_supplementary_3f6e78.json
artifacts/_project/report/task_c_supplementary.json
artifacts/r16_verification/task_c_supplementary.json
artifacts/_project/data/r12_wikievents_bootstrap.json
artifacts/dream_reports/dream_20260518T162745/worst/experiment_data.json
artifacts/dream_reports/dream_20260518T162745/median/experiment_data.json
artifacts/dream_reports/dream_20260518T162745/best/experiment_data.json
artifacts/dream_reports/dream_20260516T173022/median/experiment_data.json
artifacts/dream_reports/dream_20260516T173022/best/experiment_data.json
artifacts/dream_reports/dream_20260516T021434/median/experiment_data.json
artifacts/dream_reports/dream_20260514T205155/median/experiment_data.json
artifacts/dream_reports/dream_20260514T205155/best/experiment_data.json
artifacts/_project/data/bootstrap_ci_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T04:22:36.414395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/outputs/bootstrap_ci_ft_composability.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/schema_semantic_constrained_ie/outputs/bootstrap_ci_ft_composability.json"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T04:22:36.414565+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T04:22:36.414774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"settings\\\": {\\n    \\\"Qwen-LoRA-SciERC\\\": {\\n      \\\"n_samples\\\": 551,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.4386298763082778,\\n        \\\"f1_b\\\": 0.43767840152235965,\\n        \\\"delta_point\\\": -0.0009514747859181716,\\n        \\\"delta_mean\\\": -0.0009561921675813286,\\n        \\\"ci_lower\\\": -0.002967359050445098,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 0.726\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.6705403834979663,\\n        \\\"f1_b\\\": 0.6705403834979663,\\n        \\\"delta_point\\\": 0.0,\\n        \\\"delta_mean\\\": 0.0,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 1.0\\n      }\\n    },\\n    \\\"Qwen-LoRA-DocRED\\\": {\\n      \\\"n_samples\\\": 998,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.40967427063374423,\\n        \\\"f1_b\\\": 0.4059783992145169,\\n        \\\"delta_point\\\": -0.0036958714192273368,\\n        \\\"delta_mean\\\": -0.0037055378165787153,\\n        \\\"ci_lower\\\": -0.007592290105293843,\\n        \\\"ci_upper\\\": -0.0005354787439645679,\\n        \\\"p_value\\\": 0.014\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.8222435487310727,\\n        \\\"f1_b\\\": 0.8149601010236707,\\n        \\\"delta_point\\\": -0.00728344770740208,\\n        \\\"delta_mean\\\": -0.007301595654623452,\\n        \\\"ci_lower\\\": -0.012111950558267803,\\n        \\\"ci_upper\\\": -0.003041898819680814,\\n        \\\"p_value\\\": 0.0004\\n      }\\n    },\\n    \\\"Llama-LoRA-SciERC\\\": {\\n      \\\"n_samples\\\": 551,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.4545012165450121,\\n        \\\"f1_b\\\": 0.45472249269717624,\\n        \\\"delta_point\\\": 0.00022127615216416263,\\n        \\\"delta_mean\\\": 0.00022208035589220865,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.000705289319757152,\\n        \\\
…[truncated 1537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T04:22:36.415071+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"results\\\": {\\n    \\\"qwen_scierc\\\": {\\n      \\\"rf1_unc\\\": {\\n        \\\"point\\\": 43.863,\\n        \\\"mean\\\": 43.8152,\\n        \\\"ci_lower\\\": 39.8981,\\n        \\\"ci_upper\\\": 47.7835\\n      },\\n      \\\"rf1_con\\\": {\\n        \\\"point\\\": 43.7678,\\n        \\\"mean\\\": 43.7196,\\n        \\\"ci_lower\\\": 39.8024,\\n        \\\"ci_upper\\\": 47.664\\n      },\\n      \\\"rf1_delta\\\": {\\n        \\\"point\\\": -0.0951,\\n        \\\"mean\\\": -0.0956,\\n        \\\"ci_lower\\\": -0.2967,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 0.726\\n      },\\n      \\\"dr_unc\\\": {\\n        \\\"point\\\": 1.9504,\\n        \\\"mean\\\": 1.9529,\\n        \\\"ci_lower\\\": 1.1121,\\n        \\\"ci_upper\\\": 2.8731\\n      },\\n      \\\"dr_con\\\": {\\n        \\\"point\\\": 0.0,\\n        \\\"mean\\\": 0.0,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.0\\n      },\\n      \\\"dr_delta\\\": {\\n        \\\"point\\\": -1.9504,\\n        \\\"mean\\\": -1.9529,\\n        \\\"ci_lower\\\": -2.8731,\\n        \\\"ci_upper\\\": -1.1121,\\n        \\\"p_value\\\": 0.0\\n      },\\n      \\\"global_counts\\\": {\\n        \\\"unc\\\": {\\n          \\\"rel_tp\\\": 461,\\n          \\\"rel_fp\\\": 667,\\n          \\\"rel_fn\\\": 513,\\n          \\\"dr_violations\\\": 22,\\n          \\\"total_pred_rels\\\": 1128\\n        },\\n        \\\"con\\\": {\\n          \\\"rel_tp\\\": 460,\\n          \\\"rel_fp\\\": 668,\\n          \\\"rel_fn\\\": 514,\\n          \\\"dr_violations\\\": 0,\\n          \\\"total_pred_rels\\\": 1128\\n        }\\n      },\\n      \\\"n_docs\\\": 551\\n    },\\n    \\\"llama_scierc\\\": {\\n      \\\"rf1_unc\\\": {\\n        \\\"point\\\": 45.4501,\\n        \\\"mean\\\": 45.396,\\n        \\\"ci_lower\\\": 41.41,\\n        \\\"ci_upper\\\": 49.4144\\n      },\\n      \\\"rf1_con\\\": {\\n        \\\"point\\\": 45.4722,\
…[truncated 5321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T04:22:36.415229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/bootstrap_ci_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/bootstrap_ci_results.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T04:22:36.415354+00:00_

1	See server: /root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T04:22:36.415554+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T04:22:36.415899+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Bootstrap CI for FT (LoRA) composability: constrained vs unconstrained.\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\n# --- Normalization (reuse from ZS script) ---\\n\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\ndef scierc_normalize_type(t, valid_types):\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in SCIERC_TYPE_MAP:\\n        return SCIERC_TYPE_MAP[t_lower]\\n    return None\\n\\nDOCRED_VALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\nDOCRED_ENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef docred_normalize_entity_type(raw_type):\\n    t = raw_type.strip().upper()\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = list(range(len(s2) + 1))\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\ndef build_name_to_id(rel_types):
…[truncated 7382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T04:22:36.416097+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/scripts/r12_bootstrap_ci_table2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/schema_semantic_constrained_ie/scripts/r12_bootstrap_ci_table2.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T04:22:36.416395+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Bootstrap CI for Table 2 composability: R-F1 delta & DR% delta.\\nDocument-level paired bootstrap, 10k iterations.\\nEval logic matches eval_d066_unified.py exactly.\\n\\\"\\\"\\\"\\nimport json, os\\nimport numpy as np\\n\\nSEED = 42\\nB = 10000\\nCI_LEVEL = 0.95\\nOUT_DIR = \\\"/root/schema_semantic_constrained_ie/outputs\\\"\\nSCIERC_ONT = \\\"/root/schema_semantic_constrained_ie/ontology_constraints.json\\\"\\nDOCRED_ONT = \\\"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\\"\\n\\nENTITY_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\nSETTINGS = {\\n    \\\"qwen_scierc\\\": {\\n        \\\"unc\\\": f\\\"{OUT_DIR}/w5_lora_scierc_unconstrained_eval.jsonl\\\",\\n        \\\"con\\\": f\\\"{OUT_DIR}/w5_lora_scierc_full_s1_eval.jsonl\\\",\\n        \\\"ontology\\\": SCIERC_ONT,\\n    },\\n    \\\"llama_scierc\\\": {\\n        \\\"unc\\\": f\\\"{OUT_DIR}/w5_llama_lora_scierc_unconstrained.jsonl\\\",\\n        \\\"con\\\": f\\\"{OUT_DIR}/w5_llama_lora_scierc_constrained.jsonl\\\",\\n        \\\"ontology\\\": SCIERC_ONT,\\n    },\\n    \\\"qwen_docred\\\": {\\n        \\\"unc\\\": f\\\"{OUT_DIR}/w5_qwen_docred_lora_unconstrained_eval.jsonl\\\",\\n        \\\"con\\\": f\\\"{OUT_DIR}/w5_qwen_docred_lora_constrained_eval.jsonl\\\",\\n        \\\"ontology\\\": DOCRED_ONT,\\n    },\\n    \\\"llama_docred\\\": {\\n        \\\"unc\\\": f\\\"{OUT_DIR}/w5_llama_docred_lora_unconstrained_eval.jsonl\\\",\\n        \\\"con\\\": f\\\"{OUT_DIR}/w5_llama_docred_lora_constrained_eval.jsonl\\\",\\n        \\\"ontology\\\": DOCRED_ONT,\\n    },\\n}\\n\\n\\ndef load_ontology(path):\\n    with open(path) as f:\\n        data = json.load(f)\\n    valid_etypes = set(data[\\\"entity_types\\\"])\\n    upper_map = {t.upper(): t for t in v
…[truncated 7373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T04:22:36.416695+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cat > /root/schema_semantic_constrained_ie/scripts/compute_cohens_d.py << 'PYEOF'\n\"\"\"Compute Cohen's d and Bonferroni-corrected p-values for R20 reviewer response.\nReuses eval logic from r12_bootstrap_ci_table2.py.\"\"\"\nimport json, os, sys\nimport numpy as np\n\nSEED = 42\nB = 10000\nCI_LEVEL = 0.95\nOUT_DIR = \"/root/schema_semantic_constrained_ie/outputs\"\nSCIERC_ONT = \"/root/schema_semantic_constrained_ie/ontology_constraints.json\"\nDOCRED_ONT = \"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\"\n\nENTITY_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nSETTINGS = {\n    \"qwen_scierc\": {\n        \"unc\": f\"{OUT_DIR}/w5_lora_scierc_unconstrained_eval.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_lora_scierc_full_s1_eval.jsonl\",\n        \"ontology\": SCIERC_ONT,\n    },\n    \"llama_scierc\": {\n        \"unc\": f\"{OUT_DIR}/w5_llama_lora_scierc_unconstrained.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_llama_lora_scierc_constrained.jsonl\",\n        \"ontology\": SCIERC_ONT,\n    },\n    \"qwen_docred\": {\n        \"unc\": f\"{OUT_DIR}/w5_qwen_docred_lora_unconstrained_eval.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_qwen_docred_lora_constrained_eval.jsonl\",\n        \"ontology\": DOCRED_ONT,\n    },\n    \"llama_docred\": {\n        \"unc\": f\"{OUT_DIR}/w5_llama_docred_lora_unconstrained_eval.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_llama_docred_lora_constrained_eval.jsonl\",\n        \"ontology\": DOCRED_ONT,\n    },\n}\n\n\ndef load_ontology(path):\n    with open(path) as f:\n        data = json.load(f)\n    valid_etypes = set(data[\"entity_types\"])\n    upper_map = {t.upper(): t for t in valid_etypes}\n    rt = data[\"relation_types\"]\n    is_pcode = isinstance(rt, dict)\n    pcode_to_name = rt if is_pcode else {}\n    raw_to_canonical = data.get(\"raw_to_canonical\", {})\n    rc = data.get(\"relation_constraints\", {})\n    valid_pairs = {}\n    for key, c in rc.items():\n        rn = pcode_to_name.get(key, key).lower().strip() if is_pcode else key.lower().strip()\n        valid_pairs[rn] = set(tuple(p) for p in c[\"valid_pairs\"])\n    return dict(upper_map=upper_map, is_pcode=is_pcode,\n                pcode_to_name=pcode_to_name, raw_to_canonical=raw_to_canonical,\n                valid_pairs=valid_pairs)\n\n\ndef norm_etype(raw, upper_map):\n    t = raw.strip()\n    tu = t.upper()\n    if tu in ENTITY_ALIASES:\n        return ENTITY_ALIASES[tu]\n    if tu in upper_map:\n        return upper_map[tu]\n    return t\n\n\ndef doc_stats(doc, ont):\n    parsed = doc.get(\"parsed_output\")\n    gold_rels = doc.get(\"gold_relations\", [])\n    is_pcode = ont[\"is_pcode\"]\n    p2n = ont[\"pcode_to_name\"]\n    r2c = ont[\"raw_to_canonical\"]\n    vp = ont[\"valid_pairs\"]\n    um = ont[\"upper_map\"]\n\n    gold_set = set()\n    for r in gold_rels:\n        rt = r[\"type\"]\n        rn = p2n.get(rt, rt).lower().strip() if is_pcode else rt.lower().strip()\n        gold_set.add((r[\"head\"], r[\"tail\"], rn))\n\n    if parsed is None or parsed == {}:\n        return (0, 0, len(gold_set), 0, 0)\n\n    pred_rels = parsed.get(\"relations\", [])\n    pred_set = set()\n    dr_v = 0\n    for r in pred_rels:\n        rt_raw = r.get(\"type\", \"\")\n        if rt_raw in r2c:\n            rt_raw = r2c[rt_raw]\n        rn = rt_raw.lower().strip()\n        pred_set.add((r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rn))\n        ht = r.get(\"head_type\", \"\")\n        tt = r.get(\"tail_type\", \"\")\n        if rn in vp:\n            pair = (norm_etype(ht, um), norm_etype(tt, um))\n            if pair not in vp[rn]:\n                dr_v += 1\n\n    tp = len(gold_set & pred_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return (tp, fp, fn, dr_v, len(pred_rels))\n\n\ndef f1(tp, fp, fn):\n    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n    return 2*p*r/(p+r) if (p+r) > 0 else 0.0\n\n\ndef dr_pct(dv, total):\n    return dv / total * 100 if total > 0 else 0.0\n\n\ndef bootstrap_with_cohens_d(unc_stats, con_stats, n_bootstrap=B, seed=SEED):\n    rng = np.random.RandomState(seed)\n    unc = np.array(unc_stats, dtype=np.float64)\n    con = np.array(con_stats, dtype=np.float64)\n    n = len(unc)\n\n    # Point estimates\n    uf1 = f1(unc[:,0].sum(), unc[:,1].sum(), unc[:,2].sum())\n    cf1 = f1(con[:,0].sum(), con[:,1].sum(), con[:,2].sum())\n    udr = dr_pct(unc[:,3].sum(), unc[:,4].sum())\n    cdr = dr_pct(con[:,3].sum(), con[:,4].sum())\n\n    # Bootstrap\n    uf1_samples = np.zeros(n_bootstrap)\n    cf1_samples = np.zeros(n_bootstrap)\n    udr_samples = np.zeros(n_bootstrap)\n    cdr_samples = np.zeros(n_bootstrap)\n\n    for i in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        u_b = unc[idx]\n        c_b = con[idx]\n        uf1_samples[i] = f1(u_b[:,0].sum(), u_b[:,1].sum(), u_b[:,2].sum())\n        cf1_samples[i] = f1(c_b[:,0].sum(), c_b[:,1].sum(), c_b[:,2].sum())\n        udr_samples[i] = dr_pct(u_b[:,3].sum(), u_b[:,4].sum())\n        cdr_samples[i] = dr_pct(c_b[:,3].sum(), c_b[:,4].sum())\n\n    # Convert to percentage points\n    uf1_pct = uf1_samples * 100\n    cf1_pct = cf1_samples * 100\n    df1_samples = cf1_pct - uf1_pct\n    ddr_samples = cdr_samples - udr_samples\n\n    delta_f1_point = (cf1 - uf1) * 100\n    delta_dr_point = cdr - udr\n\n    # P-values: two-sided for R-F1\n    p_f1 = 2 * min(np.mean(df1_samples <= 0), np.mean(df1_samples >= 0))\n    p_f1 = min(p_f1, 1.0)\n    # One-sided for DR (H0: delta >= 0)\n    p_dr = float(np.mean(ddr_samples >= 0))\n\n    # Cohen's d for R-F1: pooled SD approach\n    sd_unc_f1 = np.std(uf1_pct, ddof=1)\n    sd_con_f1 = np.std(cf1_pct, ddof=1)\n    pooled_sd_f1 = np.sqrt((sd_unc_f1**2 + sd_con_f1**2) / 2)\n    cohens_d_f1 = delta_f1_point / pooled_sd_f1 if pooled_sd_f1 > 0 else 0.0\n\n    # Cohen's d for DR%\n    sd_unc_dr = np.std(udr_samples, ddof=1)\n    sd_con_dr = np.std(cdr_samples, ddof=1)\n    pooled_sd_dr = np.sqrt((sd_unc_dr**2 + sd_con_dr**2) / 2)\n    cohens_d_dr = delta_dr_point / pooled_sd_dr if pooled_sd_dr > 0 else 0.0\n\n    alpha = 0.05\n    lo = (1 - CI_LEVEL) / 2\n    hi = 1 - lo\n\n    return {\n        \"rf1\": {\n            \"delta_point\": round(delta_f1_point, 4),\n            \"delta_mean\": round(float(np.mean(df1_samples)), 4),\n            \"ci_lower\": round(float(np.percentile(df1_samples, lo*100)), 4),\n            \"ci_upper\": round(float(np.percentile(df1_samples, hi*100)), 4),\n            \"p_value_raw\": round(float(p_f1), 4),\n            \"sd_unc\": round(float(sd_unc_f1), 4),\n            \"sd_con\": round(float(sd_con_f1), 4),\n            \"pooled_sd\": round(float(pooled_sd_f1), 4),\n            \"cohens_d\": round(float(cohens_d_f1), 4),\n        },\n        \"dr\": {\n            \"delta_point\": round(delta_dr_point, 4),\n            \"delta_mean\": round(float(np.mean(ddr_samples)), 4),\n            \"ci_lower\": round(float(np.percentile(ddr_samples, lo*100)), 4),\n            \"ci_upper\": round(float(np.percentile(ddr_samples, hi*100)), 4),\n            \"p_value_raw\": round(float(p_dr), 4),\n            \"sd_unc\": round(float(sd_unc_dr), 4),\n            \"sd_con\": round(float(sd_con_dr), 4),\n            \"pooled_sd\": round(float(pooled_sd_dr), 4),\n            \"cohens_d\": round(float(cohens_d_dr), 4),\n        },\n    }\n\n\ndef main():\n    k = len(SETTINGS)  # number of comparisons for Bonferroni\n    results = {}\n    \n    for name, cfg in SETTINGS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"  {name}\")\n        print(f\"{'='*60}\")\n        ont = load_ontology(cfg[\"ontology\"])\n        with open(cfg[\"unc\"]) as fh:\n            unc_recs = [json.loads(l) for l in fh if l.strip()]\n        with open(cfg[\"con\"]) as fh:\n            con_recs = [json.loads(l) for l in fh if l.strip()]\n        assert len(unc_recs) == len(con_recs)\n        for u, c in zip(unc_recs, con_recs):\n            assert u[\"doc_id\"] == c[\"doc_id\"]\n\n        us = [doc_stats(r, ont) for r in unc_recs]\n        cs = [doc_stats(r, ont) for r in con_recs]\n        res = bootstrap_with_cohens_d(us, cs)\n        res[\"n_docs\"] = len(unc_recs)\n        results[name] = res\n\n        # Print R-F1 results\n        rf = res[\"rf1\"]\n        p_bonf = min(rf[\"p_value_raw\"] * k, 1.0)\n        print(f\"  R-F1: delta={rf['delta_point']:+.2f}pp, 95%CI=[{rf['ci_lower']:+.2f}, {rf['ci_upper']:+.2f}]\")\n        print(f\"    p_raw={rf['p_value_raw']:.4f}, p_bonferroni={p_bonf:.4f}\")\n        print(f\"    SD_unc={rf['sd_unc']:.4f}, SD_con={rf['sd_con']:.4f}, pooled_SD={rf['pooled_sd']:.4f}\")\n        print(f\"    Cohen's d = {rf['cohens_d']:.4f}\")\n        d_abs = abs(rf['cohens_d'])\n        interp = \"negligible\" if d_abs < 0.2 else \"small\" if d_abs < 0.5 else \"medium\" if d_abs < 0.8 else \"large\"\n        print(f\"    Interpretation: {interp}\")\n\n        # Print DR% results\n        dr = res[\"dr\"]\n        p_bonf_dr = min(dr[\"p_value_raw\"] * k, 1.0)\n        print(f\"  DR%: delta={dr['delta_point']:+.2f}pp, 95%CI=[{dr['ci_lower']:+.2f}, {dr['ci_upper']:+.2f}]\")\n        print(f\"    p_raw={dr['p_value_raw']:.4f}, p_bonferroni={p_bonf_dr:.4f}\")\n        print(f\"    Cohen's d = {dr['cohens_d']:.4f}\")\n        d_abs_dr = abs(dr['cohens_d'])\n        interp_dr = \"negligible\" if d_abs_dr < 0.2 else \"small\" if d_abs_dr < 0.5 else \"medium\" if d_abs_dr < 0.8 else \"large\"\n        print(f\"    Interpretation: {interp_dr}\")\n\n    # Bonferroni correction\n    print(f\"\\n\\n{'='*60}\")\n    print(f\"  SUMMARY (k={k} comparisons, Bonferroni threshold = {0.05/k:.4f})\")\n    print(f\"{'='*60}\")\n    print(f\"{'Config':<18} {'delta(pp)':<10} {'p_raw':<8} {'p_bonf':<8} {'d':<8} {'|d| interp':<12} {'Sig?'}\")\n    print(\"-\" * 80)\n    for name, res in results.items():\n        rf = res[\"rf1\"]\n        p_bonf = min(rf[\"p_value_raw\"] * k, 1.0)\n        d_abs = abs(rf[\"cohens_d\"])\n        interp = \"negligible\" if d_abs < 0.2 else \"small\" if d_abs < 0.5 else \"medium\" if d_abs < 0.8 else \"large\"\n        sig = \"YES\" if p_bonf < 0.05 else \"no\"\n        print(f\"{name:<18} {rf['delta_point']:+.2f}      {rf['p_value_raw']:.4f}   {p_bonf:.4f}   {rf['cohens_d']:+.4f}  {interp:<12} {sig}\")\n\n    # Save\n    output = {\n        \"results\": results,\n        \"metadata\": {\n            \"n_bootstrap\": B, \"ci_method\": \"percentile\", \"ci_level\": CI_LEVEL,\n            \"seed\": SEED, \"k_comparisons\": k,\n            \"bonferroni_threshold\": 0.05 / k,\n            \"cohens_d_formula\": \"delta_mean / pooled_SD, pooled_SD = sqrt((SD_unc^2 + SD_con^2)/2)\",\n            \"cohens_d_note\": \"SD computed from bootstrap distribution (10k resamples); d interpretation per Cohen (1988): <0.2 negligible, 0.2-0.5 small, 0.5-0.8 medium, >0.8 large\",\n        }\n    }\n    out_path = f\"{OUT_DIR}/r20_cohens_d_pvalues.json\"\n    with open(out_path, \"w\") as fh:\n        json.dump(output, fh, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat > /root/schema_semantic_constrained_ie/scripts/compute_cohens_d.py << 'PYEOF'\n\"\"\"Compute Cohen's d and Bonferroni-corrected p-values for R20 reviewer response.\nReuses eval logic from r12_bootstrap_ci_table2.py.\"\"\"\nimport json, os, sys\nimport numpy as np\n\nSEED = 42\nB = 10000\nCI_LEVEL = 0.95\nOUT_DIR = \"/root/schema_semantic_constrained_ie/outputs\"\nSCIERC_ONT = \"/root/schema_semantic_constrained_ie/ontology_constraints.json\"\nDOCRED_ONT = \"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\"\n\nENTITY_ALIASES = {\n    'PERSON': 'PER', 'PEOPLE': 'PER',\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\n    'LOCATION': 'LOC', 'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\n    'MISCELLANEOUS': 'MISC',\n}\n\nSETTINGS = {\n    \"qwen_scierc\": {\n        \"unc\": f\"{OUT_DIR}/w5_lora_scierc_unconstrained_eval.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_lora_scierc_full_s1_eval.jsonl\",\n        \"ontology\": SCIERC_ONT,\n    },\n    \"llama_scierc\": {\n        \"unc\": f\"{OUT_DIR}/w5_llama_lora_scierc_unconstrained.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_llama_lora_scierc_constrained.jsonl\",\n        \"ontology\": SCIERC_ONT,\n    },\n    \"qwen_docred\": {\n        \"unc\": f\"{OUT_DIR}/w5_qwen_docred_lora_unconstrained_eval.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_qwen_docred_lora_constrained_eval.jsonl\",\n        \"ontology\": DOCRED_ONT,\n    },\n    \"llama_docred\": {\n        \"unc\": f\"{OUT_DIR}/w5_llama_docred_lora_unconstrained_eval.jsonl\",\n        \"con\": f\"{OUT_DIR}/w5_llama_docred_lora_constrained_eval.jsonl\",\n        \"ontology\": DOCRED_ONT,\n    },\n}\n\n\ndef load_ontology(path):\n    with open(path) as f:\n        data = json.load(f)\n    valid_etypes = set(data[\"entity_types\"])\n    upper_map = {t.upper(): t for t in valid_etypes}\n    rt = data[\"relation_types\"]\n    is_pcode = isinstance(rt, dict)\n    pcode_to_name = rt if is_pcode else {}\n    raw_to_canonical = data.get(\"raw_to_canonical\", {})\n    rc = data.get(\"relation_constraints\", {})\n    valid_pairs = {}\n    for key, c in rc.items():\n        rn = pcode_to_name.get(key, key).lower().strip() if is_pcode else key.lower().strip()\n        valid_pairs[rn] = set(tuple(p) for p in c[\"valid_pairs\"])\n    return dict(upper_map=upper_map, is_pcode=is_pcode,\n                pcode_to_name=pcode_to_name, raw_to_canonical=raw_to_canonical,\n                valid_pairs=valid_pairs)\n\n\ndef norm_etype(raw, upper_map):\n    t = raw.strip()\n    tu = t.upper()\n    if tu in ENTITY_ALIASES:\n        return ENTITY_ALIASES[tu]\n    if tu in upper_map:\n        return upper_map[tu]\n    return t\n\n\ndef doc_stats(doc, ont):\n    parsed = doc.get(\"parsed_output\")\n    gold_rels = doc.get(\"gold_relations\", [])\n    is_pcode = ont[\"is_pcode\"]\n    p2n = ont[\"pcode_to_name\"]\n    r2c = ont[\"raw_to_canonical\"]\n    vp = ont[\"valid_pairs\"]\n    um = ont[\"upper_map\"]\n\n    gold_set = set()\n    for r in gold_rels:\n        rt = r[\"type\"]\n        rn = p2n.get(rt, rt).lower().strip() if is_pcode else rt.lower().strip()\n        gold_set.add((r[\"head\"], r[\"tail\"], rn))\n\n    if parsed is None or parsed == {}:\n        return (0, 0, len(gold_set), 0, 0)\n\n    pred_rels = parsed.get(\"relations\", [])\n    pred_set = set()\n    dr_v = 0\n    for r in pred_rels:\n        rt_raw = r.get(\"type\", \"\")\n        if rt_raw in r2c:\n            rt_raw = r2c[rt_raw]\n        rn = rt_raw.lower().strip()\n        pred_set.add((r.get(\"head\", \"\"), r.get(\"tail\", \"\"), rn))\n        ht = r.get(\"head_type\", \"\")\n        tt = r.get(\"tail_type\", \"\")\n        if rn in vp:\n            pair = (norm_etype(ht, um), norm_etype(tt, um))\n            if pair not in vp[rn]:\n                dr_v += 1\n\n    tp = len(gold_set & pred_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return (tp, fp, fn, dr_v, len(pred_rels))\n\n\ndef f1(tp, fp, fn):\n    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n    return 2*p*r/(p+r) if (p+r) > 0 else 0.0\n\n\ndef dr_pct(dv, total):\n    return dv / total * 100 if total > 0 else 0.0\n\n\ndef bootstrap_with_cohens_d(unc_stats, con_stats, n_bootstrap=B, seed=SEED):\n    rng = np.random.RandomState(seed)\n    unc = np.array(unc_stats, dtype=np.float64)\n    con = np.array(con_stats, dtype=np.float64)\n    n = len(unc)\n\n    # Point estimates\n    uf1 = f1(unc[:,0].sum(), unc[:,1].sum(), unc[:,2].sum())\n    cf1 = f1(con[:,0].sum(), con[:,1].sum(), con[:,2].sum())\n    udr = dr_pct(unc[:,3].sum(), unc[:,4].sum())\n    cdr = dr_pct(con[:,3].sum(), con[:,4].sum())\n\n    # Bootstrap\n    uf1_samples = np.zeros(n_bootstrap)\n    cf1_samples = np.zeros(n_bootstrap)\n    udr_samples = np.zeros(n_bootstrap)\n    cdr_samples = np.zeros(n_bootstrap)\n\n    for i in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        u_b = unc[idx]\n        c_b = con[idx]\n        uf1_samples[i] = f1(u_b[:,0].sum(), u_b[:,1].sum(), u_b[:,2].sum())\n        cf1_samples[i] = f1(c_b[:,0].sum(), c_b[:,1].sum(), c_b[:,2].sum())\n        udr_samples[i] = dr_pct(u_b[:,3].sum(), u_b[:,4].sum())\n        cdr_samples[i] = dr_pct(c_b[:,3].sum(), c_b[:,4].sum())\n\n    # Convert to percentage points\n    uf1_pct = uf1_samples * 100\n    cf1_pct = cf1_samples * 100\n    df1_samples = cf1_pct - uf1_pct\n    ddr_samples = cdr_samples - udr_samples\n\n    delta_f1_point = (cf1 - uf1) * 100\n    delta_dr_point = cdr - udr\n\n    # P-values: two-sided for R-F1\n    p_f1 = 2 * min(np.mean(df1_samples <= 0), np.mean(df1_samples >= 0))\n    p_f1 = min(p_f1, 1.0)\n    # One-sided for DR (H0: delta >= 0)\n    p_dr = float(np.mean(ddr_samples >= 0))\n\n    # Cohen's d for R-F1: pooled SD approach\n    sd_unc_f1 = np.std(uf1_pct, ddof=1)\n    sd_con_f1 = np.std(cf1_pct, ddof=1)\n    pooled_sd_f1 = np.sqrt((sd_unc_f1**2 + sd_con_f1**2) / 2)\n    cohens_d_f1 = delta_f1_point / pooled_sd_f1 if pooled_sd_f1 > 0 else 0.0\n\n    # Cohen's d for DR%\n    sd_unc_dr = np.std(udr_samples, ddof=1)\n    sd_con_dr = np.std(cdr_samples, ddof=1)\n    pooled_sd_dr = np.sqrt((sd_unc_dr**2 + sd_con_dr**2) / 2)\n    cohens_d_dr = delta_dr_point / pooled_sd_dr if pooled_sd_dr > 0 else 0.0\n\n    alpha = 0.05\n    lo = (1 - CI_LEVEL) / 2\n    hi = 1 - lo\n\n    return {\n        \"rf1\": {\n            \"delta_point\": round(delta_f1_point, 4),\n            \"delta_mean\": round(float(np.mean(df1_samples)), 4),\n            \"ci_lower\": round(float(np.percentile(df1_samples, lo*100)), 4),\n            \"ci_upper\": round(float(np.percentile(df1_samples, hi*100)), 4),\n            \"p_value_raw\": round(float(p_f1), 4),\n            \"sd_unc\": round(float(sd_unc_f1), 4),\n            \"sd_con\": round(float(sd_con_f1), 4),\n            \"pooled_sd\": round(float(pooled_sd_f1), 4),\n            \"cohens_d\": round(float(cohens_d_f1), 4),\n        },\n        \"dr\": {\n            \"delta_point\": round(delta_dr_point, 4),\n            \"delta_mean\": round(float(np.mean(ddr_samples)), 4),\n            \"ci_lower\": round(float(np.percentile(ddr_samples, lo*100)), 4),\n            \"ci_upper\": round(float(np.percentile(ddr_samples, hi*100)), 4),\n            \"p_value_raw\": round(float(p_dr), 4),\n            \"sd_unc\": round(float(sd_unc_dr), 4),\n            \"sd_con\": round(float(sd_con_dr), 4),\n            \"pooled_sd\": round(float(pooled_sd_dr), 4),\n            \"cohens_d\": round(float(cohens_d_dr), 4),\n        },\n    }\n\n\ndef main():\n    k = len(SETTINGS)  # number of comparisons for Bonferroni\n    results = {}\n    \n    for name, cfg in SETTINGS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"  {name}\")\n        print(f\"{'='*60}\")\n        ont = load_ontology(cfg[\"ontology\"])\n        with open(cfg[\"unc\"]) as fh:\n            unc_recs = [json.loads(l) for l in fh if l.strip()]\n        with open(cfg[\"con\"]) as fh:\n            con_recs = [json.loads(l) for l in fh if l.strip()]\n        assert len(unc_recs) == len(con_recs)\n        for u, c in zip(unc_recs, con_recs):\n            assert u[\"doc_id\"] == c[\"doc_id\"]\n\n        us = [doc_stats(r, ont) for r in unc_recs]\n        cs = [doc_stats(r, ont) for r in con_recs]\n        res = bootstrap_with_cohens_d(us, cs)\n        res[\"n_docs\"] = len(unc_recs)\n        results[name] = res\n\n        # Print R-F1 results\n        rf = res[\"rf1\"]\n        p_bonf = min(rf[\"p_value_raw\"] * k, 1.0)\n        print(f\"  R-F1: delta={rf['delta_point']:+.2f}pp, 95%CI=[{rf['ci_lower']:+.2f}, {rf['ci_upper']:+.2f}]\")\n        print(f\"    p_raw={rf['p_value_raw']:.4f}, p_bonferroni={p_bonf:.4f}\")\n        print(f\"    SD_unc={rf['sd_unc']:.4f}, SD_con={rf['sd_con']:.4f}, pooled_SD={rf['pooled_sd']:.4f}\")\n        print(f\"    Cohen's d = {rf['cohens_d']:.4f}\")\n        d_abs = abs(rf['cohens_d'])\n        interp = \"negligible\" if d_abs < 0.2 else \"small\" if d_abs < 0.5 else \"medium\" if d_abs < 0.8 else \"large\"\n        print(f\"    Interpretation: {interp}\")\n\n        # Print DR% results\n        dr = res[\"dr\"]\n        p_bonf_dr = min(dr[\"p_value_raw\"] * k, 1.0)\n        print(f\"  DR%: delta={dr['delta_point']:+.2f}pp, 95%CI=[{dr['ci_lower']:+.2f}, {dr['ci_upper']:+.2f}]\")\n        print(f\"    p_raw={dr['p_value_raw']:.4f}, p_bonferroni={p_bonf_dr:.4f}\")\n        print(f\"    Cohen's d = {dr['cohens_d']:.4f}\")\n        d_abs_dr = abs(dr['cohens_d'])\n        interp_dr = \"negligible\" if d_abs_dr < 0.2 else \"small\" if d_abs_dr < 0.5 else \"medium\" if d_abs_dr < 0.8 else \"large\"\n        print(f\"    Interpretation: {interp_dr}\")\n\n    # Bonferroni correction\n    print(f\"\\n\\n{'='*60}\")\n    print(f\"  SUMMARY (k={k} comparisons, Bonferroni threshold = {0.05/k:.4f})\")\n    print(f\"{'='*60}\")\n    print(f\"{'Config':<18} {'delta(pp)':<10} {'p_raw':<8} {'p_bonf':<8} {'d':<8} {'|d| interp':<12} {'Sig?'}\")\n    print(\"-\" * 80)\n    for name, res in results.items():\n        rf = res[\"rf1\"]\n        p_bonf = min(rf[\"p_value_raw\"] * k, 1.0)\n        d_abs = abs(rf[\"cohens_d\"])\n        interp = \"negligible\" if d_abs < 0.2 else \"small\" if d_abs < 0.5 else \"medium\" if d_abs < 0.8 else \"large\"\n        sig = \"YES\" if p_bonf < 0.05 else \"no\"\n        print(f\"{name:<18} {rf['delta_point']:+.2f}      {rf['p_value_raw']:.4f}   {p_bonf:.4f}   {rf['cohens_d']:+.4f}  {interp:<12} {sig}\")\n\n    # Save\n    output = {\n        \"results\": results,\n        \"metadata\": {\n            \"n_bootstrap\": B, \"ci_method\": \"percentile\", \"ci_level\": CI_LEVEL,\n            \"seed\": SEED, \"k_comparisons\": k,\n            \"bonferroni_threshold\": 0.05 / k,\n            \"cohens_d_formula\": \"delta_mean / pooled_SD, pooled_SD = sqrt((SD_unc^2 + SD_con^2)/2)\",\n            \"cohens_d_note\": \"SD computed from bootstrap distribution (10k resamples); d interpretation per Cohen (1988): <0.2 negligible, 0.2-0.5 small, 0.5-0.8 medium, >0.8 large\",\n        }\n    }\n    out_path = f\"{OUT_DIR}/r20_cohens_d_pvalues.json\"\n    with open(out_path, \"w\") as fh:\n        json.dump(output, fh, indent=2)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T04:22:36.416997+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T04:22:36.417141+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/compute_cohens_d.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/compute_cohens_d.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T04:22:36.417306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  qwen_scierc\\n============================================================\\n  R-F1: delta=-0.10pp, 95%CI=[-0.30, +0.00]\\n    p_raw=0.7260, p_bonferroni=1.0000\\n    SD_unc=2.0058, SD_con=2.0036, pooled_SD=2.0047\\n    Cohen's d = -0.0475\\n    Interpretation: negligible\\n  DR%: delta=-1.95pp, 95%CI=[-2.87, -1.11]\\n    p_raw=0.0000, p_bonferroni=0.0000\\n    Cohen's d = -6.1453\\n    Interpretation: large\\n\\n============================================================\\n  llama_scierc\\n============================================================\\n  R-F1: delta=+0.02pp, 95%CI=[+0.00, +0.07]\\n    p_raw=0.7364, p_bonferroni=1.0000\\n    SD_unc=2.0356, SD_con=2.0356, pooled_SD=2.0356\\n    Cohen's d = 0.0109\\n    Interpretation: negligible\\n  DR%: delta=-1.02pp, 95%CI=[-1.98, -0.29]\\n    p_raw=0.0008, p_bonferroni=0.0032\\n    Cohen's d = -3.1719\\n    Interpretation: large\\n\\n============================================================\\n  qwen_docred\\n============================================================\\n  R-F1: delta=-0.31pp, 95%CI=[-0.69, +0.01]\\n    p_raw=0.0560, p_bonferroni=0.2240\\n    SD_unc=0.8301, SD_con=0.8426, pooled_SD=0.8363\\n    Cohen's d = -0.3661\\n    Interpretation: small\\n  DR%: delta=-0.75pp, 95%CI=[-1.07, -0.48]\\n    p_raw=0.0000, p_bonferroni=0.0000\\n    Cohen's d = -6.9994\\n    Interpretation: large\\n\\n============================================================\\n  llama_docred\\n============================================================\\n  R-F1: delta=+0.06pp, 95%CI=[-0.11, +0.25]\\n    p_raw=0.5346, p_bonferroni=1.0000\\n    SD_unc=0.8375, SD_con=0.8379, pooled_SD=0.8377\\n    Cohen's d = 0.0709\\n    Interpretation: negligible\\n  DR%: delta=-0.29pp, 95%CI=[-0.53, -0.10]\\n    p_raw=0.0001, p_bonferroni=0.0004\\n    Cohen's d = -3.0191\\n    Interpretation: large\\n\\n\\n===============
…[truncated 820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T04:22:36.417563+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "Table~\\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs (10{,}000 iterations, document-level resampling) for the fine-tuning composability results (Table~\\ref{tab:composability}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}ll rrr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & $\\Delta$\\textbf{R-F1 (pp)} & \\textbf{95\\% CI} & $p$ \\\\\n\\midrule\nQwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & 0.726 \\\\\nQwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & 0.056 \\\\\nLlama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & 0.736 \\\\\nLlama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & 0.535 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textbf{DR\\% reduction (all $p < 0.001$):}} \\\\\nQwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$0.001 \\\\\nQwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$0.001 \\\\\nLlama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$0.001 \\\\\nLlama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap CIs for Table~\\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42). Top: R-F1 difference (S1 $-$ unconstrained); no comparison reaches significance at $\\alpha{=}0.05$ after Bonferroni correction ($k{=}4$, threshold $p{=}0.0125$). Bottom: DR\\% reduction; all significant. Effect sizes for R-F1 are negligible ($|\\Delta| \\leq 0.31$\\,pp, all CIs spanning or adjacent to zero).}\n\\label{tab:bootstrap-effect-sizes}\n\\end{table}",
  "new_string": "Table~\\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\\ref{tab:composability}).\nAfter Bonferroni correction for $k{=}4$ comparisons ($\\alpha_{\\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \\leq 0.37$; Cohen, 1988).\nPer-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.\nConstraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \\geq 3.0$, all $p_{\\text{Bonf}} < 0.005$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}ll rrrr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & $\\Delta$\\textbf{(pp)} & \\textbf{95\\% CI} & $p$ & $d$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\\\\nQwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\\\\nQwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\\\\nLlama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\\\\nLlama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textbf{DR\\% reduction:}} \\\\\nQwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\\\\nQwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\\\\nLlama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\\\\nLlama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap CIs and Cohen's $d$ for Table~\\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).\n$d$: Cohen's $d$ from pooled bootstrap SD.\nTop: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\\alpha_{\\text{adj}}{=}0.0125$); $|d| \\leq 0.37$ (negligible--small).\nBottom: DR\\% reduction; all $p_{\\text{Bonf}} < 0.005$, $|d| \\geq 3.0$ (large).}\n\\label{tab:bootstrap-effect-sizes}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "Table~\\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs (10{,}000 iterations, document-level resampling) for the fine-tuning composability results (Table~\\ref{tab:composability}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}ll rrr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & $\\Delta$\\textbf{R-F1 (pp)} & \\textbf{95\\% CI} & $p$ \\\\\n\\midrule\nQwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & 0.726 \\\\\nQwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & 0.056 \\\\\nLlama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & 0.736 \\\\\nLlama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & 0.535 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textbf{DR\\% reduction (all $p < 0.001$):}} \\\\\nQwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$0.001 \\\\\nQwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$0.001 \\\\\nLlama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$0.001 \\\\\nLlama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap CIs for Table~\\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42). Top: R-F1 difference (S1 $-$ unconstrained); no comparison reaches significance at $\\alpha{=}0.05$ after Bonferroni correction ($k{=}4$, threshold $p{=}0.0125$). Bottom: DR\\% reduction; all significant. Effect sizes for R-F1 are negligible ($|\\Delta| \\leq 0.31$\\,pp, all CIs spanning or adjacent to zero).}\n\\label{tab:bootstrap-effect-sizes}\n\\end{table}",
    "new_string": "Table~\\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\\ref{tab:composability}).\nAfter Bonferroni correction for $k{=}4$ comparisons ($\\alpha_{\\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \\leq 0.37$; Cohen, 1988).\nPer-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.\nConstraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \\geq 3.0$, all $p_{\\text{Bonf}} < 0.005$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}ll rrrr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & $\\Delta$\\textbf{(pp)} & \\textbf{95\\% CI} & $p$ & $d$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\\\\nQwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\\\\nQwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\\\\nLlama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\\\\nLlama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textbf{DR\\% reduction:}} \\\\\nQwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\\\\nQwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\\\\nLlama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\\\\nLlama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap CIs and Cohen's $d$ for Table~\\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).\n$d$: Cohen's $d$ from pooled bootstrap SD.\nTop: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\\alpha_{\\text{adj}}{=}0.0125$); $|d| \\leq 0.37$ (negligible--small).\nBottom: DR\\% reduction; all $p_{\\text{Bonf}} < 0.005$, $|d| \\geq 3.0$ (large).}\n\\label{tab:bootstrap-effect-sizes}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T04:22:36.417967+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T04:22:36.418141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "167",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "167",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T04:22:36.418300+00:00_

167	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
168	\label{app:bootstrap-effect-sizes}
169	
170	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\ref{tab:composability}).
171	After Bonferroni correction for $k{=}4$ comparisons ($\alpha_{\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \leq 0.37$; Cohen, 1988).
172	Per-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.
173	Constraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \geq 3.0$, all $p_{\text{Bonf}} < 0.005$).
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\setlength{\tabcolsep}{3pt}
179	\begin{tabular}{@{}ll rrrr@{}}
180	\toprule
181	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{(pp)} & \textbf{95\% CI} & $p$ & $d$ \\
182	\midrule
183	\multicolumn{6}{@{}l}{\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\
184	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\
185	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\
186	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\
187	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\
188	\midrule
189	\multicolumn{6}{@{}l}{\textbf{DR\% reduction:}} \\
190	Qwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\
191	Qwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\
192	Llama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\
193	Llama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\
194	\bottomrule
195	\end{tabular}
196	\caption{Bootstrap CIs and Cohen's $d$ for
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-23T04:22:36.418505+00:00_

已完成。更新内容总结：

**表格变更** (`appendix_discussion.tex:175-201`)：
- 新增 Cohen's $d$ 列，共 8 个配置（4 R-F1 + 4 DR%）
- R-F1 效应量：$|d| \in [0.01, 0.37]$，全部 negligible 到 small
- DR% 效应量：$|d| \in [3.02, 7.00]$，全部 large
- 表头从 5 列扩展到 6 列，`\multicolumn` 已同步更新

**文本变更** (line 170-173)：
- 新增逐配置 Bonferroni 校正后 p 值：Qwen3-8B/DocRED $p_B=0.224$ 是最接近显著的，其余均 $p_B=1.00$
- 明确说明 k=4, $\alpha_{\text{adj}}=0.0125$ 阈值
- DR% 全部 $p_{\text{Bonf}} < 0.005$

**数据来源**：westd-16980 上从原始 eval JSONL 重新运行 10,000 次 bootstrap 计算，结果存于 `/root/schema_semantic_constrained_ie/outputs/r20_cohens_d_pvalues.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_sf5-bonferroni-cohens-d_20260523T041527"
}
```

</details>

---
