# paper intro draft

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_paper_intro-draft_20260515T192303.jsonl`
- **Structured JSON:** [`c26ade121996aa361774.json`](../../sessions/c2/c26ade121996aa361774.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-15T19:26:16.302324+00:00_

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
  "session": "worker_paper_intro-draft_20260515T192303",
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

_source line 2 · 2026-05-15T19:26:16.303057+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:26:16.303364+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:26:16.303710+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight (Scenario C — ACTIVE, D029+D030 confirmed)\\nA lightweight observation-conditioned learned correction module (CRM), applied after conformal sample selection, can synthesize actions better than any individual VLA sample. The key contribution is the **sample-then-correct** pipeline itself and the discovery that **correction magnitude control is critical for closed-loop stability**. Per-DOF conformal features as CRM input offer no additional value over observation features — an honest negative result that challenges the intuition from synthetic experiments.\\n\\n## Active Framing: Scenario C\\n**Confirmed by data**: obs_only CRM > perdof CRM ≈ scalar CRM ≈ argmin on spatial (D029-D030); obs_only CRM **+7.0pp** over argmin on object 10/10 tasks FINAL (19.0% vs 12.0%); magnitude sweep shows obs_only robust to norm while perdof collapses at high norm (D032).\\n\\nStory: \\\"Observation-conditioned residual correction is the key contribution. The sample-then-correct pipeline (K=10 conformal selection + learned CRM correction) significantly outperforms pure sample selection on object manipulation tasks. Per-DOF conformal statistics as direct CRM input offer no advantage over observation features — but conformal prediction remains essential for the sample selection stage. Correction magnitude control is a critical and previously unrecognized factor for closed-loop VLA correction.\\\"\\n\\n## Core Claims (CoRL 单 Claim 论文)\\n\\n1. **Observation-conditioned learned correction (CRM) significantly improves VLA robustness beyond sample selection**\\n   - **主 claim**: obs_only CRM vs argmin-only ≥ 5pp on object bench
…[truncated 5875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:26:16.303963+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:26:16.304255+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 19:06 UTC | 更新原因: D033: Object 10-task FINAL confirmed +7pp. Paper Agent activated for CoRL draft.\\n\\n## 核心方向\\nobs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story：sample-then-correct > sample-then-select，obs features > conformal features（honest negative）。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 3 — Paper writing + seed=43 statistical validation\\n- **MVP**: PASS\\n- **Object 10/10 FINAL ✅**: obs_only 19.0% vs argmin 12.0% (+7.0pp) — **超过 5pp claim 门槛 (D033)**\\n- **Spatial LOCKED ✅**: 全部 CRM 变体确认 dead（argmin 34%, perdof 35%, obs_only 35%, scalar 32%）\\n- **Magnitude sweep**: obs_only stable 35-36% across norms, perdof collapses at high norm (D032)\\n- **Seed=43 六方部署中**: obs_only / argmin / perdof / scalar / VLA-mean / VLA-only, 预计 24-48h\\n- **Paper Agent**: 已激活，开始 CoRL 初稿 (Full Draft mode)\\n\\n## Object Benchmark（seed=42, ALL FINAL ✅）\\n\\n| 方法 | SR | vs argmin | 状态 |\\n|------|-----|-----------|------|\\n| **obs_only 0.1** | **19.0%** | **+7.0pp** | FINAL ✅ |\\n| argmin K=10 | 12.0% | baseline | FINAL ✅ |\\n| VLA-only K=1 | 12.0% | 0pp | FINAL ✅ |\\n| VLA-mean K=10 | 12.0% | 0pp | FINAL ✅ |\\n| perdof 0.1 | 11.0% | -1.0pp | FINAL ✅ |\\n| scalar 0.1 | 9.0% | -3.0pp | FINAL ✅ (negative) |\\n| obs_only 0.2 | 18.0% | +6.0pp | 5/10 running |\\n\\n## Spatial 最终结果（LOCKED ✅）\\n\\n| 方法 | 10-task SR | vs argmin |\\n|------|-----------|-----------|\\n| argmin K=10 | 34% | baseline |\\n| perdof 0.1 | 35% | +1pp |\\n| obs_only 0.1 | 35% | +1pp |\\n| scalar 0.1 | 32% | -2pp |\\n| VLA-only K=1 | 30% | -4pp |\\n| VLA-mean K=10 | 32% | -2pp |\\n\\n## Magnitude Sweep（spatial）\\n\\n| norm | obs_only | perdof | gap
…[truncated 2990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:26:16.304578+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/paper/outline.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/paper/outline.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:26:16.304803+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:26:16.304992+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/paper/method.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/paper/method.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:26:16.305167+00:00_

artifacts/_project/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:26:16.305391+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/paper/sections/related_work.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/paper/sections/related_work.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:26:16.305589+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:26:16.305895+00:00_

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
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:26:16.306218+00:00_

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
…[truncated 8716 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:26:16.306502+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/paper/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/paper/**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:26:16.306707+00:00_

artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/references.bib
artifacts/_project/paper/corl_paper_outline.md
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:26:16.306906+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/paper/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/paper/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T19:26:16.307110+00:00_

artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/references.bib
artifacts/_project/paper/corl_paper_outline.md
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T19:26:16.307355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T19:26:16.307720+00:00_

1	# ACR-VLA: CoRL 2026 Paper Outline
2	
3	## Title Candidates
4	
5	1. **ACR-VLA: Inference-Time Action Correction for Vision-Language-Action Models via Sample-Then-Correct**
6	2. **Sample-Then-Correct: Observation-Conditioned Residual Correction Improves VLA Robustness Beyond Sample Selection**
7	3. **Beyond Sample Selection: Learned Action Correction for Frozen Vision-Language-Action Models**
8	
9	Preferred: #2 — 直接点明贡献（sample-then-correct pipeline）+ 核心发现（obs-conditioned > conformal features）。
10	
11	---
12	
13	## Abstract Key Points
14	
15	- **Problem**: Flow-matching VLAs achieve near-saturated performance on standard benchmarks but remain fragile under distribution shift. Existing inference-time methods are limited to sample selection (ReconVLA) or require task-level RL training (SC-VLA).
16	- **Method**: ACR-VLA — a sample-then-correct pipeline: (1) draw K=10 samples from frozen VLA, (2) conformal prediction selects best candidate, (3) lightweight CRM (250K params) applies learned residual correction conditioned on observation features.
17	- **Key finding 1**: Sample-then-correct > sample-then-select. obs_only CRM achieves 19.0% on LIBERO-Object vs 12.0% argmin selection (+7.0pp).
18	- **Key finding 2 (negative result)**: Per-DOF conformal features as CRM input offer no advantage over observation features — perdof CRM 11.0% ≈ argmin 12.0%, while obs_only 19.0%.
19	- **Key finding 3**: Correction magnitude control is critical and previously unrecognized — norm=1.42 yields 0%, norm=0.1-0.2 yields +7pp, obs_only CRM is uniquely robust across the magnitude range.
20	- **Stats**: Fisher exact test p < 0.05 on combined seed=42+43 (200 trials). [pending seed=43 completion]
21	
22	---
23	
24	## 1. Introduction (~1.5 pages)
25	
26	### Motivation
27	- VLAs (π₀, OpenVLA, SmolVLA) represent a paradigm shift in robot learning, but distribution shift remains a major challenge.
28	- LIBERO benchmark exposes robustness gap: VLA performance degrades significantly under object/s
…[truncated 9500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T19:26:16.307976+00:00_

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
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T19:26:16.308236+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{VLA Robustness Methods.}
5	Recent work has sought to improve the robustness of vision-language-action models through training-time interventions.
6	SRPO~\cite{srpo2025} applies self-referential reinforcement learning to fine-tune VLA policies, achieving strong gains on the LIBERO-Plus benchmark.
7	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.
8	DiG-Flow~\cite{digflow2025} introduces discrepancy-guided flow matching, steering the generative process toward more accurate denoising trajectories during training.
9	SnapFlow~\cite{luan2026snapflow} distills multi-step flow-matching into single-step inference, reducing latency while preserving action quality.
10	TT-VLA~\cite{liu2026ttvla} adapts VLA parameters at test time via reinforcement learning, blurring the line between training-time and inference-time approaches.
11	VLA-GSE~\cite{vla_gse_2026} improves generalization through parameter-efficient fine-tuning with gated sparse experts, and Cosmos-Policy~\cite{cosmos_policy_2026} leverages video foundation models for visuomotor control.
12	These methods are complementary to ACR-VLA: they improve the base policy itself, whereas ACR-VLA operates as a post-hoc inference-time module that attaches to any frozen flow-matching VLA without modifying its weights.
13	This orthogonality means ACR-VLA can be composed with any of the above methods to provide additional robustness through uncertainty-conditioned correction.
14	
15	\paragraph{Uncertainty Quantification for Robot Learning.}
16	Quantifying predictive uncertainty in learned policies is essential for safe deployment.
17	Deep Ensembles~\cite{lakshminarayanan2017ensembles} and MC-Dropout~\cite{gal2016dropout} are foundational approaches that estimate epistemic uncertainty through multiple forward passes or stochastic weight perturbations, but both produce scalar or
…[truncated 4630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T19:26:16.308512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T19:26:16.308799+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	% Para 1: Problem — VLA success + robustness gap under distribution shift
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla} have reached 97--99\% success rates on standard manipulation benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: under distribution shifts common in real-world deployment---camera viewpoint changes, lighting variation, sensor noise, object layout differences---the same policies suffer substantial performance degradation~\cite{fei2025liberoplus}.
7	Closing this robustness gap is a prerequisite for deploying learned manipulation policies outside tightly controlled lab settings.
8	
9	% Para 2: Existing approaches — training-time vs inference-time, what they miss
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself: SRPO~\cite{srpo2025} applies self-referential policy optimization, while RobustVLA~\cite{robustvla2025} and DiG-Flow~\cite{digflow2025} incorporate robustness-aware objectives into training.
12	These methods are effective but require retraining or fine-tuning, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen and intervene at deployment.
14	ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy.
15	SAFE~\cite{gu2025safe} detects anomalous states and triggers fallback behaviors.
16	UPS~\cite{yuan2026ups} and CP-in-the-Loop~\cite{wang2025cploop} use conformal prediction for binary decisions---execute or abstain, safe or unsafe---but do not use conformal statistics as features for continuous correction.
17	A2C2~\cite{a2c2_2025} learns a residual correction that runs asynchronously alongside the base policy, yet applies it without uncertainty conditio
…[truncated 4480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T19:26:16.309109+00:00_

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
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T19:26:16.309471+00:00_

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
…[truncated 12225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T19:26:16.309867+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/ 2>/dev/null || echo \"NO_DIR\"",
  "description": "Check if sections directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/ 2>/dev/null || echo \"NO_DIR\"",
    "description": "Check if sections directory exists"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T19:26:16.310081+00:00_

NO_DIR

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T19:26:16.310294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections",
  "description": "Create sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections",
    "description": "Create sections directory"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T19:26:16.310492+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T19:26:16.310726+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached 97--99\\% success rates on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: distribution shifts routinely encountered in deployment---object substitution, spatial layout changes, lighting variation---can degrade success rates by 30--50 percentage points~\\cite{fei2025liberoplus}.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.\nThese approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the most conforming one, but sample selection is fundamentally limited: it cannot produce an action better than the best candidate in the sample set.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step---too slow for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction, but applies it unconditionally without first selecting a high-quality starting action.\nIn short, no existing inference-time method combines statistical sample selection with learned action correction on a frozen VLA.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce \\textbf{ACR-VLA} (\\textbf{A}daptive \\textbf{C}onformal \\textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \\emph{sample-then-correct} pipeline.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).\nCRM is a 329K-parameter MLP conditioned on the VLA's frozen observation embedding.\nIt predicts a small residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe critical design insight is that correction operates on a high-quality starting point---the conformal-selected action---and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Key findings (with exp_id references) ---\nWe evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:\n\n\\textbf{(1)~Sample-then-correct outperforms sample-then-select.}\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for conformal selection alone---a +7.0 percentage point improvement representing a 58\\% relative gain.\n% exp_id: eval-acr-object-v4-obs-only (19.0%), eval-argmin-only-object (12.0%)\n% TODO: update with pooled seed=42+43 results and Fisher exact p-value\nAveraging all $K$ samples (VLA-mean) or using a single sample (VLA-only) both yield 12.0\\%, confirming that the gain comes from learned correction, not from increased sampling alone.\n% exp_id: eval-vla-only-object-k1 (12.0%), eval-vla-mean-object (12.0%)\n\n\\textbf{(2)~Observation features suffice for correction; conformal features do not help.}\nCounter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\\%) performs no better than selection alone (12.0\\%), while scalar conformal conditioning (9.0\\%) is actively harmful.\n% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)\nOnly observation-conditioned CRM (19.0\\%) produces meaningful improvement.\nThis honest negative result highlights a gap between per-step prediction accuracy---where richer features help in offline evaluation---and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.\n\n\\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}\nWithout magnitude bounding, the CRM's natural output ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic failure: 0\\% success, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.\nConstraining corrections to $\\|\\boldsymbol{\\delta}\\|_2 \\leq 0.1$ recovers the full +7.0\\,pp gain.\n% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)\nObservation-conditioned CRM maintains stable 35--36\\% success on LIBERO-Spatial across $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% to 26\\% over the same range---further evidence that observation features provide more robust conditioning for learned correction.\n% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03\n\nWe note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, all CRM variants perform within ${\\pm}1$\\,pp of selection alone, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We propose ACR-VLA, the first system to combine conformal sample selection with learned residual correction for frozen flow-matching VLAs.\n  On LIBERO-Object, this pipeline improves SmolVLA success by +7.0\\,pp over selection alone.\n  % TODO: update with pooled seed results and p-value: (p < 0.05 on combined 200 trials, Fisher exact test)\n\n  \\item \\textbf{Systematic conditioning comparison and honest negative result.}\n  We compare three CRM conditioning variants---per-DOF conformal features, scalar uncertainty, and observation features---and find that only observation conditioning is effective.\n  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.\n\n  \\item \\textbf{First empirical study of correction magnitude sensitivity for VLA action refinement.}\n  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\\times}$ range of magnitude bounds ($\\varepsilon \\in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached 97--99\\% success rates on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: distribution shifts routinely encountered in deployment---object substitution, spatial layout changes, lighting variation---can degrade success rates by 30--50 percentage points~\\cite{fei2025liberoplus}.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.\nThese approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the most conforming one, but sample selection is fundamentally limited: it cannot produce an action better than the best candidate in the sample set.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step---too slow for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction, but applies it unconditionally without first selecting a high-quality starting action.\nIn short, no existing inference-time method combines statistical sample selection with learned action correction on a frozen VLA.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce \\textbf{ACR-VLA} (\\textbf{A}daptive \\textbf{C}onformal \\textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \\emph{sample-then-correct} pipeline.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).\nCRM is a 329K-parameter MLP conditioned on the VLA's frozen observation embedding.\nIt predicts a small residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe critical design insight is that correction operates on a high-quality starting point---the conformal-selected action---and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Key findings (with exp_id references) ---\nWe evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:\n\n\\textbf{(1)~Sample-then-correct outperforms sample-then-select.}\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for conformal selection alone---a +7.0 percentage point improvement representing a 58\\% relative gain.\n% exp_id: eval-acr-object-v4-obs-only (19.0%), eval-argmin-only-object (12.0%)\n% TODO: update with pooled seed=42+43 results and Fisher exact p-value\nAveraging all $K$ samples (VLA-mean) or using a single sample (VLA-only) both yield 12.0\\%, confirming that the gain comes from learned correction, not from increased sampling alone.\n% exp_id: eval-vla-only-object-k1 (12.0%), eval-vla-mean-object (12.0%)\n\n\\textbf{(2)~Observation features suffice for correction; conformal features do not help.}\nCounter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\\%) performs no better than selection alone (12.0\\%), while scalar conformal conditioning (9.0\\%) is actively harmful.\n% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)\nOnly observation-conditioned CRM (19.0\\%) produces meaningful improvement.\nThis honest negative result highlights a gap between per-step prediction accuracy---where richer features help in offline evaluation---and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.\n\n\\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}\nWithout magnitude bounding, the CRM's natural output ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic failure: 0\\% success, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.\nConstraining corrections to $\\|\\boldsymbol{\\delta}\\|_2 \\leq 0.1$ recovers the full +7.0\\,pp gain.\n% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)\nObservation-conditioned CRM maintains stable 35--36\\% success on LIBERO-Spatial across $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% to 26\\% over the same range---further evidence that observation features provide more robust conditioning for learned correction.\n% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03\n\nWe note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, all CRM variants perform within ${\\pm}1$\\,pp of selection alone, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We propose ACR-VLA, the first system to combine conformal sample selection with learned residual correction for frozen flow-matching VLAs.\n  On LIBERO-Object, this pipeline improves SmolVLA success by +7.0\\,pp over selection alone.\n  % TODO: update with pooled seed results and p-value: (p < 0.05 on combined 200 trials, Fisher exact test)\n\n  \\item \\textbf{Systematic conditioning comparison and honest negative result.}\n  We compare three CRM conditioning variants---per-DOF conformal features, scalar uncertainty, and observation features---and find that only observation conditioning is effective.\n  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.\n\n  \\item \\textbf{First empirical study of correction magnitude sensitivity for VLA action refinement.}\n  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\\times}$ range of magnitude bounds ($\\varepsilon \\in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T19:26:16.311084+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-draft_20260515T192303",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T19:26:16.311373+00:00_

Introduction 初稿已写到 `artifacts/_project/paper/sections/introduction.tex`。

结构：5 段落 + 贡献列表。
- Para 1: VLA 成就 + 分布偏移脆弱性
- Para 2: 现有方法（training-time vs inference-time）+ gap
- Para 3: ACR-VLA sample-then-correct pipeline 概述
- Para 4: 三个核心发现，每个附 exp_id 注释和具体数字
- Para 5: 三条贡献

关键处理：
- Spatial null result 诚实 framed（"targeted improvements on object-centric manipulation rather than universal gains"）
- 所有定量 claim 用 seed=42 confirmed 数据，标注 `% TODO: update with pooled seed results`
- 每个数字附 `% exp_id:` 注释可追溯
- 引用全部使用 references.bib 中已有的 key，无虚构引用
- 强度词匹配 evidence（只在 object benchmark 上说 "outperforms"，不用 "consistently"）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_intro-draft_20260515T192303"
}
```

</details>

---
