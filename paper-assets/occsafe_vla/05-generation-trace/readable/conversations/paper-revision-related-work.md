# paper revision related work

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_revision-related-work_20260527T022539.jsonl`
- **Structured JSON:** [`03584c0e803932c215f4.json`](../../sessions/03/03584c0e803932c215f4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-27T02:28:17.334943+00:00_

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
  "session": "worker_paper_revision-related-work_20260527T022539",
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

_source line 2 · 2026-05-27T02:28:17.335282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T02:28:17.335446+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "occsafe_vla",
  "file": "related_work.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "related_work.tex",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T02:28:17.335581+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'related_work.tex'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T02:28:17.335754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T02:28:17.335910+00:00_

1	
2	\section{Related Work}
3	
4	\subsection{VLA Safety and Spatial Representations}
5	
6	Vision-language-action models achieve high task success but remain collision-prone~\cite{li2026vlasafety}. Safety-oriented approaches either filter actions at inference via control barrier functions~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or embed constraints during training~\cite{zhang2025safevla}; none examines whether spatial representations contribute to safety.
7	
8	A separate line of work enriches VLAs with 3D structure to boost task success: depth fusion~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything}, representation alignment~\cite{li2026spatialforcing, wu2025spatialvla}, explicit geometric encoding~\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}, and occupancy prediction~\cite{liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}. At least fifteen such methods have appeared in the past year, all reporting improved task success; none evaluates collision avoidance. We address this gap.
9	
10	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
11	
12	Multi-task learning exploits shared representations across objectives~\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks can cause negative transfer through both optimization conflict and generalization gap~\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}. In overparameterized networks, multi-task training induces implicit regularization distinct from single-task fine-tuning~\cite{lippl2024implicit}; removing a gradient source can starve certain feature directions~\cite{pezeshki2021gradient}. BatchNorm statistics encode distributional assumptions that degrade performance when violated~\cite{li2017adabn, schneider2020bn}, making BN a sensitive channel for auxiliary task effects. For VLA fine-tuning wi
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T02:28:17.336169+00:00_

called mcp__agent-ml-research__edit_paper_section

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section</summary>

```json
{
  "project": "occsafe_vla",
  "section": "related_work",
  "old_text": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Safety-oriented approaches either filter actions at inference via control barrier functions~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or embed constraints during training~\\cite{zhang2025safevla}; none examines whether spatial representations contribute to safety.\n\nA separate line of work enriches VLAs with 3D structure to boost task success: depth fusion~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything}, representation alignment~\\cite{li2026spatialforcing, wu2025spatialvla}, explicit geometric encoding~\\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}, and occupancy prediction~\\cite{liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}. At least fifteen such methods have appeared in the past year, all reporting improved task success; none evaluates collision avoidance. We address this gap.",
  "new_text": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure---through depth fusion, representation alignment, geometric encoding, or occupancy prediction~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}---yet none evaluates collision avoidance. We address this gap."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "tool_args": {
    "project": "occsafe_vla",
    "section": "related_work",
    "old_text": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Safety-oriented approaches either filter actions at inference via control barrier functions~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or embed constraints during training~\\cite{zhang2025safevla}; none examines whether spatial representations contribute to safety.\n\nA separate line of work enriches VLAs with 3D structure to boost task success: depth fusion~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything}, representation alignment~\\cite{li2026spatialforcing, wu2025spatialvla}, explicit geometric encoding~\\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}, and occupancy prediction~\\cite{liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}. At least fifteen such methods have appeared in the past year, all reporting improved task success; none evaluates collision avoidance. We address this gap.",
    "new_text": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure---through depth fusion, representation alignment, geometric encoding, or occupancy prediction~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}---yet none evaluates collision avoidance. We address this gap."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T02:28:17.336336+00:00_

