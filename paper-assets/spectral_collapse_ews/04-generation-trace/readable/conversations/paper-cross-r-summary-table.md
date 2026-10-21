# paper cross r summary table

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_cross-r-summary-table_20260519T183255.jsonl`
- **Structured JSON:** [`df3cb0827baf4cf9c458.json`](../../sessions/df/df3cb0827baf4cf9c458.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-19T18:35:13.406840+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T18:35:13.407180+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T18:35:13.407359+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "spectral_collapse_ews",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "spectral_collapse_ews",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T18:35:13.408049+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_011\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:17:23.434Z\", \"updated_at\": \"2026-05-19T17:43:58.161Z\", \"hypothesis\": \"Extending r=0.2 from 5gen to 10gen will reveal whether the dip-then-recovery pattern (Type II) persists or transitions to sustained decline. If SLV continues rising through Gen 10 (like r=0.25), r=0.2 is firmly Type II. If SLV plateaus or declines after Gen 5, r=0.2 may be closer to the Type I/II boundary, providing finer resolution of the phase diagram near r_crit.\", \"parent\": \"exp_007\", \"spec\": {\"command\": \"bash -c \\\"bash /root/spectral_collapse_ews/scripts/resume_fixed_mix_r02_seed42_gen5to10.sh 0\\\"\", \"server\": \"rtx6000-diagprobe\", \"gpu\": \"cuda:0\", \"pid\": 319889, \"log_path\": \"~/runs/spectral_collapse_ews/exp_011.log\", \"submitted_at\": \"2026-05-19T16:17:48.185Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"description\": \"Phase 1: Resume r=0.2 fixed mix seed 42 from Gen 5 to Gen 10\", \"tmux_session\": \"exp_011\", \"model_name\": \"EleutherAI/pythia-410m-deduped\", \"seed\": 42, \"data_path\": \"/root/spectral_collapse_ews/data/\", \"data_count\": \"50K real pool, total_per_gen=50K (10K real + 40K synthetic per gen)\", \"generations\": \"5→10 (resume)\", \"condition\": \"fixed_mix\", \"real_ratio\": 0.2, \"checkpoint_dir\": \"/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r02_seed42/\", \"results_file\": \"/root/spectral_collapse_ews/results/phase1_fixed_mix_r02_seed42_results.json\", \"checkpoint_source\": \"exp_007 Gen 5 checkpoint\", \"eval_data\": \"/root/spectral_collapse_ews/data/eval_5k.jsonl (5K held-out samples)\"}}, \"exp_009\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:47:07.558Z\", \"updated_at\": \"2026-05-19T16:20:20.579Z\", \"hypothesis\": \"At r=0.25 (25% real data), SLV trajectory will dis
…[truncated 35968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T18:35:13.408261+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T18:35:13.408494+00:00_

1	
2	\subsection{Experimental Setup}
3	\label{subsec:setup}
4	
5	We use Pythia-410M-deduped \citep{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.
6	Starting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.
7	At each generation we compute the spectral indicators from \S\ref{subsec:spectral_metrics} on the Gram matrix of 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.
8	
9	For the mixing comparison (\S\ref{subsec:phase1}), we evaluate three strategies sharing the same total real-data budget:
10	(1)~\textbf{pure collapse} ($r_t{=}0$),
11	(2)~\textbf{fixed mix} ($r_t{=}0.50$), and
12	(3)~\textbf{adaptive} ($k{=}10$, Eq.~\ref{eq:controller}).
13	
14	\subsection{Spectral Collapse Characterization}
15	\label{subsec:phase0}
16	
17	Table~\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.
18	
19	\begin{table}[t]
20	\centering
21	\small
22	\begin{tabular}{@{}rrrrrrc@{}}
23	\toprule
24	Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
25	\midrule
26	0  & 417.55 & 2366.68 &  9.55 & .413 & .741 & 1942.8 \\
27	2  & \textbf{496.44} & \textbf{2469.93} & 13.58 & .376 & .515 &  712.0 \\
28	5  & 479.21 & 2370.17 & 24.59 & .344 & .463 &  741.0 \\
29	7  & 464.20 & 2304.19 & 38.89 & .319 & .447 &  791.3 \\
30	10 & 442.46 & 2178.95 & 76.78 & .295 & .426 &  825.7 \\
31	\bottomrule
32	\end{tabular}
33	\caption{Spectral and downstream metrics at selected generations (Pythia-410M; full trajectory described in text). Bold marks the spectral peak before collapse onset.}
34	\label{tab:phase0}
35	\end{table}
36	
37	\begin{figure}[t]
38	\centering
39	\includegraphics[width=\columnwidth]{figures/spectral_trajectory.pdf}
40	\caption{SLV across 10 recursive generati
…[truncated 11753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T18:35:13.408809+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "old_string": "Below $r_{\\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion over the observed five generations once the transient passes.",
  "new_string": "Below $r_{\\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion over the observed five generations once the transient passes.\nTable~\\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}clrrrrrc@{}}\n\\toprule\n$r$ & Type & SLV & $r_{\\text{eff}}$ & PPL & D-4 & $\\max\\Delta_t$ & Hor. \\\\\n\\midrule\n0    & I   & 2179.0 & 442.5 & 76.78 & .426 & ---   & 10 \\\\\n0.20 & II  & 2398.9$^\\dagger$ & 492.7$^\\dagger$ & 11.83$^\\dagger$ & .438$^\\dagger$ & .0019 & 5$^\\dagger$ \\\\\n0.25 & II  & 2485.0 & 512.5 & 13.29 & .357 & .0003 & 10 \\\\\n0.30 & III & 2511.1 & 521.3 & 13.38 & .342 & 0     & 10 \\\\\n0.50 & III & 2572.2 & 553.8 & 15.10 & .239 & 0     & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Final-generation spectral and downstream metrics across mixing ratios. $^\\dagger$5-generation horizon (exp\\_007); all others run 10 generations. Type classification follows \\S\\ref{subsec:phase_diagram}.}\n\\label{tab:phase_summary}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "old_string": "Below $r_{\\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion over the observed five generations once the transient passes.",
    "new_string": "Below $r_{\\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion over the observed five generations once the transient passes.\nTable~\\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}clrrrrrc@{}}\n\\toprule\n$r$ & Type & SLV & $r_{\\text{eff}}$ & PPL & D-4 & $\\max\\Delta_t$ & Hor. \\\\\n\\midrule\n0    & I   & 2179.0 & 442.5 & 76.78 & .426 & ---   & 10 \\\\\n0.20 & II  & 2398.9$^\\dagger$ & 492.7$^\\dagger$ & 11.83$^\\dagger$ & .438$^\\dagger$ & .0019 & 5$^\\dagger$ \\\\\n0.25 & II  & 2485.0 & 512.5 & 13.29 & .357 & .0003 & 10 \\\\\n0.30 & III & 2511.1 & 521.3 & 13.38 & .342 & 0     & 10 \\\\\n0.50 & III & 2572.2 & 553.8 & 15.10 & .239 & 0     & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Final-generation spectral and downstream metrics across mixing ratios. $^\\dagger$5-generation horizon (exp\\_007); all others run 10 generations. Type classification follows \\S\\ref{subsec:phase_diagram}.}\n\\label{tab:phase_summary}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T18:35:13.409029+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:35:13.409162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "offset": "138"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "offset": "138"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T18:35:13.409308+00:00_

138	At $r{=}0.3$, SLV expands monotonically from Gen~2 to 2511.1 at Gen~10 ($+$6.1\% above baseline), with sustained positive growth across all eight post-transient generations.
139	This confirms $r{=}0.3 \geq r_{\text{crit}}$ over the full 10-generation horizon, tightening the bound to $0.25 < r_{\text{crit}} \leq 0.3$.
140	
141	The largest single-generation SLV drop in the first two generations shrinks with $r$: $-9.2$ at $r{=}0.2$ (Gen~1$\to$2), $-4.6$ at $r{=}0.25$ (Gen~0$\to$1), and $-0.6$ at $r{=}0.3$ (Gen~0$\to$1), consistent with a continuous crossover rather than a sharp boundary.
142	The Type~II trajectory clarifies what $r_{\text{crit}}$ marks in practice: not a boundary between collapse and stability in final outcome, but a transition in trajectory shape.
143	Below $r_{\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion over the observed five generations once the transient passes.
144	Table~\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\begin{tabular}{@{}clrrrrrc@{}}
150	\toprule
151	$r$ & Type & SLV & $r_{\text{eff}}$ & PPL & D-4 & $\max\Delta_t$ & Hor. \\
152	\midrule
153	0    & I   & 2179.0 & 442.5 & 76.78 & .426 & ---   & 10 \\
154	0.20 & II  & 2398.9$^\dagger$ & 492.7$^\dagger$ & 11.83$^\dagger$ & .438$^\dagger$ & .0019 & 5$^\dagger$ \\
155	0.25 & II  & 2485.0 & 512.5 & 13.29 & .357 & .0003 & 10 \\
156	0.30 & III & 2511.1 & 521.3 & 13.38 & .342 & 0     & 10 \\
157	0.50 & III & 2572.2 & 553.8 & 15.10 & .239 & 0     & 10 \\
158	\bottomrule
159	\end{tabular}
160	\caption{Final-generation spectral and downstream metrics across mixing ratios. $^\dagger$5-generation horizon (exp\_007); all others run 10 generations. Type classification follows \S\ref{subsec:phase_diagram}.}
161	\label{tab:phase_summary}
162	\end{table}
163	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cross-r-summary-table_20260519T183255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T18:35:13.409480+00:00_

Table inserted at the end of §4.5 with a reference sentence at line 144. All values sourced from registry: exp_001 (r=0), exp_007 (r=0.2, 5gen†), exp_009 (r=0.25), exp_008 (r=0.3), exp_006 (r=0.5). The r=0.5 row uses exp_006 data (adaptive controller that never triggered), consistent with existing §4.4 text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_cross-r-summary-table_20260519T183255"
}
```

</details>

---
