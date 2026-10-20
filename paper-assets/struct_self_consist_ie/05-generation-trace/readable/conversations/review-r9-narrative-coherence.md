# review r9 narrative coherence

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_review_r9_narrative_coherence_20260516T010130.jsonl`
- **Structured JSON:** [`a78e6e8c0558f18373cf.json`](../../sessions/a7/a78e6e8c0558f18373cf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-16T01:05:42.938759+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T01:05:42.939166+00:00_

artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
artifacts/_project/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T01:05:42.939368+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T01:05:42.939508+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T01:05:42.939669+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T01:05:42.940151+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (3 条, D072 updated — ablation proves universality)\\n\\n### Claim 1 (PRIMARY — Universal Correlation-Selection Gap)\\nThe correlation-selection gap in structured IE is a **fundamental property of the task**, not an artifact of constrained decoding. Confidence signals reliably predict output quality (AUROC up to 0.75) but cannot select better candidates from multiple samples. A controlled free-form decoding ablation proves this gap is universal: removing constrained decoding does NOT recover logprob variance or selection ability.\\n\\n**Two-layer argument**:\\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation FALSIFIES regime-specific hypothesis**: removing constrained decoding does NOT recover logprob discrimination (std ratio 0.97, tied fraction -2pp) → compression is model/task intrinsic, proving universality via elimination.\\n\\n**Key evidence (score compression)**:\\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ:
…[truncated 25966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T01:05:42.940371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T01:05:42.940517+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T01:05:42.940652+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T01:05:42.940806+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives.
14	\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.
15	\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.
16	These require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.
17	Existing evaluations rarely separate the two.
18	Self-consistency methods designed for discrete answers \cite{wan
…[truncated 4392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T01:05:42.940970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T01:05:42.941154+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	Our work connects three research threads: self-consistency and test-time scaling methods developed for reasoning tasks, confidence estimation for structured information extraction, and broader uncertainty quantification for language models.
4	
5	\subsection{Self-Consistency and Test-Time Scaling}
6	
7	\paragraph{Self-consistency for discrete and free-form tasks.}
8	Self-consistency decoding \cite{wang2023selfconsistency} improves chain-of-thought reasoning by sampling multiple rationales and selecting the most frequent answer via majority vote.
9	This paradigm assumes a discrete answer space where outputs can be grouped by equivalence and counted---an assumption that holds for arithmetic, commonsense QA, and similar tasks but breaks for set-valued structured outputs.
10	\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.
11	\citet{thirukovalluru2024atomic} decompose long-form outputs into atomic sub-claims and measure per-claim consistency, moving beyond whole-output comparison.
12	These methods operate on text-level equivalence or entailment; our work instead compares \textit{structured sets} of entities and relations, requiring set-theoretic similarity measures that account for partial overlap, type constraints, and span-level matching.
13	
14	\paragraph{Test-time scaling and sample selection.}
15	A growing body of work studies how to allocate additional compute at inference time.
16	\citet{snell2024scaling} characterize the scaling laws governing test-time compute, showing that repeated sampling with effective selection can substitute for model scaling.
17	\citet{brown2024monkeys} demonstrate that best-of-$N$ sampling with large $N$ yields substantial gains across diverse tasks.
18	Several recent m
…[truncated 7417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T01:05:42.941305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T01:05:42.941531+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.
12	This gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\S\ref{sec:complexity_robustness}).
13	
14	\paragraph{Models.}
15	Our primary model is \textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.
16	For cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.
17	
18	\paragraph{Sampling and Evaluation.}
19	For each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.
20	We use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.
21	Quality estimation is measured along two axes: \textit{rank correlation} with instance-level F1 via Spearman $\rho$ and Kendall $\tau$, and \textit{binary discrimination} via AUROC (instances above vs.\ below median F1).
22	Downstream utility is assessed through \textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instan
…[truncated 16838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T01:05:42.941680+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T01:05:42.941827+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	Our results suggest different signal choices depending on the deployment scenario.
5	For per-instance quality estimation, entity voting provides the strongest single signal ($\rho{=}0.50$, Table~\ref{tab:quality_estimation}).
6	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.
7	Under conditional filtering, SJ achieves $\rho{\approx}0.4$ on both NER and RE (\S\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.
8	For binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).
9	For best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\ref{tab:selection}).
10	
11	\paragraph{Signals discriminate between instances, not within strata.}
12	When instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.
13	Confidence signals capture \textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.
14	This is the complementary face of the correlation-selection gap (\S\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.
15	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
16	
17	\paragraph{Task-difficulty-dependent signal selection.}
18	Across all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\S\ref{sec:complexity_robustness}).
19	However, the \text
…[truncated 2169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T01:05:42.941973+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T01:05:42.942107+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
15	Integration with conformal prediction could convert continuous confidence scores into cal
…[truncated 211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T01:05:42.942268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T01:05:42.942397+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL, the SJ--FK gap is only 0.004 ($\rho{=}0.436$ vs.\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T01:05:42.942566+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T01:05:42.942713+00:00_

artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/_project/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T01:05:42.942880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T01:05:42.943045+00:00_

1	% Requires: \usepackage{booktabs, multirow}
2	\begin{table*}[t]
3	\centering
4	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
5	\label{tab:freeform-ablation}
6	
7	%% ---- Panel A: Logprob Distribution ----
8	\vspace{2pt}
9	{\small\textsc{Panel A: Logprob Distribution}}
10	\vspace{2pt}
11	
12	\begin{tabular}{lccc}
13	\toprule
14	Metric & Constrained & Free-form & $\Delta$ \\
15	\midrule
16	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
17	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
18	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
19	\bottomrule
20	\end{tabular}
21	
22	\vspace{8pt}
23	
24	%% ---- Panel B: Selection F1 ----
25	{\small\textsc{Panel B: Selection F1}}
26	\vspace{2pt}
27	
28	\begin{tabular}{llccc}
29	\toprule
30	Task & Method & Constrained & Free-form & $\Delta$ \\
31	\midrule
32	\multirow{3}{*}{NER}
33	  & Greedy        & 0.6182 & 0.6204 & \textbf{+0.0022} \\
34	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
35	  & Selection gap & +0.0059 & +0.0018 & $-$0.0041 \\
36	\midrule
37	\multirow{3}{*}{RE}
38	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
39	  & LP-selected   & 0.2845 & 0.3050 & \textbf{+0.0205} \\
40	  & Selection gap & $-$0.0068 & +0.0169 & \textbf{+0.0237} \\
41	\bottomrule
42	\end{tabular}
43	
44	\vspace{8pt}
45	
46	%% ---- Panel C: QE Signal Quality (Spearman ρ) ----
47	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
48	\vspace{2pt}
49	
50	\begin{tabular}{l ccc ccc}
51	\toprule
52	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
53	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
54	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
55	\midrule
56	SJ & 0.3599 & 0.3774 & \textbf{+0.0175} & 0.2503 & 0.2728 & \textbf{+0.0225} \\
57	FK & 0.2665 & 0.3197 & \textbf{+0.0532} & 0.2752 & 0.3145 & \textbf{+0.0393} \\
58	LP & 0.2052 & 0.2129 & \textbf{+0.0077} & 0.2662 & 0.3042 & \textbf{+0.0379}
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T01:05:42.943250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T01:05:42.943423+00:00_

1	% N-scaling appendix tables for Structured Self-Consistency paper
2	% Requires: booktabs package
3	
4	%%% Table 1: N=8 vs N=16 Comparison (Spearman ρ)
5	\begin{table}[t]
6	\centering
7	\caption{Effect of sample pool size on signal quality (Qwen 2.5-7B, SciERC, 3-seed mean Spearman $\rho$).}
8	\label{tab:n-scaling}
9	\small
10	\begin{tabular}{l ccc ccc}
11	\toprule
12	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
13	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
14	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
15	\midrule
16	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
17	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
18	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
19	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
20	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
21	\midrule
22	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	%%% Table 2: Cross-seed Signal Ranking Stability (Kendall's W)
28	\begin{table}[t]
29	\centering
30	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
31	\label{tab:ranking-stability}
32	\small
33	\begin{tabular}{ll cc l}
34	\toprule
35	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
36	\midrule
37	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
38	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
39	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
40	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
41	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	%%% Table 3: Per-signal Cross-seed σ Comparison
47	\begin{table}[t]
48	\centering
49	\caption{Cross-seed standard deviation ($\si
…[truncated 723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T01:05:42.943575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T01:05:42.943730+00:00_

1	% N-scaling appendix tables for Structured Self-Consistency paper
2	% Requires: booktabs package
3	
4	%%% Table 1: N=8 vs N=16 Comparison (Spearman ρ)
5	\begin{table}[t]
6	\centering
7	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
8	\label{tab:n-scaling}
9	\small
10	\begin{tabular}{l ccc ccc}
11	\toprule
12	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
13	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
14	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
15	\midrule
16	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
17	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
18	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
19	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
20	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
21	\midrule
22	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	%%% Table 2: Cross-seed Signal Ranking Stability (Kendall's W)
28	\begin{table}[t]
29	\centering
30	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
31	\label{tab:ranking-stability}
32	\small
33	\begin{tabular}{ll cc l}
34	\toprule
35	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
36	\midrule
37	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
38	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
39	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
40	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
41	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	%%% Table 3: Per-signal Cross-seed σ Comparison
47	\begin{table}[t]
48	\centering
49	\caption{Cross-seed standard deviation ($\sigma
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T01:05:42.943905+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T01:05:42.944033+00:00_

artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
artifacts/_project/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T01:05:42.944184+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.{pdf,png,eps,svg}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.{pdf,png,eps,svg}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T01:05:42.944309+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T01:05:42.944423+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:method|\\\\label\\{sec:signal|\\\\input\\{|\\\\include\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:method|\\\\label\\{sec:signal|\\\\input\\{|\\\\include\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T01:05:42.944536+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T01:05:42.944676+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{fig:|\\\\ref\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{fig:|\\\\ref\\{tab:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T01:05:42.944807+00:00_

artifacts/_project/paper/experiments.tex:61:Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
artifacts/_project/paper/experiments.tex:85:We return to this distinction in \S\ref{sec:complexity_robustness} and visualize it in Figure~\ref{fig:signal_heatmap}.
artifacts/_project/paper/experiments.tex:120:Table~\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).
artifacts/_project/paper/experiments.tex:137:We attribute this gap (Figure~\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best for a given input.
artifacts/_project/paper/experiments.tex:195:Table~\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.
artifacts/_project/paper/experiments.tex:208:On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
artifacts/_project/paper/experiments.tex:221:The logprob paradox observed in Table~\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.
artifacts/_project/paper/experiments.tex:223:Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.
artifacts/_project/paper/discussion.tex:5:For per-instance quality estimation, entity voting provides the strongest single signal ($\rho{=}0.50$, Table~\ref{tab:quality_estimation}).
artifacts/_project/paper/discussion.tex:6:When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.
artifacts/_project/paper/discus
…[truncated 561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T01:05:42.944983+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{fig:|\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{fig:|\\\\label\\{tab:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T01:05:42.945113+00:00_

artifacts/_project/paper/experiments.tex:45:\label{tab:quality_estimation}
artifacts/_project/paper/experiments.tex:100:\label{tab:selection}
artifacts/_project/paper/experiments.tex:174:\label{tab:robustness}
artifacts/_project/paper/freeform_ablation_appendix_table.tex:5:\label{tab:freeform-ablation}
artifacts/_project/paper/n_scaling_appendix_tables.tex:8:\label{tab:n-scaling}
artifacts/_project/paper/n_scaling_appendix_tables.tex:31:\label{tab:ranking-stability}
artifacts/_project/paper/n_scaling_appendix_tables.tex:50:\label{tab:sigma-comparison}
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex:8:\label{tab:n-scaling}
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex:31:\label{tab:ranking-stability}
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex:50:\label{tab:sigma-comparison}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T01:05:42.945256+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "preliminary|\\\\varepsilon|epsilon",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "tool_args": {
    "pattern": "preliminary|\\\\varepsilon|epsilon",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T01:05:42.945372+00:00_

artifacts/_project/paper/freeform_ablation_appendix_table.tex:18:Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T01:05:42.945482+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "4B|Qwen3-4B|scale ablation|scale.*ablation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "tool_args": {
    "pattern": "4B|Qwen3-4B|scale ablation|scale.*ablation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T01:05:42.945593+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_r9_narrative_coherence_20260516T010130",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T01:05:42.945862+00:00_

审稿完成。以下是完整报告。

---

## Round 9 审稿报告

---

### CRITICAL（必须修复才能提交）

**C1. Method Section 完全缺失**
- `introduction.tex:49` — `\S\ref{sec:method} formalizes the problem and defines the five confidence signals`
- `experiments.tex:27` — `detailed in \S\ref{sec:signals}`
- 整个 `artifacts/_project/paper/` 目录下没有 method.tex 或 methodology.tex。五个信号的形式化定义（SJ 的 bipartite matching、Voting 的 aggregation、FK 的公式等）无处可寻。论文结构不完整，reviewer 无法评估方法。
- **建议**: 创建 method.tex，包含 problem formalization、5 signal definitions、evaluation protocol。

**C2. 全部 4 个 Figure 悬空**
- `introduction.tex:27` → `Figure~\ref{fig:overview}` — 无定义
- `experiments.tex:85` → `Figure~\ref{fig:signal_heatmap}` — 无定义
- `experiments.tex:137` → `Figure~\ref{fig:selection_gap}` — 无定义
- `experiments.tex:223` → `Figure~\ref{fig:reliability}` — 无定义
- 整个 paper 目录下无 `.pdf`/`.png`/`.eps`/`.svg` 文件，也无任何 `\begin{figure}` 环境或 `\label{fig:...}`。编译后所有 figure 引用显示为 "??"。
- **建议**: 创建全部 4 个图。framing R16 明确要求 ≥3 figures，当前为 0。

**C3. 4B Scale Ablation 完全缺失**
- Framing 将 4B ablation 列为 Claim 1 的核心证据（"Scale ablation shows the gap is not an artifact of a particular model size"），R14 标记为 RESOLVED。
- 但全文 grep "4B"、"Qwen3-4B"、"scale ablation" 返回零结果。Conclusion 提到 "scaling analysis with larger models (70B+)" 作为 future work，但对已完成的 4B 实验只字未提。
- **建议**: 在 experiments.tex 的 robustness 分析中新增 scale ablation 段落+表格，引用 framing 中的 2×2 矩阵数据。

**C4. RE 结果未标注 (preliminary)**
- 核心约束要求 "RE 结果标注 preliminary"。
- Grep "preliminary" 返回零结果。所有 RE 数据（Table 1 的 SciERC RE 列、Table 2 的 RE F1、robustness 表的 RE ρ、discussion 中的 RE 讨论）均无标注。
- **建议**: 在所有涉及 RE 的表格标题和正文关键 claim 处加注 "(preliminary; single dataset)"。

**C5. Appendix 表格 Label 冲突**
- `n_scaling_appendix_tables.tex` 和 `n_scaling_appendix_tables_44b000.tex` 都定义了 `\label{tab:n-scaling}`、`\label{tab:ranking-stability}`、`\label{tab:sigma-comparison}`。
- 如果两个文件都被 `\input`，LaTeX 会产生 duplicate label 警告且交叉引用指向错误表格。
- 且旧文件 `n_scaling_appendix_tables.tex` 的 Table 1 caption 写的是 "Qwen 2.5-7B"（过时模型名），新文件写的是 "Qwen3-8B"。
- **建议**: 删除旧文件或重命名其 labels。确认只 include 一个版本。

---

### HIGH（强烈建议修复）

**H1. Free-form Ablation 仅有附录表格，正文无讨论**
- `freeform_ablation_appendix_table.tex` 包含完整的 4-panel 数据，但 experiments.tex 和 discussion.tex 中完全没有引用 `\ref{tab:freeform-ablation}` 或讨论 ablation 结果。
- Framing 将 free-form ablation 定位为 "Story Spine Step 3: Controlled falsification"——论文叙事的核心支柱。当前论文声称 gap 是 "fundamental"（intro:23, experiments:137），但没有呈现证明 universality 的 ablation 证据。
- **建议**: 在 experiments.tex 增加 subsection 或 paragraph 讨论 free-form ablation 结果（至少 LP std ratio 0.97、tied fraction -2pp），引用 appendix 表格。

**H2. ε=0.05 无讨论或 justification**
- `freeform_ablation_appendix_table.tex:18` 使用 `ε=0.05` 定义 tied fraction，但全文无一处解释 ε 的含义、为何选 0.05、或对不同 ε 值的敏感性。
- Framing 说 "ε=0.05 有实证支撑"，但这个实证支撑没有写进论文。
- **建议**: 在 method section（待创建）或 appendix 中定义 ε 并报告 robustness（如 ε∈{0.01, 0.05, 0.1} 的 tied fraction 变化）。

**H3. WNUT-17 在 Abstract 中列为主数据集但主表中缺席**
- `abstract.tex:3` — "three datasets (SciERC, CoNLL-2003, WNUT-17)"
- `experiments.tex:8-12` — WNUT-17 作为第三个 benchmark 详细介绍
- 但 Table 1 (`tab:quality_estimation`) 只有 SciERC 和 CoNLL 的列，WNUT-17 数据仅出现在正文段落（`experiments.tex:166-168`，SJ ρ=0.062，LP ρ=-0.411）。
- Abstract 给读者的预期是三个数据集的完整对比表，实际只有两个。
- **建议**: 将 WNUT-17 加入 Table 1（即使大部分值不显著），或在 abstract 中调整表述为 "primarily evaluate on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe"。

**H4. Discussion 引用未定义的子集**
- `discussion.tex:25` — "the high-complexity RE subset (n=81) yields substantially stronger correlations (Voting ρ=0.630, SJ ρ=0.502)"
- 这个 n=81 的子集在 experiments.tex 中从未定义或引入。读者无法知道这是什么子集、如何划分。
- **建议**: 在 experiments.tex 的 capability stratification 段落中定义此子集（如 "instances with ≥3 relation triples"），或从 discussion 中删除。

**H5. Limitations 引用了论文中未呈现的 LR 分析**
- `limitations.tex:8` — "Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound."
- 论文正文没有任何地方展示 logistic regression 的结果。Framing 记录了 exp_016 的 LR ensemble（AUROC 0.666），但这些数据没有写进 paper。
- **建议**: 要么在 experiments 中加入 LR ensemble 分析，要么从 limitations 中删除此引用。

**H6. Discussion 引用无表格支撑的 AUROC=0.735**
- `discussion.tex:7` — "its ensemble with voting reaches AUROC=0.735"
- 这个数字不在任何表格中。Table 1 没有 ensemble 行；Table 2 只报告 F1 不报告 AUROC。
- **建议**: 在 Table 1 增加 ensemble 行，或将此数字移至有对应数据支撑的位置。

**H7. Fisher's z-test 比较对象不明确**
- `experiments.tex:153` — "Fisher's z-test on ρ_SJ yields z=2.31, p=0.021"
- 没有说明这是比较 NER SJ ρ vs RE SJ ρ，还是其他对。读者无法理解 z-test 在检验什么假设。
- **建议**: 改为 "Fisher's z-test comparing SJ ρ between NER (0.357) and RE (0.211) yields z=2.31, p=0.021"。

**H8. Abstract 的 Claim 2 与正文 Framing 脱节**
- Abstract line 4 说 "only log-probability helps on relation extraction (+2.3 pp)"。
- 但 framing 的 exp_016_rerun_1024 数据显示 "RE: greedy 0.4042 > logprob 0.3948"（greedy 赢）。Table 2 显示 LP=0.397 > greedy=0.374（LP 赢 2.3pp）。
- 这意味着 gold-filtered 管道 vs 原始数据的 RE selection 结论完全相反。如果 gold-filtering 改变了核心 claim 的方向，需要显式说明。
- **建议**: 验证 RE selection +2.3pp 来自哪个实验管道，确认与 gold-filtered 约束一致。

---

### LOW（可选改进）

**L1. 术语不一致：entity voting / Voting Confidence / Voting Conf.**
- Abstract 用 "entity voting"，Table 1 用 "Voting Conf."，experiments 正文用 "Voting Confidence"，discussion/conclusion 用 "entity voting"。
- **建议**: 统一为一个术语，其他地方首次出现时加括号别名。

**L2. CoNLL oracle headroom数据仅在正文中，无表格支撑**
- `experiments.tex:88-89` — "+4.2 pp (Qwen) and +1.8 pp (LLaMA)" — 这些数字不在 Table 2（只有 SciERC）也不在其他表格中。
- **建议**: 在 appendix 增加 CoNLL selection 表，或注明 "(data in Appendix Table X)"。

**L3. Ensemble 定义模糊**
- Table 2 叫 "Ensemble (SJ+Vot.)"，Discussion 叫 "its ensemble with voting"，Limitations 提到 "logistic regression proxy"。读者不清楚 ensemble 是 SJ+Voting 的简单组合还是 LR 训练的加权组合。
- **建议**: 在 method section 中明确定义 ensemble 的计算方式。

**L4. Introduction 末尾缺少对 Discussion/Conclusion/Limitations 的路线引用**
- `introduction.tex:48-51` 只提到 §Method, §Experiments, §Related Work，漏掉了 §Discussion, §Conclusion, §Limitations。
- **建议**: 补全或改为 "The remainder of this paper is organized as follows..." 只提主要 section。

**L5. N-scaling 表格数据与正文引用有细微差异**
- `experiments.tex:202` 说 N=16 SJ ρ = "0.412±0.025 (three seeds: 0.428, 0.424, 0.384)"
- `n_scaling_appendix_tables_44b000.tex` Table 1 显示 N=16 SJ NER = 0.4105
- 0.412 vs 0.4105 — 可能是四舍五入差异，但应统一精度。
- **建议**: 正文使用与附录表格完全一致的数值。

---

### 总体评估：**FAIL**

核心原因：
1. **结构不完整** — Method section 缺失，全部 4 个 figure 缺失，编译后将产生大量 "??" 引用
2. **关键证据缺失** — 4B scale ablation（framing 标记为 RESOLVED 的 R14 回应）和 free-form ablation（Story Spine 核心支柱）均未写入正文
3. **约束违反** — RE preliminary 标注缺失

现有文本质量较高——叙事逻辑清晰、claims 与 evidence 在已呈现的范围内对齐良好、related work 覆盖全面。但结构性缺失使论文无法以当前状态提交。

**建议修复优先级**：C1 (method) → C2 (figures) → C3 (4B ablation) → H1 (free-form discussion) → C4 (preliminary markers) → C5 (duplicate labels) → 其余 HIGH items。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_r9_narrative_coherence_20260516T010130"
}
```

</details>

---