{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex\", \"version\": 16, \"coverage\": \"0/46\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T02:28:17.336469+00:00_

called mcp__agent-ml-research__edit_paper_section

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section</summary>

```json
{
  "project": "occsafe_vla",
  "section": "related_work",
  "old_text": "Multi-task learning exploits shared representations across objectives~\\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks can cause negative transfer through both optimization conflict and generalization gap~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}. In overparameterized networks, multi-task training induces implicit regularization distinct from single-task fine-tuning~\\cite{lippl2024implicit}; removing a gradient source can starve certain feature directions~\\cite{pezeshki2021gradient}. BatchNorm statistics encode distributional assumptions that degrade performance when violated~\\cite{li2017adabn, schneider2020bn}, making BN a sensitive channel for auxiliary task effects. For VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied; our factorial design isolates gradient flow from spatial content and identifies an ordinal interaction that challenges the assumption that auxiliary spatial supervision should improve safety.",
  "new_text": "Multi-task learning exploits shared representations~\\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks risk negative transfer through optimization conflict or generalization failure~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}, and BatchNorm layers are sensitive to the distributional shifts they introduce~\\cite{li2017adabn, schneider2020bn}. For VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied; our factorial design isolates gradient flow from spatial content and identifies an ordinal interaction that challenges the assumption that auxiliary spatial supervision should improve safety."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "tool_args": {
    "project": "occsafe_vla",
    "section": "related_work",
    "old_text": "Multi-task learning exploits shared representations across objectives~\\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks can cause negative transfer through both optimization conflict and generalization gap~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}. In overparameterized networks, multi-task training induces implicit regularization distinct from single-task fine-tuning~\\cite{lippl2024implicit}; removing a gradient source can starve certain feature directions~\\cite{pezeshki2021gradient}. BatchNorm statistics encode distributional assumptions that degrade performance when violated~\\cite{li2017adabn, schneider2020bn}, making BN a sensitive channel for auxiliary task effects. For VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied; our factorial design isolates gradient flow from spatial content and identifies an ordinal interaction that challenges the assumption that auxiliary spatial supervision should improve safety.",
    "new_text": "Multi-task learning exploits shared representations~\\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks risk negative transfer through optimization conflict or generalization failure~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}, and BatchNorm layers are sensitive to the distributional shifts they introduce~\\cite{li2017adabn, schneider2020bn}. For VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied; our factorial design isolates gradient flow from spatial content and identifies an ordinal interaction that challenges the assumption that auxiliary spatial supervision should improve safety."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T02:28:17.336613+00:00_

{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex\", \"version\": 17, \"coverage\": \"0/46\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "mcp__agent-ml-research__edit_paper_section",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T02:28:17.336806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T02:28:17.336943+00:00_

1	
2	\section{Related Work}
3	
4	\subsection{VLA Safety and Spatial Representations}
5	
6	Vision-language-action models achieve high task success but remain collision-prone~\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure---through depth fusion, representation alignment, geometric encoding, or occupancy prediction~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}---yet none evaluates collision avoidance. We address this gap.
7	
8	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
9	
10	Multi-task learning exploits shared representations~\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks risk negative transfer through optimization conflict or generalization failure~\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}, and BatchNorm layers are sensitive to the distributional shifts they introduce~\cite{li2017adabn, schneider2020bn}. For VLA fine-tuning with LoRA~\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied; our factorial design isolates gradient flow from spatial content and identifies an ordinal interaction that challenges the assumption that auxiliary spatial supervision should improve safety.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_revision-related-work_20260527T022539",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-27T02:28:17.337111+00:00_

完成。修改摘要：

**§2.1 (5句→4句)**：
- Safety 方法合并为 1 句 bulk citation（移除按 inference/training 分列的两个 `\cite`，合并为一个）
- Spatial-VLA 方法：4 个分类各带独立 citation → 1 句枚举分类 + 单个合并 `\cite{...19 papers...}`，用 em-dash 包裹
- 删除 "At least fifteen such methods" 独立句，将 "yet none evaluates collision avoidance" 嵌入前句

**§2.2 (4句→2句)**：
- 删除 implicit regularization 句（`lippl2024implicit`）
- 删除 gradient starvation 描述（`pezeshki2021gradient`）
- BN sensitivity 从独立句吸收进第一句末尾，用逗号连接
- LoRA gap statement 保持不变（已是 1 句）

所有引用保留（除 `lippl2024implicit` 和 `pezeshki2021gradient` 随删除内容移除），三个覆盖要求（VLA safety 现有工作、auxiliary objectives 影响、本文 gap）均满足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_revision-related-work_20260527T022539"
}
```

</details>

---
