# research writing plan

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_research_writing_plan_20260516T002929.log`
- **Structured JSON:** [`ef0d1e560c587d697eab.json`](../../sessions/ef/ef0d1e560c587d697eab.json)

## Before a recorded user message

27 recorded events

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
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
  "uuid": "1c4d0f15-0829-431b-a5c9-d8c65d50a981",
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
  "uuid": "c303ad22-09fb-4b21-a44b-79500d0741f5",
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e"
}
```

---

### Assistant

_source line 4_

我先读取 paper_framing.md 获取完整 framing 信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "e6bfd0ef-ef61-4ff0-bf53-502f4097139a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BF76B6EnxNZtTq5JvbTYuJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11868,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11868
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PbrEGGD3vyX3J1ecxLY9XU`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "31dd5b33-1a52-4529-9943-df2d069ca119",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BF76B6EnxNZtTq5JvbTYuJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11868,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11868
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

_source line 6 · 2026-05-16T00:29:38.563Z_

<details><summary>↩ Tool result · `toolu_01PbrEGGD3vyX3J1ecxLY9XU`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "4fae1789-7a2f-4c9b-af55-90df5be1270d",
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

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the paper_framing.md file to get the complete framing information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "a211d5b6-b5c3-48d9-ab78-8c50080b55ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyPvrD17qZDPFYaz5Cv11b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 724
      },
      "output_tokens": 59,
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KpF7aikHaQdMGhbT3TDiPL`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "22ee836e-3eae-454e-b4e7-436876275edf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyPvrD17qZDPFYaz5Cv11b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 724
      },
      "output_tokens": 59,
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

_source line 9 · 2026-05-16T00:29:41.673Z_

<details><summary>↩ Tool result · `toolu_01KpF7aikHaQdMGhbT3TDiPL`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "389c85af-d3ac-4328-9321-963bf4d8172b",
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

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full paper_framing.md. Let me also read the memory.md and ROADMAP.md for additional context about experiments and their IDs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "cc7224a9-da82-491a-af38-74d3eb14c9c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQ5oiDpSnob4ANCDNzvQ9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5448,
      "cache_read_input_tokens": 24433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5448
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

_source line 11_

Now let me also check the experiment data sources to map exp_ids correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "ac148888-7774-42ba-99e8-3be99c738712",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQ5oiDpSnob4ANCDNzvQ9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5448,
      "cache_read_input_tokens": 24433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5448
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Cfz6k3PW8zBkTMXsFmMDri`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "fba80e46-7dc9-4b94-a8ac-757fbcbf58ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQ5oiDpSnob4ANCDNzvQ9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5448,
      "cache_read_input_tokens": 24433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5448
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

_source line 13 · 2026-05-16T00:29:47.176Z_

<details><summary>↩ Tool result · `toolu_01Cfz6k3PW8zBkTMXsFmMDri`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "9ffc70b3-2e9a-404b-bc63-0e8838d236e0",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012wu7wPKFYgkMBuUhsCTcBm`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "4d9c196d-3954-49e1-abc8-ec8d11b76960",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQ5oiDpSnob4ANCDNzvQ9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5448,
      "cache_read_input_tokens": 24433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5448
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

_source line 15 · 2026-05-16T00:29:47.734Z_

<details><summary>↩ Tool result · `toolu_012wu7wPKFYgkMBuUhsCTcBm`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "b83941f9-da8d-4b75-ab1e-975f65faba2c",
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

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need to draft a comprehensive writing_plan.yaml. Let me also check if there's a decisions.yaml to get experiment IDs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "c10a2e0c-bf43-4230-b5fa-d6227019c10f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZDF64GqXqJbKDzHUrqSFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 29881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4854
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

Now let me check the artifacts directory and decisions for experiment IDs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "9ddd9c1c-b210-4f0a-9d4e-3ac9335f3cc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZDF64GqXqJbKDzHUrqSFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 29881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4854
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

<details open><summary>🔧 Tool call — Bash · `toolu_013WMn9koQT6a6x4GrrATFwi`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ 2>/dev/null | head -30",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "b9573caf-4455-4b79-a5e6-85fb6bf8f2be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZDF64GqXqJbKDzHUrqSFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 29881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4854
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

_source line 19 · 2026-05-16T00:29:52.209Z_

<details><summary>↩ Tool result · `toolu_013WMn9koQT6a6x4GrrATFwi`</summary>

```text
_project
action_probe_design.md
controlb_analysis
dinov2_baseline
dream_reports
layer_stability_analysis.md
libero_goal_feasibility.md
literature_map.yaml
literature_map_probing.md
literature_survey_instruction_probing.md
manifest.yaml
mvp_controlb_trained
mvp_probe_trained
openvla_libero_goal_compat.md
patch_probes.py
pca_linear_probe_gc.py
pca_linear_probe_perlayer.py
pipeline_audit_libero_goal.md
probe_design_plan.md
redream_evidence_v2.md
rsa_analysis.py
untrained_last_preaction_probe.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "715a94be-a84b-4e02-8dab-474b7fb2b3ef",
  "tool_use_result": {
    "stdout": "_project\naction_probe_design.md\ncontrolb_analysis\ndinov2_baseline\ndream_reports\nlayer_stability_analysis.md\nlibero_goal_feasibility.md\nliterature_map.yaml\nliterature_map_probing.md\nliterature_survey_instruction_probing.md\nmanifest.yaml\nmvp_controlb_trained\nmvp_probe_trained\nopenvla_libero_goal_compat.md\npatch_probes.py\npca_linear_probe_gc.py\npca_linear_probe_perlayer.py\npipeline_audit_libero_goal.md\nprobe_design_plan.md\nredream_evidence_v2.md\nrsa_analysis.py\nuntrained_last_preaction_probe.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CGNJbZH8tu3ajsu9yb68vX`</summary>

