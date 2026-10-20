# paper writing introduction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260516T022839.jsonl`
- **Structured JSON:** [`8610d73b998c297e5f16.json`](../../sessions/86/8610d73b998c297e5f16.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-16T02:30:23.511610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:30:23.512160+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We report Spearman rank correlation $\rho$ betwee
…[truncated 13148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:30:23.512374+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:30:23.512516+00:00_

artifacts/_project/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:30:23.512658+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper framing files",
  "prompt": "Search for paper_framing.md or any framing/story document in the vla-ssd project. Check paths like /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ and subdirectories. Also look for references.bib. Report file paths found and key content snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find paper framing files",
    "prompt": "Search for paper_framing.md or any framing/story document in the vla-ssd project. Check paths like /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ and subdirectories. Also look for references.bib. Report file paths found and key content snippets."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T02:30:23.512808+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper_framing.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T02:30:23.513116+00:00_

artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md
paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T02:30:23.513362+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T02:30:23.513531+00:00_

docs/paper/references.bib
artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T02:30:23.513669+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*framing*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*framing*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T02:30:23.513791+00:00_

artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md
paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T02:30:23.513940+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*story*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*story*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T02:30:23.514104+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T02:30:23.514239+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -type f -name \"*.md\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -type f -name \"*.md\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T02:30:23.514364+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/director/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778877858.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_4_1778887654.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778866326.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778878478.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778865132.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778867412.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_4_1778895396.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778878475.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778889604.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778875986.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778863795.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_4_1778886984.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ta
…[truncated 159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T02:30:23.514516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T02:30:23.514700+00:00_

1	# Paper Framing — vla-ssd
2	
3	## Target Venue
4	- Primary: CoRL 2026
5	- Deadline: Abstract May 26, Paper May 29
6	- Format: 8 pages + references
7	
8	## Core Claims (3 条)
9	
10	1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA 中 action-relevant 表征结构由 frozen vision encoder 决定。RSA geometric alignment: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388)——VL pretrained encoders 显著优于 vision-only。但 functional capacity (R²) 方向相反: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587)。**Geometric alignment 和 predictive capacity 是可分离的独立维度**。VL pretraining 提供 geometric alignment（表征结构匹配 action 空间），不增加甚至略降低 functional capacity。
11	2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.630→0.599, p<0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.671 > projector 0.630, p=0.002），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector）。Readout concentration 是 learned behavior，不是架构固有属性。
12	3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。
13	
14	## Paper 主数值基准（image_mean 聚合，公平对比）
15	
16	| Model / Condition | RSA (image_mean) | Notes |
17	|---|---|---|
18	| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |
19	| VLA trained with-inst | 0.501 | Peak L23 |
20	| VLA untrained with-inst | 0.485 | Peak L23 |
21	| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |
22	| VLA untrained no-inst | 0.482 | Peak L29 |
23	| **CLIP ViT-L/14** | **0.557** | VL-pretrained control, CI=[0.442, 0.660] |
24	| DINO-V2 | 0.388 | Vision-only
…[truncated 10428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T02:30:23.514860+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T02:30:23.515043+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	% [VERIFY] Confirm venue and exact title. Likely "Prismatic VLMs" or OpenVLA architecture companion.
11	@article{karamcheti2024,
12	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
13	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
14	  journal   = {arXiv preprint arXiv:2402.07865},
15	  year      = {2024},
16	}
17	
18	@article{brohan2023_rt2,
19	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
20	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
21	  journal   = {arXiv preprint arXiv:2307.15818},
22	  year      = {2023},
23	}
24	
25	% === Benchmark ===
26	
27	@inproceedings{liu2023_libero,
28	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
29	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
30	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
31	  year      = {2023},
32	}
33	
34	% === Representation Analysis Methods ===
35	
36	@article{kriegeskorte2008,
37	  title     = {Representational Similarity Analysis -- Connecting 
…[truncated 2717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T02:30:23.515213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T02:30:23.515355+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	% [VERIFY] Confirm venue and exact title. Likely "Prismatic VLMs" or OpenVLA architecture companion.
11	@article{karamcheti2024,
12	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
13	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
14	  journal   = {arXiv preprint arXiv:2402.07865},
15	  year      = {2024},
16	}
17	
18	@article{brohan2023_rt2,
19	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
20	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
21	  journal   = {arXiv preprint arXiv:2307.15818},
22	  year      = {2023},
23	}
24	
25	% === Benchmark ===
26	
27	@inproceedings{liu2023_libero,
28	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
29	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
30	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
31	  year      = {2023},
32	}
33	
34	% === Representation Analysis Methods ===
35	
36	@article{kriegeskorte2008,
37	  title     = {Representational Similarity Analysis -- Connecting 
…[truncated 2682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T02:30:23.515510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T02:30:23.515663+00:00_

1	# Paper Framing — vla-ssd
2	
3	## Target Venue
4	- Primary: CoRL 2026
5	- Deadline: Abstract May 26, Paper May 29
6	- Format: 8 pages + references
7	
8	## Core Claims (3 条)
9	
10	1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.488）和 standalone vision model（DINOv2 ρ=0.388）。
11	2. **LLM Degrades Action Alignment**: LLM processing 降低而非增强 action-relevant 几何结构（0.615→0.488）。这一 degradation 在 trained/untrained、with/without instruction 四种条件下一致发生。
12	3. **Training and Instruction Invariance**: VLA task-specific fine-tuning（Δ<0.01）和 instruction input（Δ<0.005）均不显著改变 LLM hidden state 中的 action-relevant 表征结构。2×2 matrix（training × instruction）四格收敛于 0.48-0.49。
13	
14	## Story Spine
15	
16	- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。
17	- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。
18	- **Our framing**: 首次对 VLA 进行系统性 representational analysis——7 种 probing 方法 × 2 benchmarks × 组件级分解，定量揭示 action-relevant 结构的来源。发现 LLM 不仅不贡献，反而 degrades vision encoder 提供的 action alignment。
19	- **Headline result**: "SigLIP+projector representations achieve RSA ρ=0.615 with action structure, while the full VLA only achieves ρ≈0.488 regardless of training or instruction — the LLM degrades rather than enhances action-relevant representations."
20	
21	## Anticipated Reviewer Concerns & Responses
22	
23	### C1: 单一 VLA 架构（OpenVLA）泛化性
24	- **应对**: Scope 明确限定为 "OpenVLA-class architecture"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。
25	- **实验**: 无需额外实验，Limitations 明确标注。
26	
27	### C2: SigLIP vs DINOv2 pretraining confound
28	- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-sup
…[truncated 2272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T02:30:23.515819+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ | head -30"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T02:30:23.515975+00:00_

total 328K
drwxr-xr-x  9 ubuntu ubuntu 4.0K May 16 02:21 .
drwxrwxr-x  5 ubuntu ubuntu 4.0K May 15 04:32 ..
drwxr-xr-x  3 ubuntu ubuntu 4.0K May 15 04:32 .claude
-rw-------  1 ubuntu ubuntu    0 May 15 17:07 .registry_veak6jl2.tmp
-rw-r--r--  1 ubuntu ubuntu  13K May 16 02:28 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu    0 May 15 04:34 ROADMAP.lock
-rw-------  1 ubuntu ubuntu 4.1K May 16 02:14 ROADMAP.md
drwxr-xr-x 10 ubuntu ubuntu 4.0K May 16 02:09 artifacts
drwxr-xr-x  2 ubuntu ubuntu  32K May 16 02:17 checkpoints
-rw-r--r--  1 ubuntu ubuntu    0 May 15 19:40 constraints.lock
-rw-------  1 ubuntu ubuntu  440 May 15 19:40 constraints.yaml
-rw-r--r--  1 ubuntu ubuntu    0 May 15 11:03 decisions.lock
-rw-------  1 ubuntu ubuntu  43K May 16 02:14 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu 4.0K May 15 05:23 docs
-rwxr-xr-x  1 ubuntu ubuntu    0 May 15 05:23 dream_registry.lock
-rw-------  1 ubuntu ubuntu 1.9K May 16 01:59 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu 1.9K May 16 01:59 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 5.3K May 16 01:41 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  29K May 16 02:15 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu 4.0K May 15 04:56 logs
-rw-r--r--  1 ubuntu ubuntu 6.2K May 16 02:14 memory.md
-rw-r--r--  1 ubuntu ubuntu  15K May 16 02:21 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu    0 May 15 04:55 registry.lock
-rw-------  1 ubuntu ubuntu  83K May 16 02:20 registry.yaml
-rw-r--r--  1 ubuntu ubuntu 1.9K May 16 02:17 report.md
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 15 19:16 scripts
-rwxr-xr-x  1 ubuntu ubuntu    0 May 15 04:33 study_status.lock
drwxr-xr-x  3 ubuntu ubuntu 4.0K May 16 02:28 task_context
-rw-r--r--  1 ubuntu ubuntu  27K May 16 02:09 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T02:30:23.516187+00:00_

Perfect. I've found all the framing and bibliography files. Let me provide you with a comprehensive report.

## Summary of Findings

I found three key document types in the vla-ssd project:

### Paper Framing Documents Located

**Main file:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md`

**Dream report variants (historical iterations):**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md`

### Bibliography Files Located

**Main BibTeX file:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib`

**Archived version:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib`

---

### Key Content Snippets

**Main Paper Framing:**
The primary framing document is comprehensive and highly detailed. The core contribution is a **three-claim architecture**:

1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA action-relevant representations are determined by frozen vision encoder (SigLIP). Representational Similarity Analysis shows: SigLIP (RSA ρ=0.615) > CLIP (0.557) >> DINO (0.388). But action prediction capacity (R²) shows opposite ordering: DINO (
…[truncated 2507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Agent",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:30:23.516343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T02:30:23.516516+00:00_

1	# Paper Framing — vla-ssd
2	
3	## Target Venue
4	- Primary: CoRL 2026
5	- Deadline: Abstract May 26, Paper May 29
6	- Format: 8 pages + references
7	
8	## Core Claims (3 条)
9	
10	1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA 中 action-relevant 表征结构由 frozen vision encoder 决定。RSA geometric alignment: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388)——VL pretrained encoders 显著优于 vision-only。但 functional capacity (R²) 方向相反: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587)。**Geometric alignment 和 predictive capacity 是可分离的独立维度**。VL pretraining 提供 geometric alignment（表征结构匹配 action 空间），不增加甚至略降低 functional capacity。
11	2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.630→0.599, p<0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.671 > projector 0.630, p=0.002），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector）。Readout concentration 是 learned behavior，不是架构固有属性。
12	3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。
13	
14	## Paper 主数值基准（image_mean 聚合，公平对比）
15	
16	| Model / Condition | RSA (image_mean) | Notes |
17	|---|---|---|
18	| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |
19	| VLA trained with-inst | 0.501 | Peak L23 |
20	| VLA untrained with-inst | 0.485 | Peak L23 |
21	| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |
22	| VLA untrained no-inst | 0.482 | Peak L29 |
23	| **CLIP ViT-L/14** | **0.557** | VL-pretrained control, CI=[0.442, 0.660] |
24	| DINO-V2 | 0.388 | Vision-only
…[truncated 5489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T02:30:23.516711+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\\cite{karamcheti2024}.\nAn implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.\nBut where do action representations actually come from?\nDo they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?\n\nRecent work reveals cracks in this assumption.\nGrant et al.~\\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.\nIndependently, Hou et al.~\\cite{hou2026} and Fei et al.~\\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.\nThese findings challenge the prevailing narrative but remain at the behavioral level---they reveal \\emph{what} drives VLA outputs without explaining \\emph{where} action-relevant structure resides in the representation space.\nNo prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.\nWithout this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.\n\nWe present the first systematic representational and functional analysis of a VLA.\nTaking OpenVLA-7B~\\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\\cite{zhai2023_siglip} with MLP projector, every layer of the Llama-2 7B backbone, and the readout token position.\nWe apply Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to measure geometric alignment with the action space and train functional probes to measure action decodability.\nA $2 \\times 2$ factorial design crossing training status (trained vs.\\ untrained LLM) with instruction presence (with vs.\\ without) isolates each factor's contribution.\nExternal baselines---DINOv2~\\cite{oquab2024_dinov2} (vision-only) and CLIP ViT-L/14~\\cite{radford2021_clip} (vision-language pretrained, no VLA training)---anchor our comparisons.\n\nThree findings emerge from experiments on the LIBERO-Goal benchmark~\\cite{liu2023_libero}.\n\\textbf{First}, frozen vision-language encoders provide the dominant action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$), followed by CLIP ($\\rho = 0.557$), both far exceeding the vision-only DINOv2 ($\\rho = 0.388$).\nYet DINOv2 matches SigLIP+Projector in action prediction capacity ($R^2 = 0.712$ vs.\\ $0.706$, $p = 0.22$), revealing a geometric-functional dissociation: VL pretraining provides geometric alignment with the action space without increasing raw decodability.\n\\textbf{Second}, the LLM degrades distributed geometric alignment (RSA $0.615 \\to 0.501$) but concentrates a functionally superior signal at the readout token ($R^2 = 0.731$, exceeding the projector's $0.706$).\nThis concentration is training-dependent: an untrained LLM's readout achieves only $R^2 = 0.686$, falling below the projector baseline.\n\\textbf{Third}, training teaches routing, not creating.\nDistributed RSA is training-invariant ($\\Delta = 0.021$, 95\\% CI includes zero, $p = 0.20$), while readout concentration shows a large training effect ($\\Delta = 0.045$, $p < 0.0001$).\nLanguage instructions affect neither metric.\n\nThese results reframe how we understand VLA representations and carry direct design implications: vision encoder pretraining quality---not LLM fine-tuning---is the primary lever for action-relevant structure~\\cite{haon2025}.\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item The first systematic representational decomposition of a VLA, quantifying each component's contribution to action-relevant structure with both geometric (RSA) and functional (probe $R^2$) metrics.\n    \\item Discovery of a geometric-functional dissociation: vision-language pretraining provides geometric alignment with the action space beyond what raw information content predicts, while vision-only features are functionally rich but geometrically dissimilar.\n    \\item Evidence that LLM fine-tuning teaches information routing---concentrating pre-existing vision-encoder structure at the readout position---rather than creating new action-relevant representations.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\\cite{karamcheti2024}.\nAn implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.\nBut where do action representations actually come from?\nDo they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?\n\nRecent work reveals cracks in this assumption.\nGrant et al.~\\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.\nIndependently, Hou et al.~\\cite{hou2026} and Fei et al.~\\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.\nThese findings challenge the prevailing narrative but remain at the behavioral level---they reveal \\emph{what} drives VLA outputs without explaining \\emph{where} action-relevant structure resides in the representation space.\nNo prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.\nWithout this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.\n\nWe present the first systematic representational and functional analysis of a VLA.\nTaking OpenVLA-7B~\\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\\cite{zhai2023_siglip} with MLP projector, every layer of the Llama-2 7B backbone, and the readout token position.\nWe apply Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to measure geometric alignment with the action space and train functional probes to measure action decodability.\nA $2 \\times 2$ factorial design crossing training status (trained vs.\\ untrained LLM) with instruction presence (with vs.\\ without) isolates each factor's contribution.\nExternal baselines---DINOv2~\\cite{oquab2024_dinov2} (vision-only) and CLIP ViT-L/14~\\cite{radford2021_clip} (vision-language pretrained, no VLA training)---anchor our comparisons.\n\nThree findings emerge from experiments on the LIBERO-Goal benchmark~\\cite{liu2023_libero}.\n\\textbf{First}, frozen vision-language encoders provide the dominant action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$), followed by CLIP ($\\rho = 0.557$), both far exceeding the vision-only DINOv2 ($\\rho = 0.388$).\nYet DINOv2 matches SigLIP+Projector in action prediction capacity ($R^2 = 0.712$ vs.\\ $0.706$, $p = 0.22$), revealing a geometric-functional dissociation: VL pretraining provides geometric alignment with the action space without increasing raw decodability.\n\\textbf{Second}, the LLM degrades distributed geometric alignment (RSA $0.615 \\to 0.501$) but concentrates a functionally superior signal at the readout token ($R^2 = 0.731$, exceeding the projector's $0.706$).\nThis concentration is training-dependent: an untrained LLM's readout achieves only $R^2 = 0.686$, falling below the projector baseline.\n\\textbf{Third}, training teaches routing, not creating.\nDistributed RSA is training-invariant ($\\Delta = 0.021$, 95\\% CI includes zero, $p = 0.20$), while readout concentration shows a large training effect ($\\Delta = 0.045$, $p < 0.0001$).\nLanguage instructions affect neither metric.\n\nThese results reframe how we understand VLA representations and carry direct design implications: vision encoder pretraining quality---not LLM fine-tuning---is the primary lever for action-relevant structure~\\cite{haon2025}.\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item The first systematic representational decomposition of a VLA, quantifying each component's contribution to action-relevant structure with both geometric (RSA) and functional (probe $R^2$) metrics.\n    \\item Discovery of a geometric-functional dissociation: vision-language pretraining provides geometric alignment with the action space beyond what raw information content predicts, while vision-only features are functionally rich but geometrically dissimilar.\n    \\item Evidence that LLM fine-tuning teaches information routing---concentrating pre-existing vision-encoder structure at the readout position---rather than creating new action-relevant representations.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T02:30:23.516891+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T02:30:23.517045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T02:30:23.517171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T02:30:23.517301+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T02:30:23.517418+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T02:30:23.517571+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T02:30:23.517689+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T02:30:23.517802+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "mcp agent-ml-research",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "mcp agent-ml-research",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T02:30:23.517937+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T02:30:23.518073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T02:30:23.518220+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\cite{brohan2023_rt2,kim2024_openvla}.
5	The dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\cite{karamcheti2024}.
6	An implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.
7	But where do action representations actually come from?
8	Do they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?
9	
10	Recent work reveals cracks in this assumption.
11	Grant et al.~\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.
12	Independently, Hou et al.~\cite{hou2026} and Fei et al.~\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.
13	These findings challenge the prevailing narrative but remain at the behavioral level---they reveal \emph{what} drives VLA outputs without explaining \emph{where} action-relevant structure resides in the representation space.
14	No prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.
15	Without this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.
16	
17	We present the first systematic representational and functional analysis of a VLA.
18	Taking OpenVLA-7B~\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\cite{zhai2023_s
…[truncated 2967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T022839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-16T02:30:23.518403+00:00_

`introduction.tex` 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex`。

5 段结构：Problem → Gap → Approach → Findings (with headline numbers) → Implications + 3 contributions（enumerate）。约 ~650 词，符合 1-1.5 页目标。所有引用 key 均按指定使用，包括 `hou2026` 和 `fei2025`。数值用 p0_probe_v2 口径（R² 0.706/0.683/0.731/0.686，RSA 0.615/0.557/0.388）。

`register_artifact` 工具不在当前可用 MCP 工具列表中，无法注册。如需注册请手动操作或确认工具名称。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260516T022839"
}
```

</details>

---
