# verify final partA D

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_verify_final_partA_D_20260523T191636.jsonl`
- **Structured JSON:** [`a84c3e623c94047ae8c0.json`](../../sessions/a8/a84c3e623c94047ae8c0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-23T19:28:35.269347+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T19:28:35.269692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T19:28:35.269901+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
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
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'conclusion': 'success'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T19:28:35.270424+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"detect_remove_q05_v2_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:06:03.506Z\", \"updated_at\": \"2026-05-22T09:06:49.826Z\", \"metrics\": {\"holdout_loss\": 2.8491, \"holdout_ppl\": 17.2723, \"owt_loss\": 2.8908, \"owt_ppl\": 18.0079, \"wiki_loss\": 2.7111, \"wiki_ppl\": 15.0465, \"eval_holdout_tokens\": 4077068, \"eval_owt_tokens\": 6767242, \"eval_wiki_tokens\": 27000339, \"total_steps\": 6103, \"train_loss\": 11.01}, \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints .../detect_remove_q05_v2_seed123_r2/final --max_docs 5000 --max_length 2048\", \"server\": \"westd-41312\", \"data_path\": \"data/human/eval_holdout.jsonl, data/eval_openwebtext.jsonl, data/eval_wikipedia.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123_r2/final\", \"eval_data\": \"holdout+owt+wiki\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123_r2/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/eval_results/detect_remove_q05_v2_seed123_r2/\", \"hypothesis\": \"D&R hard filtering with seed123 should reproduce seed42 results (holdout~17.3, owt~18.0, wiki~15.1), confirming that detect-and-remove is stable across seeds.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:06:49.826Z\"}, \"bs16_adaptive_tau07_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:35:00.036Z\", \"updated_at\": \"2026-05-21T23:35:27.544Z\", \"metrics\": {\"holdout_loss\": 2.8688, \"holdout_ppl\": 17.616, \"owt_loss\": 2.9083, \"owt_ppl\": 18.325, \"wiki_loss\": 2.731, \"wiki_ppl\": 15.349}, \"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau
…[truncated 21062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:28:35.270619+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T19:28:35.270759+00:00_

docs/paper/sections/checklist.tex
docs/paper/sections/experiments.tex
docs/paper/sections/method.tex
docs/paper/main.tex
docs/paper/sections/limitations.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/introduction.tex
docs/paper/sections/abstract.tex
docs/paper/sections/discussion.tex
docs/paper/sections/related_work.tex
docs/paper/sections/results.tex
docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:28:35.270971+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:28:35.271577+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"detect_remove_q05_v2_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:06:03.506Z\", \"updated_at\": \"2026-05-22T09:06:49.826Z\", \"metrics\": {\"holdout_loss\": 2.8491, \"holdout_ppl\": 17.2723, \"owt_loss\": 2.8908, \"owt_ppl\": 18.0079, \"wiki_loss\": 2.7111, \"wiki_ppl\": 15.0465, \"eval_holdout_tokens\": 4077068, \"eval_owt_tokens\": 6767242, \"eval_wiki_tokens\": 27000339, \"total_steps\": 6103, \"train_loss\": 11.01}, \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints .../detect_remove_q05_v2_seed123_r2/final --max_docs 5000 --max_length 2048\", \"server\": \"westd-41312\", \"data_path\": \"data/human/eval_holdout.jsonl, data/eval_openwebtext.jsonl, data/eval_wikipedia.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123_r2/final\", \"eval_data\": \"holdout+owt+wiki\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123_r2/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/eval_results/detect_remove_q05_v2_seed123_r2/\", \"hypothesis\": \"D&R hard filtering with seed123 should reproduce seed42 results (holdout~17.3, owt~18.0, wiki~15.1), confirming that detect-and-remove is stable across seeds.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:06:49.826Z\"}, \"bs16_adaptive_tau07_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:35:00.036Z\", \"updated_at\": \"2026-05-21T23:35:27.544Z\", \"metrics\": {\"holdout_loss\": 2.8688, \"holdout_ppl\": 17.616, \"owt_loss\": 2.9083, \"owt_ppl\": 18.325, \"wiki_loss\": 2.731, \"wiki_ppl\": 15.349}, \"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau
…[truncated 32172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:28:35.271753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T19:28:35.271982+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	A paired $t$-test yields $t{=}{-}7.1$, $p{=}0.019$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.078$, which does not reach conventional significance, though the 95\% BCa bootstrap CI $[{-}0.028, {-}0.012]$ excludes zero.
9	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
10	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
11	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
15	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
16	Only the dual-constr
…[truncated 10325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:28:35.272145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T19:28:35.272300+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	Our self-contamination design provides a controlled testbed with known ground-truth labels but limits ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss this limitation in \S\ref{sec:limitations}.
6	
7	\paragraph{Detector.}
8	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
9	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
10	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
11	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
12	
13	\paragraph{Training.}
14	We continue pretraining Qwen3-0.6B from its pretrained 
…[truncated 1914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:28:35.272441+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T19:28:35.272575+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled continued pretraining experiments (Qwen3-0.6B, 3 seeds), we analyze when and why detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the reported advantage shrinks from 0.396 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of published gains reflect data repetition rather than filtering quality.
6	Second, effective reweighting requires both discrimination and calibration from the detector; a poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform training, while a calibrated alternative succeeds.
7	Third, minimum intervention---applying the smallest sharpening exponent meeting a quality floor---outperforms unconstrained maximization.
8	
9	As a practical corollary, these findings yield an adaptive $b^*$ that improves over uniform at $\rho \geq 0.4$ ($\Delta{=}{-}0.020$; $\rho{=}0.6$: $\Delta{=}{-}0.032$, uncorrected $p{=}0.009$), transitioning from harmful ($\rho{=}0.2$) to beneficial with a sharp boundary in $[0.3, 0.4]$.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:28:35.272707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T19:28:35.272875+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
11	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
12	
13	Our analysis yields three findings:
14	\begin{itemize}[nosep,leftmargin=*]
15	\item \textbf{Epoch confound in D\&R evaluation.}
16	The bulk of D\&R's PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure, not filtering quality; epoch-matched controls ($N{=}3$) reduce the gap from 0.396 to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
17	
18	\item \textbf{De
…[truncated 2596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:28:35.273034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T19:28:35.273207+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The bulk of D\&R's reported PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality (\S\ref{sec:main-results}).
3	An independent-LR replication (D\&R $17.651$ vs.\ shared-schedule $17.657$, $\Delta{=}0.006$) confirms that this finding is robust to LR schedule choice.
4	In multi-epoch continued pretraining, D\&R evaluations that do not control for content epochs systematically overstate filtering effectiveness; the residual benefit ($\Delta{=}0.017$ vs.\ adaptive $\bstar$, directionally consistent across 3 seeds) falls within cross-seed variance.
5	A permuted-score control (shuffled detector scores; 3-seed mean $17.951{\pm}0.007$, $+$0.26 vs.\ uniform) confirms that detector signal is load-bearing: uninformed reweighting only degrades.
6	
7	\paragraph{When uniform beats reweighting.}
8	Beyond the evaluation confound, our results identify three operational conditions for effective reweighting, each of which, when violated, makes uniform training preferable.
9	First, \emph{detector quality}: the detector must provide both sufficient discrimination (AUC) and good calibration (ECE).
10	A high-AUC but poorly calibrated detector (GPT-2, ECE\,=\,0.131) degrades PPL by $+$0.098 below uniform; even a well-calibrated detector with insufficient discrimination (N-gram, AUC\,=\,0.73) degrades by $+$0.129 (\S\ref{sec:robustness}).
11	Second, \emph{contamination level}: at $\rho{=}0.2$, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal ($\aeff$-binding at 60.1\% despite mean $q{=}0.393$), degrading PPL by $+$0.046; the method transitions from harmful to beneficial with a sharp sign change in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}).
12	Third, \emph{scale}: at 1.7B the benefit diminishes ($\Delta{=}{-}0.013$) with OOD partially inconsistent, suggesting that larger models may be inh
…[truncated 6166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:28:35.273368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T19:28:35.273698+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
20	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	Since $r_i = \mathbf{1}[q_i \leq 0.5]$, the indicator $r_i$ and $\ln(1{-}q_i)$ are positively associated by construction, so the covariance is non-negative.
29	\end{proof}
30	
31	\begin{proposition}[ESS monotonicity]
32	\label{prop:ess_mono}
33	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
34	\end{proposition}
35	
36	\begin{proof}
37	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
38	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
39	Differentiating $H$ with respect to $b$:
40	\begin{equation*}
41	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
42	\end{equation*}
43	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; th
…[truncated 27799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:28:35.273939+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "memory.md",
  "max_chars": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "memory.md",
    "max_chars": "50000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T19:28:35.274145+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/memory.md\", \"content\": \"# Memory\\n\\n## D062 coupling rule 已验证 (2026-05-17)\\n\\nbs8_auto_nmin_r5 (PPL 17.66) 确认 n_min=⌊B/2⌋ coupling rule 在 bs=8 下有效（n_min=4）。\\n- bs=4, n_min=2: adaptive_fix PPL=17.653 (success)\\n- bs=8, n_min=4: bs8_auto_nmin_r5 PPL=17.66 (success)\\n- bs=8, n_min=2: bs8_nmin2_seed42_r2 PPL=17.73 (negative — n_min 过小导致 over-downweight)\\n\\n结论：n_min=⌊B/2⌋ 是 Method section 的正式设计原则。n_min 过小 (< B/2) 导致 ESS 约束松弛，b* 过大。\\n\\n## Batch-adaptive τ 方向关闭 (2026-05-17)\\n\\n两轮实验均 negative。固定 τ=0.8 + dual constraint 已足够。不再投入资源。\\n\\n## Claim 2 跨 seed 已由 D074 定稿 (2026-05-18)\\n\\ngrid b=0.3 三 seed (17.620±0.033) vs adaptive (17.651±0.007)，gap 0.031 在方差内。\\n\\n## Claim 3 ρ=0.6 三 seed 完整 (2026-05-18)\\n\\nAdaptive: mean 17.736±0.004 vs Uniform: mean 17.763±0.008, Δ=0.028。\\nadaptive 方差仅为 uniform 的一半。\\n\\n## ρ=0.2 adaptive 无效 (2026-05-17)\\n\\nD068 决定 Claim 3 scope 限制为 ρ≥0.4, τ∈[0.7,0.8]。ρ=0.2 在 Discussion 报告为 limitation。\\n\\n## ρ=0.3 boundary check 结果 (2026-05-23, 3-seed 定稿)\\n\\n| | Adaptive holdout | Uniform holdout | Δ holdout | Δ OWT | Δ Wiki |\\n|------|-----------------|----------------|-----------|-------|--------|\\n| seed42 | 17.422 | 17.422 | 0.000 | +0.010 | −0.032 |\\n| seed123 | 17.435 | 17.433 | +0.002 | +0.022 | −0.039 |\\n| seed456 | 17.424 | 17.419 | +0.005 | +0.006 | −0.007 |\\n| **mean** | **17.427** | **17.425** | **+0.002** | **+0.013** | **−0.026** |\\n\\n**结论：ρ=0.3 是 transition zone（3-seed 确认）。** Adaptive 在 holdout/OWT 上无效（mean Δ = +0.002/+0.013），仅 wiki 上有微弱优势（−0.026）。\\n- vs ρ=0.2: adaptive 有害 → ρ=0.3: 中性 → ρ=0.4: 有效 (Δ=−0.020)\\n- 3-seed 内 Δ holdout 范围 [0.000, +0.005]，非常稳定\\n- 论文可报告为：\\\"method becomes effective at ρ ≥ 0.4; at ρ=0.3 the signal is too weak for reliable reweighting\\\"\\n\\n## Grid-b 曲线平坦性 (2026-05-17)\\n\\n[0.2, 0.5] 区间 PPL 极平坦（b=0.2: 17.643, b=0.3: 17.640, b=0.5: 17.651）。adapti
…[truncated 3725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:28:35.274305+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "report.md",
  "max_chars": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "report.md",
    "max_chars": "50000"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T19:28:35.274487+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/report.md\", \"content\": \"# Handover — 2026-05-23\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| aeff_only_nmin1_seed123 | α_eff-only ablation seed123: cross-seed replicate of aeff_only_nmin1_seed42. n_min=1 removes ESS constraint, isolating α_eff signal contribution. | — | — | — |\\n| aeff_only_nmin1_seed42 | α_eff-only ablation: adaptive reweighting with n_min=1 (ESS≥1 always satisfied, only α_eff≤τ active). If PPL worse than dual-constrained (n_min=2, 17.674±0.007), ESS constraint has independent value beyond α_eff signal. Addresses R11-C2 + R12-W1. | — | — | — |\\n| bs8_nmin4_uniform_seed456_r2 | seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size amplification statistical analysis. | — | — | — |\\n\\n## 待处理\\n- aeff_only_nmin1_seed456: α_eff-only ablation seed456: cross-seed replicate. n_min=1 removes ESS constraint. Third seed for paired t-test vs dual-constrained baseline.（准备中）\\n- detect_remove_q05_seed42: Detect-and-remove baseline: hard filtering removes samples with TF-IDF q_score < 0.5. If adaptive reweighting (PPL=17.674) outperforms hard removal, it demonstrates that soft scoring preserves useful signal from partially contaminated samples that hard thresholding discards.（准备中）\\n- eval_adaptive_1_7b_seed123（准备中）\\n- eval_uniform_1_7b_seed123（准备中）\\n- detect_remove_q05_epoch_matched（准备中）\\n- detect_remove_q07_seed42_r2（准备中）\\n- adaptive_1_7b_planb_control（准备中）\\n- eval_q01_final（准备中）\\n- status_check_41312（准备中）\\n- eval_adaptive_1_7b（准备中）\\n- …另有 8 项\\n\\n## 近期结论\\n- **bs8_nmin4_uniform_seed456** (killed): seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size amplification statistical analysi
…[truncated 3427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:28:35.274635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T19:28:35.274785+00:00_

1	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with token-level contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
2	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
3	Rather than selecting $b$ via grid search~\citep{drayson2025detection}, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
4	
5	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
6	
7	\paragraph{Quality floor.}
8	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ indicate likely-real samples. The \emph{effective real proportion} $\aeff(b) = \sum_i w_i(b) r_i / \sum_i w_i(b)$ measures weight allocated to real samples.
9	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
10	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.70$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
11	
12	\paragraph{Stability ceiling.}
13	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
14	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
15	
16	\paragraph{Adaptive $\bstar$.}
17	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
18	The optimal exponent implements \emph{minimum intervention}:
19	\begin{equation}
20	  b^{*} = \begin{cases}
21	    0        & \text{if } \aeff(0) \geq \tau, \\
22	    b_\tau   & \text{if } b_\
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T19:28:35.274961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T19:28:35.275093+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the advantage); (2) detectors require both discrimination \emph{and} calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ improves over uniform at $\rho \geq 0.4$ (directionally consistent across all seeds; $\rho{=}0.6$: uncorrected $p{=}0.009$) without tuning; batch-size amplification is monotonic across $B \in \{4, 8, 16\}$ ($1.0{\times}$ to $3.4{\times}$).
3	In continued pretraining settings, D\&R evaluations that do not control for content epochs risk overstating filtering effectiveness; for practitioners, reweighting is worthwhile only when $\rho \geq 0.4$ and the detector is well-calibrated (Table~\ref{tab:decision}).
4	Code and data will be released upon acceptance.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:28:35.275218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T19:28:35.275344+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.3, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B cross-model test showed mixed results (Appendix~\ref{app:cross_model}), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; fine-tuned neural classifiers (e.g., ModernBERT, Binoculars) and zero-shot methods (e.g., DetectGPT) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
4	Paired comparisons use $N{=}3$ seeds (2 degrees of freedom), limiting statistical power; results are directionally consistent but the sample size precludes strong generalizability claims.
5	After family-wise correction for nine comparisons, the $\rho{=}0.4$ adaptive-vs-uniform difference does not reach conventional significance ($p_{\mathrm{BH}}{=}0.078$), though the effect is directionally consistent across all seeds and the bootstrap CI excludes zero; the $\rho{=}0.6$ comparison also falls short of conventional significance under full-family correction ($p_{\mathrm{BH}}{=}0.064$, $k{=}9$), though the uncorrected $p{=}0.010$ and dose-response pattern across $\rho$ levels support a real effect.
6	The self-contamination setup provides known ground-truth labels but represents an easier detection scenario than cross-model contamination, where generator--corpus distribution mismatch may reduce detector accuracy.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T19:28:35.275476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T19:28:35.275638+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4,dubey2024llama}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; M
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:28:35.275775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T19:28:35.275933+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	\input{sections/abstract}
40	\end{abstract}
41	
42	\section{Introduction}
43	\label{sec:intro}
44	\input{sections/introduction}
45	
46	\section{Related Work}
47	\label{sec:related}
48	\input{sections/related_work}
49	
50	\section{Method}
51	\label{sec:method}
52	\input{sections/method}
53	
54	\section{Experimental Setup}
55	\label{sec:experiments}
56	\input{sections/experiments}
57	
58	\section{Results}
59	\label{sec:results}
60	\input{sections/results}
61	
62	\section{Discussion}
63	\label{sec:discussion}
64	\input{sections/discussion}
65	
66	\section{Conclusion}
67	\label{sec:conclusion}
68	\input{sections/conclusion}
69	
70	\section*{Limitations}
71	\label{sec:limitations}
72	\input{sections/limitations}
73	
74	\section*{Ethics Statement}
75	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involved. Code and data will be released upon acceptance.
76	
77	\bibliography{references}
78	
79	\ap
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T19:28:35.276133+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_provenance.yaml",
  "max_chars": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_provenance.yaml",
    "max_chars": "50000"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T19:28:35.276387+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_provenance.yaml\", \"content\": \"paper:\\n  title: ''\\n  version: 3\\n  generated_at: '2026-05-15T23:43:55.946378+00:00'\\nclaims:\\n- id: C001\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: α_eff(b) is strictly increasing in b (Proposition 1, part 1)\\n  type: theoretical\\n  evidence:\\n  - Derivative dα_eff/db = α_eff(1-α_eff)(E_w[ln(1-q)|real] - E_w[ln(1-q)|synth])\\n    > 0 since real samples have lower q-scores\\n  decisions:\\n  - D021\\n  - D023\\n  deprecated: true\\n- id: C003\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: ESS(b) is strictly decreasing in b (Proposition 1, part 2)\\n  type: theoretical\\n  evidence:\\n  - Increasing b concentrates weight mass on fewer low-q samples, reducing ESS\\n  decisions:\\n  - D023\\n  deprecated: true\\n- id: C006\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: 40.1% of reweighted batches are α_eff-binding (regime 2), where b* = 1.67\\n    on average\\n  type: empirical\\n  evidence:\\n  - 'adaptive_fix_seed42 batch-level analysis (Q1): 51,913 micro-batches, 49.9% clean,\\n    20.2% α_eff binding, 30.0% ESS binding'\\n  decisions:\\n  - D023\\n  deprecated: true\\n- id: C010\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: ESS-only approach selects b* = 4.15 for the same α_eff-binding batches — 2.5×\\n    more aggressive exponent\\n  type: empirical\\n  evidence:\\n  - 'adaptive_fix_seed42 batch-level analysis (Q1): counterfactual ESS-only b* computed\\n    for α_eff-binding batches'\\n  decisions:\\n  - D023\\n  - D029\\n  deprecated: true\\n- id: C015\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: α_eff-binding batches retain ESS = 2.60, well above floor n_min = 2\\n  type: empirical\\n  evidence
…[truncated 9711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:28:35.276557+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T19:28:35.276714+00:00_

artifacts/weighting/__init__.py
artifacts/detector/train_detector.py
artifacts/data_generation/__pycache__/generate_synthetic.cpython-314.pyc
artifacts/evaluation/eval_pipeline.py
artifacts/evaluation/compare_results.py
artifacts/run_mvp.sh
artifacts/data_generation/generate_synthetic.py
artifacts/_project/data/tfidf_detector_results.txt
artifacts/_project/report/eval_code_status.md
artifacts/evaluation/eval_code_status.md
artifacts/training_progress_check.md
artifacts/_project/report/eval_perplexity_mvp_report.md
artifacts/_project/report/interim_mvp_analysis.md
artifacts/interim_mvp_analysis.md
artifacts/grid_b5_0_seed123/report/diagnose_grid_b5_0_seed123.md
artifacts/_project/report/related_work_notes.md
artifacts/related_work_notes.md
artifacts/_project/report/seed42_diagnostic.md
artifacts/_project/report/seed42_diagnostic_5dbe1d.md
artifacts/seed42_diagnostic.md
artifacts/_project/chart/adaptive_seed_comparison_ref.txt
artifacts/_project/chart/adaptive_diagnostic_distributions_ref.txt
artifacts/worker_output.md
artifacts/training/extract_train_metrics.py
artifacts/_project/paper/experiment_setup_draft.md
artifacts/_project/report/literature_notes.md
artifacts/literature_notes.md
artifacts/experiment_setup_draft.md
artifacts/_project/paper/method_section_draft.md
artifacts/method_section_draft.md
artifacts/_project/report/mvp_analysis_summary.md
artifacts/_project/report/bstar_distribution_analysis.md
artifacts/bstar_distribution_analysis.md
artifacts/literature_diff_drayson.md
artifacts/drayson_comparison.md
artifacts/novelty_drayson_analysis.md
artifacts/_project/report/novelty_drayson_analysis.md
artifacts/_project/report/literature_diff_drayson.md
artifacts/_project/report/mvp_analysis_draft.md
artifacts/mvp_analysis_draft.md
artifacts/mvp_analysis_summary.md
artifacts/dream_reports/dream_20260515T011902/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260515T011902/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T011902/logs/pha
…[truncated 3452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_final_partA_D_20260523T191636",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-23T19:28:35.277141+00:00_

数据收集完毕。现在系统性核对所有数据点。

---

## Part A: Registry 交叉核对

### Table 1 (Main PPL, ρ=0.4, τ=0.7)

**Uniform 3-seed:**
- [Uniform seed42=17.694] 无对应 registry entry (qwen06b_uniform_seed42 仍 RUNNING) ⚠️ 无法追溯
- [Uniform seed123=17.686] exp_id=uniform_ood_seed123: 论文值=17.686, registry=17.686 ✅
- [Uniform seed456=17.702] exp_id=uniform_ood_seed456: 论文值=17.702, registry=17.702 ✅
- [Uniform mean=17.694±.008] 计算: (17.694+17.686+17.702)/3=17.694, SD=0.008 ✅

**Adaptive b* 3-seed (τ=0.7):**
- [Adaptive seed42=17.680] 无 registry entry (τ=0.7 实验未注册) ⚠️ 无法追溯
- [Adaptive seed123=17.666] 无 registry entry ⚠️
- [Adaptive seed456=17.677] 无 registry entry ⚠️
- [Adaptive mean=17.674±.007] 计算: (17.680+17.666+17.677)/3=17.6743≈17.674, SD≈0.007 ✅ 内部一致
- [Δ=-0.020] 17.674-17.694=-0.020 ✅

**Grid (b=0.3) 3-seed:**
- [Grid seed42=17.640] appendix grid table 确认 b=0.3→17.640 ✅
- [Grid seed123=17.579] exp_id=grid_b0_3_seed123: registry=17.58, 论文=17.579 ⚠️ registry 仅 2dp，差 0.001
- [Grid seed456=17.640] exp_id=grid_b0_3_seed456: registry=17.64, 论文=17.640 ✅
- [Grid mean=17.620±.033] 计算: (17.640+17.579+17.640)/3=17.620 ✅; 从 rounded 值计算 SD≈0.035，论文说 0.033 (full precision 计算) ⚠️ 无法精确验证

**ESS-only 3-seed:**
- [ESS-only seed42=17.730] 无 registry entry (ess_only_seed42 未注册) ⚠️
- [ESS-only seed123=17.720] exp_id=ess_only_seed123: RUNNING，无指标 ⚠️
- [ESS-only seed456=17.760] exp_id=ess_only_seed456: RUNNING，无指标 ⚠️
- [ESS-only mean=17.737±.021] 计算: 17.737, SD=0.021 ✅ 内部一致

**Random U(0,2) 3-seed:**
- [Random seed42=17.830] 无 Qwen3 registry entry ⚠️ (registry 中 random_reweight_baseline_seed42 是 Qwen2.5，PPL=17.958); 间接验证: random_reweight_seed123_r5 notes 称 "seed42: +0.136"，17.694+0.136=17.830 ✅ 间接一致
- [Random seed123=17.800] exp_id=random_reweight_seed123_r5: registry=17.801, 论文=17.800 ⚠️ 差 0.001 (rounding)
- [Random seed456=17.777] exp_id=random_reweight_seed456: RUNNING ⚠️ 无法验证
- [Random mean=17.802±.027] 计算: 17.802, SD=0.027 ✅ 内部一致

**Golden Ratio:**
- [Golden Ratio seed42=17.654] 无 registry entry ⚠️ 无法追溯

**Detect & Remove (q>0.3):**
- [D&R seed42=17.250, seed123=17.250, seed456=17.251, mean=17.250±.001] 无 registry entry (detect_remove_q03_seed42 标记为训练失败) ⚠️ 数据源不明

---

### Epoch-Match Table (D&R q>0.5)

**D&R full (q>0.5) 3-seed:**
- [D&R full seed42=17.285] exp_id=detect_remove_q05_v2_seed42: registry=17.2853→17.285 ✅
- [D&R full seed123=17.272] exp_id=detect_remove_q05_v2_seed123_r2: registry=17.2723→17.272 ✅
- [D&R full seed456=17.277] 无 registry entry ⚠️; memory.md 记录=17.277 ✅
- [D&R full mean=17.278±.007] memory.md=17.278±.007 ✅

**D&R epoch-matched 3-seed:**
- [Epoch-matched seed42=17.651, seed123=17.659, seed456=17.660, mean=17.657±.005] memory.md 完全一致 ✅; 无 registry entry ⚠️

---

### Table 2 / Detector Decision Summary

**N-gram:**
- [AUC=0.73] 无独立 registry 验证 ⚠️
- [ECE=0.069] appendix detector table 确认 ✅
- [Δ PPL=+0.129] 17.823-17.694=0.129 ✅; registry ngram_adaptive=17.82, vs_ngram_uniform="+0.13" ✅

**GPT-2:**
- [AUC=0.91] 无独立 registry 验证 ⚠️
- [ECE=0.131] appendix detector table 确认 ✅
- [Δ PPL=+0.098] 17.792-17.694=0.098 ✅

**TF-IDF:**
- [AUC=0.94] paper_provenance=0.939 ⚠️ 论文 round 到 0.94; appendix detector table=0.94 ✅
- [ECE=0.048] appendix detector table=0.048 ✅; experiments.tex 写 "0.05" ⚠️ 精度不一致 (Part D)
- [Δ PPL=-0.020 (τ=0.7 main)] Table 1 Δ=-0.020 ✅; detector table (τ=0.8) Δ=-0.044 ✅ (不同 τ，正确)

---

### Batch-size Amplification

**B=4:**
- [Δ=-0.020±0.008] memory.md 确认 ✅

**B=8:**
- [Δ=-0.050 (2-seed mean)] memory.md: seed42 Δ=-0.044, seed123 Δ=-0.056, mean=-0.050 ✅
- [seed42: adaptive=17.650, uniform=17.694] memory.md 确认 ✅; registry bs8_auto_nmin_r5=17.66 ⚠️ 不匹配 (不同实验 run，bs8_auto_nmin vs bs8_nmin4_adaptive)
- [seed123: adaptive=17.631, uniform=17.687] memory.md 确认 ✅; 无 registry entry

**B=16:**
- [Δ=-0.068±0.005 (3 seeds)] memory.md: adaptive=17.631±0.008, uniform=17.694±0.015, Δ=-0.068±0.005 ✅
- [seed123] exp_id=bs16_adaptive_tau07_seed123_r2: registry holdout_ppl=17.616; memory 没有 per-seed B=16 数据 ⚠️

---

### Constraint Regime (τ=0.7)

- [ρ=0.4: 50.9% α_eff / 43.3% ESS / 5.8% clean] 论文 results.tex:126 + appendix:144 一致 ✅; 来自 step_metrics 分析，无 registry 验证 ⚠️
- [ρ=0.6: 46.8% α_eff / 48.7% ESS / 4.5% clean] appendix:145 确认 ✅; 同上 ⚠️
- [Sharpening ratio 5.8×] introduction:22 引用; 需 α_eff-binding batches 的 b* 数据验证。论文说 adaptive mean b*=1.4, ESS-only=3.5-5.9。整体比例 5.9/1.4=4.2×≠5.8×。5.8× 可能是 α_eff-binding batches 子集的比例 ⚠️ 无法独立验证

---

### ρ Sensitivity

**ρ=0.2:**
- [Δ=+0.046] 论文 discussion:11 + appendix rho02:392 一致 ✅; registry rho02_adaptive_tau09_r5 给出 +0.114 但那是 τ=0.9 (不同配置) ⚠️; τ=0.8 的 rho02 实验 (rho02_adaptive_tau08_seed42) 仍 RUNNING

**ρ=0.3:**
- [Δ=+0.002 (3-seed)] appendix rho03 table + memory.md 完全一致 ✅
  - seed42: A=17.422, U=17.422, Δ=0.000 ✅
  - seed123: A=17.435, U=17.433, Δ=+0.002 ✅
  - seed456: A=17.424, U=17.419, Δ=+0.005 ✅

**ρ=0.6:**
- [Δ=-0.032, p=0.009] appendix rho06 table 确认:
  - seed42: A=17.735, U=17.766, Δ=-0.031
  - seed123: A=17.727, U=17.754, Δ=-0.027
  - seed456: A=17.732, U=17.770, Δ=-0.038
  - Mean Δ=-0.032 ✅
  - **p 值不一致**: 主文 results.tex:94 写 p=0.009; appendix rho06 caption:283 写 "3dp rounding yields t=−9.95, p=0.010" ❌ 同一计算给出不同 p 值
  - 独立验证: t=-9.95, df=2 → two-sided p=0.010, 非 0.009 ❌ 主文 p=0.009 错误

---

### 1.7B Scale

- [Adaptive 13.26, Uniform 13.28, Δ=-0.013] ❌ **严重不一致**
  - exp_id=eval_adaptive_1_7b_v2: registry=13.27 (≠论文 13.26)
  - exp_id=eval_uniform_1_7b_v3: registry=13.50 (≠论文 13.28，差 0.22!)
  - memory.md: "adaptive PPL=13.27 vs uniform PPL=13.50, Δ=-0.23"
  - 论文声称 "3 seeds" 但 report.md 显示 eval_adaptive_1_7b_seed123 / eval_uniform_1_7b_seed123 仍为 "准备中"
  - **论文 Δ=-0.013 与所有可追溯数据 (Δ=-0.23 single seed) 严重矛盾**

---

### Downstream

- [Mean accuracy=0.5414 for both] 无法从 registry 完整验证 ⚠️; registry adaptive_fix_seed42 downstream 值与 appendix per-seed 值不完全一致（可能不同 eval 配置）

---

### 统计量重算

**ρ=0.4 paired t-test:**
- 从 3dp per-seed: Δ=(-0.014, -0.020, -0.025), mean=-0.0197, SD=0.00551, t=-6.19
- 论文说 t=-7.1 (full precision 计算), p=0.019 → 对 t=-7.1, df=2: p≈0.019 ✅
- p_BH=0.078 (k=9): 无法独立验证（需全部 9 个 p 值）⚠️
- Bootstrap CI [-0.028, -0.012]: 论文已标注无法独立验证 ⚠️

**ρ=0.6 paired t-test:**
- 从 3dp per-seed: Δ=(-0.031, -0.027, -0.038), mean=-0.032, SD=0.00557, t=-9.95
- t=-9.95, df=2 → p=0.010
- 论文主文 p=0.009 ❌, appendix p=0.010 ✅

**Cohen's d = 2.86:**
- 从 paired Δ: d = |mean|/SD_paired = 0.020/0.00551 = 3.63 (rounded values)
- 若用 pooled group SD: SD_pooled ≈ 0.007, d = 0.020/0.007 = 2.86 ✅
- 注意: 2.86 用的是 pooled group SD，不是 paired difference SD；若标注为 "paired"，定义需要明确

**BH correction k=9:**
- 论文 ρ=0.4: p_BH=0.078; ρ=0.6: p_BH=0.064
- 无法验证（需全部 9 个 uncorrected p 值）⚠️

---

## Part D: 精度一致性

### PPL 值 (应统一 3dp)

- [results.tex:101] `13.26` → 应为 `13.260` ⚠️ 2dp 不一致
- [results.tex:101] `13.28` → 应为 `13.280` ⚠️ 2dp 不一致
- [appendix:199] dr_threshold 表 `17.40` → 应为 `17.400` ⚠️
- [appendix:200] `17.27` → 应为 `17.270` ⚠️
- [appendix:203] `17.28` → 应为 `17.280` ⚠️
- [appendix:204] `17.30` → 应为 `17.300` ⚠️
- [appendix:205] `17.32` → 应为 `17.320` ⚠️
- [appendix:206] `17.34` → 应为 `17.340` ⚠️
- [appendix:207] `17.42` → 应为 `17.420` ⚠️
- [appendix:199] `18.04` → 应为 `18.040` ⚠️
- [appendix:201] `17.74` → 应为 `17.740` ⚠️
- [appendix:203] `17.65` → 应为 `17.650` ⚠️
- [appendix:205] `17.62` → 应为 `17.620` ⚠️

### p 值 (应统一 3dp)

- [results.tex:94] `p=0.009` vs [appendix:283] `p=0.010` ❌ 同一统计量不一致
- 其余 p 值 (0.019, 0.009 in abstract) 均 3dp ✅

### ECE (精度不一致)

- [experiments.tex:8] `ECE=0.05` (2dp) vs [appendix detector table:349] `ECE=0.048` (3dp) ⚠️ 同一数值不同精度

### Δ PPL (应统一 3dp)

- [discussion.tex:5] `+0.26` → 应为 `+0.257` ⚠️ 2dp 不一致

### 百分比 (应统一 1dp)

- 所有百分比 (50.9%, 43.3%, 5.8%, 46.8%, 48.7%, 4.5%, 46.3%) ✅ 均为 1dp

---

## 关键问题汇总

| 严重度 | 问题 | 位置 |
|--------|------|------|
| ❌ **严重** | 1.7B 数据与 registry 严重矛盾: 论文 Δ=-0.013 (adaptive=13.26, uniform=13.28), registry/memory Δ=-0.23 (adaptive=13.27, uniform=13.50); 论文声称 3-seed 但实验尚未完成 | results.tex:100-101 |
| ❌ | ρ=0.6 p 值不一致: 主文写 p=0.009, appendix 同一计算写 p=0.010; 独立验算确认 p=0.010 | results.tex:94 vs appendix:283 |
| ⚠️ | D&R (q>0.3) Table 1 数据 (17.250±.001) 无 registry entry 可追溯 | results.tex:65 |
| ⚠️ | τ=0.7 adaptive per-seed 值 (17.680/17.666/17.677) 无 registry entry | results.tex:60 |
| ⚠️ | Random U(0,2) seed42=17.830 和 seed456=17.777 无 Qwen3 registry entry | results.tex:62 |
| ⚠️ | 1.7B PPL 2dp (13.26/13.28) 违反全文 3dp 精度约定 | results.tex:101 |
| ⚠️ | Appendix dr_threshold 表 11 个 PPL 值为 2dp，与全文 3dp 约定不一致 | appendix:199-208 |
| ⚠️ | ECE 精度不一致: experiments.tex 写 0.05, detector table 写 0.048 | experiments.tex:8 |
| ⚠️ | discussion.tex Δ=+0.26 应为 +0.257 (3dp) | discussion.tex:5 |

**最优先修复**: 1.7B 数据需要核实——如果 3-seed 实验确实未完成，论文不能声称 "3 seeds"；如果已有新数据使 Δ 从 -0.23 变为 -0.013，需要更新 registry。ρ=0.6 的 p=0.009→0.010 需要统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_verify_final_partA_D_20260523T191636"
}
```

</details>

---