```json
{
  "project": "vla-ssd",
  "file": "decisions.yaml",
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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "5dc4411a-f535-4016-acd0-73a3086d3173",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZDF64GqXqJbKDzHUrqSFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 29881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4854
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

_source line 21 · 2026-05-16T00:29:52.765Z_

<details><summary>↩ Tool result · `toolu_01CGNJbZH8tu3ajsu9yb68vX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/decisions.yaml\", \"content\": \"_next_id: 35\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 11:03 UTC\\n  summary: MVP 三分支判定标准校准：ρ下限0.3→0.5, Δρ加bootstrap CI, subtask gate加DINO baseline对比\\n  rationale: Reviewer 审查发现四项校准缺陷：(1) ρ>0.3 下限过低（DINO-V2 已达0.833，0.3只挡彻底失败）→ 提至0.5；(2)\\n    Δρ>0.1 仅为点估计缺统计检验 → 追加 bootstrapped 95% CI must exclude 0；(3) subtask_AUC>0.7\\n    无 baseline 锚点（不知道 DINO-V2 能做到多少）→ 增加条件 subtask_AUC > DINO_subtask_AUC + 0.05；(4)\\n    layer profile 不入正式判定但作为 mandatory supplementary analysis。修改后标准更严谨，降低 false positive\\n    PASS 风险。\\n  related_experiments:\\n  - exp_id: dino-v2-baseline\\n    role: baseline\\n    result: ρ=0.833\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP 判定全面切换到 per-task mean ρ，弃用 pooled ρ\\n  rationale: Reviewer 指出 pooled ρ 受 cross-task variance 膨胀（DINO pooled=0.833 vs per-task\\n    mean=0.554）。pooled-vs-pooled 虽对称但偏严（可能 false negative）。切换 per-task mean 与 task-level\\n    bootstrap CI 方法论一致，且是更公平的 apples-to-apples 比较。影响：VLA≥DINO gate 从 ρ≥0.833 变为 per-task\\n    mean≥0.554；ρ>0.5 下限同样改为 per-task mean。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: pooled ρ=0.833, per-task mean=0.554\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 12:31 UTC\\n  summary: 移除 subtask AUC gate，MVP 判定简化为纯 temporal distance (ρ) 路径\\n  rationale: DINO-V2 subtask AUC = 0.9717，Path B 要求 VLA > DINO + 0.05 = 1.0217，数学不可达（AUC\\n    上限 1.0）。根因：subtask 间视觉差异大，任何强视觉编码器都能高 AUC 区分——subtask discrimination 不是 VLA 的差异化能力。Temporal\\n    distance（连续进度信号）才是 VLA 可能独有的编码维度。简化后判定：PASS 需 VLA_ρ ≥ DINO_ρ (0.833)；CONDITIONAL\\n    需 Δρ > 0.1 但 VLA_ρ < DINO_ρ；FAIL 需 ρ ≤ 0.5 或 Δρ ≤ 0.1。Subtask AUC 保留为补充分析，不参与\\n    gate。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: trigger\\n    result: subtask AUC 0.9717 使 Path B 数学不可达\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 12:35 UTC\\n  summary: D003 勘误：DINO gate 阈值从 0.833 (pooled) 修正为 0.554 (per-task mean)，与 D002 对齐\\n  rationale: D003 写 ROADMAP 时误用 pooled ρ 0.833 作为 DINO gate 阈值，但 D002 已明确\\\"全面切换到 per-task\\n    mean ρ，弃用 pooled\\\"。DINO per-task mean ρ = 0.554。0.833 vs 0.554 差 0.28，直接影响 PASS/FAIL\\n    判定——用 0.833 会错误地将本应 PASS 的结果判为 CONDITIONAL。修正后所有文档/代码统一使用 per-task mean。同时确认 analyze_mvp.py\\n    废弃决策不变（urgent 指令已发）。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: reference\\n    result: pooled ρ=0.833, per-task mean ρ=0.554\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-15 13:31 UTC\\n  summary: D004 DINO gate 阈值作废：0.554→0.901。旧值基于 500 pairs/task 的噪声结果，新管道 5000 pairs/task\\n    下 DINO per-task mean ρ=0.9008\\n  rationale: 'Reviewer CRITICAL: 新管道 rerun DINO-V2 基线，per-task mean ρ 从 0.554 暴涨至\\n    0.901（10x 采样密度消除噪声）。旧管道 pooled/per-task 差异(0.833/0.554)是采样伪影。Gate 3 阈值必须更新为 0.901，否则\\n    analyze_results.py 判定标准错误。dinov2_baseline registry metrics 标为 invalidated。'\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: 旧 metrics invalidated; rerun per-task mean ρ=0.9008\\n  - exp_id: mvp_probe_trained\\n    role: primary\\n    result: layers 1-5 ρ≈0.950\\n  - exp_id: mvp_probe_untrained\\n    role: control\\n    result: layers 1-5 ρ≈0.925, Δρ max 0.043\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 13:32 UTC\\n  summary: 'DINO baseline invalidated: 旧管道 ρ=0.554 作废，新管道 ρ=0.901。Gate 3 阈值更新为 0.901。Gate\\n    2 预判高风险（layers 1-5 max Δρ=0.043 << 0.1）'\\n  rationale: Worker 用更新后的 train_probes.py 重跑 DINO baseline，per_task_n_pairs 从 500→5000，per-task\\n    mean ρ 从 0.554 暴涨至 0.901。旧结果系统性低估——所有 10 task 均在 0.84-0.93（旧值 0.41-0.68）。D001-D004\\n    的判定标准建立在错误基线上。同时 trained(ρ≈0.95) vs untrained(ρ≈0.93) vs DINO(ρ≈0.90) 三者差距极小，temporal\\n    distance 信号主要来自 vision encoder 而非 LLM 训练。等待 33 层全结果确认。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: invalidated baseline\\n    result: 旧 ρ=0.554 作废，新 ρ=0.901\\n  - exp_id: mvp_probe_trained\\n    role: running probe\\n    result: layers 1-5 mean ρ≈0.95\\n  - exp_id: mvp_probe_untrained\\n    role: running control\\n    result: layers 1-5 mean ρ≈0.93, Δρ<0.05\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-15 13:49 UTC\\n  summary: MVP Gate 2 FAIL 确认：33 层全结果，非坍塌层最大 Δρ=0.043 << 0.1。Temporal distance 信号来自\\n    vision encoder 而非 VLA 训练。Pivot 到 subtask predicate probe + 实用 pipeline 双线验证\\n  rationale: '完整 33 层数据：trained best ρ=0.956(L3), untrained best ρ=0.933(L1), DINO\\n    ρ=0.901。非坍塌层 Δρ 范围 0.003-0.043，无任何层接近 0.1 阈值。Gate 1 PASS(ρ>>0.5), Gate 2 FAIL(Δρ<<0.1),\\n    Gate 3 PASS(0.956>0.901)。科学结论：temporal distance 信号主要来自 SigLIP vision encoder，LLM\\n    fine-tuning 贡献 ~2-4% ρ，统计显著但实质极小。\\n\\n\\n    Pivot 理由：temporal distance 与 visual change 高度相关，vision encoder 天然擅长，不是测试 VLA 训练贡献的好\\n    probe。IDEA_BRIEF 原计划包含 subtask predicate classification（is_grasped, is_on_table\\n    等离散语义属性），这类信号需要理解 action 语义而非视觉相似度，vision encoder 不应有优势。先快速验证 subtask probe 是否展示\\n    VLA-specific 贡献，同时推进实用 pipeline（VLA ρ=0.95 已足够强，不管信号来源，self-scoring 可行）。'\\n  related_experiments:\\n  - exp_id: mvp_probe_trained\\n    role: primary probe\\n    result: best L3 ρ=0.956, 33 layers complete\\n  - exp_id: mvp_probe_untrained\\n    role: control C\\n    result: best L1 ρ=0.933, Δρ max=0.043\\n  - exp_id: dinov2_baseline\\n    role: baseline (rerun)\\n    result: ρ=0.901\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 13:58 UTC\\n  summary: MVP Gate 2 确认 FAIL（clean verdict）。Subtask predicate probe 是最后一道 VLA-specific\\n    signal 测试，48h 内出 CoRL go/no-go。\\n  rationale: P0 修复后 33 层全量结果：非坍塌层 max Δρ=0.043 << 0.1，CI [0.036, 0.050] 排除零但效应量不足。根因：temporal\\n    distance ≈ visual change，SigLIP 天然擅长（untrained ρ=0.933）。Subtask predicate probe（BDDL\\n    predicates）测试 VLA 是否编码离散 action-semantic 属性，但 DINO auto-extracted subtask AUC=0.97\\n    构成高 baseline 风险。设 48h 决策窗口：subtask probe 结果 + Control B 完成后做 CoRL go/no-go。\\n  related_experiments:\\n  - exp_id: mvp_probe_trained\\n    role: primary\\n    result: 'negative: Δρ=0.043'\\n  - exp_id: mvp_probe_untrained\\n    role: control\\n    result: 'success: ρ=0.933 baseline'\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: 'success: ρ=0.901'\\n  - exp_id: mvp_controlb_trained\\n    role: control\\n    result: running\\n  - exp_id: mvp_controlb_untrained\\n    role: control\\n    result: running\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-15 14:04 UTC\\n  summary: Subtask predicate pivot 终止。DINO auto-extracted subtask AUC=0.9717 > 0.95\\n    gate，所有 BDDL predicates 视觉可辨，VLA 训练无独特优势。转向 action prediction probe 调研。\\n  rationale: LIBERO tabletop 场景中 is_grasped/is_on_table/is_in_drawer 等 predicates\\n    在第三人称+手腕相机下视觉可辨，纯视觉模型即可高精度分类。根本问题：需要\\\"视觉不可达\\\"的 probing task 才能体现 VLA LLM 训练的独特贡献。Action\\n    prediction（预测 next action）需要策略知识，vision encoder 天然不擅长，是最有潜力的候选方向。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: evidence\\n    result: DINO subtask AUC=0.9717\\n  - exp_id: mvp_probe_trained\\n    role: context\\n    result: Δρ=0.043 insufficient\\n  - exp_id: mvp_probe_untrained\\n    role: context\\n    result: untrained ρ=0.933 vision-dominated\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 14:09 UTC\\n  summary: 批准 Action Prediction Probe 作为 MVP-2 方向。设定三门判定：G1 R²>0.3, G2 ΔR²(trained-untrained)>0.15,\\n    G3 ΔR²(trained-DINO)>0.15\\n  rationale: Temporal distance (D007) 和 subtask predicate (D009) 均因\\\"视觉可辨\\\"失败。Action\\n    prediction 需策略知识，vision encoder 不擅长，是区分 VLA 训练贡献的合理 probing task。数据现成（LIBERO HDF5\\n    自带 7-DoF action），特征可复用，运行快（~20min），低风险高信息量。\\n  related_experiments:\\n  - exp_id: mvp_probe_trained\\n    role: predecessor\\n    result: Δρ=0.043, temporal distance 视觉可辨\\n  - exp_id: mvp_probe_untrained\\n    role: predecessor\\n    result: baseline for G2 comparison\\n  - exp_id: dinov2_baseline\\n    role: predecessor\\n    result: ρ=0.901, 证明 temporal distance 视觉可辨\\n  - exp_id: mvp_controlb_trained\\n    role: running\\n    result: label permutation control\\n  - exp_id: mvp_controlb_untrained\\n    role: running\\n    result: label permutation control\\n  depends_on:\\n  - D009\\n  - D007\\n- id: D011\\n  date: 2026-05-15 14:14 UTC\\n  summary: Control B 两组实验均确认 null hypothesis（shuffled labels ρ≈0），probe 方法论完全验证。关闭\\n    MVP 实验系列。\\n  rationale: 'Trained features + shuffled labels: 33 层全部 |ρ|<0.013，信噪比 73:1。Untrained\\n    features + shuffled labels: 33 层全部 |ρ|<0.01，信噪比 104:1。结合 DINO Control B (ρ=0.039,\\n    信噪比 23:1)，三模型均通过 null control。证明 temporal distance probe 观测到的 ρ=0.955/0.933/0.901\\n    是真实信号，非 probe 过拟合或数据泄漏。MVP 实验系列（mvp_001 到 Control B）全部完成，结论：temporal distance\\n    信号主要来自 vision encoder，VLA 训练贡献 Δρ=0.043（统计显著但实质不足）。'\\n  related_experiments:\\n  - exp_id: mvp_controlb_trained\\n    role: null control\\n    result: max |ρ|=0.013, PASS\\n  - exp_id: mvp_controlb_untrained\\n    role: null control\\n    result: max |ρ|=0.009, PASS\\n  - exp_id: mvp_probe_trained\\n    role: primary\\n    result: ρ=0.955, Δρ=0.043\\n  - exp_id: mvp_probe_untrained\\n    role: control C\\n    result: ρ=0.933\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: ρ=0.901\\n  depends_on:\\n  - D008\\n  - D010\\n- id: D012\\n  date: 2026-05-15 14:23 UTC\\n  summary: 'D012: Copy baseline R²=0.97 暴露 G1 阈值无效。增加 action-delta prediction 作为核心判定指标，修订\\n    MVP-2 gates。'\\n  rationale: Reviewer 发现 copy baseline（a_{t+1}=a_t）R²=0.97，根因是机器人轨迹平滑导致连续 action 自相关极高。原\\n    G1（R²>0.3）毫无区分力，G2 的 Δ 也可能被压缩——与 MVP-1 的 vision dominates 结构性同构。解决方案：预测 action-delta（Δa\\n    = a_{t+1} - a_t），copy baseline 对 Δa 的 R² 恒为 0，彻底消除自相关混淆。当前实验继续不中断，完成后用相同 features\\n    重新训练 probe 即可（分钟级）。修订 gates：G1 保留为 sanity check；新增 G1-delta（trained peak-layer\\n    R²(Δa)>0.05）和 G2-delta（Δ(trained-untrained) on Δa >0.03 且 ≥5/10 tasks 一致）。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: primary\\n    result: running\\n  - exp_id: mvp2_action_untrained\\n    role: control\\n    result: running\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-15 15:25 UTC\\n  summary: MVP-2 Action Prediction 综合判定：G3-delta FAIL（DINO 0.061 ≈ trained 0.059）。三条探测维度（temporal\\n    distance / action prediction / action-delta）均 vision-dominated。唯一 VLA-specific\\n    发现：layer stability（训练后表征通路稳定，untrained 中间层坍塌）。建议 pivot 到 LIBERO-Goal instruction-conditioned\\n    probing。\\n  rationale: MVP-2 完整结果：G1 PASS (0.683>0.3), G1-delta borderline PASS (0.059>0.05),\\n    G2 FAIL (best-vs-best Δ=0.067<0.15), G3-action FAIL (Δ=0.007), G3-delta FAIL (DINO\\n    0.061 ≥ trained 0.059)。G2-delta Agent 报 PASS 但存在 best-vs-best vs same-layer 口径差异需核实。核心问题：DINO\\n    单层（1024 dim）在 action 和 action-delta 上均匹配 trained VLA 33 层最优（4096 dim），说明 LIBERO-10\\n    中的 action 信号（包括高阶 delta）可从视觉状态推断。VLA 训练的唯一可探测效果是 layer stability——表征通路畅通（trained\\n    31/33 层 R²>0.45, untrained 仅 ~15/33 层有效），但内容质量（可预测的信息量）未超越纯视觉。这与 Grant et al.\\n    2026 的发现一致：LIBERO-10 是 vision-solvable benchmark，language 几乎被忽略。LIBERO-Goal（多目标共享视觉场景）是文献支撑最强的下一步——该场景中\\n    vision 无法区分 goal，必须依赖 instruction。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: primary\\n    result: action R²=0.683(L19), delta R²=0.059(L14)\\n  - exp_id: mvp2_action_untrained\\n    role: control\\n    result: action R²=0.616(L32), delta R²=0.049(L32)\\n  - exp_id: mvp2_action_dino\\n    role: baseline\\n    result: action R²=0.676, delta R²=0.061 — matches trained VLA\\n  depends_on:\\n  - D012\\n  - D010\\n- id: D014\\n  date: 2026-05-15 15:26 UTC\\n  summary: MVP-2 判死：action prediction + action-delta 三轮 probing 一致确认 LIBERO-10 上 VLA\\n    训练未注入视觉编码器以外的独特信息。Pivot 到 LIBERO-Goal instruction-conditioned probing。\\n  rationale: 三轮 probing 结果一致：(1) temporal distance Δρ=0.043, (2) raw action ΔR²=0.067(T-U)/0.007(T-DINO),\\n    (3) action-delta ΔR²=0.012(T-U)/-0.001(T-DINO, DINO 反超)。DINO 单层 1024-dim 在所有指标上打平或超过\\n    trained VLA 33 层 4096-dim。根因：LIBERO-10 单目标 tabletop 场景视觉状态强烈约束 action 空间，无需语言或策略推理消歧。文献支撑\\n    pivot：Grant et al. 2026 发现 LIBERO-Goal 多目标场景中 language 贡献关键（正确 prompt 94% vs 错误\\n    10%）。唯一正面发现：VLA 训练创造了跨层稳定表征（trained 31/33 层 > untrained），但这是 representational\\n    reorganization 而非 new knowledge，单独不足以撑论文。Agent 报告的 G2-delta PASS 有误——best-vs-best\\n    Δ=0.012 < 0.03，0/10 tasks 超过阈值，实为 FAIL。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: primary\\n    result: best L19 R²=0.683, delta best L14 R²=0.060\\n  - exp_id: mvp2_action_untrained\\n    role: control\\n    result: best L32 R²=0.616, delta best L32 R²=0.048\\n  - exp_id: mvp2_action_dino\\n    role: baseline\\n    result: R²=0.676 action, R²=0.061 delta — matches or exceeds trained\\n  - exp_id: mvp_probe_trained\\n    role: predecessor\\n    result: temporal distance ρ=0.955, Δρ=0.043\\n  - exp_id: mvp_probe_untrained\\n    role: predecessor\\n    result: temporal distance ρ=0.933\\n  depends_on:\\n  - D012\\n  - D010\\n  - D007\\n- id: D015\\n  date: 2026-05-15 16:06 UTC\\n  summary: '选择 Option A: Pivot 到 LIBERO-Goal instruction-conditioned probing。Reviewer\\n    独立评估一致推荐，预期 CoRL 录用概率 15-30%（vs Option B 的 5-12%），且 worst case 退化为加强版 B。'\\n  rationale: Reviewer 独立评估结论：(1) Expected value 最高——LIBERO-Goal positive 时构成 \\\"vision-sufficient\\n    vs vision-ambiguous\\\" 对比叙事，FAIL 时退化为双 benchmark negative（仍优于纯 Option B）；(2) 实验成本极低（特征提取\\n    ~半天 GPU + probe 复用）；(3) Layer-wise mechanistic insight 是 vs Grant et al. 2026\\n    的差异化卖点——Grant 只做了 behavioral（input-output），我们提供 WHERE/HOW 的 representational 证据；(4)\\n    11 天内可行（7-9 天实际工作量）。关键风险：OpenVLA checkpoint 仅在 LIBERO-10 fine-tune，未见过 LIBERO-Goal\\n    多目标场景。缓解：先检查 scene overlap，必要时做 LIBERO-Goal fine-tune（+1 天）。用户授权：\\\"你们确定好怎么走我就同意\\\"。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: evidence\\n    result: action-delta R²=0.059, DINO ≈ trained, vision-dominated\\n  - exp_id: mvp2_action_dino\\n    role: evidence\\n    result: delta R²=0.061, matches trained VLA\\n  depends_on:\\n  - D013\\n- id: D016\\n  date: 2026-05-15 16:16 UTC\\n  summary: LIBERO-Goal 实验统一用 base pretrained OpenVLA checkpoint（非 LIBERO-10 fine-tuned）。同时用\\n    pretrained 重提 LIBERO-10 特征，确保跨 benchmark 对比公平——唯一变量是 benchmark，非 fine-tuning 状态。\\n  rationale: Reviewer 指出 checkpoint 不一致 confound：LIBERO-10 用 fine-tuned、LIBERO-Goal\\n    用 pretrained → reviewer 会攻击差异来自 fine-tuning 而非 benchmark 特性。Solution 1（base pretrained\\n    统一）最 clean：(1) 唯一变量是 benchmark，排除 fine-tuning confound；(2) 如果 pretrained VLA 已编码\\n    instruction grounding，novelty 更高（pretraining 产物 vs task-specific fine-tuning 产物）；(3)\\n    额外 GPU 成本仅 3h，当前 GPU 空闲正好利用；(4) 与 Grant et al. 差异化更清晰（Grant 用 OFT fine-tuned，我们用\\n    pretrained）。附带发现：Grant 的 100%→10% 效应来自 OpenVLA-OFT 而非 base，我们效应量可能小一些但更有说服力。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: predecessor (fine-tuned)\\n    result: R²=0.683, will re-extract with pretrained\\n  - exp_id: mvp2_action_dino\\n    role: baseline\\n    result: R²=0.676, unchanged\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-15 16:22 UTC\\n  summary: D016 修正：改用 LIBERO-10 fine-tuned checkpoint 统一提取两个 benchmark 特征（取代 base\\n    pretrained 方案）。LIBERO-Goal 是 OOD 测试——场景不重叠，positive 结果 = 泛化而非记忆。\\n  rationale: Reviewer 二次审视后提出更优方案：(1) fine-tuned checkpoint 在 LIBERO-Goal 上是 OOD——场景确认不重叠、指令未见过，positive\\n    结果直接证明 instruction grounding 泛化能力，story 更强；(2) LIBERO-10 特征已提取完毕无需重跑，省 3h GPU；(3)\\n    同一 checkpoint 跨两个 benchmark = 公平对比，唯一变量仍是 benchmark 特性；(4) base pretrained 可作为后续\\n    ablation 补充（如果 fine-tuned 结果 positive 且时间允许）。此决策取代 D016 的 base pretrained 方案。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: existing features\\n    result: LIBERO-10 fine-tuned features already extracted, reusable\\n  depends_on:\\n  - D016\\n  - D015\\n- id: D018\\n  date: 2026-05-15 19:20 UTC\\n  summary: G3-GC FAIL 确认为维度混淆方法论问题，启动 PCA-1024 + linear probe 控制实验\\n  rationale: Untrained VLA bin 0 = 100%（与 trained 相同），证伪 \\\"language grounding from\\n    training\\\" 原 claim。根因是 4096-dim MLP probe 对 10 类分类 capacity 过大（Hewitt & Manning\\n    2019）。需要 PCA 降维到 1024（与 DINO 对齐）+ linear probe 消除维度和 probe complexity 混淆后重新判定。暂定\\n    Option C framing（Methodology + Temporal Dynamics），最终取决于 PCA 结果。\\n  related_experiments:\\n  - exp_id: lg_gc_untrained\\n    role: trigger\\n    result: G3-GC FAIL, Δ(trained-untrained)=0pp\\n  depends_on: []\\n- id: D019\\n  date: 2026-05-15 19:44 UTC\\n  summary: Goal classification probing 方法论失败，pivot 到 Representational Similarity Analysis\\n    (RSA) 测试 training 是否改善 action-relevant 表征结构\\n  rationale: Goal classification 无法区分 trained vs untrained VLA（5 个实验变体全部 ~100%）。根因：两者都接收\\n    instruction text 作为输入，即使 random LLM 的高维投影也能完美分离 10 个不同文本的 goal。这不是维度/probe 选择问题，而是任务设计根本缺陷——测的是\\\"表征是否包含\\n    instruction 信息\\\"（trivially yes），而非\\\"training 是否改善 instruction encoding\\\"。DINO 低(35%→97%)是因为没有\\n    instruction 输入，不是 language grounding 差异。下一步用 RSA 测量 representation space 与 action\\n    space 的结构对齐程度，这避免了 trivial separability 问题。\\n  related_experiments:\\n  - exp_id: lg_gc_trained_frame0\\n    role: evidence\\n    result: trained 100% L3+\\n  - exp_id: lg_gc_untrained\\n    role: evidence\\n    result: untrained also 100%\\n  - exp_id: lg_pca1024_linear_pertimestep\\n    role: evidence\\n    result: 'PCA-1024 linear: trained 99.9% vs untrained 100%'\\n  depends_on:\\n  - D018\\n  - D015\\n- id: D020\\n  date: 2026-05-15 19:51 UTC\\n  summary: 'D020: RSA success gates 定义 + 要求在 LIBERO-Goal 上优先运行（cross-goal same-scene\\n    RDM），kill dead-end GPU 进程'\\n  rationale: 'Reviewer WARNING: RSA 启动无 gate 定义，重复 D001-D014 教训。补定 gates：G1 trained\\n    best-layer RSA ρ(repr RDM, action RDM) > 0.15；G2 Δρ(trained-untrained) > 0.08\\n    且 bootstrap 95% CI 排除 0；G3 trained ρ > DINO ρ（任何正 margin）。关键设计约束：LIBERO-Goal 的\\n    same-scene/different-goal 对是核心——DINO 在这些对上 visual RDM 高度相似但 action RDM 完全不同，预期\\n    RSA ρ 接近 0 或为负；trained VLA 应展示 goal-conditioned action structure，ρ 应显著高于 untrained\\n    和 DINO。同时 Reviewer 发现 GPU 上仍有两个已关闭路线的进程（PID 650060, 648231），应 kill 释放资源。'\\n  related_experiments:\\n  - exp_id: lg_rsa_analysis\\n    role: primary\\n    result: running, gates now defined\\n  - exp_id: lg_gc_untrained\\n    role: predecessor\\n    result: goal classification dead\\n  - exp_id: lg_pca1024_linear_pertimestep\\n    role: predecessor\\n    result: PCA+linear confirmed trivial separability\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-15 20:08 UTC\\n  summary: 'D021: Framing pivot 到 Option B \\\"Architecture Trumps Training\\\"。5 轮 probing\\n    一致 G1+G3 PASS / G2 FAIL → VLA 架构提供 instruction conditioning，训练不改变表征结构。启动 instruction\\n    ablation + output head analysis 验证。'\\n  rationale: 6 轮实验（temporal distance, action prediction, action-delta, goal classification,\\n    RSA）× 2 benchmark（LIBERO-10, LIBERO-Goal）一致模式：trained ≈ untrained >> DINO。训练效应从未超过\\n    noise level（最大 Δρ=0.043）。三个 framing 备选中选 Option B 理由：(1) positive framing——\\\"架构设计驱动\\n    instruction conditioning\\\"比\\\"训练无用\\\"更 actionable；(2) 与 Grant 2026 互补（他们发现 behavioral\\n    \\\"encoded but not used\\\"，我们发现 representational \\\"not even encoded differently\\\"）；(3)\\n    只需 instruction ablation（1 个实验）验证机制——去掉 instruction 后 RSA 应 collapse，证明 architecture\\n    pathway 是关键；(4) output head analysis 补充解释行为改善如何在表征不变时发生（\\\"shallow adaptation\\\"）。Option\\n    C（random LLM sufficiency）作为 B 的自然推论在 Discussion 中讨论，不作为主 claim（需要 LLM size ablation，时间不够）。\\n  related_experiments:\\n  - exp_id: lg_rsa_analysis\\n    role: final confirming evidence\\n    result: G1 PASS ρ=0.49, G2 FAIL Δρ=0.003, G3 PASS Δ=0.10\\n  - exp_id: mvp_probe_trained\\n    role: temporal distance\\n    result: G2 FAIL Δρ=0.043\\n  - exp_id: mvp2_action_trained\\n    role: action prediction\\n    result: G2 FAIL ΔR²=0.067\\n  - exp_id: mvp2_action_dino\\n    role: action-delta baseline\\n    result: G3-delta FAIL, DINO ≈ trained\\n  - exp_id: lg_gc_untrained\\n    role: goal classification\\n    result: untrained 100% = trained\\n  depends_on:\\n  - D019\\n  - D020\\n  - D015\\n  - D014\\n- id: D022\\n  date: 2026-05-15 20:08 UTC\\n  summary: 'D021: RSA G2 FAIL (Δρ=0.003 << 0.08)。6 轮 probing 一致确认 VLA 训练不改变表征结构。Go/no-go\\n    决策点：推荐 Option A \\\"Representational Redundancy\\\" negative finding paper for CoRL'\\n  rationale: 6 轮系统性 probing（temporal distance / subtask / action prediction / action\\n    delta / goal classification / RSA）× 2 benchmarks（LIBERO-10 vision-sufficient +\\n    LIBERO-Goal vision-ambiguous）× 多种 probe（MLP/linear/PCA/RSA/CKA），全部呈现一致模式：G1 PASS（VLA\\n    表征编码 task-relevant 信息）、G2 FAIL（trained ≈ untrained，训练不改变表征内容）、G3 PASS（VLA >> DINO，架构提供\\n    instruction conditioning）。RSA 的 CKA 深层 0.85-0.86 进一步确认 trained-untrained 表征几何高度相似。原\\n    hypothesis \\\"VLA training contributes meaningful language grounding\\\" 被系统性否定。但 consistent\\n    negative + mechanistic insights (layer stability, temporal specialization) 本身构成有文献价值的发现——推翻\\n    VLA 领域 \\\"fine-tuning injects new representational knowledge\\\" 的隐性假设。三个 framing 备选：A)\\n    Representational Redundancy（最少额外实验）, B) Architecture Trumps Training（需 ablation）,\\n    C) Random LLM Sufficiency（需 LLM size ablation）。推荐 Option A：直接利用全部现有证据，仅需 output\\n    head analysis 补充 mechanism。\\n  related_experiments:\\n  - exp_id: lg_rsa_analysis\\n    role: final probe\\n    result: G1 PASS (ρ=0.488), G2 FAIL (Δ=0.003), G3 PASS (+0.10)\\n  - exp_id: mvp_probe_trained\\n    role: temporal distance\\n    result: Δρ=0.043\\n  - exp_id: mvp2_action_trained\\n    role: action prediction\\n    result: G3 FAIL, DINO ≈ trained\\n  - exp_id: lg_gc_untrained\\n    role: goal classification\\n    result: untrained 100% = trained 100%\\n  - exp_id: lg_pca1024_linear_pertimestep\\n    role: PCA+linear control\\n    result: Δ=-0.08pp\\n  depends_on:\\n  - D019\\n  - D020\\n  - D014\\n  - D013\\n- id: D023\\n  date: 2026-05-15 20:14 UTC\\n  summary: 'D023: Reviewer 共识——B framing 可行但 claim 需收窄为 \\\"instruction input pathway\\\"，instruction\\n    ablation 为 hard gate，FAIL 则回退 Option A'\\n  rationale: 两份独立 Reviewer 报告一致指出：(1) \\\"architecture\\\" 一词 overclaims——当前证据只证明 \\\"VLA pathway（含\\n    instruction 输入）>> 纯视觉\\\"，未 ablate 具体组件（text encoder / LLM backbone / fusion），应精确到\\n    \\\"instruction input pathway\\\"；(2) instruction ablation 是 blocking experiment，非 nice-to-have——没有它\\n    \\\"architecture provides instruction conditioning\\\" 是 speculation 不是 conclusion；(3)\\n    layer stability（31/33 vs 15/33）与 \\\"training doesn't change representation\\\" 存在内部张力，需定位为\\n    \\\"reorganization without new knowledge injection\\\"；(4) output head analysis 重要但非\\n    blocking（可放 Discussion）；(5) 最大 reviewer attack surface 是单 VLA 架构，scope 必须限定为 OpenVLA-class。采纳全部建议，设\\n    instruction ablation 为 hard gate：PASS 则锁定 B，FAIL 则立即回退 A。\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: blocking_gate\\n    result: PREPARING\\n  - exp_id: d021_output_head_analysis\\n    role: supporting\\n    result: PREPARING\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-15 20:15 UTC\\n  summary: 'D023: Reviewer 评估 D021 framing — 接受 claim 精度建议，记录 attack surface 应对'\\n  rationale: Reviewer warning 级别评估 D021 \\\"Architecture Trumps Training\\\" framing。关键采纳：(1)\\n    claim 从 \\\"architecture\\\" 精确到 \\\"instruction input pathway\\\"；(2) instruction ablation\\n    是 critical path，FAIL 则切 Option A；(3) \\\"trivial separability\\\" 攻击需 random instruction\\n    control 回应（research 阶段第一优先）；(4) Grant checkpoint 差异 + 单 VLA 架构限制需在 Discussion/Limitations\\n    处理。不采纳：trivial separability 严重度被高估——RSA 测量 representation-action geometry correspondence\\n    而非分类，但 control 实验仍值得做。\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: critical_path\\n    result: PREPARING\\n  - exp_id: d021_output_head_analysis\\n    role: supporting\\n    result: PREPARING\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D025\\n  date: 2026-05-15 20:17 UTC\\n  summary: 'D024: Instruction ablation gate 从绝对阈值改为 DINO-anchored 相对标准'\\n  rationale: Reviewer 指出绝对阈值 0.30 缺乏锚定依据。改用 DINO RSA 作为锚点的相对标准：PASS 要求 no-instruction\\n    RSA 显著下降（Δ>0.10, CI 排除 0）且退化到 DINO 水平；FAIL 要求去掉 instruction 几乎无影响（Δ<0.05）；中间为\\n    INCONCLUSIVE。这避免了 \\\"RSA=0.38 接近 DINO 但按绝对阈值判 PASS\\\" 的假阳性。\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: gate_definition\\n    result: PREPARING\\n  depends_on:\\n  - D023\\n- id: D026\\n  date: 2026-05-15 20:19 UTC\\n  summary: 'D025: Output head analysis FAIL — shallow adaptation 不成立，发现 projector\\n    bottleneck 机制'\\n  rationale: Head/LLM ratio = 1.12x (阈值 3x)，权重差异均匀分布于 LLM 32 层。但关键发现：SigLIP + Projector\\n    在 trained/untrained 间完全相同（rel_change=0, cos_sim=1.0），说明 untrained model 的 from_config()\\n    只重初始化 LLM。这提供了 trained≈untrained 的精确机制：frozen projector bottleneck 约束表征空间，使得下游\\n    LLM 权重（即使 cos_sim≈0.2 完全不同）无法改变表征结构。Shallow adaptation → Discussion 中 ruled-out\\n    hypothesis。Projector bottleneck → 替代机制解释。Caveat：当前比较是 pretrained+finetuned vs\\n    random init LLM，差异被 pretrained vs random 主导，但这恰恰是最强测试——如果极端不同的 LLM 都不影响表征，中间态更不会。\\n  related_experiments:\\n  - exp_id: d021_output_head_analysis\\n    role: primary\\n    result: FAIL_but_informative\\n  - exp_id: d021_instruction_ablation\\n    role: complementary\\n    result: RUNNING\\n  depends_on:\\n  - D024\\n- id: D027\\n  date: 2026-05-15 22:09 UTC\\n  summary: 'D027: Instruction Ablation FAIL — Option B 死亡，回退 Option A。选择 A2 \\\"Vision\\n    Encoder Dominance\\\" framing，SigLIP frozen encoder 是 action-relevant 表征的真正来源'\\n  rationale: 'Instruction ablation 结果：去掉 instruction text 后 untrained RSA ρ=0.4802\\n    vs with-inst ρ=0.4846，Δ=0.0044 远低于 0.10 阈值。no-inst RSA=0.48 远高于 DINO+0.05=0.438。Gate\\n    双 FAIL。Instruction pathway 不是 action-relevant 结构来源。\\n\\n\\n    综合全部证据链：(1) trained ≈ untrained（6 轮 probing 一致）；(2) VLA >> DINO（一致）；(3) instruction\\n    不影响 RSA（ablation 证实）；(4) SigLIP+projector frozen（output head analysis 证实）。唯一一致解释：SigLIP\\n    frozen vision encoder 决定了 action-relevant 表征结构。选 A2 framing 理由：指向具体组件，因果链清晰，与\\n    Grant 2026 互补（behavioral→representational），实用价值高（选 encoder 比 fine-tuning LLM 重要）。\\n\\n\\n    需补充 SigLIP-only features 提取 + RSA 作为 smoking gun 验证（不过 LLM 直接测 SigLIP 输出的 RSA），以及\\n    trained no-inst RSA 完成 2×2 matrix。两个实验完成 + positive → complete_mvp。'\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: hard_gate\\n    result: 'FAIL: Δ=0.0044 << 0.10, no-inst RSA=0.48 >> DINO+0.05'\\n  - exp_id: d021_output_head_analysis\\n    role: supporting\\n    result: 'negative but informative: projector bottleneck mechanism'\\n  - exp_id: lg_rsa_analysis\\n    role: baseline\\n    result: 'with-inst RSA: trained 0.49, untrained 0.48, DINO 0.39'\\n  depends_on:\\n  - D023\\n  - D026\\n- id: D028\\n  date: 2026-05-15 22:26 UTC\\n  summary: 'D028: SigLIP-only RSA smoking gun PASS (0.615 >> 0.488)。LLM 是 degrader\\n    而非 passthrough。complete_mvp 批准，A2 framing 升级含 LLM degradation claim'\\n  rationale: 'SigLIP+Projector RSA = 0.615，远超 Gate 阈值 0.45-0.50，也远超 full VLA 的 0.488。证明\\n    action-relevant 表征结构完全来自 frozen vision encoder。\\n\\n\\n    意外发现：LLM 不是 passthrough 而是 degrader（0.615→0.488），无论 trained/untrained、with/without\\n    instruction。2×2 matrix 四格全部收敛于 0.48-0.49，Bootstrap CI 包含 0。Per-layer analysis\\n    确认 instruction 对任何层无实质影响（max |Δ|<0.015）。\\n\\n\\n    A2 framing 升级为三个 core claims：(1) action-relevant 表征源自 frozen SigLIP encoder；(2)\\n    LLM processing 降低 action-relevant 结构（degrader，非 passthrough/enhancer）；(3) training\\n    和 instruction 均不改变表征结构。Claim 2 是 novel contribution——无已有论文测量过 projector output\\n    vs LLM hidden state 的 RSA 差异。\\n\\n\\n    批准 complete_mvp，进入 research/writing 阶段。CoRL abstract DDL May 26（11天），paper DDL\\n    May 29（14天）。'\\n  related_experiments:\\n  - exp_id: d027_siglip_only_rsa\\n    role: smoking_gun\\n    result: 'PASS: RSA=0.615, far exceeding 0.45-0.50 gate and full VLA 0.488'\\n  - exp_id: d027_trained_no_inst_rsa\\n    role: 2x2_completion\\n    result: All 4 cells converge at 0.48-0.49, training x instruction both null\\n  - exp_id: d021_instruction_ablation\\n    role: per_layer_analysis\\n    result: max |delta|<0.015 across all layers\\n  depends_on:\\n  - D027\\n  - D023\\n- id: D029\\n  date: 2026-05-15 22:43 UTC\\n  summary: 'D029: Claim 2 聚合伪影排除。VLA image_mean RSA=0.501 仍远低于 SigLIP 0.615（gap=0.114），LLM\\n    degradation 是真实效应。Per-layer 分析显示降解集中在 Proj→L1 界面，中间层部分恢复'\\n  rationale: 'Reviewer CRITICAL 指出 SigLIP 用 mean pooling vs VLA 用 last_preaction 不公平。验证结果：改用完全相同的\\n    image_mean 聚合后，trained VLA RSA=0.5014（vs last_preaction 0.4876，差异仅 0.014），仍远低于\\n    SigLIP 0.6153。Gap=0.114，LLM degradation ~18.5%，排除聚合伪影。\\n\\n\\n    Per-layer degradation curve 补充 nuance：(1) 降解主要在 Proj→L1 界面（drop 0.13-0.25）；(2)\\n    3/4 条件非单调，中间层部分恢复；(3) no-inst trained 独特呈 L1→L30 持续上升。Claim 2 措辞应精炼为 \\\"LLM input\\n    interface introduces primary degradation; subsequent layers partially recover\\n    but net degradation persists (~18%)\\\"。\\n\\n\\n    论文应同时呈现 last_preaction 和 image_mean 两种聚合的 RSA 作为 robustness check。'\\n  related_experiments:\\n  - exp_id: d027_siglip_only_rsa\\n    role: reference\\n    result: RSA=0.6153 (mean pooling)\\n  - exp_id: plan_003_perlayer_degradation\\n    role: supplementary\\n    result: Proj→L1 drop 0.13-0.25, non-monotonic recovery\\n  - exp_id: d027_trained_no_inst_rsa\\n    role: aggregation_check\\n    result: 'image_mean RSA: trained 0.5014, untrained 0.4847'\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-15 23:20 UTC\\n  summary: 'D030: Dream 三档均低于 acceptance（best borderline reject, median 5/10, worst\\n    4/10）。6 个结构性问题识别，P0 行动：functional validation via projector-output action probe'\\n  rationale: 'Dream 审稿三档一致指出 6 个结构性问题：(1) 无功能验证——RSA geometric alignment 不等于 task\\n    performance，是论文最大弱点；(2) 单架构 claim 过广；(3) confirmatory of concurrent behavioral\\n    work；(4) related work 严重不足；(5) LIBERO-only；(6) degradation framing 争议。\\n\\n\\n    P0 行动——functional validation 实验：在 projector output features 上训练 linear action\\n    predictor，对比 best LLM layer（已有 R²=0.683 from MVP-2）和 DINO（R²=0.676）。如果 projector\\n    R² ≥ LLM best → \\\"degradation is functional\\\" 从 correlational 升级为 causal evidence，彻底回应\\n    D1+D6。Features 已提取，probe 代码可复用，CPU/minimal GPU，~1h。\\n\\n\\n    P1 行动——scope claims to OpenVLA, 提升 trained≈untrained 为核心 novelty, 扩充 related work,\\n    加 figures。\\n\\n\\n    framing + plan 改动后必须 re-dream 验证。'\\n  related_experiments:\\n  - exp_id: d027_siglip_only_rsa\\n    role: features_source\\n    result: projector output features available for action probe\\n  - exp_id: mvp2_action_trained\\n    role: comparison\\n    result: LLM best layer R²=0.683\\n  - exp_id: mvp2_action_dino\\n    role: comparison\\n    result: DINO R²=0.676\\n  depends_on:\\n  - D028\\n  - D029\\n- id: D031\\n  date: 2026-05-15 23:43 UTC\\n  summary: 'Claim 2 framing pivot: \\\"LLM degrades\\\" → \\\"LLM redistributes\\\" — functional\\n    probe reveals LLM degrades image tokens (0.706→0.683) but concentrates action\\n    signal to readout token (0.731)'\\n  rationale: plan_011 functional validation 揭示了比 RSA 更丰富的图景：(1) Projector R²=0.706\\n    > LLM image_mean 0.683 确认 image token 级别的功能性降解；(2) 但 LLM last_preaction 0.731\\n    > Projector 0.706（bootstrap p=0.001），说明 LLM 的 attention 机制将分散的 action 信号聚合到 readout\\n    token。新 framing \\\"redistribution\\\" 比 \\\"degradation\\\" 更准确、更 interesting、且直接回应 Dream\\n    审稿 W3 concern（\\\"degradation framing interpretively problematic\\\"）。Core insight 不变：vision\\n    encoder 是 action information 的源头，LLM 的贡献是 readout/concentration 而非 new information\\n    injection。\\n  related_experiments:\\n  - exp_id: p0_functional_action_probe\\n    role: primary\\n    result: Projector R²=0.706 > LLM image_mean 0.683, but LLM last_preaction 0.731\\n      > Projector. PASS with nuance.\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-15 23:47 UTC\\n  summary: Confirm Option A framing (\\\"LLM routes, not creates\\\"); functional probe\\n    needs re-run with bootstrap CI for main comparison + DINO probe\\n  rationale: 'Reviewer CRITICAL: (1) projector vs image_mean_trained (0.706 vs 0.683)\\n    缺 bootstrap CI，当前 PASS 无统计检验支撑；(2) DINO probe 未包含，缺三方对比。Delta probe BELOW 但 CI\\n    含 0。Agent 提出三个 framing option，选 A（\\\"96.6% functional capacity already in projector,\\n    LLM contributes routing not knowledge\\\"）——最平衡，保持 redistribution 叙事同时 defensible。修正后重跑是\\n    re-dream 前置条件。'\\n  related_experiments:\\n  - exp_id: p0_functional_action_probe\\n    role: primary\\n    result: 'PASS pending stat verification: proj 0.706 vs LLM img_mean 0.683 (CI\\n      needed), readout 0.731 (p=0.001)'\\n  - exp_id: p0_functional_action_delta_probe\\n    role: secondary\\n    result: 'BELOW: proj 0.118 < LLM 0.122, CI includes 0, not significant'\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 23:54 UTC\\n  summary: 'DINO R²=0.712 ≈ Projector R²=0.706 (p=0.22) — Claim 1 reframe: geometric-functional\\n    dissociation. SigLIP advantage is geometric alignment (RSA), not predictive content\\n    (R²)'\\n  rationale: V2 probe 发现 DINO functional R²=0.712，与 SigLIP projector 0.706 无显著差异（p=0.22）。但\\n    RSA 维度 SigLIP (0.615) >> DINO (0.388)。这意味着：(1) action-relevant 信息在视觉编码器中是 ubiquitous\\n    的，不是 VL pretraining 独有；(2) VL pretraining 的价值在于 geometric organization（让表征几何结构与\\n    action 结构对齐），而非增加 predictive content。这个 geometric-functional dissociation 本身是一个新颖发现，可以强化论文。Claim\\n    1 从 \\\"SigLIP dominance\\\" 调整为 \\\"vision encoders universally contain action info +\\n    VL pretraining provides geometric alignment\\\"。旧 DINO 数字 0.676（MVP-2）已过时，V2 的 0.712\\n    是同一框架内的可信数字。仍需补 untrained last_preaction (C001) 和调查 MVP-2 vs V2 差异。\\n  related_experiments:\\n  - exp_id: p0_functional_probe_v2\\n    role: primary\\n    result: 'DINO CLS R²=0.712, Projector R²=0.706, p=0.22 NS. Bootstrap projector\\n      vs img_mean: delta=+0.023, CI=[0.011, 0.037], p<0.001 confirmed.'\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-16 00:07 UTC\\n  summary: 'Untrained last_preaction R²=0.689 < projector 0.706: redistribution is\\n    training-dependent. Claim 2 add qualifier, Claim 3 split by aggregation'\\n  rationale: C001 untrained 对照完成。Untrained readout best (L1, 0.689) < projector (0.706)\\n    < trained readout (L19, 0.731)。这意味着：(1) LLM 的 readout concentration 不是架构固有属性，需要训练才能超过\\n    projector baseline；(2) Claim 3 (training invariance) 在 image_mean 维度成立（distributed\\n    representation invariant）但在 last_preaction 维度不成立（readout concentration training-dependent）。综合\\n    story：VLA training 的贡献不是注入新的 action knowledge（image_mean invariant），而是学习将已有的 visual\\n    action information 高效路由到 output position（readout concentration learned）。这与 \\\"LLM\\n    routes, not creates\\\" (Option A) 完美一致，且比纯 \\\"training invariance\\\" 更有深度。需补 untrained\\n    vs trained last_preaction bootstrap CI 做统计确认。\\n  related_experiments:\\n  - exp_id: p0_functional_probe_v2\\n    role: primary\\n    result: Untrained last_preaction best L1 R²=0.689 < projector 0.706. L12-L18 +\\n      L24-L31 all collapsed to chance (0.059). Training-dependent redistribution confirmed.\\n  depends_on:\\n  - D031\\n  - D033\\n\", \"total_chars\": 33237, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "f1cc8f8e-434d-4a10-b185-f23a1018170e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/decisions.yaml\\\", \\\"content\\\": \\\"_next_id: 35\\\\ndecisions:\\\\n- id: D001\\\\n  date: 2026-05-15 11:03 UTC\\\\n  summary: MVP 三分支判定标准校准：ρ下限0.3→0.5, Δρ加bootstrap CI, subtask gate加DINO baseline对比\\\\n  rationale: Reviewer 审查发现四项校准缺陷：(1) ρ>0.3 下限过低（DINO-V2 已达0.833，0.3只挡彻底失败）→ 提至0.5；(2)\\\\n    Δρ>0.1 仅为点估计缺统计检验 → 追加 bootstrapped 95% CI must exclude 0；(3) subtask_AUC>0.7\\\\n    无 baseline 锚点（不知道 DINO-V2 能做到多少）→ 增加条件 subtask_AUC > DINO_subtask_AUC + 0.05；(4)\\\\n    layer profile 不入正式判定但作为 mandatory supplementary analysis。修改后标准更严谨，降低 false positive\\\\n    PASS 风险。\\\\n  related_experiments:\\\\n  - exp_id: dino-v2-baseline\\\\n    role: baseline\\\\n    result: ρ=0.833\\\\n  depends_on: []\\\\n- id: D002\\\\n  date: 2026-05-15 12:02 UTC\\\\n  summary: MVP 判定全面切换到 per-task mean ρ，弃用 pooled ρ\\\\n  rationale: Reviewer 指出 pooled ρ 受 cross-task variance 膨胀（DINO pooled=0.833 vs per-task\\\\n    mean=0.554）。pooled-vs-pooled 虽对称但偏严（可能 false negative）。切换 per-task mean 与 task-level\\\\n    bootstrap CI 方法论一致，且是更公平的 apples-to-apples 比较。影响：VLA≥DINO gate 从 ρ≥0.833 变为 per-task\\\\n    mean≥0.554；ρ>0.5 下限同样改为 per-task mean。\\\\n  related_experiments:\\\\n  - exp_id: dinov2_baseline\\\\n    role: baseline\\\\n    result: pooled ρ=0.833, per-task mean=0.554\\\\n  depends_on:\\\\n  - D001\\\\n- id: D003\\\\n  date: 2026-05-15 12:31 UTC\\\\n  summary: 移除 subtask AUC gate，MVP 判定简化为纯 temporal distance (ρ) 路径\\\\n  rationale: DINO-V2 subtask AUC = 0.9717，Path B 要求 VLA > DINO + 0.05 = 1.0217，数学不可达（AUC\\\\n    上限 1.0）。根因：subtask 间视觉差异大，任何强视觉编码器都能高 AUC 区分——subtask discrimination 不是 VLA 的差异化能力。Temporal\\\\n    distance（连续进度信号）才是 VLA 可能独有的编码维度。简化后判定：PASS 需 VLA_ρ ≥ DINO_ρ (0.833)；CONDITIONAL\\\\n    需 Δρ > 0.1 但 VLA_ρ < DINO_ρ；FAIL 需 ρ ≤ 0.5 或 Δρ ≤ 0.1。Subtask AUC 保留为补充分析，不参与\\\\n    gate。\\\\n  related_experiments:\\\\n  - exp_id: dinov2_baseline\\\\n    role: trigger\\\\n    result: subtask AUC 0.9717 使 Path B 数学不可达\\\\n  depends_on:\\\\n  - D001\\\\n- id: D004\\\\n  date: 2026-05-15 12:35 UTC\\\\n  summary: D003 勘误：DINO gate 阈值从 0.833 (pooled) 修正为 0.554 (per-task mean)，与 D002 对齐\\\\n  rationale: D003 写 ROADMAP 时误用 pooled ρ 0.833 作为 DINO gate 阈值，但 D002 已明确\\\\\\\"全面切换到 per-task\\\\n    mean ρ，弃用 pooled\\\\\\\"。DINO per-task mean ρ = 0.554。0.833 vs 0.554 差 0.28，直接影响 PASS/FAIL\\\\n    判定——用 0.833 会错误地将本应 PASS 的结果判为 CONDITIONAL。修正后所有文档/代码统一使用 per-task mean。同时确认 analyze_mvp.py\\\\n    废弃决策不变（urgent 指令已发）。\\\\n  related_experiments:\\\\n  - exp_id: dinov2_baseline\\\\n    role: reference\\\\n    result: pooled ρ=0.833, per-task mean ρ=0.554\\\\n  depends_on:\\\\n  - D002\\\\n  - D003\\\\n- id: D005\\\\n  date: 2026-05-15 13:31 UTC\\\\n  summary: D004 DINO gate 阈值作废：0.554→0.901。旧值基于 500 pairs/task 的噪声结果，新管道 5000 pairs/task\\\\n    下 DINO per-task mean ρ=0.9008\\\\n  rationale: 'Reviewer CRITICAL: 新管道 rerun DINO-V2 基线，per-task mean ρ 从 0.554 暴涨至\\\\n    0.901（10x 采样密度消除噪声）。旧管道 pooled/per-task 差异(0.833/0.554)是采样伪影。Gate 3 阈值必须更新为 0.901，否则\\\\n    analyze_results.py 判定标准错误。dinov2_baseline registry metrics 标为 invalidated。'\\\\n  related_experiments:\\\\n  - exp_id: dinov2_baseline\\\\n    role: baseline\\\\n    result: 旧 metrics invalidated; rerun per-task mean ρ=0.9008\\\\n  - exp_id: mvp_probe_trained\\\\n    role: primary\\\\n    result: layers 1-5 ρ≈0.950\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: control\\\\n    result: layers 1-5 ρ≈0.925, Δρ max 0.043\\\\n  depends_on:\\\\n  - D004\\\\n- id: D006\\\\n  date: 2026-05-15 13:32 UTC\\\\n  summary: 'DINO baseline invalidated: 旧管道 ρ=0.554 作废，新管道 ρ=0.901。Gate 3 阈值更新为 0.901。Gate\\\\n    2 预判高风险（layers 1-5 max Δρ=0.043 << 0.1）'\\\\n  rationale: Worker 用更新后的 train_probes.py 重跑 DINO baseline，per_task_n_pairs 从 500→5000，per-task\\\\n    mean ρ 从 0.554 暴涨至 0.901。旧结果系统性低估——所有 10 task 均在 0.84-0.93（旧值 0.41-0.68）。D001-D004\\\\n    的判定标准建立在错误基线上。同时 trained(ρ≈0.95) vs untrained(ρ≈0.93) vs DINO(ρ≈0.90) 三者差距极小，temporal\\\\n    distance 信号主要来自 vision encoder 而非 LLM 训练。等待 33 层全结果确认。\\\\n  related_experiments:\\\\n  - exp_id: dinov2_baseline\\\\n    role: invalidated baseline\\\\n    result: 旧 ρ=0.554 作废，新 ρ=0.901\\\\n  - exp_id: mvp_probe_trained\\\\n    role: running probe\\\\n    result: layers 1-5 mean ρ≈0.95\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: running control\\\\n    result: layers 1-5 mean ρ≈0.93, Δρ<0.05\\\\n  depends_on:\\\\n  - D004\\\\n- id: D007\\\\n  date: 2026-05-15 13:49 UTC\\\\n  summary: MVP Gate 2 FAIL 确认：33 层全结果，非坍塌层最大 Δρ=0.043 << 0.1。Temporal distance 信号来自\\\\n    vision encoder 而非 VLA 训练。Pivot 到 subtask predicate probe + 实用 pipeline 双线验证\\\\n  rationale: '完整 33 层数据：trained best ρ=0.956(L3), untrained best ρ=0.933(L1), DINO\\\\n    ρ=0.901。非坍塌层 Δρ 范围 0.003-0.043，无任何层接近 0.1 阈值。Gate 1 PASS(ρ>>0.5), Gate 2 FAIL(Δρ<<0.1),\\\\n    Gate 3 PASS(0.956>0.901)。科学结论：temporal distance 信号主要来自 SigLIP vision encoder，LLM\\\\n    fine-tuning 贡献 ~2-4% ρ，统计显著但实质极小。\\\\n\\\\n\\\\n    Pivot 理由：temporal distance 与 visual change 高度相关，vision encoder 天然擅长，不是测试 VLA 训练贡献的好\\\\n    probe。IDEA_BRIEF 原计划包含 subtask predicate classification（is_grasped, is_on_table\\\\n    等离散语义属性），这类信号需要理解 action 语义而非视觉相似度，vision encoder 不应有优势。先快速验证 subtask probe 是否展示\\\\n    VLA-specific 贡献，同时推进实用 pipeline（VLA ρ=0.95 已足够强，不管信号来源，self-scoring 可行）。'\\\\n  related_experiments:\\\\n  - exp_id: mvp_probe_trained\\\\n    role: primary probe\\\\n    result: best L3 ρ=0.956, 33 layers complete\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: control C\\\\n    result: best L1 ρ=0.933, Δρ max=0.043\\\\n  - exp_id: dinov2_baseline\\\\n    role: baseline (rerun)\\\\n    result: ρ=0.901\\\\n  depends_on:\\\\n  - D006\\\\n- id: D008\\\\n  date: 2026-05-15 13:58 UTC\\\\n  summary: MVP Gate 2 确认 FAIL（clean verdict）。Subtask predicate probe 是最后一道 VLA-specific\\\\n    signal 测试，48h 内出 CoRL go/no-go。\\\\n  rationale: P0 修复后 33 层全量结果：非坍塌层 max Δρ=0.043 << 0.1，CI [0.036, 0.050] 排除零但效应量不足。根因：temporal\\\\n    distance ≈ visual change，SigLIP 天然擅长（untrained ρ=0.933）。Subtask predicate probe（BDDL\\\\n    predicates）测试 VLA 是否编码离散 action-semantic 属性，但 DINO auto-extracted subtask AUC=0.97\\\\n    构成高 baseline 风险。设 48h 决策窗口：subtask probe 结果 + Control B 完成后做 CoRL go/no-go。\\\\n  related_experiments:\\\\n  - exp_id: mvp_probe_trained\\\\n    role: primary\\\\n    result: 'negative: Δρ=0.043'\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: control\\\\n    result: 'success: ρ=0.933 baseline'\\\\n  - exp_id: dinov2_baseline\\\\n    role: baseline\\\\n    result: 'success: ρ=0.901'\\\\n  - exp_id: mvp_controlb_trained\\\\n    role: control\\\\n    result: running\\\\n  - exp_id: mvp_controlb_untrained\\\\n    role: control\\\\n    result: running\\\\n  depends_on:\\\\n  - D007\\\\n- id: D009\\\\n  date: 2026-05-15 14:04 UTC\\\\n  summary: Subtask predicate pivot 终止。DINO auto-extracted subtask AUC=0.9717 > 0.95\\\\n    gate，所有 BDDL predicates 视觉可辨，VLA 训练无独特优势。转向 action prediction probe 调研。\\\\n  rationale: LIBERO tabletop 场景中 is_grasped/is_on_table/is_in_drawer 等 predicates\\\\n    在第三人称+手腕相机下视觉可辨，纯视觉模型即可高精度分类。根本问题：需要\\\\\\\"视觉不可达\\\\\\\"的 probing task 才能体现 VLA LLM 训练的独特贡献。Action\\\\n    prediction（预测 next action）需要策略知识，vision encoder 天然不擅长，是最有潜力的候选方向。\\\\n  related_experiments:\\\\n  - exp_id: dinov2_baseline\\\\n    role: evidence\\\\n    result: DINO subtask AUC=0.9717\\\\n  - exp_id: mvp_probe_trained\\\\n    role: context\\\\n    result: Δρ=0.043 insufficient\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: context\\\\n    result: untrained ρ=0.933 vision-dominated\\\\n  depends_on:\\\\n  - D008\\\\n- id: D010\\\\n  date: 2026-05-15 14:09 UTC\\\\n  summary: 批准 Action Prediction Probe 作为 MVP-2 方向。设定三门判定：G1 R²>0.3, G2 ΔR²(trained-untrained)>0.15,\\\\n    G3 ΔR²(trained-DINO)>0.15\\\\n  rationale: Temporal distance (D007) 和 subtask predicate (D009) 均因\\\\\\\"视觉可辨\\\\\\\"失败。Action\\\\n    prediction 需策略知识，vision encoder 不擅长，是区分 VLA 训练贡献的合理 probing task。数据现成（LIBERO HDF5\\\\n    自带 7-DoF action），特征可复用，运行快（~20min），低风险高信息量。\\\\n  related_experiments:\\\\n  - exp_id: mvp_probe_trained\\\\n    role: predecessor\\\\n    result: Δρ=0.043, temporal distance 视觉可辨\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: predecessor\\\\n    result: baseline for G2 comparison\\\\n  - exp_id: dinov2_baseline\\\\n    role: predecessor\\\\n    result: ρ=0.901, 证明 temporal distance 视觉可辨\\\\n  - exp_id: mvp_controlb_trained\\\\n    role: running\\\\n    result: label permutation control\\\\n  - exp_id: mvp_controlb_untrained\\\\n    role: running\\\\n    result: label permutation control\\\\n  depends_on:\\\\n  - D009\\\\n  - D007\\\\n- id: D011\\\\n  date: 2026-05-15 14:14 UTC\\\\n  summary: Control B 两组实验均确认 null hypothesis（shuffled labels ρ≈0），probe 方法论完全验证。关闭\\\\n    MVP 实验系列。\\\\n  rationale: 'Trained features + shuffled labels: 33 层全部 |ρ|<0.013，信噪比 73:1。Untrained\\\\n    features + shuffled labels: 33 层全部 |ρ|<0.01，信噪比 104:1。结合 DINO Control B (ρ=0.039,\\\\n    信噪比 23:1)，三模型均通过 null control。证明 temporal distance probe 观测到的 ρ=0.955/0.933/0.901\\\\n    是真实信号，非 probe 过拟合或数据泄漏。MVP 实验系列（mvp_001 到 Control B）全部完成，结论：temporal distance\\\\n    信号主要来自 vision encoder，VLA 训练贡献 Δρ=0.043（统计显著但实质不足）。'\\\\n  related_experiments:\\\\n  - exp_id: mvp_controlb_trained\\\\n    role: null control\\\\n    result: max |ρ|=0.013, PASS\\\\n  - exp_id: mvp_controlb_untrained\\\\n    role: null control\\\\n    result: max |ρ|=0.009, PASS\\\\n  - exp_id: mvp_probe_trained\\\\n    role: primary\\\\n    result: ρ=0.955, Δρ=0.043\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: control C\\\\n    result: ρ=0.933\\\\n  - exp_id: dinov2_baseline\\\\n    role: baseline\\\\n    result: ρ=0.901\\\\n  depends_on:\\\\n  - D008\\\\n  - D010\\\\n- id: D012\\\\n  date: 2026-05-15 14:23 UTC\\\\n  summary: 'D012: Copy baseline R²=0.97 暴露 G1 阈值无效。增加 action-delta prediction 作为核心判定指标，修订\\\\n    MVP-2 gates。'\\\\n  rationale: Reviewer 发现 copy baseline（a_{t+1}=a_t）R²=0.97，根因是机器人轨迹平滑导致连续 action 自相关极高。原\\\\n    G1（R²>0.3）毫无区分力，G2 的 Δ 也可能被压缩——与 MVP-1 的 vision dominates 结构性同构。解决方案：预测 action-delta（Δa\\\\n    = a_{t+1} - a_t），copy baseline 对 Δa 的 R² 恒为 0，彻底消除自相关混淆。当前实验继续不中断，完成后用相同 features\\\\n    重新训练 probe 即可（分钟级）。修订 gates：G1 保留为 sanity check；新增 G1-delta（trained peak-layer\\\\n    R²(Δa)>0.05）和 G2-delta（Δ(trained-untrained) on Δa >0.03 且 ≥5/10 tasks 一致）。\\\\n  related_experiments:\\\\n  - exp_id: mvp2_action_trained\\\\n    role: primary\\\\n    result: running\\\\n  - exp_id: mvp2_action_untrained\\\\n    role: control\\\\n    result: running\\\\n  depends_on:\\\\n  - D010\\\\n- id: D013\\\\n  date: 2026-05-15 15:25 UTC\\\\n  summary: MVP-2 Action Prediction 综合判定：G3-delta FAIL（DINO 0.061 ≈ trained 0.059）。三条探测维度（temporal\\\\n    distance / action prediction / action-delta）均 vision-dominated。唯一 VLA-specific\\\\n    发现：layer stability（训练后表征通路稳定，untrained 中间层坍塌）。建议 pivot 到 LIBERO-Goal instruction-conditioned\\\\n    probing。\\\\n  rationale: MVP-2 完整结果：G1 PASS (0.683>0.3), G1-delta borderline PASS (0.059>0.05),\\\\n    G2 FAIL (best-vs-best Δ=0.067<0.15), G3-action FAIL (Δ=0.007), G3-delta FAIL (DINO\\\\n    0.061 ≥ trained 0.059)。G2-delta Agent 报 PASS 但存在 best-vs-best vs same-layer 口径差异需核实。核心问题：DINO\\\\n    单层（1024 dim）在 action 和 action-delta 上均匹配 trained VLA 33 层最优（4096 dim），说明 LIBERO-10\\\\n    中的 action 信号（包括高阶 delta）可从视觉状态推断。VLA 训练的唯一可探测效果是 layer stability——表征通路畅通（trained\\\\n    31/33 层 R²>0.45, untrained 仅 ~15/33 层有效），但内容质量（可预测的信息量）未超越纯视觉。这与 Grant et al.\\\\n    2026 的发现一致：LIBERO-10 是 vision-solvable benchmark，language 几乎被忽略。LIBERO-Goal（多目标共享视觉场景）是文献支撑最强的下一步——该场景中\\\\n    vision 无法区分 goal，必须依赖 instruction。\\\\n  related_experiments:\\\\n  - exp_id: mvp2_action_trained\\\\n    role: primary\\\\n    result: action R²=0.683(L19), delta R²=0.059(L14)\\\\n  - exp_id: mvp2_action_untrained\\\\n    role: control\\\\n    result: action R²=0.616(L32), delta R²=0.049(L32)\\\\n  - exp_id: mvp2_action_dino\\\\n    role: baseline\\\\n    result: action R²=0.676, delta R²=0.061 — matches trained VLA\\\\n  depends_on:\\\\n  - D012\\\\n  - D010\\\\n- id: D014\\\\n  date: 2026-05-15 15:26 UTC\\\\n  summary: MVP-2 判死：action prediction + action-delta 三轮 probing 一致确认 LIBERO-10 上 VLA\\\\n    训练未注入视觉编码器以外的独特信息。Pivot 到 LIBERO-Goal instruction-conditioned probing。\\\\n  rationale: 三轮 probing 结果一致：(1) temporal distance Δρ=0.043, (2) raw action ΔR²=0.067(T-U)/0.007(T-DINO),\\\\n    (3) action-delta ΔR²=0.012(T-U)/-0.001(T-DINO, DINO 反超)。DINO 单层 1024-dim 在所有指标上打平或超过\\\\n    trained VLA 33 层 4096-dim。根因：LIBERO-10 单目标 tabletop 场景视觉状态强烈约束 action 空间，无需语言或策略推理消歧。文献支撑\\\\n    pivot：Grant et al. 2026 发现 LIBERO-Goal 多目标场景中 language 贡献关键（正确 prompt 94% vs 错误\\\\n    10%）。唯一正面发现：VLA 训练创造了跨层稳定表征（trained 31/33 层 > untrained），但这是 representational\\\\n    reorganization 而非 new knowledge，单独不足以撑论文。Agent 报告的 G2-delta PASS 有误——best-vs-best\\\\n    Δ=0.012 < 0.03，0/10 tasks 超过阈值，实为 FAIL。\\\\n  related_experiments:\\\\n  - exp_id: mvp2_action_trained\\\\n    role: primary\\\\n    result: best L19 R²=0.683, delta best L14 R²=0.060\\\\n  - exp_id: mvp2_action_untrained\\\\n    role: control\\\\n    result: best L32 R²=0.616, delta best L32 R²=0.048\\\\n  - exp_id: mvp2_action_dino\\\\n    role: baseline\\\\n    result: R²=0.676 action, R²=0.061 delta — matches or exceeds trained\\\\n  - exp_id: mvp_probe_trained\\\\n    role: predecessor\\\\n    result: temporal distance ρ=0.955, Δρ=0.043\\\\n  - exp_id: mvp_probe_untrained\\\\n    role: predecessor\\\\n    result: temporal distance ρ=0.933\\\\n  depends_on:\\\\n  - D012\\\\n  - D010\\\\n  - D007\\\\n- id: D015\\\\n  date: 2026-05-15 16:06 UTC\\\\n  summary: '选择 Option A: Pivot 到 LIBERO-Goal instruction-conditioned probing。Reviewer\\\\n    独立评估一致推荐，预期 CoRL 录用概率 15-30%（vs Option B 的 5-12%），且 worst case 退化为加强版 B。'\\\\n  rationale: Reviewer 独立评估结论：(1) Expected value 最高——LIBERO-Goal positive 时构成 \\\\\\\"vision-sufficient\\\\n    vs vision-ambiguous\\\\\\\" 对比叙事，FAIL 时退化为双 benchmark negative（仍优于纯 Option B）；(2) 实验成本极低（特征提取\\\\n    ~半天 GPU + probe 复用）；(3) Layer-wise mechanistic insight 是 vs Grant et al. 2026\\\\n    的差异化卖点——Grant 只做了 behavioral（input-output），我们提供 WHERE/HOW 的 representational 证据；(4)\\\\n    11 天内可行（7-9 天实际工作量）。关键风险：OpenVLA checkpoint 仅在 LIBERO-10 fine-tune，未见过 LIBERO-Goal\\\\n    多目标场景。缓解：先检查 scene overlap，必要时做 LIBERO-Goal fine-tune（+1 天）。用户授权：\\\\\\\"你们确定好怎么走我就同意\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: mvp2_action_trained\\\\n    role: evidence\\\\n    result: action-delta R²=0.059, DINO ≈ trained, vision-dominated\\\\n  - exp_id: mvp2_action_dino\\\\n    role: evidence\\\\n    result: delta R²=0.061, matches trained VLA\\\\n  depends_on:\\\\n  - D013\\\\n- id: D016\\\\n  date: 2026-05-15 16:16 UTC\\\\n  summary: LIBERO-Goal 实验统一用 base pretrained OpenVLA checkpoint（非 LIBERO-10 fine-tuned）。同时用\\\\n    pretrained 重提 LIBERO-10 特征，确保跨 benchmark 对比公平——唯一变量是 benchmark，非 fine-tuning 状态。\\\\n  rationale: Reviewer 指出 checkpoint 不一致 confound：LIBERO-10 用 fine-tuned、LIBERO-Goal\\\\n    用 pretrained → reviewer 会攻击差异来自 fine-tuning 而非 benchmark 特性。Solution 1（base pretrained\\\\n    统一）最 clean：(1) 唯一变量是 benchmark，排除 fine-tuning confound；(2) 如果 pretrained VLA 已编码\\\\n    instruction grounding，novelty 更高（pretraining 产物 vs task-specific fine-tuning 产物）；(3)\\\\n    额外 GPU 成本仅 3h，当前 GPU 空闲正好利用；(4) 与 Grant et al. 差异化更清晰（Grant 用 OFT fine-tuned，我们用\\\\n    pretrained）。附带发现：Grant 的 100%→10% 效应来自 OpenVLA-OFT 而非 base，我们效应量可能小一些但更有说服力。\\\\n  related_experiments:\\\\n  - exp_id: mvp2_action_trained\\\\n    role: predecessor (fine-tuned)\\\\n    result: R²=0.683, will re-extract with pretrained\\\\n  - exp_id: mvp2_action_dino\\\\n    role: baseline\\\\n    result: R²=0.676, unchanged\\\\n  depends_on:\\\\n  - D015\\\\n- id: D017\\\\n  date: 2026-05-15 16:22 UTC\\\\n  summary: D016 修正：改用 LIBERO-10 fine-tuned checkpoint 统一提取两个 benchmark 特征（取代 base\\\\n    pretrained 方案）。LIBERO-Goal 是 OOD 测试——场景不重叠，positive 结果 = 泛化而非记忆。\\\\n  rationale: Reviewer 二次审视后提出更优方案：(1) fine-tuned checkpoint 在 LIBERO-Goal 上是 OOD——场景确认不重叠、指令未见过，positive\\\\n    结果直接证明 instruction grounding 泛化能力，story 更强；(2) LIBERO-10 特征已提取完毕无需重跑，省 3h GPU；(3)\\\\n    同一 checkpoint 跨两个 benchmark = 公平对比，唯一变量仍是 benchmark 特性；(4) base pretrained 可作为后续\\\\n    ablation 补充（如果 fine-tuned 结果 positive 且时间允许）。此决策取代 D016 的 base pretrained 方案。\\\\n  related_experiments:\\\\n  - exp_id: mvp2_action_trained\\\\n    role: existing features\\\\n    result: LIBERO-10 fine-tuned features already extracted, reusable\\\\n  depends_on:\\\\n  - D016\\\\n  - D015\\\\n- id: D018\\\\n  date: 2026-05-15 19:20 UTC\\\\n  summary: G3-GC FAIL 确认为维度混淆方法论问题，启动 PCA-1024 + linear probe 控制实验\\\\n  rationale: Untrained VLA bin 0 = 100%（与 trained 相同），证伪 \\\\\\\"language grounding from\\\\n    training\\\\\\\" 原 claim。根因是 4096-dim MLP probe 对 10 类分类 capacity 过大（Hewitt & Manning\\\\n    2019）。需要 PCA 降维到 1024（与 DINO 对齐）+ linear probe 消除维度和 probe complexity 混淆后重新判定。暂定\\\\n    Option C framing（Methodology + Temporal Dynamics），最终取决于 PCA 结果。\\\\n  related_experiments:\\\\n  - exp_id: lg_gc_untrained\\\\n    role: trigger\\\\n    result: G3-GC FAIL, Δ(trained-untrained)=0pp\\\\n  depends_on: []\\\\n- id: D019\\\\n  date: 2026-05-15 19:44 UTC\\\\n  summary: Goal classification probing 方法论失败，pivot 到 Representational Similarity Analysis\\\\n    (RSA) 测试 training 是否改善 action-relevant 表征结构\\\\n  rationale: Goal classification 无法区分 trained vs untrained VLA（5 个实验变体全部 ~100%）。根因：两者都接收\\\\n    instruction text 作为输入，即使 random LLM 的高维投影也能完美分离 10 个不同文本的 goal。这不是维度/probe 选择问题，而是任务设计根本缺陷——测的是\\\\\\\"表征是否包含\\\\n    instruction 信息\\\\\\\"（trivially yes），而非\\\\\\\"training 是否改善 instruction encoding\\\\\\\"。DINO 低(35%→97%)是因为没有\\\\n    instruction 输入，不是 language grounding 差异。下一步用 RSA 测量 representation space 与 action\\\\n    space 的结构对齐程度，这避免了 trivial separability 问题。\\\\n  related_experiments:\\\\n  - exp_id: lg_gc_trained_frame0\\\\n    role: evidence\\\\n    result: trained 100% L3+\\\\n  - exp_id: lg_gc_untrained\\\\n    role: evidence\\\\n    result: untrained also 100%\\\\n  - exp_id: lg_pca1024_linear_pertimestep\\\\n    role: evidence\\\\n    result: 'PCA-1024 linear: trained 99.9% vs untrained 100%'\\\\n  depends_on:\\\\n  - D018\\\\n  - D015\\\\n- id: D020\\\\n  date: 2026-05-15 19:51 UTC\\\\n  summary: 'D020: RSA success gates 定义 + 要求在 LIBERO-Goal 上优先运行（cross-goal same-scene\\\\n    RDM），kill dead-end GPU 进程'\\\\n  rationale: 'Reviewer WARNING: RSA 启动无 gate 定义，重复 D001-D014 教训。补定 gates：G1 trained\\\\n    best-layer RSA ρ(repr RDM, action RDM) > 0.15；G2 Δρ(trained-untrained) > 0.08\\\\n    且 bootstrap 95% CI 排除 0；G3 trained ρ > DINO ρ（任何正 margin）。关键设计约束：LIBERO-Goal 的\\\\n    same-scene/different-goal 对是核心——DINO 在这些对上 visual RDM 高度相似但 action RDM 完全不同，预期\\\\n    RSA ρ 接近 0 或为负；trained VLA 应展示 goal-conditioned action structure，ρ 应显著高于 untrained\\\\n    和 DINO。同时 Reviewer 发现 GPU 上仍有两个已关闭路线的进程（PID 650060, 648231），应 kill 释放资源。'\\\\n  related_experiments:\\\\n  - exp_id: lg_rsa_analysis\\\\n    role: primary\\\\n    result: running, gates now defined\\\\n  - exp_id: lg_gc_untrained\\\\n    role: predecessor\\\\n    result: goal classification dead\\\\n  - exp_id: lg_pca1024_linear_pertimestep\\\\n    role: predecessor\\\\n    result: PCA+linear confirmed trivial separability\\\\n  depends_on:\\\\n  - D019\\\\n- id: D021\\\\n  date: 2026-05-15 20:08 UTC\\\\n  summary: 'D021: Framing pivot 到 Option B \\\\\\\"Architecture Trumps Training\\\\\\\"。5 轮 probing\\\\n    一致 G1+G3 PASS / G2 FAIL → VLA 架构提供 instruction conditioning，训练不改变表征结构。启动 instruction\\\\n    ablation + output head analysis 验证。'\\\\n  rationale: 6 轮实验（temporal distance, action prediction, action-delta, goal classification,\\\\n    RSA）× 2 benchmark（LIBERO-10, LIBERO-Goal）一致模式：trained ≈ untrained >> DINO。训练效应从未超过\\\\n    noise level（最大 Δρ=0.043）。三个 framing 备选中选 Option B 理由：(1) positive framing——\\\\\\\"架构设计驱动\\\\n    instruction conditioning\\\\\\\"比\\\\\\\"训练无用\\\\\\\"更 actionable；(2) 与 Grant 2026 互补（他们发现 behavioral\\\\n    \\\\\\\"encoded but not used\\\\\\\"，我们发现 representational \\\\\\\"not even encoded differently\\\\\\\"）；(3)\\\\n    只需 instruction ablation（1 个实验）验证机制——去掉 instruction 后 RSA 应 collapse，证明 architecture\\\\n    pathway 是关键；(4) output head analysis 补充解释行为改善如何在表征不变时发生（\\\\\\\"shallow adaptation\\\\\\\"）。Option\\\\n    C（random LLM sufficiency）作为 B 的自然推论在 Discussion 中讨论，不作为主 claim（需要 LLM size ablation，时间不够）。\\\\n  related_experiments:\\\\n  - exp_id: lg_rsa_analysis\\\\n    role: final confirming evidence\\\\n    result: G1 PASS ρ=0.49, G2 FAIL Δρ=0.003, G3 PASS Δ=0.10\\\\n  - exp_id: mvp_probe_trained\\\\n    role: temporal distance\\\\n    result: G2 FAIL Δρ=0.043\\\\n  - exp_id: mvp2_action_trained\\\\n    role: action prediction\\\\n    result: G2 FAIL ΔR²=0.067\\\\n  - exp_id: mvp2_action_dino\\\\n    role: action-delta baseline\\\\n    result: G3-delta FAIL, DINO ≈ trained\\\\n  - exp_id: lg_gc_untrained\\\\n    role: goal classification\\\\n    result: untrained 100% = trained\\\\n  depends_on:\\\\n  - D019\\\\n  - D020\\\\n  - D015\\\\n  - D014\\\\n- id: D022\\\\n  date: 2026-05-15 20:08 UTC\\\\n  summary: 'D021: RSA G2 FAIL (Δρ=0.003 << 0.08)。6 轮 probing 一致确认 VLA 训练不改变表征结构。Go/no-go\\\\n    决策点：推荐 Option A \\\\\\\"Representational Redundancy\\\\\\\" negative finding paper for CoRL'\\\\n  rationale: 6 轮系统性 probing（temporal distance / subtask / action prediction / action\\\\n    delta / goal classification / RSA）× 2 benchmarks（LIBERO-10 vision-sufficient +\\\\n    LIBERO-Goal vision-ambiguous）× 多种 probe（MLP/linear/PCA/RSA/CKA），全部呈现一致模式：G1 PASS（VLA\\\\n    表征编码 task-relevant 信息）、G2 FAIL（trained ≈ untrained，训练不改变表征内容）、G3 PASS（VLA >> DINO，架构提供\\\\n    instruction conditioning）。RSA 的 CKA 深层 0.85-0.86 进一步确认 trained-untrained 表征几何高度相似。原\\\\n    hypothesis \\\\\\\"VLA training contributes meaningful language grounding\\\\\\\" 被系统性否定。但 consistent\\\\n    negative + mechanistic insights (layer stability, temporal specialization) 本身构成有文献价值的发现——推翻\\\\n    VLA 领域 \\\\\\\"fine-tuning injects new representational knowledge\\\\\\\" 的隐性假设。三个 framing 备选：A)\\\\n    Representational Redundancy（最少额外实验）, B) Architecture Trumps Training（需 ablation）,\\\\n    C) Random LLM Sufficiency（需 LLM size ablation）。推荐 Option A：直接利用全部现有证据，仅需 output\\\\n    head analysis 补充 mechanism。\\\\n  related_experiments:\\\\n  - exp_id: lg_rsa_analysis\\\\n    role: final probe\\\\n    result: G1 PASS (ρ=0.488), G2 FAIL (Δ=0.003), G3 PASS (+0.10)\\\\n  - exp_id: mvp_probe_trained\\\\n    role: temporal distance\\\\n    result: Δρ=0.043\\\\n  - exp_id: mvp2_action_trained\\\\n    role: action prediction\\\\n    result: G3 FAIL, DINO ≈ trained\\\\n  - exp_id: lg_gc_untrained\\\\n    role: goal classification\\\\n    result: untrained 100% = trained 100%\\\\n  - exp_id: lg_pca1024_linear_pertimestep\\\\n    role: PCA+linear control\\\\n    result: Δ=-0.08pp\\\\n  depends_on:\\\\n  - D019\\\\n  - D020\\\\n  - D014\\\\n  - D013\\\\n- id: D023\\\\n  date: 2026-05-15 20:14 UTC\\\\n  summary: 'D023: Reviewer 共识——B framing 可行但 claim 需收窄为 \\\\\\\"instruction input pathway\\\\\\\"，instruction\\\\n    ablation 为 hard gate，FAIL 则回退 Option A'\\\\n  rationale: 两份独立 Reviewer 报告一致指出：(1) \\\\\\\"architecture\\\\\\\" 一词 overclaims——当前证据只证明 \\\\\\\"VLA pathway（含\\\\n    instruction 输入）>> 纯视觉\\\\\\\"，未 ablate 具体组件（text encoder / LLM backbone / fusion），应精确到\\\\n    \\\\\\\"instruction input pathway\\\\\\\"；(2) instruction ablation 是 blocking experiment，非 nice-to-have——没有它\\\\n    \\\\\\\"architecture provides instruction conditioning\\\\\\\" 是 speculation 不是 conclusion；(3)\\\\n    layer stability（31/33 vs 15/33）与 \\\\\\\"training doesn't change representation\\\\\\\" 存在内部张力，需定位为\\\\n    \\\\\\\"reorganization without new knowledge injection\\\\\\\"；(4) output head analysis 重要但非\\\\n    blocking（可放 Discussion）；(5) 最大 reviewer attack surface 是单 VLA 架构，scope 必须限定为 OpenVLA-class。采纳全部建议，设\\\\n    instruction ablation 为 hard gate：PASS 则锁定 B，FAIL 则立即回退 A。\\\\n  related_experiments:\\\\n  - exp_id: d021_instruction_ablation\\\\n    role: blocking_gate\\\\n    result: PREPARING\\\\n  - exp_id: d021_output_head_analysis\\\\n    role: supporting\\\\n    result: PREPARING\\\\n  depends_on:\\\\n  - D021\\\\n  - D022\\\\n- id: D024\\\\n  date: 2026-05-15 20:15 UTC\\\\n  summary: 'D023: Reviewer 评估 D021 framing — 接受 claim 精度建议，记录 attack surface 应对'\\\\n  rationale: Reviewer warning 级别评估 D021 \\\\\\\"Architecture Trumps Training\\\\\\\" framing。关键采纳：(1)\\\\n    claim 从 \\\\\\\"architecture\\\\\\\" 精确到 \\\\\\\"instruction input pathway\\\\\\\"；(2) instruction ablation\\\\n    是 critical path，FAIL 则切 Option A；(3) \\\\\\\"trivial separability\\\\\\\" 攻击需 random instruction\\\\n    control 回应（research 阶段第一优先）；(4) Grant checkpoint 差异 + 单 VLA 架构限制需在 Discussion/Limitations\\\\n    处理。不采纳：trivial separability 严重度被高估——RSA 测量 representation-action geometry correspondence\\\\n    而非分类，但 control 实验仍值得做。\\\\n  related_experiments:\\\\n  - exp_id: d021_instruction_ablation\\\\n    role: critical_path\\\\n    result: PREPARING\\\\n  - exp_id: d021_output_head_analysis\\\\n    role: supporting\\\\n    result: PREPARING\\\\n  depends_on:\\\\n  - D021\\\\n  - D022\\\\n- id: D025\\\\n  date: 2026-05-15 20:17 UTC\\\\n  summary: 'D024: Instruction ablation gate 从绝对阈值改为 DINO-anchored 相对标准'\\\\n  rationale: Reviewer 指出绝对阈值 0.30 缺乏锚定依据。改用 DINO RSA 作为锚点的相对标准：PASS 要求 no-instruction\\\\n    RSA 显著下降（Δ>0.10, CI 排除 0）且退化到 DINO 水平；FAIL 要求去掉 instruction 几乎无影响（Δ<0.05）；中间为\\\\n    INCONCLUSIVE。这避免了 \\\\\\\"RSA=0.38 接近 DINO 但按绝对阈值判 PASS\\\\\\\" 的假阳性。\\\\n  related_experiments:\\\\n  - exp_id: d021_instruction_ablation\\\\n    role: gate_definition\\\\n    result: PREPARING\\\\n  depends_on:\\\\n  - D023\\\\n- id: D026\\\\n  date: 2026-05-15 20:19 UTC\\\\n  summary: 'D025: Output head analysis FAIL — shallow adaptation 不成立，发现 projector\\\\n    bottleneck 机制'\\\\n  rationale: Head/LLM ratio = 1.12x (阈值 3x)，权重差异均匀分布于 LLM 32 层。但关键发现：SigLIP + Projector\\\\n    在 trained/untrained 间完全相同（rel_change=0, cos_sim=1.0），说明 untrained model 的 from_config()\\\\n    只重初始化 LLM。这提供了 trained≈untrained 的精确机制：frozen projector bottleneck 约束表征空间，使得下游\\\\n    LLM 权重（即使 cos_sim≈0.2 完全不同）无法改变表征结构。Shallow adaptation → Discussion 中 ruled-out\\\\n    hypothesis。Projector bottleneck → 替代机制解释。Caveat：当前比较是 pretrained+finetuned vs\\\\n    random init LLM，差异被 pretrained vs random 主导，但这恰恰是最强测试——如果极端不同的 LLM 都不影响表征，中间态更不会。\\\\n  related_experiments:\\\\n  - exp_id: d021_output_head_analysis\\\\n    role: primary\\\\n    result: FAIL_but_informative\\\\n  - exp_id: d021_instruction_ablation\\\\n    role: complementary\\\\n    result: RUNNING\\\\n  depends_on:\\\\n  - D024\\\\n- id: D027\\\\n  date: 2026-05-15 22:09 UTC\\\\n  summary: 'D027: Instruction Ablation FAIL — Option B 死亡，回退 Option A。选择 A2 \\\\\\\"Vision\\\\n    Encoder Dominance\\\\\\\" framing，SigLIP frozen encoder 是 action-relevant 表征的真正来源'\\\\n  rationale: 'Instruction ablation 结果：去掉 instruction text 后 untrained RSA ρ=0.4802\\\\n    vs with-inst ρ=0.4846，Δ=0.0044 远低于 0.10 阈值。no-inst RSA=0.48 远高于 DINO+0.05=0.438。Gate\\\\n    双 FAIL。Instruction pathway 不是 action-relevant 结构来源。\\\\n\\\\n\\\\n    综合全部证据链：(1) trained ≈ untrained（6 轮 probing 一致）；(2) VLA >> DINO（一致）；(3) instruction\\\\n    不影响 RSA（ablation 证实）；(4) SigLIP+projector frozen（output head analysis 证实）。唯一一致解释：SigLIP\\\\n    frozen vision encoder 决定了 action-relevant 表征结构。选 A2 framing 理由：指向具体组件，因果链清晰，与\\\\n    Grant 2026 互补（behavioral→representational），实用价值高（选 encoder 比 fine-tuning LLM 重要）。\\\\n\\\\n\\\\n    需补充 SigLIP-only features 提取 + RSA 作为 smoking gun 验证（不过 LLM 直接测 SigLIP 输出的 RSA），以及\\\\n    trained no-inst RSA 完成 2×2 matrix。两个实验完成 + positive → complete_mvp。'\\\\n  related_experiments:\\\\n  - exp_id: d021_instruction_ablation\\\\n    role: hard_gate\\\\n    result: 'FAIL: Δ=0.0044 << 0.10, no-inst RSA=0.48 >> DINO+0.05'\\\\n  - exp_id: d021_output_head_analysis\\\\n    role: supporting\\\\n    result: 'negative but informative: projector bottleneck mechanism'\\\\n  - exp_id: lg_rsa_analysis\\\\n    role: baseline\\\\n    result: 'with-inst RSA: trained 0.49, untrained 0.48, DINO 0.39'\\\\n  depends_on:\\\\n  - D023\\\\n  - D026\\\\n- id: D028\\\\n  date: 2026-05-15 22:26 UTC\\\\n  summary: 'D028: SigLIP-only RSA smoking gun PASS (0.615 >> 0.488)。LLM 是 degrader\\\\n    而非 passthrough。complete_mvp 批准，A2 framing 升级含 LLM degradation claim'\\\\n  rationale: 'SigLIP+Projector RSA = 0.615，远超 Gate 阈值 0.45-0.50，也远超 full VLA 的 0.488。证明\\\\n    action-relevant 表征结构完全来自 frozen vision encoder。\\\\n\\\\n\\\\n    意外发现：LLM 不是 passthrough 而是 degrader（0.615→0.488），无论 trained/untrained、with/without\\\\n    instruction。2×2 matrix 四格全部收敛于 0.48-0.49，Bootstrap CI 包含 0。Per-layer analysis\\\\n    确认 instruction 对任何层无实质影响（max |Δ|<0.015）。\\\\n\\\\n\\\\n    A2 framing 升级为三个 core claims：(1) action-relevant 表征源自 frozen SigLIP encoder；(2)\\\\n    LLM processing 降低 action-relevant 结构（degrader，非 passthrough/enhancer）；(3) training\\\\n    和 instruction 均不改变表征结构。Claim 2 是 novel contribution——无已有论文测量过 projector output\\\\n    vs LLM hidden state 的 RSA 差异。\\\\n\\\\n\\\\n    批准 complete_mvp，进入 research/writing 阶段。CoRL abstract DDL May 26（11天），paper DDL\\\\n    May 29（14天）。'\\\\n  related_experiments:\\\\n  - exp_id: d027_siglip_only_rsa\\\\n    role: smoking_gun\\\\n    result: 'PASS: RSA=0.615, far exceeding 0.45-0.50 gate and full VLA 0.488'\\\\n  - exp_id: d027_trained_no_inst_rsa\\\\n    role: 2x2_completion\\\\n    result: All 4 cells converge at 0.48-0.49, training x instruction both null\\\\n  - exp_id: d021_instruction_ablation\\\\n    role: per_layer_analysis\\\\n    result: max |delta|<0.015 across all layers\\\\n  depends_on:\\\\n  - D027\\\\n  - D023\\\\n- id: D029\\\\n  date: 2026-05-15 22:43 UTC\\\\n  summary: 'D029: Claim 2 聚合伪影排除。VLA image_mean RSA=0.501 仍远低于 SigLIP 0.615（gap=0.114），LLM\\\\n    degradation 是真实效应。Per-layer 分析显示降解集中在 Proj→L1 界面，中间层部分恢复'\\\\n  rationale: 'Reviewer CRITICAL 指出 SigLIP 用 mean pooling vs VLA 用 last_preaction 不公平。验证结果：改用完全相同的\\\\n    image_mean 聚合后，trained VLA RSA=0.5014（vs last_preaction 0.4876，差异仅 0.014），仍远低于\\\\n    SigLIP 0.6153。Gap=0.114，LLM degradation ~18.5%，排除聚合伪影。\\\\n\\\\n\\\\n    Per-layer degradation curve 补充 nuance：(1) 降解主要在 Proj→L1 界面（drop 0.13-0.25）；(2)\\\\n    3/4 条件非单调，中间层部分恢复；(3) no-inst trained 独特呈 L1→L30 持续上升。Claim 2 措辞应精炼为 \\\\\\\"LLM input\\\\n    interface introduces primary degradation; subsequent layers partially recover\\\\n    but net degradation persists (~18%)\\\\\\\"。\\\\n\\\\n\\\\n    论文应同时呈现 last_preaction 和 image_mean 两种聚合的 RSA 作为 robustness check。'\\\\n  related_experiments:\\\\n  - exp_id: d027_siglip_only_rsa\\\\n    role: reference\\\\n    result: RSA=0.6153 (mean pooling)\\\\n  - exp_id: plan_003_perlayer_degradation\\\\n    role: supplementary\\\\n    result: Proj→L1 drop 0.13-0.25, non-monotonic recovery\\\\n  - exp_id: d027_trained_no_inst_rsa\\\\n    role: aggregation_check\\\\n    result: 'image_mean RSA: trained 0.5014, untrained 0.4847'\\\\n  depends_on:\\\\n  - D028\\\\n- id: D030\\\\n  date: 2026-05-15 23:20 UTC\\\\n  summary: 'D030: Dream 三档均低于 acceptance（best borderline reject, median 5/10, worst\\\\n    4/10）。6 个结构性问题识别，P0 行动：functional validation via projector-output action probe'\\\\n  rationale: 'Dream 审稿三档一致指出 6 个结构性问题：(1) 无功能验证——RSA geometric alignment 不等于 task\\\\n    performance，是论文最大弱点；(2) 单架构 claim 过广；(3) confirmatory of concurrent behavioral\\\\n    work；(4) related work 严重不足；(5) LIBERO-only；(6) degradation framing 争议。\\\\n\\\\n\\\\n    P0 行动——functional validation 实验：在 projector output features 上训练 linear action\\\\n    predictor，对比 best LLM layer（已有 R²=0.683 from MVP-2）和 DINO（R²=0.676）。如果 projector\\\\n    R² ≥ LLM best → \\\\\\\"degradation is functional\\\\\\\" 从 correlational 升级为 causal evidence，彻底回应\\\\n    D1+D6。Features 已提取，probe 代码可复用，CPU/minimal GPU，~1h。\\\\n\\\\n\\\\n    P1 行动——scope claims to OpenVLA, 提升 trained≈untrained 为核心 novelty, 扩充 related work,\\\\n    加 figures。\\\\n\\\\n\\\\n    framing + plan 改动后必须 re-dream 验证。'\\\\n  related_experiments:\\\\n  - exp_id: d027_siglip_only_rsa\\\\n    role: features_source\\\\n    result: projector output features available for action probe\\\\n  - exp_id: mvp2_action_trained\\\\n    role: comparison\\\\n    result: LLM best layer R²=0.683\\\\n  - exp_id: mvp2_action_dino\\\\n    role: comparison\\\\n    result: DINO R²=0.676\\\\n  depends_on:\\\\n  - D028\\\\n  - D029\\\\n- id: D031\\\\n  date: 2026-05-15 23:43 UTC\\\\n  summary: 'Claim 2 framing pivot: \\\\\\\"LLM degrades\\\\\\\" → \\\\\\\"LLM redistributes\\\\\\\" — functional\\\\n    probe reveals LLM degrades image tokens (0.706→0.683) but concentrates action\\\\n    signal to readout token (0.731)'\\\\n  rationale: plan_011 functional validation 揭示了比 RSA 更丰富的图景：(1) Projector R²=0.706\\\\n    > LLM image_mean 0.683 确认 image token 级别的功能性降解；(2) 但 LLM last_preaction 0.731\\\\n    > Projector 0.706（bootstrap p=0.001），说明 LLM 的 attention 机制将分散的 action 信号聚合到 readout\\\\n    token。新 framing \\\\\\\"redistribution\\\\\\\" 比 \\\\\\\"degradation\\\\\\\" 更准确、更 interesting、且直接回应 Dream\\\\n    审稿 W3 concern（\\\\\\\"degradation framing interpretively problematic\\\\\\\"）。Core insight 不变：vision\\\\n    encoder 是 action information 的源头，LLM 的贡献是 readout/concentration 而非 new information\\\\n    injection。\\\\n  related_experiments:\\\\n  - exp_id: p0_functional_action_probe\\\\n    role: primary\\\\n    result: Projector R²=0.706 > LLM image_mean 0.683, but LLM last_preaction 0.731\\\\n      > Projector. PASS with nuance.\\\\n  depends_on:\\\\n  - D030\\\\n- id: D032\\\\n  date: 2026-05-15 23:47 UTC\\\\n  summary: Confirm Option A framing (\\\\\\\"LLM routes, not creates\\\\\\\"); functional probe\\\\n    needs re-run with bootstrap CI for main comparison + DINO probe\\\\n  rationale: 'Reviewer CRITICAL: (1) projector vs image_mean_trained (0.706 vs 0.683)\\\\n    缺 bootstrap CI，当前 PASS 无统计检验支撑；(2) DINO probe 未包含，缺三方对比。Delta probe BELOW 但 CI\\\\n    含 0。Agent 提出三个 framing option，选 A（\\\\\\\"96.6% functional capacity already in projector,\\\\n    LLM contributes routing not knowledge\\\\\\\"）——最平衡，保持 redistribution 叙事同时 defensible。修正后重跑是\\\\n    re-dream 前置条件。'\\\\n  related_experiments:\\\\n  - exp_id: p0_functional_action_probe\\\\n    role: primary\\\\n    result: 'PASS pending stat verification: proj 0.706 vs LLM img_mean 0.683 (CI\\\\n      needed), readout 0.731 (p=0.001)'\\\\n  - exp_id: p0_functional_action_delta_probe\\\\n    role: secondary\\\\n    result: 'BELOW: proj 0.118 < LLM 0.122, CI includes 0, not significant'\\\\n  depends_on:\\\\n  - D031\\\\n- id: D033\\\\n  date: 2026-05-15 23:54 UTC\\\\n  summary: 'DINO R²=0.712 ≈ Projector R²=0.706 (p=0.22) — Claim 1 reframe: geometric-functional\\\\n    dissociation. SigLIP advantage is geometric alignment (RSA), not predictive content\\\\n    (R²)'\\\\n  rationale: V2 probe 发现 DINO functional R²=0.712，与 SigLIP projector 0.706 无显著差异（p=0.22）。但\\\\n    RSA 维度 SigLIP (0.615) >> DINO (0.388)。这意味着：(1) action-relevant 信息在视觉编码器中是 ubiquitous\\\\n    的，不是 VL pretraining 独有；(2) VL pretraining 的价值在于 geometric organization（让表征几何结构与\\\\n    action 结构对齐），而非增加 predictive content。这个 geometric-functional dissociation 本身是一个新颖发现，可以强化论文。Claim\\\\n    1 从 \\\\\\\"SigLIP dominance\\\\\\\" 调整为 \\\\\\\"vision encoders universally contain action info +\\\\n    VL pretraining provides geometric alignment\\\\\\\"。旧 DINO 数字 0.676（MVP-2）已过时，V2 的 0.712\\\\n    是同一框架内的可信数字。仍需补 untrained last_preaction (C001) 和调查 MVP-2 vs V2 差异。\\\\n  related_experiments:\\\\n  - exp_id: p0_functional_probe_v2\\\\n    role: primary\\\\n    result: 'DINO CLS R²=0.712, Projector R²=0.706, p=0.22 NS. Bootstrap projector\\\\n      vs img_mean: delta=+0.023, CI=[0.011, 0.037], p<0.001 confirmed.'\\\\n  depends_on:\\\\n  - D031\\\\n  - D032\\\\n- id: D034\\\\n  date: 2026-05-16 00:07 UTC\\\\n  summary: 'Untrained last_preaction R²=0.689 < projector 0.706: redistribution is\\\\n    training-dependent. Claim 2 add qualifier, Claim 3 split by aggregation'\\\\n  rationale: C001 untrained 对照完成。Untrained readout best (L1, 0.689) < projector (0.706)\\\\n    < trained readout (L19, 0.731)。这意味着：(1) LLM 的 readout concentration 不是架构固有属性，需要训练才能超过\\\\n    projector baseline；(2) Claim 3 (training invariance) 在 image_mean 维度成立（distributed\\\\n    representation invariant）但在 last_preaction 维度不成立（readout concentration training-dependent）。综合\\\\n    story：VLA training 的贡献不是注入新的 action knowledge（image_mean invariant），而是学习将已有的 visual\\\\n    action information 高效路由到 output position（readout concentration learned）。这与 \\\\\\\"LLM\\\\n    routes, not creates\\\\\\\" (Option A) 完美一致，且比纯 \\\\\\\"training invariance\\\\\\\" 更有深度。需补 untrained\\\\n    vs trained last_preaction bootstrap CI 做统计确认。\\\\n  related_experiments:\\\\n  - exp_id: p0_functional_probe_v2\\\\n    role: primary\\\\n    result: Untrained last_preaction best L1 R²=0.689 < projector 0.706. L12-L18 +\\\\n      L24-L31 all collapsed to chance (0.059). Training-dependent redistribution confirmed.\\\\n  depends_on:\\\\n  - D031\\\\n  - D033\\\\n\\\", \\\"total_chars\\\": 33237, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/decisions.yaml\", \"content\": \"_next_id: 35\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 11:03 UTC\\n  summary: MVP 三分支判定标准校准：ρ下限0.3→0.5, Δρ加bootstrap CI, subtask gate加DINO baseline对比\\n  rationale: Reviewer 审查发现四项校准缺陷：(1) ρ>0.3 下限过低（DINO-V2 已达0.833，0.3只挡彻底失败）→ 提至0.5；(2)\\n    Δρ>0.1 仅为点估计缺统计检验 → 追加 bootstrapped 95% CI must exclude 0；(3) subtask_AUC>0.7\\n    无 baseline 锚点（不知道 DINO-V2 能做到多少）→ 增加条件 subtask_AUC > DINO_subtask_AUC + 0.05；(4)\\n    layer profile 不入正式判定但作为 mandatory supplementary analysis。修改后标准更严谨，降低 false positive\\n    PASS 风险。\\n  related_experiments:\\n  - exp_id: dino-v2-baseline\\n    role: baseline\\n    result: ρ=0.833\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP 判定全面切换到 per-task mean ρ，弃用 pooled ρ\\n  rationale: Reviewer 指出 pooled ρ 受 cross-task variance 膨胀（DINO pooled=0.833 vs per-task\\n    mean=0.554）。pooled-vs-pooled 虽对称但偏严（可能 false negative）。切换 per-task mean 与 task-level\\n    bootstrap CI 方法论一致，且是更公平的 apples-to-apples 比较。影响：VLA≥DINO gate 从 ρ≥0.833 变为 per-task\\n    mean≥0.554；ρ>0.5 下限同样改为 per-task mean。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: pooled ρ=0.833, per-task mean=0.554\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 12:31 UTC\\n  summary: 移除 subtask AUC gate，MVP 判定简化为纯 temporal distance (ρ) 路径\\n  rationale: DINO-V2 subtask AUC = 0.9717，Path B 要求 VLA > DINO + 0.05 = 1.0217，数学不可达（AUC\\n    上限 1.0）。根因：subtask 间视觉差异大，任何强视觉编码器都能高 AUC 区分——subtask discrimination 不是 VLA 的差异化能力。Temporal\\n    distance（连续进度信号）才是 VLA 可能独有的编码维度。简化后判定：PASS 需 VLA_ρ ≥ DINO_ρ (0.833)；CONDITIONAL\\n    需 Δρ > 0.1 但 VLA_ρ < DINO_ρ；FAIL 需 ρ ≤ 0.5 或 Δρ ≤ 0.1。Subtask AUC 保留为补充分析，不参与\\n    gate。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: trigger\\n    result: subtask AUC 0.9717 使 Path B 数学不可达\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 12:35 UTC\\n  summary: D003 勘误：DINO gate 阈值从 0.833 (pooled) 修正为 0.554 (per-task mean)，与 D002 对齐\\n  rationale: D003 写 ROADMAP 时误用 pooled ρ 0.833 作为 DINO gate 阈值，但 D002 已明确\\\"全面切换到 per-task\\n    mean ρ，弃用 pooled\\\"。DINO per-task mean ρ = 0.554。0.833 vs 0.554 差 0.28，直接影响 PASS/FAIL\\n    判定——用 0.833 会错误地将本应 PASS 的结果判为 CONDITIONAL。修正后所有文档/代码统一使用 per-task mean。同时确认 analyze_mvp.py\\n    废弃决策不变（urgent 指令已发）。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: reference\\n    result: pooled ρ=0.833, per-task mean ρ=0.554\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-15 13:31 UTC\\n  summary: D004 DINO gate 阈值作废：0.554→0.901。旧值基于 500 pairs/task 的噪声结果，新管道 5000 pairs/task\\n    下 DINO per-task mean ρ=0.9008\\n  rationale: 'Reviewer CRITICAL: 新管道 rerun DINO-V2 基线，per-task mean ρ 从 0.554 暴涨至\\n    0.901（10x 采样密度消除噪声）。旧管道 pooled/per-task 差异(0.833/0.554)是采样伪影。Gate 3 阈值必须更新为 0.901，否则\\n    analyze_results.py 判定标准错误。dinov2_baseline registry metrics 标为 invalidated。'\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: 旧 metrics invalidated; rerun per-task mean ρ=0.9008\\n  - exp_id: mvp_probe_trained\\n    role: primary\\n    result: layers 1-5 ρ≈0.950\\n  - exp_id: mvp_probe_untrained\\n    role: control\\n    result: layers 1-5 ρ≈0.925, Δρ max 0.043\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 13:32 UTC\\n  summary: 'DINO baseline invalidated: 旧管道 ρ=0.554 作废，新管道 ρ=0.901。Gate 3 阈值更新为 0.901。Gate\\n    2 预判高风险（layers 1-5 max Δρ=0.043 << 0.1）'\\n  rationale: Worker 用更新后的 train_probes.py 重跑 DINO baseline，per_task_n_pairs 从 500→5000，per-task\\n    mean ρ 从 0.554 暴涨至 0.901。旧结果系统性低估——所有 10 task 均在 0.84-0.93（旧值 0.41-0.68）。D001-D004\\n    的判定标准建立在错误基线上。同时 trained(ρ≈0.95) vs untrained(ρ≈0.93) vs DINO(ρ≈0.90) 三者差距极小，temporal\\n    distance 信号主要来自 vision encoder 而非 LLM 训练。等待 33 层全结果确认。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: invalidated baseline\\n    result: 旧 ρ=0.554 作废，新 ρ=0.901\\n  - exp_id: mvp_probe_trained\\n    role: running probe\\n    result: layers 1-5 mean ρ≈0.95\\n  - exp_id: mvp_probe_untrained\\n    role: running control\\n    result: layers 1-5 mean ρ≈0.93, Δρ<0.05\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-15 13:49 UTC\\n  summary: MVP Gate 2 FAIL 确认：33 层全结果，非坍塌层最大 Δρ=0.043 << 0.1。Temporal distance 信号来自\\n    vision encoder 而非 VLA 训练。Pivot 到 subtask predicate probe + 实用 pipeline 双线验证\\n  rationale: '完整 33 层数据：trained best ρ=0.956(L3), untrained best ρ=0.933(L1), DINO\\n    ρ=0.901。非坍塌层 Δρ 范围 0.003-0.043，无任何层接近 0.1 阈值。Gate 1 PASS(ρ>>0.5), Gate 2 FAIL(Δρ<<0.1),\\n    Gate 3 PASS(0.956>0.901)。科学结论：temporal distance 信号主要来自 SigLIP vision encoder，LLM\\n    fine-tuning 贡献 ~2-4% ρ，统计显著但实质极小。\\n\\n\\n    Pivot 理由：temporal distance 与 visual change 高度相关，vision encoder 天然擅长，不是测试 VLA 训练贡献的好\\n    probe。IDEA_BRIEF 原计划包含 subtask predicate classification（is_grasped, is_on_table\\n    等离散语义属性），这类信号需要理解 action 语义而非视觉相似度，vision encoder 不应有优势。先快速验证 subtask probe 是否展示\\n    VLA-specific 贡献，同时推进实用 pipeline（VLA ρ=0.95 已足够强，不管信号来源，self-scoring 可行）。'\\n  related_experiments:\\n  - exp_id: mvp_probe_trained\\n    role: primary probe\\n    result: best L3 ρ=0.956, 33 layers complete\\n  - exp_id: mvp_probe_untrained\\n    role: control C\\n    result: best L1 ρ=0.933, Δρ max=0.043\\n  - exp_id: dinov2_baseline\\n    role: baseline (rerun)\\n    result: ρ=0.901\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 13:58 UTC\\n  summary: MVP Gate 2 确认 FAIL（clean verdict）。Subtask predicate probe 是最后一道 VLA-specific\\n    signal 测试，48h 内出 CoRL go/no-go。\\n  rationale: P0 修复后 33 层全量结果：非坍塌层 max Δρ=0.043 << 0.1，CI [0.036, 0.050] 排除零但效应量不足。根因：temporal\\n    distance ≈ visual change，SigLIP 天然擅长（untrained ρ=0.933）。Subtask predicate probe（BDDL\\n    predicates）测试 VLA 是否编码离散 action-semantic 属性，但 DINO auto-extracted subtask AUC=0.97\\n    构成高 baseline 风险。设 48h 决策窗口：subtask probe 结果 + Control B 完成后做 CoRL go/no-go。\\n  related_experiments:\\n  - exp_id: mvp_probe_trained\\n    role: primary\\n    result: 'negative: Δρ=0.043'\\n  - exp_id: mvp_probe_untrained\\n    role: control\\n    result: 'success: ρ=0.933 baseline'\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: 'success: ρ=0.901'\\n  - exp_id: mvp_controlb_trained\\n    role: control\\n    result: running\\n  - exp_id: mvp_controlb_untrained\\n    role: control\\n    result: running\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-15 14:04 UTC\\n  summary: Subtask predicate pivot 终止。DINO auto-extracted subtask AUC=0.9717 > 0.95\\n    gate，所有 BDDL predicates 视觉可辨，VLA 训练无独特优势。转向 action prediction probe 调研。\\n  rationale: LIBERO tabletop 场景中 is_grasped/is_on_table/is_in_drawer 等 predicates\\n    在第三人称+手腕相机下视觉可辨，纯视觉模型即可高精度分类。根本问题：需要\\\"视觉不可达\\\"的 probing task 才能体现 VLA LLM 训练的独特贡献。Action\\n    prediction（预测 next action）需要策略知识，vision encoder 天然不擅长，是最有潜力的候选方向。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: evidence\\n    result: DINO subtask AUC=0.9717\\n  - exp_id: mvp_probe_trained\\n    role: context\\n    result: Δρ=0.043 insufficient\\n  - exp_id: mvp_probe_untrained\\n    role: context\\n    result: untrained ρ=0.933 vision-dominated\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 14:09 UTC\\n  summary: 批准 Action Prediction Probe 作为 MVP-2 方向。设定三门判定：G1 R²>0.3, G2 ΔR²(trained-untrained)>0.15,\\n    G3 ΔR²(trained-DINO)>0.15\\n  rationale: Temporal distance (D007) 和 subtask predicate (D009) 均因\\\"视觉可辨\\\"失败。Action\\n    prediction 需策略知识，vision encoder 不擅长，是区分 VLA 训练贡献的合理 probing task。数据现成（LIBERO HDF5\\n    自带 7-DoF action），特征可复用，运行快（~20min），低风险高信息量。\\n  related_experiments:\\n  - exp_id: mvp_probe_trained\\n    role: predecessor\\n    result: Δρ=0.043, temporal distance 视觉可辨\\n  - exp_id: mvp_probe_untrained\\n    role: predecessor\\n    result: baseline for G2 comparison\\n  - exp_id: dinov2_baseline\\n    role: predecessor\\n    result: ρ=0.901, 证明 temporal distance 视觉可辨\\n  - exp_id: mvp_controlb_trained\\n    role: running\\n    result: label permutation control\\n  - exp_id: mvp_controlb_untrained\\n    role: running\\n    result: label permutation control\\n  depends_on:\\n  - D009\\n  - D007\\n- id: D011\\n  date: 2026-05-15 14:14 UTC\\n  summary: Control B 两组实验均确认 null hypothesis（shuffled labels ρ≈0），probe 方法论完全验证。关闭\\n    MVP 实验系列。\\n  rationale: 'Trained features + shuffled labels: 33 层全部 |ρ|<0.013，信噪比 73:1。Untrained\\n    features + shuffled labels: 33 层全部 |ρ|<0.01，信噪比 104:1。结合 DINO Control B (ρ=0.039,\\n    信噪比 23:1)，三模型均通过 null control。证明 temporal distance probe 观测到的 ρ=0.955/0.933/0.901\\n    是真实信号，非 probe 过拟合或数据泄漏。MVP 实验系列（mvp_001 到 Control B）全部完成，结论：temporal distance\\n    信号主要来自 vision encoder，VLA 训练贡献 Δρ=0.043（统计显著但实质不足）。'\\n  related_experiments:\\n  - exp_id: mvp_controlb_trained\\n    role: null control\\n    result: max |ρ|=0.013, PASS\\n  - exp_id: mvp_controlb_untrained\\n    role: null control\\n    result: max |ρ|=0.009, PASS\\n  - exp_id: mvp_probe_trained\\n    role: primary\\n    result: ρ=0.955, Δρ=0.043\\n  - exp_id: mvp_probe_untrained\\n    role: control C\\n    result: ρ=0.933\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: ρ=0.901\\n  depends_on:\\n  - D008\\n  - D010\\n- id: D012\\n  date: 2026-05-15 14:23 UTC\\n  summary: 'D012: Copy baseline R²=0.97 暴露 G1 阈值无效。增加 action-delta prediction 作为核心判定指标，修订\\n    MVP-2 gates。'\\n  rationale: Reviewer 发现 copy baseline（a_{t+1}=a_t）R²=0.97，根因是机器人轨迹平滑导致连续 action 自相关极高。原\\n    G1（R²>0.3）毫无区分力，G2 的 Δ 也可能被压缩——与 MVP-1 的 vision dominates 结构性同构。解决方案：预测 action-delta（Δa\\n    = a_{t+1} - a_t），copy baseline 对 Δa 的 R² 恒为 0，彻底消除自相关混淆。当前实验继续不中断，完成后用相同 features\\n    重新训练 probe 即可（分钟级）。修订 gates：G1 保留为 sanity check；新增 G1-delta（trained peak-layer\\n    R²(Δa)>0.05）和 G2-delta（Δ(trained-untrained) on Δa >0.03 且 ≥5/10 tasks 一致）。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: primary\\n    result: running\\n  - exp_id: mvp2_action_untrained\\n    role: control\\n    result: running\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-15 15:25 UTC\\n  summary: MVP-2 Action Prediction 综合判定：G3-delta FAIL（DINO 0.061 ≈ trained 0.059）。三条探测维度（temporal\\n    distance / action prediction / action-delta）均 vision-dominated。唯一 VLA-specific\\n    发现：layer stability（训练后表征通路稳定，untrained 中间层坍塌）。建议 pivot 到 LIBERO-Goal instruction-conditioned\\n    probing。\\n  rationale: MVP-2 完整结果：G1 PASS (0.683>0.3), G1-delta borderline PASS (0.059>0.05),\\n    G2 FAIL (best-vs-best Δ=0.067<0.15), G3-action FAIL (Δ=0.007), G3-delta FAIL (DINO\\n    0.061 ≥ trained 0.059)。G2-delta Agent 报 PASS 但存在 best-vs-best vs same-layer 口径差异需核实。核心问题：DINO\\n    单层（1024 dim）在 action 和 action-delta 上均匹配 trained VLA 33 层最优（4096 dim），说明 LIBERO-10\\n    中的 action 信号（包括高阶 delta）可从视觉状态推断。VLA 训练的唯一可探测效果是 layer stability——表征通路畅通（trained\\n    31/33 层 R²>0.45, untrained 仅 ~15/33 层有效），但内容质量（可预测的信息量）未超越纯视觉。这与 Grant et al.\\n    2026 的发现一致：LIBERO-10 是 vision-solvable benchmark，language 几乎被忽略。LIBERO-Goal（多目标共享视觉场景）是文献支撑最强的下一步——该场景中\\n    vision 无法区分 goal，必须依赖 instruction。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: primary\\n    result: action R²=0.683(L19), delta R²=0.059(L14)\\n  - exp_id: mvp2_action_untrained\\n    role: control\\n    result: action R²=0.616(L32), delta R²=0.049(L32)\\n  - exp_id: mvp2_action_dino\\n    role: baseline\\n    result: action R²=0.676, delta R²=0.061 — matches trained VLA\\n  depends_on:\\n  - D012\\n  - D010\\n- id: D014\\n  date: 2026-05-15 15:26 UTC\\n  summary: MVP-2 判死：action prediction + action-delta 三轮 probing 一致确认 LIBERO-10 上 VLA\\n    训练未注入视觉编码器以外的独特信息。Pivot 到 LIBERO-Goal instruction-conditioned probing。\\n  rationale: 三轮 probing 结果一致：(1) temporal distance Δρ=0.043, (2) raw action ΔR²=0.067(T-U)/0.007(T-DINO),\\n    (3) action-delta ΔR²=0.012(T-U)/-0.001(T-DINO, DINO 反超)。DINO 单层 1024-dim 在所有指标上打平或超过\\n    trained VLA 33 层 4096-dim。根因：LIBERO-10 单目标 tabletop 场景视觉状态强烈约束 action 空间，无需语言或策略推理消歧。文献支撑\\n    pivot：Grant et al. 2026 发现 LIBERO-Goal 多目标场景中 language 贡献关键（正确 prompt 94% vs 错误\\n    10%）。唯一正面发现：VLA 训练创造了跨层稳定表征（trained 31/33 层 > untrained），但这是 representational\\n    reorganization 而非 new knowledge，单独不足以撑论文。Agent 报告的 G2-delta PASS 有误——best-vs-best\\n    Δ=0.012 < 0.03，0/10 tasks 超过阈值，实为 FAIL。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: primary\\n    result: best L19 R²=0.683, delta best L14 R²=0.060\\n  - exp_id: mvp2_action_untrained\\n    role: control\\n    result: best L32 R²=0.616, delta best L32 R²=0.048\\n  - exp_id: mvp2_action_dino\\n    role: baseline\\n    result: R²=0.676 action, R²=0.061 delta — matches or exceeds trained\\n  - exp_id: mvp_probe_trained\\n    role: predecessor\\n    result: temporal distance ρ=0.955, Δρ=0.043\\n  - exp_id: mvp_probe_untrained\\n    role: predecessor\\n    result: temporal distance ρ=0.933\\n  depends_on:\\n  - D012\\n  - D010\\n  - D007\\n- id: D015\\n  date: 2026-05-15 16:06 UTC\\n  summary: '选择 Option A: Pivot 到 LIBERO-Goal instruction-conditioned probing。Reviewer\\n    独立评估一致推荐，预期 CoRL 录用概率 15-30%（vs Option B 的 5-12%），且 worst case 退化为加强版 B。'\\n  rationale: Reviewer 独立评估结论：(1) Expected value 最高——LIBERO-Goal positive 时构成 \\\"vision-sufficient\\n    vs vision-ambiguous\\\" 对比叙事，FAIL 时退化为双 benchmark negative（仍优于纯 Option B）；(2) 实验成本极低（特征提取\\n    ~半天 GPU + probe 复用）；(3) Layer-wise mechanistic insight 是 vs Grant et al. 2026\\n    的差异化卖点——Grant 只做了 behavioral（input-output），我们提供 WHERE/HOW 的 representational 证据；(4)\\n    11 天内可行（7-9 天实际工作量）。关键风险：OpenVLA checkpoint 仅在 LIBERO-10 fine-tune，未见过 LIBERO-Goal\\n    多目标场景。缓解：先检查 scene overlap，必要时做 LIBERO-Goal fine-tune（+1 天）。用户授权：\\\"你们确定好怎么走我就同意\\\"。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: evidence\\n    result: action-delta R²=0.059, DINO ≈ trained, vision-dominated\\n  - exp_id: mvp2_action_dino\\n    role: evidence\\n    result: delta R²=0.061, matches trained VLA\\n  depends_on:\\n  - D013\\n- id: D016\\n  date: 2026-05-15 16:16 UTC\\n  summary: LIBERO-Goal 实验统一用 base pretrained OpenVLA checkpoint（非 LIBERO-10 fine-tuned）。同时用\\n    pretrained 重提 LIBERO-10 特征，确保跨 benchmark 对比公平——唯一变量是 benchmark，非 fine-tuning 状态。\\n  rationale: Reviewer 指出 checkpoint 不一致 confound：LIBERO-10 用 fine-tuned、LIBERO-Goal\\n    用 pretrained → reviewer 会攻击差异来自 fine-tuning 而非 benchmark 特性。Solution 1（base pretrained\\n    统一）最 clean：(1) 唯一变量是 benchmark，排除 fine-tuning confound；(2) 如果 pretrained VLA 已编码\\n    instruction grounding，novelty 更高（pretraining 产物 vs task-specific fine-tuning 产物）；(3)\\n    额外 GPU 成本仅 3h，当前 GPU 空闲正好利用；(4) 与 Grant et al. 差异化更清晰（Grant 用 OFT fine-tuned，我们用\\n    pretrained）。附带发现：Grant 的 100%→10% 效应来自 OpenVLA-OFT 而非 base，我们效应量可能小一些但更有说服力。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: predecessor (fine-tuned)\\n    result: R²=0.683, will re-extract with pretrained\\n  - exp_id: mvp2_action_dino\\n    role: baseline\\n    result: R²=0.676, unchanged\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-15 16:22 UTC\\n  summary: D016 修正：改用 LIBERO-10 fine-tuned checkpoint 统一提取两个 benchmark 特征（取代 base\\n    pretrained 方案）。LIBERO-Goal 是 OOD 测试——场景不重叠，positive 结果 = 泛化而非记忆。\\n  rationale: Reviewer 二次审视后提出更优方案：(1) fine-tuned checkpoint 在 LIBERO-Goal 上是 OOD——场景确认不重叠、指令未见过，positive\\n    结果直接证明 instruction grounding 泛化能力，story 更强；(2) LIBERO-10 特征已提取完毕无需重跑，省 3h GPU；(3)\\n    同一 checkpoint 跨两个 benchmark = 公平对比，唯一变量仍是 benchmark 特性；(4) base pretrained 可作为后续\\n    ablation 补充（如果 fine-tuned 结果 positive 且时间允许）。此决策取代 D016 的 base pretrained 方案。\\n  related_experiments:\\n  - exp_id: mvp2_action_trained\\n    role: existing features\\n    result: LIBERO-10 fine-tuned features already extracted, reusable\\n  depends_on:\\n  - D016\\n  - D015\\n- id: D018\\n  date: 2026-05-15 19:20 UTC\\n  summary: G3-GC FAIL 确认为维度混淆方法论问题，启动 PCA-1024 + linear probe 控制实验\\n  rationale: Untrained VLA bin 0 = 100%（与 trained 相同），证伪 \\\"language grounding from\\n    training\\\" 原 claim。根因是 4096-dim MLP probe 对 10 类分类 capacity 过大（Hewitt & Manning\\n    2019）。需要 PCA 降维到 1024（与 DINO 对齐）+ linear probe 消除维度和 probe complexity 混淆后重新判定。暂定\\n    Option C framing（Methodology + Temporal Dynamics），最终取决于 PCA 结果。\\n  related_experiments:\\n  - exp_id: lg_gc_untrained\\n    role: trigger\\n    result: G3-GC FAIL, Δ(trained-untrained)=0pp\\n  depends_on: []\\n- id: D019\\n  date: 2026-05-15 19:44 UTC\\n  summary: Goal classification probing 方法论失败，pivot 到 Representational Similarity Analysis\\n    (RSA) 测试 training 是否改善 action-relevant 表征结构\\n  rationale: Goal classification 无法区分 trained vs untrained VLA（5 个实验变体全部 ~100%）。根因：两者都接收\\n    instruction text 作为输入，即使 random LLM 的高维投影也能完美分离 10 个不同文本的 goal。这不是维度/probe 选择问题，而是任务设计根本缺陷——测的是\\\"表征是否包含\\n    instruction 信息\\\"（trivially yes），而非\\\"training 是否改善 instruction encoding\\\"。DINO 低(35%→97%)是因为没有\\n    instruction 输入，不是 language grounding 差异。下一步用 RSA 测量 representation space 与 action\\n    space 的结构对齐程度，这避免了 trivial separability 问题。\\n  related_experiments:\\n  - exp_id: lg_gc_trained_frame0\\n    role: evidence\\n    result: trained 100% L3+\\n  - exp_id: lg_gc_untrained\\n    role: evidence\\n    result: untrained also 100%\\n  - exp_id: lg_pca1024_linear_pertimestep\\n    role: evidence\\n    result: 'PCA-1024 linear: trained 99.9% vs untrained 100%'\\n  depends_on:\\n  - D018\\n  - D015\\n- id: D020\\n  date: 2026-05-15 19:51 UTC\\n  summary: 'D020: RSA success gates 定义 + 要求在 LIBERO-Goal 上优先运行（cross-goal same-scene\\n    RDM），kill dead-end GPU 进程'\\n  rationale: 'Reviewer WARNING: RSA 启动无 gate 定义，重复 D001-D014 教训。补定 gates：G1 trained\\n    best-layer RSA ρ(repr RDM, action RDM) > 0.15；G2 Δρ(trained-untrained) > 0.08\\n    且 bootstrap 95% CI 排除 0；G3 trained ρ > DINO ρ（任何正 margin）。关键设计约束：LIBERO-Goal 的\\n    same-scene/different-goal 对是核心——DINO 在这些对上 visual RDM 高度相似但 action RDM 完全不同，预期\\n    RSA ρ 接近 0 或为负；trained VLA 应展示 goal-conditioned action structure，ρ 应显著高于 untrained\\n    和 DINO。同时 Reviewer 发现 GPU 上仍有两个已关闭路线的进程（PID 650060, 648231），应 kill 释放资源。'\\n  related_experiments:\\n  - exp_id: lg_rsa_analysis\\n    role: primary\\n    result: running, gates now defined\\n  - exp_id: lg_gc_untrained\\n    role: predecessor\\n    result: goal classification dead\\n  - exp_id: lg_pca1024_linear_pertimestep\\n    role: predecessor\\n    result: PCA+linear confirmed trivial separability\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-15 20:08 UTC\\n  summary: 'D021: Framing pivot 到 Option B \\\"Architecture Trumps Training\\\"。5 轮 probing\\n    一致 G1+G3 PASS / G2 FAIL → VLA 架构提供 instruction conditioning，训练不改变表征结构。启动 instruction\\n    ablation + output head analysis 验证。'\\n  rationale: 6 轮实验（temporal distance, action prediction, action-delta, goal classification,\\n    RSA）× 2 benchmark（LIBERO-10, LIBERO-Goal）一致模式：trained ≈ untrained >> DINO。训练效应从未超过\\n    noise level（最大 Δρ=0.043）。三个 framing 备选中选 Option B 理由：(1) positive framing——\\\"架构设计驱动\\n    instruction conditioning\\\"比\\\"训练无用\\\"更 actionable；(2) 与 Grant 2026 互补（他们发现 behavioral\\n    \\\"encoded but not used\\\"，我们发现 representational \\\"not even encoded differently\\\"）；(3)\\n    只需 instruction ablation（1 个实验）验证机制——去掉 instruction 后 RSA 应 collapse，证明 architecture\\n    pathway 是关键；(4) output head analysis 补充解释行为改善如何在表征不变时发生（\\\"shallow adaptation\\\"）。Option\\n    C（random LLM sufficiency）作为 B 的自然推论在 Discussion 中讨论，不作为主 claim（需要 LLM size ablation，时间不够）。\\n  related_experiments:\\n  - exp_id: lg_rsa_analysis\\n    role: final confirming evidence\\n    result: G1 PASS ρ=0.49, G2 FAIL Δρ=0.003, G3 PASS Δ=0.10\\n  - exp_id: mvp_probe_trained\\n    role: temporal distance\\n    result: G2 FAIL Δρ=0.043\\n  - exp_id: mvp2_action_trained\\n    role: action prediction\\n    result: G2 FAIL ΔR²=0.067\\n  - exp_id: mvp2_action_dino\\n    role: action-delta baseline\\n    result: G3-delta FAIL, DINO ≈ trained\\n  - exp_id: lg_gc_untrained\\n    role: goal classification\\n    result: untrained 100% = trained\\n  depends_on:\\n  - D019\\n  - D020\\n  - D015\\n  - D014\\n- id: D022\\n  date: 2026-05-15 20:08 UTC\\n  summary: 'D021: RSA G2 FAIL (Δρ=0.003 << 0.08)。6 轮 probing 一致确认 VLA 训练不改变表征结构。Go/no-go\\n    决策点：推荐 Option A \\\"Representational Redundancy\\\" negative finding paper for CoRL'\\n  rationale: 6 轮系统性 probing（temporal distance / subtask / action prediction / action\\n    delta / goal classification / RSA）× 2 benchmarks（LIBERO-10 vision-sufficient +\\n    LIBERO-Goal vision-ambiguous）× 多种 probe（MLP/linear/PCA/RSA/CKA），全部呈现一致模式：G1 PASS（VLA\\n    表征编码 task-relevant 信息）、G2 FAIL（trained ≈ untrained，训练不改变表征内容）、G3 PASS（VLA >> DINO，架构提供\\n    instruction conditioning）。RSA 的 CKA 深层 0.85-0.86 进一步确认 trained-untrained 表征几何高度相似。原\\n    hypothesis \\\"VLA training contributes meaningful language grounding\\\" 被系统性否定。但 consistent\\n    negative + mechanistic insights (layer stability, temporal specialization) 本身构成有文献价值的发现——推翻\\n    VLA 领域 \\\"fine-tuning injects new representational knowledge\\\" 的隐性假设。三个 framing 备选：A)\\n    Representational Redundancy（最少额外实验）, B) Architecture Trumps Training（需 ablation）,\\n    C) Random LLM Sufficiency（需 LLM size ablation）。推荐 Option A：直接利用全部现有证据，仅需 output\\n    head analysis 补充 mechanism。\\n  related_experiments:\\n  - exp_id: lg_rsa_analysis\\n    role: final probe\\n    result: G1 PASS (ρ=0.488), G2 FAIL (Δ=0.003), G3 PASS (+0.10)\\n  - exp_id: mvp_probe_trained\\n    role: temporal distance\\n    result: Δρ=0.043\\n  - exp_id: mvp2_action_trained\\n    role: action prediction\\n    result: G3 FAIL, DINO ≈ trained\\n  - exp_id: lg_gc_untrained\\n    role: goal classification\\n    result: untrained 100% = trained 100%\\n  - exp_id: lg_pca1024_linear_pertimestep\\n    role: PCA+linear control\\n    result: Δ=-0.08pp\\n  depends_on:\\n  - D019\\n  - D020\\n  - D014\\n  - D013\\n- id: D023\\n  date: 2026-05-15 20:14 UTC\\n  summary: 'D023: Reviewer 共识——B framing 可行但 claim 需收窄为 \\\"instruction input pathway\\\"，instruction\\n    ablation 为 hard gate，FAIL 则回退 Option A'\\n  rationale: 两份独立 Reviewer 报告一致指出：(1) \\\"architecture\\\" 一词 overclaims——当前证据只证明 \\\"VLA pathway（含\\n    instruction 输入）>> 纯视觉\\\"，未 ablate 具体组件（text encoder / LLM backbone / fusion），应精确到\\n    \\\"instruction input pathway\\\"；(2) instruction ablation 是 blocking experiment，非 nice-to-have——没有它\\n    \\\"architecture provides instruction conditioning\\\" 是 speculation 不是 conclusion；(3)\\n    layer stability（31/33 vs 15/33）与 \\\"training doesn't change representation\\\" 存在内部张力，需定位为\\n    \\\"reorganization without new knowledge injection\\\"；(4) output head analysis 重要但非\\n    blocking（可放 Discussion）；(5) 最大 reviewer attack surface 是单 VLA 架构，scope 必须限定为 OpenVLA-class。采纳全部建议，设\\n    instruction ablation 为 hard gate：PASS 则锁定 B，FAIL 则立即回退 A。\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: blocking_gate\\n    result: PREPARING\\n  - exp_id: d021_output_head_analysis\\n    role: supporting\\n    result: PREPARING\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-15 20:15 UTC\\n  summary: 'D023: Reviewer 评估 D021 framing — 接受 claim 精度建议，记录 attack surface 应对'\\n  rationale: Reviewer warning 级别评估 D021 \\\"Architecture Trumps Training\\\" framing。关键采纳：(1)\\n    claim 从 \\\"architecture\\\" 精确到 \\\"instruction input pathway\\\"；(2) instruction ablation\\n    是 critical path，FAIL 则切 Option A；(3) \\\"trivial separability\\\" 攻击需 random instruction\\n    control 回应（research 阶段第一优先）；(4) Grant checkpoint 差异 + 单 VLA 架构限制需在 Discussion/Limitations\\n    处理。不采纳：trivial separability 严重度被高估——RSA 测量 representation-action geometry correspondence\\n    而非分类，但 control 实验仍值得做。\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: critical_path\\n    result: PREPARING\\n  - exp_id: d021_output_head_analysis\\n    role: supporting\\n    result: PREPARING\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D025\\n  date: 2026-05-15 20:17 UTC\\n  summary: 'D024: Instruction ablation gate 从绝对阈值改为 DINO-anchored 相对标准'\\n  rationale: Reviewer 指出绝对阈值 0.30 缺乏锚定依据。改用 DINO RSA 作为锚点的相对标准：PASS 要求 no-instruction\\n    RSA 显著下降（Δ>0.10, CI 排除 0）且退化到 DINO 水平；FAIL 要求去掉 instruction 几乎无影响（Δ<0.05）；中间为\\n    INCONCLUSIVE。这避免了 \\\"RSA=0.38 接近 DINO 但按绝对阈值判 PASS\\\" 的假阳性。\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: gate_definition\\n    result: PREPARING\\n  depends_on:\\n  - D023\\n- id: D026\\n  date: 2026-05-15 20:19 UTC\\n  summary: 'D025: Output head analysis FAIL — shallow adaptation 不成立，发现 projector\\n    bottleneck 机制'\\n  rationale: Head/LLM ratio = 1.12x (阈值 3x)，权重差异均匀分布于 LLM 32 层。但关键发现：SigLIP + Projector\\n    在 trained/untrained 间完全相同（rel_change=0, cos_sim=1.0），说明 untrained model 的 from_config()\\n    只重初始化 LLM。这提供了 trained≈untrained 的精确机制：frozen projector bottleneck 约束表征空间，使得下游\\n    LLM 权重（即使 cos_sim≈0.2 完全不同）无法改变表征结构。Shallow adaptation → Discussion 中 ruled-out\\n    hypothesis。Projector bottleneck → 替代机制解释。Caveat：当前比较是 pretrained+finetuned vs\\n    random init LLM，差异被 pretrained vs random 主导，但这恰恰是最强测试——如果极端不同的 LLM 都不影响表征，中间态更不会。\\n  related_experiments:\\n  - exp_id: d021_output_head_analysis\\n    role: primary\\n    result: FAIL_but_informative\\n  - exp_id: d021_instruction_ablation\\n    role: complementary\\n    result: RUNNING\\n  depends_on:\\n  - D024\\n- id: D027\\n  date: 2026-05-15 22:09 UTC\\n  summary: 'D027: Instruction Ablation FAIL — Option B 死亡，回退 Option A。选择 A2 \\\"Vision\\n    Encoder Dominance\\\" framing，SigLIP frozen encoder 是 action-relevant 表征的真正来源'\\n  rationale: 'Instruction ablation 结果：去掉 instruction text 后 untrained RSA ρ=0.4802\\n    vs with-inst ρ=0.4846，Δ=0.0044 远低于 0.10 阈值。no-inst RSA=0.48 远高于 DINO+0.05=0.438。Gate\\n    双 FAIL。Instruction pathway 不是 action-relevant 结构来源。\\n\\n\\n    综合全部证据链：(1) trained ≈ untrained（6 轮 probing 一致）；(2) VLA >> DINO（一致）；(3) instruction\\n    不影响 RSA（ablation 证实）；(4) SigLIP+projector frozen（output head analysis 证实）。唯一一致解释：SigLIP\\n    frozen vision encoder 决定了 action-relevant 表征结构。选 A2 framing 理由：指向具体组件，因果链清晰，与\\n    Grant 2026 互补（behavioral→representational），实用价值高（选 encoder 比 fine-tuning LLM 重要）。\\n\\n\\n    需补充 SigLIP-only features 提取 + RSA 作为 smoking gun 验证（不过 LLM 直接测 SigLIP 输出的 RSA），以及\\n    trained no-inst RSA 完成 2×2 matrix。两个实验完成 + positive → complete_mvp。'\\n  related_experiments:\\n  - exp_id: d021_instruction_ablation\\n    role: hard_gate\\n    result: 'FAIL: Δ=0.0044 << 0.10, no-inst RSA=0.48 >> DINO+0.05'\\n  - exp_id: d021_output_head_analysis\\n    role: supporting\\n    result: 'negative but informative: projector bottleneck mechanism'\\n  - exp_id: lg_rsa_analysis\\n    role: baseline\\n    result: 'with-inst RSA: trained 0.49, untrained 0.48, DINO 0.39'\\n  depends_on:\\n  - D023\\n  - D026\\n- id: D028\\n  date: 2026-05-15 22:26 UTC\\n  summary: 'D028: SigLIP-only RSA smoking gun PASS (0.615 >> 0.488)。LLM 是 degrader\\n    而非 passthrough。complete_mvp 批准，A2 framing 升级含 LLM degradation claim'\\n  rationale: 'SigLIP+Projector RSA = 0.615，远超 Gate 阈值 0.45-0.50，也远超 full VLA 的 0.488。证明\\n    action-relevant 表征结构完全来自 frozen vision encoder。\\n\\n\\n    意外发现：LLM 不是 passthrough 而是 degrader（0.615→0.488），无论 trained/untrained、with/without\\n    instruction。2×2 matrix 四格全部收敛于 0.48-0.49，Bootstrap CI 包含 0。Per-layer analysis\\n    确认 instruction 对任何层无实质影响（max |Δ|<0.015）。\\n\\n\\n    A2 framing 升级为三个 core claims：(1) action-relevant 表征源自 frozen SigLIP encoder；(2)\\n    LLM processing 降低 action-relevant 结构（degrader，非 passthrough/enhancer）；(3) training\\n    和 instruction 均不改变表征结构。Claim 2 是 novel contribution——无已有论文测量过 projector output\\n    vs LLM hidden state 的 RSA 差异。\\n\\n\\n    批准 complete_mvp，进入 research/writing 阶段。CoRL abstract DDL May 26（11天），paper DDL\\n    May 29（14天）。'\\n  related_experiments:\\n  - exp_id: d027_siglip_only_rsa\\n    role: smoking_gun\\n    result: 'PASS: RSA=0.615, far exceeding 0.45-0.50 gate and full VLA 0.488'\\n  - exp_id: d027_trained_no_inst_rsa\\n    role: 2x2_completion\\n    result: All 4 cells converge at 0.48-0.49, training x instruction both null\\n  - exp_id: d021_instruction_ablation\\n    role: per_layer_analysis\\n    result: max |delta|<0.015 across all layers\\n  depends_on:\\n  - D027\\n  - D023\\n- id: D029\\n  date: 2026-05-15 22:43 UTC\\n  summary: 'D029: Claim 2 聚合伪影排除。VLA image_mean RSA=0.501 仍远低于 SigLIP 0.615（gap=0.114），LLM\\n    degradation 是真实效应。Per-layer 分析显示降解集中在 Proj→L1 界面，中间层部分恢复'\\n  rationale: 'Reviewer CRITICAL 指出 SigLIP 用 mean pooling vs VLA 用 last_preaction 不公平。验证结果：改用完全相同的\\n    image_mean 聚合后，trained VLA RSA=0.5014（vs last_preaction 0.4876，差异仅 0.014），仍远低于\\n    SigLIP 0.6153。Gap=0.114，LLM degradation ~18.5%，排除聚合伪影。\\n\\n\\n    Per-layer degradation curve 补充 nuance：(1) 降解主要在 Proj→L1 界面（drop 0.13-0.25）；(2)\\n    3/4 条件非单调，中间层部分恢复；(3) no-inst trained 独特呈 L1→L30 持续上升。Claim 2 措辞应精炼为 \\\"LLM input\\n    interface introduces primary degradation; subsequent layers partially recover\\n    but net degradation persists (~18%)\\\"。\\n\\n\\n    论文应同时呈现 last_preaction 和 image_mean 两种聚合的 RSA 作为 robustness check。'\\n  related_experiments:\\n  - exp_id: d027_siglip_only_rsa\\n    role: reference\\n    result: RSA=0.6153 (mean pooling)\\n  - exp_id: plan_003_perlayer_degradation\\n    role: supplementary\\n    result: Proj→L1 drop 0.13-0.25, non-monotonic recovery\\n  - exp_id: d027_trained_no_inst_rsa\\n    role: aggregation_check\\n    result: 'image_mean RSA: trained 0.5014, untrained 0.4847'\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-15 23:20 UTC\\n  summary: 'D030: Dream 三档均低于 acceptance（best borderline reject, median 5/10, worst\\n    4/10）。6 个结构性问题识别，P0 行动：functional validation via projector-output action probe'\\n  rationale: 'Dream 审稿三档一致指出 6 个结构性问题：(1) 无功能验证——RSA geometric alignment 不等于 task\\n    performance，是论文最大弱点；(2) 单架构 claim 过广；(3) confirmatory of concurrent behavioral\\n    work；(4) related work 严重不足；(5) LIBERO-only；(6) degradation framing 争议。\\n\\n\\n    P0 行动——functional validation 实验：在 projector output features 上训练 linear action\\n    predictor，对比 best LLM layer（已有 R²=0.683 from MVP-2）和 DINO（R²=0.676）。如果 projector\\n    R² ≥ LLM best → \\\"degradation is functional\\\" 从 correlational 升级为 causal evidence，彻底回应\\n    D1+D6。Features 已提取，probe 代码可复用，CPU/minimal GPU，~1h。\\n\\n\\n    P1 行动——scope claims to OpenVLA, 提升 trained≈untrained 为核心 novelty, 扩充 related work,\\n    加 figures。\\n\\n\\n    framing + plan 改动后必须 re-dream 验证。'\\n  related_experiments:\\n  - exp_id: d027_siglip_only_rsa\\n    role: features_source\\n    result: projector output features available for action probe\\n  - exp_id: mvp2_action_trained\\n    role: comparison\\n    result: LLM best layer R²=0.683\\n  - exp_id: mvp2_action_dino\\n    role: comparison\\n    result: DINO R²=0.676\\n  depends_on:\\n  - D028\\n  - D029\\n- id: D031\\n  date: 2026-05-15 23:43 UTC\\n  summary: 'Claim 2 framing pivot: \\\"LLM degrades\\\" → \\\"LLM redistributes\\\" — functional\\n    probe reveals LLM degrades image tokens (0.706→0.683) but concentrates action\\n    signal to readout token (0.731)'\\n  rationale: plan_011 functional validation 揭示了比 RSA 更丰富的图景：(1) Projector R²=0.706\\n    > LLM image_mean 0.683 确认 image token 级别的功能性降解；(2) 但 LLM last_preaction 0.731\\n    > Projector 0.706（bootstrap p=0.001），说明 LLM 的 attention 机制将分散的 action 信号聚合到 readout\\n    token。新 framing \\\"redistribution\\\" 比 \\\"degradation\\\" 更准确、更 interesting、且直接回应 Dream\\n    审稿 W3 concern（\\\"degradation framing interpretively problematic\\\"）。Core insight 不变：vision\\n    encoder 是 action information 的源头，LLM 的贡献是 readout/concentration 而非 new information\\n    injection。\\n  related_experiments:\\n  - exp_id: p0_functional_action_probe\\n    role: primary\\n    result: Projector R²=0.706 > LLM image_mean 0.683, but LLM last_preaction 0.731\\n      > Projector. PASS with nuance.\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-15 23:47 UTC\\n  summary: Confirm Option A framing (\\\"LLM routes, not creates\\\"); functional probe\\n    needs re-run with bootstrap CI for main comparison + DINO probe\\n  rationale: 'Reviewer CRITICAL: (1) projector vs image_mean_trained (0.706 vs 0.683)\\n    缺 bootstrap CI，当前 PASS 无统计检验支撑；(2) DINO probe 未包含，缺三方对比。Delta probe BELOW 但 CI\\n    含 0。Agent 提出三个 framing option，选 A（\\\"96.6% functional capacity already in projector,\\n    LLM contributes routing not knowledge\\\"）——最平衡，保持 redistribution 叙事同时 defensible。修正后重跑是\\n    re-dream 前置条件。'\\n  related_experiments:\\n  - exp_id: p0_functional_action_probe\\n    role: primary\\n    result: 'PASS pending stat verification: proj 0.706 vs LLM img_mean 0.683 (CI\\n      needed), readout 0.731 (p=0.001)'\\n  - exp_id: p0_functional_action_delta_probe\\n    role: secondary\\n    result: 'BELOW: proj 0.118 < LLM 0.122, CI includes 0, not significant'\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 23:54 UTC\\n  summary: 'DINO R²=0.712 ≈ Projector R²=0.706 (p=0.22) — Claim 1 reframe: geometric-functional\\n    dissociation. SigLIP advantage is geometric alignment (RSA), not predictive content\\n    (R²)'\\n  rationale: V2 probe 发现 DINO functional R²=0.712，与 SigLIP projector 0.706 无显著差异（p=0.22）。但\\n    RSA 维度 SigLIP (0.615) >> DINO (0.388)。这意味着：(1) action-relevant 信息在视觉编码器中是 ubiquitous\\n    的，不是 VL pretraining 独有；(2) VL pretraining 的价值在于 geometric organization（让表征几何结构与\\n    action 结构对齐），而非增加 predictive content。这个 geometric-functional dissociation 本身是一个新颖发现，可以强化论文。Claim\\n    1 从 \\\"SigLIP dominance\\\" 调整为 \\\"vision encoders universally contain action info +\\n    VL pretraining provides geometric alignment\\\"。旧 DINO 数字 0.676（MVP-2）已过时，V2 的 0.712\\n    是同一框架内的可信数字。仍需补 untrained last_preaction (C001) 和调查 MVP-2 vs V2 差异。\\n  related_experiments:\\n  - exp_id: p0_functional_probe_v2\\n    role: primary\\n    result: 'DINO CLS R²=0.712, Projector R²=0.706, p=0.22 NS. Bootstrap projector\\n      vs img_mean: delta=+0.023, CI=[0.011, 0.037], p<0.001 confirmed.'\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-16 00:07 UTC\\n  summary: 'Untrained last_preaction R²=0.689 < projector 0.706: redistribution is\\n    training-dependent. Claim 2 add qualifier, Claim 3 split by aggregation'\\n  rationale: C001 untrained 对照完成。Untrained readout best (L1, 0.689) < projector (0.706)\\n    < trained readout (L19, 0.731)。这意味着：(1) LLM 的 readout concentration 不是架构固有属性，需要训练才能超过\\n    projector baseline；(2) Claim 3 (training invariance) 在 image_mean 维度成立（distributed\\n    representation invariant）但在 last_preaction 维度不成立（readout concentration training-dependent）。综合\\n    story：VLA training 的贡献不是注入新的 action knowledge（image_mean invariant），而是学习将已有的 visual\\n    action information 高效路由到 output position（readout concentration learned）。这与 \\\"LLM\\n    routes, not creates\\\" (Option A) 完美一致，且比纯 \\\"training invariance\\\" 更有深度。需补 untrained\\n    vs trained last_preaction bootstrap CI 做统计确认。\\n  related_experiments:\\n  - exp_id: p0_functional_probe_v2\\n    role: primary\\n    result: Untrained last_preaction best L1 R²=0.689 < projector 0.706. L12-L18 +\\n      L24-L31 all collapsed to chance (0.059). Training-dependent redistribution confirmed.\\n  depends_on:\\n  - D031\\n  - D033\\n\", \"total_chars\": 33237, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to draft a comprehensive writing_plan.yaml. Let me synthesize everything from:

