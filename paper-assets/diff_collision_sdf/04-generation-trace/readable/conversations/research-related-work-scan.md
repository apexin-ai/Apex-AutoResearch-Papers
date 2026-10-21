# research related work scan

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_research_related_work_scan_20260527T220506.jsonl`
- **Structured JSON:** [`a553021339e03c56cf8e.json`](../../sessions/a5/a553021339e03c56cf8e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-27T22:07:37.634805+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T22:07:37.635120+00:00_

docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/archive/analysis_claim4.tex
docs/paper/archive/analysis_claim2.tex
docs/paper/archive/analysis_claim1.tex
docs/paper/archive/analysis_claim3.tex
docs/paper/contingency_claim3.tex
docs/paper/experimental_framework.tex
docs/paper/main.tex
docs/paper/claim1.tex
docs/paper/claim2.tex
docs/paper/related_work.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/claim3.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T22:07:37.635292+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T22:07:37.635447+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T22:07:37.635580+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T22:07:37.635700+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T22:07:37.635817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T22:07:37.635958+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. Recent extensions to configuration space~\cite{chen2026cssdfnet} and model predictive control~\cite{jacquet2025neuralnmpc} demonstrate effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored. Most methods query the SDF a
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T22:07:37.636113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T22:07:37.636322+00:00_

1	% The Safety Illusion — References
2	% Analysis paper on fake safety in VLA collision avoidance evaluation
3	% Generated: 2026-05-24
4	
5	% ===== VLA Foundation Models =====
6	
7	@article{black2024pi0,
8	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
9	  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
10	  journal={arXiv preprint arXiv:2410.24164},
11	  year={2024}
12	}
13	
14	@inproceedings{kim2024openvla,
15	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
16	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},
17	  booktitle={Conference on Robot Learning (CoRL)},
18	  year={2024}
19	}
20	
21	@inproceedings{brohan2023rt2,
22	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
23	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
24	  booktitle={Conference on Robot Learning (CoRL)},
25	  year={2023}
26	}
27	
28	% ===== Collision-Aware VLA Methods =====
29	
30	@article{hu2025vlsa,
31	  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
32	  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},
33	  journal={arXiv preprint arXiv:2512.11891},
34	  year={2025}
35	}
36	
37	@inproceedings{zhang2025safevla,
38	  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
39	  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},
40	  boo
…[truncated 8360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T22:07:37.636694+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T22:07:37.637089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T22:07:37.637327+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA safety vision-language-action model safe manipulation 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA safety vision-language-action model safe manipulation 2024 2025 paper"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T22:07:37.637557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "robot collision avoidance learning neural network 2024 2025 ICRA CoRL NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "robot collision avoidance learning neural network 2024 2025 ICRA CoRL NeurIPS"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T22:07:37.637743+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "signed distance field robot manipulation learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "signed distance field robot manipulation learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T22:07:37.637931+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safe imitation learning robot manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safe imitation learning robot manipulation 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T22:07:37.638146+00:00_

Web search results for query: "VLA safety vision-language-action model safe manipulation 2024 2025 paper"

Links: [{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"Paper page - VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://huggingface.co/papers/2512.11891"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"SafeVLA: Towards Safety Alignment of Vision- Language-Action Model via Constrained Learning","url":"https://arxiv.org/html/2503.03480v2"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://arxiv.org/pdf/2601.15541"}]

Based on the search results, I found several relevant papers on VLA (Vision-Language-Action) models with safety considerations for robotic manipulation in 2024-2025:

## Key Papers Found:

### 1. SafeVLA: Towards Safety Alignment of Vision-Language-Action Model
This paper achieved an 83.58% improvement in safety-performance trade-offs, reducing the cumulative cost of safety violations with no performance loss. SafeVLA explicitly incorporates safety within a constrained learning framework, ensuring that safety constraints are prioritized and satisfied. The aligned policies showed robust safety assurance, mitigating long-tail risks and generalizing to out-of-distribution perturbations and extreme failures, marking a first systematic integration of 
…[truncated 1098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T22:07:37.638398+00:00_

Web search results for query: "signed distance field robot manipulation learning 2024 2025"

Links: [{"title":"Configuration Space Distance Fields for Manipulation ...","url":"https://www.roboticsproceedings.org/rss20/p131.pdf"},{"title":"Geometric Structures for Learning and Optimization in Robotics | Annual Reviews","url":"https://www.annualreviews.org/content/journals/10.1146/annurev-control-022624-013742"},{"title":"(PDF) Learning Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://www.researchgate.net/publication/372074663_Learning_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"},{"title":"Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Request PDF","url":"https://www.researchgate.net/publication/373665800_Collision-Free_Motion_Generation_Based_on_Stochastic_Optimization_and_Composite_Signed_Distance_Field_Networks_of_Articulated_Robot"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382979799_Representing_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://arxiv.org/pdf/2204.02296"},{"title":"Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/pdf/2406.01137"},{"title":"Learning Models as Functionals of Signed-Distance Fields for   Manipulation Planning","url":"https://arxiv.org/pdf/2110.00792"},{"title":"Representing Robot Geometry as D
…[truncated 1761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T22:07:37.638686+00:00_

Web search results for query: "robot collision avoidance learning neural network 2024 2025 ICRA CoRL NeurIPS"

Links: [{"title":"Uncertainty-Aware Reinforcement Learning for Collision Avoidance","url":"https://arxiv.org/pdf/1702.01182"},{"title":"Distributed Non-Communicating Multi-Robot Collision Avoidance via Map-Based Deep Reinforcement Learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7506975/"},{"title":"Publications | IRoM-Lab - Princeton University","url":"https://irom-lab.princeton.edu/publications/"},{"title":"CoRL-MPPI: Enhancing MPPI With Learnable Behaviours For Efficient And Provably-Safe Multi-Robot Collision Avoidance","url":"https://arxiv.org/pdf/2511.09331"},{"title":"Deep Reinforcement Learning with anticipatory reward in LSTM for Collision Avoidance of Mobile Robots","url":"https://arxiv.org/pdf/2508.07941"},{"title":"Fully Distributed Multi-Robot Collision Avoidance via Deep Reinforcement   Learning for Safe and Efficient Navigation in Complex Scenarios","url":"https://arxiv.org/pdf/1808.03841"},{"title":"Collision Avoidance in Pedestrian-Rich Environments with Deep   Reinforcement Learning","url":"https://arxiv.org/pdf/1910.11689"},{"title":"Accelerated Sim-to-Real Deep Reinforcement Learning: Learning Collision   Avoidance from Human Player","url":"https://arxiv.org/pdf/2102.10711"}]

Based on the search results, here are relevant recent developments in robot collision avoidance using neural networks and learning:

## Recent Work (2024-2025)

CoRL-MPPI is a recent approach that combines Cooperative Reinforcement Learning with Model Predictive Path Integral (MPPI) for decentralized multi-robot collision avoidance, introducing a fusion that addresses limitations of purely random sampling in MPPI-based controllers. This work trains an action policy approximated as a deep neural network to learn local cooperative collision avoidance behaviors.

Another 2024 approach proposes a collision risk anticipation method using Long Short-Term Mem
…[truncated 1130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T22:07:37.638950+00:00_

Web search results for query: "safe imitation learning robot manipulation 2024 2025"

Links: [{"title":"A Survey on Imitation Learning for Contact-Rich Tasks in Robotics","url":"https://arxiv.org/html/2506.13498v1"},{"title":"RoboCopilot: Human-in-the-loop Interactive Imitation Learning for Robot Manipulation","url":"https://arxiv.org/html/2503.07771v1"},{"title":"Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12757213/"},{"title":"Towards cost-effective and safe contact-rich robotic manipulation with reinforcement learning: A review of techniques for future industrial automation - Anselmo Parnada, Mo Qu, Marco Castellani, Hyung Jin Chang, Yongjing Wang, 2026","url":"https://journals.sagepub.com/doi/10.1177/09596518251350353"},{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"}]

I found several relevant research results on safe imitation learning for robot manipulation. Here's a summary of the recent developments:

## Key Recent Advances (2024-2025)

**Novel Approaches to Imitation Learning:**

The self-corrected (SC-)-VLA framework enhances manipulation robustness by combining a fast action predictor with a slow, reflective system that uses Chain-of-Thought reasoning to correct failures step by step.

The Mamba model, a state-space model capable of handling long sequences with greater efficiency, improves generalization under limited data by focusing on salient features.

RoboFlamingo uses an existing VLM by incorporating an explicit policy head, and is fine-tuned by imitation learning only on language-conditioned manipulation datasets.

**Safety and Interactive Imitation Learning:**

Interactive imitation learning (IIL) can address sample efficiency, safety, and robustness in re
…[truncated 705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-27T22:07:37.639192+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CompliantVLA impedance control VLA safe contact manipulation 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CompliantVLA impedance control VLA safe contact manipulation 2025 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T22:07:37.639372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"configuration space distance field\" robot SDF manipulation planning RSS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"configuration space distance field\" robot SDF manipulation planning RSS 2024"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T22:07:37.639541+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA Pi0 safety collision avoidance evaluation benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA Pi0 safety collision avoidance evaluation benchmark 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-27T22:07:37.639668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "diffusion policy safety constraint collision aware manipulation 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "diffusion policy safety constraint collision aware manipulation 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T22:07:37.639817+00:00_

Web search results for query: ""configuration space distance field" robot SDF manipulation planning RSS 2024"

Links: [{"title":"[2406.01137] Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/abs/2406.01137"},{"title":"Configuration Space Distance Fields for Manipulation Planning · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/program/papers/131/"},{"title":"[PDF] Configuration Space Distance Fields for Manipulation Planning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Configuration-Space-Distance-Fields-for-Planning-Li-Chi/75af8f157566854a49e72ead68f807166b791809"},{"title":"Configuration Space Distance Fields","url":"https://sites.google.com/view/cdfmp/home"},{"title":"Robotics: Science and Systems XX - Online Proceedings","url":"https://www.roboticsproceedings.org/rss20/p131.html"},{"title":"(PDF) Configuration Space Distance Fields for Manipulation Planning","url":"https://www.researchgate.net/publication/383891276_Configuration_Space_Distance_Fields_for_Manipulation_Planning"},{"title":"Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://arxiv.org/html/2503.04929"},{"title":"Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/pdf/2406.01137"},{"title":"Configuration Space Distance Fields for Manipulation Planning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240601137L/abstract"}]

Based on the search results, I found relevant information about this topic:

The paper introduces "Configuration Space Distance Fields" (CDF), which applies SDFs in the robot configuration space for optimization. This work by Yiming Li, Xuemin Chi, Amirreza Razmjoo, and Sylvain Calinon was presented at Robotics: Science and Systems (RSS) 2024 in Delft, Netherlands.

The signed distance field (SDF) is a popular implicit shape representation in robotics that provides geometric information about objects and obstacles i
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T22:07:37.639986+00:00_

Web search results for query: "CompliantVLA impedance control VLA safe contact manipulation 2025 2026 arxiv"

Links: [{"title":"CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://arxiv.org/html/2601.15541v1"},{"title":"(PDF) CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://www.researchgate.net/publication/400002803_CompliantVLA-adaptor_VLM-Guided_Variable_Impedance_Action_for_Safe_Contact-Rich_Manipulation"},{"title":"[2601.15541] CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://arxiv.org/abs/2601.15541"},{"title":"CompliantVLA-adaptor: VLM-Guided Variable Impedance ...","url":"https://arxiv.org/pdf/2601.15541"},{"title":"[2109.12103] RMPs for Safe Impedance Control in Contact-Rich Manipulation","url":"https://arxiv.org/abs/2109.12103"}]

I found the research paper you're looking for. Here's what I found:

CompliantVLA-adaptor is a system that augments Vision-Language-Action (VLA) models with vision-language model (VLM)-informed context-aware variable impedance control (VIC) to improve the safety and effectiveness of contact-rich robotic manipulation tasks.

Existing VLA systems like RDT, Pi0.5, and OpenVLA-oft typically output position but lack force-aware adaptation, leading to unsafe or failed interactions in physical tasks involving contact, compliance, or uncertainty.

In CompliantVLA-adaptor, a VLM interprets task context from images and natural language to adapt the stiffness and damping parameters of a VIC controller, with these parameters further regulated using real-time force/torque feedback to ensure interaction forces remain within safe thresholds.

The method outperforms VLA baselines on a suite of complex contact-rich tasks in both simulation and the real world, with improved success rates and reduced force violations.

The paper was published on arXiv (arxiv 2601.15541) in
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T22:07:37.640160+00:00_

Web search results for query: "OpenVLA Pi0 safety collision avoidance evaluation benchmark 2025 2026"

Links: [{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775v1"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"Adversarial Reinforcement Learning Framework for Benchmarking Collision   Avoidance Mechanisms in Autonomous Vehicles","url":"https://arxiv.org/pdf/1806.01368"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"arXiv:2505.05540v2 [cs.CV] 17 Jun 2025","url":"https://arxiv.org/pdf/2505.05540"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"VLA Leaderboard 2026: RT-2 vs OpenVLA vs Pi0 vs Octo (Robotics Benchmarks) | Codesota | CodeSOTA","url":"https://www.codesota.com/robotics"},{"title":"Survey of Autonomous Vehicles’ Collision Avoidance Algorithms","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11769269/"}]

Based on the web search results, here's what I found regarding OpenVLA, Pi0, and safety collision avoidance evaluation benchmarks in 2025-2026:

## Safety Benchmarks and Evaluation

Pi0.5 and OpenVLA-OFT achieved an average collision avoidance rate (CAR) of only 18.69% and 15.13% respectively in complex environments, with performance dropping to 12.75% and 5.50% in the SafeLIBERO-Long suite, indicating that these models struggle significantly with collision avoidance in safety-critical scenarios.

## SafeLIBERO Benchmark

A SafeLIBERO benchmark is being used to evaluate performance, with models being assessed under identical conditions. The evaluation metrics include collision
…[truncated 781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-27T22:07:37.640332+00:00_

Web search results for query: "diffusion policy safety constraint collision aware manipulation 2024 2025 arxiv"

Links: [{"title":"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation","url":"https://arxiv.org/html/2407.00451v2"},{"title":"[2407.00451] Language-Guided Object-Centric Diffusion Policy for Generalizable and Collision-Aware Robotic Manipulation","url":"https://arxiv.org/abs/2407.00451"},{"title":"SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation","url":"https://arxiv.org/pdf/2508.18268"},{"title":"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance","url":"https://arxiv.org/pdf/2511.22773"},{"title":"Diffusion-Based Planning for Trajectory Optimization","url":"https://www.emergentmind.com/topics/diffusion-based-planning"},{"title":"Language-Guided Object-Centric Diffusion Policy for Generalizable and   Collision-Aware Robotic Manipulation","url":"https://arxiv.org/pdf/2407.00451"},{"title":"[2512.17568] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation","url":"https://arxiv.org/abs/2512.17568"}]

I found several relevant papers on arXiv related to diffusion policy with safety constraints and collision-aware manipulation from 2024-2025:

## Key Results:

1. **Language-Guided Object-Centric Diffusion Policy (July 2024, updated March 2025)**
   - Introduces Lan-o3dp, a language guided object centric diffusion policy that takes 3D representation of task relevant objects as conditional input and can be guided by cost function for safety constraints at inference time. Enables strong generalization in various aspects, such as background changes, visual ambiguity and can avoid novel obstacles that are unseen during the demonstration process.

2. **SafeBimanual (2025)**
   - Proposes a test-time trajectory optimization framework for pre-trained diffusion-based bimanual manipulation policies
…[truncated 916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-27T22:07:37.640545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeBimanual diffusion trajectory optimization safe bimanual manipulation 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeBimanual diffusion trajectory optimization safe bimanual manipulation 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-27T22:07:37.640686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"robot distance field\" RDF whole-body manipulation SDF learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"robot distance field\" RDF whole-body manipulation SDF learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-27T22:07:37.640809+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"neural configuration space barrier\" manipulation safety control 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"neural configuration space barrier\" manipulation safety control 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T22:07:37.640932+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "kinematics-aware diffusion policy whole-arm manipulation collision 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "kinematics-aware diffusion policy whole-arm manipulation collision 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T22:07:37.641071+00:00_

Web search results for query: "kinematics-aware diffusion policy whole-arm manipulation collision 2025 arxiv"

Links: [{"title":"[2512.17568] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation","url":"https://arxiv.org/abs/2512.17568"},{"title":"(PDF) Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation","url":"https://www.researchgate.net/publication/398936740_Kinematics-Aware_Diffusion_Policy_with_Consistent_3D_Observation_and_Action_Space_for_Whole-Arm_Robotic_Manipulation"},{"title":"Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/abs/2512.17568"},{"title":"Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation","url":"https://arxiv.org/html/2512.17568"},{"title":"Kinematics-Aware Diffusion Policy","url":"https://kinematics-aware-diffusion-policy.github.io/"},{"title":"Kinematics-Aware Diffusion Policy with Consistent 3D ...","url":"https://arxiv.org/pdf/2512.17568"},{"title":"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation","url":"https://arxiv.org/html/2407.00451v2"}]

Based on the search results, I found the paper you're looking for:

**Title:** Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation

**Key Details:**
- **ArXiv ID:** 2512.17568
- **Date:** December 19, 2025

**Summary:**
The paper addresses whole-body control of robotic manipulators with awareness of full-arm kinematics for manipulation scenarios involving body collision avoidance or body-object interactions. 

The framework proposes a kinematics-aware imitation learning approach with consistent task, observation, and action spaces, all represented in the same 3D space. The approach incorporat
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T22:07:37.641235+00:00_

Web search results for query: ""robot distance field" RDF whole-body manipulation SDF learning 2024 2025"

Links: [{"title":"(PDF) Learning Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://www.researchgate.net/publication/372074663_Learning_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"Learning Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://www.catalyzex.com/paper/learning-robot-geometry-as-distance-fields"},{"title":"Representing Robot Geometry as Distance Fields: Applications to   Whole-body Manipulation","url":"https://arxiv.org/pdf/2307.00533"},{"title":"\\textcolorblackRepresenting Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://arxiv.org/html/2307.00533v3"},{"title":"[2307.00533] Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://arxiv.org/abs/2307.00533"},{"title":"[PDF] Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Representing-Robot-Geometry-as-Distance-Fields:-to-Li-Zhang/e0cfb62fc1ce2f20c5b40e6174b172107f3d4ea0"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382979799_Representing_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"}]

Based on the search results, I found relevant research on robot distance fields (RDF) and whole-body manipulation:

## Key Findings

The primary work proposes learning robot geometry as distance fields (RDF), which extend the signed distance field (SDF) of the robot with joint configurations. The RDF approach leverages the kinematic chain of the robot, which reduces the dimensionality and complexity of the problem, resulting in more accurate and reliable SDFs.

## Te
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T22:07:37.641513+00:00_

Web search results for query: "SafeBimanual diffusion trajectory optimization safe bimanual manipulation 2025 arxiv"

Links: [{"title":"[2508.18268] SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation","url":"https://arxiv.org/abs/2508.18268"},{"title":"Safebimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation","url":"https://denghaoyuan123.github.io/SafeBimanip/"},{"title":"Diffusion-based Trajectory Optimization for Safe Bimanual ...","url":"https://arxiv.org/pdf/2508.18268"},{"title":"SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation","url":"https://arxiv.org/html/2508.18268v1"},{"title":"SafeBimanual: Diffusion-based trajectory optimization for safe bimanual manipulation | OpenReview","url":"https://openreview.net/forum?id=Q0H9xlNdVm"},{"title":"SafeBimanual: Diffusion-based Trajectory Optimization for Safe ...","url":"https://openreview.net/pdf/610a05a497c095fad609967bbfcf021ca7787961.pdf"},{"title":"[Literature Review] Learning Coordinated Bimanual Manipulation Policies using State Diffusion and Inverse Dynamics Models","url":"https://www.themoonlight.io/en/review/learning-coordinated-bimanual-manipulation-policies-using-state-diffusion-and-inverse-dynamics-models"}]

Based on the search results, I found the paper you're looking for:

**SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation**

SafeBimanual is a test-time trajectory optimization framework for any pre-trained diffusion-based bimanual manipulation policies, which imposes safety constraints on bimanual actions to avoid dangerous robot behaviors with improved success rate.

**Key Features:**

The framework designs diverse cost functions for safety constraints in different dual-arm cooperation patterns including avoidance of tearing objects and collision between arms and objects, which optimizes the manipulator trajectories with guided sampling of diffusion denoising process.

…[truncated 788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T22:07:37.641713+00:00_

Web search results for query: ""neural configuration space barrier" manipulation safety control 2025 arxiv"

Links: [{"title":"[Literature Review] Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://www.themoonlight.io/en/review/neural-configuration-space-barriers-for-manipulation-planning-and-control"},{"title":"(PDF) Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://www.researchgate.net/publication/389694312_Neural_Configuration-Space_Barriers_for_Manipulation_Planning_and_Control"},{"title":"Neural Configuration-Space Barriers for Manipulation Planning and   Control","url":"https://arxiv.org/pdf/2503.04929"},{"title":"Neural Configuration-Space Barriers for Manipulation Planning and Control | alphaXiv","url":"https://www.alphaxiv.org/abs/2503.04929"},{"title":"[2503.04929] Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://arxiv.org/abs/2503.04929"},{"title":"Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://arxiv.org/html/2503.04929v1"},{"title":"Computer Science Mar 2025","url":"http://arxiv.org/list/cs/2025-03?skip=2475&show=50"},{"title":"Systems and Control Mar 2025","url":"https://www.arxiv.org/list/eess.SY/2025-03?skip=475&show=25"},{"title":"[2507.13871] Safety Certification in the Latent space using Control Barrier Functions and World Models","url":"https://arxiv.org/abs/2507.13871"}]

I found the paper you're searching for! Here are the key details about "Neural Configuration-Space Barriers for Manipulation Planning and Control":

## Paper Overview

The paper addresses planning and control for high-dimensional robot manipulators in cluttered, dynamic environments, requiring both computational efficiency and robust safety guarantees.

## Main Approach

The authors propose a unified framework for motion planning and control that formulates safety constraints as CDF barriers, inspired by recent advance
…[truncated 1066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-27T22:07:37.641868+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SDF end-to-end policy learning auxiliary supervision manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SDF end-to-end policy learning auxiliary supervision manipulation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-27T22:07:37.641995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "action collapse diffusion policy mode collapse robot manipulation evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "action collapse diffusion policy mode collapse robot manipulation evaluation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-27T22:07:37.642113+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "3D scene representation VLA spatial reasoning robot safety 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "3D scene representation VLA spatial reasoning robot safety 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-27T22:07:37.642247+00:00_

Web search results for query: "SDF end-to-end policy learning auxiliary supervision manipulation 2024 2025"

Links: [{"title":"End-to-End Training of Deep Visuomotor Policies","url":"https://arxiv.org/pdf/1504.00702"},{"title":"Loss is its own Reward: Self-Supervision for Reinforcement Learning","url":"https://arxiv.org/pdf/1612.07307"},{"title":"Learning End-to-end Autonomous Driving using Guided Auxiliary   Supervision","url":"https://arxiv.org/pdf/1808.10393"},{"title":"Accept Synthetic Objects as Real: End-to-End Training of Attentive Deep   Visuomotor Policies for Manipulation in Clutter","url":"https://arxiv.org/pdf/1909.11128"},{"title":"Reinforcement learning with scheduled auxiliary control","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11893480"}]

The search results contain several papers related to end-to-end policy learning with auxiliary supervision and manipulation tasks, though the specific combination of all your query terms appears across multiple papers rather than in a single 2024-2025 paper.

Here's what I found:

**Relevant papers in the search results:**

1. **End-to-End Training of Deep Visuomotor Policies** (2015) - Policies are represented by deep convolutional neural networks trained using a partially observed guided policy search method, which transforms policy search into supervised learning with supervision provided by a trajectory-centric reinforcement learning method.

2. **Loss is its own Reward: Self-Supervision for Reinforcement Learning** - This work considers self-supervised tasks that incorporate states, actions, and successors to provide auxiliary losses that offer ubiquitous and instantaneous supervision for representation learning even in the absence of reward.

3. **Learning End-to-end Autonomous Driving using Guided Auxiliary Supervision** (2018) - A Multi-task Learning from Demonstration framework uses supervised auxiliary task prediction to guide the main task, with the network intermediately pre
…[truncated 748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-27T22:07:37.642433+00:00_

Web search results for query: "3D scene representation VLA spatial reasoning robot safety 2025 2026"

Links: [{"title":"Avi: Action from Volumetric Inference","url":"https://arxiv.org/pdf/2510.21746"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding","url":"https://arxiv.org/pdf/2507.00416"},{"title":"ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation","url":"https://arxiv.org/pdf/2603.13788"},{"title":"RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/pdf/2509.21243"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/pdf/2503.07511"},{"title":"A Multi-Modal Neuro-Symbolic Approach for Spatial Reasoning-Based Visual Grounding in Robotics","url":"https://arxiv.org/pdf/2510.27033"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"}]

Based on the search results, here's what I found about 3D scene representation, VLA, spatial reasoning, and robot safety in 2025-2026:

## 3D Scene Representation and Spatial Reasoning in VLAs

Most existing VLA models primarily rely on 2D visual inputs and lack effective mechanisms for modeling the 3D spatial structure of the scene, which limits their spatial reasoning capabilities in complex manipulation tasks. Recent advances are addressing this gap:

- VLA models excel at robotic tasks by leveraging large-scale 2D vision-language pre-training, but their reliance on RGB i
…[truncated 1348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-27T22:07:37.642607+00:00_

Web search results for query: "action collapse diffusion policy mode collapse robot manipulation evaluation 2024 2025"

Links: [{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising","url":"https://arxiv.org/pdf/2510.21991"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"D2PPO: Diffusion Policy Policy Optimization with Dispersive Loss","url":"https://arxiv.org/pdf/2508.02644"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Demystifying Diffusion Policies: Action","url":"https://corl25-genpriors.github.io/Papers/19_Demystifying_Diffusion_Poli.pdf"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/pdf/2303.04137"}]

Based on the web search results, here are the key findings related to action collapse, diffusion policy, mode collapse, and robot manipulation evaluation in 2024-2025:

## Key Papers and Research

**Diffusion Policy Overview**
Diffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process, and it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9% across multiple manipulation benchmarks.

**Mode Collapse Issues**
Traditional models using MDNs or clustering with offset prediction tend to exhibit mode collapse and are limited in their ability to express high-precision behavior. Diffusion policies were developed to address these limitations by gracefully handling multimodal action distributions
…[truncated 984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-27T22:07:37.642775+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CDF\" \"configuration space distance field\" Li Calinon RSS 2024 manipulation planning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CDF\" \"configuration space distance field\" Li Calinon RSS 2024 manipulation planning"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-27T22:07:37.642899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained reinforcement learning safe robot policy 2024 2025 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained reinforcement learning safe robot policy 2024 2025 survey"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-27T22:07:37.643018+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GraspSDF SafeDiffuser safety-constrained diffusion model robotics 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GraspSDF SafeDiffuser safety-constrained diffusion model robotics 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T22:07:37.643166+00:00_

Web search results for query: ""CDF" "configuration space distance field" Li Calinon RSS 2024 manipulation planning"

Links: [{"title":"(PDF) Configuration Space Distance Fields for Manipulation Planning","url":"https://www.researchgate.net/publication/383891276_Configuration_Space_Distance_Fields_for_Manipulation_Planning"},{"title":"Configuration Space Distance Fields","url":"https://sites.google.com/view/cdfmp/home"},{"title":"Configuration Space Distance Fields for Manipulation ...","url":"https://calinon.ch/paper3102.htm"},{"title":"[PDF] Configuration Space Distance Fields for Manipulation Planning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Configuration-Space-Distance-Fields-for-Planning-Li-Chi/75af8f157566854a49e72ead68f807166b791809"},{"title":"Configuration Space Distance Fields (CDFs)","url":"https://www.emergentmind.com/topics/configuration-space-distance-fields-cdfs"},{"title":"[2406.01137] Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/abs/2406.01137"},{"title":"GitHub - idiap/cdf: Configuration Space Distance Fields for Manipulation Planning · GitHub","url":"https://github.com/idiap/cdf"},{"title":"Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/pdf/2406.01137"}]

Great! I found comprehensive information about Configuration Space Distance Fields (CDF). Here are the search results:

## Summary

Configuration Space Distance Fields (CDF) is research by Yiming Li, Xuemin Chi, Amirreza Razmjoo, and Sylvain Calinon from Idiap Research Institute and EPFL, presented at Robotics: Science and Systems (RSS) 2024.

### What is CDF?

CDF extends the signed distance field (SDF) concept to robot configuration spaces, which for a robot manipulator typically corresponds to the joint angles for each articulation of the robot.

### Key Advantages

CDF allows the implicit structure to be leveraged by control, optimization, and learning problems in a unified manner, unli
…[truncated 1003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-27T22:07:37.643334+00:00_

Web search results for query: "GraspSDF SafeDiffuser safety-constrained diffusion model robotics 2024 2025"

Links: [{"title":"SAFEDIFFUSER: SAFE PLANNING WITH DIFFUSION ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f95606d8e870020085990d9650b4f2a1-Paper-Conference.pdf"},{"title":"[PDF] SafeDiffuser: Safe Planning with Diffusion Probabilistic Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SafeDiffuser:-Safe-Planning-with-Diffusion-Models-Xiao-Wang/0b6eea72dcbe3257cac62afb0db9ec28505ede0b"},{"title":"SafeDiffuser: Safe Planning with Diffusion Probabilistic Models | OpenReview","url":"https://openreview.net/forum?id=ig2wk7kK9J"},{"title":"SafeDiffuser: Safe Planning with Diffusion Probabilistic Models","url":"https://arxiv.org/pdf/2306.00148"},{"title":"SafeDiffuser: Safe Planning with Diffusion Probabilistic Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230600148X/abstract"},{"title":"SafeDiffuser: Safe Planning with Diffusion Probabilistic Models","url":"https://safediffuser.github.io/safediffuser/"},{"title":"[2306.00148] SafeDiffuser: Safe Planning with Diffusion Probabilistic Models","url":"https://arxiv.org/abs/2306.00148"},{"title":"ICLR Poster SafeDiffuser: Safe Planning with Diffusion Probabilistic Models","url":"https://iclr.cc/virtual/2025/poster/28682"},{"title":"[Quick Review] SafeDiffuser: Safe Planning with Diffusion Probabilistic Models","url":"https://liner.com/review/safediffuser-safe-planning-with-diffusion-probabilistic-models"}]

I found comprehensive information about SafeDiffuser. Here are the key findings:

## Overview

SafeDiffuser is a method to equip diffusion models with safety guarantees via control barrier functions. Diffusion model-based approaches have shown promise in data-driven planning, but there are no safety guarantees, thus making it hard to be applied for safety-critical applications.

## Key Technical Approach

The key idea of the approach is to embed finite-time 
…[truncated 1139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T22:07:37.643529+00:00_

Web search results for query: "constrained reinforcement learning safe robot policy 2024 2025 survey"

Links: [{"title":"(PDF) A Survey of Safe Reinforcement Learning Methods in Robotics","url":"https://www.researchgate.net/publication/395361319_A_Survey_of_Safe_Reinforcement_Learning_Methods_in_Robotics"},{"title":"[2402.02025] A Survey of Constraint Formulations in Safe Reinforcement Learning","url":"https://arxiv.org/abs/2402.02025"},{"title":"A Survey of Safe Reinforcement Learning Methods in Robotics Yuen Xie","url":"https://www.itm-conferences.org/articles/itmconf/pdf/2025/09/itmconf_cseit2025_01014.pdf"},{"title":"A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety","url":"https://arxiv.org/html/2505.17342v1"},{"title":"A survey of constraint formulations in safe reinforcement learning | Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence","url":"https://dl.acm.org/doi/10.24963/ijcai.2024/913"},{"title":"[2505.17342] A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety","url":"https://arxiv.org/abs/2505.17342"},{"title":"Anytime Safe Reinforcement Learning","url":"http://terrano.ucsd.edu/jorge/publications/data/2025_MeMaCo-l4dc.pdf"},{"title":"A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety","url":"https://arxiv.org/pdf/2505.17342"},{"title":"Constrained Variational Policy Optimization for Safe Reinforcement   Learning","url":"https://arxiv.org/pdf/2201.11927"},{"title":"A Survey of Constraint Formulations in Safe Reinforcement Learning","url":"https://www.ijcai.org/proceedings/2024/0913.pdf"}]

Based on the web search results, here are several relevant surveys and resources on constrained reinforcement learning and safe robot policies from 2024-2025:

## Recent Surveys (2024-2025)

A comprehensive review of representa
…[truncated 1397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_scan_20260527T220506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-27T22:07:37.643776+00:00_

Analysis complete. Here's the gap report.

---

## 遗漏论文清单

### Tier 1: 高相关性，建议补充

| # | 论文 | 作者 | 年份/会议 | 与本文关系 | 建议引用位置 |
|---|------|------|-----------|-----------|-------------|
| 1 | **SafeDiffuser: Safe Planning with Diffusion Probabilistic Models** | Xiao, Wang et al. | ICLR 2025 (arXiv:2306.00148) | 将 CBF 嵌入 diffusion denoising 过程实现安全规划——与本文"safety imposed externally vs. learned intrinsically"的对比论述直接相关 | §Safety in Robot Learning，与 CAPE/Li2024langguided 并列，作为 diffusion-process 安全约束的代表 |
| 2 | **CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation** | (arXiv:2601.15541, Jan 2026) | 用 VLM 指导变阻抗控制实现 VLA 安全，属于 runtime shield 类方法 | §Safety in Robot Learning，作为 test-time 安全方法的又一变体，紧跟 VLSA/CoFreeVLA 之后 |
| 3 | **SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation** | Deng et al. | CoRL 2025 (arXiv:2508.18268) | Test-time trajectory optimization 对 diffusion policy 施加安全约束，与 CAPE 互补 | §Safety in Robot Learning，与 CAPE 并列为 test-time diffusion 安全方法 |
| 4 | **Configuration Space Distance Fields for Manipulation Planning** | Li, Chi, Razmjoo, Calinon | RSS 2024 (arXiv:2406.01137) | C-space SDF 的奠基工作，CSSDF-Net (Chen 2026) 的直接前驱 | §SDF in Robotics，在 CSSDF-Net 之前引用，作为 C-space SDF 的源头 |
| 5 | **Representing Robot Geometry as Distance Fields (RDF)** | Li, Zhang et al. | ICRA 2024 (arXiv:2307.00533) | 学习机器人自身几何的 SDF 用于 whole-body manipulation 和碰撞避免——与本文"full-body collision awareness remains open"直接对话 | §SDF in Robotics，补充 robot-body SDF 方向，与 DeepSDF/iSDF 的 scene SDF 形成对比 |
| 6 | **Neural Configuration-Space Barriers for Manipulation Planning and Control** | Long, Lee et al. (UCSD) | 2025 (arXiv:2503.04929) | 将 C-space SDF 与 CBF 结合实现安全保证——同时横跨 SDF 和 safety 两个 section | §SDF in Robotics 末尾或 §Safety in Robot Learning，作为 SDF+safety 的桥梁工作 |

### Tier 2: 中等相关性，可选补充

| # | 论文 | 作者 | 年份/会议 | 与本文关系 | 建议引用位置 |
|---|------|------|-----------|-----------|-------------|
| 7 | **Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation** | (arXiv:2512.17568, Dec 2025) | 将 full-arm kinematics 引入 diffusion policy，关注 whole-body collision avoidance | §SDF in Robotics 末尾讨论 full-body awareness 时可作为 policy-learning 侧的对应工作 |
| 8 | **PointVLA: Injecting the 3D World into Vision-Language-Action Models** | (arXiv:2503.07511, 2025) | 将 3D 点云注入 VLA，与 DepthVLA/SpatialForcing 同属 3D-aware VLA | §VLA Models，已有 3 篇 3D-aware VLA，此篇为补充但非必须 |

### 总结

**最需要补充的 3 篇**：
1. **SafeDiffuser** (ICLR 2025) — 当前 §Safety 已引用 CAPE 和 Li2024langguided 作为 diffusion-process safety 代表，但 SafeDiffuser 是该方向最有影响力的工作（ICLR oral-level），遗漏明显
2. **CDF** (RSS 2024) — 已引用 CSSDF-Net 却未引用其直接前驱，reviewers 可能注意到
3. **RDF** (ICRA 2024) — related work 末尾写"full-body collision awareness remains open"，但未引用明确做 robot-body SDF 的工作

**现有引用覆盖良好的方面**：VLA 基础模型（RT-2/Pi0/OpenVLA）、SafeLIBERO benchmark、action collapse、评估方法论、VLA 安全综述——这些方面不需要补充。

Sources:
- [SafeDiffuser (ICLR 2025)](https://arxiv.org/abs/2306.00148)
- [CompliantVLA-adaptor](https://arxiv.org/abs/2601.15541)
- [SafeBimanual (CoRL 2025)](https://arxiv.org/abs/2508.18268)
- [CDF (RSS 2024)](https://arxiv.org/abs/2406.01137)
- [RDF (ICRA 2024)](https://arxiv.org/abs/2307.00533)
- [Neural C-Space Barriers](https://arxiv.org/abs/2503.04929)
- [Kinematics-Aware Diffusion Policy](https://arxiv.org/abs/2512.17568)
- [PointVLA](https://arxiv.org/abs/2503.07511)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related_work_scan_20260527T220506"
}
```

</details>

---
