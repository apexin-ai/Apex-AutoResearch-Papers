# paper p1 1 terminology

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 91
- **Recorded user turns:** 0
- **Tool calls:** 45
- **Original source:** `logs/chats/worker_paper_p1-1-terminology_20260528T061837.jsonl`
- **Structured JSON:** [`1bf5443e43ee4e6ab199.json`](../../sessions/1b/1bf5443e43ee4e6ab199.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

91 recorded events

### Tool call

_source line 1 · 2026-05-28T06:22:21.436488+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "frozen episode|frozen episodes|frozen rate",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "tool_args": {
    "pattern": "frozen episode|frozen episodes|frozen rate",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T06:22:21.436843+00:00_

docs/paper/claim3.tex:3:Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
docs/paper/claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
docs/paper/claim3.tex:26:[Omitted long matching line]
docs/paper/claim3.tex:29:Fine-tuning degrades TSR by ${\sim}$18--20\,pp (71.5\% $\to$ 51.5--54.0\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
docs/paper/experimental_framework.tex:25:\paragraph{Auxiliary metrics.} We additionally report the \emph{Frozen Rate}, the fraction of episodes with $d_{\max} < \tau_d$, which quantifies the severity of action collapse for each method. The \emph{Simultaneous Success Rate} (SSR $= $ TSR $\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.
docs/paper/archive/analysis_claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active colli
…[truncated 1184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T06:22:21.437042+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fake safe|fake safety|Fake Safety|Fake safe",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fake safe|fake safety|Fake Safety|Fake safe",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T06:22:21.437218+00:00_

docs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:7:\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
docs/paper/archive/analysis_claim2.tex:13:Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
docs/paper/archive/analysis_claim2.tex:27:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:1:\subsection{The Fake Safety Problem}\label{sec:fake_safety}
docs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:9:\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
docs/paper/archive/analysis_claim1.tex:15:Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
docs/paper/archive/analysis_claim1.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:38:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/claim2.tex:13:Method & CAR (\%) & Fake Safe (\%) & Refines/ep \\
docs/paper/appendix.tex:14:To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
docs/paper/introduction.tex:8:\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out acti
…[truncated 1380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T06:22:21.437381+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\bfrozen\\b",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\bfrozen\\b",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T06:22:21.437631+00:00_

docs/paper/related_work.tex:15:[Omitted long matching line]
docs/paper/claim3.tex:3:Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
docs/paper/claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
docs/paper/claim3.tex:26:[Omitted long matching line]
docs/paper/claim3.tex:29:Fine-tuning degrades TSR by ${\sim}$18--20\,pp (71.5\% $\to$ 51.5--54.0\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
docs/paper/discussion.tex:14:[Omitted long matching line]
docs/paper/experimental_framework.tex:25:\paragraph{Auxiliary metrics.} We additionally report the \emph{Frozen Rate}, the fraction of episodes with $d_{\max} < \tau_d$, which quantifies the severity of action collapse for each method. The \emph{Simultaneous Success Rate} (SSR $= $ TSR $\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.
docs/paper/experimental_framework.tex:36:\item \textit{Pi0.5 + A1}: The A1 architecture applied to the Pi0.5 backbone. Training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features w
…[truncated 4169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T06:22:21.437841+00:00_

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
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T06:22:21.438007+00:00_

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
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T06:22:21.438165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T06:22:21.438316+00:00_

1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\% of collision-free episodes are action-collapse artifacts (Table~\ref{tab:fake_safety}).\footnote{Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (\S\ref{sec:dfcar}). Sub-millimeter displacement indicates action collapse in both cases.} Applying dfCAR collapses all three to ${\approx}$\,0\%. Pi0+A1 achieves the \emph{highest} raw CAR (91.5\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\ref{tab:configurations}) yields higher fake safety. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\,mm displacement, and dfCAR equals raw CAR (28.5\%). The displacement distribution is sharply bimodal (Appendix~\ref{sec:appendix_displacement}), with a five-order-of-magnitude gap that makes $\tau_d$ robust.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Fake safety decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau_d = 0.1$\,mm.}
8	\label{tab:fake_safety}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Ep. & CAR (\%) & TSR (\%) & Fake Safe (\%) & dfCAR (\%) \\
14	\midrule
15	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\approx$\,0 \\
16	Pi0 LoRA     & 200 & 82.0 & 0.0 & ${\sim}$99 & $\approx$\,0 \\
17	Pi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\approx$\,0$^*$ \\
18	\midrule
19	Pi0.5  & 200 & 28.5 & 71.5 & 0.0 & 28.5 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1pt}
23	{\footnotesize $^*$\,3/732 safe episodes above threshold; denominator too small for reliable rate.}
24	\end{table}
25	
26	Figure~\ref{fig:tsr_car_scatter} reveals spatial structure in the TSR-CAR plane.\label{sec:anticorrelation} Pi0-family models cluster
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T06:22:21.438505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T06:22:21.438673+00:00_

1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_bar} show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccc}
12	\toprule
13	Method & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 77.1 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{figure}[t]
28	\centering
29	\includegraphics[width=0.85\linewidth]{fig_oracle_bar.pdf}
30	\caption{CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform baselines despite perfect distance information.}
31	\label{fig:oracle_bar}
32	\end{figure}
33	
34	Per-task analysis reveals the mechanism (Appendix~\ref{sec:appendix_pertask_oracle}). On the one task where the EE is the primary collision body, oracle refinement helps (+9 points). On the remaining three, the SDF gradient pushes the EE away from obstacles but rotates intermediate arm links into obstacle volumes; the net effect is one collision trad
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T06:22:21.438824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T06:22:21.438993+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,58
…[truncated 4014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T06:22:21.439148+00:00_

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
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T06:22:21.439302+00:00_

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
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T06:22:21.439481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T06:22:21.439666+00:00_

1	\section{Experimental Framework}\label{sec:framework}
2	
3	This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (dfCAR), which separates genuine avoidance from action collapse.
4	
5	\subsection{Benchmark and Evaluation Protocol}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
8	
9	We select the \textit{object\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.
10	
11	Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
12	
13	\subsection{Evaluation Metrics}\label{sec:metrics}
14	
15	\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
16	
17	\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, 
…[truncated 4574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T06:22:21.439814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T06:22:21.439968+00:00_

1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	\subsection{Benchmark and Models}\label{sec:benchmark}
4	
5	We evaluate on SafeLIBERO~\cite{hu2025vlsa}, the \textit{object\_pudding} suite (Level~II): four tabletop pick-and-place tasks with collision hazards and per-timestep collision detection. Two VLA families are tested: \textbf{Pi0} (${\sim}$2.5B)~\cite{black2024pi0} with flow matching~\cite{lipman2023flow}, and \textbf{Pi0.5} with broader pre-training. Table~\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). All metrics are computed using a fixed evaluation seed (seed\,=\,7); the reported $\pm$ values reflect variance across training seeds, not evaluation stochasticity. We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction of episodes that complete the task~\cite{hu2025vlsa,zhang2025safevla}.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Training configurations. Trainable parameters exclude the frozen backbone.}
10	\label{tab:configurations}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{llr}
14	\toprule
15	Configuration & Description & Trainable Params \\
16	\midrule
17	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
18	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
19	Pi0+A1 (SDF aux)\textsuperscript{$\dagger$} & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
20	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
21	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
22	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
23	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
24	\bottomrule
25	\end{tabular}
26	\vspace{2pt}
27	\raggedright\footnotesize\textsuperscript{$\dagger$}LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained.
28	\end{table}
29	
30	
…[truncated 1646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T06:22:21.440118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T06:22:21.440254+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\,mm. The robot is frozen, not safe.
4	We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\,mm threshold range.
5	We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\lambda \in \{0.005, 0.01, 0.1\}$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; $\lambda = 0.1$: 57.00\%$\,\pm\,$2.18, 3 seeds).
6	Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across a 20$\times$ loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T06:22:21.440385+00:00_

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
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T06:22:21.440556+00:00_

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
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T06:22:21.440705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T06:22:21.440982+00:00_

1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Frozen rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\
…[truncated 23824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T06:22:21.441148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T06:22:21.441332+00:00_

1	% contingency_claim3.tex — Three pre-written §6.3 paragraphs for λ=0.1 results.
2	% NOT \input'd into main.tex. Copy the matching scenario into claim3.tex
3	% when results arrive. Replace {MEAN}, {S0}, {S1} with actual numbers.
4	%
5	% Scenario selection (D033 thresholds):
6	%   B: CAR mean ≤ 57%    → full redundancy confirmed
7	%   C: CAR mean 57–60%   → inconclusive, flag 2/3 seeds
8	%   A: CAR mean > 60%    → dose-response evidence
9	%
10	% Also includes discussion + abstract patch bullets at the end.
11	
12	
13	%% ====================================================================
14	%% SCENARIO B — Full redundancy (CAR ≤ 57%)
15	%% ====================================================================
16	
17	% --- claim3 §6.3 paragraph ---
18	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
19	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), within the null distribution (mean 54.5\%, $\sigma = 2.15$). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude (Level~A) but the structural mismatch between end-effector monitoring and full-body collision surfaces (Level~B). Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
20	
21	
22	%% ====================================================================
23	%% SCENARIO C — Inconclusive / gray zone (CAR 57–60%)
24	%% ====================================================================
25	
26	% --- claim3 §6.3 paragraph ---
27	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
28	At $\lambda = 0.1$, CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), representing a suggestive 
…[truncated 4686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T06:22:21.441606+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "The robot is frozen, not safe.",
  "new_string": "The robot is action-collapsed, not safe."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "old_string": "The robot is frozen, not safe.",
    "new_string": "The robot is action-collapsed, not safe."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T06:22:21.441762+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-28T06:22:21.441907+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left).",
  "new_string": "\\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "old_string": "\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left).",
    "new_string": "\\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left)."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T06:22:21.442064+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-28T06:22:21.442195+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{fake safety}: \\emph{action collapse}",
  "new_string": "The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{action-collapsed safety} (colloquially, ``fake safety''): \\emph{action collapse}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "old_string": "The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{fake safety}: \\emph{action collapse}",
    "new_string": "The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{action-collapsed safety} (colloquially, ``fake safety''): \\emph{action collapse}"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T06:22:21.442343+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T06:22:21.442488+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "\\textbf{Fake safety is pervasive.}",
  "new_string": "\\textbf{Action collapse is pervasive.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "old_string": "\\textbf{Fake safety is pervasive.}",
    "new_string": "\\textbf{Action collapse is pervasive.}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T06:22:21.442636+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T06:22:21.442755+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "with zero frozen episodes. Adding",
  "new_string": "with zero action-collapsed episodes. Adding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "old_string": "with zero frozen episodes. Adding",
    "new_string": "with zero action-collapsed episodes. Adding"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-28T06:22:21.442894+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-28T06:22:21.443014+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "\\item \\textbf{Fake safety diagnosis:}",
  "new_string": "\\item \\textbf{Action-collapse diagnosis:}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "old_string": "\\item \\textbf{Fake safety diagnosis:}",
    "new_string": "\\item \\textbf{Action-collapse diagnosis:}"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-28T06:22:21.443150+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-28T06:22:21.443289+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
  "old_string": "\\section{The Fake Safety Problem}\\label{sec:fake_safety}",
  "new_string": "\\section{The Action-Collapsed Safety Problem}\\label{sec:fake_safety}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
    "old_string": "\\section{The Fake Safety Problem}\\label{sec:fake_safety}",
    "new_string": "\\section{The Action-Collapsed Safety Problem}\\label{sec:fake_safety}"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-28T06:22:21.443451+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-28T06:22:21.443585+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
  "old_string": "yields higher fake safety.",
  "new_string": "yields greater CAR inflation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
    "old_string": "yields higher fake safety.",
    "new_string": "yields greater CAR inflation."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T06:22:21.443727+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-28T06:22:21.443848+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
  "old_string": "\\caption{Fake safety decomposition on SafeLIBERO.",
  "new_string": "\\caption{Action-collapse decomposition on SafeLIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
    "old_string": "\\caption{Fake safety decomposition on SafeLIBERO.",
    "new_string": "\\caption{Action-collapse decomposition on SafeLIBERO."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T06:22:21.443981+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-28T06:22:21.444100+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
  "old_string": "Fake Safe (\\%)",
  "new_string": "Collapsed (\\%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
    "old_string": "Fake Safe (\\%)",
    "new_string": "Collapsed (\\%)"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-28T06:22:21.444232+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-28T06:22:21.444369+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex",
  "old_string": "Fake Safe (\\%)",
  "new_string": "Collapsed (\\%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex",
    "old_string": "Fake Safe (\\%)",
    "new_string": "Collapsed (\\%)"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T06:22:21.444532+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-28T06:22:21.444670+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "with zero frozen episodes. Does SDF",
  "new_string": "with zero action-collapsed episodes. Does SDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "with zero frozen episodes. Does SDF",
    "new_string": "with zero action-collapsed episodes. Does SDF"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-28T06:22:21.444789+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-28T06:22:21.444912+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "0\\% frozen rate and displacement",
  "new_string": "0\\% action-collapse rate and displacement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "0\\% frozen rate and displacement",
    "new_string": "0\\% action-collapse rate and displacement"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-28T06:22:21.445030+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-28T06:22:21.445144+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "with zero frozen episodes and displacement above 0.37\\,m",
  "new_string": "with zero action-collapsed episodes and displacement above 0.37\\,m"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "with zero frozen episodes and displacement above 0.37\\,m",
    "new_string": "with zero action-collapsed episodes and displacement above 0.37\\,m"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-28T06:22:21.445259+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-28T06:22:21.445372+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "and 0\\% frozen episodes)",
  "new_string": "and 0\\% action-collapsed episodes)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "and 0\\% frozen episodes)",
    "new_string": "and 0\\% action-collapsed episodes)"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T06:22:21.445516+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-28T06:22:21.445631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-28T06:22:21.445792+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,5
…[truncated 4026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-28T06:22:21.445941+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "with zero frozen episodes. Does SDF",
  "new_string": "with zero action-collapsed episodes. Does SDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "with zero frozen episodes. Does SDF",
    "new_string": "with zero action-collapsed episodes. Does SDF"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-28T06:22:21.446088+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-28T06:22:21.446207+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "0\\% frozen rate and displacement",
  "new_string": "0\\% action-collapse rate and displacement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "0\\% frozen rate and displacement",
    "new_string": "0\\% action-collapse rate and displacement"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-28T06:22:21.446350+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-28T06:22:21.446489+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "with zero frozen episodes and displacement above 0.37\\,m",
  "new_string": "with zero action-collapsed episodes and displacement above 0.37\\,m"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "with zero frozen episodes and displacement above 0.37\\,m",
    "new_string": "with zero action-collapsed episodes and displacement above 0.37\\,m"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-28T06:22:21.446646+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-28T06:22:21.446766+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "and 0\\% frozen episodes)",
  "new_string": "and 0\\% action-collapsed episodes)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "and 0\\% frozen episodes)",
    "new_string": "and 0\\% action-collapsed episodes)"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-28T06:22:21.446919+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-28T06:22:21.447060+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex",
  "old_string": "\\emph{Frozen Rate}",
  "new_string": "\\emph{Action-Collapse Rate}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex",
    "old_string": "\\emph{Frozen Rate}",
    "new_string": "\\emph{Action-Collapse Rate}"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-28T06:22:21.447222+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-28T06:22:21.447368+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "we evaluate the frozen rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% frozen rate even at the most conservative setting.",
  "new_string": "we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "we evaluate the frozen rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% frozen rate even at the most conservative setting.",
    "new_string": "we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting."
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-28T06:22:21.447597+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-28T06:22:21.447727+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "\\caption{Frozen rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}",
  "new_string": "\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "\\caption{Frozen rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}",
    "new_string": "\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-28T06:22:21.447926+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-28T06:22:21.448054+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "classified as frozen, while all Pi0.5",
  "new_string": "classified as action-collapsed, while all Pi0.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "classified as frozen, while all Pi0.5",
    "new_string": "classified as action-collapsed, while all Pi0.5"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-28T06:22:21.448252+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-28T06:22:21.448381+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "rather than frozen behavior.",
  "new_string": "rather than action-collapsed behavior."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "rather than frozen behavior.",
    "new_string": "rather than action-collapsed behavior."
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-28T06:22:21.448604+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-28T06:22:21.448757+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "old_string": "a frozen robot scores near-perfect CAR",
  "new_string": "an action-collapsed robot scores near-perfect CAR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
    "old_string": "a frozen robot scores near-perfect CAR",
    "new_string": "an action-collapsed robot scores near-perfect CAR"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-28T06:22:21.448906+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-28T06:22:21.449046+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "a largely frozen model",
  "new_string": "a largely action-collapsed model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "a largely frozen model",
    "new_string": "a largely action-collapsed model"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-28T06:22:21.449194+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-28T06:22:21.449334+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "frozen episode|frozen episodes|frozen rate",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "tool_args": {
    "pattern": "frozen episode|frozen episodes|frozen rate",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-28T06:22:21.449493+00:00_

docs/paper/archive/analysis_claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
docs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:54:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:7:\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\max} < \tau_d$ (action collapse; Section~\ref{sec:metrics}). Pi0.5+A1 produces 0\% frozen episodes at 10K steps, so CAR$_\text{f}$ equals raw CAR.}
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-28T06:22:21.449627+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fake safe|fake safety|Fake Safety|Fake safe",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fake safe|fake safety|Fake Safety|Fake safe",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-28T06:22:21.449759+00:00_

docs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:7:\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
docs/paper/archive/analysis_claim2.tex:13:Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
docs/paper/archive/analysis_claim2.tex:27:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:1:\subsection{The Fake Safety Problem}\label{sec:fake_safety}
docs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:9:\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
docs/paper/archive/analysis_claim1.tex:15:Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
docs/paper/archive/analysis_claim1.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:38:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-28T06:22:21.449896+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\bfrozen\\b",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\bfrozen\\b",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-28T06:22:21.450037+00:00_

docs/paper/experimental_framework.tex:36:\item \textit{Pi0.5 + A1}: The A1 architecture applied to the Pi0.5 backbone. Training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization. We evaluate $\lambda_\text{SDF} \in \{0.005, 0.01\}$.
docs/paper/method.tex:9:\caption{Training configurations. Trainable parameters exclude the frozen backbone.}
docs/paper/archive/analysis_claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
docs/paper/archive/analysis_claim3.tex:13:Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
docs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:54:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:7:\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\max} < \tau_d$ (action collapse; Section~\ref{sec:metrics}). Pi0.5+A1 produces 0\% frozen episodes at 10K steps, so CAR$_\text{f}$ equals raw CAR.}
docs/paper/archive/analysis_claim4.tex:13:Method & TSR (\%) & CAR (\%) & CAR$_\text{f}$ (\%) & SSR (\%) & Frozen (\%) \\
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/_archive/method.tex:95:\paragraph{Phase 1: Auxiliary module warmup ($0 \to 5\mathrm{K}$ steps).} The entire backbone, including LoRA parameters, is frozen. Only the SDF decoder (${\sim}$395K params) and EE extractor (${\sim}$263K params) are trained on detached features ($\bar{\mathbf{z}}.\mathrm{detach}()$) to avoid destabilizing the pretraine
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-28T06:22:21.450218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "limit": "28"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "limit": "28"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-28T06:22:21.450377+00:00_

1	\section{Introduction}\label{sec:intro}
2	
3	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$; Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{action-collapsed safety} (colloquially, ``fake safety''): \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation epis
…[truncated 2322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p1-1-terminology_20260528T061837",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 91 · 2026-05-28T06:22:21.450588+00:00_

All replacements are clean and consistent. Summary of changes across 9 files:

| Term | Replacement | Count |
|---|---|---|
| frozen episodes/episode | action-collapsed episodes/episode | 5 |
| frozen rate / Frozen Rate | action-collapse rate / Action-Collapse Rate | 5 |
| fake safety (after first mention) | action-collapsed safety / action-collapse / CAR inflation | 5 |
| fake safety (first mention, intro:12) | action-collapsed safety (colloquially, "fake safety") | 1 (kept as colloquial note) |
| Fake Safe (%) table header | Collapsed (%) | 2 |
| frozen robot / frozen (robot behavior) | action-collapsed robot / action-collapsed | 6 |

Preserved without changes:
- All `\label{sec:fake_safety}`, `\ref{sec:fake_safety}`, `\label{tab:fake_safety}` identifiers
- "frozen backbone", "parameters are frozen" (ML training terms)
- All `archive/` files

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_p1-1-terminology_20260528T061837"
}
```

</details>

---