1. paper_framing.md - Core claims, evidence, literature positioning
2. memory.md - Key findings and technical details
3. ROADMAP.md - Experiment status and timeline
4. decisions.yaml - Full experiment history and IDs

Let me draft the writing_plan.yaml now.

Key experiments and their IDs:
- d027_siglip_only_rsa: SigLIP+Projector RSA=0.615 (smoking gun)


- lg_rsa_analysis: VLA RSA analysis on LIBERO-Goal
- dinov2_baseline: DINO baseline
- plan_003_perlayer_degradation: Per-layer RSA curve
- d021_instruction_ablation: Instruction ablation
- d021_output_head_analysis: Output head analysis
- p0_functional_probe_v2: Functional action probe (main)
- p0_functional_action_probe: Earlier functional probe
- p0_functional_action_delta_probe: Action-delta probe
- plan_009: CK

I need to verify the random instruction control experiment and the trained model without instructions RSA. For the paper structure, I'm planning five main figures: an overview diagram, RSA comparisons across conditions, per-layer degradation curves, functional probe results, and a training-by-instruction matrix heatmap. I'll also need two tables for numerical summaries and statistical significance. The manuscript should span about 8 pages with the introduction and results sections taking up the most space, while keeping the abstract concise and the conclusion brief.

Now I'm calculating the word budget—a two-column CoRL format typically runs around 5000-6000 words across 8 pages, so I'll draft the YAML configuration accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "ce255b17-d106-480f-86f8-fceae3193ebc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHcu2uvFnqhHYUcv6XQrHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17512,
      "cache_read_input_tokens": 34735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17512
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

