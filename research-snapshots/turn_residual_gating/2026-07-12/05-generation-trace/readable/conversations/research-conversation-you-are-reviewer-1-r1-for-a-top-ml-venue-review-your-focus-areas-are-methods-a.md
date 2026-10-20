# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **methods** and **experiments**. Review the foll

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a910e29cfb65eeab1.jsonl`
- **Structured JSON:** [`001ea038c3367d311287.json`](../../sessions/00/001ea038c3367d311287.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-19T15:28:16.263Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **methods** and **experiments**. 

Review the following paper: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"

## Paper Summary (from my reading)

This paper investigates whether lightweight residual gating (ThreadGate) can fix multi-turn attention degradation in LLMs. Key findings:

1. **GAR degradation confirmed** (C1): Qwen-2.5-7B shows 70.8% GAR drop over 10 turns; Llama-3.1-8B shows 69%.

2. **Training succeeds, inference fails** (C2): ThreadGate raises GAR from 0.02→0.48 during training, but at inference GAR=0.016 (30× gap on Qwen, 26× on Llama).

3. **Gating provides zero benefit** (C4): Four-way ablation (TG/UG/LoRA-only/Base) shows all fine-tuned variants converge to identical GAR and PPL. Bootstrap CI includes zero (p=0.71, Cohen's d=0.02).

4. **Cross-model validation** (C5): Llama-3.1-8B replicates the pattern. TG-LoRA diff is 0.19-0.20pp on both models.

5. **Gradient competition** (§6.1): NTP gradients dominate GAR gradients by 7.5-16.2× on gate parameters, with 63-79% of layers showing directional conflict.

6. **Exposure bias mitigation** (§6.4): Scheduled sampling reduces gap from 30× to 4.3× (7× reduction), providing causal evidence.

7. **Downstream correlation** (§6.5): Instruction compliance correlates with GAR at r=0.82.

## Architecture (§4.1)
- Per-layer scalar gate g_l, sigmoid-activated, ReZero-style: x_{l+1} = x_l + σ(g_l) · f_l(x_l)
- Combined with LoRA r=16 on attention projections
- Loss: L = L_NTP + λ_GAR · L_GAR + λ_div · L_div, where L_GAR = (GAR - τ)^2 with τ=0.5

## Training Setup (§4.3)
- Qwen-2.5-7B-Instruct and Llama-3.1-8B-Instruct
- 1,000-conversation subset of UltraChat, 3 epochs
- Single seed (42)

## Key Tables
- Table 1: GAR degradation by turn (both models)
- Table 2: Training-inference GAR gap (30× Qwen, 26× Llama)
- Table 3: Four-way ablation on Qwen (TG/UG/LO/Base all converge)
- Table 4: Cross-model convergence (TG-LO diff ~0.2pp)
- Table 5: Bootstrap CI (n=50, 10K resamples, CI includes zero)
- Table 6: Gradient conflict statistics (cos_sim, conflict%, mag ratio across epochs)
- Table 7: Scheduled sampling results (gap 30×→4.3×)
- Table 8: Instruction compliance (Appendix B)

## Experiment Design Context
The review_context.yaml lists these imagined experiments:
- Qwen v7 Gradient Conflict Analysis (3 checkpoints) — covered in §6.1 + Table 6 + Appendix C
- Attention Heatmap Visualization (4 models × 3 convs × 28 layers) — partially covered in §6.3 (mentioned but no figure shown in main text)
- Llama-3.1-8B Phase 1 GAR Degradation Diagnosis — covered in §5.1 + Table 1
- Llama-3.1-8B ThreadGate v7 Training — covered in §5.2 + Table 2
- Llama-3.1-8B LoRA-only Training — covered implicitly in §5.4
- Llama-3.1-8B 3-Way Eval — covered in §5.4 + Table 4
- Llama-3.1-8B Gradient Conflict Analysis — covered in §6.1 + Table 6
- Downstream Task Sanity Check — covered in §6.5 + Table 8 (Appendix B)
- Bootstrap CI for Zero Benefit — covered in §5.5 + Table 5
- Exposure-Bias Mitigation (Scheduled Sampling) — covered in §6.4 + Table 7

## Your Task

Evaluate the paper on these dimensions, writing 2-4 sentences per dimension:

1. **Methodological soundness**: Is ThreadGate well-designed? Is the ablation design appropriate? Any methodological flaws?
2. **Experimental rigor**: Are experiments sufficient to support claims? Are baselines adequate? Statistical validation?
3. **Reproducibility**: Are enough details provided? Any missing hyperparameters or setup details?
4. **Analysis depth**: Is the gradient competition analysis convincing? Is the exposure bias causal argument well-supported?
5. **Weaknesses in methods/experiments**: What's missing or could be stronger?

Then provide:
- **Strengths** (bullet list, 4-6 items)
- **Weaknesses** (bullet list, 4-6 items)
- **Questions for authors** (3-5 specific questions)
- **Overall assessment score** (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
- **Confidence** (1-5: 1=low, 5=expert)

Be critical but fair. This is a negative-result + mechanistic analysis paper, so evaluate the quality of the negative result and analysis rather than expecting a positive method contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "f01d3258-c0e0-4c1c-a07e-fd2b4749b312",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T15:28:16.267Z_

```json
{
  "parentUuid": "f01d3258-c0e0-4c1c-a07e-fd2b4749b312",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "0bd5ec63-cf78-4966-90b9-5047267365b0",
  "timestamp": "2026-05-19T15:28:16.267Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T15:28:22.031Z_



I'll review the paper by first reading the full manuscript and related project files to ground my assessment in the actual content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bd5ec63-cf78-4966-90b9-5047267365b0",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAU8Q5PH6Hukxr959RV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ddee0d8-64af-4c9a-84ec-24ed3f795677",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPU4NFmLxajFDgWs5acUJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15059,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15059,
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

_source line 4 · 2026-05-19T15:28:22.733Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WQ4Et9nSkLamhZ3thcJN4Z`</summary>

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
  "parentUuid": "2ddee0d8-64af-4c9a-84ec-24ed3f795677",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAU8Q5PH6Hukxr959RV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c94d22c-2342-4c06-b6e5-53e679124254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPU4NFmLxajFDgWs5acUJk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15059,
      "cache_read_input_tokens": 0,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 130,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15059,
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

_source line 5 · 2026-05-19T15:28:22.740Z_

<details><summary>↩ Tool result · `toolu_01WQ4Et9nSkLamhZ3thcJN4Z`</summary>

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
  "parentUuid": "0c94d22c-2342-4c06-b6e5-53e679124254",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "efdb025b-e1c6-45a8-ad4b-4e5af87d6f8a",
  "sourceToolAssistantUUID": "0c94d22c-2342-4c06-b6e5-53e679124254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T15:28:25.760Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01QMTSkDvfUjyxgJ6spiYY1M`</summary>

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
  "parentUuid": "efdb025b-e1c6-45a8-ad4b-4e5af87d6f8a",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAUcFPSJovG43LkxzUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17ac6190-d95d-402f-9d2c-b30c8c3e4aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTKfR64EBcUQmGsdWCmLKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 15059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 7 · 2026-05-19T15:28:25.834Z_

<details><summary>↩ Tool result · `toolu_01QMTSkDvfUjyxgJ6spiYY1M`</summary>

```text
{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (16 个)\n\n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: PREPARING — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v6**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase2_tg_s42**: DONE (negative) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- phase2_tg_s42_v8_schedsampling: Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。（准备中）\n\n## 近期结论\n- **analysis_attention_heatmap** (success): 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。 ← 基于 phase2_tg_s42_v7\n- **analysis_gradient_conflict** (success): NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。 ← 基于 phase2_tg_s42_v7\n- **phase2_4way_eval_heldout** (success): 四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。 ← 基于 phase2_4way_eval\n\n## 趋势\n成功 8 / 负向 5 / 失败 1 / 共 15\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-20861: 无 GPU 信息\n\n## 告警\n- phase2_tg_s42_v2: 已被终止 — unknown\n- phase2_tg_s42_v4: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17ac6190-d95d-402f-9d2c-b30c8c3e4aa0",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "a4f71b52-3211-4692-93bd-766d79b4d479",
  "sourceToolAssistantUUID": "17ac6190-d95d-402f-9d2c-b30c8c3e4aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T15:28:26.677Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01ERKvwG5KMoMkVSmWVGUbJV`</summary>

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
  "parentUuid": "a4f71b52-3211-4692-93bd-766d79b4d479",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAUcFPSJovG43LkxzUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0421ae88-e988-462e-8bd1-2930373431c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTKfR64EBcUQmGsdWCmLKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 15059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 9 · 2026-05-19T15:28:26.697Z_

<details><summary>↩ Tool result · `toolu_01ERKvwG5KMoMkVSmWVGUbJV`</summary>

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
  "parentUuid": "0421ae88-e988-462e-8bd1-2930373431c4",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "6f539f41-a632-4f8e-99dd-862929b7b391",
  "sourceToolAssistantUUID": "0421ae88-e988-462e-8bd1-2930373431c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T15:28:27.315Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RjzhtkxKLGsbTtsd8zWWqR`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f539f41-a632-4f8e-99dd-862929b7b391",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAUcFPSJovG43LkxzUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e03248b6-aa53-4b6c-b6ba-53c2004b716a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTKfR64EBcUQmGsdWCmLKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 15059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1453,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 11 · 2026-05-19T15:28:27.330Z_

<details><summary>↩ Tool result · `toolu_01RjzhtkxKLGsbTtsd8zWWqR`</summary>

```text
literature_map.yaml
mistakes.yaml
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260519T135115/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T135115/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T135115/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T135115/best/review_context.yaml
artifacts/dream_reports/dream_20260519T143220/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T143220/median/imagined_experiments.yaml
decisions.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260519T145320/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T145320/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T145320/worst/imagined_experiments.yaml
registry.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260519T145320/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e03248b6-aa53-4b6c-b6ba-53c2004b716a",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "eae1d904-dda2-4af2-9c36-b665aad9f15e",
  "sourceToolAssistantUUID": "e03248b6-aa53-4b6c-b6ba-53c2004b716a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T15:28:30.151Z_

Let me read the latest paper and supporting files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae1d904-dda2-4af2-9c36-b665aad9f15e",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAUxBwovJg7wq8RcpVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84938f5c-9790-487c-9470-e0d0e1a91977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULr9piBaNQbya5914NvZE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 16512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1875,
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

_source line 13 · 2026-05-19T15:28:31.228Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KGDc1qPBWU3LcKmrF8CTjg`</summary>

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
  "parentUuid": "84938f5c-9790-487c-9470-e0d0e1a91977",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAUxBwovJg7wq8RcpVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1520f2ab-f36e-4e2f-9ad6-c8f690559b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULr9piBaNQbya5914NvZE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 16512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1875,
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

_source line 14 · 2026-05-19T15:28:31.551Z_

<details open><summary>🔧 Tool call — Read · `toolu_014dEcNbv4i5Pk9cT2fS5qvZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1520f2ab-f36e-4e2f-9ad6-c8f690559b92",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAUxBwovJg7wq8RcpVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84b7531c-6e7b-4af7-975e-605b39e6849a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULr9piBaNQbya5914NvZE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 16512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1875,
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

_source line 15 · 2026-05-19T15:28:31.678Z_

<details><summary>↩ Tool result · `toolu_01KGDc1qPBWU3LcKmrF8CTjg`</summary>

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
  "parentUuid": "1520f2ab-f36e-4e2f-9ad6-c8f690559b92",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "0599d7e8-d8f2-4797-b825-a95169a7609f",
  "sourceToolAssistantUUID": "1520f2ab-f36e-4e2f-9ad6-c8f690559b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T15:28:31.563Z_

<details><summary>↩ Tool result · `toolu_014dEcNbv4i5Pk9cT2fS5qvZ`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立且增强。C1-C5 全部验证。Llama-3 跨模型数据将 ''30x gap 是 exposure
2	  bias 在 auxiliary attention loss 上的首个定量测量'' 从单模型观察升级为普遍现象。Mitigation 实验闭合因果环 （缓解
3	  exposure bias → gap 缩小 → 确认 exposure bias 是根因），论文从纯 negative result 升级为 ''diagnosis
4	  + partial cure''。投 EMNLP Main，reviewer 可能给 Borderline Accept (3.5-4.0)。
5	
6	  '
7	imagined_experiments:
8	- name: Qwen v7 Gradient Conflict Analysis (3 checkpoints)
9	  plan_id: plan_006
10	  description: '对 v7 训练的 3 个 epoch checkpoint 逐层计算 NTP 和 GAR loss 对 gate 参数的梯度， 得到
11	    cos_sim（方向冲突）和 mag_ratio（幅度压制），量化 NTP 如何系统性压制 GAR 信号。
12	
13	    '
14	  expected_results:
15	    epoch0_mean_cos_sim: -0.089
16	    epoch1_mean_cos_sim: -0.061
17	    epoch2_mean_cos_sim: -0.042
18	    epoch0_conflict_layer_pct: 0.79
19	    epoch1_conflict_layer_pct: 0.71
20	    epoch2_conflict_layer_pct: 0.67
21	    epoch0_mean_mag_ratio: 7.5
22	    epoch1_mean_mag_ratio: 10.8
23	    epoch2_mean_mag_ratio: 14.7
24	    epoch2_L27_mag_ratio: 1139
25	    epoch2_L26_mag_ratio: 287
26	    epoch2_L3_mag_ratio: 3.2
27	    epoch0_gar_grad_norm_mean: 0.0041
28	    epoch2_gar_grad_norm_mean: 0.00089
29	    epoch0_ntp_grad_norm_mean: 0.031
30	    epoch2_ntp_grad_norm_mean: 0.013
31	  result_rationale: 'v7 使用 MSE target loss（GAR 收敛到 0.48 后 loss→0），因此 GAR 梯度随训练递减是结构性的：
32	    target 达成后 loss landscape 变平，梯度自然衰减。但 NTP loss 始终活跃（final ~0.896）， 其梯度虽也下降但幅度远小于
33	    GAR。结果是 mag_ratio 从 7.5x 增长到 14.7x——不是因为 NTP 变强，而是 GAR 变弱。cos_sim 从 -0.089 趋向
34	    -0.042 表面上是"冲突缓解"，实质是 GAR 信号被边缘化后无力对抗。深层（L26-L27）mag_ratio 爆炸到 100-1000x，因为这些层
35	    NTP loss 的反向传播路径更短、梯度更强，而 GAR 信号经过多层衰减后几乎消失。这解释了 NF1 中 27/28 层 gate diff < 0 的反向
36	    turn conditioning：NTP 推 gate→1.0 的力量在深层 无人对抗，gate 在这些层完全服从 NTP。
37	
38	    '
39	  tables:
40	  - name: 'Table: Per-layer gradient conflict across training'
41	    description: '28 层 x 3 epoch 的 cos_sim 和 mag_ratio 热力图表。行=层，列=epoch。 深层呈现 mag_ratio
42	      指数增长，浅层相对温和（3-8x）。cos_sim 在大多数层为负值， 但绝对值随训练减小（GAR 信号消失而非调和）。
43	
44	      '
45	  - name: 'Table: Summary statistics by epoch'
46	    description: '汇总 mean/median/max cos_sim, mag_ratio, conflict_layer_pct。 关键数字：conflict_pct
47	      67-79%, mag_ratio 7.5→14.7x。
48	
49	      '
50	  figures_description:
51	  - 'Fig: 双轴折线图。左轴 cos_sim（3 条线=3 epoch across 28 layers），右轴 mag_ratio（同）。X 轴=层编号。展示深层
52	    mag_ratio 爆炸性增长 + cos_sim 在大多数层为负值。'
53	  - 'Fig: 训练过程中 GAR vs NTP 梯度 L2-norm 的衰减曲线。GAR norm 衰减 ~5x，NTP norm 衰减 ~2.4x，差距拉大。'
54	  analysis: '梯度冲突数据完整支撑 C3 和 SP2。三个关键 insight：(1) 方向冲突（cos_sim 负值）证实 NTP 和 GAR 在 gate
55	    参数空间确实竞争；(2) 幅度压制（mag_ratio 14.7x）证实 GAR 信号 不足以改变 gate 行为；(3) 冲突"缓解"的机制是 GAR 边缘化而非调和，这是
56	    paper 中 需要清晰传达的反直觉发现。与 NF1 的 gate profile 数据形成因果链： 梯度压制 → gate 服从 NTP → 反向 turn
57	    conditioning → 推理时干预不足。
58	
59	    '
60	- name: Attention Heatmap Visualization (4 models x 3 convs x 28 layers)
61	  plan_id: plan_007
62	  description: '对 Base/TG/UG/LoRA-only 四个模型，各取 3 段多轮对话，可视化 28 层的 attention 分布。 关注
63	    goal token（system prompt + first user query）在不同 turn 的 attention weight。
64	
65	    '
66	  expected_results:
67	    base_goal_attn_turn1: 0.042
68	    base_goal_attn_turn10: 0.008
69	    tg_goal_attn_turn1: 0.039
70	    tg_goal_attn_turn10: 0.009
71	    ug_goal_attn_turn1: 0.041
72	    ug_goal_attn_turn10: 0.008
73	    lora_goal_attn_turn1: 0.04
74	    lora_goal_attn_turn10: 0.009
75	    cross_model_attn_pattern_correlation: 0.97
76	    layer_specific_pattern: L3-L5 goal attn 最高，L20+ 趋近 uniform
77	  result_rationale: '四路 eval 已确认推理时 GAR 三路收敛（TG≈UG≈LoRA-only, Dongre GAR 0.013-0.016）。
78	    Attention heatmap 是这个数字结果的视觉解释：在推理时（自回归生成），所有四个模型的 attention pattern 几乎不可区分，因为
79	    gate attenuation 仅 2-7%（NF3），远不足以改变 attention 分布。具体而言，goal token 的 attention 在所有模型中都随
80	    turn 单调衰减， 衰减曲线高度相关（r>0.95）。浅层（L3-L5）对 goal 的 attention 略高是因为这些层 做局部 token mixing
81	    时 position 信号更强；深层（L20+）attention 趋向 uniform 是 attention sink 现象（Xiao et al. 2024）的体现。TG
82	    和 UG 的 gate 在推理时 mean=0.93-0.96， 对 attention pattern 的扰动在数值噪声范围内。
83	
84	    '
85	  tables:
86	  - name: 'Table: Goal attention by turn (4 models, aggregated over layers)'
87	    description: '4 模型 x 10 turn 的 goal attention weight 均值。四条曲线几乎重合。
88	
89	      '
90	  figures_description:
91	  - 'Fig: 4x3 grid heatmap（4 models x 3 convs），每个 cell 是 28 层 x T turn 的 attention-to-goal
92	    热力图。视觉上四行几乎不可区分，证明 gating 在推理时无法改变 attention pattern。'
93	  - 'Fig: 对比 TG 训练时 vs 推理时同一层（选 L14，gate dynamic range 最大的层之一）的 attention heatmap。训练时
94	    goal attention 清晰可见；推理时 goal attention 消失，直观展示 30x gap。'
95	  analysis: 'Heatmap 提供了 30x gap 的直观视觉证据。最有冲击力的 figure 是 TG 训练-推理对比： 同一个模型、同一层，在 teacher-forced
96	    context 下 goal attention 显著，在自回归 context 下完全消失。这直接支撑 SP1（exposure bias 摧毁 attention
97	    pattern 泛化性）。 四模型推理时 heatmap 的不可区分性支撑 C4（gating 零增量），比数字更有说服力。
98	
99	    '
100	- name: Llama-3.1-8B Phase 1 GAR Degradation Diagnosis
101	  plan_id: plan_009
102	  description: '在 Llama-3.1-8B base 模型上运行 GAR 诊断，确认跨架构的 GAR 衰减现象。 使用与 Qwen 相同的 eval
103	    对话和 GAR 计算方法。
104	
105	    '
106	  expected_results:
107	    turn1_avg_gar: 0.0351
108	    turn2_avg_gar: 0.0198
109	    turn3_avg_gar: 0.0173
110	    turn4_avg_gar: 0.0115
111	    turn5_avg_gar: 0.0109
112	    turn6_avg_gar: 0.0081
113	    turn7_avg_gar: 0.0069
114	    turn8_avg_gar: 0.0063
115	    turn9_avg_gar: 0.0098
116	    turn10_avg_gar: 0.0055
117	    mid_turns_avg_gar: 0.0107
118	    relative_drop: 0.69
119	    normalized_drop: 0.18
120	  result_rationale: 'Llama-3.1-8B 使用 GQA（grouped query attention）而非 Qwen 的 standard
121	    MHA， KV heads 更少（8 vs 28），这意味着每个 KV head 承载更多 query 的 attention。 尽管架构不同，GAR 衰减是
122	    Transformer 在长 context 下的结构性现象——随 turn 增长， context 窗口中 goal token 占比下降，attention
123	    被近期 token 和 attention sink 稀释。 Dongre 在 12 个不同模型上观察到 27-48% raw drop，Qwen 实测 70.8%。Llama-3
124	    的 relative drop 预期在 60-75% 范围（best 档要求 ≥50%），因为 GQA 的 KV 共享可能 稍微增加 attention 集中度，但不足以抵消
125	    context 长度带来的稀释。绝对 GAR 值可能 略低于 Qwen（0.035 vs 0.042），因为 Llama-3 的 attention 分布可能更分散（RoPE
126	    实现细节不同），但衰减模式（单调下降 + turn 9 微弱回升）应一致——回升是 eval 数据 中该 turn 恰好有 goal-relevant 内容的统计波动，不是系统性的。
127	
128	    '
129	  tables:
130	  - name: 'Table: Qwen vs Llama-3 GAR degradation comparison'
131	    description: '并排对比两个模型 10 turn 的 GAR 衰减曲线。格式：Turn | Qwen GAR | Llama GAR。 底部行显示
132	      relative_drop 和 mid_turns_avg。
133	
134	      '
135	  figures_description:
136	  - 'Fig: 双线折线图，X=turn, Y=GAR。Qwen（蓝）和 Llama-3（橙）衰减曲线形状高度相似，绝对值略有偏移。'
137	  analysis: 'Llama-3 的 69% relative drop 落在 best 档范围 [50%, 75%] 内，与 Qwen 的 70.8% 可比。这确认
138	    GAR 衰减不是 Qwen 特定的架构 artifact，而是跨架构的普遍现象。 为 C5（跨模型验证）和 C1（GAR 衰减普遍性）提供关键支撑。
139	
140	    '
141	- name: Llama-3.1-8B ThreadGate v7 Training
142	  plan_id: plan_010
143	  description: '在 Llama-3.1-8B 上复制 Qwen ThreadGate v7 训练设置（MSE+gate_div loss, LoRA
144	    r=16, 3 epoch on UltraChat subset）。验证 30x training-inference gap 跨模型存在。
145	
146	    '
147	  expected_results:
148	    training_gar_convergence: true
149	    gar_convergence_phase: A(gs0-90):plateau@0.015 B(gs90-170):rapid_rise C(gs170+):converged@0.42
150	    final_avg_loss: 0.912
151	    final_avg_ntp: 0.911
152	    final_avg_gar: 0.001
153	    final_avg_div: 0.0
154	    final_gate_mean: 0.941
155	    final_gate_std: 0.044
156	    final_gate_min: 0.802
157	    final_gate_max: 0.991
158	    final_profile_L3: 0.815
159	    final_profile_L4: 0.802
160	    training_time_hours: 6.8
161	    eval_dongre_turn1_gar: 0.0498
162	    eval_dongre_mid_gar: 0.0161
163	    eval_dongre_recovery_pp: 0.39
164	    eval_ours_mid_gar: 0.4203
165	    eval_ours_turn1_gar: 0.0437
166	    train_infer_gar_gap_ratio: 26
167	    gate_direction: 'WRONG: attenuate more at early turns'
168	    eval_gate_L14_turn1: 0.762
169	    eval_gate_L14_turn21: 0.958
170	    eval_gate_L14_diff: -0.196
171	  result_rationale: 'Llama-3.1-8B 有 32 层（vs Qwen 28 层），hidden dim 4096（vs 3584），使用
172	    GQA。 训练 GAR 收敛略低于 Qwen（0.42 vs 0.48），因为 GQA 的 KV 共享使得 gate 对 attention 的调控粒度更粗——每个
173	    gate 值影响 8 个 query head 的共同 KV representation， 调控精度不如 MHA。但 MSE target loss 的收敛机制是通用的（目标值明确→loss
174	    单调下降）， 所以训练仍然成功。推理时 Dongre GAR ~0.016，与 Qwen 几乎相同，因为推理时的 attention 分散是 context
175	    长度驱动的（与 gate 无关）。training-inference gap ratio = 0.42/0.016 ≈ 26x，落在 best 档 [20x,
176	    40x] 内。Gate profile 同样呈现反向 turn conditioning（深层 gate→1.0 at late turns），因为 NTP
177	    梯度压制是 loss landscape 的结构性特征，不依赖具体架构。NTP loss 略高（0.911 vs 0.896）， 因为 Llama-3 base
178	    的 NTP 起点更高（不同 tokenizer 和预训练数据）， 但训练 3 epoch 后 NTP 下降幅度相当。训练时间略长（6.8h vs 5.9h），
179	    因为 Llama-3 的 32 层比 Qwen 28 层多 14% 计算量，加上 GQA 的 KV projection 在 backward pass 中需要额外
180	    bookkeeping。
181	
182	    '
183	  tables:
184	  - name: 'Table: Llama-3 TG v7 training dynamics'
185	    description: '3 epoch 的 loss 组件（NTP, GAR, div）+ gate 统计（mean, std, min, max）。
186	      与 Qwen v7 同表格对比格式。
187	
188	      '
189	  - name: 'Table: Llama-3 vs Qwen train-inference gap comparison'
190	    description: 'Side-by-side: 训练 GAR | 推理 Dongre GAR | Gap ratio。 Llama: 0.42 /
191	      0.016 / 26x。Qwen: 0.48 / 0.016 / 30x。
192	
193	      '
194	  figures_description:
195	  - 'Fig: Llama-3 v7 训练 GAR 曲线，三阶段（plateau→rise→converge）清晰可见。与 Qwen 叠加对比，形状相似但 Llama
196	    收敛略低且 phase transition 略迟。'
197	  - 'Fig: Llama-3 gate profile 热力图（32 层 x eval turns），展示反向 turn conditioning。'
198	  analysis: 'Llama-3 的 26x gap 与 Qwen 的 30x gap 量级一致，确认 training-inference distribution
199	    shift 不是 Qwen 特有。训练 GAR 略低（0.42 vs 0.48）但推理 GAR 几乎相同（~0.016）， 这强化了核心论点：推理时的 attention
200	    分散是 teacher-forcing→autoregressive 分布偏移 的直接后果，与训练时的优化成功度无关。反向 turn conditioning
201	    在 32 层中同样出现， 进一步证实 NTP 梯度压制是 universal 的。
202	
203	    '
204	- name: Llama-3.1-8B LoRA-only Training
205	  plan_id: plan_011
206	  description: 'Llama-3.1-8B 上仅训练 LoRA（无 gate），NTP-only loss，作为 Llama 跨模型消融的 baseline。
207	
208	    '
209	  expected_results:
210	    epochs_completed: 3
211	    global_steps: 3000
212	    training_time_hours: 6.2
213	    final_ntp_loss: 0.908
214	    final_lora_size_mb: 22
215	    gate_fixed: 1
216	    gate_type_actual: none
217	  result_rationale: 'LoRA-only 训练是纯 NTP 微调，无 GAR loss，无 gate 参数。Llama-3 的 32 层比 Qwen
218	    28 层多 ~14% 的 LoRA 参数（每层一对 A/B 矩阵），因此 checkpoint 略大 （22MB vs 20MB）。NTP loss 收敛到
219	    0.908，略高于 Qwen LoRA-only 的 ~0.948 （因为 Llama 和 Qwen 的 tokenizer 不同导致 per-token
220	    entropy 分布不同， 绝对 NTP 值不直接可比，但收敛行为一致）。训练时间 6.2h，比 Qwen 的 5.7h 略长（同理，多 4 层）。这个实验本身没有
221	    interesting finding，价值在于为 plan_012 的三路 eval 提供 LoRA-only baseline。
222	
223	    '
224	  tables: []
225	  figures_description: []
226	  analysis: '纯 baseline 实验。关键输出是 checkpoint，供 plan_012 eval 使用。
227	
228	    '
229	- name: Llama-3.1-8B 3-Way Eval (Base/TG/LoRA-only)
230	  plan_id: plan_012
231	  description: '在 held-out eval set 上对 Llama-3 的 Base/TG/LoRA-only 三个模型进行 GAR + PPL
232	    评估。 验证 gating 零增量的跨模型普遍性。省略 UG 以节省 GPU（Qwen 已证明 UG≈TG）。
233	
234	    '
235	  expected_results:
236	    base_dongre_mid_gar: 0.0028
237	    base_dongre_recovery_pp: -0.95
238	    base_ppl: 4.51
239	    base_ntp: 1.4321
240	    tg_dongre_mid_gar: 0.0161
241	    tg_dongre_recovery_pp: 0.39
242	    tg_ppl: 2.91
243	    tg_ntp: 0.9912
244	    lora_dongre_mid_gar: 0.0142
245	    lora_dongre_recovery_pp: 0.22
246	    lora_ppl: 2.9
247	    lora_ntp: 0.9901
248	    tg_vs_lora_dongre_gar_diff_pp: 0.19
249	    tg_vs_lora_ppl_diff: 0.01
250	    three_way_convergence: true
251	    base_ours_mid_gar: 0.0118
252	    tg_ours_mid_gar: 0.4203
253	    lora_ours_mid_gar: 0.4147
254	  result_rationale: 'best 档要求 TG-LoRA Dongre GAR 差异 <1pp（实际预测 0.19pp），PPL 几乎相同。 三路收敛的原因与
255	    Qwen 完全一致：(1) 推理时 gate mean 0.94→接近 identity， gating 不改变 attention pattern；(2)
256	    LoRA 微调本身已经将 NTP 降到 ~0.99， gate 参数的额外自由度无法进一步改善；(3) GAR-ours 指标下 TG 和 LoRA 都在
257	    0.42-0.41，因为 teacher-forced context 下 LoRA 本身就优化了 representation quality。Dongre
258	    GAR 下 TG 0.016 vs LoRA 0.014 的微小差异在 bootstrap CI 的噪声范围内。PPL 方面 TG 略高于 LoRA（2.91
259	    vs 2.90），但差异 0.01 远在 统计噪声内。base model PPL 4.51（高于 Qwen 的 4.34），因为 Llama-3 的 tokenizer
260	    有 128k vocab（Qwen 152k），token 粒度不同导致 per-token PPL 绝对值不直接可比，但 LoRA 微调后的 PPL 改善比例一致（~35%
261	    drop）。
262	
263	    '
264	  tables:
265	  - name: 'Table: Llama-3 3-way eval results'
266	    description: 'Base / TG / LoRA-only 三行，列: GAR-ours mid | GAR-Dongre mid | Recovery
267	      pp (Dongre) | PPL | NTP。
268	
269	      '
270	  - name: 'Table: Cross-model convergence summary (Qwen + Llama)'
271	    description: '汇总两模型的 TG-LoRA diff（Dongre GAR pp 和 PPL）， 证明零增量结论跨模型成立。Qwen: 0.20pp
272	      / 0.00 PPL; Llama: 0.19pp / 0.01 PPL。
273	
274	      '
275	  figures_description:
276	  - 'Fig: 并排 bar chart（左 Qwen 右 Llama），每组 3 bars (Base/TG/LoRA)，Y=Dongre GAR。视觉上 TG
277	    和 LoRA 的 bar 不可区分。'
278	  analysis: 'Llama-3 三路收敛完美复现 Qwen 结果。TG-LoRA Dongre GAR diff 0.19pp 落在 best 档 [-0.5,
279	    1.0]pp 内。这是 C4（gating 零增量）和 C5（跨模型验证）的 关键证据。跨模型一致性将论文核心 claim 从 "在 Qwen 上观察到"
280	    升级为 "跨架构的普遍现象"。
281	
282	    '
283	- name: Llama-3.1-8B Gradient Conflict Analysis
284	  plan_id: plan_013
285	  description: '对 Llama-3 TG v7 的 3 个 epoch checkpoint 逐层计算 NTP-GAR 梯度冲突， 验证梯度压制机制的跨模型一致性。
286	
287	    '
288	  expected_results:
289	    epoch0_mean_cos_sim: -0.076
290	    epoch1_mean_cos_sim: -0.052
291	    epoch2_mean_cos_sim: -0.038
292	    epoch0_conflict_layer_pct: 0.75
293	    epoch1_conflict_layer_pct: 0.69
294	    epoch2_conflict_layer_pct: 0.63
295	    epoch0_mean_mag_ratio: 8.1
296	    epoch1_mean_mag_ratio: 11.5
297	    epoch2_mean_mag_ratio: 16.2
298	    epoch2_L31_mag_ratio: 982
299	    epoch2_L30_mag_ratio: 245
300	    epoch2_L3_mag_ratio: 3.6
301	  result_rationale: 'best 档要求 cos_sim 在 [-0.12, -0.03] 范围，mag_ratio final ≥5x。Llama-3
302	    有 32 层（vs Qwen 28），GQA 机制下每个 KV head 对应更多 query head，gate 的梯度信号来源更分散。具体而言，GAR
303	    loss 对 attention 的梯度需要经过 GQA 的 KV projection 反传到 gate，路径比 MHA 更间接（一个 KV head 的梯度是多个
304	    query head 梯度的聚合），导致 GAR gradient 信号略弱。因此 mag_ratio 可能 略高于 Qwen（16.2 vs 14.7），cos_sim
305	    绝对值略小（-0.038 vs -0.042）， 但方向一致。conflict_layer_pct 在 63-75% 范围，与 Qwen 的 67-79%
306	    可比。 深层 mag_ratio 爆炸到 ~1000x 的现象同样存在，因为这是 NTP loss 对最后几层 的反向传播路径优势造成的（与架构无关）。Llama-3
307	    的 32 层比 Qwen 多 4 层， 最深层的 GAR 梯度衰减更严重，理论上 L31 的 mag_ratio 可能比 Qwen L27 更高， 但由于
308	    GAR gradient 本身更弱，实际比值接近（982 vs 1139）。
309	
310	    '
311	  tables:
312	  - name: 'Table: Cross-model gradient conflict comparison'
313	    description: 'Qwen vs Llama 的 cos_sim 和 mag_ratio 逐 epoch 对比。 两模型的趋势（cos_sim 趋零
314	      + mag_ratio 增长）完全一致。
315	
316	      '
317	  figures_description:
318	  - 'Fig: 双模型逐层 mag_ratio 对比（epoch2），Qwen 28 层 + Llama 32 层。两条曲线形状相似，深层 mag_ratio
319	    指数增长。'
320	  analysis: '梯度冲突的跨模型一致性是 SP2（NTP-GAR 梯度竞争量化）的关键强化证据。 GQA vs MHA 的差异导致绝对值有偏移，但定性结论完全一致：
321	    (1) NTP 和 GAR 梯度方向冲突，(2) NTP 幅度压制随训练加剧， (3) 深层压制比浅层严重。这排除了 "梯度冲突是 Qwen 架构特有" 的质疑。
322	
323	    '
324	- name: Downstream Task Sanity Check
325	  plan_id: plan_014
326	  description: '设计简单的 instruction retention 测试：system prompt 包含明确指令（如 "always respond
327	    in bullet points"），测量 10 turn 后模型遵循指令的准确率，链接 GAR 到实际任务表现。
328	
329	    '
330	  expected_results:
331	    base_turn1_compliance: 0.88
332	    base_turn5_compliance: 0.71
333	    base_turn10_compliance: 0.54
334	    tg_turn1_compliance: 0.89
335	    tg_turn5_compliance: 0.72
336	    tg_turn10_compliance: 0.55
337	    lora_turn1_compliance: 0.88
338	    lora_turn5_compliance: 0.73
339	    lora_turn10_compliance: 0.56
340	    compliance_gar_correlation: 0.82
341	    cross_model_compliance_diff_pp: 1.2
342	  result_rationale: '这是 P2 优先级的 sanity check，主要目的是回应 W3（GAR 作为唯一代理指标）。 Instruction
343	    compliance 与 GAR 的相关性 ~0.82 预期较高但不为 1.0，因为 compliance 还取决于 instruction 复杂度、模型能力等
344	    GAR 以外的因素。关键预测 是三个模型的 compliance 几乎不可区分（diff <2pp），与 GAR Dongre 指标的 三路收敛一致。Base
345	    model compliance 也在同一范围（因为 eval 使用相同文本， base 没有 LoRA 微调但 instruction following
346	    是预训练能力的一部分）。 compliance 随 turn 单调下降（0.88→0.54）直观展示了 "模型在长对话中丢失指令"， 为非 NLP 背景的
347	    reviewer 提供了 GAR 的任务层面解释。但这个实验不会改变 paper 的核心论点（它只是 sanity check），所以数据放 Appendix。
348	
349	    '
350	  tables:
351	  - name: 'Table: Instruction compliance by turn and model'
352	    description: '4 模型 x 10 turn 的 compliance 率。附 GAR-compliance Pearson r。
353	
354	      '
355	  figures_description:
356	  - 'Fig: 双轴图，左轴 compliance rate（4 模型叠加），右轴 GAR（对应模型）。两组曲线同步下降，视觉上建立 GAR-compliance
357	    关联。'
358	  analysis: 'Sanity check 成功建立 GAR 和任务表现的关联（r=0.82），回应 W3。 模型间差异 <2pp 进一步确认 gating
359	    零增量不仅在 GAR 层面， 在下游任务层面也成立。数据放 Appendix B。
360	
361	    '
362	- name: Bootstrap CI for Zero Benefit (Held-out 50 convs)
363	  plan_id: plan_015
364	  description: '对 held-out eval 的 50 段对话，计算 TG-LoRA Dongre GAR 差异的 paired bootstrap
365	    95% CI。如果 CI 包含 0，统计支持 "zero benefit"。回应 W7（单 seed 无方差估计）。
366	
367	    '
368	  expected_results:
369	    n_conversations: 50
370	    n_bootstrap_samples: 10000
371	    tg_dongre_gar_mean: 0.0152
372	    lora_dongre_gar_mean: 0.0132
373	    paired_diff_mean: 0.002
374	    paired_diff_std: 0.0089
375	    ci_95_lower: -0.012
376	    ci_95_upper: 0.016
377	    ci_includes_zero: true
378	    effect_size_cohens_d: 0.022
379	    p_value_two_sided: 0.71
380	    tg_ours_gar_mean: 0.5035
381	    lora_ours_gar_mean: 0.4978
382	    ours_paired_diff_mean: 0.0057
383	    ours_ci_95_lower: -0.008
384	    ours_ci_95_upper: 0.019
385	    ours_ci_includes_zero: true
386	  result_rationale: 'best 档要求 bootstrap CI lower bound 在 [-0.015, 0.0]。预测 lower=-0.012，
387	    上界 +0.016，CI 包含 0。50 段对话的 paired design 提供足够 power 来检测 ≥2pp 的差异（power analysis:
388	    50 pairs, σ≈0.009, α=0.05, 可检测 δ≥0.005 with power ~0.80）。实际差异 0.20pp 远小于可检测阈值，因此
389	    p-value 高（0.71） 且 Cohen''s d 接近 0（0.022）。这不是 power 不足导致的 null（power 足以检测 有意义的差异），而是真正的
390	    zero effect。在 GAR-ours 定义下，CI 同样包含 0 （diff 0.57pp, CI [-0.8, 1.9]pp），两种定义一致支持
391	    "zero benefit"。 Effect size 的微小正值（TG 略高于 LoRA）在统计上与零不可区分，排除了 "gating 有微弱正效果但被噪声掩盖"
392	    的解释。
393	
394	    '
395	  tables:
396	  - name: 'Table: Bootstrap CI results for TG vs LoRA-only'
397	    description: '两行（GAR-Dongre / GAR-ours），列: Mean diff | SD | 95% CI | p-value |
398	      Cohen''s d。 两行 CI 均包含 0。
399	
400	      '
401	  figures_description:
402	  - 'Fig: Bootstrap 分布直方图 + CI bar。灰色直方图=10000 bootstrap samples 的 TG-LoRA diff 分布。红色竖线=0。蓝色
403	    bar=95% CI。CI 横跨 0。'
404	  analysis: 'Bootstrap CI 统计确认 "zero benefit"，直接回应 W7（单 seed）和 C4。 Cohen''s d ~0.02
405	    表明效应量在实践中可忽略。这是 paper 中 §6 (Experiments) 的核心统计证据，与四路 eval 的描述性统计互补。
406	
407	    '
408	- name: Exposure-Bias Mitigation (Scheduled Sampling for GAR Loss)
409	  plan_id: plan_016
410	  description: '在 ThreadGate v7 基础上引入 scheduled sampling：训练过程中逐步增加使用模型自身生成 （而非 gold
411	    context）来计算 GAR loss 的比例。初始 100% teacher-forced，线性增加到 epoch 3 结束时 50% model-generated。测试
412	    exposure bias mitigation 能否缩小 30x gap。
413	
414	    '
415	  expected_results:
416	    ss_schedule: linear 0%→50% model-generated over 3 epochs
417	    training_converged: true
418	    training_gar_final: 0.31
419	    training_ntp_final: 0.921
420	    training_time_hours: 9.2
421	    eval_dongre_mid_gar: 0.072
422	    eval_dongre_turn1_gar: 0.119
423	    eval_dongre_recovery_pp: 5.98
424	    eval_ours_mid_gar: 0.31
425	    eval_ours_turn1_gar: 0.087
426	    train_infer_gap_ratio: 4.3
427	    gap_reduction_factor: 7.0
428	    original_gap_ratio: 30
429	    mitigated_gap_ratio: 4.3
430	    gate_mean_final: 0.912
431	    gate_std_final: 0.063
432	    gate_direction_corrected: false
433	    gate_L14_turn1: 0.783
434	    gate_L14_turn21: 0.942
435	    remaining_gap_explanation: partial mitigation — 50% SS not enough to close fully
436	    eval_ppl: 2.71
437	    ppl_vs_tg_diff: 0.08
438	  result_rationale: 'Scheduled sampling 通过在训练中暴露模型自身的生成来缓解 teacher-forcing 和 autoregressive
439	    generation 之间的分布偏移。预测训练 GAR 从 0.48 降到 0.31 （因为 model-generated context 质量低于 gold
440	    context，GAR 更难优化）， 但推理 GAR 从 0.016 提升到 0.072——一个 4.5x 的改善。30x gap 缩小到 4.3x， gap
441	    reduction factor ~7x，超出 best 档要求 [3x, 6x] 上限，因为 best 档的 叙事需要足够大的 gap reduction
442	    来 convincingly 证明 "exposure bias 是因果因素"。
443	
444	    机制解释：在训练中使用 model-generated context 时，attention pattern 被迫 适应噪声更大、偏离 gold 分布的输入。这相当于
445	    data augmentation——模型看到了 更接近推理时实际遇到的 context，因此学到的 attention pattern 更鲁棒。但 gap
446	    未完全关闭（4.3x 而非 1x）有两个原因：(1) 50% SS 比例不够——即使最终只有 50% model-generated，仍有 50% teacher-forced
447	    样本，模型在两种分布间折中； (2) model-generated context 的质量在训练早期很差（模型尚未学好），导致 GAR 信号噪声极大，gate
448	    在这些样本上收到混乱梯度。
449	
450	    推理 GAR 0.072 落在 best 档 [0.05, 0.10] 内。虽然远未达到训练时的 0.31， 但比原始 TG 的 0.016 有 4.5x
451	    改善，这是论文升级的关键数据点： (1) 证明 exposure bias 确实是 30x gap 的因果因素（缓解 exposure bias → gap
452	    缩小）； (2) 表明完全解决需要更激进的 mitigation（100% SS 或 policy gradient 方法）； (3) 为 Discussion
453	    中的 "future directions" 提供实证支撑。
454	
455	    训练时间增加（9.2h vs 5.9h），因为 model-generated context 需要额外的 forward pass（teacher-forcing
456	    只需一次 forward，SS 需要先 generate 再 forward）。 PPL 略高于纯 TG（2.71 vs 2.63），因为 SS 引入的噪声稍微干扰了
457	    NTP 优化， 但差异不大（0.08）。Gate profile 仍然显示反向 turn conditioning（未完全纠正）， 因为 NTP 梯度压制的根本机制未改变——SS
458	    只是让 GAR 信号在推理分布上更准， 但不改变 NTP 和 GAR 的力量对比。
459	
460	    '
461	  tables:
462	  - name: 'Table: Exposure-bias mitigation results'
463	    description: '三行（TG-original / TG-SS / LoRA-only），列: Train GAR | Infer Dongre
464	      GAR | Gap ratio | PPL。TG-SS 的 gap ratio 从 30x 缩小到 4.3x。
465	
466	      '
467	  - name: 'Table: Gap reduction analysis'
468	    description: 'Original gap (30x) → Mitigated gap (4.3x) → Reduction factor (7.0x)。
469	      附 percentage of gap explained by exposure bias: ~86%。
470	
471	      '
472	  figures_description:
473	  - 'Fig: Bar chart 三组（TG / TG-SS / LoRA-only），每组双 bar（训练 GAR 蓝色 / 推理 GAR 橙色）。TG 的蓝-橙
474	    gap 巨大，TG-SS 的 gap 显著缩小，LoRA 无训练 GAR。'
475	  - 'Fig: 训练曲线对比（TG vs TG-SS），X=global step, Y=GAR。TG-SS 曲线低于 TG（因为 model-generated
476	    context 更难），但最终仍收敛。'
477	  - 'Fig: 因果推理图 (causal diagram)。Exposure bias → 30x gap。Mitigation (SS) → gap 缩小到
478	    4.3x。剩余 4.3x → 其他因素（NTP 压制 + gate 架构限制）。'
479	  analysis: '这是 best 档最关键的新实验。gap reduction factor 7x 提供了 exposure bias 因果关系的直接证据：如果
480	    30x gap 不是由 exposure bias 造成的，那么缓解 exposure bias 不应缩小 gap。但实际缩小了 7x，说明 exposure
481	    bias 解释了 gap 的主要部分（~86% in log scale: log(30)/log(4.3)≈1.47/0.63， exposure bias
482	    解释了 (1.47-0.63)/1.47≈57% 的 log-gap，或等价地 (30-4.3)/30≈86% 的 linear gap）。
483	
484	    论文叙事升级路径： §7 Analysis 新增 "Exposure Bias as Causal Factor" 小节，展示 SS 实验数据。 §8 Discussion
485	    从 "这些方向值得探索" 变为 "我们已初步验证 exposure bias mitigation 的有效性，但完全解决需要更强的技术（policy gradient
486	    / 100% SS / inference-time intervention）"。 Abstract 从 "negative result + mechanistic
487	    insight" 升级为 "negative result + diagnosis + partial cure via exposure bias mitigation"。
488	    贡献列表新增 "首个在 auxiliary attention loss 上验证 scheduled sampling 缓解 exposure bias 的实证"
489	    作为第 4 贡献（在跨模型验证之前）。
490	
491	    '
492	- name: Qwen v7 Gradient Conflict (Formal Run)
493	  plan_id: plan_006
494	  description: '[注：此为 plan_006 的正式实验执行记录，与上方 "Qwen v7 Gradient Conflict Analysis"
495	    为同一实验的两种描述角度。以上已在首条 imagined_experiment 中详细展开。此处仅标注 plan_id 对应关系，避免重复。]
496	
497	    '
498	  expected_results:
499	    see_first_entry: true
500	  result_rationale: 见首条 imagined_experiment (plan_006)
501	  tables: []
502	  figures_description: []
503	  analysis: 见首条 imagined_experiment
504	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84b7531c-6e7b-4af7-975e-605b39e6849a",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "b3d63107-5537-455d-8cb5-a65637754b9b",
  "sourceToolAssistantUUID": "84b7531c-6e7b-4af7-975e-605b39e6849a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T15:28:32.075Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GGvShVdXrXVWQdmRfkJrPV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3d63107-5537-455d-8cb5-a65637754b9b",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAUxBwovJg7wq8RcpVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4988aaf8-b733-40fa-aed4-28fb54accdfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULr9piBaNQbya5914NvZE4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 16512,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 16512,
          "cache_creation_input_tokens": 1875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1875,
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

_source line 18 · 2026-05-19T15:28:32.082Z_

<details><summary>↩ Tool result · `toolu_01GGvShVdXrXVWQdmRfkJrPV`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立且增强。C1-C5 全部验证。Llama-3 跨模型数据将 ''30x gap 是 exposure
3	  bias 在 auxiliary attention loss 上的首个定量测量'' 从单模型观察升级为普遍现象。Mitigation 实验闭合因果环 （缓解
4	  exposure bias → gap 缩小 → 确认 exposure bias 是根因），论文从纯 negative result 升级为 ''diagnosis
5	  + partial cure''。投 EMNLP Main，reviewer 可能给 Borderline Accept (3.5-4.0)。
6	
7	  '
8	imagined_experiments:
9	- name: Qwen v7 Gradient Conflict Analysis (3 checkpoints)
10	  plan_id: plan_006
11	  description: '对 v7 训练的 3 个 epoch checkpoint 逐层计算 NTP 和 GAR loss 对 gate 参数的梯度， 得到
12	    cos_sim（方向冲突）和 mag_ratio（幅度压制），量化 NTP 如何系统性压制 GAR 信号。
13	
14	    '
15	  expected_results:
16	    epoch0_mean_cos_sim: -0.089
17	    epoch1_mean_cos_sim: -0.061
18	    epoch2_mean_cos_sim: -0.042
19	    epoch0_conflict_layer_pct: 0.79
20	    epoch1_conflict_layer_pct: 0.71
21	    epoch2_conflict_layer_pct: 0.67
22	    epoch0_mean_mag_ratio: 7.5
23	    epoch1_mean_mag_ratio: 10.8
24	    epoch2_mean_mag_ratio: 14.7
25	    epoch2_L27_mag_ratio: 1139
26	    epoch2_L26_mag_ratio: 287
27	    epoch2_L3_mag_ratio: 3.2
28	    epoch0_gar_grad_norm_mean: 0.0041
29	    epoch2_gar_grad_norm_mean: 0.00089
30	    epoch0_ntp_grad_norm_mean: 0.031
31	    epoch2_ntp_grad_norm_mean: 0.013
32	  result_rationale: 'v7 使用 MSE target loss（GAR 收敛到 0.48 后 loss→0），因此 GAR 梯度随训练递减是结构性的：
33	    target 达成后 loss landscape 变平，梯度自然衰减。但 NTP loss 始终活跃（final ~0.896）， 其梯度虽也下降但幅度远小于
34	    GAR。结果是 mag_ratio 从 7.5x 增长到 14.7x——不是因为 NTP 变强，而是 GAR 变弱。cos_sim 从 -0.089 趋向
35	    -0.042 表面上是"冲突缓解"，实质是 GAR 信号被边缘化后无力对抗。深层（L26-L27）mag_ratio 爆炸到 100-1000x，因为这些层
36	    NTP loss 的反向传播路径更短、梯度更强，而 GAR 信号经过多层衰减后几乎消失。这解释了 NF1 中 27/28 层 gate diff < 0 的反向
37	    turn conditioning：NTP 推 gate→1.0 的力量在深层 无人对抗，gate 在这些层完全服从 NTP。
38	
39	    '
40	  tables:
41	  - name: 'Table: Per-layer gradient conflict across training'
42	    description: '28 层 x 3 epoch 的 cos_sim 和 mag_ratio 热力图表。行=层，列=epoch。 深层呈现 mag_ratio
43	      指数增长，浅层相对温和（3-8x）。cos_sim 在大多数层为负值， 但绝对值随训练减小（GAR 信号消失而非调和）。
44	
45	      '
46	  - name: 'Table: Summary statistics by epoch'
47	    description: '汇总 mean/median/max cos_sim, mag_ratio, conflict_layer_pct。 关键数字：conflict_pct
48	      67-79%, mag_ratio 7.5→14.7x。
49	
50	      '
51	  figures_description:
52	  - 'Fig: 双轴折线图。左轴 cos_sim（3 条线=3 epoch across 28 layers），右轴 mag_ratio（同）。X 轴=层编号。展示深层
53	    mag_ratio 爆炸性增长 + cos_sim 在大多数层为负值。'
54	  - 'Fig: 训练过程中 GAR vs NTP 梯度 L2-norm 的衰减曲线。GAR norm 衰减 ~5x，NTP norm 衰减 ~2.4x，差距拉大。'
55	  analysis: '梯度冲突数据完整支撑 C3 和 SP2。三个关键 insight：(1) 方向冲突（cos_sim 负值）证实 NTP 和 GAR 在 gate
56	    参数空间确实竞争；(2) 幅度压制（mag_ratio 14.7x）证实 GAR 信号 不足以改变 gate 行为；(3) 冲突"缓解"的机制是 GAR 边缘化而非调和，这是
57	    paper 中 需要清晰传达的反直觉发现。与 NF1 的 gate profile 数据形成因果链： 梯度压制 → gate 服从 NTP → 反向 turn
58	    conditioning → 推理时干预不足。
59	
60	    '
61	- name: Attention Heatmap Visualization (4 models x 3 convs x 28 layers)
62	  plan_id: plan_007
63	  description: '对 Base/TG/UG/LoRA-only 四个模型，各取 3 段多轮对话，可视化 28 层的 attention 分布。 关注
64	    goal token（system prompt + first user query）在不同 turn 的 attention weight。
65	
66	    '
67	  expected_results:
68	    base_goal_attn_turn1: 0.042
69	    base_goal_attn_turn10: 0.008
70	    tg_goal_attn_turn1: 0.039
71	    tg_goal_attn_turn10: 0.009
72	    ug_goal_attn_turn1: 0.041
73	    ug_goal_attn_turn10: 0.008
74	    lora_goal_attn_turn1: 0.04
75	    lora_goal_attn_turn10: 0.009
76	    cross_model_attn_pattern_correlation: 0.97
77	    layer_specific_pattern: L3-L5 goal attn 最高，L20+ 趋近 uniform
78	  result_rationale: '四路 eval 已确认推理时 GAR 三路收敛（TG≈UG≈LoRA-only, Dongre GAR 0.013-0.016）。
79	    Attention heatmap 是这个数字结果的视觉解释：在推理时（自回归生成），所有四个模型的 attention pattern 几乎不可区分，因为
80	    gate attenuation 仅 2-7%（NF3），远不足以改变 attention 分布。具体而言，goal token 的 attention 在所有模型中都随
81	    turn 单调衰减， 衰减曲线高度相关（r>0.95）。浅层（L3-L5）对 goal 的 attention 略高是因为这些层 做局部 token mixing
82	    时 position 信号更强；深层（L20+）attention 趋向 uniform 是 attention sink 现象（Xiao et al. 2024）的体现。TG
83	    和 UG 的 gate 在推理时 mean=0.93-0.96， 对 attention pattern 的扰动在数值噪声范围内。
84	
85	    '
86	  tables:
87	  - name: 'Table: Goal attention by turn (4 models, aggregated over layers)'
88	    description: '4 模型 x 10 turn 的 goal attention weight 均值。四条曲线几乎重合。
89	
90	      '
91	  figures_description:
92	  - 'Fig: 4x3 grid heatmap（4 models x 3 convs），每个 cell 是 28 层 x T turn 的 attention-to-goal
93	    热力图。视觉上四行几乎不可区分，证明 gating 在推理时无法改变 attention pattern。'
94	  - 'Fig: 对比 TG 训练时 vs 推理时同一层（选 L14，gate dynamic range 最大的层之一）的 attention heatmap。训练时
95	    goal attention 清晰可见；推理时 goal attention 消失，直观展示 30x gap。'
96	  analysis: 'Heatmap 提供了 30x gap 的直观视觉证据。最有冲击力的 figure 是 TG 训练-推理对比： 同一个模型、同一层，在 teacher-forced
97	    context 下 goal attention 显著，在自回归 context 下完全消失。这直接支撑 SP1（exposure bias 摧毁 attention
98	    pattern 泛化性）。 四模型推理时 heatmap 的不可区分性支撑 C4（gating 零增量），比数字更有说服力。
99	
100	    '
101	- name: Llama-3.1-8B Phase 1 GAR Degradation Diagnosis
102	  plan_id: plan_009
103	  description: '在 Llama-3.1-8B base 模型上运行 GAR 诊断，确认跨架构的 GAR 衰减现象。 使用与 Qwen 相同的 eval
104	    对话和 GAR 计算方法。
105	
106	    '
107	  expected_results:
108	    turn1_avg_gar: 0.0351
109	    turn2_avg_gar: 0.0198
110	    turn3_avg_gar: 0.0173
111	    turn4_avg_gar: 0.0115
112	    turn5_avg_gar: 0.0109
113	    turn6_avg_gar: 0.0081
114	    turn7_avg_gar: 0.0069
115	    turn8_avg_gar: 0.0063
116	    turn9_avg_gar: 0.0098
117	    turn10_avg_gar: 0.0055
118	    mid_turns_avg_gar: 0.0107
119	    relative_drop: 0.69
120	    normalized_drop: 0.18
121	  result_rationale: 'Llama-3.1-8B 使用 GQA（grouped query attention）而非 Qwen 的 standard
122	    MHA， KV heads 更少（8 vs 28），这意味着每个 KV head 承载更多 query 的 attention。 尽管架构不同，GAR 衰减是
123	    Transformer 在长 context 下的结构性现象——随 turn 增长， context 窗口中 goal token 占比下降，attention
124	    被近期 token 和 attention sink 稀释。 Dongre 在 12 个不同模型上观察到 27-48% raw drop，Qwen 实测 70.8%。Llama-3
125	    的 relative drop 预期在 60-75% 范围（best 档要求 ≥50%），因为 GQA 的 KV 共享可能 稍微增加 attention 集中度，但不足以抵消
126	    context 长度带来的稀释。绝对 GAR 值可能 略低于 Qwen（0.035 vs 0.042），因为 Llama-3 的 attention 分布可能更分散（RoPE
127	    实现细节不同），但衰减模式（单调下降 + turn 9 微弱回升）应一致——回升是 eval 数据 中该 turn 恰好有 goal-relevant 内容的统计波动，不是系统性的。
128	
129	    '
130	  tables:
131	  - name: 'Table: Qwen vs Llama-3 GAR degradation comparison'
132	    description: '并排对比两个模型 10 turn 的 GAR 衰减曲线。格式：Turn | Qwen GAR | Llama GAR。 底部行显示
133	      relative_drop 和 mid_turns_avg。
134	
135	      '
136	  figures_description:
137	  - 'Fig: 双线折线图，X=turn, Y=GAR。Qwen（蓝）和 Llama-3（橙）衰减曲线形状高度相似，绝对值略有偏移。'
138	  analysis: 'Llama-3 的 69% relative drop 落在 best 档范围 [50%, 75%] 内，与 Qwen 的 70.8% 可比。这确认
139	    GAR 衰减不是 Qwen 特定的架构 artifact，而是跨架构的普遍现象。 为 C5（跨模型验证）和 C1（GAR 衰减普遍性）提供关键支撑。
140	
141	    '
142	- name: Llama-3.1-8B ThreadGate v7 Training
143	  plan_id: plan_010
144	  description: '在 Llama-3.1-8B 上复制 Qwen ThreadGate v7 训练设置（MSE+gate_div loss, LoRA
145	    r=16, 3 epoch on UltraChat subset）。验证 30x training-inference gap 跨模型存在。
146	
147	    '
148	  expected_results:
149	    training_gar_convergence: true
150	    gar_convergence_phase: A(gs0-90):plateau@0.015 B(gs90-170):rapid_rise C(gs170+):converged@0.42
151	    final_avg_loss: 0.912
152	    final_avg_ntp: 0.911
153	    final_avg_gar: 0.001
154	    final_avg_div: 0.0
155	    final_gate_mean: 0.941
156	    final_gate_std: 0.044
157	    final_gate_min: 0.802
158	    final_gate_max: 0.991
159	    final_profile_L3: 0.815
160	    final_profile_L4: 0.802
161	    training_time_hours: 6.8
162	    eval_dongre_turn1_gar: 0.0498
163	    eval_dongre_mid_gar: 0.0161
164	    eval_dongre_recovery_pp: 0.39
165	    eval_ours_mid_gar: 0.4203
166	    eval_ours_turn1_gar: 0.0437
167	    train_infer_gar_gap_ratio: 26
168	    gate_direction: 'WRONG: attenuate more at early turns'
169	    eval_gate_L14_turn1: 0.762
170	    eval_gate_L14_turn21: 0.958
171	    eval_gate_L14_diff: -0.196
172	  result_rationale: 'Llama-3.1-8B 有 32 层（vs Qwen 28 层），hidden dim 4096（vs 3584），使用
173	    GQA。 训练 GAR 收敛略低于 Qwen（0.42 vs 0.48），因为 GQA 的 KV 共享使得 gate 对 attention 的调控粒度更粗——每个
174	    gate 值影响 8 个 query head 的共同 KV representation， 调控精度不如 MHA。但 MSE target loss 的收敛机制是通用的（目标值明确→loss
175	    单调下降）， 所以训练仍然成功。推理时 Dongre GAR ~0.016，与 Qwen 几乎相同，因为推理时的 attention 分散是 context
176	    长度驱动的（与 gate 无关）。training-inference gap ratio = 0.42/0.016 ≈ 26x，落在 best 档 [20x,
177	    40x] 内。Gate profile 同样呈现反向 turn conditioning（深层 gate→1.0 at late turns），因为 NTP
178	    梯度压制是 loss landscape 的结构性特征，不依赖具体架构。NTP loss 略高（0.911 vs 0.896）， 因为 Llama-3 base
179	    的 NTP 起点更高（不同 tokenizer 和预训练数据）， 但训练 3 epoch 后 NTP 下降幅度相当。训练时间略长（6.8h vs 5.9h），
180	    因为 Llama-3 的 32 层比 Qwen 28 层多 14% 计算量，加上 GQA 的 KV projection 在 backward pass 中需要额外
181	    bookkeeping。
182	
183	    '
184	  tables:
185	  - name: 'Table: Llama-3 TG v7 training dynamics'
186	    description: '3 epoch 的 loss 组件（NTP, GAR, div）+ gate 统计（mean, std, min, max）。
187	      与 Qwen v7 同表格对比格式。
188	
189	      '
190	  - name: 'Table: Llama-3 vs Qwen train-inference gap comparison'
191	    description: 'Side-by-side: 训练 GAR | 推理 Dongre GAR | Gap ratio。 Llama: 0.42 /
192	      0.016 / 26x。Qwen: 0.48 / 0.016 / 30x。
193	
194	      '
195	  figures_description:
196	  - 'Fig: Llama-3 v7 训练 GAR 曲线，三阶段（plateau→rise→converge）清晰可见。与 Qwen 叠加对比，形状相似但 Llama
197	    收敛略低且 phase transition 略迟。'
198	  - 'Fig: Llama-3 gate profile 热力图（32 层 x eval turns），展示反向 turn conditioning。'
199	  analysis: 'Llama-3 的 26x gap 与 Qwen 的 30x gap 量级一致，确认 training-inference distribution
200	    shift 不是 Qwen 特有。训练 GAR 略低（0.42 vs 0.48）但推理 GAR 几乎相同（~0.016）， 这强化了核心论点：推理时的 attention
201	    分散是 teacher-forcing→autoregressive 分布偏移 的直接后果，与训练时的优化成功度无关。反向 turn conditioning
202	    在 32 层中同样出现， 进一步证实 NTP 梯度压制是 universal 的。
203	
204	    '
205	- name: Llama-3.1-8B LoRA-only Training
206	  plan_id: plan_011
207	  description: 'Llama-3.1-8B 上仅训练 LoRA（无 gate），NTP-only loss，作为 Llama 跨模型消融的 baseline。
208	
209	    '
210	  expected_results:
211	    epochs_completed: 3
212	    global_steps: 3000
213	    training_time_hours: 6.2
214	    final_ntp_loss: 0.908
215	    final_lora_size_mb: 22
216	    gate_fixed: 1
217	    gate_type_actual: none
218	  result_rationale: 'LoRA-only 训练是纯 NTP 微调，无 GAR loss，无 gate 参数。Llama-3 的 32 层比 Qwen
219	    28 层多 ~14% 的 LoRA 参数（每层一对 A/B 矩阵），因此 checkpoint 略大 （22MB vs 20MB）。NTP loss 收敛到
220	    0.908，略高于 Qwen LoRA-only 的 ~0.948 （因为 Llama 和 Qwen 的 tokenizer 不同导致 per-token
221	    entropy 分布不同， 绝对 NTP 值不直接可比，但收敛行为一致）。训练时间 6.2h，比 Qwen 的 5.7h 略长（同理，多 4 层）。这个实验本身没有
222	    interesting finding，价值在于为 plan_012 的三路 eval 提供 LoRA-only baseline。
223	
224	    '
225	  tables: []
226	  figures_description: []
227	  analysis: '纯 baseline 实验。关键输出是 checkpoint，供 plan_012 eval 使用。
228	
229	    '
230	- name: Llama-3.1-8B 3-Way Eval (Base/TG/LoRA-only)
231	  plan_id: plan_012
232	  description: '在 held-out eval set 上对 Llama-3 的 Base/TG/LoRA-only 三个模型进行 GAR + PPL
233	    评估。 验证 gating 零增量的跨模型普遍性。省略 UG 以节省 GPU（Qwen 已证明 UG≈TG）。
234	
235	    '
236	  expected_results:
237	    base_dongre_mid_gar: 0.0028
238	    base_dongre_recovery_pp: -0.95
239	    base_ppl: 4.51
240	    base_ntp: 1.4321
241	    tg_dongre_mid_gar: 0.0161
242	    tg_dongre_recovery_pp: 0.39
243	    tg_ppl: 2.91
244	    tg_ntp: 0.9912
245	    lora_dongre_mid_gar: 0.0142
246	    lora_dongre_recovery_pp: 0.22
247	    lora_ppl: 2.9
248	    lora_ntp: 0.9901
249	    tg_vs_lora_dongre_gar_diff_pp: 0.19
250	    tg_vs_lora_ppl_diff: 0.01
251	    three_way_convergence: true
252	    base_ours_mid_gar: 0.0118
253	    tg_ours_mid_gar: 0.4203
254	    lora_ours_mid_gar: 0.4147
255	  result_rationale: 'best 档要求 TG-LoRA Dongre GAR 差异 <1pp（实际预测 0.19pp），PPL 几乎相同。 三路收敛的原因与
256	    Qwen 完全一致：(1) 推理时 gate mean 0.94→接近 identity， gating 不改变 attention pattern；(2)
257	    LoRA 微调本身已经将 NTP 降到 ~0.99， gate 参数的额外自由度无法进一步改善；(3) GAR-ours 指标下 TG 和 LoRA 都在
258	    0.42-0.41，因为 teacher-forced context 下 LoRA 本身就优化了 representation quality。Dongre
259	    GAR 下 TG 0.016 vs LoRA 0.014 的微小差异在 bootstrap CI 的噪声范围内。PPL 方面 TG 略高于 LoRA（2.91
260	    vs 2.90），但差异 0.01 远在 统计噪声内。base model PPL 4.51（高于 Qwen 的 4.34），因为 Llama-3 的 tokenizer
261	    有 128k vocab（Qwen 152k），token 粒度不同导致 per-token PPL 绝对值不直接可比，但 LoRA 微调后的 PPL 改善比例一致（~35%
262	    drop）。
263	
264	    '
265	  tables:
266	  - name: 'Table: Llama-3 3-way eval results'
267	    description: 'Base / TG / LoRA-only 三行，列: GAR-ours mid | GAR-Dongre mid | Recovery
268	      pp (Dongre) | PPL | NTP。
269	
270	      '
271	  - name: 'Table: Cross-model convergence summary (Qwen + Llama)'
272	    description: '汇总两模型的 TG-LoRA diff（Dongre GAR pp 和 PPL）， 证明零增量结论跨模型成立。Qwen: 0.20pp
273	      / 0.00 PPL; Llama: 0.19pp / 0.01 PPL。
274	
275	      '
276	  figures_description:
277	  - 'Fig: 并排 bar chart（左 Qwen 右 Llama），每组 3 bars (Base/TG/LoRA)，Y=Dongre GAR。视觉上 TG
278	    和 LoRA 的 bar 不可区分。'
279	  analysis: 'Llama-3 三路收敛完美复现 Qwen 结果。TG-LoRA Dongre GAR diff 0.19pp 落在 best 档 [-0.5,
280	    1.0]pp 内。这是 C4（gating 零增量）和 C5（跨模型验证）的 关键证据。跨模型一致性将论文核心 claim 从 "在 Qwen 上观察到"
281	    升级为 "跨架构的普遍现象"。
282	
283	    '
284	- name: Llama-3.1-8B Gradient Conflict Analysis
285	  plan_id: plan_013
286	  description: '对 Llama-3 TG v7 的 3 个 epoch checkpoint 逐层计算 NTP-GAR 梯度冲突， 验证梯度压制机制的跨模型一致性。
287	
288	    '
289	  expected_results:
290	    epoch0_mean_cos_sim: -0.076
291	    epoch1_mean_cos_sim: -0.052
292	    epoch2_mean_cos_sim: -0.038
293	    epoch0_conflict_layer_pct: 0.75
294	    epoch1_conflict_layer_pct: 0.69
295	    epoch2_conflict_layer_pct: 0.63
296	    epoch0_mean_mag_ratio: 8.1
297	    epoch1_mean_mag_ratio: 11.5
298	    epoch2_mean_mag_ratio: 16.2
299	    epoch2_L31_mag_ratio: 982
300	    epoch2_L30_mag_ratio: 245
301	    epoch2_L3_mag_ratio: 3.6
302	  result_rationale: 'best 档要求 cos_sim 在 [-0.12, -0.03] 范围，mag_ratio final ≥5x。Llama-3
303	    有 32 层（vs Qwen 28），GQA 机制下每个 KV head 对应更多 query head，gate 的梯度信号来源更分散。具体而言，GAR
304	    loss 对 attention 的梯度需要经过 GQA 的 KV projection 反传到 gate，路径比 MHA 更间接（一个 KV head 的梯度是多个
305	    query head 梯度的聚合），导致 GAR gradient 信号略弱。因此 mag_ratio 可能 略高于 Qwen（16.2 vs 14.7），cos_sim
306	    绝对值略小（-0.038 vs -0.042）， 但方向一致。conflict_layer_pct 在 63-75% 范围，与 Qwen 的 67-79%
307	    可比。 深层 mag_ratio 爆炸到 ~1000x 的现象同样存在，因为这是 NTP loss 对最后几层 的反向传播路径优势造成的（与架构无关）。Llama-3
308	    的 32 层比 Qwen 多 4 层， 最深层的 GAR 梯度衰减更严重，理论上 L31 的 mag_ratio 可能比 Qwen L27 更高， 但由于
309	    GAR gradient 本身更弱，实际比值接近（982 vs 1139）。
310	
311	    '
312	  tables:
313	  - name: 'Table: Cross-model gradient conflict comparison'
314	    description: 'Qwen vs Llama 的 cos_sim 和 mag_ratio 逐 epoch 对比。 两模型的趋势（cos_sim 趋零
315	      + mag_ratio 增长）完全一致。
316	
317	      '
318	  figures_description:
319	  - 'Fig: 双模型逐层 mag_ratio 对比（epoch2），Qwen 28 层 + Llama 32 层。两条曲线形状相似，深层 mag_ratio
320	    指数增长。'
321	  analysis: '梯度冲突的跨模型一致性是 SP2（NTP-GAR 梯度竞争量化）的关键强化证据。 GQA vs MHA 的差异导致绝对值有偏移，但定性结论完全一致：
322	    (1) NTP 和 GAR 梯度方向冲突，(2) NTP 幅度压制随训练加剧， (3) 深层压制比浅层严重。这排除了 "梯度冲突是 Qwen 架构特有" 的质疑。
323	
324	    '
325	- name: Downstream Task Sanity Check
326	  plan_id: plan_014
327	  description: '设计简单的 instruction retention 测试：system prompt 包含明确指令（如 "always respond
328	    in bullet points"），测量 10 turn 后模型遵循指令的准确率，链接 GAR 到实际任务表现。
329	
330	    '
331	  expected_results:
332	    base_turn1_compliance: 0.88
333	    base_turn5_compliance: 0.71
334	    base_turn10_compliance: 0.54
335	    tg_turn1_compliance: 0.89
336	    tg_turn5_compliance: 0.72
337	    tg_turn10_compliance: 0.55
338	    lora_turn1_compliance: 0.88
339	    lora_turn5_compliance: 0.73
340	    lora_turn10_compliance: 0.56
341	    compliance_gar_correlation: 0.82
342	    cross_model_compliance_diff_pp: 1.2
343	  result_rationale: '这是 P2 优先级的 sanity check，主要目的是回应 W3（GAR 作为唯一代理指标）。 Instruction
344	    compliance 与 GAR 的相关性 ~0.82 预期较高但不为 1.0，因为 compliance 还取决于 instruction 复杂度、模型能力等
345	    GAR 以外的因素。关键预测 是三个模型的 compliance 几乎不可区分（diff <2pp），与 GAR Dongre 指标的 三路收敛一致。Base
346	    model compliance 也在同一范围（因为 eval 使用相同文本， base 没有 LoRA 微调但 instruction following
347	    是预训练能力的一部分）。 compliance 随 turn 单调下降（0.88→0.54）直观展示了 "模型在长对话中丢失指令"， 为非 NLP 背景的
348	    reviewer 提供了 GAR 的任务层面解释。但这个实验不会改变 paper 的核心论点（它只是 sanity check），所以数据放 Appendix。
349	
350	    '
351	  tables:
352	  - name: 'Table: Instruction compliance by turn and model'
353	    description: '4 模型 x 10 turn 的 compliance 率。附 GAR-compliance Pearson r。
354	
355	      '
356	  figures_description:
357	  - 'Fig: 双轴图，左轴 compliance rate（4 模型叠加），右轴 GAR（对应模型）。两组曲线同步下降，视觉上建立 GAR-compliance
358	    关联。'
359	  analysis: 'Sanity check 成功建立 GAR 和任务表现的关联（r=0.82），回应 W3。 模型间差异 <2pp 进一步确认 gating
360	    零增量不仅在 GAR 层面， 在下游任务层面也成立。数据放 Appendix B。
361	
362	    '
363	- name: Bootstrap CI for Zero Benefit (Held-out 50 convs)
364	  plan_id: plan_015
365	  description: '对 held-out eval 的 50 段对话，计算 TG-LoRA Dongre GAR 差异的 paired bootstrap
366	    95% CI。如果 CI 包含 0，统计支持 "zero benefit"。回应 W7（单 seed 无方差估计）。
367	
368	    '
369	  expected_results:
370	    n_conversations: 50
371	    n_bootstrap_samples: 10000
372	    tg_dongre_gar_mean: 0.0152
373	    lora_dongre_gar_mean: 0.0132
374	    paired_diff_mean: 0.002
375	    paired_diff_std: 0.0089
376	    ci_95_lower: -0.012
377	    ci_95_upper: 0.016
378	    ci_includes_zero: true
379	    effect_size_cohens_d: 0.022
380	    p_value_two_sided: 0.71
381	    tg_ours_gar_mean: 0.5035
382	    lora_ours_gar_mean: 0.4978
383	    ours_paired_diff_mean: 0.0057
384	    ours_ci_95_lower: -0.008
385	    ours_ci_95_upper: 0.019
386	    ours_ci_includes_zero: true
387	  result_rationale: 'best 档要求 bootstrap CI lower bound 在 [-0.015, 0.0]。预测 lower=-0.012，
388	    上界 +0.016，CI 包含 0。50 段对话的 paired design 提供足够 power 来检测 ≥2pp 的差异（power analysis:
389	    50 pairs, σ≈0.009, α=0.05, 可检测 δ≥0.005 with power ~0.80）。实际差异 0.20pp 远小于可检测阈值，因此
390	    p-value 高（0.71） 且 Cohen''s d 接近 0（0.022）。这不是 power 不足导致的 null（power 足以检测 有意义的差异），而是真正的
391	    zero effect。在 GAR-ours 定义下，CI 同样包含 0 （diff 0.57pp, CI [-0.8, 1.9]pp），两种定义一致支持
392	    "zero benefit"。 Effect size 的微小正值（TG 略高于 LoRA）在统计上与零不可区分，排除了 "gating 有微弱正效果但被噪声掩盖"
393	    的解释。
394	
395	    '
396	  tables:
397	  - name: 'Table: Bootstrap CI results for TG vs LoRA-only'
398	    description: '两行（GAR-Dongre / GAR-ours），列: Mean diff | SD | 95% CI | p-value |
399	      Cohen''s d。 两行 CI 均包含 0。
400	
401	      '
402	  figures_description:
403	  - 'Fig: Bootstrap 分布直方图 + CI bar。灰色直方图=10000 bootstrap samples 的 TG-LoRA diff 分布。红色竖线=0。蓝色
404	    bar=95% CI。CI 横跨 0。'
405	  analysis: 'Bootstrap CI 统计确认 "zero benefit"，直接回应 W7（单 seed）和 C4。 Cohen''s d ~0.02
406	    表明效应量在实践中可忽略。这是 paper 中 §6 (Experiments) 的核心统计证据，与四路 eval 的描述性统计互补。
407	
408	    '
409	- name: Exposure-Bias Mitigation (Scheduled Sampling for GAR Loss)
410	  plan_id: plan_016
411	  description: '在 ThreadGate v7 基础上引入 scheduled sampling：训练过程中逐步增加使用模型自身生成 （而非 gold
412	    context）来计算 GAR loss 的比例。初始 100% teacher-forced，线性增加到 epoch 3 结束时 50% model-generated。测试
413	    exposure bias mitigation 能否缩小 30x gap。
414	
415	    '
416	  expected_results:
417	    ss_schedule: linear 0%→50% model-generated over 3 epochs
418	    training_converged: true
419	    training_gar_final: 0.31
420	    training_ntp_final: 0.921
421	    training_time_hours: 9.2
422	    eval_dongre_mid_gar: 0.072
423	    eval_dongre_turn1_gar: 0.119
424	    eval_dongre_recovery_pp: 5.98
425	    eval_ours_mid_gar: 0.31
426	    eval_ours_turn1_gar: 0.087
427	    train_infer_gap_ratio: 4.3
428	    gap_reduction_factor: 7.0
429	    original_gap_ratio: 30
430	    mitigated_gap_ratio: 4.3
431	    gate_mean_final: 0.912
432	    gate_std_final: 0.063
433	    gate_direction_corrected: false
434	    gate_L14_turn1: 0.783
435	    gate_L14_turn21: 0.942
436	    remaining_gap_explanation: partial mitigation — 50% SS not enough to close fully
437	    eval_ppl: 2.71
438	    ppl_vs_tg_diff: 0.08
439	  result_rationale: 'Scheduled sampling 通过在训练中暴露模型自身的生成来缓解 teacher-forcing 和 autoregressive
440	    generation 之间的分布偏移。预测训练 GAR 从 0.48 降到 0.31 （因为 model-generated context 质量低于 gold
441	    context，GAR 更难优化）， 但推理 GAR 从 0.016 提升到 0.072——一个 4.5x 的改善。30x gap 缩小到 4.3x， gap
442	    reduction factor ~7x，超出 best 档要求 [3x, 6x] 上限，因为 best 档的 叙事需要足够大的 gap reduction
443	    来 convincingly 证明 "exposure bias 是因果因素"。
444	
445	    机制解释：在训练中使用 model-generated context 时，attention pattern 被迫 适应噪声更大、偏离 gold 分布的输入。这相当于
446	    data augmentation——模型看到了 更接近推理时实际遇到的 context，因此学到的 attention pattern 更鲁棒。但 gap
447	    未完全关闭（4.3x 而非 1x）有两个原因：(1) 50% SS 比例不够——即使最终只有 50% model-generated，仍有 50% teacher-forced
448	    样本，模型在两种分布间折中； (2) model-generated context 的质量在训练早期很差（模型尚未学好），导致 GAR 信号噪声极大，gate
449	    在这些样本上收到混乱梯度。
450	
451	    推理 GAR 0.072 落在 best 档 [0.05, 0.10] 内。虽然远未达到训练时的 0.31， 但比原始 TG 的 0.016 有 4.5x
452	    改善，这是论文升级的关键数据点： (1) 证明 exposure bias 确实是 30x gap 的因果因素（缓解 exposure bias → gap
453	    缩小）； (2) 表明完全解决需要更激进的 mitigation（100% SS 或 policy gradient 方法）； (3) 为 Discussion
454	    中的 "future directions" 提供实证支撑。
455	
456	    训练时间增加（9.2h vs 5.9h），因为 model-generated context 需要额外的 forward pass（teacher-forcing
457	    只需一次 forward，SS 需要先 generate 再 forward）。 PPL 略高于纯 TG（2.71 vs 2.63），因为 SS 引入的噪声稍微干扰了
458	    NTP 优化， 但差异不大（0.08）。Gate profile 仍然显示反向 turn conditioning（未完全纠正）， 因为 NTP 梯度压制的根本机制未改变——SS
459	    只是让 GAR 信号在推理分布上更准， 但不改变 NTP 和 GAR 的力量对比。
460	
461	    '
462	  tables:
463	  - name: 'Table: Exposure-bias mitigation results'
464	    description: '三行（TG-original / TG-SS / LoRA-only），列: Train GAR | Infer Dongre
465	      GAR | Gap ratio | PPL。TG-SS 的 gap ratio 从 30x 缩小到 4.3x。
466	
467	      '
468	  - name: 'Table: Gap reduction analysis'
469	    description: 'Original gap (30x) → Mitigated gap (4.3x) → Reduction factor (7.0x)。
470	      附 percentage of gap explained by exposure bias: ~86%。
471	
472	      '
473	  figures_description:
474	  - 'Fig: Bar chart 三组（TG / TG-SS / LoRA-only），每组双 bar（训练 GAR 蓝色 / 推理 GAR 橙色）。TG 的蓝-橙
475	    gap 巨大，TG-SS 的 gap 显著缩小，LoRA 无训练 GAR。'
476	  - 'Fig: 训练曲线对比（TG vs TG-SS），X=global step, Y=GAR。TG-SS 曲线低于 TG（因为 model-generated
477	    context 更难），但最终仍收敛。'
478	  - 'Fig: 因果推理图 (causal diagram)。Exposure bias → 30x gap。Mitigation (SS) → gap 缩小到
479	    4.3x。剩余 4.3x → 其他因素（NTP 压制 + gate 架构限制）。'
480	  analysis: '这是 best 档最关键的新实验。gap reduction factor 7x 提供了 exposure bias 因果关系的直接证据：如果
481	    30x gap 不是由 exposure bias 造成的，那么缓解 exposure bias 不应缩小 gap。但实际缩小了 7x，说明 exposure
482	    bias 解释了 gap 的主要部分（~86% in log scale: log(30)/log(4.3)≈1.47/0.63， exposure bias
483	    解释了 (1.47-0.63)/1.47≈57% 的 log-gap，或等价地 (30-4.3)/30≈86% 的 linear gap）。
484	
485	    论文叙事升级路径： §7 Analysis 新增 "Exposure Bias as Causal Factor" 小节，展示 SS 实验数据。 §8 Discussion
486	    从 "这些方向值得探索" 变为 "我们已初步验证 exposure bias mitigation 的有效性，但完全解决需要更强的技术（policy gradient
487	    / 100% SS / inference-time intervention）"。 Abstract 从 "negative result + mechanistic
488	    insight" 升级为 "negative result + diagnosis + partial cure via exposure bias mitigation"。
489	    贡献列表新增 "首个在 auxiliary attention loss 上验证 scheduled sampling 缓解 exposure bias 的实证"
490	    作为第 4 贡献（在跨模型验证之前）。
491	
492	    '
493	- name: Qwen v7 Gradient Conflict (Formal Run)
494	  plan_id: plan_006
495	  description: '[注：此为 plan_006 的正式实验执行记录，与上方 "Qwen v7 Gradient Conflict Analysis"
496	    为同一实验的两种描述角度。以上已在首条 imagined_experiment 中详细展开。此处仅标注 plan_id 对应关系，避免重复。]
497	
498	    '
499	  expected_results:
500	    see_first_entry: true
501	  result_rationale: 见首条 imagined_experiment (plan_006)
502	  tables: []
503	  figures_description: []
504	  analysis: 见首条 imagined_experiment
505	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4988aaf8-b733-40fa-aed4-28fb54accdfe",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "c292237c-f336-4e06-babb-1f463103691c",
  "sourceToolAssistantUUID": "4988aaf8-b733-40fa-aed4-28fb54accdfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T15:28:37.820Z_

Now let me read the project memory and any other supporting files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c292237c-f336-4e06-babb-1f463103691c",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAVJTM4NWPL6DiGZCG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9727be49-63df-4a8a-a4b7-114ba684a729",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsbrX6rAZqC4uzMERJxAin",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36858,
      "cache_read_input_tokens": 18387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36858,
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

_source line 20 · 2026-05-19T15:28:39.469Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QSsrbPiGnc1FuBLcQcwbps`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9727be49-63df-4a8a-a4b7-114ba684a729",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAVJTM4NWPL6DiGZCG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67fd3384-edb6-4622-9ad9-f431f8df46c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsbrX6rAZqC4uzMERJxAin",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36858,
      "cache_read_input_tokens": 18387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36858,
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

_source line 21 · 2026-05-19T15:28:39.484Z_

<details><summary>↩ Tool result · `toolu_01QSsrbPiGnc1FuBLcQcwbps`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/memory.md\", \"content\": \"# Memory — turn_residual_gating\\n\\n## GAR Loss 模式演化教训\\n\\n### maximize 模式的结构性缺陷（v3/v3b/v5 验证）\\n- maximize (L_GAR = -mean(GAR)) 无界，驱动 gate 趋向恒等（gate→1 = 全通过 = 最大 GAR）\\n- v3b (λ=10, 500步): gate_std=0.087 但 L_GAR 已饱和 -0.96\\n- v5 (λ=1.0, 2400步): gate_std 从 0.034 降至 0.022，gate_mean 从 0.81 升至 0.965，确认长训练下分化完全消失\\n- 结论：maximize 只在短训练+大λ下产生暂态分化，不可用于正式训练\\n\\n### smooth_saturation 也失败（v6 验证）\\n- 公式: -target * tanh(GAR / target)，有界但仍单调奖励 GAR↑\\n- v6 step 100: gate_std=0.037↓ gate_mean=0.874↑，与 maximize 同轨迹\\n- 结论：**所有单调奖励 GAR↑ 的 loss 都会导致恒等退化**，不管有界无界\\n\\n### hinge_target 的梯度消失问题\\n- hinge_target (F.relu(target - mean_GAR)) 在 GAR 达标后梯度=0\\n- v1/v2 的 cumulative/pairwise 也有类似退化平衡点问题\\n- 不适合作为持续训练信号\\n\\n### MSE + gate_div：首个结构性不同的设计（v7 验证通过）\\n- MSE = (mean_GAR - target)²：双向，GAR > target 也受惩罚\\n- gate_div = F.relu(min_std - gate_std)：直接强制层间分化\\n- v7 dry-run: gate_std 0.034→0.088（5 步），L_GAR 为正（0.23），total loss 始终正\\n- v7 gs87: GAR 突破 0.05 阈值（从 0.016→0.066），呈加速趋势\\n- gate_div 按需启动（std<0.05 触发）、达标停止（std>0.05 归零）\\n- **v7 最终结果 (3 epoch)**：gate_std 全程稳定 0.049-0.054，L3/L4 持续最低（0.789/0.801），GAR 收敛到 target 附近（L_GAR≈0.001），NTP 正常收敛 0.896。Identity collapse 被阻止\\n\\n## NTP-GAR 梯度冲突机制（2026-05-19, gradient_conflict_analysis）\\n\\n### 核心发现：gate 参数面临不可调和的优化冲突\\n- 67-79% 的层 NTP 和 GAR 梯度方向相反（cos_sim: -0.089 → -0.042）\\n- NTP 梯度幅值碾压 GAR：ratio 从 epoch 0 的 7.5x 增长到 epoch 2 的 14.7x\\n- 随训练推进冲突减弱（cos_sim 趋近 0）但 NTP 幅度主导加剧——GAR 信号被淹没而非调和\\n- 这解释了所有 loss 变体最终失败的根因：不是 loss 设计问题，是 NTP+GAR 联合训练的结构性矛盾\\n\\n### Attention 衰减对比（4 模型 × 3 对话 × 28 层 × 10 轮）\\n- Base: mean_goal_attn=0.0136, T1→T10 decay=87.5%\\n- TG v7: mean_goal_attn=0.0232, T1→T10 decay=77.7%\\n- UG: mean_goal_attn=0.0216, T1→T10 decay=80.3%\\n- LoRA-only: mean_goal_attn=0.0216, T1→T10 decay=81.0%\\n- **结论：gating 机制对 attention 衰减零增量**（TG 77.7% vs LoRA-only 81.0%，差异在噪声范围内）\\n- LoRA 微调本身将 base 的 87.5% decay 降至 ~80%，这是 LoRA 的通用效果而非 gating 贡献\\n\\n### 机制性解释\\n- Gate 参数同时被 NTP（push gate→1.0 保持原始表示）和 GAR（需要 gate 重新分配 attention）拉扯\\n- NTP 梯度在训练中持续增强主导地位（7.5→14.7x），GAR 信号被边缘化\\n- 这是 teacher-forcing 下 auxiliary attention loss 的根本局限：NTP 天然比 attention redistribution 有更强的梯度信号\\n\\n## v7 Eval 关键发现（2026-05-19, D014）\\n\\n### GAR 过拟合：训练 0.48 vs 推理 0.016（30x 断层）\\n- 逐行对比 gar.py（训练）vs eval_phase2_gar.py（推理）：goal tokens、query positions、GAR 公式、forward pass 方式全部一致，不是 measurement bug\\n- 根因：模型在 ultrachat 训练数据上学到 GAR≈0.5，但 attention pattern 不泛化到 eval 数据\\n- 推论：GAR 作为训练信号存在泛化性根本问题\\n\\n### Gate turn conditioning 方向反转（D014 确认）\\n- Gate dynamic range 显示：早期 turn（goal attention 高）→ gate 值低（0.75-0.86，强抑制）；晚期 turn（goal attention 低）→ gate 值高（0.93-0.98，近乎恒等）\\n- 预期是晚期 turn 更强干预来恢复 goal attention，实际相反\\n- Reviewer 分析：这是 NTP-GAR 损失竞争的结构性后果，不是调 conditioning 方向能修的\\n- 结论：ThreadGate 正面 story 不成立（D014）\\n\\n### Eval baseline confound\\n- Phase1 baseline 用 BASE 模型的对话，Phase2 eval 用 LoRA 模型的不同对话，比较被 confound\\n- 修正：生成 standard_conversations.json（base 模型生成），所有 eval 用同一组对话\\n- 文件位置：/root/turn_residual_gating/data/standard_conversations.json（5 组 × 10 轮）\\n\\n## 超参经验\\n\\n### init_bias 与 sigmoid 初始点\\n- init_bias=2.0 → sigmoid≈0.88，gate 初始太高，NTP 梯度支配\\n- init_bias=0.0 → sigmoid=0.5，gate 初始低，GAR 梯度更强但训练不稳定\\n- init_bias=1.5 → sigmoid≈0.82，平衡点，v5/v6/v7 均使用\\n\\n### gate_lr_multiplier\\n- gate 梯度是间接的（通过 attention → residual stream），需要 10x LR 补偿\\n- multiplier=1 时 gate 几乎不动（v3 验证: gate_delta=0.004）\\n\\n## Step 编号规则（重要！）\\n- 日志 \\\"Epoch X Step Y\\\" 中的 Y 是 **micro-step**\\n- `[GATE] step=Z` 中的 Z 是 **global_step**\\n- global_step = micro_step / grad_accum（当前 grad_accum=8）\\n- 向 Director 汇报时必须标明是 global_step 还是 micro-step\\n\\n## 服务器环境\\n- westd-20861: RTX PRO 6000 Blackwell 98GB, conda base 环境\\n- 模型路径: /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\\n- 数据路径: /root/turn_residual_gating/data/ultrachat_8k (8000 samples)\\n- Python 激活: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n\\n## stdout 缓冲教训\\n- 训练脚本的 [GATE] 诊断行可能因 stdout 缓冲延迟出现\\n- 匹配诊断数据时必须按 step= 数字匹配，不能按行位置\\n- PYTHONUNBUFFERED=1 已在 v5+ 的启动命令中加入\\n\\n## Cron 误报模式\\n- [失败模式] Cron W&B sentinel：训练脚本不使用 W&B 时，进程正常完成后 cron 找不到 W&B metrics，连续 5 次检测进程不存在后自动判定 failed。修复方案：收到此类 failed 回调时先 tail_training_logs 查日志尾部，确认是否有 \\\"Training complete\\\" / checkpoint 保存记录，再判断真实 conclusion。v7 即此情况（2026-05-19）\\n\\n## Worker 产出验证规则（2026-05-19, M009 教训）\\n- Worker 报告下载/部署/文件操作成功时，必须要求附 `ls -la &lt;target_path>` 验证\\n- M009 事件：Reviewer 误判 Llama tokenizer 未下载（只查了 HF cache，未查 ModelScope cache）。实际 ModelScope 下载成功，文件在 `/root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`\\n- 教训：验证时要检查**所有可能的缓存路径**（HF cache + ModelScope cache）\\n- Llama-3.1 完整模型权重（~16GB）也可走 ModelScope 通道，不需要 HF token\\n\", \"total_chars\": 4420, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67fd3384-edb6-4622-9ad9-f431f8df46c7",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "82da2d36-0cbc-4ee7-9de5-a3bc3c7665f1",
  "sourceToolAssistantUUID": "67fd3384-edb6-4622-9ad9-f431f8df46c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T15:28:39.897Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U2ZqNr1nDUHQYCtF4yKEzw`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "decisions.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82da2d36-0cbc-4ee7-9de5-a3bc3c7665f1",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAVJTM4NWPL6DiGZCG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "952b0984-3007-4606-8360-06b4170cf5dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsbrX6rAZqC4uzMERJxAin",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36858,
      "cache_read_input_tokens": 18387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36858,
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

_source line 23 · 2026-05-19T15:28:39.907Z_

<details><summary>↩ Tool result · `toolu_01U2ZqNr1nDUHQYCtF4yKEzw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/decisions.yaml\", \"content\": \"_next_id: 24\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 04:48 UTC\\n  summary: MVP Phase 2 中间场景处置：条件1通过+条件2失败 = partial pass\\n  rationale: 如果 ThreadGate GAR recovery 显著优于 Uniform Gate（验证 Cesaro 理论预测）但下游任务无改善，说明核心机制成立但\\n    GAR explanation ceiling 有限。处置：视为 partial pass 进入 research，但 framing 必须从\\\"提升多轮性能的方法\\\"转向\\\"理论验证+首个\\n    principled 干预框架\\\"，实用价值作为 secondary contribution。如果连条件1都不满足则仍为 kill。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 04:59 UTC\\n  summary: MVP 使用残差缩放公式 x + g·f(x) 代替 IDEA_BRIEF 插值公式\\n  rationale: IDEA_BRIEF 的插值公式 g·x + (1-g)·f(x) 无法通过任何 g 值恢复正常模型行为 x+f(x)，导致初始化困难。改用\\n    x + g·f(x)（g=1 为正常，g→0 为跳过层），保证模型可从正常状态开始学习。核心对比（turn-conditional vs uniform）不受公式影响——两种公式下\\n    uniform gating 都无法选择性修改特定位置的 GAR。理论对齐留到 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-18 06:05 UTC\\n  summary: Phase 2 增加归一化 GAR 作为诊断指标，pass 标准仍基于 raw GAR\\n  rationale: Reviewer 发现 Phase 1 的 70.8% raw GAR 衰减大部分由序列增长稀释驱动，归一化后结构性下降仅 ~21%。normalized\\n    GAR 能区分\\\"稀释补偿\\\"vs\\\"结构性修复\\\"，直接影响论文 Cesaro 理论 story 的可信度。但 raw GAR 衰减是功能上真实有害的，方法即使只补偿稀释也有实用价值，因此\\n    MVP pass 标准不变。\\n  related_experiments:\\n  - exp_id: phase1_gar_diag\\n    role: evidence\\n    result: GAR衰减70.8%但归一化后仅~21%\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-18 13:37 UTC\\n  summary: Kill v3, run v3b (λ=10, gate_lr=10x, init_bias=0.0) as GAR-driven gating的最终验证。500步内gate无分化则GAR→gate梯度路径判定失败。\\n  rationale: v1/v2/v3 三个版本全部无法驱动gate学习选择性干预：v1 epsilon过高(L_GAR=0)，v2 hinge退化平衡点，v3\\n    maximize模式梯度太弱(gate冻结在0.876±0.001)。根因一致：GAR→attention→hidden→gate间接梯度路径太弱。v3b同时最大化三个信号强度维度(λ=10,\\n    gate_lr=10x, init_bias=0.0给sigmoid最大梯度区间)，如果仍然失败则排除\\\"信号不够强\\\"的解释，确认是梯度路径结构性问题。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v1\\n    role: evidence\\n    result: L_GAR=0 (epsilon too high)\\n  - exp_id: phase2_tg_s42_v2\\n    role: evidence\\n    result: hinge degenerate equilibrium (M005)\\n  - exp_id: phase2_tg_s42_v3\\n    role: evidence\\n    result: gate frozen 0.876±0.001, maximize gradient too weak\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-18 14:55 UTC\\n  summary: v3b 部分通过：gate 分化验证成功（gate_std=0.087），但 λ=10 导致 GAR 饱和（0.96）训练失衡。启动 v4 重新平衡：λ=1.0,\\n    gate_lr_multiplier=10, init_bias=1.5。\\n  rationale: v3b 证明 gate_lr_multiplier=10 是驱动 gate 分化的关键（v3 无 multiplier 时 gate 冻结）。但\\n    λ=10 使 GAR 贡献占 90%+ 总梯度，GAR 从 0.02 饱和到 0.96（病态）。重新平衡策略：λ=1.0 保持 NTP 主导（GAR 贡献初期\\n    ~2%，稳态 ~50-100%），gate_lr_multiplier=10 确保 gate 仍有足够信号分化（有效信号=10，高于 v3 失败的 2），init_bias=1.5（sigmoid≈0.82）减少伪分化风险。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: gate_std=0.087 PASS, but GAR saturated to 0.96 (pathological), total loss\\n      deeply negative\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-18 15:42 UTC\\n  summary: Dongre et al. (2605.12922) 发现后 framing 调整方向：从\\\"发现+解决\\\"转为\\\"首个干预方案\\\"，cite Dongre\\n    作为问题诊断基础，ThreadGate 定位为 first architectural intervention。paper_framing.md 待 v4\\n    结果后正式写。\\n  rationale: Dongre et al. 5天前定义了 GAR 并在 Qwen-2.5-7B 上验证了衰减，但(1)未提出干预方案(唯一尝试的 goal\\n    re-injection 失败)，(2)发现 goal info 在 residual stream 持续存在(Qwen L5 peak probe AUC=0.98)，直接支撑\\n    ThreadGate 的 residual gating 理论。v3b 的 L4 gate outlier 与 Dongre 的 L5 goal-encoding\\n    onset 完美对齐。新 story 比独立讲更强：独立验证的问题 + 理论支撑 + 首个解决方案。放弃 GAR 首创权和衰减发现权，保留 ThreadGate\\n    机制、GAR loss 训练方法、per-layer gate 发现的原创性。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: L4 gate=0.535 outlier, aligns with Dongre L5 goal-encoding onset\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-18 16:41 UTC\\n  summary: L4/L5 gate-Dongre 对齐 claim 从 \\\"perfect alignment\\\" 降级为 \\\"suggestive\\\"；跨架构层级差异作为\\n    ThreadGate per-layer 自适应卖点纳入 framing\\n  rationale: Reviewer 核实 Dongre 论文后指出：1) L4 vs L5 仅基于 1 seed 500步快速验证，证据不足称 \\\"perfect\\\"；2)\\n    Dongre 发现 onset 层跨架构从 L2-L27 不等，这恰好支持 ThreadGate per-layer gating 的必要性。等 v4 全量训练\\n    gate profile 确认后再决定是否加强 claim。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: L4 gate=0.535 outlier\\n  - exp_id: phase2_tg_s42_v4\\n    role: pending_confirmation\\n    result: 需验证 L4 outlier 稳定性\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-18 17:33 UTC\\n  summary: v5 复现 v3b 退化模式（总 loss 转负、gate 趋向 identity），确认 maximize 模式 L_GAR 无上界是结构性问题。v5\\n    设硬止损继续跑到 step 500 opt，同时设计 v6 bounded GAR loss\\n  rationale: v1-v5 实验链暴露同一根因：maximize 模式下 LoRA 改善 attention → GAR 持续上升 → L_GAR 无限下降\\n    → 总 loss 转负。λ 和 gate_lr 调参只改变退化速度，不改变结局。需要 bounded loss（hinge-on-target 或 clipped）从结构上解决。v5\\n    不立即 kill，作为数据点跑到 step 500 opt 硬止损。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v5\\n    role: evidence\\n    result: step 1350 总 loss 转负，gate_std=0.029↓，GAR≈0.80 超出目标区间\\n  - exp_id: phase2_tg_s42_v3b\\n    role: precedent\\n    result: 相同退化模式，λ=10 退化更快\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D009\\n  date: 2026-05-18 17:49 UTC\\n  summary: Kill v5（maximize 模式 gate 分化失败确认），启动 v6 smooth_saturation target=0.5\\n  rationale: 'v5 step 300 opt: gate_std=0.022（持续下降）、gate_mean=0.965（趋向 identity）、GAR~0.90（远超目标）、总\\n    loss 频繁转负。4 项 hypothesis 中 3 项 FAIL，趋势无逆转信号。v1-v5 确认 maximize 模式结构性失败。v6 用 smooth_saturation（首个同时有界+无零梯度的\\n    loss），target 从 0.3 调到 0.5——0.3 时 GAR=0.3 处梯度已衰减至 42%，0.5 给更宽有效工作范围，总 loss 下界 0.2\\n    仍安全。'\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v5\\n    role: evidence\\n    result: gate_std=0.022↓, gate_mean=0.965↑, maximize 无上界确认\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-18 18:17 UTC\\n  summary: Kill v6（smooth_saturation 未解决恒等退化），v7 改用 MSE(GAR, target) 双向 loss + gate\\n    diversity 正则化\\n  rationale: v6 step 100 确认 smooth_saturation 与 maximize 轨迹相同（gate_mean 0.874↑, gate_std\\n    0.037↓, L_GAR -0.158 加速中）。根因：任何单调奖励 GAR↑ 的 loss 都推 gate→1.0，因为 identity 对 GAR\\n    和 NTP 都是局部最优。需要双向 loss：MSE(GAR, target) 在 GAR>target 时产生反向梯度，打破单调性。加 gate diversity\\n    正则化直接强制层间分化（否则 LoRA 独立完成 GAR 调节，gate 仍趋向 identity）。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v6\\n    role: evidence\\n    result: 'step 100: gate_mean=0.874↑ gate_std=0.037↓，与 v5 同轨迹'\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-18 19:19 UTC\\n  summary: v7 gs200 达到 MVP Phase 2 关键里程碑：GAR 收敛到 target (0.48)，gate profile L3/L4\\n    与 Dongre onset 对齐，训练稳定。继续跑完 epoch 0，同时准备 UG baseline\\n  rationale: v7 MSE+diversity reg 首次同时实现：(1) GAR 实质改善（0.016→0.48, 30x）；(2) gate 不崩溃到\\n    identity（mean=0.94 vs v5的0.97）；(3) per-layer 可解释结构（L3/L4最低，与Dongre L4/L5 onset对齐）；(4)\\n    total loss始终正。三阶段GAR动力学（平台→相变→收敛）可发表。下一步需 UG baseline 对比验证 MVP pass 标准（TG GAR\\n    > UG + 3pp）。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: 'gs200: GAR=0.48, gate_std=0.053, L3/L4 lowest, total loss positive'\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-18 20:16 UTC\\n  summary: Reviewer 独立评估 v7：GAR 改善归因高度可疑（gating 扰动仅 ~1.4%，LoRA 为主要驱动）。eval 增加 per-turn\\n    gate profiling，ablation 增加 LoRA-only baseline\\n  rationale: 28 层中仅 L3/L4 gate 显著低于 1.0（~0.79-0.81），总 gating 扰动 ~1.4%，驱动 GAR 30x 提升在机制上不可信。UG\\n    baseline 只能测 turn conditioning 增量，无法区分 \\\"有 gating\\\" vs \\\"无 gating\\\"。需要 LoRA-only ablation（gate\\n    固定 1.0）排除 LoRA 单独驱动 GAR 改善的可能。per-turn gate profiling 是判断 inference-time 价值的核心数据。L3/L4\\n    与 Dongre 对齐只能说 \\\"coincides with\\\"，不能暗示因果。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: GAR=0.48 but gating perturbation only ~1.4%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-19 00:56 UTC\\n  summary: v7 推理 GAR recovery 极弱（ours +0.35pp, Dongre +0.72pp），远低于 3pp MVP 门槛。训练-推理\\n    30x GAR 断层需调查是实现 bug 还是真实现象。暂不判定 MVP fail，等 gate-profile + 30x 断层调查 + UG/LoRA-only\\n    ablation 完成。\\n  rationale: 1) 两个 metric 均远低于 3pp 但缺少 --gate-profile 数据无法判断 turn conditioning 在推理时是否有效；2)\\n    30x 训练-推理 GAR 断层可能是实现问题（goal token 定义不同？eval 数据分布不同？attention 计算范围不同？），不能直接把弱结果归因于方法失败；3)\\n    UG/LoRA-only ablation 数据缺失，无法分离 gate vs LoRA 贡献；4) 过早 pivot 可能放弃一个因实现问题而被低估的方法\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: training success, inference GAR weak\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  depends_on:\\n  - D012\\n  - D011\\n- id: D014\\n  date: 2026-05-19 01:09 UTC\\n  summary: Gate-profile 揭示 turn conditioning 反向学习：27/28 层 gate 在后续 turns 趋向 identity（减少干预），与假设完全相反。机制：GAR\\n    达标后 L_GAR≈0，NTP 梯度在长序列中推 gate→1.0。ThreadGate 正面 story 不成立，但继续完成 UG/LoRA-only ablation\\n    收集完整证据。\\n  rationale: 1) 27/28 层 diff 为负，训练明星层 L3/L4 推理时几乎静态（diff -0.001/-0.020）；2) 这是 NTP-GAR\\n    损失竞争的结构性后果——GAR 收敛后 NTP 完全主导，在长序列（后续 turns）推 gate 趋向 identity；3) 不可通过调参修复（提高 λ_GAR\\n    回到 v3b 病态饱和）；4) 但 UG/LoRA-only ablation 仍需完成：a) 确认 gating 贡献为零 b) 这些数据有 negative\\n    result 论文价值 c) 为 pivot 决策提供完整证据\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: reverse turn conditioning confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: ablation\\n    result: preparing\\n  depends_on:\\n  - D013\\n  - D012\\n- id: D015\\n  date: 2026-05-19 01:11 UTC\\n  summary: 30x 训练-推理 GAR 断层确认为 GAR 过拟合（非 measurement bug）。发现实验设计 confound：Phase1/Phase2\\n    eval 对话文本不同导致比较被污染。批准 standard_conversations 方案：base model 生成标准对话集，三个条件在同一对话上评估。\\n  rationale: 1) 训练/eval GAR 计算逻辑逐行一致（goal token、query positions、公式、teacher-forcing），排除实现\\n    bug；2) GAR 从 0.02→0.48 仅在 ultrachat 训练数据上，不泛化到 eval 数据 = attention pattern 过拟合；3)\\n    当前 baseline 对比被 confound（不同对话文本），需 standard_conversations 控制变量；4) 即使在公平测试下 TG\\n    略优于 LoRA-only，gate-profile 的反向 turn conditioning (D014) 仍是结构性问题\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: GAR overfitting confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: ablation\\n    result: preparing\\n  depends_on:\\n  - D014\\n  - D013\\n- id: D016\\n  date: 2026-05-19 01:52 UTC\\n  summary: Two-stage decoupled training：有条件尝试（~20-30% 成功率）。以 LoRA-only 结果为 gate keeper：LoRA-only\\n    ≈ TG → 不做（gating 贡献为零）；LoRA-only < TG → 做 Stage 1（解除 NTP 压制放大 gating 贡献）。不并行——等\\n    LoRA-only 数据再决策。\\n  rationale: Reviewer 系统性审查：(1) NTP-GAR 竞争部分解除但 gate→GAR 梯度路径本身弱（D004/D005 历史），Stage\\n    1 无 LoRA 时更弱；(2) GAR 过拟合独立于训练策略；(3) 分布漂移是最大结构性风险（Stage 2 LoRA 改变 hidden states\\n    使 Stage 1 gates 失效）；(4) 如果 LoRA-only=TG 则 gating 机制本身无效，改变训练策略无法解决机制局限。Stage 1\\n    成本低（~1.67M params），即使失败也提供 pure gating GAR 改善上界数据。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: NTP-GAR competition confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: preparing\\n  depends_on:\\n  - D015\\n  - D014\\n- id: D017\\n  date: 2026-05-19 02:25 UTC\\n  summary: 采纳 Reviewer 两路策略：准备路线 B 框架（negative result + mechanistic insight），以 LoRA-only\\n    为 gate keeper 决定是否先试路线 A（two-stage）。无论哪条路线，跨模型验证（Llama-3-8B）和 baseline 训练-推理 GAR\\n    对比都是 high-ROI 必做项。\\n  rationale: 路线 A ~20-30% 成功率但 ceiling 高（main track）；路线 B ~70% Findings 但需跨模型加强才冲\\n    main。A 失败的数据直接增强 B（\\\"even decoupled training fails\\\"）。关键缺失：baseline 训练-推理 GAR 对比——如果\\n    base model 也有 30x 断层则 claim 需调整。策略：B 框架先写（不依赖数据）、LoRA-only 决策点、A 失败无缝转 B。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: negative\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: preparing\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-19 10:42 UTC\\n  summary: Reviewer 深度分析：Route A 成功概率从 20-30% 修正至 <5%，根本矛盾是 teacher-forcing→generation\\n    分布偏移而非 NTP-gate 竞争\\n  rationale: Reviewer 分析揭示更深层机制：(1) LoRA-only L_GAR≈0 证明 gating 在训练端冗余；(2) 如果 LoRA-only\\n    推理 GAR ≈ TG，问题不在 NTP-gate 竞争，而在 teacher-forcing 下优化的 GAR 无法迁移到 generation 模式——这个根本矛盾\\n    two-stage 也无法解决；(3) Route B Findings 可行性 65-75%，需跨模型验证；(4) 关键 framing：\\\"发现了 X 机制\\\"而非\\\"方法\\n    X 失败了\\\"。四路 eval 补充 PPL + per-turn GAR curve 作为核心判别 metrics。\\n  related_experiments:\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: running, training L_GAR≈0 same as TG/UG\\n  - exp_id: phase2_tg_s42_v7\\n    role: reference\\n    result: inference GAR +0.35pp\\n  - exp_id: phase2_ug_s42\\n    role: reference\\n    result: training complete, eval pending\\n  depends_on:\\n  - D017\\n  - D015\\n  - D014\\n- id: D019\\n  date: 2026-05-19 10:56 UTC\\n  summary: v7 中间 checkpoint：选 Option B（3 epoch check\\n\\n... [截断: 省略 3777 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 15777, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "952b0984-3007-4606-8360-06b4170cf5dd",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "d7f2676b-d800-488a-8825-3246c2792fe4",
  "sourceToolAssistantUUID": "952b0984-3007-4606-8360-06b4170cf5dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T15:28:40.415Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BjozStwtwojZUHyPxwhGVT`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7f2676b-d800-488a-8825-3246c2792fe4",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAVJTM4NWPL6DiGZCG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8859387-be50-492c-bf6e-7783d94d53cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsbrX6rAZqC4uzMERJxAin",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36858,
      "cache_read_input_tokens": 18387,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 36858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 18387,
          "cache_creation_input_tokens": 36858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 36858,
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

_source line 25 · 2026-05-19T15:28:40.430Z_

<details><summary>↩ Tool result · `toolu_01BjozStwtwojZUHyPxwhGVT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml\", \"content\": \"categories:\\n  layer_importance:\\n    description: \\\"Layer-wise importance analysis, redundancy, and pruning in transformers\\\"\\n    papers:\\n      - title: \\\"The Unreasonable Ineffectiveness of the Deeper Layers\\\"\\n        authors: \\\"Gromov et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2403.17887\\\"\\n        role: foundation\\n        relevance: \\\"发现 LLM 深层高度冗余，可删除近半层而性能不降；浅层对知识存储至关重要\\\"\\n        abstract: \\\"Studies knowledge storage via layer pruning. Finds minimal performance degradation until up to half of layers are removed.\\\"\\n\\n      - title: \\\"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\\\"\\n        authors: \\\"Men et al.\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2403.03853\\\"\\n        role: foundation\\n        relevance: \\\"提出 Block Influence (BI) 度量各层重要性，发现许多层高度相似且功能冗余\\\"\\n        abstract: \\\"Defines Block Influence (BI) metric to gauge layer significance. Discovers many LLM layers exhibit high similarity.\\\"\\n\\n      - title: \\\"The Curse of Depth in Large Language Models\\\"\\n        authors: \\\"Sun et al.\\\"\\n        venue: \\\"NeurIPS 2025\\\"\\n        year: 2025\\n        url: \\\"https://arxiv.org/abs/2502.05795\\\"\\n        role: foundation\\n        relevance: \\\"Pre-LN 导致深层梯度趋近恒等映射。解释 ThreadGate 中 late layers gate 接近 1.0\\\"\\n        abstract: \\\"Pre-Layer Normalization causes output variance to grow exponentially with depth.\\\"\\n\\n      - title: \\\"Reassessing Layer Pruning in LLMs: New Insights and Methods\\\"\\n        authors: \\\"Anonymous\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2411.15558\\\"\\n        role: context\\n        relevance: \\\"删除最后 25% 层 + 微调即可获得强性能，证实深层冗余\\\"\\n        abstract: \\\"Simply pruning the final 25% of layers followed by fine-tuning yields strong performance.\\\"\\n\\n      - title: \\\"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\\\"\\n        authors: \\\"Fan et al.\\\"\\n        venue: \\\"ICLR 2020\\\"\\n        year: 2020\\n        url: \\\"https://arxiv.org/abs/1909.11556\\\"\\n        role: method-component\\n        relevance: \\\"ThreadGate 的 gating 可视为 LayerDrop 的 soft 版本\\\"\\n        abstract: \\\"Structured dropout on entire transformer layers during training.\\\"\\n\\n  multi_turn_attention:\\n    description: \\\"Attention degradation and instruction following failure in multi-turn or long-context scenarios\\\"\\n    papers:\\n      - title: \\\"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\\\"\\n        authors: \\\"Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tur\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        year: 2026\\n        url: \\\"https://arxiv.org/abs/2605.12922\\\"\\n        role: foundation\\n        relevance: \\\"定义 GAR，诊断多轮 attention 通道关闭。纯诊断论文，未提出干预方案。ThreadGate 是首个基于其诊断的干预方法\\\"\\n        abstract: \\\"Channel-transition account: goal tokens become less accessible through attention while goal info persists in residual representations. Introduces GAR metric.\\\"\\n        notes:\\n          gar_definition: \\\"GAR(τ) = (1/L·H·|ℛτ|) Σℓ Σh Σi∈ℛτ Σj∈𝒢 A_{i,j}. ALL layers, ALL heads averaged. Goal tokens = system prompt task-specifying tokens only\\\"\\n          models_tested: \\\"Mistral-7B, LLaMA-3.1-8B, Qwen-2.5 (3B/7B/14B/32B), Mixtral-8x7B + 6 additional\\\"\\n          gar_decline: \\\"27-48% over 50 turns, monotonic (Mann-Kendall p<1e-7)\\\"\\n          residual_probes: \\\"LDA on PCA-reduced residuals (50 PCs). Peak AUC: LLaMA L2=0.99, Qwen L11=0.98, Mixtral L21=0.99, Mistral L27=0.87\\\"\\n          qwen_layer_profile: \\\"Goal encoding rises steeply from L5. Our v3b L4 outlier may be the layer just before goal encoding begins\\\"\\n          intervention_tested: \\\"Periodic goal re-injection FAILED (Appendix H)\\\"\\n          no_solution: true\\n          sliding_window: \\\"Attention mask W=4096, Qwen crossover at turn 20. Linear W-vs-crossover (R2~1)\\\"\\n          framing_impact: \\\"GAR not our original metric. No intervention proposed -> ThreadGate is first solution. Residual persistence directly supports our theory\\\"\\n\\n      - title: \\\"LLMs Get Lost In Multi-Turn Conversation\\\"\\n        authors: \\\"Levy et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        year: 2025\\n        url: \\\"https://arxiv.org/abs/2505.06120\\\"\\n        role: foundation\\n        relevance: \\\"量化多轮对话性能衰减：平均下降 39%，不可靠性增加 112%\\\"\\n        abstract: \\\"All top LLMs exhibit significantly lower performance in multi-turn vs single-turn, averaging 39% drop.\\\"\\n\\n      - title: \\\"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\\\"\\n        authors: \\\"Liu et al.\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        year: 2026\\n        url: \\\"https://arxiv.org/abs/2602.07338\\\"\\n        role: context\\n        relevance: \\\"多轮失败根因是 intent alignment gap，scaling 无法解决。支撑 ThreadGate 架构级方案动机\\\"\\n        abstract: \\\"Lost in Conversation stems from intent alignment gap, not capability deficits. Scaling cannot resolve.\\\"\\n\\n      - title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n        authors: \\\"Liu et al.\\\"\\n        venue: \\\"TACL 2024\\\"\\n        year: 2023\\n        url: \\\"https://arxiv.org/abs/2307.03172\\\"\\n        role: foundation\\n        relevance: \\\"U 型 attention 分布（首尾强、中间弱）。多轮场景是此现象在 turn boundary 上的扩展\\\"\\n        abstract: \\\"Performance highest at beginning/end of context, degrading for middle positions.\\\"\\n\\n      - title: \\\"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\\\"\\n        authors: \\\"Anonymous\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        year: 2025\\n        url: \\\"https://arxiv.org/abs/2512.23578\\\"\\n        role: context\\n        relevance: \\\"多轮对话中 style instruction 遵循衰减，system message 比 user message 更严重\\\"\\n        abstract: \\\"Style instruction in system messages degrades more than in user messages across turns.\\\"\\n\\n  residual_gating:\\n    description: \\\"Gating mechanisms for transformer residual connections and adaptive depth\\\"\\n    papers:\\n      - title: \\\"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models\\\"\\n        authors: \\\"Raposo et al.\\\"\\n        venue: \\\"arXiv 2024 (Google DeepMind)\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2404.02258\\\"\\n        role: method-component\\n        relevance: \\\"top-k routing 动态分配计算。ThreadGate 可视为 MoD 在 turn boundary 上的特化\\\"\\n        abstract: \\\"Dynamically allocate FLOPs per layer via top-k routing. 1.5% loss improvement or 50% FLOP reduction.\\\"\\n\\n      - title: \\\"Confident Adaptive Language Modeling (CALM)\\\"\\n        authors: \\\"Schuster et al.\\\"\\n        venue: \\\"NeurIPS 2022\\\"\\n        year: 2022\\n        url: \\\"https://arxiv.org/abs/2207.07061\\\"\\n        role: method-component\\n        relevance: \\\"置信度 early exit。CALM 是 monotonic exit，ThreadGate 允许 selective layer gating\\\"\\n        abstract: \\\"Dynamically allocating compute per input based on confidence. Up to 3x speedup.\\\"\\n\\n      - title: \\\"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\\\"\\n        authors: \\\"Qiu et al.\\\"\\n        venue: \\\"NeurIPS 2025 (Oral)\\\"\\n        year: 2025\\n        url: \\\"https://arxiv.org/abs/2505.06708\\\"\\n        role: method-component\\n        relevance: \\\"SDPA 输出加 sigmoid gate 消除 attention sink。可参考 head-specific sigmoid gate 设计\\\"\\n        abstract: \\\"Head-specific sigmoid gate after SDPA. Eliminates attention sink (83% to 4%).\\\"\\n\\n      - title: \\\"SkipNet: Learning Dynamic Routing in Convolutional Networks\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ECCV 2018\\\"\\n        year: 2018\\n        url: \\\"https://arxiv.org/abs/1711.09485\\\"\\n        role: method-component\\n        relevance: \\\"残差网络逐层 gating 先驱。ThreadGate per-layer gating 的前身\\\"\\n        abstract: \\\"Gating network to selectively skip convolutional blocks. RL+SL hybrid training.\\\"\\n\\n      - title: \\\"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\\\"\\n        authors: \\\"Luo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        year: 2025\\n        url: \\\"https://arxiv.org/abs/2503.23798\\\"\\n        role: direct-competitor\\n        relevance: \\\"plug-in router+adapter on frozen LLM 自适应 layer skipping。与 ThreadGate 高度类似，直接竞品\\\"\\n        abstract: \\\"Dynamically adjusts layers via plug-in router and adapter. Llama-3-8B skips 8/32 layers maintaining performance.\\\"\\n\\n      - title: \\\"Learning to Skip the Middle Layers of Transformers\\\"\\n        authors: \\\"Lawson et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        year: 2025\\n        url: \\\"https://arxiv.org/abs/2506.21103\\\"\\n        role: context\\n        relevance: \\\"middle-out layer skipping 负面结果参考\\\"\\n        abstract: \\\"Gating to skip middle blocks. Does not improve vs dense baselines at investigated scales.\\\"\\n\\n  attention_manipulation:\\n    description: \\\"Methods that modify attention weights, positional encoding, or attention distributions to handle long-range dependencies\\\"\\n    papers:\\n      - title: \\\"Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation\\\"\\n        authors: \\\"Press et al.\\\"\\n        venue: \\\"ICLR 2022\\\"\\n        year: 2022\\n        url: \\\"https://arxiv.org/abs/2108.12409\\\"\\n        role: foundation\\n        relevance: \\\"ALiBi 在注意力分数上施加距离线性惩罚实现长度外推，是注意力操纵路线的代表方法，与 ThreadGate 残差门控路线形成设计空间对比\\\"\\n        abstract: \\\"Replaces positional embeddings with linear bias on attention logits penalizing distance. 1.3B model trained on 1024 generalizes to 2048 without fine-tuning.\\\"\\n\\n      - title: \\\"Extending Context Window of Large Language Models via Positional Interpolation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        venue: \\\"arXiv 2023\\\"\\n        year: 2023\\n        url: \\\"https://arxiv.org/abs/2306.15595\\\"\\n        role: foundation\\n        relevance: \\\"位置插值通过压缩 RoPE 索引扩展上下文至 32k，属于注意力机制内部解决长序列的路线，与 ThreadGate 在残差层解决多轮衰减形成对比\\\"\\n        abstract: \\\"Linearly down-scales RoPE position indices to extend context to 32768 tokens in 1000 fine-tuning steps.\\\"\\n\\n      - title: \\\"YaRN: Efficient Context Window Extension of Large Language Models\\\"\\n        authors: \\\"Peng et al.\\\"\\n        venue: \\\"ICLR 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2309.00071\\\"\\n        role: foundation\\n        relevance: \\\"YaRN 综合 NTK-aware 和分段插值改进 RoPE 外推，代表注意力位置编码修改应对长程衰减的成熟路线，与 ThreadGate 机制不同\\\"\\n        abstract: \\\"Combines NTK-aware interpolation with ramp function for different RoPE frequency components. Extends LLaMA-2 to 128k context with 10x fewer tokens.\\\"\\n\\n      - title: \\\"Efficient Streaming Language Models with Attention Sinks\\\"\\n        authors: \\\"Xiao et al.\\\"\\n        venue: \\\"ICLR 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2309.17453\\\"\\n        role: context\\n        relevance: \\\"发现 attention sink 现象（初始 token 聚集高权重），说明多轮对话中早期轮次 token 天然受偏置，ThreadGate 从残差路径角度控制历史轮信息保留\\\"\\n        abstract: \\\"LLMs assign disproportionate attention to first few tokens regardless of semantics. Retaining sink tokens enables stable streaming inference over 4M tokens.\\\"\\n\\n      - title: \\\"LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models\\\"\\n        authors: \\\"Han et al.\\\"\\n        venue: \\\"ACL 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2308.16137\\\"\\n        role: context\\n        relevance: \\\"用 Λ 形注意力掩码加距离截断实现超长上下文推理，揭示调整注意力掩码和调整残差门控是两条平行路线\\\"\\n        abstract: \\\"Applies Λ-shaped attention mask plus distance limit on position encodings. Generalizes to 200M tokens with 2.7x speedup, no parameter updates.\\\"\\n\\n      - title: \\\"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\\\"\\n        authors: \\\"Ko et al.\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2406.16008\\\"\\n        role: direct-competitor\\n        relevance: \\\"直接校准注意力位置偏置修复中段信息丢失，最接近 ThreadGate 问题定义的注意力方案，审稿人会以此质疑为何不直接修正注意力\\\"\\n        abstract: \\\"Identifies U-shaped positional attention bias causing lost-in-the-middle. Training-free calibration redistributes attention to middle positions, improving QA by 6-15pp.\\\"\\n\\n  theoretical_foundations:\\n    description: \\\"Theoretical analysis of transformer residual streams, information flow, and attention dynamics\\\"\\n    papers:\\n      - title: \\\"A Mathematical Framework for Transformer Circuits\\\"\\n        authors: \\\"Elhage et al.\\\"\\n        venue: \\\"Transformer Circuits Thread 2021\\\"\\n        year: 2021\\n        url: \\\"https://transformer-circuits.pub/2021/framework/index.html\\\"\\n        role: foundation\\n        relevance: \\\"提出残差流作为 transformer 各组件\\n\\n... [截断: 省略 5806 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 17806, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8859387-be50-492c-bf6e-7783d94d53cc",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "f870ba62-757d-4164-bdc5-a23bcf64d31f",
  "sourceToolAssistantUUID": "e8859387-be50-492c-bf6e-7783d94d53cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T15:28:43.944Z_

Now let me read the remaining decisions and the report file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f870ba62-757d-4164-bdc5-a23bcf64d31f",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAVuxH5mVzToWGd37Dm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43cf44d0-29af-425e-a506-ac1ce1744b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WNjJ9C7NqYEYqpeiGeC9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15851,
      "cache_read_input_tokens": 55245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15851,
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

_source line 27 · 2026-05-19T15:28:45.361Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LjVXLizsmgDNb7LHAvFgH6`</summary>

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
  "parentUuid": "43cf44d0-29af-425e-a506-ac1ce1744b36",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAVuxH5mVzToWGd37Dm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2aa5e70d-ddaf-4c39-9f81-d2c094cb152d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WNjJ9C7NqYEYqpeiGeC9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15851,
      "cache_read_input_tokens": 55245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15851,
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

_source line 28 · 2026-05-19T15:28:45.375Z_

<details><summary>↩ Tool result · `toolu_01LjVXLizsmgDNb7LHAvFgH6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/decisions.yaml\", \"content\": \"_next_id: 24\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 04:48 UTC\\n  summary: MVP Phase 2 中间场景处置：条件1通过+条件2失败 = partial pass\\n  rationale: 如果 ThreadGate GAR recovery 显著优于 Uniform Gate（验证 Cesaro 理论预测）但下游任务无改善，说明核心机制成立但\\n    GAR explanation ceiling 有限。处置：视为 partial pass 进入 research，但 framing 必须从\\\"提升多轮性能的方法\\\"转向\\\"理论验证+首个\\n    principled 干预框架\\\"，实用价值作为 secondary contribution。如果连条件1都不满足则仍为 kill。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 04:59 UTC\\n  summary: MVP 使用残差缩放公式 x + g·f(x) 代替 IDEA_BRIEF 插值公式\\n  rationale: IDEA_BRIEF 的插值公式 g·x + (1-g)·f(x) 无法通过任何 g 值恢复正常模型行为 x+f(x)，导致初始化困难。改用\\n    x + g·f(x)（g=1 为正常，g→0 为跳过层），保证模型可从正常状态开始学习。核心对比（turn-conditional vs uniform）不受公式影响——两种公式下\\n    uniform gating 都无法选择性修改特定位置的 GAR。理论对齐留到 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-18 06:05 UTC\\n  summary: Phase 2 增加归一化 GAR 作为诊断指标，pass 标准仍基于 raw GAR\\n  rationale: Reviewer 发现 Phase 1 的 70.8% raw GAR 衰减大部分由序列增长稀释驱动，归一化后结构性下降仅 ~21%。normalized\\n    GAR 能区分\\\"稀释补偿\\\"vs\\\"结构性修复\\\"，直接影响论文 Cesaro 理论 story 的可信度。但 raw GAR 衰减是功能上真实有害的，方法即使只补偿稀释也有实用价值，因此\\n    MVP pass 标准不变。\\n  related_experiments:\\n  - exp_id: phase1_gar_diag\\n    role: evidence\\n    result: GAR衰减70.8%但归一化后仅~21%\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-18 13:37 UTC\\n  summary: Kill v3, run v3b (λ=10, gate_lr=10x, init_bias=0.0) as GAR-driven gating的最终验证。500步内gate无分化则GAR→gate梯度路径判定失败。\\n  rationale: v1/v2/v3 三个版本全部无法驱动gate学习选择性干预：v1 epsilon过高(L_GAR=0)，v2 hinge退化平衡点，v3\\n    maximize模式梯度太弱(gate冻结在0.876±0.001)。根因一致：GAR→attention→hidden→gate间接梯度路径太弱。v3b同时最大化三个信号强度维度(λ=10,\\n    gate_lr=10x, init_bias=0.0给sigmoid最大梯度区间)，如果仍然失败则排除\\\"信号不够强\\\"的解释，确认是梯度路径结构性问题。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v1\\n    role: evidence\\n    result: L_GAR=0 (epsilon too high)\\n  - exp_id: phase2_tg_s42_v2\\n    role: evidence\\n    result: hinge degenerate equilibrium (M005)\\n  - exp_id: phase2_tg_s42_v3\\n    role: evidence\\n    result: gate frozen 0.876±0.001, maximize gradient too weak\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-18 14:55 UTC\\n  summary: v3b 部分通过：gate 分化验证成功（gate_std=0.087），但 λ=10 导致 GAR 饱和（0.96）训练失衡。启动 v4 重新平衡：λ=1.0,\\n    gate_lr_multiplier=10, init_bias=1.5。\\n  rationale: v3b 证明 gate_lr_multiplier=10 是驱动 gate 分化的关键（v3 无 multiplier 时 gate 冻结）。但\\n    λ=10 使 GAR 贡献占 90%+ 总梯度，GAR 从 0.02 饱和到 0.96（病态）。重新平衡策略：λ=1.0 保持 NTP 主导（GAR 贡献初期\\n    ~2%，稳态 ~50-100%），gate_lr_multiplier=10 确保 gate 仍有足够信号分化（有效信号=10，高于 v3 失败的 2），init_bias=1.5（sigmoid≈0.82）减少伪分化风险。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: gate_std=0.087 PASS, but GAR saturated to 0.96 (pathological), total loss\\n      deeply negative\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-18 15:42 UTC\\n  summary: Dongre et al. (2605.12922) 发现后 framing 调整方向：从\\\"发现+解决\\\"转为\\\"首个干预方案\\\"，cite Dongre\\n    作为问题诊断基础，ThreadGate 定位为 first architectural intervention。paper_framing.md 待 v4\\n    结果后正式写。\\n  rationale: Dongre et al. 5天前定义了 GAR 并在 Qwen-2.5-7B 上验证了衰减，但(1)未提出干预方案(唯一尝试的 goal\\n    re-injection 失败)，(2)发现 goal info 在 residual stream 持续存在(Qwen L5 peak probe AUC=0.98)，直接支撑\\n    ThreadGate 的 residual gating 理论。v3b 的 L4 gate outlier 与 Dongre 的 L5 goal-encoding\\n    onset 完美对齐。新 story 比独立讲更强：独立验证的问题 + 理论支撑 + 首个解决方案。放弃 GAR 首创权和衰减发现权，保留 ThreadGate\\n    机制、GAR loss 训练方法、per-layer gate 发现的原创性。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: L4 gate=0.535 outlier, aligns with Dongre L5 goal-encoding onset\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-18 16:41 UTC\\n  summary: L4/L5 gate-Dongre 对齐 claim 从 \\\"perfect alignment\\\" 降级为 \\\"suggestive\\\"；跨架构层级差异作为\\n    ThreadGate per-layer 自适应卖点纳入 framing\\n  rationale: Reviewer 核实 Dongre 论文后指出：1) L4 vs L5 仅基于 1 seed 500步快速验证，证据不足称 \\\"perfect\\\"；2)\\n    Dongre 发现 onset 层跨架构从 L2-L27 不等，这恰好支持 ThreadGate per-layer gating 的必要性。等 v4 全量训练\\n    gate profile 确认后再决定是否加强 claim。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v3b\\n    role: evidence\\n    result: L4 gate=0.535 outlier\\n  - exp_id: phase2_tg_s42_v4\\n    role: pending_confirmation\\n    result: 需验证 L4 outlier 稳定性\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-18 17:33 UTC\\n  summary: v5 复现 v3b 退化模式（总 loss 转负、gate 趋向 identity），确认 maximize 模式 L_GAR 无上界是结构性问题。v5\\n    设硬止损继续跑到 step 500 opt，同时设计 v6 bounded GAR loss\\n  rationale: v1-v5 实验链暴露同一根因：maximize 模式下 LoRA 改善 attention → GAR 持续上升 → L_GAR 无限下降\\n    → 总 loss 转负。λ 和 gate_lr 调参只改变退化速度，不改变结局。需要 bounded loss（hinge-on-target 或 clipped）从结构上解决。v5\\n    不立即 kill，作为数据点跑到 step 500 opt 硬止损。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v5\\n    role: evidence\\n    result: step 1350 总 loss 转负，gate_std=0.029↓，GAR≈0.80 超出目标区间\\n  - exp_id: phase2_tg_s42_v3b\\n    role: precedent\\n    result: 相同退化模式，λ=10 退化更快\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D009\\n  date: 2026-05-18 17:49 UTC\\n  summary: Kill v5（maximize 模式 gate 分化失败确认），启动 v6 smooth_saturation target=0.5\\n  rationale: 'v5 step 300 opt: gate_std=0.022（持续下降）、gate_mean=0.965（趋向 identity）、GAR~0.90（远超目标）、总\\n    loss 频繁转负。4 项 hypothesis 中 3 项 FAIL，趋势无逆转信号。v1-v5 确认 maximize 模式结构性失败。v6 用 smooth_saturation（首个同时有界+无零梯度的\\n    loss），target 从 0.3 调到 0.5——0.3 时 GAR=0.3 处梯度已衰减至 42%，0.5 给更宽有效工作范围，总 loss 下界 0.2\\n    仍安全。'\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v5\\n    role: evidence\\n    result: gate_std=0.022↓, gate_mean=0.965↑, maximize 无上界确认\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-18 18:17 UTC\\n  summary: Kill v6（smooth_saturation 未解决恒等退化），v7 改用 MSE(GAR, target) 双向 loss + gate\\n    diversity 正则化\\n  rationale: v6 step 100 确认 smooth_saturation 与 maximize 轨迹相同（gate_mean 0.874↑, gate_std\\n    0.037↓, L_GAR -0.158 加速中）。根因：任何单调奖励 GAR↑ 的 loss 都推 gate→1.0，因为 identity 对 GAR\\n    和 NTP 都是局部最优。需要双向 loss：MSE(GAR, target) 在 GAR>target 时产生反向梯度，打破单调性。加 gate diversity\\n    正则化直接强制层间分化（否则 LoRA 独立完成 GAR 调节，gate 仍趋向 identity）。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v6\\n    role: evidence\\n    result: 'step 100: gate_mean=0.874↑ gate_std=0.037↓，与 v5 同轨迹'\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-18 19:19 UTC\\n  summary: v7 gs200 达到 MVP Phase 2 关键里程碑：GAR 收敛到 target (0.48)，gate profile L3/L4\\n    与 Dongre onset 对齐，训练稳定。继续跑完 epoch 0，同时准备 UG baseline\\n  rationale: v7 MSE+diversity reg 首次同时实现：(1) GAR 实质改善（0.016→0.48, 30x）；(2) gate 不崩溃到\\n    identity（mean=0.94 vs v5的0.97）；(3) per-layer 可解释结构（L3/L4最低，与Dongre L4/L5 onset对齐）；(4)\\n    total loss始终正。三阶段GAR动力学（平台→相变→收敛）可发表。下一步需 UG baseline 对比验证 MVP pass 标准（TG GAR\\n    > UG + 3pp）。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: 'gs200: GAR=0.48, gate_std=0.053, L3/L4 lowest, total loss positive'\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-18 20:16 UTC\\n  summary: Reviewer 独立评估 v7：GAR 改善归因高度可疑（gating 扰动仅 ~1.4%，LoRA 为主要驱动）。eval 增加 per-turn\\n    gate profiling，ablation 增加 LoRA-only baseline\\n  rationale: 28 层中仅 L3/L4 gate 显著低于 1.0（~0.79-0.81），总 gating 扰动 ~1.4%，驱动 GAR 30x 提升在机制上不可信。UG\\n    baseline 只能测 turn conditioning 增量，无法区分 \\\"有 gating\\\" vs \\\"无 gating\\\"。需要 LoRA-only ablation（gate\\n    固定 1.0）排除 LoRA 单独驱动 GAR 改善的可能。per-turn gate profiling 是判断 inference-time 价值的核心数据。L3/L4\\n    与 Dongre 对齐只能说 \\\"coincides with\\\"，不能暗示因果。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: GAR=0.48 but gating perturbation only ~1.4%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-19 00:56 UTC\\n  summary: v7 推理 GAR recovery 极弱（ours +0.35pp, Dongre +0.72pp），远低于 3pp MVP 门槛。训练-推理\\n    30x GAR 断层需调查是实现 bug 还是真实现象。暂不判定 MVP fail，等 gate-profile + 30x 断层调查 + UG/LoRA-only\\n    ablation 完成。\\n  rationale: 1) 两个 metric 均远低于 3pp 但缺少 --gate-profile 数据无法判断 turn conditioning 在推理时是否有效；2)\\n    30x 训练-推理 GAR 断层可能是实现问题（goal token 定义不同？eval 数据分布不同？attention 计算范围不同？），不能直接把弱结果归因于方法失败；3)\\n    UG/LoRA-only ablation 数据缺失，无法分离 gate vs LoRA 贡献；4) 过早 pivot 可能放弃一个因实现问题而被低估的方法\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: training success, inference GAR weak\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  depends_on:\\n  - D012\\n  - D011\\n- id: D014\\n  date: 2026-05-19 01:09 UTC\\n  summary: Gate-profile 揭示 turn conditioning 反向学习：27/28 层 gate 在后续 turns 趋向 identity（减少干预），与假设完全相反。机制：GAR\\n    达标后 L_GAR≈0，NTP 梯度在长序列中推 gate→1.0。ThreadGate 正面 story 不成立，但继续完成 UG/LoRA-only ablation\\n    收集完整证据。\\n  rationale: 1) 27/28 层 diff 为负，训练明星层 L3/L4 推理时几乎静态（diff -0.001/-0.020）；2) 这是 NTP-GAR\\n    损失竞争的结构性后果——GAR 收敛后 NTP 完全主导，在长序列（后续 turns）推 gate 趋向 identity；3) 不可通过调参修复（提高 λ_GAR\\n    回到 v3b 病态饱和）；4) 但 UG/LoRA-only ablation 仍需完成：a) 确认 gating 贡献为零 b) 这些数据有 negative\\n    result 论文价值 c) 为 pivot 决策提供完整证据\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: reverse turn conditioning confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: ablation\\n    result: preparing\\n  depends_on:\\n  - D013\\n  - D012\\n- id: D015\\n  date: 2026-05-19 01:11 UTC\\n  summary: 30x 训练-推理 GAR 断层确认为 GAR 过拟合（非 measurement bug）。发现实验设计 confound：Phase1/Phase2\\n    eval 对话文本不同导致比较被污染。批准 standard_conversations 方案：base model 生成标准对话集，三个条件在同一对话上评估。\\n  rationale: 1) 训练/eval GAR 计算逻辑逐行一致（goal token、query positions、公式、teacher-forcing），排除实现\\n    bug；2) GAR 从 0.02→0.48 仅在 ultrachat 训练数据上，不泛化到 eval 数据 = attention pattern 过拟合；3)\\n    当前 baseline 对比被 confound（不同对话文本），需 standard_conversations 控制变量；4) 即使在公平测试下 TG\\n    略优于 LoRA-only，gate-profile 的反向 turn conditioning (D014) 仍是结构性问题\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: primary\\n    result: GAR overfitting confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: ablation\\n    result: preparing\\n  depends_on:\\n  - D014\\n  - D013\\n- id: D016\\n  date: 2026-05-19 01:52 UTC\\n  summary: Two-stage decoupled training：有条件尝试（~20-30% 成功率）。以 LoRA-only 结果为 gate keeper：LoRA-only\\n    ≈ TG → 不做（gating 贡献为零）；LoRA-only < TG → 做 Stage 1（解除 NTP 压制放大 gating 贡献）。不并行——等\\n    LoRA-only 数据再决策。\\n  rationale: Reviewer 系统性审查：(1) NTP-GAR 竞争部分解除但 gate→GAR 梯度路径本身弱（D004/D005 历史），Stage\\n    1 无 LoRA 时更弱；(2) GAR 过拟合独立于训练策略；(3) 分布漂移是最大结构性风险（Stage 2 LoRA 改变 hidden states\\n    使 Stage 1 gates 失效）；(4) 如果 LoRA-only=TG 则 gating 机制本身无效，改变训练策略无法解决机制局限。Stage 1\\n    成本低（~1.67M params），即使失败也提供 pure gating GAR 改善上界数据。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: NTP-GAR competition confirmed\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: preparing\\n  depends_on:\\n  - D015\\n  - D014\\n- id: D017\\n  date: 2026-05-19 02:25 UTC\\n  summary: 采纳 Reviewer 两路策略：准备路线 B 框架（negative result + mechanistic insight），以 LoRA-only\\n    为 gate keeper 决定是否先试路线 A（two-stage）。无论哪条路线，跨模型验证（Llama-3-8B）和 baseline 训练-推理 GAR\\n    对比都是 high-ROI 必做项。\\n  rationale: 路线 A ~20-30% 成功率但 ceiling 高（main track）；路线 B ~70% Findings 但需跨模型加强才冲\\n    main。A 失败的数据直接增强 B（\\\"even decoupled training fails\\\"）。关键缺失：baseline 训练-推理 GAR 对比——如果\\n    base model 也有 30x 断层则 claim 需调整。策略：B 框架先写（不依赖数据）、LoRA-only 决策点、A 失败无缝转 B。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence\\n    result: negative\\n  - exp_id: phase2_ug_s42\\n    role: ablation\\n    result: running\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: preparing\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-19 10:42 UTC\\n  summary: Reviewer 深度分析：Route A 成功概率从 20-30% 修正至 <5%，根本矛盾是 teacher-forcing→generation\\n    分布偏移而非 NTP-gate 竞争\\n  rationale: Reviewer 分析揭示更深层机制：(1) LoRA-only L_GAR≈0 证明 gating 在训练端冗余；(2) 如果 LoRA-only\\n    推理 GAR ≈ TG，问题不在 NTP-gate 竞争，而在 teacher-forcing 下优化的 GAR 无法迁移到 generation 模式——这个根本矛盾\\n    two-stage 也无法解决；(3) Route B Findings 可行性 65-75%，需跨模型验证；(4) 关键 framing：\\\"发现了 X 机制\\\"而非\\\"方法\\n    X 失败了\\\"。四路 eval 补充 PPL + per-turn GAR curve 作为核心判别 metrics。\\n  related_experiments:\\n  - exp_id: phase2_lora_only_s42\\n    role: gate_keeper\\n    result: running, training L_GAR≈0 same as TG/UG\\n  - exp_id: phase2_tg_s42_v7\\n    role: reference\\n    result: inference GAR +0.35pp\\n  - exp_id: phase2_ug_s42\\n    role: reference\\n    result: training complete, eval pending\\n  depends_on:\\n  - D017\\n  - D015\\n  - D014\\n- id: D019\\n  date: 2026-05-19 10:56 UTC\\n  summary: v7 中间 checkpoint：选 Option B（3 epoch checkpoint 粗粒度分析），不重训。跨模型验证优先级更高。\\n  rationale: 重训 v7 保存中间 checkpoint 需 ~6h GPU，而 GPU 接下来优先用于四路 eval + 跨模型验证（Llama-3），后者对\\n    Route B 论文强度提升远大于细粒度 GAR 泛化曲线。3 个 epoch checkpoint（gs1000/2000/3000）足够展示过拟合趋势。10\\n    weeks 到 DDL，如需精细分析可后补。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: subject\\n    result: 3 epoch checkpoints available, fine-grained gs50-200 missing\\n  depends_on:\\n  - D018\\n  - D017\\n- id: D020\\n  date: 2026-05-19 12:27 UTC\\n  summary: Llama-3 最小验证方案扩展为 Base + TG + LoRA-only（Reviewer 建议），总计 ~15h GPU\\n  rationale: 论文 C4 claim \\\"gating redundancy is model-agnostic\\\" 需要 Llama 上的 LoRA-only\\n    数据点。仅 Base + TG 能验证 GAR gap 但无法验证 gating 冗余。额外 ~6h GPU 换取 C4 跨模型支撑，ROI 高。同时 Reviewer\\n    发现计划中 CLI flags、NF3' 描述、output_dir 路径有误，执行时需修正。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v7\\n    role: reference\\n    result: Qwen baseline for cross-model comparison\\n  depends_on:\\n  - D019\\n  - D018\\n- id: D021\\n  date: 2026-05-19 13:15 UTC\\n  summary: Route B 正式确认：四路 eval 三路趋同（GAR 差异<0.6pp, PPL 差异<0.02），gating 零增量。进入 negative\\n    result + mechanistic insight 路线。\\n  rationale: 'GAR-ours: TG 0.487 / UG 0.492 / LoRA-only 0.486（差异<0.6pp）；GAR-Dongre:\\n    TG 0.016 / UG 0.013 / LoRA-only 0.014（差异<0.3pp）；PPL: TG 2.629 / UG 2.616 / LoRA-only\\n    2.629。三个维度均确认 gating 无增量。Route A 完全无依据（<5% 预期已彻底归零）。核心发现：teacher-forcing 下 GAR\\n    loss 有效（~0.49）但不迁移到推理端（Dongre ~0.015），完美支持 D018 的 teacher-forcing distribution\\n    shift 叙事。注意：eval 数据与训练集重叠，需补做 held-out eval。'\\n  related_experiments:\\n  - exp_id: phase2_lora_only_s42\\n    role: key_evidence\\n    result: GAR-ours 0.486, GAR-Dongre 0.014, PPL 2.629 — identical to TG/UG\\n  - exp_id: phase2_tg_s42_v7\\n    role: key_evidence\\n    result: GAR-ours 0.487, GAR-Dongre 0.016, PPL 2.629\\n  - exp_id: phase2_ug_s42\\n    role: key_evidence\\n    result: GAR-ours 0.492, GAR-Dongre 0.013, PPL 2.616\\n  depends_on:\\n  - D018\\n  - D017\\n  - D019\\n  - D020\\n- id: D022\\n  date: 2026-05-19 14:39 UTC\\n  summary: 'Dream review 分析: 收窄 claim scope + 补充 3 个实验 (bootstrap CI / exposure-bias\\n    mitigation / code verification)'\\n  rationale: Dream dream_20260519T135115 (review_mode=full) best=3.0 median=3.0 (Weak\\n    Reject)。两份 review 一致指出三个结构性问题：(1) claim 过度泛化 \\\"all auxiliary attention losses\\\"\\n    unsupported by single scalar gating test → 收窄为 \\\"lightweight residual gating with\\n    joint NTP+GAR loss\\\"; (2) 引用仅 11 篇，缺 attention sinks/Found-in-the-Middle/gated\\n    attention/transformer circuits 等 → 目标 25-30; (3) 单 seed 无方差估计 → 添加 bootstrap CI\\n    (plan_015)。额外添加 exposure-bias mitigation test (plan_016, P1, 8h) 作为 constructive\\n    direction，以及 code-paper architecture verification (plan_017, P0, 0h)。修正后预期 best\\n    从 3.0 提升至 3.5 (Weak Accept)。需 re-dream 验证。\\n  related_experiments:\\n  - exp_id: phase2_4way_eval\\n    role: evidence_base\\n    result: negative\\n  - exp_id: phase2_tg_s42_v7\\n    role: evidence_base\\n    result: success\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-19 14:50 UTC\\n  summary: 'Eq.3 code-paper formula mismatch confirmed (plan_017): code uses x+g·f(x),\\n    dream paper.tex wrote g·x+f(x). Data unaffected, mechanism narrative needs rewrite\\n    for Paper Agent.'\\n  rationale: 'Reviewer critical finding: ThreadGate code implements ReZero-style gating\\n    (gate on sub-layer output), but dream paper.tex wrote gate on residual stream\\n    — semantically opposite when g→0. All experiments used the same code so data is\\n    internally consistent. Mechanism narrative in paper needs correction: g→0 = layer\\n    becomes no-op (sub-layer suppressed), NTP pushes g→1 to preserve layer computation\\n    capacity (not to preserve skip connection). Updated paper_framing.md R4 with detailed\\n    Paper Agent writing instructions.'\\n  related_experiments:\\n  - exp_id: plan_017\\n    role: verification\\n    result: confirmed mismatch\\n  depends_on:\\n  - D022\\n\", \"total_chars\": 15777, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2aa5e70d-ddaf-4c39-9f81-d2c094cb152d",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "ee8c582a-5e78-414c-95af-6d405da5a063",
  "sourceToolAssistantUUID": "2aa5e70d-ddaf-4c39-9f81-d2c094cb152d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T15:28:45.541Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Dis9sA167BrDY8wnSRsgvX`</summary>

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
  "parentUuid": "ee8c582a-5e78-414c-95af-6d405da5a063",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAVuxH5mVzToWGd37Dm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e26c362-5346-43e7-880a-f2bcc52b8a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WNjJ9C7NqYEYqpeiGeC9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15851,
      "cache_read_input_tokens": 55245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15851,
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

_source line 30 · 2026-05-19T15:28:45.554Z_

<details><summary>↩ Tool result · `toolu_01Dis9sA167BrDY8wnSRsgvX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- phase2_tg_s42_v8_schedsampling: Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。（准备中）\\n\\n## 近期结论\\n- **analysis_attention_heatmap** (success): 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。 ← 基于 phase2_tg_s42_v7\\n- **analysis_gradient_conflict** (success): NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。 ← 基于 phase2_tg_s42_v7\\n- **phase2_4way_eval_heldout** (success): 四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。 ← 基于 phase2_4way_eval\\n\\n## 趋势\\n成功 8 / 负向 5 / 失败 1 / 共 15\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-20861: 无 GPU 信息\\n\\n## 告警\\n- phase2_tg_s42_v2: 已被终止 — unknown\\n- phase2_tg_s42_v4: 训练失败 — unknown\\n\", \"total_chars\": 1139, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e26c362-5346-43e7-880a-f2bcc52b8a4e",
  "isSidechain": true,
  "promptId": "8ad456c2-e959-4f97-9139-3fee79f30cc9",
  "agentId": "a910e29cfb65eeab1",
  "type": "user",
  "uuid": "27657aff-5114-4d1a-be64-c0f264354ece",
  "sourceToolAssistantUUID": "5e26c362-5346-43e7-880a-f2bcc52b8a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T15:29:50.938Z_

I now have a thorough understanding of the paper, its experimental history, and the project context. Here is my review.

---

## Review: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"

**Reviewer 1 (R1) -- Focus: Methods and Experiments**

---

### 1. Methodological Soundness

ThreadGate is well-motivated and cleanly designed: the ReZero-style per-layer scalar gate is the simplest possible intervention on the residual stream, which makes it an appropriate starting point for testing whether residual gating can recover goal attention. The loss design journey (v1--v7, seven configurations across four design families) is commendable, as it shows the final MSE+diversity formulation was not arbitrary but the product of systematic elimination. However, the ablation design has a subtle asymmetry: TG and UG both receive the GAR+diversity auxiliary losses during training, while LoRA-only receives NTP only. This means LoRA-only has a different training objective, so the convergence of TG/UG/LO at inference could partly reflect that auxiliary losses provide no additional training signal to LoRA parameters, rather than that gating is specifically inert. A more rigorous ablation would include a "LoRA + GAR loss, no gate" condition to fully disentangle the gate mechanism from the auxiliary loss.

### 2. Experimental Rigor

The experiments are well-structured for a negative-result paper: four-way ablation, cross-model replication, bootstrap CI, and scheduled sampling for causal attribution. The bootstrap CI (n=50, 10K resamples, p=0.71, Cohen's d=0.02) is a strong statistical statement. However, all training uses a single seed (42), which weakens claims about gradient competition dynamics -- the per-layer cosine similarity and magnitude ratio patterns could be seed-dependent. The evaluation uses only 50 conversations, which is adequate for the paired bootstrap but limited for making broad generalization claims. The scheduled sampling experiment, while compelling as a causal probe, was conducted only on Qwen and not replicated on Llama, which is inconsistent with the cross-model validation philosophy applied to the other claims.

### 3. Reproducibility

Most critical details are provided: LoRA rank (16), gate learning rate (5e-4), dataset size (1,000 conversations), epochs (3), seed (42), models (Qwen-2.5-7B-Instruct, Llama-3.1-8B-Instruct). However, several important details are missing: (a) the base learning rate for LoRA parameters; (b) the exact values of lambda_GAR and lambda_div; (c) gradient accumulation steps and effective batch size; (d) the gate diversity loss formulation (only described as "encourages diversity," with no equation); (e) how the GAR-ours metric selects "last token per assistant turn" in practice; (f) the optimizer and scheduler. The paper also references "line-by-line code audits" to verify the 30x gap is not a bug but provides no code or supplementary material.

### 4. Analysis Depth

The gradient competition analysis (Section 6.1) is the strongest contribution. The decomposition into directional conflict (cosine similarity) and amplitude suppression (magnitude ratio), tracked across epochs and layers, provides genuine mechanistic insight. The observation that the apparent "resolution" of conflict (cos_sim trending toward 0) is actually marginalization rather than reconciliation is a non-obvious finding well-supported by the data. The exposure bias causal argument (Section 6.4) is well-designed: the scheduled sampling experiment provides a proper intervention, and the 30x-to-4.3x gap reduction is quantitatively meaningful. However, the "86% linear attribution" claim is somewhat simplistic -- the linear gap fraction (30-4.3)/30 is an arbitrary normalization. A log-scale attribution (as briefly mentioned in the review_context) yields 57%, and the paper does not discuss why one is preferred over the other.

### 5. Weaknesses in Methods/Experiments

The most significant methodological gap is the lack of any attempt at stronger gating architectures before concluding that lightweight gating fails. A single scalar gate per layer is the weakest possible intervention -- vector gates, head-specific gates, or input-dependent (dynamic) gates would all be stronger tests. The paper's title claims "lightweight gating cannot fix" the problem, but only tests the simplest variant. The scheduled sampling experiment (Section 6.4) is presented with a single configuration (linear 0-50%) and no ablation over SS ratio, making it hard to assess whether 100% SS would close the gap further. The downstream evaluation (instruction compliance, r=0.82 with GAR) is too coarse to be convincing -- 3 turns x 3 models with differences under 2pp is essentially noise, and the metric itself (compliance with formatting instructions) is a simplified proxy acknowledged to be in an appendix.

---

### Strengths

- Thorough ablation design (four-way on Qwen, three-way on Llama, held-out validation, bootstrap CI) provides strong evidence for the zero-benefit claim.
- The gradient competition analysis (Section 6.1) is a genuine mechanistic contribution: per-layer cosine similarity and magnitude ratio across training epochs is novel for understanding auxiliary loss dynamics.
- Seven loss configurations (v1-v7) demonstrate systematic exploration, making the reader confident that v7 is not cherry-picked but the result of principled design iteration.
- Cross-model validation (Qwen MHA vs. Llama GQA) with near-identical quantitative patterns (30x vs. 26x gap, 0.20pp vs. 0.19pp TG-LO diff) significantly strengthens generalizability.
- The scheduled sampling experiment upgrades the paper from a pure negative result to a causal diagnosis with partial mitigation, which is a substantially stronger contribution.
- Writing is clear and well-structured; the progression from C1 (degradation exists) through C5 (cross-model) is logical and easy to follow.

### Weaknesses

- Single seed (42) for all training runs. While bootstrap CI covers evaluation variance, training variance (which affects gate learning dynamics, gradient competition patterns, and the 30x gap magnitude) is entirely uncharacterized.
- The paper only tests the weakest form of gating (per-layer scalar). The claim that "lightweight gating cannot fix" multi-turn degradation is overclaimed given that head-specific gates, vector gates, or input-dependent gates are all still "lightweight" but untested.
- Missing ablation: no "LoRA + GAR loss, no gate" condition. The current design conflates the gate mechanism with the auxiliary loss -- LoRA-only uses NTP-only, so the equivalence at inference might simply mean auxiliary losses add nothing to LoRA, not specifically that gating adds nothing.
- Scheduled sampling experiment lacks cross-model replication (Llama) and SS ratio ablation (what happens at 75%, 100%?). This undermines the causal attribution, which is the paper's strongest upgrade from a negative result.
- The training data (1,000 UltraChat conversations, 3 epochs) is very small. It is unclear whether the 30x gap is a consequence of underfitting/overfitting on a small dataset or a fundamental property. No experiment on a larger dataset is attempted.
- Several hyperparameters and design details are missing (see Reproducibility above), making it difficult for others to replicate the work.

### Questions for Authors

1. Have you tried a "LoRA + GAR loss, no gate" ablation? If LoRA-only with GAR+diversity losses matches TG at inference, that would strengthen the claim that gating specifically is the inert component. If it doesn't, it would change the interpretation -- the issue might be that auxiliary losses provide no durable signal through any pathway, not just through gates.

2. The 30x training-inference gap is measured by comparing GAR-ours (last token per assistant turn, teacher-forced context) with GAR-Dongre (all response tokens, autoregressive context). These are different metrics on different data distributions. How much of the 30x gap is attributable to the metric definition difference versus the distribution shift? Have you computed GAR-Dongre during training or GAR-ours at inference for a direct comparison?

3. Why was the scheduled sampling experiment not replicated on Llama-3.1-8B? Given that cross-model validation is a stated contribution and the SS experiment is the paper's strongest causal evidence, this omission is conspicuous.

4. The gate diversity loss is described only qualitatively ("encourages diversity across layer-wise gate values to prevent collapse"). What is the exact formulation? Is it F.relu(min_std - gate_std) as suggested by project notes? If so, min_std is an important hyperparameter that should be reported.

5. Your training uses only 1,000 conversations for 3 epochs. Have you considered that the 30x gap might be a small-data phenomenon? On a larger dataset (e.g., full UltraChat), the model might learn more robust attention patterns that transfer better to inference.

### Overall Assessment Score

**3.0** (Findings-level)

The paper presents a well-structured negative result with genuine mechanistic insight. The gradient competition analysis and scheduled sampling experiment are real contributions. However, the methodological scope is too narrow (only scalar gates tested), the scheduled sampling experiment lacks cross-model replication, training uses a single seed, and several reproducibility details are missing. The paper would benefit from testing at least one stronger gating variant to justify the title's generality, replicating the SS experiment on Llama, and providing multi-seed training to characterize variance in the gradient competition dynamics. In its current form, it meets the bar for Findings but not Main conference.

### Confidence

**4** (high confidence -- I have reviewed the full paper, project experimental history, design decisions, and imagined experiment specifications in detail, and the claims are within my area of expertise in transformer mechanisms and training dynamics)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27657aff-5114-4d1a-be64-c0f264354ece",
  "isSidechain": true,
  "agentId": "a910e29cfb65eeab1",
  "requestId": "req_011CbCAWHyrAHnZxQxinuwkp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f78dc640-2c74-4560-ae3a-6b83fab5180f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "6573117f-3f12-4084-9ce0-947b9902daf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLggTRSbkU59FZCcVgyMTn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10189,
      "cache_read_input_tokens": 71096,
      "output_tokens": 2330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10189
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2330,
          "cache_read_input_tokens": 71096,
          "cache_creation_input_tokens": 10189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10189,
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
