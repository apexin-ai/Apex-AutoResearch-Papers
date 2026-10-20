# Director coordination — Part 5 of 5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/34/344e7a91893ffee82516.json)

## Round 114

### Tool result

_source line 1199 · 2026-05-25T21:14:34.569578+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in three stages (Figure~\ref{fig:pipeline}): Stage~1 estimates per-item contamination exposure via training-free signal fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to recover clean ability estimates with credible intervals; Stage~3 classifies dose-response trajectories into canonical patterns.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{de_ayala_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoni
…[truncated 7656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-25T21:14:34.569982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1201 · 2026-05-25T21:14:35.072875+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\begin{table}[t]
5	\centering
6	\caption{MMLU method comparison on a single random subsample of 300 items (Qwen2.5, $J$=16). ARC and GSM8K baselines in Appendix~\ref{sec:full_baselines}; ARC IRT diagnostics in Appendix~\ref{sec:arc_irt}.}
7	\label{tab:baselines}
8	\footnotesize
9	\begin{tabular}{lcc}
10	\toprule
11	Method & MAE & $\tau$ \\
12	\midrule
13	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
14	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
15	B3: Vanilla 2PL & 0.008 & 0.731 \\
16	B4: Linear Regression & 0.010 & 0.751 \\
17	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
18	B6: DCR (reimpl.) & 0.108 & 0.654 \\
19	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	\subsection{Controlled SFT Injection}
25	\label{sec:injection}
26	
27	We construct a controlled contamination testbed spanning five independent model families from five labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), Gemma-2 \citep{gemmateam2024gemma2} (9B), and Falcon3 \citep{tiiuae2024falcon3} (7B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, dropout$=0$, targeting all attention and multilayer perceptron (MLP) projections; lr$=5\times10^{-5}$, bf16, 1 epoch, batch size$=1$, gradient accumulation$=16$, warmup ratio$=0.03$; trainable parameters range from 0.45\% of Phi-4 14.7B to 2.10\% of Qwen2.5-0.5B; convergence in Appendix~\ref{sec:training_convergence}) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) to
…[truncated 5101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-25T21:14:35.073399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-25T21:14:35.525616+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.88\columnwidth]{figures/fig_cross_benchmark_heatmap.pdf}
7	\caption{Cross-benchmark transfer at d100. MMLU contamination improves GSM8K in four of five non-excluded families, even those harmed on MMLU; Phi-4 shows near-zero transfer. Gemma-2 GSM8K ($+$1.33pp) is based on a low baseline (17.8\%, CoT collapse under MC-format SFT) and is excluded from Table~\ref{tab:gsm8k_transfer}.}
8	\label{fig:cross_benchmark_heatmap}
9	\end{figure}
10	
11	Cross-family SFT-injection results (\S\ref{sec:taxonomy}) use seed$=$42 data across six models from five independent families ($\leq$3B dose-response in Appendix~\ref{sec:dose_response_details}). Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
12	
13	\subsection{Dose-Response Patterns}
14	\label{sec:taxonomy}
15	
16	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families.
17	
18	\paragraph{Replication status.}
19	Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is 
…[truncated 8562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-25T21:14:35.526008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-25T21:14:35.978094+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals a spectrum of dose-response patterns, not uniform inflation. Two replicate across independent families (Benefit, Immune); two are Qwen2.5-specific and await replication. DiD finds no item-specific memorization (MDES 1.25--2.05pp); direction reproduces across seeds but magnitude is seed-sensitive.
4	
5	\paragraph{Contamination vs.\ additional training.}
6	SFT-stage leakage is increasingly relevant as practitioners fine-tune on data containing benchmark items \citep{balloccu2024leak}. Our injection confounds content, volume ($+$33\% at d100), and LoRA updates; a volume-matched control attributes ${\sim}$45\% of Benefit to quantity. Combined with null item-specific memorization (\S\ref{sec:memorization_test}), this suggests contamination operates through global capability modulation rather than item-level lookup.
7	
8	\paragraph{Implications for practice.}
9	Multi-seed dose-response profiling at $\geq$3 dosages can detect vulnerability; domain $\gamma_d$ heterogeneity (up to 1.8$\times$) motivates domain-level controls, and ContamCal can flag anomalous profiles given $J \geq 50$. Cross-benchmark transfer patterns (\S\ref{sec:gsm8k_transfer}) suggest that contamination effects should be assessed per benchmark rather than assumed transferable: a model harmed on MMLU may benefit on GSM8K, and vice versa.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-25T21:14:36.028828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-25T21:14:36.481063+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models $\leq$14.7B with $n\!=\!3$ seeds; 70B+ models may exhibit different contamination dynamics, and borderline classifications (e.g., OLMo-2) should be interpreted with caution. Our LoRA-based SFT injection differs from pretraining-stage leakage; the AUGMENT protocol increases training volume with dosage ($+$33\% at d100), partially confounding content and quantity effects. IRT is fitted on 300 subsampled items (2.1\% of MMLU), and RRF exposure scores are point estimates whose measurement uncertainty is not propagated into $\gamma$ credible intervals.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1208 · 2026-05-25T21:14:36.481594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-25T21:14:36.933645+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-25T21:14:36.933998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-25T21:14:37.336910+00:00_

1	\appendix
2	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
3	\setlength{\belowcaptionskip}{0pt}
4	
5	\section{ARC-Challenge Cross-Benchmark Analysis}
6	\label{sec:arc_cross_benchmark}
7	
8	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for five of six models: OLMo-2 benefits ($+$3.9pp), Falcon3 benefits ($+$4.0pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
9	
10	\paragraph{Cross-seed ARC consistency.}
11	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp, with cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp d
…[truncated 48485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-25T21:14:54.659287+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-25T21:14:54.760150+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-25T21:14:58.123043+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-25T21:14:58.324245+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'config.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-25T21:15:01.291440+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-25T21:15:01.392674+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-25T21:15:05.209274+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contamcal-irt-calibration/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contamcal-irt-calibration/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-25T21:15:05.360495+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-25T21:15:07.971477+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contamcal-irt-calibration/agent/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contamcal-irt-calibration/agent/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-25T21:15:08.022218+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-25T21:15:10.532451+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/projects.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/projects.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-25T21:15:10.634699+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-25T21:15:13.245823+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/",
  "description": "List workspace root directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/",
    "description": "List workspace root directory"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-25T21:15:13.449923+00:00_

AGENTS.md
config
global
idea_generator
projects
skills
state
workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 204
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-25T21:15:16.214666+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/",
  "description": "List config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/",
    "description": "List config directory"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-25T21:15:16.365845+00:00_

approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_briefer.json
mcp_config_director.json
mcp_config_distiller.json
mcp_config_dream_review_director.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_paper_audit_content.json
mcp_config_paper_audit_review_visual.json
mcp_config_paper_audit_visual.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_00dfb0018fc66ec96d8b8ea00616820b.json
mcp_config_worker_074936fc4b5d802648d5b9b7fe3a8a01.json
mcp_config_worker_09731295942d3269e0517509703bed15.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_3223f6c92aba6990fc4fd60c9c817114.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
mcp_config_worker_34a94861e96b7887a157fa6d27e375e0.json
mcp_config_worker_34b8beca3d3e38da8c29b9af314ca15a.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_39b779349130764ce7503c2772342ff4.json
mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
mcp_config_worker_4abc3d757168e825e9637e1693914dfd.json
mcp_config_worker_4dc52b836d4b7ae24139c5fa8c29372a.json
mcp_config_worker_567fac45f9ef5ad1a9223cbb3364faf1.json
mcp_config_worker_592b3808646a7c6e68254a6eac279699.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json
mcp_config_worker_6f0b694c30c8a0575c498898ae58e765.json
mcp_config_worker_6fd17e67a8715a880e8a0fc749aac552.json
mcp_config_worker_72b5a7797b623899786091579596a8b2.json
mcp_config_worker_7f289b4cf49d35629c3aa93f15a08233.json
mcp_config_worker
…[truncated 1399 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-25T21:15:19.930551+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/",
  "description": "List project configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/",
    "description": "List project configs"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-25T21:15:19.981357+00:00_

contamcal-irt-calibration.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-25T21:15:22.491897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/contamcal-irt-calibration.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/projects/contamcal-irt-calibration.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1231 · 2026-05-25T21:15:22.542648+00:00_

1	execution:
2	  gpu_ids:
3	  - 0
4	  project_path: /root/contamcal-irt-calibration
5	  servers:
6	  - cqa1-21977
7	feishu:
8	  chat_id: oc_4960c7baa442eabd4fa0aceeac2693ca
9	  check_references: false
10	  operational_chat_id: oc_a79563aecf81c0da6bbb0710df2f0b6d
11	  review_mode: fresh
12	  review_paper_path: projects/contamcal-irt-calibration/docs/paper/main.tex
13	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_12/submitted.pdf
14	  review_round: 12
15	  review_supplementary_paths: ''
16	  submission_chat_id: oc_da6d629d7f92da47a5e85cb7e296ae13
17	project:
18	  created_at: '2026-05-13T04:23:49.315Z'
19	  description: 'ContamCal: Bayesian Calibration of Contamination-Adjusted Benchmark
20	    Scores via Provenance-Augmented Item Response Theory'
21	  name: contamcal-irt-calibration
22	  phase: research
23	  source_idea_id: idea_017
24	ralph_loop:
25	  enabled: false
26	venue: emnlp-2026
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-25T21:15:26.716427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-25T21:15:26.767037+00:00_

1	venues:
2	  corl-2026:
3	    display_name: CoRL 2026
4	  emnlp-2026:
5	    display_name: EMNLP 2026
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-25T21:15:30.733909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_rules/",
  "description": "List venue rules"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_rules/",
    "description": "List venue rules"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-25T21:15:30.784523+00:00_

corl-2026.yaml
emnlp-2026.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-25T21:15:33.345503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-25T21:15:33.396133+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	  - created_at: '2026-05-23T03:52:31Z'
25	    id: d66635
26	    text: 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section
27	  - created_at: '2026-05-23T11:42:30Z'
28	    id: 8a2af2
29	    text: abstract 不要超过 200 words
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-25T21:15:41.228877+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
  }
}
```

</details>

---


### Tool call

_source line 1239 · 2026-05-25T21:15:42.183884+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check review issues tracker"
  }
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-25T21:15:42.636507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1241 · 2026-05-25T21:15:45.050671+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3821
}
```

</details>

---


### Tool result

_source line 1242 · 2026-05-25T21:15:45.051362+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	% --- LLaMA-3 ---
6	
7	@article{grattafiori2024llama3,
8	  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and others},
9	  title     = {The Llama 3 Herd of Models},
10	  journal   = {arXiv preprint arXiv:2407.21783},
11	  year      = {2024},
12	}
13	
14	% --- Restored entries (required by reviewer) ---
15	
16	@book{camilli_1994_dif,
17	  author    = {Camilli, Gregory and Shepard, Lorrie A.},
18	  title     = {Methods for Identifying Biased Test Items},
19	  series    = {Measurement Methods for the Social Sciences},
20	  publisher = {Sage Publications},
21	  year      = {1994},
22	  address   = {Thousand Oaks, CA},
23	  isbn      = {978-0-8039-4416-9}
24	}
25	
26	@article{swaminathan_1990_dif,
27	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
28	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
29	  journal = {Journal of Educational Measurement},
30	  volume  = {27},
31	  number  = {4},
32	  pages   = {361--370},
33	  year    = {1990},
34	  doi     = {10.1111/j.1745-3984.1990.tb00754.x}
35	}
36	
37	@book{holland_1993_dif,
38	  editor    = {Holland, Paul W. and Wainer, Howard},
39	  title     = {Differential Item Functioning},
40	  publisher = {Lawrence Erlbaum Associates},
41	  year      = {1993},
42	  address   = {Hillsdale, NJ}
43	}
44	
45	@article{xu_2024_leakage,
46	  author        = {Xu, Ruijie and Wang, Zengzhi and Fan, Run-Ze and Liu, Pengfei},
47	  title         = {Benchmarking Benchmark Leakage in Large Language Models},
48	  journal       = {arXiv preprint},
49	  year          = {2024},
50	  eprint        = {2404.18824},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 2414
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-25T21:15:45.102925+00:00_

&lt;persisted-output>
Output too large (41.5KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-director-c2ad40d8/cdadb92b-ca9f-4fe6-b967-ead4a3511049/tool-results/b7m7ib62f.txt

Preview (first 2KB):
- id: "R2-N1"
  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 6
  mentions:
    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks."}
    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'."}
    - {round: 4, reviewers: "R1,R2", note: "Title promises decomposition but core result is nothing to decompose."}
    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
    - {round: 8, reviewers: "", note: "本轮未提及。Title now 'Not All Models Are Inflated'."}
    - {round: 9, reviewers: "", note: "本轮未提及（fresh review）。"}
    - {round: 10, reviewers: "", note: "本轮未提及（fresh review）。"}
    - {round: 11, reviewers: "", note: "本轮未直接提及。新 overclaiming concerns under R8-N3 and R11-N1."}
    - {round: 12, reviewers: "", note: "本轮未直接提及（fresh review）。Title framing itself resolved; overclaiming tracked under R11-N1."}
    - {round: 13, reviewers: "", note: "本轮未直接提及（fresh review）。Title overclaiming tracked under R11-N1."}
  action_items:
    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
    - {round: 4, action: "Reframe as empirical investigation", assigned_to: "paper_agent", status: "done"}
    - {round: 5, action: "Rewrite Introduction as question-driven", assigned_to: "paper_agent",
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 2919
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-25T21:16:16.048875+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Round 1\n\n**你是 Reviewer 1，侧重方法严谨性、实验设计、统计有效性。**\n\n### 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节 \\input 独立 .tex 文件，同目录下）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_12/submitted.pdf`\n\n### Venue 要求（EMNLP 2026 via ARR）\n- 长文正文 ≤ 8 页（严格），引用页数无限\n- Limitations section 必须有，不计入页数\n- Ethics section 可选，不计入页数\n- Appendix 不计入页数，但不应包含评估 novelty/claims 所需的关键材料\n- Double-blind 匿名审稿\n- ACL 模板格式\n- Abstract ≤ 200 words\n- ARR Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计有效性**，重点审查以下方面：\n\n1. **IRT 模型设计**：2PL+γ 的 formulation 是否合理？γ 放在 discrimination bracket 外的 justification 是否充分？Prior sensitivity 问题是否被充分 acknowledge？\n2. **RRF 信号融合**：三个信号（S1 embedding similarity, S2 Min-K%++, S4 Self-Critique）的选择和组合是否有理论依据？S2 的已知 failure mode 是否被充分处理？\n3. **实验设计**：\n   - SFT injection 作为 contamination proxy 的外部效度（vs pretraining-stage leakage）\n   - Volume confound（d100 比 d000 多 33% 训练数据）的控制是否充分\n   - n=3 seeds 的统计功效是否足以支撑 claims\n   - J=16 的 IRT ensemble size 是否足以可靠估计 γ\n4. **统计分析**：\n   - Bootstrap CI 的使用是否恰当\n   - DiD 分析的 parallel trends assumption 是否可信\n   - MDES 和 power analysis 是否正确\n   - Domain-level γ 的 multiple comparison correction（Bonferroni）\n5. **Identifiability**：simulation 中 AUC≥0.55 + J≥50 的要求 vs 实际 J=16 的 gap\n6. **Reproducibility**：实验细节是否足够复现\n\n请输出完整审稿意见，格式如下：\n- **Summary**（2-3句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要 related work）\n- **Overall Assessment**（ARR 评分 + 置信度 + 1-2句总评）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Round 1\n\n**你是 Reviewer 1，侧重方法严谨性、实验设计、统计有效性。**\n\n### 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节 \\input 独立 .tex 文件，同目录下）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_12/submitted.pdf`\n\n### Venue 要求（EMNLP 2026 via ARR）\n- 长文正文 ≤ 8 页（严格），引用页数无限\n- Limitations section 必须有，不计入页数\n- Ethics section 可选，不计入页数\n- Appendix 不计入页数，但不应包含评估 novelty/claims 所需的关键材料\n- Double-blind 匿名审稿\n- ACL 模板格式\n- Abstract ≤ 200 words\n- ARR Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计有效性**，重点审查以下方面：\n\n1. **IRT 模型设计**：2PL+γ 的 formulation 是否合理？γ 放在 discrimination bracket 外的 justification 是否充分？Prior sensitivity 问题是否被充分 acknowledge？\n2. **RRF 信号融合**：三个信号（S1 embedding similarity, S2 Min-K%++, S4 Self-Critique）的选择和组合是否有理论依据？S2 的已知 failure mode 是否被充分处理？\n3. **实验设计**：\n   - SFT injection 作为 contamination proxy 的外部效度（vs pretraining-stage leakage）\n   - Volume confound（d100 比 d000 多 33% 训练数据）的控制是否充分\n   - n=3 seeds 的统计功效是否足以支撑 claims\n   - J=16 的 IRT ensemble size 是否足以可靠估计 γ\n4. **统计分析**：\n   - Bootstrap CI 的使用是否恰当\n   - DiD 分析的 parallel trends assumption 是否可信\n   - MDES 和 power analysis 是否正确\n   - Domain-level γ 的 multiple comparison correction（Bonferroni）\n5. **Identifiability**：simulation 中 AUC≥0.55 + J≥50 的要求 vs 实际 J=16 的 gap\n6. **Reproducibility**：实验细节是否足够复现\n\n请输出完整审稿意见，格式如下：\n- **Summary**（2-3句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要 related work）\n- **Overall Assessment**（ARR 评分 + 置信度 + 1-2句总评）"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-25T21:16:31.336834+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15287
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-25T21:16:31.487827+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Round 1\n\n**你是 Reviewer 2，侧重新颖性、Related Work 完整性、写作质量、整体完成度。**\n\n### 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节 \\input 独立 .tex 文件，同目录下）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_12/submitted.pdf`\n\n### Venue 要求（EMNLP 2026 via ARR）\n- 长文正文 ≤ 8 页（严格），引用页数无限\n- Limitations section 必须有，不计入页数\n- Ethics section 可选，不计入页数\n- Appendix 不计入页数，但不应包含评估 novelty/claims 所需的关键材料\n- Double-blind 匿名审稿\n- ACL 模板格式\n- Abstract ≤ 200 words\n- ARR Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**新颖性 + Related Work 完整性 + 写作质量 + 整体完成度**，重点审查以下方面：\n\n1. **新颖性评估**：\n   - 核心贡献（dose-response profiling, ContamCal framework, domain-level γ diagnosis）相对于现有工作的增量价值\n   - 与 Han et al. (2026) 的 observational DIF 方法和 Schaeffer et al. (2026) 的 controlled pretraining injection 的区分度\n   - \"Not uniform inflation\" 这一 finding 是否足够 novel（考虑 Bordt et al. 2025 已 argue contamination effects are often negligible）\n2. **Related Work 完整性**：\n   - 是否遗漏了 benchmark contamination 领域的重要工作\n   - IRT for LLM evaluation 的引用是否全面\n   - 是否充分引用了 dose-response modeling 和 psychometrics 方面的文献\n3. **写作质量**：\n   - 论文叙事流畅度和逻辑连贯性\n   - Claims 与 evidence 的匹配程度（是否存在 overclaiming）\n   - Abstract 是否准确概括主要贡献（注意 ≤ 200 words 限制）\n   - Figure/Table 的信息密度和可读性\n   - 符号一致性和术语使用\n4. **论文结构和完整度**：\n   - 8 页正文是否包含了所有必要信息，还是过度依赖 Appendix\n   - Limitations section 是否覆盖主要局限\n   - 匿名性是否保持（检查 anonymous link、作者信息泄露）\n   - 格式是否符合 ACL 模板规范\n5. **Presentation 问题**：\n   - 信息过载 vs 遗漏的平衡\n   - 关键 Figure（Fig 1 dose-response, Fig 2 pipeline）的质量\n\n请输出完整审稿意见，格式如下：\n- **Summary**（2-3句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要 related work）\n- **Overall Assessment**（ARR 评分 + 置信度 + 1-2句总评）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Round 1\n\n**你是 Reviewer 2，侧重新颖性、Related Work 完整性、写作质量、整体完成度。**\n\n### 论文信息\n- **标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节 \\input 独立 .tex 文件，同目录下）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_round_12/submitted.pdf`\n\n### Venue 要求（EMNLP 2026 via ARR）\n- 长文正文 ≤ 8 页（严格），引用页数无限\n- Limitations section 必须有，不计入页数\n- Ethics section 可选，不计入页数\n- Appendix 不计入页数，但不应包含评估 novelty/claims 所需的关键材料\n- Double-blind 匿名审稿\n- ACL 模板格式\n- Abstract ≤ 200 words\n- ARR Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**新颖性 + Related Work 完整性 + 写作质量 + 整体完成度**，重点审查以下方面：\n\n1. **新颖性评估**：\n   - 核心贡献（dose-response profiling, ContamCal framework, domain-level γ diagnosis）相对于现有工作的增量价值\n   - 与 Han et al. (2026) 的 observational DIF 方法和 Schaeffer et al. (2026) 的 controlled pretraining injection 的区分度\n   - \"Not uniform inflation\" 这一 finding 是否足够 novel（考虑 Bordt et al. 2025 已 argue contamination effects are often negligible）\n2. **Related Work 完整性**：\n   - 是否遗漏了 benchmark contamination 领域的重要工作\n   - IRT for LLM evaluation 的引用是否全面\n   - 是否充分引用了 dose-response modeling 和 psychometrics 方面的文献\n3. **写作质量**：\n   - 论文叙事流畅度和逻辑连贯性\n   - Claims 与 evidence 的匹配程度（是否存在 overclaiming）\n   - Abstract 是否准确概括主要贡献（注意 ≤ 200 words 限制）\n   - Figure/Table 的信息密度和可读性\n   - 符号一致性和术语使用\n4. **论文结构和完整度**：\n   - 8 页正文是否包含了所有必要信息，还是过度依赖 Appendix\n   - Limitations section 是否覆盖主要局限\n   - 匿名性是否保持（检查 anonymous link、作者信息泄露）\n   - 格式是否符合 ACL 模板规范\n5. **Presentation 问题**：\n   - 信息过载 vs 遗漏的平衡\n   - 关键 Figure（Fig 1 dose-response, Fig 2 pipeline）的质量\n\n请输出完整审稿意见，格式如下：\n- **Summary**（2-3句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要 related work）\n- **Overall Assessment**（ARR 评分 + 置信度 + 1-2句总评）"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-25T21:16:32.852517+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 1248 · 2026-05-25T21:16:37.982983+00:00_

两名 Reviewer 已派发，等待初审结果返回。

**当前状态**：
- Reviewer 1（方法严谨性）：已派发，审稿中
- Reviewer 2（新颖性/完整性）：已派发，审稿中
- 视觉审查 Agent：已启动，异步进行
- 外部审稿：未配置，跳过

等待 Reviewer 返回初审意见后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 115

## Round 115

2 recorded events


### User

_source line 1249 · 2026-05-25T21:23:27.132167+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — Round 1

**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**Venue**: EMNLP 2026 via ARR
**审查侧重**: 方法严谨性、实验设计、统计有效性

---

### Summary

本文提出 ContamCal，一个结合多信号暴露映射（RRF 融合 embedding similarity、Min-K%++、Self-Critique）与污染增强 2PL IRT 模型的框架，用于量化 benchmark contamination 的 dose-response 效应。通过对五个家族六个模型进行五级 SFT 注入实验，发现 contamination 效应是 benchmark-conditional 而非 uniform inflation：三个模型获益、一个免疫、两个坍塌。框架本身有创新性，但核心 γ 估计的 identifiability 不足（J=16 vs. 模拟要求 J≥50）和 volume confound 的不完全控制削弱了论文最强的 claims。

---

### Strengths

**S1. 新颖且理论扎实的框架设计。** 将 IRT 的 item-parameter 估计机制用于分离 contamination 效应与真实 ability，是对该领域的实质性贡献。将 psychometric 传统中的 DIF（Differential Item Functioning）思想迁移到 LLM contamination 诊断场景，理论动机清晰（§3.1, §3.3）。

**S2. 实验规模与控制变量设计严谨。** 五个独立家族、六个模型、三个 benchmark、五级 dosage、n=3 seeds 的 factorial 设计（§4.1），加上 cross-seed（Table 3）和 cross-benchmark（§5.2, Table 4）评估，实验规模在该领域少见。Dose-response 分类算法（Algorithm 1, Appendix S）提供了可操作的诊断工具。

**S3. 极其充分的消融和敏感性分析。** Appendix 涵盖 RRF 信号消融（Table 7）、DIF 参数化对比（Appendix G, Table 10）、prior sensitivity（Appendix L）、volume 控制（Appendix R）、identifiability 模拟（Appendix F）、4PL 扩展（Appendix H）。这种透明度在实证论文中罕见，体现了良好的科学实践。

**S4. 诚实的 limitations 承认。** 论文没有回避 J=16 的 identifiability 不足、SFT vs. pretraining 的 gap、prior sensitivity 等核心局限，这在投稿中不常见。

**S5. 有实用价值的发现。** Cross-benchmark transfer 分析（§5.2：MMLU contamination 在 4/5 家族提升 GSMK）和 benchmark-conditional 效应（§5.1：非 uniform inflation）对 benchmark 设计者和模型评估者有直接参考价值。

**S6. 诊断流水线的工程完整性。** 三阶段 pipeline（Figure 2）从信号融合到 IRT 估计到 dose-response 分类，形成完整的端到端方案，且 RRF 消融（Table 7）和 single-signal 对比（Appendix E, Table 8）验证了 multi-signal fusion 的必要性。

---

### Weaknesses

**W1 [Must-Fix] Identifiability gap：J=16 远低于模拟验证要求的 J≥50，domain-level γ claims 缺乏统计支撑。**
- **具体位置**: §3.3 ("simulation validates that recovery requires AUC≥0.55 with J≥50"), Appendix F (Figure 8), Appendix L
- **问题**: 论文自身的 identifiability simulation（Appendix F）建立了 γ 可靠恢复的下限条件：AUC≥0.55 且 J≥50。实际实验使用 J=16（31 个初始配置排除后剩余 16 个）。这是 3× 的缺口。Prior sensitivity 分析（Appendix L）证实了后果：posterior mean 在三种 prior specification（N(0,1), N(0,0.5), N(0,0.2)）下从 0.34 漂移到 0.89，95% CI 在**所有情况**下均包含零。Bonferroni 校正后 Social Sciences 的显著性（P(γ<0) = 99.35–99.85%）在 tight prior 下以 0.025pp 之差失败。
- **为什么影响接收**: Domain-level γ 估计是论文的核心贡献之一（Contribution 2, §1）。当 γ 对 prior 敏感且 CI 始终包含零时，"calibrated ability estimates with credible intervals"（Abstract）这一 claim 无法成立。论文虽标注 "exploratory"，但 main text 中 Figure 6 和 §5.7 的 presentation 仍给出了具体 γ 数值和方向性结论。
- **建议修改方向**: (a) 在 main text 中将 domain-level γ 分析明确标记为 "illustrative/pilot"，而非作为 key finding 呈现；(b) 讨论实际可行的路径将 J 提升至 ≥50（如纳入更多模型家族/规模变体）；(c) 或将 domain-level 分析移至 appendix，main text 仅保留 aggregate γ 结果。

**W2 [Must-Fix] Volume confound 仅对一个模型做了控制，但显示 43–53% 效应来自数据量而非 contamination 内容。**
- **具体位置**: §4.1（SFT 注入协议）, Appendix R (Table 17)
- **问题**: SFT 注入在更高 dosage 时系统性增加训练数据量（d100 比 d000 多约 33% 训练数据）。Volume 控制实验（Appendix R）仅对 Falcon3-7B 执行，发现 volume 贡献了 MMLU 43%、ARC 45%、GSMK 53% 的总效应。这不是可忽略的分数。但其余五个模型缺少同样的 volume 控制，因此 Figure 1 中的 dose-response 曲线将 contamination content 与 data quantity 混在同一 x 轴上。
- **为什么影响接收**: 论文的核心叙事是 "profiling contamination dose-response"，但如果接近一半的效应来自单纯的数据量增加，dose-response 曲线的解释就不再 clean。尤其是 Collapse 模式（Qwen2.5, Falcon3）的解释：是 contamination 导致坍塌，还是过多 SFT 数据导致 catastrophic forgetting？
- **建议修改方向**: (a) 对至少 2–3 个代表性家族（特别是一个 Collapse 家族和一个 Benefit 家族）补做 volume 控制；(b) 或在 main text 中显著讨论 volume confound 的量级（目前仅在 Appendix R 提及），并将所有 dose-response 解释加上 "contamination content + volume" 的限定。

**W3 [Must-Fix] Prior sensitivity 表明 J=16 下 γ 估计不稳定，但 main text 仍报告具体 γ 值作为 findings。**
- **具体位置**: Appendix L, Figure 6, Table 12, §5.7
- **问题**: Appendix L 的 prior sensitivity 分析显示 posterior mean 在不同 prior 下从 0.34 变化到 0.89（2.6×）。对于一个号称 "calibrated" 的方法，估计值对 prior 的这种敏感度是不可接受的。这不同于 W1（W1 关注 identifiability 的理论下限，W3 关注实际估计的 instability），但两者都指向同一根因：J=16 太小。
- **为什么影响接收**: "Calibrated" 是论文标题中 "ContamCal" 的含义核心和 Abstract 中的核心 claim。当估计值对先验如此敏感时，"calibration" 的承诺未兑现。
- **建议修改方向**: (a) 在 main text 中报告 γ 估计时，始终报告三种 prior 下的范围而非单一默认值；(b) 明确讨论 "data-dominated" vs. "prior-dominated" regime 的分界，承认当前在后者。

**W4 [Should-Fix] n=3 seeds 下的 BCa bootstrap CI 不可靠，中间 dosage 的 dose-response 曲线形状不确定。**
- **具体位置**: Figure 5（BCa bootstrap 95% CI, n = seeds; Falcon3 n = 2）, §4.1, Limitations
- **问题**: BCa（bias-corrected and accelerated）bootstrap 需要估计 acceleration 和 bias 参数。n=3（Falcon3 为 n=2）时这些参数的估计极不稳定，CI 可能严重 miscalibrated。MDES 为 1.25–2.05pp 意味着中间 dosage（d025, d050）的效应低于检测阈值，无法与零可靠区分。这使得 dose-response 曲线在中间段的形状（线性 vs. 非线性 vs. 非单调）无法确定——但 Algorithm 1 的分类恰恰依赖这些中间点。
- **建议**: (a) 改用 percentile bootstrap 或直接报告 seed-level 结果而非 BCa；(b) 在讨论 dose-response 形状时注明中间 dosage 的统计功效不足；(c) 考虑增加 seeds 到 n≥5 以改善 CI 估计的稳定性。

**W5 [Should-Fix] S2 (Min-K%++) 在 model-level 层面有害，但仍被保留在 RRF pipeline 中，justification 不充分。**
- **具体位置**: Table 7 (Appendix D, page 13), §5.6, §3.2
- **问题**: Leave-one-out 消融（Table 7）显示移除 S2 使 MMLU 的 ρ_model 从 0.049 跃升至 0.471。论文自己承认 S2 "actively suppresses model-level dosage discrimination"。保留 S2 的理由是 item-level 信息（ρ = 0.773），但下游 IRT 模型需要可靠的 item-level exposure scores——如果 S2 在 model level 引入系统性偏差，这种偏差可能传播到 γ 估计中。论文未分析 S2 对 γ 估计本身的影响。
- **建议**: 补充一个消融实验：在移除 S2 后重新拟合 IRT 模型，比较 γ 估计值的变化。如果 γ 对 S2 的包含/排除敏感，则需要更充分的 justification。

**W6 [Should-Fix] SFT 注入作为 contamination proxy 的外部效度讨论不足。**
- **具体位置**: §4.1, Limitations (page 8)
- **问题**: SFT 在已学习的 representation 上操作，创建的 "捷径" 与 pretraining 阶段的数据泄露机制不同。Pretraining contamination 影响的是基础表征学习，而 SFT contamination 是在现有能力之上的微调。Limitations 中一句话带过，但 main text 的叙事框架（"dose-response profiling"）暗示了对 pretraining leakage 的 generalizability。Volume 控制实验（Appendix R）部分缓解但未解决此问题。
- **建议**: (a) 在 §4.1 中更明确地讨论 SFT vs. pretraining contamination 的机制差异；(b) 将 findings 的 scope 限定为 "SFT-stage contamination dose-response"；(c) 讨论哪些发现可能迁移到 pretraining leakage（如 cross-family heterogeneity 可能是 robust 的），哪些可能不迁移（如具体的 dose-response 曲线形状）。

**W7 [Should-Fix] DiD 分析的 parallel trends assumption 仅有单一 pre-treatment period，无法正式验证。**
- **具体位置**: §5.4, Table 14, Figure 10–11
- **问题**: DiD 分析用于测试 item-specific memorization。Parallel trends assumption 要求 treated 和 untreated items 在无 treatment 情况下会有相似的变化趋势。但实验仅有一个 pre-treatment period（d000），无法区分 level equivalence（d000 处 balanced）和 trend equivalence。
- **建议**: (a) 承认 parallel trends 是一个不可检验的假设（单一 pre-period）；(b) 考虑使用 placebo tests（如在 untreated items 中随机划分 pseudo-treatment/control 组）来评估 DiD 估计的基线噪声水平。

**W8 [Minor] "Global capability modulation" 的解释可能过度。**
- **具体位置**: §5.2, §6 (Discussion)
- MMLU 包含 Math 和 CS 等数学相关 domain，GSMK 的提升可能反映 domain-specific knowledge transfer 而非 truly global capability changes。论文在 Appendix R 中部分讨论了 family-specificity，但 Discussion 中的 "global capability modulation" 框架暗示了更广泛的机制。

**W9 [Minor] Out-of-sample validation 仅一个 held-out 家族。**
- LLaMA-3.1-8B 作为唯一的 held-out family（§5.1）是 thin evidence for generalizability。建议至少承认一个 family 不足以 robustly validate cross-family generalization。

**W10 [Minor] γ 参数化选择（outside vs. inside discrimination bracket）缺乏理论论证。**
- **具体位置**: Eq. 2 (§3.3), Appendix G (Table 10)
- 两种参数化 yield comparable model fit，但 outside-bracket 意味着 contamination effect 与 item discrimination 独立。论文应简要讨论这两种 formulation 在何种条件下会 diverge，以及 independence assumption 是否合理。

---

### Questions

**Q1.** Appendix R 的 volume 控制实验中，Falcon3-7B 的 volume 贡献为 43–53%。是否有初步数据或计算资源允许对至少一个 Collapse 家族（如 Qwen2.5）重复此控制？Collapse 模式是否可能主要由 SFT data volume 引起的 catastrophic forgetting 驱动，而非 contamination content？

**Q2.** 如果将 S2 (Min-K%++) 从 RRF pipeline 中移除并重新拟合 IRT 模型，γ 估计值会如何变化？考虑到 S2 在 model level 引入系统性偏差（Table 7），这种偏差是否传播到了 γ 的 posterior？

**Q3.** 论文报告 d000 配置下的 accuracy change 非常小（Table 1: Phi-4 为 −0.06pp, 95% CI 包含零），这些 clean control 的效应大小是否与 n=3 的 measurement noise floor 一致？即，是否有足够的证据区分 "真正的零效应" 和 "功效不足的不显著效应"？

**Q4.** 4PL 扩展（Appendix H）要求 J≥16 以避免 overparameterization，但 domain-level 分析使用的 J 是多少？如果 domain-level J 显著低于 16，4PL 估计是否可靠？

**Q5.** Cross-benchmark transfer 中 Gemma-2 被排除（"due to CoT collapse under MC-format SFT"）。能否简述 CoT collapse 的具体表现？这是否暗示 contamination 的影响机制在 instruction-following 和 CoT 层面有不同的 failure mode？

---

### Missing References

未发现明显遗漏的关键 related work。引用覆盖了 contamination detection（Shi et al., Zhang et al., Dekoninck et al.）、IRT for LLM（Rodriguez et al., Han et al., Polo et al.）、DIF 理论（Holland & Thayer, Swaminathan & Rogers）、以及 benchmark contamination mitigation（Sun et al., Oren et al.）。建议考虑：
- Deng et al. (2024) "Investigating Data Contamination in Modern Benchmarks for Large Language Models" (NAACL 2024)（如未 cite 的话），对 contamination 在不同 benchmark 上的差异化效应有 complementary 发现。

---

### 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 (Acceptable) | 框架设计和大部分实验方法论合理，但 identifiability gap（J=16 vs J≥50）和 volume confound 的不完全控制使 domain-level γ claims 缺乏充分支撑。Prior sensitivity 进一步确认 γ 估计在当前 J 下不稳定。Aggregate-level 结果（dose-response profiling, cross-family comparison）更可信。 |
| **Excitement** | 3.5/5 | 将 IRT 引入 contamination 量化是有创意的角度，dose-response profiling 和 family-level heterogeneity 发现有新意。但核心 γ 估计的 underpowering 限制了兴奋度。如果解决 J 的问题，潜力显著。 |
| **Reproducibility** | 4/5 | 代码和数据 available（§1 footnote），实验细节充分（Appendix J-K），超参数完整记录（Table 11）。n=3 seeds 的再现需注意 seed sensitivity。 |
| **Confidence** | 4/5 | 对 IRT 模型设计、统计方法和实验设计有扎实理解。可能遗漏了某些 NLP-specific 的 contamination detection 细节。 |

### Overall Assessment

**3.5 — Borderline Conference**

ContamCal 提出的框架——multi-signal exposure mapping + contamination-augmented IRT——是对 benchmark contamination 研究的实质性方法论贡献。实验设计的规模和透明度令人印象深刻。然而，论文最核心的 claim（"calibrated domain-level contamination diagnosis with credible intervals"）与实际实验条件之间存在 gap：J=16 远低于自身模拟验证的 J≥50 要求，γ 对 prior 敏感，volume confound 仅对 1/6 模型做了控制。如果作者能将 domain-level γ claims 适当降级为 exploratory、补充 volume 控制证据、并更谨慎地框定 "calibration" 的范围，本文的 aggregate-level 发现（dose-response pattern taxonomy, cross-family heterogeneity, cross-benchmark transfer）足以支撑 Conference 级别的贡献。当前版本在方法论 promise 和实际 statistical power 之间的 gap 使其处于 borderline。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1250 · 2026-05-25T21:23:32.664770+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 116

## Round 116

10 recorded events


### User

_source line 1251 · 2026-05-25T21:23:39.393733+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**要点总结**：

- **Overall: 3.5 (Borderline Conference)**
- 3 个 Must-Fix：(1) J=16 vs J≥50 identifiability gap 使 domain-level γ claims 缺乏支撑；(2) volume confound 仅控制了 1/6 模型但贡献了 43-53% 效应；(3) γ 估计对 prior 敏感（posterior mean 跨 prior 漂移 2.6×）
- 4 个 Should-Fix：n=3 BCa bootstrap 不可靠、S2 信号在 model-level 有害但被保留、SFT 外部效度讨论不足、DiD parallel trends 不可验证
- 3 个 Minor：global capability modulation 解释过度、out-of-sample validation 仅一个家族、γ 参数化选择缺理论论证
- 核心判断：框架本身有创新性，aggregate-level 发现可信，但 "calibrated domain-level diagnosis" 这一最强 claim 与 J=16 的统计功效不匹配

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-25T21:24:06.052953+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-25T21:24:06.154175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-25T21:24:17.418614+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool call

_source line 1255 · 2026-05-25T21:24:17.871632+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-25T21:24:17.872072+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-25T21:24:18.475803+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (433 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\n- sft_gemma2_s0_sweep_v2（准备中）\n- falcon3-7b-download（准备中）\n- falcon3-7b-dl-v2（准备中）\n- falcon3-7b-dl-v3（准备中）\n- falcon3-7b-dl-v4（准备中）\n- falcon3-7b-dl-v5（准备中）\n- …另有 34 项\n\n## 近期结论\n- **analysis_dif_comparison** (success): Non-uniform DIF (gamma outside discrimination bracket) provides comparable or better model fit than uniform DIF (gamma inside bracket) on MMLU, as measured by WAIC
…[truncated 2659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-25T21:24:18.476409+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 604
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-25T21:24:18.526969+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:44.763907+00:00\", \"completed_at\": \"2026-05-25T21:19:25.916698+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Figure 1 图例文字偏小（约 6-7pt），多条线在低剂量区域密集重叠，审稿人可能需要放大才能区分 Phi-4 和 LLaMA-3.1 的曲线。建议加大 marker 差异或增加 legend 字号\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Table 1 列数较多（~8 列），全宽排列，最右几列内容紧凑但未溢出。精度统一（小数点后 2-3 位），最优值有加粗标注，booktabs 风格正确\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 右栏放置得当，但 MAE 列的数值精度不完全统一（部分 3 位小数，部分 4 位），建议统一到 3 位\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Section 5 \\\"Results\\\" heading 出现在左栏底部约 1/4 处，后面跟了 Section 5.1 标题 + 约 3 行正文，勉强不算孤悬但位置偏低\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"页面密度很高（Table 4 + Figure 5 + 5 个 subsection），信息量大但不影响可读性，Figure 5 的 caption 中 \\\"Filled markers: C1 excludes zero\\\" 字号偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 6 的 per-domain 点图清晰，CI 可读；Limitations 段落简短（~1 段），符合 EMNLP 要求\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix 最密集页：3 tables + 1 figure + 文字，Figure 8 的多面板子图 axis label 字号偏小（约 6pt），但因是 appendix，影响可控\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 10 (DID boxplot) 和 Figure 11 (DiD by dosage) 清晰度良好，双面板图 axis label 可读\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Algorithm 1 伪代码排版规范，使用 algorithmic 环境，缩进清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 2 pipeline 架构图全宽排列，三阶段颜色区分明确（蓝/橙/绿），caption 自包含，是全文最佳 display item\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 10}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 654
}
```

</details>

---


### Assistant

_source line 1260 · 2026-05-25T21:24:43.424530+00:00_

Reviewer 1 初审完成，评分 3.5（Borderline Conference）。记录要点：

**Must-Fix (3)**:
1. J=16 vs J≥50 identifiability gap → domain-level γ claims 统计功效不足
2. Volume confound 仅控制 1/6 模型但贡献 43-53% 效应
3. γ 估计对 prior 敏感（posterior mean 跨 prior 漂移 2.6×）

**Should-Fix (4)**: n=3 BCa bootstrap、S2 信号有害但保留、SFT 外部效度、DiD parallel trends 不可验证

**Minor (3)**: global capability modulation 解释过度、out-of-sample 仅一个家族、γ 参数化选择缺理论论证

视觉审查已完成（10 条 info 级发现，无 critical/warning）。外部审稿未请求。

等待 Reviewer 2 完成初审后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 117

## Round 117

6 recorded events


### User

_source line 1261 · 2026-05-25T21:25:56.738291+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**审查侧重**: 新颖性、Related Work 完整性、写作质量、整体完成度

---

## Summary

本文提出 ContamCal，一个结合多信号暴露度映射和污染增强 IRT 的诊断框架，通过对 5 个模型家族的 6 个模型进行 5 个剂量级别的受控 SFT 注入，发现污染效应呈异质性光谱（Immune/Benefit/Collapse/V-Recovery），而非统一膨胀。论文还展示了域级别 γ 诊断能力和跨基准迁移效应。

---

## Strengths

**S1. 重要且及时的实证发现。** 系统性地证明污染效应在模型家族间是异质的（非统一膨胀），这对 benchmark 解释实践有直接价值。Figure 1 的剂量-响应曲线提供了清晰的视觉证据（Section 5.1）。

**S2. 严谨的实验设计。** 多种子复现（n=3）、跨基准验证（MMLU→GSM8K/ARC）、留出验证（LLaMA-3.1-8B）、以及 DID 记忆化测试（Section 5.4）构成了多层验证体系，增强了主要发现的可信度。

**S3. 详尽的消融分析。** Appendix 涵盖信号消融（D）、DIF 参数化比较（G）、4PL 扩展（H）、可辨识性模拟（F）、鲁棒性分析（Y）等 20+ 个附录，展现了充分的技术严谨性。

**S4. 合理的 hedging。** Collapse 和 V-Recovery 模式被明确标注为单家族观察、待独立复现（Abstract、Section 5.1），域级别分析被定位为"exploratory"（Section 5.7），这种审慎态度在实证研究中值得肯定。

**S5. 三阶段流水线设计清晰。** Figure 2 的 pipeline 图简洁地呈现了从信号融合到 IRT 建模到剂量-响应分类的完整流程，Section 3 的方法叙述逻辑连贯。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] Abstract 首句及 Introduction 对新颖性的过度宣称**
- 具体位置：Abstract 第 1 句、Section 1 第 1 段
- 问题：Abstract 声称 "its actual effect has never been measured across model families"。然而：(1) Schaeffer et al. (2026) 已在 Qwen 3 架构上（34M–344M）进行了受控预训练注入并拟合了剂量-响应曲线；(2) Bordt et al. (2025, ICML) 在模型参数量维度上扩展至 1.6B 并系统考察了污染遗忘规律。这些工作虽然在规模和阶段（pretraining vs SFT）上与本文不同，但 "never been measured" 的说法明显过强。
- 为什么影响接收：审稿人在评估新颖性时会立即对照这些工作，过度宣称会削弱论文的可信度，甚至引发 "是否充分了解 prior art" 的质疑。
- 建议修改方向：将 claim 精确限定为 "the dose-response profile of SFT-stage contamination has not been systematically characterized across diverse model families at the 7B–14B scale"，并在 Introduction 中明确与 Schaeffer et al. 和 Bordt et al. 的实验范围区分。

**N2 [critical] 与 Han et al. (2026) 的技术区分不足**
- 具体位置：Section 2 Related Work 最后一段、Section 3.3
- 问题：Han et al. (2026) 同样将 DIF 方法应用于 LLM 污染检测（observational DIF on IRT）。本文使用受控注入 + 连续暴露度协变量，这是一个重要的方法论差异，但论文仅在 Related Work 中用一句话带过（"apply observational differential item functioning..."），而在 Method Section 3.3 中完全没有讨论为什么连续 γ_i 参数化优于 Han et al. 的 group-level DIF，或观察性 DIF 方法的具体局限性是什么。
- 为什么影响接收：这是本文最直接的竞争者。如果审稿人认为本文只是 Han et al. 的受控实验版本而缺乏方法论进步，会显著降低新颖性评分。
- 建议修改方向：在 Section 3.3 中增加一段明确对比：(a) 观察性 DIF 无法量化剂量效应、无法区分模型家族间的异质响应；(b) 连续暴露度协变量 vs. 二元 DIF grouping 在统计效力和可解释性上的差异。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] 剂量-响应分类体系（4 类）基于过小样本，有过拟合风险**
- 具体位置：Section 3.4 Algorithm 1、Section 5.1、Table 1
- 问题：4 种剂量-响应模式（Immune, Collapse, V-Recovery, Benefit）是从仅 5 个模型家族的观察中归纳的。其中 Collapse 和 V-Recovery 各仅在 1 个家族（Qwen2.5）中观察到。虽然论文已标注 "preliminary"，但 Algorithm 1 的规则化分类和 Table 1 的呈现方式暗示这是一个完整的分类体系。
- 建议：明确讨论该分类是否穷尽（是否可能存在第 5 种模式），以及在更多模型家族上验证后分类边界可能如何调整。

**W2 [warning] "Benefit" 模式的因果解释不完整**
- 具体位置：Section 5.1、Section 5.2、Appendix R
- 问题：部分模型在污染后性能提升。DID 分析（Section 5.4）未检出 item-level 记忆化，volume-matched control（Appendix R）将 45% 归因于数据量。这意味着：(a) "Benefit" 的很大一部分来自额外训练数据而非污染本身；(b) 剩余 55% 可能是 capability elicitation 或格式适应。当 "Benefit" 并非来自记忆化而是来自通用能力提升时，将其归类为 "contamination dose-response" 在概念上是否准确？这个区分对论文的核心叙事 "Not All Models Are Inflated" 至关重要。
- 建议：在 Section 6 Discussion 中更深入地讨论 "contamination-driven" vs. "training-driven" benefit 的边界，以及这对 benchmark 解释的不同 implications。

**W3 [warning] 域级别诊断的证据支撑有限**
- 具体位置：Section 5.7、Figure 6、Abstract
- 问题：域级别 γ 分析作为 ContamCal 的关键贡献在 Abstract 中被突出（"enables within-family domain-level contamination diagnosis with credible intervals"），但仅 Qwen2.5 显示统计显著的域级别效应（Social Sciences 负向，STEM 正向）。其他 5 个模型家族未显示显著域异质性。Abstract 的措辞使读者期待一个普遍适用的诊断能力，但实际证据仅支持单个家族。
- 建议：将 Abstract 的 claim 限定为 "enables domain-level diagnosis when contamination effects are sufficiently large"，并在 Section 5.7 中量化该诊断能力的 power boundary。

**W4 [warning] 方法论新颖性的定位不够明确**
- 具体位置：Section 1 Contributions、Section 3 整体
- 问题：ContamCal 的各组件均基于现有方法：信号检测（Min-K%++, embedding similarity 等）是已有方法的组合；RRF 融合是标准的；2PL + 协变量是 De Boeck and Wilson (2004) 建立的解释性 IRT 框架；Algorithm 1 是基于阈值的简单规则。论文的贡献更多在于将这些组件整合为一个针对污染分析的应用框架，以及系统性的实证研究。但 Section 1 的 Contributions 列表没有明确区分 "方法论创新" 和 "应用创新"。
- 建议：在 Contributions 中明确定位为 "systematic empirical investigation + diagnostic application framework"，而非暗示方法论的根本性创新。

**W5 [warning] Main text 中未引用剂量-响应建模的核心文献**
- 具体位置：Section 1、Section 3.4
- 问题：论文的核心概念框架借自药理学/毒理学的剂量-响应模型。Hill (1910) 的 sigmoid dose-response equation 是该领域的奠基性工作，但仅在 Appendix AB 中被引用。Section 3.4 在 main text 中建立剂量-响应分类时没有引用任何该领域的经典文献。作为论文标题和核心贡献的概念来源，这一遗漏在 main text 中不应出现。
- 建议：在 Section 1 或 Section 3.4 中引用 Hill (1910) 及相关剂量-响应方法论文献。

### 小问题（不影响接收）

**M1** Section 3.1 的符号引入过于紧凑，从问题形式化到三阶段流水线的过渡缺少衔接。建议增加一句桥接说明为什么需要这种特定分解。

**M2** Figure 1（page 1）的小内嵌子图在正常打印尺寸下难以辨读。考虑放大或移至 appendix。

**M3** Abstract 字数（估计 ~196–210 词，取决于连字符计算方式）接近 EMNLP 2026 的 200 词限制。如果按 LaTeX texcount 标准的单字计算 hyphenated compounds 则可能合规，但建议作者自行验证并确认。

**M4** Section 6 (Discussion and Conclusion) 偏短（约 2/3 页），"Implications for practice" 段落可进一步展开具体的实践建议。

**M5** Page 1 脚注提到 "Code and data are available"，但未具体说明 data 包含什么内容（污染训练语料？IRT 参数估计？原始评估结果？）。

**M6** AI Assistance 披露（Appendix AD）提到 Claude 被用于 "summarizing related papers to inform related work section"。虽然这是合规的透明披露，但建议作者确保 Related Work 中的每篇引用都经过了深入阅读而非仅依赖 AI 摘要。

---

## Questions for Authors

**Q1.** Algorithm 1 的噪声阈值 τ=2pp 和严重度阈值 σ=5 是如何选择的？是否进行了敏感性分析？（Appendix U 的 sensitivity analysis 似乎仅涉及 prior，未涉及 Algorithm 1 的阈值。）

**Q2.** 为什么选择 LoRA 而非 full fine-tuning？LoRA 的低秩约束可能抑制记忆化效应（如 Collapse 的程度），使观察到的剂量-响应模式偏保守。作者是否认为 full fine-tuning 会产生不同的分类结果？

**Q3.** "Benefit" 模式中，性能提升的 55%（扣除 volume-matched control 的 45%）具体归因于什么？是格式适应（MC template familiarity）、能力引出（capability elicitation）、还是其他机制？

**Q4.** Gemma-2 因 "MC-format SFT destroying chain-of-thought reasoning" 被排除在多个分析之外（Section 4.1）。这是否意味着 CoT-dependent 模型系统性地表现为 Collapse，从而实际上有第五种模式（"Format-Sensitivity Collapse"）？

**Q5.** 跨基准迁移（MMLU→GSM8K, Section 5.2）是否可能由 SFT 训练引入的通用 instruction-following 能力提升解释，而非污染效应的跨域传播？

---

## Missing References

1. **Zhou et al. (2023)** "Don't Make Your LLM an Evaluation Benchmark Cheater" (arXiv:2311.01964) — 讨论 benchmark leakage 的风险和指南，与本文的 motivation 直接相关但未被引用。
2. **Hill (1910)** — 应在 main text（非仅 Appendix AB）中引用，作为剂量-响应建模的概念来源。
3. **Li et al. (2024) / Deng et al. (2024)** — contamination detection 领域的综述性工作（ACL Findings / arXiv survey），可补充 Related Work Section 2 的背景。
4. **Quantifying Data Contamination in Psychometric Evaluations of LLMs**（Han et al. 2026, arXiv:2510.07175）——虽已引用，但讨论深度不足（见 N2）。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法合理，实验设计严谨，但训练量混淆、LoRA 限制和小样本分类体系存在问题 |
| Excitement | 3/5 | 异质性污染效应的发现有实用价值，但方法论创新有限，主要是已有技术的应用组合 |
| Reproducibility | 4/5 | 匿名代码链接已提供，实验设置描述清晰，但需要显著计算资源 |
| Reviewer Confidence | 4/5 | 仔细阅读了全文和附录，对 IRT 和 contamination detection 领域有较好了解 |

## Overall Assessment

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 一项执行良好的系统性实证研究，证明了污染效应在模型家族间的异质性这一有价值的发现，但方法论新颖性有限（主要是已有技术的应用组合），核心宣称存在过度表述，且剂量-响应分类体系和域级别诊断能力的证据支撑偏弱。

**详细总评**: 论文的核心贡献——系统性地证明 "not all models are inflated"——对 benchmark 评估实践有直接价值。受控 SFT 注入 + 多种子复现 + 跨基准验证的实验设计比该领域大多数工作更严谨。然而，论文的新颖性更多在于实证发现和应用框架，而非方法论创新，且 Abstract/Introduction 的措辞暗示了超出实际贡献的新颖性。如果作者能 (1) 精确限定新颖性宣称的范围，(2) 充分区分与 Han et al. (2026) 的技术差异，(3) 更透明地讨论 "Benefit" 模式的因果解释，这篇论文有潜力达到 Conference 水平（4.0）。当前版本处于 Borderline Conference 与 Findings 之间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-25T21:27:49.974374+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Round 1 Step 2\n\n以下是 **Reviewer 2** 的完整初审意见。请逐条审阅，对每个 Must-Fix、Should-Fix 和 Minor 问题给出 `[AGREE]` 或 `[REBUT]`（附理由）。如果你有补充观察，也可标注 `[ADD]`。\n\n重点关注：Reviewer 2 侧重新颖性和写作，与你的方法/实验侧重互补。请特别注意你们是否在以下问题上存在分歧：\n- N1 的 \"overclaiming\" 判断是否合理\n- W4 关于方法论新颖性定位——你作为方法审查者如何看待\n- W2 \"Benefit\" 模式的因果解释——是否与你的 volume confound 发现一致\n\n---\n\n**Reviewer 2 完整审稿意见：**\n\n**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、整体完成度\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个结合多信号暴露度映射和污染增强 IRT 的诊断框架，通过对 5 个模型家族的 6 个模型进行 5 个剂量级别的受控 SFT 注入，发现污染效应呈异质性光谱（Immune/Benefit/Collapse/V-Recovery），而非统一膨胀。论文还展示了域级别 γ 诊断能力和跨基准迁移效应。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的实证发现。** 系统性地证明污染效应在模型家族间是异质的（非统一膨胀），这对 benchmark 解释实践有直接价值。Figure 1 的剂量-响应曲线提供了清晰的视觉证据（Section 5.1）。\n\n**S2. 严谨的实验设计。** 多种子复现（n=3）、跨基准验证（MMLU→GSM8K/ARC）、留出验证（LLaMA-3.1-8B）、以及 DID 记忆化测试（Section 5.4）构成了多层验证体系，增强了主要发现的可信度。\n\n**S3. 详尽的消融分析。** Appendix 涵盖信号消融（D）、DIF 参数化比较（G）、4PL 扩展（H）、可辨识性模拟（F）、鲁棒性分析（Y）等 20+ 个附录，展现了充分的技术严谨性。\n\n**S4. 合理的 hedging。** Collapse 和 V-Recovery 模式被明确标注为单家族观察、待独立复现（Abstract、Section 5.1），域级别分析被定位为\"exploratory\"（Section 5.7），这种审慎态度在实证研究中值得肯定。\n\n**S5. 三阶段流水线设计清晰。** Figure 2 的 pipeline 图简洁地呈现了从信号融合到 IRT 建模到剂量-响应分类的完整流程，Section 3 的方法叙述逻辑连贯。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Abstract 首句及 Introduction 对新颖性的过度宣称**\n- 具体位置：Abstract 第 1 句、Section 1 第 1 段\n- 问题：Abstract 声称 \"its actual effect has never been measured across model families\"。然而：(1) Schaeffer et al. (2026) 已在 Qwen 3 架构上（34M–344M）进行了受控预训练注入并拟合了剂量-响应曲线；(2) Bordt et al. (2025, ICML) 在模型参数量维度上扩展至 1.6B 并系统考察了污染遗忘规律。这些工作虽然在规模和阶段（pretraining vs SFT）上与本文不同，但 \"never been measured\" 的说法明显过强。\n- 为什么影响接收：审稿人在评估新颖性时会立即对照这些工作，过度宣称会削弱论文的可信度，甚至引发 \"是否充分了解 prior art\" 的质疑。\n- 建议修改方向：将 claim 精确限定为 \"the dose-response profile of SFT-stage contamination has not been systematically characterized across diverse model families at the 7B–14B scale\"，并在 Introduction 中明确与 Schaeffer et al. 和 Bordt et al. 的实验范围区分。\n\n**N2 [critical] 与 Han et al. (2026) 的技术区分不足**\n- 具体位置：Section 2 Related Work 最后一段、Section 3.3\n- 问题：Han et al. (2026) 同样将 DIF 方法应用于 LLM 污染检测（observational DIF on IRT）。本文使用受控注入 + 连续暴露度协变量，这是一个重要的方法论差异，但论文仅在 Related Work 中用一句话带过（\"apply observational differential item functioning...\"），而在 Method Section 3.3 中完全没有讨论为什么连续 γ_i 参数化优于 Han et al. 的 group-level DIF，或观察性 DIF 方法的具体局限性是什么。\n- 为什么影响接收：这是本文最直接的竞争者。如果审稿人认为本文只是 Han et al. 的受控实验版本而缺乏方法论进步，会显著降低新颖性评分。\n- 建议修改方向：在 Section 3.3 中增加一段明确对比：(a) 观察性 DIF 无法量化剂量效应、无法区分模型家族间的异质响应；(b) 连续暴露度协变量 vs. 二元 DIF grouping 在统计效力和可解释性上的差异。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] 剂量-响应分类体系（4 类）基于过小样本，有过拟合风险**\n- 具体位置：Section 3.4 Algorithm 1、Section 5.1、Table 1\n- 问题：4 种剂量-响应模式（Immune, Collapse, V-Recovery, Benefit）是从仅 5 个模型家族的观察中归纳的。其中 Collapse 和 V-Recovery 各仅在 1 个家族（Qwen2.5）中观察到。虽然论文已标注 \"preliminary\"，但 Algorithm 1 的规则化分类和 Table 1 的呈现方式暗示这是一个完整的分类体系。\n- 建议：明确讨论该分类是否穷尽（是否可能存在第 5 种模式），以及在更多模型家族上验证后分类边界可能如何调整。\n\n**W2 [warning] \"Benefit\" 模式的因果解释不完整**\n- 具体位置：Section 5.1、Section 5.2、Appendix R\n- 问题：部分模型在污染后性能提升。DID 分析（Section 5.4）未检出 item-level 记忆化，volume-matched control（Appendix R）将 45% 归因于数据量。这意味着：(a) \"Benefit\" 的很大一部分来自额外训练数据而非污染本身；(b) 剩余 55% 可能是 capability elicitation 或格式适应。当 \"Benefit\" 并非来自记忆化而是来自通用能力提升时，将其归类为 \"contamination dose-response\" 在概念上是否准确？这个区分对论文的核心叙事 \"Not All Models Are Inflated\" 至关重要。\n- 建议：在 Section 6 Discussion 中更深入地讨论 \"contamination-driven\" vs. \"training-driven\" benefit 的边界，以及这对 benchmark 解释的不同 implications。\n\n**W3 [warning] 域级别诊断的证据支撑有限**\n- 具体位置：Section 5.7、Figure 6、Abstract\n- 问题：域级别 γ 分析作为 ContamCal 的关键贡献在 Abstract 中被突出（\"enables within-family domain-level contamination diagnosis with credible intervals\"），但仅 Qwen2.5 显示统计显著的域级别效应（Social Sciences 负向，STEM 正向）。其他 5 个模型家族未显示显著域异质性。Abstract 的措辞使读者期待一个普遍适用的诊断能力，但实际证据仅支持单个家族。\n- 建议：将 Abstract 的 claim 限定为 \"enables domain-level diagnosis when contamination effects are sufficiently large\"，并在 Section 5.7 中量化该诊断能力的 power boundary。\n\n**W4 [warning] 方法论新颖性的定位不够明确**\n- 具体位置：Section 1 Contributions、Section 3 整体\n- 问题：ContamCal 的各组件均基于现有方法：信号检测（Min-K%++, embedding similarity 等）是已有方法的组合；RRF 融合是标准的；2PL + 协变量是 De Boeck and Wilson (2004) 建立的解释性 IRT 框架；Algorithm 1 是基于阈值的简单规则。论文的贡献更多在于将这些组件整合为一个针对污染分析的应用框架，以及系统性的实证研究。但 Section 1 的 Contributions 列表没有明确区分 \"方法论创新\" 和 \"应用创新\"。\n- 建议：在 Contributions 中明确定位为 \"systematic empirical investigation + diagnostic application framework\"，而非暗示方法论的根本性创新。\n\n**W5 [warning] Main text 中未引用剂量-响应建模的核心文献**\n- 具体位置：Section 1、Section 3.4\n- 问题：论文的核心概念框架借自药理学/毒理学的剂量-响应模型。Hill (1910) 的 sigmoid dose-response equation 是该领域的奠基性工作，但仅在 Appendix AB 中被引用。Section 3.4 在 main text 中建立剂量-响应分类时没有引用任何该领域的经典文献。作为论文标题和核心贡献的概念来源，这一遗漏在 main text 中不应出现。\n- 建议：在 Section 1 或 Section 3.4 中引用 Hill (1910) 及相关剂量-响应方法论文献。\n\n### 小问题（不影响接收）\n\n**M1** Section 3.1 的符号引入过于紧凑，从问题形式化到三阶段流水线的过渡缺少衔接。建议增加一句桥接说明为什么需要这种特定分解。\n\n**M2** Figure 1（page 1）的小内嵌子图在正常打印尺寸下难以辨读。考虑放大或移至 appendix。\n\n**M3** Abstract 字数（估计 ~196–210 词，取决于连字符计算方式）接近 EMNLP 2026 的 200 词限制。如果按 LaTeX texcount 标准的单字计算 hyphenated compounds 则可能合规，但建议作者自行验证并确认。\n\n**M4** Section 6 (Discussion and Conclusion) 偏短（约 2/3 页），\"Implications for practice\" 段落可进一步展开具体的实践建议。\n\n**M5** Page 1 脚注提到 \"Code and data are available\"，但未具体说明 data 包含什么内容（污染训练语料？IRT 参数估计？原始评估结果？）。\n\n**M6** AI Assistance 披露（Appendix AD）提到 Claude 被用于 \"summarizing related papers to inform related work section\"。虽然这是合规的透明披露，但建议作者确保 Related Work 中的每篇引用都经过了深入阅读而非仅依赖 AI 摘要。\n\n---\n\n## Questions for Authors\n\n**Q1.** Algorithm 1 的噪声阈值 τ=2pp 和严重度阈值 σ=5 是如何选择的？是否进行了敏感性分析？\n\n**Q2.** 为什么选择 LoRA 而非 full fine-tuning？LoRA 的低秩约束可能抑制记忆化效应（如 Collapse 的程度），使观察到的剂量-响应模式偏保守。作者是否认为 full fine-tuning 会产生不同的分类结果？\n\n**Q3.** \"Benefit\" 模式中，性能提升的 55%（扣除 volume-matched control 的 45%）具体归因于什么？\n\n**Q4.** Gemma-2 因 \"MC-format SFT destroying chain-of-thought reasoning\" 被排除在多个分析之外（Section 4.1）。这是否意味着 CoT-dependent 模型系统性地表现为 Collapse？\n\n**Q5.** 跨基准迁移（MMLU→GSM8K, Section 5.2）是否可能由 SFT 训练引入的通用 instruction-following 能力提升解释，而非污染效应的跨域传播？\n\n---\n\n## Missing References\n\n1. **Zhou et al. (2023)** \"Don't Make Your LLM an Evaluation Benchmark Cheater\" (arXiv:2311.01964)\n2. **Hill (1910)** — 应在 main text 中引用\n3. **Li et al. (2024) / Deng et al. (2024)** — contamination detection 综述\n4. **Han et al. (2026, arXiv:2510.07175)** — 已引用但讨论深度不足\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Round 1 Step 2\n\n以下是 **Reviewer 2** 的完整初审意见。请逐条审阅，对每个 Must-Fix、Should-Fix 和 Minor 问题给出 `[AGREE]` 或 `[REBUT]`（附理由）。如果你有补充观察，也可标注 `[ADD]`。\n\n重点关注：Reviewer 2 侧重新颖性和写作，与你的方法/实验侧重互补。请特别注意你们是否在以下问题上存在分歧：\n- N1 的 \"overclaiming\" 判断是否合理\n- W4 关于方法论新颖性定位——你作为方法审查者如何看待\n- W2 \"Benefit\" 模式的因果解释——是否与你的 volume confound 发现一致\n\n---\n\n**Reviewer 2 完整审稿意见：**\n\n**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、整体完成度\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个结合多信号暴露度映射和污染增强 IRT 的诊断框架，通过对 5 个模型家族的 6 个模型进行 5 个剂量级别的受控 SFT 注入，发现污染效应呈异质性光谱（Immune/Benefit/Collapse/V-Recovery），而非统一膨胀。论文还展示了域级别 γ 诊断能力和跨基准迁移效应。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的实证发现。** 系统性地证明污染效应在模型家族间是异质的（非统一膨胀），这对 benchmark 解释实践有直接价值。Figure 1 的剂量-响应曲线提供了清晰的视觉证据（Section 5.1）。\n\n**S2. 严谨的实验设计。** 多种子复现（n=3）、跨基准验证（MMLU→GSM8K/ARC）、留出验证（LLaMA-3.1-8B）、以及 DID 记忆化测试（Section 5.4）构成了多层验证体系，增强了主要发现的可信度。\n\n**S3. 详尽的消融分析。** Appendix 涵盖信号消融（D）、DIF 参数化比较（G）、4PL 扩展（H）、可辨识性模拟（F）、鲁棒性分析（Y）等 20+ 个附录，展现了充分的技术严谨性。\n\n**S4. 合理的 hedging。** Collapse 和 V-Recovery 模式被明确标注为单家族观察、待独立复现（Abstract、Section 5.1），域级别分析被定位为\"exploratory\"（Section 5.7），这种审慎态度在实证研究中值得肯定。\n\n**S5. 三阶段流水线设计清晰。** Figure 2 的 pipeline 图简洁地呈现了从信号融合到 IRT 建模到剂量-响应分类的完整流程，Section 3 的方法叙述逻辑连贯。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Abstract 首句及 Introduction 对新颖性的过度宣称**\n- 具体位置：Abstract 第 1 句、Section 1 第 1 段\n- 问题：Abstract 声称 \"its actual effect has never been measured across model families\"。然而：(1) Schaeffer et al. (2026) 已在 Qwen 3 架构上（34M–344M）进行了受控预训练注入并拟合了剂量-响应曲线；(2) Bordt et al. (2025, ICML) 在模型参数量维度上扩展至 1.6B 并系统考察了污染遗忘规律。这些工作虽然在规模和阶段（pretraining vs SFT）上与本文不同，但 \"never been measured\" 的说法明显过强。\n- 为什么影响接收：审稿人在评估新颖性时会立即对照这些工作，过度宣称会削弱论文的可信度，甚至引发 \"是否充分了解 prior art\" 的质疑。\n- 建议修改方向：将 claim 精确限定为 \"the dose-response profile of SFT-stage contamination has not been systematically characterized across diverse model families at the 7B–14B scale\"，并在 Introduction 中明确与 Schaeffer et al. 和 Bordt et al. 的实验范围区分。\n\n**N2 [critical] 与 Han et al. (2026) 的技术区分不足**\n- 具体位置：Section 2 Related Work 最后一段、Section 3.3\n- 问题：Han et al. (2026) 同样将 DIF 方法应用于 LLM 污染检测（observational DIF on IRT）。本文使用受控注入 + 连续暴露度协变量，这是一个重要的方法论差异，但论文仅在 Related Work 中用一句话带过（\"apply observational differential item functioning...\"），而在 Method Section 3.3 中完全没有讨论为什么连续 γ_i 参数化优于 Han et al. 的 group-level DIF，或观察性 DIF 方法的具体局限性是什么。\n- 为什么影响接收：这是本文最直接的竞争者。如果审稿人认为本文只是 Han et al. 的受控实验版本而缺乏方法论进步，会显著降低新颖性评分。\n- 建议修改方向：在 Section 3.3 中增加一段明确对比：(a) 观察性 DIF 无法量化剂量效应、无法区分模型家族间的异质响应；(b) 连续暴露度协变量 vs. 二元 DIF grouping 在统计效力和可解释性上的差异。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] 剂量-响应分类体系（4 类）基于过小样本，有过拟合风险**\n- 具体位置：Section 3.4 Algorithm 1、Section 5.1、Table 1\n- 问题：4 种剂量-响应模式（Immune, Collapse, V-Recovery, Benefit）是从仅 5 个模型家族的观察中归纳的。其中 Collapse 和 V-Recovery 各仅在 1 个家族（Qwen2.5）中观察到。虽然论文已标注 \"preliminary\"，但 Algorithm 1 的规则化分类和 Table 1 的呈现方式暗示这是一个完整的分类体系。\n- 建议：明确讨论该分类是否穷尽（是否可能存在第 5 种模式），以及在更多模型家族上验证后分类边界可能如何调整。\n\n**W2 [warning] \"Benefit\" 模式的因果解释不完整**\n- 具体位置：Section 5.1、Section 5.2、Appendix R\n- 问题：部分模型在污染后性能提升。DID 分析（Section 5.4）未检出 item-level 记忆化，volume-matched control（Appendix R）将 45% 归因于数据量。这意味着：(a) \"Benefit\" 的很大一部分来自额外训练数据而非污染本身；(b) 剩余 55% 可能是 capability elicitation 或格式适应。当 \"Benefit\" 并非来自记忆化而是来自通用能力提升时，将其归类为 \"contamination dose-response\" 在概念上是否准确？这个区分对论文的核心叙事 \"Not All Models Are Inflated\" 至关重要。\n- 建议：在 Section 6 Discussion 中更深入地讨论 \"contamination-driven\" vs. \"training-driven\" benefit 的边界，以及这对 benchmark 解释的不同 implications。\n\n**W3 [warning] 域级别诊断的证据支撑有限**\n- 具体位置：Section 5.7、Figure 6、Abstract\n- 问题：域级别 γ 分析作为 ContamCal 的关键贡献在 Abstract 中被突出（\"enables within-family domain-level contamination diagnosis with credible intervals\"），但仅 Qwen2.5 显示统计显著的域级别效应（Social Sciences 负向，STEM 正向）。其他 5 个模型家族未显示显著域异质性。Abstract 的措辞使读者期待一个普遍适用的诊断能力，但实际证据仅支持单个家族。\n- 建议：将 Abstract 的 claim 限定为 \"enables domain-level diagnosis when contamination effects are sufficiently large\"，并在 Section 5.7 中量化该诊断能力的 power boundary。\n\n**W4 [warning] 方法论新颖性的定位不够明确**\n- 具体位置：Section 1 Contributions、Section 3 整体\n- 问题：ContamCal 的各组件均基于现有方法：信号检测（Min-K%++, embedding similarity 等）是已有方法的组合；RRF 融合是标准的；2PL + 协变量是 De Boeck and Wilson (2004) 建立的解释性 IRT 框架；Algorithm 1 是基于阈值的简单规则。论文的贡献更多在于将这些组件整合为一个针对污染分析的应用框架，以及系统性的实证研究。但 Section 1 的 Contributions 列表没有明确区分 \"方法论创新\" 和 \"应用创新\"。\n- 建议：在 Contributions 中明确定位为 \"systematic empirical investigation + diagnostic application framework\"，而非暗示方法论的根本性创新。\n\n**W5 [warning] Main text 中未引用剂量-响应建模的核心文献**\n- 具体位置：Section 1、Section 3.4\n- 问题：论文的核心概念框架借自药理学/毒理学的剂量-响应模型。Hill (1910) 的 sigmoid dose-response equation 是该领域的奠基性工作，但仅在 Appendix AB 中被引用。Section 3.4 在 main text 中建立剂量-响应分类时没有引用任何该领域的经典文献。作为论文标题和核心贡献的概念来源，这一遗漏在 main text 中不应出现。\n- 建议：在 Section 1 或 Section 3.4 中引用 Hill (1910) 及相关剂量-响应方法论文献。\n\n### 小问题（不影响接收）\n\n**M1** Section 3.1 的符号引入过于紧凑，从问题形式化到三阶段流水线的过渡缺少衔接。建议增加一句桥接说明为什么需要这种特定分解。\n\n**M2** Figure 1（page 1）的小内嵌子图在正常打印尺寸下难以辨读。考虑放大或移至 appendix。\n\n**M3** Abstract 字数（估计 ~196–210 词，取决于连字符计算方式）接近 EMNLP 2026 的 200 词限制。如果按 LaTeX texcount 标准的单字计算 hyphenated compounds 则可能合规，但建议作者自行验证并确认。\n\n**M4** Section 6 (Discussion and Conclusion) 偏短（约 2/3 页），\"Implications for practice\" 段落可进一步展开具体的实践建议。\n\n**M5** Page 1 脚注提到 \"Code and data are available\"，但未具体说明 data 包含什么内容（污染训练语料？IRT 参数估计？原始评估结果？）。\n\n**M6** AI Assistance 披露（Appendix AD）提到 Claude 被用于 \"summarizing related papers to inform related work section\"。虽然这是合规的透明披露，但建议作者确保 Related Work 中的每篇引用都经过了深入阅读而非仅依赖 AI 摘要。\n\n---\n\n## Questions for Authors\n\n**Q1.** Algorithm 1 的噪声阈值 τ=2pp 和严重度阈值 σ=5 是如何选择的？是否进行了敏感性分析？\n\n**Q2.** 为什么选择 LoRA 而非 full fine-tuning？LoRA 的低秩约束可能抑制记忆化效应（如 Collapse 的程度），使观察到的剂量-响应模式偏保守。作者是否认为 full fine-tuning 会产生不同的分类结果？\n\n**Q3.** \"Benefit\" 模式中，性能提升的 55%（扣除 volume-matched control 的 45%）具体归因于什么？\n\n**Q4.** Gemma-2 因 \"MC-format SFT destroying chain-of-thought reasoning\" 被排除在多个分析之外（Section 4.1）。这是否意味着 CoT-dependent 模型系统性地表现为 Collapse？\n\n**Q5.** 跨基准迁移（MMLU→GSM8K, Section 5.2）是否可能由 SFT 训练引入的通用 instruction-following 能力提升解释，而非污染效应的跨域传播？\n\n---\n\n## Missing References\n\n1. **Zhou et al. (2023)** \"Don't Make Your LLM an Evaluation Benchmark Cheater\" (arXiv:2311.01964)\n2. **Hill (1910)** — 应在 main text 中引用\n3. **Li et al. (2024) / Deng et al. (2024)** — contamination detection 综述\n4. **Han et al. (2026, arXiv:2510.07175)** — 已引用但讨论深度不足\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-25T21:28:24.835140+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34860
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-25T21:28:25.237619+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Round 1 Step 2\n\n以下是 **Reviewer 1** 的完整初审意见。请逐条审阅，对每个 Must-Fix、Should-Fix 和 Minor 问题给出 `[AGREE]` 或 `[REBUT]`（附理由）。如果你有补充观察，也可标注 `[ADD]`。\n\n重点关注：Reviewer 1 侧重方法和实验严谨性，与你的新颖性/写作侧重互补。请特别注意你们是否在以下问题上存在分歧：\n- Reviewer 1 的 Must-Fix 1（J=16 identifiability）与你的 W3（域级别证据有限）是否指向同一根本问题\n- Reviewer 1 的 Must-Fix 2（volume confound）与你的 W2（\"Benefit\" 因果解释）的关联\n- Reviewer 1 对 γ prior sensitivity 的关注——你是否同意这是 Must-Fix 级别\n\n---\n\n**Reviewer 1 完整审稿意见：**\n\n**Overall: 3.5 (Borderline Conference)**\n\n**3 个 Must-Fix：**\n\n**(1) J=16 vs J≥50 identifiability gap 使 domain-level γ claims 缺乏支撑**\n- 论文在 domain-level γ 分析中使用的 item 数量仅 J=16（MMLU 每个 domain 的 item 数），远低于 IRT 文献中的 identifiability 要求（通常 J≥50）。Appendix F 的模拟在 J=100/200/500 上进行，但没有在 J=16 这一实际使用的规模上验证 γ 的可辨识性。这意味着 domain-level γ 的置信区间可能过宽以至于无法支撑任何有意义的推断，而论文却将域级别诊断作为关键贡献之一。\n\n**(2) Volume confound 仅控制了 1/6 模型但贡献了 43-53% 效应**\n- Appendix R 的 volume-matched control 仅在 Phi-4 上执行（1/6 模型），却发现训练数据量贡献了 43-53% 的观察效应。这意味着：(a) 所有 \"Benefit\" 类模型的效应大小都可能被高估近一半；(b) 不同模型家族对训练量的敏感度可能不同，单一模型的控制实验无法代表全部。这是一个系统性混淆因素。\n\n**(3) γ 估计对 prior 敏感（posterior mean 跨 prior 漂移 2.6×）**\n- Appendix U 的 prior sensitivity 分析显示，γ 的 posterior mean 在不同 prior 设定下漂移高达 2.6 倍。对于一个被用作诊断统计量的参数，这种程度的 prior 依赖性表明数据本身的信息量不足以稳定估计。论文选择 N(0,1) 作为默认 prior，但没有给出充分的理论或实证理由说明为什么这是最合适的选择。\n\n**4 个 Should-Fix：**\n\n**(1) n=3 BCa bootstrap 不可靠**\n- 种子级复现使用 n=3 个 random seeds，在此基础上计算 BCa bootstrap 置信区间。BCa 方法在小样本（n<10）下的覆盖率属性不可靠，可能产生过窄或不稳定的置信区间。建议改用 percentile bootstrap 或明确报告 n=3 的统计功效限制。\n\n**(2) S2 信号在 model-level 有害但被保留**\n- 信号消融分析（Appendix D）显示 S2（Min-K++）在 model-level 分析中是有害信号（剔除后效果更好），但在 item-level 可能有用。论文最终保留了 S2 用于所有分析层级。如果 S2 在 aggregate-level 引入噪声，为什么不在不同分析层级使用不同的信号组合？\n\n**(3) SFT 外部效度讨论不足**\n- 论文通过 SFT 注入模拟污染，但真实污染通常发生在 pretraining 阶段。SFT vs. pretraining 阶段的污染可能产生不同的记忆化和遗忘动态。论文对这一外部效度限制的讨论不够充分。\n\n**(4) DiD parallel trends 不可验证**\n- DID 分析假设 parallel trends（污染 items 和非污染 items 在无污染情况下的性能变化趋势平行），但只有两个时间点（pre/post SFT），无法验证这一假设。\n\n**3 个 Minor：**\n\n**(1)** global capability modulation 解释过度——将跨基准迁移效应统一归因于 \"global capability modulation\" 可能过于简化\n\n**(2)** out-of-sample validation 仅在一个家族（LLaMA-3.1-8B）上进行，代表性有限\n\n**(3)** γ 参数化选择（连续 vs. 离散）缺乏理论论证\n\n**核心判断**：框架本身有创新性，aggregate-level 发现可信，但 \"calibrated domain-level diagnosis\" 这一最强 claim 与 J=16 的统计功效不匹配。",
  "reviewer_id": "2",
  "project": "contamcal-irt-calibration",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Round 1 Step 2\n\n以下是 **Reviewer 1** 的完整初审意见。请逐条审阅，对每个 Must-Fix、Should-Fix 和 Minor 问题给出 `[AGREE]` 或 `[REBUT]`（附理由）。如果你有补充观察，也可标注 `[ADD]`。\n\n重点关注：Reviewer 1 侧重方法和实验严谨性，与你的新颖性/写作侧重互补。请特别注意你们是否在以下问题上存在分歧：\n- Reviewer 1 的 Must-Fix 1（J=16 identifiability）与你的 W3（域级别证据有限）是否指向同一根本问题\n- Reviewer 1 的 Must-Fix 2（volume confound）与你的 W2（\"Benefit\" 因果解释）的关联\n- Reviewer 1 对 γ prior sensitivity 的关注——你是否同意这是 Must-Fix 级别\n\n---\n\n**Reviewer 1 完整审稿意见：**\n\n**Overall: 3.5 (Borderline Conference)**\n\n**3 个 Must-Fix：**\n\n**(1) J=16 vs J≥50 identifiability gap 使 domain-level γ claims 缺乏支撑**\n- 论文在 domain-level γ 分析中使用的 item 数量仅 J=16（MMLU 每个 domain 的 item 数），远低于 IRT 文献中的 identifiability 要求（通常 J≥50）。Appendix F 的模拟在 J=100/200/500 上进行，但没有在 J=16 这一实际使用的规模上验证 γ 的可辨识性。这意味着 domain-level γ 的置信区间可能过宽以至于无法支撑任何有意义的推断，而论文却将域级别诊断作为关键贡献之一。\n\n**(2) Volume confound 仅控制了 1/6 模型但贡献了 43-53% 效应**\n- Appendix R 的 volume-matched control 仅在 Phi-4 上执行（1/6 模型），却发现训练数据量贡献了 43-53% 的观察效应。这意味着：(a) 所有 \"Benefit\" 类模型的效应大小都可能被高估近一半；(b) 不同模型家族对训练量的敏感度可能不同，单一模型的控制实验无法代表全部。这是一个系统性混淆因素。\n\n**(3) γ 估计对 prior 敏感（posterior mean 跨 prior 漂移 2.6×）**\n- Appendix U 的 prior sensitivity 分析显示，γ 的 posterior mean 在不同 prior 设定下漂移高达 2.6 倍。对于一个被用作诊断统计量的参数，这种程度的 prior 依赖性表明数据本身的信息量不足以稳定估计。论文选择 N(0,1) 作为默认 prior，但没有给出充分的理论或实证理由说明为什么这是最合适的选择。\n\n**4 个 Should-Fix：**\n\n**(1) n=3 BCa bootstrap 不可靠**\n- 种子级复现使用 n=3 个 random seeds，在此基础上计算 BCa bootstrap 置信区间。BCa 方法在小样本（n<10）下的覆盖率属性不可靠，可能产生过窄或不稳定的置信区间。建议改用 percentile bootstrap 或明确报告 n=3 的统计功效限制。\n\n**(2) S2 信号在 model-level 有害但被保留**\n- 信号消融分析（Appendix D）显示 S2（Min-K++）在 model-level 分析中是有害信号（剔除后效果更好），但在 item-level 可能有用。论文最终保留了 S2 用于所有分析层级。如果 S2 在 aggregate-level 引入噪声，为什么不在不同分析层级使用不同的信号组合？\n\n**(3) SFT 外部效度讨论不足**\n- 论文通过 SFT 注入模拟污染，但真实污染通常发生在 pretraining 阶段。SFT vs. pretraining 阶段的污染可能产生不同的记忆化和遗忘动态。论文对这一外部效度限制的讨论不够充分。\n\n**(4) DiD parallel trends 不可验证**\n- DID 分析假设 parallel trends（污染 items 和非污染 items 在无污染情况下的性能变化趋势平行），但只有两个时间点（pre/post SFT），无法验证这一假设。\n\n**3 个 Minor：**\n\n**(1)** global capability modulation 解释过度——将跨基准迁移效应统一归因于 \"global capability modulation\" 可能过于简化\n\n**(2)** out-of-sample validation 仅在一个家族（LLaMA-3.1-8B）上进行，代表性有限\n\n**(3)** γ 参数化选择（连续 vs. 离散）缺乏理论论证\n\n**核心判断**：框架本身有创新性，aggregate-level 发现可信，但 \"calibrated domain-level diagnosis\" 这一最强 claim 与 J=16 的统计功效不匹配。",
    "reviewer_id": "2",
    "project": "contamcal-irt-calibration",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-25T21:28:26.499931+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1262
}
```

</details>

---


### Assistant

_source line 1266 · 2026-05-25T21:28:32.462114+00:00_

交叉分享已派发。两位 Reviewer 正在审阅对方的完整审稿意见并准备逐条回应。等待回收结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1267 · 2026-05-25T21:28:34.935946+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。核心判断：

**Overall: 3.5 (Borderline Conference)**

主要发现：
- **2 个 Must-Fix**：Abstract 首句 overclaiming（"never been measured" 忽略了 Schaeffer et al. 2026 和 Bordt et al. 2025），以及与 Han et al. (2026) observational DIF 方法的技术区分不足
- **5 个 Should-Fix**：分类体系过拟合风险（4类/5家族）、"Benefit"模式因果解释不完整、域级别诊断证据仅支持单个家族、方法论新颖性定位模糊、main text 未引用 Hill (1910) 等剂量-响应核心文献
- **6 个 Minor**：符号密度、Figure 1 可读性、abstract 字数边界、Discussion 偏短等

论文的实证贡献（异质性污染效应）有实用价值，实验设计严谨，但方法论创新主要是已有技术的应用组合，若修正 overclaiming 并加强与直接竞争者的区分，有潜力提升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1268 · 2026-05-25T21:28:42.811724+00:00_

交叉分享已派发给两位 Reviewer，等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 119

## Round 119

2 recorded events


### User

_source line 1269 · 2026-05-25T21:30:07.924763+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见

---

### Must-Fix 问题

**[AGREE] R2-N1: Abstract 首句 overclaiming**

同意方向，但认为 severity 可从 critical 降为 warning。Reviewer 2 引用的 Schaeffer et al. (2025) 确实进行了受控预训练注入实验，但其实验范围是**单一架构（Qwen 3）在 34M–344M 规模**。本文的区分点——**跨 5 个独立家族在 7B–14B 生产规模**——是实质性的。"Never been measured across model families" 如果严格按 "across independent architecture families" 解读，claim 可以成立。但我同意当前措辞过于绝对，应加限定。建议的修改方向（限定为 SFT-stage + 7B–14B scale + diverse families）合理。

补充一点：Bordt et al. (2025) 的实验扩展至 1.6B，仍远低于本文的 7B–14B 规模。规模差异在 contamination 研究中不是 trivial 的——小模型和大模型的 contamination 响应机制可能根本不同（本文的 Collapse/V-Recovery 模式就是证据）。因此 overclaiming 的程度比 R2 评估的要温和。

**[AGREE] R2-N2: 与 Han et al. (2026) 的技术区分不足**

完全同意需要更深入的对比。作为方法审查者，我认为两者之间的差异是**方法论层面的实质差异**，而非仅仅是受控 vs. 观察性实验设计的区别：

1. Han et al. 使用 group-level binary DIF（contaminated vs. clean group），本文使用 continuous exposure covariate（per-item c_{ij} ∈ [0,1]）——后者在统计效力和效应量化精度上有明确优势
2. Han et al. 无法量化 dose-response 关系（只有 contaminated/clean 二分），本文的框架天然支持剂量梯度分析
3. Han et al. 的 observational DIF 受 confound 影响（无法区分 contamination 和 capability），本文通过受控注入建立了 causal footing

这些区分**应该**在 Section 3.3 中用 1–2 段明确讨论。但我倾向于将 severity 定为 should-fix 而非 must-fix——因为方法论差异是真实存在的，缺的只是清晰的 articulation，不是缺乏新颖性本身。

---

### Should-Fix 问题

**[AGREE] R2-W1: 剂量-响应分类体系基于过小样本的过拟合风险**

同意。4 类模式来自 5 个家族，其中 Collapse 和 V-Recovery 各仅 1 个观察。Algorithm 1 的规则化分类（τ=2pp, σ=5）赋予了分类体系一种"完备性"的外观，但实际上缺乏充分的样本支撑。这与我的 W4 concern（n=3 seeds 下中间 dosage 曲线形状不确定）互补——分类不仅依赖家族数量，还依赖中间剂量点的可靠估计。

补充 [ADD]：Algorithm 1 的阈值 τ=2pp 和 σ=5 的选择似乎缺乏 sensitivity analysis（R2 的 Q1 也提到了这一点）。如果这些阈值稍有调整，部分家族的分类可能改变。建议在 Appendix U（已有 profile stability 分析）中加入 τ 和 σ 的 sensitivity sweep。

**[AGREE] R2-W2: "Benefit" 模式的因果解释不完整——与我的 volume confound 发现高度一致**

这是本次交叉审稿中最重要的共识点。R2 的 concern 与我的 W2（volume confound）从不同角度指向同一问题：

- 我的 W2（方法角度）：volume 控制仅对 Falcon3-7B 执行，显示 43–53% 效应来自数据量。其余 5 个模型缺少同样的控制。
- R2 的 W2（概念角度）：当 "Benefit" 的很大一部分来自额外训练数据 + capability elicitation 而非 memorization，将其归类为 "contamination dose-response" 在概念上可能有误。

两个 concern 合并后，论文面临的核心挑战更清晰：**dose-response 曲线的 x 轴不是纯粹的 contamination content axis，而是 contamination + volume + capability elicitation 的混合轴。** 论文的标题 "Not All Models Are Inflated" 暗示的是 contamination 导致的差异化响应，但如果 Benefit 模式主要由 training volume 和 capability elicitation 驱动，那么核心叙事需要重新框定。

R2 提出的概念问题比我的 volume confound 更尖锐，因为它质疑的是整个分类体系的 conceptual validity，而不仅仅是某个 confound 的控制。我将我的评估提升：**两位 reviewer 的 volume/causality concern 合在一起构成一个 must-fix 级别的问题**。

**[AGREE] R2-W3: 域级别诊断证据有限**

完全同意，与我的 W1（identifiability gap, J=16 vs J≥50）和 W3（prior sensitivity）互补。R2 从经验证据角度指出仅 Qwen2.5 显示显著域异质性；我从统计理论角度指出 J=16 不足以可靠估计域级 γ。两个视角共同表明：Abstract 中 "enables within-family domain-level contamination diagnosis" 的 claim 在当前证据下不成立。

**[REBUT] R2-W4: 方法论新颖性定位——部分不同意**

作为方法审查者，我认为 R2 对方法论新颖性的评估偏低。R2 的论点是各组件均为现有方法（Min-K%++、RRF、explanatory IRT、threshold-based classification），因此贡献更多是应用框架而非方法论创新。我有不同看法：

1. **组件组合本身具有方法论价值。** 将 training-free contamination detection signals 通过 RRF 融合为 per-item continuous exposure scores，然后嵌入 IRT 的 covariate 结构——这个**完整的技术路径**在之前不存在。Individual components being standard 不等于 their combination is trivial。IRT 文献中大量的方法论贡献正是将 existing statistical machinery 应用于新的 covariate 结构。

2. **γ 的参数化是非 trivial 的设计决策。** 将 contamination 建模为 logit-scale additive shift（outside discrimination bracket，Eq. 2）vs. inside bracket（Appendix G）是一个有理论含义的选择，类似于 IRT 文献中 pseudo-guessing 参数的 parameterization debate。论文虽未充分讨论（我的 W10），但 Table 10 的对比表明了有意识的方法论探索。

3. **RRF 到 IRT 的 pipeline 解决了一个真实的技术问题**：现有 contamination detection 方法产生的是 point estimates without uncertainty quantification；IRT 框架自然地将这些 signal 转化为 credible intervals。这不仅是 "应用"，而是解决了一个 estimation-theoretic gap。

建议折中：论文应在 Contributions 中更明确地区分 "the specific technical contribution (contamination-augmented IRT with continuous exposure covariates)" 和 "the empirical contribution (dose-response profiling)"。但将方法论部分降级为 "merely application" 会低估这项工作。

**[AGREE] R2-W5: Hill (1910) 应在 main text 中引用**

同意。dose-response 是论文标题和核心概念，Hill (1910) 是该领域的奠基性工作。仅在 Appendix AB 引用是 oversight。

---

### Minor 问题

**[AGREE] R2-M1:** 同意 Section 3.1 的符号引入需要更好的过渡。

**[AGREE] R2-M2:** Figure 1 的小子图确实在正常打印尺寸下难以辨读。

**[AGREE] R2-M3:** Abstract 字数需要作者自行验证。如果超过 200 词，这会从 Minor 升级为格式违规。

**[AGREE] R2-M4:** Discussion 确实偏短，practical implications 可以更具体。

**[AGREE] R2-M5:** 数据内容描述应更具体。

**[AGREE] R2-M6:** AI Assistance 披露本身合规，但提醒作者确保引用都经过深入阅读是合理的建议。

---

### 对 R2 Questions 的补充

**R2-Q2（LoRA vs full fine-tuning）**: 这是一个非常好的问题，与我的 W6（SFT 外部效度）紧密相关。LoRA 的低秩约束（r=16, Table 11 中记录）确实可能抑制 memorization 效应。如果 full fine-tuning 产生更强的 Collapse，那么当前观察到的 Benefit 模式可能是 LoRA 特有的 artifact。建议作者至少对一个模型做 full fine-tuning 消融。

**R2-Q5（instruction-following vs contamination transfer）**: 与我的 W8 一致。Cross-benchmark transfer 可能反映 SFT 引入的 instruction-following 能力提升，而非真正的 contamination 跨域传播。Volume 控制实验（Appendix R）对 GSMK 显示 53% volume contribution，进一步支持了这一 alternative explanation。

---

### 总结：与 R2 的共识与分歧

**共识（5/7 Should-Fix + 2/2 Must-Fix 方向一致）：**
- N1 overclaiming：方向一致，我认为 severity 略低（warning vs critical）
- N2 Han et al. 对比不足：方向一致，我认为 severity 略低（should-fix vs must-fix）
- W1 分类过拟合风险：完全同意
- W2 Benefit 因果解释：**高度同意，与我的 volume confound 发现互相强化**
- W3 域级别证据不足：完全同意，与我的 W1/W3 互补
- W5 Hill (1910)：完全同意
- Minor M1–M6：全部同意

**分歧：**
- **W4 方法论新颖性**：R2 认为主要是 application framework，我认为 contamination-augmented IRT with continuous exposure covariates 构成实质性方法论贡献。建议论文更清晰地 articulate 这一区分，而非降级方法论贡献。

**两位 Reviewer 合并后的 top priorities for revision：**
1. Volume confound + Benefit causality（R1-W2 + R2-W2）：需补充更多模型的 volume 控制，并重新框定 "dose-response" 的概念范围
2. Domain-level γ claims 需降级（R1-W1/W3 + R2-W3）：identifiability 不足 + 经验证据有限
3. 与 prior art 的区分需强化（R2-N1/N2）：Abstract claim 限定 + Han et al. 深入对比


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1270 · 2026-05-25T21:30:52.779301+00:00_

收到 Reviewer 1 的交叉回应。

**R1 交叉回应摘要：**

| R2 原始问题 | R1 立场 | 备注 |
|---|---|---|
| N1 Abstract overclaiming | AGREE | severity 降为 warning |
| N2 Han et al. 对比不足 | AGREE | severity 降为 should-fix |
| W1 分类过拟合 | AGREE | 补充 τ/σ sensitivity analysis 需求 |
| W2 Benefit 因果解释 | **AGREE（强化）** | 与 R1-W2 volume confound 合并 → **升级 must-fix** |
| W3 域级别证据不足 | AGREE | 与 R1-W1/W3 互补 |
| W4 方法论新颖性 | **REBUT** | R1 认为 contamination-augmented IRT 构成实质性方法论贡献 |
| W5 Hill (1910) | AGREE | |
| M1–M6 | 全部 AGREE | |

**唯一分歧点：W4 方法论新颖性定位。** R1 论点——组件组合非 trivial、γ 参数化有理论含义、RRF→IRT pipeline 解决了 estimation-theoretic gap——有说服力。

等待 Reviewer 2 的交叉回应。两份交叉回应到齐后评估收敛性，决定是否需要 Round 2 或直接合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 120

## Round 120

30 recorded events


### User

_source line 1271 · 2026-05-25T21:30:55.586638+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心要点：

- **5/7 个 Should-Fix + 2/2 个 Must-Fix 方向与 R2 一致**
- **唯一分歧在 W4（方法论新颖性）**：我认为 contamination-augmented IRT with continuous exposure covariates 不是简单的 "应用框架"，而是实质性方法论贡献，R2 评估偏低
- **最重要的共识**：R2 的 "Benefit 因果解释" concern 与我的 "volume confound" 发现从概念和方法两个角度互相强化，合并后构成论文最需要回应的问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-25T21:32:18.608673+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_external_review_status,get_visual_check_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_external_review_status,get_visual_check_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-25T21:32:18.609041+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-25T21:32:19.412547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-25T21:32:19.463583+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-25T21:32:27.699705+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-25T21:32:27.750467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-25T21:32:32.842273+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-25T21:32:33.344824+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-25T21:32:33.345171+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-25T21:32:33.646881+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:44.763907+00:00\", \"completed_at\": \"2026-05-25T21:19:25.916698+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Figure 1 图例文字偏小（约 6-7pt），多条线在低剂量区域密集重叠，审稿人可能需要放大才能区分 Phi-4 和 LLaMA-3.1 的曲线。建议加大 marker 差异或增加 legend 字号\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Table 1 列数较多（~8 列），全宽排列，最右几列内容紧凑但未溢出。精度统一（小数点后 2-3 位），最优值有加粗标注，booktabs 风格正确\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 右栏放置得当，但 MAE 列的数值精度不完全统一（部分 3 位小数，部分 4 位），建议统一到 3 位\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Section 5 \\\"Results\\\" heading 出现在左栏底部约 1/4 处，后面跟了 Section 5.1 标题 + 约 3 行正文，勉强不算孤悬但位置偏低\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"页面密度很高（Table 4 + Figure 5 + 5 个 subsection），信息量大但不影响可读性，Figure 5 的 caption 中 \\\"Filled markers: C1 excludes zero\\\" 字号偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 6 的 per-domain 点图清晰，CI 可读；Limitations 段落简短（~1 段），符合 EMNLP 要求\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix 最密集页：3 tables + 1 figure + 文字，Figure 8 的多面板子图 axis label 字号偏小（约 6pt），但因是 appendix，影响可控\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 10 (DID boxplot) 和 Figure 11 (DiD by dosage) 清晰度良好，双面板图 axis label 可读\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Algorithm 1 伪代码排版规范，使用 algorithmic 环境，缩进清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 2 pipeline 架构图全宽排列，三阶段颜色区分明确（蓝/橙/绿），caption 自包含，是全文最佳 display item\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 10}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-25T21:32:33.797954+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-25T21:32:33.898784+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-25T21:32:41.983084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-25T21:32:42.637143+00:00_

1	- id: "R2-N1"
2	  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 2
7	  last_seen_round: 6
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'."}
11	    - {round: 4, reviewers: "R1,R2", note: "Title promises decomposition but core result is nothing to decompose."}
12	    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
13	    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
14	    - {round: 8, reviewers: "", note: "本轮未提及。Title now 'Not All Models Are Inflated'."}
15	    - {round: 9, reviewers: "", note: "本轮未提及（fresh review）。"}
16	    - {round: 10, reviewers: "", note: "本轮未提及（fresh review）。"}
17	    - {round: 11, reviewers: "", note: "本轮未直接提及。新 overclaiming concerns under R8-N3 and R11-N1."}
18	    - {round: 12, reviewers: "", note: "本轮未直接提及（fresh review）。Title framing itself resolved; overclaiming tracked under R11-N1."}
19	    - {round: 13, reviewers: "", note: "本轮未直接提及（fresh review）。Title overclaiming tracked under R11-N1."}
20	  action_items:
21	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
22	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
23	    - {round: 4, action: "Reframe as empirical investigation", assigned_to: "paper_agent", status: "done"}
24	    - {round: 5, action: "Rewrite Introduction as question-driven", assigned_to: "paper_agent", status: "done"}
25	    - {round: 6, action: "Modify title to scope claim", assigned_to: "paper_agent", status: "done"}
26	  resolution: "Title changed to 'Not All Models Are Inflated'. Paper repositioned as empirical investigation."
27	  resolution_round: 
…[truncated 42914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-25T21:32:42.688036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-25T21:32:42.738718+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{amsmath}
9	\usepackage{amssymb}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{algorithm}
14	\usepackage{algpseudocode}
15	\usepackage{float}
16	\usepackage{alphalph}
17	\usepackage{flushend}
18	
19	\setlength{\belowcaptionskip}{-8pt}
20	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
21	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
22	
23	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\begin{abstract}
31	\input{abstract}
32	\end{abstract}
33	
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experimental_setup}
38	\input{results}
39	\input{conclusion}
40	
41	\input{limitations}
42	\input{ethics}
43	
44	\bibliography{references}
45	
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-25T21:34:16.748272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-25T21:34:16.798992+00:00_

1	Benchmark contamination is widely assumed to inflate language model scores, yet its actual effect has never been measured across model families. We perform controlled supervised fine-tuning (SFT) injection at five dosage levels into six models (7B to 14.7B) from five open-source families and discover a spectrum of dose-response patterns, not uniform inflation. Two patterns replicate across independent families: Immune (Phi-4, LLaMA-3.1) and Benefit (statistically significant for Gemma-2, bootstrap 95\% CI [$+$1.49, $+$3.14]\,pp; exploratory for OLMo-2 and Falcon3). Collapse and V-recovery are each observed in one family (Qwen2.5) across three seeds but remain preliminary pending independent replication. Effects are benchmark-conditional: MMLU-targeted contamination improves GSM8K in four of five non-excluded families, even those harmed on MMLU. Difference-in-differences analysis detects no item-specific memorization; a volume-matched control attributes 45\% of Benefit to data quantity. ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented Item Response Theory (IRT), enables within-family domain-level contamination diagnosis with credible intervals. On Qwen2.5, Social Sciences contamination effects are negative while STEM effects are positive, a pattern invisible to aggregate scoring. Out-of-sample validation on LLaMA-3.1-8B confirms that model family characteristics beyond baseline ability modulate vulnerability. Model-specific dose-response profiling is necessary for reliable benchmark interpretation\footnote{Code and data are available at \url{https://anonymous.4open.science/r/contamcal-irt-calibration-EB85/}.}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-25T21:40:14.465898+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
  "old_string": "    - {round: 13, reviewers: \"R2\", note: \"Coverage now comprehensive (50+ refs). Minor: Deng et al. cited as arXiv but may be NAACL 2024—update citation info. Schaeffer et al. discussion in §2 could be deeper.\"}",
  "new_string": "    - {round: 13, reviewers: \"R1,R2\", note: \"Coverage comprehensive (50+ refs). Hill (1910) dose-response foundational ref only in Appendix AB—must cite in main text. Deng et al. arXiv vs NAACL 2024 unverified. Schaeffer et al. §2 discussion insufficient.\"}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
    "old_string": "    - {round: 13, reviewers: \"R2\", note: \"Coverage now comprehensive (50+ refs). Minor: Deng et al. cited as arXiv but may be NAACL 2024—update citation info. Schaeffer et al. discussion in §2 could be deeper.\"}",
    "new_string": "    - {round: 13, reviewers: \"R1,R2\", note: \"Coverage comprehensive (50+ refs). Hill (1910) dose-response foundational ref only in Appendix AB—must cite in main text. Deng et al. arXiv vs NAACL 2024 unverified. Schaeffer et al. §2 discussion insufficient.\"}"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-25T21:40:14.918570+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Edit",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-25T21:40:16.224662+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
  "old_string": "    - {round: 13, action: \"Update Deng et al. citation to NAACL 2024 if published; deepen Schaeffer et al. discussion in §2\", assigned_to: \"paper_agent\", status: \"open\"}",
  "new_string": "    - {round: 13, action: \"Cite Hill (1910) in main text §1 or §3; update Deng et al. citation; deepen Schaeffer et al. in §2\", assigned_to: \"paper_agent\", status: \"open\"}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml",
    "old_string": "    - {round: 13, action: \"Update Deng et al. citation to NAACL 2024 if published; deepen Schaeffer et al. discussion in §2\", assigned_to: \"paper_agent\", status: \"open\"}",
    "new_string": "    - {round: 13, action: \"Cite Hill (1910) in main text §1 or §3; update Deng et al. citation; deepen Schaeffer et al. in §2\", assigned_to: \"paper_agent\", status: \"open\"}"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-25T21:40:16.276904+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Edit",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-25T21:40:20.243777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-25T21:40:20.546269+00:00_

1	- id: "R2-N1"
2	  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 2
7	  last_seen_round: 6
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'."}
11	    - {round: 4, reviewers: "R1,R2", note: "Title promises decomposition but core result is nothing to decompose."}
12	    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
13	    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
14	    - {round: 8, reviewers: "", note: "本轮未提及。Title now 'Not All Models Are Inflated'."}
15	    - {round: 9, reviewers: "", note: "本轮未提及（fresh review）。"}
16	    - {round: 10, reviewers: "", note: "本轮未提及（fresh review）。"}
17	    - {round: 11, reviewers: "", note: "本轮未直接提及。新 overclaiming concerns under R8-N3 and R11-N1."}
18	    - {round: 12, reviewers: "", note: "本轮未直接提及（fresh review）。Title framing itself resolved; overclaiming tracked under R11-N1."}
19	    - {round: 13, reviewers: "", note: "本轮未直接提及（fresh review）。Title overclaiming tracked under R11-N1."}
20	  action_items:
21	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
22	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
23	    - {round: 4, action: "Reframe as empirical investigation", assigned_to: "paper_agent", status: "done"}
24	    - {round: 5, action: "Rewrite Introduction as question-driven", assigned_to: "paper_agent", status: "done"}
25	    - {round: 6, action: "Modify title to scope claim", assigned_to: "paper_agent", status: "done"}
26	  resolution: "Title changed to 'Not All Models Are Inflated'. Paper repositioned as empirical investigation."
27	  resolution_round: 
…[truncated 42962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-25T21:45:06.186533+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title promises decomposition but core result is nothing to decompose.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Title now 'Not All Models Are Inflated'.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 11, reviewers: \"\", note: \"本轮未直接提及。新 overclaiming concerns under R8-N3 and R11-N1.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及（fresh review）。Title framing itself resolved; overclaiming tracked under R11-N1.\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未直接提及（fresh review）。Title overclaiming tracked under R11-N1.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction as question-driven\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Title changed to 'Not All Models Are Inflated'. Paper repositioned as empirical investigation.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Limitations discussion still too brief.\"}\n    - {round: 10, reviewers: \"\", note: \"Section 6 includes Schaeffer et al. comparison.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Re-raised as part of R11-N1.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Should-Fix W8. Add SFT-injected qualifier throughout main text.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Should-Fix. SFT injection simultaneously introduces content exposure + extra training signal + LoRA updates. Conceptual tension with 'contamination' framing. Cross-response consensus: Limitations must explicitly address SFT-to-pretraining generalizability.\"}\n  action_items:\n    - {round: 9, action: \"Expand SFT discussion in Section 6\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 12, action: \"Add SFT-injected qualifier at first occurrence of contamination in each section\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"DGP robustness appendix addresses this.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及（fresh review）。DGP simulation in Appendix addressed.\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance — P(γ<0) inconsistency and Bonferroni claim unstable\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text still presents J=13.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. P(γ<0) inconsistency between §5.7 and Appendix K.\"}\n    - {round: 12, reviewers: \"R1\", note: \"Minor-5: Abstract cites 99.7% without mentioning tight prior failure.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. γ posterior mean shifts 2.6× across priors (0.34→0.89). J=16 insufficient to override prior. Paper acknowledges in Appendix M but not in main text. Cross-response reinforced: R1 W1/W3 (identifiability) + R2 W3 (empirical evidence) converge.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Resolve P(γ<0) numerical inconsistency; mark γ conclusions exploratory\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 13, action: \"Discuss prior sensitivity in main text; acknowledge γ absolute values unreliable at J=16\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J — IRT results unreliable\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"MMLU PPP=0.16-0.25 only in Appendix, not main text.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Cross-benchmark direction based on raw accuracy not IRT. Paper should explicitly separate raw-accuracy and IRT-based conclusions.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. ARC PPP=0.003 (structural misfit acknowledged by authors) but ARC results still in main text §5.2 cross-benchmark transfer. Misleading.\"}\n  action_items:\n    - {round: 9, action: \"Add ARC PPP=0.003 discussion in main text\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report MMLU PPP in main text\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 12, action: \"Add explicit statement in §5.2 that cross-benchmark direction conclusions are based on raw accuracy, not IRT estimates\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Move ARC IRT results entirely to appendix; main text ARC conclusions should use raw accuracy only\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — S2/S4 near-random signals retained despite evidence of harm\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete. Downgraded to warning.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"S2/S4 AUC≈0.48-0.51 near random.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. S1-only pipeline needed as reference baseline. S2 actively harmful at model level.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Removing S2 improves ρ_dose from 0.049 to 0.471 (~10× improvement). S2 actively suppresses dosage discrimination at model level. Item-level ρ≈0.773 defense does not justify model-level harm. Must test full pipeline without S2.\"}\n  action_items:\n    - {round: 9, action: \"Report s_ij classification performance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 12, action: \"Run S1-only pipeline IRT fitting; report γ + MAE comparison vs full RRF\", assigned_to: \"main_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Run pipeline without S2; report downstream ContamCal MAE as Appendix supplementary data (not replace main analysis)\", assigned_to: \"main_agent\", status: \"in_progress\"}\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need coverage + root cause.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis insufficient.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  resolution: \"Root-cause diagnosis in §5.5.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own analysis is underpowered.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n  resolution: \"Results §5 specifies J=16 for domain γ.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI not reported.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 5, action: \"Rename to Cross-Family Exploratory Analysis\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete.\"\n  resolution_round: 5\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation unverified\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc.\"\n  resolution_round: 6\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu, Sainz et al., Yang et al.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"58 citations verified, references now comprehensive.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"New missing: Rodriguez et al. (2021), Carlini et al. (2023), Gu et al. (2024) OLMES.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"4 new: Oren et al. (2024 ICLR), Deng et al. (2024 NAACL), Yang et al. (2023), Gu et al. (2024 OLMES).\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Coverage comprehensive (50+ refs). Hill (1910) dose-response foundational ref only in Appendix AB—must cite in main text. Deng et al. arXiv vs NAACL 2024 unverified. Schaeffer et al. §2 discussion insufficient.\"}\n  action_items:\n    - {round: 11, action: \"Add Rodriguez et al., Carlini et al., Gu et al.\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Verify and add Oren et al. (2024), Deng et al. (2024), Yang et al. (2023), Gu et al. (2024)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Cite Hill (1910) in main text §1 or §3; update Deng et al. citation; deepen Schaeffer et al. in §2\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"~6+ quantitative claims in Abstract.\"}\n    - {round: 7, reviewers: \"\", note: \"Abstract rewritten. Resolved.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Re-raised: ~25+ numbers. Core message buried.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. 20+ numbers in ~193 words. Core insight buried.\"}\n  action_items:\n    - {round: 12, action: \"Reduce Abstract to 8-10 key numbers, ≤200 words\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both suggest explicit positioning statement.\"}\n    - {round: 11, reviewers: \"R2\", note: \"Excitement=2.5.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"ContamCal MAE worse than raw further weakens method contribution. Reposition as diagnostic framework.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"DIVERGENT. R2 maintains 2PL+γ is standard DIF. R1 partially rebuts: continuous RRF exposure → IRT covariate pipeline is novel integration; γ parameterization (outside vs inside a_i) is non-trivial design decision; IRT provides credible intervals unavailable from raw accuracy. Both agree positioning statement needed.\"}\n  action_items:\n    - {round: 10, action: \"Add explicit positioning statement\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Reposition ContamCal as diagnostic framework in Abstract/Intro/§3.4\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Explicitly state 2PL+γ is standard explanatory IRT; contribution is application to LLM contamination + multi-signal exposure + causal framework\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R2-W8\"\n  summary: \"Related Work gaps — Han et al. and Schaeffer et al. differentiation\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree dedicated comparison needed.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"DIVERGENT on Schaeffer severity.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。Section 2 comparison paragraph exists.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Han et al. §2 adequate at method level. Schaeffer et al. §2 discussion insufficient—statistical power analysis highly relevant to n=3 seed limitation. Cross-response consensus: R1 notes Han uses group-level binary DIF vs this paper's continuous exposure; both agree empirical cross-comparison lacking.\"}\n  action_items:\n    - {round: 10, action: \"Expand Han/Schaeffer discussion\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R5-N1\"\n  summary: \"Page limit compliance\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - {round: 9, reviewers: \"R2\", note: \"8 pages confirmed.\"}\n    - {round: 12, reviewers: \"visual\", note: \"Visual check confirms 8 pages main text. Compliant.\"}\n    - {round: 13, reviewers: \"R2,visual\", note: \"Confirmed compliant. 8 pages main text, Limitations on p.8.\"}\n  resolution: \"Confirmed 8 pages main text, EMNLP 2026 compliant.\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"SFT AUGMENT mode volume confound\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"AUGMENT vs REPLACE not specified.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"d000=50k, d100≈66.5k (+33.1%). Should-Fix.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. Data-quantity control most critical missing experiment.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Should-Fix. Volume control on Falcon3 done (45%/55%). Generalizability unverified—needs at least one non-Benefit family.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Falcon3 volume control done but covers only 1/6 models. 45% volume contribution is large. Collapse (Qwen-14B -25pp) lacks volume control—catastrophic forgetting from extra training is unrebutted alternative. Cross-response strongest consensus: R1 W2 (method) + R2 W2 (concept) converge—dose-response x-axis is contamination+volume+LoRA confound axis.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report training set sizes per dosage\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 11, action: \"Add data-quantity control\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 12, action: \"Acknowledge single-family limitation in Limitations; note Collapse corrected harm -11.3pp strengthens contamination-specificity\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Keep dose-response terminology; add Discussion paragraph on contamination vs volume vs LoRA triple confound; surface Falcon3 45%/55% more prominently; Limitations caveat on single-family volume control\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 signal computation details\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix E added.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix F added.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Within-family GSM8K PPP not reported.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"n=3 seeds yields wide CIs; strict sign consistency only 2/5.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"n=3 acceptable given compute. Downgraded to Minor.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Major. Re-raised.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. OLMo-2 CI crosses zero. Gemma-2 CI [+1.49,+3.14] excludes zero. AICc: Gemma-2/OLMo-2 curve shape indistinguishable from constant.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. n=3 BCa bootstrap has minimal resample space. OLMo-2 borderline. AICc shows Gemma-2/OLMo-2 indistinguishable from constant. R1 notes only Immune (Phi-4) is statistically robust across seeds.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 or weaken claims\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 11, action: \"Report p-value for directional test under H0\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Report AICc in main text; keep Gemma-2 Benefit (CI excludes zero); relabel OLMo-2 as borderline; reframe Benefit as 2 significant + 1 borderline\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Contribution 2 reframed with MDES.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"DiD rated Acceptable.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。DiD analysis not re-raised.\"}\n  resolution: \"Contribution 2 includes 'at current power levels'. MDES reported.\"\n  resolution_round: 9\n\n- id: \"R8-N3\"\n  summary: \"N=6 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"4 patterns on 4 families is post-hoc.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Reposition as 'observed profiles'.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. Collapse n=1, V-recovery n=1.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Qwen within-family inconsistency.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical (strongest). Restructure to 2+2 framework.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Collapse/V-recovery both Qwen2.5-only. n=1 family insufficient for generalizable pattern category. R1 further notes even Benefit statistical basis is weak (AICc indistinguishable from constant for Gemma-2/OLMo-2). Must restructure to 2 confirmed + 2 preliminary.\"}\n  action_items:\n    - {round: 9, action: \"Fix §5.1 count. Use 'preliminary at N=5'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Replace 'taxonomy' with 'profiles'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 11, action: \"Discuss within-family inconsistency\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 12, action: \"Restructure to 2+2 framework: 2 replicated (Immune, Benefit) + 2 preliminary Qwen2.5-specific (Collapse, V-recovery)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. is most direct prior work.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"DIVERGENT on Schaeffer severity.\"}\n    - {round: 12, reviewers: \"\", note: \"Section 2 comparison paragraph exists. Not re-raised.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Han et al. differentiation in §2 adequate at method level (R1 cross-response notes: binary group DIF vs continuous exposure, no dose-response capability, observational vs controlled). Lacks empirical cross-comparison. Schaeffer et al. §2 discussion needs expansion.\"}\n  action_items:\n    - {round: 8, action: \"Add methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"'significant', 'p-value' in frequentist sense.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"DIVERGENT→RESOLVED. R2 raises as Should-Fix. R1 rebuts: field norm in NLP, no logical contradiction. Consensus: label CI types (credible vs confidence) at first occurrence.\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 13, action: \"Label CI types at first occurrence: credible interval (Bayesian IRT) vs confidence interval (bootstrap)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-W2\"\n  summary: \"Identifiability simulation uses uniform exposure vs empirical right-skewed\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Empirical RRF highly right-skewed.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Re-run simulation with right-skewed exposure\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold τ=2pp lacks theoretical basis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"30/30 pass too coarse.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Appendix includes nearest-transition analysis.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"DIVERGENT: R1 Major, R2 Critical.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Label as descriptive heuristic or provide permutation null.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Algorithm 1 is descriptive heuristic, not method contribution. Appendix U sensitivity sweep helps but does not change fundamental nature. Position as 'organizational framework for experimental results'. Cross-response: R1 adds τ and σ sensitivity analysis needed.\"}\n  action_items:\n    - {round: 11, action: \"Report Immune/Benefit boundary sensitivity\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 12, action: \"Label Algorithm 1 as descriptive heuristic in §4\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu, Sainz et al., Yang et al.\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Three missing refs.\"}\n    - {round: 10, reviewers: \"\", note: \"Golchin & Surdeanu and Sainz now cited.\"}\n    - {round: 12, reviewers: \"\", note: \"Merged into R4-W4.\"}\n  action_items:\n    - {round: 8, action: \"Add missing references\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — Figure 1 caption, Table formatting\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Figure 1 y-axis ranges differ across panels.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Figure 1 y-axis 50-75%.\"}\n    - {round: 12, reviewers: \"visual\", note: \"Figure 3 heatmap cell text small. Figure 6 text at readability limit.\"}\n    - {round: 13, reviewers: \"R1,visual\", note: \"Figure 1 y-axis range inconsistent. Figure 2/3 heatmap cell text too small for print. Figure 1 caption ~60 words, too dense.\"}\n  action_items:\n    - {round: 12, action: \"Fix Figure 1 Y-axis label to 'Δ Accuracy (percentage points)'\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"AUDIT-1\"\n  summary: \"Figure 1 missing from PDF\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"audit\", note: \"Figure 1 does not exist.\"}\n    - {round: 9, reviewers: \"\", note: \"Figure 1 present on page 2.\"}\n    - {round: 12, reviewers: \"visual\", note: \"Confirmed present on page 2.\"}\n    - {round: 13, reviewers: \"visual\", note: \"Confirmed present on page 2.\"}\n  resolution: \"Figure 1 present in Introduction.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy based on ad-hoc Algorithm 1 — lacks parametric DR modeling\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Pharmacology has parametric DR models.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Appendix W: parametric DR comparison added.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。Parametric comparison exists.\"}\n  resolution: \"Appendix W: Parametric DR Model Comparison added.\"\n  resolution_round: 9\n\n- id: \"R9-N2\"\n  summary: \"'Architecture determines vulnerability' causal claim exceeds evidence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Replace with 'family-level factors'.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。\"}\n  resolution: \"All causal claims replaced. Confounders listed.\"\n  resolution_round: 9\n\n- id: \"R9-S1\"\n  summary: \"Unified LoRA r=16 unequal treatment strength across scales\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Parameter fraction 0.45% (Phi-4) to 2.10%.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Phi-4 vs Qwen-14B counter-argument has merit.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"DIVERGENT. R1 maintains concern; R2 considers largely addressed by same-scale comparison.\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未直接提及。Limitations discussion exists.\"}\n  action_items:\n    - {round: 9, action: \"Discuss LoRA confound in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report trainable parameter percentages\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R9-S2\"\n  summary: \"'65-70% MMLU baseline vulnerability band' over-precise for N=6\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Qualify with 'in our five-family sample'.\"}\n    - {round: 10, reviewers: \"\", note: \"All claims qualified. Resolved.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Reopened. Band = 2 Qwen models only. LLaMA contradicts.\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未直接提及。Discussion §6 mentions 65-70% with LLaMA-3.1 contradiction acknowledged.\"}\n  action_items:\n    - {round: 12, action: \"Remove 65-70% from Abstract/Intro; downgrade to Discussion observational association\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R9-S3\"\n  summary: \"Calibration baseline missing IRT variants\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"2PL vs 2PL+γ ablation would be better.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及。\"}\n  action_items:\n    - {round: 9, action: \"Add 2PL vs 2PL+γ ablation\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R10-N1\"\n  summary: \"ContamCal calibration MAE (0.009) worse than raw accuracy (0.006)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R2\", note: \"Core method underperforms 'do nothing' baseline.\"}\n    - {round: 10, reviewers: \"R1\", note: \"REBUT: §3.3 predicts this; γ serves diagnosis.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Reposition as diagnostic framework, not calibration tool.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical (strongest consensus). MMLU MAE=0.009>0.006, ARC MAE=0.020>0.007. Method name 'ContamCal' promises calibration but delivers worse-than-baseline results. 'Value lies in diagnosis' defense itself problematic—if observed dosages produce small effects, framework's practical utility is questionable. R1 notes IRT provides credible intervals and item-level modeling unavailable from raw accuracy, but concedes γ unreliability (N3) undermines these incremental benefits.\"}\n  action_items:\n    - {round: 10, action: \"Clarify ContamCal value is diagnostic not calibration\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Reposition ContamCal as diagnostic framework in Abstract/Intro; contextualize Table 3 MAE\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Rewrite §5.5 from 'Calibration Quality' to 'Diagnostic Utility'; lead with domain-level γ_d vs raw accuracy contrast (Social Sciences γ_d=-0.63 vs pooled non-significant); contextualize aggregate MAE as non-target\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R10-W1\"\n  summary: \"γ parameterization outside a_i bracket unjustified\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Non-uniform vs uniform DIF.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Notation improved. Substantive question unanswered.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Both recommend Appendix comparison (PPP, WAIC).\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"DIVERGENT→RESOLVED. R2 rebuts R1: ΔELPD≈0 actually supports author's choice (neither better). R1 accepts. Consensus: state choice is interpretive convenience (ΔELPD≈0), not statistical evidence.\"}\n  action_items:\n    - {round: 10, action: \"Justify γ outside a_i or compare with inside-a_i form\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 12, action: \"Run uniform vs non-uniform DIF comparison (PPP/WAIC) if time permits\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 13, action: \"Add one sentence in §3.2 noting ΔELPD≈0 and choice is for interpretive convenience\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R10-W2\"\n  summary: \"300/14042 MMLU item subset — selection bias toward high-exposure-variance items\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. 2.1% of items selected.\"}\n    - {round: 11, reviewers: \"R1\", note: \"High exposure variance items may be systematically different.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Report subset distribution comparison. Attempt full-item or larger subset IRT.\"}\n    - {round: 13, reviewers: \"R1\", note: \"Minor. KS/χ² tests in §5.5 confirm representativeness (p=0.946/0.574). But exposure variance bias untested—should mention in limitations.\"}\n  action_items:\n    - {round: 12, action: \"Compute 300 vs 14042 difficulty/domain distribution comparison + KS test\", assigned_to: \"main_agent\", status: \"in_progress\"}\n\n- id: \"R11-N1\"\n  summary: \"Abstract/Title overclaiming — 'Not All Models Are Inflated' exceeds evidence from 6 models ≤14B under SFT\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Three overclaim dimensions.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Strongly reinforced. Title implies generality for N=6 SFT study.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Title scope exceeds evidence: 6 models ≤14.7B, all SFT, all open-source. R1 cross-response: claim defensible if scoped to 'SFT-stage + 7B-14B + diverse families', but current wording lacks qualification. Schaeffer et al. (2025) and Bordt et al. (2025) performed controlled injection at smaller scale.\"}\n  action_items:\n    - {round: 11, action: \"Add scope qualifier to title; soften Abstract language\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Strengthen scope qualification in Abstract; keep title but soften surrounding language\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Abstract first sentence must scope: 6 models, 7-14B, 5 open-source families, SFT injection\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R11-W1\"\n  summary: \"DiD parallel trends assumption untested\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"No pre-treatment trend comparison.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"DIVERGENT. R2 rebuts: controlled experiment, pre-treatment balance strong (Cohen's d=0.02).\"}\n  action_items:\n    - {round: 11, action: \"Report pre-treatment balance; add parallel trends discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Pre-treatment balance reported (Cohen's d=0.02, p>0.19). Controlled experiment design largely mitigates concern.\"\n  resolution_round: 12\n\n- id: \"R11-W2\"\n  summary: \"'Contamination' vs 'additional training' conceptual tension\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Major. DiD null + augmentation confound.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Should-Fix. Volume control 45%/55% clarifies but terminology needs precision.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. SFT injection = content exposure + extra volume + LoRA updates. Table 1 labels conflate all three as 'contamination response'. Volume control shows 45% is volume. §6 Discussion paragraph exists but insufficient. Cross-response: R2 concept concern + R1 method concern converge to challenge core narrative framing.\"}\n  action_items:\n    - {round: 11, action: \"Distinguish contamination-specific from general training effects\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Add Discussion paragraph defining contamination vs additional training in this framework\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Expand Discussion paragraph: triple confound (content/volume/LoRA), surface 45%/55% Falcon3 split prominently, Limitations caveat on single-family control\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R11-W3\"\n  summary: \"2PL+γ identifiability — θ and γ·e collinearity with b\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R2,R1\", note: \"Potential collinearity if e_ij correlates with b_j.\"}\n    - {round: 12, reviewers: \"\", note: \"§3.3 includes identifiability discussion: |r|<0.13, R²<0.014.\"}\n  action_items:\n    - {round: 11, action: \"Expand identifiability discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"§3.3 reports e_ij and b_i near-orthogonal (|r|<0.13, R²<0.014).\"\n  resolution_round: 12\n\n- id: \"R11-M1\"\n  summary: \"Benchmark diversity insufficient — MMLU dominates\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - {round: 11, reviewers: \"R2\", note: \"Only 3 benchmarks, MMLU dominates.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"DIVERGENT. R1 rebuts: 3 formats comprehensive. Both agree MMLU-driven but acceptable.\"}\n  action_items:\n    - {round: 11, action: \"Scope cross-benchmark conclusions\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"3 benchmarks across 3 formats accepted. MMLU dominance acknowledged. Not re-raised as must-fix.\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"Algorithm 1 Benefit sub-branches both return same label — dead code\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: \"R1,R2\", note: \"Lines 91-94 both return BENEFIT. Remove dead logic or add sub-labels.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Re-confirmed. Two branches (saturating/sustained gain) both return BENEFIT. Either design remnant or intentional merge—either way, remove redundant branching.\"}\n  action_items:\n    - {round: 12, action: \"Remove unused branching logic in Algorithm 1\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R12-M2\"\n  summary: \"Stage 1→Stage 2 uncertainty propagation missing — e_ij is point estimate\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: \"R1\", note: \"RRF is rank-based non-parametric. Uncertainty propagation non-trivial.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. e_ij from RRF enters IRT as fixed covariate. Exposure measurement error → γ CI underestimated. Especially severe at J=16 where uncertainty is already large. May partly explain γ instability (R4-N1).\"}\n  action_items:\n    - {round: 12, action: \"Acknowledge e_ij point estimate limitation; mention as future work\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R13-W1\"\n  summary: \"DiD MDES 1.2-2.0pp practical significance boundary undiscussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: \"R1\", note: \"MDES 1.2-2.0pp rules out effects >2pp but 1pp item-specific effects may matter in high-stakes evaluation. Paper does not discuss practical significance threshold.\"}\n  action_items:\n    - {round: 13, action: \"Discuss MDES practical significance in context of real-world contamination scenarios\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R13-m5\"\n  summary: \"Table 1 'Stab.' column definition unclear\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: \"R1,R2\", note: \"Stab. column in Table 1 not defined in caption or footnote.\"}\n  action_items:\n    - {round: 13, action: \"Add footnote defining Stab. column in Table 1\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R13-m6\"\n  summary: \"ρ=0.3 saturation ratio source not cited\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: \"R1\", note: \"ρ=0.3 saturation ratio used in Algorithm 1 without source.\"}\n  action_items:\n    - {round: 13, action: \"Add source or justification for ρ=0.3\", assigned_to: \"paper_agent\", status: \"in_progress\"}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title promises decomposition but core result is nothing to decompose.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form but framing still inconsistent.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes.\"}\n    - {round: 8, reviewers: \"\", note: \"本轮未提及。Title now 'Not All Models Are Inflated'.\"}\n    - {round: 9, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 10, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 11, reviewers: \"\", note: \"本轮未直接提及。新 overclaiming concerns under R8-N3 and R11-N1.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及（fresh review）。Title framing itself resolved; overclaiming tracked under R11-N1.\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未直接提及（fresh review）。Title overclaiming tracked under R11-N1.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction as question-driven\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Title changed to 'Not All Models Are Inflated'. Paper repositioned as empirical investigation.\"\n  resolution_round: 7\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Limitations discussion still too brief.\"}\n    - {round: 10, reviewers: \"\", note: \"Section 6 includes Schaeffer et al. comparison.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Re-raised as part of R11-N1.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Should-Fix W8. Add SFT-injected qualifier throughout main text.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Should-Fix. SFT injection simultaneously introduces content exposure + extra training signal + LoRA updates. Conceptual tension with 'contamination' framing. Cross-response consensus: Limitations must explicitly address SFT-to-pretraining generalizability.\"}\n  action_items:\n    - {round: 9, action: \"Expand SFT discussion in Section 6\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 12, action: \"Add SFT-injected qualifier at first occurrence of contamination in each section\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R2 proposes threshold DGP simulation.\"}\n    - {round: 8, reviewers: \"\", note: \"DGP robustness appendix addresses this.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及（fresh review）。DGP simulation in Appendix addressed.\"}\n  resolution: \"400-run threshold DGP simulation completed. Appendix P written.\"\n  resolution_round: 7\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance — P(γ<0) inconsistency and Bonferroni claim unstable\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Bonferroni α=0.00625; CI upper bound likely includes zero.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Social Sciences at 99.1% does not pass Bonferroni.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"J=16 data available but main text still presents J=13.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. P(γ<0) inconsistency between §5.7 and Appendix K.\"}\n    - {round: 12, reviewers: \"R1\", note: \"Minor-5: Abstract cites 99.7% without mentioning tight prior failure.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. γ posterior mean shifts 2.6× across priors (0.34→0.89). J=16 insufficient to override prior. Paper acknowledges in Appendix M but not in main text. Cross-response reinforced: R1 W1/W3 (identifiability) + R2 W3 (empirical evidence) converge.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni corrected results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16 results\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Resolve P(γ<0) numerical inconsistency; mark γ conclusions exploratory\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 13, action: \"Discuss prior sensitivity in main text; acknowledge γ absolute values unreliable at J=16\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J — IRT results unreliable\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003. Move ARC IRT to Appendix.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"MMLU PPP=0.16-0.25 only in Appendix, not main text.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Cross-benchmark direction based on raw accuracy not IRT. Paper should explicitly separate raw-accuracy and IRT-based conclusions.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. ARC PPP=0.003 (structural misfit acknowledged by authors) but ARC results still in main text §5.2 cross-benchmark transfer. Misleading.\"}\n  action_items:\n    - {round: 9, action: \"Add ARC PPP=0.003 discussion in main text\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report MMLU PPP in main text\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 12, action: \"Add explicit statement in §5.2 that cross-benchmark direction conclusions are based on raw accuracy, not IRT estimates\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Move ARC IRT results entirely to appendix; main text ARC conclusions should use raw accuracy only\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — S2/S4 near-random signals retained despite evidence of harm\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation complete. Downgraded to warning.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"S2/S4 AUC≈0.48-0.51 near random.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. S1-only pipeline needed as reference baseline. S2 actively harmful at model level.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Removing S2 improves ρ_dose from 0.049 to 0.471 (~10× improvement). S2 actively suppresses dosage discrimination at model level. Item-level ρ≈0.773 defense does not justify model-level harm. Must test full pipeline without S2.\"}\n  action_items:\n    - {round: 9, action: \"Report s_ij classification performance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 12, action: \"Run S1-only pipeline IRT fitting; report γ + MAE comparison vs full RRF\", assigned_to: \"main_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Run pipeline without S2; report downstream ContamCal MAE as Appendix supplementary data (not replace main analysis)\", assigned_to: \"main_agent\", status: \"in_progress\"}\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need coverage + root cause.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Root cause diagnosis insufficient.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  resolution: \"Root-cause diagnosis in §5.5.\"\n  resolution_round: 7\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own analysis is underpowered.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。J=16 now in main text.\"}\n  resolution: \"Results §5 specifies J=16 for domain γ.\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Mean a_i comparison shows no discrimination confound.\"\n  resolution_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 may reflect higher average a_i.\"}\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"MAE CI not reported.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 5, action: \"Rename to Cross-Family Exploratory Analysis\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Full prior sensitivity complete.\"\n  resolution_round: 5\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation unverified\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Conclusion scoped. Hypothesis labeled post-hoc.\"\n  resolution_round: 6\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"3 empirical contributions.\"\n  resolution_round: 7\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. EACL 2026 most direct concurrent work.\"}\n    - {round: 8, reviewers: \"R1,R2\", note: \"New missing refs: Golchin & Surdeanu, Sainz et al., Yang et al.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"58 citations verified, references now comprehensive.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"New missing: Rodriguez et al. (2021), Carlini et al. (2023), Gu et al. (2024) OLMES.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"4 new: Oren et al. (2024 ICLR), Deng et al. (2024 NAACL), Yang et al. (2023), Gu et al. (2024 OLMES).\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Coverage comprehensive (50+ refs). Hill (1910) dose-response foundational ref only in Appendix AB—must cite in main text. Deng et al. arXiv vs NAACL 2024 unverified. Schaeffer et al. §2 discussion insufficient.\"}\n  action_items:\n    - {round: 11, action: \"Add Rodriguez et al., Carlini et al., Gu et al.\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Verify and add Oren et al. (2024), Deng et al. (2024), Yang et al. (2023), Gu et al. (2024)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Cite Hill (1910) in main text §1 or §3; update Deng et al. citation; deepen Schaeffer et al. in §2\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"~6+ quantitative claims in Abstract.\"}\n    - {round: 7, reviewers: \"\", note: \"Abstract rewritten. Resolved.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Re-raised: ~25+ numbers. Core message buried.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. 20+ numbers in ~193 words. Core insight buried.\"}\n  action_items:\n    - {round: 12, action: \"Reduce Abstract to 8-10 key numbers, ≤200 words\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both suggest explicit positioning statement.\"}\n    - {round: 11, reviewers: \"R2\", note: \"Excitement=2.5.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"ContamCal MAE worse than raw further weakens method contribution. Reposition as diagnostic framework.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"DIVERGENT. R2 maintains 2PL+γ is standard DIF. R1 partially rebuts: continuous RRF exposure → IRT covariate pipeline is novel integration; γ parameterization (outside vs inside a_i) is non-trivial design decision; IRT provides credible intervals unavailable from raw accuracy. Both agree positioning statement needed.\"}\n  action_items:\n    - {round: 10, action: \"Add explicit positioning statement\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Reposition ContamCal as diagnostic framework in Abstract/Intro/§3.4\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Explicitly state 2PL+γ is standard explanatory IRT; contribution is application to LLM contamination + multi-signal exposure + causal framework\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R2-W8\"\n  summary: \"Related Work gaps — Han et al. and Schaeffer et al. differentiation\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree dedicated comparison needed.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"DIVERGENT on Schaeffer severity.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。Section 2 comparison paragraph exists.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Han et al. §2 adequate at method level. Schaeffer et al. §2 discussion insufficient—statistical power analysis highly relevant to n=3 seed limitation. Cross-response consensus: R1 notes Han uses group-level binary DIF vs this paper's continuous exposure; both agree empirical cross-comparison lacking.\"}\n  action_items:\n    - {round: 10, action: \"Expand Han/Schaeffer discussion\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R5-N1\"\n  summary: \"Page limit compliance\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - {round: 9, reviewers: \"R2\", note: \"8 pages confirmed.\"}\n    - {round: 12, reviewers: \"visual\", note: \"Visual check confirms 8 pages main text. Compliant.\"}\n    - {round: 13, reviewers: \"R2,visual\", note: \"Confirmed compliant. 8 pages main text, Limitations on p.8.\"}\n  resolution: \"Confirmed 8 pages main text, EMNLP 2026 compliant.\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"k reserved for benchmark, d for domain.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"SFT AUGMENT mode volume confound\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"AUGMENT vs REPLACE not specified.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"d000=50k, d100≈66.5k (+33.1%). Should-Fix.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. Data-quantity control most critical missing experiment.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Should-Fix. Volume control on Falcon3 done (45%/55%). Generalizability unverified—needs at least one non-Benefit family.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Falcon3 volume control done but covers only 1/6 models. 45% volume contribution is large. Collapse (Qwen-14B -25pp) lacks volume control—catastrophic forgetting from extra training is unrebutted alternative. Cross-response strongest consensus: R1 W2 (method) + R2 W2 (concept) converge—dose-response x-axis is contamination+volume+LoRA confound axis.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report training set sizes per dosage\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 11, action: \"Add data-quantity control\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 12, action: \"Acknowledge single-family limitation in Limitations; note Collapse corrected harm -11.3pp strengthens contamination-specificity\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Keep dose-response terminology; add Discussion paragraph on contamination vs volume vs LoRA triple confound; surface Falcon3 45%/55% more prominently; Limitations caveat on single-family volume control\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R6-W2\"\n  summary: \"S4 signal computation details\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix E added.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix F added.\"\n  resolution_round: 8\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"Within-family GSM8K PPP not reported.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-N1\"\n  summary: \"Cross-seed stability claims overstated — n=3 seeds insufficient for taxonomy validation\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"n=3 seeds yields wide CIs; strict sign consistency only 2/5.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"n=3 acceptable given compute. Downgraded to Minor.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Major. Re-raised.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. OLMo-2 CI crosses zero. Gemma-2 CI [+1.49,+3.14] excludes zero. AICc: Gemma-2/OLMo-2 curve shape indistinguishable from constant.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. n=3 BCa bootstrap has minimal resample space. OLMo-2 borderline. AICc shows Gemma-2/OLMo-2 indistinguishable from constant. R1 notes only Immune (Phi-4) is statistically robust across seeds.\"}\n  action_items:\n    - {round: 8, action: \"Increase seeds to n≥5 or weaken claims\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 11, action: \"Report p-value for directional test under H0\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Report AICc in main text; keep Gemma-2 Benefit (CI excludes zero); relabel OLMo-2 as borderline; reframe Benefit as 2 significant + 1 borderline\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-N2\"\n  summary: \"DiD null result lacks power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Contribution 2 reframed with MDES.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"DiD rated Acceptable.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。DiD analysis not re-raised.\"}\n  resolution: \"Contribution 2 includes 'at current power levels'. MDES reported.\"\n  resolution_round: 9\n\n- id: \"R8-N3\"\n  summary: \"N=6 model families supporting 4-class taxonomy — generalization evidence insufficient\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"4 patterns on 4 families is post-hoc.\"}\n    - {round: 9, reviewers: \"R1,R2\", note: \"Reposition as 'observed profiles'.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Must-Fix. Collapse n=1, V-recovery n=1.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Qwen within-family inconsistency.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical (strongest). Restructure to 2+2 framework.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Collapse/V-recovery both Qwen2.5-only. n=1 family insufficient for generalizable pattern category. R1 further notes even Benefit statistical basis is weak (AICc indistinguishable from constant for Gemma-2/OLMo-2). Must restructure to 2 confirmed + 2 preliminary.\"}\n  action_items:\n    - {round: 9, action: \"Fix §5.1 count. Use 'preliminary at N=5'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Replace 'taxonomy' with 'profiles'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 11, action: \"Discuss within-family inconsistency\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 12, action: \"Restructure to 2+2 framework: 2 replicated (Immune, Benefit) + 2 preliminary Qwen2.5-specific (Collapse, V-recovery)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-N4\"\n  summary: \"Han et al. (2026) differentiation insufficient\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Han et al. is most direct prior work.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"DIVERGENT on Schaeffer severity.\"}\n    - {round: 12, reviewers: \"\", note: \"Section 2 comparison paragraph exists. Not re-raised.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Han et al. differentiation in §2 adequate at method level (R1 cross-response notes: binary group DIF vs continuous exposure, no dose-response capability, observational vs controlled). Lacks empirical cross-comparison. Schaeffer et al. §2 discussion needs expansion.\"}\n  action_items:\n    - {round: 8, action: \"Add methodological comparison with Han et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-W1\"\n  summary: \"Bayesian and frequentist terminology mixed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"'significant', 'p-value' in frequentist sense.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"DIVERGENT→RESOLVED. R2 raises as Should-Fix. R1 rebuts: field norm in NLP, no logical contradiction. Consensus: label CI types (credible vs confidence) at first occurrence.\"}\n  action_items:\n    - {round: 8, action: \"Unify terminology\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 13, action: \"Label CI types at first occurrence: credible interval (Bayesian IRT) vs confidence interval (bootstrap)\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-W2\"\n  summary: \"Identifiability simulation uses uniform exposure vs empirical right-skewed\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Empirical RRF highly right-skewed.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及（fresh review）。\"}\n  action_items:\n    - {round: 8, action: \"Re-run simulation with right-skewed exposure\", assigned_to: \"main_agent\", status: \"open\"}\n\n- id: \"R8-W3\"\n  summary: \"Algorithm 1 threshold τ=2pp lacks theoretical basis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"R2,R1\", note: \"30/30 pass too coarse.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Appendix includes nearest-transition analysis.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"DIVERGENT: R1 Major, R2 Critical.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Label as descriptive heuristic or provide permutation null.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Algorithm 1 is descriptive heuristic, not method contribution. Appendix U sensitivity sweep helps but does not change fundamental nature. Position as 'organizational framework for experimental results'. Cross-response: R1 adds τ and σ sensitivity analysis needed.\"}\n  action_items:\n    - {round: 11, action: \"Report Immune/Benefit boundary sensitivity\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 12, action: \"Label Algorithm 1 as descriptive heuristic in §4\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R8-M1\"\n  summary: \"Missing references — Golchin & Surdeanu, Sainz et al., Yang et al.\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1,R2\", note: \"Three missing refs.\"}\n    - {round: 10, reviewers: \"\", note: \"Golchin & Surdeanu and Sainz now cited.\"}\n    - {round: 12, reviewers: \"\", note: \"Merged into R4-W4.\"}\n  action_items:\n    - {round: 8, action: \"Add missing references\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R8-M2\"\n  summary: \"Minor writing issues — Figure 1 caption, Table formatting\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Figure 1 y-axis ranges differ across panels.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Figure 1 y-axis 50-75%.\"}\n    - {round: 12, reviewers: \"visual\", note: \"Figure 3 heatmap cell text small. Figure 6 text at readability limit.\"}\n    - {round: 13, reviewers: \"R1,visual\", note: \"Figure 1 y-axis range inconsistent. Figure 2/3 heatmap cell text too small for print. Figure 1 caption ~60 words, too dense.\"}\n  action_items:\n    - {round: 12, action: \"Fix Figure 1 Y-axis label to 'Δ Accuracy (percentage points)'\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"AUDIT-1\"\n  summary: \"Figure 1 missing from PDF\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - {round: 8, reviewers: \"audit\", note: \"Figure 1 does not exist.\"}\n    - {round: 9, reviewers: \"\", note: \"Figure 1 present on page 2.\"}\n    - {round: 12, reviewers: \"visual\", note: \"Confirmed present on page 2.\"}\n    - {round: 13, reviewers: \"visual\", note: \"Confirmed present on page 2.\"}\n  resolution: \"Figure 1 present in Introduction.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy based on ad-hoc Algorithm 1 — lacks parametric DR modeling\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Pharmacology has parametric DR models.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Appendix W: parametric DR comparison added.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。Parametric comparison exists.\"}\n  resolution: \"Appendix W: Parametric DR Model Comparison added.\"\n  resolution_round: 9\n\n- id: \"R9-N2\"\n  summary: \"'Architecture determines vulnerability' causal claim exceeds evidence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Replace with 'family-level factors'.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未直接提及。\"}\n  resolution: \"All causal claims replaced. Confounders listed.\"\n  resolution_round: 9\n\n- id: \"R9-S1\"\n  summary: \"Unified LoRA r=16 unequal treatment strength across scales\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Parameter fraction 0.45% (Phi-4) to 2.10%.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Phi-4 vs Qwen-14B counter-argument has merit.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"DIVERGENT. R1 maintains concern; R2 considers largely addressed by same-scale comparison.\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未直接提及。Limitations discussion exists.\"}\n  action_items:\n    - {round: 9, action: \"Discuss LoRA confound in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 10, action: \"Report trainable parameter percentages\", assigned_to: \"paper_agent\", status: \"done\"}\n\n- id: \"R9-S2\"\n  summary: \"'65-70% MMLU baseline vulnerability band' over-precise for N=6\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Qualify with 'in our five-family sample'.\"}\n    - {round: 10, reviewers: \"\", note: \"All claims qualified. Resolved.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Reopened. Band = 2 Qwen models only. LLaMA contradicts.\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未直接提及。Discussion §6 mentions 65-70% with LLaMA-3.1 contradiction acknowledged.\"}\n  action_items:\n    - {round: 12, action: \"Remove 65-70% from Abstract/Intro; downgrade to Discussion observational association\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R9-S3\"\n  summary: \"Calibration baseline missing IRT variants\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"2PL vs 2PL+γ ablation would be better.\"}\n    - {round: 12, reviewers: \"\", note: \"本轮未提及。\"}\n    - {round: 13, reviewers: \"\", note: \"本轮未提及。\"}\n  action_items:\n    - {round: 9, action: \"Add 2PL vs 2PL+γ ablation\", assigned_to: \"paper_agent\", status: \"open\"}\n\n- id: \"R10-N1\"\n  summary: \"ContamCal calibration MAE (0.009) worse than raw accuracy (0.006)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R2\", note: \"Core method underperforms 'do nothing' baseline.\"}\n    - {round: 10, reviewers: \"R1\", note: \"REBUT: §3.3 predicts this; γ serves diagnosis.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Reposition as diagnostic framework, not calibration tool.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Critical (strongest consensus). MMLU MAE=0.009>0.006, ARC MAE=0.020>0.007. Method name 'ContamCal' promises calibration but delivers worse-than-baseline results. 'Value lies in diagnosis' defense itself problematic—if observed dosages produce small effects, framework's practical utility is questionable. R1 notes IRT provides credible intervals and item-level modeling unavailable from raw accuracy, but concedes γ unreliability (N3) undermines these incremental benefits.\"}\n  action_items:\n    - {round: 10, action: \"Clarify ContamCal value is diagnostic not calibration\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Reposition ContamCal as diagnostic framework in Abstract/Intro; contextualize Table 3 MAE\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Rewrite §5.5 from 'Calibration Quality' to 'Diagnostic Utility'; lead with domain-level γ_d vs raw accuracy contrast (Social Sciences γ_d=-0.63 vs pooled non-significant); contextualize aggregate MAE as non-target\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R10-W1\"\n  summary: \"γ parameterization outside a_i bracket unjustified\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Non-uniform vs uniform DIF.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Notation improved. Substantive question unanswered.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Both recommend Appendix comparison (PPP, WAIC).\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"DIVERGENT→RESOLVED. R2 rebuts R1: ΔELPD≈0 actually supports author's choice (neither better). R1 accepts. Consensus: state choice is interpretive convenience (ΔELPD≈0), not statistical evidence.\"}\n  action_items:\n    - {round: 10, action: \"Justify γ outside a_i or compare with inside-a_i form\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 12, action: \"Run uniform vs non-uniform DIF comparison (PPP/WAIC) if time permits\", assigned_to: \"main_agent\", status: \"open\"}\n    - {round: 13, action: \"Add one sentence in §3.2 noting ΔELPD≈0 and choice is for interpretive convenience\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R10-W2\"\n  summary: \"300/14042 MMLU item subset — selection bias toward high-exposure-variance items\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. 2.1% of items selected.\"}\n    - {round: 11, reviewers: \"R1\", note: \"High exposure variance items may be systematically different.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Report subset distribution comparison. Attempt full-item or larger subset IRT.\"}\n    - {round: 13, reviewers: \"R1\", note: \"Minor. KS/χ² tests in §5.5 confirm representativeness (p=0.946/0.574). But exposure variance bias untested—should mention in limitations.\"}\n  action_items:\n    - {round: 12, action: \"Compute 300 vs 14042 difficulty/domain distribution comparison + KS test\", assigned_to: \"main_agent\", status: \"in_progress\"}\n\n- id: \"R11-N1\"\n  summary: \"Abstract/Title overclaiming — 'Not All Models Are Inflated' exceeds evidence from 6 models ≤14B under SFT\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Critical. Three overclaim dimensions.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Strongly reinforced. Title implies generality for N=6 SFT study.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. Title scope exceeds evidence: 6 models ≤14.7B, all SFT, all open-source. R1 cross-response: claim defensible if scoped to 'SFT-stage + 7B-14B + diverse families', but current wording lacks qualification. Schaeffer et al. (2025) and Bordt et al. (2025) performed controlled injection at smaller scale.\"}\n  action_items:\n    - {round: 11, action: \"Add scope qualifier to title; soften Abstract language\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Strengthen scope qualification in Abstract; keep title but soften surrounding language\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Abstract first sentence must scope: 6 models, 7-14B, 5 open-source families, SFT injection\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R11-W1\"\n  summary: \"DiD parallel trends assumption untested\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"No pre-treatment trend comparison.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"DIVERGENT. R2 rebuts: controlled experiment, pre-treatment balance strong (Cohen's d=0.02).\"}\n  action_items:\n    - {round: 11, action: \"Report pre-treatment balance; add parallel trends discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Pre-treatment balance reported (Cohen's d=0.02, p>0.19). Controlled experiment design largely mitigates concern.\"\n  resolution_round: 12\n\n- id: \"R11-W2\"\n  summary: \"'Contamination' vs 'additional training' conceptual tension\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"CONSENSUS Major. DiD null + augmentation confound.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"Should-Fix. Volume control 45%/55% clarifies but terminology needs precision.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. SFT injection = content exposure + extra volume + LoRA updates. Table 1 labels conflate all three as 'contamination response'. Volume control shows 45% is volume. §6 Discussion paragraph exists but insufficient. Cross-response: R2 concept concern + R1 method concern converge to challenge core narrative framing.\"}\n  action_items:\n    - {round: 11, action: \"Distinguish contamination-specific from general training effects\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 12, action: \"Add Discussion paragraph defining contamination vs additional training in this framework\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n    - {round: 13, action: \"Expand Discussion paragraph: triple confound (content/volume/LoRA), surface 45%/55% Falcon3 split prominently, Limitations caveat on single-family control\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R11-W3\"\n  summary: \"2PL+γ identifiability — θ and γ·e collinearity with b\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R2,R1\", note: \"Potential collinearity if e_ij correlates with b_j.\"}\n    - {round: 12, reviewers: \"\", note: \"§3.3 includes identifiability discussion: |r|<0.13, R²<0.014.\"}\n  action_items:\n    - {round: 11, action: \"Expand identifiability discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"§3.3 reports e_ij and b_i near-orthogonal (|r|<0.13, R²<0.014).\"\n  resolution_round: 12\n\n- id: \"R11-M1\"\n  summary: \"Benchmark diversity insufficient — MMLU dominates\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - {round: 11, reviewers: \"R2\", note: \"Only 3 benchmarks, MMLU dominates.\"}\n    - {round: 12, reviewers: \"R1,R2\", note: \"DIVERGENT. R1 rebuts: 3 formats comprehensive. Both agree MMLU-driven but acceptable.\"}\n  action_items:\n    - {round: 11, action: \"Scope cross-benchmark conclusions\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"3 benchmarks across 3 formats accepted. MMLU dominance acknowledged. Not re-raised as must-fix.\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"Algorithm 1 Benefit sub-branches both return same label — dead code\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: \"R1,R2\", note: \"Lines 91-94 both return BENEFIT. Remove dead logic or add sub-labels.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"Re-confirmed. Two branches (saturating/sustained gain) both return BENEFIT. Either design remnant or intentional merge—either way, remove redundant branching.\"}\n  action_items:\n    - {round: 12, action: \"Remove unused branching logic in Algorithm 1\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R12-M2\"\n  summary: \"Stage 1→Stage 2 uncertainty propagation missing — e_ij is point estimate\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: \"R1\", note: \"RRF is rank-based non-parametric. Uncertainty propagation non-trivial.\"}\n    - {round: 13, reviewers: \"R1,R2\", note: \"CONSENSUS Should-Fix. e_ij from RRF enters IRT as fixed covariate. Exposure measurement error → γ CI underestimated. Especially severe at J=16 where uncertainty is already large. May partly explain γ instability (R4-N1).\"}\n  action_items:\n    - {round: 12, action: \"Acknowledge e_ij point estimate limitation; mention as future work\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R13-W1\"\n  summary: \"DiD MDES 1.2-2.0pp practical significance boundary undiscussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: \"R1\", note: \"MDES 1.2-2.0pp rules out effects >2pp but 1pp item-specific effects may matter in high-stakes evaluation. Paper does not discuss practical significance threshold.\"}\n  action_items:\n    - {round: 13, action: \"Discuss MDES practical significance in context of real-world contamination scenarios\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R13-m5\"\n  summary: \"Table 1 'Stab.' column definition unclear\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: \"R1,R2\", note: \"Stab. column in Table 1 not defined in caption or footnote.\"}\n  action_items:\n    - {round: 13, action: \"Add footnote defining Stab. column in Table 1\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n\n- id: \"R13-m6\"\n  summary: \"ρ=0.3 saturation ratio source not cited\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: \"R1\", note: \"ρ=0.3 saturation ratio used in Algorithm 1 without source.\"}\n  action_items:\n    - {round: 13, action: \"Add source or justification for ρ=0.3\", assigned_to: \"paper_agent\", status: \"in_progress\"}"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-25T21:47:52.761650+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml\", \"bytes\": 42781}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 166575
}
```

</details>

---


### Tool call

_source line 1298 · 2026-05-25T21:47:55.674647+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 13 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR) | **模式**: Fresh review | **Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性) | **交叉回应**: 已完成，已收敛\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个结合多信号污染检测与污染增强 IRT（Item Response Theory）的诊断框架，用于研究 benchmark 污染在不同模型家族间的剂量-响应模式。通过对 5 个开源家族的 6 个模型（7B–14.7B）进行 5 个剂量水平的受控 SFT 注入实验，论文识别出 4 种剂量-响应模式（Immune、Benefit、Collapse、V-Recovery），其中前两种在独立家族间可复现，后两种仅在 Qwen2.5 中观察到。论文还报告了跨 benchmark 传递效应、DiD 无 item 级记忆化结果、以及 volume 控制实验显示 45% 的 Benefit 效应来自数据量而非污染内容。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的研究问题。** 此前研究将污染效应视为均匀膨胀，本文首次在生产级规模（7B–14B）对多个独立模型家族进行受控剂量-响应分析，填补了文献中的实质性空白。\n\n**S2. 跨家族受控实验设计。** 5 个家族（Phi-4、LLaMA-3.1、Gemma-2、OLMo-2、Falcon3）+ Qwen2.5（两个规模），覆盖了不同架构和训练流程，是目前最全面的受控污染实验。\n\n**S3. 多信号暴露映射。** RRF 融合 4 个污染检测信号为连续 per-item 暴露分数，解决了二元污染标签的局限性，工程贡献合理。\n\n**S4. 负面结果的诚实报告。** 论文坦诚报告了 ContamCal MAE 劣于 raw accuracy、DiD 未检测到 item 级记忆化、以及 volume 控制显示 45% 来自数据量。这种透明度值得肯定。\n\n**S5. 广泛的鲁棒性分析。** 附录包含 prior sensitivity、DGP simulation、profile stability、parametric DR 比较、identifiability 分析、KS 检验等，展示了对方法论假设的严谨审视。\n\n**S6. 实际意义。** \"并非所有模型都被污染膨胀\"的发现对 benchmark leaderboard 解读有直接影响。\n\n---\n\n## Weaknesses\n\n### Must-Fix（6 项）\n\n**W1. Volume confound 控制不足——威胁核心叙事 [R6-W1 + R11-W2, CONSENSUS Critical]**\n\nSFT 注入协议同时引入 (i) 污染内容、(ii) 额外训练数据量、(iii) LoRA 参数更新。Falcon3-7B 的 volume 控制实验揭示 45% 的 Benefit 来自数据量。但此控制仅覆盖 6 个模型中的 1 个。Collapse 模式（Qwen2.5-14B, −25pp at d100）完全没有 volume 控制——来自额外训练的灾难性遗忘是未被反驳的替代解释。这意味着 \"dose-response\" 的 x 轴不是纯粹的污染内容轴，而是污染 + 数据量 + LoRA 的混合轴，削弱了论文关于模型家族展现不同\"污染\"响应的核心主张。\n\n**交叉回应共识**：这是本轮两位 Reviewer 最强的共识点。R1 从方法角度（单一家族控制不足）、R2 从概念角度（\"Benefit\" 归类为污染响应在概念上可能有误）分别指向同一问题，合并后构成论文最需要回应的挑战。\n\n**W2. RRF pipeline 完整性——S2 信号主动有害 [R2-W1, CONSENSUS Critical]**\n\n移除 S2（AUC ≈ 0.48–0.51，接近随机）后，ρ_dose 从 0.049 提升到 0.471（~10× 改善）。尽管有此证据，主分析仍保留 S2。item 级 ρ ≈ 0.773 的辩护不能抵消 model 级的伤害。论文至少应报告去除 S2 后的完整 pipeline 结果，验证下游 γ 估计和剂量-响应 profile 是否被扭曲。\n\n**W3. ContamCal 劣于 raw accuracy baseline [R10-N1, CONSENSUS Critical]**\n\nMMLU MAE = 0.009 vs raw accuracy MAE = 0.006; ARC MAE = 0.020 vs 0.007。名为 \"ContamCal\"（校准）的框架产出了比 \"什么都不做\" 更差的校准结果。\"价值在于诊断\"的辩护本身成问题：如果观察到的剂量产生的效应小到 raw accuracy 已能捕捉群体模式，框架的实际效用存疑。IRT 提供的 credible intervals 和 item 级建模虽是 raw accuracy 不具备的，但 γ 在 J=16 下的不可靠性（W5）削弱了这些增量收益。\n\n**W4. 剂量-响应分类体系证据不足 [R8-N3, CONSENSUS Critical]**\n\n4 个分类来自 5 个家族。Collapse 和 V-Recovery 各仅在 1 个家族（均为 Qwen2.5 不同规模）中观察到——同一家族的不同规模不构成独立复现。更严峻的是，即使在 \"已复现\" 的模式中，Benefit 的统计基础也很薄弱：AICc 分析显示 Gemma-2 和 OLMo-2 的剂量-响应曲线与常数在统计上不可区分。仅 Immune（Phi-4）在跨 seed 下统计稳健。分类体系必须重构为 2 confirmed + 2 preliminary。\n\n**W5. Domain-level γ 在 J=16 下不可靠 [R4-N1, CONSENSUS Critical]**\n\nγ 后验均值在不同先验下偏移 2.6×（0.34 → 0.89），表明数据（每域 J=16 items）不足以压制先验。论文在 Appendix M 中承认了这一点但未在正文中讨论。Abstract 中 \"enables within-family domain-level contamination diagnosis with credible intervals\" 的声明在当前证据下不成立。域级分析（Social Sciences 负面、STEM 正面）应被显式标记为先验敏感且探索性的。\n\n**W6. ARC IRT 结果结构性无效 [R3-N3, CONSENSUS Critical]**\n\nARC 后验预测 p 值（PPP）= 0.003，表明 2PL+γ 模型对 ARC 数据存在严重结构性失配。尽管如此，ARC IRT 结果仍出现在正文 §5.2（跨 benchmark 传递分析）中。使用来自明显不拟合模型的 IRT 估计值具有误导性。正文中的 ARC 结论应完全基于 raw accuracy，IRT 结果移至附录并附适当警告。\n\n### Should-Fix（8 项）\n\n**W7. Abstract/Title 范围超出证据 [R11-N1, CONSENSUS Should-Fix]**\n\n\"Not All Models Are Inflated\" 和 \"Across Model Families\" 暗示广泛适用性，但研究仅覆盖 ≤14.7B 的 6 个开源模型在 SFT 下的表现。Abstract 首句 \"has never been measured across model families\" 过度声明——Schaeffer et al. (2025) 在更小规模进行了受控预训练注入，Bordt et al. (2025) 扩展到 1.6B。如果显式限定为 \"SFT-stage injection at 7B–14B scale across five independent open-source families\"，claim 可以成立。\n\n**W8. n=3 seeds 统计不充分 [R8-N1, CONSENSUS Should-Fix]**\n\nBCa bootstrap with n=3 seeds 的 resample 空间极小。OLMo-2 的 CI 跨越零。AICc 显示 Gemma-2 和 OLMo-2 与常数不可区分。仅 Immune (Phi-4) 在跨 seed 下统计稳健。跨 seed 稳定性声明应大幅弱化。\n\n**W9. Stage 1→2 不确定性传播缺失 [R12-M2, CONSENSUS Should-Fix]**\n\nRRF 暴露分数 (e_ij) 作为固定协变量进入 IRT 模型。Stage 1 的暴露测量误差导致 Stage 2 的 γ credible interval 被低估。在 J=16 下尤为严重，可能部分解释 γ 不稳定性（W5）。最低要求：在 Limitations 中承认并讨论对 γ CI 解释的影响。\n\n**W10. Han et al. (2026) 和 Schaeffer et al. (2025) 区分不足 [R8-N4 + R2-W8]**\n\n与 Han et al. 的方法论区分（group-level binary DIF vs. continuous exposure covariate）在方法层面足够，但缺少经验对比。Schaeffer et al. 在 §2 的讨论不充分——他们的统计功效分析与本文的 n=3 seed 局限高度相关，应予讨论。\n\n**W11. Algorithm 1 是描述性启发式，非方法贡献 [R8-W3, CONSENSUS Should-Fix]**\n\nAlgorithm 1 的阈值（τ=2pp, σ=5, ρ=0.3）缺乏理论基础。Appendix U 的 sensitivity sweep 有帮助但不改变其本质。应显式定位为\"实验结果的组织框架\"而非与 IRT 模型并列的方法论贡献。\n\n**W12. Abstract 数字密度过高 [R4-W6, CONSENSUS Should-Fix]**\n\nAbstract 在 ~193 词中包含 20+ 个数字。核心洞见（模型对污染的响应不同，并非都被膨胀）被定量细节淹没。减少到 8–10 个关键数字，以概念发现引领。\n\n**W13. Bayesian/频率主义术语混用 [R8-W1, DIVERGENT→RESOLVED]**\n\n论文同时使用 \"credible intervals\"（Bayesian IRT）和 \"confidence intervals\"（bootstrap）以及 \"significant\"。在首次出现时标注 CI 类型：credible interval（来自 Bayesian IRT）vs. confidence interval（来自 bootstrap）。\n\n**W14. SFT 生态效度警告不足 [R2-W6, Should-Fix]**\n\nSFT 注入同时引入内容暴露、额外训练信号和 LoRA 更新。现实中的污染发生在预训练阶段。Limitations 应明确讨论 SFT 特异性发现能否推广到预训练污染。\n\n### Minor（5 项）\n\n**M1.** Algorithm 1 dead code：Lines 91–94 两个分支（saturating/sustained gain）均返回 BENEFIT。删除冗余或添加子标签。\n\n**M2.** Table 1 'Stab.' 列未在 caption 或脚注中定义。\n\n**M3.** ρ=0.3 saturation ratio 在 Algorithm 1 中使用但未引用来源。\n\n**M4.** Figure 1 图例文字 ~6–7pt，低剂量区域多条线重叠，打印尺寸下难以辨识。\n\n**M5.** Table 2 MAE 精度不一致（混合 3 位和 4 位小数）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **Volume confound 是论文最关键的弱点**（W1）。R1 从方法/实验角度（单一家族控制）、R2 从概念角度（\"污染剂量-响应\"概念在 45% 为数据量时的有效性）独立识别，合并后挑战核心叙事。\n\n2. **ContamCal 劣于 baseline 是根本性问题**（W3）。两者一致认为\"诊断价值\"辩护在 γ 不可靠的情况下不充分。\n\n3. **分类体系需重构为 2+2**（W4）。Collapse/V-Recovery 应显式标为 Qwen2.5 特异的初步观察。\n\n4. **Domain-level γ claims 必须降级**（W5）。R1 从统计理论（J=16 < J≥50 minimum）、R2 从经验证据（仅 Qwen2.5 显示显著域异质性）共同得出 Abstract claim 不成立。\n\n5. **ARC IRT 结果应退出正文**（W6）。PPP=0.003 使 IRT 估计不可靠。\n\n6. **RRF S2 信号必须处理**（W2）。移除后 10× 改善不可忽视。\n\n7. **Abstract 需限定范围**（W7）。两者一致认为需要 SFT-stage 限定。\n\n---\n\n## Reviewer Divergence\n\n**技术新颖性定位 [R3-N7]：**\n\n- **Reviewer 2** 认为 2PL+γ 是标准 explanatory IRT/DIF 方法论，贡献主要是应用框架而非方法创新。各组件（Min-K%++、RRF、explanatory IRT、threshold classification）均为标准方法。\n- **Reviewer 1** 部分反驳：training-free contamination signals → RRF fusion → continuous per-item exposure → IRT covariate structure → credible intervals 的完整技术路径此前不存在。γ 的参数化选择（outside vs inside a_i bracket）是有理论含义的非 trivial 设计决策。将方法论贡献降级为 \"merely application\" 低估了应用层面的创新。\n- **共识落点**：论文需要更清晰的定位声明，显式承认 2PL+γ 是标准 explanatory IRT，同时阐明将其应用于 LLM 污染检测（连续暴露协变量）的具体创新之处。当前表述模糊了这一区分。\n\n---\n\n## Questions for Authors\n\n**Q1.** Volume 控制何时能推广到至少一个非 Benefit 家族（如 Collapse 模式的 Qwen2.5-14B）？没有这个控制，剂量-响应分类混淆了污染与数据量效应。\n\n**Q2.** 移除 S2 后 γ 估计和剂量-响应 profile 如何变化？10× ρ_dose 改善暗示下游有实质影响。\n\n**Q3.** Full fine-tuning 是否会产生不同的剂量-响应模式？LoRA 的低秩约束（r=16）可能抑制记忆化效应，使 Benefit 模式可能是 LoRA 特有的 artifact。\n\n**Q4.** 鉴于 γ 在 J=16 下对先验的 2.6× 敏感性，读者应如何解读具体 γ 值（如 Social Sciences γ_d=−0.63）？符号是否稳健即使数值不稳定？\n\n**Q5.** 跨 benchmark 传递有多少是 SFT 引入的指令跟随能力提升，而非真正的污染传播？GSM8K 的 volume 控制显示 53% volume 贡献，支持此替代解释。\n\n**Q6.** 如果框架的价值是诊断而非校准，是否应重命名？当前名称创造了论文无法满足的期望。\n\n---\n\n## Missing References\n\n- **Hill (1910)** — dose-response 是论文标题概念和核心框架。奠基性文献仅出现在 Appendix AB，必须在正文（§1 或 §3）中引用。\n- **Deng et al. (2024)** — 引用为 arXiv 但可能已发表于 NAACL 2024，需验证并更新引用元数据。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未派发外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（耗时 ~4 分钟）。\n\n10 项发现，均为 info 级别（0 critical, 0 warning）：\n\n- **Figure 1 (p.1)**：图例文字 ~6–7pt，低剂量区多条曲线重叠。建议加大 marker 差异。\n- **Table 1 (p.2)**：8+ 列，紧凑但未溢出。booktabs 格式正确。\n- **Table 2 (p.5)**：MAE 精度不一致（3 vs 4 位小数）。\n- **Section 5 heading (p.6)**：出现在左栏底部 ~1/4 处，勉强可接受。\n- **Page 7**：密度很高（Table 4 + Figure 5 + 5 个 subsection），不影响可读性。\n- **Figure 6 (p.8)**：Per-domain CI 图清晰。Limitations ~1 段，EMNLP 合规。\n- **Figure 2 (p.3)**：全文最佳 display item——pipeline 架构图，三阶段颜色区分明确。\n- **Appendix (p.13, p.17)**：多面板子图 axis label ~6pt，附录可接受。\n- **Algorithm 1 (p.18)**：排版规范。\n\n**未检测到格式违规。** 8 页正文确认，EMNLP 2026 合规。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n\n**Confidence: 4/5 (High)**\n\n本文探讨了一个重要问题——不同模型家族如何响应 benchmark 污染——并在生产级规模进行了精心设计的受控实验。核心经验发现（污染不均匀膨胀分数、剂量-响应模式因家族而异）对社区有真正的信息价值。\n\n但论文面临三个相互关联的问题，阻碍了主会议推荐：\n\n1. **方法论框架（ContamCal）未兑现承诺。** 校准性能劣于 raw accuracy，域级估计对先验敏感且在 J=16 下不可靠，核心信号组件之一（S2）主动损害 pipeline 性能。IRT 诊断是论文声称的方法论贡献，但当前状态下其可靠性不如它声称要改进的 baseline。\n\n2. **剂量-响应叙事被混淆。** 45% 的 Benefit 来自数据量，Collapse 可能由额外训练的灾难性遗忘解释，且仅一个家族有 volume 控制。论文无法自信地将剂量-响应模式归因于污染特异性效应。核心主张可能从\"模型对*污染*的响应不同\"变为\"模型对*内容重叠不同的额外 SFT 训练*的响应不同\"。\n\n3. **分类体系从不充分的证据过度泛化。** 四个类别来自五个家族，其中两个类别各基于一个家族（均为 Qwen2.5），两个 \"已复现\" 类别的统计支持从稳健（Immune/Phi-4）到边界（Benefit/OLMo-2）到统计不可区分（Benefit/Gemma-2 on AICc）。\n\n这些问题单独看是实质性的，合并后相互强化：volume confound (1) 削弱 taxonomy (3)，而 IRT 框架的不可靠性 (2) 削弱了本可帮助解纠缠混淆因素的域级诊断。鉴于真正的经验贡献，Findings 级别发表是合适的，但主会议接收需要解决 volume 控制缺口、pipeline 完整性和框架重新定位。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 首句需显式限定范围：\"across *five open-source* model families *at 7B–14B scale under SFT injection*\"\n- \"enables within-family domain-level contamination diagnosis with credible intervals\" 在 J=16 下不成立，替换为限定性语言或删除\n- 20+ 数字减至 8–10，以概念发现引领\n- 字数 ~193，在 EMNLP 2026 的 200 词限制内\n\n### Section 1 (Introduction)\n- 引入 dose-response 概念时引用 Hill (1910)\n- 将 claims 限定至 SFT injection at 7B–14B\n\n### Section 2 (Related Work)\n- 扩展 Schaeffer et al. (2025) 讨论——其统计功效分析直接相关于 n=3 seed 局限\n- Han et al. (2026) 方法层面区分足够；考虑增加 1–2 句经验对比范围\n\n### Section 3 (Method)\n- §3.2：增加一句说明 ΔELPD ≈ 0（γ outside vs inside a_i），选择基于解释便利性\n- §3.3：承认 e_ij 点估计限制及对 γ CI 宽度的影响\n- §3.4：显式声明 Algorithm 1 是描述性启发式，非方法贡献\n\n### Section 4 (Experimental Setup)\n- 报告 volume 控制设计理由和局限（仅测试 Falcon3）\n\n### Section 5 (Results)\n- §5.1：重构为 2 confirmed (Immune, Benefit) + 2 preliminary (Collapse, V-Recovery)，增加 AICc 证据\n- §5.2：ARC 跨 benchmark 结论必须基于 raw accuracy 而非 IRT，增加显式声明\n- §5.5：从 \"Calibration Quality\" 改写为 \"Diagnostic Utility\"，以域级 γ_d 对比引领，将聚合 MAE 定位为非目标指标\n- 域级 γ 讨论处：在正文（非仅附录）中增加 prior sensitivity 警告\n\n### Section 6 (Discussion)\n- 增加段落讨论 triple confound (content/volume/LoRA)\n- 更显著地呈现 Falcon3 45%/55% 分解\n- 删除或限定 \"65–70% baseline vulnerability band\"（基于 2 个 Qwen 模型，被 LLaMA 反例推翻）\n\n### Limitations\n- 承认：(a) 单一家族 volume 控制，(b) SFT 特异性发现可能不推广到预训练污染，(c) 暴露测量不确定性未传播到 γ CI\n\n### 格式\n- 首次出现时标注 CI 类型：\"credible interval (from Bayesian IRT)\" vs \"confidence interval (from bootstrap)\"\n- Table 1：定义 'Stab.' 列\n- Algorithm 1：删除 dead branching (lines 91–94)\n- Figure 1：增大图例字号，区分 markers",
  "project": "contamcal-irt-calibration",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 13 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR) | **模式**: Fresh review | **Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性) | **交叉回应**: 已完成，已收敛\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个结合多信号污染检测与污染增强 IRT（Item Response Theory）的诊断框架，用于研究 benchmark 污染在不同模型家族间的剂量-响应模式。通过对 5 个开源家族的 6 个模型（7B–14.7B）进行 5 个剂量水平的受控 SFT 注入实验，论文识别出 4 种剂量-响应模式（Immune、Benefit、Collapse、V-Recovery），其中前两种在独立家族间可复现，后两种仅在 Qwen2.5 中观察到。论文还报告了跨 benchmark 传递效应、DiD 无 item 级记忆化结果、以及 volume 控制实验显示 45% 的 Benefit 效应来自数据量而非污染内容。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的研究问题。** 此前研究将污染效应视为均匀膨胀，本文首次在生产级规模（7B–14B）对多个独立模型家族进行受控剂量-响应分析，填补了文献中的实质性空白。\n\n**S2. 跨家族受控实验设计。** 5 个家族（Phi-4、LLaMA-3.1、Gemma-2、OLMo-2、Falcon3）+ Qwen2.5（两个规模），覆盖了不同架构和训练流程，是目前最全面的受控污染实验。\n\n**S3. 多信号暴露映射。** RRF 融合 4 个污染检测信号为连续 per-item 暴露分数，解决了二元污染标签的局限性，工程贡献合理。\n\n**S4. 负面结果的诚实报告。** 论文坦诚报告了 ContamCal MAE 劣于 raw accuracy、DiD 未检测到 item 级记忆化、以及 volume 控制显示 45% 来自数据量。这种透明度值得肯定。\n\n**S5. 广泛的鲁棒性分析。** 附录包含 prior sensitivity、DGP simulation、profile stability、parametric DR 比较、identifiability 分析、KS 检验等，展示了对方法论假设的严谨审视。\n\n**S6. 实际意义。** \"并非所有模型都被污染膨胀\"的发现对 benchmark leaderboard 解读有直接影响。\n\n---\n\n## Weaknesses\n\n### Must-Fix（6 项）\n\n**W1. Volume confound 控制不足——威胁核心叙事 [R6-W1 + R11-W2, CONSENSUS Critical]**\n\nSFT 注入协议同时引入 (i) 污染内容、(ii) 额外训练数据量、(iii) LoRA 参数更新。Falcon3-7B 的 volume 控制实验揭示 45% 的 Benefit 来自数据量。但此控制仅覆盖 6 个模型中的 1 个。Collapse 模式（Qwen2.5-14B, −25pp at d100）完全没有 volume 控制——来自额外训练的灾难性遗忘是未被反驳的替代解释。这意味着 \"dose-response\" 的 x 轴不是纯粹的污染内容轴，而是污染 + 数据量 + LoRA 的混合轴，削弱了论文关于模型家族展现不同\"污染\"响应的核心主张。\n\n**交叉回应共识**：这是本轮两位 Reviewer 最强的共识点。R1 从方法角度（单一家族控制不足）、R2 从概念角度（\"Benefit\" 归类为污染响应在概念上可能有误）分别指向同一问题，合并后构成论文最需要回应的挑战。\n\n**W2. RRF pipeline 完整性——S2 信号主动有害 [R2-W1, CONSENSUS Critical]**\n\n移除 S2（AUC ≈ 0.48–0.51，接近随机）后，ρ_dose 从 0.049 提升到 0.471（~10× 改善）。尽管有此证据，主分析仍保留 S2。item 级 ρ ≈ 0.773 的辩护不能抵消 model 级的伤害。论文至少应报告去除 S2 后的完整 pipeline 结果，验证下游 γ 估计和剂量-响应 profile 是否被扭曲。\n\n**W3. ContamCal 劣于 raw accuracy baseline [R10-N1, CONSENSUS Critical]**\n\nMMLU MAE = 0.009 vs raw accuracy MAE = 0.006; ARC MAE = 0.020 vs 0.007。名为 \"ContamCal\"（校准）的框架产出了比 \"什么都不做\" 更差的校准结果。\"价值在于诊断\"的辩护本身成问题：如果观察到的剂量产生的效应小到 raw accuracy 已能捕捉群体模式，框架的实际效用存疑。IRT 提供的 credible intervals 和 item 级建模虽是 raw accuracy 不具备的，但 γ 在 J=16 下的不可靠性（W5）削弱了这些增量收益。\n\n**W4. 剂量-响应分类体系证据不足 [R8-N3, CONSENSUS Critical]**\n\n4 个分类来自 5 个家族。Collapse 和 V-Recovery 各仅在 1 个家族（均为 Qwen2.5 不同规模）中观察到——同一家族的不同规模不构成独立复现。更严峻的是，即使在 \"已复现\" 的模式中，Benefit 的统计基础也很薄弱：AICc 分析显示 Gemma-2 和 OLMo-2 的剂量-响应曲线与常数在统计上不可区分。仅 Immune（Phi-4）在跨 seed 下统计稳健。分类体系必须重构为 2 confirmed + 2 preliminary。\n\n**W5. Domain-level γ 在 J=16 下不可靠 [R4-N1, CONSENSUS Critical]**\n\nγ 后验均值在不同先验下偏移 2.6×（0.34 → 0.89），表明数据（每域 J=16 items）不足以压制先验。论文在 Appendix M 中承认了这一点但未在正文中讨论。Abstract 中 \"enables within-family domain-level contamination diagnosis with credible intervals\" 的声明在当前证据下不成立。域级分析（Social Sciences 负面、STEM 正面）应被显式标记为先验敏感且探索性的。\n\n**W6. ARC IRT 结果结构性无效 [R3-N3, CONSENSUS Critical]**\n\nARC 后验预测 p 值（PPP）= 0.003，表明 2PL+γ 模型对 ARC 数据存在严重结构性失配。尽管如此，ARC IRT 结果仍出现在正文 §5.2（跨 benchmark 传递分析）中。使用来自明显不拟合模型的 IRT 估计值具有误导性。正文中的 ARC 结论应完全基于 raw accuracy，IRT 结果移至附录并附适当警告。\n\n### Should-Fix（8 项）\n\n**W7. Abstract/Title 范围超出证据 [R11-N1, CONSENSUS Should-Fix]**\n\n\"Not All Models Are Inflated\" 和 \"Across Model Families\" 暗示广泛适用性，但研究仅覆盖 ≤14.7B 的 6 个开源模型在 SFT 下的表现。Abstract 首句 \"has never been measured across model families\" 过度声明——Schaeffer et al. (2025) 在更小规模进行了受控预训练注入，Bordt et al. (2025) 扩展到 1.6B。如果显式限定为 \"SFT-stage injection at 7B–14B scale across five independent open-source families\"，claim 可以成立。\n\n**W8. n=3 seeds 统计不充分 [R8-N1, CONSENSUS Should-Fix]**\n\nBCa bootstrap with n=3 seeds 的 resample 空间极小。OLMo-2 的 CI 跨越零。AICc 显示 Gemma-2 和 OLMo-2 与常数不可区分。仅 Immune (Phi-4) 在跨 seed 下统计稳健。跨 seed 稳定性声明应大幅弱化。\n\n**W9. Stage 1→2 不确定性传播缺失 [R12-M2, CONSENSUS Should-Fix]**\n\nRRF 暴露分数 (e_ij) 作为固定协变量进入 IRT 模型。Stage 1 的暴露测量误差导致 Stage 2 的 γ credible interval 被低估。在 J=16 下尤为严重，可能部分解释 γ 不稳定性（W5）。最低要求：在 Limitations 中承认并讨论对 γ CI 解释的影响。\n\n**W10. Han et al. (2026) 和 Schaeffer et al. (2025) 区分不足 [R8-N4 + R2-W8]**\n\n与 Han et al. 的方法论区分（group-level binary DIF vs. continuous exposure covariate）在方法层面足够，但缺少经验对比。Schaeffer et al. 在 §2 的讨论不充分——他们的统计功效分析与本文的 n=3 seed 局限高度相关，应予讨论。\n\n**W11. Algorithm 1 是描述性启发式，非方法贡献 [R8-W3, CONSENSUS Should-Fix]**\n\nAlgorithm 1 的阈值（τ=2pp, σ=5, ρ=0.3）缺乏理论基础。Appendix U 的 sensitivity sweep 有帮助但不改变其本质。应显式定位为\"实验结果的组织框架\"而非与 IRT 模型并列的方法论贡献。\n\n**W12. Abstract 数字密度过高 [R4-W6, CONSENSUS Should-Fix]**\n\nAbstract 在 ~193 词中包含 20+ 个数字。核心洞见（模型对污染的响应不同，并非都被膨胀）被定量细节淹没。减少到 8–10 个关键数字，以概念发现引领。\n\n**W13. Bayesian/频率主义术语混用 [R8-W1, DIVERGENT→RESOLVED]**\n\n论文同时使用 \"credible intervals\"（Bayesian IRT）和 \"confidence intervals\"（bootstrap）以及 \"significant\"。在首次出现时标注 CI 类型：credible interval（来自 Bayesian IRT）vs. confidence interval（来自 bootstrap）。\n\n**W14. SFT 生态效度警告不足 [R2-W6, Should-Fix]**\n\nSFT 注入同时引入内容暴露、额外训练信号和 LoRA 更新。现实中的污染发生在预训练阶段。Limitations 应明确讨论 SFT 特异性发现能否推广到预训练污染。\n\n### Minor（5 项）\n\n**M1.** Algorithm 1 dead code：Lines 91–94 两个分支（saturating/sustained gain）均返回 BENEFIT。删除冗余或添加子标签。\n\n**M2.** Table 1 'Stab.' 列未在 caption 或脚注中定义。\n\n**M3.** ρ=0.3 saturation ratio 在 Algorithm 1 中使用但未引用来源。\n\n**M4.** Figure 1 图例文字 ~6–7pt，低剂量区域多条线重叠，打印尺寸下难以辨识。\n\n**M5.** Table 2 MAE 精度不一致（混合 3 位和 4 位小数）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **Volume confound 是论文最关键的弱点**（W1）。R1 从方法/实验角度（单一家族控制）、R2 从概念角度（\"污染剂量-响应\"概念在 45% 为数据量时的有效性）独立识别，合并后挑战核心叙事。\n\n2. **ContamCal 劣于 baseline 是根本性问题**（W3）。两者一致认为\"诊断价值\"辩护在 γ 不可靠的情况下不充分。\n\n3. **分类体系需重构为 2+2**（W4）。Collapse/V-Recovery 应显式标为 Qwen2.5 特异的初步观察。\n\n4. **Domain-level γ claims 必须降级**（W5）。R1 从统计理论（J=16 < J≥50 minimum）、R2 从经验证据（仅 Qwen2.5 显示显著域异质性）共同得出 Abstract claim 不成立。\n\n5. **ARC IRT 结果应退出正文**（W6）。PPP=0.003 使 IRT 估计不可靠。\n\n6. **RRF S2 信号必须处理**（W2）。移除后 10× 改善不可忽视。\n\n7. **Abstract 需限定范围**（W7）。两者一致认为需要 SFT-stage 限定。\n\n---\n\n## Reviewer Divergence\n\n**技术新颖性定位 [R3-N7]：**\n\n- **Reviewer 2** 认为 2PL+γ 是标准 explanatory IRT/DIF 方法论，贡献主要是应用框架而非方法创新。各组件（Min-K%++、RRF、explanatory IRT、threshold classification）均为标准方法。\n- **Reviewer 1** 部分反驳：training-free contamination signals → RRF fusion → continuous per-item exposure → IRT covariate structure → credible intervals 的完整技术路径此前不存在。γ 的参数化选择（outside vs inside a_i bracket）是有理论含义的非 trivial 设计决策。将方法论贡献降级为 \"merely application\" 低估了应用层面的创新。\n- **共识落点**：论文需要更清晰的定位声明，显式承认 2PL+γ 是标准 explanatory IRT，同时阐明将其应用于 LLM 污染检测（连续暴露协变量）的具体创新之处。当前表述模糊了这一区分。\n\n---\n\n## Questions for Authors\n\n**Q1.** Volume 控制何时能推广到至少一个非 Benefit 家族（如 Collapse 模式的 Qwen2.5-14B）？没有这个控制，剂量-响应分类混淆了污染与数据量效应。\n\n**Q2.** 移除 S2 后 γ 估计和剂量-响应 profile 如何变化？10× ρ_dose 改善暗示下游有实质影响。\n\n**Q3.** Full fine-tuning 是否会产生不同的剂量-响应模式？LoRA 的低秩约束（r=16）可能抑制记忆化效应，使 Benefit 模式可能是 LoRA 特有的 artifact。\n\n**Q4.** 鉴于 γ 在 J=16 下对先验的 2.6× 敏感性，读者应如何解读具体 γ 值（如 Social Sciences γ_d=−0.63）？符号是否稳健即使数值不稳定？\n\n**Q5.** 跨 benchmark 传递有多少是 SFT 引入的指令跟随能力提升，而非真正的污染传播？GSM8K 的 volume 控制显示 53% volume 贡献，支持此替代解释。\n\n**Q6.** 如果框架的价值是诊断而非校准，是否应重命名？当前名称创造了论文无法满足的期望。\n\n---\n\n## Missing References\n\n- **Hill (1910)** — dose-response 是论文标题概念和核心框架。奠基性文献仅出现在 Appendix AB，必须在正文（§1 或 §3）中引用。\n- **Deng et al. (2024)** — 引用为 arXiv 但可能已发表于 NAACL 2024，需验证并更新引用元数据。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未派发外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（耗时 ~4 分钟）。\n\n10 项发现，均为 info 级别（0 critical, 0 warning）：\n\n- **Figure 1 (p.1)**：图例文字 ~6–7pt，低剂量区多条曲线重叠。建议加大 marker 差异。\n- **Table 1 (p.2)**：8+ 列，紧凑但未溢出。booktabs 格式正确。\n- **Table 2 (p.5)**：MAE 精度不一致（3 vs 4 位小数）。\n- **Section 5 heading (p.6)**：出现在左栏底部 ~1/4 处，勉强可接受。\n- **Page 7**：密度很高（Table 4 + Figure 5 + 5 个 subsection），不影响可读性。\n- **Figure 6 (p.8)**：Per-domain CI 图清晰。Limitations ~1 段，EMNLP 合规。\n- **Figure 2 (p.3)**：全文最佳 display item——pipeline 架构图，三阶段颜色区分明确。\n- **Appendix (p.13, p.17)**：多面板子图 axis label ~6pt，附录可接受。\n- **Algorithm 1 (p.18)**：排版规范。\n\n**未检测到格式违规。** 8 页正文确认，EMNLP 2026 合规。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n\n**Confidence: 4/5 (High)**\n\n本文探讨了一个重要问题——不同模型家族如何响应 benchmark 污染——并在生产级规模进行了精心设计的受控实验。核心经验发现（污染不均匀膨胀分数、剂量-响应模式因家族而异）对社区有真正的信息价值。\n\n但论文面临三个相互关联的问题，阻碍了主会议推荐：\n\n1. **方法论框架（ContamCal）未兑现承诺。** 校准性能劣于 raw accuracy，域级估计对先验敏感且在 J=16 下不可靠，核心信号组件之一（S2）主动损害 pipeline 性能。IRT 诊断是论文声称的方法论贡献，但当前状态下其可靠性不如它声称要改进的 baseline。\n\n2. **剂量-响应叙事被混淆。** 45% 的 Benefit 来自数据量，Collapse 可能由额外训练的灾难性遗忘解释，且仅一个家族有 volume 控制。论文无法自信地将剂量-响应模式归因于污染特异性效应。核心主张可能从\"模型对*污染*的响应不同\"变为\"模型对*内容重叠不同的额外 SFT 训练*的响应不同\"。\n\n3. **分类体系从不充分的证据过度泛化。** 四个类别来自五个家族，其中两个类别各基于一个家族（均为 Qwen2.5），两个 \"已复现\" 类别的统计支持从稳健（Immune/Phi-4）到边界（Benefit/OLMo-2）到统计不可区分（Benefit/Gemma-2 on AICc）。\n\n这些问题单独看是实质性的，合并后相互强化：volume confound (1) 削弱 taxonomy (3)，而 IRT 框架的不可靠性 (2) 削弱了本可帮助解纠缠混淆因素的域级诊断。鉴于真正的经验贡献，Findings 级别发表是合适的，但主会议接收需要解决 volume 控制缺口、pipeline 完整性和框架重新定位。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 首句需显式限定范围：\"across *five open-source* model families *at 7B–14B scale under SFT injection*\"\n- \"enables within-family domain-level contamination diagnosis with credible intervals\" 在 J=16 下不成立，替换为限定性语言或删除\n- 20+ 数字减至 8–10，以概念发现引领\n- 字数 ~193，在 EMNLP 2026 的 200 词限制内\n\n### Section 1 (Introduction)\n- 引入 dose-response 概念时引用 Hill (1910)\n- 将 claims 限定至 SFT injection at 7B–14B\n\n### Section 2 (Related Work)\n- 扩展 Schaeffer et al. (2025) 讨论——其统计功效分析直接相关于 n=3 seed 局限\n- Han et al. (2026) 方法层面区分足够；考虑增加 1–2 句经验对比范围\n\n### Section 3 (Method)\n- §3.2：增加一句说明 ΔELPD ≈ 0（γ outside vs inside a_i），选择基于解释便利性\n- §3.3：承认 e_ij 点估计限制及对 γ CI 宽度的影响\n- §3.4：显式声明 Algorithm 1 是描述性启发式，非方法贡献\n\n### Section 4 (Experimental Setup)\n- 报告 volume 控制设计理由和局限（仅测试 Falcon3）\n\n### Section 5 (Results)\n- §5.1：重构为 2 confirmed (Immune, Benefit) + 2 preliminary (Collapse, V-Recovery)，增加 AICc 证据\n- §5.2：ARC 跨 benchmark 结论必须基于 raw accuracy 而非 IRT，增加显式声明\n- §5.5：从 \"Calibration Quality\" 改写为 \"Diagnostic Utility\"，以域级 γ_d 对比引领，将聚合 MAE 定位为非目标指标\n- 域级 γ 讨论处：在正文（非仅附录）中增加 prior sensitivity 警告\n\n### Section 6 (Discussion)\n- 增加段落讨论 triple confound (content/volume/LoRA)\n- 更显著地呈现 Falcon3 45%/55% 分解\n- 删除或限定 \"65–70% baseline vulnerability band\"（基于 2 个 Qwen 模型，被 LLaMA 反例推翻）\n\n### Limitations\n- 承认：(a) 单一家族 volume 控制，(b) SFT 特异性发现可能不推广到预训练污染，(c) 暴露测量不确定性未传播到 γ CI\n\n### 格式\n- 首次出现时标注 CI 类型：\"credible interval (from Bayesian IRT)\" vs \"confidence interval (from bootstrap)\"\n- Table 1：定义 'Stab.' 列\n- Algorithm 1：删除 dead branching (lines 91–94)\n- Figure 1：增大图例字号，区分 markers",
    "project": "contamcal-irt-calibration",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
  }
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-25T21:47:59.692375+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Assistant

_source line 1300 · 2026-05-25T21:48:27.827109+00:00_

Round 13 审稿报告已投递，Issue Tracker 已同步。

**本轮审稿总结：**

- **评分：3.0 (Findings)**，置信度 4/5
- **6 项 Must-Fix**：volume confound 控制不足（最强共识）、S2 信号主动有害、ContamCal 劣于 baseline、分类体系证据不足、domain-level γ 不可靠、ARC IRT 结构性失配
- **8 项 Should-Fix**：Abstract 范围过宽、n=3 seeds 不充分、不确定性传播缺失、prior work 区分不足、Algorithm 1 启发式定位、Abstract 数字密度、术语混用、SFT 生态效度
- **唯一分歧**：技术新颖性定位（R2 认为标准 DIF，R1 认为应用集成有实质价值）——共识落点为需要更清晰的定位声明
- **视觉审查**：已完成，0 critical/0 warning/10 info，无格式违规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 121

## Round 121

2 recorded events


### User

_source line 1301 · 2026-05-25T21:48:27.831901+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — Reviewer 1 初审意见

---

### Must-Fix 问题

**[AGREE] R1-Must-Fix-1: J=16 identifiability gap 使 domain-level γ claims 缺乏支撑**

同意这是一个关键问题，并且与我的 W3 指向同一根本缺陷。

需要澄清的技术细节：论文的 IRT 模型是在 benchmark 级别拟合的（J=300 subsampled items for MMLU），γ_i 是 item-level 参数。Domain-level 分析是对同一 domain 内的 ~16 个 item-level γ_i 进行聚合。因此 R1 的担忧应理解为：不是 IRT 模型本身的可辨识性问题（J=300 足够），而是 domain-level 聚合统计量的 **统计功效** 问题——16 个 γ_i 的均值能否可靠地检测域级别差异。

即便如此，R1 的核心论点完全成立：Appendix F 的模拟在 J=100/200/500 上进行，跳过了 J=16 这一实际使用规模。更关键的是，论文仅在 Qwen2.5 上观察到显著域级别效应（Section 5.7），这与我的 W3 互相印证——Abstract 中 "enables within-family domain-level contamination diagnosis" 的措辞承诺了一个在现有证据下无法兑现的能力。

**我的补充**：R1 指出的 identifiability gap 和我指出的 evidence gap 共同构成一个更强的论据：domain-level diagnosis 不仅在统计理论上缺乏支撑（J=16 功效不足），在实证数据上也仅有单一家族的证据。建议将 domain-level diagnosis 从 "key contribution" 降级为 "exploratory analysis"。

---

**[AGREE] R1-Must-Fix-2: Volume confound 仅控制 1/6 模型但解释了 43-53%**

完全同意，且此问题与我的 W2（"Benefit" 因果解释）直接互补。

R1 从方法论角度指出了 volume-matched control 的代表性问题（单模型无法代表全部），我从概念角度指出了 "Benefit" 定义的模糊性（如果 45-55% 来自数据量/格式适应而非记忆化，还能称之为 contamination-driven 效应吗？）。两个问题叠加后，"Benefit" 模式的整个叙事都需要重新审视。

**关键补充**：R1 提到 volume confound 贡献了 "43-53%"。我从论文中读到的是 45%（Appendix R，Phi-4 单模型），但 R1 给出了一个范围。如果不同模型的 volume sensitivity 不同（这很可能——Gemma-2 vs. Phi-4 的 capacity 差异显著），那么 "Benefit" 模式中的某些家族可能 **完全** 由数据量解释，而非污染效应。这需要在更多模型上验证。

---

**[PARTIALLY AGREE → 降级为 Should-Fix] R1-Must-Fix-3: γ prior sensitivity（posterior mean 2.6× 漂移）**

R1 的事实观察完全正确——Appendix L 显示 γ posterior mean 在 N(0,1) vs N(0,0.2) 下从 0.34 漂移到 0.89，约 2.6× 变化。这确实表明数据对 γ 的约束力有限。

但我认为这是 **Should-Fix 而非 Must-Fix**，理由如下：

1. **方向稳定性**：Appendix L 明确指出 95% CI 在所有 prior 设定下都包含零（lower bound 稳定在 ≈ −0.1）。这意味着 prior sensitivity 影响的是 magnitude 而非 direction。如果论文的推断主要依赖方向性判断（STEM 正向 vs Social Sciences 负向），prior sensitivity 不改变核心结论。

2. **分类算法的鲁棒性**：Algorithm 1 的分类主要基于 end-to-end accuracy shift 的方向和噪声阈值（τ=2pp），而非 γ 的具体数值。γ 在 Algorithm 1 中仅用于 domain-level 细分（Section 3.4 最后），因此 prior sensitivity 主要影响 domain-level 分析（已被 R1-Must-Fix-1 覆盖），而不影响 aggregate-level 的剂量-响应分类。

3. **Bayesian 分析中的常规现象**：当 effective sample size 有限时，informative vs. weakly informative priors 产生不同 posterior 是预期的。关键问题不是 "posterior 是否对 prior 敏感"，而是 "在合理的 prior 范围内，实质性结论是否改变"。论文使用的 N(0,1) default prior 在 IRT 文献中是标准的弱信息先验。

**我的判断**：prior sensitivity 是一个需要在论文中更充分讨论的问题（应解释为什么选择 N(0,1)，以及在什么条件下 γ 的 magnitude 可以被信任），但不构成一票否决的 Must-Fix。将其与 R1-Must-Fix-1 合并处理更合理：都指向 domain-level 分析的统计功效不足。

---

### Should-Fix 问题

**[AGREE] R1-Should-Fix-1: n=3 BCa bootstrap 不可靠**

同意。BCa bootstrap 的 bias-correction 和 acceleration 估计在 n=3 下没有统计保障。n=3 的 bootstrap 置信区间本身就只应被视为描述性的，不应用于假设检验。论文在多处使用 "statistically significant for Gemma 2, bootstrap 95% CI [+1.49, +3.14]pp"（Abstract），这种基于 n=3 BCa 的显著性声明具有误导性。

建议：(1) 删除 "statistically significant" 的措辞，改为 "consistently positive across three seeds"；(2) 明确报告 n=3 的限制。

---

**[AGREE] R1-Should-Fix-2: S2 信号在 model-level 有害但被保留**

同意。Appendix D Table 7 显示剔除 S2 后 model-level ρ_mean 从 0.049 跳到 0.471（MMLU），说明 S2 在 model-level 引入了大量噪声。论文的解释是 S2 在 item-level 提供了有用信息（"S2 provides unique item-level information, ρ = 0.773"）。

但如果分析同时在 model-level 和 item-level 进行（Section 5.7 vs Section 5.1），使用同一信号组合在不同层级产生矛盾效果，至少应该在论文中讨论这一 trade-off，或提供层级自适应的信号选择方案。

---

**[AGREE] R1-Should-Fix-3: SFT 外部效度讨论不足**

同意，且与我的 Q2 一致。LoRA-based SFT 注入与真实 pretraining 阶段污染在记忆化动态上的差异是论文最大的外部效度限制。Limitations section 仅用一句话带过（"Our LoRA-based SFT injection differs from pretraining-stage leakage"），缺乏对以下关键差异的讨论：

- SFT 阶段模型已经收敛，记忆化模式可能与 pretraining 中的 gradual exposure 不同
- LoRA 的低秩约束可能限制了模型记忆 benchmark items 的能力，使观察到的效应偏保守
- Schaeffer et al. (2026) 在 pretraining 注入中发现更陡的剂量-响应曲线，暗示 SFT 和 pretraining 的模式可能系统性不同

---

**[PARTIALLY AGREE] R1-Should-Fix-4: DiD parallel trends 不可验证**

部分同意。R1 指出 DID 仅有两个时间点（pre/post SFT），无法验证 parallel trends 假设。这在技术上是正确的。

但需要注意：论文的 DID 设计（Section 5.4）不是标准的面板数据 DID——它比较的是同一模型在 treated（污染 items）和 untreated（非污染 items）之间的 accuracy 变化。pre-treatment balance check（Table 14, p > 0.10）提供了一定程度的支持，虽然不等同于 parallel trends 验证。

此外，DID 在 pre/post 设计中的应用在应用微观经济学中是常规做法（如 policy evaluation），通常通过 pre-treatment covariates balance 而非多期数据来增强可信度。

**我的判断**：这是一个有效的统计方法论 caveat，但不影响论文的核心结论（DID 的结论是 "no item-specific memorization detected"，这是一个 null result）。作为 null result 的稳健性问题，其影响低于 positive claims 的稳健性问题。维持 Should-Fix。

---

### Minor 问题

**[AGREE] R1-Minor-1: Global capability modulation 解释过度**

同意。跨基准迁移（MMLU→GSM8K）可能有多种解释：instruction-following 能力提升、格式适应、或通用知识强化。将其统一归因于 "global capability modulation"（Section 5.2, Section 6）过于简化。这与我的 Q5 一致。

---

**[AGREE] R1-Minor-2: Out-of-sample validation 仅一个家族**

同意。LLaMA-3.1-8B 是被分类为 Immune 的家族，out-of-sample validation 确认了 Immune 分类。但 Benefit 和 Collapse 模式没有 out-of-sample 验证，这些是更有争议的分类。

---

**[REBUT] R1-Minor-3: γ 参数化选择（连续 vs. 离散）缺乏理论论证**

不完全同意。连续 γ_i · e_ij 参数化是对离散 DIF grouping 的自然推广。给定论文的 Stage 1 产生连续的暴露度分数 e_ij ∈ [0,1]，使用连续协变量而非将其二值化是统计上更合理的选择——二值化会丢失信息且引入任意阈值。De Boeck and Wilson (2004) 的解释性 IRT 框架明确支持连续协变量。

论文在 Appendix G 中还比较了连续参数化 vs. 统一 DIF alternative，显示两者产生可比结果但连续版本提供了更高的 effective sample size 和更紧的 posterior 估计。

**我的判断**：这不需要额外的理论论证，参数化选择已有充分的方法论支持。降为非问题。

---

### 综合判断

R1 和我的审查意见在以下方面高度一致：

1. **Domain-level diagnosis 是论文最薄弱的 claim**：R1 从 identifiability（J=16）和 prior sensitivity 角度，我从证据覆盖度和 Abstract overclaiming 角度，共同指向同一结论——domain-level 诊断应从 key contribution 降级为 exploratory analysis。

2. **Volume confound 是系统性问题**：R1 指出控制实验的代表性不足，我指出 "Benefit" 概念的定义模糊性。两者叠加后，Benefit 模式的整个叙事需要更审慎的表述。

3. **Aggregate-level 发现可信**：我们都认为异质性剂量-响应模式（Immune/Benefit/Collapse）的 aggregate-level 发现是论文的核心价值，且实验设计在这个层面上是严谨的。

**分歧点**：γ prior sensitivity 的严重程度。R1 视为 Must-Fix，我认为在方向稳定的前提下更适合 Should-Fix（但需在论文中更充分讨论）。这个分歧的根源在于：如果将 domain-level γ diagnosis 视为核心贡献，prior sensitivity 是 Must-Fix（因为它直接影响该贡献的可靠性）；如果将其降级为 exploratory analysis，prior sensitivity 就是 Should-Fix（因为 aggregate-level 分类不依赖 γ magnitude）。

**建议统一处理**：将 R1-Must-Fix-1（J=16）、R1-Must-Fix-3（prior sensitivity）、和我的 W3（evidence gap）合并为一个统一的 Must-Fix：**domain-level diagnosis claim 在统计功效、prior stability、和实证覆盖三个维度上都缺乏充分支撑，应降级为 exploratory finding。**

---

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：与 Reviewer 1 在主要问题上高度一致（domain-level claim 过强、volume confound 系统性、aggregate-level 可信），仅在 γ prior sensitivity 的严重程度上有分歧（R1 视为 Must-Fix，我认为 Should-Fix），并建议将三个相关问题合并为一个统一的 Must-Fix 处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1302 · 2026-05-25T21:49:18.314011+00:00_

R2 交叉回应已收到。审稿报告已于 R1 交叉回应完成后投递（基于 tracker 中两位 Reviewer 的 Round 1 完整数据）。

R2 的交叉回应与已提交报告高度一致，无需重新投递：

**与报告的一致性：**
- Domain-level γ claim 应降级为 exploratory：完全一致（报告 W5）
- Volume confound 是系统性问题：完全一致（报告 W1）
- Aggregate-level 发现可信：与报告 Strengths 一致
- S2 信号有害、n=3 BCa 不可靠、SFT 外部效度：全部一致

**报告未覆盖的两个额外分歧点：**
1. **γ prior sensitivity 严重程度**：R1 视为 Must-Fix，R2 认为 Should-Fix（方向稳定，仅 magnitude 受影响）。报告中将其合并到 W5（domain-level γ）作为 Must-Fix 处理，R2 对此合并处理方式表示同意。
2. **γ 参数化选择**（R1 Minor-3）：R2 REBUT——连续 γ_i·e_ij 是离散 DIF grouping 的自然推广，有 De Boeck & Wilson (2004) 方法论支持，不需要额外论证。报告中该问题仅在 Detailed Comments §3.2 以一句话提及（ΔELPD≈0，解释便利性），与 R2 的 REBUT 方向一致。

这两个额外分歧均不影响报告的整体评分（3.0 Findings）和优先级排序。报告已投递，本轮审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---