_source line 23_

所有源材料已就绪，开始起草 writing_plan.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "52b3c356-28d1-4d0c-85ff-4a4785bd869e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHcu2uvFnqhHYUcv6XQrHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17512,
      "cache_read_input_tokens": 34735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17512
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01DKHdeLddQf5PBausrnHCVM`</summary>

```json
{
  "project": "vla-ssd",
  "file": "writing_plan.yaml",
  "content": "# =============================================================================\n# Writing Plan — VLA Representational Analysis (CoRL 2026)\n# =============================================================================\n# 共享合约：Paper Agent Worker 依据此文件执行写作任务\n# 最后更新: 2026-05-16\n\nmeta:\n  venue: CoRL 2026\n  format: 8 pages + unlimited references\n  deadlines:\n    abstract: 2026-05-26\n    paper: 2026-05-29\n  title_candidates:\n    - \"The Frozen Encoder Hypothesis: Action-Relevant Representations in VLAs Originate from Vision, Not Fine-Tuning\"\n    - \"Routing Without Creating: How Vision-Language-Action Models Redistribute Pre-Existing Visual Representations\"\n    - \"Where Does Action Knowledge Live? A Representational Analysis of Vision-Language-Action Models\"\n  model_under_study: OpenVLA (Prismatic SigLIP + Llama-2-7B)\n  benchmark: LIBERO-Goal (10 tasks, OOD for fine-tuned checkpoint)\n\n# =============================================================================\n# Core Claims (locked, from paper_framing.md)\n# =============================================================================\nclaims:\n  C1:\n    label: Vision Encoder Dominance\n    one_liner: >\n      SigLIP+projector RSA=0.615 >> VLA 0.501 >> DINO 0.388.\n      Action-relevant representation structure originates from the frozen vision encoder.\n    nuance: >\n      DINO ≈ Projector in R² (0.712 vs 0.706, p=0.22) but RSA gap is large (0.388 vs 0.615).\n      VL pretraining provides geometric alignment, not additional predictive content.\n\n  C2:\n    label: \"LLM Redistributes (Training-Dependent)\"\n    one_liner: >\n      LLM degrades distributed image token geometry (RSA 0.615→0.501) but concentrates\n      action signal to readout token via training-dependent attention (trained R²=0.731\n      > proj 0.706 > untrained readout 0.686).\n    nuance: >\n      CKA shows monotonic increase (global structure preserved) — degradation is geometric (RSA),\n      not global. Readout concentration requires training (untrained readout < projector).\n\n  C3:\n    label: \"Training = Routing, Not Creating\"\n    one_liner: >\n      Distributed RSA invariant (trained ≈ untrained, bootstrap CI includes 0).\n      Training teaches routing (readout concentration), not new knowledge injection.\n      Instruction has no effect.\n    nuance: >\n      image_mean RSA Δ=+0.021, CI=[−0.031, +0.064], p=0.20.\n      last_preaction R² Δ=+0.045, CI=[0.032, 0.058], p<0.0001.\n\n# =============================================================================\n# Section Outline\n# =============================================================================\n# 字数预算基于 CoRL 双栏格式 (~750 words/page, 8 pages ≈ 6000 words text + figures/tables)\nsections:\n\n  abstract:\n    word_budget: 150\n    claims: [C1, C2, C3]\n    key_points:\n      - Problem: VLAs achieve strong performance via LLM fine-tuning, but where do action-relevant representations come from?\n      - Method: systematic representational (RSA) + functional (linear probe) decomposition of OpenVLA components\n      - \"Result 1: frozen SigLIP+projector RSA=0.615 >> full VLA ~0.50 >> DINO 0.388\"\n      - \"Result 2: LLM degrades distributed image tokens but concentrates signal to readout (R² 0.731 > proj 0.706)\"\n      - \"Result 3: concentration is training-dependent; distributed structure is training-invariant; instruction has no effect\"\n      - Implication: VLA fine-tuning learns information routing, not new action knowledge\n    writing_order: 6  # last\n\n  introduction:\n    word_budget: 1100\n    claims: [C1, C2, C3]\n    key_points:\n      - VLAs repurpose LLMs for robot control — implicit assumption that fine-tuning injects action knowledge\n      - Grant et al. 2026 showed behaviorally that visual pathway dominates, but no representational decomposition exists\n      - \"Our contribution: first systematic component-level representational + functional analysis of a VLA\"\n      - Three findings (one paragraph each, mirroring claims)\n      - Practical implications (vision encoder selection matters more than LLM fine-tuning strategy)\n    must_cite:\n      - \"Karamcheti et al. 2024 (Prismatic/OpenVLA)\"\n      - \"Grant et al. 2026 (visual pathway dominance)\"\n      - \"Kim et al. 2024 (OpenVLA)\"\n    writing_order: 4  # after results\n\n  related_work:\n    word_budget: 600\n    key_points:\n      - \"VLA architectures: RT-2, OpenVLA, Octo, π₀ — frame as LLM-based robot control\"\n      - \"VLA interpretability: Haon et al. (activation steering), Lu et al. (linear probing), Swann et al. (SAE), Molinari et al. (world models), Rizzardo et al. (observability)\"\n      - \"VLA + language: Grant et al. 2026 (behavioral), Hou 2026/LangGap (language gap), Fei 2025/LIBERO-Plus\"\n      - \"Representation analysis methods: RSA (Kriegeskorte 2008), CKA (Kornblith 2019), probing classifiers\"\n      - \"VLM fine-tuning effects: Fang 2025 (fine-tuning erodes reasoning)\"\n    must_cite:\n      - \"Kriegeskorte et al. 2008 (RSA)\"\n      - \"Kornblith et al. 2019 (CKA)\"\n      - \"Haon et al. 2025 (mechanistic interpretability on OpenVLA)\"\n      - \"Lu et al. 2025 (linear probing on OpenVLA)\"\n      - \"Swann et al. 2026 (SAE-based OpenVLA)\"\n      - \"Molinari et al. 2025 (emergent world representations)\"\n      - \"Rizzardo et al. 2026 (feature observability)\"\n      - \"Fang 2025 (fine-tuning erodes VLM reasoning)\"\n      - \"Hou 2026 / Fei 2025 (language gap)\"\n    writing_order: 5  # after intro\n\n  method:\n    word_budget: 1200\n    claims: [C1, C2, C3]\n    subsections:\n      model_and_data:\n        points:\n          - \"OpenVLA architecture: SigLIP-SO400M → MLP projector → Llama-2-7B (32 layers)\"\n          - \"LIBERO-Goal benchmark: 10 tasks, multi-goal scenes requiring instruction conditioning\"\n          - \"Checkpoint: LIBERO-10 fine-tuned (LIBERO-Goal is OOD test)\"\n          - \"Untrained control: from_config() re-initializes LLM only, SigLIP+projector frozen\"\n      rsa_analysis:\n        points:\n          - \"Representational Dissimilarity Matrices (RDMs) at each component: SigLIP output, projector output, LLM layers 0-32\"\n          - \"Action RDM: pairwise Euclidean distances in 7-DoF action space\"\n          - \"RSA: Spearman rank correlation between representation RDM and action RDM\"\n          - \"Aggregation: image_mean (primary, fair comparison) + last_preaction (supplementary)\"\n          - \"5000 pairs/task, per-task mean\"\n      functional_probes:\n        points:\n          - \"Linear ridge regression: representation → 7-DoF action, R² metric\"\n          - \"Probe targets: raw action (a_t+1) and action-delta (Δa = a_{t+1} - a_t)\"\n          - \"Models probed: projector output, LLM per-layer (image_mean + last_preaction), DINO-V2 (CLS token)\"\n          - \"Bootstrap confidence intervals (10000 resamples) for all pairwise comparisons\"\n      experimental_conditions:\n        points:\n          - \"2×2 factorial: {trained, untrained} × {with-instruction, no-instruction}\"\n          - \"Additional: random instruction control (plan_008), SigLIP-only (no LLM)\"\n    writing_order: 1  # first\n\n  results:\n    word_budget: 1800\n    subsections:\n      vision_encoder_dominance:\n        claims: [C1]\n        word_budget: 500\n        key_points:\n          - \"SigLIP+Projector RSA=0.615 [CI: 0.526, 0.695] — highest among all representations\"\n          - \"Full VLA (all 4 conditions): 0.48-0.50 band\"\n          - \"DINO: 0.388\"\n          - \"Geometric-functional dissociation: DINO R²=0.712 ≈ Projector R²=0.706 (p=0.22), but RSA 0.388 vs 0.615\"\n          - \"Implication: VL pretraining provides geometric alignment, not additional predictive content\"\n        figures: [fig2, fig4]\n        tables: [table1]\n\n      llm_redistribution:\n        claims: [C2]\n        word_budget: 700\n        key_points:\n          - \"Image token degradation: Proj RSA 0.615 → VLA image_mean 0.501 (~18% drop)\"\n          - \"Functional degradation confirmed: Proj R²=0.706 > LLM image_mean R²=0.683 (CI=[0.011, 0.037], p=0.001)\"\n          - \"Readout concentration: trained last_preaction R²=0.731 > Proj 0.706 (p=0.001)\"\n          - \"Per-layer: non-monotonic, Proj→L1 is primary drop, middle layers partial recovery\"\n          - \"CKA monotonically increases — global structure preserved, geometric alignment degraded\"\n          - \"Training-dependent: untrained readout R²=0.686 < Proj 0.706\"\n        figures: [fig3, fig4]\n        tables: [table1, table2]\n\n      training_routes_not_creates:\n        claims: [C3]\n        word_budget: 600\n        key_points:\n          - \"Distributed RSA invariant: trained 0.501 ≈ untrained 0.485, Δ=+0.021, CI=[−0.031, +0.064], p=0.20\"\n          - \"Readout concentration learned: Δ=0.045, CI=[0.032, 0.058], p<0.0001\"\n          - \"Instruction has no effect: all 4 conditions of 2×2 matrix converge at 0.48-0.50\"\n          - \"Random instruction control: [pending plan_008 results]\"\n          - \"Synthesis: training teaches routing (where to send signal), not creating (what signal to have)\"\n        figures: [fig5]\n        tables: [table2]\n\n    writing_order: 2  # after method\n\n  discussion:\n    word_budget: 800\n    key_points:\n      - \"Interpretation: frozen vision encoder as universal action-information source\"\n      - \"VL pretraining vs self-supervised: geometric alignment (RSA) vs information content (R²) dissociation\"\n      - \"RSA vs CKA dissociation: local geometric alignment vs global structure preservation (supplementary detail)\"\n      - \"Practical implications: (1) invest in vision encoder pretraining; (2) use projector output for image-level tasks; (3) LLM's value is readout concentration\"\n      - \"Connection to Grant et al. 2026: behavioral 'encoded but not used' ← our representational 'not even created by training'\"\n      - \"Aggregation sensitivity: image_mean vs last_preaction (honest discussion, both in paper)\"\n    subsections:\n      limitations:\n        points:\n          - \"Single VLA architecture (OpenVLA) — scope explicitly limited to OpenVLA-class\"\n          - \"Single benchmark family (LIBERO) — LIBERO-Goal is OOD but same simulator\"\n          - \"SigLIP vs DINO confound: pretraining objective conflated with architecture (mitigated by geometric-functional dissociation finding)\"\n          - \"Linear probes may underestimate nonlinear structure\"\n    writing_order: 4  # after intro\n\n  conclusion:\n    word_budget: 250\n    key_points:\n      - Restate three findings concisely\n      - \"VLA fine-tuning is routing optimization, not knowledge injection\"\n      - \"Future: multi-architecture validation, non-LIBERO benchmarks, attention map analysis for routing mechanism\"\n    writing_order: 7  # last before abstract\n\n# =============================================================================\n# Figure Plan\n# =============================================================================\nfigures:\n\n  fig1:\n    title: \"Analysis Pipeline Overview\"\n    type: conceptual_diagram\n    description: >\n      Left: OpenVLA architecture (SigLIP → projector → Llama-2-7B → action head)\n      with extraction points marked (projector output, per-layer LLM hidden states,\n      readout token). Right: analysis pipeline (RSA + functional probes).\n      Show 2×2 experimental conditions (trained/untrained × with/no instruction).\n    data_source: none (conceptual)\n    size: \"full_width (2-column)\"\n    placement: page 1 or 2\n    priority: P0\n\n  fig2:\n    title: \"RSA: Vision Encoder Dominance\"\n    type: bar_chart\n    description: >\n      Bar chart comparing RSA (Spearman ρ) across representations:\n      SigLIP+Projector (0.615), VLA trained with-inst (0.501), VLA trained no-inst (0.501),\n      VLA untrained with-inst (0.485), VLA untrained no-inst (0.482), DINO (0.388).\n      Error bars: bootstrap 95% CI. Horizontal dashed lines at projector and DINO levels.\n      Color code: projector=gold, trained=blue, untrained=red, DINO=gray.\n    data_source:\n      - exp: d027_siglip_only_rsa\n      - exp: lg_rsa_analysis (4 VLA conditions, image_mean aggregation)\n      - exp: dinov2_baseline\n    size: \"single_column\"\n    placement: results 4.1\n    claims: [C1, C3]\n    priority: P0\n\n  fig3:\n    title: \"Per-Layer RSA Degradation\"\n    type: line_chart\n    description: >\n      X-axis: layer (Proj, L0, L1, ..., L32). Y-axis: RSA ρ.\n      4 lines: trained with-inst, trained no-inst, untrained with-inst, untrained no-inst.\n      Horizontal dashed line at projector RSA=0.615. Highlight Proj→L1 drop zone.\n      Show non-monotonic pattern with partial middle-layer recovery.\n      Inset or annotation: \"Primary degradation at embedding interface\".\n    data_source:\n      - exp: plan_003_perlayer_degradation\n    size: \"single_column\"\n    placement: results 4.2\n    claims: [C2]\n    priority: P0\n\n  fig4:\n    title: \"Functional Probe: Geometric-Functional Dissociation\"\n    type: grouped_bar_chart\n    description: >\n      Two groups side by side:\n      Left group (RSA): Projector 0.615, LLM img_mean 0.501, DINO 0.388\n      Right group (Action R²): Projector 0.706, LLM img_mean 0.683, LLM readout 0.731, DINO 0.712\n      Key visual: DINO and Projector swap relative positions between RSA and R².\n      Bootstrap CI error bars. Significance brackets for key comparisons.\n    data_source:\n      - exp: p0_functional_probe_v2 (R² values + bootstrap CIs)\n      - exp: d027_siglip_only_rsa (RSA values)\n      - exp: dinov2_baseline (RSA)\n    size: \"full_width (2-column)\"\n    placement: results 4.1-4.2 boundary\n    claims: [C1, C2]\n    priority: P0\n\n  fig5:\n    title: \"2×2 Matrix: Training × Instruction\"\n    type: heatmap\n    description: >\n      2×2 heatmap with RSA values. Rows: trained/untrained. Cols: with-inst/no-inst.\n      Cell values: 0.501, 0.501, 0.485, 0.482.\n      Color scale anchored: projector=0.615 (top), DINO=0.388 (bottom).\n      Annotation: \"All conditions converge within [0.48, 0.50] — neither training nor instruction alters distributed structure.\"\n      Optional: second panel with bootstrap Δ CIs showing all include 0.\n    data_source:\n      - exp: lg_rsa_analysis\n      - exp: d027_trained_no_inst_rsa\n      - exp: d021_instruction_ablation\n    size: \"single_column\"\n    placement: results 4.3\n    claims: [C3]\n    priority: P0\n\n  fig6:\n    title: \"Readout Concentration: Training-Dependent\"\n    type: bar_chart_or_line\n    description: >\n      Compare last_preaction R² across layers for trained vs untrained.\n      Trained: peak L19 R²=0.731. Untrained: best L1 R²=0.686, most layers collapsed.\n      Horizontal dashed line at projector R²=0.706.\n      Key visual: trained readout exceeds projector, untrained does not.\n    data_source:\n      - exp: p0_functional_probe_v2 (trained + untrained last_preaction per-layer)\n    size: \"single_column\"\n    placement: results 4.2 or 4.3\n    claims: [C2, C3]\n    priority: P0\n\n# =============================================================================\n# Table Plan\n# =============================================================================\ntables:\n\n  table1:\n    title: \"Main Results: RSA and Functional Probe Summary\"\n    description: >\n      Rows: SigLIP+Projector, VLA Trained (image_mean), VLA Trained (readout),\n      VLA Untrained (image_mean), VLA Untrained (readout), DINO.\n      Columns: RSA ρ [95% CI], Action R² [95% CI], Action-Delta R².\n      Bold best values. Significance markers (*, **, ***) for key comparisons.\n    data_source:\n      - exp: d027_siglip_only_rsa\n      - exp: lg_rsa_analysis\n      - exp: p0_functional_probe_v2\n      - exp: dinov2_baseline\n    placement: results (top of section or 4.1)\n    claims: [C1, C2, C3]\n    priority: P0\n\n  table2:\n    title: \"Bootstrap Statistical Tests\"\n    description: >\n      Rows: key pairwise comparisons.\n      1. Proj vs LLM image_mean (RSA): Δ=0.114\n      2. Proj vs LLM image_mean (R²): Δ=0.023, CI=[0.011, 0.037], p=0.001\n      3. Trained readout vs Proj (R²): Δ=0.025, p=0.001\n      4. Trained vs Untrained readout (R²): Δ=0.045, CI=[0.032, 0.058], p<0.0001\n      5. Trained vs Untrained image_mean (RSA): Δ=0.021, CI=[−0.031, +0.064], p=0.20\n      6. DINO vs Proj (R²): Δ=0.005, CI=[−0.008, 0.019], p=0.22\n      Columns: Comparison, Δ, 95% CI, p-value, Interpretation.\n    data_source:\n      - exp: p0_functional_probe_v2\n      - exp: lg_rsa_analysis\n    placement: results 4.2 or 4.3\n    claims: [C1, C2, C3]\n    priority: P0\n\n# =============================================================================\n# Supplementary Material Plan\n# =============================================================================\nsupplementary:\n\n  supp_cka:\n    title: \"CKA Analysis and RSA-CKA Dissociation\"\n    description: >\n      CKA ordering reversal vs RSA. CKA per-layer curve (monotonic increase).\n      CKA last_preaction highest (0.127). Discussion of RSA vs CKA capturing\n      different aspects (local geometric alignment vs global structure preservation).\n    data_source:\n      - exp: plan_009\n\n  supp_aggregation:\n    title: \"Aggregation Robustness Check\"\n    description: >\n      last_preaction RSA values alongside image_mean. Both aggregations yield\n      consistent conclusions. last_preaction: trained 0.488, untrained 0.485.\n    data_source:\n      - exp: lg_rsa_analysis\n      - exp: d027_siglip_only_rsa\n\n  supp_action_delta:\n    title: \"Action-Delta Probe Results\"\n    description: >\n      Full action-delta R² comparison. Proj 0.118, LLM 0.122, DINO 0.061-0.100.\n      CI includes 0 for proj vs LLM — consistent with main findings.\n    data_source:\n      - exp: p0_functional_action_delta_probe\n\n  supp_random_instruction:\n    title: \"Random Instruction Control\"\n    description: >\n      [Pending plan_008 results]. Random/mismatched instructions should not\n      affect RSA, confirming instruction content is irrelevant to representation structure.\n    data_source:\n      - exp: plan_008\n\n  supp_per_layer_probe:\n    title: \"Per-Layer Functional Probe Curves\"\n    description: >\n      R² across all 33 layers for trained and untrained, both image_mean and\n      last_preaction. Shows untrained layer collapse pattern vs trained stability.\n    data_source:\n      - exp: p0_functional_probe_v2\n\n# =============================================================================\n# Writing Order\n# =============================================================================\nwriting_order:\n  - section: method\n    reason: \"Establishes experimental framework; most straightforward to write from existing protocol\"\n  - section: results\n    reason: \"Data-driven, write directly from experiment outputs\"\n  - section: discussion\n    reason: \"Interpret results, address limitations\"\n  - section: introduction\n    reason: \"Frame story after knowing exact results and discussion points\"\n  - section: related_work\n    reason: \"Position after intro framing is set\"\n  - section: abstract\n    reason: \"Compress final paper into 150 words\"\n  - section: conclusion\n    reason: \"Brief, write alongside abstract\"\n\n# =============================================================================\n# Literature (must-cite list)\n# =============================================================================\nliterature:\n  foundational:\n    - key: \"karamcheti2024prismatic\"\n      why: \"OpenVLA's architectural foundation (SigLIP + Llama-2)\"\n    - key: \"kim2024openvla\"\n      why: \"The model we analyze\"\n    - key: \"kriegeskorte2008rsa\"\n      why: \"RSA methodology\"\n    - key: \"kornblith2019cka\"\n      why: \"CKA methodology (supplementary)\"\n\n  directly_related:\n    - key: \"grant2026visual\"\n      why: \"Behavioral-level visual pathway dominance — we provide representational confirmation\"\n    - key: \"haon2025mechanistic\"\n      why: \"Mechanistic interpretability on same model (OpenVLA), complementary approach\"\n    - key: \"lu2025linear\"\n      why: \"Linear probing on OpenVLA layers — methodologically closest, must differentiate\"\n    - key: \"swann2026sae\"\n      why: \"SAE-based OpenVLA interpretability\"\n    - key: \"molinari2025emergent\"\n      why: \"Emergent world representations in OpenVLA\"\n    - key: \"rizzardo2026observability\"\n      why: \"Feature observability/controllability in VLAs\"\n\n  language_gap:\n    - key: \"hou2026langgap\"\n      why: \"VLAs ignore language — we explain representationally why\"\n    - key: \"fei2025liberoplus\"\n      why: \"LIBERO-Plus language evaluation — same finding, different level\"\n\n  broader_context:\n    - key: \"fang2025finetuning\"\n      why: \"Fine-tuning erodes VLM reasoning — LLM step itself degrades visual structure\"\n    - key: \"brohan2023rt2\"\n      why: \"RT-2 as seminal VLA architecture\"\n    - key: \"team2024octo\"\n      why: \"Alternative VLA architecture for context\"\n    - key: \"hewitt2019probe\"\n      why: \"Probe complexity / selectivity concerns (methodology)\"\n    - key: \"libero2023\"\n      why: \"LIBERO benchmark\"\n\n# =============================================================================\n# Risk Matrix (Reviewer Attack Surface)\n# =============================================================================\nrisks:\n\n  R1:\n    threat: \"Single VLA architecture — findings may not generalize\"\n    severity: high\n    mitigation: >\n      Scope all claims explicitly to \"OpenVLA-class architectures.\" OpenVLA is the most\n      widely studied open-source VLA. Discussion: predict which findings likely generalize\n      (vision encoder dominance) vs architecture-specific (layer-level patterns).\n    section: discussion/limitations\n\n  R2:\n    threat: \"SigLIP vs DINO pretraining confound\"\n    severity: medium\n    mitigation: >\n      Turn into a positive finding: geometric-functional dissociation (DINO ≈ Proj in R²\n      but RSA gap large) proves VL pretraining provides geometric alignment, not extra content.\n      plan_012 CLIP-ViT control (P1) if time permits.\n    section: discussion\n\n  R3:\n    threat: \"RSA ≠ task performance (correlational, not causal)\"\n    severity: medium\n    mitigation: >\n      Functional probes provide causal grounding: projector R²=0.706 confirms RSA alignment\n      translates to decodable action information. Readout R²=0.731 shows LLM concentrates\n      this information. Both RSA and R² tell consistent story.\n    section: results + discussion\n\n  R4:\n    threat: \"Aggregation method affects conclusions\"\n    severity: medium\n    mitigation: >\n      Main text uses image_mean (fair). Supplementary shows last_preaction.\n      Both aggregations yield same qualitative conclusions.\n      Honest discussion paragraph in 4.2 or Discussion.\n    section: results + supplementary\n\n  R5:\n    threat: \"'Training invariance' contradicts readout concentration being training-dependent\"\n    severity: medium\n    mitigation: >\n      Carefully scoped: distributed representation structure is invariant (image_mean RSA),\n      but information routing is learned (last_preaction R²). These are complementary,\n      not contradictory — training changes WHERE information goes, not WHAT information exists.\n    section: results 4.3\n\n  R6:\n    threat: \"Confirmatory of Grant et al. 2026\"\n    severity: medium\n    mitigation: >\n      Differentiate clearly: Grant = behavioral (input-output), we = representational\n      (WHERE inside the model + HOW). Our component decomposition, per-layer analysis,\n      and redistribution finding are novel contributions beyond behavioral confirmation.\n    section: introduction + related_work\n\n  R7:\n    threat: \"LIBERO-only benchmark\"\n    severity: low\n    mitigation: >\n      LIBERO-Goal is specifically chosen as vision-ambiguous (same scene, different goals),\n      making it a strong test. Acknowledge limitation; plan_010 cross-benchmark as future work.\n    section: limitations\n\n  R8:\n    threat: \"Linear probes may underestimate nonlinear structure\"\n    severity: low\n    mitigation: >\n      RSA is probe-free (directly measures geometry). Functional probes are linear by design\n      to test what is linearly decodable (standard in probing literature, cite Hewitt & Manning 2019).\n    section: method\n\n# =============================================================================\n# Timeline\n# =============================================================================\ntimeline:\n  \"2026-05-16\":\n    - \"Finalize writing_plan.yaml\"\n    - \"plan_008 results analysis (when complete)\"\n    - \"Re-dream with updated framing\"\n  \"2026-05-17\":\n    - \"Method + Results draft\"\n    - \"Generate all figures (fig1-fig6)\"\n    - \"Generate tables (table1-table2)\"\n  \"2026-05-18\":\n    - \"Introduction + Related Work + Discussion draft\"\n    - \"Internal review pass\"\n  \"2026-05-19\":\n    - \"Abstract + Conclusion\"\n    - \"Full paper revision pass\"\n  \"2026-05-20_to_25\":\n    - \"Polish, figure refinement, reference audit\"\n    - \"plan_012 CLIP-ViT control (if time permits)\"\n  \"2026-05-26\":\n    - \"Submit abstract\"\n  \"2026-05-27_to_28\":\n    - \"Final revision\"\n  \"2026-05-29\":\n    - \"Submit paper\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "bbc986d8-0d6b-4fb7-960a-4408eeda1b68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHcu2uvFnqhHYUcv6XQrHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17512,
      "cache_read_input_tokens": 34735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17512
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

_source line 25 · 2026-05-16T00:32:30.318Z_

<details><summary>↩ Tool result · `toolu_01DKHdeLddQf5PBausrnHCVM`</summary>

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
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "6620e80e-77d3-42b3-a494-aa268a67c750",
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

_source line 26_

`writing_plan.yaml` 已写入，包含：

- **7 个 section** 的要点、字数预算和 claim 映射
- **6 张图**：pipeline 概念图、RSA 对比、per-layer 曲线、geometric-functional dissociation、2×2 heatmap、readout concentration 对比，每张标注数据来源 exp_id 和尺寸
- **2 张表**：主数值汇总 + bootstrap 统计检验
- **5 项 supplementary**：CKA dissociation、聚合 robustness、action-delta、random instruction、per-layer probe
- **写作顺序**：Method → Results → Discussion → Introduction → Related Work → Abstract → Conclusion
- **17 篇必引文献**，分 foundational / directly related / language gap / broader context 四组
- **8 个 reviewer 风险点**及对应防御策略和落位 section
- **时间线**：5/17 Method+Results 初稿，5/19 全文初稿，5/26 abstract，5/29 paper

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "uuid": "1201d857-e5a0-4e7d-b271-c8e9ce8fc1d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XthPx2EHTe1aUsLQHamXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8404,
      "cache_read_input_tokens": 52247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8404
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

_source line 27_

`writing_plan.yaml` 已写入，包含：

- **7 个 section** 的要点、字数预算和 claim 映射
- **6 张图**：pipeline 概念图、RSA 对比、per-layer 曲线、geometric-functional dissociation、2×2 heatmap、readout concentration 对比，每张标注数据来源 exp_id 和尺寸
- **2 张表**：主数值汇总 + bootstrap 统计检验
- **5 项 supplementary**：CKA dissociation、聚合 robustness、action-delta、random instruction、per-layer probe
- **写作顺序**：Method → Results → Discussion → Introduction → Related Work → Abstract → Conclusion
- **17 篇必引文献**，分 foundational / directly related / language gap / broader context 四组
- **8 个 reviewer 风险点**及对应防御策略和落位 section
- **时间线**：5/17 Method+Results 初稿，5/19 全文初稿，5/26 abstract，5/29 paper

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 183658,
  "duration_api_ms": 185043,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "05c1006d-527b-4be0-b564-d910b89a5d6e",
  "total_cost_usd": 0.6280165000000001,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 48810,
    "cache_read_input_tokens": 176846,
    "output_tokens": 9306,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48810,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 291,
        "cache_read_input_tokens": 52247,
        "cache_creation_input_tokens": 8404,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 8404
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1741,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001831,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 9306,
      "cacheReadInputTokens": 176846,
      "cacheCreationInputTokens": 48810,
      "webSearchRequests": 0,
      "costUSD": 0.6261855,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f665d4fa-996b-4c00-a8a3-032b090b953e"
}
```

</details>

---
