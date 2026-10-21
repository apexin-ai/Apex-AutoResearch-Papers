# knowledge literature map update

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_knowledge_literature_map_update_20260520T092540.log`
- **Structured JSON:** [`2100d9abf4e6661f433b.json`](../../sessions/21/2100d9abf4e6661f433b.json)

## Before a recorded user message

20 recorded events

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
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
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
  "uuid": "74295814-2646-4d4c-bcd5-5e3cfe0567b0",
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
    "resetsAt": 1779283200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a7b8cd5f-a77f-44ff-912b-5e97d930e322",
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current literature_map.yaml file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "1ef99372-6362-45e9-aea7-abe5271dfe3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELoeqr7QTitCV16QUgy1vZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
      },
      "output_tokens": 46,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HhX8d7qprjxBTaWKGNLDAJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "759ee2ba-10f0-4d54-9a31-9df454573ee2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELoeqr7QTitCV16QUgy1vZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
      },
      "output_tokens": 46,
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

_source line 6 · 2026-05-20T09:25:49.982Z_

<details><summary>↩ Tool result · `toolu_01HhX8d7qprjxBTaWKGNLDAJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

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
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "1248ebff-23e2-42b2-b2ca-60dc3910ff0c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Rzoraoh4i772S1U8eAq3Q8`</summary>

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
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "9d30166c-52d0-4994-8138-78b011c26642",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cToU4YVtYEU4aH3hdFhoG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 23267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 728
      },
      "output_tokens": 69,
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

_source line 8 · 2026-05-20T09:25:52.769Z_

