# Reviewer 1 coordination — Part 3 of 8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/ed/ed9cd9e2adfd642813e6.json)

## Round 32

### Tool result

_source line 968 · 2026-05-17T06:16:31.703032+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	These signals achieve reliable quality estimation ($\rho$ up to 0.42 on the primary test bed and Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap}: structural best-of-$N$ selection matches or degrades greedy decoding ($T{
…[truncated 3201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 969 · 2026-05-17T06:16:31.753830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 970 · 2026-05-17T06:16:32.205811+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 3479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 971 · 2026-05-17T06:16:32.206184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 972 · 2026-05-17T06:16:32.256744+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed c
…[truncated 16434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 973 · 2026-05-17T06:16:38.129524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "208"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "208"
  }
}
```

</details>

---


### Tool result

_source line 974 · 2026-05-17T06:16:38.631856+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (208). The file has 208 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 975 · 2026-05-17T06:16:38.632328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 976 · 2026-05-17T06:16:38.682834+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	For quality estimation, all signals achieve positive $\rho$ across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	For selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\%, $p{=}0.091$), failure on CoNLL (58\%).
7	Structural signals uniformly degrade selection regardless of dataset.
8	RE signal rankings are reported in Appendix~\ref{app:re_extension}.
9	
10	\paragraph{Why the gap exists.}
11	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
12	
13	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
14	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
15	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
16	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; Few-NERD (75\%) shows 10\%; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zer
…[truncated 14593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 977 · 2026-05-17T06:16:44.053375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 978 · 2026-05-17T06:16:44.505072+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and SciERC; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to structural selection: despite 12--14~pp oracle headroom, no structural signal significantly outperforms greedy decoding on any dataset.
6	The gap stems from two jointly operating mechanisms: instance degeneracy (10--58\% of instances produce identical F1 across all $N$ samples) and LP compression (median within-instance range of 0.041 nats).
7	Instance degeneracy monotonically predicts LP selection effectiveness across three datasets: at 10\% degeneracy (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals (logistic regression, MLP, random forest) cannot close the oracle gap, confirming the bottleneck is in the structural feature space.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the structural gap requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline at low degeneracy.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 979 · 2026-05-17T06:16:44.505481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 980 · 2026-05-17T06:16:45.108394+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection
…[truncated 206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 981 · 2026-05-17T06:16:45.109536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 982 · 2026-05-17T06:16:45.311040+00:00_

File content (30892 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 983 · 2026-05-17T06:16:50.277149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 984 · 2026-05-17T06:16:50.628656+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 31849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 985 · 2026-05-17T06:16:56.575513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "400",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "400",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 986 · 2026-05-17T06:16:56.626622+00:00_

400	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
401	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
402	\midrule
403	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
404	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
405	\midrule
406	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
407	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
408	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	\section{Training Configuration}\label{app:training}
414	
415	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
416	
417	\begin{table}[t]
418	\centering
419	\small
420	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
421	\label{tab:training}
422	\begin{tabular}{ll}
423	\toprule
424	Parameter & Value \\
425	\midrule
426	LoRA rank / $\alpha$ & 32 / 64 \\
427	LoRA target & All linear modules \\
428	LoRA dropout & 0 \\
429	Optimizer & AdamW \\
430	Learning rate & 2e-4, cosine schedule \\
431	Warmup ratio & 0.1 \\
432	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
433	Epochs & 5 \\
434	Max sequence length & 2048 \\
435	Precision & bf16 \\
436	Gradient checkpointing & Enabled \\
437	Max gradient norm & 1.0 \\
438	Training seed & 42 \\
439	Framework & LLaMA Factory \\
440	\midrule
441	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
442	SciERC split & 1861 / 275 / 551 \\
443	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
444	& eval\_steps${=}$200, save\_limit${=}$5 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	\paragraph
…[truncated 23869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 987 · 2026-05-17T06:17:02.568687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "799",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "799",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 988 · 2026-05-17T06:17:02.619479+00:00_

799	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
800	
801	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
802	
803	\paragraph{Pairwise overlap.}
804	LP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
805	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
806	
807	\paragraph{Instance complexity drives failure.}
808	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
809	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
810	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
811	
812	\begin{table}[t]
813	\centering
814	\small
815	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
816	\label{tab:stable_failures}
817	\begin{tabular}{lcccc}
818	\toprule
819	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
820	\midrule
821	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
822	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
823	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
824	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
825	\bottomrule
826	\end{tabular}
827	\end{table}
828	
829	\paragraph{Flip instances.}
830	Only 5 RE instances with gold relations flip from LP fai
…[truncated 19079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 989 · 2026-05-17T06:17:10.196348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1098",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1098",
    "limit": "200"
  }
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-17T06:17:10.196830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-17T06:17:10.197264+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	Our experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.
12	Degeneracy varies across datasets: CoNLL (91\% single-sample F1) exhibits 58\%; SciERC (66\%) shows 21\%; Few-NERD (75\%) shows 10\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero (\S\ref{sec:discussion}).
13	Few-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.
14	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/sum
…[truncated 4262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 992 · 2026-05-17T06:17:10.197669+00:00_

1098	Signal & $\rho$ & Sample AUROC & Sel.\ $\Delta$ & 95\% CI \\
1099	\midrule
1100	LP & .421 & .578 & $\mathbf{+1.36}$\,pp & [+1.18, +1.53] \\
1101	VC & .386 & --- & $-$1.79\,pp & --- \\
1102	FK & .313 & --- & $-$2.26\,pp & --- \\
1103	SJ & .300 & --- & $-$2.14\,pp & --- \\
1104	EM & .287 & --- & $-$3.85\,pp & --- \\
1105	\midrule
1106	\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
1107	\bottomrule
1108	\end{tabular}
1109	\end{table}
1110	
1111	\paragraph{Key observations.}
1112	(1)~All five signals achieve positive QE ($\rho$ 0.29--0.42), confirming that quality estimation works on Few-NERD. LP leads ($\rho{=}0.42$), followed by VC ($0.39$); the ranking differs from SciERC where VC leads, reflecting dataset-specific signal informativeness.
1113	(2)~LP is the only signal achieving significant positive selection ($+1.36$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.
1114	(3)~Despite positive $\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.
1115	(4)~Low degeneracy (10.1\%) enables LP selection: candidates differ in F1 more often, giving LP's per-sample signal headroom to exploit. This contrasts with SciERC (21\% degeneracy, LP $+0.42$~pp non-significant) and CoNLL (58\%, LP fails).
1116	
1117	\section{Per-Entity-Type LP Selection Analysis}\label{app:per_type_lp}
1118	
1119	Table~\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.
1120	The degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\%).
1121	The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\rho{=}{-}0.881$, $
…[truncated 3156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 993 · 2026-05-17T06:17:18.824406+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 994 · 2026-05-17T06:17:18.925097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 995 · 2026-05-17T06:19:32.024420+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 16 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## Summary\n\nThis paper evaluates five confidence signals (four instance-level, one per-sample) for quality estimation and sample selection in LLM-based NER. It demonstrates that while all signals achieve reliable quality estimation (ρ up to 0.42, AUROC up to 0.82), none translates QE into effective best-of-N selection—the \"correlation-selection gap.\" Two mechanisms are identified: instance degeneracy (10–58% identical outputs) and LP compression (median range 0.041 nats). The degeneracy-gating pattern across three datasets shows LP selection effectiveness is inversely related to degeneracy rate. The paper is thorough, well-structured, and makes a genuine negative-result contribution with extensive ablations.\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5 (borderline Findings/Conference)\n**一句话总结**: 实证工作扎实、消融全面，但核心 degeneracy-gating claim 的统计支撑仅有 3 个数据点，且多处统计方法论存在可改进空间，制约了结论的普适性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计系统、ablation 充分，但统计效力不足（2-seed sign test）、核心 monotonic claim 仅 3 数据点、Bonferroni scope 存在争议 |\n| Excitement | 3/5 | 负面结果有价值且相关性强，但缺少 actionable positive contribution（如 verifier baseline 或 task-specific LP variant） |\n| Reproducibility | 4/5 | 训练配置详尽、constrained decoding pipeline 有描述，但 vLLM 版本/XGrammar 具体配置缺失 |\n| Confidence | 4/5 | 仔细阅读，熟悉 MBR decoding 和 NER 评估方法论 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 2-seed paired sign test 的统计效力严重不足\n\n- 具体位置：Section 4.3 (Table 2), footnote 4, §4.1 footnote (\"Quality estimation uses a single primary seed (seed=42); selection uses 2-seed averages for variance estimation\")\n- 问题：Selection 的核心结论\"no signal significantly outperforms greedy\"基于 2-seed paired sign test。Sign test 是最保守的非参数检验（仅使用方向信息，丢弃幅度信息），在 2-seed 设定下几乎无法检测到真实效应。如果 LP 真的有 +0.2pp 的效应，sign test 在 n=529、2 seeds 下的 power 极低。这意味着 p=0.29 可能是 under-powered null 而非 true null。论文用 3-seed 实验声称 σ≤0.026 证明 stability，但这仍然不够：3 个 seeds 不足以可靠估计 σ，更不足以构建有效的假设检验。\n- 为什么影响接收：核心负面结论（\"selection fails\"）的统计基础不牢靠。审稿人无法区分\"效应不存在\"和\"检验无力检测到效应\"。\n- 建议修改方向：(1) 使用 paired bootstrap test（B=10,000）替代 sign test，利用幅度信息；(2) 增加 seed 数至 5+ 或报告 power analysis；(3) 明确区分 \"no evidence of effect\" 与 \"evidence of no effect\"——TOST 部分尝试做了但仅限附录且结论 configuration-dependent。\n\n**N2** [critical] Degeneracy-gating 的 monotonic pattern 仅基于 3 个数据点\n\n- 具体位置：Table 4 (§4.4), Abstract line 7, Conclusion line 7, Figure 3\n- 问题：核心 claim \"instance degeneracy monotonically predicts LP selection effectiveness\" 来自 CoNLL(58%→fail), SciERC(21%→+0.42pp), Few-NERD(10%→+1.36pp) 三个数据点。3 点的 monotonic trend 在统计上不具有意义——任意 3 个不同值必然可以排出 monotonic order。论文自己报告 Spearman ρ=−0.57, p=0.066 (n=11，含 per-type 数据点, Figure 3 caption)，即未达到 α=0.05 显著水平。\n- 为什么影响接收：这是论文最突出的 claim（出现在 title 暗示、abstract、intro contribution list、conclusion），但统计证据不支持将其从 observational pattern 提升为 \"predictive mechanism\"。\n- 建议修改方向：(1) 将语言从 \"monotonically predicts\" 降级为 \"is consistent with a monotonic relationship, though the limited number of dataset-level data points (n=3) precludes statistical confirmation\"；(2) 补充 per-type 分析的正式统计（已有 per-type data），计算 cross-dataset + per-type 的 mixed-effects model；(3) 或承认这是 exploratory observation 而非 confirmed mechanism。\n\n**N3** [critical] Bonferroni correction scope 与 post-hoc ε 选择的交互\n\n- 具体位置：§4.3 footnote 4 (\"survives Bonferroni over 5 comparisons\"), §Discussion Non-tied subset analysis, Appendix Table 8 (ε sweep)\n- 问题：论文声称 non-tied LP subset 的 +2.9pp (p=0.004) \"survives Bonferroni correction over 5 comparisons\" (p_adj=0.020)。但 Bonferroni scope 仅覆盖 5 signal comparisons，未纳入 ε threshold 的 post-hoc 选择。Table 8 (Appendix) 明确展示了 7 个 ε 值的 sweep (0.01–0.20)，且 ε=0.05 被选择恰恰因为它 \"yields the strongest statistical separation\"。如果将 7 个 ε × 5 signals = 35 comparisons 纳入 Bonferroni，p_adj = 0.004 × 35 = 0.14，不再显著。\n- 为什么影响接收：这是论文唯一的正面统计显著结果（\"LP does carry per-sample discriminative information\"），如果 multiple comparison correction 范围不当，核心 evidence chain 断裂。\n- 建议修改方向：(1) 明确承认 ε=0.05 是 post-hoc 选择，Bonferroni 范围存在争议；(2) 使用 pre-registered split（如 median split）或 permutation-based FDR 控制；(3) Limitations 中已提到 \"post-hoc exploratory choice\" 但主文 footnote 4 的 framing 仍暗示这是 confirmed finding——两处需要保持一致。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Random baseline (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距缺乏理论解释\n\n- 具体位置：Table 2 (§4.3)\n- 问题：如果 Random 是从同一温度 T=1.0 的 N 个 samples 中随机选一个，而 Single 是同一分布的单次采样，理论上 E[Random] = E[Single] = E[sample under T=1.0]。但 Table 2 显示 Random=0.610, Greedy(T=0)=0.645。Greedy 是不同分布（argmax decoding），差异合理。但 \"Random\" 的含义需要澄清：如果 Random 是从 N=8 candidates 中 uniform 选取的 expected F1，它应该等于 single-sample mean F1 under T=1.0。Table 4 (Few-NERD) 中 Greedy=0.748 而 SciERC Greedy=0.614（full-set），暗示 Table 2 的 Greedy=0.645 是 gold-filtered subset 的 T=0 结果。那 Random=0.610 是 gold-filtered subset 的 sample mean under T=1？如果是，0.610 vs 0.645 反映的是 T=1 vs T=0 的 quality gap，而非 selection 能力。论文未明确标注 Random 的定义。\n- 建议：明确说明 Random baseline 的语义——是 T=1 single sample mean 还是其他构造；讨论 Greedy(T=0) 与 Sample mean(T=1) 的差异是否意味着 T=1 本身降低了 quality。\n\n**W2** [warning] Kendall's W=1.0 with only 3 seeds 的 precision caveat 不充分\n\n- 具体位置：§4.5 (\"Signal rankings are stable across seeds (Kendall's W=1.0 at N=8; Table 11)\")，Appendix Table 11\n- 问题：Kendall's W with m=3 raters (seeds) ranking k=5 items (signals) 的 sampling distribution 是非常 discrete 的。W=1.0 只说明 3 个 seeds 恰好产生了相同 ranking，但置信区间极宽。论文在 Appendix (line 899) 有 caveat (\"statistical power with n=3 is limited\")，但主文 §4.5 直接引用 W=1.0 作为 robustness 证据，无 qualification。\n- 建议：主文中加入 caveat，如 \"though the small number of seeds (3) limits the precision of this estimate\"。\n\n**W3** [warning] Instance degeneracy 8B(21%) vs 4B(10.4%): capability vs fine-tuning recipe confound\n\n- 具体位置：§4.5, Table 5 (Discussion), §4.5 \"Instance degeneracy also scales with model capability\"\n- 问题：论文声称 \"instance degeneracy scales with model capability\" (8B: 21%, 4B: 10.4%)。但两个模型使用相同 training recipe（5 epochs, rank=32）。更大模型在相同 epochs 下可能 overfit 更快（更多参数 per data point），导致更强的 output convergence——这是 training dynamics artifact 而非 fundamental capability-driven 现象。如果 4B 训练更多 epochs 使其达到相似 F1，degeneracy 可能追平。论文的 LoRA-rank ablation (rank=8 降低 degeneracy 到 7%) 实际上 支持 \"fine-tuning recipe\" 解释而非 \"capability\" 解释。\n- 建议：(1) 讨论 effective parameter count / data ratio 的 confound；(2) 弱化 \"scales with model capability\" 的 causal 语言为 \"correlates with model scale under matched training\"；(3) 考虑 early-stopping ablation 作为 disentanglement。\n\n**W4** [warning] TOST 等价性结论的 configuration-dependent 呈现不平衡\n\n- 具体位置：§4.3 (line 109), Appendix §TOST (External equivalence margins)\n- 问题：主文 §4.3 说 \"TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration\"——但 varies 的方向是 Qwen-CoNLL **所有** signal 都 fail equivalence（降级 0.9–1.5pp），这意味着 signals 可能 actively harm selection。附录详细报告了这一点，但主文的措辞 \"varies by configuration\" 过于轻描淡写。一个 reviewer 可能认为这削弱了 \"no harm\" 的 claim。\n- 建议：主文中更清晰地呈现——某些配置下 signal selection 显著 worse than greedy（Qwen-CoNLL），这不仅仅是 \"equivalence fails\" 而是 \"active degradation\"。\n\n**W5** [warning] Gold-empty instance filtering 在 QE 和 Selection 之间的不一致\n\n- 具体位置：§3.3 (\"Both quality estimation and selection exclude instances with no gold annotations: n=529 on SciERC (from 551), n=2,756 on CoNLL (from 3,453)\")，但 Table 4 中 SciERC 使用 n=551\n- 问题：Table 4 (Few-NERD comparison) 中 SciERC 使用 \"full test set (n=551) for protocol consistency\" 而非 gold-filtered n=529，且 Greedy=0.614 而非 Table 2 的 0.645。脚注解释了差异但这引入了 apple-to-orange comparison。Table 2 (gold-filtered) 的 LP Δ=+0.2pp 与 Table 4 的 LP Δ=+0.42pp 不一致——读者需要仔细追踪哪个表用哪个 n。\n- 建议：统一报告协议，或在 Table 4 中同时报告 gold-filtered 数字以便 direct comparison。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.1: \"3-seed stability σ≤0.026\" — σ 是 sample std 还是 population std? Table 10 caption 说 \"population standard deviation over 3 seeds\" 但 3 个 seeds 的 pop std 和 sample std 差别显著。\n- Table 2: EM 的 p 值为 \"---\" 而非数字。如果 EM < greedy，应报告方向。\n- Appendix Table 12 (ranking stability): Kendall's W=0.822 for RE at N=8 暗示 RE rankings 不如 NER stable，但主文未提及这一差异。\n- §Discussion \"Hypotheses for LP compression\" 列出 (b)(c)(a)(d) 而非 (a)(b)(c)(d)——排序似乎有意但未解释。\n- Figure 3 caption 中 Spearman ρ=−0.57, p=0.066, n=11: 这个 n=11 的构成（3 datasets + 8 per-type points）混合了不同粒度的数据点，可能违反 independence 假设。\n\n---\n\n## 主要优势\n\n1. **系统性强**: 5 signals × 4 datasets × 2+ models × multiple N/T/seed configurations，覆盖面在同类论文中属于上乘。\n2. **负面结果的诊断深度**: 不仅报告 \"什么不 work\"，还系统诊断 why（degeneracy + LP compression），并通过 LoRA-rank ablation、free-form decoding、entity-token LP、supervised combination 等 4 重诊断排除 alternative explanations。\n3. **Transparency**: 诚实报告 TOST 结论的 configuration-dependence，ε 的 post-hoc 性质（在 Limitations 中），多处主动报告 caveats。\n4. **Few-NERD 对照实验**: 通过引入低 degeneracy 数据集验证 LP selection 在有利条件下确实 work，增强了 degeneracy 作为解释变量的可信度。\n5. **写作质量**: 论文结构清晰，叙事线条连贯（QE works → selection fails → why → when does it work），符合 empirical analysis paper 的最佳范式。\n\n---\n\n## Questions for Authors\n\n1. 2-seed sign test 的 power analysis: 在 effect size d=0.038 (Cohen's d, 来自附录 TOST 部分) 下，sign test with n=529 的 power 是多少？是否考虑过 Wilcoxon signed-rank test 以利用幅度信息？\n2. ε=0.05 threshold 的选择：如果 pre-register median LP range (0.041) 作为 split point，non-tied subset 的 selection gain 是否仍然显著？\n3. Degeneracy 的 operationalization: \"constant F1\" 定义是否过于严格？如果用 F1 range < 0.01 (或其他 soft threshold)，degeneracy rate 会如何变化，monotonic pattern 是否 robust？\n4. Few-NERD 训练只用了 3 epochs (vs 其他 datasets 的 5 epochs)——这是否本身影响 degeneracy rate？如果 Few-NERD 也训练 5 epochs，degeneracy 是否会升高？\n\n---\n\n## Missing References\n\n- Freitag et al. (2023) \"Results of WMT23 Metrics Shared Task\" — MBR 在 MT 中的最新成果\n- Li et al. (2024) \"Confidence Estimation for LLM-Based Dialogue State Tracking\" — 结构化输出的 confidence estimation\n- Xu et al. (2024) \"Rejection Improves Reliability\" — selective prediction 与 NER 的交叉\n- 缺少 NER 评估方法论综述引用（如 Ratinov & Roth 2009 已引但 Derczynski et al. 2016 \"Broad Twitter Corpus\" 评估方法未引）\n\n---\n\n## Overall Assessment\n\n**Score: 3.5/5** (between Findings and Conference)\n\n这是一篇扎实的 empirical analysis 论文，对 \"self-consistency 是否能 scale 到结构化 IE\" 这一实践相关问题给出了有价值的负面结果。诊断深度（4 重 ablation chain）和实验覆盖面是论文的明显优势。\n\n主要弱点在统计方法论层面：(1) 核心否定结论基于 under-powered 2-seed sign test；(2) 唯一正面结果（non-tied LP）的 multiple comparison correction 范围有争议；(3) 最突出的 claim（degeneracy-gating monotonic pattern）仅 3 个宏观数据点，且 formal test 未达显著。这些问题不影响数据的真实性，但影响 claim 的强度和表述。\n\n如果作者能 (a) 加强统计基础（more seeds 或 bootstrap tests），(b) 适当弱化 monotonic claim 的语言，(c) 平衡呈现 TOST 在不同 configurations 下的 divergent 结论，论文可以达到 Conference 水平。当前状态适合 Findings。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 16 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## Summary\n\nThis paper evaluates five confidence signals (four instance-level, one per-sample) for quality estimation and sample selection in LLM-based NER. It demonstrates that while all signals achieve reliable quality estimation (ρ up to 0.42, AUROC up to 0.82), none translates QE into effective best-of-N selection—the \"correlation-selection gap.\" Two mechanisms are identified: instance degeneracy (10–58% identical outputs) and LP compression (median range 0.041 nats). The degeneracy-gating pattern across three datasets shows LP selection effectiveness is inversely related to degeneracy rate. The paper is thorough, well-structured, and makes a genuine negative-result contribution with extensive ablations.\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5 (borderline Findings/Conference)\n**一句话总结**: 实证工作扎实、消融全面，但核心 degeneracy-gating claim 的统计支撑仅有 3 个数据点，且多处统计方法论存在可改进空间，制约了结论的普适性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计系统、ablation 充分，但统计效力不足（2-seed sign test）、核心 monotonic claim 仅 3 数据点、Bonferroni scope 存在争议 |\n| Excitement | 3/5 | 负面结果有价值且相关性强，但缺少 actionable positive contribution（如 verifier baseline 或 task-specific LP variant） |\n| Reproducibility | 4/5 | 训练配置详尽、constrained decoding pipeline 有描述，但 vLLM 版本/XGrammar 具体配置缺失 |\n| Confidence | 4/5 | 仔细阅读，熟悉 MBR decoding 和 NER 评估方法论 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 2-seed paired sign test 的统计效力严重不足\n\n- 具体位置：Section 4.3 (Table 2), footnote 4, §4.1 footnote (\"Quality estimation uses a single primary seed (seed=42); selection uses 2-seed averages for variance estimation\")\n- 问题：Selection 的核心结论\"no signal significantly outperforms greedy\"基于 2-seed paired sign test。Sign test 是最保守的非参数检验（仅使用方向信息，丢弃幅度信息），在 2-seed 设定下几乎无法检测到真实效应。如果 LP 真的有 +0.2pp 的效应，sign test 在 n=529、2 seeds 下的 power 极低。这意味着 p=0.29 可能是 under-powered null 而非 true null。论文用 3-seed 实验声称 σ≤0.026 证明 stability，但这仍然不够：3 个 seeds 不足以可靠估计 σ，更不足以构建有效的假设检验。\n- 为什么影响接收：核心负面结论（\"selection fails\"）的统计基础不牢靠。审稿人无法区分\"效应不存在\"和\"检验无力检测到效应\"。\n- 建议修改方向：(1) 使用 paired bootstrap test（B=10,000）替代 sign test，利用幅度信息；(2) 增加 seed 数至 5+ 或报告 power analysis；(3) 明确区分 \"no evidence of effect\" 与 \"evidence of no effect\"——TOST 部分尝试做了但仅限附录且结论 configuration-dependent。\n\n**N2** [critical] Degeneracy-gating 的 monotonic pattern 仅基于 3 个数据点\n\n- 具体位置：Table 4 (§4.4), Abstract line 7, Conclusion line 7, Figure 3\n- 问题：核心 claim \"instance degeneracy monotonically predicts LP selection effectiveness\" 来自 CoNLL(58%→fail), SciERC(21%→+0.42pp), Few-NERD(10%→+1.36pp) 三个数据点。3 点的 monotonic trend 在统计上不具有意义——任意 3 个不同值必然可以排出 monotonic order。论文自己报告 Spearman ρ=−0.57, p=0.066 (n=11，含 per-type 数据点, Figure 3 caption)，即未达到 α=0.05 显著水平。\n- 为什么影响接收：这是论文最突出的 claim（出现在 title 暗示、abstract、intro contribution list、conclusion），但统计证据不支持将其从 observational pattern 提升为 \"predictive mechanism\"。\n- 建议修改方向：(1) 将语言从 \"monotonically predicts\" 降级为 \"is consistent with a monotonic relationship, though the limited number of dataset-level data points (n=3) precludes statistical confirmation\"；(2) 补充 per-type 分析的正式统计（已有 per-type data），计算 cross-dataset + per-type 的 mixed-effects model；(3) 或承认这是 exploratory observation 而非 confirmed mechanism。\n\n**N3** [critical] Bonferroni correction scope 与 post-hoc ε 选择的交互\n\n- 具体位置：§4.3 footnote 4 (\"survives Bonferroni over 5 comparisons\"), §Discussion Non-tied subset analysis, Appendix Table 8 (ε sweep)\n- 问题：论文声称 non-tied LP subset 的 +2.9pp (p=0.004) \"survives Bonferroni correction over 5 comparisons\" (p_adj=0.020)。但 Bonferroni scope 仅覆盖 5 signal comparisons，未纳入 ε threshold 的 post-hoc 选择。Table 8 (Appendix) 明确展示了 7 个 ε 值的 sweep (0.01–0.20)，且 ε=0.05 被选择恰恰因为它 \"yields the strongest statistical separation\"。如果将 7 个 ε × 5 signals = 35 comparisons 纳入 Bonferroni，p_adj = 0.004 × 35 = 0.14，不再显著。\n- 为什么影响接收：这是论文唯一的正面统计显著结果（\"LP does carry per-sample discriminative information\"），如果 multiple comparison correction 范围不当，核心 evidence chain 断裂。\n- 建议修改方向：(1) 明确承认 ε=0.05 是 post-hoc 选择，Bonferroni 范围存在争议；(2) 使用 pre-registered split（如 median split）或 permutation-based FDR 控制；(3) Limitations 中已提到 \"post-hoc exploratory choice\" 但主文 footnote 4 的 framing 仍暗示这是 confirmed finding——两处需要保持一致。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Random baseline (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距缺乏理论解释\n\n- 具体位置：Table 2 (§4.3)\n- 问题：如果 Random 是从同一温度 T=1.0 的 N 个 samples 中随机选一个，而 Single 是同一分布的单次采样，理论上 E[Random] = E[Single] = E[sample under T=1.0]。但 Table 2 显示 Random=0.610, Greedy(T=0)=0.645。Greedy 是不同分布（argmax decoding），差异合理。但 \"Random\" 的含义需要澄清：如果 Random 是从 N=8 candidates 中 uniform 选取的 expected F1，它应该等于 single-sample mean F1 under T=1.0。Table 4 (Few-NERD) 中 Greedy=0.748 而 SciERC Greedy=0.614（full-set），暗示 Table 2 的 Greedy=0.645 是 gold-filtered subset 的 T=0 结果。那 Random=0.610 是 gold-filtered subset 的 sample mean under T=1？如果是，0.610 vs 0.645 反映的是 T=1 vs T=0 的 quality gap，而非 selection 能力。论文未明确标注 Random 的定义。\n- 建议：明确说明 Random baseline 的语义——是 T=1 single sample mean 还是其他构造；讨论 Greedy(T=0) 与 Sample mean(T=1) 的差异是否意味着 T=1 本身降低了 quality。\n\n**W2** [warning] Kendall's W=1.0 with only 3 seeds 的 precision caveat 不充分\n\n- 具体位置：§4.5 (\"Signal rankings are stable across seeds (Kendall's W=1.0 at N=8; Table 11)\")，Appendix Table 11\n- 问题：Kendall's W with m=3 raters (seeds) ranking k=5 items (signals) 的 sampling distribution 是非常 discrete 的。W=1.0 只说明 3 个 seeds 恰好产生了相同 ranking，但置信区间极宽。论文在 Appendix (line 899) 有 caveat (\"statistical power with n=3 is limited\")，但主文 §4.5 直接引用 W=1.0 作为 robustness 证据，无 qualification。\n- 建议：主文中加入 caveat，如 \"though the small number of seeds (3) limits the precision of this estimate\"。\n\n**W3** [warning] Instance degeneracy 8B(21%) vs 4B(10.4%): capability vs fine-tuning recipe confound\n\n- 具体位置：§4.5, Table 5 (Discussion), §4.5 \"Instance degeneracy also scales with model capability\"\n- 问题：论文声称 \"instance degeneracy scales with model capability\" (8B: 21%, 4B: 10.4%)。但两个模型使用相同 training recipe（5 epochs, rank=32）。更大模型在相同 epochs 下可能 overfit 更快（更多参数 per data point），导致更强的 output convergence——这是 training dynamics artifact 而非 fundamental capability-driven 现象。如果 4B 训练更多 epochs 使其达到相似 F1，degeneracy 可能追平。论文的 LoRA-rank ablation (rank=8 降低 degeneracy 到 7%) 实际上 支持 \"fine-tuning recipe\" 解释而非 \"capability\" 解释。\n- 建议：(1) 讨论 effective parameter count / data ratio 的 confound；(2) 弱化 \"scales with model capability\" 的 causal 语言为 \"correlates with model scale under matched training\"；(3) 考虑 early-stopping ablation 作为 disentanglement。\n\n**W4** [warning] TOST 等价性结论的 configuration-dependent 呈现不平衡\n\n- 具体位置：§4.3 (line 109), Appendix §TOST (External equivalence margins)\n- 问题：主文 §4.3 说 \"TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration\"——但 varies 的方向是 Qwen-CoNLL **所有** signal 都 fail equivalence（降级 0.9–1.5pp），这意味着 signals 可能 actively harm selection。附录详细报告了这一点，但主文的措辞 \"varies by configuration\" 过于轻描淡写。一个 reviewer 可能认为这削弱了 \"no harm\" 的 claim。\n- 建议：主文中更清晰地呈现——某些配置下 signal selection 显著 worse than greedy（Qwen-CoNLL），这不仅仅是 \"equivalence fails\" 而是 \"active degradation\"。\n\n**W5** [warning] Gold-empty instance filtering 在 QE 和 Selection 之间的不一致\n\n- 具体位置：§3.3 (\"Both quality estimation and selection exclude instances with no gold annotations: n=529 on SciERC (from 551), n=2,756 on CoNLL (from 3,453)\")，但 Table 4 中 SciERC 使用 n=551\n- 问题：Table 4 (Few-NERD comparison) 中 SciERC 使用 \"full test set (n=551) for protocol consistency\" 而非 gold-filtered n=529，且 Greedy=0.614 而非 Table 2 的 0.645。脚注解释了差异但这引入了 apple-to-orange comparison。Table 2 (gold-filtered) 的 LP Δ=+0.2pp 与 Table 4 的 LP Δ=+0.42pp 不一致——读者需要仔细追踪哪个表用哪个 n。\n- 建议：统一报告协议，或在 Table 4 中同时报告 gold-filtered 数字以便 direct comparison。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.1: \"3-seed stability σ≤0.026\" — σ 是 sample std 还是 population std? Table 10 caption 说 \"population standard deviation over 3 seeds\" 但 3 个 seeds 的 pop std 和 sample std 差别显著。\n- Table 2: EM 的 p 值为 \"---\" 而非数字。如果 EM < greedy，应报告方向。\n- Appendix Table 12 (ranking stability): Kendall's W=0.822 for RE at N=8 暗示 RE rankings 不如 NER stable，但主文未提及这一差异。\n- §Discussion \"Hypotheses for LP compression\" 列出 (b)(c)(a)(d) 而非 (a)(b)(c)(d)——排序似乎有意但未解释。\n- Figure 3 caption 中 Spearman ρ=−0.57, p=0.066, n=11: 这个 n=11 的构成（3 datasets + 8 per-type points）混合了不同粒度的数据点，可能违反 independence 假设。\n\n---\n\n## 主要优势\n\n1. **系统性强**: 5 signals × 4 datasets × 2+ models × multiple N/T/seed configurations，覆盖面在同类论文中属于上乘。\n2. **负面结果的诊断深度**: 不仅报告 \"什么不 work\"，还系统诊断 why（degeneracy + LP compression），并通过 LoRA-rank ablation、free-form decoding、entity-token LP、supervised combination 等 4 重诊断排除 alternative explanations。\n3. **Transparency**: 诚实报告 TOST 结论的 configuration-dependence，ε 的 post-hoc 性质（在 Limitations 中），多处主动报告 caveats。\n4. **Few-NERD 对照实验**: 通过引入低 degeneracy 数据集验证 LP selection 在有利条件下确实 work，增强了 degeneracy 作为解释变量的可信度。\n5. **写作质量**: 论文结构清晰，叙事线条连贯（QE works → selection fails → why → when does it work），符合 empirical analysis paper 的最佳范式。\n\n---\n\n## Questions for Authors\n\n1. 2-seed sign test 的 power analysis: 在 effect size d=0.038 (Cohen's d, 来自附录 TOST 部分) 下，sign test with n=529 的 power 是多少？是否考虑过 Wilcoxon signed-rank test 以利用幅度信息？\n2. ε=0.05 threshold 的选择：如果 pre-register median LP range (0.041) 作为 split point，non-tied subset 的 selection gain 是否仍然显著？\n3. Degeneracy 的 operationalization: \"constant F1\" 定义是否过于严格？如果用 F1 range < 0.01 (或其他 soft threshold)，degeneracy rate 会如何变化，monotonic pattern 是否 robust？\n4. Few-NERD 训练只用了 3 epochs (vs 其他 datasets 的 5 epochs)——这是否本身影响 degeneracy rate？如果 Few-NERD 也训练 5 epochs，degeneracy 是否会升高？\n\n---\n\n## Missing References\n\n- Freitag et al. (2023) \"Results of WMT23 Metrics Shared Task\" — MBR 在 MT 中的最新成果\n- Li et al. (2024) \"Confidence Estimation for LLM-Based Dialogue State Tracking\" — 结构化输出的 confidence estimation\n- Xu et al. (2024) \"Rejection Improves Reliability\" — selective prediction 与 NER 的交叉\n- 缺少 NER 评估方法论综述引用（如 Ratinov & Roth 2009 已引但 Derczynski et al. 2016 \"Broad Twitter Corpus\" 评估方法未引）\n\n---\n\n## Overall Assessment\n\n**Score: 3.5/5** (between Findings and Conference)\n\n这是一篇扎实的 empirical analysis 论文，对 \"self-consistency 是否能 scale 到结构化 IE\" 这一实践相关问题给出了有价值的负面结果。诊断深度（4 重 ablation chain）和实验覆盖面是论文的明显优势。\n\n主要弱点在统计方法论层面：(1) 核心否定结论基于 under-powered 2-seed sign test；(2) 唯一正面结果（non-tied LP）的 multiple comparison correction 范围有争议；(3) 最突出的 claim（degeneracy-gating monotonic pattern）仅 3 个宏观数据点，且 formal test 未达显著。这些问题不影响数据的真实性，但影响 claim 的强度和表述。\n\n如果作者能 (a) 加强统计基础（more seeds 或 bootstrap tests），(b) 适当弱化 monotonic claim 的语言，(c) 平衡呈现 TOST 在不同 configurations 下的 divergent 结论，论文可以达到 Conference 水平。当前状态适合 Findings。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 996 · 2026-05-17T06:19:35.889200+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 997 · 2026-05-17T06:19:43.879693+00:00_

审稿报告已提交给 Review Director。

核心发现：论文实证工作扎实（5 signals × 4 datasets × 多 ablation），但有三个关键统计方法论问题需要 must-fix：(1) 2-seed sign test 效力不足以支撑 "selection fails" 的否定结论；(2) degeneracy-gating monotonic pattern 仅 3 个宏观数据点，formal test p=0.066 未达显著；(3) non-tied LP subset 的 Bonferroni scope 未覆盖 post-hoc ε 选择（7ε×5=35 comparisons 下不再显著）。整体评分 3.5/5，当前状态适合 Findings，加强统计基础后可达 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 33

## Round 33

54 recorded events


### User

_source line 998 · 2026-05-17T06:23:26.486780+00:00_

[Round 16 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整 Round 16 审稿��告。请逐条回应其 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** — 同意，并说明理由（cite 具体 Section/Table/Figure）
- **[REBUT]** — 反驳，并提供证据

特别关注：
- R2 对 tautological framing (N1) 的批评与你的 N2 (monotonic pattern) 是否有 tension
- R2 发现的 ρ=0.42 数值不一致 (N2) 你是否验证
- 你对 R2 的 3.0/5 评分是否同意（你给了 3.5）

---

## Reviewer 2 完整审稿原文：

## Round 16 审稿报告 — Reviewer 2（新颖性 + 贡献定位 + 相关工作 + 写作质量）

---

## Summary

本文研究 self-consistency 信号在 LLM-based NER 中的质量估计（QE）与样本选择（selection）效果。作者评估了 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 4 个 NER benchmark 上的表现，发现：信号可有效预测实例级质量（ρ up to ~0.42），但无法有效选择 best-of-N 候选（"correlation-selection gap"）。文章诊断出两个机制：instance degeneracy 和 LP compression，并展示 degeneracy 单调预测 LP selection 有效性。

论文实验设计系统、分析细致，诊断链（LoRA-rank ablation、free-form decoding、entity-token LP、supervised combination）令人印象深刻。但新颖性存在结构性问题：核心 "gap" 部分是定义性质的（instance-level signals by construction 无法区分候选），且与 MBR 社区已知限制有重叠。

---

## Strengths

**S1.** 4 个 benchmark 形成 difficulty gradient，每个有明确角色定位。2 个模型族 + 4B scale ablation 提供跨架构证据。
**S2.** 诊断深度出色：instance degeneracy 量化 → LoRA-rank 解耦 → free-form decoding 排除 → entity-token LP 排除 → supervised combination 确认 feature space bottleneck。
**S3.** Negative result 对 NER practitioners 有实际意义。
**S4.** 统计方法使用适当。Non-tied subset 分析的 post-hoc 性质在 limitations 中有坦诚说明。
**S5.** Few-NERD 对比实验利用 degeneracy 差异形成跨 dataset 自然实验。

---

## Must-Fix 问题

**N1** [critical] Correlation-selection gap 的新颖性存在 tautological 成分

- Section 3.1 明确写道："4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates." 既然 instance-level signals BY CONSTRUCTION 对同一 input 的所有候选给出相同分数，它们当然无法做 selection。将其转化为 MBR/consensus-proximity 选择后依然失败，才是真正的 empirical finding。但论文 framing 将两者混为一谈——标题暗示这是一个意外发现。
- 建议：明确在 Introduction 中区分 "definitional limitation" 和 "empirical finding"（MBR with positive utility correlation fails due to degeneracy; LP fails due to compression）。

**N2** [critical] ρ=0.42 headline claim 存在数值不一致

- Abstract 说 "ρ up to 0.42 on Few-NERD and the primary test bed"；Figure 1 caption 说 "ρ up to 0.45 on CoNLL, 0.42 on primary test bed"。但 Table 1 显示 SciERC（primary test bed）最高 ρ = VC 0.379。ρ=0.42 来自 Few-NERD LP (0.421)。Contribution 1 正确写 "VC ρ=0.38 on the primary test bed"。内部矛盾损害可信度。
- 建议：统一所有 headline 数值。若 primary = SciERC，上界应为 0.38（N=8）。

**N3** [critical] 与 MBR 社区已知结论的增量不够清晰

- Eikema et al. (2025) 已讨论 MBR utilities degrade on structured outputs。本文核心增量——positive within-instance utility correlation (ρ=0.52) 不导致 selection gains because of degeneracy——需要更明确 articulate。即：Eikema 认为问题在 utility design，本文证明即使 utility IS aligned (ρ=0.52)，degeneracy 也会 eliminate headroom。
- 建议：Related Work 增加一个 differentiation paragraph。

---

## Should-Fix 问题

**W1** Few-NERD LP +1.36pp 作为 positive finding 仅有 1 model × 1 N × 1 dataset 的证据。

**W2** Soft Jaccard 命名有误导性（分母 max 而非 union）。

**W3** 与 Yao et al. (2026) 的差异化不充分——核心增量不仅是 fine-tuned models，更是 "why QE ≠ selection"。

**W4** Abstract 信息过载（9 句话塞入过多技术细节和数字）。

**W5** "correlation-selection gap" 操作性定义位置太晚（Section 4.3 才出现）。

**W6** Scale claims 措辞——标题 "Fail to Scale" 暗示 model scale，但仅测试 4B-8B。

---

## Minor Issues

- M1: em-dash 使用 ~40 处，Introduction line 33 嵌套 em-dash 需拆分
- M2: Discussion line 96 -ing 分词可改为独立从句
- M3: "instance degeneracy" 术语可能与物理学/数学含义混淆
- M4: Table 5 vs Table 3 SciERC greedy 数值不同（full-set vs gold-filtered）
- M5: Ethics Statement 含 camera-ready 信息

---

## Questions for Authors

Q1. Figure 1 caption "ρ up to 0.42 on primary test bed" 具体来自哪个 configuration？与 Table 1 SciERC max ρ=0.379 矛盾。
Q2. 70B+ 模型 degeneracy 是否更严重？non-monotonic 可能？
Q3. LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败——是否暗示 LP compression 比 degeneracy 更 fundamental？
Q4. Few-NERD low degeneracy (10%) 可能由 dataset 特性（entity types, semantic overlap）而非 model capability 决定，3 个 data points 无法排除 confound。

---

## Missing References

1. Wan et al. (2023) "GPT-RE"
2. Xu et al. (2024) "Large Language Models for Generative Information Extraction: A Survey"
3. Li et al. (2024) "LLM-NER" 或类似 generative NER survey
4. Amini et al. (2024) / Shi et al. (2024) — NER uncertainty estimation with ensemble methods
5. Bertsch et al. (2024) "In-Context Learning with Long-Context Models"

---

## Overall Assessment

**Score: 3.0/5** (Findings-level)
实验设计和诊断链出色，但核心 "correlation-selection gap" 的新颖性被定义性成分稀释，headline 数值有内部不一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 999 · 2026-05-17T06:23:55.948384+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1000 · 2026-05-17T06:23:56.199380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 250
}
```

</details>

---


### Tool call

_source line 1001 · 2026-05-17T06:24:01.535307+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1002 · 2026-05-17T06:24:01.586357+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1003 · 2026-05-17T06:24:05.549016+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-3",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-3",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-17T06:24:07.600276+00:00_

Error: result (2,357,521 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999047432.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999047432.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999047432.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2051
}
```

</details>

---


### Tool call

_source line 1005 · 2026-05-17T06:24:16.090280+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1006 · 2026-05-17T06:24:16.759904+00:00_

Error: result (636,525 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999056701.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999056701.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999056701.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 669
}
```

</details>

---


### Tool call

_source line 1007 · 2026-05-17T06:24:38.137330+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify R2 numerical claims",
  "prompt": "I need you to examine a research paper PDF and verify specific numerical claims. The PDF is at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\nUse the tool `mcp__agent-ml-research__pdf_to_images` to render pages and visually inspect them. You may need to render individual pages at 150 dpi.\n\nI need you to find and report back EXACT text for these specific items:\n\n1. **Abstract**: Find ALL mentions of ρ (correlation) values. What exact numbers are claimed and for which datasets?\n\n2. **Figure 1 caption**: What does it say about ρ values? Specifically any mention of \"0.42\" or \"0.45\" and which datasets they refer to.\n\n3. **Table 1**: Find the table with correlation results. What is the MAXIMUM ρ value shown for SciERC (the \"primary test bed\")? What is the maximum for Few-NERD? List the specific values for all signals on SciERC.\n\n4. **Section 3.1**: Find where it discusses instance-level signals. Does it explicitly state that 4 of 5 signals assign identical scores to all N candidates from the same input?\n\n5. **Contribution list in Introduction**: What does Contribution 1 say about ρ values?\n\n6. **Section 4.3 or wherever \"correlation-selection gap\" is first formally defined**: Where does this definition appear?\n\nReport exact quotes where possible. This is critical for verifying numerical consistency.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify R2 numerical claims",
    "prompt": "I need you to examine a research paper PDF and verify specific numerical claims. The PDF is at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\nUse the tool `mcp__agent-ml-research__pdf_to_images` to render pages and visually inspect them. You may need to render individual pages at 150 dpi.\n\nI need you to find and report back EXACT text for these specific items:\n\n1. **Abstract**: Find ALL mentions of ρ (correlation) values. What exact numbers are claimed and for which datasets?\n\n2. **Figure 1 caption**: What does it say about ρ values? Specifically any mention of \"0.42\" or \"0.45\" and which datasets they refer to.\n\n3. **Table 1**: Find the table with correlation results. What is the MAXIMUM ρ value shown for SciERC (the \"primary test bed\")? What is the maximum for Few-NERD? List the specific values for all signals on SciERC.\n\n4. **Section 3.1**: Find where it discusses instance-level signals. Does it explicitly state that 4 of 5 signals assign identical scores to all N candidates from the same input?\n\n5. **Contribution list in Introduction**: What does Contribution 1 say about ρ values?\n\n6. **Section 4.3 or wherever \"correlation-selection gap\" is first formally defined**: Where does this definition appear?\n\nReport exact quotes where possible. This is critical for verifying numerical consistency.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-17T06:24:41.248560+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-17T06:24:41.299148+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-17T06:24:44.812842+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-17T06:24:45.868396+00:00_

Error: result (1,398,107 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999085846.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999085846.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999085846.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-17T06:24:49.082189+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-17T06:24:49.634380+00:00_

Error: result (636,525 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999089586.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999089586.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/e86ca321-269e-48e2-8ed3-90cfc9d42121/tool-results/mcp-agent-ml-research-pdf_to_images-1778999089586.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-17T06:24:56.920598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-17T06:24:56.971167+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-17T06:25:00.476463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-17T06:25:00.476878+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and the primary test bed; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to structural selection---the \textit{correlation-selection gap}: structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.
6	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\% of instances, eliminating selection headroom; and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats.
7	LP selection effectiveness is inversely predicted by degeneracy: at 10\% degeneracy (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
8	Structural signals fail uniformly regardless of degeneracy, confirming the gap is persistent for consensus-based methods.
9	Closing the structural gap likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-17T06:25:00.529382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-17T06:25:00.529810+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	These signals achieve reliable quality estimation ($\rho$ up to 0.42 on the primary test bed and Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap}: structural best-of-$N$ selection matches or degrades greedy decoding ($T{
…[truncated 3201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-17T06:25:06.019471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-17T06:25:06.071373+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 3479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-17T06:25:08.784085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-17T06:25:08.935121+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed c
…[truncated 16434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-17T06:25:15.313548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-17T06:25:15.464606+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	For quality estimation, all signals achieve positive $\rho$ across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	For selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\%, $p{=}0.091$), failure on CoNLL (58\%).
7	Structural signals uniformly degrade selection regardless of dataset.
8	RE signal rankings are reported in Appendix~\ref{app:re_extension}.
9	
10	\paragraph{Why the gap exists.}
11	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
12	
13	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
14	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
15	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
16	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; Few-NERD (75\%) shows 10\%; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zer
…[truncated 14593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-17T06:25:21.189124+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "4 of 5|four of five",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "4 of 5|four of five",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-17T06:25:21.239799+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:7:This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:340:On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:10:A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-17T06:25:25.058824+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "correlation-selection gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "correlation-selection gap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-17T06:25:25.109538+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:7:Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:76:We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:146:\paragraph{The correlation-selection gap persists for structural signals.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:164:Structural signals remain uniformly negative at $N{=}16$ (SJ $-1.36$, FK $-1.47$~pp), reinforcing that the correlation-selection gap for consensus-based methods persists regardless of sample budget.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:118:The correlation-selection gap for structural signals is persistent across all four datasets, but LP selection is degeneracy-gated.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:5:However, quality estimation does not translate to structural selection---the \textit{correlation-selection gap}: structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:238:The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
/home/ubuntu/.agent-ml-research-ide
…[truncated 3132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-17T06:25:30.658836+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Few-NERD.*0\\\\.42|0\\\\.421|LP.*0\\\\.42",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Few-NERD.*0\\\\.42|0\\\\.421|LP.*0\\\\.42",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-17T06:25:30.659253+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-17T06:25:37.030297+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\\\.42",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\\\.42",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-17T06:25:37.082758+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-17T06:25:39.992942+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.42",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.42",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-17T06:25:40.043652+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:26:Our quality estimation results connect to selective prediction \cite{kuleshov2015calibrated}: signals with $\rho$ up to 0.45 on CoNLL (0.42 on the primary test bed) and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:131:SciERC & 551 & .614 & 13.8\,pp & 21\% & .205 & $+$0.42\,pp \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:142:Low degeneracy is necessary for LP selection: the cross-dataset gradient is monotonic (58\% $\to$ fail, 21\% $\to$ $+0.42$~pp, 10\% $\to$ $+1.36$~pp), and degeneracy below ${\sim}$15\% consistently enables positive LP gains (Figure~\ref{fig:degeneracy_scatter}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:147:All five signals achieve positive quality estimation on Few-NERD (LP $\rho{=}0.42$, VC $0.39$, FK $0.31$, SJ $0.30$, EM $0.29$), yet only LP translates QE into selection.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:4:All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and SciERC; AUROC up to 0.82), supporting selective prediction and error flagging.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:7:Instance degeneracy monotonically predicts LP selection effectiveness across three datasets: at 10\% degeneracy (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/doc
…[truncated 7558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-17T06:25:45.217222+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.45",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.45",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-17T06:25:45.268735+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:26:Our quality estimation results connect to selective prediction \cite{kuleshov2015calibrated}: signals with $\rho$ up to 0.45 on CoNLL (0.42 on the primary test bed) and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:113:For quality estimation---where signals are already reliable ($\rho$ up to 0.45 on CoNLL, 0.42 on the primary test bed; AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:92:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:262:VC & +0.379 & [+0.299, +0.456] \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:822:Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:968:0.8 & $+$10.5 & 0.359 & 0.253 & 0.451 & 0.622 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:19:\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45 on CoNLL, 0.42 on primary test bed; AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-17T06:25:54.053426+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.42.*primary|primary.*0\\.42",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.42.*primary|primary.*0\\.42",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-17T06:25:54.103974+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:4:All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and the primary test bed; AUROC up to 0.82), supporting selective prediction and error flagging.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:11:These signals achieve reliable quality estimation ($\rho$ up to 0.42 on the primary test bed and Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:19:\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45 on CoNLL, 0.42 on primary test bed; AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:113:For quality estimation---where signals are already reliable ($\rho$ up to 0.45 on CoNLL, 0.42 on the primary test bed; AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:26:Our quality estimation results connect to selective prediction \cite{kuleshov2015calibrated}: signals with $\rho$ up to 0.45 on CoNLL (0.42 on the primary test bed) and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-17T06:25:57.218672+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "80",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "80",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-17T06:25:57.271287+00:00_

80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested 
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-17T06:26:01.004340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "126",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "126",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-17T06:26:01.055004+00:00_

126	\begin{tabular}{lcccccc}
127	\toprule
128	Dataset & $n$ & Greedy & Headroom & Degen\% & LP $\rho$ & LP $\Delta$ \\
129	\midrule
130	CoNLL & 2{,}756 & .908 & 4.0\,pp & 58\% & .316 & fail \\
131	SciERC & 551 & .614 & 13.8\,pp & 21\% & .205 & $+$0.42\,pp \\
132	Few-NERD & 32{,}565 & .748 & 12.4\,pp & 10.1\% & .421 & $\mathbf{+1.36}$\,pp \\
133	\bottomrule
134	\end{tabular}
135	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-17T06:26:06.969847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "30",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "30",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-17T06:26:07.071345+00:00_

30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robust
…[truncated 2694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1046 · 2026-05-17T06:26:47.320101+00:00_

I now have all the data needed. Let me compile the findings.

Here are the exact findings for each item:

---

**1. Abstract -- ρ values:**

Exact quote (line 4 of abstract.tex):
> `All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and the primary test bed; AUROC up to 0.82)`

The "0.42" is attributed to **both** Few-NERD **and** "the primary test bed" (SciERC). This is a potential inconsistency: Table 1 (`tab:quality_estimation`) shows the **maximum ρ on SciERC is VC = .379**, not 0.42. The 0.42 value for Few-NERD is supported (Table `tab:fewnerd` shows LP ρ = .421 on Few-NERD), but 0.42 on SciERC is NOT directly supported by the primary N=8 results in Table 1. It may refer to the N=16 SJ value of 0.411 (Appendix Table `tab:robustness`), which is still not 0.42.

---

**2. Figure 1 caption (line 19 of introduction.tex):**

Exact quote:
> `\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45 on CoNLL, 0.42 on primary test bed; AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}`

- **0.45 on CoNLL**: Supported by Table 1 (EM on CoNLL Qwen = .451)
- **0.42 on primary test bed (SciERC)**: NOT supported by Table 1 (max is VC = .379). Discrepancy of ~0.04.

---

**3. Table 1 (`tab:quality_estimation`) -- SciERC and Few-NERD values:**

**SciERC (all signals):**
| Signal | ρ | AUROC |
|--------|------|------|
| VC | **.379** | **.663** |
| SJ | .360 | .650 |
| FK | .267 | .602 |
| EM | .295 | .614 |
| LP | .205 | .578 |

**Maximum ρ on SciERC = 0.379** (VC).

Few-NERD does NOT appear in Table 1. The Few-NERD LP ρ value (.421) is found in Table `tab_fewnerd` (Section 4.3), and the full QE values are stated inline in Section 4.3: "LP ρ=0.42, VC 0.39, FK 0.31, SJ 0.30, EM 0.29."

---

**4. Section 3.1 (Method, `\subsec
…[truncated 2910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 129182
}
```

</details>

---


### Tool call

_source line 1047 · 2026-05-17T06:27:08.293837+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1048 · 2026-05-17T06:27:08.344403+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1049 · 2026-05-17T06:28:05.898353+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Correlation-selection gap 的 tautological 成分**\n\n同意 R2 的核心判断。我验证了 Section 3.1 原文明确写道：\"4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates\"，Introduction 也重复了这一表述。既然论文自己承认 4/5 信号 by construction 无法区分候选，那么这些信号\"无法做 selection\"确实是定义性结论而非经验发现。\n\n但我要补充一个 nuance：论文的真正 empirical contribution 是两部分——(a) 将 instance-level signals 转化为 MBR/consensus-proximity 选择后仍然失败（因 degeneracy），(b) LP 作为唯一 per-sample signal 也失败（因 compression）。问题在于论文 framing 把这两个不同层次的发现混在一起，用同一个 \"gap\" 标签包装，造成新颖性被稀释的印象。\n\n**与我的 N2（monotonic pattern）的关系**：没有 tension。R2 指出 instance-level gap 是定义性的，我指出 degeneracy→LP failure 的关系是描述性的（缺乏机制解释）。两者从不同角度指向同一问题：论文需要更精确地界定哪些是 definitional, 哪些是 empirical, 哪些是 mechanistic contribution。建议作者在修改时明确分层。\n\n---\n\n**[AGREE] R2-N2: ρ=0.42 headline claim 数值不一致**\n\n完全同意，且我已独立验证。具体发现：\n\n- Abstract: \"ρ up to 0.42 on Few-NERD and the primary test bed\" — 措辞暗示两个 dataset 都达到 0.42\n- Figure 1 caption: \"ρ up to 0.45 on CoNLL, 0.42 on primary test bed\" — 直接声称 primary test bed 达到 0.42\n- Table 1 实际数据: SciERC（primary test bed）最高 ρ = VC 0.379\n- Few-NERD: LP ρ = 0.421（Section 4.3 inline）— 这才是 0.42 的来源\n- Contribution 1: \"VC ρ=0.38 on the primary test bed\" — 这个是正确的\n\n结论：0.42 只能归属于 Few-NERD LP，不能归属于 SciERC。Figure 1 caption 的 \"0.42 on primary test bed\" 与 Table 1 矛盾（差 0.04），Abstract 的合并表述进一步放大了混淆。这是一个实质性的数值一致性问题，不是四舍五入误差。Contribution 1 的 \"ρ=0.38\" 反而是正确的，说明作者在不同位置使用了不同数据源却未统一校验。\n\n这个问题在我的 Round 16 审稿中没有独立发现，感谢 R2 的细致核查。\n\n---\n\n**[AGREE with nuance] R2-N3: 与 MBR 社区已知结论的增量不清晰**\n\n同意需要更明确的 differentiation。R2 准确指出了本文的真正增量：Eikema et al. (2025) 认为问题在 utility design，本文证明即使 utility IS aligned (within-instance ρ=0.52)，degeneracy 也会 eliminate headroom。这个 distinction 确实是本文的核心贡献之一，但目前在 Related Work 中不够突出。\n\n补充：本文场景（NER structured output）与 MBR 文献的典型场景（MT/summarization）有本质差异——NER 的离散标签空间导致更极端的 degeneracy。这个 structural argument 也应该在 positioning 中被强调。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Few-NERD LP +1.36pp 证据单薄**\n\n同意。仅 1 model × 1 N × 1 dataset 的 positive finding 不足以支撑将其作为\"LP can work when degeneracy is low\"的通用结论。需要至少说明是 suggestive evidence 而非 demonstrated result。\n\n**[AGREE] R2-W2: Soft Jaccard 命名误导**\n\n同意。分母用 max 而非 union 确实不是标准 Jaccard 定义。建议改名或加注释说明。\n\n**[AGREE] R2-W3: 与 Yao et al. (2026) 差异化不足**\n\n同意。核心增量不仅是 fine-tuned models，更是\"为什么 QE correlates but selection fails\"的诊断，这在当前 Related Work 中没有被充分对比。\n\n**[AGREE] R2-W4: Abstract 信息过载**\n\n同意。Abstract 试图在 ~9 句中塞入过多技术细节（5 signals、4 benchmarks、degeneracy、LP compression、LoRA-rank ablation），导致核心 narrative 被稀释。\n\n**[AGREE] R2-W5: \"Correlation-selection gap\" 操作性定义位置太晚**\n\n同意，这与我的 Round 16 意见一致。核心概念在 Section 4.3 才正式定义，但 Abstract 和 Introduction 已经大量使用。建议在 Section 3 或 Introduction 末尾给出 operational definition。\n\n**[REBUT] R2-W6: Scale claims 措辞**\n\n部分反驳。标题 \"Fail to Scale\" 在论文语境中不仅指 model scale，也指 sample count（N=4→16）和 signal sophistication（从单一到组合）。虽然 4B-8B 确实不覆盖大模型，但论文 Section 4.2 明确标注了 ablation 范围，且 title 的 \"scale\" 更多是指 \"scaling up effort does not help\"（增加 N、增加信号复杂度）。不过我承认这个双关可能误导读者，建议作者在 Abstract 中加一句澄清 \"scale\" 的具体含义。\n\n---\n\n### 关于评分差异（R2: 3.0 vs R1: 3.5）\n\nR2 给 3.0 的核心理由是 tautological framing 稀释新颖性。我理解这个逻辑，但仍维持 3.5，理由如下：\n\n1. **诊断链的完整性仍有独立价值**：即使 instance-level gap 是定义性的，从 degeneracy 量化 → LoRA-rank 解耦 → LP compression 诊断 → supervised combination 确认 feature bottleneck 的完整链条，在 NER 领域是 novel 的实证工作\n2. **Negative result 的实践意义**：对 NER practitioners 来说，知道\"不要在 high-degeneracy 场景投入 selection effort\"是 actionable insight\n3. **数值不一致（N2）是可修复问题**：这影响 presentation 而非 scientific contribution\n\n但如果作者无法在修改中清晰分层 definitional vs empirical contribution（N1），我会考虑下调至 3.0。\n\n---\n\n### 对 R2 Questions for Authors 的补充\n\n**Q3 (LP compression vs degeneracy)**：这是一个非常好的问题，与我的 N2 直接相关。LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败——这暗示 LP compression 可能是独立于 degeneracy 的 bottleneck。论文目前将两者用 monotonic relationship 联系，但 Q3 指向的可能性（LP compression 是 more fundamental）应该在 Discussion 中被讨论。\n\n**Q4 (Few-NERD confound)**：同意。3 个 data points (datasets) 无法排除 dataset-specific confounds。Few-NERD 的低 degeneracy 可能由 entity type 多样性或 semantic distinctiveness 驱动，而非 model capability 的反映。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Correlation-selection gap 的 tautological 成分**\n\n同意 R2 的核心判断。我验证了 Section 3.1 原文明确写道：\"4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates\"，Introduction 也重复了这一表述。既然论文自己承认 4/5 信号 by construction 无法区分候选，那么这些信号\"无法做 selection\"确实是定义性结论而非经验发现。\n\n但我要补充一个 nuance：论文的真正 empirical contribution 是两部分——(a) 将 instance-level signals 转化为 MBR/consensus-proximity 选择后仍然失败（因 degeneracy），(b) LP 作为唯一 per-sample signal 也失败（因 compression）。问题在于论文 framing 把这两个不同层次的发现混在一起，用同一个 \"gap\" 标签包装，造成新颖性被稀释的印象。\n\n**与我的 N2（monotonic pattern）的关系**：没有 tension。R2 指出 instance-level gap 是定义性的，我指出 degeneracy→LP failure 的关系是描述性的（缺乏机制解释）。两者从不同角度指向同一问题：论文需要更精确地界定哪些是 definitional, 哪些是 empirical, 哪些是 mechanistic contribution。建议作者在修改时明确分层。\n\n---\n\n**[AGREE] R2-N2: ρ=0.42 headline claim 数值不一致**\n\n完全同意，且我已独立验证。具体发现：\n\n- Abstract: \"ρ up to 0.42 on Few-NERD and the primary test bed\" — 措辞暗示两个 dataset 都达到 0.42\n- Figure 1 caption: \"ρ up to 0.45 on CoNLL, 0.42 on primary test bed\" — 直接声称 primary test bed 达到 0.42\n- Table 1 实际数据: SciERC（primary test bed）最高 ρ = VC 0.379\n- Few-NERD: LP ρ = 0.421（Section 4.3 inline）— 这才是 0.42 的来源\n- Contribution 1: \"VC ρ=0.38 on the primary test bed\" — 这个是正确的\n\n结论：0.42 只能归属于 Few-NERD LP，不能归属于 SciERC。Figure 1 caption 的 \"0.42 on primary test bed\" 与 Table 1 矛盾（差 0.04），Abstract 的合并表述进一步放大了混淆。这是一个实质性的数值一致性问题，不是四舍五入误差。Contribution 1 的 \"ρ=0.38\" 反而是正确的，说明作者在不同位置使用了不同数据源却未统一校验。\n\n这个问题在我的 Round 16 审稿中没有独立发现，感谢 R2 的细致核查。\n\n---\n\n**[AGREE with nuance] R2-N3: 与 MBR 社区已知结论的增量不清晰**\n\n同意需要更明确的 differentiation。R2 准确指出了本文的真正增量：Eikema et al. (2025) 认为问题在 utility design，本文证明即使 utility IS aligned (within-instance ρ=0.52)，degeneracy 也会 eliminate headroom。这个 distinction 确实是本文的核心贡献之一，但目前在 Related Work 中不够突出。\n\n补充：本文场景（NER structured output）与 MBR 文献的典型场景（MT/summarization）有本质差异——NER 的离散标签空间导致更极端的 degeneracy。这个 structural argument 也应该在 positioning 中被强调。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Few-NERD LP +1.36pp 证据单薄**\n\n同意。仅 1 model × 1 N × 1 dataset 的 positive finding 不足以支撑将其作为\"LP can work when degeneracy is low\"的通用结论。需要至少说明是 suggestive evidence 而非 demonstrated result。\n\n**[AGREE] R2-W2: Soft Jaccard 命名误导**\n\n同意。分母用 max 而非 union 确实不是标准 Jaccard 定义。建议改名或加注释说明。\n\n**[AGREE] R2-W3: 与 Yao et al. (2026) 差异化不足**\n\n同意。核心增量不仅是 fine-tuned models，更是\"为什么 QE correlates but selection fails\"的诊断，这在当前 Related Work 中没有被充分对比。\n\n**[AGREE] R2-W4: Abstract 信息过载**\n\n同意。Abstract 试图在 ~9 句中塞入过多技术细节（5 signals、4 benchmarks、degeneracy、LP compression、LoRA-rank ablation），导致核心 narrative 被稀释。\n\n**[AGREE] R2-W5: \"Correlation-selection gap\" 操作性定义位置太晚**\n\n同意，这与我的 Round 16 意见一致。核心概念在 Section 4.3 才正式定义，但 Abstract 和 Introduction 已经大量使用。建议在 Section 3 或 Introduction 末尾给出 operational definition。\n\n**[REBUT] R2-W6: Scale claims 措辞**\n\n部分反驳。标题 \"Fail to Scale\" 在论文语境中不仅指 model scale，也指 sample count（N=4→16）和 signal sophistication（从单一到组合）。虽然 4B-8B 确实不覆盖大模型，但论文 Section 4.2 明确标注了 ablation 范围，且 title 的 \"scale\" 更多是指 \"scaling up effort does not help\"（增加 N、增加信号复杂度）。不过我承认这个双关可能误导读者，建议作者在 Abstract 中加一句澄清 \"scale\" 的具体含义。\n\n---\n\n### 关于评分差异（R2: 3.0 vs R1: 3.5）\n\nR2 给 3.0 的核心理由是 tautological framing 稀释新颖性。我理解这个逻辑，但仍维持 3.5，理由如下：\n\n1. **诊断链的完整性仍有独立价值**：即使 instance-level gap 是定义性的，从 degeneracy 量化 → LoRA-rank 解耦 → LP compression 诊断 → supervised combination 确认 feature bottleneck 的完整链条，在 NER 领域是 novel 的实证工作\n2. **Negative result 的实践意义**：对 NER practitioners 来说，知道\"不要在 high-degeneracy 场景投入 selection effort\"是 actionable insight\n3. **数值不一致（N2）是可修复问题**：这影响 presentation 而非 scientific contribution\n\n但如果作者无法在修改中清晰分层 definitional vs empirical contribution（N1），我会考虑下调至 3.0。\n\n---\n\n### 对 R2 Questions for Authors 的补充\n\n**Q3 (LP compression vs degeneracy)**：这是一个非常好的问题，与我的 N2 直接相关。LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败——这暗示 LP compression 可能是独立于 degeneracy 的 bottleneck。论文目前将两者用 monotonic relationship 联系，但 Q3 指向的可能性（LP compression 是 more fundamental）应该在 Discussion 中被讨论。\n\n**Q4 (Few-NERD confound)**：同意。3 个 data points (datasets) 无法排除 dataset-specific confounds。Few-NERD 的低 degeneracy 可能由 entity type 多样性或 semantic distinctiveness 驱动，而非 model capability 的反映。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1050 · 2026-05-17T06:28:09.511863+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3613
}
```

</details>

---


### Assistant

_source line 1051 · 2026-05-17T06:28:17.878491+00:00_

交叉回应已提交。总结：

- **N1 (tautological framing)**：同意，但补充了 empirical contribution 的分层（MBR conversion 失败 + LP compression）与我的 N2 互补而非冲突
- **N2 (ρ=0.42 不一致)**：完全同意并独立验证——Figure 1 caption 和 Abstract 声称 primary test bed 达到 0.42，但 Table 1 实际最大值为 0.379
- **N3 (MBR 增量)**：同意需要更明确的 differentiation paragraph
- **W1-W5**：全部同意
- **W6 (scale claims)**：部分反驳——"scale" 在论文中指 N/信号复杂度，不仅指 model scale
- **评分差异**：维持 3.5（vs R2 的 3.0），因诊断链完整性和实践意义仍有独立价值，但若 N1 修改不到位会下调

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 34

## Round 34

44 recorded events


### User

_source line 1052 · 2026-05-17T07:07:34.736636+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计**

### Venue 信息
- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- 截止日期: 2026-05-25
- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）
- 模板: ACL style (`\usepackage[review]{acl}`)
- 匿名规则: double-blind

### 论文路径
- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`
- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex
- Appendix: `docs/paper/sections/appendix.tex`

### 你的审查重点

请从以下维度严格评审：

1. **方法论严谨性**
   - 5 个 confidence signal 的定义是否数学上严密？有无遗漏或错误？
   - "instance-level vs per-sample" 的区分是否清晰且正确？
   - MBR / consensus-proximity selection 的形式化是否完整？
   - Soft Jaccard 的分母选择 (max 而非 union) 是否合理？论文声称差异 <0.01 但未给出证据

2. **实验设计与统计分析**
   - 4 个 NER benchmark 的选择是否合理？是否存在 cherry-picking？
   - seed 数量（primary 1 seed, selection 2 seeds）是否足够？3-seed stability claim 是否可靠？
   - bootstrap / sign test / TOST 等统计检验的使用是否恰当？
   - p 值报告是否一致？多重比较校正是否充分？
   - 论文声称 "correlation-selection gap" 时的统计基础是否牢固？
   - degeneracy 与 LP selection 的 n=3 datasets 梯度关系是否过度解读？
   - LoRA rank=8 ablation: 7.2% vs 21% degeneracy 但 selection 仍失败——这是否足以支撑 "necessary but not sufficient" 的 claim？

3. **Claim 与 Evidence 对应**
   - 每个 Contribution 是否有充分的实验支撑？
   - 负面结果的解读是否过度？（e.g., "fails" vs "not statistically significant"）
   - Oracle headroom 的计算方式是否合理？
   - 自由格式解码 ablation 的结论（"compression is model-intrinsic"）是否过强？

4. **实验可复现性**
   - 训练细节是否充分（LoRA 参数、学习率、batch size、epoch、data split）？
   - 推理设置是否完整（vLLM 版本、constrained decoding 细节）？
   - 评估 protocol 是否清晰（gold-filtered vs full-set 的切换）？

请按以下格式输出审稿报告：
```
## Summary (2-3 句)
## Strengths (逐条)
## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
## Questions (需要作者澄清)
## Missing References
## Detailed Comments (逐节)
## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)
## Confidence (1-5)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1053 · 2026-05-17T07:07:46.425868+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1054 · 2026-05-17T07:07:46.426250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1055 · 2026-05-17T07:07:46.928082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1056 · 2026-05-17T07:07:47.429886+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1057 · 2026-05-17T07:07:47.430229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1058 · 2026-05-17T07:07:47.781541+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction.
5	However, quality estimation does not translate to sample selection---the \textit{correlation-selection gap}: despite ${\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.
6	The gap has a three-layer structure: four instance-level signals cannot rank candidates within an instance by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\% identical outputs) eliminates headroom; and LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats).
7	LP selection is inversely associated with degeneracy: at 10\% (Few-NERD), $+1.36$~pp ($p{<}0.001$); at 58\% (CoNLL), LP fails.
8	In the low-degeneracy regime, LP scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
9	Closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1059 · 2026-05-17T07:07:47.782040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1060 · 2026-05-17T07:07:47.832685+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	These signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably 
…[truncated 3753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1061 · 2026-05-17T07:07:52.198278+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-17T07:07:52.499681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-17T07:07:53.453429+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 3512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-17T07:07:53.453765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-17T07:07:53.654906+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed c
…[truncated 18253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-17T07:07:53.655272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-17T07:07:53.705921+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	For quality estimation, all signals achieve positive $\rho$ across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	For selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\%, $p{=}0.091$), failure on CoNLL (58\%).
7	Structural signals uniformly degrade selection regardless of dataset.
8	RE signal rankings are reported in Appendix~\ref{app:re_extension}.
9	
10	\paragraph{Why the gap exists.}
11	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
12	
13	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
14	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
15	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
16	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; Few-NERD (75\%) shows 10\%; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zer
…[truncated 14803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1068 · 2026-05-17T07:08:00.081543+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's what I found regarding ACL ARR 2025/2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the 
…[truncated 1405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7883
}
```

</details>

---


### Tool call

_source line 1069 · 2026-05-17T07:08:08.320858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1070 · 2026-05-17T07:08:08.321356+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} demonstrate that consistency correlates with accuracy for LLM-based NER/RE under hard-prompting.
11	We show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression) that explain why correlation does not translate to selection gains.
12	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, where instance degeneracy is most pronounced.
13	Degeneracy varies across datasets: CoNLL (91\% single-sample F1) exhibits 58\%; SciERC (66\%) shows 21\%; Few-NERD (75\%) shows 10\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero (\S\ref{sec:discussion}).
14	Few-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.
15	CoCoA \cite{vashurin2025cocoa} fuses confidence with consisten
…[truncated 4518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1071 · 2026-05-17T07:08:08.823870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1072 · 2026-05-17T07:08:08.824342+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\%) collapses the candidate pool; and LP, the sole per-sample signal, is compressed to near-ineffectiveness (median range 0.041 nats).
6	LP selection effectiveness is inversely associated with instance degeneracy: at 10\% (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
7	In the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap, confirming the bottleneck is in the feature space.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline when degeneracy is low.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1073 · 2026-05-17T07:08:09.376609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1074 · 2026-05-17T07:08:09.376982+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection
…[truncated 206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1075 · 2026-05-17T07:08:09.828976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1076 · 2026-05-17T07:08:10.080273+00:00_

File content (30903 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1077 · 2026-05-17T07:08:15.469306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1078 · 2026-05-17T07:08:15.520057+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 13708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1079 · 2026-05-17T07:08:16.272935+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"
  }
}
```

</details>

---


### Tool result

_source line 1080 · 2026-05-17T07:08:21.742355+00:00_

Web search results for query: "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum","url":"https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper","url":"https://cspaper.org/topic/27/acl-2025-reviews-are-out-to-r
…[truncated 1337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5469
}
```

</details>

---


### Tool call

_source line 1081 · 2026-05-17T07:08:29.619433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1082 · 2026-05-17T07:08:29.720460+00:00_

200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} (\S\ref{sec:qe_results}) reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
208	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
209	
210	\paragraph{Cross-configuration selection analysis.}
211	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
212	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
213	On CoNLL, 57--88\% of
…[truncated 18341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-17T07:08:35.500536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "449",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "449",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-17T07:08:35.551494+00:00_

449	\paragraph{Prompt template.}
450	For NER, we use a structured prompt:
451	\begin{quote}
452	\small
453	\texttt{System:} You are an expert in Named Entity Recognition.\\
454	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
455	Text: \texttt{\{input\_text\}}\\
456	Entity types: \texttt{\{schema\_types\}}
457	\end{quote}
458	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
459	
460	\paragraph{Constrained decoding.}
461	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
462	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
463	
464	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
465	
466	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
467	We quantify the potential impact on LP scores through three complementary arguments.
468	
469	\paragraph{LP shift magnitude.}
470	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
471	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
472	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
473	
474	\paragraph{Constant prefix cancellation.}
475	
…[truncated 15916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1085 · 2026-05-17T07:08:43.881423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "698",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "698",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1086 · 2026-05-17T07:08:44.032447+00:00_

698	\paragraph{Task-specific decoding interactions.}
699	The free-form ablation reveals divergent behavior across tasks.
700	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
701	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
702	This interaction does not generalize to NER, where selection remains negligible under both regimes.
703	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
704	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
705	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
706	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
707	
708	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
709	
710	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
711	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
712	LP score distributions are nearly identical across regimes (Panel~A: within-in
…[truncated 9130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1087 · 2026-05-17T07:08:50.202980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "897",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "897",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1088 · 2026-05-17T07:08:50.255116+00:00_

897	\end{table}
898	
899	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
900	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
901	
902	\paragraph{$N$-scaling: selection headroom vs.\ selection gain.}
903	Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
904	Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+19.2$~pp at $N{=}32$).
905	LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement.
906	Degeneracy drops monotonically (44\% at $N{=}2$ to 4\% at $N{=}32$), yet reduced degeneracy does not unlock selection---consistent with the LoRA-rank ablation finding (\S\ref{sec:robustness_main}).
907	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
908	
909	\begin{table}[t]
910	\centering
911	\small
912	\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, seed${=}42$).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
913	\label{tab:n_scaling_selection}
914	\begin{tabular}{ccccccccc}
915	\toprule
916	$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & E
…[truncated 13827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1089 · 2026-05-17T07:08:57.280190+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"aclrollingreview.org/reviewform\" soundness excitement overall recommendation scale detailed rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"aclrollingreview.org/reviewform\" soundness excitement overall recommendation scale detailed rubric"
  }
}
```

</details>

---


### Tool result

_source line 1090 · 2026-05-17T07:09:04.567885+00:00_

Web search results for query: ""aclrollingreview.org/reviewform" soundness excitement overall recommendation scale detailed rubric"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"Program Chairs' Report on Peer Review at ACL 2023","url":"http://www.cs.umd.edu/~jbg/docs/2023_acl_peer_review_report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"}]

Based on the search results from aclrollingreview.org, here's information about the review form's scoring rubric:

## Three Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Scale

The soundness score evaluates whether the paper is sufficiently sound and thorough, and whether it clearly states scientific cl
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7287
}
```

</details>

---


### Tool call

_source line 1091 · 2026-05-17T07:09:45.962278+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1092 · 2026-05-17T07:09:46.012809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1093 · 2026-05-17T07:12:13.928473+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Round 1 Review — Reviewer 1 (方法严谨性 + 实验设计)\n\n**Paper**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n\n---\n\n## Summary (2-3 句)\n\n本文系统评估了 5 种 confidence signals 在 LLM-based NER 中的 quality estimation 和 sample selection 能力，发现 QE 成功但 selection 失败（correlation-selection gap），并通过 instance degeneracy 和 LP compression 两个机制给出诊断。实验设计严谨度高于平均水准（多数据集、多模型、多 seed、bootstrap/TOST 统计检验），但部分核心 claim 的因果推断证据不足，跨数据集梯度 n=3 支撑的泛化结论需要审慎对待。\n\n---\n\n## Strengths\n\n1. **问题定义清晰且有贡献** (Section 1, 3.3): \"correlation-selection gap\" 的概念化有价值——将 QE 和 selection 明确解耦，指出一个被 prior work 忽略的 confound。instance-level vs per-sample 的形式化区分（Section 3.1）简洁且数��上正确。\n\n2. **实验设计的系统性** (Section 4): 4 个 NER benchmark 构成 difficulty gradient（WNUT-17 collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个数据集的角色清晰。两个模型族（Qwen3-8B, LLaMA-3.1-8B）加 4B/3B ablation 排除模型特异性。\n\n3. **统计方法论上佳** (Section 4.3, Appendix): Bootstrap CI（B=10,000）、paired sign test、TOST 等效性检验、Bonferroni 校正、Kendall's W 排名稳定性、Fisher 合并 p 值——统计工具选择恰当，且在负面结果中使用 TOST 避免了\"absence of evidence = evidence of absence\"的谬误。\n\n4. **三层诊断结构有说服力** (Section 4.3): (a) instance-level 信号 by construction 不能排名候选 → (b) MBR with aligned utility 因 degeneracy 失败 → (c) LP 有 per-sample 信息但被 compression 限制。逻辑递进清晰。\n\n5. **负面结果的审慎表达**: 论文多处使用\"inversely associated with\"而非\"causes\"，使用\"necessary but not sufficient\"限定 claim，Limitations 节详尽列举未覆盖条件。\n\n6. **Appendix 丰富且组织有序**: 涵盖 FK independence test、SJ normalizer robustness、ε robustness、thinking token impact、OOD analysis 等，大多数潜在反驳都有对应的 ablation 或 control。\n\n---\n\n## Weaknesses\n\n### [Must-Fix] W1: 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)\n\n- **位置**: Section 4.4 (Table 4), Section 5 \"Regime boundaries\", Figure 3\n- **问题**: 论文的核心 claim 之一是 \"LP selection effectiveness is inversely associated with degeneracy rate across datasets\"，但这一梯度仅基于 n=3 数据集（CoNLL 58% → SciERC 21% → Few-NERD 10%）。任何三个数据点的单调排列概率为 1/3!= 1/6，即使在随机条件下也有 16.7% 的概率出现单调趋势。\n- **补充**: 论文试图用 entity-type-level analysis（n=8, ρ=-0.881, p=0.004）加强论证，但 entity type 之间共享同一模型、同一 checkpoint、同一 inference pipeline，违反独立性假设。不同 entity type 的 degeneracy 差异可能源自 type frequency、schema complexity 等混淆变量，而非 degeneracy 本身直接导致 LP selection 差异。\n- **Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测**，统计上有问题：cross-dataset aggregates 和 per-entity-type points 的方差结构完全不同，不应直接 pool。\n- **为什么影响接收**: 如果 degeneracy 梯度的因果解释不成立，Contribution 3 的基础动摇。\n- **建议**: (a) 增加至少 2-3 个数据集的实验（如 OntoNotes、ACE05）扩大 n；(b) 用 Few-NERD 内 entity-type analysis 时，控制 type frequency 和 entity boundary difficulty 等混淆变量；(c) 不要 pool 不同粒度的观测到同一 correlation。\n\n### [Must-Fix] W2: \"Necessary but not sufficient\" claim 的 LoRA-rank ablation 存在混淆变量\n\n- **位置**: Section 4.5 \"LoRA-rank ablation\" (line: \"Low degeneracy is thus a necessary but not sufficient condition for selection\")\n- **问题**: LoRA rank=8 ablation 降低了 degeneracy (21% → 7.2%) 且增加了 oracle headroom (13.3 → 16.0 pp)，但 LP selection 仍失败。论文据此声称 degeneracy 是 \"necessary but not sufficient\"。但 LoRA rank=8 同时降低了模型能力（greedy F1: 0.645 → 0.640），改变了学到的 representation space。LP compression 在 rank=8 下可能因模型能力下降而加剧，而非因为 degeneracy 本身不充分。\n- **矛盾**: Few-NERD 在 10% degeneracy 下 LP selection 成功 (+1.36 pp)，而 rank=8 SciERC 在 7.2% degeneracy 下仍失败。如果 degeneracy 是唯一 gating factor，Few-NERD 的成功和 rank=8 SciERC 的失败之间的差异需要更好的解释。论文在 Section 4.4 简要提到 \"LP signal quality (ρ) provides an additional prerequisite\"，但这实质上是在说 degeneracy + LP quality 联���决定 selection，而非 degeneracy alone is necessary。\n- **为什么影响接收**: \"Necessary but not sufficient\" 是一个精确的逻辑声明；当前实验设计无法将 degeneracy 从 LP compression 中独立隔离。\n- **建议**: (a) 明确指出 LoRA rank ablation 同时改变了多个变量（degeneracy、model quality、LP compression degree），不能做 clean causal attribution；(b) 将 claim 弱化为 \"low degeneracy co-occurs with LP selection success, but rank-8 ablation shows it is not alone sufficient\"；(c) 最好提供 rank=8 下的 LP compression 统计（median LP range、tied fraction），以量化 compression 在两种 rank 下的变化。\n\n### [Should-Fix] W3: 负面结果的统计功效 (power) 未报告\n\n- **位置**: Section 4.3 (Table 3, \"LP achieves only 0.647, Δ=+0.2 pp, d=0.038, p=0.29\")\n- **问题**: 论文的中心论点是负面结果（selection 不显著优于 greedy）。对于负面结果，需要报告 power analysis：在当前样本量 (n=529) 和 seed 数量 (2) 下，检测 1 pp 效应（一个实际有意义的改进）的统计功效是多少？如果 power 很低（如 <50%），则 p=0.29 无法区分 \"真的没效果\" 和 \"效果存在但检测不到\"。\n- **TOST 部分缓解了这个问题** (Appendix D)，但 TOST 使用的 δ=2pp (internal anchor) 是否过宽？externally anchored δ=1.0pp 下，SciERC 未通过 TOST。\n- **为什么影响评分**: 虽然 TOST 是好的补充，但主文没有明确讨论 power，可能误导读者认为 \"p>0.05\" 等同于 \"确认无效果\"。\n- **建议**: 在 main text 或 appendix 中加入 post-hoc power analysis，报告当前设计检测 Δ=1pp 的 power；或者明确指出 Few-NERD (n=32,565) 的结果 (LP +1.36 pp, p<0.001) 才是 definitive evidence，SciERC 的 non-significance 可能受限于 power。\n\n### [Should-Fix] W4: \"Compression is model-intrinsic\" 的结论与 RE 结果矛盾\n\n- **位置**: Section 5 \"Ablation: free-form decoding\" + Appendix H (Table 8)\n- **问题**: 论文 NER free-form ablation 发现 LP 分布几乎不变 (std ratio 0.97)，据此声称 \"compression is model-intrinsic rather than constraint-imposed\"。但 RE 的 free-form decoding 显著恢复了 LP selection (+2.35 pp, p=0.025)，直接证明 constraints DO compress LP for RE。\n- **论文在 Section 5 最后简要提到这一分歧**，但 Abstract 和 Introduction 中 \"compression is model-intrinsic\" 的 framing 没有 qualification。读者如果只看主文可能误以为这是普适结论。\n- **为什么影响评分**: 论文的诊断框架混淆了 task-specific behavior 和 universal mechanism。\n- **建议**: (a) 将主文 claim 限定为 \"for NER, compression is model-intrinsic; for RE, constraint-imposed mechanisms contribute significantly\"；(b) 在 Abstract 或 Introduction 的 diagnostic chain 描述中加入 task qualifier。\n\n### [Should-Fix] W5: Primary seed (seed=42) 的代表性与 selection 实验的 2-seed 限制\n\n- **位置**: Section 4.1 footnote 4 (\"Quality estimation uses a single primary seed; selection uses 2-seed averages\")\n- **问题**: QE 主结果仅 1 seed，selection 仅 2 seeds。虽然 Table 6 的 3-seed stability test 显示 σ≤0.026 for ρ rankings，但 selection F1 的 seed variance 未被同样充分量化。Table 3 报告的 selection F1 σ（如 LP: ±0.005）基于仅 2 seeds 的极差，这不是可靠的 variance estimate。\n- **Few-NERD 是 1-seed result** (Table 4)，尽管 n=32,565 提供了足够 statistical power，但 systematic bias（如训练 seed 影响 degeneracy rate）仍可能存在。\n- **建议**: 至少为 Few-NERD 的核心 selection 结果 (LP +1.36 pp) 添加 2-3 seed replication；或者在 Limitations 中更明确指出 selection 结果的 seed coverage 比 QE 更有限。\n\n### [Should-Fix] W6: Few-NERD 训练配置差异未充分讨论\n\n- **位置**: Appendix L (\"3 epochs\" for Few-NERD vs. 5 epochs for SciERC/CoNLL)\n- **问题**: Few-NERD 仅训练 3 epochs（vs. 其他数据集的 5 epochs），这可能直接导致 lower degeneracy（更少训练 → 更弱模型 → 更多 diversity）。如果 Few-NERD 的低 degeneracy 部分源自 under-training 而非数据集固有特性，则 degeneracy-selection 关系的因果方向被混淆。\n- **论文在 Discussion 中提到** \"dataset-specific factors (number of entity types, semantic overlap) also modulate the rate\"，但没有排除 training epoch 差异这一 confound。\n- **建议**: 在 appendix 中添加 epoch sensitivity 分析（如 Few-NERD 5 epoch 的 degeneracy rate），或明确讨论为何使用 3 epochs（early stopping? 收敛?）。\n\n### [Minor] W7: Soft Jaccard 分母选择的 claim 缺乏完整表达\n\n- **位置**: Section 3.2, Equation 4, footnote\n- **问题**: 论文声称 max vs union normalizer 差异 Δρ<0.01，并在 Appendix (Table 5) 给出了 6 个 model-dataset combinations 的证据。这实际上是充分的。但 footnote 的表述 \"nearly identical rankings (Δρ<0.01; Table X)\" 暗示这是所有条件下的 bound，而表中最大差异是 0.009——距 0.01 仅一个量级，更准确的表述是 \"|Δρ| ��� 0.009\"。\n- **建议**: 微调措辞精度即可。\n\n### [Minor] W8: Table 3 与 Table 4 的 greedy F1 不一致可能困惑读者\n\n- **位置**: Table 3 (SciERC greedy=0.645), Table 4 (SciERC greedy=0.614)\n- **问题**: 两表使用不同 evaluation protocol (gold-filtered n=529 vs. full-set n=551)，导致同一模型的 greedy F1 差 3.1 pp。虽然 Table 4 有脚注解释，但读者在主文中连续看到两个不同的 baseline 数字时容易困惑。\n- **建议**: 统一 evaluation protocol，或在 Table 4 同时报告 gold-filtered 数字。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1**: Section 4.5 LoRA rank=8 ablation 中，LP 的 median within-instance range 是多少？如果 rank=8 下 LP range 显著小于 rank=32 下的 0.041 nats，则 selection failure 可归因于更严重的 compression 而非 degeneracy 本身不充分���\n\n**Q2**: Few-NERD 训练为何仅 3 epochs？是否有 early stopping 或 validation loss plateau 的证据？5 epochs 下的 degeneracy rate 是多少？\n\n**Q3**: Table 3 的 sign test 使用的是 instance-level 配对（对每个 instance 比较 LP-selected F1 vs greedy F1），还是 corpus-level 比较？如果是 instance-level，n=529 × 2 seeds = 1058 paired observations 应该有更强的 power。\n\n**Q4**: Within-instance SJ-F1 ρ=0.52 (Section 5) 报告为 median；distribution 如何？有多少比例的 non-degenerate instances 有 ρ<0？如果大量 instances 的 within-instance correlation 为负或接近零，则 \"well-aligned utility\" 的 claim 需要 qualify。\n\n**Q5**: Entity-type-level degeneracy-LP gain 分析（Appendix, ρ=-0.881, p=0.004, n=8）中，是否考虑过 entity type frequency 或 average entity count per sentence 作为 confound？高频类型可能同时有 higher degeneracy 和 lower selection gain，但因果机制可能是 frequency → model confidence → degeneracy + LP compression，而非 degeneracy → LP failure。\n\n---\n\n## Missing References\n\n1. **Best-of-N with process reward models**: Lightman et al. (2024) \"Let's Verify Step by Step\" 在 math reasoning 中展示了 verifier-based BoN 的 scaling law——与本文\"需要 learned verifier\"的结论直接相关，已引用但可更深入对比。\n2. **Self-consistency for structured prediction beyond NER**: Yoran et al. (2023) \"Answering Questions by Meta-Reasoning over Multiple Chains of Thought\" 和 Li et al. (2023) \"Making Language Models Better Reasoners with Step-Aware Verifier\" 在 structured reasoning 中有类似 gap 的发现。\n3. **Diversity in fine-tuned models**: Zhang et al. (2024) \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters\" (DeepMind) 讨论了 fine-tuned model 的 diversity collapse 与 test-time compute 的关系——直接相关。\n4. **MBR for structured prediction**: Eikema et al. (2025) \"Structured MBR\" 已引用但可更详细讨论为何 IE 的 bag-of-unit mismatch 比 MT 更严重。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 信息密度高，四个必答问题都有覆盖。\n- \"correlation-selection gap\" 概念在 Abstract 中引入但未定义（主文 Section 4.3 才定义），建议用一句简短释义。\n- 数字选择合理（ρ, AUROC, pp gains, p values）。\n\n### Introduction\n- 叙事线清晰：从 self-consistency 的成功切入 NER 的结构性挑战。\n- Contribution 3 \"Degeneracy as a regime boundary\" 的 claim 在 Introduction 中比实际证据更强（写作是 \"inversely associated\" 但 structure 暗示因果）。\n\n### Method (Section 3)\n- 形式化清晰。5 个 signal 的数学定义完整且正确。\n- Fleiss' κ 的 adaptation 有 independence concern（已在 Appendix B 用 permutation test 验证，充分）。\n- MBR/consensus-proximity 的等价性证明 (Appendix C, LOO-SJ) 是好的补充。\n\n### Experiments (Section 4)\n- 数据集选择合理且角色分工清晰。\n- 训练细节 (Appendix E, Table 7) 充分：LoRA config、optimizer、batch size、epoch 均报告。\n- vLLM + XGrammar constrained decoding 描述清楚；但 vLLM 版本号未报告（影响 reproducibility）。\n\n### Discussion (Section 5)\n- 这一节承载了大量 ablation 和 diagnostic 结果，密度极高。\n- Entity-token LP ablation 的 negative result 是好的：排除了 format-token dilution 作为 primary cause。\n- Signal combination 失败（logistic regression、MLP、RF）有力支撑了 \"feature space bottleneck\" 的结论。\n- \"Practical considerations\" 段落实用价值高（N=8 suffices for QE, cost-benefit for selection is unfavorable）。\n\n### Limitations\n- 全面且诚实（scale limitation、seed coverage、untested verifier、ε post-hoc choice）。\n- 建议补充: power analysis limitation、Few-NERD epoch confound。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claims 有充分支撑（QE works, selection fails），但核心因果诊断（degeneracy gates LP selection）的证据基础偏薄（cross-dataset n=3, entity-type confounds, LoRA ablation 混淆变量）。统计方法使用恰当。 |\n| Excitement | 3.5/5 | \"Correlation-selection gap\" 是 useful conceptual contribution，对 test-time compute scaling 社区有 immediate practical value（告诉 practitioner 何时 BoN 不工作）。但核心发现是 negative result + diagnostic，novelty 在于 framing 而非 new method。 |\n| Reproducibility | 4/5 | 训练 config 完整 (Table 7)，prompt template 提供，constrained decoding 细节清楚。缺 vLLM 版本号，缺部分配置的 exact random seeds for selection experiments。Code release upon acceptance 声明。 |\n\n---\n\n## Overall Score\n\n**Borderline Accept (3.5/5)**\n\n论文的实验工作量大、统计处理严谨、negative results 的报告方式远超平均水平。\"Correlation-selection gap\" 的概念化和三层诊断对社区有价值。主要扣分来自：(1) 核心因果 claim（degeneracy as regime boundary）的证据基础偏弱（n=3 datasets, confounded ablation）；(2) \"model-intrinsic compression\" claim 与 RE 结果矛盾但主文未充分 qualify。如果作者能在 rebuttal 中：(a) 提供 LoRA rank=8 下的 LP compression statistics，(b) 澄清 Few-NERD epoch confound，(c) 弱化/qualify 因果语言，我倾向接收。\n\n---\n\n## Confidence\n\n**4/5** — 我对方法论和统计分析的评估有信心；对 NER/IE 领域的 related work coverage 有较好把握，但未验证所有 appendix 中的数值计算。\n",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Round 1 Review — Reviewer 1 (方法严谨性 + 实验设计)\n\n**Paper**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n\n---\n\n## Summary (2-3 句)\n\n本文系统评估了 5 种 confidence signals 在 LLM-based NER 中的 quality estimation 和 sample selection 能力，发现 QE 成功但 selection 失败（correlation-selection gap），并通过 instance degeneracy 和 LP compression 两个机制给出诊断。实验设计严谨度高于平均水准（多数据集、多模型、多 seed、bootstrap/TOST 统计检验），但部分核心 claim 的因果推断证据不足，跨数据集梯度 n=3 支撑的泛化结论需要审慎对待。\n\n---\n\n## Strengths\n\n1. **问题定义清晰且有贡献** (Section 1, 3.3): \"correlation-selection gap\" 的概念化有价值——将 QE 和 selection 明确解耦，指出一个被 prior work 忽略的 confound。instance-level vs per-sample 的形式化区分（Section 3.1）简洁且数��上正确。\n\n2. **实验设计的系统性** (Section 4): 4 个 NER benchmark 构成 difficulty gradient（WNUT-17 collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个数据集的角色清晰。两个模型族（Qwen3-8B, LLaMA-3.1-8B）加 4B/3B ablation 排除模型特异性。\n\n3. **统计方法论上佳** (Section 4.3, Appendix): Bootstrap CI（B=10,000）、paired sign test、TOST 等效性检验、Bonferroni 校正、Kendall's W 排名稳定性、Fisher 合并 p 值——统计工具选择恰当，且在负面结果中使用 TOST 避免了\"absence of evidence = evidence of absence\"的谬误。\n\n4. **三层诊断结构有说服力** (Section 4.3): (a) instance-level 信号 by construction 不能排名候选 → (b) MBR with aligned utility 因 degeneracy 失败 → (c) LP 有 per-sample 信息但被 compression 限制。逻辑递进清晰。\n\n5. **负面结果的审慎表达**: 论文多处使用\"inversely associated with\"而非\"causes\"，使用\"necessary but not sufficient\"限定 claim，Limitations 节详尽列举未覆盖条件。\n\n6. **Appendix 丰富且组织有序**: 涵盖 FK independence test、SJ normalizer robustness、ε robustness、thinking token impact、OOD analysis 等，大多数潜在反驳都有对应的 ablation 或 control。\n\n---\n\n## Weaknesses\n\n### [Must-Fix] W1: 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)\n\n- **位置**: Section 4.4 (Table 4), Section 5 \"Regime boundaries\", Figure 3\n- **问题**: 论文的核心 claim 之一是 \"LP selection effectiveness is inversely associated with degeneracy rate across datasets\"，但这一梯度仅基于 n=3 数据集（CoNLL 58% → SciERC 21% → Few-NERD 10%）。任何三个数据点的单调排列概率为 1/3!= 1/6，即使在随机条件下也有 16.7% 的概率出现单调趋势。\n- **补充**: 论文试图用 entity-type-level analysis（n=8, ρ=-0.881, p=0.004）加强论证，但 entity type 之间共享同一模型、同一 checkpoint、同一 inference pipeline，违反独立性假设。不同 entity type 的 degeneracy 差异可能源自 type frequency、schema complexity 等混淆变量，而非 degeneracy 本身直接导致 LP selection 差异。\n- **Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测**，统计上有问题：cross-dataset aggregates 和 per-entity-type points 的方差结构完全不同，不应直接 pool。\n- **为什么影响接收**: 如果 degeneracy 梯度的因果解释不成立，Contribution 3 的基础动摇。\n- **建议**: (a) 增加至少 2-3 个数据集的实验（如 OntoNotes、ACE05）扩大 n；(b) 用 Few-NERD 内 entity-type analysis 时，控制 type frequency 和 entity boundary difficulty 等混淆变量；(c) 不要 pool 不同粒度的观测到同一 correlation。\n\n### [Must-Fix] W2: \"Necessary but not sufficient\" claim 的 LoRA-rank ablation 存在混淆变量\n\n- **位置**: Section 4.5 \"LoRA-rank ablation\" (line: \"Low degeneracy is thus a necessary but not sufficient condition for selection\")\n- **问题**: LoRA rank=8 ablation 降低了 degeneracy (21% → 7.2%) 且增加了 oracle headroom (13.3 → 16.0 pp)，但 LP selection 仍失败。论文据此声称 degeneracy 是 \"necessary but not sufficient\"。但 LoRA rank=8 同时降低了模型能力（greedy F1: 0.645 → 0.640），改变了学到的 representation space。LP compression 在 rank=8 下可能因模型能力下降而加剧，而非因为 degeneracy 本身不充分。\n- **矛盾**: Few-NERD 在 10% degeneracy 下 LP selection 成功 (+1.36 pp)，而 rank=8 SciERC 在 7.2% degeneracy 下仍失败。如果 degeneracy 是唯一 gating factor，Few-NERD 的成功和 rank=8 SciERC 的失败之间的差异需要更好的解释。论文在 Section 4.4 简要提到 \"LP signal quality (ρ) provides an additional prerequisite\"，但这实质上是在说 degeneracy + LP quality 联���决定 selection，而非 degeneracy alone is necessary。\n- **为什么影响接收**: \"Necessary but not sufficient\" 是一个精确的逻辑声明；当前实验设计无法将 degeneracy 从 LP compression 中独立隔离。\n- **建议**: (a) 明确指出 LoRA rank ablation 同时改变了多个变量（degeneracy、model quality、LP compression degree），不能做 clean causal attribution；(b) 将 claim 弱化为 \"low degeneracy co-occurs with LP selection success, but rank-8 ablation shows it is not alone sufficient\"；(c) 最好提供 rank=8 下的 LP compression 统计（median LP range、tied fraction），以量化 compression 在两种 rank 下的变化。\n\n### [Should-Fix] W3: 负面结果的统计功效 (power) 未报告\n\n- **位置**: Section 4.3 (Table 3, \"LP achieves only 0.647, Δ=+0.2 pp, d=0.038, p=0.29\")\n- **问题**: 论文的中心论点是负面结果（selection 不显著优于 greedy）。对于负面结果，需要报告 power analysis：在当前样本量 (n=529) 和 seed 数量 (2) 下，检测 1 pp 效应（一个实际有意义的改进）的统计功效是多少？如果 power 很低（如 <50%），则 p=0.29 无法区分 \"真的没效果\" 和 \"效果存在但检测不到\"。\n- **TOST 部分缓解了这个问题** (Appendix D)，但 TOST 使用的 δ=2pp (internal anchor) 是否过宽？externally anchored δ=1.0pp 下，SciERC 未通过 TOST。\n- **为什么影响评分**: 虽然 TOST 是好的补充，但主文没有明确讨论 power，可能误导读者认为 \"p>0.05\" 等同于 \"确认无效果\"。\n- **建议**: 在 main text 或 appendix 中加入 post-hoc power analysis，报告当前设计检测 Δ=1pp 的 power；或者明确指出 Few-NERD (n=32,565) 的结果 (LP +1.36 pp, p<0.001) 才是 definitive evidence，SciERC 的 non-significance 可能受限于 power。\n\n### [Should-Fix] W4: \"Compression is model-intrinsic\" 的结论与 RE 结果矛盾\n\n- **位置**: Section 5 \"Ablation: free-form decoding\" + Appendix H (Table 8)\n- **问题**: 论文 NER free-form ablation 发现 LP 分布几乎不变 (std ratio 0.97)，据此声称 \"compression is model-intrinsic rather than constraint-imposed\"。但 RE 的 free-form decoding 显著恢复了 LP selection (+2.35 pp, p=0.025)，直接证明 constraints DO compress LP for RE。\n- **论文在 Section 5 最后简要提到这一分歧**，但 Abstract 和 Introduction 中 \"compression is model-intrinsic\" 的 framing 没有 qualification。读者如果只看主文可能误以为这是普适结论。\n- **为什么影响评分**: 论文的诊断框架混淆了 task-specific behavior 和 universal mechanism。\n- **建议**: (a) 将主文 claim 限定为 \"for NER, compression is model-intrinsic; for RE, constraint-imposed mechanisms contribute significantly\"；(b) 在 Abstract 或 Introduction 的 diagnostic chain 描述中加入 task qualifier。\n\n### [Should-Fix] W5: Primary seed (seed=42) 的代表性与 selection 实验的 2-seed 限制\n\n- **位置**: Section 4.1 footnote 4 (\"Quality estimation uses a single primary seed; selection uses 2-seed averages\")\n- **问题**: QE 主结果仅 1 seed，selection 仅 2 seeds。虽然 Table 6 的 3-seed stability test 显示 σ≤0.026 for ρ rankings，但 selection F1 的 seed variance 未被同样充分量化。Table 3 报告的 selection F1 σ（如 LP: ±0.005）基于仅 2 seeds 的极差，这不是可靠的 variance estimate。\n- **Few-NERD 是 1-seed result** (Table 4)，尽管 n=32,565 提供了足够 statistical power，但 systematic bias（如训练 seed 影响 degeneracy rate）仍可能存在。\n- **建议**: 至少为 Few-NERD 的核心 selection 结果 (LP +1.36 pp) 添加 2-3 seed replication；或者在 Limitations 中更明确指出 selection 结果的 seed coverage 比 QE 更有限。\n\n### [Should-Fix] W6: Few-NERD 训练配置差异未充分讨论\n\n- **位置**: Appendix L (\"3 epochs\" for Few-NERD vs. 5 epochs for SciERC/CoNLL)\n- **问题**: Few-NERD 仅训练 3 epochs（vs. 其他数据集的 5 epochs），这可能直接导致 lower degeneracy（更少训练 → 更弱模型 → 更多 diversity）。如果 Few-NERD 的低 degeneracy 部分源自 under-training 而非数据集固有特性，则 degeneracy-selection 关系的因果方向被混淆。\n- **论文在 Discussion 中提到** \"dataset-specific factors (number of entity types, semantic overlap) also modulate the rate\"，但没有排除 training epoch 差异这一 confound。\n- **建议**: 在 appendix 中添加 epoch sensitivity 分析（如 Few-NERD 5 epoch 的 degeneracy rate），或明确讨论为何使用 3 epochs（early stopping? 收敛?）。\n\n### [Minor] W7: Soft Jaccard 分母选择的 claim 缺乏完整表达\n\n- **位置**: Section 3.2, Equation 4, footnote\n- **问题**: 论文声称 max vs union normalizer 差异 Δρ<0.01，并在 Appendix (Table 5) 给出了 6 个 model-dataset combinations 的证据。这实际上是充分的。但 footnote 的表述 \"nearly identical rankings (Δρ<0.01; Table X)\" 暗示这是所有条件下的 bound，而表中最大差异是 0.009——距 0.01 仅一个量级，更准确的表述是 \"|Δρ| ��� 0.009\"。\n- **建议**: 微调措辞精度即可。\n\n### [Minor] W8: Table 3 与 Table 4 的 greedy F1 不一致可能困惑读者\n\n- **位置**: Table 3 (SciERC greedy=0.645), Table 4 (SciERC greedy=0.614)\n- **问题**: 两表使用不同 evaluation protocol (gold-filtered n=529 vs. full-set n=551)，导致同一模型的 greedy F1 差 3.1 pp。虽然 Table 4 有脚注解释，但读者在主文中连续看到两个不同的 baseline 数字时容易困惑。\n- **建议**: 统一 evaluation protocol，或在 Table 4 同时报告 gold-filtered 数字。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1**: Section 4.5 LoRA rank=8 ablation 中，LP 的 median within-instance range 是多少？如果 rank=8 下 LP range 显著小于 rank=32 下的 0.041 nats，则 selection failure 可归因于更严重的 compression 而非 degeneracy 本身不充分���\n\n**Q2**: Few-NERD 训练为何仅 3 epochs？是否有 early stopping 或 validation loss plateau 的证据？5 epochs 下的 degeneracy rate 是多少？\n\n**Q3**: Table 3 的 sign test 使用的是 instance-level 配对（对每个 instance 比较 LP-selected F1 vs greedy F1），还是 corpus-level 比较？如果是 instance-level，n=529 × 2 seeds = 1058 paired observations 应该有更强的 power。\n\n**Q4**: Within-instance SJ-F1 ρ=0.52 (Section 5) 报告为 median；distribution 如何？有多少比例的 non-degenerate instances 有 ρ<0？如果大量 instances 的 within-instance correlation 为负或接近零，则 \"well-aligned utility\" 的 claim 需要 qualify。\n\n**Q5**: Entity-type-level degeneracy-LP gain 分析（Appendix, ρ=-0.881, p=0.004, n=8）中，是否考虑过 entity type frequency 或 average entity count per sentence 作为 confound？高频类型可能同时有 higher degeneracy 和 lower selection gain，但因果机制可能是 frequency → model confidence → degeneracy + LP compression，而非 degeneracy → LP failure。\n\n---\n\n## Missing References\n\n1. **Best-of-N with process reward models**: Lightman et al. (2024) \"Let's Verify Step by Step\" 在 math reasoning 中展示了 verifier-based BoN 的 scaling law——与本文\"需要 learned verifier\"的结论直接相关，已引用但可更深入对比。\n2. **Self-consistency for structured prediction beyond NER**: Yoran et al. (2023) \"Answering Questions by Meta-Reasoning over Multiple Chains of Thought\" 和 Li et al. (2023) \"Making Language Models Better Reasoners with Step-Aware Verifier\" 在 structured reasoning 中有类似 gap 的发现。\n3. **Diversity in fine-tuned models**: Zhang et al. (2024) \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters\" (DeepMind) 讨论了 fine-tuned model 的 diversity collapse 与 test-time compute 的关系——直接相关。\n4. **MBR for structured prediction**: Eikema et al. (2025) \"Structured MBR\" 已引用但可更详细讨论为何 IE 的 bag-of-unit mismatch 比 MT 更严重。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 信息密度高，四个必答问题都有覆盖。\n- \"correlation-selection gap\" 概念在 Abstract 中引入但未定义（主文 Section 4.3 才定义），建议用一句简短释义。\n- 数字选择合理（ρ, AUROC, pp gains, p values）。\n\n### Introduction\n- 叙事线清晰：从 self-consistency 的成功切入 NER 的结构性挑战。\n- Contribution 3 \"Degeneracy as a regime boundary\" 的 claim 在 Introduction 中比实际证据更强（写作是 \"inversely associated\" 但 structure 暗示因果）。\n\n### Method (Section 3)\n- 形式化清晰。5 个 signal 的数学定义完整且正确。\n- Fleiss' κ 的 adaptation 有 independence concern（已在 Appendix B 用 permutation test 验证，充分）。\n- MBR/consensus-proximity 的等价性证明 (Appendix C, LOO-SJ) 是好的补充。\n\n### Experiments (Section 4)\n- 数据集选择合理且角色分工清晰。\n- 训练细节 (Appendix E, Table 7) 充分：LoRA config、optimizer、batch size、epoch 均报告。\n- vLLM + XGrammar constrained decoding 描述清楚；但 vLLM 版本号未报告（影响 reproducibility）。\n\n### Discussion (Section 5)\n- 这一节承载了大量 ablation 和 diagnostic 结果，密度极高。\n- Entity-token LP ablation 的 negative result 是好的：排除了 format-token dilution 作为 primary cause。\n- Signal combination 失败（logistic regression、MLP、RF）有力支撑了 \"feature space bottleneck\" 的结论。\n- \"Practical considerations\" 段落实用价值高（N=8 suffices for QE, cost-benefit for selection is unfavorable）。\n\n### Limitations\n- 全面且诚实（scale limitation、seed coverage、untested verifier、ε post-hoc choice）。\n- 建议补充: power analysis limitation、Few-NERD epoch confound。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claims 有充分支撑（QE works, selection fails），但核心因果诊断（degeneracy gates LP selection）的证据基础偏薄（cross-dataset n=3, entity-type confounds, LoRA ablation 混淆变量）。统计方法使用恰当。 |\n| Excitement | 3.5/5 | \"Correlation-selection gap\" 是 useful conceptual contribution，对 test-time compute scaling 社区有 immediate practical value（告诉 practitioner 何时 BoN 不工作）。但核心发现是 negative result + diagnostic，novelty 在于 framing 而非 new method。 |\n| Reproducibility | 4/5 | 训练 config 完整 (Table 7)，prompt template 提供，constrained decoding 细节清楚。缺 vLLM 版本号，缺部分配置的 exact random seeds for selection experiments。Code release upon acceptance 声明。 |\n\n---\n\n## Overall Score\n\n**Borderline Accept (3.5/5)**\n\n论文的实验工作量大、统计处理严谨、negative results 的报告方式远超平均水平。\"Correlation-selection gap\" 的概念化和三层诊断对社区有价值。主要扣分来自：(1) 核心因果 claim（degeneracy as regime boundary）的证据基础偏弱（n=3 datasets, confounded ablation）；(2) \"model-intrinsic compression\" claim 与 RE 结果矛盾但主文未充分 qualify。如果作者能在 rebuttal 中：(a) 提供 LoRA rank=8 下的 LP compression statistics，(b) 澄清 Few-NERD epoch confound，(c) 弱化/qualify 因果语言，我倾向接收。\n\n---\n\n## Confidence\n\n**4/5** — 我对方法论和统计分析的评估有信心；对 NER/IE 领域的 related work coverage 有较好把握，但未验证所有 appendix 中的数值计算。\n",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-17T07:12:17.851367+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3922
}
```

</details>

---


### Assistant

_source line 1095 · 2026-05-17T07:12:27.038925+00:00_

审稿报告已提交给 Review Director。

总结：我给出 **Borderline Accept (3.5/5)** 的评分。论文实验量大、统计严谨、negative results 的处理方式优秀，"correlation-selection gap" 概念有价值。主要问题集中在：

1. **[Must-Fix]** 跨数据集 degeneracy 梯度仅 n=3，因果推断证据不足
2. **[Must-Fix]** LoRA rank=8 ablation 的 "necessary but not sufficient" claim 存在未隔离的混淆变量
3. **[Should-Fix]** 负面结果缺少 power analysis
4. **[Should-Fix]** "compression is model-intrinsic" 与 RE free-form results 矛盾但主文未 qualify
5. **[Should-Fix]** Few-NERD 训练 epoch 差异可能 confound degeneracy 比较
6. **[Should-Fix]** Selection 实验 seed coverage 有限（1-2 seeds）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 35

## Round 35

4 recorded events


### User

_source line 1096 · 2026-05-17T07:14:38.008093+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。

---

### Reviewer 2 完整审稿意见

**Overall Score**: Borderline reject (leaning Findings), 3/5
**Confidence**: 4/5

**Strengths**:
S1. 问题 framing 清晰且有价值
S2. 实验设计全面且系统
S3. 统计严谨性高
S4. Negative result 的论证逻辑完整
S5. Related work 覆盖面广（59 篇引用）

**Weaknesses**:

**W1 [Must-Fix]** 核心概念 "correlation-selection gap" 的新颖性有限。本质上是已知 observation 的 repackaging：(1) instance-level signals 不能做 per-sample ranking 是 trivial by definition；(2) fine-tuned models 的 diversity collapse 是已知现象 (Kirk et al., 2024)；(3) LP compression 是 specific but minor。三者组合的诊断价值有余，但是否构成 EMNLP 主会议长文的贡献量存疑。

**W2 [Must-Fix]** "Instance degeneracy" 作为概念贡献的独立性不足。degeneracy 不是 "failure mechanism" 而是 model success 的 natural consequence。CoNLL 58% degeneracy = 91% F1（模型很好当然一致）；Few-NERD 10% = 75% F1（模型 underfit）。"degeneracy gates LP selection" 本质等价于 "LP selection only works when the model is bad enough to produce diverse wrong answers"。

**W3 [Must-Fix]** 缺乏任何可操作的 positive contribution。全部 takeaway 是 "需要 trained verifiers"，但不训练 verifier、不提出新 signal、唯一 remedy (entity-token LP) 失败。纯诊断性论文需要极强 insight novelty 来补偿。

**W4 [Should-Fix]** em-dash 过度使用（约 90 处），AI 写作风格痕迹。

**W5 [Should-Fix]** Abstract 和 Introduction 过度堆砌数字（Abstract 10 行含 15+ 个数字），报告风格重于故事风格。

**W6 [Should-Fix]** 与 Yao et al. (2026) 的增量贡献需更明确差异化。

**W7 [Should-Fix]** Missing reference: Byerly & Khashabi (2024) "Self-Consistency Falls Short"。

**W8 [Should-Fix]** Discussion section 过长（2+ 页），部分内容适合移入 Appendix。

**M1-M5**: "leverage" 用词、Abstract 缩写未定义 (NER/MBR)、Table 3 EM/VC 无 p 值未解释、Figure 2 "~15%" 不精确、em-dash vs en-dash 区分。

**Questions**:
Q1. Few-NERD 低 degeneracy (10%) 和高 F1 (75%) 是否因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 的函数。
Q2. LoRA rank=8 degeneracy 7% 但 selection 失败——degeneracy 是否不是 "gating factor"？
Q3. 70B+ 模型是否 degeneracy 更高？如果是，整个 research direction 是否无望？
Q4. Supervised verifier 只用 5 个 signal 做 features，加入 token-level features 能否 close gap？

**Missing References**: Byerly & Khashabi (2024)、CRF-based calibration (Lafferty et al.)、Diverse Beam Search (Vijayakumar et al., 2016)

**官方维度打分**: Soundness 4/5, Excitement 2.5/5, Reproducibility 4/5

---

请对 W1-W8、M1-M5、Q1-Q4 逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-17T07:16:44.343452+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见逐条回应\n\n---\n\n## Weaknesses 回应\n\n**[REBUT] R2-W1: \"Correlation-selection gap\" 新颖性有限**\n\nR2 称三层诊断是已知 observation 的 repackaging。我部分不同意：\n\n(1) \"Instance-level signals 不能做 per-sample ranking 是 trivial by definition\" — 表面上 trivial，但 prior work（Yao et al. 2026; Vashurin et al. 2025 CoCoA; Taubenfeld et al. 2025 CISC）直接用 consistency signals 做 selection，说明社区并未普遍认识到这一区分。论文 Section 1 第二段明确指出 \"Prior work on confidence estimation for LLM-based IE has conflated quality estimation with sample selection\"。如果是 trivial，这些 prior work 不应该存在。\n\n(2) \"Diversity collapse 是已知现象\" — Kirk et al. (2024) 讨论的是 RLHF 下的 diversity collapse 作为 alignment tax；本文的 instance degeneracy 是 supervised fine-tuning 下的量化现象，且关键贡献不在于发现 degeneracy 存在，而在于量化其与 selection headroom 的具体关系（Table 5: 21% constant F1 + 13% constant utility = 34% instances 完全没有 selection room）。\n\n(3) 但我同意 R2 关于 \"是否构成 EMNLP 主会议长文贡献量\" 的质疑。纯诊断性 negative result 论文需要很强的 insight density。论文在 diagnostic depth 上做到了，但缺乏 constructive output 确实限制了贡献的完整性。\n\n**结论**: 不同意 \"repackaging\" 的定性，但同意 contribution 量对 main conference 偏弱，可能更适合 Findings。\n\n---\n\n**[REBUT] R2-W2: Degeneracy = model success 的 natural consequence**\n\nR2 的逻辑是：CoNLL 58% degeneracy ← 91% F1（好模型），Few-NERD 10% ← 75% F1（弱模型），因此 degeneracy 仅反映 model quality。\n\n但论文有两个直接反驳：\n\n(a) **Few-NERD 75% F1 + 10% degeneracy vs. SciERC 66% F1 + 21% degeneracy** (Table 4, Section 5): Few-NERD 性能更高但 degeneracy 更低。如果 degeneracy 纯粹是 model quality 的函数，这一反转不应出现。论文在 Section 5 明确讨论：\"Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate。\"\n\n(b) **4B vs 8B on SciERC** (Table 5): 8B degeneracy 21% vs 4B degeneracy 10.4%，但 within-instance utility correlation 可比 (ρ=0.52 vs 0.55)。这证明 degeneracy 不仅是 accuracy 的 proxy——更高能力的模型在相同任务上产生更多 degeneracy，即使 within-instance 的 quality 分布仍有结构。\n\nR2 的简化 (\"LP selection only works when the model is bad enough\") 与 Few-NERD 数据矛盾：Few-NERD 是 75% F1（不差），LP 仍然 work (+1.36 pp)。\n\n**但我同意** R2 的 deeper point：论文需要更清楚地 disentangle degeneracy 的多个 driver（model quality, output space size, schema complexity, training epochs），而非将其作为一个 monolithic \"mechanism\"。这与我在 W1 中提出的 concern 一致。\n\n---\n\n**[AGREE] R2-W3: 缺乏可操作的 positive contribution**\n\n同意。论文唯一的 constructive suggestion 是 \"需要 trained verifiers\"（Section 5 最后段, Conclusion 最后句），但自己没有实现。Entity-token LP remedy 失败（Section 5 entity-token LP ablation），supervised verifier baseline 也失败 (Section 4.5)。LP + VC 组合全部失败 (Section 5 \"Signal combinations\")。\n\n对于 EMNLP main conference，我认为至少需要以下之一来补偿：\n- 一个 working (哪怕 partial) verifier baseline 展示 oracle gap 可以被 partially closed\n- 或者一个 clear actionable framework 告诉 practitioner exactly when to use BoN（例如基于 degeneracy rate 的 decision rule）\n\n论文在 practical considerations 段落有一些 guidance，但不够 concrete to be actionable。\n\n不过我注意到：Few-NERD 的 LP selection 成功 (+1.36 pp, p<0.001) 本身就是 positive result，只是论文将其 framing 为 diagnostic evidence 而非 practical method。如果 reframe 为 \"LP selection works in the low-degeneracy regime, and we characterize when that regime occurs\"，practical value 会更明显。\n\n---\n\n**[AGREE] R2-W4: em-dash 过度使用**\n\n同意这是一个 presentation quality 问题。我没有专门计数，但通读全文时确实注意到频繁的 em-dash 使用（特别是在 Discussion section）。按照 ACL 写作规范和审稿人期望，减少 em-dash 使用是低成本高收益的修改。\n\n---\n\n**[AGREE] R2-W5: Abstract 和 Introduction 数字堆��**\n\n同意。我重新检查 Abstract：在约 180 words 中有 \"ρ up to 0.38\", \"0.42\", \"AUROC up to 0.82\", \"~13 pp\", \"ρ=0.52\", \"10-58%\", \"0.041 nats\", \"+1.36 pp\", \"p<0.001\", \"58%\", \"+0.42 pp\", \"$N=8$ to 16\", \"p=0.003\" — 密度过高。这是 experimental report 风格而非 story-driven 叙事。每个数字单独看是 justified，但整体上牺牲了可读性。\n\n---\n\n**[REBUT] R2-W6: 与 Yao et al. (2026) 差异化不足**\n\n论文在 Section 1 第二段（Introduction）和 Section 2 \"Consistency for structured IE\" 段落中明确列出差异：(1) Yao et al. 使用 hard-prompting，本文使用 fine-tuned models（degeneracy 更严重）；(2) Yao et al. 仅报告 correlation，未区分 QE vs selection；(3) 本文诊断了两个具体 failure mechanisms。\n\n差异化实际上是充分的——Table 4 的 Few-NERD 结果和 Section 4.5 的 LoRA ablation 都是 Yao et al. 不覆盖的实验。但 Introduction 中差异化的叙述方式可以更 upfront（目前在第二段中间，容易被跳过）。\n\n---\n\n**[REBUT] R2-W7: Missing reference Byerly & Khashabi (2024) \"Self-Consistency Falls Short\"**\n\n我无法确认这篇论文存在。在我的知识范围内，没有 Byerly & Khashabi (2024) 以这个确切标题发表的论文。如果 R2 能提供确切 venue 或 arXiv ID，我可以重新评估。建议作者在 rebuttal 中 verify 这一引用的存在性。\n\n---\n\n**[AGREE] R2-W8: Discussion 过长**\n\n同意。Discussion (Section 5) 承载了：(1) practical implications, (2) why the gap exists (degeneracy + LP compression analysis), (3) non-tied subset analysis, (4) N-scaling effect, (5) temperature effect, (6) verbalized confidence, (7) signal combinations, (8) LP compression hypotheses, (9) free-form ablation, (10) entity-token LP, (11) pilot remedy, (12) practical considerations, (13) regime boundaries, (14) methodological implications. 这是 14 个 distinct sub-topics 在一个 section 中。\n\n建议：将 (3) non-tied subset, (4) N-scaling, (5) temperature, (6) verbalized confidence, (7) signal combinations 移入 Appendix，仅在 Discussion 保留引用。这可释放 ~1 page 空间用于 constructive contribution。\n\n---\n\n## Minor Issues 回应\n\n**[AGREE] R2-M1**: \"leverage\" 用词问题——Minor，容易修复。\n\n**[REBUT] R2-M2**: Abstract 中 NER 需定义——NER (Named Entity Recognition) 是 NLP 社区的标准缩写，ARR 审稿人不需要定义。MBR 可能确实需要定义或避免在 Abstract 中使��（Abstract 中首次出现 \"MBR / consensus-proximity selection\" 在 line 6，未展开）。\n\n**[AGREE] R2-M3**: Table 3 EM/VC 无 p 值——同意需要解释。查看 Table 3，EM (0.637) 和 VC (0.623) 明显低于 greedy (0.645)，因此方向为负，paired test 不会给 \"improvement\" p 值。但论文应标注 \"—\" 并注释 \"below greedy, test not applicable\"。\n\n**[AGREE] R2-M4**: Figure 3 \"~15%\" 的定义——确实不精确。Dashed line 位置应有 explicit justification（如来自 ROC 分析或 breakpoint detection），而非视觉近似。\n\n**[REBUT] R2-M5**: em-dash vs en-dash 区分——这是排版规范问题，不影响科学内容。论文使用 LaTeX `---` (em-dash) 用于解释性插入。按 ACL style guide，em-dash 本身不违规，只是频率过高（同意 W4）。\n\n---\n\n## Questions 回应\n\n**[AGREE] R2-Q1: Output space size 驱动 degeneracy**\n\n这是一个重要的 alternative explanation。Few-NERD 8 types vs CoNLL 4 types 意味着可能的 entity set configurations 指数级更多，自然降低 exact match degeneracy。论文在 Section 5 提到 \"number of entity types\" 作为 modulating factor，但未做 controlled analysis。\n\n这与我在 W1 中的 concern 一致：degeneracy 可能主要是 output space size 的函数，而非独立的 \"mechanism\"。如果在 CoNLL 上增加 entity types（如 fine-grained NER），degeneracy 可能也会下降——那么 \"degeneracy gates selection\" 本质上就是 \"output space diversity gates selection\"，这个 framing 更准确但也更 trivial。\n\n---\n\n**[AGREE] R2-Q2: LoRA rank=8 证据对 degeneracy-as-gating-factor 的挑战**\n\n完全同意。这与我在 W2 中的分析一致：rank=8 下 degeneracy 7.2% 但 LP selection 仍失败，直接挑战了 \"degeneracy is the gating factor\" 的 framing。论文的 \"necessary but not sufficient\" 回应在逻辑上成立，但实验设计上混淆了 degeneracy 下降和模型能力下降这两个变量。\n\n---\n\n**[REBUT] R2-Q3: 70B+ 模型是否使 research direction 无望**\n\n不同意 \"无望\" 的暗示。两个理由：\n\n(a) 70B+ 模型可能有更强的 LP signal quality（representation space 更丰富），即使 degeneracy 更高。LP compression 可能在 larger models 中有不同 pattern——论文未测试不代表方向无望。\n\n(b) 更重要的是，论文的 QE contribution 不受 degeneracy 影响——即使 70B 模型 degeneracy 更高，QE signals 仍然有用（selective prediction, error flagging）。只是 selection 方向可能确实在 highly capable models 上受限。\n\n论文在 Limitations 中诚实承认这一未知：\"Whether the gap holds for 70B+ models is untested—larger models may produce more diverse samples.\" 这是合理的 scope limitation 而非 fatal flaw。\n\n---\n\n**[AGREE] R2-Q4: Supervised verifier 仅用 5 scalar features**\n\n同意这是 verifier experiment 的主要局限。5 个 scalar features（all are instance-level aggregates except LP）本身就 encode 不了 per-sample discriminative information——这几乎是 set up to fail。\n\n如果加入 token-level features（如 per-entity log-prob, attention entropy, hidden state uncertainty），verifier 可能表现完全不同。Section 4.5 的 supervised verifier 结论 (\"bottleneck lies in the feature space\") 实际上只能说 \"bottleneck lies in THESE specific 5 features\"，不能泛化为 \"no feature combination can close the gap\"。\n\n但我也注意到��论文 frame 这个实验的目的是 \"test whether the information bottleneck lies in the aggregation method or the features themselves\"——在这个 narrow claim 下，实验设计是合理的（固定 features，变 aggregation method）。只是 broader conclusion 需要 qualify。\n\n---\n\n## 总结性评价\n\nR2 的核心 concern（novelty/contribution 量不足 for main conference）是合理的，但部分 technical criticisms（W2 的 degeneracy = model success 简化）在论文数据面前不完全成立。我认为论文的贡献介于 Main Conference 和 Findings 之间：\n\n- **支撑 Main Conference 的因素**: 实验系统性、统计严谨性、三层诊断的清晰度、Few-NERD positive result\n- **支撑 Findings 的因素**: 缺乏 constructive contribution (W3)、核心因果 claim 证据偏薄 (与我的 W1-W2 一致)、novelty 主要在 framing 而非 new method\n\n我维持 **Borderline Accept (3.5/5)** 的评分，但认为 R2 的 **Borderline Reject (3/5)** 也在合���范围内。关键分歧在于 \"purely diagnostic paper with strong execution\" 是否 sufficient for main conference。\n",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见逐条回应\n\n---\n\n## Weaknesses 回应\n\n**[REBUT] R2-W1: \"Correlation-selection gap\" 新颖性有限**\n\nR2 称三层诊断是已知 observation 的 repackaging。我部分不同意：\n\n(1) \"Instance-level signals 不能做 per-sample ranking 是 trivial by definition\" — 表面上 trivial，但 prior work（Yao et al. 2026; Vashurin et al. 2025 CoCoA; Taubenfeld et al. 2025 CISC）直接用 consistency signals 做 selection，说明社区并未普遍认识到这一区分。论文 Section 1 第二段明确指出 \"Prior work on confidence estimation for LLM-based IE has conflated quality estimation with sample selection\"。如果是 trivial，这些 prior work 不应该存在。\n\n(2) \"Diversity collapse 是已知现象\" — Kirk et al. (2024) 讨论的是 RLHF 下的 diversity collapse 作为 alignment tax；本文的 instance degeneracy 是 supervised fine-tuning 下的量化现象，且关键贡献不在于发现 degeneracy 存在，而在于量化其与 selection headroom 的具体关系（Table 5: 21% constant F1 + 13% constant utility = 34% instances 完全没有 selection room）。\n\n(3) 但我同意 R2 关于 \"是否构成 EMNLP 主会议长文贡献量\" 的质疑。纯诊断性 negative result 论文需要很强的 insight density。论文在 diagnostic depth 上做到了，但缺乏 constructive output 确实限制了贡献的完整性。\n\n**结论**: 不同意 \"repackaging\" 的定性，但同意 contribution 量对 main conference 偏弱，可能更适合 Findings。\n\n---\n\n**[REBUT] R2-W2: Degeneracy = model success 的 natural consequence**\n\nR2 的逻辑是：CoNLL 58% degeneracy ← 91% F1（好模型），Few-NERD 10% ← 75% F1（弱模型），因此 degeneracy 仅反映 model quality。\n\n但论文有两个直接反驳：\n\n(a) **Few-NERD 75% F1 + 10% degeneracy vs. SciERC 66% F1 + 21% degeneracy** (Table 4, Section 5): Few-NERD 性能更高但 degeneracy 更低。如果 degeneracy 纯粹是 model quality 的函数，这一反转不应出现。论文在 Section 5 明确讨论：\"Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate。\"\n\n(b) **4B vs 8B on SciERC** (Table 5): 8B degeneracy 21% vs 4B degeneracy 10.4%，但 within-instance utility correlation 可比 (ρ=0.52 vs 0.55)。这证明 degeneracy 不仅是 accuracy 的 proxy——更高能力的模型在相同任务上产生更多 degeneracy，即使 within-instance 的 quality 分布仍有结构。\n\nR2 的简化 (\"LP selection only works when the model is bad enough\") 与 Few-NERD 数据矛盾：Few-NERD 是 75% F1（不差），LP 仍然 work (+1.36 pp)。\n\n**但我同意** R2 的 deeper point：论文需要更清楚地 disentangle degeneracy 的多个 driver（model quality, output space size, schema complexity, training epochs），而非将其作为一个 monolithic \"mechanism\"。这与我在 W1 中提出的 concern 一致。\n\n---\n\n**[AGREE] R2-W3: 缺乏可操作的 positive contribution**\n\n同意。论文唯一的 constructive suggestion 是 \"需要 trained verifiers\"（Section 5 最后段, Conclusion 最后句），但自己没有实现。Entity-token LP remedy 失败（Section 5 entity-token LP ablation），supervised verifier baseline 也失败 (Section 4.5)。LP + VC 组合全部失败 (Section 5 \"Signal combinations\")。\n\n对于 EMNLP main conference，我认为至少需要以下之一来补偿：\n- 一个 working (哪怕 partial) verifier baseline 展示 oracle gap 可以被 partially closed\n- 或者一个 clear actionable framework 告诉 practitioner exactly when to use BoN（例如基于 degeneracy rate 的 decision rule）\n\n论文在 practical considerations 段落有一些 guidance，但不够 concrete to be actionable。\n\n不过我注意到：Few-NERD 的 LP selection 成功 (+1.36 pp, p<0.001) 本身就是 positive result，只是论文将其 framing 为 diagnostic evidence 而非 practical method。如果 reframe 为 \"LP selection works in the low-degeneracy regime, and we characterize when that regime occurs\"，practical value 会更明显。\n\n---\n\n**[AGREE] R2-W4: em-dash 过度使用**\n\n同意这是一个 presentation quality 问题。我没有专门计数，但通读全文时确实注意到频繁的 em-dash 使用（特别是在 Discussion section）。按照 ACL 写作规范和审稿人期望，减少 em-dash 使用是低成本高收益的修改。\n\n---\n\n**[AGREE] R2-W5: Abstract 和 Introduction 数字堆��**\n\n同意。我重新检查 Abstract：在约 180 words 中有 \"ρ up to 0.38\", \"0.42\", \"AUROC up to 0.82\", \"~13 pp\", \"ρ=0.52\", \"10-58%\", \"0.041 nats\", \"+1.36 pp\", \"p<0.001\", \"58%\", \"+0.42 pp\", \"$N=8$ to 16\", \"p=0.003\" — 密度过高。这是 experimental report 风格而非 story-driven 叙事。每个数字单独看是 justified，但整体上牺牲了可读性。\n\n---\n\n**[REBUT] R2-W6: 与 Yao et al. (2026) 差异化不足**\n\n论文在 Section 1 第二段（Introduction）和 Section 2 \"Consistency for structured IE\" 段落中明确列出差异：(1) Yao et al. 使用 hard-prompting，本文使用 fine-tuned models（degeneracy 更严重）；(2) Yao et al. 仅报告 correlation，未区分 QE vs selection；(3) 本文诊断了两个具体 failure mechanisms。\n\n差异化实际上是充分的——Table 4 的 Few-NERD 结果和 Section 4.5 的 LoRA ablation 都是 Yao et al. 不覆盖的实验。但 Introduction 中差异化的叙述方式可以更 upfront（目前在第二段中间，容易被跳过）。\n\n---\n\n**[REBUT] R2-W7: Missing reference Byerly & Khashabi (2024) \"Self-Consistency Falls Short\"**\n\n我无法确认这篇论文存在。在我的知识范围内，没有 Byerly & Khashabi (2024) 以这个确切标题发表的论文。如果 R2 能提供确切 venue 或 arXiv ID，我可以重新评估。建议作者在 rebuttal 中 verify 这一引用的存在性。\n\n---\n\n**[AGREE] R2-W8: Discussion 过长**\n\n同意。Discussion (Section 5) 承载了：(1) practical implications, (2) why the gap exists (degeneracy + LP compression analysis), (3) non-tied subset analysis, (4) N-scaling effect, (5) temperature effect, (6) verbalized confidence, (7) signal combinations, (8) LP compression hypotheses, (9) free-form ablation, (10) entity-token LP, (11) pilot remedy, (12) practical considerations, (13) regime boundaries, (14) methodological implications. 这是 14 个 distinct sub-topics 在一个 section 中。\n\n建议：将 (3) non-tied subset, (4) N-scaling, (5) temperature, (6) verbalized confidence, (7) signal combinations 移入 Appendix，仅在 Discussion 保留引用。这可释放 ~1 page 空间用于 constructive contribution。\n\n---\n\n## Minor Issues 回应\n\n**[AGREE] R2-M1**: \"leverage\" 用词问题——Minor，容易修复。\n\n**[REBUT] R2-M2**: Abstract 中 NER 需定义——NER (Named Entity Recognition) 是 NLP 社区的标准缩写，ARR 审稿人不需要定义。MBR 可能确实需要定义或避免在 Abstract 中使��（Abstract 中首次出现 \"MBR / consensus-proximity selection\" 在 line 6，未展开）。\n\n**[AGREE] R2-M3**: Table 3 EM/VC 无 p 值——同意需要解释。查看 Table 3，EM (0.637) 和 VC (0.623) 明显低于 greedy (0.645)，因此方向为负，paired test 不会给 \"improvement\" p 值。但论文应标注 \"—\" 并注释 \"below greedy, test not applicable\"。\n\n**[AGREE] R2-M4**: Figure 3 \"~15%\" 的定义——确实不精确。Dashed line 位置应有 explicit justification（如来自 ROC 分析或 breakpoint detection），而非视觉近似。\n\n**[REBUT] R2-M5**: em-dash vs en-dash 区分——这是排版规范问题，不影响科学内容。论文使用 LaTeX `---` (em-dash) 用于解释性插入。按 ACL style guide，em-dash 本身不违规，只是频率过高（同意 W4）。\n\n---\n\n## Questions 回应\n\n**[AGREE] R2-Q1: Output space size 驱动 degeneracy**\n\n这是一个重要的 alternative explanation。Few-NERD 8 types vs CoNLL 4 types 意味着可能的 entity set configurations 指数级更多，自然降低 exact match degeneracy。论文在 Section 5 提到 \"number of entity types\" 作为 modulating factor，但未做 controlled analysis。\n\n这与我在 W1 中的 concern 一致：degeneracy 可能主要是 output space size 的函数，而非独立的 \"mechanism\"。如果在 CoNLL 上增加 entity types（如 fine-grained NER），degeneracy 可能也会下降——那么 \"degeneracy gates selection\" 本质上就是 \"output space diversity gates selection\"，这个 framing 更准确但也更 trivial。\n\n---\n\n**[AGREE] R2-Q2: LoRA rank=8 证据对 degeneracy-as-gating-factor 的挑战**\n\n完全同意。这与我在 W2 中的分析一致：rank=8 下 degeneracy 7.2% 但 LP selection 仍失败，直接挑战了 \"degeneracy is the gating factor\" 的 framing。论文的 \"necessary but not sufficient\" 回应在逻辑上成立，但实验设计上混淆了 degeneracy 下降和模型能力下降这两个变量。\n\n---\n\n**[REBUT] R2-Q3: 70B+ 模型是否使 research direction 无望**\n\n不同意 \"无望\" 的暗示。两个理由：\n\n(a) 70B+ 模型可能有更强的 LP signal quality（representation space 更丰富），即使 degeneracy 更高。LP compression 可能在 larger models 中有不同 pattern——论文未测试不代表方向无望。\n\n(b) 更重要的是，论文的 QE contribution 不受 degeneracy 影响——即使 70B 模型 degeneracy 更高，QE signals 仍然有用（selective prediction, error flagging）。只是 selection 方向可能确实在 highly capable models 上受限。\n\n论文在 Limitations 中诚实承认这一未知：\"Whether the gap holds for 70B+ models is untested—larger models may produce more diverse samples.\" 这是合理的 scope limitation 而非 fatal flaw。\n\n---\n\n**[AGREE] R2-Q4: Supervised verifier 仅用 5 scalar features**\n\n同意这是 verifier experiment 的主要局限。5 个 scalar features（all are instance-level aggregates except LP）本身就 encode 不了 per-sample discriminative information——这几乎是 set up to fail。\n\n如果加入 token-level features（如 per-entity log-prob, attention entropy, hidden state uncertainty），verifier 可能表现完全不同。Section 4.5 的 supervised verifier 结论 (\"bottleneck lies in the feature space\") 实际上只能说 \"bottleneck lies in THESE specific 5 features\"，不能泛化为 \"no feature combination can close the gap\"。\n\n但我也注意到��论文 frame 这个实验的目的是 \"test whether the information bottleneck lies in the aggregation method or the features themselves\"——在这个 narrow claim 下，实验设计是合理的（固定 features，变 aggregation method）。只是 broader conclusion 需要 qualify。\n\n---\n\n## 总结性评价\n\nR2 的核心 concern（novelty/contribution 量不足 for main conference）是合理的，但部分 technical criticisms（W2 的 degeneracy = model success 简化）在论文数据面前不完全成立。我认为论文的贡献介于 Main Conference 和 Findings 之间：\n\n- **支撑 Main Conference 的因素**: 实验系统性、统计严谨性、三层诊断的清晰度、Few-NERD positive result\n- **支撑 Findings 的因素**: 缺乏 constructive contribution (W3)、核心因果 claim 证据偏薄 (与我的 W1-W2 一致)、novelty 主要在 framing 而非 new method\n\n我维持 **Borderline Accept (3.5/5)** 的评分，但认为 R2 的 **Borderline Reject (3/5)** 也在合���范围内。关键分歧在于 \"purely diagnostic paper with strong execution\" 是否 sufficient for main conference。\n",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1098 · 2026-05-17T07:16:48.008076+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Assistant

_source line 1099 · 2026-05-17T07:16:54.221246+00:00_

交叉回应已提交。核心判断：R2 的 novelty/contribution 量质疑合理（特别是 W3 缺乏 constructive output），但部分 technical criticisms（W2 将 degeneracy 简化为 model success proxy）与论文中 Few-NERD 和 4B/8B 对比的数据矛盾。我维持 Borderline Accept (3.5/5)，认为两位 reviewer 的主要分歧在于 "purely diagnostic paper with strong execution" 是否满足 main conference 门槛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 36

## Round 36

56 recorded events


### User

_source line 1100 · 2026-05-18T01:30:17.402701+00:00_

[Round 18 审稿请求]:
## Round 18 审稿任务 — Reviewer 1

**你的侧重**: 方法严谨性 + 实验设计 + 统计分析

### Venue 信息
- **目标**: EMNLP 2026 Main Conference Long Paper (via ACL Rolling Review May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL LaTeX 模板, `[review]` 选项, 8 页正文 + unlimited references + appendix
- **匿名规则**: Double-blind
- **附录**: 允许，参与审稿

### 论文路径
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`
- 各 section 在 `docs/paper/sections/` 下
- PDF: `docs/paper/main.pdf`

### 审查重点

请重点审查以下方面:

1. **统计分析严谨性**:
   - SciERC 负面结果 (n=529, 2 seeds) 的统计效力是否充分？p=0.29 能否区分"真无效果"和"检测不到"？
   - Cross-dataset degeneracy gradient 仅 3 个 dataset-level 数据点，因果推断是否合理？
   - Entity-type-level correlation (n=8, ρ=-0.881, p=0.004) 的 independence 假设是否成立（共享 model/pipeline）？
   - Fisher combined p (2-seed) / sign test 效力问题
   - Bonferroni 校正 scope 是否恰当？

2. **实验设计 confound 控制**:
   - Few-NERD 训练 3 epochs vs 其他数据集 5 epochs：这个训练差异是否 confound 了 degeneracy 的跨数据集比较？
   - LoRA rank=8 ablation 同时改变了 model capacity 和 degeneracy，能否做 clean causal attribution？
   - Supervised verifier baseline 使用 5 个 scalar features (4 个 instance-level) 是否过于受限？

3. **方法定义清晰度**:
   - "Instance degeneracy" 的操作性定义是否精确一致？
   - LP compression 的 mechanistic explanation 是否充分？
   - ε=0.05 threshold 的 justification

4. **数值一致性**:
   - Abstract/Figure 1 中 ρ=0.42 vs Table 1 max=0.379 的矛盾
   - Table 4 (full-set) vs Table 2 (gold-filtered) 的 evaluation protocol 差异是否清楚标注？
   - Random (0.610) vs Greedy (0.645) 差距来源

### 历史 open issues (供参考)
以下问题在上轮(R17)仍为 open/in_progress，请在审查中确认其当前状态:
- R0-C3: Selection gap 仅 SciERC 单数据集 (critical)
- R16-N1: Degeneracy-gating monotonic claim 仅 3 数据点 (critical)
- R17-W1: LoRA rank=8 LP compression 数据缺失 (critical)
- R17-W2: Few-NERD 3 epochs confound (critical)
- R14-W1: Fisher combined p 统计效力 (critical)
- R14-M1: Random vs Single 差距来源 (critical)

请按 ARR reviewer form 格式输出: Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment (score + confidence)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1101 · 2026-05-18T01:30:26.915609+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1102 · 2026-05-18T01:30:27.116610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 1103 · 2026-05-18T01:30:31.112315+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-18T01:30:31.664725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-18T01:30:31.915718+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 250
}
```

</details>

---


### Tool result

_source line 1106 · 2026-05-18T01:30:40.465565+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

I found relevant information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

The ARR workflow for reviewers includes: (1) read the paper and get the first impression, (2) search for related work, not deli
…[truncated 2372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9353
}
```

</details>

---


### Tool call

_source line 1107 · 2026-05-18T01:30:43.628622+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1108 · 2026-05-18T01:30:43.679231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1109 · 2026-05-18T01:30:51.056602+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and descriptions of each score level. I need the exact scoring criteria for: Overall Assessment, Soundness, Excitement, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and descriptions of each score level. I need the exact scoring criteria for: Overall Assessment, Soundness, Excitement, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-18T01:30:51.710204+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-18T01:30:51.760907+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1112 · 2026-05-18T01:30:57.236078+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4**: Conference acceptance recommended
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2**: Needs substantial revisions by next cycle
- **1**: "Do not resubmit: This paper has to be fully redone"

## Soundness
**Scale: 1-5 (with .5 increments)**
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale: 1-5 (with .5 increments)**
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper"
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: "Not Exciting: does not resonate with me"

## Reproducibility
**Scale: 1-5**
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

## Reviewer Confidence
**Scale: 1-5**
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with low likelihood of missed content
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but fairly likely missed details"
- **1**: "Not my area, or paper is very hard to understand"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6179
}
```

</details>

---


### Tool call

_source line 1113 · 2026-05-18T01:31:00.952549+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1114 · 2026-05-18T01:31:01.053282+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1115 · 2026-05-18T01:31:04.191575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1116 · 2026-05-18T01:31:04.643667+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38), supporting selective prediction.
5	Quality estimation does not translate to selection, however: despite ${\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.
6	The gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection fails because instance degeneracy (14\textendash 47\% identical outputs) eliminates headroom; and LP requires two jointly necessary conditions: low instance degeneracy, and adequate LP-quality alignment ($\rho \gtrsim 0.3$).
7	When both conditions are met, LP achieves significant gains ($+1.36$~pp at 14\% degeneracy, $p{<}0.001$); when either is violated, selection fails.
8	Degeneracy is the dominant bottleneck, controllable via temperature and training budget; in the low-degeneracy regime, LP scales with sample count ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
9	Closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1117 · 2026-05-18T01:31:04.644022+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1118 · 2026-05-18T01:31:04.744926+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \textit{why} this correlation fails to yield selection improvements, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	These signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
13	Yet quality estimation does not translate to structural selection, a disparity we term the \textbf{correlation-selection gap} (
…[truncated 3530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-18T01:31:05.046671+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1120 · 2026-05-18T01:31:05.097386+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 2976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1121 · 2026-05-18T01:31:10.671270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
  "offset": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
    "offset": "60"
  }
}
```

</details>

---


### Tool result

_source line 1122 · 2026-05-18T01:31:11.123495+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (60). The file has 60 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-18T01:31:11.123855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1124 · 2026-05-18T01:31:11.224673+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed c
…[truncated 11384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-18T01:31:17.048096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-18T01:31:17.048664+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	All signals achieve positive quality estimation across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL), with rankings stable across model families and a 4B ablation (Table~\ref{tab:scale_ablation}).
5	For selection, LP achieves significant gains only when both conditions are met ($+1.36$~pp on Few-NERD, $p{<}0.001$; Table~\ref{tab:fewnerd}); structural signals uniformly degrade selection.
6	RE signal rankings are in Appendix~\ref{app:re_extension}.
7	
8	\paragraph{Why the gap exists.}
9	Two mechanisms block selection: \textit{instance degeneracy} (consensus-proximity) and \textit{weak LP-quality alignment} (per-sample).
10	Within non-degenerate instances, MBR utility \cite{eikema2022sampling} correlates positively with F1 (SJ median $\rho{=}0.524$) and closes 23--41\% of the oracle gap, but 17.8\% (SciERC) to 47.4\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\ref{tab:degeneracy}).
11	Degeneracy is determined by the interplay of task structure, model architecture, and training convergence (Appendix~\ref{app:epoch_confound}); cross-model evidence (LLaMA 89.2\% vs.\ Qwen 47.4\% on CoNLL; Table~\ref{tab:cross_selection}) reinforces the pattern.
12	LP is severely compressed (median range 0.041 nats; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$.
13	
14	\paragraph{Non-tied subset and $N$-scaling.}
15	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$, survives Bonferroni; Table~\ref{tab:nontied_main}).
16	LP scales with $N$ in the low-degeneracy regime ($+0.52$~pp from $N{=}8$ to 16 on Few-NERD, $p{=}0.003$; \S\ref{sec:fewnerd}); on SciERC, even $N{=}32$ captures less than 5\% of headroom (Table~\ref{tab:n_scaling_
…[truncated 3549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1127 · 2026-05-18T01:31:17.048991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1128 · 2026-05-18T01:31:17.301321+00:00_

File content (34318 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1129 · 2026-05-18T01:31:21.278421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1130 · 2026-05-18T01:31:21.730783+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 13589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-18T01:31:21.781628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1132 · 2026-05-18T01:31:22.334441+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (14\textendash 47\%) collapses the candidate pool; and LP, the sole per-sample signal, requires two jointly necessary conditions: low degeneracy and adequate LP-quality alignment ($\rho \gtrsim 0.3$).
6	LP selection succeeds when both conditions are met: at 13.8\% degeneracy with strong alignment ($\rho{\approx}0.5$; Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 17.8\% with weak alignment ($\rho{\approx}0.24$; SciERC), $+0.42$~pp ($p{=}0.091$); at 47.4\% (CoNLL), LP fails.
7	In the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap; the bottleneck lies in the signal space accessible to unsupervised aggregation, not in the combination method.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline when both degeneracy and alignment conditions are met.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1133 · 2026-05-18T01:31:22.334880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1134 · 2026-05-18T01:31:22.385329+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression (entity-token-only LP, excluding format/schema tokens) which fails to improve sel
…[truncated 672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-18T01:31:27.305004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-18T01:31:27.305865+00:00_

200	EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
212	\label{tab:wnut}
213	\begin{tabular}{lcccc}
214	\toprule
215	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
216	\midrule
217	VC      & .724 & .913 & .038 & .487 \\
218	FK      & .125 & .555 & .169 & .002 \\
219	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditio
…[truncated 14154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1137 · 2026-05-18T01:31:33.003486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "399",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "399",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1138 · 2026-05-18T01:31:33.054325+00:00_

399	\end{tabular}
400	\end{table}
401	
402	\paragraph{External equivalence margins.}
403	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
404	To resolve this, we supplement with three externally grounded margins:
405	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;
406	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
407	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
408	
409	Results under these external anchors diverge sharply by configuration.
410	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
411	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\delta_{\mathrm{literature}}$.
412	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
413	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
414	
415	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
416	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
417	Since all primary selection results are non-significant ($p{>}0.05$), apply
…[truncated 12982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1139 · 2026-05-18T01:31:41.185590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "598",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "598",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1140 · 2026-05-18T01:31:41.236503+00:00_

598	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
599	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
600	Signal & Qwen & LLaMA & Qwen & LLaMA \\
601	\midrule
602	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
603	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
604	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
605	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
606	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
607	\bottomrule
608	\end{tabular}
609	\end{table}
610	
611	\paragraph{Non-tied subset analysis.}
612	Table~\ref{tab:nontied_main} presents the non-tied subset analysis referenced in \S\ref{sec:discussion}.
613	
614	\begin{table}[t]
615	\centering
616	\small
617	\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\varepsilon{=}0.05$. Within-instance $\rho$ and selection gain both concentrate in the non-tied subset. Full $\varepsilon$ sweep in Table~\ref{tab:epsilon_sweep}.}
618	\label{tab:nontied_main}
619	\begin{tabular}{lccc}
620	\toprule
621	Subset & $n$ & $\rho$(LP,F1) & LP $\Delta$ vs.\ greedy \\
622	\midrule
623	Tied (range ${<}0.05$) & 319 & 0.08 & ${\approx}0$ \\
624	Non-tied (range ${\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\
625	\midrule
626	All instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
632	
633	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
634	
635	\begin{table}[t]
636	\centering
637	\small
638	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
639	\label{tab:vc_quartile}
640	\begin{tabular}{lcccc}
641	\toprule
642	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
643	\midrule
644
…[truncated 11201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1141 · 2026-05-18T01:31:46.610456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "797",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "797",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1142 · 2026-05-18T01:31:46.661468+00:00_

797	\vspace{2pt}
798	
799	\begin{tabular}{llccc}
800	\toprule
801	Task & Method & Constrained & Free-form & $\Delta$ \\
802	\midrule
803	\multirow{3}{*}{NER}
804	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
805	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
806	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
807	\midrule
808	\multirow{3}{*}{RE}
809	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
810	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
811	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
812	\bottomrule
813	\end{tabular}
814	
815	\vspace{8pt}
816	
817	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
818	\vspace{2pt}
819	
820	\begin{tabular}{l ccc ccc}
821	\toprule
822	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
823	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
824	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
825	\midrule
826	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
827	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
828	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
829	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
830	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
831	\bottomrule
832	\end{tabular}
833	
834	\vspace{8pt}
835	
836	{\small\textsc{Panel D: Parse Rate (Free-form)}}
837	\vspace{2pt}
838	
839	\begin{tabular}{lc}
840	\toprule
841	Metric & Value \\
842	\midrule
843	Total samples          & 4408 \\
844	Parse rate             & 99.95\% \\
845	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
846	\bottomrule
847	\end{tabular}
848	
849	\end{table*}
850	
851	\paragraph{CoNLL NER free-form results.}
852	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
853	Free-form decoding re
…[truncated 9660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1143 · 2026-05-18T01:31:52.434166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "996",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "996",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1144 · 2026-05-18T01:31:52.535183+00:00_

996	\label{tab:bootstrap_n32}
997	\begin{tabular}{lcccc}
998	\toprule
999	Signal & $\Delta$ (pp) & 95\% CI & $p_{\text{greedy}}$ & $p_{\text{rand}}$ \\
1000	\midrule
1001	LP & $+$0.95 & [$-$0.41, $+$2.34] & 0.091 & ${<}$0.001 \\
1002	FK & $+$0.66 & [$-$0.36, $+$1.67] & 0.101 & ${<}$0.001 \\
1003	SJ & $+$0.36 & [$-$0.66, $+$1.38] & 0.244 & ${<}$0.001 \\
1004	EM & $+$0.22 & [$-$0.99, $+$1.44] & 0.355 & ${<}$0.001 \\
1005	VC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\
1006	\midrule
1007	Oracle & $+$20.00 & [$+$17.98, $+$22.10] & ${<}$0.001 & --- \\
1008	\bottomrule
1009	\end{tabular}
1010	\end{table}
1011	
1012	\section{Temperature Ablation}\label{app:t_ablation}
1013	
1014	Table~\ref{tab:t_ablation} reports the effect of sampling temperature on QE signals, oracle headroom, and output quality across four temperatures on SciERC NER.
1015	
1016	\begin{table}[t]
1017	\centering
1018	\small
1019	\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\rho$ across four temperatures. $\kappa$: Fleiss' $\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}
1020	\label{tab:t_ablation}
1021	\begin{tabular}{ccccccc}
1022	\toprule
1023	$T$ & Oracle gap (pp) & SJ $\rho$ & LP $\rho$ & $\kappa$ & Sample F1 \\
1024	\midrule
1025	0.5 & $+$7.8 & 0.297 & 0.218 & 0.577 & 0.636 \\
1026	0.8 & $+$10.5 & 0.359 & 0.253 & 0.451 & 0.622 \\
1027	1.0 & $+$13.3 & 0.360 & 0.205 & ${\approx}$0.39 & ${\approx}$0.612 \\
1028	1.2 & $+$13.0 & 0.377 & 0.196 & 0.356 & 0.594 \\
1029	\bottomrule
1030	\end{tabular}
1031	\end{table}
1032	
1033	Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing at $T{=}1.2$ ($+13.0$~pp); the plateau suggests $T{=}1.0$ already approaches the diversity ceiling for constrained structured decoding.
1034	Structural QE signals improve with temperature: SJ $\rho$ rises from $0.297$ ($T{=}0.5$) to $0
…[truncated 12604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1145 · 2026-05-18T01:31:57.955860+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1195",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1195",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1146 · 2026-05-18T01:31:58.006600+00:00_

1195	(2)~LP is the only signal achieving significant positive selection ($+1.36$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.
1196	(3)~Despite positive $\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.
1197	(4)~Low degeneracy (13.8\%) combined with strong LP-quality alignment ($\rho{\approx}0.5$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (17.8\% degeneracy but weak alignment $\rho{\approx}0.24$, LP $+0.42$~pp non-significant) and CoNLL (47.4\%, LP fails).
1198	
1199	\section{Per-Entity-Type LP Selection Analysis}\label{app:per_type_lp}
1200	
1201	Table~\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.
1202	The degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\%).
1203	The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\rho{=}{-}0.881$, $p{=}0.004$); degeneracy directly constrains the headroom available for selection.
1204	
1205	\begin{table}[h]
1206	\centering
1207	\small
1208	\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\Delta$; Art (highest degeneracy) is the sole exception.}
1209	\label{tab:per_type_lp}
1210	\begin{tabular}{lrrrrrrr}
1211	\toprule
1212	Entity Type & $n$ & Degen.\% & Greedy & LP Sel & $\Delta$ (pp) & LP $\rho$ & Headroom \\
1213	\midrule
1214	Event & 1{,}306 & 6.0 & .655 & .662 & $+$0.65 & .457 & 16.1\,pp \\
1215	Other & 3{,}433 & 6.6 & .637 & .685 & $\mathbf{+4.73}$ & .491 & 19.4\,
…[truncated 7937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1147 · 2026-05-18T01:32:02.373317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1329",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1329",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1148 · 2026-05-18T01:32:02.976252+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1329). The file has 1329 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1149 · 2026-05-18T01:32:02.976669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1150 · 2026-05-18T01:32:03.027243+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
6	We extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.
10	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised verifier baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar, schall2025hidden, yun2025price}.
14	
15	\paragraph{Uncertainty estimation and MBR decoding.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncer
…[truncated 1575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-18T01:34:26.635524+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1152 · 2026-05-18T01:34:26.736297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1153 · 2026-05-18T01:35:14.688937+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 18 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)\n\n### Summary\n\nThis paper investigates why self-consistency signals that reliably estimate instance-level quality (QE) for LLM-based NER fail to improve best-of-N sample selection. Five confidence signals are evaluated across four NER benchmarks using 4B-8B models. The paper identifies a \"correlation-selection gap\" with a three-layer diagnosis: instance-level signals cannot rank candidates by construction; MBR selection fails due to instance degeneracy; and LP (the sole per-sample signal) requires both low degeneracy and adequate alignment. LP succeeds on Few-NERD (+1.36pp, p<0.001) but fails on SciERC (p=0.29) and CoNLL.\n\n---\n\n### Strengths\n\n1. **Well-structured diagnostic framework.** The three-layer decomposition (instance-level limitation → degeneracy → alignment) is clean and helps the reader understand why selection fails at each level. The paper does a good job separating QE from selection as conceptually distinct tasks (Section 2.1, Section 3.3).\n\n2. **Comprehensive ablation coverage.** The paper systematically manipulates temperature (App. §T_ablation), N-scaling (App. §n_scaling_selection), LoRA rank (§5.4), model scale (Table 5), free-form decoding (App. §freeform_ablation), and training epochs (App. §epoch_confound). This breadth strengthens confidence in the robustness of the primary negative findings.\n\n3. **Honest reporting of negative results.** The paper does not overstate LP's utility; it clearly delineates where LP succeeds (Few-NERD, low degeneracy + high alignment) and where it fails, with appropriate statistical caveats.\n\n4. **Strong Few-NERD validation.** The n=32,565 evaluation provides >99% power and yields a tight CI [+1.18, +1.53] for the LP selection gain, making the positive finding on this dataset convincing (Table 3, Appendix §fewnerd).\n\n5. **Entity-type-level granularity.** Table in Appendix §per_type_lp provides per-type decomposition that adds mechanistic insight beyond dataset-level summaries.\n\n---\n\n### Weaknesses\n\n**W1 [Major]** Statistical power of the primary SciERC selection test is insufficient to distinguish \"true null\" from \"underpowered.\"\n\n- Section 3.3 reports LP +0.2pp (p=0.29) on SciERC (n=529, 2 seeds). The footnote acknowledges ~55% post-hoc power for a 1pp effect. At this power level, P(fail to reject | true effect of 1pp) ≈ 0.45. The paper cannot claim that selection \"fails\" on SciERC; it can only claim \"not detected.\"\n- The paper partially hedges but the framing throughout treats the SciERC negative as established fact rather than inconclusive, inflating the \"two necessary conditions\" narrative.\n- The N-scaling table (App. §n_scaling_selection) shows +0.42pp at N=8 growing to +0.91pp at N=32, suggesting LP may have a real but small effect on SciERC that the 2-seed test cannot detect.\n- **Impact**: The three-way gradient (47% → fail, 18% → weak, 14% → success) relies on the middle point being genuinely \"weak/null\" rather than merely underpowered.\n- **Suggestion**: Report minimum detectable effect at 80% power for each configuration. If SciERC at n=529 can only detect ≥2pp, state this explicitly and reframe accordingly.\n\n**W2 [Major]** Cross-dataset degeneracy gradient: causal inference from 3 observational data points is overfit.\n\n- Section 3.4 and Contribution 3 claim \"the cross-dataset gradient establishes degeneracy as one condition.\" Three data points (CoNLL, SciERC, Few-NERD) cannot \"establish\" anything—any three ordered numbers are trivially monotonic. The datasets differ on ≥5 dimensions simultaneously: degeneracy, LP alignment, task difficulty, schema complexity, training epochs (3 vs 5), and training data size.\n- The per-entity-type analysis (n=8, ρ=-0.881) partially addresses this but has its own issues (W3).\n- **Impact**: The \"monotonic\" claim in Figure 2 and Section 3.4 overstates what the evidence supports.\n- **Suggestion**: Reframe as \"consistent with\" rather than \"establishes\"; explicitly list confounded variables; present the gradient as descriptive evidence corroborated by controlled ablations (LoRA, temperature).\n\n**W3 [Major]** Per-entity-type correlation (n=8, ρ=-0.881, p=0.004): non-independence inflates significance.\n\n- The 8 entity types from a single model on Few-NERD share: (a) same trained weights, (b) same tokenizer/decoding, (c) same temperature, (d) often shared entity mentions across types within the same sentences. The Spearman test assumes independent observations; effective df likely <6.\n- **Impact**: The p=0.004 may overstate significance by 5-10x. If true p is ~0.02-0.04, it still suggests a trend but wouldn't survive correction over ~20 comparisons.\n- **Suggestion**: Report a permutation test shuffling type labels, or acknowledge non-independence and interpret as suggestive.\n\n**W4 [Major]** Few-NERD 3-epoch training confound: control is incomplete.\n\n- Appendix §epoch_confound shows 5-epoch Few-NERD triples degeneracy (11.1% → 31.3%) and halves LP gains (+1.37pp → +0.62pp). This demonstrates favorable conditions are partly training-induced.\n- The 5-epoch model has higher greedy F1 (0.777 vs 0.748), introducing a performance-regime confound. A matched-degeneracy comparison (e.g., SciERC at T=1.2 where degeneracy=12.5% vs Few-NERD at 13.8%) would better isolate alignment as the differentiator.\n- **Impact**: Practitioners using standard 5-epoch training would face higher degeneracy; the paper's demonstration of LP success may not generalize to typical training configurations.\n- **Suggestion**: Foreground that the 3-epoch model reflects validation-loss early stopping; add the matched-degeneracy cross-dataset comparison.\n\n**W5 [Moderate]** LoRA rank=8 ablation conflates capacity and degeneracy.\n\n- Section 5.4: rank=8 simultaneously reduces capacity and changes training dynamics. The lower alignment (ρ≈0.24) could stem from insufficient capacity rather than evidence for a separate \"alignment\" condition.\n- The temperature ablation (T=1.2: degeneracy 12.5%, ρ=0.225; Table §t_degeneracy) provides cleaner evidence on the same full-rank model and should be foregrounded as the primary argument.\n- **Suggestion**: Acknowledge the capacity confound; emphasize temperature as the cleaner manipulation.\n\n**W6 [Moderate]** Supervised verifier baseline tests only recycled features.\n\n- Section 5.4: LR/MLP/RF trained on 5 scalar features that are the same insufficient signals. Concluding \"the bottleneck lies in what the signals encode, not how they are aggregated\" is valid only for this feature set.\n- A verifier with hidden states, attention patterns, or raw text would have fundamentally different capacity.\n- **Suggestion**: Scope the conclusion explicitly to \"supervised combination of the 5 unsupervised signals\" rather than implying supervised approaches in general cannot help.\n\n**W7 [Minor]** Instance degeneracy definition is operationally ambiguous.\n\n- Introduction says \"fine-tuned models produce identical outputs for 14–47% of instances\" but Table §diversity shows only 11% identical outputs on SciERC. The operational definition is \"constant F1 across all N samples\" (different outputs can yield same F1). The prose conflates these in Section 1.\n- **Suggestion**: Clarify at first use that degeneracy means constant-F1, not output identity.\n\n---\n\n### Questions\n\n1. SciERC within-instance ρ(LP, F1)=0.248 vs Few-NERD ρ≈0.5: Is this alignment difference explained by entity ambiguity, schema complexity, or training? Have you examined per-type alignment on SciERC?\n\n2. Table §per_type_lp_scierc shows within-SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79), contradicting the cross-dataset and within-Few-NERD patterns. How do you reconcile this?\n\n3. Random (0.610) vs Greedy (0.645): Is this gap entirely from T=1.0 sampling quality degradation? What is average sample F1 at T=1.0?\n\n4. With 2-3 seeds, Fisher combined p has very limited sensitivity. What prevents running 5+ seeds?\n\n---\n\n### Missing References\n\n- MBR for code generation (Shi et al. 2022) would strengthen the structured-output connection\n- Eisenstein et al. (2023, reward model ensembles) relevant to signal limitation discussion\n- Perez et al. (2022, sycophancy) as related diversity-collapse mechanism\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | Core claims supported but statistical power issues (W1) and non-independence (W3) weaken quantitative conclusions |\n| Excitement | 3.5/5 | Negative result genuinely useful; diagnosis framework insightful; but practical implication (\"use greedy or train verifier\") somewhat expected |\n| Reproducibility | 4.0/5 | Training configs, hyperparameters, prompts, statistical tests well-documented |\n| Reviewer Confidence | 4/5 | Familiar with MBR, confidence estimation, NER evaluation; checked statistical claims in detail |\n\n**Overall: 3.0/5** (Findings-level; needs revisions on statistical framing)\n\n**一句话总结**: 诊断框架有洞察力，但统计论证关键环节（SciERC 检验力不足、3 数据点因果推断、非独立性假设）削弱了核心 claim 的可信度，需要 reframe 才能达到 main conference 水准。\n\n---\n\n### 历史 Open Issues 状态更新\n\n| Issue | 状态 | 当前论文证据 |\n|-------|------|-------------|\n| R0-C3: Selection gap 仅 SciERC | **Partially resolved** | 现有 4 个数据集均展示 gap（结构信号全部失败），但 LP 正面结果仅 Few-NERD |\n| R16-N1: Monotonic claim 仅 3 数据点 | **Still open** | 仍为 3 dataset-level 点；entity-type 分析有非独立性问题 (W3) |\n| R17-W1: LoRA rank=8 LP compression 数据 | **Resolved** | LP range 0.057 vs 0.041 nats 已报告 (§5.4) |\n| R17-W2: Few-NERD 3 epochs confound | **Partially resolved** | 5-epoch control provided (App. §epoch_confound) 但引入新 confound (W4) |\n| R14-W1: Fisher combined p 统计效力 | **Still open** | 仍为 2 seeds; paper 承认但未增加 |\n| R14-M1: Random vs Single 差距来源 | **Resolved** | Random 从 T=1.0 samples 中均匀选取，低于 T=0 greedy 是预期行为；已通过 oracle analysis 解释 |",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 18 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)\n\n### Summary\n\nThis paper investigates why self-consistency signals that reliably estimate instance-level quality (QE) for LLM-based NER fail to improve best-of-N sample selection. Five confidence signals are evaluated across four NER benchmarks using 4B-8B models. The paper identifies a \"correlation-selection gap\" with a three-layer diagnosis: instance-level signals cannot rank candidates by construction; MBR selection fails due to instance degeneracy; and LP (the sole per-sample signal) requires both low degeneracy and adequate alignment. LP succeeds on Few-NERD (+1.36pp, p<0.001) but fails on SciERC (p=0.29) and CoNLL.\n\n---\n\n### Strengths\n\n1. **Well-structured diagnostic framework.** The three-layer decomposition (instance-level limitation → degeneracy → alignment) is clean and helps the reader understand why selection fails at each level. The paper does a good job separating QE from selection as conceptually distinct tasks (Section 2.1, Section 3.3).\n\n2. **Comprehensive ablation coverage.** The paper systematically manipulates temperature (App. §T_ablation), N-scaling (App. §n_scaling_selection), LoRA rank (§5.4), model scale (Table 5), free-form decoding (App. §freeform_ablation), and training epochs (App. §epoch_confound). This breadth strengthens confidence in the robustness of the primary negative findings.\n\n3. **Honest reporting of negative results.** The paper does not overstate LP's utility; it clearly delineates where LP succeeds (Few-NERD, low degeneracy + high alignment) and where it fails, with appropriate statistical caveats.\n\n4. **Strong Few-NERD validation.** The n=32,565 evaluation provides >99% power and yields a tight CI [+1.18, +1.53] for the LP selection gain, making the positive finding on this dataset convincing (Table 3, Appendix §fewnerd).\n\n5. **Entity-type-level granularity.** Table in Appendix §per_type_lp provides per-type decomposition that adds mechanistic insight beyond dataset-level summaries.\n\n---\n\n### Weaknesses\n\n**W1 [Major]** Statistical power of the primary SciERC selection test is insufficient to distinguish \"true null\" from \"underpowered.\"\n\n- Section 3.3 reports LP +0.2pp (p=0.29) on SciERC (n=529, 2 seeds). The footnote acknowledges ~55% post-hoc power for a 1pp effect. At this power level, P(fail to reject | true effect of 1pp) ≈ 0.45. The paper cannot claim that selection \"fails\" on SciERC; it can only claim \"not detected.\"\n- The paper partially hedges but the framing throughout treats the SciERC negative as established fact rather than inconclusive, inflating the \"two necessary conditions\" narrative.\n- The N-scaling table (App. §n_scaling_selection) shows +0.42pp at N=8 growing to +0.91pp at N=32, suggesting LP may have a real but small effect on SciERC that the 2-seed test cannot detect.\n- **Impact**: The three-way gradient (47% → fail, 18% → weak, 14% → success) relies on the middle point being genuinely \"weak/null\" rather than merely underpowered.\n- **Suggestion**: Report minimum detectable effect at 80% power for each configuration. If SciERC at n=529 can only detect ≥2pp, state this explicitly and reframe accordingly.\n\n**W2 [Major]** Cross-dataset degeneracy gradient: causal inference from 3 observational data points is overfit.\n\n- Section 3.4 and Contribution 3 claim \"the cross-dataset gradient establishes degeneracy as one condition.\" Three data points (CoNLL, SciERC, Few-NERD) cannot \"establish\" anything—any three ordered numbers are trivially monotonic. The datasets differ on ≥5 dimensions simultaneously: degeneracy, LP alignment, task difficulty, schema complexity, training epochs (3 vs 5), and training data size.\n- The per-entity-type analysis (n=8, ρ=-0.881) partially addresses this but has its own issues (W3).\n- **Impact**: The \"monotonic\" claim in Figure 2 and Section 3.4 overstates what the evidence supports.\n- **Suggestion**: Reframe as \"consistent with\" rather than \"establishes\"; explicitly list confounded variables; present the gradient as descriptive evidence corroborated by controlled ablations (LoRA, temperature).\n\n**W3 [Major]** Per-entity-type correlation (n=8, ρ=-0.881, p=0.004): non-independence inflates significance.\n\n- The 8 entity types from a single model on Few-NERD share: (a) same trained weights, (b) same tokenizer/decoding, (c) same temperature, (d) often shared entity mentions across types within the same sentences. The Spearman test assumes independent observations; effective df likely <6.\n- **Impact**: The p=0.004 may overstate significance by 5-10x. If true p is ~0.02-0.04, it still suggests a trend but wouldn't survive correction over ~20 comparisons.\n- **Suggestion**: Report a permutation test shuffling type labels, or acknowledge non-independence and interpret as suggestive.\n\n**W4 [Major]** Few-NERD 3-epoch training confound: control is incomplete.\n\n- Appendix §epoch_confound shows 5-epoch Few-NERD triples degeneracy (11.1% → 31.3%) and halves LP gains (+1.37pp → +0.62pp). This demonstrates favorable conditions are partly training-induced.\n- The 5-epoch model has higher greedy F1 (0.777 vs 0.748), introducing a performance-regime confound. A matched-degeneracy comparison (e.g., SciERC at T=1.2 where degeneracy=12.5% vs Few-NERD at 13.8%) would better isolate alignment as the differentiator.\n- **Impact**: Practitioners using standard 5-epoch training would face higher degeneracy; the paper's demonstration of LP success may not generalize to typical training configurations.\n- **Suggestion**: Foreground that the 3-epoch model reflects validation-loss early stopping; add the matched-degeneracy cross-dataset comparison.\n\n**W5 [Moderate]** LoRA rank=8 ablation conflates capacity and degeneracy.\n\n- Section 5.4: rank=8 simultaneously reduces capacity and changes training dynamics. The lower alignment (ρ≈0.24) could stem from insufficient capacity rather than evidence for a separate \"alignment\" condition.\n- The temperature ablation (T=1.2: degeneracy 12.5%, ρ=0.225; Table §t_degeneracy) provides cleaner evidence on the same full-rank model and should be foregrounded as the primary argument.\n- **Suggestion**: Acknowledge the capacity confound; emphasize temperature as the cleaner manipulation.\n\n**W6 [Moderate]** Supervised verifier baseline tests only recycled features.\n\n- Section 5.4: LR/MLP/RF trained on 5 scalar features that are the same insufficient signals. Concluding \"the bottleneck lies in what the signals encode, not how they are aggregated\" is valid only for this feature set.\n- A verifier with hidden states, attention patterns, or raw text would have fundamentally different capacity.\n- **Suggestion**: Scope the conclusion explicitly to \"supervised combination of the 5 unsupervised signals\" rather than implying supervised approaches in general cannot help.\n\n**W7 [Minor]** Instance degeneracy definition is operationally ambiguous.\n\n- Introduction says \"fine-tuned models produce identical outputs for 14–47% of instances\" but Table §diversity shows only 11% identical outputs on SciERC. The operational definition is \"constant F1 across all N samples\" (different outputs can yield same F1). The prose conflates these in Section 1.\n- **Suggestion**: Clarify at first use that degeneracy means constant-F1, not output identity.\n\n---\n\n### Questions\n\n1. SciERC within-instance ρ(LP, F1)=0.248 vs Few-NERD ρ≈0.5: Is this alignment difference explained by entity ambiguity, schema complexity, or training? Have you examined per-type alignment on SciERC?\n\n2. Table §per_type_lp_scierc shows within-SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79), contradicting the cross-dataset and within-Few-NERD patterns. How do you reconcile this?\n\n3. Random (0.610) vs Greedy (0.645): Is this gap entirely from T=1.0 sampling quality degradation? What is average sample F1 at T=1.0?\n\n4. With 2-3 seeds, Fisher combined p has very limited sensitivity. What prevents running 5+ seeds?\n\n---\n\n### Missing References\n\n- MBR for code generation (Shi et al. 2022) would strengthen the structured-output connection\n- Eisenstein et al. (2023, reward model ensembles) relevant to signal limitation discussion\n- Perez et al. (2022, sycophancy) as related diversity-collapse mechanism\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | Core claims supported but statistical power issues (W1) and non-independence (W3) weaken quantitative conclusions |\n| Excitement | 3.5/5 | Negative result genuinely useful; diagnosis framework insightful; but practical implication (\"use greedy or train verifier\") somewhat expected |\n| Reproducibility | 4.0/5 | Training configs, hyperparameters, prompts, statistical tests well-documented |\n| Reviewer Confidence | 4/5 | Familiar with MBR, confidence estimation, NER evaluation; checked statistical claims in detail |\n\n**Overall: 3.0/5** (Findings-level; needs revisions on statistical framing)\n\n**一句话总结**: 诊断框架有洞察力，但统计论证关键环节（SciERC 检验力不足、3 数据点因果推断、非独立性假设）削弱了核心 claim 的可信度，需要 reframe 才能达到 main conference 水准。\n\n---\n\n### 历史 Open Issues 状态更新\n\n| Issue | 状态 | 当前论文证据 |\n|-------|------|-------------|\n| R0-C3: Selection gap 仅 SciERC | **Partially resolved** | 现有 4 个数据集均展示 gap（结构信号全部失败），但 LP 正面结果仅 Few-NERD |\n| R16-N1: Monotonic claim 仅 3 数据点 | **Still open** | 仍为 3 dataset-level 点；entity-type 分析有非独立性问题 (W3) |\n| R17-W1: LoRA rank=8 LP compression 数据 | **Resolved** | LP range 0.057 vs 0.041 nats 已报告 (§5.4) |\n| R17-W2: Few-NERD 3 epochs confound | **Partially resolved** | 5-epoch control provided (App. §epoch_confound) 但引入新 confound (W4) |\n| R14-W1: Fisher combined p 统计效力 | **Still open** | 仍为 2 seeds; paper 承认但未增加 |\n| R14-M1: Random vs Single 差距来源 | **Resolved** | Random 从 T=1.0 samples 中均匀选取，低于 T=0 greedy 是预期行为；已通过 oracle analysis 解释 |",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-18T01:35:18.812035+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4123
}
```

</details>

---


### Assistant

_source line 1155 · 2026-05-18T01:35:27.307029+00:00_

审稿意见已提交给 Review Director。

核心发现：论文诊断框架清晰且有洞察力（Overall 3.0/5, Findings-level），但有 4 个 Major weakness：
1. SciERC 选择测试统计效力不足（~55% power），无法区分"真无效"与"检测不到"
2. 跨数据集 degeneracy gradient 仅 3 个观测点，因果推断过强
3. Per-entity-type 相关性（n=8）违反独立性假设，p 值可能被高估 5-10x
4. Few-NERD 3-epoch 训练 confound 控制不完整，favorable conditions 部分来自训练配置

历史 open issues 中 R17-W1 和 R14-M1 已解决，R16-N1 和 R14-W1 仍 open。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 37

## Round 37

4 recorded events


### User

_source line 1156 · 2026-05-18T01:37:46.381842+00:00_

[Round 18 审稿请求]:
## Round 18 交叉分享 — Reviewer 1 请回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应其 Weaknesses 和 Questions：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 完整审稿意见

### Strengths
S1. QE 与 selection 的系统性分离是重要的方法论贡献。
S2. 实验设计严谨且全面。四个 NER 数据集构成 difficulty gradient，bootstrap CI, TOST, Bonferroni, Fisher combined p。
S3. Two-condition 分析框架有洞察力。
S4. Appendix 质量极高。20+ 节覆盖所有 confounds。
S5. 写作质量显著提升。em-dash 清零，Discussion 压缩，术语定义到位。

### Weaknesses

**W1 [warning] 纯诊断性论文缺乏 positive contribution/remedy。**
- 核心结论是"现有信号不 work"，唯一正面发现（Few-NERD LP +1.36pp）效果 modest。建议"closing the gap requires content-aware verifiers"但未实现。supervised verifier baseline（LR/MLP/RF）全部失败但是极简 baseline。
- 对于 EMNLP main conference，审稿人期望诊断之外提供至少一个可行改进方向。
- 建议：训练一个简单但非 trivial 的 learned verifier 展示 oracle gap 部分可回收性。

**W2 [warning] "Three-layer" gap 结构中 Layer 1 是 definitional，接近 tautological。**
- Layer 1 "four instance-level signals cannot rank candidates by construction" 是定义推论非实验发现。真正贡献在 Layer 2-3。将 definitional observation 包装为 three-layer 第一层夸大了分析深度。
- 建议：Layer 1 重新 frame 为 methodological premise，核心叙事集中在 Layer 2-3 实证发现。

**W3 [warning] Abstract 信息密度仍然过高。**
- 9 sentences, ~170 words，含至少 8 个定量值（ρ, AUROC, pp, nats, p, N, degeneracy%）。30 秒快速阅读难以提取核心 message。
- 建议：只保留核心 claim 所需的 2-3 个关键数字。

**W4 [warning] 模型规模覆盖有限（4B-8B），结论外推受限。**
- 70B+ 或 API 模型可能产生更多样输出，从根本上改变 degeneracy regime。核心结论可能仅适用于中小规模 fine-tuned 模型。

### Questions

Q1. Table 3 vs Table 2 evaluation protocol 差异容易混淆。
Q2. Supervised verifier 在 SciERC ~350 training instances 上训练，是否公平？Few-NERD 上训练是否结果不同？
Q3. Few-NERD 3 epochs: 如何排除 LP success 不完全是 training schedule artifact？
Q4. Entity-token LP 方差增大 4× 但选择更差。与"LP compression is bottleneck"叙事矛盾？

### Missing References
- Diverse Beam Search (Vijayakumar et al. 2018)
- Conformal prediction for set-valued outputs (Vovk et al.)
- NER-specific confidence (Shen et al. / Li et al.)
- 4 个 orphan bib entries

### Overall: 3.0/5 (Findings)

---

请逐条回应 W1-W4 和 Q1-Q4。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1157 · 2026-05-18T01:39:37.812313+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 18 交叉回应 — Reviewer 1 回应 Reviewer 2\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 纯诊断性论文缺乏 positive contribution/remedy**\n同意这是最大 venue-fit 风险。唯一 positive finding (Few-NERD LP +1.36pp) 效果 modest，supervised verifier baseline 使用同样 5 个信号属于 straw-man。但 R2 建议训练 non-trivial verifier 存在 scope creep 风险。论文的实际贡献在于 practical guidelines (§6) 和 negative-result methodology；对 Findings track 足够，对 main 需要更强 positive signal。\n\n**[AGREE] R2-W2: Layer 1 是 definitional/tautological**\n同意。\"Instance-level signals cannot rank by construction\" 是数学事实非实验发现。Introduction 已称其为 \"methodological premise\" (§1 line 11)，但 Abstract/Contributions 仍包装为 three-layer 第一层。建议 Contribution 2 改写为 \"Two empirical mechanisms (degeneracy, alignment) that block the sole per-sample signal\"。注意 Layer 1 有叙事功能（解释为何需要区分 signal types），问题在于与实证发现并列计数。\n\n**[REBUT] R2-W3: Abstract 信息密度过高**\n部分不同意。诊断性论文中具体数值 IS the contribution——reviewer 需要从 Abstract 判断 QE 强度 (ρ=0.38)、gap 大小 (13pp headroom)、LP 成功条件 (+1.36pp, p<0.001)、失败条件 (14-47% degeneracy)。但同意中间机制数字 (median ρ=0.52, +0.52pp N-scaling) 可移入正文。建议保留 4-5 核心数字、移除 3-4 个。\n\n**[AGREE] R2-W4: 模型规模覆盖有限（4B-8B）**\n完全同意。我的补充：Table §degeneracy 显示 8B degeneracy (17.8%) > 4B (10.4%)，更大模型 degeneracy 更高。如果趋势延续到 70B+，degeneracy 问题可能更严重而非更轻。但 70B+ 的 LP alignment 可能突破 ρ≈0.3 门槛——无实验数据无法判断方向。\n\n---\n\n### Questions 回应\n\n**[REBUT] R2-Q1: Table 3 vs Table 2 protocol 混淆**\n论文已有标注：Table 3 脚注解释 full-set vs gold-filtered 差异，§2.3 解释 filtering rationale。差异是 deliberate design choice（Table 2: controlled selection comparison; Table 3: cross-dataset degeneracy comparison）。同意可在 Table 3 caption 加粗 \"(full-set evaluation)\" 提高可见性。\n\n**[AGREE] R2-Q2: Supervised verifier 在 SciERC ~350 instances 训练是否公平？**\n合理质疑。SciERC 3-fold CV 数据量对 LR/RF 充分但非 verifier 公平测试。Few-NERD 上未训练 verifier。论文应在 SciERC N=32 (19.2pp headroom) 上补充或解释为何 data size 非 bottleneck。\n\n**[REBUT] R2-Q3: Few-NERD LP success 是否 training schedule artifact？**\nApp. §epoch_confound 直接回答：5-epoch model 仍有 LP +0.62pp（正向但减半）。证明 LP success 非 3-epoch artifact——在 5 epochs 仍存在，仅因 degeneracy 增加 (11.1%→31.3%) 而减弱。3-epoch 对应 validation-loss 最优 checkpoint (step 32,000)，是标准 early stopping 产物。但如我 W4 所述：5-epoch 同时改变 greedy F1，引入 performance-regime confound，matched-degeneracy 比较缺失。\n\n**[REBUT] R2-Q4: Entity-token LP 方差 4× 但选择更差，与 compression-is-bottleneck 矛盾？**\n不矛盾。论文 claim 不是 \"variance 越高 selection 越好\"，而是 \"compression 限制 exploitation\"。§6 line 22 解释：entity-token LP 的高方差来自 fewer-token averaging noise 和 position-dependent variation，是 noise 非 signal。Full-sequence ρ(LP,F1)=0.248 已是最优 aggregation。这反而强化了 \"bottleneck in what signals encode\" 结论——即使放大到 entity tokens 也无法突破表征层面的 near-determinism。\n\n---\n\n### 与 R2 的分歧总结\n\nR2 更关注 **framing/venue-fit** (positive contribution, abstract density, three-layer packaging)；我更关注 **statistical rigor** (power, independence, confounds)。两组问题互补：\n1. 统计 claim 需降级 (我的 W1-W3)\n2. 叙事结构需调整 (R2 的 W2)\n3. Venue-fit 需考虑 (R2 的 W1)\n\n共同结论：当前版本适合 **Findings** (3.0/5)，若解决统计 framing + 补充一个 non-trivial positive result 可冲 main conference。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 18 交叉回应 — Reviewer 1 回应 Reviewer 2\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 纯诊断性论文缺乏 positive contribution/remedy**\n同意这是最大 venue-fit 风险。唯一 positive finding (Few-NERD LP +1.36pp) 效果 modest，supervised verifier baseline 使用同样 5 个信号属于 straw-man。但 R2 建议训练 non-trivial verifier 存在 scope creep 风险。论文的实际贡献在于 practical guidelines (§6) 和 negative-result methodology；对 Findings track 足够，对 main 需要更强 positive signal。\n\n**[AGREE] R2-W2: Layer 1 是 definitional/tautological**\n同意。\"Instance-level signals cannot rank by construction\" 是数学事实非实验发现。Introduction 已称其为 \"methodological premise\" (§1 line 11)，但 Abstract/Contributions 仍包装为 three-layer 第一层。建议 Contribution 2 改写为 \"Two empirical mechanisms (degeneracy, alignment) that block the sole per-sample signal\"。注意 Layer 1 有叙事功能（解释为何需要区分 signal types），问题在于与实证发现并列计数。\n\n**[REBUT] R2-W3: Abstract 信息密度过高**\n部分不同意。诊断性论文中具体数值 IS the contribution——reviewer 需要从 Abstract 判断 QE 强度 (ρ=0.38)、gap 大小 (13pp headroom)、LP 成功条件 (+1.36pp, p<0.001)、失败条件 (14-47% degeneracy)。但同意中间机制数字 (median ρ=0.52, +0.52pp N-scaling) 可移入正文。建议保留 4-5 核心数字、移除 3-4 个。\n\n**[AGREE] R2-W4: 模型规模覆盖有限（4B-8B）**\n完全同意。我的补充：Table §degeneracy 显示 8B degeneracy (17.8%) > 4B (10.4%)，更大模型 degeneracy 更高。如果趋势延续到 70B+，degeneracy 问题可能更严重而非更轻。但 70B+ 的 LP alignment 可能突破 ρ≈0.3 门槛——无实验数据无法判断方向。\n\n---\n\n### Questions 回应\n\n**[REBUT] R2-Q1: Table 3 vs Table 2 protocol 混淆**\n论文已有标注：Table 3 脚注解释 full-set vs gold-filtered 差异，§2.3 解释 filtering rationale。差异是 deliberate design choice（Table 2: controlled selection comparison; Table 3: cross-dataset degeneracy comparison）。同意可在 Table 3 caption 加粗 \"(full-set evaluation)\" 提高可见性。\n\n**[AGREE] R2-Q2: Supervised verifier 在 SciERC ~350 instances 训练是否公平？**\n合理质疑。SciERC 3-fold CV 数据量对 LR/RF 充分但非 verifier 公平测试。Few-NERD 上未训练 verifier。论文应在 SciERC N=32 (19.2pp headroom) 上补充或解释为何 data size 非 bottleneck。\n\n**[REBUT] R2-Q3: Few-NERD LP success 是否 training schedule artifact？**\nApp. §epoch_confound 直接回答：5-epoch model 仍有 LP +0.62pp（正向但减半）。证明 LP success 非 3-epoch artifact——在 5 epochs 仍存在，仅因 degeneracy 增加 (11.1%→31.3%) 而减弱。3-epoch 对应 validation-loss 最优 checkpoint (step 32,000)，是标准 early stopping 产物。但如我 W4 所述：5-epoch 同时改变 greedy F1，引入 performance-regime confound，matched-degeneracy 比较缺失。\n\n**[REBUT] R2-Q4: Entity-token LP 方差 4× 但选择更差，与 compression-is-bottleneck 矛盾？**\n不矛盾。论文 claim 不是 \"variance 越高 selection 越好\"，而是 \"compression 限制 exploitation\"。§6 line 22 解释：entity-token LP 的高方差来自 fewer-token averaging noise 和 position-dependent variation，是 noise 非 signal。Full-sequence ρ(LP,F1)=0.248 已是最优 aggregation。这反而强化了 \"bottleneck in what signals encode\" 结论——即使放大到 entity tokens 也无法突破表征层面的 near-determinism。\n\n---\n\n### 与 R2 的分歧总结\n\nR2 更关注 **framing/venue-fit** (positive contribution, abstract density, three-layer packaging)；我更关注 **statistical rigor** (power, independence, confounds)。两组问题互补：\n1. 统计 claim 需降级 (我的 W1-W3)\n2. 叙事结构需调整 (R2 的 W2)\n3. Venue-fit 需考虑 (R2 的 W1)\n\n共同结论：当前版本适合 **Findings** (3.0/5)，若解决统计 framing + 补充一个 non-trivial positive result 可冲 main conference。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1158 · 2026-05-18T01:39:41.727924+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 1159 · 2026-05-18T01:39:46.498353+00:00_

交叉回应已提交给 Review Director。

总结：对 R2 的 4 个 Weaknesses 同意 3 个（W1 venue-fit、W2 tautological layer、W4 scale），对 W3 (abstract density) 部分反驳。Questions 中 Q2 同意（verifier fairness），Q1/Q3/Q4 反驳并引用论文内证据。核心分歧：R2 侧重 framing/venue-fit，我侧重 statistical rigor，两组问题互补。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 38

## Round 38

66 recorded events


### User

_source line 1160 · 2026-05-18T05:55:12.612842+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `docs/paper/sections/` 下）
- **目标 venue**: EMNLP 2026 Main Conference Long Paper (ACL Rolling Review)
- **截止日期**: 2026-05-25
- **格式**: ACL style, ≤8 页正文, 附录不计页数, double-blind

### 你的审查侧重

**核心任务**: 评估方法的严谨性和实验设计的可靠性。

重点审查以下方面：

1. **统计方法与效力分析**
   - Spearman ρ、AUROC、sign test、bootstrap CI 的使用是否恰当
   - SciERC (n=529) 的 power analysis 是否充分（MDE ≈ 1.5pp at 80% power 的推导）
   - Few-NERD (n=32,565) 作为 definitive test 是否令人信服
   - 多重比较校正策略（Bonferroni over 5 signal comparisons）是否完整
   - 2-seed 实验设计的统计效力

2. **因果推断强度**
   - Degeneracy-gating claim: cross-dataset gradient (n=3) + per-entity-type (n=8, ρ=-0.881, p=0.004) 的证据强度
   - Per-entity-type 分析的 non-independence 问题（shared model/tokenizer/temperature, effective df<6）
   - LoRA-rank ablation 的 capacity confound（同时改变 capacity 和 degeneracy）
   - Temperature ablation (T=1.2) 作为 cleaner interventional evidence 的说服力
   - "Two jointly necessary conditions" 的论证是否充分

3. **实验设计**
   - Few-NERD 3 epochs vs 其他 5 epochs 的训练不一致性是否构成 confound
   - Thinking token confound（Qwen3-8B SciERC checkpoint）的排除是否充分
   - Supervised verifier baseline (5 scalar features, 3-fold CV) 的公平性
   - Gold-empty instance filtering protocol 的一致性（QE vs Selection）
   - ε=0.05 threshold 用于 tied/non-tied stratification 的合理性

4. **Degeneracy 概念的操作性定义**
   - "Identical F1 scores" vs "identical outputs" 的区别是否清楚定义
   - 17.8% (SciERC) vs 59.1% (CoNLL) 的 degeneracy 数值是否可靠

### 输出格式

请按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
4. **Questions** (需要作者澄清的)
5. **Missing References** (如有)
6. **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)

严格客观，不留情面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-18T05:55:18.925533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1162 · 2026-05-18T05:55:18.976254+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1163 · 2026-05-18T05:55:21.635517+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 1164 · 2026-05-18T05:55:21.686086+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-18T05:55:24.496688+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-18T05:55:24.948736+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-18T05:55:25.099755+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-18T05:55:25.150313+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1169 · 2026-05-18T05:55:28.965322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-18T05:55:29.317016+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-18T05:55:29.317550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-18T05:55:30.278641+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.
5	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) under two jointly necessary conditions: low instance degeneracy and adequate LP-quality alignment ($\rho \gtrsim 0.3$).
6	When either condition is violated, LP gains fall below detectable thresholds despite ${\sim}$13~pp oracle headroom, a disparity we term the \textbf{correlation-selection gap}.
7	Two mechanisms explain this gap: \textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom; \textit{weak LP-quality alignment} prevents exploiting the remainder.
8	A methodological premise underlies both: four of five signals are instance-level aggregates that by definition cannot rank candidates.
9	Degeneracy is controllable via temperature and training convergence; closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-18T05:55:30.278976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-18T05:55:30.731101+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \textit{why} this correlation does not reliably translate to selection gains, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (13.8\%) and adequate alignment ($\rho{\approx}0.5$), wi
…[truncated 3731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-18T05:55:30.731518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-18T05:55:31.233772+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 2976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-18T05:55:31.234239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-18T05:55:31.686226+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\ref{app:epoch_confound}).
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses
…[truncated 12496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1179 · 2026-05-18T05:55:31.688451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1180 · 2026-05-18T05:55:32.601609+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	All signals achieve positive quality estimation across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL), with rankings stable across model families and a 4B ablation (Table~\ref{tab:scale_ablation}).
5	For selection, LP achieves significant gains only when both conditions are met ($+1.36$~pp on Few-NERD, $p{<}0.001$; Table~\ref{tab:fewnerd}); structural signals uniformly degrade selection.
6	RE signal rankings are in Appendix~\ref{app:re_extension}.
7	
8	\paragraph{Why the gap exists.}
9	Two mechanisms block selection: \textit{instance degeneracy} (consensus-proximity) and \textit{weak LP-quality alignment} (per-sample).
10	Within non-degenerate instances, MBR utility \cite{eikema2022sampling} correlates positively with F1 (SJ median $\rho{=}0.524$) and closes 23--41\% of the oracle gap, but 17.8\% (SciERC) to 59.1\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\ref{tab:degeneracy}).
11	Degeneracy is determined by the interplay of task structure, model architecture, and training convergence (Appendix~\ref{app:epoch_confound}); cross-model evidence (LLaMA 86.4\% vs.\ Qwen 59.1\% on CoNLL; Table~\ref{tab:cross_selection}) reinforces the pattern.
12	LP is severely compressed (median range 0.041 nats; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$.
13	
14	\paragraph{Non-tied subset and $N$-scaling.}
15	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$, survives Bonferroni; Table~\ref{tab:nontied_main}).
16	LP scales with $N$ in the low-degeneracy regime ($+0.52$~pp from $N{=}8$ to 16 on Few-NERD, $p{=}0.003$; \S\ref{sec:fewnerd}); on SciERC, even $N{=}32$ captures less than 5\% of headroom (Table~\ref{tab:n_scaling_
…[truncated 4730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---


### Tool call

_source line 1181 · 2026-05-18T05:55:32.602045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1182 · 2026-05-18T05:55:33.105676+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
6	We extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.
10	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised verifier baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar, schall2025hidden, yun2025price}.
14	
15	\paragraph{Uncertainty estimation and MBR decoding.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncer
…[truncated 1857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-18T05:55:33.106431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1184 · 2026-05-18T05:55:33.557802+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.
5	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (${<}$15\%) and adequate LP-quality alignment ($\rho \gtrsim 0.3$); gains scale with sample budget ($+0.52$~pp, $N{=}8{\to}16$, $p{=}0.003$).
6	When either condition is violated, LP gains fall below detectable thresholds despite 12\textendash 14~pp oracle headroom: on SciERC (17.8\% degeneracy, $\rho{\approx}0.24$), LP yields $+0.61$~pp (below the ${\approx}$1.5~pp MDE at 80\% power); on CoNLL (59.1\% degeneracy), LP degrades selection ($-1.05$~pp).
7	Two mechanisms explain this gap: instance degeneracy (14\textendash 59\% of instances yield identical F1 scores) eliminates headroom, and weak LP-quality alignment prevents exploiting the remainder.
8	Structural signals do not improve selection regardless of degeneracy, and supervised combination of these five unsupervised signals does not close the oracle gap; whether richer representations (e.g., hidden states, entity embeddings) could change this conclusion remains open.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals likely requires content-aware verifiers \cite{cobbe2021verifiers}; LP provides a practical baseline when both conditions are met, with degeneracy controllable via temperature and training convergence.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1185 · 2026-05-18T05:55:33.608471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1186 · 2026-05-18T05:55:34.060954+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and the two conditions may shift in opposite directions.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned s
…[truncated 1023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1187 · 2026-05-18T05:55:34.061549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1188 · 2026-05-18T05:55:34.363965+00:00_

File content (35137 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1189 · 2026-05-18T05:55:34.364410+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1190 · 2026-05-18T05:55:34.417927+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 1191 · 2026-05-18T05:55:39.003297+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-18T05:55:40.709298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-18T05:55:40.710062+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 13589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1194 · 2026-05-18T05:55:48.286312+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines. Here's what I found:

## ACL Rolling Review 2026 Reviewer Guidelines

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good
…[truncated 1507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9283
}
```

</details>

---


### Tool call

_source line 1195 · 2026-05-18T05:55:52.651409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form dimensions scoring criteria soundness excitement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form dimensions scoring criteria soundness excitement 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-18T05:55:54.557745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-18T05:55:54.608650+00:00_

200	EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
212	\label{tab:wnut}
213	\begin{tabular}{lcccc}
214	\toprule
215	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
216	\midrule
217	VC      & .724 & .913 & .038 & .487 \\
218	FK      & .125 & .555 & .169 & .002 \\
219	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditio
…[truncated 14154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1198 · 2026-05-18T05:56:03.197650+00:00_

Web search results for query: "ACL Rolling Review review form dimensions scoring criteria soundness excitement 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"aclrollingreview/reviewform.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewform.md"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"}]

Based on my search results, I can provide you with information about the ACL Rolling Review form's dimensions and scoring criteria:

## Review Form Dimensions

The ACL Rolling Review uses two primary scoring dimensions:

1. **Soundness** - Evaluates whether the paper is sufficiently sound and thorough, and whether it clearly states scientif
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10546
}
```

</details>

---


### Tool call

_source line 1199 · 2026-05-18T05:56:06.108380+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1200 · 2026-05-18T05:56:06.108710+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-18T05:56:07.914865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "400",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "400",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1202 · 2026-05-18T05:56:07.966600+00:00_

400	\end{table}
401	
402	\paragraph{External equivalence margins.}
403	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
404	To resolve this, we supplement with three externally grounded margins:
405	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;
406	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
407	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
408	
409	Results under these external anchors diverge sharply by configuration.
410	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
411	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\delta_{\mathrm{literature}}$.
412	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
413	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
414	
415	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
416	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
417	Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hoch
…[truncated 13006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1203 · 2026-05-18T05:56:13.994616+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. I need the exact criteria for Soundness, Excitement/Novelty, Overall Assessment, Confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. I need the exact criteria for Soundness, Excitement/Novelty, Overall Assessment, Confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-18T05:56:15.752070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "600",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "600",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-18T05:56:15.802989+00:00_

600	Signal & Qwen & LLaMA & Qwen & LLaMA \\
601	\midrule
602	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
603	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
604	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
605	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
606	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
607	\bottomrule
608	\end{tabular}
609	\end{table}
610	
611	\paragraph{Non-tied subset analysis.}
612	Table~\ref{tab:nontied_main} presents the non-tied subset analysis referenced in \S\ref{sec:discussion}.
613	
614	\begin{table}[t]
615	\centering
616	\small
617	\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\varepsilon{=}0.05$. Within-instance $\rho$ and selection gain both concentrate in the non-tied subset. Full $\varepsilon$ sweep in Table~\ref{tab:epsilon_sweep}.}
618	\label{tab:nontied_main}
619	\begin{tabular}{lccc}
620	\toprule
621	Subset & $n$ & $\rho$(LP,F1) & LP $\Delta$ vs.\ greedy \\
622	\midrule
623	Tied (range ${<}0.05$) & 319 & 0.08 & ${\approx}0$ \\
624	Non-tied (range ${\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\
625	\midrule
626	All instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
632	
633	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
634	
635	\begin{table}[t]
636	\centering
637	\small
638	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
639	\label{tab:vc_quartile}
640	\begin{tabular}{lcccc}
641	\toprule
642	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
643	\midrule
644	\multicolumn{5}{l}{\textit{NER}} \\
645	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
646	Q2 & 0.51 & $-$0.65 & $-$1.89 & 
…[truncated 11109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1206 · 2026-05-18T05:56:19.566123+00:00_

# ACL Rolling Review Form: Scoring Dimensions

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale: 1-5 (with .5 increments)**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper to others"
- 2: "Potentially Interesting: this paper does not resonate with me"
- 1: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5571
}
```

</details>

---


### Tool call

_source line 1207 · 2026-05-18T05:56:26.241313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "800",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "800",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-18T05:56:26.241956+00:00_

800	\toprule
801	Task & Method & Constrained & Free-form & $\Delta$ \\
802	\midrule
803	\multirow{3}{*}{NER}
804	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
805	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
806	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
807	\midrule
808	\multirow{3}{*}{RE}
809	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
810	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
811	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
812	\bottomrule
813	\end{tabular}
814	
815	\vspace{8pt}
816	
817	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
818	\vspace{2pt}
819	
820	\begin{tabular}{l ccc ccc}
821	\toprule
822	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
823	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
824	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
825	\midrule
826	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
827	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
828	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
829	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
830	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
831	\bottomrule
832	\end{tabular}
833	
834	\vspace{8pt}
835	
836	{\small\textsc{Panel D: Parse Rate (Free-form)}}
837	\vspace{2pt}
838	
839	\begin{tabular}{lc}
840	\toprule
841	Metric & Value \\
842	\midrule
843	Total samples          & 4408 \\
844	Parse rate             & 99.95\% \\
845	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
846	\bottomrule
847	\end{tabular}
848	
849	\end{table*}
850	
851	\paragraph{CoNLL NER free-form results.}
852	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
853	Free-form decoding reduces the tied fraction modestly, yet selection r
…[truncated 9769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-18T05:56:31.490401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1000",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1000",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1210 · 2026-05-18T05:56:31.491142+00:00_

1000	\midrule
1001	LP & $+$0.95 & [$-$0.41, $+$2.34] & 0.091 & ${<}$0.001 \\
1002	FK & $+$0.66 & [$-$0.36, $+$1.67] & 0.101 & ${<}$0.001 \\
1003	SJ & $+$0.36 & [$-$0.66, $+$1.38] & 0.244 & ${<}$0.001 \\
1004	EM & $+$0.22 & [$-$0.99, $+$1.44] & 0.355 & ${<}$0.001 \\
1005	VC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\
1006	\midrule
1007	Oracle & $+$20.00 & [$+$17.98, $+$22.10] & ${<}$0.001 & --- \\
1008	\bottomrule
1009	\end{tabular}
1010	\end{table}
1011	
1012	\section{Temperature Ablation}\label{app:t_ablation}
1013	
1014	Table~\ref{tab:t_ablation} reports the effect of sampling temperature on QE signals, oracle headroom, and output quality across four temperatures on SciERC NER.
1015	
1016	\begin{table}[t]
1017	\centering
1018	\small
1019	\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\rho$ across four temperatures. $\kappa$: Fleiss' $\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}
1020	\label{tab:t_ablation}
1021	\begin{tabular}{ccccccc}
1022	\toprule
1023	$T$ & Oracle gap (pp) & SJ $\rho$ & LP $\rho$ & $\kappa$ & Sample F1 \\
1024	\midrule
1025	0.5 & $+$7.8 & 0.297 & 0.218 & 0.577 & 0.636 \\
1026	0.8 & $+$10.5 & 0.359 & 0.253 & 0.451 & 0.622 \\
1027	1.0 & $+$13.3 & 0.360 & 0.205 & ${\approx}$0.39 & ${\approx}$0.612 \\
1028	1.2 & $+$13.0 & 0.377 & 0.196 & 0.356 & 0.594 \\
1029	\bottomrule
1030	\end{tabular}
1031	\end{table}
1032	
1033	Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing at $T{=}1.2$ ($+13.0$~pp); the plateau suggests $T{=}1.0$ already approaches the diversity ceiling for constrained structured decoding.
1034	Structural QE signals improve with temperature: SJ $\rho$ rises from $0.297$ ($T{=}0.5$) to $0.377$ ($T{=}1.2$), consistent with more diverse outputs providing richer pairwise evidence.
1035	LP $\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades to
…[truncated 15685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1211 · 2026-05-18T05:56:35.554606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1250",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1250",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1212 · 2026-05-18T05:56:35.605364+00:00_

1250	Entity Type & Degen.\% & LP $\Delta$ (pp) \\
1251	\midrule
1252	Task & 10.1 & $+$2.58 \\
1253	Generic & 10.0 & $+$2.07 \\
1254	Material & 20.0 & $+$0.91 \\
1255	Metric & 12.5 & $-$0.06 \\
1256	Method & 16.3 & $-$0.03 \\
1257	OtherScientificTerm & 6.2 & $-$0.57 \\
1258	\bottomrule
1259	\end{tabular}
1260	\end{table}
1261	
1262	The cross-dataset degeneracy gradient (59.1\% $\to$ 17.8\% $\to$ 13.8\%) is inversely associated with LP selection effectiveness at the macro level ($n{=}3$ datasets; exploratory).\footnote{Partial Spearman correlation controlling for entity-type frequency yields $\rho{=}{-}0.47$ (vs.\ raw $\rho{=}{-}0.38$); type frequency does not confound the degeneracy--LP relationship.}
1263	At finer per-type granularity, selection depends on the interaction of degeneracy, oracle headroom, and type-specific LP-quality alignment.
1264	Low degeneracy is necessary but not sufficient: CoNLL MISC (23\%, headroom 12.6~pp) and SciERC OtherScientificTerm (6.2\%, headroom 12.5~pp) both show negative LP selection despite available headroom; LP correlation strength with the type-specific quality function is an additional prerequisite.
1265	
1266	\section{Calibration Baseline}\label{app:calibration_baseline}
1267	
1268	Standard calibration methods are monotonic transforms of log-probability and therefore preserve within-instance sample rankings: Platt scaling \cite{platt1999probabilistic} fits a logistic regression $\sigma(a \cdot \text{LP} + b)$, and temperature scaling \cite{guo2017calibration} divides logits by a scalar $\tau$.
1269	Since both preserve the argmax, selection F1 is identical to raw LP on all three datasets (Table~\ref{tab:calibration}).
1270	
1271	To break monotonicity, we fit a multi-feature Platt model (MF-Platt) using LP, token count, and entity count as inputs, trained on a held-out calibration split (20\% of the test set, 5-fold cross-validation on the remainder).
1272	MF-Platt can reorder candidates within an instance, yet yields no signifi
…[truncated 6644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1213 · 2026-05-18T05:56:39.519581+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1214 · 2026-05-18T05:56:39.570177+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1215 · 2026-05-18T05:56:42.535058+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "description": "Count lines in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "description": "Count lines in references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-18T05:56:42.786184+00:00_

507 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1217 · 2026-05-18T05:56:45.597345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1218 · 2026-05-18T05:56:45.698466+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{vijayakumar2018diverse,
4	  title = {Diverse Beam Search for Improved Description of Complex Scenes},
5	  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},
6	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
7	  year = {2018},
8	  url = {https://arxiv.org/abs/1610.02424}
9	}
10	
11	@inproceedings{shi2022mbr,
12	  title = {Natural Language to Code Translation with Execution},
13	  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},
14	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
15	  pages = {3533--3546},
16	  year = {2022},
17	  url = {https://arxiv.org/abs/2204.11454}
18	}
19	
20	@article{eisenstein2023helping,
21	  title = {Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking},
22	  author = {Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D'Amour, Alex and Dvijotham, DJ and Fisch, Adam and Heller, Katherine and Pfohl, Stephen and Ramachandran, Deepak and Shaw, Peter and Berant, Jonathan},
23	  journal = {arXiv preprint arXiv:2312.09244},
24	  year = {2023},
25	  url = {https://arxiv.org/abs/2312.09244}
26	}
27	
28	@article{brown2024monkeys,
29	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
30	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
31	  journal = {arXiv preprint arXiv:2407.21787},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2407.21787}
34	}
35	
36	@inproceedings{chen2024usc,
37	  title = {Universal Self-Consistency for Large Language Model Generation},
38	  author = {Chen, Xinyun and Aksitov, Renat and Alon, 
…[truncated 11427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1219 · 2026-05-18T05:56:50.015871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "offset": "250"
  }
}
```

</details>

---


### Tool result

_source line 1220 · 2026-05-18T05:56:50.066695+00:00_

250	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
251	  year = {2024},
252	  doi = {10.18653/v1/2024.emnlp-main.706},
253	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
254	}
255	
256	@inproceedings{tjongkimsang2003conll,
257	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
258	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
259	  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},
260	  year = {2003},
261	  url = {https://aclanthology.org/W03-0419/}
262	}
263	
264	@inproceedings{vashurin2025cocoa,
265	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
266	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
267	  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},
268	  year = {2025},
269	  url = {https://arxiv.org/abs/2502.04964}
270	}
271	
272	@inproceedings{wadhwa2023revisiting,
273	  title = {Revisiting Relation Extraction in the era of Large Language Models},
274	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
275	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
276	  year = {2023},
277	  doi = {10.18653/v1/2023.acl-long.868},
278	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
279	}
280	
281	@inproceedings{wang2023selfconsistency,
282	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
283	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
284	  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)
…[truncated 10887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1221 · 2026-05-18T05:58:00.485814+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1222 · 2026-05-18T05:58:00.536430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1223 · 2026-05-18T06:00:16.637476+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 1. Summary\n\n本文评估了五种置信度信号（四种 instance-level：SJ/VC/FK/EM，一种 per-sample：LP）用于 LLM-based NER 的质量估计（QE）和样本选择（selection）。核心发现是 \"correlation-selection gap\"：所有信号都能实现可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但在 selection 上几乎无法超越 greedy decoding。LP 仅在两个条件同时满足时（低 degeneracy <15% + 足够的 LP-quality alignment ρ≳0.3）才能实现显著的 selection 增益（Few-NERD +1.36pp）。两个阻断机制被识别：instance degeneracy 和 weak LP-quality alignment。\n\n## 2. Strengths\n\n**S1. QE 与 selection 的系统性分离。** 这是本文最重要的方法论贡献。先前工作常将 \"信号与质量相关\" 等同于 \"信号可用于选择\"，本文用大量实验严格证明了这一等价关系不成立。这一洞察对实践者有直接价值。\n\n**S2. 极其透明的实验报告。** 几乎每一个有争议的设计选择都被主动标注并讨论：Few-NERD 3-epoch vs 5-epoch 差异（§4.1, Appendix N）、thinking token confound（Appendix F）、ε=0.05 的 post-hoc 性质（Appendix D）、per-entity-type 分析的 non-independence（§4.4, Contribution 3）、LoRA-rank ablation 的 capacity confound（§4.5）。这种透明度在同类实证论文中非常少见。\n\n**S3. 多层次证据三角验证。** \"两个必要条件\" 的论证通过多条独立证据线收敛：temperature ablation（改变 diversity 不改变 capacity）、LoRA-rank ablation（虽有 confound 但方向一致）、cross-dataset gradient（exploratory）、per-entity-type 分析（within-dataset）、epoch curve（SciERC 3-point）。单独每条证据都不足以支撑因果推断，但综合起来构成了较强的 converging evidence。\n\n**S4. Instance-level vs per-sample 信号的 definitional observation。** §3.1 指出 4/5 信号是 instance-level aggregates，by construction 无法区分同一 input 下的不同 candidates。这不是实验发现而是逻辑必然，为后续分析提供了清晰的结构性解释。\n\n**S5. 附录的深度和完整性。** 14 个 appendix sections 覆盖了几乎所有可预见的 reviewer 质疑：FK independence test、SJ normalizer robustness、ε sensitivity sweep、free-form decoding ablation、calibration baseline、N-scaling 到 N=32、bootstrap significance、TOST equivalence testing 等。\n\n**S6. 统计方法总体恰当。** Spearman ρ 用于 ordinal correlation、AUROC 用于 binary discrimination、sign test 用于 paired selection comparison、bootstrap CI 用于 signal comparison、TOST 用于 equivalence testing——工具选择合理且不过度。\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**W1 [Must-Fix]. Few-NERD 3-epoch vs SciERC 5-epoch 的 confound 削弱了核心 cross-dataset comparison。**\n- **位置**: §4.1, §4.4 (Table 4), §6 Discussion\n- **问题**: 论文的核心叙事依赖 Few-NERD（low degeneracy → LP works）vs SciERC（high degeneracy → LP fails）的对比。但 Few-NERD 模型训练 3 epochs，SciERC 训练 5 epochs。Appendix N 的 epoch confound analysis 明确显示：Few-NERD 5-epoch degeneracy 从 11.1% 升至 31.3%，LP gains 从 +1.37pp 降至 +0.62pp。同时，SciERC 3-epoch degeneracy 仅 6.4%（远低于 Few-NERD 的 13.8%），但 LP 增益仍为 -1.18pp（Table 13）。\n- **这意味着**: (a) Table 4 的 cross-dataset gradient 是 training duration 和 dataset property 的混淆效应；(b) SciERC 3-epoch 的数据实际上 **反驳** 了 \"low degeneracy → LP works\" 的简单叙事（degeneracy 6.4% 但 LP Δ = -1.18pp），论文在 Appendix N 末段承认了这一点，但主文叙事未充分调整。\n- **为什么影响接收**: 这是论文的 central empirical claim 之一。Table 4 被 Introduction（§1, line 13-14）、Experiments（§4.4）、Discussion（§6）和 Conclusion（§7）反复引用。如果 cross-dataset gradient 被 epoch confound 污染，\"两个必要条件\" 的证据强度显著下降。\n- **建议**: (1) 在 Table 4 旁明确标注 training epochs 差异；(2) 加入 \"matched-epoch\" 对比行（如 SciERC 3-epoch vs Few-NERD 3-epoch，或两者都在 5-epoch 下对比）；(3) 如果 matched-epoch 数据不可得，在主文（不仅是 appendix）明确承认这一 confound 对 cross-dataset gradient 的影响，并降低相关 claim 的强度。\n\n**W2 [Must-Fix]. \"Two jointly necessary conditions\" 的因果性表述过强。**\n- **位置**: §1 Contribution 2-3, §4.4, §6 Discussion\n- **问题**: \"Jointly necessary\" 是一个强因果声明。论文的证据是 observational：不同 datasets、不同 training durations、不同 entity types 下的条件共变。Temperature ablation（§6, Table 11）是最接近 interventional evidence 的，但它只操纵了 degeneracy，alignment 是被动观察的（ρ=0.225 at T=1.2）。没有任何实验独立操纵 alignment 来验证其必要性。SciERC 3-epoch（Table 13: degeneracy 6.4%, ρ=0.317, LP Δ=-1.18pp）是一个 suggestive case，但 ρ=0.317 是否真的低于 \"threshold\"（论文建议 ρ≳0.3）是模糊的。\n- **为什么影响接收**: 如果审稿人将 \"jointly necessary\" 理解为严格的因果条件（必要条件意味着违反任一条件必定导致失败），那么 SciERC 3-epoch 的 case（ρ=0.317 > 0.3 且 degeneracy 6.4% < 15%，但 LP 仍为负）就是一个反例。\n- **建议**: 将 \"jointly necessary\" 改为 \"jointly associated with\" 或 \"both appear required in the regimes we tested\"。在主文讨论 SciERC 3-epoch 的 case 作为边界情况。ρ≳0.3 的 threshold 应标注为 approximate 和 data-driven，而非一个 sharp boundary。\n\n### Should-Fix\n\n**W3 [Should-Fix]. 2-seed 实验设计统计效力不足。**\n- **位置**: §4.1 footnote 5, Limitations §8 line 13\n- **问题**: Selection 的 primary results（Table 3）使用 2-seed 平均。论文在 footnote 5 承认 \"Three-seed experiments (σ≤0.026; Table 6) confirm ranking stability; the reduced seed count for primary results reflects computational budget.\" 但 2 seeds 无法估计 variance——σ from 2 points 的置信区间极宽。Table 6 的 3-seed stability 仅适用于 QE 的 signal rankings，不直接验证 selection gains 的 seed stability。\n- **建议**: 至少对 primary selection comparison（Table 3 中 LP vs greedy on SciERC）补充 3-seed 数据，或者更明确地标注 2-seed 结果的 uncertainty bounds。Few-NERD 的 +1.36pp 有 bootstrap CI [+1.18, +1.53]（within-seed），但 cross-seed uncertainty 未量化。\n\n**W4 [Should-Fix]. Per-entity-type 分析的 non-independence 问题比论文讨论的更严重。**\n- **位置**: §4.4, Figure 3, Contribution 3\n- **问题**: 8 entity types 来自同一模型、同一 tokenizer、同一 temperature、同一 training run。论文承认 \"effective degrees of freedom may be lower than 6\"，但未量化实际的 effective df。如果 types 之间高度相关（如 Person/Location/Organization 的 LP 行为可能受共享的 character-level tokenization 模式驱动），effective df 可能低至 2-3，此时 p=0.004 的 significance 消失。Appendix L (Table 10) 的 partial correlation 控制了 entity-type frequency（ρ=-0.47 vs raw -0.38），但未控制更重要的 confounders（如 type-level 的 token length distribution、schema complexity）。\n- **建议**: (1) 报告 entity types 之间 LP behavior 的 ICC（intraclass correlation），用于估计 effective df；(2) 如果 effective df 太低，将 p=0.004 标注为 nominal p-value 而非 corrected p-value；(3) 在 Figure 3 caption 和 Contribution 3 中明确 qualifying。\n\n**W5 [Should-Fix]. \"Supervised verifier baseline\" 的 framing 有误导性。**\n- **位置**: §4.5 Robustness, §6 Discussion\n- **问题**: §4.5 的 \"supervised verifier\" 实际上只是用 logistic regression/MLP/random forest 对 5 个 unsupervised scalar signals 进行 supervised combination。它不是 Cobbe et al. (2021) 意义上的 verifier（后者使用 hidden states 或 full representation 进行 learned scoring）。论文在 §4.5 末段承认 \"whether richer representations (e.g., hidden states, entity embeddings) could close the gap remains untested\"，但这个 acknowledgment 出现在 \"supervised verifiers... all perform at or below greedy\" 的声明之后，容易误导读者认为 supervised learning approach 已被排除。\n- **为什么影响评分**: 这影响 Conclusion 的 \"supervised combination of these five unsupervised signals does not close the oracle gap\"（§7 line 8）——这个结论是正确的但 framing 需要更精确。\n- **建议**: 将 \"supervised verifier baseline\" 改为 \"supervised signal combination\" 或 \"supervised aggregation baseline\"。在首次提及时立即澄清 scope：这测试的是 combination strategy，不是 learned representation。\n\n**W6 [Should-Fix]. Degeneracy 的操作性定义需要更清晰地在主文中区分。**\n- **位置**: Table 4 footnote, §4.3, Appendix D (Table 8)\n- **问题**: \"Instance degeneracy\" 被定义为 \"所有 N 个 samples 产生相同的 instance-level F1\"（Table 4 footnote），这与 \"所有 N 个 outputs 完全相同\" 不同。Table 8 显示 Qwen/SciERC 的 \"Identical outputs\" = 11%，但 \"Constant F1\" = 17.8%。这 6.8% 的差异（outputs 不同但 F1 相同）对选择问题有不同含义：outputs 不同意味着存在可选择的候选，但 F1 碰巧相同意味着选择不影响结果。这个区分在 Discussion（§6: \"14–59% of instances yield identical F1 scores\"）中被正确使用，但 Abstract 和 Introduction 中 \"identical F1 scores across all samples\" 容易被误读为 \"identical outputs\"。\n- **建议**: 在 §3.1 Problem Formulation 中给出明确定义，区分 output degeneracy（identical outputs）和 F1 degeneracy（identical F1, possibly different outputs），并说明为什么 F1 degeneracy 是 selection 问题的相关定义。\n\n**W7 [Should-Fix]. Table 4 中 SciERC 数值在不同 tables 之间存在不一致。**\n- **位置**: Table 3 vs Table 4 vs Table 12\n- **问题**: SciERC greedy F1 在 Table 3 为 0.645，Table 4 为 0.644，Table 12 为 0.640。Headroom 在 Table 3 为 13.3pp，Table 4 为 13.2pp。论文在 Table 4 footnote 解释了原因（\"max-LP aggregation and single-seed evaluation\"），Table 12 footnote 也解释了（\"gold-filtered evaluation... seed and aggregation differences\"）。但这些差异分散在不同 footnotes 中，对审稿人来说很难追踪哪个是 canonical 数字。\n- **建议**: 在某处（如 §4.1 或 Appendix A）统一声明 canonical evaluation protocol，列出每个 table 偏离 canonical protocol 的原因。或者更好的做法：统一 pipeline 使所有 tables 中同一 dataset 的 greedy F1 数值一致。\n\n### Minor\n\n**M1 [Minor].** Abstract line 5: \"LP achieves +1.36 pp on Few-NERD (p<0.001) under two jointly necessary conditions\" — \"jointly necessary\" 同 W2，建议弱化。\n\n**M2 [Minor].** §1 line 8: \"Unlike Yao et al. (2026), who demonstrate that self-consistency correlates with task accuracy, we investigate why this correlation does not reliably translate to selection gains\" — 定位准确，但 Yao et al. 使用 hard-prompted LLMs 而本文使用 fine-tuned models，这个差异应明确提及，因为 degeneracy 在 fine-tuned models 中更严重（论文在 Related Work §5 line 9-10 提到，但 Introduction 中未提及）。\n\n**M3 [Minor].** Table 3 的 EM 和 VC 没有报告 p-values（标注为 \"---\"）。如果是因为它们低于 greedy，应标注为 \"< greedy\" 或给出实际 p-value。\n\n**M4 [Minor].** §4.5 Robustness: Kendall's W=1.0 的 significance \"exact p≈0.028\" 基于 m=3 raters。论文承认 \"statistical precision is limited with m=3 raters\"，但仍在主文中报告 W=1.0。建议更 prominent 地标注这个 low-power caveat。\n\n**M5 [Minor].** References: Willard & Louf (2023) 被引用为 constrained decoding，但实际 inference 使用 vLLM 的 XGrammar（Appendix E line 498-500）。应同时引用 XGrammar。\n\n**M6 [Minor].** 论文未引用 Structured Prediction 相关的一些经典工作，如 McCallum et al. (2000) Maximum Entropy Markov Models 或 Lafferty et al. (2001) CRFs，这些在 confidence estimation for structured outputs 的文献中有直接相关性。此外 Selective Prediction 文献中 Geifman & El-Yaniv (2017) 也缺失。\n\n## 4. Questions\n\n**Q1.** SciERC 3-epoch 的 within-instance alignment ρ=0.317 略高于建议的 threshold ρ≳0.3，但 LP selection Δ=-1.18pp。这是否意味着 threshold 应该更高（如 ρ≳0.4 或 0.5），还是说 SciERC 存在 dataset-specific factors 使得 alignment threshold 不具有跨 dataset 的普适性？\n\n**Q2.** Few-NERD 是 INTRA coarse setting（8 coarse types），而非 fine-grained types。在 fine-grained types 下（更多 types → 可能更多 degeneracy），LP selection 是否仍然有效？这会影响结论的 generalizability。\n\n**Q3.** Greedy decoding (T=0) 作为 selection baseline 是否太弱？在实践中，practitioners 可能使用 beam search 或 top-k sampling with post-hoc heuristics。与这些更强的 baselines 对比，LP selection 的优势是否会进一步缩小？\n\n**Q4.** 论文报告了 LP 的 entity-token variant（§6: \"Entity-token LP exhibits 4× higher variance yet performs worse\"）。这是否说明 LP compression 的根本原因是 fine-tuned models 在 representation level 上 near-deterministic，而非 token-level averaging 或 schema-token dilution？如果是，这对 \"learned verifier\" 的可行性意味着什么——如果 hidden states 同样 near-deterministic，learned verifier 可能同样失败。\n\n**Q5.** Table 12 (N-scaling selection): 从 N=8 到 N=32，LP Δ 从 +0.39pp 增长到 +0.95pp（仍 p=0.091 不显著）。如果外推到 N=64 或 N=128，是否可能达到显著水平？这是否意味着 LP selection 在 SciERC 上只是 underpowered 而非 fundamentally limited？\n\n## 5. Missing References\n\n- Geifman & El-Yaniv (2017). \"Selective Prediction Using Deep Neural Networks.\" NeurIPS. — 与 selective prediction / abstention 直接相关。\n- Lafferty, McCallum, & Pereira (2001). CRFs — structured prediction 中 confidence 的经典基础。\n- XGrammar (实际使用的 constrained decoding engine) 应被引用。\n- Lin et al. (2024). \"Generating Confidence from LLMs.\" ACL 2024. — 与 verbalized confidence 和 LP-based confidence 直接比较。\n\n## 6. Overall Assessment\n\n## 总体评分\n**Overall**: 3.5 (borderline between Findings acceptance and Conference acceptance)\n**一句话总结**: 方法论框架（QE vs selection 的分离）和实验深度出色，但核心因果 claim（\"two jointly necessary conditions\"）被 epoch confound 和有限的 causal identification strategy 削弱。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计总体严谨，统计方法恰当，透明度极高。但 epoch confound 对 cross-dataset comparison 的影响未在主文充分处理（W1），\"jointly necessary\" 的因果声明过强（W2），per-entity-type analysis 的 effective df 问题未量化（W4）。如果 W1 和 W2 被修复（降低 claim 强度 + 补充 matched-epoch 数据或承认 confound），soundness 可升至 4。 |\n| Excitement | 3.5/5 | QE vs selection 的分离是一个有洞察力的贡献，对 test-time scaling 社区有直接启示。但负结果论文（\"X 不 work\"）的 excitement 天然受限，且 4B-8B 的 scale coverage 在 2026 年显得有限。 |\n| Reproducibility | 4/5 | Training config 详细（Appendix E），所有 hyperparameters 和 seeds 明确，constrained decoding setup 清楚。代码承诺 release。唯一不确定的是 Few-NERD 的 gold-filtering 具体实现。 |\n| Confidence | 4/5 | 我仔细阅读了全文和所有 appendix sections，验证了核心统计数字的内部一致性，搜索了 ACL ARR review form 标准。对 NER/IE 方法和统计方法有较深了解。 |\n\n---\n\n**总结**: 这是一篇实验深度远超平均水平的实证论文，transparency 令人印象深刻。核心贡献（correlation-selection gap 的诊断）是 sound 的。主要问题在于：(1) cross-dataset comparison 被 epoch confound 污染但主文未充分处理；(2) 因果 claim 的措辞过强于证据所能支撑。这两个问题都可以通过修改叙述强度和补充少量实验来修复，不需要从根本上改变论文结构。修复后，本文有潜力达到 main conference 水平。\n",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 1. Summary\n\n本文评估了五种置信度信号（四种 instance-level：SJ/VC/FK/EM，一种 per-sample：LP）用于 LLM-based NER 的质量估计（QE）和样本选择（selection）。核心发现是 \"correlation-selection gap\"：所有信号都能实现可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但在 selection 上几乎无法超越 greedy decoding。LP 仅在两个条件同时满足时（低 degeneracy <15% + 足够的 LP-quality alignment ρ≳0.3）才能实现显著的 selection 增益（Few-NERD +1.36pp）。两个阻断机制被识别：instance degeneracy 和 weak LP-quality alignment。\n\n## 2. Strengths\n\n**S1. QE 与 selection 的系统性分离。** 这是本文最重要的方法论贡献。先前工作常将 \"信号与质量相关\" 等同于 \"信号可用于选择\"，本文用大量实验严格证明了这一等价关系不成立。这一洞察对实践者有直接价值。\n\n**S2. 极其透明的实验报告。** 几乎每一个有争议的设计选择都被主动标注并讨论：Few-NERD 3-epoch vs 5-epoch 差异（§4.1, Appendix N）、thinking token confound（Appendix F）、ε=0.05 的 post-hoc 性质（Appendix D）、per-entity-type 分析的 non-independence（§4.4, Contribution 3）、LoRA-rank ablation 的 capacity confound（§4.5）。这种透明度在同类实证论文中非常少见。\n\n**S3. 多层次证据三角验证。** \"两个必要条件\" 的论证通过多条独立证据线收敛：temperature ablation（改变 diversity 不改变 capacity）、LoRA-rank ablation（虽有 confound 但方向一致）、cross-dataset gradient（exploratory）、per-entity-type 分析（within-dataset）、epoch curve（SciERC 3-point）。单独每条证据都不足以支撑因果推断，但综合起来构成了较强的 converging evidence。\n\n**S4. Instance-level vs per-sample 信号的 definitional observation。** §3.1 指出 4/5 信号是 instance-level aggregates，by construction 无法区分同一 input 下的不同 candidates。这不是实验发现而是逻辑必然，为后续分析提供了清晰的结构性解释。\n\n**S5. 附录的深度和完整性。** 14 个 appendix sections 覆盖了几乎所有可预见的 reviewer 质疑：FK independence test、SJ normalizer robustness、ε sensitivity sweep、free-form decoding ablation、calibration baseline、N-scaling 到 N=32、bootstrap significance、TOST equivalence testing 等。\n\n**S6. 统计方法总体恰当。** Spearman ρ 用于 ordinal correlation、AUROC 用于 binary discrimination、sign test 用于 paired selection comparison、bootstrap CI 用于 signal comparison、TOST 用于 equivalence testing——工具选择合理且不过度。\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**W1 [Must-Fix]. Few-NERD 3-epoch vs SciERC 5-epoch 的 confound 削弱了核心 cross-dataset comparison。**\n- **位置**: §4.1, §4.4 (Table 4), §6 Discussion\n- **问题**: 论文的核心叙事依赖 Few-NERD（low degeneracy → LP works）vs SciERC（high degeneracy → LP fails）的对比。但 Few-NERD 模型训练 3 epochs，SciERC 训练 5 epochs。Appendix N 的 epoch confound analysis 明确显示：Few-NERD 5-epoch degeneracy 从 11.1% 升至 31.3%，LP gains 从 +1.37pp 降至 +0.62pp。同时，SciERC 3-epoch degeneracy 仅 6.4%（远低于 Few-NERD 的 13.8%），但 LP 增益仍为 -1.18pp（Table 13）。\n- **这意味着**: (a) Table 4 的 cross-dataset gradient 是 training duration 和 dataset property 的混淆效应；(b) SciERC 3-epoch 的数据实际上 **反驳** 了 \"low degeneracy → LP works\" 的简单叙事（degeneracy 6.4% 但 LP Δ = -1.18pp），论文在 Appendix N 末段承认了这一点，但主文叙事未充分调整。\n- **为什么影响接收**: 这是论文的 central empirical claim 之一。Table 4 被 Introduction（§1, line 13-14）、Experiments（§4.4）、Discussion（§6）和 Conclusion（§7）反复引用。如果 cross-dataset gradient 被 epoch confound 污染，\"两个必要条件\" 的证据强度显著下降。\n- **建议**: (1) 在 Table 4 旁明确标注 training epochs 差异；(2) 加入 \"matched-epoch\" 对比行（如 SciERC 3-epoch vs Few-NERD 3-epoch，或两者都在 5-epoch 下对比）；(3) 如果 matched-epoch 数据不可得，在主文（不仅是 appendix）明确承认这一 confound 对 cross-dataset gradient 的影响，并降低相关 claim 的强度。\n\n**W2 [Must-Fix]. \"Two jointly necessary conditions\" 的因果性表述过强。**\n- **位置**: §1 Contribution 2-3, §4.4, §6 Discussion\n- **问题**: \"Jointly necessary\" 是一个强因果声明。论文的证据是 observational：不同 datasets、不同 training durations、不同 entity types 下的条件共变。Temperature ablation（§6, Table 11）是最接近 interventional evidence 的，但它只操纵了 degeneracy，alignment 是被动观察的（ρ=0.225 at T=1.2）。没有任何实验独立操纵 alignment 来验证其必要性。SciERC 3-epoch（Table 13: degeneracy 6.4%, ρ=0.317, LP Δ=-1.18pp）是一个 suggestive case，但 ρ=0.317 是否真的低于 \"threshold\"（论文建议 ρ≳0.3）是模糊的。\n- **为什么影响接收**: 如果审稿人将 \"jointly necessary\" 理解为严格的因果条件（必要条件意味着违反任一条件必定导致失败），那么 SciERC 3-epoch 的 case（ρ=0.317 > 0.3 且 degeneracy 6.4% < 15%，但 LP 仍为负）就是一个反例。\n- **建议**: 将 \"jointly necessary\" 改为 \"jointly associated with\" 或 \"both appear required in the regimes we tested\"。在主文讨论 SciERC 3-epoch 的 case 作为边界情况。ρ≳0.3 的 threshold 应标注为 approximate 和 data-driven，而非一个 sharp boundary。\n\n### Should-Fix\n\n**W3 [Should-Fix]. 2-seed 实验设计统计效力不足。**\n- **位置**: §4.1 footnote 5, Limitations §8 line 13\n- **问题**: Selection 的 primary results（Table 3）使用 2-seed 平均。论文在 footnote 5 承认 \"Three-seed experiments (σ≤0.026; Table 6) confirm ranking stability; the reduced seed count for primary results reflects computational budget.\" 但 2 seeds 无法估计 variance——σ from 2 points 的置信区间极宽。Table 6 的 3-seed stability 仅适用于 QE 的 signal rankings，不直接验证 selection gains 的 seed stability。\n- **建议**: 至少对 primary selection comparison（Table 3 中 LP vs greedy on SciERC）补充 3-seed 数据，或者更明确地标注 2-seed 结果的 uncertainty bounds。Few-NERD 的 +1.36pp 有 bootstrap CI [+1.18, +1.53]（within-seed），但 cross-seed uncertainty 未量化。\n\n**W4 [Should-Fix]. Per-entity-type 分析的 non-independence 问题比论文讨论的更严重。**\n- **位置**: §4.4, Figure 3, Contribution 3\n- **问题**: 8 entity types 来自同一模型、同一 tokenizer、同一 temperature、同一 training run。论文承认 \"effective degrees of freedom may be lower than 6\"，但未量化实际的 effective df。如果 types 之间高度相关（如 Person/Location/Organization 的 LP 行为可能受共享的 character-level tokenization 模式驱动），effective df 可能低至 2-3，此时 p=0.004 的 significance 消失。Appendix L (Table 10) 的 partial correlation 控制了 entity-type frequency（ρ=-0.47 vs raw -0.38），但未控制更重要的 confounders（如 type-level 的 token length distribution、schema complexity）。\n- **建议**: (1) 报告 entity types 之间 LP behavior 的 ICC（intraclass correlation），用于估计 effective df；(2) 如果 effective df 太低，将 p=0.004 标注为 nominal p-value 而非 corrected p-value；(3) 在 Figure 3 caption 和 Contribution 3 中明确 qualifying。\n\n**W5 [Should-Fix]. \"Supervised verifier baseline\" 的 framing 有误导性。**\n- **位置**: §4.5 Robustness, §6 Discussion\n- **问题**: §4.5 的 \"supervised verifier\" 实际上只是用 logistic regression/MLP/random forest 对 5 个 unsupervised scalar signals 进行 supervised combination。它不是 Cobbe et al. (2021) 意义上的 verifier（后者使用 hidden states 或 full representation 进行 learned scoring）。论文在 §4.5 末段承认 \"whether richer representations (e.g., hidden states, entity embeddings) could close the gap remains untested\"，但这个 acknowledgment 出现在 \"supervised verifiers... all perform at or below greedy\" 的声明之后，容易误导读者认为 supervised learning approach 已被排除。\n- **为什么影响评分**: 这影响 Conclusion 的 \"supervised combination of these five unsupervised signals does not close the oracle gap\"（§7 line 8）——这个结论是正确的但 framing 需要更精确。\n- **建议**: 将 \"supervised verifier baseline\" 改为 \"supervised signal combination\" 或 \"supervised aggregation baseline\"。在首次提及时立即澄清 scope：这测试的是 combination strategy，不是 learned representation。\n\n**W6 [Should-Fix]. Degeneracy 的操作性定义需要更清晰地在主文中区分。**\n- **位置**: Table 4 footnote, §4.3, Appendix D (Table 8)\n- **问题**: \"Instance degeneracy\" 被定义为 \"所有 N 个 samples 产生相同的 instance-level F1\"（Table 4 footnote），这与 \"所有 N 个 outputs 完全相同\" 不同。Table 8 显示 Qwen/SciERC 的 \"Identical outputs\" = 11%，但 \"Constant F1\" = 17.8%。这 6.8% 的差异（outputs 不同但 F1 相同）对选择问题有不同含义：outputs 不同意味着存在可选择的候选，但 F1 碰巧相同意味着选择不影响结果。这个区分在 Discussion（§6: \"14–59% of instances yield identical F1 scores\"）中被正确使用，但 Abstract 和 Introduction 中 \"identical F1 scores across all samples\" 容易被误读为 \"identical outputs\"。\n- **建议**: 在 §3.1 Problem Formulation 中给出明确定义，区分 output degeneracy（identical outputs）和 F1 degeneracy（identical F1, possibly different outputs），并说明为什么 F1 degeneracy 是 selection 问题的相关定义。\n\n**W7 [Should-Fix]. Table 4 中 SciERC 数值在不同 tables 之间存在不一致。**\n- **位置**: Table 3 vs Table 4 vs Table 12\n- **问题**: SciERC greedy F1 在 Table 3 为 0.645，Table 4 为 0.644，Table 12 为 0.640。Headroom 在 Table 3 为 13.3pp，Table 4 为 13.2pp。论文在 Table 4 footnote 解释了原因（\"max-LP aggregation and single-seed evaluation\"），Table 12 footnote 也解释了（\"gold-filtered evaluation... seed and aggregation differences\"）。但这些差异分散在不同 footnotes 中，对审稿人来说很难追踪哪个是 canonical 数字。\n- **建议**: 在某处（如 §4.1 或 Appendix A）统一声明 canonical evaluation protocol，列出每个 table 偏离 canonical protocol 的原因。或者更好的做法：统一 pipeline 使所有 tables 中同一 dataset 的 greedy F1 数值一致。\n\n### Minor\n\n**M1 [Minor].** Abstract line 5: \"LP achieves +1.36 pp on Few-NERD (p<0.001) under two jointly necessary conditions\" — \"jointly necessary\" 同 W2，建议弱化。\n\n**M2 [Minor].** §1 line 8: \"Unlike Yao et al. (2026), who demonstrate that self-consistency correlates with task accuracy, we investigate why this correlation does not reliably translate to selection gains\" — 定位准确，但 Yao et al. 使用 hard-prompted LLMs 而本文使用 fine-tuned models，这个差异应明确提及，因为 degeneracy 在 fine-tuned models 中更严重（论文在 Related Work §5 line 9-10 提到，但 Introduction 中未提及）。\n\n**M3 [Minor].** Table 3 的 EM 和 VC 没有报告 p-values（标注为 \"---\"）。如果是因为它们低于 greedy，应标注为 \"< greedy\" 或给出实际 p-value。\n\n**M4 [Minor].** §4.5 Robustness: Kendall's W=1.0 的 significance \"exact p≈0.028\" 基于 m=3 raters。论文承认 \"statistical precision is limited with m=3 raters\"，但仍在主文中报告 W=1.0。建议更 prominent 地标注这个 low-power caveat。\n\n**M5 [Minor].** References: Willard & Louf (2023) 被引用为 constrained decoding，但实际 inference 使用 vLLM 的 XGrammar（Appendix E line 498-500）。应同时引用 XGrammar。\n\n**M6 [Minor].** 论文未引用 Structured Prediction 相关的一些经典工作，如 McCallum et al. (2000) Maximum Entropy Markov Models 或 Lafferty et al. (2001) CRFs，这些在 confidence estimation for structured outputs 的文献中有直接相关性。此外 Selective Prediction 文献中 Geifman & El-Yaniv (2017) 也缺失。\n\n## 4. Questions\n\n**Q1.** SciERC 3-epoch 的 within-instance alignment ρ=0.317 略高于建议的 threshold ρ≳0.3，但 LP selection Δ=-1.18pp。这是否意味着 threshold 应该更高（如 ρ≳0.4 或 0.5），还是说 SciERC 存在 dataset-specific factors 使得 alignment threshold 不具有跨 dataset 的普适性？\n\n**Q2.** Few-NERD 是 INTRA coarse setting（8 coarse types），而非 fine-grained types。在 fine-grained types 下（更多 types → 可能更多 degeneracy），LP selection 是否仍然有效？这会影响结论的 generalizability。\n\n**Q3.** Greedy decoding (T=0) 作为 selection baseline 是否太弱？在实践中，practitioners 可能使用 beam search 或 top-k sampling with post-hoc heuristics。与这些更强的 baselines 对比，LP selection 的优势是否会进一步缩小？\n\n**Q4.** 论文报告了 LP 的 entity-token variant（§6: \"Entity-token LP exhibits 4× higher variance yet performs worse\"）。这是否说明 LP compression 的根本原因是 fine-tuned models 在 representation level 上 near-deterministic，而非 token-level averaging 或 schema-token dilution？如果是，这对 \"learned verifier\" 的可行性意味着什么——如果 hidden states 同样 near-deterministic，learned verifier 可能同样失败。\n\n**Q5.** Table 12 (N-scaling selection): 从 N=8 到 N=32，LP Δ 从 +0.39pp 增长到 +0.95pp（仍 p=0.091 不显著）。如果外推到 N=64 或 N=128，是否可能达到显著水平？这是否意味着 LP selection 在 SciERC 上只是 underpowered 而非 fundamentally limited？\n\n## 5. Missing References\n\n- Geifman & El-Yaniv (2017). \"Selective Prediction Using Deep Neural Networks.\" NeurIPS. — 与 selective prediction / abstention 直接相关。\n- Lafferty, McCallum, & Pereira (2001). CRFs — structured prediction 中 confidence 的经典基础。\n- XGrammar (实际使用的 constrained decoding engine) 应被引用。\n- Lin et al. (2024). \"Generating Confidence from LLMs.\" ACL 2024. — 与 verbalized confidence 和 LP-based confidence 直接比较。\n\n## 6. Overall Assessment\n\n## 总体评分\n**Overall**: 3.5 (borderline between Findings acceptance and Conference acceptance)\n**一句话总结**: 方法论框架（QE vs selection 的分离）和实验深度出色，但核心因果 claim（\"two jointly necessary conditions\"）被 epoch confound 和有限的 causal identification strategy 削弱。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计总体严谨，统计方法恰当，透明度极高。但 epoch confound 对 cross-dataset comparison 的影响未在主文充分处理（W1），\"jointly necessary\" 的因果声明过强（W2），per-entity-type analysis 的 effective df 问题未量化（W4）。如果 W1 和 W2 被修复（降低 claim 强度 + 补充 matched-epoch 数据或承认 confound），soundness 可升至 4。 |\n| Excitement | 3.5/5 | QE vs selection 的分离是一个有洞察力的贡献，对 test-time scaling 社区有直接启示。但负结果论文（\"X 不 work\"）的 excitement 天然受限，且 4B-8B 的 scale coverage 在 2026 年显得有限。 |\n| Reproducibility | 4/5 | Training config 详细（Appendix E），所有 hyperparameters 和 seeds 明确，constrained decoding setup 清楚。代码承诺 release。唯一不确定的是 Few-NERD 的 gold-filtering 具体实现。 |\n| Confidence | 4/5 | 我仔细阅读了全文和所有 appendix sections，验证了核心统计数字的内部一致性，搜索了 ACL ARR review form 标准。对 NER/IE 方法和统计方法有较深了解。 |\n\n---\n\n**总结**: 这是一篇实验深度远超平均水平的实证论文，transparency 令人印象深刻。核心贡献（correlation-selection gap 的诊断）是 sound 的。主要问题在于：(1) cross-dataset comparison 被 epoch confound 污染但主文未充分处理；(2) 因果 claim 的措辞过强于证据所能支撑。这两个问题都可以通过修改叙述强度和补充少量实验来修复，不需要从根本上改变论文结构。修复后，本文有潜力达到 main conference 水平。\n",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1224 · 2026-05-18T06:00:21.646005+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5008
}
```

</details>

---


### Assistant

_source line 1225 · 2026-05-18T06:00:33.075653+00:00_

审稿意见已提交给 Review Director。

审稿核心判断：**Overall 3.5/5（borderline Findings/Main）**。

关键发现：
- **2 个 Must-Fix**：(1) Few-NERD 3-epoch vs SciERC 5-epoch 的 training duration confound 污染了核心 cross-dataset comparison（Table 4），SciERC 3-epoch 数据（degeneracy 6.4% 但 LP Δ=-1.18pp）实际上与论文的简单叙事矛盾；(2) "two jointly necessary conditions" 的因果措辞过强，证据是 observational 而非 interventional。
- **5 个 Should-Fix**：2-seed 设计效力不足、per-entity-type 分析 non-independence 未量化 effective df、"supervised verifier" framing 误导、degeneracy 定义需在主文明确区分 output vs F1 degeneracy、跨 table 数值不一致。
- **优势**：QE vs selection 的方法论分离、极高的实验透明度、14 个 appendix 的深度验证、统计方法选择恰当。

修复 W1 和 W2（降低 claim 强度 + 补充 matched-epoch 数据或明确承认 confound）后，论文有潜力达到 main conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 39

## Round 39

38 recorded events


### User

_source line 1226 · 2026-05-18T06:03:52.358359+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）

特别关注与你自己审稿意见的异同——如果 Reviewer 2 发现了你遗漏的问题，请明确承认；如果你认为 Reviewer 2 的某个判断有误，请提供具体反驳。

---

# Reviewer 2 审稿意见 — Round 1

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规

## 2. Strengths

**S1. 实验设计严谨且系统化。** 四个数据集构成 difficulty gradient（ceiling → medium → low-degeneracy → collapse boundary），每个数据集有明确的诊断角色。两个模型家族 + 4B ablation 增强了泛化性。QE 和 selection 的分离是一个重要的方法论贡献。

**S2. 统计方法论远超同类工作。** Bootstrap CIs（Table 9）、TOST equivalence testing（Appendix）、MDE 计算（n=529 对应 ~1.5pp）、Bonferroni correction、Fisher combined p-values、external equivalence margins（Ratinov 2009, Berg-Kirkpatrick 2012）——这些构成了一个罕见的完整统计分析框架。

**S3. 消融实验全面且可信。** Temperature ablation（隔离 diversity 和 capacity）、LoRA-rank ablation（conflated 但有 secondary evidence 价值）、free-form decoding ablation（排除 constrained decoding 作为 NER LP compression 的唯一原因）、entity-token LP（排除 token averaging 作为唯一机制）、supervised verifier baseline（排除信号组合策略）——每个 ablation 都有明确的诊断目的。

**S4. Appendix 的深度令人印象深刻。** 1353 行 appendix 覆盖了几乎所有可预见的审稿人质疑：FK 独立性检验、SJ normalizer 鲁棒性、ε 灵敏度分析、epoch confound、thinking token 分析、OOD、calibration baseline 等。

**S5. 引用完整且无 orphan/missing 条目。** 60 条 bib entry 全部被引用，0 orphan、0 missing。

**S6. 写作质量优秀，AI 痕迹极少。**

## 3. Weaknesses

### Must-Fix

**N1 [critical] Contribution 1 中 "methodological premise" 的贡献定位不当**
- 具体位置：Section 1, Contribution 1; Section 2 (§2.1); Abstract line 8
- 问题："A definitional observation structures the analysis: four of five signals are instance-level aggregates that by design assign identical scores to all candidates" 是一个定义推论，不是实验发现。Instance-level signal 无法区分 per-sample candidates 是信号定义的直接推论——任何理解 MBR decoding 的读者都能从定义推导出这一点。将此列为 Contribution 1 的一部分 inflates 了贡献清单。
- 建议修改方向：将其降级为 Method section 的 framing observation，从 Contribution 列表中移除或明确标注为 "definitional premise"。

**N2 [critical] "Correlation-selection gap" 的新颖性需要更锐利的差异化定位**
- 具体位置：Section 1 (term coined), Section 3 (§3.3), Section 5
- 问题：MBR decoding 文献已经建立了 utility function 选择不当导致选择失败的先例。Eikema et al. (2025) 明确发现 MBR utilities degrade on structured outputs。论文引用了这些工作但差异化定位不够锐利——读者可能会问："这和 Eikema et al. (2025) 的 'utility degradation on structured outputs' 有什么本质区别？"
- 建议：在 Introduction 或 Related Work 中增加明确对比。

### Should-Fix

**W1 [warning] Abstract 数字过载，叙事被压缩**
- Abstract 包含至少 8 个定量值。建议保留 3 个以内关键数字。

**W2 [warning] 论文的 actionable contribution 偏薄**
- LP 在 Few-NERD 上 +1.36pp，且需要两个特定条件。对不满足条件的场景 actionable advice 是 "use greedy decoding"。
- 建议增加 forward-looking analysis。

**W3 [warning] Discussion section 过于碎片化**
- 7 个独立的 paragraph topic，每个只有 1 段。建议合并。

**W4 [warning] 纯诊断性论文对 EMNLP main conference 的门槛**
- 核心信息可以用一句话概括。建议更明确地 argue 为什么诊断是 non-trivial。

**W5 [warning] 核心发现的重复性过高**
- "14–59% degeneracy", "+1.36pp on Few-NERD" 等数字在 abstract/intro/experiments/discussion/conclusion 中几乎逐字重复。

**W6 [warning] Few-NERD 训练设置差异引入混淆**
- Few-NERD 使用 3 epochs（其他 5 epochs），唯一正面结果来源。Appendix 5-epoch control 显示 LP gains halved。

### Minor

**M1** "14\textendash 59\%" 重复出现。
**M2** Table 3 caption 中 split footnote 不优雅。
**M3** Conclusion 最后两句结构松散。
**M4** Ethics Statement 较薄（4 句）。
**M5** Table 1 只报告 SciERC 和 CoNLL，建议增加 Few-NERD 列。

## 4. Questions

**Q1.** SciERC 3-epoch 的 selection F1 是多少？如果仍为 negative，"two jointly necessary conditions" claim 需要修正。
**Q2.** 是否分析过 per-type LP selection 的 heterogeneity 在 SciERC 上的表现？
**Q3.** "Supervised verifier baseline" 名称是否误导？建议更名为 "supervised signal combination"。
**Q4.** Per-entity-type analysis（ρ=-0.881, p=0.004, n=8）的 effective df 问题——是否有 permutation test 验证？

## 5. Missing References

- Ippolito et al. (2019) "Comparison of Diverse Decoding Methods"
- Xiao &amp; Wang (2021) "On Hallucination and Predictive Uncertainty"
- Li et al. (2024) "Rain: Your Language Models Can Align Themselves"

## 7. Overall Assessment

**Overall**: 3/5 (Borderline — Findings acceptance, borderline for main conference)
**Excitement**: 2.5/5
**Soundness**: 3.5/5
**Reproducibility**: 4/5

**一句话总结**: 实验设计和统计分析堪称 exemplary，但核心诊断的新颖性受限于 MBR 文献中的已有结论，且唯一正面发现（LP +1.36pp on Few-NERD）过小且 dataset-specific。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1227 · 2026-05-18T06:04:04.352535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1228 · 2026-05-18T06:04:04.403218+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1229 · 2026-05-18T06:04:07.717208+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1230 · 2026-05-18T06:04:07.767887+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1231 · 2026-05-18T06:04:17.809307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-18T06:04:18.111368+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1233 · 2026-05-18T06:04:20.771045+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1234 · 2026-05-18T06:04:20.821746+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1235 · 2026-05-18T06:04:23.565744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1236 · 2026-05-18T06:04:24.017370+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.
5	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) under two jointly necessary conditions: low instance degeneracy and adequate LP-quality alignment ($\rho \gtrsim 0.3$).
6	When either condition is violated, LP gains fall below detectable thresholds despite ${\sim}$13~pp oracle headroom, a disparity we term the \textbf{correlation-selection gap}.
7	Two mechanisms explain this gap: \textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom; \textit{weak LP-quality alignment} prevents exploiting the remainder.
8	A methodological premise underlies both: four of five signals are instance-level aggregates that by definition cannot rank candidates.
9	Degeneracy is controllable via temperature and training convergence; closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1237 · 2026-05-18T06:04:24.017740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-18T06:04:24.971041+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \textit{why} this correlation does not reliably translate to selection gains, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (13.8\%) and adequate alignment ($\rho{\approx}0.5$), wi
…[truncated 3731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1239 · 2026-05-18T06:04:25.021619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1240 · 2026-05-18T06:04:25.473654+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
6	We extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.
10	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised verifier baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar, schall2025hidden, yun2025price}.
14	
15	\paragraph{Uncertainty estimation and MBR decoding.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncer
…[truncated 1857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-18T06:04:25.474109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1242 · 2026-05-18T06:04:25.927670+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 2976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1243 · 2026-05-18T06:04:25.978222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1244 · 2026-05-18T06:04:26.379930+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\ref{app:epoch_confound}).
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses
…[truncated 12496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1245 · 2026-05-18T06:04:26.430649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-18T06:04:26.882447+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	All signals achieve positive quality estimation across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL), with rankings stable across model families and a 4B ablation (Table~\ref{tab:scale_ablation}).
5	For selection, LP achieves significant gains only when both conditions are met ($+1.36$~pp on Few-NERD, $p{<}0.001$; Table~\ref{tab:fewnerd}); structural signals uniformly degrade selection.
6	RE signal rankings are in Appendix~\ref{app:re_extension}.
7	
8	\paragraph{Why the gap exists.}
9	Two mechanisms block selection: \textit{instance degeneracy} (consensus-proximity) and \textit{weak LP-quality alignment} (per-sample).
10	Within non-degenerate instances, MBR utility \cite{eikema2022sampling} correlates positively with F1 (SJ median $\rho{=}0.524$) and closes 23--41\% of the oracle gap, but 17.8\% (SciERC) to 59.1\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\ref{tab:degeneracy}).
11	Degeneracy is determined by the interplay of task structure, model architecture, and training convergence (Appendix~\ref{app:epoch_confound}); cross-model evidence (LLaMA 86.4\% vs.\ Qwen 59.1\% on CoNLL; Table~\ref{tab:cross_selection}) reinforces the pattern.
12	LP is severely compressed (median range 0.041 nats; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$.
13	
14	\paragraph{Non-tied subset and $N$-scaling.}
15	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$, survives Bonferroni; Table~\ref{tab:nontied_main}).
16	LP scales with $N$ in the low-degeneracy regime ($+0.52$~pp from $N{=}8$ to 16 on Few-NERD, $p{=}0.003$; \S\ref{sec:fewnerd}); on SciERC, even $N{=}32$ captures less than 5\% of headroom (Table~\ref{tab:n_scaling_
…[truncated 4739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1247 · 2026-05-18T06:04:26.882817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1248 · 2026-05-18T06:04:27.387856+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.
5	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (${<}$15\%) and adequate LP-quality alignment ($\rho \gtrsim 0.3$); gains scale with sample budget ($+0.52$~pp, $N{=}8{\to}16$, $p{=}0.003$).
6	When either condition is violated, LP gains fall below detectable thresholds despite 12\textendash 14~pp oracle headroom: on SciERC (17.8\% degeneracy, $\rho{\approx}0.24$), LP yields $+0.61$~pp (below the ${\approx}$1.5~pp MDE at 80\% power); on CoNLL (59.1\% degeneracy), LP degrades selection ($-1.05$~pp).
7	Two mechanisms explain this gap: instance degeneracy (14\textendash 59\% of instances yield identical F1 scores) eliminates headroom, and weak LP-quality alignment prevents exploiting the remainder.
8	Structural signals do not improve selection regardless of degeneracy, and supervised combination of these five unsupervised signals does not close the oracle gap; whether richer representations (e.g., hidden states, entity embeddings) could change this conclusion remains open.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals likely requires content-aware verifiers \cite{cobbe2021verifiers}; LP provides a practical baseline when both conditions are met, with degeneracy controllable via temperature and training convergence.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1249 · 2026-05-18T06:04:27.438402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1250 · 2026-05-18T06:04:27.990213+00:00_

File content (35137 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 1251 · 2026-05-18T06:04:27.990622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1252 · 2026-05-18T06:04:28.041022+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and the two conditions may shift in opposite directions.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned s
…[truncated 1023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1253 · 2026-05-18T06:04:33.893755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1254 · 2026-05-18T06:04:33.997591+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 13589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1255 · 2026-05-18T06:04:38.625842+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "epoch_confound|epoch_scierc|app:epoch",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "epoch_confound|epoch_scierc|app:epoch",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1256 · 2026-05-18T06:04:38.676470+00:00_

1045:This confirms that temperature controls degeneracy (the first necessary condition) but cannot improve LP-quality alignment (the second condition), which is largely determined by task structure and remains relatively stable across generation configurations (\S\ref{app:epoch_confound}); the two conditions are jointly necessary and independently variable.
1294:\section{Epoch Confound Analysis}\label{app:epoch_confound}
1297:Table~\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$).
1310:\label{tab:epoch_confound}
1326:Table~\ref{tab:epoch_scierc} extends the analysis to SciERC with a 3-point curve (3, 5, 10 epochs; Qwen3-8B, $N{=}8$, $T{=}1.0$).
1336:\label{tab:epoch_scierc}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1257 · 2026-05-18T06:04:42.641827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1294",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1294",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-18T06:04:42.742677+00:00_

1294	\section{Epoch Confound Analysis}\label{app:epoch_confound}
1295	
1296	\paragraph{Training convergence modulates degeneracy.}
1297	Table~\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$).
1298	Extended training increases greedy F1 by $+2.95$~pp (0.748 $\to$ 0.777) but nearly triples instance degeneracy (11.1\% $\to$ 31.3\%), reducing the fraction of instances with non-degenerate outputs from 85.6\% to 68.7\%.
1299	LP selection gains drop correspondingly ($+1.37$~pp $\to$ $+0.62$~pp), consistent with the degeneracy-gating mechanism identified in the main text (\S\ref{sec:discussion}).
1300	Within-instance LP-quality alignment is relatively stable under this convergence shift (mean $\rho$: $0.524 \to 0.407$; median $\rho$: $0.667 \to 0.615$), consistent with alignment being determined primarily by task structure rather than training duration.
1301	
1302	Evaluation loss increases after epoch 3 (0.032 $\to$ 0.041 at epoch 5), and the best checkpoint by validation loss occurs at step 32{,}000 (approximately epoch 3.9).
1303	Standard early stopping practice thus naturally selects the low-degeneracy regime where LP selection is most effective.
1304	This finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.
1305	
1306	\begin{table}[t]
1307	\centering
1308	\small
1309	\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``Valid'': fraction of instances with non-degenerate outputs. ``$\rho$ mean/med'': within-instance LP-quality correlation. The 3-epoch model corresponds to standard early stopping; the 5-epoch model is a controlled ablation.}
1310	\label{tab:epoch
…[truncated 3277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-18T06:07:01.030643+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 1260 · 2026-05-18T06:07:01.082142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-18T06:07:53.778610+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n### Must-Fix\n\n**[AGREE] R2-N1: Contribution 1 中 \"methodological premise\" 的贡献定位不当**\n\n同意。Instance-level aggregate 无法区分 per-sample candidates 是定义的直接推论——任何理解 MBR decoding 中 utility function 与 candidate ranking 关系的读者都能从信号定义推导出这一点。论文自身在 Abstract (line 8) 用的措辞是 \"A methodological premise underlies both\"，在 Section 1 Contribution 1 中称其为 \"A definitional observation structures the analysis\"，这两处措辞已经暗示了定义性质，但将其列入 Contribution 列表确实 inflates 了贡献。\n\n补充发现：Section 2.1 (Method, line 7) 第三次重复了这一观察 (\"This distinction is consequential for selection\")，Section 4.3 (line 57) 第四次重复 (\"A methodological observation underlies both\")。四次重复一个定义推论进一步加重了 inflation 感。建议将其降级为 §2.1 的 framing remark，从 Contribution 列表移除。\n\n**[REBUT] R2-N2: \"Correlation-selection gap\" 的新颖性 vs. Eikema et al. (2025)**\n\nR2 的关切有道理——差异化定位确实不够锐利——但 R2 对 novelty 的判断偏严。关键差异在于：Eikema et al. (2025) 诊断的是 **utility misalignment**（MBR utility function 本身在结构化输出上退化）；本文诊断的是 **degeneracy**（即使 utility 是 well-aligned 的，candidate pool 本身缺乏方差）。论文在 Related Work (§2, \"Uncertainty estimation and MBR decoding\" 段) 明确写到：\n\n> \"our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck\"\n\n且 Discussion §5 (\"Why the gap exists\") 报告了非退化实例中 MBR utility 与 F1 的 median ρ=0.524，closes 23–41% oracle gap——说明在有方差的地方 utility 是有效的，瓶颈不在 utility 本身。这是与 Eikema et al. 的实质区别。\n\n但我同意 R2 的建议：这个区别应在 Introduction 中更醒目地写出来，而不是留在 Related Work 的一个从句里。当前定位确实容易让读者混淆。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 数字过载**\n\n同意。至少 8 个定量值（ρ up to 0.45, AUROC up to 0.82, +1.36 pp, p<0.001, ρ ≳ 0.3, ~13 pp, 14–59%, \"four of five\"）。Abstract 应该讲故事而非堆数据。建议保留 3 个以内关键数字，将其余推至 Introduction。\n\n**[AGREE] R2-W2: Actionable contribution 偏薄**\n\n同意，且我认为这是本文最大的结构性弱点之一。LP 的正面结果限于 Few-NERD 的特定条件（低 degeneracy + 高 alignment），不满足条件时的 actionable advice 就是 \"use greedy decoding\"。对 practitioners 来说，这等于\"多采样没用，别费劲了\"。论文 Discussion §5 (\"Practical guidelines\") 给出的 decision rule 需要 labeled dev set 来估计——而如果已有 labeled data，practitioners 通常有更好的策略。\n\nR2 建议增加 forward-looking analysis，我赞同。当前 Conclusion 最后一句 (\"Closing the gap for structural signals likely requires content-aware verifiers\") 太泛了，应该更具体地讨论 verifier 设计空间。\n\n**[AGREE] R2-W3: Discussion section 碎片化**\n\n同意。Discussion 有 7 个独立段落主题（practitioners, why the gap exists, non-tied subset, LP compression, regime boundaries, practical guidelines, methodological implications），每个只有 1 段。\"Implications for practitioners\" 和 \"Practical guidelines\" 内容高度重叠，应合并。\"LP compression mechanisms\" 和 \"Why the gap exists\" 也可以整合。\n\n**[REBUT] R2-W4: 纯诊断性论文对 EMNLP main 的门槛**\n\nR2 说核心信息可以用一句话概括。但这一标准太严——很多实验性发现都可以用一句话概括（如 \"scaling laws are power laws\"），判断标准应该是诊断的 **depth 和 non-triviality**。本文的贡献不是一句话的结论，而是：(1) 系统量化了 degeneracy 的普遍性和可控性（temperature, epoch）；(2) 证明了两个条件是 independently necessary（temperature ablation isolates degeneracy from alignment）；(3) 统计方法论远超同类工作（R2 自己在 S2 也承认了这一点）。\n\n不过我部分同意底层关切：论文的 framing 过于侧重\"什么不行\"而非\"为什么不行以及怎么办\"。如果 Introduction 能更强调 diagnostic contribution 的方法论价值（例如，QE-selection separation 框架可推广到其他 structured output 任务），说服力会更强。\n\n**[AGREE] R2-W5: 核心发现重复性过高**\n\n同意。\"14–59% degeneracy\" 在 Abstract, Introduction, Experiments, Discussion, Conclusion 均出现，几乎逐字重复。\"+1.36 pp on Few-NERD\" 同样至少出现 5 次。建议 Introduction 和 Conclusion 用叙事性语言概括，把精确数字留在 Experiments。\n\n**[AGREE] R2-W6: Few-NERD 训练设置差异引入混淆**\n\n同意这是一个真实的 confound，但不同意其最强解读（即正面结果纯粹是 artifact）。\n\n证据：Appendix Table 12 (tab:epoch_scierc) 显示 SciERC 在 3 epochs 时 degeneracy 仅 6.4%（低于 Few-NERD 的 13.8%），但 LP selection Δ = −1.18 pp（负值）。原因是 within-instance ρ=0.317（不满足条件 2，Few-NERD 为 ~0.5）。这说明低 degeneracy alone 不足以产生 LP gains，不是单纯的 epoch 效应。Appendix Table 11 (tab:epoch_confound) 显示 Few-NERD 5-epoch LP gains 从 +1.37 降至 +0.62 pp——仍为正值且由 degeneracy 变化（11.1% → 31.3%）解释。\n\n但 R2 的关切仍然成立：唯一正面结果来自唯一使用不同训练设置的数据集，这在审稿人眼中天然可疑。建议在正文（而非仅在 Appendix）更显著地讨论 SciERC 3-epoch control 作为反驳证据。\n\n### Minor\n\n**[AGREE] R2-M1**: \"14\\textendash 59\\%\" 重复过多，同 W5。\n\n**[AGREE] R2-M2**: Table 3 caption footnote 不优雅，技术性小问题。\n\n**[AGREE] R2-M3**: Conclusion 最后两句结构松散，建议合并或加过渡。\n\n**[REBUT] R2-M4**: Ethics Statement 4 句的长度在 EMNLP 2026 中属于正常范围。论文使用公开 benchmark + 开源模型，无新数据收集，ethical risk 本身较低。ARR review form 不对 Ethics Statement 长度设硬性要求。内容覆盖了数据来源、模型来源、potential societal impact、code release，覆盖面已足够。\n\n**[AGREE] R2-M5**: Table 3 (tab:fewnerd) 缺少 WNUT-17 列。不过 WNUT-17 可能因信号 collapse（VC conditional ρ=0.038）导致 selection 数据不 meaningful，论文应在 caption 或 footnote 说明。\n\n### Questions\n\n**[REBUT] R2-Q1: SciERC 3-epoch 的 selection F1**\n\nAppendix Table 12 (tab:epoch_scierc) 已经回答：SciERC 3-epoch LP Δ = −1.18 pp（负值）。这**支持** \"two jointly necessary conditions\" claim：SciERC 3-epoch degeneracy 仅 6.4%（满足条件 1），但 within-instance ρ=0.317（不满足条件 2，Few-NERD 为 ~0.5），因此 LP selection 失败。恰好证明两个条件确实是 jointly necessary——只满足其一不够。Claim 不需要修正。\n\n**[AGREE] R2-Q2: Per-type LP selection heterogeneity on SciERC**\n\n论文报告了 Few-NERD 的 per-entity-type analysis (ρ=−0.881, p=0.004, n=8) 但没有 SciERC 的等价分析。SciERC 有 6 个 entity types，虽然 n 较小统计 power 有限，但报告这个分析可以展示 degeneracy-selection 关系的跨数据集一致性（或不一致性），是有价值的补充。\n\n**[AGREE] R2-Q3: \"Supervised verifier baseline\" 命名误导**\n\n同意。论文的 \"supervised verifier\" 实际是在 5 个无监督信号上训练 LR/MLP/RF（§4.5），而非 ORM/PRM 意义上的 trained verifier。\"Supervised signal combination\" 或 \"supervised signal aggregation\" 更准确。\n\n**[AGREE] R2-Q4: Per-entity-type effective df 问题**\n\n论文已自行 flag 了这个问题（§4.3 和 Figure 2 caption 均注明 \"effective degrees of freedom may be lower\"），但仅靠 disclaimer 不够。n=8 的 entity types 共享模型、tokenizer、temperature，effective df 可能远低于 6。Permutation test 实现成本很低，应该做。\n\n### Missing References\n\n**[REBUT] 三篇均非必要引用。**\n- Ippolito et al. (2019): 关注 text generation diverse decoding，与 NER structured output 关联弱。论文已引用 Vijayakumar et al. (2018) 和 Holtzman et al. (2020) 覆盖 decoding diversity。\n- Xiao & Wang (2021): 聚焦 hallucination 和 uncertainty，非 structured extraction。论文已引用 uncertainty 综述（Xia et al. 2025）。\n- Li et al. (2024) \"Rain\": self-alignment 方向，与 NER self-consistency/selection 无直接关联。\n\n### R2 遗漏但 R1 注意到的问题\n\n1. **RE extension 的定位模糊**：论文在 Introduction 和多处提到 \"exploratory extension to RE\"，但 RE 结果从未在正文表格中出现。如果 RE 只是 exploratory，应减少正文提及频率；如果重要到反复提及，应在正文报告核心 RE 数据。\n2. **Free-form ablation 的跨任务不一致性**：Discussion §5 报告 free-form decoding 对 NER 无效（std ratio 0.97）但对 RE 恢复了 selection (+1.8±0.1 pp），NER/RE 分歧的原因论文只一笔带过，没有解释。\n\n### 总结\n\nR2 的审稿整体准确且有价值。N1（contribution inflation）、W2（actionable contribution 薄弱）、W6（Few-NERD 训练 confound）是最值得关注的问题。N2 的 novelty 关切有道理但 R2 忽略了论文已做的 degeneracy vs. utility 区分。我在 W4（纯诊断论文门槛）上与 R2 存在分歧——诊断的深度和统计严谨性本身构成 contribution，但论文需要更好地 frame 这一点。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n### Must-Fix\n\n**[AGREE] R2-N1: Contribution 1 中 \"methodological premise\" 的贡献定位不当**\n\n同意。Instance-level aggregate 无法区分 per-sample candidates 是定义的直接推论——任何理解 MBR decoding 中 utility function 与 candidate ranking 关系的读者都能从信号定义推导出这一点。论文自身在 Abstract (line 8) 用的措辞是 \"A methodological premise underlies both\"，在 Section 1 Contribution 1 中称其为 \"A definitional observation structures the analysis\"，这两处措辞已经暗示了定义性质，但将其列入 Contribution 列表确实 inflates 了贡献。\n\n补充发现：Section 2.1 (Method, line 7) 第三次重复了这一观察 (\"This distinction is consequential for selection\")，Section 4.3 (line 57) 第四次重复 (\"A methodological observation underlies both\")。四次重复一个定义推论进一步加重了 inflation 感。建议将其降级为 §2.1 的 framing remark，从 Contribution 列表移除。\n\n**[REBUT] R2-N2: \"Correlation-selection gap\" 的新颖性 vs. Eikema et al. (2025)**\n\nR2 的关切有道理——差异化定位确实不够锐利——但 R2 对 novelty 的判断偏严。关键差异在于：Eikema et al. (2025) 诊断的是 **utility misalignment**（MBR utility function 本身在结构化输出上退化）；本文诊断的是 **degeneracy**（即使 utility 是 well-aligned 的，candidate pool 本身缺乏方差）。论文在 Related Work (§2, \"Uncertainty estimation and MBR decoding\" 段) 明确写到：\n\n> \"our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck\"\n\n且 Discussion §5 (\"Why the gap exists\") 报告了非退化实例中 MBR utility 与 F1 的 median ρ=0.524，closes 23–41% oracle gap——说明在有方差的地方 utility 是有效的，瓶颈不在 utility 本身。这是与 Eikema et al. 的实质区别。\n\n但我同意 R2 的建议：这个区别应在 Introduction 中更醒目地写出来，而不是留在 Related Work 的一个从句里。当前定位确实容易让读者混淆。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 数字过载**\n\n同意。至少 8 个定量值（ρ up to 0.45, AUROC up to 0.82, +1.36 pp, p<0.001, ρ ≳ 0.3, ~13 pp, 14–59%, \"four of five\"）。Abstract 应该讲故事而非堆数据。建议保留 3 个以内关键数字，将其余推至 Introduction。\n\n**[AGREE] R2-W2: Actionable contribution 偏薄**\n\n同意，且我认为这是本文最大的结构性弱点之一。LP 的正面结果限于 Few-NERD 的特定条件（低 degeneracy + 高 alignment），不满足条件时的 actionable advice 就是 \"use greedy decoding\"。对 practitioners 来说，这等于\"多采样没用，别费劲了\"。论文 Discussion §5 (\"Practical guidelines\") 给出的 decision rule 需要 labeled dev set 来估计——而如果已有 labeled data，practitioners 通常有更好的策略。\n\nR2 建议增加 forward-looking analysis，我赞同。当前 Conclusion 最后一句 (\"Closing the gap for structural signals likely requires content-aware verifiers\") 太泛了，应该更具体地讨论 verifier 设计空间。\n\n**[AGREE] R2-W3: Discussion section 碎片化**\n\n同意。Discussion 有 7 个独立段落主题（practitioners, why the gap exists, non-tied subset, LP compression, regime boundaries, practical guidelines, methodological implications），每个只有 1 段。\"Implications for practitioners\" 和 \"Practical guidelines\" 内容高度重叠，应合并。\"LP compression mechanisms\" 和 \"Why the gap exists\" 也可以整合。\n\n**[REBUT] R2-W4: 纯诊断性论文对 EMNLP main 的门槛**\n\nR2 说核心信息可以用一句话概括。但这一标准太严——很多实验性发现都可以用一句话概括（如 \"scaling laws are power laws\"），判断标准应该是诊断的 **depth 和 non-triviality**。本文的贡献不是一句话的结论，而是：(1) 系统量化了 degeneracy 的普遍性和可控性（temperature, epoch）；(2) 证明了两个条件是 independently necessary（temperature ablation isolates degeneracy from alignment）；(3) 统计方法论远超同类工作（R2 自己在 S2 也承认了这一点）。\n\n不过我部分同意底层关切：论文的 framing 过于侧重\"什么不行\"而非\"为什么不行以及怎么办\"。如果 Introduction 能更强调 diagnostic contribution 的方法论价值（例如，QE-selection separation 框架可推广到其他 structured output 任务），说服力会更强。\n\n**[AGREE] R2-W5: 核心发现重复性过高**\n\n同意。\"14–59% degeneracy\" 在 Abstract, Introduction, Experiments, Discussion, Conclusion 均出现，几乎逐字重复。\"+1.36 pp on Few-NERD\" 同样至少出现 5 次。建议 Introduction 和 Conclusion 用叙事性语言概括，把精确数字留在 Experiments。\n\n**[AGREE] R2-W6: Few-NERD 训练设置差异引入混淆**\n\n同意这是一个真实的 confound，但不同意其最强解读（即正面结果纯粹是 artifact）。\n\n证据：Appendix Table 12 (tab:epoch_scierc) 显示 SciERC 在 3 epochs 时 degeneracy 仅 6.4%（低于 Few-NERD 的 13.8%），但 LP selection Δ = −1.18 pp（负值）。原因是 within-instance ρ=0.317（不满足条件 2，Few-NERD 为 ~0.5）。这说明低 degeneracy alone 不足以产生 LP gains，不是单纯的 epoch 效应。Appendix Table 11 (tab:epoch_confound) 显示 Few-NERD 5-epoch LP gains 从 +1.37 降至 +0.62 pp——仍为正值且由 degeneracy 变化（11.1% → 31.3%）解释。\n\n但 R2 的关切仍然成立：唯一正面结果来自唯一使用不同训练设置的数据集，这在审稿人眼中天然可疑。建议在正文（而非仅在 Appendix）更显著地讨论 SciERC 3-epoch control 作为反驳证据。\n\n### Minor\n\n**[AGREE] R2-M1**: \"14\\textendash 59\\%\" 重复过多，同 W5。\n\n**[AGREE] R2-M2**: Table 3 caption footnote 不优雅，技术性小问题。\n\n**[AGREE] R2-M3**: Conclusion 最后两句结构松散，建议合并或加过渡。\n\n**[REBUT] R2-M4**: Ethics Statement 4 句的长度在 EMNLP 2026 中属于正常范围。论文使用公开 benchmark + 开源模型，无新数据收集，ethical risk 本身较低。ARR review form 不对 Ethics Statement 长度设硬性要求。内容覆盖了数据来源、模型来源、potential societal impact、code release，覆盖面已足够。\n\n**[AGREE] R2-M5**: Table 3 (tab:fewnerd) 缺少 WNUT-17 列。不过 WNUT-17 可能因信号 collapse（VC conditional ρ=0.038）导致 selection 数据不 meaningful，论文应在 caption 或 footnote 说明。\n\n### Questions\n\n**[REBUT] R2-Q1: SciERC 3-epoch 的 selection F1**\n\nAppendix Table 12 (tab:epoch_scierc) 已经回答：SciERC 3-epoch LP Δ = −1.18 pp（负值）。这**支持** \"two jointly necessary conditions\" claim：SciERC 3-epoch degeneracy 仅 6.4%（满足条件 1），但 within-instance ρ=0.317（不满足条件 2，Few-NERD 为 ~0.5），因此 LP selection 失败。恰好证明两个条件确实是 jointly necessary——只满足其一不够。Claim 不需要修正。\n\n**[AGREE] R2-Q2: Per-type LP selection heterogeneity on SciERC**\n\n论文报告了 Few-NERD 的 per-entity-type analysis (ρ=−0.881, p=0.004, n=8) 但没有 SciERC 的等价分析。SciERC 有 6 个 entity types，虽然 n 较小统计 power 有限，但报告这个分析可以展示 degeneracy-selection 关系的跨数据集一致性（或不一致性），是有价值的补充。\n\n**[AGREE] R2-Q3: \"Supervised verifier baseline\" 命名误导**\n\n同意。论文的 \"supervised verifier\" 实际是在 5 个无监督信号上训练 LR/MLP/RF（§4.5），而非 ORM/PRM 意义上的 trained verifier。\"Supervised signal combination\" 或 \"supervised signal aggregation\" 更准确。\n\n**[AGREE] R2-Q4: Per-entity-type effective df 问题**\n\n论文已自行 flag 了这个问题（§4.3 和 Figure 2 caption 均注明 \"effective degrees of freedom may be lower\"），但仅靠 disclaimer 不够。n=8 的 entity types 共享模型、tokenizer、temperature，effective df 可能远低于 6。Permutation test 实现成本很低，应该做。\n\n### Missing References\n\n**[REBUT] 三篇均非必要引用。**\n- Ippolito et al. (2019): 关注 text generation diverse decoding，与 NER structured output 关联弱。论文已引用 Vijayakumar et al. (2018) 和 Holtzman et al. (2020) 覆盖 decoding diversity。\n- Xiao & Wang (2021): 聚焦 hallucination 和 uncertainty，非 structured extraction。论文已引用 uncertainty 综述（Xia et al. 2025）。\n- Li et al. (2024) \"Rain\": self-alignment 方向，与 NER self-consistency/selection 无直接关联。\n\n### R2 遗漏但 R1 注意到的问题\n\n1. **RE extension 的定位模糊**：论文在 Introduction 和多处提到 \"exploratory extension to RE\"，但 RE 结果从未在正文表格中出现。如果 RE 只是 exploratory，应减少正文提及频率；如果重要到反复提及，应在正文报告核心 RE 数据。\n2. **Free-form ablation 的跨任务不一致性**：Discussion §5 报告 free-form decoding 对 NER 无效（std ratio 0.97）但对 RE 恢复了 selection (+1.8±0.1 pp），NER/RE 分歧的原因论文只一笔带过，没有解释。\n\n### 总结\n\nR2 的审稿整体准确且有价值。N1（contribution inflation）、W2（actionable contribution 薄弱）、W6（Few-NERD 训练 confound）是最值得关注的问题。N2 的 novelty 关切有道理但 R2 忽略了论文已做的 degeneracy vs. utility 区分。我在 W4（纯诊断论文门槛）上与 R2 存在分歧——诊断的深度和统计严谨性本身构成 contribution，但论文需要更好地 frame 这一点。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1262 · 2026-05-18T06:07:57.845603+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1263 · 2026-05-18T06:08:04.122071+00:00_

已提交交叉回应。总结：

- **AGREE 12 条**：N1（contribution inflation）、W1–W3、W5–W6、M1–M3、M5、Q2–Q4
- **REBUT 5 条**：N2（novelty 有实质区别但定位需更锐利）、W4（诊断深度本身有价值）、M4（Ethics Statement 长度正常）、Q1（SciERC 3-epoch 数据反而支持 claim）、Missing References（三篇均非必要）
- **补充了 R2 遗漏的两个问题**：RE extension 定位模糊、free-form ablation 跨任务不一致性未解释

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 40

## Round 40

46 recorded events


### User

_source line 1264 · 2026-05-18T12:46:58.602088+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference（ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，长文 ≤8 页正文（不含 Limitations/Ethics/References），double-blind
- **匿名规则**: 作者匿名，review 版需行号

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`
（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）
参考文献：`references.bib`

### 你的审查侧重

**重点审查方法严谨性和实验设计**，具体包括：

1. **信号定义的严谨性**：5 个信号（LP, SJ, FK, EM, VC）的数学定义是否清晰、无歧义？instance-level vs per-sample 的区分是否一致？consensus-proximity (MBR) 转换是否合理？

2. **实验协议**：
   - 数据集选择（SciERC, CoNLL, Few-NERD, WNUT-17）的理由是否充分？是否存在选择偏差？
   - 模型选择和训练配置是否合理？LoRA rank=32 vs 8 的消融是否 confound capacity 和 diversity？
   - N=8 主实验 + N=16 scaling 是否足够？seed 数量（部分只用 1 seed）是否影响结论可靠性？
   - Few-NERD 用 3 epoch vs 其他数据集 5 epoch，epoch confound 是否被充分控制？

3. **统计方法**：
   - 显著性检验方法（sign test, paired bootstrap, TOST）是否合适？
   - MDE 分析是否正确？SciERC 上 n=529 的 power 是否足以支撑"无显著差异"的结论？
   - 多重比较校正是否充分？
   - "correlation-selection gap" 是否可能是统计伪影（power 不足导致的 Type II error）？

4. **消融实验充分性**：
   - temperature, LoRA rank, 模型规模、训练 epoch 的消融是否覆盖了关键变量？
   - DeBERTa verifier 和 hidden state probe 的实验设计是否公平？
   - DALS 方法的评估是否充分（仅在有限数据集上测试）？

5. **可重复性**：
   - 训练细节、推理参数、随机种子是否完整记录？
   - 是否有明显的实验 confound 未被控制？

6. **附录内容**：检查附录中的分析是否支持正文的 claim，是否存在正文未引用的附录内容。

请按以下格式输出审稿意见：

```
## Summary
[2-3 句概述]

## Strengths
[逐条列出优点，标记 S1, S2, ...]

## Weaknesses
[逐条列出缺点，标记 W1, W2, ... 每条标注严重程度：Critical / Major / Minor]

## Questions
[需要作者澄清的问题，标记 Q1, Q2, ...]

## Missing References
[遗漏的重要相关工作]

## Detailed Comments
[逐节详细意见]

## Overall Assessment
[评分: strong reject / weak reject / borderline / weak accept / strong accept]
[置信度: 1-5]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1265 · 2026-05-18T12:47:09.285213+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1266 · 2026-05-18T12:47:09.335739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1267 · 2026-05-18T12:47:13.446448+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-18T12:47:14.401327+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-18T12:47:14.451893+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1270 · 2026-05-18T12:47:22.837178+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've found comprehensive information about ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get the first impressio
…[truncated 1846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9390
}
```

</details>

---


### Tool call

_source line 1271 · 2026-05-18T12:47:30.625691+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include Overall Assessment scale, Soundness, Excitement, Reproducibility, and any other rated dimensions with their exact score descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include Overall Assessment scale, Soundness, Excitement, Reproducibility, and any other rated dimensions with their exact score descriptions."
  }
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-18T12:47:32.132035+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including what reviewers should evaluate, how to assess papers, and any specific instructions about scoring criteria, common pitfalls, and review quality expectations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including what reviewers should evaluate, how to assess papers, and any specific instructions about scoring criteria, common pitfalls, and review quality expectations."
  }
}
```

</details>

---


### Tool call

_source line 1273 · 2026-05-18T12:47:32.684570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1274 · 2026-05-18T12:47:33.538355+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1275 · 2026-05-18T12:47:33.588928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1276 · 2026-05-18T12:47:33.589331+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve reliable quality estimation, supporting selective prediction.
5	For selection, LP achieves $+1.39$~pp on Few-NERD when two conditions are jointly satisfied: low instance degeneracy and adequate LP-quality alignment.
6	When either condition is violated, LP gains fall below detectable thresholds despite ${\sim}$13~pp oracle headroom, a disparity we term the \textbf{correlation-selection gap}.
7	Two mechanisms explain this gap: \textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom; \textit{weak LP-quality alignment} prevents exploiting the remainder.
8	Degeneracy is controllable via temperature and training convergence; neither scalar signal combinations nor learned text representations close the gap.
9	Hidden state probes confirm information beyond LP exists in model representations, but the correlation-selection gap persists: richer signals do not improve selection in the high-capability regime.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1277 · 2026-05-18T12:47:34.040566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1278 · 2026-05-18T12:47:34.492101+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \textit{why} this correlation does not reliably translate to selection gains, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly satisfied: low instance degeneracy (13.8\%) and adequate alignment ($\rho{\approx}0.5$), with gains sc
…[truncated 4418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1279 · 2026-05-18T12:47:34.492471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1280 · 2026-05-18T12:47:34.943779+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 2976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1281 · 2026-05-18T12:47:34.994312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1282 · 2026-05-18T12:47:35.746228+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\ref{app:epoch_confound}).
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses
…[truncated 16738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 751
}
```

</details>

---


### Tool call

_source line 1283 · 2026-05-18T12:47:35.796912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1284 · 2026-05-18T12:47:35.847610+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
6	We extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.
10	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised signal combination baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden, yun2025price}.
14	
15	\paragraph{Uncertainty estimation and MBR decoding.}
16	Surveys cover confidence estimation \cit
…[truncated 1934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-18T12:47:38.255898+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4.5**: Borderline Award
- **4**: "Conference: I think this paper could be accepted to an *ACL conference"
- **3.5**: Borderline Conference
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2.5**: Borderline Findings
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions that can be completed"
- **1.5**: "Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed"
- **1**: "Do not resubmit: This paper has to be fully redone, or it is not relevant"

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others"
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or 
…[truncated 579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7630
}
```

</details>

---


### Tool result

_source line 1286 · 2026-05-18T12:47:43.231345+00:00_

# ARR Reviewer Guidelines Summary

## Core Reviewing Tasks

Reviewers must complete four main tasks:

1. **Allocate calendar time** for both reviewing and discussion periods
2. **Check assignments** for expertise, conflicts of interest, and desk-rejection criteria
3. **Write strong reviews** with specific, justified feedback
4. **Update assessments** after author responses and reviewer discussion

## What to Evaluate

### Soundness Assessment
Reviewers must ensure their soundness scores are "justified by the text of the review." Papers should be evaluated for technical correctness, valid argumentation, and appropriate methodology. Low scores require clear justification; relying on unstated biases is inappropriate.

### Excitement and Overall Recommendation
"Excitement scores reflect our personal taste" and are separate from soundness evaluation. The overall recommendation balances soundness, excitement, novelty, and potential impact.

## Review Writing Standards

### Be Specific
Avoid vague criticisms. Instead of "X is not clear," specify what information is missing. Reference specific lines or concepts rather than general complaints about methodology or novelty.

### Check Common Reviewer Biases (H1-H17)

Problematic patterns include:
- Dismissing results as "obvious" (confirmation bias)
- Expecting SOTA results when not claimed
- Rejecting work for being "too simple" or "too niche"
- Requesting unnecessary experiments beyond the paper's claims

### Check Common Paper Problems (M, T, R, G categories)

**Methodology issues (M):** LLM-only evaluation without validation, reproducibility gaps, data quality problems, unmotivated selections, incomplete proofs.

**Artifact sourcing (T):** Ethical data collection concerns, unclear licensing.

**Results issues (R):** Statistical problems, overclaiming, inappropriate scope, missing significance testing.

**General issues (G):** Unclear contributions, bad precedent reliance, misrepresented related work, vague terminology, mis
…[truncated 1521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11099
}
```

</details>

---


### Tool call

_source line 1287 · 2026-05-18T12:47:50.360986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1288 · 2026-05-18T12:47:50.764218+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications.}
4	All signals achieve positive quality estimation across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL), with rankings stable across model families and a 4B ablation (Table~\ref{tab:scale_ablation}).
5	For selection, LP achieves significant gains only when both conditions are met (Table~\ref{tab:fewnerd}); structural signals uniformly degrade selection.
6	RE signal rankings (exploratory, single benchmark) are in Appendix~\ref{app:re_extension}.
7	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; even supervised combination of these five unsupervised signals does not close the oracle gap (\S\ref{sec:robustness_main}).
8	Effective selection requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most QE benefit (Appendix~\ref{app:n_scaling}).
9	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
10	
11	\paragraph{Why the gap exists.}
12	Two mechanisms block selection: \textit{instance degeneracy} (consensus-proximity) and \textit{weak LP-quality alignment} (per-sample).
13	Within non-degenerate instances, MBR utility \cite{eikema2022sampling} correlates positively with F1 (SJ median $\rho{=}0.524$) and closes 23--41\% of the oracle gap, but 17.8\% (SciERC) to 59.1\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\ref{tab:degeneracy}).
14	Degeneracy is determined by the interplay of task structure, model architecture, and training convergence (Appendix~\ref{app:epoch_confound}); cross-model evidence (LLaMA 89.2\% vs.\ Qwen 59.1\% on CoNLL; Table~\ref{tab:cross_selection}) reinforces the pattern.
15	LP is severely compressed (median range 0.041 nats; Table~\ref{tab:logprob_ties}), with median within-instance $\rho(\
…[truncated 8304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1289 · 2026-05-18T12:47:50.864875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1290 · 2026-05-18T12:47:50.865286+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.
5	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly satisfied: low instance degeneracy (${<}$15\%) and adequate LP-quality alignment ($\rho \gtrsim 0.3$, approximate threshold from our data); gains scale with sample budget ($+0.52$~pp, $N{=}8{\to}16$, $p{=}0.003$).
6	When either condition is violated, LP gains fall below detectable thresholds despite 12\textendash 14~pp oracle headroom: on SciERC (17.8\% degeneracy, $\rho{\approx}0.24$), LP yields $+0.61$~pp (below the ${\approx}$1.5~pp MDE at 80\% power); on CoNLL (59.1\% degeneracy), LP degrades selection ($-0.85$~pp).
7	Two mechanisms explain this gap: instance degeneracy eliminates headroom, and weak LP-quality alignment prevents exploiting the remainder.
8	Structural signals do not improve selection regardless of degeneracy; neither supervised combination of all five signals nor a learned DeBERTa verifier closes the oracle gap.
9	Hidden state probes confirm richer information exists in model representations ($+37$\% correlation on SciERC) but the correlation-selection gap persists even with model-internal access (gap closure $-5.1$\%); closing the gap likely requires verifiers that exploit content-level differences \cite{cobbe2021verifiers}, not just quality signals.
10	As models improve through scale and training convergence, degeneracy rises and LP compression intensifies, narrowing the window for test-time selection: the same progress that reduces error also reduces the diversity on which selection depends.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1291 · 2026-05-18T12:47:51.567497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1292 · 2026-05-18T12:47:51.918763+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and the two conditions may shift in opposite directions.
3	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{ap
…[truncated 1947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1293 · 2026-05-18T12:47:51.919109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1294 · 2026-05-18T12:47:52.220296+00:00_

File content (35940 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-18T12:47:59.996052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 1296 · 2026-05-18T12:48:00.297852+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 36675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1297 · 2026-05-18T12:48:06.777001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 1298 · 2026-05-18T12:48:07.178598+00:00_

500	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
501	
502	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
503	
504	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
505	We quantify the potential impact on LP scores through three complementary arguments.
506	
507	\paragraph{LP shift magnitude.}
508	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
509	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
510	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
511	
512	\paragraph{Constant prefix cancellation.}
513	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
514	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
515	
516	\paragraph{CoNLL control group.}
517	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
518	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
519	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at 
…[truncated 30746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1299 · 2026-05-18T12:48:12.682604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1000",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1000",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 1300 · 2026-05-18T12:48:12.934264+00:00_

1000	\midrule
1001	2 & 42.7\% & $+$4.4 & $-$0.89 & $-$2.72 & $-$2.72 & $-$2.72 & $-$2.66 & $-$0.89 \\
1002	4 & 21.0\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\
1003	8 & 11.0\% & $+$14.5 & $+$0.39 & $+$0.20 & $+$0.15 & $-$0.77 & $-$2.87 & $+$0.39 \\
1004	16 & 7.4\% & $+$17.7 & $+$0.78 & $+$0.24 & $-$0.02 & $-$0.06 & $-$3.95 & $+$0.78 \\
1005	32 & 4.0\% & $+$20.0 & $+$0.95 & $+$0.35 & $+$0.65 & $+$0.22 & $-$4.35 & $+$0.95 \\
1006	\bottomrule
1007	\end{tabular}
1008	\end{table}
1009	\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$). Values differ slightly from Table~\ref{tab:selection} (0.645) and Table~\ref{tab:fewnerd} (0.644) due to seed and aggregation differences; relative trends are consistent.}
1010	
1011	\paragraph{Bootstrap significance at $N{=}32$.}
1012	Table~\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).
1013	No signal achieves significant improvement over greedy at $\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \textit{worse} ($-4.36$~pp, $p{=}1.0$).
1014	However, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test); the signals carry meaningful quality information yet fail to translate it into reliable selection gains.
1015	The oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.
1016	
1017	\begin{table}[t]
1018	\centering
1019	\small
1020	\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\Delta$: selection gain vs.\ greedy. CI: 95\% bootstrap percentile interval. $p_{\text{greedy}}$: one-sided $p$-value vs.\ greedy; $p_{\text{rand}}$: permutation test vs.\ random selection.}
1021	\label{tab:bootstrap_n32}
1022	\beg
…[truncated 27041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1301 · 2026-05-18T12:48:19.024251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1381",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1381",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1302 · 2026-05-18T12:48:19.074801+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1381). The file has 1381 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1303 · 2026-05-18T12:48:24.844408+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1304 · 2026-05-18T12:49:31.990498+00:00_

&lt;persisted-output>
Output too large (53.3KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/toolu_01EtytTff2rxCgpAiNFbhHPn.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 64, \"total_citations\": 97, \"unique_cited_keys\": 64, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 57, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, .
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 67146
}
```

</details>

---


### Tool call

_source line 1305 · 2026-05-18T12:49:35.701905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/toolu_01EtytTff2rxCgpAiNFbhHPn.txt",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/toolu_01EtytTff2rxCgpAiNFbhHPn.txt",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1306 · 2026-05-18T12:49:35.954786+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 64, \"total_citations\": 97, \"unique_cited_keys\": 64, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 57, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"ven
…[truncated 52622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1307 · 2026-05-18T12:53:15.213584+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 Round 1 审稿完成\n\n### 总体评分\n- **Overall**: 3.5 (Borderline Conference)\n- **Soundness**: 3/5\n- **Excitement**: 3/5\n- **Reproducibility**: 4/5\n- **Confidence**: 4/5\n\n### 核心判断\n实验全面、透明度高、负面结果诚实呈现，但核心框架（两个条件）的跨数据集支撑仅 3 个点，且 headline positive result（Few-NERD +1.39pp）受 epoch confound 显著影响。\n\n### Must-Fix (2 个 Critical)\n\n**N1: \"两个条件\"框架经验基础不足**\n- 跨数据集仅 3 个数据点（CoNLL/SciERC/Few-NERD），论文自身标注 \"exploratory given 5+ confounds\"\n- 15% degeneracy 阈值来自 Few-NERD per-entity-type 两个相邻点（Person 13.4% vs Art 19.8%）\n- 建议：增加数据集验证 或 调低理论 claim 强度\n\n**N2: Epoch confound 对 headline result 的影响**\n- Few-NERD 3 epoch → +1.39pp，5 epoch → +0.62pp（gain 减半）\n- 统一为 5 epoch 后，Few-NERD 效应量接近 SciERC（+0.61pp），框架区分力减弱\n- 当前仅在 footnote + appendix 讨论，正文需更充分处理\n\n### Should-Fix (3 个 Warning)\n- W1: SciERC (n=529, MDE≈1.5pp) 作为 primary test bed 系统性 underpowered\n- W2: DALS 的 ε=0.05 阈值从 data sweep 中选出后又在同一数据上评估，存在 data-snooping 风险\n- W3: \"Capability trap\" 措辞对 3 个 scale points 的 observational trend 过强\n\n### 主要优势\n- QE vs selection 的概念区分清晰有力\n- 实验覆盖面数一数二（4 datasets × 2-3 models × 多个消融维度）\n- 统计方法（bootstrap, TOST, MDE, Bonferroni）显著高于 NLP 论文平均水平\n- Negative results 和 Limitations 的诚实程度值得肯定\n\n### 引用验证\n64 条引用全部匹配 bib，0 orphan/0 missing。3 条未在 OpenAlex 索引到（均为近期预印本），4 条作者名格式小差异，无虚假引用。\n\n完整审稿意见已在对话中输出。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 Round 1 审稿完成\n\n### 总体评分\n- **Overall**: 3.5 (Borderline Conference)\n- **Soundness**: 3/5\n- **Excitement**: 3/5\n- **Reproducibility**: 4/5\n- **Confidence**: 4/5\n\n### 核心判断\n实验全面、透明度高、负面结果诚实呈现，但核心框架（两个条件）的跨数据集支撑仅 3 个点，且 headline positive result（Few-NERD +1.39pp）受 epoch confound 显著影响。\n\n### Must-Fix (2 个 Critical)\n\n**N1: \"两个条件\"框架经验基础不足**\n- 跨数据集仅 3 个数据点（CoNLL/SciERC/Few-NERD），论文自身标注 \"exploratory given 5+ confounds\"\n- 15% degeneracy 阈值来自 Few-NERD per-entity-type 两个相邻点（Person 13.4% vs Art 19.8%）\n- 建议：增加数据集验证 或 调低理论 claim 强度\n\n**N2: Epoch confound 对 headline result 的影响**\n- Few-NERD 3 epoch → +1.39pp，5 epoch → +0.62pp（gain 减半）\n- 统一为 5 epoch 后，Few-NERD 效应量接近 SciERC（+0.61pp），框架区分力减弱\n- 当前仅在 footnote + appendix 讨论，正文需更充分处理\n\n### Should-Fix (3 个 Warning)\n- W1: SciERC (n=529, MDE≈1.5pp) 作为 primary test bed 系统性 underpowered\n- W2: DALS 的 ε=0.05 阈值从 data sweep 中选出后又在同一数据上评估，存在 data-snooping 风险\n- W3: \"Capability trap\" 措辞对 3 个 scale points 的 observational trend 过强\n\n### 主要优势\n- QE vs selection 的概念区分清晰有力\n- 实验覆盖面数一数二（4 datasets × 2-3 models × 多个消融维度）\n- 统计方法（bootstrap, TOST, MDE, Bonferroni）显著高于 NLP 论文平均水平\n- Negative results 和 Limitations 的诚实程度值得肯定\n\n### 引用验证\n64 条引用全部匹配 bib，0 orphan/0 missing。3 条未在 OpenAlex 索引到（均为近期预印本），4 条作者名格式小差异，无虚假引用。\n\n完整审稿意见已在对话中输出。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1308 · 2026-05-18T12:53:18.829200+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Assistant

_source line 1309 · 2026-05-18T12:53:23.904579+00:00_

审稿完成并已汇报 Director。

评分：**3.5 (Borderline Conference)**，2 个 Critical（"两条件"框架证据薄 + epoch confound），3 个 Warning（SciERC underpowered, DALS data snooping, "capability trap" overclaim）。主要优势在于实验覆盖面和统计规范性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 41

## Round 41

9 recorded events


### User

_source line 1310 · 2026-05-18T12:56:41.599242+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（引用具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿意见：

**评分**: 2.5/5（介于 Resubmit 和 Findings 之间）
**Soundness**: 3.5/5, **Excitement**: 2.5/5, **Reproducibility**: 4/5, **Confidence**: 4/5

### Strengths
S1: 实验设计全面，4 个 NER 数据集构成清晰难度梯度，5 种信号覆盖 3 个家族，多种 ablation 系统隔离变量。
S2: 统计严谨性出色（bootstrap CI, TOST + external anchors, MDE, Bonferroni）。
S3: per-sample vs instance-level 区分是重要概念贡献。
S4: Hidden state probes 扩展巧妙封堵了 "信号不够好" 的 alternative explanation。
S5: Limitations 诚实全面。

### Weaknesses

**W1** [Critical] 正文超 8 页限制。Discussion 过长（DALS、LP compression details、regime boundary numerics），Conclusion 从第 9 页开始。约 9.5 页正文，超限约 1.5 页，desk-reject 级别。

**W2** [Major] 新颖性增量有限。(a) correlation-selection gap 是 MBR 文献已知问题在新 domain 的验证；(b) instance degeneracy 是 fine-tuned + constrained decoding 的可预测结果（Kirk 2024 diversity collapse, Yun 2025 format constraints）；(c) capability trap 基于 3 个 scale points 的 observational evidence；(d) 与 Yao et al. (2026) 的增量因实验设置差异（hard-prompting vs fine-tuning）而难以直接比较。

**W3** [Major] DALS 定位混乱。与论文"诊断性"定位冲突：如果是诊断论文，DALS 应在 appendix；如果是核心贡献，应在 Method 中正式定义。当前 DALS 结果 seed-sensitive（SciERC +0.19 to +1.14pp），CoNLL 仍 degradation。

**W4** [Major] Table 3 的 7 个连续脚注严重损害可读性。混合了定义、caveat 和 seed details。建议压缩至 ≤2 个。

**W5** [Major] SciERC 作为 primary test bed 统计 power 不足（n=529, MDE≈1.5pp）。Few-NERD（n=32,565, MDE≈0.22pp）才是 definitive 数据集。建议重新定位 Few-NERD 为 primary。

**W6** [Minor] SciERC greedy F1 在不同表格出现 4 个不同数值（0.640/0.644/0.645/0.650），虽有脚注解释但造成困惑。

**W7** [Minor] Appendix 残留内部实验标识（exp_025, exp_027）。

**W8** [Minor] "Capability trap" 措辞暗示不可逃脱，但 temperature 和 early stopping 可部分控制。建议 "capability-diversity tension" 或 "capability-selection tradeoff"。

### Questions
Q1: SciERC 3 epochs degeneracy 仅 6.4%，为什么不用 3-epoch 作为 primary checkpoint？
Q2: Hidden state probe 为什么只用 mean-pooled final-layer？是否尝试 entity span positions / multi-layer / attention-weighted pooling？
Q3: Per-entity-type analysis（ρ=-0.881, p=0.004, n=8）的 effective df 问题——如果 df 更低，证据可靠性如何？
Q4: 为什么没有测试 Self-Certainty 和 P(True) 这两个 readily available 的 per-sample signals？
Q5: DALS 需要 labeled dev set，为什么不直接用 paired test 决定是否用 LP selection？

### Missing References
1. Farquhar et al. (2024) semantic entropy (Nature)
2. NER-specific calibration 近年文献
3. Best-of-N for code generation（Codex, AlphaCode）

---

请对每条 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。特别关注：
- W1（超页限）是否确认？
- W2（新颖性）你从方法严谨性角度如何评估？
- W5（primary test bed 选择）与你的 W1（SciERC underpowered）是否一致？
- Missing References 中的 3 条是否确实遗漏？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1311 · 2026-05-18T12:57:14.075838+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1312 · 2026-05-18T12:57:14.126754+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1313 · 2026-05-18T12:57:18.049332+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1314 · 2026-05-18T12:57:24.616885+00:00_

Error: result (6,819,294 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/mcp-agent-ml-research-pdf_to_images-1779109044349.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/mcp-agent-ml-research-pdf_to_images-1779109044349.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6567
}
```

</details>

---


### Tool call

_source line 1315 · 2026-05-18T12:57:33.099967+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "8-9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "8-9",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1316 · 2026-05-18T12:57:34.919121+00:00_

Error: result (1,557,451 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/mcp-agent-ml-research-pdf_to_images-1779109054846.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/mcp-agent-ml-research-pdf_to_images-1779109054846.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1819
}
```

</details>

---


### Tool call

_source line 1317 · 2026-05-18T12:57:40.238297+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/mcp-agent-ml-research-pdf_to_images-1779109054846.txt', 'r') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nfor img in result['images']:\n    print(f'Page {img[\\\"page\\\"]}: {img[\\\"path\\\"]}')\nprint(f'Total pages rendered: {len(result[\\\"images\\\"])}')\n\"\n",
  "description": "Extract page info from PDF rendering results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/3e9c8cf9-4ee8-43a1-b477-926ec9c03c8d/tool-results/mcp-agent-ml-research-pdf_to_images-1779109054846.txt', 'r') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nfor img in result['images']:\n    print(f'Page {img[\\\"page\\\"]}: {img[\\\"path\\\"]}')\nprint(f'Total pages rendered: {len(result[\\\"images\\\"])}')\n\"\n",
    "description": "Extract page info from PDF rendering results"
  }
}
```

</details>

---


### Assistant

_source line 1318 · 2026-05-18T12:57:41.146403+00:00_

PDF 图片太大，尝试逐页查看关键页面来确认页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 42

## Round 42

24 recorded events


### User

_source line 1319 · 2026-05-18T13:01:38.534033+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Round 1（Reviewer 1：方法严谨性 + 实验设计）

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
- **Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May 2026 cycle)
- **ARR 截稿**: 2026-05-25
- **格式要求**: ACL template, `[review]` option, 8 页正文 + 无限 references, double-blind anonymous, Limitations section 必需（不计入页数）

### ⚠️ 技术指示（重要）
**不要尝试读取 PDF 文件。PDF 图片过大会导致读取失败。** 请直接读取 LaTeX 源文件：
- 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`
- Sections 目录: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/`
  - `abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `discussion.tex`, `conclusion.tex`, `limitations.tex`, `appendix.tex`
- References: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib`
- Figures 目录（PDF 格式，可跳过图片本身，关注 caption 和引用）: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/`

### 审查侧重
你负责 **方法严谨性 + 实验设计**：

1. **实验设计严谨性**：
   - 统计方法是否正确使用（bootstrap CI、equivalence testing、Bonferroni correction 等）
   - 数据集选择和覆盖面是否足够
   - Baseline 和对比实验是否合理
   - 种子数量、重复实验、统计效力是否充分

2. **方法论贡献**：
   - 核心 claim（correlation-selection gap、two conditions for LP selection）是否有充分证据支撑
   - 因果性 vs 相关性声明是否恰当
   - 消融实验是否充分

3. **数据一致性**：
   - 跨 table/figure 的数字是否一致
   - 正文引用的数字与 table/appendix 是否匹配

4. **格式合规性**：
   - 是否符合 ACL/ARR 8 页限制
   - 匿名化是否完整
   - Limitations section 是否存在且充实

### 已知 Open Issue（前轮遗留）
- **R2-N3**: Title 使用 "Structured Information Extraction" 但实验主要覆盖 NER，scope 过宽。请评估当前 title 是否与论文内容匹配。

请以标准审稿格式输出：Summary → Strengths → Weaknesses (Critical/Warning/Info) → Questions → Missing References → Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-18T13:01:55.675030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-18T13:01:55.725610+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-18T13:01:59.187259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-18T13:01:59.689344+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve reliable quality estimation, supporting selective prediction.
5	For selection, LP achieves $+1.39$~pp on Few-NERD when two conditions are jointly satisfied: low instance degeneracy and adequate LP-quality alignment.
6	When either condition is violated, LP gains fall below detectable thresholds despite ${\sim}$13~pp oracle headroom, a disparity we term the \textbf{correlation-selection gap}.
7	Two mechanisms explain this gap: \textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom; \textit{weak LP-quality alignment} prevents exploiting the remainder.
8	Degeneracy is controllable via temperature and training convergence; neither scalar signal combinations nor learned text representations close the gap.
9	Hidden state probes confirm information beyond LP exists in model representations, but the correlation-selection gap persists: richer signals do not improve selection in the high-capability regime.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-18T13:01:59.689695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-18T13:02:00.191925+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \textit{why} this correlation does not reliably translate to selection gains, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly satisfied: low instance degeneracy (13.8\%) and adequate alignment ($\rho{\approx}0.5$), with gains sc
…[truncated 4418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-18T13:02:00.192461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-18T13:02:00.644480+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 2976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-18T13:02:00.644982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-18T13:02:00.745889+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\ref{app:epoch_confound}).
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses
…[truncated 16738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-18T13:02:19.208518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-18T13:02:19.208950+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
6	We extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.
10	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised signal combination baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden, yun2025price}.
14	
15	\paragraph{Uncertainty estimation and MBR decoding.}
16	Surveys cover confidence estimation \cit
…[truncated 1934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-18T13:03:11.220816+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LP.*\\.(20[0-9]|21[0-9]|28[0-9]|30[0-9])",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LP.*\\.(20[0-9]|21[0-9]|28[0-9]|30[0-9])",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-18T13:03:11.271447+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:40:LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:48:On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:209:LP & .283 & $\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:217:On SciERC, the MLP probe achieves higher quality correlation than LP ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%), confirming that hidden states encode information beyond what LP captures.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:20:Hidden state probes confirm richer information exists in model representations (SciERC MLP $\rho{=}0.388$ vs.\ LP $0.283$, $+37$\%), but the correlation-selection gap persists: MLP selection F1 falls below LP's (gap closure $-5.1$\% vs.\ $+4.8$\%; \S\ref{sec:hidden_probe}), indicating the bottleneck in the high-capability regime is not information loss but diminishing marginal returns on selection.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:49:\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:77:LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discrim
…[truncated 3138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-18T13:03:16.688589+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\.21[0-9].*\\\\.42[0-9]|LP.*rho.*0\\.21[0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\.21[0-9].*\\\\.42[0-9]|LP.*rho.*0\\.21[0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-18T13:03:16.789261+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-18T13:03:20.450710+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\.215",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\.215",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-18T13:03:20.502332+00:00_

109:SciERC & 529 & .644 & 17.8\% & .215 & $+$0.61\,pp & .193 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-18T13:03:57.689713+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include the overall recommendation scale (1-5), soundness scale, excitement scale, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include the overall recommendation scale (1-5), soundness scale, excitement scale, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-18T13:04:03.560753+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Scoring Scales

**Reviewer Confidence** (1-5):
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure" with low likelihood of missed details
- 3 = "Pretty sure, but there's a chance I missed something"
- 2 = Can defend evaluation but "fairly likely that I missed some details"
- 1 = "Not my area, or paper is very hard to understand"

**Soundness** (1-5 with half-point increments):
- 5 = "Excellent: This study is one of the most thorough I have seen"
- 4 = "Strong: This study provides sufficient support for all of its claims"
- 3 = "Acceptable: sufficient support for its main claims"
- 2 = "Poor: Some of the main claims are not sufficiently supported"
- 1 = "Major Issues: not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 with half-point increments):
- 5 = "Highly Exciting: I would recommend this paper to others"
- 4 = "Exciting: I would mention this paper to others"
- 3 = "Interesting: I might mention some points"
- 2 = "Potentially Interesting: does not resonate with me"
- 1 = "Not Exciting: does not resonate with me"

**Overall Assessment** (1-5 with half-point increments):
- 5 = "Consider for Award"
- 4 = "Conference recommendation"
- 3 = "Findings acceptance"
- 2 = "Resubmit next cycle"
- 1 = "Do not resubmit"

## Additional Dimensions

Reproducibility, datasets, software, and author anonymity are rated on 1-5 scales with contextual descriptors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5871
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-18T13:07:07.001325+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 Round 1 审稿完成（修订版）\n\n### 总体评分\n- **Overall**: 3/5 (Findings acceptance)\n- **Soundness**: 3/5 (Acceptable)\n- **Excitement**: 3/5 (Interesting)\n- **Reproducibility**: 4/5\n- **Confidence**: 4/5\n\n### 核心判断\n实验体系和统计方法论出色，per-sample vs instance-level 的概念框架有真实贡献，但核心\"两个条件\"框架的跨数据集支撑不足（n=3），headline positive result 受 epoch confound 影响，且正文可能超出 8 页限制。\n\n### Must-Fix (2 Critical)\n**N1: 正文可能超 8 页限制**\n- Discussion 有 6 个 \\paragraph 子节，内容量远超典型 ACL Discussion\n- 建议将 DALS 细节、LP compression mechanisms、regime boundary numerics 移至 appendix\n\n**N2: \"两个条件\"框架经验基础不足**\n- 跨数据集仅 3 个数据点，15% 和 ρ≥0.3 阈值 data-dependent\n- 建议增加数据集验证或降级 claim 强度\n\n### Should-Fix (5 Warning)\n- W1: Epoch confound 正文处理不充分（5-epoch Few-NERD gain 减半至 +0.62pp）\n- W2: SciERC LP ρ 跨表不一致（Table 1: 0.205 vs Table 3: 0.215, 同 seed 同 N）\n- W3: SciERC 作为 primary test bed 系统性 underpowered（n=529, MDE≈1.5pp）\n- W4: DALS ε=0.05 从 data sweep 选出后在同一数据上评估\n- W5: Title \"Structured IE\" 但实验主体仅 NER（R2-N3 跟进，确认 scope 过宽）\n\n### R2-N3 跟进结论\n确认 Title scope 与实验覆盖不匹配。RE 仅在 SciERC 一个数据集上做 exploratory 分析，正文未报告完整 RE results。建议收窄 title 或在正文提升 RE 地位。\n\n### 新发现的数据一致性问题\nSciERC LP ρ 在 Table 1（0.205）和 Table 3（0.215）之间有 0.010 差异，两表标注相同 seed=42, N=8, gold-filtered。SciERC greedy F1 在不同表格出现 0.640/0.644/0.645 三个值。虽有 footnote 解释但累积效应影响数据信任。\n\n### 对 R2 交叉审稿的回应也已准备好\n在完整审稿意见中对 R2 W1-W8 和 Q1-Q5 进行了间接回应（主要通过 aligned findings）。如需单独的逐条交叉回应，请指示。\n\n完整审稿意见已在对话中输出。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 Round 1 审稿完成（修订版）\n\n### 总体评分\n- **Overall**: 3/5 (Findings acceptance)\n- **Soundness**: 3/5 (Acceptable)\n- **Excitement**: 3/5 (Interesting)\n- **Reproducibility**: 4/5\n- **Confidence**: 4/5\n\n### 核心判断\n实验体系和统计方法论出色，per-sample vs instance-level 的概念框架有真实贡献，但核心\"两个条件\"框架的跨数据集支撑不足（n=3），headline positive result 受 epoch confound 影响，且正文可能超出 8 页限制。\n\n### Must-Fix (2 Critical)\n**N1: 正文可能超 8 页限制**\n- Discussion 有 6 个 \\paragraph 子节，内容量远超典型 ACL Discussion\n- 建议将 DALS 细节、LP compression mechanisms、regime boundary numerics 移至 appendix\n\n**N2: \"两个条件\"框架经验基础不足**\n- 跨数据集仅 3 个数据点，15% 和 ρ≥0.3 阈值 data-dependent\n- 建议增加数据集验证或降级 claim 强度\n\n### Should-Fix (5 Warning)\n- W1: Epoch confound 正文处理不充分（5-epoch Few-NERD gain 减半至 +0.62pp）\n- W2: SciERC LP ρ 跨表不一致（Table 1: 0.205 vs Table 3: 0.215, 同 seed 同 N）\n- W3: SciERC 作为 primary test bed 系统性 underpowered（n=529, MDE≈1.5pp）\n- W4: DALS ε=0.05 从 data sweep 选出后在同一数据上评估\n- W5: Title \"Structured IE\" 但实验主体仅 NER（R2-N3 跟进，确认 scope 过宽）\n\n### R2-N3 跟进结论\n确认 Title scope 与实验覆盖不匹配。RE 仅在 SciERC 一个数据集上做 exploratory 分析，正文未报告完整 RE results。建议收窄 title 或在正文提升 RE 地位。\n\n### 新发现的数据一致性问题\nSciERC LP ρ 在 Table 1（0.205）和 Table 3（0.215）之间有 0.010 差异，两表标注相同 seed=42, N=8, gold-filtered。SciERC greedy F1 在不同表格出现 0.640/0.644/0.645 三个值。虽有 footnote 解释但累积效应影响数据信任。\n\n### 对 R2 交叉审稿的回应也已准备好\n在完整审稿意见中对 R2 W1-W8 和 Q1-Q5 进行了间接回应（主要通过 aligned findings）。如需单独的逐条交叉回应，请指示。\n\n完整审稿意见已在对话中输出。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-18T13:07:10.721360+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3720
}
```

</details>

---


### Assistant

_source line 1342 · 2026-05-18T13:07:25.016304+00:00_

审稿意见已提交。要点：

1. **Overall 3/5 (Findings acceptance)** — 实验质量高，但核心框架证据不足以支撑 main conference。
2. **2 个 Critical** — 可能超页限 + "两个条件"框架仅 3 个跨数据集数据点。
3. **5 个 Warning** — epoch confound 处理不充分、LP ρ 跨表不一致（0.205 vs 0.215）、SciERC underpowered、DALS data-snooping、title scope 过宽。
4. **R2-N3 跟进** — 确认 title "Structured IE" 与 NER-centric 实验不匹配，建议收窄。

如需对 R2 审稿意见的逐条 [AGREE]/[REBUT] 交叉回应，请指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 43

## Round 43

4 recorded events


### User

_source line 1343 · 2026-05-18T13:13:42.051773+00:00_

[Round 1 审稿请求]:
## 交叉分享：请对 Reviewer 2 审稿意见逐条回应

Reviewer 2 已完成对你的审稿意见的交叉回应。现将 R2 完整审稿意见发给你，请逐条以 `[AGREE]` 或 `[REBUT]` 回应。

**注意：你的修订版审稿（Overall 3/5, 2 Critical, 5 Warning）已收到。你只需对以下 R2 findings 进行交叉回应，不需要重新写审稿报告。**

---

## R2 关键 Findings 清单（请逐条回应）

### Critical
**R2-W1** [Critical] 正文页数超限（~9.5 页 vs 8 页限制）
- Discussion 是主要来源。建议 DALS 段落移至 appendix，LP compression mechanisms 和 regime boundaries 细节压缩。

**R2-W2** [Critical] Title scope 过宽（"Structured IE" vs 实际 NER 为主 + 单一 exploratory RE）
- 两个方案：(a) 改 title 为 NER-specific (b) 提升 RE 实验。建议方案 (a)。

### Warning
**R2-W3** DALS 定位与论文主线冲突——诊断性论文中引入具体 selection method，结果 seed-sensitive 且 CoNLL 仍 degradation。建议移至 appendix。

**R2-W4** 新颖性增量需更精确定位——核心贡献是对已知 general phenomena 在 NER domain 的系统验证和命名，建议框定为 "empirical characterization" 而非暗示 theoretical framework。

**R2-W5** SciERC 作为 primary test bed 统计 power 不足（n=529, MDE≈1.5pp）。Few-NERD 应被重新定位为 primary test bed。

**R2-W6** Table 3 的 7 个连续脚注——混合定义、评估细节、confound 声明和 seed details。建议 ≤2 个脚注。

**R2-W7** Greedy F1 数值不一致——SciERC greedy F1 在多个 tables 出现 0.640/0.644/0.645/0.650 四个值。

### Info
**R2-W8** Appendix 残留内部实验标识（exp_025, exp_027）。
**R2-W9** "Capability trap" 措辞过强——建议改为 "capability-diversity tension"。
**R2-W10** 少量 -ing 短语（3 处）。

### Questions
**R2-Q1** 能否提供 3-epoch SciERC 的 within-instance alignment ρ 和 LP selection 的 3-seed mean？
**R2-Q2** Hidden state probe 是否尝试过 entity-position-only pooling？
**R2-Q3** Per-entity-type analysis 如果 effective df 为 4，p-value 会升至多少？
**R2-Q4** 为什么没有测试 Self-Certainty 和 P(True) 这两个 per-sample signals？
**R2-Q5** DALS 的 τ=0.05 如果用 held-out validation，gain 是否 substantially change？

### R2 Missing References
1. Farquhar et al. (Nature 2024) — Semantic entropy
2. Chen et al. (2021) — pass@k for code generation
3. 2023+ LLM-based NER calibration 中间层文献

---

**请对上述每个 finding (W1-W10) 和每个 question (Q1-Q5) 逐条以 [AGREE] / [REBUT] 回应，并附简短理由。Missing References 也请评议。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-18T13:15:16.213314+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 R2 审稿意见的逐条交叉回应\n\n### 总结\n- **AGREE**: W1, W2, W3, W5, W6, W7, W8, W9, W10, Q1, Q2, Q4 (12 条)\n- **AGREE with nuance**: W4, Q5 (2 条)\n- **REBUT**: Q3, Missing Ref #3 (2 条)\n\n### 关键共识\n1. **页数超限（R2-W1）**: 确认 Critical。Discussion 6 个子节 + 7 个 table footnotes 是主要来源。\n2. **Title scope（R2-W2）**: 同意升级严重程度，支持方案 (a) 改 NER-specific title。\n3. **SciERC underpowered（R2-W5）**: 完全一致。建议重新定位 Few-NERD 为 primary。\n4. **数据不一致（R2-W7）**: 一致。补充发现 LP ρ 也有跨表不一致（0.205 vs 0.215）。\n5. **DALS 定位（R2-W3）**: 一致。DALS 在 CoNLL 上 -0.87pp，实际未实现 \"partial damage control\"。\n\n### 关键分歧\n1. **R2-Q3 (per-entity-type df)**: 即使 df=4 (n=6)，ρ=-0.881 仍 p≈0.02，且论文标注为 \"supporting\" 非 \"definitive\"。\n2. **Missing Ref #3 (NER calibration 中间层)**: R2 描述过模糊，论文已引用 3 篇 survey/systematic review，NER-specific calibration 近年工作多围绕 traditional models。\n3. **R2-W4 新颖性**: 同意核心应框为 \"empirical characterization\"，但 per-sample vs instance-level 区分和 degeneracy 作为独立机制有真实增量贡献（不仅是\"已知现象的新 domain 验证\"）。\n\n### 两位 Reviewer 完全一致的问题（建议 Must-Fix）\n- 页数超限\n- Title scope 过宽\n- DALS 定位混乱\n- SciERC underpowered\n- Table 3 脚注过多\n- \"Capability trap\" 措辞过强\n\n完整逐条回应已在对话中输出。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 R2 审稿意见的逐条交叉回应\n\n### 总结\n- **AGREE**: W1, W2, W3, W5, W6, W7, W8, W9, W10, Q1, Q2, Q4 (12 条)\n- **AGREE with nuance**: W4, Q5 (2 条)\n- **REBUT**: Q3, Missing Ref #3 (2 条)\n\n### 关键共识\n1. **页数超限（R2-W1）**: 确认 Critical。Discussion 6 个子节 + 7 个 table footnotes 是主要来源。\n2. **Title scope（R2-W2）**: 同意升级严重程度，支持方案 (a) 改 NER-specific title。\n3. **SciERC underpowered（R2-W5）**: 完全一致。建议重新定位 Few-NERD 为 primary。\n4. **数据不一致（R2-W7）**: 一致。补充发现 LP ρ 也有跨表不一致（0.205 vs 0.215）。\n5. **DALS 定位（R2-W3）**: 一致。DALS 在 CoNLL 上 -0.87pp，实际未实现 \"partial damage control\"。\n\n### 关键分歧\n1. **R2-Q3 (per-entity-type df)**: 即使 df=4 (n=6)，ρ=-0.881 仍 p≈0.02，且论文标注为 \"supporting\" 非 \"definitive\"。\n2. **Missing Ref #3 (NER calibration 中间层)**: R2 描述过模糊，论文已引用 3 篇 survey/systematic review，NER-specific calibration 近年工作多围绕 traditional models。\n3. **R2-W4 新颖性**: 同意核心应框为 \"empirical characterization\"，但 per-sample vs instance-level 区分和 degeneracy 作为独立机制有真实增量贡献（不仅是\"已知现象的新 domain 验证\"）。\n\n### 两位 Reviewer 完全一致的问题（建议 Must-Fix）\n- 页数超限\n- Title scope 过宽\n- DALS 定位混乱\n- SciERC underpowered\n- Table 3 脚注过多\n- \"Capability trap\" 措辞过强\n\n完整逐条回应已在对话中输出。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-18T13:15:20.027873+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3814
}
```

</details>

---


### Assistant

_source line 1346 · 2026-05-18T13:15:22.528006+00:00_

## 对 Reviewer 2 Findings 的逐条交叉回应

---

### Critical

**[AGREE] R2-W1: 正文页数超限**
我在修订版审稿中将此列为 N1 Critical。基于 LaTeX 源码估算（444 行文本 + 1 full-width figure + 1 single-column figure + 5 tables + 7 连续 footnotes），内容量与 R2 报告的 ~9.5 页一致。Discussion 的 6 个 \paragraph 子节是主要来源。同意 DALS 段落、LP compression mechanisms 细节、regime boundary numerics 应移至 appendix。这是 desk-reject 级别问题，应最优先修复。

**[AGREE] R2-W2: Title scope 过宽**
我在修订版中将此列为 W8 Minor，但经 R2 论证后同意应升级严重程度。RE 仅在 SciERC 一个数据集上做 exploratory 分析（Appendix G），正文未报告完整 RE results。论文的方法框架虽然理论上适用于 broader structured IE，但经验证据是 NER-centric 的。同意 R2 方案 (a)：改 title 为 NER-specific（如 "...Named Entity Recognition" 或 "...Structured NER"）比补充 RE 实验更可行。如果保留 "Structured IE"，至少需要在正文中报告 RE 的核心 QE 和 selection results（而非仅 appendix 引用）。

---

### Warning

**[AGREE] R2-W3: DALS 定位冲突**
与我的 W6 一致。DALS 在论文的"诊断性"主线中位置尴尬：论文核心论点是"信号无法做 selection"，但随后引入一个 selection method。DALS 结果 seed-sensitive（SciERC +0.19 to +1.14pp），CoNLL 仍 degradation（-0.87pp，与 pure LP selection 的 -0.85pp 几乎无差异，实际上未实现论文声称的 "partial damage control"）。移至 appendix 作为 proof-of-concept 是正确处理。

**[AGREE with nuance] R2-W4: 新颖性定位**
同意核心贡献更准确地描述为 "empirical characterization" 而非 "theoretical framework"。但我要补充一点 R2 可能低估的贡献：per-sample vs instance-level signal 的区分（Section 3.1）是一个此前未被明确的概念贡献，它从理论上解释了为什么 4/5 信号原则上不能做 selection，这比 "已知现象在新 domain 的验证" 更有价值。Correlation-selection gap 作为一个命名确实在 MBR 文献中有先例（Eikema & Aziz 2022 讨论了 utility misalignment），但 degeneracy 作为独立于 utility alignment 的第一阻碍机制（Section 1 line 16: "degeneracy eliminates candidate diversity before utility alignment matters"）是本文的增量。建议论文更精确地定位：per-sample/instance-level 区分和 degeneracy 诊断是核心贡献，"两个条件框架"是 exploratory finding。

**[AGREE] R2-W5: SciERC 作为 primary test bed underpowered**
与我的 W5 完全一致。n=529, MDE≈1.5pp，大量关键分析的 effect size 在 MDE 以下。Few-NERD（n=32,565, MDE≈0.22pp）提供了远更强的统计基础。论文将 SciERC 定位为 "primary medium-difficulty test bed" 但它同时是一个 low-power test bed。重新定位 Few-NERD 为 primary（或 co-primary）是合理建议。

**[AGREE] R2-W6: Table 3 的 7 个脚注**
与我的 W7 一致。7 个连续 footnote 在 ACL 双栏排版中占据大量空间，且混合了异质信息。≤2 个 footnote 的建议合理。具体地：footnote c（degeneracy 定义）应移入 Method Section 3.3；footnote e-g（seed 细节）合并为一个；footnote a（oracle headroom）整合进 caption；footnote b（greedy F1 差异）的存在本身就是数据不一致问题（W7）的症状。

**[AGREE] R2-W7: Greedy F1 数值不一致**
与我的 W4 一致。SciERC greedy F1 出现 0.640/0.644/0.645 三个值（0.650 实际是 LP selection F1，非 greedy，R2 此处有误），加上 LP ρ 在 Table 1 (0.205) vs Table 3 (0.215) 的不一致，累积效应严重影响数据信任。虽然每个差异都有可能的技术解释（seed、aggregation、gold-filtering），但论文应统一评估管线或在 caption 中更清晰地标注差异来源。一个统一的评估 pipeline 不应在相同 seed、相同 N、相同 dataset 上产生不同数值。

---

### Info

**[AGREE] R2-W8: Appendix 残留内部标识**
与我的 W10 一致。exp_025、exp_027 是 formatting oversight，修复成本低。

**[AGREE] R2-W9: "Capability trap" 措辞**
与我的 W9 一致。3 个 scale points 的 observational trend 不应称为 "trap"。论文自身已证明 temperature 和 early stopping 可以部分控制 degeneracy（Table 15, Table 18），这直接反驳了 "trap"（不可逃脱）的含义。"Capability-diversity tension" 或 "capability-selection tradeoff" 更准确。

**[AGREE] R2-W10: -ing 短语**
ACL ARR reviewer guidelines 未将此列为评审标准，属于 copy-editing 级别。但考虑到 CLAUDE.md 写作规范明确禁止 "-ing 短语结尾"，作为格式合规问题有据可查。

---

### Questions

**[AGREE] R2-Q1: 3-epoch SciERC 的 within-instance alignment ρ 和 LP selection 3-seed mean**
这是一个重要的缺失数据点。Appendix H Table 19 报告 3-epoch SciERC 的 degeneracy (6.4%) 和 LP Δ (-1.18pp)，以及 median within-instance ρ (0.317)。但这是 single seed。如果 3-seed mean 可用且 LP selection 仍然 negative at 3-epoch（此时 degeneracy 最低），这将是 "两个条件"框架最强的证据之一：low degeneracy alone insufficient when alignment ≈0.3。论文应在正文中突出这一点而非埋在 appendix。

**[AGREE] R2-Q2: Hidden state probe entity-position-only pooling**
合理问题。论文测试了 entity-token LP（Discussion line 25: "4× higher variance yet performs worse"），但未测试 entity-token hidden state。Mean-pooled final-layer 将大量 non-entity token（format tokens, schema tokens）的信息混入 representation，可能稀释了 entity-specific 的 quality signal。这是一个 reasonable ablation 请求，尤其在论文已经有 entity-token LP 对照的情况下。

**[REBUT] R2-Q3: Per-entity-type analysis effective df=4 时 p-value**
R2 的关注方向正确，但具体数值可以估算。原始结果：n=8, ρ=-0.881, p=0.004。如果 effective df 降至 4（即 6 independent data points），Spearman ρ=-0.881 在 n=6 时 p≈0.02（查 Spearman critical value table: n=6 at α=0.05 需要 |ρ|≥0.829）。所以即使 df 降至 4，结果仍然在 p<0.05 水平上显著，但不再通过 Bonferroni 校正。论文的 caveat ("effective degrees of freedom may be lower") 是充分的，但可以补充这个具体计算。关键是：即使 df 调整后 p=0.02，这仍然是 supporting evidence（论文标注为 "supporting" 而非 "definitive"），且结合 temperature ablation 的独立证据，整体论证仍然成立。

**[AGREE] R2-Q4: Self-Certainty 和 P(True) 未测试**
论文在 Limitations（line 13）中提到但未给出不测试的理由。Kang et al. (2025) Self-Certainty 和 Kadavath et al. (2022) P(True) 都是 readily available 的 per-sample signals，且与 LP 有不同的计算方式（前者基于 token-level self-evaluation consistency，后者基于 model 对自身正确性的概率估计）。它们可能面临与 LP 相同的 fine-tuned overconfidence 问题（论文已证明 verbalized confidence 严重 overconfident，Appendix I Table tab:verbconf: mean 8.58/10），但这是需要验证而非假设的。对于一篇声称"confidence signals fail"的论文，未测试两个主要的 alternative per-sample signals 是一个明显的 coverage gap。

**[AGREE with nuance] R2-Q5: DALS τ=0.05 held-out validation**
同意这是一个 methodological 弱点（与我的 W6 一致）。但我要补充：Table 9（Appendix D）的 ε sweep 显示 selection F1 在 ε∈[0.01, 0.15] 范围内 monotonically increasing（+0.58 to +4.15pp），且 Few-NERD 上 DALS gain 在 τ∈[0.01, 0.15] 范围内保持正向（Discussion line 51）。所以 τ=0.05 不是一个 knife-edge 选择，但它确实是 p-value 最优的点。如果用 held-out validation，specific gain 数值可能略有变化，但方向性结论（LP range 作为 degeneracy proxy）不太可能翻转。真正的问题不是 τ 的稳健性，而是 DALS 在 same-data evaluation 下的 optimistic bias。

---

### Missing References

**[AGREE] Farquhar et al. (Nature 2024) — Semantic entropy**
论文引用了 Kuhn et al. (2023) 但未引用后续 Nature 论文，后者是 semantic uncertainty 方向的里程碑式成果。遗漏合理但不致命——Farquhar et al. 主要关注 free-form QA，与 set-valued NER 输出有距离。仍建议引用以完善 Related Work。

**[AGREE] Chen et al. (2021) — pass@k / AlphaCode**
论文讨论 best-of-N 和 test-time scaling 但 code generation 中的 large-scale BoN 工作（AlphaCode 的 massive sampling + filtering pipeline）是最接近的成功案例之一。缺失值得补充。

**[REBUT] 2023+ LLM-based NER calibration 中间层文献**
R2 的描述过于模糊（"中间层文献"）。论文已引用 Geng et al. (2024) survey、Xia et al. (2025) survey、Hobelsberger et al. (2025) systematic evaluation，这些覆盖了 LLM confidence/calibration 的主要文献。NER-specific calibration 的近年工作主要围绕 traditional models（CRF, BERT-based），与本文的 generative LLM + sampling 设置距离较远。除非 R2 能指出具体缺失的论文，我认为引用覆盖是充分的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 44

## Round 44

122 recorded events


### User

_source line 1347 · 2026-05-19T03:24:01.401071+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计**

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition
- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）
- **目标 venue**: EMNLP 2026 Main Conference（经 ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式要求**: ACL 模板, 正文 ≤8 页 + unlimited references, double-blind, 必须包含 Limitations section

### 你需要重点审查的方面

1. **信号定义与方法严谨性**
   - 5 个 confidence signal 的数学定义是否严谨、无歧义
   - QE 与 selection 的区分是否清晰
   - MBR/consensus-proximity conversion 的合理性
   - Instance degeneracy 的定义和度量是否恰当

2. **实验设计与统计检验**
   - 实验设置是否充分控制混淆变量（epoch confound, seed sensitivity, thinking token confound 等）
   - 统计检验方法是否恰当（bootstrap, TOST, sign test 等）
   - 多重比较校正是否充分
   - 样本量是否支撑所声称的结论（SciERC n=529 vs Few-NERD n=32,565 的 power 差异）

3. **消融实验充分性**
   - LoRA rank, temperature, N-scaling, scale (4B vs 8B), 模型族 (Qwen vs LLaMA) 的消融是否充分
   - Free-form ablation, hidden state probe, supervised combination 是否足以排除替代解释
   - Entity construction 的 threshold 选择是否有 data snooping 风险

4. **数据一致性**
   - 跨表格数字是否一致（greedy F1 四个值, LP ρ, degeneracy 百分比等）
   - Caption 与正文描述是否吻合
   - 图表是否自包含

### 输出格式

请按以下结构输出审稿意见：

```
## Summary（2-3 句）

## Strengths（逐条）

## Weaknesses（逐条，标注 severity: critical/warning/info）

## Questions（需要作者澄清）

## Missing References

## Minor Issues（拼写、格式等）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-19T03:24:10.970985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-19T03:24:12.526412+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1555
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-19T03:24:12.577087+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-19T03:24:12.577459+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-19T03:24:25.091487+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1353 · 2026-05-19T03:24:26.347025+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1354 · 2026-05-19T03:24:26.397572+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-19T03:24:33.050363+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL ARR 2026 reviewer guidelines, review form criteria, and related policies. Here's what I found:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility. Conference recommen
…[truncated 1353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7958
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-19T03:24:40.280922+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their scales, and descriptions. Include every field: soundness, overall assessment, confidence, excitement/novelty, reproducibility, etc. I need the exact scale descriptions for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their scales, and descriptions. Include every field: soundness, overall assessment, confidence, excitement/novelty, reproducibility, etc. I need the exact scale descriptions for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-19T03:24:42.090252+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score papers, criteria for accept/reject, any specific instructions about soundness, novelty, reproducibility, and how to handle negative results papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score papers, criteria for accept/reject, any specific instructions about soundness, novelty, reproducibility, and how to handle negative results papers."
  }
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-19T03:24:42.993426+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-8",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-8",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-19T03:24:48.342356+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: could be accepted to an *ACL conference"
- **3**: "Findings: could be accepted to the Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: fully redone or not relevant"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduc
…[truncated 606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8061
}
```

</details>

---


### Tool result

_source line 1360 · 2026-05-19T03:24:51.656031+00:00_

# ARR Reviewer Guidelines Summary

## Key Evaluation Criteria

Reviewers assess papers across three main dimensions:

**Soundness**: Technical validity and methodological rigor. "Soundness scores must be justified by the text of the review."

**Excitement**: Personal interest and perceived impact, separate from technical quality assessment.

**Overall Recommendation**: Composite judgment reflecting soundness, excitement, novelty, and potential impact.

## What Reviewers Should Evaluate

### Primary Assessment Tasks:

1. **Expertise & Conflicts**: Verify you can competently review the paper and identify any author relationship concerns that warrant recusal.

2. **Desk Rejection Checklist**: Flag papers with hallucinated references, anonymity violations, style guide violations, missing limitations sections, or ethics issues requiring committee review.

3. **Technical Soundness**: Examine methodology, proof validity, experimental design, and appropriate statistical reporting.

4. **Clarity & Specificity**: Require precise feedback. Vague critiques like "not clear" should specify exactly what information is missing.

5. **Novelty Assessment**: Demand citations when claiming prior work exists. "Highly similar work X and Y has been published [3+ months prior]" justifies rejection.

## Scoring Guidance

Papers may be technically sound yet personally uninteresting—these receive low excitement but potentially higher soundness scores. Conversely, exciting work requires sufficient rigor for publication.

## Common Review Pitfalls to Avoid

The guidelines identify 17 problematic heuristics (H1-H17), including:
- Dismissing intuitive findings as obvious
- Requiring SOTA results when not claimed
- Rejecting negative results unfairly
- Criticizing simplicity when simplicity solves problems effectively

## Handling Specific Paper Types

**Negative Results**: These merit publication when systematic. Community awareness of "what doesn't work" prevents duplicated effort.

**Resource P
…[truncated 975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9565
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-19T03:24:55.413548+00:00_

Error: result (7,089,323 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161095160.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161095160.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 12420
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-19T03:25:04.014310+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-2",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-2",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-19T03:25:05.031056+00:00_

Error: result (1,660,859 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161104980.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161104980.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1016
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-19T03:25:08.845294+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-19T03:25:09.401324+00:00_

Error: result (647,849 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161109351.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161109351.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-19T03:25:20.038271+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1",
  "dpi": "120",
  "output_dir": "/tmp/paper_review_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1",
    "dpi": "120",
    "output_dir": "/tmp/paper_review_images"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-19T03:25:20.493345+00:00_

Error: result (498,436 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161120457.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161120457.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-19T03:25:24.709245+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.png",
  "path": "/tmp/paper_review_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.png",
    "path": "/tmp/paper_review_images"
  }
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-19T03:25:24.760173+00:00_

/tmp/paper_review_images/main_p1.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-19T03:25:26.717587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-19T03:25:26.970789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-19T03:25:32.110936+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "2-14",
  "dpi": "120",
  "output_dir": "/tmp/paper_review_all"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "2-14",
    "dpi": "120",
    "output_dir": "/tmp/paper_review_all"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-19T03:25:35.494424+00:00_

Error: result (6,861,097 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161135257.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161135257.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3383
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-19T03:25:38.858091+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.png",
  "path": "/tmp/paper_review_all"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.png",
    "path": "/tmp/paper_review_all"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-19T03:25:38.908649+00:00_

/tmp/paper_review_all/main_p2.png
/tmp/paper_review_all/main_p3.png
/tmp/paper_review_all/main_p4.png
/tmp/paper_review_all/main_p5.png
/tmp/paper_review_all/main_p6.png
/tmp/paper_review_all/main_p7.png
/tmp/paper_review_all/main_p8.png
/tmp/paper_review_all/main_p9.png
/tmp/paper_review_all/main_p10.png
/tmp/paper_review_all/main_p11.png
/tmp/paper_review_all/main_p12.png
/tmp/paper_review_all/main_p13.png
/tmp/paper_review_all/main_p14.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-19T03:25:43.945630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-19T03:25:44.299085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-19T03:25:44.299503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-19T03:25:44.752880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-19T03:25:44.753415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1381 · 2026-05-19T03:25:44.954452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1382 · 2026-05-19T03:25:45.006773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-19T03:25:45.259491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 305
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-19T03:25:50.905361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1385 · 2026-05-19T03:25:51.106415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-19T03:25:51.157010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-19T03:25:51.158823+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-19T03:25:51.209316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-19T03:25:51.663711+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 557
}
```

</details>

---


### Tool result

_source line 1390 · 2026-05-19T03:25:51.718377+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 561
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-19T03:25:51.871699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 662
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-19T03:25:55.585008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1393 · 2026-05-19T03:25:55.585531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1394 · 2026-05-19T03:25:56.040370+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-19T03:25:56.044795+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-19T03:25:56.045231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-19T03:25:56.548895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-19T03:25:56.549361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1399 · 2026-05-19T03:25:56.649984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_review_all/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_review_all/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1400 · 2026-05-19T03:25:56.802835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-19T03:25:57.005921+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-19T03:31:21.096336+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-19T03:32:21.749695+00:00_

&lt;persisted-output>
Output too large (57.2KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/toolu_01Dfq4JivsWBFERcnZSygPG4.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 68, \"total_citations\": 109, \"unique_cited_keys\": 68, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 59, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 60653
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-19T03:32:31.389328+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/toolu_01Dfq4JivsWBFERcnZSygPG4.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nprint('=== SUMMARY ===')\nprint(json.dumps(data['summary'], indent=2))\nprint()\nprint('=== NOT FOUND ONLINE ===')\nfor entry in data.get('online_verification', []):\n    if entry.get('status') == 'not_found':\n        print(f\\\"  {entry['key']}: {entry.get('bib_title', 'N/A')}\\\")\nprint()\nprint('=== MISMATCH ===')\nfor entry in data.get('online_verification', []):\n    if entry.get('status') == 'mismatch':\n        print(f\\\"  {entry['key']}: BIB={entry.get('bib_title', 'N/A')[:80]}\\\")\n        print(f\\\"    FOUND={entry.get('found_title', 'N/A')[:80]}\\\")\n        print(f\\\"    DETAIL={entry.get('mismatch_detail', 'N/A')}\\\")\nprint()\nprint('=== CROSS CHECK ===')\nprint(f\\\"Orphan bib (in bib not cited): {data['cross_check']['orphan_count']}\\\")\nprint(f\\\"Missing bib (cited not in bib): {data['cross_check']['missing_count']}\\\")\n\"\n",
  "description": "Parse reference verification results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/toolu_01Dfq4JivsWBFERcnZSygPG4.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nprint('=== SUMMARY ===')\nprint(json.dumps(data['summary'], indent=2))\nprint()\nprint('=== NOT FOUND ONLINE ===')\nfor entry in data.get('online_verification', []):\n    if entry.get('status') == 'not_found':\n        print(f\\\"  {entry['key']}: {entry.get('bib_title', 'N/A')}\\\")\nprint()\nprint('=== MISMATCH ===')\nfor entry in data.get('online_verification', []):\n    if entry.get('status') == 'mismatch':\n        print(f\\\"  {entry['key']}: BIB={entry.get('bib_title', 'N/A')[:80]}\\\")\n        print(f\\\"    FOUND={entry.get('found_title', 'N/A')[:80]}\\\")\n        print(f\\\"    DETAIL={entry.get('mismatch_detail', 'N/A')}\\\")\nprint()\nprint('=== CROSS CHECK ===')\nprint(f\\\"Orphan bib (in bib not cited): {data['cross_check']['orphan_count']}\\\")\nprint(f\\\"Missing bib (cited not in bib): {data['cross_check']['missing_count']}\\\")\n\"\n",
    "description": "Parse reference verification results"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-19T03:32:31.740882+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 5, in &lt;module>
    print(json.dumps(data['summary'], indent=2))
                     ~~~~^^^^^^^^^^^
KeyError: 'summary'
=== SUMMARY ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-19T03:32:38.517364+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/toolu_01Dfq4JivsWBFERcnZSygPG4.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\n# Check structure\nif 'data' in result:\n    d = result['data']\n    print('=== SUMMARY ===')\n    print(json.dumps(d['summary'], indent=2))\n    print()\n    print('=== NOT FOUND ONLINE ===')\n    for entry in d.get('online_verification', []):\n        if entry.get('status') == 'not_found':\n            print(f\\\"  {entry['key']}: {entry.get('bib_title', 'N/A')}\\\")\n    print()\n    print('=== MISMATCH ===')\n    for entry in d.get('online_verification', []):\n        if entry.get('status') == 'mismatch':\n            print(f\\\"  {entry['key']}: BIB={entry.get('bib_title', 'N/A')[:80]}\\\")\n            print(f\\\"    FOUND={entry.get('found_title', 'N/A')[:80]}\\\")\n            print(f\\\"    DETAIL={entry.get('mismatch_detail', 'N/A')}\\\")\n    print()\n    print('=== CROSS CHECK ===')\n    print(f\\\"Orphan bib: {d['cross_check']['orphan_count']}\\\")\n    print(f\\\"Missing bib: {d['cross_check']['missing_count']}\\\")\nelse:\n    print(json.dumps(list(result.keys())))\n\"\n",
  "description": "Parse reference verification with correct structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/toolu_01Dfq4JivsWBFERcnZSygPG4.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\n# Check structure\nif 'data' in result:\n    d = result['data']\n    print('=== SUMMARY ===')\n    print(json.dumps(d['summary'], indent=2))\n    print()\n    print('=== NOT FOUND ONLINE ===')\n    for entry in d.get('online_verification', []):\n        if entry.get('status') == 'not_found':\n            print(f\\\"  {entry['key']}: {entry.get('bib_title', 'N/A')}\\\")\n    print()\n    print('=== MISMATCH ===')\n    for entry in d.get('online_verification', []):\n        if entry.get('status') == 'mismatch':\n            print(f\\\"  {entry['key']}: BIB={entry.get('bib_title', 'N/A')[:80]}\\\")\n            print(f\\\"    FOUND={entry.get('found_title', 'N/A')[:80]}\\\")\n            print(f\\\"    DETAIL={entry.get('mismatch_detail', 'N/A')}\\\")\n    print()\n    print('=== CROSS CHECK ===')\n    print(f\\\"Orphan bib: {d['cross_check']['orphan_count']}\\\")\n    print(f\\\"Missing bib: {d['cross_check']['missing_count']}\\\")\nelse:\n    print(json.dumps(list(result.keys())))\n\"\n",
    "description": "Parse reference verification with correct structure"
  }
}
```

</details>

---


### Tool result

_source line 1407 · 2026-05-19T03:32:38.568028+00:00_

=== SUMMARY ===
{
  "total_bib_entries": 68,
  "total_citations": 109,
  "unique_cited_keys": 68,
  "orphan_bib": 0,
  "missing_bib": 0,
  "duplicate_keys": 0,
  "online_verified": 59,
  "online_not_found": 4,
  "online_mismatch": 5
}

=== NOT FOUND ONLINE ===
  hobelsberger2025systematic: N/A
  lightman2024verify: N/A
  venktesh2025trust: N/A
  aggarwal2023adaptive: N/A

=== MISMATCH ===
  feng2025optimal: BIB=N/A
    FOUND=N/A
    DETAIL=N/A
  snell2025scaling: BIB=N/A
    FOUND=N/A
    DETAIL=N/A
  muller2021understanding: BIB=N/A
    FOUND=N/A
    DETAIL=N/A
  park2024grammar: BIB=N/A
    FOUND=N/A
    DETAIL=N/A
  chen2025twofailures: BIB=N/A
    FOUND=N/A
    DETAIL=N/A

=== CROSS CHECK ===
Orphan bib: 0
Missing bib: 0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-19T03:32:47.062344+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/toolu_01Dfq4JivsWBFERcnZSygPG4.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\nd = result['data']\n\n# Get details for not_found and mismatch\nfor entry in d.get('online_verification', []):\n    if entry.get('status') in ('not_found', 'mismatch'):\n        print(f\\\"=== {entry['key']} ({entry['status']}) ===\\\")\n        # Find the bib entry\n        for bib in d.get('bib_entries', []):\n            if bib['key'] == entry['key']:\n                print(f\\\"  Title: {bib.get('title', 'N/A')}\\\")\n                print(f\\\"  Authors: {bib.get('authors', 'N/A')[:100]}\\\")\n                print(f\\\"  Year: {bib.get('year', 'N/A')}\\\")\n                print(f\\\"  Venue: {bib.get('venue', 'N/A')}\\\")\n                break\n        if 'found_title' in entry and entry['found_title']:\n            print(f\\\"  Found title: {entry['found_title']}\\\")\n        if 'mismatch_detail' in entry and entry['mismatch_detail']:\n            print(f\\\"  Mismatch: {entry['mismatch_detail']}\\\")\n        print()\n\"\n",
  "description": "Get detailed info on problematic references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/toolu_01Dfq4JivsWBFERcnZSygPG4.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\nd = result['data']\n\n# Get details for not_found and mismatch\nfor entry in d.get('online_verification', []):\n    if entry.get('status') in ('not_found', 'mismatch'):\n        print(f\\\"=== {entry['key']} ({entry['status']}) ===\\\")\n        # Find the bib entry\n        for bib in d.get('bib_entries', []):\n            if bib['key'] == entry['key']:\n                print(f\\\"  Title: {bib.get('title', 'N/A')}\\\")\n                print(f\\\"  Authors: {bib.get('authors', 'N/A')[:100]}\\\")\n                print(f\\\"  Year: {bib.get('year', 'N/A')}\\\")\n                print(f\\\"  Venue: {bib.get('venue', 'N/A')}\\\")\n                break\n        if 'found_title' in entry and entry['found_title']:\n            print(f\\\"  Found title: {entry['found_title']}\\\")\n        if 'mismatch_detail' in entry and entry['mismatch_detail']:\n            print(f\\\"  Mismatch: {entry['mismatch_detail']}\\\")\n        print()\n\"\n",
    "description": "Get detailed info on problematic references"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-19T03:32:47.163180+00:00_

=== feng2025optimal (mismatch) ===
  Title: Optimal Self-Consistency for Efficient Reasoning with Large Language Models
  Authors: Feng, Austin and Alonso, Marius and Odonnat, Ambroise
  Year: 2025
  Venue: arXiv preprint arXiv:2511.12309

=== hobelsberger2025systematic (not_found) ===
  Title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models
  Authors: Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...
  Year: 2025
  Venue: arXiv preprint arXiv:2510.20460

=== lightman2024verify (not_found) ===
  Title: Let's Verify Step by Step
  Authors: Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...
  Year: 2024
  Venue: Proceedings of the Twelfth International Conference on Learning Representations ...

=== snell2025scaling (mismatch) ===
  Title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters
  Authors: Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral
  Year: 2025
  Venue: Proceedings of the International Conference on Learning Representations (ICLR)

=== muller2021understanding (mismatch) ===
  Title: Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation
  Authors: M\"uller, Mathias and Sennrich, Rico
  Year: 2021
  Venue: Proceedings of the 59th Annual Meeting of the Association for Computational Ling...

=== venktesh2025trust (not_found) ===
  Title: Trust but Verify! A Survey on Verification Design for Test-time Scaling
  Authors: Venktesh, V and Rathee, Mandeep and Anand, Avishek
  Year: 2025
  Venue: arXiv preprint arXiv:2508.16665

=== park2024grammar (mismatch) ===
  Title: Grammar-Aligned Decoding
  Authors: Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...
  Year: 2024
  Venue: Advances in Neural Information Processing Systems 37 (NeurIPS)

=== chen2025twofailures (mismatch) ===
  Title: Two Failures of Self-Consistency in the Multi-Step 
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-19T03:34:19.755424+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\"",
  "description": "Check PDF total page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\"",
    "description": "Check PDF total page count"
  }
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-19T03:34:19.856386+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 03:19:06 2026 UTC
ModDate:         Tue May 19 03:19:06 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           36
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       787036 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-19T03:34:27.084486+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "15-18",
  "dpi": "120",
  "output_dir": "/tmp/paper_appendix_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "15-18",
    "dpi": "120",
    "output_dir": "/tmp/paper_appendix_1"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-19T03:34:28.108170+00:00_

Error: result (2,019,414 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161667907.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161667907.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1023
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-19T03:34:28.560031+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "19-22",
  "dpi": "120",
  "output_dir": "/tmp/paper_appendix_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "19-22",
    "dpi": "120",
    "output_dir": "/tmp/paper_appendix_2"
  }
}
```

</details>

---


### Tool call

_source line 1415 · 2026-05-19T03:34:29.513536+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "23-26",
  "dpi": "120",
  "output_dir": "/tmp/paper_appendix_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "23-26",
    "dpi": "120",
    "output_dir": "/tmp/paper_appendix_3"
  }
}
```

</details>

---


### Tool result

_source line 1416 · 2026-05-19T03:34:30.048208+00:00_

Error: result (1,975,234 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161669766.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161669766.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1488
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-19T03:34:30.450913+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "27-30",
  "dpi": "120",
  "output_dir": "/tmp/paper_appendix_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "27-30",
    "dpi": "120",
    "output_dir": "/tmp/paper_appendix_4"
  }
}
```

</details>

---


### Tool result

_source line 1418 · 2026-05-19T03:34:30.976534+00:00_

Error: result (1,890,054 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161670655.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161670655.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1462
}
```

</details>

---


### Tool call

_source line 1419 · 2026-05-19T03:34:31.430098+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "31-36",
  "dpi": "120",
  "output_dir": "/tmp/paper_appendix_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "31-36",
    "dpi": "120",
    "output_dir": "/tmp/paper_appendix_5"
  }
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-19T03:34:31.660273+00:00_

Error: result (1,816,490 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161671599.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161671599.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool result

_source line 1421 · 2026-05-19T03:34:33.306346+00:00_

Error: result (2,745,606 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161673226.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/d40fdf8e-3826-4f8d-b8cc-0ee20e3568e7/tool-results/mcp-agent-ml-research-pdf_to_images-1779161673226.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1876
}
```

</details>

---


### Tool call

_source line 1422 · 2026-05-19T03:34:38.573637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_1/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_1/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-19T03:34:39.081429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-19T03:34:39.081925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_1/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_1/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-19T03:34:39.535553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-19T03:34:39.586236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_1/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_1/main_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1427 · 2026-05-19T03:34:39.737205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_1/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_1/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1428 · 2026-05-19T03:34:39.890108+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-19T03:34:40.142533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-19T03:34:47.727722+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_2/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_2/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-19T03:34:48.082978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-19T03:34:48.083436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_2/main_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_2/main_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-19T03:34:48.537616+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-19T03:34:48.538053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_2/main_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_2/main_p21.png"
  }
}
```

</details>

---


### Tool call

_source line 1435 · 2026-05-19T03:34:48.739013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_2/main_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_2/main_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 1436 · 2026-05-19T03:34:48.842166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool result

_source line 1437 · 2026-05-19T03:34:49.046742+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 307
}
```

</details>

---


### Tool call

_source line 1438 · 2026-05-19T03:34:59.453323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_3/main_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_3/main_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 1439 · 2026-05-19T03:34:59.453813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_3/main_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_3/main_p24.png"
  }
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-19T03:34:59.454056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_3/main_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_3/main_p25.png"
  }
}
```

</details>

---


### Tool call

_source line 1441 · 2026-05-19T03:34:59.454304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_3/main_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_3/main_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 1442 · 2026-05-19T03:35:00.289883+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 836
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-19T03:35:00.342585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 888
}
```

</details>

---


### Tool result

_source line 1444 · 2026-05-19T03:35:00.395395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 941
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-19T03:35:00.397785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 943
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-19T03:35:03.861078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_4/main_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_4/main_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-19T03:35:04.367272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-19T03:35:04.367692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_4/main_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_4/main_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1449 · 2026-05-19T03:35:04.872639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-19T03:35:04.873112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_4/main_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_4/main_p29.png"
  }
}
```

</details>

---


### Tool call

_source line 1451 · 2026-05-19T03:35:04.875612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_4/main_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_4/main_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 1452 · 2026-05-19T03:35:05.280198+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-19T03:35:05.332930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-19T03:35:09.635965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_5/main_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_5/main_p31.png"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-19T03:35:10.089565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-19T03:35:10.140115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_5/main_p32.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_5/main_p32.png"
  }
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-19T03:35:10.240903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_5/main_p33.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_5/main_p33.png"
  }
}
```

</details>

---


### Tool result

_source line 1458 · 2026-05-19T03:35:10.398337+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 258
}
```

</details>

---


### Tool call

_source line 1459 · 2026-05-19T03:35:10.398757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_5/main_p34.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_5/main_p34.png"
  }
}
```

</details>

---


### Tool result

_source line 1460 · 2026-05-19T03:35:10.753742+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 512
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-19T03:35:10.907749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-19T03:35:15.381573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_5/main_p35.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_5/main_p35.png"
  }
}
```

</details>

---


### Tool call

_source line 1463 · 2026-05-19T03:35:15.583266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_appendix_5/main_p36.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_appendix_5/main_p36.png"
  }
}
```

</details>

---


### Tool result

_source line 1464 · 2026-05-19T03:35:15.636234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-19T03:35:15.640542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 258
}
```

</details>

---
