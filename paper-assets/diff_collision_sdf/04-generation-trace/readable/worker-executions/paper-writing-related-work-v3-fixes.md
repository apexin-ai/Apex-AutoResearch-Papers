# paper writing related work v3 fixes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_writing_related_work_v3_fixes_20260526T162642.log`
- **Structured JSON:** [`e561301651da43ab2326.json`](../../sessions/e5/e561301651da43ab2326.json)

## Before a recorded user message

50 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "6450b59d-2c90-491e-881f-1c9b1783a616",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779819600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "620248f1-51d8-4058-88d4-4f18de01fca4",
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25"
}
```

---

### Assistant

_source line 4_

I'll start by reading the relevant files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "80c10633-dd14-4fc6-a704-fea8c018000d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUpKJN7FHGnFKSrwb8Mt2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12246,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12246
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01E3DhkKpCYkKog8crxu88x4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "96184f77-0742-4d1c-8762-99ca6cabd954",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUpKJN7FHGnFKSrwb8Mt2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12246,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12246
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T16:26:59.522Z_

<details><summary>↩ Tool result · `toolu_01E3DhkKpCYkKog8crxu88x4`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models for Manipulation.}
4	Vision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.
5	RT-2~\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.
6	$\pi_0$~\cite{black2024pi0} introduced flow matching~\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.
7	OpenVLA~\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.
8	These models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\cite{hu2022lora}.
9	Recent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.
10	Spatial Forcing~\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\cite{li2025qdepth} and DepthVLA~\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.
11	Despite this progress, safety considerations remain largely absent from VLA training and evaluation.
12	Most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.
13	This paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.
14	
15	\paragraph{Safety in Robot Learning.}
16	Safety-aware robot learning spans training-time and test-time approaches.
17	At training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\%.
18	At test time, several methods apply external safety filters to learned policies.
19	VLSA~\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.
20	CoFreeVLA~\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.
21	iKinQP-RL~\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.
22	In the diffusion policy setting, \citet{li2024langguided} and CAPE~\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.
23	A recent survey~\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.
24	Common to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.
25	The end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.
26	This work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.
27	
28	\paragraph{Signed Distance Functions in Robotics.}
29	Signed distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.
30	DeepSDF~\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.
31	In robotics, SDFs serve perception, planning, and control.
32	iSDF~\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.
33	VoxPoser~\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.
34	For motion planning, RAMP~\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.
35	Recent work extends SDFs beyond task space: CSSDF-Net~\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.
36	These works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.
37	Critically, these methods typically query the SDF at the end-effector or a small set of control points, leaving full-body collision awareness as an open problem.
38	We evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.
39	
40	\paragraph{Evaluation Metrics for Safe Manipulation.}
41	Evaluation of manipulation safety requires metrics beyond binary task success.
42	LIBERO~\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.
43	SafeLIBERO, introduced by \citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.
44	Task success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.
45	However, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores near-perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.
46	Neither case reflects learned avoidance behavior.
47	This failure mode echoes broader concerns about metric reliability.
48	Goodhart's law in RL~\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.
49	Recent work on statistically rigorous robot evaluation~\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.
50	We propose displacement-filtered CAR ($\dfCAR$, \S\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "c24a1443-8a8d-4c2a-b4f2-021ffd67af25",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models for Manipulation.}\nVision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.\nRT-2~\\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.\n$\\pi_0$~\\cite{black2024pi0} introduced flow matching~\\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.\nOpenVLA~\\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.\nThese models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\\cite{hu2022lora}.\nRecent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.\nSpatial Forcing~\\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\\cite{li2025qdepth} and DepthVLA~\\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.\nDespite this progress, safety considerations remain largely absent from VLA training and evaluation.\nMost VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.\nThis paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware robot learning spans training-time and test-time approaches.\nAt training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\\%.\nAt test time, several methods apply external safety filters to learned policies.\nVLSA~\\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.\nCoFreeVLA~\\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.\niKinQP-RL~\\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.\nIn the diffusion policy setting, \\citet{li2024langguided} and CAPE~\\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.\nA recent survey~\\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.\nCommon to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.\nThe end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.\nThis work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSigned distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.\nDeepSDF~\\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.\nIn robotics, SDFs serve perception, planning, and control.\niSDF~\\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.\nVoxPoser~\\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.\nFor motion planning, RAMP~\\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.\nRecent work extends SDFs beyond task space: CSSDF-Net~\\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.\nThese works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.\nCritically, these methods typically query the SDF at the end-effector or a small set of control points, leaving full-body collision awareness as an open problem.\nWe evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nEvaluation of manipulation safety requires metrics beyond binary task success.\nLIBERO~\\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.\nSafeLIBERO, introduced by \\citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.\nTask success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.\nHowever, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores near-perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.\nNeither case reflects learned avoidance behavior.\nThis failure mode echoes broader concerns about metric reliability.\nGoodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.\nRecent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nWe propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015S3bzLBojK8qasd1ERWRRt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "35e29e3d-ca88-4b2f-a093-7c485129a8a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUpKJN7FHGnFKSrwb8Mt2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12246,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12246
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T16:26:59.730Z_

<details><summary>↩ Tool result · `toolu_015S3bzLBojK8qasd1ERWRRt`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "d78719e9-6200-48c4-9265-b7a2198f7a70",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the literature_map.yaml to find the Dong et al. 2025 bib key, and also check references.bib for existing entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "7afd2355-e7ab-4212-9414-871721b46986",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153EMRpzEjEsGqKXW9xsnGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2177
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G4bgqbPWnGvbmQjzgs3p8i`</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "49cd4219-d5c0-4519-b38d-6551a7145118",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153EMRpzEjEsGqKXW9xsnGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2177
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T16:27:04.916Z_

