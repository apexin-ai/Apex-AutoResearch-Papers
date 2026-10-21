# paper table2 llama fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_paper_table2_llama_fix_20260520T111247.jsonl`
- **Structured JSON:** [`4bc6832763bac40f27a0.json`](../../sessions/4b/4bc6832763bac40f27a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-20T11:17:01.804972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T11:17:01.805326+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T11:17:01.805502+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T11:17:01.805640+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T11:17:01.805819+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T11:17:01.805950+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T11:17:01.806102+00:00_

artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
artifacts/_project/paper/section6_relwork_additions.tex
artifacts/_project/paper/discussion_paragraphs.tex
artifacts/dream_reports/dream_20260514T205155/best/paper.tex
artifacts/dream_reports/dream_20260514T205155/median/paper.tex
artifacts/dream_reports/dream_20260514T205155/worst/paper.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
artifacts/dream_reports/dream_20260516T021434/best/paper.tex
artifacts/dream_reports/dream_20260516T021434/median/paper.tex
artifacts/dream_reports/dream_20260516T021434/worst/paper.tex
artifacts/dream_reports/dream_20260516T173022/best/paper.tex
artifacts/dream_reports/dream_20260516T173022/median/paper.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/appendix_sampling_table.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/p3_case_studies.tex
artifacts/_project/paper/p3_case_studies_861a0d.tex
artifacts/p3_case_studies.tex
artifacts/dream_reports/dream_20260518T162745/best/paper.tex
artifacts/dream_reports/dream_20260518T162745/median/paper.tex
artifacts/dream_reports/dream_20260518T162745/worst/paper.tex
artifacts/_project/paper/appendix_sampling_table.tex
artifacts/_project/paper/appendix_full_ft.tex
artifacts/_project/paper/appendix_doc_length.tex
artifacts/_project/paper/appendix_prompt_sensitivity.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/appendix_case_studies.tex
artifact
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T11:17:01.806273+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
analyze_cf_fallback.py
analyze_cf_violations.py
artifacts
checkpoints
compiler
data
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.lock
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
registry.lock
registry.yaml
report.md
run_extraction_docred.py
scripts
study_status.lock
task_context
violation_checker.py
violation_checker_docred.py
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T11:17:01.806430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T11:17:01.806649+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation b
…[truncated 6044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T11:17:01.806845+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.20|0\\.26|44\\.23",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.20|0\\.26|44\\.23",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T11:17:01.807017+00:00_

artifacts/_project/paper/section5_docred_draft_9b84f1.tex:107:% phase2_docred_grammar_only: DR=0.2617
artifacts/_project/paper/section5_docred_draft_9b84f1.tex:146:% phase2_docred_full_s1: DR=0.1019; delta=(13.84-10.19)/13.84=0.264
artifacts/_project/paper/main.tex:81:Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.20\%, R-F1 within $\pm$0.6\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
artifacts/_project/paper/section5_crossmodel_draft.tex:59:Fine-tuning resolves both: DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.18\%, R-F1 $\pm$0.6\,pp (\S\ref{sec:composability}).
artifacts/_project/paper/section5_scierc_draft.tex:105:On DocRED ($\bar{\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\% to 0.01\% (Qwen, $\downarrow$99\%) and 0.49\% to 0.20\% (Llama, $\downarrow$59\%); R-F1 changes are $-$0.30\,pp and $+$0.51\,pp.
artifacts/_project/paper/section5_scierc_draft.tex:107:Across all four model-dataset settings, DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp.
artifacts/_project/paper/section5_scierc_draft.tex:109:LoRA + greedy S1 is the recommended fast deployment configuration: DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.2\% at R-F1 40--46, with $+$10\% latency overhead (\S\ref{sec:runtime}).
artifacts/_project/paper/section5_scierc_draft.tex:110:Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \S\ref{sec:beam-results}).
artifacts/_project/paper/section5_scierc_draft.tex:140:  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\downarrow$59\% \\
artifacts/_project/paper/section5_scierc_draft.tex:144:DR\,$\leq$\,0.20\% across both datasets with R-F1 within $\pm$0.6\,pp.
artifacts/_project/paper/appendix_tcr.tex:63:  & Llam
…[truncated 2252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T11:17:01.807228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "250",
  "limit": "90"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "250",
    "limit": "90"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T11:17:01.807412+00:00_

250	\midrule
251	\multirow{8}{*}{DocRED}
252	  & \multirow{4}{*}{Qwen3-8B}
253	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.09 & 7.11 & 82.15 & 40.86 \\
254	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
255	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
256	  & & Full S1       & \textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\
257	  \cmidrule(l){2-10}
258	  & \multirow{4}{*}{Llama-3.1-8B}
259	    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\
260	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
261	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
262	  & & Full S1       & \textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\
263	\bottomrule
264	\end{tabular}}%
265	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
266	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
267	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
268	Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
269	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED full vs.\ unconstrained).}
270	\label{tab:ft-ablation}
271	\end{table}
272	
273	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
274	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
275	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specific
…[truncated 4673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T11:17:01.807667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex",
  "offset": "55",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex",
    "offset": "55",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T11:17:01.807845+00:00_

55	\midrule
56	\multirow{3}{*}{Zero-shot}
57	  & Qwen    & 13.11 & \textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\
58	  & Llama   & 23.71 & \textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\
59	  & 70B     & 11.61 & \textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\
60	\midrule
61	\multirow{2}{*}{LoRA}
62	  & Qwen    &  0.42 & \textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\
63	  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
64	\bottomrule
65	\end{tabular}
66	\caption{TCR on DocRED ($\bar{\kappa}{=}0.842$, 998 docs).
67	Under zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\,pp for Llama) and E-F1 drops (up to $-$5.98\,pp for 70B).
68	Fundamental conflict rates are 12--23\%, an order of magnitude higher than SciERC.
69	Under LoRA, low baseline CF (0.36--0.42\%) limits both TCR impact and DR cost.}
70	\label{tab:tcr-docred}
71	\end{table}
72	
73	\paragraph{Analysis.}
74	TCR effectiveness correlates inversely with schema constraint tightness $\bar{\kappa}$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T11:17:01.807981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
  "offset": "65",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
    "offset": "65",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T11:17:01.808113+00:00_

65	
66	% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1
67	\paragraph{Layer contributions.}
68	Grammar-only eliminates RV and ET but \emph{increases} DR to 26.17\%: OOV triples (29.66\% baseline) become evaluable and expose latent type incompatibilities.\footnote{The grammar-only DR increase reflects constraint-altered generation trajectories in long documents, where vocabulary restriction shifts token probabilities away from natural but type-violating sequences.}
69	Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same enabling dependency observed on SciERC.
70	Residual DR (10.21\% vs.\ SciERC's 0.93\%) reflects higher tightness ($\bar{\kappa}{=}0.842$ vs.\ 0.333), which forces frequent fallback; effective semantic coverage is $\sim$90\% (Appendix~\ref{app:fallback-coverage}).
71	Under fine-tuning, residual narrows to 0.01--0.20\% (Table~\ref{tab:composability}).
72	The increase in Llama parse failures under constraints (6.8\%\,$\to$\,9.1\%) reflects an inherent trade-off: constraint masking alters token probability distributions, which can push generation toward suboptimal paths in long documents.
73	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T11:17:01.808248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
  "offset": "125",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
    "offset": "125",
    "limit": "45"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T11:17:01.808403+00:00_

125	\midrule
126	\multirow{2}{*}{8}
127	 & \textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\times$ \\
128	 & \textsc{con} & 66.36 & 43.65 & \textbf{0} & 0    & 5.058 & 2.03$\times$ \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	\paragraph{Composability with fine-tuning.}
134	Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with full S1 constraints already achieves DR=0\% but retains CF=1.18\% (21 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.
135	Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=44.23; changes within $\pm$0.5\,pp).
136	Llama-3.1-8B (LoRA, SciERC) with full S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) with R-F1=46.11; the zero-violation result thus generalizes across calibrated model families.
137	% exp_id: q1_llama_ft_beam_scierc
138	The three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.
139	
140	Beam search on DocRED (zero-shot, 50 documents) introduces a modest increase in parse failures (3/50, 6\%) compared to greedy (1.1\%), as longer beam-generated sequences occasionally produce malformed JSON in complex documents.
141	With DR=0 in 50 DocRED documents for both calibrated models, the Clopper-Pearson 95\% CI upper bound is 5.8\%; the full-scale LoRA evaluation below (998 documents, CI${\approx}$0.3\%) provides stronger statistical confirmation.
142	
143	Table~\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\ba
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T11:17:01.808614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "offset": "25",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
    "offset": "25",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T11:17:01.808796+00:00_

25	%
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes schema restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions; fallback frequency and residual DR increase accordingly.
28	This dual-factor pattern (tightness $\times$ baseline violation rate; $n{=}4$ model--dataset pairs, descriptive) aligns with the cross-dataset results: SciERC ($\bar{\kappa}{=}0.333$) achieves 94--99\% DR reduction vs.\ DocRED ($\bar{\kappa}{=}0.842$) at 45--90\%; the full range across three models is 42--99\% (\S\ref{sec:cross-model}; Appendix~\ref{app:dual-factor}).
29	The pattern extends to WikiEvents EE ($\bar{\kappa}{=}0.82$; Appendix~\ref{app:wikievents-kappa}).
30	However, $\kappa$ is necessary but not sufficient for high violation rates: per-relation analysis shows that high-$\kappa$ relations with unambiguous entity types (\textsc{place\_of\_birth}, $\kappa{=}0.92$, DR${=}$0\%) have zero violations, while relations with comparable $\kappa$ but confusable types (\textsc{basin\_country}, $\kappa{=}0.97$, DR${=}$74.6\%) are highly vulnerable (Appendix~\ref{app:kappa-case-study}).
31	$\bar{\kappa}$ provides deployment guidance: schemas with $\bar{\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\% reduction); schemas with $\bar{\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\,0.01--0.20\%).
32	$\bar{\kappa}$ also determines post-hoc resolution feasibility: low-$\bar{\kappa}$ schemas ($<$0.5) benefit from TCR with negligible DR regression ($\leq$0.28\,pp), while high-$\bar{\kappa}$ schemas ($>$0.8) suffer harmful DR increases (up to $+$9.38\,pp; Appendix~\ref{app:tcr}).
33	
34	\paragraph{Non-Rectangularity and Sequential Masking.}
35	\label{sec:rectangularity}
36	% Data source: artifacts/rebuttal/w2_rectangularity_report.md
37	Sequential masking is necessary because ontology type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED relations sa
…[truncated 442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T11:17:01.808949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "offset": "75",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "offset": "75",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T11:17:01.809093+00:00_

75	Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations; larger training sets or manual constraint table completion can reduce this gap.
76	
77	\paragraph{Evaluation coverage.}
78	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
79	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated only on 8B-class models.
80	Scaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
81	Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.20\%, R-F1 within $\pm$0.6\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
82	WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
83	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and DocRED (50 zero-shot, 998 fine-tuned documents) across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
84	
85	\paragraph{Engineering considerations.}
86	Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\% inference overhead and sub-second compilation ($<$0.5\,s; Appendix~\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.
87	Evaluation covers LoRA and full fine-tuning on 8B-class
…[truncated 243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T11:17:01.809232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
  "offset": "1",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
    "offset": "1",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T11:17:01.809369+00:00_

1	% Section 7 — Discussion and Conclusion
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	$\bar{\kappa}$ characterizes constraint regimes, with entity type confusability as the critical co-factor (Appendix~\ref{app:kappa-case-study}); the decidability taxonomy and $\bar{\kappa}$ diagnostic yield a principled deployment workflow.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T11:17:01.809543+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "    & Unconstr.\\ &  0.49 & ---  & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\",
  "new_string": "    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "    & Unconstr.\\ &  0.49 & ---  & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\",
    "new_string": "    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T11:17:01.809741+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T11:17:01.809881+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.",
  "new_string": "0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.",
    "new_string": "0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T11:17:01.810055+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T11:17:01.810184+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "The lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%)",
  "new_string": "The lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "The lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%)",
    "new_string": "The lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%)"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T11:17:01.810354+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T11:17:01.810478+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.",
  "new_string": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.",
    "new_string": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T11:17:01.810657+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T11:17:01.810813+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
  "new_string": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.21\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
    "new_string": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.21\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime})."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T11:17:01.810990+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T11:17:01.811117+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "DR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.",
  "new_string": "DR\\,$\\leq$\\,0.21\\% across both datasets with R-F1 within $\\pm$0.6\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "DR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.",
    "new_string": "DR\\,$\\leq$\\,0.21\\% across both datasets with R-F1 within $\\pm$0.6\\,pp."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T11:17:01.811282+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T11:17:01.811419+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\\\",
  "new_string": "    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\\\",
    "new_string": "    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T11:17:01.811697+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T11:17:01.811851+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\",
  "new_string": "  & & Full S1       & \\textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\",
    "new_string": "  & & Full S1       & \\textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T11:17:01.812089+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T11:17:01.812229+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings)",
  "new_string": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.21\\% in all 4 settings)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings)",
    "new_string": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.21\\% in all 4 settings)"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T11:17:01.812461+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T11:17:01.812598+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\",
  "new_string": "  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\",
    "new_string": "  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\\\"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T11:17:01.812845+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T11:17:01.812984+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
  "old_string": "residual narrows to 0.01--0.20\\%",
  "new_string": "residual narrows to 0.01--0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
    "old_string": "residual narrows to 0.01--0.20\\%",
    "new_string": "residual narrows to 0.01--0.21\\%"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T11:17:01.813145+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T11:17:01.813270+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "old_string": "DR\\,0.01--0.20\\%",
  "new_string": "DR\\,0.01--0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
    "old_string": "DR\\,0.01--0.20\\%",
    "new_string": "DR\\,0.01--0.21\\%"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T11:17:01.813427+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T11:17:01.813550+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "old_string": "DR drops to $\\leq$\\,0.20\\%",
  "new_string": "DR drops to $\\leq$\\,0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
    "old_string": "DR drops to $\\leq$\\,0.20\\%",
    "new_string": "DR drops to $\\leq$\\,0.21\\%"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T11:17:01.813728+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T11:17:01.813863+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "old_string": "DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp",
  "new_string": "DR\\,$\\leq$\\,0.21\\%, R-F1 within $\\pm$0.6\\,pp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "old_string": "DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp",
    "new_string": "DR\\,$\\leq$\\,0.21\\%, R-F1 within $\\pm$0.6\\,pp"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T11:17:01.814044+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T11:17:01.814173+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
  "old_string": "DR\\,$\\leq$\\,0.20\\%",
  "new_string": "DR\\,$\\leq$\\,0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
    "old_string": "DR\\,$\\leq$\\,0.20\\%",
    "new_string": "DR\\,$\\leq$\\,0.21\\%"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T11:17:01.814312+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T11:17:01.814444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && latexmk -pdf main.tex 2>&1 | tail -30",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && latexmk -pdf main.tex 2>&1 | tail -30",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T11:17:01.814603+00:00_

lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/
ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/zapfding/uzdr.pfb>
Output written on main.pdf (31 pages, 503393 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./relwork_new_entries.bib
Latexmk: All targets (main.pdf) are up-to-date

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T11:17:01.814771+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"LaTeX Error\\|Undefined control sequence\\|undefined references\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"LaTeX Error\\|Undefined control sequence\\|undefined references\" main.log"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T11:17:01.814891+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T11:17:01.815021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": "112",
  "limit": "37"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "offset": "112",
    "limit": "37"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T11:17:01.815158+00:00_

112	\begin{table}[t]
113	\centering
114	\small
115	\setlength{\tabcolsep}{3pt}
116	\resizebox{\columnwidth}{!}{%
117	\begin{tabular}{@{}lll rrrr r@{}}
118	\toprule
119	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
120	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
121	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
122	  & \textbf{$\Delta$DR} \\
123	\midrule
124	\multirow{4}{*}{Qwen3-8B}
125	  & \multirow{2}{*}{SciERC}
126	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
127	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
128	\cmidrule(l){2-8}
129	  & \multirow{2}{*}{DocRED}
130	    & Unconstr.\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\
131	  & & Full S1    & \textbf{0.01} & 0.27 & 40.56 & 81.43 & $\downarrow$99\% \\
132	\midrule
133	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
134	  & \multirow{2}{*}{SciERC}
135	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
136	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
137	\cmidrule(l){2-8}
138	  & \multirow{2}{*}{DocRED}
139	    & Unconstr.\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\
140	  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\downarrow$57\% \\
141	\bottomrule
142	\end{tabular}}%
143	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
144	DR\,$\leq$\,0.21\% across both datasets with R-F1 within $\pm$0.6\,pp.
145	F1\,$\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.
146	E-F1 includes parse-failure documents (Qwen PF: 7--9\%; Llama PF: 2--3\%); excluding parse failures, E-F1 is stable for both models ($\pm$0.1\,pp).}
147	\label{tab:composability}
148	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_table2_llama_fix_20260520T111247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-20T11:17:01.815340+00:00_

