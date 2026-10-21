# paper related work collision sdf

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_paper_related_work_collision_sdf_20260525T074038.log`
- **Structured JSON:** [`bf030bddcf7c14b50df5.json`](../../sessions/bf/bf030bddcf7c14b50df5.json)

## Before a recorded user message

67 recorded events

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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
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
  "uuid": "abb344a6-caf9-4650-9444-b15fedaf0f05",
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
    "resetsAt": 1779711000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "02ec00dc-728f-4f8f-8d33-44a0dc741b19",
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to supplement the Related Work section of a paper with literature on two topics: collision-aware manipulation and SDF in robotics. Let me start by reading the existing files to understand what's already covered.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "b767892b-ba67-45d5-a83a-484e946a4887",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fyHXe71gH2rby1nFh7qZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11967,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11967
      },
      "output_tokens": 26,
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

_source line 5_

先读取现有文献和论文定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "1d31b7b5-0d1b-45e9-8013-e08c6a8be119",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fyHXe71gH2rby1nFh7qZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11967,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11967
      },
      "output_tokens": 26,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017sNT8hKYC4FErmecihzLgA`</summary>

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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "17f86321-83e6-492c-9955-a51ae8e0c05f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fyHXe71gH2rby1nFh7qZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11967,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11967
      },
      "output_tokens": 26,
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

_source line 7 · 2026-05-25T07:40:52.902Z_

<details><summary>↩ Tool result · `toolu_017sNT8hKYC4FErmecihzLgA`</summary>

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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "e76ba1cc-dbbe-4fda-a288-dc196b7ecfea",
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NBFEh77XDzuY1mvXib6CUJ`</summary>

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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "77e06e42-a134-4237-b768-b6cb91ee0930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDwTEq7NpXoDe3HRnK8HS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 23414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 508
      },
      "output_tokens": 48,
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

_source line 9 · 2026-05-25T07:40:56.406Z_

<details><summary>↩ Tool result · `toolu_01NBFEh77XDzuY1mvXib6CUJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-20\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\\n  # ===== 新增 P3: Benchmark =====\\n\\n  - title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv: \\\"2306.03310\\\"\\n    role: benchmark\\n    relevance: \\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\"\\n\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\n\\n  - title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\"\\n    venue: \\\"ICLR 2023\\\"\\n    arxiv: \\\"2210.02747\\\"\\n    role: method-component\\n    relevance: \\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\"\\n\", \"total_chars\": 7788, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "1f46d86d-c88d-4a61-80d1-99619ad1ab12",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\\\", \\\"content\\\": \\\"# ColliForce-VLA Literature Map\\\\n# Updated: 2026-05-20\\\\n\\\\npapers:\\\\n\\\\n  # ===== 已有论文 =====\\\\n\\\\n  - paper_id: \\\\\\\"2512.11891\\\\\\\"\\\\n    title: \\\\\\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\\\\\"\\\\n    authors: \\\\\\\"Hu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    one_line_summary: \\\\\\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.14836\\\\\\\"\\\\n    title: \\\\\\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: spatial-aware-vla\\\\n    one_line_summary: \\\\\\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.12276\\\\\\\"\\\\n    title: \\\\\\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: ICLR 2026\\\\n    role: method-component\\\\n    category: spatial-aware-vla\\\\n    one_line_summary: \\\\\\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.05973\\\\\\\"\\\\n    title: \\\\\\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Huang et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: CoRL 2023\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2410.24164\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al., Physical Intelligence\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    role: backbone\\\\n    category: vla-foundation\\\\n    one_line_summary: \\\\\\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"1901.05103\\\\\\\"\\\\n    title: \\\\\\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\\\\\"\\\\n    authors: \\\\\\\"Park et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: CVPR 2019\\\\n    role: method-component\\\\n    category: sdf-representation\\\\n    one_line_summary: \\\\\\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.00533\\\\\\\"\\\\n    title: \\\\\\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\\\\\"\\\\n\\\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\\\n\\\\n  - paper_id: \\\\\\\"2503.03480\\\\\\\"\\\\n    title: \\\\\\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: NeurIPS 2025 (Spotlight)\\\\n    arxiv: \\\\\\\"2503.03480\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\\\\\"\\\\n    relevance: \\\\\\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2407.00451\\\\\\\"\\\\n    title: \\\\\\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: ICRA 2025\\\\n    arxiv: \\\\\\\"2407.00451\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\\\\\"\\\\n    relevance: \\\\\\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2511.22773\\\\\\\"\\\\n    title: \\\\\\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2511.22773\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\\\\\"\\\\n    relevance: \\\\\\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.08233\\\\\\\"\\\\n    title: \\\\\\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\\\\\"\\\\n    authors: \\\\\\\"Spalter et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2409.08233\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\\\\\"\\\\n    relevance: \\\\\\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\\\\\"\\\\n\\\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\\\n\\\\n  - paper_id: \\\\\\\"2204.02296\\\\\\\"\\\\n    title: \\\\\\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\\\\\"\\\\n    authors: \\\\\\\"Ortiz et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: RSS 2022\\\\n    arxiv: \\\\\\\"2204.02296\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\\\\\"\\\\n    relevance: \\\\\\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2305.10534\\\\\\\"\\\\n    title: \\\\\\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\\\\\"\\\\n    authors: \\\\\\\"Vasilopoulos et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: IROS 2023\\\\n    arxiv: \\\\\\\"2305.10534\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\\\\\"\\\\n    relevance: \\\\\\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2102.07413\\\\\\\"\\\\n    title: \\\\\\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Zhi et al.\\\\\\\"\\\\n    year: 2021\\\\n    venue: IEEE T-RO\\\\n    arxiv: \\\\\\\"2102.07413\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\\\\\"\\\\n    relevance: \\\\\\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\\\\\"\\\\n\\\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\\\n\\\\n  - paper_id: \\\\\\\"2307.15818\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al., Google DeepMind\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2307.15818\\\\\\\"\\\\n    role: foundational\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\\\\\"\\\\n    relevance: \\\\\\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2406.09246\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2406.09246\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\\\\\"\\\\n    relevance: \\\\\\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2405.12213\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Octo Model Team\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2405.12213\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\\\\\"\\\\n    relevance: \\\\\\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\\\\\"\\\\n\\\\n  # ===== 新增 P3: Benchmark =====\\\\n\\\\n  - title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    arxiv: \\\\\\\"2306.03310\\\\\\\"\\\\n    role: benchmark\\\\n    relevance: \\\\\\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\\\\\"\\\\n\\\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\\\n\\\\n  - title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    arxiv: \\\\\\\"2210.02747\\\\\\\"\\\\n    role: method-component\\\\n    relevance: \\\\\\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 7788, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-20\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\\n  # ===== 新增 P3: Benchmark =====\\n\\n  - title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv: \\\"2306.03310\\\"\\n    role: benchmark\\n    relevance: \\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\"\\n\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\n\\n  - title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\"\\n    venue: \\\"ICLR 2023\\\"\\n    arxiv: \\\"2210.02747\\\"\\n    role: method-component\\n    relevance: \\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\"\\n\", \"total_chars\": 7788, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SurTeBEbddunw3vn4QDLWb`</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "paper_framing.md",
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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "a29a5d3f-7edc-42d4-b523-f0e1ed3a615b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDwTEq7NpXoDe3HRnK8HS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 23414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 508
      },
      "output_tokens": 48,
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

_source line 11 · 2026-05-25T07:40:56.448Z_

<details><summary>↩ Tool result · `toolu_01SurTeBEbddunw3vn4QDLWb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\\n\\n## Core Insight\\n\\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\\n\\n## Working Title\\n\\n\\\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\\\"\\n\\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \\\"all SDF methods\\\"，聚焦 metric contamination 这一更可防御的贡献\\n\\n## Core Claims\\n\\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\\\"Collision-free\\\" ≠ \\\"collision-avoiding\\\"。\\n\\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\\n\\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\\n\\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\\n\\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\\n\\n**限制**: 仅 2 个 model families, Pi0 的 \\\"高 CAR\\\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\\n\\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\\n\\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\\n\\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\\\"analysis paper with positive method contribution\\\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \\\"问题可解决\\\" 以验证 analysis 框架的价值。\\n\\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \\\"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\\\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\\n\\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\\n**如果失败**: 额外 negative evidence, 强化 structural insight\\n\\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \\\"sweet spot\\\" claim\\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n\\\"任何了解机器人运动学的人都知道肘部会碰\\\"\\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\\n\\n### R3: No positive result\\n\\\"告诉我什么不 work 但没告诉我什么 work\\\"\\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\\n\\n### R4: Action collapse is trivial\\n\\\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\\\"\\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\\n\\n## Figure Plan\\n\\n| ID | 内容 | 优先级 | 数据来源 |\\n|----|------|--------|---------|\\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\\n\\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\\n\\n## Narrative Focus (Reviewer Report #30)\\n\\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\\n\\n## Negative Results Narrative Strategy (D018 + 16 negatives)\\n\\n16 个阴性结果按叙事功能分为 3 层：\\n\\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\\n这些 negative 本身就是 paper 的 finding：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\\n\\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\\n提供边界信息，但非核心贡献：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\\n\\n### Tier C: 省略（技术失败 / 与结论无关）\\n不进入论文正文或 appendix：\\n\\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\\n- 被 kill 的实验（资源调度，无结论）\\n\\n### 叙事原则\\n1. Tier A 的 negative 不是\\\"失败\\\"，是 **evidence for structural claims** — 用 \\\"we demonstrate\\\" 而非 \\\"we failed to\\\"\\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\\n4. Tier C 完全不提\\n\\n## Contingency Plans (Post Step-10K Eval)\\n\\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\\n→ 纯 analysis paper, 聚焦 structural insight\\n\\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\\n→ 必须对比纯 LoRA baseline 才能归因\\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\\n\\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\\n\\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\\n|---------------|----------|----------|\\n| ~27% (≈baseline) | +30pp 全归 SDF | \\\"geometric supervision is effective\\\" — 最强 method claim |\\n| ~35% | +22pp | \\\"LoRA capacity tuning helps, SDF provides major additional benefit\\\" — 仍强 |\\n| ~45% | +12pp | \\\"LoRA is primary driver, SDF provides dose-dependent safety margin\\\" — 需 4-point lambda 曲线支撑 monotonic trend |\\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\\n\\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \\\"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\\\"。\\n\\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\\n→ 继续到 30K, 升级为 \\\"analysis paper with positive method contribution\\\"（非纯 method paper）\\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \\\"sweet spot\\\" claim\\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\\n\\n## Dependencies\\n\\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\\n- [x] Oracle 3 variants (Claim 3) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\\n\", \"total_chars\": 8058, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "79b0c449-4bba-4b83-8c18-56c901eeeacb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\\\", \\\"content\\\": \\\"# ColliForce-VLA Paper Framing\\\\n\\\\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\\\\n\\\\n## Core Insight\\\\n\\\\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \\\\\\\"安全\\\\\\\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\\\\n\\\\n## Working Title\\\\n\\\\n\\\\\\\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\\\\\\\"\\\\n\\\\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \\\\\\\"all SDF methods\\\\\\\"，聚焦 metric contamination 这一更可防御的贡献\\\\n\\\\n## Core Claims\\\\n\\\\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\\\\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\\\\\\\"Collision-free\\\\\\\" ≠ \\\\\\\"collision-avoiding\\\\\\\"。\\\\n\\\\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\\\\n\\\\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\\\\n\\\\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\\\\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\\\\n\\\\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\\\\n\\\\n**限制**: 仅 2 个 model families, Pi0 的 \\\\\\\"高 CAR\\\\\\\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\\\\n\\\\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\\\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\\\n\\\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\\\n\\\\n**限制**: \\\\\\\"EE-only 不够\\\\\\\" 是 expected result; 缺乏 full-body SDF 对照\\\\n\\\\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\\\\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\\\\n\\\\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\\\\n\\\\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\\\\\\\"analysis paper with positive method contribution\\\\\\\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \\\\\\\"问题可解决\\\\\\\" 以验证 analysis 框架的价值。\\\\n\\\\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \\\\\\\"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\\\\\\\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\\\\n\\\\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\\\\n**如果失败**: 额外 negative evidence, 强化 structural insight\\\\n\\\\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\\\\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\\\\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\\\\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \\\\\\\"sweet spot\\\\\\\" claim\\\\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1 (最致命): Generalizability\\\\n\\\\\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\\\\\"\\\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\\\\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\\\\n\\\\n### R2: Novelty of EE-only limitation\\\\n\\\\\\\"任何了解机器人运动学的人都知道肘部会碰\\\\\\\"\\\\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\\\\n\\\\n### R3: No positive result\\\\n\\\\\\\"告诉我什么不 work 但没告诉我什么 work\\\\\\\"\\\\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\\\\n\\\\n### R4: Action collapse is trivial\\\\n\\\\\\\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\\\\\\\"\\\\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\\\\n\\\\n## Figure Plan\\\\n\\\\n| ID | 内容 | 优先级 | 数据来源 |\\\\n|----|------|--------|---------|\\\\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\\\\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\\\\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\\\\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\\\\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\\\\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\\\\n\\\\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\\\\n\\\\n## Target Venue\\\\n\\\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\\\\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\\\\n\\\\n## Narrative Focus (Reviewer Report #30)\\\\n\\\\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\\\\n\\\\n## Negative Results Narrative Strategy (D018 + 16 negatives)\\\\n\\\\n16 个阴性结果按叙事功能分为 3 层：\\\\n\\\\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\\\\n这些 negative 本身就是 paper 的 finding：\\\\n\\\\n| 类别 | 实验 | 论文功能 |\\\\n|------|------|----------|\\\\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\\\\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\\\\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\\\\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\\\\n\\\\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\\\\n提供边界信息，但非核心贡献：\\\\n\\\\n| 类别 | 实验 | 论文功能 |\\\\n|------|------|----------|\\\\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\\\\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\\\\n\\\\n### Tier C: 省略（技术失败 / 与结论无关）\\\\n不进入论文正文或 appendix：\\\\n\\\\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\\\\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\\\\n- 被 kill 的实验（资源调度，无结论）\\\\n\\\\n### 叙事原则\\\\n1. Tier A 的 negative 不是\\\\\\\"失败\\\\\\\"，是 **evidence for structural claims** — 用 \\\\\\\"we demonstrate\\\\\\\" 而非 \\\\\\\"we failed to\\\\\\\"\\\\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\\\\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\\\\n4. Tier C 完全不提\\\\n\\\\n## Contingency Plans (Post Step-10K Eval)\\\\n\\\\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\\\\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\\\\n→ 纯 analysis paper, 聚焦 structural insight\\\\n\\\\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\\\\n→ 必须对比纯 LoRA baseline 才能归因\\\\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\\\\n\\\\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\\\\n\\\\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\\\\n|---------------|----------|----------|\\\\n| ~27% (≈baseline) | +30pp 全归 SDF | \\\\\\\"geometric supervision is effective\\\\\\\" — 最强 method claim |\\\\n| ~35% | +22pp | \\\\\\\"LoRA capacity tuning helps, SDF provides major additional benefit\\\\\\\" — 仍强 |\\\\n| ~45% | +12pp | \\\\\\\"LoRA is primary driver, SDF provides dose-dependent safety margin\\\\\\\" — 需 4-point lambda 曲线支撑 monotonic trend |\\\\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\\\\n\\\\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \\\\\\\"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\\\\\\\"。\\\\n\\\\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\\\\n→ 继续到 30K, 升级为 \\\\\\\"analysis paper with positive method contribution\\\\\\\"（非纯 method paper）\\\\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \\\\\\\"sweet spot\\\\\\\" claim\\\\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\\\\n\\\\n## Dependencies\\\\n\\\\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\\\\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\\\\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\\\\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\\\\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\\\\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\\\\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\\\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\\\\n- [x] Oracle 3 variants (Claim 3) — all < baseline\\\\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\\\\n\\\", \\\"total_chars\\\": 8058, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\\n\\n## Core Insight\\n\\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\\n\\n## Working Title\\n\\n\\\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\\\"\\n\\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \\\"all SDF methods\\\"，聚焦 metric contamination 这一更可防御的贡献\\n\\n## Core Claims\\n\\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\\\"Collision-free\\\" ≠ \\\"collision-avoiding\\\"。\\n\\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\\n\\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\\n\\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\\n\\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\\n\\n**限制**: 仅 2 个 model families, Pi0 的 \\\"高 CAR\\\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\\n\\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)\\n在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？\\n\\n**状态**: 3-seed × 2-lambda 训练中, 预计 5/24 18:00 出结果\\n\\n**Framing 策略 (Reviewer #37)**：即使最优结果也定位为 **\\\"analysis paper with positive method contribution\\\"**，而非纯 method paper。原因：analysis 贡献 scope-proof（适用所有 VLA），method 贡献 scope-limited（1-2 models, 2-4 tasks）。SDF aux loss 作为 secondary proof-of-concept，证明 \\\"问题可解决\\\" 以验证 analysis 框架的价值。\\n\\n**Claim 措辞上限** (按 Reviewer 预审升级，基于 10K +30pp 证据): \\\"Training-time SDF auxiliary loss yields substantial collision avoidance improvement (+Xpp displacement-filtered CAR, frozen_rate=0%) on Pi0.5, confirming that geometric supervision effectively addresses action-collapse-contaminated safety in capable VLAs — at a moderate task performance cost (TSR: 74.7%→Y%)\\\"（必须包含 TSR tradeoff；禁区: SOTA / consistently outperforms / general solution）\\n\\n**如果成功 (CAR ≥ 33%)**: 升级为 method contribution (secondary)\\n**如果失败**: 额外 negative evidence, 强化 structural insight\\n\\n**泛化扩展计划 (Reviewer #37, 提升接受率)**：\\n- 必须: spatial_bowl 第 2 task 训练（代码准备中）→ 接受率 40% → 55-65%\\n- 应该做: OpenVLA zero-shot eval 验证 fake safety 在第 3 model 上存在（仅 inference）\\n- 应该做: 4-point lambda 曲线 (0, 0.005, 0.01, 0.1) 支持 \\\"sweet spot\\\" claim\\n- Nice-to-have: SafeLIBERO 4 suite 各 1 task\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl, 代码准备中); (2) 3+ models 的 analysis (Pi0 + Pi0.5 已有, 加 OpenVLA zero-shot eval); (3) 收窄 claim scope + discussion 中做机制分析\\n→ **接受率估算** (Reviewer #37): 1 task ~40% / 2 tasks+2 model ~55-65% / 4 tasks+3 model ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n\\\"任何了解机器人运动学的人都知道肘部会碰\\\"\\n→ **应对**: 强调定量分析 (arm-body vs EE 碰撞比例量化 + oracle 排除其他解释) 而非定性观察; 作为 supporting claim 而非 primary\\n\\n### R3: No positive result\\n\\\"告诉我什么不 work 但没告诉我什么 work\\\"\\n→ **应对**: real_CAR 指标是 positive 工具贡献; Pi0.5+A1 如果成功也是正面结果; diagnostic framework 有方法论价值\\n\\n### R4: Action collapse is trivial\\n\\\"Undertrained Pi0 的 action collapse 不是 safety 特有的, 是训练不足的自然结果\\\"\\n→ **应对**: 必须在论文中承认这一点; 但指出即使原因 trivial, metric contamination 的后果 non-trivial — 后续工作可能基于被污染的 CAR 得出错误结论\\n\\n## Figure Plan\\n\\n| ID | 内容 | 优先级 | 数据来源 |\\n|----|------|--------|---------|\\n| Fig 1 | Fake vs real safety 概念图 | 重要 | 设计 |\\n| Fig 2 | Displacement 分布 (A1 vs baseline vs Pi0.5) | **必须** | 800ep A1 + 200ep baseline + 600ep Pi0.5 |\\n| Fig 3 | TSR-CAR scatter + obstacle geometry 2-panel | 重要 | 多模型/多方法数据 + per-task geometry |\\n| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle variants + baselines |\\n| Table 1 | 3-seed × 2-lambda 完整结果矩阵 | **必须** | Pi0.5+A1 训练结果 (pending) |\\n| Fig 5 | Lambda-CAR 曲线 (4 点: 0, 0.005, 0.01, 0.1) | 重要 | pure LoRA + A1 训练 (pending) |\\n\\n> Fig 3 合并了原 Fig 3 (TSR-CAR scatter) 和 Fig 4 (geometry vs CAR), 按 Reviewer 建议\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会，不是 workshop)\\n**条件**: 需要至少一个正向贡献（Pi0.5+A1 成功 / 新 SDF 集成方式 / full-body SDF PoC）\\n\\n## Narrative Focus (Reviewer Report #30)\\n\\n论文核心贡献应聚焦于 **结构性洞察**（EE-only SDF 无法影响 full-body safety），而非 negative results 堆叠。三次方法失败（A1 openpi / A3 runtime / A1 Pi0.5）如果 root cause 相同，论文叙事应集中在这个 structural insight，各实验作为不同角度的验证。\\n\\n## Negative Results Narrative Strategy (D018 + 16 negatives)\\n\\n16 个阴性结果按叙事功能分为 3 层：\\n\\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\\n这些 negative 本身就是 paper 的 finding：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\\n\\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\\n提供边界信息，但非核心贡献：\\n\\n| 类别 | 实验 | 论文功能 |\\n|------|------|----------|\\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\\n\\n### Tier C: 省略（技术失败 / 与结论无关）\\n不进入论文正文或 appendix：\\n\\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\\n- 被 kill 的实验（资源调度，无结论）\\n\\n### 叙事原则\\n1. Tier A 的 negative 不是\\\"失败\\\"，是 **evidence for structural claims** — 用 \\\"we demonstrate\\\" 而非 \\\"we failed to\\\"\\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\\n4. Tier C 完全不提\\n\\n## Contingency Plans (Post Step-10K Eval)\\n\\n**场景 1 (最可能)**: λ=0.005 ≈ λ=0.01, 均 ≤ baseline → SDF signal 被 action loss 淹没\\n→ Early-stop λ=0.01 runs, 用释放 GPU 跑纯 LoRA baseline + λ=0.1 bracket\\n→ 纯 analysis paper, 聚焦 structural insight\\n\\n**场景 2**: 两个 lambda 均 > baseline, 无差异 → 改善可能来自 LoRA 本身\\n→ 必须对比纯 LoRA baseline 才能归因\\n→ 无纯 LoRA baseline 的 CAR 改善不可发表\\n\\n**场景 2a-2d (LoRA 中间场景，Reviewer 预审补充)**:\\n\\n| LoRA-only CAR | SDF 增量 | 叙事策略 |\\n|---------------|----------|----------|\\n| ~27% (≈baseline) | +30pp 全归 SDF | \\\"geometric supervision is effective\\\" — 最强 method claim |\\n| ~35% | +22pp | \\\"LoRA capacity tuning helps, SDF provides major additional benefit\\\" — 仍强 |\\n| ~45% | +12pp | \\\"LoRA is primary driver, SDF provides dose-dependent safety margin\\\" — 需 4-point lambda 曲线支撑 monotonic trend |\\n| ~55%+ (≈A1) | ≈0pp | 归纯 LoRA → pure analysis paper, SDF 作为 negative evidence |\\n\\n关键防御：即使 SDF 增量仅 +10-15pp，只要 4-point lambda 曲线呈 monotonic trend，仍可 claim \\\"geometric supervision signal provides dose-dependent safety improvement beyond LoRA capacity tuning\\\"。\\n\\n**场景 3**: λ=0.01 > λ=0.005 → SDF 有效\\n→ 继续到 30K, 升级为 \\\"analysis paper with positive method contribution\\\"（非纯 method paper）\\n→ 加 λ=0 (pure LoRA) + λ=0.1 构建 4-point lambda 曲线, 支持 \\\"sweet spot\\\" claim\\n→ 扩展到 spatial_bowl 第 2 task, 强化泛化性\\n\\n## Dependencies\\n\\n- [ ] Pi0.5+A1 训练结果 (Claim 4, Table 1) — ETA 5/24 18:00\\n- [ ] Step 10K mid-eval — ETA 5/23 ~16:25 UTC\\n- [ ] 纯 LoRA baseline (无 SDF/EE loss) — **RUNNING** (westd-45947, 2-seed, ETA ~5/26 01:30)\\n- [ ] λ=0.1 bracket (1-seed Pi0.5) — 10K eval 后启动, 4-point lambda 曲线必需\\n- [ ] spatial_bowl A1 训练 (2-seed × best-lambda) — **代码准备中（Agent 已派 Worker）**, 必须 5/28 前启动（CoRL DDL 约束）\\n- [ ] OpenVLA zero-shot SafeLIBERO eval — 仅 inference, 验证 fake safety 跨模型存在\\n- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake\\n- [x] Oracle 3 variants (Claim 3) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant\\n\", \"total_chars\": 8058, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of:

1. The existing literature map - already has papers on collision-aware VLA, SDF in robotics, VLA foundations, benchmarks, etc.
2. The paper framing - an analysis paper about fake safety in VLA collision avoidance metrics, with SDF auxiliary loss as a method contribution.

The user wants me to search for 2024-2026 papers in two directions:
1. Collision-aware manipulation (broader than just VLA)
2. SDF in robotics

Let me search for recent papers in these areas. I'll use WebSearch to find relevant papers.


Now I'm reviewing what's already in the literature map - there's solid coverage of collision-aware manipulation work like VLSA, SafeVLA, and CAPE from 2024-2025, plus some earlier SDF robotics papers like VoxPoser. I should focus my search on finding any gaps in these areas or newer papers that might have been published more recently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "0c0e4d41-747b-46b3-8fc1-bdace1215c23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SitA9kKxho4UNCEG8UDd6m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 23922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9161
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

_source line 13_

现有文献已覆盖 5 篇 collision-aware 和 6 篇 SDF-robotics 论文。开始搜索 2024-2026 年的补充文献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "6cdefa5f-2685-4c5a-81bb-cc5857b2e588",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SitA9kKxho4UNCEG8UDd6m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 23922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9161
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

_source line 14_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UCNFR785s8BUmTqT9Tp4Fp`</summary>

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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "0db0bb1d-16bb-43f1-853e-7085a8dd9f42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SitA9kKxho4UNCEG8UDd6m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 23922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9161
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

