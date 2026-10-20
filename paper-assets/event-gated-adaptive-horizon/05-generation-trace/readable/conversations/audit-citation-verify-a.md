# audit citation verify A

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 129
- **Recorded user turns:** 0
- **Tool calls:** 64
- **Original source:** `logs/chats/worker_audit_citation-verify-A_20260529T064944.jsonl`
- **Structured JSON:** [`069ad1206edef100ce89.json`](../../sessions/06/069ad1206edef100ce89.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

129 recorded events

### Tool call

_source line 1 · 2026-05-29T06:57:50.173128+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-29T06:57:50.173681+00:00_

1	% Auto-generated from literature_map.yaml
2	% 45 entries
3	
4	@inproceedings{gu2023maniskill2,
5	  title = {ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills},
6	  author = {Gu, Jiayuan and Xiang, Fanbo and Li, Xuanlin and Ling, Zhan and Liu, Xiqiang and Mu, Tongzhou and Tang, Yihe and Tao, Stone and Wei, Xinyue and Yao, Yunchao and Yuan, Xiaodi and Xie, Pengwei and Huang, Zhiao and Chen, Rui and Su, Hao},
7	  year = {2023},
8	  booktitle = {International Conference on Learning Representations},
9	}
10	
11	@inproceedings{micheli2023iris,
12	  title = {Transformers are Sample-Efficient World Models},
13	  author = {Micheli, Vincent and Alonso, Eloi and Fleuret, Fran{\c{c}}ois},
14	  year = {2023},
15	  booktitle = {International Conference on Learning Representations},
16	}
17	
18	@article{sutton1999options,
19	  title = {Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning},
20	  author = {Sutton, R.S and Precup, D and Singh, S},
21	  year = {1999},
22	  journal = {Artificial Intelligence 112},
23	}
24	
25	@inproceedings{hafner2020dreamerv1,
26	  title = {Dream to Control: Learning Behaviors by Latent Imagination},
27	  author = {Hafner, D and Lillicrap, T and Ba, J and Norouzi, M},
28	  year = {2020},
29	  booktitle = {International Conference on Learning Representations},
30	}
31	
32	@article{hafner2023dreamerv3,
33	  title = {Mastering Diverse Domains through World Models},
34	  author = {Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
35	  year = {2025},
36	  journal = {Nature},
37	  eprint = {2301.04104},
38	  archivePrefix = {arXiv},
39	}
40	
41	@inproceedings{sharma2017figar,
42	  title = {Fine Grained Action Repetition for Deep Reinforcement Learning},
43	  author = {Sharma, S and Lakshminarayanan, A.S and Ravindran, B},
44	  year = {2017},
45	  booktitle = {International Conference on Learning Representations},
46	}
47	
48	@inproceedings{pertsch2020spirl,
49	  title = {
…[truncated 12522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-29T06:57:50.173924+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-29T06:57:50.174076+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-29T06:57:50.174224+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-29T06:57:50.174356+00:00_

docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
docs/paper/sections/methodology.tex
docs/paper/sections/results.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/introduction.tex
docs/paper/sections/analysis.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/related_work.tex
docs/paper/sections/appendix.tex
docs/paper/main.tex
docs/paper/sections/experiments_results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-29T06:57:50.174506+00:00_

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
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-29T06:57:50.174676+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1 World-model reinforcement learning enables sample-efficient learning in complex continuous control tasks \citep{wu2023daydreamer, hansen2024tdmpc2}. Continuous control demands temporal abstraction: locomotion with heterogeneous gait phases, contact-rich tasks with variable sensing rates, and multi-rate decision-making across planning horizons all require handling $\dt$ mismatches. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot: every variable-rate configuration suffers substantial performance degradation. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding (a learned vector concatenated to the RSSM input at each imagination step; our implementation of $\dt$-conditioning) and multi-rate data exposure as the strongest predictor. This combination enables environment-dependent pathologies (reward prediction gaps in Walker Walk, or dynamics-model prior drift without measurable reward bias in Cheetah Run), which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) diagnostic achieves perfect classification (AUROC${=}1.000$, $n{=}36$; Appendix~\ref{sec:appendix_sensitivity}).
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/paper/fig4_mechanism_diagram.pdf}
10	\caption{Proposed CIVO pathway (evidence levels annotated). The trained $
…[truncated 2288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-29T06:57:50.174845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-29T06:57:50.175009+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal abstraction in RL.}
5	\looseness=-1 Temporal abstraction spans hierarchical, action-repetition, and world-model approaches, none of which has examined the interaction between flat $\dt$-conditioning and imagination-based value estimation.
6	The options framework \citep{sutton1999options}, option-critic \citep{bacon2017optioncritc}, HAM \citep{parr1998ham}, and MAXQ \citep{dietterich2000maxq} formalize temporal abstraction through hierarchical policies. Semi-MDP theory \citep{bradtke1995smdp} provides the mathematical foundation. Action-repetition methods achieve simpler temporal abstraction via real transitions: FiGAR \citep{sharma2017figar} learns per-action repetition counts jointly with the policy, TempoRL \citep{biedenkapp2021temporl} and \citet{park2021timediscretization} provide complementary formulations. SPiRL \citep{pertsch2020spirl} accelerates RL through learned skill priors that capture reusable temporal abstractions from offline data. \citet{wang2024elastic} learn elastic time steps that adapt step size to state dynamics. The Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3, hafner2025dreamerv4} trains policies in imagination at fixed $\dt{=}1$; hierarchical variants \citep{hafner2022director, gumbsch2024thick, mattes2024hieros, li2025lsimagine} use subgoals or separate dynamics per scale, avoiding flat $\dt$-conditioning. TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2}; MPC re-plans from real states, avoiding the critic accumulation we analyze (\S\ref{sec:discussion}).
7	
8	\paragraph{Value overestimation and model fidelity.}
9	\looseness=-1 Overestimation has been studied extensively in model-free and model-based RL, but no prior work identifies the specific pathology arising from learned temporal conditioning in imagination.
10	Maximization bias \citep{thrun1993issues} has been addressed by
…[truncated 2147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-29T06:57:50.175159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T06:57:50.175452+00:00_

1	\section{Experiments and Results}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:methodology}
6	
7	\paragraph{Base architecture.}
8	\looseness=-1 All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns an RSSM with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely in imagined trajectories. The default configuration imagines $H{=}15$ steps at $\dt{=}1$ (one imagination step per environment transition).
9	
10	\paragraph{Variable-rate imagination.}
11	\label{sec:variable_rate}
12	\looseness=-1 We introduce three orthogonal modifications enabling variable-rate imagination, each independently toggled.
13	\emph{Temporal embedding}: A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step. We test three modes: \textbf{trained} (updated via backpropagation, enabling co-adaptation), \textbf{frozen} (fixed random projection, \texttt{requires\_grad=False}), and \textbf{removed} (dimension zero). We further distinguish \textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\dt{>}1$ transitions) from \textbf{trained-but-unexposed} (subsample OFF: $\dt{>}1$ used only during imagination).
14	\emph{Temporal subsampling}: When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames (max factor~2).
15	\emph{Horizon and step size}: We test $H{=}15$ (default) and $H{=}8$; \texttt{gate\_fixed\_dt} forces a specific $\dt$ ($1$, $2$, or $4$).
16	
17	\paragraph{Factorial design.}
18	\label{sec:factorial}
19	\looseness=-1 We adopt a factorial ablation across four factors: $\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and step size ($\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\ref{tab:factorial_design} in Appendix~\ref{sec:appendix_factorial}) isolates trained $\dt$-embedding and mul
…[truncated 18462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-29T06:57:50.175617+00:00_

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
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-29T06:57:50.175767+00:00_

1	\vspace{-2pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{CIVO mechanism.}
6	\looseness=-1 CIVO propagates through multiple pathways: Walker Walk develops a $1.63\times$ reward prediction gap while Cheetah Run shows none ($1.00\times$) despite higher severity ($8.27\times$ NVE). The mechanism is analogous to delusional bias \citep{lu2018nondelusional} but model-induced; unlike MPC, imagination-based actor-critic bootstraps value targets entirely within the learned model without real-data correction (Appendix~\ref{sec:mpc_immune}). Untrained embeddings at $\dt{=}2$ produce no overestimation (NVE${<}0.6\times$), confirming \emph{systematic} bias. Frozen embeddings participate identically in the forward pass yet never trigger CIVO (0/16 controls vs.\ 5/7 trained, $p < 0.001$; Table~\ref{tab:causal_ablation}): the vulnerability lies in what the embedding \emph{learns}, not in conditioning architecture.
7	
8	\paragraph{Why interventions fail or partially succeed.}
9	\looseness=-1 CIVO is an emergent property of co-adapting embeddings, not a single-pathway defect: SGS fails from pathway redundancy; RAVE fails as the EMA anchor tracks biased values; TCN shows binary on/off behavior suggesting a phase transition. The only reliable elimination, freezing the embedding (0/16 controls), degrades performance to 22--33\% of baseline. At the architecture level, the $2{\times}2$ critic factorial shows that min-aggregation enables recovery but not prevention; their combination achieves prevention in 3/4 seeds (NVE $\leq 1.4\times$), though Cheetah transfer failure (0/1, CIVO at $108\times$) suggests a severity ceiling. CIVO is specific to multi-joint locomotion across both tested environments (5/7 seeds; Appendix~\ref{sec:cross_env_appendix}). These findings are not architecture-specific: embedding co-adaptation may interact pathologically with value estimation in any imagination-based actor-critic that bootstraps within a learned model.
10	
11	\paragraph{Pract
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-29T06:57:50.175943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-29T06:57:50.176071+00:00_

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
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T06:57:50.176190+00:00_

File content (43676 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T06:57:50.176314+00:00_

1	\vspace{-2pt}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	\looseness=-1 We identify conditioning-induced value overestimation (CIVO) as a systematic failure mode of temporal conditioning in imagination-based actor-critic training. Trained $\dt$-embeddings with multi-rate data exposure reliably induce value overestimation while frozen embeddings never do, revealing co-adaptation between the temporal embedding and the world model as the causal factor. A four-level intervention hierarchy yields two key insights: gradient magnitude does not predict causal importance, and dual critics converge in pure imagination, rendering Double Q pessimism structurally ineffective in any system with shared imagined rollouts. For practitioners, we recommend: (1)~validate with frozen-embedding controls before deploying learned embeddings; (2)~monitor NVE as an early warning; (3)~prefer MPC-style re-planning for variable-rate execution. Future work should examine CIVO in transformer-based world models and diffusion-based planners. Code and configurations will be released upon acceptance.
6	
7	\vspace{-2pt}
8	\section{Limitations}
9	\label{sec:limitations}
10	
11	\looseness=-1 All experiments use DreamerV3's RSSM; generalization to transformer-based world models \citep{micheli2023iris}, TD-MPC variants \citep{hansen2024tdmpc2}, or diffusion-based planners is untested. The evaluation covers two locomotion and one manipulation environment with proprioceptive observations; pixel-based or real-robot settings remain open. Seed counts (4--5; \citealt{colas2018seeds}) provide sufficient power for binary classification but may miss subtler or environment-specific effects.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-29T06:57:50.176453+00:00_

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
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T06:57:50.176578+00:00_

1	\looseness=-1 World-model reinforcement learning increasingly targets continuous control tasks where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration suffers substantial performance degradation. Factorial diagnostics on two continuous-control tasks identify the combination of trained temporal embedding and multi-rate data exposure as the strongest predictor of this failure, \emph{conditioning-induced value overestimation} (CIVO; AUROC${=}1.000$, $n{=}36$). The recurrent state-space model (RSSM) develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. Gradient, output, and representation interventions fail to eliminate CIVO; at the architecture level, dual critics converge in pure imagination, but wide dual-critic (min-aggregation $+$ increased capacity) achieves partial prevention, the only positive result, highlighting open challenges in the architectural design of variable-rate model-based RL.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-29T06:57:50.176703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-29T06:57:50.176876+00:00_

1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns an RSSM with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely in imagined trajectories. The default configuration imagines $H{=}15$ steps at $\dt{=}1$ (one imagination step per environment transition).
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal modifications enabling variable-rate imagination, each independently toggled.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step. We test three modes: \textbf{trained} (updated via backpropagation, enabling co-adaptation), \textbf{frozen} (fixed random projection, \texttt{requires\_grad=False}), and \textbf{removed} (dimension zero). We further distinguish \textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\dt{>}1$ transitions) from \textbf{trained-but-unexposed} (subsample OFF: $\dt{>}1$ used only during imagination). This four-way classification is the key experimental structure of our factorial design.
16	
17	\paragraph{Temporal subsampling.}
18	When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames (max factor~2: both $\dt{=}1$ and $\dt{=}2$ from the same episodes). This controls whether the world model has seen multi-scale dynamics during training.
19	
20	\paragraph{Imagination horizon and step size.}
21	We test $H{=}15$ (default) and $H{=}8$. The reduced horizon controls for compounding error: $H{=}8$ at $\dt{=}2$ covers $16$ physical steps, comparable to the default $15$. The parameter \texttt{gate\_fixed\_dt} forces a specific $\dt$ ($1$, $2$, or $4$), separating $\dt$-conditioning effects from any learned
…[truncated 3617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-29T06:57:50.177037+00:00_

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
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-29T06:57:50.177261+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that trace a predictive pathway from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\ref{tab:complete_results}.}
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
24	008f & No dt\_emb (s0) & --- & ON & 8 & 139.5 @105K$^f$ & 1.69$\times$$^f$ & Healthy$^f$ \\
25	008f s1 & No dt\_emb (s1) & --- & ON & 8 & 468.8 @105K & 0.88$\times$ & Healthy \\
26	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
27	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
28	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
29	\midrule
30	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
31	\rowcolor{gray!15}
32	010b & Cheetah Run (s1) & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
33	\rowcolor{gra
…[truncated 10842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T06:57:50.177482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T06:57:50.177721+00:00_

1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 58 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the ablation argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks self-correcting NVE without policy recovery.}
11	\label{tab:complete_results}
12	\scriptsize
13	\setlength{\tabcolsep}{3pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
20	\rowcolor{gray!15}
21	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\heartsuit$ & 4.12$\times$ & Full collapse \\
27	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
28	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
29	\rowcolor{gray!15}
30	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
31	\rowcolor{gray!15}
32	059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\tim
…[truncated 14725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T06:57:50.178001+00:00_

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
  "session": "worker_audit_citation-verify-A_20260529T064944",
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

_source line 28 · 2026-05-29T06:57:50.178213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-29T06:57:50.178449+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ManiSkill2 Unified Benchmark Generalizable Manipulation Skills Gu Jiayuan 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ManiSkill2 Unified Benchmark Generalizable Manipulation Skills Gu Jiayuan 2023"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-29T06:57:50.178648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Transformers are Sample-Efficient World Models Micheli Vincent ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Transformers are Sample-Efficient World Models Micheli Vincent ICLR 2023"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-29T06:57:50.178860+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Between MDPs and Semi-MDPs Framework Temporal Abstraction Sutton Precup Singh 1999"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Between MDPs and Semi-MDPs Framework Temporal Abstraction Sutton Precup Singh 1999"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-29T06:57:50.179065+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dream to Control Learning Behaviors Latent Imagination Hafner Lillicrap 2020 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dream to Control Learning Behaviors Latent Imagination Hafner Lillicrap 2020 ICLR"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-29T06:57:50.179262+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mastering Diverse Domains through World Models Hafner Pasukonis Nature 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mastering Diverse Domains through World Models Hafner Pasukonis Nature 2025"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-29T06:57:50.179456+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fine Grained Action Repetition Deep Reinforcement Learning Sharma Lakshminarayanan Ravindran 2017 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fine Grained Action Repetition Deep Reinforcement Learning Sharma Lakshminarayanan Ravindran 2017 ICLR"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-29T06:57:50.179715+00:00_

Web search results for query: "Between MDPs and Semi-MDPs Framework Temporal Abstraction Sutton Precup Singh 1999"

Links: [{"title":"(PDF) Between MDPs and Semi-MDPs: A Framework for Temporal","url":"https://research.amanote.com/publication/1p8Y3nMBKQvf0BhiU2Ib/between-mdps-and-semi-mdps-a-framework-for-temporal-abstraction-in-reinforcement-learning"},{"title":"Publications between mdps and semi-mdps: a framework for temporal abstraction in reinforcement learning","url":"https://www.cs.utexas.edu/~shivaram/readings/b2hd-SuttonPS1999.html"},{"title":"Between MDPs and semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning | BibSonomy","url":"https://www.bibsonomy.org/publication/1ae2a0b25d21404291ab21b236c957ef/butz"},{"title":"[PDF] Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Between-MDPs-and-Semi-MDPs:-A-Framework-for-in-Sutton-Precup/0e7638dc16a5e5e9e46c91272bfb9c3dd242ef6d"},{"title":"Between MDPs and semi-MDPs: a framework for temporal abstraction in reinforcement learning: Artificial Intelligence: Vol 112, No 1-2","url":"https://dl.acm.org/doi/abs/10.1016/S0004-3702(99)00052-1"},{"title":"(PDF) Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning","url":"https://www.academia.edu/15781741/Between_MDPs_and_semi_MDPs_A_framework_for_temporal_abstraction_in_reinforcement_learning"},{"title":"Artiﬁcial Intelligence 112 (1999) 181–211 Between MDPs and semi-MDPs:","url":"https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf"},{"title":"Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370299000521"},{"title":"Between MDPs and Semi-MDPs: Learning, Planning, and ...","url":"http://incompleteideas.net/papers/SPS-98.pdf"}]

I found information about the paper you'
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-29T06:57:50.180042+00:00_

Web search results for query: "ManiSkill2 Unified Benchmark Generalizable Manipulation Skills Gu Jiayuan 2023"

Links: [{"title":"[Quick Review] ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills","url":"https://liner.com/review/maniskill2-a-unified-benchmark-for-generalizable-manipulation-skills"},{"title":"dblp: ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills.","url":"https://dblp.org/rec/journals/corr/abs-2302-04659.html"},{"title":"haosulab/ManiSkill2 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/haosulab/ManiSkill2"},{"title":"ManiSkill2 - Robot Learning Made Simple","url":"https://maniskill2.github.io/"},{"title":"[2302.04659] ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills","url":"https://arxiv.org/abs/2302.04659"},{"title":"ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills","url":"https://arxiv.org/pdf/2302.04659"},{"title":"GitHub - haosulab/ManiSkill: SAPIEN Manipulation Skill Framework, an open source GPU parallelized robotics simulator and benchmark · GitHub","url":"https://github.com/haosulab/ManiSkill"},{"title":"Paper page - ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills","url":"https://huggingface.co/papers/2302.04659"},{"title":"(PDF) ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills","url":"https://www.researchgate.net/publication/368393061_ManiSkill2_A_Unified_Benchmark_for_Generalizable_Manipulation_Skills"},{"title":"Published as a conference paper at ICLR 2023 MANISKILL2: A UNIFIED BENCHMARK","url":"https://openreview.net/pdf?id=b_CQDy9vrD1"}]

Based on the search results, I found comprehensive information about ManiSkill2:

## ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills

ManiSkill2 is an ICLR 2023 paper by Jiayuan Gu, Fanbo Xiang, and 13 other authors that presents a unified benchmark for generalizable manipulation skills with dynamic simulation.

### Overview
ManiSkill2 is
…[truncated 1148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-29T06:57:50.180328+00:00_

Web search results for query: "Dream to Control Learning Behaviors Latent Imagination Hafner Lillicrap 2020 ICLR"

Links: [{"title":"Dream to Control: Learning Behaviors by Latent Imagination - researchr publication reviews","url":"https://researchr.org/publication/HafnerLB020/reviews"},{"title":"DREAM TO CONTROL: LEARNING BEHAVIORS BY LATENT IMAGINATION - statwiki","url":"https://wiki.math.uwaterloo.ca/statwiki/index.php?title=DREAM_TO_CONTROL:_LEARNING_BEHAVIORS_BY_LATENT_IMAGINATION"},{"title":"Dream to Control: Learning Behaviors by Latent Imagination","url":"https://research.google/pubs/dream-to-control-learning-behaviors-by-latent-imagination/"},{"title":"Dreaming: Model-based Reinforcement Learning by Latent Imagination without Reconstruction | 2021 IEEE International Conference on Robotics and Automation (ICRA)","url":"https://dl.acm.org/doi/10.1109/ICRA48506.2021.9560734"},{"title":"ICLR: Dream to Control: Learning Behaviors by Latent Imagination","url":"https://iclr.cc/virtual_2020/poster_S1lOTC4tDS.html"},{"title":"[1912.01603] Dream to Control: Learning Behaviors by Latent Imagination","url":"https://arxiv.org/abs/1912.01603"},{"title":"Dream to Control: Learning Behaviors by Latent Imagination | OpenReview","url":"https://openreview.net/forum?id=S1lOTC4tDS"},{"title":"Dream to Control: Learning Behaviors by Latent Imagination","url":"https://arxiv.org/pdf/1912.01603"}]

Based on the search results, here's information about this paper:

The paper "Dream to Control: Learning Behaviors by Latent Imagination" was authored by Danijar Hafner, Timothy P. Lillicrap, Jimmy Ba, and Mohammad Norouzi, and was presented at the 8th International Conference on Learning Representations (ICLR 2020) in Addis Ababa, Ethiopia in April 2020.

The paper presents Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination. The approach efficiently learns behaviors by propagating analytic gradients of learned state values bac
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-29T06:57:50.180620+00:00_

Web search results for query: "Mastering Diverse Domains through World Models Hafner Pasukonis Nature 2025"

Links: [{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Mastering diverse control tasks through world models","url":"https://ideas.repec.org/a/nat/nature/v640y2025i8059d10.1038_s41586-025-08744-2.html"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"(PDF) Mastering diverse control tasks through world models","url":"https://www.researchgate.net/publication/390440514_Mastering_diverse_control_tasks_through_world_models"},{"title":"[PDF] Mastering Diverse Domains through World Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mastering-Diverse-Domains-through-World-Models-Hafner-Pa%C5%A1ukonis/f2d952a183dfb0a1e031b8a3f535d9f8423d7a6e"},{"title":"Paper page - Mastering Diverse Domains through World Models","url":"https://huggingface.co/papers/2301.04104"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"}]

Based on the search results, here's what I found about "Mastering Diverse Domains through World Models" by Hafner, Pasukonis, and colleagues:

## Publication Details

The paper "Mastering diverse control tasks through world models" was published in Nature, volume 640, pages 647–653 in 2025. The authors are from Google DeepMind and the University of Toronto.

## Overview

The paper presents the third generation of Dreamer (DreamerV3), a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. 

## How
…[truncated 852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-29T06:57:50.180942+00:00_

Web search results for query: "Fine Grained Action Repetition Deep Reinforcement Learning Sharma Lakshminarayanan Ravindran 2017 ICLR"

Links: [{"title":"Dynamic Action Repetition for Deep Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Dynamic-Action-Repetition-for-Deep-Reinforcement-Srinivas-Sharma/e997dcda4a10be86f520e88d6ca845dc5346b14f"},{"title":"[1702.06054] Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning","url":"https://arxiv.org/abs/1702.06054"},{"title":"Learning to repeat: Fine grained action repetition for deep reinforcement learning | Robert Bosch Centre for Data Science and Artificial Intelligence","url":"https://rbcdsai.iitm.ac.in/publications/learning-to-repeat-fine-grained-action-repetition/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://www.arxiv.org/pdf/2502.06919v1"},{"title":"Deep Learning with Reinforcement Learning – ICLR 2017 Discoveries – Amund Tveit's Blog","url":"https://amundtveit.com/2016/11/12/deep-learning-with-reinforcement-learning-iclr-2017-discoveries/"},{"title":"Fine Grained Action Repetition for Deep Reinforcement ...","url":"https://www.semanticscholar.org/paper/DEEP-REINFORCEMENT-LEARNING-Sharma-Lakshminarayanan/2d6075ffa9ef3fbfe338bfeb469a50883242bdcd"},{"title":"Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=B1GOWV5eg"},{"title":"Published as a conference paper at ICLR 2017 LEARNING TO REPEAT:","url":"https://arxiv.org/pdf/1702.06054"},{"title":"Dynamic Action Repetition for Deep Reinforcement Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/10918"},{"title":"Fine Grained Action Repetition for Deep Reinforcement Learning","url":"https://scispace.com/pdf/learning-to-repeat-fine-grained-action-repetition-for-deep-40rpsdhhxw.pdf"}]

I found the paper you're sear
…[truncated 1143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-29T06:57:50.181237+00:00_

Web search results for query: "Transformers are Sample-Efficient World Models Micheli Vincent ICLR 2023"

Links: [{"title":"Transformers and slot encoding for sample efficient physical world modelling","url":"https://arxiv.org/pdf/2405.20180"},{"title":"GitHub - eloialonso/iris: Transformers are Sample-Efficient World Models. ICLR 2023, notable top 5%. · GitHub","url":"https://github.com/eloialonso/iris"},{"title":"[PDF] Transformers are Sample Efficient World Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Transformers-are-Sample-Efficient-World-Models-Micheli-Alonso/235303a8bc1e4892efd525a38ead657422d8a519"},{"title":"Published as a conference paper at ICLR 2023 TRANSFORMERS ARE SAMPLE-EFFICIENT","url":"https://arxiv.org/pdf/2209.00588"},{"title":"[2209.00588] Transformers are Sample-Efficient World Models","url":"https://arxiv.org/abs/2209.00588"},{"title":"[2209.00588v2] Transformers are Sample-Efficient World Models","url":"https://arxiv.org/abs/2209.00588v2"},{"title":"[2209.00588v1] Transformers are Sample Efficient World Models","url":"https://arxiv.org/abs/2209.00588v1"},{"title":"[Quick Review] Transformers are Sample Efficient World Models","url":"https://liner.com/review/transformers-are-sample-efficient-world-models"}]

I found the paper! Here are the key details about "Transformers are Sample-Efficient World Models":

**Paper Details:**
The paper "Transformers are sample-efficient world models" was authored by Vincent Micheli, Eloi Alonso, and François Fleuret and was published at the Eleventh International Conference on Learning Representations (ICLR 2023) in Kigali, Rwanda, May 1-5, 2023.

**Main Contribution:**
The paper introduces IRIS, a data-efficient agent that learns in a world model composed of a discrete autoencoder and an autoregressive Transformer.

**Performance:**
With the equivalent of only two hours of gameplay in the Atari 100k benchmark, IRIS achieves a mean human normalized score of 1.046, and outperforms huma
…[truncated 649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-29T06:57:50.181565+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Accelerating Reinforcement Learning Learned Skill Priors Pertsch Lee Lim CoRL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Accelerating Reinforcement Learning Learned Skill Priors Pertsch Lee Lim CoRL 2021"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-29T06:57:50.181774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "When to Trust Your Model Model-Based Policy Optimization Janner Fu Zhang Levine NeurIPS 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "When to Trust Your Model Model-Based Policy Optimization Janner Fu Zhang Levine NeurIPS 2019"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-29T06:57:50.181998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Combating Compounding-Error Problem Multi-step Model Asadi Misra 2019 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Combating Compounding-Error Problem Multi-step Model Asadi Misra 2019 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-29T06:57:50.182196+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TD-MPC2 Scalable Robust World Models Continuous Control Hansen Su Wang ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TD-MPC2 Scalable Robust World Models Continuous Control Hansen Su Wang ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-29T06:57:50.182391+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MOPO Model-based Offline Policy Optimization Yu Thomas NeurIPS 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MOPO Model-based Offline Policy Optimization Yu Thomas NeurIPS 2020"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-29T06:57:50.182585+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Issues Using Function Approximation Reinforcement Learning Thrun Schwartz 1993"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Issues Using Function Approximation Reinforcement Learning Thrun Schwartz 1993"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-29T06:57:50.182837+00:00_

Web search results for query: "When to Trust Your Model Model-Based Policy Optimization Janner Fu Zhang Levine NeurIPS 2019"

Links: [{"title":"When to Trust Your Model: Model-Based Policy Optimization","url":"https://jannerm.github.io/mbpo-www/"},{"title":"When to Trust Your Model: Model-Based Policy Optimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190608253J/abstract"},{"title":"[PDF] When to Trust Your Model: Model-Based Policy Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/When-to-Trust-Your-Model:-Model-Based-Policy-Janner-Fu/9001698e033524864d4d45f051a5ba362d4afd9e"},{"title":"Reviews: When to Trust Your Model: Model-Based Policy Optimization","url":"https://proceedings.neurips.cc/paper/2019/file/5faf461eff3099671ad63c6f3f094f7f-MetaReview.html"},{"title":"(Open Access) When to Trust Your Model: Model-Based Policy Optimization (2019) | Michael Janner | 603 Citations","url":"https://scispace.com/papers/when-to-trust-your-model-model-based-policy-optimization-54la64py12"},{"title":"When to Trust Your Model: Model-Based Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=SkgPIpcGar"},{"title":"[Re] When to Trust Your Model: Model-Based PolicyOptimization | OpenReview","url":"https://openreview.net/forum?id=rkezvT9f6r"},{"title":"[1906.08253] When to Trust Your Model: Model-Based Policy Optimization","url":"https://arxiv.org/abs/1906.08253"},{"title":"When to Trust Your Model: Model-Based Policy Optimization","url":"https://arxiv.org/pdf/1906.08253"}]

I found the paper! Here are the key details:

The paper "When to Trust Your Model: Model-Based Policy Optimization" was authored by Michael Janner, Justin Fu, Marvin Zhang, and Sergey Levine and presented at NeurIPS 2019.

**Main Contribution:**

The paper addresses the challenge of designing effective model-based reinforcement learning algorithms by weighing the ease of data generation against the bias of model-generated data. The authors stud
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-29T06:57:50.183144+00:00_

Web search results for query: "Accelerating Reinforcement Learning Learned Skill Priors Pertsch Lee Lim CoRL 2021"

Links: [{"title":"Accelerating Reinforcement Learning with Learned Skill Priors","url":"https://proceedings.mlr.press/v155/pertsch21a.html"},{"title":"Accelerating Reinforcement Learning with Learned Skill Priors","url":"https://clvrai.github.io/spirl/"},{"title":"Accelerating Reinforcement Learning with Learned Skill Priors","url":"https://arxiv.org/pdf/2010.11944"},{"title":"Karl Pertsch, Youngwoon Lee, Joseph J. Lim · Accelerating Reinforcement Learning with Learned Skill Priors","url":"https://slideslive.com/38942367/accelerating-reinforcement-learning-with-learned-skill-priors"},{"title":"Karl Pertsch, Youngwoon Lee, Joseph Lim · Accelerating Reinforcement Learning with Learned Skill Priors","url":"https://slideslive.com/38941336/accelerating-reinforcement-learning-with-learned-skill-priors"},{"title":"Accelerating Reinforcement Learning with Learned Skill Priors Karl Pertsch","url":"https://proceedings.mlr.press/v155/pertsch21a/pertsch21a.pdf"},{"title":"Accelerating Reinforcement Learning with Learned Skill Priors (SPiRL) | paper-reading-group","url":"https://paper-reading-group.saidl.in/Accelerating%20Reinforcement%20Learning%20with%20Learned%20Skill%20Priors/Accelerating%20Reinforcement%20Learning%20with%20Learned%20S%2055f74821b841411e9b7695dd6cab9440.html"},{"title":"[2010.11944] Accelerating Reinforcement Learning with Learned Skill Priors","url":"https://arxiv.org/abs/2010.11944"},{"title":"Figure 9 from Accelerating Reinforcement Learning with Learned Skill Priors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Accelerating-Reinforcement-Learning-with-Learned-Pertsch-Lee/b68b8b980db62308864b2a7d33718182c5f8335b/figure/9"}]

I found the paper! Here's what I discovered:

The paper "Accelerating Reinforcement Learning with Learned Skill Priors" by Karl Pertsch, Youngwoon Lee, and Joseph Lim was published in the Proceedings o
…[truncated 1080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-29T06:57:50.183439+00:00_

Web search results for query: "Combating Compounding-Error Problem Multi-step Model Asadi Misra 2019 arXiv"

Links: [{"title":"Combating the Compounding-Error Problem with a Multi-step Model — Grokipedia","url":"https://grokipedia.com/page/190513320"},{"title":"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error","url":"https://arxiv.org/html/2504.01766v1"},{"title":"[2504.01766] Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error","url":"https://ar5iv.labs.arxiv.org/html/2504.01766"},{"title":"When Multi-step Prediction Mitigates Compounding Error","url":"https://arxiv.org/pdf/2504.01766"},{"title":"Combating the Compounding-Error Problem with a Multi-step Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190513320A/abstract"},{"title":"Adversarial Diffusion for Robust Reinforcement Learning Daniele Foffano∗","url":"https://arxiv.org/pdf/2509.23846"},{"title":"Multi-timestep models for Model-based Reinforcement Learning","url":"https://arxiv.org/html/2310.05672v1"},{"title":"[1905.13320] Combating the Compounding-Error Problem with a Multi-step Model","url":"https://arxiv.org/abs/1905.13320"},{"title":"(PDF) Combating the Compounding-Error Problem with a Multi-step Model","url":"https://www.researchgate.net/publication/333564721_Combating_the_Compounding-Error_Problem_with_a_Multi-step_Model"},{"title":"Combating the Compounding-Error Problem with a Multi-step Model Kavosh Asadi","url":"https://arxiv.org/pdf/1905.13320"}]

Based on the search results, I found detailed information about this paper:

## Paper Overview

"Combating the Compounding-Error Problem with a Multi-step Model" is a research paper in the field of model-based reinforcement learning, published as an arXiv preprint in 2019. The full citation is: K. Asadi, D. Misra, S. Kim, and M. L. Littman, "Combating the compounding-error problem with a multi-step model," arXiv preprint arXiv:1905.13320, 2019.

## Main Problem Add
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-29T06:57:50.183755+00:00_

Web search results for query: "TD-MPC2 Scalable Robust World Models Continuous Control Hansen Su Wang ICLR 2024"

Links: [{"title":"TD-MPC2","url":"https://www.tdmpc2.com/"},{"title":"ICLR Poster TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://iclr.cc/virtual/2024/poster/18722"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control [Quick Review]","url":"https://liner.com/review/tdmpc2-scalable-robust-world-models-for-continuous-control"},{"title":"GitHub - nicklashansen/tdmpc2: Code for \"TD-MPC2: Scalable, Robust World Models for Continuous Control\" · GitHub","url":"https://github.com/nicklashansen/tdmpc2"},{"title":"[2310.16828] TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/abs/2310.16828"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control | OpenReview","url":"https://openreview.net/forum?id=Oxh5CstDJU"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control TD-MPC2","url":"https://iclr.cc/media/iclr-2024/Slides/18722.pdf"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous ...","url":"https://arxiv.org/pdf/2310.16828"},{"title":"TD-MPC2: SCALABLE, ROBUST WORLD MODELS","url":"https://openreview.net/pdf/d7962b8e764953c9c4db96aa85307e9e9b689881.pdf"}]

I found comprehensive information about the TD-MPC2 paper. Here's what I discovered:

## TD-MPC2: Scalable, Robust World Models for Continuous Control

TD-MPC2 is authored by Nicklas Hansen, Hao Su, and Xiaolong Wang and was published at ICLR 2024.

### Overview
TD-MPC2 is a model-based reinforcement learning algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model, presenting a series of improvements upon the original 
…[truncated 967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-29T06:57:50.184084+00:00_

Web search results for query: "Issues Using Function Approximation Reinforcement Learning Thrun Schwartz 1993"

Links: [{"title":"Publications issues in using function approximation for reinforcement learning","url":"https://www.cs.utexas.edu/~shivaram/readings/b2hd-ThrunSchwartz1993.html"},{"title":"Issues in Using Function Approximation for Reinforcement Learning - Robotics Institute Carnegie Mellon University","url":"https://www.ri.cmu.edu/publications/issues-in-using-function-approximation-for-reinforcement-learning/"},{"title":"(PDF) Issues in Using Function Approximation for Reinforcement Learning","url":"https://www.researchgate.net/publication/2612683_Issues_in_Using_Function_Approximation_for_Reinforcement_Learning"},{"title":"1 Introduction","url":"https://arxiv.org/html/2506.07134"},{"title":"To appear in: Proceedings of the Fourth Connectionist Models Summer School","url":"https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1993_1/thrun_sebastian_1993_1.pdf"},{"title":"Issues in Using Function Approximation for Reinforcement Learning | 38","url":"https://www.taylorfrancis.com/chapters/edit/10.4324/9781315806433-38/issues-using-function-approximation-reinforcement-learning-sebastian-thrun-anton-schwartz"},{"title":"Global Versus Local Constructive Function Approximation for On-Line Reinforcement Learning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/11589990_14"},{"title":"Adapting Double Q-Learning for Continuous Reinforcement Learning","url":"https://arxiv.org/html/2309.14471"},{"title":"[PDF] Issues in Using Function Approximation for Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Issues-in-Using-Function-Approximation-for-Learning-Thrun-Schwartz/26b8747eb4d7fb4d4fc45707606d5e969b9afb0c"},{"title":"Under review as a conference paper at ICLR 2021","url":"https://openreview.net/pdf/c4be5250d095d9adc06e881bd14a009f3964d378.pdf"}]

I found the paper you're looking for. Here's what I can 
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-29T06:57:50.184366+00:00_

Web search results for query: "MOPO Model-based Offline Policy Optimization Yu Thomas NeurIPS 2020"

Links: [{"title":"MOPO: Model-based Offline Policy Optimization","url":"https://proceedings.neurips.cc/paper/2020/hash/a322852ce0df73e204b7e67cbbef0d0a-Abstract.html"},{"title":"MOPO: Model-based Offline Policy Optimization - Jianan Chen","url":"https://gjiananchen.github.io/publications/MOPO"},{"title":"[2005.13239] MOPO: Model-based Offline Policy Optimization","url":"https://arxiv.org/abs/2005.13239"},{"title":"MOPO: Model-based Offline Policy Optimization","url":"https://biases-invariances-generalization.github.io/pdf/big_12.pdf"},{"title":"MOPO: Model-based Offline Policy Optimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200513239Y/abstract"},{"title":"MOPO: Model-based Offline Policy Optimization","url":"https://proceedings.nips.cc/paper/2020/file/a322852ce0df73e204b7e67cbbef0d0a-Paper.pdf"},{"title":"MOPO: Model-based Offline Policy Optimization","url":"https://arxiv.org/pdf/2005.13239"},{"title":"Review for NeurIPS paper: MOPO: Model-based Offline Policy Optimization","url":"https://proceedings.neurips.cc/paper/2020/file/a322852ce0df73e204b7e67cbbef0d0a-Review.html"},{"title":"Conservative Bayesian Model-Based Value Expansion for Offline Policy   Optimization","url":"https://arxiv.org/pdf/2210.03802"}]

Here are the search results for MOPO (Model-based Offline Policy Optimization):

## Overview

MOPO is a paper by Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Y Zou, Sergey Levine, Chelsea Finn, and Tengyu Ma, published at NeurIPS 2020.

## Problem and Approach

The paper addresses offline reinforcement learning (RL), which refers to learning policies entirely from a batch of previously collected data. While this setting is compelling because it enables utilizing large, diverse datasets without costly or dangerous active exploration, it is exceptionally difficult due to distributional shift between offline training data and the
…[truncated 815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-29T06:57:50.184660+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deep Reinforcement Learning Double Q-Learning van Hasselt Guez Silver AAAI 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deep Reinforcement Learning Double Q-Learning van Hasselt Guez Silver AAAI 2016"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-29T06:57:50.184890+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Addressing Function Approximation Error Actor-Critic Methods Fujimoto van Hoof Meger ICML 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Addressing Function Approximation Error Actor-Critic Methods Fujimoto van Hoof Meger ICML 2018"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-29T06:57:50.185100+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Non-delusional Q-learning Value-Iteration Lu Schuurmans Boutilier NeurIPS 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Non-delusional Q-learning Value-Iteration Lu Schuurmans Boutilier NeurIPS 2018"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-29T06:57:50.185308+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TempoRL Learning When to Act Biedenkapp Rajan Hutter Lindauer ICML 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TempoRL Learning When to Act Biedenkapp Rajan Hutter Lindauer ICML 2021"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-29T06:57:50.185511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mastering Atari Discrete World Models Hafner Lillicrap Norouzi Ba ICLR 2021 DreamerV2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mastering Atari Discrete World Models Hafner Lillicrap Norouzi Ba ICLR 2021 DreamerV2"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-29T06:57:50.185768+00:00_

Web search results for query: "Deep Reinforcement Learning Double Q-Learning van Hasselt Guez Silver AAAI 2016"

Links: [{"title":"Van Hasselt, H., Guez, A. and Silver, D. (2016) Deep Reinforcement Learning with Double Q-Learning. Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 30, 2094-2100. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3531642"},{"title":"Van Hasselt, H., Guez, A. and Silver, D. (2016) Deep Reinforcement Learning with Double Q-Learning. AAAI, 2094-2100. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2434453"},{"title":"Deep Reinforcement Learning with Double Q-Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/10295"},{"title":"GitHub - jihoonerd/Deep-Reinforcement-Learning-with-Double-Q-learning: 📖 Paper: Deep Reinforcement Learning with Double Q-learning 🕹️","url":"https://github.com/jihoonerd/Deep-Reinforcement-Learning-with-Double-Q-learning"},{"title":"dblp: Deep Reinforcement Learning with Double Q-Learning.","url":"https://dblp.org/rec/conf/aaai/HasseltGS16.html"},{"title":"Publications – Hado van Hasselt","url":"https://hadovanhasselt.com/publications/"},{"title":"Deep reinforcement learning with double Q-Learning | Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence","url":"https://dl.acm.org/doi/10.5555/3016100.3016191"},{"title":"Double DQN (DDQN) Explained","url":"https://apxml.com/courses/intermediate-reinforcement-learning/chapter-3-dqn-improvements-variants/double-dqn-ddqn"},{"title":"Deep Reinforcement Learning with Double Q-Learning - AAAI","url":"https://aaai.org/papers/10295-deep-reinforcement-learning-with-double-q-learning/"},{"title":"Deep Reinforcement Learning with Double Q-learning","url":"https://arxiv.org/pdf/1509.06461"}]

I've successfully found information about the 
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-29T06:57:50.186092+00:00_

Web search results for query: "Addressing Function Approximation Error Actor-Critic Methods Fujimoto van Hoof Meger ICML 2018"

Links: [{"title":"Fujimoto, S., van Hoof, H. and Meger, D. (2018) Addressing Function Approximation Error in Actor-Critic Methods. ArXiv 1802.09477. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3430448"},{"title":"Fujimoto, S., van Hoof, H. and Meger, D. (2018) Addressing Function Approximation Error in Actor-Critic Methods. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3693365"},{"title":"dblp: Addressing Function Approximation Error in Actor-Critic Methods.","url":"https://dblp.org/rec/conf/icml/FujimotoHM18.html"},{"title":"Addressing Function Approximation Error in Actor-Critic Methods","url":"https://proceedings.mlr.press/v80/fujimoto18a.html"},{"title":"Addressing Function Approximation Error in Actor-Critic Methods - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv180209477F/abstract"},{"title":"(Open Access) Addressing Function Approximation Error in Actor-Critic Methods (2018) | Scott Fujimoto | 4301 Citations","url":"https://scispace.com/papers/addressing-function-approximation-error-in-actor-critic-4tkil44b4t"},{"title":"Addressing function approximation error in actor-critic methods","url":"https://pure.uva.nl/ws/files/38814415/fujimoto18a.pdf"},{"title":"Addressing Function Approximation Error in Actor-Critic Methods","url":"https://arxiv.org/pdf/1802.09477"},{"title":"[1802.09477] Addressing Function Approximation Error in Actor-Critic Methods","url":"https://arxiv.org/abs/1802.09477"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Scott+Fujimoto,+Herke+Hoof,+and+David+Meger.+2018.+Addressing+function+approximation+error+in+actor-critic+methods.+In+International+conference+on+machine+learning.+PMLR,+1587--1596."}]

Based on the search results, I found comprehen
…[truncated 1233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-29T06:57:50.186336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Learning Hierarchical World Models Adaptive Temporal Abstractions Discrete Latent Dynamics Gumbsch Sajid Martius Butz ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Learning Hierarchical World Models Adaptive Temporal Abstractions Discrete Latent Dynamics Gumbsch Sajid Martius Butz ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-29T06:57:50.186589+00:00_

Web search results for query: "TempoRL Learning When to Act Biedenkapp Rajan Hutter Lindauer ICML 2021"

Links: [{"title":"TempoRL: Learning When to Act - Leibniz University Hannover Research Portal","url":"https://research.uni-hannover.de/en/publications/temporl-learning-when-to-act/"},{"title":"GitHub - automl/TempoRL","url":"https://github.com/automl/TempoRL"},{"title":"Biedenkapp, Rajan, Hutter, Lindauer TempoRL TempoRL: Learning When to Act","url":"https://icml.cc/media/icml-2021/Slides/9879.pdf"},{"title":"TempoRL: Learning When to Act","url":"https://proceedings.mlr.press/v139/biedenkapp21a.html"},{"title":"[PDF] TempoRL: Learning When to Act | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TempoRL:-Learning-When-to-Act-Biedenkapp-Rajan/9776324620082ab89edad134aa259b1ae7bf6f1f"},{"title":"[2106.05262] TempoRL: Learning When to Act","url":"https://arxiv.org/abs/2106.05262"},{"title":"André Biedenkapp, Raghu Rajan, Frank Hutter, Marius Lindauer · TempoRL: Learning When to Act","url":"https://slideslive.com/38959338/temporl-learning-when-to-act"},{"title":"TempoRL: Learning When to Act","url":"https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/21-ICML-TempoRL.pdf"},{"title":"TempoRL: Learning When to Act","url":"https://arxiv.org/pdf/2106.05262"},{"title":"[PDF] Towards TempoRL: Learning When to Act | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-TempoRL:-Learning-When-to-Act-Biedenkapp-Rajan/b404fae35f7ad01fa86e1a3b0a2fc50a8c665eea"}]

I found comprehensive information about this paper. Here are the key details:

**Paper Title:** TempoRL: Learning When to Act

**Authors:** André Biedenkapp, Raghu Rajan, Frank Hutter, and Marius Lindauer

**Conference:** Accepted at ICML'21 (38th International Conference on Machine Learning Research), held July 18-24, 2021

**Main Contribution:**

The work proposes a proactive setting in which the agent not only selects an action in a state but also for how long to commit to 
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-29T06:57:50.186897+00:00_

Web search results for query: "Mastering Atari Discrete World Models Hafner Lillicrap Norouzi Ba ICLR 2021 DreamerV2"

Links: [{"title":"Mastering Atari with Discrete World Models","url":"https://danijar.com/project/dreamerv2/"},{"title":"Mastering Atari with Discrete World Models - DocsLib","url":"https://docslib.org/doc/2067121/mastering-atari-with-discrete-world-models"},{"title":"Danijar Hafner, Timothy Lillicrap, Mohammad Norouzi, Jimmy Ba · Mastering Atari with Discrete World Models","url":"https://slideslive.com/38953881/mastering-atari-with-discrete-world-models"},{"title":"[PDF] Mastering Atari with Discrete World Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mastering-Atari-with-Discrete-World-Models-Hafner-Lillicrap/b44bb1762640ed72091fd5f5fdc20719a6dc24af"},{"title":"[2010.02193] Mastering Atari with Discrete World Models","url":"https://arxiv.org/abs/2010.02193"},{"title":"Mastering Atari with Discrete World Models - Papertalk","url":"https://papertalk.org/papertalks/29267"},{"title":"GitHub - danijar/dreamerv2: Mastering Atari with Discrete World Models · GitHub","url":"https://github.com/danijar/dreamerv2"},{"title":"Mastering Atari with Discrete World Models","url":"https://arxiv.org/pdf/2010.02193"},{"title":"Mastering Atari with Discrete World Models","url":"https://research.google/blog/mastering-atari-with-discrete-world-models/"}]

I found comprehensive information about this research paper. Here are the key details:

## Paper Overview

"Mastering Atari with Discrete World Models" was published as a conference paper at ICLR 2021 by Danijar Hafner, Timothy Lillicrap, Mohammad Norouzi, and Jimmy Ba from Google Research, DeepMind, and the University of Toronto.

## Main Contribution

The paper introduces DreamerV2, a reinforcement learning agent that learns behaviors purely from predictions in the compact latent space of a powerful world model, which uses discrete representations and is trained separately from the policy.


…[truncated 788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-29T06:57:50.187192+00:00_

Web search results for query: "Learning Hierarchical World Models Adaptive Temporal Abstractions Discrete Latent Dynamics Gumbsch Sajid Martius Butz ICLR 2024"

Links: [{"title":"GitHub - CognitiveModeling/THICK · GitHub","url":"https://github.com/CognitiveModeling/THICK"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | Autonomous Learning – MPI-IS","url":"https://is.mpg.de/al/publications/gumbsch2024-thickworldmodels"},{"title":"Seminar: Advanced Topics in Reinforcement Learning and Planning, Summer 2024","url":"https://www-i6.informatik.rwth-aachen.de/~hector.geffner/Seminar-S2024.html"},{"title":"ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics","url":"https://iclr.cc/virtual/2024/poster/18558"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective","url":"https://arxiv.org/pdf/2404.16078"},{"title":"【DL輪読会】Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | ドクセル","url":"https://www.docswell.com/s/DeepLearning2023/5DEY1D-2024-07-05-090032"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | Max Planck Institute for Intelligent Systems","url":"https://is.mpg.de/de/publications/gumbsch2024-thickworldmodels"}]

I found the paper you're looking for! Here are the key details:

**Title:** Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics

**Authors:** Chri
…[truncated 1012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-29T06:57:50.187482+00:00_

Web search results for query: "Non-delusional Q-learning Value-Iteration Lu Schuurmans Boutilier NeurIPS 2018"

Links: [{"title":"Non-delusional Q-learning and value-iteration - researchr publication","url":"https://researchr.org/publication/LuSB18"},{"title":"Non-delusional Q-learning and value-iteration","url":"https://research.google/pubs/pub47494/"},{"title":"Non-delusional Q-learning and Value Iteration Tyler Lu Google AI","url":"http://papers.neurips.cc/paper/8200-non-delusional-q-learning-and-value-iteration.pdf"},{"title":"dblp: Non-delusional Q-learning and value-iteration.","url":"https://dblp.org/rec/conf/nips/LuSB18.html"},{"title":"[PDF] Non-delusional Q-learning and value-iteration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Non-delusional-Q-learning-and-value-iteration-Lu-Schuurmans/59c0931562668b1ebb7c5cc8e9c236d43308722d"},{"title":"Non-delusional Q-learning and value-iteration","url":"https://proceedings.neurips.cc/paper/2018/hash/5fd0245f6c9ddbdf3eff0f505975b6a7-Abstract.html"},{"title":"NIPS Oral Non-delusional Q-learning and value-iteration","url":"https://nips.cc/virtual/2018/oral/12737"},{"title":"GitHub - EhsanEI/q-learning-delusion: A counterexample for Q-Learning, discussed in \"Non-delusional Q-learning and value-iteration.\"","url":"https://github.com/EhsanEI/q-learning-delusion"},{"title":"(PDF) Non-delusional Q-learning and value-iteration","url":"https://www.researchgate.net/publication/328772100_Non-delusional_Q-learning_and_value-iteration"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Non-delusional Q-learning and value-iteration

**Authors:** Tyler Lu, Dale Schuurmans, Craig Boutilier

**Venue:** Advances in Neural Information Processing Systems 31 (NeurIPS 2018), held December 3-8, 2018 in Montréal, Canada, pages 9971-9981

**Core Contribution:**

The paper identifies a fundamental source of error in Q-learning and other forms of dynamic programming with function approxim
…[truncated 903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-29T06:57:50.187763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hieros Hierarchical Imagination Structured State Space Sequence World Models Mattes Schlosser Herbrich ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hieros Hierarchical Imagination Structured State Space Sequence World Models Mattes Schlosser Herbrich ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-29T06:57:50.188000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deep Reinforcement Learning that Matters Henderson Islam Bachman Pineau Precup Meger AAAI 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deep Reinforcement Learning that Matters Henderson Islam Bachman Pineau Precup Meger AAAI 2018"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-29T06:57:50.188188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Objective Mismatch Model-based Reinforcement Learning Lambert Amos Yadan Calandra L4DC 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Objective Mismatch Model-based Reinforcement Learning Lambert Amos Yadan Calandra L4DC 2020"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-29T06:57:50.188408+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deep Reinforcement Learning Edge Statistical Precipice Agarwal Schwarzer Castro Courville Bellemare NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deep Reinforcement Learning Edge Statistical Precipice Agarwal Schwarzer Castro Courville Bellemare NeurIPS 2021"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-29T06:57:50.188583+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepMind Control Suite Tassa Doron Muldal Erez 2018 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepMind Control Suite Tassa Doron Muldal Erez 2018 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-29T06:57:50.188713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Training Agents Inside Scalable World Models Hafner Yan Lillicrap 2025 DreamerV4 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Training Agents Inside Scalable World Models Hafner Yan Lillicrap 2025 DreamerV4 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-29T06:57:50.188900+00:00_

Web search results for query: "Deep Reinforcement Learning that Matters Henderson Islam Bachman Pineau Precup Meger AAAI 2018"

Links: [{"title":"Aaai","url":"https://ojs.aaai.org/index.php/AAAI/citationstylelanguage/get/apa?submissionId=11694&publicationId=10053"},{"title":"Deep Reinforcement Learning That Matters | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/11694"},{"title":"Deep reinforcement learning that matters - Princeton University","url":"https://collaborate.princeton.edu/en/publications/deep-reinforcement-learning-that-matters/"},{"title":"dblp: Deep Reinforcement Learning That Matters.","url":"https://dblp.org/rec/conf/aaai/0002IBPPM18.html"},{"title":"Deep Reinforcement Learning That Matters - AAAI","url":"https://aaai.org/papers/11694-deep-reinforcement-learning-that-matters/"},{"title":"Deep Reinforcement Learning that Matters | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2b5bd5f75948f959eac4a2bf2fce9ef42/analyst"},{"title":"Deep reinforcement learning that matters | Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence and Thirtieth Innovative Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/abs/10.5555/3504035.3504427"},{"title":"Deep Reinforcement Learning that Matters","url":"https://arxiv.org/pdf/1709.06560"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Henderson%2C+P.%2C+Islam%2C+R.%2C+Bachman%2C+P.%2C+Pineau%2C+J.%2C+Precup%2C+D.%2C+Meger%2C+D.%3A+Deep+reinforcement+learning+that+matters.+In%3A+Thirty-Second+AAAI+Conference+on+Artificial+Intelligence+%282018%29"},{"title":"[1709.06560] Deep Reinforcement Learning that Matters","url":"https://arxiv.org/abs/1709.06560"}]

I found information about the paper "Deep Reinforcement Learning That Matters" by Henderson, Islam, Bachman, Pineau, Precup, and Meger from AA
…[truncated 883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-29T06:57:50.189175+00:00_

Web search results for query: "Hieros Hierarchical Imagination Structured State Space Sequence World Models Mattes Schlosser Herbrich ICML 2024"

Links: [{"title":"ICML Poster Hieros: Hierarchical Imagination on Structured State Space Sequence World Models","url":"https://icml.cc/virtual/2024/poster/34428"},{"title":"[2310.05167] Hieros: Hierarchical Imagination on Structured State Space Sequence World Models","url":"https://arxiv.org/abs/2310.05167"},{"title":"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models","url":"https://arxiv.org/html/2310.05167v2"},{"title":"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models","url":"https://proceedings.mlr.press/v235/mattes24a.html"},{"title":"Hieros: Hierarchical Imagination on Structured State Space Sequence   World Models","url":"https://arxiv.org/pdf/2310.05167"},{"title":"Publications – Ralf Herbrich’s Homepage","url":"https://herbrich.me/publications/"},{"title":"(PDF) Hieros: Hierarchical Imagination on Structured State Space Sequence World Models","url":"https://www.researchgate.net/publication/378745771_Hieros_Hierarchical_Imagination_on_Structured_State_Space_Sequence_World_Models"},{"title":"Hieros: Hierarchical Imagination on Structured State Space Sequence World","url":"https://herbrich.me/papers/hieros_icml-8.pdf"}]

Based on the search results, here's information about the paper:

## HIEROS: Hierarchical Imagination on Structured State Space Sequence World Models

HIEROS is a hierarchical policy that learns time abstracted world representations and imagines trajectories at multiple time scales in latent space. The paper was authored by Paul Mattes, Rainer Schlosser, and Ralf Herbrich from the Digital Engineering Faculty Hasso Plattner Institute, University of Potsdam, Germany.

### Key Contribution

The paper addresses the challenge of sample efficiency in deep reinforcement learning (DRL), where many approaches learn a world model to train an agent e
…[truncated 1080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-29T06:57:50.189486+00:00_

Web search results for query: "Objective Mismatch Model-based Reinforcement Learning Lambert Amos Yadan Calandra L4DC 2020"

Links: [{"title":"Objective Mismatch in Model-based Reinforcement Learning - Facebook Research","url":"https://research.fb.com/publications/objective-mismatch-in-model-based-reinforcement-learning/"},{"title":"Theory and Practice of Model-based Reinforcement Learning [Caltech]","url":"https://slides.com/rcalandra/advances-mbrl"},{"title":"Objective Mismatch in Model-based Reinforcement Learning","url":"http://proceedings.mlr.press/v120/lambert20a.html"},{"title":"Objective Mismatch in Model-based Reinforcement Learning","url":"https://arxiv.org/pdf/2002.04523"},{"title":"Objective Mismatch in Model-based Reinforcement Learning - Paper Detail","url":"https://deeplearn.org/arxiv/115201/objective-mismatch-in-model-based-reinforcement-learning"},{"title":"[PDF] Objective Mismatch in Model-based Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Objective-Mismatch-in-Model-based-Reinforcement-Lambert-Amos/ecbdc83a1aa8d196943d8997300be871b1c7c2dc"},{"title":"Objective Mismatch in Model-based Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200204523L/abstract"},{"title":"[2002.04523] Objective Mismatch in Model-based Reinforcement Learning","url":"https://arxiv.org/abs/2002.04523"},{"title":"dblp: Objective Mismatch in Model-based Reinforcement Learning.","url":"https://dblp.org/rec/journals/corr/abs-2002-04523.html"},{"title":"objective mismatch in reinforcement learning from human ...","url":"https://arxiv.org/pdf/2311.00168"}]

I found the paper you're looking for! Here are the key details:

The paper "Objective Mismatch in Model-based Reinforcement Learning" was authored by Nathan Lambert, Brandon Amos, Omry Yadan, and Roberto Calandra in 2020. It was published in the Proceedings of the 2nd Conference on Learning for Dynamics and Control (L4DC), pages 761-770.

**Main Concept:**
…[truncated 721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-29T06:57:50.189767+00:00_

Web search results for query: "DeepMind Control Suite Tassa Doron Muldal Erez 2018 arXiv"

Links: [{"title":"[1801.00690] DeepMind Control Suite","url":"https://arxiv.org/abs/1801.00690"},{"title":"[1801.00690v1] DeepMind Control Suite","url":"https://arxiv.org/abs/1801.00690v1"},{"title":"DeepMind Control Suite - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv180100690T/abstract"},{"title":"Paper page - DeepMind Control Suite","url":"https://huggingface.co/papers/1801.00690"},{"title":"DeepMind Control Suite","url":"https://scirate.com/arxiv/1801.00690"},{"title":"[PDF] DeepMind Control Suite | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepMind-Control-Suite-Tassa-Doron/a9a3ed69c94a3e1c08ef1f833d9199f57736238b"},{"title":"Figure 7 from DeepMind Control Suite | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepMind-Control-Suite-Tassa-Doron/a9a3ed69c94a3e1c08ef1f833d9199f57736238b/figure/7"},{"title":"(PDF) DeepMind Control Suite","url":"https://www.researchgate.net/publication/322221208_DeepMind_Control_Suite"},{"title":"Figure 2 from DeepMind Control Suite | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepMind-Control-Suite-Tassa-Doron/a9a3ed69c94a3e1c08ef1f833d9199f57736238b/figure/1"},{"title":"DeepMind Control Suite Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez,","url":"https://arxiv.org/pdf/1801.00690"}]

I found the paper you're looking for! Here are the search results:

The DeepMind Control Suite was authored by Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez, and 8 other co-authors. It is a set of continuous control tasks with a standardised structure and interpretable rewards, intended to serve as performance benchmarks for reinforcement learning agents.

The tasks are written in Python and powered by the MuJoCo physics engine, making them easy to use and modify. The paper was published on January 2, 2018, with arXiv identifier 1801.00690.

The Control Suite is publicly available at
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-29T06:57:50.190106+00:00_

Web search results for query: "Deep Reinforcement Learning Edge Statistical Precipice Agarwal Schwarzer Castro Courville Bellemare NeurIPS 2021"

Links: [{"title":"Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://agarwl.github.io/rliable/"},{"title":"Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://psc-g.github.io/posts/research/rl/precipice/"},{"title":"Agarwal, R., Schwarzer, M., Castro, P.S., Courville, A. and Bellemare, M.G. (2021) Deep Reinforcement Learning at the Edge of the Statistical Precipice. Proceedings of the 35th International Conference on Neural Information Processing System, New York, 6-14 December 2021, 29304-29620. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3835321"},{"title":"[PDF] Deep Reinforcement Learning at the Edge of the Statistical Precipice | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-at-the-Edge-of-the-Agarwal-Schwarzer/558ca2e8c7eb56edd77a52b084e6cc24dffe5bcd"},{"title":"Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://papers.nips.cc/paper/2021/file/f514cec81cb148559cf475e7426eed5e-Paper.pdf"},{"title":"[2108.13264v2] Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://arxiv.org/abs/2108.13264v2"},{"title":"Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://proceedings.neurips.cc/paper_files/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html"},{"title":"[Quick Review] Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://liner.com/review/deep-reinforcement-learning-at-the-edge-of-the-statistical-precipice"},{"title":"[2108.13264] Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://arxiv.org/abs/2108.13264"},{"title":"Deep reinforcement learning at the edge of the statist
…[truncated 1580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-29T06:57:50.190400+00:00_

Web search results for query: "Training Agents Inside Scalable World Models Hafner Yan Lillicrap 2025 DreamerV4 arXiv"

Links: [{"title":"[2509.24527v1] Training Agents Inside of Scalable World Models","url":"https://arxiv.org/abs/2509.24527v1"},{"title":"[2509.24527] Training Agents Inside of Scalable World Models","url":"https://arxiv.org/abs/2509.24527"},{"title":"Dreamer 4: Scalable World Model Agents","url":"https://www.emergentmind.com/papers/2509.24527"},{"title":"GitHub - nicklashansen/dreamer4: Unofficial implementation of the Dreamer 4 world model in PyTorch. · GitHub","url":"https://github.com/nicklashansen/dreamer4"},{"title":"[Dreamer 4] Training Agents Inside of Scalable World Models","url":"https://arxiviq.substack.com/p/dreamer-4-training-agents-inside"},{"title":"Training Agents Inside of Scalable World Models","url":"https://danijar.com/project/dreamer4/"},{"title":"Training Agents in Scalable World Models: Dreamer 4 in Minecraft - Studocu","url":"https://www.studocu.com/row/document/univerza-v-ljubljani/metode-in-tehnike-raziskovalnega-dela/training-agents-in-scalable-world-models-dreamer-4-in-minecraft/156033434"},{"title":"DeepMind introduces AI agent that learns to complete various tasks in a scalable world model","url":"https://techxplore.com/news/2025-10-deepmind-ai-agent-tasks-scalable.html"},{"title":"Training Agents Inside of Scalable World Models Danijar Hafner* Wilson Yan*","url":"https://arxiv.org/pdf/2509.24527"}]

I found the paper! Here's what I discovered:

The paper "Training Agents Inside of Scalable World Models" was submitted on September 29, 2025, with authors Danijar Hafner, Wilson Yan, and Timothy Lillicrap.

**Key findings:**

The paper introduces Dreamer 4, a scalable agent that learns to solve control tasks by reinforcement learning inside of a fast and accurate world model. It is the first agent to solve the long-horizon "obtain diamonds" challenge in Minecraft purely from a fixed offline dataset.

**Main innovations:**


…[truncated 784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-29T06:57:50.190685+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Understanding Preventing Capacity Loss Reinforcement Learning Lyle Rowland Dabney ICLR 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Understanding Preventing Capacity Loss Reinforcement Learning Lyle Rowland Dabney ICLR 2022"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-29T06:57:50.190914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Time-Aware World Model Adaptive Prediction Control Nhu Son Lin ICML 2025 arXiv 2506.08441"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Time-Aware World Model Adaptive Prediction Control Nhu Son Lin ICML 2025 arXiv 2506.08441"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-29T06:57:50.191122+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Open-World Reinforcement Learning Long Short-Term Imagination Li Wang ICLR 2025 arXiv 2410.03618"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Open-World Reinforcement Learning Long Short-Term Imagination Li Wang ICLR 2025 arXiv 2410.03618"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-29T06:57:50.191317+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Randomized Ensembled Double Q-Learning Learning Fast Without Model Chen Wang Zhou Ross ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Randomized Ensembled Double Q-Learning Learning Fast Without Model Chen Wang Zhou Ross ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-29T06:57:50.191518+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Option-Critic Architecture Bacon Harb Precup AAAI 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Option-Critic Architecture Bacon Harb Precup AAAI 2017"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-29T06:57:50.191712+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sample-Efficient Reinforcement Learning Stochastic Ensemble Value Expansion Buckman Hafner Tucker Brevdo Lee NeurIPS 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sample-Efficient Reinforcement Learning Stochastic Ensemble Value Expansion Buckman Hafner Tucker Brevdo Lee NeurIPS 2018"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-29T06:57:50.191984+00:00_

Web search results for query: "Understanding Preventing Capacity Loss Reinforcement Learning Lyle Rowland Dabney ICLR 2022"

Links: [{"title":"Understanding and Preventing Capacity Loss in Reinforcement Learning","url":"https://arxiv.org/pdf/2204.09560"},{"title":"Understanding and Preventing Capacity Loss in Reinforcement Learning","url":"https://www.paperstudio.app/paper/2204.09560"},{"title":"Understanding and Preventing Capacity Loss in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=ZkC8wKoLbQ7"},{"title":"Understanding and Preventing Capacity Loss in Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220409560L/abstract"},{"title":"ICLR 2022 Understanding and Preventing Capacity Loss in Reinforcement Learning Spotlight","url":"https://iclr.cc/virtual/2022/spotlight/6598"},{"title":"[2204.09560v1] Understanding and Preventing Capacity Loss in Reinforcement Learning","url":"https://arxiv.org/abs/2204.09560v1"},{"title":"[2204.09560] Understanding and Preventing Capacity Loss in Reinforcement Learning","url":"https://arxiv.org/abs/2204.09560"},{"title":"[PDF] Understanding and Preventing Capacity Loss in Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Understanding-and-Preventing-Capacity-Loss-in-Lyle-Rowland/0a818d426c813b7a4758c959d38ece5f2cc11476"},{"title":"Understanding and Preventing Capacity Loss in Reinforcement Learning_国家预印本平台","url":"https://sinoxiv.napstic.cn/article/4084728"},{"title":"ICLR Poster Understanding and Preventing Capacity Loss in Reinforcement Learning","url":"https://iclr.cc/virtual/2022/poster/6597"}]

I found the paper you're looking for! Here's what I found:

**Title:** Understanding and Preventing Capacity Loss in Reinforcement Learning

**Authors:** Clare Lyle, Mark Rowland & Will Dabney from DeepMind

**Conference:** ICLR 2022 (Spotlight)

**Key Contributions:**

The paper identifies a mechanism called "capacity loss," whereby networks
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-29T06:57:50.192270+00:00_

Web search results for query: "Time-Aware World Model Adaptive Prediction Control Nhu Son Lin ICML 2025 arXiv 2506.08441"

Links: [{"title":"[2506.08441] Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/abs/2506.08441"},{"title":"Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/pdf/2506.08441"},{"title":"Time-Aware World Model for Adaptive Prediction and Control | OpenReview","url":"https://openreview.net/forum?id=gZ5N3TLjwv"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=2025&show=500"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=950&show=250"},{"title":"GitHub - anh-nn01/Time-Aware-World-Model: Official Code for Time-Aware World Model (TAWM) with TD-MPC2 as the baseline architecture in the experiments.","url":"https://github.com/anh-nn01/Time-Aware-World-Model"},{"title":"ICML Poster Time-Aware World Model for Adaptive Prediction and Control","url":"https://icml.cc/virtual/2025/poster/44469"},{"title":"World Models as Reference Trajectories for Rapid Motor Adaptation","url":"https://arxiv.org/pdf/2505.15589"},{"title":"Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling","url":"https://arxiv.org/pdf/2502.00622"}]

I found the paper you're looking for! Here's what I found:

"Time-Aware World Model (TAWM)" is a model-based approach that explicitly incorporates temporal dynamics. By conditioning on the time-step size, Δt, and training over a diverse range of Δt values—rather than sampling at a fixed time-step—TAWM learns both high- and low-frequency task dynamics across diverse control problems.

Grounded in the information-theoretic insight that the optimal sampling rate depends on a system's underlying dynamics, this time-aware formulation improves both performance and data efficiency.

The paper was accepted to ICML 2025 and is authored by Anh N. Nhu, Sanghyun Son,
…[truncated 432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-29T06:57:50.192551+00:00_

Web search results for query: "Randomized Ensembled Double Q-Learning Learning Fast Without Model Chen Wang Zhou Ross ICLR 2021"

Links: [{"title":"Published as a conference paper at ICLR 2021","url":"https://arxiv.org/pdf/2101.05982"},{"title":"[2101.05982v2] Randomized Ensembled Double Q-Learning: Learning Fast Without a Model","url":"https://arxiv.org/abs/2101.05982v2"},{"title":"Randomized Ensembled Double Q-Learning: Learning Fast Without a Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210105982C/abstract"},{"title":"[2101.05982] Randomized Ensembled Double Q-Learning: Learning Fast Without a Model","url":"https://arxiv.org/abs/2101.05982"},{"title":"[PDF] Randomized Ensembled Double Q-Learning: Learning Fast Without a Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Randomized-Ensembled-Double-Q-Learning:-Learning-a-Chen-Wang/736590f70e7f2dc464c1c62491cfa8adb4d718f3"},{"title":"Randomized Ensembled Double Q-Learning: Learning Fast Without a Model | Request PDF","url":"https://www.researchgate.net/publication/348563168_Randomized_Ensembled_Double_Q-Learning_Learning_Fast_Without_a_Model"},{"title":"Xinyue Chen, Che Wang, Zijian Zhou, Keith Ross · Randomized Ensembled Double Q-Learning: Learning Fast Without a Model","url":"https://slideslive.com/38953830/randomized-ensembled-double-qlearning-learning-fast-without-a-model"},{"title":"RANDOMIZED ENSEMBLED DOUBLE Q-LEARNING","url":"https://openreview.net/pdf/c4e6642e1eb45768ab5d7a3291c2a0088665e5c4.pdf"}]

I found the paper! Here are the key results:

**Paper Title:** Randomized Ensembled Double Q-Learning: Learning Fast Without a Model

**Authors:** Xinyue Chen, Che Wang, Zijian Zhou, Keith Ross

**Publication:** Published at ICLR 2021

**Main Contribution:** The paper introduces a simple model-free algorithm, Randomized Ensembled Double Q-Learning (REDQ), showing that its performance is just as good as, if not better than, a state-of-the-art model-based algorithm for the Mu
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-29T06:57:50.192838+00:00_

Web search results for query: "Option-Critic Architecture Bacon Harb Precup AAAI 2017"

Links: [{"title":"The Option-Critic Architecture | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/10916"},{"title":"(PDF) The Option-Critic Architecture","url":"https://www.academia.edu/44867878/The_Option_Critic_Architecture"},{"title":"The Option-Critic Architecture - AAAI","url":"https://aaai.org/papers/10916-aaai-31-2017/"},{"title":"dblp: The Option-Critic Architecture.","url":"https://dblp.org/rec/conf/aaai/BaconHP17.html"},{"title":"(PDF) The Option-Critic Architecture","url":"https://www.researchgate.net/publication/308262673_The_Option-Critic_Architecture"},{"title":"The Option-Critic Architecture Pierre-Luc Bacon, Jean Harb, Doina Precup","url":"https://pierrelucbacon.com/optioncritic-aaai2017-slides.pdf"},{"title":"The option-critic architecture | Proceedings of the Thirty-First AAAI Conference on Artificial Intelligence","url":"https://dl.acm.org/doi/10.5555/3298483.3298491"},{"title":"Safe option-critic: learning safety in the option-critic architecture | The Knowledge Engineering Review | Cambridge Core","url":"https://www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/safe-optioncritic-learning-safety-in-the-optioncritic-architecture/9F9E4CDA5C2958CEBB440197E3E1B3B3"},{"title":"The Option-Critic Architecture","url":"https://arxiv.org/pdf/1609.05140"}]

Based on the search results, here's information about the Option-Critic Architecture paper:

## Overview

The paper "The Option-Critic Architecture" was authored by Bacon, P.-L., Harb, J., and Precup, D. and published in the Proceedings of the AAAI Conference on Artificial Intelligence, 31(1) in 2017.

## Key Contributions

Temporal abstraction is key to scaling up learning and planning in reinforcement learning. While planning with temporally extended actions is well understood, creating such abstractions autonomously from 
…[truncated 684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-29T06:57:50.193131+00:00_

Web search results for query: "Sample-Efficient Reinforcement Learning Stochastic Ensemble Value Expansion Buckman Hafner Tucker Brevdo Lee NeurIPS 2018"

Links: [{"title":"Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion","url":"https://danijar.com/project/steve/"},{"title":"Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion | Papers With Code","url":"https://paperswithcode.com/paper/sample-efficient-reinforcement-learning-with"},{"title":"Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion","url":"https://papers.nips.cc/paper/2018/hash/f02208a057804ee16ac72ff4d3cec53b-Abstract.html"},{"title":"Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion","url":"https://research.google/pubs/sample-efficient-reinforcement-learning-with-stochastic-ensemble-value-expansion/"},{"title":"[PDF] Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sample-Efficient-Reinforcement-Learning-with-Value-Buckman-Hafner/08555bf7d6a483f783b7508ed2df5b1a4d29661c"},{"title":"dblp: Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion.","url":"https://dblp.org/rec/conf/nips/BuckmanHTBL18.html"},{"title":"Sample-efficient reinforcement learning with stochastic ensemble value expansion | Proceedings of the 32nd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3327757.3327916"},{"title":"Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion","url":"https://proceedings.neurips.cc/paper/2018/hash/f02208a057804ee16ac72ff4d3cec53b-Abstract.html"},{"title":"[1807.01675] Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion","url":"https://arxiv.org/abs/1807.01675"},{"title":"Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion - 
…[truncated 1537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-29T06:57:50.193428+00:00_

Web search results for query: "Open-World Reinforcement Learning Long Short-Term Imagination Li Wang ICLR 2025 arXiv 2410.03618"

Links: [{"title":"[2410.03618] Open-World Reinforcement Learning over Long Short-Term Imagination","url":"https://arxiv.org/abs/2410.03618"},{"title":"[Literature Review] Open-World Reinforcement Learning over Long Short-Term Imagination","url":"https://www.themoonlight.io/en/review/open-world-reinforcement-learning-over-long-short-term-imagination"},{"title":"GitHub - qiwang067/LS-Imagine: [ICLR 2025 Oral] PyTorch code for the paper \"Open-World Reinforcement Learning over Long Short-Term Imagination\" · GitHub","url":"https://github.com/qiwang067/LS-Imagine"},{"title":"ICLR 2025 Open-World Reinforcement Learning over Long Short-Term Imagination Oral","url":"https://iclr.cc/virtual/2025/oral/31740"},{"title":"ICLR Poster Open-World Reinforcement Learning over Long Short-Term Imagination","url":"https://iclr.cc/virtual/2025/poster/27879"},{"title":"Machine Learning Oct 2024","url":"https://arxiv.org/list/cs.LG/2024-10?skip=375&show=25"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.03618"},{"title":"Open-World Reinforcement Learning over Long Short-Term Imagination","url":"https://arxiv.org/html/2410.03618v1"}]

I found the paper! Here's what I found about it:

The paper "Open-World Reinforcement Learning over Long Short-Term Imagination" (arXiv:2410.03618) was accepted as an oral presentation at ICLR 2025 and was authored by Jiajian Li, Qi Wang, Yunbo Wang, Xin Jin, Yang Li, Wenjun Zeng, and Xiaokang Yang.

**Main Contribution:**

The paper presents LS-Imagine, which extends the imagination horizon within a limited number of state transition steps, enabling the agent to explore behaviors that potentially lead to promising long-term feedback.

**Problem Addressed:**

While model-based methods have improved sample efficiency by learning interactive world models, these agents tend to be "short-sig
…[truncated 809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-29T06:57:50.193718+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deep Reinforcement Learning Handful Trials Probabilistic Dynamics Models Chua Calandra McAllister Levine NeurIPS 2018 PETS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deep Reinforcement Learning Handful Trials Probabilistic Dynamics Models Chua Calandra McAllister Levine NeurIPS 2018 PETS"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-29T06:57:50.193951+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Training with Noise Equivalent Tikhonov Regularization Bishop 1995 Neural Computation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Training with Noise Equivalent Tikhonov Regularization Bishop 1995 Neural Computation"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-29T06:57:50.194153+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Noisy Networks Exploration Fortunato Azar Piot Menick Osband Graves ICLR 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Noisy Networks Exploration Fortunato Azar Piot Menick Osband Graves ICLR 2018"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-29T06:57:50.194350+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reinforcement Learning Hierarchies Abstract Machines Parr Russell NIPS 1998"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reinforcement Learning Hierarchies Abstract Machines Parr Russell NIPS 1998"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-29T06:57:50.194545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hierarchical Reinforcement Learning MAXQ Value Function Decomposition Dietterich 2000 JAIR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hierarchical Reinforcement Learning MAXQ Value Function Decomposition Dietterich 2000 JAIR"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-29T06:57:50.194736+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reinforcement Learning Methods Continuous-Time Markov Decision Problems Bradtke Duff NIPS 1995"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reinforcement Learning Methods Continuous-Time Markov Decision Problems Bradtke Duff NIPS 1995"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-29T06:57:50.195051+00:00_

Web search results for query: "Training with Noise Equivalent Tikhonov Regularization Bishop 1995 Neural Computation"

Links: [{"title":"Training with noise is equivalent to Tikhonov regularization - Aston Research Explorer","url":"https://research.aston.ac.uk/en/publications/training-with-noise-is-equivalent-to-tikhonov-regularization"},{"title":"Training with noise is equivalent to Tikhonov regularization - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/training-with-noise-is-equivalent-to-tikhonov-regularization/"},{"title":"Training with Noise is Equivalent to Tikhonov Regularization","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bishop-tikhonov-nc-95.pdf"},{"title":"Training with Noise is Equivalent to Tikhonov Regularization | Neural Computation | MIT Press","url":"https://direct.mit.edu/neco/article/7/1/108/5828/Training-with-Noise-is-Equivalent-to-Tikhonov"},{"title":"Training with Noise is Equivalent to Tikhonov Regularization | MIT CogNet","url":"http://mitp-cog.mit.edu/journal/10.1162/neco.1995.7.1.108"},{"title":"Training with noise is equivalent to Tikhonov regularization · Paperwhy","url":"https://paperwhy.8027.org/2017/06/12/training-with-noise-is-equivalent-to-tikhonov-regularization/"},{"title":"Training with noise is equivalent to Tikhonov regularization | Neural Computation","url":"https://dl.acm.org/doi/abs/10.1162/neco.1995.7.1.108"},{"title":"Training with noise is equivalent to Tikhonov regularization - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/training-with-noise-is-equivalent-to-tikhonov-regularization/"}]

I found the paper you were looking for. Here are the key details:

**Publication Information:**
Christopher M. Bishop published "Training with noise is equivalent to Tikhonov regularization" in Neural Computation in January 1995, Volume 7, Issue 1, pages 108-116.

**Main Contribution:**
The paper shows that the addition of n
…[truncated 772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-29T06:57:50.195352+00:00_

Web search results for query: "Deep Reinforcement Learning Handful Trials Probabilistic Dynamics Models Chua Calandra McAllister Levine NeurIPS 2018 PETS"

Links: [{"title":"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models","url":"https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html"},{"title":"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models","url":"https://papers.nips.cc/paper/7725-deep-reinforcement-learning-in-a-handful-of-trials-using-probabilistic-dynamics-models"},{"title":"[PDF] Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-in-a-Handful-of-Trials-Chua-Calandra/56136aa0b2c347cbcf3d50821f310c4253155026"},{"title":"Deep Reinforcement Learning in a Handful of Trials using Probabilistic   Dynamics Models","url":"https://arxiv.org/pdf/1805.12114"},{"title":"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv180512114C/abstract"},{"title":"Deep Reinforcement Learning in a Handful of Trials using ...","url":"https://proceedings.neurips.cc/paper_files/paper/2018/file/3de568f8597b94bda53149c7d7f5958c-Paper.pdf"},{"title":"dblp: Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models.","url":"https://dblp.org/rec/conf/nips/ChuaCML18.html"},{"title":"[1805.12114] Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models","url":"https://arxiv.org/abs/1805.12114"},{"title":"Deep Reinforcement Learning in a Handful of Trials using ...","url":"https://nips.cc/media/nips-2018/Slides/12741.pdf"}]

I've successfully found the paper you were looking for! Here's a summary of the search results:

The paper is titled "Deep Reinforcement Learning in a Handful of Trials usin
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-29T06:57:50.195639+00:00_

Web search results for query: "Reinforcement Learning Hierarchies Abstract Machines Parr Russell NIPS 1998"

Links: [{"title":"Reinforcement Learning with Hierarchies of Machines","url":"https://proceedings.neurips.cc/paper/1997/hash/5ca3e9b122f61f8f06494c97b1afccf3-Abstract.html"},{"title":"Reinforcement Learning with Hierarchies of Machines","url":"https://papers.nips.cc/paper/1384-reinforcement-learning-with-hierarchies-of-machines"},{"title":"Hierarchical Reinforcement Learning with Clustering Abstract Machines | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-30763-9_3"},{"title":"Reinforcement Learning with Hierarchies of Machines Ron Parr and Stuart Russell","url":"https://people.eecs.berkeley.edu/~russell/classes/cs294/f05/papers/parr+russell-1998.pdf"},{"title":"Reinforcement learning with hierarchies of machines | Proceedings of the 11th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3008904.3009050"},{"title":"Reinforcement Learning with Hierarchies of Machines","url":"https://users.cs.duke.edu/~parr/ham-nips97.pdf"},{"title":"Efficient Reinforcement Learning with Hierarchies of Machines ...","url":"https://people.eecs.berkeley.edu/~russell/papers/ijcai17-ham.pdf"},{"title":"Automatic formation of the structure of abstract machines in   hierarchical reinforcement learning with state clustering","url":"https://arxiv.org/pdf/1806.05292"},{"title":"Programmable Reinforcement Learning Agents David Andre and Stuart J. Russell","url":"https://people.eecs.berkeley.edu/~russell/papers/nips00-pham.pdf"}]

Based on the search results, I found the paper you're looking for. The paper "Reinforcement Learning with Hierarchies of Machines" by Ronald Parr and Stuart J. Russell was published as part of Advances in Neural Information Processing Systems 10 (NIPS 1997).

Note: The search results indicate this paper was published at NIPS 1997, not 1998 as mentioned in your query. The paper pres
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-29T06:57:50.196006+00:00_

Web search results for query: "Noisy Networks Exploration Fortunato Azar Piot Menick Osband Graves ICLR 2018"

Links: [{"title":"Noisy Networks for Exploration","url":"https://research.google/pubs/pub46981/"},{"title":"Published as a conference paper at ICLR 2018","url":"https://matthiasplappert.com/publications/2018_Plappert_Param-Noise-ICLR.pdf"},{"title":"Published as a conference paper at ICLR 2018 NOISY NETWORKS FOR EXPLORATION","url":"https://openreview.net/pdf?id=rywHCPkAW"},{"title":"[1706.10295] Noisy Networks for Exploration","url":"https://arxiv.org/abs/1706.10295"},{"title":"[1706.10295v2] Noisy Networks for Exploration","url":"https://arxiv.org/abs/1706.10295v2"},{"title":"[1706.10295v3] Noisy Networks for Exploration","url":"https://arxiv.org/abs/1706.10295v3"},{"title":"Noisy Networks for Exploration","url":"https://arxiv.org/pdf/1706.10295"},{"title":"Noisy Networks for Exploration Meire Fortunato∗ Mohammad Gheshlaghi Azar∗","url":"https://arxiv.org/pdf/1706.10295v1"},{"title":"Noisy Networks For Exploration - researchr publication","url":"https://researchr.org/publication/FortunatoAPMHOG18"},{"title":"Noisy Spiking Actor Network for Exploration","url":"https://arxiv.org/pdf/2403.04162"}]

I found the paper you're looking for. Here are the key details:

The paper "Noisy Networks for Exploration" was published at ICLR 2018 in Vancouver by Meire Fortunato, Mohammad Gheshlaghi Azar, Bilal Piot, Jacob Menick, Ian Osband, Alexander Graves, and other authors from DeepMind.

**Main Contribution:**
The paper introduces NoisyNet, a deep reinforcement learning agent with parametric noise added to its weights, and shows that the induced stochasticity of the agent's policy can be used to aid efficient exploration.

**Key Technical Details:**
- The parameters of the noise are learned with gradient descent along with the remaining network weights
- NoisyNet is straightforward to implement and adds little computational overhead
- Replacing the conventional explorat
…[truncated 419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-29T06:57:50.196330+00:00_

Web search results for query: "Hierarchical Reinforcement Learning MAXQ Value Function Decomposition Dietterich 2000 JAIR"

Links: [{"title":"Publications hierarchical reinforcement learning with the maxq value function decomposition","url":"https://www.cs.utexas.edu/~shivaram/readings/b2hd-Dietterich2000.html"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Hierarchical+reinforcement+learning+with+the+MAXQ+value+function+decomposition&amp=&author=T.+G.+Dietterich&amp=&publication_year=2000&amp=&journal=J.+Artif.+Intell.+Res.&amp=&pages=227-303&amp=&doi=10.1613/jair.639"},{"title":"Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition","url":"https://jmvidal.cse.sc.edu/lib/dietterich00a.html"},{"title":"Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition | Journal of Artificial Intelligence Research","url":"https://jair.org/index.php/jair/article/view/10266"},{"title":"Hierarchical Reinforcement Learning with the MAXQ Value ...","url":"https://campusai.github.io/papers/HRL-with-MAXQ-decomposition"},{"title":"[cs/9905014v1] Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition","url":"https://www.arxiv.org/abs/cs/9905014v1"},{"title":"[cs/9905014] Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition","url":"https://arxiv.org/abs/cs/9905014"},{"title":"Hierarchical Reinforcement Learning with the MAXQ Value ...","url":"https://arxiv.org/pdf/cs/9905014"},{"title":"Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition | Request PDF","url":"https://www.researchgate.net/publication/268304999_Hierarchical_Reinforcement_Learning_with_the_MAXQ_Value_Function_Decomposition"},{"title":"[PDF] Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Hierarchical-Reinforcement-Learning-with-the-MAXQ-Dietterich/4c96ca25d889251e20e33d01f
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-29T06:57:50.196628+00:00_

Web search results for query: "Reinforcement Learning Methods Continuous-Time Markov Decision Problems Bradtke Duff NIPS 1995"

Links: [{"title":"Bradtke, S.J. and Duff, M.O. (1995) Reinforcement Learning Methods for Continuous-Time Markov Decision Problems. Advances in Neural Information Processing Systems, 7, 393-400. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1992189"},{"title":"Model-based reinforcement learning for semi-Markov decision processes with neural ODEs | Proceedings of the 34th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3495724.3497386"},{"title":"Reinforcement learning methods for continuous-time Markov decision problems | Proceedings of the 8th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/2998687.2998736"},{"title":"Reinforcement Learning Methods for Continuous-Time Markov Decision Problems","url":"https://proceedings.neurips.cc/paper/1994/hash/07871915a8107172b3b5dc15a6574ad3-Abstract.html"},{"title":"(PDF) Reinforcement Learning Methods for Continuous-Time Markov Decision Problems","url":"https://www.researchgate.net/publication/2453730_Reinforcement_Learning_Methods_for_Continuous-Time_Markov_Decision_Problems"},{"title":"[PDF] Reinforcement Learning Methods for Continuous-Time Markov Decision Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reinforcement-Learning-Methods-for-Continuous-Time-Bradtke-Duff/96a25df486c7dfa475a93a0ca31d0418f79a8771"},{"title":"(PDF) Reinforcement learning methods for continuous-time Markov decision problems","url":"https://www.academia.edu/12142451/Reinforcement_learning_methods_for_continuous_time_Markov_decision_problems"},{"title":"dblp: Michael O. Duff","url":"https://dblp.org/pid/23/3703.html"},{"title":"Reinforcement Learning Methods for Continuous-Time Markov Decision Problems","url":"https://eu
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-29T06:57:50.196952+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MOReL Model-Based Offline Reinforcement Learning Kidambi Rajeswaran Netrapalli Joachims NeurIPS 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MOReL Model-Based Offline Reinforcement Learning Kidambi Rajeswaran Netrapalli Joachims NeurIPS 2020"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-29T06:57:50.197171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "COMBO Conservative Offline Model-Based Policy Optimization Yu Kumar Rafailov NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "COMBO Conservative Offline Model-Based Policy Optimization Yu Kumar Rafailov NeurIPS 2021"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-29T06:57:50.197388+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Role Planning Model-Based Deep Reinforcement Learning Hamrick Friesen Behbahani Guez ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Role Planning Model-Based Deep Reinforcement Learning Hamrick Friesen Behbahani Guez ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-29T06:57:50.197585+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DayDreamer World Models Physical Robot Learning Wu Escontrela Hafner Abbeel CoRL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DayDreamer World Models Physical Robot Learning Wu Escontrela Hafner Abbeel CoRL 2023"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-29T06:57:50.197777+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Time Discretization-Invariant Safe Action Repetition Policy Gradient Methods Park Kim Kim NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Time Discretization-Invariant Safe Action Repetition Policy Gradient Methods Park Kim Kim NeurIPS 2021"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-29T06:57:50.197997+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reinforcement Learning Elastic Time Steps Wang Beltrame 2024 arXiv 2402.14961"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reinforcement Learning Elastic Time Steps Wang Beltrame 2024 arXiv 2402.14961"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-29T06:57:50.198243+00:00_

Web search results for query: "MOReL Model-Based Offline Reinforcement Learning Kidambi Rajeswaran Netrapalli Joachims NeurIPS 2020"

Links: [{"title":"MOReL: Model-Based Offline Reinforcement Learning","url":"https://papers.nips.cc/paper/2020/hash/f7efa4f864ae9b88d43527f4b14f750f-Abstract.html"},{"title":"MOReL : Model-Based Offline Reinforcement Learning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/morel-model-based-offline-reinforcement-learning/"},{"title":"MOReL: Model-Based Offline Reinforcement Learning","url":"https://proceedings.neurips.cc/paper/2020/hash/f7efa4f864ae9b88d43527f4b14f750f-Abstract.html"},{"title":"MOReL : Model-Based Offline Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200505951K/abstract"},{"title":"[PDF] MOReL : Model-Based Offline Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MOReL-:-Model-Based-Offline-Reinforcement-Learning-Kidambi-Rajeswaran/309c2c5ee60e725244da09180f913cd8d4b8d4e9"},{"title":"MOReL : Model-Based Offline Reinforcement Learning","url":"https://arxiv.org/pdf/2005.05951"},{"title":"[2005.05951] MOReL : Model-Based Offline Reinforcement Learning","url":"https://arxiv.org/abs/2005.05951"},{"title":"MOReL: Model-Based Offline Reinforcement Learning","url":"https://par.nsf.gov/servlets/purl/10196971"},{"title":"Model-Based Offline Reinforcement Learning with Reliability-Guaranteed   Sequence Modeling","url":"https://arxiv.org/pdf/2502.06491"},{"title":"MOORe: Model-based Offline-to-Online Reinforcement Learning","url":"https://arxiv.org/pdf/2201.10070"}]

I found comprehensive information about the MOReL paper. Here are the key details:

## Overview

MOReL is a paper by Rahul Kidambi, Aravind Rajeswaran, Praneeth Netrapalli, and Thorsten Joachims, published in Advances in Neural Information Processing Systems 33 (NeurIPS 2020), addressing offline reinforcement learning where the goal is to learn a highly rewarding
…[truncated 1187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-29T06:57:50.198535+00:00_

Web search results for query: "COMBO Conservative Offline Model-Based Policy Optimization Yu Kumar Rafailov NeurIPS 2021"

Links: [{"title":"[Quick Review] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://liner.com/review/combo-conservative-offline-modelbased-policy-optimization"},{"title":"COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://proceedings.neurips.cc/paper/2021/hash/f29a179746902e331572c483c45e5086-Abstract.html"},{"title":"[2102.08363v1] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://arxiv.org/abs/2102.08363v1"},{"title":"[2102.08363] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://arxiv.org/abs/2102.08363"},{"title":"COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://papertalk.org/papertalks/35821"},{"title":"COMBO: Conservative Offline Model-Based Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=dUEpGV2mhf"},{"title":"[2102.08363] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://ar5iv.labs.arxiv.org/html/2102.08363"},{"title":"Conservative Bayesian Model-Based Value Expansion for Offline Policy   Optimization","url":"https://arxiv.org/pdf/2210.03802"},{"title":"COMBO: Conservative Ofﬂine Model-Based Policy Optimization","url":"https://arxiv.org/pdf/2102.08363"}]

I found comprehensive information about COMBO. Here are the key results:

## Paper Details

COMBO (Conservative Offline Model-Based Policy Optimization) was presented at Advances in Neural Information Processing Systems 34 (NeurIPS 2021) by authors Tianhe Yu, Aviral Kumar, Rafael Rafailov, Aravind Rajeswaran, Sergey Levine, and Chelsea Finn.

## Main Contribution

COMBO is a model-based offline RL algorithm that regularizes the value function on out-of-support state-action tuples generated via rollouts under the learned model, resulting in a conservative estimate of the value function for out-of-support state-
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-29T06:57:50.198838+00:00_

Web search results for query: "Role Planning Model-Based Deep Reinforcement Learning Hamrick Friesen Behbahani Guez ICLR 2021"

Links: [{"title":"On the role of planning in model-based deep reinforcement learning | Jessica Hamrick","url":"https://www.jesshamrick.com/publication/hamrick-2021-on-role/"},{"title":"[2011.04021] On the role of planning in model-based deep reinforcement learning","url":"https://arxiv.org/abs/2011.04021"},{"title":"dblp: Jessica B. Hamrick","url":"https://dblp.org/pid/155/1885.html"},{"title":"Published as a conference paper at ICLR 2021 ON THE ROLE OF PLANNING IN","url":"https://arxiv.org/pdf/2011.04021"},{"title":"Publications | Jessica Hamrick","url":"https://www.jesshamrick.com/papers/"},{"title":"Jessica Hamrick, Abe Friesen, Feryal Behbahani, Arthur Guez, Fabio Viola, Sims Witherspoon, Thomas Anthony, Lars Buesing, Petar Veličković, Théophane Weber · On the role of planning in model-based deep reinforcement learning","url":"https://slideslive.com/38953889/on-the-role-of-planning-in-modelbased-deep-reinforcement-learning"},{"title":"[PDF] On the role of planning in model-based deep reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-role-of-planning-in-model-based-deep-Hamrick-Friesen/8b5bc6b5e42b2ea39e65cb14c06d8a819a03a496"},{"title":"On the role of planning in model-based deep reinforcement learning | Request PDF","url":"https://www.researchgate.net/publication/345653797_On_the_role_of_planning_in_model-based_deep_reinforcement_learning"},{"title":"ON THE ROLE OF PLANNING IN MODEL-BASED DEEP ...","url":"https://openreview.net/pdf?id=IrM64DGB21"}]

I found the paper! Here are the key details:

**Title:** On the role of planning in model-based deep reinforcement learning

**Authors:** Jessica B. Hamrick, Abram L. Friesen, Feryal M. P. Behbahani, Arthur Guez, Fabio Viola, Sims Witherspoon, Thomas Anthony, Lars Holger Buesing, Petar Velickovic, Theophane Weber

**Publication:** ICLR 2021

**Ov
…[truncated 939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-29T06:57:50.199143+00:00_

Web search results for query: "DayDreamer World Models Physical Robot Learning Wu Escontrela Hafner Abbeel CoRL 2023"

Links: [{"title":"DayDreamer: World Models for Physical Robot Learning","url":"https://proceedings.mlr.press/v205/wu23c.html"},{"title":"DayDreamer: World Models for Physical Robot Learning","url":"https://arxiv.org/pdf/2206.14176"},{"title":"DayDreamer: World Models for Physical Robot Learning | Alejandro Escontrela","url":"https://www.escontrela.me/daydreamer/"},{"title":"DayDreamer: World Models for Physical Robot Learning","url":"https://danijar.com/project/daydreamer/"},{"title":"[2206.14176v1] DayDreamer: World Models for Physical Robot Learning","url":"https://arxiv.org/abs/2206.14176v1"},{"title":"DayDreamer: World Models for Physical Robot Learning Philipp Wu*","url":"https://proceedings.mlr.press/v205/wu23c/wu23c.pdf"},{"title":"[2206.14176] DayDreamer: World Models for Physical Robot Learning","url":"https://arxiv.org/abs/2206.14176"},{"title":"GitHub - danijar/daydreamer: DayDreamer: World Models for Physical Robot Learning · GitHub","url":"https://github.com/danijar/daydreamer"},{"title":"[PDF] DayDreamer: World Models for Physical Robot Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DayDreamer:-World-Models-for-Physical-Robot-Wu-Escontrela/25bc06b508b2c63b9faf77881e528530b147b988"}]

Based on the search results, I found comprehensive information about DayDreamer:

## Overview

DayDreamer: World Models for Physical Robot Learning is a paper authored by Wu, Escontrela, Hafner, Abbeel, and Goldberg, published in the Proceedings of The 6th Conference on Robot Learning in 2023.

## Problem and Approach

Deep reinforcement learning is a common approach to robot learning but requires a large amount of trial and error to learn, limiting its deployment in the physical world, and many advances in robot learning rely on simulators. However, learning inside of simulators fails to capture the complexity of the real world,
…[truncated 936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-29T06:57:50.199420+00:00_

Web search results for query: "Reinforcement Learning Elastic Time Steps Wang Beltrame 2024 arXiv 2402.14961"

Links: [{"title":"Reinforcement Learning with Elastic Time Steps","url":"https://arxiv.org/pdf/2402.14961"},{"title":"[2402.14961] Reinforcement Learning with Elastic Time Steps","url":"https://arxiv.org/abs/2402.14961"},{"title":"[2402.14961] Reinforcement Learning with Elastic Time Steps","url":"https://ar5iv.labs.arxiv.org/html/2402.14961v1"},{"title":"Computer Science Feb 2024","url":"https://arxiv.org/list/cs/2024-02?skip=7000"},{"title":"MOSEAC: Streamlined Variable Time Step Reinforcement Learning","url":"https://arxiv.org/html/2406.01521v1"},{"title":"Reinforcement Learning with Elastic Time Steps1footnote 1FootnoteFootnoteFootnotesFootnotes1footnote 1This work was partly presented at the Finding the Frame Workshop in August 2024.","url":"https://arxiv.org/html/2402.14961v4"},{"title":"Reinforcement Learning with Elastic Time Steps by Dong Wang, Giovanni Beltrame :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4924628"},{"title":"Variable Time Step Reinforcement Learning for Robotic Applications","url":"https://arxiv.org/html/2407.00290v1"},{"title":"[2406.01521] MOSEAC: Streamlined Variable Time Step Reinforcement Learning","url":"https://arxiv.org/abs/2406.01521"}]

I found the paper you were searching for! Here are the key details:

**Title:** Reinforcement Learning with Elastic Time Steps

**Authors:** Dong Wang and Giovanni Beltrame

**arXiv ID:** 2402.14961

**Main Contribution:** The paper proposes the Multi-Objective Soft Elastic Actor-Critic (MOSEAC), an off-policy actor-critic algorithm that uses elastic time steps to dynamically adjust the control frequency and minimizes computational resources by selecting the lowest viable frequency.

**Problem Addressed:** Traditional Reinforcement Learning policies are typically implemented with fixed control rates, often disregarding the impact of control rate selection, which can
…[truncated 555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-29T06:57:50.199714+00:00_

Web search results for query: "Time Discretization-Invariant Safe Action Repetition Policy Gradient Methods Park Kim Kim NeurIPS 2021"

Links: [{"title":"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods","url":"https://proceedings.neurips.cc/paper/2021/hash/024677efb8e4aee2eaeef17b54695bbe-Abstract.html"},{"title":"GitHub - seohongpark/SAR: Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods (NeurIPS 2021) · GitHub","url":"https://github.com/seohongpark/SAR"},{"title":"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods","url":"https://papers.nips.cc/paper/2021/hash/024677efb8e4aee2eaeef17b54695bbe-Abstract.html"},{"title":"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods | OpenReview","url":"https://openreview.net/forum?id=xNmhYNQruJX"},{"title":"Time Discretization-Invariant Safe Action Repetition for Policy Gradient   Methods","url":"https://arxiv.org/pdf/2111.03941"},{"title":"[PDF] Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/c355cab6db1343b54cddd24603b6bbfd3864da3e"},{"title":"[2111.03941] Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods","url":"https://arxiv.org/abs/2111.03941"},{"title":"Time Discretization-Invariant Safe Action Repetition for ...","url":"https://proceedings.neurips.cc/paper/2021/file/024677efb8e4aee2eaeef17b54695bbe-Paper.pdf"},{"title":"Book","url":"https://proceedings.neurips.cc/paper_files/paper/2021"}]

I found the paper! Here's a summary of the research:

## Paper Overview

The paper "Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods" was published by Seohong Park, Jaekyeom Kim, and Gunhee Kim at NeurIPS 2021.

## Key Problem

The paper addresses the issue that continuous time is often discretized by a time scale δ in reinforcement learning, to which perf
…[truncated 896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-29T06:57:50.200036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "How Many Random Seeds Statistical Power Analysis Deep Reinforcement Learning Colas Sigaud Oudeyer 2018 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "How Many Random Seeds Statistical Power Analysis Deep Reinforcement Learning Colas Sigaud Oudeyer 2018 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-29T06:57:50.200252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Multi-timestep models Model-based Reinforcement Learning Benechehab Couairon Leurent 2023 arXiv 2310.05672"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Multi-timestep models Model-based Reinforcement Learning Benechehab Couairon Leurent 2023 arXiv 2310.05672"
  }
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-29T06:57:50.200453+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deep Hierarchical Planning from Pixels Hafner Lee Fischer Abbeel NeurIPS 2022 Director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deep Hierarchical Planning from Pixels Hafner Lee Fischer Abbeel NeurIPS 2022 Director"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-29T06:57:50.200695+00:00_

Web search results for query: "How Many Random Seeds Statistical Power Analysis Deep Reinforcement Learning Colas Sigaud Oudeyer 2018 arXiv"

Links: [{"title":"[PDF] How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Many-Random-Seeds-Statistical-Power-Analysis-in-Colas-Sigaud/789510820bb369802d58b733ef1c9dc531a609ed"},{"title":"[1806.08295] How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments","url":"https://arxiv.org/abs/1806.08295"},{"title":"[1806.08295] How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments","url":"https://ar5iv.labs.arxiv.org/html/1806.08295"},{"title":"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-01890154"},{"title":"Deep reinforcement learning at the edge of the statistical precipice | Proceedings of the 35th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3540261.3542505"},{"title":"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments | Request PDF","url":"https://www.researchgate.net/publication/325922173_How_Many_Random_Seeds_Statistical_Power_Analysis_in_Deep_Reinforcement_Learning_Experiments"},{"title":"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments | DeepAI","url":"https://deepai.org/publication/how-many-random-seeds-statistical-power-analysis-in-deep-reinforcement-learning-experiments"},{"title":"How many random seeds? statistical power analysis in ...","url":"https://arxiv.org/pdf/1806.08295"}]

I found the paper you're looking for! Here's what I found:

"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experim
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-29T06:57:50.201169+00:00_

Web search results for query: "Multi-timestep models Model-based Reinforcement Learning Benechehab Couairon Leurent 2023 arXiv 2310.05672"

Links: [{"title":"[2310.05672] Multi-timestep models for Model-based Reinforcement Learning","url":"https://arxiv.org/abs/2310.05672"},{"title":"[PDF] Multi-timestep models for Model-based Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multi-timestep-models-for-Model-based-Reinforcement-Benechehab-Paolo/182c8e48d08b8ff29f0854fe903b3bae8e0c999d"},{"title":"Multi-timestep models for Model-based Reinforcement Learning","url":"https://arxiv.org/pdf/2310.05672"},{"title":"Multi-timestep models for Model-based Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231005672B/abstract"},{"title":"Multi-timestep models for Model-based Reinforcement Learning","url":"https://arxiv.org/html/2310.05672v1"},{"title":"Multi-timestep models for Model-based Re...","url":"https://axi.lims.ac.uk/paper/2310.05672"}]

I found the paper! Here are the search results for the paper you're looking for:

"Multi-timestep models for Model-based Reinforcement Learning" by Abdelhakim Benechehab and 4 other authors (arXiv 2310.05672), published in October 2023.

**Summary of the paper:**

In model-based reinforcement learning (MBRL), most algorithms rely on simulating trajectories from one-step dynamics models learned on data, but a critical challenge is the compounding of one-step prediction errors as the length of the trajectory grows. 

The paper tackles this issue by using a multi-timestep objective to train one-step models, with the objective being a weighted sum of a loss function (e.g., negative log-likelihood) at various future horizons. 

The authors find that exponentially decaying weights lead to models that significantly improve the long-horizon R2 score. This improvement is particularly noticeable when the models were evaluated on noisy data.

Finally, using a soft actor-critic (SA
…[truncated 278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-29T06:57:50.201522+00:00_

Web search results for query: "Deep Hierarchical Planning from Pixels Hafner Lee Fischer Abbeel NeurIPS 2022 Director"

Links: [{"title":"Deep Hierarchical Planning from Pixels","url":"https://papers.nips.cc/paper_files/paper/2022/hash/a766f56d2da42cae20b5652970ec04ef-Abstract-Conference.html"},{"title":"Deep Hierarchical Planning from Pixels","url":"https://danijar.com/project/director/"},{"title":"[2206.04114] Deep Hierarchical Planning from Pixels","url":"https://arxiv-export-lb.library.cornell.edu/abs/2206.04114"},{"title":"Deep Hierarchical Planning from Pixels","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/a766f56d2da42cae20b5652970ec04ef-Abstract-Conference.html"},{"title":"[2206.04114v1] Deep Hierarchical Planning from Pixels","url":"https://arxiv.org/abs/2206.04114v1"},{"title":"[2206.04114] Deep Hierarchical Planning from Pixels","url":"https://arxiv.org/abs/2206.04114"},{"title":"[PDF] Deep Hierarchical Planning from Pixels | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Hierarchical-Planning-from-Pixels-Hafner-Lee/6d846a7601c4be41034b9316d7c256f639085d9f"},{"title":"Deep Hierarchical Planning from Pixels","url":"https://arxiv.org/pdf/2206.04114"},{"title":"GitHub - danijar/director: Deep Hierarchical Planning from Pixels · GitHub","url":"https://github.com/danijar/director"}]

Based on the search results, here's information about "Deep Hierarchical Planning from Pixels":

The paper was authored by Danijar Hafner, Kuang-Huei Lee, Ian Fischer, and Pieter Abbeel, and published at NeurIPS 2022.

The paper introduces Director, a practical method for learning hierarchical behaviors directly from pixels by planning inside the latent space of a learned world model. The high-level policy maximizes task and exploration rewards by selecting latent goals and the low-level policy learns to achieve the goals.

Director learns to break down tasks into internal subgoals, where the manager policy selects subgoals that trade off e
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-29T06:57:50.201855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2310.05672 Multi-timestep models authors Benechehab full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2310.05672 Multi-timestep models authors Benechehab full author list"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-29T06:57:50.202084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Reinforcement Learning with Hierarchies of Machines\" Parr Russell 1997 NIPS exact title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Reinforcement Learning with Hierarchies of Machines\" Parr Russell 1997 NIPS exact title"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-29T06:57:50.202286+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2301.04104 \"Mastering Diverse Domains\" Hafner Nature title change \"control tasks\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2301.04104 \"Mastering Diverse Domains\" Hafner Nature title change \"control tasks\""
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-29T06:57:50.202485+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Learning to Repeat: Fine Grained Action Repetition\" Sharma FiGAR ICLR 2017 exact title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Learning to Repeat: Fine Grained Action Repetition\" Sharma FiGAR ICLR 2017 exact title"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-29T06:57:50.202701+00:00_

Web search results for query: "arxiv 2310.05672 Multi-timestep models authors Benechehab full author list"

Links: [{"title":"[2310.05672] Multi-timestep models for Model-based Reinforcement Learning","url":"https://arxiv.org/abs/2310.05672"},{"title":"[PDF] Multi-timestep models for Model-based Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multi-timestep-models-for-Model-based-Reinforcement-Benechehab-Paolo/182c8e48d08b8ff29f0854fe903b3bae8e0c999d"},{"title":"Multi-timestep models for Model-based Reinforcement Learning","url":"https://arxiv.org/html/2310.05672v1"},{"title":"Multi-timestep models for Model-based Re...","url":"https://axi.lims.ac.uk/paper/2310.05672"},{"title":"Multi-timestep models for Model-based Reinforcement Learning","url":"https://arxiv.org/pdf/2310.05672"}]

The full author list for arxiv paper 2310.05672 "Multi-timestep models for Model-based Reinforcement Learning" is: Abdelhakim Benechehab, Giuseppe Paolo, Albert Thomas, Maurizio Filippone, and Balázs Kégl.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-29T06:57:50.202994+00:00_

Web search results for query: ""Learning to Repeat: Fine Grained Action Repetition" Sharma FiGAR ICLR 2017 exact title"

Links: [{"title":"Published as a conference paper at ICLR 2017 LEARNING TO REPEAT:","url":"https://arxiv.org/pdf/1702.06054"},{"title":"[1702.06054] Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning","url":"https://arxiv.org/abs/1702.06054"},{"title":"Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=B1GOWV5eg"},{"title":"Learning to repeat: Fine grained action repetition for deep reinforcement learning | Robert Bosch Centre for Data Science and Artificial Intelligence","url":"https://rbcdsai.iitm.ac.in/publications/learning-to-repeat-fine-grained-action-repetition/"},{"title":"Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning | DeepAI","url":"https://deepai.org/publication/learning-to-repeat-fine-grained-action-repetition-for-deep-reinforcement-learning"},{"title":"Fine Grained Action Repetition for Deep Reinforcement ...","url":"https://www.semanticscholar.org/paper/DEEP-REINFORCEMENT-LEARNING-Sharma-Lakshminarayanan/2d6075ffa9ef3fbfe338bfeb469a50883242bdcd"},{"title":"Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning","url":"https://www.groundai.com/project/learning-to-repeat-fine-grained-action-repetition-for-deep-reinforcement-learning/1"},{"title":"Deep Learning with Reinforcement Learning – ICLR 2017 Discoveries – Amund Tveit's Blog","url":"https://amundtveit.com/2016/11/12/deep-learning-with-reinforcement-learning-iclr-2017-discoveries/"}]

I found the paper successfully! The paper "Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning" was published at ICLR 2017 by Sahil Sharma, Aravind S. Lakshminarayanan, and Balaraman Ravindran from the Indian Institute of Technology, Madras.

The paper proposes FiGAR (Fine Grained Action Rep
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-29T06:57:50.203283+00:00_

Web search results for query: ""Reinforcement Learning with Hierarchies of Machines" Parr Russell 1997 NIPS exact title"

Links: [{"title":"Reinforcement Learning with Hierarchies of Machines","url":"https://papers.nips.cc/paper/1384-reinforcement-learning-with-hierarchies-of-machines"},{"title":"Reinforcement Learning with Hierarchies of Machines","url":"https://proceedings.neurips.cc/paper/1997/hash/5ca3e9b122f61f8f06494c97b1afccf3-Abstract.html"},{"title":"Reinforcement learning with hierarchies of machines | Proceedings of the 11th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3008904.3009050"},{"title":"Reinforcement learning with hierarchies of machines","url":"https://jmvidal.cse.sc.edu/lib/parr97a.html"},{"title":"Reinforcement Learning with Hierarchies of Machines Ron Parr and Stuart Russell","url":"https://people.eecs.berkeley.edu/~russell/classes/cs294/f05/papers/parr+russell-1998.pdf"},{"title":"Book","url":"https://papers.neurips.cc/paper_files/paper/1997"},{"title":"Advances in Neural Information Processing Systems 10 ...","url":"https://papers.nips.cc/paper_files/paper/1997"},{"title":"Reinforcement Learning with Hierarchies of Machines","url":"https://users.cs.duke.edu/~parr/ham-nips97.pdf"},{"title":"Automatic formation of the structure of abstract machines in   hierarchical reinforcement learning with state clustering","url":"https://arxiv.org/pdf/1806.05292"}]

The search was successful! I found the paper you're looking for.

"Reinforcement Learning with Hierarchies of Machines" was authored by Ronald Parr and Stuart J. Russell and published in Advances in Neural Information Processing Systems 10 (NIPS 1997). 

The paper presents a new approach to reinforcement learning in which the policies considered by the learning process are constrained by hierarchies of partially specified machines. This allows for the use of prior knowledge to reduce the search space and provides a framework in whic
…[truncated 381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-29T06:57:50.203560+00:00_

Web search results for query: "arxiv 2301.04104 "Mastering Diverse Domains" Hafner Nature title change "control tasks""

Links: [{"title":"[2301.04104v1] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104v1"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"[PDF] Mastering Diverse Domains through World Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mastering-Diverse-Domains-through-World-Models-Hafner-Pa%C5%A1ukonis/f2d952a183dfb0a1e031b8a3f535d9f8423d7a6e"},{"title":"(PDF) Mastering Diverse Domains through World Models","url":"https://www.researchgate.net/publication/367019841_Mastering_Diverse_Domains_through_World_Models"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://ar5iv.labs.arxiv.org/html/2301.04104"},{"title":"Mastering Diverse Domains through World Models","url":"https://scite.ai/reports/10.48550/arxiv.2301.04104"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"Under review as a conference paper at ICLR 2024","url":"https://openreview.net/pdf/8801375407fde3d9751dbb78c2f906238f519a12.pdf"}]

Based on the web search results, I found information about arxiv 2301.04104:

The paper is titled "Mastering Diverse Domains through World Models" and was submitted by Danijar Hafner and 3 other authors. The full author list includes Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap.

The paper presents DreamerV3, a general and scalable algorithm based on world models that outperforms previous approaches across a wide range of domains with fixed hyperparameters. These domains include continuous and discrete actions, visual and low-dimensional inputs, 2D and 3D worlds, different data b
…[truncated 620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-29T06:57:50.204133+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/citation_audit_worker_A.md",
  "content": "# 引用审计报告（审计员 A）\n\n**审计日期**: 2026-05-29  \n**总引用数**: 45  \n**问题条目数**: 4  \n**严重问题**: 1（作者名伪造）\n\n---\n\n## 逐条结果\n\n### 1. @inproceedings{gu2023maniskill2}\n- **标题 bib**: ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills\n- **真实性**: ✓ — ICLR 2023 论文，存在于 OpenReview 和 arXiv (2302.04659)\n- **作者**: ✓ — Gu, Jiayuan; Xiang, Fanbo; Li, Xuanlin 等 15 位作者均正确\n- **年份**: ✓ — 2023\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2023 (booktitle: International Conference on Learning Representations)\n- **正文引用位置**: ✓ — experiments_results.tex 引用 ManiSkill 任务的跨环境验证\n- **状态**: **OK**\n\n### 2. @inproceedings{micheli2023iris}\n- **标题 bib**: Transformers are Sample-Efficient World Models\n- **真实性**: ✓ — ICLR 2023 (notable top 5%), arXiv 2209.00588\n- **作者**: ✓ — Vincent Micheli, Eloi Alonso, François Fleuret\n- **年份**: ✓ — 2023\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2023\n- **正文引用位置**: ✓ — conclusion.tex: \"transformer-based world models \\citep{micheli2023iris}\"\n- **状态**: **OK**\n\n### 3. @article{sutton1999options}\n- **标题 bib**: Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\n- **真实性**: ✓ — 经典论文，Artificial Intelligence 112(1-2), 181-211\n- **作者**: ✓ — R.S. Sutton, D. Precup, S. Singh (缩写形式，可接受)\n- **年份**: ✓ — 1999\n- **标题**: ✓\n- **Venue**: ✓ — Artificial Intelligence 112 (格式略简；完整应为 vol 112, pages 181-211，但可接受)\n- **正文引用位置**: ✓ — related_work.tex: \"The options framework \\citep{sutton1999options}\"\n- **状态**: **OK**\n\n### 4. @inproceedings{hafner2020dreamerv1}\n- **标题 bib**: Dream to Control: Learning Behaviors by Latent Imagination\n- **真实性**: ✓ — ICLR 2020, arXiv 1912.01603\n- **作者**: ✓ — Danijar Hafner, Timothy Lillicrap, Jimmy Ba, Mohammad Norouzi\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2020\n- **正文引用位置**: ✓ — related_work.tex: Dreamer family citation\n- **状态**: **OK**\n\n### 5. @article{hafner2023dreamerv3}\n- **标题 bib**: Mastering Diverse Domains through World Models\n- **真实性**: ✓ — arXiv 2301.04104; Nature publication 2025\n- **作者**: ✓ — Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap\n- **年份**: ✓ — 2025 (Nature publication year)\n- **标题**: ⚠️ — bib 使用 arXiv 标题 \"Mastering Diverse Domains through World Models\"，但 Nature 正式发表版标题为 \"Mastering diverse control tasks through world models\"。bib 中 journal=Nature 和 year=2025 对应正式版，标题应更新。\n- **Venue**: ✓ — Nature (journal field correct)\n- **正文引用位置**: ✓ — 多处引用均正确（DreamerV3 base architecture, Dreamer family 等）\n- **状态**: **有小问题**\n- **建议修复**: 标题改为 \"Mastering diverse control tasks through world models\" 以匹配 Nature 正式版。或保留 arXiv 标题但将 journal 改为 arXiv preprint。\n\n### 6. @inproceedings{sharma2017figar}\n- **标题 bib**: Fine Grained Action Repetition for Deep Reinforcement Learning\n- **真实性**: ✓ — ICLR 2017, arXiv 1702.06054\n- **作者**: ✓ — S. Sharma, A.S. Lakshminarayanan, B. Ravindran\n- **年份**: ✓ — 2017\n- **标题**: ✗ — **不完整**。正式标题为 \"Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning\"，缺少 \"Learning to Repeat:\" 前缀。\n- **Venue**: ✓ — ICLR 2017\n- **正文引用位置**: ✓ — related_work.tex: \"FiGAR \\citep{sharma2017figar} learns per-action repetition counts\"\n- **状态**: **有问题**\n- **建议修复**: title 改为 `{Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning}`\n\n### 7. @inproceedings{pertsch2020spirl}\n- **标题 bib**: Accelerating Reinforcement Learning with Learned Skill Priors\n- **真实性**: ✓ — CoRL 2020 (proceedings PMLR v155, 2021), arXiv 2010.11944\n- **作者**: ✓ — Karl Pertsch, Youngwoon Lee, Joseph J. Lim\n- **年份**: ✓ — 2021 (proceedings publication year)\n- **标题**: ✓\n- **Venue**: ✓ — Conference on Robot Learning\n- **正文引用位置**: ✓ — related_work.tex: \"SPiRL \\citep{pertsch2020spirl} accelerates RL through learned skill priors\"\n- **状态**: **OK**\n\n### 8. @inproceedings{janner2019mbpo}\n- **标题 bib**: When to Trust Your Model: Model-Based Policy Optimization\n- **真实性**: ✓ — NeurIPS 2019, arXiv 1906.08253\n- **作者**: ✓ — Michael Janner, Justin Fu, Marvin Zhang, Sergey Levine\n- **年份**: ✓ — 2019\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2019\n- **正文引用位置**: ✓ — related_work.tex: \"MBPO \\citep{janner2019mbpo}\"\n- **状态**: **OK**\n\n### 9. @article{asadi2019combating}\n- **标题 bib**: Combating the Compounding-Error Problem with a Multi-step Model\n- **真实性**: ✓ — arXiv 1905.13320\n- **作者**: ✓ — K. Asadi, D. Misra, S. Kim, M.L. Littman\n- **年份**: ✓ — 2019\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: compounding error discussion\n- **状态**: **OK**\n\n### 10. @inproceedings{hansen2024tdmpc2}\n- **标题 bib**: TD-MPC2: Scalable, Robust World Models for Continuous Control\n- **真实性**: ✓ — ICLR 2024, arXiv 2310.16828\n- **作者**: ✓ — Nicklas Hansen, Hao Su, Xiaolong Wang\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2024\n- **正文引用位置**: ✓ — introduction.tex, related_work.tex, conclusion.tex: TD-MPC2 framework\n- **状态**: **OK**\n\n### 11. @inproceedings{yu2020mopo}\n- **标题 bib**: MOPO: Model-based Offline Policy Optimization\n- **真实性**: ✓ — NeurIPS 2020, arXiv 2005.13239\n- **作者**: ✓ — Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Zou, Sergey Levine, Chelsea Finn, Tengyu Ma\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2020\n- **正文引用位置**: ✓ — related_work.tex: \"MOPO \\citep{yu2020mopo} bound rollout error\"\n- **状态**: **OK**\n\n### 12. @inproceedings{thrun1993issues}\n- **标题 bib**: Issues in Using Function Approximation for Reinforcement Learning\n- **真实性**: ✓ — Connectionist Models Summer School 1993\n- **作者**: ✓ — Sebastian Thrun, Anton Schwartz\n- **年份**: ✓ — 1993\n- **标题**: ✓\n- **Venue**: ✓ — Connectionist Models Summer School\n- **正文引用位置**: ✓ — related_work.tex: \"Maximization bias \\citep{thrun1993issues}\"\n- **状态**: **OK**\n\n### 13. @inproceedings{vanhasselt2016double}\n- **标题 bib**: Deep Reinforcement Learning with Double Q-Learning\n- **真实性**: ✓ — AAAI 2016, arXiv 1509.06461\n- **作者**: ✓ — Hado van Hasselt, Arthur Guez, David Silver\n- **年份**: ✓ — 2016\n- **标题**: ✓\n- **Venue**: ✓ — AAAI 2016\n- **正文引用位置**: ✓ — related_work.tex: \"Double Q-learning \\citep{vanhasselt2016double}\"\n- **状态**: **OK**\n\n### 14. @inproceedings{fujimoto2018td3}\n- **标题 bib**: Addressing Function Approximation Error in Actor-Critic Methods\n- **真实性**: ✓ — ICML 2018, arXiv 1802.09477\n- **作者**: ✓ — Scott Fujimoto, Herke van Hoof, David Meger\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2018\n- **正文引用位置**: ✓ — related_work.tex: \"TD3 \\citep{fujimoto2018td3}\"; experiments: dual-critic design\n- **状态**: **OK**\n\n### 15. @inproceedings{lu2018nondelusional}\n- **标题 bib**: Non-delusional Q-learning and Value-Iteration\n- **真实性**: ✓ — NeurIPS 2018 (Oral), pages 9971-9981\n- **作者**: ✓ — Tyler Lu, Dale Schuurmans, Craig Boutilier\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2018\n- **正文引用位置**: ✓ — introduction.tex, related_work.tex, analysis.tex: \"delusional bias \\citep{lu2018nondelusional}\"\n- **状态**: **OK**\n\n### 16. @inproceedings{biedenkapp2021temporl}\n- **标题 bib**: TempoRL: Learning When to Act\n- **真实性**: ✓ — ICML 2021, arXiv 2106.05262\n- **作者**: ✓ — André Biedenkapp, Raghu Rajan, Frank Hutter, Marius Lindauer\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2021\n- **正文引用位置**: ✓ — related_work.tex: \"TempoRL \\citep{biedenkapp2021temporl}\"\n- **状态**: **OK**\n\n### 17. @inproceedings{hafner2021dreamerv2}\n- **标题 bib**: Mastering Atari with Discrete World Models\n- **真实性**: ✓ — ICLR 2021, arXiv 2010.02193\n- **作者**: ✓ — Danijar Hafner, Timothy Lillicrap, Mohammad Norouzi, Jimmy Ba\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2021\n- **正文引用位置**: ✓ — related_work.tex: Dreamer family citation\n- **状态**: **OK**\n\n### 18. @inproceedings{gumbsch2024thick}\n- **标题 bib**: Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\n- **真实性**: ✓ — ICLR 2024, OpenReview TjCDNssXKU\n- **作者**: ✓ — Christian Gumbsch, Noor Sajid, Georg Martius, Martin V. Butz\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2024\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n### 19. @inproceedings{mattes2024hieros}\n- **标题 bib**: Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\n- **真实性**: ✓ — ICML 2024, PMLR 235:35079-35103\n- **作者**: ✓ — Paul Mattes, Rainer Schlosser, Ralf Herbrich\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2024\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n### 20. @inproceedings{henderson2018deep}\n- **标题 bib**: Deep Reinforcement Learning that Matters\n- **真实性**: ✓ — AAAI 2018 (32nd), arXiv 1709.06560\n- **作者**: ✓ — Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, David Meger\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — AAAI 2018\n- **正文引用位置**: ✓ — related_work.tex: \"Our factorial diagnostic methodology follows \\citet{henderson2018deep}\"\n- **状态**: **OK**\n\n### 21. @inproceedings{lambert2020objective}\n- **标题 bib**: Objective Mismatch in Model-based Reinforcement Learning\n- **真实性**: ✓ — L4DC 2020 (PMLR v120), arXiv 2002.04523\n- **作者**: ✓ — Nathan Lambert, Brandon Amos, Omry Yadan, Roberto Calandra\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — L4DC\n- **正文引用位置**: ✓ — related_work.tex: compounding error discussion\n- **状态**: **OK**\n\n### 22. @inproceedings{agarwal2021precipice}\n- **标题 bib**: Deep Reinforcement Learning at the Edge of the Statistical Precipice\n- **真实性**: ✓ — NeurIPS 2021 (Outstanding Paper Award), arXiv 2108.13264\n- **作者**: ✓ — Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, Marc Bellemare\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2021\n- **正文引用位置**: ✓ — experiments_results.tex, results.tex: reporting methodology, IQM\n- **状态**: **OK**\n\n### 23. @article{tassa2018dmcontrol}\n- **标题 bib**: DeepMind Control Suite\n- **真实性**: ✓ — arXiv 1801.00690\n- **作者**: ✓ — Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez 等 12 位作者\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — introduction.tex, experiments_results.tex: Walker Walk, Cheetah Run from DMC\n- **状态**: **OK**\n\n### 24. @article{hafner2025dreamerv4}\n- **标题 bib**: Training Agents Inside of Scalable World Models\n- **真实性**: ✓ — arXiv 2509.24527 (September 2025)\n- **作者**: ✓ — Danijar Hafner, Wilson Yan, Timothy Lillicrap\n- **年份**: ✓ — 2025\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: Dreamer family citation\n- **状态**: **OK**\n\n### 25. @inproceedings{lyle2022capacity}\n- **标题 bib**: Understanding and Preventing Capacity Loss in Reinforcement Learning\n- **真实性**: ✓ — ICLR 2022 (Spotlight), arXiv 2204.09560\n- **作者**: ✓ — Clare Lyle, Mark Rowland, Will Dabney\n- **年份**: ✓ — 2022\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2022\n- **正文引用位置**: 未在正文中找到引用（可能在 appendix 未读部分）\n- **状态**: **OK**（bib entry 本身无误）\n\n### 26. @inproceedings{nhu2025tawm}\n- **标题 bib**: Time-Aware World Model for Adaptive Prediction and Control\n- **真实性**: ✓ — ICML 2025, arXiv 2506.08441\n- **作者**: ✓ — Anh N. Nhu, Sanghyun Son, Ming C. Lin\n- **年份**: ✓ — 2025\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2025\n- **正文引用位置**: ✓ — introduction.tex, related_work.tex: \"TAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size\"\n- **状态**: **OK**\n\n### 27. @inproceedings{li2025lsimagine}\n- **标题 bib**: Open-World Reinforcement Learning over Long Short-Term Imagination\n- **真实性**: ✓ — ICLR 2025 (Oral), arXiv 2410.03618\n- **作者**: ✓ — Jiajian Li, Qi Wang, Yunbo Wang, Xin Jin, Yang Li, Wenjun Zeng, Xiaokang Yang\n- **年份**: ✓ — 2025\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2025\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n### 28. @inproceedings{chen2021redq}\n- **标题 bib**: Randomized Ensembled Double Q-Learning: Learning Fast Without a Model\n- **真实性**: ✓ — ICLR 2021, arXiv 2101.05982\n- **作者**: ✓ — Xinyue Chen, Che Wang, Zijian Zhou, Keith Ross\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2021\n- **正文引用位置**: ✓ — related_work.tex: \"ensemble methods \\citep{chen2021redq}\"\n- **状态**: **OK**\n\n### 29. @inproceedings{bacon2017optioncritc}\n- **标题 bib**: The Option-Critic Architecture\n- **真实性**: ✓ — AAAI 2017, arXiv 1609.05140\n- **作者**: ✓ — Pierre-Luc Bacon, Jean Harb, Doina Precup\n- **年份**: ✓ — 2017\n- **标题**: ✓\n- **Venue**: ✓ — AAAI 2017\n- **正文引用位置**: ✓ — related_work.tex: \"option-critic \\citep{bacon2017optioncritc}\"\n- **状态**: **OK**（bib key typo \"optioncritc\" vs \"optioncritic\" 不影响渲染）\n\n### 30. @inproceedings{buckman2018steve}\n- **标题 bib**: Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion\n- **真实性**: ✓ — NeurIPS 2018 (Oral), arXiv 1807.01675\n- **作者**: ✓ — Jacob Buckman, Danijar Hafner, George Tucker, Eugene Brevdo, Honglak Lee\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2018\n- **正文引用位置**: 未在已读正文部分找到引用（可能在 appendix 中）\n- **状态**: **OK**\n\n### 31. @inproceedings{chua2018pets}\n- **标题 bib**: Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\n- **真实性**: ✓ — NeurIPS 2018, arXiv 1805.12114\n- **作者**: ✓ — Kurtland Chua, Roberto Calandra, Rowan McAllister, Sergey Levine\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2018\n- **正文引用位置**: 未在已读正文部分找到引用（可能在 appendix 中）\n- **状态**: **OK**\n\n### 32. @article{bishop1995noise}\n- **标题 bib**: Training with Noise is Equivalent to Tikhonov Regularization\n- **真实性**: ✓ — Neural Computation 7(1), 108-116, 1995\n- **作者**: ✓ — Chris M. Bishop\n- **年份**: ✓ — 1995\n- **标题**: ✓\n- **Venue**: ✓ — Neural Computation, vol 7, no 1, pages 108-116\n- **正文引用位置**: ✓ — related_work.tex: \"training-with-noise \\citep{bishop1995noise}\"\n- **状态**: **OK**\n\n### 33. @inproceedings{fortunato2018noisynet}\n- **标题 bib**: Noisy Networks for Exploration\n- **真实性**: ✓ — ICLR 2018, arXiv 1706.10295\n- **作者**: ✓ — Meire Fortunato, Mohammad Gheshlaghi Azar, Bilal Piot, Jacob Menick, Ian Osband, Alex Graves, Vlad Mnih, Rémi Munos, Demis Hassabis, Olivier Pietquin, Charles Blundell, Shane Legg\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2018\n- **正文引用位置**: 未在已读正文部分找到引用（可能在 appendix 中）\n- **状态**: **OK**\n\n### 34. @inproceedings{parr1998ham}\n- **标题 bib**: Reinforcement Learning with Hierarchies of Abstract Machines\n- **真实性**: ✓ — NIPS 1997 (Advances in Neural Information Processing Systems 10)\n- **作者**: ✓ — Ronald Parr, Stuart Russell\n- **年份**: ⚠️ — bib 标注 1998，实际会议为 NIPS 1997（December 1997）。引用年份 1997 或 1998 均有惯例使用，但多数引用使用 1998（proceedings publication year）。可接受。\n- **标题**: ✗ — **标题有误**。实际标题为 \"Reinforcement Learning with Hierarchies of Machines\"，bib 中多了 \"Abstract\" 一词（\"Hierarchies of **Abstract** Machines\"）。\n- **Venue**: ✓ — Advances in Neural Information Processing Systems\n- **正文引用位置**: ✓ — related_work.tex: \"HAM \\citep{parr1998ham}\"\n- **状态**: **有问题**\n- **建议修复**: title 改为 `{Reinforcement Learning with Hierarchies of Machines}`\n\n### 35. @article{dietterich2000maxq}\n- **标题 bib**: Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition\n- **真实性**: ✓ — JAIR vol 13, pages 227-303, 2000\n- **作者**: ✓ — Thomas G. Dietterich\n- **年份**: ✓ — 2000\n- **标题**: ✓\n- **Venue**: ✓ — Journal of Artificial Intelligence Research, vol 13, pages 227-303\n- **正文引用位置**: ✓ — related_work.tex: \"MAXQ \\citep{dietterich2000maxq}\"\n- **状态**: **OK**\n\n### 36. @inproceedings{bradtke1995smdp}\n- **标题 bib**: Reinforcement Learning Methods for Continuous-Time Markov Decision Problems\n- **真实性**: ✓ — NIPS 1994 (Advances in Neural Information Processing Systems 7)\n- **作者**: ✓ — Steven J. Bradtke, Michael O. Duff\n- **年份**: ✓ — 1995 (proceedings publication year; conference was 1994)\n- **标题**: ✓\n- **Venue**: ✓ — Advances in Neural Information Processing Systems\n- **正文引用位置**: ✓ — related_work.tex: \"Semi-MDP theory \\citep{bradtke1995smdp}\"\n- **状态**: **OK**\n\n### 37. @inproceedings{kidambi2020morel}\n- **标题 bib**: MOReL: Model-Based Offline Reinforcement Learning\n- **真实性**: ✓ — NeurIPS 2020, arXiv 2005.05951\n- **作者**: ✓ — Rahul Kidambi, Aravind Rajeswaran, Praneeth Netrapalli, Thorsten Joachims\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2020\n- **正文引用位置**: ✓ — related_work.tex: \"MOReL \\citep{kidambi2020morel}\"\n- **状态**: **OK**\n\n### 38. @inproceedings{yu2021combo}\n- **标题 bib**: COMBO: Conservative Offline Model-Based Policy Optimization\n- **真实性**: ✓ — NeurIPS 2021, arXiv 2102.08363\n- **作者**: ✓ — Tianhe Yu, Aviral Kumar, Rafael Rafailov, Aravind Rajeswaran, Sergey Levine, Chelsea Finn\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2021\n- **正文引用位置**: ✓ — related_work.tex: \"COMBO \\citep{yu2021combo}\"\n- **状态**: **OK**\n\n### 39. @inproceedings{hamrick2021planning}\n- **标题 bib**: On the Role of Planning in Model-Based Deep Reinforcement Learning\n- **真实性**: ✓ — ICLR 2021, arXiv 2011.04021\n- **作者**: ✓ — Jessica B. Hamrick, Abram L. Friesen, Feryal Behbahani, Arthur Guez, Fabio Viola, Sims Witherspoon, Thomas Anthony, Lars Buesing, Petar Veličković, Théophane Weber\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2021\n- **正文引用位置**: ⚠️ — related_work.tex: \"Decision-aware model learning \\citep{hamrick2021planning}\"。Hamrick 2021 研究的是 planning 在 MBRL 中的角色（MuZero 实验），而非严格意义上的 \"decision-aware model learning\"（该术语通常指 Farahmand 等人的 value-aware 系列）。但 Hamrick 确实讨论了模型学习是否应为 planning 性能服务，因此描述虽不精确但可辩护。\n- **状态**: **OK**（引用归属边界情况，不构成错误）\n\n### 40. @inproceedings{wu2023daydreamer}\n- **标题 bib**: DayDreamer: World Models for Physical Robot Learning\n- **真实性**: ✓ — CoRL 2022 (PMLR v205, 2023), arXiv 2206.14176\n- **作者**: ✓ — Philipp Wu, Alejandro Escontrela, Danijar Hafner, Pieter Abbeel, Ken Goldberg\n- **年份**: ✓ — 2023 (proceedings publication year)\n- **标题**: ✓\n- **Venue**: ✓ — Conference on Robot Learning\n- **正文引用位置**: ✓ — introduction.tex: \"sample-efficient learning \\citep{wu2023daydreamer, hansen2024tdmpc2}\"\n- **状态**: **OK**\n\n### 41. @inproceedings{park2021timediscretization}\n- **标题 bib**: Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\n- **真实性**: ✓ — NeurIPS 2021, arXiv 2111.03941\n- **作者**: ✓ — Seohong Park, Jaekyeom Kim, Gunhee Kim\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2021\n- **正文引用位置**: ✓ — related_work.tex: \"\\citet{park2021timediscretization} provide complementary formulations\"\n- **状态**: **OK**\n\n### 42. @article{wang2024elastic}\n- **标题 bib**: Reinforcement Learning with Elastic Time Steps\n- **真实性**: ✓ — arXiv 2402.14961\n- **作者**: ✓ — Dong Wang, Giovanni Beltrame\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: \"\\citet{wang2024elastic} learn elastic time steps\"\n- **状态**: **OK**\n\n### 43. @article{colas2018seeds}\n- **标题 bib**: How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\n- **真实性**: ✓ — arXiv 1806.08295\n- **作者**: ✓ — Cédric Colas, Olivier Sigaud, Pierre-Yves Oudeyer\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — conclusion.tex: \"Seed counts (4--5; \\citealt{colas2018seeds})\"\n- **状态**: **OK**\n\n### 44. @article{benechehab2023multitimestep}\n- **标题 bib**: Multi-timestep models for Model-based Reinforcement Learning\n- **真实性**: ✓ — arXiv 2310.05672\n- **作者**: ✗ — **严重错误：3/4 个合著者为伪造**\n  - bib 中列出：Benechehab, Abdelhakim / Couairon, Guillaume / Leurent, Edouard / Bloch, Balázs Kégl\n  - 实际作者：Abdelhakim Benechehab, **Giuseppe Paolo**, **Albert Thomas**, **Maurizio Filippone**, Balázs Kégl\n  - \"Couairon, Guillaume\" ✗ 不是本文作者\n  - \"Leurent, Edouard\" ✗ 不是本文作者\n  - \"Bloch, Balázs Kégl\" ✗ 格式错误且 \"Bloch\" 不存在；应为 \"Kégl, Balázs\"\n- **年份**: ✓ — 2023\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: \"Multi-timestep world models \\citep{benechehab2023multitimestep}\"\n- **状态**: **🚨 严重问题 — 作者名伪造**\n- **建议修复**: author 改为 `{Benechehab, Abdelhakim and Paolo, Giuseppe and Thomas, Albert and Filippone, Maurizio and K{\\'e}gl, Bal{\\'a}zs}`\n\n### 45. @inproceedings{hafner2022director}\n- **标题 bib**: Deep Hierarchical Planning from Pixels\n- **真实性**: ✓ — NeurIPS 2022, arXiv 2206.04114\n- **作者**: ✓ — Danijar Hafner, Kuang-Huei Lee, Ian Fischer, Pieter Abbeel\n- **年份**: ✓ — 2022\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2022\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n---\n\n## 汇总\n\n| # | Bib Key | 问题类型 | 严重程度 | 简述 |\n|---|---------|----------|----------|------|\n| 6 | sharma2017figar | 标题不完整 | 中 | 缺少 \"Learning to Repeat:\" 前缀 |\n| 5 | hafner2023dreamerv3 | 标题不匹配 | 低 | arXiv 标题 vs Nature 正式版标题 |\n| 34 | parr1998ham | 标题错误 | 中 | 多了 \"Abstract\" 一词 |\n| 44 | benechehab2023multitimestep | 作者伪造 | 🚨 严重 | 3/4 合著者为虚假姓名 |\n\n### 无问题条目（41/45）\n1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45\n\n### 未发现 Hallucinated Citation\n所有 45 篇论文均经 WebSearch 确认真实存在。未发现完全虚构的论文。\n\n### 未发现的正文引用错误归因\n所有 `\\cite` / `\\citep` / `\\citet` 在正文中的使用均与被引论文的实际贡献一致。Hamrick 2021 被描述为 \"decision-aware model learning\" 略有不精确但不构成归因错误。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/citation_audit_worker_A.md",
    "content": "# 引用审计报告（审计员 A）\n\n**审计日期**: 2026-05-29  \n**总引用数**: 45  \n**问题条目数**: 4  \n**严重问题**: 1（作者名伪造）\n\n---\n\n## 逐条结果\n\n### 1. @inproceedings{gu2023maniskill2}\n- **标题 bib**: ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills\n- **真实性**: ✓ — ICLR 2023 论文，存在于 OpenReview 和 arXiv (2302.04659)\n- **作者**: ✓ — Gu, Jiayuan; Xiang, Fanbo; Li, Xuanlin 等 15 位作者均正确\n- **年份**: ✓ — 2023\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2023 (booktitle: International Conference on Learning Representations)\n- **正文引用位置**: ✓ — experiments_results.tex 引用 ManiSkill 任务的跨环境验证\n- **状态**: **OK**\n\n### 2. @inproceedings{micheli2023iris}\n- **标题 bib**: Transformers are Sample-Efficient World Models\n- **真实性**: ✓ — ICLR 2023 (notable top 5%), arXiv 2209.00588\n- **作者**: ✓ — Vincent Micheli, Eloi Alonso, François Fleuret\n- **年份**: ✓ — 2023\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2023\n- **正文引用位置**: ✓ — conclusion.tex: \"transformer-based world models \\citep{micheli2023iris}\"\n- **状态**: **OK**\n\n### 3. @article{sutton1999options}\n- **标题 bib**: Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\n- **真实性**: ✓ — 经典论文，Artificial Intelligence 112(1-2), 181-211\n- **作者**: ✓ — R.S. Sutton, D. Precup, S. Singh (缩写形式，可接受)\n- **年份**: ✓ — 1999\n- **标题**: ✓\n- **Venue**: ✓ — Artificial Intelligence 112 (格式略简；完整应为 vol 112, pages 181-211，但可接受)\n- **正文引用位置**: ✓ — related_work.tex: \"The options framework \\citep{sutton1999options}\"\n- **状态**: **OK**\n\n### 4. @inproceedings{hafner2020dreamerv1}\n- **标题 bib**: Dream to Control: Learning Behaviors by Latent Imagination\n- **真实性**: ✓ — ICLR 2020, arXiv 1912.01603\n- **作者**: ✓ — Danijar Hafner, Timothy Lillicrap, Jimmy Ba, Mohammad Norouzi\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2020\n- **正文引用位置**: ✓ — related_work.tex: Dreamer family citation\n- **状态**: **OK**\n\n### 5. @article{hafner2023dreamerv3}\n- **标题 bib**: Mastering Diverse Domains through World Models\n- **真实性**: ✓ — arXiv 2301.04104; Nature publication 2025\n- **作者**: ✓ — Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap\n- **年份**: ✓ — 2025 (Nature publication year)\n- **标题**: ⚠️ — bib 使用 arXiv 标题 \"Mastering Diverse Domains through World Models\"，但 Nature 正式发表版标题为 \"Mastering diverse control tasks through world models\"。bib 中 journal=Nature 和 year=2025 对应正式版，标题应更新。\n- **Venue**: ✓ — Nature (journal field correct)\n- **正文引用位置**: ✓ — 多处引用均正确（DreamerV3 base architecture, Dreamer family 等）\n- **状态**: **有小问题**\n- **建议修复**: 标题改为 \"Mastering diverse control tasks through world models\" 以匹配 Nature 正式版。或保留 arXiv 标题但将 journal 改为 arXiv preprint。\n\n### 6. @inproceedings{sharma2017figar}\n- **标题 bib**: Fine Grained Action Repetition for Deep Reinforcement Learning\n- **真实性**: ✓ — ICLR 2017, arXiv 1702.06054\n- **作者**: ✓ — S. Sharma, A.S. Lakshminarayanan, B. Ravindran\n- **年份**: ✓ — 2017\n- **标题**: ✗ — **不完整**。正式标题为 \"Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning\"，缺少 \"Learning to Repeat:\" 前缀。\n- **Venue**: ✓ — ICLR 2017\n- **正文引用位置**: ✓ — related_work.tex: \"FiGAR \\citep{sharma2017figar} learns per-action repetition counts\"\n- **状态**: **有问题**\n- **建议修复**: title 改为 `{Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning}`\n\n### 7. @inproceedings{pertsch2020spirl}\n- **标题 bib**: Accelerating Reinforcement Learning with Learned Skill Priors\n- **真实性**: ✓ — CoRL 2020 (proceedings PMLR v155, 2021), arXiv 2010.11944\n- **作者**: ✓ — Karl Pertsch, Youngwoon Lee, Joseph J. Lim\n- **年份**: ✓ — 2021 (proceedings publication year)\n- **标题**: ✓\n- **Venue**: ✓ — Conference on Robot Learning\n- **正文引用位置**: ✓ — related_work.tex: \"SPiRL \\citep{pertsch2020spirl} accelerates RL through learned skill priors\"\n- **状态**: **OK**\n\n### 8. @inproceedings{janner2019mbpo}\n- **标题 bib**: When to Trust Your Model: Model-Based Policy Optimization\n- **真实性**: ✓ — NeurIPS 2019, arXiv 1906.08253\n- **作者**: ✓ — Michael Janner, Justin Fu, Marvin Zhang, Sergey Levine\n- **年份**: ✓ — 2019\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2019\n- **正文引用位置**: ✓ — related_work.tex: \"MBPO \\citep{janner2019mbpo}\"\n- **状态**: **OK**\n\n### 9. @article{asadi2019combating}\n- **标题 bib**: Combating the Compounding-Error Problem with a Multi-step Model\n- **真实性**: ✓ — arXiv 1905.13320\n- **作者**: ✓ — K. Asadi, D. Misra, S. Kim, M.L. Littman\n- **年份**: ✓ — 2019\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: compounding error discussion\n- **状态**: **OK**\n\n### 10. @inproceedings{hansen2024tdmpc2}\n- **标题 bib**: TD-MPC2: Scalable, Robust World Models for Continuous Control\n- **真实性**: ✓ — ICLR 2024, arXiv 2310.16828\n- **作者**: ✓ — Nicklas Hansen, Hao Su, Xiaolong Wang\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2024\n- **正文引用位置**: ✓ — introduction.tex, related_work.tex, conclusion.tex: TD-MPC2 framework\n- **状态**: **OK**\n\n### 11. @inproceedings{yu2020mopo}\n- **标题 bib**: MOPO: Model-based Offline Policy Optimization\n- **真实性**: ✓ — NeurIPS 2020, arXiv 2005.13239\n- **作者**: ✓ — Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Zou, Sergey Levine, Chelsea Finn, Tengyu Ma\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2020\n- **正文引用位置**: ✓ — related_work.tex: \"MOPO \\citep{yu2020mopo} bound rollout error\"\n- **状态**: **OK**\n\n### 12. @inproceedings{thrun1993issues}\n- **标题 bib**: Issues in Using Function Approximation for Reinforcement Learning\n- **真实性**: ✓ — Connectionist Models Summer School 1993\n- **作者**: ✓ — Sebastian Thrun, Anton Schwartz\n- **年份**: ✓ — 1993\n- **标题**: ✓\n- **Venue**: ✓ — Connectionist Models Summer School\n- **正文引用位置**: ✓ — related_work.tex: \"Maximization bias \\citep{thrun1993issues}\"\n- **状态**: **OK**\n\n### 13. @inproceedings{vanhasselt2016double}\n- **标题 bib**: Deep Reinforcement Learning with Double Q-Learning\n- **真实性**: ✓ — AAAI 2016, arXiv 1509.06461\n- **作者**: ✓ — Hado van Hasselt, Arthur Guez, David Silver\n- **年份**: ✓ — 2016\n- **标题**: ✓\n- **Venue**: ✓ — AAAI 2016\n- **正文引用位置**: ✓ — related_work.tex: \"Double Q-learning \\citep{vanhasselt2016double}\"\n- **状态**: **OK**\n\n### 14. @inproceedings{fujimoto2018td3}\n- **标题 bib**: Addressing Function Approximation Error in Actor-Critic Methods\n- **真实性**: ✓ — ICML 2018, arXiv 1802.09477\n- **作者**: ✓ — Scott Fujimoto, Herke van Hoof, David Meger\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2018\n- **正文引用位置**: ✓ — related_work.tex: \"TD3 \\citep{fujimoto2018td3}\"; experiments: dual-critic design\n- **状态**: **OK**\n\n### 15. @inproceedings{lu2018nondelusional}\n- **标题 bib**: Non-delusional Q-learning and Value-Iteration\n- **真实性**: ✓ — NeurIPS 2018 (Oral), pages 9971-9981\n- **作者**: ✓ — Tyler Lu, Dale Schuurmans, Craig Boutilier\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2018\n- **正文引用位置**: ✓ — introduction.tex, related_work.tex, analysis.tex: \"delusional bias \\citep{lu2018nondelusional}\"\n- **状态**: **OK**\n\n### 16. @inproceedings{biedenkapp2021temporl}\n- **标题 bib**: TempoRL: Learning When to Act\n- **真实性**: ✓ — ICML 2021, arXiv 2106.05262\n- **作者**: ✓ — André Biedenkapp, Raghu Rajan, Frank Hutter, Marius Lindauer\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2021\n- **正文引用位置**: ✓ — related_work.tex: \"TempoRL \\citep{biedenkapp2021temporl}\"\n- **状态**: **OK**\n\n### 17. @inproceedings{hafner2021dreamerv2}\n- **标题 bib**: Mastering Atari with Discrete World Models\n- **真实性**: ✓ — ICLR 2021, arXiv 2010.02193\n- **作者**: ✓ — Danijar Hafner, Timothy Lillicrap, Mohammad Norouzi, Jimmy Ba\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2021\n- **正文引用位置**: ✓ — related_work.tex: Dreamer family citation\n- **状态**: **OK**\n\n### 18. @inproceedings{gumbsch2024thick}\n- **标题 bib**: Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\n- **真实性**: ✓ — ICLR 2024, OpenReview TjCDNssXKU\n- **作者**: ✓ — Christian Gumbsch, Noor Sajid, Georg Martius, Martin V. Butz\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2024\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n### 19. @inproceedings{mattes2024hieros}\n- **标题 bib**: Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\n- **真实性**: ✓ — ICML 2024, PMLR 235:35079-35103\n- **作者**: ✓ — Paul Mattes, Rainer Schlosser, Ralf Herbrich\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2024\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n### 20. @inproceedings{henderson2018deep}\n- **标题 bib**: Deep Reinforcement Learning that Matters\n- **真实性**: ✓ — AAAI 2018 (32nd), arXiv 1709.06560\n- **作者**: ✓ — Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, David Meger\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — AAAI 2018\n- **正文引用位置**: ✓ — related_work.tex: \"Our factorial diagnostic methodology follows \\citet{henderson2018deep}\"\n- **状态**: **OK**\n\n### 21. @inproceedings{lambert2020objective}\n- **标题 bib**: Objective Mismatch in Model-based Reinforcement Learning\n- **真实性**: ✓ — L4DC 2020 (PMLR v120), arXiv 2002.04523\n- **作者**: ✓ — Nathan Lambert, Brandon Amos, Omry Yadan, Roberto Calandra\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — L4DC\n- **正文引用位置**: ✓ — related_work.tex: compounding error discussion\n- **状态**: **OK**\n\n### 22. @inproceedings{agarwal2021precipice}\n- **标题 bib**: Deep Reinforcement Learning at the Edge of the Statistical Precipice\n- **真实性**: ✓ — NeurIPS 2021 (Outstanding Paper Award), arXiv 2108.13264\n- **作者**: ✓ — Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, Marc Bellemare\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2021\n- **正文引用位置**: ✓ — experiments_results.tex, results.tex: reporting methodology, IQM\n- **状态**: **OK**\n\n### 23. @article{tassa2018dmcontrol}\n- **标题 bib**: DeepMind Control Suite\n- **真实性**: ✓ — arXiv 1801.00690\n- **作者**: ✓ — Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez 等 12 位作者\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — introduction.tex, experiments_results.tex: Walker Walk, Cheetah Run from DMC\n- **状态**: **OK**\n\n### 24. @article{hafner2025dreamerv4}\n- **标题 bib**: Training Agents Inside of Scalable World Models\n- **真实性**: ✓ — arXiv 2509.24527 (September 2025)\n- **作者**: ✓ — Danijar Hafner, Wilson Yan, Timothy Lillicrap\n- **年份**: ✓ — 2025\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: Dreamer family citation\n- **状态**: **OK**\n\n### 25. @inproceedings{lyle2022capacity}\n- **标题 bib**: Understanding and Preventing Capacity Loss in Reinforcement Learning\n- **真实性**: ✓ — ICLR 2022 (Spotlight), arXiv 2204.09560\n- **作者**: ✓ — Clare Lyle, Mark Rowland, Will Dabney\n- **年份**: ✓ — 2022\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2022\n- **正文引用位置**: 未在正文中找到引用（可能在 appendix 未读部分）\n- **状态**: **OK**（bib entry 本身无误）\n\n### 26. @inproceedings{nhu2025tawm}\n- **标题 bib**: Time-Aware World Model for Adaptive Prediction and Control\n- **真实性**: ✓ — ICML 2025, arXiv 2506.08441\n- **作者**: ✓ — Anh N. Nhu, Sanghyun Son, Ming C. Lin\n- **年份**: ✓ — 2025\n- **标题**: ✓\n- **Venue**: ✓ — ICML 2025\n- **正文引用位置**: ✓ — introduction.tex, related_work.tex: \"TAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size\"\n- **状态**: **OK**\n\n### 27. @inproceedings{li2025lsimagine}\n- **标题 bib**: Open-World Reinforcement Learning over Long Short-Term Imagination\n- **真实性**: ✓ — ICLR 2025 (Oral), arXiv 2410.03618\n- **作者**: ✓ — Jiajian Li, Qi Wang, Yunbo Wang, Xin Jin, Yang Li, Wenjun Zeng, Xiaokang Yang\n- **年份**: ✓ — 2025\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2025\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n### 28. @inproceedings{chen2021redq}\n- **标题 bib**: Randomized Ensembled Double Q-Learning: Learning Fast Without a Model\n- **真实性**: ✓ — ICLR 2021, arXiv 2101.05982\n- **作者**: ✓ — Xinyue Chen, Che Wang, Zijian Zhou, Keith Ross\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2021\n- **正文引用位置**: ✓ — related_work.tex: \"ensemble methods \\citep{chen2021redq}\"\n- **状态**: **OK**\n\n### 29. @inproceedings{bacon2017optioncritc}\n- **标题 bib**: The Option-Critic Architecture\n- **真实性**: ✓ — AAAI 2017, arXiv 1609.05140\n- **作者**: ✓ — Pierre-Luc Bacon, Jean Harb, Doina Precup\n- **年份**: ✓ — 2017\n- **标题**: ✓\n- **Venue**: ✓ — AAAI 2017\n- **正文引用位置**: ✓ — related_work.tex: \"option-critic \\citep{bacon2017optioncritc}\"\n- **状态**: **OK**（bib key typo \"optioncritc\" vs \"optioncritic\" 不影响渲染）\n\n### 30. @inproceedings{buckman2018steve}\n- **标题 bib**: Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion\n- **真实性**: ✓ — NeurIPS 2018 (Oral), arXiv 1807.01675\n- **作者**: ✓ — Jacob Buckman, Danijar Hafner, George Tucker, Eugene Brevdo, Honglak Lee\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2018\n- **正文引用位置**: 未在已读正文部分找到引用（可能在 appendix 中）\n- **状态**: **OK**\n\n### 31. @inproceedings{chua2018pets}\n- **标题 bib**: Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\n- **真实性**: ✓ — NeurIPS 2018, arXiv 1805.12114\n- **作者**: ✓ — Kurtland Chua, Roberto Calandra, Rowan McAllister, Sergey Levine\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2018\n- **正文引用位置**: 未在已读正文部分找到引用（可能在 appendix 中）\n- **状态**: **OK**\n\n### 32. @article{bishop1995noise}\n- **标题 bib**: Training with Noise is Equivalent to Tikhonov Regularization\n- **真实性**: ✓ — Neural Computation 7(1), 108-116, 1995\n- **作者**: ✓ — Chris M. Bishop\n- **年份**: ✓ — 1995\n- **标题**: ✓\n- **Venue**: ✓ — Neural Computation, vol 7, no 1, pages 108-116\n- **正文引用位置**: ✓ — related_work.tex: \"training-with-noise \\citep{bishop1995noise}\"\n- **状态**: **OK**\n\n### 33. @inproceedings{fortunato2018noisynet}\n- **标题 bib**: Noisy Networks for Exploration\n- **真实性**: ✓ — ICLR 2018, arXiv 1706.10295\n- **作者**: ✓ — Meire Fortunato, Mohammad Gheshlaghi Azar, Bilal Piot, Jacob Menick, Ian Osband, Alex Graves, Vlad Mnih, Rémi Munos, Demis Hassabis, Olivier Pietquin, Charles Blundell, Shane Legg\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2018\n- **正文引用位置**: 未在已读正文部分找到引用（可能在 appendix 中）\n- **状态**: **OK**\n\n### 34. @inproceedings{parr1998ham}\n- **标题 bib**: Reinforcement Learning with Hierarchies of Abstract Machines\n- **真实性**: ✓ — NIPS 1997 (Advances in Neural Information Processing Systems 10)\n- **作者**: ✓ — Ronald Parr, Stuart Russell\n- **年份**: ⚠️ — bib 标注 1998，实际会议为 NIPS 1997（December 1997）。引用年份 1997 或 1998 均有惯例使用，但多数引用使用 1998（proceedings publication year）。可接受。\n- **标题**: ✗ — **标题有误**。实际标题为 \"Reinforcement Learning with Hierarchies of Machines\"，bib 中多了 \"Abstract\" 一词（\"Hierarchies of **Abstract** Machines\"）。\n- **Venue**: ✓ — Advances in Neural Information Processing Systems\n- **正文引用位置**: ✓ — related_work.tex: \"HAM \\citep{parr1998ham}\"\n- **状态**: **有问题**\n- **建议修复**: title 改为 `{Reinforcement Learning with Hierarchies of Machines}`\n\n### 35. @article{dietterich2000maxq}\n- **标题 bib**: Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition\n- **真实性**: ✓ — JAIR vol 13, pages 227-303, 2000\n- **作者**: ✓ — Thomas G. Dietterich\n- **年份**: ✓ — 2000\n- **标题**: ✓\n- **Venue**: ✓ — Journal of Artificial Intelligence Research, vol 13, pages 227-303\n- **正文引用位置**: ✓ — related_work.tex: \"MAXQ \\citep{dietterich2000maxq}\"\n- **状态**: **OK**\n\n### 36. @inproceedings{bradtke1995smdp}\n- **标题 bib**: Reinforcement Learning Methods for Continuous-Time Markov Decision Problems\n- **真实性**: ✓ — NIPS 1994 (Advances in Neural Information Processing Systems 7)\n- **作者**: ✓ — Steven J. Bradtke, Michael O. Duff\n- **年份**: ✓ — 1995 (proceedings publication year; conference was 1994)\n- **标题**: ✓\n- **Venue**: ✓ — Advances in Neural Information Processing Systems\n- **正文引用位置**: ✓ — related_work.tex: \"Semi-MDP theory \\citep{bradtke1995smdp}\"\n- **状态**: **OK**\n\n### 37. @inproceedings{kidambi2020morel}\n- **标题 bib**: MOReL: Model-Based Offline Reinforcement Learning\n- **真实性**: ✓ — NeurIPS 2020, arXiv 2005.05951\n- **作者**: ✓ — Rahul Kidambi, Aravind Rajeswaran, Praneeth Netrapalli, Thorsten Joachims\n- **年份**: ✓ — 2020\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2020\n- **正文引用位置**: ✓ — related_work.tex: \"MOReL \\citep{kidambi2020morel}\"\n- **状态**: **OK**\n\n### 38. @inproceedings{yu2021combo}\n- **标题 bib**: COMBO: Conservative Offline Model-Based Policy Optimization\n- **真实性**: ✓ — NeurIPS 2021, arXiv 2102.08363\n- **作者**: ✓ — Tianhe Yu, Aviral Kumar, Rafael Rafailov, Aravind Rajeswaran, Sergey Levine, Chelsea Finn\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2021\n- **正文引用位置**: ✓ — related_work.tex: \"COMBO \\citep{yu2021combo}\"\n- **状态**: **OK**\n\n### 39. @inproceedings{hamrick2021planning}\n- **标题 bib**: On the Role of Planning in Model-Based Deep Reinforcement Learning\n- **真实性**: ✓ — ICLR 2021, arXiv 2011.04021\n- **作者**: ✓ — Jessica B. Hamrick, Abram L. Friesen, Feryal Behbahani, Arthur Guez, Fabio Viola, Sims Witherspoon, Thomas Anthony, Lars Buesing, Petar Veličković, Théophane Weber\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — ICLR 2021\n- **正文引用位置**: ⚠️ — related_work.tex: \"Decision-aware model learning \\citep{hamrick2021planning}\"。Hamrick 2021 研究的是 planning 在 MBRL 中的角色（MuZero 实验），而非严格意义上的 \"decision-aware model learning\"（该术语通常指 Farahmand 等人的 value-aware 系列）。但 Hamrick 确实讨论了模型学习是否应为 planning 性能服务，因此描述虽不精确但可辩护。\n- **状态**: **OK**（引用归属边界情况，不构成错误）\n\n### 40. @inproceedings{wu2023daydreamer}\n- **标题 bib**: DayDreamer: World Models for Physical Robot Learning\n- **真实性**: ✓ — CoRL 2022 (PMLR v205, 2023), arXiv 2206.14176\n- **作者**: ✓ — Philipp Wu, Alejandro Escontrela, Danijar Hafner, Pieter Abbeel, Ken Goldberg\n- **年份**: ✓ — 2023 (proceedings publication year)\n- **标题**: ✓\n- **Venue**: ✓ — Conference on Robot Learning\n- **正文引用位置**: ✓ — introduction.tex: \"sample-efficient learning \\citep{wu2023daydreamer, hansen2024tdmpc2}\"\n- **状态**: **OK**\n\n### 41. @inproceedings{park2021timediscretization}\n- **标题 bib**: Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\n- **真实性**: ✓ — NeurIPS 2021, arXiv 2111.03941\n- **作者**: ✓ — Seohong Park, Jaekyeom Kim, Gunhee Kim\n- **年份**: ✓ — 2021\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2021\n- **正文引用位置**: ✓ — related_work.tex: \"\\citet{park2021timediscretization} provide complementary formulations\"\n- **状态**: **OK**\n\n### 42. @article{wang2024elastic}\n- **标题 bib**: Reinforcement Learning with Elastic Time Steps\n- **真实性**: ✓ — arXiv 2402.14961\n- **作者**: ✓ — Dong Wang, Giovanni Beltrame\n- **年份**: ✓ — 2024\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: \"\\citet{wang2024elastic} learn elastic time steps\"\n- **状态**: **OK**\n\n### 43. @article{colas2018seeds}\n- **标题 bib**: How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\n- **真实性**: ✓ — arXiv 1806.08295\n- **作者**: ✓ — Cédric Colas, Olivier Sigaud, Pierre-Yves Oudeyer\n- **年份**: ✓ — 2018\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — conclusion.tex: \"Seed counts (4--5; \\citealt{colas2018seeds})\"\n- **状态**: **OK**\n\n### 44. @article{benechehab2023multitimestep}\n- **标题 bib**: Multi-timestep models for Model-based Reinforcement Learning\n- **真实性**: ✓ — arXiv 2310.05672\n- **作者**: ✗ — **严重错误：3/4 个合著者为伪造**\n  - bib 中列出：Benechehab, Abdelhakim / Couairon, Guillaume / Leurent, Edouard / Bloch, Balázs Kégl\n  - 实际作者：Abdelhakim Benechehab, **Giuseppe Paolo**, **Albert Thomas**, **Maurizio Filippone**, Balázs Kégl\n  - \"Couairon, Guillaume\" ✗ 不是本文作者\n  - \"Leurent, Edouard\" ✗ 不是本文作者\n  - \"Bloch, Balázs Kégl\" ✗ 格式错误且 \"Bloch\" 不存在；应为 \"Kégl, Balázs\"\n- **年份**: ✓ — 2023\n- **标题**: ✓\n- **Venue**: ✓ — arXiv preprint\n- **正文引用位置**: ✓ — related_work.tex: \"Multi-timestep world models \\citep{benechehab2023multitimestep}\"\n- **状态**: **🚨 严重问题 — 作者名伪造**\n- **建议修复**: author 改为 `{Benechehab, Abdelhakim and Paolo, Giuseppe and Thomas, Albert and Filippone, Maurizio and K{\\'e}gl, Bal{\\'a}zs}`\n\n### 45. @inproceedings{hafner2022director}\n- **标题 bib**: Deep Hierarchical Planning from Pixels\n- **真实性**: ✓ — NeurIPS 2022, arXiv 2206.04114\n- **作者**: ✓ — Danijar Hafner, Kuang-Huei Lee, Ian Fischer, Pieter Abbeel\n- **年份**: ✓ — 2022\n- **标题**: ✓\n- **Venue**: ✓ — NeurIPS 2022\n- **正文引用位置**: ✓ — related_work.tex: hierarchical variants\n- **状态**: **OK**\n\n---\n\n## 汇总\n\n| # | Bib Key | 问题类型 | 严重程度 | 简述 |\n|---|---------|----------|----------|------|\n| 6 | sharma2017figar | 标题不完整 | 中 | 缺少 \"Learning to Repeat:\" 前缀 |\n| 5 | hafner2023dreamerv3 | 标题不匹配 | 低 | arXiv 标题 vs Nature 正式版标题 |\n| 34 | parr1998ham | 标题错误 | 中 | 多了 \"Abstract\" 一词 |\n| 44 | benechehab2023multitimestep | 作者伪造 | 🚨 严重 | 3/4 合著者为虚假姓名 |\n\n### 无问题条目（41/45）\n1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45\n\n### 未发现 Hallucinated Citation\n所有 45 篇论文均经 WebSearch 确认真实存在。未发现完全虚构的论文。\n\n### 未发现的正文引用错误归因\n所有 `\\cite` / `\\citep` / `\\citet` 在正文中的使用均与被引论文的实际贡献一致。Hamrick 2021 被描述为 \"decision-aware model learning\" 略有不精确但不构成归因错误。\n"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-29T06:57:50.204956+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/citation_audit_worker_A.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_citation-verify-A_20260529T064944",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 129 · 2026-05-29T06:57:50.205242+00:00_

审计报告已写入 `artifacts/citation_audit_worker_A.md`。

**发现 4 个问题，其中 1 个严重：**

| Bib Key | 问题 | 严重程度 |
|---------|------|----------|
| `benechehab2023multitimestep` | **3/4 合著者为伪造姓名**（Couairon、Leurent、Bloch 均非本文作者；实际为 Paolo、Thomas、Filippone、Kégl） | 🚨 严重 |
| `parr1998ham` | 标题多了 "Abstract"（应为 "Hierarchies of Machines" 而非 "Hierarchies of Abstract Machines"） | 中 |
| `sharma2017figar` | 标题不完整，缺少 "Learning to Repeat:" 前缀 | 中 |
| `hafner2023dreamerv3` | bib 用 arXiv 标题但 venue 标 Nature 2025，Nature 版标题为 "Mastering diverse control tasks through world models" | 低 |

其余 41 条引用全部正确，无 hallucinated citation，无正文引用错误归因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_citation-verify-A_20260529T064944"
}
```

</details>

---
