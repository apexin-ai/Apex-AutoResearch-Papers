# paper research

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/workers/worker_paper_research_20260520T200319.log`
- **Structured JSON:** [`48b92bbfb2fda0cfb045.json`](../../sessions/48/48b92bbfb2fda0cfb045.json)

## Before a recorded user message

79 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_figures_and_layout",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "78bda64c-2b04-438a-8f80-df5afedf0fb1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

Let me start by reading the current literature_map.yaml to understand the existing format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "e91042e8-7dce-49d9-8b3a-400f0a6acab6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcwSQ6s7Xzu9iPqDsTAA2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13559,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13559
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

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_01Aa69djFFoyZLbfLPyWojNi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "8c0c891b-cee9-452b-a047-02b77029dd99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcwSQ6s7Xzu9iPqDsTAA2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13559,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13559
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

_source line 5 · 2026-05-20T20:03:28.462Z_

<details><summary>↩ Tool result · `toolu_01Aa69djFFoyZLbfLPyWojNi`</summary>

```text
1	# Literature Map for OccSafe-VLA (AAAI 2027)
2	# Generated: 2026-05-20
3	# Paper: OccSafe-VLA: Occupancy-Conditioned Safety for VLA via Systematic Spatial-Safety Interaction Analysis
4	#
5	# Core gap: No work studies the interaction between spatial representations and safety
6	# mechanisms in VLAs. 15+ spatial-VLA papers never evaluate collision metrics;
7	# all safety-VLA methods ignore spatial representation advances.
8	
9	papers:
10	
11	  # ============================================================
12	  # CATEGORY: direct-competitor (spatial-safety intersection)
13	  # ============================================================
14	
15	  - id: "liu2025occvla"
16	    title: "OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision"
17	    authors: "Liu et al."
18	    venue: "arXiv preprint"
19	    year: 2025
20	    arxiv: "2509.05578"
21	    category: "direct-competitor"
22	    role: "最近概念：occupancy + VLA，但面向自动驾驶"
23	    key_finding: "将 3D 占据预测作为 VLA 辅助任务，学习空间结构，推理时可跳过（零开销）。在 nuScenes 轨迹规划上达到 SOTA"
24	    our_differentiation: "OccVLA 仅验证自动驾驶；我们将占据辅助迁移到 manipulation，需解决精度尺度（厘米级 vs 米级）和动作空间差异"
25	
26	  - id: "hu2025aegis"
27	    title: "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer"
28	    authors: "Hu et al."
29	    venue: "arXiv preprint"
30	    year: 2025
31	    arxiv: "2512.11891"
32	    category: "direct-competitor"
33	    role: "唯一发表的 manipulation safety-VLA，plug-in CBF 方案"
34	    key_finding: "AEGIS plug-in 安全约束层用 CBF + 开放集检测 + 深度图，SafeLIBERO 上 CAR 提升 59.16%"
35	    our_differentiation: "AEGIS 是 plug-in 后处理，不影响 VLA 内部空间理解；我们将占据感知内化到 VLA 架构，实现预见性避障而非事后修正"
36	
37	  - id: "zhan2025safevla"
38	    title: "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning"
39	    authors: "Zhan et al."
40	    venue: "NeurIPS 2025 Spotlight"
41	    year: 2025
42	    arxiv: "2503.03480"
43	    category: "direct-competitor"
44	    role: "RL-based VLA 安全对齐，NeurIPS 2025 Spotlight"
45	    key_finding: "用约束马尔可夫决策过程进行 VLA 安全对齐"
46	    our_differentiation: "SafeVLA 用 RL 方法，不涉及几何/占据表征；我们是几何驱动的空间-安全交互方案"
47	
48	  - id: "chen2026cofreevla"
49	    title: "CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation"
50	    authors: "Chen et al."
51	    venue: "arXiv preprint"
52	    year: 2026
53	    arxiv: "2601.21712"
54	    category: "direct-competitor"
55	    role: "半内化风险估计器 + collision labels"
56	    key_finding: "半内化风险估计器结合模型生成的碰撞标签实现无碰撞双臂操作"
57	    our_differentiation: "CoFreeVLA 不使用占据表征，风险估计不利用空间结构；我们的 OCC-CBF 基于占据特征做语义碰撞推理"
58	
59	  # ============================================================
60	  # CATEGORY: spatial-vla (3D representation for VLA, no safety eval)
61	  # ============================================================
62	
63	  - id: "li2025spatialforcing"
64	    title: "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model"
65	    authors: "Li et al."
66	    venue: "ICLR 2026"
67	    year: 2025
68	    arxiv: "2510.12276"
69	    category: "spatial-vla"
70	    role: "隐式 3D 对齐 SOTA，factorial study 的 general-purpose 3D 条件参考"
71	    key_finding: "将 VLA 中间层视觉嵌入与冻结 3D 基础模型对齐，超越所有 2D/3D VLA 基线，训练加速 3.8x"
72	    our_differentiation: "Spatial Forcing 不产生显式占据场，未评估碰撞安全；我们的 factorial study 将其作为 general-purpose 3D 条件之一"
73	
74	  - id: "an2025depthvla"
75	    title: "DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning"
76	    authors: "An et al."
77	    venue: "arXiv preprint"
78	    year: 2025
79	    arxiv: "2510.13375"
80	    category: "spatial-vla"
81	    role: "深度辅助监督，factorial study 的 general-purpose 3D 条件参考"
82	    key_finding: "通过 mixture-of-transformers 添加深度 transformer，真实世界 78.5% 成功率"
83	    our_differentiation: "DepthVLA 未评估碰撞指标；我们将其与 Spatial Forcing 合并为 factorial 中的 general-purpose 3D 条件"
84	
85	  - id: "chen2026gstvla"
86	    title: "GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models"
87	    authors: "Chen et al."
88	    venue: "arXiv preprint"
89	    year: 2026
90	    arxiv: "2603.09079"
91	    category: "spatial-vla"
92	    role: "最精致的结构化空间表征，LIBERO 96.4%，无安全评估"
93	    key_finding: "128 个各向异性 3D 高斯原语 + DA-CoT 推理，LIBERO 96.4%"
94	    our_differentiation: "GST-VLA 是 ICRA 2027 扩展版的候选条件（Gaussian 空间表征 vs 体素占据）；AAAI 版暂不含"
95	
96	  # ============================================================
97	  # CATEGORY: safety-mechanism (barrier functions / occupancy-based safety)
98	  # ============================================================
99	
100	  - id: "ji2024ogmcbf"
101	    title: "OGM-CBF: Safe Robot Control using Occupancy Grid Map-based Control Barrier Function"
102	    authors: "Ji et al."
103	    venue: "arXiv preprint"
104	    year: 2024
105	    arxiv: "2405.10703"
106	    category: "safety-mechanism"
107	    role: "OCC-CBF 的古典机器人学前身：离散占据网格 + SDF → CBF"
108	    key_finding: "从占据网格图构建 CBF，比原始距离更有效地处理任意障碍物形状"
109	    our_differentiation: "OGM-CBF 用离散网格 + SDF；我们的 OCC-CBF 在 VLA 连续学习特征空间操作，支持语义碰撞推理"
110	
111	  - id: "kwon2026learningnudge"
112	    title: "Learning to Nudge: A Scalable Barrier Function Framework for Safe Robot Interaction in Dense Clutter"
113	    authors: "Kwon et al."
114	    venue: "arXiv preprint"
115	    year: 2026
116	    arxiv: "2601.02686"
117	    category: "safety-mechanism"
118	    role: "学习型可组合 barrier function，manipulation 密集场景"
119	    key_finding: "Dense Contact Barrier Functions (DCBF) — 学习型、可组合、以物体为中心的 barrier function，线性扩展到任意物体集"
120	    our_differentiation: "DCBF 以物体为中心需显式物体分解；OCC-CBF 基于体积占据特征，推理连续空间结构含遮挡区域"
121	
122	  # ============================================================
123	  # CATEGORY: infrastructure (base architecture / benchmarks / recipes)
124	  # ============================================================
125	
126	  - id: "kim2025openvlaoft"
127	    title: "OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"
128	    authors: "Kim et al."
129	    venue: "arXiv preprint"
130	    year: 2025
131	    arxiv: "2502.19645"
132	    category: "infrastructure"
133	    role: "MVP 和 factorial study 的 base architecture"
134	    key_finding: "优化微调配方，LIBERO 97.1%，26x 加速"
135	    our_differentiation: "OpenVLA-OFT 是我们的受控基准架构，不是对比对象"
136	
137	  - id: "ma2026vlanext"
138	    title: "VLANeXt: Recipes for Building Strong VLA Models"
139	    authors: "Ma et al."
140	    venue: "arXiv preprint"
141	    year: 2026
142	    arxiv: "2602.18532"
143	    category: "infrastructure"
144	    role: "系统性 VLA 设计空间探索，我们工作的正交互补"
145	    key_finding: "12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制"
146	    our_differentiation: "VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度"
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "3956586a-e8da-40a4-a4c4-51b3d4aeafb9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/literature_map.yaml",
      "content": "# Literature Map for OccSafe-VLA (AAAI 2027)\n# Generated: 2026-05-20\n# Paper: OccSafe-VLA: Occupancy-Conditioned Safety for VLA via Systematic Spatial-Safety Interaction Analysis\n#\n# Core gap: No work studies the interaction between spatial representations and safety\n# mechanisms in VLAs. 15+ spatial-VLA papers never evaluate collision metrics;\n# all safety-VLA methods ignore spatial representation advances.\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor (spatial-safety intersection)\n  # ============================================================\n\n  - id: \"liu2025occvla\"\n    title: \"OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision\"\n    authors: \"Liu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.05578\"\n    category: \"direct-competitor\"\n    role: \"最近概念：occupancy + VLA，但面向自动驾驶\"\n    key_finding: \"将 3D 占据预测作为 VLA 辅助任务，学习空间结构，推理时可跳过（零开销）。在 nuScenes 轨迹规划上达到 SOTA\"\n    our_differentiation: \"OccVLA 仅验证自动驾驶；我们将占据辅助迁移到 manipulation，需解决精度尺度（厘米级 vs 米级）和动作空间差异\"\n\n  - id: \"hu2025aegis\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.11891\"\n    category: \"direct-competitor\"\n    role: \"唯一发表的 manipulation safety-VLA，plug-in CBF 方案\"\n    key_finding: \"AEGIS plug-in 安全约束层用 CBF + 开放集检测 + 深度图，SafeLIBERO 上 CAR 提升 59.16%\"\n    our_differentiation: \"AEGIS 是 plug-in 后处理，不影响 VLA 内部空间理解；我们将占据感知内化到 VLA 架构，实现预见性避障而非事后修正\"\n\n  - id: \"zhan2025safevla\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhan et al.\"\n    venue: \"NeurIPS 2025 Spotlight\"\n    year: 2025\n    arxiv: \"2503.03480\"\n    category: \"direct-competitor\"\n    role: \"RL-based VLA 安全对齐，NeurIPS 2025 Spotlight\"\n    key_finding: \"用约束马尔可夫决策过程进行 VLA 安全对齐\"\n    our_differentiation: \"SafeVLA 用 RL 方法，不涉及几何/占据表征；我们是几何驱动的空间-安全交互方案\"\n\n  - id: \"chen2026cofreevla\"\n    title: \"CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.21712\"\n    category: \"direct-competitor\"\n    role: \"半内化风险估计器 + collision labels\"\n    key_finding: \"半内化风险估计器结合模型生成的碰撞标签实现无碰撞双臂操作\"\n    our_differentiation: \"CoFreeVLA 不使用占据表征，风险估计不利用空间结构；我们的 OCC-CBF 基于占据特征做语义碰撞推理\"\n\n  # ============================================================\n  # CATEGORY: spatial-vla (3D representation for VLA, no safety eval)\n  # ============================================================\n\n  - id: \"li2025spatialforcing\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv: \"2510.12276\"\n    category: \"spatial-vla\"\n    role: \"隐式 3D 对齐 SOTA，factorial study 的 general-purpose 3D 条件参考\"\n    key_finding: \"将 VLA 中间层视觉嵌入与冻结 3D 基础模型对齐，超越所有 2D/3D VLA 基线，训练加速 3.8x\"\n    our_differentiation: \"Spatial Forcing 不产生显式占据场，未评估碰撞安全；我们的 factorial study 将其作为 general-purpose 3D 条件之一\"\n\n  - id: \"an2025depthvla\"\n    title: \"DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning\"\n    authors: \"An et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2510.13375\"\n    category: \"spatial-vla\"\n    role: \"深度辅助监督，factorial study 的 general-purpose 3D 条件参考\"\n    key_finding: \"通过 mixture-of-transformers 添加深度 transformer，真实世界 78.5% 成功率\"\n    our_differentiation: \"DepthVLA 未评估碰撞指标；我们将其与 Spatial Forcing 合并为 factorial 中的 general-purpose 3D 条件\"\n\n  - id: \"chen2026gstvla\"\n    title: \"GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.09079\"\n    category: \"spatial-vla\"\n    role: \"最精致的结构化空间表征，LIBERO 96.4%，无安全评估\"\n    key_finding: \"128 个各向异性 3D 高斯原语 + DA-CoT 推理，LIBERO 96.4%\"\n    our_differentiation: \"GST-VLA 是 ICRA 2027 扩展版的候选条件（Gaussian 空间表征 vs 体素占据）；AAAI 版暂不含\"\n\n  # ============================================================\n  # CATEGORY: safety-mechanism (barrier functions / occupancy-based safety)\n  # ============================================================\n\n  - id: \"ji2024ogmcbf\"\n    title: \"OGM-CBF: Safe Robot Control using Occupancy Grid Map-based Control Barrier Function\"\n    authors: \"Ji et al.\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2405.10703\"\n    category: \"safety-mechanism\"\n    role: \"OCC-CBF 的古典机器人学前身：离散占据网格 + SDF → CBF\"\n    key_finding: \"从占据网格图构建 CBF，比原始距离更有效地处理任意障碍物形状\"\n    our_differentiation: \"OGM-CBF 用离散网格 + SDF；我们的 OCC-CBF 在 VLA 连续学习特征空间操作，支持语义碰撞推理\"\n\n  - id: \"kwon2026learningnudge\"\n    title: \"Learning to Nudge: A Scalable Barrier Function Framework for Safe Robot Interaction in Dense Clutter\"\n    authors: \"Kwon et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.02686\"\n    category: \"safety-mechanism\"\n    role: \"学习型可组合 barrier function，manipulation 密集场景\"\n    key_finding: \"Dense Contact Barrier Functions (DCBF) — 学习型、可组合、以物体为中心的 barrier function，线性扩展到任意物体集\"\n    our_differentiation: \"DCBF 以物体为中心需显式物体分解；OCC-CBF 基于体积占据特征，推理连续空间结构含遮挡区域\"\n\n  # ============================================================\n  # CATEGORY: infrastructure (base architecture / benchmarks / recipes)\n  # ============================================================\n\n  - id: \"kim2025openvlaoft\"\n    title: \"OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\"\n    authors: \"Kim et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.19645\"\n    category: \"infrastructure\"\n    role: \"MVP 和 factorial study 的 base architecture\"\n    key_finding: \"优化微调配方，LIBERO 97.1%，26x 加速\"\n    our_differentiation: \"OpenVLA-OFT 是我们的受控基准架构，不是对比对象\"\n\n  - id: \"ma2026vlanext\"\n    title: \"VLANeXt: Recipes for Building Strong VLA Models\"\n    authors: \"Ma et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.18532\"\n    category: \"infrastructure\"\n    role: \"系统性 VLA 设计空间探索，我们工作的正交互补\"\n    key_finding: \"12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制\"\n    our_differentiation: \"VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度\"\n",
      "numLines": 147,
      "startLine": 1,
      "totalLines": 147
    }
  }
}
```

</details>

---

### Runtime record

_source line 6_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779315000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "59aee2b7-fce1-491e-bbd4-0e9681077593",
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249"
}
```

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file. Let me understand the format and prepare all 19 new entries. I need to verify some arXiv IDs via web search. Let me batch verify a few key ones, but the task says "优先信任 IDEA_BRIEF 提供的 arXiv ID" so I'll trust most of them and do a quick batch verification.

Let me construct the entries and append them to the file. I'll organize them by category as specified.

Let me build all the entries now. I need to be careful about:
1. Matching the existing YAML format exactly


2. Placing entries in the right category sections
3. Not duplicating existing entries

The existing structure has 4 category sections with comments. I should append new entries within their respective sections. Since the entries are just in a flat list under `papers:`, I can add them at the end with appropriate category comments to keep things organized.

Now I'm looking at the file structure more carefully—it's a flat YAML list where each entry has a `category` field, and the comment headers are just for readability. So I'll append all new entries at the end, grouped by category with comments. I need to map out the entries and extract author names from the paper IDs, using the "First Author et al." format for the titles. I need to do batch web searches to verify the arXiv IDs and collect author information for these papers, since the task prioritizes trusting the provided IDs but still requires verification. Let me search through several batches at once to gather the missing author names and confirm the details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "8a19f4a8-c0c1-4f28-8986-1d01dea9d2b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ja7ikYkh8qPuRYhzHNzrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3091,
      "cache_read_input_tokens": 25400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3091
      },
      "output_tokens": 10,
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

_source line 8_

Now let me batch verify arXiv IDs and get author names for the papers. I'll search in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "13da2af7-e6b0-41c5-a672-a4aeb8955f17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ja7ikYkh8qPuRYhzHNzrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3091,
      "cache_read_input_tokens": 25400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3091
      },
      "output_tokens": 10,
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

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WJYrsb3fgVmxGFeNjZJ4XZ`</summary>

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
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "6d3bce57-098a-4a34-a68c-1c3dd89fd499",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ja7ikYkh8qPuRYhzHNzrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3091,
      "cache_read_input_tokens": 25400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3091
      },
      "output_tokens": 10,
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

_source line 10 · 2026-05-20T20:03:51.468Z_

<details><summary>↩ Tool result · `toolu_01WJYrsb3fgVmxGFeNjZJ4XZ`</summary>

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
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "aff1f23e-5089-46c6-8966-cff9b37ae759",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me do parallel web searches to verify arXiv IDs and get author names for the papers I need to add. I'll batch them into a few searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "c960e3b6-745b-4026-9127-91d239bd2c15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

_source line 12_

Let me batch verify the arXiv IDs and get author names in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "c181cbf6-baeb-4e34-878f-11b81ea02efa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WN8cMUwsjQFQio6xr5WrMq`</summary>

```json
{
  "query": "arXiv 2501.15830 SpatialVLA Exploring Spatial Representations",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "925fa6a5-65b4-4368-9713-d71d86982fc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kq1w6SDorVkYTih4AEpiMq`</summary>

```json
{
  "query": "arXiv 2510.14836 QDepth-VLA quantized depth prediction",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "62836094-de19-4211-ba2a-9304dbe7b4c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VfTWLZ3DpYo3LcNZxGbBQo`</summary>

