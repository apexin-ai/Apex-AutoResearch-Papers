# analysis d112 claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_analysis_d112_claim_audit_20260516T094502.jsonl`
- **Structured JSON:** [`3b747ee39f5b2efe50f8.json`](../../sessions/3b/3b747ee39f5b2efe50f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-16T09:53:10.647522+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T09:53:10.647891+00:00_

docs/paper/sections/appendix.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/sections/limitations.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/discussion.tex
docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T09:53:10.648059+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T09:53:10.648350+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---on a medium-difficulty benchmark (SciERC) with ceiling-effect (CoNLL) and signal-collapse (WNUT-17) controls, within a narrow model-scale range (4B--8B).
4	All signals achieve moderate quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control), yet best-of-$N$ selection fails to outperform greedy decoding ($T{=}0$)---the \textit{correlation-selection gap}.
5	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats, with entity-token isolation revealing intrinsic overconfidence rather than format-token dilution.
6	A five-layer ablation chain (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding.
7	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T09:53:10.648562+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:53:10.648892+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing two failure mechanisms---instance degeneracy and LP compression---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	We define the \textbf{correlation-selection gap} as the disparity between a signal's rank correlation with F1 ($\rho$) and its ability to select the best output from $N$ candidates (Figure~\ref{fig:overview}): on SciERC, signals achieve moderate quality estimation ($\rho{=}0.38$, up to 0.45 on a ceiling-effect control) yet selection fails to improve over greedy decoding
…[truncated 3024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T09:53:10.649071+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:53:10.649280+00:00_

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
…[truncated 3040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T09:53:10.649437+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T09:53:10.649632+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
…[truncated 7949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T09:53:10.649784+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:53:10.649959+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	VC leads on medium-difficulty NER ($\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\ref{app:re_extension}.
6	
7	\paragraph{Why the gap exists.}
8	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
9	
10	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
11	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
12	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
13	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero---the tension between model quality and selection utility is inherent.
14	Scale ablation confirms this tension: Qwen3-8B shows 21\% instance degeneracy on SciERC vs.\ 10.4\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\rho{=}0.52$ vs.\ $0.55$; Table~\ref{tab:degeneracy}).
15	Despite MBR's success in machine translation \cite{freitag2022high}, all 
…[truncated 7276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T09:53:10.650113+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:53:10.650273+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate quality estimation ($\rho{=}0.38$ on medium-difficulty NER, up to 0.45 on a ceiling-effect control) coexists with selection that fails to outperform greedy decoding ($T{=}0$).
4	The gap stems from two mechanisms: instance degeneracy (21--58\% of instances produce identical F1 across all $N$ samples, scaling with model capability and eliminating selection headroom despite positive within-instance utility correlation) and LP compression (the only per-sample signal has median within-instance range of 0.041 nats).
5	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
6	The gap is demonstrated in the medium-difficulty regime where models achieve moderate but imperfect accuracy; signal rankings shift with difficulty and collapse at the capability boundary in the small-model regime (3B--8B).
7	Whether these mechanisms persist at 70B+ scales is an open question; trained verifiers and an exploratory extension to relation extraction (Appendix~\ref{app:re_extension}) are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T09:53:10.650410+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:53:10.650547+00:00_

1	Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.4$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selectio
…[truncated 207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T09:53:10.650698+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:53:10.650970+00:00_

File content (26138 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T09:53:10.651144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T09:53:10.651487+00:00_

1	paper:
2	  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence
3	    Signals for Test-Time Scaling in Information Extraction'
4	  version: 100
5	  generated_at: '2026-05-16T08:28:21.069996+00:00'
6	  source: manual provenance build by Paper Agent
7	claims:
8	- id: c001_voting_rho_scierc_ner
9	  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation
10	    artifact)
11	  sections:
12	  - abstract
13	  - introduction
14	  - experiments
15	  - conclusion
16	  - discussion
17	  - related_work
18	  tier: 1
19	  evidence:
20	  - exp_id: exp_012_rerun_1024
21	    metric: ner.voting_rho_full
22	    value: 0.379
23	  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected
24	    via exp_012_rerun_1024 (max_tokens=1024).
25	- id: c002_auroc_dissociation_scierc
26	  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while
27	    Voting leads ρ (NER 0.379, RE 0.422)
28	  sections:
29	  - abstract
30	  - introduction
31	  - experiments
32	  - conclusion
33	  - discussion
34	  tier: 1
35	  evidence:
36	  - exp_id: exp_012_rerun_1024
37	    metric: ner.em_auroc
38	    value: 0.749
39	  - exp_id: exp_012_rerun_1024
40	    metric: re.em_auroc
41	    value: 0.706
42	  - exp_id: exp_012_rerun_1024
43	    metric: ner.voting_auroc
44	    value: 0.684
45	  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected
46	    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline
47	    claim changed from "entity voting achieves ρ=0.38 and AUROC=0.74" to split ρ (Voting
48	    0.38) / AUROC (EM 0.75) claim.
49	- id: c003_sj_rho_scierc_ner
50	  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)
51	  sections:
52	  - experiments
53	  tier: 1
54	  evidence:
55	  - exp_id: exp_012_rerun_1024
56	    metric: ner.sj_rho_full
57	    value: 0.36
58	  - exp_id: exp_004_re_diagnostic
59	    metric: bootstrap_ci_95.ner_sj
60	   
…[truncated 28979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T09:53:10.651686+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
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

_source line 22 · 2026-05-16T09:53:10.652234+00:00_

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
…[truncated 37198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T09:53:10.652443+00:00_

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
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T09:53:10.652611+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	Our experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.
12	Degeneracy scales with model capability: CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero (\S\ref{sec:discussion}).
13	This creates an inherent tension between model quality and selection utility that we expect to intensify as models improve.
14	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
15	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence es
…[truncated 2303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T09:53:10.652790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "500"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T09:53:10.653114+00:00_

500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significa
…[truncated 32505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T09:53:10.653812+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit",
  "description": "Create audit output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit",
    "description": "Create audit output directory"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T09:53:10.654118+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T09:53:10.654312+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md",
  "content": "# Claim Audit Report: Numerical Consistency Check\n\n**Paper**: Strong Predictors, Weak Selectors  \n**Date**: 2026-05-16  \n**Scope**: All sections in `docs/paper/sections/` + `paper_provenance.yaml`\n\n---\n\n## Inconsistency List\n\n| # | Location 1 | Value 1 | Location 2 | Value 2 | Severity | Issue | Suggested Fix |\n|---|-----------|---------|-----------|---------|----------|-------|---------------|\n| 1 | discussion.tex:L43 | LP×VC best: +0.1pp over single-sample | limitations.tex:L10 | LP×VC: +0.4pp over greedy | **HIGH** | Mathematically contradictory. If best=single+0.1pp=0.646, then vs greedy (0.663)=-1.7pp, not +0.4pp. | Limitations should read \"+0.4pp over single-sample\" OR discussion value needs correction. Verify from exp data which is correct. |\n| 2 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | appendix.tex tab:multiseed (L419) | VC NER AUROC mean = .697±.010 | **HIGH** | Mathematically impossible: if seed=42 gives .663, population σ over 3 seeds cannot be .010 with mean .697 (seed=42 deviation alone = .034 > 3×σ). | Either Table 1 AUROC is not from seed=42, or multi-seed AUROC values are from a different eval protocol. Reconcile. |\n| 3 | paper_provenance.yaml c002 | EM NER AUROC = 0.749 | experiments.tex Table 1 (L37) | EM SciERC AUROC = .614 | **HIGH** | Provenance claims EM leads AUROC at 0.749; published Table 1 shows EM=.614, VC leads at .663. Provenance narrative contradicts paper. | Update provenance to match final Table 1 values. |\n| 4 | paper_provenance.yaml c013 | greedy F1 = 0.644 | experiments.tex Table 2 (L67) | Greedy (T=0) F1 = 0.663 | **HIGH** | 1.9pp discrepancy in greedy baseline between provenance (exp_016_rerun_1024_bootstrap) and paper Table 2 (exp_016_signal_ensemble). | Clarify which experiment sources Table 2. If different experiments, provenance should reference the correct one. |\n| 5 | paper_provenance.yaml c013 | oracle = 0.776 | experiments.tex Table 2 (L66) | Oracle = 0.778±0.003 | MEDIUM | Minor discrepancy (0.002). Different source experiments. | Align provenance to published value. |\n| 6 | experiments.tex:L9 | SciERC: ≈65% F1 | discussion.tex:L13 | SciERC (66%) | MEDIUM | \"≈65%\" refers to single-sample (0.645), \"66%\" refers to greedy (0.663). With the \"Single=greedy\" issue, these become entangled. | Standardize: if \"Single\" is the reference, use \"65%\"; if greedy, use \"66%\". Pick one. |\n| 7 | experiments.tex:L11 | WNUT-17: 52% zero F1 | paper_provenance.yaml c021 | 54% zero F1 (evidence: 53.7%) | MEDIUM | Paper says 52%, provenance says 54%/53.7%. Different filtering or rounding. | Verify exact number from exp_003 data and standardize. |\n| 8 | experiments.tex:L89 | LP Δ=+0.2pp (LP 0.647 - Single 0.645) | paper_provenance.yaml c011 | logprob +0.6pp (LP 0.650 - greedy 0.644) | MEDIUM | Different source experiments produce different LP values (0.647 vs 0.650) and different baselines. | Provenance should reference the same experiment as Table 2. |\n| 9 | appendix.tex:L81 | SJ N=8→N=16 gain = +0.047 | appendix.tex tab:n-scaling (L861) | SJ N=8→N=16 Δ = +0.0464 | LOW | Appendix text uses different baseline (single-seed 0.360) vs N-scaling table (3-seed mean 0.3641). Reported as +0.047 but actual calculation from text values: 0.411-0.360=0.051. | Use consistent baselines; if comparing 3-seed means, use both from N-scaling table (+0.046). |\n| 10 | paper_provenance.yaml c025 | SJ T=0.7 ρ = 0.388 | appendix.tex tab:robustness (L44) | SJ T=0.7 ρ = 0.364 | MEDIUM | Provenance cites exp_005 value (0.388); published table uses different value (0.364). Provenance is stale. | Update provenance to match published appendix table. |\n| 11 | paper_provenance.yaml c002 | VC AUROC (corrected) = 0.684 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | **HIGH** | Provenance note says \"Corrected to .684 via exp_012_rerun_1024\" but Table 1 shows .663. | Provenance values don't match final paper. Update provenance. |\n| 12 | introduction.tex:L35 | \"13-18 pp oracle headroom\" (context: greedy surpasses) | experiments.tex Table 2 | Oracle-Greedy = 0.778-0.663 = 11.5pp | MEDIUM | \"13-18pp\" is oracle vs single-sample (13.3 NER, 18.1 RE), not oracle vs greedy. The sentence juxtaposes greedy performance with headroom measured from a different baseline. Technically correct but misleading in context. | Consider rephrasing: \"despite 13pp oracle headroom above single-sample\" to avoid conflation with the greedy baseline in the same sentence. |\n| 13 | paper_provenance.yaml c004 | Voting RE ρ=0.350 (corrected) | appendix.tex tab:multiseed (L417) | RE VC mean ρ=0.309±0.024 | LOW | Provenance (single seed=42) vs appendix (3-seed mean). Both can be correct for their context but provenance should note this is single-seed. | Add note to provenance that 0.350 is seed=42 only; 3-seed mean is 0.309. |\n\n---\n\n## Provenance-Paper Alignment Summary\n\nThe provenance yaml (version 100, built 2026-05-16) has multiple values that don't match the final published tables. Key mismatches:\n\n| Provenance Claim | Provenance Value | Paper Value | Status |\n|-----------------|-----------------|-------------|--------|\n| c002: EM NER AUROC | 0.749 | 0.614 | **STALE** |\n| c002: VC NER AUROC | 0.684 | 0.663 | **STALE** |\n| c013: greedy NER F1 | 0.644 | 0.663 | **STALE** |\n| c013: oracle NER F1 | 0.776 | 0.778 | Minor |\n| c011: LP F1 | 0.650 | 0.647 | **STALE** |\n| c025: SJ T=0.7 ρ | 0.388 | 0.364 | **STALE** |\n\n**Root cause**: Provenance references experiments (exp_012_rerun_1024, exp_016_rerun_1024_bootstrap) that differ from the experiment sourcing Table 2 (exp_016_signal_ensemble). The provenance was not updated after the final table values were finalized.\n\n---\n\n## Cross-Section Consistency for Key Numbers\n\n### Consistent across sections (verified):\n- ρ up to 0.38 (abstract/intro/conclusion) ← VC 0.379 rounds to 0.38 ✓\n- 0.45 on ceiling control (abstract/intro/conclusion) ← EM CoNLL 0.451 ✓\n- 21-58% instance degeneracy (abstract/intro/discussion/conclusion) ← Table 3 ✓\n- median ρ=0.52 within-instance (abstract/intro/discussion) ← Table 3: 0.524 ✓\n- 0.041 nats LP range (abstract/intro/discussion/conclusion/appendix) ✓\n- MBR closes 23-41% (intro/discussion/Table 3) ✓\n- Greedy F1=0.663 (intro/experiments/discussion) ✓\n- Non-tied LP: +2.9pp, p=0.004 (experiments/discussion/appendix) ✓\n- VerbConf mean 8.58/10 SciERC (discussion 8.6, limitations 8.58, appendix 8.58) ✓\n- ECE 0.069-0.096 NER (experiments/appendix) ✓\n- Entity-token LP 4× variance (discussion/limitations) ✓\n\n### Rounding conventions used:\n- 0.379 → \"0.38\" in prose ✓\n- 0.451 → \"0.45\" in prose ✓\n- 8.58 → \"8.6\" in discussion prose ✓\n- 0.524 → \"0.52\" in abstract/intro ✓\n\n---\n\n## Recommendations (Priority Order)\n\n1. **Fix #1 immediately** (reviewer-flagged): Resolve the \"+0.1pp over single\" vs \"+0.4pp over greedy\" contradiction in limitations.tex\n2. **Fix #2**: Reconcile Table 1 AUROC values with multi-seed table — either add a note about different eval protocols or correct one table\n3. **Rebuild provenance**: Multiple provenance entries reference superseded experiments. Full provenance rebuild needed against final Table 1/2 values.\n4. **Standardize SciERC F1 reference**: Pick \"≈65%\" (single-sample) or \"≈66%\" (greedy) and use consistently. Given the \"Single=greedy\" issue, this needs resolution first.\n5. **Minor fixes**: WNUT zero-F1 percentage (52% vs 53.7%), N-scaling gain reporting.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md",
    "content": "# Claim Audit Report: Numerical Consistency Check\n\n**Paper**: Strong Predictors, Weak Selectors  \n**Date**: 2026-05-16  \n**Scope**: All sections in `docs/paper/sections/` + `paper_provenance.yaml`\n\n---\n\n## Inconsistency List\n\n| # | Location 1 | Value 1 | Location 2 | Value 2 | Severity | Issue | Suggested Fix |\n|---|-----------|---------|-----------|---------|----------|-------|---------------|\n| 1 | discussion.tex:L43 | LP×VC best: +0.1pp over single-sample | limitations.tex:L10 | LP×VC: +0.4pp over greedy | **HIGH** | Mathematically contradictory. If best=single+0.1pp=0.646, then vs greedy (0.663)=-1.7pp, not +0.4pp. | Limitations should read \"+0.4pp over single-sample\" OR discussion value needs correction. Verify from exp data which is correct. |\n| 2 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | appendix.tex tab:multiseed (L419) | VC NER AUROC mean = .697±.010 | **HIGH** | Mathematically impossible: if seed=42 gives .663, population σ over 3 seeds cannot be .010 with mean .697 (seed=42 deviation alone = .034 > 3×σ). | Either Table 1 AUROC is not from seed=42, or multi-seed AUROC values are from a different eval protocol. Reconcile. |\n| 3 | paper_provenance.yaml c002 | EM NER AUROC = 0.749 | experiments.tex Table 1 (L37) | EM SciERC AUROC = .614 | **HIGH** | Provenance claims EM leads AUROC at 0.749; published Table 1 shows EM=.614, VC leads at .663. Provenance narrative contradicts paper. | Update provenance to match final Table 1 values. |\n| 4 | paper_provenance.yaml c013 | greedy F1 = 0.644 | experiments.tex Table 2 (L67) | Greedy (T=0) F1 = 0.663 | **HIGH** | 1.9pp discrepancy in greedy baseline between provenance (exp_016_rerun_1024_bootstrap) and paper Table 2 (exp_016_signal_ensemble). | Clarify which experiment sources Table 2. If different experiments, provenance should reference the correct one. |\n| 5 | paper_provenance.yaml c013 | oracle = 0.776 | experiments.tex Table 2 (L66) | Oracle = 0.778±0.003 | MEDIUM | Minor discrepancy (0.002). Different source experiments. | Align provenance to published value. |\n| 6 | experiments.tex:L9 | SciERC: ≈65% F1 | discussion.tex:L13 | SciERC (66%) | MEDIUM | \"≈65%\" refers to single-sample (0.645), \"66%\" refers to greedy (0.663). With the \"Single=greedy\" issue, these become entangled. | Standardize: if \"Single\" is the reference, use \"65%\"; if greedy, use \"66%\". Pick one. |\n| 7 | experiments.tex:L11 | WNUT-17: 52% zero F1 | paper_provenance.yaml c021 | 54% zero F1 (evidence: 53.7%) | MEDIUM | Paper says 52%, provenance says 54%/53.7%. Different filtering or rounding. | Verify exact number from exp_003 data and standardize. |\n| 8 | experiments.tex:L89 | LP Δ=+0.2pp (LP 0.647 - Single 0.645) | paper_provenance.yaml c011 | logprob +0.6pp (LP 0.650 - greedy 0.644) | MEDIUM | Different source experiments produce different LP values (0.647 vs 0.650) and different baselines. | Provenance should reference the same experiment as Table 2. |\n| 9 | appendix.tex:L81 | SJ N=8→N=16 gain = +0.047 | appendix.tex tab:n-scaling (L861) | SJ N=8→N=16 Δ = +0.0464 | LOW | Appendix text uses different baseline (single-seed 0.360) vs N-scaling table (3-seed mean 0.3641). Reported as +0.047 but actual calculation from text values: 0.411-0.360=0.051. | Use consistent baselines; if comparing 3-seed means, use both from N-scaling table (+0.046). |\n| 10 | paper_provenance.yaml c025 | SJ T=0.7 ρ = 0.388 | appendix.tex tab:robustness (L44) | SJ T=0.7 ρ = 0.364 | MEDIUM | Provenance cites exp_005 value (0.388); published table uses different value (0.364). Provenance is stale. | Update provenance to match published appendix table. |\n| 11 | paper_provenance.yaml c002 | VC AUROC (corrected) = 0.684 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | **HIGH** | Provenance note says \"Corrected to .684 via exp_012_rerun_1024\" but Table 1 shows .663. | Provenance values don't match final paper. Update provenance. |\n| 12 | introduction.tex:L35 | \"13-18 pp oracle headroom\" (context: greedy surpasses) | experiments.tex Table 2 | Oracle-Greedy = 0.778-0.663 = 11.5pp | MEDIUM | \"13-18pp\" is oracle vs single-sample (13.3 NER, 18.1 RE), not oracle vs greedy. The sentence juxtaposes greedy performance with headroom measured from a different baseline. Technically correct but misleading in context. | Consider rephrasing: \"despite 13pp oracle headroom above single-sample\" to avoid conflation with the greedy baseline in the same sentence. |\n| 13 | paper_provenance.yaml c004 | Voting RE ρ=0.350 (corrected) | appendix.tex tab:multiseed (L417) | RE VC mean ρ=0.309±0.024 | LOW | Provenance (single seed=42) vs appendix (3-seed mean). Both can be correct for their context but provenance should note this is single-seed. | Add note to provenance that 0.350 is seed=42 only; 3-seed mean is 0.309. |\n\n---\n\n## Provenance-Paper Alignment Summary\n\nThe provenance yaml (version 100, built 2026-05-16) has multiple values that don't match the final published tables. Key mismatches:\n\n| Provenance Claim | Provenance Value | Paper Value | Status |\n|-----------------|-----------------|-------------|--------|\n| c002: EM NER AUROC | 0.749 | 0.614 | **STALE** |\n| c002: VC NER AUROC | 0.684 | 0.663 | **STALE** |\n| c013: greedy NER F1 | 0.644 | 0.663 | **STALE** |\n| c013: oracle NER F1 | 0.776 | 0.778 | Minor |\n| c011: LP F1 | 0.650 | 0.647 | **STALE** |\n| c025: SJ T=0.7 ρ | 0.388 | 0.364 | **STALE** |\n\n**Root cause**: Provenance references experiments (exp_012_rerun_1024, exp_016_rerun_1024_bootstrap) that differ from the experiment sourcing Table 2 (exp_016_signal_ensemble). The provenance was not updated after the final table values were finalized.\n\n---\n\n## Cross-Section Consistency for Key Numbers\n\n### Consistent across sections (verified):\n- ρ up to 0.38 (abstract/intro/conclusion) ← VC 0.379 rounds to 0.38 ✓\n- 0.45 on ceiling control (abstract/intro/conclusion) ← EM CoNLL 0.451 ✓\n- 21-58% instance degeneracy (abstract/intro/discussion/conclusion) ← Table 3 ✓\n- median ρ=0.52 within-instance (abstract/intro/discussion) ← Table 3: 0.524 ✓\n- 0.041 nats LP range (abstract/intro/discussion/conclusion/appendix) ✓\n- MBR closes 23-41% (intro/discussion/Table 3) ✓\n- Greedy F1=0.663 (intro/experiments/discussion) ✓\n- Non-tied LP: +2.9pp, p=0.004 (experiments/discussion/appendix) ✓\n- VerbConf mean 8.58/10 SciERC (discussion 8.6, limitations 8.58, appendix 8.58) ✓\n- ECE 0.069-0.096 NER (experiments/appendix) ✓\n- Entity-token LP 4× variance (discussion/limitations) ✓\n\n### Rounding conventions used:\n- 0.379 → \"0.38\" in prose ✓\n- 0.451 → \"0.45\" in prose ✓\n- 8.58 → \"8.6\" in discussion prose ✓\n- 0.524 → \"0.52\" in abstract/intro ✓\n\n---\n\n## Recommendations (Priority Order)\n\n1. **Fix #1 immediately** (reviewer-flagged): Resolve the \"+0.1pp over single\" vs \"+0.4pp over greedy\" contradiction in limitations.tex\n2. **Fix #2**: Reconcile Table 1 AUROC values with multi-seed table — either add a note about different eval protocols or correct one table\n3. **Rebuild provenance**: Multiple provenance entries reference superseded experiments. Full provenance rebuild needed against final Table 1/2 values.\n4. **Standardize SciERC F1 reference**: Pick \"≈65%\" (single-sample) or \"≈66%\" (greedy) and use consistently. Given the \"Single=greedy\" issue, this needs resolution first.\n5. **Minor fixes**: WNUT zero-F1 percentage (52% vs 53.7%), N-scaling gain reporting.\n"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T09:53:10.654559+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T09:53:10.654716+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md",
  "content": "# \"Single\" Label Issues\n\n**Background**: Discovery that Table 2's \"Single\" row may actually be T=0 greedy decoding, mislabeled as \"one T=1.0 draw.\"\n\n---\n\n## Evidence For/Against \"Single = T=0 Greedy\"\n\n### Arguments supporting the mislabeling theory:\n1. Provenance c013 lists `greedy=0.644` — very close to paper's `Single=0.645`\n2. The provenance selection data (c011) has no explicit \"single\" field — only `greedy: 0.644, logprob: 0.650, sj: 0.645...`\n3. Provenance c011 computes LP gain as \"+0.6pp\" — this is `0.650-0.644=+0.6pp`, treating the 0.644 value as the single-sample baseline\n\n### Arguments against the mislabeling theory:\n1. Table 2 shows `Single: 0.645 ± 0.001` — the ±0.001 variance implies stochasticity, inconsistent with deterministic T=0\n2. Paper has BOTH `Greedy (T=0) = 0.663` and `Single = 0.645` as separate rows — if both are T=0, they should be identical\n3. Method.tex L61 explicitly defines: \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\"\n4. Table 2 footnote: \"‡Single: one T=1.0 draw (expected performance of a single sample)\"\n\n### Possible resolution:\nThe numbers suggest the pipeline has TWO different evaluation protocols both labeled as \"greedy/T=0\":\n- `Greedy (T=0)` in Table 2 (F1=0.663): from one experiment/eval set\n- `greedy` in provenance c013 (F1=0.644): from a different experiment (exp_016_rerun_1024_bootstrap)\n\nThe 1.9pp gap between them (0.663 vs 0.644) is too large to be noise. Likely explanations:\n- Different instance filtering (full set vs gold-filtered)\n- Different seed\n- One is 2-seed averaged, the other single-seed\n\nIf \"Single\" (0.645) ≈ provenance \"greedy\" (0.644), the issue may be that the provenance experiment computed its \"greedy\" baseline differently from Table 2's \"Greedy\" row.\n\n---\n\n## Affected Claims (If Single IS T=0 Greedy)\n\n### Category A: \"Over single-sample\" comparisons become \"over greedy\"\n\n| Location | Claim | Current Interpretation | If Single=Greedy |\n|----------|-------|----------------------|------------------|\n| experiments.tex:L89 | \"LP achieves 0.647 (Δ=+0.2pp)\" | LP beats single T=1.0 draw | LP beats greedy by 0.2pp → greedy no longer best |\n| experiments.tex:L89 | \"oracle reveals 13.3pp headroom above single-sample\" | Headroom above T=1.0 draw | Headroom above greedy |\n| experiments.tex:L93 | \"Greedy (T=0) surpasses all N=8 selection strategies\" | Greedy > LP > Single | If Single=Greedy, contradiction: \"Greedy\"(0.663) ≠ \"Single\"(0.645) |\n| introduction.tex:L35 | \"Greedy decoding (F1=0.663) surpasses all N=8 selection strategies (best: 0.647) despite 13-18pp oracle headroom\" | Clean claim | The \"13-18pp\" is now headroom over greedy, not over a stochastic sample |\n| discussion.tex:L43 | \"All three fail to improve over single-sample (best: +0.1pp)\" | Combinations vs T=1.0 | Combinations vs greedy |\n\n### Category B: The \"correlation-selection gap\" framing\n\nThe gap is defined as: \"quality estimation works (ρ=0.38), but selection fails to beat single-sample.\"\n- If single-sample IS greedy, then the gap is: \"QE works, but selection fails to beat greedy.\"\n- This actually STRENGTHENS the argument (it's even harder to beat greedy than a random T=1.0 draw).\n- BUT: it removes the claim that \"multi-sample is worse than the trivial single-sample baseline\" because the baseline is no longer trivial (it's the best possible deterministic output).\n\n### Category C: Definition contradictions\n\n| Location | Text | Issue |\n|----------|------|-------|\n| method.tex:L61 | \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\" | Definition explicitly says NOT argmax |\n| experiments.tex:L60-61 | \"‡Single: one T=1.0 draw (expected performance of a single sample)\" | Footnote repeats the T=1.0 claim |\n| experiments.tex:L78 | `Single‡ & 0.645 ± 0.001` | ±0.001 would be expected for T=1.0 across seeds |\n\n### Category D: If there are TWO greedy values in the paper\n\n| Row | F1 | Claimed Identity | Actual |\n|-----|-----|-----------------|--------|\n| Greedy (T=0)† | 0.663 | argmax decoding | ??? |\n| Single‡ | 0.645±0.001 | one T=1.0 draw | ??? |\n\nIf both are T=0, they MUST give identical F1 (deterministic). The 1.8pp difference proves they cannot both be T=0 under the same evaluation protocol. Therefore EITHER:\n1. Single IS T=1.0 (as stated) — no mislabeling, just confusing provenance\n2. They use different eval sets (e.g., Greedy on n=551, Single on n=529 gold-filtered)\n3. One is averaged over seeds differently\n\n---\n\n## Recommended Investigation\n\n1. **Check the experiment code**: Verify the temperature parameter used when computing the \"single\" baseline in exp_016_signal_ensemble\n2. **Check instance counts**: If Greedy uses n=551 (full) and Single uses n=529 (gold-filtered), the 1.8pp difference could be explained by the 22 excluded instances\n3. **Reconcile provenance \"greedy=0.644\" with paper \"Greedy=0.663\"**: Identify which experiment/filtering produces each\n4. **If Single is confirmed T=1.0**: Update provenance to stop conflating \"single\" with \"greedy\"\n5. **If Single is confirmed T=0**: \n   - Correct method.tex definition\n   - Correct table footnotes\n   - Reframe all \"vs single-sample\" claims\n   - Address why Greedy(0.663)≠Single(0.645) if both are T=0\n\n---\n\n## Impact Assessment\n\n| Scenario | Impact on Paper Claims | Severity |\n|----------|----------------------|----------|\n| Single is actually T=1.0 (no bug) | No impact; provenance needs cleanup only | Low |\n| Single is T=0 but from different eval set | Need to clarify eval protocol; minor text fixes | Medium |\n| Single is truly mislabeled T=0 with same eval set | Major rewrite of framing; \"Greedy=0.663\" row becomes unexplained | **Critical** |\n\nThe ±0.001 variance in the Single row and the 1.8pp gap from Greedy argue strongly that **Single is genuinely T=1.0** and the confusion stems from provenance using a different experiment's \"greedy\" value (0.644) that happens to be close to Single (0.645). The real issue is the provenance-paper misalignment documented in the main audit report.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md",
    "content": "# \"Single\" Label Issues\n\n**Background**: Discovery that Table 2's \"Single\" row may actually be T=0 greedy decoding, mislabeled as \"one T=1.0 draw.\"\n\n---\n\n## Evidence For/Against \"Single = T=0 Greedy\"\n\n### Arguments supporting the mislabeling theory:\n1. Provenance c013 lists `greedy=0.644` — very close to paper's `Single=0.645`\n2. The provenance selection data (c011) has no explicit \"single\" field — only `greedy: 0.644, logprob: 0.650, sj: 0.645...`\n3. Provenance c011 computes LP gain as \"+0.6pp\" — this is `0.650-0.644=+0.6pp`, treating the 0.644 value as the single-sample baseline\n\n### Arguments against the mislabeling theory:\n1. Table 2 shows `Single: 0.645 ± 0.001` — the ±0.001 variance implies stochasticity, inconsistent with deterministic T=0\n2. Paper has BOTH `Greedy (T=0) = 0.663` and `Single = 0.645` as separate rows — if both are T=0, they should be identical\n3. Method.tex L61 explicitly defines: \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\"\n4. Table 2 footnote: \"‡Single: one T=1.0 draw (expected performance of a single sample)\"\n\n### Possible resolution:\nThe numbers suggest the pipeline has TWO different evaluation protocols both labeled as \"greedy/T=0\":\n- `Greedy (T=0)` in Table 2 (F1=0.663): from one experiment/eval set\n- `greedy` in provenance c013 (F1=0.644): from a different experiment (exp_016_rerun_1024_bootstrap)\n\nThe 1.9pp gap between them (0.663 vs 0.644) is too large to be noise. Likely explanations:\n- Different instance filtering (full set vs gold-filtered)\n- Different seed\n- One is 2-seed averaged, the other single-seed\n\nIf \"Single\" (0.645) ≈ provenance \"greedy\" (0.644), the issue may be that the provenance experiment computed its \"greedy\" baseline differently from Table 2's \"Greedy\" row.\n\n---\n\n## Affected Claims (If Single IS T=0 Greedy)\n\n### Category A: \"Over single-sample\" comparisons become \"over greedy\"\n\n| Location | Claim | Current Interpretation | If Single=Greedy |\n|----------|-------|----------------------|------------------|\n| experiments.tex:L89 | \"LP achieves 0.647 (Δ=+0.2pp)\" | LP beats single T=1.0 draw | LP beats greedy by 0.2pp → greedy no longer best |\n| experiments.tex:L89 | \"oracle reveals 13.3pp headroom above single-sample\" | Headroom above T=1.0 draw | Headroom above greedy |\n| experiments.tex:L93 | \"Greedy (T=0) surpasses all N=8 selection strategies\" | Greedy > LP > Single | If Single=Greedy, contradiction: \"Greedy\"(0.663) ≠ \"Single\"(0.645) |\n| introduction.tex:L35 | \"Greedy decoding (F1=0.663) surpasses all N=8 selection strategies (best: 0.647) despite 13-18pp oracle headroom\" | Clean claim | The \"13-18pp\" is now headroom over greedy, not over a stochastic sample |\n| discussion.tex:L43 | \"All three fail to improve over single-sample (best: +0.1pp)\" | Combinations vs T=1.0 | Combinations vs greedy |\n\n### Category B: The \"correlation-selection gap\" framing\n\nThe gap is defined as: \"quality estimation works (ρ=0.38), but selection fails to beat single-sample.\"\n- If single-sample IS greedy, then the gap is: \"QE works, but selection fails to beat greedy.\"\n- This actually STRENGTHENS the argument (it's even harder to beat greedy than a random T=1.0 draw).\n- BUT: it removes the claim that \"multi-sample is worse than the trivial single-sample baseline\" because the baseline is no longer trivial (it's the best possible deterministic output).\n\n### Category C: Definition contradictions\n\n| Location | Text | Issue |\n|----------|------|-------|\n| method.tex:L61 | \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\" | Definition explicitly says NOT argmax |\n| experiments.tex:L60-61 | \"‡Single: one T=1.0 draw (expected performance of a single sample)\" | Footnote repeats the T=1.0 claim |\n| experiments.tex:L78 | `Single‡ & 0.645 ± 0.001` | ±0.001 would be expected for T=1.0 across seeds |\n\n### Category D: If there are TWO greedy values in the paper\n\n| Row | F1 | Claimed Identity | Actual |\n|-----|-----|-----------------|--------|\n| Greedy (T=0)† | 0.663 | argmax decoding | ??? |\n| Single‡ | 0.645±0.001 | one T=1.0 draw | ??? |\n\nIf both are T=0, they MUST give identical F1 (deterministic). The 1.8pp difference proves they cannot both be T=0 under the same evaluation protocol. Therefore EITHER:\n1. Single IS T=1.0 (as stated) — no mislabeling, just confusing provenance\n2. They use different eval sets (e.g., Greedy on n=551, Single on n=529 gold-filtered)\n3. One is averaged over seeds differently\n\n---\n\n## Recommended Investigation\n\n1. **Check the experiment code**: Verify the temperature parameter used when computing the \"single\" baseline in exp_016_signal_ensemble\n2. **Check instance counts**: If Greedy uses n=551 (full) and Single uses n=529 (gold-filtered), the 1.8pp difference could be explained by the 22 excluded instances\n3. **Reconcile provenance \"greedy=0.644\" with paper \"Greedy=0.663\"**: Identify which experiment/filtering produces each\n4. **If Single is confirmed T=1.0**: Update provenance to stop conflating \"single\" with \"greedy\"\n5. **If Single is confirmed T=0**: \n   - Correct method.tex definition\n   - Correct table footnotes\n   - Reframe all \"vs single-sample\" claims\n   - Address why Greedy(0.663)≠Single(0.645) if both are T=0\n\n---\n\n## Impact Assessment\n\n| Scenario | Impact on Paper Claims | Severity |\n|----------|----------------------|----------|\n| Single is actually T=1.0 (no bug) | No impact; provenance needs cleanup only | Low |\n| Single is T=0 but from different eval set | Need to clarify eval protocol; minor text fixes | Medium |\n| Single is truly mislabeled T=0 with same eval set | Major rewrite of framing; \"Greedy=0.663\" row becomes unexplained | **Critical** |\n\nThe ±0.001 variance in the Single row and the 1.8pp gap from Greedy argue strongly that **Single is genuinely T=1.0** and the confusion stems from provenance using a different experiment's \"greedy\" value (0.644) that happens to be close to Single (0.645). The real issue is the provenance-paper misalignment documented in the main audit report.\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T09:53:10.654935+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T09:53:10.655079+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:53:10.655344+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T09:53:10.655498+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "d112_claim_audit_report",
  "type": "report",
  "description": "Systematic numerical consistency audit of all paper sections. Found 13 inconsistencies (5 HIGH, 5 MEDIUM, 3 LOW) including reviewer-flagged +0.1pp/+0.4pp contradiction, Table 1 vs multi-seed AUROC mathematical impossibility, and 6 stale provenance entries.",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md",
  "tags": "['paper', 'audit', 'round15', 'numerical-consistency']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "d112_claim_audit_report",
    "type": "report",
    "description": "Systematic numerical consistency audit of all paper sections. Found 13 inconsistencies (5 HIGH, 5 MEDIUM, 3 LOW) including reviewer-flagged +0.1pp/+0.4pp contradiction, Table 1 vs multi-seed AUROC mathematical impossibility, and 6 stale provenance entries.",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md",
    "tags": "['paper', 'audit', 'round15', 'numerical-consistency']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T09:53:10.655722+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_736eaa\", \"name\": \"d112_claim_audit_report\", \"type\": \"report\", \"description\": \"Systematic numerical consistency audit of all paper sections. Found 13 inconsistencies (5 HIGH, 5 MEDIUM, 3 LOW) including reviewer-flagged +0.1pp/+0.4pp contradiction, Table 1 vs multi-seed AUROC mathematical impossibility, and 6 stale provenance entries.\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/audit_report_736eaa.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T09:52:54.496903+00:00\", \"tags\": [\"paper\", \"audit\", \"round15\", \"numerical-consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T09:53:10.655874+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "d112_single_label_issues",
  "type": "report",
  "description": "Analysis of the 'Single' row mislabeling issue in Table 2. Concludes that Single is likely genuinely T=1.0 (±0.001 variance and 1.8pp gap from Greedy prove they cannot both be T=0). The confusion stems from provenance using a different experiment's greedy value (0.644) that coincidentally approximates Single (0.645).",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md",
  "tags": "['paper', 'audit', 'round15', 'single-label', 'table2']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "d112_single_label_issues",
    "type": "report",
    "description": "Analysis of the 'Single' row mislabeling issue in Table 2. Concludes that Single is likely genuinely T=1.0 (±0.001 variance and 1.8pp gap from Greedy prove they cannot both be T=0). The confusion stems from provenance using a different experiment's greedy value (0.644) that coincidentally approximates Single (0.645).",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md",
    "tags": "['paper', 'audit', 'round15', 'single-label', 'table2']"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T09:53:10.656032+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e0eca0\", \"name\": \"d112_single_label_issues\", \"type\": \"report\", \"description\": \"Analysis of the 'Single' row mislabeling issue in Table 2. Concludes that Single is likely genuinely T=1.0 (±0.001 variance and 1.8pp gap from Greedy prove they cannot both be T=0). The confusion stems from provenance using a different experiment's greedy value (0.644) that coincidentally approximates Single (0.645).\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/single_label_issues.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T09:52:57.463770+00:00\", \"tags\": [\"paper\", \"audit\", \"round15\", \"single-label\", \"table2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_claim_audit_20260516T094502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-16T09:53:10.656240+00:00_

审计完成。主要发现：

**5个HIGH严重度问题：**
1. Discussion "+0.1pp over single-sample" vs Limitations "+0.4pp over greedy" — 数学上矛盾（审稿人已指出）
2. Table 1 VC AUROC (.663) vs multi-seed table (.697±.010) — seed=42 数学上不可能产生这个均值/σ组合
3. Provenance c002 "EM AUROC=0.749" vs Table 1 实际值 .614 — provenance 严重过时
4. Provenance greedy=0.644 vs paper greedy=0.663 — 来源实验不同，1.9pp差距
5. Provenance VC AUROC=0.684 vs Table 1 VC AUROC=.663 — provenance 过时

**关于 "Single=T=0 greedy" 的结论：**
Single 行大概率确实是 T=1.0。证据：±0.001 方差（T=0 应为零方差）+ 与 Greedy 行差 1.8pp（如果都是 T=0 应完全相同）。混淆来源是 provenance 引用了不同实验的 greedy 值 (0.644) 恰好接近 Single (0.645)。

**最优先修复：** limitations.tex L10 的 "+0.4pp over greedy" 需改为 "+0.1pp over single-sample"（或从实验数据确认正确值）。

产出已保存到 `artifacts/d112_claim_audit/` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d112_claim_audit_20260516T094502"
}
```

</details>

---
