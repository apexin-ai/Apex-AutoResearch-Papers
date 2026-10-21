# research reference audit r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 95
- **Recorded user turns:** 0
- **Tool calls:** 47
- **Original source:** `logs/chats/worker_research_reference-audit-r2_20260515T204542.jsonl`
- **Structured JSON:** [`743361c00ab819bf8da8.json`](../../sessions/74/743361c00ab819bf8da8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

95 recorded events

### Tool call

_source line 1 · 2026-05-15T20:53:17.829861+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,WebSearch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,WebSearch",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T20:53:17.830403+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T20:53:17.830726+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/intro.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper/intro.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T20:53:17.830961+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/intro.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T20:53:17.831169+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/method.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper/method.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T20:53:17.831404+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/method.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:53:17.831605+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/experiments.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper/experiments.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T20:53:17.831804+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T20:53:17.831999+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/related_work.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper/related_work.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T20:53:17.832196+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/related_work.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T20:53:17.832471+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T20:53:17.832750+00:00_

docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260513T015051/best/review_report.md
artifacts/dream_reports/dream_20260513T015051/median/review_report.md
artifacts/dream_reports/dream_20260513T023849/best/paper_framing.md
artifacts/libero-smolvla-env-report.md
artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md
artifacts/dream_reports/dream_20260513T023849/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T023849/best/review_report.md
artifacts/dream_reports/dream_20260513T023849/median/review_report.md
artifacts/dream_reports/dream_20260513T023849/worst/review_report.md
artifacts/pipeline-dimension-verification.md
.claude/sessions/paper_agent_f11cbd51/memory/MEMORY.md
artifacts/smolvla-libero-finetune-survey.md
artifacts/lerobot-pipeline-alignment.md
artifacts/_project/report/v4_deployment_report.md
task_context/history/reviewer/loop_1.md
task_context/history/director/loop_1.md
artifacts/eval-reconvla-spatial-v1-diag.md
artifacts/_project/report/claim-strength-analysis.md
artifacts/precompute-k5-analysis.md
artifacts/precompute-k5/report/precompute-k5-analysis.md
artifacts/reconvla-comparison-report.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_1.md
task_context/history/agent/loop_1_1778714300.md
task_context/history/agent/loop_1_1778723011.md
artifacts/_project/report/next_batch_plan.md
artifacts/diag-eval-v6-batch-failure.md
task_context/history/agent/loop_1_1778724391.md
task_context/history/agent/loop_1_1778724423.md
task_context/history/agent/loop_1_1778725595.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2.md
task_context/history/agent/loop_2_1778728390.md
task_context/history/agent/loop_2_1778728392.md
task_context/history/agent/loop_2_1778728430.md
task_context/history/agent/loop_2_1778728433.md
task_context/history/agent/loop_2_1778744616.md
artifacts/_project/report/object_eval_commands.md
artifacts/object_eval_commands.md
artifacts/_project/report/competitor_analysi
…[truncated 2805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T20:53:17.832992+00:00_

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
  "session": "worker_research_reference-audit-r2_20260515T204542",
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

_source line 14 · 2026-05-15T20:53:17.833201+00:00_

artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/corl_paper_outline.md
paper/outline.md
paper/sections/related_work.md
paper/figure_plan.md
artifacts/_project/paper/abstract_a1674b.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/references.bib
artifacts/_project/paper/related_work_80791f.tex
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/references.bib
docs/paper/discussion.tex
artifacts/_project/paper/experiments.tex
docs/paper/experiments.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/sections/discussion.tex
artifacts/_project/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T20:53:17.833485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T20:53:17.833782+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment---camera viewpoint shifts, object layout changes, robot initial state variation---can degrade success rates by over 65 percentage points---for example, $\pi_0$ drops from 94.2\% to 6.6\% under robot initial-state perturbation, and UniVLA from 95.2\% to 4.3\% under camera viewpoint changes~\cite{fei2025liberoplus}.
7	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.
8	
9	% --- Para 2: Existing approaches and the gap ---
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}.
12	These approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen.
14	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method.
15	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step---too slow for real-time manipulation.
16	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without mul
…[truncated 5926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T20:53:17.834076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T20:53:17.834387+00:00_

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
…[truncated 7150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T20:53:17.834638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T20:53:17.835033+00:00_

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
…[truncated 12262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T20:53:17.835305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T20:53:17.835550+00:00_

1	Flow-matching vision-language-action models (VLAs) achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift---dropping over 65 percentage points on LIBERO-Plus perturbations.
2	Existing inference-time remedies either select among multiple action samples, which cannot exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops.
3	%
4	We propose ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining.
5	At each control step, ACR-VLA draws $K{=}10$ action samples, selects one via Mahalanobis-based conformal scoring, and applies a bounded residual correction through a lightweight Conformal Residual Module (CRM, ${\sim}$329K parameters, ${\sim}$3\,ms overhead).
6	%
7	On LIBERO-Object, observation-conditioned CRM achieves 19.0\% success versus 12.0\% for selection alone (+7.0\,pp, 58\% relative gain).
8	Conditioning CRM on per-DOF conformal features (11.0\%) or scalar uncertainty (9.0\%) fails to improve over selection alone (12.0\%)---only observation features reach 19.0\%---an honest negative result we attribute to noisy covariance estimation at the $K{=}10$ sample budget.
9	Magnitude control proves critical: unbounded correction leads to 0\% success.
10	On LIBERO-Spatial, correction and selection perform comparably (${\pm}$1\,pp), indicating the benefit is task-dependent.
11	%
12	Sample-then-correct outperforms sample-then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T20:53:17.835699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T20:53:17.835907+00:00_

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
…[truncated 14540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T20:53:17.836289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T20:53:17.836606+00:00_

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
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T20:53:17.836859+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T20:53:17.837123+00:00_

1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Why per-DOF conformal features fail.}
6	The negative result on conformal conditioning (Section~\ref{sec:ablation}) warrants explanation.
7	% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%
8	At $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio $d/K = 0.6$ means that even with Ledoit--Wolf shrinkage~\cite{ledoit2004well}, per-DOF statistics---standard deviations, conformal radii---carry substantial estimation noise.
9	The frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ already encodes the geometric information these features attempt to capture: object identity, spatial layout, and gripper-object relationship.
10	Adding noisy low-dimensional statistics to a rich representation does not improve the CRM's predictions; it degrades them.
11	
12	A subtler issue is the gap between offline and closed-loop metrics.
13	All CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop success.
14	In closed-loop execution, compounding error~\cite{ross2011dagger} shifts the state distribution away from training data, and the noisy conformal features amplify this drift---occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.
15	This challenges the intuition from controlled synthetic settings that richer uncertainty features improve corrections, and raises an open question: would larger $K$ (e.g., $K{=}50$) yield reliable enough covariance estimates for per-DOF features to help?
16	We cannot test this due to the $K$-fold increase in VLA forward passes per control step.
17	
18	\paragraph{When does action-level correction help?}
19	% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%
20	% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%
21	The +7.0\,pp gain on LIBERO-Object 
…[truncated 3971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T20:53:17.838530+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReconVLA chen 2026 \"uncertainty-guided\" conformal quantile regression VLA robotic control arXiv 2604.16677"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReconVLA chen 2026 \"uncertainty-guided\" conformal quantile regression VLA robotic control arXiv 2604.16677"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T20:53:17.838836+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "A2C2 \"Leave No Observation Behind\" VLA action chunks correction 2025 arXiv 2509.23224"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "A2C2 \"Leave No Observation Behind\" VLA action chunks correction 2025 arXiv 2509.23224"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T20:53:17.839089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SRPO \"self-referential policy optimization\" VLA 2025 arXiv 2511.15605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SRPO \"self-referential policy optimization\" VLA 2025 arXiv 2511.15605"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T20:53:17.839299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RobustVLA \"robustness-aware reinforcement post-training\" VLA 2025 arXiv 2511.01331"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RobustVLA \"robustness-aware reinforcement post-training\" VLA 2025 arXiv 2511.01331"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T20:53:17.839525+00:00_

Web search results for query: "ReconVLA chen 2026 "uncertainty-guided" conformal quantile regression VLA robotic control arXiv 2604.16677"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Conformal Quantile Regression for Neural Probabilistic Constitutive Modeling","url":"https://arxiv.org/html/2601.17437"},{"title":"Conformal prediction for uncertainties in the neutron star equation of state","url":"https://arxiv.org/html/2604.21039"},{"title":"1 INTRODUCTION","url":"https://arxiv.org/html/2306.08693v2"},{"title":"QUTCC : Quantile Uncertainty Training and Conformal Calibration for Imaging Inverse Problems","url":"https://arxiv.org/html/2507.14760"},{"title":"[2507.14760] QUTCC: Quantile Uncertainty Training and Conformal Calibration for Imaging Inverse Problems","url":"https://arxiv.org/abs/2507.14760"},{"title":"[2306.08693] Integrating Uncertainty Awareness into Conformalized Quantile Regression","url":"https://arxiv.org/abs/2306.08693"},{"title":"Behind the Noise: Conformal Quantile Regression Reveals Emergent Representations","url":"https://arxiv.org/html/2505.08176v1"},{"title":"Conformalized Quantile Regression Yaniv Romano Department of Statistics","url":"https://papers.neurips.cc/paper/8613-conformalized-quantile-regression.pdf"},{"title":"Conformalized quantile regression | Proceedings of the 33rd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3454287.3454605"}]

Perfect! I found the paper. Here are the search results for your query:

The paper "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control" was authored by Lingling Chen, Zongyao Lyu, and William J. Beksi from The University of Texas at Arlington, with arXiv ID 2604.16677v1 posted on April 17, 2026.

The paper introduces ReconVLA, a reliable conformal model that prod
…[truncated 627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T20:53:17.839815+00:00_

Web search results for query: "A2C2 "Leave No Observation Behind" VLA action chunks correction 2025 arXiv 2509.23224"

Links: [{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"LEAVE NO OBSERVATION BEHIND: REAL-TIME COR- RECTION FOR VLA ACTION CHUNKS","url":"https://www.arxiv.org/pdf/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning","url":"https://arxiv.org/html/2509.25718"},{"title":"VGAS: Value-Guided Action-Chunk Selection for Few-Shot Vision-Language-Action Adaptation","url":"https://arxiv.org/html/2602.07399"},{"title":"VLA Knows Its Limits","url":"https://arxiv.org/html/2602.21445"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":": A Vision-Language-Action Model Bridging Understanding and Generation to Actions","url":"https://arxiv.org/html/2509.06951v2"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"}]

Based on the search results, I found detailed information about the paper you're looking for:

## "Leave No Observation Behind: Real-time Correction for VLA Action Chunks"

Asynchronous Action Chunk Correction (A2C2) is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk.

### Key Problem and Solution

To improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chu
…[truncated 1053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T20:53:17.840109+00:00_

Web search results for query: "SRPO "self-referential policy optimization" VLA 2025 arXiv 2511.15605"

Links: [{"title":"[2511.15605] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.15605"},{"title":"Paper page - SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://huggingface.co/papers/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.15605v1"},{"title":"[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"},{"title":"[Literature Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/srpo-self-referential-policy-optimization-for-vision-language-action-models"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/397780691_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models"},{"title":"SRPO Code Implementation Explained — siiRL documentation","url":"https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"},{"title":"[2406.01660] Self-Improving Robust Preference Optimization","url":"https://arxiv.org/abs/2406.01660"},{"title":"WMPO: World Model-based Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.09515v1"}]

I found comprehensive information about the SRPO paper. Here's what the search results reveal:

## SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

The paper was submitted on November 19, 2025,
…[truncated 1668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T20:53:17.840418+00:00_

Web search results for query: "RobustVLA "robustness-aware reinforcement post-training" VLA 2025 arXiv 2511.01331"

Links: [{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=9g7UXLqD4B"},{"title":"[Literature Review] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/robustvla-robustness-aware-reinforcement-post-training-for-vision-language-action-models"},{"title":"ROBUSTVLA: ROBUSTNESS-AWARE REINFORCE","url":"https://openreview.net/pdf/d2f9e3b68ce76261050b0db5ea64048b5e336142.pdf"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"}]

I found comprehensive information about RobustVLA. Here are the key findings:

## Overview

RobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models. Vision-Language-Action (VLA) models have recently emerged as powerful general-purpose policies for robotic manipulation, bu
…[truncated 1094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T20:53:17.840758+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DiG-Flow \"discrepancy-guided flow matching\" VLA 2025 arXiv 2512.01715 distributional discrepancy gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DiG-Flow \"discrepancy-guided flow matching\" VLA 2025 arXiv 2512.01715 distributional discrepancy gating"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T20:53:17.840979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TT-VLA \"test-time reinforcement learning\" VLA adaptation 2026 arXiv 2601.06748"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TT-VLA \"test-time reinforcement learning\" VLA adaptation 2026 arXiv 2601.06748"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T20:53:17.841174+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-Pilot \"evolutionary diffusion optimization\" MLLM verifier 2025 arXiv 2511.14178 inference time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-Pilot \"evolutionary diffusion optimization\" MLLM verifier 2025 arXiv 2511.14178 inference time"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T20:53:17.841472+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SC-VLA \"self-correcting VLA\" sparse world imagination residual RL 2026 arXiv 2602.21633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SC-VLA \"self-correcting VLA\" sparse world imagination residual RL 2026 arXiv 2602.21633"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T20:53:17.841721+00:00_

Web search results for query: "VLA-Pilot "evolutionary diffusion optimization" MLLM verifier 2025 arXiv 2511.14178 inference time"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"[2511.14178] Towards Deploying VLA without Fine-Tuning","url":"https://arxiv.org/abs/2511.14178"},{"title":"[2511.01718] Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process","url":"https://arxiv.org/abs/2511.01718"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process","url":"https://arxiv.org/html/2511.01718v1"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2511.21542] E0: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion","url":"https://arxiv.org/abs/2511.21542"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2509.06951"},{"title":"Beyond Autoregression: An Empirical Study of Diffusion Large Language Models for Code Generation","url":"https://arxiv.org/html/2509.11252v1"}]

I found the paper you're searching for! Here's what I found about VLA-Pilot and the relevant details:

VLA-Pilot is a training-free inference-time policy steering method that improves both the generalization and task alignment of pre-trained VLA policies for downstream deployment. 

Regarding the key components you asked about:

- **MLLM Verifier**: The method leverages Multimodal Large Language Model (MLLMs) as open-world verifiers to enhance generalizat
…[truncated 698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T20:53:17.841992+00:00_

Web search results for query: "TT-VLA "test-time reinforcement learning" VLA adaptation 2026 arXiv 2601.06748"

Links: [{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"[2601.06748] On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2601.06748"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.06748"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/399707107_On-the-Fly_VLA_Adaptation_via_Test-Time_Reinforcement_Learning"},{"title":"Test-Time RL for VLAs","url":"https://www.emergentmind.com/topics/test-time-reinforcement-learning-for-vlas-tt-vla"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084"},{"title":"TTRL: Test-Time Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=VuVhgEiu20"}]

Based on the search results, I found the paper you were looking for. Here's what the research is about:

## TT-VLA: On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning

TT-VLA is a framework that enables on-the-fly policy adaptation during inference. The paper addresses a key limitation in Vision-Language-Action models by enabling robots to adapt their behavior during deployment without requiring explicit fine-tuning phases.

**Key Details:**

- **ArXiv ID**: 2601.06748
- **Submission Date**: January 11, 2026 (la
…[truncated 959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T20:53:17.842289+00:00_

Web search results for query: "SC-VLA "self-correcting VLA" sparse world imagination residual RL 2026 arXiv 2602.21633"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633.pdf"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/pdf/2602.06508"},{"title":"Interesting Directions in Vision-Language-Action Model Research","url":"https://itcanthink.substack.com/p/interesting-directions-in-vision"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/html/2507.22424v1"}]

Based on the search results, here's what I found about SC-VLA (Self-Correcting VLA):

Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination. The method designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution. It also i
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T20:53:17.842619+00:00_

Web search results for query: "DiG-Flow "discrepancy-guided flow matching" VLA 2025 arXiv 2512.01715 distributional discrepancy gating"

Links: [{"title":"BeingBeyond ∝ DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"},{"title":"[2512.01715] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/abs/2512.01715"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/html/2512.01715v1"},{"title":"GitHub - BeingBeyond/DiG-Flow: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://github.com/BeingBeyond/DiG-Flow"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models - Takara TLDR | Takara TLDR","url":"https://tldr.takara.ai/p/2512.01715"},{"title":"[Quick Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://liner.com/review/digflow-discrepancyguided-flow-matching-for-robust-vla-models"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"Dream-VL & Dream-VLA: Open Vision-Language and ...","url":"https://arxiv.org/pdf/2512.22615"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"[2506.02070] An Introduction to Flow Matching and Diffusion Models","url":"https://arxiv.org/abs/2506.02070"}]

Based on the search results, I found the paper you're looking for. Here's information about DiG-Flow:

## DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models

DiG-Flow is a framework for Vision-Language-Action (VLA) models trained with flow matching for robotic manipulation tasks. The paper addresses the problem that VLA model performance often degrades under distribution shift and on complex multi-step tasks, suggesting that learned representations may not robustly capture
…[truncated 1335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T20:53:17.842927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReconVLA arXiv 2604.16677 action selection modification \"failure-aware\" mechanism what does it do with actions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReconVLA arXiv 2604.16677 action selection modification \"failure-aware\" mechanism what does it do with actions"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T20:53:17.843120+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TRANSIC \"sim-to-real policy transfer\" \"online correction\" binary gate 2024 arXiv 2405.10315"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TRANSIC \"sim-to-real policy transfer\" \"online correction\" binary gate 2024 arXiv 2405.10315"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T20:53:17.843314+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PLD \"self-improving VLA\" \"residual RL\" bounded corrections distillation 2026 arXiv 2511.00091"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PLD \"self-improving VLA\" \"residual RL\" bounded corrections distillation 2026 arXiv 2511.00091"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T20:53:17.843494+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DRC \"decaying relative correction\" policy refinement exponential decay 2025 arXiv 2503.15368"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DRC \"decaying relative correction\" policy refinement exponential decay 2025 arXiv 2503.15368"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T20:53:17.843695+00:00_

Web search results for query: "ReconVLA arXiv 2604.16677 action selection modification "failure-aware" mechanism what does it do with actions"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=263&show=2000"},{"title":"[2604.15771] Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing","url":"https://arxiv.org/abs/2604.15771"},{"title":"Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming","url":"https://arxiv.org/html/2604.05595v1"},{"title":"Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection","url":"https://arxiv.org/html/2604.13942v1"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=675&show=1000"},{"title":"Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions","url":"https://arxiv.org/html/2509.18847v2"},{"title":"1. Introduction","url":"https://arxiv.org/html/2604.16339"}]

Based on the search results, I found information about the ReconVLA paper (arXiv 2604.16677) and its failure-aware mechanism.

The failure-aware mechanism in ReconVLA uses an SMD-based detector that monitors latent state distributions to identify out-of-distribution (OOD) or failure-prone conditions. 

More specifically, this failure detection mechanism works by extending conformal prediction to the robot state space to detect outliers or unsafe states before failures occur. The framework incorporates conform
…[truncated 634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T20:53:17.843925+00:00_

Web search results for query: "PLD "self-improving VLA" "residual RL" bounded corrections distillation 2026 arXiv 2511.00091"

Links: [{"title":"PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)","url":"https://wenlixiao.com/self-improve-VLA-PLD"}]

Based on the search results, I found the paper you're looking for:

**PLD (Probe, Learn, Distill)** is a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection.

The framework works as follows:

- **Stage 1 (specialist acquisition)**: Freeze the VLA backbone and train lightweight residual actors via off-policy RL. These specialists take over in states where the base policy fails, thereby probing failure regions of the VLA generalist.

- **Stage 2 (data collection)**: Employ a hybrid rollout scheme that biases residual interventions toward states frequently visited by the base policy, aligning collected trajectories with the generalist's deployment distribution while capturing recovery behaviors.

- **Stage 3 (fine-tuning)**: Curated trajectories are distilled back into the generalist with standard SFT, applicable to both flow-matching and autoregressive heads.

The framework achieves a near-saturated 99% task success rate on the LIBERO benchmark, delivers over 50% performance gains in SimplerEnv, and demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.

This is the arXiv paper 2511.00091 (also accepted to ICLR 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T20:53:17.844213+00:00_

Web search results for query: "DRC "decaying relative correction" policy refinement exponential decay 2025 arXiv 2503.15368"

Links: [{"title":"[2503.15368] Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/abs/2503.15368"},{"title":"Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/html/2503.15368"}]

I found the paper! Here's what the search returned:

The Decaying Relative Correction (DRC) is a correction method based upon the spatial offset vector provided by the expert and exists temporarily, reducing the intervention steps required by an expert.

The DRC method is designed for correction of robotic manipulation and is made possible by a use of an 8 degree of freedom (DoF) teleoperation system and cable driven robot. The relative correction motion provided by the expert's teleoperation is a vector of correction which is only temporary, and stays valid for only a period of time, disappearing with a given decay rate.

The results demonstrate that DRC reduces the required expert intervention rate by 30% compared to a standard absolute corrective method. Integrating DRC within an online imitation learning framework rapidly increases the success rate of manipulation tasks such as raspberry harvesting and cloth wiping.

The paper was published on March 19, 2025, with the arXiv identifier 2503.15368.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T20:53:17.844479+00:00_

Web search results for query: "TRANSIC "sim-to-real policy transfer" "online correction" binary gate 2024 arXiv 2405.10315"

Links: [{"title":"[2405.10315] TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://arxiv.org/abs/2405.10315"},{"title":"Transic: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://arxiv.org/html/2405.10315v2"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://www.researchgate.net/publication/380635321_TRANSIC_Sim-to-Real_Policy_Transfer_by_Learning_from_Online_Correction"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction | alphaXiv","url":"https://www.alphaxiv.org/overview/2405.10315v3"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction (2024) | Yunfan Jiang | 10 Citations","url":"https://scispace.com/papers/transic-sim-to-real-policy-transfer-by-learning-from-online-2heee0h3xd"},{"title":"TRANSIC | Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://transic-robot.github.io/"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning ...","url":"https://arxiv-sanity-lite.com/?rank=pid&pid=2405.10315"},{"title":"GitHub - transic-robot/transic · GitHub","url":"https://github.com/transic-robot/transic"},{"title":"TRANSIC: Human-in-the-Loop Sim-to-Real Transfer","url":"https://www.emergentmind.com/papers/2405.10315"},{"title":"transic-robot/data · Datasets at Hugging Face","url":"https://huggingface.co/datasets/transic-robot/data"}]

I found comprehensive information about TRANSIC (arXiv 2405.10315). Here's a summary of what the research presents:

## Overview

TRANSIC is a data-driven approach to enable successful sim-to-real transfer based on a human-in-the-loop framework that allows humans to augment simulation policies to overcome various unmodeled sim-to-real gaps holistically through intervention and online correction.

## Key A
…[truncated 1097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T20:53:17.844825+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DiU \"divergence is uncertainty\" flow matching posterior covariance velocity field divergence 2026 arXiv 2605.00941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DiU \"divergence is uncertainty\" flow matching posterior covariance velocity field divergence 2026 arXiv 2605.00941"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T20:53:17.845040+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SAFE \"multitask failure detection\" VLA conformal prediction 2025 NeurIPS arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SAFE \"multitask failure detection\" VLA conformal prediction 2025 NeurIPS arXiv"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T20:53:17.845235+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zollo Zemel \"confidence calibration\" VLA \"prompt ensembles\" \"Platt scaling\" 2025 arXiv 2507.17383"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zollo Zemel \"confidence calibration\" VLA \"prompt ensembles\" \"Platt scaling\" 2025 arXiv 2507.17383"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-15T20:53:17.845464+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Braun Berta Jordan Bach \"conformalized gaussian scoring\" multivariate standardized residuals conformal prediction 2025 arXiv 2507.20941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Braun Berta Jordan Bach \"conformalized gaussian scoring\" multivariate standardized residuals conformal prediction 2025 arXiv 2507.20941"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T20:53:17.845726+00:00_

Web search results for query: "SAFE "multitask failure detection" VLA conformal prediction 2025 NeurIPS arXiv"

Links: [{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://vla-safe.github.io/"},{"title":"[2506.09937] SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09937"},{"title":"GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub","url":"https://github.com/vla-safe/SAFE"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09937v2"},{"title":"NeurIPS Poster SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://neurips.cc/virtual/2025/poster/117510"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=XPyAukgsFf"},{"title":"[PDF] SAFE: Multitask Failure Detection for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SAFE:-Multitask-Failure-Detection-for-Models-Gu-Ju/8165f26c174bd327506242ee898cf18a3abe61cf"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models | Toyota Research Institute","url":"https://www.tri.global/research/safe-multitask-failure-detection-vision-language-action-models"},{"title":"Paper page - SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.09937"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://neurips.cc/media/neurips-2025/Slides/117510.pdf"}]

Based on the search results, I found comprehensive information about SAFE:

## SAFE: Multitask Failure Detection for Vision-Language-Action Models

SAFE is a failure detector for generalist robot policies such as VLAs, and it was published as a NeurIPS 2025 post
…[truncated 1411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T20:53:17.846012+00:00_

Web search results for query: "DiU "divergence is uncertainty" flow matching posterior covariance velocity field divergence 2026 arXiv 2605.00941"

Links: [{"title":"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching","url":"https://arxiv.org/html/2605.00941"},{"title":"[2605.00941] Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching","url":"https://arxiv.org/abs/2605.00941"},{"title":"Discrete Flow Matching: Convergence Guarantees Under Minimal Assumptions","url":"https://arxiv.org/html/2605.08882"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"[2511.05480] On Flow Matching KL Divergence","url":"https://arxiv.org/abs/2511.05480"},{"title":"[2605.08882] Discrete Flow Matching: Convergence Guarantees Under Minimal Assumptions","url":"https://arxiv.org/abs/2605.08882"},{"title":"Training-Free Refinement of Flow Matching with Divergence-based Sampling","url":"https://arxiv.org/html/2604.04646v1"},{"title":"How and Why: Taming Flow Matching for Unsupervised Anomaly Detection and Localization","url":"https://arxiv.org/html/2508.05461v1"},{"title":"[2604.04646v1] Training-Free Refinement of Flow Matching with Divergence-based Sampling","url":"https://arxiv.org/abs/2604.04646v1"},{"title":"Last Update: Novermber 7, 2025 On Flow Matching KL Divergence Maojiang Su†∗1","url":"https://arxiv.org/pdf/2511.05480"}]

I found the paper you're looking for! Here's information about arXiv 2605.00941:

## "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching"

The paper was submitted on May 1, 2026 by Jiarui Xing and 2 other authors.

**Main Contribution:**

The paper proves that for any pre-trained flow matching velocity field, the trace of the posterior covariance over the clean data given the current state equals, in closed form, the divergence of the velocity field, up to a known time-dependent prefact
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T20:53:17.846310+00:00_

Web search results for query: "Zollo Zemel "confidence calibration" VLA "prompt ensembles" "Platt scaling" 2025 arXiv 2507.17383"

Links: [{"title":"[2507.17383] Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/abs/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models Thomas Zollo","url":"https://arxiv.org/pdf/2507.17383"},{"title":"(PDF) Confidence Calibration in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/393966020_Confidence_Calibration_in_Vision-Language-Action_Models"},{"title":"Confidence Calibration in Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=aiPC7jAd2f"},{"title":"[2410.05407v1] Improving Predictor Reliability with Selective Recalibration","url":"https://arxiv.org/abs/2410.05407v1"},{"title":"[2604.19444] Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation","url":"https://arxiv.org/abs/2604.19444"},{"title":"[2507.05220] QuEst: Enhancing Estimates of Quantile-Based Distributional Measures Using Model Predictions","url":"https://arxiv.org/abs/2507.05220"},{"title":"[1706.04599] On Calibration of Modern Neural Networks","url":"https://arxiv.org/abs/1706.04599"},{"title":"Calibration Meets Reality: Making Machine Learning Predictions Trustworthy","url":"https://arxiv.org/html/2509.23665v1"}]

I found the paper you're looking for! Here are the key findings:

## Paper Summary

The paper presents a first-of-its-kind study of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands.

## Main Contributions

The researchers establish a confidence baseline for VLAs, examine how task success relates to calibration error and how calibration evolves over time, and introduce two lightweight 
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T20:53:17.846724+00:00_

Web search results for query: "Braun Berta Jordan Bach "conformalized gaussian scoring" multivariate standardized residuals conformal prediction 2025 arXiv 2507.20941"

Links: [{"title":"[2507.20941] Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/abs/2507.20941"},{"title":"(PDF) Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://www.researchgate.net/publication/394081259_Multivariate_Conformal_Prediction_via_Conformalized_Gaussian_Scoring"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/pdf/2507.20941"},{"title":"[PDF] Multivariate Conformal Prediction via Conformalized Gaussian Scoring | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multivariate-Conformal-Prediction-via-Conformalized-Braun-Berta/eb97eda6c4159d62c1fd5d2ca6404b323e44123c"},{"title":"Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/html/2507.20941"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian ...","url":"https://ribbitribbit.co/paper/arxiv.2507.20941-Multivariate-Conformal-Prediction-via-Conformalized-Gaussian-Scoring"},{"title":"Publications - People @EECS","url":"https://people.eecs.berkeley.edu/~jordan/publications.html"},{"title":"Methodology Jul 2025","url":"https://www.arxiv.org/list/stat.ME/2025-07?skip=350&show=1000"},{"title":"Statistics","url":"https://www.arxiv.org/list/stat/recent?skip=111&show=25"},{"title":"Eugene Berta","url":"https://eugeneberta.github.io/"}]

I found the paper you're looking for! Here are the search results for arXiv paper 2507.20941:

## Paper Information

The paper is titled "Multivariate Standardized Residuals for Conformal Prediction" by Sacha Braun, Eugène Berta, Michael I. Jordan, and Francis Bach.

## Main Contribution

The paper proposes a natural extension of normalization to the multivariate setting, effectively whitening the residuals to decouple 
…[truncated 1273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T20:53:17.847053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus \"pi0\" \"94.2\" \"6.6\" OR \"UniVLA\" \"95.2\" \"4.3\" robustness perturbation arXiv 2510.13626"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus \"pi0\" \"94.2\" \"6.6\" OR \"UniVLA\" \"95.2\" \"4.3\" robustness perturbation arXiv 2510.13626"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-15T20:53:17.847260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"conformalized teleoperation\" Zhao Simmons Admoni Bajcsy RSS 2024 high-DOF action mappings shared autonomy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"conformalized teleoperation\" Zhao Simmons Admoni Bajcsy RSS 2024 high-DOF action mappings shared autonomy"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T20:53:17.847523+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CP-in-the-Loop\" Wang Ning conformal prediction trajectory optimization 2025 arXiv 2510.16376"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CP-in-the-Loop\" Wang Ning conformal prediction trajectory optimization 2025 arXiv 2510.16376"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-15T20:53:17.847725+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Silver Allen Tenenbaum Kaelbling \"residual policy learning\" zero-initialization 2018 RSS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Silver Allen Tenenbaum Kaelbling \"residual policy learning\" zero-initialization 2018 RSS"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-15T20:53:17.847966+00:00_

Web search results for query: ""conformalized teleoperation" Zhao Simmons Admoni Bajcsy RSS 2024 high-DOF action mappings shared autonomy"

Links: [{"title":"[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/abs/2406.07767"},{"title":"[2406.07767v1] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"http://arxiv.org/abs/2406.07767v1"},{"title":"dblp: Robotics: Science and Systems 2024","url":"https://dblp.org/db/conf/rss/rss2024.html"},{"title":"Conformalized Teleoperation: Confidently Mapping Human ...","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/html/2406.07767v2"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/program/papers/8/"},{"title":"[2410.08852] Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback","url":"https://arxiv.org/abs/2410.08852"},{"title":"Publications | Henny Admoni","url":"https://www.hennyadmoni.com/publications/"},{"title":"Michelle Zhao","url":"https://michellezhao.net/"},{"title":"Reid SIMMONS | Carnegie Mellon University, Pittsburgh | CMU | Robotics Institute | Research profile","url":"https://www.researchgate.net/profile/Reid-Simmons"}]

Great! I found the research paper you were looking for. Here are the search results:

## Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions

The paper "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions" was authored by Michelle D. Zhao, Reid G. Simmons, Henny Admoni, and Andrea Bajcsy, and it was presented at RSS 2024 (Robotics: Science and Systems) in Delft, Net
…[truncated 1343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T20:53:17.848238+00:00_

Web search results for query: "Silver Allen Tenenbaum Kaelbling "residual policy learning" zero-initialization 2018 RSS"

Links: [{"title":"[PDF] Residual Policy Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Residual-Policy-Learning-Silver-Allen/8c21a1d8844e6b58fd74b2b94c512a23497029c1"},{"title":"[1812.06298] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298"},{"title":"Residual Policy Learning","url":"https://www.researchgate.net/publication/329734796_Residual_Policy_Learning"},{"title":"Residual Policy Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181206298S/abstract"},{"title":"[1812.06298v2] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298v2"},{"title":"Residual Policy Learning","url":"https://vitalab.github.io/article/2019/06/27/RPL.html"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Residual+policy+learning&amp=&author=T+Silver&amp=&author=K+Allen&amp=&author=J+Tenenbaum&amp=&author=L+Kaelbling&amp=&publication_year=2018&amp=&journal=arXiv+preprint+arXiv:1812.06298"},{"title":"Residual Policy Learning","url":"https://arxiv.org/pdf/1812.06298v2"},{"title":"[1812.06298] Residual Policy Learning - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1812.06298"},{"title":"Accelerating Residual Reinforcement Learning with Uncertainty Estimation | Request PDF","url":"https://www.researchgate.net/publication/392942022_Accelerating_Residual_Reinforcement_Learning_with_Uncertainty_Estimation"}]

I found the paper! Here are the search results for the "Residual Policy Learning" paper:

**Paper Details:**
- Authors: Tom Silver, Kelsey Allen, Josh Tenenbaum, and Leslie Kaelbling from MIT
- Published on arXiv as paper 1812.06298 (released January 3, 2019, but dated 2018)

**Summary:**
The paper presents Residual Policy Learning (RPL): a simple method for improving nondifferentiable policies using model-free deep reinforcement learning that thrives in com
…[truncated 760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T20:53:17.848551+00:00_

Web search results for query: "LIBERO-Plus "pi0" "94.2" "6.6" OR "UniVLA" "95.2" "4.3" robustness perturbation arXiv 2510.13626"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"}]

I found the research paper you were looking for. Here are the key details:

## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

Visual-Language-Action (VLA) models report impressive success rates on robotic manipulation benchmarks, yet a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions—objects layout, camera viewpoints, robot initial states, la
…[truncated 1165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T20:53:17.848854+00:00_

Web search results for query: ""CP-in-the-Loop" Wang Ning conformal prediction trajectory optimization 2025 arXiv 2510.16376"

Links: [{"title":"[2510.16376] Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://arxiv.org/abs/2510.16376"},{"title":"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://arxiv.org/html/2510.16376v1"},{"title":"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=lg51XnHt2H"},{"title":"End-to-End Conformal Prediction for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=ilcsm8B7Pe"},{"title":"NeurIPS Poster Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116267"},{"title":"Adaptive Conformal Prediction Intervals Over Trajectory Ensembles","url":"https://arxiv.org/html/2508.13362v1"},{"title":"Conformal Prediction in The Loop: A Feedback-Based ...","url":"https://www.researchgate.net/publication/396714858_Conformal_Prediction_in_The_Loop_A_Feedback-Based_Uncertainty_Model_for_Trajectory_Optimization"},{"title":"Who Moved My Distribution? Conformal Prediction for Interactive Multi-Agent Systems","url":"https://arxiv.org/html/2511.11567"},{"title":"Adaptive Conformal Prediction Intervals Over Trajectory Ensembles","url":"https://www.arxiv.org/pdf/2508.13362"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"}]

I found the paper! Here's what I found about the research:

## "Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization"

**Paper Details:**
- arXiv: 2510.16376
- Authors: Han Wang and Chao Ning
- Submitted: October 18, 2025

**Overview:**
The paper addresses how Conformal Prediction (CP) 
…[truncated 1178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T20:53:17.849236+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus arXiv 2510.13626 pi0 UniVLA success rate robot initial state camera viewpoint specific numbers table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus arXiv 2510.13626 pi0 UniVLA success rate robot initial state camera viewpoint specific numbers table"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-15T20:53:17.849478+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SC-VLA arXiv 2602.21633 method details \"residual RL\" OR \"reinforcement learning\" action refinement training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SC-VLA arXiv 2602.21633 method details \"residual RL\" OR \"reinforcement learning\" action refinement training"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T20:53:17.849765+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou Zhang Luo \"adaptive conformal prediction\" \"control barrier functions\" safe reinforcement learning ICRA 2025 arXiv 2503.17678"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou Zhang Luo \"adaptive conformal prediction\" \"control barrier functions\" safe reinforcement learning ICRA 2025 arXiv 2503.17678"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T20:53:17.850059+00:00_

Web search results for query: "SC-VLA arXiv 2602.21633 method details "residual RL" OR "reinforcement learning" action refinement training"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models","url":"https://arxiv.org/html/2602.12628v1"},{"title":"From Imitation to Refinement – Residual RL for Precise Assembly","url":"https://arxiv.org/html/2407.16677v4"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"RLinf-VLA: A unified and efficient framework for VLA+RL training","url":"https://arxiv.org/html/2510.06710v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"From Imitation to Refinement – Residual RL for Precise Visual Assembly","url":"https://arxiv.org/html/2407.16677v1"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/html/2602.06508v1"}]

Based on the search results, here are the method details for SC-VLA (arXiv 2602.21633):

## SC-VLA Method Overview

Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.

## Key Components

**Sparse World Imagination:** The method integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.

**Online Action Refinement Module:** SC-VLA 
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-15T20:53:17.850360+00:00_

Web search results for query: "LIBERO-Plus arXiv 2510.13626 pi0 UniVLA success rate robot initial state camera viewpoint specific numbers table"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Unified Vision-Language-Action Model","url":"https://arxiv.org/html/2506.19850v1"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2511.11298v1"},{"title":"[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"}]

Based on the search results from arXiv paper 2510.13626 (LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models), here are the key findings about performance under perturbations:

## Key Results

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

## UniVLA Specif
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T20:53:17.850783+00:00_

Web search results for query: "Zhou Zhang Luo "adaptive conformal prediction" "control barrier functions" safe reinforcement learning ICRA 2025 arXiv 2503.17678"

Links: [{"title":"[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2503.17678"},{"title":"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/html/2503.17678"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1000&show=100"},{"title":"Computer Vision and Pattern Recognition Jul 2025","url":"https://arxiv.org/list/cs.CV/2025-07?skip=1500&show=2000"},{"title":"Computer Science Feb 2025 - arXiv","url":"https://arxiv.org/list/cs/2025-02?skip=8775&show=2000"},{"title":"[2302.12238] Improving Adaptive Conformal Prediction Using Self-Supervised Learning","url":"https://arxiv.org/abs/2302.12238"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=1725&show=2000"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/pdf/2410.06494"},{"title":"[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/abs/2506.07804"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=7065&show=2000"}]

I found the paper you're looking for! The paper is "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction" (arXiv 2503.17678).

The authors are Hao Zhou and 2 other authors (including Yanze Zhang), and based on the search results, the third author is Wenhao Luo. The paper addresses safety concerns in learning-enabled autonomous systems, especially for real-world deployment.

The key technical approach is: The Adaptive Conformal Prediction (ACP) is used to quantify the uncertainty from online observations and combin
…[truncated 547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T20:53:17.851116+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus 2510.13626 \"pi0\" OR \"π0\" OR \"pi0-fast\" \"94.2\" OR \"94\" success rate original table results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus 2510.13626 \"pi0\" OR \"π0\" OR \"pi0-fast\" \"94.2\" OR \"94\" success rate original table results"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-15T20:53:17.851354+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SC-VLA self-correcting VLA 2602.21633 how is the action refinement module trained RL or supervised"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SC-VLA self-correcting VLA 2602.21633 how is the action refinement module trained RL or supervised"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-15T20:53:17.851647+00:00_

Web search results for query: "LIBERO-Plus 2510.13626 "pi0" OR "π0" OR "pi0-fast" "94.2" OR "94" success rate original table results"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626.pdf"},{"title":"Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2114"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2533"}]

I found relevant information about the LIBERO-Plus paper (arXiv:2510.13626) and related models. Based on the search results, the LIBERO-Plus paper evaluated 10,030 tasks using four representative models—OpenVLA-OFT, π0, π0-fast, and UniVLA.

However, I was unable to lo
…[truncated 835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T20:53:17.851932+00:00_

Web search results for query: "SC-VLA self-correcting VLA 2602.21633 how is the action refinement module trained RL or supervised"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/html/2405.17418v2"},{"title":"From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/pdf/2602.01811"},{"title":"[2405.17418] A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/abs/2405.17418"},{"title":"[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/abs/2602.01811"},{"title":"DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving","url":"https://arxiv.org/html/2602.14577"},{"title":"JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse","url":"https://craftjarvis.github.io/JarvisVLA/"}]

Based on the search results for SC-VLA (arXiv:2602.21633), the online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states. 

The Online Action Refinement (OAR) dynamically optimizes policies via residual adjustments and reshaped rewards. This indicates that
…[truncated 446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T20:53:17.852299+00:00_

called mcp__agent-ml-research__edit_paper_section

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "section": "introduction",
  "old_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method.",
  "new_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "section": "introduction",
    "old_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method.",
    "new_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals."
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T20:53:17.852534+00:00_

{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex\", \"version\": 8, \"coverage\": \"0/0\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T20:53:17.852758+00:00_

called mcp__agent-ml-research__edit_paper_section

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "section": "related_work",
  "old_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions.",
  "new_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "section": "related_work",
    "old_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions.",
    "new_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining."
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T20:53:17.852972+00:00_

{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex\", \"version\": 9, \"coverage\": \"0/0\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T20:53:17.853220+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "old_string": "    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
  "new_string": "    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
    "old_string": "    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
    "new_string": "    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T20:53:17.853442+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T20:53:17.853641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "offset": "305",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
    "offset": "305",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-15T20:53:17.853870+00:00_

305	    primaryClass={cs.RO}
306	}
307	
308	@inproceedings{zhou2025acp_cbf,
309	    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},
310	    author={Hao Zhou and Yanze Zhang and Wenhao Luo},
311	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
312	    year={2025},
313	    note={arXiv:2503.17678}
314	}
315	
316	@misc{zollo2025vla_calibration,
317	    title={Confidence Calibration in Vision-Language-Action Models},
318	    author={Thomas Zollo and Richard Zemel},
319	    year={2025},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T20:53:17.854069+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "old_string": "    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
  "new_string": "    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
    "old_string": "    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
    "new_string": "    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T20:53:17.854339+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-15T20:53:17.854567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "offset": "13",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
    "offset": "13",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T20:53:17.854752+00:00_

13	\emph{Inference-time methods} leave the policy frozen.
14	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.
15	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step---too slow for real-time manipulation.
16	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
17	In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T20:53:17.854936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "offset": "14",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "offset": "14",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T20:53:17.855119+00:00_

14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-15T20:53:17.855377+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reference_audit_r2",
  "type": "report",
  "description": "Method attribution audit for all citations in the ACR-VLA paper (intro, method, experiments, related work, discussion). Verified each citation's method description against the actual paper via web search.",
  "project": "acr-vla-conformal-refinement",
  "content_filename": "reference_audit_r2.md",
  "content": "# Method Attribution Audit — ACR-VLA Paper (R2)\n\n**Date**: 2026-05-15\n**Scope**: All citations across Introduction, Method, Experiments, Related Work, Discussion sections\n**Method**: Web search verification of each citation's method description against actual paper content\n\n---\n\n## Summary\n\n- **Total citations audited**: 30 unique references\n- **Critical errors found & fixed**: 2 (ReconVLA attribution in intro + related work)\n- **Bib title error found & fixed**: 1 (ACP+CBF)\n- **Minor issues flagged**: 2 (SC-VLA classification, LIBERO-Plus specific numbers)\n- **All other attributions**: ✅ Verified correct\n\n---\n\n## FIXED: ReconVLA (chen2026reconvla) — CRITICAL\n\n### Error\n**Intro**: \"operates as an uncertainty quantification framework rather than an action improvement method\"\n**Related Work**: \"providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions\"\n\n### Reality\nReconVLA uses CQR-based uncertainty estimation to **guide action selection** under generative variability and performs OOD/failure detection. It DOES influence action selection, contradicting \"does not modify the VLA's actions.\"\n\n### Fix Applied\n**Intro**: → \"applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\"\n**Related Work**: → \"applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.\"\n\n### D034 Alignment\nNow correctly positions ReconVLA as a **UQ-guided approach** (same domain, different route) rather than a direct competitor or a passive UQ tool. The gap statement (\"no existing inference-time method combines multi-sample conformal selection with bounded residual correction\") remains valid since ReconVLA does UQ-guided selection but not learned residual correction.\n\n---\n\n## FIXED: ACP+CBF Bib Title (zhou2025acp_cbf)\n\n### Error\nBib entry title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\nActual paper title: \"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction\"\n\n### Fix Applied\nUpdated bib entry title to match actual paper.\n\n---\n\n## FLAGGED (not changed): SC-VLA \"residual RL\" Classification\n\n### Current Text\n\"SC-VLA performs online action refinement through sparse world imagination combined with residual RL\"\n\n### Observation\nSC-VLA uses an Online Action Refinement (OAR) module with progress-dependent dense rewards and residual adjustments. The term \"residual RL\" is defensible (it does use RL with residual adjustments) but could be confused with the RPL framework (Silver et al.). More precise would be \"RL-based action refinement with progress-dependent rewards.\"\n\n### Recommendation\nMinor issue — acceptable as-is. Consider \"online RL\" instead of \"residual RL\" if a future revision refines the taxonomy.\n\n---\n\n## FLAGGED (not changed): LIBERO-Plus Specific Numbers\n\n### Current Text (Intro)\n\"π₀ drops from 94.2% to 6.6% under robot initial-state perturbation, and UniVLA from 95.2% to 4.3% under camera viewpoint changes\"\n\n### Observation\n- LIBERO-Plus tests π0, π0-fast, UniVLA, OpenVLA-OFT among others\n- Web search confirms UniVLA achieves ~95.5% baseline (close to cited 95.2%)\n- General trend (dramatic drops under perturbation) is confirmed\n- Exact numbers (94.2%, 6.6%, 95.2%, 4.3%) could not be precisely verified via web search alone\n\n### Recommendation\nVerify exact numbers against LIBERO-Plus Table 1 before submission. The general claim is sound.\n\n---\n\n## Verified Correct: All Other Citations\n\n### Training-time VLA Robustness\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `robustvla2025` | RL post-training + Jacobian regularization + smoothness regularization | ✅ Confirmed |\n| `srpo2025` | Self-referential RL fine-tuning, own successful rollouts as references, latent world model | ✅ Confirmed |\n| `digflow2025` | Distributional discrepancy as gating signal to rebalance representation-level control | ✅ Confirmed |\n| `liu2026ttvla` | Test-time RL with step-by-step progress rewards | ✅ Confirmed |\n\n### Inference-time VLA Methods\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `a2c2_2025` | Lightweight per-step correction head for action chunks, no selection stage | ✅ Confirmed |\n| `li2025vlapilot` | Evolutionary diffusion optimization + MLLM verifier, 2.41s/step | ✅ Confirmed |\n| `liu2026scvla` | Online action refinement via sparse world imagination + RL | ✅ (see flag above) |\n\n### Conformal Prediction in Robotics\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `angelopoulos2023gentle` | Distribution-free coverage guarantees under exchangeability | ✅ Confirmed |\n| `braun2025cgs` | CGS: Mahalanobis-based nonconformity scores for multivariate CP | ✅ Confirmed |\n| `zhao2024conformalized` | CP for high-DOF action mappings in shared autonomy teleoperation | ✅ Confirmed |\n| `wang2025cploop` | CP regions as feedback constraints in trajectory optimization | ✅ Confirmed |\n| `zhou2025acp_cbf` | Adaptive CP + control barrier functions for safe RL | ✅ Confirmed |\n\n### Residual Policy Learning\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `silver2018residual` | Introduced RPL framework for classical controllers, zero-initialization | ✅ Confirmed |\n| `jiang2024transic` | Gated residual policy for sim-to-real transfer | ✅ Confirmed |\n| `xiao2026pld` | Frozen VLA + lightweight residual actors + off-policy RL + distillation | ✅ Confirmed |\n| `pan2025drc` | Decaying relative correction for online imitation learning via teleoperation | ✅ Confirmed |\n\n### Uncertainty Quantification for VLAs\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `xing2026diu` | Closed-form posterior covariance via velocity field divergence (single-pass) | ✅ Confirmed |\n| `gu2025safe` | Multitask failure detector on VLA features + functional CP calibration | ✅ Confirmed |\n| `zollo2025vla_calibration` | First systematic VLA calibration study, prompt ensembles + Platt scaling | ✅ Confirmed |\n\n### Foundation / Infrastructure\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `black2024pi0` | π₀: flow-matching VLA | ✅ |\n| `shukor2025smolvla` | SmolVLA: 450M flow-matching VLA | ✅ |\n| `lipman2023flow` | Flow matching for generative modeling | ✅ |\n| `liu2023libero` | LIBERO benchmark | ✅ |\n| `fei2025liberoplus` | LIBERO-Plus robustness analysis | ✅ (numbers flagged) |\n| `ledoit2004well` | Ledoit-Wolf shrinkage covariance estimation | ✅ |\n| `ross2011dagger` | DAgger / compounding error in imitation learning | ✅ |\n\n---\n\n## Pre-Submission Checklist\n- [x] ReconVLA attribution fixed (intro + related work)\n- [x] ACP+CBF bib title corrected\n- [ ] Verify LIBERO-Plus exact numbers (94.2%, 6.6%, 95.2%, 4.3%) against Table 1\n- [ ] Consider refining SC-VLA \"residual RL\" → \"online RL\" (optional)\n",
  "tags": "['audit', 'paper', 'references', 'corl-submission']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reference_audit_r2",
    "type": "report",
    "description": "Method attribution audit for all citations in the ACR-VLA paper (intro, method, experiments, related work, discussion). Verified each citation's method description against the actual paper via web search.",
    "project": "acr-vla-conformal-refinement",
    "content_filename": "reference_audit_r2.md",
    "content": "# Method Attribution Audit — ACR-VLA Paper (R2)\n\n**Date**: 2026-05-15\n**Scope**: All citations across Introduction, Method, Experiments, Related Work, Discussion sections\n**Method**: Web search verification of each citation's method description against actual paper content\n\n---\n\n## Summary\n\n- **Total citations audited**: 30 unique references\n- **Critical errors found & fixed**: 2 (ReconVLA attribution in intro + related work)\n- **Bib title error found & fixed**: 1 (ACP+CBF)\n- **Minor issues flagged**: 2 (SC-VLA classification, LIBERO-Plus specific numbers)\n- **All other attributions**: ✅ Verified correct\n\n---\n\n## FIXED: ReconVLA (chen2026reconvla) — CRITICAL\n\n### Error\n**Intro**: \"operates as an uncertainty quantification framework rather than an action improvement method\"\n**Related Work**: \"providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions\"\n\n### Reality\nReconVLA uses CQR-based uncertainty estimation to **guide action selection** under generative variability and performs OOD/failure detection. It DOES influence action selection, contradicting \"does not modify the VLA's actions.\"\n\n### Fix Applied\n**Intro**: → \"applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\"\n**Related Work**: → \"applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.\"\n\n### D034 Alignment\nNow correctly positions ReconVLA as a **UQ-guided approach** (same domain, different route) rather than a direct competitor or a passive UQ tool. The gap statement (\"no existing inference-time method combines multi-sample conformal selection with bounded residual correction\") remains valid since ReconVLA does UQ-guided selection but not learned residual correction.\n\n---\n\n## FIXED: ACP+CBF Bib Title (zhou2025acp_cbf)\n\n### Error\nBib entry title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\nActual paper title: \"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction\"\n\n### Fix Applied\nUpdated bib entry title to match actual paper.\n\n---\n\n## FLAGGED (not changed): SC-VLA \"residual RL\" Classification\n\n### Current Text\n\"SC-VLA performs online action refinement through sparse world imagination combined with residual RL\"\n\n### Observation\nSC-VLA uses an Online Action Refinement (OAR) module with progress-dependent dense rewards and residual adjustments. The term \"residual RL\" is defensible (it does use RL with residual adjustments) but could be confused with the RPL framework (Silver et al.). More precise would be \"RL-based action refinement with progress-dependent rewards.\"\n\n### Recommendation\nMinor issue — acceptable as-is. Consider \"online RL\" instead of \"residual RL\" if a future revision refines the taxonomy.\n\n---\n\n## FLAGGED (not changed): LIBERO-Plus Specific Numbers\n\n### Current Text (Intro)\n\"π₀ drops from 94.2% to 6.6% under robot initial-state perturbation, and UniVLA from 95.2% to 4.3% under camera viewpoint changes\"\n\n### Observation\n- LIBERO-Plus tests π0, π0-fast, UniVLA, OpenVLA-OFT among others\n- Web search confirms UniVLA achieves ~95.5% baseline (close to cited 95.2%)\n- General trend (dramatic drops under perturbation) is confirmed\n- Exact numbers (94.2%, 6.6%, 95.2%, 4.3%) could not be precisely verified via web search alone\n\n### Recommendation\nVerify exact numbers against LIBERO-Plus Table 1 before submission. The general claim is sound.\n\n---\n\n## Verified Correct: All Other Citations\n\n### Training-time VLA Robustness\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `robustvla2025` | RL post-training + Jacobian regularization + smoothness regularization | ✅ Confirmed |\n| `srpo2025` | Self-referential RL fine-tuning, own successful rollouts as references, latent world model | ✅ Confirmed |\n| `digflow2025` | Distributional discrepancy as gating signal to rebalance representation-level control | ✅ Confirmed |\n| `liu2026ttvla` | Test-time RL with step-by-step progress rewards | ✅ Confirmed |\n\n### Inference-time VLA Methods\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `a2c2_2025` | Lightweight per-step correction head for action chunks, no selection stage | ✅ Confirmed |\n| `li2025vlapilot` | Evolutionary diffusion optimization + MLLM verifier, 2.41s/step | ✅ Confirmed |\n| `liu2026scvla` | Online action refinement via sparse world imagination + RL | ✅ (see flag above) |\n\n### Conformal Prediction in Robotics\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `angelopoulos2023gentle` | Distribution-free coverage guarantees under exchangeability | ✅ Confirmed |\n| `braun2025cgs` | CGS: Mahalanobis-based nonconformity scores for multivariate CP | ✅ Confirmed |\n| `zhao2024conformalized` | CP for high-DOF action mappings in shared autonomy teleoperation | ✅ Confirmed |\n| `wang2025cploop` | CP regions as feedback constraints in trajectory optimization | ✅ Confirmed |\n| `zhou2025acp_cbf` | Adaptive CP + control barrier functions for safe RL | ✅ Confirmed |\n\n### Residual Policy Learning\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `silver2018residual` | Introduced RPL framework for classical controllers, zero-initialization | ✅ Confirmed |\n| `jiang2024transic` | Gated residual policy for sim-to-real transfer | ✅ Confirmed |\n| `xiao2026pld` | Frozen VLA + lightweight residual actors + off-policy RL + distillation | ✅ Confirmed |\n| `pan2025drc` | Decaying relative correction for online imitation learning via teleoperation | ✅ Confirmed |\n\n### Uncertainty Quantification for VLAs\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `xing2026diu` | Closed-form posterior covariance via velocity field divergence (single-pass) | ✅ Confirmed |\n| `gu2025safe` | Multitask failure detector on VLA features + functional CP calibration | ✅ Confirmed |\n| `zollo2025vla_calibration` | First systematic VLA calibration study, prompt ensembles + Platt scaling | ✅ Confirmed |\n\n### Foundation / Infrastructure\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `black2024pi0` | π₀: flow-matching VLA | ✅ |\n| `shukor2025smolvla` | SmolVLA: 450M flow-matching VLA | ✅ |\n| `lipman2023flow` | Flow matching for generative modeling | ✅ |\n| `liu2023libero` | LIBERO benchmark | ✅ |\n| `fei2025liberoplus` | LIBERO-Plus robustness analysis | ✅ (numbers flagged) |\n| `ledoit2004well` | Ledoit-Wolf shrinkage covariance estimation | ✅ |\n| `ross2011dagger` | DAgger / compounding error in imitation learning | ✅ |\n\n---\n\n## Pre-Submission Checklist\n- [x] ReconVLA attribution fixed (intro + related work)\n- [x] ACP+CBF bib title corrected\n- [ ] Verify LIBERO-Plus exact numbers (94.2%, 6.6%, 95.2%, 4.3%) against Table 1\n- [ ] Consider refining SC-VLA \"residual RL\" → \"online RL\" (optional)\n",
    "tags": "['audit', 'paper', 'references', 'corl-submission']"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T20:53:17.855779+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_fa22d2\", \"name\": \"reference_audit_r2\", \"type\": \"report\", \"description\": \"Method attribution audit for all citations in the ACR-VLA paper (intro, method, experiments, related work, discussion). Verified each citation's method description against the actual paper via web search.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/reference_audit_r2.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T20:53:08.961788+00:00\", \"tags\": [\"audit\", \"paper\", \"references\", \"corl-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-audit-r2_20260515T204542",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 95 · 2026-05-15T20:53:17.856042+00:00_

Audit complete. Here's the summary:

### Fixes Applied (3)

1. **ReconVLA intro** — Changed "operates as an uncertainty quantification framework rather than an action improvement method" → correctly describes it as using UQ for **action selection and OOD detection**, taking a "complementary UQ-driven approach rather than learning explicit corrective residuals"

2. **ReconVLA related work** — Changed "does not modify the VLA's actions" → correctly states it "enables uncertainty-guided action selection and proactive failure detection without retraining"

3. **ACP+CBF bib title** — Corrected from fabricated title to actual paper title "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction"

### Flagged for Pre-Submission (2, not blocking)

- **LIBERO-Plus numbers** (94.2%→6.6% for π₀, 95.2%→4.3% for UniVLA) — general trend confirmed, exact numbers need verification against Table 1 of the actual paper
- **SC-VLA "residual RL"** — defensible but imprecise; "online RL" would be more accurate

### Verified Correct (27/30 citations)
All other method attributions checked out against the actual papers via web search.

Full report registered as `artifacts/_project/report/reference_audit_r2.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_reference-audit-r2_20260515T204542"
}
```

</details>

---
