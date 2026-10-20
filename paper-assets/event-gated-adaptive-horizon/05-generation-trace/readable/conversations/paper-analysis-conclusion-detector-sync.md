# paper analysis conclusion detector sync

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_analysis-conclusion-detector-sync_20260517T180715.jsonl`
- **Structured JSON:** [`aa5e8c95228652439792.json`](../../sessions/aa/aa5e8c95228652439792.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-17T18:08:43.260965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T18:08:43.261334+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T18:08:43.261511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T18:08:43.261649+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T18:08:43.261770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T18:08:43.261911+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T18:08:43.262054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T18:08:43.262178+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T18:08:43.262322+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T18:08:43.262450+00:00_

docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
artifacts/analysis/detector_table.tex
docs/paper/main.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/introduction.tex
paper/tables/nve_sensitivity_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
docs/paper/sections/related_work.tex
docs/paper/sections/methodology.tex
docs/paper/sections/results.tex
docs/paper/sections/appendix.tex
docs/paper/sections/analysis.tex
docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T18:08:43.262594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/",
  "description": "List project directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/",
    "description": "List project directory contents"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T18:08:43.262727+00:00_

total 564
drwxr-xr-x 10 ubuntu ubuntu   4096 May 17 17:09 .
drwxrwxr-x  5 ubuntu ubuntu   4096 May 13 01:02 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 13 01:02 .claude
-rw-r--r--  1 ubuntu ubuntu  16440 May 17 18:04 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu      0 May 13 01:05 ROADMAP.lock
-rw-------  1 ubuntu ubuntu   4402 May 17 17:09 ROADMAP.md
drwxr-xr-x 38 ubuntu ubuntu   4096 May 17 14:54 artifacts
drwxr-xr-x  2 ubuntu ubuntu  45056 May 17 15:20 checkpoints
-rw-r--r--  1 ubuntu ubuntu      0 May 13 01:05 decisions.lock
-rw-------  1 ubuntu ubuntu  96665 May 17 17:05 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 13 02:35 docs
-rwxr-xr-x  1 ubuntu ubuntu      0 May 13 02:07 dream_registry.lock
-rw-------  1 ubuntu ubuntu   5148 May 16 18:04 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   5153 May 16 18:04 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu      0 May 15 11:55 experiment_plan.lock
-rw-------  1 ubuntu ubuntu  10057 May 15 14:52 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  62316 May 16 20:27 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 13 01:07 logs
-rw-r--r--  1 ubuntu ubuntu   3554 May 17 14:02 memory.md
-rw-r--r--  1 ubuntu ubuntu      0 May 16 22:02 mistakes.lock
-rw-------  1 ubuntu ubuntu  10544 May 17 16:00 mistakes.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 16 05:14 paper
-rw-r--r--  1 ubuntu ubuntu  36297 May 17 17:04 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu      0 May 15 11:03 paper_provenance.lock
-rw-------  1 ubuntu ubuntu  26588 May 15 19:22 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu      0 May 13 02:09 registry.lock
-rw-------  1 ubuntu ubuntu 149544 May 17 15:20 registry.yaml
-rw-r--r--  1 ubuntu ubuntu   4109 May 17 14:55 report.md
drwxr-xr-x  2 ubuntu ubuntu   4096 May 16 11:08 scripts
-rwxr-xr-x  1 ubuntu ubuntu      0 May 13 01:02 study_status.lock
drwxr-xr-x  3 ubuntu ubuntu   4096 May 17 18:04 task_context
-rw-r--r--  1 ubuntu ubuntu  26838 May 15 10:17 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T18:08:43.262911+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T18:08:43.263076+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The results establish three insights that frame CIVO as a structural vulnerability of flat temporal conditioning in imagination-based RL. Full mechanistic analysis, gradient decomposition, and seed-divergence discussion are in Appendix~\ref{sec:appendix_analysis}.
5	
6	\paragraph{CIVO mechanism.}
7	The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning (Table~\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes and the actor exploits, creating a four-stage feedback loop analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced.  Full-pathway SGS (exp\_018) targets the gradient channel that maintains this bias, yet yields mixed results (50\% collapse prevention), indicating that CIVO involves mechanisms beyond gradient-mediated co-adaptation of the temporal embedding.
8	
9	\paragraph{Gradient decomposition and intervention design.}
10	\label{sec:gradient_evolution_main}
11	Gradient decomposition (Figure~\ref{fig:gradient_decomp}, Table~\ref{tab:gradient_decomposition}) reveals a non-obvious structure: the reward head provides the largest gradient contribution to $e_{\Delta t}$ (49.0\% at 55K, 38.1\% at 112K), yet reward-only SGS (exp\_016e) is functionally insufficient (NVE $10.42\times$, collapse).  The observation decoder channel contributes the smallest share (16.3\% at 55K, 21.5\% at 112K) but encodes the critical $\dt$-specific spatial predictions that generate the RSSM fidelity gap.  Full-pathway SGS, which removes observation decoder \emph{and} reward gradients from $e_{\Delta t}$, \sgsclaim{} (seed~1: peak NVE $\sgsnve{}\times$, eval \sgseval{}; seed~2: collapsed, eval 40.8).  The 50\% prevention rate confirms that the observation decoder gradient pathway is causally involved but reveals that CIVO's feedback loop has redundant mechanisms not fully captured by grad
…[truncated 4233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T18:08:43.263228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T18:08:43.263382+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3 across two continuous-control environments, identifying the combination of trained $\dt$-embedding and multi-rate data exposure as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:
5	
6	\begin{enumerate}[nosep,leftmargin=*]
7	\item Every variable-rate imagination configuration degrades relative to the $\dt{=}1$ baseline, with degradation scaling monotonically with $\dt$.
8	\item A normalized value-to-eval threshold of $\nve \geq 1.5\times$ (35K+ window) achieves 11/12 CIVO classification ($n{=}12$, 91.7\%), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The combination of trained $\dt$-embedding and multi-rate data exposure is the causal factor; unexposed, frozen, or removed embeddings prevent overestimation.
9	\item The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning, providing the systematic bias that drives critic overestimation.
10	\item The same CIVO trigger produces stochastic downstream outcomes (full collapse and transient CIVO with self-correction) across seeds of identical configurations.
11	\item Restricting imagination to $\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy), demonstrating that the trained $\dt$-embedding creates vulnerability through multiple mechanisms.
12	\item A lightweight online detector that monitors the dynamics of the value-to-evaluation ratio identifies CIVO onset with 100\% sensitivity across three positive cases, with predictive detection (alert before performance degradation) in two of three. A timing guideline ($<$70K steps = high confidence) separates genuine CIVO from late-stage false positives.
13	\end{enumerate}
14	
15	The contrast 
…[truncated 2440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T18:08:43.263534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T18:08:43.263662+00:00_

1	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance, despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through factorial diagnostics on two continuous-control tasks (Walker Walk, Cheetah Run), we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. This mechanism universally degrades performance to below 30\% of baseline across all three tested seeds ($n{=}3$), with two progressing toward full collapse and one self-correcting to a stable but degraded state. Gradient decomposition reveals that despite the reward head providing the largest gradient contribution (38--49\%), the observation decoder channel (16--22\%) carries the critical $\Delta t$-specific spatial information that drives the fidelity gap. Full-pathway gradient stopping partially prevents CIVO but succeeds in only 50\% of cases; this exposes additional mechanisms beyond gradient-mediated co-adaptation. A lightweight online detector that monitors value-to-evaluation ratio dynamics identifies CIVO onset with 100\% sensitivity (3/3 cases) and provides predictive warning before performance degradation in 2/3 cases, which supports early intervention without a reference baseline. The contrast with MPC-based methods identifies the feedback architecture (imagination-based bootstrapping versus re-planning) as the structural factor that transforms manageable model imprecision into pathological value dynamics.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T18:08:43.263793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T18:08:43.263964+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the causal factor within the factorial design tested. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A $\nve \geq 1.5\times$ threshold (35K+ window) achieves 11/12 CIVO classification ($n{=}12$, single environment), with one non-CIVO false positive, a failure mode analogous to delusional bias \citep{lu2018nondelusional} that arises from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals a non-obvious mechanism: the reward head contributes the largest gradient share (38--49\%) but does not encode $\dt$-specific structural information, while the observation decoder channel (16--22\%) carries the critical spatial predictions that drive the RSSM fidelity gap. Reward-only gradient stopping fails (NVE $10.42\times$) despite targeting the largest pathway; full-pathway SGS that removes observation decoder gradients from the temporal embedding \sgsclaim{} (eval \sgseva
…[truncated 1256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T18:08:43.264137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T18:08:43.264422+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 17 configurations in Table~\ref{tab:complete_results}.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\midrule
22	\rowcolor{gray!15}
23	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
24	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
25	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
26	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
27	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
28	\midrule
29	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
30	\rowcolor{gray!15}
31	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\times$ & Collapsed \\
32	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
33	\bottomrule
34	\end{tabula
…[truncated 20430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T18:08:43.264678+00:00_

所有四个文件已读取。现在对比 results.tex 中的最新数据逐一检查。

**最新正确数据（来自 results.tex）：**
- detector 验证：n=11 runs
- TPR=3/3 (1.00)，FPR=2/8 (0.25)
- 三环境：Walker Walk, Cheetah Run, PickCube-v1
- NVE threshold 分类：11/12, AUROC=0.926, n=12

---

### 检查结果

**analysis.tex** — 无需修改
- Line 23: "perfect sensitivity (3/3 true positives) with a false positive rate of 2/8 (25%)" ✓
- Line 23: "calibrated on eleven runs across three environments" ✓
- 无 n=10、2/7、"two environments" 等旧数据

**conclusion.tex** — 无需修改
- Line 8: "11/12 CIVO classification ($n{=}12$, 91.7%)" — NVE threshold 分类，不是 detector，数据正确 ✓
- Line 12: "100\% sensitivity across three positive cases" ✓
- Line 18: "calibrated on eleven runs across three environments" ✓
- Line 4: "across two continuous-control environments" — 这指的是 factorial diagnostic（Walker + Cheetah，均为 DMC 连续控制），不是 detector 验证范围，准确 ✓

**abstract_body.tex** — 无需修改
- "100\% sensitivity (3/3 cases)" ✓
- "predictive warning before performance degradation in 2/3 cases" ✓
- 无具体 n= 或 FPR 数字

**introduction.tex** — 无需修改
- Line 8: "achieves 100\% sensitivity for CIVO detection (3/3 cases) with predictive warning before performance degradation in 2/3 cases" ✓
- 无 n=10、FPR=2/7 等旧数据

---

### 额外发现：results.tex 内部不一致

results.tex Line 182 仍写着 `$n{=}10$ runs`：
> "we retain $0.1$ to avoid overfitting to $n{=}10$ runs"

但同一文件 Line 185 说 "eleven runs"，Line 227 说 "eleven runs across three environments"。这是 results.tex 内部的残留不一致，应改为 `$n{=}11$`。需要修复吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_analysis-conclusion-detector-sync_20260517T180715"
}
```

</details>

---