<details><summary>↩ Tool result · `toolu_01Rzoraoh4i772S1U8eAq3Q8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-20\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 occupancy field。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\", \"total_chars\": 7018, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "700a5deb-b839-478a-8dd5-f912834b11bb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\\\", \\\"content\\\": \\\"# ColliForce-VLA Literature Map\\\\n# Updated: 2026-05-20\\\\n\\\\npapers:\\\\n\\\\n  # ===== 已有论文 =====\\\\n\\\\n  - paper_id: \\\\\\\"2512.11891\\\\\\\"\\\\n    title: \\\\\\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\\\\\"\\\\n    authors: \\\\\\\"Hu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    one_line_summary: \\\\\\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.14836\\\\\\\"\\\\n    title: \\\\\\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    one_line_summary: \\\\\\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 occupancy field。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.12276\\\\\\\"\\\\n    title: \\\\\\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: ICLR 2026\\\\n    role: method-component\\\\n    category: spatial-aware-vla\\\\n    one_line_summary: \\\\\\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.05973\\\\\\\"\\\\n    title: \\\\\\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Huang et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: CoRL 2023\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2410.24164\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al., Physical Intelligence\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    role: backbone\\\\n    category: vla-foundation\\\\n    one_line_summary: \\\\\\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"1901.05103\\\\\\\"\\\\n    title: \\\\\\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\\\\\"\\\\n    authors: \\\\\\\"Park et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: CVPR 2019\\\\n    role: method-component\\\\n    category: sdf-representation\\\\n    one_line_summary: \\\\\\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.00533\\\\\\\"\\\\n    title: \\\\\\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\\\\\"\\\\n\\\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\\\n\\\\n  - paper_id: \\\\\\\"2503.03480\\\\\\\"\\\\n    title: \\\\\\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: NeurIPS 2025 (Spotlight)\\\\n    arxiv: \\\\\\\"2503.03480\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\\\\\"\\\\n    relevance: \\\\\\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2407.00451\\\\\\\"\\\\n    title: \\\\\\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: ICRA 2025\\\\n    arxiv: \\\\\\\"2407.00451\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\\\\\"\\\\n    relevance: \\\\\\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2511.22773\\\\\\\"\\\\n    title: \\\\\\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2511.22773\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\\\\\"\\\\n    relevance: \\\\\\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.08233\\\\\\\"\\\\n    title: \\\\\\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\\\\\"\\\\n    authors: \\\\\\\"Spalter et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2409.08233\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\\\\\"\\\\n    relevance: \\\\\\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\\\\\"\\\\n\\\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\\\n\\\\n  - paper_id: \\\\\\\"2204.02296\\\\\\\"\\\\n    title: \\\\\\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\\\\\"\\\\n    authors: \\\\\\\"Ortiz et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: RSS 2022\\\\n    arxiv: \\\\\\\"2204.02296\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\\\\\"\\\\n    relevance: \\\\\\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2305.10534\\\\\\\"\\\\n    title: \\\\\\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\\\\\"\\\\n    authors: \\\\\\\"Vasilopoulos et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: IROS 2023\\\\n    arxiv: \\\\\\\"2305.10534\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\\\\\"\\\\n    relevance: \\\\\\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2102.07413\\\\\\\"\\\\n    title: \\\\\\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Zhi et al.\\\\\\\"\\\\n    year: 2021\\\\n    venue: IEEE T-RO\\\\n    arxiv: \\\\\\\"2102.07413\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\\\\\"\\\\n    relevance: \\\\\\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\\\\\"\\\\n\\\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\\\n\\\\n  - paper_id: \\\\\\\"2307.15818\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al., Google DeepMind\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2307.15818\\\\\\\"\\\\n    role: foundational\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\\\\\"\\\\n    relevance: \\\\\\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2406.09246\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2406.09246\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\\\\\"\\\\n    relevance: \\\\\\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2405.12213\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Octo Model Team\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2405.12213\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\\\\\"\\\\n    relevance: \\\\\\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 7018, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-20\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 occupancy field。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\", \"total_chars\": 7018, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The file doesn't contain LIBERO benchmark paper or Flow Matching paper. I need to add both. Let me check the existing structure and add them to appropriate categories.

Looking at the existing categories:
- collision-aware-vla
- sdf-robotics
- sdf-representation
- spatial-aware-vla
- vla-foundation

LIBERO should go into a benchmark category. Flow Matching should go into a method-component category (like vla-foundation or a new foundational-method category).

Let me add them. I'll place LIBERO after the VLA foundation section and Flow Matching in the method-component area. 

I'm noticing the existing entries use inconsistent field names—some have `summary`, others have `one_line_summary` or `relevance`—but the user specified exact YAML formatting to follow. I'll append both new entries at the end of the file under appropriate section comments, matching the existing pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "efa37492-f02f-4410-9b31-8321a9b0a22e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BM3GgiPSLMCPEDSd9FgWHh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 23995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 10_

两篇论文均缺失，补充到文件末尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "c6d1e076-a417-4a3f-8811-7a417db4deba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BM3GgiPSLMCPEDSd9FgWHh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 23995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01YJVNH67AxG4FopAH2XTAsk`</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "literature_map.yaml",
  "content": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-20\n\npapers:\n\n  # ===== 已有论文 =====\n\n  - paper_id: \"2512.11891\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\"\n\n  - paper_id: \"2510.14836\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 occupancy field。\"\n\n  - paper_id: \"2510.12276\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICLR 2026\n    role: method-component\n    category: spatial-aware-vla\n    one_line_summary: \"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\"\n\n  - paper_id: \"2307.05973\"\n    title: \"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: CoRL 2023\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\"\n\n  - paper_id: \"2410.24164\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al., Physical Intelligence\"\n    year: 2024\n    venue: arXiv\n    role: backbone\n    category: vla-foundation\n    one_line_summary: \"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\"\n\n  - paper_id: \"1901.05103\"\n    title: \"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\"\n    authors: \"Park et al.\"\n    year: 2019\n    venue: CVPR 2019\n    role: method-component\n    category: sdf-representation\n    one_line_summary: \"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\"\n\n  - paper_id: \"2307.00533\"\n    title: \"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: arXiv\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\"\n\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\n\n  - paper_id: \"2503.03480\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    arxiv: \"2503.03480\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\"\n    relevance: \"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\"\n\n  - paper_id: \"2407.00451\"\n    title: \"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: ICRA 2025\n    arxiv: \"2407.00451\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\"\n    relevance: \"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\"\n\n  - paper_id: \"2511.22773\"\n    title: \"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\"\n    authors: \"Yang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2511.22773\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\"\n    relevance: \"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\"\n\n  - paper_id: \"2409.08233\"\n    title: \"Towards Online Safety Corrections for Robotic Manipulation Policies\"\n    authors: \"Spalter et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.08233\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"\n    relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\n\n  - paper_id: \"2204.02296\"\n    title: \"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\"\n    authors: \"Ortiz et al.\"\n    year: 2022\n    venue: RSS 2022\n    arxiv: \"2204.02296\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\"\n    relevance: \"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\"\n\n  - paper_id: \"2305.10534\"\n    title: \"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\"\n    authors: \"Vasilopoulos et al.\"\n    year: 2023\n    venue: IROS 2023\n    arxiv: \"2305.10534\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\"\n    relevance: \"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\"\n\n  - paper_id: \"2102.07413\"\n    title: \"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\"\n    authors: \"Zhi et al.\"\n    year: 2021\n    venue: IEEE T-RO\n    arxiv: \"2102.07413\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"\n    relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====\n\n  - paper_id: \"2307.15818\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al., Google DeepMind\"\n    year: 2023\n    venue: arXiv\n    arxiv: \"2307.15818\"\n    role: foundational\n    category: vla-foundation\n    summary: \"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\"\n    relevance: \"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\"\n\n  - paper_id: \"2406.09246\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2406.09246\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\"\n    relevance: \"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\"\n\n  - paper_id: \"2405.12213\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2405.12213\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"\n    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n\n  # ===== 新增 P3: Benchmark =====\n\n  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2306.03310\"\n    role: benchmark\n    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"\n\n  # ===== 新增 P4: 生成式建模基础方法 =====\n\n  - title: \"Flow Matching for Generative Modeling\"\n    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.02747\"\n    role: method-component\n    relevance: \"π0 base model 使用的 flow matching 训练范式；A3 gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "60a2e992-7e4a-4257-939f-b065043e7714",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BM3GgiPSLMCPEDSd9FgWHh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4046,
      "cache_read_input_tokens": 23995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4046
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

