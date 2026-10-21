# paper update experiments tex

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_update-experiments-tex_20260520T105917.jsonl`
- **Structured JSON:** [`e869e7e0c054d7d7c85b.json`](../../sessions/e8/e869e7e0c054d7d7c85b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-20T11:03:00.505531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T11:03:00.505969+00:00_

1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\ref{sec:m2_sign_misattribution}?
7	
8	\subsection{Experimental Setup}
9	\label{sec:experimental_setup}
10	
11	\paragraph{Environment.}
12	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib
13	ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.
14	
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window contain
…[truncated 14854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T11:03:00.506332+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "old_string": "\\placeholder{plan\\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}",
  "new_string": "All $h$-sweep conditions are currently single-seed. Multi-seed replication (3 seeds per $h$) is planned.% Sources: exp028c ($h=2$), exp029 (episode-level)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
    "old_string": "\\placeholder{plan\\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}",
    "new_string": "All $h$-sweep conditions are currently single-seed. Multi-seed replication (3 seeds per $h$) is planned.% Sources: exp028c ($h=2$), exp029 (episode-level)."
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T11:03:00.506561+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T11:03:00.506736+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "old_string": "\\placeholder{tab1\\_main\\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\\%), Action Valid (\\%), Pass@8. Multi-seed mean$\\pm$std from plan\\_003.}",
  "new_string": "Table~\\ref{tab:main_results} summarizes the central comparison. All seed results are reported individually due to high inter-seed variance under step-independent conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{1.7B ALFWorld results across credit assignment methods. OOD: held-out test tasks; In-Dist: 32-episode validation set. All seeds shown; no aggregation due to high inter-seed variance.}\n\\label{tab:main_results}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed} & \\textbf{OOD (\\%)} & \\textbf{In-Dist (\\%)} \\\\\n\\midrule\nStep-indep.\\ ($h{=}2$, windowed) & 1 & 0 & 0 \\\\  % Cell A\n                                  & 2 & 3.73 & 9.375 \\\\  % Cell A seed2\n\\midrule\nStep-indep.\\ (factorial)          & 1 & 0.75 & 20 \\\\  % Cell B\n                                  & 2 & 0.75 & 55.5 \\\\  % Cell B seed2\n\\midrule\nEpisode-level (full context)      & 1 & 23.88 & 28.125 \\\\  % Cell C, exp029\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
    "old_string": "\\placeholder{tab1\\_main\\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\\%), Action Valid (\\%), Pass@8. Multi-seed mean$\\pm$std from plan\\_003.}",
    "new_string": "Table~\\ref{tab:main_results} summarizes the central comparison. All seed results are reported individually due to high inter-seed variance under step-independent conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{1.7B ALFWorld results across credit assignment methods. OOD: held-out test tasks; In-Dist: 32-episode validation set. All seeds shown; no aggregation due to high inter-seed variance.}\n\\label{tab:main_results}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed} & \\textbf{OOD (\\%)} & \\textbf{In-Dist (\\%)} \\\\\n\\midrule\nStep-indep.\\ ($h{=}2$, windowed) & 1 & 0 & 0 \\\\  % Cell A\n                                  & 2 & 3.73 & 9.375 \\\\  % Cell A seed2\n\\midrule\nStep-indep.\\ (factorial)          & 1 & 0.75 & 20 \\\\  % Cell B\n                                  & 2 & 0.75 & 55.5 \\\\  % Cell B seed2\n\\midrule\nEpisode-level (full context)      & 1 & 23.88 & 28.125 \\\\  % Cell C, exp029\n\\bottomrule\n\\end{tabular}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T11:03:00.506951+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T11:03:00.507090+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "old_string": "\\placeholder{tab2\\_h\\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \\in \\{2, 5, 10, 20, \\text{full}\\}$, 3 seeds per $h$.}",
  "new_string": "\\begin{table}[t]\n\\centering\n\\caption{Window-size ablation (1.7B, single seed). OOD success rate at the final training step. $h = \\text{full}$ denotes episode-level training (exp029).}\n\\label{tab:h_sweep}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Window size $h$} & \\textbf{OOD Success (\\%)} \\\\\n\\midrule\n$h = 2$  & 0 \\\\\n$h = 5$  & 0 \\\\\n$h = 10$ & 6.25 \\\\\n$h = 20$ & 15.6 \\\\\n$h = \\text{full}$ (episode-level) & 23.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
    "old_string": "\\placeholder{tab2\\_h\\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \\in \\{2, 5, 10, 20, \\text{full}\\}$, 3 seeds per $h$.}",
    "new_string": "\\begin{table}[t]\n\\centering\n\\caption{Window-size ablation (1.7B, single seed). OOD success rate at the final training step. $h = \\text{full}$ denotes episode-level training (exp029).}\n\\label{tab:h_sweep}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Window size $h$} & \\textbf{OOD Success (\\%)} \\\\\n\\midrule\n$h = 2$  & 0 \\\\\n$h = 5$  & 0 \\\\\n$h = 10$ & 6.25 \\\\\n$h = 20$ & 15.6 \\\\\n$h = \\text{full}$ (episode-level) & 23.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T11:03:00.507277+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T11:03:00.507410+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "old_string": "The ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.",
  "new_string": "The ablation reveals a credit assignment cliff consistent with our theoretical predictions (Table~\\ref{tab:h_sweep}). OOD success rate is 0\\% for $h \\leq 5$, rises to 6.25\\% at $h = 10$ and 15.6\\% at $h = 20$, and reaches 23.88\\% under episode-level training ($h = T$). The transition between $h = 5$ and $h = 10$ marks the onset of non-trivial generalization. Results are single-seed; multi-seed replication is in progress."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
    "old_string": "The ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.",
    "new_string": "The ablation reveals a credit assignment cliff consistent with our theoretical predictions (Table~\\ref{tab:h_sweep}). OOD success rate is 0\\% for $h \\leq 5$, rises to 6.25\\% at $h = 10$ and 15.6\\% at $h = 20$, and reaches 23.88\\% under episode-level training ($h = T$). The transition between $h = 5$ and $h = 10$ marks the onset of non-trivial generalization. Results are single-seed; multi-seed replication is in progress."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T11:03:00.507607+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T11:03:00.507759+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "old_string": "\\placeholder{tab3\\_mechanism\\_verification: Sign misattribution empirical verification. Columns: Metric, Measured Value, Theoretical Prediction, Agreement. Rows: sign-outcome correlation, sign-quality correlation, $P(\\text{correct sign})$. Data from plan\\_004 per-window advantage logging.}",
  "new_string": "Table~\\ref{tab:sign_verification} reports the empirical measurements. The credit agreement rate---the fraction of windows where the advantage sign matches local action quality---is 52.07\\%, indistinguishable from the 50\\% expected under random sign assignment. The point biserial correlation between advantage sign and local action quality is $r = 0.068$, confirming near-zero dependence. Additionally, a discount factor sweep reveals that \\textit{all} $\\gamma$ values produce collapse, including $\\gamma = 1.0$ (no discounting). The $\\gamma = 1.0$ result rules out temporal discounting as the failure cause and isolates sign misattribution as the root mechanism.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical verification of sign misattribution under step-independent training ($h{=}2$). Credit agreement rate measures the fraction of windows where advantage sign matches local action quality; 50\\% indicates random assignment.}\n\\label{tab:sign_verification}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Measured} & \\textbf{Predicted} \\\\\n\\midrule\nCredit agreement rate & 52.07\\% & $\\approx$ 50\\% (random) \\\\\nPoint biserial $r$ (sign vs.\\ quality) & 0.068 & $\\approx$ 0 \\\\\nCollapse at $\\gamma = 1.0$ (no discounting) & Yes & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
    "old_string": "\\placeholder{tab3\\_mechanism\\_verification: Sign misattribution empirical verification. Columns: Metric, Measured Value, Theoretical Prediction, Agreement. Rows: sign-outcome correlation, sign-quality correlation, $P(\\text{correct sign})$. Data from plan\\_004 per-window advantage logging.}",
    "new_string": "Table~\\ref{tab:sign_verification} reports the empirical measurements. The credit agreement rate---the fraction of windows where the advantage sign matches local action quality---is 52.07\\%, indistinguishable from the 50\\% expected under random sign assignment. The point biserial correlation between advantage sign and local action quality is $r = 0.068$, confirming near-zero dependence. Additionally, a discount factor sweep reveals that \\textit{all} $\\gamma$ values produce collapse, including $\\gamma = 1.0$ (no discounting). The $\\gamma = 1.0$ result rules out temporal discounting as the failure cause and isolates sign misattribution as the root mechanism.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical verification of sign misattribution under step-independent training ($h{=}2$). Credit agreement rate measures the fraction of windows where advantage sign matches local action quality; 50\\% indicates random assignment.}\n\\label{tab:sign_verification}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Measured} & \\textbf{Predicted} \\\\\n\\midrule\nCredit agreement rate & 52.07\\% & $\\approx$ 50\\% (random) \\\\\nPoint biserial $r$ (sign vs.\\ quality) & 0.068 & $\\approx$ 0 \\\\\nCollapse at $\\gamma = 1.0$ (no discounting) & Yes & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T11:03:00.507961+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T11:03:00.508110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T11:03:00.508336+00:00_

1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\ref{sec:m2_sign_misattribution}?
7	
8	\subsection{Experimental Setup}
9	\label{sec:experimental_setup}
10	
11	\paragraph{Environment.}
12	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib
13	ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.
14	
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window contain
…[truncated 17352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update-experiments-tex_20260520T105917",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-20T11:03:00.508557+00:00_

完成。具体改动：

**替换了 5 个 placeholder：**

1. **`plan_002`** (line 47) → 单 seed 状态说明，附 exp028c/exp029 来源注释
2. **`tab1_main_results`** (原 line 60) → 1.7B 主结果表（Table 1），含 Cell A（h=2, 2 seeds: 0%/0%, 3.73%/9.375%）、Cell B（factorial, 2 seeds: 0.75%/20%, 0.75%/55.5%）、Cell C（episode-level: 23.88%/28.125%）
3. **`tab2_h_sweep`** (原 line 71) → h-sweep 消融表（Table 2），h=2→0%, h=5→0%, h=10→6.25%, h=20→15.6%, full→23.88%
4. **h-sweep 正文段落** (原 line 75-76) → 用具体数字替换 "precise numbers await multi-seed completion"，描述 credit assignment cliff
5. **`tab3_mechanism_verification`** (原 line 112) → sign misattribution 验证表（Table 3）+ 解释段落：credit agreement 52.07%≈random, point biserial r=0.068≈0, γ=1.0 坍缩

**未替换的 placeholder（无数据）：**
- `fig6_training_curves`、`fig5_h_sweep_curve`（图表占位）
- `plan_003b`（GAE baseline）
- `tab4_selective_comparison`（selective verification）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_update-experiments-tex_20260520T105917"
}
```

</details>

---