_source line 15 · 2026-05-25T07:41:10.554Z_

<details><summary>↩ Tool result · `toolu_01UCNFR785s8BUmTqT9Tp4Fp`</summary>

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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "9320306d-0247-46a2-bc13-d6f0fa6c8c2e",
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

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01An784shmo2Ky1HLaRH3MQ6`</summary>

```json
{
  "query": "collision-aware robot manipulation learning 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "f00946d1-41f3-4d6f-9cf1-f3c371ce6c84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKhW4SSysUtmFsJoW8f7FF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1056,
      "cache_read_input_tokens": 33083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1056
      },
      "output_tokens": 51,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015gB91coEqJtqDp3kFdAZXf`</summary>

```json
{
  "query": "signed distance field SDF robot motion planning manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "acf4e2e5-1f37-4298-a4fe-17a6600ce3da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKhW4SSysUtmFsJoW8f7FF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1056,
      "cache_read_input_tokens": 33083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1056
      },
      "output_tokens": 51,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K48CZ6nzfHc91m9PADTh7v`</summary>

```json
{
  "query": "safe robot manipulation policy learning contact-aware 2024 2025 ICRA CoRL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "404964d8-41ea-48d9-a323-ec8a518644da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKhW4SSysUtmFsJoW8f7FF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1056,
      "cache_read_input_tokens": 33083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1056
      },
      "output_tokens": 51,
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012LR87SrY9S7NTu9wfDG7od`</summary>

```json
{
  "query": "neural SDF differentiable collision checking robotics 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "1f9ecd70-b787-4090-99aa-918295530593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKhW4SSysUtmFsJoW8f7FF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1056,
      "cache_read_input_tokens": 33083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1056
      },
      "output_tokens": 51,
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

_source line 20 · 2026-05-25T07:41:23.360Z_

<details><summary>↩ Tool result · `toolu_015gB91coEqJtqDp3kFdAZXf`</summary>

```text
Web search results for query: "signed distance field SDF robot motion planning manipulation 2024 2025"

Links: [{"title":"[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"},{"title":"[2204.02296] iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://ar5iv.labs.arxiv.org/html/2204.02296"},{"title":"Predicted Composite Signed-Distance Fields for Real-Time Motion Planning   in Dynamic Environments","url":"https://arxiv.org/pdf/2008.00969"},{"title":"Configuration Space Distance Fields for Manipulation Planning","url":"https://calinon.ch/papers/Li-RSS2024.pdf"},{"title":"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using   Implicit Signed Distance Functions","url":"https://arxiv.org/pdf/2305.10534"},{"title":"Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/pdf/2406.01137"},{"title":"Collision-free Motion Generation Based on Stochastic Optimization and   Composite Signed Distance Field Networks of Articulated Robot","url":"https://arxiv.org/pdf/2306.04130"}]

Here are the key findings from the web search on signed distance fields (SDFs) for robot motion planning and manipulation in 2024-2025:

## Recent Developments

**Configuration Space Distance Fields (2024):**
SDFs are popular implicit shape representations in robotics, providing geometric information about objects and obstacles that can be combined with control, optimization and learning techniques. SDFs can be used in robot configuration spaces, which for a robot manipulator typically corresponds to the joint angles. For manipulation tasks, configuration distance fields (CDFs) directly estimate the minimum joint motion required by the robot to establish contact with an object.

**Composite SDF Networks (2025):**
A stochastic optimization-based motion generation method generates collision-free and time-optimal motion for articulated robots represented by composite SDF networks and integrates these networks into trajectory planning algorithms.

**Spatial Anchor-based Motion Policy (2025):**
A unified framework called SAMP simultaneously encodes the environment and the manipulator using signed distance fields anchored on a shared spatial grid.

## Real-Time Applications

iSDF produces more accurate reconstructions and better approximations of collision costs and gradients useful for downstream planners in domains from navigation to manipulation. Using SDFs allows for smoother collision cost definitions in trajectory planning and, combined with safety guarantees of vector field trajectory followers, enables incremental real-time global trajectory planning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "2d8f3e02-c0c8-4b27-8db4-ca14c8606971",
  "tool_use_result": {
    "query": "signed distance field SDF robot motion planning manipulation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QrnrWTUNGFggvNr8eSUBSg",
        "content": [
          {
            "title": "[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"
          },
          {
            "title": "[2204.02296] iSDF: Real-Time Neural Signed Distance Fields for Robot Perception",
            "url": "https://ar5iv.labs.arxiv.org/html/2204.02296"
          },
          {
            "title": "Predicted Composite Signed-Distance Fields for Real-Time Motion Planning   in Dynamic Environments",
            "url": "https://arxiv.org/pdf/2008.00969"
          },
          {
            "title": "Configuration Space Distance Fields for Manipulation Planning",
            "url": "https://calinon.ch/papers/Li-RSS2024.pdf"
          },
          {
            "title": "RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using   Implicit Signed Distance Functions",
            "url": "https://arxiv.org/pdf/2305.10534"
          },
          {
            "title": "Configuration Space Distance Fields for Manipulation Planning",
            "url": "https://arxiv.org/pdf/2406.01137"
          },
          {
            "title": "Collision-free Motion Generation Based on Stochastic Optimization and   Composite Signed Distance Field Networks of Articulated Robot",
            "url": "https://arxiv.org/pdf/2306.04130"
          }
        ]
      },
      "Here are the key findings from the web search on signed distance fields (SDFs) for robot motion planning and manipulation in 2024-2025:\n\n## Recent Developments\n\n**Configuration Space Distance Fields (2024):**\nSDFs are popular implicit shape representations in robotics, providing geometric information about objects and obstacles that can be combined with control, optimization and learning techniques. SDFs can be used in robot configuration spaces, which for a robot manipulator typically corresponds to the joint angles. For manipulation tasks, configuration distance fields (CDFs) directly estimate the minimum joint motion required by the robot to establish contact with an object.\n\n**Composite SDF Networks (2025):**\nA stochastic optimization-based motion generation method generates collision-free and time-optimal motion for articulated robots represented by composite SDF networks and integrates these networks into trajectory planning algorithms.\n\n**Spatial Anchor-based Motion Policy (2025):**\nA unified framework called SAMP simultaneously encodes the environment and the manipulator using signed distance fields anchored on a shared spatial grid.\n\n## Real-Time Applications\n\niSDF produces more accurate reconstructions and better approximations of collision costs and gradients useful for downstream planners in domains from navigation to manipulation. Using SDFs allows for smoother collision cost definitions in trajectory planning and, combined with safety guarantees of vector field trajectory followers, enables incremental real-time global trajectory planning."
    ],
    "durationSeconds": 6.363768781999999
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T07:41:24.689Z_

<details><summary>↩ Tool result · `toolu_01An784shmo2Ky1HLaRH3MQ6`</summary>

```text
Web search results for query: "collision-aware robot manipulation learning 2024 2025 arxiv"

Links: [{"title":"A Contact-Safe Reinforcement Learning Framework for Contact-Rich Robot Manipulation","url":"https://arxiv.org/pdf/2207.13438"},{"title":"Language-Guided Object-Centric Diffusion Policy for Generalizable and   Collision-Aware Robotic Manipulation","url":"https://arxiv.org/pdf/2407.00451"},{"title":"Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions","url":"https://arxiv.org/pdf/2412.06983"},{"title":"Robotics Jan 2025","url":"https://www.arxiv.org/list/cs.RO/2025-01?skip=25&show=250"},{"title":"Towards Autonomous Reinforcement Learning for Real-World Robotic Manipulation with Large Language Models","url":"https://arxiv.org/html/2503.04280v2"},{"title":"[2408.14183] Robot Navigation with Entity-Based Collision Avoidance using Deep Reinforcement Learning","url":"https://arxiv.org/abs/2408.14183"}]

I found several relevant research papers on collision-aware robot manipulation learning from arxiv. Here are the key findings:

## Recent Papers (2024-2025)

**Language-Guided Object-Centric Diffusion Policy (2024):**
This framework adapts to unseen situations such as cluttered scenes, shifting camera views, and ambiguous similar objects while offering training-free collision avoidance and achieving high success rates with few demonstrations. The approach trains a diffusion model conditioned on 3D point clouds to predict end-effector trajectories, and incorporates cost optimization into denoising steps to guide generated trajectories to be collision-free.

**Collision-Inclusive Manipulation Planning (2024):**
This work addresses grasp configurations where the target object is occluded by surrounding objects, requiring the robot to collide with surrounding objects for successful grasping by allowing safe interactions between the gripper and environment. Such collision-inclusive strategies require safe contact and effective interactions between the robot and objects, for which robot compliance is essential.

**Autonomous Reinforcement Learning with LLMs (2025):**
Recent work includes APIs for contact and collision checks as part of frameworks for real-world robotic manipulation using large language models.

**Robot Navigation with Collision Avoidance (2024):**
A deep reinforcement learning approach improves robot navigation with entity-based collision avoidance, using information about entity types and introducing reward functions that penalize proximity to different types of agents and obstacles.