<details><summary>↩ Tool result · `toolu_01G4bgqbPWnGvbmQjzgs3p8i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-25\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\\n\\n  - paper_id: \\\"2601.21712\\\"\\n    title: \\\"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\\\"\\n    authors: \\\"Zhai et al.\\\"\\n    year: 2026\\n    venue: arXiv\\n    arxiv: \\\"2601.21712\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\\\"\\n    relevance: \\\"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\\\"\\n\\n  - paper_id: \\\"2404.02284\\\"\\n    title: \\\"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\\\"\\n    authors: \\\"Dastider et al.\\\"\\n    year: 2024\\n    venue: IROS 2024\\n    arxiv: \\\"2404.02284\\\"\\n    role: related-approach\\n    category: collision-aware-manipulation\\n    summary: \\\"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\\\"\\n    relevance: \\\"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\\\"\\n\\n  - paper_id: \\\"2512.11908\\\"\\n    title: \\\"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2512.11908\\\"\\n    role: survey\\n    category: collision-aware-manipulation\\n    summary: \\\"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\\\"\\n    relevance: \\\"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\\n\\n  - paper_id: \\\"2406.01137\\\"\\n    title: \\\"Configuration Space Distance Fields for Manipulation Planning\\\"\\n    authors: \\\"Li, Chi, Razmjoo, Calinon\\\"\\n    year: 2024\\n    venue: RSS 2024\\n    arxiv: \\\"2406.01137\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\\\"\\n    relevance: \\\"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\\\"\\n\\n  - paper_id: \\\"2409.14955\\\"\\n    title: \\\"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.14955\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\\\"\\n    relevance: \\\"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\\\"\\n\\n  - paper_id: \\\"2511.21312\\\"\\n    title: \\\"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\\\"\\n    authors: \\\"Jacquet, Harms, Alexis\\\"\\n    year: 2025\\n    venue: IJRR 2025\\n    arxiv: \\\"2511.21312\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\\\"\\n    relevance: \\\"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\\n  # ===== 新增 P3: Benchmark =====\\n\\n  - title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv: \\\"2306.03310\\\"\\n    role: benchmark\\n    relevance: \\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\"\\n\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\n\\n  - title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\"\\n    venue: \\\"ICLR 2023\\\"\\n    arxiv: \\\"2210.02747\\\"\\n    role: method-component\\n    relevance: \\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\"\\n\\n  # ===== 新增 P5: Action Collapse / Mode Collapse =====\\n\\n  - paper_id: \\\"2505.11123\\\"\\n    title: \\\"Conditioning Matters: Training Diffusion Policies is Faster Than You Think\\\"\\n    authors: \\\"Dong et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2505.11123\\\"\\n    role: related-approach\\n    category: action-collapse\\n    summary: \\\"发现 diffusion policy 训练中的 'loss collapse'——observation 条件难区分时训练退化为建模 marginal action 分布而非 condition-specific 分布，提出 Cocos 通过条件依赖的源分布锚定解决。\\\"\\n    relevance: \\\"与 ColliForce 的 action collapse 机制类似：collision penalty 可导致策略忽略 task-relevant conditioning 而坍缩到 degenerate marginal（如静止不动），提供了 diffusion policy 中 loss collapse 的理论对照。\\\"\\n\\n  - paper_id: \\\"2303.04137\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: RSS 2023 / IJRR 2024\\n    arxiv: \\\"2303.04137\\\"\\n    role: foundational\\n    category: action-collapse\\n    summary: \\\"提出基于扩散模型的视觉运动策略，解决行为克隆中的 mode averaging 问题——标准回归策略在多模态演示上取均值产生不安全的中间轨迹。\\\"\\n    relevance: \\\"定义了 IL 中 mode averaging/collapse 的规范表述；ColliForce 的 collision penalty 可能在表达性策略架构中重新引入类似的模态坍缩，将动作分布推向单一 'freeze' 模态。\\\"\\n\\n  # ===== 新增 P6: Safe RL / Safe Imitation Learning =====\\n\\n  - paper_id: \\\"1705.10528\\\"\\n    title: \\\"Constrained Policy Optimization\\\"\\n    authors: \\\"Achiam et al.\\\"\\n    year: 2017\\n    venue: ICML 2017\\n    arxiv: \\\"1705.10528\\\"\\n    role: foundational\\n    category: safe-rl\\n    summary: \\\"训练时安全 RL 基础方法，在 trust-region 框架中约束策略更新满足 cost 限制，形式化为 constrained MDP。\\\"\\n    relevance: \\\"Safe RL 奠基工作；仅用标量 cost 信号，不含几何碰撞信息，不处理高维视觉-语言观测空间。ColliForce 的可微 SDF 辅助损失提供比 CPO 标量约束更丰富的连续几何安全信号。\\\"\\n\\n  - paper_id: \\\"2409.19190\\\"\\n    title: \\\"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution\\\"\\n    authors: \\\"Jung et al.\\\"\\n    year: 2025\\n    venue: ICRA 2025\\n    arxiv: \\\"2409.19190\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"测试时安全方法：训练标准 IL 策略后用可达性分析安全过滤器在运行时覆盖不安全动作，实现 0% 碰撞率。\\\"\\n    relevance: \\\"策略本身不学安全，与 ColliForce 训练时 SDF 嵌入形成对比。解耦方式意味着过滤器频繁干预时可能降低任务性能，ColliForce 通过让策略原生碰撞感知来避免这一问题。\\\"\\n\\n  - paper_id: \\\"2503.17432\\\"\\n    title: \\\"TamedPUMA: Safe and Stable Imitation Learning with Geometric Fabrics\\\"\\n    authors: \\\"Bakker et al.\\\"\\n    year: 2025\\n    venue: L4DC 2025\\n    arxiv: \\\"2503.17432\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"将学习的运动基元与 geometric fabrics 融合，在运行时强制碰撞回避和关节限制，需已知障碍物解析表示。\\\"\\n    relevance: \\\"运行时安全机制叠加在 IL 之上；需要运行时解析障碍物表示，ColliForce 在训练时嵌入 SDF 使策略泛化到新场景而无需运行时几何计算。\\\"\\n\", \"total_chars\": 13371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "a6368399-3384-4c9a-a0aa-73da853efc46",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\\\", \\\"content\\\": \\\"# ColliForce-VLA Literature Map\\\\n# Updated: 2026-05-25\\\\n\\\\npapers:\\\\n\\\\n  # ===== 已有论文 =====\\\\n\\\\n  - paper_id: \\\\\\\"2512.11891\\\\\\\"\\\\n    title: \\\\\\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\\\\\"\\\\n    authors: \\\\\\\"Hu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    one_line_summary: \\\\\\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.14836\\\\\\\"\\\\n    title: \\\\\\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: spatial-aware-vla\\\\n    one_line_summary: \\\\\\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.12276\\\\\\\"\\\\n    title: \\\\\\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: ICLR 2026\\\\n    role: method-component\\\\n    category: spatial-aware-vla\\\\n    one_line_summary: \\\\\\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.05973\\\\\\\"\\\\n    title: \\\\\\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Huang et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: CoRL 2023\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2410.24164\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al., Physical Intelligence\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    role: backbone\\\\n    category: vla-foundation\\\\n    one_line_summary: \\\\\\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"1901.05103\\\\\\\"\\\\n    title: \\\\\\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\\\\\"\\\\n    authors: \\\\\\\"Park et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: CVPR 2019\\\\n    role: method-component\\\\n    category: sdf-representation\\\\n    one_line_summary: \\\\\\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.00533\\\\\\\"\\\\n    title: \\\\\\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\\\\\"\\\\n\\\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\\\n\\\\n  - paper_id: \\\\\\\"2503.03480\\\\\\\"\\\\n    title: \\\\\\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: NeurIPS 2025 (Spotlight)\\\\n    arxiv: \\\\\\\"2503.03480\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\\\\\"\\\\n    relevance: \\\\\\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2407.00451\\\\\\\"\\\\n    title: \\\\\\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: ICRA 2025\\\\n    arxiv: \\\\\\\"2407.00451\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\\\\\"\\\\n    relevance: \\\\\\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2511.22773\\\\\\\"\\\\n    title: \\\\\\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2511.22773\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\\\\\"\\\\n    relevance: \\\\\\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.08233\\\\\\\"\\\\n    title: \\\\\\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\\\\\"\\\\n    authors: \\\\\\\"Spalter et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2409.08233\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\\\\\"\\\\n    relevance: \\\\\\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\\\\\"\\\\n\\\\n  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\\\\n\\\\n  - paper_id: \\\\\\\"2601.21712\\\\\\\"\\\\n    title: \\\\\\\"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\\\\\\\"\\\\n    authors: \\\\\\\"Zhai et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2601.21712\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\\\\\\\"\\\\n    relevance: \\\\\\\"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2404.02284\\\\\\\"\\\\n    title: \\\\\\\"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\\\\\\\"\\\\n    authors: \\\\\\\"Dastider et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: IROS 2024\\\\n    arxiv: \\\\\\\"2404.02284\\\\\\\"\\\\n    role: related-approach\\\\n    category: collision-aware-manipulation\\\\n    summary: \\\\\\\"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\\\\\\\"\\\\n    relevance: \\\\\\\"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2512.11908\\\\\\\"\\\\n    title: \\\\\\\"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2512.11908\\\\\\\"\\\\n    role: survey\\\\n    category: collision-aware-manipulation\\\\n    summary: \\\\\\\"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\\\\\\\"\\\\n    relevance: \\\\\\\"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\\\\\\\"\\\\n\\\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\\\n\\\\n  - paper_id: \\\\\\\"2204.02296\\\\\\\"\\\\n    title: \\\\\\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\\\\\"\\\\n    authors: \\\\\\\"Ortiz et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: RSS 2022\\\\n    arxiv: \\\\\\\"2204.02296\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\\\\\"\\\\n    relevance: \\\\\\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2305.10534\\\\\\\"\\\\n    title: \\\\\\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\\\\\"\\\\n    authors: \\\\\\\"Vasilopoulos et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: IROS 2023\\\\n    arxiv: \\\\\\\"2305.10534\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\\\\\"\\\\n    relevance: \\\\\\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2102.07413\\\\\\\"\\\\n    title: \\\\\\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Zhi et al.\\\\\\\"\\\\n    year: 2021\\\\n    venue: IEEE T-RO\\\\n    arxiv: \\\\\\\"2102.07413\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\\\\\"\\\\n    relevance: \\\\\\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\\\\\"\\\\n\\\\n  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\\\\n\\\\n  - paper_id: \\\\\\\"2406.01137\\\\\\\"\\\\n    title: \\\\\\\"Configuration Space Distance Fields for Manipulation Planning\\\\\\\"\\\\n    authors: \\\\\\\"Li, Chi, Razmjoo, Calinon\\\\\\\"\\\\n    year: 2024\\\\n    venue: RSS 2024\\\\n    arxiv: \\\\\\\"2406.01137\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\\\\\\\"\\\\n    relevance: \\\\\\\"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.14955\\\\\\\"\\\\n    title: \\\\\\\"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\\\\\\\"\\\\n    authors: \\\\\\\"Zhu et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2409.14955\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\\\\\\\"\\\\n    relevance: \\\\\\\"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2511.21312\\\\\\\"\\\\n    title: \\\\\\\"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\\\\\\\"\\\\n    authors: \\\\\\\"Jacquet, Harms, Alexis\\\\\\\"\\\\n    year: 2025\\\\n    venue: IJRR 2025\\\\n    arxiv: \\\\\\\"2511.21312\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\\\\\\\"\\\\n    relevance: \\\\\\\"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\\\\\\\"\\\\n\\\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\\\n\\\\n  - paper_id: \\\\\\\"2307.15818\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al., Google DeepMind\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2307.15818\\\\\\\"\\\\n    role: foundational\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\\\\\"\\\\n    relevance: \\\\\\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2406.09246\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2406.09246\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\\\\\"\\\\n    relevance: \\\\\\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2405.12213\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Octo Model Team\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2405.12213\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\\\\\"\\\\n    relevance: \\\\\\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\\\\\"\\\\n\\\\n  # ===== 新增 P3: Benchmark =====\\\\n\\\\n  - title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    arxiv: \\\\\\\"2306.03310\\\\\\\"\\\\n    role: benchmark\\\\n    relevance: \\\\\\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\\\\\"\\\\n\\\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\\\n\\\\n  - title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    arxiv: \\\\\\\"2210.02747\\\\\\\"\\\\n    role: method-component\\\\n    relevance: \\\\\\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\\\\\"\\\\n\\\\n  # ===== 新增 P5: Action Collapse / Mode Collapse =====\\\\n\\\\n  - paper_id: \\\\\\\"2505.11123\\\\\\\"\\\\n    title: \\\\\\\"Conditioning Matters: Training Diffusion Policies is Faster Than You Think\\\\\\\"\\\\n    authors: \\\\\\\"Dong et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2505.11123\\\\\\\"\\\\n    role: related-approach\\\\n    category: action-collapse\\\\n    summary: \\\\\\\"发现 diffusion policy 训练中的 'loss collapse'——observation 条件难区分时训练退化为建模 marginal action 分布而非 condition-specific 分布，提出 Cocos 通过条件依赖的源分布锚定解决。\\\\\\\"\\\\n    relevance: \\\\\\\"与 ColliForce 的 action collapse 机制类似：collision penalty 可导致策略忽略 task-relevant conditioning 而坍缩到 degenerate marginal（如静止不动），提供了 diffusion policy 中 loss collapse 的理论对照。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2303.04137\\\\\\\"\\\\n    title: \\\\\\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Chi et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: RSS 2023 / IJRR 2024\\\\n    arxiv: \\\\\\\"2303.04137\\\\\\\"\\\\n    role: foundational\\\\n    category: action-collapse\\\\n    summary: \\\\\\\"提出基于扩散模型的视觉运动策略，解决行为克隆中的 mode averaging 问题——标准回归策略在多模态演示上取均值产生不安全的中间轨迹。\\\\\\\"\\\\n    relevance: \\\\\\\"定义了 IL 中 mode averaging/collapse 的规范表述；ColliForce 的 collision penalty 可能在表达性策略架构中重新引入类似的模态坍缩，将动作分布推向单一 'freeze' 模态。\\\\\\\"\\\\n\\\\n  # ===== 新增 P6: Safe RL / Safe Imitation Learning =====\\\\n\\\\n  - paper_id: \\\\\\\"1705.10528\\\\\\\"\\\\n    title: \\\\\\\"Constrained Policy Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Achiam et al.\\\\\\\"\\\\n    year: 2017\\\\n    venue: ICML 2017\\\\n    arxiv: \\\\\\\"1705.10528\\\\\\\"\\\\n    role: foundational\\\\n    category: safe-rl\\\\n    summary: \\\\\\\"训练时安全 RL 基础方法，在 trust-region 框架中约束策略更新满足 cost 限制，形式化为 constrained MDP。\\\\\\\"\\\\n    relevance: \\\\\\\"Safe RL 奠基工作；仅用标量 cost 信号，不含几何碰撞信息，不处理高维视觉-语言观测空间。ColliForce 的可微 SDF 辅助损失提供比 CPO 标量约束更丰富的连续几何安全信号。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.19190\\\\\\\"\\\\n    title: \\\\\\\"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution\\\\\\\"\\\\n    authors: \\\\\\\"Jung et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: ICRA 2025\\\\n    arxiv: \\\\\\\"2409.19190\\\\\\\"\\\\n    role: related-approach\\\\n    category: safe-rl\\\\n    summary: \\\\\\\"测试时安全方法：训练标准 IL 策略后用可达性分析安全过滤器在运行时覆盖不安全动作，实现 0% 碰撞率。\\\\\\\"\\\\n    relevance: \\\\\\\"策略本身不学安全，与 ColliForce 训练时 SDF 嵌入形成对比。解耦方式意味着过滤器频繁干预时可能降低任务性能，ColliForce 通过让策略原生碰撞感知来避免这一问题。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2503.17432\\\\\\\"\\\\n    title: \\\\\\\"TamedPUMA: Safe and Stable Imitation Learning with Geometric Fabrics\\\\\\\"\\\\n    authors: \\\\\\\"Bakker et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: L4DC 2025\\\\n    arxiv: \\\\\\\"2503.17432\\\\\\\"\\\\n    role: related-approach\\\\n    category: safe-rl\\\\n    summary: \\\\\\\"将学习的运动基元与 geometric fabrics 融合，在运行时强制碰撞回避和关节限制，需已知障碍物解析表示。\\\\\\\"\\\\n    relevance: \\\\\\\"运行时安全机制叠加在 IL 之上；需要运行时解析障碍物表示，ColliForce 在训练时嵌入 SDF 使策略泛化到新场景而无需运行时几何计算。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 13371, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-25\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\\n\\n  - paper_id: \\\"2601.21712\\\"\\n    title: \\\"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\\\"\\n    authors: \\\"Zhai et al.\\\"\\n    year: 2026\\n    venue: arXiv\\n    arxiv: \\\"2601.21712\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\\\"\\n    relevance: \\\"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\\\"\\n\\n  - paper_id: \\\"2404.02284\\\"\\n    title: \\\"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\\\"\\n    authors: \\\"Dastider et al.\\\"\\n    year: 2024\\n    venue: IROS 2024\\n    arxiv: \\\"2404.02284\\\"\\n    role: related-approach\\n    category: collision-aware-manipulation\\n    summary: \\\"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\\\"\\n    relevance: \\\"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\\\"\\n\\n  - paper_id: \\\"2512.11908\\\"\\n    title: \\\"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2512.11908\\\"\\n    role: survey\\n    category: collision-aware-manipulation\\n    summary: \\\"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\\\"\\n    relevance: \\\"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\\n\\n  - paper_id: \\\"2406.01137\\\"\\n    title: \\\"Configuration Space Distance Fields for Manipulation Planning\\\"\\n    authors: \\\"Li, Chi, Razmjoo, Calinon\\\"\\n    year: 2024\\n    venue: RSS 2024\\n    arxiv: \\\"2406.01137\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\\\"\\n    relevance: \\\"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\\\"\\n\\n  - paper_id: \\\"2409.14955\\\"\\n    title: \\\"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.14955\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\\\"\\n    relevance: \\\"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\\\"\\n\\n  - paper_id: \\\"2511.21312\\\"\\n    title: \\\"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\\\"\\n    authors: \\\"Jacquet, Harms, Alexis\\\"\\n    year: 2025\\n    venue: IJRR 2025\\n    arxiv: \\\"2511.21312\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\\\"\\n    relevance: \\\"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\\n  # ===== 新增 P3: Benchmark =====\\n\\n  - title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv: \\\"2306.03310\\\"\\n    role: benchmark\\n    relevance: \\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\"\\n\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\n\\n  - title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\"\\n    venue: \\\"ICLR 2023\\\"\\n    arxiv: \\\"2210.02747\\\"\\n    role: method-component\\n    relevance: \\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\"\\n\\n  # ===== 新增 P5: Action Collapse / Mode Collapse =====\\n\\n  - paper_id: \\\"2505.11123\\\"\\n    title: \\\"Conditioning Matters: Training Diffusion Policies is Faster Than You Think\\\"\\n    authors: \\\"Dong et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2505.11123\\\"\\n    role: related-approach\\n    category: action-collapse\\n    summary: \\\"发现 diffusion policy 训练中的 'loss collapse'——observation 条件难区分时训练退化为建模 marginal action 分布而非 condition-specific 分布，提出 Cocos 通过条件依赖的源分布锚定解决。\\\"\\n    relevance: \\\"与 ColliForce 的 action collapse 机制类似：collision penalty 可导致策略忽略 task-relevant conditioning 而坍缩到 degenerate marginal（如静止不动），提供了 diffusion policy 中 loss collapse 的理论对照。\\\"\\n\\n  - paper_id: \\\"2303.04137\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: RSS 2023 / IJRR 2024\\n    arxiv: \\\"2303.04137\\\"\\n    role: foundational\\n    category: action-collapse\\n    summary: \\\"提出基于扩散模型的视觉运动策略，解决行为克隆中的 mode averaging 问题——标准回归策略在多模态演示上取均值产生不安全的中间轨迹。\\\"\\n    relevance: \\\"定义了 IL 中 mode averaging/collapse 的规范表述；ColliForce 的 collision penalty 可能在表达性策略架构中重新引入类似的模态坍缩，将动作分布推向单一 'freeze' 模态。\\\"\\n\\n  # ===== 新增 P6: Safe RL / Safe Imitation Learning =====\\n\\n  - paper_id: \\\"1705.10528\\\"\\n    title: \\\"Constrained Policy Optimization\\\"\\n    authors: \\\"Achiam et al.\\\"\\n    year: 2017\\n    venue: ICML 2017\\n    arxiv: \\\"1705.10528\\\"\\n    role: foundational\\n    category: safe-rl\\n    summary: \\\"训练时安全 RL 基础方法，在 trust-region 框架中约束策略更新满足 cost 限制，形式化为 constrained MDP。\\\"\\n    relevance: \\\"Safe RL 奠基工作；仅用标量 cost 信号，不含几何碰撞信息，不处理高维视觉-语言观测空间。ColliForce 的可微 SDF 辅助损失提供比 CPO 标量约束更丰富的连续几何安全信号。\\\"\\n\\n  - paper_id: \\\"2409.19190\\\"\\n    title: \\\"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution\\\"\\n    authors: \\\"Jung et al.\\\"\\n    year: 2025\\n    venue: ICRA 2025\\n    arxiv: \\\"2409.19190\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"测试时安全方法：训练标准 IL 策略后用可达性分析安全过滤器在运行时覆盖不安全动作，实现 0% 碰撞率。\\\"\\n    relevance: \\\"策略本身不学安全，与 ColliForce 训练时 SDF 嵌入形成对比。解耦方式意味着过滤器频繁干预时可能降低任务性能，ColliForce 通过让策略原生碰撞感知来避免这一问题。\\\"\\n\\n  - paper_id: \\\"2503.17432\\\"\\n    title: \\\"TamedPUMA: Safe and Stable Imitation Learning with Geometric Fabrics\\\"\\n    authors: \\\"Bakker et al.\\\"\\n    year: 2025\\n    venue: L4DC 2025\\n    arxiv: \\\"2503.17432\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"将学习的运动基元与 geometric fabrics 融合，在运行时强制碰撞回避和关节限制，需已知障碍物解析表示。\\\"\\n    relevance: \\\"运行时安全机制叠加在 IL 之上；需要运行时解析障碍物表示，ColliForce 在训练时嵌入 SDF 使策略泛化到新场景而无需运行时几何计算。\\\"\\n\", \"total_chars\": 13371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Grep · `toolu_01XPMyCq8D4DHviG5ub4AGNK`</summary>

```json
{
  "pattern": "dong|Dong|conditioning.?matters|2505\\.11123|action.?collapse",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "d8edb0c9-e09e-44ad-ba1c-bd239cc5aecf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153EMRpzEjEsGqKXW9xsnGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2177
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T16:27:07.771Z_

<details><summary>↩ Tool result · `toolu_01XPMyCq8D4DHviG5ub4AGNK`</summary>

```text
39:  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},
83:  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\"o}fer, Michael and Mukadam, Mustafa},
194:  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},
201:  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},
222:  author={Qu, Delin and Song, Haoming and Chen, Qizhi and Yao, Yuanqi and Ye, Xinyi and Gu, Jiayuan and Wang, Zhigang and Ding, Yan and Zhao, Bin and Wang, Dong and Li, Xuelong},
264:  author={Rao, Zhifeng and Chen, Wenlong and Xie, Lei and Hua, Xia and Yin, Dongfu and Tian, Zhen and Yu, F. Richard},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "5250bac2-1f4d-4ac0-adc2-dff3229dc09b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "39:  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},\n83:  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\\\"o}fer, Michael and Mukadam, Mustafa},\n194:  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},\n201:  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},\n222:  author={Qu, Delin and Song, Haoming and Chen, Qizhi and Yao, Yuanqi and Ye, Xinyi and Gu, Jiayuan and Wang, Zhigang and Ding, Yan and Zhao, Bin and Wang, Dong and Li, Xuelong},\n264:  author={Rao, Zhifeng and Chen, Wenlong and Xie, Lei and Hua, Xia and Yin, Dongfu and Tian, Zhen and Yu, F. Richard},",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01CA9XxQHR6WfuRJoHx9D8M7`</summary>

```json
{
  "pattern": "\\\\\\\\dfCAR",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "3b7fe624-2dc1-4a1c-a268-3c2f81d5be69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153EMRpzEjEsGqKXW9xsnGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2177
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T16:27:08.517Z_

<details><summary>↩ Tool result · `toolu_01CA9XxQHR6WfuRJoHx9D8M7`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "42fa89fc-29d7-42f6-9759-85846b681372",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The grep for `\\dfCAR` returned no matches. Let me try a different pattern - the file has `$\dfCAR$` on line 50.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "89069f0e-3421-4c40-ac4e-ffd8ac8d889f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ouxAQ7KUCuXFmbx1b5qxb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 25870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 17_

The `\\dfCAR` grep didn't match due to escaping. Let me search more carefully and check the bib file for the Dong entry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "b49d2be1-94e5-4960-b87f-a48527fb04d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ouxAQ7KUCuXFmbx1b5qxb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 25870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01MUiabv7XD9eR6WCjYpjPw9`</summary>

```json
{
  "pattern": "dfCAR",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "ae040422-22ba-4608-98e7-2265e5ab9806",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ouxAQ7KUCuXFmbx1b5qxb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 25870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T16:27:14.984Z_

<details><summary>↩ Tool result · `toolu_01MUiabv7XD9eR6WCjYpjPw9`</summary>

```text
50:We propose displacement-filtered CAR ($\dfCAR$, \S\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "bd7be0e2-01da-483f-8492-bc05e2562783",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "50:We propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01EedKxhwp3SzLTMgivWJVY6`</summary>

```json
{
  "pattern": "dong2025|conditioning",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "75d31149-ef7b-48d9-917c-e558e866c843",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ouxAQ7KUCuXFmbx1b5qxb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 25870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T16:27:16.157Z_

<details><summary>↩ Tool result · `toolu_01EedKxhwp3SzLTMgivWJVY6`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "d510cb0d-a154-4f03-bdcd-20e108888913",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 22_

Found `$\dfCAR$` on line 50. No Dong et al. entry in references.bib. Let me also check if `\dfCAR` is defined as a command in main.tex, and verify the full author list via web search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "480fbf2d-c082-4e33-b761-f88fdcd2893c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132nKdYXB4zW3pV6mzCSsdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 34248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Grep · `toolu_01KfrS9YP8QCb8YyqoabQQZF`</summary>

```json
{
  "pattern": "dfCAR",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "37973ccb-94a0-430a-8f7a-a392ce675878",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132nKdYXB4zW3pV6mzCSsdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 34248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T16:27:20.547Z_

<details><summary>↩ Tool result · `toolu_01KfrS9YP8QCb8YyqoabQQZF`</summary>

```text
docs/paper/related_work.tex:50:We propose displacement-filtered CAR ($\dfCAR$, \S\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.
docs/paper/main.tex:15:\newcommand{\dfCAR}{\text{dfCAR}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "9dca2ace-8651-4891-87f6-b48a8b0a1797",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:50:We propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.\ndocs/paper/main.tex:15:\\newcommand{\\dfCAR}{\\text{dfCAR}}",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013nh9PXXe3A87VYFFNjJyGX`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "6e867929-43f4-4e1c-9c3e-d54652cd8d23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132nKdYXB4zW3pV6mzCSsdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 34248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T16:27:21.020Z_

<details><summary>↩ Tool result · `toolu_013nh9PXXe3A87VYFFNjJyGX`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "4e2f7d9b-f4ac-4a5b-adc6-70f6b605840f",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 27_

`\dfCAR` is defined as a command in main.tex:15. Let me check how it's used across the paper to decide whether to replace it or keep it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "441622a5-23fb-4a1a-98c1-ad2d6f379cd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnnRMNcDjpm5UL5eTGaNg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 34709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1002
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_01UdqSBQQQeLvqyevxZwqd8d`</summary>

```json
{
  "pattern": "dfCAR",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "b1e9d5ab-80ae-4a70-869c-443b56988f4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnnRMNcDjpm5UL5eTGaNg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 34709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1002
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T16:27:24.782Z_

<details><summary>↩ Tool result · `toolu_01UdqSBQQQeLvqyevxZwqd8d`</summary>

```text
docs/paper/related_work.tex:1
docs/paper/main.tex:1

Found 2 total occurrences across 2 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "18f291ac-076f-48f2-99ba-285c8c7029d9",
  "tool_use_result": {
    "mode": "count",
    "numFiles": 2,
    "filenames": [],
    "content": "docs/paper/related_work.tex:1\ndocs/paper/main.tex:1",
    "numMatches": 2
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ESbVmEonpDw3VsoiLew1yD`</summary>

```json
{
  "query": "arXiv 2505.11123 \"Conditioning Matters\" Dong authors diffusion policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "37aaf3fe-052f-4759-8f95-d8a6f0cfa00f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnnRMNcDjpm5UL5eTGaNg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 34709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1002
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T16:27:31.479Z_

<details><summary>↩ Tool result · `toolu_01ESbVmEonpDw3VsoiLew1yD`</summary>

```text
Web search results for query: "arXiv 2505.11123 "Conditioning Matters" Dong authors diffusion policy"

Links: [{"title":"[2505.11123] Conditioning Matters: Training Diffusion Policies is Faster Than You Think","url":"https://arxiv.org/abs/2505.11123"},{"title":"Conditioning Matters: Training Diffusion Policies is Faster Than You Think","url":"https://arxiv.org/html/2505.11123"},{"title":"Unpacking the Individual Components of Diffusion Policy","url":"https://arxiv.org/html/2412.00084v1"},{"title":"Unpacking the Individual Components of Diffusion Policy","url":"https://arxiv.org/pdf/2412.00084"},{"title":"VLM-TDP: VLM-guided Trajectory-conditioned Diffusion Policy for Robust Long-Horizon Manipulation","url":"https://arxiv.org/pdf/2507.04524"},{"title":"Factorizing Diffusion Policies for Observation Modality Prioritization","url":"https://arxiv.org/pdf/2509.16830"}]

Based on the search results, here's what I found about arXiv paper 2505.11123:

**Paper Title:** Conditioning Matters: Training Diffusion Policies is Faster Than You Think

**Authors:** Zibin Dong, Yicheng Liu, Yinchuan Li, Hang Zhao, Jianye Hao

**Main Contribution:** The paper identifies a fundamental challenge in conditional diffusion policy training: when generative conditions are hard to distinguish, the training objective degenerates into modeling the marginal action distribution, a phenomenon termed loss collapse.

**Proposed Solution:** The authors propose Cocos, a simple yet general solution that modifies the source distribution in the conditional flow matching to be condition-dependent, encouraging stronger condition integration and preventing loss collapse.

**Scope:** The paper provides theoretical justification and extensive empirical results across simulation and real-world benchmarks.

The paper was submitted on May 16, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "7942421c-5f67-4cdd-b2a2-6f28e4a240ac",
  "tool_use_result": {
    "query": "arXiv 2505.11123 \"Conditioning Matters\" Dong authors diffusion policy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X5J7W7Z9VJ5DJg67FtXTwe",
        "content": [
          {
            "title": "[2505.11123] Conditioning Matters: Training Diffusion Policies is Faster Than You Think",
            "url": "https://arxiv.org/abs/2505.11123"
          },
          {
            "title": "Conditioning Matters: Training Diffusion Policies is Faster Than You Think",
            "url": "https://arxiv.org/html/2505.11123"
          },
          {
            "title": "Unpacking the Individual Components of Diffusion Policy",
            "url": "https://arxiv.org/html/2412.00084v1"
          },
          {
            "title": "Unpacking the Individual Components of Diffusion Policy",
            "url": "https://arxiv.org/pdf/2412.00084"
          },
          {
            "title": "VLM-TDP: VLM-guided Trajectory-conditioned Diffusion Policy for Robust Long-Horizon Manipulation",
            "url": "https://arxiv.org/pdf/2507.04524"
          },
          {
            "title": "Factorizing Diffusion Policies for Observation Modality Prioritization",
            "url": "https://arxiv.org/pdf/2509.16830"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2505.11123:\n\n**Paper Title:** Conditioning Matters: Training Diffusion Policies is Faster Than You Think\n\n**Authors:** Zibin Dong, Yicheng Liu, Yinchuan Li, Hang Zhao, Jianye Hao\n\n**Main Contribution:** The paper identifies a fundamental challenge in conditional diffusion policy training: when generative conditions are hard to distinguish, the training objective degenerates into modeling the marginal action distribution, a phenomenon termed loss collapse.\n\n**Proposed Solution:** The authors propose Cocos, a simple yet general solution that modifies the source distribution in the conditional flow matching to be condition-dependent, encouraging stronger condition integration and preventing loss collapse.\n\n**Scope:** The paper provides theoretical justification and extensive empirical results across simulation and real-world benchmarks.\n\nThe paper was submitted on May 16, 2025."
    ],
    "durationSeconds": 5.9303614640000015
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need:

1. `\dfCAR` is defined in main.tex as `\newcommand{\dfCAR}{\text{dfCAR}}` and used in 2 files (main.tex definition + related_work.tex usage). Since it's a defined command used consistently, the task says to change it to `CAR$_\text{f}$` unless `\dfCAR` is defined in main.tex and used consistently. It IS defined, but the task explicitly says to change it. Let me re-read the task:

"找到 line 50（或附近）的 `$\dfCAR$`，改为 `CAR$_\text{f}$`。

全文符号统一用 `CAR$_\text{f}$`，不要用 `\dfCAR` 命令（除非 main.tex 中定义了该命令且全文统一使用）。"

So the exception applies: main.tex defines `\dfCAR` and it's used consistently. But wait - it only appears twice: once in the definition and once in related_work.tex. That's not really "全文统一使用" (used consistently throughout). Let me check the grep results more carefully to see if there are other occurrences I'm missing.

Actually, looking at the actual usage: `\dfCAR` is defined in main.tex but only appears once in the text itself (in related_work.tex). The task specifies the exception only applies if it's defined AND used consistently throughout the document. Since it's barely used, I should switch to the standard format `CAR$_\text{f}$` instead. The task is specifically asking me to change line 50 in related_work.tex to use `CAR$_\text{f}$` directly. Since the `\dfCAR` command is only used in that one location and not consistently throughout the paper, I should replace it with the explicit formatting rather than keep the command definition.

I need to make three changes: update the symbol in related_work.tex, add the Dong et al. 2025 reference to the bibliography with the authors I found, and incorporate a sentence or two about action collapse into the evaluation section. I should also verify whether the `sec:dfcar` label needs adjustment if we're moving away from the command-based notation.

For the evaluation paragraph addition, I'm looking at what the task specifies—essentially that action collapse has been observed in diffusion policy training before, but its systematic impact on safety metrics like CAR hasn't been documented until now, which is what CAR_f is designed to address. The bibliography entry doesn't have an explicit key specified yet, so I'll need to derive one from the paper ID or create a sensible citation key.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "124acec6-3ec2-40d9-a439-6ecbf4ac06b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WxouRacUpowbv2FX7fAGV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 35711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 821
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 33_

`\dfCAR` is defined in main.tex but only used once (in related_work.tex). Not "全文统一使用", so I'll replace it. Authors confirmed: Zibin Dong, Yicheng Liu, Yinchuan Li, Hang Zhao, Jianye Hao. Let me read the end of references.bib to add the new entry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "6895ba86-540a-4b82-a8b7-9b04d6cdfac7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WxouRacUpowbv2FX7fAGV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 35711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 821
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01Pd6oJBXHiBXnipwGRu9JYV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
  "offset": 260
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "d37fe3bc-6acd-40be-b7b4-b7f78dc72d46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WxouRacUpowbv2FX7fAGV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 35711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 821
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T16:28:06.339Z_

<details><summary>↩ Tool result · `toolu_01Pd6oJBXHiBXnipwGRu9JYV`</summary>

```text
260	}
261	
262	@article{augvla3d2026,
263	  title={{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},
264	  author={Rao, Zhifeng and Chen, Wenlong and Xie, Lei and Hua, Xia and Yin, Dongfu and Tian, Zhen and Yu, F. Richard},
265	  journal={arXiv preprint arXiv:2602.10698},
266	  year={2026}
267	}
268	
269	@article{evodepth2026,
270	  title={{Evo-Depth}: A Lightweight Depth-Enhanced Vision-Language-Action Model},
271	  author={Lin, Tao and Du, Yuxin and Liu, Jiting and Zhu, Nuobei and Li, Yunhe and Fu, Yuqian and Chen, Yinxinyu and Cai, Hongyi and Ye, Zewei and Cheng, Bing and others},
272	  journal={arXiv preprint arXiv:2605.14950},
273	  year={2026}
274	}
275	
276	% ===== Action Refinement =====
277	
278	@article{chen2026dfmvla,
279	  title={{DFM-VLA}: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching},
280	  author={Chen, Jiayi and Song, Wenxuan and Chen, Shuai and Wang, Jingbo and Li, Zhijun and Li, Haoang},
281	  journal={arXiv preprint arXiv:2603.26320},
282	  year={2026}
283	}
284	
285	% ===== Parameter-Efficient Fine-Tuning =====
286	
287	@inproceedings{hu2022lora,
288	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
289	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
290	  booktitle = {International Conference on Learning Representations (ICLR)},
291	  year      = {2022},
292	}
293	
294	% ===== VLA Safety Survey =====
295	
296	@article{li2026vlasafety,
297	  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
298	  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},
299	  journal={arXiv preprint arXiv:2604.23775},
300	  year={2026}
301	}
302	
303	% ===== Evaluation Methodology =====
304	
305	@article{snyder2026beyond,
306	  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},
307	  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},
308	  journal={arXiv preprint arXiv:2603.13616},
309	  year={2026}
310	}
311	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "8caa17df-60e5-4c9f-8601-7b33652e3b30",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
      "content": "}\n\n@article{augvla3d2026,\n  title={{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},\n  author={Rao, Zhifeng and Chen, Wenlong and Xie, Lei and Hua, Xia and Yin, Dongfu and Tian, Zhen and Yu, F. Richard},\n  journal={arXiv preprint arXiv:2602.10698},\n  year={2026}\n}\n\n@article{evodepth2026,\n  title={{Evo-Depth}: A Lightweight Depth-Enhanced Vision-Language-Action Model},\n  author={Lin, Tao and Du, Yuxin and Liu, Jiting and Zhu, Nuobei and Li, Yunhe and Fu, Yuqian and Chen, Yinxinyu and Cai, Hongyi and Ye, Zewei and Cheng, Bing and others},\n  journal={arXiv preprint arXiv:2605.14950},\n  year={2026}\n}\n\n% ===== Action Refinement =====\n\n@article{chen2026dfmvla,\n  title={{DFM-VLA}: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching},\n  author={Chen, Jiayi and Song, Wenxuan and Chen, Shuai and Wang, Jingbo and Li, Zhijun and Li, Haoang},\n  journal={arXiv preprint arXiv:2603.26320},\n  year={2026}\n}\n\n% ===== Parameter-Efficient Fine-Tuning =====\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n}\n\n% ===== VLA Safety Survey =====\n\n@article{li2026vlasafety,\n  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},\n  journal={arXiv preprint arXiv:2604.23775},\n  year={2026}\n}\n\n% ===== Evaluation Methodology =====\n\n@article{snyder2026beyond,\n  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},\n  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},\n  journal={arXiv preprint arXiv:2603.13616},\n  year={2026}\n}\n",
      "numLines": 52,
      "startLine": 260,
      "totalLines": 311
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

````text
I also need to check if there's a section for action collapse or if I should add it under a specific section in the bib file. Let me also check what sections exist.

Now let me also check for Goodhart and annotation artifacts references to see where the action collapse citation fits best.

Looking at line 50 in related_work.tex:
```
We propose displacement-filtered CAR ($\dfCAR$, \S\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.


```

I need to update the notation from `$\dfCAR$` to `CAR$_\text{f}$`, then add 1-2 sentences about action collapse before this proposal sentence to connect it to the existing discussion, citing Dong et al. 2025. The action collapse context should flow naturally into the CAR_f introduction, and I'll need to add the corresponding bibliography entry.

```
Action collapse in diffusion policies—where models degenerate into capturing marginal action distributions rather than condition-specific behavior—has been documented as a training pathology, but its systematic contamination of safety metrics like CAR hasn't been previously identified. This is the gap that displacement-filtered CAR addresses by excluding low-motion episodes to isolate genuine avoidance behavior.
``` I'm refining the phrasing to be more direct and specific—replacing "has been identified" with "has been observed" and clarifying that this systematic contamination of safety metrics like CAR is the novel contribution here, then finalizing the edits across the full passage.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "905f8b5a-d6b7-44dc-a235-fe9b748575a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4u1zhF8a2Eqma6GyUdWZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2544,
      "cache_read_input_tokens": 36532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2544
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 37_

Now I have everything I need. Let me make all three changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "859662a1-b6c2-46c9-a744-e5e34c180b1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4u1zhF8a2Eqma6GyUdWZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2544,
      "cache_read_input_tokens": 36532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2544
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01JyWT5F8vKGaXc4GyZwaNJv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "old_string": "Recent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nWe propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.",
  "new_string": "Recent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nAction collapse, where a diffusion policy degenerates to modeling the marginal action distribution instead of condition-specific behavior, has been identified as a training failure mode~\\cite{dong2025conditioning}. Its systematic effect on safety evaluation metrics such as CAR, however, has not been previously examined.\nWe propose displacement-filtered CAR (CAR$_\\text{f}$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to detect this contamination and isolate genuine avoidance behavior."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "b9b36379-65ff-4929-8997-db0e749f79bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4u1zhF8a2Eqma6GyUdWZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2544,
      "cache_read_input_tokens": 36532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2544
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T16:28:37.726Z_

<details><summary>↩ Tool result · `toolu_01JyWT5F8vKGaXc4GyZwaNJv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "6f329367-c95c-464e-ace8-def50043e756",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
    "oldString": "Recent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nWe propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.",
    "newString": "Recent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nAction collapse, where a diffusion policy degenerates to modeling the marginal action distribution instead of condition-specific behavior, has been identified as a training failure mode~\\cite{dong2025conditioning}. Its systematic effect on safety evaluation metrics such as CAR, however, has not been previously examined.\nWe propose displacement-filtered CAR (CAR$_\\text{f}$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to detect this contamination and isolate genuine avoidance behavior.",
    "originalFile": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models for Manipulation.}\nVision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.\nRT-2~\\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.\n$\\pi_0$~\\cite{black2024pi0} introduced flow matching~\\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.\nOpenVLA~\\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.\nThese models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\\cite{hu2022lora}.\nRecent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.\nSpatial Forcing~\\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\\cite{li2025qdepth} and DepthVLA~\\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.\nDespite this progress, safety considerations remain largely absent from VLA training and evaluation.\nMost VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.\nThis paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware robot learning spans training-time and test-time approaches.\nAt training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\\%.\nAt test time, several methods apply external safety filters to learned policies.\nVLSA~\\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.\nCoFreeVLA~\\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.\niKinQP-RL~\\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.\nIn the diffusion policy setting, \\citet{li2024langguided} and CAPE~\\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.\nA recent survey~\\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.\nCommon to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.\nThe end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.\nThis work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSigned distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.\nDeepSDF~\\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.\nIn robotics, SDFs serve perception, planning, and control.\niSDF~\\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.\nVoxPoser~\\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.\nFor motion planning, RAMP~\\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.\nRecent work extends SDFs beyond task space: CSSDF-Net~\\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.\nThese works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.\nCritically, these methods typically query the SDF at the end-effector or a small set of control points, leaving full-body collision awareness as an open problem.\nWe evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nEvaluation of manipulation safety requires metrics beyond binary task success.\nLIBERO~\\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.\nSafeLIBERO, introduced by \\citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.\nTask success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.\nHowever, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores near-perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.\nNeither case reflects learned avoidance behavior.\nThis failure mode echoes broader concerns about metric reliability.\nGoodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.\nRecent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nWe propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.\n",
    "structuredPatch": [
      {
        "oldStart": 47,
        "oldLines": 4,
        "newStart": 47,
        "newLines": 5,
        "lines": [
          " This failure mode echoes broader concerns about metric reliability.",
          " Goodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.",
          " Recent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.",
          "-We propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.",
          "+Action collapse, where a diffusion policy degenerates to modeling the marginal action distribution instead of condition-specific behavior, has been identified as a training failure mode~\\cite{dong2025conditioning}. Its systematic effect on safety evaluation metrics such as CAR, however, has not been previously examined.",
          "+We propose displacement-filtered CAR (CAR$_\\text{f}$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to detect this contamination and isolate genuine avoidance behavior."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_01BCtmk3dT5Fn9NeBJuPgvjU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
  "old_string": "% ===== Evaluation Methodology =====",
  "new_string": "% ===== Action Collapse =====\n\n@article{dong2025conditioning,\n  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},\n  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},\n  journal={arXiv preprint arXiv:2505.11123},\n  year={2025}\n}\n\n% ===== Evaluation Methodology ====="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "224ab7f3-9bd7-4633-a68c-84bd09159f21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4u1zhF8a2Eqma6GyUdWZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2544,
      "cache_read_input_tokens": 36532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2544
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T16:28:40.431Z_

<details><summary>↩ Tool result · `toolu_01BCtmk3dT5Fn9NeBJuPgvjU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "59f2bbbb-d871-4640-bd0c-278d3ecc6517",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
    "oldString": "% ===== Evaluation Methodology =====",
    "newString": "% ===== Action Collapse =====\n\n@article{dong2025conditioning,\n  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},\n  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},\n  journal={arXiv preprint arXiv:2505.11123},\n  year={2025}\n}\n\n% ===== Evaluation Methodology =====",
    "originalFile": "% The Safety Illusion — References\n% Analysis paper on fake safety in VLA collision avoidance evaluation\n% Generated: 2026-05-24\n\n% ===== VLA Foundation Models =====\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Collision-Aware VLA Methods =====\n\n@article{hu2025vlsa,\n  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},\n  journal={arXiv preprint arXiv:2512.11891},\n  year={2025}\n}\n\n@inproceedings{zhang2025safevla,\n  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cofreeevla2026,\n  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},\n  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},\n  journal={arXiv preprint arXiv:2601.21712},\n  year={2026}\n}\n\n@article{spalter2024ikinqp,\n  title={Towards Online Safety Corrections for Robotic Manipulation Policies},\n  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},\n  journal={arXiv preprint arXiv:2409.08233},\n  year={2024}\n}\n\n@inproceedings{li2024langguided,\n  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},\n  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2025}\n}\n\n@article{yang2025cape,\n  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},\n  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},\n  journal={arXiv preprint arXiv:2511.22773},\n  year={2025}\n}\n\n% ===== SDF in Robotics =====\n\n@inproceedings{park2019deepsdf,\n  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},\n  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2019}\n}\n\n@inproceedings{ortiz2022isdf,\n  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},\n  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\\\"o}fer, Michael and Mukadam, Mustafa},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2022}\n}\n\n@article{zhi2021diffco,\n  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},\n  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},\n  journal={IEEE Transactions on Robotics},\n  volume={38},\n  number={5},\n  pages={2668--2685},\n  year={2022}\n}\n\n@inproceedings{huang2023voxposer,\n  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},\n  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Benchmarks and Training =====\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ===== Evaluation Reliability =====\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2018}\n}\n\n@inproceedings{karwowski2024goodhart,\n  title={Goodhart's Law in Reinforcement Learning},\n  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% ===== Diffusion Policy =====\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n% ===== SDF in Robotics (additional) =====\n\n@inproceedings{vasilopoulos2023ramp,\n  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},\n  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},\n  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year={2023}\n}\n\n@article{chen2026cssdfnet,\n  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},\n  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},\n  journal={arXiv preprint arXiv:2603.18669},\n  year={2026}\n}\n\n@article{jacquet2025neuralnmpc,\n  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},\n  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},\n  journal={The International Journal of Robotics Research},\n  year={2025}\n}\n\n@article{chen2025samp,\n  title={{SAMP}: Spatial Anchor-based Motion Policy for Collision-Aware Robotic Manipulators},\n  author={Chen, Kai and Bi, Zhihai and Zhao, Guoyang and Zheng, Chunxin and Li, Yulin and Zhao, Hang and Ma, Jun},\n  journal={arXiv preprint arXiv:2509.11185},\n  year={2025}\n}\n\n@inproceedings{ruan2025profrobot,\n  title={Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions},\n  author={Ruan, Quanyuan and Lei, Jiabao and Yuan, Wenhao and Zhang, Yanglin and Lu, Dekun and Liu, Guiliang and Jia, Kui},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2025}\n}\n\n% ===== 3D-Aware VLA Methods =====\n\n@article{depthvla2025,\n  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},\n  journal={arXiv preprint arXiv:2510.13375},\n  year={2025}\n}\n\n@article{li2025qdepth,\n  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},\n  journal={arXiv preprint arXiv:2510.14836},\n  year={2025}\n}\n\n@article{li2025spatialforcing,\n  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},\n  journal={arXiv preprint arXiv:2510.12276},\n  year={2025}\n}\n\n@article{3dcavla2025,\n  title={{3D CAVLA}: Leveraging Depth and {3D} Context to Generalize Vision Language Action Models for Unseen Tasks},\n  author={Bhat, Vineet and Lan, Yu-Hsiang and Krishnamurthy, Prashanth and Karri, Ramesh and Khorrami, Farshad},\n  journal={arXiv preprint arXiv:2505.05800},\n  year={2025}\n}\n\n@article{geoaware2025,\n  title={{GeoAware-VLA}: Implicit Geometry Aware Vision-Language-Action Model},\n  author={Abouzeid, Ali and Mansour, Malak and Sun, Qinbo and Sun, Zezhou and Song, Dezhen},\n  journal={arXiv preprint arXiv:2509.14117},\n  year={2025}\n}\n\n@inproceedings{spatialvla2025,\n  title={{SpatialVLA}: Exploring Spatial Representations for Visual-Language-Action Model},\n  author={Qu, Delin and Song, Haoming and Chen, Qizhi and Yao, Yuanqi and Ye, Xinyi and Gu, Jiayuan and Wang, Zhigang and Ding, Yan and Zhao, Bin and Wang, Dong and Li, Xuelong},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2025}\n}\n\n@article{gstvla2026,\n  title={{GST-VLA}: Structured Gaussian Spatial Tokens for {3D} Depth-Aware Vision-Language-Action Models},\n  author={Sarowar, Md Selim and Tariq, Omer and Kim, Sungho},\n  journal={arXiv preprint arXiv:2603.09079},\n  year={2026}\n}\n\n@article{stemvla2026,\n  title={{StemVLA}: An Open-Source Vision-Language-Action Model with Future {3D} Spatial Geometry Knowledge and {4D} Historical Representation},\n  author={Xiao, Jiasong and She, Yutao and Li, Kai and Sha, Yuyang and Cheng, Ziang and Tong, Ziang},\n  journal={arXiv preprint arXiv:2602.23721},\n  year={2026}\n}\n\n@article{stvla2026,\n  title={{ST-VLA}: Enabling {4D}-Aware Spatiotemporal Understanding for General Robot Manipulation},\n  author={Wu, You and Chen, Zixuan and Ou, Cunxu and Wang, Wenxuan and Huang, Wenbo and Cao, Lin and Chen, Yangtao and Qiu, Weichao and Quan, Xingyue and Shi, Jieqi and Huo, Jing and Gao, Yang},\n  journal={arXiv preprint arXiv:2603.13788},\n  year={2026}\n}\n\n@article{evo02025,\n  title={{Evo-0}: Vision-Language-Action Model with Implicit Spatial Understanding},\n  author={Lin, Tao and Li, Gen and Zhong, Yilei and Zou, Yanwen and Du, Yuxin and Liu, Jiting and Gu, Encheng and Zhao, Bo},\n  journal={arXiv preprint arXiv:2507.00416},\n  year={2025}\n}\n\n@article{savla2026,\n  title={{SA-VLA}: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning},\n  author={Pan, Xu and Wan, Zhenglin and Yu, Xingrui and Zheng, Xianwei and Ke, Youkai and Sun, Ming and Wang, Rui and Wang, Ziwei and Tsang, Ivor},\n  journal={arXiv preprint arXiv:2602.00743},\n  year={2026}\n}\n\n@article{augvla3d2026,\n  title={{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},\n  author={Rao, Zhifeng and Chen, Wenlong and Xie, Lei and Hua, Xia and Yin, Dongfu and Tian, Zhen and Yu, F. Richard},\n  journal={arXiv preprint arXiv:2602.10698},\n  year={2026}\n}\n\n@article{evodepth2026,\n  title={{Evo-Depth}: A Lightweight Depth-Enhanced Vision-Language-Action Model},\n  author={Lin, Tao and Du, Yuxin and Liu, Jiting and Zhu, Nuobei and Li, Yunhe and Fu, Yuqian and Chen, Yinxinyu and Cai, Hongyi and Ye, Zewei and Cheng, Bing and others},\n  journal={arXiv preprint arXiv:2605.14950},\n  year={2026}\n}\n\n% ===== Action Refinement =====\n\n@article{chen2026dfmvla,\n  title={{DFM-VLA}: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching},\n  author={Chen, Jiayi and Song, Wenxuan and Chen, Shuai and Wang, Jingbo and Li, Zhijun and Li, Haoang},\n  journal={arXiv preprint arXiv:2603.26320},\n  year={2026}\n}\n\n% ===== Parameter-Efficient Fine-Tuning =====\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n}\n\n% ===== VLA Safety Survey =====\n\n@article{li2026vlasafety,\n  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},\n  journal={arXiv preprint arXiv:2604.23775},\n  year={2026}\n}\n\n% ===== Evaluation Methodology =====\n\n@article{snyder2026beyond,\n  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},\n  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},\n  journal={arXiv preprint arXiv:2603.13616},\n  year={2026}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 300,
        "oldLines": 6,
        "newStart": 300,
        "newLines": 15,
        "lines": [
          "   year={2026}",
          " }",
          " ",
          "+% ===== Action Collapse =====",
          "+",
          "+@article{dong2025conditioning,",
          "+  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},",
          "+  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},",
          "+  journal={arXiv preprint arXiv:2505.11123},",
          "+  year={2025}",
          "+}",
          "+",
          " % ===== Evaluation Methodology =====",
          " ",
          " @article{snyder2026beyond,"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 42_

Now let me verify all three conditions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "65af928f-8fc0-4583-b20f-3a3fa64bd270",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RbVAM8ZDmVR57Xp1XrQSo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 39076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1912
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01HdTG9KqWwGcHwU8TSBKdPJ`</summary>

```json
{
  "pattern": "dfCAR",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "df05c6e2-f056-4a68-8573-9760812677b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RbVAM8ZDmVR57Xp1XrQSo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 39076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1912
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T16:28:44.214Z_

<details><summary>↩ Tool result · `toolu_01HdTG9KqWwGcHwU8TSBKdPJ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "e07259dd-8e74-4941-ace3-7c569bd60eef",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_01SZ3wW6D78uwsF8aMStyKQ1`</summary>

```json
{
  "pattern": "dong2025conditioning",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
  "output_mode": "content",
  "-A": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "997bdc06-3818-441e-ab9b-2d66dc435fa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RbVAM8ZDmVR57Xp1XrQSo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 39076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1912
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T16:28:45.136Z_

<details><summary>↩ Tool result · `toolu_01SZ3wW6D78uwsF8aMStyKQ1`</summary>

```text
305:@article{dong2025conditioning,
306-  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},
307-  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},
308-  journal={arXiv preprint arXiv:2505.11123},
309-  year={2025}
310-}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "b0618be9-1b94-49d0-8718-4bd19aaf4fde",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "305:@article{dong2025conditioning,\n306-  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},\n307-  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},\n308-  journal={arXiv preprint arXiv:2505.11123},\n309-  year={2025}\n310-}",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01U5dFJWa3EX9X2CYRxg7bDw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "offset": 46,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "6e8f66ef-7dda-4904-b82f-776e752b8211",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RbVAM8ZDmVR57Xp1XrQSo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 39076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1912
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T16:28:46.227Z_

<details><summary>↩ Tool result · `toolu_01U5dFJWa3EX9X2CYRxg7bDw`</summary>

```text
46	Neither case reflects learned avoidance behavior.
47	This failure mode echoes broader concerns about metric reliability.
48	Goodhart's law in RL~\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.
49	Recent work on statistically rigorous robot evaluation~\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.
50	Action collapse, where a diffusion policy degenerates to modeling the marginal action distribution instead of condition-specific behavior, has been identified as a training failure mode~\cite{dong2025conditioning}. Its systematic effect on safety evaluation metrics such as CAR, however, has not been previously examined.
51	We propose displacement-filtered CAR (CAR$_\text{f}$, \S\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to detect this contamination and isolate genuine avoidance behavior.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "09ab8560-520a-46bb-a376-bcaf67021a02",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
      "content": "Neither case reflects learned avoidance behavior.\nThis failure mode echoes broader concerns about metric reliability.\nGoodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.\nRecent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nAction collapse, where a diffusion policy degenerates to modeling the marginal action distribution instead of condition-specific behavior, has been identified as a training failure mode~\\cite{dong2025conditioning}. Its systematic effect on safety evaluation metrics such as CAR, however, has not been previously examined.\nWe propose displacement-filtered CAR (CAR$_\\text{f}$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to detect this contamination and isolate genuine avoidance behavior.\n",
      "numLines": 7,
      "startLine": 46,
      "totalLines": 52
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

三项验证全部通过：

1. `\dfCAR` 已从 related_work.tex 中移除（grep 无匹配），替换为 `CAR$_\text{f}$`
2. `dong2025conditioning` 条目已添加到 references.bib（完整作者列表：Dong, Zibin; Liu, Yicheng; Li, Yinchuan; Zhao, Hang; Hao, Jianye）
3. Line 50 新增 action collapse 引用句，与后续 CAR$_\text{f}$ 提案句自然衔接

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "uuid": "2c454652-6be6-4fb0-a4aa-7c3da5bd7217",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVARC6WikuHa2nqpmChiYA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 40988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 925
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 50_

三项验证全部通过：

1. `\dfCAR` 已从 related_work.tex 中移除（grep 无匹配），替换为 `CAR$_\text{f}$`
2. `dong2025conditioning` 条目已添加到 references.bib（完整作者列表：Dong, Zibin; Liu, Yicheng; Li, Yinchuan; Zhao, Hang; Hao, Jianye）
3. Line 50 新增 action collapse 引用句，与后续 CAR$_\text{f}$ 提案句自然衔接

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 119790,
  "duration_api_ms": 120758,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "cabde197-a0d6-4c92-8769-d6c3107ffb25",
  "total_cost_usd": 0.4848795,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 30466,
    "cache_read_input_tokens": 282274,
    "output_tokens": 5250,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30466,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 164,
        "cache_read_input_tokens": 40988,
        "cache_creation_input_tokens": 925,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 925
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 10170,
      "outputTokens": 368,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 1,
      "costUSD": 0.022010000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 5250,
      "cacheReadInputTokens": 282274,
      "cacheCreationInputTokens": 30466,
      "webSearchRequests": 0,
      "costUSD": 0.46286950000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "02c7fca6-b408-4132-8c25-7174d61ddd2d"
}
```

</details>

---
