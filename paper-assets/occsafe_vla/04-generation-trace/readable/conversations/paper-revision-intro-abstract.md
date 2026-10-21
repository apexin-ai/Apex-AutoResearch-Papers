# paper revision intro abstract

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_revision-intro-abstract_20260527T022614.jsonl`
- **Structured JSON:** [`e607524a2d17ee7ab04e.json`](../../sessions/e6/e607524a2d17ee7ab04e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-27T02:28:11.045595+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T02:28:11.045965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T02:28:11.046144+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "occsafe_vla",
  "file": "introduction.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "introduction.tex",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T02:28:11.046283+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'introduction.tex'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T02:28:11.046410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T02:28:11.046580+00:00_

1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: CoRL 2026
3	\documentclass{article}
4	
5	\usepackage[dvipsnames]{xcolor}
6	\usepackage{corl_2026}
7	
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{subcaption}
13	\usepackage{placeins}
14	
15	\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\ An Empirical Investigation}
16	
17	\author{
18	Anonymous Author(s)
19	}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates substantially lagging task completion on safety-critical benchmarks.
26	We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance, with twelve conditions varying gradient flow, label content, normalization type, spatial reference frame, and temporal extent.
27	Our central finding is negative: \textbf{all auxiliary spatial head configurations perform at or below the no-auxiliary-head baseline} on Collision Avoidance Rate (0 of 12 configurations improve; sign test on four factorial cell means, $p{=}0.0625$, with directional consistency across all twelve structurally related conditions). A $2{\times}2$ factorial (gradient flow $\times$ normalization) shows a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head into the vision encoders is associated with lower safety under both normalization types ($\Delta{=}-4.2$\,pp within BatchNorm, $-$2.5\,pp within LayerNorm). Effect sizes are large but the small-sample design ($n{\leq}4$ per cell) limits pairwise power; whether normalization type modulates the magnitude requires additional LN seeds to confirm. The BatchNorm + gradient flow cell is both the worst-performing and the most unstable configuration, with cross
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T02:28:11.046805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T02:28:11.046983+00:00_

1	\section{Introduction}
2	
3	Vision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\cite{kim2025oft} reaches a Task Success Rate (TSR) of 90.7\% but a Collision Avoidance Rate (CAR) of only 78.0\%. On the three most constrained tasks, collision rates reach 43--93\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.
4	
5	Two active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety meth
…[truncated 4143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T02:28:11.047216+00:00_

called mcp__agent-ml-research__edit_paper_section

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section</summary>

```json
{
  "project": "occsafe_vla",
  "section": "introduction",
  "old_text": "The central result is negative: \\textbf{all auxiliary spatial head configurations perform at or below the Vanilla baseline} on Collision Avoidance Rate (0 of 12 configurations improve; sign test on four factorial cell means, $p{=}0.0625$). The $2{\\times}2$ factorial subset reveals a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head degrades safety under both normalization types ($\\Delta{=}-4.2$\\,pp within BatchNorm, $-$2.5\\,pp within LayerNorm), the BN + gradient flow cell is the most unstable configuration ($\\sigma > 2.5{\\times}$ other cells), and spatial label content is irrelevant (\\S\\ref{sec:results}).",
  "new_text": "The central result is negative: \\textbf{at most 1 of 12 auxiliary spatial head configurations exceeds the Vanilla baseline} on Collision Avoidance Rate, and this difference is not statistically significant ($p{=}0.28$); the remaining 11 perform at or below baseline (11/12 $\\leq$ Vanilla; $p{\\approx}0.003$, binomial test). A $2{\\times}2$ factorial subset reveals a pattern consistent with an ordinal interaction: gradient flow degrades safety, BatchNorm amplifies the deficit and increases training instability, and spatial label content is irrelevant (\\S\\ref{sec:results})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "tool_args": {
    "project": "occsafe_vla",
    "section": "introduction",
    "old_text": "The central result is negative: \\textbf{all auxiliary spatial head configurations perform at or below the Vanilla baseline} on Collision Avoidance Rate (0 of 12 configurations improve; sign test on four factorial cell means, $p{=}0.0625$). The $2{\\times}2$ factorial subset reveals a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head degrades safety under both normalization types ($\\Delta{=}-4.2$\\,pp within BatchNorm, $-$2.5\\,pp within LayerNorm), the BN + gradient flow cell is the most unstable configuration ($\\sigma > 2.5{\\times}$ other cells), and spatial label content is irrelevant (\\S\\ref{sec:results}).",
    "new_text": "The central result is negative: \\textbf{at most 1 of 12 auxiliary spatial head configurations exceeds the Vanilla baseline} on Collision Avoidance Rate, and this difference is not statistically significant ($p{=}0.28$); the remaining 11 perform at or below baseline (11/12 $\\leq$ Vanilla; $p{\\approx}0.003$, binomial test). A $2{\\times}2$ factorial subset reveals a pattern consistent with an ordinal interaction: gradient flow degrades safety, BatchNorm amplifies the deficit and increases training instability, and spatial label content is irrelevant (\\S\\ref{sec:results})."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T02:28:11.047368+00:00_

{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex\", \"version\": 12, \"coverage\": \"0/46\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T02:28:11.047532+00:00_

called mcp__agent-ml-research__edit_paper_section

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section</summary>

```json
{
  "project": "occsafe_vla",
  "section": "introduction",
  "old_text": "shows large effect sizes consistent with an ordinal interaction:",
  "new_text": "shows large effect sizes consistent with an ordinal interaction pattern:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "tool_args": {
    "project": "occsafe_vla",
    "section": "introduction",
    "old_text": "shows large effect sizes consistent with an ordinal interaction:",
    "new_text": "shows large effect sizes consistent with an ordinal interaction pattern:"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T02:28:11.047684+00:00_

{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex\", \"version\": 13, \"coverage\": \"0/46\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T02:28:11.047836+00:00_

called mcp__agent-ml-research__edit_paper_section

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section</summary>

```json
{
  "project": "occsafe_vla",
  "section": "main",
  "old_text": "Our central finding is negative: \\textbf{all auxiliary spatial head configurations perform at or below the no-auxiliary-head baseline} on Collision Avoidance Rate (0 of 12 configurations improve; sign test on four factorial cell means, $p{=}0.0625$, with directional consistency across all twelve structurally related conditions). A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) shows a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head into the vision encoders is associated with lower safety under both normalization types ($\\Delta{=}-4.2$\\,pp within BatchNorm, $-$2.5\\,pp within LayerNorm). Effect sizes are large but the small-sample design ($n{\\leq}4$ per cell) limits pairwise power; whether normalization type modulates the magnitude requires additional LN seeds to confirm. The BatchNorm + gradient flow cell is both the worst-performing and the most unstable configuration, with cross-seed standard deviation more than $2.5{\\times}$ that of other cells.",
  "new_text": "Our central finding is negative: \\textbf{at most 1 of 12 auxiliary spatial head configurations exceeds the Vanilla baseline} on Collision Avoidance Rate (CAR), and this difference is not statistically significant ($p{=}0.28$); the remaining 11 perform at or below baseline (11/12 $\\leq$ Vanilla; $p{\\approx}0.003$, binomial test). A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) shows a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head into the vision encoders is associated with lower safety ($\\Delta{=}-4.2$\\,pp within the BatchNorm conditions), and BatchNorm amplifies this deficit compared to LayerNorm. Effect sizes are large but the small-sample design ($n{\\leq}4$ per cell) limits pairwise power; the global directional consistency across all twelve conditions provides the primary statistical evidence. The BatchNorm + gradient flow cell is both the worst-performing and the most unstable configuration, with cross-seed standard deviation more than $2.5{\\times}$ that of other cells."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "tool_args": {
    "project": "occsafe_vla",
    "section": "main",
    "old_text": "Our central finding is negative: \\textbf{all auxiliary spatial head configurations perform at or below the no-auxiliary-head baseline} on Collision Avoidance Rate (0 of 12 configurations improve; sign test on four factorial cell means, $p{=}0.0625$, with directional consistency across all twelve structurally related conditions). A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) shows a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head into the vision encoders is associated with lower safety under both normalization types ($\\Delta{=}-4.2$\\,pp within BatchNorm, $-$2.5\\,pp within LayerNorm). Effect sizes are large but the small-sample design ($n{\\leq}4$ per cell) limits pairwise power; whether normalization type modulates the magnitude requires additional LN seeds to confirm. The BatchNorm + gradient flow cell is both the worst-performing and the most unstable configuration, with cross-seed standard deviation more than $2.5{\\times}$ that of other cells.",
    "new_text": "Our central finding is negative: \\textbf{at most 1 of 12 auxiliary spatial head configurations exceeds the Vanilla baseline} on Collision Avoidance Rate (CAR), and this difference is not statistically significant ($p{=}0.28$); the remaining 11 perform at or below baseline (11/12 $\\leq$ Vanilla; $p{\\approx}0.003$, binomial test). A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) shows a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head into the vision encoders is associated with lower safety ($\\Delta{=}-4.2$\\,pp within the BatchNorm conditions), and BatchNorm amplifies this deficit compared to LayerNorm. Effect sizes are large but the small-sample design ($n{\\leq}4$ per cell) limits pairwise power; the global directional consistency across all twelve conditions provides the primary statistical evidence. The BatchNorm + gradient flow cell is both the worst-performing and the most unstable configuration, with cross-seed standard deviation more than $2.5{\\times}$ that of other cells."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T02:28:11.047982+00:00_

{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex\", \"version\": 15, \"coverage\": \"0/46\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T02:28:11.048123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "offset": "15",
  "limit": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "offset": "15",
    "limit": "11"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T02:28:11.048259+00:00_

15	
16	The central result is negative: \textbf{at most 1 of 12 auxiliary spatial head configurations exceeds the Vanilla baseline} on Collision Avoidance Rate, and this difference is not statistically significant ($p{=}0.28$); the remaining 11 perform at or below baseline (11/12 $\leq$ Vanilla; $p{\approx}0.003$, binomial test). A $2{\times}2$ factorial subset reveals a pattern consistent with an ordinal interaction: gradient flow degrades safety, BatchNorm amplifies the deficit and increases training instability, and spatial label content is irrelevant (\S\ref{sec:results}).
17	
18	Our contributions are:
19	\begin{enumerate}[nosep,leftmargin=*]
20	    \item \textbf{Negative core finding.} We show that auxiliary spatial supervision does not improve VLA collision avoidance under any of 12 configurations tested. A $2{\times}2$ factorial (gradient flow $\times$ normalization) shows large effect sizes consistent with an ordinal interaction pattern: gradient flow is associated with lower safety under both normalization types, and the BN + gradient flow combination is the most unstable configuration. Spatial label content does not affect outcomes (\S\ref{sec:results}, Table~\ref{tab:main_results}, Figure~\ref{fig:factorial}).
21	
22	    \item \textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first systematic factorial comparison of how auxiliary head design choices interact during VLA fine-tuning. This design can detect interactions that single-factor ablations would miss (\S\ref{sec:ablation}, Table~\ref{tab:ablation_design}).
23	
24	    \item \textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads for the purpose of improving collision avoidance. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN), and never combine BatchNorm with gradient flow. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\S\ref{sec:discussion}).
25	\end{enumera
…[truncated 3 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T02:28:11.048400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "offset": "24",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "offset": "24",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T02:28:11.048532+00:00_

24	\begin{abstract}
25	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates substantially lagging task completion on safety-critical benchmarks.
26	We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance, with twelve conditions varying gradient flow, label content, normalization type, spatial reference frame, and temporal extent.
27	Our central finding is negative: \textbf{at most 1 of 12 auxiliary spatial head configurations exceeds the Vanilla baseline} on Collision Avoidance Rate (CAR), and this difference is not statistically significant ($p{=}0.28$); the remaining 11 perform at or below baseline (11/12 $\leq$ Vanilla; $p{\approx}0.003$, binomial test). A $2{\times}2$ factorial (gradient flow $\times$ normalization) shows a pattern consistent with an ordinal interaction: gradient flow through the auxiliary head into the vision encoders is associated with lower safety ($\Delta{=}-4.2$\,pp within the BatchNorm conditions), and BatchNorm amplifies this deficit compared to LayerNorm. Effect sizes are large but the small-sample design ($n{\leq}4$ per cell) limits pairwise power; the global directional consistency across all twelve conditions provides the primary statistical evidence. The BatchNorm + gradient flow cell is both the worst-performing and the most unstable configuration, with cross-seed standard deviation more than $2.5{\times}$ that of other cells.
28	Gradient analysis confirms orthogonality between action and auxiliary gradients (cosine similarity near zero), ruling out direct gradient conflict. Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) does not affect safety outcomes, indicating that the gradient pathway, not the spatial information, determines the result.
29	Practical guidelines: do not add auxiliary spatial heads for safety purposes. If a
…[truncated 241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-intro-abstract_20260527T022614",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-27T02:28:11.048730+00:00_

全部修订完成，验证通过：

- **Introduction ¶4 (L16)**: 压缩至 ~60w，改用 "at most 1 of 12" + binomial test ($p\approx0.003$)，删除旧 sign test 和 η²/d 数字
- **Introduction C1 (L20)**: "ordinal interaction" → "ordinal interaction pattern"，无 η² 残留
- **Abstract ¶3 (L27)**: 重构为 "at most 1 of 12" + binomial test，LayerNorm 对比改为单侧 $\Delta$，pairwise power 说明改为 "global directional consistency provides the primary statistical evidence"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_revision-intro-abstract_20260527T022614"
}
```

</details>

---