These papers demonstrate the active research area combining collision awareness with robot learning through various approaches including diffusion models, reinforcement learning, and language-guided frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "39a8a681-63c2-4645-a693-559818fbe326",
  "tool_use_result": {
    "query": "collision-aware robot manipulation learning 2024 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YRLztj1LSkvqMn36RhiX7v",
        "content": [
          {
            "title": "A Contact-Safe Reinforcement Learning Framework for Contact-Rich Robot Manipulation",
            "url": "https://arxiv.org/pdf/2207.13438"
          },
          {
            "title": "Language-Guided Object-Centric Diffusion Policy for Generalizable and   Collision-Aware Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2407.00451"
          },
          {
            "title": "Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions",
            "url": "https://arxiv.org/pdf/2412.06983"
          },
          {
            "title": "Robotics Jan 2025",
            "url": "https://www.arxiv.org/list/cs.RO/2025-01?skip=25&show=250"
          },
          {
            "title": "Towards Autonomous Reinforcement Learning for Real-World Robotic Manipulation with Large Language Models",
            "url": "https://arxiv.org/html/2503.04280v2"
          },
          {
            "title": "[2408.14183] Robot Navigation with Entity-Based Collision Avoidance using Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2408.14183"
          }
        ]
      },
      "I found several relevant research papers on collision-aware robot manipulation learning from arxiv. Here are the key findings:\n\n## Recent Papers (2024-2025)\n\n**Language-Guided Object-Centric Diffusion Policy (2024):**\nThis framework adapts to unseen situations such as cluttered scenes, shifting camera views, and ambiguous similar objects while offering training-free collision avoidance and achieving high success rates with few demonstrations. The approach trains a diffusion model conditioned on 3D point clouds to predict end-effector trajectories, and incorporates cost optimization into denoising steps to guide generated trajectories to be collision-free.\n\n**Collision-Inclusive Manipulation Planning (2024):**\nThis work addresses grasp configurations where the target object is occluded by surrounding objects, requiring the robot to collide with surrounding objects for successful grasping by allowing safe interactions between the gripper and environment. Such collision-inclusive strategies require safe contact and effective interactions between the robot and objects, for which robot compliance is essential.\n\n**Autonomous Reinforcement Learning with LLMs (2025):**\nRecent work includes APIs for contact and collision checks as part of frameworks for real-world robotic manipulation using large language models.\n\n**Robot Navigation with Collision Avoidance (2024):**\nA deep reinforcement learning approach improves robot navigation with entity-based collision avoidance, using information about entity types and introducing reward functions that penalize proximity to different types of agents and obstacles.\n\nThese papers demonstrate the active research area combining collision awareness with robot learning through various approaches including diffusion models, reinforcement learning, and language-guided frameworks."
    ],
    "durationSeconds": 8.158197986
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T07:41:26.256Z_

<details><summary>↩ Tool result · `toolu_012LR87SrY9S7NTu9wfDG7od`</summary>

```text
Web search results for query: "neural SDF differentiable collision checking robotics 2024 2025"

Links: [{"title":"Neural SDF: Implicit 3D Geometry","url":"https://www.emergentmind.com/topics/neural-signed-distance-function-sdf"},{"title":"Neural Signed Distance Functions (SDFs)","url":"https://www.emergentmind.com/topics/neural-signed-distance-functions-sdfs"},{"title":"Neural Signed Distance Field (NSDF)","url":"https://www.emergentmind.com/topics/neural-signed-distance-field-nsdf"},{"title":"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion","url":"https://arxiv.org/html/2409.14955v1"},{"title":"Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024","url":"https://www.roboticsproceedings.org/rss20/p131.pdf"},{"title":"Differentiable Composite Neural Signed Distance Fields for Robot   Navigation in Dynamic Indoor Environments","url":"https://arxiv.org/pdf/2502.02664"},{"title":"Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251401223"}]

Based on the web search results, here's what I found about neural SDF differentiable collision checking in robotics for 2024-2025:

## Key Applications and Recent Work

Real-time, differentiable SDFs facilitate collision checking, grasp planning, and trajectory optimization in robot perception and planning. Systems like iSDF and HIO-SDF provide compact, adaptive, and updatable representations suited for mobile robots in evolving workspaces.

## Recent Developments (2024-2025)

Differentiable composite SDFs supply robust collision checking, continuous gradients, and online scene adaptation suitable for robot motion planning in dynamic and partially observed environments. 

Neural Signed Distance Fields provide a differentiable environment representation to readily obtain collision checks and well-defined gradients for robot navigation tasks. However, updating neural SDFs as the scene evolves entails re-training, which is tedious, time consuming, and inefficient.

## Advanced Techniques

A neural variant called neural CDF has been proposed, which offers a compact, continuous, analytical, and latent space representation, thereby facilitating seamless integration into learning, optimization, and control frameworks.

Recent work also includes neural nonlinear model predictive control (NMPC) frameworks for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "11206070-3845-4a49-94f8-23380e2ec6c7",
  "tool_use_result": {
    "query": "neural SDF differentiable collision checking robotics 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P4DiPigNUbA23w4w2fbQp4",
        "content": [
          {
            "title": "Neural SDF: Implicit 3D Geometry",
            "url": "https://www.emergentmind.com/topics/neural-signed-distance-function-sdf"
          },
          {
            "title": "Neural Signed Distance Functions (SDFs)",
            "url": "https://www.emergentmind.com/topics/neural-signed-distance-functions-sdfs"
          },
          {
            "title": "Neural Signed Distance Field (NSDF)",
            "url": "https://www.emergentmind.com/topics/neural-signed-distance-field-nsdf"
          },
          {
            "title": "Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion",
            "url": "https://arxiv.org/html/2409.14955v1"
          },
          {
            "title": "Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024",
            "url": "https://www.roboticsproceedings.org/rss20/p131.pdf"
          },
          {
            "title": "Differentiable Composite Neural Signed Distance Fields for Robot   Navigation in Dynamic Indoor Environments",
            "url": "https://arxiv.org/pdf/2502.02664"
          },
          {
            "title": "Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/02783649251401223"
          }
        ]
      },
      "Based on the web search results, here's what I found about neural SDF differentiable collision checking in robotics for 2024-2025:\n\n## Key Applications and Recent Work\n\nReal-time, differentiable SDFs facilitate collision checking, grasp planning, and trajectory optimization in robot perception and planning. Systems like iSDF and HIO-SDF provide compact, adaptive, and updatable representations suited for mobile robots in evolving workspaces.\n\n## Recent Developments (2024-2025)\n\nDifferentiable composite SDFs supply robust collision checking, continuous gradients, and online scene adaptation suitable for robot motion planning in dynamic and partially observed environments. \n\nNeural Signed Distance Fields provide a differentiable environment representation to readily obtain collision checks and well-defined gradients for robot navigation tasks. However, updating neural SDFs as the scene evolves entails re-training, which is tedious, time consuming, and inefficient.\n\n## Advanced Techniques\n\nA neural variant called neural CDF has been proposed, which offers a compact, continuous, analytical, and latent space representation, thereby facilitating seamless integration into learning, optimization, and control frameworks.\n\nRecent work also includes neural nonlinear model predictive control (NMPC) frameworks for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing."
    ],
    "durationSeconds": 8.093662185000001
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T07:41:35.124Z_

<details><summary>↩ Tool result · `toolu_01K48CZ6nzfHc91m9PADTh7v`</summary>

```text
Web search results for query: "safe robot manipulation policy learning contact-aware 2024 2025 ICRA CoRL"

