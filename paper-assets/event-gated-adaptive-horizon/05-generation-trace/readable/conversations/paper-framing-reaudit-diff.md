# paper framing reaudit diff

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_framing-reaudit-diff_20260515T224855.jsonl`
- **Structured JSON:** [`7b9eea02a9aafe7fa1d7.json`](../../sessions/7b/7b9eea02a9aafe7fa1d7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-15T22:51:27.085084+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T22:51:27.085442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T22:51:27.085653+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T22:51:27.086108+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure 
…[truncated 32079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T22:51:27.086343+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T22:51:27.086487+00:00_

docs/paper/sections/related_work.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/analysis.tex
docs/paper/sections/introduction.tex
docs/paper/sections/results.tex
docs/paper/sections/methodology.tex
docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T22:51:27.086644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T22:51:27.086780+00:00_

1	\begin{abstract}
2	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify trained temporal embedding as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. A normalized value-to-eval threshold of $1.5\times$ (35K+ training window) achieves 7/8 classification ($n{=}8$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, transient CIVO with self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T22:51:27.086954+00:00_

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
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T22:51:27.087108+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the \emph{trained} $\dt$-embedding as the causal factor. This embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A $\nve \geq 1.5\times$ threshold (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, single environment), with one non-CIVO false positive---a failure mode analogous to delusional bias \citep{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning.
7	
8	Three further findings complicate the picture: (1)~the same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations; (2)~restricting imagination to $\dt{=}1$ while retaining the trained embedding does not prevent collapse, with one of two seeds failing via a qualitatively distinct non-CIVO pathway (evaluation-driven, increasing entropy); and (3)~the contrast with TAWM identifies the feedback architecture---imagination-based bootstrapping versus MPC re-planning---as the structural fac
…[truncated 85 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T22:51:27.087260+00:00_

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
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T22:51:27.087398+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal Abstraction.}
5	The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
6	
7	\paragraph{TAWM and the MPC--Imagination Contrast.}
8	TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping---transforming manageable imprecision into pathological value overestimation.
9	
10	\paragraph{Value Overestimation.}
11	Value overestimation is well-studied in model-free \citep{fujimoto2018td3, vanhasselt2016double} and model-based settings \citep{janner2019mbpo, yu2020mopo}. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints; our CIVO is mechanistically distinct, arising from model imprecision amplified by learned temporal conditioning. \citet{tallec2019making} show Q-function degradation with temporal resolution mismatches, underpinning our finding at $\dt > 1$. \citet{f
…[truncated 299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T22:51:27.087537+00:00_

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
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T22:51:27.087701+00:00_

1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step, conditioning state predictions on the temporal scale. We test three modes:
16	\begin{itemize}[nosep,leftmargin=*]
17	\item \textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, allowing the RSSM to co-adapt its dynamics and reward predictions to the temporal scale.
18	\item \textbf{Untrained}: a fixed random projection of identical dimensionality. The RSSM receives a temporal signal but cannot co-adapt to it.
19	\item \textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.
20	\end{itemize}
21	The trained-vs-untrained contrast is the key causal control: it isolates the effect of \emph{learning} the temporal conditioning from its mere architectural presence.
22	
23	\paragraph{Temporal subsampling.}
24	When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames. Concretely, with a maximum subsampling factor of~2, the RSSM trains on both $\dt{=}1$ and $\dt{=}2$ transitions
…[truncated 6829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T22:51:27.087873+00:00_

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
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T22:51:27.088129+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{All configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & OFF & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\rowcolor{gray!15}
22	006 & Fixed $\dt{=}2$ & trained & OFF & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
23	007 & Fixed $\dt{=}4$ & trained & OFF & 15 & 152.5 @55K & --- & Collapsed \\
24	005 & Learned gate & trained & ON & 15 & 98.8 @145K & --- & Collapsed \\
25	\midrule
26	\rowcolor{gray!15}
27	008d & Factorial (s0) & trained & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
28	\rowcolor{gray!15}
29	009b & Factorial (s2) & trained & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
30	\rowcolor{gray!15}
31	009e & Factorial (s1) & trained & ON & 8 & 131.1 @105K & 4.12$\times$ & Oscillatory \\
32	008f & No dt\_emb (s
…[truncated 13942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T22:51:27.088290+00:00_

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
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T22:51:27.088457+00:00_

1	\section{Analysis \& Discussion}
2	\label{sec:analysis}
3	
4	The preceding results establish that trained $\dt$-embedding is the causal factor behind pathological value dynamics in variable-rate DreamerV3. In this section, we synthesize these findings into a mechanistic account of conditioning-induced value overestimation (CIVO), explain why the same CIVO trigger produces divergent outcomes across seeds, contrast the imagination-based setting with MPC-based temporal conditioning, and discuss the fundamental tension inherent in the $\dt$-embedding design.
5	
6	\subsection{The CIVO Mechanism}
7	\label{sec:civo_mechanism}
8	
9	The RSSM fidelity analysis (Table~\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\dt{=}1$ is $0.0568$, while at $\dt{=}2$ it rises to $0.1579$---a $2.78\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\times$ gap, and the baseline shows $1.56\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.
10	
11	This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\dt$-embedding causes RSSM predictions at $\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\nve$ above $1.5\times$, followed by evaluation collapse.
12	
13	A random-policy control experiment ($
…[truncated 6052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T22:51:27.088601+00:00_

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
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T22:51:27.088742+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3, identifying trained $\dt$-embedding as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:
5	
6	\begin{enumerate}[nosep,leftmargin=*]
7	\item Every variable-rate imagination configuration degrades relative to the $\dt{=}1$ baseline, with degradation scaling monotonically with $\dt$.
8	\item A normalized value-to-eval threshold of $\nve \geq 1.5\times$ (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, 87.5\%), with the single false positive arising from a mechanistically distinct non-CIVO collapse. Trained $\dt$-embedding is the causal factor; untrained or removed embeddings prevent overestimation.
9	\item The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning, providing the systematic bias that drives critic overestimation.
10	\item The same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations.
11	\item Restricting imagination to $\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy), demonstrating that the trained $\dt$-embedding creates vulnerability through multiple mechanisms.
12	\end{enumerate}
13	
14	The contrast with TAWM's success in MPC identifies the feedback architecture as the critical factor: $\dt$-conditioning succeeds when errors are contained by re-planning from real states, but fails when errors compound through imagination-based actor-critic bootstrapping.
15	
16	\paragraph{Limitations.}
17	Our experiments focus on a single environment (Walker Walk) and a single world-model architecture (DreamerV3/RSSM). While multi-seed replication establishes robustness within this setting, ge
…[truncated 1125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T22:51:27.088911+00:00_

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
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T22:51:27.089084+00:00_

1	% --- APPENDIX: NVE Threshold Sensitivity Analysis ---
2	
3	\appendix
4	\section{NVE Threshold Sensitivity Analysis}
5	\label{sec:appendix_sensitivity}
6	
7	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 1.5\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO---experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
8	
9	\subsection{Per-Experiment NVE Values}
10	
11	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.
12	
13	\begin{table}[h]
14	\centering
15	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\ = transient CIVO with self-correction.}
16	\label{tab:nve_raw}
17	\small
18	\begin{tabular}{@{}lrccc@{}}
19	\toprule
20	Experiment & NVE & Mechanism & B1 & B2 \\
21	\midrule
22	006          & 4.84 & sustained CIVO & $+$ & $+$ \\
23	008d         & 4.13 & sustained CIVO & $+$ & $+$ \\
24	008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
25	009b         & 1.62 & transient CIVO & $-$ & $+$ \\
26	001          & 1.00 & non-CIVO       & $-$ & $-$ \\
27	008f         & 0.97 & non-CIVO       & $-$ & $-$ \\
28	008e\_v3\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\
29	008a         & 0.93 & non-CIVO       & $-$ & $-$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\subsection{Multi-Threshold Classificati
…[truncated 4610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T22:51:27.089314+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Framing B Re-audit Diff Checklist",
  "type": "report",
  "description": "Per-section diff checklist for integrating 016e SGS informative negative into Framing B diagnostic paper",
  "project": "event-gated-adaptive-horizon",
  "content_filename": "framing_b_reaudit_diff.md",
  "content": "# Framing B Re-audit: 逐章节 Diff 清单\n\n**日期**: 2026-05-15\n**背景**: 016e SGS (reward_dt_emb_detach=True) 结果加入论文，定位为 informative negative — \"reward 梯度通路是贡献因素之一但非唯一根因，CIVO 是 representation-level 效应\"\n**016e 关键数据**: peak 326.7@75K → collapse 31.7@95K, NVE=10.42x; delays onset ~50K steps vs 008d, raises peak 2x (327 vs 167), but collapse more severe\n\n---\n\n## 1. abstract.tex — 小修\n\n**修改级别**: 小修（加 1 句）\n\n### 新增\n- 在 \"restricting imagination to $\\dt{=}1$ does not prevent collapse\" 句之后（或 \"multiple mechanisms\" 句之前），加入 SGS 结论：\n  > \"Selectively detaching reward-head gradients from the temporal embedding (SGS) delays CIVO onset by ~50K steps and doubles peak performance, but ultimately produces the most severe collapse observed (NVE 10.42×), confirming that the vulnerability operates at the representation level rather than solely through the reward gradient pathway.\"\n\n### 无需删除的旧 claim\n- 现有所有 claim 保持成立。SGS 结果**强化**而非矛盾现有叙事。\n\n---\n\n## 2. introduction.tex — 小修\n\n**修改级别**: 小修（加 1 条 finding）\n\n### 新增\n- 当前 \"Three further findings complicate the picture: (1)...(2)...(3)...\" 扩展为 **四条**，新增 (4)：\n  > \"(4) selectively detaching reward-head gradients from the temporal embedding delays CIVO onset by ${\\sim}50$K steps and doubles peak performance, yet collapse is ultimately more severe ($\\nve = 10.42\\times$ vs.\\ $4.12\\times$), establishing that the reward gradient pathway contributes to CIVO timing but the root vulnerability operates at the representation level.\"\n\n### 无需修改的旧 claim\n- \"every variable-rate configuration degrades\" — 016e 也崩溃，**强化**此 claim\n- TAWM contrast — 不受影响\n- Contribution framing — 不受影响\n\n---\n\n## 3. related_work.tex — 小修\n\n**修改级别**: 小修（加 1 段 ~5 句）\n\n### 新增\n- 在 \"Value Overestimation\" paragraph 之后（或之内），新增一段 **Gradient Intervention in MBRL**：\n  > \"\\paragraph{Gradient Intervention in Model-Based RL.}\n  > Several works address gradient conflicts in world-model training. PCGrad \\citep{yu2020pcgrad} projects conflicting task gradients to mitigate negative transfer in multi-task learning. HarmonyDream \\citep{hao2024harmonydream} balances observation and reward reconstruction gradients in Dreamer-style agents. VaGraM \\citep{voelcker2024vagram} uses value-gradient-weighted model learning to prioritize value-relevant dynamics. Our SGS experiment (selective gradient stopping on the reward head's $\\dt$-embedding path) tests whether the reward gradient pathway is the primary channel for CIVO; the negative result—SGS delays but does not prevent collapse—distinguishes CIVO from gradient-conflict phenomena and localizes the failure at the representation level.\"\n\n### 无需修改的旧内容\n- Temporal Abstraction paragraph — 不变\n- TAWM paragraph — 不变\n- 现有 Value Overestimation paragraph — 不变（SGS 新段是补充，不是替换）\n\n---\n\n## 4. methodology.tex — 小修\n\n**修改级别**: 小修（加 1 段方法描述 + 更新 factorial table）\n\n### 新增\n- §3.2 (Variable-Rate Imagination Mechanism) 末尾新增一段 **Selective Gradient Stopping (SGS)**：\n  > \"\\paragraph{Selective gradient stopping (SGS).}\n  > To test whether the reward gradient pathway is a primary driver of CIVO, we introduce a stop-gradient operation on the $\\dt$-embedding input specifically for the reward prediction head. Concretely, during the world model forward pass, the reward head receives $\\texttt{sg}(e(\\dt))$ (detached temporal embedding) while all other heads (observation, continuation, dynamics) receive the full $e(\\dt)$ with gradients intact. This isolates the reward head from co-adapting its predictions with the temporal signal, blocking one hypothesized channel for CIVO while preserving $\\dt$-conditioning for dynamics and observation predictions.\"\n\n- Table 1 (factorial_design) 新增一行：\n  > `016e & SGS (reward detach) & trn* & on & 8 & 2`\n  > 脚注加 `*reward head receives sg(e(dt))`\n\n- §3.3 (Factorial Design) 文字中加入第四个 diagnostic question：\n  > \"Fourth, exp\\_016e applies selective gradient stopping to the reward head's $\\dt$-embedding path, testing whether the reward gradient is the primary channel for CIVO or whether the vulnerability operates at the representation level independently of reward co-adaptation.\"\n\n### 无需修改的旧内容\n- Temporal embedding 三种 mode 描述 — 不变\n- Temporal subsampling 描述 — 不变\n- Diagnostic metrics — 不变\n- Environment and Training Details — 不变\n\n---\n\n## 5. results.tex — 重写局部（新增 F7 subsection + 更新 Table 1 + 更新 summary）\n\n**修改级别**: 中修（新增 ~0.5 页 subsection）\n\n### 新增\n\n#### Table 1 (main_results) 新增一行\n在 008e_v3 s2 行之后：\n> `016e & SGS (reward detach) & trained* & ON & 8 & 31.7 @95K & 10.42× & Delayed collapse`\n\n#### 新增 F7 subsection（在 F6 之后、RSSM fidelity analysis 之前）\n\n> \"\\subsection{F7: Selective Gradient Stopping Delays but Does Not Prevent Collapse}\n> \\label{sec:f7}\n>\n> Exp\\_016e applies selective gradient stopping (SGS) to the reward head's $\\dt$-embedding input (\\S\\ref{sec:methodology}), testing whether the reward gradient pathway is the primary driver of CIVO. If CIVO were predominantly a reward-gradient phenomenon, blocking this pathway should substantially mitigate or prevent collapse.\n>\n> SGS produces a striking partial effect (Figure~\\ref{fig:sgs_comparison}):\n> \\begin{itemize}[nosep,leftmargin=*]\n> \\item \\textbf{Delayed onset}: CIVO onset is delayed by ${\\sim}50$K steps (008d: $\\nve > 1.5\\times$ at 35K; 016e: not until ${\\sim}85$K).\n> \\item \\textbf{Higher peak}: Peak evaluation doubles (016e: 326.7 at 75K vs.\\ 008d: 167.1 at 35K).\n> \\item \\textbf{More severe collapse}: Once triggered, collapse is the most severe observed ($\\nve = 10.42\\times$ at 95K vs.\\ 008d: $4.12\\times$; evaluation: 31.7 vs.\\ 82.8).\n> \\end{itemize}\n>\n> \\begin{table}[t]\n> \\centering\n> \\caption{SGS (016e) vs.\\ full trained embedding (008d). SGS delays onset and raises peak but produces more severe collapse.}\n> \\label{tab:sgs_comparison}\n> \\footnotesize\n> \\begin{tabular}{lcccc}\n> \\toprule\n> & \\textbf{Onset} & \\textbf{Peak eval} & \\textbf{Final eval} & \\textbf{Peak NVE} \\\\\n> \\midrule\n> 008d (no SGS) & ${\\sim}$35K & 167.1 & 82.8 & 4.12$\\times$ \\\\\n> 016e (SGS) & ${\\sim}$85K & 326.7 & 31.7 & 10.42$\\times$ \\\\\n> \\bottomrule\n> \\end{tabular}\n> \\end{table}\n>\n> The delay confirms that the reward gradient pathway is a \\emph{contributing factor} to CIVO timing: blocking it slows the feedback loop's onset. However, the eventual collapse—more severe than the unmodified version—demonstrates that the root vulnerability operates at the representation level. The trained $\\dt$-embedding's learned features are embedded in the world model's latent dynamics through the observation and continuation heads (which retain full gradients under SGS), and these features alone are sufficient to drive CIVO once the critic accumulates enough exposure to biased $\\dt > 1$ trajectories. SGS does not block this channel—it merely removes the reward head's direct contribution to the co-adaptation, which delays but cannot prevent the representation-level bias from reaching the critic.\"\n\n#### Summary paragraph 更新\n现有 summary \"F1--F5 establish trained $\\dt$-embedding as the causal factor...F6 shows that restricting imagination...\" 改为：\n> \"F1--F5 establish trained $\\dt$-embedding as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$. F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes. F7 demonstrates that selectively detaching reward gradients delays CIVO onset by ${\\sim}50$K steps but produces even more severe eventual collapse ($\\nve = 10.42\\times$), localizing the root vulnerability at the representation level rather than the reward gradient pathway.\"\n\n### 需修改的旧 claim\n- **无旧 claim 需删除**。所有 F1-F6 findings 保持成立。016e 是**新增证据**，不矛盾任何现有发现。\n\n---\n\n## 6. analysis.tex — 中修（更新 §5.1 CIVO Mechanism + §5.5 Implications + 新增 §5.X SGS 段）\n\n**修改级别**: 中修\n\n### 新增\n\n#### 新增 subsection（建议放在 §5.4 Multiple Vulnerability Pathways 之后，§5.6 Implications 之前）\n\n> \"\\subsection{Gradient Pathway Analysis: SGS as Informative Negative}\n> \\label{sec:sgs_analysis}\n>\n> The SGS result (F7) decomposes the CIVO feedback loop into two contribution channels:\n>\n> \\textbf{Channel 1 (reward gradient pathway):} The reward head co-adapts with $e(\\dt)$, learning temporally differentiated but asymmetrically biased predictions. SGS blocks this channel. The ${\\sim}50$K onset delay under SGS quantifies this channel's contribution to CIVO timing.\n>\n> \\textbf{Channel 2 (representation-level pathway):} The dynamics and observation heads retain full $e(\\dt)$ gradients under SGS. Through world model training on $\\dt > 1$ transitions, the temporal embedding's learned features become entangled with the latent state representation. The critic, trained on imagined trajectories through these latent states, absorbs the bias indirectly—not through reward prediction error, but through the systematic distortion of the state space at $\\dt > 1$.\n>\n> SGS eliminates Channel 1 but leaves Channel 2 intact. The result—delayed but more severe collapse—has a natural interpretation: blocking the reward gradient pathway removes an \\emph{early warning} signal that would otherwise trigger collapse sooner (when the agent has accumulated less training and the representations are less entangled). By the time Channel 2 alone drives the critic past the tipping point, the representation-level bias is more deeply embedded, making the collapse harder to recover from.\n>\n> This result has direct implications for mitigation: interventions targeting the reward head alone (gradient stopping, reward smoothing \\citep{lee2024dreamsmooth}) are insufficient. Effective mitigation must address the representation-level entanglement—either through architectural separation of temporal scales (THICK, Hieros) or through regularization that prevents the temporal embedding from distorting the shared latent space.\"\n\n#### §5.1 (CIVO Mechanism) 更新\n- 在 four-stage feedback loop 描述末尾加入 SGS 佐证：\n  > \"The SGS experiment (exp\\_016e, \\S\\ref{sec:f7}) provides a partial decomposition: blocking stage (1) specifically for the reward head delays but does not prevent CIVO, confirming that the bias also propagates through the dynamics model's latent representations independently of direct reward co-adaptation.\"\n\n#### §5.6 (Implications) 更新\n- 现有文字 \"Regularization of the $\\dt$-embedding (e.g., gradient stopping or spectral normalization) could preserve the temporal signal while preventing co-adaptation\" **需修改为**：\n  > \"Our SGS experiment directly tested gradient stopping on the reward head's $\\dt$-embedding path; the result—delayed but more severe collapse—demonstrates that reward-pathway intervention alone is insufficient. Effective regularization must target the representation level, preventing $e(\\dt)$ from distorting the shared latent space used by dynamics and observation heads. Spectral normalization of $e(\\dt)$ or orthogonality constraints that decouple temporal features from task-relevant latent dimensions are potential directions, but our results suggest that architectural separation (as in THICK and Hieros) may be more robust than regularization-based approaches.\"\n\n### 需修改的旧 claim\n| 位置 | 旧文字 | 修改方式 |\n|------|--------|----------|\n| §5.6 最后一段 | \"Regularization of the $\\dt$-embedding (e.g., gradient stopping or spectral normalization) could preserve the temporal signal while preventing co-adaptation; we leave empirical evaluation to future work.\" | **替换** — gradient stopping 已实测否定，不再是纯 future work（见上方新文字） |\n\n---\n\n## 7. conclusion.tex — 小修\n\n**修改级别**: 小修（contribution list 加 1 条 + future directions 更新）\n\n### 新增\n- Contribution list (enumerate) 在第 5 条之后加第 6 条：\n  > \"\\item Selective gradient stopping on the reward head delays CIVO onset by ${\\sim}50$K steps but produces more severe eventual collapse ($\\nve = 10.42\\times$), establishing that the vulnerability operates primarily at the representation level rather than through the reward gradient pathway alone.\"\n\n### 需修改的旧 claim\n| 位置 | 旧文字 | 修改方式 |\n|------|--------|----------|\n| Future directions, 第 2 条 | \"regularization of the $\\dt$-embedding (e.g., gradient stopping or spectral normalization) could potentially preserve the temporal signal while preventing co-adaptation with the reward head\" | **修改为**: \"Our SGS experiment shows that gradient stopping on the reward head alone is insufficient; stronger interventions targeting the shared representation—such as spectral normalization of $e(\\dt)$ or orthogonality constraints—remain to be tested.\" |\n\n---\n\n## 8. appendix.tex — 小修\n\n**修改级别**: 小修（新增 016e 详细 metrics section）\n\n### 新增\n- 在现有 NVE Threshold Sensitivity Analysis 之后，新增：\n\n> \"\\section{SGS Experiment Details}\n> \\label{sec:appendix_sgs}\n>\n> Table~\\ref{tab:sgs_detailed} reports per-checkpoint metrics for exp\\_016e (SGS: reward\\_dt\\_emb\\_detach=True, subsample ON, H=8, seed 1).\n>\n> [表格: step, eval_return, value, v/e ratio, nve, actor_entropy, reward_MAE_dt1, reward_MAE_dt2]\"\n\n- Table 1 in appendix (nve_raw) 新增 016e 行：\n  > `016e & 10.42 & delayed CIVO & $+$ & $+$`\n\n- Table B1/B2 sensitivity tables 需重新计算（n 从 8 变为 9），或在 limitation 中注明 016e 未纳入 threshold analysis（因其配置不同于 factorial grid）。**建议**：保持 n=8 不变，在 limitation 中注明 016e 为独立验证实验，不纳入 threshold 统计。\n\n### 无需修改的旧内容\n- NVE threshold recommendation — 保持不变（016e 不改变 n=8 grid 的统计结论）\n\n---\n\n## 总览\n\n| 章节 | 修改级别 | 主要变更 |\n|------|----------|----------|\n| abstract | 小修 | +1 句 SGS 结论 |\n| introduction | 小修 | finding (3) → (4)，新增 SGS 发现 |\n| related_work | 小修 | +1 段 gradient intervention in MBRL (PCGrad, HarmonyDream, VaGraM) |\n| methodology | 小修 | +1 段 SGS 方法描述 + table 新增 016e 行 |\n| results | 中修 | +F7 subsection (~0.5 页) + table 更新 + summary 更新 |\n| analysis | 中修 | +1 subsection SGS 分析 (~0.4 页) + 更新 CIVO mechanism + **修改 implications 中 gradient stopping 为已验证** |\n| conclusion | 小修 | +1 条 contribution + 修改 future directions gradient stopping claim |\n| appendix | 小修 | +016e 详细 metrics table + nve_raw table 新增行 |\n\n## 需删除/修改的旧 Claim 汇总\n\n仅 **2 处旧 claim 需修改**（无需删除任何 claim）：\n\n1. **analysis.tex §5.6**: \"gradient stopping...could preserve the temporal signal while preventing co-adaptation; we leave empirical evaluation to future work\" → 已实测，需改为已验证的 negative result\n2. **conclusion.tex future directions**: 同上 — gradient stopping 不再是纯 future work\n\n所有其他现有 claim (C1-C6 / F1-F6) **完全保持成立**。016e SGS 是纯增量证据，强化而非矛盾现有叙事。\n",
  "tags": "['paper', 'framing-b', '016e', 'sgs', 'diff-checklist']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Framing B Re-audit Diff Checklist",
    "type": "report",
    "description": "Per-section diff checklist for integrating 016e SGS informative negative into Framing B diagnostic paper",
    "project": "event-gated-adaptive-horizon",
    "content_filename": "framing_b_reaudit_diff.md",
    "content": "# Framing B Re-audit: 逐章节 Diff 清单\n\n**日期**: 2026-05-15\n**背景**: 016e SGS (reward_dt_emb_detach=True) 结果加入论文，定位为 informative negative — \"reward 梯度通路是贡献因素之一但非唯一根因，CIVO 是 representation-level 效应\"\n**016e 关键数据**: peak 326.7@75K → collapse 31.7@95K, NVE=10.42x; delays onset ~50K steps vs 008d, raises peak 2x (327 vs 167), but collapse more severe\n\n---\n\n## 1. abstract.tex — 小修\n\n**修改级别**: 小修（加 1 句）\n\n### 新增\n- 在 \"restricting imagination to $\\dt{=}1$ does not prevent collapse\" 句之后（或 \"multiple mechanisms\" 句之前），加入 SGS 结论：\n  > \"Selectively detaching reward-head gradients from the temporal embedding (SGS) delays CIVO onset by ~50K steps and doubles peak performance, but ultimately produces the most severe collapse observed (NVE 10.42×), confirming that the vulnerability operates at the representation level rather than solely through the reward gradient pathway.\"\n\n### 无需删除的旧 claim\n- 现有所有 claim 保持成立。SGS 结果**强化**而非矛盾现有叙事。\n\n---\n\n## 2. introduction.tex — 小修\n\n**修改级别**: 小修（加 1 条 finding）\n\n### 新增\n- 当前 \"Three further findings complicate the picture: (1)...(2)...(3)...\" 扩展为 **四条**，新增 (4)：\n  > \"(4) selectively detaching reward-head gradients from the temporal embedding delays CIVO onset by ${\\sim}50$K steps and doubles peak performance, yet collapse is ultimately more severe ($\\nve = 10.42\\times$ vs.\\ $4.12\\times$), establishing that the reward gradient pathway contributes to CIVO timing but the root vulnerability operates at the representation level.\"\n\n### 无需修改的旧 claim\n- \"every variable-rate configuration degrades\" — 016e 也崩溃，**强化**此 claim\n- TAWM contrast — 不受影响\n- Contribution framing — 不受影响\n\n---\n\n## 3. related_work.tex — 小修\n\n**修改级别**: 小修（加 1 段 ~5 句）\n\n### 新增\n- 在 \"Value Overestimation\" paragraph 之后（或之内），新增一段 **Gradient Intervention in MBRL**：\n  > \"\\paragraph{Gradient Intervention in Model-Based RL.}\n  > Several works address gradient conflicts in world-model training. PCGrad \\citep{yu2020pcgrad} projects conflicting task gradients to mitigate negative transfer in multi-task learning. HarmonyDream \\citep{hao2024harmonydream} balances observation and reward reconstruction gradients in Dreamer-style agents. VaGraM \\citep{voelcker2024vagram} uses value-gradient-weighted model learning to prioritize value-relevant dynamics. Our SGS experiment (selective gradient stopping on the reward head's $\\dt$-embedding path) tests whether the reward gradient pathway is the primary channel for CIVO; the negative result—SGS delays but does not prevent collapse—distinguishes CIVO from gradient-conflict phenomena and localizes the failure at the representation level.\"\n\n### 无需修改的旧内容\n- Temporal Abstraction paragraph — 不变\n- TAWM paragraph — 不变\n- 现有 Value Overestimation paragraph — 不变（SGS 新段是补充，不是替换）\n\n---\n\n## 4. methodology.tex — 小修\n\n**修改级别**: 小修（加 1 段方法描述 + 更新 factorial table）\n\n### 新增\n- §3.2 (Variable-Rate Imagination Mechanism) 末尾新增一段 **Selective Gradient Stopping (SGS)**：\n  > \"\\paragraph{Selective gradient stopping (SGS).}\n  > To test whether the reward gradient pathway is a primary driver of CIVO, we introduce a stop-gradient operation on the $\\dt$-embedding input specifically for the reward prediction head. Concretely, during the world model forward pass, the reward head receives $\\texttt{sg}(e(\\dt))$ (detached temporal embedding) while all other heads (observation, continuation, dynamics) receive the full $e(\\dt)$ with gradients intact. This isolates the reward head from co-adapting its predictions with the temporal signal, blocking one hypothesized channel for CIVO while preserving $\\dt$-conditioning for dynamics and observation predictions.\"\n\n- Table 1 (factorial_design) 新增一行：\n  > `016e & SGS (reward detach) & trn* & on & 8 & 2`\n  > 脚注加 `*reward head receives sg(e(dt))`\n\n- §3.3 (Factorial Design) 文字中加入第四个 diagnostic question：\n  > \"Fourth, exp\\_016e applies selective gradient stopping to the reward head's $\\dt$-embedding path, testing whether the reward gradient is the primary channel for CIVO or whether the vulnerability operates at the representation level independently of reward co-adaptation.\"\n\n### 无需修改的旧内容\n- Temporal embedding 三种 mode 描述 — 不变\n- Temporal subsampling 描述 — 不变\n- Diagnostic metrics — 不变\n- Environment and Training Details — 不变\n\n---\n\n## 5. results.tex — 重写局部（新增 F7 subsection + 更新 Table 1 + 更新 summary）\n\n**修改级别**: 中修（新增 ~0.5 页 subsection）\n\n### 新增\n\n#### Table 1 (main_results) 新增一行\n在 008e_v3 s2 行之后：\n> `016e & SGS (reward detach) & trained* & ON & 8 & 31.7 @95K & 10.42× & Delayed collapse`\n\n#### 新增 F7 subsection（在 F6 之后、RSSM fidelity analysis 之前）\n\n> \"\\subsection{F7: Selective Gradient Stopping Delays but Does Not Prevent Collapse}\n> \\label{sec:f7}\n>\n> Exp\\_016e applies selective gradient stopping (SGS) to the reward head's $\\dt$-embedding input (\\S\\ref{sec:methodology}), testing whether the reward gradient pathway is the primary driver of CIVO. If CIVO were predominantly a reward-gradient phenomenon, blocking this pathway should substantially mitigate or prevent collapse.\n>\n> SGS produces a striking partial effect (Figure~\\ref{fig:sgs_comparison}):\n> \\begin{itemize}[nosep,leftmargin=*]\n> \\item \\textbf{Delayed onset}: CIVO onset is delayed by ${\\sim}50$K steps (008d: $\\nve > 1.5\\times$ at 35K; 016e: not until ${\\sim}85$K).\n> \\item \\textbf{Higher peak}: Peak evaluation doubles (016e: 326.7 at 75K vs.\\ 008d: 167.1 at 35K).\n> \\item \\textbf{More severe collapse}: Once triggered, collapse is the most severe observed ($\\nve = 10.42\\times$ at 95K vs.\\ 008d: $4.12\\times$; evaluation: 31.7 vs.\\ 82.8).\n> \\end{itemize}\n>\n> \\begin{table}[t]\n> \\centering\n> \\caption{SGS (016e) vs.\\ full trained embedding (008d). SGS delays onset and raises peak but produces more severe collapse.}\n> \\label{tab:sgs_comparison}\n> \\footnotesize\n> \\begin{tabular}{lcccc}\n> \\toprule\n> & \\textbf{Onset} & \\textbf{Peak eval} & \\textbf{Final eval} & \\textbf{Peak NVE} \\\\\n> \\midrule\n> 008d (no SGS) & ${\\sim}$35K & 167.1 & 82.8 & 4.12$\\times$ \\\\\n> 016e (SGS) & ${\\sim}$85K & 326.7 & 31.7 & 10.42$\\times$ \\\\\n> \\bottomrule\n> \\end{tabular}\n> \\end{table}\n>\n> The delay confirms that the reward gradient pathway is a \\emph{contributing factor} to CIVO timing: blocking it slows the feedback loop's onset. However, the eventual collapse—more severe than the unmodified version—demonstrates that the root vulnerability operates at the representation level. The trained $\\dt$-embedding's learned features are embedded in the world model's latent dynamics through the observation and continuation heads (which retain full gradients under SGS), and these features alone are sufficient to drive CIVO once the critic accumulates enough exposure to biased $\\dt > 1$ trajectories. SGS does not block this channel—it merely removes the reward head's direct contribution to the co-adaptation, which delays but cannot prevent the representation-level bias from reaching the critic.\"\n\n#### Summary paragraph 更新\n现有 summary \"F1--F5 establish trained $\\dt$-embedding as the causal factor...F6 shows that restricting imagination...\" 改为：\n> \"F1--F5 establish trained $\\dt$-embedding as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$. F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes. F7 demonstrates that selectively detaching reward gradients delays CIVO onset by ${\\sim}50$K steps but produces even more severe eventual collapse ($\\nve = 10.42\\times$), localizing the root vulnerability at the representation level rather than the reward gradient pathway.\"\n\n### 需修改的旧 claim\n- **无旧 claim 需删除**。所有 F1-F6 findings 保持成立。016e 是**新增证据**，不矛盾任何现有发现。\n\n---\n\n## 6. analysis.tex — 中修（更新 §5.1 CIVO Mechanism + §5.5 Implications + 新增 §5.X SGS 段）\n\n**修改级别**: 中修\n\n### 新增\n\n#### 新增 subsection（建议放在 §5.4 Multiple Vulnerability Pathways 之后，§5.6 Implications 之前）\n\n> \"\\subsection{Gradient Pathway Analysis: SGS as Informative Negative}\n> \\label{sec:sgs_analysis}\n>\n> The SGS result (F7) decomposes the CIVO feedback loop into two contribution channels:\n>\n> \\textbf{Channel 1 (reward gradient pathway):} The reward head co-adapts with $e(\\dt)$, learning temporally differentiated but asymmetrically biased predictions. SGS blocks this channel. The ${\\sim}50$K onset delay under SGS quantifies this channel's contribution to CIVO timing.\n>\n> \\textbf{Channel 2 (representation-level pathway):} The dynamics and observation heads retain full $e(\\dt)$ gradients under SGS. Through world model training on $\\dt > 1$ transitions, the temporal embedding's learned features become entangled with the latent state representation. The critic, trained on imagined trajectories through these latent states, absorbs the bias indirectly—not through reward prediction error, but through the systematic distortion of the state space at $\\dt > 1$.\n>\n> SGS eliminates Channel 1 but leaves Channel 2 intact. The result—delayed but more severe collapse—has a natural interpretation: blocking the reward gradient pathway removes an \\emph{early warning} signal that would otherwise trigger collapse sooner (when the agent has accumulated less training and the representations are less entangled). By the time Channel 2 alone drives the critic past the tipping point, the representation-level bias is more deeply embedded, making the collapse harder to recover from.\n>\n> This result has direct implications for mitigation: interventions targeting the reward head alone (gradient stopping, reward smoothing \\citep{lee2024dreamsmooth}) are insufficient. Effective mitigation must address the representation-level entanglement—either through architectural separation of temporal scales (THICK, Hieros) or through regularization that prevents the temporal embedding from distorting the shared latent space.\"\n\n#### §5.1 (CIVO Mechanism) 更新\n- 在 four-stage feedback loop 描述末尾加入 SGS 佐证：\n  > \"The SGS experiment (exp\\_016e, \\S\\ref{sec:f7}) provides a partial decomposition: blocking stage (1) specifically for the reward head delays but does not prevent CIVO, confirming that the bias also propagates through the dynamics model's latent representations independently of direct reward co-adaptation.\"\n\n#### §5.6 (Implications) 更新\n- 现有文字 \"Regularization of the $\\dt$-embedding (e.g., gradient stopping or spectral normalization) could preserve the temporal signal while preventing co-adaptation\" **需修改为**：\n  > \"Our SGS experiment directly tested gradient stopping on the reward head's $\\dt$-embedding path; the result—delayed but more severe collapse—demonstrates that reward-pathway intervention alone is insufficient. Effective regularization must target the representation level, preventing $e(\\dt)$ from distorting the shared latent space used by dynamics and observation heads. Spectral normalization of $e(\\dt)$ or orthogonality constraints that decouple temporal features from task-relevant latent dimensions are potential directions, but our results suggest that architectural separation (as in THICK and Hieros) may be more robust than regularization-based approaches.\"\n\n### 需修改的旧 claim\n| 位置 | 旧文字 | 修改方式 |\n|------|--------|----------|\n| §5.6 最后一段 | \"Regularization of the $\\dt$-embedding (e.g., gradient stopping or spectral normalization) could preserve the temporal signal while preventing co-adaptation; we leave empirical evaluation to future work.\" | **替换** — gradient stopping 已实测否定，不再是纯 future work（见上方新文字） |\n\n---\n\n## 7. conclusion.tex — 小修\n\n**修改级别**: 小修（contribution list 加 1 条 + future directions 更新）\n\n### 新增\n- Contribution list (enumerate) 在第 5 条之后加第 6 条：\n  > \"\\item Selective gradient stopping on the reward head delays CIVO onset by ${\\sim}50$K steps but produces more severe eventual collapse ($\\nve = 10.42\\times$), establishing that the vulnerability operates primarily at the representation level rather than through the reward gradient pathway alone.\"\n\n### 需修改的旧 claim\n| 位置 | 旧文字 | 修改方式 |\n|------|--------|----------|\n| Future directions, 第 2 条 | \"regularization of the $\\dt$-embedding (e.g., gradient stopping or spectral normalization) could potentially preserve the temporal signal while preventing co-adaptation with the reward head\" | **修改为**: \"Our SGS experiment shows that gradient stopping on the reward head alone is insufficient; stronger interventions targeting the shared representation—such as spectral normalization of $e(\\dt)$ or orthogonality constraints—remain to be tested.\" |\n\n---\n\n## 8. appendix.tex — 小修\n\n**修改级别**: 小修（新增 016e 详细 metrics section）\n\n### 新增\n- 在现有 NVE Threshold Sensitivity Analysis 之后，新增：\n\n> \"\\section{SGS Experiment Details}\n> \\label{sec:appendix_sgs}\n>\n> Table~\\ref{tab:sgs_detailed} reports per-checkpoint metrics for exp\\_016e (SGS: reward\\_dt\\_emb\\_detach=True, subsample ON, H=8, seed 1).\n>\n> [表格: step, eval_return, value, v/e ratio, nve, actor_entropy, reward_MAE_dt1, reward_MAE_dt2]\"\n\n- Table 1 in appendix (nve_raw) 新增 016e 行：\n  > `016e & 10.42 & delayed CIVO & $+$ & $+$`\n\n- Table B1/B2 sensitivity tables 需重新计算（n 从 8 变为 9），或在 limitation 中注明 016e 未纳入 threshold analysis（因其配置不同于 factorial grid）。**建议**：保持 n=8 不变，在 limitation 中注明 016e 为独立验证实验，不纳入 threshold 统计。\n\n### 无需修改的旧内容\n- NVE threshold recommendation — 保持不变（016e 不改变 n=8 grid 的统计结论）\n\n---\n\n## 总览\n\n| 章节 | 修改级别 | 主要变更 |\n|------|----------|----------|\n| abstract | 小修 | +1 句 SGS 结论 |\n| introduction | 小修 | finding (3) → (4)，新增 SGS 发现 |\n| related_work | 小修 | +1 段 gradient intervention in MBRL (PCGrad, HarmonyDream, VaGraM) |\n| methodology | 小修 | +1 段 SGS 方法描述 + table 新增 016e 行 |\n| results | 中修 | +F7 subsection (~0.5 页) + table 更新 + summary 更新 |\n| analysis | 中修 | +1 subsection SGS 分析 (~0.4 页) + 更新 CIVO mechanism + **修改 implications 中 gradient stopping 为已验证** |\n| conclusion | 小修 | +1 条 contribution + 修改 future directions gradient stopping claim |\n| appendix | 小修 | +016e 详细 metrics table + nve_raw table 新增行 |\n\n## 需删除/修改的旧 Claim 汇总\n\n仅 **2 处旧 claim 需修改**（无需删除任何 claim）：\n\n1. **analysis.tex §5.6**: \"gradient stopping...could preserve the temporal signal while preventing co-adaptation; we leave empirical evaluation to future work\" → 已实测，需改为已验证的 negative result\n2. **conclusion.tex future directions**: 同上 — gradient stopping 不再是纯 future work\n\n所有其他现有 claim (C1-C6 / F1-F6) **完全保持成立**。016e SGS 是纯增量证据，强化而非矛盾现有叙事。\n",
    "tags": "['paper', 'framing-b', '016e', 'sgs', 'diff-checklist']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T22:51:27.089631+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_8c32ec\", \"name\": \"Framing B Re-audit Diff Checklist\", \"type\": \"report\", \"description\": \"Per-section diff checklist for integrating 016e SGS informative negative into Framing B diagnostic paper\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/framing_b_reaudit_diff.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T22:51:19.616510+00:00\", \"tags\": [\"paper\", \"framing-b\", \"016e\", \"sgs\", \"diff-checklist\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T22:51:27.089811+00:00_

Diff 清单已生成并注册为 artifact `framing_b_reaudit_diff.md`。

核心结论：

**仅 2 处旧 claim 需修改**（均在 analysis.tex §5.6 和 conclusion.tex future directions — "gradient stopping...we leave to future work" → 已实测为 negative result）。所有 F1-F6 完全保持成立，016e 是纯增量证据。

**修改量分布**：
- **中修**：results.tex（+F7 subsection ~0.5 页）、analysis.tex（+SGS 分析段 ~0.4 页 + 更新 implications）
- **小修**：abstract（+1句）、introduction（+1条 finding）、related_work（+1段 gradient intervention lit）、methodology（+SGS 方法描述 + table 行）、conclusion（+1条 contribution + 修改 future directions）、appendix（+016e metrics table）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_framing-reaudit-diff_20260515T224855"
}
```

</details>

---
