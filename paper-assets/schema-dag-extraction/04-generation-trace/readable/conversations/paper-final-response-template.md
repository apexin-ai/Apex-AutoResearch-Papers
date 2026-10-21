# paper final response template

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_final_response_template_20260522T110854.jsonl`
- **Structured JSON:** [`e3b6bdb003300f20915a.json`](../../sessions/e3/e3b6bdb003300f20915a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T11:11:48.578942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T11:11:48.579406+00:00_

1	# Author Response Template — Schema-DAG-Extraction
2	
3	Prepared 2026-05-22. Based on v34+ paper (post semipartial R² fix, post cross-model error taxonomy). Covers 5 anticipated attack surfaces from R29.
4	
5	---
6	
7	### Q1: BCS scope limited to FewRel RE
8	
9	**Anticipated Reviewer Question**: "BCS batch-level prediction only works on FewRel RE. The generalizability of your confusability framework is questionable."
10	
11	**Response Draft**:
12	
13	> Thank you for this important point. Our design deliberately uses FewRel as the primary testbed for batch-level BCS analysis because its balanced design (700 instances per type) and low multicollinearity (VIF = 1.18; §4.3) cleanly isolate the confusability effect — semipartial R² = 0.273 after partialing centrality. DocRED shows directional consistency (ridge β\_BCS < 0 across all λ ≥ 0; Appendix E.1), but VIF = 50.9 prevents reliable quantification; we explicitly report this as directional evidence (§4.3). The NER batch-level null is consistent across three models (Qwen3-32B, LLaMA-8B, LLaMA-70B) and two prompts, with power analysis confirming minimum detectable |r| ≈ 0.132 (Appendix E.2). Crucially, the *pairwise* confusability signal generalizes across all three tasks: Few-NERD r = 0.112 [0.076, 0.156], MAVEN r = 0.129 [0.104, 0.156] (Table 2), both CIs excluding zero. The NER–RE asymmetry has a structural explanation: NER errors distribute across miss (43–65%), boundary, and type substitution modes rather than concentrating in type confusion (Appendix Y). Using FewRel to establish the clean effect and other datasets to characterize boundary conditions is a principled analytical strategy, not a limitation of the metric.
14	
15	---
16	
17	### Q2: DocRED VIF = 50.9
18	
19	**Anticipated Reviewer Question**: "DocRED's VIF is 50.9. How can you trust any partial correlation or regression result on this dataset?"
20	
21	**Response Draft**:
22	
23	> We agree that VIF = 50.9 renders standard partial correlations unstable o
…[truncated 4915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T11:11:48.579608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/analysis_m1_gemini_leverage.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/analysis_m1_gemini_leverage.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T11:11:48.579792+00:00_

1	# M1: Gemini 2.5 Flash — Leverage Sensitivity Analysis (Cook's Distance)
2	
3	**Date**: 2026-05-22  
4	**Data**: `exp_gemini_flash/part2/results_incremental.jsonl` (6720 samples, 60 batches)  
5	**Batch groups**: count_8 (25 low + 25 high BCS), count_16 (5 low + 5 high BCS)
6	
7	---
8	
9	## 1. Count_16 BCS-Controlled (n=10)
10	
11	### Full Correlation
12	
13	| Metric | Value | p-value |
14	|--------|-------|---------|
15	| Pearson r | **-0.8043** | 0.005 |
16	| Spearman ρ | -0.4012 | 0.250 |
17	
18	### Cook's Distance (threshold = 4/n = 0.400)
19	
20	| Batch | BCS | Accuracy | Cook's D | Flag |
21	|-------|-----|----------|----------|------|
22	| count_16_high_4 | **0.9706** | **0.5990** | **0.4904** | LEVERAGE |
23	| count_16_high_0 | 0.5814 | 0.6615 | 0.3334 | |
24	| count_16_high_2 | 0.5890 | 0.8385 | 0.1017 | |
25	| (7 others) | 0.50–0.62 | 0.79–0.84 | <0.05 | |
26	
27	### Leverage Point Characterization — count_16_high_4
28	
29	- **BCS = 0.9706**: 11.2σ above the mean of the other 9 batches (mean=0.553, std=0.037). This is an extreme x-outlier — the other 9 batches cluster in [0.50, 0.62].
30	- **h_ii = 0.934**: hat value is 4.7× the mean (0.200). This single point captures 93% of the x-axis leverage.
31	- **Residual = +0.003**: near-zero residual (acc falls exactly on the regression line). The point is influential not because it deviates from the trend, but because it *defines* the trend.
32	- **Why it matters**: Without this point, the remaining 9 batches span only BCS=[0.50, 0.62] — too narrow a range for meaningful correlation.
33	
34	### Trimmed Correlation (n=9, removing high_4)
35	
36	| Metric | Value | p-value |
37	|--------|-------|---------|
38	| Pearson r | **-0.4173** | 0.264 |
39	| Spearman ρ | -0.1757 | 0.651 |
40	
41	**Conclusion**: count_16 correlation is single-point driven. The claim r=-0.80 is entirely dependent on high_4 (BCS=0.97). Removing it drops Pearson to r=-0.42 (n.s.) and Spearman to ρ=-0.18 (n.s.). This is consistent with the pape
…[truncated 4843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T11:11:48.580012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/analysis_m2_ecological_fallacy.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/analysis_m2_ecological_fallacy.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T11:11:48.580202+00:00_

1	# M2: Ecological Fallacy Analysis — BCS–Accuracy Relationship
2	
3	## Question
4	
5	The paper reports semipartial R²=0.273 (FewRel) for the BCS→accuracy relationship at the **batch level**. Is this susceptible to ecological fallacy — i.e., does the batch-level correlation misrepresent the instance-level relationship?
6	
7	## TL;DR
8	
9	**Ecological fallacy is structurally inapplicable.** BCS is a contextual (Level-2) variable with zero within-batch variance, not an aggregated individual-level variable. The classic ecological fallacy requires within-group variation in X, which does not exist here. The batch-level analysis is the correct and only possible level for BCS claims.
10	
11	## Data Sources
12	
13	| Dataset | Level | Records | Model |
14	|---------|-------|---------|-------|
15	| eval_exp1.json + eval_exp2.json | Per-type within batch | 1,548 type-obs across 74 multi-type batches | Qwen3-32B |
16	| Gemini Flash JSONL | Per-instance | 65,136 instances across 130 batches | Gemini Flash |
17	
18	## Analysis 1: ICC — Variance Decomposition
19	
20	### Type-level (Qwen3, n=1,548)
21	
22	| Component | Variance | % |
23	|-----------|----------|---|
24	| Between-batch | 0.0156 | 18.3% |
25	| Within-batch | 0.0695 | 81.7% |
26	| **ICC(1,1)** | **0.146** | — |
27	
28	F(73, 1474) = 4.52, p < .001.
29	
30	### Instance-level (Gemini Flash, n=65,136)
31	
32	| Component | Value |
33	|-----------|-------|
34	| ICC(1,1) | 0.035 |
35	| Between-batch MS | 3.797 |
36	| Within-batch MS | 0.200 |
37	| F(129, 65006) | 19.02, p < .001 |
38	
39	### ICC by count level (Qwen3 type-level)
40	
41	| count | ICC | F | n_batches |
42	|-------|-----|---|-----------|
43	| count_4 | −0.019 | 0.93 | 5 |
44	| count_8 | 0.068 | 1.58 | 27 |
45	| count_16 | 0.039 | 1.64 | 27 |
46	| count_32 | 0.006 | 1.19 | 5 |
47	| count_64 | −0.008 | 0.52 | 5 |
48	
49	**Within each count level**, ICC is low (< 0.07), meaning type-accuracy variance within batches is overwhelmingly within-batch (instance/type diff
…[truncated 5409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T11:11:48.580353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/analysis_m4_contamination.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/analysis_m4_contamination.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T11:11:48.580542+00:00_

1	# M4: FewRel Data Contamination / Memorization Detection
2	
3	**Date:** 2026-05-22
4	**Target:** Qwen3-32B on FewRel (80-rel pool, wiki_80 split)
5	**Core question:** Is the BCS–accuracy correlation on FewRel an artifact of model memorization?
6	
7	---
8	
9	## Approach A: Per-Type Accuracy Distribution Analysis
10	
11	**Data source:** `eval_exp1.json` — 80 relation types, 12 instances each at count=1 (single-type batches, BCS=0).
12	
13	Count=1 eliminates confusability; the model only needs to recognize one relation type per batch. If the model memorized FewRel, we'd expect uniformly high accuracy across all types.
14	
15	### Observed distribution
16	
17	| Statistic | Value |
18	|-----------|-------|
19	| Mean | 0.857 |
20	| Median | 0.917 |
21	| Std | **0.147** |
22	| Min | 0.417 |
23	| Max | 1.000 |
24	| IQR | 0.250 |
25	
26	| Accuracy range | # types | % |
27	|----------------|---------|---|
28	| [0.00, 0.50) Very hard | 2 | 2.5% |
29	| [0.50, 0.60) Hard | 4 | 5.0% |
30	| [0.60, 0.70) Below avg | 6 | 7.5% |
31	| [0.70, 0.80) Moderate | 9 | 11.2% |
32	| [0.80, 0.90) Good | 16 | 20.0% |
33	| [0.90, 0.99) High | 18 | 22.5% |
34	| [0.99, 1.00] Perfect | 25 | 31.2% |
35	
36	### Key observations
37	
38	1. **Massive variance (std=0.147)** is inconsistent with memorization. Memorized data would produce near-uniform high accuracy.
39	2. **15 types (18.8%) have accuracy < 0.70.** Worst cases: "work location" (0.167), "located on terrain feature" (0.185), "occupant" (0.199), "participant" (0.256). These are genuinely difficult ambiguous relations.
40	3. **25 types (31.2%) have perfect accuracy**, but these are semantically distinctive types: "child", "father", "spouse", "country", "sport", "military rank" — relations with clear, unambiguous entity-pair semantics that any strong LLM would get right.
41	4. **The bimodal pattern** (easy/distinctive types near 1.0 + hard/ambiguous types below 0.7) is characteristic of genuine task difficulty variation, not memorization.
42	
4
…[truncated 8408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T11:11:48.580741+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.218|22%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.218|22%",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T11:11:48.580918+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T11:11:48.581078+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ && ls main.aux 2>/dev/null && echo \"AUX_EXISTS\" || (pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && echo \"COMPILED\" || echo \"COMPILE_FAILED\")",
  "description": "Check if aux exists or compile paper",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ && ls main.aux 2>/dev/null && echo \"AUX_EXISTS\" || (pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && echo \"COMPILED\" || echo \"COMPILE_FAILED\")",
    "description": "Check if aux exists or compile paper",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T11:11:48.581207+00:00_

/bin/bash: line 1: cd: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/: No such file or directory
COMPILE_FAILED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T11:11:48.581325+00:00_

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
  "session": "worker_paper_final_response_template_20260522T110854",
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

_source line 14 · 2026-05-22T11:11:48.581468+00:00_

artifacts/_project/paper/method_framework.md
artifacts/_project/paper/related_work_draft.md
artifacts/_project/paper/maven_description.md
figures/paper/fig_sdgd_comparison.pdf
figures/paper/fig_sdgd_comparison.png
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
docs/paper/acl.sty
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
artifacts/_project/paper/results.tex
docs/figures/paper/fig_re_channels.pdf
docs/figures/paper/fig_re_channels.png
docs/figures/paper/gen_fig_re_dual_panel.py
docs/figures/paper/fig_re_dual_panel.pdf
docs/paper/supplementary.bbl
docs/paper/supplementary.tex
docs/paper/_pdf_check/main_p8.png
docs/paper/_pdf_check/main_p9.png
docs/paper/_pdf_check2/main_p8.png
docs/paper/_pdf_check3/main_p9.png
docs/paper/_pdf_check4/main_p8.png
docs/paper/_pdf_check5/main_p8.png
docs/paper/_pdf_check6/main_p8.png
docs/paper/_pdf_check7/main_p6.png
docs/paper/_pdf_check7/main_p16.png
docs/paper/_pdf_check7/main_p20.png
docs/paper/_pdf_check7/main_p22.png
docs/paper/_pdf_check8/main_p6.png
docs/paper/_pdf_check8/main_p7.png
docs/paper/_pdf_check8/main_p15.png
docs/paper/_pdf_check8/main_p19.png
docs/paper/_pdf_check8/main_p21.png
docs/paper/_pdf_check9/main_p7.png
docs/paper/_pdf_check9/main_p8.png
docs/paper/_pdf_check10/main_p5.png
docs/paper/_pdf_check10/main_p6.png
artifacts/_project/paper/rebuttal_response_template.md
figures/paper/fig_error_taxonomy.pdf
figures/paper/fig_error_taxonomy.png
figures/paper/fig_count_curves.pdf
figures/paper/fig_count_curves.png
figures/paper/fig_bcs_scaling.pdf
figures/paper/fig_bcs_scaling.png
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
docs/paper/acl_natbib.bst
artifacts/_project/paper/main_715ed3.pdf
artifacts/_project/paper/main_33d9cb.pdf
artifacts/_project/paper/main_62ea55.pdf
artifacts/_project/paper/main_e49b2c.pdf
artifacts/_project/paper/paper_v30_llama70b_ner_null.pdf
artifacts/_project/paper/paper_v
…[truncated 1274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T11:11:48.581615+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T11:11:48.581744+00:00_

artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
docs/paper/supplementary.tex
artifacts/acknowledgements_draft.tex
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
artifacts/_project/paper/docred_ridge_appendix.tex
artifacts/docred_ridge_appendix.tex
docs/paper/sdgd_negative.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/experimental_setup.tex
docs/paper/discussion.tex
docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T11:11:48.581931+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -E \"newlabel\\{(tab:|sec:appendix|app:|sec:limit)\" main.aux",
  "description": "Extract table and appendix labels from aux file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -E \"newlabel\\{(tab:|sec:appendix|app:|sec:limit)\" main.aux",
    "description": "Extract table and appendix labels from aux file"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T11:11:48.582143+00:00_

\newlabel{tab:datasets}{{1}{4}{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\dagger $Trigger mentions across 8{,}042 sentences}{table.caption.9}{}}
\newlabel{tab:pairwise}{{2}{6}{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\to }t_j) + C(t_j{\to }t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S \ref {sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185])}{table.caption.14}{}}
\newlabel{sec:appendix_figures}{{A}{12}{Additional Figures}{appendix.A}{}}
\newlabel{tab:cross_model}{{3}{12}{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S \ref {sec:model}) for fair cross-model comparison; the count-curve results in \S \ref {sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1}{table.caption.26}{}}
\newlabel{tab:cross_model_bcs}{{4}{12}{Cross-model BCS-controlled FewRel accuracy. High-BCS accuracy converges to $\approx $51\% regardless of model, while low-BCS accuracy reflects model capacity differences. The confusability gap ($\Delta $, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B}{table.caption.27}{}}
\newlabel{tab:cross_model_ner_null}{{5}{12}{NER batch-level BCS--F1 correlation across models. $^\dagger $Partial correlation controlling for type frequency. $^\ddagger $LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested}{table.caption.28}{}}
\newlabel{s
…[truncated 13666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T11:11:48.582354+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "leverage|Cook|count_16.*caveat|high_4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Grep",
  "tool_args": {
    "pattern": "leverage|Cook|count_16.*caveat|high_4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T11:11:48.582487+00:00_

main.tex:756:[Omitted long matching line]
results.tex:68:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T11:11:48.582609+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "newlabel\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Grep",
  "tool_args": {
    "pattern": "newlabel\\{fig:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T11:11:48.582727+00:00_

453:[Omitted long matching line]
620:\newlabel{fig:error_taxonomy}{{2}{7}{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\rho = 0.84\text {--}1.0$; Table~\ref {tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic}{figure.caption.15}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T11:11:48.582888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "60",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "60",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T11:11:48.583082+00:00_

60	
61	\paragraph{Practical magnitude.}
62	\label{sec:practical_magnitude}
63	\looseness=-1
64	Direct regression on 100 random 16-type batches within the 80-relation pool yields a conservative restricted-range estimate ($r = -0.22$, $R^2 \approx 0.05$, $p = 0.027$) due to narrow BCS range (SD${}\,=\,0.044$ vs.\ pooled SD${}\,=\,0.141$). The pooled analysis (semipartial $R^2 = 0.273$, $n = 204$; \S\ref{sec:bcs_controlled}) provides the primary variance estimate; DocRED pooled $R^2 = 0.578$ ($n = 110$) is inflated by multicollinearity (VIF${}\,=\,50.9$; semipartial $R^2_{\text{BCS}} = 0.056$; Appendix~\ref{sec:appendix_partial_corr}). Quartile comparison: bottom-BCS batches average 82.8\% vs.\ 78.9\% for top-BCS ($\Delta = 3.9$\,pp; IQR-based expected gap: 2.2\,pp, 95\% CI [0.4, 4.0]). The amplification from pairwise $r^2 \approx 1.5\%$ to pooled semipartial $R^2 \approx 27.3\%$ reflects the operative mechanism: correlated confusable-type interactions compound within shared prompts \citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal (${\sim}3\times$ amplification; Monte Carlo simulation in Appendix~\ref{app:aggregation-sim}).
65	
66	\paragraph{Cross-model validation.}
67	\looseness=-1
68	The effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap (Table~\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\Delta = -17.6$\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \to -0.42$, $p = 0.22$; Spearman: $\rho = -0.40 \to -0.18$, $p = 0.64$; Appendix~\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\ref{tab:cross_mo
…[truncated 1484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T11:11:48.583256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "748",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "748",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T11:11:48.583400+00:00_

748	\end{tabular}
749	\end{table}
750	
751	Table~\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\rho = -1.0$). Including count 1, the Gemini count curve yields $\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\,pp from count 4 to 32) than for Qwen3 ($-$21.8\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\,pp at count 4 vs.\ 8.7\,pp at count 32, 9.8\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.
752	
753	\paragraph{Dimension~2: BCS-controlled confusability.}
754	We replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).
755	
756	At count 8, low-BCS batches achieve 90.5\% vs.\ high-BCS 72.9\% ($\Delta = -17.6$\,pp, 95\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\% vs.\ 82.3\%) leaves less room for degradation.
757	
758	Table~\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.
759	
760	\begin{table}[h]
761	\centering
762	\small
763	\caption{Cross-model BC
…[truncated 445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T11:11:48.583628+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md",
  "old_string": " We already use the qualifier \"to our knowledge\" in the abstract. We are not aware of such a study but would appreciate any references we may have overlooked.",
  "new_string": " We already use the qualifier \"to our knowledge\" in the abstract. We are not aware of such a study but would appreciate any references we may have overlooked.\n\n---\n\n### Q6: Gemini leverage sensitivity\n\n**Anticipated Reviewer Question**: \"The Gemini cross-model r=−0.80 is driven by leverage points. How robust is the cross-model evidence?\"\n\n**Response Draft**:\n\n> We acknowledge and have already disclosed this limitation. The count_16 correlation (r=−0.80, n=10) is indeed driven by a single leverage point (BCS=0.97, Cook's D=0.490, hat value h_ii=0.934); removing it drops r to −0.42 (n.s.). The paper explicitly reports this leave-one-out analysis (§4.3; Appendix U). Crucially, the count_8 result (n=50) is fully robust: Cook's distance identifies only two points exceeding the 4/n threshold, both residual-driven accuracy outliers (not BCS outliers), and trimmed r *strengthens* from −0.887 to −0.913 (p<10⁻¹⁹). The primary Gemini evidence — Δ=−17.6 pp at count 8 (95% CI [15.1, 20.1]; Table 25) — is unaffected by leverage removal. The count_16 fragility reflects a design limitation (5+5 batches with poor BCS separation), not evidence against the BCS effect. We frame Gemini as \"partial but fragile corroboration\" precisely because of this issue (§4.3).\n\n---\n\n### Q7: Ecological fallacy\n\n**Anticipated Reviewer Question**: \"Batch-level R² doesn't represent instance-level prediction. This could be ecological fallacy.\"\n\n**Response Draft**:\n\n> The ecological fallacy concern is structurally inapplicable. Classical ecological fallacy (Robinson, 1950) arises when a group-level predictor is an *aggregation* of individual-level values, creating a mismatch between group- and individual-level β. BCS is not an aggregated variable — it is an irreducibly batch-level construct (mean pairwise SCS across all schema types). Every instance within a batch shares identical BCS; within-batch BCS variance is exactly zero. In multilevel terms, BCS is a *contextual* (Level-2) variable; the batch-level analysis is the correct and only meaningful level for the batch composition hypothesis. Empirically, the effect direction is consistently negative at every available level: batch (semipartial R²=0.273; §4.3), type (β=−0.485, p<.001, cluster-robust SEs), and within every count stratum — no subgroup reverses the sign. The low ICC (0.035–0.146) confirms instance outcomes are noisy (expected for binary classification), not that the batch-level relationship is spurious.\n\n---\n\n### Q8: FewRel contamination\n\n**Anticipated Reviewer Question**: \"FewRel may be memorized by the model. How can you trust the BCS evidence?\"\n\n**Response Draft**:\n\n> Three lines of evidence mitigate this concern. First, per-type accuracy at count=1 (single-type batches, BCS=0) shows high variance (σ=0.147): 15 of 80 types fall below 70%, including \"work location\" (16.7%) and \"located on terrain feature\" (18.5%) — inconsistent with memorization. Second, the count-degradation pattern replicates across four model families with near-identical slopes (Qwen3: −30.1 pp, LLaMA-70B: −30.7 pp from count 8→80), ruling out model-specific artifacts. Third, the error taxonomy confirms a causal mechanism: intra-batch substitution scales monotonically with BCS (ρ=0.954; Table 6, Figure 2) — text recall cannot explain why errors concentrate specifically among semantically similar co-occurring types. While FewRel's Wikipedia source is likely in pretraining corpora, our task format (schema-conditioned extraction with novel batch compositions) differs from any plausible training exposure. Key BCS findings replicate on DocRED and Few-NERD (Table 2), neither sharing FewRel's annotation source."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md",
    "old_string": " We already use the qualifier \"to our knowledge\" in the abstract. We are not aware of such a study but would appreciate any references we may have overlooked.",
    "new_string": " We already use the qualifier \"to our knowledge\" in the abstract. We are not aware of such a study but would appreciate any references we may have overlooked.\n\n---\n\n### Q6: Gemini leverage sensitivity\n\n**Anticipated Reviewer Question**: \"The Gemini cross-model r=−0.80 is driven by leverage points. How robust is the cross-model evidence?\"\n\n**Response Draft**:\n\n> We acknowledge and have already disclosed this limitation. The count_16 correlation (r=−0.80, n=10) is indeed driven by a single leverage point (BCS=0.97, Cook's D=0.490, hat value h_ii=0.934); removing it drops r to −0.42 (n.s.). The paper explicitly reports this leave-one-out analysis (§4.3; Appendix U). Crucially, the count_8 result (n=50) is fully robust: Cook's distance identifies only two points exceeding the 4/n threshold, both residual-driven accuracy outliers (not BCS outliers), and trimmed r *strengthens* from −0.887 to −0.913 (p<10⁻¹⁹). The primary Gemini evidence — Δ=−17.6 pp at count 8 (95% CI [15.1, 20.1]; Table 25) — is unaffected by leverage removal. The count_16 fragility reflects a design limitation (5+5 batches with poor BCS separation), not evidence against the BCS effect. We frame Gemini as \"partial but fragile corroboration\" precisely because of this issue (§4.3).\n\n---\n\n### Q7: Ecological fallacy\n\n**Anticipated Reviewer Question**: \"Batch-level R² doesn't represent instance-level prediction. This could be ecological fallacy.\"\n\n**Response Draft**:\n\n> The ecological fallacy concern is structurally inapplicable. Classical ecological fallacy (Robinson, 1950) arises when a group-level predictor is an *aggregation* of individual-level values, creating a mismatch between group- and individual-level β. BCS is not an aggregated variable — it is an irreducibly batch-level construct (mean pairwise SCS across all schema types). Every instance within a batch shares identical BCS; within-batch BCS variance is exactly zero. In multilevel terms, BCS is a *contextual* (Level-2) variable; the batch-level analysis is the correct and only meaningful level for the batch composition hypothesis. Empirically, the effect direction is consistently negative at every available level: batch (semipartial R²=0.273; §4.3), type (β=−0.485, p<.001, cluster-robust SEs), and within every count stratum — no subgroup reverses the sign. The low ICC (0.035–0.146) confirms instance outcomes are noisy (expected for binary classification), not that the batch-level relationship is spurious.\n\n---\n\n### Q8: FewRel contamination\n\n**Anticipated Reviewer Question**: \"FewRel may be memorized by the model. How can you trust the BCS evidence?\"\n\n**Response Draft**:\n\n> Three lines of evidence mitigate this concern. First, per-type accuracy at count=1 (single-type batches, BCS=0) shows high variance (σ=0.147): 15 of 80 types fall below 70%, including \"work location\" (16.7%) and \"located on terrain feature\" (18.5%) — inconsistent with memorization. Second, the count-degradation pattern replicates across four model families with near-identical slopes (Qwen3: −30.1 pp, LLaMA-70B: −30.7 pp from count 8→80), ruling out model-specific artifacts. Third, the error taxonomy confirms a causal mechanism: intra-batch substitution scales monotonically with BCS (ρ=0.954; Table 6, Figure 2) — text recall cannot explain why errors concentrate specifically among semantically similar co-occurring types. While FewRel's Wikipedia source is likely in pretraining corpora, our task format (schema-conditioned extraction with novel batch compositions) differs from any plausible training exposure. Key BCS findings replicate on DocRED and Few-NERD (Table 2), neither sharing FewRel's annotation source."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T11:11:48.583884+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T11:11:48.584057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/author_response_template.md"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T11:11:48.584235+00:00_

1	# Author Response Template — Schema-DAG-Extraction
2	
3	Prepared 2026-05-22. Based on v34+ paper (post semipartial R² fix, post cross-model error taxonomy). Covers 5 anticipated attack surfaces from R29.
4	
5	---
6	
7	### Q1: BCS scope limited to FewRel RE
8	
9	**Anticipated Reviewer Question**: "BCS batch-level prediction only works on FewRel RE. The generalizability of your confusability framework is questionable."
10	
11	**Response Draft**:
12	
13	> Thank you for this important point. Our design deliberately uses FewRel as the primary testbed for batch-level BCS analysis because its balanced design (700 instances per type) and low multicollinearity (VIF = 1.18; §4.3) cleanly isolate the confusability effect — semipartial R² = 0.273 after partialing centrality. DocRED shows directional consistency (ridge β\_BCS < 0 across all λ ≥ 0; Appendix E.1), but VIF = 50.9 prevents reliable quantification; we explicitly report this as directional evidence (§4.3). The NER batch-level null is consistent across three models (Qwen3-32B, LLaMA-8B, LLaMA-70B) and two prompts, with power analysis confirming minimum detectable |r| ≈ 0.132 (Appendix E.2). Crucially, the *pairwise* confusability signal generalizes across all three tasks: Few-NERD r = 0.112 [0.076, 0.156], MAVEN r = 0.129 [0.104, 0.156] (Table 2), both CIs excluding zero. The NER–RE asymmetry has a structural explanation: NER errors distribute across miss (43–65%), boundary, and type substitution modes rather than concentrating in type confusion (Appendix Y). Using FewRel to establish the clean effect and other datasets to characterize boundary conditions is a principled analytical strategy, not a limitation of the metric.
14	
15	---
16	
17	### Q2: DocRED VIF = 50.9
18	
19	**Anticipated Reviewer Question**: "DocRED's VIF is 50.9. How can you trust any partial correlation or regression result on this dataset?"
20	
21	**Response Draft**:
22	
23	> We agree that VIF = 50.9 renders standard partial correlations unstable o
…[truncated 8512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_final_response_template_20260522T110854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T11:11:48.584586+00:00_

更新完成。总结：

1. **R² 数字** — 模板中无 "0.218" / "22%" 残留，全部已是 semipartial R²=0.273。

2. **新增 3 个 Q&A blocks**：
   - **Q6 (Gemini leverage)**: count_16 r=−0.80 确实由单个 leverage point 驱动（Cook's D=0.490），但 count_8 (n=50) trimmed r 从 −0.887 增强至 −0.913，论文已在 §4.3/Appendix U 中披露。
   - **Q7 (Ecological fallacy)**: BCS 是 Level-2 contextual variable，within-batch variance=0，ecological fallacy 结构上不适用；effect direction 在所有层级一致为负。
   - **Q8 (FewRel contamination)**: 三条证据线——per-type accuracy 高方差(σ=0.147)、跨模型 degradation slope 一致、IntraSub causal mechanism (ρ=0.954)——排除 memorization artifact。

3. **Appendix/Table 编号** — 全部 8 个 Q&A 中的引用与 main.aux 一致：E.1=Partial Correlation, E.2=NER Power, U=Gemini Cross-Model, Y=Relaxed Matching, C=Factorial, Table 2/5/6/10/25 均正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_final_response_template_20260522T110854"
}
```

</details>

---