```json
{
  "query": "arXiv 2509.14117 GeoAware implicit geometry VLA",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "6887f357-1874-4b0d-a33a-56a8b74a4da6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012c4PA6S6N1z2cbmb6Dy8gG`</summary>

```json
{
  "query": "arXiv 2602.10698 AugVLA-3D depth-driven feature augmentation",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "b9b2849f-90a0-45cd-bdfd-e8e84dc2f5fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GJGmrpXUV84pW5VcqX5FC2`</summary>

```json
{
  "query": "arXiv 2507.00416 Evo-0 vision language action implicit spatial",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "7955f0b9-aef6-4eec-b9e5-07c7d5569a55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UaaY234HkFatEFtNS94PeQ`</summary>

```json
{
  "query": "arXiv 2603.22760 SG-VLA spatially-grounded mobile manipulation",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "55afbb09-b527-49b9-aa5a-605b8f5195e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVfTjZU59Cd1oiYFCtsvoh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 28491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
      },
      "output_tokens": 33,
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

_source line 19 · 2026-05-20T20:04:02.923Z_

<details><summary>↩ Tool result · `toolu_01Kq1w6SDorVkYTih4AEpiMq`</summary>

```text
Web search results for query: "arXiv 2510.14836 QDepth-VLA quantized depth prediction"

Links: [{"title":"[2510.14836] QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.14836"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.14836"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision–Language–Action Models","url":"https://arxiv.org/html/2510.14836v1"},{"title":"DepthVLA: Enhancing Vision-Language-Action Models with","url":"https://arxiv.org/pdf/2510.13375"},{"title":"QuartDepth: Post-Training Quantization for Real-Time Depth Estimation on the Edge","url":"https://arxiv.org/html/2503.16709v1"},{"title":"[2510.13375] DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning","url":"https://arxiv.org/abs/2510.13375"}]

Based on the search results, here's what I found about arXiv paper 2510.14836:

## QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models

The paper is titled "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models" by Yixuan Li and 5 other authors.

**Key Contributions:**

QDepth-VLA is a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues.

**Problem Addressed:**

Spatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control.

**Results:**

Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