Table 2 验证通过，与 eval 结果完全一致：

| | E-F1 | R-F1 | DR% | CF% |
|---|------|------|-----|-----|
| Qwen unc | 82.15 | 40.86 | 0.76 | 0.09 |
| Qwen con | 81.43 | 40.56 | 0.01 | 0.27 |
| Llama unc | 83.93 | 43.72 | 0.49 | 0.08 |
| Llama con | 83.94 | 43.78 | 0.21 | 0.21 |

## 修改汇总

### Table 2 (section5_scierc_draft.tex:139-140)
| 位置 | 旧值 | 新值 |
|------|------|------|
| Llama unc CF | `---` | `0.08` |
| Llama con DR | `0.20` | `0.21` |
| Llama con CF | `0.26` | `0.21` |
| Llama con R-F1 | `44.23` | `43.78` |
| Llama con ΔDR | `59%` | `57%` |

### 正文连带修改 (section5_scierc_draft.tex)
- L105: DR `0.20→0.21`, ΔDR `59%→57%`, R-F1变化 `+0.51pp→+0.06pp`
- L106: `59%→57%`
- L107, L109, L144: `DR≤0.20%→DR≤0.21%`

### Appendix 连带修改 (appendix_discussion.tex)
- L259: Llama DocRED unc CF `---→0.08`
- L262: DR `0.20→0.21`, CF `0.26→0.21`, R-F1 `44.23→43.78`
- L275: `DR≤0.20%→DR≤0.21%`
- L329: post-hoc表 R-F1_cd `44.23→43.78`

### 其他文件连带修改
- section5_docred_draft.tex L71: `0.01--0.20%→0.01--0.21%`
- section4_composition_draft.tex L31, L40: `0.20%→0.21%`
- main.tex L81: `DR≤0.20%→DR≤0.21%`
- section7_conclusion_compressed.tex L4: `DR≤0.20%→DR≤0.21%`

### 未修改（非 Llama DocRED con 数据）
- appendix_beam_search.tex L135 `R-F1=44.23` — Qwen SciERC beam 结果
- appendix_beam_search.tex L161 `CF=0.26` — d065 4096-context 独立实验
- appendix_tcr.tex L63 `0.21/0.20` — TCR 独立指标

编译通过，31 pages，0 errors。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_table2_llama_fix_20260520T111247"
}
```

</details>

---
