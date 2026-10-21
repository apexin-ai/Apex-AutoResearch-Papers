# knowledge writing plan draft

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_knowledge_writing-plan-draft_20260516T002952.log`
- **Structured JSON:** [`56cf4231c0bbb524740d.json`](../../sessions/56/56cf4231c0bbb524740d.json)

## Before a recorded user message

33 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "23af018e-f026-46ae-a4bf-5a2e39c5d93c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1778907600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8de3c997-313c-4923-885a-8ca62a039e0a",
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required project files to get full context before drafting the writing plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "ef64a208-3139-479b-99d0-bf463dea2b07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Dfxp3xNmeu6vJZwwuQw7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11946
      },
      "output_tokens": 28,
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

读取项目文件和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "fdecd0b7-f04d-4f8b-93f2-1864c1baada4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Dfxp3xNmeu6vJZwwuQw7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11946
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AeQHqszLDSdwygGzFriMtX`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "fc1c923c-c329-4d82-a469-aedeab4d4d6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Dfxp3xNmeu6vJZwwuQw7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11946
      },
      "output_tokens": 28,
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

_source line 7 · 2026-05-16T00:30:02.746Z_

<details><summary>↩ Tool result · `toolu_01AeQHqszLDSdwygGzFriMtX`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "0e71cdcd-5525-4d25-8819-c33e23b97f41",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MnEgE95KQj8GsiRzXraATx`</summary>

```json
{
  "project": "vla-ssd",
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
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "0f4888dc-ab59-40ac-8c5f-08a7ef3d2a89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwxDD7cKnyMjTQw4UXp6TV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 23787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
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

_source line 9 · 2026-05-16T00:30:05.286Z_

<details><summary>↩ Tool result · `toolu_01MnEgE95KQj8GsiRzXraATx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Claims (3 条)\\n\\n1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.501, image_mean 聚合）和 standalone vision model（DINOv2 ρ=0.388）。\\n2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.706→0.683, p=0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.731 > projector 0.706, p=0.001），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector 0.706）。Readout concentration 是 learned behavior，不是架构固有属性。\\n3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。\\n\\n## Paper 主数值基准（image_mean 聚合，公平对比）\\n\\n| Model / Condition | RSA (image_mean) | Notes |\\n|---|---|---|\\n| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |\\n| VLA trained with-inst | 0.501 | Peak L23 |\\n| VLA untrained with-inst | 0.485 | Peak L23 |\\n| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |\\n| VLA untrained no-inst | 0.482 | Peak L29 |\\n| DINO-V2 | 0.388 | Vision-only baseline |\\n\\nlast_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。\\n\\n## Functional Probe 数值基准\\n\\n### Raw Action Prediction R²\\n\\n| Model | mean_R² | Notes |\\n|---|---|---|\\n| **SigLIP+Projector** | **0.706** | Vision encoder output |\\n| VLA Trained image_mean L19 | 0.683 | image tokens degraded — ✅ bootstrap CI=[0.011, 0.037], p=0.001 vs Proj |\\n| **Trained last_preaction L19** | **0.731** | readout concentration (p=0.001 vs projector) |\\n| Untrained image_mean L0 | 0.714 | Architecture-intrinsic |\\n| **Untrained last_preaction L32** | **0.686** | < projector (0.706) → redistribution requires training (D034) |\\n| DINO-V2 (LIBERO-Goal) | **0.712** | ✅ cls_token; DINO ≈ Proj (Δ=0.005, CI=[-0.008, 0.019], p=0.22, n.s.) |\\n\\n**Three-way ordering**: DINO (0.712) ≈ Projector (0.706) > LLM image_mean (0.683)\\n\\n**重要发现**: DINO 与 Projector 在 action decodability (R²) 上无显著差异，但 RSA 几何对齐差异显著（0.388 vs 0.615）。说明 action information 的 presence（probe 可解码）与 geometric alignment（表征空间结构匹配 action 空间结构）是不同维度。论文需区分这两个层面。\\n\\n### Action-Delta Prediction R²\\n\\n| Model | mean_R² | Notes |\\n|---|---|---|\\n| VLA Trained image_mean L14 | 0.122 | |\\n| SigLIP+Projector | 0.118 | ≈ LLM, CI includes 0 (p=0.04) |\\n| Untrained image_mean L0 | 0.117 | ≈ projector ≈ LLM |\\n| DINO (LIBERO-Goal) | 0.100 | action_delta probe from v2 |\\n| DINO (MVP-2 LIBERO-10) | 0.061 | 2× lower than projector/LLM |\\n\\n**Delta 维度结论**：三者几乎相同（~0.12），远 > DINO (0.06-0.10)。支持 vision encoder dominance（所有 action-delta info 追溯到 SigLIP）。Delta last_preaction 缺失（待补）。\\n\\n### 聚合口径依赖性（论文必须如实讨论）\\n\\n| Comparison | image_mean | last_preaction |\\n|---|---|---|\\n| Raw action: Proj vs LLM | Proj wins (+0.023, CI=[0.011, 0.037], p=0.001) | LLM wins (+0.025, p=0.001) |\\n| Delta: Proj vs LLM | ≈ tie (−0.003, CI includes 0) | TBD |\\n\\n主文用 image_mean（公平聚合），last_preaction 放 supplementary。但必须讨论聚合口径对结论的影响。\\n\\n## Story Spine\\n\\n- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。\\n- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。\\n- **Our framing**: 首次对 VLA 进行系统性 representational + functional analysis——组件级分解 + per-layer probing + action prediction probes，定量揭示 action-relevant 结构的来源和 LLM 对其的变换。发现 vision encoder 是 action information 的通用源头（DINO ≈ SigLIP in R²，但 VL pretraining 赋予 geometric alignment）。LLM 降解分布式 image token 表征但通过**训练依赖的** attention 机制将信号聚合到 readout token——training 教会 routing 而非 creating new knowledge。\\n- **Headline result**: \\\"The frozen vision encoder provides action-relevant representations (RSA ρ=0.615, action probe R²=0.706) that the LLM degrades at the image-token level (R²→0.683) but reconcentrates into a readout token (R²=0.731). This reconcentration is training-dependent (untrained readout R²=0.686 < projector 0.706), while distributed representation structure remains training-invariant (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20). Language instructions affect neither.\\\"\\n- **⚠️ Remaining**: (1) ~~untrained vs trained last_preaction bootstrap CI~~ ✅ Done (Δ=0.045, CI=[0.032, 0.058], p<0.0001); (2) plan_008 random instruction results (RUNNING). 其余 pending 均已解决。\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n### C1: 单一 VLA 架构（OpenVLA）泛化性\\n- **应对**: Scope 明确限定为 \\\"OpenVLA-class architecture\\\"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。\\n- **实验**: 无需额外实验，Limitations 明确标注。\\n\\n### C2: SigLIP vs DINOv2 pretraining confound\\n- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。\\n- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。新发现加强此论点：DINO 与 Projector 在 action R² 上无差异（0.712 vs 0.706, p=0.22），但 RSA 几何差异显著（0.388 vs 0.615）。说明 VL pretraining 的贡献在于 geometric alignment 而非 information content。\\n- **实验**: plan_012 CLIP-ViT control (P1)。区分 \\\"use VL-pretrained encoder\\\" vs \\\"use SigLIP specifically\\\"。\\n\\n### C3: LLM 对 action structure 的作用机制\\n- **问题**: LLM 到底做了什么？为什么 image token RSA 降低？\\n- **应对**: Functional probe 揭示机制——LLM 降解分布式 image token 表征（R² 0.706→0.683, bootstrap CI=[0.011, 0.037]）但通过 self-attention 将 action 信号 concentrate 到 readout token（R² 0.731）。这是 next-token prediction architecture 的自然行为：信息从 context tokens 流向 prediction position。Per-layer curve 的非单调模式（中间层部分恢复）与此一致。\\n- **实验**: ✅ plan_011 functional probe (Done) + plan_003 per-layer curve (Done)。\\n\\n### C4: Grant 2026 checkpoint 差异\\n- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。\\n- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。\\n\\n### C5: Practical implications / 功能验证\\n- **问题**: RSA alignment ≠ task performance。Practical implications?\\n- **应对**: ✅ plan_011 functional probe 完成——projector R²=0.706 vs LLM image_mean 0.683（gap=0.023, bootstrap CI=[0.011, 0.037], p=0.001）。LLM readout token R²=0.731 > projector（p=0.001）。Delta probe: projector < LLM 但不显著（CI 含 0）。三个建议：(1) Vision encoder pretraining 是 action info 关键；(2) Image-level tasks 用 projector output；(3) LLM 的价值在于 readout concentration。\\n- **实验**: ✅ plan_011 Done（含 bootstrap CI + DINO 三方对比）。\\n\\n### C6: 聚合方式伪影（已解决）\\n- **问题**: SigLIP 用 mean pooling，VLA 用 last token，比较不公平。\\n- **应对**: ✅ 已用 image_mean 聚合验证。VLA image_mean RSA=0.501，仍远低于 SigLIP 0.615（gap=0.114）。两种聚合方式结果一致（last_preaction 0.488 vs image_mean 0.501）。主文使用 image_mean 保证公平，last_preaction 放 supplementary。\\n\\n## Key Evidence Inventory\\n\\n| Evidence | Claim | Status |\\n|----------|-------|--------|\\n| SigLIP+Projector RSA=0.615 | C1, C2 | ✅ Done |\\n| Full VLA RSA ≈ 0.501 (image_mean, 4 conditions) | C2, C3 | ✅ Done |\\n| DINO RSA=0.388 | C1 | ✅ Done |\\n| 6 probing methods × 2 benchmarks: trained ≈ untrained | C3 | ✅ Done |\\n| Instruction ablation Δ=0.004 | C3 | ✅ Done |\\n| 2×2 matrix Bootstrap CI includes 0 | C3 | ✅ Done |\\n| Output head analysis: SigLIP+projector frozen | C1, C2 | ✅ Done |\\n| Per-layer RSA degradation curve | C2 | ✅ Done — non-monotonic, Proj→L1 primary drop |\\n| VLA image_mean RSA (aggregation robustness) | C2 | ✅ Done — 0.501 vs SigLIP 0.615, gap=0.114 |\\n| Bootstrap CI on training effect (image_mean) | C3 | ✅ Done — CI includes 0, invariance holds |\\n| Functional action probe: Proj 0.706 vs LLM img_mean 0.683 vs readout 0.731 | C1, C2 | ✅ Done — bootstrap CI=[0.011, 0.037], p=0.001 |\\n| DINO action probe on LIBERO-Goal | C1 | ✅ Done — R²=0.712, DINO ≈ Proj (p=0.22) |\\n| Action-delta probe: Proj 0.118 < LLM 0.122, CI includes 0 | C2 | ✅ Done — BELOW but not significant |\\n| No-inst image_mean RSA: trained 0.501 = with-inst, untrained 0.482 | C3 | ✅ Done |\\n| Untrained last_preaction: L32 R²=0.686 < projector 0.706 | C2, C3 | ✅ Done — redistribution is training-dependent (D034) |\\n| Untrained vs trained last_preaction bootstrap CI | C2, C3 | ✅ Done — Δ=0.045, CI=[0.032, 0.058], p<0.0001 |\\n| Random instruction control | C3 | 🔄 Running (plan_008, ETA ~01:00 UTC) |\\n| CLIP-ViT pretraining control | C1, C2 | 📋 P1 planned (plan_012) |\\n| CKA verification: ordering reversal — CKA untrained > trained > proj > DINO | C1, C2, C7 | ✅ Done — RSA-CKA dissociation (plan_009) |\\n| LIBERO-Spatial cross-benchmark | C1, C2, C3 | 📋 P2 planned (plan_010) |\\n\\n### C7: RSA vs CKA metric dependency — 排序反转（plan_009 已完成）\\n- **问题**: CKA 不仅缩小 gap，还**反转排序**。RSA: projector > trained > untrained > DINO。CKA: untrained > trained > projector > DINO。\\n- **数据**:\\n  - CKA vs actions: untrained L23 (0.089) > trained L23 (0.083) > projector (0.081) > DINO (0.066)\\n  - CKA per-layer trained image_mean: L0=0.081 **单调上升** to L32=0.098（与 RSA 的非单调模式不同）\\n  - CKA last_preaction: L32=0.127（最高，支持 redistribution — readout concentration）\\n  - CKA_RDM: last_preaction (0.290) > projector (0.257) ≈ trained (0.260) > DINO (0.241)（部分一致）\\n- **应对**: 论文正面讨论作为 finding。关键区分：\\n  - RSA 捕捉 **local geometric alignment**（representation 距离结构是否匹配 action 距离结构）→ LLM 降解\\n  - CKA 捕捉 **global structure preservation**（整体变换后结构是否保留）→ LLM 保留或改善\\n  - **Claim 2 必须明确限定为 \\\"geometric (RSA) degradation\\\"**，不能泛化为 \\\"representation quality degradation\\\"\\n  - CKA last_preaction 最高 (0.127) 与 redistribution narrative 一致\\n- **实验**: ✅ plan_009 Done。\\n\\n## Literature Positioning\\n\\n- **Grant et al. 2026**: Behavioral level \\\"visual pathway dominates\\\" → 我们 representational level 确认 + 定量组件分解\\n- **Fang 2025**: \\\"Fine-tuning erodes VLM reasoning\\\" → 我们发现 LLM step 本身（不只是 fine-tuning）就降低 visual structure\\n- **Hou 2026 (LangGap) / Fei 2025 (LIBERO-Plus)**: \\\"VLAs ignore language instructions\\\" → 我们从 representation level 解释 why：instruction text 对表征结构无实质影响\\n- **Haon et al. (CoRL 2025)**: Mechanistic interpretability + activation steering on OpenVLA — same venue, same model. Must discuss: their sparse semantic directions vs our geometric analysis are complementary views\\n- **Lu et al. 2025**: Linear probing on OpenVLA hidden layers >90% accuracy — methodologically closest, must differentiate (component decomposition vs layer probing)\\n- **Rizzardo et al. 2026**: Feature observability/controllability in VLAs\\n- **Swann et al. 2026**: SAE-based OpenVLA interpretability\\n- **Molinari et al. 2025**: Emergent world representations in OpenVLA\\n- **Karamcheti et al. 2024 (Prismatic)**: OpenVLA's architectural foundation, must cite\\n\", \"total_chars\": 11077, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "2a8dfd33-5716-43f2-9eb8-55355ad61ac7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — vla-ssd\\\\n\\\\n## Target Venue\\\\n- Primary: CoRL 2026\\\\n- Deadline: Abstract May 26, Paper May 29\\\\n- Format: 8 pages + references\\\\n\\\\n## Core Claims (3 条)\\\\n\\\\n1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.501, image_mean 聚合）和 standalone vision model（DINOv2 ρ=0.388）。\\\\n2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.706→0.683, p=0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.731 > projector 0.706, p=0.001），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector 0.706）。Readout concentration 是 learned behavior，不是架构固有属性。\\\\n3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。\\\\n\\\\n## Paper 主数值基准（image_mean 聚合，公平对比）\\\\n\\\\n| Model / Condition | RSA (image_mean) | Notes |\\\\n|---|---|---|\\\\n| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |\\\\n| VLA trained with-inst | 0.501 | Peak L23 |\\\\n| VLA untrained with-inst | 0.485 | Peak L23 |\\\\n| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |\\\\n| VLA untrained no-inst | 0.482 | Peak L29 |\\\\n| DINO-V2 | 0.388 | Vision-only baseline |\\\\n\\\\nlast_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。\\\\n\\\\n## Functional Probe 数值基准\\\\n\\\\n### Raw Action Prediction R²\\\\n\\\\n| Model | mean_R² | Notes |\\\\n|---|---|---|\\\\n| **SigLIP+Projector** | **0.706** | Vision encoder output |\\\\n| VLA Trained image_mean L19 | 0.683 | image tokens degraded — ✅ bootstrap CI=[0.011, 0.037], p=0.001 vs Proj |\\\\n| **Trained last_preaction L19** | **0.731** | readout concentration (p=0.001 vs projector) |\\\\n| Untrained image_mean L0 | 0.714 | Architecture-intrinsic |\\\\n| **Untrained last_preaction L32** | **0.686** | < projector (0.706) → redistribution requires training (D034) |\\\\n| DINO-V2 (LIBERO-Goal) | **0.712** | ✅ cls_token; DINO ≈ Proj (Δ=0.005, CI=[-0.008, 0.019], p=0.22, n.s.) |\\\\n\\\\n**Three-way ordering**: DINO (0.712) ≈ Projector (0.706) > LLM image_mean (0.683)\\\\n\\\\n**重要发现**: DINO 与 Projector 在 action decodability (R²) 上无显著差异，但 RSA 几何对齐差异显著（0.388 vs 0.615）。说明 action information 的 presence（probe 可解码）与 geometric alignment（表征空间结构匹配 action 空间结构）是不同维度。论文需区分这两个层面。\\\\n\\\\n### Action-Delta Prediction R²\\\\n\\\\n| Model | mean_R² | Notes |\\\\n|---|---|---|\\\\n| VLA Trained image_mean L14 | 0.122 | |\\\\n| SigLIP+Projector | 0.118 | ≈ LLM, CI includes 0 (p=0.04) |\\\\n| Untrained image_mean L0 | 0.117 | ≈ projector ≈ LLM |\\\\n| DINO (LIBERO-Goal) | 0.100 | action_delta probe from v2 |\\\\n| DINO (MVP-2 LIBERO-10) | 0.061 | 2× lower than projector/LLM |\\\\n\\\\n**Delta 维度结论**：三者几乎相同（~0.12），远 > DINO (0.06-0.10)。支持 vision encoder dominance（所有 action-delta info 追溯到 SigLIP）。Delta last_preaction 缺失（待补）。\\\\n\\\\n### 聚合口径依赖性（论文必须如实讨论）\\\\n\\\\n| Comparison | image_mean | last_preaction |\\\\n|---|---|---|\\\\n| Raw action: Proj vs LLM | Proj wins (+0.023, CI=[0.011, 0.037], p=0.001) | LLM wins (+0.025, p=0.001) |\\\\n| Delta: Proj vs LLM | ≈ tie (−0.003, CI includes 0) | TBD |\\\\n\\\\n主文用 image_mean（公平聚合），last_preaction 放 supplementary。但必须讨论聚合口径对结论的影响。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。\\\\n- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。\\\\n- **Our framing**: 首次对 VLA 进行系统性 representational + functional analysis——组件级分解 + per-layer probing + action prediction probes，定量揭示 action-relevant 结构的来源和 LLM 对其的变换。发现 vision encoder 是 action information 的通用源头（DINO ≈ SigLIP in R²，但 VL pretraining 赋予 geometric alignment）。LLM 降解分布式 image token 表征但通过**训练依赖的** attention 机制将信号聚合到 readout token——training 教会 routing 而非 creating new knowledge。\\\\n- **Headline result**: \\\\\\\"The frozen vision encoder provides action-relevant representations (RSA ρ=0.615, action probe R²=0.706) that the LLM degrades at the image-token level (R²→0.683) but reconcentrates into a readout token (R²=0.731). This reconcentration is training-dependent (untrained readout R²=0.686 < projector 0.706), while distributed representation structure remains training-invariant (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20). Language instructions affect neither.\\\\\\\"\\\\n- **⚠️ Remaining**: (1) ~~untrained vs trained last_preaction bootstrap CI~~ ✅ Done (Δ=0.045, CI=[0.032, 0.058], p<0.0001); (2) plan_008 random instruction results (RUNNING). 其余 pending 均已解决。\\\\n\\\\n## Anticipated Reviewer Concerns & Responses\\\\n\\\\n### C1: 单一 VLA 架构（OpenVLA）泛化性\\\\n- **应对**: Scope 明确限定为 \\\\\\\"OpenVLA-class architecture\\\\\\\"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。\\\\n- **实验**: 无需额外实验，Limitations 明确标注。\\\\n\\\\n### C2: SigLIP vs DINOv2 pretraining confound\\\\n- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。\\\\n- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。新发现加强此论点：DINO 与 Projector 在 action R² 上无差异（0.712 vs 0.706, p=0.22），但 RSA 几何差异显著（0.388 vs 0.615）。说明 VL pretraining 的贡献在于 geometric alignment 而非 information content。\\\\n- **实验**: plan_012 CLIP-ViT control (P1)。区分 \\\\\\\"use VL-pretrained encoder\\\\\\\" vs \\\\\\\"use SigLIP specifically\\\\\\\"。\\\\n\\\\n### C3: LLM 对 action structure 的作用机制\\\\n- **问题**: LLM 到底做了什么？为什么 image token RSA 降低？\\\\n- **应对**: Functional probe 揭示机制——LLM 降解分布式 image token 表征（R² 0.706→0.683, bootstrap CI=[0.011, 0.037]）但通过 self-attention 将 action 信号 concentrate 到 readout token（R² 0.731）。这是 next-token prediction architecture 的自然行为：信息从 context tokens 流向 prediction position。Per-layer curve 的非单调模式（中间层部分恢复）与此一致。\\\\n- **实验**: ✅ plan_011 functional probe (Done) + plan_003 per-layer curve (Done)。\\\\n\\\\n### C4: Grant 2026 checkpoint 差异\\\\n- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。\\\\n- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。\\\\n\\\\n### C5: Practical implications / 功能验证\\\\n- **问题**: RSA alignment ≠ task performance。Practical implications?\\\\n- **应对**: ✅ plan_011 functional probe 完成——projector R²=0.706 vs LLM image_mean 0.683（gap=0.023, bootstrap CI=[0.011, 0.037], p=0.001）。LLM readout token R²=0.731 > projector（p=0.001）。Delta probe: projector < LLM 但不显著（CI 含 0）。三个建议：(1) Vision encoder pretraining 是 action info 关键；(2) Image-level tasks 用 projector output；(3) LLM 的价值在于 readout concentration。\\\\n- **实验**: ✅ plan_011 Done（含 bootstrap CI + DINO 三方对比）。\\\\n\\\\n### C6: 聚合方式伪影（已解决）\\\\n- **问题**: SigLIP 用 mean pooling，VLA 用 last token，比较不公平。\\\\n- **应对**: ✅ 已用 image_mean 聚合验证。VLA image_mean RSA=0.501，仍远低于 SigLIP 0.615（gap=0.114）。两种聚合方式结果一致（last_preaction 0.488 vs image_mean 0.501）。主文使用 image_mean 保证公平，last_preaction 放 supplementary。\\\\n\\\\n## Key Evidence Inventory\\\\n\\\\n| Evidence | Claim | Status |\\\\n|----------|-------|--------|\\\\n| SigLIP+Projector RSA=0.615 | C1, C2 | ✅ Done |\\\\n| Full VLA RSA ≈ 0.501 (image_mean, 4 conditions) | C2, C3 | ✅ Done |\\\\n| DINO RSA=0.388 | C1 | ✅ Done |\\\\n| 6 probing methods × 2 benchmarks: trained ≈ untrained | C3 | ✅ Done |\\\\n| Instruction ablation Δ=0.004 | C3 | ✅ Done |\\\\n| 2×2 matrix Bootstrap CI includes 0 | C3 | ✅ Done |\\\\n| Output head analysis: SigLIP+projector frozen | C1, C2 | ✅ Done |\\\\n| Per-layer RSA degradation curve | C2 | ✅ Done — non-monotonic, Proj→L1 primary drop |\\\\n| VLA image_mean RSA (aggregation robustness) | C2 | ✅ Done — 0.501 vs SigLIP 0.615, gap=0.114 |\\\\n| Bootstrap CI on training effect (image_mean) | C3 | ✅ Done — CI includes 0, invariance holds |\\\\n| Functional action probe: Proj 0.706 vs LLM img_mean 0.683 vs readout 0.731 | C1, C2 | ✅ Done — bootstrap CI=[0.011, 0.037], p=0.001 |\\\\n| DINO action probe on LIBERO-Goal | C1 | ✅ Done — R²=0.712, DINO ≈ Proj (p=0.22) |\\\\n| Action-delta probe: Proj 0.118 < LLM 0.122, CI includes 0 | C2 | ✅ Done — BELOW but not significant |\\\\n| No-inst image_mean RSA: trained 0.501 = with-inst, untrained 0.482 | C3 | ✅ Done |\\\\n| Untrained last_preaction: L32 R²=0.686 < projector 0.706 | C2, C3 | ✅ Done — redistribution is training-dependent (D034) |\\\\n| Untrained vs trained last_preaction bootstrap CI | C2, C3 | ✅ Done — Δ=0.045, CI=[0.032, 0.058], p<0.0001 |\\\\n| Random instruction control | C3 | 🔄 Running (plan_008, ETA ~01:00 UTC) |\\\\n| CLIP-ViT pretraining control | C1, C2 | 📋 P1 planned (plan_012) |\\\\n| CKA verification: ordering reversal — CKA untrained > trained > proj > DINO | C1, C2, C7 | ✅ Done — RSA-CKA dissociation (plan_009) |\\\\n| LIBERO-Spatial cross-benchmark | C1, C2, C3 | 📋 P2 planned (plan_010) |\\\\n\\\\n### C7: RSA vs CKA metric dependency — 排序反转（plan_009 已完成）\\\\n- **问题**: CKA 不仅缩小 gap，还**反转排序**。RSA: projector > trained > untrained > DINO。CKA: untrained > trained > projector > DINO。\\\\n- **数据**:\\\\n  - CKA vs actions: untrained L23 (0.089) > trained L23 (0.083) > projector (0.081) > DINO (0.066)\\\\n  - CKA per-layer trained image_mean: L0=0.081 **单调上升** to L32=0.098（与 RSA 的非单调模式不同）\\\\n  - CKA last_preaction: L32=0.127（最高，支持 redistribution — readout concentration）\\\\n  - CKA_RDM: last_preaction (0.290) > projector (0.257) ≈ trained (0.260) > DINO (0.241)（部分一致）\\\\n- **应对**: 论文正面讨论作为 finding。关键区分：\\\\n  - RSA 捕捉 **local geometric alignment**（representation 距离结构是否匹配 action 距离结构）→ LLM 降解\\\\n  - CKA 捕捉 **global structure preservation**（整体变换后结构是否保留）→ LLM 保留或改善\\\\n  - **Claim 2 必须明确限定为 \\\\\\\"geometric (RSA) degradation\\\\\\\"**，不能泛化为 \\\\\\\"representation quality degradation\\\\\\\"\\\\n  - CKA last_preaction 最高 (0.127) 与 redistribution narrative 一致\\\\n- **实验**: ✅ plan_009 Done。\\\\n\\\\n## Literature Positioning\\\\n\\\\n- **Grant et al. 2026**: Behavioral level \\\\\\\"visual pathway dominates\\\\\\\" → 我们 representational level 确认 + 定量组件分解\\\\n- **Fang 2025**: \\\\\\\"Fine-tuning erodes VLM reasoning\\\\\\\" → 我们发现 LLM step 本身（不只是 fine-tuning）就降低 visual structure\\\\n- **Hou 2026 (LangGap) / Fei 2025 (LIBERO-Plus)**: \\\\\\\"VLAs ignore language instructions\\\\\\\" → 我们从 representation level 解释 why：instruction text 对表征结构无实质影响\\\\n- **Haon et al. (CoRL 2025)**: Mechanistic interpretability + activation steering on OpenVLA — same venue, same model. Must discuss: their sparse semantic directions vs our geometric analysis are complementary views\\\\n- **Lu et al. 2025**: Linear probing on OpenVLA hidden layers >90% accuracy — methodologically closest, must differentiate (component decomposition vs layer probing)\\\\n- **Rizzardo et al. 2026**: Feature observability/controllability in VLAs\\\\n- **Swann et al. 2026**: SAE-based OpenVLA interpretability\\\\n- **Molinari et al. 2025**: Emergent world representations in OpenVLA\\\\n- **Karamcheti et al. 2024 (Prismatic)**: OpenVLA's architectural foundation, must cite\\\\n\\\", \\\"total_chars\\\": 11077, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Claims (3 条)\\n\\n1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.501, image_mean 聚合）和 standalone vision model（DINOv2 ρ=0.388）。\\n2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.706→0.683, p=0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.731 > projector 0.706, p=0.001），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector 0.706）。Readout concentration 是 learned behavior，不是架构固有属性。\\n3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。\\n\\n## Paper 主数值基准（image_mean 聚合，公平对比）\\n\\n| Model / Condition | RSA (image_mean) | Notes |\\n|---|---|---|\\n| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |\\n| VLA trained with-inst | 0.501 | Peak L23 |\\n| VLA untrained with-inst | 0.485 | Peak L23 |\\n| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |\\n| VLA untrained no-inst | 0.482 | Peak L29 |\\n| DINO-V2 | 0.388 | Vision-only baseline |\\n\\nlast_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。\\n\\n## Functional Probe 数值基准\\n\\n### Raw Action Prediction R²\\n\\n| Model | mean_R² | Notes |\\n|---|---|---|\\n| **SigLIP+Projector** | **0.706** | Vision encoder output |\\n| VLA Trained image_mean L19 | 0.683 | image tokens degraded — ✅ bootstrap CI=[0.011, 0.037], p=0.001 vs Proj |\\n| **Trained last_preaction L19** | **0.731** | readout concentration (p=0.001 vs projector) |\\n| Untrained image_mean L0 | 0.714 | Architecture-intrinsic |\\n| **Untrained last_preaction L32** | **0.686** | < projector (0.706) → redistribution requires training (D034) |\\n| DINO-V2 (LIBERO-Goal) | **0.712** | ✅ cls_token; DINO ≈ Proj (Δ=0.005, CI=[-0.008, 0.019], p=0.22, n.s.) |\\n\\n**Three-way ordering**: DINO (0.712) ≈ Projector (0.706) > LLM image_mean (0.683)\\n\\n**重要发现**: DINO 与 Projector 在 action decodability (R²) 上无显著差异，但 RSA 几何对齐差异显著（0.388 vs 0.615）。说明 action information 的 presence（probe 可解码）与 geometric alignment（表征空间结构匹配 action 空间结构）是不同维度。论文需区分这两个层面。\\n\\n### Action-Delta Prediction R²\\n\\n| Model | mean_R² | Notes |\\n|---|---|---|\\n| VLA Trained image_mean L14 | 0.122 | |\\n| SigLIP+Projector | 0.118 | ≈ LLM, CI includes 0 (p=0.04) |\\n| Untrained image_mean L0 | 0.117 | ≈ projector ≈ LLM |\\n| DINO (LIBERO-Goal) | 0.100 | action_delta probe from v2 |\\n| DINO (MVP-2 LIBERO-10) | 0.061 | 2× lower than projector/LLM |\\n\\n**Delta 维度结论**：三者几乎相同（~0.12），远 > DINO (0.06-0.10)。支持 vision encoder dominance（所有 action-delta info 追溯到 SigLIP）。Delta last_preaction 缺失（待补）。\\n\\n### 聚合口径依赖性（论文必须如实讨论）\\n\\n| Comparison | image_mean | last_preaction |\\n|---|---|---|\\n| Raw action: Proj vs LLM | Proj wins (+0.023, CI=[0.011, 0.037], p=0.001) | LLM wins (+0.025, p=0.001) |\\n| Delta: Proj vs LLM | ≈ tie (−0.003, CI includes 0) | TBD |\\n\\n主文用 image_mean（公平聚合），last_preaction 放 supplementary。但必须讨论聚合口径对结论的影响。\\n\\n## Story Spine\\n\\n- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。\\n- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。\\n- **Our framing**: 首次对 VLA 进行系统性 representational + functional analysis——组件级分解 + per-layer probing + action prediction probes，定量揭示 action-relevant 结构的来源和 LLM 对其的变换。发现 vision encoder 是 action information 的通用源头（DINO ≈ SigLIP in R²，但 VL pretraining 赋予 geometric alignment）。LLM 降解分布式 image token 表征但通过**训练依赖的** attention 机制将信号聚合到 readout token——training 教会 routing 而非 creating new knowledge。\\n- **Headline result**: \\\"The frozen vision encoder provides action-relevant representations (RSA ρ=0.615, action probe R²=0.706) that the LLM degrades at the image-token level (R²→0.683) but reconcentrates into a readout token (R²=0.731). This reconcentration is training-dependent (untrained readout R²=0.686 < projector 0.706), while distributed representation structure remains training-invariant (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20). Language instructions affect neither.\\\"\\n- **⚠️ Remaining**: (1) ~~untrained vs trained last_preaction bootstrap CI~~ ✅ Done (Δ=0.045, CI=[0.032, 0.058], p<0.0001); (2) plan_008 random instruction results (RUNNING). 其余 pending 均已解决。\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n### C1: 单一 VLA 架构（OpenVLA）泛化性\\n- **应对**: Scope 明确限定为 \\\"OpenVLA-class architecture\\\"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。\\n- **实验**: 无需额外实验，Limitations 明确标注。\\n\\n### C2: SigLIP vs DINOv2 pretraining confound\\n- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。\\n- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。新发现加强此论点：DINO 与 Projector 在 action R² 上无差异（0.712 vs 0.706, p=0.22），但 RSA 几何差异显著（0.388 vs 0.615）。说明 VL pretraining 的贡献在于 geometric alignment 而非 information content。\\n- **实验**: plan_012 CLIP-ViT control (P1)。区分 \\\"use VL-pretrained encoder\\\" vs \\\"use SigLIP specifically\\\"。\\n\\n### C3: LLM 对 action structure 的作用机制\\n- **问题**: LLM 到底做了什么？为什么 image token RSA 降低？\\n- **应对**: Functional probe 揭示机制——LLM 降解分布式 image token 表征（R² 0.706→0.683, bootstrap CI=[0.011, 0.037]）但通过 self-attention 将 action 信号 concentrate 到 readout token（R² 0.731）。这是 next-token prediction architecture 的自然行为：信息从 context tokens 流向 prediction position。Per-layer curve 的非单调模式（中间层部分恢复）与此一致。\\n- **实验**: ✅ plan_011 functional probe (Done) + plan_003 per-layer curve (Done)。\\n\\n### C4: Grant 2026 checkpoint 差异\\n- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。\\n- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。\\n\\n### C5: Practical implications / 功能验证\\n- **问题**: RSA alignment ≠ task performance。Practical implications?\\n- **应对**: ✅ plan_011 functional probe 完成——projector R²=0.706 vs LLM image_mean 0.683（gap=0.023, bootstrap CI=[0.011, 0.037], p=0.001）。LLM readout token R²=0.731 > projector（p=0.001）。Delta probe: projector < LLM 但不显著（CI 含 0）。三个建议：(1) Vision encoder pretraining 是 action info 关键；(2) Image-level tasks 用 projector output；(3) LLM 的价值在于 readout concentration。\\n- **实验**: ✅ plan_011 Done（含 bootstrap CI + DINO 三方对比）。\\n\\n### C6: 聚合方式伪影（已解决）\\n- **问题**: SigLIP 用 mean pooling，VLA 用 last token，比较不公平。\\n- **应对**: ✅ 已用 image_mean 聚合验证。VLA image_mean RSA=0.501，仍远低于 SigLIP 0.615（gap=0.114）。两种聚合方式结果一致（last_preaction 0.488 vs image_mean 0.501）。主文使用 image_mean 保证公平，last_preaction 放 supplementary。\\n\\n## Key Evidence Inventory\\n\\n| Evidence | Claim | Status |\\n|----------|-------|--------|\\n| SigLIP+Projector RSA=0.615 | C1, C2 | ✅ Done |\\n| Full VLA RSA ≈ 0.501 (image_mean, 4 conditions) | C2, C3 | ✅ Done |\\n| DINO RSA=0.388 | C1 | ✅ Done |\\n| 6 probing methods × 2 benchmarks: trained ≈ untrained | C3 | ✅ Done |\\n| Instruction ablation Δ=0.004 | C3 | ✅ Done |\\n| 2×2 matrix Bootstrap CI includes 0 | C3 | ✅ Done |\\n| Output head analysis: SigLIP+projector frozen | C1, C2 | ✅ Done |\\n| Per-layer RSA degradation curve | C2 | ✅ Done — non-monotonic, Proj→L1 primary drop |\\n| VLA image_mean RSA (aggregation robustness) | C2 | ✅ Done — 0.501 vs SigLIP 0.615, gap=0.114 |\\n| Bootstrap CI on training effect (image_mean) | C3 | ✅ Done — CI includes 0, invariance holds |\\n| Functional action probe: Proj 0.706 vs LLM img_mean 0.683 vs readout 0.731 | C1, C2 | ✅ Done — bootstrap CI=[0.011, 0.037], p=0.001 |\\n| DINO action probe on LIBERO-Goal | C1 | ✅ Done — R²=0.712, DINO ≈ Proj (p=0.22) |\\n| Action-delta probe: Proj 0.118 < LLM 0.122, CI includes 0 | C2 | ✅ Done — BELOW but not significant |\\n| No-inst image_mean RSA: trained 0.501 = with-inst, untrained 0.482 | C3 | ✅ Done |\\n| Untrained last_preaction: L32 R²=0.686 < projector 0.706 | C2, C3 | ✅ Done — redistribution is training-dependent (D034) |\\n| Untrained vs trained last_preaction bootstrap CI | C2, C3 | ✅ Done — Δ=0.045, CI=[0.032, 0.058], p<0.0001 |\\n| Random instruction control | C3 | 🔄 Running (plan_008, ETA ~01:00 UTC) |\\n| CLIP-ViT pretraining control | C1, C2 | 📋 P1 planned (plan_012) |\\n| CKA verification: ordering reversal — CKA untrained > trained > proj > DINO | C1, C2, C7 | ✅ Done — RSA-CKA dissociation (plan_009) |\\n| LIBERO-Spatial cross-benchmark | C1, C2, C3 | 📋 P2 planned (plan_010) |\\n\\n### C7: RSA vs CKA metric dependency — 排序反转（plan_009 已完成）\\n- **问题**: CKA 不仅缩小 gap，还**反转排序**。RSA: projector > trained > untrained > DINO。CKA: untrained > trained > projector > DINO。\\n- **数据**:\\n  - CKA vs actions: untrained L23 (0.089) > trained L23 (0.083) > projector (0.081) > DINO (0.066)\\n  - CKA per-layer trained image_mean: L0=0.081 **单调上升** to L32=0.098（与 RSA 的非单调模式不同）\\n  - CKA last_preaction: L32=0.127（最高，支持 redistribution — readout concentration）\\n  - CKA_RDM: last_preaction (0.290) > projector (0.257) ≈ trained (0.260) > DINO (0.241)（部分一致）\\n- **应对**: 论文正面讨论作为 finding。关键区分：\\n  - RSA 捕捉 **local geometric alignment**（representation 距离结构是否匹配 action 距离结构）→ LLM 降解\\n  - CKA 捕捉 **global structure preservation**（整体变换后结构是否保留）→ LLM 保留或改善\\n  - **Claim 2 必须明确限定为 \\\"geometric (RSA) degradation\\\"**，不能泛化为 \\\"representation quality degradation\\\"\\n  - CKA last_preaction 最高 (0.127) 与 redistribution narrative 一致\\n- **实验**: ✅ plan_009 Done。\\n\\n## Literature Positioning\\n\\n- **Grant et al. 2026**: Behavioral level \\\"visual pathway dominates\\\" → 我们 representational level 确认 + 定量组件分解\\n- **Fang 2025**: \\\"Fine-tuning erodes VLM reasoning\\\" → 我们发现 LLM step 本身（不只是 fine-tuning）就降低 visual structure\\n- **Hou 2026 (LangGap) / Fei 2025 (LIBERO-Plus)**: \\\"VLAs ignore language instructions\\\" → 我们从 representation level 解释 why：instruction text 对表征结构无实质影响\\n- **Haon et al. (CoRL 2025)**: Mechanistic interpretability + activation steering on OpenVLA — same venue, same model. Must discuss: their sparse semantic directions vs our geometric analysis are complementary views\\n- **Lu et al. 2025**: Linear probing on OpenVLA hidden layers >90% accuracy — methodologically closest, must differentiate (component decomposition vs layer probing)\\n- **Rizzardo et al. 2026**: Feature observability/controllability in VLAs\\n- **Swann et al. 2026**: SAE-based OpenVLA interpretability\\n- **Molinari et al. 2025**: Emergent world representations in OpenVLA\\n- **Karamcheti et al. 2024 (Prismatic)**: OpenVLA's architectural foundation, must cite\\n\", \"total_chars\": 11077, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H8rpSGQrkMmxNbFHdqaNXe`</summary>

```json
{
  "project": "vla-ssd",
  "file": "ROADMAP.md",
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
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "4ba727f2-6f2a-45cd-9981-9caa9264379b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwxDD7cKnyMjTQw4UXp6TV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 23787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
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

_source line 11 · 2026-05-16T00:30:06.289Z_

<details><summary>↩ Tool result · `toolu_01H8rpSGQrkMmxNbFHdqaNXe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-16 00:14 UTC | 更新原因: Sync with D033/D034, CKA results, plan_008 running, updated Claims\\n\\n## 核心方向\\nVLA 中 action-relevant 表征的来源与 LLM 的 redistribution 机制。三层发现：(1) Vision encoder 是 action info 的通用源头，VL pretraining 赋予 geometric alignment 而非额外 predictive content；(2) LLM 降解分布式 image token 几何结构（RSA）但保留全局结构（CKA），通过训练依赖的 attention 将信号 concentrate 到 readout token；(3) Training 教会 routing（readout concentration），而非 creating new knowledge（distributed structure invariant）。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research phase, post-D034**。三条 Claim 完整成型，所有 P0 实验完成。等待：(1) untrained vs trained last_preaction bootstrap CI（已派 Agent）；(2) plan_008 random instruction control（RUNNING）。两者完成后 re-dream 验证新 framing，达标则启动 Paper Agent。\\n\\n## 已完成核心实验\\n- ✅ plan_001-007: RSA 组件分解 + 2×2 matrix + per-layer curve + instruction ablation\\n- ✅ plan_011: Functional action probe — Proj R²=0.706 > LLM img_mean 0.683 (p=0.001); readout 0.731 > Proj (p=0.001)\\n- ✅ plan_009: CKA verification — ordering reversal vs RSA (partial). RSA-CKA dissociation 成为新 finding\\n- ✅ D033: DINO R²=0.712 ≈ Projector 0.706 (p=0.22) — geometric-functional dissociation\\n- ✅ D034: Untrained readout R²=0.686 < projector 0.706 — redistribution is training-dependent\\n- ✅ Aggregation robustness: image_mean RSA 0.501 vs SigLIP 0.615, gap=0.114\\n- ✅ Bootstrap CI: training effect on image_mean CI includes 0, distributed structure invariant\\n\\n## 近期任务\\n- [ ] Untrained vs trained last_preaction bootstrap CI（Agent 已派，分钟级）\\n- [ ] plan_008 random instruction control 结果分析（RUNNING，等完成）\\n- [ ] Re-dream with updated framing（上述两项完成后立即触发）\\n- [ ] Paper Agent Full Draft（re-dream 达标后启动）\\n- [ ] plan_012 CLIP-ViT control（P1，Paper Agent 启动后并行）\\n\\n## GPU 预算\\nwestd-19183: 2× GPU（plan_008 占用中）\\n剩余预算: ~7 GPU·h\\n\\n## 关键里程碑\\n| 日期 | 事件 |\\n|------|------|\\n| 5/15 | MVP PASS → Dream → D030 → plan_011 PASS → D031 redistribution |\\n| 5/16 | D033 geometric-functional dissociation, D034 training-dependent redistribution, plan_009 CKA done |\\n| 5/16 | **paper_framing.md 三条 Claim 定稿** |\\n| 5/16-17 | bootstrap CI + plan_008 → re-dream |\\n| 5/17-18 | Paper Agent Full Draft |\\n| 5/26 | CoRL abstract DDL |\\n| 5/29 | CoRL paper DDL |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D034 | 2026-05-16 | Untrained last_preaction R²=0.689 < projector 0.70 | p0_functional_probe_v2 |\\n| D033 | 2026-05-15 | DINO R²=0.712 ≈ Projector R²=0.706 (p=0.22) — Clai | p0_functional_probe_v2 |\\n| D032 | 2026-05-15 | Confirm Option A framing (\\\"LLM routes, not creates | p0_functional_action_probe, p0_functional_action_delta_probe |\\n| D031 | 2026-05-15 | Claim 2 framing pivot: \\\"LLM degrades\\\" → \\\"LLM redis | p0_functional_action_probe |\\n| D030 | 2026-05-15 | D030: Dream 三档均低于 acceptance（best borderline rejec | d027_siglip_only_rsa, mvp2_action_trained, mvp2_action_dino |\\n| D029 | 2026-05-15 | D029: Claim 2 聚合伪影排除。VLA image_mean RSA=0.501 仍远低于 | d027_siglip_only_rsa, plan_003_perlayer_degradation, d027_trained_no_inst_rsa |\\n| D028 | 2026-05-15 | D028: SigLIP-only RSA smoking gun PASS (0.615 >> 0 | d027_siglip_only_rsa, d027_trained_no_inst_rsa, d021_instruction_ablation |\\n| D027 | 2026-05-15 | D027: Instruction Ablation FAIL — Option B 死亡，回退 O | d021_instruction_ablation, d021_output_head_analysis, lg_rsa_analysis |\\n| D026 | 2026-05-15 | D025: Output head analysis FAIL — shallow adaptati | d021_output_head_analysis, d021_instruction_ablation |\\n| D025 | 2026-05-15 | D024: Instruction ablation gate 从绝对阈值改为 DINO-ancho | d021_instruction_ablation |\\n\\n\\n\", \"total_chars\": 3504, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "b420ea72-912c-4040-ad5f-80c42b502f48",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\\\", \\\"content\\\": \\\"# vla-ssd — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-16 00:14 UTC | 更新原因: Sync with D033/D034, CKA results, plan_008 running, updated Claims\\\\n\\\\n## 核心方向\\\\nVLA 中 action-relevant 表征的来源与 LLM 的 redistribution 机制。三层发现：(1) Vision encoder 是 action info 的通用源头，VL pretraining 赋予 geometric alignment 而非额外 predictive content；(2) LLM 降解分布式 image token 几何结构（RSA）但保留全局结构（CKA），通过训练依赖的 attention 将信号 concentrate 到 readout token；(3) Training 教会 routing（readout concentration），而非 creating new knowledge（distributed structure invariant）。详见 paper_framing.md。\\\\n\\\\n## 当前阶段\\\\n**Research phase, post-D034**。三条 Claim 完整成型，所有 P0 实验完成。等待：(1) untrained vs trained last_preaction bootstrap CI（已派 Agent）；(2) plan_008 random instruction control（RUNNING）。两者完成后 re-dream 验证新 framing，达标则启动 Paper Agent。\\\\n\\\\n## 已完成核心实验\\\\n- ✅ plan_001-007: RSA 组件分解 + 2×2 matrix + per-layer curve + instruction ablation\\\\n- ✅ plan_011: Functional action probe — Proj R²=0.706 > LLM img_mean 0.683 (p=0.001); readout 0.731 > Proj (p=0.001)\\\\n- ✅ plan_009: CKA verification — ordering reversal vs RSA (partial). RSA-CKA dissociation 成为新 finding\\\\n- ✅ D033: DINO R²=0.712 ≈ Projector 0.706 (p=0.22) — geometric-functional dissociation\\\\n- ✅ D034: Untrained readout R²=0.686 < projector 0.706 — redistribution is training-dependent\\\\n- ✅ Aggregation robustness: image_mean RSA 0.501 vs SigLIP 0.615, gap=0.114\\\\n- ✅ Bootstrap CI: training effect on image_mean CI includes 0, distributed structure invariant\\\\n\\\\n## 近期任务\\\\n- [ ] Untrained vs trained last_preaction bootstrap CI（Agent 已派，分钟级）\\\\n- [ ] plan_008 random instruction control 结果分析（RUNNING，等完成）\\\\n- [ ] Re-dream with updated framing（上述两项完成后立即触发）\\\\n- [ ] Paper Agent Full Draft（re-dream 达标后启动）\\\\n- [ ] plan_012 CLIP-ViT control（P1，Paper Agent 启动后并行）\\\\n\\\\n## GPU 预算\\\\nwestd-19183: 2× GPU（plan_008 占用中）\\\\n剩余预算: ~7 GPU·h\\\\n\\\\n## 关键里程碑\\\\n| 日期 | 事件 |\\\\n|------|------|\\\\n| 5/15 | MVP PASS → Dream → D030 → plan_011 PASS → D031 redistribution |\\\\n| 5/16 | D033 geometric-functional dissociation, D034 training-dependent redistribution, plan_009 CKA done |\\\\n| 5/16 | **paper_framing.md 三条 Claim 定稿** |\\\\n| 5/16-17 | bootstrap CI + plan_008 → re-dream |\\\\n| 5/17-18 | Paper Agent Full Draft |\\\\n| 5/26 | CoRL abstract DDL |\\\\n| 5/29 | CoRL paper DDL |\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D034 | 2026-05-16 | Untrained last_preaction R²=0.689 < projector 0.70 | p0_functional_probe_v2 |\\\\n| D033 | 2026-05-15 | DINO R²=0.712 ≈ Projector R²=0.706 (p=0.22) — Clai | p0_functional_probe_v2 |\\\\n| D032 | 2026-05-15 | Confirm Option A framing (\\\\\\\"LLM routes, not creates | p0_functional_action_probe, p0_functional_action_delta_probe |\\\\n| D031 | 2026-05-15 | Claim 2 framing pivot: \\\\\\\"LLM degrades\\\\\\\" → \\\\\\\"LLM redis | p0_functional_action_probe |\\\\n| D030 | 2026-05-15 | D030: Dream 三档均低于 acceptance（best borderline rejec | d027_siglip_only_rsa, mvp2_action_trained, mvp2_action_dino |\\\\n| D029 | 2026-05-15 | D029: Claim 2 聚合伪影排除。VLA image_mean RSA=0.501 仍远低于 | d027_siglip_only_rsa, plan_003_perlayer_degradation, d027_trained_no_inst_rsa |\\\\n| D028 | 2026-05-15 | D028: SigLIP-only RSA smoking gun PASS (0.615 >> 0 | d027_siglip_only_rsa, d027_trained_no_inst_rsa, d021_instruction_ablation |\\\\n| D027 | 2026-05-15 | D027: Instruction Ablation FAIL — Option B 死亡，回退 O | d021_instruction_ablation, d021_output_head_analysis, lg_rsa_analysis |\\\\n| D026 | 2026-05-15 | D025: Output head analysis FAIL — shallow adaptati | d021_output_head_analysis, d021_instruction_ablation |\\\\n| D025 | 2026-05-15 | D024: Instruction ablation gate 从绝对阈值改为 DINO-ancho | d021_instruction_ablation |\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 3504, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-16 00:14 UTC | 更新原因: Sync with D033/D034, CKA results, plan_008 running, updated Claims\\n\\n## 核心方向\\nVLA 中 action-relevant 表征的来源与 LLM 的 redistribution 机制。三层发现：(1) Vision encoder 是 action info 的通用源头，VL pretraining 赋予 geometric alignment 而非额外 predictive content；(2) LLM 降解分布式 image token 几何结构（RSA）但保留全局结构（CKA），通过训练依赖的 attention 将信号 concentrate 到 readout token；(3) Training 教会 routing（readout concentration），而非 creating new knowledge（distributed structure invariant）。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research phase, post-D034**。三条 Claim 完整成型，所有 P0 实验完成。等待：(1) untrained vs trained last_preaction bootstrap CI（已派 Agent）；(2) plan_008 random instruction control（RUNNING）。两者完成后 re-dream 验证新 framing，达标则启动 Paper Agent。\\n\\n## 已完成核心实验\\n- ✅ plan_001-007: RSA 组件分解 + 2×2 matrix + per-layer curve + instruction ablation\\n- ✅ plan_011: Functional action probe — Proj R²=0.706 > LLM img_mean 0.683 (p=0.001); readout 0.731 > Proj (p=0.001)\\n- ✅ plan_009: CKA verification — ordering reversal vs RSA (partial). RSA-CKA dissociation 成为新 finding\\n- ✅ D033: DINO R²=0.712 ≈ Projector 0.706 (p=0.22) — geometric-functional dissociation\\n- ✅ D034: Untrained readout R²=0.686 < projector 0.706 — redistribution is training-dependent\\n- ✅ Aggregation robustness: image_mean RSA 0.501 vs SigLIP 0.615, gap=0.114\\n- ✅ Bootstrap CI: training effect on image_mean CI includes 0, distributed structure invariant\\n\\n## 近期任务\\n- [ ] Untrained vs trained last_preaction bootstrap CI（Agent 已派，分钟级）\\n- [ ] plan_008 random instruction control 结果分析（RUNNING，等完成）\\n- [ ] Re-dream with updated framing（上述两项完成后立即触发）\\n- [ ] Paper Agent Full Draft（re-dream 达标后启动）\\n- [ ] plan_012 CLIP-ViT control（P1，Paper Agent 启动后并行）\\n\\n## GPU 预算\\nwestd-19183: 2× GPU（plan_008 占用中）\\n剩余预算: ~7 GPU·h\\n\\n## 关键里程碑\\n| 日期 | 事件 |\\n|------|------|\\n| 5/15 | MVP PASS → Dream → D030 → plan_011 PASS → D031 redistribution |\\n| 5/16 | D033 geometric-functional dissociation, D034 training-dependent redistribution, plan_009 CKA done |\\n| 5/16 | **paper_framing.md 三条 Claim 定稿** |\\n| 5/16-17 | bootstrap CI + plan_008 → re-dream |\\n| 5/17-18 | Paper Agent Full Draft |\\n| 5/26 | CoRL abstract DDL |\\n| 5/29 | CoRL paper DDL |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D034 | 2026-05-16 | Untrained last_preaction R²=0.689 < projector 0.70 | p0_functional_probe_v2 |\\n| D033 | 2026-05-15 | DINO R²=0.712 ≈ Projector R²=0.706 (p=0.22) — Clai | p0_functional_probe_v2 |\\n| D032 | 2026-05-15 | Confirm Option A framing (\\\"LLM routes, not creates | p0_functional_action_probe, p0_functional_action_delta_probe |\\n| D031 | 2026-05-15 | Claim 2 framing pivot: \\\"LLM degrades\\\" → \\\"LLM redis | p0_functional_action_probe |\\n| D030 | 2026-05-15 | D030: Dream 三档均低于 acceptance（best borderline rejec | d027_siglip_only_rsa, mvp2_action_trained, mvp2_action_dino |\\n| D029 | 2026-05-15 | D029: Claim 2 聚合伪影排除。VLA image_mean RSA=0.501 仍远低于 | d027_siglip_only_rsa, plan_003_perlayer_degradation, d027_trained_no_inst_rsa |\\n| D028 | 2026-05-15 | D028: SigLIP-only RSA smoking gun PASS (0.615 >> 0 | d027_siglip_only_rsa, d027_trained_no_inst_rsa, d021_instruction_ablation |\\n| D027 | 2026-05-15 | D027: Instruction Ablation FAIL — Option B 死亡，回退 O | d021_instruction_ablation, d021_output_head_analysis, lg_rsa_analysis |\\n| D026 | 2026-05-15 | D025: Output head analysis FAIL — shallow adaptati | d021_output_head_analysis, d021_instruction_ablation |\\n| D025 | 2026-05-15 | D024: Instruction ablation gate 从绝对阈值改为 DINO-ancho | d021_instruction_ablation |\\n\\n\\n\", \"total_chars\": 3504, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GY7AmUCXDdmT2Sf1YxRhK1`</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md",
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
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "785a939a-0cd0-4fcc-afb4-164ac1385b52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwxDD7cKnyMjTQw4UXp6TV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 23787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
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

_source line 13 · 2026-05-16T00:30:06.755Z_

<details><summary>↩ Tool result · `toolu_01GY7AmUCXDdmT2Sf1YxRhK1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## CKA 指标依赖性发现（2026-05-16，plan_009 = success）\\n\\n**CKA 部分验证 RSA，但 projector vs trained 排序是指标依赖的。**\\n\\n| 发现 | RSA | RDM CKA | 一致？ |\\n|------|-----|---------|--------|\\n| DINO 最弱 | ✓ (0.388) | ✓ (0.241) | **Yes** |\\n| last_preaction >> image_mean | ✓ | ✓ (0.290 vs 0.260) | **Yes** |\\n| Projector > Trained | 0.615 vs 0.501 | 0.257 ≈ 0.260 | **No** — gap 压缩 |\\n| Per-layer 趋势 later > earlier | ✓ | ✓ | **Yes** |\\n\\n**论文语言约束**：projector \\\"dominance\\\" 只在 RSA 下显著，CKA 下 projector ≈ trained。论文应呈 RSA 为 primary，CKA 为 supplementary，并讨论 metric sensitivity（C7 应对方案）。Linear CKA 因维度不匹配（4096-D vs 7-D）不可靠，不作证据。\\n\\n## ⚠️ Functional Probe 分离发现（2026-05-15，p0_functional_action_probe = negative）\\n\\n**RSA 与 functional probe 发生分离——这是论文 Claim 2 的关键转折点。**\\n\\n| 度量 | Projector | LLM image_mean L19 | LLM last_preaction L19 |\\n|------|-----------|--------------------|-----------------------|\\n| RSA | 0.615 | ~0.49 | ~0.49 |\\n| Action R² | **0.706** | 0.683 | **0.731** |\\n\\n**机制**：LLM self-attention 将 action-relevant 信息从分布式 visual tokens **重新路由**到 output position (last_preaction)。visual tokens 的几何结构 (RSA) 和功能性 (image_mean R²) 都降低了，但 action token 集中了更多信息。\\n\\n**关键数字**：Projector 已提供 LLM 96.6% 的 functional capacity (0.706/0.731)。LLM 边际贡献仅 +3.5%。\\n\\n**对 Claim 2 的影响**：不能再说 \\\"LLM degrades\\\"，需精炼为 \\\"LLM redistributes\\\"（推荐 Option A）。Framing 提案已提交 Director，D032 确认 Option A 锁定。\\n\\n## SMOKING GUN 确认：SigLIP+Projector RSA = 0.6153（2026-05-15）\\n\\n**d027_siglip_only_rsa 结果**: SigLIP+projector 直接输出（不过 LLM）的 RSA = 0.6153 [95% CI: 0.5257, 0.6954]。\\n\\n**关键发现：LLM 降低 action alignment（不是 passthrough）**：\\n- SigLIP+projector: **0.6153**\\n- Full VLA（任何条件）: ~0.48-0.49\\n- DINO: 0.388\\n\\nLLM 不仅没增强 action-relevant structure，反而将 RSA 从 0.615 降到 ~0.488（约 20% 下降）。这比 \\\"passthrough\\\" 更强——是 \\\"degradation\\\"。\\n\\n**机制解释**: SigLIP image-text 预训练产生的 visual features 天然具有强 action-relevant 结构。Projector 保持这一结构（cos_sim=1.0 frozen）。LLM 的高维 token mixing 稀释了这种结构（trained 和 untrained LLM 稀释程度一致）。\\n\\n## Per-Layer Degradation Curve 发现（2026-05-15）\\n\\n**plan_003_perlayer_degradation 结果**：降解非单调，集中在 embedding interface。\\n\\n**关键机制洞察**：\\n- Proj→L1 是最大 single-step drop（0.13–0.25，~20–40%），token embedding 是 degradation bottleneck\\n- L0（embedding layer）是异常值：trained 模型 RSA≈0，结构从 L1 才开始恢复\\n- 中间层有 partial recovery（non-monotonic），LLM 不是 \\\"progressive degrader\\\"\\n- **no-inst trained 独特模式**：唯一呈 L1→L30 持续上升的条件（peak at L30），training 在无 instruction 时让 LLM 逐层积累 action 信号。其余 3 个条件均 non-monotonic\\n- 总降解幅度 ~0.13：best LLM layer 仍比 projector 低 ~0.127\\n\\n## 完整 2×2 Matrix + SigLIP-only（2026-05-15）\\n\\n| 条件 | RSA | 备注 |\\n|------|-----|------|\\n| **SigLIP+Projector (no LLM)** | **0.6153** | smoking gun |\\n| Trained with-inst | 0.4876 | L9 peak |\\n| Trained no-inst | 0.489 | L30 peak |\\n| Untrained with-inst | 0.4846 | L12 peak |\\n| Untrained no-inst | 0.4802 | — |\\n| DINO | 0.388 | — |\\n\\n**结论**: 所有 4 个 full VLA 条件收敛在 0.48-0.49 band。SigLIP-only 显著高于 full VLA。Training 和 instruction 均无 meaningful effect。\\n\\n## Bootstrap CI on Training Effect（2026-05-15）\\n\\nimage_mean Δ=+0.021, CI=[−0.031, +0.064], p=0.20; last_preaction Δ=+0.008, CI=[−0.040, +0.056], p=0.37。**两个 CI 都包含 0**，Claim 3 invariance 成立。\\n\\n## Instruction Ablation FAIL — Option B 被否证（2026-05-15）\\n\\n**d021_instruction_ablation 结果**: no-inst untrained RSA = 0.4802 ≈ with-inst 0.4846（Δ=0.0044 << 0.10 阈值）。\\n\\n## Output Head Analysis 发现（2026-05-15，negative）\\n\\nVision backbone + Projector 在 trained 和 untrained 之间完全一致（rel_change=0, cos_sim=1.0）。Shallow adaptation FAIL。**Caveat**: trained vs untrained 比较的是 pretrained Llama + fine-tune vs random init。\\n\\n## 文献关键发现\\n\\n14 篇论文确认 vision encoder dominance 是已知现象（behavioral level）。我们在 representation level 发现同一模式，是独特贡献。Grant 2026: LIBERO-Goal 中 language 贡献关键（behavioral level），OFT checkpoint。\\n\\n## Novelty Gap\\n\\n| 工作 | 做了什么 | 没做什么 |\\n|------|---------|---------|\\n| Grant et al. 2026 | Behavioral intervention, \\\"encoded but not used\\\" | 无 trained vs untrained 对比 |\\n| Swann/Buurmeijer | SAE interpretability on OpenVLA+LIBERO | 无 language features 分析 |\\n| LIBERO-CF | Counterfactual behavioral benchmark | 无 representation analysis |\\n\\n## 方向 Pivot 历史\\n\\nMVP-1 Temporal Distance → G2 FAIL → MVP-2 Action Prediction → G2 FAIL → Action-Delta → G3 FAIL → D015 Pivot LIBERO-Goal → D018 Goal Classification → G3 FAIL → D019 RSA → G2 FAIL → D021 Instruction Ablation (FAIL) + Output Head (negative) → D027 Option A2 锁定 → **SigLIP-only SMOKING GUN PASS → MVP Gate 通过** → **Functional Probe: RSA-functional dissociation (negative for Claim 2 \\\"degrades\\\")** → **D031 Redistribution pivot → D032 Option A 锁定**\\n\\n## 技术约束\\n\\n- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）\\n- D017: 统一用 LIBERO-10 fine-tuned checkpoint（LIBERO-Goal 是 OOD 测试）\\n- Token 聚合：Primary = last pre-action token\\n- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/\\n- **分析 Worker 不得覆盖 spec 字段**\\n- **服务器无外网**：AutoProcessor/HF 操作必须 `local_files_only=True`\\n- **Instruction ablation bug**: `if args.task_instruction:` 对空字符串返回 False，已修复\\n\", \"total_chars\": 4867, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "6ef23acb-d117-44ec-991d-5003578e6e5f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\\\", \\\"content\\\": \\\"# VLA-SSD Project Memory\\\\n\\\\n## CKA 指标依赖性发现（2026-05-16，plan_009 = success）\\\\n\\\\n**CKA 部分验证 RSA，但 projector vs trained 排序是指标依赖的。**\\\\n\\\\n| 发现 | RSA | RDM CKA | 一致？ |\\\\n|------|-----|---------|--------|\\\\n| DINO 最弱 | ✓ (0.388) | ✓ (0.241) | **Yes** |\\\\n| last_preaction >> image_mean | ✓ | ✓ (0.290 vs 0.260) | **Yes** |\\\\n| Projector > Trained | 0.615 vs 0.501 | 0.257 ≈ 0.260 | **No** — gap 压缩 |\\\\n| Per-layer 趋势 later > earlier | ✓ | ✓ | **Yes** |\\\\n\\\\n**论文语言约束**：projector \\\\\\\"dominance\\\\\\\" 只在 RSA 下显著，CKA 下 projector ≈ trained。论文应呈 RSA 为 primary，CKA 为 supplementary，并讨论 metric sensitivity（C7 应对方案）。Linear CKA 因维度不匹配（4096-D vs 7-D）不可靠，不作证据。\\\\n\\\\n## ⚠️ Functional Probe 分离发现（2026-05-15，p0_functional_action_probe = negative）\\\\n\\\\n**RSA 与 functional probe 发生分离——这是论文 Claim 2 的关键转折点。**\\\\n\\\\n| 度量 | Projector | LLM image_mean L19 | LLM last_preaction L19 |\\\\n|------|-----------|--------------------|-----------------------|\\\\n| RSA | 0.615 | ~0.49 | ~0.49 |\\\\n| Action R² | **0.706** | 0.683 | **0.731** |\\\\n\\\\n**机制**：LLM self-attention 将 action-relevant 信息从分布式 visual tokens **重新路由**到 output position (last_preaction)。visual tokens 的几何结构 (RSA) 和功能性 (image_mean R²) 都降低了，但 action token 集中了更多信息。\\\\n\\\\n**关键数字**：Projector 已提供 LLM 96.6% 的 functional capacity (0.706/0.731)。LLM 边际贡献仅 +3.5%。\\\\n\\\\n**对 Claim 2 的影响**：不能再说 \\\\\\\"LLM degrades\\\\\\\"，需精炼为 \\\\\\\"LLM redistributes\\\\\\\"（推荐 Option A）。Framing 提案已提交 Director，D032 确认 Option A 锁定。\\\\n\\\\n## SMOKING GUN 确认：SigLIP+Projector RSA = 0.6153（2026-05-15）\\\\n\\\\n**d027_siglip_only_rsa 结果**: SigLIP+projector 直接输出（不过 LLM）的 RSA = 0.6153 [95% CI: 0.5257, 0.6954]。\\\\n\\\\n**关键发现：LLM 降低 action alignment（不是 passthrough）**：\\\\n- SigLIP+projector: **0.6153**\\\\n- Full VLA（任何条件）: ~0.48-0.49\\\\n- DINO: 0.388\\\\n\\\\nLLM 不仅没增强 action-relevant structure，反而将 RSA 从 0.615 降到 ~0.488（约 20% 下降）。这比 \\\\\\\"passthrough\\\\\\\" 更强——是 \\\\\\\"degradation\\\\\\\"。\\\\n\\\\n**机制解释**: SigLIP image-text 预训练产生的 visual features 天然具有强 action-relevant 结构。Projector 保持这一结构（cos_sim=1.0 frozen）。LLM 的高维 token mixing 稀释了这种结构（trained 和 untrained LLM 稀释程度一致）。\\\\n\\\\n## Per-Layer Degradation Curve 发现（2026-05-15）\\\\n\\\\n**plan_003_perlayer_degradation 结果**：降解非单调，集中在 embedding interface。\\\\n\\\\n**关键机制洞察**：\\\\n- Proj→L1 是最大 single-step drop（0.13–0.25，~20–40%），token embedding 是 degradation bottleneck\\\\n- L0（embedding layer）是异常值：trained 模型 RSA≈0，结构从 L1 才开始恢复\\\\n- 中间层有 partial recovery（non-monotonic），LLM 不是 \\\\\\\"progressive degrader\\\\\\\"\\\\n- **no-inst trained 独特模式**：唯一呈 L1→L30 持续上升的条件（peak at L30），training 在无 instruction 时让 LLM 逐层积累 action 信号。其余 3 个条件均 non-monotonic\\\\n- 总降解幅度 ~0.13：best LLM layer 仍比 projector 低 ~0.127\\\\n\\\\n## 完整 2×2 Matrix + SigLIP-only（2026-05-15）\\\\n\\\\n| 条件 | RSA | 备注 |\\\\n|------|-----|------|\\\\n| **SigLIP+Projector (no LLM)** | **0.6153** | smoking gun |\\\\n| Trained with-inst | 0.4876 | L9 peak |\\\\n| Trained no-inst | 0.489 | L30 peak |\\\\n| Untrained with-inst | 0.4846 | L12 peak |\\\\n| Untrained no-inst | 0.4802 | — |\\\\n| DINO | 0.388 | — |\\\\n\\\\n**结论**: 所有 4 个 full VLA 条件收敛在 0.48-0.49 band。SigLIP-only 显著高于 full VLA。Training 和 instruction 均无 meaningful effect。\\\\n\\\\n## Bootstrap CI on Training Effect（2026-05-15）\\\\n\\\\nimage_mean Δ=+0.021, CI=[−0.031, +0.064], p=0.20; last_preaction Δ=+0.008, CI=[−0.040, +0.056], p=0.37。**两个 CI 都包含 0**，Claim 3 invariance 成立。\\\\n\\\\n## Instruction Ablation FAIL — Option B 被否证（2026-05-15）\\\\n\\\\n**d021_instruction_ablation 结果**: no-inst untrained RSA = 0.4802 ≈ with-inst 0.4846（Δ=0.0044 << 0.10 阈值）。\\\\n\\\\n## Output Head Analysis 发现（2026-05-15，negative）\\\\n\\\\nVision backbone + Projector 在 trained 和 untrained 之间完全一致（rel_change=0, cos_sim=1.0）。Shallow adaptation FAIL。**Caveat**: trained vs untrained 比较的是 pretrained Llama + fine-tune vs random init。\\\\n\\\\n## 文献关键发现\\\\n\\\\n14 篇论文确认 vision encoder dominance 是已知现象（behavioral level）。我们在 representation level 发现同一模式，是独特贡献。Grant 2026: LIBERO-Goal 中 language 贡献关键（behavioral level），OFT checkpoint。\\\\n\\\\n## Novelty Gap\\\\n\\\\n| 工作 | 做了什么 | 没做什么 |\\\\n|------|---------|---------|\\\\n| Grant et al. 2026 | Behavioral intervention, \\\\\\\"encoded but not used\\\\\\\" | 无 trained vs untrained 对比 |\\\\n| Swann/Buurmeijer | SAE interpretability on OpenVLA+LIBERO | 无 language features 分析 |\\\\n| LIBERO-CF | Counterfactual behavioral benchmark | 无 representation analysis |\\\\n\\\\n## 方向 Pivot 历史\\\\n\\\\nMVP-1 Temporal Distance → G2 FAIL → MVP-2 Action Prediction → G2 FAIL → Action-Delta → G3 FAIL → D015 Pivot LIBERO-Goal → D018 Goal Classification → G3 FAIL → D019 RSA → G2 FAIL → D021 Instruction Ablation (FAIL) + Output Head (negative) → D027 Option A2 锁定 → **SigLIP-only SMOKING GUN PASS → MVP Gate 通过** → **Functional Probe: RSA-functional dissociation (negative for Claim 2 \\\\\\\"degrades\\\\\\\")** → **D031 Redistribution pivot → D032 Option A 锁定**\\\\n\\\\n## 技术约束\\\\n\\\\n- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）\\\\n- D017: 统一用 LIBERO-10 fine-tuned checkpoint（LIBERO-Goal 是 OOD 测试）\\\\n- Token 聚合：Primary = last pre-action token\\\\n- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/\\\\n- **分析 Worker 不得覆盖 spec 字段**\\\\n- **服务器无外网**：AutoProcessor/HF 操作必须 `local_files_only=True`\\\\n- **Instruction ablation bug**: `if args.task_instruction:` 对空字符串返回 False，已修复\\\\n\\\", \\\"total_chars\\\": 4867, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## CKA 指标依赖性发现（2026-05-16，plan_009 = success）\\n\\n**CKA 部分验证 RSA，但 projector vs trained 排序是指标依赖的。**\\n\\n| 发现 | RSA | RDM CKA | 一致？ |\\n|------|-----|---------|--------|\\n| DINO 最弱 | ✓ (0.388) | ✓ (0.241) | **Yes** |\\n| last_preaction >> image_mean | ✓ | ✓ (0.290 vs 0.260) | **Yes** |\\n| Projector > Trained | 0.615 vs 0.501 | 0.257 ≈ 0.260 | **No** — gap 压缩 |\\n| Per-layer 趋势 later > earlier | ✓ | ✓ | **Yes** |\\n\\n**论文语言约束**：projector \\\"dominance\\\" 只在 RSA 下显著，CKA 下 projector ≈ trained。论文应呈 RSA 为 primary，CKA 为 supplementary，并讨论 metric sensitivity（C7 应对方案）。Linear CKA 因维度不匹配（4096-D vs 7-D）不可靠，不作证据。\\n\\n## ⚠️ Functional Probe 分离发现（2026-05-15，p0_functional_action_probe = negative）\\n\\n**RSA 与 functional probe 发生分离——这是论文 Claim 2 的关键转折点。**\\n\\n| 度量 | Projector | LLM image_mean L19 | LLM last_preaction L19 |\\n|------|-----------|--------------------|-----------------------|\\n| RSA | 0.615 | ~0.49 | ~0.49 |\\n| Action R² | **0.706** | 0.683 | **0.731** |\\n\\n**机制**：LLM self-attention 将 action-relevant 信息从分布式 visual tokens **重新路由**到 output position (last_preaction)。visual tokens 的几何结构 (RSA) 和功能性 (image_mean R²) 都降低了，但 action token 集中了更多信息。\\n\\n**关键数字**：Projector 已提供 LLM 96.6% 的 functional capacity (0.706/0.731)。LLM 边际贡献仅 +3.5%。\\n\\n**对 Claim 2 的影响**：不能再说 \\\"LLM degrades\\\"，需精炼为 \\\"LLM redistributes\\\"（推荐 Option A）。Framing 提案已提交 Director，D032 确认 Option A 锁定。\\n\\n## SMOKING GUN 确认：SigLIP+Projector RSA = 0.6153（2026-05-15）\\n\\n**d027_siglip_only_rsa 结果**: SigLIP+projector 直接输出（不过 LLM）的 RSA = 0.6153 [95% CI: 0.5257, 0.6954]。\\n\\n**关键发现：LLM 降低 action alignment（不是 passthrough）**：\\n- SigLIP+projector: **0.6153**\\n- Full VLA（任何条件）: ~0.48-0.49\\n- DINO: 0.388\\n\\nLLM 不仅没增强 action-relevant structure，反而将 RSA 从 0.615 降到 ~0.488（约 20% 下降）。这比 \\\"passthrough\\\" 更强——是 \\\"degradation\\\"。\\n\\n**机制解释**: SigLIP image-text 预训练产生的 visual features 天然具有强 action-relevant 结构。Projector 保持这一结构（cos_sim=1.0 frozen）。LLM 的高维 token mixing 稀释了这种结构（trained 和 untrained LLM 稀释程度一致）。\\n\\n## Per-Layer Degradation Curve 发现（2026-05-15）\\n\\n**plan_003_perlayer_degradation 结果**：降解非单调，集中在 embedding interface。\\n\\n**关键机制洞察**：\\n- Proj→L1 是最大 single-step drop（0.13–0.25，~20–40%），token embedding 是 degradation bottleneck\\n- L0（embedding layer）是异常值：trained 模型 RSA≈0，结构从 L1 才开始恢复\\n- 中间层有 partial recovery（non-monotonic），LLM 不是 \\\"progressive degrader\\\"\\n- **no-inst trained 独特模式**：唯一呈 L1→L30 持续上升的条件（peak at L30），training 在无 instruction 时让 LLM 逐层积累 action 信号。其余 3 个条件均 non-monotonic\\n- 总降解幅度 ~0.13：best LLM layer 仍比 projector 低 ~0.127\\n\\n## 完整 2×2 Matrix + SigLIP-only（2026-05-15）\\n\\n| 条件 | RSA | 备注 |\\n|------|-----|------|\\n| **SigLIP+Projector (no LLM)** | **0.6153** | smoking gun |\\n| Trained with-inst | 0.4876 | L9 peak |\\n| Trained no-inst | 0.489 | L30 peak |\\n| Untrained with-inst | 0.4846 | L12 peak |\\n| Untrained no-inst | 0.4802 | — |\\n| DINO | 0.388 | — |\\n\\n**结论**: 所有 4 个 full VLA 条件收敛在 0.48-0.49 band。SigLIP-only 显著高于 full VLA。Training 和 instruction 均无 meaningful effect。\\n\\n## Bootstrap CI on Training Effect（2026-05-15）\\n\\nimage_mean Δ=+0.021, CI=[−0.031, +0.064], p=0.20; last_preaction Δ=+0.008, CI=[−0.040, +0.056], p=0.37。**两个 CI 都包含 0**，Claim 3 invariance 成立。\\n\\n## Instruction Ablation FAIL — Option B 被否证（2026-05-15）\\n\\n**d021_instruction_ablation 结果**: no-inst untrained RSA = 0.4802 ≈ with-inst 0.4846（Δ=0.0044 << 0.10 阈值）。\\n\\n## Output Head Analysis 发现（2026-05-15，negative）\\n\\nVision backbone + Projector 在 trained 和 untrained 之间完全一致（rel_change=0, cos_sim=1.0）。Shallow adaptation FAIL。**Caveat**: trained vs untrained 比较的是 pretrained Llama + fine-tune vs random init。\\n\\n## 文献关键发现\\n\\n14 篇论文确认 vision encoder dominance 是已知现象（behavioral level）。我们在 representation level 发现同一模式，是独特贡献。Grant 2026: LIBERO-Goal 中 language 贡献关键（behavioral level），OFT checkpoint。\\n\\n## Novelty Gap\\n\\n| 工作 | 做了什么 | 没做什么 |\\n|------|---------|---------|\\n| Grant et al. 2026 | Behavioral intervention, \\\"encoded but not used\\\" | 无 trained vs untrained 对比 |\\n| Swann/Buurmeijer | SAE interpretability on OpenVLA+LIBERO | 无 language features 分析 |\\n| LIBERO-CF | Counterfactual behavioral benchmark | 无 representation analysis |\\n\\n## 方向 Pivot 历史\\n\\nMVP-1 Temporal Distance → G2 FAIL → MVP-2 Action Prediction → G2 FAIL → Action-Delta → G3 FAIL → D015 Pivot LIBERO-Goal → D018 Goal Classification → G3 FAIL → D019 RSA → G2 FAIL → D021 Instruction Ablation (FAIL) + Output Head (negative) → D027 Option A2 锁定 → **SigLIP-only SMOKING GUN PASS → MVP Gate 通过** → **Functional Probe: RSA-functional dissociation (negative for Claim 2 \\\"degrades\\\")** → **D031 Redistribution pivot → D032 Option A 锁定**\\n\\n## 技术约束\\n\\n- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）\\n- D017: 统一用 LIBERO-10 fine-tuned checkpoint（LIBERO-Goal 是 OOD 测试）\\n- Token 聚合：Primary = last pre-action token\\n- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/\\n- **分析 Worker 不得覆盖 spec 字段**\\n- **服务器无外网**：AutoProcessor/HF 操作必须 `local_files_only=True`\\n- **Instruction ablation bug**: `if args.task_instruction:` 对空字符串返回 False，已修复\\n\", \"total_chars\": 4867, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LBDTfPW69ywVsHd2MoC1vR`</summary>

```json
{
  "project": "vla-ssd",
  "fields": [
    "*"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "1a33e4b2-84bd-4413-b76d-6a1e159abe06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwxDD7cKnyMjTQw4UXp6TV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 23787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
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

_source line 15 · 2026-05-16T00:30:07.964Z_

<details><summary>↩ Tool result · `toolu_01LBDTfPW69ywVsHd2MoC1vR`</summary>

```text
Error: result (79,120 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "248e231e-99d4-4cc9-b0bc-74e818b9ee73",
  "tool_use_result": {
    "content": "Error: result (79,120 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"untrained_last_preaction_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:56.469Z\", \"updated_at\": \"2026-05-16T00:14:01.670Z\", \"spec\": {\"command\": \"python scripts/action_probe.py --features untrained --feature_key last_preaction\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b-untrained\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe analysis)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/\"}, \"metrics\": {\"untrained_last_preaction_L19_mean_R2\": 0.325, \"trained_last_preaction_L19_mean_R2\": 0.7309, \"projector_mean_R2\": 0.706, \"delta_trained_vs_untrained_L19\": 0.406, \"untrained_best_layer\": \"L32\", \"untrained_best_R2\": 0.6858, \"delta_best_vs_best\": 0.0452, \"bootstrap_ci_trained_vs_untrained\": {\"trained_L19_mean_R2\": 0.7309, \"untrained_L32_mean_R2\": 0.6858, \"observed_delta\": 0.0452, \"ci_95\": [0.0321, 0.0585], \"p_value\": 0.0001, \"ci_excludes_0\": true, \"all_10_tasks_positive\": true, \"per_task_delta_range\": [0.02, 0.083], \"n_bootstrap\": 10000}, \"conclusion_summary\": \"Untrained best last_preaction R²=0.686 < trained 0.731 (Δ=0.045, CI=[0.032,0.059], p<0.0001). Redistribution is training-dependent.\"}, \"hypothesis\": \"C001 control: Untrained VLA last_preaction action probe. If untrained last_preaction R² < projector (0.706) → redistribution is training-dependent. If ≈ projector → architectural.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis experiment)\", \"completed_at\": \"2026-05-16T00:11:13.235Z\"}, \"plan_008_random_inst_control\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:57:16.908Z\", \"updated_at\": \"2026-05-16T00:06:04.233Z\", \"hypothesis\": \"Plan_008 (Claim 3): Random instruction control. Replace real instruction with random gibberish (random_s0) or word-shuffled version (shuffled). If RSA ≈ normal instruction (0.488) → instruction content irrelevant, supports invariance. If RSA drops significantly → instruction content matters.\", \"spec\": {\"command\": \"python scripts/extract_features_rand_inst.py --instruction_mode random --seed 0 --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b\", \"seed\": 0}, \"notes\": \"Feature extraction in progress: random_s0 (cuda:0) + shuffled (cuda:1), ~6 min/task, 10 tasks each. Started ~08:00 server time, ETA ~09:00 server time (~01:00 UTC). Intermediate finding: token-level shuffled_token_control already done — original probe acc 100% → shuffled 20.6%±7.1% (destroys linear separability). Existing RSA baseline: normal=0.4888 vs empty=0.4723 (L16, Δ=-0.0165). RSA script ready to auto-detect shuffled/random_s0 dirs upon extraction completion.\"}, \"plan_009_cka_verification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:43:19.084Z\", \"updated_at\": \"2026-05-16T00:03:29.018Z\", \"hypothesis\": \"Plan 009: CKA verification — replicate RSA findings with CKA metric to ensure conclusions are not metric-dependent. CPU-only, uses existing features. SigLIP+projector CKA should show same dominance pattern as RSA.\", \"spec\": {\"command\": \"python scripts/cka_analysis.py (CPU-only, multiple conditions)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,siglip_only,dino}_libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b\", \"seed\": 0, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/cka_verification/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:03:19.946Z\", \"metrics\": {\"linear_cka\": {\"untrained_img_mean_L23\": 0.0894, \"trained_img_mean_L23\": 0.0834, \"projector\": 0.0809, \"dino\": 0.0664, \"trained_last_preaction_L32\": 0.127}, \"rdm_cka\": {\"trained_img_mean_L23\": 0.2599, \"projector\": 0.2568, \"untrained_img_mean_L23\": 0.2464, \"dino\": 0.2408, \"trained_last_preaction_L32\": 0.2898}, \"findings\": \"DINO lowest across all metrics (robust). last_preaction >> image_mean (redistribution confirmed). Projector vs trained gap compressed in CKA vs RSA (metric-dependent).\"}}, \"p0_functional_probe_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:47:31.973Z\", \"updated_at\": \"2026-05-15T23:52:37.355Z\", \"hypothesis\": \"V2 corrected functional probe: (1) Add projector vs image_mean_L19 bootstrap CI as primary gate (0.706 vs 0.683), (2) Add DINO action probe for three-way comparison, (3) Diagnose untrained L10/L11 anomaly (R² drops from 0.632 to 0.029). Re-dream prerequisite.\", \"metrics\": {\"bootstrap_proj_vs_image_mean_L19\": {\"proj_mean_R2\": 0.7063, \"image_mean_L19_mean_R2\": 0.6832, \"delta\": 0.0231, \"ci_95\": [0.0105, 0.0367], \"p_value\": 0.001, \"gate\": \"PASS — CI lower bound > 0\"}, \"dino_action\": {\"mean_R2\": 0.7116, \"feature_key\": \"cls_token\"}, \"dino_action_delta\": {\"mean_R2\": 0.1}, \"bootstrap_dino_vs_proj\": {\"delta\": 0.005, \"ci_95\": [-0.008, 0.019], \"p_value\": 0.22, \"significant\": false}, \"three_way_ordering\": \"DINO (0.712) ≈ Projector (0.706) > LLM image_mean (0.683)\", \"untrained_L10_L11_diagnosis\": {\"verdict\": \"pathological_random_init\", \"detail\": \"Feature stats normal (no NaN/Inf/zeros, std~5), but probe R² drops L9=0.632→L10=0.029. Random LLM weights create non-decodable representations at these layers.\"}, \"result_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_v2.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (probe task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_v2.json\", \"completed_at\": \"2026-05-15T23:52:03.717Z\"}, \"p0_functional_action_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:21:52.011Z\", \"updated_at\": \"2026-05-15T23:47:31.338Z\", \"hypothesis\": \"P0 BLOCKING Functional Validation: Action prediction probe on SigLIP+projector output features. If projector R² ≥ LLM best layer (0.683) → smoking gun functional validation. If < LLM but > DINO (0.676) → partial. If ≤ DINO → degradation claim needs reeval. Also tests image_mean aggregation from LLM hidden states.\", \"metrics\": {\"projector\": {\"mean_R2\": 0.7063, \"overall_R2\": 0.7169, \"grip_acc\": 0.9221}, \"image_mean_trained_L19\": {\"mean_R2\": 0.6832, \"overall_R2\": 0.6961, \"grip_acc\": 0.9182}, \"image_mean_trained_L23\": {\"mean_R2\": 0.5736, \"overall_R2\": 0.59, \"grip_acc\": 0.8924}, \"llm_last_preaction_L19\": {\"mean_R2\": 0.7309, \"overall_R2\": 0.7397, \"grip_acc\": 0.9184}, \"untrained_image_mean_L0\": {\"mean_R2\": 0.7136, \"overall_R2\": 0.7234, \"grip_acc\": 0.9218}, \"bootstrap_ci_proj_vs_llm_last_preaction\": {\"delta\": -0.0246, \"ci_95\": [-0.04, -0.009], \"p_value\": 0.0014}, \"gate_judgment\": \"PASS — projector 0.706 ≥ 0.683 threshold. But LLM last_preaction (0.731) > projector (0.706), p=0.001.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (probe evaluation)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json\", \"completed_at\": \"2026-05-15T23:43:02.159Z\", \"notes\": \"V1 完成但缺统计检验：(1) 缺 projector vs image_mean_L19 bootstrap CI (主比较 0.706 vs 0.683), (2) 缺 DINO probe, (3) untrained L10/L11 异常需排查。V2 修正版见 p0_functional_probe_v2。\"}, \"p0_functional_action_delta_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:21:52.667Z\", \"updated_at\": \"2026-05-15T23:47:29.211Z\", \"hypothesis\": \"P0 BLOCKING Functional Validation: Action-delta prediction (Δa = a_{t+1}-a_t) on SigLIP+projector output features. Removes autocorrelation. Compare with LLM best (L14, R²=0.059) and DINO (R²=0.060). Also tests image_mean aggregation.\", \"metrics\": {\"projector\": {\"mean_R2\": 0.1181, \"overall_R2\": 0.1053}, \"trained_image_mean_L14\": {\"mean_R2\": 0.1215, \"overall_R2\": 0.1091}, \"untrained_best_L0\": {\"mean_R2\": 0.1174, \"overall_R2\": 0.107}, \"bootstrap_proj_vs_trained\": {\"delta\": -0.0034, \"ci_95\": [-0.0066, 0.0005], \"p_value\": 0.04}, \"note\": \"image_mean R² (~0.12) substantially higher than last_preaction (~0.06). Per-dim: dz=0.46, dx=0.29, dy=0.25 most predictable.\", \"gate\": \"Projector (0.118) ≈ LLM (0.122), gap tiny (Δ=0.003). Consistent with redistribution narrative.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_delta_probe_projector.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (probe task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_delta_probe_projector.json\", \"completed_at\": \"2026-05-15T23:45:44.568Z\", \"notes\": \"Delta probe: projector (0.118) BELOW LLM (0.122), CI=[-0.007, +0.001] 含 0, p=0.04. 差异不显著。论文需如实汇报：raw action PASS (projector > image_mean), delta BELOW (差异不显著)。双维度呈现。\"}, \"p0_bootstrap_ci_training_effect\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:44:40.511Z\", \"updated_at\": \"2026-05-15T22:49:25.162Z\", \"hypothesis\": \"P0: Bootstrap CI on training effect (image_mean aggregation). Trained RSA=0.5014 vs untrained RSA=0.4847, Δ=+0.017. Task-level resampling bootstrap 95% CI. If CI excludes 0 → Claim 3 needs minor adjustment (\\\"minimal but detectable\\\"). If CI includes 0 → Claim 3 \\\"invariance\\\" holds.\", \"metrics\": {\"image_mean\": {\"delta\": 0.0206, \"ci_95\": [-0.0314, 0.0638], \"p_value\": 0.2, \"significant\": false}, \"last_preaction\": {\"delta\": 0.0076, \"ci_95\": [-0.0395, 0.0558], \"p_value\": 0.37, \"significant\": false}, \"n_bootstrap\": 10000, \"n_tasks\": 10, \"conclusion\": \"Both CIs include 0. Training effect not significant under task-level bootstrap. Claim 3 invariance holds.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/bootstrap_training_effect.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (statistical test)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/bootstrap_training_effect.json\", \"completed_at\": \"2026-05-15T22:49:25.162Z\"}, \"p0_image_mean_rsa_verify\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:33:21.471Z\", \"updated_at\": \"2026-05-15T22:43:41.904Z\", \"hypothesis\": \"P0 CRITICAL: Verify Claim 2 (LLM degrades action alignment 0.615→0.488) is not an aggregation artifact. SigLIP uses mean pooling, VLA used last_preaction. Re-run RSA with image_mean feature key for trained with-inst and untrained with-inst. If image_mean RSA ≈ 0.61 → Claim 2 is artifact. If ≈ 0.49 → Claim 2 holds.\", \"metrics\": {\"trained_image_mean_rsa\": 0.5014, \"trained_image_mean_peak_layer\": 23, \"trained_last_preaction_rsa\": 0.4876, \"untrained_image_mean_rsa\": 0.4847, \"untrained_image_mean_peak_layer\": 23, \"untrained_last_preaction_rsa\": 0.4846, \"siglip_projector_rsa\": 0.6153, \"gap_siglip_vs_image_mean\": 0.1139, \"verdict\": \"Claim 2 HOLDS — image_mean RSA (0.5014) ≈ last_preaction (0.4876), both far below SigLIP (0.6153). Aggregation artifact hypothesis rejected.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (verification task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json\", \"completed_at\": \"2026-05-15T22:42:57.560Z\", \"notes\": \"额外发现 (SSH worker): image_mean 聚合下 trained-untrained delta = +0.017 (L23)，比 last_preaction 的 +0.003 明显更大。Training 增强了 image token 表征的 action 相关性，但信号在 last_preaction (序列末位 token) 中被稀释。Trained 呈 inverted-U 曲线 (L0=0.45→L23=0.50→L32=0.44)，untrained 近乎平坦 (0.47-0.48)。Layer 0 trained=untrained=0.4509 (LLM 处理前一致)。\"}, \"plan_003_perlayer_degradation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:30:49.507Z\", \"updated_at\": \"2026-05-15T22:35:08.118Z\", \"hypothesis\": \"D028 plan_003: Per-layer RSA degradation curve. Track RSA from SigLIP+projector output (L0=0.615) through LLM layers 1-32 (~0.48). If monotonic decrease → LLM progressively degrades action alignment. If non-monotonic → some layers partially recover. Supports Claim 2 (LLM degrades action-relevant structure).\", \"metrics\": {\"siglip_projector_rsa\": 0.6153, \"perlayer_summary\": {\"with_inst_trained\": {\"peak_rsa\": 0.4876, \"peak_layer\": 9, \"proj_to_l1_drop\": 0.2036, \"pattern\": \"non_monotonic\"}, \"with_inst_untrained\": {\"peak_rsa\": 0.4846, \"peak_layer\": 12, \"proj_to_l1_drop\": 0.1512, \"pattern\": \"non_monotonic\"}, \"no_inst_trained\": {\"peak_rsa\": 0.489, \"peak_layer\": 30, \"proj_to_l1_drop\": 0.2526, \"pattern\": \"predominantly_increasing\"}, \"no_inst_untrained\": {\"peak_rsa\": 0.4802, \"peak_layer\": 6, \"proj_to_l1_drop\": 0.1374, \"pattern\": \"non_monotonic\"}}, \"total_degradation_range\": [0.126, 0.135], \"key_findings\": [\"Proj→L1 is the biggest RSA drop (0.13-0.25, ~20-40%)\", \"L0 (embedding) is anomaly (RSA≈0 for trained), structure recovers at L1\", \"No-inst trained is unique: predominantly increasing L1→L30\", \"All LLM layers RSA >> DINO (0.388)\", \"Total degradation ~0.13: best LLM layer still 0.13 below projector output\"], \"result_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/perlayer_degradation_curve.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/perlayer_degradation_curve.json\", \"completed_at\": \"2026-05-15T22:35:08.118Z\"}, \"lg_output_head_analysis\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.398Z\", \"updated_at\": \"2026-05-15T22:30:46.827Z\", \"hypothesis\": \"D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences across layers. If training does \\\"shallow adaptation\\\", output head weight diff >> middle layer weight diff. Explains \\\"representations unchanged but behavior improved\\\".\", \"conclusion\": \"killed\", \"notes\": \"Duplicate of d021_output_head_analysis. Superseded by Director-specified ID. Cleaned up per D028.\"}, \"lg_instruction_ablation\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:57.146Z\", \"updated_at\": \"2026-05-15T22:30:45.973Z\", \"hypothesis\": \"D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.\", \"conclusion\": \"killed\", \"notes\": \"Duplicate of d021_instruction_ablation. Superseded by Director-specified ID. Cleaned up per D028.\"}, \"d027_siglip_only_rsa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:10:53.129Z\", \"updated_at\": \"2026-05-15T22:25:27.345Z\", \"hypothesis\": \"D027 Exp-1 (SMOKING GUN): Extract SigLIP+projector output features (LLM input embeddings) from VLA architecture on LIBERO-Goal, run RSA. If SigLIP-only RSA ≈ 0.45-0.50 → confirms vision encoder is the source of action-relevant structure (LLM is passthrough). If RSA ≈ 0.39 (DINO level) → projector/LLM architecture contributes, need reanalysis.\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/extract_siglip_features.py + python /root/vla-ssd/rsa_siglip_only.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/siglip_only_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 1 layer (projector output, 4096 dim)\", \"model_name\": \"openvla/openvla-7b SigLIP+projector only (no LLM forward)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_siglip_only.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}, \"metrics\": {\"siglip_projector_rsa\": 0.6153, \"bootstrap_95_ci\": [0.5257, 0.6954], \"comparison\": {\"siglip_projector\": 0.6153, \"trained_with_inst\": 0.4876, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"trained_no_inst\": 0.489, \"dino\": 0.388}, \"llm_degradation\": \"LLM reduces RSA from 0.615 (projector output) to ~0.488 (LLM hidden states)\", \"gate_judgment\": \"PASS — SigLIP+projector RSA=0.6153 >> 0.45-0.50 threshold. Vision encoder is the source of action-relevant structure. LLM is not passthrough but actually degrades action alignment.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:25:27.345Z\"}, \"d027_trained_no_inst_rsa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:10:55.271Z\", \"updated_at\": \"2026-05-15T22:16:04.389Z\", \"hypothesis\": \"D027 Exp-2: Extract trained VLA features with empty instruction on LIBERO-Goal, run RSA. Completes the 2×2 matrix (training × instruction). Expected: trained no-inst RSA ≈ untrained no-inst (0.4802), further confirming training is irrelevant to representational structure.\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/extract_features.py --task_instruction '' + python /root/vla-ssd/rsa_analysis.py (trained no-inst)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal_no_inst/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (trained, no instruction)\", \"model_name\": \"openvla/openvla-7b (trained, empty instruction)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_trained_no_inst.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}, \"metrics\": {\"trained_no_inst_peak_rsa\": 0.489, \"trained_no_inst_peak_layer\": 30, \"full_2x2_matrix\": {\"trained_with_inst\": 0.4876, \"trained_no_inst\": 0.489, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"dino\": 0.388}, \"training_effect_with_inst\": 0.003, \"training_effect_no_inst\": 0.0088, \"instruction_effect_trained\": -0.0014, \"instruction_effect_untrained\": 0.0044, \"bootstrap_delta_ci\": \"[-0.058, 0.072] includes 0\", \"conclusion_summary\": \"All 4 conditions converge in 0.48-0.49 band. Neither training nor instruction has meaningful effect on RSA.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:16:04.389Z\"}, \"d021_instruction_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:11:15.503Z\", \"updated_at\": \"2026-05-15T22:06:08.026Z\", \"hypothesis\": \"D021 Exp-1 (HARD GATE): Instruction Ablation on untrained VLA. Replace instruction with empty string, extract LIBERO-Goal features, run RSA. Gate (D023 relative): PASS = no-inst RSA significantly below with-inst (Δ>0.10, bootstrap CI excludes 0) AND no-inst RSA ≤ DINO RSA + 0.05. FAIL = no-inst RSA ≥ with-inst RSA − 0.05. PASS → lock Option B. FAIL → fallback Option A.\", \"spec\": {\"command\": \"python scripts/extract_features_no_instruction.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50 && python rsa_analysis.py (no-inst features)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (no instruction)\", \"model_name\": \"openvla/openvla-7b-untrained (empty instruction ablation)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_no_instruction.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\", \"note\": \"Worker: worker_ssh_instruction-ablation_20260515T200929. Gate: PASS = Δ(with-no)>0.10 + CI excludes 0 + no-inst ≤ DINO+0.05. FAIL = no-inst ≥ with-inst−0.05.\"}, \"metrics\": {\"no_inst_untrained_peak_rsa\": 0.4802, \"with_inst_untrained_peak_rsa\": 0.4846, \"with_inst_trained_peak_rsa\": 0.4876, \"dino_rsa\": 0.388, \"delta_with_minus_no_inst\": 0.0044, \"gate_threshold_delta\": 0.1, \"gate_threshold_no_inst_max\": 0.438, \"gate_judgment\": \"FAIL — Δ=0.0044 << 0.10; no_inst=0.4802 >> DINO+0.05=0.438\", \"interpretation\": \"Removing instruction text does NOT collapse RSA. Untrained VLA action-relevant structure is vision-driven, not instruction-driven. Option B framing falsified.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T22:06:08.026Z\"}, \"d021_output_head_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:11:17.179Z\", \"updated_at\": \"2026-05-15T20:18:12.515Z\", \"hypothesis\": \"D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences per layer (Frobenius norm ratio). PASS: output head norm ratio >> LLM deep layer mean (>3x), confirming shallow adaptation. FAIL: differences uniformly distributed.\", \"spec\": {\"command\": \"python output_head_analysis.py (load trained + untrained state_dicts, compute per-layer Frobenius norm ratio)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/ + openvla-7b-untrained/\", \"data_count\": \"2 models x ~7B params each\", \"model_name\": \"openvla/openvla-7b vs openvla-7b-untrained weight comparison\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/output_head_analysis.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"note\": \"Worker: worker_ssh_output-head-analysis_20260515T200957. CPU-only analysis. PASS: output head norm ratio > 3x LLM layer mean.\"}, \"metrics\": {\"group_summary\": {\"vision\": {\"count\": 685, \"mean_rel_change\": 0, \"cos_sim\": 1, \"verdict\": \"IDENTICAL\"}, \"projector\": {\"count\": 6, \"mean_rel_change\": 0, \"cos_sim\": 1.001, \"verdict\": \"IDENTICAL\"}, \"embedding\": {\"count\": 1, \"rel_change\": 1.3287, \"cos_sim\": -0.0001}, \"llm\": {\"count\": 288, \"mean_rel_change\": 1.3156, \"std\": 0.3759, \"cos_sim\": 0.2178, \"range\": [1.22, 1.37]}, \"llm_final_norm\": {\"count\": 1, \"rel_change\": 0.8628, \"cos_sim\": 0.998}, \"head_lm_head\": {\"count\": 1, \"rel_change\": 1.4754, \"cos_sim\": 0.0002}}, \"head_vs_llm_ratio\": 1.12, \"shallow_adaptation_gate\": \"FAIL (ratio 1.12x, threshold 3x)\", \"key_finding_1\": \"Vision backbone + Projector IDENTICAL between trained and untrained (rel_change=0, cos_sim=1.0)\", \"key_finding_2\": \"LLM weight diffs uniformly distributed across all 32 layers (rel_change 1.22-1.37), head not special\", \"key_finding_3\": \"Shared frozen components (SigLIP + projector) explain WHY trained ≈ untrained in representation structure — regardless of LLM weights\", \"caveat\": \"Comparison is pretrained Llama + fine-tune vs random init, not fine-tuned vs pre-fine-tuning. Differences dominated by pretrained vs random.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T20:18:12.515Z\"}, \"lg_rsa_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:45:51.878Z\", \"updated_at\": \"2026-05-15T20:05:37.885Z\", \"hypothesis\": \"D019/D020: RSA on LIBERO-Goal features. Same-scene/different-goal cross-goal RSA: representation RDM vs action RDM correlation. Gates (D020): G1 trained best-layer RSA ρ > 0.15; G2 Δρ(trained-untrained) > 0.08 with bootstrap 95% CI excluding 0; G3 trained ρ > DINO ρ (any positive margin).\", \"spec\": {\"command\": \"python rsa_analysis.py (full run on LIBERO-Goal features)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,dinov2}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers (VLA) / 1 layer (DINO)\", \"model_name\": \"RSA: Spearman(repr_RDM, action_RDM) per layer + CKA\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}, \"metrics\": {\"trained_peak_rsa\": 0.4876, \"trained_peak_layer\": 9, \"untrained_peak_rsa\": 0.4846, \"untrained_peak_layer\": 12, \"dino_rsa\": 0.388, \"delta_TU_at_trained_peak\": 0.003, \"delta_TU_range\": [-0.0722, 0.0109], \"layers_trained_gt_untrained\": 4, \"layers_total\": 33, \"per_phase\": {\"early\": {\"trained\": 0.3197, \"untrained\": 0.4148, \"dino\": 0.4909}, \"mid\": {\"trained\": 0.5231, \"untrained\": 0.5248, \"dino\": 0.4132}, \"late\": {\"trained\": 0.4758, \"untrained\": 0.4592, \"dino\": 0.2601}}, \"cka_range\": [0.687, 0.86], \"gate_G1_D020\": \"PASS (0.4876 > 0.15)\", \"gate_G2_D020\": \"FAIL (Δρ=0.003, threshold 0.08)\", \"gate_G3_D020\": \"PASS (0.4876 > 0.388, margin +0.0996)\", \"interpretation\": \"Architecture matters (VLA >> DINO), training doesn't (trained ≈ untrained). Instruction input adds action-relevant structure, but LLM training does not improve it.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T20:05:37.885Z\"}, \"lg_shuffled_token_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:27:18.397Z\", \"updated_at\": \"2026-05-15T19:48:27.481Z\", \"hypothesis\": \"Control: token-shuffled goal classification on trained VLA features. Shuffling token order destroys positional/sequential info. NOTE: uses bare task name prompt (not formatted prompt like main pipeline) — results not directly comparable.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --shuffle_tokens\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (token-shuffled)\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features with shuffled tokens\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"note\": \"Control: uses bare task name prompt (NOT formatted prompt). Results not directly comparable to main pipeline. Worker: worker_ssh_shuffled-tokens-control\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_shuffled_token_control.log\"}, \"conclusion\": \"killed\", \"notes\": \"实验从未实际启动：GPU 0%，输出目录不存在。Worker 可能在 Agent OOM kill 前未完成提交。加之 prompt format 不一致（bare task name vs formatted prompt），参考价值有限。标记 CANCELLED per D019 Reviewer 审查。\", \"completed_at\": \"2026-05-15T19:48:27.481Z\"}, \"lg_pca1024_linear_pertimestep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:39:51.209Z\", \"updated_at\": \"2026-05-15T19:40:23.583Z\", \"hypothesis\": \"D018 Exp-2: PCA-1024 + Linear Probe per-timestep (10 bins). Tests whether trained VLA shows stronger goal encoding than untrained at early timesteps (visual ambiguity highest). Success: t=0 bin Δ(trained-untrained) > 15pp.\", \"spec\": {\"command\": \"python pca_linear_probe_pertimestep.py --trained_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --untrained_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --dino_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --pca_dim 1024 --output /root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,dinov2}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos, best layer features, 10 timestep bins\", \"model_name\": \"LogisticRegression (PCA-1024), per-timestep evaluation\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\"}, \"metrics\": {\"bin_0_trained\": 0.9992, \"bin_0_untrained\": 1, \"bin_0_dino\": 0.354, \"bin_0_delta_TU\": -0.0008, \"overall_trained\": 0.9999, \"overall_untrained\": 1, \"overall_dino\": 0.8397, \"per_bin\": {\"0\": {\"trained\": 0.9992, \"untrained\": 1, \"dino\": 0.354}, \"1\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.7662}, \"2\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8244}, \"3\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8676}, \"4\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8575}, \"5\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8903}, \"6\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.9618}, \"7\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.9574}, \"8\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.969}, \"9\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.9676}}, \"gate_exp2\": \"FAIL\", \"gate_exp2_delta\": -0.0008, \"gate_exp2_threshold\": 0.15}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T19:40:23.583Z\"}, \"lg_gc_trained_frame0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:27:20.212Z\", \"updated_at\": \"2026-05-15T19:36:26.561Z\", \"hypothesis\": \"Frame-0-only goal classification on trained VLA features (33 layers). Tests instruction encoding when visual states are most similar across goals. Key layer curve: L0=10%, L1=39%, L2=58%, L3+=100%.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_frames 1\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (frame 0 only)\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features frame-0 only\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"note\": \"Frame-0 layer curve: L0=10%, L1=39%, L2=58%, L3+=100%. Shows 3+ layers needed for instruction integration at max visual ambiguity. Worker: worker_ssh_initial-frame-gc\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained_frame0.log\"}, \"metrics\": {\"trained_best_layer\": 3, \"trained_best_acc\": 1, \"trained_best_f1\": 1, \"untrained_best_layer\": 2, \"untrained_best_acc\": 1, \"untrained_best_f1\": 1, \"dino_best_acc\": 0.15, \"dino_best_f1\": 0.0911, \"n_classes\": 10, \"n_train\": 400, \"n_val\": 100, \"trained_layer_curve\": {\"L0\": 0.1, \"L1\": 0.39, \"L2\": 0.58, \"L3\": 1, \"L4_to_L18\": 1, \"L19\": 1, \"L28\": 1, \"L31\": 1, \"L32\": 1}, \"untrained_layer_curve\": {\"L0\": 0.1, \"L1\": 0.95, \"L2\": 1, \"L3\": 0.99, \"L19\": 0.91, \"L28\": 0.9, \"L31\": 0.88, \"L32\": 0.98}, \"sanity_gc_frame0\": \"PASS (DINO 15% <= 25%)\", \"g3_gc_frame0\": \"FAIL (Δ=0pp, both 100%)\", \"key_finding\": \"DINO 15% at t=0 confirms visual ambiguity. But MLP+4096 probe capacity still saturates both VLA models. Trained VLA more stable across layers (100% L3+) vs untrained (88-100% oscillation in deep layers). Needs PCA+linear verification.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:36:26.561Z\"}, \"lg_gc_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:51:49.753Z\", \"updated_at\": \"2026-05-15T18:03:31.246Z\", \"hypothesis\": \"Goal classification probe on untrained VLA LIBERO-Goal features (33 layers). Baseline for G2-GC gate: Δ(trained-untrained) best-layer acc > 25pp. Untrained VLA with random LLM should show lower goal classification accuracy.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), untrained VLA features\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_untrained\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ + /root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_libero_goal/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_untrained.log\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"pid\": 635369, \"reproduce\": {\"finished_at\": \"2026-05-15T18:01:11.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:01:12.865150+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"best_layer\": 1, \"best_accuracy\": 1, \"best_traj_accuracy\": 1, \"best_macro_f1\": 1, \"worst_layer\": 31, \"worst_accuracy\": 0.9971, \"n_classes\": 10, \"n_train\": 50880, \"n_val\": 12848, \"per_layer_accuracies\": {\"0\": 0.1582, \"1\": 1, \"2\": 1, \"3\": 1, \"4\": 1, \"5\": 1, \"6\": 1, \"7\": 1, \"8\": 1, \"9\": 1, \"10\": 0.9998, \"11\": 0.9998, \"12\": 0.9999, \"13\": 0.9999, \"14\": 0.9996, \"15\": 0.9996, \"16\": 0.9998, \"17\": 0.9994, \"18\": 0.9989, \"19\": 0.9992, \"20\": 0.9995, \"21\": 0.9993, \"22\": 0.9996, \"23\": 0.9991, \"24\": 0.9994, \"25\": 0.9988, \"26\": 0.9993, \"27\": 0.9993, \"28\": 0.9986, \"29\": 0.9984, \"30\": 0.9977, \"31\": 0.9971, \"32\": 0.9991}, \"gate_G2_GC\": \"FAIL\", \"gate_G2_GC_delta\": 0, \"gate_G2_GC_threshold\": 0.25, \"layer0_detail\": \"predicts_only_class1_acc_0.158_random_level\", \"comparison\": {\"trained_best_acc\": 1, \"untrained_best_acc\": 1, \"dino_best_acc\": 0.8626, \"delta_trained_untrained\": 0, \"delta_trained_dino\": 0.1374}, \"interpretation\": \"Untrained VLA (random LLM) achieves identical 100% goal classification from layer 1+. G2-GC FAIL: Δ=0pp (threshold 25pp). Goal classification is NOT a valid discriminator between trained and untrained VLA — the MLP probe on 4096-dim features trivially separates 10 classes even from random projections.\"}, \"completed_at\": \"2026-05-15T18:03:31.246Z\"}, \"lg_gc_dino\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:53:30.361Z\", \"updated_at\": \"2026-05-15T18:00:37.784Z\", \"hypothesis\": \"DINO-V2 LIBERO-Goal goal classification probe (Sanity-GC gate). DINO acc must be ≤ 25% (10-class random=10%). If DINO > 25%, goals are visually distinguishable and experiment premise is challenged.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"635723\", \"log_path\": \"~/runs/vla-ssd/lg_gc_dino.log\", \"submitted_at\": \"2026-05-15T17:54:11.228Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 1 layer x 1024 dim\", \"model_name\": \"GoalClassificationProbe MLP (1024->256->10), DINO-V2 features\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/goal_classification/\", \"wall_clock_seconds\": 386.6, \"gpu_hours\": 0.11}, \"conclusion\": \"success\", \"metrics\": {\"best_accuracy\": 0.8626, \"best_traj_accuracy\": 1, \"best_macro_f1\": 0.8412, \"n_classes\": 10, \"num_layers\": 1, \"feature_dim\": 1024, \"gate_Sanity_GC\": \"FAIL\", \"note\": \"DINO acc 86.26% >> 25% threshold. Goals are visually distinguishable. Sanity-GC gate FAILED.\"}, \"completed_at\": \"2026-05-15T18:00:37.784Z\"}, \"lg_dino_extract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:42:52.995Z\", \"updated_at\": \"2026-05-15T17:56:18.045Z\", \"hypothesis\": \"DINO-V2 LIBERO-Goal feature extraction — vision-only baseline for Goal Classification gate (Sanity-GC: DINO acc ≤ 25%)\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T17:43:09.957Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_dinov2.py --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large --gpu 0\\\"\", \"finished_at\": \"2026-05-15T17:49:37.592Z\", \"training_hours\": 0.11}, \"spec\": {\"command\": \"python scripts/extract_dinov2.py --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/\", \"log_path\": \"~/runs/vla-ssd/lg_dino_extract.log\"}, \"pid\": \"634279\", \"log_path\": \"~/runs/vla-ssd/lg_dino_extract.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:49:38.728557+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": 10, \"tasks_total\": 10, \"demos_per_task\": 50, \"total_frames\": 63728, \"feature_dim\": 1024, \"dtype\": \"float16\", \"feature_keys\": [\"cls_token\", \"patch_mean\"], \"file_count\": 10, \"total_size_mb\": 234, \"extraction_fps\": 183, \"extraction_time_s\": 347.3}, \"completed_at\": \"2026-05-15T17:53:27.460Z\"}, \"lg_gc_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:42:55.296Z\", \"updated_at\": \"2026-05-15T17:54:35.688Z\", \"hypothesis\": \"Goal classification probe on trained VLA LIBERO-Goal features (33 layers). Gate G1-GC: best-layer acc > 40%. Core evidence for instruction encoding in VLA representations.\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"reproduce\": {\"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T17:43:12.537Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\\\"\", \"finished_at\": \"2026-05-15T17:51:48.066Z\", \"training_hours\": 0.14}, \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir .../trained_libero_goal/ --output_dir .../results/trained_libero_goal/ --probe_type goal_classification --data_dir .../libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/ + /root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained.log\"}, \"pid\": \"634360\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:51:52.405382+00:00\"}]}, \"metrics\": {\"best_layer\": 1, \"best_accuracy\": 1, \"best_traj_accuracy\": 1, \"best_macro_f1\": 1, \"n_classes\": 10, \"n_train\": 50880, \"n_val\": 12848, \"per_layer_accuracies\": {\"0\": 0.1582, \"1\": 1, \"2\": 1, \"3\": 1, \"4\": 1, \"5\": 1, \"6\": 1, \"7\": 1, \"8\": 1, \"9\": 1, \"10\": 1, \"11\": 1, \"12\": 1, \"13\": 1, \"14\": 1, \"15\": 1, \"16\": 1, \"17\": 1, \"18\": 1, \"19\": 1, \"20\": 1, \"21\": 1, \"22\": 1, \"23\": 1, \"24\": 1, \"25\": 1, \"26\": 1, \"27\": 1, \"28\": 1, \"29\": 1, \"30\": 1, \"31\": 1, \"32\": 1}, \"layer0_detail\": \"predicts_only_class1_acc_0.158\", \"layer1_epochs\": 13, \"layers_2_32_epochs\": 6, \"gate_G1_GC\": \"PASS\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:54:35.688Z\"}, \"lg_extract_untrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T16:42:35.326Z\", \"updated_at\": \"2026-05-15T17:42:04.075Z\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"finished_at\": \"2026-05-15T17:41:31.327Z\"}, \"failure_reason\": \"Traceback → -packages/urllib3/util/connection.py\\\", line 85, in create_connection raise err File \\\"/root/miniconda3/lib/python3.12/site-packages/urllib3/util/connection.py\\\", line 73, in create_connection sock.connect(sa) OSError: [Errno 101] Network is unreachable\", \"completed_at\": \"2026-05-15T16:54:31.908Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:54:33.449692+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:41:32.343537+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 同 lg_extract_trained — AutoProcessor.from_pretrained() 网络不可达。提取进度到 22%。诊断 Worker: worker_diagnose_lg_extract_failed_20260515T165835\"}}, \"notes\": \"失败原因: 同 lg_extract_trained — AutoProcessor.from_pretrained() 网络不可达。提取进度到 22%。诊断 Worker: worker_diagnose_lg_extract_failed_20260515T165835\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"pid\": \"627335\", \"log_path\": \"~/runs/vla-ssd/lg_extract_untrained.log\", \"restarted_at\": \"2026-05-15T17:00:00Z\", \"retry_count\": 1, \"note\": \"--gpu 0 + CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/\"}, \"pid\": 627335, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"exit_code\": 0, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"note\": \"Retry after local_files_only fix. 2/10 from first run + 8/10 from retry.\"}}, \"lg_extract_trained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T16:42:33.477Z\", \"updated_at\": \"2026-05-15T17:41:46.136Z\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"finished_at\": \"2026-05-15T17:39:24.617Z\"}, \"failure_reason\": \"Traceback → -packages/urllib3/util/connection.py\\\", line 85, in create_connection raise err File \\\"/root/miniconda3/lib/python3.12/site-packages/urllib3/util/connection.py\\\", line 73, in create_connection sock.connect(sa) OSError: [Errno 101] Network is unreachable\", \"completed_at\": \"2026-05-15T16:54:26.701Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:54:27.826438+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:39:25.096897+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: AutoProcessor.from_pretrained() 连接 huggingface.co 失败 (Network is unreachable)，AutoDL 服务器网络未启用代理。日志显示提取进度到 52%（open_the_top_drawer task），说明模型可能从缓存加载成功但后续网络调用导致崩溃。诊断 Worker: worker_diagnose_lg_extract_failed_20260515T165835\"}}, \"notes\": \"Retry #1 after local_files_only fix. PID 627256 restarted ~17:00 UTC. Script skips completed h5 files (3/10 done from first run).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"pid\": \"627256\", \"log_path\": \"~/runs/vla-ssd/lg_extract_trained.log\", \"restarted_at\": \"2026-05-15T17:00:00Z\", \"retry_count\": 1, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"wall_clock_seconds\": 3204, \"gpu_hours\": 0.89}, \"pid\": 627256, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"extraction_time_min\": 53.4, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"exit_code\": 0, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"note\": \"Retry after local_files_only fix. 3/10 from first run + 7/10 from retry.\"}}, \"mvp2_action_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:10:18.939Z\", \"updated_at\": \"2026-05-15T17:30:12.186Z\", \"hypothesis\": \"VLA trained model hidden states encode action prediction knowledge (next action a_{t+1}) that untrained VLA and DINO-V2 lack. Gates: G1 R²>0.3, G2 Δ(trained-untrained)>0.15, G3 Δ(trained-DINO)>0.15\", \"parent\": \"mvp_001\", \"metrics\": {\"copy_baseline_R2\": 0.975, \"copy_baseline_per_task_mean_R2\": 0.972, \"random_frame_baseline_R2\": -0.91, \"random_frame_per_task_mean_R2\": -0.977, \"copy_baseline_per_dim_R2\": {\"dx\": 0.979, \"dy\": 0.988, \"dz\": 0.982, \"drx\": 0.971, \"dry\": 0.966, \"drz\": 0.991, \"grip\": 0.949}, \"note\": \"LIBERO action autocorrelation very high — copy a_t predicts a_{t+1} at R²=0.975. Action probe R² must be interpreted relative to this ceiling. Key comparison remains trained-vs-untrained Δ, not absolute R².\"}, \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - parent experiment, superseded by LIBERO-Goal pivot (D015)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"notes\": \"Superseded by LIBERO-Goal pivot (D015). Sub-experiments (mvp2_action_trained/untrained/dino, mvp2_delta_trained/untrained/dino) all completed as DONE. Parent umbrella experiment killed per Director instruction.\", \"completed_at\": \"2026-05-15T17:30:12.186Z\"}, \"lg_extract_untrained_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:23.059Z\", \"updated_at\": \"2026-05-15T17:11:52.014Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA. Fixed local_files_only=True. Continues from 2/10 tasks (skip existing).\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"Retry of lg_extract_untrained after local_files_only fix. Script uses --gpu 0 but CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1.\", \"pid\": \"627335\", \"log_path\": \"~/runs/vla-ssd/lg_extract_untrained.log\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:43.781Z\", \"notes\": \"Duplicate of original experiment lg_extract_untrained. Cleaned up per Director instruction.\"}, \"lg_extract_trained_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:18.970Z\", \"updated_at\": \"2026-05-15T17:11:51.155Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. Fixed local_files_only=True. Continues from 3/10 tasks (skip existing).\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"Retry of lg_extract_trained after local_files_only fix. Script skips completed .h5 files.\", \"pid\": \"627256\", \"log_path\": \"~/runs/vla-ssd/lg_extract_trained.log\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:42.929Z\", \"notes\": \"Duplicate of original experiment lg_extract_trained. Cleaned up per Director instruction.\"}, \"lg_extract_untrained_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:27.492Z\", \"updated_at\": \"2026-05-15T17:11:50.295Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA (random LLM + preserved SigLIP). Baseline for instruction probing.\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"retry of lg_extract_untrained after network failure, script uses --gpu 0 but CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"pid\": 627335, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:42.431Z\", \"notes\": \"Duplicate of original experiment lg_extract_untrained. Cleaned up per Director instruction.\"}, \"lg_extract_trained_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:23.268Z\", \"updated_at\": \"2026-05-15T17:11:49.214Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. OOD test. Fix: local_files_only=True, skip logic resumes from completed tasks.\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"retry of lg_extract_trained after network failure\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"pid\": 627256, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:41.473Z\", \"notes\": \"Duplicate of original experiment lg_extract_trained. Cleaned up per Director instruction.\"}, \"mvp2_delta_dino\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:23:29.771Z\", \"updated_at\": \"2026-05-15T16:00:24.789Z\", \"hypothesis\": \"DINO-V2 action-delta baseline (single layer) — establishes vision-only floor for G3 action-delta comparison\", \"parent\": \"mvp2_action_probe\", \"metrics\": {\"overall_R2\": 0.0604, \"per_task_mean_R2\": 0.0609, \"gripper_accuracy\": 0.57, \"per_dim_R2\": {\"dx\": 0.1744, \"dy\": 0.2588, \"dz\": 0.3745, \"drx\": 0.084, \"dry\": 0.0563, \"drz\": 0.1765, \"gripper\": 0.0365}, \"num_layers\": 1, \"feature_dim\": 1024}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_delta --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_source\": \"dinov2_baseline\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ + actions from libero_10\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/\"}, \"completed_at\": \"2026-05-15T16:00:24.789Z\"}, \"mvp2_delta_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:42:59.680Z\", \"updated_at\": \"2026-05-15T15:23:24.627Z\", \"hypothesis\": \"Action-delta prediction (Δa = a_{t+1}-a_t) on untrained VLA. Baseline for G2-delta comparison — expected lower R² than trained\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"617923\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_untrained.log\", \"submitted_at\": \"2026-05-15T14:43:14.724Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP action-delta probe (4096->256->7)\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ + actions from libero_10\", \"wall_clock_seconds\": 2409.9, \"gpu_hours\": 0.67}, \"metrics\": {\"best_layer\": 32, \"per_task_mean_R2\": 0.0485, \"overall_R2\": 0.0485, \"per_dim_R2_at_best\": {\"note\": \"L32 only layer with signal; L5-L28 all ≈ 0\"}, \"layer_stability\": \"catastrophic — layers 5-28 all R²≈0, only L1-L4 and L32 have signal\", \"collapsed_layers\": \"5,6,7,8,9,10,11,12,13,14,15,17,18,26,28\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained/action_delta/\", \"completed_at\": \"2026-05-15T15:23:24.627Z\"}, \"mvp2_delta_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:42:58.840Z\", \"updated_at\": \"2026-05-15T15:23:24.190Z\", \"hypothesis\": \"Action-delta prediction (Δa = a_{t+1}-a_t) removes autocorrelation. 33-layer sweep on trained VLA. Gate G1-delta: peak R²>0.05, G2-delta: Δ(trained-untrained)>0.03 in ≥5/10 tasks\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"617841\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_trained.log\", \"submitted_at\": \"2026-05-15T14:43:13.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP action-delta probe (4096->256->7)\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ + actions from libero_10\", \"wall_clock_seconds\": 2410.9, \"gpu_hours\": 0.67}, \"metrics\": {\"best_layer\": 14, \"per_task_mean_R2\": 0.0594, \"overall_R2\": 0.0594, \"per_dim_R2_at_best\": {\"dx\": 0.1783, \"dy\": 0.2665, \"dz\": 0.3576, \"drx\": 0.0942, \"dry\": 0.0511, \"drz\": 0.1735, \"gripper\": 0.0357}, \"layer_stability\": \"stable plateau 0.04-0.06 across layers 5-30, smooth curve\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained/action_delta/\", \"completed_at\": \"2026-05-15T15:23:24.190Z\"}, \"mvp2_action_dino\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:22:11.911Z\", \"updated_at\": \"2026-05-15T15:19:25.002Z\", \"hypothesis\": \"DINO-V2 ViT-L/14 action prediction baseline (single cls_token layer) — establishes vision-only floor for Gate G3 comparison\", \"parent\": \"mvp2_action_probe\", \"conclusion\": \"success\", \"metrics\": {\"overall_R2\": 0.6689, \"per_task_mean_R2\": 0.6759, \"gripper_accuracy\": 0.9001, \"epochs\": 17, \"training_time_seconds\": 7.3, \"num_layers\": 1, \"feature_dim\": 1024, \"feature_key\": \"cls_token\", \"probe_type\": \"MLP action probe (1024->256->7)\"}, \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_prediction --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_source\": \"dinov2_baseline\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ (10 tasks H5) + actions from libero_10\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/\"}, \"completed_at\": \"2026-05-15T14:22:47.835Z\"}, \"mvp2_action_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:17:44.922Z\", \"updated_at\": \"2026-05-15T14:46:17.287Z\", \"hypothesis\": \"Untrained VLA (random LLM + preserved vision) 33-layer action prediction baseline — expected lower R² than trained, establishing Δ for Gate G2\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"613477\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_untrained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/ + /root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim features + 7-dim actions\", \"model_name\": \"MLP action probe (4096->256->7), untrained openvla features\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ (10 tasks x 50 demos H5) + actions from /root/autodl-tmp/vla-ssd/data/libero/libero_10/\"}, \"metrics\": {\"best_layer\": 32, \"per_task_mean_R2\": 0.6164, \"overall_R2\": 0.6067, \"gripper_accuracy\": 0.8726, \"per_dim_R2_at_best\": {\"dx\": 0.5345, \"dy\": 0.7067, \"dz\": 0.5102, \"drx\": 0.3658, \"dry\": 0.2037, \"drz\": 0.6361, \"gripper\": 0.6066}, \"layers_unstable_range\": \"0.05-0.62 (many layers R²<0.25, probe likely not converging)\", \"layer_stability\": \"very low — wildly oscillating, multiple collapsed layers\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained/action_prediction/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:46:17.287Z\"}, \"mvp2_action_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:17:43.720Z\", \"updated_at\": \"2026-05-15T14:46:16.968Z\", \"hypothesis\": \"VLA trained model 33-layer action prediction sweep: per-layer R² distribution reveals where action knowledge is encoded. Gate G1: R²>0.3, G2: Δ(trained-untrained)>0.15\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"613335\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_trained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/ + /root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim features + 7-dim actions\", \"model_name\": \"MLP action probe (4096->256->7), trained on openvla-7b features\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ (10 tasks x 50 demos H5) + actions from /root/autodl-tmp/vla-ssd/data/libero/libero_10/\"}, \"metrics\": {\"best_layer\": 19, \"per_task_mean_R2\": 0.6831, \"overall_R2\": 0.677, \"gripper_accuracy\": 0.8989, \"per_dim_R2_at_best\": {\"dx\": 0.5885, \"dy\": 0.7629, \"dz\": 0.5854, \"drx\": 0.3712, \"dry\": 0.1649, \"drz\": 0.6654, \"gripper\": 0.6815}, \"layers_stable_range\": \"0.45-0.68 (31/33 layers > untrained)\", \"layer_stability\": \"high — smooth R² curve across all 33 layers\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained/action_prediction/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:46:16.968Z\"}, \"dinov2_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:05.849Z\", \"updated_at\": \"2026-05-15T14:15:20.188Z\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type temporal_distance --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps = 138,090 frames\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large, 304.4M params)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/\", \"feature_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ (503MB, 10 .pt files)\", \"probe_config\": \"MLP (1 hidden layer) trained with Adam + early stopping, task-level 80/20 split, distance-stratified sampling (10 bins x 50 pairs/bin/traj)\", \"feature_dim\": 1024, \"feature_key\": \"cls_token\", \"extraction_time\": \"795.8s, 174 fps, batch_size=32\"}, \"conclusion\": \"success\", \"metrics\": {\"temporal_distance_rho\": 0.833, \"temporal_distance_rho_pooled\": 0.833, \"per_task_rho_mean\": 0.9008, \"per_task_rho_range\": [0.41, 0.68], \"per_task_n_pairs\": 500, \"R2\": 0.687, \"MAE\": 0.127, \"feature_dim\": 1024, \"num_layers\": 1, \"probe_type\": \"mlp_adam_early_stopping\", \"training_time_seconds\": 7.5, \"note\": \"pooled ρ=0.833 inflated by cross-task variance; per-task mean ρ=0.9008 is correct comparison baseline (updated per D005/D006)\", \"subtask_macro_auc\": 0.9717, \"subtask_auc_per_predicate\": {\"subtask_0\": 0.9694, \"subtask_1\": 0.9739}, \"subtask_labels\": \"auto-extracted from MuJoCo state transitions (2 subtasks per task)\", \"subtask_probe_type\": \"sklearn_logistic_regression_lbfgs\", \"control_b_label_permutation_rho\": 0.039, \"control_b_label_permutation_per_task_mean\": 0.039, \"control_b_label_permutation_R2\": -0.052, \"cross_traj_rho\": 0.65, \"cross_traj_note\": \"supplementary analysis, not control; visual progress transfers across trajectories\"}, \"completed_at\": \"2026-05-15T11:24:37.420Z\"}, \"mvp_controlb_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:13:48.663Z\", \"spec\": {\"command\": \"python scripts/train_probes.py --shuffle-labels --untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-untrained\", \"seed\": 42, \"wall_clock_seconds\": 1377.0, \"gpu_hours\": 0.38, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\"}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mean_rho_across_layers\": 0.0003, \"mean_task_rho_across_layers\": 0.0003, \"best_layer_rho\": 0.0085, \"best_layer\": 1, \"mean_R2\": -0.0092, \"mean_MAE\": 0.2482, \"rho_std\": 0.0034, \"constant_prediction_layers\": 21, \"normal_experiment_rho\": 0.933, \"rho_ratio_normal_vs_shuffled\": 3110}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.504Z\"}, \"mvp_controlb_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:13:46.328Z\", \"spec\": {\"command\": \"python scripts/train_probes.py --shuffle-labels --trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-trained\", \"seed\": 42, \"wall_clock_seconds\": 1377.9, \"gpu_hours\": 0.38, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\"}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mean_rho_across_layers\": 0.0012, \"mean_task_rho_across_layers\": 0.0011, \"best_layer_rho\": 0.0123, \"best_layer\": 8, \"mean_R2\": -0.0041, \"mean_MAE\": 0.2478, \"rho_std\": 0.0051, \"all_layers_abs_rho_below_0.013\": true, \"normal_experiment_rho\": 0.955, \"rho_ratio_normal_vs_shuffled\": 783}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.105Z\"}, \"mvp_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:55:16.912Z\", \"updated_at\": \"2026-05-15T14:01:25.245Z\", \"hypothesis\": \"OpenVLA 7B 隐状态编码了 task-progress 信息（temporal distance），且信号来自 task-semantic content 而非 positional shortcut (RoPE)\", \"spec\": {\"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"model_name\": \"openvla/openvla-7b\", \"model_version\": \"HuggingFace main\", \"seed\": 42, \"gpu\": \"2xRTX PRO 6000\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"feature_path\": \"/root/vla-ssd/features/ (symlink to data disk)\", \"controls\": [\"Control A: timestep fraction oracle\", \"Control B: cross-trajectory shuffle\", \"Control C: untrained model baseline\", \"Control D: DINO-V2 ViT-L/14\"], \"pass_criteria\": \"best_layer rho>0.3 AND delta_rho(trained-untrained)>0.1 AND (VLA>=DINO-V2 OR subtask_AUC>0.7)\", \"command\": \"python scripts/extract_features.py (trained cuda:0 + untrained cuda:1)\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps = ~125K frames\", \"phase\": \"Phase 2 feature extraction\", \"tmux_sessions\": [\"openvla-trained-extract\", \"openvla-untrained-extract\"]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T14:01:16.724Z\", \"metrics\": {\"overall_verdict\": \"FAIL\", \"gate1_rho_pass\": true, \"gate2_delta_pass\": false, \"gate3_dino_pass\": true, \"best_layer\": 4, \"best_per_task_mean_rho\": 0.955, \"delta_rho_at_best\": 0.0427, \"dino_per_task_mean_rho\": 0.9008, \"collapsed_layers\": 16, \"healthy_layers\": 17, \"subtask_predicate_pivot_viable\": false, \"subtask_predicate_reason\": \"all LIBERO predicates visually observable, DINO AUC=0.9717\"}}, \"mvp_probe_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:24:31.814Z\", \"updated_at\": \"2026-05-15T13:55:20.999Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"606129\", \"log_path\": \"~/runs/vla-ssd/mvp_probe_untrained.log\", \"submitted_at\": \"2026-05-15T13:24:31.801Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP probe (1 hidden layer, Adam + early stopping)\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ (10 tasks x 50 demos H5)\", \"wall_clock_seconds\": 1638.6, \"gpu_hours\": 0.46}, \"hypothesis\": \"Control C: untrained OpenVLA (random LLM + preserved vision) temporal distance probe as baseline for Δρ comparison\", \"parent\": \"mvp_001\", \"reproduce\": {\"finished_at\": \"2026-05-15T13:46:43.876Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:46:45.174989+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.9334, \"note\": \"Control C baseline — untrained model (random LLM + preserved SigLIP vision encoder) already achieves ρ=0.933, confirming temporal distance signal is vision-dominated\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/\", \"completed_at\": \"2026-05-15T13:51:50.407Z\"}, \"mvp_probe_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:24:31.011Z\", \"updated_at\": \"2026-05-15T13:55:11.968Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"606050\", \"log_path\": \"~/runs/vla-ssd/mvp_probe_trained.log\", \"submitted_at\": \"2026-05-15T13:24:30.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP probe (1 hidden layer, Adam + early stopping)\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ (10 tasks x 50 demos H5)\", \"wall_clock_seconds\": 1634.3, \"gpu_hours\": 0.45}, \"hypothesis\": \"OpenVLA 7B trained model hidden states encode temporal distance (per-task mean ρ > 0.5), with signal from VLA training (Δρ vs untrained > 0.1)\", \"parent\": \"mvp_001\", \"reproduce\": {\"finished_at\": \"2026-05-15T13:46:42.038Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:46:42.772416+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained/temporal_distance/\", \"metrics\": {\"best_layer\": 4, \"best_per_task_mean_rho\": 0.955, \"best_pooled_rho\": 0.9556, \"delta_rho_at_best\": 0.0427, \"delta_rho_ci_95\": [0.0359, 0.0502], \"delta_rho_perm_p\": 0, \"gate1_rho_pass\": true, \"gate2_delta_pass\": false, \"gate3_dino_pass\": true, \"overall_verdict\": \"FAIL\", \"collapsed_layers\": 16, \"healthy_layers\": 17, \"dino_threshold\": 0.901, \"dino_per_task_mean_rho\": 0.9008}, \"completed_at\": \"2026-05-15T13:51:45.260Z\"}, \"openvla-untrained-extract\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T10:07:29.551Z\", \"updated_at\": \"2026-05-15T13:21:17.046Z\", \"notes\": \"1. 当前 untrained checkpoint 未使用固定 seed（init_untrained.py 缺 torch.manual_seed），但 checkpoint 已持久化到 /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/，可复现。脚本已补 seed=42 供将来使用。2. 日志中 mode=trained 为 extract_features.py 默认值，实际使用的是 openvla-7b-untrained checkpoint。3. EXIT_CODE=130 是 Worker(fix-extraction-restart) 主动 kill 以修复 I/O 瓶颈（264次 .cpu() → 2次/batch，52x 加速）。4. fix-extraction-restart Worker 补完 LIVING_ROOM_SCENE6 + STUDY_SCENE1（18.5 min），最终 10/10 tasks 全部完成。features/untrained/ 现有 10 个 .h5 文件，每个 50 demos。\", \"reproduce\": {\"finished_at\": \"2026-05-15T12:54:22.478Z\"}, \"failure_reason\": \"EXIT_CODE=130 (SIGINT / Ctrl-C)\", \"completed_at\": \"2026-05-15T12:54:27.745Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:54:28.598354+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"1. 当前 untrained checkpoint 未使用固定 seed（init_untrained.py 缺 torch.manual_seed），但 checkpoint 已持久化到 /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/，可复现。脚本已补 seed=42 供将来使用。2. 日志中 mode=trained 为 extract_features.py 默认值，实际使用的是 openvla-7b-untrained checkpoint。3. EXIT_CODE=130 是 Worker(fix-extraction-restart) 主动 kill 以修复 I/O 瓶颈（264次 .cpu() → 2次/batch）。8/10 tasks 已完成，剩 LIVING_ROOM_SCENE6 和 STUDY_SCENE1。Worker 正在修复脚本后重启提取剩余 2 tasks。\"}}, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"total_size_gb\": 52, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"io_fix_speedup\": \"52x (0.8→42 step/s)\", \"reextracted_tasks\": [\"LIVING_ROOM_SCENE6\", \"STUDY_SCENE1\"], \"reextraction_time_min\": 18.5}, \"spec\": {\"command\": \"python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir features/untrained/ --gpu 0 --max_demos 50 (retry: reextracted LIVING_ROOM_SCENE6 + STUDY_SCENE1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps\", \"model_name\": \"openvla/openvla-7b-untrained (LLM 6.74B random from_config, Vision 0.80B preserved)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"log_path\": \"~/runs/vla-ssd/openvla-untrained-extract.log\"}}, \"openvla-trained-extract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:01:11.067Z\", \"updated_at\": \"2026-05-15T13:12:48.634Z\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path openvla-7b --output_dir features/trained/ --gpu 0 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"27091\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"submitted_at\": \"2026-05-15T10:01:11.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps\", \"model_name\": \"openvla/openvla-7b\", \"seed\": 42, \"notes\": \"transformers 版本差异: 模型期望 4.40.1, 实际 4.57.6。trained/untrained 使用同一版本，对比有效。复现时需注意版本匹配。\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"wall_clock_seconds\": 11497.6, \"gpu_hours\": 3.19}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:07:39.142Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:07:39.880750+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"total_size_gb\": 53, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"extraction_time_min\": 185.3, \"exit_code\": 0}, \"completed_at\": \"2026-05-15T13:12:48.634Z\"}}, \"count\": 44, \"total\": 44, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2921}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The registry output is too large and was saved to a file. I need to read it in chunks. Let me read it to get all experiment details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "6e50032d-d635-4a61-8b16-4ac266025cda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG44zSFcNGRFcaMA7cEsrh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10679,
      "cache_read_input_tokens": 24878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10679
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

_source line 17_

Registry 太大，分块读取。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "52dbd6c1-245c-4422-ba8d-fd8989f3c25d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG44zSFcNGRFcaMA7cEsrh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10679,
      "cache_read_input_tokens": 24878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10679
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01VuPMw4MBhCxURLFdEpr5sV`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "1e20dbb1-6f90-4a17-8745-0f0127e2a6f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG44zSFcNGRFcaMA7cEsrh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10679,
      "cache_read_input_tokens": 24878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10679
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

_source line 19 · 2026-05-16T00:30:12.541Z_

<details><summary>↩ Tool result · reported error · `toolu_01VuPMw4MBhCxURLFdEpr5sV`</summary>

```text
File content (32670 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "5a274187-8f0c-4712-9b44-202fa516cf74",
  "tool_use_result": "Error: File content (32670 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_016kQAey6Wj98ojBQPUuVeBD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "58aaeee2-46c3-4cd2-b69d-be3c3de991a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhYJTFZgf7s6xQzgKCMBfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 35557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
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

_source line 21 · 2026-05-16T00:30:19.068Z_

<details><summary>↩ Tool result · reported error · `toolu_016kQAey6Wj98ojBQPUuVeBD`</summary>

```text
File content (32670 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "9c4ef2b3-d3e9-435d-b300-95935eb9734b",
  "tool_use_result": "Error: File content (32670 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01UwBxKxLykRdTKvTR5eix6h`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    eid = e.get('exp_id','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')[:120] if e.get('conclusion') else ''\n    metrics = e.get('metrics',{})\n    m_str = json.dumps(metrics)[:200] if metrics else '{}'\n    print(f'=== {eid} | {status} ===')\n    print(f'  conclusion: {conclusion}')\n    print(f'  metrics: {m_str}')\n    print()\n\"",
  "description": "Extract exp_id, status, conclusion, and metrics from registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "09473b38-2bd2-456f-8e69-21a17d4d8c0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnX5KdDXy4ke5uqRPkTvtr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 35832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
      },
      "output_tokens": 70,
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

_source line 23 · 2026-05-16T00:30:24.909Z_

<details><summary>↩ Tool result · reported error · `toolu_01UwBxKxLykRdTKvTR5eix6h`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    eid = e.get('exp_id','?')
          ^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "87717f4f-8544-4a34-ba9e-8c1ee615679f",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    eid = e.get('exp_id','?')\n          ^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01QPh15RiFbBEM53M1d4YeZh`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult_str = data['result']\nresult = json.loads(result_str)\ninner = result['data']\n# Check structure\nif isinstance(inner, dict) and 'experiments' in inner:\n    exps = inner['experiments']\nelif isinstance(inner, list):\n    exps = inner\nelse:\n    print(type(inner), list(inner.keys()) if isinstance(inner, dict) else 'N/A')\n    sys.exit(0)\nprint(f'Total experiments: {len(exps)}')\nprint(f'Type of first: {type(exps[0])}')\nif isinstance(exps[0], str):\n    # exps might be a dict with exp_id keys\n    print('First key:', exps[0][:200])\nelif isinstance(exps[0], dict):\n    print('First keys:', list(exps[0].keys())[:10])\n\"",
  "description": "Inspect registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "0ed440e7-d662-4360-a4e9-0250670cdc18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVcJgEj7nHqTXSpCJUSBrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 36067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 546
      },
      "output_tokens": 70,
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

_source line 25 · 2026-05-16T00:30:31.433Z_

<details><summary>↩ Tool result · reported error · `toolu_01QPh15RiFbBEM53M1d4YeZh`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 17, in &lt;module>
    print(f'Type of first: {type(exps[0])}')
                                 ~~~~^^^
KeyError: 0
Total experiments: 44
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "a3ed635f-15ad-4a23-9cfb-475a41276ad1",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 17, in &lt;module>\n    print(f'Type of first: {type(exps[0])}')\n                                 ~~~~^^^\nKeyError: 0\nTotal experiments: 44"
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01CBiUpLKfvWDUkK4dzsy6cN`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/a07025ac-e9d0-41a2-b15c-642972f33050/tool-results/mcp-agent-ml-research-read_registry-1778891407940.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# It's a dict with exp_id as keys\nfor eid, e in exps.items():\n    status = e.get('status','?')\n    conclusion = (e.get('conclusion','') or '')[:150]\n    metrics = e.get('metrics',{})\n    m_str = json.dumps(metrics)[:250] if metrics else '{}'\n    print(f'=== {eid} | {status} ===')\n    if conclusion:\n        print(f'  conclusion: {conclusion}')\n    print(f'  metrics: {m_str}')\n    print()\n\"",
  "description": "Extract all experiments from registry dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "7be0a40b-8e62-4789-84fd-cd96cb80202b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Xh9Ji2fMhSsKDphmLwGj5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 494,
      "cache_read_input_tokens": 36613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 494
      },
      "output_tokens": 70,
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

_source line 27 · 2026-05-16T00:30:36.484Z_

<details><summary>↩ Tool result · `toolu_01CBiUpLKfvWDUkK4dzsy6cN`</summary>

```text
=== untrained_last_preaction_probe | DONE ===
  conclusion: success
  metrics: {"untrained_last_preaction_L19_mean_R2": 0.325, "trained_last_preaction_L19_mean_R2": 0.7309, "projector_mean_R2": 0.706, "delta_trained_vs_untrained_L19": 0.406, "untrained_best_layer": "L32", "untrained_best_R2": 0.6858, "delta_best_vs_best": 0.045

=== plan_008_random_inst_control | RUNNING ===
  metrics: {}

=== plan_009_cka_verification | DONE ===
  conclusion: success
  metrics: {"linear_cka": {"untrained_img_mean_L23": 0.0894, "trained_img_mean_L23": 0.0834, "projector": 0.0809, "dino": 0.0664, "trained_last_preaction_L32": 0.127}, "rdm_cka": {"trained_img_mean_L23": 0.2599, "projector": 0.2568, "untrained_img_mean_L23": 0.

=== p0_functional_probe_v2 | DONE ===
  conclusion: success
  metrics: {"bootstrap_proj_vs_image_mean_L19": {"proj_mean_R2": 0.7063, "image_mean_L19_mean_R2": 0.6832, "delta": 0.0231, "ci_95": [0.0105, 0.0367], "p_value": 0.001, "gate": "PASS \u2014 CI lower bound > 0"}, "dino_action": {"mean_R2": 0.7116, "feature_key":

=== p0_functional_action_probe | DONE ===
  conclusion: success
  metrics: {"projector": {"mean_R2": 0.7063, "overall_R2": 0.7169, "grip_acc": 0.9221}, "image_mean_trained_L19": {"mean_R2": 0.6832, "overall_R2": 0.6961, "grip_acc": 0.9182}, "image_mean_trained_L23": {"mean_R2": 0.5736, "overall_R2": 0.59, "grip_acc": 0.8924

=== p0_functional_action_delta_probe | DONE ===
  conclusion: success
  metrics: {"projector": {"mean_R2": 0.1181, "overall_R2": 0.1053}, "trained_image_mean_L14": {"mean_R2": 0.1215, "overall_R2": 0.1091}, "untrained_best_L0": {"mean_R2": 0.1174, "overall_R2": 0.107}, "bootstrap_proj_vs_trained": {"delta": -0.0034, "ci_95": [-0.

=== p0_bootstrap_ci_training_effect | DONE ===
  conclusion: success
  metrics: {"image_mean": {"delta": 0.0206, "ci_95": [-0.0314, 0.0638], "p_value": 0.2, "significant": false}, "last_preaction": {"delta": 0.0076, "ci_95": [-0.0395, 0.0558], "p_value": 0.37, "significant": false}, "n_bootstrap": 10000, "n_tasks": 10, "conclusi

=== p0_image_mean_rsa_verify | DONE ===
  conclusion: success
  metrics: {"trained_image_mean_rsa": 0.5014, "trained_image_mean_peak_layer": 23, "trained_last_preaction_rsa": 0.4876, "untrained_image_mean_rsa": 0.4847, "untrained_image_mean_peak_layer": 23, "untrained_last_preaction_rsa": 0.4846, "siglip_projector_rsa": 0

=== plan_003_perlayer_degradation | DONE ===
  conclusion: success
  metrics: {"siglip_projector_rsa": 0.6153, "perlayer_summary": {"with_inst_trained": {"peak_rsa": 0.4876, "peak_layer": 9, "proj_to_l1_drop": 0.2036, "pattern": "non_monotonic"}, "with_inst_untrained": {"peak_rsa": 0.4846, "peak_layer": 12, "proj_to_l1_drop": 

=== lg_output_head_analysis | QUEUED ===
  conclusion: killed
  metrics: {}

=== lg_instruction_ablation | QUEUED ===
  conclusion: killed
  metrics: {}

=== d027_siglip_only_rsa | DONE ===
  conclusion: success
  metrics: {"siglip_projector_rsa": 0.6153, "bootstrap_95_ci": [0.5257, 0.6954], "comparison": {"siglip_projector": 0.6153, "trained_with_inst": 0.4876, "untrained_with_inst": 0.4846, "untrained_no_inst": 0.4802, "trained_no_inst": 0.489, "dino": 0.388}, "llm_d

=== d027_trained_no_inst_rsa | DONE ===
  conclusion: success
  metrics: {"trained_no_inst_peak_rsa": 0.489, "trained_no_inst_peak_layer": 30, "full_2x2_matrix": {"trained_with_inst": 0.4876, "trained_no_inst": 0.489, "untrained_with_inst": 0.4846, "untrained_no_inst": 0.4802, "dino": 0.388}, "training_effect_with_inst": 

=== d021_instruction_ablation | DONE ===
  conclusion: negative
  metrics: {"no_inst_untrained_peak_rsa": 0.4802, "with_inst_untrained_peak_rsa": 0.4846, "with_inst_trained_peak_rsa": 0.4876, "dino_rsa": 0.388, "delta_with_minus_no_inst": 0.0044, "gate_threshold_delta": 0.1, "gate_threshold_no_inst_max": 0.438, "gate_judgme

=== d021_output_head_analysis | DONE ===
  conclusion: negative
  metrics: {"group_summary": {"vision": {"count": 685, "mean_rel_change": 0, "cos_sim": 1, "verdict": "IDENTICAL"}, "projector": {"count": 6, "mean_rel_change": 0, "cos_sim": 1.001, "verdict": "IDENTICAL"}, "embedding": {"count": 1, "rel_change": 1.3287, "cos_s

=== lg_rsa_analysis | DONE ===
  conclusion: negative
  metrics: {"trained_peak_rsa": 0.4876, "trained_peak_layer": 9, "untrained_peak_rsa": 0.4846, "untrained_peak_layer": 12, "dino_rsa": 0.388, "delta_TU_at_trained_peak": 0.003, "delta_TU_range": [-0.0722, 0.0109], "layers_trained_gt_untrained": 4, "layers_total

=== lg_shuffled_token_control | DONE ===
  conclusion: killed
  metrics: {}

=== lg_pca1024_linear_pertimestep | DONE ===
  conclusion: negative
  metrics: {"bin_0_trained": 0.9992, "bin_0_untrained": 1, "bin_0_dino": 0.354, "bin_0_delta_TU": -0.0008, "overall_trained": 0.9999, "overall_untrained": 1, "overall_dino": 0.8397, "per_bin": {"0": {"trained": 0.9992, "untrained": 1, "dino": 0.354}, "1": {"tra

=== lg_gc_trained_frame0 | DONE ===
  conclusion: success
  metrics: {"trained_best_layer": 3, "trained_best_acc": 1, "trained_best_f1": 1, "untrained_best_layer": 2, "untrained_best_acc": 1, "untrained_best_f1": 1, "dino_best_acc": 0.15, "dino_best_f1": 0.0911, "n_classes": 10, "n_train": 400, "n_val": 100, "trained_

=== lg_gc_untrained | DONE ===
  conclusion: negative
  metrics: {"best_layer": 1, "best_accuracy": 1, "best_traj_accuracy": 1, "best_macro_f1": 1, "worst_layer": 31, "worst_accuracy": 0.9971, "n_classes": 10, "n_train": 50880, "n_val": 12848, "per_layer_accuracies": {"0": 0.1582, "1": 1, "2": 1, "3": 1, "4": 1, "

=== lg_gc_dino | DONE ===
  conclusion: success
  metrics: {"best_accuracy": 0.8626, "best_traj_accuracy": 1, "best_macro_f1": 0.8412, "n_classes": 10, "num_layers": 1, "feature_dim": 1024, "gate_Sanity_GC": "FAIL", "note": "DINO acc 86.26% >> 25% threshold. Goals are visually distinguishable. Sanity-GC gate

=== lg_dino_extract | DONE ===
  conclusion: success
  metrics: {"tasks_completed": 10, "tasks_total": 10, "demos_per_task": 50, "total_frames": 63728, "feature_dim": 1024, "dtype": "float16", "feature_keys": ["cls_token", "patch_mean"], "file_count": 10, "total_size_mb": 234, "extraction_fps": 183, "extraction_t

=== lg_gc_trained | DONE ===
  conclusion: success
  metrics: {"best_layer": 1, "best_accuracy": 1, "best_traj_accuracy": 1, "best_macro_f1": 1, "n_classes": 10, "n_train": 50880, "n_val": 12848, "per_layer_accuracies": {"0": 0.1582, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1, "10": 

=== lg_extract_untrained | DONE ===
  conclusion: success
  metrics: {"tasks_completed": "10/10", "feature_dim": 4096, "num_layers": 33, "dtype": "float16", "demos_per_task": 50, "exit_code": 0, "feature_keys": ["image_mean", "last_preaction"], "note": "Retry after local_files_only fix. 2/10 from first run + 8/10 from

=== lg_extract_trained | DONE ===
  conclusion: success
  metrics: {"tasks_completed": "10/10", "extraction_time_min": 53.4, "feature_dim": 4096, "num_layers": 33, "dtype": "float16", "demos_per_task": 50, "exit_code": 0, "feature_keys": ["image_mean", "last_preaction"], "note": "Retry after local_files_only fix. 3/

=== mvp2_action_probe | DONE ===
  conclusion: killed
  metrics: {"copy_baseline_R2": 0.975, "copy_baseline_per_task_mean_R2": 0.972, "random_frame_baseline_R2": -0.91, "random_frame_per_task_mean_R2": -0.977, "copy_baseline_per_dim_R2": {"dx": 0.979, "dy": 0.988, "dz": 0.982, "drx": 0.971, "dry": 0.966, "drz": 0.

=== lg_extract_untrained_r2 | DONE ===
  conclusion: killed
  metrics: {}

=== lg_extract_trained_r2 | DONE ===
  conclusion: killed
  metrics: {}

=== lg_extract_untrained_r1 | DONE ===
  conclusion: killed
  metrics: {}

=== lg_extract_trained_r1 | DONE ===
  conclusion: killed
  metrics: {}

=== mvp2_delta_dino | DONE ===
  conclusion: success
  metrics: {"overall_R2": 0.0604, "per_task_mean_R2": 0.0609, "gripper_accuracy": 0.57, "per_dim_R2": {"dx": 0.1744, "dy": 0.2588, "dz": 0.3745, "drx": 0.084, "dry": 0.0563, "drz": 0.1765, "gripper": 0.0365}, "num_layers": 1, "feature_dim": 1024}

=== mvp2_delta_untrained | DONE ===
  conclusion: success
  metrics: {"best_layer": 32, "per_task_mean_R2": 0.0485, "overall_R2": 0.0485, "per_dim_R2_at_best": {"note": "L32 only layer with signal; L5-L28 all \u2248 0"}, "layer_stability": "catastrophic \u2014 layers 5-28 all R\u00b2\u22480, only L1-L4 and L32 have si

=== mvp2_delta_trained | DONE ===
  conclusion: success
  metrics: {"best_layer": 14, "per_task_mean_R2": 0.0594, "overall_R2": 0.0594, "per_dim_R2_at_best": {"dx": 0.1783, "dy": 0.2665, "dz": 0.3576, "drx": 0.0942, "dry": 0.0511, "drz": 0.1735, "gripper": 0.0357}, "layer_stability": "stable plateau 0.04-0.06 across

=== mvp2_action_dino | DONE ===
  conclusion: success
  metrics: {"overall_R2": 0.6689, "per_task_mean_R2": 0.6759, "gripper_accuracy": 0.9001, "epochs": 17, "training_time_seconds": 7.3, "num_layers": 1, "feature_dim": 1024, "feature_key": "cls_token", "probe_type": "MLP action probe (1024->256->7)"}

=== mvp2_action_untrained | DONE ===
  conclusion: success
  metrics: {"best_layer": 32, "per_task_mean_R2": 0.6164, "overall_R2": 0.6067, "gripper_accuracy": 0.8726, "per_dim_R2_at_best": {"dx": 0.5345, "dy": 0.7067, "dz": 0.5102, "drx": 0.3658, "dry": 0.2037, "drz": 0.6361, "gripper": 0.6066}, "layers_unstable_range"

=== mvp2_action_trained | DONE ===
  conclusion: success
  metrics: {"best_layer": 19, "per_task_mean_R2": 0.6831, "overall_R2": 0.677, "gripper_accuracy": 0.8989, "per_dim_R2_at_best": {"dx": 0.5885, "dy": 0.7629, "dz": 0.5854, "drx": 0.3712, "dry": 0.1649, "drz": 0.6654, "gripper": 0.6815}, "layers_stable_range": "

=== dinov2_baseline | DONE ===
  conclusion: success
  metrics: {"temporal_distance_rho": 0.833, "temporal_distance_rho_pooled": 0.833, "per_task_rho_mean": 0.9008, "per_task_rho_range": [0.41, 0.68], "per_task_n_pairs": 500, "R2": 0.687, "MAE": 0.127, "feature_dim": 1024, "num_layers": 1, "probe_type": "mlp_adam

=== mvp_controlb_untrained | DONE ===
  conclusion: success
  metrics: {"mean_rho_across_layers": 0.0003, "mean_task_rho_across_layers": 0.0003, "best_layer_rho": 0.0085, "best_layer": 1, "mean_R2": -0.0092, "mean_MAE": 0.2482, "rho_std": 0.0034, "constant_prediction_layers": 21, "normal_experiment_rho": 0.933, "rho_rat

=== mvp_controlb_trained | DONE ===
  conclusion: success
  metrics: {"mean_rho_across_layers": 0.0012, "mean_task_rho_across_layers": 0.0011, "best_layer_rho": 0.0123, "best_layer": 8, "mean_R2": -0.0041, "mean_MAE": 0.2478, "rho_std": 0.0051, "all_layers_abs_rho_below_0.013": true, "normal_experiment_rho": 0.955, "r

=== mvp_001 | DONE ===
  conclusion: negative
  metrics: {"overall_verdict": "FAIL", "gate1_rho_pass": true, "gate2_delta_pass": false, "gate3_dino_pass": true, "best_layer": 4, "best_per_task_mean_rho": 0.955, "delta_rho_at_best": 0.0427, "dino_per_task_mean_rho": 0.9008, "collapsed_layers": 16, "healthy_

=== mvp_probe_untrained | DONE ===
  conclusion: success
  metrics: {"best_layer": 1, "best_per_task_mean_rho": 0.9334, "note": "Control C baseline \u2014 untrained model (random LLM + preserved SigLIP vision encoder) already achieves \u03c1=0.933, confirming temporal distance signal is vision-dominated"}

=== mvp_probe_trained | DONE ===
  conclusion: negative
  metrics: {"best_layer": 4, "best_per_task_mean_rho": 0.955, "best_pooled_rho": 0.9556, "delta_rho_at_best": 0.0427, "delta_rho_ci_95": [0.0359, 0.0502], "delta_rho_perm_p": 0, "gate1_rho_pass": true, "gate2_delta_pass": false, "gate3_dino_pass": true, "overal

=== openvla-untrained-extract | DONE ===
  conclusion: success
  metrics: {"tasks_completed": "10/10", "total_size_gb": 52, "feature_dim": 4096, "num_layers": 33, "dtype": "float16", "demos_per_task": 50, "feature_keys": ["image_mean", "last_preaction"], "io_fix_speedup": "52x (0.8\u219242 step/s)", "reextracted_tasks": ["

=== openvla-trained-extract | DONE ===
  conclusion: success
  metrics: {"tasks_completed": "10/10", "total_size_gb": 53, "feature_dim": 4096, "num_layers": 33, "dtype": "float16", "demos_per_task": 50, "feature_keys": ["image_mean", "last_preaction"], "extraction_time_min": 185.3, "exit_code": 0}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "43328f2d-1152-40c3-8831-87ec24592de6",
  "tool_use_result": {
    "stdout": "=== untrained_last_preaction_probe | DONE ===\n  conclusion: success\n  metrics: {\"untrained_last_preaction_L19_mean_R2\": 0.325, \"trained_last_preaction_L19_mean_R2\": 0.7309, \"projector_mean_R2\": 0.706, \"delta_trained_vs_untrained_L19\": 0.406, \"untrained_best_layer\": \"L32\", \"untrained_best_R2\": 0.6858, \"delta_best_vs_best\": 0.045\n\n=== plan_008_random_inst_control | RUNNING ===\n  metrics: {}\n\n=== plan_009_cka_verification | DONE ===\n  conclusion: success\n  metrics: {\"linear_cka\": {\"untrained_img_mean_L23\": 0.0894, \"trained_img_mean_L23\": 0.0834, \"projector\": 0.0809, \"dino\": 0.0664, \"trained_last_preaction_L32\": 0.127}, \"rdm_cka\": {\"trained_img_mean_L23\": 0.2599, \"projector\": 0.2568, \"untrained_img_mean_L23\": 0.\n\n=== p0_functional_probe_v2 | DONE ===\n  conclusion: success\n  metrics: {\"bootstrap_proj_vs_image_mean_L19\": {\"proj_mean_R2\": 0.7063, \"image_mean_L19_mean_R2\": 0.6832, \"delta\": 0.0231, \"ci_95\": [0.0105, 0.0367], \"p_value\": 0.001, \"gate\": \"PASS \\u2014 CI lower bound > 0\"}, \"dino_action\": {\"mean_R2\": 0.7116, \"feature_key\":\n\n=== p0_functional_action_probe | DONE ===\n  conclusion: success\n  metrics: {\"projector\": {\"mean_R2\": 0.7063, \"overall_R2\": 0.7169, \"grip_acc\": 0.9221}, \"image_mean_trained_L19\": {\"mean_R2\": 0.6832, \"overall_R2\": 0.6961, \"grip_acc\": 0.9182}, \"image_mean_trained_L23\": {\"mean_R2\": 0.5736, \"overall_R2\": 0.59, \"grip_acc\": 0.8924\n\n=== p0_functional_action_delta_probe | DONE ===\n  conclusion: success\n  metrics: {\"projector\": {\"mean_R2\": 0.1181, \"overall_R2\": 0.1053}, \"trained_image_mean_L14\": {\"mean_R2\": 0.1215, \"overall_R2\": 0.1091}, \"untrained_best_L0\": {\"mean_R2\": 0.1174, \"overall_R2\": 0.107}, \"bootstrap_proj_vs_trained\": {\"delta\": -0.0034, \"ci_95\": [-0.\n\n=== p0_bootstrap_ci_training_effect | DONE ===\n  conclusion: success\n  metrics: {\"image_mean\": {\"delta\": 0.0206, \"ci_95\": [-0.0314, 0.0638], \"p_value\": 0.2, \"significant\": false}, \"last_preaction\": {\"delta\": 0.0076, \"ci_95\": [-0.0395, 0.0558], \"p_value\": 0.37, \"significant\": false}, \"n_bootstrap\": 10000, \"n_tasks\": 10, \"conclusi\n\n=== p0_image_mean_rsa_verify | DONE ===\n  conclusion: success\n  metrics: {\"trained_image_mean_rsa\": 0.5014, \"trained_image_mean_peak_layer\": 23, \"trained_last_preaction_rsa\": 0.4876, \"untrained_image_mean_rsa\": 0.4847, \"untrained_image_mean_peak_layer\": 23, \"untrained_last_preaction_rsa\": 0.4846, \"siglip_projector_rsa\": 0\n\n=== plan_003_perlayer_degradation | DONE ===\n  conclusion: success\n  metrics: {\"siglip_projector_rsa\": 0.6153, \"perlayer_summary\": {\"with_inst_trained\": {\"peak_rsa\": 0.4876, \"peak_layer\": 9, \"proj_to_l1_drop\": 0.2036, \"pattern\": \"non_monotonic\"}, \"with_inst_untrained\": {\"peak_rsa\": 0.4846, \"peak_layer\": 12, \"proj_to_l1_drop\": \n\n=== lg_output_head_analysis | QUEUED ===\n  conclusion: killed\n  metrics: {}\n\n=== lg_instruction_ablation | QUEUED ===\n  conclusion: killed\n  metrics: {}\n\n=== d027_siglip_only_rsa | DONE ===\n  conclusion: success\n  metrics: {\"siglip_projector_rsa\": 0.6153, \"bootstrap_95_ci\": [0.5257, 0.6954], \"comparison\": {\"siglip_projector\": 0.6153, \"trained_with_inst\": 0.4876, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"trained_no_inst\": 0.489, \"dino\": 0.388}, \"llm_d\n\n=== d027_trained_no_inst_rsa | DONE ===\n  conclusion: success\n  metrics: {\"trained_no_inst_peak_rsa\": 0.489, \"trained_no_inst_peak_layer\": 30, \"full_2x2_matrix\": {\"trained_with_inst\": 0.4876, \"trained_no_inst\": 0.489, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"dino\": 0.388}, \"training_effect_with_inst\": \n\n=== d021_instruction_ablation | DONE ===\n  conclusion: negative\n  metrics: {\"no_inst_untrained_peak_rsa\": 0.4802, \"with_inst_untrained_peak_rsa\": 0.4846, \"with_inst_trained_peak_rsa\": 0.4876, \"dino_rsa\": 0.388, \"delta_with_minus_no_inst\": 0.0044, \"gate_threshold_delta\": 0.1, \"gate_threshold_no_inst_max\": 0.438, \"gate_judgme\n\n=== d021_output_head_analysis | DONE ===\n  conclusion: negative\n  metrics: {\"group_summary\": {\"vision\": {\"count\": 685, \"mean_rel_change\": 0, \"cos_sim\": 1, \"verdict\": \"IDENTICAL\"}, \"projector\": {\"count\": 6, \"mean_rel_change\": 0, \"cos_sim\": 1.001, \"verdict\": \"IDENTICAL\"}, \"embedding\": {\"count\": 1, \"rel_change\": 1.3287, \"cos_s\n\n=== lg_rsa_analysis | DONE ===\n  conclusion: negative\n  metrics: {\"trained_peak_rsa\": 0.4876, \"trained_peak_layer\": 9, \"untrained_peak_rsa\": 0.4846, \"untrained_peak_layer\": 12, \"dino_rsa\": 0.388, \"delta_TU_at_trained_peak\": 0.003, \"delta_TU_range\": [-0.0722, 0.0109], \"layers_trained_gt_untrained\": 4, \"layers_total\n\n=== lg_shuffled_token_control | DONE ===\n  conclusion: killed\n  metrics: {}\n\n=== lg_pca1024_linear_pertimestep | DONE ===\n  conclusion: negative\n  metrics: {\"bin_0_trained\": 0.9992, \"bin_0_untrained\": 1, \"bin_0_dino\": 0.354, \"bin_0_delta_TU\": -0.0008, \"overall_trained\": 0.9999, \"overall_untrained\": 1, \"overall_dino\": 0.8397, \"per_bin\": {\"0\": {\"trained\": 0.9992, \"untrained\": 1, \"dino\": 0.354}, \"1\": {\"tra\n\n=== lg_gc_trained_frame0 | DONE ===\n  conclusion: success\n  metrics: {\"trained_best_layer\": 3, \"trained_best_acc\": 1, \"trained_best_f1\": 1, \"untrained_best_layer\": 2, \"untrained_best_acc\": 1, \"untrained_best_f1\": 1, \"dino_best_acc\": 0.15, \"dino_best_f1\": 0.0911, \"n_classes\": 10, \"n_train\": 400, \"n_val\": 100, \"trained_\n\n=== lg_gc_untrained | DONE ===\n  conclusion: negative\n  metrics: {\"best_layer\": 1, \"best_accuracy\": 1, \"best_traj_accuracy\": 1, \"best_macro_f1\": 1, \"worst_layer\": 31, \"worst_accuracy\": 0.9971, \"n_classes\": 10, \"n_train\": 50880, \"n_val\": 12848, \"per_layer_accuracies\": {\"0\": 0.1582, \"1\": 1, \"2\": 1, \"3\": 1, \"4\": 1, \"\n\n=== lg_gc_dino | DONE ===\n  conclusion: success\n  metrics: {\"best_accuracy\": 0.8626, \"best_traj_accuracy\": 1, \"best_macro_f1\": 0.8412, \"n_classes\": 10, \"num_layers\": 1, \"feature_dim\": 1024, \"gate_Sanity_GC\": \"FAIL\", \"note\": \"DINO acc 86.26% >> 25% threshold. Goals are visually distinguishable. Sanity-GC gate\n\n=== lg_dino_extract | DONE ===\n  conclusion: success\n  metrics: {\"tasks_completed\": 10, \"tasks_total\": 10, \"demos_per_task\": 50, \"total_frames\": 63728, \"feature_dim\": 1024, \"dtype\": \"float16\", \"feature_keys\": [\"cls_token\", \"patch_mean\"], \"file_count\": 10, \"total_size_mb\": 234, \"extraction_fps\": 183, \"extraction_t\n\n=== lg_gc_trained | DONE ===\n  conclusion: success\n  metrics: {\"best_layer\": 1, \"best_accuracy\": 1, \"best_traj_accuracy\": 1, \"best_macro_f1\": 1, \"n_classes\": 10, \"n_train\": 50880, \"n_val\": 12848, \"per_layer_accuracies\": {\"0\": 0.1582, \"1\": 1, \"2\": 1, \"3\": 1, \"4\": 1, \"5\": 1, \"6\": 1, \"7\": 1, \"8\": 1, \"9\": 1, \"10\": \n\n=== lg_extract_untrained | DONE ===\n  conclusion: success\n  metrics: {\"tasks_completed\": \"10/10\", \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"exit_code\": 0, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"note\": \"Retry after local_files_only fix. 2/10 from first run + 8/10 from\n\n=== lg_extract_trained | DONE ===\n  conclusion: success\n  metrics: {\"tasks_completed\": \"10/10\", \"extraction_time_min\": 53.4, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"exit_code\": 0, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"note\": \"Retry after local_files_only fix. 3/\n\n=== mvp2_action_probe | DONE ===\n  conclusion: killed\n  metrics: {\"copy_baseline_R2\": 0.975, \"copy_baseline_per_task_mean_R2\": 0.972, \"random_frame_baseline_R2\": -0.91, \"random_frame_per_task_mean_R2\": -0.977, \"copy_baseline_per_dim_R2\": {\"dx\": 0.979, \"dy\": 0.988, \"dz\": 0.982, \"drx\": 0.971, \"dry\": 0.966, \"drz\": 0.\n\n=== lg_extract_untrained_r2 | DONE ===\n  conclusion: killed\n  metrics: {}\n\n=== lg_extract_trained_r2 | DONE ===\n  conclusion: killed\n  metrics: {}\n\n=== lg_extract_untrained_r1 | DONE ===\n  conclusion: killed\n  metrics: {}\n\n=== lg_extract_trained_r1 | DONE ===\n  conclusion: killed\n  metrics: {}\n\n=== mvp2_delta_dino | DONE ===\n  conclusion: success\n  metrics: {\"overall_R2\": 0.0604, \"per_task_mean_R2\": 0.0609, \"gripper_accuracy\": 0.57, \"per_dim_R2\": {\"dx\": 0.1744, \"dy\": 0.2588, \"dz\": 0.3745, \"drx\": 0.084, \"dry\": 0.0563, \"drz\": 0.1765, \"gripper\": 0.0365}, \"num_layers\": 1, \"feature_dim\": 1024}\n\n=== mvp2_delta_untrained | DONE ===\n  conclusion: success\n  metrics: {\"best_layer\": 32, \"per_task_mean_R2\": 0.0485, \"overall_R2\": 0.0485, \"per_dim_R2_at_best\": {\"note\": \"L32 only layer with signal; L5-L28 all \\u2248 0\"}, \"layer_stability\": \"catastrophic \\u2014 layers 5-28 all R\\u00b2\\u22480, only L1-L4 and L32 have si\n\n=== mvp2_delta_trained | DONE ===\n  conclusion: success\n  metrics: {\"best_layer\": 14, \"per_task_mean_R2\": 0.0594, \"overall_R2\": 0.0594, \"per_dim_R2_at_best\": {\"dx\": 0.1783, \"dy\": 0.2665, \"dz\": 0.3576, \"drx\": 0.0942, \"dry\": 0.0511, \"drz\": 0.1735, \"gripper\": 0.0357}, \"layer_stability\": \"stable plateau 0.04-0.06 across\n\n=== mvp2_action_dino | DONE ===\n  conclusion: success\n  metrics: {\"overall_R2\": 0.6689, \"per_task_mean_R2\": 0.6759, \"gripper_accuracy\": 0.9001, \"epochs\": 17, \"training_time_seconds\": 7.3, \"num_layers\": 1, \"feature_dim\": 1024, \"feature_key\": \"cls_token\", \"probe_type\": \"MLP action probe (1024->256->7)\"}\n\n=== mvp2_action_untrained | DONE ===\n  conclusion: success\n  metrics: {\"best_layer\": 32, \"per_task_mean_R2\": 0.6164, \"overall_R2\": 0.6067, \"gripper_accuracy\": 0.8726, \"per_dim_R2_at_best\": {\"dx\": 0.5345, \"dy\": 0.7067, \"dz\": 0.5102, \"drx\": 0.3658, \"dry\": 0.2037, \"drz\": 0.6361, \"gripper\": 0.6066}, \"layers_unstable_range\"\n\n=== mvp2_action_trained | DONE ===\n  conclusion: success\n  metrics: {\"best_layer\": 19, \"per_task_mean_R2\": 0.6831, \"overall_R2\": 0.677, \"gripper_accuracy\": 0.8989, \"per_dim_R2_at_best\": {\"dx\": 0.5885, \"dy\": 0.7629, \"dz\": 0.5854, \"drx\": 0.3712, \"dry\": 0.1649, \"drz\": 0.6654, \"gripper\": 0.6815}, \"layers_stable_range\": \"\n\n=== dinov2_baseline | DONE ===\n  conclusion: success\n  metrics: {\"temporal_distance_rho\": 0.833, \"temporal_distance_rho_pooled\": 0.833, \"per_task_rho_mean\": 0.9008, \"per_task_rho_range\": [0.41, 0.68], \"per_task_n_pairs\": 500, \"R2\": 0.687, \"MAE\": 0.127, \"feature_dim\": 1024, \"num_layers\": 1, \"probe_type\": \"mlp_adam\n\n=== mvp_controlb_untrained | DONE ===\n  conclusion: success\n  metrics: {\"mean_rho_across_layers\": 0.0003, \"mean_task_rho_across_layers\": 0.0003, \"best_layer_rho\": 0.0085, \"best_layer\": 1, \"mean_R2\": -0.0092, \"mean_MAE\": 0.2482, \"rho_std\": 0.0034, \"constant_prediction_layers\": 21, \"normal_experiment_rho\": 0.933, \"rho_rat\n\n=== mvp_controlb_trained | DONE ===\n  conclusion: success\n  metrics: {\"mean_rho_across_layers\": 0.0012, \"mean_task_rho_across_layers\": 0.0011, \"best_layer_rho\": 0.0123, \"best_layer\": 8, \"mean_R2\": -0.0041, \"mean_MAE\": 0.2478, \"rho_std\": 0.0051, \"all_layers_abs_rho_below_0.013\": true, \"normal_experiment_rho\": 0.955, \"r\n\n=== mvp_001 | DONE ===\n  conclusion: negative\n  metrics: {\"overall_verdict\": \"FAIL\", \"gate1_rho_pass\": true, \"gate2_delta_pass\": false, \"gate3_dino_pass\": true, \"best_layer\": 4, \"best_per_task_mean_rho\": 0.955, \"delta_rho_at_best\": 0.0427, \"dino_per_task_mean_rho\": 0.9008, \"collapsed_layers\": 16, \"healthy_\n\n=== mvp_probe_untrained | DONE ===\n  conclusion: success\n  metrics: {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.9334, \"note\": \"Control C baseline \\u2014 untrained model (random LLM + preserved SigLIP vision encoder) already achieves \\u03c1=0.933, confirming temporal distance signal is vision-dominated\"}\n\n=== mvp_probe_trained | DONE ===\n  conclusion: negative\n  metrics: {\"best_layer\": 4, \"best_per_task_mean_rho\": 0.955, \"best_pooled_rho\": 0.9556, \"delta_rho_at_best\": 0.0427, \"delta_rho_ci_95\": [0.0359, 0.0502], \"delta_rho_perm_p\": 0, \"gate1_rho_pass\": true, \"gate2_delta_pass\": false, \"gate3_dino_pass\": true, \"overal\n\n=== openvla-untrained-extract | DONE ===\n  conclusion: success\n  metrics: {\"tasks_completed\": \"10/10\", \"total_size_gb\": 52, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"io_fix_speedup\": \"52x (0.8\\u219242 step/s)\", \"reextracted_tasks\": [\"\n\n=== openvla-trained-extract | DONE ===\n  conclusion: success\n  metrics: {\"tasks_completed\": \"10/10\", \"total_size_gb\": 53, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"extraction_time_min\": 185.3, \"exit_code\": 0}",
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

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me organize the experiments by their relevance to each claim and draft the writing_plan.yaml.

Key experiments and their IDs:
1. **Claim 1 (Vision Encoder Dominance)**:
   - `d027_siglip_only_rsa`: SigLIP+Projector RSA=0.615 [CI: 0.526, 0.695]
   - `lg_rsa_analysis`: trained peak RSA=0.4876, untrained peak=0.4846, DINO=0.388
   - `p0_functional_action_probe`: Projector R²=0.706 versus image_mean trained L19 R²=0.683
   - `p0_functional_probe_v2`: DINO R²=0.712 nearly matches Projector 0.706 (p=0.22), showing geometric-functional dissociation
   - `p0_functional_action_delta_probe` and `dinov2_baseline` for additional functional comparisons

2. **Claim 2 (LLM Redistributes)**:
   - `plan_003_perlayer_degradation`: per-layer RSA curve tracking how the projector transforms representations across layers, with L1 showing the biggest drop
   - `p0_functional_action_probe`: readout at L19 reaches R²=0.731, exceeding the projector's 0.706
   - `p0_image_mean_rsa_verify`: image_mean RSA=0.501 falls short of projector's 0.615
   - `plan_009_cka_verification`: CKA results reveal ordering reversals between representations
   - `untrained_last_preaction_probe`: untrained readout at L32 yields R²=0.686, below the projector baseline

3. **Claim 3 (Training = Routing)**:
   - `p0_bootstrap_ci_training_effect`: image_mean shows Δ=0.021 with confidence interval including zero, last_preaction shows Δ=0.008 also with zero in CI
   - `d021_instruction_ablation`: comparing no-instruction versus instruction conditions shows minimal difference

Looking at the RSA metrics more closely, I'm seeing the trained no-instruction variant reaches 0.489, while the untrained last_preaction probe shows a significant Δ=0.045 between trained and untrained conditions with tight confidence bounds [0.032, 0.058] and strong statistical significance. The vision backbone analysis confirms identical architecture between trained and untrained versions, and there's an ongoing control experiment with random instructions to validate the findings.

Now I'm compiling the functional probe R² values across all conditions and comparing them against the RSA results. The trained last_preaction layer achieves the highest R² at 0.731, while untrained image_mean reaches 0.714, suggesting different optimal probing points depending on training status. I'm organizing these into a figure plan that includes the conceptual architecture showing the VLA pipeline decomposition with probe locations, RSA comparisons across all baselines, per-layer degradation curves for the four main conditions, and the functional probe performance summary.

For the paper structure, I'm planning to lead with experiments to establish the empirical findings, then formalize the methodology, and finally craft the introduction once the narrative arc is clear. I'll need to ensure Grant et al. 2026 and Karam are properly cited for the foundational work on visual dominance in behavioral tasks.

Looking at the key literature I need to cover: there's a cluster of recent work on vision-language-action models—Prismatic and OpenVLA architectures, studies on how fine-tuning affects reasoning capabilities, activation steering approaches, and mechanistic interpretability work through linear probing and sparse autoencoders. I also want to ground this in the broader context of emergent world representations and task-specific adaptation.

For the image_mean RSA values, I'm seeing the trained condition with instructions yields 0.501 while the untrained version comes in at 0.485, which suggests a meaningful but modest effect from training.

Now I'm cross-checking these against the actual metrics—the verification data shows trained_image_mean_rsa at 0.5014 and untrained at 0.4847, which aligns closely. The earlier lg_rsa_analysis using last_preaction as the reference point gave me different peak layers (L9 for trained, L12 for untrained), but when I switch to image_mean as the baseline, both conditions peak at L23. I'm ready to structure this into the YAML configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "54522b31-f720-4017-a94b-3fa129c253c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hrg7MSPA2UhAMzuAfhrApS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5650,
      "cache_read_input_tokens": 37107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5650
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

_source line 29_

全部数据收集完毕。开始起草 writing_plan.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "608eea4a-e7d4-4913-bcaa-da7242efc111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hrg7MSPA2UhAMzuAfhrApS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5650,
      "cache_read_input_tokens": 37107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5650
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_019CMs1LSoko7QtRPyUaM7Yp`</summary>

```json
{
  "project": "vla-ssd",
  "file": "writing_plan.yaml",
  "content": "venue: CoRL 2026\nabstract_ddl: 2026-05-26\npaper_ddl: 2026-05-29\nformat: \"8 pages + references\"\n\ntitle_candidates:\n  - \"Where Do Action Representations Come From? Dissecting Vision-Language-Action Models\"\n  - \"The Frozen Encoder Provides, the LLM Routes: Representational Analysis of Vision-Language-Action Models\"\n  - \"Vision Encodes, Language Routes: A Representational Decomposition of VLA Action Knowledge\"\n\n# ============================================================\n# SECTIONS\n# ============================================================\nsections:\n\n  - name: Abstract\n    core_evidence:\n      - d027_siglip_only_rsa          # RSA=0.615 smoking gun\n      - p0_functional_action_probe    # R² projector 0.706, readout 0.731\n      - p0_bootstrap_ci_training_effect  # training invariance CI includes 0\n      - untrained_last_preaction_probe   # readout trained-dependent Δ=0.045\n    key_numbers:\n      - \"SigLIP+projector RSA ρ=0.615 vs full VLA ρ≈0.50 vs DINO ρ=0.388\"\n      - \"Projector action R²=0.706; LLM image_mean R²=0.683 (degradation); readout R²=0.731 (concentration)\"\n      - \"Training effect on distributed RSA: Δ=0.021, CI=[−0.031, +0.064], n.s.\"\n      - \"Training effect on readout R²: Δ=0.045, CI=[0.032, 0.058], p<0.0001\"\n      - \"Untrained readout R²=0.686 < projector 0.706 — redistribution is learned\"\n\n  - name: Introduction\n    structure:\n      - para_1_problem: >\n          VLAs achieve impressive manipulation performance by fine-tuning LLMs on robot data.\n          Implicit assumption: fine-tuning injects action-relevant representational knowledge.\n          But where do action representations actually come from?\n      - para_2_gap: >\n          Grant et al. 2026 showed visual pathway dominates at behavioral level.\n          Hou 2026 / Fei 2025 showed VLAs largely ignore language instructions.\n          But no work has performed representational decomposition — measuring each component's\n          independent contribution to action-relevant structure.\n      - para_3_approach: >\n          We systematically decompose OpenVLA: extract representations from\n          (1) frozen SigLIP+projector, (2) LLM at every layer, (3) readout token.\n          Compare trained vs untrained LLM × with/without instruction, using RSA (geometric alignment)\n          and functional probes (action prediction R²).\n      - para_4_findings: >\n          Three findings: (1) Frozen vision encoder provides dominant action-relevant structure\n          (RSA=0.615 >> VLA 0.50 >> DINO 0.388). (2) LLM degrades distributed geometric alignment\n          but concentrates signal into readout token via training-dependent attention.\n          (3) Training teaches routing, not creating — distributed structure is training-invariant.\n      - para_5_implications: >\n          Implications for VLA design: vision encoder pretraining matters most;\n          LLM's role is information routing not knowledge injection;\n          VL pretraining provides geometric alignment beyond raw information content.\n    core_evidence:\n      - d027_siglip_only_rsa\n      - p0_functional_probe_v2   # DINO ≈ Proj in R²\n      - p0_bootstrap_ci_training_effect\n\n  - name: Related Work\n    categories:\n      - name: \"Vision-Language-Action Models\"\n        papers:\n          - \"Karamcheti et al. 2024 (Prismatic/OpenVLA) — architectural foundation\"\n          - \"Kim et al. 2024 (OpenVLA) — model we analyze\"\n          - \"Brohan et al. 2023 (RT-2) — VLA paradigm origin\"\n      - name: \"Behavioral Analysis of VLAs\"\n        papers:\n          - \"Grant et al. 2026 — visual pathway dominance (behavioral level)\"\n          - \"Hou 2026 (LangGap) — VLAs ignore language instructions\"\n          - \"Fei 2025 (LIBERO-Plus) — language-conditioned evaluation\"\n      - name: \"Mechanistic Interpretability of VLAs\"\n        papers:\n          - \"Haon et al. CoRL 2025 — activation steering on OpenVLA\"\n          - \"Swann et al. 2026 — SAE-based OpenVLA interpretability\"\n          - \"Rizzardo et al. 2026 — feature observability/controllability\"\n          - \"Molinari et al. 2025 — emergent world representations\"\n          - \"Lu et al. 2025 — linear probing OpenVLA hidden layers\"\n      - name: \"Vision Encoder Representations\"\n        papers:\n          - \"Fang 2025 — fine-tuning erodes VLM reasoning\"\n          - \"Oquab et al. 2024 (DINOv2) — self-supervised vision baseline\"\n          - \"Zhai et al. 2023 (SigLIP) — vision-language pretraining\"\n      - name: \"Representational Similarity Analysis\"\n        papers:\n          - \"Kriegeskorte et al. 2008 — RSA framework\"\n          - \"Kornblith et al. 2019 — CKA\"\n    positioning: >\n      Grant et al. 2026 is closest — we confirm their behavioral finding at representation level\n      with quantitative component decomposition. Lu et al. 2025 methodologically closest —\n      we differentiate via component-level (not just layer-level) analysis and causal controls\n      (trained/untrained × instruction ablation). Haon et al. same venue+model —\n      complementary (sparse semantic directions vs geometric analysis).\n\n  - name: Method\n    subsections:\n      - name: \"2.1 Model and Data\"\n        content_outline: >\n          OpenVLA architecture: SigLIP-SO400M → MLP projector → Llama-2 7B → action head.\n          LIBERO-10 fine-tuned checkpoint (10 tasks, 50 demos/task).\n          LIBERO-Goal as OOD evaluation benchmark (shared initial states, different goals).\n          Untrained control: from_config() reinitializes LLM (6.74B random), preserves SigLIP (0.80B).\n      - name: \"2.2 Representation Extraction\"\n        content_outline: >\n          Four representation sources: (a) SigLIP+projector output (before LLM),\n          (b) LLM per-layer image_mean (mean of image tokens at each layer),\n          (c) LLM per-layer last_preaction (readout token = last token before action prediction),\n          (d) DINOv2 cls_token (vision-only baseline).\n          2×2 conditions: trained/untrained × with-instruction/no-instruction.\n      - name: \"2.3 Representational Similarity Analysis (RSA)\"\n        content_outline: >\n          Construct RDMs for representations and 7-D action space.\n          Spearman correlation between upper-triangular RDM vectors.\n          Task-level analysis with per-task RSA + cross-task aggregation.\n          Bootstrap CI (10,000 resamples) for pairwise comparisons.\n      - name: \"2.4 Functional Action Probes\"\n        content_outline: >\n          MLP probe (dim→256→7) trained on representation→action mapping.\n          Mean R² across 7 action dimensions. Per-task train/val splits.\n          Bootstrap paired comparison for statistical significance.\n          Also: action-delta probes (predict Δaction = a_{t+1} - a_t).\n      - name: \"2.5 CKA Analysis\"\n        content_outline: >\n          Linear CKA and RDM-based CKA as complementary metric to RSA.\n          Motivation: RSA captures local geometric alignment, CKA captures global structure.\n          Note dimension mismatch caveat for linear CKA (4096-D repr vs 7-D action).\n\n  - name: Experiments\n    subsections:\n      - name: \"3.1 Experimental Setup\"\n        content_outline: >\n          LIBERO-Goal benchmark: 10 manipulation tasks, 50 demos each, 500 frames per task.\n          Representation extraction pipeline. Statistical testing protocol (bootstrap, permutation).\n          Hardware: 2× GPU on westd-19183.\n\n      - name: \"3.2 Vision Encoder Dominance (Claim 1)\"\n        core_evidence:\n          - d027_siglip_only_rsa          # SigLIP RSA=0.615 [CI: 0.526, 0.695]\n          - lg_rsa_analysis               # VLA conditions 0.48-0.49\n          - dinov2_baseline               # DINO RSA=0.388\n          - p0_functional_probe_v2        # DINO R²=0.712 ≈ Proj 0.706 (p=0.22)\n          - p0_functional_action_probe    # Proj R²=0.706\n          - p0_functional_action_delta_probe  # Delta: Proj 0.118 ≈ LLM 0.122\n        key_numbers:\n          - \"SigLIP+Proj RSA=0.615 [CI: 0.526, 0.695]\"\n          - \"Full VLA RSA ≈ 0.50 (image_mean, all 4 conditions)\"\n          - \"DINO RSA=0.388\"\n          - \"LLM degradation: RSA gap = 0.615 − 0.501 = 0.114\"\n          - \"DINO action R²=0.712 ≈ Projector R²=0.706 (Δ=0.005, p=0.22, n.s.)\"\n          - \"Geometric-functional dissociation: DINO=Proj in R², DINO<&lt;Proj in RSA\"\n        structure: >\n          (a) RSA comparison: projector >> VLA >> DINO.\n          (b) Functional probe: projector R²=0.706, confirming informational richness.\n          (c) DINO control: R²≈Proj but RSA<&lt;Proj → VL pretraining provides geometric alignment,\n              not extra information content. Key dissociation finding.\n          (d) Action-delta: all ~0.12, > DINO 0.06-0.10. SigLIP is source.\n\n      - name: \"3.3 LLM Redistributes Action Structure (Claim 2)\"\n        core_evidence:\n          - plan_003_perlayer_degradation  # Per-layer RSA curve\n          - p0_functional_action_probe     # image_mean R²=0.683 < Proj 0.706; readout 0.731\n          - p0_image_mean_rsa_verify       # image_mean RSA=0.501\n          - untrained_last_preaction_probe  # untrained readout R²=0.686 < Proj 0.706\n          - plan_009_cka_verification      # CKA: monotonic increase, ordering reversal\n        key_numbers:\n          - \"RSA degradation: 0.615 → 0.501 (image_mean)\"\n          - \"R² degradation: 0.706 → 0.683 (CI=[0.011, 0.037], p=0.001)\"\n          - \"Readout concentration: R²=0.731 (CI vs proj: p=0.001)\"\n          - \"Untrained readout: R²=0.686 < projector 0.706\"\n          - \"Trained vs untrained readout: Δ=0.045, CI=[0.032, 0.058], p<0.0001\"\n          - \"Per-layer: Proj→L1 biggest drop (0.13-0.25), non-monotonic middle layers\"\n          - \"CKA: monotonic increase L0→L32, last_preaction CKA=0.127 (highest)\"\n        structure: >\n          (a) Distributed degradation: image_mean RSA and R² both decrease through LLM.\n          (b) Per-layer curve: non-monotonic, embedding interface is bottleneck.\n          (c) Readout concentration: last_preaction R²=0.731 > projector.\n          (d) Training-dependence: untrained readout 0.686 < projector 0.706.\n              Trained readout 0.731 >> untrained 0.686 (Δ=0.045, p<0.0001).\n          (e) CKA complement: global structure preserved (monotonic CKA),\n              RSA-CKA dissociation as finding (Sec 3.5 or Discussion).\n\n      - name: \"3.4 Training = Routing, Not Creating (Claim 3)\"\n        core_evidence:\n          - p0_bootstrap_ci_training_effect  # image_mean CI includes 0\n          - d021_instruction_ablation        # inst effect Δ=0.004\n          - d027_trained_no_inst_rsa         # full 2×2 matrix\n          - untrained_last_preaction_probe   # readout Δ=0.045 significant\n          - d021_output_head_analysis        # vision backbone identical\n          - plan_008_random_inst_control     # RUNNING — random instruction control\n        key_numbers:\n          - \"Training effect on image_mean RSA: Δ=0.021, CI=[−0.031, +0.064], p=0.20 (n.s.)\"\n          - \"Training effect on last_preaction RSA: Δ=0.008, CI=[−0.040, +0.056], p=0.37 (n.s.)\"\n          - \"Instruction effect: Δ=0.004, far below threshold\"\n          - \"Training effect on readout R²: Δ=0.045, CI=[0.032, 0.058], p<0.0001 (significant)\"\n          - \"2×2 matrix: all 4 conditions within 0.48-0.50 band\"\n          - \"Vision backbone + projector: identical weights (cos_sim=1.0) between trained/untrained\"\n        structure: >\n          (a) 2×2 RSA matrix: trained ≈ untrained, with-inst ≈ no-inst (all n.s.).\n          (b) Bootstrap CI: distributed structure is training- and instruction-invariant.\n          (c) Readout concentration IS training-dependent (Δ=0.045, p<0.0001).\n          (d) Interpretation: training teaches LLM to route existing information to readout,\n              does not create new action-relevant structure.\n          (e) Random instruction control (plan_008, if available): further confirms instruction invariance.\n\n      - name: \"3.5 Metric Sensitivity: RSA vs CKA (Supplementary or Main)\"\n        core_evidence:\n          - plan_009_cka_verification\n        key_numbers:\n          - \"Linear CKA: untrained(0.089) > trained(0.083) > proj(0.081) > DINO(0.066)\"\n          - \"RDM CKA: last_preaction(0.290) > proj(0.257) ≈ trained(0.260) > DINO(0.241)\"\n          - \"CKA per-layer: monotonic increase (vs RSA non-monotonic)\"\n        structure: >\n          RSA vs CKA ordering reversal for projector vs trained.\n          RSA = local geometric alignment; CKA = global structure preservation.\n          Claim 2 explicitly scoped to \"geometric (RSA) degradation.\"\n          CKA last_preaction highest — consistent with redistribution.\n          Could be main text subsection or supplementary depending on space.\n\n  - name: Discussion\n    structure:\n      - para_1_synthesis: >\n          Three findings form coherent picture: vision encoder is the source,\n          LLM is the router, training teaches the routing policy.\n          Projector provides 96.6% of LLM's functional capacity (0.706/0.731).\n      - para_2_geometric_functional_dissociation: >\n          DINO ≈ Projector in R² but << in RSA. Action information (decodability) is\n          separate from geometric alignment (structural match to action space).\n          VL pretraining (SigLIP) provides alignment, not extra information.\n          Implications for encoder selection in VLA design.\n      - para_3_rsa_cka_dissociation: >\n          RSA and CKA capture different aspects — degradation in local geometry\n          coexists with preservation/improvement in global structure.\n          LLM transforms, not destroys. Metric choice determines narrative.\n      - para_4_implications: >\n          (1) Vision encoder pretraining quality is primary lever for action representations.\n          (2) For tasks depending on distributed representations, use projector output directly.\n          (3) LLM's value is readout concentration — relevant for action head design.\n          (4) Language instructions do not modulate representation structure — rethink instruction role.\n      - para_5_connection_to_behavioral: >\n          Our representational findings explain Grant et al. 2026's behavioral results:\n          vision dominates because the frozen encoder provides the action-relevant structure.\n          \"Encoded but not used\" (their instruction finding) aligns with our instruction invariance.\n      - para_6_limitations: >\n          Single architecture (OpenVLA). Single benchmark suite (LIBERO).\n          RSA captures structural alignment, not causal contribution.\n          plan_012 CLIP-ViT control would strengthen encoder comparison.\n    core_evidence:\n      - p0_functional_probe_v2   # DINO ≈ Proj dissociation\n      - plan_009_cka_verification  # RSA-CKA dissociation\n      - d021_instruction_ablation  # instruction invariance\n\n  - name: Conclusion\n    structure:\n      - para_1_summary: >\n          First representational decomposition of a VLA. Three findings:\n          (1) frozen vision encoder dominates action-relevant structure,\n          (2) LLM redistributes via training-dependent readout concentration,\n          (3) training teaches routing, not creating.\n      - para_2_takeaway: >\n          Action representations in VLAs are inherited, not learned.\n          Design implications: invest in vision encoder pretraining,\n          not in larger LLMs or more fine-tuning data for action knowledge.\n\n# ============================================================\n# FIGURES\n# ============================================================\nfigures:\n  - id: fig1\n    type: \"概念图/架构图\"\n    description: >\n      VLA pipeline decomposition diagram. Shows SigLIP → Projector → LLM (32 layers) → Action Head.\n      Annotate extraction points: (a) projector output, (b) per-layer image_mean, (c) per-layer\n      last_preaction (readout token). Show 2×2 conditions (trained/untrained × with/no instruction).\n      Inset: RSA and functional probe methodology schematic.\n    data_source: \"architectural (no experiment data)\"\n    placement: \"Section 2 or Section 1\"\n\n  - id: fig2\n    type: \"实验结果图 — Bar chart\"\n    description: >\n      Main RSA comparison. Bars: SigLIP+Projector (0.615), VLA trained w-inst (0.501),\n      VLA untrained w-inst (0.485), VLA trained no-inst (0.501), VLA untrained no-inst (0.482),\n      DINO (0.388). Error bars from bootstrap CI. Clear visual gap between projector and all VLA conditions.\n    data_source:\n      - d027_siglip_only_rsa\n      - p0_image_mean_rsa_verify\n      - d027_trained_no_inst_rsa\n      - d021_instruction_ablation\n    placement: \"Section 3.2\"\n\n  - id: fig3\n    type: \"实验结果图 — Line plot\"\n    description: >\n      Per-layer RSA degradation curves. X-axis: Projector → L0 → L1 → ... → L32.\n      Y-axis: RSA with action space. Four lines: trained w-inst, trained no-inst,\n      untrained w-inst, untrained no-inst. Horizontal reference line at projector (0.615)\n      and DINO (0.388). Shows non-monotonic pattern, Proj→L1 major drop,\n      partial mid-layer recovery.\n    data_source:\n      - plan_003_perlayer_degradation\n    placement: \"Section 3.3\"\n\n  - id: fig4\n    type: \"实验结果图 — Grouped bar chart\"\n    description: >\n      Functional probe R² comparison. Groups: Projector, LLM image_mean (trained),\n      LLM readout (trained), LLM readout (untrained), DINO.\n      Shows: (a) image_mean < projector (degradation), (b) trained readout > projector (concentration),\n      (c) untrained readout < projector (redistribution requires training),\n      (d) DINO ≈ projector (geometric-functional dissociation).\n      Error bars from bootstrap. Significance brackets for key comparisons.\n    data_source:\n      - p0_functional_action_probe\n      - p0_functional_probe_v2\n      - untrained_last_preaction_probe\n    placement: \"Section 3.3\"\n\n  - id: fig5\n    type: \"实验结果图 — 2×2 heatmap or matrix plot\"\n    description: >\n      Training × Instruction effect matrix. 2×2 grid showing RSA values for\n      trained/untrained × with/no-inst. All values in narrow 0.48-0.50 band.\n      Bootstrap CI annotations. Visual message: training and instruction have negligible effect\n      on distributed structure.\n    data_source:\n      - d027_trained_no_inst_rsa\n      - p0_bootstrap_ci_training_effect\n    placement: \"Section 3.4\"\n\n  - id: fig6\n    type: \"实验结果图 — Dual-axis or panel plot (supplementary candidate)\"\n    description: >\n      RSA vs CKA per-layer comparison. Two panels or dual Y-axis.\n      RSA: non-monotonic, degradation from projector. CKA: monotonic increase.\n      Shows metric-dependent interpretation. CKA last_preaction as outlier (highest).\n    data_source:\n      - plan_009_cka_verification\n      - plan_003_perlayer_degradation\n    placement: \"Section 3.5 or Supplementary\"\n\n# ============================================================\n# TABLES\n# ============================================================\ntables:\n  - id: tab1\n    description: \"Main RSA results — component comparison with bootstrap CI\"\n    columns: [\"Model/Condition\", \"Aggregation\", \"Peak Layer\", \"RSA ρ\", \"95% CI\"]\n    rows_outline:\n      - \"SigLIP+Projector | — | — | 0.615 | [0.526, 0.695]\"\n      - \"VLA Trained w-inst | image_mean | L23 | 0.501 | TBD\"\n      - \"VLA Trained no-inst | image_mean | L23 | 0.501 | TBD\"\n      - \"VLA Untrained w-inst | image_mean | L23 | 0.485 | TBD\"\n      - \"VLA Untrained no-inst | image_mean | L23 | 0.482 | TBD\"\n      - \"DINOv2 | cls_token | — | 0.388 | TBD\"\n    data_source:\n      - d027_siglip_only_rsa\n      - p0_image_mean_rsa_verify\n      - d027_trained_no_inst_rsa\n      - d021_instruction_ablation\n    placement: \"Section 3.2\"\n\n  - id: tab2\n    description: \"Functional action probe R² — component decomposition\"\n    columns: [\"Representation\", \"Raw Action R²\", \"Action-Delta R²\", \"Notes\"]\n    rows_outline:\n      - \"SigLIP+Projector | 0.706 | 0.118 | Vision encoder output\"\n      - \"VLA Trained image_mean L19 | 0.683 | 0.122 | Degraded vs Proj (p=0.001)\"\n      - \"VLA Trained readout L19 | 0.731 | TBD | Concentrated (p=0.001 vs Proj)\"\n      - \"VLA Untrained image_mean L0 | 0.714 | 0.117 | Architecture-intrinsic\"\n      - \"VLA Untrained readout L32 | 0.686 | TBD | < Proj → redistribution requires training\"\n      - \"DINOv2 cls_token | 0.712 | 0.100 | ≈ Proj in R² (p=0.22), << in RSA\"\n    data_source:\n      - p0_functional_action_probe\n      - p0_functional_action_delta_probe\n      - p0_functional_probe_v2\n      - untrained_last_preaction_probe\n    placement: \"Section 3.3\"\n\n  - id: tab3\n    description: \"Bootstrap CI for training and instruction effects\"\n    columns: [\"Comparison\", \"Aggregation\", \"Δ\", \"95% CI\", \"p-value\", \"Significant?\"]\n    rows_outline:\n      - \"Training (image_mean RSA) | image_mean | +0.021 | [−0.031, +0.064] | 0.20 | No\"\n      - \"Training (last_preaction RSA) | last_preaction | +0.008 | [−0.040, +0.056] | 0.37 | No\"\n      - \"Training (readout R²) | last_preaction | +0.045 | [+0.032, +0.058] | <0.0001 | Yes\"\n      - \"Instruction (RSA) | — | +0.004 | — | — | No\"\n      - \"Proj vs LLM image_mean (R²) | image_mean | +0.023 | [+0.011, +0.037] | 0.001 | Yes\"\n      - \"Trained readout vs Proj (R²) | last_preaction | +0.025 | — | 0.001 | Yes\"\n    data_source:\n      - p0_bootstrap_ci_training_effect\n      - untrained_last_preaction_probe\n      - p0_functional_probe_v2\n    placement: \"Section 3.4\"\n\n# ============================================================\n# WRITING ORDER\n# ============================================================\nwriting_order:\n  - section: \"Experiments (Sec 3)\"\n    reason: \"Evidence-first: establish all claims with data before writing narrative\"\n  - section: \"Method (Sec 2)\"\n    reason: \"Formalize methodology after experiments are written — ensures method matches what was actually done\"\n  - section: \"Discussion\"\n    reason: \"Synthesize implications after results are on paper\"\n  - section: \"Introduction\"\n    reason: \"Now the story arc is clear — write intro that sets up the exact findings\"\n  - section: \"Related Work\"\n    reason: \"Position against literature with full knowledge of our contributions\"\n  - section: \"Conclusion\"\n    reason: \"Compress the story\"\n  - section: \"Abstract\"\n    reason: \"Last — summarizes the complete paper\"\n\n# ============================================================\n# LITERATURE STRATEGY\n# ============================================================\nliterature_strategy:\n  must_cite:\n    - \"Kim et al. 2024 — OpenVLA (model we analyze)\"\n    - \"Karamcheti et al. 2024 — Prismatic (OpenVLA's architectural foundation)\"\n    - \"Grant et al. 2026 — behavioral visual dominance in VLAs\"\n    - \"Brohan et al. 2023 — RT-2 (VLA paradigm)\"\n    - \"Hou 2026 (LangGap) — VLAs ignore language\"\n    - \"Fei 2025 (LIBERO-Plus) — language-conditioned evaluation\"\n    - \"Haon et al. CoRL 2025 — activation steering OpenVLA\"\n    - \"Liu et al. 2024 (LIBERO) — benchmark\"\n    - \"Kriegeskorte et al. 2008 — RSA methodology\"\n    - \"Zhai et al. 2023 — SigLIP\"\n    - \"Oquab et al. 2024 — DINOv2\"\n  compare_with:\n    - \"Grant et al. 2026 — behavioral vs representational evidence (complementary)\"\n    - \"Lu et al. 2025 — linear probing OpenVLA (differentiate: component decomposition vs layer probing)\"\n    - \"Haon et al. CoRL 2025 — activation steering (complementary: sparse directions vs geometric analysis)\"\n    - \"Swann et al. 2026 — SAE interpretability (complementary: feature-level vs geometric-level)\"\n    - \"Fang 2025 — fine-tuning erodes reasoning (related but different scope: VLM vs VLA)\"\n    - \"Molinari et al. 2025 — emergent world representations (complementary: world models vs action structure)\"\n    - \"Rizzardo et al. 2026 — feature observability (complementary: controllability vs decomposition)\"\n\n# ============================================================\n# PENDING / CONTINGENT\n# ============================================================\npending:\n  - exp_id: plan_008_random_inst_control\n    status: RUNNING\n    impact: \"Strengthens Claim 3 instruction invariance. If significant → revise Claim 3 language.\"\n    fallback: \"Claim 3 already supported by 2×2 matrix; random-inst is supplementary confirmation.\"\n  - exp_id: plan_012_clip_vit_control\n    status: PLANNED\n    impact: \"Distinguishes 'VL pretraining' from 'SigLIP specifically' for Claim 1.\"\n    fallback: \"Discussion acknowledges confound; DINO ≈ Proj dissociation partially addresses.\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "13c6b4be-6162-4216-a22f-4c2e62d77061",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hrg7MSPA2UhAMzuAfhrApS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5650,
      "cache_read_input_tokens": 37107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5650
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

_source line 31 · 2026-05-16T00:33:28.542Z_

<details><summary>↩ Tool result · `toolu_019CMs1LSoko7QtRPyUaM7Yp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "4b2045b7-2d42-42cd-a136-a75214e753ef",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/writing_plan.yaml\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

writing_plan.yaml 已保存。结构概览：

**7 sections**，每个 section 带 core_evidence（引用 exp_id）和 key_numbers（可追溯到 registry metrics）。

**6 figures**：
- fig1: 架构分解概念图
- fig2: RSA 主对比 bar chart（Proj 0.615 >> VLA ~0.50 >> DINO 0.388）
- fig3: Per-layer RSA 降解曲线（4 条件）
- fig4: Functional probe R² grouped bar（degradation + concentration + training-dependence）
- fig5: 2×2 training×instruction matrix（invariance 可视化）
- fig6: RSA vs CKA 对比（supplementary 候选）

**3 tables**：tab1 RSA 主表，tab2 functional probe R² 分解，tab3 bootstrap CI 汇总。

**Writing order**: Experiments → Method → Discussion → Introduction → Related Work → Conclusion → Abstract（evidence-first）。

**Pending**: plan_008（RUNNING，instruction invariance 补充）和 plan_012（PLANNED，CLIP-ViT control），均有 fallback 方案不阻塞写作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "uuid": "5398eb22-c262-4a26-be45-9816a58c111d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtaXGNSrfDaeMgGPFVsr77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9377,
      "cache_read_input_tokens": 42757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9377
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

_source line 33_

writing_plan.yaml 已保存。结构概览：

**7 sections**，每个 section 带 core_evidence（引用 exp_id）和 key_numbers（可追溯到 registry metrics）。

**6 figures**：
- fig1: 架构分解概念图
- fig2: RSA 主对比 bar chart（Proj 0.615 >> VLA ~0.50 >> DINO 0.388）
- fig3: Per-layer RSA 降解曲线（4 条件）
- fig4: Functional probe R² grouped bar（degradation + concentration + training-dependence）
- fig5: 2×2 training×instruction matrix（invariance 可视化）
- fig6: RSA vs CKA 对比（supplementary 候选）

**3 tables**：tab1 RSA 主表，tab2 functional probe R² 分解，tab3 bootstrap CI 汇总。

**Writing order**: Experiments → Method → Discussion → Introduction → Related Work → Conclusion → Abstract（evidence-first）。

**Pending**: plan_008（RUNNING，instruction invariance 补充）和 plan_012（PLANNED，CLIP-ViT control），均有 fallback 方案不阻塞写作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 217624,
  "duration_api_ms": 216842,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "a07025ac-e9d0-41a2-b15c-642972f33050",
  "total_cost_usd": 0.68755975,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 40293,
    "cache_read_input_tokens": 284439,
    "output_tokens": 11663,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40293,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 322,
        "cache_read_input_tokens": 42757,
        "cache_creation_input_tokens": 9377,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9377
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1779,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001874,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 11663,
      "cacheReadInputTokens": 284439,
      "cacheCreationInputTokens": 40293,
      "webSearchRequests": 0,
      "costUSD": 0.6856857500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "95d1e83e-1c36-4113-a57f-ea5f9cebf691"
}
```

</details>

---
