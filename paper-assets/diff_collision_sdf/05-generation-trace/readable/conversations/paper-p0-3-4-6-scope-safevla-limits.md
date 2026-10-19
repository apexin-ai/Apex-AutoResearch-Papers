# paper p0 3 4 6 scope safevla limits

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943.jsonl`
- **Structured JSON:** [`f9e7d024157f382490c6.json`](../../sessions/f9/f9e7d024157f382490c6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-28T06:11:20.900928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T06:11:20.901443+00:00_

1	\section{Introduction}\label{sec:intro}
2	
3	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$; Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{fake safety}: \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Fake safety is pervasive.} We int
…[truncated 2227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T06:11:20.901685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T06:11:20.901855+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.
7	
8	\parag
…[truncated 1780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T06:11:20.902017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T06:11:20.902171+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. SafeDiffuser~\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. CDF~\cite{li202
…[truncated 1445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T06:11:20.902317+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "safevla|vlsa|SafeVLA|VLSA",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
  "output_mode": "content",
  "-i": "True",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Grep",
  "tool_args": {
    "pattern": "safevla|vlsa|SafeVLA|VLSA",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
    "output_mode": "content",
    "-i": "True",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T06:11:20.902481+00:00_

28-% ===== Collision-Aware VLA Methods =====
29-
30:@article{hu2025vlsa,
31:  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
32-  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},
33-  journal={arXiv preprint arXiv:2512.11891},
--
35-}
36-
37:@inproceedings{zhang2025safevla,
38:  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
39-  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},
40-  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T06:11:20.902684+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "case study",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Grep",
  "tool_args": {
    "pattern": "case study",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T06:11:20.902817+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T06:11:20.902939+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "we demonstrate",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Grep",
  "tool_args": {
    "pattern": "we demonstrate",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T06:11:20.903059+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T06:11:20.903225+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Evaluation Metrics for Safe Manipulation.}",
  "new_string": "\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constraint-based planning}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
    "old_string": "\\paragraph{Evaluation Metrics for Safe Manipulation.}",
    "new_string": "\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constraint-based planning}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T06:11:20.903388+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T06:11:20.903559+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
  "new_string": "These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
    "new_string": "These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T06:11:20.903723+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T06:11:20.903856+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.",
  "new_string": "\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.",
    "new_string": "\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T06:11:20.904028+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T06:11:20.904155+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.",
  "new_string": "\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.",
    "new_string": "\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T06:11:20.904310+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T06:11:20.904463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T06:11:20.904624+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure
…[truncated 3815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T06:11:20.904770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T06:11:20.904926+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. SafeDiffuser~\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. CDF~\cite{li202
…[truncated 2384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T06:11:20.905071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python paper_switch.py --verify 2>&1",
  "description": "Run paper_switch.py --verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python paper_switch.py --verify 2>&1",
    "description": "Run paper_switch.py --verify"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T06:11:20.905190+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T06:11:20.905306+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python3 paper_switch.py --verify 2>&1",
  "description": "Run paper_switch.py --verify with python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python3 paper_switch.py --verify 2>&1",
    "description": "Run paper_switch.py --verify with python3"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T06:11:20.905461+00:00_

--- Scenario B (10 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      claim3 L38 fig caption              claim3.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
--- Scenario C (11 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      claim3 L38 fig caption              claim3.tex
  [OK]      discussion L3 scope                 discussion.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-28T06:11:20.905668+00:00_

全部通过。下面是修改汇总：

---

### related_work.tex

**新增** `\paragraph{SDF integration pathways.}`（第12行，"Signed Distance Functions in Robotics" 和 "Evaluation Metrics" 之间）：
- 区分三种 SDF 集成路径：(a) training-time auxiliary loss, (b) constraint-based planning (SafeVLA), (c) runtime filtering (VLSA)
- 明确本文负面发现仅适用于 pathway (a)
- 引用键 `zhang2025safevla` 和 `hu2025vlsa` 均已验证存在于 bib 中

---

### discussion.tex

**4 处修改**：

1. **第6行末尾新增** pathway-specific 句子：
   > "The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms."

2. **第11行新增** `\paragraph{Scope and generalizability.}`（Implications 和 Limitations 之间）：
   - 明确列出 scope：1 benchmark, 2 model families, 4 tasks, MuJoCo simulation
   - 区分 Claim 1 的结构通用性 vs. prevalence 的 benchmark-specificity
   - Claim 3 限定为 EE-only auxiliary loss pathway，引用 `\ref{sec:related}`

3. **第13-14行替换** Limitations 段落：
   - **新增**：sim-to-real gap 不确定性、sensor noise 影响、task diversity 限制、统计功效（n=3, ~5pp MDE at 80% power）
   - **保留**：原有的 oracle frozen model、full-body SDF untested、TSR degradation 内容

4. **第19-20行替换** Broader Impact 段落：
   - **改前**：2 句（dfCAR exposes gap）
   - **改后**：3 句——dfCAR 定位为 diagnostic complement、SDF redundancy 是 methodology insight 而非对 safety training 的否定、警告不要过度解读

---

### introduction.tex

未修改。"case study" 和 "we demonstrate" 在当前版本中均不存在（已被前一个 Worker 处理）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943"
}
```

</details>

---