The paper was submitted on October 16, 2025, with a revised version on December 22, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "bc9a6f96-d402-439c-8fab-a2478bc614dc",
  "tool_use_result": {
    "query": "arXiv 2510.14836 QDepth-VLA quantized depth prediction",
    "results": [
      {
        "tool_use_id": "srvtoolu_012vwtoJc4TkDkiBzdDRhDEy",
        "content": [
          {
            "title": "[2510.14836] QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.14836"
          },
          {
            "title": "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.14836"
          },
          {
            "title": "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision–Language–Action Models",
            "url": "https://arxiv.org/html/2510.14836v1"
          },
          {
            "title": "DepthVLA: Enhancing Vision-Language-Action Models with",
            "url": "https://arxiv.org/pdf/2510.13375"
          },
          {
            "title": "QuartDepth: Post-Training Quantization for Real-Time Depth Estimation on the Edge",
            "url": "https://arxiv.org/html/2503.16709v1"
          },
          {
            "title": "[2510.13375] DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning",
            "url": "https://arxiv.org/abs/2510.13375"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2510.14836:\n\n## QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\n\nThe paper is titled \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\" by Yixuan Li and 5 other authors.\n\n**Key Contributions:**\n\nQDepth-VLA is a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues.\n\n**Problem Addressed:**\n\nSpatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control.\n\n**Results:**\n\nExperimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.\n\nThe paper was submitted on October 16, 2025, with a revised version on December 22, 2025."
    ],
    "durationSeconds": 6.254309313999999
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T20:04:03.588Z_

<details><summary>↩ Tool result · `toolu_01WN8cMUwsjQFQio6xr5WrMq`</summary>

```text
Web search results for query: "arXiv 2501.15830 SpatialVLA Exploring Spatial Representations"

Links: [{"title":"[2501.15830v5] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/abs/2501.15830v5"},{"title":"[2501.15830] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/abs/2501.15830"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://arxiv.org/html/2501.15830v1"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/html/2501.15830v5"},{"title":"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://arxiv.org/html/2510.12276v1"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual- ...","url":"https://arxiv.org/pdf/2501.15830"},{"title":"SEM: Enhancing Spatial Understanding for Robust Robot Manipulation","url":"https://arxiv.org/html/2505.16196"}]

Based on the search results, here's information about arXiv paper 2501.15830 on SpatialVLA:

SpatialVLA explores effective spatial representations for the robot foundation model, claiming that spatial understanding is the keypoint in robot manipulation.

**Key Technical Contributions:**

The paper introduces Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and proposes Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control.

**Training and Performance:**

SpatialVLA is pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner.

**Results:**

The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability.

The paper was submitted on January 27, 2025, and the latest version (v5) was revised on May 19, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "0fec9e40-59ba-41e8-8dec-f67ec8f960ff",
  "tool_use_result": {
    "query": "arXiv 2501.15830 SpatialVLA Exploring Spatial Representations",
    "results": [
      {
        "tool_use_id": "srvtoolu_018cLwQLqezi2CgJD4f27gPJ",
        "content": [
          {
            "title": "[2501.15830v5] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model",
            "url": "https://arxiv.org/abs/2501.15830v5"
          },
          {
            "title": "[2501.15830] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model",
            "url": "https://arxiv.org/abs/2501.15830"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models",
            "url": "https://arxiv.org/html/2501.15830v1"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model",
            "url": "https://arxiv.org/html/2501.15830v5"
          },
          {
            "title": "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model",
            "url": "https://arxiv.org/html/2510.12276v1"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual- ...",
            "url": "https://arxiv.org/pdf/2501.15830"
          },
          {
            "title": "SEM: Enhancing Spatial Understanding for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2505.16196"
          }
        ]
      },
      "Based on the search results, here's information about arXiv paper 2501.15830 on SpatialVLA:\n\nSpatialVLA explores effective spatial representations for the robot foundation model, claiming that spatial understanding is the keypoint in robot manipulation.\n\n**Key Technical Contributions:**\n\nThe paper introduces Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and proposes Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control.\n\n**Training and Performance:**\n\nSpatialVLA is pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner.\n\n**Results:**\n\nThe superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability.\n\nThe paper was submitted on January 27, 2025, and the latest version (v5) was revised on May 19, 2025."
    ],
    "durationSeconds": 7.8755905399999975
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T20:04:04.432Z_

<details><summary>↩ Tool result · `toolu_01UaaY234HkFatEFtNS94PeQ`</summary>

```text
Web search results for query: "arXiv 2603.22760 SG-VLA spatially-grounded mobile manipulation"

Links: [{"title":"[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/abs/2603.22760"},{"title":"[2603.22760v1] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/abs/2603.22760v1"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/html/2603.22760v1"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"},{"title":"[2601.14649] Spatially Generalizable Mobile Manipulation via Adaptive Experience Selection and Dynamic Imagination","url":"https://arxiv.org/abs/2601.14649"}]

Based on the search results, I found the arXiv paper you're looking for:

**SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation**

The paper is authored by Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, and Zhuowen Tu from UC San Diego and Lambda, Inc., and was submitted on March 24, 2026.

**Overview:**

Mobile manipulation tasks require robots to simultaneously reason about global scene layout, fine-grained object geometry, and high-dimensional continuous actions, making standard imitation learning insufficient for robust control.

**Main Contribution:**

The paper introduces a framework for learning spatially-grounded VLA models that strengthens both perception and representation learning through auxiliary task co-training and multi-modal input enhancement, addressing the challenge of controlling a 13-dimensional action space involving coordinated base motion, arm articulation, and gripper actuation.

**Technical Approach:**

The model incorporates multi-view RGB observations, depth cues, and short temporal history, and co-trains auxiliary decoders that reconstruct interpretable intermediate signals including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks from shared visual-language features.

You can access the paper directly at https://arxiv.org/abs/2603.22760


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "30549b94-b826-4dd3-a68a-ef42ee6f6773",
  "tool_use_result": {
    "query": "arXiv 2603.22760 SG-VLA spatially-grounded mobile manipulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BK9gMxwB7P6n1ie5aLHCjh",
        "content": [
          {
            "title": "[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/abs/2603.22760"
          },
          {
            "title": "[2603.22760v1] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/abs/2603.22760v1"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/html/2603.22760v1"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/pdf/2603.22760"
          },
          {
            "title": "[2601.14649] Spatially Generalizable Mobile Manipulation via Adaptive Experience Selection and Dynamic Imagination",
            "url": "https://arxiv.org/abs/2601.14649"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper you're looking for:\n\n**SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation**\n\nThe paper is authored by Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, and Zhuowen Tu from UC San Diego and Lambda, Inc., and was submitted on March 24, 2026.\n\n**Overview:**\n\nMobile manipulation tasks require robots to simultaneously reason about global scene layout, fine-grained object geometry, and high-dimensional continuous actions, making standard imitation learning insufficient for robust control.\n\n**Main Contribution:**\n\nThe paper introduces a framework for learning spatially-grounded VLA models that strengthens both perception and representation learning through auxiliary task co-training and multi-modal input enhancement, addressing the challenge of controlling a 13-dimensional action space involving coordinated base motion, arm articulation, and gripper actuation.\n\n**Technical Approach:**\n\nThe model incorporates multi-view RGB observations, depth cues, and short temporal history, and co-trains auxiliary decoders that reconstruct interpretable intermediate signals including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks from shared visual-language features.\n\nYou can access the paper directly at https://arxiv.org/abs/2603.22760"
    ],
    "durationSeconds": 4.283472050999997
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T20:04:05.431Z_

<details><summary>↩ Tool result · `toolu_01VfTWLZ3DpYo3LcNZxGbBQo`</summary>

```text
Web search results for query: "arXiv 2509.14117 GeoAware implicit geometry VLA"

Links: [{"title":"[2509.14117] GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model","url":"https://arxiv.org/abs/2509.14117"},{"title":"GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model","url":"https://arxiv.org/html/2509.14117"},{"title":"GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model","url":"https://arxiv.org/pdf/2509.14117"},{"title":"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://arxiv.org/html/2510.12276v1"},{"title":"[2512.16811] GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation","url":"https://arxiv.org/abs/2512.16811"}]

Based on the search results, here's what I found about arXiv paper 2509.14117:

## GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model

GeoAware-VLA is a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone.

**The Problem:** Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images.

**The Solution:** The approach leverages a frozen, pretrained geometric vision model as a feature extractor, with a lightweight, trainable projection layer that adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch.

**Results:** Through extensive evaluations on the LIBERO and CALVIN benchmarks, GeoAware-VLA achieves substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. These gains transfer to the physical world, where the model shows significant improvement on a real robotic platform.

**Authors:** The paper is by Ali Abouzeid, Malak Mansour, Qinbo Sun, Zezhou Sun, and Dezhen Song.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "df01da52-32f5-4ded-b436-6f7176497e26",
  "tool_use_result": {
    "query": "arXiv 2509.14117 GeoAware implicit geometry VLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TTqzJmL5iS44bQRt41LTB1",
        "content": [
          {
            "title": "[2509.14117] GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model",
            "url": "https://arxiv.org/abs/2509.14117"
          },
          {
            "title": "GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2509.14117"
          },
          {
            "title": "GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2509.14117"
          },
          {
            "title": "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model",
            "url": "https://arxiv.org/html/2510.12276v1"
          },
          {
            "title": "[2512.16811] GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation",
            "url": "https://arxiv.org/abs/2512.16811"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2509.14117:\n\n## GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model\n\nGeoAware-VLA is a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone.\n\n**The Problem:** Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images.\n\n**The Solution:** The approach leverages a frozen, pretrained geometric vision model as a feature extractor, with a lightweight, trainable projection layer that adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch.\n\n**Results:** Through extensive evaluations on the LIBERO and CALVIN benchmarks, GeoAware-VLA achieves substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. These gains transfer to the physical world, where the model shows significant improvement on a real robotic platform.\n\n**Authors:** The paper is by Ali Abouzeid, Malak Mansour, Qinbo Sun, Zezhou Sun, and Dezhen Song."
    ],
    "durationSeconds": 7.817210565000002
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T20:04:05.583Z_

<details><summary>↩ Tool result · `toolu_012c4PA6S6N1z2cbmb6Dy8gG`</summary>

```text
Web search results for query: "arXiv 2602.10698 AugVLA-3D depth-driven feature augmentation"

Links: [{"title":"[2602.10698] AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.10698"},{"title":"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2602.10698"},{"title":"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.10698v1"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.14836"},{"title":"Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds","url":"https://arxiv.org/pdf/2602.00807"}]

Based on the search results, here's what I found about arXiv paper 2602.10698:

## AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models

Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic perception and control, yet most existing approaches primarily rely on VLM trained using 2D images, which limits their spatial understanding and action grounding in complex 3D environments.

### Approach

The proposed framework integrates depth estimation into VLA models to enrich 3D feature representations. Specifically, it employs a depth estimation baseline called VGGT to extract geometry-aware 3D cues from standard RGB inputs, enabling efficient utilization of existing large-scale 2D datasets while implicitly recovering 3D structural information.

### Key Innovation: Action Assistant Module

To further enhance the reliability of these depth-derived features, the authors introduce a new module called action assistant, which constrains the learned 3D representations with action priors and ensures their consistency with downstream control tasks.

### Results and Impact

By fusing the enhanced 3D features with conventional 2D visual tokens, the approach significantly improves the generalization ability and robustness of VLA models. Experimental results demonstrate that the proposed method not only strengthens perception in geometrically ambiguous scenarios but also leads to superior action prediction accuracy.

The paper was submitted on February 11, 2026, and represents a contribution to improving how robotic systems can understand and act in 3D environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "2fe8aaec-fb57-4c50-9bbb-5440fe5f8c64",
  "tool_use_result": {
    "query": "arXiv 2602.10698 AugVLA-3D depth-driven feature augmentation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EgN4mPJBjzYkyjxQGpeipD",
        "content": [
          {
            "title": "[2602.10698] AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2602.10698"
          },
          {
            "title": "AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2602.10698"
          },
          {
            "title": "AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.10698v1"
          },
          {
            "title": "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.14836"
          },
          {
            "title": "Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
            "url": "https://arxiv.org/pdf/2602.00807"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2602.10698:\n\n## AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models\n\nVision-Language-Action (VLA) models have recently achieved remarkable progress in robotic perception and control, yet most existing approaches primarily rely on VLM trained using 2D images, which limits their spatial understanding and action grounding in complex 3D environments.\n\n### Approach\n\nThe proposed framework integrates depth estimation into VLA models to enrich 3D feature representations. Specifically, it employs a depth estimation baseline called VGGT to extract geometry-aware 3D cues from standard RGB inputs, enabling efficient utilization of existing large-scale 2D datasets while implicitly recovering 3D structural information.\n\n### Key Innovation: Action Assistant Module\n\nTo further enhance the reliability of these depth-derived features, the authors introduce a new module called action assistant, which constrains the learned 3D representations with action priors and ensures their consistency with downstream control tasks.\n\n### Results and Impact\n\nBy fusing the enhanced 3D features with conventional 2D visual tokens, the approach significantly improves the generalization ability and robustness of VLA models. Experimental results demonstrate that the proposed method not only strengthens perception in geometrically ambiguous scenarios but also leads to superior action prediction accuracy.\n\nThe paper was submitted on February 11, 2026, and represents a contribution to improving how robotic systems can understand and act in 3D environments."
    ],
    "durationSeconds": 7.025857944000003
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T20:04:07.539Z_

<details><summary>↩ Tool result · `toolu_01GJGmrpXUV84pW5VcqX5FC2`</summary>

```text
Web search results for query: "arXiv 2507.00416 Evo-0 vision language action implicit spatial"

Links: [{"title":"[2507.00416] Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding","url":"https://arxiv.org/abs/2507.00416"},{"title":"Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding","url":"https://arxiv.org/pdf/2507.00416"},{"title":"Vision-Language-Action Model with Implicit Spatial Understanding","url":"https://www.arxiv.org/pdf/2507.00416v1"},{"title":"GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model","url":"https://arxiv.org/html/2509.14117v4"},{"title":"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://arxiv.org/html/2510.12276v1"},{"title":"Computer Vision and Pattern Recognition Jul 2025","url":"https://arxiv.org/list/cs.CV/2025-07?skip=2250&show=100"},{"title":"Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model","url":"https://arxiv.org/html/2605.14950"},{"title":"From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors","url":"https://arxiv.org/pdf/2510.17439"}]

Based on the search results, here's what I found about arXiv paper 2507.00416:

## Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding

Vision-Language-Action (VLA) models have emerged as a promising framework for enabling generalist robots capable of perceiving, reasoning, and acting in the real world. These models usually build upon pretrained Vision-Language Models (VLMs), which excel at semantic understanding due to large-scale image and text pretraining.

However, existing VLMs typically lack precise spatial understanding capabilities, as they are primarily tuned on 2D image-text pairs without 3D supervision. Recent approaches have incorporated explicit 3D inputs such as point clouds or depth maps, but this necessitates additional depth sensors or pre-trained depth estimation models. In contrast, Evo-0 introduces a plug-and-play module that implicitly incorporates 3D geometry features into VLA models by leveraging an off-the-shelf visual geometry foundation model.

The paper was authored by Tao Lin, Gen Li, Yilei Zhong, Yanwen Zou, Yuxin Du, Jiting Liu, Encheng Gu, and Bo Zhao, and was submitted on July 1, 2025, with the last revision on November 24, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "0019fe44-1519-4341-bbc0-1eb876cf3b0b",
  "tool_use_result": {
    "query": "arXiv 2507.00416 Evo-0 vision language action implicit spatial",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GPYoa2Rcb1BxM75b5bi5JB",
        "content": [
          {
            "title": "[2507.00416] Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding",
            "url": "https://arxiv.org/abs/2507.00416"
          },
          {
            "title": "Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding",
            "url": "https://arxiv.org/pdf/2507.00416"
          },
          {
            "title": "Vision-Language-Action Model with Implicit Spatial Understanding",
            "url": "https://www.arxiv.org/pdf/2507.00416v1"
          },
          {
            "title": "GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2509.14117v4"
          },
          {
            "title": "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model",
            "url": "https://arxiv.org/html/2510.12276v1"
          },
          {
            "title": "Computer Vision and Pattern Recognition Jul 2025",
            "url": "https://arxiv.org/list/cs.CV/2025-07?skip=2250&show=100"
          },
          {
            "title": "Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2605.14950"
          },
          {
            "title": "From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors",
            "url": "https://arxiv.org/pdf/2510.17439"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2507.00416:\n\n## Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding\n\nVision-Language-Action (VLA) models have emerged as a promising framework for enabling generalist robots capable of perceiving, reasoning, and acting in the real world. These models usually build upon pretrained Vision-Language Models (VLMs), which excel at semantic understanding due to large-scale image and text pretraining.\n\nHowever, existing VLMs typically lack precise spatial understanding capabilities, as they are primarily tuned on 2D image-text pairs without 3D supervision. Recent approaches have incorporated explicit 3D inputs such as point clouds or depth maps, but this necessitates additional depth sensors or pre-trained depth estimation models. In contrast, Evo-0 introduces a plug-and-play module that implicitly incorporates 3D geometry features into VLA models by leveraging an off-the-shelf visual geometry foundation model.\n\nThe paper was authored by Tao Lin, Gen Li, Yilei Zhong, Yanwen Zou, Yuxin Du, Jiting Liu, Encheng Gu, and Bo Zhao, and was submitted on July 1, 2025, with the last revision on November 24, 2025."
    ],
    "durationSeconds": 8.0356083
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Good, first batch verified. Let me now search for the remaining papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "0ed94209-fe0e-495e-b899-ce607692477c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 26_

First batch verified. Continuing with the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "9366f24d-9ac5-4974-af19-d6c166f0a3c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETHCAQENRdc42CZVD5LAVU`</summary>

```json
{
  "query": "arXiv 2602.23721 StemVLA open-source future 3D spatial geometry",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "08ce8a65-6a4f-4f18-8712-e067862ba372",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0194EFMGDr8QiTuyWzjzrNqe`</summary>

```json
{
  "query": "arXiv 2505.05800 3D-CAVLA leveraging depth 3D context generalize VLA",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "7f6225ce-5eb8-46a0-997f-99e263eb630f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tPR8ZMwCaevJDXhUC4FE4`</summary>

```json
{
  "query": "arXiv 2603.13788 ST-VLA 4D spatiotemporal understanding robot manipulation",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "9b1b26a0-45cf-4750-87bf-fc2f25a9b36d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N9YqjWqUA1vEyYvvUpo6yi`</summary>

```json
{
  "query": "arXiv 2604.21241 CorridorVLA explicit spatial constraints sparse anchors",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "1c058f8a-48fd-4e12-821b-a8ae1316fc2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SNXo5S9GF14i4BUT7Hmah8`</summary>

```json
{
  "query": "arXiv 2508.09071 GeoVLA point cloud integration",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "0f43825f-9196-48f6-a263-26eb14135254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZh1H1KyajMreNUyAvK8GV`</summary>

```json
{
  "query": "arXiv 2503.07511 PointVLA injecting 3D point cloud features",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "813c36cc-3309-45ec-9b15-452832f65563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBGnCbdg4PZG7JMjNxbPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 29973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 33 · 2026-05-20T20:04:18.038Z_

<details><summary>↩ Tool result · `toolu_01ETHCAQENRdc42CZVD5LAVU`</summary>

```text
Web search results for query: "arXiv 2602.23721 StemVLA open-source future 3D spatial geometry"

Links: [{"title":"[2602.23721] StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation","url":"https://arxiv.org/abs/2602.23721"},{"title":"StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation","url":"https://arxiv.org/pdf/2602.23721"},{"title":"Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding","url":"https://arxiv.org/pdf/2507.00416"},{"title":"[2602.23814] Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation","url":"https://arxiv.org/abs/2602.23814"},{"title":"[2602.03916] SpatiaLab: Can Vision-Language Models Perform Spatial Reasoning in the Wild?","url":"https://arxiv.org/abs/2602.03916"}]

I found the paper! Here's what I found about arXiv 2602.23721:

StemVLA is an open-source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation, submitted on February 27, 2026.

Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics, which may limit spatial reasoning and long-horizon decision-making in dynamic environments.

To address this limitation, the authors propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. Specifically, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Additionally, the model feeds historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations and aggregates them across time using a temporal attention module.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "a7dae2ad-dffe-438b-8924-037092994be9",
  "tool_use_result": {
    "query": "arXiv 2602.23721 StemVLA open-source future 3D spatial geometry",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GAJCHEbXUcXs2zyjFgzCFt",
        "content": [
          {
            "title": "[2602.23721] StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation",
            "url": "https://arxiv.org/abs/2602.23721"
          },
          {
            "title": "StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation",
            "url": "https://arxiv.org/pdf/2602.23721"
          },
          {
            "title": "Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding",
            "url": "https://arxiv.org/pdf/2507.00416"
          },
          {
            "title": "[2602.23814] Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation",
            "url": "https://arxiv.org/abs/2602.23814"
          },
          {
            "title": "[2602.03916] SpatiaLab: Can Vision-Language Models Perform Spatial Reasoning in the Wild?",
            "url": "https://arxiv.org/abs/2602.03916"
          }
        ]
      },
      "I found the paper! Here's what I found about arXiv 2602.23721:\n\nStemVLA is an open-source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation, submitted on February 27, 2026.\n\nVision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics, which may limit spatial reasoning and long-horizon decision-making in dynamic environments.\n\nTo address this limitation, the authors propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. Specifically, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Additionally, the model feeds historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations and aggregates them across time using a temporal attention module."
    ],
    "durationSeconds": 6.615792376999998
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T20:04:19.819Z_

<details><summary>↩ Tool result · `toolu_0194EFMGDr8QiTuyWzjzrNqe`</summary>

```text
Web search results for query: "arXiv 2505.05800 3D-CAVLA leveraging depth 3D context generalize VLA"

Links: [{"title":"[2505.05800] 3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks","url":"https://arxiv.org/abs/2505.05800"},{"title":"3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks","url":"https://arxiv.org/pdf/2505.05800"},{"title":"3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks","url":"https://arxiv.org/html/2505.05800"},{"title":"Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds","url":"https://arxiv.org/html/2602.00807v1"},{"title":"3D-CAVLA: Leveraging Depth and 3D Context to Generalize Vision–Language Action Models for Unseen Tasks","url":"https://arxiv.org/html/2505.05800v1"},{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/html/2508.09071v1"}]

Based on the search results, here's what I found about arXiv paper 2505.05800:

## 3D-CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models

3D-CAVLA is a novel finetuning framework that enhances task generalization of VLA policies by incorporating three key components: (i) chain-of-thought reasoning for structured decision-making, (ii) depth-aware perception for 3D spatial understanding, and (iii) task-oriented region-of-interest detection for focused manipulation.

**Authors:** Vineet Bhat, Yu-Hsiang Lan, Prashanth Krishnamurthy, Ramesh Karri, and Farshad Khorrami

**Key Results:** 
- 3D-CAVLA achieves an average success rate of 98.1% across diverse in-domain task suites in the LIBERO simulation environment
- On unseen tasks, 3D-CAVLA delivers an absolute improvement of 8.8% in success rate, underscoring the benefits of 3D scene awareness for robust generalization
- The approach is validated on real-world tabletop experiments demonstrating that the proposed model translates effectively from simulation to physical robots

**Framework Details:** 3D-CAVLA is a finetuning paradigm and can be applied after pre-training the vision-language encoders of any standard VLA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "e729adec-4305-4ce0-966a-025c88c2a038",
  "tool_use_result": {
    "query": "arXiv 2505.05800 3D-CAVLA leveraging depth 3D context generalize VLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BapbEeL1HHemJsspzfFLst",
        "content": [
          {
            "title": "[2505.05800] 3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks",
            "url": "https://arxiv.org/abs/2505.05800"
          },
          {
            "title": "3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks",
            "url": "https://arxiv.org/pdf/2505.05800"
          },
          {
            "title": "3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks",
            "url": "https://arxiv.org/html/2505.05800"
          },
          {
            "title": "Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
            "url": "https://arxiv.org/html/2602.00807v1"
          },
          {
            "title": "3D-CAVLA: Leveraging Depth and 3D Context to Generalize Vision–Language Action Models for Unseen Tasks",
            "url": "https://arxiv.org/html/2505.05800v1"
          },
          {
            "title": "GeoVLA: Empowering 3D Representations in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.09071v1"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2505.05800:\n\n## 3D-CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models\n\n3D-CAVLA is a novel finetuning framework that enhances task generalization of VLA policies by incorporating three key components: (i) chain-of-thought reasoning for structured decision-making, (ii) depth-aware perception for 3D spatial understanding, and (iii) task-oriented region-of-interest detection for focused manipulation.\n\n**Authors:** Vineet Bhat, Yu-Hsiang Lan, Prashanth Krishnamurthy, Ramesh Karri, and Farshad Khorrami\n\n**Key Results:** \n- 3D-CAVLA achieves an average success rate of 98.1% across diverse in-domain task suites in the LIBERO simulation environment\n- On unseen tasks, 3D-CAVLA delivers an absolute improvement of 8.8% in success rate, underscoring the benefits of 3D scene awareness for robust generalization\n- The approach is validated on real-world tabletop experiments demonstrating that the proposed model translates effectively from simulation to physical robots\n\n**Framework Details:** 3D-CAVLA is a finetuning paradigm and can be applied after pre-training the vision-language encoders of any standard VLA."
    ],
    "durationSeconds": 6.985979633000003
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T20:04:19.880Z_

<details><summary>↩ Tool result · `toolu_015tPR8ZMwCaevJDXhUC4FE4`</summary>

```text
Web search results for query: "arXiv 2603.13788 ST-VLA 4D spatiotemporal understanding robot manipulation"

Links: [{"title":"ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation","url":"https://arxiv.org/pdf/2603.13788"},{"title":"ST-𝜋: Structured SpatioTemporal VLA for Robotic Manipulation","url":"https://arxiv.org/html/2604.17880v1"},{"title":"VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation","url":"https://arxiv.org/html/2511.17199"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"[2511.17199] VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation","url":"https://arxiv.org/abs/2511.17199"}]

Based on the search results, here's what I found about arXiv 2603.13788:

**ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation** is authored by You Wu, Zixuan Chen, and others.

**Key contributions:**

ST-VLA is a hierarchical Vision-Language-Action (VLA) framework that uses a unified 3D-4D representation to bridge perception and action, converting 2D guidance into 3D trajectories and generating smooth spatial masks that capture 4D spatiotemporal context.

The researchers introduced ST-Human, a large-scale human manipulation dataset with 14 tasks and 300k episodes, and used it to train ST-VLM, a spatiotemporal vision-language model that generates spatially grounded and temporally coherent 3D representations.

**Performance:**

Experiments on RLBench and real-world manipulation tasks show that ST-VLA significantly outperforms state-of-the-art baselines, improving zero-shot success rates by 44.6% and 30.3%.

The paper addresses limitations of existing hierarchical VLA frameworks that typically use 2D representations and lack depth awareness and temporal consistency in complex 3D scenes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "242202d3-633d-417e-a9a9-8802d23e999a",
  "tool_use_result": {
    "query": "arXiv 2603.13788 ST-VLA 4D spatiotemporal understanding robot manipulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_011uqukjrSUn3zH9AtRiyuY1",
        "content": [
          {
            "title": "ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation",
            "url": "https://arxiv.org/pdf/2603.13788"
          },
          {
            "title": "ST-𝜋: Structured SpatioTemporal VLA for Robotic Manipulation",
            "url": "https://arxiv.org/html/2604.17880v1"
          },
          {
            "title": "VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.17199"
          },
          {
            "title": "Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2508.13073v1"
          },
          {
            "title": "[2511.17199] VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.17199"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv 2603.13788:\n\n**ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation** is authored by You Wu, Zixuan Chen, and others.\n\n**Key contributions:**\n\nST-VLA is a hierarchical Vision-Language-Action (VLA) framework that uses a unified 3D-4D representation to bridge perception and action, converting 2D guidance into 3D trajectories and generating smooth spatial masks that capture 4D spatiotemporal context.\n\nThe researchers introduced ST-Human, a large-scale human manipulation dataset with 14 tasks and 300k episodes, and used it to train ST-VLM, a spatiotemporal vision-language model that generates spatially grounded and temporally coherent 3D representations.\n\n**Performance:**\n\nExperiments on RLBench and real-world manipulation tasks show that ST-VLA significantly outperforms state-of-the-art baselines, improving zero-shot success rates by 44.6% and 30.3%.\n\nThe paper addresses limitations of existing hierarchical VLA frameworks that typically use 2D representations and lack depth awareness and temporal consistency in complex 3D scenes."
    ],
    "durationSeconds": 6.1062057420000055
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T20:04:22.216Z_

<details><summary>↩ Tool result · `toolu_01N9YqjWqUA1vEyYvvUpo6yi`</summary>

```text
Web search results for query: "arXiv 2604.21241 CorridorVLA explicit spatial constraints sparse anchors"

Links: [{"title":"[2604.21241] CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors","url":"https://arxiv.org/abs/2604.21241"},{"title":"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors","url":"https://arxiv.org/html/2604.21241"},{"title":"SparseOccVLA: Bridging Occupancy and Vision-Language Models via Sparse Queries for Unified 4D Scene Understanding and Planning","url":"https://arxiv.org/pdf/2601.06474"},{"title":"Sparse Laneformer","url":"https://arxiv.org/pdf/2404.07821"},{"title":"PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention","url":"https://arxiv.org/pdf/2512.03724"}]

I found the paper you're looking for! Here's what I found:

CorridorVLA predicts sparse spatial anchors as incremental physical changes (e.g., Δ-positions) and uses them to impose an explicit tolerance region in the training objective for action generation.

Vision-Language-Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. The anchors define a corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside it receive corrective gradients, while minor deviations from contacts and execution noise are permitted.

On the LIBERO-Plus benchmark, CorridorVLA yields consistent gains across both SmolVLA and GR00T, improving success rate by 3.4%-12.4% over the corresponding baselines; notably, the GR00T-Corr variant reaches a success rate of 83.21%.

The paper was submitted on April 23, 2026, and is authored by Dachong Li, Zhuangzhuang Chen, Jin Zhang, and Jianqiang Li from Shenzhen University and the National Engineering Laboratory for Big Data System Computing Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "a557b90d-21e8-4ec1-839b-50e9c16ed881",
  "tool_use_result": {
    "query": "arXiv 2604.21241 CorridorVLA explicit spatial constraints sparse anchors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QKyYPqPimeBfGp1xLuyPs7",
        "content": [
          {
            "title": "[2604.21241] CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors",
            "url": "https://arxiv.org/abs/2604.21241"
          },
          {
            "title": "CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors",
            "url": "https://arxiv.org/html/2604.21241"
          },
          {
            "title": "SparseOccVLA: Bridging Occupancy and Vision-Language Models via Sparse Queries for Unified 4D Scene Understanding and Planning",
            "url": "https://arxiv.org/pdf/2601.06474"
          },
          {
            "title": "Sparse Laneformer",
            "url": "https://arxiv.org/pdf/2404.07821"
          },
          {
            "title": "PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention",
            "url": "https://arxiv.org/pdf/2512.03724"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\nCorridorVLA predicts sparse spatial anchors as incremental physical changes (e.g., Δ-positions) and uses them to impose an explicit tolerance region in the training objective for action generation.\n\nVision-Language-Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. The anchors define a corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside it receive corrective gradients, while minor deviations from contacts and execution noise are permitted.\n\nOn the LIBERO-Plus benchmark, CorridorVLA yields consistent gains across both SmolVLA and GR00T, improving success rate by 3.4%-12.4% over the corresponding baselines; notably, the GR00T-Corr variant reaches a success rate of 83.21%.\n\nThe paper was submitted on April 23, 2026, and is authored by Dachong Li, Zhuangzhuang Chen, Jin Zhang, and Jianqiang Li from Shenzhen University and the National Engineering Laboratory for Big Data System Computing Technology."
    ],
    "durationSeconds": 7.041868499999997
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T20:04:24.377Z_

<details><summary>↩ Tool result · `toolu_01QZh1H1KyajMreNUyAvK8GV`</summary>

```text
Web search results for query: "arXiv 2503.07511 PointVLA injecting 3D point cloud features"

Links: [{"title":"[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.07511"},{"title":"[2503.07511v1] PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.07511v1"},{"title":"PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/html/2503.07511v1"},{"title":"PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/pdf/2503.07511"},{"title":"Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds","url":"https://arxiv.org/pdf/2602.00807"},{"title":"Cross-attention guided discriminative feature selection for robust point cloud domain generalization","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12349007/"},{"title":"ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation","url":"https://arxiv.org/html/2505.22159v1"}]

Based on the search results, here's information about arXiv 2503.07511:

**Paper Title:** PointVLA: Injecting the 3D World into Vision-Language-Action Models

**Overview:**
Vision-Language-Action (VLA) models excel at robotic tasks by leveraging large-scale 2D vision-language pretraining, but their reliance on RGB images limits spatial reasoning critical for real-world interaction. PointVLA is a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining, and freezes the vanilla action expert while injecting 3D features via a lightweight modular block.

**Technical Approach:**
To identify the most effective way of integrating point cloud representations, the authors conduct a skip-block analysis to pinpoint less useful blocks in the vanilla action expert, ensuring that 3D features are injected only into these blocks--minimizing disruption to pre-trained representations.

**Key Capabilities:**
PointVLA enables several key advantages: few-shot multi-tasking where it successfully performs four different tasks using only 20 demonstrations each, real-vs-photo discrimination to distinguish real objects from their images, and height adaptability for robots to adapt to objects at varying table heights unseen in training data.

The paper was submitted on March 10, 2025, and includes extensive experiments demonstrating improvements over state-of-the-art 2D imitation learning methods in both simulated and real-world robotic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "0bd44529-fefe-4208-b2bb-5b521bcca63f",
  "tool_use_result": {
    "query": "arXiv 2503.07511 PointVLA injecting 3D point cloud features",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TcdeGLR9r3X9CreCPCGJMH",
        "content": [
          {
            "title": "[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.07511"
          },
          {
            "title": "[2503.07511v1] PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.07511v1"
          },
          {
            "title": "PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2503.07511v1"
          },
          {
            "title": "PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2503.07511"
          },
          {
            "title": "Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
            "url": "https://arxiv.org/pdf/2602.00807"
          },
          {
            "title": "Cross-attention guided discriminative feature selection for robust point cloud domain generalization",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12349007/"
          },
          {
            "title": "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation",
            "url": "https://arxiv.org/html/2505.22159v1"
          }
        ]
      },
      "Based on the search results, here's information about arXiv 2503.07511:\n\n**Paper Title:** PointVLA: Injecting the 3D World into Vision-Language-Action Models\n\n**Overview:**\nVision-Language-Action (VLA) models excel at robotic tasks by leveraging large-scale 2D vision-language pretraining, but their reliance on RGB images limits spatial reasoning critical for real-world interaction. PointVLA is a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining, and freezes the vanilla action expert while injecting 3D features via a lightweight modular block.\n\n**Technical Approach:**\nTo identify the most effective way of integrating point cloud representations, the authors conduct a skip-block analysis to pinpoint less useful blocks in the vanilla action expert, ensuring that 3D features are injected only into these blocks--minimizing disruption to pre-trained representations.\n\n**Key Capabilities:**\nPointVLA enables several key advantages: few-shot multi-tasking where it successfully performs four different tasks using only 20 demonstrations each, real-vs-photo discrimination to distinguish real objects from their images, and height adaptability for robots to adapt to objects at varying table heights unseen in training data.\n\nThe paper was submitted on March 10, 2025, and includes extensive experiments demonstrating improvements over state-of-the-art 2D imitation learning methods in both simulated and real-world robotic tasks."
    ],
    "durationSeconds": 7.712783714999998
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T20:04:26.156Z_

<details><summary>↩ Tool result · `toolu_01SNXo5S9GF14i4BUT7Hmah8`</summary>

```text
Web search results for query: "arXiv 2508.09071 GeoVLA point cloud integration"

Links: [{"title":"[2508.09071] GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.09071"},{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/html/2508.09071v2"},{"title":"Detection of Building Equipment from Mobile Laser Scanning Point Clouds Using Reflection Intensity Correction for Detailed BIM Generation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12656139/"},{"title":"PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/pdf/2503.07511"},{"title":"Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds","url":"https://arxiv.org/pdf/2602.00807"},{"title":"Robust Low-Overlap Point Cloud Registration via Displacement-Corrected Geometric Consistency for Enhanced 3D Sensing","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12300971/"},{"title":"Automatic labelling of urban point clouds using data fusion","url":"https://arxiv.org/pdf/2108.13757"}]

Based on the search results, here's what I found about arXiv paper 2508.09071:

## GeoVLA: Empowering 3D Representations in Vision-Language-Action Models

GeoVLA is a novel VLA framework that effectively integrates 3D information to advance robotic manipulation.

### Point Cloud Integration

The framework converts depth maps into point clouds and employs a customized point encoder, called Point Embedding Network, to generate 3D geometric embeddings independently. These embeddings are then concatenated and processed by a proposed spatial-aware action expert, called 3D-enhanced Action Expert, which combines information from different sensor modalities.

### Problem It Addresses

Current VLA models mainly rely on 2D visual inputs, neglecting the rich geometric information in the 3D physical world, which limits their spatial awareness and adaptability.

### Performance

GeoVLA achieves state-of-the-art results in the LIBERO and ManiSkill2 simulation benchmarks, and shows remarkable robustness in real-world tasks requiring height adaptability, scale awareness and viewpoint invariance.

You can access the full paper at https://arxiv.org/abs/2508.09071.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "c4f516d6-f42e-4ba4-a9a8-97b4b67574a9",
  "tool_use_result": {
    "query": "arXiv 2508.09071 GeoVLA point cloud integration",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SjkAPbzcTsz5gYdJbbT5dr",
        "content": [
          {
            "title": "[2508.09071] GeoVLA: Empowering 3D Representations in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2508.09071"
          },
          {
            "title": "GeoVLA: Empowering 3D Representations in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.09071v2"
          },
          {
            "title": "Detection of Building Equipment from Mobile Laser Scanning Point Clouds Using Reflection Intensity Correction for Detailed BIM Generation",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12656139/"
          },
          {
            "title": "PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2503.07511"
          },
          {
            "title": "Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
            "url": "https://arxiv.org/pdf/2602.00807"
          },
          {
            "title": "Robust Low-Overlap Point Cloud Registration via Displacement-Corrected Geometric Consistency for Enhanced 3D Sensing",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12300971/"
          },
          {
            "title": "Automatic labelling of urban point clouds using data fusion",
            "url": "https://arxiv.org/pdf/2108.13757"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2508.09071:\n\n## GeoVLA: Empowering 3D Representations in Vision-Language-Action Models\n\nGeoVLA is a novel VLA framework that effectively integrates 3D information to advance robotic manipulation.\n\n### Point Cloud Integration\n\nThe framework converts depth maps into point clouds and employs a customized point encoder, called Point Embedding Network, to generate 3D geometric embeddings independently. These embeddings are then concatenated and processed by a proposed spatial-aware action expert, called 3D-enhanced Action Expert, which combines information from different sensor modalities.\n\n### Problem It Addresses\n\nCurrent VLA models mainly rely on 2D visual inputs, neglecting the rich geometric information in the 3D physical world, which limits their spatial awareness and adaptability.\n\n### Performance\n\nGeoVLA achieves state-of-the-art results in the LIBERO and ManiSkill2 simulation benchmarks, and shows remarkable robustness in real-world tasks requiring height adaptability, scale awareness and viewpoint invariance.\n\nYou can access the full paper at https://arxiv.org/abs/2508.09071."
    ],
    "durationSeconds": 9.972722747
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Good, all verified so far. Let me search for the remaining papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "c9f1158b-902b-47a8-85e1-c099cb793ead",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 40_

Continuing with the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "acbe5359-309e-4dcb-8c4d-af7b10436968",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D1gK3EKKfKoPPB2smeG8KC`</summary>

```json
{
  "query": "arXiv 2602.00743 SA-VLA spatially-aware flow-matching reinforcement learning",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "2855f8ac-fefe-43a4-8b83-895324f32a85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JsTtN9Lash13pX7pv5r9WM`</summary>

```json
{
  "query": "arXiv 2603.05754 Safe-Night VLA thermal-perceptive safety-critical manipulation",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "a27eb427-22f3-469b-b251-fafa70bb62e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 43_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015E3RYvGTEagNg7J7fLADNL`</summary>

```json
{
  "query": "arXiv 2604.23775 VLA safety survey threats challenges evaluations mechanisms",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "17e1af85-deaf-4888-884a-a9fabdfdf5a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JwWZ6Y9kPr6XnUGg7hWGXA`</summary>

```json
{
  "query": "arXiv 2503.04929 neural configuration-space barriers manipulation planning",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "9c3d9053-7147-4e75-8de9-7f4c2431b35b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013fKnKmv4CpGn6vpsnz5cu5`</summary>

```json
{
  "query": "arXiv 2406.09246 OpenVLA open-source vision-language-action model",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "282bce28-c564-48fe-a1ed-403d4d0a7acf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NeGbL8WJE6WvqEGQs4HR8r`</summary>

```json
{
  "query": "arXiv 2506.01844 SmolVLA affordable efficient robotics 0.45B",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "8c601e2d-78e9-42fa-a8f1-dcf511075a0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRezc9GREVpejwLXD2oQpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 4408,
      "cache_read_input_tokens": 33960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4408
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

_source line 47 · 2026-05-20T20:04:38.305Z_

<details><summary>↩ Tool result · `toolu_01JsTtN9Lash13pX7pv5r9WM`</summary>

```text
Web search results for query: "arXiv 2603.05754 Safe-Night VLA thermal-perceptive safety-critical manipulation"

Links: [{"title":"Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation","url":"https://arxiv.org/pdf/2603.05754"},{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation","url":"https://arxiv.org/html/2603.12717v1"},{"title":"Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models","url":"https://arxiv.org/pdf/2602.01834"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"Sensor-Fused Nighttime System for Enhanced Pedestrian Detection in ADAS and Autonomous Vehicles","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11281306/"},{"title":"[2603.05111] SPIRIT: Perceptive Shared Autonomy for Robust Robotic Manipulation under Deep Learning Uncertainty","url":"https://arxiv.org/abs/2603.05111"}]

Based on the search results, I found the paper you're looking for:

**Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation** is authored by Dian Yu, Qingchuan Zhou, Bingkun Huang, Majid Khadiv, and Zewen Yang.

The paper addresses limitations in current Vision-Language-Action (VLA) models that rely primarily on RGB perception and lack explicit safety constraints, proposing Safe-Night VLA as a multimodal manipulation framework that enables robots to perceive thermal signals while enforcing rigorous safety constraints for thermal-aware manipulation in unstructured environments.

Specifically, Safe-Night VLA integrates long-wave infrared thermal perception into a pre-trained vision-language backbone for semantic reasoning grounded in thermodynamic properties, and incorporates a safety filter via control barrier functions to provide deterministic workspace constraint enforcement during policy execution.

The framework was validated through real-world experiments on a Franka manipulator with novel evaluation tasks including temperature-conditioned manipulation, subsurface target localization, and reflection disambiguation, demonstrating that Safe-Night VLA outperforms RGB-only baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "bbbddf6a-75e5-472d-88df-2296a3e0a95f",
  "tool_use_result": {
    "query": "arXiv 2603.05754 Safe-Night VLA thermal-perceptive safety-critical manipulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HnH568VL3FetmTmNJUcsdx",
        "content": [
          {
            "title": "Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation",
            "url": "https://arxiv.org/pdf/2603.05754"
          },
          {
            "title": "Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation",
            "url": "https://arxiv.org/html/2603.12717v1"
          },
          {
            "title": "Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models",
            "url": "https://arxiv.org/pdf/2602.01834"
          },
          {
            "title": "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer",
            "url": "https://arxiv.org/pdf/2512.11891"
          },
          {
            "title": "Sensor-Fused Nighttime System for Enhanced Pedestrian Detection in ADAS and Autonomous Vehicles",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11281306/"
          },
          {
            "title": "[2603.05111] SPIRIT: Perceptive Shared Autonomy for Robust Robotic Manipulation under Deep Learning Uncertainty",
            "url": "https://arxiv.org/abs/2603.05111"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation** is authored by Dian Yu, Qingchuan Zhou, Bingkun Huang, Majid Khadiv, and Zewen Yang.\n\nThe paper addresses limitations in current Vision-Language-Action (VLA) models that rely primarily on RGB perception and lack explicit safety constraints, proposing Safe-Night VLA as a multimodal manipulation framework that enables robots to perceive thermal signals while enforcing rigorous safety constraints for thermal-aware manipulation in unstructured environments.\n\nSpecifically, Safe-Night VLA integrates long-wave infrared thermal perception into a pre-trained vision-language backbone for semantic reasoning grounded in thermodynamic properties, and incorporates a safety filter via control barrier functions to provide deterministic workspace constraint enforcement during policy execution.\n\nThe framework was validated through real-world experiments on a Franka manipulator with novel evaluation tasks including temperature-conditioned manipulation, subsurface target localization, and reflection disambiguation, demonstrating that Safe-Night VLA outperforms RGB-only baselines."
    ],
    "durationSeconds": 7.003050091000012
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T20:04:38.987Z_

<details><summary>↩ Tool result · `toolu_015E3RYvGTEagNg7J7fLADNL`</summary>

```text
Web search results for query: "arXiv 2604.23775 VLA safety survey threats challenges evaluations mechanisms"

Links: [{"title":"[2604.23775] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/abs/2604.23775"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775"},{"title":"A Survey of Safety on Large Vision-Language Models: Attacks, Defenses   and Evaluations","url":"https://arxiv.org/pdf/2502.14881"},{"title":"HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models","url":"https://arxiv.org/html/2604.12447"},{"title":"A Survey on Vision-Language-Action Models for Autonomous Driving","url":"https://arxiv.org/html/2506.24044v1"},{"title":"Safety Case Patterns for VLA-based driving systems: Insights from SimLingo","url":"https://arxiv.org/pdf/2603.16013"}]

I found the paper you're looking for! Here's information about arXiv 2604.23775:

The paper is titled "Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms" and provides a unified and up-to-date overview of safety in Vision-Language-Action models.

**Key topics covered:**

The survey addresses safety challenges stemming from the embodied nature of VLA systems, including irreversible physical consequences, a multimodal attack surface across vision, language, and state, real-time latency constraints on defense, error propagation over long-horizon trajectories, and vulnerabilities in the data supply chain.

The field is organized along two parallel timing axes—attack timing (training-time vs. inference-time) and defense timing (training-time vs. inference-time)—linking each class of threat to the stage at which it can be mitigated.

**Research scope:**

The survey examines the literature through four lenses: Attacks, Defenses, Evaluation, and Deployment, surveying training-time threats such as data poisoning and backdoors, as well as inference-time attacks including adversarial patches, cross-modal perturbations, semantic jailbreaks, and freezing attacks, while reviewing training-time and runtime defenses, analyzing existing benchmarks and metrics, and discussing safety challenges across six deployment domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "5b43e47e-cefb-4db9-9f0c-57b83f7f50e2",
  "tool_use_result": {
    "query": "arXiv 2604.23775 VLA safety survey threats challenges evaluations mechanisms",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A12ctjfoTtyZLgZB8vFTNK",
        "content": [
          {
            "title": "[2604.23775] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms",
            "url": "https://arxiv.org/abs/2604.23775"
          },
          {
            "title": "Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms",
            "url": "https://arxiv.org/html/2604.23775"
          },
          {
            "title": "A Survey of Safety on Large Vision-Language Models: Attacks, Defenses   and Evaluations",
            "url": "https://arxiv.org/pdf/2502.14881"
          },
          {
            "title": "HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models",
            "url": "https://arxiv.org/html/2604.12447"
          },
          {
            "title": "A Survey on Vision-Language-Action Models for Autonomous Driving",
            "url": "https://arxiv.org/html/2506.24044v1"
          },
          {
            "title": "Safety Case Patterns for VLA-based driving systems: Insights from SimLingo",
            "url": "https://arxiv.org/pdf/2603.16013"
          }
        ]
      },
      "I found the paper you're looking for! Here's information about arXiv 2604.23775:\n\nThe paper is titled \"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms\" and provides a unified and up-to-date overview of safety in Vision-Language-Action models.\n\n**Key topics covered:**\n\nThe survey addresses safety challenges stemming from the embodied nature of VLA systems, including irreversible physical consequences, a multimodal attack surface across vision, language, and state, real-time latency constraints on defense, error propagation over long-horizon trajectories, and vulnerabilities in the data supply chain.\n\nThe field is organized along two parallel timing axes—attack timing (training-time vs. inference-time) and defense timing (training-time vs. inference-time)—linking each class of threat to the stage at which it can be mitigated.\n\n**Research scope:**\n\nThe survey examines the literature through four lenses: Attacks, Defenses, Evaluation, and Deployment, surveying training-time threats such as data poisoning and backdoors, as well as inference-time attacks including adversarial patches, cross-modal perturbations, semantic jailbreaks, and freezing attacks, while reviewing training-time and runtime defenses, analyzing existing benchmarks and metrics, and discussing safety challenges across six deployment domains."
    ],
    "durationSeconds": 6.670955424999993
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T20:04:39.693Z_

<details><summary>↩ Tool result · `toolu_013fKnKmv4CpGn6vpsnz5cu5`</summary>

```text
Web search results for query: "arXiv 2406.09246 OpenVLA open-source vision-language-action model"

Links: [{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"[2406.09246v3] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246v3"},{"title":"Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations","url":"https://arxiv.org/html/2509.18953v1"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"},{"title":"Dexbotic: Open-Source Vision-Language-Action Toolbox","url":"https://arxiv.org/html/2510.23511v1"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v1"},{"title":"Benchmarking Vision, Language, & Action Models on Robotic Learning Tasks","url":"https://arxiv.org/html/2411.05821v2"}]

I found information about arXiv paper 2406.09246 on OpenVLA. Here are the key findings:

## Overview

OpenVLA is a vision-language-action (VLA) model that can be fine-tuned to obtain robust, generalizable policies for visuomotor control.

## Key Characteristics

OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.

## Motivation and Purpose

Widespread adoption of VLAs for robotics has been challenging because existing VLAs are largely closed and inaccessible to the public, and prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks. The OpenVLA project was developed to address these limitations by providing an open-source alternative.

## Research Team

The paper was authored by Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, and 14 additional researchers, with the paper submitted on June 13, 2024, and last revised on September 5, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "095da3c4-79ec-42ef-8d78-73822d89748c",
  "tool_use_result": {
    "query": "arXiv 2406.09246 OpenVLA open-source vision-language-action model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UtGkdaUpE8bBeH19WpFUXP",
        "content": [
          {
            "title": "[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/abs/2406.09246"
          },
          {
            "title": "[2406.09246v3] OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/abs/2406.09246v3"
          },
          {
            "title": "Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations",
            "url": "https://arxiv.org/html/2509.18953v1"
          },
          {
            "title": "Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions",
            "url": "https://arxiv.org/html/2505.11214v1"
          },
          {
            "title": "Dexbotic: Open-Source Vision-Language-Action Toolbox",
            "url": "https://arxiv.org/html/2510.23511v1"
          },
          {
            "title": "VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.03309v1"
          },
          {
            "title": "VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models",
            "url": "https://arxiv.org/html/2604.03956v1"
          },
          {
            "title": "Benchmarking Vision, Language, & Action Models on Robotic Learning Tasks",
            "url": "https://arxiv.org/html/2411.05821v2"
          }
        ]
      },
      "I found information about arXiv paper 2406.09246 on OpenVLA. Here are the key findings:\n\n## Overview\n\nOpenVLA is a vision-language-action (VLA) model that can be fine-tuned to obtain robust, generalizable policies for visuomotor control.\n\n## Key Characteristics\n\nOpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.\n\n## Motivation and Purpose\n\nWidespread adoption of VLAs for robotics has been challenging because existing VLAs are largely closed and inaccessible to the public, and prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks. The OpenVLA project was developed to address these limitations by providing an open-source alternative.\n\n## Research Team\n\nThe paper was authored by Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, and 14 additional researchers, with the paper submitted on June 13, 2024, and last revised on September 5, 2024."
    ],
    "durationSeconds": 5.5203802319999955
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T20:04:40.207Z_

<details><summary>↩ Tool result · `toolu_01JwWZ6Y9kPr6XnUGg7hWGXA`</summary>

```text
Web search results for query: "arXiv 2503.04929 neural configuration-space barriers manipulation planning"

Links: [{"title":"[2503.04929] Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://arxiv.org/abs/2503.04929"},{"title":"Neural Configuration-Space Barriers for Manipulation Planning and   Control","url":"https://arxiv.org/pdf/2503.04929"},{"title":"Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://arxiv.org/html/2503.04929v1"},{"title":"Systems and Control Mar 2025","url":"https://www.arxiv.org/list/eess.SY/2025-03?skip=475&show=25"},{"title":"Computer Science Mar 2025","url":"http://arxiv.org/list/cs/2025-03?skip=2475&show=50"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=2350&show=25"},{"title":"Robotics Mar 2025","url":"https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"}]

I found the arXiv paper you're looking for. Here's what it's about:

The paper is titled "Neural Configuration-Space Barriers for Manipulation Planning and Control" by Kehan Long, Ki Myung Brian Lee, Nikola Raicevic, Niyas Attasseri, Melvin Leok, and Nikolay Atanasov.

The paper proposes a unified framework for motion planning and control for high-dimensional robot manipulators in cluttered, dynamic environments that formulates safety constraints as CDF (configuration-space distance function) barriers. The approach is inspired by recent advances in learning configuration-space distance functions as robot body representations, and a CDF barrier approximates the local free configuration space, substantially reducing the number of collision-checking operations during motion planning.

To handle uncertainties from learning a CDF barrier with a neural network and relying on online sensor observations, the authors develop a distributionally robust CDF barrier formulation for control that explicitly accounts for modeling errors and sensor noise without assuming a known underlying distribution.

You can access the full paper at: https://arxiv.org/abs/2503.04929


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "8e5c7172-6561-4daa-8f59-9b930d9d605d",
  "tool_use_result": {
    "query": "arXiv 2503.04929 neural configuration-space barriers manipulation planning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FptZ5RZuAxf17TjHMXfBmd",
        "content": [
          {
            "title": "[2503.04929] Neural Configuration-Space Barriers for Manipulation Planning and Control",
            "url": "https://arxiv.org/abs/2503.04929"
          },
          {
            "title": "Neural Configuration-Space Barriers for Manipulation Planning and   Control",
            "url": "https://arxiv.org/pdf/2503.04929"
          },
          {
            "title": "Neural Configuration-Space Barriers for Manipulation Planning and Control",
            "url": "https://arxiv.org/html/2503.04929v1"
          },
          {
            "title": "Systems and Control Mar 2025",
            "url": "https://www.arxiv.org/list/eess.SY/2025-03?skip=475&show=25"
          },
          {
            "title": "Computer Science Mar 2025",
            "url": "http://arxiv.org/list/cs/2025-03?skip=2475&show=50"
          },
          {
            "title": "Machine Learning Mar 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-03?skip=2350&show=25"
          },
          {
            "title": "Robotics Mar 2025",
            "url": "https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"
          }
        ]
      },
      "I found the arXiv paper you're looking for. Here's what it's about:\n\nThe paper is titled \"Neural Configuration-Space Barriers for Manipulation Planning and Control\" by Kehan Long, Ki Myung Brian Lee, Nikola Raicevic, Niyas Attasseri, Melvin Leok, and Nikolay Atanasov.\n\nThe paper proposes a unified framework for motion planning and control for high-dimensional robot manipulators in cluttered, dynamic environments that formulates safety constraints as CDF (configuration-space distance function) barriers. The approach is inspired by recent advances in learning configuration-space distance functions as robot body representations, and a CDF barrier approximates the local free configuration space, substantially reducing the number of collision-checking operations during motion planning.\n\nTo handle uncertainties from learning a CDF barrier with a neural network and relying on online sensor observations, the authors develop a distributionally robust CDF barrier formulation for control that explicitly accounts for modeling errors and sensor noise without assuming a known underlying distribution.\n\nYou can access the full paper at: https://arxiv.org/abs/2503.04929"
    ],
    "durationSeconds": 6.8383360200000025
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T20:04:40.774Z_

<details><summary>↩ Tool result · `toolu_01NeGbL8WJE6WvqEGQs4HR8r`</summary>

```text
Web search results for query: "arXiv 2506.01844 SmolVLA affordable efficient robotics 0.45B"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=1025&show=100"},{"title":"VLA-0: Building State-of-the-Art VLAs with Zero Modification","url":"https://arxiv.org/html/2510.13054v1"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10274v1"},{"title":"BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation","url":"https://arxiv.org/html/2506.07530v2"},{"title":"SimVLA: A Simple VLA Baseline for Robotic Manipulation","url":"https://arxiv.org/html/2602.18224v1"}]

Based on the search results, here's information about arXiv paper 2506.01844:

## SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.

### Key Features:

SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.

### Problem It Addresses:

Existing VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability.

### Performance:

Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.

### Design Approach:

The model introduces an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation.

### Evaluation:

SmolVLA is evaluated on a range of both simulated as well as real-world robotic benchmarks and releases all code, pretrained models, and training data.

The paper was submitted to arXiv on June 2, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "f09b7d08-cb1f-4428-8106-a12cd577bbff",
  "tool_use_result": {
    "query": "arXiv 2506.01844 SmolVLA affordable efficient robotics 0.45B",
    "results": [
      {
        "tool_use_id": "srvtoolu_014d8fkmpUhTEJznoCnacNee",
        "content": [
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://arxiv.org/abs/2506.01844"
          },
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "http://export.arxiv.org/abs/2506.01844"
          },
          {
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "Computer Science Jun 2025",
            "url": "https://arxiv.org/list/cs/2025-06?skip=1025&show=100"
          },
          {
            "title": "VLA-0: Building State-of-the-Art VLAs with Zero Modification",
            "url": "https://arxiv.org/html/2510.13054v1"
          },
          {
            "title": "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2510.10274v1"
          },
          {
            "title": "BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation",
            "url": "https://arxiv.org/html/2506.07530v2"
          },
          {
            "title": "SimVLA: A Simple VLA Baseline for Robotic Manipulation",
            "url": "https://arxiv.org/html/2602.18224v1"
          }
        ]
      },
      "Based on the search results, here's information about arXiv paper 2506.01844:\n\n## SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\n\nSmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.\n\n### Key Features:\n\nSmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.\n\n### Problem It Addresses:\n\nExisting VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability.\n\n### Performance:\n\nDespite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.\n\n### Design Approach:\n\nThe model introduces an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation.\n\n### Evaluation:\n\nSmolVLA is evaluated on a range of both simulated as well as real-world robotic benchmarks and releases all code, pretrained models, and training data.\n\nThe paper was submitted to arXiv on June 2, 2025."
    ],
    "durationSeconds": 5.629046424
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T20:04:46.437Z_

<details><summary>↩ Tool result · `toolu_01D1gK3EKKfKoPPB2smeG8KC`</summary>

```text
Web search results for query: "arXiv 2602.00743 SA-VLA spatially-aware flow-matching reinforcement learning"

Links: [{"title":"[2602.00743] SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning","url":"https://arxiv.org/abs/2602.00743"},{"title":"SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning","url":"https://arxiv.org/pdf/2602.00743"},{"title":"Reinforcement Learning for Flow-Matching Policies","url":"https://arxiv.org/pdf/2507.15073"},{"title":"Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.09976"},{"title":"[2602.01606] Boosting Maximum Entropy Reinforcement Learning via One-Step Flow Matching","url":"https://arxiv.org/abs/2602.01606"}]

Based on the search results, here's what I found about arXiv paper 2602.00743:

SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning addresses the issue that Vision-Language-Action (VLA) models exhibit strong generalization in robotic manipulation, yet reinforcement learning (RL) fine-tuning often degrades robustness under spatial distribution shifts.

For flow-matching VLA policies, this degradation is closely associated with the erosion of spatial inductive bias during RL adaptation, as sparse rewards and spatially agnostic exploration increasingly favor short-horizon visual cues.

To address this issue, SA-VLA is a spatially-aware RL adaptation framework that preserves spatial grounding during policy optimization by aligning representation learning, reward design, and exploration with task geometry, fusing implicit spatial representations with visual tokens, providing dense rewards that reflect geometric progress, and employing SCAN, a spatially-conditioned annealed exploration strategy tailored to flow-matching dynamics.

The paper was authored by Xu Pan, Zhenglin Wan, Xingrui Yu, Xianwei Zheng, Youkai Ke, Ming Sun, Rui Wang, Ziwei Wang, and Ivor Tsang. The paper was submitted on January 31, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "82108b19-472e-4ae0-b77a-0a63dc333e8d",
  "tool_use_result": {
    "query": "arXiv 2602.00743 SA-VLA spatially-aware flow-matching reinforcement learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PWQegvQZJNrVnorGJ3wZF7",
        "content": [
          {
            "title": "[2602.00743] SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.00743"
          },
          {
            "title": "SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.00743"
          },
          {
            "title": "Reinforcement Learning for Flow-Matching Policies",
            "url": "https://arxiv.org/pdf/2507.15073"
          },
          {
            "title": "Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.09976"
          },
          {
            "title": "[2602.01606] Boosting Maximum Entropy Reinforcement Learning via One-Step Flow Matching",
            "url": "https://arxiv.org/abs/2602.01606"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2602.00743:\n\nSA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning addresses the issue that Vision-Language-Action (VLA) models exhibit strong generalization in robotic manipulation, yet reinforcement learning (RL) fine-tuning often degrades robustness under spatial distribution shifts.\n\nFor flow-matching VLA policies, this degradation is closely associated with the erosion of spatial inductive bias during RL adaptation, as sparse rewards and spatially agnostic exploration increasingly favor short-horizon visual cues.\n\nTo address this issue, SA-VLA is a spatially-aware RL adaptation framework that preserves spatial grounding during policy optimization by aligning representation learning, reward design, and exploration with task geometry, fusing implicit spatial representations with visual tokens, providing dense rewards that reflect geometric progress, and employing SCAN, a spatially-conditioned annealed exploration strategy tailored to flow-matching dynamics.\n\nThe paper was authored by Xu Pan, Zhenglin Wan, Xingrui Yu, Xianwei Zheng, Youkai Ke, Ming Sun, Rui Wang, Ziwei Wang, and Ivor Tsang. The paper was submitted on January 31, 2026."
    ],
    "durationSeconds": 16.490903076000002
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Good, now let me search for the last paper - vla-eval.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "3f320373-97c9-47d8-bbf3-062bc02f95b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcE9QEVafQEdbRZTDJyJZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3332,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 38368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

_source line 54_

One more to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "11e3416f-049c-44b3-a51e-cbf0ae751ee8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcE9QEVafQEdbRZTDJyJZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3332,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 38368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

_source line 55_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014EuvJ2ywwBv4Jx1556D6yk`</summary>

```json
{
  "query": "arXiv 2603.13966 vla-eval unified evaluation harness vision-language-action",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "d1ae16c9-87c8-4901-b252-ae0193ccad17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcE9QEVafQEdbRZTDJyJZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3332,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 38368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

_source line 56 · 2026-05-20T20:04:56.065Z_

<details><summary>↩ Tool result · `toolu_014EuvJ2ywwBv4Jx1556D6yk`</summary>

```text
Web search results for query: "arXiv 2603.13966 vla-eval unified evaluation harness vision-language-action"

Links: [{"title":"[2603.13966] vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.13966"},{"title":"vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.13966"},{"title":"LADEV: A Language-Driven Testing and Evaluation Platform for   Vision-Language-Action Models in Robotic Manipulation","url":"https://arxiv.org/pdf/2410.05191"},{"title":"Unified Vision-Language-Action Model","url":"https://arxiv.org/html/2506.19850v1"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.09930"},{"title":"Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations","url":"https://arxiv.org/html/2509.18953v1"},{"title":"Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process","url":"https://arxiv.org/html/2511.01718v1"}]

Based on the search results, I found the paper you're looking for:

**vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models** (arXiv:2603.13966) is authored by Suhwan Choi, Yunsung Lee, Yubeen Park, Chris Dongjoo Kim, Ranjay Krishna, Dieter Fox, and Youngjae Yu.

The paper addresses a key problem in VLA research: Vision-Language-Action (VLA) models are increasingly evaluated across multiple simulation benchmarks, yet adding each benchmark to an evaluation pipeline requires resolving incompatible dependencies, matching underspecified evaluation protocols, and reverse-engineering undocumented preprocessing.

vla-eval is an open-source evaluation harness that eliminates this per-benchmark cost by decoupling model inference from benchmark execution through a WebSocket+msgpack protocol with Docker-based environment isolation. This unified approach aims to make comprehensive evaluation of VLA models more practical for research teams.

The paper was submitted on March 14, 2026, with a revised version released on April 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "e859abbc-a8aa-42c5-8a1b-fdf56b42957f",
  "tool_use_result": {
    "query": "arXiv 2603.13966 vla-eval unified evaluation harness vision-language-action",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EmxucCiqoUyt2KJtxeeXwS",
        "content": [
          {
            "title": "[2603.13966] vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.13966"
          },
          {
            "title": "vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.13966"
          },
          {
            "title": "LADEV: A Language-Driven Testing and Evaluation Platform for   Vision-Language-Action Models in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2410.05191"
          },
          {
            "title": "Unified Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2506.19850v1"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2506.09930"
          },
          {
            "title": "Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations",
            "url": "https://arxiv.org/html/2509.18953v1"
          },
          {
            "title": "Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process",
            "url": "https://arxiv.org/html/2511.01718v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models** (arXiv:2603.13966) is authored by Suhwan Choi, Yunsung Lee, Yubeen Park, Chris Dongjoo Kim, Ranjay Krishna, Dieter Fox, and Youngjae Yu.\n\nThe paper addresses a key problem in VLA research: Vision-Language-Action (VLA) models are increasingly evaluated across multiple simulation benchmarks, yet adding each benchmark to an evaluation pipeline requires resolving incompatible dependencies, matching underspecified evaluation protocols, and reverse-engineering undocumented preprocessing.\n\nvla-eval is an open-source evaluation harness that eliminates this per-benchmark cost by decoupling model inference from benchmark execution through a WebSocket+msgpack protocol with Docker-based environment isolation. This unified approach aims to make comprehensive evaluation of VLA models more practical for research teams.\n\nThe paper was submitted on March 14, 2026, with a revised version released on April 17, 2026."
    ],
    "durationSeconds": 5.660305447999999
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
All 19 papers verified. Now let me construct the entries and append them to the YAML file. I need to get author names from the search results:

1. wu2025spatialvla - Wu et al. (from ID)
2. qdepthvla2025 - Li et al. (Yixuan Li)
3. geoaware2025 - Abouzeid et al. (Ali Abouzeid)
4. augvla3d2026 - authors not clearly stated, let me use the common format... The search said "the authors" but didn't explicitly name them. 

For the remaining papers, I'll fill in the author names where I have them from the search results, and for the ones without clear attribution, I'll apply standard arXiv naming conventions based on what information is available. For the remaining papers without clear author attribution, I'm noticing the search results didn't capture specific names for StemVLA, GeoVLA, PointVLA, the VLA Safety Survey, SmolVLA, and AugVLA-3D, so I'll need to do another targeted search to fill in those gaps. I still need to track down the authors for a few more entries—vlasafetysurvey2026 and smolvla2025—so let me run another batch of searches to fill those in.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "ac3699fe-b1af-475b-80f8-f4c588a2b000",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 58_

All arXiv IDs verified. Let me get author names for the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "42639ee2-a0c6-401a-a821-1283742e44d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 59_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DqTnWwDWJrdFX2nvqdtJ5s`</summary>

```json
{
  "query": "arXiv 2602.10698 AugVLA-3D authors",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "b92ba419-22f0-4200-93da-6be80c5040be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011nu7qBNY5pHRfQNnVXVrDo`</summary>

```json
{
  "query": "arXiv 2602.23721 StemVLA authors",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "a6014085-63c8-442d-b374-c361cb70a943",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D8BRWjb9Uwbh5bAbEYFpRX`</summary>

```json
{
  "query": "arXiv 2508.09071 GeoVLA authors",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "7160a6a9-3dc3-4c21-9cab-41c501031f27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ZjM3USRRN8mWP5DddeQbF`</summary>

```json
{
  "query": "arXiv 2503.07511 PointVLA authors first",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "28132719-85db-4c9d-b2fa-3d9ea7a464c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X5GaD7pwPTrKQ7WTmSD3W7`</summary>

```json
{
  "query": "arXiv 2604.23775 VLA safety survey authors",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "20a2399d-11d5-496c-ba9c-b803607f2a2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dq4j8rfyAzk1EUMECDpJP3`</summary>

```json
{
  "query": "arXiv 2506.01844 SmolVLA authors first",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "39102ac5-5ebe-4d25-8f96-7d5d9b225fa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8i1yuKfGfNcxzTsNmTgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 40352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4098
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

_source line 65 · 2026-05-20T20:05:22.881Z_

<details><summary>↩ Tool result · `toolu_011nu7qBNY5pHRfQNnVXVrDo`</summary>

```text
Web search results for query: "arXiv 2602.23721 StemVLA authors"

Links: [{"title":"[2602.23721] StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation","url":"https://arxiv.org/abs/2602.23721"},{"title":"StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation","url":"https://arxiv.org/pdf/2602.23721"},{"title":"Identifying weak signals in inhomogeneous neuronal images for large-scale tracing of neurites","url":"https://www.biorxiv.org/content/10.1101/181867.full.pdf"},{"title":"VERITAS and multiwavelength observations of the Blazar B3 2247+381 in   response to an IceCube neutrino alert","url":"https://arxiv.org/pdf/2502.03853"},{"title":"Performance of LHAASO-WCDA and Observation of Crab Nebula as a Standard   Candle","url":"https://arxiv.org/pdf/2101.03508"}]

Based on the search results, the authors of arXiv paper 2602.23721 (StemVLA) are Jiasong Xiao, Yutao She, Kai Li, Yuyang Sha, Ziang Cheng, and Ziang Tong.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "b98406e4-85bd-496c-ba12-cec2e29afbc0",
  "tool_use_result": {
    "query": "arXiv 2602.23721 StemVLA authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SScwPkgQ6M88oSnwzH7xWP",
        "content": [
          {
            "title": "[2602.23721] StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation",
            "url": "https://arxiv.org/abs/2602.23721"
          },
          {
            "title": "StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation",
            "url": "https://arxiv.org/pdf/2602.23721"
          },
          {
            "title": "Identifying weak signals in inhomogeneous neuronal images for large-scale tracing of neurites",
            "url": "https://www.biorxiv.org/content/10.1101/181867.full.pdf"
          },
          {
            "title": "VERITAS and multiwavelength observations of the Blazar B3 2247+381 in   response to an IceCube neutrino alert",
            "url": "https://arxiv.org/pdf/2502.03853"
          },
          {
            "title": "Performance of LHAASO-WCDA and Observation of Crab Nebula as a Standard   Candle",
            "url": "https://arxiv.org/pdf/2101.03508"
          }
        ]
      },
      "Based on the search results, the authors of arXiv paper 2602.23721 (StemVLA) are Jiasong Xiao, Yutao She, Kai Li, Yuyang Sha, Ziang Cheng, and Ziang Tong."
    ],
    "durationSeconds": 3.808273031000004
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T20:05:23.587Z_

<details><summary>↩ Tool result · `toolu_012ZjM3USRRN8mWP5DddeQbF`</summary>

```text
Web search results for query: "arXiv 2503.07511 PointVLA authors first"

Links: [{"title":"[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.07511"},{"title":"[2503.07511v1] PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.07511v1"},{"title":"PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/pdf/2503.07511"},{"title":"PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/html/2503.07511.pdf"},{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/html/2508.09071v1"},{"title":"ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation","url":"https://arxiv.org/html/2505.22159v1"}]

The first author of the arXiv paper 2503.07511 "PointVLA: Injecting the 3D World into Vision-Language-Action Models" is Chengmeng Li. The full list of authors includes Chengmeng Li, Junjie Wen, Yan Peng, Yaxin Peng, Feifei Feng, and Yichen Zhu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "d2b531f8-719e-4612-8abd-73f3a8f08f46",
  "tool_use_result": {
    "query": "arXiv 2503.07511 PointVLA authors first",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GHnnjWH4zWSqxPDvmKYtbN",
        "content": [
          {
            "title": "[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.07511"
          },
          {
            "title": "[2503.07511v1] PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.07511v1"
          },
          {
            "title": "PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2503.07511"
          },
          {
            "title": "PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2503.07511.pdf"
          },
          {
            "title": "GeoVLA: Empowering 3D Representations in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.09071v1"
          },
          {
            "title": "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation",
            "url": "https://arxiv.org/html/2505.22159v1"
          }
        ]
      },
      "The first author of the arXiv paper 2503.07511 \"PointVLA: Injecting the 3D World into Vision-Language-Action Models\" is Chengmeng Li. The full list of authors includes Chengmeng Li, Junjie Wen, Yan Peng, Yaxin Peng, Feifei Feng, and Yichen Zhu."
    ],
    "durationSeconds": 3.0016834499999967
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-20T20:05:25.133Z_

<details><summary>↩ Tool result · `toolu_01DqTnWwDWJrdFX2nvqdtJ5s`</summary>

```text
Web search results for query: "arXiv 2602.10698 AugVLA-3D authors"

Links: [{"title":"[2602.10698] AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.10698"},{"title":"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2602.10698"},{"title":"Forecasting Alzheimer’s Disease Progression with Deep Multimodal Learning: Integration of 3D MRI and Tabular Clinical Records via a Large Vision-Language Model","url":"https://www.medrxiv.org/content/10.64898/2026.01.06.26343479.full.pdf"},{"title":"OCT-based Visual Field Estimation via Segmentation-free 3D CNNs Shows Lower Longitudinal Variability than Standard Automated Perimetry","url":"https://www.medrxiv.org/content/10.1101/2024.08.17.24312150.full.pdf"},{"title":"A Semi-Automated Method for 3D Reconstruction from Routine Ultrasound Videos: Visualization of Transient Gallbladder Lesions","url":"https://www.medrxiv.org/content/10.1101/2025.11.11.25340033.full.pdf"}]

The authors of arXiv paper 2602.10698 "AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models" are: Zhifeng Rao, Wenlong Chen, Lei Xie, Xia Hua, Dongfu Yin, Zhen Tian, and F. Richard Yu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "6175cb48-4cf3-4e3f-9d26-38e334ac0e4a",
  "tool_use_result": {
    "query": "arXiv 2602.10698 AugVLA-3D authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EqRj6aBxPGEo1UVF5fQYU4",
        "content": [
          {
            "title": "[2602.10698] AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2602.10698"
          },
          {
            "title": "AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2602.10698"
          },
          {
            "title": "Forecasting Alzheimer’s Disease Progression with Deep Multimodal Learning: Integration of 3D MRI and Tabular Clinical Records via a Large Vision-Language Model",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.06.26343479.full.pdf"
          },
          {
            "title": "OCT-based Visual Field Estimation via Segmentation-free 3D CNNs Shows Lower Longitudinal Variability than Standard Automated Perimetry",
            "url": "https://www.medrxiv.org/content/10.1101/2024.08.17.24312150.full.pdf"
          },
          {
            "title": "A Semi-Automated Method for 3D Reconstruction from Routine Ultrasound Videos: Visualization of Transient Gallbladder Lesions",
            "url": "https://www.medrxiv.org/content/10.1101/2025.11.11.25340033.full.pdf"
          }
        ]
      },
      "The authors of arXiv paper 2602.10698 \"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models\" are: Zhifeng Rao, Wenlong Chen, Lei Xie, Xia Hua, Dongfu Yin, Zhen Tian, and F. Richard Yu."
    ],
    "durationSeconds": 6.864344535999989
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T20:05:25.274Z_

<details><summary>↩ Tool result · `toolu_01X5GaD7pwPTrKQ7WTmSD3W7`</summary>

```text
Web search results for query: "arXiv 2604.23775 VLA safety survey authors"

Links: [{"title":"[2604.23775] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/abs/2604.23775"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775"},{"title":"A Survey on Vision-Language-Action Models for Autonomous Driving","url":"https://arxiv.org/html/2506.24044v1"},{"title":"[2506.24044] A Survey on Vision-Language-Action Models for Autonomous Driving","url":"https://arxiv.org/abs/2506.24044"},{"title":"[2604.12447] HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.12447"},{"title":"[2604.23001] Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/abs/2604.23001"}]

Based on the search results, the authors of arXiv paper 2604.23775 "Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms" are Qi Li (Project Lead), Bo Yin, Weiqi Huang, Ruhao Liu, Bojun Zou, Runpeng Yu, Jingwen Ye, Weihao Yu, and Xinchao Wang (Corresponding Author), with affiliations including National University of Singapore, Monash University, and Peking University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "08e09f08-0f09-42b7-b6cb-be92224c0d82",
  "tool_use_result": {
    "query": "arXiv 2604.23775 VLA safety survey authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_017Tk2SKofQcAHV1Jm7A6eHH",
        "content": [
          {
            "title": "[2604.23775] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms",
            "url": "https://arxiv.org/abs/2604.23775"
          },
          {
            "title": "Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms",
            "url": "https://arxiv.org/html/2604.23775"
          },
          {
            "title": "A Survey on Vision-Language-Action Models for Autonomous Driving",
            "url": "https://arxiv.org/html/2506.24044v1"
          },
          {
            "title": "[2506.24044] A Survey on Vision-Language-Action Models for Autonomous Driving",
            "url": "https://arxiv.org/abs/2506.24044"
          },
          {
            "title": "[2604.12447] HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.12447"
          },
          {
            "title": "[2604.23001] Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines",
            "url": "https://arxiv.org/abs/2604.23001"
          }
        ]
      },
      "Based on the search results, the authors of arXiv paper 2604.23775 \"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms\" are Qi Li (Project Lead), Bo Yin, Weiqi Huang, Ruhao Liu, Bojun Zou, Runpeng Yu, Jingwen Ye, Weihao Yu, and Xinchao Wang (Corresponding Author), with affiliations including National University of Singapore, Monash University, and Peking University."
    ],
    "durationSeconds": 4.248157775999993
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-20T20:05:25.570Z_

<details><summary>↩ Tool result · `toolu_01Dq4j8rfyAzk1EUMECDpJP3`</summary>

```text
Web search results for query: "arXiv 2506.01844 SmolVLA authors first"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"VLA-0: Building State-of-the-Art VLAs with Zero Modification","url":"https://arxiv.org/pdf/2510.13054"},{"title":"NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies","url":"https://arxiv.org/html/2510.25122v1"},{"title":"Lite VLA: Efficient Vision-Language-Action Control on CPU-Bound Edge Robots","url":"https://arxiv.org/html/2511.05642v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"}]

Based on the search results for arXiv 2506.01844, here are the authors of the SmolVLA paper:

The first authors are Mustafa Shukor, Dana Aubakirova, and Francesco Capuano (marked as the core team), followed by Pepijn Kooijmans, Steven Palma, Adil Zouitine, Michel Aractingi, Caroline Pascal, Martino Russi, Andres Marafioti, Simon Alibert, Matthieu Cord, Thomas Wolf, and Remi Cadene.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "e85c2307-9111-41a3-b85f-8f0bd7dd8289",
  "tool_use_result": {
    "query": "arXiv 2506.01844 SmolVLA authors first",
    "results": [
      {
        "tool_use_id": "srvtoolu_016b5q6ZgPtDUGMd6ANAmb7J",
        "content": [
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://arxiv.org/abs/2506.01844"
          },
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "http://export.arxiv.org/abs/2506.01844"
          },
          {
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "VLA-0: Building State-of-the-Art VLAs with Zero Modification",
            "url": "https://arxiv.org/pdf/2510.13054"
          },
          {
            "title": "NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies",
            "url": "https://arxiv.org/html/2510.25122v1"
          },
          {
            "title": "Lite VLA: Efficient Vision-Language-Action Control on CPU-Bound Edge Robots",
            "url": "https://arxiv.org/html/2511.05642v1"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "Leave No Observation Behind: Real-time Correction for VLA Action Chunks",
            "url": "https://arxiv.org/html/2509.23224v1"
          }
        ]
      },
      "Based on the search results for arXiv 2506.01844, here are the authors of the SmolVLA paper:\n\nThe first authors are Mustafa Shukor, Dana Aubakirova, and Francesco Capuano (marked as the core team), followed by Pepijn Kooijmans, Steven Palma, Adil Zouitine, Michel Aractingi, Caroline Pascal, Martino Russi, Andres Marafioti, Simon Alibert, Matthieu Cord, Thomas Wolf, and Remi Cadene."
    ],
    "durationSeconds": 4.235681414000006
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T20:05:25.769Z_

<details><summary>↩ Tool result · `toolu_01D8BRWjb9Uwbh5bAbEYFpRX`</summary>

```text
Web search results for query: "arXiv 2508.09071 GeoVLA authors"

Links: [{"title":"[2508.09071] GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.09071"},{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/html/2508.09071v1"},{"title":"MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2508.19236v1"},{"title":"Mitigating Source Structure in Geodetic VLBI on the Visibility Level","url":"https://arxiv.org/pdf/2501.04787"},{"title":"Broad band flux-density monitoring of radio sources with the Onsala twin   telescopes","url":"https://arxiv.org/pdf/2203.08590"},{"title":"Discovery of perturbation gene targets via free text metadata mining in Gene Expression Omnibus","url":"https://www.biorxiv.org/content/10.1101/150896.full.pdf"}]

The authors of arXiv paper 2508.09071 (GeoVLA) are Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, and Jiale Cao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "90c47c7f-7a2d-42a5-adcd-46c082bffcee",
  "tool_use_result": {
    "query": "arXiv 2508.09071 GeoVLA authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HjLfyU78UN2mnkuFAaoEQK",
        "content": [
          {
            "title": "[2508.09071] GeoVLA: Empowering 3D Representations in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2508.09071"
          },
          {
            "title": "GeoVLA: Empowering 3D Representations in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.09071v1"
          },
          {
            "title": "MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2508.19236v1"
          },
          {
            "title": "Mitigating Source Structure in Geodetic VLBI on the Visibility Level",
            "url": "https://arxiv.org/pdf/2501.04787"
          },
          {
            "title": "Broad band flux-density monitoring of radio sources with the Onsala twin   telescopes",
            "url": "https://arxiv.org/pdf/2203.08590"
          },
          {
            "title": "Discovery of perturbation gene targets via free text metadata mining in Gene Expression Omnibus",
            "url": "https://www.biorxiv.org/content/10.1101/150896.full.pdf"
          }
        ]
      },
      "The authors of arXiv paper 2508.09071 (GeoVLA) are Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, and Jiale Cao."
    ],
    "durationSeconds": 6.176934747000007
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the entries and construct the YAML to append to the file.

Author summary:
1. wu2025spatialvla - Wu et al.
2. qdepthvla2025 - Li et al.
3. geoaware2025 - Abouzeid et al.
4. augvla3d2026 - Rao et al.
5. evo02025 - Lin et al.
6. sgvla2026 - Tu et al.
7. stemvla2026 - Xiao et al.
8. 3dcavla2025 - Bhat et al.


9. stvla2026 - Wu et al.
10. corridorvla2026 - Li et al.
11. geovla2025 - Sun et al.
12. pointvla2025 - Li et al. (Chengmeng Li)
13. savla2026 - Pan et al.
14. safenightvla2026 - Yu et al.
15. vlasafetysurvey2026 - Li et al. (Qi Li)
16. neuralcsbf2025 - Long et al.
17. kim2024openvla - Kim et al.
18. smolvla2025 - Shukor et al.
19. vlaeval2026 - Choi et al.

Now I'm formatting the YAML entries to match the existing structure—each with id, title, authors, venue, year, arxiv, category, role, key_finding, and our_differentiation fields, maintaining consistent indentation and organizing them by category sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "d4636069-1ebb-40a4-bc1d-80cdf7e27f40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xkytNUYpuh3T2LNsmtVUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1553,
      "cache_creation_input_tokens": 2791,
      "cache_read_input_tokens": 44450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2791
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

_source line 72_

All arXiv IDs verified, all author names collected. Now I'll append the 19 new entries to the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "813b7342-e6ff-4b2f-a69e-6afb7f36f365",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xkytNUYpuh3T2LNsmtVUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1553,
      "cache_creation_input_tokens": 2791,
      "cache_read_input_tokens": 44450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2791
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

_source line 73_

<details open><summary>🔧 Tool call — Edit · `toolu_01JisGnpCa6EwDot7QfvVybe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/literature_map.yaml",
  "old_string": "  - id: \"ma2026vlanext\"\n    title: \"VLANeXt: Recipes for Building Strong VLA Models\"\n    authors: \"Ma et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.18532\"\n    category: \"infrastructure\"\n    role: \"系统性 VLA 设计空间探索，我们工作的正交互补\"\n    key_finding: \"12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制\"\n    our_differentiation: \"VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度\"",
  "new_string": "  - id: \"ma2026vlanext\"\n    title: \"VLANeXt: Recipes for Building Strong VLA Models\"\n    authors: \"Ma et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.18532\"\n    category: \"infrastructure\"\n    role: \"系统性 VLA 设计空间探索，我们工作的正交互补\"\n    key_finding: \"12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制\"\n    our_differentiation: \"VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度\"\n\n  # ============================================================\n  # CATEGORY: spatial-vla (additional — 3D/depth/occupancy for VLA)\n  # ============================================================\n\n  - id: \"wu2025spatialvla\"\n    title: \"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model\"\n    authors: \"Wu et al.\"\n    venue: \"RSS 2026\"\n    year: 2025\n    arxiv: \"2501.15830\"\n    category: \"spatial-vla\"\n    role: \"大规模空间 VLA 预训练代表作，Ego3D Position Encoding\"\n    key_finding: \"Ego3D Position Encoding + Adaptive Action Grids，1.1M episodes 预训练，零样本跨机器人泛化\"\n    our_differentiation: \"SpatialVLA 无任何安全评估；我们首次研究空间表征与碰撞安全的交互\"\n\n  - id: \"qdepthvla2025\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2510.14836\"\n    category: \"spatial-vla\"\n    role: \"VQ-VAE 量化深度辅助监督方案，factorial study 参考\"\n    key_finding: \"深度专家预测 VQ-VAE 量化深度 token，学习深度感知表征提升精细操作\"\n    our_differentiation: \"QDepth-VLA 不产生占据场，未评估碰撞安全；我们将占据辅助与安全机制联合优化\"\n\n  - id: \"geoaware2025\"\n    title: \"GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model\"\n    authors: \"Abouzeid et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.14117\"\n    category: \"spatial-vla\"\n    role: \"冻结几何视觉模型注入 3D 先验，视角泛化 +35pp\"\n    key_finding: \"冻结预训练几何模型作为特征提取器，LIBERO 未见视角成功率提升 35 个百分点\"\n    our_differentiation: \"GeoAware-VLA 关注视角鲁棒性而非安全；我们关注空间表征如何改善碰撞避免\"\n\n  - id: \"augvla3d2026\"\n    title: \"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models\"\n    authors: \"Rao et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.10698\"\n    category: \"spatial-vla\"\n    role: \"VGGT 驱动的 3D 特征增强，action assistant 约束\"\n    key_finding: \"VGGT 提取几何感知 3D 线索 + action assistant 模块约束深度特征与动作一致性\"\n    our_differentiation: \"AugVLA-3D 用 VGGT 增强任务性能；我们研究 VGGT 类 3D 特征能否同时改善安全指标\"\n\n  - id: \"evo02025\"\n    title: \"Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding\"\n    authors: \"Lin et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2507.00416\"\n    category: \"spatial-vla\"\n    role: \"VGGT 即插即用隐式 3D 模块，无额外传感器\"\n    key_finding: \"即插即用模块利用视觉几何基础模型隐式注入 3D 几何特征，无需深度传感器\"\n    our_differentiation: \"Evo-0 不评估安全；我们首次系统研究此类隐式 3D 特征对碰撞安全的影响\"\n\n  - id: \"sgvla2026\"\n    title: \"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation\"\n    authors: \"Tu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.22760\"\n    category: \"spatial-vla\"\n    role: \"深度线索 + 辅助解码器用于移动操作 13 维动作空间\"\n    key_finding: \"多视角 RGB+深度+时间历史，辅助解码器重建全局位置/关节/抓取可供性/分割掩码\"\n    our_differentiation: \"SG-VLA 面向移动操作泛化；我们聚焦空间表征对固定基座 manipulation 碰撞安全的影响\"\n\n  - id: \"stemvla2026\"\n    title: \"StemVLA: An Open-Source VLA with Future 3D Spatial Geometry Knowledge and 4D Historical Representation\"\n    authors: \"Xiao et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.23721\"\n    category: \"spatial-vla\"\n    role: \"未来 3D 几何预测 + VideoFormer 4D 时空表征\"\n    key_finding: \"预测未来 3D 空间几何 + 时序注意力聚合历史 4D 时空表征，增强长时决策\"\n    our_differentiation: \"StemVLA 无碰撞评估；我们研究此类时空表征是否为安全 VLA 提供可利用的空间信号\"\n\n  - id: \"3dcavla2025\"\n    title: \"3D-CAVLA: Leveraging Depth and 3D Context to Generalize VLA for Unseen Tasks\"\n    authors: \"Bhat et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2505.05800\"\n    category: \"spatial-vla\"\n    role: \"深度+3D 上下文+CoT 推理，LIBERO 98.1%\"\n    key_finding: \"链式推理+深度感知+任务目标 ROI 检测，LIBERO 98.1%，未见任务 +8.8%\"\n    our_differentiation: \"3D-CAVLA 无碰撞评估；我们首次将类似 3D 上下文与安全机制结合\"\n\n  - id: \"stvla2026\"\n    title: \"ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation\"\n    authors: \"Wu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.13788\"\n    category: \"spatial-vla\"\n    role: \"4D 时空 VLA，2D 引导转 3D 轨迹，零样本 +44.6%\"\n    key_finding: \"统一 3D-4D 表征，2D 引导转 3D 轨迹 + 时空掩码，RLBench 零样本 +44.6%\"\n    our_differentiation: \"ST-VLA 关注任务泛化；我们关注 4D 时空表征能否被安全机制利用来预见碰撞\"\n\n  - id: \"corridorvla2026\"\n    title: \"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.21241\"\n    category: \"spatial-vla\"\n    role: \"空间锚点定义 action corridors，模糊空间-安全边界但未评估碰撞\"\n    key_finding: \"稀疏空间锚点定义容差走廊约束 flow-matching action head，LIBERO-Plus +3.4-12.4%\"\n    our_differentiation: \"CorridorVLA 的空间约束面向轨迹质量而非碰撞避免；我们的占据 CBF 显式优化安全\"\n\n  - id: \"geovla2025\"\n    title: \"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models\"\n    authors: \"Sun et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.09071\"\n    category: \"spatial-vla\"\n    role: \"点云编码器 + 3D 增强动作专家\"\n    key_finding: \"深度转点云 + Point Embedding Network + 3D-enhanced Action Expert，LIBERO/ManiSkill2 SOTA\"\n    our_differentiation: \"GeoVLA 无碰撞评估；我们研究点云表征能否被占据 CBF 利用来改善安全\"\n\n  - id: \"pointvla2025\"\n    title: \"PointVLA: Injecting the 3D World into Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.07511\"\n    category: \"spatial-vla\"\n    role: \"轻量级 3D 点云特征注入，skip-block 分析定位注入层\"\n    key_finding: \"冻结原始动作专家，通过 skip-block 分析选择性注入 3D 特征，少样本多任务泛化\"\n    our_differentiation: \"PointVLA 关注数据效率和视角鲁棒性；我们研究 3D 注入是否同时改善碰撞安全\"\n\n  - id: \"savla2026\"\n    title: \"SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning\"\n    authors: \"Pan et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.00743\"\n    category: \"spatial-vla\"\n    role: \"空间表征+空间奖励+空间探索，最接近空间-安全连接\"\n    key_finding: \"隐式空间表征融合+几何进度密集奖励+空间条件退火探索，解决 RL 微调空间偏移\"\n    our_differentiation: \"SA-VLA 关注 RL 微调分布偏移鲁棒性而非碰撞安全；我们直接优化碰撞避免指标\"\n\n  # ============================================================\n  # CATEGORY: direct-competitor (additional — safety-VLA methods)\n  # ============================================================\n\n  - id: \"safenightvla2026\"\n    title: \"Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.05754\"\n    category: \"direct-competitor\"\n    role: \"热成像+CBF 安全约束，不同感知模态的安全 VLA\"\n    key_finding: \"长波红外热成像融合语义推理 + CBF 安全滤波器，温度条件操作/遮挡目标定位\"\n    our_differentiation: \"Safe-Night VLA 依赖热成像特殊模态；我们利用 RGB 空间表征进步实现安全，无需额外传感器\"\n\n  - id: \"vlasafetysurvey2026\"\n    title: \"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.23775\"\n    category: \"direct-competitor\"\n    role: \"VLA 安全综述，按攻击/防御时间线分类，不研究空间表征维度\"\n    key_finding: \"沿攻击时间轴和防御时间轴组织 VLA 安全文献，覆盖数据投毒/对抗补丁/语义越狱等\"\n    our_differentiation: \"该综述确认空间表征-安全交互维度尚未被研究，支撑我们的核心 gap 声明\"\n\n  # ============================================================\n  # CATEGORY: safety-mechanism (additional — barrier functions)\n  # ============================================================\n\n  - id: \"neuralcsbf2025\"\n    title: \"Neural Configuration-Space Barriers for Manipulation Planning and Control\"\n    authors: \"Long et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.04929\"\n    category: \"safety-mechanism\"\n    role: \"学习 CDF barrier for manipulation，分布鲁棒公式\"\n    key_finding: \"学习配置空间距离函数 (CDF) barrier，分布鲁棒公式处理建模误差和传感器噪声\"\n    our_differentiation: \"Neural CS-BF 在配置空间操作需显式机器人模型；OCC-CBF 在占据特征空间操作，端到端与 VLA 联合\"\n\n  # ============================================================\n  # CATEGORY: infrastructure (additional — base models / benchmarks)\n  # ============================================================\n\n  - id: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2406.09246\"\n    category: \"infrastructure\"\n    role: \"开源 VLA 基础架构，OpenVLA-OFT 的前身\"\n    key_finding: \"Llama 2 + DINOv2/SigLIP 视觉编码器，首个大规模开源 VLA，支持高效微调\"\n    our_differentiation: \"OpenVLA 是 VLA 生态基础设施；我们在其微调变体 OFT 上构建实验\"\n\n  - id: \"smolvla2025\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.01844\"\n    category: \"infrastructure\"\n    role: \"0.45B 轻量 VLA，单 GPU 训练，消费级部署\"\n    key_finding: \"0.45B 参数 + 异步推理栈，单 GPU 训练，性能比肩 10x 大模型\"\n    our_differentiation: \"SmolVLA 是轻量 VLA 基线；我们的方法可适配不同规模 VLA 架构\"\n\n  - id: \"vlaeval2026\"\n    title: \"vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models\"\n    authors: \"Choi et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.13966\"\n    category: \"infrastructure\"\n    role: \"统一 VLA 评估框架，WebSocket+Docker 隔离\"\n    key_finding: \"WebSocket+msgpack 协议解耦模型推理与 benchmark 执行，47x 吞吐提升\"\n    our_differentiation: \"vla-eval 是评估基础设施；我们的安全评估指标可集成到此类统一框架\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "848948b9-dfca-45f4-b11d-efdcb6959eee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xkytNUYpuh3T2LNsmtVUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1553,
      "cache_creation_input_tokens": 2791,
      "cache_read_input_tokens": 44450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2791
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

_source line 74 · 2026-05-20T20:06:54.849Z_

<details><summary>↩ Tool result · `toolu_01JisGnpCa6EwDot7QfvVybe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "1a0d011b-7603-47d7-b2ad-f6708e879c41",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/literature_map.yaml",
    "oldString": "  - id: \"ma2026vlanext\"\n    title: \"VLANeXt: Recipes for Building Strong VLA Models\"\n    authors: \"Ma et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.18532\"\n    category: \"infrastructure\"\n    role: \"系统性 VLA 设计空间探索，我们工作的正交互补\"\n    key_finding: \"12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制\"\n    our_differentiation: \"VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度\"",
    "newString": "  - id: \"ma2026vlanext\"\n    title: \"VLANeXt: Recipes for Building Strong VLA Models\"\n    authors: \"Ma et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.18532\"\n    category: \"infrastructure\"\n    role: \"系统性 VLA 设计空间探索，我们工作的正交互补\"\n    key_finding: \"12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制\"\n    our_differentiation: \"VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度\"\n\n  # ============================================================\n  # CATEGORY: spatial-vla (additional — 3D/depth/occupancy for VLA)\n  # ============================================================\n\n  - id: \"wu2025spatialvla\"\n    title: \"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model\"\n    authors: \"Wu et al.\"\n    venue: \"RSS 2026\"\n    year: 2025\n    arxiv: \"2501.15830\"\n    category: \"spatial-vla\"\n    role: \"大规模空间 VLA 预训练代表作，Ego3D Position Encoding\"\n    key_finding: \"Ego3D Position Encoding + Adaptive Action Grids，1.1M episodes 预训练，零样本跨机器人泛化\"\n    our_differentiation: \"SpatialVLA 无任何安全评估；我们首次研究空间表征与碰撞安全的交互\"\n\n  - id: \"qdepthvla2025\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2510.14836\"\n    category: \"spatial-vla\"\n    role: \"VQ-VAE 量化深度辅助监督方案，factorial study 参考\"\n    key_finding: \"深度专家预测 VQ-VAE 量化深度 token，学习深度感知表征提升精细操作\"\n    our_differentiation: \"QDepth-VLA 不产生占据场，未评估碰撞安全；我们将占据辅助与安全机制联合优化\"\n\n  - id: \"geoaware2025\"\n    title: \"GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model\"\n    authors: \"Abouzeid et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.14117\"\n    category: \"spatial-vla\"\n    role: \"冻结几何视觉模型注入 3D 先验，视角泛化 +35pp\"\n    key_finding: \"冻结预训练几何模型作为特征提取器，LIBERO 未见视角成功率提升 35 个百分点\"\n    our_differentiation: \"GeoAware-VLA 关注视角鲁棒性而非安全；我们关注空间表征如何改善碰撞避免\"\n\n  - id: \"augvla3d2026\"\n    title: \"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models\"\n    authors: \"Rao et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.10698\"\n    category: \"spatial-vla\"\n    role: \"VGGT 驱动的 3D 特征增强，action assistant 约束\"\n    key_finding: \"VGGT 提取几何感知 3D 线索 + action assistant 模块约束深度特征与动作一致性\"\n    our_differentiation: \"AugVLA-3D 用 VGGT 增强任务性能；我们研究 VGGT 类 3D 特征能否同时改善安全指标\"\n\n  - id: \"evo02025\"\n    title: \"Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding\"\n    authors: \"Lin et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2507.00416\"\n    category: \"spatial-vla\"\n    role: \"VGGT 即插即用隐式 3D 模块，无额外传感器\"\n    key_finding: \"即插即用模块利用视觉几何基础模型隐式注入 3D 几何特征，无需深度传感器\"\n    our_differentiation: \"Evo-0 不评估安全；我们首次系统研究此类隐式 3D 特征对碰撞安全的影响\"\n\n  - id: \"sgvla2026\"\n    title: \"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation\"\n    authors: \"Tu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.22760\"\n    category: \"spatial-vla\"\n    role: \"深度线索 + 辅助解码器用于移动操作 13 维动作空间\"\n    key_finding: \"多视角 RGB+深度+时间历史，辅助解码器重建全局位置/关节/抓取可供性/分割掩码\"\n    our_differentiation: \"SG-VLA 面向移动操作泛化；我们聚焦空间表征对固定基座 manipulation 碰撞安全的影响\"\n\n  - id: \"stemvla2026\"\n    title: \"StemVLA: An Open-Source VLA with Future 3D Spatial Geometry Knowledge and 4D Historical Representation\"\n    authors: \"Xiao et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.23721\"\n    category: \"spatial-vla\"\n    role: \"未来 3D 几何预测 + VideoFormer 4D 时空表征\"\n    key_finding: \"预测未来 3D 空间几何 + 时序注意力聚合历史 4D 时空表征，增强长时决策\"\n    our_differentiation: \"StemVLA 无碰撞评估；我们研究此类时空表征是否为安全 VLA 提供可利用的空间信号\"\n\n  - id: \"3dcavla2025\"\n    title: \"3D-CAVLA: Leveraging Depth and 3D Context to Generalize VLA for Unseen Tasks\"\n    authors: \"Bhat et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2505.05800\"\n    category: \"spatial-vla\"\n    role: \"深度+3D 上下文+CoT 推理，LIBERO 98.1%\"\n    key_finding: \"链式推理+深度感知+任务目标 ROI 检测，LIBERO 98.1%，未见任务 +8.8%\"\n    our_differentiation: \"3D-CAVLA 无碰撞评估；我们首次将类似 3D 上下文与安全机制结合\"\n\n  - id: \"stvla2026\"\n    title: \"ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation\"\n    authors: \"Wu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.13788\"\n    category: \"spatial-vla\"\n    role: \"4D 时空 VLA，2D 引导转 3D 轨迹，零样本 +44.6%\"\n    key_finding: \"统一 3D-4D 表征，2D 引导转 3D 轨迹 + 时空掩码，RLBench 零样本 +44.6%\"\n    our_differentiation: \"ST-VLA 关注任务泛化；我们关注 4D 时空表征能否被安全机制利用来预见碰撞\"\n\n  - id: \"corridorvla2026\"\n    title: \"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.21241\"\n    category: \"spatial-vla\"\n    role: \"空间锚点定义 action corridors，模糊空间-安全边界但未评估碰撞\"\n    key_finding: \"稀疏空间锚点定义容差走廊约束 flow-matching action head，LIBERO-Plus +3.4-12.4%\"\n    our_differentiation: \"CorridorVLA 的空间约束面向轨迹质量而非碰撞避免；我们的占据 CBF 显式优化安全\"\n\n  - id: \"geovla2025\"\n    title: \"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models\"\n    authors: \"Sun et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2508.09071\"\n    category: \"spatial-vla\"\n    role: \"点云编码器 + 3D 增强动作专家\"\n    key_finding: \"深度转点云 + Point Embedding Network + 3D-enhanced Action Expert，LIBERO/ManiSkill2 SOTA\"\n    our_differentiation: \"GeoVLA 无碰撞评估；我们研究点云表征能否被占据 CBF 利用来改善安全\"\n\n  - id: \"pointvla2025\"\n    title: \"PointVLA: Injecting the 3D World into Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.07511\"\n    category: \"spatial-vla\"\n    role: \"轻量级 3D 点云特征注入，skip-block 分析定位注入层\"\n    key_finding: \"冻结原始动作专家，通过 skip-block 分析选择性注入 3D 特征，少样本多任务泛化\"\n    our_differentiation: \"PointVLA 关注数据效率和视角鲁棒性；我们研究 3D 注入是否同时改善碰撞安全\"\n\n  - id: \"savla2026\"\n    title: \"SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning\"\n    authors: \"Pan et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.00743\"\n    category: \"spatial-vla\"\n    role: \"空间表征+空间奖励+空间探索，最接近空间-安全连接\"\n    key_finding: \"隐式空间表征融合+几何进度密集奖励+空间条件退火探索，解决 RL 微调空间偏移\"\n    our_differentiation: \"SA-VLA 关注 RL 微调分布偏移鲁棒性而非碰撞安全；我们直接优化碰撞避免指标\"\n\n  # ============================================================\n  # CATEGORY: direct-competitor (additional — safety-VLA methods)\n  # ============================================================\n\n  - id: \"safenightvla2026\"\n    title: \"Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.05754\"\n    category: \"direct-competitor\"\n    role: \"热成像+CBF 安全约束，不同感知模态的安全 VLA\"\n    key_finding: \"长波红外热成像融合语义推理 + CBF 安全滤波器，温度条件操作/遮挡目标定位\"\n    our_differentiation: \"Safe-Night VLA 依赖热成像特殊模态；我们利用 RGB 空间表征进步实现安全，无需额外传感器\"\n\n  - id: \"vlasafetysurvey2026\"\n    title: \"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms\"\n    authors: \"Li et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2604.23775\"\n    category: \"direct-competitor\"\n    role: \"VLA 安全综述，按攻击/防御时间线分类，不研究空间表征维度\"\n    key_finding: \"沿攻击时间轴和防御时间轴组织 VLA 安全文献，覆盖数据投毒/对抗补丁/语义越狱等\"\n    our_differentiation: \"该综述确认空间表征-安全交互维度尚未被研究，支撑我们的核心 gap 声明\"\n\n  # ============================================================\n  # CATEGORY: safety-mechanism (additional — barrier functions)\n  # ============================================================\n\n  - id: \"neuralcsbf2025\"\n    title: \"Neural Configuration-Space Barriers for Manipulation Planning and Control\"\n    authors: \"Long et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2503.04929\"\n    category: \"safety-mechanism\"\n    role: \"学习 CDF barrier for manipulation，分布鲁棒公式\"\n    key_finding: \"学习配置空间距离函数 (CDF) barrier，分布鲁棒公式处理建模误差和传感器噪声\"\n    our_differentiation: \"Neural CS-BF 在配置空间操作需显式机器人模型；OCC-CBF 在占据特征空间操作，端到端与 VLA 联合\"\n\n  # ============================================================\n  # CATEGORY: infrastructure (additional — base models / benchmarks)\n  # ============================================================\n\n  - id: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2406.09246\"\n    category: \"infrastructure\"\n    role: \"开源 VLA 基础架构，OpenVLA-OFT 的前身\"\n    key_finding: \"Llama 2 + DINOv2/SigLIP 视觉编码器，首个大规模开源 VLA，支持高效微调\"\n    our_differentiation: \"OpenVLA 是 VLA 生态基础设施；我们在其微调变体 OFT 上构建实验\"\n\n  - id: \"smolvla2025\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2506.01844\"\n    category: \"infrastructure\"\n    role: \"0.45B 轻量 VLA，单 GPU 训练，消费级部署\"\n    key_finding: \"0.45B 参数 + 异步推理栈，单 GPU 训练，性能比肩 10x 大模型\"\n    our_differentiation: \"SmolVLA 是轻量 VLA 基线；我们的方法可适配不同规模 VLA 架构\"\n\n  - id: \"vlaeval2026\"\n    title: \"vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models\"\n    authors: \"Choi et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.13966\"\n    category: \"infrastructure\"\n    role: \"统一 VLA 评估框架，WebSocket+Docker 隔离\"\n    key_finding: \"WebSocket+msgpack 协议解耦模型推理与 benchmark 执行，47x 吞吐提升\"\n    our_differentiation: \"vla-eval 是评估基础设施；我们的安全评估指标可集成到此类统一框架\"",
    "originalFile": "# Literature Map for OccSafe-VLA (AAAI 2027)\n# Generated: 2026-05-20\n# Paper: OccSafe-VLA: Occupancy-Conditioned Safety for VLA via Systematic Spatial-Safety Interaction Analysis\n#\n# Core gap: No work studies the interaction between spatial representations and safety\n# mechanisms in VLAs. 15+ spatial-VLA papers never evaluate collision metrics;\n# all safety-VLA methods ignore spatial representation advances.\n\npapers:\n\n  # ============================================================\n  # CATEGORY: direct-competitor (spatial-safety intersection)\n  # ============================================================\n\n  - id: \"liu2025occvla\"\n    title: \"OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision\"\n    authors: \"Liu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2509.05578\"\n    category: \"direct-competitor\"\n    role: \"最近概念：occupancy + VLA，但面向自动驾驶\"\n    key_finding: \"将 3D 占据预测作为 VLA 辅助任务，学习空间结构，推理时可跳过（零开销）。在 nuScenes 轨迹规划上达到 SOTA\"\n    our_differentiation: \"OccVLA 仅验证自动驾驶；我们将占据辅助迁移到 manipulation，需解决精度尺度（厘米级 vs 米级）和动作空间差异\"\n\n  - id: \"hu2025aegis\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.11891\"\n    category: \"direct-competitor\"\n    role: \"唯一发表的 manipulation safety-VLA，plug-in CBF 方案\"\n    key_finding: \"AEGIS plug-in 安全约束层用 CBF + 开放集检测 + 深度图，SafeLIBERO 上 CAR 提升 59.16%\"\n    our_differentiation: \"AEGIS 是 plug-in 后处理，不影响 VLA 内部空间理解；我们将占据感知内化到 VLA 架构，实现预见性避障而非事后修正\"\n\n  - id: \"zhan2025safevla\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhan et al.\"\n    venue: \"NeurIPS 2025 Spotlight\"\n    year: 2025\n    arxiv: \"2503.03480\"\n    category: \"direct-competitor\"\n    role: \"RL-based VLA 安全对齐，NeurIPS 2025 Spotlight\"\n    key_finding: \"用约束马尔可夫决策过程进行 VLA 安全对齐\"\n    our_differentiation: \"SafeVLA 用 RL 方法，不涉及几何/占据表征；我们是几何驱动的空间-安全交互方案\"\n\n  - id: \"chen2026cofreevla\"\n    title: \"CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.21712\"\n    category: \"direct-competitor\"\n    role: \"半内化风险估计器 + collision labels\"\n    key_finding: \"半内化风险估计器结合模型生成的碰撞标签实现无碰撞双臂操作\"\n    our_differentiation: \"CoFreeVLA 不使用占据表征，风险估计不利用空间结构；我们的 OCC-CBF 基于占据特征做语义碰撞推理\"\n\n  # ============================================================\n  # CATEGORY: spatial-vla (3D representation for VLA, no safety eval)\n  # ============================================================\n\n  - id: \"li2025spatialforcing\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv: \"2510.12276\"\n    category: \"spatial-vla\"\n    role: \"隐式 3D 对齐 SOTA，factorial study 的 general-purpose 3D 条件参考\"\n    key_finding: \"将 VLA 中间层视觉嵌入与冻结 3D 基础模型对齐，超越所有 2D/3D VLA 基线，训练加速 3.8x\"\n    our_differentiation: \"Spatial Forcing 不产生显式占据场，未评估碰撞安全；我们的 factorial study 将其作为 general-purpose 3D 条件之一\"\n\n  - id: \"an2025depthvla\"\n    title: \"DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning\"\n    authors: \"An et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2510.13375\"\n    category: \"spatial-vla\"\n    role: \"深度辅助监督，factorial study 的 general-purpose 3D 条件参考\"\n    key_finding: \"通过 mixture-of-transformers 添加深度 transformer，真实世界 78.5% 成功率\"\n    our_differentiation: \"DepthVLA 未评估碰撞指标；我们将其与 Spatial Forcing 合并为 factorial 中的 general-purpose 3D 条件\"\n\n  - id: \"chen2026gstvla\"\n    title: \"GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2603.09079\"\n    category: \"spatial-vla\"\n    role: \"最精致的结构化空间表征，LIBERO 96.4%，无安全评估\"\n    key_finding: \"128 个各向异性 3D 高斯原语 + DA-CoT 推理，LIBERO 96.4%\"\n    our_differentiation: \"GST-VLA 是 ICRA 2027 扩展版的候选条件（Gaussian 空间表征 vs 体素占据）；AAAI 版暂不含\"\n\n  # ============================================================\n  # CATEGORY: safety-mechanism (barrier functions / occupancy-based safety)\n  # ============================================================\n\n  - id: \"ji2024ogmcbf\"\n    title: \"OGM-CBF: Safe Robot Control using Occupancy Grid Map-based Control Barrier Function\"\n    authors: \"Ji et al.\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2405.10703\"\n    category: \"safety-mechanism\"\n    role: \"OCC-CBF 的古典机器人学前身：离散占据网格 + SDF → CBF\"\n    key_finding: \"从占据网格图构建 CBF，比原始距离更有效地处理任意障碍物形状\"\n    our_differentiation: \"OGM-CBF 用离散网格 + SDF；我们的 OCC-CBF 在 VLA 连续学习特征空间操作，支持语义碰撞推理\"\n\n  - id: \"kwon2026learningnudge\"\n    title: \"Learning to Nudge: A Scalable Barrier Function Framework for Safe Robot Interaction in Dense Clutter\"\n    authors: \"Kwon et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2601.02686\"\n    category: \"safety-mechanism\"\n    role: \"学习型可组合 barrier function，manipulation 密集场景\"\n    key_finding: \"Dense Contact Barrier Functions (DCBF) — 学习型、可组合、以物体为中心的 barrier function，线性扩展到任意物体集\"\n    our_differentiation: \"DCBF 以物体为中心需显式物体分解；OCC-CBF 基于体积占据特征，推理连续空间结构含遮挡区域\"\n\n  # ============================================================\n  # CATEGORY: infrastructure (base architecture / benchmarks / recipes)\n  # ============================================================\n\n  - id: \"kim2025openvlaoft\"\n    title: \"OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\"\n    authors: \"Kim et al.\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2502.19645\"\n    category: \"infrastructure\"\n    role: \"MVP 和 factorial study 的 base architecture\"\n    key_finding: \"优化微调配方，LIBERO 97.1%，26x 加速\"\n    our_differentiation: \"OpenVLA-OFT 是我们的受控基准架构，不是对比对象\"\n\n  - id: \"ma2026vlanext\"\n    title: \"VLANeXt: Recipes for Building Strong VLA Models\"\n    authors: \"Ma et al.\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.18532\"\n    category: \"infrastructure\"\n    role: \"系统性 VLA 设计空间探索，我们工作的正交互补\"\n    key_finding: \"12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制\"\n    our_differentiation: \"VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度\"\n",
    "structuredPatch": [
      {
        "oldStart": 144,
        "oldLines": 3,
        "newStart": 144,
        "newLines": 228,
        "lines": [
          "     role: \"系统性 VLA 设计空间探索，我们工作的正交互补\"",
          "     key_finding: \"12 个关键发现覆盖基础/感知/动作维度，但不研究 3D 空间表征和安全机制\"",
          "     our_differentiation: \"VLANeXt 给出任务性能配方；我们给出安全 VLA 设计配方。正交维度\"",
          "+",
          "+  # ============================================================",
          "+  # CATEGORY: spatial-vla (additional — 3D/depth/occupancy for VLA)",
          "+  # ============================================================",
          "+",
          "+  - id: \"wu2025spatialvla\"",
          "+    title: \"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model\"",
          "+    authors: \"Wu et al.\"",
          "+    venue: \"RSS 2026\"",
          "+    year: 2025",
          "+    arxiv: \"2501.15830\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"大规模空间 VLA 预训练代表作，Ego3D Position Encoding\"",
          "+    key_finding: \"Ego3D Position Encoding + Adaptive Action Grids，1.1M episodes 预训练，零样本跨机器人泛化\"",
          "+    our_differentiation: \"SpatialVLA 无任何安全评估；我们首次研究空间表征与碰撞安全的交互\"",
          "+",
          "+  - id: \"qdepthvla2025\"",
          "+    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"",
          "+    authors: \"Li et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2510.14836\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"VQ-VAE 量化深度辅助监督方案，factorial study 参考\"",
          "+    key_finding: \"深度专家预测 VQ-VAE 量化深度 token，学习深度感知表征提升精细操作\"",
          "+    our_differentiation: \"QDepth-VLA 不产生占据场，未评估碰撞安全；我们将占据辅助与安全机制联合优化\"",
          "+",
          "+  - id: \"geoaware2025\"",
          "+    title: \"GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model\"",
          "+    authors: \"Abouzeid et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2509.14117\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"冻结几何视觉模型注入 3D 先验，视角泛化 +35pp\"",
          "+    key_finding: \"冻结预训练几何模型作为特征提取器，LIBERO 未见视角成功率提升 35 个百分点\"",
          "+    our_differentiation: \"GeoAware-VLA 关注视角鲁棒性而非安全；我们关注空间表征如何改善碰撞避免\"",
          "+",
          "+  - id: \"augvla3d2026\"",
          "+    title: \"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models\"",
          "+    authors: \"Rao et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2602.10698\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"VGGT 驱动的 3D 特征增强，action assistant 约束\"",
          "+    key_finding: \"VGGT 提取几何感知 3D 线索 + action assistant 模块约束深度特征与动作一致性\"",
          "+    our_differentiation: \"AugVLA-3D 用 VGGT 增强任务性能；我们研究 VGGT 类 3D 特征能否同时改善安全指标\"",
          "+",
          "+  - id: \"evo02025\"",
          "+    title: \"Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding\"",
          "+    authors: \"Lin et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2507.00416\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"VGGT 即插即用隐式 3D 模块，无额外传感器\"",
          "+    key_finding: \"即插即用模块利用视觉几何基础模型隐式注入 3D 几何特征，无需深度传感器\"",
          "+    our_differentiation: \"Evo-0 不评估安全；我们首次系统研究此类隐式 3D 特征对碰撞安全的影响\"",
          "+",
          "+  - id: \"sgvla2026\"",
          "+    title: \"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation\"",
          "+    authors: \"Tu et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2603.22760\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"深度线索 + 辅助解码器用于移动操作 13 维动作空间\"",
          "+    key_finding: \"多视角 RGB+深度+时间历史，辅助解码器重建全局位置/关节/抓取可供性/分割掩码\"",
          "+    our_differentiation: \"SG-VLA 面向移动操作泛化；我们聚焦空间表征对固定基座 manipulation 碰撞安全的影响\"",
          "+",
          "+  - id: \"stemvla2026\"",
          "+    title: \"StemVLA: An Open-Source VLA with Future 3D Spatial Geometry Knowledge and 4D Historical Representation\"",
          "+    authors: \"Xiao et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2602.23721\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"未来 3D 几何预测 + VideoFormer 4D 时空表征\"",
          "+    key_finding: \"预测未来 3D 空间几何 + 时序注意力聚合历史 4D 时空表征，增强长时决策\"",
          "+    our_differentiation: \"StemVLA 无碰撞评估；我们研究此类时空表征是否为安全 VLA 提供可利用的空间信号\"",
          "+",
          "+  - id: \"3dcavla2025\"",
          "+    title: \"3D-CAVLA: Leveraging Depth and 3D Context to Generalize VLA for Unseen Tasks\"",
          "+    authors: \"Bhat et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2505.05800\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"深度+3D 上下文+CoT 推理，LIBERO 98.1%\"",
          "+    key_finding: \"链式推理+深度感知+任务目标 ROI 检测，LIBERO 98.1%，未见任务 +8.8%\"",
          "+    our_differentiation: \"3D-CAVLA 无碰撞评估；我们首次将类似 3D 上下文与安全机制结合\"",
          "+",
          "+  - id: \"stvla2026\"",
          "+    title: \"ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation\"",
          "+    authors: \"Wu et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2603.13788\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"4D 时空 VLA，2D 引导转 3D 轨迹，零样本 +44.6%\"",
          "+    key_finding: \"统一 3D-4D 表征，2D 引导转 3D 轨迹 + 时空掩码，RLBench 零样本 +44.6%\"",
          "+    our_differentiation: \"ST-VLA 关注任务泛化；我们关注 4D 时空表征能否被安全机制利用来预见碰撞\"",
          "+",
          "+  - id: \"corridorvla2026\"",
          "+    title: \"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors\"",
          "+    authors: \"Li et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2604.21241\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"空间锚点定义 action corridors，模糊空间-安全边界但未评估碰撞\"",
          "+    key_finding: \"稀疏空间锚点定义容差走廊约束 flow-matching action head，LIBERO-Plus +3.4-12.4%\"",
          "+    our_differentiation: \"CorridorVLA 的空间约束面向轨迹质量而非碰撞避免；我们的占据 CBF 显式优化安全\"",
          "+",
          "+  - id: \"geovla2025\"",
          "+    title: \"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models\"",
          "+    authors: \"Sun et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2508.09071\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"点云编码器 + 3D 增强动作专家\"",
          "+    key_finding: \"深度转点云 + Point Embedding Network + 3D-enhanced Action Expert，LIBERO/ManiSkill2 SOTA\"",
          "+    our_differentiation: \"GeoVLA 无碰撞评估；我们研究点云表征能否被占据 CBF 利用来改善安全\"",
          "+",
          "+  - id: \"pointvla2025\"",
          "+    title: \"PointVLA: Injecting the 3D World into Vision-Language-Action Models\"",
          "+    authors: \"Li et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2503.07511\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"轻量级 3D 点云特征注入，skip-block 分析定位注入层\"",
          "+    key_finding: \"冻结原始动作专家，通过 skip-block 分析选择性注入 3D 特征，少样本多任务泛化\"",
          "+    our_differentiation: \"PointVLA 关注数据效率和视角鲁棒性；我们研究 3D 注入是否同时改善碰撞安全\"",
          "+",
          "+  - id: \"savla2026\"",
          "+    title: \"SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning\"",
          "+    authors: \"Pan et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2602.00743\"",
          "+    category: \"spatial-vla\"",
          "+    role: \"空间表征+空间奖励+空间探索，最接近空间-安全连接\"",
          "+    key_finding: \"隐式空间表征融合+几何进度密集奖励+空间条件退火探索，解决 RL 微调空间偏移\"",
          "+    our_differentiation: \"SA-VLA 关注 RL 微调分布偏移鲁棒性而非碰撞安全；我们直接优化碰撞避免指标\"",
          "+",
          "+  # ============================================================",
          "+  # CATEGORY: direct-competitor (additional — safety-VLA methods)",
          "+  # ============================================================",
          "+",
          "+  - id: \"safenightvla2026\"",
          "+    title: \"Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation\"",
          "+    authors: \"Yu et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2603.05754\"",
          "+    category: \"direct-competitor\"",
          "+    role: \"热成像+CBF 安全约束，不同感知模态的安全 VLA\"",
          "+    key_finding: \"长波红外热成像融合语义推理 + CBF 安全滤波器，温度条件操作/遮挡目标定位\"",
          "+    our_differentiation: \"Safe-Night VLA 依赖热成像特殊模态；我们利用 RGB 空间表征进步实现安全，无需额外传感器\"",
          "+",
          "+  - id: \"vlasafetysurvey2026\"",
          "+    title: \"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms\"",
          "+    authors: \"Li et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2604.23775\"",
          "+    category: \"direct-competitor\"",
          "+    role: \"VLA 安全综述，按攻击/防御时间线分类，不研究空间表征维度\"",
          "+    key_finding: \"沿攻击时间轴和防御时间轴组织 VLA 安全文献，覆盖数据投毒/对抗补丁/语义越狱等\"",
          "+    our_differentiation: \"该综述确认空间表征-安全交互维度尚未被研究，支撑我们的核心 gap 声明\"",
          "+",
          "+  # ============================================================",
          "+  # CATEGORY: safety-mechanism (additional — barrier functions)",
          "+  # ============================================================",
          "+",
          "+  - id: \"neuralcsbf2025\"",
          "+    title: \"Neural Configuration-Space Barriers for Manipulation Planning and Control\"",
          "+    authors: \"Long et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2503.04929\"",
          "+    category: \"safety-mechanism\"",
          "+    role: \"学习 CDF barrier for manipulation，分布鲁棒公式\"",
          "+    key_finding: \"学习配置空间距离函数 (CDF) barrier，分布鲁棒公式处理建模误差和传感器噪声\"",
          "+    our_differentiation: \"Neural CS-BF 在配置空间操作需显式机器人模型；OCC-CBF 在占据特征空间操作，端到端与 VLA 联合\"",
          "+",
          "+  # ============================================================",
          "+  # CATEGORY: infrastructure (additional — base models / benchmarks)",
          "+  # ============================================================",
          "+",
          "+  - id: \"kim2024openvla\"",
          "+    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"",
          "+    authors: \"Kim et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2024",
          "+    arxiv: \"2406.09246\"",
          "+    category: \"infrastructure\"",
          "+    role: \"开源 VLA 基础架构，OpenVLA-OFT 的前身\"",
          "+    key_finding: \"Llama 2 + DINOv2/SigLIP 视觉编码器，首个大规模开源 VLA，支持高效微调\"",
          "+    our_differentiation: \"OpenVLA 是 VLA 生态基础设施；我们在其微调变体 OFT 上构建实验\"",
          "+",
          "+  - id: \"smolvla2025\"",
          "+    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"",
          "+    authors: \"Shukor et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2025",
          "+    arxiv: \"2506.01844\"",
          "+    category: \"infrastructure\"",
          "+    role: \"0.45B 轻量 VLA，单 GPU 训练，消费级部署\"",
          "+    key_finding: \"0.45B 参数 + 异步推理栈，单 GPU 训练，性能比肩 10x 大模型\"",
          "+    our_differentiation: \"SmolVLA 是轻量 VLA 基线；我们的方法可适配不同规模 VLA 架构\"",
          "+",
          "+  - id: \"vlaeval2026\"",
          "+    title: \"vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models\"",
          "+    authors: \"Choi et al.\"",
          "+    venue: \"arXiv preprint\"",
          "+    year: 2026",
          "+    arxiv: \"2603.13966\"",
          "+    category: \"infrastructure\"",
          "+    role: \"统一 VLA 评估框架，WebSocket+Docker 隔离\"",
          "+    key_finding: \"WebSocket+msgpack 协议解耦模型推理与 benchmark 执行，47x 吞吐提升\"",
          "+    our_differentiation: \"vla-eval 是评估基础设施；我们的安全评估指标可集成到此类统一框架\""
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

_source line 75_

Now let me validate the YAML syntax.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "0e8848d0-38a9-4019-84e5-56487e027d65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvjKDf4ritjFere8jtSX3i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7018,
      "cache_read_input_tokens": 47241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7018
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

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01FkWVkPDKUdUH1wx9jcQKJP`</summary>

```json
{
  "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/literature_map.yaml')); papers = data['papers']; print(f'Total papers: {len(papers)}'); ids = [p['id'] for p in papers]; print(f'Unique IDs: {len(set(ids))}'); cats = {}; [cats.update({p['category']: cats.get(p['category'], 0) + 1}) for p in papers]; print(f'By category: {cats}')\"",
  "description": "Validate YAML syntax and count papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "a5e599d8-eb22-463e-832b-d372cc7552fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvjKDf4ritjFere8jtSX3i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7018,
      "cache_read_input_tokens": 47241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7018
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

_source line 77 · 2026-05-20T20:06:59.281Z_

<details><summary>↩ Tool result · `toolu_01FkWVkPDKUdUH1wx9jcQKJP`</summary>

```text
Total papers: 30
Unique IDs: 30
By category: {'direct-competitor': 6, 'spatial-vla': 16, 'safety-mechanism': 3, 'infrastructure': 5}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "f24c2f58-366c-4356-8219-e6a20dbc0e9f",
  "tool_use_result": {
    "stdout": "Total papers: 30\nUnique IDs: 30\nBy category: {'direct-competitor': 6, 'spatial-vla': 16, 'safety-mechanism': 3, 'infrastructure': 5}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 78_

YAML 验证通过。

- 总计 30 篇论文（原 11 + 新增 19），无重复 ID
- 分布：direct-competitor 6、spatial-vla 16、safety-mechanism 3、infrastructure 5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "uuid": "4e5f2afd-2cdc-4965-bdbf-cf271ab66173",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKiLXN2L2odViDfKFe9Zsx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
      },
      "output_tokens": 3,
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

_source line 79_

YAML 验证通过。

- 总计 30 篇论文（原 11 + 新增 19），无重复 ID
- 分布：direct-competitor 6、spatial-vla 16、safety-mechanism 3、infrastructure 5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 217331,
  "duration_api_ms": 357573,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "bc4d085e-630c-4156-877d-b832edba0249",
  "total_cost_usd": 1.2571394999999999,
  "usage": {
    "input_tokens": 6299,
    "cache_creation_input_tokens": 42712,
    "cache_read_input_tokens": 354335,
    "output_tokens": 9909,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42712,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 68,
        "cache_read_input_tokens": 54259,
        "cache_creation_input_tokens": 294,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 294
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 6299,
      "outputTokens": 9909,
      "cacheReadInputTokens": 354335,
      "cacheCreationInputTokens": 42712,
      "webSearchRequests": 0,
      "costUSD": 0.7233375000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 238692,
      "outputTokens": 9022,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 25,
      "costUSD": 0.533802,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b3e13849-f6fe-406c-8a76-dda3aa9598f3"
}
```

</details>

---