_source line 12 · 2026-05-20T09:26:35.806Z_

<details><summary>↩ Tool result · `toolu_01YJVNH67AxG4FopAH2XTAsk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "76c18c15-3ca5-4191-a7b3-d6ce93fed37f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool doesn't allow writing literature_map.yaml. I need to write it directly to the file system.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "b6a82176-7cee-4e8a-9c06-f34d75a14f20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUnzhKrFXx9nYC5eRA3SS3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4158,
      "cache_read_input_tokens": 28041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4158
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

_source line 14_

工具不支持写 literature_map.yaml，直接写文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "761a44e8-67f5-4f31-b7ee-5b53a5824399",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUnzhKrFXx9nYC5eRA3SS3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4158,
      "cache_read_input_tokens": 28041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4158
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_0154gwuWScNf3USevgdMdjWo`</summary>

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
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "d5f039a1-02a3-4e33-909a-874af8c7aa8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUnzhKrFXx9nYC5eRA3SS3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4158,
      "cache_read_input_tokens": 28041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4158
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

_source line 16 · 2026-05-20T09:26:39.997Z_

<details><summary>↩ Tool result · `toolu_0154gwuWScNf3USevgdMdjWo`</summary>

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
23	    category: collision-aware-vla
24	    one_line_summary: "用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 occupancy field。"
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "d88d831f-52e7-46d4-a1ca-5b3769035d72",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
      "content": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-20\n\npapers:\n\n  # ===== 已有论文 =====\n\n  - paper_id: \"2512.11891\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\"\n\n  - paper_id: \"2510.14836\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 occupancy field。\"\n\n  - paper_id: \"2510.12276\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICLR 2026\n    role: method-component\n    category: spatial-aware-vla\n    one_line_summary: \"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\"\n\n  - paper_id: \"2307.05973\"\n    title: \"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: CoRL 2023\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\"\n\n  - paper_id: \"2410.24164\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al., Physical Intelligence\"\n    year: 2024\n    venue: arXiv\n    role: backbone\n    category: vla-foundation\n    one_line_summary: \"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\"\n\n  - paper_id: \"1901.05103\"\n    title: \"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\"\n    authors: \"Park et al.\"\n    year: 2019\n    venue: CVPR 2019\n    role: method-component\n    category: sdf-representation\n    one_line_summary: \"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\"\n\n  - paper_id: \"2307.00533\"\n    title: \"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: arXiv\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\"\n\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\n\n  - paper_id: \"2503.03480\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    arxiv: \"2503.03480\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\"\n    relevance: \"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\"\n\n  - paper_id: \"2407.00451\"\n    title: \"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: ICRA 2025\n    arxiv: \"2407.00451\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\"\n    relevance: \"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\"\n\n  - paper_id: \"2511.22773\"\n    title: \"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\"\n    authors: \"Yang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2511.22773\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\"\n    relevance: \"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\"\n\n  - paper_id: \"2409.08233\"\n    title: \"Towards Online Safety Corrections for Robotic Manipulation Policies\"\n    authors: \"Spalter et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.08233\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"\n    relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\n\n  - paper_id: \"2204.02296\"\n    title: \"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\"\n    authors: \"Ortiz et al.\"\n    year: 2022\n    venue: RSS 2022\n    arxiv: \"2204.02296\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\"\n    relevance: \"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\"\n\n  - paper_id: \"2305.10534\"\n    title: \"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\"\n    authors: \"Vasilopoulos et al.\"\n    year: 2023\n    venue: IROS 2023\n    arxiv: \"2305.10534\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\"\n    relevance: \"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\"\n\n  - paper_id: \"2102.07413\"\n    title: \"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\"\n    authors: \"Zhi et al.\"\n    year: 2021\n    venue: IEEE T-RO\n    arxiv: \"2102.07413\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"\n    relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====\n\n  - paper_id: \"2307.15818\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al., Google DeepMind\"\n    year: 2023\n    venue: arXiv\n    arxiv: \"2307.15818\"\n    role: foundational\n    category: vla-foundation\n    summary: \"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\"\n    relevance: \"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\"\n\n  - paper_id: \"2406.09246\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2406.09246\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\"\n    relevance: \"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\"\n\n  - paper_id: \"2405.12213\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2405.12213\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"\n    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n",
      "numLines": 186,
      "startLine": 1,
      "totalLines": 186
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01VP6RbYYqBs9SAsTgR7nGUo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
  "old_string": "    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"",
  "new_string": "    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n\n  # ===== 新增 P3: Benchmark =====\n\n  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2306.03310\"\n    role: benchmark\n    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"\n\n  # ===== 新增 P4: 生成式建模基础方法 =====\n\n  - title: \"Flow Matching for Generative Modeling\"\n    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.02747\"\n    role: method-component\n    relevance: \"π0 base model 使用的 flow matching 训练范式；A3 gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "82b90283-3b1f-41f9-9555-d52353aec36e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrTb491nwPNpg8iyZbHALk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3900,
      "cache_read_input_tokens": 32199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3900
      },
      "output_tokens": 64,
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

