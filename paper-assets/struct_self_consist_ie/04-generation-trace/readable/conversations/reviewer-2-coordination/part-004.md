# Reviewer 2 coordination — Part 4 of 9

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/dd/dded1175c26e184c6fa2.json)

## Round 40

### Tool result

_source line 1531 · 2026-05-18T06:04:44.449408+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-18T06:04:44.499971+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-18T06:04:44.951699+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-18T06:04:44.952034+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-18T06:04:44.952308+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-18T06:04:45.403593+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-18T06:04:45.454389+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-18T06:04:49.819673+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-18T06:04:50.380958+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 561
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-18T06:04:50.381474+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-18T06:04:50.835982+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1542 · 2026-05-18T06:04:50.886752+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1543 · 2026-05-18T06:04:51.188315+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-18T06:04:51.188721+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-18T06:04:51.239745+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-18T06:04:56.866358+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1547 · 2026-05-18T06:04:57.117584+00:00_

File content (35137 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-18T06:04:59.927372+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1549 · 2026-05-18T06:05:00.179342+00:00_

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
…[truncated 36657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-18T06:05:04.718386+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1551 · 2026-05-18T06:05:04.969859+00:00_

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
…[truncated 31220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-18T06:05:09.284715+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1553 · 2026-05-18T06:05:09.285426+00:00_

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
…[truncated 24330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-18T06:05:19.133035+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1555 · 2026-05-18T06:05:19.133469+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-18T06:05:19.535421+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: all scoring criteria, what constitutes a good review, specific instructions on how to evaluate novelty, soundness, reproducibility, and other dimensions. Include any rubrics or detailed descriptions of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: all scoring criteria, what constitutes a good review, specific instructions on how to evaluate novelty, soundness, reproducibility, and other dimensions. Include any rubrics or detailed descriptions of each score level."
  }
}
```

</details>

---


### Tool result

_source line 1557 · 2026-05-18T06:05:36.202940+00:00_

# ARR Reviewer Guidelines: Scoring Criteria and Evaluation Standards

## Three Core Scoring Dimensions

ARR uses three distinct scores (as of February 2025):

1. **Soundness**: Technical validity and methodological rigor
2. **Excitement**: Personal interest and engagement with the work
3. **Overall Recommendation**: Composite assessment for venue suitability

## Soundness Score Requirements

The soundness rating must align with your review text. As the guidelines state: "The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it."

Low soundness ratings require explicit justification through identified technical problems.

## Excitement vs. Soundness Distinction

Excitement reflects subjective preference and operates independently from soundness assessment. You may rate a technically sound paper low on excitement if it lacks personal interest, while maintaining consistency between soundness scores and identified technical issues.

## Overall Recommendation Scope

This composite score should reflect soundness, excitement, novelty, and potential impact. The guidelines note that papers need sufficient soundness for acceptance but acknowledge that "you may consider a paper worthy of the main conference even if you personally are not excited about it."

## Key Evaluation Principles

**Adjust expectations before critiquing**: Read papers twice—skimming to assess research questions, then in-depth analysis. This prevents bias from prototype papers in your subfield.

**Specificity requirement**: Replace vague criticisms ("X is unclear") with concrete observations ("Y and Z are missing from the description of X").

## Common Review Pitfalls (Heuristic Checklist)

The guidelines identify problematic reasoning patterns to avoid:

- **H1-H2**: Dismissing results as "obvious" or contradicting your ex
…[truncated 1995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 16667
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-18T06:05:41.023588+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1559 · 2026-05-18T06:05:44.455658+00:00_

Error: result (6,934,562 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3432
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-18T06:05:49.379398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nprint('Keys:', list(result.keys()))\nprint('Pages:', len(result.get('pages', [])))\nfor p in result.get('pages', []):\n    print(f'Page {p[\\\"page_number\\\"]}: {p[\\\"image_path\\\"]}')\n\"\n",
  "description": "Parse PDF-to-images output to find page image paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nprint('Keys:', list(result.keys()))\nprint('Pages:', len(result.get('pages', [])))\nfor p in result.get('pages', []):\n    print(f'Page {p[\\\"page_number\\\"]}: {p[\\\"image_path\\\"]}')\n\"\n",
    "description": "Parse PDF-to-images output to find page image paths"
  }
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-18T06:05:50.084754+00:00_

Keys: ['success', 'data', 'error', 'metadata']
Pages: 0
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-18T06:05:55.461316+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nprint('Top-level keys:', list(result.keys()))\nd = result.get('data', {})\nprint('Data keys:', list(d.keys()))\npages = d.get('pages', [])\nprint('Num pages:', len(pages))\nfor p in pages:\n    print(f'Page {p.get(\\\"page_number\\\")}: {p.get(\\\"image_path\\\", \\\"N/A\\\")[:100]}')\n\"\n",
  "description": "Parse PDF-to-images JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nprint('Top-level keys:', list(result.keys()))\nd = result.get('data', {})\nprint('Data keys:', list(d.keys()))\npages = d.get('pages', [])\nprint('Num pages:', len(pages))\nfor p in pages:\n    print(f'Page {p.get(\\\"page_number\\\")}: {p.get(\\\"image_path\\\", \\\"N/A\\\")[:100]}')\n\"\n",
    "description": "Parse PDF-to-images JSON structure"
  }
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-18T06:05:55.764718+00:00_

Top-level keys: ['success', 'data', 'error', 'metadata']
Data keys: ['images', 'total_pages', 'rendered_pages', 'dpi', 'output_dir']
Num pages: 0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-18T06:06:00.837701+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nd = result['data']\nprint('total_pages:', d.get('total_pages'))\nprint('rendered_pages:', d.get('rendered_pages'))\nprint('dpi:', d.get('dpi'))\nprint('output_dir:', d.get('output_dir'))\nimages = d.get('images', [])\nprint('Num images:', len(images))\nfor img in images[:3]:\n    print('  page:', img.get('page_number'), 'path:', img.get('image_path', 'N/A')[:120])\n\"\n",
  "description": "Get PDF page info and image paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nd = result['data']\nprint('total_pages:', d.get('total_pages'))\nprint('rendered_pages:', d.get('rendered_pages'))\nprint('dpi:', d.get('dpi'))\nprint('output_dir:', d.get('output_dir'))\nimages = d.get('images', [])\nprint('Num images:', len(images))\nfor img in images[:3]:\n    print('  page:', img.get('page_number'), 'path:', img.get('image_path', 'N/A')[:120])\n\"\n",
    "description": "Get PDF page info and image paths"
  }
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-18T06:06:00.988788+00:00_

total_pages: 29
rendered_pages: 10
dpi: 150
output_dir: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images
Num images: 10
  page: None path: N/A
  page: None path: N/A
  page: None path: N/A

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-18T06:06:06.721406+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nimages = result['data']['images']\nfor i, img in enumerate(images[:3]):\n    print(f'Image {i}: keys={list(img.keys())}')\n    for k, v in img.items():\n        if k != 'base64':\n            print(f'  {k}: {str(v)[:100]}')\n        else:\n            print(f'  base64: (length {len(str(v))})')\n\"\n",
  "description": "Inspect image structure to find paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/53bb0d46-1afc-4fea-afef-fc85e7d6fef7/tool-results/mcp-agent-ml-research-pdf_to_images-1779084343981.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nimages = result['data']['images']\nfor i, img in enumerate(images[:3]):\n    print(f'Image {i}: keys={list(img.keys())}')\n    for k, v in img.items():\n        if k != 'base64':\n            print(f'  {k}: {str(v)[:100]}')\n        else:\n            print(f'  base64: (length {len(str(v))})')\n\"\n",
    "description": "Inspect image structure to find paths"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-18T06:06:06.822178+00:00_

Image 0: keys=['page', 'path', 'base64', 'width', 'height', 'size_kb']
  page: 1
  path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_imag
  base64: (length 634856)
  width: 1241
  height: 1754
  size_kb: 465.0
Image 1: keys=['page', 'path', 'base64', 'width', 'height', 'size_kb']
  page: 2
  path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_imag
  base64: (length 559620)
  width: 1241
  height: 1754
  size_kb: 409.9
Image 2: keys=['page', 'path', 'base64', 'width', 'height', 'size_kb']
  page: 3
  path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_imag
  base64: (length 706036)
  width: 1241
  height: 1754
  size_kb: 517.1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-18T06:06:10.899675+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "_pdf_images/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "_pdf_images/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-18T06:06:11.000426+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-18T06:06:14.822293+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/ 2>/dev/null | head -20",
  "description": "List PDF image output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/ 2>/dev/null | head -20",
    "description": "List PDF image output files"
  }
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-18T06:06:15.023781+00:00_

main_p1.png
main_p10.png
main_p11.png
main_p12.png
main_p13.png
main_p14.png
main_p15.png
main_p16.png
main_p17.png
main_p18.png
main_p19.png
main_p2.png
main_p20.png
main_p21.png
main_p22.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1572 · 2026-05-18T06:06:18.140974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1573 · 2026-05-18T06:06:18.744160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1574 · 2026-05-18T06:06:19.752327+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1611
}
```

</details>

---


### Tool result

_source line 1575 · 2026-05-18T06:06:19.814914+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1070
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-18T06:06:20.035304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1577 · 2026-05-18T06:06:20.035726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1578 · 2026-05-18T06:06:22.405319+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2370
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-18T06:06:22.641702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2605
}
```

</details>

---


### Tool call

_source line 1580 · 2026-05-18T06:08:05.689890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1581 · 2026-05-18T06:08:05.690365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1582 · 2026-05-18T06:08:06.745681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-18T06:08:06.746638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-18T06:10:06.654163+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review)\n**审查侧重**: Novelty + Completeness\n\n---\n\n## Paper Summary\n\n本文研究了 LLM-based NER 中 confidence signals 用于 quality estimation (QE) 与 sample selection 之间的脱节现象。作者在四个 NER benchmark 上评估了五种 confidence signals（四种 instance-level：Soft Jaccard, Voting Confidence, Fleiss' κ, Exact Match；一种 per-sample：Log-Probability），使用 3B–8B 模型。核心发现是 \"correlation-selection gap\"：所有 signals 均能实现可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但没有 signal 能稳定地超越 greedy decoding 进行 sample selection。两个机制解释了这一 gap：(1) instance degeneracy（14–59% 的 instances 所有 samples 产出相同 F1）；(2) weak LP-quality alignment。LP 仅在两个条件同时满足时实现显著 selection gain（Few-NERD: +1.36 pp, p<0.001）。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5 (Findings borderline)\n**一句话总结**: 实验设计严谨、文档详尽的 empirical study，但 conceptual contribution 有限——核心发现（instance-level signals 无法 rank candidates）可从第一性原理推导，\"two necessary conditions\" 框架是描述性的而非预测性的，且任务/模型覆盖面不足以支撑 title 中 \"Structured Information Extraction\" 的泛化声明。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论严谨（bootstrap CI, TOST, power analysis），但核心 claim 的泛化性超出了证据范围（3 datasets 推导 threshold，仅 NER+exploratory RE 支撑 \"structured IE\" 声明） |\n| Excitement | 2/5 | 有用的 negative result，但 conceptual depth 有限；gap 的解释基本可从 signal 定义预测（4/5 signals 是 instance-level → 无法 rank candidates），LP 压缩是细粒度 empirical finding 但非 surprising insight；没有提出有效的解决方案 |\n| Reproducibility | 4/5 | 训练配置（Table A.1）、prompt template、constrained decoding 细节均充分；code/data 承诺 release；seed stability 有验证 |\n| Confidence | 4/5 | 我仔细阅读了全文和附录，熟悉 self-consistency、MBR decoding、confidence estimation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心概念 \"correlation-selection gap\" 的新颖性不足**\n- 具体位置：§1 (Introduction, lines 5-8), §4.3, §5 (Discussion)\n- 问题：论文的核心 framing 是 \"quality estimation 不等于 selection\"，但这一 gap 的主要原因——4/5 signals 是 instance-level aggregates，by definition 无法区分同一 instance 内的 candidates——是从 signal 定义可直接推导的（论文自身在 §3.1 第 7 行承认 \"This distinction is consequential for selection\"）。真正需要解释的只有 LP（唯一 per-sample signal）为何失败，而 LP 失败的解释（compression + degeneracy）是描述性的 empirical observation，不构成 deep conceptual insight。\n- 与已有工作的区分度：\"Two necessary conditions\" 框架（degeneracy <15% + alignment ρ≳0.3）来自仅 3 个 datasets 的 cross-dataset gradient（§4.4, exploratory, 作者自己标注 \"5+ confounds\"），辅以 Few-NERD 8 个 entity types 的 within-dataset 分析（effective df may be lower，作者自己承认）。作为 generalization framework 证据极薄。与 Yao et al. (2026) 的增量主要是 \"correlation → selection 的 failure mode diagnosis\"，但诊断的核心工具（instance-level vs. per-sample 的区分）是 definitional，不是 discovered。\n- 为什么影响接收：EMNLP 要求 sufficient intellectual contribution。文中最 novel 的 finding 是 LP compression 的详细刻画（§5, Appendix F），但这被包装在一个看起来更大但实际上较浅的 \"correlation-selection gap\" 框架中。\n- 建议修改方向：(1) 重新 frame 核心贡献为 LP compression 的诊断和 fine-tuned model 在 structured output 上的 diversity collapse，而非 instance-level signals 无法 select（后者不需要实验证明）；(2) 提供 LP compression 的理论解释（不只是描述四种机制），例如分析 constrained decoding 对 entropy 的影响。\n\n**N2** [critical] **任务覆盖面远不足以支撑论文声明的泛化范围**\n- 具体位置：Title (\"Structured Information Extraction\"), Abstract line 1 (\"named entity recognition\"), §1 contributions\n- 问题：Title 和多处 claim 使用 \"Structured Information Extraction\"，但实验仅覆盖 NER（4 benchmarks）+ exploratory RE（仅 SciERC 一个 benchmark，且被标注为 \"preliminary\"）。结构化 IE 还包括 event extraction、slot filling、open IE、nested NER、discontinuous NER 等。论文没有在任何 non-NER/non-RE 任务上验证 \"correlation-selection gap\" 是否存在。\n- 为什么影响接收：论文的核心 claim 是关于 structured outputs 与 self-consistency 的 fundamental tension，但 NER 是最简单的 structured IE 形式。更复杂的 structured tasks（event extraction with argument roles, nested structures）可能有完全不同的 degeneracy 和 alignment 特征。\n- 建议修改方向：(1) 将 title 和 claims 缩窄为 \"Named Entity Recognition\" 或 \"Entity-level Information Extraction\"；或者 (2) 增加至少一个非 NER 的 structured IE 任务的完整实验（不仅是 appendix exploratory）。\n\n**N3** [critical] **模型规模范围不足以支撑结论的实用价值**\n- 具体位置：§4.1 \"two 8B models with a 4B ablation\", §1 line 25 \"behavior at 70B+ scales remains an open question\", Limitations\n- 问题：所有实验在 3B–8B 范围内。当前生产 NER 系统越来越多使用 70B+ 模型或 closed-source APIs（GPT-4, Claude）。论文声称的 \"practical guidelines\"（§5 \"Practical guidelines\"）在实际部署场景中的适用性未知。关键机制——instance degeneracy 和 LP compression——可能在更大模型上表现完全不同：更大模型通常有更好的 calibration、更高的 output diversity、更强的 LP-quality alignment。\n- 为什么影响接收：论文的 framing 是面向 practitioners 的 negative result + practical guidelines，但 guidelines 的适用范围被限制在一个相对边缘的部署场景（fine-tuned 4B-8B models with LoRA）。这不是 \"a limitation\" 而是影响论文核心价值定位的问题。\n- 建议修改方向：至少在一个 70B scale（Qwen2.5-72B 或 LLaMA-3.1-70B，zero-shot or few-shot，不需要 fine-tune）上验证 degeneracy 和 LP compression 是否仍然存在；或者明确重新定位论文为 \"fine-tuned small LMs for NER\" 的 scope。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **\"Two necessary conditions\" 框架缺乏预测力**\n- 具体位置：§4.4 (cross-dataset gradient), §5 (Practical guidelines)\n- 问题：Practical guidelines 要求 \"先在 labeled dev set 上估计 degeneracy 和 alignment\"，然后决定是否使用 LP selection。但如果你有 labeled dev set，就可以直接评估 LP selection 效果本身，不需要中间代理指标。框架的实用价值应该是 *a priori* 预测（无需标注数据），但当前形式等价于 \"在标注数据上跑一次看看\"。\n- 建议：探索无监督代理指标（如 output diversity 统计、LP range 分布），使框架能在无标注场景下提供 guidance。\n\n**W2** [warning] **缺少重要 baseline signals**\n- 具体位置：§3.2, §4.5 (Robustness), Appendix L (Verbalized Confidence)\n- 问题：(1) 没有测试 P(True)（Kadavath et al., 2022）或 Self-Certainty（Kang et al., 2025）作为 per-sample selection signal——VerbConf (Appendix L) 有测试但仅用了 raw 1-10 分数，没有 calibration；(2) 没有 hidden-state-based signals（论文在 limitations 中承认但作为 \"future work\" 处理，这对于声称 \"five signals studied\" 足以得出结论是不够的）；(3) 论文的 supervised verifier baseline（§4.5）仅使用五种 unsupervised signals 作为 features，这不是一个 fair test of \"whether learned approaches could help\"——应至少尝试用 hidden states 或 entity embeddings。\n- 建议：至少增加 Self-Certainty（首 token probability）作为额外 per-sample signal 进行完整评估。\n\n**W3** [warning] **Few-NERD 的训练设置差异构成 confound**\n- 具体位置：§4.1 line 15 \"except Few-NERD models which use 3 epochs\", Table E.8, Appendix N\n- 问题：Few-NERD 是唯一显示 LP selection success 的 dataset，也是唯一使用 3 epochs（vs. 5 epochs for others）的 dataset。Appendix N 的 epoch confound analysis 显示 5 epochs 时 LP gains 减半（+1.37 → +0.62 pp）。这意味着 Few-NERD 的 positive result 至少部分归因于训练设置差异，而非纯粹的 task structure。\n- 正文中 §4.4 和 §5 将 Few-NERD 的 success 主要归因于 \"low degeneracy + strong alignment\"（task properties），但 epoch confound 在正文的叙述中没有被充分强调。这可能导致 reader 过度概括 \"Few-NERD 类型的 tasks 天然适合 LP selection\"。\n- 建议：在正文 §4.4 明确讨论 epoch confound 对 Few-NERD positive result 的贡献程度，并在其他 dataset 上用 3 epochs 复现实验以解耦 epoch 效应和 task 效应。\n\n**W4** [warning] **RE extension 过于 preliminary 但在正文中引用频繁**\n- 具体位置：§1 line 26, §5 lines 6/21, Appendices G-I\n- 问题：RE 仅在 SciERC 一个 benchmark 上用一个 model 测试（§G 开头 \"Qwen3-8B unless noted\"），且被标注为 \"preliminary\" / \"single-dataset observation\"，但正文中多处引用 RE 结果来 support claims（如 §5 的 LP compression 讨论引用 RE free-form 结果）。Single-benchmark RE 结果不应作为支撑 general claims 的证据。\n- 建议：要么在 RE 上增加更多 benchmarks（ACE05, TACRED, DocRED），要么将 RE 引用严格限制在 appendix 且不作为正文 claims 的 evidence。\n\n---\n\n## 小问题（不影响接收）\n\n1. Abstract 较 dense：第 4-7 句连续出现大量数字（ρ, AUROC, pp, p-value），读起来像 results summary 而非 engaging abstract。建议精简数字，突出 conceptual contribution。\n2. 不同 table 之间的 greedy F1 基线略有不一致（Table 2: 0.645; Table 3: 0.644; N-scaling table: 0.640），虽然脚注解释了原因（seed 和 aggregation 差异），但仍可能造成 confusion。\n3. 统计检验方法多样（sign test, bootstrap, Fisher combined, TOST, permutation），但何时使用哪种方法的选择标准不够明确。建议在 Method 中统一说明 statistical testing strategy。\n4. §3.2 的 Fleiss' κ adaptation 到 entity sets 是 novel 的，但缺少对这种 adaptation 的 validity 论证——κ 假设 raters 独立，而同一 LM 的 samples 显然不完全独立（论文仅在 Appendix A 提供了 mild negative dependence 的 empirical check，但没有理论论证）。\n5. Reference verification: 3 entries not found in OpenAlex（hobelsberger2025systematic, lightman2024verify, venktesh2025trust）——请核实这些引用的准确性。lightman2024verify 应为 ICLR 2024 paper，OpenAlex 可能未收录；其余两篇为 arXiv preprints，需确认 title/year 正确。\n6. Table 1 caption 提到 \"RE results in Appendix D\" 但 Appendix D 的 section label 是 \"Bootstrap CI for Signal Comparisons\"——请检查 cross-reference 一致性（注：可能是我对 appendix lettering 的理解有误，但作者应确认）。\n\n---\n\n## 主要优势\n\n1. **实验设计的系统性和严谨度**: 5 signals × 4 datasets × 3 model families × 多个 temperature/N/epoch configurations，覆盖了大量潜在 confounds。Statistical methodology（bootstrap CI, TOST equivalence testing, power analysis with MDE）远超平均水平。\n2. **QE 与 selection 的清晰分离**: 这是一个有用的 methodological contribution。许多先前工作将两者混为一谈，本文明确区分并展示了它们可以 decouple。\n3. **透明的 limitations 讨论**: 论文对每一个 confound（epoch, thinking token, ε threshold, LoRA rank-capacity conflation）都提供了详细分析，这种 transparency 难能可贵。\n4. **附录极其详尽**: 21 页 appendix 覆盖了几乎所有可能的 reviewer concern（calibration, free-form ablation, OOD, verbalized confidence, per-type analysis, N-scaling, epoch confound, etc.）。\n5. **Few-NERD 的 positive result 是 well-powered**: n=32,565, CI [+1.18, +1.53]，这是 convincing evidence that LP selection CAN work under specific conditions。\n\n---\n\n## Missing References / 遗漏的相关工作\n\n1. **Selective Prediction for NER**: 论文引用了 Kuleshov & Liang (2015) 但缺少更多 selective prediction 文献，特别是 Geifman & El-Yaniv (2017) \"Selective Classification for Deep Neural Networks\" 和 Varshney et al. (2022) \"Investigating Selective Prediction Approaches Across Several Tasks in IID, OOD, and Adversarial Settings\"——这些直接与 QE-based abstention 相关。\n2. **LLM-based NER 的更多 baselines**: Xie et al. (2023) \"DecomposedPrompt\" for structured NER; Wang et al. (2023) \"GPT-NER\" 等 LLM-NER 工作应在 Related Work §2.3 提及。\n3. **Structured MBR 的更多文献**: 除了 Eikema et al. (2025) Structure-Conditional MBR，还应引用 Cheng & Vlachos (2023) \"Faster Minimum Bayes Risk Decoding with Confidence-based Pruning\" 和相关 structured decoding 工作。\n\n---\n\n## Verdict\n\n这是一篇实验工作极其严谨的论文，附录中的分析深度令人印象深刻。但核心 intellectual contribution 有限：(1) \"instance-level signals can't rank candidates\" 是 definitional 而非 discovered；(2) LP compression 的诊断有价值但被过度包装在一个 shallow \"gap\" 框架中；(3) 任务和模型覆盖面不足以支撑 title-level claims。建议作者要么缩窄 scope 并深化对 LP compression 的理论理解，要么扩展到更多 tasks/scales 以 empirically 支撑 general claims。\n\n当前形式可能适合 Findings，距 main conference 还有距离。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review)\n**审查侧重**: Novelty + Completeness\n\n---\n\n## Paper Summary\n\n本文研究了 LLM-based NER 中 confidence signals 用于 quality estimation (QE) 与 sample selection 之间的脱节现象。作者在四个 NER benchmark 上评估了五种 confidence signals（四种 instance-level：Soft Jaccard, Voting Confidence, Fleiss' κ, Exact Match；一种 per-sample：Log-Probability），使用 3B–8B 模型。核心发现是 \"correlation-selection gap\"：所有 signals 均能实现可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但没有 signal 能稳定地超越 greedy decoding 进行 sample selection。两个机制解释了这一 gap：(1) instance degeneracy（14–59% 的 instances 所有 samples 产出相同 F1）；(2) weak LP-quality alignment。LP 仅在两个条件同时满足时实现显著 selection gain（Few-NERD: +1.36 pp, p<0.001）。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5 (Findings borderline)\n**一句话总结**: 实验设计严谨、文档详尽的 empirical study，但 conceptual contribution 有限——核心发现（instance-level signals 无法 rank candidates）可从第一性原理推导，\"two necessary conditions\" 框架是描述性的而非预测性的，且任务/模型覆盖面不足以支撑 title 中 \"Structured Information Extraction\" 的泛化声明。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论严谨（bootstrap CI, TOST, power analysis），但核心 claim 的泛化性超出了证据范围（3 datasets 推导 threshold，仅 NER+exploratory RE 支撑 \"structured IE\" 声明） |\n| Excitement | 2/5 | 有用的 negative result，但 conceptual depth 有限；gap 的解释基本可从 signal 定义预测（4/5 signals 是 instance-level → 无法 rank candidates），LP 压缩是细粒度 empirical finding 但非 surprising insight；没有提出有效的解决方案 |\n| Reproducibility | 4/5 | 训练配置（Table A.1）、prompt template、constrained decoding 细节均充分；code/data 承诺 release；seed stability 有验证 |\n| Confidence | 4/5 | 我仔细阅读了全文和附录，熟悉 self-consistency、MBR decoding、confidence estimation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心概念 \"correlation-selection gap\" 的新颖性不足**\n- 具体位置：§1 (Introduction, lines 5-8), §4.3, §5 (Discussion)\n- 问题：论文的核心 framing 是 \"quality estimation 不等于 selection\"，但这一 gap 的主要原因——4/5 signals 是 instance-level aggregates，by definition 无法区分同一 instance 内的 candidates——是从 signal 定义可直接推导的（论文自身在 §3.1 第 7 行承认 \"This distinction is consequential for selection\"）。真正需要解释的只有 LP（唯一 per-sample signal）为何失败，而 LP 失败的解释（compression + degeneracy）是描述性的 empirical observation，不构成 deep conceptual insight。\n- 与已有工作的区分度：\"Two necessary conditions\" 框架（degeneracy <15% + alignment ρ≳0.3）来自仅 3 个 datasets 的 cross-dataset gradient（§4.4, exploratory, 作者自己标注 \"5+ confounds\"），辅以 Few-NERD 8 个 entity types 的 within-dataset 分析（effective df may be lower，作者自己承认）。作为 generalization framework 证据极薄。与 Yao et al. (2026) 的增量主要是 \"correlation → selection 的 failure mode diagnosis\"，但诊断的核心工具（instance-level vs. per-sample 的区分）是 definitional，不是 discovered。\n- 为什么影响接收：EMNLP 要求 sufficient intellectual contribution。文中最 novel 的 finding 是 LP compression 的详细刻画（§5, Appendix F），但这被包装在一个看起来更大但实际上较浅的 \"correlation-selection gap\" 框架中。\n- 建议修改方向：(1) 重新 frame 核心贡献为 LP compression 的诊断和 fine-tuned model 在 structured output 上的 diversity collapse，而非 instance-level signals 无法 select（后者不需要实验证明）；(2) 提供 LP compression 的理论解释（不只是描述四种机制），例如分析 constrained decoding 对 entropy 的影响。\n\n**N2** [critical] **任务覆盖面远不足以支撑论文声明的泛化范围**\n- 具体位置：Title (\"Structured Information Extraction\"), Abstract line 1 (\"named entity recognition\"), §1 contributions\n- 问题：Title 和多处 claim 使用 \"Structured Information Extraction\"，但实验仅覆盖 NER（4 benchmarks）+ exploratory RE（仅 SciERC 一个 benchmark，且被标注为 \"preliminary\"）。结构化 IE 还包括 event extraction、slot filling、open IE、nested NER、discontinuous NER 等。论文没有在任何 non-NER/non-RE 任务上验证 \"correlation-selection gap\" 是否存在。\n- 为什么影响接收：论文的核心 claim 是关于 structured outputs 与 self-consistency 的 fundamental tension，但 NER 是最简单的 structured IE 形式。更复杂的 structured tasks（event extraction with argument roles, nested structures）可能有完全不同的 degeneracy 和 alignment 特征。\n- 建议修改方向：(1) 将 title 和 claims 缩窄为 \"Named Entity Recognition\" 或 \"Entity-level Information Extraction\"；或者 (2) 增加至少一个非 NER 的 structured IE 任务的完整实验（不仅是 appendix exploratory）。\n\n**N3** [critical] **模型规模范围不足以支撑结论的实用价值**\n- 具体位置：§4.1 \"two 8B models with a 4B ablation\", §1 line 25 \"behavior at 70B+ scales remains an open question\", Limitations\n- 问题：所有实验在 3B–8B 范围内。当前生产 NER 系统越来越多使用 70B+ 模型或 closed-source APIs（GPT-4, Claude）。论文声称的 \"practical guidelines\"（§5 \"Practical guidelines\"）在实际部署场景中的适用性未知。关键机制——instance degeneracy 和 LP compression——可能在更大模型上表现完全不同：更大模型通常有更好的 calibration、更高的 output diversity、更强的 LP-quality alignment。\n- 为什么影响接收：论文的 framing 是面向 practitioners 的 negative result + practical guidelines，但 guidelines 的适用范围被限制在一个相对边缘的部署场景（fine-tuned 4B-8B models with LoRA）。这不是 \"a limitation\" 而是影响论文核心价值定位的问题。\n- 建议修改方向：至少在一个 70B scale（Qwen2.5-72B 或 LLaMA-3.1-70B，zero-shot or few-shot，不需要 fine-tune）上验证 degeneracy 和 LP compression 是否仍然存在；或者明确重新定位论文为 \"fine-tuned small LMs for NER\" 的 scope。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **\"Two necessary conditions\" 框架缺乏预测力**\n- 具体位置：§4.4 (cross-dataset gradient), §5 (Practical guidelines)\n- 问题：Practical guidelines 要求 \"先在 labeled dev set 上估计 degeneracy 和 alignment\"，然后决定是否使用 LP selection。但如果你有 labeled dev set，就可以直接评估 LP selection 效果本身，不需要中间代理指标。框架的实用价值应该是 *a priori* 预测（无需标注数据），但当前形式等价于 \"在标注数据上跑一次看看\"。\n- 建议：探索无监督代理指标（如 output diversity 统计、LP range 分布），使框架能在无标注场景下提供 guidance。\n\n**W2** [warning] **缺少重要 baseline signals**\n- 具体位置：§3.2, §4.5 (Robustness), Appendix L (Verbalized Confidence)\n- 问题：(1) 没有测试 P(True)（Kadavath et al., 2022）或 Self-Certainty（Kang et al., 2025）作为 per-sample selection signal——VerbConf (Appendix L) 有测试但仅用了 raw 1-10 分数，没有 calibration；(2) 没有 hidden-state-based signals（论文在 limitations 中承认但作为 \"future work\" 处理，这对于声称 \"five signals studied\" 足以得出结论是不够的）；(3) 论文的 supervised verifier baseline（§4.5）仅使用五种 unsupervised signals 作为 features，这不是一个 fair test of \"whether learned approaches could help\"——应至少尝试用 hidden states 或 entity embeddings。\n- 建议：至少增加 Self-Certainty（首 token probability）作为额外 per-sample signal 进行完整评估。\n\n**W3** [warning] **Few-NERD 的训练设置差异构成 confound**\n- 具体位置：§4.1 line 15 \"except Few-NERD models which use 3 epochs\", Table E.8, Appendix N\n- 问题：Few-NERD 是唯一显示 LP selection success 的 dataset，也是唯一使用 3 epochs（vs. 5 epochs for others）的 dataset。Appendix N 的 epoch confound analysis 显示 5 epochs 时 LP gains 减半（+1.37 → +0.62 pp）。这意味着 Few-NERD 的 positive result 至少部分归因于训练设置差异，而非纯粹的 task structure。\n- 正文中 §4.4 和 §5 将 Few-NERD 的 success 主要归因于 \"low degeneracy + strong alignment\"（task properties），但 epoch confound 在正文的叙述中没有被充分强调。这可能导致 reader 过度概括 \"Few-NERD 类型的 tasks 天然适合 LP selection\"。\n- 建议：在正文 §4.4 明确讨论 epoch confound 对 Few-NERD positive result 的贡献程度，并在其他 dataset 上用 3 epochs 复现实验以解耦 epoch 效应和 task 效应。\n\n**W4** [warning] **RE extension 过于 preliminary 但在正文中引用频繁**\n- 具体位置：§1 line 26, §5 lines 6/21, Appendices G-I\n- 问题：RE 仅在 SciERC 一个 benchmark 上用一个 model 测试（§G 开头 \"Qwen3-8B unless noted\"），且被标注为 \"preliminary\" / \"single-dataset observation\"，但正文中多处引用 RE 结果来 support claims（如 §5 的 LP compression 讨论引用 RE free-form 结果）。Single-benchmark RE 结果不应作为支撑 general claims 的证据。\n- 建议：要么在 RE 上增加更多 benchmarks（ACE05, TACRED, DocRED），要么将 RE 引用严格限制在 appendix 且不作为正文 claims 的 evidence。\n\n---\n\n## 小问题（不影响接收）\n\n1. Abstract 较 dense：第 4-7 句连续出现大量数字（ρ, AUROC, pp, p-value），读起来像 results summary 而非 engaging abstract。建议精简数字，突出 conceptual contribution。\n2. 不同 table 之间的 greedy F1 基线略有不一致（Table 2: 0.645; Table 3: 0.644; N-scaling table: 0.640），虽然脚注解释了原因（seed 和 aggregation 差异），但仍可能造成 confusion。\n3. 统计检验方法多样（sign test, bootstrap, Fisher combined, TOST, permutation），但何时使用哪种方法的选择标准不够明确。建议在 Method 中统一说明 statistical testing strategy。\n4. §3.2 的 Fleiss' κ adaptation 到 entity sets 是 novel 的，但缺少对这种 adaptation 的 validity 论证——κ 假设 raters 独立，而同一 LM 的 samples 显然不完全独立（论文仅在 Appendix A 提供了 mild negative dependence 的 empirical check，但没有理论论证）。\n5. Reference verification: 3 entries not found in OpenAlex（hobelsberger2025systematic, lightman2024verify, venktesh2025trust）——请核实这些引用的准确性。lightman2024verify 应为 ICLR 2024 paper，OpenAlex 可能未收录；其余两篇为 arXiv preprints，需确认 title/year 正确。\n6. Table 1 caption 提到 \"RE results in Appendix D\" 但 Appendix D 的 section label 是 \"Bootstrap CI for Signal Comparisons\"——请检查 cross-reference 一致性（注：可能是我对 appendix lettering 的理解有误，但作者应确认）。\n\n---\n\n## 主要优势\n\n1. **实验设计的系统性和严谨度**: 5 signals × 4 datasets × 3 model families × 多个 temperature/N/epoch configurations，覆盖了大量潜在 confounds。Statistical methodology（bootstrap CI, TOST equivalence testing, power analysis with MDE）远超平均水平。\n2. **QE 与 selection 的清晰分离**: 这是一个有用的 methodological contribution。许多先前工作将两者混为一谈，本文明确区分并展示了它们可以 decouple。\n3. **透明的 limitations 讨论**: 论文对每一个 confound（epoch, thinking token, ε threshold, LoRA rank-capacity conflation）都提供了详细分析，这种 transparency 难能可贵。\n4. **附录极其详尽**: 21 页 appendix 覆盖了几乎所有可能的 reviewer concern（calibration, free-form ablation, OOD, verbalized confidence, per-type analysis, N-scaling, epoch confound, etc.）。\n5. **Few-NERD 的 positive result 是 well-powered**: n=32,565, CI [+1.18, +1.53]，这是 convincing evidence that LP selection CAN work under specific conditions。\n\n---\n\n## Missing References / 遗漏的相关工作\n\n1. **Selective Prediction for NER**: 论文引用了 Kuleshov & Liang (2015) 但缺少更多 selective prediction 文献，特别是 Geifman & El-Yaniv (2017) \"Selective Classification for Deep Neural Networks\" 和 Varshney et al. (2022) \"Investigating Selective Prediction Approaches Across Several Tasks in IID, OOD, and Adversarial Settings\"——这些直接与 QE-based abstention 相关。\n2. **LLM-based NER 的更多 baselines**: Xie et al. (2023) \"DecomposedPrompt\" for structured NER; Wang et al. (2023) \"GPT-NER\" 等 LLM-NER 工作应在 Related Work §2.3 提及。\n3. **Structured MBR 的更多文献**: 除了 Eikema et al. (2025) Structure-Conditional MBR，还应引用 Cheng & Vlachos (2023) \"Faster Minimum Bayes Risk Decoding with Confidence-based Pruning\" 和相关 structured decoding 工作。\n\n---\n\n## Verdict\n\n这是一篇实验工作极其严谨的论文，附录中的分析深度令人印象深刻。但核心 intellectual contribution 有限：(1) \"instance-level signals can't rank candidates\" 是 definitional 而非 discovered；(2) LP compression 的诊断有价值但被过度包装在一个 shallow \"gap\" 框架中；(3) 任务和模型覆盖面不足以支撑 title-level claims。建议作者要么缩窄 scope 并深化对 LP compression 的理论理解，要么扩展到更多 tasks/scales 以 empirically 支撑 general claims。\n\n当前形式可能适合 Findings，距 main conference 还有距离。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-18T06:10:11.337329+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4683
}
```

</details>

---


### Assistant

_source line 1586 · 2026-05-18T06:10:19.756531+00:00_

审稿报告已提交给 Review Director。

总结：本文实验设计严谨（5 signals × 4 datasets × 3 model families，统计方法远超平均水平），但 intellectual contribution 受限于三个关键问题：(1) 核心概念 "correlation-selection gap" 新颖性不足——4/5 signals 无法 rank candidates 是 definitional 而非 discovered；(2) 仅覆盖 NER（+exploratory RE）不足以支撑 "Structured IE" 的泛化声明；(3) 3B-8B 模型范围限制了 practical guidelines 的适用性。评分 Overall 2.5/5（Findings borderline），Soundness 3.5/5，Excitement 2/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 41

## Round 41

8 recorded events


### User

_source line 1587 · 2026-05-18T06:10:21.075655+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）

特别关注与你自己审稿意见的异同——如果 Reviewer 1 发现了你遗漏的问题，请明确承认；如果你认为 Reviewer 1 的某个判断有误，请提供具体反驳。

---

# Reviewer 1 审稿意见 — Round 1

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
**审查侧重**: 方法严谨性 + 实验设计

## 2. Strengths

**S1. QE 与 selection 的系统性分离。** 先前工作常将 "信号与质量相关" 等同于 "信号可用于选择"，本文用大量实验严格证明了这一等价关系不成立。

**S2. 极其透明的实验报告。** 几乎每一个有争议的设计选择都被主动标注并讨论。

**S3. 多层次证据三角验证。** "两个必要条件" 的论证通过多条独立证据线收敛。

**S4. Instance-level vs per-sample 信号的 definitional observation。** §3.1 指出 4/5 信号是 instance-level aggregates，by construction 无法区分同一 input 下的不同 candidates。

**S5. 附录的深度和完整性。** 14 个 appendix sections。

**S6. 统计方法总体恰当。**

## 3. Weaknesses

### Must-Fix

**W1 [Must-Fix]. Few-NERD 3-epoch vs SciERC 5-epoch 的 confound 削弱了核心 cross-dataset comparison。**
- Table 4 的 cross-dataset gradient 是 training duration 和 dataset property 的混淆效应。
- SciERC 3-epoch（degeneracy 6.4% 但 LP Δ=-1.18pp）反驳了 "low degeneracy → LP works" 的简单叙事。
- 论文在 Appendix N 承认但主文叙事未充分调整。
- 建议：(1) Table 4 旁标注 training epochs 差异；(2) 加入 matched-epoch 对比行；(3) 在主文承认 confound 影响，降低 claim 强度。

**W2 [Must-Fix]. "Two jointly necessary conditions" 的因果性表述过强。**
- "Jointly necessary" 是强因果声明，但证据是 observational。
- Temperature ablation 只操纵了 degeneracy，alignment 是被动观察的。
- SciERC 3-epoch（ρ=0.317 > 0.3 且 degeneracy 6.4% < 15%，但 LP 仍为负）是一个潜在反例。
- 建议：改为 "jointly associated with" 或 "both appear required in the regimes we tested"。

### Should-Fix

**W3 [Should-Fix]. 2-seed 实验设计统计效力不足。**
- Selection 的 primary results（Table 3）使用 2-seed 平均。2 seeds 无法估计 variance。
- Table 6 的 3-seed stability 仅适用于 QE signal rankings，不直接验证 selection gains 的 seed stability。

**W4 [Should-Fix]. Per-entity-type 分析的 non-independence 问题比论文讨论的更严重。**
- 8 entity types 来自同一模型/tokenizer/temperature/training run。
- 建议报告 ICC 估计 effective df。

**W5 [Should-Fix]. "Supervised verifier baseline" 的 framing 有误导性。**
- §4.5 的 "supervised verifier" 实际只是对 5 个 unsupervised signals 的 supervised combination。
- 不是 Cobbe et al. (2021) 意义上的 verifier。
- 建议改为 "supervised signal combination"。

**W6 [Should-Fix]. Degeneracy 的操作性定义需要在主文中更清晰地区分。**
- "Instance degeneracy"（所有 samples 产生相同 F1）与 "所有 outputs 完全相同" 不同。
- Table 8 显示 SciERC "Identical outputs" = 11% 但 "Constant F1" = 17.8%。

**W7 [Should-Fix]. Table 4 中 SciERC 数值在不同 tables 之间存在不一致。**
- SciERC greedy F1 在 Table 3 为 0.645，Table 4 为 0.644，Table 12 为 0.640。
- 建议统一或在某处统一声明 canonical evaluation protocol。

### Minor

**M1** Abstract "jointly necessary" 同 W2。
**M2** §1 line 8 Yao et al. 使用 hard-prompted LLMs vs 本文 fine-tuned models 差异应明确提及。
**M3** Table 3 的 EM/VC 没有报告 p-values。
**M4** Kendall's W=1.0 基于 m=3 raters，statistical precision limited。
**M5** References: 实际使用 XGrammar 应被引用。
**M6** 缺失引用：Geifman &amp; El-Yaniv (2017)、Lafferty et al. (2001) CRFs、Lin et al. (2024)。

## 4. Questions

**Q1.** SciERC 3-epoch 的 ρ=0.317 略高于建议的 threshold ρ≳0.3，但 LP Δ=-1.18pp。Threshold 是否应该更高？

**Q2.** Few-NERD 是 INTRA coarse setting（8 coarse types）。Fine-grained types 下 LP selection 是否仍然有效？

**Q3.** Greedy decoding (T=0) 作为 selection baseline 是否太弱？Beam search 或 top-k sampling 对比如何？

**Q4.** Entity-token LP 的高 variance + 低性能是否说明 fine-tuned models 在 representation level 上 near-deterministic？

**Q5.** Table 12 N-scaling: N=8→N=32 LP Δ 从 +0.39pp→+0.95pp（p=0.091）。外推到 N=64/128 是否可能显著？

## 5. Missing References

- Geifman &amp; El-Yaniv (2017) Selective Prediction
- Lafferty et al. (2001) CRFs
- XGrammar
- Lin et al. (2024) "Generating Confidence from LLMs"

## 6. Overall Assessment

**Overall**: 3.5 (borderline between Findings acceptance and Conference acceptance)
**Soundness**: 3.5/5
**Excitement**: 3.5/5
**Reproducibility**: 4/5
**Confidence**: 4/5

**一句话总结**: 方法论框架和实验深度出色，但核心因果 claim 被 epoch confound 和有限的 causal identification strategy 削弱。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-18T06:10:46.851778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "offset": "28",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "offset": "28",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-18T06:10:46.902314+00:00_

28	Temperature manipulation provides the primary evidence ($T{=}1.2$: degeneracy 12.5\%, $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}): it alters output diversity without changing model capacity, isolating the degeneracy lever from alignment.
29	Even at degeneracy approaching Few-NERD levels (12.5\% vs.\ 13.8\%), LP does not improve selection because alignment remains weak ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5).
30	LoRA rank${=}8$ (degeneracy 7.2\%, $\rho{=}0.24$) corroborates the pattern, though this ablation conflates diversity with capacity (secondary evidence).
31	The cross-dataset gradient (59\% $\to$ $-1.05$~pp, 18\% $\to$ $+0.61$~pp, 14\% $\to$ $+1.36$~pp; $n{=}3$ datasets, exploratory) is consistent with an inverse relationship; per-entity-type analysis within Few-NERD ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; entity types share model and tokenizer, effective $\mathit{df}$ may be lower; Appendix~\ref{app:per_type_lp}) provides supporting evidence.
32	
33	\paragraph{Practical guidelines.}
34	Practitioners should first estimate instance degeneracy and LP-quality alignment on a labeled development set.
35	The decision rule is: if degeneracy ${<}$15\% and within-instance $\rho(\text{LP}, \text{F1}) \gtrsim 0.3$, use LP selection (Few-NERD: $+1.36$~pp, $p{<}0.001$; gains scale with $N$); otherwise, prefer greedy decoding ($T{=}0$), using structural signals for quality estimation only ($\rho{=}0.43$--$0.47$ even in the high-degeneracy regime; Table~\ref{tab:degeneracy}).
36	Temperature provides a controllable lever for degeneracy (40.3\% at $T{=}0.5$ to 12.5\% at $T{=}1.2$; Table~\ref{tab:t_degeneracy}) but cannot address alignment; training convergence offers a second lever: on Few-NERD, degeneracy rises from 11\% to 31\% between 3 and 5 epochs, halving LP gains (Table~\ref{tab:epoch_confound}); a SciERC 3-point curve (3, 5, 10 epochs) shows both conditions degrading in tandem, with degeneracy rising from 6.4\% to 47.8\% while within-instance alignment collap
…[truncated 1282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1590 · 2026-05-18T06:10:50.718442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1325",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1325",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1591 · 2026-05-18T06:10:50.718968+00:00_

1325	\paragraph{SciERC epoch curve.}
1326	Table~\ref{tab:epoch_scierc} extends the analysis to SciERC with a 3-point curve (3, 5, 10 epochs; Qwen3-8B, $N{=}8$, $T{=}1.0$).
1327	Degeneracy increases monotonically (6.4\% $\to$ 17.8\% $\to$ 47.8\%), and within-instance LP-quality correlation degrades in tandem (median $\rho$: 0.317 $\to$ 0.282 $\to$ 0.120), confirming that overtraining erodes both necessary conditions simultaneously.
1328	LP selection does not yield significant gains at any training duration ($-1.18$, $+0.62$, $+0.75$~pp; all below the ${\approx}$1.5~pp MDE), despite oracle headroom ranging from 8.4 to 15.0~pp.
1329	At 10 epochs, the model retains competitive greedy F1 (0.649 vs.\ 0.650 at 3 epochs) yet both conditions are violated: 47.8\% degenerate instances and $\rho{=}0.120$.
1330	The gradient confirms that degeneracy is convergence-driven rather than a fixed dataset property: extended training compresses output distributions, degrading both diversity and within-instance alignment. However, even at 3 epochs (lowest degeneracy, 6.4\%), SciERC's within-instance alignment ($\rho{=}0.317$) remains below the threshold observed on Few-NERD ($\rho{\sim}0.5$), reinforcing that controlling degeneracy alone is insufficient when the alignment condition is not met.
1331	
1332	\begin{table}[t]
1333	\centering
1334	\small
1335	\caption{SciERC NER epoch curve (Qwen3-8B, $N{=}8$, $T{=}1.0$). Training duration modulates both instance degeneracy and within-instance LP-quality alignment. ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``LP $\Delta$'': LP selection gain over greedy (gold-filtered; none reaches the ${\approx}$1.5~pp MDE). ``$\rho$ med'': median within-instance LP-quality correlation.}
1336	\label{tab:epoch_scierc}
1337	\begin{tabular}{lccc}
1338	\toprule
1339	Metric & 3-epoch & 5-epoch & 10-epoch \\
1340	\midrule
1341	Greedy F1 & 0.650 & 0.644 & 0.649 \\
1342	Instance degen.\ (\%) & 6.4 & 17.8 & 47.8 \\
1343	LP $\Delta$ (pp) & $-$1.18 & $+
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1592 · 2026-05-18T06:12:46.872450+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见\n\n---\n\n### Weaknesses 逐条回应\n\n---\n\n**[AGREE] R1-W1: Few-NERD 3-epoch vs SciERC 5-epoch confound**\n\n完全同意。这是我在 R2-W3 中独立提出的同一问题。R1 的表述比我更精确：Table 4 的 cross-dataset gradient 同时编码了 training duration 差异和 dataset properties，无法分离两者的贡献。\n\n补充 R1 的论点：Table E.8（Appendix N）显示 Few-NERD 5-epoch 的 LP gains 从 +1.37pp 降至 +0.62pp，即 epochs 差异解释了约 55% 的 gain 幅度差。更关键的是，SciERC 3-epoch（Table E.9）degeneracy 仅 6.4%（远低于 Few-NERD 的 13.8%），但 LP Δ=-1.18pp——这不仅说明 epoch confound 存在，还直接挑战了 \"low degeneracy → LP works\" 的核心叙事。\n\nR1 建议在 Table 4 旁标注 epochs 差异并加入 matched-epoch 行，我认为这是最低要求。理想情况下应在所有 4 datasets 上用统一 epoch 设置（例如 early stopping by validation loss）重跑 Table 4。\n\n---\n\n**[AGREE] R1-W2: \"Jointly necessary\" 的因果性表述过强**\n\n强烈同意，且 R1 提出了一个我未充分分析的具体反例。\n\n核心证据：SciERC 3-epoch（Table E.9, Appendix N）满足论文自身的 practical guideline（§5 line 35: \"if degeneracy <15% and within-instance ρ(LP,F1) ≳ 0.3\"）：\n- Degeneracy = 6.4% ✓（远低于 15%）\n- ρ = 0.317 ✓（高于 ≳0.3）\n- 但 LP Δ = **-1.18pp** ✗\n\n这是论文框架的直接反例。论文在 Appendix N 试图用 \"ρ=0.317 remains below Few-NERD's ~0.5\" 来解释，但这意味着实际 threshold 是 ~0.5 而非 ≳0.3——与 §5 的 guideline 自相矛盾。如果 threshold 需要事后调整以排除反例，则框架没有预测力。\n\nR1 建议改为 \"jointly associated with\" 是恰当的。我进一步建议：(1) 删除 \"necessary conditions\" 表述，改为 \"jointly associated conditions\"；(2) 不给出具体 threshold（因为现有证据无法确定），改为 \"degeneracy 和 alignment 存在梯度关系\"；(3) 在 §5 practical guidelines 明确声明 SciERC 3-epoch 反例。\n\n---\n\n**[AGREE] R1-W3: 2-seed 实验设计统计效力不足**\n\n同意。这是我遗漏的一个重要问题。\n\n2 seeds 的根本问题是无法可靠估计 training seed 方差。Table 6（multiseed）报告了 QE 的 3-seed stability（σ≤0.026），但 selection 的 primary results（Table 3）仅用 2-seed 平均。论文在脚注（§4.3 footnote）承认 \"the reduced seed count for primary results reflects computational budget\"，但这不改变统计效力不足的事实。\n\n具体影响：Table 3 报告 LP selection F1 = 0.647±0.005（SciERC），其中 ±0.005 来自 2 seeds，不足以可靠估计 seed-level variance。Few-NERD 的 LP +1.36pp 结论可能更稳健（n=32,565 提供了高 within-seed power），但 between-seed stability 仍只有 2 个点。\n\n---\n\n**[AGREE] R1-W4: Per-entity-type 分析的 non-independence 问题**\n\n同意，且我认为 R1 对这个问题的严重程度判断准确。\n\n论文承认 \"effective degrees of freedom may be lower than 6\"（§4.4, Figure 2 caption），但没有量化。8 个 entity types 来自同一 model checkpoint、同一 tokenizer、同一 temperature、同一 training data distribution。Type 之间的 LP behavior 必然受到 shared representation 的约束——例如，如果模型的 entity-boundary detection 整体偏弱，所有 types 的 LP 都会受影响。\n\nR1 建议报告 ICC 来估计 effective df，这是一个可行的建议。如果 ICC 高（例如 >0.5），有效样本量可能只有 3-4，Spearman ρ=-0.881 的 p=0.004 会大幅膨胀。\n\n---\n\n**[AGREE] R1-W5: \"Supervised verifier baseline\" 的 framing 有误导性**\n\n同意。这与我在 R2-W2 中提出的问题一致。\n\n§4.5 的 baseline 使用 logistic regression / MLP / random forest 对 5 个 unsupervised signals 做 supervised combination，这与 Cobbe et al. (2021) 的 learned verifiers（直接从 model representations 学习 per-sample scoring）有本质区别。前者受限于输入 features 本身的信息瓶颈（论文自身在 §4.5 最后一句承认：\"whether richer representations could close the gap remains untested\"）；后者可以访问 hidden states、attention patterns 等更丰富的信息。\n\n将 \"supervised signal combination\" 称为 \"supervised verifier baseline\" 会给 reader 留下 \"learned verification doesn't work\" 的错误印象，而实际上论文根本没有测试真正的 learned verifier。\n\nR1 建议改名为 \"supervised signal combination\"，我完全支持。\n\n---\n\n**[AGREE] R1-W6: Degeneracy 的操作性定义需要区分**\n\n同意。这是我遗漏的一个 clarity 问题。\n\nTable 8（Appendix E）清楚地显示了差异：SciERC 8B 的 \"Identical outputs\" = 11%，但 \"Constant F1\" = 17.8%。这意味着 6.8% 的 instances 产生了不同的 outputs 但恰好得到相同的 F1 score（例如，两个 sample 各自 miss 了不同的 entity 但总 F1 相同）。\n\n这个区分对 selection 分析很重要：在 \"different outputs, same F1\" 的 instances 中，selection signal 确实在 rank candidates，但 rank 的正确与否无法影响 F1——这是 evaluation metric 的 resolution 限制，不是 signal 的 failure。论文应在 §4.3 或 §5 明确讨论这个区分。\n\n---\n\n**[AGREE] R1-W7: 数值不一致**\n\n同意。我在 R2 minor issues #2 中独立提出了同样的问题。\n\nSciERC greedy F1 在不同 tables 中的值：Table 3 = 0.645, Table 4 = 0.644, Table 12 = 0.640, N-scaling table footnote 说明 \"Values differ slightly from Table 3 due to seed and aggregation differences\"。虽然差异不大且有解释，但对于一篇强调统计严谨性的论文，多处 baseline 数值不一致会削弱 reader 的信任。\n\nR1 建议在某处统一声明 canonical evaluation protocol，这是合理的。\n\n---\n\n### Questions 逐条回应\n\n---\n\n**[AGREE] R1-Q1: SciERC 3-epoch 的 ρ=0.317 是否说明 threshold 应更高？**\n\n这是 R1-W2 的延伸。如前分析，SciERC 3-epoch（degeneracy 6.4%, ρ=0.317）是论文 ≳0.3 threshold 的直接反例（LP Δ=-1.18pp）。论文在 Appendix N 暗示实际 threshold 在 ~0.5（Few-NERD 的 alignment level），但：\n1. 如果 threshold 是 ~0.5 而非 ~0.3，则论文只有 1 个 dataset（Few-NERD）满足条件，framework 的实用价值进一步降低；\n2. 用 Few-NERD 的 ρ 值来定义 threshold，然后声称 Few-NERD 满足 threshold，是循环论证。\n\n我认为这个 question 实质上揭示了 \"two necessary conditions\" 框架的根本缺陷：threshold 是从极少数据点 post-hoc 拟合的，缺乏独立验证。\n\n---\n\n**[AGREE] R1-Q2: Few-NERD INTRA coarse vs fine-grained types 的影响**\n\n这是我遗漏的一个好问题。Few-NERD INTRA coarse 使用 8 个 coarse entity types，其 degeneracy 仅 13.8%。Fine-grained types（66 types）下：\n- 每个 type 的 instances 更少 → 统计效力降低\n- 更细粒度的 type 区分可能增加 extraction ambiguity → 可能改变 degeneracy 和 alignment\n- 论文没有报告任何 fine-grained Few-NERD 结果\n\n这个 gap 与我 R2-N2 的 concern（任务覆盖面不足）相呼应。\n\n---\n\n**[REBUT] R1-Q3: Greedy (T=0) 作为 baseline 是否太弱？**\n\n部分不同意。\n\nGreedy decoding (T=0) 是 sample selection 的 natural baseline——它代表 \"不做 sampling，直接取 argmax\" 的 strategy。对于 best-of-N selection，核心问题是 \"sample N 次后用 signal 选择，是否优于不 sample 直接 greedy\"。如果 signal-selected output 不能 beat greedy，则 sampling + selection 的 compute overhead 不值得。\n\nBeam search 是另一种 decode strategy，但它不属于 sample selection 范畴——beam search 在 decoding 过程中就做了 pruning，而非先 sample 后 select。将 beam search 引入比较会混淆 decoding strategy 和 post-hoc selection 两个维度。\n\n不过，R1 的 concern 有一个合理之处：如果论文声称 \"confidence signals fail to scale structured IE\"（title），那么应该与所有 test-time compute 策略比较，不仅限于 sample-then-select。Beam search + length normalization 作为 structured decoding 的 standard technique 确实缺失。\n\n---\n\n**[AGREE] R1-Q4: Entity-token LP 的高 variance + 低性能是否说明 fine-tuned models 在 representation level 上 near-deterministic？**\n\n同意这是一个重要的 interpretive question。论文在 §5 line 22 给出了解释：\"fine-tuned models assign near-deterministic probabilities at the representation level, and compression cannot be broken by disaggregating to entity tokens\"。\n\n但这个解释如果成立，有一个深层 implication 论文未讨论：如果 fine-tuned models 在 representation level 上 near-deterministic，那么 LP-based selection 在 fine-tuned setting 下可能 *fundamentally* 不可能工作（不仅仅是 \"compressed\" 而是 \"absent\"）。这会改变论文的 framing——从 \"LP fails because of compression\" 变为 \"LP fails because fine-tuning eliminates the per-sample quality information that LP could encode\"。这是一个更 fundamental 的 negative result。\n\n---\n\n**[REBUT] R1-Q5: N=64/128 外推是否可能让 LP 变显著？**\n\nTable 12（Appendix K）显示 SciERC 上 N=8→32 LP Δ 从 +0.39pp 到 +0.95pp（p=0.091）。但趋势是 sublinear 的，且即使在 N=32（degeneracy 仅 4%，oracle headroom +20pp），LP 也只捕获了 <5% 的 headroom。\n\n即使外推到 N=64/128 并达到统计显著性，practical significance 仍然极低（可能 <2pp on a 20pp headroom）。且 compute cost scales linearly with N。论文自己的结论是准确的：\"signal-based selection captures less than 5% of headroom even at N=32\"（Appendix K）。\n\n但 R1 的 question 暗示了一个论文未探索的 possibility：N-scaling 是否会改变 within-instance LP-quality alignment（而非仅改变 degeneracy）？Table 12 未报告不同 N 下的 within-instance ρ，只报告了 degeneracy。如果 N 增加时 ρ 也改善（更多 samples 提供了更好的 LP discrimination landscape），趋势可能不仅仅是 sublinear。这是一个值得探索的方向。\n\n---\n\n### 与我自己审稿意见的交叉对比\n\n**R1 发现了我遗漏的问题（我明确承认）：**\n1. **R1-W3（2-seed 不足）**: 我未独立提出。这是一个有效的统计效力问题。\n2. **R1-W4（per-entity-type non-independence）**: 我未深入分析。R1 建议的 ICC 方法是合理的。\n3. **R1-W6（degeneracy 定义不清晰）**: 我遗漏了 \"identical outputs\" vs \"constant F1\" 的区分。\n4. **R1-Q2（Few-NERD coarse vs fine-grained）**: 好问题，我未想到。\n5. **R1-Q4（entity-token LP → near-deterministic representation）**: 我未将这个 observation 推到其 logical conclusion。\n6. **R1-M5（XGrammar 引用缺失）**: 论文实际使用了 XGrammar 但仅引用了 Willard & Louf (2023)，应引用 XGrammar 本身。\n\n**R1 与我共同发现的问题：**\n1. **Epoch confound**（R1-W1 ≈ R2-W3）\n2. **\"Supervised verifier\" 命名不当**（R1-W5 ≈ R2-W2 的部分内容）\n3. **数值不一致**（R1-W7 ≈ R2 minor #2）\n4. **Missing references: Geifman & El-Yaniv (2017)**（R1-M6 ≈ R2 missing references #1）\n\n**我提出但 R1 未提出的问题：**\n1. **R2-N1（核心概念新颖性不足）**: R1 未质疑 \"correlation-selection gap\" 的 novelty，反而在 Excitement 上给了 3.5/5。我认为这是我们最大的分歧点——我认为 gap 的核心解释（instance-level signals can't rank by definition）是 definitional 而非 discovered，R1 似乎认为系统性的 empirical documentation 本身构成 sufficient contribution。\n2. **R2-N2（任务覆盖面不足以支撑 title claims）**: R1 未质疑 \"Structured IE\" 的泛化范围。\n3. **R2-N3（模型规模范围不足）**: R1 未将此列为 critical issue。\n4. **R2-W1（framework 缺乏预测力的循环性）**: R1 的 Q1 触及了这个问题但未将其升级为 weakness。\n\n---\n\n### 我与 R1 的评分差异分析\n\n| 维度 | R1 | R2 | 差异原因 |\n|------|----|----|----------|\n| Overall | 3.5 | 2.5 | 我对 novelty 的要求更高；R1 认为 empirical documentation 的深度足以构成 contribution，我认为需要更深的 conceptual insight |\n| Excitement | 3.5 | 2.0 | 最大分歧。R1 可能更看重 practical relevance（negative result 对 practitioners 有价值），我更看重 intellectual novelty（core insight is definitional） |\n| Soundness | 3.5 | 3.5 | 一致 |\n\n我维持我的评分。核心分歧是 novelty 标准：R1-W2 指出 \"jointly necessary\" 的因果 claim 过强，如果 downgrade 为 \"associated\"，论文的 contribution 进一步从 \"framework discovery\" 降为 \"empirical observation\"，这在我看来更接近 Findings 而非 main conference。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见\n\n---\n\n### Weaknesses 逐条回应\n\n---\n\n**[AGREE] R1-W1: Few-NERD 3-epoch vs SciERC 5-epoch confound**\n\n完全同意。这是我在 R2-W3 中独立提出的同一问题。R1 的表述比我更精确：Table 4 的 cross-dataset gradient 同时编码了 training duration 差异和 dataset properties，无法分离两者的贡献。\n\n补充 R1 的论点：Table E.8（Appendix N）显示 Few-NERD 5-epoch 的 LP gains 从 +1.37pp 降至 +0.62pp，即 epochs 差异解释了约 55% 的 gain 幅度差。更关键的是，SciERC 3-epoch（Table E.9）degeneracy 仅 6.4%（远低于 Few-NERD 的 13.8%），但 LP Δ=-1.18pp——这不仅说明 epoch confound 存在，还直接挑战了 \"low degeneracy → LP works\" 的核心叙事。\n\nR1 建议在 Table 4 旁标注 epochs 差异并加入 matched-epoch 行，我认为这是最低要求。理想情况下应在所有 4 datasets 上用统一 epoch 设置（例如 early stopping by validation loss）重跑 Table 4。\n\n---\n\n**[AGREE] R1-W2: \"Jointly necessary\" 的因果性表述过强**\n\n强烈同意，且 R1 提出了一个我未充分分析的具体反例。\n\n核心证据：SciERC 3-epoch（Table E.9, Appendix N）满足论文自身的 practical guideline（§5 line 35: \"if degeneracy <15% and within-instance ρ(LP,F1) ≳ 0.3\"）：\n- Degeneracy = 6.4% ✓（远低于 15%）\n- ρ = 0.317 ✓（高于 ≳0.3）\n- 但 LP Δ = **-1.18pp** ✗\n\n这是论文框架的直接反例。论文在 Appendix N 试图用 \"ρ=0.317 remains below Few-NERD's ~0.5\" 来解释，但这意味着实际 threshold 是 ~0.5 而非 ≳0.3——与 §5 的 guideline 自相矛盾。如果 threshold 需要事后调整以排除反例，则框架没有预测力。\n\nR1 建议改为 \"jointly associated with\" 是恰当的。我进一步建议：(1) 删除 \"necessary conditions\" 表述，改为 \"jointly associated conditions\"；(2) 不给出具体 threshold（因为现有证据无法确定），改为 \"degeneracy 和 alignment 存在梯度关系\"；(3) 在 §5 practical guidelines 明确声明 SciERC 3-epoch 反例。\n\n---\n\n**[AGREE] R1-W3: 2-seed 实验设计统计效力不足**\n\n同意。这是我遗漏的一个重要问题。\n\n2 seeds 的根本问题是无法可靠估计 training seed 方差。Table 6（multiseed）报告了 QE 的 3-seed stability（σ≤0.026），但 selection 的 primary results（Table 3）仅用 2-seed 平均。论文在脚注（§4.3 footnote）承认 \"the reduced seed count for primary results reflects computational budget\"，但这不改变统计效力不足的事实。\n\n具体影响：Table 3 报告 LP selection F1 = 0.647±0.005（SciERC），其中 ±0.005 来自 2 seeds，不足以可靠估计 seed-level variance。Few-NERD 的 LP +1.36pp 结论可能更稳健（n=32,565 提供了高 within-seed power），但 between-seed stability 仍只有 2 个点。\n\n---\n\n**[AGREE] R1-W4: Per-entity-type 分析的 non-independence 问题**\n\n同意，且我认为 R1 对这个问题的严重程度判断准确。\n\n论文承认 \"effective degrees of freedom may be lower than 6\"（§4.4, Figure 2 caption），但没有量化。8 个 entity types 来自同一 model checkpoint、同一 tokenizer、同一 temperature、同一 training data distribution。Type 之间的 LP behavior 必然受到 shared representation 的约束——例如，如果模型的 entity-boundary detection 整体偏弱，所有 types 的 LP 都会受影响。\n\nR1 建议报告 ICC 来估计 effective df，这是一个可行的建议。如果 ICC 高（例如 >0.5），有效样本量可能只有 3-4，Spearman ρ=-0.881 的 p=0.004 会大幅膨胀。\n\n---\n\n**[AGREE] R1-W5: \"Supervised verifier baseline\" 的 framing 有误导性**\n\n同意。这与我在 R2-W2 中提出的问题一致。\n\n§4.5 的 baseline 使用 logistic regression / MLP / random forest 对 5 个 unsupervised signals 做 supervised combination，这与 Cobbe et al. (2021) 的 learned verifiers（直接从 model representations 学习 per-sample scoring）有本质区别。前者受限于输入 features 本身的信息瓶颈（论文自身在 §4.5 最后一句承认：\"whether richer representations could close the gap remains untested\"）；后者可以访问 hidden states、attention patterns 等更丰富的信息。\n\n将 \"supervised signal combination\" 称为 \"supervised verifier baseline\" 会给 reader 留下 \"learned verification doesn't work\" 的错误印象，而实际上论文根本没有测试真正的 learned verifier。\n\nR1 建议改名为 \"supervised signal combination\"，我完全支持。\n\n---\n\n**[AGREE] R1-W6: Degeneracy 的操作性定义需要区分**\n\n同意。这是我遗漏的一个 clarity 问题。\n\nTable 8（Appendix E）清楚地显示了差异：SciERC 8B 的 \"Identical outputs\" = 11%，但 \"Constant F1\" = 17.8%。这意味着 6.8% 的 instances 产生了不同的 outputs 但恰好得到相同的 F1 score（例如，两个 sample 各自 miss 了不同的 entity 但总 F1 相同）。\n\n这个区分对 selection 分析很重要：在 \"different outputs, same F1\" 的 instances 中，selection signal 确实在 rank candidates，但 rank 的正确与否无法影响 F1——这是 evaluation metric 的 resolution 限制，不是 signal 的 failure。论文应在 §4.3 或 §5 明确讨论这个区分。\n\n---\n\n**[AGREE] R1-W7: 数值不一致**\n\n同意。我在 R2 minor issues #2 中独立提出了同样的问题。\n\nSciERC greedy F1 在不同 tables 中的值：Table 3 = 0.645, Table 4 = 0.644, Table 12 = 0.640, N-scaling table footnote 说明 \"Values differ slightly from Table 3 due to seed and aggregation differences\"。虽然差异不大且有解释，但对于一篇强调统计严谨性的论文，多处 baseline 数值不一致会削弱 reader 的信任。\n\nR1 建议在某处统一声明 canonical evaluation protocol，这是合理的。\n\n---\n\n### Questions 逐条回应\n\n---\n\n**[AGREE] R1-Q1: SciERC 3-epoch 的 ρ=0.317 是否说明 threshold 应更高？**\n\n这是 R1-W2 的延伸。如前分析，SciERC 3-epoch（degeneracy 6.4%, ρ=0.317）是论文 ≳0.3 threshold 的直接反例（LP Δ=-1.18pp）。论文在 Appendix N 暗示实际 threshold 在 ~0.5（Few-NERD 的 alignment level），但：\n1. 如果 threshold 是 ~0.5 而非 ~0.3，则论文只有 1 个 dataset（Few-NERD）满足条件，framework 的实用价值进一步降低；\n2. 用 Few-NERD 的 ρ 值来定义 threshold，然后声称 Few-NERD 满足 threshold，是循环论证。\n\n我认为这个 question 实质上揭示了 \"two necessary conditions\" 框架的根本缺陷：threshold 是从极少数据点 post-hoc 拟合的，缺乏独立验证。\n\n---\n\n**[AGREE] R1-Q2: Few-NERD INTRA coarse vs fine-grained types 的影响**\n\n这是我遗漏的一个好问题。Few-NERD INTRA coarse 使用 8 个 coarse entity types，其 degeneracy 仅 13.8%。Fine-grained types（66 types）下：\n- 每个 type 的 instances 更少 → 统计效力降低\n- 更细粒度的 type 区分可能增加 extraction ambiguity → 可能改变 degeneracy 和 alignment\n- 论文没有报告任何 fine-grained Few-NERD 结果\n\n这个 gap 与我 R2-N2 的 concern（任务覆盖面不足）相呼应。\n\n---\n\n**[REBUT] R1-Q3: Greedy (T=0) 作为 baseline 是否太弱？**\n\n部分不同意。\n\nGreedy decoding (T=0) 是 sample selection 的 natural baseline——它代表 \"不做 sampling，直接取 argmax\" 的 strategy。对于 best-of-N selection，核心问题是 \"sample N 次后用 signal 选择，是否优于不 sample 直接 greedy\"。如果 signal-selected output 不能 beat greedy，则 sampling + selection 的 compute overhead 不值得。\n\nBeam search 是另一种 decode strategy，但它不属于 sample selection 范畴——beam search 在 decoding 过程中就做了 pruning，而非先 sample 后 select。将 beam search 引入比较会混淆 decoding strategy 和 post-hoc selection 两个维度。\n\n不过，R1 的 concern 有一个合理之处：如果论文声称 \"confidence signals fail to scale structured IE\"（title），那么应该与所有 test-time compute 策略比较，不仅限于 sample-then-select。Beam search + length normalization 作为 structured decoding 的 standard technique 确实缺失。\n\n---\n\n**[AGREE] R1-Q4: Entity-token LP 的高 variance + 低性能是否说明 fine-tuned models 在 representation level 上 near-deterministic？**\n\n同意这是一个重要的 interpretive question。论文在 §5 line 22 给出了解释：\"fine-tuned models assign near-deterministic probabilities at the representation level, and compression cannot be broken by disaggregating to entity tokens\"。\n\n但这个解释如果成立，有一个深层 implication 论文未讨论：如果 fine-tuned models 在 representation level 上 near-deterministic，那么 LP-based selection 在 fine-tuned setting 下可能 *fundamentally* 不可能工作（不仅仅是 \"compressed\" 而是 \"absent\"）。这会改变论文的 framing——从 \"LP fails because of compression\" 变为 \"LP fails because fine-tuning eliminates the per-sample quality information that LP could encode\"。这是一个更 fundamental 的 negative result。\n\n---\n\n**[REBUT] R1-Q5: N=64/128 外推是否可能让 LP 变显著？**\n\nTable 12（Appendix K）显示 SciERC 上 N=8→32 LP Δ 从 +0.39pp 到 +0.95pp（p=0.091）。但趋势是 sublinear 的，且即使在 N=32（degeneracy 仅 4%，oracle headroom +20pp），LP 也只捕获了 <5% 的 headroom。\n\n即使外推到 N=64/128 并达到统计显著性，practical significance 仍然极低（可能 <2pp on a 20pp headroom）。且 compute cost scales linearly with N。论文自己的结论是准确的：\"signal-based selection captures less than 5% of headroom even at N=32\"（Appendix K）。\n\n但 R1 的 question 暗示了一个论文未探索的 possibility：N-scaling 是否会改变 within-instance LP-quality alignment（而非仅改变 degeneracy）？Table 12 未报告不同 N 下的 within-instance ρ，只报告了 degeneracy。如果 N 增加时 ρ 也改善（更多 samples 提供了更好的 LP discrimination landscape），趋势可能不仅仅是 sublinear。这是一个值得探索的方向。\n\n---\n\n### 与我自己审稿意见的交叉对比\n\n**R1 发现了我遗漏的问题（我明确承认）：**\n1. **R1-W3（2-seed 不足）**: 我未独立提出。这是一个有效的统计效力问题。\n2. **R1-W4（per-entity-type non-independence）**: 我未深入分析。R1 建议的 ICC 方法是合理的。\n3. **R1-W6（degeneracy 定义不清晰）**: 我遗漏了 \"identical outputs\" vs \"constant F1\" 的区分。\n4. **R1-Q2（Few-NERD coarse vs fine-grained）**: 好问题，我未想到。\n5. **R1-Q4（entity-token LP → near-deterministic representation）**: 我未将这个 observation 推到其 logical conclusion。\n6. **R1-M5（XGrammar 引用缺失）**: 论文实际使用了 XGrammar 但仅引用了 Willard & Louf (2023)，应引用 XGrammar 本身。\n\n**R1 与我共同发现的问题：**\n1. **Epoch confound**（R1-W1 ≈ R2-W3）\n2. **\"Supervised verifier\" 命名不当**（R1-W5 ≈ R2-W2 的部分内容）\n3. **数值不一致**（R1-W7 ≈ R2 minor #2）\n4. **Missing references: Geifman & El-Yaniv (2017)**（R1-M6 ≈ R2 missing references #1）\n\n**我提出但 R1 未提出的问题：**\n1. **R2-N1（核心概念新颖性不足）**: R1 未质疑 \"correlation-selection gap\" 的 novelty，反而在 Excitement 上给了 3.5/5。我认为这是我们最大的分歧点——我认为 gap 的核心解释（instance-level signals can't rank by definition）是 definitional 而非 discovered，R1 似乎认为系统性的 empirical documentation 本身构成 sufficient contribution。\n2. **R2-N2（任务覆盖面不足以支撑 title claims）**: R1 未质疑 \"Structured IE\" 的泛化范围。\n3. **R2-N3（模型规模范围不足）**: R1 未将此列为 critical issue。\n4. **R2-W1（framework 缺乏预测力的循环性）**: R1 的 Q1 触及了这个问题但未将其升级为 weakness。\n\n---\n\n### 我与 R1 的评分差异分析\n\n| 维度 | R1 | R2 | 差异原因 |\n|------|----|----|----------|\n| Overall | 3.5 | 2.5 | 我对 novelty 的要求更高；R1 认为 empirical documentation 的深度足以构成 contribution，我认为需要更深的 conceptual insight |\n| Excitement | 3.5 | 2.0 | 最大分歧。R1 可能更看重 practical relevance（negative result 对 practitioners 有价值），我更看重 intellectual novelty（core insight is definitional） |\n| Soundness | 3.5 | 3.5 | 一致 |\n\n我维持我的评分。核心分歧是 novelty 标准：R1-W2 指出 \"jointly necessary\" 的因果 claim 过强，如果 downgrade 为 \"associated\"，论文的 contribution 进一步从 \"framework discovery\" 降为 \"empirical observation\"，这在我看来更接近 Findings 而非 main conference。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-18T06:12:50.989120+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4116
}
```

</details>

---


### Assistant

_source line 1594 · 2026-05-18T06:12:59.541829+00:00_

交叉回应已提交。

逐条回应了 R1 的 7 个 Weaknesses 和 5 个 Questions：
- **6 个 AGREE**（W1-W7 中 6 个 + Q1/Q2/Q4）：epoch confound、因果 claim 过强、2-seed 不足、per-entity non-independence、verifier 命名、degeneracy 定义、数值不一致
- **2 个 REBUT**（Q3 greedy baseline、Q5 N-scaling 外推）：greedy 作为 selection baseline 是合理的（beam search 属于不同范畴）；N-scaling 外推即使显著也 practical significance 极低

最大分歧在 Excitement 维度：R1 给 3.5，我给 2.0。我认为核心 insight（instance-level signals can't rank by definition）是 definitional 而非 discovered，R1 更看重 empirical documentation 的系统性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 42

## Round 42

102 recorded events


### User

_source line 1595 · 2026-05-18T12:47:16.307759+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性）

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

**重点审查新颖性、完整性、Related Work 和写作质量**，具体包括：

1. **新颖性和贡献增量**：
   - "correlation-selection gap" 概念是否是真正的新贡献？还是已有工作（如 Eikema et al. 2025 MBR utility misalignment, Yao et al. 2026 consistency for NER）的增量？
   - "instance degeneracy" 和 "LP compression" 作为两个机制的诊断价值如何？是否只是对已知现象的重新命名？
   - 论文的 framing（"strong predictors, weak selectors"）是否准确反映了实验发现？
   - 实际的 positive contribution 是什么？主要发现是 negative result（大多数信号不能改善 selection），EMNLP 是否接受这种类型的贡献？

2. **Related Work 覆盖度**：
   - 是否遗漏了重要的直接相关工作？
   - Self-consistency 系列论文、MBR decoding、uncertainty estimation 等类别的覆盖是否充分？
   - 与 Yao et al. (2026) 的区分是否清晰？（他们研究 NER/RE 的 consistency-accuracy correlation，本文的增量是什么？）
   - NER 领域的 calibration/confidence estimation 工作是否被充分讨论？

3. **叙事结构和主线统一性**：
   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线？
   - 论文标题和 framing 是否与实验发现一致？
   - "capability trap" 的论述是否有足够的证据支持，还是过度推广？
   - DALS 方法在 Discussion 中引入是否影响论文的"诊断性"定位？

4. **写作质量**：
   - 是否存在 AI 写作痕迹（解释性 em-dash、-ing 结尾短语、过度分段、"Furthermore/Moreover" 堆砌）？
   - 专有名词是否在首次出现时定义？
   - 图表知识密度如何？Caption 是否自包含？
   - 脚注数量是否过多？（注意 Table 3 似乎有大量脚注）

5. **格式合规性**：
   - 正文是否符合 ≤8 页限制？
   - Limitations section 是否按要求放置？
   - 参考文献格式是否一致？
   - 匿名化是否彻底（检查是否泄露作者身份）？

6. **Limitations 和 Ethics Statement**：
   - Limitations 是否诚实、全面？
   - Ethics Statement 是否充分？

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1596 · 2026-05-18T12:47:36.749468+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-18T12:47:36.749883+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-18T12:47:40.214631+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1599 · 2026-05-18T12:47:41.875957+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1600 · 2026-05-18T12:47:42.026755+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1601 · 2026-05-18T12:47:42.127606+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1602 · 2026-05-18T12:47:42.128069+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-18T12:47:48.199811+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

Reviewers should read the paper and get a first impression, then search for related work without deliberately try
…[truncated 1574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7985
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-18T12:47:53.019349+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1605 · 2026-05-18T12:47:53.069871+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1606 · 2026-05-18T12:47:57.285258+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. I need the exact criteria for: Overall Assessment, Soundness, Excitement, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. I need the exact criteria for: Overall Assessment, Soundness, Excitement, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1607 · 2026-05-18T12:47:58.239203+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-10",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-10",
    "dpi": "180"
  }
}
```

</details>

---


### Tool call

_source line 1608 · 2026-05-18T12:47:58.690940+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1609 · 2026-05-18T12:47:59.192988+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-18T12:47:59.644765+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool call

_source line 1611 · 2026-05-18T12:48:00.146574+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1612 · 2026-05-18T12:48:04.464745+00:00_

# ACL ARR Review Form Scoring Dimensions

## Overall Assessment
**Scale:** 1-5 (with .5 increments)
- **5:** "Consider for Award: I think this paper could be considered for an outstanding paper award" (top 2.5%)
- **4:** Conference acceptance recommended
- **3:** "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2:** Needs substantial revisions for next cycle
- **1:** "Do not resubmit: This paper has to be fully redone, or it is not relevant"

## Soundness
**Scale:** 1-5 (with .5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type"
- **4:** "Strong: This study provides sufficient support for all of its claims"
- **3:** "Acceptable: This study provides sufficient support for its main claims"
- **2:** "Poor: Some of the main claims are not sufficiently supported"
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale:** 1-5 (with .5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend"
- **3:** "Interesting: I might mention some points of this paper to others"
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others"
- **1:** "Not Exciting: this paper does not resonate with me"

## Reviewer Confidence
**Scale:** 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully"
- **4:** "Quite sure. I tried to check the important points carefully"
- **3:** "Pretty sure, but there's a chance I missed something"
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1:** "Not my area, or paper is very hard to understand"

## Reproducibility
**Scale:** 1-5
- **5:** "They could easily reproduce the results"
- **4:** "They could mostly reproduce the results, but there may be some variation"

…[truncated 496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7179
}
```

</details>

---


### Tool result

_source line 1613 · 2026-05-18T12:48:08.215248+00:00_

Error: result (8,037,206 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/mcp-agent-ml-research-pdf_to_images-1779108487897.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/mcp-agent-ml-research-pdf_to_images-1779108487897.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9976
}
```

</details>

---


### Tool result

_source line 1614 · 2026-05-18T12:48:08.215648+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9524
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-18T12:48:08.215912+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8069
}
```

</details>

---


### Tool result

_source line 1616 · 2026-05-18T12:48:08.216120+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8571
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-18T12:48:08.216380+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9023
}
```

</details>

---


### Tool call

_source line 1618 · 2026-05-18T12:48:14.263772+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-18T12:48:14.615104+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-18T12:48:14.665864+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-18T12:48:15.117547+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-18T12:48:15.117880+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-18T12:48:15.620286+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-18T12:48:15.671041+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-18T12:48:16.172749+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-18T12:48:16.173119+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-18T12:48:16.775105+00:00_

File content (35940 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 601
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-18T12:48:16.825639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-18T12:48:17.077471+00:00_

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
…[truncated 25702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-18T12:48:26.125758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-18T12:48:26.628430+00:00_

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
…[truncated 21524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-18T12:48:27.135675+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-4",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-4",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1633 · 2026-05-18T12:48:28.772058+00:00_

Error: result (2,589,539 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/mcp-agent-ml-research-pdf_to_images-1779108508694.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/mcp-agent-ml-research-pdf_to_images-1779108508694.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1636
}
```

</details>

---


### Tool call

_source line 1634 · 2026-05-18T12:48:37.409489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "300",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "300",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-18T12:48:38.313030+00:00_

300	\smallskip
301	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
302	\end{table}
303	
304	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
305	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
306	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
307	
308	\section{Diversity and Selection Analysis}\label{app:diversity}
309	
310	\begin{figure*}[t]
311	\centering
312	\includegraphics[width=\textwidth]{fig_selection_gap}
313	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
314	\label{fig:selection_gap}
315	\end{figure*}
316	
317	\paragraph{Output diversity quantification.}
318	Table~\ref{tab:diversity} summarizes output diversity across configurations.
319	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
320	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
321	On CoNLL, diversity collapses: 59\% (Qwen) to 89\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 alre
…[truncated 20966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-18T12:48:38.463942+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-18T12:48:38.664976+00:00_

Pages:           32
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-18T12:48:46.758549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "600",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "600",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1639 · 2026-05-18T12:48:46.759253+00:00_

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
631	\paragraph{Within-instance LP-quality alignment.}\label{app:within_instance_rho}
632	
633	Table~\ref{tab:within_rho} reports median within-instance $\rho(\text{LP}, \text{F1})$ across datasets, computed over non-degenerate instances (those with ${\geq}2$ distinct F1 values across $N{=}8$ samples).
634	Few-NERD exhibits substantially stronger alignment ($\rho{=}0.667$) than SciERC ($\rho{=}0.262$), directly explaining why LP selection succeeds only on Few-NERD.
635	CoNLL alignment is moderate ($\rho{\approx}0.51$), but the valid-instance fraction is low (41\% for Qwen, 11\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.
636	This pattern provides the most direct evidence that both conditions (low degeneracy \textit{and} adequate alignment) are independently required.
6
…[truncated 16730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1640 · 2026-05-18T12:48:47.563282+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1641 · 2026-05-18T12:49:53.285859+00:00_

&lt;persisted-output>
Output too large (53.3KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/toolu_01ApzJhh2EvGwAZWr5fj6b3Y.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 64, \"total_citations\": 97, \"unique_cited_keys\": 64, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 57, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, .
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 65722
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-18T12:50:03.675783+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/toolu_01ApzJhh2EvGwAZWr5fj6b3Y.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])['data']\nprint('=== Summary ===')\nprint(json.dumps(result['summary'], indent=2))\nprint()\nprint('=== Not Found ===')\nfor v in result['online_verification']:\n    if v.get('status') == 'not_found':\n        print(f\\\"  {v['key']}: {v.get('bib_title', 'N/A')}\\\")\nprint()\nprint('=== Mismatch ===')\nfor v in result['online_verification']:\n    if v.get('status') == 'mismatch':\n        print(f\\\"  {v['key']}: bib='{v.get('bib_title', '')}' vs found='{v.get('found_title', '')}'\\\")\n\"\n",
  "description": "Extract reference verification summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/toolu_01ApzJhh2EvGwAZWr5fj6b3Y.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])['data']\nprint('=== Summary ===')\nprint(json.dumps(result['summary'], indent=2))\nprint()\nprint('=== Not Found ===')\nfor v in result['online_verification']:\n    if v.get('status') == 'not_found':\n        print(f\\\"  {v['key']}: {v.get('bib_title', 'N/A')}\\\")\nprint()\nprint('=== Mismatch ===')\nfor v in result['online_verification']:\n    if v.get('status') == 'mismatch':\n        print(f\\\"  {v['key']}: bib='{v.get('bib_title', '')}' vs found='{v.get('found_title', '')}'\\\")\n\"\n",
    "description": "Extract reference verification summary"
  }
}
```

</details>

---


### Tool result

_source line 1643 · 2026-05-18T12:50:04.479762+00:00_

=== Summary ===
{
  "total_bib_entries": 64,
  "total_citations": 97,
  "unique_cited_keys": 64,
  "orphan_bib": 0,
  "missing_bib": 0,
  "duplicate_keys": 0,
  "online_verified": 57,
  "online_not_found": 3,
  "online_mismatch": 4
}

=== Not Found ===
  hobelsberger2025systematic: N/A
  lightman2024verify: N/A
  venktesh2025trust: N/A

=== Mismatch ===
  feng2025optimal: bib='' vs found=''
  snell2025scaling: bib='' vs found=''
  muller2021understanding: bib='' vs found=''
  park2024grammar: bib='' vs found=''

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-18T12:50:04.530270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "900",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "900",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-18T12:50:04.580968+00:00_

900	\begin{tabular}{lcccc}
901	\toprule
902	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
903	\midrule
904	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
905	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
906	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
907	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
908	\bottomrule
909	\end{tabular}
910	\end{table}
911	
912	\paragraph{Flip instances.}
913	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
914	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
915	
916	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
917	
918	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
919	
920	\begin{table}[t]
921	\centering
922	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
923	\label{tab:n-scaling}
924	\small
925	\begin{tabular}{l ccc ccc}
926	\toprule
927	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
928	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
929	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
930	\midrule
931	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
932	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
933	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
934	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
935	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
936	\midrule
937	
…[truncated 18824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-18T12:50:11.102917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-18T12:50:11.554880+00:00_

1200	\small
1201	\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
1202	\label{tab:fewnerd_full}
1203	\begin{tabular}{lcccc}
1204	\toprule
1205	Signal & $\rho$ & Sample AUROC & Sel.\ $\Delta$ & 95\% CI \\
1206	\midrule
1207	LP & .421 & .578 & $\mathbf{+1.39}$\,pp & [+1.18, +1.53] \\
1208	VC & .386 & --- & $-$1.79\,pp & --- \\
1209	FK & .313 & --- & $-$2.26\,pp & --- \\
1210	SJ & .300 & --- & $-$2.14\,pp & --- \\
1211	EM & .287 & --- & $-$3.85\,pp & --- \\
1212	\midrule
1213	\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
1214	\bottomrule
1215	\end{tabular}
1216	\end{table}
1217	
1218	\paragraph{Key observations.}
1219	(1)~All five signals achieve positive QE ($\rho$ 0.29--0.42); quality estimation works on Few-NERD. LP leads ($\rho{=}0.42$), followed by VC ($0.39$); the ranking differs from SciERC where VC leads, consistent with dataset-specific signal informativeness.
1220	(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.
1221	(3)~Despite positive $\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.
1222	(4)~Low degeneracy (13.8\%) combined with strong LP-quality alignment ($\rho{\approx}0.5$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (17.8\% degeneracy but weak alignment $\rho{\approx}0.24$, LP $+0.61$~pp) and CoNLL (59.1\%, LP $-0.85$~pp).
1223	
1224	\section{Per-Entity-Type LP Sel
…[truncated 11891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-18T12:50:11.907300+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1649 · 2026-05-18T12:50:12.812945+00:00_

Error: result (643,133 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/mcp-agent-ml-research-pdf_to_images-1779108612754.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f6b59758-6be5-4cc1-a302-408ad8e257c7/tool-results/mcp-agent-ml-research-pdf_to_images-1779108612754.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1650 · 2026-05-18T12:50:26.419398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdftotext main.pdf - 2>/dev/null | grep -n \"Limitations\\|Ethics Statement\\|References\\|\\\\\\\\bibliography\" | head -20",
  "description": "Find where Limitations/References start in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdftotext main.pdf - 2>/dev/null | grep -n \"Limitations\\|Ethics Statement\\|References\\|\\\\\\\\bibliography\" | head -20",
    "description": "Find where Limitations/References start in PDF"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-18T12:50:26.921399+00:00_

1925:Limitations
2005:Ethics Statement
2074:References
4673:See §4.1 and Limitations for discussion of this confound.
7512:Limitations. The Few-NERD epoch analysis
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-18T12:50:33.499908+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\nlines = text.split('\\n')\n# Find page breaks (form feed characters)\npages = text.split('\\f')\nprint(f'Total pages: {len(pages)}')\n# Find which page Limitations is on\nfor i, page in enumerate(pages):\n    if 'Limitations' in page and i < 15:\n        print(f'Page {i+1} contains Limitations')\n    if 'Ethics Statement' in page and i < 15:\n        print(f'Page {i+1} contains Ethics Statement')\n    if 'References' in page and i < 15:\n        # Check if it's the References section header\n        if page.strip().count('References') > 0:\n            first_ref_line = [l for l in page.split('\\n') if 'References' in l]\n            if first_ref_line:\n                print(f'Page {i+1} contains References section')\n\"\n",
  "description": "Identify page numbers for main sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\nlines = text.split('\\n')\n# Find page breaks (form feed characters)\npages = text.split('\\f')\nprint(f'Total pages: {len(pages)}')\n# Find which page Limitations is on\nfor i, page in enumerate(pages):\n    if 'Limitations' in page and i < 15:\n        print(f'Page {i+1} contains Limitations')\n    if 'Ethics Statement' in page and i < 15:\n        print(f'Page {i+1} contains Ethics Statement')\n    if 'References' in page and i < 15:\n        # Check if it's the References section header\n        if page.strip().count('References') > 0:\n            first_ref_line = [l for l in page.split('\\n') if 'References' in l]\n            if first_ref_line:\n                print(f'Page {i+1} contains References section')\n\"\n",
    "description": "Identify page numbers for main sections"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-18T12:50:34.052653+00:00_

Total pages: 33
Page 10 contains Limitations
Page 10 contains Ethics Statement
Page 11 contains References section
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-18T12:50:44.350280+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages[:12]):\n    if 'Conclusion' in page:\n        lines_with_conclusion = [l.strip() for l in page.split('\\n') if 'Conclusion' in l]\n        print(f'Page {i+1}: {lines_with_conclusion}')\n    if 'Limitations' in page and i < 12:\n        lines_with_lim = [l.strip() for l in page.split('\\n') if 'Limitations' in l]\n        print(f'Page {i+1} Limitations: {lines_with_lim[:3]}')\n# Check page 9 content end\nprint()\nprint('=== Page 9 last 10 lines ===')\np9_lines = pages[8].strip().split('\\n')\nfor l in p9_lines[-10:]:\n    print(l)\nprint()\nprint('=== Page 10 first 10 lines ===')\np10_lines = pages[9].strip().split('\\n')\nfor l in p10_lines[:10]:\n    print(l)\n\"\n",
  "description": "Check Conclusion and Limitations page boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages[:12]):\n    if 'Conclusion' in page:\n        lines_with_conclusion = [l.strip() for l in page.split('\\n') if 'Conclusion' in l]\n        print(f'Page {i+1}: {lines_with_conclusion}')\n    if 'Limitations' in page and i < 12:\n        lines_with_lim = [l.strip() for l in page.split('\\n') if 'Limitations' in l]\n        print(f'Page {i+1} Limitations: {lines_with_lim[:3]}')\n# Check page 9 content end\nprint()\nprint('=== Page 9 last 10 lines ===')\np9_lines = pages[8].strip().split('\\n')\nfor l in p9_lines[-10:]:\n    print(l)\nprint()\nprint('=== Page 10 first 10 lines ===')\np10_lines = pages[9].strip().split('\\n')\nfor l in p10_lines[:10]:\n    print(l)\n\"\n",
    "description": "Check Conclusion and Limitations page boundaries"
  }
}
```

</details>

---


### Tool result

_source line 1655 · 2026-05-18T12:50:44.851969+00:00_

Page 9: ['6   Conclusion                                          686']
Page 10 Limitations: ['723   Limitations                                                  untested. Other per-sample scoring methods exist         774']

=== Page 9 last 10 lines ===
642   2023; Snell et al., 2025); for structured IE, the same       selective prediction. For selection, LP achieves        692
643   training progress that reduces error also reduces the        +1.39 pp on Few-NERD (p<0.001) when two                 693
644   output diversity on which selection depends. The             conditions are jointly satisfied: low instance de-      694
645   sole per-sample signal that carries information (LP)         generacy (<15%) and adequate LP-quality align-          695
646   is the one most vulnerable to high-confidence com-           ment (ρ ≳ 0.3, approximate threshold from our           696
647   pression (median range 0.041 nats). This pattern is          data); gains scale with sample budget (+0.52 pp,        697
648   observational (3 scale points, 2 model families, 3           N =8→16, p=0.003). When either condition is             698


                                                               9

=== Page 10 first 10 lines ===
699   violated, LP gains fall below detectable thresholds          sample signal; it exhibits severe overconfidence         749
700   despite 12–14 pp oracle headroom: on SciERC                  (mean 8.58/10 on SciERC, 9.24/10 on CoNLL)               750
701   (17.8% degeneracy, ρ≈0.24), LP yields +0.61 pp               and yields the weakest QE and selection among all        751
702   (below the ≈1.5 pp MDE at 80% power); on                     signals (Appendix U). Ad-hoc LP×VC combina-              752
703   CoNLL (59.1% degeneracy), LP degrades selec-                 tions yield at most +0.2 pp over greedy (not sig-        753
704   tion (−0.85 pp). Two mechanisms explain this                 nificant; §5); whether learned combinations could 
…[truncated 669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-18T12:51:37.312963+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && grep -rn \"—\" sections/*.tex | head -30",
  "description": "Check for em-dash usage in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && grep -rn \"—\" sections/*.tex | head -30",
    "description": "Check for em-dash usage in paper"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-18T12:51:37.413688+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-18T12:51:38.016321+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && grep -rn \" – \" sections/*.tex | head -20",
  "description": "Check for en-dash usage in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && grep -rn \" – \" sections/*.tex | head -20",
    "description": "Check for en-dash usage in paper"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-18T12:51:38.869126+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 852
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-18T12:51:38.970294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && grep -rn \"Furthermore\\|Moreover\\|Additionally\\|Notably\\|It is worth noting\" sections/*.tex | head -20",
  "description": "Check for AI transition word patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && grep -rn \"Furthermore\\|Moreover\\|Additionally\\|Notably\\|It is worth noting\" sections/*.tex | head -20",
    "description": "Check for AI transition word patterns"
  }
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-18T12:51:39.020891+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-18T12:51:43.487088+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-18T12:51:44.089040+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 601
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-18T12:51:44.565710+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-18T12:51:45.067803+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1666 · 2026-05-18T12:51:45.620055+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (highlighting|demonstrating|indicating|suggesting|revealing|showcasing|underscoring)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (highlighting|demonstrating|indicating|suggesting|revealing|showcasing|underscoring)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1667 · 2026-05-18T12:51:45.720746+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:183:DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds), indicating moderate quality prediction but poor selection utility: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:20:Hidden state probes confirm richer information exists in model representations (SciERC MLP $\rho{=}0.388$ vs.\ LP $0.283$, $+37$\%), but the correlation-selection gap persists: MLP selection F1 falls below LP's (gap closure $-5.1$\% vs.\ $+4.8$\%; \S\ref{sec:hidden_probe}), indicating the bottleneck in the high-capability regime is not information loss but diminishing marginal returns on selection.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:18:Both mechanisms intensify with model capability: degeneracy rises with scale and training convergence (\S\ref{sec:discussion}), revealing a tension between model quality and test-time improvability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1668 · 2026-05-18T12:51:51.540561+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\footnote",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\footnote",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 1669 · 2026-05-18T12:51:51.992001+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:16
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:3
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:7

Found 26 total occurrences across 3 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-18T12:51:52.493464+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\footnotemark|\\\\footnotetext",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\footnotemark|\\\\footnotetext",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1671 · 2026-05-18T12:51:52.544035+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:101:\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). $p$: paired bootstrap ($n{=}10{,}000$) vs.\ greedy.\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:114:\footnotetext{Oracle headroom: 4.0~pp (CoNLL), 13.2~pp (SciERC), 12.4~pp (Few-NERD).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:115:\footnotetext{SciERC values (greedy${=}0.644$, headroom${=}13.2$~pp) differ slightly from Table~\ref{tab:selection} (greedy${=}0.645$, headroom${=}13.3$~pp) due to max-LP aggregation and single-seed evaluation; the ranking is unchanged.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:116:\footnotetext{Instance degeneracy: fraction of gold-filtered instances where all $N$ samples produce identical instance-level F1.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:117:\footnotetext{Few-NERD uses 3-epoch checkpoints (early stopping); SciERC and CoNLL use 5 epochs. A 5-epoch Few-NERD control confirms LP selection remains positive though gains are halved (Appendix~\ref{app:epoch_confound}).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:118:\footnotetext{SciERC LP $\Delta$ is single-seed (seed${=}42$); 3-seed mean: $+0.04{\pm}0.48$~pp, reflecting high seed sensitivity at this sample size ($n{=}529$).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:119:\footnotetext{Few-NERD LP $\Del
…[truncated 1789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-18T12:52:17.017900+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp_0|github|anonymized|http|url",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp_0|github|anonymized|http|url",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 1673 · 2026-05-18T12:52:17.068545+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1674 · 2026-05-18T12:52:20.619667+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp_0|github|anonymized|http|url",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp_0|github|anonymized|http|url",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1675 · 2026-05-18T12:52:20.670227+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex:44:Code and data will be released upon acceptance at [anonymized URL].

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1676 · 2026-05-18T12:52:24.633308+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp_025|exp\\_025",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp_025|exp\\_025",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-18T12:52:24.683888+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1678 · 2026-05-18T12:52:28.454279+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp.025",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp.025",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-18T12:52:28.554988+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1680 · 2026-05-18T12:52:32.366298+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "head_limit": "5",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "head_limit": "5",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1681 · 2026-05-18T12:52:32.467105+00:00_

157:Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
231:On CoNLL, 59--89\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
349:This rules out insufficient diversity as an explanation for the correlation-selection gap.
491:\texttt{System:} You are an expert in Named Entity Recognition.\\
500:[Omitted long matching line]

[Showing results with pagination = limit: 5]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1682 · 2026-05-18T12:52:35.875267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "993",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "993",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 1683 · 2026-05-18T12:52:35.925712+00:00_

993	\centering
994	\small
995	\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\_025).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
996	\label{tab:n_scaling_selection}
997	\begin{tabular}{ccccccccc}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1684 · 2026-05-18T12:52:41.343764+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp\\\\_\\\\d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp\\\\_\\\\d",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1685 · 2026-05-18T12:52:41.344097+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1686 · 2026-05-18T12:52:45.630724+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp_",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp_",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1687 · 2026-05-18T12:52:45.731506+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1688 · 2026-05-18T12:52:49.092691+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"exp_\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "description": "Find internal experiment identifiers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"exp_\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "description": "Find internal experiment identifiers"
  }
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-18T12:52:49.145306+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-18T12:52:53.159212+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'exp\\\\\\\\\\_' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "description": "Find escaped experiment identifiers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'exp\\\\\\\\\\_' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "description": "Find escaped experiment identifiers"
  }
}
```

</details>

---


### Tool result

_source line 1691 · 2026-05-18T12:52:53.209807+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1692 · 2026-05-18T12:52:56.873501+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -Pn 'exp\\\\_' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "description": "Find LaTeX-escaped experiment identifiers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -Pn 'exp\\\\_' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "description": "Find LaTeX-escaped experiment identifiers"
  }
}
```

</details>

---


### Tool result

_source line 1693 · 2026-05-18T12:52:56.974217+00:00_

995:\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\_025).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
1336:\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$). Evaluated on the exp\_027 5K subsample (gold-filtered $n{=}4{,}351$); main-table results (Table~\ref{tab:fewnerd}) use the full test set ($n{=}32{,}565$, gold-filtered), yielding slightly different degeneracy (13.8\% vs.\ 11.1\% here). ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``Valid'': fraction of instances with non-degenerate outputs. ``$\rho$ mean/med'': within-instance LP-quality correlation. The 3-epoch model corresponds to standard early stopping; the 5-epoch model is a controlled ablation.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-18T12:55:47.109274+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**审稿侧重**：新颖性、完整性、Related Work、写作质量\n\n---\n\n## Summary\n\n本文研究为什么在 NER 任务中有效的 quality estimation 信号（Spearman ρ 达 0.45, AUROC 达 0.82）无法转化为 best-of-N sample selection 增益。通过在 4 个 NER benchmark、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）和 1 个 4B ablation 上评估 5 种 confidence signals，作者诊断出两个阻塞机制：instance degeneracy（14–59% 实例所有样本产生相同 F1）和 weak LP-quality alignment。唯一取得显著 selection 增益的条件是 Few-NERD 上 LP（+1.39pp, p<0.001），需要 degeneracy <15% 且 alignment ρ≈0.5 两个条件同时满足。论文还通过 hidden state probes 证明即使模型内部表示包含更丰富的信息（ρ=0.388 vs. LP 0.283），correlation-selection gap 依然存在。\n\n---\n\n## Strengths\n\n**S1** [实验设计全面] 4 个 NER 数据集构成清晰的难度梯度（WNUT-17 signal collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个数据集服务于明确的实验角色。5 种信号覆盖 structural/surface/model-internal 三个家族。多种 ablation（temperature, LoRA rank, epoch, N-scaling, free-form decoding）系统地隔离变量。\n\n**S2** [统计严谨性] 论文在统计方法上表现出色：bootstrap CI（B=10,000）、TOST equivalence testing（含 external anchors 修正 circularity）、MDE 计算（明确指出 SciERC n=529 的 power limitation）、多重比较校正（Bonferroni）。Non-tied subset 的 sole positive finding（+2.9pp, p=0.004）经 Bonferroni 校正后仍然 significant——这种严谨性在同类工作中少见。\n\n**S3** [per-sample vs. instance-level 区分] 将 5 种信号明确分为 instance-level（4 种，对 selection 无信息量 by construction）和 per-sample（仅 LP）是一个重要的概念贡献。这个区分解释了为什么 structural signals 在 QE 上强但 selection 上弱，比简单报告\"没有信号有效\"更有洞察力。\n\n**S4** [Hidden state probes 扩展] Section 5.6 的 hidden state probe 实验直接测试了\"是否更丰富的信号能改善 selection\"这一自然后续问题。MLP probe ρ=0.388（比 LP 高 37%）但 selection 反而更差（gap closure -5.1% vs. +4.8%），有力地证明了 bottleneck 不在 information 而在 diminishing marginal returns。\n\n**S5** [Limitations 诚实全面] Limitations section 和 appendix 中对各种 confounds 的讨论（thinking token, epoch confound, SciERC seed sensitivity）非常透明，主动报告了所有已知的弱点。\n\n---\n\n## Weaknesses\n\n**W1** [Critical] **正文页数超限**\n通过 PDF 分析，Conclusion（Section 6）从第 9 页开始并延续到第 10 页，Limitations 也在第 10 页。ACL 长文限制为 ≤8 页正文（不含 Limitations/Ethics/References）。主体内容约 9.5 页，超出限制约 1.5 页。这是 desk-reject 级别的问题。\n\n- 主要来源：Discussion（Section 5）过长，包含多个可移至 appendix 的段落（LP compression mechanisms, regime boundaries 的详细数值、DALS 方法介绍）。\n- 建议：将 DALS 段落完整移至 appendix；压缩 \"regime boundaries\" 段落为 2–3 句总结性陈述并 refer appendix；将 \"LP compression mechanisms\" 的 4 个机制列表移至 appendix，正文仅保留结论。\n\n**W2** [Major] **新颖性增量有限**\n论文的核心贡献是一个 diagnostic negative result + 两个命名概念。逐一评估：\n\n(a) **Correlation-selection gap**：correlation 不意味着 selection utility 是 MBR 文献中的已知问题。Eikema et al. (2025) 的 MBR utility misalignment 和本文的 diagnosis 是 complementary 的（论文承认这点，Introduction line 16），但\"对已知现象在新 domain 中的验证\"的新颖性阈值较低。\n\n(b) **Instance degeneracy**：fine-tuned models + constrained decoding 产生低多样性输出是可预测的结果。Kirk et al. (2024) 讨论了 RLHF 下的 diversity collapse，Yun et al. (2025) 讨论了 format constraints 下的 diversity collapse。将这些现象量化并命名为 \"instance degeneracy\" 有一定 diagnostic 价值，但不构成方法论创新。\n\n(c) **Capability trap**：基于 3 个 scale points（3B, 4B, 8B）、2 个 model families、3 个 convergence levels 的 observational evidence，论文正确指出\"does not establish causality\"（Discussion line 46）。但 \"capability trap\" 这一术语暗示了比证据支撑更强的普遍性。在 70B+ 模型上，更强的表达能力可能同时减少 degeneracy 和改善 alignment，逆转当前趋势。\n\n(d) **与 Yao et al. (2026) 的区分**：论文声称 Yao et al. 只展示了 correlation 而自己诊断了 why correlation 不 translate to selection。这个定位是合理的，但 Yao et al. 用 hard-prompting（非 fine-tuning），degeneracy 可能天然更低，两者的实验设置差异限制了直接增量比较。\n\n对于 EMNLP 而言：negative/diagnostic results 是被接受的，但需要 (i) 足够的覆盖度证明 negative result 的 robustness，(ii) 有意义的 actionable insight。条件 (i) 满足良好（多数据集、多模型、多 ablation）。条件 (ii) 部分满足：QE 的 practical guidelines 有价值，但 selection 方面的 actionable output 有限（DALS 增益微弱且 seed-sensitive）。\n\n**W3** [Major] **DALS 定位混乱**\nDiscussion 中引入的 DALS（Degeneracy-Aware LP Selection）方法与论文的\"诊断性\"定位产生冲突：\n- 如果这是诊断论文：DALS 应在 appendix 中作为 exploratory extension\n- 如果 DALS 是核心贡献：应在 Method section 中正式定义，有独立的实验表格，并在 contribution list 中列出\n\n当前 DALS 的结果是 seed-sensitive 的（SciERC: +0.19 to +1.14pp across seeds），且在 CoNLL 上仍然 degradation（-0.87pp）。将一个如此 preliminary 的方法放在 Discussion 中会造成 contribution 边界模糊。\n\n**W4** [Major] **Table 3（tab:fewnerd）的 7 个连续脚注**\nTable 3 caption 中使用了 `\\protect\\footnotemark` 7 次，产生 7 个连续的脚注文本。这严重损害可读性：审稿人需要在表格和页底之间反复跳转，且脚注内容（oracle headroom、greedy F1 差异、degeneracy 定义、epoch difference、seed details ×3）混合了定义性信息和技术 caveat。\n\n建议：将 degeneracy 定义移至首次使用处（Section 3/4）；将 3-seed details 移至 appendix table 或正文段落；将 SciERC greedy F1 差异解释整合到一个 \"notation note\" 中。最终 Table 3 的脚注应不超过 2 个。\n\n**W5** [Major] **SciERC 作为 primary test bed 统计 power 不足**\nSciERC 有 n=529（gold-filtered），论文自己计算 MDE≈1.5pp at 80% power。然而论文声称 LP 在 SciERC 上的 +0.61pp \"falls below detectable thresholds\"（Table 3）——这意味着在 primary test bed 上无法区分 \"真的没有效果\" 和 \"效果太小检测不出来\"。\n\nFew-NERD（n=32,565, MDE≈0.22pp）才是真正有 definitive power 的数据集。建议重新定位：将 Few-NERD 作为 primary test bed（LP selection 的 definitive positive evidence），SciERC 作为 \"medium-difficulty, underpowered\" secondary test bed。当前的叙事结构（SciERC 为主 → Few-NERD 为 contrast）弱化了论文最强的实证结果。\n\n**W6** [Minor] **Greedy F1 数值不一致**\nSciERC 的 greedy F1 在不同表格中出现多个值：0.640（Table N-scaling）、0.644（Table 3 / fewnerd）、0.645（Table 2 / selection）、0.650（Table hidden_probe, epoch 3-epoch）。虽然每个差异都有脚注解释（seed 差异、aggregation 差异、gold-filtering），但审稿人看到同一 baseline 有 4 个不同数值会产生困惑和不信任感。\n\n建议：统一所有表格的 evaluation protocol（相同 seed、相同 filtering、相同 aggregation），或在 Methods section 中明确声明各表格使用的协议差异并给出原因。\n\n**W7** [Minor] **Appendix 中残留内部实验标识**\nAppendix Table~\\ref{tab:n_scaling_selection} caption 含 \"exp\\_025\"，Table~\\ref{tab:epoch_confound} caption 含 \"exp\\_027\"。这些是内部实验管理系统的标识符，应在投稿前删除。虽然不直接泄露作者身份，但显得不够 professional。\n\n**W8** [Minor] **\"Capability trap\" 措辞的 framing 风险**\n\"Trap\" 一词暗示了不可逃脱的困境。但论文自己展示了 temperature 和 early stopping 可以部分控制 degeneracy；更大规模模型（70B+）的行为完全未知。\"Capability-diversity tension\" 或 \"capability-selection tradeoff\" 是更准确的描述。\n\n---\n\n## Questions\n\n**Q1** Few-NERD 使用 3 epochs 而 SciERC/CoNLL 使用 5 epochs（Table 3 脚注 4）。5-epoch Few-NERD control 的 degeneracy 上升到 31% 且 LP 增益减半。那么 SciERC 在 3 epochs 时 degeneracy 仅 6.4%（Table epoch_scierc），为什么不将 3-epoch SciERC 作为 primary checkpoint？这似乎能产生更有信息量的 comparison with Few-NERD。\n\n**Q2** Hidden state probe 使用 mean-pooled final-layer hidden state。是否尝试过：(a) entity span 位置的 hidden states，(b) 多层 pooling，(c) attention-weighted pooling？Mean pooling 可能丢失了与 NER 最相关的 local information。\n\n**Q3** Per-entity-type analysis within Few-NERD（ρ=-0.881, p=0.004, n=8）被用作 degeneracy-selection 关系的 supporting evidence，但论文注意到 \"types share model and tokenizer, so effective degrees of freedom may be lower than 6\"。如果 effective df 更低，p-value 应该更大——这条证据线的可靠性如何？\n\n**Q4** 论文测试了 LP、VerbConf 和 hidden state probes 作为 per-sample signals，但没有测试 Self-Certainty (Kang et al. 2025) 和 P(True) (Kadavath et al. 2022)，两者都在 Limitations 中被提及。给出这些是 readily available 的 per-sample signals，为什么没有在实验中包含？\n\n**Q5** DALS 在 CoNLL 上仍然表现为 degradation（Qwen: -0.87pp）。如果 DALS 的 decision rule 需要 labeled development set 来估计 degeneracy 和 alignment，为什么不直接在 development set 上用 LP selection vs. greedy 的 paired test 来决定是否使用 LP selection？这个更简单的 approach 是否等价？\n\n---\n\n## Missing References\n\n1. **Semantic entropy** — Farquhar et al. (2024) \"Detecting Hallucinations in Large Language Models Using Semantic Entropy\" (Nature)。与 semantic uncertainty (Kuhn et al. 2023) 相关但不同；更直接涉及结构化输出的不确定性度量。\n\n2. **NER 特定的 calibration 工作** — Related Work 中 NER-specific confidence/calibration 仅引用了 pre-LLM 工作 (Culotta 2004, Mejer 2010)。近年 LLM-based NER 的 calibration 文献（如果存在）应被讨论。当前 Related Work 从 general confidence estimation surveys 直接跳到本文，缺少 NER-specific 中间层。\n\n3. **Best-of-N for code generation** — Chen et al. (2021) \"Evaluating Large Language Models Trained on Code\" (Codex paper) 和 Li et al. (2022) AlphaCode 都展示了 best-of-N 在 code generation 中的成功。当前仅引用 Shi et al. (2022) 的 execution-based MBR。更全面的 BoN 成功案例讨论能更好地 contextualize NER 的特殊困难。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 符合 4-question 结构（问题、重要性、方法、结果）。\n- \"four instance-level, one per-sample log-probability [LP]\" 中 \"LP\" 在 Abstract 中首次出现但未完整定义（log-probability 已给出，但 LP 作为缩写的显式定义不够明确）。\n- 信息密度适中，约 150 words。\n\n### Introduction (Section 1)\n- 叙事结构完整：background → existing conflation → our distinction → mechanisms → contributions。\n- Line 6 \"Unlike Yao et al. (2026)\" 的区分清晰且公平。\n- Contribution list 过长：contribution 2 有 4 行子句，contribution 3 有 3 行，各包含过多的数值细节。建议将数值 evidence 移到各 contribution 对应的 section 中，contribution list 仅保留概念性描述。\n- Figure 1 信息密度高且 caption 自包含。\n\n### Related Work (Section 2)\n- 结构清晰（4 个 paragraph），每类都有明确的 positioning。\n- \"We extend self-consistency to set-valued structured outputs\" 是合理的 positioning。\n- 与 Yao et al. (2026) 的区分到位：\"we show correlation is necessary but not sufficient\"。\n- 可以补充 NER-specific calibration 的更多讨论（见 Missing References）。\n\n### Method (Section 3)\n- 5 种 signal 的定义清楚，数学形式正确。\n- Per-sample vs. instance-level 的区分从 Section 3.1 就建立，贯穿全文。\n- SJ 的 normalizer robustness 在正文脚注中提及并 refer appendix，处理得当。\n- Evaluation framework（QE vs. Selection）定义清楚。\n\n### Experiments (Section 4)\n- Dataset 角色分配清晰（primary / low-degeneracy contrast / ceiling control / signal-collapse boundary）。\n- Table 1（QE results）格式清楚，但缺少 Few-NERD 和 WNUT-17 的数据（分散在 appendix 各处）。建议在正文中补充一个统一的 full-dataset QE 汇总表。\n- Table 2（selection results）有效传达了核心 negative finding。\n- Table 3 的脚注问题如 W4 所述。\n- Section 4.4（Robustness）混合了多个 ablation，段落之间缺乏明确的逻辑连接。\n- Section 4.5（Hidden state probes）是新颖的分析，值得肯定。\n\n### Discussion (Section 5)\n- 过长，是导致 W1（超页限）的主要原因。\n- \"LP compression mechanisms\" 段落列出 4 个机制但每个只用 1–2 句话，没有足够深度；适合 appendix。\n- \"Regime boundaries\" 段落试图给出 practical guidelines 但太详细（含完整的 decision rule 和数值条件）。\n- DALS 段落如 W3 所述定位不清。\n- \"Capability trap\" 段落的 framing 如 W8 所述略有过度。\n\n### Conclusion (Section 6)\n- 是 Introduction 和 Discussion 的有效总结，没有引入新信息。\n- 最后一句（\"the same progress that reduces error also reduces the diversity on which selection depends\"）是一个有力的结束。\n\n### Limitations\n- 非常全面，诚实地讨论了：scale gap, seed sensitivity, single-dataset RE, epoch confounds, untested signals (Self-Certainty, P(True)), ε threshold 的 post-hoc 性质。\n- 信息量过大——部分内容（如 verbalized confidence 的详细结果描述）更适合 appendix。\n\n### 写作质量\n- **AI 标志检查**：无 em-dash（—）使用；无 \"Furthermore/Moreover/Additionally\" 堆砌；仅 3 处 \"-ing\" 短语（\"indicating\" ×2, \"revealing\" ×1），均在可接受范围内。论文在 AI 写作痕迹控制方面做得很好。\n- **专有名词定义**：correlation-selection gap、instance degeneracy 在首次使用时有定义。LP、QE、MDE 等缩写的首次定义基本到位。DALS 在 Discussion 中首次出现并定义。\n- **段落结构**：整体合理，未出现过度分段。\n\n### 格式合规性\n- `\\usepackage[review]{acl}` — 正确。\n- Author: Anonymous — 正确。\n- 行号：review option 会自动生成 — 正确。\n- **正文超限** — 见 W1。\n- Appendix 中残留 \"exp\\_025\"、\"exp\\_027\" — 见 W7。\n- References 格式基本一致；verify_references 显示 64 条引用、0 orphan、0 missing、3 条 online not found（hobelsberger2025, lightman2024, venktesh2025——可能是 preprint 尚未被 OpenAlex 索引）、4 条 mismatch（可能是 title 变体）。\n\n---\n\n## Overall Assessment\n\n**Overall**: 2.5 / 5（介于 \"Resubmit next cycle\" 和 \"Findings\" 之间）\n\n**一句话总结**：一篇实验严谨、统计透明的诊断性研究，但正文超页限是 hard blocker，新颖性增量有限（主要是对已知现象在 NER 中的系统验证和命名），且 primary test bed 的统计 power 不足以区分 null effect 和 small effect。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计和统计方法优秀（S2），但 primary test bed power 不足（W5），greedy F1 不一致（W6），DALS 评估不充分（W3） |\n| Excitement | 2.5/5 | 诊断性 insight 有价值（S3, S4），但核心发现是 negative result 且 actionable output 有限；named concepts 的新颖性增量有限（W2） |\n| Reproducibility | 4/5 | Training config、prompt template、evaluation protocol 详细；代码承诺 release；appendix 极其全面。唯一扣分：greedy F1 多个数值的 protocol 差异增加复现难度 |\n| Confidence | 4/5 | 仔细阅读了全文和 appendix；NER evaluation 和 MBR/uncertainty estimation 是我的熟悉领域 |\n\n## Must-Fix 问题\n\n**N1** [critical] 正文超 8 页限制\n- 具体位置：Section 5 (Discussion) 和 Section 6 (Conclusion) 延伸到 page 10\n- 问题：ACL 长文 ≤8 页正文（不含 Limitations/Ethics/References）；当前约 9.5 页\n- 为什么影响接收：格式不合规可能导致 desk reject\n- 建议：压缩 Discussion（将 DALS、LP compression details、regime boundary numerics 移至 appendix），contribution list 精简数值\n\n## Should-Fix 问题\n\n**W1-ref** [warning] Table 3 的 7 个脚注\n- 具体位置：Section 4.3, Table~\\ref{tab:fewnerd}\n- 问题：7 个连续 \\footnotetext，严重影响可读性\n- 建议：整合为 ≤2 个脚注 + appendix table\n\n**W2-ref** [warning] 新颖性定位需要强化\n- 建议：更明确地阐述与 Eikema et al. (2025) 和 Kirk et al. (2024) 的 difference，以及为什么在 NER 中验证这些现象构成独立贡献。如果 primary contribution 是 diagnostic framework，考虑在 title 中突出 diagnostic 性质。\n\n**W3-ref** [warning] DALS 定位调整\n- 将 DALS 移至 appendix 作为 exploratory extension，或升级为 Method section 中的正式方法并补充 rigorous evaluation\n\n**W4-ref** [warning] Primary test bed 选择\n- 考虑将 Few-NERD 重新定位为 primary（definitive statistical power），SciERC 作为 secondary（exploratory, underpowered）\n\n## 小问题\n\n- Appendix 中 \"exp\\_025\"、\"exp\\_027\" 应删除\n- Contribution 2 和 3 过长，应精简\n- \"Capability trap\" 建议改为更 neutral 的措辞\n- SciERC greedy F1 的 4 个不同数值应统一或在 Methods 中提前声明 protocol 差异\n\n## 主要优势\n\n- 实验设计系统全面，难度梯度 + 功能角色分配是 benchmark 设计的范例\n- 统计处理（TOST + external anchors, bootstrap CI, MDE）在 NLP 论文中罕见的严谨\n- Per-sample vs. instance-level 的概念区分是有洞察力的框架贡献\n- Hidden state probe 实验巧妙地封堵了\"只是信号不够好\"的 alternative explanation\n- Limitations 的透明度超过大多数投稿论文",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**审稿侧重**：新颖性、完整性、Related Work、写作质量\n\n---\n\n## Summary\n\n本文研究为什么在 NER 任务中有效的 quality estimation 信号（Spearman ρ 达 0.45, AUROC 达 0.82）无法转化为 best-of-N sample selection 增益。通过在 4 个 NER benchmark、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）和 1 个 4B ablation 上评估 5 种 confidence signals，作者诊断出两个阻塞机制：instance degeneracy（14–59% 实例所有样本产生相同 F1）和 weak LP-quality alignment。唯一取得显著 selection 增益的条件是 Few-NERD 上 LP（+1.39pp, p<0.001），需要 degeneracy <15% 且 alignment ρ≈0.5 两个条件同时满足。论文还通过 hidden state probes 证明即使模型内部表示包含更丰富的信息（ρ=0.388 vs. LP 0.283），correlation-selection gap 依然存在。\n\n---\n\n## Strengths\n\n**S1** [实验设计全面] 4 个 NER 数据集构成清晰的难度梯度（WNUT-17 signal collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个数据集服务于明确的实验角色。5 种信号覆盖 structural/surface/model-internal 三个家族。多种 ablation（temperature, LoRA rank, epoch, N-scaling, free-form decoding）系统地隔离变量。\n\n**S2** [统计严谨性] 论文在统计方法上表现出色：bootstrap CI（B=10,000）、TOST equivalence testing（含 external anchors 修正 circularity）、MDE 计算（明确指出 SciERC n=529 的 power limitation）、多重比较校正（Bonferroni）。Non-tied subset 的 sole positive finding（+2.9pp, p=0.004）经 Bonferroni 校正后仍然 significant——这种严谨性在同类工作中少见。\n\n**S3** [per-sample vs. instance-level 区分] 将 5 种信号明确分为 instance-level（4 种，对 selection 无信息量 by construction）和 per-sample（仅 LP）是一个重要的概念贡献。这个区分解释了为什么 structural signals 在 QE 上强但 selection 上弱，比简单报告\"没有信号有效\"更有洞察力。\n\n**S4** [Hidden state probes 扩展] Section 5.6 的 hidden state probe 实验直接测试了\"是否更丰富的信号能改善 selection\"这一自然后续问题。MLP probe ρ=0.388（比 LP 高 37%）但 selection 反而更差（gap closure -5.1% vs. +4.8%），有力地证明了 bottleneck 不在 information 而在 diminishing marginal returns。\n\n**S5** [Limitations 诚实全面] Limitations section 和 appendix 中对各种 confounds 的讨论（thinking token, epoch confound, SciERC seed sensitivity）非常透明，主动报告了所有已知的弱点。\n\n---\n\n## Weaknesses\n\n**W1** [Critical] **正文页数超限**\n通过 PDF 分析，Conclusion（Section 6）从第 9 页开始并延续到第 10 页，Limitations 也在第 10 页。ACL 长文限制为 ≤8 页正文（不含 Limitations/Ethics/References）。主体内容约 9.5 页，超出限制约 1.5 页。这是 desk-reject 级别的问题。\n\n- 主要来源：Discussion（Section 5）过长，包含多个可移至 appendix 的段落（LP compression mechanisms, regime boundaries 的详细数值、DALS 方法介绍）。\n- 建议：将 DALS 段落完整移至 appendix；压缩 \"regime boundaries\" 段落为 2–3 句总结性陈述并 refer appendix；将 \"LP compression mechanisms\" 的 4 个机制列表移至 appendix，正文仅保留结论。\n\n**W2** [Major] **新颖性增量有限**\n论文的核心贡献是一个 diagnostic negative result + 两个命名概念。逐一评估：\n\n(a) **Correlation-selection gap**：correlation 不意味着 selection utility 是 MBR 文献中的已知问题。Eikema et al. (2025) 的 MBR utility misalignment 和本文的 diagnosis 是 complementary 的（论文承认这点，Introduction line 16），但\"对已知现象在新 domain 中的验证\"的新颖性阈值较低。\n\n(b) **Instance degeneracy**：fine-tuned models + constrained decoding 产生低多样性输出是可预测的结果。Kirk et al. (2024) 讨论了 RLHF 下的 diversity collapse，Yun et al. (2025) 讨论了 format constraints 下的 diversity collapse。将这些现象量化并命名为 \"instance degeneracy\" 有一定 diagnostic 价值，但不构成方法论创新。\n\n(c) **Capability trap**：基于 3 个 scale points（3B, 4B, 8B）、2 个 model families、3 个 convergence levels 的 observational evidence，论文正确指出\"does not establish causality\"（Discussion line 46）。但 \"capability trap\" 这一术语暗示了比证据支撑更强的普遍性。在 70B+ 模型上，更强的表达能力可能同时减少 degeneracy 和改善 alignment，逆转当前趋势。\n\n(d) **与 Yao et al. (2026) 的区分**：论文声称 Yao et al. 只展示了 correlation 而自己诊断了 why correlation 不 translate to selection。这个定位是合理的，但 Yao et al. 用 hard-prompting（非 fine-tuning），degeneracy 可能天然更低，两者的实验设置差异限制了直接增量比较。\n\n对于 EMNLP 而言：negative/diagnostic results 是被接受的，但需要 (i) 足够的覆盖度证明 negative result 的 robustness，(ii) 有意义的 actionable insight。条件 (i) 满足良好（多数据集、多模型、多 ablation）。条件 (ii) 部分满足：QE 的 practical guidelines 有价值，但 selection 方面的 actionable output 有限（DALS 增益微弱且 seed-sensitive）。\n\n**W3** [Major] **DALS 定位混乱**\nDiscussion 中引入的 DALS（Degeneracy-Aware LP Selection）方法与论文的\"诊断性\"定位产生冲突：\n- 如果这是诊断论文：DALS 应在 appendix 中作为 exploratory extension\n- 如果 DALS 是核心贡献：应在 Method section 中正式定义，有独立的实验表格，并在 contribution list 中列出\n\n当前 DALS 的结果是 seed-sensitive 的（SciERC: +0.19 to +1.14pp across seeds），且在 CoNLL 上仍然 degradation（-0.87pp）。将一个如此 preliminary 的方法放在 Discussion 中会造成 contribution 边界模糊。\n\n**W4** [Major] **Table 3（tab:fewnerd）的 7 个连续脚注**\nTable 3 caption 中使用了 `\\protect\\footnotemark` 7 次，产生 7 个连续的脚注文本。这严重损害可读性：审稿人需要在表格和页底之间反复跳转，且脚注内容（oracle headroom、greedy F1 差异、degeneracy 定义、epoch difference、seed details ×3）混合了定义性信息和技术 caveat。\n\n建议：将 degeneracy 定义移至首次使用处（Section 3/4）；将 3-seed details 移至 appendix table 或正文段落；将 SciERC greedy F1 差异解释整合到一个 \"notation note\" 中。最终 Table 3 的脚注应不超过 2 个。\n\n**W5** [Major] **SciERC 作为 primary test bed 统计 power 不足**\nSciERC 有 n=529（gold-filtered），论文自己计算 MDE≈1.5pp at 80% power。然而论文声称 LP 在 SciERC 上的 +0.61pp \"falls below detectable thresholds\"（Table 3）——这意味着在 primary test bed 上无法区分 \"真的没有效果\" 和 \"效果太小检测不出来\"。\n\nFew-NERD（n=32,565, MDE≈0.22pp）才是真正有 definitive power 的数据集。建议重新定位：将 Few-NERD 作为 primary test bed（LP selection 的 definitive positive evidence），SciERC 作为 \"medium-difficulty, underpowered\" secondary test bed。当前的叙事结构（SciERC 为主 → Few-NERD 为 contrast）弱化了论文最强的实证结果。\n\n**W6** [Minor] **Greedy F1 数值不一致**\nSciERC 的 greedy F1 在不同表格中出现多个值：0.640（Table N-scaling）、0.644（Table 3 / fewnerd）、0.645（Table 2 / selection）、0.650（Table hidden_probe, epoch 3-epoch）。虽然每个差异都有脚注解释（seed 差异、aggregation 差异、gold-filtering），但审稿人看到同一 baseline 有 4 个不同数值会产生困惑和不信任感。\n\n建议：统一所有表格的 evaluation protocol（相同 seed、相同 filtering、相同 aggregation），或在 Methods section 中明确声明各表格使用的协议差异并给出原因。\n\n**W7** [Minor] **Appendix 中残留内部实验标识**\nAppendix Table~\\ref{tab:n_scaling_selection} caption 含 \"exp\\_025\"，Table~\\ref{tab:epoch_confound} caption 含 \"exp\\_027\"。这些是内部实验管理系统的标识符，应在投稿前删除。虽然不直接泄露作者身份，但显得不够 professional。\n\n**W8** [Minor] **\"Capability trap\" 措辞的 framing 风险**\n\"Trap\" 一词暗示了不可逃脱的困境。但论文自己展示了 temperature 和 early stopping 可以部分控制 degeneracy；更大规模模型（70B+）的行为完全未知。\"Capability-diversity tension\" 或 \"capability-selection tradeoff\" 是更准确的描述。\n\n---\n\n## Questions\n\n**Q1** Few-NERD 使用 3 epochs 而 SciERC/CoNLL 使用 5 epochs（Table 3 脚注 4）。5-epoch Few-NERD control 的 degeneracy 上升到 31% 且 LP 增益减半。那么 SciERC 在 3 epochs 时 degeneracy 仅 6.4%（Table epoch_scierc），为什么不将 3-epoch SciERC 作为 primary checkpoint？这似乎能产生更有信息量的 comparison with Few-NERD。\n\n**Q2** Hidden state probe 使用 mean-pooled final-layer hidden state。是否尝试过：(a) entity span 位置的 hidden states，(b) 多层 pooling，(c) attention-weighted pooling？Mean pooling 可能丢失了与 NER 最相关的 local information。\n\n**Q3** Per-entity-type analysis within Few-NERD（ρ=-0.881, p=0.004, n=8）被用作 degeneracy-selection 关系的 supporting evidence，但论文注意到 \"types share model and tokenizer, so effective degrees of freedom may be lower than 6\"。如果 effective df 更低，p-value 应该更大——这条证据线的可靠性如何？\n\n**Q4** 论文测试了 LP、VerbConf 和 hidden state probes 作为 per-sample signals，但没有测试 Self-Certainty (Kang et al. 2025) 和 P(True) (Kadavath et al. 2022)，两者都在 Limitations 中被提及。给出这些是 readily available 的 per-sample signals，为什么没有在实验中包含？\n\n**Q5** DALS 在 CoNLL 上仍然表现为 degradation（Qwen: -0.87pp）。如果 DALS 的 decision rule 需要 labeled development set 来估计 degeneracy 和 alignment，为什么不直接在 development set 上用 LP selection vs. greedy 的 paired test 来决定是否使用 LP selection？这个更简单的 approach 是否等价？\n\n---\n\n## Missing References\n\n1. **Semantic entropy** — Farquhar et al. (2024) \"Detecting Hallucinations in Large Language Models Using Semantic Entropy\" (Nature)。与 semantic uncertainty (Kuhn et al. 2023) 相关但不同；更直接涉及结构化输出的不确定性度量。\n\n2. **NER 特定的 calibration 工作** — Related Work 中 NER-specific confidence/calibration 仅引用了 pre-LLM 工作 (Culotta 2004, Mejer 2010)。近年 LLM-based NER 的 calibration 文献（如果存在）应被讨论。当前 Related Work 从 general confidence estimation surveys 直接跳到本文，缺少 NER-specific 中间层。\n\n3. **Best-of-N for code generation** — Chen et al. (2021) \"Evaluating Large Language Models Trained on Code\" (Codex paper) 和 Li et al. (2022) AlphaCode 都展示了 best-of-N 在 code generation 中的成功。当前仅引用 Shi et al. (2022) 的 execution-based MBR。更全面的 BoN 成功案例讨论能更好地 contextualize NER 的特殊困难。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 符合 4-question 结构（问题、重要性、方法、结果）。\n- \"four instance-level, one per-sample log-probability [LP]\" 中 \"LP\" 在 Abstract 中首次出现但未完整定义（log-probability 已给出，但 LP 作为缩写的显式定义不够明确）。\n- 信息密度适中，约 150 words。\n\n### Introduction (Section 1)\n- 叙事结构完整：background → existing conflation → our distinction → mechanisms → contributions。\n- Line 6 \"Unlike Yao et al. (2026)\" 的区分清晰且公平。\n- Contribution list 过长：contribution 2 有 4 行子句，contribution 3 有 3 行，各包含过多的数值细节。建议将数值 evidence 移到各 contribution 对应的 section 中，contribution list 仅保留概念性描述。\n- Figure 1 信息密度高且 caption 自包含。\n\n### Related Work (Section 2)\n- 结构清晰（4 个 paragraph），每类都有明确的 positioning。\n- \"We extend self-consistency to set-valued structured outputs\" 是合理的 positioning。\n- 与 Yao et al. (2026) 的区分到位：\"we show correlation is necessary but not sufficient\"。\n- 可以补充 NER-specific calibration 的更多讨论（见 Missing References）。\n\n### Method (Section 3)\n- 5 种 signal 的定义清楚，数学形式正确。\n- Per-sample vs. instance-level 的区分从 Section 3.1 就建立，贯穿全文。\n- SJ 的 normalizer robustness 在正文脚注中提及并 refer appendix，处理得当。\n- Evaluation framework（QE vs. Selection）定义清楚。\n\n### Experiments (Section 4)\n- Dataset 角色分配清晰（primary / low-degeneracy contrast / ceiling control / signal-collapse boundary）。\n- Table 1（QE results）格式清楚，但缺少 Few-NERD 和 WNUT-17 的数据（分散在 appendix 各处）。建议在正文中补充一个统一的 full-dataset QE 汇总表。\n- Table 2（selection results）有效传达了核心 negative finding。\n- Table 3 的脚注问题如 W4 所述。\n- Section 4.4（Robustness）混合了多个 ablation，段落之间缺乏明确的逻辑连接。\n- Section 4.5（Hidden state probes）是新颖的分析，值得肯定。\n\n### Discussion (Section 5)\n- 过长，是导致 W1（超页限）的主要原因。\n- \"LP compression mechanisms\" 段落列出 4 个机制但每个只用 1–2 句话，没有足够深度；适合 appendix。\n- \"Regime boundaries\" 段落试图给出 practical guidelines 但太详细（含完整的 decision rule 和数值条件）。\n- DALS 段落如 W3 所述定位不清。\n- \"Capability trap\" 段落的 framing 如 W8 所述略有过度。\n\n### Conclusion (Section 6)\n- 是 Introduction 和 Discussion 的有效总结，没有引入新信息。\n- 最后一句（\"the same progress that reduces error also reduces the diversity on which selection depends\"）是一个有力的结束。\n\n### Limitations\n- 非常全面，诚实地讨论了：scale gap, seed sensitivity, single-dataset RE, epoch confounds, untested signals (Self-Certainty, P(True)), ε threshold 的 post-hoc 性质。\n- 信息量过大——部分内容（如 verbalized confidence 的详细结果描述）更适合 appendix。\n\n### 写作质量\n- **AI 标志检查**：无 em-dash（—）使用；无 \"Furthermore/Moreover/Additionally\" 堆砌；仅 3 处 \"-ing\" 短语（\"indicating\" ×2, \"revealing\" ×1），均在可接受范围内。论文在 AI 写作痕迹控制方面做得很好。\n- **专有名词定义**：correlation-selection gap、instance degeneracy 在首次使用时有定义。LP、QE、MDE 等缩写的首次定义基本到位。DALS 在 Discussion 中首次出现并定义。\n- **段落结构**：整体合理，未出现过度分段。\n\n### 格式合规性\n- `\\usepackage[review]{acl}` — 正确。\n- Author: Anonymous — 正确。\n- 行号：review option 会自动生成 — 正确。\n- **正文超限** — 见 W1。\n- Appendix 中残留 \"exp\\_025\"、\"exp\\_027\" — 见 W7。\n- References 格式基本一致；verify_references 显示 64 条引用、0 orphan、0 missing、3 条 online not found（hobelsberger2025, lightman2024, venktesh2025——可能是 preprint 尚未被 OpenAlex 索引）、4 条 mismatch（可能是 title 变体）。\n\n---\n\n## Overall Assessment\n\n**Overall**: 2.5 / 5（介于 \"Resubmit next cycle\" 和 \"Findings\" 之间）\n\n**一句话总结**：一篇实验严谨、统计透明的诊断性研究，但正文超页限是 hard blocker，新颖性增量有限（主要是对已知现象在 NER 中的系统验证和命名），且 primary test bed 的统计 power 不足以区分 null effect 和 small effect。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计和统计方法优秀（S2），但 primary test bed power 不足（W5），greedy F1 不一致（W6），DALS 评估不充分（W3） |\n| Excitement | 2.5/5 | 诊断性 insight 有价值（S3, S4），但核心发现是 negative result 且 actionable output 有限；named concepts 的新颖性增量有限（W2） |\n| Reproducibility | 4/5 | Training config、prompt template、evaluation protocol 详细；代码承诺 release；appendix 极其全面。唯一扣分：greedy F1 多个数值的 protocol 差异增加复现难度 |\n| Confidence | 4/5 | 仔细阅读了全文和 appendix；NER evaluation 和 MBR/uncertainty estimation 是我的熟悉领域 |\n\n## Must-Fix 问题\n\n**N1** [critical] 正文超 8 页限制\n- 具体位置：Section 5 (Discussion) 和 Section 6 (Conclusion) 延伸到 page 10\n- 问题：ACL 长文 ≤8 页正文（不含 Limitations/Ethics/References）；当前约 9.5 页\n- 为什么影响接收：格式不合规可能导致 desk reject\n- 建议：压缩 Discussion（将 DALS、LP compression details、regime boundary numerics 移至 appendix），contribution list 精简数值\n\n## Should-Fix 问题\n\n**W1-ref** [warning] Table 3 的 7 个脚注\n- 具体位置：Section 4.3, Table~\\ref{tab:fewnerd}\n- 问题：7 个连续 \\footnotetext，严重影响可读性\n- 建议：整合为 ≤2 个脚注 + appendix table\n\n**W2-ref** [warning] 新颖性定位需要强化\n- 建议：更明确地阐述与 Eikema et al. (2025) 和 Kirk et al. (2024) 的 difference，以及为什么在 NER 中验证这些现象构成独立贡献。如果 primary contribution 是 diagnostic framework，考虑在 title 中突出 diagnostic 性质。\n\n**W3-ref** [warning] DALS 定位调整\n- 将 DALS 移至 appendix 作为 exploratory extension，或升级为 Method section 中的正式方法并补充 rigorous evaluation\n\n**W4-ref** [warning] Primary test bed 选择\n- 考虑将 Few-NERD 重新定位为 primary（definitive statistical power），SciERC 作为 secondary（exploratory, underpowered）\n\n## 小问题\n\n- Appendix 中 \"exp\\_025\"、\"exp\\_027\" 应删除\n- Contribution 2 和 3 过长，应精简\n- \"Capability trap\" 建议改为更 neutral 的措辞\n- SciERC greedy F1 的 4 个不同数值应统一或在 Methods 中提前声明 protocol 差异\n\n## 主要优势\n\n- 实验设计系统全面，难度梯度 + 功能角色分配是 benchmark 设计的范例\n- 统计处理（TOST + external anchors, bootstrap CI, MDE）在 NLP 论文中罕见的严谨\n- Per-sample vs. instance-level 的概念区分是有洞察力的框架贡献\n- Hidden state probe 实验巧妙地封堵了\"只是信号不够好\"的 alternative explanation\n- Limitations 的透明度超过大多数投稿论文",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-18T12:55:50.874826+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3765
}
```

</details>

---


### Assistant

_source line 1696 · 2026-05-18T12:56:00.787389+00:00_

审稿意见已提交给 Review Director。

审稿核心结论：

- **Overall 2.5/5**（介于 Resubmit next cycle 和 Findings 之间）
- **1 个 Critical 问题**：正文超 8 页限制（约 9.5 页），Discussion 过长是主因
- **4 个 Major 问题**：新颖性增量有限（主要是对已知现象的 NER 验证和命名）、DALS 定位混乱、Table 3 的 7 个脚注爆炸、SciERC 作为 primary test bed 统计 power 不足
- **4 个 Minor 问题**：greedy F1 不一致、appendix 残留 exp\_025/027 标识、"capability trap" 措辞过度、contribution list 过长
- **主要优势**：实验设计系统全面、统计方法严谨（TOST + bootstrap + MDE）、per-sample vs. instance-level 区分有洞察力、hidden state probe 实验巧妙

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 43

## Round 43

5 recorded events


### User

_source line 1697 · 2026-05-18T12:57:00.753000+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每一条 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（引用具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿意见：

**评分**: 3.5/5 (Borderline Conference)
**Soundness**: 3/5, **Excitement**: 3/5, **Reproducibility**: 4/5, **Confidence**: 4/5

**核心判断**: 实验全面、透明度高、负面结果诚实呈现，但核心框架（两个条件）的跨数据集支撑仅 3 个点，且 headline positive result（Few-NERD +1.39pp）受 epoch confound 显著影响。

### Must-Fix (Critical)

**N1: "两个条件"框架经验基础不足**
- 跨数据集仅 3 个数据点（CoNLL/SciERC/Few-NERD），论文自身标注 "exploratory given 5+ confounds"
- 15% degeneracy 阈值来自 Few-NERD per-entity-type 两个相邻点（Person 13.4% vs Art 19.8%）
- 建议：增加数据集验证 或 调低理论 claim 强度

**N2: Epoch confound 对 headline result 的影响**
- Few-NERD 3 epoch → +1.39pp，5 epoch → +0.62pp（gain 减半）
- 统一为 5 epoch 后，Few-NERD 效应量接近 SciERC（+0.61pp），框架区分力减弱
- 当前仅在 footnote + appendix 讨论，正文需更充分处理

### Should-Fix (Warning)

**W1: SciERC (n=529, MDE≈1.5pp) 作为 primary test bed 系统性 underpowered**

**W2: DALS 的 ε=0.05 阈值从 data sweep 中选出后又在同一数据上评估，存在 data-snooping 风险**

**W3: "Capability trap" 措辞对 3 个 scale points 的 observational trend 过强**

### 主要优势
- QE vs selection 的概念区分清晰有力
- 实验覆盖面数一数二（4 datasets × 2-3 models × 多个消融维度）
- 统计方法（bootstrap, TOST, MDE, Bonferroni）显著高于 NLP 论文平均水平
- Negative results 和 Limitations 的诚实程度值得肯定

### 引用验证
64 条引用全部匹配 bib，0 orphan / 0 missing，3 条 online not found（近期预印本），4 条作者名格式小差异，无虚假引用。

---

请对 N1, N2, W1, W2, W3 逐条回应 [AGREE] 或 [REBUT]。特别关注：
- N1（两条件框架证据薄）——你在 W2 中指出新颖性有限，两者是否指向同一个问题？
- N2（epoch confound）——你如何从新颖性角度评估这个问题？如果 5-epoch 统一后 Few-NERD 和 SciERC 效果相近，论文的区分性故事是否还成立？
- W1（SciERC underpowered）——与你的 W5 是否完全一致？
- W2（DALS data snooping）——你的 W3 也指出了 DALS 的问题，这两个 concern 是否互补？
- W3（capability trap）——与你的 W8 是否一致？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-18T12:57:09.247023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "95",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "95",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-18T12:57:09.648888+00:00_

95	\subsection{Cross-Dataset Contrast: Few-NERD}
96	\label{sec:fewnerd}
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). $p$: paired bootstrap ($n{=}10{,}000$) vs.\ greedy.\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark\protect\footnotemark}
102	\label{tab:fewnerd}
103	\resizebox{\columnwidth}{!}{%
104	\begin{tabular}{@{}lrccccr@{}}
105	\toprule
106	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
107	\midrule
108	CoNLL & 2{,}756 & .908 & 59.1\% & .302 & $-$0.85\,pp & 1.0 \\
109	SciERC & 529 & .644 & 17.8\% & .215 & $+$0.61\,pp & .193 \\
110	Few-NERD & 32{,}565 & .748 & 13.8\% & .421 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
111	\bottomrule
112	\end{tabular}}
113	\end{table}
114	\footnotetext{Oracle headroom: 4.0~pp (CoNLL), 13.2~pp (SciERC), 12.4~pp (Few-NERD).}
115	\footnotetext{SciERC values (greedy${=}0.644$, headroom${=}13.2$~pp) differ slightly from Table~\ref{tab:selection} (greedy${=}0.645$, headroom${=}13.3$~pp) due to max-LP aggregation and single-seed evaluation; the ranking is unchanged.}
116	\footnotetext{Instance degeneracy: fraction of gold-filtered instances where all $N$ samples produce identical instance-level F1.}
117	\footnotetext{Few-NERD uses 3-epoch checkpoints (early stopping); SciERC and CoNLL use 5 epochs. A 5-epoch Few-NERD control confirms LP selection remains positive though gains are halved (Appendix~\ref{app:epoch_confound}).}
118	\footnotetext{SciERC LP $\Delta$ is single-seed (seed${=}42$); 3-seed mean: $+0.04{\pm}0.48$~pp, reflecting high seed sensitivity at this sample size ($n{=}529$).}
119	\footnotetext{Few-NERD LP $\Delta$ is 3-seed mean (seeds 42, 123, 456); individual: $+1.36$, $+1.44$, $+1.37$~pp. All seeds $p{<}0.001$.}
120	\footnotetext{CoNLL LP $\Delta$ is 3-seed mean (seeds 42, 123, 456); individual: $-1.05$, $-0.77$, $-0.73$~pp.}
121	
122	F
…[truncated 2744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-18T12:57:10.854583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "offset": "28",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "offset": "28",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-18T12:57:10.956440+00:00_

28	\paragraph{Regime boundaries and practical guidelines.}
29	At the low-resource boundary (WNUT-17), QE signals collapse (VC conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); at the ceiling boundary (CoNLL, degeneracy 59--89\%), LP degrades selection ($-0.85$~pp).
30	In the moderate regime, two conditions jointly determine effectiveness.
31	Temperature manipulation provides the primary evidence ($T{=}1.2$: degeneracy 12.5\%, $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}): it alters output diversity without changing model capacity, isolating the degeneracy lever from alignment.
32	Even at degeneracy approaching Few-NERD levels (12.5\% vs.\ 13.8\%), LP does not improve selection because alignment remains weak ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5).
33	LoRA rank${=}8$ (degeneracy 7.2\%, $\rho{=}0.24$) corroborates the pattern, though this ablation conflates diversity with capacity (secondary evidence).
34	SciERC at 3 epochs (degeneracy 6.4\%, $\rho{=}0.317$) provides a boundary case: despite degeneracy well below 15\%, alignment remains insufficient relative to Few-NERD ($\rho{\approx}0.5$) and LP selection stays below detectable thresholds (Table~\ref{tab:epoch_scierc}).
35	The cross-dataset gradient (59\% $\to$ $-0.85$~pp, 18\% $\to$ $+0.61$~pp, 14\% $\to$ $+1.39$~pp; $n{=}3$ datasets, exploratory) is consistent with an inverse relationship; per-entity-type analysis within Few-NERD ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; entity types share model and tokenizer, effective $\mathit{df}$ may be lower; Appendix~\ref{app:per_type_lp}) provides supporting evidence.
36	Practitioners should first estimate instance degeneracy and LP-quality alignment on a labeled development set.
37	The decision rule is: if degeneracy ${<}$15\% and within-instance $\rho(\text{LP}, \text{F1}) \gtrsim 0.3$ (approximate thresholds from our data), use LP selection (gains scale with $N$; Table~\ref{tab:fewnerd}); otherwise, prefer greedy decoding ($T{=}0$), using structural signals for quali
…[truncated 1001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


## Round 44

## Round 44

20 recorded events


### User

_source line 1702 · 2026-05-18T13:01:49.760930+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Round 1（Reviewer 2：新颖性 + 完整性）

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
你负责 **新颖性 + 完整性**：

1. **新颖性评估**：
   - 核心发现（correlation-selection gap, degeneracy mechanism）相对于现有文献的增量贡献
   - 与 MBR 文献（特别是 Eikema et al. 2025）的差异化是否清晰
   - 与 self-consistency 文献（Wang et al. 2023, Chen et al. 2024, Kang et al. 2025）的定位

2. **Related Work 完整性**：
   - 引用是否充分覆盖：直接相关方法、baseline 论文、benchmark 论文、理论基础
   - 是否有遗漏的重要相关工作
   - Related Work 是否做了归纳比较（而非论文堆砌）

3. **写作质量**：
   - 叙事是否连贯（Abstract → Intro → Method → Experiments → Discussion → Conclusion 主线一致性）
   - AI 写作痕迹检查（em-dash/en-dash 滥用、-ing phrases、过度分段、黑名单用词）
   - 专有名词是否有定义
   - 图表 caption 是否自包含

4. **Contribution 与证据匹配**：
   - 每条 Contribution 是否有对应的 section/table 支撑
   - Claims 的强度是否与证据匹配

### 已知 Open Issue（前轮遗留）
- **R2-N3**: Title 使用 "Structured Information Extraction" 但实验主要覆盖 NER + 仅单一 RE benchmark。请评估 title scope 与论文实际内容的匹配度，给出明确建议。

请以标准审稿格式输出：Summary → Strengths → Weaknesses (Critical/Warning/Info) → Questions → Missing References → Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1703 · 2026-05-18T13:02:01.336234+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1704 · 2026-05-18T13:02:02.540932+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1204
}
```

</details>

---


### Tool call

_source line 1705 · 2026-05-18T13:02:02.691828+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1706 · 2026-05-18T13:02:02.692216+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1707 · 2026-05-18T13:02:02.692424+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1708 · 2026-05-18T13:02:02.793037+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1709 · 2026-05-18T13:02:06.914701+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1710 · 2026-05-18T13:02:06.915185+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1711 · 2026-05-18T13:02:31.898917+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nprint(f'Total pages: {len(pages)}')\nfor i in range(min(12, len(pages))):\n    # Find section headers\n    for line in pages[i].split('\\n'):\n        stripped = line.strip()\n        if any(kw in stripped for kw in ['Introduction', 'Related Work', 'Method', 'Experiments', 'Discussion', 'Conclusion', 'Limitations', 'Ethics Statement', 'References', 'Notation']):\n            if len(stripped) < 120 and not stripped.startswith('Table') and not stripped.startswith('Figure'):\n                print(f'Page {i+1}: {stripped[:80]}')\n\" 2>/dev/null\n",
  "description": "Map section locations to page numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nprint(f'Total pages: {len(pages)}')\nfor i in range(min(12, len(pages))):\n    # Find section headers\n    for line in pages[i].split('\\n'):\n        stripped = line.strip()\n        if any(kw in stripped for kw in ['Introduction', 'Related Work', 'Method', 'Experiments', 'Discussion', 'Conclusion', 'Limitations', 'Ethics Statement', 'References', 'Notation']):\n            if len(stripped) < 120 and not stripped.startswith('Table') and not stripped.startswith('Figure'):\n                print(f'Page {i+1}: {stripped[:80]}')\n\" 2>/dev/null\n",
    "description": "Map section locations to page numbers"
  }
}
```

</details>

---


### Tool result

_source line 1712 · 2026-05-18T13:02:32.501882+00:00_

Total pages: 33
Page 1: 031   1   Introduction
Page 2: 2     Related Work                                       146
Page 7: Method              ρ          Sel. F1    Gap%        ρ       Gap%
Page 9: 6   Conclusion                                          686
Page 11: 2022 Conference on Empirical Methods in Natural         860
Page 12: Methods in Natural Language Processing.                     993
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1713 · 2026-05-18T13:02:38.933375+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 9 and 10 more carefully for Conclusion end and Limitations start\nfor i in [8, 9]:  # pages 9 and 10\n    lines = pages[i].split('\\n')\n    for j, line in enumerate(lines):\n        s = line.strip()\n        if any(k in s for k in ['Conclusion', 'Limitation', 'Ethics']):\n            print(f'Page {i+1}, line ~{j}: {s[:100]}')\n    # Show last 5 non-empty lines\n    non_empty = [l.strip() for l in lines if l.strip()]\n    print(f'  Page {i+1} ends with: {non_empty[-1][:80] if non_empty else \\\"(empty)\\\"}')\n    print()\n\" 2>/dev/null\n",
  "description": "Precise location of Conclusion/Limitations boundary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 9 and 10 more carefully for Conclusion end and Limitations start\nfor i in [8, 9]:  # pages 9 and 10\n    lines = pages[i].split('\\n')\n    for j, line in enumerate(lines):\n        s = line.strip()\n        if any(k in s for k in ['Conclusion', 'Limitation', 'Ethics']):\n            print(f'Page {i+1}, line ~{j}: {s[:100]}')\n    # Show last 5 non-empty lines\n    non_empty = [l.strip() for l in lines if l.strip()]\n    print(f'  Page {i+1} ends with: {non_empty[-1][:80] if non_empty else \\\"(empty)\\\"}')\n    print()\n\" 2>/dev/null\n",
    "description": "Precise location of Conclusion/Limitations boundary"
  }
}
```

</details>

---


### Tool result

_source line 1714 · 2026-05-18T13:02:39.434881+00:00_

Page 9, line ~71: 6   Conclusion                                          686
  Page 9 ends with: 9

Page 10, line ~25: 723   Limitations                                                  untested. Other per-sample scorin
Page 10, line ~43: 740   form results are in Appendix L. Qwen3-8B’s Sci-              Ethics Statement                 
  Page 10 ends with: 10
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1715 · 2026-05-18T13:02:55.446297+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, scale definitions, and criteria. Include the exact scoring scales for Overall Assessment, Soundness, Excitement, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, scale definitions, and criteria. Include the exact scoring scales for Overall Assessment, Soundness, Excitement, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 1716 · 2026-05-18T13:03:03.221963+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
Scale: 1-5 with half-point increments

- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award" (top 2.5%)
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance recommended
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions"
- **1**: Do not resubmit or lacks relevance to computational linguistics

## Soundness
Scale: 1-5 with half-point increments

- **5**: Excellent; exceptionally thorough given paper type
- **4**: Strong; sufficient support for claims with optional enhancements
- **3**: Acceptable; main claims supported with minor gaps
- **2**: Poor; major technical/methodological problems
- **1**: Major Issues; insufficient for publication

## Excitement
Scale: 1-5 with half-point increments

- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points" if time permits
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: "Not Exciting: does not resonate" with broader community

## Reproducibility
Scale: 1-5

- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Impossible to reproduce

## Dataset Value
Scale: 1-5

- **5**: Enabling new research directions
- **4**: Useful for other researchers
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable datasets

## Software Value
Scale: 1-5

- **5**: Enabling new research directions
- **4**: Useful for other researchers
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable software

## Reviewer Confidence
Scale: 1-5

- **5**: Very careful review; familiar with related work
- **4**: Quite sure; unlikely ma
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7775
}
```

</details>

---


### Tool call

_source line 1717 · 2026-05-18T13:03:10.445928+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures"
  }
}
```

</details>

---


### Tool result

_source line 1718 · 2026-05-18T13:03:10.496624+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_degeneracy_lp_scatter.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1719 · 2026-05-18T13:06:40.729445+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）\n\n---\n\n## Summary\n\n本文研究 self-consistency 类 confidence signals 在 LLM-based NER 中 quality estimation（QE）与 sample selection 之间的脱钩现象。在 4 个 NER benchmark、2 个 8B 模型家族和 1 个 4B ablation 上评估 5 种信号，发现所有信号均可实现可靠的 QE（ρ 达 0.45, AUROC 达 0.82），但仅 LP 在特定条件下（Few-NERD, degeneracy <15%, alignment ρ≈0.5）取得显著 selection 增益（+1.39pp）。论文诊断出两个阻塞机制——instance degeneracy 和 weak LP-quality alignment，合称 correlation-selection gap。Hidden state probes 进一步证明即使模型内部表示包含更丰富信息，selection gap 依然存在。\n\n---\n\n## Strengths\n\n**S1** [概念框架] Per-sample vs. instance-level signal 的区分（Section 3.1）是论文最有洞察力的贡献。4/5 信号是 instance-level aggregates，对 selection 无信息量 by construction——这个 observation 直接解释了为什么高 ρ 不能转化为 selection，比泛泛报告\"没有信号有效\"更有诊断价值。这个框架对后续 test-time scaling 研究在结构化输出上的工作有指导意义。\n\n**S2** [实验系统性] 4 个数据集的角色设计（WNUT-17 signal-collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling）构成清晰的难度梯度。每个数据集服务于明确的实验功能，不是简单的\"多数据集堆砌\"。多种 ablation（temperature, LoRA rank, epoch, N-scaling, free-form decoding, hidden state probes, DeBERTa verifier, supervised combination）系统地排除 alternative explanations。\n\n**S3** [统计严谨性] Bootstrap CI（B=10,000）、TOST equivalence testing（含 external anchors 修正 circularity）、MDE 计算（明确 SciERC n=529 的 power limitation）、Bonferroni correction。Non-tied subset positive finding（+2.9pp, p=0.004）经 Bonferroni 校正后仍 significant。这在 NLP 论文中罕见。\n\n**S4** [Hidden state probe 实验] Section 4.5 直接测试了\"需要更强信号\"这一 natural follow-up。MLP probe ρ=0.388（比 LP 高 37%）但 selection 反而更差（gap closure -5.1% vs. +4.8%），有力封堵了\"bottleneck 在 information loss\"的 alternative explanation，将 diagnosis 推进到 diminishing marginal returns。\n\n**S5** [Limitations 透明度] 主动报告所有已知弱点：SciERC seed sensitivity（σ=0.48pp）、epoch confound（3 vs. 5 epochs）、scale gap（4B-8B only）、未测试的 per-sample signals（Self-Certainty, P(True)）、ε threshold 的 post-hoc 性质。透明度超过大多数投稿论文。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1** [Critical] **正文页数超限（~9.5 页 vs. 8 页限制）**\n- 具体位置：Section 5 (Discussion) 延续到 page 9+, Section 6 (Conclusion) 从 page 9 开始并延伸到 page 10, Limitations 也在 page 10。\n- 问题：ACL 长文正文 ≤8 页（不含 Limitations/Ethics/References）。通过 pdftotext 分析确认 Conclusion 在 page 9 开始、page 10 结束，Limitations 在 page 10 中部开始。主体内容约 9.5 页。\n- 为什么影响接收：格式不合规是 desk-reject 级别问题。\n- 建议：Discussion 是主要来源。建议将 DALS 段落完整移至 appendix（见 W3）；\"LP compression mechanisms\" 4 个机制仅用 1-2 句各，适合 appendix；\"Regime boundaries\" 段落过于 detailed（含完整 decision rule 和所有数值条件），压缩为 3 句 refer appendix。Contribution list 中 contribution 2（4 行）和 3（3 行）的数值细节也可精简。\n\n**W2** [Critical] **Title scope 过宽（R2-N3）**\n- 具体位置：Title \"Structured Information Extraction\" vs. 实际内容\n- 问题：Title 声称 \"Structured Information Extraction\"，但实验覆盖：\n  - NER：4 个 benchmark（SciERC, Few-NERD, CoNLL-2003, WNUT-17）——这是论文的全部主线\n  - RE：仅 SciERC RE，全文标注为 \"exploratory single-benchmark analysis\"（Appendix Section L, line 692），且结果全部在 appendix\n  - 无 event extraction、slot filling、open IE 或其他 IE 子任务\n- \"Structured IE\" 暗示的覆盖度远超实际内容。审稿人看到 title 会预期至少 2 个 IE 子任务有 substantive coverage，但 RE 被明确标为 exploratory 且仅用 SciERC 单一 benchmark。\n- 建议两个方案：\n  (a) **修改 title**：改为 \"...Fail to Scale LLM-Based Named Entity Recognition\" 或 \"...Fail to Scale Structured Output Selection\"。前者精确但限缩 scope，后者保留 generality 但不 overclaim。\n  (b) **提升 RE 实验**：将 RE 从 exploratory appendix 升级为正文中的 secondary evaluation，至少加一个 RE benchmark 以支撑 \"IE\" 这个 claim。\n  在当前状态下，建议方案 (a)。\n\n### Warning\n\n**W3** [Warning] **DALS 定位与论文主线冲突**\n- 具体位置：Discussion Section 5, \"From diagnosis to selection\" 段落\n- 问题：论文核心定位是 diagnostic study（诊断 correlation-selection gap），但 Discussion 中引入 DALS（Degeneracy-Aware LP Selection）作为一个具体的 selection method。这产生两个问题：\n  (1) 如果 DALS 是 contribution，应在 Method section 正式定义，有独立实验表格，并列入 contribution list。当前 DALS 仅在 Discussion 中描述，没有独立评估。\n  (2) DALS 结果 seed-sensitive（SciERC: +0.19 to +1.14pp across seeds），CoNLL 仍 degradation（-0.87pp）。将如此 preliminary 的结果放在 Discussion 中模糊了论文的 contribution 边界。\n- 建议：将 DALS 移至 appendix 作为 \"exploratory extension\"，与 RE extension 平行处理。Discussion 的 \"From diagnosis to selection\" 段落可保留 1-2 句作为 future direction pointer。这同时有助于解决 W1（页数超限）。\n\n**W4** [Warning] **新颖性增量需要更精确的定位**\n- 问题：论文的核心贡献是对已知 general phenomena 在 NER 特定 domain 中的系统验证和机制命名。逐项评估：\n  (a) **Correlation-selection gap**：QE correlation ≠ selection utility 在 MBR 文献中是已知问题。Eikema et al. (2025) 的 utility misalignment 是 complementary（论文正确指出，Introduction line 16, Related Work line 18）。本文的 specific contribution 是将 bottleneck 归因于 degeneracy 而非 utility misalignment——这是一个 domain-specific refinement，not a new general principle。\n  (b) **Instance degeneracy**：Fine-tuned models + constrained decoding 产生低多样性是可预测的。Kirk et al. (2024) 和 Yun et al. (2025) 已讨论 diversity collapse。本文的贡献在于将这些现象量化为 per-instance metric 并展示其对 selection 的直接影响——是 useful empirical characterization，但不构成方法论突破。\n  (c) **Capability trap**：基于 3 scale points（3B, 4B, 8B）的 observational trend。论文正确使用 hedging language（\"does not establish causality\", Discussion line 46），但 \"trap\" 这个术语暗示了超出证据的普遍性。在 70B+ 模型上的行为完全未知——更大模型可能同时减少 degeneracy（更强的生成能力）和改善 alignment。\n- EMNLP 接受 negative/diagnostic results 的前提是 (i) robustness 充分、(ii) actionable insight 有意义。条件 (i) 满足良好。条件 (ii) 部分满足：QE guidelines 有实用价值，但 selection 方面的 actionable output 有限。\n- 建议：在 Introduction 中更明确地框定 contribution 类型——\"We provide the first systematic empirical characterization of...\" 而非暗示 theoretical framework。这会让审稿人以 empirical contribution 标准评判，降低 novelty 期望。\n\n**W5** [Warning] **SciERC 作为 primary test bed 统计 power 不足**\n- 具体位置：Section 4.1（\"primary medium-difficulty test bed\"）, Table 2, Table 3\n- 问题：SciERC n=529, MDE≈1.5pp at 80% power。论文报告 LP 在 SciERC 上 +0.61pp（p=0.193）——这无法区分 \"真的没有效果\" 和 \"效果太小检测不到\"。3-seed mean 更是 +0.04±0.48pp，本质上是 noise。\n- Few-NERD（n=32,565, MDE≈0.22pp）才有 definitive power：LP +1.39pp, p<0.001, 3-seed std 仅 0.04pp。\n- 建议：将 Few-NERD 重新定位为 primary test bed（definitive evidence for LP selection）。SciERC 应被明确标注为 \"medium-difficulty, underpowered exploratory test bed\"，其 negative result 应被 framed 为 \"consistent with but not confirming the null\"。当前叙事结构（SciERC primary → Few-NERD contrast）弱化了论文最强的实证结果。\n\n**W6** [Warning] **Table 3 的 7 个连续脚注**\n- 具体位置：Section 4.3, Table~\\ref{tab:fewnerd}, experiments.tex lines 101-120\n- 问题：Caption 中 `\\protect\\footnotemark` ×7，产生 7 个连续 `\\footnotetext`。混合了定义性信息（degeneracy 定义）、评估细节（oracle headroom）、confound 声明（epoch difference）和 per-dataset seed details（×3）。审稿人需在表格和页底之间反复跳转。\n- 建议：将 degeneracy 定义移至首次使用处（Section 3 或 Section 4.1）；per-dataset seed details 整合为 appendix table；SciERC greedy F1 差异解释合并为一个 \"evaluation note\"。目标：≤2 个脚注。\n\n**W7** [Warning] **Greedy F1 数值不一致**\n- 具体位置：SciERC greedy F1 在多个 tables 中出现不同值：0.640（Table N-scaling, appendix）、0.644（Table 3/fewnerd）、0.645（Table 2/selection）、0.650（Table hidden_probe + epoch 3-epoch）。\n- 每个差异都有脚注解释（seed, aggregation, gold-filtering protocol），但审稿人看到同一 baseline 有 4 个数值会产生困惑。\n- 建议：统一所有 tables 的 evaluation protocol，或在 Section 3.3（Evaluation Framework）中提前声明存在哪些 protocol variants 及原因。\n\n### Info\n\n**W8** [Info] **Appendix 残留内部实验标识**\n- 具体位置：Appendix Table~\\ref{tab:n_scaling_selection} caption (\"exp\\_025\"), Table~\\ref{tab:epoch_confound} caption (\"exp\\_027\")\n- 问题：内部实验管理标识符应在投稿前删除。\n- 影响：不直接泄露身份但不 professional。\n\n**W9** [Info] **\"Capability trap\" 措辞**\n- \"Trap\" 暗示不可逃脱的困境，但论文自己展示了 temperature（Section 5, Table~\\ref{tab:t_degeneracy}）和 early stopping（Appendix~\\ref{app:epoch_confound}）可部分控制 degeneracy。\n- 建议改为 \"capability-diversity tension\" 或 \"capability-selection tradeoff\"。\n\n**W10** [Info] **少量 -ing 短语**\n- \"indicating moderate quality prediction but poor selection utility\"（experiments.tex:183）\n- \"indicating the bottleneck...\"（discussion.tex:20）\n- \"revealing a tension...\"（introduction.tex:18）\n- 均可接受，但建议改写以避免残余 AI writing pattern。\n\n---\n\n## Questions\n\n**Q1** Few-NERD 使用 3 epochs 而 SciERC/CoNLL 使用 5 epochs（Table 3 脚注 4）。5-epoch Few-NERD control degeneracy 上升到 31% 且 LP gain 减半至 +0.62pp。SciERC 在 3 epochs 时 degeneracy 仅 6.4%（Table~\\ref{tab:epoch_scierc}），但 LP 仍无显著增益（-1.18pp）。能否提供 3-epoch SciERC 的 within-instance alignment ρ 和 LP selection 的 3-seed mean？这将有助于判断 epoch confound 在多大程度上解释了 SciERC-vs-Few-NERD 的差异。\n\n**Q2** Hidden state probe（Section 4.5）使用 mean-pooled final-layer hidden state。NER 的 quality 信息可能集中在 entity span 位置。是否尝试过 entity-position-only pooling 或 attention-weighted pooling？这与 entity-token LP 的 4× 更高 variance 但更差 selection（Section 5, LP compression）形成对比——entity-level information 是否在 hidden state 中同样存在 aliasing？\n\n**Q3** Per-entity-type analysis within Few-NERD（ρ=-0.881, p=0.004, n=8）的 effective df 问题：论文注明 \"types share model and tokenizer, so effective degrees of freedom may be lower than 6\"。如果 effective df 为 4（考虑到 shared model + shared temperature + shared sampling strategy），p-value 会升至多少？这条证据线的 robustness 对 \"两条件\" 框架的支撑有多关键？\n\n**Q4** 论文在 Limitations 中提到 Self-Certainty (Kang et al. 2025) 和 P(True) (Kadavath et al. 2022) 作为未测试的 per-sample signals。LP 是当前唯一的 per-sample signal 且是唯一有正面 selection 结果的信号。如果存在更多 per-sample signals 且它们 also fail，这会加强 \"gap is fundamental\" 的论证；如果它们 succeed，则 gap 是 LP-specific 的。为什么没有在实验中包含这些 readily available 的 signals？\n\n**Q5** DALS 的 τ=0.05 threshold 来自 non-tied analysis 的 same data。如果用 leave-one-out 或 held-out validation 来选择 τ，DALS 的 gain 是否会 substantially change？当前的 evaluation 存在 circular optimization 风险。\n\n---\n\n## Missing References\n\n1. **Semantic entropy (Farquhar et al., Nature 2024)**：与 semantic uncertainty (Kuhn et al. 2023, 已引) 相关但不同；更直接涉及结构化输出的 uncertainty 度量，且是高影响力工作。当前 Related Work 引用了 Kuhn et al. 但未引 Farquhar et al.。\n\n2. **Best-of-N for code generation (Chen et al. 2021, \"Evaluating Large Language Models Trained on Code\")**：pass@k 是 best-of-N 在 code generation 中的经典成功案例。当前仅引 Shi et al. (2022) 的 execution-based MBR。补充 pass@k 的讨论能更好地 contextualize NER 中 selection 失败的 structural reasons（code 有 execution oracle，NER 没有）。\n\n3. **NER-specific LLM uncertainty**：Related Work 中 NER-specific confidence 仅引用 pre-LLM 工作（Culotta 2004, Mejer 2010）。如果存在 2023+ 的 LLM-based NER calibration/confidence 工作，应被讨论。当前从 general surveys 直接跳到本文，缺少 NER-specific 中间层。\n\n---\n\n## Detailed Comments\n\n### Narrative Coherence Check\nAbstract → Introduction → Method → Experiments → Discussion → Conclusion 的主线检查：\n\n- **Abstract**（sections/abstract.tex）：4-question 结构完整（问题、方法、发现、机制）。\"LP\" 在 Abstract 中首次出现时有括号展开 \"[LP]\" ——acceptable但不完全显式（\"log-probability [LP]\" 而非 \"log-probability (LP, hereafter)\"）。信息密度适当。\n- **Introduction**（sections/introduction.tex）：叙事线完整：existing conflation of QE and selection → partial overlap breaks majority voting → our distinction → mechanisms → contributions。Contribution list 过长（contribution 2 有 4 行含子句，contribution 3 有 3 行），建议精简数值。\n- **Related Work**（sections/related_work.tex）：4 个清晰的 paragraph 主题（self-consistency, consistency for IE, uncertainty/MBR, BoN with verifiers）。不是论文堆砌——每段有明确的 positioning sentence（\"We extend...\", \"We show correlation is necessary but not sufficient\", \"Our diagnosis is complementary\"）。Yao et al. (2026) 的区分到位（Related Work line 9）。\n- **Method**（sections/method.tex）：5 种信号定义清楚，per-sample vs. instance-level 区分从 Section 3.1 建立。Evaluation framework 简洁但完整。\n- **Experiments**（sections/experiments.tex）：Results 按 QE → selection gap → cross-dataset → robustness → hidden probes 递进。逻辑清晰。\n- **Discussion**（sections/discussion.tex）：过长（见 W1），但内容本身与前文一致。\"Capability trap\" 段落的 hedging adequate（\"observational\", \"does not establish causality\"）。\n- **Conclusion**（sections/conclusion.tex）：有效总结，无新信息引入。末句有力。\n\n**主线统一性判断**：Abstract 到 Conclusion 的主线基本一致——\"QE works, selection doesn't, here's why\"。唯一的主线偏移是 DALS 在 Discussion 中的引入（W3），它打断了诊断性叙事。\n\n### Contribution-Evidence 匹配\n\n| Contribution | 对应 Section/Table | 证据充分性 |\n|---|---|---|\n| 1. QE framework | Table 1, Table robustness, Table multiseed | ✓ 充分 |\n| 2. Two mechanisms (degeneracy + alignment) | Table 2, Table 3, Table degeneracy, Fig degeneracy_scatter | ⚠ Cross-dataset 仅 n=3 datasets; per-entity-type p=0.004 但 effective df 存疑 |\n| 3. Practical conditions for LP selection | Table 3, Table within_rho, Discussion regime boundaries | ⚠ 15% 阈值来自 2 个相邻 data points；ρ≈0.3 threshold 的 precision 未 validated |\n\n### AI 写作痕迹检查\n- **Em-dash（—）**：全文零使用。✓\n- **En-dash（–）**：仅用于数字范围（4B–8B, 14–59%），正确用法。✓\n- **-ing 结尾短语**：3 处（experiments.tex:183, discussion.tex:20, introduction.tex:18），均在可接受范围。⚠ 建议改写。\n- **过度分段**：无。段落长度适当（5-8 句）。✓\n- **黑名单用词**：无 \"delve/leverage/utilize/facilitate/myriad/plethora/paradigm shift\"。✓\n- **\"Furthermore/Moreover/Additionally\"**：零使用。✓\n- **整体判断**：写作质量高，AI 痕迹控制得当。\n\n### 格式合规性\n- `\\documentclass[11pt]{article}` + `\\usepackage[review]{acl}` ✓\n- `\\author{Anonymous}` ✓\n- 行号：review option 自动生成 ✓\n- Limitations section：存在，不含在正文页数中 ✓\n- Ethics Statement：存在 ✓\n- **正文超限**：~9.5 页 ✗（见 W1）\n- Appendix 内部标识：\"exp\\_025\"、\"exp\\_027\" ✗（见 W8）\n\n### References 完整性\n引用验证结果（via verify_references tool）：\n- 64 bib entries, 97 citations, 0 orphan, 0 missing\n- 3 online not found（hobelsberger2025, lightman2024, venktesh2025——可能为近期 preprint 未被索引）\n- 4 mismatch（author name 格式差异，非虚假引用）\n- **无虚假引用**\n\n---\n\n## Overall Assessment\n\n**Overall**: 3 / 5（Findings track acceptance recommended）\n\n**Soundness**: 3.5 / 5 — 实验设计和统计方法优秀，但 primary test bed power 不足（W5），\"两条件\" 框架跨数据集支撑仅 3 点（Q3），greedy F1 不一致增加复现复杂度（W7）。\n\n**Excitement**: 2.5 / 5 — Per-sample vs. instance-level 的概念区分有价值（S1），hidden state probe 封堵 alternative explanation 巧妙（S4），但核心发现是 negative result 且 actionable output 有限。Named concepts 的新颖性增量相对 MBR 和 diversity collapse 文献有限（W4）。\n\n**Reproducibility**: 4 / 5 — Training config 详细（Appendix Table training），prompt template 和 evaluation protocol 清楚，代码承诺 release。唯一扣分：greedy F1 多个数值的 protocol 差异增加复现难度。\n\n**Confidence**: 4 / 5 — 仔细阅读全文含完整 appendix；NER evaluation、MBR decoding、uncertainty estimation 是熟悉领域。\n\n**一句话总结**：实验严谨、统计透明的诊断性研究，但正文超页限是 hard blocker，title scope 过宽（NER 为主却声称 \"Structured IE\"），新颖性增量有限（对已知现象在 NER 中的系统验证和命名），且 headline positive result 的 primary test bed（SciERC）统计 power 不足。\n\n---\n\n## 交叉回应 Reviewer 1\n\n### [AGREE] R1-N1: \"两条件\"框架经验基础不足\n同意。跨数据集仅 3 个 data points（论文自标 \"exploratory given 5+ confounds\", experiments.tex:127），15% 阈值来自 Few-NERD per-entity-type 两个相邻点（Person 13.4% vs Art 19.8%）。我的 W4 从不同角度指出相同问题：这些 named concepts 是 useful empirical characterizations 而非 validated theoretical thresholds。两条评审意见指向同一 root issue：framework claim strength > evidence strength。建议作者降低 claim 强度，使用 \"empirical pattern\" / \"approximate boundary in our data\" 而非 \"two conditions\" / \"15% threshold\"。\n\n### [AGREE] R1-N2: Epoch confound 对 headline result 的影响\n同意这是重要问题。5-epoch Few-NERD 的 LP gain 降至 +0.62pp，接近 SciERC 的 +0.61pp（Table 3），框架区分力确实减弱。但我认为 severity 需要 nuance：\n\n(a) **正面**：5-epoch Few-NERD 仍然是 positive selection（+0.62pp），而 SciERC 5-epoch 的 3-seed mean 是 +0.04±0.48pp——方向一致但 magnitude 差异仍在（n=32,565 vs. n=529 的 power 差异是关键）。\n\n(b) **论文已在正文提及但 insufficient**：experiments.tex:124 提到 \"halves LP gains, though selection remains positive\"，但这是一句话处理一个 major confound。需要在正文中正式呈现 epoch-controlled comparison（当前仅在 appendix Table~\\ref{tab:epoch_confound}）。\n\n(c) **从新颖性角度**：如果 LP selection 的 positive result 本质上取决于 \"使用 under-trained checkpoint\"，那么 practical value 就需要与 early stopping 的 standard practice 对齐——论文在 Discussion:38 指出 \"Standard early stopping practice thus naturally selects the low-degeneracy regime\"，这是一个合理的 counter-argument，但应更 prominent。\n\n### [AGREE] R1-W1: SciERC underpowered\n与我的 W5 完全一致。SciERC n=529, MDE≈1.5pp, 3-seed mean LP Δ=+0.04±0.48pp——这个 test bed 对 LP selection 的 effect size 没有 discriminative power。Few-NERD 应被 repositioned 为 primary。\n\n### [AGREE with refinement] R1-W2: DALS data-snooping 风险\n与我的 W3 互补。R1 关注 ε=0.05 threshold 的 data-snooping 问题；我的 W3 关注 DALS 的 positioning 问题。两者可以统一为一个 recommendation：将 DALS 移至 appendix 作为 exploratory extension，同时在 appendix 中报告 held-out validation 或 leave-one-out 的 ε sensitivity。这同时解决 data-snooping concern 和 positioning conflict。\n\n### [AGREE] R1-W3: \"Capability trap\" 措辞过强\n与我的 W9 一致。3 个 scale points 的 observational trend 不足以支撑 \"trap\" 这样的 strong terminology。R1 和我都建议弱化措辞。\n\n---\n\n## 对 Director 问题的回应\n\n### N1 和 W2（新颖性有限）是否指向同一问题？\n是的，但角度不同。R1-N1 关注框架的**经验基础**（data points 不够），我的 W4 关注框架的**概念新颖性**（对已知现象的 domain-specific verification）。两者共同指向：claim strength > evidence strength + novelty。如果作者 (a) 降低 claim 强度为 \"empirical characterization\"，(b) 增加 1-2 个数据集或 IE 子任务的验证，这两个问题可以同时 mitigate。\n\n### Epoch confound 对新颖性的影响\n如果 5-epoch 统一后 Few-NERD 和 SciERC 的 LP gain 接近（+0.62pp vs. +0.61pp），论文的区分性故事（\"Few-NERD works because of low degeneracy\"）需要修正为 \"Few-NERD works because of both low degeneracy AND strong alignment, even after controlling for epoch\"——关键是 within-instance alignment 在 Few-NERD 上仍然显著高于 SciERC（ρ≈0.5 vs. ≈0.24，Table~\\ref{tab:within_rho}）。论文已有这个 argument（Discussion:32），但需要 promote to main narrative。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）\n\n---\n\n## Summary\n\n本文研究 self-consistency 类 confidence signals 在 LLM-based NER 中 quality estimation（QE）与 sample selection 之间的脱钩现象。在 4 个 NER benchmark、2 个 8B 模型家族和 1 个 4B ablation 上评估 5 种信号，发现所有信号均可实现可靠的 QE（ρ 达 0.45, AUROC 达 0.82），但仅 LP 在特定条件下（Few-NERD, degeneracy <15%, alignment ρ≈0.5）取得显著 selection 增益（+1.39pp）。论文诊断出两个阻塞机制——instance degeneracy 和 weak LP-quality alignment，合称 correlation-selection gap。Hidden state probes 进一步证明即使模型内部表示包含更丰富信息，selection gap 依然存在。\n\n---\n\n## Strengths\n\n**S1** [概念框架] Per-sample vs. instance-level signal 的区分（Section 3.1）是论文最有洞察力的贡献。4/5 信号是 instance-level aggregates，对 selection 无信息量 by construction——这个 observation 直接解释了为什么高 ρ 不能转化为 selection，比泛泛报告\"没有信号有效\"更有诊断价值。这个框架对后续 test-time scaling 研究在结构化输出上的工作有指导意义。\n\n**S2** [实验系统性] 4 个数据集的角色设计（WNUT-17 signal-collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling）构成清晰的难度梯度。每个数据集服务于明确的实验功能，不是简单的\"多数据集堆砌\"。多种 ablation（temperature, LoRA rank, epoch, N-scaling, free-form decoding, hidden state probes, DeBERTa verifier, supervised combination）系统地排除 alternative explanations。\n\n**S3** [统计严谨性] Bootstrap CI（B=10,000）、TOST equivalence testing（含 external anchors 修正 circularity）、MDE 计算（明确 SciERC n=529 的 power limitation）、Bonferroni correction。Non-tied subset positive finding（+2.9pp, p=0.004）经 Bonferroni 校正后仍 significant。这在 NLP 论文中罕见。\n\n**S4** [Hidden state probe 实验] Section 4.5 直接测试了\"需要更强信号\"这一 natural follow-up。MLP probe ρ=0.388（比 LP 高 37%）但 selection 反而更差（gap closure -5.1% vs. +4.8%），有力封堵了\"bottleneck 在 information loss\"的 alternative explanation，将 diagnosis 推进到 diminishing marginal returns。\n\n**S5** [Limitations 透明度] 主动报告所有已知弱点：SciERC seed sensitivity（σ=0.48pp）、epoch confound（3 vs. 5 epochs）、scale gap（4B-8B only）、未测试的 per-sample signals（Self-Certainty, P(True)）、ε threshold 的 post-hoc 性质。透明度超过大多数投稿论文。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1** [Critical] **正文页数超限（~9.5 页 vs. 8 页限制）**\n- 具体位置：Section 5 (Discussion) 延续到 page 9+, Section 6 (Conclusion) 从 page 9 开始并延伸到 page 10, Limitations 也在 page 10。\n- 问题：ACL 长文正文 ≤8 页（不含 Limitations/Ethics/References）。通过 pdftotext 分析确认 Conclusion 在 page 9 开始、page 10 结束，Limitations 在 page 10 中部开始。主体内容约 9.5 页。\n- 为什么影响接收：格式不合规是 desk-reject 级别问题。\n- 建议：Discussion 是主要来源。建议将 DALS 段落完整移至 appendix（见 W3）；\"LP compression mechanisms\" 4 个机制仅用 1-2 句各，适合 appendix；\"Regime boundaries\" 段落过于 detailed（含完整 decision rule 和所有数值条件），压缩为 3 句 refer appendix。Contribution list 中 contribution 2（4 行）和 3（3 行）的数值细节也可精简。\n\n**W2** [Critical] **Title scope 过宽（R2-N3）**\n- 具体位置：Title \"Structured Information Extraction\" vs. 实际内容\n- 问题：Title 声称 \"Structured Information Extraction\"，但实验覆盖：\n  - NER：4 个 benchmark（SciERC, Few-NERD, CoNLL-2003, WNUT-17）——这是论文的全部主线\n  - RE：仅 SciERC RE，全文标注为 \"exploratory single-benchmark analysis\"（Appendix Section L, line 692），且结果全部在 appendix\n  - 无 event extraction、slot filling、open IE 或其他 IE 子任务\n- \"Structured IE\" 暗示的覆盖度远超实际内容。审稿人看到 title 会预期至少 2 个 IE 子任务有 substantive coverage，但 RE 被明确标为 exploratory 且仅用 SciERC 单一 benchmark。\n- 建议两个方案：\n  (a) **修改 title**：改为 \"...Fail to Scale LLM-Based Named Entity Recognition\" 或 \"...Fail to Scale Structured Output Selection\"。前者精确但限缩 scope，后者保留 generality 但不 overclaim。\n  (b) **提升 RE 实验**：将 RE 从 exploratory appendix 升级为正文中的 secondary evaluation，至少加一个 RE benchmark 以支撑 \"IE\" 这个 claim。\n  在当前状态下，建议方案 (a)。\n\n### Warning\n\n**W3** [Warning] **DALS 定位与论文主线冲突**\n- 具体位置：Discussion Section 5, \"From diagnosis to selection\" 段落\n- 问题：论文核心定位是 diagnostic study（诊断 correlation-selection gap），但 Discussion 中引入 DALS（Degeneracy-Aware LP Selection）作为一个具体的 selection method。这产生两个问题：\n  (1) 如果 DALS 是 contribution，应在 Method section 正式定义，有独立实验表格，并列入 contribution list。当前 DALS 仅在 Discussion 中描述，没有独立评估。\n  (2) DALS 结果 seed-sensitive（SciERC: +0.19 to +1.14pp across seeds），CoNLL 仍 degradation（-0.87pp）。将如此 preliminary 的结果放在 Discussion 中模糊了论文的 contribution 边界。\n- 建议：将 DALS 移至 appendix 作为 \"exploratory extension\"，与 RE extension 平行处理。Discussion 的 \"From diagnosis to selection\" 段落可保留 1-2 句作为 future direction pointer。这同时有助于解决 W1（页数超限）。\n\n**W4** [Warning] **新颖性增量需要更精确的定位**\n- 问题：论文的核心贡献是对已知 general phenomena 在 NER 特定 domain 中的系统验证和机制命名。逐项评估：\n  (a) **Correlation-selection gap**：QE correlation ≠ selection utility 在 MBR 文献中是已知问题。Eikema et al. (2025) 的 utility misalignment 是 complementary（论文正确指出，Introduction line 16, Related Work line 18）。本文的 specific contribution 是将 bottleneck 归因于 degeneracy 而非 utility misalignment——这是一个 domain-specific refinement，not a new general principle。\n  (b) **Instance degeneracy**：Fine-tuned models + constrained decoding 产生低多样性是可预测的。Kirk et al. (2024) 和 Yun et al. (2025) 已讨论 diversity collapse。本文的贡献在于将这些现象量化为 per-instance metric 并展示其对 selection 的直接影响——是 useful empirical characterization，但不构成方法论突破。\n  (c) **Capability trap**：基于 3 scale points（3B, 4B, 8B）的 observational trend。论文正确使用 hedging language（\"does not establish causality\", Discussion line 46），但 \"trap\" 这个术语暗示了超出证据的普遍性。在 70B+ 模型上的行为完全未知——更大模型可能同时减少 degeneracy（更强的生成能力）和改善 alignment。\n- EMNLP 接受 negative/diagnostic results 的前提是 (i) robustness 充分、(ii) actionable insight 有意义。条件 (i) 满足良好。条件 (ii) 部分满足：QE guidelines 有实用价值，但 selection 方面的 actionable output 有限。\n- 建议：在 Introduction 中更明确地框定 contribution 类型——\"We provide the first systematic empirical characterization of...\" 而非暗示 theoretical framework。这会让审稿人以 empirical contribution 标准评判，降低 novelty 期望。\n\n**W5** [Warning] **SciERC 作为 primary test bed 统计 power 不足**\n- 具体位置：Section 4.1（\"primary medium-difficulty test bed\"）, Table 2, Table 3\n- 问题：SciERC n=529, MDE≈1.5pp at 80% power。论文报告 LP 在 SciERC 上 +0.61pp（p=0.193）——这无法区分 \"真的没有效果\" 和 \"效果太小检测不到\"。3-seed mean 更是 +0.04±0.48pp，本质上是 noise。\n- Few-NERD（n=32,565, MDE≈0.22pp）才有 definitive power：LP +1.39pp, p<0.001, 3-seed std 仅 0.04pp。\n- 建议：将 Few-NERD 重新定位为 primary test bed（definitive evidence for LP selection）。SciERC 应被明确标注为 \"medium-difficulty, underpowered exploratory test bed\"，其 negative result 应被 framed 为 \"consistent with but not confirming the null\"。当前叙事结构（SciERC primary → Few-NERD contrast）弱化了论文最强的实证结果。\n\n**W6** [Warning] **Table 3 的 7 个连续脚注**\n- 具体位置：Section 4.3, Table~\\ref{tab:fewnerd}, experiments.tex lines 101-120\n- 问题：Caption 中 `\\protect\\footnotemark` ×7，产生 7 个连续 `\\footnotetext`。混合了定义性信息（degeneracy 定义）、评估细节（oracle headroom）、confound 声明（epoch difference）和 per-dataset seed details（×3）。审稿人需在表格和页底之间反复跳转。\n- 建议：将 degeneracy 定义移至首次使用处（Section 3 或 Section 4.1）；per-dataset seed details 整合为 appendix table；SciERC greedy F1 差异解释合并为一个 \"evaluation note\"。目标：≤2 个脚注。\n\n**W7** [Warning] **Greedy F1 数值不一致**\n- 具体位置：SciERC greedy F1 在多个 tables 中出现不同值：0.640（Table N-scaling, appendix）、0.644（Table 3/fewnerd）、0.645（Table 2/selection）、0.650（Table hidden_probe + epoch 3-epoch）。\n- 每个差异都有脚注解释（seed, aggregation, gold-filtering protocol），但审稿人看到同一 baseline 有 4 个数值会产生困惑。\n- 建议：统一所有 tables 的 evaluation protocol，或在 Section 3.3（Evaluation Framework）中提前声明存在哪些 protocol variants 及原因。\n\n### Info\n\n**W8** [Info] **Appendix 残留内部实验标识**\n- 具体位置：Appendix Table~\\ref{tab:n_scaling_selection} caption (\"exp\\_025\"), Table~\\ref{tab:epoch_confound} caption (\"exp\\_027\")\n- 问题：内部实验管理标识符应在投稿前删除。\n- 影响：不直接泄露身份但不 professional。\n\n**W9** [Info] **\"Capability trap\" 措辞**\n- \"Trap\" 暗示不可逃脱的困境，但论文自己展示了 temperature（Section 5, Table~\\ref{tab:t_degeneracy}）和 early stopping（Appendix~\\ref{app:epoch_confound}）可部分控制 degeneracy。\n- 建议改为 \"capability-diversity tension\" 或 \"capability-selection tradeoff\"。\n\n**W10** [Info] **少量 -ing 短语**\n- \"indicating moderate quality prediction but poor selection utility\"（experiments.tex:183）\n- \"indicating the bottleneck...\"（discussion.tex:20）\n- \"revealing a tension...\"（introduction.tex:18）\n- 均可接受，但建议改写以避免残余 AI writing pattern。\n\n---\n\n## Questions\n\n**Q1** Few-NERD 使用 3 epochs 而 SciERC/CoNLL 使用 5 epochs（Table 3 脚注 4）。5-epoch Few-NERD control degeneracy 上升到 31% 且 LP gain 减半至 +0.62pp。SciERC 在 3 epochs 时 degeneracy 仅 6.4%（Table~\\ref{tab:epoch_scierc}），但 LP 仍无显著增益（-1.18pp）。能否提供 3-epoch SciERC 的 within-instance alignment ρ 和 LP selection 的 3-seed mean？这将有助于判断 epoch confound 在多大程度上解释了 SciERC-vs-Few-NERD 的差异。\n\n**Q2** Hidden state probe（Section 4.5）使用 mean-pooled final-layer hidden state。NER 的 quality 信息可能集中在 entity span 位置。是否尝试过 entity-position-only pooling 或 attention-weighted pooling？这与 entity-token LP 的 4× 更高 variance 但更差 selection（Section 5, LP compression）形成对比——entity-level information 是否在 hidden state 中同样存在 aliasing？\n\n**Q3** Per-entity-type analysis within Few-NERD（ρ=-0.881, p=0.004, n=8）的 effective df 问题：论文注明 \"types share model and tokenizer, so effective degrees of freedom may be lower than 6\"。如果 effective df 为 4（考虑到 shared model + shared temperature + shared sampling strategy），p-value 会升至多少？这条证据线的 robustness 对 \"两条件\" 框架的支撑有多关键？\n\n**Q4** 论文在 Limitations 中提到 Self-Certainty (Kang et al. 2025) 和 P(True) (Kadavath et al. 2022) 作为未测试的 per-sample signals。LP 是当前唯一的 per-sample signal 且是唯一有正面 selection 结果的信号。如果存在更多 per-sample signals 且它们 also fail，这会加强 \"gap is fundamental\" 的论证；如果它们 succeed，则 gap 是 LP-specific 的。为什么没有在实验中包含这些 readily available 的 signals？\n\n**Q5** DALS 的 τ=0.05 threshold 来自 non-tied analysis 的 same data。如果用 leave-one-out 或 held-out validation 来选择 τ，DALS 的 gain 是否会 substantially change？当前的 evaluation 存在 circular optimization 风险。\n\n---\n\n## Missing References\n\n1. **Semantic entropy (Farquhar et al., Nature 2024)**：与 semantic uncertainty (Kuhn et al. 2023, 已引) 相关但不同；更直接涉及结构化输出的 uncertainty 度量，且是高影响力工作。当前 Related Work 引用了 Kuhn et al. 但未引 Farquhar et al.。\n\n2. **Best-of-N for code generation (Chen et al. 2021, \"Evaluating Large Language Models Trained on Code\")**：pass@k 是 best-of-N 在 code generation 中的经典成功案例。当前仅引 Shi et al. (2022) 的 execution-based MBR。补充 pass@k 的讨论能更好地 contextualize NER 中 selection 失败的 structural reasons（code 有 execution oracle，NER 没有）。\n\n3. **NER-specific LLM uncertainty**：Related Work 中 NER-specific confidence 仅引用 pre-LLM 工作（Culotta 2004, Mejer 2010）。如果存在 2023+ 的 LLM-based NER calibration/confidence 工作，应被讨论。当前从 general surveys 直接跳到本文，缺少 NER-specific 中间层。\n\n---\n\n## Detailed Comments\n\n### Narrative Coherence Check\nAbstract → Introduction → Method → Experiments → Discussion → Conclusion 的主线检查：\n\n- **Abstract**（sections/abstract.tex）：4-question 结构完整（问题、方法、发现、机制）。\"LP\" 在 Abstract 中首次出现时有括号展开 \"[LP]\" ——acceptable但不完全显式（\"log-probability [LP]\" 而非 \"log-probability (LP, hereafter)\"）。信息密度适当。\n- **Introduction**（sections/introduction.tex）：叙事线完整：existing conflation of QE and selection → partial overlap breaks majority voting → our distinction → mechanisms → contributions。Contribution list 过长（contribution 2 有 4 行含子句，contribution 3 有 3 行），建议精简数值。\n- **Related Work**（sections/related_work.tex）：4 个清晰的 paragraph 主题（self-consistency, consistency for IE, uncertainty/MBR, BoN with verifiers）。不是论文堆砌——每段有明确的 positioning sentence（\"We extend...\", \"We show correlation is necessary but not sufficient\", \"Our diagnosis is complementary\"）。Yao et al. (2026) 的区分到位（Related Work line 9）。\n- **Method**（sections/method.tex）：5 种信号定义清楚，per-sample vs. instance-level 区分从 Section 3.1 建立。Evaluation framework 简洁但完整。\n- **Experiments**（sections/experiments.tex）：Results 按 QE → selection gap → cross-dataset → robustness → hidden probes 递进。逻辑清晰。\n- **Discussion**（sections/discussion.tex）：过长（见 W1），但内容本身与前文一致。\"Capability trap\" 段落的 hedging adequate（\"observational\", \"does not establish causality\"）。\n- **Conclusion**（sections/conclusion.tex）：有效总结，无新信息引入。末句有力。\n\n**主线统一性判断**：Abstract 到 Conclusion 的主线基本一致——\"QE works, selection doesn't, here's why\"。唯一的主线偏移是 DALS 在 Discussion 中的引入（W3），它打断了诊断性叙事。\n\n### Contribution-Evidence 匹配\n\n| Contribution | 对应 Section/Table | 证据充分性 |\n|---|---|---|\n| 1. QE framework | Table 1, Table robustness, Table multiseed | ✓ 充分 |\n| 2. Two mechanisms (degeneracy + alignment) | Table 2, Table 3, Table degeneracy, Fig degeneracy_scatter | ⚠ Cross-dataset 仅 n=3 datasets; per-entity-type p=0.004 但 effective df 存疑 |\n| 3. Practical conditions for LP selection | Table 3, Table within_rho, Discussion regime boundaries | ⚠ 15% 阈值来自 2 个相邻 data points；ρ≈0.3 threshold 的 precision 未 validated |\n\n### AI 写作痕迹检查\n- **Em-dash（—）**：全文零使用。✓\n- **En-dash（–）**：仅用于数字范围（4B–8B, 14–59%），正确用法。✓\n- **-ing 结尾短语**：3 处（experiments.tex:183, discussion.tex:20, introduction.tex:18），均在可接受范围。⚠ 建议改写。\n- **过度分段**：无。段落长度适当（5-8 句）。✓\n- **黑名单用词**：无 \"delve/leverage/utilize/facilitate/myriad/plethora/paradigm shift\"。✓\n- **\"Furthermore/Moreover/Additionally\"**：零使用。✓\n- **整体判断**：写作质量高，AI 痕迹控制得当。\n\n### 格式合规性\n- `\\documentclass[11pt]{article}` + `\\usepackage[review]{acl}` ✓\n- `\\author{Anonymous}` ✓\n- 行号：review option 自动生成 ✓\n- Limitations section：存在，不含在正文页数中 ✓\n- Ethics Statement：存在 ✓\n- **正文超限**：~9.5 页 ✗（见 W1）\n- Appendix 内部标识：\"exp\\_025\"、\"exp\\_027\" ✗（见 W8）\n\n### References 完整性\n引用验证结果（via verify_references tool）：\n- 64 bib entries, 97 citations, 0 orphan, 0 missing\n- 3 online not found（hobelsberger2025, lightman2024, venktesh2025——可能为近期 preprint 未被索引）\n- 4 mismatch（author name 格式差异，非虚假引用）\n- **无虚假引用**\n\n---\n\n## Overall Assessment\n\n**Overall**: 3 / 5（Findings track acceptance recommended）\n\n**Soundness**: 3.5 / 5 — 实验设计和统计方法优秀，但 primary test bed power 不足（W5），\"两条件\" 框架跨数据集支撑仅 3 点（Q3），greedy F1 不一致增加复现复杂度（W7）。\n\n**Excitement**: 2.5 / 5 — Per-sample vs. instance-level 的概念区分有价值（S1），hidden state probe 封堵 alternative explanation 巧妙（S4），但核心发现是 negative result 且 actionable output 有限。Named concepts 的新颖性增量相对 MBR 和 diversity collapse 文献有限（W4）。\n\n**Reproducibility**: 4 / 5 — Training config 详细（Appendix Table training），prompt template 和 evaluation protocol 清楚，代码承诺 release。唯一扣分：greedy F1 多个数值的 protocol 差异增加复现难度。\n\n**Confidence**: 4 / 5 — 仔细阅读全文含完整 appendix；NER evaluation、MBR decoding、uncertainty estimation 是熟悉领域。\n\n**一句话总结**：实验严谨、统计透明的诊断性研究，但正文超页限是 hard blocker，title scope 过宽（NER 为主却声称 \"Structured IE\"），新颖性增量有限（对已知现象在 NER 中的系统验证和命名），且 headline positive result 的 primary test bed（SciERC）统计 power 不足。\n\n---\n\n## 交叉回应 Reviewer 1\n\n### [AGREE] R1-N1: \"两条件\"框架经验基础不足\n同意。跨数据集仅 3 个 data points（论文自标 \"exploratory given 5+ confounds\", experiments.tex:127），15% 阈值来自 Few-NERD per-entity-type 两个相邻点（Person 13.4% vs Art 19.8%）。我的 W4 从不同角度指出相同问题：这些 named concepts 是 useful empirical characterizations 而非 validated theoretical thresholds。两条评审意见指向同一 root issue：framework claim strength > evidence strength。建议作者降低 claim 强度，使用 \"empirical pattern\" / \"approximate boundary in our data\" 而非 \"two conditions\" / \"15% threshold\"。\n\n### [AGREE] R1-N2: Epoch confound 对 headline result 的影响\n同意这是重要问题。5-epoch Few-NERD 的 LP gain 降至 +0.62pp，接近 SciERC 的 +0.61pp（Table 3），框架区分力确实减弱。但我认为 severity 需要 nuance：\n\n(a) **正面**：5-epoch Few-NERD 仍然是 positive selection（+0.62pp），而 SciERC 5-epoch 的 3-seed mean 是 +0.04±0.48pp——方向一致但 magnitude 差异仍在（n=32,565 vs. n=529 的 power 差异是关键）。\n\n(b) **论文已在正文提及但 insufficient**：experiments.tex:124 提到 \"halves LP gains, though selection remains positive\"，但这是一句话处理一个 major confound。需要在正文中正式呈现 epoch-controlled comparison（当前仅在 appendix Table~\\ref{tab:epoch_confound}）。\n\n(c) **从新颖性角度**：如果 LP selection 的 positive result 本质上取决于 \"使用 under-trained checkpoint\"，那么 practical value 就需要与 early stopping 的 standard practice 对齐——论文在 Discussion:38 指出 \"Standard early stopping practice thus naturally selects the low-degeneracy regime\"，这是一个合理的 counter-argument，但应更 prominent。\n\n### [AGREE] R1-W1: SciERC underpowered\n与我的 W5 完全一致。SciERC n=529, MDE≈1.5pp, 3-seed mean LP Δ=+0.04±0.48pp——这个 test bed 对 LP selection 的 effect size 没有 discriminative power。Few-NERD 应被 repositioned 为 primary。\n\n### [AGREE with refinement] R1-W2: DALS data-snooping 风险\n与我的 W3 互补。R1 关注 ε=0.05 threshold 的 data-snooping 问题；我的 W3 关注 DALS 的 positioning 问题。两者可以统一为一个 recommendation：将 DALS 移至 appendix 作为 exploratory extension，同时在 appendix 中报告 held-out validation 或 leave-one-out 的 ε sensitivity。这同时解决 data-snooping concern 和 positioning conflict。\n\n### [AGREE] R1-W3: \"Capability trap\" 措辞过强\n与我的 W9 一致。3 个 scale points 的 observational trend 不足以支撑 \"trap\" 这样的 strong terminology。R1 和我都建议弱化措辞。\n\n---\n\n## 对 Director 问题的回应\n\n### N1 和 W2（新颖性有限）是否指向同一问题？\n是的，但角度不同。R1-N1 关注框架的**经验基础**（data points 不够），我的 W4 关注框架的**概念新颖性**（对已知现象的 domain-specific verification）。两者共同指向：claim strength > evidence strength + novelty。如果作者 (a) 降低 claim 强度为 \"empirical characterization\"，(b) 增加 1-2 个数据集或 IE 子任务的验证，这两个问题可以同时 mitigate。\n\n### Epoch confound 对新颖性的影响\n如果 5-epoch 统一后 Few-NERD 和 SciERC 的 LP gain 接近（+0.62pp vs. +0.61pp），论文的区分性故事（\"Few-NERD works because of low degeneracy\"）需要修正为 \"Few-NERD works because of both low degeneracy AND strong alignment, even after controlling for epoch\"——关键是 within-instance alignment 在 Few-NERD 上仍然显著高于 SciERC（ρ≈0.5 vs. ≈0.24，Table~\\ref{tab:within_rho}）。论文已有这个 argument（Discussion:32），但需要 promote to main narrative。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1720 · 2026-05-18T13:06:44.798340+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 1721 · 2026-05-18T13:06:54.960896+00:00_

审稿意见已提交给 Review Director。

本轮审查覆盖了：
- **新颖性**：识别出 5 个 strengths 和 10 个 weaknesses（2 critical, 7 warning, 1 info），核心判断是论文实验严谨但新颖性增量有限且正文超页限
- **Title scope（R2-N3）**：明确指出 "Structured Information Extraction" 与实际内容（NER 为主 + 单一 exploratory RE）不匹配，建议修改 title 或提升 RE 实验
- **交叉回应 R1**：5 条全部 AGREE（N1 框架证据薄、N2 epoch confound、W1 SciERC underpowered、W2 DALS data-snooping、W3 capability trap），指出与我自己 findings 的交汇点和互补性
- **Overall**: 3/5（Findings track），Excitement 2.5/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 45

## Round 45

76 recorded events


### User

_source line 1722 · 2026-05-19T03:24:14.116384+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 叙事完整性 + 写作质量**

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition
- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）
- **目标 venue**: EMNLP 2026 Main Conference（经 ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式要求**: ACL 模板, 正文 ≤8 页 + unlimited references, double-blind, 必须包含 Limitations section

### 你需要重点审查的方面

1. **新颖性与贡献定位**
   - 三个 contribution 是否有足够的新颖性达到 EMNLP Main Conference 水平
   - 与 Yao et al. 2026（consistency for IE）的区分是否足够锐利
   - "Correlation-selection gap" 作为核心概念是否有足够的理论或实证深度
   - Entity-level construction 的新颖性评估（vs 标准 majority voting）
   - 诊断性论文（"when and why X fails"）在 EMNLP 的接受度

2. **叙事完整性与连贯性**
   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条连贯主线
   - 核心 framing（从 QE 到 selection gap 到 construction）的逻辑过渡是否平滑
   - 论文标题是否准确反映内容（标题暗示 negative result，但实际有 positive construction result）
   - Contributions 列表中每项是否有充分的 section/table 支撑

3. **Related Work 覆盖度**
   - 引用是否充分覆盖：self-consistency, MBR decoding, confidence estimation, NER/IE, selective prediction
   - 是否有重要的遗漏工作
   - Positioning 是否清晰（不是 survey 而是定位自身工作）

4. **写作质量（硬规则检查）**
   - 检查 em-dash (—) 和解释性 en-dash (–) 的使用
   - 检查 -ing 短语结尾模式
   - 检查过度分段
   - 检查 AI 写作痕迹（leverage, utilize, delve into, furthermore/moreover 连续使用等）
   - 专有名词首次出现是否有定义
   - Abstract 中缩写是否展开
   - 页数是否合规（正文 ≤8 页）

5. **格式合规性**
   - ACL 模板使用是否正确（\usepackage[review]{acl}）
   - 匿名化是否到位
   - Limitations section 位置是否正确
   - Ethics Statement 是否充实
   - Responsible NLP Research Checklist 是否认真填写

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1723 · 2026-05-19T03:24:24.235601+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1724 · 2026-05-19T03:24:24.286320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1725 · 2026-05-19T03:24:28.310369+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-19T03:24:29.818071+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1727 · 2026-05-19T03:24:29.920447+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-19T03:24:29.971040+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-19T03:24:30.022872+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1730 · 2026-05-19T03:24:35.245299+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommen
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6934
}
```

</details>

---


### Tool call

_source line 1731 · 2026-05-19T03:24:40.840265+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include: overall assessment, soundness, excitement/novelty, reproducibility, and any other rated dimensions. List the exact scale descriptions for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include: overall assessment, soundness, excitement/novelty, reproducibility, and any other rated dimensions. List the exact scale descriptions for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-19T03:24:41.144396+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-19T03:24:41.646761+00:00_

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
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition}
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
46	\section*{Responsible NLP Research Checklist}
47	\input{sections/checklist}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1734 · 2026-05-19T03:24:41.647116+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1735 · 2026-05-19T03:24:41.998414+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) where LP-quality alignment is strong, but gains are absent elsewhere despite ${\sim}$13~pp oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose two causes: instance degeneracy (13\textendash 87\%) and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations).
7	The correct self-consistency analogy for structured outputs is entity-level \textit{construction}: aggregating entities across samples improves F1 by $+0.88$ to $+1.67$\,pp ($p{<}0.005$) on datasets where instance-level selection fails or is marginal. Construction and LP selection are complementary, governed by LP-quality alignment; an alignment-based gating protocol correctly routes all three evaluated datasets.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-19T03:24:41.998892+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1737 · 2026-05-19T03:24:42.049337+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low instance degeneracy and adequate alignment are prese
…[truncated 4181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1738 · 2026-05-19T03:24:53.678553+00:00_

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
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: Could be considered for outstanding paper award (top 2.5%)."
- **4**: "Conference: Could be accepted to an *ACL conference."
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1**: "Do not resubmit: Has to be fully redone or not relevant to *ACL community."

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 12838
}
```

</details>

---


### Tool call

_source line 1739 · 2026-05-19T03:24:57.103748+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1740 · 2026-05-19T03:24:57.906798+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
9	
10	\paragraph{Consistency for structured IE.}
11	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
12	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
13	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised signal combination baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
14	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
15	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained de
…[truncated 2309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1741 · 2026-05-19T03:24:57.907178+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1742 · 2026-05-19T03:24:58.376425+00:00_

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
…[truncated 3629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 469
}
```

</details>

---


### Tool call

_source line 1743 · 2026-05-19T03:24:58.376897+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1744 · 2026-05-19T03:24:58.578222+00:00_

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
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments (ranking stability $\sigma{\leq}0.026$, Table~\ref{tab:multiseed}; sublinear gains beyond $N{=}8$, Appendix~\ref{app:n_scaling}).
18	Inference uses vLLM with constrained decoding \cite{willard2023guided} (seed protocol: Appendix~\ref{app:multiseed}).
19	
20	%% ===================================
…[truncated 21780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1745 · 2026-05-19T03:24:58.578610+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1746 · 2026-05-19T03:24:58.629102+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications.}
4	All signals achieve positive quality estimation across non-collapsed datasets, with rankings stable across model families and a 4B ablation (Table~\ref{tab:scale_ablation}; RE in Appendix~\ref{app:re_extension}).
5	For selection, LP gains are associated with strong LP-quality alignment (Table~\ref{tab:fewnerd}); structural signals uniformly degrade selection.
6	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
7	
8	\paragraph{Why the gap exists.}
9	Two factors constrain selection: \textit{instance degeneracy} (consensus-proximity) limits the available headroom, and \textit{weak LP-quality alignment} (per-sample) prevents exploiting the remainder.
10	Within non-degenerate instances, MBR utility \cite{eikema2022sampling} correlates positively with F1 (SJ median $\rho{=}0.524$), but 17.8\% (SciERC) to 48.4\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\ref{tab:degeneracy}).
11	LP is severely compressed (median range 0.041 nats; Table~\ref{tab:logprob_ties}), with within-instance $\rho(\text{LP}, \text{F1})$ ranging from 0.262 (SciERC) to 0.667 (Few-NERD; Table~\ref{tab:within_rho}).
12	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}).
13	An oracle tiebreaker within VC-equivalent groups recovers $+7.9$~pp, confirming per-sample signal exists but current signals cannot extract it (Appendices~\ref{app:n_scaling}, \ref{app:verbalized_confidence}, \ref{app:vc_quartile}).
14	Hidden state probes confirm richer information exists (SciERC MLP $\rho{=}0.388$ vs.\ LP $0.283$, $+37$\%), but the correlation-selection gap persists (gap closure $-5.1$\% v
…[truncated 4766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1747 · 2026-05-19T03:25:03.699434+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1748 · 2026-05-19T03:25:04.051095+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
4	Instance-level selection fails due to degeneracy and LP compression, but the correct self-consistency analogy for structured outputs is entity-level construction: LP-weighted entity aggregation yields $+1.67$\,pp on SciERC ($p{=}0.004$) and $+0.88$\,pp on Few-NERD ($p{<}0.001$).
5	Construction and LP selection are complementary, governed by LP-quality alignment; a alignment-based gating protocol routes the appropriate method per dataset.
6	For practitioners: use QE-based selective prediction when deployment requires reliability guarantees; apply entity construction when multi-sample generation is feasible; assess LP-alignment via held-out validation to choose between construction and LP selection.
7	As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1749 · 2026-05-19T03:25:04.051545+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1750 · 2026-05-19T03:25:04.503546+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
3	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app
…[truncated 1946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1751 · 2026-05-19T03:25:04.504017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1752 · 2026-05-19T03:25:05.106755+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract (4 claims) and Section~\ref{sec:introduction} (4 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released un
…[truncated 4179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1753 · 2026-05-19T03:25:05.257563+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1754 · 2026-05-19T03:25:05.609294+00:00_

File content (38782 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1755 · 2026-05-19T03:25:09.572444+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1756 · 2026-05-19T03:25:09.924266+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1757 · 2026-05-19T03:25:10.075337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1758 · 2026-05-19T03:25:10.176361+00:00_

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
…[truncated 8823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1759 · 2026-05-19T03:25:17.208607+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1760 · 2026-05-19T03:25:17.610398+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1761 · 2026-05-19T03:25:18.162705+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1762 · 2026-05-19T03:25:18.614681+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1763 · 2026-05-19T03:25:19.116754+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1764 · 2026-05-19T03:25:19.569010+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:68:Oracle & $0.775 \pm 0.001$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:69:Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:77:EM           & $0.637 \pm 0.001$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:78:VC           & $0.623 \pm 0.004$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:80:Random           & $0.610 \pm 0.003$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:213:Hidden Linear & $.179{\pm}.019$ & $.613{\pm}.002$ & $-$23.4 & \multicolumn{2}{c}{---} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:48:\quad LP & $T{=}0.7$ & 0.249 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:58:\quad SJ &  & $0.474{\pm}0.009$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:59:\quad FK &  & $0.467{\pm}0.009$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:60:\quad EM &  & $0.473{\pm}0.010$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:61:\quad VC &  & $0.470{\pm}0.006$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:62:\quad LP &  & $0.311{\pm}0.003$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514
…[truncated 2789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1765 · 2026-05-19T03:25:20.071436+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\textendash",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\textendash",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1766 · 2026-05-19T03:25:20.574409+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2:We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:3:We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using 4B\textendash 8B models.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:6:We diagnose two causes: instance degeneracy (13\textendash 87\%) and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:15:Two factors shape this gap: (a)~\textit{instance degeneracy}, the fraction of instances where all $N$ samples produce identical F1, (13\textendash 87\% across our benchmarks) limits the available headroom; (b)~\textit{LP-quality alignment} (within-instance $\rho(\text{LP}, \text{F1})$) determines whether LP can exploit the remaining headroom (\S\ref{sec:discussion}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:28:We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B\textendash 8B range; behavior at 70B+ scales remains an open question.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1767 · 2026-05-19T03:25:21.026300+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1768 · 2026-05-19T03:25:21.076950+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:3:\paragraph{Self-consistency and test-time scaling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:5:Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:6:Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:18:\paragraph{Uncertainty estimation and MBR decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:20:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:14:\paragraph{Models and sampling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:99:Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021ver
…[truncated 10132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1769 · 2026-05-19T03:25:27.299422+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "leverage|utilize|delve|facilitate|myriad|plethora|paradigm shift|Furthermore|Moreover|Additionally|It is worth noting|Notably,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "leverage|utilize|delve|facilitate|myriad|plethora|paradigm shift|Furthermore|Moreover|Additionally|It is worth noting|Notably,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 1770 · 2026-05-19T03:25:27.851796+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1771 · 2026-05-19T03:25:28.946381+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\textendash|--",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\textendash|--",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1772 · 2026-05-19T03:25:29.448314+00:00_

3:We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using 4B\textendash 8B models.
4:All signals achieve reliable QE ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
6:We diagnose two causes: instance degeneracy (13\textendash 87\%) and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1773 · 2026-05-19T03:25:29.498804+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1774 · 2026-05-19T03:26:37.677942+00:00_

&lt;persisted-output>
Output too large (57.2KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/toolu_01M4Zp3bTDUznCaEaiUuosWe.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 68, \"total_citations\": 109, \"unique_cited_keys\": 68, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 59, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 68179
}
```

</details>

---


### Tool call

_source line 1775 · 2026-05-19T03:26:56.231296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/toolu_01M4Zp3bTDUznCaEaiUuosWe.txt",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/toolu_01M4Zp3bTDUznCaEaiUuosWe.txt",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1776 · 2026-05-19T03:26:56.533907+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 68, \"total_citations\": 109, \"unique_cited_keys\": 68, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 59, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"ve
…[truncated 56617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1777 · 2026-05-19T03:27:16.360564+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1778 · 2026-05-19T03:27:17.263893+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1779 · 2026-05-19T03:27:17.314474+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1780 · 2026-05-19T03:27:17.365436+00:00_

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
…[truncated 14570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1781 · 2026-05-19T03:27:23.436305+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null | grep \"Pages\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null | grep \"Pages\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1782 · 2026-05-19T03:27:23.587257+00:00_

Pages:           36

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1783 · 2026-05-19T03:27:32.398271+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1784 · 2026-05-19T03:27:35.724481+00:00_

Error: result (6,809,998 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/mcp-agent-ml-research-pdf_to_images-1779161255447.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/mcp-agent-ml-research-pdf_to_images-1779161255447.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3326
}
```

</details>

---


### Tool call

_source line 1785 · 2026-05-19T03:27:38.987315+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "8-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "8-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1786 · 2026-05-19T03:27:39.960330+00:00_

Error: result (2,187,371 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/mcp-agent-ml-research-pdf_to_images-1779161259909.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/mcp-agent-ml-research-pdf_to_images-1779161259909.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 973
}
```

</details>

---


### Tool call

_source line 1787 · 2026-05-19T03:27:43.177278+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "9",
  "dpi": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "9",
    "dpi": "100"
  }
}
```

</details>

---


### Tool result

_source line 1788 · 2026-05-19T03:27:44.233537+00:00_

Error: result (440,964 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/mcp-agent-ml-research-pdf_to_images-1779161264198.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/47c883c1-a4ec-49bd-bd75-6c3717be954a/tool-results/mcp-agent-ml-research-pdf_to_images-1779161264198.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 1789 · 2026-05-19T03:27:49.459298+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', '-f', '8', '-l', '10', 'main.pdf', '-'], capture_output=True, text=True)\nprint(result.stdout[:3000] if result.stdout else 'pdftotext not available')\n\" 2>/dev/null || echo \"pdftotext not available, trying alternative\"",
  "description": "Extract text from pages 8-10 to check page boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', '-f', '8', '-l', '10', 'main.pdf', '-'], capture_output=True, text=True)\nprint(result.stdout[:3000] if result.stdout else 'pdftotext not available')\n\" 2>/dev/null || echo \"pdftotext not available, trying alternative\"",
    "description": "Extract text from pages 8-10 to check page boundaries"
  }
}
```

</details>

---


### Tool result

_source line 1790 · 2026-05-19T03:27:49.610267+00:00_

      Table 5: Hidden state probes vs. LP for sample selection                  Table 6: Entity-level construction vs. greedy decoding
      (5-fold CV × 3 seeds). ρ: Spearman correlation with                       (∆ macro F1; N =8, T =1.0, Qwen3-8B, matching Ta-
      per-sample F1. Sel. F1: selection F1. Gap%: oracle gap                    bles 2–3). LP: LP-weighted entity aggregation; Unif.:
      closure. SciERC greedy=0.644, oracle=0.775.                               frequency-based. θ=2/N for SciERC; 5-fold CV for
                                                                                others. p: paired bootstrap vs. greedy. Best per dataset
                                   SciERC                 Few-NERD              in bold.
      Method              ρ          Sel. F1    Gap%        ρ       Gap%
      LP                  .283         .650     +4.8      .606       12.3       Dataset      Wt.     Greedy    Constr.      ∆         p
      Hidden Linear    .179±.019    .613±.002   −23.4          —
      Hidden MLP      .388±.013     .637±.003   −5.1    .629±.007    11.7       SciERC       LP        .644     .661     +1.67 pp    .004
                                                                                             Unif.     .644      .659    +1.54 pp    .023
                                                                                Few-NERD     LP        .748     .757     +0.88 pp   <.001
518   Cross-dataset asymmetry. On SciERC, the                                                Unif.     .748      .751    +0.32 pp    .003
519   MLP probe achieves higher quality correlation
                                                                                CoNLL        Unif.     .908     .904     −0.39 pp    n.s.
520   than LP (ρ=0.388 vs. 0.283, +37%); hidden
521   states encode information beyond what LP cap-
522   tures. Yet higher correlation does not yield bet-                         correct entities across samples recovers mentions 
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1791 · 2026-05-19T03:27:53.474462+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdftotext -layout -f 9 -l 12 main.pdf - 2>/dev/null | head -100",
  "description": "Extract text from pages 9-12 to find where Limitations/Ethics start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdftotext -layout -f 9 -l 12 main.pdf - 2>/dev/null | head -100",
    "description": "Extract text from pages 9-12 to find where Limitations/Ethics start"
  }
}
```

</details>

---


### Tool result

_source line 1792 · 2026-05-19T03:27:53.625712+00:00_

595   Selective prediction. Orthogonal to construction,            LP compression mechanisms. Four non-                     643
596   QE signals support selective prediction: retaining           mutually-exclusive      mechanisms      contribute       644
597   the top-k% highest-confidence instances. At 80%              (Appendix P); entity-token LP shows 4× higher            645
598   coverage, selective prediction yields +5–8 pp F1             variance yet performs worse; compression operates        646
599   gain (AUPRC 0.70–0.92), with VC as the strongest             at the representation level, not token aggregation       647
600   signal on Qwen (note: VC selection is model-                 (Appendix Z.3).                                          648
601   dependent; LLaMA FewNERD VC degrades se-
602   lection by −2.39 pp, Table 12). For practition-              Regime boundaries. QE signals collapse at                649

603   ers, when selection fails, QE scores can route low-          the low-resource boundary (WNUT-17, condi-               650

604   confidence instances to human review rather than             tional ρ=0.038; Table 11) and LP degrades selec-         651

605   sample N candidates to identify the best output.             tion at the ceiling (CoNLL, degeneracy 48–87%,           652
                                                                   −0.85 pp). Temperature manipulation disentangles         653
                                                                   the two factors: at T =1.2, degeneracy drops to          654
606   5   Discussion                                               14.9% yet LP does not improve because alignment          655
                                                                   remains weak (ρ=0.225 vs. Few-NERD ∼0.5–0.7;             656
607   Implications. All signals achieve positive qual-             Table 35); the SciERC epoch curve corroborates           657
608   ity estimation across no
…[truncated 9514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1793 · 2026-05-19T03:27:59.308515+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdftotext -layout -f 10 -l 13 main.pdf - 2>/dev/null | head -120",
  "description": "Extract text from pages 10-13 to find where references/appendix start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdftotext -layout -f 10 -l 13 main.pdf - 2>/dev/null | head -120",
    "description": "Extract text from pages 10-13 to find where references/appendix start"
  }
}
```

</details>

---


### Tool result

_source line 1794 · 2026-05-19T03:27:59.410611+00:00_

693   passes both failure mechanisms: it aggregates               tion when deployment requires reliability guaran-       743
694   across samples rather than ranking them, recov-             tees; apply entity construction when multi-sample       744
695   ering +1.67 pp (SciERC) and +0.88 pp (Few-                  generation is feasible; assess LP-alignment via         745
696   NERD) via LP-weighted entity aggregation (Ta-               held-out validation to choose between construction      746
697   ble 6). Construction and LP selection are com-              and LP selection. As models improve, degeneracy         747
698   plementary, governed by LP-quality alignment                rises and the selection window narrows; content-        748
699   (§4.7), and a simple alignment-based gating pro-            aware verifiers (Cobbe et al., 2021) may be needed      749
700   tocol selects the better method per dataset. For            to close the remaining gap.                             750
701   practitioners, QE-based selective prediction pro-
702   vides an orthogonal, immediate payoff: routing              Limitations                                             751
703   low-confidence instances to human review yields
704   +5–8 pp at 80% coverage without requiring multi-            Our evaluation covers four NER datasets; an ex-         752
705   sample generation at inference time.                        ploratory RE extension on SciERC is reported in         753
                                                                  Appendix L but generalization to other RE bench-        754
706   When would consistency-based selection work?                marks remains unvalidated. We cover 4B–8B scale;        755
707   Our negative results are specific to fine-tuned mod-        whether the gap holds for 70B+ models or closed-        756
708   els with constrained decoding on structured IE.             source APIs is untested. Larger models may pro-         757

…[truncated 10849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1795 · 2026-05-19T03:31:08.330492+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见 — Round 1\n\n## 审查侧重：新颖性 + 叙事完整性 + 写作质量\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5（Findings: Could be accepted to the Findings of the ACL）\n**一句话总结**: 实验设计扎实、诊断有深度的实证分析论文，但正文严重超页（约 10 页 vs 8 页限制），核心概念 \"correlation-selection gap\" 的理论深度不足以支撑 Main Conference 水平，且标题暗示纯 negative result 与实际 positive construction result 之间存在叙事张力。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论扎实：多数据集、多模型、多 seed、bootstrap CI、TOST equivalence testing、power analysis (MDE)。但 gating protocol 的验证存在循环性（probe instances drawn from test set, §4.7），SciERC 主实验仅用 1 seed（σ=0.48 pp，限制统计推断力）。 |\n| Excitement | 2.5/5 | 诊断性论文（\"when and why X fails\"）定位 Findings 更合适。correlation-selection gap 的概念有启发性但缺乏足够的理论支撑。entity-level construction 的增量偏小（+0.88 to +1.67 pp）。 |\n| Reproducibility | 4/5 | 详尽的超参数报告（Appendix H）、训练配置、seed 协议、evaluation protocol。承诺 code release。唯一缺失：未报告总 GPU hours。 |\n| Overall Assessment | 3.0/5 | 适合 Findings；Main Conference 需要更锐利的贡献定位和更强的正面结果。 |\n| Confidence | 4/5 | 仔细阅读了全文，熟悉 self-consistency、MBR decoding 和 NER 相关工作。 |\n\n---\n\n## Summary\n\n本文系统评估了五种置信信号在 LLM NER 任务上的质量估计（QE）和样本选择（selection）能力，发现所有信号在 QE 上表现可靠（ρ 高达 0.45, AUROC 高达 0.82），但在 best-of-N selection 上普遍失败。论文诊断出两个失败机制——instance degeneracy 和 LP compression——并提出 entity-level construction 作为替代方案。实验在 4 个 NER benchmark、2 个模型家族上进行，统计分析全面。\n\n---\n\n## Strengths\n\n**S1. 实验设计和统计严谨性出色。** 论文在 4 个难度梯度的 NER 数据集上、2 个模型家族 + 4B ablation 上系统测试 5 种信号。统计分析包括 multi-seed stability（Table S1）、bootstrap CI（Table 7）、TOST equivalence testing（Table 9）、power analysis（MDE ≈ 1.5 pp at 80% power）、和 Bonferroni correction。这种严谨程度在 NLP 实证论文中少见。\n\n**S2. QE-selection 分离的 framing 有价值。** 明确区分 quality estimation 和 sample selection 两个任务（§3.1），并实证证明 QE 强不等于 selection 强，这对实际部署有直接指导意义。Instance-level signal 不能 rank per-sample candidates 的 \"by construction\" 论证清晰。\n\n**S3. 诊断分析有深度。** Instance degeneracy、LP compression、capability-diversity tension 的诊断链条逻辑自洽。温度消融（Table 35）提供了更干净的因果测试（改变 diversity 不改变 capacity）。Hidden state probe（§4.6）确认了信息瓶颈不在 feature engineering 层面。\n\n**S4. Entity-level construction 提供了可操作的正面结果。** LP-weighted entity aggregation 在 SciERC (+1.67 pp, p=0.004) 和 Few-NERD (+0.88 pp, p<0.001) 上显著优于 greedy，提供了 selective prediction 之外的实用方案。\n\n**S5. 写作质量在 AI 风格检查上表现优秀。** 全文无 em-dash (—) 或解释性 en-dash (–)；无 AI 写作黑名单词汇（leverage, utilize, delve, furthermore 连续使用等）；无过度分段；\\textendash 仅用于数值范围（4B–8B, 13–87%），用法正确。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **正文严重超页：约 10 页 vs 8 页限制**\n- 具体位置：main.pdf 页面统计\n- 问题：通过 pdftotext 验证，Section 6 Conclusion 结束于 PDF 第 10 页右栏（约 line 750），Limitations 紧随其后在同页开始。ACL ARR 规定正文（abstract 到 conclusion）≤ 8 页，当前超出约 2 页。\n- 为什么影响接收：这是 desk reject 级别的格式违规。ARR 政策明确：超页论文可直接被拒。\n- 建议修改方向：(a) Discussion 从独立 Section 降级为 Experiments 的 subsection 并大幅压缩；(b) Hidden state probe (§4.6) 和 Robustness (§4.5) 的细节移入 appendix，主文仅保留结论性陈述；(c) Figure 1 和 Figure 2 考虑合并或缩小。\n\n**N2** [critical] **核心概念 \"correlation-selection gap\" 缺乏足够的理论深度**\n- 具体位置：§4.3, §5 (\"Why the gap exists\")\n- 问题：correlation-selection gap 本质上是一个实证观察而非理论贡献。论文未提供形式化分析来解释为什么 QE 相关性高不等于 selection 有效——例如，未给出在什么条件下 Spearman ρ 可以预测 best-of-N gain 的理论界限。Discussion 中 \"diminishing marginal returns on selection\" 的解释是直觉性的，缺乏理论支撑。\n- 为什么影响接收：对于诊断性论文，如果核心发现停留在实证描述层面而没有提供更深的理论洞察，EMNLP Main Conference 的 excitement bar 难以达到。\n- 建议修改方向：(a) 提供一个简化的形式化分析：在 degeneracy 率 d 和 alignment ρ 已知的情况下，推导 best-of-N expected gain 的 bound，展示 gap 何时不可避免；(b) 或者更清楚地将 gap 与 MBR/BoN 的已有理论联系，例如 Gao et al. (2023) 的 BoN scaling law 框架。\n\n**N3** [critical] **标题与内容的 framing 不一致**\n- 具体位置：Title vs §4.7 (Prescriptive Results), §6 (Conclusion)\n- 问题：标题 \"Why Confidence Signals **Fail** to Improve LLM-Based NER\" 暗示纯 negative result，但 §4.7 的 entity-level construction 实际给出了显著的 positive result（+1.67 pp on SciERC, p=0.004）。Conclusion 也以 construction 和 gating protocol 作为积极贡献结尾。这种标题与正面结果之间的矛盾会让审稿人困惑论文的核心贡献定位。\n- 为什么影响接收：叙事主线不统一是审稿人常见的负面评价来源。如果标题是 negative，但论文一半内容在讲 positive result，说明 framing 需要调整。\n- 建议修改方向：标题应反映完整的故事弧。例如 \"From Selection to Construction: Why Best-of-N Fails but Entity Aggregation Succeeds for LLM-Based NER\" 或类似表述。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Abstract 中 LP 和 AUROC 缩写未展开**\n- 具体位置：abstract.tex, lines 5-6\n- 问题：LP（log-probability）在 abstract 第 5 行首次出现时未给出全称。AUROC 在第 4 行出现也未展开。按 ACL 规范和论文写作硬规则，Abstract 中首次出现的缩写必须给出完整定义。\n- 建议：将 \"LP achieves\" 改为 \"log-probability (LP) achieves\"；将 \"AUROC up to 0.82\" 改为 \"area under the ROC curve [AUROC] up to 0.82\"。\n\n**W2** [warning] **与 Yao et al. (2026) 的区分可以更锐利**\n- 具体位置：§1 (line 8), §2 (\"Consistency for structured IE\" paragraph)\n- 问题：Introduction 第 8 行说 \"Unlike Yao et al., who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of when and why LP-based selection succeeds or fails\"。但 Yao et al. (2026) 研究的是 hard-prompted LLMs for plant-health data（domain-specific），而本文用的是 fine-tuned models on general benchmarks。这两个设置的差异本身就是区分点，但论文未充分利用。\n- 建议：在 Related Work 中更明确地列出与 Yao et al. 的 3-4 个关键差异（fine-tuned vs. prompted, general NER vs. domain-specific, QE vs. selection 的分离, degeneracy 诊断）。\n\n**W3** [warning] **LP-alignment gating protocol 的验证存在方法论问题**\n- 具体位置：§4.7 (\"LP-alignment gating\" paragraph)\n- 问题：论文承认 \"probe instances are drawn from the test set for simplicity\"（line 266），且仅在 3 个数据集上验证。这意味着 gating 效果可能因 test-set information leakage 而被高估。论文声称 \"correctly routes all three evaluated datasets\"，但 3 个数据集的成功率不构成有效验证。\n- 建议：(a) 在 SciERC 上用真正的 validation split 重做 gating 实验；(b) 弱化 claim，明确标注为 preliminary proof-of-concept。\n\n**W4** [warning] **SciERC 主实验仅用 1 个 training seed，seed sensitivity 高**\n- 具体位置：§4.3 (Table 2 caption), Limitations (line 14)\n- 问题：SciERC 是 primary test bed，但 selection 实验仅用 1 primary seed，且 multi-seed σ=0.48 pp（相对于 LP gain +0.61 pp 来说很大）。Table 2 用 2-seed mean，但 Limitations 承认 3-seed mean 仅 +0.04±0.48 pp。这意味着 SciERC 上的 LP selection 结论高度依赖种子选择。\n- 建议：在 main text 中更显著地讨论 seed sensitivity，而非仅在 Limitations 中提到。\n\n**W5** [warning] **Entity-level construction 的新颖性有限**\n- 具体位置：§4.7 (Entity-level construction paragraph)\n- 问题：Entity-level aggregation（按频率或加权频率筛选实体）本质上是 entity-level majority voting。Li et al. (2025) 已提出 generative self-aggregation for IE（Related Work §2 line 8 提到）。虽然本文的 LP-weighted 变体有新颖性，但核心思想（聚合 entity 而非选择 complete output）并不新颖。\n- 建议：更清楚地区分 LP-weighted construction 与 simple majority voting 和 Li et al. (2025) 的 self-aggregation 的差异，量化 LP weighting 的增量贡献。\n\n**W6** [warning] **Contribution 3 的 \"correct self-consistency analogy\" 措辞过于绝对**\n- 具体位置：Introduction, Contribution 3 (line 40)\n- 问题：称 entity-level construction 为 \"the correct self-consistency analogy for structured outputs\" 暗示这是唯一正确的方法。但论文仅在 NER 上验证，且 construction 在 CoNLL 上不 work（-0.39 pp, n.s.）。RE extension 在 appendix 中也是 preliminary。\"Correct\" 的断言过于强烈。\n- 建议：改为 \"a more effective\" 或 \"a natural\" self-consistency analogy，并注明适用条件。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** SciERC greedy F1 在不同表中出现 4 个不同值（0.640, 0.644, 0.645, 0.650; §3.3 line 61），虽然论文解释了 protocol variants 的原因，但这种不一致性增加了读者的认知负担。能否统一为一个 canonical configuration，其他值在 footnote 中说明？\n\n**Q2.** Few-NERD 使用 3 epochs 而 SciERC/CoNLL 使用 5 epochs（§4.1 line 15），论文承认这是一个 confound。Appendix 中的 epoch ablation（5-epoch Few-NERD control）显示 LP gains 减半。那么 Few-NERD 上 LP selection 的成功是否本质上是 under-training 的结果，而非 dataset 特性？\n\n**Q3.** 论文发现 degeneracy 与 LP gain 跨数据集无相关性（ρ=0.052, p=0.81; Figure 3），但宣称 LP-quality alignment 是 primary predictor。那么 within-instance ρ(LP, F1) 跨数据集与 LP gain 的相关性是多少？论文是否有这个数据点？\n\n**Q4.** Entity-level construction 的阈值 θ 在 SciERC 上用 θ=2/N（post-hoc），在 Few-NERD/CoNLL 上用 5-fold CV。为什么 SciERC 不也用 CV？这个不一致性是否影响了 SciERC 上 construction gain 的可靠性？\n\n---\n\n## Missing References\n\n1. **Wan et al. (2024)** — \"Knowledge Extraction in Low-Resource Scenarios: Survey and Opportunities\" (ACL 2024 Findings) — NER/IE 中的 LLM 方法综述，论文未 cite。\n2. **Xie et al. (2023)** — \"Self-Evaluation Guided Beam Search for Reasoning\" (NeurIPS 2023) — 另一种 per-sample scoring method（self-evaluation），论文仅在 Limitations 中提到 Self-Certainty 和 P(True) 但未包括 self-evaluation beam search。\n3. **Sun et al. (2023)** — \"Text Classification via Large Language Models\" — 讨论了 LLM 的 calibration 和 confidence-based selection，与本文 QE framework 相关。\n4. Related Work 中虽然覆盖了 MBR decoding 和 self-consistency 的主要工作，但缺少对 **ensemble-based IE methods**（如 multi-model voting for NER）的讨论，这与 entity-level construction 有直接关联。\n\n---\n\n## Minor Issues\n\n1. **Conclusion line 5**: \"a alignment-based gating protocol\" → \"an alignment-based gating protocol\"（冠词错误）。\n2. **Abstract line 7**: 最后一句话过长（约 50 words），包含太多技术细节（construction, LP selection, complementary, alignment-based gating）。建议拆分。\n3. **Figure 2 caption**: \"Bars show best-of-N selection F1; the line marks quality estimation ρ\" — 应指明具体是哪条线（是所有信号还是某一个信号的 ρ？）。\n4. **Table 3 caption**: \"Minor greedy F1 variations across tables reflect protocol differences (§3.3)\" 这个说明放在 caption 中显得突兀，建议移到正文或 footnote。\n5. **引用格式**: `\\citep` 和 `\\cite` 混用（e.g., Introduction line 3 uses `\\citep{wang2023selfconsistency}` but `\\cite{snell2025scaling}`）。应统一。\n\n---\n\n## 主要优势总结\n\n- 实验设计严谨，统计分析远超平均水平\n- QE-selection 分离的 framing 对社区有实际指导价值\n- 写作质量在去 AI 风格方面做得很好\n- Entity-level construction 提供了可操作的正面结果\n\n## 核心判断\n\n这是一篇实证扎实的诊断性论文，核心价值在于实验中揭示的 QE-selection 脱钩现象和 entity-level construction 方案。但三个 critical 问题限制了其竞争力：(1) 正文严重超页需要大幅压缩；(2) correlation-selection gap 停留在实证描述层面，缺乏理论支撑；(3) 标题与正面结果的叙事张力。建议投稿至 Findings，或在解决上述问题后重投 Main Conference。\n",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见 — Round 1\n\n## 审查侧重：新颖性 + 叙事完整性 + 写作质量\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5（Findings: Could be accepted to the Findings of the ACL）\n**一句话总结**: 实验设计扎实、诊断有深度的实证分析论文，但正文严重超页（约 10 页 vs 8 页限制），核心概念 \"correlation-selection gap\" 的理论深度不足以支撑 Main Conference 水平，且标题暗示纯 negative result 与实际 positive construction result 之间存在叙事张力。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论扎实：多数据集、多模型、多 seed、bootstrap CI、TOST equivalence testing、power analysis (MDE)。但 gating protocol 的验证存在循环性（probe instances drawn from test set, §4.7），SciERC 主实验仅用 1 seed（σ=0.48 pp，限制统计推断力）。 |\n| Excitement | 2.5/5 | 诊断性论文（\"when and why X fails\"）定位 Findings 更合适。correlation-selection gap 的概念有启发性但缺乏足够的理论支撑。entity-level construction 的增量偏小（+0.88 to +1.67 pp）。 |\n| Reproducibility | 4/5 | 详尽的超参数报告（Appendix H）、训练配置、seed 协议、evaluation protocol。承诺 code release。唯一缺失：未报告总 GPU hours。 |\n| Overall Assessment | 3.0/5 | 适合 Findings；Main Conference 需要更锐利的贡献定位和更强的正面结果。 |\n| Confidence | 4/5 | 仔细阅读了全文，熟悉 self-consistency、MBR decoding 和 NER 相关工作。 |\n\n---\n\n## Summary\n\n本文系统评估了五种置信信号在 LLM NER 任务上的质量估计（QE）和样本选择（selection）能力，发现所有信号在 QE 上表现可靠（ρ 高达 0.45, AUROC 高达 0.82），但在 best-of-N selection 上普遍失败。论文诊断出两个失败机制——instance degeneracy 和 LP compression——并提出 entity-level construction 作为替代方案。实验在 4 个 NER benchmark、2 个模型家族上进行，统计分析全面。\n\n---\n\n## Strengths\n\n**S1. 实验设计和统计严谨性出色。** 论文在 4 个难度梯度的 NER 数据集上、2 个模型家族 + 4B ablation 上系统测试 5 种信号。统计分析包括 multi-seed stability（Table S1）、bootstrap CI（Table 7）、TOST equivalence testing（Table 9）、power analysis（MDE ≈ 1.5 pp at 80% power）、和 Bonferroni correction。这种严谨程度在 NLP 实证论文中少见。\n\n**S2. QE-selection 分离的 framing 有价值。** 明确区分 quality estimation 和 sample selection 两个任务（§3.1），并实证证明 QE 强不等于 selection 强，这对实际部署有直接指导意义。Instance-level signal 不能 rank per-sample candidates 的 \"by construction\" 论证清晰。\n\n**S3. 诊断分析有深度。** Instance degeneracy、LP compression、capability-diversity tension 的诊断链条逻辑自洽。温度消融（Table 35）提供了更干净的因果测试（改变 diversity 不改变 capacity）。Hidden state probe（§4.6）确认了信息瓶颈不在 feature engineering 层面。\n\n**S4. Entity-level construction 提供了可操作的正面结果。** LP-weighted entity aggregation 在 SciERC (+1.67 pp, p=0.004) 和 Few-NERD (+0.88 pp, p<0.001) 上显著优于 greedy，提供了 selective prediction 之外的实用方案。\n\n**S5. 写作质量在 AI 风格检查上表现优秀。** 全文无 em-dash (—) 或解释性 en-dash (–)；无 AI 写作黑名单词汇（leverage, utilize, delve, furthermore 连续使用等）；无过度分段；\\textendash 仅用于数值范围（4B–8B, 13–87%），用法正确。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **正文严重超页：约 10 页 vs 8 页限制**\n- 具体位置：main.pdf 页面统计\n- 问题：通过 pdftotext 验证，Section 6 Conclusion 结束于 PDF 第 10 页右栏（约 line 750），Limitations 紧随其后在同页开始。ACL ARR 规定正文（abstract 到 conclusion）≤ 8 页，当前超出约 2 页。\n- 为什么影响接收：这是 desk reject 级别的格式违规。ARR 政策明确：超页论文可直接被拒。\n- 建议修改方向：(a) Discussion 从独立 Section 降级为 Experiments 的 subsection 并大幅压缩；(b) Hidden state probe (§4.6) 和 Robustness (§4.5) 的细节移入 appendix，主文仅保留结论性陈述；(c) Figure 1 和 Figure 2 考虑合并或缩小。\n\n**N2** [critical] **核心概念 \"correlation-selection gap\" 缺乏足够的理论深度**\n- 具体位置：§4.3, §5 (\"Why the gap exists\")\n- 问题：correlation-selection gap 本质上是一个实证观察而非理论贡献。论文未提供形式化分析来解释为什么 QE 相关性高不等于 selection 有效——例如，未给出在什么条件下 Spearman ρ 可以预测 best-of-N gain 的理论界限。Discussion 中 \"diminishing marginal returns on selection\" 的解释是直觉性的，缺乏理论支撑。\n- 为什么影响接收：对于诊断性论文，如果核心发现停留在实证描述层面而没有提供更深的理论洞察，EMNLP Main Conference 的 excitement bar 难以达到。\n- 建议修改方向：(a) 提供一个简化的形式化分析：在 degeneracy 率 d 和 alignment ρ 已知的情况下，推导 best-of-N expected gain 的 bound，展示 gap 何时不可避免；(b) 或者更清楚地将 gap 与 MBR/BoN 的已有理论联系，例如 Gao et al. (2023) 的 BoN scaling law 框架。\n\n**N3** [critical] **标题与内容的 framing 不一致**\n- 具体位置：Title vs §4.7 (Prescriptive Results), §6 (Conclusion)\n- 问题：标题 \"Why Confidence Signals **Fail** to Improve LLM-Based NER\" 暗示纯 negative result，但 §4.7 的 entity-level construction 实际给出了显著的 positive result（+1.67 pp on SciERC, p=0.004）。Conclusion 也以 construction 和 gating protocol 作为积极贡献结尾。这种标题与正面结果之间的矛盾会让审稿人困惑论文的核心贡献定位。\n- 为什么影响接收：叙事主线不统一是审稿人常见的负面评价来源。如果标题是 negative，但论文一半内容在讲 positive result，说明 framing 需要调整。\n- 建议修改方向：标题应反映完整的故事弧。例如 \"From Selection to Construction: Why Best-of-N Fails but Entity Aggregation Succeeds for LLM-Based NER\" 或类似表述。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Abstract 中 LP 和 AUROC 缩写未展开**\n- 具体位置：abstract.tex, lines 5-6\n- 问题：LP（log-probability）在 abstract 第 5 行首次出现时未给出全称。AUROC 在第 4 行出现也未展开。按 ACL 规范和论文写作硬规则，Abstract 中首次出现的缩写必须给出完整定义。\n- 建议：将 \"LP achieves\" 改为 \"log-probability (LP) achieves\"；将 \"AUROC up to 0.82\" 改为 \"area under the ROC curve [AUROC] up to 0.82\"。\n\n**W2** [warning] **与 Yao et al. (2026) 的区分可以更锐利**\n- 具体位置：§1 (line 8), §2 (\"Consistency for structured IE\" paragraph)\n- 问题：Introduction 第 8 行说 \"Unlike Yao et al., who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of when and why LP-based selection succeeds or fails\"。但 Yao et al. (2026) 研究的是 hard-prompted LLMs for plant-health data（domain-specific），而本文用的是 fine-tuned models on general benchmarks。这两个设置的差异本身就是区分点，但论文未充分利用。\n- 建议：在 Related Work 中更明确地列出与 Yao et al. 的 3-4 个关键差异（fine-tuned vs. prompted, general NER vs. domain-specific, QE vs. selection 的分离, degeneracy 诊断）。\n\n**W3** [warning] **LP-alignment gating protocol 的验证存在方法论问题**\n- 具体位置：§4.7 (\"LP-alignment gating\" paragraph)\n- 问题：论文承认 \"probe instances are drawn from the test set for simplicity\"（line 266），且仅在 3 个数据集上验证。这意味着 gating 效果可能因 test-set information leakage 而被高估。论文声称 \"correctly routes all three evaluated datasets\"，但 3 个数据集的成功率不构成有效验证。\n- 建议：(a) 在 SciERC 上用真正的 validation split 重做 gating 实验；(b) 弱化 claim，明确标注为 preliminary proof-of-concept。\n\n**W4** [warning] **SciERC 主实验仅用 1 个 training seed，seed sensitivity 高**\n- 具体位置：§4.3 (Table 2 caption), Limitations (line 14)\n- 问题：SciERC 是 primary test bed，但 selection 实验仅用 1 primary seed，且 multi-seed σ=0.48 pp（相对于 LP gain +0.61 pp 来说很大）。Table 2 用 2-seed mean，但 Limitations 承认 3-seed mean 仅 +0.04±0.48 pp。这意味着 SciERC 上的 LP selection 结论高度依赖种子选择。\n- 建议：在 main text 中更显著地讨论 seed sensitivity，而非仅在 Limitations 中提到。\n\n**W5** [warning] **Entity-level construction 的新颖性有限**\n- 具体位置：§4.7 (Entity-level construction paragraph)\n- 问题：Entity-level aggregation（按频率或加权频率筛选实体）本质上是 entity-level majority voting。Li et al. (2025) 已提出 generative self-aggregation for IE（Related Work §2 line 8 提到）。虽然本文的 LP-weighted 变体有新颖性，但核心思想（聚合 entity 而非选择 complete output）并不新颖。\n- 建议：更清楚地区分 LP-weighted construction 与 simple majority voting 和 Li et al. (2025) 的 self-aggregation 的差异，量化 LP weighting 的增量贡献。\n\n**W6** [warning] **Contribution 3 的 \"correct self-consistency analogy\" 措辞过于绝对**\n- 具体位置：Introduction, Contribution 3 (line 40)\n- 问题：称 entity-level construction 为 \"the correct self-consistency analogy for structured outputs\" 暗示这是唯一正确的方法。但论文仅在 NER 上验证，且 construction 在 CoNLL 上不 work（-0.39 pp, n.s.）。RE extension 在 appendix 中也是 preliminary。\"Correct\" 的断言过于强烈。\n- 建议：改为 \"a more effective\" 或 \"a natural\" self-consistency analogy，并注明适用条件。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** SciERC greedy F1 在不同表中出现 4 个不同值（0.640, 0.644, 0.645, 0.650; §3.3 line 61），虽然论文解释了 protocol variants 的原因，但这种不一致性增加了读者的认知负担。能否统一为一个 canonical configuration，其他值在 footnote 中说明？\n\n**Q2.** Few-NERD 使用 3 epochs 而 SciERC/CoNLL 使用 5 epochs（§4.1 line 15），论文承认这是一个 confound。Appendix 中的 epoch ablation（5-epoch Few-NERD control）显示 LP gains 减半。那么 Few-NERD 上 LP selection 的成功是否本质上是 under-training 的结果，而非 dataset 特性？\n\n**Q3.** 论文发现 degeneracy 与 LP gain 跨数据集无相关性（ρ=0.052, p=0.81; Figure 3），但宣称 LP-quality alignment 是 primary predictor。那么 within-instance ρ(LP, F1) 跨数据集与 LP gain 的相关性是多少？论文是否有这个数据点？\n\n**Q4.** Entity-level construction 的阈值 θ 在 SciERC 上用 θ=2/N（post-hoc），在 Few-NERD/CoNLL 上用 5-fold CV。为什么 SciERC 不也用 CV？这个不一致性是否影响了 SciERC 上 construction gain 的可靠性？\n\n---\n\n## Missing References\n\n1. **Wan et al. (2024)** — \"Knowledge Extraction in Low-Resource Scenarios: Survey and Opportunities\" (ACL 2024 Findings) — NER/IE 中的 LLM 方法综述，论文未 cite。\n2. **Xie et al. (2023)** — \"Self-Evaluation Guided Beam Search for Reasoning\" (NeurIPS 2023) — 另一种 per-sample scoring method（self-evaluation），论文仅在 Limitations 中提到 Self-Certainty 和 P(True) 但未包括 self-evaluation beam search。\n3. **Sun et al. (2023)** — \"Text Classification via Large Language Models\" — 讨论了 LLM 的 calibration 和 confidence-based selection，与本文 QE framework 相关。\n4. Related Work 中虽然覆盖了 MBR decoding 和 self-consistency 的主要工作，但缺少对 **ensemble-based IE methods**（如 multi-model voting for NER）的讨论，这与 entity-level construction 有直接关联。\n\n---\n\n## Minor Issues\n\n1. **Conclusion line 5**: \"a alignment-based gating protocol\" → \"an alignment-based gating protocol\"（冠词错误）。\n2. **Abstract line 7**: 最后一句话过长（约 50 words），包含太多技术细节（construction, LP selection, complementary, alignment-based gating）。建议拆分。\n3. **Figure 2 caption**: \"Bars show best-of-N selection F1; the line marks quality estimation ρ\" — 应指明具体是哪条线（是所有信号还是某一个信号的 ρ？）。\n4. **Table 3 caption**: \"Minor greedy F1 variations across tables reflect protocol differences (§3.3)\" 这个说明放在 caption 中显得突兀，建议移到正文或 footnote。\n5. **引用格式**: `\\citep` 和 `\\cite` 混用（e.g., Introduction line 3 uses `\\citep{wang2023selfconsistency}` but `\\cite{snell2025scaling}`）。应统一。\n\n---\n\n## 主要优势总结\n\n- 实验设计严谨，统计分析远超平均水平\n- QE-selection 分离的 framing 对社区有实际指导价值\n- 写作质量在去 AI 风格方面做得很好\n- Entity-level construction 提供了可操作的正面结果\n\n## 核心判断\n\n这是一篇实证扎实的诊断性论文，核心价值在于实验中揭示的 QE-selection 脱钩现象和 entity-level construction 方案。但三个 critical 问题限制了其竞争力：(1) 正文严重超页需要大幅压缩；(2) correlation-selection gap 停留在实证描述层面，缺乏理论支撑；(3) 标题与正面结果的叙事张力。建议投稿至 Findings，或在解决上述问题后重投 Main Conference。\n",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1796 · 2026-05-19T03:31:12.601291+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4270
}
```

</details>

---


### Assistant

_source line 1797 · 2026-05-19T03:31:22.961492+00:00_

审稿意见已提交给 Review Director。

主要发现摘要：

**Overall: 3.0/5（建议 Findings）**

三个 Critical 问题：
1. **正文超页约 2 页**（10 页 vs 8 页限制），desk reject 风险
2. **"Correlation-selection gap" 缺乏理论深度**，停留在实证描述层面
3. **标题暗示纯 negative result，但 §4.7 有显著 positive construction result**，叙事不统一

五个 Warning 问题：Abstract 缩写未展开（LP, AUROC）、与 Yao et al. 2026 区分不够锐利、gating protocol 用 test set 做 probe、SciERC 主实验仅 1 seed 且 sensitivity 高、entity-level construction 本质是 entity majority voting 新颖性有限。

写作质量方面通过了 AI 风格检查：无 em-dash、无黑名单词汇、无 -ing 短语结尾模式。引用验证通过（68 条全部有对应 cite，无 orphan/missing）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 46

## Round 46

14 recorded events


### User

_source line 1798 · 2026-05-19T03:43:32.396747+00:00_

[Round 1 审稿请求]:
## Round 1 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：
- **[AGREE]**：同意并说明理由
- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）

---

# Reviewer 1 审稿意见 — Round 1

## 审查侧重：方法严谨性 + 实验设计

**Overall**: 3/5（Findings）

## Summary

本文系统评估 5 种 confidence signal 能否通过 QE 或样本选择改善 LLM-based NER。核心发现为"correlation-selection gap"。论文将此归因于 instance degeneracy 和 LP alignment compression。研究极其彻底（4 数据集、2 模型族、3 seed、5-fold CV、22 页附录）。

## Must-Fix

**N1** [critical] **正文主体超出 8 页限制（约 9.5 页）**
Section 5 Discussion 单独占约 2 页。建议将 Discussion 中诊断细节移至附录，正文仅保留核心结论。

**N2** [critical] **实体匹配标准未精确定义——核心方法论缺陷**
EVC 和 Soft Jaccard 中"匹配"含义未定义：(a) 是否需精确文本+精确类型？(b) span 边界是否需完全一致？(c) 是否允许部分重叠？这是 5 个信号中 2 个的核心定义缺失。建议给出数学定义并消融不同匹配严格度。

**N3** [critical] **核心 claim 在高性能数据集上存在循环论证风险，且 entity-level 结果与标题矛盾**
两层问题：
- CoNLL degeneracy ≥65%，"信号无法改善选择"近乎同义反复——场景不需要信号，而非信号失败
- 标题 "Why Confidence Signals Fail" 做出普遍性否定，但 SciERC entity-level construction +1.57 pp 是正面结果
建议将 claim 精确限定为特定设置，标题突出 gap 而非 failure。

## Should-Fix

**W1** [warning] 最关键的鲁棒性证据（T=1.0 低 degeneracy 下 selection 仍失败）埋在附录中。
**W2** [warning] 仅测试 LoRA 微调，但标题做出不限定的 claim。建议限定为 "LoRA fine-tuned LLMs" 或增加 ICL baseline。
**W3** [warning] SciERC n=529 统计功效可能不足以支撑等价性声明，未报告 TOST post-hoc power。
**W4** [warning] Oracle 分析未回答：信号在哪些 instance 具体失败？缺少 instance-level error analysis。
**W5** [warning] "Soft Jaccard" 命名与标准 Jaccard index 混淆。

## Questions
Q1. EVC 和 SJ 中实体"匹配"的具体标准？
Q2. TOST 等价边界 δ 的具体值和选择依据？
Q3. Entity-level voting 在 SciERC +1.57 pp vs CoNLL -0.38 pp 的不对称如何调和？
Q4. Greedy (T=0) 与单个 T=0.6 样本的 F1 比较？
Q5. Supervised combination 的 5-fold CV 是否存在数据泄露？
Q6. LP 计算是否排除了 thinking tokens？

## Missing References
1. Kadavath et al. (2022) "Language Models Know What They Know" — LLM self-evaluation
2. 结构化预测 uncertainty estimation 工作
3. 9 条 bib entry 需复核年份/venue（hobelsberger2025, lightman2024 等）

## Minor Issues
1. "Confidence signal" 作为总称不够精确，建议用 "quality signal"
2. Figure 3 打印尺寸下标签可能难辨
3. "N-scaling" vs "sample size scaling" 术语不统一

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1799 · 2026-05-19T03:44:19.100870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
  "offset": "33",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
    "offset": "33",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1800 · 2026-05-19T03:44:19.101445+00:00_

33	
34	\paragraph{Soft Jaccard (structural, instance-level).}
35	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:
36	\begin{equation}\label{eq:sj}
37	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
38	\end{equation}
39	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.\footnote{The two normalizer variants produce nearly identical rankings ($|\Delta\rho|{\leq}0.009$; Table~\ref{tab:sj_normalizer}).}
40	The instance-level QE signal averages over all pairs: $c_{\text{sj}}(x) = \binom{N}{2}^{-1} \sum_{i&lt;j} \text{SJ}(y_i, y_j)$.
41	For selection, consensus-proximity converts this to per-sample utility $u_{\text{sj}}(y_i) = (N{-}1)^{-1} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, equivalent to MBR decoding \cite{eikema2022sampling}. The same construction applies to FK, EM, and VC.
42	
43	\paragraph{Entity voting confidence (structural, instance-level).}
44	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
45	The instance-level confidence is the mean frequency:
46	\begin{equation}\label{eq:voting}
47	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
48	\end{equation}
49	When $E_\cup = \emptyset$, $c_{\mathrm{vc}}(x) = 0$.\footnote{For voted-output \textit{selection}, we include only entities with frequency ${>}N/2$ (standard majority voting).}
50	
51	\subsection{Evaluation Framework}\label{sec:evaluation}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1801 · 2026-05-19T03:44:19.753772+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1802 · 2026-05-19T03:44:19.754380+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low instance degeneracy and adequate alignment are prese
…[truncated 4181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1803 · 2026-05-19T03:44:20.508308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "370",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "370",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1804 · 2026-05-19T03:44:20.659408+00:00_

370	\paragraph{TOST equivalence testing.}\label{app:tost}
371	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
372	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
373	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
374	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
375	We address this below with externally anchored equivalence margins.
376	The breakpoint $\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
377	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
378	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
379	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
380	
381	\begin{table}[t]
382	\centering
383	\small
384	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
…[truncated 3450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1805 · 2026-05-19T03:44:26.530551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "490",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "490",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 1806 · 2026-05-19T03:44:26.982839+00:00_

490	\texttt{System:} You are an expert in Named Entity Recognition.\\
491	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
492	Text: \texttt{\{input\_text\}}\\
493	Entity types: \texttt{\{schema\_types\}}
494	\end{quote}
495	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
496	
497	\paragraph{Constrained decoding.}
498	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
499	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
500	
501	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
502	
503	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
504	We quantify the potential impact on LP scores through three complementary arguments.
505	
506	\paragraph{LP shift magnitude.}
507	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
508	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
509	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
510	
511	\paragraph{Constant prefix cancellation.}
512	All $N$ samples within an instance share the same prompt and, under constrained decod
…[truncated 2092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1807 · 2026-05-19T03:44:27.234110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "180",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "180",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 1808 · 2026-05-19T03:44:27.284688+00:00_

180	Temperature manipulation (\S\ref{sec:discussion}) provides a cleaner test by altering diversity without changing capacity, and yields the same conclusion: both low degeneracy and adequate alignment appear independently associated with selection success.
181	
182	\paragraph{Supervised signal combination.}
183	Supervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).
184	Adding pairwise interaction features does not help (AUROC 0.634 vs.\ 0.638).
185	To test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.
186	DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).
187	Cross-dataset transfer fails entirely ($-27$\% to $-72$\% gap closure).
188	Neither handcrafted signal combinations (LR, MLP, RF on 5 scalar signals) nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.
189	
190	%% ============================================================
191	\subsection{Probing the Information Gap}
192	\label{sec:hidden_probe}
193	
194	The preceding negative results suggest the bottleneck is model-internal rather than a feature engineering problem.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1809 · 2026-05-19T03:46:34.839534+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 正文超页（约 9.5–10 页 vs 8 页限制）**\n同意。我在独立审稿中将此列为最高优先级问题（我的 N1）。PDF 第 10 页右栏仍包含 Section 6 Conclusion 正文。这是 desk reject 级别违规，需大幅压缩。\n\nR1 建议将 Discussion 细节移至附录、正文仅保留核心结论，我认为可行。补充建议：§4.5 Robustness 中 scale ablation / LoRA-rank ablation / supervised combination 的细节也适合移入附录，每项在正文仅保留一句结论。§4.6 Hidden state probe 的 setup 细节（mean-pooled hidden state, d=4096, MLP dim=256）同理。\n\n---\n\n**[REBUT] R1-N2: 实体匹配标准未精确定义**\nR1 称 EVC 和 SJ 的\"匹配\"含义未定义，但 §3.2 中实际上给出了完整定义：\n\n- **VC (§3.2 line 44)**: 明确使用 \"unique (text, type) tuples\"，即精确文本 + 精确类型。freq(e) = |{i : e ∈ yᵢ}| / N，其中 e 是 (text, type) tuple。匹配标准 = 完全一致。\n- **SJ (§3.2 line 35)**: 明确说明 \"group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU)\"。这回答了 R1 的三个子问题：(a) 按类型分组后匹配，不要求精确文本；(b) span 边界通过 token-level IoU 度量，不要求完全一致；(c) 允许部分重叠，IoU 连续度量重叠程度。\n- **FK (§3.2 line 26)**: \"items are unique (text, type) tuples\"，与 VC 相同的精确匹配。论文还在 line 32 明确说 \"Unlike structural signals, FK relies on exact string matching\"，暗示 SJ 不依赖精确匹配。\n- **EM (§3.2 line 20-22)**: 定义为 \"proportion of samples producing the most common output\"，即整个输出的精确匹配。\n\n定义确实分散在各 signal 的段落中，但并非缺失。不过，我同意论文可以在一处统一对比各 signal 的匹配标准（如一个小表格），提升可读性。R1 建议\"消融不同匹配严格度\"有参考价值，但考虑到正文已超页，这更适合作为 future work 而非 must-fix。\n\n---\n\n**[PARTIALLY AGREE] R1-N3: CoNLL 循环论证 + 标题矛盾**\n\n关于 **标题矛盾**：**同意**。我在独立审稿中将此列为 N3（critical），理由完全一致：标题暗示纯 negative result，但 §4.7 entity-level construction 给出了显著 positive result。叙事主线需要调整。\n\n关于 **CoNLL 循环论证**：**部分反驳**。R1 称 \"CoNLL degeneracy ≥65%，'信号无法改善选择'近乎同义反复\"。但论文明确将 CoNLL 定位为 \"ceiling-effect control where limited oracle headroom constrains selection gains\"（§4.1 line 11），而非作为 gap 的核心证据。核心诊断建立在 SciERC（17.8% degeneracy, 13 pp headroom）和 Few-NERD（13.8% degeneracy, 12.4 pp headroom）上，这两个数据集有充足的 non-degenerate headroom 可供信号利用，但信号仍然失败或仅提供微弱改善。CoNLL 在论文叙事中的角色是补全难度梯度的一端，而非核心 claim 的支柱。\n\n不过，R1 的批评有一个有效延伸：论文标题 \"Why Confidence Signals **Fail**\" 的普遍性措辞确实让 CoNLL 上的 \"failure\" 显得像循环论证。如果标题限定为 specific settings，这个问题会缓解。\n\n---\n\n## Should-Fix 问题\n\n**[REBUT] R1-W1: 关键鲁棒性证据（T=1.0 低 degeneracy 下 selection 仍失败）埋在附录**\nR1 称此证据仅在附录中，但实际上 Discussion §5 \"Regime boundaries\" 段落（main text）明确写道：\"at T=1.2, degeneracy drops to 14.9% yet LP does not improve because alignment remains weak (ρ=0.225 vs. Few-NERD ~0.5–0.7; Table 35)\"。核心结论在正文中，仅支持性数据表（Table 35）在附录。这是标准的 main-text-conclusion + appendix-evidence 结构。\n\n但我注意到 R1 说的是 \"T=1.0 低 degeneracy 下 selection 仍失败\"，而论文的温度消融是 T=1.2。如果 R1 指的是 Few-NERD（T=1.0, degeneracy 13.8%）上 structural signals 仍然 degrade selection，那这个结论确实在 §4.4 (Table 3) 主文中。\n\n---\n\n**[PARTIALLY AGREE] R1-W2: 仅测试 LoRA 微调，但标题做出不限定的 claim**\nR1 建议限定为 \"LoRA fine-tuned LLMs\" 或增加 ICL baseline。\n\n标题 \"LLM-Based Named Entity Recognition\" 确实涵盖面较广。不过，Discussion §5 最后一段 \"When would consistency-based selection work?\" 明确讨论了 ICL 设置可能恢复 selection headroom 的理由（更大 diversity、更低 degeneracy），且 Limitations 也承认 \"whether the gap holds for ... closed-source APIs is untested\"。\n\n我认为在标题中加入 \"fine-tuned\" 是合理的建议（\"... Fine-Tuned LLM-Based NER\"），但标记为 critical 过重。论文的核心贡献（QE-selection gap 的诊断框架和 entity-level construction）不依赖于 fine-tuning 特定假设。\n\n---\n\n**[AGREE] R1-W3: SciERC n=529 统计功效可能不足，未报告 TOST post-hoc power**\n同意。我在独立审稿中将 SciERC seed sensitivity 列为 W4。论文在 §4.3 footnote 中报告了 MDE ≈ 1.5 pp at 80% power，但 Appendix E（Table 9）的 TOST 分析未报告 post-hoc power。在 SciERC NER 上，δ=±2 pp 时 FK 和 EM 不通过 TOST，但 R1 正确指出我们不知道在这个 n 下 TOST 是否有足够 power 来拒绝等价假设。\n\n补充：Few-NERD（n=32,565）提供了远超 SciERC 的统计 power（MDE ≈ 0.22 pp），论文在 §4.3 中也明确指出 \"Few-NERD provides the definitive test\"。核心结论不依赖 SciERC 的等价性检验。\n\n---\n\n**[PARTIALLY AGREE] R1-W4: 缺少 instance-level error analysis**\n论文有一些 instance-level 分析（Appendix 中的 conditional decomposition、per-entity-type analysis、VC quartile analysis），但确实没有提供一个系统的 \"信号在哪些具体 instance 上失败及为什么\" 的分析。这对理解 gap 的来源有价值。\n\n不过，§4.6 Hidden state probe 的结果（MLP ρ=0.388 vs LP 0.283，但 selection gap closure -5.1%）从另一个角度回答了这个问题：即使拥有更丰富的 instance-level 信息，selection 仍然失败，说明瓶颈不在于识别哪些 instance 失败，而在于 inter-sample F1 差异太小（\"diminishing marginal returns\"）。\n\n---\n\n**[REBUT] R1-W5: \"Soft Jaccard\" 命名与标准 Jaccard 混淆**\n\"Soft Jaccard\" 的命名是恰当的：它保留了 Jaccard 的集合交集/并集结构（分子=匹配相似度之和，分母=最大集合大小），但将 exact match 替换为 token-level IoU（continuous similarity）。\"Soft\" 恰好传达了这个关键区别。这是计算语言学中常见的命名模式（如 \"soft attention\" vs \"hard attention\", \"soft alignment\" vs \"hard alignment\"）。论文在 §3.2 中给出了完整公式（Eq. 4），读者不会混淆。\n\n---\n\n## Questions\n\n**[REBUT] R1-Q1: EVC 和 SJ 中实体\"匹配\"的具体标准**\n见上方 N2 回应。VC 使用 exact (text, type) tuple match；SJ 使用 type-grouped Hungarian matching with token-level IoU。两个定义在 §3.2 中是完整的。\n\n**[REBUT] R1-Q2: TOST 等价边界 δ 的具体值和选择依据**\nAppendix E（Table 9）给出了三组 δ：±2, ±3, ±5 pp，并将每个 δ 对照 oracle headroom 做了比例解释（δ=5 pp ≈ 28–38% of headroom）。论文还承认了这个对照的循环性（Appendix E line 374），并补充了三个外部锚定 margin：(1) δ_SEM = bootstrapped SE of single-sample F1 (0.43–1.33 pp)；(2) δ_practical = 0.5 pp (Ratinov & Roth 2009 NER 可忽略差异阈值)；(3) δ_literature = 1.0 pp (Berg-Kirkpatrick et al. 2012 NLP 显著性阈值)。R1 的问题在论文中有详尽回答。\n\n**[REBUT] R1-Q3: Entity-level voting SciERC +1.67 pp vs CoNLL -0.39 pp 不对称**\n论文在 §4.7 line 256 明确说明：\"CoNLL shows no significant gain (−0.39 pp), consistent with ceiling-regime degeneracy.\" 机制是 recall-driven：construction 通过聚合低频 correct entities 提升 recall。在 CoNLL（greedy F1 ≈ 0.91）上，greedy 已捕获大部分 entities，额外聚合反而引入 false positives。§5 \"Capability-diversity tension\" 对此有系统性讨论。\n\n**[AGREE] R1-Q4: Greedy (T=0) 与单个 T=0.6 样本的 F1 比较**\n论文未提供这个比较，但它对理解 temperature 对 single-sample quality 的影响有参考价值。\n\n**[REBUT] R1-Q5: Supervised combination 的 5-fold CV 是否存在数据泄露**\n§4.5 line 183 描述 \"5-fold CV, 3-seed mean\"。5-fold CV 在 instance 层面切分，每个 fold 的 test instances 不出现在该 fold 的 train set 中。由于信号是 per-instance 计算的（不依赖其他 instances），fold 之间不存在 information leakage。DeBERTa verifier（line 185-186）也使用 5-fold CV。这是标准的 CV 设计。\n\n**[REBUT] R1-Q6: LP 计算是否排除了 thinking tokens**\nAppendix I（§ Thinking Token Impact Analysis）提供了三部分论证：(1) LP shift 仅 0.001 nats/token（占 median LP range 的 2.68%），影响 <1.5% instances 的 selection；(2) 所有 N 个 samples 共享相同的 thinking token offset，within-instance rankings 不变；(3) CoNLL control group（无 thinking tokens）显示更高而非更低的 tied fraction（86.8% vs SciERC 60.3%），直接否定 thinking token 假设。\n\n---\n\n## Missing References\n\n**[REBUT] R1-Missing-1: Kadavath et al. (2022) \"Language Models Know What They Know\"**\n该论文已被引用。References.bib 中有完整条目 `kadavath2022language`，在 Related Work §2 line 19（\"P(True) [Kadavath et al., 2022]\"）和 Limitations line 13 均有 cite。R1 可能遗漏了。\n\n**[PARTIALLY AGREE] R1-Missing-2: 结构化预测 uncertainty estimation 工作**\n论文在 Related Work §2 line 14 引用了 Culotta & McCallum (2004), Mejer & Crammer (2010), Fomicheva et al. (2020) 作为 \"confidence for structured prediction\" 的前序工作。覆盖面可能不够全面，但基础覆盖存在。\n\n**[AGREE] R1-Missing-3: 9 条 bib entry 需复核年份/venue**\n引用验证工具显示 4 条 not_found（hobelsberger2025, lightman2024, venktesh2025, aggarwal2023——均为真实论文，OpenAlex 覆盖不完整）和 5 条 mismatch（多为 first_author 格式差异或 year 偏移，如 chen2025twofailures bib year=2025 vs API year=2023）。建议作者核查这些条目的 venue 和 year 是否反映最终发表版而非 arXiv 版。\n\n---\n\n## Minor Issues\n\n**[REBUT] R1-Minor-1: \"Confidence signal\" 应改为 \"quality signal\"**\n\"Confidence signal\" 在论文语境中是准确的：5 个信号中 4 个基于 consistency/agreement（即 confidence 的操作化定义），1 个是 log-probability（模型 confidence 的直接度量）。\"Quality signal\" 的语义更广，可能让读者误以为包含 learned verifiers 或 reward models，而这正是论文认为缺失的。标题中 \"confidence signals\" 与 Related Work 中的 \"confidence estimation\" 文献保持术语一致。\n\n**[AGREE] R1-Minor-2: Figure 3 打印尺寸下标签可能难辨**\n需要检查渲染后的 PDF，但 scatter plot 在单栏宽度下确实容易出现标签重叠。\n\n**[AGREE] R1-Minor-3: \"N-scaling\" vs \"sample size scaling\" 术语不统一**\n同意。论文在 §4.5 用 \"sublinear N-scaling gains\"，在 Appendix 中用 \"Sample size scaling\" 和 \"Diminishing returns of N-scaling\"，应统一。\n",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 正文超页（约 9.5–10 页 vs 8 页限制）**\n同意。我在独立审稿中将此列为最高优先级问题（我的 N1）。PDF 第 10 页右栏仍包含 Section 6 Conclusion 正文。这是 desk reject 级别违规，需大幅压缩。\n\nR1 建议将 Discussion 细节移至附录、正文仅保留核心结论，我认为可行。补充建议：§4.5 Robustness 中 scale ablation / LoRA-rank ablation / supervised combination 的细节也适合移入附录，每项在正文仅保留一句结论。§4.6 Hidden state probe 的 setup 细节（mean-pooled hidden state, d=4096, MLP dim=256）同理。\n\n---\n\n**[REBUT] R1-N2: 实体匹配标准未精确定义**\nR1 称 EVC 和 SJ 的\"匹配\"含义未定义，但 §3.2 中实际上给出了完整定义：\n\n- **VC (§3.2 line 44)**: 明确使用 \"unique (text, type) tuples\"，即精确文本 + 精确类型。freq(e) = |{i : e ∈ yᵢ}| / N，其中 e 是 (text, type) tuple。匹配标准 = 完全一致。\n- **SJ (§3.2 line 35)**: 明确说明 \"group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU)\"。这回答了 R1 的三个子问题：(a) 按类型分组后匹配，不要求精确文本；(b) span 边界通过 token-level IoU 度量，不要求完全一致；(c) 允许部分重叠，IoU 连续度量重叠程度。\n- **FK (§3.2 line 26)**: \"items are unique (text, type) tuples\"，与 VC 相同的精确匹配。论文还在 line 32 明确说 \"Unlike structural signals, FK relies on exact string matching\"，暗示 SJ 不依赖精确匹配。\n- **EM (§3.2 line 20-22)**: 定义为 \"proportion of samples producing the most common output\"，即整个输出的精确匹配。\n\n定义确实分散在各 signal 的段落中，但并非缺失。不过，我同意论文可以在一处统一对比各 signal 的匹配标准（如一个小表格），提升可读性。R1 建议\"消融不同匹配严格度\"有参考价值，但考虑到正文已超页，这更适合作为 future work 而非 must-fix。\n\n---\n\n**[PARTIALLY AGREE] R1-N3: CoNLL 循环论证 + 标题矛盾**\n\n关于 **标题矛盾**：**同意**。我在独立审稿中将此列为 N3（critical），理由完全一致：标题暗示纯 negative result，但 §4.7 entity-level construction 给出了显著 positive result。叙事主线需要调整。\n\n关于 **CoNLL 循环论证**：**部分反驳**。R1 称 \"CoNLL degeneracy ≥65%，'信号无法改善选择'近乎同义反复\"。但论文明确将 CoNLL 定位为 \"ceiling-effect control where limited oracle headroom constrains selection gains\"（§4.1 line 11），而非作为 gap 的核心证据。核心诊断建立在 SciERC（17.8% degeneracy, 13 pp headroom）和 Few-NERD（13.8% degeneracy, 12.4 pp headroom）上，这两个数据集有充足的 non-degenerate headroom 可供信号利用，但信号仍然失败或仅提供微弱改善。CoNLL 在论文叙事中的角色是补全难度梯度的一端，而非核心 claim 的支柱。\n\n不过，R1 的批评有一个有效延伸：论文标题 \"Why Confidence Signals **Fail**\" 的普遍性措辞确实让 CoNLL 上的 \"failure\" 显得像循环论证。如果标题限定为 specific settings，这个问题会缓解。\n\n---\n\n## Should-Fix 问题\n\n**[REBUT] R1-W1: 关键鲁棒性证据（T=1.0 低 degeneracy 下 selection 仍失败）埋在附录**\nR1 称此证据仅在附录中，但实际上 Discussion §5 \"Regime boundaries\" 段落（main text）明确写道：\"at T=1.2, degeneracy drops to 14.9% yet LP does not improve because alignment remains weak (ρ=0.225 vs. Few-NERD ~0.5–0.7; Table 35)\"。核心结论在正文中，仅支持性数据表（Table 35）在附录。这是标准的 main-text-conclusion + appendix-evidence 结构。\n\n但我注意到 R1 说的是 \"T=1.0 低 degeneracy 下 selection 仍失败\"，而论文的温度消融是 T=1.2。如果 R1 指的是 Few-NERD（T=1.0, degeneracy 13.8%）上 structural signals 仍然 degrade selection，那这个结论确实在 §4.4 (Table 3) 主文中。\n\n---\n\n**[PARTIALLY AGREE] R1-W2: 仅测试 LoRA 微调，但标题做出不限定的 claim**\nR1 建议限定为 \"LoRA fine-tuned LLMs\" 或增加 ICL baseline。\n\n标题 \"LLM-Based Named Entity Recognition\" 确实涵盖面较广。不过，Discussion §5 最后一段 \"When would consistency-based selection work?\" 明确讨论了 ICL 设置可能恢复 selection headroom 的理由（更大 diversity、更低 degeneracy），且 Limitations 也承认 \"whether the gap holds for ... closed-source APIs is untested\"。\n\n我认为在标题中加入 \"fine-tuned\" 是合理的建议（\"... Fine-Tuned LLM-Based NER\"），但标记为 critical 过重。论文的核心贡献（QE-selection gap 的诊断框架和 entity-level construction）不依赖于 fine-tuning 特定假设。\n\n---\n\n**[AGREE] R1-W3: SciERC n=529 统计功效可能不足，未报告 TOST post-hoc power**\n同意。我在独立审稿中将 SciERC seed sensitivity 列为 W4。论文在 §4.3 footnote 中报告了 MDE ≈ 1.5 pp at 80% power，但 Appendix E（Table 9）的 TOST 分析未报告 post-hoc power。在 SciERC NER 上，δ=±2 pp 时 FK 和 EM 不通过 TOST，但 R1 正确指出我们不知道在这个 n 下 TOST 是否有足够 power 来拒绝等价假设。\n\n补充：Few-NERD（n=32,565）提供了远超 SciERC 的统计 power（MDE ≈ 0.22 pp），论文在 §4.3 中也明确指出 \"Few-NERD provides the definitive test\"。核心结论不依赖 SciERC 的等价性检验。\n\n---\n\n**[PARTIALLY AGREE] R1-W4: 缺少 instance-level error analysis**\n论文有一些 instance-level 分析（Appendix 中的 conditional decomposition、per-entity-type analysis、VC quartile analysis），但确实没有提供一个系统的 \"信号在哪些具体 instance 上失败及为什么\" 的分析。这对理解 gap 的来源有价值。\n\n不过，§4.6 Hidden state probe 的结果（MLP ρ=0.388 vs LP 0.283，但 selection gap closure -5.1%）从另一个角度回答了这个问题：即使拥有更丰富的 instance-level 信息，selection 仍然失败，说明瓶颈不在于识别哪些 instance 失败，而在于 inter-sample F1 差异太小（\"diminishing marginal returns\"）。\n\n---\n\n**[REBUT] R1-W5: \"Soft Jaccard\" 命名与标准 Jaccard 混淆**\n\"Soft Jaccard\" 的命名是恰当的：它保留了 Jaccard 的集合交集/并集结构（分子=匹配相似度之和，分母=最大集合大小），但将 exact match 替换为 token-level IoU（continuous similarity）。\"Soft\" 恰好传达了这个关键区别。这是计算语言学中常见的命名模式（如 \"soft attention\" vs \"hard attention\", \"soft alignment\" vs \"hard alignment\"）。论文在 §3.2 中给出了完整公式（Eq. 4），读者不会混淆。\n\n---\n\n## Questions\n\n**[REBUT] R1-Q1: EVC 和 SJ 中实体\"匹配\"的具体标准**\n见上方 N2 回应。VC 使用 exact (text, type) tuple match；SJ 使用 type-grouped Hungarian matching with token-level IoU。两个定义在 §3.2 中是完整的。\n\n**[REBUT] R1-Q2: TOST 等价边界 δ 的具体值和选择依据**\nAppendix E（Table 9）给出了三组 δ：±2, ±3, ±5 pp，并将每个 δ 对照 oracle headroom 做了比例解释（δ=5 pp ≈ 28–38% of headroom）。论文还承认了这个对照的循环性（Appendix E line 374），并补充了三个外部锚定 margin：(1) δ_SEM = bootstrapped SE of single-sample F1 (0.43–1.33 pp)；(2) δ_practical = 0.5 pp (Ratinov & Roth 2009 NER 可忽略差异阈值)；(3) δ_literature = 1.0 pp (Berg-Kirkpatrick et al. 2012 NLP 显著性阈值)。R1 的问题在论文中有详尽回答。\n\n**[REBUT] R1-Q3: Entity-level voting SciERC +1.67 pp vs CoNLL -0.39 pp 不对称**\n论文在 §4.7 line 256 明确说明：\"CoNLL shows no significant gain (−0.39 pp), consistent with ceiling-regime degeneracy.\" 机制是 recall-driven：construction 通过聚合低频 correct entities 提升 recall。在 CoNLL（greedy F1 ≈ 0.91）上，greedy 已捕获大部分 entities，额外聚合反而引入 false positives。§5 \"Capability-diversity tension\" 对此有系统性讨论。\n\n**[AGREE] R1-Q4: Greedy (T=0) 与单个 T=0.6 样本的 F1 比较**\n论文未提供这个比较，但它对理解 temperature 对 single-sample quality 的影响有参考价值。\n\n**[REBUT] R1-Q5: Supervised combination 的 5-fold CV 是否存在数据泄露**\n§4.5 line 183 描述 \"5-fold CV, 3-seed mean\"。5-fold CV 在 instance 层面切分，每个 fold 的 test instances 不出现在该 fold 的 train set 中。由于信号是 per-instance 计算的（不依赖其他 instances），fold 之间不存在 information leakage。DeBERTa verifier（line 185-186）也使用 5-fold CV。这是标准的 CV 设计。\n\n**[REBUT] R1-Q6: LP 计算是否排除了 thinking tokens**\nAppendix I（§ Thinking Token Impact Analysis）提供了三部分论证：(1) LP shift 仅 0.001 nats/token（占 median LP range 的 2.68%），影响 <1.5% instances 的 selection；(2) 所有 N 个 samples 共享相同的 thinking token offset，within-instance rankings 不变；(3) CoNLL control group（无 thinking tokens）显示更高而非更低的 tied fraction（86.8% vs SciERC 60.3%），直接否定 thinking token 假设。\n\n---\n\n## Missing References\n\n**[REBUT] R1-Missing-1: Kadavath et al. (2022) \"Language Models Know What They Know\"**\n该论文已被引用。References.bib 中有完整条目 `kadavath2022language`，在 Related Work §2 line 19（\"P(True) [Kadavath et al., 2022]\"）和 Limitations line 13 均有 cite。R1 可能遗漏了。\n\n**[PARTIALLY AGREE] R1-Missing-2: 结构化预测 uncertainty estimation 工作**\n论文在 Related Work §2 line 14 引用了 Culotta & McCallum (2004), Mejer & Crammer (2010), Fomicheva et al. (2020) 作为 \"confidence for structured prediction\" 的前序工作。覆盖面可能不够全面，但基础覆盖存在。\n\n**[AGREE] R1-Missing-3: 9 条 bib entry 需复核年份/venue**\n引用验证工具显示 4 条 not_found（hobelsberger2025, lightman2024, venktesh2025, aggarwal2023——均为真实论文，OpenAlex 覆盖不完整）和 5 条 mismatch（多为 first_author 格式差异或 year 偏移，如 chen2025twofailures bib year=2025 vs API year=2023）。建议作者核查这些条目的 venue 和 year 是否反映最终发表版而非 arXiv 版。\n\n---\n\n## Minor Issues\n\n**[REBUT] R1-Minor-1: \"Confidence signal\" 应改为 \"quality signal\"**\n\"Confidence signal\" 在论文语境中是准确的：5 个信号中 4 个基于 consistency/agreement（即 confidence 的操作化定义），1 个是 log-probability（模型 confidence 的直接度量）。\"Quality signal\" 的语义更广，可能让读者误以为包含 learned verifiers 或 reward models，而这正是论文认为缺失的。标题中 \"confidence signals\" 与 Related Work 中的 \"confidence estimation\" 文献保持术语一致。\n\n**[AGREE] R1-Minor-2: Figure 3 打印尺寸下标签可能难辨**\n需要检查渲染后的 PDF，但 scatter plot 在单栏宽度下确实容易出现标签重叠。\n\n**[AGREE] R1-Minor-3: \"N-scaling\" vs \"sample size scaling\" 术语不统一**\n同意。论文在 §4.5 用 \"sublinear N-scaling gains\"，在 Appendix 中用 \"Sample size scaling\" 和 \"Diminishing returns of N-scaling\"，应统一。\n",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1810 · 2026-05-19T03:46:39.927870+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5088
}
```

</details>

---


### Assistant

_source line 1811 · 2026-05-19T03:46:48.300645+00:00_

交叉回应已提交。总结：

- **AGREE（6 项）**：N1 超页、N3 标题矛盾部分、W3 TOST power、W4 instance-level error analysis 部分、Q4 T=0.6 对比缺失、Minor-2/3
- **REBUT（8 项）**：N2 实体匹配定义实际存在于 §3.2、W1 关键证据在 Discussion 正文中、W5 Soft Jaccard 命名合理、Q1/Q2/Q3/Q5/Q6 论文中有充分回答、Missing-1 Kadavath 已被引用、Minor-1 confidence signal 术语准确
- **PARTIALLY AGREE（3 项）**：N3 CoNLL 循环论证（CoNLL 定位为 control 而非核心证据）、W2 仅 LoRA（Discussion 已讨论 ICL）、Missing-2 结构化预测 uncertainty 覆盖

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 47

## Round 47

78 recorded events


### User

_source line 1812 · 2026-05-19T04:52:05.451621+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的侧重：新颖性 + 完整性 + 格式合规**

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各 section 在 `sections/` 子目录）
- **目标 venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，正文上限 8 页（不含 references 和 limitations），double-blind

### 你的审查重点

1. **新颖性评估**
   - 相对于 Wang et al. 2023 (self-consistency)、Taubenfeld et al. 2025 (CISC)、Kang et al. 2025 (self-certainty)、Yao et al. 2026 (consistency for IE) 等直接竞争者，本文增量贡献是否足够
   - "correlation-selection gap" 概念是否有足够理论深度，还是仅仅是实证观察的包装
   - Entity-level construction 相对于 ensemble NER / entity-level majority voting 的新颖性
   - 负面结果（selection fails）的诊断价值评估

2. **叙事统一性**
   - 标题 → Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条连贯主线
   - 标题是否准确反映论文完整故事（诊断 + 修复两部分）
   - Contributions 列表是否与实验结果对应
   - 正面结果（construction）和负面结果（selection fails）的平衡

3. **Related Work 质量**
   - 分类和组织是否清晰
   - 是否充分覆盖：self-consistency methods、structured IE confidence、MBR decoding、BoN with verifiers
   - 与本文的 positioning 是否清楚
   - 引用密度是否符合 EMNLP 水平

4. **格式合规**
   - 正文是否在 8 页内（检查 section 内容量估算）
   - ACL 匿名规则（检查 \author{Anonymous}）
   - Limitations 节位置和内容
   - Responsible NLP Research Checklist 是否认真填写
   - 缩写首次使用是否展开（特别是 Abstract 内的缩写）

5. **写作质量**
   - AI 写作痕迹检查（dash、-ing phrases、过度分段、用词黑名单）
   - 专有名词首次出现是否有定义
   - 图表 caption 是否自包含
   - 引用格式一致性（\cite vs \citep）

### 输出格式

请按以下结构输出审稿意见：
- **Summary**: 论文概述（2-3 句）
- **Strengths**: 优点（逐条）
- **Weaknesses**: 缺点（逐条，按 critical / warning / info 分级，每条给出具体证据和建议）
- **Questions**: 需要作者澄清的问题
- **Missing References**: 相关工作/引用方面的遗漏
- **Overall Assessment**: 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度 + 简要理由

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1813 · 2026-05-19T04:52:23.477532+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1814 · 2026-05-19T04:52:23.778869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1815 · 2026-05-19T04:52:28.293779+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1816 · 2026-05-19T04:52:28.695528+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1817 · 2026-05-19T04:52:28.695842+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 1818 · 2026-05-19T04:52:29.197663+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1819 · 2026-05-19T04:52:29.197988+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 1820 · 2026-05-19T04:52:37.377018+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about ACL ARR (ACL Rolling Review) reviewer guidelines and scoring for 2025-2026:

## Reviewer Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Criteria

The review guidelines emphasize that all papers recommended for Findings or main conference are expected to be sound and reproducible. ARR developed detailed guidelines and suggestions for each step of the process, including a list of common problems in
…[truncated 869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8179
}
```

</details>

---


### Tool call

_source line 1821 · 2026-05-19T04:52:43.983949+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1822 · 2026-05-19T04:52:43.984298+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1823 · 2026-05-19T04:52:44.889369+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales (e.g., soundness 1-5, excitement 1-5, overall assessment scale). List all dimensions with their exact score ranges and descriptions for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales (e.g., soundness 1-5, excitement 1-5, overall assessment scale). List all dimensions with their exact score ranges and descriptions for each score level."
  }
}
```

</details>

---


### Tool result

_source line 1824 · 2026-05-19T04:52:50.667377+00:00_

# ARR Review Form Criteria and Scoring

Based on the provided guidelines, the document describes three primary scoring dimensions for ARR reviews, though **specific numerical scales are not detailed in this content**.

## Scoring Dimensions Mentioned

The guidelines reference three scores reviewers must provide:

1. **Soundness** - Assesses technical validity and rigor. Scores "must be justified by the text of the review." Low soundness ratings require explicit substantiation in the written feedback.

2. **Excitement** - Reflects "personal taste" and subjective interest. This dimension is "orthogonal to the assessment of the soundness of the paper," allowing reviewers to distinguish technical quality from personal appeal.

3. **Overall Assessment** - A composite recommendation score that "reflects your assessment of soundness, excitement, and also other factors like novelty and impact."

## Key Guidance

The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," though excitement levels may vary.

## Limitation

**The actual numerical scales (e.g., 1-5 ranges, specific descriptor text for each level) are not provided in this document excerpt.** The guidelines reference a separate resource: "a post describing the ARR review form in detail," which presumably contains the complete scoring specifications.

To obtain precise scoring scales, you would need to consult the linked review form documentation or current OpenReview platform interface.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5778
}
```

</details>

---


### Tool call

_source line 1825 · 2026-05-19T04:52:53.176062+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement overall assessment score scale 1 2 3 4 5 description"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement overall assessment score scale 1 2 3 4 5 description"
  }
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-19T04:52:53.678789+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-19T04:52:53.729442+00:00_

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
21	\title{Strong Predictors, Weak Selectors:\\ Diagnosing and Fixing Self-Consistency for Named Entity Recognition}
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
46	\section*{Responsible NLP Research Checklist}
47	\input{sections/checklist}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1828 · 2026-05-19T04:53:00.902541+00:00_

Web search results for query: "ACL ARR review form soundness excitement overall assessment score scale 1 2 3 4 5 description"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL 2023 Peer Review Report - ACL 2023","url":"https://2023.aclweb.org/blog/review-report/"}]

Based on the search results, I found detailed information about the ACL ARR (Associaton for Computational Linguistics Rolling Review) review form and its scoring system.

## Three Review Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review. The soundness assessment is separate from excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Excitement Score

Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons. The search results show example descriptions including: "5 = Highly Exciting: I would recommend this paper to others and/or attend its pre
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7726
}
```

</details>

---


### Tool call

_source line 1829 · 2026-05-19T04:53:05.516746+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL scoring dimensions with their complete numerical scales and description for each level. I need the exact scale for soundness, excitement, overall assessment, and any other scored dimensions. List every score level (1, 2, 3, 4, 5) with its description text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL scoring dimensions with their complete numerical scales and description for each level. I need the exact scale for soundness, excitement, overall assessment, and any other scored dimensions. List every score level (1, 2, 3, 4, 5) with its description text."
  }
}
```

</details>

---


### Tool call

_source line 1830 · 2026-05-19T04:53:07.273529+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1831 · 2026-05-19T04:53:07.675115+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) where LP-quality alignment is strong, but gains are absent elsewhere despite ${\sim}$13~pp oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose two causes: instance degeneracy (13\textendash 87\%) and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations).
7	A more effective self-consistency analogy for structured outputs is entity-level \textit{construction}: aggregating entities across samples improves F1 by $+0.88$ to $+1.67$\,pp ($p{<}0.005$) on datasets where instance-level selection fails or is marginal. Construction and LP selection are complementary, governed by LP-quality alignment; an alignment-based gating protocol correctly routes all three evaluated datasets.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1832 · 2026-05-19T04:53:07.675515+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1833 · 2026-05-19T04:53:08.177452+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low inst
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-19T04:53:08.177870+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1835 · 2026-05-19T04:53:09.131287+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{xiao2025el4ner}; our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity.
14	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.
15
…[truncated 1948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1836 · 2026-05-19T04:53:09.282209+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-19T04:53:09.282663+00:00_

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
11	Throughout, entity matching uses exact span and type match (a predicted entity is correct iff its character offsets and type label both match a gold entity).
12	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
13	
14	\paragraph{Log-probability (model-internal, per-sample).}
15	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
16	\begin{equation}\label{eq:logprob}
17	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
18	\end{equation}
19	
20	\paragraph{Exact match voting (surface, instance-level).}
21	The proportion of samples producing the most common output:
22	\begin{equation}\label{eq:em}
23	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
24	\end{equation}
25	
26	\paragraph{Fleiss' $\kappa$ (surface, insta
…[truncated 3790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-19T04:53:09.282871+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-19T04:53:09.333502+00:00_

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
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\topr
…[truncated 16461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1840 · 2026-05-19T04:53:12.203743+00:00_

# ACL Rolling Review: Scoring Dimensions

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
- **5**: "Consider for Award: up to top 2.5% papers"
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: has to be fully redone"

## Reproducibility
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be h
…[truncated 230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6686
}
```

</details>

---


### Tool call

_source line 1841 · 2026-05-19T04:53:31.992043+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-19T04:53:31.992504+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool call

_source line 1843 · 2026-05-19T04:53:31.992917+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1844 · 2026-05-19T04:53:32.194389+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Two factors constrain selection: instance degeneracy (17.8--48.4\%) eliminates headroom, and LP compression (within-instance $\rho$ 0.262--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}).
6	Temperature disentangles the two factors: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5--0.7; Table~\ref{tab:t_degeneracy}); degeneracy rises with model scale and training convergence (Tables~\ref{tab:scale_ablation}, \ref{tab:epoch_confound}), so the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms ($+1.67$\,pp SciERC, $+0.88$\,pp Few-NERD; Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}).
11	Our negative results are specific to fine-tuned models with constrained decoding; settings with greater output diversity may restore selection headroom (Appendix~\ref{app:when_selection_works}).
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 1845 · 2026-05-19T04:53:32.194758+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
4	Instance-level selection fails due to degeneracy and LP compression, but a more effective self-consistency analogy for structured outputs is entity-level construction: LP-weighted entity aggregation yields $+1.67$\,pp on SciERC ($p{=}0.004$) and $+0.88$\,pp on Few-NERD ($p{<}0.001$).
5	Construction and LP selection are complementary, governed by LP-quality alignment; an alignment-based gating protocol routes the appropriate method per dataset.
6	For practitioners: use QE-based selective prediction when deployment requires reliability guarantees; apply entity construction when multi-sample generation is feasible; assess LP-alignment via held-out validation to choose between construction and LP selection.
7	As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 1846 · 2026-05-19T04:53:32.194987+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
3	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app
…[truncated 1951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1847 · 2026-05-19T04:53:32.446108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1848 · 2026-05-19T04:53:32.597105+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1849 · 2026-05-19T04:53:32.597464+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1850 · 2026-05-19T04:53:32.899687+00:00_

File content (40360 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1851 · 2026-05-19T04:53:38.520151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1852 · 2026-05-19T04:53:39.072693+00:00_

0	\section{Notation}\label{app:notation}
1	
2	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{cl}
8	\toprule
9	Symbol & Meaning \\
10	\midrule
11	$\mathcal{M}$ & Language model \\
12	$x$ & Input instance \\
13	$y_i$ & $i$-th stochastic sample \\
14	$N$ & Number of samples \\
15	$T$ & Sampling temperature \\
16	$c(\cdot)$ & Confidence signal \\
17	SJ & Soft Jaccard similarity \\
18	FK & Fleiss' $\kappa$ \\
19	EM & Exact-match voting rate \\
20	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
21	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
22	\bottomrule
23	\end{tabular}
24	\caption{Notation used throughout the paper.}
25	\label{tab:notation}
26	\end{table}
27	
28	\section{Robustness Analysis}\label{app:robustness}
29	
30	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
31	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
37	\label{tab:robustness}
38	\begin{tabular}{llcc}
39	\toprule
40	& & NER $\rho$ & RE $\rho$ \\
41	\midrule
42	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
43	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
44	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
45	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
46	\quad FK & $T
…[truncated 13587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1853 · 2026-05-19T04:53:39.223599+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1854 · 2026-05-19T04:53:39.224025+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1855 · 2026-05-19T04:53:53.688085+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1856 · 2026-05-19T04:53:53.688717+00:00_

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
…[truncated 20520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1857 · 2026-05-19T04:53:54.692019+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1858 · 2026-05-19T04:54:51.096704+00:00_

&lt;persisted-output>
Output too large (60.9KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/6637d7ef-76dd-44ee-b3c2-e639897c1b30/tool-results/toolu_011br5ijEWgi2CMdkPiiaAuZ.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 73, \"total_citations\": 110, \"unique_cited_keys\": 69, \"orphan_bib\": 4, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 64, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"eisenstein2023helping\", \"li2025llms\", \"naderi2021ensemble\", \"sarcinelli2025local\"], \"missing_bib\": [], \"orphan_count\": 4, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"aut
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 56404
}
```

</details>

---


### Tool call

_source line 1859 · 2026-05-19T04:54:58.975310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/6637d7ef-76dd-44ee-b3c2-e639897c1b30/tool-results/toolu_011br5ijEWgi2CMdkPiiaAuZ.txt",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/6637d7ef-76dd-44ee-b3c2-e639897c1b30/tool-results/toolu_011br5ijEWgi2CMdkPiiaAuZ.txt",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1860 · 2026-05-19T04:54:59.428520+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 73, \"total_citations\": 110, \"unique_cited_keys\": 69, \"orphan_bib\": 4, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 64, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"eisenstein2023helping\", \"li2025llms\", \"naderi2021ensemble\", \"sarcinelli2025local\"], \"missing_bib\": [], \"orphan_count\": 4, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksi
…[truncated 60335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1861 · 2026-05-19T04:54:59.829939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "450",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "450",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1862 · 2026-05-19T04:54:59.880813+00:00_

450	\label{tab:hidden_probe}
451	\resizebox{\columnwidth}{!}{%
452	\begin{tabular}{@{}l ccc cc@{}}
453	\toprule
454	& \multicolumn{3}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{Few-NERD}} \\
455	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
456	Method & $\rho$ & Sel.\ F1 & Gap\% & $\rho$ & Gap\% \\
457	\midrule
458	LP & .283 & $\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\
459	Hidden Linear & $.179{\pm}.019$ & $.613{\pm}.002$ & $-$23.4 & \multicolumn{2}{c}{---} \\
460	Hidden MLP & $\mathbf{.388{\pm}.013}$ & $.637{\pm}.003$ & $-$5.1 & $\mathbf{.629{\pm}.007}$ & 11.7 \\
461	\bottomrule
462	\end{tabular}}
463	\end{table}
464	
465	\paragraph{Cross-dataset asymmetry.}
466	On SciERC, the MLP probe achieves higher quality correlation than LP ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%); hidden states encode information beyond what LP captures.
467	Yet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\% vs.\ $+4.8$\%; Table~\ref{tab:hidden_probe}).
468	The linear probe performs worse still ($\rho{=}0.179$, gap closure $-23.4$\%).
469	On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\% vs.\ $12.3$\%).
470	A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%); LP's bottleneck is not token aggregation.
471	The correlation-selection gap extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\S\ref{sec:discussion}).
472	
473	\section{Multi-Seed Stability}\label{app:multiseed}
474	
475	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
476	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is ident
…[truncated 14708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1863 · 2026-05-19T04:55:04.595777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "700",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "700",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1864 · 2026-05-19T04:55:04.646531+00:00_

700	SciERC & Qwen3-8B & 0.262 & 435 / 529 & 82\% \\
701	Few-NERD & Qwen3-8B & 0.667 & 28{,}055 / 32{,}565 & 86\% \\
702	CoNLL & Qwen3-8B & 0.506 & 1{,}124 / 2{,}756 & 41\% \\
703	CoNLL & LLaMA-3.1-8B & 0.512 & 298 / 2{,}756 & 11\% \\
704	\bottomrule
705	\end{tabular}}
706	\end{table}
707	
708	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
709	
710	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
711	
712	\begin{table}[t]
713	\centering
714	\small
715	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
716	\label{tab:vc_quartile}
717	\begin{tabular}{lcccc}
718	\toprule
719	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
720	\midrule
721	\multicolumn{5}{l}{\textit{NER}} \\
722	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
723	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
724	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
725	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
726	\midrule
727	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
728	Q1 (low) & --- & $-$3.56 & --- & --- \\
729	Q4 (high) & --- & $+$4.01 & --- & --- \\
730	\bottomrule
731	\end{tabular}
732	\end{table}
733	
734	The NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
735	\begin{itemize}
736	\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp. Samples have already converged, leaving little room for any signal to improve selection.
737	\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, and LP rankings produce inconsistent $\Delta$ signs across quartiles.
738	\end{itemize}
…[truncated 14029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1865 · 2026-05-19T04:55:09.213630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "950",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "950",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1866 · 2026-05-19T04:55:09.264399+00:00_

950	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
951	\label{tab:stable_failures}
952	\begin{tabular}{lcccc}
953	\toprule
954	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
955	\midrule
956	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
957	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
958	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
959	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
960	\bottomrule
961	\end{tabular}
962	\end{table}
963	
964	\paragraph{Flip instances.}
965	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
966	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
967	
968	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
969	
970	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
971	
972	\begin{table}[t]
973	\centering
974	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
975	\label{tab:n-scaling}
976	\small
977	\begin{tabular}{l ccc ccc}
978	\toprule
979	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
980	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
981	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
982	\midrule
983	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
984	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
985	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf
…[truncated 18998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1867 · 2026-05-19T04:55:16.758978+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1868 · 2026-05-19T04:55:17.210947+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib:1:% Auto-generated from literature_map.yaml — do not edit manually

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1869 · 2026-05-19T04:55:17.662950+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1870 · 2026-05-19T04:55:18.165211+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1871 · 2026-05-19T04:55:18.667434+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\textendash",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\textendash",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1872 · 2026-05-19T04:55:19.119627+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:15:Two factors shape this gap: (a)~\textit{instance degeneracy}, the fraction of instances where all $N$ samples produce identical F1, (13\textendash 87\% across our benchmarks) limits the available headroom; (b)~\textit{LP-quality alignment} (within-instance $\rho(\text{LP}, \text{F1})$) determines whether LP can exploit the remaining headroom (\S\ref{sec:discussion}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:28:We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B\textendash 8B range; behavior at 70B+ scales remains an open question.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2:We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:3:We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:6:We diagnose two causes: instance degeneracy (13\textendash 87\%) and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1873 · 2026-05-19T04:55:19.170259+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1874 · 2026-05-19T04:55:19.220766+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1875 · 2026-05-19T04:55:23.034022+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", highlighting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", highlighting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1876 · 2026-05-19T04:55:23.536067+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1877 · 2026-05-19T04:55:23.536617+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", demonstrating",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", demonstrating",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1878 · 2026-05-19T04:55:23.988032+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1879 · 2026-05-19T04:55:24.941217+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1880 · 2026-05-19T04:55:25.443040+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1881 · 2026-05-19T04:55:26.245892+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "leverage|utilize|delve|plethora|myriad|paradigm shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "leverage|utilize|delve|plethora|myriad|paradigm shift",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 1882 · 2026-05-19T04:55:26.296495+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1883 · 2026-05-19T04:55:36.581310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1250",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1250",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1884 · 2026-05-19T04:55:36.581872+00:00_

1250	\begin{table}[t]
1251	\centering
1252	\small
1253	\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
1254	\label{tab:fewnerd_full}
1255	\begin{tabular}{lcccc}
1256	\toprule
1257	Signal & $\rho$ & Sample AUROC & Sel.\ $\Delta$ & 95\% CI \\
1258	\midrule
1259	LP & .220 & .578 & $\mathbf{+1.39}$\,pp & [+1.18, +1.53] \\
1260	VC & .386 & --- & $-$1.79\,pp & --- \\
1261	FK & .313 & --- & $-$2.26\,pp & --- \\
1262	SJ & .300 & --- & $-$2.14\,pp & --- \\
1263	EM & .287 & --- & $-$3.85\,pp & --- \\
1264	\midrule
1265	\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
1266	\bottomrule
1267	\end{tabular}
1268	\end{table}
1269	
1270	\paragraph{Key observations.}
1271	(1)~All five signals achieve positive QE ($\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.
1272	(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.
1273	(3)~Despite positive $\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.
1274	(4)~Low degeneracy (13.8\%) combined with strong LP-quality alignment ($\rho{\approx}0.5$--$0.7$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (17.8\% degeneracy but weak alignment $\rho{\approx}0.24$, LP $+0.61$~pp) and
…[truncated 18239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1885 · 2026-05-19T04:56:46.944369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers page limit format requirements submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers page limit format requirements submission guidelines"
  }
}
```

</details>

---


### Tool result

_source line 1886 · 2026-05-19T04:56:55.759313+00:00_

Web search results for query: "EMNLP 2026 call for papers page limit format requirements submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

I found information about EMNLP 2026 submission guidelines, but I need to search for more specific details about page limits and format requirements.

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Porta
…[truncated 2161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8814
}
```

</details>

---


### Tool call

_source line 1887 · 2026-05-19T04:59:41.355727+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**审查侧重**: 新颖性 + 叙事统一性 + Related Work 质量 + 格式合规 + 写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 实验设计严谨、分析透彻的实证研究，但核心贡献（诊断 + entity-level construction）的新颖性增量有限，不足以支撑 EMNLP main conference。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 | 实验设计严谨：多种统计检验（bootstrap CI、paired sign test、TOST equivalence、Bonferroni correction），多 seed 验证，消融充分。少数统计问题（见 W2、W3）。 |\n| **Excitement** | 2/5 | 核心发现在概念层面缺乏意外性：4/5 signal 是 instance-level 因此不能 rank candidates（定义性而非经验性）；entity-level construction 本质是 entity-level majority voting（已有大量 ensemble NER 工作）。 |\n| **Reproducibility** | 4/5 | 训练配置、prompt template、超参数均详细报告（Appendix Table 8）；数据集全部公开可用；constrained decoding 工具已注明。代码承诺 upon acceptance 发布。 |\n\n---\n\n## Summary\n\n本文研究 self-consistency 方法在 NER 任务上的适用性。作者评估了 5 种 confidence signal 在 quality estimation（QE）和 sample selection 两个维度上的表现，发现 QE 表现良好（ρ up to 0.45, AUROC up to 0.82）但 instance-level selection 普遍失败。作者将此命名为 \"correlation-selection gap\"，归因于两个机制：instance degeneracy（13–87%）和 LP compression。最终提出 entity-level construction（跨 sample 聚合 entity）作为替代方案，在 SciERC (+1.67pp) 和 Few-NERD (+0.88pp) 上取得显著改进。\n\n---\n\n## Strengths\n\n**S1. 实验严谨度高于同类工作。**\n多 seed 稳定性分析（Table 7）、bootstrap CI（Appendix Table 5）、TOST equivalence testing（Appendix Table 6）、外部 equivalence margin 分析、MDE 计算——统计方法论层面做到了高水准。在 NER 领域的 self-consistency/confidence 研究中，这种统计严谨度是少见的。\n\n**S2. 系统性的消融设计。**\ntemperature（4 点）、N-scaling（5 点，N=2 到 32）、model scale（3B/4B/8B）、epoch confound（2–3 点 curve）、LoRA rank、constrained vs. free-form decoding、supervised combination、hidden state probes——每个维度都有对应消融，形成完整的证据网络。\n\n**S3. 问题分解清晰。**\n将 quality estimation 和 sample selection 明确分离是一个好的框架选择；correlation-selection gap 的命名虽然在概念上不够新（见 W1），但作为一个具体现象的操作化定义是有用的。\n\n**S4. 负面结果的透明度。**\n论文如实报告了大量负面结果（supervised combination 失败、hidden state probe 失败、DALS 效果有限、VerbConf 过度自信），没有隐藏或淡化。Limitations section 覆盖全面（15+ 条限制），这是值得肯定的科学态度。\n\n**S5. 写作质量整体良好。**\n无明显 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无 \"Furthermore/Moreover\" 堆叠、无黑名单用词）。技术写作清晰紧凑，术语使用一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Entity-level construction 的新颖性不足**\n- 具体位置：§5.5 (Prescriptive Results), Table 4\n- 问题：Entity-level construction 本质是 entity-level majority voting：对每个 unique entity mention 统计跨 sample 出现频率，保留超过阈值 θ=2/N 的 entity。这是一个自然且直接的想法，与 ensemble NER（如 Xiao et al. 2025 EL4NER、Naderi et al. 2021 等已有工作）在机制上高度相似——区别仅在于 ensemble 跨模型聚合，本文跨同模型 sample 聚合。LP-weighted 变体相对 uniform voting 的增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 的贡献有限。\n- 为什么影响接收：这是论文的两大贡献之一（\"Fixing\" 部分）。如果这部分不具备足够新颖性，论文的 contribution 主要就是诊断性的负面结果，对 main conference 而言贡献量级不够。\n- 建议修改方向：更清晰地 articulate entity-level construction 相对于 ensemble NER entity voting 的技术区别（例如：单模型多 sample vs 多模型，是否有不同的 diversity 特征？LP weighting 在 ensemble 设定下是否可行？）。或将 construction 定位为 \"applying known technique to confirm it works\"，但那就需要 diagnostic 部分有更强的理论贡献来补偿。\n\n**N2** [critical] **Correlation-selection gap 的概念深度有限**\n- 具体位置：§4.2 (The Correlation-Selection Gap), §1 Introduction ¶5\n- 问题：论文将 4/5 信号是 instance-level（对同一 input 的所有 N 个 candidate 赋同一分数）作为 selection 失败的一个关键原因。但这是这些信号的 **定义性质**，不是经验发现——instance-level signal 按定义不能区分 candidate。论文在 §3.1 已明确指出 \"This distinction is consequential for selection\"，但随后仍将其作为 \"gap\" 的组成部分来报告，混淆了定义性限制和经验性发现。真正的经验性发现是：LP（唯一的 per-sample signal）也未能有效 select——这才是 gap 的实质，但它被 4 个 instance-level signal 的\"失败\"稀释了。\n- 为什么影响接收：如果审稿人认为核心发现可归约为 \"instance-level metrics 不能 rank candidates（tautological）+ LP 在 constrained decoding 下被压缩（已知现象，Yun et al. 2025, Schall et al. 2025）\"，论文的诊断贡献将大幅缩水。\n- 建议修改方向：在 framing 上将 instance-level signal 的失败作为 **背景/动机**（\"4/5 signals are instance-level and thus cannot rank by construction; LP is the only viable selector\"），然后将分析聚焦在 LP selection 为何失败的两个机制上。这样 gap 的概念会更有深度——从 \"5 个信号都不行\" 变为 \"唯一有可能的信号也受限于 degeneracy 和 compression\"。\n\n**N3** [critical] **Gating protocol 的 evaluation 使用 test set 作为 probe source**\n- 具体位置：§5.5 LP-alignment gating 段落\n- 问题：论文承认 \"probe instances are drawn from the test set for simplicity; in deployment, a held-out validation set should be used\"。但这意味着 gating protocol 的准确性（\"correctly routes all three evaluated datasets\"）是在 test set 上 evaluated 的，存在信息泄漏。虽然 probe 只用 50 个 instance，且作者指出 adjusted ρ 差距 >0.15，但这仍然是一个方法论上的瑕疵。更重要的是，gating 仅在 3 个 dataset 上验证，且 3 个 dataset 的 ρ 差距很大（SciERC ~0.26, Few-NERD ~0.5-0.7），routing decision 的\"正确性\"可能只是因为差距足够大，而非 protocol 本身 robust。\n- 为什么影响接收：这是 prescriptive contribution 的一部分（\"how to decide between construction and LP selection\"）。在 3 个 dataset 上用 test set 验证的 gating protocol 的 generalizability 存疑。\n- 建议修改方向：至少用 cross-validation 或 development set 重新验证 gating，或明确标注这是 \"proof of concept\" 而非 deployable protocol（论文已部分这样做，但在 contribution list 中仍然列为贡献之一）。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **SciERC greedy F1 值不一致，增加理解负担**\n- 具体位置：§3.3 最后一段，跨 Tables 1-4\n- 问题：论文报告了 4 个不同的 SciERC greedy F1 值（0.640, 0.644, 0.645, 0.650），归因于 \"protocol variants: primary seed vs. multi-seed mean, 5-epoch vs. 3-epoch checkpoint, and gold-filtered vs. full test set\"。虽然 §3.3 末尾有解释，但读者需要在多个表格间追踪不同的 protocol 才能理解数字差异，显著增加了认知负担。\n- 建议：统一使用一个 primary protocol 报告 SciERC 核心结果，将 protocol variant 的差异集中在一个 appendix 表格中说明。\n\n**W2** [warning] **Few-NERD 3-epoch vs 5-epoch 的 confound 未完全消解**\n- 具体位置：§4.1 ¶2, Appendix §H (epoch_confound)\n- 问题：Few-NERD 使用 3 epochs（其他 dataset 使用 5 epochs），论文的解释是 \"earlier convergence\"。这引入了一个重要的 confound：LP selection 在 Few-NERD 上的成功可能部分归因于更早的 early stopping 导致的低 degeneracy。Appendix 提供了 2-point ablation（3 vs 5 epoch），但 (a) 5-epoch LP 仍然 positive (+0.62pp)，说明效果方向不变，这是好的；(b) 但 SciERC 的 3-epoch model degeneracy 仅 6.4% 却 LP selection 仍然失败（−1.24pp），说明 degeneracy 不是唯一因素。论文的结论（LP-quality alignment 是主要因素）是合理的，但 Few-NERD 和 SciERC 之间的 epoch 差异仍然是一个混淆变量。\n- 建议：在 Limitations 或 Discussion 中更明确地讨论：是否有可能在 matched epoch 条件下比较 Few-NERD 和 SciERC（例如都用 3 epoch）。\n\n**W3** [warning] **Abstract 信息密度过高**\n- 具体位置：Abstract（8 行）\n- 问题：Abstract 包含 ρ=0.45, AUROC 0.82, +5–8pp, +1.39pp, p<0.001, 13–87%, ρ=0.052, 23 configurations, +0.88, +1.67pp, p<0.005 等大量数字。这使得 Abstract 读起来像实验报告的压缩版，而非论文故事的精炼概述。审稿人在 30 秒内难以从这些数字中提取核心 message。\n- 建议：保留 2-3 个关键数字（如 construction 的增益和 p-value），将其余数字移入正文。\n\n**W4** [warning] **Selective prediction 贡献的定位不清晰**\n- 具体位置：§5.5 Selective prediction 段落, Contribution #1\n- 问题：Selective prediction（基于 QE score 过滤低置信度 instance，80% coverage 下 +5–8pp）在 Contribution #1 中被列出，但这本质是 QE signal 的直接应用，不是本文的方法创新。任何能预测 instance quality 的 signal 都可以做 selective prediction。将此列为贡献会稀释真正的贡献点。\n- 建议：将 selective prediction 作为 QE signal 实用性的一个 demonstration，而非独立贡献。\n\n**W5** [warning] **模型规模范围有限（4B–8B），对结论普适性的影响**\n- 具体位置：Limitations ¶2\n- 问题：论文仅覆盖 3B–8B 规模的 fine-tuned models，且 Discussion §5 指出 \"degeneracy rises with model capability\"，暗示 70B+ 模型可能情况更糟（degeneracy 更高）。但同时，更大模型可能有更好的 LP-quality alignment，这两个因素的交互效应未知。论文在 Limitations 中承认了这一点，但这限制了结论的适用范围。\n- 建议：在 Limitations 中增加对 70B+/closed-source API 场景的具体讨论（例如：closed-source API 通常不提供 LP，因此 construction 可能是唯一可行方案——这实际上强化了 construction 的贡献）。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Entity-level construction 中 θ=2/N 是 \"tuning-free\" 的，但 θ=0.5（majority voting baseline）的结果在 Appendix 中。能否提供 θ 在 [1/N, 1] 范围内的敏感性分析？θ=2/N 在 N=8 时等于 0.25，这比 majority voting 的 0.5 低很多。这个较低的阈值本质上是在 boost recall 的同时可能降低 precision——能否提供 construction 的 precision/recall 分解来验证？\n\n**Q2.** 论文在 §1 中声称提供 \"the first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction\"。但 Yao et al. 2026 已经研究了 consistency-accuracy correlation for entity and relation extraction，且 Vashurin et al. 2025 (CoCoA) 结合了 confidence 和 consistency。能否更精确地界定 \"first\" 的 scope？\n\n**Q3.** Qwen3-8B SciERC checkpoint 使用了空的 `&lt;think>&lt;/think>` blocks（Appendix §E）。虽然论文通过三个论证排除了影响，但这本身是一个不理想的实验设计。为什么不重新训练一个 clean checkpoint？\n\n**Q4.** Within-instance LP-quality alignment（ρ≈0.26 on SciERC vs ≈0.5-0.7 on Few-NERD）的差异是否可能由 entity type 数量差异驱动（SciERC 6 types vs Few-NERD 8 types）？或者由 train/test distribution shift 驱动？\n\n---\n\n## Missing References\n\n1. **Entity-level aggregation in NER**: 论文引用了 Xiao et al. 2025 (EL4NER) 作为 ensemble NER 的代表，但缺少对 entity-level voting 机制本身的更广泛文献覆盖。例如：\n   - Ratinov & Roth 2009 讨论了 NER 的 ensemble strategies（论文在 appendix 中引用了此文但未在 entity-level voting 的语境下讨论）\n   - Luo et al. 2023 (Zero-shot NER with ChatGPT) 中的 self-annotation + voting 机制\n\n2. **MBR decoding for structured prediction**: Eikema et al. 2025 已被引用，但 Wiher et al. 2022 (\"On Decoding Strategies for Neural Text Generators\") 提供了 MBR 与 MAP decoding 在多种 NLG 任务上的对比，对 selection-gap 的讨论有补充价值。\n\n3. **Test-time compute scaling 的最新进展**: 考虑引用 Muennighoff et al. 2025 (\"s1: Simple Test-Time Scaling\") 或 Qu et al. 2025 (\"Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning\")，因为这些工作进一步探讨了 test-time scaling 在不同任务上的适用性。\n\n---\n\n## 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| ACL 模板 (`\\usepackage[review]{acl}`) | ✅ | 正确使用 review 模式 |\n| 匿名 (`\\author{Anonymous}`) | ✅ | |\n| 正文 ≤8 页 | ⚠️ | 需要确认。正文包含 Abstract + 5 sections + Limitations，其中 Experiments 和 Introduction 都包含大表格和图表。内容密度极高，可能在边界。Discussion 仅 11 行 tex，Conclusion 仅 7 行——这些被压缩以腾出空间给 Experiments，说明正文空间非常紧张。 |\n| Limitations section | ✅ | 在 Conclusion 之后，内容全面（15+ 条限制） |\n| Ethics Statement | ✅ | |\n| Responsible NLP Checklist | ✅ | 认真填写，无全 N/A |\n| 行号 | ✅ | `[review]` 选项启用 |\n| 缩写定义（Abstract 内） | ✅ | NER, QE, AUROC, LP 均在 Abstract 内展开定义 |\n| 引用格式 | ✅ | `\\cite` 和 `\\citep`/`\\citet` 使用一致（parenthetical vs textual） |\n| 引用覆盖 | ✅ | 73 条 bib 条目，69 条被引用；4 条 orphan bib entries（eisenstein2023helping, li2025llms, naderi2021ensemble, sarcinelli2025local）不影响论文 |\n| 引用真实性 | ✅ | OpenAlex 验证：64 条 verified，4 条 not found（可能为最新 preprint），5 条 minor mismatch（first_author 格式差异或 year 差异）。无 fake citation。 |\n\n---\n\n## 写作质量检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| Em-dash (—) | ✅ | 仅在 .bib 注释中出现一次，正文无 |\n| En-dash 解释性用法 ( – ) | ✅ | 无 |\n| \\textendash | ✅ | 仅用于数值范围（4B–8B, 13–87%），用法正确 |\n| -ing phrase 结尾 | ✅ | 未检出 |\n| 过度分段 | ✅ | 段落长度适中 |\n| 黑名单用词 (leverage/utilize/delve/myriad/plethora) | ✅ | 未检出 |\n| 连续过渡词 (Furthermore/Moreover/Additionally) | ✅ | 未检出 |\n\n---\n\n## 主要优势总结\n\n1. 统计方法论严谨度在 NER/IE 领域罕见（多重检验校正、equivalence testing、外部 margin 等）\n2. 消融设计系统完整，形成闭环的证据网络\n3. 负面结果的透明报告（6+ negative experiments: supervised combination, hidden probes, DeBERTa verifier, DALS, VerbConf, calibration baseline）\n4. 写作质量高，无 AI 痕迹，技术表述清晰\n5. Limitations section 堪称范例（覆盖全面、诚实、有具体建议）\n\n---\n\n## Overall Assessment\n\n**3/5 — Findings**\n\n本文是一篇高质量的实证分析论文，实验设计和统计方法论的严谨度远高于同类工作。核心问题（self-consistency 如何适用于 structured IE）有实际意义。\n\n但两个核心贡献的新颖性存在疑虑：\n- **Diagnostic**: correlation-selection gap 的概念中，4/5 signal 的失败是定义性的（instance-level signal 不能 rank candidates），LP 在 constrained decoding 下的压缩是已知现象。Instance degeneracy 的 operationalization 有价值，但概念层面并不 surprising。\n- **Prescriptive**: entity-level construction 本质是 entity-level majority voting（well-known in ensemble NER），LP weighting 的增量贡献微小。\n\n论文更适合 Findings track：分析透彻、实验扎实、对 practitioner 有直接参考价值，但概念创新不足以进入 main conference。如果作者能在 rebuttal 中 (a) 更清晰地 differentiate entity-level construction 与已有 ensemble NER voting，(b) 提供 gating protocol 的 proper validation（non-test-set probe），(c) 深化 correlation-selection gap 的理论解释（而非仅仅是 \"degeneracy + compression\" 的实证组合），评分有上调空间。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**审查侧重**: 新颖性 + 叙事统一性 + Related Work 质量 + 格式合规 + 写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 实验设计严谨、分析透彻的实证研究，但核心贡献（诊断 + entity-level construction）的新颖性增量有限，不足以支撑 EMNLP main conference。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 | 实验设计严谨：多种统计检验（bootstrap CI、paired sign test、TOST equivalence、Bonferroni correction），多 seed 验证，消融充分。少数统计问题（见 W2、W3）。 |\n| **Excitement** | 2/5 | 核心发现在概念层面缺乏意外性：4/5 signal 是 instance-level 因此不能 rank candidates（定义性而非经验性）；entity-level construction 本质是 entity-level majority voting（已有大量 ensemble NER 工作）。 |\n| **Reproducibility** | 4/5 | 训练配置、prompt template、超参数均详细报告（Appendix Table 8）；数据集全部公开可用；constrained decoding 工具已注明。代码承诺 upon acceptance 发布。 |\n\n---\n\n## Summary\n\n本文研究 self-consistency 方法在 NER 任务上的适用性。作者评估了 5 种 confidence signal 在 quality estimation（QE）和 sample selection 两个维度上的表现，发现 QE 表现良好（ρ up to 0.45, AUROC up to 0.82）但 instance-level selection 普遍失败。作者将此命名为 \"correlation-selection gap\"，归因于两个机制：instance degeneracy（13–87%）和 LP compression。最终提出 entity-level construction（跨 sample 聚合 entity）作为替代方案，在 SciERC (+1.67pp) 和 Few-NERD (+0.88pp) 上取得显著改进。\n\n---\n\n## Strengths\n\n**S1. 实验严谨度高于同类工作。**\n多 seed 稳定性分析（Table 7）、bootstrap CI（Appendix Table 5）、TOST equivalence testing（Appendix Table 6）、外部 equivalence margin 分析、MDE 计算——统计方法论层面做到了高水准。在 NER 领域的 self-consistency/confidence 研究中，这种统计严谨度是少见的。\n\n**S2. 系统性的消融设计。**\ntemperature（4 点）、N-scaling（5 点，N=2 到 32）、model scale（3B/4B/8B）、epoch confound（2–3 点 curve）、LoRA rank、constrained vs. free-form decoding、supervised combination、hidden state probes——每个维度都有对应消融，形成完整的证据网络。\n\n**S3. 问题分解清晰。**\n将 quality estimation 和 sample selection 明确分离是一个好的框架选择；correlation-selection gap 的命名虽然在概念上不够新（见 W1），但作为一个具体现象的操作化定义是有用的。\n\n**S4. 负面结果的透明度。**\n论文如实报告了大量负面结果（supervised combination 失败、hidden state probe 失败、DALS 效果有限、VerbConf 过度自信），没有隐藏或淡化。Limitations section 覆盖全面（15+ 条限制），这是值得肯定的科学态度。\n\n**S5. 写作质量整体良好。**\n无明显 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无 \"Furthermore/Moreover\" 堆叠、无黑名单用词）。技术写作清晰紧凑，术语使用一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Entity-level construction 的新颖性不足**\n- 具体位置：§5.5 (Prescriptive Results), Table 4\n- 问题：Entity-level construction 本质是 entity-level majority voting：对每个 unique entity mention 统计跨 sample 出现频率，保留超过阈值 θ=2/N 的 entity。这是一个自然且直接的想法，与 ensemble NER（如 Xiao et al. 2025 EL4NER、Naderi et al. 2021 等已有工作）在机制上高度相似——区别仅在于 ensemble 跨模型聚合，本文跨同模型 sample 聚合。LP-weighted 变体相对 uniform voting 的增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 的贡献有限。\n- 为什么影响接收：这是论文的两大贡献之一（\"Fixing\" 部分）。如果这部分不具备足够新颖性，论文的 contribution 主要就是诊断性的负面结果，对 main conference 而言贡献量级不够。\n- 建议修改方向：更清晰地 articulate entity-level construction 相对于 ensemble NER entity voting 的技术区别（例如：单模型多 sample vs 多模型，是否有不同的 diversity 特征？LP weighting 在 ensemble 设定下是否可行？）。或将 construction 定位为 \"applying known technique to confirm it works\"，但那就需要 diagnostic 部分有更强的理论贡献来补偿。\n\n**N2** [critical] **Correlation-selection gap 的概念深度有限**\n- 具体位置：§4.2 (The Correlation-Selection Gap), §1 Introduction ¶5\n- 问题：论文将 4/5 信号是 instance-level（对同一 input 的所有 N 个 candidate 赋同一分数）作为 selection 失败的一个关键原因。但这是这些信号的 **定义性质**，不是经验发现——instance-level signal 按定义不能区分 candidate。论文在 §3.1 已明确指出 \"This distinction is consequential for selection\"，但随后仍将其作为 \"gap\" 的组成部分来报告，混淆了定义性限制和经验性发现。真正的经验性发现是：LP（唯一的 per-sample signal）也未能有效 select——这才是 gap 的实质，但它被 4 个 instance-level signal 的\"失败\"稀释了。\n- 为什么影响接收：如果审稿人认为核心发现可归约为 \"instance-level metrics 不能 rank candidates（tautological）+ LP 在 constrained decoding 下被压缩（已知现象，Yun et al. 2025, Schall et al. 2025）\"，论文的诊断贡献将大幅缩水。\n- 建议修改方向：在 framing 上将 instance-level signal 的失败作为 **背景/动机**（\"4/5 signals are instance-level and thus cannot rank by construction; LP is the only viable selector\"），然后将分析聚焦在 LP selection 为何失败的两个机制上。这样 gap 的概念会更有深度——从 \"5 个信号都不行\" 变为 \"唯一有可能的信号也受限于 degeneracy 和 compression\"。\n\n**N3** [critical] **Gating protocol 的 evaluation 使用 test set 作为 probe source**\n- 具体位置：§5.5 LP-alignment gating 段落\n- 问题：论文承认 \"probe instances are drawn from the test set for simplicity; in deployment, a held-out validation set should be used\"。但这意味着 gating protocol 的准确性（\"correctly routes all three evaluated datasets\"）是在 test set 上 evaluated 的，存在信息泄漏。虽然 probe 只用 50 个 instance，且作者指出 adjusted ρ 差距 >0.15，但这仍然是一个方法论上的瑕疵。更重要的是，gating 仅在 3 个 dataset 上验证，且 3 个 dataset 的 ρ 差距很大（SciERC ~0.26, Few-NERD ~0.5-0.7），routing decision 的\"正确性\"可能只是因为差距足够大，而非 protocol 本身 robust。\n- 为什么影响接收：这是 prescriptive contribution 的一部分（\"how to decide between construction and LP selection\"）。在 3 个 dataset 上用 test set 验证的 gating protocol 的 generalizability 存疑。\n- 建议修改方向：至少用 cross-validation 或 development set 重新验证 gating，或明确标注这是 \"proof of concept\" 而非 deployable protocol（论文已部分这样做，但在 contribution list 中仍然列为贡献之一）。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **SciERC greedy F1 值不一致，增加理解负担**\n- 具体位置：§3.3 最后一段，跨 Tables 1-4\n- 问题：论文报告了 4 个不同的 SciERC greedy F1 值（0.640, 0.644, 0.645, 0.650），归因于 \"protocol variants: primary seed vs. multi-seed mean, 5-epoch vs. 3-epoch checkpoint, and gold-filtered vs. full test set\"。虽然 §3.3 末尾有解释，但读者需要在多个表格间追踪不同的 protocol 才能理解数字差异，显著增加了认知负担。\n- 建议：统一使用一个 primary protocol 报告 SciERC 核心结果，将 protocol variant 的差异集中在一个 appendix 表格中说明。\n\n**W2** [warning] **Few-NERD 3-epoch vs 5-epoch 的 confound 未完全消解**\n- 具体位置：§4.1 ¶2, Appendix §H (epoch_confound)\n- 问题：Few-NERD 使用 3 epochs（其他 dataset 使用 5 epochs），论文的解释是 \"earlier convergence\"。这引入了一个重要的 confound：LP selection 在 Few-NERD 上的成功可能部分归因于更早的 early stopping 导致的低 degeneracy。Appendix 提供了 2-point ablation（3 vs 5 epoch），但 (a) 5-epoch LP 仍然 positive (+0.62pp)，说明效果方向不变，这是好的；(b) 但 SciERC 的 3-epoch model degeneracy 仅 6.4% 却 LP selection 仍然失败（−1.24pp），说明 degeneracy 不是唯一因素。论文的结论（LP-quality alignment 是主要因素）是合理的，但 Few-NERD 和 SciERC 之间的 epoch 差异仍然是一个混淆变量。\n- 建议：在 Limitations 或 Discussion 中更明确地讨论：是否有可能在 matched epoch 条件下比较 Few-NERD 和 SciERC（例如都用 3 epoch）。\n\n**W3** [warning] **Abstract 信息密度过高**\n- 具体位置：Abstract（8 行）\n- 问题：Abstract 包含 ρ=0.45, AUROC 0.82, +5–8pp, +1.39pp, p<0.001, 13–87%, ρ=0.052, 23 configurations, +0.88, +1.67pp, p<0.005 等大量数字。这使得 Abstract 读起来像实验报告的压缩版，而非论文故事的精炼概述。审稿人在 30 秒内难以从这些数字中提取核心 message。\n- 建议：保留 2-3 个关键数字（如 construction 的增益和 p-value），将其余数字移入正文。\n\n**W4** [warning] **Selective prediction 贡献的定位不清晰**\n- 具体位置：§5.5 Selective prediction 段落, Contribution #1\n- 问题：Selective prediction（基于 QE score 过滤低置信度 instance，80% coverage 下 +5–8pp）在 Contribution #1 中被列出，但这本质是 QE signal 的直接应用，不是本文的方法创新。任何能预测 instance quality 的 signal 都可以做 selective prediction。将此列为贡献会稀释真正的贡献点。\n- 建议：将 selective prediction 作为 QE signal 实用性的一个 demonstration，而非独立贡献。\n\n**W5** [warning] **模型规模范围有限（4B–8B），对结论普适性的影响**\n- 具体位置：Limitations ¶2\n- 问题：论文仅覆盖 3B–8B 规模的 fine-tuned models，且 Discussion §5 指出 \"degeneracy rises with model capability\"，暗示 70B+ 模型可能情况更糟（degeneracy 更高）。但同时，更大模型可能有更好的 LP-quality alignment，这两个因素的交互效应未知。论文在 Limitations 中承认了这一点，但这限制了结论的适用范围。\n- 建议：在 Limitations 中增加对 70B+/closed-source API 场景的具体讨论（例如：closed-source API 通常不提供 LP，因此 construction 可能是唯一可行方案——这实际上强化了 construction 的贡献）。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Entity-level construction 中 θ=2/N 是 \"tuning-free\" 的，但 θ=0.5（majority voting baseline）的结果在 Appendix 中。能否提供 θ 在 [1/N, 1] 范围内的敏感性分析？θ=2/N 在 N=8 时等于 0.25，这比 majority voting 的 0.5 低很多。这个较低的阈值本质上是在 boost recall 的同时可能降低 precision——能否提供 construction 的 precision/recall 分解来验证？\n\n**Q2.** 论文在 §1 中声称提供 \"the first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction\"。但 Yao et al. 2026 已经研究了 consistency-accuracy correlation for entity and relation extraction，且 Vashurin et al. 2025 (CoCoA) 结合了 confidence 和 consistency。能否更精确地界定 \"first\" 的 scope？\n\n**Q3.** Qwen3-8B SciERC checkpoint 使用了空的 `&lt;think>&lt;/think>` blocks（Appendix §E）。虽然论文通过三个论证排除了影响，但这本身是一个不理想的实验设计。为什么不重新训练一个 clean checkpoint？\n\n**Q4.** Within-instance LP-quality alignment（ρ≈0.26 on SciERC vs ≈0.5-0.7 on Few-NERD）的差异是否可能由 entity type 数量差异驱动（SciERC 6 types vs Few-NERD 8 types）？或者由 train/test distribution shift 驱动？\n\n---\n\n## Missing References\n\n1. **Entity-level aggregation in NER**: 论文引用了 Xiao et al. 2025 (EL4NER) 作为 ensemble NER 的代表，但缺少对 entity-level voting 机制本身的更广泛文献覆盖。例如：\n   - Ratinov & Roth 2009 讨论了 NER 的 ensemble strategies（论文在 appendix 中引用了此文但未在 entity-level voting 的语境下讨论）\n   - Luo et al. 2023 (Zero-shot NER with ChatGPT) 中的 self-annotation + voting 机制\n\n2. **MBR decoding for structured prediction**: Eikema et al. 2025 已被引用，但 Wiher et al. 2022 (\"On Decoding Strategies for Neural Text Generators\") 提供了 MBR 与 MAP decoding 在多种 NLG 任务上的对比，对 selection-gap 的讨论有补充价值。\n\n3. **Test-time compute scaling 的最新进展**: 考虑引用 Muennighoff et al. 2025 (\"s1: Simple Test-Time Scaling\") 或 Qu et al. 2025 (\"Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning\")，因为这些工作进一步探讨了 test-time scaling 在不同任务上的适用性。\n\n---\n\n## 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| ACL 模板 (`\\usepackage[review]{acl}`) | ✅ | 正确使用 review 模式 |\n| 匿名 (`\\author{Anonymous}`) | ✅ | |\n| 正文 ≤8 页 | ⚠️ | 需要确认。正文包含 Abstract + 5 sections + Limitations，其中 Experiments 和 Introduction 都包含大表格和图表。内容密度极高，可能在边界。Discussion 仅 11 行 tex，Conclusion 仅 7 行——这些被压缩以腾出空间给 Experiments，说明正文空间非常紧张。 |\n| Limitations section | ✅ | 在 Conclusion 之后，内容全面（15+ 条限制） |\n| Ethics Statement | ✅ | |\n| Responsible NLP Checklist | ✅ | 认真填写，无全 N/A |\n| 行号 | ✅ | `[review]` 选项启用 |\n| 缩写定义（Abstract 内） | ✅ | NER, QE, AUROC, LP 均在 Abstract 内展开定义 |\n| 引用格式 | ✅ | `\\cite` 和 `\\citep`/`\\citet` 使用一致（parenthetical vs textual） |\n| 引用覆盖 | ✅ | 73 条 bib 条目，69 条被引用；4 条 orphan bib entries（eisenstein2023helping, li2025llms, naderi2021ensemble, sarcinelli2025local）不影响论文 |\n| 引用真实性 | ✅ | OpenAlex 验证：64 条 verified，4 条 not found（可能为最新 preprint），5 条 minor mismatch（first_author 格式差异或 year 差异）。无 fake citation。 |\n\n---\n\n## 写作质量检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| Em-dash (—) | ✅ | 仅在 .bib 注释中出现一次，正文无 |\n| En-dash 解释性用法 ( – ) | ✅ | 无 |\n| \\textendash | ✅ | 仅用于数值范围（4B–8B, 13–87%），用法正确 |\n| -ing phrase 结尾 | ✅ | 未检出 |\n| 过度分段 | ✅ | 段落长度适中 |\n| 黑名单用词 (leverage/utilize/delve/myriad/plethora) | ✅ | 未检出 |\n| 连续过渡词 (Furthermore/Moreover/Additionally) | ✅ | 未检出 |\n\n---\n\n## 主要优势总结\n\n1. 统计方法论严谨度在 NER/IE 领域罕见（多重检验校正、equivalence testing、外部 margin 等）\n2. 消融设计系统完整，形成闭环的证据网络\n3. 负面结果的透明报告（6+ negative experiments: supervised combination, hidden probes, DeBERTa verifier, DALS, VerbConf, calibration baseline）\n4. 写作质量高，无 AI 痕迹，技术表述清晰\n5. Limitations section 堪称范例（覆盖全面、诚实、有具体建议）\n\n---\n\n## Overall Assessment\n\n**3/5 — Findings**\n\n本文是一篇高质量的实证分析论文，实验设计和统计方法论的严谨度远高于同类工作。核心问题（self-consistency 如何适用于 structured IE）有实际意义。\n\n但两个核心贡献的新颖性存在疑虑：\n- **Diagnostic**: correlation-selection gap 的概念中，4/5 signal 的失败是定义性的（instance-level signal 不能 rank candidates），LP 在 constrained decoding 下的压缩是已知现象。Instance degeneracy 的 operationalization 有价值，但概念层面并不 surprising。\n- **Prescriptive**: entity-level construction 本质是 entity-level majority voting（well-known in ensemble NER），LP weighting 的增量贡献微小。\n\n论文更适合 Findings track：分析透彻、实验扎实、对 practitioner 有直接参考价值，但概念创新不足以进入 main conference。如果作者能在 rebuttal 中 (a) 更清晰地 differentiate entity-level construction 与已有 ensemble NER voting，(b) 提供 gating protocol 的 proper validation（non-test-set probe），(c) 深化 correlation-selection gap 的理论解释（而非仅仅是 \"degeneracy + compression\" 的实证组合），评分有上调空间。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1888 · 2026-05-19T04:59:45.169298+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3813
}
```

</details>

---


### Assistant

_source line 1889 · 2026-05-19T04:59:54.484821+00:00_

审稿意见已提交给 Review Director。

核心判断：**Overall 3/5 (Findings)**。

三个 critical 问题：
1. Entity-level construction 的新颖性有限——本质是 entity-level majority voting，与已有 ensemble NER 工作（EL4NER 等）机制高度相似，LP-weighting 增量微小
2. Correlation-selection gap 概念的深度不够——4/5 signal 的失败是定义性的（instance-level 不能 rank candidates），LP compression 是已知现象
3. Gating protocol 使用 test set probe + 仅 3 dataset 验证，方法论上有瑕疵

主要优势：统计严谨度在同领域罕见，消融设计系统完整，负面结果透明报告，写作质量高（无 AI 痕迹），格式合规无问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 48

## Round 48

8 recorded events


### User

_source line 1890 · 2026-05-19T05:00:49.569742+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你与 Reviewer 1 在以下问题上是否存在分歧：
- ε=0.05 non-tied subset 的叙事权重（R1-N2）——你是否认为这是同等严重的问题？
- Expected selection gain bound 的形式化程度（R1-N3）——你对 "bound" vs "heuristic" 的判断？
- θ=2/N "tuning-free" claim（R1-W1）——你是否同意需要 sensitivity sweep？

---

## Reviewer 1 完整审稿意见

### Must-Fix 问题

**N1** [critical] **LP-alignment gating 使用 test set 构成 information leakage**
- Gating protocol 使用 50 个 test set instances 估计 within-instance ρ(LP, F1)，然后基于该估计选择方法应用于同一 test set。Gold labels 参与了 gating decision。
- 建议：(a) held-out validation set 重新验证，或 (b) leave-one-dataset-out CV，或 (c) 降级为 "illustrative proof of concept"。

**N2** [critical] **Non-tied subset ε=0.05 是 post-hoc 最优切点，叙事权重过高**
- ε sweep（Table 10）显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），相邻切点显著性更弱。Bonferroni 校正应覆盖 ε sweep 的多重比较（7 个阈值），而非仅覆盖 5 个 signal。
- 建议：对 ε sweep 做 Bonferroni/BH 校正，降低该结果在叙事中的权重。

**N3** [critical] **Expected selection gain "bound" 缺乏形式化**
- E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within)，其中 g(·) 被描述为 "monotonically increasing function" 但从未定义。没有定理、引理或证明。
- 建议：给出 g(·) 具体形式并推导，或将 "bounded by" 改为 "decomposed as"/"heuristically approximated by"。

### Should-Fix 问题

**W1** [warning] Entity construction θ=2/N "tuning-free" claim 缺证据——无 θ sensitivity sweep
**W2** [warning] SciERC greedy F1 出现 4 个值，协议不统一（Table 2 用 2-seed vs Table 3/7 用 3-seed）
**W3** [warning] 3-seed 统计功效不足以支撑 ranking stability claims（Kendall's W=1.0, m=3）
**W4** [warning] Complementarity claim 仅基于 3 个 dataset（实际仅 2 个 informative data points）
**W5** [warning] 模型规模覆盖仅 3B-8B，claims 表述过于一般化

### 小问题
- Table D.1 diversity "Identical" vs "Constant F1" 概念混淆
- Table 4 缺少 multi-seed ±σ
- WNUT-17 under-analyzed
- Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致
- Appendix 体量过大（7:1 ratio）

### 主要优势
诊断框架设计精良; 实验覆盖广; negative results 有价值; 统计方法恰当; 透明度高

### Overall: 3/5 (Findings), Confidence 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1891 · 2026-05-19T05:00:58.318567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "95",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "95",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1892 · 2026-05-19T05:00:58.369292+00:00_

95	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
96	Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
97	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers} (the sole positive finding, non-tied LP subset $+2.9$~pp $p{=}0.004$, survives Bonferroni correction; \S\ref{sec:discussion}).
98	
99	\paragraph{Expected selection gain decomposition.}
100	The expected selection gain is bounded by $\mathbb{E}[\Delta\text{F1}] \leq (1 - d) \cdot \Delta_{\text{oracle}} \cdot g(\rho_{\text{within}})$, where $d$ is the degeneracy rate, $\Delta_{\text{oracle}}$ is the oracle headroom, and $g(\cdot)$ is a monotonically increasing function of within-instance LP-F1 correlation $\rho_{\text{within}}$.
101	This decomposition is consistent with the observed data: SciERC ($d{=}17.8\%$, $\Delta_{\text{oracle}}{=}13.1$\,pp, $\rho_{\text{within}}{=}0.262$) predicts a small gain (actual: $+0.04{\pm}0.48$\,pp, 3-seed mean${\pm}\sigma$; Table~\ref{tab:multiseed}); Few-NERD ($d{=}13.8\%$, $\Delta_{\text{oracle}}{\approx}8$\,pp, $\rho_{\text{within}}{=}0.667$) predicts the largest gain (actual: $+1.39$\,pp); CoNLL ($d{=}48.4\%$, $\Delta_{\text{oracle}}{\approx}2$\,pp, low $\rho_{\text{within}}$) predicts near-zero gain (actual: $-0.85$\,pp).
102	The high SciERC seed variance ($\sigma{=}0.48$\,pp) reflects weak LP-quality alignment ($\rho{\approx}0.26$), consistent with the bound predicting unreliable selection.
103	
104	%% ============================================================
105	\subsection{Cross-Dataset Contrast: Few-NERD}
106	\label{sec:fewnerd}
107	
108	\begin{table}[t]
109	\centering
1
…[truncated 858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1893 · 2026-05-19T05:00:58.520216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "180",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "180",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1894 · 2026-05-19T05:00:58.572277+00:00_

180	%% ============================================================
181	\subsection{Prescriptive Results}
182	\label{sec:prescriptive}
183	
184	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
185	
186	\paragraph{Entity-level construction.}
187	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\theta{=}2/N$ (an entity is included if it appears in ${\geq}2$ of $N$ samples). This threshold is tuning-free across all datasets ($\theta{=}0.5$ majority baseline in Appendix~\ref{app:entity_merge}).
188	
189	\begin{table}[t]
190	\centering
191	\small
192	\caption{Entity-level construction vs.\ greedy decoding ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, matching Tables~\ref{tab:selection}--\ref{tab:fewnerd}). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\theta{=}2/N$ (tuning-free). $p$: paired bootstrap vs.\ greedy. Best per dataset in \textbf{bold}.}
193	\label{tab:entity_construction}
194	\begin{tabular}{@{}llcccc@{}}
195	\toprule
196	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
197	\midrule
198	SciERC & LP & .644 & $\mathbf{.661}$ & $+$1.67\,pp & .004 \\
199	       & Unif. & .644 & .659 & $+$1.54\,pp & .023 \\
200	\addlinespace
201	Few-NERD & LP & .748 & $\mathbf{.757}$ & $+$0.88\,pp & ${<}.001$ \\
202	         & Unif. & .748 & .751 & $+$0.32\,pp & .003 \\
203	\addlinespace
204	CoNLL & Unif. & .908 & .904 & $-$0.39\,pp & n.s. \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	LP-weighted construction significantly improves over greedy on SciERC ($+1.67$\,pp, $p{=}0.004$) and Few-NERD ($+0.88$\,pp, $p{<}0.001$; Table~\ref{tab:entity_construction}). CoNLL shows no significant gain ($-0.39$\,pp
…[truncated 2548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1895 · 2026-05-19T05:02:36.482617+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 的审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[AGREE] R1-N1: LP-alignment gating 使用 test set 构成 information leakage**\n\n同意。这与我的 N3 完全一致。§5.5 LP-alignment gating 段落承认 \"probe instances are drawn from the test set for simplicity\"，但论文仍将 gating protocol 列为 Contribution #3 的一部分（\"an alignment-based gating protocol correctly routes all three evaluated datasets\"）。Gold F1 labels 参与了 gating decision，这不仅是 information leakage，更是让 gating 的\"正确性\"无法被信任。\n\n补充：论文自己写了三条 caveats (a)(b)(c)，实际上已经承认了这个问题。建议同 R1：要么用 proper validation set 重新验证，要么在 Contribution list 中明确降级为 \"proof of concept\"，不作为独立贡献列出。\n\n---\n\n**[AGREE] R1-N2: Non-tied subset ε=0.05 是 post-hoc 最优切点，叙事权重过高**\n\n同意这是一个真实问题，但我对严重程度的判断与 R1 略有不同。\n\n**同意的部分**：Table 10（ε sweep）确实显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），且论文在 Appendix §F 已标注这是 \"post-hoc exploratory analysis\"。但主文 §4.2 中的措辞（\"the sole positive finding, non-tied LP subset +2.9pp p=0.004, survives Bonferroni correction\"）中的 Bonferroni correction 仅覆盖 5 个 signal comparisons，未覆盖 ε sweep 的 7 个阈值。如果做 7×5=35 的 Bonferroni correction，p_adj = 0.004 × 35 = 0.14，不再显著。R1 的批评在统计层面是正确的。\n\n**不完全同意的部分**：论文在 §F 第一段已明确将 ε=0.05 定义为 \"post-hoc exploratory choice\"，且 Table 9 的 ε robustness 分析显示 selection F1 本身在 ε ∈ [0, 0.2] 范围内变化不大（consistency signals ≤1.09pp）。所以这个结果的叙事功能更多是 \"characterizing the compression phenomenon\" 而非 \"demonstrating a tuned selection strategy\"——论文的 Limitations section 第11段已明确这一点。问题不在于结果本身，而在于主文 §4.2 的措辞（\"survives Bonferroni correction\"）给读者一种该结果已经充分校正的印象。\n\n**建议**：(a) 将主文中 \"survives Bonferroni correction\" 改为明确说明 Bonferroni 范围（仅 5 signals，未含 ε sweep）；(b) 将 non-tied subset 的讨论从 §4.2 移至 Discussion 或 Appendix，降低叙事权重；(c) 补充 ε sweep 的 BH correction 结果。\n\n---\n\n**[AGREE with reservation] R1-N3: Expected selection gain \"bound\" 缺乏形式化**\n\n同意方向，但对严重程度的判断比 R1 宽容。\n\n**同意的部分**：§4.2 中的 E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within) 确实不是一个形式化的 bound。g(·) 被描述为 \"monotonically increasing function\" 但从未给出具体形式或推导。在数学上，一个包含未定义函数的不等式不构成 bound——它更接近一个 conceptual decomposition。\n\n**保留意见**：这个 \"bound\" 在论文中的角色是 **组织叙事**而非提供理论保证。它帮助读者理解三个因素（degeneracy、oracle headroom、LP alignment）如何交互影响 selection gain，并且论文确实用 3 个 dataset 的实际数据验证了 decomposition 的一致性（§4.2 第101行）。如果将 \"bounded by\" 改为 \"decomposed as\" 或 \"heuristically characterized by\"，这个框架的诊断价值不变。与 R1 不同的是，我不认为这需要正式定理/证明——这是一篇实证论文，不是理论论文。要求形式化推导可能超出了论文的 scope。\n\n**建议**：将 \"bounded by\" 改为 \"heuristically decomposed as\"，并在脚注中说明 g(·) 的具体假设（例如 g(0)=0, g(1)=1，或引用 decision-theoretic framework 来 justify monotonicity）。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: Entity construction θ=2/N \"tuning-free\" claim 缺乏 θ sensitivity sweep**\n\n同意。这也是我在 Q1 中提出的问题。§5.5 声称 θ=2/N 是 \"tuning-free across all datasets\"，但仅提供了 θ=0.5（majority baseline）作为对比（提及 Appendix），没有展示 θ 在 [1/N, 1] 范围内的 sensitivity curve。θ=2/N 在 N=8 时等于 0.25，比 majority voting 的 0.5 低很多——这本质上是在大幅 boost recall（任何在 ≥2/8 个 sample 中出现的 entity 都被保留），可能在某些 high-noise 场景下引入大量 false positives。没有 precision/recall 分解和 θ sweep，\"tuning-free\" 的 claim 不成立。\n\n---\n\n**[AGREE] R1-W2: SciERC greedy F1 的 4 个值增加理解负担**\n\n同意，与我的 W1 一致。§3.3 末尾的解释（\"protocol variants: primary seed vs. multi-seed mean, 5-epoch vs. 3-epoch checkpoint, and gold-filtered vs. full test set\"）虽然存在，但分散在正文最后，而非在第一次出现不一致数值时就说明。建议统一一个 primary protocol，差异集中在 appendix 说明。\n\n---\n\n**[AGREE] R1-W3: 3-seed 统计功效不足以支撑 ranking stability claims**\n\n同意。Appendix Table 12 报告 Kendall's W=1.0（m=3 raters），论文自己也注明 \"interpret with caution given low m; exact p≈0.028\"。但 m=3 时 W=1.0 的含义仅仅是 3 个 seed 碰巧给出了相同排名——这在很大程度上可能是偶然的，尤其是在 top signals（VC vs SJ）差距很小（Δρ=0.019，bootstrap CI 跨零；Appendix Table 5）的情况下。论文应将这一结果明确标注为 \"descriptive\" 而非 \"robust stability evidence\"。\n\n---\n\n**[AGREE] R1-W4: Complementarity claim 仅基于 3 个 dataset（实际仅 2 个 informative data points）**\n\n同意。CoNLL 因 ceiling effect 两种方法都不 work，不构成 informative data point。实际上 complementarity 的证据来自 2 个 dataset：SciERC（construction 好）和 Few-NERD（LP selection 好）。2 个 data point 不足以支撑 \"complementarity governed by LP-quality alignment\" 的 general claim——可能只是两个不同 dataset 上的巧合。但这个 limitation 在论文中已有 partial acknowledgment（gating 的 caveat (b)），所以问题更多是措辞力度而非实验缺陷。\n\n---\n\n**[AGREE] R1-W5: 模型规模覆盖仅 3B-8B**\n\n同意，与我的 W5 一致。论文的 claims（如标题 \"Diagnosing and Fixing Self-Consistency for NER\"）暗示了比实验覆盖更广的适用范围。但 70B+ 规模下的行为可能根本不同：(a) degeneracy 可能更高（论文自己的 scale ablation 显示 8B > 4B > 3B 的 degeneracy），(b) 但 LP-quality alignment 可能也更强，(c) 更大模型可能根本不需要 multi-sample improvement 因为 greedy 已经很好。建议将 claims 限定为 \"4B–8B fine-tuned models\" 范围。\n\n---\n\n### 小问题回应\n\n**[AGREE] Table D.1 diversity \"Identical\" vs \"Constant F1\" 概念混淆**\n\n同意。Table D.1 的 \"Identical\" 定义为 \"fraction of instances with all N outputs identical\"（string-level），而主文中的 \"instance degeneracy\" 定义为 \"constant F1\"（F1-level）。两个概念不同（相同 F1 不意味着相同 output），但交替使用可能误导读者。例如 Qwen/SciERC \"Identical\"=11% vs \"Constant F1\"=17.8%（Table D.2）——差异 6.8pp 说明确实有 output 不同但 F1 相同的 instances。\n\n**[AGREE] Table 4 缺少 multi-seed ±σ**\n\n同意。Table 4 的 entity construction 结果仅用 single seed 报告，但论文在 Table 3 中用 2-seed，Table 7 中用 3-seed。Prescriptive 贡献理应有更强的统计支撑。\n\n**[AGREE] WNUT-17 under-analyzed**\n\n同意。WNUT-17 在 §4.1 仅被简要提及（\"signal-collapse boundary\"），完整分析在 Appendix Table 3。作为 4 个 benchmark 之一，正文分析不足。但鉴于 WNUT-17 的 52% zero-F1 rate 使其成为 boundary case，不给予过多正文空间是合理的。\n\n**[AGREE] Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致**\n\n同意这会造成困惑。Figure 1 caption 报 ρ=0.39 是 SciERC VC 的值，Abstract 报 ρ=0.45 是 CoNLL EM 的值（Table 1）。两个都正确，但 scope 不同且未在 caption 中说明。\n\n**[REBUT] Appendix 体量过大（7:1 ratio）**\n\n不完全同意。ARR 对 appendix 长度没有明确限制（reviewers are not required to read appendix, but it can be included），且本文 appendix 的内容几乎都是 robustness checks、ablations、negative experiments 的完整报告——这恰恰是正文无法容纳但对 reproducibility 和 soundness 至关重要的材料。如果删减 appendix 以降低 ratio，反而会削弱论文的透明度和可验证性。问题不在 appendix 的量，而在正文是否 self-contained（答案是 yes：正文的核心 claim 不依赖 appendix 的具体数字）。\n\n---\n\n### 总结\n\n与 R1 在 8/12 个问题上完全一致（N1, W1, W2, W3, W4, W5, 以及 3 个小问题）。在 3 个问题上部分一致但对严重程度有不同判断：\n\n1. **ε=0.05（R1-N2）**：同意统计问题真实存在（Bonferroni 未覆盖 ε sweep），但论文已在 Limitations 和 Appendix 中做了适当 hedging。需要修改的是主文 §4.2 的措辞，而非删除该分析。建议从 critical 降为 warning。\n\n2. **Expected selection gain bound（R1-N3）**：同意 \"bounded by\" 措辞不当（g(·) 未定义），但不认为需要形式化定理。这是一个有用的 conceptual decomposition，在实证论文中降级措辞即可。建议从 critical 降为 warning。\n\n3. **Appendix 体量**：不同意这是问题。Appendix 材料对 reproducibility 有价值，且正文 self-contained。\n\n维持 Overall 3/5 (Findings) 评分不变。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 的审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[AGREE] R1-N1: LP-alignment gating 使用 test set 构成 information leakage**\n\n同意。这与我的 N3 完全一致。§5.5 LP-alignment gating 段落承认 \"probe instances are drawn from the test set for simplicity\"，但论文仍将 gating protocol 列为 Contribution #3 的一部分（\"an alignment-based gating protocol correctly routes all three evaluated datasets\"）。Gold F1 labels 参与了 gating decision，这不仅是 information leakage，更是让 gating 的\"正确性\"无法被信任。\n\n补充：论文自己写了三条 caveats (a)(b)(c)，实际上已经承认了这个问题。建议同 R1：要么用 proper validation set 重新验证，要么在 Contribution list 中明确降级为 \"proof of concept\"，不作为独立贡献列出。\n\n---\n\n**[AGREE] R1-N2: Non-tied subset ε=0.05 是 post-hoc 最优切点，叙事权重过高**\n\n同意这是一个真实问题，但我对严重程度的判断与 R1 略有不同。\n\n**同意的部分**：Table 10（ε sweep）确实显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），且论文在 Appendix §F 已标注这是 \"post-hoc exploratory analysis\"。但主文 §4.2 中的措辞（\"the sole positive finding, non-tied LP subset +2.9pp p=0.004, survives Bonferroni correction\"）中的 Bonferroni correction 仅覆盖 5 个 signal comparisons，未覆盖 ε sweep 的 7 个阈值。如果做 7×5=35 的 Bonferroni correction，p_adj = 0.004 × 35 = 0.14，不再显著。R1 的批评在统计层面是正确的。\n\n**不完全同意的部分**：论文在 §F 第一段已明确将 ε=0.05 定义为 \"post-hoc exploratory choice\"，且 Table 9 的 ε robustness 分析显示 selection F1 本身在 ε ∈ [0, 0.2] 范围内变化不大（consistency signals ≤1.09pp）。所以这个结果的叙事功能更多是 \"characterizing the compression phenomenon\" 而非 \"demonstrating a tuned selection strategy\"——论文的 Limitations section 第11段已明确这一点。问题不在于结果本身，而在于主文 §4.2 的措辞（\"survives Bonferroni correction\"）给读者一种该结果已经充分校正的印象。\n\n**建议**：(a) 将主文中 \"survives Bonferroni correction\" 改为明确说明 Bonferroni 范围（仅 5 signals，未含 ε sweep）；(b) 将 non-tied subset 的讨论从 §4.2 移至 Discussion 或 Appendix，降低叙事权重；(c) 补充 ε sweep 的 BH correction 结果。\n\n---\n\n**[AGREE with reservation] R1-N3: Expected selection gain \"bound\" 缺乏形式化**\n\n同意方向，但对严重程度的判断比 R1 宽容。\n\n**同意的部分**：§4.2 中的 E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within) 确实不是一个形式化的 bound。g(·) 被描述为 \"monotonically increasing function\" 但从未给出具体形式或推导。在数学上，一个包含未定义函数的不等式不构成 bound——它更接近一个 conceptual decomposition。\n\n**保留意见**：这个 \"bound\" 在论文中的角色是 **组织叙事**而非提供理论保证。它帮助读者理解三个因素（degeneracy、oracle headroom、LP alignment）如何交互影响 selection gain，并且论文确实用 3 个 dataset 的实际数据验证了 decomposition 的一致性（§4.2 第101行）。如果将 \"bounded by\" 改为 \"decomposed as\" 或 \"heuristically characterized by\"，这个框架的诊断价值不变。与 R1 不同的是，我不认为这需要正式定理/证明——这是一篇实证论文，不是理论论文。要求形式化推导可能超出了论文的 scope。\n\n**建议**：将 \"bounded by\" 改为 \"heuristically decomposed as\"，并在脚注中说明 g(·) 的具体假设（例如 g(0)=0, g(1)=1，或引用 decision-theoretic framework 来 justify monotonicity）。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: Entity construction θ=2/N \"tuning-free\" claim 缺乏 θ sensitivity sweep**\n\n同意。这也是我在 Q1 中提出的问题。§5.5 声称 θ=2/N 是 \"tuning-free across all datasets\"，但仅提供了 θ=0.5（majority baseline）作为对比（提及 Appendix），没有展示 θ 在 [1/N, 1] 范围内的 sensitivity curve。θ=2/N 在 N=8 时等于 0.25，比 majority voting 的 0.5 低很多——这本质上是在大幅 boost recall（任何在 ≥2/8 个 sample 中出现的 entity 都被保留），可能在某些 high-noise 场景下引入大量 false positives。没有 precision/recall 分解和 θ sweep，\"tuning-free\" 的 claim 不成立。\n\n---\n\n**[AGREE] R1-W2: SciERC greedy F1 的 4 个值增加理解负担**\n\n同意，与我的 W1 一致。§3.3 末尾的解释（\"protocol variants: primary seed vs. multi-seed mean, 5-epoch vs. 3-epoch checkpoint, and gold-filtered vs. full test set\"）虽然存在，但分散在正文最后，而非在第一次出现不一致数值时就说明。建议统一一个 primary protocol，差异集中在 appendix 说明。\n\n---\n\n**[AGREE] R1-W3: 3-seed 统计功效不足以支撑 ranking stability claims**\n\n同意。Appendix Table 12 报告 Kendall's W=1.0（m=3 raters），论文自己也注明 \"interpret with caution given low m; exact p≈0.028\"。但 m=3 时 W=1.0 的含义仅仅是 3 个 seed 碰巧给出了相同排名——这在很大程度上可能是偶然的，尤其是在 top signals（VC vs SJ）差距很小（Δρ=0.019，bootstrap CI 跨零；Appendix Table 5）的情况下。论文应将这一结果明确标注为 \"descriptive\" 而非 \"robust stability evidence\"。\n\n---\n\n**[AGREE] R1-W4: Complementarity claim 仅基于 3 个 dataset（实际仅 2 个 informative data points）**\n\n同意。CoNLL 因 ceiling effect 两种方法都不 work，不构成 informative data point。实际上 complementarity 的证据来自 2 个 dataset：SciERC（construction 好）和 Few-NERD（LP selection 好）。2 个 data point 不足以支撑 \"complementarity governed by LP-quality alignment\" 的 general claim——可能只是两个不同 dataset 上的巧合。但这个 limitation 在论文中已有 partial acknowledgment（gating 的 caveat (b)），所以问题更多是措辞力度而非实验缺陷。\n\n---\n\n**[AGREE] R1-W5: 模型规模覆盖仅 3B-8B**\n\n同意，与我的 W5 一致。论文的 claims（如标题 \"Diagnosing and Fixing Self-Consistency for NER\"）暗示了比实验覆盖更广的适用范围。但 70B+ 规模下的行为可能根本不同：(a) degeneracy 可能更高（论文自己的 scale ablation 显示 8B > 4B > 3B 的 degeneracy），(b) 但 LP-quality alignment 可能也更强，(c) 更大模型可能根本不需要 multi-sample improvement 因为 greedy 已经很好。建议将 claims 限定为 \"4B–8B fine-tuned models\" 范围。\n\n---\n\n### 小问题回应\n\n**[AGREE] Table D.1 diversity \"Identical\" vs \"Constant F1\" 概念混淆**\n\n同意。Table D.1 的 \"Identical\" 定义为 \"fraction of instances with all N outputs identical\"（string-level），而主文中的 \"instance degeneracy\" 定义为 \"constant F1\"（F1-level）。两个概念不同（相同 F1 不意味着相同 output），但交替使用可能误导读者。例如 Qwen/SciERC \"Identical\"=11% vs \"Constant F1\"=17.8%（Table D.2）——差异 6.8pp 说明确实有 output 不同但 F1 相同的 instances。\n\n**[AGREE] Table 4 缺少 multi-seed ±σ**\n\n同意。Table 4 的 entity construction 结果仅用 single seed 报告，但论文在 Table 3 中用 2-seed，Table 7 中用 3-seed。Prescriptive 贡献理应有更强的统计支撑。\n\n**[AGREE] WNUT-17 under-analyzed**\n\n同意。WNUT-17 在 §4.1 仅被简要提及（\"signal-collapse boundary\"），完整分析在 Appendix Table 3。作为 4 个 benchmark 之一，正文分析不足。但鉴于 WNUT-17 的 52% zero-F1 rate 使其成为 boundary case，不给予过多正文空间是合理的。\n\n**[AGREE] Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致**\n\n同意这会造成困惑。Figure 1 caption 报 ρ=0.39 是 SciERC VC 的值，Abstract 报 ρ=0.45 是 CoNLL EM 的值（Table 1）。两个都正确，但 scope 不同且未在 caption 中说明。\n\n**[REBUT] Appendix 体量过大（7:1 ratio）**\n\n不完全同意。ARR 对 appendix 长度没有明确限制（reviewers are not required to read appendix, but it can be included），且本文 appendix 的内容几乎都是 robustness checks、ablations、negative experiments 的完整报告——这恰恰是正文无法容纳但对 reproducibility 和 soundness 至关重要的材料。如果删减 appendix 以降低 ratio，反而会削弱论文的透明度和可验证性。问题不在 appendix 的量，而在正文是否 self-contained（答案是 yes：正文的核心 claim 不依赖 appendix 的具体数字）。\n\n---\n\n### 总结\n\n与 R1 在 8/12 个问题上完全一致（N1, W1, W2, W3, W4, W5, 以及 3 个小问题）。在 3 个问题上部分一致但对严重程度有不同判断：\n\n1. **ε=0.05（R1-N2）**：同意统计问题真实存在（Bonferroni 未覆盖 ε sweep），但论文已在 Limitations 和 Appendix 中做了适当 hedging。需要修改的是主文 §4.2 的措辞，而非删除该分析。建议从 critical 降为 warning。\n\n2. **Expected selection gain bound（R1-N3）**：同意 \"bounded by\" 措辞不当（g(·) 未定义），但不认为需要形式化定理。这是一个有用的 conceptual decomposition，在实证论文中降级措辞即可。建议从 critical 降为 warning。\n\n3. **Appendix 体量**：不同意这是问题。Appendix 材料对 reproducibility 有价值，且正文 self-contained。\n\n维持 Overall 3/5 (Findings) 评分不变。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1896 · 2026-05-19T05:02:40.197029+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---


### Assistant

_source line 1897 · 2026-05-19T05:02:48.111661+00:00_

交叉回应已提交给 Review Director。

与 R1 在绝大多数问题上达成共识（8/12 完全一致），在 3 个问题上对严重程度有不同判断：
- **ε=0.05 non-tied subset**：同意统计瑕疵，但论文已有 hedging，建议降为 warning
- **Expected selection gain bound**：同意措辞不当，但不需要形式化定理，降级措辞即可
- **Appendix 体量**：不同意是问题，正文 self-contained，appendix 对 reproducibility 有价值

两位 reviewer 均给出 3/5 (Findings)，核心共识：实验严谨但新颖性不足以进入 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 49

## Round 49

68 recorded events


### User

_source line 1898 · 2026-05-19T06:10:11.582865+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 叙事完整性 + 写作质量 + Related Work positioning**。

## 论文信息
- 标题: "Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition"
- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（modular: `sections/` 下各文件）
- 目标 venue: **EMNLP 2026 Main Conference** (via ACL Rolling Review)
- 截止: 2026-05-25 (AoE)
- 格式: ACL style, long paper 8页正文, double-blind, mandatory Limitations + Checklist
- 附录: ~1571 行，包含大量补充实验

## 你的审查侧重

### 1. 新颖性与贡献度
- "correlation-selection gap" 概念的新颖性如何？instance-level 信号无法做 selection 是否本就显而易见？
- Entity-level construction 本质上是对 ensemble NER 的 entity voting 的直接迁移，新颖性如何评估？
- 相比 Yao et al. (2026), Taubenfeld et al. (2025), Kang et al. (2025) 等直接竞争对手，增量是否显著？
- 负结果（selection 失败）是否足以支撑一篇 EMNLP Main 论文？

### 2. 叙事结构与故事线
- Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的主线是否统一？
- 是否存在"实验报告风格"而非"故事驱动"？
- Introduction 的 5 段结构是否完整？问题重要性论证是否充分？
- Contribution 列表与正文内容是否对应？

### 3. 写作质量（按 CLAUDE.md paper-writing-norms 严格检查）
- 有无 AI 写作痕迹？（em-dash/en-dash, -ing phrases, 过度分段, 用词黑名单）
- 专有名词是否全部有定义？Abstract 中缩写是否展开？
- 过渡词使用是否自然？段落长度是否合理？
- 图表 caption 是否自包含？知识密度是否足够？

### 4. Related Work Positioning
- 文献调研是否充分？有无遗漏的重要相关工作？
- 与 MBR decoding、structured prediction 文献的定位是否清晰？
- 引用密度是否匹配 EMNLP 近年录用论文？

### 5. 格式与投稿规范
- ACL style 是否正确使用？
- Limitations section 是否充分？
- Responsible NLP Checklist 是否认真填写？

请按以下结构输出审稿报告：
1. Summary (2-3句)
2. Strengths (逐条)
3. Weaknesses (逐条，标注 severity: critical/warning/info)
4. Questions for Authors
5. Missing References (如有)
6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)
7. Detailed Comments (逐 section)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1899 · 2026-05-19T06:10:20.180351+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1900 · 2026-05-19T06:10:20.180791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1901 · 2026-05-19T06:10:23.758903+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool call

_source line 1902 · 2026-05-19T06:10:23.759386+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 1903 · 2026-05-19T06:10:24.615267+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 1904 · 2026-05-19T06:10:24.615720+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1905 · 2026-05-19T06:10:24.615969+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-19T06:10:24.817014+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool result

_source line 1907 · 2026-05-19T06:10:29.335370+00:00_

Web search results for query: "EMNLP 2026 submission guidelines author instructions page limit"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Information For Authors | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/information/authors"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the EMNLP 2026 submission guidelines regarding page limits:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

For the Industry Track specifically, authors are invited to submit original, full-length (maximum of 6 pages) industry track papers.

## Additional Requirements

Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations", which should be included at the end of the paper, before the references, and it will not count toward the page limit.

Submissions that exceed the length requirements, or are missing a limit
…[truncated 141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4518
}
```

</details>

---


### Tool result

_source line 1908 · 2026-05-19T06:10:35.310996+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about ACL Rolling Review 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

The suggested workflow is to (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel that you are qualified to review some aspects of the paper but not others (e.g. experimental results but not the formal proofs), please state in the review if you did not check some major parts, such as p
…[truncated 1315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10695
}
```

</details>

---


### Tool call

_source line 1909 · 2026-05-19T06:10:39.600543+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1910 · 2026-05-19T06:10:40.052574+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1911 · 2026-05-19T06:10:40.052989+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1912 · 2026-05-19T06:10:40.103499+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1913 · 2026-05-19T06:10:42.009480+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract all review form fields, their rating scales (1-5 or whatever scale), and descriptions. I need the complete list of dimensions reviewers must score, including soundness, excitement, reproducibility, etc. Return the complete form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract all review form fields, their rating scales (1-5 or whatever scale), and descriptions. I need the complete list of dimensions reviewers must score, including soundness, excitement, reproducibility, etc. Return the complete form structure."
  }
}
```

</details>

---


### Tool call

_source line 1914 · 2026-05-19T06:10:42.662534+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score papers, specific criteria for each dimension, and any special instructions. Return full details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score papers, specific criteria for each dimension, and any special instructions. Return full details."
  }
}
```

</details>

---


### Tool result

_source line 1915 · 2026-05-19T06:10:47.432821+00:00_

# ACL Rolling Review Form Structure

## Scoring Dimensions

### 1. **Reviewer Confidence**
- Scale: 1-5
- Description: "Positive that my evaluation is correct" (5) to "Not my area, or paper is very hard to understand" (1)

### 2. **Soundness**
- Scale: 1-5 (with .5 increments: 4.5, 3.5, 2.5, 1.5)
- Description: Evaluates whether the study is "sufficiently sound and thorough" with adequate support for claims

### 3. **Excitement**
- Scale: 1-5 (with .5 increments)
- Description: Subjective assessment of whether paper presents "conceptual breakthroughs" or challenges assumptions; ranges from "Highly Exciting" (5) to "Not Exciting" (1)

### 4. **Overall Assessment**
- Scale: 1-5 (with .5 increments)
- Description: Conference placement recommendation, ranging from "Consider for Award" (5) to "Do not resubmit" (1)

### 5. **Reproducibility**
- Scale: 1-5
- Description: Measures "enough information...for a reader to reproduce the main results"

### 6. **Datasets**
- Scale: 1-5
- Description: Evaluates value of released datasets, from "Enabling" (5) to "No usable datasets" (1)

### 7. **Software**
- Scale: 1-5
- Description: Assesses value of released code, from "Enabling" (5) to "No usable software" (1)

### 8. **Author Identity Knowledge**
- Scale: 1-5
- Description: Disclosure of potential author identification sources

## Qualitative Fields
- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Limitations and Societal Impact
- Ethical Concerns
- Best paper justification

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5423
}
```

</details>

---


### Tool result

_source line 1916 · 2026-05-19T06:10:54.122903+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Framework

ARR reviewers assess papers using three primary scores:

1. **Soundness**: Technical validity and methodological rigor. Scores must be justified by review content. Low soundness scores without identified faults indicate an unfaithful assessment.

2. **Excitement**: Personal interest in the work (subjective). This dimension remains orthogonal to soundness judgments.

3. **Overall Recommendation**: Composite assessment reflecting soundness, excitement, novelty, and potential impact for publication venues.

## What Reviewers Should Evaluate

**Expertise & Conflicts**: Determine qualification to review. Indicate if author identity is known and recuse yourself if serious conflicts exist.

**Appropriate Scope**: Verify the paper addresses "a research question and contributes new knowledge" within ARR/conference scope, using methodology aligned with disciplinary norms.

**Technical Soundness**: Check for "valid argumentation, proof validity, and sound methodology" during in-depth reading.

## Critical Guidelines for Strong Reviews

### Be Specific (Marked I1)
Replace vague criticisms ("missing references") with concrete details: "missing references XYZ" or "the formulation of X omits factor Y."

### Avoid Common Review Pitfalls (Marked I2, I10)
The guidelines identify seventeen heuristics reflecting unconscious bias:

- Dismissing findings as "unsurprising" despite lacking prior empirical validation (H1)
- Rejecting results contradicting your expectations (H2)
- Requiring novelty standards beyond conference scope (H3, H4)
- Expecting SOTA results when not claimed (H5)
- Devaluing negative results (H6)
- Criticizing methodological simplicity (H7)
- Imposing preferred methodologies on interdisciplinary work (H8)
- Penalizing niche topics or non-English languages (H9, H10)

### Check Paper-Specific Issues
Monitor for common NLP problems: LLM-only evaluation without validation (M1), reproducibility gaps (M2), und
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 11460
}
```

</details>

---


### Tool call

_source line 1917 · 2026-05-19T06:10:59.043260+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
  "description": "Find paper tex and bib files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
    "description": "Find paper tex and bib files"
  }
}
```

</details>

---


### Tool result

_source line 1918 · 2026-05-19T06:10:59.194559+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1919 · 2026-05-19T06:11:01.954044+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1920 · 2026-05-19T06:11:02.406624+00:00_

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
21	\title{Strong Predictors, Weak Selectors:\\ Diagnosing and Resolving Self-Consistency for Named Entity Recognition}
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
46	\section*{Responsible NLP Research Checklist}
47	\input{sections/checklist}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1921 · 2026-05-19T06:11:02.407017+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1922 · 2026-05-19T06:11:02.858458+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose two causes: instance degeneracy and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
7	The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1923 · 2026-05-19T06:11:02.858809+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1924 · 2026-05-19T06:11:03.761889+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low inst
…[truncated 4606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1925 · 2026-05-19T06:11:03.762291+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1926 · 2026-05-19T06:11:04.263846+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity.
14	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, sch
…[truncated 1966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1927 · 2026-05-19T06:11:04.264225+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1928 · 2026-05-19T06:11:04.766090+00:00_

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
11	Throughout, entity matching uses exact span and type match (a predicted entity is correct iff its character offsets and type label both match a gold entity).
12	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
13	
14	\paragraph{Log-probability (model-internal, per-sample).}
15	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
16	\begin{equation}\label{eq:logprob}
17	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
18	\end{equation}
19	
20	\paragraph{Exact match voting (surface, instance-level).}
21	The proportion of samples producing the most common output:
22	\begin{equation}\label{eq:em}
23	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
24	\end{equation}
25	
26	\paragraph{Fleiss' $\kappa$ (surface, insta
…[truncated 4000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1929 · 2026-05-19T06:11:04.766517+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1930 · 2026-05-19T06:11:05.218165+00:00_

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
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\topr
…[truncated 16694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1931 · 2026-05-19T06:11:05.218532+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1932 · 2026-05-19T06:11:05.669889+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Two factors constrain selection: instance degeneracy (17.8--48.4\%) eliminates headroom, and LP compression (within-instance $\rho$ 0.262--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$, surviving Bonferroni across 5 signals; Table~\ref{tab:nontied_main}). However, $\varepsilon{=}0.05$ is selected post-hoc from a 7-point sweep (Appendix~\ref{app:epsilon_robustness}); joint correction across thresholds and signals yields $p_{\text{adj}}{=}0.14$, so this finding is exploratory evidence for LP compression's role in the selection bottleneck.
6	Temperature disentangles the two factors: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5--0.7; Table~\ref{tab:t_degeneracy}); degeneracy rises with model scale and training convergence (Tables~\ref{tab:scale_ablation}, \ref{tab:epoch_confound}), so the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms ($+1.40$\,pp Few-NERD, $+1.02$\,pp SciERC, multi-seed mean; Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}).
11	Our negative results are specific to fine-tuned models with constrained decoding; settings with greater outp
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1933 · 2026-05-19T06:11:05.670450+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1934 · 2026-05-19T06:11:06.171866+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
4	Instance-level selection fails due to degeneracy and LP compression, but the diagnostic naturally motivates entity-level construction, adapting entity voting to stochastic sampling: LP-weighted aggregation yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$).
5	Construction and LP selection are complementary on two informative datasets (SciERC and Few-NERD; CoNLL operates in a ceiling regime), governed by LP-quality alignment.
6	For practitioners: use QE-based selective prediction when deployment requires reliability guarantees; apply entity construction when multi-sample generation is feasible; assess LP-alignment via held-out validation to choose between construction and LP selection.
7	As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1935 · 2026-05-19T06:11:06.172242+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1936 · 2026-05-19T06:11:07.075392+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
3	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app
…[truncated 1951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1937 · 2026-05-19T06:11:07.075984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1938 · 2026-05-19T06:11:07.578308+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1939 · 2026-05-19T06:11:07.578727+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1940 · 2026-05-19T06:11:07.879602+00:00_

File content (41711 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 300
}
```

</details>

---


### Tool call

_source line 1941 · 2026-05-19T06:11:07.930212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1942 · 2026-05-19T06:11:08.231840+00:00_

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
…[truncated 32874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1943 · 2026-05-19T06:11:14.623790+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1944 · 2026-05-19T06:11:15.026294+00:00_

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
…[truncated 39844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1945 · 2026-05-19T06:11:20.444738+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1946 · 2026-05-19T06:11:20.746647+00:00_

500	\end{tabular}
501	\end{table}
502	
503	\section{Training Configuration}\label{app:training}
504	
505	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
506	
507	\begin{table}[t]
508	\centering
509	\small
510	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
511	\label{tab:training}
512	\begin{tabular}{ll}
513	\toprule
514	Parameter & Value \\
515	\midrule
516	LoRA rank / $\alpha$ & 32 / 64 \\
517	LoRA target & All linear modules \\
518	LoRA dropout & 0 \\
519	Optimizer & AdamW \\
520	Learning rate & 2e-4, cosine schedule \\
521	Warmup ratio & 0.1 \\
522	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
523	Epochs & 5 \\
524	Max sequence length & 2048 \\
525	Precision & bf16 \\
526	Gradient checkpointing & Enabled \\
527	Max gradient norm & 1.0 \\
528	Training seed & 42 \\
529	Framework & LLaMA Factory \\
530	\midrule
531	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
532	SciERC split & 1861 / 275 / 551 \\
533	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
534	& eval\_steps${=}$200, save\_limit${=}$5 \\
535	\bottomrule
536	\end{tabular}
537	\end{table}
538	
539	\paragraph{Prompt template.}
540	For NER, we use a structured prompt:
541	\begin{quote}
542	\small
543	\texttt{System:} You are an expert in Named Entity Recognition.\\
544	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
545	Text: \texttt{\{input\_text\}}\\
546	Entity types: \texttt{\{schema\_types\}}
547	\end{quote}
548	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
549	
550	\paragraph{Constrained decoding.}
551	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schem
…[truncated 29458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1947 · 2026-05-19T06:11:25.176615+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1948 · 2026-05-19T06:11:25.428633+00:00_

1000	\toprule
1001	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
1002	\midrule
1003	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1004	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
1005	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1006	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1007	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1008	\bottomrule
1009	\end{tabular}
1010	\end{table}
1011	
1012	\begin{table}[t]
1013	\centering
1014	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
1015	\label{tab:sigma-comparison}
1016	\small
1017	\begin{tabular}{l cc cc}
1018	\toprule
1019	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
1020	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1021	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
1022	\midrule
1023	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
1024	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
1025	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
1026	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
1027	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
1028	\midrule
1029	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
1030	\bottomrule
1031	\end{tabular}
1032	\end{table}
1033	
1034	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
1035	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER); additional samples stabilize structural signals more than LP.
1036	
1037	\paragraph{$N$-scalin
…[truncated 36717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1949 · 2026-05-19T06:11:30.649611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1500",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1500",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1950 · 2026-05-19T06:11:30.650044+00:00_

1500	Despite stronger correlation ($+$48\%) and higher AUROC, entity-token LP produces worse selection, reinforcing that compression operates at the representation level rather than token aggregation: the correlation-selection gap persists even with a more targeted signal.
1501	
1502	\subsection{Entity-Level Majority Voting}\label{app:entity_merge}
1503	
1504	Entity-level majority voting constructs a merged output by including all (text, type) entity tuples that appear in at least $k$ of $N$ samples (with $k = N/2$ as the default majority threshold).
1505	Unlike best-of-$N$ selection (which picks one complete sample), merge combines evidence across samples at entity granularity.
1506	We sweep $k \in \{2, 3, \ldots, 8\}$ on each dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$) and report the best threshold per dataset.
1507	
1508	\begin{table}[h]
1509	\centering
1510	\small
1511	\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \in \{2, \ldots, 8\}$. ``$\Delta$'': merge F1 minus greedy. ``Recovery'': $\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}
1512	\label{tab:entity_merge}
1513	\begin{tabular}{lcccc}
1514	\toprule
1515	Dataset & Greedy & Best merge ($k^*$) & $\Delta$ (pp) & Recovery (\%) \\
1516	\midrule
1517	SciERC & 0.644 & 0.660 ($k{=}3$) & $+$1.57 & $+$11.9 \\
1518	CoNLL & 0.907 & 0.903 ($k{=}3$) & $-$0.38 & $-$9.0 \\
1519	Few-NERD & 0.748 & 0.744 ($k{=}2$) & $-$0.43 & $-$3.6 \\
1520	\bottomrule
1521	\end{tabular}
1522	\end{table}
1523	
1524	On degenerate subsets (instances where all $N$ samples yield identical F1), merge is uniformly negative across all three datasets, confirming that entity-level aggregation cannot bypass the diversity bottleneck identified in the main text (\S\ref{sec:discussion}).
1525	
1526	\subsection{Entity Construction Threshold Sensitivity}
1527	\label{app:theta_
…[truncated 2382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1951 · 2026-05-19T06:11:36.222085+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1952 · 2026-05-19T06:11:36.673668+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1953 · 2026-05-19T06:11:37.175512+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1954 · 2026-05-19T06:11:37.627223+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1955 · 2026-05-19T06:11:38.121603+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1956 · 2026-05-19T06:11:39.175879+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:5:Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:14:Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:19:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:127:Under standard early stopping, Few-NERD degeneracy is 13.8\% and LP achieves $+1.39$~pp ($p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp); LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:9:We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref
…[truncated 3176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1957 · 2026-05-19T06:11:40.079441+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(Furthermore|Moreover|Additionally|Notably|delve|leverage|utilize|facilitate|myriad|plethora)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(Furthermore|Moreover|Additionally|Notably|delve|leverage|utilize|facilitate|myriad|plethora)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 1958 · 2026-05-19T06:11:40.482071+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1959 · 2026-05-19T06:11:40.683062+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 1960 · 2026-05-19T06:13:04.773888+00:00_

&lt;persisted-output>
Output too large (64KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/a85943c3-a133-450f-957a-65d14343e34a/tool-results/toolu_01XhnyBrBznz5u65pyXmBQwA.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 78, \"total_citations\": 111, \"unique_cited_keys\": 70, \"orphan_bib\": 8, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 69, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"eisenstein2023helping\", \"kamath2020selective\", \"li2025llms\", \"muennighoff2025s1\", \"naderi2021ensemble\", \"sarcinelli2025local\", \"wiher2022decoding\", \"xie2023zeroshot\"], \"missing_bib\": [], \"orphan_count\": 8, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"ti
…[truncated 361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 84090
}
```

</details>

---


### Tool call

_source line 1961 · 2026-05-19T06:13:08.735838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/a85943c3-a133-450f-957a-65d14343e34a/tool-results/toolu_01XhnyBrBznz5u65pyXmBQwA.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/a85943c3-a133-450f-957a-65d14343e34a/tool-results/toolu_01XhnyBrBznz5u65pyXmBQwA.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1962 · 2026-05-19T06:13:09.038337+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 78, \"total_citations\": 111, \"unique_cited_keys\": 70, \"orphan_bib\": 8, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 69, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"eisenstein2023helping\", \"kamath2020selective\", \"li2025llms\", \"muennighoff2025s1\", \"naderi2021ensemble\", \"sarcinelli2025local\", \"wiher2022decoding\", \"xie2023zeroshot\"], \"missing_bib\": [], \"orphan_count\": 8, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal 
…[truncated 63559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1963 · 2026-05-19T06:16:47.459305+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告 — Round 1\n\n**论文**: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)\n**审查侧重**: 新颖性 + 叙事完整性 + 写作质量 + Related Work positioning\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Borderline)\n**一句话总结**: 实验扎实、诊断细致的 empirical study，但核心新颖性有限，positive contribution（entity construction）增量小且源自已知技术的直接迁移，负结果虽有价值但主线在 diagnostic 与 prescriptive 之间摇摆。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨、统计方法充分（bootstrap CI, MDE, TOST, 多种校正），但几个核心发现依赖 post-hoc 分析（ε=0.05），confound（thinking token）虽被 address 但增加了不确定性 |\n| Excitement | 2.5/5 | 诊断有价值但结论部分可预测（instance-level 信号无法 within-instance 选择几乎是 by construction）；positive contribution 增量小（~1pp），对领域推进有限 |\n| Reproducibility | 4.0/5 | 超参、prompt、训练配置详尽（Appendix Table 7），承诺代码开源，所有 benchmark 公开可用，多 seed 报告 |\n| Confidence | 4/5 | 本人熟悉 NER/IE、test-time scaling 和 MBR decoding 文献 |\n\n---\n\n## Strengths\n\n**S1. 统计严谨性超越同类工作。** 全文贯穿 paired bootstrap tests, MDE 分析, TOST 等价性检验, Bonferroni/BH 校正, 以及 multi-seed stability 报告。对 SciERC 的 MDE≈1.5pp 限制有明确声明（Section 4.3, footnote 6），这在 NLP 经验研究中很少见。\n\n**S2. 诊断框架清晰。** QE 与 selection 的显式分离（Section 3.1 的 per-sample vs. instance-level 信号分类）是有效的概念贡献。Expected selection gain decomposition 虽非严格推导，但在三个 dataset 上方向一致，具有启发性。\n\n**S3. 实验覆盖面广。** 4 个 NER benchmark 形成难度梯度（WNUT-17 signal collapse → SciERC medium → Few-NERD low degeneracy → CoNLL ceiling），各自承担明确的实验角色。附录约 1571 行，几乎每个可能的混淆因素都有 ablation。\n\n**S4. 诚实的负结果呈现。** 坦率承认 supervised combinations、hidden state probes、DeBERTa verifier 均无法关闭 selection gap，并清楚区分 exploratory 与 confirmatory findings。\n\n**S5. 写作质量整体良好。** 无 em-dash/en-dash AI 写作痕迹，无黑名单词汇。术语定义完整。段落长度合理，过渡自然。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **\"Correlation-selection gap\" 的新颖性存疑：instance-level 信号无法做 within-instance selection 是结构性事实，非实证发现。**\n- 具体位置：Section 3.1, Section 4.3\n- 4/5 个信号是 instance-level aggregate（\"assign identical scores to all N candidates\"），这是信号定义的直接结果——不需要实验验证。实际需要验证的只是 LP 的 selection 失败。LP 在 Few-NERD 成功、SciERC 失败的归因——\"LP-quality alignment\" 接近同义反复（LP 选得好当且仅当 LP 与 quality 对齐好）。\n- 建议：更清晰区分 by-construction 与 empirical findings。核心贡献聚焦 LP compression 量化（median 0.041 nats）、degeneracy-convergence 因果关系、跨 dataset alignment 差异。\n\n**N2** [critical] **Entity-level construction 本质是 Florian et al. (2003) entity voting 的直接应用，新颖性增量有限。**\n- 具体位置：Section 4.6, Introduction Contribution #3\n- 论文自承 \"adapting entity voting from ensemble NER to stochastic sampling\"。LP-weighted vs. uniform 差异仅 +0.3-0.7pp。对于 EMNLP Main，将已有技术的 threshold 从 majority 调整到 θ=2/N 加 LP weighting 不构成 significant contribution。\n- 建议：需 stochastic sampling + entity voting 与 multi-model ensemble + entity voting 的 direct comparison，或更深入的理论分析。\n\n**N3** [critical] **负结果的 scope 限制过强，削弱诊断贡献的 generalizability。**\n- 具体位置：Discussion Section 5, Limitations\n- 核心负结果仅在 fine-tuned 4B-8B + constrained decoding 下成立。Appendix free-form ablation 展示 RE LP selection 反转（-0.68pp → +1.69pp）。70B+/closed-source APIs 未测试。\n- 建议：至少需一个非 fine-tuned 设置的验证，或在 title/abstract 中更清楚限定 scope。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] SciERC n=529 作为 primary test bed 统计功效不足（MDE≈1.5pp），建议以 Few-NERD 为 primary。\n\n**W2** [warning] Expected selection gain decomposition 缺乏理论基础，仅有 3 个 data points 验证方向一致性。\n\n**W3** [warning] Gating protocol 仅在 3 个 easily separable dataset 上验证，不具备 practical robustness 证据。\n\n**W4** [warning] Related Work 偏短（~1 column），缺少与 Taubenfeld/Kang 的技术差异对比，Li et al. 2025 在 bib 中但未 cite。\n\n**W5** [warning] Greedy F1 在不同 table 中出现 4 个值（0.640-0.650），虽有解释但反映 protocol 不统一。\n\n---\n\n## 小问题\n\n- M1: Abstract \"LP\" 首次出现未展开\n- M2: \\textendash 在 abstract/limitations 中使用，确认 ACL style 兼容性\n- M3: 8 个 orphan bib entries 应清理\n- M4: Table 2 中 EM/VC 的 p 值标 \"---\" 但应标注具体值（它们低于 greedy）\n- M5: Checklist E1 AI assistant 声明过于笼统\n\n---\n\n## Questions for Authors\n\nQ1. Table 4 的 cross-instance LP ρ (0.220) 与 Appendix Table 12 的 within-instance ρ (0.667) 差异巨大，请澄清为何 cross-instance ρ 不能预测 selection 而 within-instance ρ 可以。\n\nQ2. Entity construction 在 CoNLL 上降低 F1 (-0.39pp)。如果 gating 将 CoNLL 路由到 construction（dev ρ=0.065 < 0.3），是否 cause harm？\n\nQ3. Free-form decoding 使 RE LP selection 反转但 NER 不变，这是否说明 constrained decoding 是 failure 的根本原因？\n\nQ4. 是否测试过 Self-Certainty (Kang et al. 2025) 或 P(True)？这些 per-sample signals 的缺失是否削弱 \"no per-sample signal works\" 的结论？\n\n---\n\n## Missing References\n\n- Li et al. (2025) \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\"——在 bib 中但未 cite\n- Lafferty et al. (2001) CRF——structured prediction confidence 的经典基础\n- Muennighoff et al. (2025) s1——在 bib 中但未 cite\n\n---\n\n## Overall Assessment\n\n**3.0 / 5 — Borderline**，置信度 4/5\n\n论文的 strength 在于实验严谨性和诚实的负结果呈现。但三个 critical 问题共同削弱了 EMNLP Main 的 case：(1) 核心概念新颖性不足（\"correlation-selection gap\" 部分 by construction）；(2) positive contribution 增量过小（entity voting 的直接迁移，~1pp gains）；(3) scope 限制严重（结论可能是 fine-tuned + constrained decoding setup 的 artifact）。\n\n如果 sharpen novelty framing（聚焦 LP compression + alignment 作为独立发现），增加非 fine-tuned 验证，并对 entity construction 与 ensemble voting 做 direct comparison，可升至 weak accept。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告 — Round 1\n\n**论文**: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)\n**审查侧重**: 新颖性 + 叙事完整性 + 写作质量 + Related Work positioning\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Borderline)\n**一句话总结**: 实验扎实、诊断细致的 empirical study，但核心新颖性有限，positive contribution（entity construction）增量小且源自已知技术的直接迁移，负结果虽有价值但主线在 diagnostic 与 prescriptive 之间摇摆。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨、统计方法充分（bootstrap CI, MDE, TOST, 多种校正），但几个核心发现依赖 post-hoc 分析（ε=0.05），confound（thinking token）虽被 address 但增加了不确定性 |\n| Excitement | 2.5/5 | 诊断有价值但结论部分可预测（instance-level 信号无法 within-instance 选择几乎是 by construction）；positive contribution 增量小（~1pp），对领域推进有限 |\n| Reproducibility | 4.0/5 | 超参、prompt、训练配置详尽（Appendix Table 7），承诺代码开源，所有 benchmark 公开可用，多 seed 报告 |\n| Confidence | 4/5 | 本人熟悉 NER/IE、test-time scaling 和 MBR decoding 文献 |\n\n---\n\n## Strengths\n\n**S1. 统计严谨性超越同类工作。** 全文贯穿 paired bootstrap tests, MDE 分析, TOST 等价性检验, Bonferroni/BH 校正, 以及 multi-seed stability 报告。对 SciERC 的 MDE≈1.5pp 限制有明确声明（Section 4.3, footnote 6），这在 NLP 经验研究中很少见。\n\n**S2. 诊断框架清晰。** QE 与 selection 的显式分离（Section 3.1 的 per-sample vs. instance-level 信号分类）是有效的概念贡献。Expected selection gain decomposition 虽非严格推导，但在三个 dataset 上方向一致，具有启发性。\n\n**S3. 实验覆盖面广。** 4 个 NER benchmark 形成难度梯度（WNUT-17 signal collapse → SciERC medium → Few-NERD low degeneracy → CoNLL ceiling），各自承担明确的实验角色。附录约 1571 行，几乎每个可能的混淆因素都有 ablation。\n\n**S4. 诚实的负结果呈现。** 坦率承认 supervised combinations、hidden state probes、DeBERTa verifier 均无法关闭 selection gap，并清楚区分 exploratory 与 confirmatory findings。\n\n**S5. 写作质量整体良好。** 无 em-dash/en-dash AI 写作痕迹，无黑名单词汇。术语定义完整。段落长度合理，过渡自然。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **\"Correlation-selection gap\" 的新颖性存疑：instance-level 信号无法做 within-instance selection 是结构性事实，非实证发现。**\n- 具体位置：Section 3.1, Section 4.3\n- 4/5 个信号是 instance-level aggregate（\"assign identical scores to all N candidates\"），这是信号定义的直接结果——不需要实验验证。实际需要验证的只是 LP 的 selection 失败。LP 在 Few-NERD 成功、SciERC 失败的归因——\"LP-quality alignment\" 接近同义反复（LP 选得好当且仅当 LP 与 quality 对齐好）。\n- 建议：更清晰区分 by-construction 与 empirical findings。核心贡献聚焦 LP compression 量化（median 0.041 nats）、degeneracy-convergence 因果关系、跨 dataset alignment 差异。\n\n**N2** [critical] **Entity-level construction 本质是 Florian et al. (2003) entity voting 的直接应用，新颖性增量有限。**\n- 具体位置：Section 4.6, Introduction Contribution #3\n- 论文自承 \"adapting entity voting from ensemble NER to stochastic sampling\"。LP-weighted vs. uniform 差异仅 +0.3-0.7pp。对于 EMNLP Main，将已有技术的 threshold 从 majority 调整到 θ=2/N 加 LP weighting 不构成 significant contribution。\n- 建议：需 stochastic sampling + entity voting 与 multi-model ensemble + entity voting 的 direct comparison，或更深入的理论分析。\n\n**N3** [critical] **负结果的 scope 限制过强，削弱诊断贡献的 generalizability。**\n- 具体位置：Discussion Section 5, Limitations\n- 核心负结果仅在 fine-tuned 4B-8B + constrained decoding 下成立。Appendix free-form ablation 展示 RE LP selection 反转（-0.68pp → +1.69pp）。70B+/closed-source APIs 未测试。\n- 建议：至少需一个非 fine-tuned 设置的验证，或在 title/abstract 中更清楚限定 scope。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] SciERC n=529 作为 primary test bed 统计功效不足（MDE≈1.5pp），建议以 Few-NERD 为 primary。\n\n**W2** [warning] Expected selection gain decomposition 缺乏理论基础，仅有 3 个 data points 验证方向一致性。\n\n**W3** [warning] Gating protocol 仅在 3 个 easily separable dataset 上验证，不具备 practical robustness 证据。\n\n**W4** [warning] Related Work 偏短（~1 column），缺少与 Taubenfeld/Kang 的技术差异对比，Li et al. 2025 在 bib 中但未 cite。\n\n**W5** [warning] Greedy F1 在不同 table 中出现 4 个值（0.640-0.650），虽有解释但反映 protocol 不统一。\n\n---\n\n## 小问题\n\n- M1: Abstract \"LP\" 首次出现未展开\n- M2: \\textendash 在 abstract/limitations 中使用，确认 ACL style 兼容性\n- M3: 8 个 orphan bib entries 应清理\n- M4: Table 2 中 EM/VC 的 p 值标 \"---\" 但应标注具体值（它们低于 greedy）\n- M5: Checklist E1 AI assistant 声明过于笼统\n\n---\n\n## Questions for Authors\n\nQ1. Table 4 的 cross-instance LP ρ (0.220) 与 Appendix Table 12 的 within-instance ρ (0.667) 差异巨大，请澄清为何 cross-instance ρ 不能预测 selection 而 within-instance ρ 可以。\n\nQ2. Entity construction 在 CoNLL 上降低 F1 (-0.39pp)。如果 gating 将 CoNLL 路由到 construction（dev ρ=0.065 < 0.3），是否 cause harm？\n\nQ3. Free-form decoding 使 RE LP selection 反转但 NER 不变，这是否说明 constrained decoding 是 failure 的根本原因？\n\nQ4. 是否测试过 Self-Certainty (Kang et al. 2025) 或 P(True)？这些 per-sample signals 的缺失是否削弱 \"no per-sample signal works\" 的结论？\n\n---\n\n## Missing References\n\n- Li et al. (2025) \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\"——在 bib 中但未 cite\n- Lafferty et al. (2001) CRF——structured prediction confidence 的经典基础\n- Muennighoff et al. (2025) s1——在 bib 中但未 cite\n\n---\n\n## Overall Assessment\n\n**3.0 / 5 — Borderline**，置信度 4/5\n\n论文的 strength 在于实验严谨性和诚实的负结果呈现。但三个 critical 问题共同削弱了 EMNLP Main 的 case：(1) 核心概念新颖性不足（\"correlation-selection gap\" 部分 by construction）；(2) positive contribution 增量过小（entity voting 的直接迁移，~1pp gains）；(3) scope 限制严重（结论可能是 fine-tuned + constrained decoding setup 的 artifact）。\n\n如果 sharpen novelty framing（聚焦 LP compression + alignment 作为独立发现），增加非 fine-tuned 验证，并对 entity construction 与 ensemble voting 做 direct comparison，可升至 weak accept。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1964 · 2026-05-19T06:16:52.797682+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5338
}
```

</details>

---


### Assistant

_source line 1965 · 2026-05-19T06:17:02.053711+00:00_

审稿报告已提交给 Review Director。

**核心结论**：Overall 3.0/5 (Borderline)。三个 critical 问题：

1. **"Correlation-selection gap" 新颖性有限**——4/5 信号的 selection 失败是信号定义的直接结果（它们 by construction 对同一 input 的所有 sample 给相同分数），不是 empirical discovery。真正的 empirical contribution（LP compression、degeneracy-convergence 因果关系）被 umbrella term 模糊了。

2. **Entity construction 增量过小**——+1.0-1.4pp 来自 Florian et al. (2003) entity voting 的直接迁移加 LP weighting，对 EMNLP Main 方法贡献不够。

3. **Scope 太窄**——负结果仅限于 fine-tuned 4B-8B + constrained decoding，论文自身的 free-form ablation 已展示 RE 方向反转，暗示结论可能是 setup-specific。

写作质量方面无 AI 写作痕迹，统计处理在 NLP 论文中属于上乘水平，这是论文的主要优势。引用核查通过（78 entries, 69 verified, 8 orphan 应清理）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 50

## Round 50

4 recorded events


### User

_source line 1966 · 2026-05-19T06:19:04.099314+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿报告 — Round 1

**Overall**: 3.5/5 (Borderline accept, 倾向 Findings)

### Strengths
S1. 问题形式化清晰且重要（QE vs selection, instance-level vs per-sample 分类法）。
S2. 实验覆盖异常全面（5 signal × 4 datasets × 2 models × scale/temp/epoch/N ablations + supervised/hidden probe/DeBERTa/verbalized confidence/free-form/calibration/OOD）。
S3. 统计方法正确且透明度高（bootstrap CI, TOST, MDE, 多重比较标注）。
S4. Negative results 诚实报告。
S5. 混淆变量控制充分（thinking token, epoch, SJ normalizer, FK independence, length-LP）。

### Must-Fix (Critical)
N1. 核心分解公式 E[ΔF1] ≈ (1-d)·Δ_oracle·g(ρ_within) 是 underdetermined 启发式：g 无理论推导，仅 3 data points "验证"。23 个 configurations (Fig 3) 的数据未用于验证分解公式预测精度。
N2. Within-instance ρ(LP, F1) 作为因果预测因子具有循环性：需 gold labels 才能计算，仅为回顾性诊断。Gating protocol (50 instances, threshold 0.3) 验证不足：(a) bootstrap SE 未报告；(b) 仅 3 dataset with large margins；(c) 0.3 threshold 来源不明。

### Should-Fix (Warning)
W1. "Tuning-free" threshold 不准确：θ=2/N 是观察所有数据集后选择的，非先验原则。
W2. Entity construction 的 "Resolving" framing 过强：实际仅恢复 8-11% oracle headroom。
W3. SciERC Thinking Token Confound：无意引入的训练-推理不一致，应在正文中明确声明。
W4. 3 seeds 统计功效有限：SciERC LP selection σ=0.48pp ≈ effect size 本身。
W5. English-only + NER-heavy 泛化局限未讨论语言覆盖。

### Minor
M1-M5: F1 metric 用法不一致, Table 3 单 seed 误导, orphan bib, "as a reviewer correctly noted" 措辞, Figure 1 caption ρ up to 0.45 来源。

### Questions
Q1. 分解公式能否在 23 configurations 上做回归验证？Predicted vs actual gain 相关性？
Q2. Gating 的 50 instances 选择方式？Bootstrap CI？Threshold 0.3 敏感性？
Q3. Degeneracy rises with capability (8B>4B) 是否因 convergence 差异？有无 matched-convergence 对比？
Q4. Entity construction precision-recall trade-off 数据？
Q5. Constrained decoding + post-hoc parsing 是否有更多 headroom？Task asymmetry (NER vs RE) 解释？

### Missing References
- Jiang et al. (2023) LLM-Blender
- Ravaut et al. (2022) SummaReranker

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1967 · 2026-05-19T06:20:53.397293+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n### Strengths\n- [AGREE] R1-S1 到 R1-S5：全部同意。与我的独立评价一致。补充：S1 中 instance-level vs per-sample 分类有效，但 instance-level 信号不能做 within-instance selection 是分类法的直接推论（by construction）。\n\n### Must-Fix\n- [AGREE] R1-N1：分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 确实 underdetermined。补充：23 configurations（Figure 3）的数据完全可以做 predicted vs actual 的回归验证但论文未做，是明显遗漏。g(·) 无函数形式使得验证不可能。\n- [AGREE] R1-N2：within-instance ρ(LP,F1) 需 gold labels，仅为回顾性诊断——比我对 gating 的评价（仅指出 margin 过大）更本质。Gating 的 50 instances 无 bootstrap SE、0.3 threshold 来源不明、仅 3 dataset trivially separable。\n\n### Should-Fix\n- [AGREE] R1-W1：\"Tuning-free\" 不准确。Appendix Table 25 的 θ sweep 说明 θ=2/N 是 post-hoc observation。\n- [AGREE] R1-W2：\"Resolving\" framing 过强。Entity construction 仅恢复 7.8-11.3% oracle headroom。我在 N2 中从新颖性角度提出了同样关切。\n- [REBUT] R1-W3：Thinking token confound 的严重程度被高估。Appendix F 三方面论证（LP shift 仅 2.68% of range, constant prefix cancellation, CoNLL 控制组反驳假说）组合起来有说服力。已在 footnote 和 Limitations 中提及。\n- [AGREE] R1-W4：3 seeds 功效有限，但 Few-NERD σ=0.04pp（50× more stable），关键 positive result 是 robust 的。\n- [AGREE] R1-W5：English-only 泛化局限未在 Limitations 中讨论，是遗漏。\n\n### Minor\n- [AGREE] R1-M1/M2/M3/M5：F1 用法不一致、Table 3 单 seed、orphan bib、Figure 1 caption ρ 近似值。\n- [REBUT] R1-M4：\"as a reviewer correctly noted\" 如果是首次提交则应删除，但这是措辞问题非实质问题。\n\n### Questions\n- [AGREE] R1-Q1/Q2/Q3/Q5：分解公式定量验证、gating 细节、matched-convergence、task asymmetry 解释均合理。\n- [REBUT] R1-Q4：论文已说明 construction 是 recall-driven（Section 4.6 line 211），P/R 表是合理但非 critical 的补充。\n\n### Missing References\n- [AGREE] LLM-Blender (Jiang et al. 2023) 是 significant omission——output fusion pipeline 直接相关。\n- [REBUT] SummaReranker (Ravaut et al. 2022) 相关性较弱，论文已有 learned verifier 引用覆盖。\n\n### 综合\nR1 给 3.5/5 倾向 Findings，我给 3.0/5 Borderline。核心分歧不大。R1 在分解公式和 gating 循环性上的分析比我更深入。我比 R1 更关切 entity construction 新颖性和 scope 限制。维持 3.0/5，如定位为 Findings 可接受 3.5。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n### Strengths\n- [AGREE] R1-S1 到 R1-S5：全部同意。与我的独立评价一致。补充：S1 中 instance-level vs per-sample 分类有效，但 instance-level 信号不能做 within-instance selection 是分类法的直接推论（by construction）。\n\n### Must-Fix\n- [AGREE] R1-N1：分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 确实 underdetermined。补充：23 configurations（Figure 3）的数据完全可以做 predicted vs actual 的回归验证但论文未做，是明显遗漏。g(·) 无函数形式使得验证不可能。\n- [AGREE] R1-N2：within-instance ρ(LP,F1) 需 gold labels，仅为回顾性诊断——比我对 gating 的评价（仅指出 margin 过大）更本质。Gating 的 50 instances 无 bootstrap SE、0.3 threshold 来源不明、仅 3 dataset trivially separable。\n\n### Should-Fix\n- [AGREE] R1-W1：\"Tuning-free\" 不准确。Appendix Table 25 的 θ sweep 说明 θ=2/N 是 post-hoc observation。\n- [AGREE] R1-W2：\"Resolving\" framing 过强。Entity construction 仅恢复 7.8-11.3% oracle headroom。我在 N2 中从新颖性角度提出了同样关切。\n- [REBUT] R1-W3：Thinking token confound 的严重程度被高估。Appendix F 三方面论证（LP shift 仅 2.68% of range, constant prefix cancellation, CoNLL 控制组反驳假说）组合起来有说服力。已在 footnote 和 Limitations 中提及。\n- [AGREE] R1-W4：3 seeds 功效有限，但 Few-NERD σ=0.04pp（50× more stable），关键 positive result 是 robust 的。\n- [AGREE] R1-W5：English-only 泛化局限未在 Limitations 中讨论，是遗漏。\n\n### Minor\n- [AGREE] R1-M1/M2/M3/M5：F1 用法不一致、Table 3 单 seed、orphan bib、Figure 1 caption ρ 近似值。\n- [REBUT] R1-M4：\"as a reviewer correctly noted\" 如果是首次提交则应删除，但这是措辞问题非实质问题。\n\n### Questions\n- [AGREE] R1-Q1/Q2/Q3/Q5：分解公式定量验证、gating 细节、matched-convergence、task asymmetry 解释均合理。\n- [REBUT] R1-Q4：论文已说明 construction 是 recall-driven（Section 4.6 line 211），P/R 表是合理但非 critical 的补充。\n\n### Missing References\n- [AGREE] LLM-Blender (Jiang et al. 2023) 是 significant omission——output fusion pipeline 直接相关。\n- [REBUT] SummaReranker (Ravaut et al. 2022) 相关性较弱，论文已有 learned verifier 引用覆盖。\n\n### 综合\nR1 给 3.5/5 倾向 Findings，我给 3.0/5 Borderline。核心分歧不大。R1 在分解公式和 gating 循环性上的分析比我更深入。我比 R1 更关切 entity construction 新颖性和 scope 限制。维持 3.0/5，如定位为 Findings 可接受 3.5。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1968 · 2026-05-19T06:20:57.624520+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4227
}
```

</details>

---


### Assistant

_source line 1969 · 2026-05-19T06:21:03.640685+00:00_

交叉回应已提交。

核心判断：与 R1 在大部分问题上 converge。R1 的分解公式批评（N1）和 gating 循环性分析（N2）比我更具体，我在 entity construction 新颖性和 scope 限制上比 R1 更严格。在 thinking token confound（W3）和 SummaReranker 引用上有分歧，均非重大分歧。两人评分差距 0.5 分（3.0 vs 3.5），如定位 Findings 可 converge 到 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 51

## Round 51

166 recorded events
