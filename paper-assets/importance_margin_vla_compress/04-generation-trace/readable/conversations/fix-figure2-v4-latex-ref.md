# fix figure2 v4 latex ref

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_fix_figure2_v4_latex_ref_20260528T174620.jsonl`
- **Structured JSON:** [`804794c7a25bfadb8e9c.json`](../../sessions/80/804794c7a25bfadb8e9c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-28T17:47:06.500989+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig_architecture",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig_architecture",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T17:47:06.501345+00:00_

docs/paper/sections/background.tex:17:\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
docs/paper/method.tex:19:\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
docs/paper/background.tex:17:\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T17:47:06.501523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T17:47:06.501677+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{0pt}
20	
21	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{abstract}
27	
28	\keywords{vision-language-action models, token pruning, robot learning}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T17:47:06.501835+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\input.*background",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\input.*background",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T17:47:06.501962+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T17:47:06.502079+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\include.*background",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\include.*background",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T17:47:06.502239+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T17:47:06.502394+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture* 2>/dev/null",
  "description": "List all fig_architecture files to check for symlinks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture* 2>/dev/null",
    "description": "List all fig_architecture files to check for symlinks"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T17:47:06.502543+00:00_

-rw-r--r-- 1 ubuntu ubuntu   57833 May 22 14:21 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture.pdf
-rw-r--r-- 1 ubuntu ubuntu   61759 May 28 16:12 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture_v2.pdf
-rw-r--r-- 1 ubuntu ubuntu  154913 May 28 16:12 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture_v2.png
-rw-r--r-- 1 ubuntu ubuntu 3482734 May 28 16:08 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture_v3.pdf
-rw-r--r-- 1 ubuntu ubuntu 3395585 May 28 16:08 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture_v3.png
-rw-r--r-- 1 ubuntu ubuntu  331488 May 28 16:45 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture_v4.pdf
-rw-r--r-- 1 ubuntu ubuntu 2048851 May 28 16:45 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture_v4.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T17:47:06.502673+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig_architecture",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.log",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig_architecture",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.log",
    "head_limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T17:47:06.502794+00:00_

docs/paper/main.log:553:&lt;figures/paper/fig_architecture_v2.pdf, id=299, 414.8298pt x 245.28438pt>
docs/paper/main.log:554:File: figures/paper/fig_architecture_v2.pdf Graphic file (type pdf)
docs/paper/main.log:555:&lt;use figures/paper/fig_architecture_v2.pdf>
docs/paper/main.log:556:Package pdftex.def Info: figures/paper/fig_architecture_v2.pdf  used on input l
docs/paper/main.log:562: [3 <./figures/paper/fig_architecture_v2.pdf>]) (./experiments.tex [4]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T17:47:06.502949+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log | awk '{print $6, $7, $8}'",
  "description": "Check main.log timestamp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log | awk '{print $6, $7, $8}'",
    "description": "Check main.log timestamp"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T17:47:06.503067+00:00_

May 28 15:56

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T17:47:06.503199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "offset": "15",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "offset": "15",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T17:47:06.503326+00:00_

15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}
21	\label{fig:architecture}
22	\end{figure*}
23	
24	\begin{table}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-28T17:47:06.503496+00:00_

`method.tex:19` already correctly references `fig_architecture_v4.pdf`. The log (from 15:56) is from a prior compilation before the fix was made.

The two `background.tex` files referencing the old `fig_architecture.pdf` are **not included** in the compilation chain (no `\input{background}` or `\input{sections/background}` anywhere). They're dead files.

**Summary:**
- `method.tex:19` — already points to `fig_architecture_v4.pdf` ✓
- `background.tex:17` and `sections/background.tex:17` — reference old version but are **not compiled** (not `\input`'d by any file)
- The `main.log` showing v2 is stale (compiled before the method.tex update)

No changes needed. Recompiling the paper will produce the correct output with v4. If you want, I can also update the two orphan `background.tex` files for consistency, but they don't affect the build.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_figure2_v4_latex_ref_20260528T174620"
}
```

</details>

---