_source line 18 · 2026-05-20T09:26:50.224Z_

<details><summary>↩ Tool result · `toolu_01VP6RbYYqBs9SAsTgR7nGUo`</summary>

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
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "886290f7-0964-4061-a867-0e54eb61cecf",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml",
    "oldString": "    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"",
    "newString": "    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n\n  # ===== 新增 P3: Benchmark =====\n\n  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2306.03310\"\n    role: benchmark\n    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"\n\n  # ===== 新增 P4: 生成式建模基础方法 =====\n\n  - title: \"Flow Matching for Generative Modeling\"\n    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.02747\"\n    role: method-component\n    relevance: \"π0 base model 使用的 flow matching 训练范式；A3 gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\"",
    "originalFile": "# ColliForce-VLA Literature Map\n# Updated: 2026-05-20\n\npapers:\n\n  # ===== 已有论文 =====\n\n  - paper_id: \"2512.11891\"\n    title: \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\"\n    authors: \"Hu et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\"\n\n  - paper_id: \"2510.14836\"\n    title: \"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: arXiv\n    role: direct-competitor\n    category: collision-aware-vla\n    one_line_summary: \"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 occupancy field。\"\n\n  - paper_id: \"2510.12276\"\n    title: \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICLR 2026\n    role: method-component\n    category: spatial-aware-vla\n    one_line_summary: \"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\"\n\n  - paper_id: \"2307.05973\"\n    title: \"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: CoRL 2023\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\"\n\n  - paper_id: \"2410.24164\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al., Physical Intelligence\"\n    year: 2024\n    venue: arXiv\n    role: backbone\n    category: vla-foundation\n    one_line_summary: \"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\"\n\n  - paper_id: \"1901.05103\"\n    title: \"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\"\n    authors: \"Park et al.\"\n    year: 2019\n    venue: CVPR 2019\n    role: method-component\n    category: sdf-representation\n    one_line_summary: \"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\"\n\n  - paper_id: \"2307.00533\"\n    title: \"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: arXiv\n    role: method-component\n    category: sdf-robotics\n    one_line_summary: \"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\"\n\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\n\n  - paper_id: \"2503.03480\"\n    title: \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: NeurIPS 2025 (Spotlight)\n    arxiv: \"2503.03480\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\"\n    relevance: \"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\"\n\n  - paper_id: \"2407.00451\"\n    title: \"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: ICRA 2025\n    arxiv: \"2407.00451\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\"\n    relevance: \"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\"\n\n  - paper_id: \"2511.22773\"\n    title: \"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\"\n    authors: \"Yang et al.\"\n    year: 2025\n    venue: arXiv\n    arxiv: \"2511.22773\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\"\n    relevance: \"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\"\n\n  - paper_id: \"2409.08233\"\n    title: \"Towards Online Safety Corrections for Robotic Manipulation Policies\"\n    authors: \"Spalter et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2409.08233\"\n    role: direct-competitor\n    category: collision-aware-vla\n    summary: \"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\"\n    relevance: \"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\"\n\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\n\n  - paper_id: \"2204.02296\"\n    title: \"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\"\n    authors: \"Ortiz et al.\"\n    year: 2022\n    venue: RSS 2022\n    arxiv: \"2204.02296\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\"\n    relevance: \"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\"\n\n  - paper_id: \"2305.10534\"\n    title: \"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\"\n    authors: \"Vasilopoulos et al.\"\n    year: 2023\n    venue: IROS 2023\n    arxiv: \"2305.10534\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\"\n    relevance: \"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\"\n\n  - paper_id: \"2102.07413\"\n    title: \"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\"\n    authors: \"Zhi et al.\"\n    year: 2021\n    venue: IEEE T-RO\n    arxiv: \"2102.07413\"\n    role: method-component\n    category: sdf-robotics\n    summary: \"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\"\n    relevance: \"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\"\n\n  # ===== 新增 P2: VLA 基座模型系列 =====\n\n  - paper_id: \"2307.15818\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al., Google DeepMind\"\n    year: 2023\n    venue: arXiv\n    arxiv: \"2307.15818\"\n    role: foundational\n    category: vla-foundation\n    summary: \"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\"\n    relevance: \"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\"\n\n  - paper_id: \"2406.09246\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2406.09246\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\"\n    relevance: \"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\"\n\n  - paper_id: \"2405.12213\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team\"\n    year: 2024\n    venue: arXiv\n    arxiv: \"2405.12213\"\n    role: benchmark-source\n    category: vla-foundation\n    summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"\n    relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"\n",
    "structuredPatch": [
      {
        "oldStart": 183,
        "oldLines": 3,
        "newStart": 183,
        "newLines": 21,
        "lines": [
          "     category: vla-foundation",
          "     summary: \"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\"",
          "     relevance: \"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\"",
          "+",
          "+  # ===== 新增 P3: Benchmark =====",
          "+",
          "+  - title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"",
          "+    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"",
          "+    venue: \"NeurIPS 2023\"",
          "+    arxiv: \"2306.03310\"",
          "+    role: benchmark",
          "+    relevance: \"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\"",
          "+",
          "+  # ===== 新增 P4: 生成式建模基础方法 =====",
          "+",
          "+  - title: \"Flow Matching for Generative Modeling\"",
          "+    authors: \"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\"",
          "+    venue: \"ICLR 2023\"",
          "+    arxiv: \"2210.02747\"",
          "+    role: method-component",
          "+    relevance: \"π0 base model 使用的 flow matching 训练范式；A3 gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\""
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

_source line 19_

已补充两篇论文：LIBERO (P3: Benchmark) 和 Flow Matching (P4: 生成式建模基础方法)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "uuid": "3c4b0f47-6eea-4d64-8ec1-692efe9f627b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2ZJE6sFSHr2xxCuJD4Jx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 36099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 607
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

_source line 20_

已补充两篇论文：LIBERO (P3: Benchmark) 和 Flow Matching (P4: 生成式建模基础方法)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 66608,
  "duration_api_ms": 67831,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "1bbde27e-8d04-49ab-a6f1-50327f93ea0c",
  "total_cost_usd": 0.36279275,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 25259,
    "cache_read_input_tokens": 155048,
    "output_tokens": 5043,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25259,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 44,
        "cache_read_input_tokens": 36099,
        "cache_creation_input_tokens": 607,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 607
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1180,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001275,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 5043,
      "cacheReadInputTokens": 155048,
      "cacheCreationInputTokens": 25259,
      "webSearchRequests": 0,
      "costUSD": 0.36151774999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bf9b8fb3-52ad-4154-8f37-c9edb8859822"
}
```

</details>

---
