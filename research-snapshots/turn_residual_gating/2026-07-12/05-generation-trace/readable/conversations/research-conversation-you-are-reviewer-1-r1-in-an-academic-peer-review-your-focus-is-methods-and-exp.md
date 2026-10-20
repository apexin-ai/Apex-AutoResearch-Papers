# Research conversation: You are Reviewer 1 (R1) in an academic peer review. Your focus is **Methods and Experiments**. Evaluate this paper for a

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ae2599494e25f4698.jsonl`
- **Structured JSON:** [`c6d24056bb50ccfc819d.json`](../../sessions/c6/c6d24056bb50ccfc819d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-19T15:38:32.575Z_

You are Reviewer 1 (R1) in an academic peer review. Your focus is **Methods and Experiments**. Evaluate this paper for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

## Paper Summary

**Title**: "Why Does Gating Fail on Qwen but Not Llama? Architecture-Dependent Vulnerability of Auxiliary Attention Loss under Training-Inference Distribution Shift"

**Core idea**: ThreadGate adds per-layer learnable scalar gates g_l to residual connections (x_{l+1} = x_l + g_l · f_l(x_l)), trained jointly with NTP + GAR auxiliary loss (MSE targeting + gate diversity). On Qwen-2.5-7B, training GAR reaches 0.48 but collapses to 0.016 at inference (30× gap), zero benefit over LoRA-only. On Llama-3.1-8B, gap is 4.6×, gating yields +3.5pp GAR improvement. Divergence traced to NTP-GAR gradient conflict on gate parameters.

**Contributions claimed**:
1. First architecture-contrastive quantification of training-inference distribution shift in auxiliary attention losses (4.6× Llama vs 30× Qwen)
2. Layer-wise quantification of NTP-GAR gradient conflict (persistent on Qwen, resolves on Llama)
3. Evidence that exposure bias is not sole failure mechanism (scheduled sampling reduces gap ratio 42% but inference GAR improves only 0.18pp)
4. Systematic ablation showing architecture-dependent gating benefit (zero on Qwen, weak positive on Llama)

**Experimental Setup**:
- Models: Qwen-2.5-7B (28 layers, 7 KV head groups) and Llama-3.1-8B (32 layers, 8 KV head groups)
- Training: 3 epochs on UltraChat, LR 2e-4, LoRA rank 8, batch 4, seed 42, single GPU, 5.9-9.5 hours
- Evaluation: 50 held-out multi-turn conversations, two GAR definitions (GAR-Dongre and GAR-ours), PPL
- Qwen: 4-way ablation (Base, ThreadGate, Uniform Gate, LoRA-only)
- Llama: 3-way ablation (Base, ThreadGate, LoRA-only)
- Statistical testing: paired bootstrap 95% CI (10,000 resamples) for TG-LoRA on Qwen
- Additional: gradient conflict analysis (cosine similarity + magnitude ratio across epochs), attention heatmap visualization, scheduled sampling mitigation, downstream instruction compliance task

**Key Results**:
- Table 1: Qwen base GAR drops 70.8% (monotonic), Llama only 25.3% (non-monotonic)
- Table 2: Training-inference gap: Qwen 30.6× (ours) / 31.6× (Dongre); Llama 4.6× / 8.7×
- Table 3 (Qwen 4-way): TG GAR-Dongre=0.0152, LoRA=0.0132, diff=+0.20pp; PPL identical at 2.63
- Table 4 (Llama 3-way): TG GAR-Dongre=0.0485, LoRA=0.0132, diff=+3.53pp; PPL 2.95 vs 2.98
- Table 5: Cross-model gating benefit: Qwen=None, Llama=Weak positive
- Table 6: Qwen gradient conflict cos_sim from -0.089 to -0.042 (never positive), mag_ratio from 7.5× to 14.7×, L27 mag_ratio from 135× to 1139×
- Table 7: Cross-model gradient comparison. Llama cos_sim resolves from -0.015 to +0.008; mag_ratio 3.5×; top layer 18.5× vs Qwen 1139×
- Table 8: Attention visualization — cross-model correlation 0.97, zero visible gate effect on Qwen
- Table 9: Scheduled sampling — gap ratio drops 30.6× to 17.7× but inference GAR only +0.18pp
- Table 10: Instruction compliance — all models ~86% at turn 1 to ~49% at turn 20, TG-LoRA diff = 1pp at turn 20
- Table 11: Bootstrap CI — GAR-Dongre CI includes 0 (supports zero benefit); GAR-ours CI [+0.12, +1.05] excludes 0 (sub-1pp significant positive)

**Planned experiments from review context (check coverage)**:
All 10 planned experiments are covered in the paper: Qwen gradient conflict (plan_006→Table 6), attention heatmap (plan_007→Table 8/§6.5), Llama GAR degradation (plan_009→Table 1), Llama TG training (plan_010→Table 2), Llama LoRA training (plan_011→Table 4), Llama 3-way eval (plan_012→Tables 4-5), Llama gradient conflict (plan_013→Table 7), downstream task (plan_014→Table 10), bootstrap CI (plan_015→Table 11), scheduled sampling (plan_016→Table 9).

## Your Task

Write a detailed review covering:

1. **Strengths** (methods, experimental design, rigor, reproducibility)
2. **Weaknesses** (methodological flaws, missing controls, statistical concerns, evaluation gaps)
3. **Detailed Comments** on specific experiments and analysis
4. **Questions for Authors**
5. **Minor Issues**
6. **Overall Assessment** with score (1-6) and confidence (1-5)

Be rigorous and specific. Reference specific tables, sections, and numbers. Consider:
- Is the experimental design sufficient to support the claims?
- Are there confounding factors not controlled for?
- Is the statistical analysis appropriate?
- Are the evaluation metrics well-chosen?
- Is the gradient conflict analysis methodologically sound?
- What experiments are missing that would strengthen the paper?
- Is the single-seed evaluation a serious concern?
- How robust are the cross-architecture comparisons given the many differences between Qwen and Llama?

Output your review in structured markdown format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "4fc986df-2f4e-4819-9faa-e76ee3494d6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T15:38:32.581Z_

```json
{
  "parentUuid": "4fc986df-2f4e-4819-9faa-e76ee3494d6a",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1ceb3a65-34aa-4476-828b-b56c23ca3b17",
  "timestamp": "2026-05-19T15:38:32.581Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T15:38:35.102Z_



I need to read the paper and related project files to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ceb3a65-34aa-4476-828b-b56c23ca3b17",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBFZSivNDVGZJK2jD7W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5070b69c-ba82-4fd2-8ad2-d387642cb267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvHgaxzG3SEohBy9feWb2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16139,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16139,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T15:38:36.734Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FyhzzjMoecho9AnfkYBjS5`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5070b69c-ba82-4fd2-8ad2-d387642cb267",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBFZSivNDVGZJK2jD7W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de1e99a8-0226-44e6-bfd2-e6c02b753081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvHgaxzG3SEohBy9feWb2a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16139,
      "cache_read_input_tokens": 0,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16139
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 123,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16139,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T15:38:36.741Z_

<details><summary>↩ Tool result · `toolu_01FyhzzjMoecho9AnfkYBjS5`</summary>

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
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de1e99a8-0226-44e6-bfd2-e6c02b753081",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "2aa6ecec-994f-400a-8c66-d37ad5876db8",
  "sourceToolAssistantUUID": "de1e99a8-0226-44e6-bfd2-e6c02b753081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T15:38:39.958Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019YZNDqUZjReo3dJx3HBz3Q`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aa6ecec-994f-400a-8c66-d37ad5876db8",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBFsEJDZ3tBysYmZYgo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ccf8f66-0e15-47e7-b09d-a8e4a92cd732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgEsWUMiccS4LkEFXamdVV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T15:38:39.981Z_

<details><summary>↩ Tool result · `toolu_019YZNDqUZjReo3dJx3HBz3Q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- phase2_tg_s42_v8_schedsampling: Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。（准备中）\\n\\n## 近期结论\\n- **analysis_attention_heatmap** (success): 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。 ← 基于 phase2_tg_s42_v7\\n- **analysis_gradient_conflict** (success): NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。 ← 基于 phase2_tg_s42_v7\\n- **phase2_4way_eval_heldout** (success): 四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。 ← 基于 phase2_4way_eval\\n\\n## 趋势\\n成功 8 / 负向 5 / 失败 1 / 共 15\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-20861: 无 GPU 信息\\n\\n## 告警\\n- phase2_tg_s42_v2: 已被终止 — unknown\\n- phase2_tg_s42_v4: 训练失败 — unknown\\n\", \"total_chars\": 1139, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ccf8f66-0e15-47e7-b09d-a8e4a92cd732",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "d264740f-0378-4c04-b8e0-84d6d72518d7",
  "sourceToolAssistantUUID": "8ccf8f66-0e15-47e7-b09d-a8e4a92cd732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T15:38:40.064Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Evtccp17Xgi7nbF2xGcv5G`</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d264740f-0378-4c04-b8e0-84d6d72518d7",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBFsEJDZ3tBysYmZYgo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "099dcb09-f173-4442-8491-f693890c31f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgEsWUMiccS4LkEFXamdVV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16139,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 16139,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T15:38:40.149Z_

<details><summary>↩ Tool result · `toolu_01Evtccp17Xgi7nbF2xGcv5G`</summary>

```text
{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (16 个)\n\n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: PREPARING — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v6**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase2_tg_s42**: DONE (negative) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- phase2_tg_s42_v8_schedsampling: Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。（准备中）\n\n## 近期结论\n- **analysis_attention_heatmap** (success): 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。 ← 基于 phase2_tg_s42_v7\n- **analysis_gradient_conflict** (success): NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。 ← 基于 phase2_tg_s42_v7\n- **phase2_4way_eval_heldout** (success): 四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。 ← 基于 phase2_4way_eval\n\n## 趋势\n成功 8 / 负向 5 / 失败 1 / 共 15\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-20861: 无 GPU 信息\n\n## 告警\n- phase2_tg_s42_v2: 已被终止 — unknown\n- phase2_tg_s42_v4: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "099dcb09-f173-4442-8491-f693890c31f2",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "f0d1ffda-3acf-40f7-b112-0faae1485fa5",
  "sourceToolAssistantUUID": "099dcb09-f173-4442-8491-f693890c31f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T15:38:44.067Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FRZgK8oFkV6Htg4fzzcfZm`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0d1ffda-3acf-40f7-b112-0faae1485fa5",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBG7nehLFJSao4zvEwZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6919a586-633a-4911-a8d5-c47a52fa3211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GmCiQKp7ZMLJZMv61meXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 17585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T15:38:44.081Z_

<details><summary>↩ Tool result · `toolu_01FRZgK8oFkV6Htg4fzzcfZm`</summary>

```text
artifacts/dream_reports/dream_20260519T135115/best/paper.tex
artifacts/dream_reports/dream_20260519T135115/median/paper.tex
artifacts/dream_reports/dream_20260519T135115/worst/paper.tex
artifacts/dream_reports/dream_20260519T143220/best/paper.tex
artifacts/dream_reports/dream_20260519T143220/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/best/paper.tex
artifacts/dream_reports/dream_20260519T145320/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6919a586-633a-4911-a8d5-c47a52fa3211",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "e5ba442d-609c-423e-9b17-107be3125042",
  "sourceToolAssistantUUID": "6919a586-633a-4911-a8d5-c47a52fa3211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T15:38:45.074Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LqVzbeSueLUeRgqJYNxYFv`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5ba442d-609c-423e-9b17-107be3125042",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBG7nehLFJSao4zvEwZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "410b30d6-9f55-40d7-8d69-88da866ef5a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GmCiQKp7ZMLJZMv61meXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 17585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T15:38:45.085Z_

<details><summary>↩ Tool result · `toolu_01LqVzbeSueLUeRgqJYNxYFv`</summary>

```text
artifacts/_project/intermediate/diagnose_gar_loss_results.md
artifacts/paper/method_section_draft.md
artifacts/_project/report/route_b_design.md
artifacts/route_b_design.md
artifacts/_project/report/llama3_cross_model_plan.md
artifacts/llama3_cross_model_plan.md
artifacts/dream_reports/dream_20260519T135115/best/paper_framing.md
artifacts/dream_reports/dream_20260519T135115/median/paper_framing.md
artifacts/dream_reports/dream_20260519T135115/worst/paper_framing.md
artifacts/dream_reports/dream_20260519T135115/median/review_report.md
artifacts/dream_reports/dream_20260519T135115/best/review_report.md
artifacts/dream_reports/dream_20260519T143220/best/paper_framing.md
artifacts/dream_reports/dream_20260519T143220/median/paper_framing.md
artifacts/dream_reports/dream_20260519T145320/best/paper_framing.md
artifacts/dream_reports/dream_20260519T145320/median/paper_framing.md
artifacts/dream_reports/dream_20260519T145320/worst/paper_framing.md
artifacts/dream_reports/dream_20260519T145320/best/review_report.md
artifacts/dream_reports/dream_20260519T145320/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "410b30d6-9f55-40d7-8d69-88da866ef5a1",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "91351ed2-c87e-4cc6-9cad-1cd648b7d23f",
  "sourceToolAssistantUUID": "410b30d6-9f55-40d7-8d69-88da866ef5a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T15:38:45.626Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TxNmguqfu5QmMyucwkjnJn`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91351ed2-c87e-4cc6-9cad-1cd648b7d23f",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBG7nehLFJSao4zvEwZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3207a6e7-0e90-4535-871c-1f95d9e46b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GmCiQKp7ZMLJZMv61meXi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 17585,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2180
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 17585,
          "cache_creation_input_tokens": 2180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2180,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T15:38:45.636Z_

<details><summary>↩ Tool result · `toolu_01TxNmguqfu5QmMyucwkjnJn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md\", \"content\": \"# turn_residual_gating — Research Dashboard\\n\\n> 最后更新: 2026-05-19 14:54 UTC | 更新原因: plan_015 DONE (bootstrap CI confirms zero benefit), disk strategy corrected (246GB data disk), re-dream launched\\n\\n> 核心方向详见 paper_framing.md | 实验列表详见 experiment_plan.yaml\\n\\n## 核心方向\\n**Route B: Negative result + mechanistic insight** — lightweight residual gating 在 teacher-forcing 下的 auxiliary attention loss 泛化失败。核心卖点：exposure bias 在 auxiliary attention loss 上的首个定量测量（30x gap）+ 失败机制 taxonomy。\\n\\n**目标 venue**: EMNLP 2026（ARR August cycle, deadline 2026-08-03, ~10 weeks）\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP, framing 收窄 D022, Eq.3 修正 D023）\\n- **Re-dream**: `dream_20260519T145320` 已启动（full review mode, 修正后 focus），预计 15-25 min\\n- **Qwen 实验**: C1-C4 全部完成 ✅（含 held-out eval + bootstrap CI）\\n- **plan_015 (bootstrap CI)**: 所有 GAR-ours/PPL 95% CI 包含 0，统计确认 \\\"zero benefit\\\"。W7 已回应。\\n- **plan_017 (D023)**: Eq.3 公式与代码语义相反已确认。Paper Agent 写作时修正。\\n- **C3 注意**: plan_006/007 已完成但缺 registry_id，Agent 处理中\\n- **GPU**: westd-20861:cuda:0 空闲 → urgent 已派 plan_016\\n\\n## 核心 Claims (Route B)\\n| Claim | 状态 | 证据 |\\n|-------|------|------|\\n| C1: GAR 衰减 70.8% | ✅ | Phase 1 |\\n| C2: 训练-推理 30x 断层 | ✅ | v7 训练+eval; held-out 确认 |\\n| C3: 三个失败机制 | ✅ | 梯度冲突+gate profile+attention heatmap (缺 registry_id) |\\n| C4: 四路消融 gating 零增量 | ✅✅ | D021 + held-out + **bootstrap CI (所有 95% CI 含 0)** |\\n| C5: 跨模型验证 | ⬜ | Llama-3 (plan_009-012, MUST-HAVE) |\\n\\n## 近期任务\\n- [x] paper_framing.md 收窄 claim scope (D022)\\n- [x] plan_008 held-out eval — 三路趋同鲁棒复现\\n- [x] plan_017: code-paper 架构验证 — Eq.3 mismatch confirmed (D023)\\n- [x] plan_015: Bootstrap CI — 所有 CI 含 0，统计确认 zero benefit\\n- [ ] **plan_016: Exposure-bias mitigation test (8h GPU)** ← urgent 已派 Agent\\n- [ ] plan_006/007: 补 registry_id（Agent 处理中）\\n- [ ] **⚠️ Paper Agent 写 Method 前必须修正 Eq.3**: 用 `x+g·f(x)`，修正机制叙事\\n- [ ] Llama-3 下载到 data disk（与 plan_016 并行，零 GPU 空转）\\n- [ ] Re-dream 验证 framing 修正（dream_20260519T145320 运行中）\\n- [ ] plan_009-012: Llama-3 跨模型验证（~15h, 待 re-dream 通过）\\n- [ ] plan_014: Downstream task sanity check (P2, 1h)\\n\\n## GPU 执行序列\\n1. **plan_016** (Qwen, 8h) — exposure-bias mitigation，**同时**下载 Llama-3 到 data disk\\n2. plan_016 完成后**直接**启动 **plan_009-012** (Llama-3, ~15h)（无需清 cache，两模型共存于不同磁盘）\\n3. plan_013/014 (如时间允许)\\n\\n## GPU 预算\\n- 已分配: westd-20861:cuda:0（plan_016 启动中）\\n- 已用: ~41.6 GPU·h\\n- 剩余: plan_016(8h) + Llama-3(15.5h) + downstream(1h) = ~24.5h\\n- 磁盘: root 15G/30G (Qwen) + **data disk 246G/250G (Llama-3)**，两模型可共存\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D023 | 2026-05-19 | Eq.3 code-paper formula mismatch confirmed (plan_0 | plan_017 |\\n| D022 | 2026-05-19 | Dream review 分析: 收窄 claim scope + 补充 3 个实验 (bootst | phase2_4way_eval, phase2_tg_s42_v7 |\\n| D021 | 2026-05-19 | Route B 正式确认：四路 eval 三路趋同（GAR 差异<0.6pp, PPL 差异<0.0 | phase2_lora_only_s42, phase2_tg_s42_v7, phase2_ug_s42 |\\n| D020 | 2026-05-19 | Llama-3 最小验证方案扩展为 Base + TG + LoRA-only（Reviewer 建 | phase2_tg_s42_v7 |\\n| D019 | 2026-05-19 | v7 中间 checkpoint：选 Option B（3 epoch checkpoint 粗粒度 | phase2_tg_s42_v7 |\\n| D018 | 2026-05-19 | Reviewer 深度分析：Route A 成功概率从 20-30% 修正至 <5%，根本矛盾是 t | phase2_lora_only_s42, phase2_tg_s42_v7, phase2_ug_s42 |\\n| D017 | 2026-05-19 | 采纳 Reviewer 两路策略：准备路线 B 框架（negative result + mecha | phase2_tg_s42_v7, phase2_ug_s42, phase2_lora_only_s42 |\\n| D016 | 2026-05-19 | Two-stage decoupled training：有条件尝试（~20-30% 成功率）。以  | phase2_tg_s42_v7, phase2_ug_s42, phase2_lora_only_s42 |\\n| D015 | 2026-05-19 | 30x 训练-推理 GAR 断层确认为 GAR 过拟合（非 measurement bug）。发现实 | phase2_tg_s42_v7, phase2_ug_s42, phase2_lora_only_s42 |\\n| D014 | 2026-05-19 | Gate-profile 揭示 turn conditioning 反向学习：27/28 层 gat | phase2_tg_s42_v7, phase2_ug_s42, phase2_lora_only_s42 |\\n\\n\\n\\n\", \"total_chars\": 3647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3207a6e7-0e90-4535-871c-1f95d9e46b0b",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "94323abb-787b-4ece-832c-bab0402b16ea",
  "sourceToolAssistantUUID": "3207a6e7-0e90-4535-871c-1f95d9e46b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T15:38:48.360Z_

Let me read the latest paper drafts to get the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94323abb-787b-4ece-832c-bab0402b16ea",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBGXk3tKQJPyEXNU5Rg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a00ccdc1-a9dc-4e9e-8d10-970bbe37bf8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLbKu1yQ17ErRhVupDFPJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3140,
      "cache_read_input_tokens": 19765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3140,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T15:38:51.467Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NL4jtbrxMrwN3HgB9ESeYk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a00ccdc1-a9dc-4e9e-8d10-970bbe37bf8b",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBGXk3tKQJPyEXNU5Rg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3539065-d1a7-40eb-a379-307a71ebbd1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLbKu1yQ17ErRhVupDFPJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3140,
      "cache_read_input_tokens": 19765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3140,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T15:38:51.723Z_

<details><summary>↩ Tool result · `toolu_01NL4jtbrxMrwN3HgB9ESeYk`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	
17	\title{Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation:\\ A Mechanistic Analysis}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Large Language Models (LLMs) progressively lose attention to goal-relevant tokens as multi-turn dialogues grow longer, a phenomenon quantified by the Goal Attention Ratio \citep[GAR;][]{dongre2026}. Prior work shows that goal information persists in the residual stream (probe AUC up to 0.98) even as the attention channel closes, motivating a natural intervention: learnable per-layer gates on the residual connection trained with an auxiliary GAR objective. We implement this hypothesis as ThreadGate, a lightweight residual gating module jointly optimized with next-token prediction (NTP) and GAR losses. ThreadGate successfully raises GAR from 0.02 to 0.48 during training, yet this improvement completely fails to transfer to inference (GAR = 0.016), revealing a 30$\times$ training--inference gap. We identify two coupled mechanisms behind this failure: (1) NTP gradients dominate gate parameters by 7--15$\times$ in magnitude, causing gates to learn \emph{reverse turn conditioning} that suppresses intervention where it is most needed; (2) at inference, gates attenuate sublayer outputs by only 2--7\%, rendering the gating mechanism effectively inert. Four-way ablation across two model families (Qwen-2.5-7B and Llama-3.1-8B) confirms that gating provides zero incremental benefit over LoRA-only fine-tuning (paired bootstrap $p = 0.71$, Cohen's $d = 0.02$). A scheduled sampling experiment reduces the gap from 30$\times$ to 4.3$\times$, providing causal evidence that exposure bias is the primary driver. Our findings constitute the first quantitative measurement of how teacher-forcing distribution shift destroys auxiliary attention loss generalization in lightweight residual gating.
26	\end{abstract}
27	
28	%---------------------------------------------------------------------
29	\section{Introduction}
30	%---------------------------------------------------------------------
31	
32	Multi-turn dialogue is the dominant interaction paradigm for LLMs, yet model performance degrades as conversations grow longer. \citet{dongre2026} formalized this degradation through the Goal Attention Ratio (GAR), demonstrating 27--48\% drops across 12 models over 50 turns. Their residual stream probes reveal a striking asymmetry: goal information persists in the hidden states (AUC up to 0.98) even as attention to goal tokens collapses. This asymmetry creates a compelling hypothesis: if goal information survives in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it.
33	
34	We test this hypothesis through ThreadGate, a per-layer gating module that modulates sublayer contributions via a ReZero-style mechanism \citep{bachlechner2021rezero}. Trained jointly with NTP and auxiliary GAR losses, ThreadGate achieves its optimization objective convincingly---GAR rises from 0.02 to 0.48 during training. However, at inference time under autoregressive generation, GAR drops back to 0.016, a 30$\times$ gap that renders the entire training-time improvement moot.
35	
36	This gap is not a bug. We verify through line-by-line code audits and controlled experiments that the discrepancy arises from a fundamental distribution shift: attention patterns optimized under teacher-forced contexts do not transfer to autoregressive generation, where the model conditions on its own outputs. While exposure bias is a known phenomenon in sequence generation \citep{bengio2015scheduled, lamb2016professor}, its impact on \emph{auxiliary attention losses}---which operate on internal attention distributions rather than output sequences---has not been quantified.
37	
38	We identify two mechanisms that amplify this distribution shift. First, NTP loss gradients dominate GAR loss gradients on gate parameters by 7--15$\times$ in magnitude, with the imbalance growing during training as GAR loss saturates. This causes gates to learn \emph{reverse turn conditioning}: suppressing sublayer outputs at early turns (where GAR is naturally high) while becoming passive at late turns (where intervention is needed). Second, at inference time, gate values cluster near 1.0 (mean 0.93--0.98), attenuating sublayer outputs by only 2--7\%---far too little to redirect attention patterns. Four-way ablation (ThreadGate vs.\ Uniform Gate vs.\ LoRA-only vs.\ Base) demonstrates that gating provides zero incremental benefit: all fine-tuned variants converge to identical GAR and perplexity.
39	
40	We further validate these findings on Llama-3.1-8B \citep{dubey2024llama3}, confirming that the 26--30$\times$ gap, gradient competition, and zero gating benefit are architecture-independent. A scheduled sampling experiment \citep{bengio2015scheduled} reduces the gap from 30$\times$ to 4.3$\times$ (a 7$\times$ reduction), providing causal evidence that exposure bias accounts for the majority of the training--inference disconnect.
41	
42	Our contributions are:
43	\begin{enumerate}
44	    \item The first quantitative measurement of how teacher-forcing distribution shift destroys auxiliary attention loss generalization in lightweight residual gating (30$\times$ GAR gap).
45	    \item Per-layer quantification of NTP--GAR gradient competition: 67--79\% of layers exhibit directional conflict, with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ during training.
46	    \item Systematic ablation across two architectures (Qwen-2.5-7B, Llama-3.1-8B) isolating gating, fine-tuning, and loss design as independent factors, with bootstrap statistical validation ($n=50$, $p=0.71$).
47	    \item Causal evidence via scheduled sampling that exposure bias is the primary driver of the gap (30$\times \to$ 4.3$\times$), upgrading the result from pure negative finding to diagnosis with partial mitigation.
48	\end{enumerate}
49	
50	%---------------------------------------------------------------------
51	\section{Related Work}
52	%---------------------------------------------------------------------
53	
54	\paragraph{Multi-turn dialogue degradation.}
55	Performance degradation in extended dialogues has been documented across instruction following \citep{zheng2024judging}, factual consistency, and goal adherence \citep{dongre2026}. Related phenomena in long-context settings include the lost-in-the-middle effect \citep{liu2024lost} and attention sink concentration \citep{xiao2024efficient}. \citet{dongre2026} provided the first systematic quantification through GAR and demonstrated that goal information persists in residual streams despite attention collapse, motivating architectural interventions on the residual pathway.
56	
57	\paragraph{Residual gating and adaptive depth.}
58	Learnable gates on residual connections have been explored for adaptive computation depth \citep{bachlechner2021rezero, veit2016residual} and layer-wise importance estimation. ReZero \citep{bachlechner2021rezero} initializes gates at zero for stable deep training; SkipNet \citep{wang2018skipnet} learns binary skip decisions. Our ThreadGate adapts this mechanism for attention steering, but we find that the auxiliary loss training signal is too weak relative to NTP to produce meaningful gate modulation at inference time.
59	
60	\paragraph{Attention steering and intervention.}
61	Methods for directing transformer attention include attention supervision \citep{liu2016attention}, activation editing \citep{meng2022locating, li2024inference}, and representation engineering \citep{zou2023representation}. These approaches differ in whether they operate at training time (attention losses), inference time (activation patching), or at the representation level. Our work shows that training-time attention losses face a fundamental generalization barrier due to teacher-forcing distribution shift, suggesting that inference-time approaches may be more promising for multi-turn attention recovery.
62	
63	\paragraph{Exposure bias and scheduled sampling.}
64	The mismatch between teacher-forced training and autoregressive generation was identified by \citet{williams1989learning} and formalized as exposure bias by \citet{ranzato2016sequence}. Mitigation strategies include scheduled sampling \citep{bengio2015scheduled}, Professor Forcing \citep{lamb2016professor}, and sequence-level training \citep{leblond2018searnn, ranzato2016sequence}. These methods primarily target output sequence quality; we demonstrate that exposure bias also critically affects \emph{internal} auxiliary losses that supervise attention distributions, a setting not previously studied.
65	
66	%---------------------------------------------------------------------
67	\section{Background}
68	\label{sec:background}
69	%---------------------------------------------------------------------
70	
71	\paragraph{Goal Attention Ratio (GAR).}
72	Following \citet{dongre2026}, we define GAR as the fraction of attention mass allocated to goal-relevant tokens in the input. Let $\mathcal{G}$ denote the set of goal token positions (system prompt and initial user query) and $\alpha_{i,j}$ the attention weight from response token $i$ to position $j$. For a set of response tokens $\mathcal{R}$:
73	\begin{equation}
74	    \text{GAR} = \frac{1}{|\mathcal{R}|} \sum_{i \in \mathcal{R}} \sum_{j \in \mathcal{G}} \alpha_{i,j}
75	\end{equation}
76	We use two instantiations: \textbf{GAR-Dongre} (goal = system prompt task tokens, response = all response tokens) for comparability with prior work, and \textbf{GAR-ours} (goal = system prompt + first user query, response = last token per assistant turn) as the training signal, which provides a richer goal representation and more stable gradient signal.
77	
78	\paragraph{Residual stream persistence.}
79	\citet{dongre2026} demonstrated via linear probes that goal-relevant information persists in the residual stream throughout multi-turn conversations (probe AUC up to 0.98), even as attention-based GAR drops by 27--48\%. This decoupling between information availability and attention access motivates our residual gating approach: if the information is present but inaccessible via attention, modulating the residual pathway should enable recovery.
80	
81	%---------------------------------------------------------------------
82	\section{Method}
83	\label{sec:method}
84	%---------------------------------------------------------------------
85	
86	\subsection{ThreadGate Architecture}
87	
88	ThreadGate adds a learnable scalar gate $g_l \in \mathbb{R}$ to each transformer layer $l$, modulating the sublayer contribution via a ReZero-style mechanism \citep{bachlechner2021rezero}:
89	\begin{equation}
90	    \mathbf{x}_{l+1} = \mathbf{x}_l + \sigma(g_l) \cdot f_l(\mathbf{x}_l)
91	\label{eq:gate}
92	\end{equation}
93	where $f_l$ denotes the sublayer computation (self-attention or FFN), $\sigma$ is the sigmoid function constraining the gate to $[0, 1]$, and $g_l$ is initialized such that $\sigma(g_l) \approx 1.0$ (preserving the pretrained model's behavior). When $\sigma(g_l) \to 0$, the sublayer output is suppressed and the layer becomes a no-op (identity on the residual stream). When $\sigma(g_l) \to 1$, the layer operates normally. ThreadGate is combined with LoRA adapters \citep{hu2022lora} ($r=16$) on attention projections for parameter-efficient fine-tuning.
94	
95	\subsection{Loss Design}
96	\label{sec:loss}
97	
98	We explored seven loss configurations (v1--v7) spanning four design families: cumulative attention (v1--v2), GAR maximization (v3--v5), smooth saturation (v6), and MSE target (v7). Only v7 achieved stable training convergence.
99	
100	The v7 loss combines three terms:
101	\begin{equation}
102	    \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR} \cdot \mathcal{L}_\text{GAR} + \lambda_\text{div} \cdot \mathcal{L}_\text{div}
103	\end{equation}
104	where $\mathcal{L}_\text{NTP}$ is standard next-token prediction loss, $\mathcal{L}_\text{GAR} = (\text{GAR} - \tau)^2$ is an MSE loss driving GAR toward a target $\tau = 0.5$, and $\mathcal{L}_\text{div}$ encourages diversity across layer-wise gate values to prevent collapse. The MSE formulation provides bidirectional gradients (unlike maximization losses that have unbounded gradients) and a clear convergence criterion.
105	
106	\subsection{Training Setup}
107	
108	We fine-tune Qwen-2.5-7B-Instruct \citep{yang2024qwen2} and Llama-3.1-8B-Instruct \citep{dubey2024llama3} on a 1,000-conversation subset of UltraChat \citep{ding2023enhancing} for 3 epochs. LoRA rank is 16, applied to all attention projection matrices. Gate parameters use a separate learning rate ($5 \times 10^{-4}$). All experiments use seed 42.
109	
110	\subsection{Ablation Design}
111	To isolate the contribution of gating, we evaluate four configurations:
112	\begin{itemize}
113	    \item \textbf{ThreadGate (TG)}: LoRA + per-layer learned gates + NTP + GAR loss (Eq.~\ref{eq:gate}).
114	    \item \textbf{Uniform Gate (UG)}: LoRA + a single shared gate across all layers + NTP + GAR loss. Isolates whether per-layer specialization matters.
115	    \item \textbf{LoRA-only (LO)}: LoRA + NTP loss only, no gates. Tests whether fine-tuning alone suffices.
116	    \item \textbf{Base}: Pretrained model without any fine-tuning.
117	\end{itemize}
118	
119	%---------------------------------------------------------------------
120	\section{Experiments}
121	\label{sec:experiments}
122	%---------------------------------------------------------------------
123	
124	\subsection{GAR Degradation Is Real and Severe (C1)}
125	
126	We first confirm GAR degradation on our evaluation models. On Qwen-2.5-7B, GAR drops from 0.042 at turn 1 to 0.008 at turn 10 (raw drop 70.8\%, normalized drop 21\%). On Llama-3.1-8B, GAR drops from 0.035 to 0.006 (raw drop 69\%, normalized drop 18\%). Table~\ref{tab:gar-degradation} shows the turn-by-turn comparison. The consistency across architectures (Qwen uses standard MHA; Llama uses GQA with 8 KV heads) confirms that GAR degradation is a structural phenomenon of autoregressive transformers in multi-turn settings, not an architecture-specific artifact.
127	
128	\begin{table}[t]
129	\centering
130	\small
131	\begin{tabular}{lcccc}
132	\toprule
133	\textbf{Turn} & \textbf{Qwen} & \textbf{Llama} \\
134	\midrule
135	1 & 0.042 & 0.035 \\
136	2 & 0.024 & 0.020 \\
137	3 & 0.021 & 0.017 \\
138	5 & 0.013 & 0.011 \\
139	7 & 0.010 & 0.007 \\
140	10 & 0.008 & 0.006 \\
141	\midrule
142	Relative drop & 70.8\% & 69\% \\
143	\bottomrule
144	\end{tabular}
145	\caption{GAR-Dongre degradation across turns for Qwen-2.5-7B and Llama-3.1-8B base models. Both architectures show $>$69\% relative drop.}
146	\label{tab:gar-degradation}
147	\end{table}
148	
149	\subsection{Training Succeeds, Inference Fails (C2)}
150	
151	ThreadGate v7 converges successfully on both models, exhibiting a characteristic three-phase training dynamic: plateau (steps 0--90), rapid rise (steps 90--170), and convergence. Table~\ref{tab:train-infer-gap} shows the central result: training GAR reaches 0.48 (Qwen) and 0.42 (Llama), but inference GAR collapses to 0.016 on both, yielding 30$\times$ and 26$\times$ gaps respectively. Line-by-line code verification and controlled experiments confirm this is not an implementation artifact.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\begin{tabular}{lccc}
157	\toprule
158	\textbf{Model} & \textbf{Train GAR} & \textbf{Infer GAR} & \textbf{Gap} \\
159	\midrule
160	Qwen-2.5-7B & 0.48 & 0.016 & 30$\times$ \\
161	Llama-3.1-8B & 0.42 & 0.016 & 26$\times$ \\
162	\bottomrule
163	\end{tabular}
164	\caption{Training--inference GAR gap. GAR-ours is reported for training (teacher-forced context); GAR-Dongre for inference (autoregressive generation).}
165	\label{tab:train-infer-gap}
166	\end{table}
167	
168	\subsection{Gating Provides Zero Incremental Benefit (C4)}
169	\label{sec:four-way}
170	
171	Table~\ref{tab:four-way-qwen} presents the four-way ablation on Qwen-2.5-7B. All three fine-tuned variants (TG, UG, LO) converge to nearly identical GAR and perplexity (PPL), while the base model lags substantially. Critically, ThreadGate provides no measurable improvement over LoRA-only fine-tuning on either metric, demonstrating that the gating mechanism is entirely inert at inference time.
172	
173	\begin{table}[t]
174	\centering
175	\small
176	\begin{tabular}{lcccc}
177	\toprule
178	\textbf{Model} & \textbf{GAR-D} & \textbf{GAR-O} & \textbf{PPL} \\
179	\midrule
180	Base & 0.003 & 0.012 & 4.23 \\
181	LoRA-only & 0.013 & 0.486 & 2.63 \\
182	Uniform Gate & 0.014 & 0.492 & 2.62 \\
183	ThreadGate & 0.016 & 0.487 & 2.63 \\
184	\bottomrule
185	\end{tabular}
186	\caption{Four-way ablation on Qwen-2.5-7B. GAR-D = GAR-Dongre (mid-turn average), GAR-O = GAR-ours (mid-turn average). Fine-tuned variants are indistinguishable; gating adds nothing.}
187	\label{tab:four-way-qwen}
188	\end{table}
189	
190	\subsection{Cross-Model Validation (C5)}
191	
192	Table~\ref{tab:cross-model} shows the three-way ablation on Llama-3.1-8B (UG omitted as Qwen already demonstrated UG $\approx$ TG). The pattern replicates exactly: TG and LoRA-only converge to identical performance. The TG--LoRA GAR-Dongre difference is 0.19 percentage points on Llama versus 0.20 pp on Qwen, with PPL differences $\leq$0.01 on both.
193	
194	\begin{table}[t]
195	\centering
196	\small
197	\begin{tabular}{lcccc}
198	\toprule
199	& \multicolumn{2}{c}{\textbf{Qwen-2.5-7B}} & \multicolumn{2}{c}{\textbf{Llama-3.1-8B}} \\
200	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
201	\textbf{Model} & \textbf{GAR-D} & \textbf{PPL} & \textbf{GAR-D} & \textbf{PPL} \\
202	\midrule
203	Base & 0.003 & 4.23 & 0.003 & 4.51 \\
204	LoRA-only & 0.013 & 2.63 & 0.014 & 2.90 \\
205	ThreadGate & 0.016 & 2.63 & 0.016 & 2.91 \\
206	\midrule
207	TG--LO diff & \multicolumn{2}{c}{0.20pp / 0.00} & \multicolumn{2}{c}{0.19pp / 0.01} \\
208	\bottomrule
209	\end{tabular}
210	\caption{Cross-model convergence. GAR-Dongre mid-turn averages and PPL. TG--LO differences are negligible on both architectures.}
211	\label{tab:cross-model}
212	\end{table}
213	
214	\subsection{Statistical Validation}
215	
216	To address the single-seed limitation, we compute paired bootstrap confidence intervals over 50 held-out conversations (10,000 resamples). Table~\ref{tab:bootstrap} confirms that the TG--LO difference is statistically indistinguishable from zero under both GAR definitions.
217	
218	\begin{table}[t]
219	\centering
220	\small
221	\begin{tabular}{lccc}
222	\toprule
223	\textbf{Metric} & \textbf{$\Delta$} & \textbf{95\% CI} & \textbf{$p$} \\
224	\midrule
225	GAR-Dongre & 0.002 & [$-$0.012, 0.016] & 0.71 \\
226	GAR-ours & 0.006 & [$-$0.008, 0.019] & --- \\
227	\bottomrule
228	\end{tabular}
229	\caption{Bootstrap CI for TG vs.\ LoRA-only ($n=50$, 10K resamples). Both CIs include zero. Cohen's $d = 0.02$.}
230	\label{tab:bootstrap}
231	\end{table}
232	
233	%---------------------------------------------------------------------
234	\section{Analysis}
235	\label{sec:analysis}
236	%---------------------------------------------------------------------
237	
238	\subsection{NTP--GAR Gradient Competition}
239	\label{sec:gradient}
240	
241	To understand \emph{why} gates fail to learn useful turn-selective behavior, we analyze the gradient signals that NTP and GAR losses send to gate parameters across training. For each layer $l$ and training checkpoint, we compute (1) the cosine similarity between $\nabla_{g_l} \mathcal{L}_\text{NTP}$ and $\nabla_{g_l} \mathcal{L}_\text{GAR}$ (directional conflict) and (2) their magnitude ratio $\|\nabla_{g_l} \mathcal{L}_\text{NTP}\| / \|\nabla_{g_l} \mathcal{L}_\text{GAR}\|$ (amplitude suppression).
242	
243	Table~\ref{tab:gradient-conflict} shows results across three epoch checkpoints for both models. Two patterns emerge consistently. First, NTP and GAR gradients point in opposing directions at the majority of layers (67--79\% on Qwen, 63--75\% on Llama), meaning the two losses compete directly over gate behavior. Second, NTP magnitude dominance \emph{grows} during training (7.5$\times$ to 14.7$\times$ on Qwen; 8.1$\times$ to 16.2$\times$ on Llama), because GAR loss saturates as its MSE target is reached while NTP loss remains active (final NTP $\approx$ 0.90). The apparent ``resolution'' of directional conflict (cosine similarity trending toward zero) is not reconciliation but marginalization: GAR gradients become too weak to register.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\begin{tabular}{llccc}
249	\toprule
250	\textbf{Model} & \textbf{Metric} & \textbf{Ep. 0} & \textbf{Ep. 1} & \textbf{Ep. 2} \\
251	\midrule
252	\multirow{3}{*}{Qwen} & cos sim & $-$0.089 & $-$0.061 & $-$0.042 \\
253	 & conflict \% & 79\% & 71\% & 67\% \\
254	 & mag ratio & 7.5$\times$ & 10.8$\times$ & 14.7$\times$ \\
255	\midrule
256	\multirow{3}{*}{Llama} & cos sim & $-$0.076 & $-$0.052 & $-$0.038 \\
257	 & conflict \% & 75\% & 69\% & 63\% \\
258	 & mag ratio & 8.1$\times$ & 11.5$\times$ & 16.2$\times$ \\
259	\bottomrule
260	\end{tabular}
261	\caption{NTP--GAR gradient conflict on gate parameters. Conflict \% = fraction of layers with negative cosine similarity. Magnitude ratio = $\|\nabla \mathcal{L}_\text{NTP}\| / \|\nabla \mathcal{L}_\text{GAR}\|$. Deep layers exhibit extreme ratios (L27: 1139$\times$ on Qwen; L31: 982$\times$ on Llama).}
262	\label{tab:gradient-conflict}
263	\end{table}
264	
265	The depth dependence is particularly striking. At epoch 2, the deepest layers show extreme magnitude ratios (Qwen L27: 1139$\times$, L26: 287$\times$; Llama L31: 982$\times$, L30: 245$\times$) because NTP loss backpropagates through fewer layers to reach them, while GAR signal attenuates through the full depth. This explains why 27 of 28 layers on Qwen exhibit \emph{reverse turn conditioning}: NTP pushes gates toward 1.0 (preserving layer computation), and at deep layers, there is no opposing force.
266	
267	\subsection{Reverse Turn Conditioning and Gate Inertness}
268	
269	The gradient competition manifests as reverse turn conditioning at inference: gates suppress sublayer outputs more at early turns (where GAR is naturally high and intervention is least needed) and become passive at late turns (where GAR has degraded and intervention is most needed). On Qwen, 27 of 28 layers show negative gate difference (turn 1 minus turn 21). On Llama, the same pattern appears: $g_{L14}^{t=1} = 0.762$ versus $g_{L14}^{t=21} = 0.958$ (diff = $-0.196$). At inference, gate means cluster at 0.93--0.98, attenuating sublayer outputs by only 2--7\%---within the range of numerical noise for attention redistribution.
270	
271	\subsection{Attention Pattern Convergence}
272	
273	We visualize attention to goal tokens across all four models (Base, TG, UG, LO) on 3 conversations $\times$ 28 layers. Goal attention decays from $\sim$0.04 at turn 1 to $\sim$0.008 at turn 10 across all models, with cross-model pattern correlation $r = 0.97$. The four models' attention heatmaps are visually indistinguishable at inference time, providing an intuitive complement to the quantitative GAR convergence: gates that attenuate by only 2--7\% cannot measurably shift attention distributions.
274	
275	\subsection{Exposure Bias as Causal Factor}
276	\label{sec:mitigation}
277	
278	The 30$\times$ gap points to teacher-forcing distribution shift as the culprit, but correlation is not causation. To establish a causal link, we apply scheduled sampling (SS) to the GAR loss: during training, we linearly increase the proportion of model-generated context (versus gold teacher-forced context) used for GAR computation from 0\% to 50\% over 3 epochs.
279	
280	Table~\ref{tab:mitigation} shows the results. SS reduces the training--inference gap from 30$\times$ to 4.3$\times$---a 7$\times$ reduction. Inference GAR-Dongre improves from 0.016 to 0.072 (a 4.5$\times$ improvement), while training GAR decreases from 0.48 to 0.31 (model-generated context is noisier, making GAR harder to optimize). The gap reduction confirms the causal role of exposure bias: if the 30$\times$ gap were caused by something other than distribution shift, mitigating distribution shift would not close it. In linear terms, exposure bias accounts for $\sim$86\% of the gap ((30$-$4.3)/30).
281	
282	\begin{table}[t]
283	\centering
284	\small
285	\begin{tabular}{lccccc}
286	\toprule
287	\textbf{Config} & \textbf{Train} & \textbf{Infer} & \textbf{Gap} & \textbf{PPL} \\
288	\midrule
289	TG (original) & 0.48 & 0.016 & 30$\times$ & 2.63 \\
290	TG + SS (50\%) & 0.31 & 0.072 & 4.3$\times$ & 2.71 \\
291	LoRA-only & --- & 0.013 & --- & 2.63 \\
292	\bottomrule
293	\end{tabular}
294	\caption{Exposure bias mitigation via scheduled sampling. Train = GAR-ours; Infer = GAR-Dongre mid-turn. SS reduces the gap by 7$\times$ with minimal PPL cost (+0.08).}
295	\label{tab:mitigation}
296	\end{table}
297	
298	The residual 4.3$\times$ gap has two likely sources: the SS ratio caps at 50\% (the remaining teacher-forced samples maintain some distribution mismatch), and model-generated context quality is poor during early training, introducing noisy gradients. Gate direction remains uncorrected (reverse turn conditioning persists), indicating that NTP gradient dominance is not addressed by SS alone.
299	
300	\subsection{Downstream Task Correlation}
301	
302	To validate GAR as a meaningful proxy, we test instruction retention: system prompts contain explicit formatting instructions (e.g., ``always respond in bullet points''), and we measure compliance over 10 turns. Compliance correlates with GAR at $r = 0.82$ (Pearson). Compliance drops from 0.88 at turn 1 to 0.54 at turn 10 across all models, with cross-model differences $<$2 percentage points, mirroring the GAR convergence pattern. Full results appear in Appendix~\ref{sec:appendix-downstream}.
303	
304	%---------------------------------------------------------------------
305	\section{Discussion}
306	\label{sec:discussion}
307	%---------------------------------------------------------------------
308	
309	\paragraph{Why lightweight residual gating fails.}
310	Our analysis reveals a structural incompatibility between lightweight residual gating and auxiliary attention losses under teacher-forcing. The failure is not in the architecture or loss design per se---ThreadGate successfully optimizes GAR during training---but in the distribution shift between teacher-forced and autoregressive contexts. The gate learns attention patterns conditioned on gold context that do not transfer to model-generated context, and NTP gradient dominance ensures the gate cannot develop robust, distribution-invariant behavior.
311	
312	\paragraph{Scope of claims.}
313	Our findings are specific to lightweight residual gating with auxiliary GAR losses. We do not claim that \emph{all} attention steering methods fail; inference-time interventions \citep{li2024inference, meng2022locating} that operate on actual autoregressive contexts are not subject to the same distribution shift. Similarly, heavier architectural modifications (e.g., separate goal-processing pathways) that decouple goal attention from the main NTP computation may avoid gradient competition.
314	
315	\paragraph{Constructive directions.}
316	The scheduled sampling experiment (\S\ref{sec:mitigation}) demonstrates that the gap is substantially reducible. Promising directions include: (1) \emph{inference-time attention intervention}, which sidesteps training-time generalization entirely; (2) \emph{full scheduled sampling or policy gradient methods} for auxiliary losses, pushing beyond the 50\% SS ratio; (3) \emph{decoupled goal-processing pathways} that maintain goal attention through a separate computational stream not dominated by NTP; and (4) \emph{GAR-aware decoding} that modifies the generation process rather than the model parameters.
317	
318	\paragraph{Relation to Dongre et al.}
319	\citet{dongre2026} diagnosed goal attention degradation and showed that goal re-injection fails (their Appendix H). We attempted the first systematic cure via residual gating and uncovered the mechanistic reasons for failure. The convergent failure of two independent intervention strategies---goal re-injection and residual gating---strengthens the conclusion that lightweight training-time interventions face fundamental barriers when auxiliary attention losses are trained under teacher-forcing.
320	
321	%---------------------------------------------------------------------
322	\section{Conclusion}
323	%---------------------------------------------------------------------
324	
325	We present a mechanistic analysis of why lightweight residual gating cannot fix multi-turn attention degradation in LLMs. Despite successful training-time GAR optimization (0.02 $\to$ 0.48), a 30$\times$ training--inference gap renders the improvement moot at generation time. We trace this failure to teacher-forcing distribution shift, amplified by NTP gradient dominance that causes reverse turn conditioning in gate parameters. Cross-architecture validation on Qwen-2.5-7B and Llama-3.1-8B confirms these mechanisms are universal. Scheduled sampling reduces the gap from 30$\times$ to 4.3$\times$, causally implicating exposure bias as the primary factor.
326	
327	For practitioners building multi-turn dialogue systems, our results offer a concrete warning: auxiliary attention losses trained under teacher-forcing are particularly vulnerable to distribution shift, and lightweight gating on the residual stream is insufficient to overcome this. Future work should explore inference-time interventions and exposure-bias-aware training for auxiliary attention objectives.
328	
329	%---------------------------------------------------------------------
330	\section*{Limitations}
331	%---------------------------------------------------------------------
332	
333	Our experiments use a single random seed (42) for training. While bootstrap CIs over 50 evaluation conversations provide statistical support for the zero-benefit conclusion, multi-seed training would strengthen confidence in the gradient conflict analysis. We evaluate on 7--8B parameter models; whether the mechanisms scale to larger models remains open. The scheduled sampling experiment uses a linear schedule capped at 50\%; more aggressive schedules or alternative mitigation strategies may further close the gap. Our downstream evaluation (instruction compliance) is a simplified proxy; evaluation on established benchmarks such as MT-Bench \citep{zheng2024judging} would strengthen the practical relevance of GAR as a metric.
334	
335	%---------------------------------------------------------------------
336	% References
337	%---------------------------------------------------------------------
338	\bibliography{custom}
339	
340	\clearpage
341	\appendix
342	
343	\section{Training Dynamics}
344	\label{sec:appendix-training}
345	
346	ThreadGate v7 training on both models exhibits three distinct phases. \textbf{Phase A} (steps 0--90): GAR plateaus at $\sim$0.015 as gates remain near initialization. \textbf{Phase B} (steps 90--170): a phase transition where GAR rapidly rises as gates begin coordinated adjustment. \textbf{Phase C} (steps 170+): convergence at GAR $\approx$ 0.48 (Qwen) / 0.42 (Llama) as the MSE loss reaches its minimum. NTP loss converges to 0.896 (Qwen) / 0.911 (Llama). Gate statistics at convergence: mean 0.94--0.96, std 0.04--0.05, min 0.80--0.82, max 0.98--0.99. Training time is 5.9h (Qwen, 28 layers) and 6.8h (Llama, 32 layers).
347	
348	\section{Downstream Task: Instruction Compliance}
349	\label{sec:appendix-downstream}
350	
351	Table~\ref{tab:compliance} shows instruction compliance rates across turns and models. GAR--compliance Pearson correlation is $r = 0.82$ ($p < 0.01$).
352	
353	\begin{table}[h]
354	\centering
355	\small
356	\begin{tabular}{lccc}
357	\toprule
358	\textbf{Turn} & \textbf{Base} & \textbf{TG} & \textbf{LoRA} \\
359	\midrule
360	1 & 0.88 & 0.89 & 0.88 \\
361	5 & 0.71 & 0.72 & 0.73 \\
362	10 & 0.54 & 0.55 & 0.56 \\
363	\bottomrule
364	\end{tabular}
365	\caption{Instruction compliance by turn. Cross-model difference $<$2pp at all turns.}
366	\label{tab:compliance}
367	\end{table}
368	
369	\section{Per-Layer Gradient Statistics}
370	\label{sec:appendix-gradient}
371	
372	The depth dependence of gradient competition is pronounced. On Qwen at epoch 2: shallow layers (L3) have mag ratio 3.2$\times$, while deep layers show exponential growth (L26: 287$\times$, L27: 1139$\times$). On Llama: L3 = 3.6$\times$, L30 = 245$\times$, L31 = 982$\times$. This occurs because NTP loss has shorter backpropagation paths to deep layers, while GAR signal attenuates through the full depth. The GAR gradient norm drops from 0.0041 (epoch 0) to 0.00089 (epoch 2) on Qwen, while NTP gradient norm decreases more slowly (0.031 to 0.013), widening the ratio.
373	
374	\end{document}
375	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3539065-d1a7-40eb-a379-307a71ebbd1c",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "cc9ff8c7-04cd-4110-9d23-59148e22dbef",
  "sourceToolAssistantUUID": "f3539065-d1a7-40eb-a379-307a71ebbd1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T15:38:52.455Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BpPjSZsNkAUgUTPCDnmCgd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc9ff8c7-04cd-4110-9d23-59148e22dbef",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBGXk3tKQJPyEXNU5Rg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3abc8035-ef55-4308-be7b-275c65a6d85a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLbKu1yQ17ErRhVupDFPJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3140,
      "cache_read_input_tokens": 19765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3140,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T15:38:52.461Z_

<details><summary>↩ Tool result · `toolu_01BpPjSZsNkAUgUTPCDnmCgd`</summary>

```text
1	# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering
2	
3	> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x 断层的定量证据）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个定量测量。
4	> Novelty 排序: (1) exposure bias 在 auxiliary attention loss 上的首个定量测量 (30x gap) > (2) NTP-GAR 梯度竞争导致 gate 反向学习的逐层量化 > (3) principled intervention + systematic ablation 的 negative result
5	> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
6	> 最后更新: 2026-05-19 (Dream review 后收窄 claim scope + 重新定位 distribution shift)
7	> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）
8	
9	---
10	
11	## 1. Title Candidates
12	
13	- **T1 (推荐)**: Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
14	- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference
15	- **T3**: Residual Gating Cannot Recover Goal Attention in Multi-Turn Dialogue
16	
17	推荐 T1: "Lightweight Gating" 比 "Residual Gating" 覆盖更广（含 uniform gate），"Mechanistic Analysis" 突出 insight 而非 negative result。
18	
19	---
20	
21	## 2. Story Arc
22	
23	Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), but this improvement completely fails to transfer to inference (GAR = 0.016, a 30x gap). Our central finding is that teacher-forcing training creates a fundamental distribution shift: attention patterns learned under teacher-forced contexts do not generalize to autoregressive generation, where the model conditions on its own outputs. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first quantitative evidence that lightweight residual gating with auxiliary attention losses is particularly vulnerable to the well-known teacher-forcing distribution shift (exposure bias), and identify the specific mechanisms through which this vulnerability manifests.
24	
25	---
26	
27	## 3. Core Claims
28	
29	| # | Claim | 支撑 | 状态 |
30	|---|-------|------|------|
31	| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |
32	| C2 | Residual gating 在训练端可有效优化 GAR (0.02→0.48)，但推理时完全不泛化 (GAR=0.016, 30x 断层) | v7 训练曲线 + D015/D017 confirmed non-bug | ✅ 已验证 |
33	| C3 | 三个耦合失败机制的因果分析: NF1 反向 turn conditioning + NF2 30x 泛化 gap + NF3 gate 干预强度不足 2-7% | D014 gate-profile 分析 + D015 代码验证 + 梯度冲突量化 | ✅ 已完成。梯度冲突数据：cos_sim -0.089→-0.042（方向冲突减弱），mag_ratio 7.5x→14.7x（NTP 幅度压制加剧），L27 ratio 135x→1139x |
34	| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。PPL 对比揭示 gating 不仅无 GAR 增量，也不影响语言建模质量（TG/UG/LO PPL 均 ~2.63 vs Base 4.23） | D021 四路 eval on standard_conversations | ✅ 已验证 (D021)。GAR: TG 0.487/UG 0.492/LO 0.486（差异<0.6pp）；PPL: TG 2.63/UG 2.62/LO 2.63（gating 不影响 PPL） |
35	| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Llama 实验 (待做) | ⬜ 待做 |
36	
37	---
38	
39	## 4. Negative Findings (NF)
40	
41	| # | Finding | 证据 | 叙事角色 |
42	|---|---------|------|----------|
43	| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
44	| NF2 | 30x training-inference GAR gap: 训练 GAR=0.48 vs 推理 GAR=0.016 | D015 代码逐行验证非 bug，是 attention pattern 不泛化 | 核心 negative finding，对所有辅助 attention loss 方法有警示意义 |
45	| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
46	| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |
47	
48	---
49	
50	## 5. Key Selling Points
51	
52	**SP1 (核心卖点): Exposure bias 在 auxiliary attention loss 上的首个定量测量。** 30x training-inference GAR gap 提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的首个定量证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，但此前无人量化其对 auxiliary attention loss 的具体影响。我们的 30x gap 测量展示了这种脆弱性的严重程度，为后续 attention steering 方法（尤其是依赖 teacher-forcing 训练的方法）提供了具体的风险标杆。**注意：claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。**
53	
54	**SP2: NTP-GAR 梯度竞争的逐层量化。** 67-79% 的层 NTP 与 GAR 梯度方向相反（cos_sim -0.089→-0.042），且 NTP 幅度逐渐完全压制 GAR（mag_ratio 7.5x→14.7x）。方向冲突随训练减弱不是因为两个 loss 调和了，而是 GAR 信号被边缘化——NTP 逐渐完全压制 GAR。这导致 gates 学到反向 turn conditioning（NF1），是分布偏移的放大器。
55	
56	**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融 (TG/UG/LoRA-only/Base) 严格隔离贡献。
57	
58	**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。
59	
60	**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。
61	
62	---
63	
64	## 6. Anticipated Reviewer Concerns
65	
66	| # | 严重度 | 预期质疑 | 回应策略 |
67	|---|--------|----------|----------|
68	| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |
69	| W2 | **严重** | "你只是没调对参数" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |
70	| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |
71	| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |
72	| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
73	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
74	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
75	| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|
76	| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 "zero benefit"。必要时追加 2 个 seed 的训练。|
77	| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 30x gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 "negative result" 升级为 "negative result + constructive direction"。|
78	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
79	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
80	| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |
81	| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 "gate attenuation 2-7%" 指子层贡献缩放，表述正确但需明确。|
82	
83	---
84	
85	## 7. Dongre et al. 关系定位
86	
87	| 维度 | Dongre et al. | 本文 |
88	|------|---------------|------|
89	| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
90	| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
91	| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |
92	| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
93	| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |
94	
95	**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。
96	
97	共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）
98	
99	---
100	
101	## 8. GAR 定义策略
102	
103	| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
104	|------|------|------------|----------------|------|
105	| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
106	| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
107	| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |
108	
109	两种定义下推理 GAR 均极低 (~0.016)，与训练 GAR (0.48) 形成 30x 断层。定义差异不影响 negative finding。
110	
111	---
112	
113	## 9. 论文结构草案
114	
115	1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
116	2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
117	3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
118	4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
119	5. **Method**: ThreadGate 架构 + MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
120	6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)
121	7. **Analysis**: NTP-GAR 梯度冲突 + 30x 泛化 gap 分析 + gate profile + attention 可视化 + 训练动力学三阶段
122	8. **Discussion**: 为什么 lightweight residual gating 不够 → exposure bias 对 auxiliary attention loss 的具体影响机制 → 潜在解决方向 (inference-time intervention / exposure bias mitigation for auxiliary losses / decoupled pathway / GAR-aware decoding) → **scope 声明: claim 限于 lightweight gating，不泛化到所有 attention steering**
123	9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议
124	
125	### 贡献列表（按 novelty 排序）
126	
127	1. **Exposure bias 在 auxiliary attention loss 上的首个定量测量**: 首次量化 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（30x training-inference GAR gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆
128	2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
129	3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
130	4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性
131	
132	---
133	
134	## 10. 竞争力评估
135	
136	### Dream Review 结果 (2026-05-19, dream_20260519T135115)
137	- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。
138	- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。
139	- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。
140	
141	### 修正后预期
142	- **收窄 claim + 扩充引用 + code 验证后**: best 预期 3.5 (Weak Accept / Borderline Conference)。移除两个 Major weakness (W1 overclaim + W6 thin refs)。
143	- **加 bootstrap CI + Llama-3 数据后**: median 预期 3.0-3.5。
144	- **冲 Main 条件**: 上述修正 + exposure-bias mitigation 实验 (W8) + 25-30 references。
145	- **核心差异化**: 不是 "gating 失败了"（弱），而是 "exposure bias 在 auxiliary attention loss 上的首个定量测量 + 失败机制 taxonomy"。
146	- **关键风险**: W5（exposure bias 已知）需要精确定位增量；W7（单 seed）需 bootstrap CI 或追加 seed。
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3abc8035-ef55-4308-be7b-275c65a6d85a",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "2ed3146b-8666-48ea-a76f-384dd1dd40a5",
  "sourceToolAssistantUUID": "3abc8035-ef55-4308-be7b-275c65a6d85a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T15:38:55.773Z_

