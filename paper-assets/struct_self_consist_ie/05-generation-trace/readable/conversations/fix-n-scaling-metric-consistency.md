# fix n scaling metric consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 95
- **Recorded user turns:** 0
- **Tool calls:** 47
- **Original source:** `logs/chats/worker_fix_n_scaling_metric_consistency_20260516T154206.jsonl`
- **Structured JSON:** [`79a29594d1bc7501444a.json`](../../sessions/79/79a29594d1bc7501444a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

95 recorded events

### Tool call

_source line 1 · 2026-05-16T15:53:22.091487+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T15:53:22.091914+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T15:53:22.092111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/docs/paper/sections -name \"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/docs/paper/sections -name \"*.tex\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T15:53:22.092341+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/struct_self_consist_ie/docs/paper/sections': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T15:53:22.092484+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.tex\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.tex\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T15:53:22.092617+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_tables.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T15:53:22.092771+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T15:53:22.092926+00:00_

artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T092241/best/paper.tex
artifacts/dream_reports/dream_20260516T092241/median/paper.tex
artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
docs/paper/sections/limitations.tex
artifacts/dream_reports/dream_20260516T113255/best/paper.tex
artifacts/dream_reports/dream_20260516T113255/median/paper.tex
artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
docs/paper/main.tex
docs/paper/sections/method.tex
docs/paper/sections/abstract.tex
docs/paper/sections/introduction.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work.tex
docs/paper/sections/conclusion.tex
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T15:53:22.093115+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "n_scaling|N-scaling|n.scaling",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "tool_args": {
    "pattern": "n_scaling|N-scaling|n.scaling",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T15:53:22.093295+00:00_

docs/paper/sections/experiments.tex:16:We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
docs/paper/sections/limitations.tex:5:We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
docs/paper/sections/discussion.tex:62:Increasing $N$ from 2 to 32 expands oracle headroom sixfold ($+3.3$ to ${\sim}{+}20$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom exceeds 20~pp---the best signal captures less than 5\% of the available improvement (Table~\ref{tab:n_scaling_selection}).
docs/paper/sections/discussion.tex:106:For quality estimation---where signals are already reliable ($\rho$ up to 0.45 on CoNLL, 0.42 on the primary test bed; AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.
docs/paper/sections/discussion.tex:113:Effective selection thus requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers, venktesh2025trust}, not confidence signal aggregation; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
docs/paper/sections/appendix.tex:833:\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
docs/paper/sections/appendix.tex:835:Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
docs/paper/sections/appendix.tex:840:\label{tab:n-scaling}
docs/paper/sections/appendix.tex:903:Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degen
…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T15:53:22.093445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "833",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "833",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T15:53:22.093617+00:00_

833	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
834	
835	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
836	
837	\begin{table}[t]
838	\centering
839	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
840	\label{tab:n-scaling}
841	\small
842	\begin{tabular}{l ccc ccc}
843	\toprule
844	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
845	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
846	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
847	\midrule
848	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
849	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
850	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
851	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
852	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
853	\midrule
854	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
855	\bottomrule
856	\end{tabular}
857	\end{table}
858	
859	\begin{table}[t]
860	\centering
861	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
862	\label{tab:ranking-stability}
863	\small
864	\begin{tabular}{ll cc l}
865	\toprule
866	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
867	\midrule
868	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
869	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
870	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
871	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
872	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
873	\bottomrule
874	\end{tabular}
875	\end{table}
876	
877	\begin{table}[t]
878	\centering
879	\caption{Cross-seed standard deviation ($\sigma$) of S
…[truncated 3803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T15:53:22.093828+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "tab:selection|Table 2|greedy|0\\\\.64",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "tool_args": {
    "pattern": "tab:selection|Table 2|greedy|0\\\\.64",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T15:53:22.093978+00:00_

80:\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$, $p$ vs.\ greedy baseline from paired sign tests). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Random: uniform random selection from $N$ candidates. Non-tied LP subset analysis in \S\ref{sec:discussion}; RE selection in Appendix~\ref{app:re_extension}.}
81:\label{tab:selection}
103:Despite moderate quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
104:Instance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none improves over the greedy baseline.
107:\paragraph{No significant improvement over greedy.}
108:On SciERC NER (2-seed sign tests\footnote{Multi-seed NER experiments confirm seed variation is small ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
112:LP approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3~pp gap).
141:Repeating with Qwen3-4B (Table~\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the g
…[truncated 312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T15:53:22.094144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "80",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "80",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T15:53:22.094293+00:00_

80	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$, $p$ vs.\ greedy baseline from paired sign tests). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Random: uniform random selection from $N$ candidates. Non-tied LP subset analysis in \S\ref{sec:discussion}; RE selection in Appendix~\ref{app:re_extension}.}
81	\label{tab:selection}
82	\begin{tabular}{lcc}
83	\toprule
84	Method & NER F1 & $p$ \\
85	\midrule
86	Oracle & $0.778 \pm 0.003$ & --- \\
87	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
88	\midrule
89	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
90	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
91	\midrule
92	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
93	SJ           & $0.646 \pm 0.002$ & .67 \\
94	FK           & $0.646 \pm 0.001$ & .79 \\
95	EM           & $0.637 \pm 0.001$ & --- \\
96	VC           & $0.623 \pm 0.004$ & --- \\
97	\midrule
98	Random           & $0.610 \pm 0.003$ & --- \\
99	\bottomrule
100	\end{tabular}
101	\end{table}
102	
103	Despite moderate quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
104	Instance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none improves over the greedy baseline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T15:53:22.094472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_scaling_appendix_tables.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_scaling_appendix_tables.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T15:53:22.094628+00:00_

1	% N-scaling appendix tables for Structured Self-Consistency paper
2	% Requires: booktabs package
3	
4	%%% Table 1: N=8 vs N=16 Comparison (Spearman ρ)
5	\begin{table}[t]
6	\centering
7	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
8	\label{tab:n-scaling}
9	\small
10	\begin{tabular}{l ccc ccc}
11	\toprule
12	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
13	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
14	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
15	\midrule
16	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
17	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
18	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
19	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
20	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
21	\midrule
22	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	%%% Table 2: Cross-seed Signal Ranking Stability (Kendall's W)
28	\begin{table}[t]
29	\centering
30	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
31	\label{tab:ranking-stability}
32	\small
33	\begin{tabular}{ll cc l}
34	\toprule
35	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
36	\midrule
37	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
38	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
39	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
40	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
41	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	%%% Table 3: Per-signal Cross-seed σ Comparison
47	\begin{table}[t]
48	\centering
49	\caption{Cross-seed standard deviation ($\sigma
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T15:53:22.094812+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*n_scaling*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*n_scaling*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T15:53:22.094947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T15:53:22.095071+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*selection*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*selection*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T15:53:22.095280+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp016_signal_ensemble/selection_f1_comparison.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp016_signal_ensemble/selection_f1_full.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp010_selection_curves/figures/fig_selection_curves.pdf\\n/root/autodl-tmp/struct_self_consist_ie/output/exp010_selection_curves/figures/fig_selection_curves.png\\n/root/autodl-tmp/struct_self_consist_ie/output/exp010_selection_curves/plot_selection_curves.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2/selection_f1_comparison.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/selection_f1_comparison.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/selection_f1_full.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/run_selection_f1.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_scierc_n8.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_scierc_n16.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_qwen_conll_n8.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_conll_n8.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_4configs_summary.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_bootstrap.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_bootstrap.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_reconcile.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/recompute_re_selection.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_recompute.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_stratified_selection.json\\n/root/autodl-tmp/struct_self_consist_ie/output
…[truncated 1400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T15:53:22.095436+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*n_scaling*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*n_scaling*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T15:53:22.095573+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T15:53:22.095697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -path \"*n_scaling*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie -path \"*n_scaling*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T15:53:22.095820+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T15:53:22.095937+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_table2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_table2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T15:53:22.096152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"seeds\\\": [\\n    42,\\n    123\\n  ],\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"methods\\\": {\\n    \\\"Greedy\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6439219990259687,\\n        \\\"123\\\": 0.6457455273145254\\n      },\\n      \\\"mean\\\": 0.644833763170247,\\n      \\\"std\\\": 0.00128942921852394\\n    },\\n    \\\"Random\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6077394535406134,\\n        \\\"123\\\": 0.6125472312176403\\n      },\\n      \\\"mean\\\": 0.6101433423791269,\\n      \\\"std\\\": 0.0033996121978630226,\\n      \\\"delta_vs_greedy\\\": -0.03469042079112006\\n    },\\n    \\\"LP\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6500718843902431,\\n        \\\"123\\\": 0.6436180382499742\\n      },\\n      \\\"mean\\\": 0.6468449613201086,\\n      \\\"std\\\": 0.00456355837051876,\\n      \\\"delta_vs_greedy\\\": 0.002011198149861615,\\n      \\\"per_seed_p\\\": {\\n        \\\"42\\\": 0.5425074179193997,\\n        \\\"123\\\": 0.15233780606025285\\n      },\\n      \\\"combined_p\\\": 0.28869407141823045,\\n      \\\"per_seed_wins\\\": {\\n        \\\"42\\\": 62,\\n        \\\"123\\\": 47\\n      },\\n      \\\"per_seed_losses\\\": {\\n        \\\"42\\\": 70,\\n        \\\"123\\\": 63\\n      },\\n      \\\"per_seed_ties\\\": {\\n        \\\"42\\\": 398,\\n        \\\"123\\\": 419\\n      }\\n    },\\n    \\\"SJ\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6450050009215592,\\n        \\\"123\\\": 0.6474774323740186\\n      },\\n      \\\"mean\\\": 0.6462412166477889,\\n      \\\"std\\\": 0.0017482730460529079,\\n      \\\"delta_vs_greedy\\\": 0.0014074534775418979,\\n      \\\"per_seed_p\\\": {\\n        \\\"42\\\": 0.5657001139736343,\\n        \\\"123\\\": 0.5507089135982713\\n      },\\n      \\\"combined_p\\\": 0.6748619732918099,\\n      \\\"per_seed_wins\\\": {\\n        \\\"42\\\": 58,\\n        \\\"123\\\": 54\\n 
…[truncated 2895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T15:53:22.096421+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*scaling*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*scaling*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T15:53:22.096595+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T15:53:22.096725+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*.json\" -path \"*review_round*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*.json\" -path \"*review_round*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T15:53:22.096887+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/review_round2/wnut17_full_signal_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_scierc_n8.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_scierc_n16.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_qwen_conll_n8.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_conll_n8.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_4configs_summary.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/n8_bootstrap_ci.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_bootstrap.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/sj_threshold_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_recompute.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/wnut_zero_f1_verify.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_conditional_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/em_exact_match_freq.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/fk_independence_test.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_stratified_selection.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/vc_implementation_diff.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/oracle_improvable_fraction.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/tost_equivalence.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/oracle_improvable_tost.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/qwen_scierc_3seed_summary.json\\n/root/aut
…[truncated 3159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T15:53:22.097042+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*exp013*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*exp013*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T15:53:22.097220+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T15:53:22.097374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*subsamp*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*subsamp*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T15:53:22.097503+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T15:53:22.097622+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T15:53:22.097789+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_epsilon_sweep\\nanalysis_fk_bootstrap_ci.json\\nanalysis_fk_bootstrap_per_instance.json\\nanalysis_lp_range_cdf.json\\nanalysis_lp_range_cdf_n16_3seed.json\\nanalysis_multiseed_selection_f1.json\\nanalysis_round8\\nanalysis_scierc_n16_3seed_selection_f1.json\\nanalysis_scierc_n16_3seed_selection_f1_merged.json\\nanalysis_scierc_re_n16_3seed_selection_f1.json\\nanalysis_unified_rho_full.json\\nbootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\nconditional_filter_diagnosis.json\\nd108_greedy_f1\\nd108_lp_vc_combination\\nd108_mbr_within_rho\\nd108_q4q5\\nd110_4b_degeneracy\\nd112_disk_cleanup\\nd112_hybrid_strategy\\nd112_mf3_random_single\\nd112_table2_fix\\nd114_auroc_investigation\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp018_3seed_5signal_results.json\\nexp_001_seed123_v2\\nexp_001_seed123_v2_r1024\\nexp_001_seed42_v2\\nexp_001_seed42_v2_r1024\\nexp_001_seed456_v2\\nexp_001_seed456_v2_ner\\nexp_001_seed456_v2_ner.log\\nexp_001_seed456_v2_ner_r1024\\nexp_002_conll_n16\\nexp_002_conll_n16.log\\nexp_002_conll_n16_r1024\\nexp_003_wnut17_v2_infer\\nexp_005_v2_temperature\\nexp_006_v2\\nexp_006_v2_run.lo
…[truncated 2610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T15:53:22.097954+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T15:53:22.098087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"n_ablation.py\\nn_ablation_fixed.py\\nresults.json\\nresults_fixed.json\\ntable.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T15:53:22.098236+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results_fixed.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results_fixed.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T15:53:22.098472+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"rank32_N2\\\": {\\n    \\\"regime\\\": \\\"rank32\\\",\\n    \\\"N\\\": 2,\\n    \\\"greedy_f1\\\": 0.6650674662668666,\\n    \\\"oracle_f1\\\": 0.6996110264329252,\\n    \\\"oracle_gap\\\": 0.03454356016605853,\\n    \\\"degeneracy\\\": 0.42892249527410203,\\n    \\\"lp_range\\\": 0.011278706911152854,\\n    \\\"selection_f1\\\": {\\n      \\\"LP\\\": 0.6495358680764369,\\n      \\\"SJ\\\": 0.6322339450939927,\\n      \\\"FK\\\": 0.6322339450939927,\\n      \\\"EM\\\": 0.6322339450939927,\\n      \\\"VC\\\": 0.6255636533635056\\n    },\\n    \\\"deltas\\\": {\\n      \\\"LP\\\": -0.015531598190429707,\\n      \\\"SJ\\\": -0.03283352117287397,\\n      \\\"FK\\\": -0.03283352117287397,\\n      \\\"EM\\\": -0.03283352117287397,\\n      \\\"VC\\\": -0.039503812903361024\\n    },\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta\\\": -0.015531598190429707\\n  },\\n  \\\"rank32_N4\\\": {\\n    \\\"regime\\\": \\\"rank32\\\",\\n    \\\"N\\\": 4,\\n    \\\"greedy_f1\\\": 0.6650674662668666,\\n    \\\"oracle_f1\\\": 0.7496934866525413,\\n    \\\"oracle_gap\\\": 0.08462602038567468,\\n    \\\"degeneracy\\\": 0.22249527410207942,\\n    \\\"lp_range\\\": 0.025825508153027577,\\n    \\\"selection_f1\\\": {\\n      \\\"LP\\\": 0.6620436372213201,\\n      \\\"SJ\\\": 0.6527894637458281,\\n      \\\"FK\\\": 0.6524839863661807,\\n      \\\"EM\\\": 0.6463706821823887,\\n      \\\"VC\\\": 0.6324699742312337\\n    },\\n    \\\"deltas\\\": {\\n      \\\"LP\\\": -0.0030238290455465444,\\n      \\\"SJ\\\": -0.0122780025210385,\\n      \\\"FK\\\": -0.012583479900685979,\\n      \\\"EM\\\": -0.018696784084477946,\\n      \\\"VC\\\": -0.03259749203563289\\n    },\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta\\\": -0.0030238290455465444\\n  },\\n  \\\"rank32_N8\\\": {\\n    \\\"regime\\\": \\\"rank32\\\",\\n    \\\"N\\\": 8,\\n    \\\"greedy_f1\\\": 0.6650674662668666,\\n    \\\"oracle_f1\\\": 0.7868490
…[truncated 5255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T15:53:22.098673+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/table.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/table.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T15:53:22.098825+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"| Regime | N | Degeneracy% | LP_range | Oracle_F1 | Greedy_F1 | Oracle_gap | LP_Δ | SJ_Δ | FK_Δ | EM_Δ | VC_Δ | Best_Δ |\\n|--------|---|-------------|----------|-----------|-----------|------------|------|------|------|------|------|--------|\\n| rank32 | 2 | 53.0±1.6 | 0.0113 | 0.6846 | 0.6442 | 0.0404 | -1.67 | -3.68 | -3.68 | -3.68 | -3.60 | -1.67 |\\n| rank32 | 4 | 30.7±1.2 | 0.0258 | 0.7412 | 0.6442 | 0.0970 | -0.30 | -1.53 | -1.54 | -2.22 | -2.80 | -0.30 |\\n| rank32 | 8 | 18.7±0.9 | 0.0408 | 0.7836 | 0.6442 | 0.1394 | +0.15 | -0.57 | -0.61 | -1.44 | -3.19 | +0.15 |\\n| rank32 | 16 | 11.5 | 0.0536 | 0.8194 | 0.6442 | 0.1752 | +0.23 | +0.20 | +0.27 | -1.30 | -3.46 | +0.27 |\\n| rank8 | 2 | 38.2±1.9 | 0.0164 | 0.6617 | 0.6397 | 0.0220 | -4.48 | -8.32 | -8.32 | -8.32 | -8.25 | -4.48 |\\n| rank8 | 4 | 15.7±0.9 | 0.0379 | 0.7431 | 0.6397 | 0.1034 | -2.22 | -3.10 | -3.26 | -6.11 | -5.10 | -2.22 |\\n| rank8 | 8 | 7.2 | 0.0564 | 0.7998 | 0.6397 | 0.1601 | -0.47 | -0.91 | -1.33 | -3.24 | -4.79 | -0.47 |\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T15:53:22.098967+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T15:53:22.099405+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"rank32\\\": {\\n    \\\"N=2\\\": {\\n      \\\"mean\\\": {\\n        \\\"greedy_f1\\\": 0.6441821796820129,\\n        \\\"oracle_f1\\\": 0.6845551755650915,\\n        \\\"degeneracy_rate\\\": 0.5302457466918714,\\n        \\\"lp_range_median\\\": 0.011278706911152854,\\n        \\\"oracle_gap\\\": 0.04037299588307862,\\n        \\\"best_signal_f1\\\": 0.6275034484445567,\\n        \\\"selection_f1\\\": {\\n          \\\"LP\\\": 0.6275034484445567,\\n          \\\"SJ\\\": 0.607403005083387,\\n          \\\"FK\\\": 0.607403005083387,\\n          \\\"EM\\\": 0.607403005083387,\\n          \\\"VC\\\": 0.6081526893879273\\n        },\\n        \\\"best_signal\\\": \\\"LP\\\"\\n      },\\n      \\\"std\\\": {\\n        \\\"greedy_f1\\\": 0.0,\\n        \\\"oracle_f1\\\": 0.005527700692701951,\\n        \\\"degeneracy_rate\\\": 0.016001195276982596,\\n        \\\"lp_range_median\\\": 0.0007464926004543067,\\n        \\\"oracle_gap\\\": 0.005527700692701951,\\n        \\\"best_signal_f1\\\": 0.005999858204705868,\\n        \\\"selection_f1\\\": {\\n          \\\"LP\\\": 0.005999858204705868,\\n          \\\"SJ\\\": 0.005682995405252551,\\n          \\\"FK\\\": 0.005682995405252551,\\n          \\\"EM\\\": 0.005682995405252551,\\n          \\\"VC\\\": 0.005191992480575876\\n        }\\n      },\\n      \\\"n_repeats\\\": 10\\n    },\\n    \\\"N=4\\\": {\\n      \\\"mean\\\": {\\n        \\\"greedy_f1\\\": 0.6441821796820129,\\n        \\\"oracle_f1\\\": 0.7412045358092041,\\n        \\\"degeneracy_rate\\\": 0.3073724007561437,\\n        \\\"lp_range_median\\\": 0.025825508153027577,\\n        \\\"oracle_gap\\\": 0.09702235612719132,\\n        \\\"best_signal_f1\\\": 0.6411523503121113,\\n        \\\"selection_f1\\\": {\\n          \\\"LP\\\": 0.6411523503121113,\\n          \\\"SJ\\\": 0.6288426795309807,\\n          \\\"FK\\\": 0.6287628129577303,\\n          \\\"EM\\\": 0.6220221284387495,\\n          \\\"VC
…[truncated 8079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T15:53:22.099664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation_fixed.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation_fixed.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T15:53:22.099906+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fixed N-ablation analysis.\\n\\nBug fixes vs original:\\n1. Uses inst[\\\"greedy\\\"] field (actual greedy decoding), not samples[0]\\n2. Computes micro F1 (aggregate TP/FP/FN), not macro (mean per-instance F1)\\n3. Filters instances with empty gold entities (standard practice)\\n4. N=32 uses same methodology as N=2/4/8/16\\n\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport numpy as np\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import _ner_soft_jaccard_pair, _extract_surface_keys\\nfrom evaluation import per_instance_f1, entity_strict_match\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nOUT_DIR = f\\\"{BASE}/output/exp_025_n_ablation\\\"\\nSUBTASK = \\\"ner\\\"\\nSIGNALS = [\\\"LP\\\", \\\"SJ\\\", \\\"FK\\\", \\\"EM\\\", \\\"VC\\\"]\\nN_REPEATS = 10\\n\\nCONFIGS = [\\n    (\\\"rank32\\\", f\\\"{BASE}/output/exp_001_seed42_v2/samples.jsonl\\\", 16, [2, 4, 8, 16]),\\n    (\\\"rank32\\\", f\\\"{BASE}/output/exp_025_n32/samples.jsonl\\\", 32, [32]),\\n    (\\\"rank8\\\", f\\\"{BASE}/output/exp_023_rank8_inference/samples.jsonl\\\", 8, [2, 4, 8]),\\n]\\n\\n\\ndef compute_signals(samples):\\n    N = len(samples)\\n    lp_scores = []\\n    for s in samples:\\n        lp = s.get(\\\"mean_logprob\\\")\\n        if lp is None:\\n            lp = s.get(\\\"cumulative_logprob\\\", -999) / max(s.get(\\\"n_tokens\\\", 1), 1)\\n        lp_scores.append(lp)\\n\\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\\n\\n    # FK: pairwise surface Jaccard\\n    fk_matrix = np.zeros((N, N))\\n    for i in range(N):\\n        for j in range(i + 1, N):\\n            union = len(key_sets[i] | key_sets[j])\\n            inter = len(key_sets[i] & key_sets[j])\\n            s = inter / union if union > 0 else 1.0\\n            fk_matrix[i][j] = s\\n            fk_matrix[j][i] 
…[truncated 6782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T15:53:22.100107+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T15:53:22.100411+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"N ablation via random subsampling from existing N=16 / N=8 data.\\n\\nFor each target N, subsample 10 random seeds, recompute pairwise signals\\n(SJ, FK, EM, VC) on subset, select top-1 per signal, compute F1 vs gold.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport os\\nimport numpy as np\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import _ner_soft_jaccard_pair, _extract_surface_keys\\nfrom evaluation import per_instance_f1\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nOUT_DIR = f\\\"{BASE}/output/exp_025_n_ablation\\\"\\n\\nCONFIGS = {\\n    \\\"rank32\\\": {\\n        \\\"path\\\": f\\\"{BASE}/output/exp_001_seed42_v2/samples.jsonl\\\",\\n        \\\"source_N\\\": 16,\\n        \\\"target_Ns\\\": [2, 4, 8, 16],\\n    },\\n    \\\"rank8\\\": {\\n        \\\"path\\\": f\\\"{BASE}/output/exp_023_rank8_inference/samples.jsonl\\\",\\n        \\\"source_N\\\": 8,\\n        \\\"target_Ns\\\": [2, 4, 8],\\n    },\\n}\\n\\nN_REPEATS = 10\\nSUBTASK = \\\"ner\\\"\\nSIGNALS = [\\\"LP\\\", \\\"SJ\\\", \\\"FK\\\", \\\"EM\\\", \\\"VC\\\"]\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef compute_signals_for_subset(samples):\\n    \\\"\\\"\\\"Compute all 5 signal scores for a subset of samples.\\\"\\\"\\\"\\n    N = len(samples)\\n    \\n    # LP: per-sample, no recomputation needed\\n    lp_scores = []\\n    for s in samples:\\n        lp = s.get(\\\"mean_logprob\\\")\\n        if lp is None:\\n            lp = s.get(\\\"cumulative_logprob\\\", -999) / max(s.get(\\\"n_tokens\\\", 1), 1)\\n        lp_scores.append(lp)\\n    \\n    # Surface key sets (for FK, VC, EM)\\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\\n    \\n    # FK: pairwise surface Jaccard\\n    fk_matrix
…[truncated 7190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T15:53:22.100683+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T15:53:22.100833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"llama_conll_result.json\\nresults.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T15:53:22.100967+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T15:53:22.101313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Qwen_CoNLL\\\": {\\n    \\\"n_instances\\\": 2756,\\n    \\\"n8_samples_per_inst\\\": 8,\\n    \\\"n16_samples_per_inst\\\": 16,\\n    \\\"actual_n8_vs_n16\\\": {\\n      \\\"SJ\\\": {\\n        \\\"rho_n16\\\": 0.4496,\\n        \\\"rho_n8\\\": 0.4389,\\n        \\\"delta_rho_point\\\": 0.0107,\\n        \\\"delta_rho_mean\\\": 0.0107,\\n        \\\"ci_95_lo\\\": -0.0138,\\n        \\\"ci_95_hi\\\": 0.0353,\\n        \\\"p_positive\\\": 0.7987,\\n        \\\"n_valid_bootstrap\\\": 10000\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho_n16\\\": 0.3928,\\n        \\\"rho_n8\\\": 0.4038,\\n        \\\"delta_rho_point\\\": -0.011,\\n        \\\"delta_rho_mean\\\": -0.0111,\\n        \\\"ci_95_lo\\\": -0.0409,\\n        \\\"ci_95_hi\\\": 0.0189,\\n        \\\"p_positive\\\": 0.2365,\\n        \\\"n_valid_bootstrap\\\": 10000\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho_n16\\\": 0.4612,\\n        \\\"rho_n8\\\": 0.4523,\\n        \\\"delta_rho_point\\\": 0.0089,\\n        \\\"delta_rho_mean\\\": 0.0088,\\n        \\\"ci_95_lo\\\": -0.0146,\\n        \\\"ci_95_hi\\\": 0.0323,\\n        \\\"p_positive\\\": 0.775,\\n        \\\"n_valid_bootstrap\\\": 10000\\n      },\\n      \\\"voting_conf\\\": {\\n        \\\"rho_n16\\\": 0.4286,\\n        \\\"rho_n8\\\": 0.4277,\\n        \\\"delta_rho_point\\\": 0.0009,\\n        \\\"delta_rho_mean\\\": 0.0007,\\n        \\\"ci_95_lo\\\": -0.0245,\\n        \\\"ci_95_hi\\\": 0.0265,\\n        \\\"p_positive\\\": 0.5208,\\n        \\\"n_valid_bootstrap\\\": 10000\\n      },\\n      \\\"logprob\\\": {\\n        \\\"rho_n16\\\": 0.3146,\\n        \\\"rho_n8\\\": 0.3158,\\n        \\\"delta_rho_point\\\": -0.0011,\\n        \\\"delta_rho_mean\\\": -0.0012,\\n        \\\"ci_95_lo\\\": -0.0145,\\n        \\\"ci_95_hi\\\": 0.0117,\\n        \\\"p_positive\\\": 0.4329,\\n        \\\"n_valid_bootstrap\\\": 10000\\n      }\\n    },\\n    \\\"paired_first8_vs_full16\\\": {\\
…[truncated 8414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T15:53:22.101513+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*n_scaling_selection*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*n_scaling_selection*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T15:53:22.101652+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T15:53:22.101783+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*exp_025*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*exp_025*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T15:53:22.101910+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T15:53:22.102033+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T15:53:22.102177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_n32.py\\nfix_n32_greedy.py\\nreport.json\\nsamples.jsonl\\nunified_n_ablation.py\\nunified_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T15:53:22.102304+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/unified_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/unified_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T15:53:22.102511+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"N=2\\\": {\\n    \\\"mean\\\": {\\n      \\\"greedy_f1\\\": 0.6141426397404832,\\n      \\\"oracle_f1\\\": 0.6579218605611794,\\n      \\\"degeneracy_rate\\\": 0.44101633393829404,\\n      \\\"lp_range_median\\\": 0.011581578814283528,\\n      \\\"selection_f1\\\": {\\n        \\\"LP\\\": 0.6066211648943465,\\n        \\\"SJ\\\": 0.588790100419491,\\n        \\\"FK\\\": 0.588790100419491,\\n        \\\"EM\\\": 0.588790100419491,\\n        \\\"VC\\\": 0.5914766014325639\\n      },\\n      \\\"best_signal\\\": \\\"LP\\\",\\n      \\\"best_signal_f1\\\": 0.6066211648943465,\\n      \\\"oracle_gap\\\": 0.043779220820696185\\n    },\\n    \\\"std\\\": {\\n      \\\"greedy_f1\\\": 0.0,\\n      \\\"oracle_f1\\\": 0.0066041802196025855,\\n      \\\"degeneracy_rate\\\": 0.014632046730124412,\\n      \\\"lp_range_median\\\": 0.0006619078367656543,\\n      \\\"selection_f1\\\": {\\n        \\\"LP\\\": 0.0088900508526633,\\n        \\\"SJ\\\": 0.007559922683892509,\\n        \\\"FK\\\": 0.007559922683892509,\\n        \\\"EM\\\": 0.007559922683892509,\\n        \\\"VC\\\": 0.007355651905085648\\n      },\\n      \\\"best_signal_f1\\\": 0.0088900508526633\\n    },\\n    \\\"n_repeats\\\": 10\\n  },\\n  \\\"N=4\\\": {\\n    \\\"mean\\\": {\\n      \\\"greedy_f1\\\": 0.6141426397404832,\\n      \\\"oracle_f1\\\": 0.7121691534862774,\\n      \\\"degeneracy_rate\\\": 0.22359346642468242,\\n      \\\"lp_range_median\\\": 0.026751114496887655,\\n      \\\"selection_f1\\\": {\\n        \\\"LP\\\": 0.6140475833349519,\\n        \\\"SJ\\\": 0.608049178586462,\\n        \\\"FK\\\": 0.6091707600897588,\\n        \\\"EM\\\": 0.601419782873023,\\n        \\\"VC\\\": 0.6011393117912787\\n      },\\n      \\\"best_signal\\\": \\\"LP\\\",\\n      \\\"best_signal_f1\\\": 0.6140475833349519,\\n      \\\"oracle_gap\\\": 0.09802651374579419\\n    },\\n    \\\"std\\\": {\\n      \\\"greedy_f1\\\": 0.0,\\n      \\\"oracle_f1\\\": 0.004
…[truncated 3908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T15:53:22.102705+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/unified_n_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/unified_n_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T15:53:22.102981+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Unified N-ablation from N=32 data source.\\nSubsamples N={2,4,8,16} from the 32-sample pool, computes N=32 natively.\\nAll metrics use same greedy, same instances, same evaluation logic.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport numpy as np\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import _ner_soft_jaccard_pair, _extract_surface_keys\\nfrom evaluation import per_instance_f1\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nDATA_PATH = f\\\"{BASE}/output/exp_025_n32/samples.jsonl\\\"\\nOUT_PATH = f\\\"{BASE}/output/exp_025_n32/unified_results.json\\\"\\nSUBTASK = \\\"ner\\\"\\nSIGNALS = [\\\"LP\\\", \\\"SJ\\\", \\\"FK\\\", \\\"EM\\\", \\\"VC\\\"]\\nTARGET_NS = [2, 4, 8, 16, 32]\\nN_REPEATS = 10  # for subsampled N < 32\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef compute_signals_for_subset(samples):\\n    n = len(samples)\\n    \\n    lp_scores = []\\n    for s in samples:\\n        lp = s.get(\\\"mean_logprob\\\")\\n        if lp is None:\\n            lp = s.get(\\\"cumulative_logprob\\\", -999) / max(s.get(\\\"n_tokens\\\", 1), 1)\\n        lp_scores.append(lp)\\n    \\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\\n    \\n    # FK\\n    fk_matrix = np.zeros((n, n))\\n    for i in range(n):\\n        for j in range(i + 1, n):\\n            union = len(key_sets[i] | key_sets[j])\\n            inter = len(key_sets[i] & key_sets[j])\\n            s = inter / union if union > 0 else 1.0\\n            fk_matrix[i][j] = s\\n            fk_matrix[j][i] = s\\n    np.fill_diagonal(fk_matrix, 1.0)\\n    fk_scores = [float(np.mean([fk_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]\\n    \\n    # SJ\\n    sj_matrix = np.zeros((n, n))\\n    for i
…[truncated 7224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T15:53:22.103202+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T15:53:22.103465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 32,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6581145584725536,\\n  \\\"ner_oracle_f1\\\": 0.8379351740696278,\\n  \\\"ner_oracle_headroom\\\": 0.17982061559707418,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.49884618890774235,\\n  \\\"ner_soft_jaccard_mean\\\": 0.6972727616819528,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3104317317443776,\\n    \\\"p_value\\\": 2.7879349634746094e-13,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.43972007053492873,\\n    \\\"p_value\\\": 2.0197400341096664e-26,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.22489714613893846,\\n    \\\"p_value\\\": 6.953617417429226e-07,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3949849480599202,\\n    \\\"p_value\\\": 2.929001157753286e-19,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.12928833879055113,\\n  \\\"ner_sample_f1_mean\\\": 0.6102440308251512,\\n  \\\"ner_sample_f1_std\\\": 0.31752821191771086,\\n  \\\"ner_sample_f1_pct_zero\\\": 12.340500945179585,\\n  \\\"ner_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.21069909022670782,\\n      \\\"p_rho\\\": 1.0103511807447588e-06,\\n      \\\"tau\\\": 0.15259812016250662,\\n      \\\"p_tau\\\": 5.442449251443652e-07,\\n      \\\"auroc\\\": 0.573367358775084,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.1476779389494176,\\n      \\\"p_rho\\\": 0.0012180261242491065,\\n      \\\"tau\\\": 0.10746986008
…[truncated 2344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T15:53:22.103650+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/analyze_n32.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/analyze_n32.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T15:53:22.103915+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute selection metrics for N=32 native inference (no subsampling).\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport os\\nimport numpy as np\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import _ner_soft_jaccard_pair, _extract_surface_keys\\nfrom evaluation import per_instance_f1\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nDATA_PATH = f\\\"{BASE}/output/exp_025_n32/samples.jsonl\\\"\\nRESULTS_PATH = f\\\"{BASE}/output/exp_025_n_ablation/results.json\\\"\\nSUBTASK = \\\"ner\\\"\\nSIGNALS = [\\\"LP\\\", \\\"SJ\\\", \\\"FK\\\", \\\"EM\\\", \\\"VC\\\"]\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef compute_signals_for_subset(samples):\\n    N = len(samples)\\n    \\n    # LP\\n    lp_scores = []\\n    for s in samples:\\n        lp = s.get(\\\"mean_logprob\\\")\\n        if lp is None:\\n            lp = s.get(\\\"cumulative_logprob\\\", -999) / max(s.get(\\\"n_tokens\\\", 1), 1)\\n        lp_scores.append(lp)\\n    \\n    # Surface key sets\\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\\n    \\n    # FK: pairwise surface Jaccard\\n    fk_matrix = np.zeros((N, N))\\n    for i in range(N):\\n        for j in range(i + 1, N):\\n            union = len(key_sets[i] | key_sets[j])\\n            inter = len(key_sets[i] & key_sets[j])\\n            s = inter / union if union > 0 else 1.0\\n            fk_matrix[i][j] = s\\n            fk_matrix[j][i] = s\\n    np.fill_diagonal(fk_matrix, 1.0)\\n    fk_scores = [float(np.mean([fk_matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\\n    \\n    # SJ: structural soft Jaccard\\n    sj_matrix = np.zeros((N, N))\\n    for i in range(N):\\n        for j in range(i + 1, N):\\n            s = _ner_soft_jaccard_pai
…[truncated 6398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T15:53:22.104104+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/fix_n32_greedy.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/fix_n32_greedy.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T15:53:22.104397+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fix N=32 analysis: use actual greedy field instead of samples[0].\\nUses EXACTLY the same evaluation logic as n_ablation.py.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport numpy as np\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import _ner_soft_jaccard_pair, _extract_surface_keys\\nfrom evaluation import per_instance_f1\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nDATA_PATH = f\\\"{BASE}/output/exp_025_n32/samples.jsonl\\\"\\nRESULTS_PATH = f\\\"{BASE}/output/exp_025_n_ablation/results.json\\\"\\nSUBTASK = \\\"ner\\\"\\nSIGNALS = [\\\"LP\\\", \\\"SJ\\\", \\\"FK\\\", \\\"EM\\\", \\\"VC\\\"]\\nN = 32\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef compute_signals_for_subset(samples):\\n    n = len(samples)\\n    \\n    # LP\\n    lp_scores = []\\n    for s in samples:\\n        lp = s.get(\\\"mean_logprob\\\")\\n        if lp is None:\\n            lp = s.get(\\\"cumulative_logprob\\\", -999) / max(s.get(\\\"n_tokens\\\", 1), 1)\\n        lp_scores.append(lp)\\n    \\n    # Surface key sets\\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\\n    \\n    # FK: pairwise surface Jaccard\\n    fk_matrix = np.zeros((n, n))\\n    for i in range(n):\\n        for j in range(i + 1, n):\\n            union = len(key_sets[i] | key_sets[j])\\n            inter = len(key_sets[i] & key_sets[j])\\n            s = inter / union if union > 0 else 1.0\\n            fk_matrix[i][j] = s\\n            fk_matrix[j][i] = s\\n    np.fill_diagonal(fk_matrix, 1.0)\\n    fk_scores = [float(np.mean([fk_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]\\n    \\n    # SJ: structural soft Jaccard\\n    sj_matrix = np.zeros((n, n))\\n    for i in range(n):\\n        for j in rang
…[truncated 7153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T15:53:22.104600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T15:53:22.104738+00:00_

1	% DEPRECATED: This file has been superseded by n_scaling_appendix_tables_44b000.tex
2	% The original content used outdated model name "Qwen 2.5-7B".
3	% Kept as reference only — do not \input this file.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T15:53:22.104867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-16T15:53:22.105019+00:00_

1	% N-scaling appendix tables for Structured Self-Consistency paper
2	% Requires: booktabs package
3	
4	%%% Table 1: N=8 vs N=16 Comparison (Spearman ρ)
5	\begin{table}[t]
6	\centering
7	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
8	\label{tab:n-scaling}
9	\small
10	\begin{tabular}{l ccc ccc}
11	\toprule
12	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
13	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
14	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
15	\midrule
16	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
17	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
18	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
19	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
20	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
21	\midrule
22	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	%%% Table 2: Cross-seed Signal Ranking Stability (Kendall's W)
28	\begin{table}[t]
29	\centering
30	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
31	\label{tab:ranking-stability}
32	\small
33	\begin{tabular}{ll cc l}
34	\toprule
35	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
36	\midrule
37	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
38	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
39	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
40	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
41	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	%%% Table 3: Per-signal Cross-seed σ Comparison
47	\begin{table}[t]
48	\centering
49	\caption{Cross-seed standard deviation ($\sigma
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-16T15:53:22.105267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "909",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "909",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-16T15:53:22.105423+00:00_

909	\begin{table}[t]
910	\centering
911	\small
912	\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, seed${=}42$).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
913	\label{tab:n_scaling_selection}
914	\begin{tabular}{ccccccccc}
915	\toprule
916	$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
917	\midrule
918	2 & 44.1\% & $+$3.3 & $-$0.75 & $-$2.26 & $-$1.79 & $-$1.91 & $-$2.27 & $-$0.75 \\
919	4 & 24.6\% & $+$9.2 & $-$0.02 & $-$0.53 & $-$0.54 & $-$0.58 & $-$2.18 & $-$0.02 \\
920	8 & 13.3\% & $+$14.2 & $+$0.42 & $+$0.01 & $+$0.18 & $+$0.35 & $-$1.43 & $+$0.42 \\
921	16 & 7.2\% & $+$17.8 & $+$0.63 & $+$0.15 & $+$0.24 & $+$0.40 & $-$2.04 & $+$0.63 \\
922	32 & 4.0\% & ${\sim}+$20 & $+$0.91 & $+$0.34 & $+$0.83 & $+$0.22 & $-$4.18 & $+$0.91 \\
923	\bottomrule
924	\end{tabular}
925	\end{table}
926	\footnotetext{$N$-scaling analysis uses subsampled evaluation on the full 551-instance test set. Absolute greedy F1 (0.614) differs from Table~\ref{tab:selection} (0.645) due to the subsampling procedure and instance weighting; relative trends are consistent.}
927	
928	\section{Temperature Ablation}\label{app:t_ablation}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-16T15:53:22.105562+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "2 & 44.1\\% & $+$3.3 & $-$0.75 & $-$2.26 & $-$1.79 & $-$1.91 & $-$2.27 & $-$0.75 \\\\\n4 & 24.6\\% & $+$9.2 & $-$0.02 & $-$0.53 & $-$0.54 & $-$0.58 & $-$2.18 & $-$0.02 \\\\\n8 & 13.3\\% & $+$14.2 & $+$0.42 & $+$0.01 & $+$0.18 & $+$0.35 & $-$1.43 & $+$0.42 \\\\\n16 & 7.2\\% & $+$17.8 & $+$0.63 & $+$0.15 & $+$0.24 & $+$0.40 & $-$2.04 & $+$0.63 \\\\\n32 & 4.0\\% & ${\\sim}+$20 & $+$0.91 & $+$0.34 & $+$0.83 & $+$0.22 & $-$4.18 & $+$0.91 \\\\",
  "new_string": "2 & 44.1\\% & $+$4.4 & $-$0.75 & $-$2.54 & $-$2.54 & $-$2.54 & $-$2.27 & $-$0.75 \\\\\n4 & 22.4\\% & $+$9.8 & $-$0.01 & $-$0.61 & $-$0.50 & $-$1.27 & $-$1.30 & $-$0.01 \\\\\n8 & 12.4\\% & $+$13.8 & $+$0.42 & $+$0.03 & $+$0.11 & $-$0.33 & $-$1.82 & $+$0.42 \\\\\n16 & 6.8\\% & $+$16.7 & $+$0.63 & $+$0.26 & $+$0.43 & $-$0.15 & $-$2.91 & $+$0.63 \\\\\n32 & 4.0\\% & $+$19.2 & $+$0.91 & $+$0.33 & $+$0.62 & $+$0.21 & $-$4.18 & $+$0.91 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "2 & 44.1\\% & $+$3.3 & $-$0.75 & $-$2.26 & $-$1.79 & $-$1.91 & $-$2.27 & $-$0.75 \\\\\n4 & 24.6\\% & $+$9.2 & $-$0.02 & $-$0.53 & $-$0.54 & $-$0.58 & $-$2.18 & $-$0.02 \\\\\n8 & 13.3\\% & $+$14.2 & $+$0.42 & $+$0.01 & $+$0.18 & $+$0.35 & $-$1.43 & $+$0.42 \\\\\n16 & 7.2\\% & $+$17.8 & $+$0.63 & $+$0.15 & $+$0.24 & $+$0.40 & $-$2.04 & $+$0.63 \\\\\n32 & 4.0\\% & ${\\sim}+$20 & $+$0.91 & $+$0.34 & $+$0.83 & $+$0.22 & $-$4.18 & $+$0.91 \\\\",
    "new_string": "2 & 44.1\\% & $+$4.4 & $-$0.75 & $-$2.54 & $-$2.54 & $-$2.54 & $-$2.27 & $-$0.75 \\\\\n4 & 22.4\\% & $+$9.8 & $-$0.01 & $-$0.61 & $-$0.50 & $-$1.27 & $-$1.30 & $-$0.01 \\\\\n8 & 12.4\\% & $+$13.8 & $+$0.42 & $+$0.03 & $+$0.11 & $-$0.33 & $-$1.82 & $+$0.42 \\\\\n16 & 6.8\\% & $+$16.7 & $+$0.63 & $+$0.26 & $+$0.43 & $-$0.15 & $-$2.91 & $+$0.63 \\\\\n32 & 4.0\\% & $+$19.2 & $+$0.91 & $+$0.33 & $+$0.62 & $+$0.21 & $-$4.18 & $+$0.91 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-16T15:53:22.105892+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-16T15:53:22.106056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "offset": "60",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "offset": "60",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-16T15:53:22.106222+00:00_

60	Stratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
61	\paragraph{Effect of sample count.}
62	Increasing $N$ from 2 to 32 expands oracle headroom sixfold ($+3.3$ to ${\sim}{+}20$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom exceeds 20~pp---the best signal captures less than 5\% of the available improvement (Table~\ref{tab:n_scaling_selection}).
63	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
64	
65	\paragraph{Effect of sampling temperature.}
66	Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing beyond $T{=}1.0$ ($+13.0$~pp at $T{=}1.2$; Table~\ref{tab:t_ablation} in Appendix), confirming that higher temperature produces more diverse candidate pools.
67	Structural QE signals (SJ $\rho$) improve with temperature ($0.297 \to 0.377$), while LP $\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades---consistent with LP compression being model-intrinsic rather than temperature-dependent.
68	Despite expanded headroom and improved QE signals at higher temperatures, selection gains remain negligible, further isolating the bottleneck at the within-instance ranking mechanism rather than signal quality or output diversity.
69	
70	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidence}; \
…[truncated 402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-16T15:53:22.106377+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "old_string": "Increasing $N$ from 2 to 32 expands oracle headroom sixfold ($+3.3$ to ${\\sim}{+}20$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom exceeds 20~pp---the best signal captures less than 5\\% of the available improvement (Table~\\ref{tab:n_scaling_selection}).",
  "new_string": "Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement (Table~\\ref{tab:n_scaling_selection})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "old_string": "Increasing $N$ from 2 to 32 expands oracle headroom sixfold ($+3.3$ to ${\\sim}{+}20$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom exceeds 20~pp---the best signal captures less than 5\\% of the available improvement (Table~\\ref{tab:n_scaling_selection}).",
    "new_string": "Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement (Table~\\ref{tab:n_scaling_selection})."
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-16T15:53:22.106558+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-16T15:53:22.106701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "902",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "902",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T15:53:22.106830+00:00_

902	\paragraph{$N$-scaling: selection headroom vs.\ selection gain.}
903	Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
904	Oracle headroom grows roughly linearly with $N$ ($+3.3$~pp at $N{=}2$ to ${\sim}{+}20$~pp at $N{=}32$).
905	LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom exceeds 20~pp---the best signal captures less than 5\% of the available improvement.
906	Degeneracy drops monotonically (44\% at $N{=}2$ to 4\% at $N{=}32$), yet reduced degeneracy does not unlock selection---consistent with the LoRA-rank ablation finding (\S\ref{sec:robustness_main}).
907	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
908	
909	\begin{table}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-16T15:53:22.106965+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "Oracle headroom grows roughly linearly with $N$ ($+3.3$~pp at $N{=}2$ to ${\\sim}{+}20$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom exceeds 20~pp---the best signal captures less than 5\\% of the available improvement.",
  "new_string": "Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+19.2$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "Oracle headroom grows roughly linearly with $N$ ($+3.3$~pp at $N{=}2$ to ${\\sim}{+}20$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom exceeds 20~pp---the best signal captures less than 5\\% of the available improvement.",
    "new_string": "Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+19.2$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement."
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T15:53:22.107338+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-16T15:53:22.107525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "902",
  "limit": "28"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "902",
    "limit": "28"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T15:53:22.107674+00:00_

902	\paragraph{$N$-scaling: selection headroom vs.\ selection gain.}
903	Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
904	Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+19.2$~pp at $N{=}32$).
905	LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement.
906	Degeneracy drops monotonically (44\% at $N{=}2$ to 4\% at $N{=}32$), yet reduced degeneracy does not unlock selection---consistent with the LoRA-rank ablation finding (\S\ref{sec:robustness_main}).
907	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
908	
909	\begin{table}[t]
910	\centering
911	\small
912	\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, seed${=}42$).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
913	\label{tab:n_scaling_selection}
914	\begin{tabular}{ccccccccc}
915	\toprule
916	$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
917	\midrule
918	2 & 44.1\% & $+$4.4 & $-$0.75 & $-$2.54 & $-$2.54 & $-$2.54 & $-$2.27 & $-$0.75 \\
919	4 & 22.4\% & $+$9.8 & $-$0.01 & $-$0.61 & $-$0.50 & $-$1.27 & $-$1.30 & $-$0.01 \\
920	8 & 12.4\% & $+$13.8 & $+$0.42 & $+$0.03 & $+$0.11 & $-$0.33 & $-$1.82 & $+$0.42 \\
921	16 & 6.8\% & $+$16.7 & $+$0.63 & $+$0.26 & $+$0.43 & $-$0.15 & $-$2.91 & $+$0.63 \\
922	32 & 4.0\% & $+$19.2 & $+$0.91 & $+$0.33 & $+$0.62 & $+$0.21 & $-$4.18 & $+$0.91 \\
923	\bottomrule
924	\end{tabular}
925	\end{table}
926	\footnotetext{$N$-scaling analysis uses subsampled evaluation on the full 551-instance test set. Absol
…[truncated 225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-16T15:53:22.107860+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "3\\.3|sixfold|exceeds 20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "tool_args": {
    "pattern": "3\\.3|sixfold|exceeds 20",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-16T15:53:22.108000+00:00_

docs/paper/sections/experiments.tex:108:On SciERC NER (2-seed sign tests\footnote{Multi-seed NER experiments confirm seed variation is small ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
docs/paper/sections/experiments.tex:112:LP approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3~pp gap).
docs/paper/sections/experiments.tex:146:Reducing rank lowers degeneracy from 21\% to 7.2\% and increases oracle headroom from 13.3~pp to 16.0~pp, confirming that fine-tuning capacity drives output convergence.
docs/paper/sections/discussion.tex:16:Meanwhile, LP selection approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, $p{=}0.29$; Table~\ref{tab:selection}), and both fall far short of the oracle (0.778, 13.3~pp gap)---multi-sample selection adds cost without closing the gap.
docs/paper/sections/discussion.tex:66:Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing beyond $T{=}1.0$ ($+13.0$~pp at $T{=}1.2$; Table~\ref{tab:t_ablation} in Appendix), confirming that higher temperature produces more diverse candidate pools.
docs/paper/sections/discussion.tex:96:However, entity-token LP selection performs strictly \textit{worse} than full-sequence LP on both datasets ($-2.0$~pp on SciERC, $-3.3$~pp on CoNLL).
docs/paper/sections/appendix.tex:701:The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
docs/paper/sections/appendix.tex:943:1.0 & $+$13.3 &
…[truncated 348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-16T15:53:22.108174+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fourfold|fivefold|sixfold",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fourfold|fivefold|sixfold",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-16T15:53:22.108309+00:00_

docs/paper/sections/discussion.tex:62:Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement (Table~\ref{tab:n_scaling_selection}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-16T15:53:22.108454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "offset": "61",
  "limit": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "offset": "61",
    "limit": "4"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-16T15:53:22.108581+00:00_

61	\paragraph{Effect of sample count.}
62	Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement (Table~\ref{tab:n_scaling_selection}).
63	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
64	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 95 · 2026-05-16T15:53:22.108749+00:00_

## 报告

### N-scaling 表修正结果

**修改文件：**
1. `docs/paper/sections/appendix.tex` — 表格数据 + 上方总结文字
2. `docs/paper/sections/discussion.tex` — 引用数值

**数据源：** `/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/unified_results.json`（macro F1, 551实例, seed=42 inference, 10-trial subsampling for N<32）

### 修正前后对比

| N | 列 | 旧值 | 新值 | 问题 |
|---|---|------|------|------|
| 2 | Oracle | +3.3 | +4.4 | 数值错误 |
| 2 | SJ/FK/EM | -2.26/-1.79/-1.91 | -2.54/-2.54/-2.54 | N=2时3个信号必然相同（对称tie） |
| 4 | Degen | 24.6% | 22.4% | |
| 4 | EM | -0.58 | -1.27 | |
| 4 | VC | -2.18 | -1.30 | |
| 8 | Degen | 13.3% | 12.4% | |
| 8 | Oracle | +14.2 | +13.8 | |
| 8 | **EM** | **+0.35** | **-0.33** | **符号错误** |
| 8 | VC | -1.43 | -1.82 | |
| 16 | **EM** | **+0.40** | **-0.15** | **符号错误** |
| 16 | VC | -2.04 | -2.91 | |
| 32 | Oracle | ~+20 | +19.2 | |
| 32 | FK | +0.83 | +0.62 | |

### 与 Table 2 的关系

- **Table 2 greedy**: 0.645 macro F1 (529 instances, 2-seed mean)
- **N-scaling 表 greedy**: 0.614 macro F1 (551 instances, seed=42 only)
- Footnote 已说明差异来源（instance set + weighting）
- 表内只报告 deltas (pp)，无直接绝对值冲突
- **结论：metric 空间一致（都是 macro F1），baseline 差异已由 footnote 充分说明**

### 根因

旧表格由一个有 bug 的早期脚本生成（`n_ablation.py` 的 `results.json` 中 rank32 regime），未使用统一 N=32 数据源的正确 greedy field，且 N=2 时未正确处理 consensus 信号的对称 tie。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_n_scaling_metric_consistency_20260516T154206"
}
```

</details>

---
