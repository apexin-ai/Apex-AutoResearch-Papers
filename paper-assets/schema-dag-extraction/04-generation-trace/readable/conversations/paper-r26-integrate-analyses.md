# paper r26 integrate analyses

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 0
- **Tool calls:** 53
- **Original source:** `logs/chats/worker_paper_r26_integrate_analyses_20260522T052238.jsonl`
- **Structured JSON:** [`859655f1ff1c15844dd7.json`](../../sessions/85/859655f1ff1c15844dd7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

107 recorded events

### Tool call

_source line 1 · 2026-05-22T05:26:32.885139+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find appendix and artifact files",
  "prompt": "I need to find the following files in this project:\n\n1. The appendix tex file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ - look for appendix*.tex files\n2. The main.tex file structure to understand how appendix is included\n3. In /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/, find:\n   - docred_ridge_regression.json\n   - docred_ridge_appendix.tex\n   - Any bootstrap-related result files\n   - fewrel_domain_distribution.json\n4. results.tex around line 52 to see the ridge regression reference\n\nList all found files with their full paths. For the tex files, read their contents. For the JSON files, read their contents too. For results.tex, read lines 40-65."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find appendix and artifact files",
    "prompt": "I need to find the following files in this project:\n\n1. The appendix tex file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ - look for appendix*.tex files\n2. The main.tex file structure to understand how appendix is included\n3. In /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/, find:\n   - docred_ridge_regression.json\n   - docred_ridge_appendix.tex\n   - Any bootstrap-related result files\n   - fewrel_domain_distribution.json\n4. results.tex around line 52 to see the ridge regression reference\n\nList all found files with their full paths. For the tex files, read their contents. For the JSON files, read their contents too. For results.tex, read lines 40-65."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-22T05:26:32.885516+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-22T05:26:32.885695+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T05:26:32.885851+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/*.json"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T05:26:32.886012+00:00_

artifacts/_project/data/bcs_comparison.json
artifacts/bcs_comparison.json
artifacts/ace05_code/configs/ace05_entity_types.json
artifacts/exp-004/data/ace05_entity_types.json
artifacts/ace05_code/configs/ace05_relation_types.json
artifacts/exp-004/data/ace05_relation_types.json
artifacts/_project/data/maven_event_types.json
artifacts/maven_code/configs/maven_event_types.json
artifacts/exp003a_analysis.json
artifacts/exp003a/report/exp003a_analysis.json
artifacts/dream_reports/dream_20260515T053106/best/experiment_data.json
artifacts/dream_reports/dream_20260515T053106/median/experiment_data.json
artifacts/dream_reports/dream_20260515T053106/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T113743/best/experiment_data.json
artifacts/dream_reports/dream_20260515T113743/median/experiment_data.json
artifacts/dream_reports/dream_20260515T113743/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T140829/best/experiment_data.json
artifacts/dream_reports/dream_20260515T140829/median/experiment_data.json
artifacts/dream_reports/dream_20260515T140829/worst/experiment_data.json
artifacts/eval_exp1.json
artifacts/eval_exp2.json
artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json
artifacts/_project/data/w3_cluster_bootstrap_results.json
artifacts/d037_statistical_analyses/w4_count_recall_ci_results.json
artifacts/_project/data/w4_count_recall_ci_results.json
artifacts/d037_statistical_analyses/w2_practical_effect_results.json
artifacts/_project/data/w2_practical_effect_results.json
artifacts/fewrel_v2_bcs/eval_results.json
artifacts/exp_fewrel_v2_bcs_controlled/data/eval_results.json
artifacts/fewrel_v2_bcs/bootstrap_ci.json
artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json
artifacts/d037_ner_v2_bcs_analysis.json
artifacts/d037_data_consistency_check.json
artifacts/d037_statistical_analyses/figure_data_audit.json
artifacts/_project/data/bcs_fix_results.json
artifacts/bcs_fix/bcs_fix_results.json
artifacts/exp_docred_conf
…[truncated 2581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T05:26:32.886169+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T05:26:32.886305+00:00_

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
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
artifacts/acknowledgements_draft.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
artifacts/_project/paper/docred_ridge_appendix.tex
artifacts/docred_ridge_appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T05:26:32.886444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper -name \"appendix*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper -name \"appendix*.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T05:26:32.886565+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T05:26:32.886692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T05:26:32.886962+00:00_

1	{
2	  "method": "Ridge regression (analytic from correlation matrix, GCV λ selection)",
3	  "data_source": "exp_docred_bcs_expanded: 110 DocRED batches (96-type pool, count_16+32)",
4	  "n_batches": 110,
5	  "correlation_matrix": {
6	    "r_BCS_accuracy": -0.7602,
7	    "r_centrality_accuracy": -0.7344,
8	    "r_BCS_centrality": 0.9901,
9	    "VIF": 50.8
10	  },
11	  "gcv_selected_alpha": 0.001231,
12	  "r2_ridge": 0.5944,
13	  "standardized_coefficients": {
14	    "bcs_coefficient": -1.5342,
15	    "centrality_coefficient": 0.7837
16	  },
17	  "ols_standardized_coefficients": {
18	    "bcs_coefficient": -1.6785,
19	    "centrality_coefficient": 0.9275,
20	    "r2": 0.5949
21	  },
22	  "ridge_path_at_selected_lambdas": {
23	    "0.01": {
24	      "bcs_coefficient": -1.0219,
25	      "centrality_coefficient": 0.2746
26	    },
27	    "0.1": {
28	      "bcs_coefficient": -0.4749,
29	      "centrality_coefficient": -0.2402
30	    },
31	    "1.0": {
32	      "bcs_coefficient": -0.2627,
33	      "centrality_coefficient": -0.2372
34	    },
35	    "10.0": {
36	      "bcs_coefficient": -0.0636,
37	      "centrality_coefficient": -0.061
38	    },
39	    "100.0": {
40	      "bcs_coefficient": -0.0075,
41	      "centrality_coefficient": -0.0072
42	    }
43	  },
44	  "sign_robustness": {
45	    "bcs_negative_for_all_lambda": true,
46	    "bcs_coef_range": [
47	      -1.6655,
48	      -0.0001
49	    ],
50	    "analytic_proof": "β_BCS = [(1+λ)·r_{BCS,y} − r_{BCS,cent}·r_{cent,y}] / [(1+λ)² − r²_{BCS,cent}]. Numerator = −(1+λ)·0.7602 + 0.7271 = −0.0331 − λ·0.7602, monotonically decreasing in λ and negative at λ=0. Denominator > 0. Hence β_BCS < 0 for all λ ≥ 0."
51	  },
52	  "note": "Analytic ridge from the 3-variable correlation matrix is equivalent to RidgeCV on standardized data for any given λ. GCV replaces k-fold CV. The extreme VIF (50.9) confirms high multicollinearity; ridge stabilizes the coefficients. The BCS coefficient is provably negative for all λ ≥ 0."
53	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T05:26:32.887342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T05:26:32.887522+00:00_

1	% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)
2	
3	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms
4	the negative direction of the BCS--accuracy relationship even after
5	regularizing for the severe BCS--centrality multicollinearity
6	(VIF\,$\approx$\,50.9).
7	The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$
8	($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$).
9	An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for
10	\emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge
11	solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at
12	$\lambda{=}0$ and monotonically decreasing thereafter.
13	Given the shrinkage bias inherent to ridge estimation, we interpret only
14	the sign---not the magnitude---of the BCS coefficient as directional
15	evidence that higher schema confusability degrades extraction accuracy,
16	independent of degree centrality.
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T05:26:32.887665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T05:26:32.887860+00:00_

1	{
2	  "domain_classification": {
3	    "country": "geography",
4	    "country of citizenship": "geography",
5	    "country of origin": "geography",
6	    "location": "geography",
7	    "located in the administrative territorial entity": "geography",
8	    "contains administrative territorial entity": "geography",
9	    "headquarters location": "geography",
10	    "location of formation": "geography",
11	    "work location": "geography",
12	    "residence": "geography",
13	    "located in or next to body of water": "geography",
14	    "located on terrain feature": "geography",
15	    "mountain range": "geography",
16	    "mouth of the watercourse": "geography",
17	    "tributary": "geography",
18	    "place served by transport hub": "geography",
19	    "crosses": "geography",
20	    "constellation": "geography",
21	    "applies to jurisdiction": "geography",
22	    "licensed to broadcast to": "geography",
23	    "father": "person",
24	    "mother": "person",
25	    "child": "person",
26	    "sibling": "person",
27	    "spouse": "person",
28	    "occupation": "person",
29	    "religion": "person",
30	    "position held": "person",
31	    "member of political party": "person",
32	    "military rank": "person",
33	    "military branch": "person",
34	    "field of work": "person",
35	    "voice type": "person",
36	    "owned by": "organization",
37	    "subsidiary": "organization",
38	    "operator": "organization",
39	    "manufacturer": "organization",
40	    "developer": "organization",
41	    "publisher": "organization",
42	    "distributor": "organization",
43	    "member of": "organization",
44	    "participating team": "organization",
45	    "participant": "organization",
46	    "league": "organization",
47	    "performer": "creative_work",
48	    "composer": "creative_work",
49	    "director": "creative_work",
50	    "screenwriter": "creative_work",
51	    "after a work by": "creative_work",
52	    "characters": "creative_work",
53	    "genre": "creative_work",
…[truncated 6033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T05:26:32.888097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/results.tex",
  "offset": "40",
  "limit": "26"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/results.tex",
    "offset": "40",
    "limit": "26"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T05:26:32.888274+00:00_

40	
41	The correlations are modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. Other factors---entity frequency, prompt position effects \cite{lost-in-middle-2024}, and type definition quality---jointly account for the remainder. Nevertheless, the signal is robust: both correlations survive bootstrap resampling with CIs bounded well above zero, and replicate across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings).
42	
43	Spearman rank correlations from the SCS validation experiment (exp-015) corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ ($p = 5 \times 10^{-5}$) for Qwen3 and $\rho = 0.306$ ($p = 4.6 \times 10^{-6}$) for MiniLM, indicating that among types the model actually confuses, embedding similarity is a stronger predictor.
44	
45	We frame these results as identifying one factor among several that drive type confusion, but the first to be empirically isolated in a controlled zero-shot IE setting.
46	
47	\subsection{BCS-Controlled Experiments}
48	\label{sec:bcs_controlled}
49	
50	To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes; Figure~\ref{fig:bcs_scaling} visualizes the scaling relationship.
51	
52	\begin{table}[t]
53	\centering
54	\small
55	\begin{tabular}{lcrrrr}
56	\toprule
57	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS Acc} & \textbf{High-BCS Acc} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
58	\midrule
59	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
60	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
61	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\

…[truncated 295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T05:26:32.888431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T05:26:32.888583+00:00_

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
…[truncated 6025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T05:26:32.888750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/dataset_stats.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T05:26:32.888932+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dataset statistics. \emph{Cross}: schema types span diverse semantic domains. \emph{Same}: types derive from a single ontological field (FrameNet event frames).}
5	\label{tab:datasets}
6	\begin{tabular}{@{}lccrl@{}}
7	\toprule
8	\textbf{Dataset} & \textbf{Task} & \textbf{\#\,Types} & \textbf{Eval.\ Size} & \textbf{Domain} \\
9	\midrule
10	Few-NERD & NER & 66 & 1{,}000 & Cross \\
11	FewRel   & RE  & 80 & 1{,}000 & Cross \\
12	MAVEN    & ED  & 168 & 18{,}904$^\dagger$ & Same \\
13	\bottomrule
14	\end{tabular}
15	\vspace{1mm}\\
16	{\footnotesize $^\dagger$Trigger mentions across 710 documents.}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T05:26:32.889100+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*bootstrap*\" -type f | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*bootstrap*\" -type f | head -20"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T05:26:32.889236+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"main.tex\" -o -name \"paper.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"main.tex\" -o -name \"paper.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T05:26:32.889378+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_bootstrap_ci_20260515T150128_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_exp_fewrel_80pool_16sub_bootstrap_20260516T014220_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_a1_bootstrap_corrected_20260519T184730_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_fix_bootstrap_ci_discrepancy_20260516T022039.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_debug_exp_fewrel_80pool_16sub_bootstrap_20260516T021106.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_bootstrap_ci_20260515T150128.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_a1_bootstrap_corrected_20260519T184730.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_diagnose_exp_fewrel_16rel_bootstrap_20260516T015515_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_bootstrap_reconcile_20260515T152233_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_fix_bootstrap_ci_discrepancy_20260516T022039_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_submit_exp_fewrel_80pool_16sub_bootstrap_20260516T015642.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_submit_exp_fewrel_16rel_bootstrap_20260516T010228.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_split_sample_boots
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T05:26:32.889520+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T05:26:32.889661+00:00_

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
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T05:26:32.889794+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper -name \"*.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T05:26:32.889935+00:00_

File content (26119 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T05:26:32.890055+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T05:26:32.890188+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/split_sample_bootstrap.json 2>&1 | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/split_sample_bootstrap.json 2>&1 | head -5"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T05:26:32.890306+00:00_

-rw-r--r-- 1 ubuntu ubuntu 4246 May 22 05:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/split_sample_bootstrap.json
-rw-r--r-- 1 ubuntu ubuntu 4246 May 22 05:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T05:26:32.890429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T05:26:32.890575+00:00_

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
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factoria
…[truncated 5658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T05:26:32.890727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T05:26:32.890903+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T05:26:32.891068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-22T05:26:32.891191+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T05:26:32.891319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T05:26:32.891464+00:00_

1	{
2	  "dataset": {
3	    "name": "FewRel combined (exp1=110 + exp2=54 batches, 80-type pool)",
4	    "n_batches": 164,
5	    "n_unique_types": 80,
6	    "original_r": -0.5178,
7	    "original_R2": 0.2681,
8	    "original_p": 1.2502070529685776e-12
9	  },
10	  "instance_sharing": {
11	    "mean_pairwise_overlap": 0.218,
12	    "fraction_pairs_with_overlap": 0.345,
13	    "icc_shared_type_pairs": 0.2119,
14	    "icc_independent_pairs": -0.0137
15	  },
16	  "design_effect": {
17	    "avg_batches_per_type": 21.9,
18	    "DEFF": 5.42,
19	    "effective_n": 30.3,
20	    "nominal_n": 164
21	  },
22	  "slope_standard_errors": {
23	    "slope": -0.1923,
24	    "ols_se": 0.025,
25	    "ols_95ci": [
26	      -0.2412,
27	      -0.1434
28	    ],
29	    "hc1_se": 0.0255,
30	    "hc1_95ci": [
31	      -0.2423,
32	      -0.1423
33	    ],
34	    "hc1_inflation": 1.02,
35	    "cluster_robust_se": 0.0239,
36	    "cluster_robust_95ci": [
37	      -0.2392,
38	      -0.1454
39	    ],
40	    "cluster_robust_inflation": 0.96,
41	    "n_clusters": 81
42	  },
43	  "bootstrap_R2": {
44	    "n_iterations": 10000,
45	    "standard": {
46	      "mean": 0.2731,
47	      "ci_95": [
48	        0.1451,
49	        0.417
50	      ],
51	      "ci_width": 0.2719
52	    },
53	    "cluster": {
54	      "mean": 0.2729,
55	      "ci_95": [
56	        0.1434,
57	        0.4111
58	      ],
59	      "ci_width": 0.2678,
60	      "width_change_pct": -1.5
61	    }
62	  },
63	  "bootstrap_slope": {
64	    "standard": {
65	      "mean": -0.192,
66	      "ci_95": [
67	        -0.2407,
68	        -0.1416
69	      ],
70	      "ci_width": 0.099
71	    },
72	    "cluster": {
73	      "mean": -0.1915,
74	      "ci_95": [
75	        -0.236,
76	        -0.1429
77	      ],
78	      "ci_width": 0.0931,
79	      "width_change_pct": -6.0
80	    }
81	  },
82	  "significance": {
83	    "ols_t": -7.7,
84	    "ols_p": 1.2501111257279263e-12,
85	    "cluster_robust_t": -8.04,
86	    "cluster_robust_p": 7.192690887336539e-12,
87	 
…[truncated 2822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T05:26:32.891621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "40",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "40",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T05:26:32.891763+00:00_

40	\label{fig:error_taxonomy}
41	\end{figure*}
42	
43	\subsection{BCS-Controlled Experiments}
44	\label{sec:bcs_controlled}
45	
46	\looseness=-1
47	On FewRel, BCS explains ${\sim}$22\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\,=\,1.18$). DocRED partial correlation ($r_{\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\,=\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\ref{sec:appendix_partial_corr}, Table~\ref{tab:partial_corr}).} the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
48	
49	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (95\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
50	
51	\paragraph{Document-level RE (DocRED).}
52	The effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\footnote{DocRED uses 5 batches per count level (vs.\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\,pp at count 16 ($\rho = -0.762$, 95\% CI [$-$0.88, $-$0.58]) and $-$15.7\,pp at count 32 ($\rho = -0.693$, 95\% CI [$-$0.8
…[truncated 3870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T05:26:32.891942+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ridge\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ridge\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-22T05:26:32.892064+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T05:26:32.892189+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"appendix\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"appendix\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex | head -20"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T05:26:32.892320+00:00_

40:\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
42:\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\,=\,0$) yields residual SD${}\,=\,0.88$\,pp, approximately 18--44\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\,pp) is far inside the $\pm 3$\,pp equivalence margin.
58:\appendix
61:\label{sec:appendix_figures}
156:\label{sec:appendix_sdgd}
200:\label{sec:appendix_routing}
227:\label{sec:appendix_factorial}
263:\label{sec:appendi
…[truncated 1860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-22T05:26:32.892469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "300",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "300",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-22T05:26:32.892620+00:00_

300	\end{tabular}}
301	\end{table}
302	
303	\paragraph{Interpretation.}
304	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
305	
306	Under joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
307	
308	\subsection{Partial Correlation: Controlling for Degree Centrality}
309	\label{sec:appendix_partial_corr}
310	
311	To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).
312	
313	\begin{table}[h]
314	\centering
315	\small
316	\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\,=\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\,=\,50.9$, $r = 0.99$), but the partial correlatio
…[truncated 7731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-22T05:26:32.892778+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts -name \"*bootstrap*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts -name \"*bootstrap*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-22T05:26:32.892951+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/w3_cluster_bootstrap_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/split_sample_bootstrap.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_v2_bcs/bootstrap_ci.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/bootstrap_analysis.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-22T05:26:32.893094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_v2_bcs/bootstrap_ci.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_v2_bcs/bootstrap_ci.json"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-22T05:26:32.893216+00:00_

1	{
2	  "delta_pp": 7.92,
3	  "ci_lower_pp": -5.21,
4	  "ci_upper_pp": 21.46,
5	  "low_mean_acc": 0.8042,
6	  "high_mean_acc": 0.725,
7	  "low_accs": [0.8333, 0.8125, 0.875, 0.8229, 0.6771],
8	  "high_accs": [0.7708, 0.7188, 0.7083, 0.9271, 0.5],
9	  "low_bcs_values": [0.4715, 0.6465, 0.6653, 0.6724, 0.6742],
10	  "high_bcs_values": [0.7778, 0.7908, 0.8201, 0.8226, 0.9706],
11	  "n_bootstrap": 10000
12	}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-22T05:26:32.893344+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-22T05:26:32.893463+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1.2K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
-rw-r--r-- 1 ubuntu ubuntu 6.3K May 21 03:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
-rw-r--r-- 1 ubuntu ubuntu  172 May 15 20:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu 1.2K May 22 05:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  11K May 21 21:49 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
-rw-r--r-- 1 ubuntu ubuntu 5.2K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  72K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu 6.4K May 20 08:59 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
-rw-r--r-- 1 ubuntu ubuntu 4.2K May 22 04:39 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  15K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
-rw-r--r-- 1 ubuntu ubuntu  643 May 22 05:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
-rw-r--r-- 1 ubuntu ubuntu  444 May 17 10:29 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T05:26:32.893679+00:00_

Perfect! Now I have all the information needed. Let me compile the comprehensive report:

## Summary of Found Files

### 1. Paper TEX Files (in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/)

**Main Paper Structure:**
- **main.tex** - Main paper document (72 KB). Includes \input directives for:
  - abstract.tex
  - introduction.tex
  - related_work.tex
  - experimental_setup.tex
  - results.tex
  - sdgd_negative.tex
  - discussion.tex
  - prompt_appendix.tex (via \input{prompt_appendix} at line 357)
  - Contains appendix sections starting at line 58 with \appendix directive

**Appendix Files Found:**
- **prompt_appendix.tex** (6.4 KB) - Complete prompt templates for all three extraction tasks (NER, ED, RE)
- Paper includes embedded appendix sections in main.tex covering:
  - Additional Figures (sec:appendix_figures)
  - SDGD failure analysis (sec:appendix_sdgd)
  - Routing analysis (sec:appendix_routing)
  - Factorial interaction (sec:appendix_factorial)
  - Within-pool controlled comparison (sec:appendix_within_pool)
  - Residualized BCS (sec:appendix_residualized_bcs)
  - Partial correlation / Degree centrality control (sec:appendix_partial_corr) - This section references the ridge regression!
  - NER BCS-null power analysis (sec:appendix_ner_power)
  - Batch composition results (sec:appendix_batch_composition)
  - Prompt version sensitivity (sec:appendix_prompt_sensitivity)
  - Cross-prompt-variant analysis (sec:appendix_prompt_variants)

**Other Paper Files:**
- abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, discussion.tex, sdgd_negative.tex, checklist.tex, conclusion.tex, supplementary.tex

### 2. Results TEX Files (in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/...)

- **/artifacts/_project/paper/results.tex** - Copy of results section
- **/artifacts/paper/tables/dataset_stats.tex** - Dataset statistics table
- **/artifacts/paper/
…[truncated 4929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Agent",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T05:26:32.894063+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T05:26:32.894201+00:00_

docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-22T05:26:32.894322+00:00_

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
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-22T05:26:32.894445+00:00_

File content (26119 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-22T05:26:32.894566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "0",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "0",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-22T05:26:32.894730+00:00_

0	\documentclass[11pt]{article}
1	
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{enumitem}
13	\usepackage[normalem]{ulem}
14	\usepackage{listings}
15	
16	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
40	
41	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial
…[truncated 4757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-22T05:26:32.894896+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sec:appendix_partial_corr",
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
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sec:appendix_partial_corr",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-22T05:26:32.895025+00:00_

docs/paper/main.tex:309:\label{sec:appendix_partial_corr}
docs/paper/results.tex:47:[Omitted long matching line]
docs/paper/results.tex:52:[Omitted long matching line]
docs/paper/results.tex:61:[Omitted long matching line]
docs/paper/main.aux:1593:\newlabel{sec:appendix_partial_corr}{{E.1}{16}{Partial Correlation: Controlling for Degree Centrality}{subsection.E.1}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-22T05:26:32.895162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "300",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "300",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-22T05:26:32.895341+00:00_

300	\end{tabular}}
301	\end{table}
302	
303	\paragraph{Interpretation.}
304	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
305	
306	Under joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
307	
308	\subsection{Partial Correlation: Controlling for Degree Centrality}
309	\label{sec:appendix_partial_corr}
310	
311	To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).
312	
313	\begin{table}[h]
314	\centering
315	\small
316	\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\,=\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\,=\,50.9$, $r = 0.99$), but the partial correlatio
…[truncated 7731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-22T05:26:32.895485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "399",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "399",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-22T05:26:32.895659+00:00_

399	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
400	
401	\section{BCS Aggregation Sensitivity}
402	\label{sec:appendix_bcs_sensitivity}
403	
404	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\ref{tab:bcs_aggregation}).
405	
406	\begin{table}[h]
407	\centering
408	\small
409	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
410	\label{tab:bcs_aggregation}
411	\resizebox{\columnwidth}{!}{%
412	\begin{tabular}{llcccc}
413	\toprule
414	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
415	\midr
…[truncated 6271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-22T05:26:32.895812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-22T05:26:32.895971+00:00_

1	% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)
2	
3	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms
4	the negative direction of the BCS--accuracy relationship even after
5	regularizing for the severe BCS--centrality multicollinearity
6	(VIF\,$\approx$\,50.9).
7	The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$
8	($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$).
9	An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for
10	\emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge
11	solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at
12	$\lambda{=}0$ and monotonically decreasing thereafter.
13	Given the shrinkage bias inherent to ridge estimation, we interpret only
14	the sign---not the magnitude---of the BCS coefficient as directional
15	evidence that higher schema confusability degrades extraction accuracy,
16	independent of degree centrality.
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-22T05:26:32.896101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-22T05:26:32.896253+00:00_

1	{
2	  "method": "Ridge regression (analytic from correlation matrix, GCV λ selection)",
3	  "data_source": "exp_docred_bcs_expanded: 110 DocRED batches (96-type pool, count_16+32)",
4	  "n_batches": 110,
5	  "correlation_matrix": {
6	    "r_BCS_accuracy": -0.7602,
7	    "r_centrality_accuracy": -0.7344,
8	    "r_BCS_centrality": 0.9901,
9	    "VIF": 50.8
10	  },
11	  "gcv_selected_alpha": 0.001231,
12	  "r2_ridge": 0.5944,
13	  "standardized_coefficients": {
14	    "bcs_coefficient": -1.5342,
15	    "centrality_coefficient": 0.7837
16	  },
17	  "ols_standardized_coefficients": {
18	    "bcs_coefficient": -1.6785,
19	    "centrality_coefficient": 0.9275,
20	    "r2": 0.5949
21	  },
22	  "ridge_path_at_selected_lambdas": {
23	    "0.01": {
24	      "bcs_coefficient": -1.0219,
25	      "centrality_coefficient": 0.2746
26	    },
27	    "0.1": {
28	      "bcs_coefficient": -0.4749,
29	      "centrality_coefficient": -0.2402
30	    },
31	    "1.0": {
32	      "bcs_coefficient": -0.2627,
33	      "centrality_coefficient": -0.2372
34	    },
35	    "10.0": {
36	      "bcs_coefficient": -0.0636,
37	      "centrality_coefficient": -0.061
38	    },
39	    "100.0": {
40	      "bcs_coefficient": -0.0075,
41	      "centrality_coefficient": -0.0072
42	    }
43	  },
44	  "sign_robustness": {
45	    "bcs_negative_for_all_lambda": true,
46	    "bcs_coef_range": [
47	      -1.6655,
48	      -0.0001
49	    ],
50	    "analytic_proof": "β_BCS = [(1+λ)·r_{BCS,y} − r_{BCS,cent}·r_{cent,y}] / [(1+λ)² − r²_{BCS,cent}]. Numerator = −(1+λ)·0.7602 + 0.7271 = −0.0331 − λ·0.7602, monotonically decreasing in λ and negative at λ=0. Denominator > 0. Hence β_BCS < 0 for all λ ≥ 0."
51	  },
52	  "note": "Analytic ridge from the 3-variable correlation matrix is equivalent to RidgeCV on standardized data for any given λ. GCV replaces k-fold CV. The extreme VIF (50.9) confirms high multicollinearity; ridge stabilizes the coefficients. The BCS coefficient is provably negative for all λ ≥ 0."
53	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-22T05:26:32.896403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-22T05:26:32.896582+00:00_

1	{
2	  "dataset": {
3	    "name": "FewRel combined (exp1=110 + exp2=54 batches, 80-type pool)",
4	    "n_batches": 164,
5	    "n_unique_types": 80,
6	    "original_r": -0.5178,
7	    "original_R2": 0.2681,
8	    "original_p": 1.2502070529685776e-12
9	  },
10	  "instance_sharing": {
11	    "mean_pairwise_overlap": 0.218,
12	    "fraction_pairs_with_overlap": 0.345,
13	    "icc_shared_type_pairs": 0.2119,
14	    "icc_independent_pairs": -0.0137
15	  },
16	  "design_effect": {
17	    "avg_batches_per_type": 21.9,
18	    "DEFF": 5.42,
19	    "effective_n": 30.3,
20	    "nominal_n": 164
21	  },
22	  "slope_standard_errors": {
23	    "slope": -0.1923,
24	    "ols_se": 0.025,
25	    "ols_95ci": [
26	      -0.2412,
27	      -0.1434
28	    ],
29	    "hc1_se": 0.0255,
30	    "hc1_95ci": [
31	      -0.2423,
32	      -0.1423
33	    ],
34	    "hc1_inflation": 1.02,
35	    "cluster_robust_se": 0.0239,
36	    "cluster_robust_95ci": [
37	      -0.2392,
38	      -0.1454
39	    ],
40	    "cluster_robust_inflation": 0.96,
41	    "n_clusters": 81
42	  },
43	  "bootstrap_R2": {
44	    "n_iterations": 10000,
45	    "standard": {
46	      "mean": 0.2731,
47	      "ci_95": [
48	        0.1451,
49	        0.417
50	      ],
51	      "ci_width": 0.2719
52	    },
53	    "cluster": {
54	      "mean": 0.2729,
55	      "ci_95": [
56	        0.1434,
57	        0.4111
58	      ],
59	      "ci_width": 0.2678,
60	      "width_change_pct": -1.5
61	    }
62	  },
63	  "bootstrap_slope": {
64	    "standard": {
65	      "mean": -0.192,
66	      "ci_95": [
67	        -0.2407,
68	        -0.1416
69	      ],
70	      "ci_width": 0.099
71	    },
72	    "cluster": {
73	      "mean": -0.1915,
74	      "ci_95": [
75	        -0.236,
76	        -0.1429
77	      ],
78	      "ci_width": 0.0931,
79	      "width_change_pct": -6.0
80	    }
81	  },
82	  "significance": {
83	    "ols_t": -7.7,
84	    "ols_p": 1.2501111257279263e-12,
85	    "cluster_robust_t": -8.04,
86	    "cluster_robust_p": 7.192690887336539e-12,
87	 
…[truncated 2822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-22T05:26:32.896735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-22T05:26:32.897049+00:00_

1	{
2	  "domain_classification": {
3	    "country": "geography",
4	    "country of citizenship": "geography",
5	    "country of origin": "geography",
6	    "location": "geography",
7	    "located in the administrative territorial entity": "geography",
8	    "contains administrative territorial entity": "geography",
9	    "headquarters location": "geography",
10	    "location of formation": "geography",
11	    "work location": "geography",
12	    "residence": "geography",
13	    "located in or next to body of water": "geography",
14	    "located on terrain feature": "geography",
15	    "mountain range": "geography",
16	    "mouth of the watercourse": "geography",
17	    "tributary": "geography",
18	    "place served by transport hub": "geography",
19	    "crosses": "geography",
20	    "constellation": "geography",
21	    "applies to jurisdiction": "geography",
22	    "licensed to broadcast to": "geography",
23	    "father": "person",
24	    "mother": "person",
25	    "child": "person",
26	    "sibling": "person",
27	    "spouse": "person",
28	    "occupation": "person",
29	    "religion": "person",
30	    "position held": "person",
31	    "member of political party": "person",
32	    "military rank": "person",
33	    "military branch": "person",
34	    "field of work": "person",
35	    "voice type": "person",
36	    "owned by": "organization",
37	    "subsidiary": "organization",
38	    "operator": "organization",
39	    "manufacturer": "organization",
40	    "developer": "organization",
41	    "publisher": "organization",
42	    "distributor": "organization",
43	    "member of": "organization",
44	    "participating team": "organization",
45	    "participant": "organization",
46	    "league": "organization",
47	    "performer": "creative_work",
48	    "composer": "creative_work",
49	    "director": "creative_work",
50	    "screenwriter": "creative_work",
51	    "after a work by": "creative_work",
52	    "characters": "creative_work",
53	    "genre": "creative_work",
…[truncated 6033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-22T05:26:32.897310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "40",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "40",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-22T05:26:32.897603+00:00_

40	\label{fig:error_taxonomy}
41	\end{figure*}
42	
43	\subsection{BCS-Controlled Experiments}
44	\label{sec:bcs_controlled}
45	
46	\looseness=-1
47	On FewRel, BCS explains ${\sim}$22\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\,=\,1.18$). DocRED partial correlation ($r_{\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\,=\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\ref{sec:appendix_partial_corr}, Table~\ref{tab:partial_corr}).} the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
48	
49	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (95\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
50	
51	\paragraph{Document-level RE (DocRED).}
52	The effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\footnote{DocRED uses 5 batches per count level (vs.\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\,pp at count 16 ($\rho = -0.762$, 95\% CI [$-$0.88, $-$0.58]) and $-$15.7\,pp at count 32 ($\rho = -0.693$, 95\% CI [$-$0.8
…[truncated 3870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-22T05:26:32.897784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "326",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "326",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-22T05:26:32.897946+00:00_

326	\end{table}
327	
328	As Table~\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\text{partial}} = -0.537$ vs.\ $r_{\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\S\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.
329	
330	\subsection{NER BCS-Null Power Analysis}
331	\label{sec:appendix_ner_power}
332	
333	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
334	
335	\section{Batch Composition Results}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-22T05:26:32.898096+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "^\\\\\\\\(section|subsection)\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "^\\\\\\\\(section|subsection)\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-22T05:26:32.898220+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-22T05:26:32.898339+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\section\\{|\\\\subsection\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\section\\{|\\\\subsection\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-22T05:26:32.898476+00:00_

60:\section{Additional Figures}
155:\section{SDGD Full Protocol and Results}
199:\subsection{Practical Routing Strategies on RE}
226:\section{Factorial Analysis and Separability Test}
262:\section{Within-Pool CI Details}
267:\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
308:\subsection{Partial Correlation: Controlling for Degree Centrality}
330:\subsection{NER BCS-Null Power Analysis}
335:\section{Batch Composition Results}
359:\section{Prompt Version Sensitivity Analysis}
373:\subsection{Cross-Prompt-Variant BCS Correlation}
401:\section{BCS Aggregation Sensitivity}
427:\section{BCS-Controlled Detailed Results}
450:\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
520:\section{Within-Pool Analysis Methodology}
551:\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
578:\section{Pair-to-Batch Aggregation Simulation}
596:\section{BCS Independence from Type Composition}
601:\section{SCS vs.\ Simple Baselines}
629:\section{Split-Origin Covariate Analysis}
643:\section{Cross-Seed Variance Decomposition}
668:\section{Cross-Domain Connections}
673:\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
713:\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
764:\section{Few-Shot Prompting and Confusability}
789:\section{Qualitative Error Analysis}
858:\section{Schema Label Renaming Experiment}
880:\section{Relaxed Matching Evaluation (NER)}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-22T05:26:32.898660+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}",
  "new_string": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}",
    "new_string": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-22T05:26:32.899112+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-22T05:26:32.899282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "335",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "335",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-22T05:26:32.899420+00:00_

335	
336	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
337	
338	\section{Batch Composition Results}
339	\label{sec:appendix_batch_composition}
340	
341	\begin{table}[h]
342	\centering
343	\small
344	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-22T05:26:32.899561+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}",
  "new_string": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}",
    "new_string": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-22T05:26:32.900026+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-22T05:26:32.900198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-22T05:26:32.900339+00:00_

are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/he
lvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 481024 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-22T05:26:32.900477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-22T05:26:32.900617+00:00_

The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--can't use both volume and number fields in guo-2021-label-confusion
(There was 1 warning)
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 480721 bytes).
Transcript written on main.log.
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 480721 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-22T05:26:32.900752+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^!\" main.log && grep -ci \"undefined\" main.log && grep \"undefined\" main.log | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^!\" main.log && grep -ci \"undefined\" main.log && grep \"undefined\" main.log | head -10"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-22T05:26:32.900908+00:00_

Exit code 1
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-22T05:26:32.901049+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^!\" main.log; grep -ci \"undefined\" main.log; grep \"LaTeX Warning.*undefined\" main.log | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^!\" main.log; grep -ci \"undefined\" main.log; grep \"LaTeX Warning.*undefined\" main.log | head -10"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-22T05:26:32.901167+00:00_

0
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-22T05:26:32.901291+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\appendix\" main.log | head -3; grep \"page.*shipped out\" main.log | tail -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\appendix\" main.log | head -3; grep \"page.*shipped out\" main.log | tail -3"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-22T05:26:32.901546+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-22T05:26:32.901716+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"Output written\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"Output written\" main.log"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-22T05:26:32.901865+00:00_

Output written on main.pdf (27 pages, 480721 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-22T05:26:32.901989+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"sec:appendix_partial_corr\" main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"sec:appendix_partial_corr\" main.aux"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-22T05:26:32.902104+00:00_

1593:\newlabel{sec:appendix_partial_corr}{{E.1}{16}{Partial Correlation: Controlling for Degree Centrality}{subsection.E.1}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-22T05:26:32.902230+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"appendix_bootstrap_ci|appendix_domain_distribution\" main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"appendix_bootstrap_ci|appendix_domain_distribution\" main.aux"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-22T05:26:32.902345+00:00_

\newlabel{sec:appendix_bootstrap_ci}{{E.3}{17}{Bootstrap CI Robustness}{subsection.E.3}{}}
\newlabel{sec:appendix_domain_distribution}{{E.4}{17}{Domain Distribution in Extreme-BCS Batches}{subsection.E.4}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-22T05:26:32.902470+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"\\\\\\\\appendix\" main.aux | head -1; grep \"newlabel{sec:appendix_figures}\" main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"\\\\\\\\appendix\" main.aux | head -1; grep \"newlabel{sec:appendix_figures}\" main.aux"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-22T05:26:32.902584+00:00_

\newlabel{sec:appendix_figures}{{A}{13}{Additional Figures}{appendix.A}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 107 · 2026-05-22T05:26:32.902742+00:00_

Appendix starts on page 13; body is within 8 pages (pages 1–8 body + references on pages 9–12).

### 修改摘要

| 任务 | 位置 | 内容 |
|------|------|------|
| **A: Ridge Regression** | `main.tex` 原 line 329, subsection E.1 内新 `\paragraph{Ridge regression under multicollinearity.}` | RidgeCV λ=0.001, β_BCS=−1.53, β_centrality=0.78, R²=0.594; 解析证明 β_BCS<0 对所有 λ≥0 成立; 仅做方向性解读 |
| **B: Bootstrap CI** | 新 subsection E.3 (`sec:appendix_bootstrap_ci`, page 17) | 164 FewRel batches, 6 个 Jaccard 阈值下 cluster-robust SE = 0.96–0.97× OLS SE, slope 显著 (p<10⁻¹¹), R² CI 宽度变化 −6%~+6%, 结论 robust |
| **C: Domain Distribution** | 新 subsection E.4 (`sec:appendix_domain_distribution`, page 17) | χ²=230.74 (p<0.001), high-BCS→science/taxonomy 49.5% + event/temporal 26.0%, low-BCS→geography 45.5% + creative_work 25.5%; 解释为 mediator 非独立 confound |

**编译结果**: 0 errors, 0 undefined references, 27 pages total (body ≤ 8 pages, appendix 从 page 13 起)。`\ref{sec:appendix_partial_corr}` 正确解析为 E.1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r26_integrate_analyses_20260522T052238"
}
```

</details>

---