Links: [{"title":"A Contact-Safe Reinforcement Learning Framework for Contact-Rich Robot Manipulation","url":"https://arxiv.org/pdf/2207.13438"},{"title":"Uncertainty-aware Contact-safe Model-based Reinforcement Learning","url":"https://arxiv.org/pdf/2010.08169"},{"title":"Learning to Act Through Contact: A Unified View of Multi-Task Robot Learning","url":"https://arxiv.org/pdf/2510.03599"},{"title":"Workshop on Generalizable Priors for Robot Manipulation | CoRL 2025","url":"https://corl25-genpriors.github.io/"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models","url":"https://arxiv.org/pdf/2602.09017"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/pdf/2512.11908"},{"title":"SRL-VIC: A Variable Stiffness-Based Safe Reinforcement Learning for   Contact-Rich Robotic Tasks","url":"https://arxiv.org/pdf/2406.13744"}]

Based on the search results, here are the key findings related to safe robot manipulation policy learning with contact-awareness for 2024-2025 in ICRA and CoRL conferences:

## Recent Research Papers

A comprehensive survey on safe learning-based methods for robot contact-rich tasks categorizes existing approaches into safe exploration, which minimizes risk during learning, and safe execution, which ensures policy robustness during deployment.

Key techniques include constrained reinforcement learning, risk-sensitive optimization, uncertainty-aware modeling, control barrier functions, and model predictive safety shields.

## Specific Works

A contact-safe reinforcement learning framework for contact-rich robot manipulation maintains safety in both task and joint space by immediately detecting collisions and ensuring contact force remains small.

Contact-safe model-based reinforcement learning uses probabilistic model predictive control with control limits associated to model uncertainty, adjusting allowed acceleration according to learning progress.

## 2025 Conference Spotlight

Recent work presented at the CoRL 2025 Workshop on Generalizable Priors for Robot Manipulation includes research on "Touch begins where vision ends: Generalizable policies for contact-rich manipulation" and "Learning to Act Through Contact: A Unified View of Multi-Task Robot Learning".

These works collectively address the challenge of ensuring safety during both policy learning and execution in contact-rich manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "120a4b31-b06e-49e3-9b9e-3d2c1947c231",
  "tool_use_result": {
    "query": "safe robot manipulation policy learning contact-aware 2024 2025 ICRA CoRL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XT4FzyCLuAFTzFAF6LtjpF",
        "content": [
          {
            "title": "A Contact-Safe Reinforcement Learning Framework for Contact-Rich Robot Manipulation",
            "url": "https://arxiv.org/pdf/2207.13438"
          },
          {
            "title": "Uncertainty-aware Contact-safe Model-based Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2010.08169"
          },
          {
            "title": "Learning to Act Through Contact: A Unified View of Multi-Task Robot Learning",
            "url": "https://arxiv.org/pdf/2510.03599"
          },
          {
            "title": "Workshop on Generalizable Priors for Robot Manipulation | CoRL 2025",
            "url": "https://corl25-genpriors.github.io/"
          },
          {
            "title": "Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation",
            "url": "https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"
          },
          {
            "title": "Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models",
            "url": "https://arxiv.org/pdf/2602.09017"
          },
          {
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/pdf/2512.11908"
          },
          {
            "title": "SRL-VIC: A Variable Stiffness-Based Safe Reinforcement Learning for   Contact-Rich Robotic Tasks",
            "url": "https://arxiv.org/pdf/2406.13744"
          }
        ]
      },
      "Based on the search results, here are the key findings related to safe robot manipulation policy learning with contact-awareness for 2024-2025 in ICRA and CoRL conferences:\n\n## Recent Research Papers\n\nA comprehensive survey on safe learning-based methods for robot contact-rich tasks categorizes existing approaches into safe exploration, which minimizes risk during learning, and safe execution, which ensures policy robustness during deployment.\n\nKey techniques include constrained reinforcement learning, risk-sensitive optimization, uncertainty-aware modeling, control barrier functions, and model predictive safety shields.\n\n## Specific Works\n\nA contact-safe reinforcement learning framework for contact-rich robot manipulation maintains safety in both task and joint space by immediately detecting collisions and ensuring contact force remains small.\n\nContact-safe model-based reinforcement learning uses probabilistic model predictive control with control limits associated to model uncertainty, adjusting allowed acceleration according to learning progress.\n\n## 2025 Conference Spotlight\n\nRecent work presented at the CoRL 2025 Workshop on Generalizable Priors for Robot Manipulation includes research on \"Touch begins where vision ends: Generalizable policies for contact-rich manipulation\" and \"Learning to Act Through Contact: A Unified View of Multi-Task Robot Learning\".\n\nThese works collectively address the challenge of ensuring safety during both policy learning and execution in contact-rich manipulation tasks."
    ],
    "durationSeconds": 17.089764089999996
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
I found some interesting leads. Let me search for more specific papers to get details:

1. **Configuration Space Distance Fields** (Li et al., RSS 2024) - this is interesting for SDF direction
2. **Composite SDF Networks** for articulated robots (Liu et al., 2023/2025)
3. **Neural NMPC through SDF encoding** (Jacquet et al., 2025)
4. **Collision-Inclusive Manipulation Planning** (2024)
5. **Safe Learning for Contact-Rich Tasks survey** (2025)
6. **SRL-VIC** (2024)


7. Now I'm doing more targeted searches to find recent papers from 2024-2026 that fill the gaps and aren't already covered in my literature map.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "4555ac3a-f77b-478b-bc0a-9c4085e0b6e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNqH4xfQyp1xUwTw56GMWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 2487,
      "cache_read_input_tokens": 34139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2487
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

_source line 25_

找到几条有价值的线索，继续深挖具体论文细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "edbf7af7-2785-48c1-bf1c-ae794c6c92e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNqH4xfQyp1xUwTw56GMWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 2487,
      "cache_read_input_tokens": 34139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2487
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ThWC2TenZGPoGfuRvhniiy`</summary>

```json
{
  "query": "arxiv 2406.01137 Configuration Space Distance Fields manipulation planning RSS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "88543ed8-9766-4d96-9291-550e0da103cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNqH4xfQyp1xUwTw56GMWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 2487,
      "cache_read_input_tokens": 34139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2487
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ChU3EUpRqiN1WaCc93xzLh`</summary>

```json
{
  "query": "arxiv 2502.02664 differentiable composite neural signed distance fields robot navigation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "7b1f000d-cd13-4813-a5e4-7e59cf134dbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNqH4xfQyp1xUwTw56GMWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 2487,
      "cache_read_input_tokens": 34139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2487
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018bYpMjfagf8ZAk7tSHWSjC`</summary>

```json
{
  "query": "\"neural NMPC\" \"signed distance field\" collision avoidance robot 2025 Jacquet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "bb85a767-a150-46b9-8ead-a88c78011c88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNqH4xfQyp1xUwTw56GMWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 2487,
      "cache_read_input_tokens": 34139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2487
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JrTZu6aKBhKUhT1H9Bkn1s`</summary>

```json
{
  "query": "arxiv 2512.11908 safe learning contact-rich robot survey foundation models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "9e71c3a1-b2de-4e3e-9082-4d1378de6ec7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNqH4xfQyp1xUwTw56GMWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 2487,
      "cache_read_input_tokens": 34139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2487
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

_source line 30 · 2026-05-25T07:41:50.889Z_

<details><summary>↩ Tool result · `toolu_01ThWC2TenZGPoGfuRvhniiy`</summary>

```text
Web search results for query: "arxiv 2406.01137 Configuration Space Distance Fields manipulation planning RSS 2024"

Links: [{"title":"[2406.01137] Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/abs/2406.01137"},{"title":"Configuration Space Distance Fields for Manipulation Planning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240601137L/abstract"},{"title":"Configuration Space Distance Fields for Manipulation Planning","url":"https://calinon.ch/papers/Li-RSS2024.pdf"},{"title":"(PDF) Configuration Space Distance Fields for Manipulation Planning","url":"https://www.researchgate.net/publication/381122586_Configuration_Space_Distance_Fields_for_Manipulation_Planning"},{"title":"[PDF] Configuration Space Distance Fields for Manipulation Planning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Configuration-Space-Distance-Fields-for-Planning-Li-Chi/75af8f157566854a49e72ead68f807166b791809"},{"title":"One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields","url":"https://arxiv.org/html/2509.00836"},{"title":"(PDF) Neural Configuration-Space Barriers for Manipulation Planning and Control","url":"https://www.researchgate.net/publication/389694312_Neural_Configuration-Space_Barriers_for_Manipulation_Planning_and_Control"}]

Based on the search results, here's what I found about arxiv paper 2406.01137:

## Paper Overview

This paper demonstrates the potential of considering signed distance fields (SDFs) in the robot configuration space for optimization, which is called the configuration space distance field.

## Key Details

- **Title**: Configuration Space Distance Fields for Manipulation Planning
- **Authors**: Yiming Li, Xuemin Chi, Amirreza Razmjoo, and Sylvain Calinon
- **Submission Date**: June 3, 2024
- **Venue**: Accepted to Robotics: Science and Systems (RSS), 2024

## Main Contribution

The signed distance field is a popular implicit shape representation in robotics, providing geometric information about objects and obstacles in a form that can easily be combined with control, optimization and learning techniques. While SDFs are most often used to represent distances in task space, this paper extends the approach to robot configuration spaces, which typically correspond to the joint angles for each articulation of the robot.

The paper demonstrates the potential of considering SDFs in the robot configuration space for optimization and proposes an efficient algorithm to compute and fuse configuration space distance fields (CDFs) that can be generalized to arbitrary scenes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "88f66e07-ab7c-482b-b0cb-c8e3183b8f0d",
  "tool_use_result": {
    "query": "arxiv 2406.01137 Configuration Space Distance Fields manipulation planning RSS 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FGDM4Dp2z6rUVMBb1h7dCT",
        "content": [
          {
            "title": "[2406.01137] Configuration Space Distance Fields for Manipulation Planning",
            "url": "https://arxiv.org/abs/2406.01137"
          },
          {
            "title": "Configuration Space Distance Fields for Manipulation Planning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240601137L/abstract"
          },
          {
            "title": "Configuration Space Distance Fields for Manipulation Planning",
            "url": "https://calinon.ch/papers/Li-RSS2024.pdf"
          },
          {
            "title": "(PDF) Configuration Space Distance Fields for Manipulation Planning",
            "url": "https://www.researchgate.net/publication/381122586_Configuration_Space_Distance_Fields_for_Manipulation_Planning"
          },
          {
            "title": "[PDF] Configuration Space Distance Fields for Manipulation Planning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Configuration-Space-Distance-Fields-for-Planning-Li-Chi/75af8f157566854a49e72ead68f807166b791809"
          },
          {
            "title": "One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields",
            "url": "https://arxiv.org/html/2509.00836"
          },
          {
            "title": "(PDF) Neural Configuration-Space Barriers for Manipulation Planning and Control",
            "url": "https://www.researchgate.net/publication/389694312_Neural_Configuration-Space_Barriers_for_Manipulation_Planning_and_Control"
          }
        ]
      },
      "Based on the search results, here's what I found about arxiv paper 2406.01137:\n\n## Paper Overview\n\nThis paper demonstrates the potential of considering signed distance fields (SDFs) in the robot configuration space for optimization, which is called the configuration space distance field.\n\n## Key Details\n\n- **Title**: Configuration Space Distance Fields for Manipulation Planning\n- **Authors**: Yiming Li, Xuemin Chi, Amirreza Razmjoo, and Sylvain Calinon\n- **Submission Date**: June 3, 2024\n- **Venue**: Accepted to Robotics: Science and Systems (RSS), 2024\n\n## Main Contribution\n\nThe signed distance field is a popular implicit shape representation in robotics, providing geometric information about objects and obstacles in a form that can easily be combined with control, optimization and learning techniques. While SDFs are most often used to represent distances in task space, this paper extends the approach to robot configuration spaces, which typically correspond to the joint angles for each articulation of the robot.\n\nThe paper demonstrates the potential of considering SDFs in the robot configuration space for optimization and proposes an efficient algorithm to compute and fuse configuration space distance fields (CDFs) that can be generalized to arbitrary scenes."
    ],
    "durationSeconds": 7.021469215000004
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T07:41:51.603Z_

<details><summary>↩ Tool result · `toolu_018bYpMjfagf8ZAk7tSHWSjC`</summary>

```text
Web search results for query: ""neural NMPC" "signed distance field" collision avoidance robot 2025 Jacquet"

Links: [{"title":"[2511.21312] Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/abs/2511.21312"},{"title":"Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251401223"},{"title":"AiSDF: Structure-aware Neural Signed Distance Fields in Indoor Scenes","url":"https://www.researchgate.net/publication/378844122_AiSDF_Structure-aware_Neural_Signed_Distance_Fields_in_Indoor_Scenes"},{"title":"Neural SDF-MPC (NMPC) - Unified Autonomy Stack","url":"https://ntnu-arl.github.io/unified_autonomy_stack/nmpc/"},{"title":"GitHub - ntnu-arl/sdf-nmpc","url":"https://github.com/ntnu-arl/sdf-nmpc"},{"title":"N-MPC for Deep Neural Network-Based Collision Avoidance exploiting Depth Images | Request PDF","url":"https://www.researchgate.net/publication/382984469_N-MPC_for_Deep_Neural_Network-Based_Collision_Avoidance_exploiting_Depth_Images"},{"title":"(PDF) Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://www.researchgate.net/publication/398025684_Neural_NMPC_through_Signed_Distance_Field_Encoding_for_Collision_Avoidance"},{"title":"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/pdf/2511.21312"},{"title":"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/html/2511.21312v1"}]

Based on the search results, I found a recent paper by Martin Jacquet and colleagues on this exact topic:

The research introduces a neural nonlinear model predictive control (NMPC) framework for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing, leveraging deep neural networks to encode a single range image into a signed distance function (SDF).

The proposed neural architecture consists of two cascaded networks: a convolutional encoder that compresses the input image into a low-dimensional latent vector, and a Multi-Layer Perceptron that approximates the corresponding spatial SDF, with this latter network parametrizing an explicit position constraint used for collision avoidance embedded in a velocity-tracking NMPC that outputs thrust and attitude commands to the robot.

The real-world experiments are conducted in forest environments, demonstrating that the neural NMPC effectively performs collision avoidance in cluttered settings against an adversarial reference velocity input and drifting position estimates. The implementation of the contributed NMPC and the associated neural networks is released open-source.

The paper was published in December 2025 in the International Journal of Robotics Research, with an arXiv preprint released in November 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "5259f072-f990-4159-ae26-9c69e01c4892",
  "tool_use_result": {
    "query": "\"neural NMPC\" \"signed distance field\" collision avoidance robot 2025 Jacquet",
    "results": [
      {
        "tool_use_id": "srvtoolu_013fi3wX96cEa4audkGt2sy2",
        "content": [
          {
            "title": "[2511.21312] Neural NMPC through Signed Distance Field Encoding for Collision Avoidance",
            "url": "https://arxiv.org/abs/2511.21312"
          },
          {
            "title": "Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/02783649251401223"
          },
          {
            "title": "AiSDF: Structure-aware Neural Signed Distance Fields in Indoor Scenes",
            "url": "https://www.researchgate.net/publication/378844122_AiSDF_Structure-aware_Neural_Signed_Distance_Fields_in_Indoor_Scenes"
          },
          {
            "title": "Neural SDF-MPC (NMPC) - Unified Autonomy Stack",
            "url": "https://ntnu-arl.github.io/unified_autonomy_stack/nmpc/"
          },
          {
            "title": "GitHub - ntnu-arl/sdf-nmpc",
            "url": "https://github.com/ntnu-arl/sdf-nmpc"
          },
          {
            "title": "N-MPC for Deep Neural Network-Based Collision Avoidance exploiting Depth Images | Request PDF",
            "url": "https://www.researchgate.net/publication/382984469_N-MPC_for_Deep_Neural_Network-Based_Collision_Avoidance_exploiting_Depth_Images"
          },
          {
            "title": "(PDF) Neural NMPC through Signed Distance Field Encoding for Collision Avoidance",
            "url": "https://www.researchgate.net/publication/398025684_Neural_NMPC_through_Signed_Distance_Field_Encoding_for_Collision_Avoidance"
          },
          {
            "title": "Neural NMPC through Signed Distance Field Encoding for Collision Avoidance",
            "url": "https://arxiv.org/pdf/2511.21312"
          },
          {
            "title": "Neural NMPC through Signed Distance Field Encoding for Collision Avoidance",
            "url": "https://arxiv.org/html/2511.21312v1"
          }
        ]
      },
      "Based on the search results, I found a recent paper by Martin Jacquet and colleagues on this exact topic:\n\nThe research introduces a neural nonlinear model predictive control (NMPC) framework for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing, leveraging deep neural networks to encode a single range image into a signed distance function (SDF).\n\nThe proposed neural architecture consists of two cascaded networks: a convolutional encoder that compresses the input image into a low-dimensional latent vector, and a Multi-Layer Perceptron that approximates the corresponding spatial SDF, with this latter network parametrizing an explicit position constraint used for collision avoidance embedded in a velocity-tracking NMPC that outputs thrust and attitude commands to the robot.\n\nThe real-world experiments are conducted in forest environments, demonstrating that the neural NMPC effectively performs collision avoidance in cluttered settings against an adversarial reference velocity input and drifting position estimates. The implementation of the contributed NMPC and the associated neural networks is released open-source.\n\nThe paper was published in December 2025 in the International Journal of Robotics Research, with an arXiv preprint released in November 2025."
    ],
    "durationSeconds": 6.182786275999999
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T07:41:51.740Z_

<details><summary>↩ Tool result · `toolu_01JrTZu6aKBhKUhT1H9Bkn1s`</summary>

```text
Web search results for query: "arxiv 2512.11908 safe learning contact-rich robot survey foundation models"

Links: [{"title":"[2512.11908] Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/abs/2512.11908"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/pdf/2512.11908"},{"title":"(PDF) Safe Learning for Contact-Rich Robot Tasks: A Survey From Classical Learning-Based Methods to Safe Foundation Models","url":"https://www.researchgate.net/publication/398287994_Safe_Learning_for_Contact-Rich_Robot_Tasks_A_Survey_From_Classical_Learning-Based_Methods_to_Safe_Foundation_Models"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/html/2512.11908v2"},{"title":"GitHub - jack-sherman01/Awesome-Learning4Safe-Contact-rich-tasks: A paper collection for learning based methods for safe contact-rich robotics tasks · GitHub","url":"https://github.com/jack-sherman01/Awesome-Learning4Safe-Contact-rich-tasks"},{"title":"A Survey on Imitation Learning for Contact-Rich Tasks in Robotics","url":"https://arxiv.org/pdf/2506.13498"}]

Based on the search results, I found the paper you're looking for:

**Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models** (arXiv:2512.11908) is authored by Heng Zhang, Rui Dai, Gokhan Solak, Pokuang Zhou, Yu She, and Arash Ajoudani. The paper was last revised on January 26, 2026.

**Overview:**

The survey addresses contact-rich tasks which pose significant challenges for robotic systems due to inherent uncertainty, complex dynamics, and the high risk of damage during interaction. While learning-based control has shown great potential in enabling robots to acquire and generalize complex manipulation skills, ensuring safety during exploration and execution remains critical for reliable real-world deployment.

**Scope:**

The survey categorizes existing approaches into two main domains: safe exploration and safe execution, and reviews key techniques including constrained reinforcement learning, risk-sensitive optimization, uncertainty-aware modeling, control barrier functions, and model predictive safety shields.

The paper provides a comprehensive overview that bridges classical learning-based methods with emerging robotic foundation models for safe contact-rich manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "d57efc50-c6aa-4297-8816-2d37c57092b7",
  "tool_use_result": {
    "query": "arxiv 2512.11908 safe learning contact-rich robot survey foundation models",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SZwj1dVXbF6Smav9WLdocY",
        "content": [
          {
            "title": "[2512.11908] Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/abs/2512.11908"
          },
          {
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/pdf/2512.11908"
          },
          {
            "title": "(PDF) Safe Learning for Contact-Rich Robot Tasks: A Survey From Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://www.researchgate.net/publication/398287994_Safe_Learning_for_Contact-Rich_Robot_Tasks_A_Survey_From_Classical_Learning-Based_Methods_to_Safe_Foundation_Models"
          },
          {
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/html/2512.11908v2"
          },
          {
            "title": "GitHub - jack-sherman01/Awesome-Learning4Safe-Contact-rich-tasks: A paper collection for learning based methods for safe contact-rich robotics tasks · GitHub",
            "url": "https://github.com/jack-sherman01/Awesome-Learning4Safe-Contact-rich-tasks"
          },
          {
            "title": "A Survey on Imitation Learning for Contact-Rich Tasks in Robotics",
            "url": "https://arxiv.org/pdf/2506.13498"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models** (arXiv:2512.11908) is authored by Heng Zhang, Rui Dai, Gokhan Solak, Pokuang Zhou, Yu She, and Arash Ajoudani. The paper was last revised on January 26, 2026.\n\n**Overview:**\n\nThe survey addresses contact-rich tasks which pose significant challenges for robotic systems due to inherent uncertainty, complex dynamics, and the high risk of damage during interaction. While learning-based control has shown great potential in enabling robots to acquire and generalize complex manipulation skills, ensuring safety during exploration and execution remains critical for reliable real-world deployment.\n\n**Scope:**\n\nThe survey categorizes existing approaches into two main domains: safe exploration and safe execution, and reviews key techniques including constrained reinforcement learning, risk-sensitive optimization, uncertainty-aware modeling, control barrier functions, and model predictive safety shields.\n\nThe paper provides a comprehensive overview that bridges classical learning-based methods with emerging robotic foundation models for safe contact-rich manipulation tasks."
    ],
    "durationSeconds": 6.108031463000007
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T07:41:53.770Z_

<details><summary>↩ Tool result · `toolu_01ChU3EUpRqiN1WaCc93xzLh`</summary>

```text
Web search results for query: "arxiv 2502.02664 differentiable composite neural signed distance fields robot navigation"

Links: [{"title":"[2502.02664] Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments","url":"https://arxiv.org/abs/2502.02664"},{"title":"Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments","url":"https://arxiv.org/html/2502.02664"},{"title":"Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments - YouTube","url":"https://www.youtube.com/watch?v=YI7LUMmFpS0"},{"title":"Differentiable Composite Neural Signed Distance Fields for Robot   Navigation in Dynamic Indoor Environments","url":"https://arxiv.org/pdf/2502.02664"},{"title":"GitHub - stalhabukhari/comp-sdf-dyn-nav: Code for ICRA'25 paper: \"Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments\" · GitHub","url":"https://github.com/stalhabukhari/comp-sdf-dyn-nav"},{"title":"RNBF: Real-Time RGB-D Based Neural Barrier Functions for Safe Robotic Navigation","url":"https://arxiv.org/html/2505.02294v2"},{"title":"Neural Signed Distance Functions (SDFs)","url":"https://www.emergentmind.com/topics/neural-signed-distance-functions-sdfs"}]

I found the paper you're searching for! Here's what I found:

arXiv:2502.02664 is titled "Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments", authored by S. Talha Bukhari, Daniel Lawson, and Ahmed H. Qureshi.

**Key Contributions:**

Neural Signed Distance Fields (SDFs) provide a differentiable environment representation to readily obtain collision checks and well-defined gradients for robot navigation tasks. However, updating neural SDFs as the scene evolves entails re-training, which is tedious, time consuming, and inefficient, making it unsuitable for robot navigation with limited field-of-view in dynamic environments.

The authors propose a compositional framework of neural SDFs to solve robot navigation in indoor environments using only an onboard RGB-D sensor. The framework embodies a dual mode procedure for trajectory optimization, with different modes using complementary methods of modeling collision costs and collision avoidance gradients.

**Paper Details:**
- Submitted on 4 Feb 2025, with the latest revision on 6 Mar 2025
- This is an ICRA'25 paper with code available on GitHub

You can access the full paper at https://arxiv.org/abs/2502.02664


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "68a04cff-b6a6-4a5f-bfa5-1996d3e2400d",
  "tool_use_result": {
    "query": "arxiv 2502.02664 differentiable composite neural signed distance fields robot navigation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H1F76PziCu4MZgomE3xbWS",
        "content": [
          {
            "title": "[2502.02664] Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments",
            "url": "https://arxiv.org/abs/2502.02664"
          },
          {
            "title": "Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments",
            "url": "https://arxiv.org/html/2502.02664"
          },
          {
            "title": "Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments - YouTube",
            "url": "https://www.youtube.com/watch?v=YI7LUMmFpS0"
          },
          {
            "title": "Differentiable Composite Neural Signed Distance Fields for Robot   Navigation in Dynamic Indoor Environments",
            "url": "https://arxiv.org/pdf/2502.02664"
          },
          {
            "title": "GitHub - stalhabukhari/comp-sdf-dyn-nav: Code for ICRA'25 paper: \"Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments\" · GitHub",
            "url": "https://github.com/stalhabukhari/comp-sdf-dyn-nav"
          },
          {
            "title": "RNBF: Real-Time RGB-D Based Neural Barrier Functions for Safe Robotic Navigation",
            "url": "https://arxiv.org/html/2505.02294v2"
          },
          {
            "title": "Neural Signed Distance Functions (SDFs)",
            "url": "https://www.emergentmind.com/topics/neural-signed-distance-functions-sdfs"
          }
        ]
      },
      "I found the paper you're searching for! Here's what I found:\n\narXiv:2502.02664 is titled \"Differentiable Composite Neural Signed Distance Fields for Robot Navigation in Dynamic Indoor Environments\", authored by S. Talha Bukhari, Daniel Lawson, and Ahmed H. Qureshi.\n\n**Key Contributions:**\n\nNeural Signed Distance Fields (SDFs) provide a differentiable environment representation to readily obtain collision checks and well-defined gradients for robot navigation tasks. However, updating neural SDFs as the scene evolves entails re-training, which is tedious, time consuming, and inefficient, making it unsuitable for robot navigation with limited field-of-view in dynamic environments.\n\nThe authors propose a compositional framework of neural SDFs to solve robot navigation in indoor environments using only an onboard RGB-D sensor. The framework embodies a dual mode procedure for trajectory optimization, with different modes using complementary methods of modeling collision costs and collision avoidance gradients.\n\n**Paper Details:**\n- Submitted on 4 Feb 2025, with the latest revision on 6 Mar 2025\n- This is an ICRA'25 paper with code available on GitHub\n\nYou can access the full paper at https://arxiv.org/abs/2502.02664"
    ],
    "durationSeconds": 9.425028385999997
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Good, I'm getting closer. Let me now search for a few more specific papers that could be relevant:

1. For collision-aware manipulation direction, I need papers that aren't already in the lit map. Let me look for:
   - The safe learning survey (2512.11908) - good survey paper
   - Collision-Inclusive Manipulation Planning (2412.06983)
   - Maybe some more specific work on collision avoidance in diffusion policies or VLA

2. For SDF in robotics:
   - Configuration Space Distance Fields (2406.01137) - RSS 2024, very relevant
   - Neural NMPC through SDF (2511.21312) - IJRR 2025
   - Differentiable Composite Neural SDF (2502.02664) - ICRA 2025

I should do a broader search to make sure I'm capturing the most relevant papers for these areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "5348f66e-d9dd-4f9a-a62e-a995db9049a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1i9uT9CdGJHBZunEVxqUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1506,
      "cache_creation_input_tokens": 2550,
      "cache_read_input_tokens": 36626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2550
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

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgSNhGHjg7aANFR2YxKzat`</summary>

```json
{
  "query": "arxiv 2412.06983 collision-inclusive manipulation planning occluded object grasping compliant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "0c3f96a9-21ee-499c-905c-d01866188f8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1i9uT9CdGJHBZunEVxqUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1506,
      "cache_creation_input_tokens": 2550,
      "cache_read_input_tokens": 36626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2550
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

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BnSgCa6kYNgz5hC4N7sXGh`</summary>

```json
{
  "query": "SDF collision avoidance robot arm manipulation training 2024 2025 differentiable distance field policy learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "7513608e-c4d0-40d8-8d43-e6c9923587f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1i9uT9CdGJHBZunEVxqUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1506,
      "cache_creation_input_tokens": 2550,
      "cache_read_input_tokens": 36626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2550
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JidAk8Vu2uMziGQWKsTwTZ`</summary>

```json
{
  "query": "\"collision-free\" \"diffusion policy\" robot manipulation 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "ef79fc02-5cb2-4622-8984-79ff56cf3d2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1i9uT9CdGJHBZunEVxqUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1506,
      "cache_creation_input_tokens": 2550,
      "cache_read_input_tokens": 36626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2550
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

_source line 38 · 2026-05-25T07:42:12.466Z_

<details><summary>↩ Tool result · `toolu_01BnSgCa6kYNgz5hC4N7sXGh`</summary>

```text
Web search results for query: "SDF collision avoidance robot arm manipulation training 2024 2025 differentiable distance field policy learning"

Links: [{"title":"Real-time collision avoidance with robot distance fields in a task-priority framework - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0921889026000679"},{"title":"CSSDF-Net: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field","url":"https://arxiv.org/pdf/2603.18669"},{"title":"Representing Robot Geometry as Distance Fields: Applications to   Whole-body Manipulation","url":"https://arxiv.org/pdf/2307.00533"},{"title":"\\textcolorblackRepresenting Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://arxiv.org/html/2307.00533v3"},{"title":"RMMI: Reactive Mobile Manipulation using an Implicit Neural Map","url":"https://arxiv.org/pdf/2408.16206"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://arxiv.org/pdf/2204.02296"},{"title":"Efficient Collision Detection Framework for Enhancing Collision-Free   Robot Motion","url":"https://arxiv.org/pdf/2409.14955"},{"title":"Representing Robot Geometry as Distance Fields:","url":"https://publications.idiap.ch/attachments/papers/2024/Li_ICRA-2_2024.pdf"},{"title":"RobotSDF: Implicit Morphology Modeling for the Robotic Arm - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11359239/"}]

I found several relevant research papers on using signed distance fields (SDFs) for robot arm collision avoidance and manipulation. Here are the key findings:

## Recent Work on SDFs for Robot Collision Avoidance

**Recent Publications (2024-2025):**

A recent framework embeds signed distance fields directly into control loops, with robot links represented using Bernstein polynomial-based distance fields that provide continuous geometry models and closed-form gradients for defining repulsive actions. These avoidance behaviors are executed in real time through GPU-accelerated implementation.

Another approach introduces a spatial-hashing-based data generation pipeline for zero-shot generalization, with the learned distance field integrated into safety-constrained trajectory optimization and receding-horizon MPC, enabling both offline planning and online reactive avoidance, demonstrated on planar arms and 7-DoF manipulators.

## Key Advantages of SDFs

A key advantage of SDFs lies in their differentiability, which ensures that their derivatives are continuous and smooth, enabling robust and reliable gradient-based control strategies.

Bernstein polynomials are used as basis functions to represent SDFs for each robot link, providing continuous and smooth distance representation with easy access to derivatives that are particularly well-suited for robot optimization problems such as motion planning and collision avoidance.

## Applications

Research demonstrates efficiency in dual-arm settings for tasks involving collision avoidance and whole-body manipulation.

These approaches leverage the differentiability of SDFs to enable gradient-based optimization for both control and policy learning in robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "493b3b44-df2e-49a8-8652-13c7e2b3cad4",
  "tool_use_result": {
    "query": "SDF collision avoidance robot arm manipulation training 2024 2025 differentiable distance field policy learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LxqF3a9ZdJRzwEF2AW56qP",
        "content": [
          {
            "title": "Real-time collision avoidance with robot distance fields in a task-priority framework - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0921889026000679"
          },
          {
            "title": "CSSDF-Net: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field",
            "url": "https://arxiv.org/pdf/2603.18669"
          },
          {
            "title": "Representing Robot Geometry as Distance Fields: Applications to   Whole-body Manipulation",
            "url": "https://arxiv.org/pdf/2307.00533"
          },
          {
            "title": "\\textcolorblackRepresenting Robot Geometry as Distance Fields: Applications to Whole-body Manipulation",
            "url": "https://arxiv.org/html/2307.00533v3"
          },
          {
            "title": "RMMI: Reactive Mobile Manipulation using an Implicit Neural Map",
            "url": "https://arxiv.org/pdf/2408.16206"
          },
          {
            "title": "iSDF: Real-Time Neural Signed Distance Fields for Robot Perception",
            "url": "https://arxiv.org/pdf/2204.02296"
          },
          {
            "title": "Efficient Collision Detection Framework for Enhancing Collision-Free   Robot Motion",
            "url": "https://arxiv.org/pdf/2409.14955"
          },
          {
            "title": "Representing Robot Geometry as Distance Fields:",
            "url": "https://publications.idiap.ch/attachments/papers/2024/Li_ICRA-2_2024.pdf"
          },
          {
            "title": "RobotSDF: Implicit Morphology Modeling for the Robotic Arm - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11359239/"
          }
        ]
      },
      "I found several relevant research papers on using signed distance fields (SDFs) for robot arm collision avoidance and manipulation. Here are the key findings:\n\n## Recent Work on SDFs for Robot Collision Avoidance\n\n**Recent Publications (2024-2025):**\n\nA recent framework embeds signed distance fields directly into control loops, with robot links represented using Bernstein polynomial-based distance fields that provide continuous geometry models and closed-form gradients for defining repulsive actions. These avoidance behaviors are executed in real time through GPU-accelerated implementation.\n\nAnother approach introduces a spatial-hashing-based data generation pipeline for zero-shot generalization, with the learned distance field integrated into safety-constrained trajectory optimization and receding-horizon MPC, enabling both offline planning and online reactive avoidance, demonstrated on planar arms and 7-DoF manipulators.\n\n## Key Advantages of SDFs\n\nA key advantage of SDFs lies in their differentiability, which ensures that their derivatives are continuous and smooth, enabling robust and reliable gradient-based control strategies.\n\nBernstein polynomials are used as basis functions to represent SDFs for each robot link, providing continuous and smooth distance representation with easy access to derivatives that are particularly well-suited for robot optimization problems such as motion planning and collision avoidance.\n\n## Applications\n\nResearch demonstrates efficiency in dual-arm settings for tasks involving collision avoidance and whole-body manipulation.\n\nThese approaches leverage the differentiability of SDFs to enable gradient-based optimization for both control and policy learning in robot manipulation tasks."
    ],
    "durationSeconds": 8.066870273000008
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-25T07:42:12.471Z_

<details><summary>↩ Tool result · `toolu_01JidAk8Vu2uMziGQWKsTwTZ`</summary>

```text
Web search results for query: ""collision-free" "diffusion policy" robot manipulation 2025 arxiv"

Links: [{"title":"[2407.00451] Language-Guided Object-Centric Diffusion Policy for Generalizable and Collision-Aware Robotic Manipulation","url":"https://arxiv.org/abs/2407.00451"},{"title":"Language-Guided Object-Centric Diffusion Policy for Generalizable and   Collision-Aware Robotic Manipulation","url":"https://arxiv.org/pdf/2407.00451"},{"title":"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance","url":"https://arxiv.org/pdf/2511.22773"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free   Generative Diffusion Models","url":"https://arxiv.org/pdf/2404.02284"}]

I found several relevant research papers on collision-free diffusion policies for robot manipulation. Here are the key results:

1. **Language-Guided Object-Centric Diffusion Policy (Lan-o3dp)** - This framework adapts to unseen situations such as cluttered scenes, shifting camera views, and ambiguous similar objects while offering training-free collision avoidance and achieving a high success rate with few demonstrations. During inference, cost optimization is incorporated into denoising steps to guide the generated trajectory to be collision-free. This paper was last revised in March 2025.

2. **CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion** - For collision avoidance, CAPE expands trajectory distribution modes with collision-aware context, enabling the sampling of collision-free trajectories in previously unseen environments while maintaining goal consistency. It demonstrates up to 26% and 80% higher success rates respectively compared to SOTA methods on diverse manipulation tasks in cluttered unseen simulated and real-world settings.

3. **APEX: Ambidextrous Dual-Arm Robotic Manipulation** - APEX introduces a collision-free latent diffusion model for both robotic motion planning and manipulation. It integrates obstacle information utilizing a classifier-guidance technique, thereby guaranteeing both the feasibility and safety of the generated manipulation trajectories.

These papers represent the current state-of-the-art work combining diffusion policies with collision avoidance for robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "04333af5-d326-40a3-b12f-bbe6716ea4d8",
  "tool_use_result": {
    "query": "\"collision-free\" \"diffusion policy\" robot manipulation 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WaKfumRXfX9KHP4gq87bxH",
        "content": [
          {
            "title": "[2407.00451] Language-Guided Object-Centric Diffusion Policy for Generalizable and Collision-Aware Robotic Manipulation",
            "url": "https://arxiv.org/abs/2407.00451"
          },
          {
            "title": "Language-Guided Object-Centric Diffusion Policy for Generalizable and   Collision-Aware Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2407.00451"
          },
          {
            "title": "CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance",
            "url": "https://arxiv.org/pdf/2511.22773"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free   Generative Diffusion Models",
            "url": "https://arxiv.org/pdf/2404.02284"
          }
        ]
      },
      "I found several relevant research papers on collision-free diffusion policies for robot manipulation. Here are the key results:\n\n1. **Language-Guided Object-Centric Diffusion Policy (Lan-o3dp)** - This framework adapts to unseen situations such as cluttered scenes, shifting camera views, and ambiguous similar objects while offering training-free collision avoidance and achieving a high success rate with few demonstrations. During inference, cost optimization is incorporated into denoising steps to guide the generated trajectory to be collision-free. This paper was last revised in March 2025.\n\n2. **CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion** - For collision avoidance, CAPE expands trajectory distribution modes with collision-aware context, enabling the sampling of collision-free trajectories in previously unseen environments while maintaining goal consistency. It demonstrates up to 26% and 80% higher success rates respectively compared to SOTA methods on diverse manipulation tasks in cluttered unseen simulated and real-world settings.\n\n3. **APEX: Ambidextrous Dual-Arm Robotic Manipulation** - APEX introduces a collision-free latent diffusion model for both robotic motion planning and manipulation. It integrates obstacle information utilizing a classifier-guidance technique, thereby guaranteeing both the feasibility and safety of the generated manipulation trajectories.\n\nThese papers represent the current state-of-the-art work combining diffusion policies with collision avoidance for robot manipulation tasks."
    ],
    "durationSeconds": 6.885269636000012
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T07:42:41.526Z_

<details><summary>↩ Tool result · `toolu_01FgSNhGHjg7aANFR2YxKzat`</summary>

```text
Web search results for query: "arxiv 2412.06983 collision-inclusive manipulation planning occluded object grasping compliant"

Links: [{"title":"[2412.06983] Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions","url":"https://arxiv.org/abs/2412.06983"},{"title":"Collision-inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions | Rice RobotΠ Lab","url":"https://robotpilab.github.io/publication/collision-inclusive-manipulation/"},{"title":"Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions","url":"https://arxiv.org/pdf/2412.06983"},{"title":"Collision-inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions","url":"https://arxiv.org/html/2412.06983v1"},{"title":"Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11091413/"},{"title":"COMBO-Grasp: Learning Constraint-Based Manipulation for Bimanual   Occluded Grasping","url":"https://arxiv.org/pdf/2502.08054"}]

Based on the search results, I found the paper you're looking for:

**Title:** Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions

**Authors:** Kejia Ren, Gaotian Wang, Andrew S. Morgan, and Kaiyu Hang

**Summary:** The paper proposes a collision-inclusive planning framework that can transition the robot to a desired task configuration via roughly modeled collisions absorbed by Cartesian impedance control. By strategically exploiting the environmental constraints and exploring inside a manipulation funnel formed by task repetitions, the framework can effectively reduce physical and perception uncertainties.

**Key Innovation:** Due to occlusions by surrounding objects, a feasible grasp configuration for the target object does not initially exist, and thus the robot has to collide with surrounding objects for a successful grasp.

**Results:** With real-world evaluations on both single-arm and dual-arm setups, the framework is able to efficiently address various realistic occluded grasping problems where a feasible grasp does not initially exist.

The paper is available on arXiv at https://arxiv.org/abs/2412.06983


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "39698aa6-058a-48ef-968d-01de8d43a860",
  "tool_use_result": {
    "query": "arxiv 2412.06983 collision-inclusive manipulation planning occluded object grasping compliant",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PsP7TWbC4xiaB8kNwYBpFe",
        "content": [
          {
            "title": "[2412.06983] Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions",
            "url": "https://arxiv.org/abs/2412.06983"
          },
          {
            "title": "Collision-inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions | Rice RobotΠ Lab",
            "url": "https://robotpilab.github.io/publication/collision-inclusive-manipulation/"
          },
          {
            "title": "Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions",
            "url": "https://arxiv.org/pdf/2412.06983"
          },
          {
            "title": "Collision-inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions",
            "url": "https://arxiv.org/html/2412.06983v1"
          },
          {
            "title": "Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/11091413/"
          },
          {
            "title": "COMBO-Grasp: Learning Constraint-Based Manipulation for Bimanual   Occluded Grasping",
            "url": "https://arxiv.org/pdf/2502.08054"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions\n\n**Authors:** Kejia Ren, Gaotian Wang, Andrew S. Morgan, and Kaiyu Hang\n\n**Summary:** The paper proposes a collision-inclusive planning framework that can transition the robot to a desired task configuration via roughly modeled collisions absorbed by Cartesian impedance control. By strategically exploiting the environmental constraints and exploring inside a manipulation funnel formed by task repetitions, the framework can effectively reduce physical and perception uncertainties.\n\n**Key Innovation:** Due to occlusions by surrounding objects, a feasible grasp configuration for the target object does not initially exist, and thus the robot has to collide with surrounding objects for a successful grasp.\n\n**Results:** With real-world evaluations on both single-arm and dual-arm setups, the framework is able to efficiently address various realistic occluded grasping problems where a feasible grasp does not initially exist.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2412.06983"
    ],
    "durationSeconds": 37.56337672500001
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Let me also look for a few more papers:
1. APEX (2404.02284) - dual-arm collision-free diffusion - this is new and relevant
2. The real-time collision avoidance with robot distance fields paper 
3. CSSDF-Net (2603.18669) - safe motion planning based on neural implicit C-space distance field

Let me get more details on these.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "d4404d69-1150-4767-8e3a-7a5ce650d677",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKBRqTEYjorpMj8gWzL7Sx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1481,
      "cache_creation_input_tokens": 2590,
      "cache_read_input_tokens": 39176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2590
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_012rot2NKRWnAynsq5WcMoW5`</summary>

```json
{
  "query": "arxiv 2404.02284 APEX ambidextrous dual-arm diffusion collision-free manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "5a2d50cd-38db-4884-9f3c-e9ca08f7e7ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKBRqTEYjorpMj8gWzL7Sx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1481,
      "cache_creation_input_tokens": 2590,
      "cache_read_input_tokens": 39176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2590
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXVV3LqZozs7KNyrcHQF2D`</summary>

```json
{
  "query": "\"robot distance field\" real-time collision avoidance task-priority 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "b32041be-e2ae-49ae-977a-189e2bacaaa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKBRqTEYjorpMj8gWzL7Sx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1481,
      "cache_creation_input_tokens": 2590,
      "cache_read_input_tokens": 39176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2590
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

_source line 44 · 2026-05-25T07:42:56.916Z_

<details><summary>↩ Tool result · `toolu_01VXVV3LqZozs7KNyrcHQF2D`</summary>

```text
Web search results for query: ""robot distance field" real-time collision avoidance task-priority 2025 2026"

Links: [{"title":"Real-time collision avoidance with robot distance fields in a task-priority framework - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0921889026000679"},{"title":"Real Time Collision Avoidance with GPU-Computed Distance Maps","url":"https://arxiv.org/pdf/2407.02363"},{"title":"Real Time Collision Avoidance with GPU-Computed Distance Maps","url":"https://arxiv.org/html/2407.02363"},{"title":"Real-time obstacle avoidance for manipulators and mobile robots | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/1087247/"},{"title":"A real-time collision avoidance method for redundant dual-arm robots in an open operational environment - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0736584524001819"},{"title":"Whole-body Dynamic Collision Avoidance with Time-varying Control Barrier   Functions","url":"https://arxiv.org/pdf/2311.18212"}]

Based on the search results, here's what I found:

## Key Research on Robot Distance Fields and Real-Time Collision Avoidance

Safe and efficient collision avoidance is essential for robots operating in dynamic and cluttered environments.

Recent research in this area includes:

1. **Task-Priority Framework with Distance Fields (2026)**: A task-priority control framework addresses safe and efficient collision avoidance for robots in dynamic and cluttered environments. This appears to be a recent publication from February 2026 directly matching your search query topic.

2. **GPU-Computed Distance Maps**: A framework utilizes discretized representation of the robot and the environment to calculate 3D Euclidean distance transform for task-priority based kinematic control. This approach was evaluated using the Tiago robot, showing that obstacle and self-collision avoidance constraints are respected within one framework even with fast moving obstacles while the robot performs end-effector pose tracking in real time.

3. **Dynamic Collision Avoidance with Signed Distance Fields**: Research also explores "Robo-centric Euclidean Signed Distance Field" approaches for whole-body dynamic collision avoidance, which represents an alternative method in this research area.

The search results indicate active research in real-time collision avoidance using distance field methods within task-priority control frameworks for robotic systems in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "80a16305-c38e-4a85-b852-bb913a4f3796",
  "tool_use_result": {
    "query": "\"robot distance field\" real-time collision avoidance task-priority 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G9JMYRvoVmFoJNvcvzzZmE",
        "content": [
          {
            "title": "Real-time collision avoidance with robot distance fields in a task-priority framework - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0921889026000679"
          },
          {
            "title": "Real Time Collision Avoidance with GPU-Computed Distance Maps",
            "url": "https://arxiv.org/pdf/2407.02363"
          },
          {
            "title": "Real Time Collision Avoidance with GPU-Computed Distance Maps",
            "url": "https://arxiv.org/html/2407.02363"
          },
          {
            "title": "Real-time obstacle avoidance for manipulators and mobile robots | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/1087247/"
          },
          {
            "title": "A real-time collision avoidance method for redundant dual-arm robots in an open operational environment - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0736584524001819"
          },
          {
            "title": "Whole-body Dynamic Collision Avoidance with Time-varying Control Barrier   Functions",
            "url": "https://arxiv.org/pdf/2311.18212"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## Key Research on Robot Distance Fields and Real-Time Collision Avoidance\n\nSafe and efficient collision avoidance is essential for robots operating in dynamic and cluttered environments.\n\nRecent research in this area includes:\n\n1. **Task-Priority Framework with Distance Fields (2026)**: A task-priority control framework addresses safe and efficient collision avoidance for robots in dynamic and cluttered environments. This appears to be a recent publication from February 2026 directly matching your search query topic.\n\n2. **GPU-Computed Distance Maps**: A framework utilizes discretized representation of the robot and the environment to calculate 3D Euclidean distance transform for task-priority based kinematic control. This approach was evaluated using the Tiago robot, showing that obstacle and self-collision avoidance constraints are respected within one framework even with fast moving obstacles while the robot performs end-effector pose tracking in real time.\n\n3. **Dynamic Collision Avoidance with Signed Distance Fields**: Research also explores \"Robo-centric Euclidean Signed Distance Field\" approaches for whole-body dynamic collision avoidance, which represents an alternative method in this research area.\n\nThe search results indicate active research in real-time collision avoidance using distance field methods within task-priority control frameworks for robotic systems in 2025-2026."
    ],
    "durationSeconds": 7.883683594000002
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T07:43:04.695Z_

<details><summary>↩ Tool result · `toolu_012rot2NKRWnAynsq5WcMoW5`</summary>

```text
Web search results for query: "arxiv 2404.02284 APEX ambidextrous dual-arm diffusion collision-free manipulation"

Links: [{"title":"[2404.02284] APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models","url":"https://arxiv.org/abs/2404.02284"},{"title":"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models","url":"https://arxiv.org/html/2404.02284v1"},{"title":"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10802655/"},{"title":"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free   Generative Diffusion Models","url":"https://arxiv.org/pdf/2404.02284"},{"title":"APEX","url":"https://sites.google.com/view/apex-dual-arm/home"},{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/html/2601.21712v1"},{"title":"Reactive collision-free motion generation for tightly coupled coordinated bimanual manipulation | ENGINEERING Mechanical Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11465-026-0873-7"}]

I found the research paper you're looking for. Here's what the search revealed:

The paper is titled "APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models" by Apan Dastider, Hao Fang, and Mingjie Lin.

**Key contributions:**

The paper proposes APEX, a collision-free latent diffusion model for both robotic motion planning and manipulation. It simplifies the complexity of real-life ambidextrous dual-arm robotic manipulation tasks by abstracting them as aligning two vectors.

The approach uses latent diffusion models to produce a variety of robotic manipulation trajectories and integrates obstacle information using a classifier-guidance technique to guarantee feasibility and safety.

**Validation:**

The algorithm was validated through extensive experiments on ambidextrous dual-arm robot hardware platforms, consistently generating successful and seamless trajectories across diverse tasks and surpassing conventional robotic motion planning algorithms.

The paper was submitted to arXiv on April 2, 2024, and was later published at the 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "3398bf36-74e7-4bc6-85e1-c8027f4c2171",
  "tool_use_result": {
    "query": "arxiv 2404.02284 APEX ambidextrous dual-arm diffusion collision-free manipulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EYU8BQSRRF287FQLgxPwJJ",
        "content": [
          {
            "title": "[2404.02284] APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models",
            "url": "https://arxiv.org/abs/2404.02284"
          },
          {
            "title": "APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models",
            "url": "https://arxiv.org/html/2404.02284v1"
          },
          {
            "title": "APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10802655/"
          },
          {
            "title": "APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free   Generative Diffusion Models",
            "url": "https://arxiv.org/pdf/2404.02284"
          },
          {
            "title": "APEX",
            "url": "https://sites.google.com/view/apex-dual-arm/home"
          },
          {
            "title": "CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation",
            "url": "https://arxiv.org/html/2601.21712v1"
          },
          {
            "title": "Reactive collision-free motion generation for tightly coupled coordinated bimanual manipulation | ENGINEERING Mechanical Engineering | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11465-026-0873-7"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what the search revealed:\n\nThe paper is titled \"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\" by Apan Dastider, Hao Fang, and Mingjie Lin.\n\n**Key contributions:**\n\nThe paper proposes APEX, a collision-free latent diffusion model for both robotic motion planning and manipulation. It simplifies the complexity of real-life ambidextrous dual-arm robotic manipulation tasks by abstracting them as aligning two vectors.\n\nThe approach uses latent diffusion models to produce a variety of robotic manipulation trajectories and integrates obstacle information using a classifier-guidance technique to guarantee feasibility and safety.\n\n**Validation:**\n\nThe algorithm was validated through extensive experiments on ambidextrous dual-arm robot hardware platforms, consistently generating successful and seamless trajectories across diverse tasks and surpassing conventional robotic motion planning algorithms.\n\nThe paper was submitted to arXiv on April 2, 2024, and was later published at the 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)."
    ],
    "durationSeconds": 16.240177976000005
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
I noticed an interesting paper: **CoFreeVLA** (2601.21712) - "Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation" - this is directly relevant! It's a VLA + collision-free approach. Let me search for it.

And I also spotted the GPU-Computed Distance Maps paper (2407.02363), which could be relevant for SDF direction.

Let me search for CoFreeVLA and a couple more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "85595e2b-7975-4309-9e65-5f12a24a099d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016z7dQpHSoQQB9PduZP5aQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 2543,
      "cache_read_input_tokens": 41766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2543
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

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XnFqtrJnN8DXt1LffuQTUn`</summary>

```json
{
  "query": "arxiv 2601.21712 CoFreeVLA collision-free dual-arm VLA risk estimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "0f7f1efc-4a69-4fef-b542-3f6d639c75f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016z7dQpHSoQQB9PduZP5aQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 2543,
      "cache_read_input_tokens": 41766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2543
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UWyo6YbqYhNXznQ3UKhvQd`</summary>

```json
{
  "query": "arxiv 2409.14955 efficient collision detection framework collision-free robot motion SDF 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "1635b0ba-cec7-44a9-aeff-53390f076e5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016z7dQpHSoQQB9PduZP5aQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 665,
      "cache_creation_input_tokens": 2543,
      "cache_read_input_tokens": 41766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2543
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

_source line 49 · 2026-05-25T07:43:18.856Z_

<details><summary>↩ Tool result · `toolu_01XnFqtrJnN8DXt1LffuQTUn`</summary>

```text
Web search results for query: "arxiv 2601.21712 CoFreeVLA collision-free dual-arm VLA risk estimation"

Links: [{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/html/2601.21712v1"},{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/pdf/2601.21712"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=2552&show=1000"},{"title":"(PDF) FCL: A General Purpose Library for Collision and Proximity Queries","url":"https://www.researchgate.net/publication/247161844_FCL_A_General_Purpose_Library_for_Collision_and_Proximity_Queries"},{"title":"Collision-Free control system for a multi-axially controllable manipulator","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5549439"}]

I found the paper you're looking for! Here's what I can tell you about it:

**CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation**

CoFreeVLA augments an end-to-end Vision-Language-Action (VLA) model with a short-horizon self-collision risk estimator that predicts collision likelihood from proprioception, visual embeddings, and planned actions. 

At the core of CoFreeVLA is a self-collision risk estimator that predicts the likelihood of future collisions given the current observation and planned actions from the VLA policy. The estimator gates risky commands, recovers to safe states via risk-guided adjustments, and shapes policy refinement for safer rollouts.

It is pre-trained with model-based collision labels and post-trained on real-robot rollouts for calibration. On five bimanual tasks with the PiPER robot arm, CoFreeVLA reduces self-collisions and improves success rates versus RDT and APEX.

The paper is authored by Xuanran Zhai, Binkai Ou, Qiaojun Yu, Ce Hao, and Yaohua Liu, and was posted on arXiv on January 29, 2026. You can access it at https://arxiv.org/html/2601.21712v1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "27053617-303b-40ff-846d-04eadc6e7022",
  "tool_use_result": {
    "query": "arxiv 2601.21712 CoFreeVLA collision-free dual-arm VLA risk estimation",
    "results": [
      {
        "tool_use_id": "srvtoolu_014j1F6Pq4EkyGf3EeiK9vG1",
        "content": [
          {
            "title": "CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation",
            "url": "https://arxiv.org/html/2601.21712v1"
          },
          {
            "title": "CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation",
            "url": "https://arxiv.org/pdf/2601.21712"
          },
          {
            "title": "Computer Science",
            "url": "https://www.arxiv.org/list/cs/recent?skip=2552&show=1000"
          },
          {
            "title": "(PDF) FCL: A General Purpose Library for Collision and Proximity Queries",
            "url": "https://www.researchgate.net/publication/247161844_FCL_A_General_Purpose_Library_for_Collision_and_Proximity_Queries"
          },
          {
            "title": "Collision-Free control system for a multi-axially controllable manipulator",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5549439"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I can tell you about it:\n\n**CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation**\n\nCoFreeVLA augments an end-to-end Vision-Language-Action (VLA) model with a short-horizon self-collision risk estimator that predicts collision likelihood from proprioception, visual embeddings, and planned actions. \n\nAt the core of CoFreeVLA is a self-collision risk estimator that predicts the likelihood of future collisions given the current observation and planned actions from the VLA policy. The estimator gates risky commands, recovers to safe states via risk-guided adjustments, and shapes policy refinement for safer rollouts.\n\nIt is pre-trained with model-based collision labels and post-trained on real-robot rollouts for calibration. On five bimanual tasks with the PiPER robot arm, CoFreeVLA reduces self-collisions and improves success rates versus RDT and APEX.\n\nThe paper is authored by Xuanran Zhai, Binkai Ou, Qiaojun Yu, Ce Hao, and Yaohua Liu, and was posted on arXiv on January 29, 2026. You can access it at https://arxiv.org/html/2601.21712v1."
    ],
    "durationSeconds": 7.719358122000005
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T07:43:19.671Z_

<details><summary>↩ Tool result · `toolu_01UWyo6YbqYhNXznQ3UKhvQd`</summary>

```text
Web search results for query: "arxiv 2409.14955 efficient collision detection framework collision-free robot motion SDF 2024"

Links: [{"title":"[2409.14955] Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion","url":"https://arxiv.org/abs/2409.14955"},{"title":"[2404.14955] A Comprehensive Survey for Hyperspectral Image Classification: The Evolution from Conventional to Transformers and Mamba Models","url":"https://arxiv.org/abs/2404.14955"},{"title":"Upregulation of ARHGAP9 is correlated with poor prognosis and immune infiltration in clear cell renal cell carcinoma","url":"https://www.medrxiv.org/content/10.1101/2023.08.31.23294890.full.pdf"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"LeafyResNet: Fusarium Wilt Detection in Lettuce Using UAV RGB Imaging and Advanced Deep Learning Model","url":"https://www.biorxiv.org/content/10.1101/2025.05.21.655416.full.pdf"}]

Based on the search results, I found the paper you're looking for:

**Title:** Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion

**ArXiv ID:** 2409.14955

**Publication Date:** September 23, 2024

**Key Content:**

The paper proposes an efficient collision detection framework based on the Signed Distance Field (SDF) of robots, seamlessly integrated with a self-collision detection module. 

The approach decomposes the robot's SDF using forward kinematics and leverages multiple extremely lightweight networks in parallel to efficiently approximate the SDF. 

Support vector machines are introduced to integrate the self-collision detection module into the framework, which is referred to as the SDF-SC framework.

The framework maintains and utilizes differentiable properties to optimize collision-free robot trajectories.

The paper is available on arXiv at: https://arxiv.org/abs/2409.14955


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "807d5e13-67d9-46d5-84d4-6493374f1b34",
  "tool_use_result": {
    "query": "arxiv 2409.14955 efficient collision detection framework collision-free robot motion SDF 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WQVcUi5rT7Nd6KVD7XNwLk",
        "content": [
          {
            "title": "[2409.14955] Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion",
            "url": "https://arxiv.org/abs/2409.14955"
          },
          {
            "title": "[2404.14955] A Comprehensive Survey for Hyperspectral Image Classification: The Evolution from Conventional to Transformers and Mamba Models",
            "url": "https://arxiv.org/abs/2404.14955"
          },
          {
            "title": "Upregulation of ARHGAP9 is correlated with poor prognosis and immune infiltration in clear cell renal cell carcinoma",
            "url": "https://www.medrxiv.org/content/10.1101/2023.08.31.23294890.full.pdf"
          },
          {
            "title": "Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models",
            "url": "https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"
          },
          {
            "title": "LeafyResNet: Fusarium Wilt Detection in Lettuce Using UAV RGB Imaging and Advanced Deep Learning Model",
            "url": "https://www.biorxiv.org/content/10.1101/2025.05.21.655416.full.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\n\n**ArXiv ID:** 2409.14955\n\n**Publication Date:** September 23, 2024\n\n**Key Content:**\n\nThe paper proposes an efficient collision detection framework based on the Signed Distance Field (SDF) of robots, seamlessly integrated with a self-collision detection module. \n\nThe approach decomposes the robot's SDF using forward kinematics and leverages multiple extremely lightweight networks in parallel to efficiently approximate the SDF. \n\nSupport vector machines are introduced to integrate the self-collision detection module into the framework, which is referred to as the SDF-SC framework.\n\nThe framework maintains and utilizes differentiable properties to optimize collision-free robot trajectories.\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2409.14955"
    ],
    "durationSeconds": 7.433968145000021
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compile the literature additions. Let me select the best papers for each direction:

**Direction 1: Collision-aware manipulation (2-3 papers to add)**

Already covered: VLSA, SafeVLA, Lan-o3dp, CAPE, iKinQP-RL

Good candidates:
1. **CoFreeVLA** (2601.21712, 2026) - Collision-Free Dual-Arm Manipulation via VLA + Risk Estimation. Directly relevant as it's a VLA + collision avoidance approach, predicts collision risk from proprioception and visual embeddings. 

2. **APEX** (2404.02284, IROS 2024) - Collision-free diffusion model for dual-arm that uses classifier-guidance for collision avoidance in latent diffusion space, offering another test-time collision avoidance method worth comparing.

3. **Safe Learning Survey** (2512.11908, 2025) - Comprehensive survey bridging classical safe learning to foundation models, providing good context for the broader field.

**Direction 2: SDF in robotics (2-3 papers to add)**

Already covered: VoxPoser, DeepSDF, Liu et al. (robot geometry as distance fields), iSDF, RAMP, DiffCo

Good candidates:
1. **

Configuration Space Distance Fields** (2406.01137, RSS 2024) - Extends SDF from task space to C-space for manipulation planning, directly addressing the end-effector-only limitation.
2. **SDF-SC: Efficient Collision Detection** (2409.14955, 2024) - Decomposes robot SDF via forward kinematics with lightweight parallel networks for differentiable collision checking.
3. **Neural NMPC through SDF** (2511.21312, IJRR 2025) - Demonstrates SDF as a constraint in optimization-based control through neural SDF encoding for collision avoidance.

Now I'm preparing the literature_map.yaml update and double-checking whether the paper aligns with these directions. I should also reconsider CoFreeVLA's relevance here.

Updating the literature map with two main directions: collision-aware manipulation approaches including CoFreeVLA, APEX, and a safe learning survey; plus the SDF-focused papers that show how distance fields can be applied across different robotics problems. Let me save these additions to the project file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "37047f7e-ad95-46ff-90f6-a8c49bcfd9f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxrKMf3cCs7aAWprDfpFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 44309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2166
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

_source line 52_

搜索完成，确定了每个方向各 3 篇补充论文。现在写入 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "0fd32dbd-c558-43fb-8394-e766279160a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxrKMf3cCs7aAWprDfpFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 44309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2166
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

_source line 53_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NhSwmA14KuqXW3cQmn75EX`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "44252814-486f-4cc3-b2c9-29a674e2b072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxrKMf3cCs7aAWprDfpFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 44309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2166
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

_source line 54 · 2026-05-25T07:43:41.289Z_

<details><summary>↩ Tool result · `toolu_01NhSwmA14KuqXW3cQmn75EX`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "6f6ac223-7b84-4711-9889-c50d732a00f1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool has a whitelist: memory.md, writing_plan.yaml, paper_framing.md. literature_map.yaml is NOT in the whitelist. So I can't use save_project_file to write literature_map.yaml directly.

Let me write it directly to the file path instead using the Write tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "e7791d1d-cb8b-411c-9e4c-4fec505f67da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XLA8BG8uHzDHizLFKkSB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 46475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1188
      },
      "output_tokens": 38,
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

_source line 56_

`save_project_file` 白名单不含 literature_map.yaml，直接写文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "54ecd243-b5a9-4800-9094-68eb0c822671",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XLA8BG8uHzDHizLFKkSB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 46475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1188
      },
      "output_tokens": 38,
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

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01Urc2ZW42EppYs9udMi3GzS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "7a748af1-5d63-4d89-98f2-264f1848a376",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XLA8BG8uHzDHizLFKkSB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 46475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1188
      },
      "output_tokens": 38,
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

_source line 58 · 2026-05-25T07:43:55.652Z_

<details><summary>↩ Tool result · `toolu_01Urc2ZW42EppYs9udMi3GzS`</summary>

```text
1	# ColliForce-VLA Literature Map
2	# Updated: 2026-05-20
3	
4	papers:
5	
6	  # ===== 已有论文 =====
7	
8	  - paper_id: "2512.11891"
9	    title: "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer"
10	    authors: "Hu et al."
11	    year: 2025
12	    venue: arXiv
13	    role: direct-competitor
14	    category: collision-aware-vla
15	    one_line_summary: "AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。"
16	
17	  - paper_id: "2510.14836"
18	    title: "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models"
19	    authors: "Li et al."
20	    year: 2025
21	    venue: arXiv
22	    role: direct-competitor
23	    category: spatial-aware-vla
24	    one_line_summary: "用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。"
25	
26	  - paper_id: "2510.12276"
27	    title: "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model"
28	    authors: "Li et al."
29	    year: 2025
30	    venue: ICLR 2026
31	    role: method-component
32	    category: spatial-aware-vla
33	    one_line_summary: "隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。"
34	
35	  - paper_id: "2307.05973"
36	    title: "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models"
37	    authors: "Huang et al."
38	    year: 2023
39	    venue: CoRL 2023
40	    role: method-component
41	    category: sdf-robotics
42	    one_line_summary: "用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。"
43	
44	  - paper_id: "2410.24164"
45	    title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
46	    authors: "Black et al., Physical Intelligence"
47	    year: 2024
48	    venue: arXiv
49	    role: backbone
50	    category: vla-foundation
51	    one_line_summary: "基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。"
52	
53	  - paper_id: "1901.05103"
54	    title: "DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation"
55	    authors: "Park et al."
56	    year: 2019
57	    venue: CVPR 2019
58	    role: method-component
59	    category: sdf-representation
60	    one_line_summary: "开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。"
61	
62	  - paper_id: "2307.00533"
63	    title: "Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation"
64	    authors: "Liu et al."
65	    year: 2023
66	    venue: arXiv
67	    role: method-component
68	    category: sdf-robotics
69	    one_line_summary: "用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。"
70	
71	  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====
72	
73	  - paper_id: "2503.03480"
74	    title: "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning"
75	    authors: "Zhang et al."
76	    year: 2025
77	    venue: NeurIPS 2025 (Spotlight)
78	    arxiv: "2503.03480"
79	    role: direct-competitor
80	    category: collision-aware-vla
81	    summary: "用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。"
82	    relevance: "最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。"
83	
84	  - paper_id: "2407.00451"
85	    title: "Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation"
86	    authors: "Li et al."
87	    year: 2024
88	    venue: ICRA 2025
89	    arxiv: "2407.00451"
90	    role: direct-competitor
91	    category: collision-aware-vla
92	    summary: "在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。"
93	    relevance: "碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。"
94	
95	  - paper_id: "2511.22773"
96	    title: "CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance"
97	    authors: "Yang et al."
98	    year: 2025
99	    venue: arXiv
100	    arxiv: "2511.22773"
101	    role: direct-competitor
102	    category: collision-aware-vla
103	    summary: "通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。"
104	    relevance: "推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。"
105	
106	  - paper_id: "2409.08233"
107	    title: "Towards Online Safety Corrections for Robotic Manipulation Policies"
108	    authors: "Spalter et al."
109	    year: 2024
110	    venue: arXiv
111	    arxiv: "2409.08233"
112	    role: direct-competitor
113	    category: collision-aware-vla
114	    summary: "iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。"
115	    relevance: "运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。"
116	
117	  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====
118	
119	  - paper_id: "2204.02296"
120	    title: "iSDF: Real-Time Neural Signed Distance Fields for Robot Perception"
121	    authors: "Ortiz et al."
122	    year: 2022
123	    venue: RSS 2022
124	    arxiv: "2204.02296"
125	    role: method-component
126	    category: sdf-robotics
127	    summary: "从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。"
128	    relevance: "验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。"
129	
130	  - paper_id: "2305.10534"
131	    title: "RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions"
132	    authors: "Vasilopoulos et al."
133	    year: 2023
134	    venue: IROS 2023
135	    arxiv: "2305.10534"
136	    role: method-component
137	    category: sdf-robotics
138	    summary: "结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。"
139	    relevance: "展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。"
140	
141	  - paper_id: "2102.07413"
142	    title: "DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization"
143	    authors: "Zhi et al."
144	    year: 2021
145	    venue: IEEE T-RO
146	    arxiv: "2102.07413"
147	    role: method-component
148	    category: sdf-robotics
149	    summary: "全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。"
150	    relevance: "可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。"
151	
152	  # ===== 新增 P2: VLA 基座模型系列 =====
153	
154	  - paper_id: "2307.15818"
155	    title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
156	    authors: "Brohan et al., Google DeepMind"
157	    year: 2023
158	    venue: arXiv
159	    arxiv: "2307.15818"
160	    role: foundational
161	    category: vla-foundation
162	    summary: "将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。"
163	    relevance: "VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。"
164	
165	  - paper_id: "2406.09246"
166	    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
167	    authors: "Kim et al."
168	    year: 2024
169	    venue: arXiv
170	    arxiv: "2406.09246"
171	    role: benchmark-source
172	    category: vla-foundation
173	    summary: "7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。"
174	    relevance: "主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。"
175	
176	  - paper_id: "2405.12213"
177	    title: "Octo: An Open-Source Generalist Robot Policy"
178	    authors: "Octo Model Team"
179	    year: 2024
180	    venue: arXiv
181	    arxiv: "2405.12213"
182	    role: benchmark-source
183	    category: vla-foundation
184	    summary: "基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。"
185	    relevance: "轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。"
186	
187	  # ===== 新增 P3: Benchmark =====
188	
189	  - title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
190	    authors: "Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone"
191	    venue: "NeurIPS 2023"
192	    arxiv: "2306.03310"
193	    role: benchmark
194	    relevance: "SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议"
195	
196	  # ===== 新增 P4: 生成式建模基础方法 =====
197	
198	  - title: "Flow Matching for Generative Modeling"
199	    authors: "Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le"
200	    venue: "ICLR 2023"
201	    arxiv: "2210.02747"
202	    role: method-component
203	    relevance: "π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入"
204	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "8d42c0e2-61f4-48b8-9047-b787f874c59d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
      "content": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-20\n\npapers:\n\n  # ===== 已有论文 =====\n\n  - paper_id: \"2512.11891\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\"\n\n  - paper_id: \"2510.14836\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: spatial-aware-vla\n    one_line_summary: \"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\"\n\n  - paper_id: \"2510.12276\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICLR 2026\n    role: method-component\n    category: spatial-aware-vla\n    one_line_summary: \"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\"\n\n  - paper_id: \"2307.05973\"\n    title: \"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: CoRL 2023\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\"\n\n  - paper_id: \"2410.24164\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al., Physical Intelligence\"\n    year: 2024\n    venue: arXiv\n    role: backbone\n    category: vla-foundation\n    one_line_summary: \"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\"\n\n  - paper_id: \"1901.05103\"\n    title: \"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\"\n    authors: \"Park et al.\"\n    year: 2019\n    venue: CVPR 2019\n    role: method-component\n    category: sdf-representation\n    one_line_summary: \"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\"\n\n  - paper_id: \"2307.00533\"\n    title: \"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: arXiv\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\"\n\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\n\n  - paper_id: \"2503.03480\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    arxiv: \"2503.03480\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\"\n    relevance: \"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\"\n\n  - paper_id: \"2407.00451\"\n    title: \"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: ICRA 2025\n    arxiv: \"2407.00451\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\"\n    relevance: \"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\"\n\n  - paper_id: \"2511.22773\"\n    title: \"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\"\n    authors: \"Yang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2511.22773\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\"\n    relevance: \"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\"\n\n  - paper_id: \"2409.08233\"\n    title: \"Towards Online Safety Corrections for Robotic Manipulation Policies\"\n    authors: \"Spalter et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.08233\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"\n    relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\n\n  - paper_id: \"2204.02296\"\n    title: \"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\"\n    authors: \"Ortiz et al.\"\n    year: 2022\n    venue: RSS 2022\n    arxiv: \"2204.02296\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\"\n    relevance: \"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\"\n\n  - paper_id: \"2305.10534\"\n    title: \"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\"\n    authors: \"Vasilopoulos et al.\"\n    year: 2023\n    venue: IROS 2023\n    arxiv: \"2305.10534\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\"\n    relevance: \"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\"\n\n  - paper_id: \"2102.07413\"\n    title: \"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\"\n    authors: \"Zhi et al.\"\n    year: 2021\n    venue: IEEE T-RO\n    arxiv: \"2102.07413\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"\n    relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====\n\n  - paper_id: \"2307.15818\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al., Google DeepMind\"\n    year: 2023\n    venue: arXiv\n    arxiv: \"2307.15818\"\n    role: foundational\n    category: vla-foundation\n    summary: \"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\"\n    relevance: \"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\"\n\n  - paper_id: \"2406.09246\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2406.09246\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\"\n    relevance: \"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\"\n\n  - paper_id: \"2405.12213\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2405.12213\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"\n    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n\n  # ===== 新增 P3: Benchmark =====\n\n  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2306.03310\"\n    role: benchmark\n    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"\n\n  # ===== 新增 P4: 生成式建模基础方法 =====\n\n  - title: \"Flow Matching for Generative Modeling\"\n    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.02747\"\n    role: method-component\n    relevance: \"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\"\n",
      "numLines": 204,
      "startLine": 1,
      "totalLines": 204
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now let me prepare the updated file. I'll add 6 new papers (3 per direction) at the end of the relevant sections.

**Direction 1: Collision-aware manipulation — 3 new papers:**

1. **CoFreeVLA** (2601.21712, 2026) - VLA + collision risk estimator for dual-arm
   - Authors: Zhai et al.
   - Very relevant: another VLA-based approach to collision-free manipulation, uses risk estimation to gate risky commands
   - Contrast: external risk estimator (post-hoc filtering) vs ColliForce's training-time SDF embedding
   
2. **APEX** (2404.02284, IROS 2024) - Collision-free latent diffusion for dual-arm
   - Authors: Dastider et al.
   - Uses classifier-guidance to integrate obstacle info into diffusion denoising
   - Contrast: test-time guidance approach, similar to Lan-o3dp/CAPE

3. **Safe Learning for Contact-Rich Tasks Survey** (2512.11908, 2025) - Comprehensive survey
   - Authors: Zhang et al.
   - Covers safe exploration + safe execution, from classical methods to foundation models
   - Good survey reference for Related Work

**Direction 2: SDF in robot...

** Now looking at three more papers on SDF-based approaches. Configuration Space Distance Fields extends SDF beyond task space to directly estimate minimum joint motion for contact-aware manipulation, which directly addresses ColliForce's limitation of only handling end-effector constraints. There's also work on decomposing robot SDFs through forward kinematics with lightweight parallel networks that includes self-collision detection, offering a whole-body alternative to ColliForce's end-effector-only approach. And a recent Neural NMPC method leveraging SDF for control.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "5c580cf7-0ce6-4fb3-886c-cef1b2d30aba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCNaFXb2t9dxAgZediL8Uf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4339,
      "cache_read_input_tokens": 47663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4339
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — Edit · `toolu_019kSqCDGT93T67WXK5dSgc1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
  "old_string": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-20",
  "new_string": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "55cdf9c3-79fb-4c7c-a640-fb4fafd9e959",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCNaFXb2t9dxAgZediL8Uf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4339,
      "cache_read_input_tokens": 47663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4339
      },
      "output_tokens": 11,
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

_source line 61 · 2026-05-25T07:44:18.415Z_

<details><summary>↩ Tool result · `toolu_019kSqCDGT93T67WXK5dSgc1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "28e9d9e5-9797-4fef-b606-d5dafc57d072",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
    "oldString": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-20",
    "newString": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-25",
    "originalFile": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-20\n\npapers:\n\n  # ===== 已有论文 =====\n\n  - paper_id: \"2512.11891\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\"\n\n  - paper_id: \"2510.14836\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: spatial-aware-vla\n    one_line_summary: \"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\"\n\n  - paper_id: \"2510.12276\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICLR 2026\n    role: method-component\n    category: spatial-aware-vla\n    one_line_summary: \"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\"\n\n  - paper_id: \"2307.05973\"\n    title: \"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: CoRL 2023\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\"\n\n  - paper_id: \"2410.24164\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al., Physical Intelligence\"\n    year: 2024\n    venue: arXiv\n    role: backbone\n    category: vla-foundation\n    one_line_summary: \"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\"\n\n  - paper_id: \"1901.05103\"\n    title: \"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\"\n    authors: \"Park et al.\"\n    year: 2019\n    venue: CVPR 2019\n    role: method-component\n    category: sdf-representation\n    one_line_summary: \"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\"\n\n  - paper_id: \"2307.00533\"\n    title: \"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: arXiv\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\"\n\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\n\n  - paper_id: \"2503.03480\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    arxiv: \"2503.03480\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\"\n    relevance: \"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\"\n\n  - paper_id: \"2407.00451\"\n    title: \"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: ICRA 2025\n    arxiv: \"2407.00451\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\"\n    relevance: \"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\"\n\n  - paper_id: \"2511.22773\"\n    title: \"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\"\n    authors: \"Yang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2511.22773\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\"\n    relevance: \"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\"\n\n  - paper_id: \"2409.08233\"\n    title: \"Towards Online Safety Corrections for Robotic Manipulation Policies\"\n    authors: \"Spalter et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.08233\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"\n    relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\n\n  - paper_id: \"2204.02296\"\n    title: \"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\"\n    authors: \"Ortiz et al.\"\n    year: 2022\n    venue: RSS 2022\n    arxiv: \"2204.02296\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\"\n    relevance: \"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\"\n\n  - paper_id: \"2305.10534\"\n    title: \"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\"\n    authors: \"Vasilopoulos et al.\"\n    year: 2023\n    venue: IROS 2023\n    arxiv: \"2305.10534\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\"\n    relevance: \"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\"\n\n  - paper_id: \"2102.07413\"\n    title: \"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\"\n    authors: \"Zhi et al.\"\n    year: 2021\n    venue: IEEE T-RO\n    arxiv: \"2102.07413\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"\n    relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====\n\n  - paper_id: \"2307.15818\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al., Google DeepMind\"\n    year: 2023\n    venue: arXiv\n    arxiv: \"2307.15818\"\n    role: foundational\n    category: vla-foundation\n    summary: \"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\"\n    relevance: \"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\"\n\n  - paper_id: \"2406.09246\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2406.09246\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\"\n    relevance: \"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\"\n\n  - paper_id: \"2405.12213\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2405.12213\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"\n    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n\n  # ===== 新增 P3: Benchmark =====\n\n  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2306.03310\"\n    role: benchmark\n    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"\n\n  # ===== 新增 P4: 生成式建模基础方法 =====\n\n  - title: \"Flow Matching for Generative Modeling\"\n    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.02747\"\n    role: method-component\n    relevance: \"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\"\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " # ColliForce-VLA Literature Map",
          "-# Updated: 2026-05-20",
          "+# Updated: 2026-05-25",
          " ",
          " papers:",
          " "
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

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01C5zzUvTY8EK8vLXNzLxhKS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
  "old_string": "  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====",
  "new_string": "  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\n\n  - paper_id: \"2601.21712\"\n    title: \"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\"\n    authors: \"Zhai et al.\"\n    year: 2026\n    venue: arXiv\n    arxiv: \"2601.21712\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\"\n    relevance: \"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\"\n\n  - paper_id: \"2404.02284\"\n    title: \"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\"\n    authors: \"Dastider et al.\"\n    year: 2024\n    venue: IROS 2024\n    arxiv: \"2404.02284\"\n    role: related-approach\n    category: collision-aware-manipulation\n    summary: \"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\"\n    relevance: \"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\"\n\n  - paper_id: \"2512.11908\"\n    title: \"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2512.11908\"\n    role: survey\n    category: collision-aware-manipulation\n    summary: \"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\"\n    relevance: \"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 ====="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "0117747a-bbf2-477c-b6f2-4e372149dd7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bH4ka3U9ZAg6Qx1Ay6SF3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 52002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
      },
      "output_tokens": 72,
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

_source line 63 · 2026-05-25T07:44:40.716Z_

<details><summary>↩ Tool result · `toolu_01C5zzUvTY8EK8vLXNzLxhKS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "24a15f7d-8d1b-47f1-b57b-2a7b33400b70",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
    "oldString": "  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====",
    "newString": "  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\n\n  - paper_id: \"2601.21712\"\n    title: \"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\"\n    authors: \"Zhai et al.\"\n    year: 2026\n    venue: arXiv\n    arxiv: \"2601.21712\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\"\n    relevance: \"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\"\n\n  - paper_id: \"2404.02284\"\n    title: \"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\"\n    authors: \"Dastider et al.\"\n    year: 2024\n    venue: IROS 2024\n    arxiv: \"2404.02284\"\n    role: related-approach\n    category: collision-aware-manipulation\n    summary: \"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\"\n    relevance: \"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\"\n\n  - paper_id: \"2512.11908\"\n    title: \"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2512.11908\"\n    role: survey\n    category: collision-aware-manipulation\n    summary: \"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\"\n    relevance: \"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====",
    "originalFile": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-25\n\npapers:\n\n  # ===== 已有论文 =====\n\n  - paper_id: \"2512.11891\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\"\n\n  - paper_id: \"2510.14836\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: spatial-aware-vla\n    one_line_summary: \"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\"\n\n  - paper_id: \"2510.12276\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICLR 2026\n    role: method-component\n    category: spatial-aware-vla\n    one_line_summary: \"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\"\n\n  - paper_id: \"2307.05973\"\n    title: \"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: CoRL 2023\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\"\n\n  - paper_id: \"2410.24164\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al., Physical Intelligence\"\n    year: 2024\n    venue: arXiv\n    role: backbone\n    category: vla-foundation\n    one_line_summary: \"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\"\n\n  - paper_id: \"1901.05103\"\n    title: \"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\"\n    authors: \"Park et al.\"\n    year: 2019\n    venue: CVPR 2019\n    role: method-component\n    category: sdf-representation\n    one_line_summary: \"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\"\n\n  - paper_id: \"2307.00533\"\n    title: \"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: arXiv\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\"\n\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\n\n  - paper_id: \"2503.03480\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    arxiv: \"2503.03480\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\"\n    relevance: \"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\"\n\n  - paper_id: \"2407.00451\"\n    title: \"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: ICRA 2025\n    arxiv: \"2407.00451\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\"\n    relevance: \"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\"\n\n  - paper_id: \"2511.22773\"\n    title: \"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\"\n    authors: \"Yang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2511.22773\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\"\n    relevance: \"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\"\n\n  - paper_id: \"2409.08233\"\n    title: \"Towards Online Safety Corrections for Robotic Manipulation Policies\"\n    authors: \"Spalter et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.08233\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"\n    relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\n\n  - paper_id: \"2204.02296\"\n    title: \"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\"\n    authors: \"Ortiz et al.\"\n    year: 2022\n    venue: RSS 2022\n    arxiv: \"2204.02296\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\"\n    relevance: \"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\"\n\n  - paper_id: \"2305.10534\"\n    title: \"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\"\n    authors: \"Vasilopoulos et al.\"\n    year: 2023\n    venue: IROS 2023\n    arxiv: \"2305.10534\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\"\n    relevance: \"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\"\n\n  - paper_id: \"2102.07413\"\n    title: \"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\"\n    authors: \"Zhi et al.\"\n    year: 2021\n    venue: IEEE T-RO\n    arxiv: \"2102.07413\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"\n    relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====\n\n  - paper_id: \"2307.15818\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al., Google DeepMind\"\n    year: 2023\n    venue: arXiv\n    arxiv: \"2307.15818\"\n    role: foundational\n    category: vla-foundation\n    summary: \"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\"\n    relevance: \"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\"\n\n  - paper_id: \"2406.09246\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2406.09246\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\"\n    relevance: \"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\"\n\n  - paper_id: \"2405.12213\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2405.12213\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"\n    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n\n  # ===== 新增 P3: Benchmark =====\n\n  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2306.03310\"\n    role: benchmark\n    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"\n\n  # ===== 新增 P4: 生成式建模基础方法 =====\n\n  - title: \"Flow Matching for Generative Modeling\"\n    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.02747\"\n    role: method-component\n    relevance: \"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\"\n",
    "structuredPatch": [
      {
        "oldStart": 114,
        "oldLines": 6,
        "newStart": 114,
        "newLines": 41,
        "lines": [
          "     summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"",
          "     relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"",
          " ",
          "+  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====",
          "+",
          "+  - paper_id: \"2601.21712\"",
          "+    title: \"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\"",
          "+    authors: \"Zhai et al.\"",
          "+    year: 2026",
          "+    venue: arXiv",
          "+    arxiv: \"2601.21712\"",
          "+    role: direct-competitor",
          "+    category: collision-aware-vla",
          "+    summary: \"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\"",
          "+    relevance: \"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\"",
          "+",
          "+  - paper_id: \"2404.02284\"",
          "+    title: \"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\"",
          "+    authors: \"Dastider et al.\"",
          "+    year: 2024",
          "+    venue: IROS 2024",
          "+    arxiv: \"2404.02284\"",
          "+    role: related-approach",
          "+    category: collision-aware-manipulation",
          "+    summary: \"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\"",
          "+    relevance: \"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\"",
          "+",
          "+  - paper_id: \"2512.11908\"",
          "+    title: \"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\"",
          "+    authors: \"Zhang et al.\"",
          "+    year: 2025",
          "+    venue: arXiv",
          "+    arxiv: \"2512.11908\"",
          "+    role: survey",
          "+    category: collision-aware-manipulation",
          "+    summary: \"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\"",
          "+    relevance: \"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\"",
          "+",
          "   # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====",
          " ",
          "   - paper_id: \"2204.02296\""
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

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_01DMMEXRnbhKthNEhMdQB5cn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
  "old_string": "  # ===== 新增 P2: VLA 基座模型系列 =====",
  "new_string": "  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\n\n  - paper_id: \"2406.01137\"\n    title: \"Configuration Space Distance Fields for Manipulation Planning\"\n    authors: \"Li, Chi, Razmjoo, Calinon\"\n    year: 2024\n    venue: RSS 2024\n    arxiv: \"2406.01137\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\"\n    relevance: \"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\"\n\n  - paper_id: \"2409.14955\"\n    title: \"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\"\n    authors: \"Liu et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.14955\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\"\n    relevance: \"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\"\n\n  - paper_id: \"2511.21312\"\n    title: \"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\"\n    authors: \"Jacquet, Harms, Alexis\"\n    year: 2025\n    venue: IJRR 2025\n    arxiv: \"2511.21312\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\"\n    relevance: \"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 ====="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "24be29bf-d77a-452f-8fa6-30c3503aa32c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYw12W18rRRhwHFAZVGpfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 52851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1077
      },
      "output_tokens": 48,
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

_source line 65 · 2026-05-25T07:45:01.298Z_

<details><summary>↩ Tool result · `toolu_01DMMEXRnbhKthNEhMdQB5cn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "0dfd03e0-d1c8-4a16-bbf8-ab57c8d3110e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
    "oldString": "  # ===== 新增 P2: VLA 基座模型系列 =====",
    "newString": "  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\n\n  - paper_id: \"2406.01137\"\n    title: \"Configuration Space Distance Fields for Manipulation Planning\"\n    authors: \"Li, Chi, Razmjoo, Calinon\"\n    year: 2024\n    venue: RSS 2024\n    arxiv: \"2406.01137\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\"\n    relevance: \"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\"\n\n  - paper_id: \"2409.14955\"\n    title: \"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\"\n    authors: \"Liu et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.14955\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\"\n    relevance: \"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\"\n\n  - paper_id: \"2511.21312\"\n    title: \"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\"\n    authors: \"Jacquet, Harms, Alexis\"\n    year: 2025\n    venue: IJRR 2025\n    arxiv: \"2511.21312\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\"\n    relevance: \"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====",
    "originalFile": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-25\n\npapers:\n\n  # ===== 已有论文 =====\n\n  - paper_id: \"2512.11891\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\"\n\n  - paper_id: \"2510.14836\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: spatial-aware-vla\n    one_line_summary: \"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\"\n\n  - paper_id: \"2510.12276\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICLR 2026\n    role: method-component\n    category: spatial-aware-vla\n    one_line_summary: \"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\"\n\n  - paper_id: \"2307.05973\"\n    title: \"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: CoRL 2023\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\"\n\n  - paper_id: \"2410.24164\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al., Physical Intelligence\"\n    year: 2024\n    venue: arXiv\n    role: backbone\n    category: vla-foundation\n    one_line_summary: \"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\"\n\n  - paper_id: \"1901.05103\"\n    title: \"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\"\n    authors: \"Park et al.\"\n    year: 2019\n    venue: CVPR 2019\n    role: method-component\n    category: sdf-representation\n    one_line_summary: \"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\"\n\n  - paper_id: \"2307.00533\"\n    title: \"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: arXiv\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\"\n\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\n\n  - paper_id: \"2503.03480\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    arxiv: \"2503.03480\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\"\n    relevance: \"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\"\n\n  - paper_id: \"2407.00451\"\n    title: \"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: ICRA 2025\n    arxiv: \"2407.00451\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\"\n    relevance: \"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\"\n\n  - paper_id: \"2511.22773\"\n    title: \"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\"\n    authors: \"Yang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2511.22773\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\"\n    relevance: \"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\"\n\n  - paper_id: \"2409.08233\"\n    title: \"Towards Online Safety Corrections for Robotic Manipulation Policies\"\n    authors: \"Spalter et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.08233\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"\n    relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"\n\n  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\n\n  - paper_id: \"2601.21712\"\n    title: \"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\"\n    authors: \"Zhai et al.\"\n    year: 2026\n    venue: arXiv\n    arxiv: \"2601.21712\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\"\n    relevance: \"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\"\n\n  - paper_id: \"2404.02284\"\n    title: \"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\"\n    authors: \"Dastider et al.\"\n    year: 2024\n    venue: IROS 2024\n    arxiv: \"2404.02284\"\n    role: related-approach\n    category: collision-aware-manipulation\n    summary: \"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\"\n    relevance: \"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\"\n\n  - paper_id: \"2512.11908\"\n    title: \"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2512.11908\"\n    role: survey\n    category: collision-aware-manipulation\n    summary: \"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\"\n    relevance: \"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\n\n  - paper_id: \"2204.02296\"\n    title: \"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\"\n    authors: \"Ortiz et al.\"\n    year: 2022\n    venue: RSS 2022\n    arxiv: \"2204.02296\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\"\n    relevance: \"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\"\n\n  - paper_id: \"2305.10534\"\n    title: \"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\"\n    authors: \"Vasilopoulos et al.\"\n    year: 2023\n    venue: IROS 2023\n    arxiv: \"2305.10534\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\"\n    relevance: \"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\"\n\n  - paper_id: \"2102.07413\"\n    title: \"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\"\n    authors: \"Zhi et al.\"\n    year: 2021\n    venue: IEEE T-RO\n    arxiv: \"2102.07413\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"\n    relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====\n\n  - paper_id: \"2307.15818\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al., Google DeepMind\"\n    year: 2023\n    venue: arXiv\n    arxiv: \"2307.15818\"\n    role: foundational\n    category: vla-foundation\n    summary: \"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\"\n    relevance: \"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\"\n\n  - paper_id: \"2406.09246\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2406.09246\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\"\n    relevance: \"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\"\n\n  - paper_id: \"2405.12213\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2405.12213\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"\n    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n\n  # ===== 新增 P3: Benchmark =====\n\n  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2306.03310\"\n    role: benchmark\n    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"\n\n  # ===== 新增 P4: 生成式建模基础方法 =====\n\n  - title: \"Flow Matching for Generative Modeling\"\n    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.02747\"\n    role: method-component\n    relevance: \"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\"\n",
    "structuredPatch": [
      {
        "oldStart": 184,
        "oldLines": 6,
        "newStart": 184,
        "newLines": 41,
        "lines": [
          "     summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"",
          "     relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"",
          " ",
          "+  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====",
          "+",
          "+  - paper_id: \"2406.01137\"",
          "+    title: \"Configuration Space Distance Fields for Manipulation Planning\"",
          "+    authors: \"Li, Chi, Razmjoo, Calinon\"",
          "+    year: 2024",
          "+    venue: RSS 2024",
          "+    arxiv: \"2406.01137\"",
          "+    role: method-component",
          "+    category: sdf-robotics",
          "+    summary: \"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\"",
          "+    relevance: \"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\"",
          "+",
          "+  - paper_id: \"2409.14955\"",
          "+    title: \"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\"",
          "+    authors: \"Liu et al.\"",
          "+    year: 2024",
          "+    venue: arXiv",
          "+    arxiv: \"2409.14955\"",
          "+    role: method-component",
          "+    category: sdf-robotics",
          "+    summary: \"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\"",
          "+    relevance: \"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\"",
          "+",
          "+  - paper_id: \"2511.21312\"",
          "+    title: \"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\"",
          "+    authors: \"Jacquet, Harms, Alexis\"",
          "+    year: 2025",
          "+    venue: IJRR 2025",
          "+    arxiv: \"2511.21312\"",
          "+    role: method-component",
          "+    category: sdf-robotics",
          "+    summary: \"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\"",
          "+    relevance: \"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\"",
          "+",
          "   # ===== 新增 P2: VLA 基座模型系列 =====",
          " ",
          "   - paper_id: \"2307.15818\""
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

_source line 66_

更新完成。以下是补充的 6 篇论文简要分析：

---

### Direction 1: Collision-aware manipulation（3 篇）

| 论文 | Venue | 与 ColliForce 的对比点 |
|------|-------|----------------------|
| **CoFreeVLA** (Zhai et al., 2026) | arXiv | 最新 VLA+碰撞安全工作。外挂风险估计器做 post-hoc 过滤，ColliForce 通过 SDF 辅助损失在训练时嵌入碰撞感知 → internal vs. external 路线对比 |
| **APEX** (Dastider et al., IROS 2024) | IROS 2024 | 潜在扩散模型 + classifier-guidance 碰撞回避。属推理阶段安全注入方法族（同 Lan-o3dp, CAPE），与 ColliForce 训练阶段方法形成 train-time vs. test-time 对比 |
| **Safe Learning Survey** (Zhang et al., 2025) | arXiv | 系统综述，将安全方法分为 constrained RL / CBF / MPC shields 等。可用于 Related Work 中定位 ColliForce 为 "training-time geometric supervision" 路线 |

### Direction 2: SDF in robotics（3 篇）

| 论文 | Venue | 与 ColliForce 的对比点 |
|------|-------|----------------------|
| **Configuration Space Distance Fields** (Li et al., RSS 2024) | RSS 2024 | 将 SDF 从 task-space 扩展到 C-space，天然覆盖全身碰撞。直接回应 ColliForce EE-only SDF 局限 → C-space SDF 是 full-body 方案的代表 |
| **SDF-SC** (Liu et al., 2024) | arXiv | FK 分解全身 SDF + 轻量并行网络 + SVM 自碰撞检测，保持可微性。展示全身 SDF 的工程可行性，为 ColliForce 后续 full-body 扩展提供参考 |
| **Neural NMPC-SDF** (Jacquet et al., IJRR 2025) | IJRR 2025 | 深度图像→神经 SDF→NMPC 约束的端到端集成。SDF 进控制 vs. ColliForce SDF 进 policy loss，两条集成路径互为对照 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "uuid": "e6aa19f6-4f2f-4fe1-bdd5-7ada40252ecf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GU1ynsyz9aa1W3V9EdJj5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1022,
      "cache_read_input_tokens": 53928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1022
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

_source line 67_

更新完成。以下是补充的 6 篇论文简要分析：

---

### Direction 1: Collision-aware manipulation（3 篇）

| 论文 | Venue | 与 ColliForce 的对比点 |
|------|-------|----------------------|
| **CoFreeVLA** (Zhai et al., 2026) | arXiv | 最新 VLA+碰撞安全工作。外挂风险估计器做 post-hoc 过滤，ColliForce 通过 SDF 辅助损失在训练时嵌入碰撞感知 → internal vs. external 路线对比 |
| **APEX** (Dastider et al., IROS 2024) | IROS 2024 | 潜在扩散模型 + classifier-guidance 碰撞回避。属推理阶段安全注入方法族（同 Lan-o3dp, CAPE），与 ColliForce 训练阶段方法形成 train-time vs. test-time 对比 |
| **Safe Learning Survey** (Zhang et al., 2025) | arXiv | 系统综述，将安全方法分为 constrained RL / CBF / MPC shields 等。可用于 Related Work 中定位 ColliForce 为 "training-time geometric supervision" 路线 |

### Direction 2: SDF in robotics（3 篇）

| 论文 | Venue | 与 ColliForce 的对比点 |
|------|-------|----------------------|
| **Configuration Space Distance Fields** (Li et al., RSS 2024) | RSS 2024 | 将 SDF 从 task-space 扩展到 C-space，天然覆盖全身碰撞。直接回应 ColliForce EE-only SDF 局限 → C-space SDF 是 full-body 方案的代表 |
| **SDF-SC** (Liu et al., 2024) | arXiv | FK 分解全身 SDF + 轻量并行网络 + SVM 自碰撞检测，保持可微性。展示全身 SDF 的工程可行性，为 ColliForce 后续 full-body 扩展提供参考 |
| **Neural NMPC-SDF** (Jacquet et al., IJRR 2025) | IJRR 2025 | 深度图像→神经 SDF→NMPC 约束的端到端集成。SDF 进控制 vs. ColliForce SDF 进 policy loss，两条集成路径互为对照 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 275737,
  "duration_api_ms": 353617,
  "num_turns": 25,
  "stop_reason": "end_turn",
  "session_id": "c3defa5a-9f34-49a4-820f-8d8e03868ecd",
  "total_cost_usd": 1.05931225,
  "usage": {
    "input_tokens": 4363,
    "cache_creation_input_tokens": 43503,
    "cache_read_input_tokens": 540801,
    "output_tokens": 7090,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 43503,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 705,
        "cache_read_input_tokens": 53928,
        "cache_creation_input_tokens": 1022,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1022
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 134598,
      "outputTokens": 6671,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 15,
      "costUSD": 0.31795299999999993,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4363,
      "outputTokens": 7090,
      "cacheReadInputTokens": 540801,
      "cacheCreationInputTokens": 43503,
      "webSearchRequests": 0,
      "costUSD": 0.74135925,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c3c60ac2-7d7e-4246-8caf-9bd42df670ba"
}
```

</details>

---