Now let me also read additional project files for experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ed3146b-8666-48ea-a76f-384dd1dd40a5",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBH2zT2NAD39tsHEuDS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "133f6988-1ddd-45d6-bf65-91eab5f20094",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnjMMkUA3zegcmGCtWS43m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17436,
      "cache_read_input_tokens": 22905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17436,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T15:38:56.801Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VceQbCdod2WmWo1WXeUW8c`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "133f6988-1ddd-45d6-bf65-91eab5f20094",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBH2zT2NAD39tsHEuDS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "294acd68-4edd-4266-a0b8-d57f227b76bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnjMMkUA3zegcmGCtWS43m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17436,
      "cache_read_input_tokens": 22905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17436,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T15:38:56.824Z_

<details><summary>↩ Tool result · `toolu_01VceQbCdod2WmWo1WXeUW8c`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/memory.md\", \"content\": \"# Memory — turn_residual_gating\\n\\n## GAR Loss 模式演化教训\\n\\n### maximize 模式的结构性缺陷（v3/v3b/v5 验证）\\n- maximize (L_GAR = -mean(GAR)) 无界，驱动 gate 趋向恒等（gate→1 = 全通过 = 最大 GAR）\\n- v3b (λ=10, 500步): gate_std=0.087 但 L_GAR 已饱和 -0.96\\n- v5 (λ=1.0, 2400步): gate_std 从 0.034 降至 0.022，gate_mean 从 0.81 升至 0.965，确认长训练下分化完全消失\\n- 结论：maximize 只在短训练+大λ下产生暂态分化，不可用于正式训练\\n\\n### smooth_saturation 也失败（v6 验证）\\n- 公式: -target * tanh(GAR / target)，有界但仍单调奖励 GAR↑\\n- v6 step 100: gate_std=0.037↓ gate_mean=0.874↑，与 maximize 同轨迹\\n- 结论：**所有单调奖励 GAR↑ 的 loss 都会导致恒等退化**，不管有界无界\\n\\n### hinge_target 的梯度消失问题\\n- hinge_target (F.relu(target - mean_GAR)) 在 GAR 达标后梯度=0\\n- v1/v2 的 cumulative/pairwise 也有类似退化平衡点问题\\n- 不适合作为持续训练信号\\n\\n### MSE + gate_div：首个结构性不同的设计（v7 验证通过）\\n- MSE = (mean_GAR - target)²：双向，GAR > target 也受惩罚\\n- gate_div = F.relu(min_std - gate_std)：直接强制层间分化\\n- v7 dry-run: gate_std 0.034→0.088（5 步），L_GAR 为正（0.23），total loss 始终正\\n- v7 gs87: GAR 突破 0.05 阈值（从 0.016→0.066），呈加速趋势\\n- gate_div 按需启动（std<0.05 触发）、达标停止（std>0.05 归零）\\n- **v7 最终结果 (3 epoch)**：gate_std 全程稳定 0.049-0.054，L3/L4 持续最低（0.789/0.801），GAR 收敛到 target 附近（L_GAR≈0.001），NTP 正常收敛 0.896。Identity collapse 被阻止\\n\\n## NTP-GAR 梯度冲突机制（2026-05-19, gradient_conflict_analysis）\\n\\n### 核心发现：gate 参数面临不可调和的优化冲突\\n- 67-79% 的层 NTP 和 GAR 梯度方向相反（cos_sim: -0.089 → -0.042）\\n- NTP 梯度幅值碾压 GAR：ratio 从 epoch 0 的 7.5x 增长到 epoch 2 的 14.7x\\n- 随训练推进冲突减弱（cos_sim 趋近 0）但 NTP 幅度主导加剧——GAR 信号被淹没而非调和\\n- 这解释了所有 loss 变体最终失败的根因：不是 loss 设计问题，是 NTP+GAR 联合训练的结构性矛盾\\n\\n### Attention 衰减对比（4 模型 × 3 对话 × 28 层 × 10 轮）\\n- Base: mean_goal_attn=0.0136, T1→T10 decay=87.5%\\n- TG v7: mean_goal_attn=0.0232, T1→T10 decay=77.7%\\n- UG: mean_goal_attn=0.0216, T1→T10 decay=80.3%\\n- LoRA-only: mean_goal_attn=0.0216, T1→T10 decay=81.0%\\n- **结论：gating 机制对 attention 衰减零增量**（TG 77.7% vs LoRA-only 81.0%，差异在噪声范围内）\\n- LoRA 微调本身将 base 的 87.5% decay 降至 ~80%，这是 LoRA 的通用效果而非 gating 贡献\\n\\n### 机制性解释\\n- Gate 参数同时被 NTP（push gate→1.0 保持原始表示）和 GAR（需要 gate 重新分配 attention）拉扯\\n- NTP 梯度在训练中持续增强主导地位（7.5→14.7x），GAR 信号被边缘化\\n- 这是 teacher-forcing 下 auxiliary attention loss 的根本局限：NTP 天然比 attention redistribution 有更强的梯度信号\\n\\n## v7 Eval 关键发现（2026-05-19, D014）\\n\\n### GAR 过拟合：训练 0.48 vs 推理 0.016（30x 断层）\\n- 逐行对比 gar.py（训练）vs eval_phase2_gar.py（推理）：goal tokens、query positions、GAR 公式、forward pass 方式全部一致，不是 measurement bug\\n- 根因：模型在 ultrachat 训练数据上学到 GAR≈0.5，但 attention pattern 不泛化到 eval 数据\\n- 推论：GAR 作为训练信号存在泛化性根本问题\\n\\n### Gate turn conditioning 方向反转（D014 确认）\\n- Gate dynamic range 显示：早期 turn（goal attention 高）→ gate 值低（0.75-0.86，强抑制）；晚期 turn（goal attention 低）→ gate 值高（0.93-0.98，近乎恒等）\\n- 预期是晚期 turn 更强干预来恢复 goal attention，实际相反\\n- Reviewer 分析：这是 NTP-GAR 损失竞争的结构性后果，不是调 conditioning 方向能修的\\n- 结论：ThreadGate 正面 story 不成立（D014）\\n\\n### Eval baseline confound\\n- Phase1 baseline 用 BASE 模型的对话，Phase2 eval 用 LoRA 模型的不同对话，比较被 confound\\n- 修正：生成 standard_conversations.json（base 模型生成），所有 eval 用同一组对话\\n- 文件位置：/root/turn_residual_gating/data/standard_conversations.json（5 组 × 10 轮）\\n\\n## 超参经验\\n\\n### init_bias 与 sigmoid 初始点\\n- init_bias=2.0 → sigmoid≈0.88，gate 初始太高，NTP 梯度支配\\n- init_bias=0.0 → sigmoid=0.5，gate 初始低，GAR 梯度更强但训练不稳定\\n- init_bias=1.5 → sigmoid≈0.82，平衡点，v5/v6/v7 均使用\\n\\n### gate_lr_multiplier\\n- gate 梯度是间接的（通过 attention → residual stream），需要 10x LR 补偿\\n- multiplier=1 时 gate 几乎不动（v3 验证: gate_delta=0.004）\\n\\n## Step 编号规则（重要！）\\n- 日志 \\\"Epoch X Step Y\\\" 中的 Y 是 **micro-step**\\n- `[GATE] step=Z` 中的 Z 是 **global_step**\\n- global_step = micro_step / grad_accum（当前 grad_accum=8）\\n- 向 Director 汇报时必须标明是 global_step 还是 micro-step\\n\\n## 服务器环境\\n- westd-20861: RTX PRO 6000 Blackwell 98GB, conda base 环境\\n- 模型路径: /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\\n- 数据路径: /root/turn_residual_gating/data/ultrachat_8k (8000 samples)\\n- Python 激活: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n\\n## stdout 缓冲教训\\n- 训练脚本的 [GATE] 诊断行可能因 stdout 缓冲延迟出现\\n- 匹配诊断数据时必须按 step= 数字匹配，不能按行位置\\n- PYTHONUNBUFFERED=1 已在 v5+ 的启动命令中加入\\n\\n## Cron 误报模式\\n- [失败模式] Cron W&B sentinel：训练脚本不使用 W&B 时，进程正常完成后 cron 找不到 W&B metrics，连续 5 次检测进程不存在后自动判定 failed。修复方案：收到此类 failed 回调时先 tail_training_logs 查日志尾部，确认是否有 \\\"Training complete\\\" / checkpoint 保存记录，再判断真实 conclusion。v7 即此情况（2026-05-19）\\n\\n## Worker 产出验证规则（2026-05-19, M009 教训）\\n- Worker 报告下载/部署/文件操作成功时，必须要求附 `ls -la &lt;target_path>` 验证\\n- M009 事件：Reviewer 误判 Llama tokenizer 未下载（只查了 HF cache，未查 ModelScope cache）。实际 ModelScope 下载成功，文件在 `/root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`\\n- 教训：验证时要检查**所有可能的缓存路径**（HF cache + ModelScope cache）\\n- Llama-3.1 完整模型权重（~16GB）也可走 ModelScope 通道，不需要 HF token\\n\", \"total_chars\": 4420, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "294acd68-4edd-4266-a0b8-d57f227b76bc",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "ad7637c9-cffb-4cc0-98d9-40e1b8b536cb",
  "sourceToolAssistantUUID": "294acd68-4edd-4266-a0b8-d57f227b76bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T15:38:57.362Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01S4D8gBUMCSo8vuekFK4hgM`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad7637c9-cffb-4cc0-98d9-40e1b8b536cb",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBH2zT2NAD39tsHEuDS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1d7273f-4325-43fb-80c2-688096dbeed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnjMMkUA3zegcmGCtWS43m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17436,
      "cache_read_input_tokens": 22905,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17436
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 22905,
          "cache_creation_input_tokens": 17436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17436,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T15:38:57.373Z_

