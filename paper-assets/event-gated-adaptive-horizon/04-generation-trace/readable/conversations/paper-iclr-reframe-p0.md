# paper iclr reframe p0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_iclr-reframe-p0_20260528T233554.jsonl`
- **Structured JSON:** [`a6c7210b1512c11e537c.json`](../../sessions/a6/a6c7210b1512c11e537c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-28T23:37:10.588753+00:00_

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
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T23:37:10.589184+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding (a learned vector concatenated to the RSSM input at each imagination step; our implementation of $\dt$-conditioning) and multi-rate data exposure as the strongest predictor. This combination enables environment-dependent pathologies---a $1.63\times$ reward prediction gap in Walker Walk, or dynamics-model prior drift without measurable reward bias in Cheetah Run---which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 2.0\times$ achieves perfect classification ($n{=}36$; AUROC${=}1.000$, F1${=}1.000$; Appendix~\ref{sec:appendix_sensitivity}).
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/paper/fig4_mechanism_diagram
…[truncated 2397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T23:37:10.589519+00:00_

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
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T23:37:10.589693+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify the combination of trained temporal embedding and multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; $n{=}36$, AUROC${=}1.000$ [95\% bootstrap CI: 1.000--1.000], F1${=}1.000$). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. Gradient, output, and representation interventions fail to eliminate CIVO; at the architecture level, dual critics converge in pure imagination ($\rho > 0.999$), but wide dual-critic (min-aggregation $+$ increased capacity) achieves 3/4 prevention---the only partial success, whose mechanism requires further study.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T23:37:10.589884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T23:37:10.590086+00:00_

1	\documentclass{article}
2	
3	% xcolor with table option must be loaded before corl_2026.sty (which loads color internally)
4	\usepackage[table]{xcolor}
5	
6	\usepackage{corl_2026} % CoRL 2026 submission (anonymous)
7	
8	\usepackage[utf8]{inputenc}
9	\usepackage[T1]{fontenc}
10	\usepackage{amsmath,amssymb}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{graphicx}
14	\graphicspath{{../../artifacts/}}
15	\usepackage{colortbl}
16	\usepackage{caption}
17	\usepackage{subcaption}
18	\usepackage{array}
19	\usepackage{enumitem}
20	\usepackage{wrapfig}
21	\usepackage{algorithm}
22	\usepackage{algorithmic}
23	
24	% Custom commands
25	\newcommand{\dt}{\mathrm{dt}}
26	\newcommand{\nve}{\mathrm{nve}}
27	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
28	\newcommand{\sgseval}{448.3}
29	\newcommand{\sgsnve}{1.66}
30	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
31	\usepackage{pifont}
32	\newcommand{\cmark}{\ding{51}}
33	\newcommand{\xmark}{\ding{55}}
34	\newcommand{\ie}{\textit{i.e.}}
35	\newcommand{\eg}{\textit{e.g.}}
36	\newcommand{\cf}{\textit{cf.}}
37	\newcommand{\etal}{\textit{et al.}}
38	
39	\title{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
40	A Diagnostic Analysis of Variable-Rate DreamerV3}
41	
42	\author{
43	  Anonymous Authors\\
44	  Anonymous Institution\\
45	  \texttt{anon@anon.edu}
46	}
47	
48	\begin{document}
49	\maketitle
50	
51	\begin{abstract}
52	\input{sections/abstract_body}
53	\end{abstract}
54	
55	\keywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
56	
57	% --- INTRODUCTION ---
58	\input{sections/introduction}
59	
60	% --- RELATED WORK ---
61	\input{sections/related_work}
62	
63	% --- EXPERIMENTS AND RESULTS (merged) ---
64	\input{sections/experiments_results}
65	
66	% --- ANALYSIS ---
67	\input{sections/analysis}
68	
69	% --- CONCLUSION ---
70	\input{sections/conclusion}
…[truncated 127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T23:37:10.590317+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "old_string": "World-model reinforcement learning enables sample-efficient learning directly on physical hardware \\citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\\dt$ mismatches between simulation and hardware.",
  "new_string": "World-model reinforcement learning enables sample-efficient learning in complex continuous control tasks \\citep{wu2023daydreamer, hansen2024tdmpc2}. Continuous control demands temporal abstraction: locomotion with heterogeneous gait phases, contact-rich tasks with variable sensing rates, and multi-rate decision-making across planning horizons all require handling $\\dt$ mismatches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "old_string": "World-model reinforcement learning enables sample-efficient learning directly on physical hardware \\citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\\dt$ mismatches between simulation and hardware.",
    "new_string": "World-model reinforcement learning enables sample-efficient learning in complex continuous control tasks \\citep{wu2023daydreamer, hansen2024tdmpc2}. Continuous control demands temporal abstraction: locomotion with heterogeneous gait phases, contact-rich tasks with variable sensing rates, and multi-rate decision-making across planning horizons all require handling $\\dt$ mismatches."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T23:37:10.590496+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T23:37:10.590637+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "old_string": "As world-model RL moves toward real systems with variable-rate sensing, understanding when temporal conditioning fails is essential for safe deployment.",
  "new_string": "As world-model RL incorporates variable-rate decision-making, understanding when temporal conditioning fails is essential for the architectural design of variable-rate model-based RL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "old_string": "As world-model RL moves toward real systems with variable-rate sensing, understanding when temporal conditioning fails is essential for safe deployment.",
    "new_string": "As world-model RL incorporates variable-rate decision-making, understanding when temporal conditioning fails is essential for the architectural design of variable-rate model-based RL."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T23:37:10.590793+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T23:37:10.590942+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex",
  "old_string": "World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales.",
  "new_string": "World-model reinforcement learning increasingly targets continuous control tasks where temporal abstraction enables planning across heterogeneous time scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex",
    "old_string": "World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales.",
    "new_string": "World-model reinforcement learning increasingly targets continuous control tasks where temporal abstraction enables planning across heterogeneous time scales."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T23:37:10.591082+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T23:37:10.591204+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex",
  "old_string": "the only partial success, whose mechanism requires further study.",
  "new_string": "the only partial success, highlighting open challenges in the architectural design of variable-rate model-based RL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex",
    "old_string": "the only partial success, whose mechanism requires further study.",
    "new_string": "the only partial success, highlighting open challenges in the architectural design of variable-rate model-based RL."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T23:37:10.591340+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T23:37:10.591476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX to check for errors",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
    "description": "Compile LaTeX to check for errors",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T23:37:10.591612+00:00_

LaTeX Warning: `h' float specifier changed to `ht'.

) [33] [34] [35] [36] [37] [38] [39] [40] [41] [42] (./main.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt0900.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uh
vr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/zapfding/uzdr.pfb>
Output wr
…[truncated 76 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-28T23:37:10.591804+00:00_

编译成功，42页，无错误。

### Diff 汇总

**introduction.tex** (2处)：
1. 第1句：`directly on physical hardware` → `in complex continuous control tasks`
2. 第2句整句重写：删除 `Real robotic tasks` / `manipulation requires fast reactive grasping` / `sim-to-real transfer`，替换为 `Continuous control demands temporal abstraction: locomotion with heterogeneous gait phases, contact-rich tasks with variable sensing rates, and multi-rate decision-making across planning horizons all require handling $\dt$ mismatches.`
3. 末段尾句：`As world-model RL moves toward real systems with variable-rate sensing, understanding when temporal conditioning fails is essential for safe deployment.` → `...incorporates variable-rate decision-making...essential for the architectural design of variable-rate model-based RL.`

**abstract_body.tex** (2处)：
1. 首句：`increasingly deployed for robot control, where temporal abstraction` → `increasingly targets continuous control tasks where temporal abstraction`
2. 尾句：`whose mechanism requires further study` → `highlighting open challenges in the architectural design of variable-rate model-based RL`

**main.tex**：Keywords 无需修改，已无 robotics 措辞。`DreamerV3` 保留。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_iclr-reframe-p0_20260528T233554"
}
```

</details>

---
