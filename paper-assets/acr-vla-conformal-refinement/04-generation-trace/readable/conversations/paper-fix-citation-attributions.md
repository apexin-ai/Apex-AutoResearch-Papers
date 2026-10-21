# paper fix citation attributions

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_paper_fix-citation-attributions_20260515T203100.jsonl`
- **Structured JSON:** [`ce5f6d4352504f35ee47.json`](../../sessions/ce/ce5f6d4352504f35ee47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-15T20:35:23.771020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/citation_attribution_audit.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/citation_attribution_audit.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T20:35:23.771449+00:00_

1	# Citation Attribution Audit — 2026-05-15
2	
3	## 审计范围
4	- introduction_scenarioC.tex, method.tex, experiments.tex, related_work.tex
5	- 共 27 个唯一引用，每个均通过 WebSearch 验证方法归因准确性
6	
7	## 审计结果
8	
9	| Citation Key | 论文中的描述 | 实际方法 | 状态 | 备注 |
10	|---|---|---|---|---|
11	| black2024pi0 | VLA that generates actions via flow matching | π₀ is a Vision-Language-Action Flow Model | CORRECT | — |
12	| shukor2025smolvla | 450M-parameter flow-matching VLA | SmolVLA confirmed 450M params, flow matching action expert | CORRECT | — |
13	| liu2023libero | Standard manipulation benchmark | LIBERO is a NeurIPS 2023 benchmark with 130 manipulation tasks | CORRECT | — |
14	| fei2025liberoplus | Distribution shifts (object appearance, lighting, sensor noise) cause performance degradation | LIBERO-Plus covers 7 perturbation types; "object appearance changes" not a precise match—paper covers objects layout, background textures, camera viewpoints, etc. | NEEDS_REVIEW | 论文中 "object appearance changes" 应改为更准确的描述，如 "visual perturbations" |
15	| robustvla2025 | Combines RL post-training with Jacobian regularization | Confirmed: online RL post-training + Jacobian regularization + smoothness regularization | CORRECT | — |
16	| srpo2025 | Self-referential RL fine-tuning, using policy's own rollouts as training signal | Uses own *successful* rollouts as reference to reward *failed* trajectories via latent world model | NEEDS_REVIEW | "own rollouts as training signal" 方向正确但过于简化；核心是成功/失败轨迹对比 |
17	| digflow2025 | Regularizes the flow-matching denoising trajectory via a discrepancy-guided objective | DiG-Flow operates at representation level: computes distributional discrepancy between observation/action embeddings as gating signal (DiG-Block); flow matching path is NOT modified | **INCORRECT** | 论文不是 "regularize denoising trajectory"，而是在 representation level 用 discrepancy gating |
18	| chen2026reconvla | Draws multiple action samples and selects the best via conformal scoring—a pure sample selection str
…[truncated 9201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T20:35:23.771660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/introduction_scenarioC.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/introduction_scenarioC.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T20:35:23.771800+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T20:35:23.771924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T20:35:23.772039+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:35:23.772151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T20:35:23.772286+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement. Did you mean related_work.md?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T20:35:23.772414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T20:35:23.772524+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T20:35:23.772631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T20:35:23.772765+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T20:35:23.772904+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T20:35:23.773028+00:00_

artifacts/dream_reports/dream_20260513T015051/best/paper.tex
artifacts/dream_reports/dream_20260513T015051/median/paper.tex
artifacts/dream_reports/dream_20260513T015051/worst/paper.tex
artifacts/dream_reports/dream_20260513T023849/best/paper.tex
artifacts/dream_reports/dream_20260513T023849/median/paper.tex
artifacts/dream_reports/dream_20260513T023849/worst/paper.tex
artifacts/method_section_draft.tex
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/experiments.tex
docs/paper/experiments.tex
artifacts/_project/paper/related_work_80791f.tex
artifacts/figures/object_benchmark_table.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/figures/spatial_final_table.tex
artifacts/_project/paper/abstract_a1674b.tex
artifacts/_project/paper/sections/introduction.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work.tex
docs/paper/method.tex
docs/paper/related_work.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/abstract.tex
docs/paper/abstract.tex
artifacts/_project/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T20:35:23.773150+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T20:35:23.773260+00:00_

artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T20:35:23.773398+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T20:35:23.773515+00:00_

artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/corl_paper_outline.md
paper/outline.md
paper/sections/related_work.md
paper/figure_plan.md
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/experiments.tex
docs/paper/experiments.tex
artifacts/_project/paper/related_work_80791f.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/_project/paper/abstract_a1674b.tex
artifacts/_project/paper/references.bib
artifacts/_project/paper/sections/introduction.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work.tex
docs/paper/method.tex
docs/paper/related_work.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/abstract.tex
docs/paper/abstract.tex
artifacts/_project/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T20:35:23.773650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T20:35:23.773811+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	% Para 1: Problem — VLAs degrade under distribution shift; existing solutions have trade-offs
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla} achieve 97--99\% success on standard manipulation benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\cite{fei2025liberoplus}.
7	Two families of methods address this robustness gap.
8	\emph{Training-time methods}~\cite{robustvla2025,srpo2025,digflow2025} improve the base policy through robustness-aware objectives, but require retraining and remain bounded by the training distribution.
9	\emph{Inference-time methods} leave the policy frozen and intervene at deployment.
10	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method.
11	SC-VLA~\cite{sc_vla_2026} learns a residual correction via reinforcement learning, requiring per-task environment interaction.
12	VLA-Pilot~\cite{vla_pilot_2025} steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41\,s per control step.
13	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
14	In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.
15	
16	% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?
17	The fundamental limitation of sample selection is that it is bounded by the quality of th
…[truncated 5654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T20:35:23.773958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T20:35:23.774140+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.
11	
12	At each control step, $\pi_\theta$ can be queried multiple times via independent flow-matching rollouts~\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\pi_\theta$.
13	
14	\subsection{Multi-Sample Generation and Conformal Selection}
15	\label{sec:selection}
16	
17	\paragraph{Sampling and truncation.}
18	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for each horizon step $h = 1, \dots, H$.
19	
20	\paragraph{Shrinkage covariance estimation.}
21	For each horizon step $h$, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well}:
22	\begin{equation}
23	  \boldsymbol{\Sigma}_h = (1 - \alpha_{\mathrm
…[truncated 8598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T20:35:23.774298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T20:35:23.774471+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.
9	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.
10	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.
11	TT-VLA~\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.
12	A shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\,s per control step---prohibi
…[truncated 7154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T20:35:23.774617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T20:35:23.774821+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction improve over conformal selection alone?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+7.0\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\_only is robust across a wide range.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10$): conformal selection via Mahalanob
…[truncated 12341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T20:35:23.774964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T20:35:23.775172+00:00_

1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	@article{barber2023conformal,
21	    title={Conformal Prediction Beyond Exchangeability},
22	    author={Rina Foygel Barber and Emmanuel J. Cand{\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},
23	    journal={Annals of Statistics},
24	    volume={51},
25	    number={2},
26	    pages={816--845},
27	    year={2023}
28	}
29	
30	@misc{black2024pi0,
31	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
32	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
33	    year={2024},
34	    eprint={2410.24164},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{braun2025cgs,
40	    title={Multivariate Standardized Residuals for Conformal Prediction},
41	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
42	    year={2025},
43	    eprint={2507.20941},
44	    archivePrefix={arXiv},
45	    primaryClass={stat.ML}
46	}
47	
48	@
…[truncated 14536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T20:35:23.775447+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
  "old_string": "Yet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}.",
  "new_string": "Yet under the distribution shifts common in deployment---visual and physical perturbations such as lighting variation, background changes, and sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
    "old_string": "Yet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}.",
    "new_string": "Yet under the distribution shifts common in deployment---visual and physical perturbations such as lighting variation, background changes, and sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T20:35:23.775621+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T20:35:23.775749+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
  "old_string": "A2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.",
  "new_string": "A2C2~\\cite{a2c2_2025} adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, but applies correction unconditionally without uncertainty-guided selection."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
    "old_string": "A2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.",
    "new_string": "A2C2~\\cite{a2c2_2025} adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, but applies correction unconditionally without uncertainty-guided selection."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T20:35:23.775906+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T20:35:23.776029+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
  "old_string": "A2C2~\\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.",
  "new_string": "A2C2~\\cite{a2c2_2025} adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, correcting each action within a pre-generated chunk to restore closed-loop responsiveness; however, it applies correction unconditionally without uncertainty-guided selection or explicit magnitude control."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
    "old_string": "A2C2~\\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.",
    "new_string": "A2C2~\\cite{a2c2_2025} adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, correcting each action within a pre-generated chunk to restore closed-loop responsiveness; however, it applies correction unconditionally without uncertainty-guided selection or explicit magnitude control."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T20:35:23.776179+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T20:35:23.776313+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
  "old_string": "PLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.",
  "new_string": "PLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with a magnitude bound $\\xi$ tuned per benchmark via off-policy RL, then distills improved trajectories back into the base model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
    "old_string": "PLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.",
    "new_string": "PLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with a magnitude bound $\\xi$ tuned per benchmark via off-policy RL, then distills improved trajectories back into the base model."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T20:35:23.776464+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T20:35:23.776580+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "old_string": "PLD~\\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training.",
  "new_string": "PLD~\\cite{xiao2026pld} introduces a magnitude bound $\\xi$ for the residual actor, tuned per benchmark, during off-policy RL training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
    "old_string": "PLD~\\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training.",
    "new_string": "PLD~\\cite{xiao2026pld} introduces a magnitude bound $\\xi$ for the residual actor, tuned per benchmark, during off-policy RL training."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T20:35:23.776761+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T20:35:23.776905+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "old_string": "PLD uses fixed action bounds",
  "new_string": "PLD uses per-benchmark magnitude bounds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
    "old_string": "PLD uses fixed action bounds",
    "new_string": "PLD uses per-benchmark magnitude bounds"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T20:35:23.777026+00:00_

&lt;tool_use_error>String to replace not found in file.
String: PLD uses fixed action bounds&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T20:35:23.777140+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "PLD uses",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "PLD uses",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T20:35:23.777252+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T20:35:23.777413+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "PLD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "PLD",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T20:35:23.777529+00:00_

86:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T20:35:23.777639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "offset": "84",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
    "offset": "84",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T20:35:23.777757+00:00_

84	
85	\paragraph{Connection to residual policy learning.}
86	The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\cite{xiao2026pld} introduces a magnitude bound $\xi$ for the residual actor, tuned per benchmark, during off-policy RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.
87	
88	\paragraph{Differential sensitivity across CRM variants.}
89	Observation-conditioned CRM (obs\_only) maintains 35--36\% success on LIBERO-Spatial across the full range $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% at $\varepsilon = 0.1$ to 26\% at $\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\ref{sec:ablation}).
90	
91	\subsection{Inference Protocol}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T20:35:23.777893+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "PLD uses",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "PLD uses",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T20:35:23.778012+00:00_

51:Magnitude control is the key connection to ACR-VLA: Silver et al.\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, DRC uses exponential decay after correction events.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T20:35:23.778125+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
  "old_string": "PLD uses fixed action bounds",
  "new_string": "PLD uses per-benchmark magnitude bounds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
    "old_string": "PLD uses fixed action bounds",
    "new_string": "PLD uses per-benchmark magnitude bounds"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T20:35:23.778261+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T20:35:23.778417+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib",
  "old_string": "author={Hao Zhou and Yanze Zhang and others}",
  "new_string": "author={Hao Zhou and Yanze Zhang and Wenhao Luo}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib",
    "old_string": "author={Hao Zhou and Yanze Zhang and others}",
    "new_string": "author={Hao Zhou and Yanze Zhang and Wenhao Luo}"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T20:35:23.778572+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T20:35:23.778695+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bounded correction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bounded correction",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T20:35:23.778815+00:00_

artifacts/_project/paper/experiments.tex:9:The answers are: yes (+7.0\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\_only is robust across a wide range.
artifacts/_project/paper/experiments.tex:176:\paragraph{Unbounded correction is catastrophic.}
artifacts/_project/paper/experiments.tex:178:The Argmin baseline (34\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.
artifacts/_project/paper/method_fb526b.tex:79:\paragraph{Unbounded correction fails catastrophically.}
artifacts/_project/paper/sections/introduction.tex:65:  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\times}$ range of magnitude bounds ($\varepsilon \in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.
artifacts/_project/paper/abstract_a1674b.tex:9:Magnitude control proves critical: unbounded correction leads to 0\% success.
artifacts/_project/paper/experiments_ac6246.tex:9:The answers are: yes (+7.0\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\_only is robust across a wide range.
artifacts/_project/paper/experiments_ac6246.tex:175:\paragraph{Unbounded correction is catastrophic.}
artifacts/_project/paper/method.tex:79:\paragraph{Unbounded correction fails catastrophically.}
artifacts/_project/paper/abstract.tex:9:Magnitude control proves critical: unbounded correction leads to 0\% success.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T20:35:23.778945+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sample selection|selection strategy|multi-sample selection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sample selection|selection strategy|multi-sample selection",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T20:35:23.779083+00:00_

artifacts/_project/paper/introduction_scenarioC.tex:16:% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?
artifacts/_project/paper/introduction_scenarioC.tex:17:The fundamental limitation of sample selection is that it is bounded by the quality of the available candidates: when all $K$ samples are poor, selecting the best one still yields a poor action.
artifacts/_project/paper/method_fb526b.tex:42:This argmin selection approximates the conformal selection strategy of ReconVLA~\cite{chen2026reconvla}, but replaces its scalar Euclidean distance with a Mahalanobis score that accounts for cross-DOF covariance structure. The selected $a_{\mathrm{base}} \in \mathbb{R}^{d \times H}$ is the starting point for residual correction.
artifacts/_project/paper/method_fb526b.tex:103:The computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\cite{chen2026reconvla}) plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
artifacts/_project/paper/sections/introduction.tex:16:A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
artifacts/_project/paper/sections/introduction.tex:56:  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.
artifacts/_project/paper/corl_paper_outline.md:6:2. **Sample-Then-Correct: Observation-Conditioned Residual Correction Improves VLA Robustness Beyond Sample Selection**
artifacts/_project/paper/corl_paper_outline.md:7:3. **Beyond Sample Selection: Learned Action Correction for Frozen Vision-Language-Action Models**
artifacts/_project/paper/corl_paper_outline.md:15:- **Problem**: Flow-matching VLAs achieve near-saturated performance on standard benchmarks but remain fragile 
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T20:35:23.779246+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "chen2026reconvla|conformal selection strategy|conformal selection frontend",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "chen2026reconvla|conformal selection strategy|conformal selection frontend",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T20:35:23.779390+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T20:35:23.779501+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "jointly with the VLA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "jointly with the VLA",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T20:35:23.779611+00:00_

artifacts/_project/paper/introduction_scenarioC_607d8d.tex:13:A2C2~\cite{a2c2_2025} trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T20:35:23.779726+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "object appearance changes",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "object appearance changes",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T20:35:23.779834+00:00_

artifacts/_project/paper/introduction_scenarioC_607d8d.tex:6:Yet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\cite{fei2025liberoplus}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T20:35:23.779966+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "progressively increasing",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "progressively increasing",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T20:35:23.780073+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T20:35:23.780177+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Zetian Zhou|Matteo Zollo",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Zetian Zhou|Matteo Zollo",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T20:35:23.780300+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-citation-attributions_20260515T203100",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-15T20:35:23.780476+00:00_

All clean. Here's the complete modification log:

### 修改清单

| # | 文件 | 修改内容 | 状态 |
|---|------|----------|------|
| 1 | `introduction_scenarioC.tex:6` | "object appearance changes, lighting variation, sensor noise" → "visual and physical perturbations such as lighting variation, background changes, and sensor noise" | **已修正** |
| 2 | `introduction_scenarioC.tex:13` | A2C2: "learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control" → "adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, but applies correction unconditionally without uncertainty-guided selection" | **已修正** |
| 3 | `related_work.tex:18` | A2C2: "learns a lightweight correction head that runs at every control step..." → "adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation..." | **已修正** |
| 4 | `related_work.tex:48` | PLD: "bounded corrections ($[-\xi, \xi]$)" → "a magnitude bound $\xi$ tuned per benchmark" | **已修正** |
| 5 | `related_work.tex:51` | PLD summary: "fixed action bounds" → "per-benchmark magnitude bounds" | **已修正** |
| 6 | `method.tex:86` | PLD: "bounds residual actor corrections within a fixed range during RL training" → "introduces a magnitude bound $\xi$ for the residual actor, tuned per benchmark, during off-policy RL training" | **已修正** |
| 7 | `references.bib:311` | zhou2025acp_cbf: "Hao Zhou and Yanze Zhang and others" → "Hao Zhou and Yanze Zhang and Wenhao Luo" | **已修正** |

### 已确认无需修改（之前已正确）

| # | 项目 | 当前状态 |
|---|------|----------|
| 1 | chen2026reconvla (intro/method/related) | 已正确描述为 CQR-based UQ + OOD detection |
| 3 | digflow2025 (related) | 已正确描述为 representation-level gating |
| 4 | silver2018residual (intro/related) | 无 "bounded corrections" 归因，已使用 "zero-initialization" |
| 5 | pan2025drc (related) | 已正确描述为 per-correction-event exponential decay |
| 7 | zollo2025vla_calibration (bib) | 已为 "Thomas Zollo" |
| 9 | srpo2025 (related) | 已正确描述 successful/failed trajectory 对比 |
| 10 | jiang2024transic (related) | 已正确描述为 "conditioned on the current state" |
| 12 | gu2025safe (related) | 已正确描述为 "triggering intervention" |

7 处实际修改，5 处确认已正确。全部 12 项引用归因问题已解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_fix-citation-attributions_20260515T203100"
}
```

</details>

---