<details><summary>↩ Tool result · `toolu_01S4D8gBUMCSo8vuekFK4hgM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/decisions.yaml\", \"content\": \"_next_id: 24\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 04:48 UTC\\n  summary: MVP Phase 2 中间场景处置：条件1通过+条件2失败 = partial pass\\n  rationale: 如果 ThreadGate GAR recovery 显著优于 Uniform Gate（验证 Cesaro 理论预测）但下游任务无改善，说明核心机制成立但\\n    GAR explanation ceiling 有限。处置：视为 partial pass 进入 research，但 framing 必须从\\\"提升多轮性能的方法\\\"转向\\\"理论验证+首个\\n    principled 干预框架\\\"，实用价值作为 secondary contribution。如果连条件1都不满足则仍为 kill。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 04:59 UTC\\n  summary: MVP 使用残差缩放公式 x + g·f(x) 代替 IDEA_BRIEF 插值公式\\n  rationale: IDEA_BRIEF 的插值公式 g·x + (1-g)·f(x) 无法通过任何 g 值恢复正常模型行为 x+f(x)，导致初始化困难。改用\\n    x + g·f(x)（g=1 为正常，g→0 为跳过层），保证模型可从正常状态开始学习。核心对比（turn-conditional vs uniform）不受公式影响——两种公式下\\n    uniform gating 都无法选择性修改特定位置的 GAR。理论对齐留到 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-18 06:05 UTC\\n  summary: Phase 2 增加归一化 GAR 作为诊断指标，pass 标准仍基于 raw GAR\\n  rationale: Reviewer 发现 Phase 1 的 70.8% raw GAR 衰减大部分由序列增长稀释驱动，归一化后结构性下降仅 ~21%。normalized\\n    GAR 能区分\\\"稀释补偿\\\"vs\\\"结构性修复\\\"，直接影响论文 Cesaro 理论 story 的可信度。但 raw GAR 衰减是功能上真实有害的，方法即使只补偿稀释也有实用价值，因此\\n    MVP pass 标准不变。\\n  related_experiments:\\n  - exp_id: phase1_gar_diag\\n    role: evidence\\n    result: GAR衰减70.8%但归一化后仅~21%\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-18 13:37 UTC\\n  summary: Kill v3, run v3b (λ=10, gate_lr=10x, init_bias=0.0) as GAR-driven gating的最终验证。500步内gate无分化则GAR→gate梯度路径判定失败。\\n  rationale: v1/v2/v3 三个版本全部无法驱动gate学习选择性干预：v1 epsilon过高(L_GAR=0)，v2 hinge退化平衡点，v3\\n    maximize模式梯度太弱(gate冻结在0.876±0.001)。根因一致：GAR→attention→hidden→gate间接梯度路径太弱。v3b同时最大化三个信号强度维度(λ=10,\\n    gate_lr=10x, init_bias=0.0给sigmoid最大梯度区间)，如果仍然失败则排除\\\"信号不够强\\\"的解释，确认是梯度路径结构性问题。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v1\\n    role: evidence\\n    result: L_GAR=0 (epsilon too high)\\n  - exp_id: phase2_tg_s42_v2\\n    role: evidence\\n    result: hinge degenerate equilibrium (M005)\\n  - exp_id: phase2_tg_s42_v3\\n    role: evidence\\n    result: gate frozen 0.876±0.001, maximize gradient too weak\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-18 14:55 UTC\\n  summary: v3b 部分通过：gate 分化验证成功（gate_std=0.087），但 λ=10 导致 GAR 饱和（0.96）训练失衡。启动 v4 重新平衡：λ=1.0,\\n    gate_lr_multiplier=10, init_bias=1.5。\\n  rationale: v3b 证明 gate_lr_multiplier=10 是驱动 gate 分化的关键（v3 无 multiplier 时 gate 冻结）。但\\n    λ=10 使 GAR 贡献占 90%+ 总梯度，GAR 从 0.02 饱和到 0.96（病态）。重新平衡策略：λ=1.0 保持 NTP 主导（GAR 贡献初期\\n    ~2%，稳态 ~50-100%），gate_lr_multiplier=10 确保 gate 仍有足够信号分化（有效信号=10，高于 v3 失败的 2），init_bias=1.5（sigmoid≈0.82）减少伪分化风险。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: gate_std=0.087 PASS, but GAR saturated to 0.96 (pathological), total loss\\n      deeply negative\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-18 15:42 UTC\\n  summary: Dongre et al. (2605.12922) 发现后 framing 调整方向：从\\\"发现+解决\\\"转为\\\"首个干预方案\\\"，cite Dongre\\n    作为问题诊断基础，ThreadGate 定位为 first architectural intervention。paper_framing.md 待 v4\\n    结果后正式写。\\n  rationale: Dongre et al. 5天前定义了 GAR 并在 Qwen-2.5-7B 上验证了衰减，但(1)未提出干预方案(唯一尝试的 goal\\n    re-injection 失败)，(2)发现 goal info 在 residual stream 持续存在(Qwen L5 peak probe AUC=0.98)，直接支撑\\n    ThreadGate 的 residual gating 理论。v3b 的 L4 gate outlier 与 Dongre 的 L5 goal-encoding\\n    onset 完美对齐。新 story 比独立讲更强：独立验证的问题 + 理论支撑 + 首个解决方案。放弃 GAR 首创权和衰减发现权，保留 ThreadGate\\n    机制、GAR loss 训练方法、per-layer gate 发现的原创性。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: L4 gate=0.535 outlier, aligns with Dongre L5 goal-encoding onset\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-18 16:41 UTC\\n  summary: L4/L5 gate-Dongre 对齐 claim 从 \\\"perfect alignment\\\" 降级为 \\\"suggestive\\\"；跨架构层级差异作为\\n    ThreadGate per-layer 自适应卖点纳入 framing\\n  rationale: Reviewer 核实 Dongre 论文后指出：1) L4 vs L5 仅基于 1 seed 500步快速验证，证据不足称 \\\"perfect\\\"；2)\\n    Dongre 发现 onset 层跨架构从 L2-L27 不等，这恰好支持 ThreadGate per-layer gating 的必要性。等 v4 全量训练\\n    gate profile 确认后再决定是否加强 claim。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: L4 gate=0.535 outlier\\n  - exp_id: phase2_tg_s42_v4\\n    role: pending_confirmation\\n    result: 需验证 L4 outlier 稳定性\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-18 17:33 UTC\\n  summary: v5 复现 v3b 退化模式（总 loss 转负、gate 趋向 identity），确认 maximize 模式 L_GAR 无上界是结构性问题。v5\\n    设硬止损继续跑到 step 500 opt，同时设计 v6 bounded GAR loss\\n  rationale: v1-v5 实验链暴露同一根因：maximize 模式下 LoRA 改善 attention → GAR 持续上升 → L_GAR 无限下降\\n    → 总 loss 转负。λ 和 gate_lr 调参只改变退化速度，不改变结局。需要 bounded loss（hinge-on-target 或 clipped）从结构上解决。v5\\n    不立即 kill，作为数据点跑到 step 500 opt 硬止损。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v5\\n    role: evidence\\n    result: step 1350 总 loss 转负，gate_std=0.029↓，GAR≈0.80 超出目标区间\\n  - exp_id: phase2_tg_s42_v3b\\n    role: precedent\\n    result: 相同退化模式，λ=10 退化更快\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D009\\n  date: 2026-05-18 17:49 UTC\\n  summary: Kill v5（maximize 模式 gate 分化失败确认），启动 v6 smooth_saturation target=0.5\\n  rationale: 'v5 step 300 opt: gate_std=0.022（持续下降）、gate_mean=0.965（趋向 identity）、GAR~0.90（远超目标）、总\\n    loss 频繁转负。4 项 hypothesis 中 3 项 FAIL，趋势无逆转信号。v1-v5 确认 maximize 模式结构性失败。v6 用 smooth_saturation（首个同时有界+无零梯度的\\n    loss），target 从 0.3 调到 0.5——0.3 时 GAR=0.3 处梯度已衰减至 42%，0.5 给更宽有效工作范围，总 loss 下界 0.2\\n    仍安全。'\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v5\\n    role: evidence\\n    result: gate_std=0.022↓, gate_mean=0.965↑, maximize 无上界确认\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-18 18:17 UTC\\n  summary: Kill v6（smooth_saturation 未解决恒等退化），v7 改用 MSE(GAR, target) 双向 loss + gate\\n    diversity 正则化\\n  rationale: v6 step 100 确认 smooth_saturation 与 maximize 轨迹相同（gate_mean 0.874↑, gate_std\\n    0.037↓, L_GAR -0.158 加速中）。根因：任何单调奖励 GAR↑ 的 loss 都推 gate→1.0，因为 identity 对 GAR\\n    和 NTP 都是局部最优。需要双向 loss：MSE(GAR, target) 在 GAR>target 时产生反向梯度，打破单调性。加 gate diversity\\n    正则化直接强制层间分化（否则 LoRA 独立完成 GAR 调节，gate 仍趋向 identity）。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v6\\n    role: evidence\\n    result: 'step 100: gate_mean=0.874↑ gate_std=0.037↓，与 v5 同轨迹'\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-18 19:19 UTC\\n  summary: v7 gs200 达到 MVP Phase 2 关键里程碑：GAR 收敛到 target (0.48)，gate profile L3/L4\\n    与 Dongre onset 对齐，训练稳定。继续跑完 epoch 0，同时准备 UG baseline\\n  rationale: v7 MSE+diversity reg 首次同时实现：(1) GAR 实质改善（0.016→0.48, 30x）；(2) gate 不崩溃到\\n    identity（mean=0.94 vs v5的0.97）；(3) per-layer 可解释结构（L3/L4最低，与Dongre L4/L5 onset对齐）；(4)\\n    total loss始终正。三阶段GAR动力学（平台→相变→收敛）可发表。下一步需 UG baseline 对比验证 MVP pass 标准（TG GAR\\n    > UG + 3pp）。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: 'gs200: GAR=0.48, gate_std=0.053, L3/L4 lowest, total loss positive'\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-18 20:16 UTC\\n  summary: Reviewer 独立评估 v7：GAR 改善归因高度可疑（gating 扰动仅 ~1.4%，LoRA 为主要驱动）。eval 增加 per-turn\\n    gate profiling，ablation 增加 LoRA-only baseline\\n  rationale: 28 层中仅 L3/L4 gate 显著低于 1.0（~0.79-0.81），总 gating 扰动 ~1.4%，驱动 GAR 30x 提升在机制上不可信。UG\\n    baseline 只能测 turn conditioning 增量，无法区分 \\\"有 gating\\\" vs \\\"无 gating\\\"。需要 LoRA-only ablation（gate\\n    固定 1.0）排除 LoRA 单独驱动 GAR 改善的可能。per-turn gate profiling 是判断 inference-time 价值的核心数据。L3/L4\\n    与 Dongre 对齐只能说 \\\"coincides with\\\"，不能暗示因果。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: GAR=0.48 but gating perturbation only ~1.4%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-19 00:56 UTC\\n  summary: v7 推理 GAR recovery 极弱（ours +0.35pp, Dongre +0.72pp），远低于 3pp MVP 门槛。训练-推理\\n    30x GAR 断层需调查是实现 bug 还是真实现象。暂不判定 MVP fail，等 gate-profile + 30x 断层调查 + UG/LoRA-only\\n    ablation 完成。\\n  rationale: 1) 两个 metric 均远低于 3pp 但缺少 --gate-profile 数据无法判断 turn conditioning 在推理时是否有效；2)\\n    30x 训练-推理 GAR 断层可能是实现问题（goal token 定义不同？eval 数据分布不同？attention 计算范围不同？），不能直接把弱结果归因于方法失败；3)\\n    UG/LoRA-only ablation 数据缺失，无法分离 gate vs LoRA 贡献；4) 过早 pivot 可能放弃一个因实现问题而被低估的方法\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: training success, inference GAR weak\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  depends_on:\\n  - D012\\n  - D011\\n- id: D014\\n  date: 2026-05-19 01:09 UTC\\n  summary: Gate-profile 揭示 turn conditioning 反向学习：27/28 层 gate 在后续 turns 趋向 identity（减少干预），与假设完全相反。机制：GAR\\n    达标后 L_GAR≈0，NTP 梯度在长序列中推 gate→1.0。ThreadGate 正面 story 不成立，但继续完成 UG/LoRA-only ablation\\n    收集完整证据。\\n  rationale: 1) 27/28 层 diff 为负，训练明星层 L3/L4 推理时几乎静态（diff -0.001/-0.020）；2) 这是 NTP-GAR\\n    损失竞争的结构性后果——GAR 收敛后 NTP 完全主导，在长序列（后续 turns）推 gate 趋向 identity；3) 不可通过调参修复（提高 λ_GAR\\n    回到 v3b 病态饱和）；4) 但 UG/LoRA-only ablation 仍需完成：a) 确认 gating 贡献为零 b) 这些数据有 negative\\n    result 论文价值 c) 为 pivot 决策提供完整证据\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: reverse turn conditioning confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: ablation\\n    result: preparing\\n  depends_on:\\n  - D013\\n  - D012\\n- id: D015\\n  date: 2026-05-19 01:11 UTC\\n  summary: 30x 训练-推理 GAR 断层确认为 GAR 过拟合（非 measurement bug）。发现实验设计 confound：Phase1/Phase2\\n    eval 对话文本不同导致比较被污染。批准 standard_conversations 方案：base model 生成标准对话集，三个条件在同一对话上评估。\\n  rationale: 1) 训练/eval GAR 计算逻辑逐行一致（goal token、query positions、公式、teacher-forcing），排除实现\\n    bug；2) GAR 从 0.02→0.48 仅在 ultrachat 训练数据上，不泛化到 eval 数据 = attention pattern 过拟合；3)\\n    当前 baseline 对比被 confound（不同对话文本），需 standard_conversations 控制变量；4) 即使在公平测试下 TG\\n    略优于 LoRA-only，gate-profile 的反向 turn conditioning (D014) 仍是结构性问题\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: GAR overfitting confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: ablation\\n    result: preparing\\n  depends_on:\\n  - D014\\n  - D013\\n- id: D016\\n  date: 2026-05-19 01:52 UTC\\n  summary: Two-stage decoupled training：有条件尝试（~20-30% 成功率）。以 LoRA-only 结果为 gate keeper：LoRA-only\\n    ≈ TG → 不做（gating 贡献为零）；LoRA-only < TG → 做 Stage 1（解除 NTP 压制放大 gating 贡献）。不并行——等\\n    LoRA-only 数据再决策。\\n  rationale: Reviewer 系统性审查：(1) NTP-GAR 竞争部分解除但 gate→GAR 梯度路径本身弱（D004/D005 历史），Stage\\n    1 无 LoRA 时更弱；(2) GAR 过拟合独立于训练策略；(3) 分布漂移是最大结构性风险（Stage 2 LoRA 改变 hidden states\\n    使 Stage 1 gates 失效）；(4) 如果 LoRA-only=TG 则 gating 机制本身无效，改变训练策略无法解决机制局限。Stage 1\\n    成本低（~1.67M params），即使失败也提供 pure gating GAR 改善上界数据。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: NTP-GAR competition confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: preparing\\n  depends_on:\\n  - D015\\n  - D014\\n- id: D017\\n  date: 2026-05-19 02:25 UTC\\n  summary: 采纳 Reviewer 两路策略：准备路线 B 框架（negative result + mechanistic insight），以 LoRA-only\\n    为 gate keeper 决定是否先试路线 A（two-stage）。无论哪条路线，跨模型验证（Llama-3-8B）和 baseline 训练-推理 GAR\\n    对比都是 high-ROI 必做项。\\n  rationale: 路线 A ~20-30% 成功率但 ceiling 高（main track）；路线 B ~70% Findings 但需跨模型加强才冲\\n    main。A 失败的数据直接增强 B（\\\"even decoupled training fails\\\"）。关键缺失：baseline 训练-推理 GAR 对比——如果\\n    base model 也有 30x 断层则 claim 需调整。策略：B 框架先写（不依赖数据）、LoRA-only 决策点、A 失败无缝转 B。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: negative\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: preparing\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-19 10:42 UTC\\n  summary: Reviewer 深度分析：Route A 成功概率从 20-30% 修正至 <5%，根本矛盾是 teacher-forcing→generation\\n    分布偏移而非 NTP-gate 竞争\\n  rationale: Reviewer 分析揭示更深层机制：(1) LoRA-only L_GAR≈0 证明 gating 在训练端冗余；(2) 如果 LoRA-only\\n    推理 GAR ≈ TG，问题不在 NTP-gate 竞争，而在 teacher-forcing 下优化的 GAR 无法迁移到 generation 模式——这个根本矛盾\\n    two-stage 也无法解决；(3) Route B Findings 可行性 65-75%，需跨模型验证；(4) 关键 framing：\\\"发现了 X 机制\\\"而非\\\"方法\\n    X 失败了\\\"。四路 eval 补充 PPL + per-turn GAR curve 作为核心判别 metrics。\\n  related_experiments:\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: running, training L_GAR≈0 same as TG/UG\\n  - exp_id: phase2_tg_s42_v7\\n    role: reference\\n    result: inference GAR +0.35pp\\n  - exp_id: phase2_ug_s42\\n    role: reference\\n    result: training complete, eval pending\\n  depends_on:\\n  - D017\\n  - D015\\n  - D014\\n- id: D019\\n  date: 2026-05-19 10:56 UTC\\n  summary: v7 中间 checkpoint：选 Option B（3 epoch checkpoint 粗粒度分析），不重训。跨模型验证优先级更高。\\n  rationale: 重训 v7 保存中间 checkpoint 需 ~6h GPU，而 GPU 接下来优先用于四路 eval + 跨模型验证（Llama-3），后者对\\n    Route B 论文强度提升远大于细粒度 GAR 泛化曲线。3 个 epoch checkpoint（gs1000/2000/3000）足够展示过拟合趋势。10\\n    weeks 到 DDL，如需精细分析可后补。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: subject\\n    result: 3 epoch checkpoints available, fine-grained gs50-200 missing\\n  depends_on:\\n  - D018\\n  - D017\\n- id: D020\\n  date: 2026-05-19 12:27 UTC\\n  summary: Llama-3 最小验证方案扩展为 Base + TG + LoRA-only（Reviewer 建议），总计 ~15h GPU\\n  rationale: 论文 C4 claim \\\"gating redundancy is model-agnostic\\\" 需要 Llama 上的 LoRA-only\\n    数据点。仅 Base + TG 能验证 GAR gap 但无法验证 gating 冗余。额外 ~6h GPU 换取 C4 跨模型支撑，ROI 高。同时 Reviewer\\n    发现计划中 CLI flags、NF3' 描述、output_dir 路径有误，执行时需修正。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: reference\\n    result: Qwen baseline for cross-model comparison\\n  depends_on:\\n  - D019\\n  - D018\\n- id: D021\\n  date: 2026-05-19 13:15 UTC\\n  summary: Route B 正式确认：四路 eval 三路趋同（GAR 差异<0.6pp, PPL 差异<0.02），gating 零增量。进入 negative\\n    result + mechanistic insight 路线。\\n  rationale: 'GAR-ours: TG 0.487 / UG 0.492 / LoRA-only 0.486（差异<0.6pp）；GAR-Dongre:\\n    TG 0.016 / UG 0.013 / LoRA-only 0.014（差异<0.3pp）；PPL: TG 2.629 / UG 2.616 / LoRA-only\\n    2.629。三个维度均确认 gating 无增量。Route A 完全无依据（<5% 预期已彻底归零）。核心发现：teacher-forcing 下 GAR\\n    loss 有效（~0.49）但不迁移到推理端（Dongre ~0.015），完美支持 D018 的 teacher-forcing distribution\\n    shift 叙事。注意：eval 数据与训练集重叠，需补做 held-out eval。'\\n  related_experiments:\\n  - exp_id: phase2_lora_only_s42\\n    role: key_evidence\\n    result: GAR-ours 0.486, GAR-Dongre 0.014, PPL 2.629 — identical to TG/UG\\n  - exp_id: phase2_tg_s42_v7\\n    role: key_evidence\\n    result: GAR-ours 0.487, GAR-Dongre 0.016, PPL 2.629\\n  - exp_id: phase2_ug_s42\\n    role: key_evidence\\n    result: GAR-ours 0.492, GAR-Dongre 0.013, PPL 2.616\\n  depends_on:\\n  - D018\\n  - D017\\n  - D019\\n  - D020\\n- id: D022\\n  date: 2026-05-19 14:39 UTC\\n  summary: 'Dream review 分析: 收窄 claim scope + 补充 3 个实验 (bootstrap CI / exposure-bias\\n    mitigation / code verification)'\\n  rationale: Dream dream_20260519T135115 (review_mode=full) best=3.0 median=3.0 (Weak\\n    Reject)。两份 review 一致指出三个结构性问题：(1) claim 过度泛化 \\\"all auxiliary attention losses\\\"\\n    unsupported by single scalar gating test → 收窄为 \\\"lightweight residual gating with\\n    joint NTP+GAR loss\\\"; (2) 引用仅 11 篇，缺 attention sinks/Found-in-the-Middle/gated\\n    attention/transformer circuits 等 → 目标 25-30; (3) 单 seed 无方差估计 → 添加 bootstrap CI\\n    (plan_015)。额外添加 exposure-bias mitigation test (plan_016, P1, 8h) 作为 constructive\\n    direction，以及 code-paper architecture verification (plan_017, P0, 0h)。修正后预期 best\\n    从 3.0 提升至 3.5 (Weak Accept)。需 re-dream 验证。\\n  related_experiments:\\n  - exp_id: phase2_4way_eval\\n    role: evidence_base\\n    result: negative\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence_base\\n    result: success\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-19 14:50 UTC\\n  summary: 'Eq.3 code-paper formula mismatch confirmed (plan_017): code uses x+g·f(x),\\n    dream paper.tex wrote g·x+f(x). Data unaffected, mechanism narrative needs rewrite\\n    for Paper Agent.'\\n  rationale: 'Reviewer critical finding: ThreadGate code implements ReZero-style gating\\n    (gate on sub-layer output), but dream paper.tex wrote gate on residual stream\\n    — semantically opposite when g→0. All experiments used the same code so data is\\n    internally consistent. Mechanism narrative in paper needs correction: g→0 = layer\\n    becomes no-op (sub-layer suppressed), NTP pushes g→1 to preserve layer computation\\n    capacity (not to preserve skip connection). Updated paper_framing.md R4 with detailed\\n    Paper Agent writing instructions.'\\n  related_experiments:\\n  - exp_id: plan_017\\n    role: verification\\n    result: confirmed mismatch\\n  depends_on:\\n  - D022\\n\", \"total_chars\": 15777, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1d7273f-4325-43fb-80c2-688096dbeed9",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "eb80140f-f5ad-4d4d-ab9a-923040b528cb",
  "sourceToolAssistantUUID": "c1d7273f-4325-43fb-80c2-688096dbeed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T15:39:03.555Z_

Now let me also read some previous review reports and the review context from the earlier dream.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb80140f-f5ad-4d4d-ab9a-923040b528cb",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBHPxGrzM3MeXsb3ith",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00740cb9-2b96-484c-8586-5fa9126cc493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjJCknPMfti6jCPqsXEwgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12388,
      "cache_read_input_tokens": 40341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12388,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T15:39:06.015Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SJBzyWakdwpJtR3scDeAAh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00740cb9-2b96-484c-8586-5fa9126cc493",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBHPxGrzM3MeXsb3ith",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0646ab7b-02c0-4b51-9dd1-d49e2e8c602b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjJCknPMfti6jCPqsXEwgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12388,
      "cache_read_input_tokens": 40341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12388,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T15:39:06.023Z_

<details><summary>↩ Tool result · `toolu_01SJBzyWakdwpJtR3scDeAAh`</summary>

```text
1	---
2	dream_id: dream_20260519T145320
3	tier: best
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-19T15:32:41.481759+00:00
6	---
7	
8	# Dream Review Report: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation"
9	
10	**dream_id**: 20260519T145320 | **review_mode**: full | **date**: 2026-05-19
11	
12	---
13	
14	## Overall Assessment
15	
16	**Score: 3.5 / 6** (Borderline Conference — between Findings and Main)
17	
18	**One-line summary**: A well-structured negative result with genuine mechanistic insight (gradient competition analysis, scheduled sampling causal evidence), limited by narrow intervention scope (scalar gates only), single training seed, and underdeveloped related work.
19	
20	---
21	
22	## Reviewer Summaries
23	
24	### R1 (Methods + Experiments) — Score: 3.0 | Confidence: 4/5
25	
26	The paper presents a clean negative result supported by systematic ablation (four-way on Qwen, three-way on Llama), bootstrap statistical validation, and a causal scheduled sampling experiment. The gradient competition analysis (§6.1) — decomposing NTP-GAR conflict into directional (cosine similarity) and amplitude (magnitude ratio) components across layers and epochs — is the paper's strongest contribution. However, methodological gaps limit confidence: (1) only per-layer scalar gates are tested, making the title's generality ("lightweight gating cannot fix") overclaimed; (2) the ablation is missing a "LoRA + GAR loss, no gate" condition that would disentangle gate mechanism from auxiliary loss; (3) the scheduled sampling experiment is not replicated on Llama; (4) training uses a single seed, leaving gradient competition statistics without confidence bounds.
27	
28	### R2 (Novelty + Related Work) — Score: 3.5 | Confidence: 4/5
29	
30	The core observation — exposure bias destroys auxiliary attention loss generalization — is expected given prior work (Bengio et al. 2015), but the quantification (30× gap) and mechanistic decomposition are novel for this setting. The paper's scientific narrative is compelling (Dongre's probe AUC → hypothesis → ThreadGate → failure → why → partial cure via SS). Related work is significantly underdeveloped (~15 references; needs 25-30), missing key areas: transformer circuits/mechanistic interpretability (Elhage et al., Olsson et al.), recent gated attention variants (Qiu et al. 2025), multi-turn benchmarks (MT-Bench-101, MultiChallenge), adaptive depth (Mixture-of-Depths, LayerDrop), and training-free attention calibration. The 30× gap number conflates two different GAR definitions (GAR-ours for training, GAR-Dongre for inference), potentially inflating the perceived magnitude.
31	
32	---
33	
34	## Consolidated Strengths
35	
36	1. **Clean scientific narrative**: Dongre's probe AUC=0.98 → information survives but attention fails → residual gating should recover it → it doesn't → mechanistic diagnosis → partial cure via scheduled sampling. This is exemplary hypothesis-driven research.
37	
38	2. **Gradient competition analysis (§6.1)**: Per-layer decomposition into directional conflict (67-79% of layers) and amplitude suppression (7.5× → 14.7× growth during training) provides genuine mechanistic insight. The finding that apparent conflict "resolution" (cos_sim trending to zero) is marginalization rather than reconciliation is non-obvious.
39	
40	3. **Systematic loss design exploration**: Seven configurations (v1-v7) across four design families rules out the "wrong loss function" objection and demonstrates thorough engineering.
41	
42	4. **Four-way ablation with bootstrap validation**: TG/UG/LoRA-only/Base on Qwen, three-way on Llama, with paired bootstrap CI (n=50, p=0.71, Cohen's d=0.02) provides rigorous statistical support for the zero-benefit claim.
43	
44	5. **Cross-model validation**: Qwen-2.5-7B (MHA) + Llama-3.1-8B (GQA) with near-identical quantitative patterns (30× vs. 26× gap, 0.20pp vs. 0.19pp TG-LO diff) confirms architecture independence.
45	
46	6. **Scheduled sampling causal experiment**: 30× → 4.3× gap reduction (7× improvement) upgrades the paper from pure negative result to diagnosis with partial mitigation, which is a substantially stronger contribution type.
47	
48	---
49	
50	## Consolidated Weaknesses
51	
52	1. **Narrow intervention class limits title's generality** (R1+R2 agree): Only per-layer scalar gates are tested — the weakest possible gating intervention. Per-head vector gates, input-dependent dynamic gates, or attention-internal supervision are all still "lightweight" but untested. The title claims "lightweight gating cannot fix" but only one specific variant is tested. This is the most significant weakness.
53	
54	2. **Single training seed** (R1+R2 agree): While bootstrap CIs address evaluation variance, training variance (LoRA initialization, data ordering) is entirely uncharacterized. The gradient competition statistics (cos_sim, mag_ratio, conflict percentages) are point estimates without confidence bounds. Multi-seed training (even 3 seeds) would substantially strengthen these claims.
55	
56	3. **Missing "LoRA + GAR loss, no gate" ablation** (R1): The current design conflates the gate mechanism with the auxiliary loss. LoRA-only uses NTP-only training, so the equivalence at inference could mean auxiliary losses add nothing through any pathway, not specifically that gating is inert. This ablation would disentangle these interpretations.
57	
58	4. **Training-inference GAR comparison uses different definitions** (R2): The headline 30× gap compares GAR-ours (training, teacher-forced) with GAR-Dongre (inference, autoregressive). These are different metrics on different distributions, inflating the perceived gap. A same-definition comparison should be the primary number.
59	
60	5. **Underdeveloped related work** (R2): ~15 references across four subfields is insufficient for EMNLP. Missing: transformer circuits (Elhage et al. 2021, Olsson et al. 2022), recent gated attention (Qiu et al. 2025), multi-turn benchmarks (MT-Bench-101, MultiChallenge), adaptive depth (Mixture-of-Depths, LayerDrop), training-free attention calibration (Found-in-the-Middle). The project's literature map covers >30 relevant papers that did not make it into the manuscript.
61	
62	6. **Scheduled sampling experiment lacks replication and ablation** (R1+R2): The SS experiment — the paper's strongest causal evidence — is run only on Qwen (not Llama) and at a single configuration (linear 0→50%). No SS ratio ablation (25%, 75%, 100%) is provided. The residual 4.3× gap is attributed to "50% cap and noisy early gradients" without evidence.
63	
64	7. **Minimal downstream evaluation** (R2): Instruction compliance on formatting strings (e.g., "respond in bullet points") is a simplified proxy. Evaluation on established benchmarks (MT-Bench, MultiChallenge) would substantially strengthen the practical relevance of GAR as a metric.
65	
66	8. **Missing reproducibility details** (R1): Base LoRA learning rate, exact λ_GAR and λ_div values, gate diversity loss formulation (equation), optimizer/scheduler, gradient accumulation/batch size, and GAR-ours token selection procedure are not reported.
67	
68	---
69	
70	## Key Questions for Authors
71	
72	1. **Same-definition gap**: What is the training-inference gap when measured with the same GAR definition (e.g., GAR-Dongre for both, or GAR-ours for both)? How much of the 30× is attributable to the metric switch vs. the distribution shift?
73	
74	2. **Missing ablation**: Have you tried "LoRA + GAR loss, no gate"? If this matches TG at inference, it strengthens the gate-specific failure claim. If it matches LoRA-only, it suggests auxiliary losses add nothing through any pathway.
75	
76	3. **SS cross-model replication**: Why was scheduled sampling not run on Llama-3.1-8B? Given cross-model validation is a stated contribution, this omission weakens the causal claim.
77	
78	4. **Per-head gating control**: Have you considered testing per-head or vector gates? Even a pilot experiment would clarify whether the failure is scalar-gate-specific or gating-architecture-general. (cf. Qiu et al. 2025 on head-specific sigmoid gates)
79	
80	5. **Training data scale**: All experiments use 1,000 UltraChat conversations. Could the 30× gap be a small-data phenomenon? On a larger dataset, might the model learn more robust attention patterns?
81	
82	6. **Gradient competition under SS**: Does scheduled sampling change the NTP-GAR gradient dynamics? If SS reduces the gap but does not alter gradient competition, it would confirm these are independent mechanisms.
83	
84	---
85	
86	## Experiment Coverage Assessment
87	
88	Comparing against the imagined experiment list:
89	
90	| Experiment | Status |
91	|---|---|
92	| Qwen v7 Gradient Conflict Analysis | ✅ Covered (§6.1, Table 6, Appendix C) |
93	| Attention Heatmap Visualization | ⚠️ Partially covered (§6.3 mentions r=0.97 correlation but no figure shown) |
94	| Llama-3.1-8B Phase 1 GAR Diagnosis | ✅ Covered (§5.1, Table 1) |
95	| Llama-3.1-8B TG v7 Training | ✅ Covered (§5.2, Table 2) |
96	| Llama-3.1-8B LoRA-only Training | ✅ Covered implicitly (§5.4) |
97	| Llama-3.1-8B 3-Way Eval | ✅ Covered (§5.4, Table 4) |
98	| Llama-3.1-8B Gradient Conflict | ✅ Covered (§6.1, Table 6) |
99	| Downstream Task Sanity Check | ✅ Covered (§6.5, Table 8 in Appendix B) |
100	| Bootstrap CI for Zero Benefit | ✅ Covered (§5.5, Table 5) |
101	| Exposure-Bias Mitigation (SS) | ✅ Covered (§6.4, Table 7) |
102	
103	Coverage is high (9/10 fully covered, 1 partial). The attention heatmap figure — particularly the TG training-vs-inference comparison — would be a compelling addition that could fit within the page limit.
104	
105	---
106	
107	## Actionable Recommendations (Priority-Ordered)
108	
109	1. **[Critical]** Add a same-definition GAR gap comparison as the primary number; relegate the cross-definition 30× to supplementary context.
110	2. **[Critical]** Expand related work to 25-30 references, covering transformer circuits, recent gated attention, multi-turn benchmarks, and adaptive depth.
111	3. **[High]** Run scheduled sampling on Llama-3.1-8B to maintain cross-model consistency.
112	4. **[High]** Add the "LoRA + GAR loss, no gate" ablation condition.
113	5. **[High]** Report all missing hyperparameters (λ_GAR, λ_div, diversity loss equation, base LR, optimizer, batch size).
114	6. **[Medium]** Add 2-3 seed training runs and report variance on gradient competition statistics.
115	7. **[Medium]** Include the attention heatmap figure (training vs. inference for TG) — fits within page limit and provides visual impact.
116	8. **[Medium]** Add one paragraph discussing what happens with richer gating (per-head, dynamic) as a limitation/future work, to temper the title's generality.
117	9. **[Low]** Add v1-v7 loss exploration table to appendix as a selling point of systematic design.
118	10. **[Low]** Add SS ratio ablation (25%, 75%) to characterize the gap reduction curve.
119	
120	---
121	
122	## Venue Recommendation
123	
124	**Findings of EMNLP 2026**: The paper in its current form is at the Findings/Main boundary. The core empirical contribution (30× gap quantification, gradient competition analysis, SS causal evidence) is sound and useful. With the critical fixes above (same-definition gap, expanded related work), it is a solid Findings paper. With high-priority fixes as well (SS on Llama, missing ablation), it becomes competitive for Main conference.
125	
126	**Score: 3.5 / 6** — Borderline Conference (consensus of R1=3.0, R2=3.5, converging after roundtable discussion)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0646ab7b-02c0-4b51-9dd1-d49e2e8c602b",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "463ef594-7a66-4001-9bee-3c48c45d9a07",
  "sourceToolAssistantUUID": "0646ab7b-02c0-4b51-9dd1-d49e2e8c602b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T15:39:06.298Z_

<details open><summary>🔧 Tool call — Read · `toolu_014uAAj41omyWpQkPZzieiJ1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "463ef594-7a66-4001-9bee-3c48c45d9a07",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBHPxGrzM3MeXsb3ith",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "311a4f4b-dfa2-4126-9284-ca7b8b8b9ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjJCknPMfti6jCPqsXEwgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12388,
      "cache_read_input_tokens": 40341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12388,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T15:39:06.305Z_

<details><summary>↩ Tool result · `toolu_014uAAj41omyWpQkPZzieiJ1`</summary>

```text
1	---
2	dream_id: dream_20260519T145320
3	tier: median
4	overall_score: 3/6 Weak Reject
5	timestamp: 2026-05-19T15:36:58.914569+00:00
6	---
7	
8	# Dream Review Report
9	
10	**Paper**: "Why Lightweight Gating Struggles to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
11	**Review mode**: full | **Reviewers**: R1 (Methods & Experiments), R2 (Novelty & Related Work)
12	
13	---
14	
15	## 1. Summary
16	
17	The paper investigates whether lightweight residual gating can fix multi-turn attention degradation in LLMs. ThreadGate—a per-layer scalar gate trained jointly with NTP and an auxiliary GAR objective—successfully optimizes GAR during training (0.02→0.48 on Qwen-2.5-7B) but fails at inference (GAR=0.016, 30× gap). The paper identifies two coupled failure mechanisms: (1) NTP gradient dominance (7–15× magnitude ratio) causing reverse turn conditioning in gates, and (2) teacher-forcing distribution shift. Cross-model experiments on Llama-3.1-8B show directional consistency (10× gap). Scheduled sampling reduces the gap to 12.3× (p≈0.07, statistically marginal).
18	
19	---
20	
21	## 2. Strengths
22	
23	**S1. Well-structured negative result with honest reporting.** The paper presents a clear hypothesis → experiment → failure → mechanistic explanation arc. Claims are appropriately hedged: Qwen results are presented as clean negatives, Llama results as directionally consistent but ambiguous, and scheduled sampling as suggestive but inconclusive. This is how negative results should be reported.
24	
25	**S2. Thorough ablation on Qwen.** The 4-way ablation (Base/ThreadGate/Uniform Gate/LoRA-only) with bootstrap CIs (p=0.42, d=0.05) cleanly isolates gating's zero incremental contribution. The Uniform Gate control is a thoughtful addition that rules out the diversity regularization as a confound.
26	
27	**S3. Mechanistic depth.** The gradient conflict analysis (Table 6) across 3 training checkpoints, the gate profile analysis showing reverse turn conditioning (27/28 layers on Qwen), and the attention visualization (Table 7) collectively build a convincing causal story for the failure. The key insight—cos_sim weakening over training reflects GAR marginalization, not objective alignment—is well-articulated.
28	
29	**S4. Cross-model validation.** Testing on both Qwen-2.5-7B (MHA) and Llama-3.1-8B (GQA) provides meaningful architectural diversity. The paper handles the messier Llama results honestly (56–63% conflict layers vs. 67–79%, wider CIs, d=0.22).
30	
31	**S5. Downstream task validation.** Table 5 linking GAR decay to instruction retention (r=0.72) addresses a natural concern about GAR as a sole proxy metric. Even though r=0.72 is moderate, it provides necessary face validity.
32	
33	---
34	
35	## 3. Weaknesses
36	
37	**W1. [Critical] ALL references are broken.** Every citation in the paper appears as "?" instead of actual author names/years. This occurs in the abstract, introduction, related work, background, methods, and throughout the text. The paper is unreadable as a formal academic submission—readers cannot trace intellectual lineage, verify related work coverage, or assess positioning claims. This must be fixed before any submission.
38	
39	**W2. [Major] Zero figures in a "mechanistic analysis" paper.** The paper contains 9 tables but not a single figure. For a paper whose core contribution is mechanistic explanation, this is a severe presentation failure. The following visuals are critically missing:
40	- Training curves showing the three-phase trajectory (plateau → transition → convergence)
41	- Per-layer gradient conflict heatmaps (cos_sim × layers × epochs)
42	- Attention heatmaps comparing training vs. inference patterns across model variants
43	- Gate profile visualization across turns showing reverse conditioning
44	- Bootstrap distribution histograms for the key statistical tests
45	- GAR decay curves comparing Qwen vs. Llama
46	
47	These were planned in the experiment design but reduced to numerical tables only.
48	
49	**W3. [Major] Single-seed training.** All experiments use seed=42 only. Bootstrap CIs address eval-time variance but not training variance. If the 30× gap varies significantly across seeds (e.g., 15×–50×), the paper's quantitative claims weaken. The paper acknowledges this (§7.3) but underestimates its impact. At minimum, 2–3 seeds would be needed to establish that the gap magnitude is stable.
50	
51	**W4. [Moderate] Asymmetric cross-model experiments.** Llama gets only a 3-way ablation (no Uniform Gate) while Qwen gets 4-way. Scheduled sampling is tested only on Qwen, not Llama. This asymmetry weakens the "cross-model" narrative and leaves open whether the Llama results would differ under the full experimental protocol.
52	
53	**W5. [Moderate] Narrow scope limiting generalizability.** ThreadGate uses per-layer scalar gates—the simplest possible gating mechanism. The paper does not test vector gates, per-head gates, MLP-based gates, or other heavier parameterizations. The conclusion "lightweight gating struggles" is technically only demonstrated for the lightest-weight variant. This limits the paper's value as a general negative result about gating approaches.
54	
55	**W6. [Moderate] Loss design evolution under-documented.** The paper mentions 7 configurations (v1–v7) across 4 loss families but only presents v7 results. The v1–v6 failures are described in one paragraph (§4.3) without tables, learning curves, or detailed analysis. Since the claim is that the negative result is not due to poor loss design, documenting the full progression is important.
56	
57	**W7. [Minor] No error bars in most tables.** Tables 1–5 and 7 report point estimates without confidence intervals or standard deviations. Only Table 8 provides proper uncertainty quantification.
58	
59	**W8. [Minor] No code/data release mentioned.** Reproducibility would be significantly aided by releasing training code, evaluation scripts, and the specific UltraChat subset used.
60	
61	---
62	
63	## 4. Novelty Assessment
64	
65	The paper's novelty is moderate:
66	- **New**: The specific 30× quantification of training-inference GAR gap under teacher-forcing; the reverse turn conditioning finding; the application of gradient conflict analysis to the NTP–GAR competition on gate parameters.
67	- **Not new**: The underlying mechanisms are compositions of known phenomena—exposure bias (Bengio et al., 2015) and multi-task gradient conflict (Yu et al., 2020; Chen et al., 2018). The paper applies and measures these in a specific new setting rather than discovering new mechanisms.
68	- **Assessment**: The novelty is in the measurement and mechanistic decomposition, not in the phenomena themselves. This is valid but incremental for a top venue.
69	
70	---
71	
72	## 5. Experiment Coverage vs. Design
73	
74	Comparing the paper against the experiment design (review_context.yaml):
75	
76	| Planned Experiment | Status in Paper |
77	|---|---|
78	| Qwen Gradient Conflict (3 checkpoints) | ✅ Covered (Table 6) |
79	| Attention Heatmap Visualization | ⚠️ Reduced to numbers only (Table 7), no actual heatmaps |
80	| Llama Phase 1 GAR Decay | ✅ Covered (Table 1) |
81	| Llama ThreadGate Training | ✅ Covered (Tables 3-4) |
82	| Llama LoRA-only Training | ✅ Covered (Table 3) |
83	| Llama 3-way Eval | ✅ Covered (Table 3) |
84	| Llama Gradient Conflict | ✅ Covered (Table 6) |
85	| Downstream Task Validation | ✅ Covered (Table 5) |
86	| Bootstrap CI | ✅ Covered (Table 8) |
87	| Scheduled Sampling Mitigation | ✅ Covered (Table 9) |
88	
89	All planned experiments are present in some form. The main gap is the downgrade from visual heatmaps to numerical tables.
90	
91	---
92	
93	## 6. Questions for Authors
94	
95	1. **Multi-seed**: Can you run at least one additional training seed to confirm that the 30× gap is stable? Even seed=43 would help.
96	2. **Heavier gates**: Have you considered testing vector gates (per-layer d-dimensional) or per-head gates? This would strengthen the generalizability claim.
97	3. **Figures**: Can you add training curves, gradient heatmaps, and attention visualizations? The numerical results are there; they need visual communication.
98	4. **References**: The broken citations must be fixed—this is the single most important revision.
99	5. **Scheduled sampling on Llama**: Running the SS experiment on Llama would complete the cross-model story.
100	6. **v1–v6 details**: An appendix with v1–v6 training curves and failure modes would strengthen the "not due to poor loss design" argument.
101	
102	---
103	
104	## 7. Scores
105	
106	### R1 (Methods & Experiments)
107	| Dimension | Score | Justification |
108	|---|---|---|
109	| Soundness | 3.5/6 | Solid methodology on Qwen; limited by single seed, small eval, asymmetric Llama experiments |
110	| Significance | 3/6 | Informative negative result but narrow scope (scalar gates, 2 models, 1 dataset) |
111	| Clarity | 3/6 | Good prose quality; severely hurt by broken references and zero figures |
112	| **Overall** | **3/6** | Weak Reject — competent analysis, insufficient scale and presentation for top venue |
113	
114	### R2 (Novelty & Related Work)
115	| Dimension | Score | Justification |
116	|---|---|---|
117	| Novelty | 3/6 | New quantification of known phenomena in a specific domain; mechanistic decomposition is useful but not surprising |
118	| Significance | 3/6 | Informative but narrow; no convincing positive path forward (SS p≈0.07) |
119	| Clarity | 3/6 | Well-organized narrative; broken references + no figures severely limit communication |
120	| **Overall** | **3/6** | Weak Reject — clear story and honest reporting, but limited novelty and presentation quality |
121	
122	### Consolidated
123	| Dimension | Score |
124	|---|---|
125	| Soundness | 3.5/6 |
126	| Novelty | 3/6 |
127	| Significance | 3/6 |
128	| Clarity | 3/6 |
129	| **Overall** | **3/6 (Weak Reject)** |
130	
131	---
132	
133	## 8. Meta-Review
134	
135	Both reviewers converge on 3/6 (Weak Reject). The paper tells a coherent and honest story about a negative result—ThreadGate's failure to transfer training-time GAR improvements to inference—and provides useful mechanistic analysis (gradient competition + distribution shift). The experimental methodology on Qwen is sound, and the statistical analysis (bootstrap CIs, effect sizes) is correctly applied and honestly reported.
136	
137	However, the paper has critical presentation issues (broken references throughout, zero figures in a mechanistic analysis paper) and methodological limitations (single-seed training, asymmetric cross-model experiments, narrow scope restricted to scalar gates). The novelty is moderate: the paper measures known phenomena (exposure bias, multi-task gradient conflict) in a new setting rather than discovering new mechanisms. The scheduled sampling mitigation (p≈0.07) is too weak to constitute a positive contribution.
138	
139	**Verdict**: In its current state, the paper is below the threshold for a top ML venue main track (~25% acceptance). With the following revisions, it could reach borderline acceptance (likely Findings-appropriate):
140	
141	1. **Must fix**: References, add 4–6 figures, run ≥1 additional training seed
142	2. **Should fix**: Symmetric Llama experiments (add Uniform Gate + SS), v1–v6 appendix, error bars in tables
143	3. **Would strengthen**: Heavier gate variants, code release, larger eval set
144	
145	The core research is solid and the findings are useful for the community. The paper's current weakness is primarily in presentation and experimental completeness, not in the underlying science.
146	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "311a4f4b-dfa2-4126-9284-ca7b8b8b9ff8",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "b55b38c5-895f-4487-8945-5a7a2e9f16b3",
  "sourceToolAssistantUUID": "311a4f4b-dfa2-4126-9284-ca7b8b8b9ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T15:39:09.426Z_

Now let me also look at the paper framing for Llama results — the task summary mentions specific numbers I should verify against.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b55b38c5-895f-4487-8945-5a7a2e9f16b3",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBJ45DPpMMu9BV5VEPu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61d4a576-7ece-4fad-bca3-3dcd4b7eb8c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS6pUoRS84QfHzkS56RaCy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6896,
      "cache_read_input_tokens": 52729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T15:39:11.758Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RtPChLjVDF8E6rQ71xWG4P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61d4a576-7ece-4fad-bca3-3dcd4b7eb8c8",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBJ45DPpMMu9BV5VEPu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2e72dff-dc22-4344-9fbb-17b9b17bc1aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS6pUoRS84QfHzkS56RaCy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6896,
      "cache_read_input_tokens": 52729,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 52729,
          "cache_creation_input_tokens": 6896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6896,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T15:39:12.065Z_

<details><summary>↩ Tool result · `toolu_01RtPChLjVDF8E6rQ71xWG4P`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{graphicx}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{hyperref}
13	\usepackage{cleveref}
14	
15	\title{Why Does Gating Fail on Qwen but Not Llama?\\Architecture-Dependent Vulnerability of Auxiliary Attention Loss\\under Training-Inference Distribution Shift}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	% ============================================================
24	\begin{abstract}
25	Multi-turn dialogue performance in large language models degrades as conversations grow longer, with goal attention ratio (GAR) declining by up to 70\% over extended turns.
26	Residual stream probing suggests goal information persists internally even as attention to goal tokens collapses, motivating lightweight residual gating as a remedy.
27	We implement ThreadGate, a per-layer gating module trained with joint next-token prediction (NTP) and GAR auxiliary objectives, and evaluate it on Qwen-2.5-7B and Llama-3.1-8B.
28	Our central finding is that the severity of gating failure is \emph{architecture-dependent}: on Qwen-2.5-7B, ThreadGate achieves a training GAR of 0.48 but collapses to 0.016 at inference (a 30$\times$ gap), with zero incremental benefit over LoRA-only fine-tuning; on Llama-3.1-8B, the gap narrows to 4.6$\times$ and gating yields a weak but measurable +3.5 percentage point GAR improvement.
29	We trace this divergence to NTP--GAR gradient conflict on gate parameters: on Qwen, 67\% of layers exhibit persistent directional conflict (cosine similarity $-0.042$) with NTP magnitude dominance up to 1139$\times$; on Llama, conflict resolves by epoch~2 (cosine similarity $+0.008$) with magnitude ratios below 4$\times$.
30	Scheduled sampling reduces the gap ratio on Qwen from 30$\times$ to 18$\times$, but inference GAR improves by only 0.18 percentage points, indicating that exposure bias is not the sole failure mechanism.
31	These results provide the first architecture-contrastive quantification of how training-inference distribution shift interacts with auxiliary attention losses, revealing that architectural properties---particularly GQA head structure and gradient subspace geometry---determine whether lightweight gating can function at all.
32	\end{abstract}
33	
34	% ============================================================
35	\section{Introduction}
36	\label{sec:intro}
37	
38	Large language models exhibit systematic performance degradation in multi-turn dialogues as conversation length increases \citep{liu2024lost,dongre2026multiturn}.
39	This degradation manifests as declining attention to goal-relevant tokens---such as system prompts and initial user instructions---which \citet{dongre2026multiturn} quantified through the Goal Attention Ratio (GAR), documenting 27--48\% drops across 12 models over 50 turns.
40	
41	A striking observation from \citeauthor{dongre2026multiturn}'s analysis is that goal information \emph{persists} in the residual stream even as the attention channel closes: linear probes achieve AUC up to 0.98 on goal-presence classification from residual representations.
42	This creates a natural architectural hypothesis: if goal information exists in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it.
43	
44	We implement this hypothesis as ThreadGate, a per-layer scalar gate trained with a joint NTP and auxiliary GAR objective.
45	ThreadGate successfully optimizes GAR during teacher-forced training, raising it from 0.02 to 0.48 on Qwen-2.5-7B.
46	However, when we evaluate under autoregressive generation, GAR collapses to 0.016---a 30$\times$ gap.
47	Four-way ablation (ThreadGate vs.\ Uniform Gate vs.\ LoRA-only vs.\ Base) confirms that gating provides zero incremental contribution on Qwen.
48	
49	The natural question is whether this failure is universal or specific to a particular architecture.
50	We replicate the full experimental pipeline on Llama-3.1-8B and find a qualitatively different outcome: the training-inference gap narrows to 4.6$\times$, and ThreadGate yields a weak but measurable +3.5 percentage point GAR improvement over LoRA-only fine-tuning.
51	This architecture-dependent divergence---rather than the failure itself---becomes our central analytical object.
52	
53	We trace the divergence to differences in NTP--GAR gradient conflict on gate parameters.
54	On Qwen, NTP and GAR gradients are persistently anti-aligned (67\% of layers with negative cosine similarity at epoch~2), and NTP magnitude dominates by up to 1139$\times$ at the most affected layer.
55	On Llama, the conflict resolves during training: cosine similarity shifts from $-0.015$ to $+0.008$, and magnitude ratios remain below 4$\times$.
56	This suggests that Llama's architecture provides sufficient gradient subspace freedom for NTP and GAR to coexist, while Qwen's does not.
57	
58	Our contributions are:
59	\begin{enumerate}
60	    \item The first architecture-contrastive quantification of training-inference distribution shift in auxiliary attention losses, showing that the shift severity varies from 4.6$\times$ (Llama) to 30$\times$ (Qwen) under identical training configurations.
61	    \item Layer-wise quantification of NTP--GAR gradient conflict, identifying persistent directional conflict and extreme magnitude dominance as Qwen-specific phenomena.
62	    \item Evidence that exposure bias is not the sole failure mechanism: scheduled sampling reduces the gap ratio by 42\% on Qwen but improves inference GAR by only 0.18 percentage points.
63	    \item Systematic four-way ablation on Qwen and three-way ablation on Llama, establishing that gating benefit is architecture-dependent (zero on Qwen, weakly positive on Llama).
64	\end{enumerate}
65	
66	% ============================================================
67	\section{Related Work}
68	\label{sec:related}
69	
70	\paragraph{Multi-Turn Dialogue Degradation.}
71	The degradation of LLM performance over extended conversations has been documented across multiple dimensions.
72	\citet{liu2024lost} demonstrated the ``lost-in-the-middle'' phenomenon for long-context retrieval.
73	\citet{xiao2024efficient} identified attention sinks---disproportionate attention to initial tokens that may compete with goal-relevant information.
74	\citet{dongre2026multiturn} provided the most systematic study of multi-turn degradation, defining GAR and documenting its decline across 12 model families.
75	MT-Bench-101 \citep{bai2024mtbench101} and MultiChallenge \citep{kamalloo2025multichallenge} provide complementary evaluation frameworks for multi-turn capabilities.
76	
77	\paragraph{Residual Gating and Adaptive Depth.}
78	Learnable gates on residual connections have a rich history.
79	ReZero \citep{bachlechner2021rezero} initializes residual gates to zero, enabling deeper network training.
80	SkipInit \citep{de2020batch} applies learnable scalars to residual branches for stabilization.
81	FlexiDepth \citep{luo2025flexidepth} uses gating for adaptive layer selection at inference time.
82	Our ThreadGate follows the ReZero parameterization ($x + g \cdot f(x)$) but repurposes gating for attention steering rather than training stability.
83	
84	\paragraph{Attention Steering and Intervention.}
85	Prior work on directing attention includes attention supervision \citep{liu2016attention}, where auxiliary losses encourage attention to align with human rationales.
86	\citet{qiu2025gated} proposed gated attention mechanisms for selective information routing.
87	Inference-time attention intervention \citep{li2023inference} modifies attention patterns without training, avoiding the distribution shift problem we identify.
88	Activation steering \citep{turner2023activation} operates on residual stream representations directly.
89	
90	\paragraph{Exposure Bias.}
91	The mismatch between teacher-forced training and autoregressive inference was formalized by \citet{bengio2015scheduled}, who proposed scheduled sampling as mitigation.
92	Professor Forcing \citep{lamb2016professor} uses adversarial training to align teacher-forced and free-running dynamics.
93	SEARNN \citep{leblond2018searnn} reformulates sequence generation as a search problem.
94	While exposure bias is well-studied for generation quality, its impact on \emph{auxiliary attention losses} has not been previously quantified.
95	
96	\paragraph{Multi-Task Gradient Conflict.}
97	Gradient conflict in multi-task learning is well-documented \citep{yu2020gradient,liu2021conflict}.
98	PCGrad \citep{yu2020gradient} projects conflicting gradients to reduce interference.
99	Our gradient analysis reveals that NTP--GAR conflict on gate parameters follows architecture-specific patterns, connecting multi-task optimization to architectural properties.
100	
101	% ============================================================
102	\section{Background}
103	\label{sec:background}
104	
105	\subsection{Goal Attention Ratio}
106	
107	Following \citet{dongre2026multiturn}, we define the Goal Attention Ratio as the fraction of attention mass allocated to goal-relevant tokens.
108	Let $\mathbf{a}_t \in \mathbb{R}^{|s|}$ denote the attention weights from response tokens at turn $t$ to goal tokens $s$ (the system prompt), averaged across heads and layers.
109	The GAR at turn $t$ is:
110	\begin{equation}
111	    \text{GAR}(t) = \frac{1}{|R_t|} \sum_{i \in R_t} \sum_{j \in s} a_{ij}
112	\end{equation}
113	where $R_t$ is the set of response token positions at turn $t$.
114	
115	We use two evaluation definitions: \textbf{GAR-Dongre}, which uses system prompt task tokens as goals and averages over all response tokens (comparable to \citeauthor{dongre2026multiturn}), and \textbf{GAR-ours}, which uses system prompt plus first user query as goals and evaluates at the last response token per turn (used as training signal).
116	
117	\subsection{Residual Stream Persistence}
118	
119	\citet{dongre2026multiturn} showed via linear probing that goal information persists in the residual stream with AUC up to 0.98, even at turns where GAR has dropped below 0.01.
120	This decoupling of attention-level access from representation-level persistence motivates residual-level intervention: if the information is present but inaccessible via attention, modulating the residual pathway should help.
121	
122	% ============================================================
123	\section{Method}
124	\label{sec:method}
125	
126	\subsection{ThreadGate Architecture}
127	
128	ThreadGate adds a learnable scalar gate $g_l \in \mathbb{R}$ to each transformer layer $l$, following the ReZero parameterization:
129	\begin{equation}
130	    \mathbf{x}_{l+1} = \mathbf{x}_l + g_l \cdot f_l(\mathbf{x}_l)
131	    \label{eq:threadgate}
132	\end{equation}
133	where $f_l$ denotes the sub-layer computation (self-attention or feed-forward).
134	When $g_l \to 0$, the sub-layer output is suppressed and the layer acts as an identity; when $g_l = 1$, the standard residual connection is recovered.
135	Gates are initialized to 1.0 (standard behavior) and trained jointly with LoRA adapters (rank 8) on the attention projection matrices.
136	
137	\subsection{Training Objective}
138	
139	The training loss combines NTP with a GAR auxiliary objective:
140	\begin{equation}
141	    \mathcal{L} = \mathcal{L}_{\text{NTP}} + \lambda_{\text{MSE}} \cdot \mathcal{L}_{\text{MSE}} + \lambda_{\text{div}} \cdot \mathcal{L}_{\text{div}}
142	\end{equation}
143	
144	The MSE component targets a reference GAR profile:
145	\begin{equation}
146	    \mathcal{L}_{\text{MSE}} = \frac{1}{T}\sum_{t=1}^{T} \left(\text{GAR}(t) - \text{GAR}_{\text{target}}(t)\right)^2
147	\end{equation}
148	where the target is derived from the turn-1 attention pattern, encouraging the model to maintain early-turn goal attention throughout the conversation.
149	
150	The gate diversity term $\mathcal{L}_{\text{div}}$ penalizes gate collapse (all gates converging to the same value), ensuring per-layer specialization.
151	
152	\subsection{Loss Design Evolution}
153	
154	The final MSE+gate\_div formulation (v7) was reached after six prior configurations spanning four loss families: cumulative GAR maximization (v1--v2), direct GAR maximization (v3--v5), smooth saturation (v6), and MSE targeting (v7).
155	Only v7 achieved stable training convergence with monotonic GAR improvement, confirming that bidirectional MSE targeting is necessary for stable GAR optimization under NTP co-training.
156	
157	% ============================================================
158	\section{Experimental Setup}
159	\label{sec:setup}
160	
161	\paragraph{Models.}
162	We evaluate on Qwen-2.5-7B \citep{qwen2025qwen25} and Llama-3.1-8B \citep{dubey2024llama3}, representing two distinct GQA architectures.
163	Qwen uses 28 layers with 7 KV head groups; Llama uses 32 layers with 8 KV head groups.
164	Both use RMSNorm and RoPE positional encoding with different implementations.
165	
166	\paragraph{Training.}
167	All models are trained for 3 epochs on the UltraChat multi-turn dialogue dataset with identical hyperparameters: learning rate $2 \times 10^{-4}$, LoRA rank 8, batch size 4, seed 42.
168	Training takes 5.9--9.5 hours on a single GPU depending on configuration.
169	
170	\paragraph{Evaluation.}
171	We evaluate on 50 held-out multi-turn conversations using both GAR definitions and perplexity (PPL).
172	For Qwen, we conduct four-way comparison: Base, ThreadGate (TG), Uniform Gate (UG, non-learned gate), and LoRA-only (no gate).
173	For Llama, we conduct three-way comparison: Base, ThreadGate, and LoRA-only.
174	
175	\paragraph{Statistical Testing.}
176	We use paired bootstrap with 10,000 resamples to construct 95\% confidence intervals for TG--LoRA differences on Qwen.
177	
178	% ============================================================
179	\section{Results}
180	\label{sec:results}
181	
182	\subsection{GAR Degradation is Architecture-Dependent}
183	\label{sec:gar_degradation}
184	
185	We first establish that the baseline severity of GAR degradation differs substantially between architectures.
186	
187	\begin{table}[h]
188	\centering
189	\small
190	\caption{Cross-model GAR degradation in base models (no fine-tuning). Qwen exhibits severe monotonic decline; Llama shows moderate non-monotonic degradation.}
191	\label{tab:gar_degradation}
192	\begin{tabular}{lcccc}
193	\toprule
194	\textbf{Model} & \textbf{Turn 1} & \textbf{Mid-Turn} & \textbf{Rel.\ Drop} & \textbf{Pattern} \\
195	\midrule
196	Qwen-2.5-7B & 0.0418 & 0.0122 & 70.8\% & Monotonic \\
197	Llama-3.1-8B & 0.0380 & 0.0284 & 25.3\% & Non-monotonic \\
198	\bottomrule
199	\end{tabular}
200	\end{table}
201	
202	Despite similar Turn-1 GAR values (0.042 vs.\ 0.038), the architectures diverge sharply over turns: Qwen's GAR drops by 70.8\% to 0.012, while Llama's drops by only 25.3\% to 0.028.
203	Llama's non-monotonic pattern---with fluctuations and a partial recovery at turn~9---suggests qualitatively different attention dynamics, potentially reflecting more distributed attention head utilization.
204	This baseline difference is consequential: Llama starts from a less degraded state, meaning even a small gating intervention may produce a measurable effect.
205	
206	\subsection{Training-Inference Gap: 30$\times$ on Qwen, 4.6$\times$ on Llama}
207	\label{sec:gap}
208	
209	ThreadGate training converges successfully on both architectures, achieving training GAR of 0.48 (Qwen) and 0.42 (Llama).
210	However, the training-inference gap differs by an order of magnitude.
211	
212	\begin{table}[h]
213	\centering
214	\small
215	\caption{Training-inference GAR gap comparison. The gap is 6--7$\times$ more severe on Qwen than on Llama under both evaluation definitions.}
216	\label{tab:gap}
217	\begin{tabular}{lccccc}
218	\toprule
219	\textbf{Model} & \textbf{Train GAR} & \textbf{Infer GAR-ours} & \textbf{Gap (ours)} & \textbf{Infer GAR-D} & \textbf{Gap (D)} \\
220	\midrule
221	Qwen-2.5-7B & 0.48 & 0.0157 & 30.6$\times$ & 0.0152 & 31.6$\times$ \\
222	Llama-3.1-8B & 0.42 & 0.092 & 4.6$\times$ & 0.0485 & 8.7$\times$ \\
223	\bottomrule
224	\end{tabular}
225	\end{table}
226	
227	On Qwen, inference GAR (0.016) is indistinguishable from the untrained base model, indicating complete failure of training-time GAR optimization to transfer.
228	On Llama, inference GAR reaches 0.092 (GAR-ours) and 0.049 (GAR-Dongre)---substantially above the Llama base (0.015 / 0.004), suggesting partial transfer.
229	The 6--7$\times$ difference in gap severity between architectures is our primary finding.
230	
231	\subsection{Gating Benefit: Zero on Qwen, Weakly Positive on Llama}
232	\label{sec:ablation}
233	
234	We isolate gating contribution via controlled ablation.
235	
236	\begin{table}[h]
237	\centering
238	\small
239	\caption{Four-way ablation on Qwen-2.5-7B. Gating provides no incremental benefit over LoRA-only fine-tuning; all fine-tuned variants converge to identical GAR and PPL.}
240	\label{tab:qwen_ablation}
241	\begin{tabular}{lcccc}
242	\toprule
243	\textbf{Model} & \textbf{GAR-Dongre} & \textbf{GAR-ours} & \textbf{PPL} & \textbf{NTP Loss} \\
244	\midrule
245	Base & 0.0035 & 0.0120 & 4.23 & 1.432 \\
246	ThreadGate & 0.0152 & 0.0157 & 2.63 & 0.982 \\
247	Uniform Gate & 0.0148 & 0.0149 & 2.62 & 0.980 \\
248	LoRA-only & 0.0132 & 0.0100 & 2.63 & 0.978 \\
249	\bottomrule
250	\end{tabular}
251	\end{table}
252	
253	On Qwen, TG--LoRA differences are negligible: +0.20 percentage points (GAR-Dongre) and +0.57pp (GAR-ours), with identical PPL (2.63).
254	The Uniform Gate---a non-learned constant gate---performs identically to ThreadGate, confirming that learned turn-selective gating provides no advantage.
255	
256	\begin{table}[h]
257	\centering
258	\small
259	\caption{Three-way ablation on Llama-3.1-8B. ThreadGate provides a weak but measurable GAR improvement over LoRA-only, contrasting sharply with the zero benefit observed on Qwen.}
260	\label{tab:llama_ablation}
261	\begin{tabular}{lcccc}
262	\toprule
263	\textbf{Model} & \textbf{GAR-Dongre} & \textbf{GAR-ours} & \textbf{PPL} & \textbf{NTP Loss} \\
264	\midrule
265	Base & 0.0035 & 0.0145 & 4.55 & 1.432 \\
266	ThreadGate & 0.0485 & 0.092 & 2.95 & 0.982 \\
267	LoRA-only & 0.0132 & 0.058 & 2.98 & 0.978 \\
268	\bottomrule
269	\end{tabular}
270	\end{table}
271	
272	On Llama, TG outperforms LoRA-only by +3.53pp (GAR-Dongre) and +3.40pp (GAR-ours), with a marginal PPL improvement ($-0.03$).
273	While modest in absolute terms, this positive increment stands in stark contrast to the zero benefit on Qwen.
274	
275	\begin{table}[h]
276	\centering
277	\small
278	\caption{Cross-model comparison of gating benefit. The architecture determines whether gating provides any incremental value.}
279	\label{tab:cross_model_benefit}
280	\begin{tabular}{lcccc}
281	\toprule
282	\textbf{Model} & \textbf{TG--LoRA (D, pp)} & \textbf{TG--LoRA (ours, pp)} & \textbf{TG--LoRA PPL} & \textbf{Benefit?} \\
283	\midrule
284	Qwen-2.5-7B & +0.20 & +0.57 & 0.00 & None \\
285	Llama-3.1-8B & +3.53 & +3.40 & $-0.03$ & Weak positive \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	\subsection{Gradient Conflict Explains the Architecture Divergence}
291	\label{sec:gradient}
292	
293	To understand \emph{why} gating fails on Qwen but partially succeeds on Llama, we analyze NTP--GAR gradient conflict on gate parameters across training.
294	
295	For each layer $l$, we compute the cosine similarity between the NTP gradient $\nabla_{g_l}\mathcal{L}_{\text{NTP}}$ and the GAR gradient $\nabla_{g_l}\mathcal{L}_{\text{GAR}}$, along with their magnitude ratio $\|\nabla_{g_l}\mathcal{L}_{\text{NTP}}\| / \|\nabla_{g_l}\mathcal{L}_{\text{GAR}}\|$.
296	
297	\begin{table}[h]
298	\centering
299	\small
300	\caption{NTP--GAR gradient conflict across training on Qwen-2.5-7B. Directional conflict weakens not because the objectives harmonize, but because GAR signal is marginalized (rising magnitude ratio).}
301	\label{tab:qwen_gradient}
302	\begin{tabular}{lcccc}
303	\toprule
304	\textbf{Checkpoint} & \textbf{cos\_sim (mean$\pm$std)} & \textbf{\% layers cos$<$0} & \textbf{mag\_ratio (mean)} & \textbf{mag\_ratio (L27)} \\
305	\midrule
306	Epoch 0 (gs 2650) & $-0.089 \pm 0.12$ & 79\% & 7.5$\times$ & 135$\times$ \\
307	Epoch 1 (gs 5300) & $-0.061 \pm 0.11$ & 71\% & 11.2$\times$ & 487$\times$ \\
308	Epoch 2 (gs 7950) & $-0.042 \pm 0.10$ & 67\% & 14.7$\times$ & 1139$\times$ \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	On Qwen, 18 of 28 layers maintain persistently negative cosine similarity throughout training.
314	The apparent reduction in conflict (from $-0.089$ to $-0.042$) is misleading: the NTP magnitude ratio simultaneously increases from 7.5$\times$ to 14.7$\times$ (mean) and from 135$\times$ to 1139$\times$ at L27, indicating that GAR is not reconciling with NTP but being silenced.
315	
316	\begin{table}[h]
317	\centering
318	\small
319	\caption{Cross-model gradient conflict comparison at key checkpoints. Llama resolves the initial conflict by epoch 2; Qwen does not.}
320	\label{tab:gradient_cross}
321	\begin{tabular}{lccc}
322	\toprule
323	\textbf{Metric} & \textbf{Qwen-2.5-7B} & \textbf{Llama-3.1-8B} & \textbf{Interpretation} \\
324	\midrule
325	cos\_sim (epoch 0) & $-0.089$ & $-0.015$ & Qwen: 6$\times$ stronger initial conflict \\
326	cos\_sim (epoch 2) & $-0.042$ & $+0.008$ & Llama resolves; Qwen retains \\
327	\% layers cos$<$0 (ep.\ 2) & 67\% & 41\% & Majority of Llama layers non-conflicting \\
328	mag\_ratio (epoch 2) & 14.7$\times$ & 3.5$\times$ & NTP dominance 4$\times$ weaker on Llama \\
329	Top layer mag\_ratio & 1139$\times$ (L27) & 18.5$\times$ (L31) & Extreme suppression is Qwen-specific \\
330	Persistent neg.\ layers & 18/28 & 6/32 & Llama: only 19\% of layers persistently conflicting \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	The contrast is striking.
336	Llama's gradient conflict is mild from the start ($-0.015$) and resolves to a positive mean ($+0.008$) by epoch~2, with 59\% of layers achieving non-negative cosine similarity.
337	The maximum magnitude ratio (18.5$\times$ at L31) is two orders of magnitude smaller than Qwen's (1139$\times$ at L27).
338	Only 6 of 32 layers show persistent negative cosine similarity, compared to 18 of 28 on Qwen.
339	
340	This gradient analysis provides a mechanistic explanation for the architecture-dependent gating benefit: on Llama, NTP and GAR can find partially orthogonal gradient subspaces, allowing the gate to learn meaningful GAR-related adjustments without being fully overridden by NTP.
341	On Qwen, the competition is zero-sum---NTP progressively silences GAR, causing gates to learn NTP-aligned behavior (near-identity at late turns where NTP loss is highest).
342	
343	\subsection{Attention Visualization Confirms Gate Inefficacy}
344	\label{sec:attention}
345	
346	We extract attention patterns across 28 layers for four Qwen model variants (Base, TG, UG, LoRA-only) on three held-out conversations, measuring goal token attention at each turn.
347	
348	\begin{table}[h]
349	\centering
350	\small
351	\caption{Goal token attention across turns on Qwen-2.5-7B, averaged over layers and conversations. All four models exhibit nearly identical attention patterns; gate effects are invisible at the attention level.}
352	\label{tab:attention}
353	\begin{tabular}{lccccc}
354	\toprule
355	\textbf{Model} & \textbf{Turn 1} & \textbf{Turn 5} & \textbf{Turn 10} & \textbf{Turn 20} & \textbf{Rel.\ Drop} \\
356	\midrule
357	Base & 0.042 & 0.018 & 0.008 & 0.005 & 88.1\% \\
358	ThreadGate & 0.039 & 0.017 & 0.009 & 0.005 & 87.2\% \\
359	Uniform Gate & 0.041 & 0.018 & 0.008 & 0.005 & 87.8\% \\
360	LoRA-only & 0.040 & 0.017 & 0.009 & 0.005 & 87.5\% \\
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	The cross-model attention pattern correlation is 0.97, and zero layers show any visible gate effect.
366	This confirms that gates attenuating sub-layer outputs by only 2--7\% (gate mean 0.93--0.98 at inference) are far too weak to alter attention distributions.
367	The attention visualization underscores the severity of the training-inference disconnect on Qwen: despite training GAR reaching 0.48, the inference attention landscape is indistinguishable across all model variants.
368	
369	\subsection{Scheduled Sampling Does Not Bridge the Gap}
370	\label{sec:mitigation}
371	
372	To test whether exposure bias is the primary mechanism behind the 30$\times$ gap on Qwen, we train ThreadGate with scheduled sampling, progressively replacing teacher-forced context with model-generated context (linear schedule from 100\% teacher-forcing at epoch~0 to 50\% model-generated at epoch~2).
373	
374	\begin{table}[h]
375	\centering
376	\small
377	\caption{Scheduled sampling results on Qwen-2.5-7B. The gap ratio decreases (from 30.6$\times$ to 17.7$\times$), but this is driven by lower training GAR, not higher inference GAR. Actual inference improvement is negligible.}
378	\label{tab:mitigation}
379	\begin{tabular}{lccc}
380	\toprule
381	\textbf{Metric} & \textbf{Baseline (TG v7)} & \textbf{Scheduled Sampling} & \textbf{Change} \\
382	\midrule
383	Training GAR (final) & 0.48 & 0.31 & $-0.17$ ($\downarrow$35\%) \\
384	Inference GAR-ours & 0.0157 & 0.0175 & +0.18pp ($\uparrow$11\%) \\
385	Inference GAR-Dongre & 0.0152 & 0.0165 & +0.13pp ($\uparrow$9\%) \\
386	Train--Infer Gap (ours) & 30.6$\times$ & 17.7$\times$ & $\downarrow$42\% \\
387	PPL & 2.63 & 2.72 & +0.09 ($\uparrow$3.4\%) \\
388	Training Time & 5.9h & 9.5h & +61\% \\
389	\bottomrule
390	\end{tabular}
391	\end{table}
392	
393	The gap ratio reduction from 30.6$\times$ to 17.7$\times$ is superficially encouraging but misleading: it is driven almost entirely by the reduction in training GAR (from 0.48 to 0.31, as model-generated context provides a harder optimization target), not by improvement in inference GAR (0.0157 $\to$ 0.0175, a mere 0.18pp increase).
394	The actual inference-time benefit is negligible despite 61\% additional training cost.
395	
396	This result has important implications: if exposure bias were the dominant failure mechanism, exposing the model to its own generated context during training should substantially improve inference GAR.
397	The failure of scheduled sampling to do so suggests that NTP--GAR gradient competition is an independent and possibly more important failure mechanism that operates regardless of context distribution.
398	
399	\subsection{Downstream Task Validation}
400	\label{sec:downstream}
401	
402	To assess whether GAR degradation corresponds to observable behavioral changes, we evaluate instruction compliance---whether models continue following system prompt directives (e.g., ``always respond in bullet points'') across turns.
403	
404	\begin{table}[h]
405	\centering
406	\small
407	\caption{Instruction compliance rate across turns on Qwen-2.5-7B. All models show similar compliance decay; gating provides no downstream benefit.}
408	\label{tab:compliance}
409	\begin{tabular}{lccccc}
410	\toprule
411	\textbf{Model} & \textbf{Turn 1} & \textbf{Turn 5} & \textbf{Turn 10} & \textbf{Turn 15} & \textbf{Turn 20} \\
412	\midrule
413	Base & 0.85 & 0.74 & 0.62 & 0.55 & 0.48 \\
414	ThreadGate & 0.87 & 0.76 & 0.63 & 0.56 & 0.50 \\
415	LoRA-only & 0.86 & 0.75 & 0.64 & 0.56 & 0.49 \\
416	Uniform Gate & 0.86 & 0.75 & 0.63 & 0.55 & 0.49 \\
417	\bottomrule
418	\end{tabular}
419	\end{table}
420	
421	All models exhibit consistent compliance degradation from $\sim$86\% at turn~1 to $\sim$49\% at turn~20.
422	The TG--LoRA compliance difference at turn~20 is 1 percentage point (0.50 vs.\ 0.49), confirming that the zero gating benefit on Qwen extends to downstream behavior.
423	The GAR--compliance correlation is 0.35 (weak positive), indicating that while GAR captures part of the degradation mechanism, compliance is influenced by factors beyond attention-to-goal alone.
424	
425	\subsection{Statistical Analysis}
426	\label{sec:stats}
427	
428	We validate the ``zero benefit'' claim on Qwen using paired bootstrap confidence intervals (10,000 resamples, 50 conversations).
429	
430	\begin{table}[h]
431	\centering
432	\small
433	\caption{Paired bootstrap 95\% CI for TG minus LoRA-only on Qwen-2.5-7B. Under the primary evaluation (GAR-Dongre), the CI includes zero, supporting the zero-benefit claim. Under GAR-ours, a statistically significant but sub-1pp effect is detected.}
434	\label{tab:bootstrap}
435	\begin{tabular}{lcccc}
436	\toprule
437	\textbf{Metric} & \textbf{Mean Diff} & \textbf{95\% CI} & \textbf{Includes 0?} & \textbf{Interpretation} \\
438	\midrule
439	GAR-Dongre (mid) & +0.20pp & [$-$0.25, +0.68] & Yes & Zero benefit \\
440	GAR-ours (mid) & +0.57pp & [+0.12, +1.05] & No & Sub-1pp positive \\
441	PPL & 0.00 & [$-$0.02, +0.02] & Yes & No impact \\
442	\bottomrule
443	\end{tabular}
444	\end{table}
445	
446	Under GAR-Dongre (our primary evaluation, comparable to \citeauthor{dongre2026multiturn}), the CI includes zero, statistically supporting the zero-benefit conclusion.
447	Under GAR-ours, a statistically significant but practically negligible effect (+0.57pp, CI [+0.12, +1.05]) is detected.
448	This sub-1pp effect likely reflects residual training signal at the last-token position used in the GAR-ours definition, rather than a meaningful gating contribution.
449	PPL is unaffected by gating under either definition.
450	
451	% ============================================================
452	\section{Analysis}
453	\label{sec:analysis}
454	
455	\subsection{What Architectural Properties Drive the Divergence?}
456	
457	The gradient conflict analysis (\Cref{sec:gradient}) reveals that the key difference is not in whether NTP--GAR conflict \emph{exists}---it does on both architectures at initialization---but in whether it \emph{resolves}.
458	We hypothesize three architectural factors:
459	
460	\paragraph{GQA Head Count.}
461	Llama-3.1-8B uses 8 KV head groups versus Qwen's 7.
462	More independent KV heads provide additional gradient subspace dimensions, allowing NTP and GAR to partially segregate across different head groups.
463	This is consistent with Llama achieving positive mean cosine similarity (+0.008) by epoch~2: the objectives have found partially non-overlapping parameter subspaces.
464	
465	\paragraph{Attention Distribution Breadth.}
466	Llama's baseline GAR degradation is less severe (25\% vs.\ 71\%), suggesting a more distributed baseline attention pattern.
467	If attention to goal tokens does not concentrate as strongly in the first place, the ``competition'' for attention mass between goal and context tokens is less intense, and a small gate perturbation can produce a measurable shift.
468	
469	\paragraph{Pre-training Scale.}
470	Llama-3.1 was trained on approximately 15T tokens versus Qwen-2.5's estimated 3--7T.
471	Larger pre-training corpora may produce more robust attention patterns that are less susceptible to extreme redistribution under fine-tuning, reducing the severity of teacher-forcing distribution shift.
472	
473	\subsection{Why Scheduled Sampling Fails}
474	
475	The scheduled sampling experiment (\Cref{sec:mitigation}) demonstrates that reducing context distribution mismatch alone is insufficient.
476	Even when the model trains on 50\% self-generated context, inference GAR improves by only 0.18pp.
477	This is because NTP--GAR gradient competition operates \emph{regardless of context source}: on model-generated context, NTP loss is actually \emph{higher} (due to higher perplexity), producing even stronger NTP gradients that further suppress GAR.
478	The result is a paradox: scheduled sampling reduces the distribution shift but amplifies the gradient competition, leaving inference GAR virtually unchanged.
479	
480	This finding establishes that the 30$\times$ gap on Qwen results from at least two entangled mechanisms---distribution shift and gradient competition---and that mitigating one without addressing the other is ineffective.
481	
482	\subsection{Gate Profile Inversion}
483	
484	On both architectures, gates exhibit a counterintuitive turn-dependent profile: attenuation is \emph{stronger} at early turns (where GAR is already high) and \emph{weaker} at late turns (where intervention is needed most).
485	On Qwen, 27 of 28 layers show this inverted pattern; on Llama, 18 of 32 layers do.
486	The inversion results from NTP gradient pressure: at late turns, NTP loss is higher (more tokens to predict with longer context), producing stronger gradients that push gates toward 1.0 (identity), disabling the gate's attenuating effect precisely when it is most needed.
487	
488	\subsection{Implications for Auxiliary Attention Loss Methods}
489	
490	Our results suggest that the viability of auxiliary attention losses trained under teacher-forcing depends critically on the target architecture's gradient subspace geometry.
491	Architectures where NTP can fully dominate auxiliary gradients (as in Qwen) will see complete failure of training-time attention steering to transfer to inference.
492	Architectures with more gradient subspace freedom (as in Llama) may see partial transfer, but the effect remains weak (3.5pp in our experiments).
493	
494	This has practical implications for the growing body of work on attention steering \citep{dongre2026multiturn,qiu2025gated}: any method that relies on teacher-forced training with auxiliary attention objectives should validate on multiple architectures, as architecture-specific gradient dynamics may silently nullify the intervention on some models.
495	
496	% ============================================================
497	\section{Discussion}
498	\label{sec:discussion}
499	
500	\paragraph{Scope of Claims.}
501	Our findings are specific to lightweight scalar gating with MSE-based GAR auxiliary losses.
502	We do not claim that all attention steering methods are doomed---in particular, inference-time interventions \citep{li2023inference,turner2023activation} bypass the training-inference distribution shift entirely.
503	Heavier architectural modifications (e.g., dedicated goal-processing pathways with separate attention heads) might also overcome the gradient competition by providing dedicated parameter subspaces.
504	
505	\paragraph{Limitations.}
506	We evaluate two architectures with a single training seed.
507	While the bootstrap CI provides variance estimates for evaluation, training variance across seeds is not characterized.
508	The downstream evaluation (instruction compliance) uses a simple proxy task; more comprehensive multi-turn benchmarks would strengthen the connection between GAR and real-world performance.
509	The weak GAR--compliance correlation (0.35) suggests that attention-to-goal is only one component of multi-turn degradation.
510	
511	\paragraph{Future Directions.}
512	Our analysis points to several promising directions:
513	(1) \emph{Inference-time attention intervention}: directly modifying attention patterns at generation time circumvents the distribution shift problem;
514	(2) \emph{Gradient-conflict-aware training}: techniques from multi-task optimization (e.g., PCGrad; \citealp{yu2020gradient}) could manage NTP--GAR interference;
515	(3) \emph{Decoupled goal-processing pathways}: architectures with dedicated goal-attention heads that are not subject to NTP gradient pressure;
516	(4) \emph{Architecture-aware auxiliary loss design}: calibrating auxiliary loss strength and targeting based on the specific architecture's gradient subspace capacity.
517	
518	% ============================================================
519	\section{Conclusion}
520	\label{sec:conclusion}
521	
522	We presented a contrastive analysis of lightweight residual gating for multi-turn attention degradation across two architectures.
523	Our experiments reveal that gating failure is not universal but architecture-dependent: Qwen-2.5-7B exhibits a 30$\times$ training-inference GAR gap with zero gating benefit, while Llama-3.1-8B shows a 4.6$\times$ gap with a weak positive effect (+3.5pp).
524	The divergence is explained by NTP--GAR gradient conflict severity, which is persistent and extreme on Qwen (1139$\times$ magnitude dominance at the most affected layer) but resolves on Llama (magnitude ratios below 4$\times$).
525	Scheduled sampling fails to bridge the gap, establishing that exposure bias and gradient competition are entangled failure mechanisms.
526	These findings provide the first architecture-contrastive evidence that auxiliary attention loss viability depends on the target model's gradient subspace geometry, and suggest that future attention steering methods must account for architecture-specific gradient dynamics.
527	
528	% ============================================================
529	\begin{thebibliography}{25}
530	
531	\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}
532	T.~Bachlechner, B.~P.~Majumder, H.~Mao, G.~Cottrell, and J.~McAuley. {ReZero} is all you need: Fast convergence at large depth. In \emph{Proc. UAI}, 2021.
533	
534	\bibitem[Bai et~al.(2024)]{bai2024mtbench101}
535	G.~Bai, J.~Liu, X.~Bu, Y.~He, J.~Liu, Z.~Zhou, Z.~Lin, W.~Su, T.~Liang, J.~Xu, et~al. {MT-Bench-101}: A fine-grained benchmark for evaluating large language models in multi-turn dialogue. In \emph{Proc. ACL}, 2024.
536	
537	\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}
538	S.~Bengio, O.~Vinyals, N.~Jaitly, and N.~Shazeer. Scheduled sampling for sequence prediction with recurrent neural networks. In \emph{Proc. NeurIPS}, 2015.
539	
540	\bibitem[De and Smith(2020)]{de2020batch}
541	S.~De and S.~L.~Smith. Batch normalization biases residual blocks towards the identity function in deep networks. In \emph{Proc. NeurIPS}, 2020.
542	
543	\bibitem[Dongre et~al.(2026)]{dongre2026multiturn}
544	A.~Dongre, A.~Abzaliev, and K.~R.~Narasimhan. Multi-turn attention degradation in large language models. \emph{Preprint}, 2026.
545	
546	\bibitem[Dubey et~al.(2024)]{dubey2024llama3}
547	A.~Dubey et~al. The {Llama} 3 herd of models. \emph{arXiv preprint arXiv:2407.21783}, 2024.
548	
549	\bibitem[Elhage et~al.(2021)]{elhage2021mathematical}
550	N.~Elhage, N.~Nanda, C.~Olsson, et~al. A mathematical framework for transformer circuits. \emph{Transformer Circuits Thread}, 2021.
551	
552	\bibitem[Kamalloo et~al.(2025)]{kamalloo2025multichallenge}
553	E.~Kamalloo, A.~Jafari, P.~Ennen, A.~Gheibi, and A.~Ghodsi. {MultiChallenge}: A realistic multi-turn dialogue benchmark for evaluating LLMs. \emph{Preprint}, 2025.
554	
555	\bibitem[Ko et~al.(2024)]{ko2024found}
556	S.~Ko, J.~Lee, and M.~Seo. Found in the middle: How language models use long contexts better via plug-and-play positional encoding. In \emph{Proc. ACL Findings}, 2024.
557	
558	\bibitem[Lamb et~al.(2016)]{lamb2016professor}
559	A.~Lamb, A.~Goyal, Y.~Zhang, S.~Zhang, A.~Courville, and Y.~Bengio. Professor forcing: A new algorithm for training recurrent networks. In \emph{Proc. NeurIPS}, 2016.
560	
561	\bibitem[Leblond et~al.(2018)]{leblond2018searnn}
562	R.~Leblond, J.-B.~Alayrac, A.~Osokin, and S.~Lacoste-Julien. {SEARNN}: Training {RNN}s with global-local losses. In \emph{Proc. ICLR}, 2018.
563	
564	\bibitem[Li et~al.(2023)]{li2023inference}
565	K.~Li, O.~Patel, F.~Vi{\'e}gas, H.~Pfister, and M.~Wattenberg. Inference-time intervention: Eliciting truthful answers from a language model. In \emph{Proc. NeurIPS}, 2023.
566	
567	\bibitem[Liu et~al.(2016)]{liu2016attention}
568	L.~Liu, M.~Utiyama, A.~Finch, and E.~Sumita. Neural machine translation with supervised attention. In \emph{Proc. COLING}, 2016.
569	
570	\bibitem[Liu et~al.(2024)]{liu2024lost}
571	N.~F.~Liu, K.~Lin, J.~Hewitt, A.~Paranjape, M.~Bevilacqua, F.~Petroni, and P.~Liang. Lost in the middle: How language models use long contexts. \emph{TACL}, 2024.
572	
573	\bibitem[Liu et~al.(2021)]{liu2021conflict}
574	S.~Liu, E.~Johns, and A.~J.~Davison. Conflict-averse gradient descent for multi-task learning. In \emph{Proc. NeurIPS}, 2021.
575	
576	\bibitem[Luo et~al.(2025)]{luo2025flexidepth}
577	Y.~Luo, H.~Xiong, and L.~Kong. {FlexiDepth}: Dynamic depth inference for efficient transformers. \emph{Preprint}, 2025.
578	
579	\bibitem[Qiu et~al.(2025)]{qiu2025gated}
580	L.~Qiu, H.~Sun, and Y.~Yang. Gated attention for selective information routing. In \emph{Proc. NAACL}, 2025.
581	
582	\bibitem[{Qwen Team}(2025)]{qwen2025qwen25}
583	{Qwen Team}. Qwen2.5 technical report. \emph{arXiv preprint arXiv:2412.15115}, 2025.
584	
585	\bibitem[Turner et~al.(2023)]{turner2023activation}
586	A.~M.~Turner, L.~Thiergart, D.~Udell, G.~Leech, U.~Mini, and M.~MacDiarmid. Activation addition: Steering language models without optimization. \emph{arXiv preprint arXiv:2308.10248}, 2023.
587	
588	\bibitem[Xiao et~al.(2024)]{xiao2024efficient}
589	G.~Xiao, Y.~Tian, B.~Chen, S.~Han, and M.~Lewis. Efficient streaming language models with attention sinks. In \emph{Proc. ICLR}, 2024.
590	
591	\bibitem[Yu et~al.(2020)]{yu2020gradient}
592	T.~Yu, S.~Kumar, A.~Gupta, S.~Levine, K.~Hausman, and C.~Finn. Gradient surgery for multi-task learning. In \emph{Proc. NeurIPS}, 2020.
593	
594	\end{thebibliography}
595	
596	\end{document}
597	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2e72dff-dc22-4344-9fbb-17b9b17bc1aa",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "e6ba850b-6292-4fda-929c-b7603ceec1b1",
  "sourceToolAssistantUUID": "c2e72dff-dc22-4344-9fbb-17b9b17bc1aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-19T15:39:15.531Z_

Now I have a thorough understanding of both paper versions and the full experimental context. Let me also check the "best" version's review report to understand the cross-version differences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6ba850b-6292-4fda-929c-b7603ceec1b1",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBJUGkWAQdTHe8bTxCj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f764bf7a-3193-412c-b925-51df29ce4667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqFmtsX1NDiXFPn7Ebsfhc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 59625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T15:39:17.717Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LrnQdqH8s3oHEe8hBWDoPj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f764bf7a-3193-412c-b925-51df29ce4667",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBJUGkWAQdTHe8bTxCj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "196f0992-e362-4e67-8e68-f8a1d0098c62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqFmtsX1NDiXFPn7Ebsfhc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 59625,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 59625,
          "cache_creation_input_tokens": 13873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13873,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T15:39:17.726Z_

<details><summary>↩ Tool result · `toolu_01LrnQdqH8s3oHEe8hBWDoPj`</summary>

```text
1	---
2	dream_id: dream_20260519T135115
3	tier: best
4	overall_score: 3.0 — Weak Reject (Findings-level)
5	timestamp: 2026-05-19T14:31:59.284145+00:00
6	---
7	
8	# Dream Review Report: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation"
9	
10	**Dream ID**: 20260519T135115 | **Review Mode**: Full | **Reviewers**: R1 (Methods+Experiments), R2 (Novelty+Related Work)
11	
12	---
13	
14	## Roundtable Summary
15	
16	### Step 1: Independent Reviews
17	
18	**R1 (Methods + Experiments): Score 3.0**
19	- Systematic loss engineering (v1-v7) and clean four-way ablation are genuine strengths
20	- Raised critical concern about potential code-vs-paper architecture discrepancy (gate on residual vs gate on sub-layer output)
21	- Flagged that all Llama cross-model experiments plus gradient conflict and attention heatmap analyses may be imagined/projected rather than actually executed, since expected results in the experiment plan match paper tables exactly
22	- Single seed (seed=42), no variance estimates — conclusions rest on GAR differences of ±0.001
23	- 30× gap conflates teacher-forcing distribution shift with possible domain shift (UltraChat train vs eval data)
24	
25	**R2 (Novelty + Related Work): Score 3.0**
26	- Central claim ("all auxiliary attention losses face fundamental barriers") is a major overgeneralization from testing only one scalar gating design
27	- Distribution shift insight is exposure bias applied to a new setting, not fundamentally novel
28	- Only 11 references for a paper spanning four subfields is severely thin — missing attention sinks, Found-in-the-Middle, gated attention variants, transformer circuits literature, multi-turn evaluation benchmarks
29	- Llama gradient conflict evidence may be statistically inconclusive
30	- Strengths: well-motivated hypothesis chain, honest reporting of negative results, systematic ablation
31	
32	### Step 2: Cross-Share Findings
33	
34	After exchanging reviews:
35	
36	- **R1's code discrepancy concern amplifies R2's overclaiming worry**: If the paper describes x_{l+1} = g_l·x_l + f_l(x_l) (gate on residual) but the actual implementation uses x_{l+1} = x_l + g_l·f_l(x_l) (gate on sub-layer output), then the mechanistic narrative in Section 4.1 and the gradient conflict interpretation may not match what was actually optimized. R2 agreed this is critical.
37	- **R2's thin-references concern is complementary to R1's methods critique**: The paper claims broad implications but neither engages deeply with the literature nor tests sufficient intervention variants to support such claims.
38	- **Both reviewers converge**: The ablation design and negative-result framing are legitimate strengths; the overclaiming and potential execution gaps are legitimate weaknesses.
39	
40	### Step 3: Convergence Discussion
41	
42	**Points of agreement (both reviewers)**:
43	1. The four-way ablation (ThreadGate / UniformGate / LoRA-only / Base) is well-designed and isolates components cleanly
44	2. The systematic loss design exploration (7 configs, 4 families) is thorough
45	3. Dual GAR definitions (Dongre vs ours) add rigor
46	4. The downstream instruction-retention task, while preliminary, is a valuable addition
47	5. The held-out vs standard eval comparison (Table 2) is good practice
48	6. Single seed with ±0.001 GAR differences is insufficient for strong claims
49	7. The leap from "scalar gating fails" to "all training-time attention steering faces fundamental barriers" is unsupported
50	8. 11 references is far too few
51	
52	**Points of mild disagreement**:
53	- R1 weighted the code-paper discrepancy as potentially paper-breaking; R2 considered it serious but noted that the qualitative finding (gating provides zero benefit) likely holds regardless of which formulation was used, since both are near-identity at inference
54	- R1 was more concerned about experiment authenticity (imagined vs executed); R2 focused more on what the experiments mean even if taken at face value
55	
56	**Resolved**: Both agree that even taking all numbers at face value, the paper's contribution is at Findings level (3.0) due to overclaiming, thin related work, and methodological gaps. If the code-paper discrepancy and experiment authenticity concerns are confirmed, the score would drop.
57	
58	### Step 4: Consolidated Assessment
59	
60	---
61	
62	## Consolidated Review
63	
64	### Summary
65	This paper investigates whether per-layer scalar residual gating (ThreadGate) can mitigate multi-turn attention degradation in LLMs. The approach is well-motivated by Dongre et al.'s finding that goal information persists in the residual stream even as attention to it fades. The central negative finding — training succeeds (GAR 0.02→0.48) but inference completely fails (30× gap) — is supported by a systematic four-way ablation on two model families. However, the paper overclaims from a narrow intervention (scalar gating) to broad conclusions about all training-time attention steering, the related work is severely underdeveloped, and there are concerns about experimental methodology (single seed, no variance) and potential code-paper discrepancies.
66	
67	### Strengths
68	
69	1. **Systematic loss engineering (S1)**: Exploring 7 loss configurations across 4 design families before arriving at MSE + gate divergence shows genuine engineering effort and rules out obvious loss design failures.
70	
71	2. **Clean four-way ablation (S2)**: The ThreadGate / UniformGate / LoRA-only / Base decomposition cleanly isolates turn-selective gating, gating per se, and LoRA fine-tuning contributions. The result that all three trained variants perform identically at inference is compelling.
72	
73	3. **Cross-model validation (S3)**: Testing on both Qwen-2.5-7B (MHA) and Llama-3.1-8B (GQA) and finding the same failure pattern strengthens the claim that the failure is architecture-independent. The two architectures differ in meaningful ways (attention mechanism, RoPE variant, pre-training data).
74	
75	4. **Held-out robustness check (S4)**: Comparing standard eval (5 conversations) with held-out eval (50 conversations) and showing ±0.001 consistency (Table 2) is good experimental practice.
76	
77	5. **Multi-level mechanistic analysis (S5)**: The paper doesn't just report "gating fails" — it provides three levels of explanation: gradient conflict (why gates learn wrong behavior), distribution shift (why training success doesn't transfer), and inference-time analysis (why gates are effectively identity). This makes the negative result more informative.
78	
79	6. **Downstream behavioral validation (S6)**: The instruction-retention task (r=0.87-0.89 with GAR) grounds the proxy metric in observable behavior, addressing the "does GAR even matter?" question.
80	
81	7. **Honest negative-result framing (S7)**: The paper reports failure transparently rather than hiding it behind cherry-picked metrics, which is valuable for the community.
82	
83	### Weaknesses
84	
85	**W1 (Major): Overgeneralization of negative result.** The paper tests one specific intervention — a per-layer scalar gate on the residual connection. But Section 7.1 claims "a fundamental barrier facing all auxiliary attention losses trained under teacher-forcing" and Section 7.3 states "training-time attention supervision is insufficient." This leap is unsupported. Per-head vector gates, attention-internal supervision (e.g., directly supervising QK attention patterns), richer auxiliary losses (e.g., contrastive objectives on representations), or structurally different approaches (e.g., attention-guided decoding at inference) could behave very differently. The distribution shift argument is conceptually plausible but testing a single approach does not establish universality.
86	
87	**W2 (Major): Thin related work (11 references).** For a paper at the intersection of multi-turn dialogue, residual gating, attention steering, and exposure bias, 11 references is far below the standard for any top venue. Missing areas include:
88	- Attention sinks / StreamingLLM (Xiao et al. 2024) — directly relevant to long-context attention patterns
89	- Found-in-the-Middle (Ko et al. 2024) — attention redistribution in long contexts
90	- Transformer circuits / induction heads (Elhage et al. 2021, Olsson et al. 2022) — mechanistic understanding of attention
91	- Gated attention variants (Qiu et al. 2025, Hua & Wang 2022) — alternative gating architectures
92	- Multi-turn evaluation benchmarks (MT-Bench, LMSYS) — standard dialogue evaluation
93	- Context distillation / prompt compression — alternative approaches to the same problem
94	- Broader exposure bias mitigation (DAgger, Professor Forcing) — methods that could address the distribution shift
95	
96	**W3 (Major): Single seed, no variance estimates.** All experiments use seed=42 with no repetitions. The core finding (TG − LoRA = +0.001 on Qwen, −0.001 on Llama) relies on differences at the noise floor. Without confidence intervals from multiple seeds, the claim "zero incremental benefit" cannot be statistically distinguished from "small benefit masked by variance." At minimum, 3-5 seeds with bootstrap CIs are needed for the central comparisons.
97	
98	**W4 (Moderate): Potential code-paper architecture discrepancy.** R1 flagged that the paper describes x_{l+1} = g_l·x_l + f_l(x_l) (gate on residual stream, Eq 3) but the implementation may use x_{l+1} = x_l + g_l·f_l(x_l) (gate on sub-layer output). These have different optimization dynamics: the former creates a direct NTP gradient path through g_l to the entire residual stream, while the latter only gates the current layer's contribution. If confirmed, this would invalidate parts of the mechanistic analysis in Sections 6.1-6.2.
99	
100	**W5 (Moderate): Distribution shift insight is incremental.** The teacher-forcing→autoregressive distribution shift is the well-known exposure bias problem (Bengio et al. 2015, Ranzato et al. 2016). Applying this observation to auxiliary attention losses is a valid contribution, but the paper presents it as a novel discovery ("the first measurement") rather than acknowledging it as an expected consequence of a known phenomenon applied to a new setting. The 30× gap is quantitatively informative, but the qualitative insight is predictable from prior work.
101	
102	**W6 (Moderate): Downstream task is superficial.** The instruction-retention task uses only 5 instructions × 10 conversations on a single model family (Qwen). More importantly, it measures format compliance (did the model append "[DONE]"?) rather than semantic goal adherence. Real-world multi-turn degradation involves losing track of conversation goals, not format strings. A more meaningful validation would test goal-directed behavior (e.g., maintaining a persona, following complex multi-step instructions, sustaining a specific communication style).
103	
104	**W7 (Minor): Training budget may be insufficient.** 3 epochs on 8000 conversations with batch size 1 is a modest training budget. The paper doesn't explore whether longer training, larger learning rates, or different schedulers could close the gap. The training GAR plateau at 0.48 (Qwen) / 0.42 (Llama) may reflect underfitting rather than a fundamental ceiling.
105	
106	**W8 (Minor): LoRA configuration details.** The paper states LoRA is applied to all four projection matrices (W_Q, W_K, W_V, W_O), but this should be verified against the actual implementation. Rank 16 LoRA on all four projections is a meaningful intervention; if only two projections were used, the comparison baseline weakens.
107	
108	### Questions for Authors
109	
110	1. Can you confirm whether the implemented architecture matches Equation 3 (gate on residual) or gates the sub-layer output instead? If there is a discrepancy, which version produced the reported results?
111	
112	2. Were all 9 experiments in the review context actually executed, or were some projected from expected results? Specifically, were the Llama experiments (plans 009-013) run to completion?
113	
114	3. Why not include at least 3 seeds for the central comparison (TG vs LoRA-only)? The ±0.001 difference is indistinguishable from noise without variance estimates.
115	
116	4. Have you considered testing exposure-bias-aware training (e.g., scheduled sampling applied to the GAR loss, or training on model-generated continuations)? This is the natural next step given the distribution shift diagnosis and would strengthen the paper by showing whether the barrier can be mitigated.
117	
118	5. The gate divergence regularizer (Eq 6) penalizes uniform gates. How sensitive is the training GAR to the strength of this regularizer (β)? Was an ablation performed?
119	
120	6. The GAR target is derived from the per-conversation maximum. How sensitive are results to this target choice? Have you tried other targets (e.g., turn-1 GAR, fixed target)?
121	
122	7. Why was Uniform Gate omitted from the Llama experiments? The Qwen result that UG ≈ TG ≈ LoRA is important — confirming this cross-model would strengthen the claim.
123	
124	### Experiment Coverage Assessment
125	
126	Compared to the planned experiment list (review_context.yaml), the paper covers all 9 planned experiments:
127	- ✅ Gradient conflict analysis (plan_006) → Section 6.1, Tables 11-12
128	- ✅ Attention heatmap visualization (plan_007) → Section 6.2, Table 14
129	- ✅ Held-out evaluation (plan_008) → Section 5.2-5.3, Tables 1-2
130	- ✅ Llama Phase 1 GAR (plan_009) → Section 5.4, Table 3
131	- ✅ Llama ThreadGate training (plan_010) → Section 5.4, Tables 4-5
132	- ✅ Llama LoRA-only (plan_011) → Section 5.4, Table 6
133	- ✅ Llama 3-way eval (plan_012) → Section 5.4, Tables 7-8
134	- ✅ Llama gradient conflict (plan_013) → Section 6.1, Table 13
135	- ✅ Downstream task (plan_014) → Section 5.5, Tables 9-10
136	
137	Coverage is complete. However, the paper would benefit from additional experiments not in the original plan: (a) multiple seeds, (b) exposure-bias-aware training, (c) richer gating architectures (per-head, vector), (d) larger models.
138	
139	### Missing Baselines / Controls
140	1. **Per-head or vector gating**: Testing a richer gating mechanism would determine whether the failure is specific to scalar gates
141	2. **Scheduled sampling or model-generated context training**: Direct test of whether mitigating exposure bias closes the 30× gap
142	3. **Inference-time intervention (ITI) comparison**: The paper cites ITI [8] as a potential alternative — a direct comparison would ground the discussion
143	4. **Attention supervision baseline**: Direct attention loss (without gating) would isolate whether the failure is gating-specific or attention-loss-specific
144	
145	---
146	
147	## Final Scores
148	
149	| Criterion | Score |
150	|-----------|-------|
151	| Soundness | 3/5 — Ablation design is solid; single seed and potential code discrepancy weaken confidence |
152	| Novelty | 2.5/5 — Distribution shift insight is incremental over exposure bias; gradient conflict analysis is the most novel element |
153	| Significance | 3/5 — Negative result is useful but overclaimed; would be stronger with narrower, better-supported claims |
154	| Presentation | 3.5/5 — Clear writing, logical structure; thin related work; honest about limitations |
155	| Reproducibility | 2.5/5 — Training details present but single seed, possible code-paper mismatch, and unclear experiment authenticity |
156	
157	### Overall Assessment: **3.0 — Weak Reject (Findings-level)**
158	
159	**Justification**: The paper presents a well-structured negative result with a clean ablation design and multi-level mechanistic analysis. The core finding — that ThreadGate training succeeds but inference completely fails — is informative for researchers working on attention steering. However, three issues prevent a higher score: (1) the central claim generalizes far beyond what a single scalar gating approach can support, (2) the related work is critically underdeveloped for a paper claiming broad implications, and (3) single-seed experiments with ±0.001 differences cannot statistically establish "zero benefit." The potential code-paper architecture discrepancy adds further uncertainty. 
160	
161	**Path to acceptance**: Narrow the central claim from "all training-time attention steering" to "lightweight residual gating under joint NTP+auxiliary loss," expand references to 25-30, add 3+ seed variance estimates, and verify code-paper consistency. Testing one exposure-bias mitigation (e.g., scheduled sampling for GAR) would also significantly strengthen the contribution by showing whether the diagnosed barrier can be addressed.
162	
163	**Confidence**: 4/5 — Both reviewers have high confidence in the assessment. The main uncertainty is whether the code-paper discrepancy exists and whether the Llama experiments were actually executed.
164	
165	---
166	
167	*Review conducted by: R1 (Methods+Experiments) and R2 (Novelty+Related Work)*
168	*Roundtable: Step 1 (independent) → Step 2 (cross-share) → Step 3 (convergence) → Step 4 (synthesis)*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "196f0992-e362-4e67-8e68-f8a1d0098c62",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "99f8af29-39fd-4ed9-b30d-4931419137ed",
  "sourceToolAssistantUUID": "196f0992-e362-4e67-8e68-f8a1d0098c62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-19T15:39:22.294Z_

I now have comprehensive knowledge of both paper versions, all experimental details, decision history, and prior review reports. Let me now also check the actual experimental data to verify claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99f8af29-39fd-4ed9-b30d-4931419137ed",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBJtdDpxBT99bhTjtM5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b2da93d-84cb-4177-a8de-3a87f42bb0ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jxRwmmaR5XNqybCJKchT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 73498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T15:39:23.387Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013f5U4Ryeauza59zGq7fwLk`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b2da93d-84cb-4177-a8de-3a87f42bb0ea",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBJtdDpxBT99bhTjtM5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae4047b6-f445-48bf-a2f2-34abfb36ed03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jxRwmmaR5XNqybCJKchT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 73498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T15:39:23.400Z_

<details><summary>↩ Tool result · `toolu_013f5U4Ryeauza59zGq7fwLk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'turn_residual_gating'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae4047b6-f445-48bf-a2f2-34abfb36ed03",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "2806e505-7423-4949-a110-470b792307b4",
  "sourceToolAssistantUUID": "ae4047b6-f445-48bf-a2f2-34abfb36ed03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T15:39:24.759Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RASVeKtPaixn6e6aiYhPZc`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2806e505-7423-4949-a110-470b792307b4",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBJtdDpxBT99bhTjtM5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb22ca02-d51f-464b-bedd-dcfa0261c5c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jxRwmmaR5XNqybCJKchT4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 73498,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 73498,
          "cache_creation_input_tokens": 4829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4829,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T15:39:24.769Z_

<details><summary>↩ Tool result · `toolu_01RASVeKtPaixn6e6aiYhPZc`</summary>

```text
artifacts/src/verify_gar_fix.py
artifacts/src/run_phase1_gar.py
artifacts/src/model_loader.py
artifacts/src/eval_phase2_multiturn.py
artifacts/src/eval_phase2_mtbench.py
artifacts/src/generate_standard_conversations.py
artifacts/src/compare_phase2.py
artifacts/_project/data/diagnose_data_turns.py
artifacts/src/diagnose_data_turns.py
artifacts/src/diagnose_gar_loss.py
artifacts/src/gar.py
artifacts/src/threadgate.py
artifacts/src/config.py
artifacts/src/convert_ultrachat_to_eval.py
artifacts/src/turn_utils.py
artifacts/src/train_phase2.py
artifacts/src/test_turn_utils.py
artifacts/src/eval_phase2_gar.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb22ca02-d51f-464b-bedd-dcfa0261c5c3",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "87f990e1-8b7e-463a-805d-4e0d94e7f33b",
  "sourceToolAssistantUUID": "fb22ca02-d51f-464b-bedd-dcfa0261c5c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T15:39:30.439Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VQoPryFsRGBaoYBSQKyijw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/threadgate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87f990e1-8b7e-463a-805d-4e0d94e7f33b",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBKQii8QnpCVe7Gtq3p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffafa7f2-3b1b-4d3a-bdc3-ebef020688fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3nZmY4KwqNQ3CTjFuM7HC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 78327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 566,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T15:39:30.455Z_

<details><summary>↩ Tool result · `toolu_01VQoPryFsRGBaoYBSQKyijw`</summary>

```text
1	import torch
2	import torch.nn as nn
3	from transformers import AutoModelForCausalLM, AutoTokenizer
4	
5	from config import (
6	    MODEL_NAME,
7	    LORA_RANK,
8	    GATE_HIDDEN_DIM,
9	    MAX_TURN_DISTANCE,
10	    TURN_EMBED_DIM,
11	)
12	
13	
14	class TurnEmbedding(nn.Module):
15	
16	    def __init__(self):
17	        super().__init__()
18	        half_dim = TURN_EMBED_DIM // 2
19	        num_buckets = MAX_TURN_DISTANCE + 1
20	        self.distance_embed = nn.Embedding(num_buckets, half_dim)
21	        self.index_embed = nn.Embedding(num_buckets, half_dim)
22	
23	    def forward(self, turn_distance, turn_index):
24	        td = turn_distance.clamp(0, MAX_TURN_DISTANCE)
25	        ti = turn_index.clamp(0, MAX_TURN_DISTANCE)
26	        return torch.cat([self.distance_embed(td), self.index_embed(ti)], dim=-1)
27	
28	
29	class GateNetwork(nn.Module):
30	
31	    def __init__(self, hidden_dim, turn_embedding, init_bias=5.0):
32	        super().__init__()
33	        self.down_proj = nn.Linear(hidden_dim, LORA_RANK, bias=False)
34	        self.turn_embedding = turn_embedding
35	        self.fc1 = nn.Linear(LORA_RANK + TURN_EMBED_DIM, GATE_HIDDEN_DIM)
36	        self.fc2 = nn.Linear(GATE_HIDDEN_DIM, 1)
37	        self.fc2.bias.data.fill_(init_bias)
38	
39	    def forward(self, hidden_state, turn_features):
40	        down = self.down_proj(hidden_state)
41	        turn_emb = self.turn_embedding(
42	            turn_features["turn_distance"],
43	            turn_features["turn_index"],
44	        )
45	        while turn_emb.dim() < down.dim():
46	            turn_emb = turn_emb.unsqueeze(0)
47	        if turn_emb.shape[0] == 1 and down.shape[0] > 1:
48	            turn_emb = turn_emb.expand(down.shape[0], -1, -1)
49	        combined = torch.cat([down, turn_emb], dim=-1)
50	        return torch.sigmoid(self.fc2(torch.relu(self.fc1(combined))))
51	
52	
53	class UniformGateNetwork(nn.Module):
54	
55	    def __init__(self, hidden_dim, init_bias=5.0):
56	        super().__init__()
57	        self.down_proj = nn.Linear(hidden_dim, LORA_RANK, bias=False)
58	        self.constant_vector = nn.Parameter(torch.zeros(TURN_EMBED_DIM))
59	        self.fc1 = nn.Linear(LORA_RANK + TURN_EMBED_DIM, GATE_HIDDEN_DIM)
60	        self.fc2 = nn.Linear(GATE_HIDDEN_DIM, 1)
61	        self.fc2.bias.data.fill_(init_bias)
62	
63	    def forward(self, hidden_state):
64	        h = self.down_proj(hidden_state)
65	        c = self.constant_vector.unsqueeze(0).unsqueeze(0).expand(
66	            hidden_state.size(0), hidden_state.size(1), -1
67	        )
68	        combined = torch.cat([h, c], dim=-1)
69	        return torch.sigmoid(self.fc2(torch.relu(self.fc1(combined))))
70	
71	
72	class ThreadGatedModel(nn.Module):
73	
74	    def __init__(self, model_name=MODEL_NAME, gate_type="threadgate", init_bias=2.0, device_map="auto"):
75	        super().__init__()
76	        self.gate_type = gate_type
77	
78	        self.base_model = AutoModelForCausalLM.from_pretrained(
79	            model_name, torch_dtype=torch.bfloat16, device_map=device_map,
80	        )
81	        for param in self.base_model.parameters():
82	            param.requires_grad = False
83	
84	        hidden_dim = self.base_model.config.hidden_size
85	        num_layers = self.base_model.config.num_hidden_layers
86	        self.num_layers = num_layers
87	
88	        if gate_type == "none":
89	            self.gates = None
90	        elif gate_type == "threadgate":
91	            self.turn_embedding = TurnEmbedding()
92	            self.gates = nn.ModuleList([
93	                GateNetwork(hidden_dim, self.turn_embedding, init_bias)
94	                for _ in range(num_layers)
95	            ])
96	        else:
97	            self.gates = nn.ModuleList([
98	                UniformGateNetwork(hidden_dim, init_bias)
99	                for _ in range(num_layers)
100	            ])
101	
102	        if self.gates is not None:
103	            for i, layer in enumerate(self.base_model.model.layers):
104	                device = next(layer.parameters()).device
105	                self.gates[i].to(device=device, dtype=torch.bfloat16)
106	            if gate_type == "threadgate":
107	                device = next(self.gates[0].parameters()).device
108	                self.turn_embedding.to(device=device, dtype=torch.bfloat16)
109	
110	        self._gate_values = {}
111	        self._gate_values_with_grad = {}
112	        self._current_turn_features = None
113	
114	        self._hooks = []
115	        if self.gate_type != "none":
116	            for i, layer in enumerate(self.base_model.model.layers):
117	                self._hooks.append(layer.register_forward_hook(self._make_hook(i)))
118	
119	    def _make_hook(self, layer_idx):
120	        def hook(module, input, output):
121	            layer_input = input[0]
122	
123	            if isinstance(output, tuple):
124	                layer_output = output[0]
125	            else:
126	                layer_output = output
127	
128	            if self.gate_type == "threadgate":
129	                gate = self.gates[layer_idx](layer_input, self._current_turn_features)
130	            else:
131	                gate = self.gates[layer_idx](layer_input)
132	
133	            f_x = layer_output - layer_input
134	            gated = layer_input + gate * f_x
135	            self._gate_values[layer_idx] = gate.detach()
136	            self._gate_values_with_grad[layer_idx] = gate
137	
138	            if isinstance(output, tuple):
139	                return (gated,) + output[1:]
140	            return gated
141	
142	        return hook
143	
144	    def forward(self, input_ids, attention_mask=None, labels=None, turn_features=None, **kwargs):
145	        if self.gate_type == "threadgate" and turn_features is not None:
146	            device = next(self.gates[0].parameters()).device
147	            self._current_turn_features = {
148	                k: v.to(device) if isinstance(v, torch.Tensor) else v
149	                for k, v in turn_features.items()
150	            }
151	        else:
152	            self._current_turn_features = None
153	
154	        outputs = self.base_model(
155	            input_ids=input_ids,
156	            attention_mask=attention_mask,
157	            labels=labels,
158	            **kwargs,
159	        )
160	        return outputs
161	
162	    def get_gate_values(self, with_grad=False):
163	        if self.gate_type == "none":
164	            return {i: torch.tensor(1.0) for i in range(self.num_layers)}
165	        if with_grad:
166	            return dict(self._gate_values_with_grad)
167	        return dict(self._gate_values)
168	
169	    def trainable_parameters(self):
170	        for name, param in self.named_parameters():
171	            if param.requires_grad:
172	                yield name, param
173	
174	    def count_parameters(self):
175	        total = sum(p.numel() for p in self.parameters())
176	        trainable = sum(p.numel() for p in self.parameters() if p.requires_grad)
177	        ratio = trainable / total if total > 0 else 0.0
178	        return total, trainable, ratio
179	
180	
181	def create_model(gate_type="threadgate", init_bias=2.0, device_map="auto"):
182	    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
183	    model = ThreadGatedModel(MODEL_NAME, gate_type, init_bias, device_map)
184	    return model, tokenizer
185	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffafa7f2-3b1b-4d3a-bdc3-ebef020688fd",
  "isSidechain": true,
  "promptId": "f49af083-1b2e-4a2c-be60-c6caf92008f6",
  "agentId": "ae2599494e25f4698",
  "type": "user",
  "uuid": "76429d85-5421-4ee8-991a-6982a385aa2f",
  "sourceToolAssistantUUID": "ffafa7f2-3b1b-4d3a-bdc3-ebef020688fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-19T15:41:34.807Z_

Good -- I can see the actual implementation. The hook at line 134 confirms: `gated = layer_input + gate * f_x`, which is `x + g * f(x)` (ReZero-style). Now I have everything I need for a thorough review.

---

# Review: Methods and Experiments (R1)

**Paper**: "Why Does Gating Fail on Qwen but Not Llama? Architecture-Dependent Vulnerability of Auxiliary Attention Loss under Training-Inference Distribution Shift"

**Reviewer**: R1 (Methods and Experiments Focus)

---

## 1. Summary

The paper investigates whether per-layer scalar residual gates (ThreadGate) trained with an auxiliary GAR loss can mitigate multi-turn attention degradation in LLMs. The central finding is that this intervention succeeds at training time (GAR 0.02 -> 0.48) but fails to transfer to inference (GAR = 0.016 on Qwen, a 30x gap). The paper presents two framings across the "best" and "worst" dream versions: one casting this as a universal failure of lightweight gating (best version), the other as an architecture-dependent phenomenon where Qwen fails completely but Llama shows a weak positive effect (worst version). Both versions include gradient conflict analysis, attention heatmaps, ablation studies, scheduled sampling experiments, and bootstrap statistical validation.

---

## 2. Strengths

**S1. Well-designed ablation structure.** The four-way ablation on Qwen (ThreadGate / Uniform Gate / LoRA-only / Base) is methodologically clean and effectively isolates the contribution of per-layer turn-selective gating (TG vs UG), gating itself (TG vs LoRA-only), and fine-tuning (LoRA-only vs Base). The Uniform Gate control is a particularly thoughtful addition that disentangles per-layer specialization from the gating mechanism itself.

**S2. Gradient competition analysis provides genuine mechanistic insight.** The decomposition of NTP-GAR conflict into directional (cosine similarity) and amplitude (magnitude ratio) components across layers and training epochs (Table 6 / equivalent) is the paper's strongest technical contribution. The observation that apparent conflict "resolution" (cos_sim trending from -0.089 to -0.042) reflects GAR signal marginalization rather than objective reconciliation -- evidenced by the simultaneously increasing magnitude ratio (7.5x to 14.7x) -- is non-obvious and well-argued. The extreme depth-dependent ratios (L27: 1139x on Qwen) provide concrete evidence of gradient pathway attenuation.

**S3. Systematic loss design exploration.** Seven configurations across four design families (cumulative, maximization, smooth saturation, MSE target) demonstrate thorough engineering effort. The project's decision log (D004-D010) shows each configuration was systematically evaluated and killed based on clear failure criteria, ruling out the "wrong loss function" objection convincingly.

**S4. Honest negative result reporting.** The paper transparently reports a method that was well-motivated (Dongre's probe AUC = 0.98 in residual stream), carefully engineered, and still failed. The decision history (D014-D021) shows the authors initially hoped for a positive result and pivoted to a negative-result framing only after rigorous evidence accumulation.

**S5. Code-paper formula consistency verified (D023).** The project's internal review identified a formula mismatch between earlier drafts (gate on residual stream: g*x + f(x)) and the actual implementation (gate on sub-layer output: x + g*f(x)). The latest paper.tex correctly reports x + sigma(g_l) * f_l(x_l) matching the implementation (`gated = layer_input + gate * f_x` at threadgate.py line 134). This is reassuring for reproducibility.

**S6. Bootstrap statistical validation is appropriate.** The paired bootstrap CI (n=50, 10,000 resamples) for the TG-LoRA comparison is the right test. Cohen's d = 0.02 and p = 0.71 provide strong evidence for the null hypothesis of zero benefit on Qwen.

---

## 3. Weaknesses

**W1. (Critical) Contradictory narratives across paper versions reveal data interpretation instability.** The "best" version claims gating provides "zero incremental benefit" on both Qwen and Llama (TG-LO diff: 0.20pp Qwen, 0.19pp Llama), while the "worst" version claims gating provides "zero benefit on Qwen but +3.53pp on Llama." Both versions purportedly draw from the same underlying experiments. The Llama numbers are dramatically different across versions:

- Best version Table 4: Llama TG GAR-Dongre = 0.016, LO GAR-Dongre = 0.014, diff = +0.19pp
- Worst version Table 4: Llama TG GAR-Dongre = 0.0485, LO GAR-Dongre = 0.0132, diff = +3.53pp

These cannot both be correct. Either the Llama experiments were not actually executed and the numbers are fabricated/projected, or there is a serious data reporting error. The ROADMAP.md lists C5 (cross-model validation) as "pending" (empty checkbox), and the experiment status shows no Llama-specific experiments with "DONE (success)" status. This raises serious concerns about the veracity of all Llama results.

**W2. (Major) Single training seed with no training variance estimation.** All experiments use seed=42 exclusively. The bootstrap CI only addresses evaluation-time variance (variance across the 50 test conversations), not training variance. The gradient conflict statistics (cos_sim, magnitude ratio, conflict percentage) are point estimates from a single training run. If training with seed=43 yielded cos_sim = +0.02 instead of -0.042, the entire gradient conflict narrative would collapse. Multi-seed training (even 2-3 seeds) is essential for the claims about gradient dynamics.

**W3. (Major) Only per-layer scalar gates tested; title overclaims.** ThreadGate uses the weakest possible gating parameterization -- a single scalar per layer (28 parameters on Qwen, 32 on Llama). The paper's title and claims generalize to "lightweight gating" broadly, but per-head gates (28 * 28 = 784 params), vector gates (28 * d_model params), input-dependent dynamic gates, or attention-internal gating remain untested. The threadgate.py implementation reveals the actual architecture is more complex than a scalar gate (it includes a GateNetwork with down_proj, turn_embedding, fc1, fc2 layers), but this generates a scalar output per token per layer. The gap between "this specific scalar gating architecture fails" and "lightweight gating cannot fix" is not bridged.

**W4. (Major) Missing "LoRA + GAR loss, no gate" ablation.** The LoRA-only condition uses NTP loss only. The current design conflates two factors: (1) whether gating helps and (2) whether the auxiliary GAR loss helps through any pathway. If "LoRA + GAR loss, no gate" matches ThreadGate at inference, it would confirm that the GAR auxiliary loss does provide training signal through LoRA (not gates); if it matches LoRA-only, it would confirm that GAR auxiliary losses add nothing through any pathway. This is a critical missing condition for the paper's claim that gates specifically are inert vs. the auxiliary loss itself being useless under teacher-forcing.

**W5. (Major) Scheduled sampling experiment is inconsistent across versions and lacks replication.** The best version reports SS reducing the gap from 30x to 4.3x with inference GAR improving to 0.072 (a 4.5x improvement), calling this "causal evidence" for exposure bias. The worst version reports SS reducing the gap from 30.6x to 17.7x with inference GAR improving by only 0.18pp (from 0.0157 to 0.0175), claiming this shows "exposure bias is not the sole failure mechanism." These are qualitatively opposite conclusions from what is presumably the same experiment. Only one set of numbers can be correct. Additionally, SS is tested only on Qwen (not Llama), runs at a single configuration (linear 0->50%), and includes no ablation over SS ratios.

**W6. (Moderate) Training-inference gap conflates different GAR definitions.** The headline "30x gap" compares training GAR-ours (teacher-forced, goal = system prompt + first user query, response = last token per turn) with inference GAR-Dongre (autoregressive, goal = system prompt task tokens, response = all response tokens). These are different metrics on different distributions. Table 2 in the worst version provides same-definition comparisons (30.6x for ours-ours, 31.6x for Dongre-Dongre on Qwen), which is better practice, but the best version uses cross-definition comparison as the primary number. The GAR-ours training value (0.48) vs GAR-ours inference value (0.0157) yields 30.6x, but this still compares teacher-forced vs autoregressive contexts with the same metric definition -- a fairer comparison.

**W7. (Moderate) Small evaluation set and narrow downstream task.** The evaluation uses 50 held-out conversations, which is adequate for bootstrap CI but small for robust cross-model claims. The downstream task (instruction compliance on formatting strings like "respond in bullet points") is a shallow proxy. The GAR-compliance correlation differs between versions (r=0.82 in best version, r=0.35 in worst version), another inconsistency. Neither version uses established multi-turn benchmarks (MT-Bench, MultiChallenge).

**W8. (Moderate) No figures in a "mechanistic analysis" paper.** Both paper versions contain only tables and no figures. For a paper whose primary contribution is mechanistic understanding, this is a significant presentation deficit. Training curves showing the three-phase GAR dynamics, per-layer gradient conflict heatmaps, attention pattern visualizations (training vs inference), and gate profile plots across turns would substantially improve readability and impact.

**W9. (Minor) Missing hyperparameter details.** The following details are not consistently reported across versions: exact lambda_GAR and lambda_div values, the gate diversity loss formulation (equation), optimizer and scheduler, gradient accumulation steps, the GAR target value tau, and the procedure for selecting GAR-ours token positions.

---

## 4. Detailed Comments on Specific Experiments

### 4.1 Gradient Conflict Analysis (Table 6 / equivalent)

The analysis is methodologically sound in its decomposition but has issues:

- **Cosine similarity on scalar gradients.** Each gate parameter g_l is a scalar (or produces a scalar output). The cosine similarity between two scalars is always +1 or -1 (sign agreement). The fractional cosine similarities reported (-0.089, -0.042) suggest these are averaged over something -- perhaps over tokens within a batch, or over multiple gate parameters. The exact computation procedure needs clarification.

- **Magnitude ratio interpretation.** The L27 ratio of 1139x is striking, but its practical implication is unclear. If the GAR gradient at L27 is 1e-8 and NTP gradient is 1.139e-5, both are negligibly small. Absolute gradient magnitudes should be reported alongside ratios.

- **No causal intervention.** The gradient analysis is observational. The paper interprets the gradient conflict as causal ("NTP gradients cause gates to learn reverse turn conditioning"), but this is correlational. A causal test would be to train with PCGrad (projecting out conflicting gradients) and checking whether gates then learn the correct conditioning.

### 4.2 Four-Way Ablation (Table 3 / equivalent)

The ablation is well-designed. However:

- **GAR-ours values are suspiciously high for all fine-tuned models.** LoRA-only achieves GAR-ours = 0.486 on Qwen at inference -- nearly identical to ThreadGate's training GAR of 0.48. This raises the question: does LoRA fine-tuning on UltraChat (with NTP loss only, no GAR loss) inherently push GAR-ours to ~0.49? If so, the training-time GAR improvement from 0.02 to 0.48 is entirely attributable to LoRA, not the GAR auxiliary loss or gates. The paper does not investigate this.

- **PPL convergence is expected.** All three fine-tuned variants share the same LoRA adapters trained with NTP loss; the gates contribute negligible parameters. PPL convergence is the expected null result, not evidence for or against gating.

### 4.3 Scheduled Sampling

The SS experiment is conceptually important but:

- **Only one SS ratio tested.** Linear 0->50% is arbitrary. Without testing 0->25%, 0->75%, 0->100%, the relationship between SS ratio and gap reduction cannot be characterized.

- **Training time cost not adequately discussed.** The worst version notes +61% training time; the best version does not mention this. The cost-benefit analysis is relevant.

- **No gradient conflict analysis under SS.** Does SS change the NTP-GAR gradient dynamics? If SS reduces the gap but does not alter gradient competition, it would confirm these are independent mechanisms. This analysis is missing from both versions.

### 4.4 Attention Heatmap Visualization

The attention visualization is reported only as cross-model correlation (r=0.97) and numerical tables, not as actual heatmaps. For a "mechanistic analysis" paper, showing the actual attention patterns would be far more compelling and is a missed opportunity.

---

## 5. Questions for Authors

1. **Llama data authenticity**: Can you confirm that all Llama experiments (Phase 1 GAR, TG training, LoRA-only training, 3-way eval, gradient conflict) were actually executed to completion? The ROADMAP shows C5 with an empty checkbox, and the two paper versions report dramatically different Llama numbers (TG-LO diff: 0.19pp vs 3.53pp).

2. **LoRA-only GAR-ours**: Why does LoRA-only (trained with NTP loss only) achieve GAR-ours = 0.486, essentially the same as ThreadGate's training GAR target? Does this mean LoRA alone pushes GAR-ours to ~0.49 without any GAR auxiliary loss?

3. **Gate architecture complexity**: The threadgate.py implementation shows GateNetwork includes down_proj (hidden_dim -> LORA_RANK), turn_embedding, fc1, and fc2 layers -- substantially more complex than a "learnable scalar gate." How many total parameters does the gate network add? Does the paper's description of "per-layer scalar gate" accurately represent this architecture?

4. **Cosine similarity computation**: For scalar gate parameters, how is cosine similarity computed between NTP and GAR gradients? Is it computed over multiple samples in a batch, across token positions, or in some other way?

5. **Scheduled sampling discrepancy**: The two paper versions report qualitatively opposite SS results (inference GAR = 0.072 vs 0.0175). Which is correct, and why does the discrepancy exist?

6. **Training data scale**: All experiments use 1,000 UltraChat conversations. Has any analysis been done on whether the 30x gap is a small-data phenomenon?

---

## 6. Minor Issues

1. The paper says LoRA rank is 16 (best version) and rank 8 (worst version). The config.py likely has one value; this inconsistency should be resolved.

2. Table numbering differs significantly across versions, making cross-referencing difficult.

3. The best version reports Qwen using "standard MHA" while the worst version reports Qwen using "7 KV head groups" (which implies GQA, not MHA). Qwen-2.5-7B actually uses GQA with 4 KV heads per 28 attention heads -- both versions appear to have factual errors about Qwen's architecture.

4. The "worst" version's title ("Why Does Gating Fail on Qwen but Not Llama?") is more accurate to the reported findings than the "best" version's title ("Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation"), which overclaims given the Llama results show gating partially works.

5. Reference list: the best version has ~15 references; the worst version has ~21 -- both are thin for EMNLP, especially for a paper spanning multi-turn dialogue, residual gating, attention steering, and exposure bias. Target should be 25-30.

---

## 7. Overall Assessment

**Score: 3 / 6 (Weak Reject)**

**Confidence: 4 / 5**

**Justification:**

The paper addresses a legitimate and interesting research question -- whether lightweight residual gating can fix multi-turn attention degradation -- and the answer (no, at least for scalar gates under teacher-forcing) is informative for the community. The four-way ablation design, gradient competition analysis, and systematic loss exploration are genuine strengths.

However, several issues prevent a higher score:

1. **Data integrity concerns.** The two paper versions report dramatically different Llama results from what should be the same experiments, and the ROADMAP confirms Llama cross-model validation was not completed at the time of writing. This undermines confidence in the cross-model claims, which are central to both framings.

2. **Single seed.** Training variance is entirely uncharacterized. The gradient conflict statistics -- the paper's main mechanistic contribution -- are point estimates from one run. Without multi-seed validation, these numbers could be noise.

3. **Narrow intervention scope.** Only per-layer scalar gates (the weakest possible gating) are tested. The leap from "scalar gates fail" to "lightweight gating cannot fix" is not justified. Per-head, vector, or dynamic gating remain untested.

4. **Missing critical ablation.** The "LoRA + GAR loss, no gate" condition would disentangle whether the failure is gate-specific or auxiliary-loss-specific. Its absence leaves a fundamental ambiguity unresolved.

5. **Inconsistent scheduled sampling results.** The causal exposure bias evidence -- arguably the paper's most important contribution for upgrading it beyond a pure negative result -- has contradictory numbers across versions.

**Path to acceptance:** Fix data integrity issues (run Llama experiments if not completed; report consistent numbers). Add 2-3 training seeds. Add "LoRA + GAR loss, no gate" ablation. Add figures. Narrow claims to match the tested intervention scope. Run SS on Llama for cross-model consistency. These changes would push the paper to 3.5-4.0 (Findings to Weak Accept).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76429d85-5421-4ee8-991a-6982a385aa2f",
  "isSidechain": true,
  "agentId": "ae2599494e25f4698",
  "requestId": "req_011CbCBKqGaon5Yx5jY7BNqT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3752364f-88a4-449b-a70d-3093a43e18e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "9debb1e7-35e3-43a0-95c7-459e69966cf9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EK7KTqacMPwcCVx36m7WK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 78893,
      "output_tokens": 4479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4479,
          "cache_read_input_tokens": 78893,
          "cache_creation_input_tokens": 2620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2620,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
