# paper writing related work

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260526T125941.jsonl`
- **Structured JSON:** [`1fe93b279b6e6a331c90.json`](../../sessions/1f/1fe93b279b6e6a331c90.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-26T13:01:20.833558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T13:01:20.834039+00:00_

1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	
33	@article{li2026vlasafety,
34	  author    = {Li and others},
35	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
36	  journal   = {arXiv preprint arXiv:2604.23775},
37	  year      = {2026},
38	  note      = {arXiv:2604.23775}
39	}
40	
41	% ============================================================
42	% Safety Mechanisms (barrier functions / occupancy-based safety)
43	% ============================================================
44	
45	
46	@article{raja2024ogmcbf,
47	  author    = {Golnaz Raja and Teemu M{\"o}kk{\"o}nen and Reza Ghabcheloo},
48	  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},
49	  journal   = {arXiv preprint
…[truncated 16327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T13:01:20.834293+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/related_work.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T13:01:20.834443+00:00_

artifacts/_project/paper/related_work.tex
docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T13:01:20.834598+00:00_

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
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T13:01:20.834792+00:00_

1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{VLA Safety and Spatial Representations}
6	
7	VLA models achieve high task success but remain prone to collisions~\cite{li2026vlasafety}. Two strategies address this gap. Runtime constraint methods add safety layers at inference: AEGIS~\cite{hu2025vlsa} filters actions via a CBF constructed from vision-language obstacle detection, improving CAR by 59\,pp on SafeLIBERO; CoFreeVLA~\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm settings; and OGM-CBF~\cite{raja2024ogmcbf} builds CBFs from occupancy grid maps. Training-time methods embed safety into the policy: SafeVLA~\cite{zhang2025safevla} applies constrained RL to reduce safety violations by 84\%. Both strategies treat safety as a behavioral constraint problem without investigating whether the VLA's internal spatial representations contribute to collision avoidance.
8	
9	Separately, a growing body of work injects 3D structure into VLA vision encoders to improve task success. Depth-based methods fuse monocular predictions with visual features~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware}, building on foundation models like Depth Anything~\cite{yang2024depthanything}. Alignment-based approaches regularize internal representations: Spatial Forcing~\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features (ICLR 2026); SpatialVLA~\cite{wu2025spatialvla} introduces egocentric 3D position encoding (RSS 2025). Point cloud and geometric methods encode explicit 3D structure~\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}. In autonomous driving, OccVLA~\cite{liu2025occvla} uses occupancy prediction as auxiliary VLA supervision, drawing on BEV representations~\cite{li2022bevformer, sima2023occnet, tian2023occ3d}. These spatial methods consistently improve task success but none evaluates collision avoidan
…[truncated 2903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T13:01:20.835026+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
  "content": "\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{VLA Safety and Spatial Representations}\n\\label{sec:related-safety-spatial}\n\nVision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\\cite{li2026vlasafety}. Existing safety methods fall into two categories. \\emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \\emph{Training-time methods} embed safety into the policy directly: SafeVLA~\\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\\% (NeurIPS 2025 Spotlight). A recent survey~\\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.\n\nA separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\\cite{li2025pointvla,sun2025geovla,wu2026stvla,chen2026gstvla,tu2026sgvla,xiao2026stemvla,li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses voxel occupancy prediction as auxiliary VLA supervision, drawing on BEV and occupancy representations from perception~\\cite{li2022bevformer,sima2023occnet,tian2023occ3d}. All of these spatial methods report improved task success, yet \\emph{none} evaluates their effect on collision avoidance.\n\nOur work addresses this gap: we study whether auxiliary spatial supervision affects safety, and find that it does not improve collision avoidance under any configuration tested.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\\label{sec:related-mtl}\n\nMulti-task learning exploits shared representations across related objectives to improve generalization~\\cite{caruana1997multitask,ruder2017overview}. In overparameterized networks, multi-task training induces implicit $\\ell_{1,2}$ regularization, whereas single-task fine-tuning exhibits nested feature selection that discards unused pretrained features~\\cite{lippl2024implicit}. A parallel line of work addresses gradient conflicts that arise when task gradients oppose each other, proposing surgery and balancing strategies~\\cite{chen2018gradnorm,yu2020pcgrad,liu2021cagrad,navon2022nashmtl}. These methods share a common premise: conflicting gradients must be reconciled for effective joint optimization. Intermediate supervision at hidden layers~\\cite{lee2015deeply} offers an alternative perspective---auxiliary losses inject gradient signal into early layers, shaping feature learning independently of gradient conflict. Gradient starvation~\\cite{pezeshki2021gradient} further shows that removing a gradient source can cause certain feature directions to receive vanishingly small updates, highlighting the sensitivity of representation learning to the set of active losses.\n\nBatch normalization (BN) statistics are known to encode distributional assumptions that, when violated, degrade performance. Li et al.~\\cite{li2017adabn} show that adapting BN running statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves robustness to input corruptions. These findings establish that BN layers act as implicit distribution descriptors, making them a sensitive channel through which auxiliary task gradients can affect the shared representation.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports faster convergence, but does not disentangle the regularization effect of auxiliary gradient flow from the informational content of the spatial signal itself. Our factorial design isolates these factors; we find that gradient flow through the auxiliary head is detrimental to safety regardless of normalization choice, an ordinal interaction that challenges the assumption that spatial supervision should help collision avoidance.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
    "content": "\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{VLA Safety and Spatial Representations}\n\\label{sec:related-safety-spatial}\n\nVision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\\cite{li2026vlasafety}. Existing safety methods fall into two categories. \\emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \\emph{Training-time methods} embed safety into the policy directly: SafeVLA~\\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\\% (NeurIPS 2025 Spotlight). A recent survey~\\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.\n\nA separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\\cite{li2025pointvla,sun2025geovla,wu2026stvla,chen2026gstvla,tu2026sgvla,xiao2026stemvla,li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses voxel occupancy prediction as auxiliary VLA supervision, drawing on BEV and occupancy representations from perception~\\cite{li2022bevformer,sima2023occnet,tian2023occ3d}. All of these spatial methods report improved task success, yet \\emph{none} evaluates their effect on collision avoidance.\n\nOur work addresses this gap: we study whether auxiliary spatial supervision affects safety, and find that it does not improve collision avoidance under any configuration tested.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\\label{sec:related-mtl}\n\nMulti-task learning exploits shared representations across related objectives to improve generalization~\\cite{caruana1997multitask,ruder2017overview}. In overparameterized networks, multi-task training induces implicit $\\ell_{1,2}$ regularization, whereas single-task fine-tuning exhibits nested feature selection that discards unused pretrained features~\\cite{lippl2024implicit}. A parallel line of work addresses gradient conflicts that arise when task gradients oppose each other, proposing surgery and balancing strategies~\\cite{chen2018gradnorm,yu2020pcgrad,liu2021cagrad,navon2022nashmtl}. These methods share a common premise: conflicting gradients must be reconciled for effective joint optimization. Intermediate supervision at hidden layers~\\cite{lee2015deeply} offers an alternative perspective---auxiliary losses inject gradient signal into early layers, shaping feature learning independently of gradient conflict. Gradient starvation~\\cite{pezeshki2021gradient} further shows that removing a gradient source can cause certain feature directions to receive vanishingly small updates, highlighting the sensitivity of representation learning to the set of active losses.\n\nBatch normalization (BN) statistics are known to encode distributional assumptions that, when violated, degrade performance. Li et al.~\\cite{li2017adabn} show that adapting BN running statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves robustness to input corruptions. These findings establish that BN layers act as implicit distribution descriptors, making them a sensitive channel through which auxiliary task gradients can affect the shared representation.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports faster convergence, but does not disentangle the regularization effect of auxiliary gradient flow from the informational content of the spatial signal itself. Our factorial design isolates these factors; we find that gradient flow through the auxiliary head is detrimental to safety regardless of normalization choice, an ordinal interaction that challenges the assumption that spatial supervision should help collision avoidance.\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T13:01:20.835262+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T13:01:20.835407+00:00_

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
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T13:01:20.835570+00:00_

1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{VLA Safety and Spatial Representations}
6	\label{sec:related-safety-spatial}
7	
8	Vision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\cite{li2026vlasafety}. Existing safety methods fall into two categories. \emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\,pp on SafeLIBERO; CoFreeVLA~\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \emph{Training-time methods} embed safety into the policy directly: SafeVLA~\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\% (NeurIPS 2025 Spotlight). A recent survey~\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.
9	
10	A separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\cite{li2025pointvla,sun2025geovla,wu2
…[truncated 3198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260526T125941",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-26T13:01:20.835786+00:00_

文件已写入。内容确认：

- **§2.1** (~500w): VLA safety 线 (AEGIS, SafeVLA, CoFreeVLA, OGM-CBF, survey) + Spatial-VLA 线 (15+ methods across depth/alignment/point-cloud/driving categories) + gap sentence
- **§2.2** (~400w): MTL foundations → implicit regularization → gradient conflict methods → intermediate supervision → gradient starvation → BN sensitivity → LoRA+auxiliary gap → our contribution (ordinal interaction)
- 所有 `\cite{}` keys 均来自 `references.bib`，无 MISSING 占位
- 无违禁词（no "crossover interaction", "BN-mediated gradient calibration", "existence regularization", "gradient collapse"）
- 使用了允许术语 "ordinal interaction" 和 "gradient orthogonality" 相关描述

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260526T125941"
}
```

</details>

---
