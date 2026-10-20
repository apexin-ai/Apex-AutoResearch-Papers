# paper tawm contribution

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_tawm-contribution_20260518T060258.jsonl`
- **Structured JSON:** [`18f9031d9c1a5736581d.json`](../../sessions/18/18f9031d9c1a5736581d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-18T06:04:02.882217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T06:04:02.882724+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T06:04:02.883014+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T06:04:02.883249+00:00_

docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
artifacts/analysis/detector_table.tex
docs/paper/sections/abstract_body.tex
paper/tables/nve_sensitivity_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
docs/paper/sections/related_work.tex
docs/paper/sections/methodology.tex
docs/paper/main.tex
docs/paper/sections/analysis.tex
docs/paper/sections/introduction.tex
docs/paper/sections/appendix.tex
docs/paper/sections/results.tex
docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T06:04:02.883472+00:00_

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
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T06:04:02.883694+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the causal factor within the factorial design tested. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A $\nve \geq 1.5\times$ threshold (35K+ window) achieves 11/12 CIVO classification ($n{=}12$, single environment), with one non-CIVO false positive, a failure mode analogous to delusional bias \citep{lu2018nondelusional} that arises from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals a non-obvious mechanism: the reward head contributes the largest gradient share (38--49\%) but does not encode $\dt$-specific structural information, while the observation decoder channel (16--22\%) carries the critical spatial predictions that drive the RSSM fidelity gap. Reward-only gradient stopping fails (NVE $10.42\times$) despite targeting the largest pathway; full-pathway SGS that removes observation decoder gradients from the temporal embedding \sgsclaim{} (eval \sgseva
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T06:04:02.884031+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "old_string": "and (4)~a lightweight four-condition rule-based monitor that tracks value-to-evaluation ratio dynamics achieves 100\\% sensitivity for CIVO detection (3/3 cases) with predictive warning before performance degradation in 2/3 cases, which supports early intervention without a reference baseline run.",
  "new_string": "and (4)~a lightweight four-condition rule-based monitor that tracks value-to-evaluation ratio dynamics achieves 100\\% sensitivity for CIVO detection (3/3 cases) with predictive warning before performance degradation in 2/3 cases, which supports early intervention without a reference baseline run.\n\n\\paragraph{Contributions.}\n\\begin{itemize}\n    \\item We identify the feedback architecture (imagination-based bootstrapping versus MPC re-planning) as the structural factor that determines whether $\\dt$-conditioning is beneficial or pathological, explaining why identical conditioning succeeds in TD-MPC2 but fails in DreamerV3.\n\\end{itemize}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "old_string": "and (4)~a lightweight four-condition rule-based monitor that tracks value-to-evaluation ratio dynamics achieves 100\\% sensitivity for CIVO detection (3/3 cases) with predictive warning before performance degradation in 2/3 cases, which supports early intervention without a reference baseline run.",
    "new_string": "and (4)~a lightweight four-condition rule-based monitor that tracks value-to-evaluation ratio dynamics achieves 100\\% sensitivity for CIVO detection (3/3 cases) with predictive warning before performance degradation in 2/3 cases, which supports early intervention without a reference baseline run.\n\n\\paragraph{Contributions.}\n\\begin{itemize}\n    \\item We identify the feedback architecture (imagination-based bootstrapping versus MPC re-planning) as the structural factor that determines whether $\\dt$-conditioning is beneficial or pathological, explaining why identical conditioning succeeds in TD-MPC2 but fails in DreamerV3.\n\\end{itemize}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T06:04:02.884432+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T06:04:02.884589+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T06:04:02.884721+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_tawm-contribution_20260518T060258",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T06:04:02.884925+00:00_

em-dash 检查通过。

修改结果：

- **文件**: `docs/paper/sections/introduction.tex`
- **位置**: 第 9 行之后（introduction 末尾）
- **内容**: 新增 `\paragraph{Contributions.}` + `\begin{itemize}` 包含一条 analytical contribution

注意：当前 introduction 原本没有正式的 contribution list。新增的是一个独立的 Contributions 段落，目前只有这一条 analytical item。如需将其他 findings（如 CIVO 发现、SGS 干预、监控器等）也提炼为正式 contribution 项，可以后续补充到同一列表中。另外，最后一段 inline 第 (3) 点的内容与新增条目高度重叠，后续可考虑精简以避免重复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_tawm-contribution_20260518T060258"
}
```

</details>

---
