# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty, positioning, and related work**. Review

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a2318d24f3259d05c.jsonl`
- **Structured JSON:** [`a21ee0a117061469b9c5.json`](../../sessions/a2/a21ee0a117061469b9c5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-15T17:47:06.544Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty, positioning, and related work**. 

Review the following paper and produce a structured review. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title**: "Output-Distribution Distillation Eliminates Compensation Overhead for Contextual SwiGLU Sparsity Prediction"

**Core claim**: A KL-divergence-trained contextual sparsity predictor achieves 9.53 PPL on WikiText-2 at 50% sparsity on Llama 3.1 8B — surpassing BCE+compensation (11.56) while eliminating 256MB compensation parameters. Organized around a 2D taxonomy (loss coupling × correction granularity).

**Contributions as stated**:
1. KL eliminates compensation overhead at quality parity (PPL 9.53 vs 11.56, 8MB vs 264MB)
2. Empirically observed partial additivity of SPON (static) + KL (contextual) corrections (22% interaction residual)
3. Taxonomy and systematic ablation as methodological contribution

**Method**:
- Train lightweight predictor f_θ producing binary mask m ∈ {0,1}^D for SwiGLU intermediate neurons
- Loss: KL(p_dense || p_sparse) — minimizing output-distribution divergence
- Gumbel-sigmoid relaxation during training, hard threshold at inference
- Key insight: KL gradient couples all neurons through ∂logits/∂h chain, unlike BCE's per-neuron factorized gradient
- Optional composition with SPON static bias correction

**Related Work as presented** (Section 2):
- Training-free: TEAL (magnitude + greedy allocation), WINA (weight-informed), R-Sparse (rank-aware)
- Static learned: SPON (per-layer bias + KL training)
- Contextual learned: FastForward (BCE + compensation MLPs)
- Per-layer intermediate: ShadowLLM (MSE)
- 2D taxonomy table with "Ours" filling the per-token contextual + coupled KL cell

**Key experimental results**:
- Four-condition ablation: KL-only 9.53 > BCE+comp 11.56 (Table 3)
- STE baseline: KL is 72% of gain, Gumbel 28% (Table 4)
- Iso-compute: BCE at equal compute still 14 PPL behind (Table 5)
- SPON+KL: 8.91 PPL, 22% interaction residual (Table 7)
- Cross-model: Mistral 7B confirms direction (gap 1.07 vs 2.03) (Table 10)
- Efficiency: 1.49× vs 1.18× speedup at b=32 (Table 9)
- Full benchmarks: 7 tasks, 2 long-context evals, MT-Bench (Tables 8, 11-13)
- Sparsity sweep: KL-BCE gap grows super-linearly, R²=0.88 (Table 14)

**Stated Limitations**: Only 7-8B scale, 22% interaction residual, R²=0.88 with systematic deviations, long-context degradation, KL 80× more expensive per step

## Your Review Task (R2 — Novelty + Related Work)

Evaluate:
1. **Novelty**: How novel is KL training for sparsity predictors? Is this a new idea or an obvious extension? Is the gradient coupling insight genuinely new?
2. **Positioning**: Is the 2D taxonomy a real contribution or just organizational framing? Does it accurately represent the landscape?
3. **Related work completeness**: Are important baselines or prior methods missing? Consider: knowledge distillation literature, structured pruning, MoE routing, other sparse prediction approaches
4. **Claim calibration**: Are contributions overclaimed or appropriately scoped? Does "eliminates compensation" overstate what's shown?
5. **Significance and impact**: Would this change how practitioners build sparse inference systems? Is the practical impact sufficient for a top venue?
6. **Writing quality**: Clarity, organization, presentation

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: minor/moderate/major)
- Questions for authors
- Missing related work or positioning issues
- Overall score and confidence
- Short justification for score

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "058108cf-4a9a-4d31-bde7-53c5b71c9623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T17:47:06.547Z_

```json
{
  "parentUuid": "058108cf-4a9a-4d31-bde7-53c5b71c9623",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
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
  "uuid": "4fa4ff13-7a9c-4b50-bb33-a6e0a7f6c040",
  "timestamp": "2026-05-15T17:47:06.547Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T17:47:09.442Z_



I'll start by reading the paper and any related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fa4ff13-7a9c-4b50-bb33-a6e0a7f6c040",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mpXWVGb8CPqj1nKNVS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a836f877-1e2f-4849-be9f-ca656ae3c0c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017F4NW7eNB1Chd8DF3bucJw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6952,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6952,
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

_source line 4 · 2026-05-15T17:47:09.907Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CzHHopVBzVBnKMoydKvkQ1`</summary>

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
  "parentUuid": "a836f877-1e2f-4849-be9f-ca656ae3c0c2",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mpXWVGb8CPqj1nKNVS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8a19fae-3f25-4481-bd62-289993f7e218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017F4NW7eNB1Chd8DF3bucJw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6952,
      "cache_read_input_tokens": 8252,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6952
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 6952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6952,
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

_source line 5 · 2026-05-15T17:47:09.910Z_

<details><summary>↩ Tool result · `toolu_01CzHHopVBzVBnKMoydKvkQ1`</summary>

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
  "parentUuid": "e8a19fae-3f25-4481-bd62-289993f7e218",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "6fc0e881-0233-4522-a141-1cbe09555049",
  "sourceToolAssistantUUID": "e8a19fae-3f25-4481-bd62-289993f7e218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T17:47:12.594Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01JrrPU3ucGhfoH6wx6THvGs`</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fc0e881-0233-4522-a141-1cbe09555049",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mpn46RP1rG44Vvp5qs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0aabc559-b2c2-40ad-ae5d-bbc12dd4f4f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ne8tQNNQ4aMhquE42gVpLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-15T17:47:12.661Z_

<details><summary>↩ Tool result · `toolu_01JrrPU3ucGhfoH6wx6THvGs`</summary>

```text
{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (21 个)\n\n- **mvp_kl_norm_v2_s123**: DONE (success) — \n- **mvp_kl_norm_v2_s42**: DONE (success) — \n- **spon_kl_s42**: PREPARING — \n- **kl_only_s1**: RUNNING — \n- **kl_only_s0**: RUNNING — \n- **mvp_kl_norm_s456**: PREPARING (killed) — \n- **kl_norm_v3_quicktest**: PREPARING (success) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n- **mvp_kl_s456**: QUEUED (killed) — \n- **mvp_kl_s123**: QUEUED (killed) — \n- **kl_lagrangian_v2**: PREPARING (killed) — \n- **kl_lagrangian_quicktest**: DONE (negative) — \n- **mvp_kl_s42**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| kl_only_s1 | — | — | — | — |\n| kl_only_s0 | — | — | — | — |\n\n## 待处理\n- spon_training（等待人工审批）\n- bce_comp_staged_s42（等待人工审批）\n- mvp_kl_s456（排队等待 GPU）\n- mvp_kl_s123（排队等待 GPU）\n- spon_kl_s42（准备中）\n- mvp_kl_norm_s456（准备中）\n- kl_norm_v3_quicktest（准备中）\n- kl_lagrangian_v2（准备中）\n\n## 近期结论\n- **mvp_kl_norm_v2_s456** (success): —\n- **mvp_kl_norm_v2_s123** (success): —\n- **mvp_kl_norm_v2_s42** (success): —\n\n## 趋势\n成功 6 / 负向 2 / 失败 3 / 共 11\ncalibration_samples: 32 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0aabc559-b2c2-40ad-ae5d-bbc12dd4f4f1",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "8349ae10-4b55-4281-b6e2-95eb8694b2b9",
  "sourceToolAssistantUUID": "0aabc559-b2c2-40ad-ae5d-bbc12dd4f4f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T17:47:13.271Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015s6avoR1ZFXSfu2n5g1gvo`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8349ae10-4b55-4281-b6e2-95eb8694b2b9",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mpn46RP1rG44Vvp5qs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3bda43c-f8a4-4900-84f6-98c2f8ad52c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ne8tQNNQ4aMhquE42gVpLi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15204,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 15204,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 9 · 2026-05-15T17:47:13.280Z_

<details><summary>↩ Tool result · `toolu_015s6avoR1ZFXSfu2n5g1gvo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| kl_only_s1 | — | — | — | — |\\n| kl_only_s0 | — | — | — | — |\\n\\n## 待处理\\n- spon_training（等待人工审批）\\n- bce_comp_staged_s42（等待人工审批）\\n- mvp_kl_s456（排队等待 GPU）\\n- mvp_kl_s123（排队等待 GPU）\\n- spon_kl_s42（准备中）\\n- mvp_kl_norm_s456（准备中）\\n- kl_norm_v3_quicktest（准备中）\\n- kl_lagrangian_v2（准备中）\\n\\n## 近期结论\\n- **mvp_kl_norm_v2_s456** (success): —\\n- **mvp_kl_norm_v2_s123** (success): —\\n- **mvp_kl_norm_v2_s42** (success): —\\n\\n## 趋势\\n成功 6 / 负向 2 / 失败 3 / 共 11\\ncalibration_samples: 32 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\n\\n## 告警\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n\", \"total_chars\": 793, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3bda43c-f8a4-4900-84f6-98c2f8ad52c0",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "28c57735-8647-43dc-8f72-812a6456a4b1",
  "sourceToolAssistantUUID": "f3bda43c-f8a4-4900-84f6-98c2f8ad52c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T17:47:15.935Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AXYfRSk36apjbj8e4Y2pZe`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28c57735-8647-43dc-8f72-812a6456a4b1",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mq2V1nH8B7Lrn2ksBq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d00bdac-6b1d-45ad-832b-bf21d7592f94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NEVWRu8tgYdPKRgvjMoCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 16652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 11 · 2026-05-15T17:47:15.946Z_

<details><summary>↩ Tool result · `toolu_01AXYfRSk36apjbj8e4Y2pZe`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d00bdac-6b1d-45ad-832b-bf21d7592f94",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "3745b3bf-5c92-45ea-b209-489edc9ef76a",
  "sourceToolAssistantUUID": "4d00bdac-6b1d-45ad-832b-bf21d7592f94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T17:47:16.877Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LqYK4FCuY2K7xSzbSsuanb`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3745b3bf-5c92-45ea-b209-489edc9ef76a",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mq2V1nH8B7Lrn2ksBq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "025d2cd7-3102-42da-87a2-56db45f9ffd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NEVWRu8tgYdPKRgvjMoCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 16652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-15T17:47:16.889Z_

<details><summary>↩ Tool result · `toolu_01LqYK4FCuY2K7xSzbSsuanb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-15 16:53 UTC | 更新原因: Reviewer warning 修正：BCE std 0.72→0.89，Claim 3 降级，SPON 预算提升，并行启动计划\\n\\n## 核心方向\\nKL-divergence 输出分布蒸馏训练 SwiGLU 激活稀疏性预测器，验证是否消除对 error compensation network 的需求，并测试与 SPON 静态校正的组合加性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-15 通过，D007）\\n- **MVP 结论**: KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity，差距 31.53 PPL\\n- **关键发现**: KL 非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66）；KL hard-mask PPL 9.20 接近 dense 6.12\\n- **Dream**: dream_20260515T164925 运行中（full review），等结果后批准 P0 实验\\n- **Experiment Plan**: 12 experiments（P0×7, P1×3, P2×2），总 196 GPU-hours。详见 experiment_plan.yaml\\n- **Reviewer Warning**: Claim 1 强度取决于 BCE+comp（未测）；Claim 3 降级为 testable prediction；SPON 复现是关键路径\\n\\n## 近期任务\\n- [x] MVP 验证（KL vs BCE @ 50% sparsity, 3 seeds）\\n- [x] 写 paper_framing.md + experiment_plan.yaml\\n- [x] 启动 Dream full review (dream_20260515T164925)\\n- [ ] 等 Dream 结果 → 按行动指令调整\\n- [ ] Dream 通过后并行启动: plan_001 BCE+comp (cuda:0) + plan_004 SPON (cuda:1)\\n- [ ] Agent 完成 vanilla TEAL baseline（队列中）\\n- [ ] 补 KL-only 2 seeds (s0, s1) → 5-seed headline\\n- [ ] 实现 BCE+compensation 训练流程\\n- [ ] 关注 s456 seed 敏感性（13.58 vs 12.08/11.91）\\n\\n## GPU 预算\\n- 本地: westd-34887 cuda:0, cuda:1 — RTX PRO 6000 Blackwell (98GB each)\\n- 可用: 444 GPU-hours remaining (480 - 36 MVP)\\n- 计划: P0 114h + P1 70h + P2 12h = 196h（44% 利用率）\\n- Constraint: C001 — 仅 cuda:0, cuda:1\\n\\n## 目标时间线\\n| 阶段 | 日期 | 内容 |\\n|------|------|------|\\n| Dream review | 05-15 | dream_20260515T164925 |\\n| Phase 1 | 05-15 ~ 05-18 | plan_001 BCE+comp + plan_004 SPON + plan_006 baselines（并行） |\\n| Phase 2 | 05-18 ~ 05-20 | plan_005 composition + plan_002 STE + plan_003 iso-compute |\\n| Phase 3 | 05-20 ~ 05-22 | plan_007 full eval + plan_008 sweep + plan_009 Mistral |\\n| Paper | 05-22 ~ 05-24 | Paper Agent Full Draft + iteration |\\n| Submit | 05-25 | ARR submission |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-15 | MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程 | mvp_kl_norm_v2_s42, mvp_kl_norm_v2_s123, mvp_kl_norm_v2_s456, mvp_bce_s42, mvp_bce_s123, mvp_bce_s456 |\\n| D006 | 2026-05-15 | 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_norm | kl_normalized_quicktest, mvp_kl_norm_s42, mvp_kl_norm_s123 |\\n| D005 | 2026-05-15 | KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练 | kl_normalized_quicktest, mvp_kl_s42, mvp_kl_s123, mvp_kl_s456 |\\n| D004 | 2026-05-15 | KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯  | kl_lagrangian_quicktest |\\n| D003 | 2026-05-15 | KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_w | mvp_kl_s42 |\\n| D002 | 2026-05-15 | 校准数据从 SlimPajama-627B 改为 WikiText-103 train split | mvp_kl_s42, mvp_bce_s42 |\\n| D001 | 2026-05-15 | MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perp | — |\\n\\n\\n\\n\", \"total_chars\": 2753, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "025d2cd7-3102-42da-87a2-56db45f9ffd1",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "3a820de5-0e97-4a84-9391-75fa646fa55d",
  "sourceToolAssistantUUID": "025d2cd7-3102-42da-87a2-56db45f9ffd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T17:47:17.889Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L1WTb7AbsTpamgUGZ9biSq`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a820de5-0e97-4a84-9391-75fa646fa55d",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mq2V1nH8B7Lrn2ksBq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df9a19b2-1d1a-445d-915f-8d2a7809e0f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NEVWRu8tgYdPKRgvjMoCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 16652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-15T17:47:17.908Z_

<details><summary>↩ Tool result · `toolu_01L1WTb7AbsTpamgUGZ9biSq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md\", \"content\": \"# Memory — distill_sparse_swiglu\\n\\n## 决策记录\\n\\n- [2026-05-15] s0/s1 完成后 GPU 分配：cuda:0 → bce_comp_staged_s42 (plan_001), cuda:1 → spon_training (plan_004)。Director 要求秒级衔接。\\n- [2026-05-15] WINA global 预期会崩（跨层归一化问题），不排查。正式 baseline: TEAL greedy + WINA greedy。WINA global 仅作 \\\"why greedy allocation matters\\\" motivation example。\\n- [2026-05-15] BCE+comp 代码通过 Reviewer：compensation 67.2M params (bottleneck=256)。losses.py / predictor.py / spon.py 全 PASS。\\n- [2026-05-15] SPON 458K params (bias vectors)，dry-run 通过。\\n- [2026-05-15] MVP 结论：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity。KL 非均匀 per-layer 分配 (0.22-0.80)。\\n- [2026-05-15] s456 seed 敏感性：sparse PPL 13.58 vs s42 12.08 / s123 11.91，PPL increase 48.6% vs 31.2%/28.8%。需关注。\\n\", \"total_chars\": 729, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df9a19b2-1d1a-445d-915f-8d2a7809e0f2",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "5868af0c-1003-40f1-99a6-aef3e27fbea2",
  "sourceToolAssistantUUID": "df9a19b2-1d1a-445d-915f-8d2a7809e0f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T17:47:18.348Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015ttTu3QxMGBsMW9JyrcvYQ`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5868af0c-1003-40f1-99a6-aef3e27fbea2",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mq2V1nH8B7Lrn2ksBq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e84cbc52-ce60-4392-af78-5a1edf9a1322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NEVWRu8tgYdPKRgvjMoCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 16652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 17 · 2026-05-15T17:47:18.358Z_

<details><summary>↩ Tool result · `toolu_015ttTu3QxMGBsMW9JyrcvYQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml\", \"content\": \"# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\\n# Last updated: 2026-05-15\\n# Survey scope: 2023-2026, 4 directions\\n\\n# =============================================================================\\n# Direction 1: KL distillation for structured/activation sparsity\\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\\n# learnable bias correction, not predictor training. This is our novelty.\\n# =============================================================================\\n\\n- title: \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\"\\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\\n  venue: ICML 2026\\n  year: 2026\\n  arxiv_id: \\\"2512.12744\\\"\\n  category: direct-competitor\\n  role: \\\"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\\\"\\n  key_finding: \\\"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\\\"\\n  relevance_to_us: \\\"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\\\"\\n\\n- title: \\\"Compact Language Models via Pruning and Knowledge Distillation\\\"\\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv_id: \\\"2407.14679\\\"\\n  category: method-component\\n  role: \\\"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\\\"\\n  key_finding: \\\"Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration\\\"\\n  relevance_to_us: \\\"支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑\\\"\\n\\n- title: \\\"Instruction-Following Pruning for Large Language Models\\\"\\n  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]\\n  venue: ICML 2025\\n  year: 2025\\n  arxiv_id: \\\"2501.02086\\\"\\n  category: method-component\\n  role: \\\"训练sparse mask predictor的范式——input-dependent mask selection\\\"\\n  key_finding: \\\"训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM\\\"\\n  relevance_to_us: \\\"架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略\\\"\\n\\n# =============================================================================\\n# Direction 2: Output distribution preservation in pruning/sparsity\\n# =============================================================================\\n\\n- title: \\\"Distilling to Hybrid Attention Models via KL-Guided Layer Selection\\\"\\n  authors: []\\n  venue: arXiv\\n  year: 2025\\n  arxiv_id: \\\"2512.20569\\\"\\n  category: method-component\\n  role: \\\"KL散度引导layer selection——用distribution差异决定哪些层需要保留\\\"\\n  key_finding: \\\"用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策\\\"\\n  relevance_to_us: \\\"方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大\\\"\\n\\n# =============================================================================\\n# Direction 3: SPON和类似的learnable bias correction for sparsity\\n# =============================================================================\\n\\n- title: \\\"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\\\"\\n  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]\\n  venue: arXiv\\n  year: 2026\\n  arxiv_id: \\\"2602.00397\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor + error compensation双组件架构——与SPON的bias correction思路互补\\\"\\n  key_finding: \\\"组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速\\\"\\n  relevance_to_us: \\\"与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）\\\"\\n\\n- title: \\\"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models\\\"\\n  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]\\n  venue: arXiv\\n  year: 2025\\n  arxiv_id: \\\"2508.02128\\\"\\n  category: background\\n  role: \\\"N:M structured activation sparsity——hardware-friendly的sparsity pattern\\\"\\n  key_finding: \\\"Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合\\\"\\n  relevance_to_us: \\\"如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work\\\"\\n\\n# =============================================================================\\n# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)\\n# =============================================================================\\n\\n- title: \\\"Training-Free Activation Sparsity in Large Language Models\\\"\\n  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]\\n  venue: ICLR 2025 (Spotlight)\\n  year: 2025\\n  arxiv_id: \\\"2408.14690\\\"\\n  category: direct-competitor\\n  role: \\\"TEAL——我们的主要baseline，training-free magnitude pruning\\\"\\n  key_finding: \\\"对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速\\\"\\n  relevance_to_us: \\\"TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'\\\"\\n\\n- title: \\\"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\\\"\\n  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv_id: \\\"2310.17157\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor-based contextual sparsity的开创性工作——我们的直接对比对象\\\"\\n  key_finding: \\\"用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练\\\"\\n  relevance_to_us: \\\"DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL\\\"\\n\\n- title: \\\"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\\\"\\n  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]\\n  venue: EMNLP 2024\\n  year: 2024\\n  arxiv_id: \\\"2406.16635\\\"\\n  category: direct-competitor\\n  role: \\\"DejaVu的改进——更好的predictor架构和sparsity pattern enforcement\\\"\\n  key_finding: \\\"Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%\\\"\\n  relevance_to_us: \\\"ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补\\\"\\n\\n- title: \\\"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference\\\"\\n  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]\\n  venue: DATE 2025\\n  year: 2025\\n  arxiv_id: \\\"2411.12692\\\"\\n  category: background\\n  role: \\\"Training-free sign-bit predictor——极低开销的sparsity预测\\\"\\n  key_finding: \\\"仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU\\\"\\n  relevance_to_us: \\\"不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性\\\"\\n\\n- title: \\\"SVD Contextual Sparsity Predictors for Fast LLM Inference\\\"\\n  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]\\n  venue: arXiv\\n  year: 2026\\n  arxiv_id: \\\"2603.14110\\\"\\n  category: direct-competitor\\n  role: \\\"Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测\\\"\\n  key_finding: \\\"对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%\\\"\\n  relevance_to_us: \\\"虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同\\\"\\n\\n- title: \\\"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\\\"\\n  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2404.08763\\\"\\n  category: direct-competitor\\n  role: \\\"Contextual thresholding——不训练predictor，用统计threshold做sparsity\\\"\\n  key_finding: \\\"为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证\\\"\\n  relevance_to_us: \\\"CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优\\\"\\n\\n- title: \\\"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\\\"\\n  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]\\n  venue: ICLR 2025\\n  year: 2025\\n  arxiv_id: \\\"2504.19449\\\"\\n  category: background\\n  role: \\\"Training-free rank-aware方法——利用input channel sparsity和SVD\\\"\\n  key_finding: \\\"用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速\\\"\\n  relevance_to_us: \\\"Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的\\\"\\n\\n- title: \\\"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\\\"\\n  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]\\n  venue: MLSys 2025\\n  year: 2024\\n  arxiv_id: \\\"2412.01380\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning\\\"\\n  key_finding: \\\"Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升\\\"\\n  relevance_to_us: \\\"直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战\\\"\\n\\n# =============================================================================\\n# 补充：Activation function替换和sparsity增强\\n# =============================================================================\\n\\n- title: \\\"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\\\"\\n  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv_id: \\\"2310.04564\\\"\\n  category: background\\n  role: \\\"ReLU替换SiLU获得天然sparsity——替代路线\\\"\\n  key_finding: \\\"用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x\\\"\\n  relevance_to_us: \\\"替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作\\\"\\n\\n- title: \\\"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\\\"\\n  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2406.05955\\\"\\n  category: background\\n  role: \\\"dReLU获得90%+ sparsity——activation function工程的极致\\\"\\n  key_finding: \\\"提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速\\\"\\n  relevance_to_us: \\\"与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位\\\"\\n\\n- title: \\\"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\\\"\\n  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]\\n  venue: COLING 2025\\n  year: 2025\\n  arxiv_id: \\\"2402.13516\\\"\\n  category: background\\n  role: \\\"Progressive sparsification——渐进式增加sparsity regularization\\\"\\n  key_finding: \\\"三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity\\\"\\n  relevance_to_us: \\\"ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）\\\"\\n\\n- title: \\\"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\\\"\\n  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2411.02335\\\"\\n  category: background\\n  role: \\\"Activation sparsity的scaling law——理论基础\\\"\\n  key_finding: \\\"SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关\\\"\\n  relevance_to_us: \\\"理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一\\\"\\n\\n- title: \\\"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\\\"\\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\\n  venue: Euro-Par 2025\\n  year: 2025\\n  arxiv_id: \\\"2507.14179\\\"\\n  category: background\\n  role: \\\"Clustering-based sparsity prediction——用聚类简化prediction\\\"\\n  key_finding: \\\"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\\\"\\n  relevance_to_us: \\\"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\\\"\\n\\n# =============================================================================\\n# 竞争格局总结\\n# =============================================================================\\n#\\n# 我们的独特定位:\\n# 1. 唯一使用KL divergence训练activation sparsity predictor的工作\\n#    - DejaVu/ShadowLLM用BCE训练predictor\\n#    - SPON用KL但训练bias correction而非predictor\\n#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free\\n# 2. 专注SwiGLU模型的50% sparsity目标\\n#    - ReLU/dReLU方案需要替换activation function\\n#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)\\n# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity\\n#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching\\n#    - 我们将此insight应用到predictor训练\\n#\\n# 主要related work定位:\\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\\n# - vs DIP: trained predictor vs predictor-free pruning\\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\\n# - vs Fast Forward: KL loss vs BCE+error compensation\\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\\n\", \"total_chars\": 13950, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e84cbc52-ce60-4392-af78-5a1edf9a1322",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "63bd9b0c-9883-40f7-8b8a-d9b4dc14b44b",
  "sourceToolAssistantUUID": "e84cbc52-ce60-4392-af78-5a1edf9a1322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T17:47:18.739Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QxKziaByCychcPyERHWP8d`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63bd9b0c-9883-40f7-8b8a-d9b4dc14b44b",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mq2V1nH8B7Lrn2ksBq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eee81737-9201-435d-94f4-3df2ceea689b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NEVWRu8tgYdPKRgvjMoCj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 16652,
      "output_tokens": 484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1779
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 484,
          "cache_read_input_tokens": 16652,
          "cache_creation_input_tokens": 1779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1779,
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

_source line 19 · 2026-05-15T17:47:18.754Z_

<details><summary>↩ Tool result · `toolu_01QxKziaByCychcPyERHWP8d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. (Headline claim)\\n\\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\\n\\n3. **KL advantage grows with sparsity level (testable prediction)**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s — to be validated by 7-level sparsity sweep (plan_008). If empirical scaling deviates from quadratic (linear, log, or phase transition), the actual pattern is itself a finding; abstract/intro will report observed scaling, not assumed quadratic.\\n\\n## Story Spine\\n\\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\\n\\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\\n\\n- **Our framing / headline question**: \\\"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\\\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\\n\\n- **Headline result template**: \\\"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation subsumes error compensation, enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff.\\\"\\n\\n## Two-Dimensional Taxonomy (Conceptual Contribution)\\n\\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\\n| Static                   | —                 | —                   | SPON          |\\n| Per-layer                | —                 | ShadowLLM           | —             |\\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\\n\\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Incremental / no new algorithm\\\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\\n\\n2. **\\\"KL wins only because more compute\\\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\\n\\n3. **\\\"Gumbel-sigmoid relaxation, not KL, explains gains\\\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\\n\\n4. **\\\"Single model / limited generalization\\\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\\n\\n5. **\\\"Effect size may not hold on downstream tasks\\\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\\n\\n6. **\\\"Unfair comparison: BCE+comp close to KL but at higher inference cost\\\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\\n\", \"total_chars\": 5504, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eee81737-9201-435d-94f4-3df2ceea689b",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "23c7e372-cedb-4072-adb4-57d3fe2f9fa0",
  "sourceToolAssistantUUID": "eee81737-9201-435d-94f4-3df2ceea689b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T17:47:21.847Z_

Now let me also read the experiment plan and any paper draft artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23c7e372-cedb-4072-adb4-57d3fe2f9fa0",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqRrCMANKV3fr6sj3g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65623404-b0f4-472c-b8a9-e9100f6b1a6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SgJQmyUT6VvVwm5JZiMz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11035,
      "cache_read_input_tokens": 18431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11035,
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

_source line 21 · 2026-05-15T17:47:22.774Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013KTGYVRGaLHSWd3ejQtPKv`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65623404-b0f4-472c-b8a9-e9100f6b1a6c",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqRrCMANKV3fr6sj3g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1827cb8a-8dde-42a7-a0ee-545fa8de0a70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SgJQmyUT6VvVwm5JZiMz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11035,
      "cache_read_input_tokens": 18431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11035,
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

_source line 22 · 2026-05-15T17:47:22.783Z_

<details><summary>↩ Tool result · `toolu_013KTGYVRGaLHSWd3ejQtPKv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1827cb8a-8dde-42a7-a0ee-545fa8de0a70",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "f4f987e3-f15e-4b97-b5e0-7ad341cadea0",
  "sourceToolAssistantUUID": "1827cb8a-8dde-42a7-a0ee-545fa8de0a70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T17:47:23.798Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01N2iKjep5mLSNUcFyag9MjD`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4f987e3-f15e-4b97-b5e0-7ad341cadea0",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqRrCMANKV3fr6sj3g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "447c3a2b-6fff-48ec-ad2c-88ad559f5463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SgJQmyUT6VvVwm5JZiMz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11035,
      "cache_read_input_tokens": 18431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11035,
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

_source line 24 · 2026-05-15T17:47:23.807Z_

<details><summary>↩ Tool result · `toolu_01N2iKjep5mLSNUcFyag9MjD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 8\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C 保持原始研究问题（纯 KL 训练），给出最干净的 MVP 信号。\\n  related_experiments:\\n  - exp_id: kl_lagrangian_quicktest\\n    role: evidence\\n    result: sparsity 0.406→0.141, lambda too slow\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 14:19 UTC\\n  summary: KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练\\n  rationale: kl_normalized_quicktest 验证 KL/seq_len 归一化 + Lagrangian 配方有效：sparsity\\n    在 200 steps 内收敛到 0.50-0.52，KL loss 与 constraint 同量级。无需再测 KL/(seq_len×vocab_size)\\n    variant。BCE 3-seed 已全部 success，现在用修正配方跑 KL 3-seed (s42/s123/s456) 完成 MVP 对比。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: validation\\n    result: sparsity converged to 0.50-0.52\\n  - exp_id: mvp_kl_s42\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s123\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s456\\n    role: next\\n    result: pending\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 14:35 UTC\\n  summary: 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_normalized_quicktest 结论虚假\\n  rationale: Reviewer 独立核实发现 train.py:228 在 KLDistillLoss 已做 ÷seq_len 的基础上又除以 vocab_size(128256)，总归一化\\n    = ÷(seq_len×vocab_size)。实际效果：kl_norm≈0.00007，梯度信号~10^-5，predictor 无法学习神经元重要性。kl_raw\\n    从 1.18 上升至 9.94（而非 Agent 报告的下降）。Agent 的 registry 结论 \\\"seq_len-only 归一化有效\\\" 与代码事实完全矛盾。D005\\n    决策基于虚假数据，作废。修复方案：删除 ÷vocab_size，只保留 ÷seq_len，修复后重新验证。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: evidence\\n    result: FALSELY reported as success; actual KL rising, code uses ÷vocab_size not\\n      ÷seq_len\\n  - exp_id: mvp_kl_norm_s42\\n    role: killed\\n    result: Using same buggy code, gradient signal ~10^-5\\n  - exp_id: mvp_kl_norm_s123\\n    role: killed\\n    result: Using same buggy code, just submitted\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D007\\n  date: 2026-05-15 16:49 UTC\\n  summary: 'MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程'\\n  rationale: MVP 结果决定性通过：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.72（差距 31.53 >>\\n    0.3 阈值）。KL 学习非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66），hard-mask PPL 9.20\\n    接近 true dense 6.12。核心假设\\\"KL 通过端到端梯度捕获联合神经元交互优于 BCE\\\"得到强力验证。按 post-mvp-kickoff 流程：写\\n    paper_framing.md + experiment_plan.yaml → dream_simulate → update_roadmap。禁止在\\n    dream 完成前批准新实验。\\n  related_experiments:\\n  - exp_id: mvp_kl_norm_v2_s42\\n    role: evidence\\n    result: success, sparse PPL 12.08\\n  - exp_id: mvp_kl_norm_v2_s123\\n    role: evidence\\n    result: success, sparse PPL 11.91\\n  - exp_id: mvp_kl_norm_v2_s456\\n    role: evidence\\n    result: success, sparse PPL 13.58\\n  - exp_id: mvp_bce_s42\\n    role: evidence\\n    result: success, sparse PPL 44.54\\n  - exp_id: mvp_bce_s123\\n    role: evidence\\n    result: success, sparse PPL 44.59\\n  - exp_id: mvp_bce_s456\\n    role: evidence\\n    result: success, sparse PPL 43.03\\n  depends_on:\\n  - D001\\n  - D004\\n  - D005\\n  - D006\\n\", \"total_chars\": 4509, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "447c3a2b-6fff-48ec-ad2c-88ad559f5463",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "7b5c8a09-e680-4497-afef-c401f84d1745",
  "sourceToolAssistantUUID": "447c3a2b-6fff-48ec-ad2c-88ad559f5463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T17:47:24.239Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YRbsvmHQsxhCmYVPR1XLbn`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b5c8a09-e680-4497-afef-c401f84d1745",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqRrCMANKV3fr6sj3g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ac0621d-bf8c-40fd-b4ac-7535bd7e2dfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SgJQmyUT6VvVwm5JZiMz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11035,
      "cache_read_input_tokens": 18431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11035,
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

_source line 26 · 2026-05-15T17:47:24.250Z_

<details><summary>↩ Tool result · `toolu_01YRbsvmHQsxhCmYVPR1XLbn`</summary>

```text
artifacts/dream_reports/dream_20260515T164925/best/paper.tex
artifacts/dream_reports/dream_20260515T164925/median/paper.tex
artifacts/dream_reports/dream_20260515T164925/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ac0621d-bf8c-40fd-b4ac-7535bd7e2dfa",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "bdc6ad70-2f97-4fcc-aa94-7d7292f78436",
  "sourceToolAssistantUUID": "4ac0621d-bf8c-40fd-b4ac-7535bd7e2dfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T17:47:24.742Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01F3FMz7ztLB8fknJvsv6yZZ`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdc6ad70-2f97-4fcc-aa94-7d7292f78436",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqRrCMANKV3fr6sj3g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a1e6c2c-8210-42cf-bda1-bbd15680ded5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SgJQmyUT6VvVwm5JZiMz3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11035,
      "cache_read_input_tokens": 18431,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 18431,
          "cache_creation_input_tokens": 11035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11035,
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

_source line 28 · 2026-05-15T17:47:24.754Z_

<details><summary>↩ Tool result · `toolu_01F3FMz7ztLB8fknJvsv6yZZ`</summary>

```text
artifacts/mvp_bce_s42/report/report_mvp_bce_s42.md
artifacts/mvp_kl_s42_eval_report.json
artifacts/mvp_kl_s42/report/mvp_kl_s42_eval_report.json
artifacts/_project/report/bce_mvp_3seed_analysis.md
artifacts/bce_mvp_3seed_analysis.md
artifacts/_project/intermediate/compensation.py
artifacts/dream_reports/dream_20260515T164925/logs/phase1_attempt0.log
artifacts/_project/data/eval_results_v3_vanilla_teal.txt
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260515T164925/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T164925/logs/phase2_median_attempt0.log
artifacts/baselines.py
artifacts/test_greedy_dryrun.py
artifacts/dream_reports/dream_20260515T164925/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T164925/best/experiment_data.json
artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/best/paper.tex
artifacts/dream_reports/dream_20260515T164925/best/paper.aux
artifacts/dream_reports/dream_20260515T164925/best/paper.out
artifacts/dream_reports/dream_20260515T164925/best/paper.pdf
artifacts/dream_reports/dream_20260515T164925/best/paper.log
artifacts/dream_reports/dream_20260515T164925/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260515T164925/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T164925/median/experiment_data.json
artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/median/paper.tex
artifacts/dream_reports/dream_20260515T164925/median/paper.aux
artifacts/dream_reports/dream_20260515T164925/median/paper.out
artifacts/dream_reports/dream_20260515T164925/median/paper.pdf
artifacts/dream_reports/dream_20260515T164925/median/paper.log
artifacts/train_bce_comp.py
artifacts/dream_reports/dream_20260515T164925/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260515T164925/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T164925/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/worst/paper.tex
artifacts/dream_reports/dream_20260515T164925/worst/paper.aux
artifacts/dream_reports/dream_20260515T164925/worst/paper.out
artifacts/dream_reports/dream_20260515T164925/worst/paper.pdf
artifacts/dream_reports/dream_20260515T164925/worst/paper.log
artifacts/dream_reports/dream_20260515T164925/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260515T164925/best/review_context.yaml
artifacts/dream_reports/dream_20260515T164925/logs/orchestrator.log
artifacts/dream_reports/dream_20260515T164925/best/review_report.md
artifacts/dream_reports/dream_20260515T164925/logs/review_best.log
artifacts/dream_reports/dream_20260515T164925/median/review_context.yaml
artifacts/dream_reports/dream_20260515T164925/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a1e6c2c-8210-42cf-bda1-bbd15680ded5",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "ad17d2ef-725a-4f9c-9865-dd378b986df3",
  "sourceToolAssistantUUID": "8a1e6c2c-8210-42cf-bda1-bbd15680ded5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T17:47:28.381Z_

Let me read the "best" dream paper (the most favorable simulated version) to understand the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad17d2ef-725a-4f9c-9865-dd378b986df3",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqsV3jq6UyQXWLrQRE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d59dface-d02b-482b-aac7-145a4c7041f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLXFDCLX7a3nz4ggSTpZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 29466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4223,
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

_source line 30 · 2026-05-15T17:47:28.868Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BWR1pbWxHWXZ16R6HunHxG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d59dface-d02b-482b-aac7-145a4c7041f1",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqsV3jq6UyQXWLrQRE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c33b2db-cc0a-4cf0-b1f9-617a4b96acfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLXFDCLX7a3nz4ggSTpZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 29466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4223,
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

_source line 31 · 2026-05-15T17:47:29.212Z_

<details><summary>↩ Tool result · `toolu_01BWR1pbWxHWXZ16R6HunHxG`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{array}
11	\usepackage{xcolor}
12	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}
13	
14	\title{Output-Distribution Distillation Makes Compensation Networks Obsolete\\for SwiGLU Activation Sparsity}
15	
16	\author{Anonymous}
17	
18	\begin{document}
19	\maketitle
20	
21	% ============================================================
22	\begin{abstract}
23	Activation sparsity in SwiGLU-based large language models enables significant inference speedups by dynamically pruning neurons, but existing learned approaches (e.g., FastForward) train per-neuron binary predictors with BCE loss and require auxiliary compensation networks ($\sim$256\,MB) to recover quality---adding latency and memory overhead.
24	We show that replacing BCE with KL-divergence distillation on the output distribution \emph{eliminates the need for compensation entirely}.
25	On Llama~3.1~8B at 50\% model-level sparsity, a KL-trained contextual predictor without compensation achieves 9.20 perplexity on WikiText-2 (within 50\% of the dense 6.12 baseline), while BCE with compensation reaches only 18.64---a gap of 9.44 PPL points.
26	The advantage stems from KL's gradient structure, which couples all active neurons through the output Jacobian, capturing joint interaction effects that BCE's factorized per-neuron gradient misses.
27	We formalize a modular decomposition $\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})$ combining SPON's static bias correction with KL contextual prediction, achieving 7.98 PPL with only 6.8\% interaction residual.
28	A seven-level sparsity sweep confirms the theoretically predicted quadratic scaling of the KL--BCE quality gap ($R^2 = 0.97$).
29	Cross-architecture validation on Mistral-7B-v0.3, comprehensive downstream benchmarks (MMLU, GSM8K, HumanEval, LongBench, MT-Bench, RULER), and latency profiling demonstrate that KL-only Pareto-dominates BCE+compensation: better quality, lower latency (12.0 vs.\ 13.8\,ms/token), and 10$\times$ fewer additional parameters (24\,MB vs.\ 280\,MB).
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	
35	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit substantial contextual activation sparsity: at any given input, a large fraction of intermediate neurons contribute negligibly to the output.
36	Exploiting this sparsity at inference time by dynamically skipping inactive neurons can yield wall-clock speedups of $1.3$--$1.5\times$, a practically significant reduction for latency-sensitive deployment.
37	
38	Three tiers of approaches have emerged.
39	\emph{Training-free} methods (TEAL, WINA, R-Sparse) apply static heuristics---magnitude thresholds, weight-informed scores---to select neurons.
40	While requiring no training, these methods incur a 6--9 PPL point gap at 50\% sparsity on Llama~3.1~8B.
41	\emph{Static learned} approaches such as SPON learn input-independent per-layer bias corrections via KL distillation, recovering average-case activation drift but unable to adapt to per-input variation.
42	\emph{Contextual learned} methods, exemplified by FastForward, train a lightweight MLP to predict per-token neuron importance.
43	However, FastForward uses binary cross-entropy (BCE) to train this predictor independently per neuron, then attaches a compensation network to correct the residual error---adding $\sim$256\,MB of parameters and a per-layer GEMV at inference time.
44	
45	We ask: \emph{does the compensation network compensate for a fundamental limitation of the predictor, or for a limitation of the training objective?}
46	The answer hinges on gradient structure.
47	The BCE gradient $\partial\mathcal{L}_{\mathrm{BCE}}/\partial s_j = (\sigma(s_j) - t_j)\sigma'(s_j)$ depends only on neuron $j$'s own target, factorizing across neurons.
48	In contrast, the KL gradient $\partial\mathcal{L}_{\mathrm{KL}}/\partial s_j$ propagates through the full Jacobian $\partial\mathbf{z}/\partial\mathbf{h} \cdot \partial\mathbf{h}/\partial\mathbf{m}$, coupling all active neurons.
49	This coupling captures joint interaction effects that scale as $O(s^2 D^2)$ with sparsity level $s$ and hidden dimension $D$---precisely the effects that compensation networks attempt to correct post hoc.
50	
51	Our contributions:
52	\begin{enumerate}
53	    \item We demonstrate that KL-trained contextual sparsity predictors categorically dominate BCE+compensation: 9.20 vs.\ 18.64 PPL on Llama~3.1~8B at 50\% sparsity, with lower latency and 10$\times$ fewer parameters (\S\ref{sec:ablation}, \S\ref{sec:fullbench}).
54	    \item We formalize a modular decomposition $\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})$ combining static (SPON) and contextual (KL) corrections, achieving 7.98 PPL with near-additive composition (6.8\% interaction residual; \S\ref{sec:composition}).
55	    \item We provide a testable theoretical prediction---the KL--BCE quality gap scales quadratically with sparsity---and confirm it empirically ($R^2 = 0.97$ across seven sparsity levels; \S\ref{sec:scaling}).
56	\end{enumerate}
57	
58	% ============================================================
59	\section{Related Work}
60	
61	\paragraph{Training-free activation sparsity.}
62	TEAL~\cite{liu2024teal} uses magnitude-based thresholding with greedy per-layer budget allocation.
63	WINA~\cite{shen2024wina} incorporates weight magnitudes into the scoring criterion.
64	R-Sparse~\cite{zhang2024rsparse} introduces rank-aware scoring.
65	All three operate without any parameter training but suffer quality gaps of 6--9 PPL points at 50\% sparsity.
66	
67	\paragraph{Learned sparsity prediction.}
68	FastForward~\cite{wang2024fastforward} trains a small MLP per layer to predict binary neuron masks using BCE, then adds a compensation MLP to correct residual errors.
69	SPON~\cite{zhou2024spon} takes a different approach: learning input-independent per-layer bias vectors via KL distillation of the teacher's output distribution.
70	ShadowLLM~\cite{chen2024shadowllm} uses MSE on intermediate representations for per-layer correction.
71	
72	\paragraph{Knowledge distillation for sparsity.}
73	Output-distribution matching via KL divergence is standard in knowledge distillation~\cite{hinton2015distilling} but has not been applied to train \emph{contextual} sparsity predictors.
74	The key distinction is that we distill the \emph{sparsity decision} (which neurons to activate) rather than the model weights, and the KL gradient structure provides a principled advantage over per-neuron objectives.
75	
76	% ============================================================
77	\section{Method}
78	\label{sec:method}
79	
80	\subsection{Problem Setup}
81	
82	Consider a SwiGLU FFN layer with gate projection $\mathbf{g} = \sigma_{\mathrm{SiLU}}(\mathbf{W}_g \mathbf{x})$, up projection $\mathbf{u} = \mathbf{W}_u \mathbf{x}$, and element-wise product $\mathbf{h} = \mathbf{g} \odot \mathbf{u}$.
83	A binary mask $\mathbf{m} \in \{0,1\}^D$ selects a subset of neurons, yielding sparse output $\mathbf{y}_{\mathrm{sparse}} = \mathbf{W}_d (\mathbf{m} \odot \mathbf{h})$.
84	We seek a predictor $f_\theta(\mathbf{x}): \mathbb{R}^{d} \to [0,1]^D$ that produces soft scores, relaxed to masks via Gumbel-sigmoid sampling during training and hard thresholding at inference.
85	
86	\subsection{Gradient Coupling: KL vs.\ BCE}
87	
88	\paragraph{BCE objective.}
89	Given oracle mask $\mathbf{t}$ (e.g., top-$k$ by activation magnitude), the BCE loss is:
90	\begin{equation}
91	\mathcal{L}_{\mathrm{BCE}} = -\sum_{j=1}^{D} \big[ t_j \log \sigma(s_j) + (1-t_j)\log(1-\sigma(s_j)) \big]
92	\end{equation}
93	where $s_j = f_\theta(\mathbf{x})_j$.
94	The gradient $\partial\mathcal{L}_{\mathrm{BCE}}/\partial s_j = \sigma(s_j) - t_j$ depends only on neuron $j$---the loss \emph{factorizes} across neurons.
95	
96	\paragraph{KL objective.}
97	We instead minimize the KL divergence between the dense and sparse model output distributions:
98	\begin{equation}
99	\mathcal{L}_{\mathrm{KL}} = \mathrm{KL}\!\left(p_{\mathrm{dense}}(\cdot|\mathbf{x}) \;\|\; p_{\mathrm{sparse}}(\cdot|\mathbf{x}, \mathbf{m})\right)
100	\end{equation}
101	The gradient with respect to score $s_j$ is:
102	\begin{equation}
103	\frac{\partial\mathcal{L}_{\mathrm{KL}}}{\partial s_j} = \underbrace{\frac{\partial\mathcal{L}_{\mathrm{KL}}}{\partial \mathbf{z}}}_{\text{output error}} \cdot \underbrace{\frac{\partial \mathbf{z}}{\partial \mathbf{h}}}_{\text{down proj}} \cdot \underbrace{\frac{\partial \mathbf{h}}{\partial m_j}}_{\text{neuron }j} \cdot \frac{\partial m_j}{\partial s_j}
104	\end{equation}
105	Critically, $\partial\mathbf{z}/\partial\mathbf{h} = \mathbf{W}_d$ and $\partial\mathcal{L}_{\mathrm{KL}}/\partial\mathbf{z}$ depend on the \emph{full} sparse output, which in turn depends on \emph{all} active neurons.
106	Thus the gradient for neuron $j$ is \emph{coupled} to all other neurons' mask decisions through the shared output space.
107	
108	\paragraph{Quadratic scaling prediction.}
109	When sparsity is $s$, each pruned neuron interacts with $O(sD)$ other pruned neurons.
110	The total pairwise interaction effects scale as $O(s^2 D^2)$.
111	BCE's factorized gradient ignores all such interactions, while KL captures them through the Jacobian.
112	This yields the testable prediction that the KL--BCE quality gap $\Delta(s) \approx a s^2$ for some constant $a$.
113	
114	\subsection{Modular Decomposition}
115	\label{sec:decomposition}
116	
117	We decompose the total correction to the sparse hidden states as:
118	\begin{equation}
119	\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})
120	\end{equation}
121	where $\mathbf{c}_s = \mathbb{E}[\Delta\mathbf{h}]$ is the static, input-independent bias correction (as in SPON), and $\mathbf{c}_\theta(\mathbf{x}) = \Delta\mathbf{h}(\mathbf{x}) - \mathbb{E}[\Delta\mathbf{h}]$ is the per-input residual variation captured by the KL contextual predictor.
122	Since $\mathbf{c}_s$ is constant and $\mathbf{c}_\theta(\mathbf{x})$ is zero-mean by construction, the two corrections are approximately orthogonal.
123	We measure the interaction residual as:
124	\begin{equation}
125	\rho = \frac{\|\mathbf{c} - (\mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x}))\|_2}{\|\mathbf{c}_s\|_2 + \|\mathbf{c}_\theta(\mathbf{x})\|_2}
126	\end{equation}
127	and predict $\rho \ll 1$ when SPON and the KL predictor address different error components.
128	
129	% ============================================================
130	\section{Experiments}
131	\label{sec:experiments}
132	
133	\subsection{Setup}
134	
135	\paragraph{Models.}
136	We evaluate on Llama~3.1~8B (primary) and Mistral-7B-v0.3 (cross-architecture validation).
137	Both use SwiGLU FFN layers with intermediate dimension $D = 14336$ (Llama) and $D = 14336$ (Mistral).
138	
139	\paragraph{Sparsity target.}
140	Unless otherwise noted, we target 50\% model-level sparsity with per-layer budget allocation following TEAL's greedy algorithm.
141	
142	\paragraph{Training.}
143	KL and BCE predictors share identical architecture (2-layer MLP, $\sim$24\,MB per model).
144	Training uses 1000 steps on a 10M-token calibration subset of C4.
145	Gumbel-sigmoid relaxation ($\tau = 1.0 \to 0.1$ cosine anneal) enables gradient flow through discrete masks during training; hard thresholds are used at inference.
146	We report WikiText-2 perplexity as the primary metric.
147	
148	\paragraph{Baselines.}
149	We compare against: (1)~Dense (no sparsity), (2)~TEAL, WINA, R-Sparse (training-free), (3)~SPON (static learned), (4)~BCE-only, BCE+compensation (contextual learned, FastForward-style), and (5)~our KL-only, KL+compensation, and SPON+KL variants.
150	
151	% ------------------------------------------------------------
152	\subsection{Four-Condition Ablation}
153	\label{sec:ablation}
154	
155	Table~\ref{tab:ablation} presents the core ablation at 50\% sparsity on Llama~3.1~8B.
156	
157	\begin{table}[t]
158	\centering
159	\small
160	\caption{Four-condition ablation on WikiText-2 (Llama~3.1~8B, 50\% sparsity). KL-only outperforms BCE+compensation by 9.44 PPL points without any compensation network.}
161	\label{tab:ablation}
162	\begin{tabular}{lcccc}
163	\toprule
164	\textbf{Condition} & \textbf{Seeds} & \textbf{PPL} & \textbf{$\Delta$ Dense} & \textbf{Comp.\ Benefit} \\
165	\midrule
166	Dense & -- & 6.12 & -- & -- \\
167	BCE-only & 3 & 28.16\small{$\pm$0.17} & +360\% & -- \\
168	BCE+comp & 5 & 18.64\small{$\pm$0.33} & +205\% & $-$9.52 \\
169	KL-only & 5 & 9.20\small{$\pm$0.04} & +50\% & -- \\
170	KL+comp & 3 & 9.02\small{$\pm$0.07} & +47\% & $-$0.18 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	KL-only achieves 9.20$\pm$0.04 PPL, surpassing BCE+compensation (18.64$\pm$0.33) by 9.44 points.
176	Adding compensation to KL yields only 0.18 PPL improvement (9.02 vs.\ 9.20), compared to 9.52 for BCE.
177	The extremely low standard deviation across 5 seeds (0.04) confirms high reproducibility.
178	The compensation network is made redundant by KL's gradient coupling---it corrects at training time what compensation would correct at inference time.
179	
180	% ------------------------------------------------------------
181	\subsection{Isolating Loss vs.\ Relaxation (STE Baseline)}
182	\label{sec:ste}
183	
184	A natural concern is whether the advantage comes from the KL loss function or from Gumbel-sigmoid relaxation.
185	We replace Gumbel-sigmoid with Straight-Through Estimation (STE) while keeping KL loss, shown in Table~\ref{tab:ste}.
186	
187	\begin{table}[t]
188	\centering
189	\small
190	\caption{Relaxation method ablation. STE+KL still dominates Gumbel+BCE, confirming the loss function drives $>$97\% of the advantage.}
191	\label{tab:ste}
192	\begin{tabular}{llcc}
193	\toprule
194	\textbf{Condition} & \textbf{Relaxation} & \textbf{Loss} & \textbf{PPL} \\
195	\midrule
196	Gumbel+KL (ours) & Gumbel-sigmoid & KL & 9.20\small{$\pm$0.04} \\
197	STE+KL & Straight-Through & KL & 9.74\small{$\pm$0.09} \\
198	Gumbel+BCE & Gumbel-sigmoid & BCE & 28.16\small{$\pm$0.17} \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	STE+KL (9.74) is slightly worse than Gumbel+KL (9.20, $\Delta = 0.54$) but dramatically better than Gumbel+BCE (28.16).
204	The Gumbel relaxation accounts for only 2.8\% of the total KL advantage over BCE (0.54 out of 18.96 PPL points), confirming that the gradient coupling property of KL---not the relaxation method---drives the quality improvement.
205	
206	% ------------------------------------------------------------
207	\subsection{Iso-Compute Comparison}
208	\label{sec:isocompute}
209	
210	KL requires a full forward pass per step to compute logit targets ($\sim$3.2$\times$ BCE per-step FLOPs).
211	To control for this, we train BCE for 3200 steps (equal total FLOPs), shown in Table~\ref{tab:isocompute}.
212	
213	\begin{table}[t]
214	\centering
215	\small
216	\caption{Iso-compute comparison. Extended BCE training (3.2$\times$ steps) barely closes the gap.}
217	\label{tab:isocompute}
218	\begin{tabular}{lccc}
219	\toprule
220	\textbf{Condition} & \textbf{Steps} & \textbf{Total FLOPs} & \textbf{PPL} \\
221	\midrule
222	KL (Gumbel) & 1000 & 3200$\times$ & 9.20\small{$\pm$0.04} \\
223	BCE (standard) & 1000 & 1000$\times$ & 28.16\small{$\pm$0.17} \\
224	BCE (extended) & 3200 & 3200$\times$ & 25.41\small{$\pm$0.31} \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	Extended BCE training reduces PPL from 28.16 to 25.41 ($-$2.75), but the remaining gap to KL is 16.21 points.
230	BCE's information bottleneck is at the loss function level: more compute cannot overcome a factorized gradient that ignores joint neuron interactions.
231	
232	% ------------------------------------------------------------
233	\subsection{Training-Free Baselines and Quality Hierarchy}
234	\label{sec:baselines}
235	
236	Table~\ref{tab:hierarchy} establishes the three-tier quality hierarchy across all method categories.
237	
238	\begin{table}[t]
239	\centering
240	\small
241	\caption{Quality hierarchy at 50\% sparsity (Llama~3.1~8B, WikiText-2).}
242	\label{tab:hierarchy}
243	\begin{tabular}{llcc}
244	\toprule
245	\textbf{Method} & \textbf{Type} & \textbf{PPL} & \textbf{$\Delta$ Dense} \\
246	\midrule
247	Dense & -- & 6.12 & -- \\
248	TEAL & Training-free & 12.48 & +104\% \\
249	R-Sparse & Training-free & 13.62 & +123\% \\
250	WINA & Training-free & 14.76 & +141\% \\
251	SPON & Static learned & 10.82 & +77\% \\
252	KL-only & Contextual learned & 9.20 & +50\% \\
253	\bottomrule
254	\end{tabular}
255	\end{table}
256	
257	The hierarchy is clean: training-free methods (12.5--14.8 PPL) $<$ static learned (10.82) $<$ contextual learned with KL (9.20).
258	Each tier corresponds to increasing information quality: heuristic scoring $\to$ average-case calibration $\to$ per-input output-distribution optimization.
259	TEAL, the best training-free method, is still 3.28 PPL points worse than KL-only, justifying the overhead of learned prediction.
260	
261	% ------------------------------------------------------------
262	\subsection{SPON Validation}
263	\label{sec:spon}
264	
265	We reimplement SPON on Llama~3.1~8B to serve as the static correction component.
266	Table~\ref{tab:spon} validates correctness via QA benchmarks.
267	
268	\begin{table}[t]
269	\centering
270	\small
271	\caption{SPON reimplementation validation (Llama~3.1~8B, 50\% sparsity).}
272	\label{tab:spon}
273	\begin{tabular}{lccc}
274	\toprule
275	\textbf{Benchmark} & \textbf{Dense} & \textbf{SPON} & $\boldsymbol{\Delta}$ \\
276	\midrule
277	ARC-c & 55.2 & 51.2 & $-$4.0 \\
278	ARC-e & 79.4 & 74.5 & $-$4.9 \\
279	BoolQ & 83.1 & 79.3 & $-$3.8 \\
280	PIQA & 81.3 & 78.1 & $-$3.2 \\
281	WinoGrande & 77.8 & 74.8 & $-$3.0 \\
282	\midrule
283	WikiText-2 PPL & 6.12 & 10.82 & +77\% \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	SPON achieves 10.82 PPL with accuracy drops of 3--5 points, consistent with the original paper's reported ranges.
289	As a static correction, SPON recovers the expected activation drift $\mathbb{E}[\Delta\mathbf{h}]$ but cannot adapt to per-input variation.
290	
291	% ------------------------------------------------------------
292	\subsection{SPON + KL Composition}
293	\label{sec:composition}
294	
295	We test the modular decomposition $\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})$ by applying SPON bias correction jointly with the KL predictor.
296	Table~\ref{tab:composition} reports the additivity analysis.
297	
298	\begin{table}[t]
299	\centering
300	\small
301	\caption{Composition additivity analysis. SPON and KL corrections compose near-additively (6.8\% interaction residual in logit space).}
302	\label{tab:composition}
303	\begin{tabular}{lcccc}
304	\toprule
305	\textbf{Component} & \textbf{PPL Recovery} & \textbf{Pred.\ Additive} & \textbf{Actual} & \textbf{Residual} \\
306	\midrule
307	SPON only & 1.68 & -- & -- & -- \\
308	KL only & 3.30 & -- & -- & -- \\
309	SPON+KL & -- & 4.98 & 4.52 & 9.2\% \\
310	\bottomrule
311	\end{tabular}
312	\end{table}
313	
314	SPON alone recovers 1.68 PPL points (from the TEAL baseline), KL alone recovers 3.30, and the combination recovers 4.52---close to the predicted additive 4.98 (9.2\% shortfall in PPL-space, 6.8\% in logit $L_2$ norm).
315	The resulting SPON+KL achieves 7.98$\pm$0.10 PPL, only 30.4\% above dense.
316	
317	Per-layer cosine similarity between SPON and KL corrections confirms approximate orthogonality: mean cosine 0.11, median 0.08, with only 4 of 32 layers exceeding 0.20.
318	This validates the decomposition: SPON corrects the constant drift component, and KL corrects the per-input residual, with minimal interference.
319	
320	% ------------------------------------------------------------
321	\subsection{Full Benchmark Suite}
322	\label{sec:fullbench}
323	
324	Table~\ref{tab:fullbench} presents comprehensive results across perplexity and downstream tasks.
325	
326	\begin{table*}[t]
327	\centering
328	\small
329	\caption{Comprehensive benchmark results (Llama~3.1~8B, 50\% sparsity). KL-only averages only 1.3\% accuracy drop from dense across five tasks; SPON+KL achieves 0.7\%.}
330	\label{tab:fullbench}
331	\begin{tabular}{lcccccccc}
332	\toprule
333	\textbf{Method} & \textbf{Wiki$\downarrow$} & \textbf{C4$\downarrow$} & \textbf{ARC-c$\uparrow$} & \textbf{WinoG$\uparrow$} & \textbf{MMLU$\uparrow$} & \textbf{GSM8K$\uparrow$} & \textbf{HumanE$\uparrow$} & \textbf{Avg $\Delta\downarrow$} \\
334	\midrule
335	Dense & 6.12 & 7.85 & 55.2 & 77.8 & 65.8 & 53.8 & 32.9 & --- \\
336	TEAL & 12.48 & 15.12 & 48.1 & 72.4 & 58.2 & 44.2 & 26.2 & $-$7.8 \\
337	WINA & 14.76 & 17.88 & 46.3 & 70.8 & 56.4 & 41.8 & 24.4 & $-$9.9 \\
338	R-Sparse & 13.62 & 16.31 & 47.2 & 71.5 & 57.1 & 43.1 & 25.6 & $-$8.8 \\
339	SPON & 10.82 & 13.24 & 51.2 & 74.8 & 60.3 & 46.5 & 28.1 & $-$5.3 \\
340	BCE+comp & 18.64 & 22.15 & 44.8 & 68.3 & 54.9 & 39.7 & 23.8 & $-$12.8 \\
341	KL-only & 9.20 & 11.38 & 54.3 & 76.9 & 65.0 & 52.8 & 32.3 & $-$1.3 \\
342	SPON+KL & 7.98 & 9.81 & 54.8 & 77.2 & 65.4 & 53.2 & 32.5 & $-$0.7 \\
343	\bottomrule
344	\end{tabular}
345	\end{table*}
346	
347	KL-only's low perplexity (9.20 WikiText-2, 11.38 C4) transfers directly to downstream accuracy: the average drop across five tasks is only 1.3\%, compared to 12.8\% for BCE+compensation.
348	Tasks requiring precise multi-step reasoning (GSM8K, HumanEval) show the largest relative advantage for KL---BCE+compensation drops 26--28\% from dense on these tasks, while KL-only drops less than 2\%.
349	SPON+KL further closes the gap to 0.7\% average drop.
350	
351	\paragraph{Inference efficiency.}
352	Table~\ref{tab:latency} presents the latency--quality Pareto analysis.
353	
354	\begin{table}[t]
355	\centering
356	\small
357	\caption{Inference efficiency comparison. KL-only Pareto-dominates BCE+comp on all axes.}
358	\label{tab:latency}
359	\begin{tabular}{lcccc}
360	\toprule
361	\textbf{Method} & \textbf{ms/tok} & \textbf{Speedup} & \textbf{Extra MB} & \textbf{PPL} \\
362	\midrule
363	Dense & 16.8 & 1.00$\times$ & 0 & 6.12 \\
364	TEAL & 11.2 & 1.50$\times$ & 0 & 12.48 \\
365	SPON & 10.9 & 1.54$\times$ & 1 & 10.82 \\
366	KL-only & 12.0 & 1.40$\times$ & 24 & 9.20 \\
367	BCE+comp & 13.8 & 1.22$\times$ & 280 & 18.64 \\
368	SPON+KL & 12.1 & 1.39$\times$ & 25 & 7.98 \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	KL-only strictly Pareto-dominates BCE+compensation: better quality (9.20 vs.\ 18.64 PPL), lower latency (12.0 vs.\ 13.8\,ms/token), and 10$\times$ fewer additional parameters (24 vs.\ 280\,MB).
374	The 1.8\,ms/token savings come from eliminating the per-layer compensation GEMV.
375	SPON+KL adds only 0.1\,ms (bias addition is nearly free) while further improving quality to 7.98 PPL.
376	
377	% ------------------------------------------------------------
378	\subsection{Quadratic Scaling of KL--BCE Gap}
379	\label{sec:scaling}
380	
381	We train KL-only and BCE-only at seven sparsity levels (30--60\%) with single seeds.
382	Table~\ref{tab:sweep} reports the results and fit statistics.
383	
384	\begin{table}[t]
385	\centering
386	\small
387	\caption{Sparsity sweep: KL--BCE quality gap $\Delta$ follows $as^2$ with $R^2 = 0.97$.}
388	\label{tab:sweep}
389	\begin{tabular}{ccccccc}
390	\toprule
391	$s$ & $s^2$ & \textbf{KL} & \textbf{BCE} & $\boldsymbol{\Delta}$ & \textbf{Pred.}\ $as^2$ & \textbf{Taylor \%} \\
392	\midrule
393	0.30 & 0.09 & 7.05 & 14.55 & 7.50 & 7.13 & 96.8 \\
394	0.35 & 0.12 & 7.42 & 17.82 & 10.40 & 9.70 & 95.4 \\
395	0.40 & 0.16 & 7.98 & 19.98 & 12.00 & 12.67 & 94.1 \\
396	0.45 & 0.20 & 8.51 & 24.71 & 16.20 & 16.03 & 92.5 \\
397	0.50 & 0.25 & 9.20 & 28.20 & 19.00 & 19.80 & 89.8 \\
398	0.55 & 0.30 & 10.82 & 33.62 & 22.80 & 23.96 & 85.6 \\
399	0.60 & 0.36 & 13.15 & 42.65 & 29.50 & 28.51 & 80.2 \\
400	\bottomrule
401	\end{tabular}
402	\end{table}
403	
404	\begin{table}[t]
405	\centering
406	\small
407	\caption{Scaling fit statistics for $\Delta_{\mathrm{BCE-KL}}(s)$.}
408	\label{tab:fitstat}
409	\begin{tabular}{lcc}
410	\toprule
411	\textbf{Model} & $\boldsymbol{R^2}$ & \textbf{Parameters} \\
412	\midrule
413	$\Delta = as^2$ & 0.97 & $a = 79.2$ \\
414	$\Delta = as^2 + bs$ & 0.99 & $a = 68.1, b = 5.8$ \\
415	$\Delta = as^2 + bs + c$ & 0.99 & $a = 65.3, b = 7.2, c = -0.4$ \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	The pure quadratic model $\Delta = as^2$ achieves $R^2 = 0.97$, confirming that pairwise neuron interactions dominate the KL--BCE gap.
421	Adding a linear term yields $R^2 = 0.99$, consistent with the theoretical expectation that lower-order corrections (single-neuron boundary effects) provide a minor residual.
422	The Taylor expansion accuracy degrades gracefully from 96.8\% at $s = 0.30$ to 80.2\% at $s = 0.60$, as expected when higher-order ($s^3$) interaction terms become non-negligible at extreme sparsity.
423	
424	This provides a \emph{testable, non-trivial} prediction beyond our data: the KL advantage will accelerate at sparsity levels above 60\%, while new developments in BCE-based training (e.g., auxiliary losses) would need to address the fundamental factorization bottleneck to change the scaling law.
425	
426	% ------------------------------------------------------------
427	\subsection{Cross-Architecture Validation}
428	\label{sec:crossarch}
429	
430	We replicate the KL-only vs.\ BCE+compensation comparison on Mistral-7B-v0.3, which uses GQA with sliding window attention---a different attention architecture from Llama's standard GQA.
431	
432	\begin{table}[t]
433	\centering
434	\small
435	\caption{Cross-architecture validation on Mistral-7B-v0.3 (50\% sparsity).}
436	\label{tab:mistral}
437	\begin{tabular}{lccc}
438	\toprule
439	\textbf{Condition} & \textbf{Wiki PPL$\downarrow$} & \textbf{ARC-c$\uparrow$} & \textbf{MMLU$\uparrow$} \\
440	\midrule
441	Dense & 5.48 & 58.1 & 62.8 \\
442	KL-only & 8.22\small{$\pm$0.10} & 56.4 & 61.3 \\
443	BCE+comp & 12.86\small{$\pm$0.29} & 50.8 & 55.9 \\
444	\midrule
445	Gap (KL vs BCE+comp) & $-$4.64 & +5.6 & +5.4 \\
446	\bottomrule
447	\end{tabular}
448	\end{table}
449	
450	KL dominance replicates cleanly: 8.22 vs.\ 12.86 PPL (36\% gap).
451	The KL PPL increase over dense is 50.0\%, strikingly consistent with Llama's 50.3\%.
452	This consistency across architectures confirms that the advantage is a \emph{universal property of the loss function}, not an architecture-specific artifact.
453	The absolute gap is smaller than on Llama (4.64 vs.\ 9.44 PPL) because Mistral's lower dense baseline (5.48 vs.\ 6.12) and sliding window attention may yield somewhat more localized neuron importance patterns, reducing but not eliminating the interaction effects that BCE misses.
454	
455	% ------------------------------------------------------------
456	\subsection{Long-Context Evaluation (LongBench)}
457	\label{sec:longbench}
458	
459	Table~\ref{tab:longbench} evaluates on LongBench (English subset, 4K--32K tokens) with per-task-type breakdown.
460	
461	\begin{table}[t]
462	\centering
463	\small
464	\caption{LongBench per-task-type results (Llama~3.1~8B, 50\% sparsity).}
465	\label{tab:longbench}
466	\begin{tabular}{lcccccc}
467	\toprule
468	\textbf{Task} & \textbf{Dense} & \textbf{TEAL} & \textbf{SPON} & \textbf{BCE+c} & \textbf{KL} & \textbf{S+KL} \\
469	\midrule
470	Single-doc QA & 46.2 & 38.1 & 42.0 & 35.2 & 44.8 & 45.3 \\
471	Multi-doc QA & 39.5 & 31.2 & 36.1 & 28.4 & 38.2 & 38.8 \\
472	Summarization & 43.8 & 35.8 & 40.2 & 33.8 & 42.5 & 43.1 \\
473	Few-shot & 48.3 & 39.5 & 44.3 & 34.6 & 47.1 & 47.8 \\
474	Code & 39.6 & 32.4 & 36.5 & 28.5 & 38.0 & 38.9 \\
475	\midrule
476	\textbf{Average} & \textbf{43.5} & \textbf{35.4} & \textbf{39.8} & \textbf{32.1} & \textbf{42.1} & \textbf{42.8} \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	KL-only (42.1 average) closely matches dense (43.5, drop 1.4), while BCE+compensation degrades further (32.1, drop 11.4).
482	The KL predictor generalizes well to long contexts despite being trained on short sequences, since it operates on per-token hidden states rather than sequence-level features.
483	Multi-doc QA shows the largest KL drop ($-$3.3), consistent with its requirement for cross-document reasoning---the most challenging setting for any approximation.
484	
485	% ------------------------------------------------------------
486	\subsection{MT-Bench Multi-Turn Evaluation}
487	\label{sec:mtbench}
488	
489	Table~\ref{tab:mtbench} reports GPT-4o-judged MT-Bench scores across 80 multi-turn prompts.
490	
491	\begin{table}[t]
492	\centering
493	\small
494	\caption{MT-Bench results (GPT-4o judge). KL-only is within judge noise of dense.}
495	\label{tab:mtbench}
496	\begin{tabular}{lccccc}
497	\toprule
498	\textbf{Method} & \textbf{Avg} & \textbf{Writing} & \textbf{Reason.} & \textbf{Math} & \textbf{Coding} \\
499	\midrule
500	Dense & 7.21 & 7.50 & 6.85 & 6.80 & 7.10 \\
501	TEAL & 6.18 & 6.45 & 5.60 & 5.40 & 5.80 \\
502	SPON & 6.78 & 7.10 & 6.35 & 6.15 & 6.55 \\
503	BCE+comp & 6.42 & 6.80 & 5.85 & 5.65 & 5.90 \\
504	KL-only & 7.05 & 7.35 & 6.65 & 6.55 & 6.85 \\
505	SPON+KL & 7.12 & 7.40 & 6.75 & 6.65 & 6.95 \\
506	\bottomrule
507	\end{tabular}
508	\end{table}
509	
510	KL-only (7.05) is within 0.16 of dense (7.21)---within the GPT-4o judge's scoring noise floor.
511	BCE+compensation (6.42) shows severe degradation on reasoning ($-$1.00) and math ($-$1.15), tasks most sensitive to output distribution fidelity.
512	SPON+KL (7.12) nearly recovers dense-level performance across all categories.
513	
514	% ------------------------------------------------------------
515	\subsection{RULER Synthetic Diagnostics}
516	\label{sec:ruler}
517	
518	Table~\ref{tab:ruler} provides fine-grained diagnostics on RULER synthetic tasks at 4K and 16K contexts.
519	
520	\begin{table}[t]
521	\centering
522	\small
523	\caption{RULER synthetic evaluation at 4K and 16K context lengths.}
524	\label{tab:ruler}
525	\begin{tabular}{llcccc}
526	\toprule
527	\textbf{Task} & \textbf{Ctx} & \textbf{Dense} & \textbf{KL} & \textbf{BCE+c} & \textbf{S+KL} \\
528	\midrule
529	Needle & 4K & 99.2 & 98.0 & 94.5 & 98.5 \\
530	Needle & 16K & 96.8 & 94.5 & 86.2 & 95.8 \\
531	Multi-key & 4K & 93.5 & 91.2 & 83.8 & 92.4 \\
532	Multi-key & 16K & 84.1 & 82.4 & 72.1 & 83.5 \\
533	Var-track & 4K & 92.8 & 92.1 & 83.9 & 92.5 \\
534	Var-track & 16K & 84.5 & 81.3 & 76.5 & 83.2 \\
535	\midrule
536	\textbf{Average} & \textbf{4K} & \textbf{95.2} & \textbf{93.8} & \textbf{87.4} & \textbf{94.5} \\
537	\textbf{Average} & \textbf{16K} & \textbf{88.5} & \textbf{86.1} & \textbf{78.3} & \textbf{87.2} \\
538	\bottomrule
539	\end{tabular}
540	\end{table}
541	
542	KL-only's context-length degradation pattern (4K$\to$16K: $-$7.7) closely tracks dense ($-$6.7), while BCE+compensation degrades more steeply ($-$9.1).
543	Multi-key retrieval shows the largest differentiation at 16K (KL 82.4 vs.\ BCE+comp 72.1), consistent with this task's sensitivity to joint neuron interactions---simultaneous retrieval of multiple scattered facts requires precise FFN activation patterns.
544	
545	% ============================================================
546	\section{Discussion}
547	
548	\paragraph{Two-dimensional taxonomy.}
549	Our results populate a two-axis taxonomy of sparsity correction methods: \emph{correction granularity} (static $\to$ per-layer $\to$ per-token) $\times$ \emph{training signal coupling} (decomposed/BCE $\to$ intermediate/MSE $\to$ coupled/KL).
550	Prior work fills specific cells---SPON (static, KL), ShadowLLM (per-layer, MSE), FastForward (per-token, BCE)---while our KL-only method fills the (per-token, KL) cell, which proves to be the Pareto-optimal configuration.
551	
552	\paragraph{Practical implications.}
553	Eliminating compensation networks simplifies the inference pipeline: no additional parameters to load, no per-layer GEMV, and a smaller memory footprint.
554	For Llama~3.1~8B, this means 256\,MB fewer parameters and 1.8\,ms/token lower latency, with strictly better quality.
555	The SPON+KL variant adds only 1\,MB (static biases) for a further 1.22 PPL improvement.
556	
557	\paragraph{Limitations.}
558	We evaluate on 7--8B parameter models; scaling behavior at 70B+ remains to be verified.
559	The quadratic scaling prediction is confirmed over $s \in [0.3, 0.6]$ but extrapolation beyond 60\% needs additional data.
560	KL training requires a teacher forward pass per step ($3.2\times$ per-step cost), though the total training time is modest (4.2 hours on a single GPU for 1000 steps).
561	
562	% ============================================================
563	\section{Conclusion}
564	
565	We have shown that output-distribution distillation via KL divergence categorically dominates BCE-based training for contextual activation sparsity prediction in SwiGLU LLMs, eliminating the need for compensation networks.
566	The advantage traces to a fundamental difference in gradient structure: KL's coupled gradients capture joint neuron interactions that BCE's factorized gradients miss, with the quality gap scaling quadratically in sparsity ($R^2 = 0.97$).
567	The resulting method is simultaneously simpler (no compensation network), smaller (24\,MB vs.\ 280\,MB), faster (12.0 vs.\ 13.8\,ms/token), and better (9.20 vs.\ 18.64 PPL) than the BCE+compensation alternative.
568	Combined with SPON's static bias correction, the modular decomposition achieves 7.98 PPL---within 30\% of dense---with near-perfect additivity.
569	
570	% ============================================================
571	\bibliography{custom}
572	
573	\begin{thebibliography}{20}
574	
575	\bibitem[Shazeer, 2020]{shazeer2020glu}
576	Noam Shazeer. 2020.
577	\newblock {GLU} Variants Improve Transformer.
578	\newblock {\em arXiv preprint arXiv:2002.05202}.
579	
580	\bibitem[Liu et~al., 2024]{liu2024teal}
581	Yixin Liu, Haotian Ye, Lei Li, and Hao Peng. 2024.
582	\newblock {TEAL}: Token-wise Efficient Activation sparsity for {LLM}s.
583	\newblock In {\em Proceedings of NeurIPS}.
584	
585	\bibitem[Shen et~al., 2024]{shen2024wina}
586	Zhihang Shen, et~al. 2024.
587	\newblock {WINA}: Weight-Informed Neuron Activation for accelerating large language model inference.
588	\newblock {\em arXiv preprint arXiv:2410.xxxx}.
589	
590	\bibitem[Zhang et~al., 2024]{zhang2024rsparse}
591	Tianyu Zhang, et~al. 2024.
592	\newblock {R-Sparse}: Rank-Aware Activation Sparsity for efficient {LLM} inference.
593	\newblock {\em arXiv preprint arXiv:2410.xxxx}.
594	
595	\bibitem[Wang et~al., 2024]{wang2024fastforward}
596	Tao Wang, et~al. 2024.
597	\newblock {FastForward}: Learned sparsity prediction with compensation for efficient {LLM} inference.
598	\newblock {\em arXiv preprint arXiv:2405.xxxx}.
599	
600	\bibitem[Zhou et~al., 2024]{zhou2024spon}
601	Yongqi Zhou, et~al. 2024.
602	\newblock {SPON}: Static-correction-based sparsity optimization for language models via {KL} distillation.
603	\newblock {\em arXiv preprint arXiv:2406.xxxx}.
604	
605	\bibitem[Chen et~al., 2024]{chen2024shadowllm}
606	Zheng Chen, et~al. 2024.
607	\newblock {ShadowLLM}: Predictor-based contextual sparsity for large language models.
608	\newblock {\em arXiv preprint arXiv:2406.xxxx}.
609	
610	\bibitem[Hinton et~al., 2015]{hinton2015distilling}
611	Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015.
612	\newblock Distilling the Knowledge in a Neural Network.
613	\newblock {\em arXiv preprint arXiv:1503.02531}.
614	
615	\end{thebibliography}
616	
617	\end{document}
618	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c33b2db-cc0a-4cf0-b1f9-617a4b96acfe",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "da0ac760-5c8d-4b13-8dcb-6e6c0185e8a3",
  "sourceToolAssistantUUID": "1c33b2db-cc0a-4cf0-b1f9-617a4b96acfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T17:47:29.331Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FN65pvJUwynWtX45EindnN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da0ac760-5c8d-4b13-8dcb-6e6c0185e8a3",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mqsV3jq6UyQXWLrQRE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "add0c96b-3b87-4750-ac88-1f9b8aa09be2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CLXFDCLX7a3nz4ggSTpZf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 29466,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4223
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 29466,
          "cache_creation_input_tokens": 4223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4223,
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

_source line 33 · 2026-05-15T17:47:29.336Z_

<details><summary>↩ Tool result · `toolu_01FN65pvJUwynWtX45EindnN`</summary>

```text
1	---
2	dream_id: dream_20260515T164925
3	tier: best
4	overall_score: Weak Reject (3/6)
5	timestamp: 2026-05-15T17:45:35.237727+00:00
6	---
7	
8	# Dream Review Report — distill_sparse_swiglu
9	
10	**Paper:** "Output-Distribution Distillation Makes Compensation Networks Obsolete for SwiGLU Activation Sparsity"
11	**Dream ID:** 20260515T164925
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	**Date:** 2026-05-15
14	
15	---
16	
17	## Roundtable Summary
18	
19	| | R1 (Methods & Experiments) | R2 (Novelty & Related Work) | Consensus |
20	|---|---|---|---|
21	| **Score** | 3/6 (Weak Reject) | 3/6 (Weak Reject) | **3/6 (Weak Reject)** |
22	| **Confidence** | 4/5 | 4/5 | 4/5 |
23	
24	Both reviewers independently converged on Weak Reject. The paper presents a large, consistent effect size (KL-only 9.20 vs BCE+comp 18.64 PPL) with thorough ablation design, but multiple major concerns — limited novelty, questionable baseline fairness, missing critical controls, and informal theory — prevent acceptance at a top ML venue (~25% acceptance rate).
25	
26	---
27	
28	## Step 1: Independent Reviews
29	
30	### R1 — Methods & Experiments (Score: 3/6)
31	
32	**Strengths:**
33	1. Well-motivated theoretical distinction between KL (gradient coupling through Jacobian) and BCE (factorized per-neuron gradient). The argument is mathematically correct.
34	2. Excellent ablation design: four-condition ablation cleanly isolates loss vs. compensation; STE baseline (Table 2) isolates loss vs. relaxation; iso-compute (Table 3) controls for FLOPs.
35	3. Large, consistent effect size with low variance (KL std=0.04 across 5 seeds). Not a paper where you squint at error bars.
36	4. Comprehensive evaluation breadth: PPL, 5 discriminative benchmarks, LongBench, MT-Bench, RULER, latency profiling, cross-architecture validation.
37	5. Practical relevance: KL-only Pareto-dominates BCE+comp on quality, latency, and parameter count simultaneously.
38	6. Modular decomposition (SPON+KL) with quantified interaction residual (6.8%) is a useful contribution.
39	
40	**Major Weaknesses:**
41	1. **Result provenance concern.** Project files suggest only MVP experiments (KL-only 3 seeds, BCE-only 3 seeds) actually completed. The remaining experiments (BCE+comp, SPON, SPON+KL, Mistral, downstream benchmarks, sparsity sweep, LongBench, MT-Bench, RULER) appear to be dream simulations with imagined numbers matching `review_context.yaml` exactly. If all experiments were actually run, this concern evaporates — but the paper should provide W&B links or training logs.
42	2. **BCE oracle target confound.** BCE is trained with top-k by activation magnitude as the binary target. This target is itself suboptimal — it does not account for downstream impact on the output distribution. KL implicitly discovers optimal masks via end-to-end gradients. Much of the KL-BCE gap may reflect target quality, not loss function quality. A BCE variant with KL-optimal targets (neurons whose removal maximizes KL divergence) would disentangle these factors.
43	3. **Quadratic scaling argument is informal.** The O(s²D²) claim conflates the count of pairwise interactions with the gradient signal magnitude gap. The actual KL-BCE difference depends on spectral properties of the Jacobian, not merely neuron pair counts. Fitting Δ=as² to 7 single-seed points with R²=0.97 is suggestive but not definitive — many monotone functions would fit comparably. No AIC/BIC comparison against alternative forms is reported.
44	
45	**Minor Weaknesses:**
46	- Sparsity constraint mechanism (Lagrangian multiplier with exponential updates, clamping to [0.1, 1000]) underreported despite being essential for reproducibility.
47	- Seed sensitivity: actual MVP results show KL std ~0.92 on TEAL sparse PPL vs. reported 0.04 on hard-mask PPL. Which evaluation protocol produces the headline number?
48	- Unequal seed counts across conditions (BCE-only 3, BCE+comp 5, KL+comp 3) are unusual.
49	- Calibration data (WikiText-103) is narrow domain; sensitivity to calibration data not analyzed.
50	
51	**Missing Experiments Requested:**
52	- BCE with KL-optimal targets
53	- Per-layer analysis of KL-BCE gap
54	- Training dynamics (learning curves for all conditions)
55	- Statistical significance tests (paired t-test on headline comparison)
56	- Predictor architecture sensitivity
57	
58	---
59	
60	### R2 — Novelty & Related Work (Score: 3/6)
61	
62	**Strengths:**
63	1. Two-dimensional taxonomy (correction granularity × training signal coupling) is a genuinely useful organizational contribution that clearly identifies the unoccupied design cell.
64	2. Thorough ablation design (STE, iso-compute) above average for this subfield.
65	3. Large effect size — the KL-BCE gap is decisive, not marginal.
66	4. Modular decomposition (SPON+KL) with orthogonality analysis is the most original contribution.
67	5. Comprehensive evaluation breadth across PPL, discriminative, generative, and long-context benchmarks.
68	
69	**Major Weaknesses:**
70	1. **Thin novelty.** The core contribution reduces to "use KL instead of BCE when training your sparsity predictor" — a one-line change in the training loop. SPON already demonstrated KL works for sparsity in this exact domain. Extending from static to contextual is a natural next step, not a conceptual leap. No new algorithm, architecture, or training procedure.
71	2. **Gradient coupling theory is trivial.** The chain rule applied to two different losses. Any output-level loss (MSE on logits, JS divergence, reverse KL) would exhibit the same coupling property. The paper does not explain why KL is uniquely better than other coupled losses.
72	3. **Missing MSE-on-logits baseline — the most critical gap.** MSE on output logits also provides gradient coupling through the same Jacobian pathway. If MSE-logits matches KL, the paper's framing collapses from "KL is special" to "any output-level loss beats BCE." This omission is conspicuous.
73	4. **BCE baseline appears unreasonably weak.** BCE-only at 28.16 PPL is worse than training-free TEAL (12.48) — a trained predictor performing 2× worse than a heuristic suggests implementation issues. Was BCE trained with Gumbel-sigmoid (designed for continuous losses) rather than STE (its natural relaxation)? Were the same target generation and hyperparameters as FastForward used?
74	
75	**Minor Weaknesses:**
76	- Only 8 references — alarmingly sparse. Missing: Deja Vu (foundational BCE predictor work), CATS, Minitron (KL for structured pruning), DIP, L0 regularization, Gumbel-softmax foundations, Sparsing Law, ReLU Strikes Back, TurboSparse, ProSparse, SparseInfer, SVD-CSP.
77	- Scope limited to two 7-8B SwiGLU models. No larger models (13B, 70B) where the efficiency tradeoff matters most. No non-SwiGLU architectures.
78	- Quadratic scaling claim is post-hoc curve fitting on 7 single-seed points presented as theoretical prediction.
79	
80	**Novelty Assessment:**
81	The paper sits at the intersection of two well-established techniques (KL distillation + learned sparsity prediction). Useful empirical knowledge, but the novelty is limited to filling a cell in the authors' own taxonomy. Engineering value is clear (simpler inference pipeline), but scientific novelty is insufficient for a ~25% acceptance rate venue. The modular decomposition (Claim 2) is the strongest original contribution but is positioned as secondary.
82	
83	---
84	
85	## Step 2: Cross-Sharing
86	
87	**R1 reacting to R2's concerns:**
88	- R1 agrees the missing MSE-on-logits baseline is critical. The gradient coupling argument applies equally to MSE, JS divergence, or any output-level loss. Without this control, the paper cannot claim KL is uniquely effective vs. "any coupled loss beats BCE."
89	- R1 agrees the BCE baseline weakness (28.16 > TEAL's 12.48) is suspicious. Combined with the oracle target concern, there are two independent reasons to question whether the BCE comparison is fair.
90	- R1 acknowledges the thin novelty concern but notes that if the effect size is this large and reproducible, it has practical impact even if the idea is simple. However, this alone is insufficient for acceptance.
91	
92	**R2 reacting to R1's concerns:**
93	- R2 notes the result provenance concern strengthens the case for rejection — if only MVP experiments were actually run, the paper's comprehensive evaluation is aspirational, not evidential.
94	- R2 agrees the Lagrangian sparsity enforcement is underreported and could be a hidden source of advantage (KL+Lagrangian is a more sophisticated training setup than vanilla BCE).
95	- R2 finds the seed sensitivity issue (0.04 vs 0.92 std depending on evaluation protocol) concerning for headline reliability.
96	
97	---
98	
99	## Step 3: Convergence
100	
101	### Areas of Full Agreement
102	1. **The effect size is large and interesting.** KL-only vs. BCE-only shows a dramatic gap that is scientifically meaningful if the comparison is fair.
103	2. **Ablation design is strong.** STE baseline, iso-compute comparison, and four-condition ablation are well-designed and above average for this subfield.
104	3. **BCE baseline fairness is questionable.** Two independent concerns: (a) oracle target quality confound (R1), (b) BCE-only worse than training-free methods suggesting implementation issues (R2).
105	4. **Quadratic scaling theory is weak.** Informal counting argument + curve-fitting on 7 single-seed points, not rigorous theory.
106	5. **Missing MSE-on-logits baseline is critical.** Cannot claim KL-specific advantage without ruling out that any output-level loss achieves similar gains.
107	6. **Novelty is limited for a top venue.** Loss function swap in an existing pipeline, even with large effect.
108	
109	### Areas of Disagreement
110	- **Severity of provenance concern:** R1 treats this as a major issue; R2 does not emphasize it (focuses on novelty instead). Resolution: if this is a dream-simulated paper, provenance is moot for the dream review — evaluate the paper as-written.
111	- **Relative weight of novelty vs. empirical contribution:** R1 is more willing to accept strong empirical findings even with limited novelty; R2 holds novelty as a hard requirement. Both converge on 3/6 regardless.
112	
113	---
114	
115	## Step 4: Final Synthesis
116	
117	### Overall Assessment: 3/6 (Weak Reject)
118	
119	**Decision rationale:** The paper identifies a real and practically important phenomenon — KL-trained contextual sparsity predictors dramatically outperform BCE-trained ones, eliminating the need for compensation networks. The ablation design is thorough and the effect size is large. However, the paper does not meet the acceptance bar for a top ML venue for the following reasons:
120	
121	### Critical Issues (must address for acceptance)
122	
123	1. **Missing MSE-on-logits baseline.** The paper's entire narrative hinges on KL being uniquely effective due to gradient coupling. But gradient coupling is a property of ANY output-level loss, not KL specifically. MSE on output logits must be tested. If MSE matches KL, the contribution generalizes to "use output-level losses for sparsity predictor training" — still useful but requires reframing. If KL uniquely dominates MSE, this strengthens the distributional matching argument considerably.
124	
125	2. **BCE baseline fairness.** Two concerns must be addressed:
126	   - (a) **Target quality confound:** BCE uses top-k by activation magnitude, while KL implicitly discovers optimal masks. Test BCE with KL-informed targets (neurons whose removal maximizes KL divergence) to separate loss function from target quality.
127	   - (b) **Implementation fairness:** BCE-only (28.16) is worse than training-free TEAL (12.48). This is anomalous for a trained predictor and suggests potential issues with Gumbel-sigmoid relaxation applied to binary targets, or other training setup differences. Explicitly confirm identical training conditions and explain this anomaly.
128	
129	3. **Thin novelty must be offset by deeper analysis.** If the core contribution is a loss function swap, the paper needs stronger theoretical or analytical depth to justify a full paper. Options:
130	   - Formal theorem connecting Jacobian spectral properties to the KL-BCE gap
131	   - Per-layer analysis showing which layers benefit and why
132	   - Information-theoretic analysis of what KL captures that BCE misses
133	   - Extend to non-SwiGLU architectures to test generality
134	
135	### Important Issues
136	
137	4. **Related work is inadequate.** 8 references for a paper in this space is insufficient. Must cite Deja Vu, CATS, Minitron, L0 regularization / Gumbel-softmax foundations, and relevant sparsity scaling work.
138	
139	5. **Quadratic scaling claim needs strengthening.** Either provide a formal derivation connecting Jacobian structure to quadratic scaling, or downgrade the claim to an empirical observation. Report AIC/BIC against alternative functional forms (power law, exponential). Use multiple seeds per sparsity level.
140	
141	6. **Scale validation.** Test on at least one model >8B (13B or 70B) to support the "makes compensation networks obsolete" claim. The gradient coupling argument predicts stronger KL advantage at larger hidden dimensions — this is a testable prediction.
142	
143	### Minor Issues
144	
145	7. Report the Lagrangian sparsity enforcement mechanism in full (essential for reproducibility).
146	8. Clarify evaluation protocol (hard-mask PPL vs. TEAL sparse PPL) and report variance for both.
147	9. Equalize seed counts across all conditions.
148	10. Test calibration data sensitivity (WikiText-103 is narrow domain).
149	
150	### What Would Change the Score
151	
152	| Action | Score Impact |
153	|--------|-------------|
154	| MSE-logits baseline shows KL uniquely dominates | +1 (→ 4/6) |
155	| BCE with KL-optimal targets still loses to KL | +0.5 |
156	| Formal quadratic scaling theorem | +0.5 |
157	| 13B/70B validation | +0.5 |
158	| Adequate related work section (≥20 refs) | +0.5 |
159	| All above combined | → 5/6 (Accept) |
160	| MSE-logits matches KL | −0.5 (→ 2-3/6, requires full reframing) |
161	| BCE implementation found unfair | −1 (→ 2/6) |
162	
163	### Strengths to Preserve
164	- The four-condition ablation + STE + iso-compute ablation battery is exemplary
165	- SPON+KL modular decomposition with orthogonality analysis is the most original contribution — consider promoting it to the headline
166	- Comprehensive benchmark coverage (PPL, discriminative, generative, long-context, efficiency)
167	- Cross-architecture validation on Mistral
168	
169	### Recommendation for Authors
170	The strongest path to acceptance is: (1) run the MSE-logits baseline, (2) fix the BCE baseline fairness concerns, (3) substantially expand related work, and (4) promote the modular decomposition to a co-equal headline contribution. If MSE-logits shows KL is uniquely effective, the paper becomes significantly stronger. If not, reframe around "output-level distillation" more broadly. Consider whether the modular decomposition + orthogonality analysis could be the primary contribution, with the KL-vs-BCE comparison as supporting evidence.
171	
172	---
173	
174	**Experiment Coverage:** All 12 planned experiments appear in the paper (Tables 1-14). Coverage is complete in breadth. The critical gap is not in coverage but in missing baselines outside the original plan (MSE-logits, BCE with better targets).
175	
176	**Venue Fit:** EMNLP Efficient Methods track is appropriate for the topic. The paper needs stronger novelty or deeper analysis to meet the acceptance bar.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "add0c96b-3b87-4750-ac88-1f9b8aa09be2",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "9ced0dfe-4ae8-4421-9c7a-2c83c41c44aa",
  "sourceToolAssistantUUID": "add0c96b-3b87-4750-ac88-1f9b8aa09be2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-15T17:47:32.814Z_

Now let me also read the median and worst dream papers to compare, and check the experiment data for what was actually measured vs. simulated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ced0dfe-4ae8-4421-9c7a-2c83c41c44aa",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mrDBDtTh4jKDvifVq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6aad5ea1-9fca-46fd-b6e0-fa2c314a2f2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014G2Tv5yeZNjDfFfFLs7tWP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18567,
      "cache_read_input_tokens": 33689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18567,
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

_source line 35 · 2026-05-15T17:47:35.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_012SLa2WjRjQEBFmeW4Dw6Kh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aad5ea1-9fca-46fd-b6e0-fa2c314a2f2a",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mrDBDtTh4jKDvifVq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fba3d42-26e1-46a4-91ba-22f3f7c83cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014G2Tv5yeZNjDfFfFLs7tWP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18567,
      "cache_read_input_tokens": 33689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18567,
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

_source line 36 · 2026-05-15T17:47:35.424Z_

<details><summary>↩ Tool result · `toolu_012SLa2WjRjQEBFmeW4Dw6Kh`</summary>

```text
1	tier: best
2	narrative_guidance: 'KL categorically dominates. Headline: ''Output-distribution distillation
3	  makes compensation networks obsolete for SwiGLU sparsity.'' 三线汇聚——理论（gradient coupling解释joint
4	  interaction）、 实验（KL-only vs BCE+comp gap 9+ PPL points）、实践（省256MB compensation weights
5	  + per-layer GEMV）。 所有planned实验均确认三条claims原样成立，无需调整framing。投EMNLP Efficient Methods。
6	
7	  '
8	imagined_experiments:
9	- name: Four-Condition Ablation @ 50% Sparsity
10	  plan_id: plan_001
11	  description: 'KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。 已有数据：KL-only
12	    3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。
13	
14	    '
15	  expected_results:
16	    kl_only_s42_ppl: 9.2142
17	    kl_only_s123_ppl: 9.2474
18	    kl_only_s456_ppl: 9.14
19	    kl_only_s0_ppl: 9.19
20	    kl_only_s1_ppl: 9.23
21	    kl_only_mean_ppl: 9.2
22	    kl_only_std_ppl: 0.04
23	    kl_only_model_sparsity: 0.498
24	    bce_comp_s42_ppl: 18.22
25	    bce_comp_s123_ppl: 18.91
26	    bce_comp_s456_ppl: 18.38
27	    bce_comp_s0_ppl: 18.65
28	    bce_comp_s1_ppl: 19.05
29	    bce_comp_mean_ppl: 18.64
30	    bce_comp_std_ppl: 0.33
31	    bce_comp_model_sparsity: 0.496
32	    kl_comp_s42_ppl: 9.05
33	    kl_comp_s123_ppl: 9.08
34	    kl_comp_s456_ppl: 8.92
35	    kl_comp_mean_ppl: 9.02
36	    kl_comp_std_ppl: 0.07
37	    bce_only_mean_ppl: 28.16
38	    bce_only_std_ppl: 0.17
39	    kl_only_vs_bce_comp_gap: 9.44
40	    kl_only_vs_dense_increase_pct: 50.3
41	    bce_comp_vs_dense_increase_pct: 204.6
42	    comp_benefit_for_bce_ppl: 9.52
43	    comp_benefit_for_kl_ppl: 0.18
44	  result_rationale: 'KL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint
45	    interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12），
46	    compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。 反观BCE的per-neuron
47	    factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint effects——这在50% sparsity下产生巨大误差（PPL
48	    28.2）。Compensation网络虽然能回收~40%的 质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling
49	    information。 5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。 核心结论：compensation对KL是冗余的（0.18
50	    PPL改善 vs 9.44 PPL gap），claims 1成立。
51	
52	    '
53	  tables:
54	  - name: 'Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B,
55	      50% sparsity)'
56	    columns:
57	    - Condition
58	    - Seeds
59	    - PPL (mean±std)
60	    - Δ vs Dense
61	    - Comp Benefit
62	    rows:
63	    - - Dense
64	      - '-'
65	      - '6.12'
66	      - '-'
67	      - '-'
68	    - - BCE-only
69	      - 3
70	      - 28.16±0.17
71	      - +360%
72	      - '-'
73	    - - BCE+comp
74	      - 5
75	      - 18.64±0.33
76	      - +205%
77	      - −9.52
78	    - - KL-only
79	      - 5
80	      - 9.20±0.04
81	      - +50%
82	      - '-'
83	    - - KL+comp
84	      - 3
85	      - 9.02±0.07
86	      - +47%
87	      - −0.18
88	  figures_description:
89	  - 'Box plot: 5-seed PPL distributions for KL-only vs BCE+comp，中位线、IQR和outliers，直观展示两个分布零重叠'
90	  - 'Bar chart: compensation benefit (PPL reduction) for BCE vs KL，量化compensation对两种loss的边际价值'
91	  analysis: 'KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献
92	    0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。 5-seed std=0.04证明高度可复现。Headline
93	    claim直接成立：output-distribution distillation eliminates the need for compensation
94	    networks.
95	
96	    '
97	- name: STE Baseline — Isolating Loss vs Relaxation
98	  plan_id: plan_002
99	  description: '用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。 目的：确认KL优势来自loss
100	    function而非Gumbel relaxation。
101	
102	    '
103	  expected_results:
104	    ste_kl_s42_ppl: 9.72
105	    ste_kl_s123_ppl: 9.85
106	    ste_kl_s456_ppl: 9.64
107	    ste_kl_mean_ppl: 9.74
108	    ste_kl_std_ppl: 0.09
109	    ste_kl_model_sparsity: 0.497
110	    ste_kl_vs_gumbel_kl_gap: 0.54
111	    ste_kl_vs_bce_only_gap: 18.42
112	    gumbel_contribution_pct: 2.8
113	  result_rationale: 'STE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的
114	    smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在 decision
115	    boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16）， 说明KL-BCE的18.96
116	    point gap中97%以上来自loss function的gradient coupling property， Gumbel relaxation仅贡献~3%的marginal
117	    improvement。这直接排除了reviewer concern "Gumbel-sigmoid relaxation, not KL, explains
118	    gains"。
119	
120	    '
121	  tables:
122	  - name: 'Table 2: Relaxation Method Ablation'
123	    columns:
124	    - Condition
125	    - Relaxation
126	    - Loss
127	    - PPL (mean±std)
128	    rows:
129	    - - Gumbel+KL (ours)
130	      - Gumbel-sigmoid
131	      - KL
132	      - 9.20±0.04
133	    - - STE+KL
134	      - Straight-Through
135	      - KL
136	      - 9.74±0.09
137	    - - Gumbel+BCE
138	      - Gumbel-sigmoid
139	      - BCE
140	      - 28.16±0.17
141	  figures_description:
142	  - 'Attribution bar chart: 将KL-BCE总gap分解为loss contribution (97.2%) vs relaxation
143	    contribution (2.8%)'
144	  analysis: 'STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是 锦上添花的minor
145	    optimization trick。这为理论narrative提供clean experimental support， 且预防了reviewer的alternative
146	    explanation attack。
147	
148	    '
149	- name: Iso-Compute BCE vs KL
150	  plan_id: plan_003
151	  description: 'KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。 给BCE同等total
152	    FLOPs预算（3.2x steps），排除compute advantage。3 seeds。
153	
154	    '
155	  expected_results:
156	    kl_steps: 1000
157	    kl_flops_per_step_ratio: 3.2
158	    kl_total_flops_ratio: 3200
159	    bce_standard_steps: 1000
160	    bce_extended_steps: 3200
161	    bce_extended_total_flops_ratio: 3200
162	    bce_extended_s42_ppl: 25.28
163	    bce_extended_s123_ppl: 25.83
164	    bce_extended_s456_ppl: 25.12
165	    bce_extended_mean_ppl: 25.41
166	    bce_extended_std_ppl: 0.31
167	    bce_standard_mean_ppl: 28.16
168	    improvement_from_extended_training: 2.75
169	    remaining_gap_vs_kl: 16.21
170	    training_wall_clock_kl_hours: 4.2
171	    training_wall_clock_bce_extended_hours: 4.1
172	  result_rationale: 'BCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ''(s_j)仅依赖neuron j自身的target，
173	    更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的 （忽略joint interaction）。因此extended
174	    training让BCE-only从28.16降到25.41（降2.75）， 收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21
175	    points。 这证明KL的优势是information-theoretic的（loss function的gradient structure差异）， 不是compute-driven的，直接回应reviewer
176	    concern "KL wins only because more compute"。
177	
178	    '
179	  tables:
180	  - name: 'Table 3: Iso-Compute Comparison'
181	    columns:
182	    - Condition
183	    - Steps
184	    - Total FLOPs (relative)
185	    - PPL (mean±std)
186	    rows:
187	    - - KL (Gumbel)
188	      - 1000
189	      - 3200x
190	      - 9.20±0.04
191	    - - BCE (standard)
192	      - 1000
193	      - 1000x
194	      - 28.16±0.17
195	    - - BCE (extended)
196	      - 3200
197	      - 3200x
198	      - 25.41±0.31
199	  figures_description:
200	  - 'BCE training curve (PPL vs steps): 展示extended training的diminishing returns，标注KL水平线作为reference'
201	  - 'FLOPs-PPL scatter: 三个condition在iso-FLOPs平面上的位置'
202	  analysis: '即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21）
203	    几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。
204	
205	    '
206	- name: SPON Reimplementation & Validation
207	  plan_id: plan_004
208	  description: '在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training），
209	    在5个QA benchmarks上验证质量以确认实现正确性。
210	
211	    '
212	  expected_results:
213	    spon_wikitext2_ppl: 10.82
214	    spon_model_sparsity: 0.501
215	    spon_ppl_increase_vs_dense_pct: 76.9
216	    spon_arc_c: 51.2
217	    spon_arc_e: 74.5
218	    spon_boolq: 79.3
219	    spon_piqa: 78.1
220	    spon_winogrande: 74.8
221	    spon_params_bytes: 1048576
222	    spon_training_time_minutes: 12
223	    dense_arc_c: 55.2
224	    dense_arc_e: 79.4
225	    dense_boolq: 83.1
226	    dense_piqa: 81.3
227	    dense_winogrande: 77.8
228	  result_rationale: 'SPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case
229	    下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理 per-input variation
230	    Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82， 是一个meaningful but limited的improvement。QA
231	    benchmarks上drops 3-6%符合PPL改善幅度。 SPON的主要价值不在于standalone quality，而是作为composition实验的building
232	    block—— 它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input
233	    variation） 应当可加。
234	
235	    '
236	  tables:
237	  - name: 'Table 4: SPON Validation on QA Benchmarks'
238	    columns:
239	    - Benchmark
240	    - Dense
241	    - SPON
242	    - Δ (abs)
243	    rows:
244	    - - ARC-c
245	      - 55.2
246	      - 51.2
247	      - −4.0
248	    - - ARC-e
249	      - 79.4
250	      - 74.5
251	      - −4.9
252	    - - BoolQ
253	      - 83.1
254	      - 79.3
255	      - −3.8
256	    - - PIQA
257	      - 81.3
258	      - 78.1
259	      - −3.2
260	    - - WinoGrande
261	      - 77.8
262	      - 74.8
263	      - −3.0
264	  figures_description:
265	  - 'Radar chart: Dense vs SPON在5个QA tasks上的profile，验证SPON实现没有catastrophic failure'
266	  analysis: 'SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。 PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim
267	    2 的additivity实验提供可靠的static correction baseline。
268	
269	    '
270	- name: SPON + KL Predictor Composition
271	  plan_id: plan_005
272	  description: '同时应用SPON bias correction和KL contextual prediction。 测试output-space
273	    linearity（interaction residual）和per-layer orthogonality。3 seeds。
274	
275	    '
276	  expected_results:
277	    spon_kl_s42_ppl: 7.95
278	    spon_kl_s123_ppl: 8.12
279	    spon_kl_s456_ppl: 7.88
280	    spon_kl_mean_ppl: 7.98
281	    spon_kl_std_ppl: 0.1
282	    spon_kl_model_sparsity: 0.499
283	    spon_kl_ppl_increase_vs_dense_pct: 30.4
284	    spon_alone_ppl_recovery: 1.68
285	    kl_alone_ppl_recovery: 3.3
286	    combined_ppl_recovery: 4.52
287	    predicted_additive_recovery: 4.98
288	    interaction_residual_pct: 6.8
289	    logit_interaction_residual_l2_norm: 0.042
290	    logit_spon_correction_l2_norm: 0.38
291	    logit_kl_correction_l2_norm: 0.61
292	    logit_interaction_ratio_pct: 6.8
293	    mean_cosine_similarity_spon_kl: 0.11
294	    max_cosine_similarity_spon_kl: 0.23
295	    layers_with_cosine_gt_0_2: 4
296	  result_rationale: 'SPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x)
297	    = Δh(x) - E[Δh] （per-input residual variation）。两者在correction space中近似正交——SPON的correction是
298	    constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合 c = c_s + c_θ(x)的interaction
299	    residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98， 接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的
300	    error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift 和per-input
301	    variation方向部分对齐（如early layers的token-independent patterns）， 但这不影响整体additivity。Claim
302	    2（modular decomposition）直接成立。
303	
304	    '
305	  tables:
306	  - name: 'Table 5: Composition Additivity Analysis'
307	    columns:
308	    - Component
309	    - PPL Recovery (from TEAL baseline)
310	    - Predicted Additive
311	    - Actual
312	    - Interaction Residual
313	    rows:
314	    - - SPON only
315	      - 1.68
316	      - '-'
317	      - '-'
318	      - '-'
319	    - - KL only
320	      - 3.3
321	      - '-'
322	      - '-'
323	      - '-'
324	    - - SPON+KL
325	      - '-'
326	      - 4.98
327	      - 4.52
328	      - 9.2%
329	  - name: 'Table 5b: Per-Layer Cosine Similarity Statistics'
330	    columns:
331	    - Statistic
332	    - Value
333	    rows:
334	    - - Mean cosine
335	      - 0.11
336	    - - Median cosine
337	      - 0.08
338	    - - Max cosine
339	      - 0.23
340	    - - Layers > 0.2
341	      - 4/32
342	  figures_description:
343	  - 'Scatter plot: per-layer SPON correction magnitude vs KL correction magnitude，color
344	    by cosine similarity，展示orthogonality'
345	  - 'Logit-space decomposition visualization: ||Δ(s+c)||, ||Δ(s)||, ||Δ(c)||, ||residual||
346	    的bar chart，直观展示linearity'
347	  - 'PPL waterfall chart: Dense → TEAL → +SPON → +KL → SPON+KL，展示每个component的incremental
348	    contribution'
349	  analysis: 'SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值， per-layer
350	    cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition experimentally
351	    validated。两种correction address不同error sources的理论预测被定量确认。
352	
353	    '
354	- name: Training-Free Baselines (TEAL, WINA, R-Sparse)
355	  plan_id: plan_006
356	  description: '三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。 建立三级hierarchy:
357	    training-free < static-learned < contextual-learned。
358	
359	    '
360	  expected_results:
361	    teal_wikitext2_ppl: 12.48
362	    wina_wikitext2_ppl: 14.76
363	    rsparse_wikitext2_ppl: 13.62
364	    teal_model_sparsity: 0.5
365	    wina_model_sparsity: 0.5
366	    rsparse_model_sparsity: 0.5
367	    teal_ppl_increase_vs_dense_pct: 103.9
368	    wina_ppl_increase_vs_dense_pct: 141.3
369	    rsparse_ppl_increase_vs_dense_pct: 122.6
370	  result_rationale: 'TEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为
371	    magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但 实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed
372	    scoring虽然 考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的
373	    correlation比standard FFN更弱（gate和up projection交互），因此表现最差。 所有三种方法PPL都在12-15范围，远逊于learned
374	    methods（KL-only 9.2、SPON 10.8）， 建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn
375	    per-input neuron importance patterns，只能依赖固定heuristic。
376	
377	    '
378	  tables:
379	  - name: 'Table 6: Training-Free Baseline Comparison'
380	    columns:
381	    - Method
382	    - Type
383	    - WikiText-2 PPL
384	    - Δ vs Dense
385	    rows:
386	    - - Dense
387	      - '-'
388	      - 6.12
389	      - '-'
390	    - - TEAL
391	      - Magnitude + greedy
392	      - 12.48
393	      - +104%
394	    - - R-Sparse
395	      - Rank-aware
396	      - 13.62
397	      - +123%
398	    - - WINA
399	      - Weight-informed
400	      - 14.76
401	      - +141%
402	    - - SPON
403	      - Static learned (KL)
404	      - 10.82
405	      - +77%
406	    - - KL-only
407	      - Contextual learned (KL)
408	      - 9.2
409	      - +50%
410	  figures_description:
411	  - 'Horizontal bar chart: 所有methods按PPL排序，color-coded by method type (training-free
412	    / static / contextual)，清晰展示三级hierarchy'
413	  analysis: '三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned
414	    (9.2)。 每级提升对应information quality的提高：heuristic → average-case calibration → per-input
415	    optimization。 TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies
416	    learned approach的overhead。
417	
418	    '
419	- name: Full Benchmark Suite + Latency Profiling
420	  plan_id: plan_007
421	  description: '所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的
422	    完整evaluation。构建efficiency-accuracy Pareto frontier。
423	
424	    '
425	  expected_results:
426	    dense_wikitext2_ppl: 6.12
427	    teal_wikitext2_ppl: 12.48
428	    wina_wikitext2_ppl: 14.76
429	    rsparse_wikitext2_ppl: 13.62
430	    spon_wikitext2_ppl: 10.82
431	    bce_only_wikitext2_ppl: 28.16
432	    bce_comp_wikitext2_ppl: 18.64
433	    kl_only_wikitext2_ppl: 9.2
434	    kl_comp_wikitext2_ppl: 9.02
435	    spon_kl_wikitext2_ppl: 7.98
436	    dense_c4_ppl: 7.85
437	    teal_c4_ppl: 15.12
438	    wina_c4_ppl: 17.88
439	    rsparse_c4_ppl: 16.31
440	    spon_c4_ppl: 13.24
441	    bce_only_c4_ppl: 33.42
442	    bce_comp_c4_ppl: 22.15
443	    kl_only_c4_ppl: 11.38
444	    kl_comp_c4_ppl: 11.12
445	    spon_kl_c4_ppl: 9.81
446	    dense_arc_c: 55.2
447	    teal_arc_c: 48.1
448	    wina_arc_c: 46.3
449	    rsparse_arc_c: 47.2
450	    spon_arc_c: 51.2
451	    bce_comp_arc_c: 44.8
452	    kl_only_arc_c: 54.3
453	    spon_kl_arc_c: 54.8
454	    dense_winogrande: 77.8
455	    teal_winogrande: 72.4
456	    wina_winogrande: 70.8
457	    rsparse_winogrande: 71.5
458	    spon_winogrande: 74.8
459	    bce_comp_winogrande: 68.3
460	    kl_only_winogrande: 76.9
461	    spon_kl_winogrande: 77.2
462	    dense_mmlu: 65.8
463	    teal_mmlu: 58.2
464	    wina_mmlu: 56.4
465	    rsparse_mmlu: 57.1
466	    spon_mmlu: 60.3
467	    bce_comp_mmlu: 54.9
468	    kl_only_mmlu: 65.0
469	    spon_kl_mmlu: 65.4
470	    dense_gsm8k: 53.8
471	    teal_gsm8k: 44.2
472	    wina_gsm8k: 41.8
473	    rsparse_gsm8k: 43.1
474	    spon_gsm8k: 46.5
475	    bce_comp_gsm8k: 39.7
476	    kl_only_gsm8k: 52.8
477	    spon_kl_gsm8k: 53.2
478	    dense_humaneval: 32.9
479	    teal_humaneval: 26.2
480	    wina_humaneval: 24.4
481	    rsparse_humaneval: 25.6
482	    spon_humaneval: 28.1
483	    bce_comp_humaneval: 23.8
484	    kl_only_humaneval: 32.3
485	    spon_kl_humaneval: 32.5
486	    kl_only_avg_acc_drop_pct: 1.3
487	    spon_kl_avg_acc_drop_pct: 0.7
488	    bce_comp_avg_acc_drop_pct: 12.8
489	    dense_latency_ms: 16.8
490	    teal_latency_ms: 11.2
491	    spon_latency_ms: 10.9
492	    bce_only_latency_ms: 12.0
493	    bce_comp_latency_ms: 13.8
494	    kl_only_latency_ms: 12.0
495	    kl_comp_latency_ms: 13.8
496	    spon_kl_latency_ms: 12.1
497	    predictor_params_mb: 24
498	    compensation_params_mb: 256
499	    spon_params_mb: 1
500	    kl_only_speedup_vs_dense_pct: 28.6
501	    bce_comp_speedup_vs_dense_pct: 17.9
502	    kl_only_speedup_vs_bce_comp_pct: 13.0
503	  result_rationale: 'Downstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上
504	    接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching， 保留了token-level的prediction
505	    quality，而downstream tasks本质上都依赖model的next-token prediction能力。BCE+comp虽然有compensation，但其PPL
506	    (18.64)反映的distribution mismatch 在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop
507	    26-28%），因为 这些任务对error compounding更敏感。 Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要
508	    compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto
509	    frontier上dominates BCE+comp——更快、更好、更小。
510	
511	    '
512	  tables:
513	  - name: 'Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)'
514	    columns:
515	    - Method
516	    - Wiki PPL↓
517	    - C4 PPL↓
518	    - ARC-c↑
519	    - WinoG↑
520	    - MMLU↑
521	    - GSM8K↑
522	    - HumanE↑
523	    - Avg Δ↓
524	    rows:
525	    - - Dense
526	      - 6.12
527	      - 7.85
528	      - 55.2
529	      - 77.8
530	      - 65.8
531	      - 53.8
532	      - 32.9
533	      - —
534	    - - TEAL
535	      - 12.48
536	      - 15.12
537	      - 48.1
538	      - 72.4
539	      - 58.2
540	      - 44.2
541	      - 26.2
542	      - −7.8
543	    - - WINA
544	      - 14.76
545	      - 17.88
546	      - 46.3
547	      - 70.8
548	      - 56.4
549	      - 41.8
550	      - 24.4
551	      - −9.9
552	    - - R-Sparse
553	      - 13.62
554	      - 16.31
555	      - 47.2
556	      - 71.5
557	      - 57.1
558	      - 43.1
559	      - 25.6
560	      - −8.8
561	    - - SPON
562	      - 10.82
563	      - 13.24
564	      - 51.2
565	      - 74.8
566	      - 60.3
567	      - 46.5
568	      - 28.1
569	      - −5.3
570	    - - BCE+comp
571	      - 18.64
572	      - 22.15
573	      - 44.8
574	      - 68.3
575	      - 54.9
576	      - 39.7
577	      - 23.8
578	      - −12.8
579	    - - KL-only
580	      - 9.2
581	      - 11.38
582	      - 54.3
583	      - 76.9
584	      - 65.0
585	      - 52.8
586	      - 32.3
587	      - −1.3
588	    - - SPON+KL
589	      - 7.98
590	      - 9.81
591	      - 54.8
592	      - 77.2
593	      - 65.4
594	      - 53.2
595	      - 32.5
596	      - −0.7
597	  - name: 'Table 8: Inference Efficiency Comparison'
598	    columns:
599	    - Method
600	    - Latency (ms/tok)
601	    - Speedup vs Dense
602	    - Extra Params (MB)
603	    - PPL
604	    rows:
605	    - - Dense
606	      - 16.8
607	      - 1.00×
608	      - 0
609	      - 6.12
610	    - - TEAL
611	      - 11.2
612	      - 1.50×
613	      - 0
614	      - 12.48
615	    - - SPON
616	      - 10.9
617	      - 1.54×
618	      - 1
619	      - 10.82
620	    - - KL-only
621	      - 12.0
622	      - 1.40×
623	      - 24
624	      - 9.2
625	    - - BCE+comp
626	      - 13.8
627	      - 1.22×
628	      - 280
629	      - 18.64
630	    - - SPON+KL
631	      - 12.1
632	      - 1.39×
633	      - 25
634	      - 7.98
635	  figures_description:
636	  - 'Pareto frontier plot: x=latency (ms/tok), y=WikiText-2 PPL, 所有conditions标注。KL-only和SPON+KL在frontier上，BCE+comp
637	    dominated'
638	  - 'Grouped bar chart: 5个downstream tasks，每个task所有methods并排，直观展示KL-only接近dense而BCE+comp远逊'
639	  - 'Taxonomy heatmap: 2D table (granularity × coupling) 填入PPL值，our cell (contextual
640	    × KL) 最优'
641	  analysis: 'KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20
642	    vs 18.64）， 更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains
643	    transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。 SPON+KL作为our
644	    best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。 Taxonomy table的每个cell都有实验数据支撑。
645	
646	    '
647	- name: 7-Level Sparsity Sweep — Quadratic Scaling Test
648	  plan_id: plan_008
649	  description: '在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed），
650	    测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。
651	
652	    '
653	  expected_results:
654	    sparsity_levels:
655	    - 0.3
656	    - 0.35
657	    - 0.4
658	    - 0.45
659	    - 0.5
660	    - 0.55
661	    - 0.6
662	    kl_ppls:
663	    - 7.05
664	    - 7.42
665	    - 7.98
666	    - 8.51
667	    - 9.2
668	    - 10.82
669	    - 13.15
670	    bce_ppls:
671	    - 14.55
672	    - 17.82
673	    - 19.98
674	    - 24.71
675	    - 28.2
676	    - 33.62
677	    - 42.65
678	    kl_bce_deltas:
679	    - 7.5
680	    - 10.4
681	    - 12.0
682	    - 16.2
683	    - 19.0
684	    - 22.8
685	    - 29.5
686	    s2_fit_coefficient_a: 79.2
687	    s2_fit_r_squared: 0.97
688	    s2_plus_linear_fit_r_squared: 0.99
689	    taylor_accuracy_pct:
690	    - 96.8
691	    - 95.4
692	    - 94.1
693	    - 92.5
694	    - 89.8
695	    - 85.6
696	    - 80.2
697	    predicted_deltas_s2_only:
698	    - 7.13
699	    - 9.7
700	    - 12.67
701	    - 16.03
702	    - 19.8
703	    - 23.96
704	    - 28.51
705	  result_rationale: 'KL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时，
706	    每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为 O(s²D²)。BCE的factorized
707	    gradient完全忽略这些interactions。因此KL-BCE quality delta 应当scale as s²（leading term来自pairwise
708	    neuron interaction）。 实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%）
709	    下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%） accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent
710	    with the theory（Taylor展开在远离展开点时精度下降）。 加入linear term后R²=0.99，说明residual主要是one lower-order
711	    correction。 Claim 3（quadratic scaling）定量验证通过。
712	
713	    '
714	  tables:
715	  - name: 'Table 9: Sparsity Sweep Results'
716	    columns:
717	    - Sparsity s
718	    - s²
719	    - KL PPL
720	    - BCE PPL
721	    - Δ (BCE−KL)
722	    - Predicted Δ (as²)
723	    - Taylor Acc %
724	    rows:
725	    - - 0.3
726	      - 0.09
727	      - 7.05
728	      - 14.55
729	      - 7.5
730	      - 7.13
731	      - 96.8
732	    - - 0.35
733	      - 0.123
734	      - 7.42
735	      - 17.82
736	      - 10.4
737	      - 9.7
738	      - 95.4
739	    - - 0.4
740	      - 0.16
741	      - 7.98
742	      - 19.98
743	      - 12.0
744	      - 12.67
745	      - 94.1
746	    - - 0.45
747	      - 0.203
748	      - 8.51
749	      - 24.71
750	      - 16.2
751	      - 16.03
752	      - 92.5
753	    - - 0.5
754	      - 0.25
755	      - 9.2
756	      - 28.2
757	      - 19.0
758	      - 19.8
759	      - 89.8
760	    - - 0.55
761	      - 0.303
762	      - 10.82
763	      - 33.62
764	      - 22.8
765	      - 23.96
766	      - 85.6
767	    - - 0.6
768	      - 0.36
769	      - 13.15
770	      - 42.65
771	      - 29.5
772	      - 28.51
773	      - 80.2
774	  - name: 'Table 9b: Scaling Fit Statistics'
775	    columns:
776	    - Model
777	    - R²
778	    - Parameters
779	    rows:
780	    - - Δ = as²
781	      - 0.97
782	      - a=79.2
783	    - - Δ = as² + bs
784	      - 0.99
785	      - a=68.1, b=5.8
786	    - - Δ = as² + bs + c
787	      - 0.99
788	      - a=65.3, b=7.2, c=−0.4
789	  figures_description:
790	  - 'Scatter + fitted curve: x=s², y=KL-BCE delta, 实测点+quadratic fit曲线+95% CI band。R²=0.97标注'
791	  - 'Dual-axis line plot: x=sparsity, 左轴=KL PPL和BCE PPL（两条线），右轴=delta（bar chart），展示gap加速增长'
792	  - 'Taylor accuracy vs sparsity: 展示理论预测precision随sparsity的graceful degradation'
793	  analysis: 'KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。 Quadratic
794	    scaling意味着在高sparsity regime（>50%），KL的优势accelerates—— 这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts
795	    extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步 增强理论credibility。Claim
796	    3直接成立。
797	
798	    '
799	- name: Mistral-7B-v0.3 Cross-Architecture Validation
800	  plan_id: plan_009
801	  description: '在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上
802	    复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3
803	    seeds each。
804	
805	    '
806	  expected_results:
807	    mistral_dense_wikitext2_ppl: 5.48
808	    mistral_dense_arc_c: 58.1
809	    mistral_dense_mmlu: 62.8
810	    mistral_kl_s42_ppl: 8.12
811	    mistral_kl_s123_ppl: 8.35
812	    mistral_kl_s456_ppl: 8.18
813	    mistral_kl_mean_ppl: 8.22
814	    mistral_kl_std_ppl: 0.1
815	    mistral_kl_model_sparsity: 0.498
816	    mistral_kl_ppl_increase_vs_dense_pct: 50.0
817	    mistral_kl_arc_c: 56.4
818	    mistral_kl_mmlu: 61.3
819	    mistral_bce_comp_s42_ppl: 12.81
820	    mistral_bce_comp_s123_ppl: 13.24
821	    mistral_bce_comp_s456_ppl: 12.53
822	    mistral_bce_comp_mean_ppl: 12.86
823	    mistral_bce_comp_std_ppl: 0.29
824	    mistral_bce_comp_model_sparsity: 0.497
825	    mistral_bce_comp_arc_c: 50.8
826	    mistral_bce_comp_mmlu: 55.9
827	    mistral_kl_vs_bce_comp_ppl_gap: 4.64
828	    mistral_kl_vs_bce_comp_ppl_gap_pct: 36.1
829	  result_rationale: 'Mistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但
830	    attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling
831	    property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity 在hidden
832	    states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。 PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64
833	    vs 9.44）较小是因为 Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。
834	    Sliding window attention可能使某些layers的neuron importance更localized，略微 降低BCE+comp的absolute
835	    PPL（12.86 vs Llama的18.64），但不改变KL dominance。
836	
837	    '
838	  tables:
839	  - name: 'Table 10: Mistral-7B-v0.3 Cross-Architecture Validation'
840	    columns:
841	    - Condition
842	    - Wiki PPL↓
843	    - ARC-c↑
844	    - MMLU↑
845	    rows:
846	    - - Dense
847	      - 5.48
848	      - 58.1
849	      - 62.8
850	    - - KL-only
851	      - 8.22±0.10
852	      - 56.4
853	      - 61.3
854	    - - BCE+comp
855	      - 12.86±0.29
856	      - 50.8
857	      - 55.9
858	    - - Gap (KL vs BCE+comp)
859	      - −4.64
860	      - '+5.6'
861	      - '+5.4'
862	  - name: 'Table 10b: Cross-Architecture Consistency'
863	    columns:
864	    - Metric
865	    - Llama 3.1 8B
866	    - Mistral-7B-v0.3
867	    rows:
868	    - - KL PPL increase vs dense
869	      - 50.3%
870	      - 50.0%
871	    - - KL vs BCE+comp gap (PPL)
872	      - 9.44
873	      - 4.64
874	    - - KL vs BCE+comp gap (%)
875	      - 50.6%
876	      - 36.1%
877	  figures_description:
878	  - 'Side-by-side bar chart: Llama和Mistral的KL-only vs BCE+comp PPL，展示cross-architecture
879	    consistency'
880	  analysis: 'Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap
881	    36%。 KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function 的universal
882	    property而非architecture-specific artifact。排除reviewer concern "Single model / limited
883	    generalization"。
884	
885	    '
886	- name: LongBench Long-Context Evaluation
887	  plan_id: plan_010
888	  description: 'LongBench English subset（4K-32K tokens），所有conditions。 Per-task-type
889	    breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。
890	
891	    '
892	  expected_results:
893	    dense_longbench_avg: 43.5
894	    teal_longbench_avg: 35.4
895	    wina_longbench_avg: 33.8
896	    rsparse_longbench_avg: 34.6
897	    spon_longbench_avg: 39.8
898	    bce_comp_longbench_avg: 32.1
899	    kl_only_longbench_avg: 42.1
900	    spon_kl_longbench_avg: 42.8
901	    kl_single_doc_qa: 44.8
902	    kl_multi_doc_qa: 38.2
903	    kl_summarization: 42.5
904	    kl_few_shot: 47.1
905	    kl_code: 38.0
906	    bce_comp_single_doc_qa: 35.2
907	    bce_comp_multi_doc_qa: 28.4
908	    bce_comp_summarization: 33.8
909	    bce_comp_few_shot: 34.6
910	    bce_comp_code: 28.5
911	    dense_single_doc_qa: 46.2
912	    dense_multi_doc_qa: 39.5
913	    dense_summarization: 43.8
914	    dense_few_shot: 48.3
915	    dense_code: 39.6
916	    kl_only_avg_drop_vs_dense: 1.4
917	    bce_comp_avg_drop_vs_dense: 11.4
918	    kl_worst_task_type: multi-doc QA
919	    kl_worst_task_drop: 3.3
920	  result_rationale: '长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution
921	    matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor 看到的是per-token
922	    hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg） 与short-context
923	    evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document reasoning），因此KL-only在此处drop最大（3.3
924	    points）。BCE+comp在长序列下degradation 更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates
925	    without compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5，
926	    进一步确认composition在长序列下仍然有效。
927	
928	    '
929	  tables:
930	  - name: 'Table 11: LongBench Per-Task-Type Breakdown'
931	    columns:
932	    - Task Type
933	    - Dense
934	    - TEAL
935	    - SPON
936	    - BCE+comp
937	    - KL-only
938	    - SPON+KL
939	    rows:
940	    - - Single-doc QA
941	      - 46.2
942	      - 38.1
943	      - 42.0
944	      - 35.2
945	      - 44.8
946	      - 45.3
947	    - - Multi-doc QA
948	      - 39.5
949	      - 31.2
950	      - 36.1
951	      - 28.4
952	      - 38.2
953	      - 38.8
954	    - - Summarization
955	      - 43.8
956	      - 35.8
957	      - 40.2
958	      - 33.8
959	      - 42.5
960	      - 43.1
961	    - - Few-shot
962	      - 48.3
963	      - 39.5
964	      - 44.3
965	      - 34.6
966	      - 47.1
967	      - 47.8
968	    - - Code
969	      - 39.6
970	      - 32.4
971	      - 36.5
972	      - 28.5
973	      - 38.0
974	      - 38.9
975	    - - '**Average**'
976	      - '**43.5**'
977	      - '**35.4**'
978	      - '**39.8**'
979	      - '**32.1**'
980	      - '**42.1**'
981	      - '**42.8**'
982	  figures_description:
983	  - 'Radar chart: 5个task types，Dense/KL-only/BCE+comp/SPON+KL四条线，展示KL-only profile近似dense'
984	  - 'Heatmap: methods × task types，color by score，直观展示BCE+comp在所有task types上consistently差'
985	  analysis: 'LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4），
986	    无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%），
987	    可能因为compensation网络对error accumulation的correction在长序列下saturate。 增强了EMNLP venue
988	    fit（NLP-specific long-context evaluation）。
989	
990	    '
991	- name: MT-Bench Multi-Turn Instruction Following
992	  plan_id: plan_011
993	  description: 'MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following
994	    quality的影响。
995	
996	    '
997	  expected_results:
998	    dense_mtbench_avg: 7.21
999	    teal_mtbench_avg: 6.18
1000	    spon_mtbench_avg: 6.78
1001	    bce_comp_mtbench_avg: 6.42
1002	    kl_only_mtbench_avg: 7.05
1003	    spon_kl_mtbench_avg: 7.12
1004	    kl_writing: 7.35
1005	    kl_roleplay: 7.15
1006	    kl_reasoning: 6.65
1007	    kl_math: 6.55
1008	    kl_coding: 6.85
1009	    kl_extraction: 7.45
1010	    kl_stem: 7.1
1011	    kl_humanities: 7.3
1012	    bce_comp_writing: 6.8
1013	    bce_comp_reasoning: 5.85
1014	    bce_comp_math: 5.65
1015	    bce_comp_coding: 5.9
1016	  result_rationale: 'MT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。
1017	    KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内）， 说明KL的output
1018	    distribution matching直接保留了instruction following能力。 Math和reasoning categories drop略大（KL-only
1019	    6.55/6.65 vs dense ~6.8/6.85），因为 这些tasks需要precise multi-step reasoning，对任何distribution
1020	    shift更敏感。 BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为
1021	    BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上
1022	    产生compounding errors，compensation无法fully recover。
1023	
1024	    '
1025	  tables:
1026	  - name: 'Table 12: MT-Bench Results'
1027	    columns:
1028	    - Method
1029	    - Avg Score
1030	    - Writing
1031	    - Reasoning
1032	    - Math
1033	    - Coding
1034	    rows:
1035	    - - Dense
1036	      - 7.21
1037	      - 7.5
1038	      - 6.85
1039	      - 6.8
1040	      - 7.1
1041	    - - TEAL
1042	      - 6.18
1043	      - 6.45
1044	      - 5.6
1045	      - 5.4
1046	      - 5.8
1047	    - - SPON
1048	      - 6.78
1049	      - 7.1
1050	      - 6.35
1051	      - 6.15
1052	      - 6.55
1053	    - - BCE+comp
1054	      - 6.42
1055	      - 6.8
1056	      - 5.85
1057	      - 5.65
1058	      - 5.9
1059	    - - KL-only
1060	      - 7.05
1061	      - 7.35
1062	      - 6.65
1063	      - 6.55
1064	      - 6.85
1065	    - - SPON+KL
1066	      - 7.12
1067	      - 7.4
1068	      - 6.75
1069	      - 6.65
1070	      - 6.95
1071	  figures_description:
1072	  - 'Grouped bar chart per category: Dense vs KL-only vs BCE+comp，8个categories并排'
1073	  analysis: 'MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异 KL-only
1074	    vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上 severe degradation（-1.15/-1.00
1075	    vs dense），而KL-only仅-0.25/-0.20。 Strengthens EMNLP NLP evaluation story。
1076	
1077	    '
1078	- name: RULER Synthetic Long-Context Diagnostics
1079	  plan_id: plan_012
1080	  description: 'RULER synthetic evaluation at 4K and 16K context，3 representative
1081	    task types (needle-in-a-haystack, multi-key retrieval, variable tracking)。 Fine-grained
1082	    diagnostics complementing LongBench。
1083	
1084	    '
1085	  expected_results:
1086	    dense_ruler_4k_avg: 95.2
1087	    kl_only_ruler_4k_avg: 93.8
1088	    bce_comp_ruler_4k_avg: 87.4
1089	    spon_kl_ruler_4k_avg: 94.5
1090	    dense_ruler_16k_avg: 88.5
1091	    kl_only_ruler_16k_avg: 86.1
1092	    bce_comp_ruler_16k_avg: 78.3
1093	    spon_kl_ruler_16k_avg: 87.2
1094	    kl_needle_4k: 98.0
1095	    kl_needle_16k: 94.5
1096	    kl_multikey_4k: 91.2
1097	    kl_multikey_16k: 82.4
1098	    kl_vartrack_4k: 92.1
1099	    kl_vartrack_16k: 81.3
1100	    bce_comp_needle_4k: 94.5
1101	    bce_comp_needle_16k: 86.2
1102	    bce_comp_multikey_4k: 83.8
1103	    bce_comp_multikey_16k: 72.1
1104	    bce_comp_vartrack_4k: 83.9
1105	    bce_comp_vartrack_16k: 76.5
1106	    kl_only_4k_to_16k_drop: 7.7
1107	    bce_comp_4k_to_16k_drop: 9.1
1108	    dense_4k_to_16k_drop: 6.7
1109	  result_rationale: 'RULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability
1110	    (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2）， 在16K下gracefully
1111	    degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)， 说明KL predictor不会随context
1112	    length引入额外的degradation。BCE+comp的4K→16K drop更大 (9.1)，在multi-key retrieval（需要同时attend
1113	    to多个scattered positions）和variable tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks
1114	    对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。 Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。
1115	
1116	    '
1117	  tables:
1118	  - name: 'Table 13: RULER Synthetic Evaluation'
1119	    columns:
1120	    - Task
1121	    - Context
1122	    - Dense
1123	    - KL-only
1124	    - BCE+comp
1125	    - SPON+KL
1126	    rows:
1127	    - - Needle
1128	      - 4K
1129	      - 99.2
1130	      - 98.0
1131	      - 94.5
1132	      - 98.5
1133	    - - Needle
1134	      - 16K
1135	      - 96.8
1136	      - 94.5
1137	      - 86.2
1138	      - 95.8
1139	    - - Multi-key
1140	      - 4K
1141	      - 93.5
1142	      - 91.2
1143	      - 83.8
1144	      - 92.4
1145	    - - Multi-key
1146	      - 16K
1147	      - 84.1
1148	      - 82.4
1149	      - 72.1
1150	      - 83.5
1151	    - - Var-track
1152	      - 4K
1153	      - 92.8
1154	      - 92.1
1155	      - 83.9
1156	      - 92.5
1157	    - - Var-track
1158	      - 16K
1159	      - 84.5
1160	      - 81.3
1161	      - 76.5
1162	      - 83.2
1163	    - - '**Average**'
1164	      - '**4K**'
1165	      - '**95.2**'
1166	      - '**93.8**'
1167	      - '**87.4**'
1168	      - '**94.5**'
1169	    - - '**Average**'
1170	      - '**16K**'
1171	      - '**88.5**'
1172	      - '**86.1**'
1173	      - '**78.3**'
1174	      - '**87.2**'
1175	  figures_description:
1176	  - 'Line plot: x=context length (4K, 16K), y=RULER avg accuracy, 每个method一条线，展示degradation
1177	    rate'
1178	  - 'Heatmap: task × method × context length，诊断哪些capabilities被sparsity影响最大'
1179	  analysis: RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致
1180	    (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval 是differentiation最大的task（KL
1181	    82.4 vs BCE+comp 72.1 at 16K），这与理论一致—— multi-key需要FFN准确处理多个simultaneously relevant
1182	    positions，joint neuron interaction quality直接影响结果。
1183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fba3d42-26e1-46a4-91ba-22f3f7c83cc2",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "1b917dfb-aa91-4e0a-9151-2d906dd549b7",
  "sourceToolAssistantUUID": "9fba3d42-26e1-46a4-91ba-22f3f7c83cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T17:47:35.674Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UJoGJD2hDgsFmA8RW1pwgP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b917dfb-aa91-4e0a-9151-2d906dd549b7",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mrDBDtTh4jKDvifVq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0b8a093-54bd-4be5-81be-bf103640adfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014G2Tv5yeZNjDfFfFLs7tWP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18567,
      "cache_read_input_tokens": 33689,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18567
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 33689,
          "cache_creation_input_tokens": 18567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18567,
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

_source line 38 · 2026-05-15T17:47:35.925Z_

<details><summary>↩ Tool result · `toolu_01UJoGJD2hDgsFmA8RW1pwgP`</summary>

```text
1	[
2	  {
3	    "name": "Four-Condition Ablation @ 50% Sparsity",
4	    "description": "KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。 已有数据：KL-only 3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。\n",
5	    "results": {
6	      "kl_only_s42_ppl": 9.2142,
7	      "kl_only_s123_ppl": 9.2474,
8	      "kl_only_s456_ppl": 9.14,
9	      "kl_only_s0_ppl": 9.19,
10	      "kl_only_s1_ppl": 9.23,
11	      "kl_only_mean_ppl": 9.2,
12	      "kl_only_std_ppl": 0.04,
13	      "kl_only_model_sparsity": 0.498,
14	      "bce_comp_s42_ppl": 18.22,
15	      "bce_comp_s123_ppl": 18.91,
16	      "bce_comp_s456_ppl": 18.38,
17	      "bce_comp_s0_ppl": 18.65,
18	      "bce_comp_s1_ppl": 19.05,
19	      "bce_comp_mean_ppl": 18.64,
20	      "bce_comp_std_ppl": 0.33,
21	      "bce_comp_model_sparsity": 0.496,
22	      "kl_comp_s42_ppl": 9.05,
23	      "kl_comp_s123_ppl": 9.08,
24	      "kl_comp_s456_ppl": 8.92,
25	      "kl_comp_mean_ppl": 9.02,
26	      "kl_comp_std_ppl": 0.07,
27	      "bce_only_mean_ppl": 28.16,
28	      "bce_only_std_ppl": 0.17,
29	      "kl_only_vs_bce_comp_gap": 9.44,
30	      "kl_only_vs_dense_increase_pct": 50.3,
31	      "bce_comp_vs_dense_increase_pct": 204.6,
32	      "comp_benefit_for_bce_ppl": 9.52,
33	      "comp_benefit_for_kl_ppl": 0.18
34	    },
35	    "tables": [
36	      {
37	        "name": "Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B, 50% sparsity)",
38	        "columns": [
39	          "Condition",
40	          "Seeds",
41	          "PPL (mean±std)",
42	          "Δ vs Dense",
43	          "Comp Benefit"
44	        ],
45	        "rows": [
46	          [
47	            "Dense",
48	            "-",
49	            "6.12",
50	            "-",
51	            "-"
52	          ],
53	          [
54	            "BCE-only",
55	            3,
56	            "28.16±0.17",
57	            "+360%",
58	            "-"
59	          ],
60	          [
61	            "BCE+comp",
62	            5,
63	            "18.64±0.33",
64	            "+205%",
65	            "−9.52"
66	          ],
67	          [
68	            "KL-only",
69	            5,
70	            "9.20±0.04",
71	            "+50%",
72	            "-"
73	          ],
74	          [
75	            "KL+comp",
76	            3,
77	            "9.02±0.07",
78	            "+47%",
79	            "−0.18"
80	          ]
81	        ]
82	      }
83	    ],
84	    "figures": [],
85	    "analysis": "KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献 0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。 5-seed std=0.04证明高度可复现。Headline claim直接成立：output-distribution distillation eliminates the need for compensation networks.\n\n\nKL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12）， compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。 反观BCE的per-neuron factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint effects——这在50% sparsity下产生巨大误差（PPL 28.2）。Compensation网络虽然能回收~40%的 质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling information。 5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。 核心结论：compensation对KL是冗余的（0.18 PPL改善 vs 9.44 PPL gap），claims 1成立。\n"
86	  },
87	  {
88	    "name": "STE Baseline — Isolating Loss vs Relaxation",
89	    "description": "用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。 目的：确认KL优势来自loss function而非Gumbel relaxation。\n",
90	    "results": {
91	      "ste_kl_s42_ppl": 9.72,
92	      "ste_kl_s123_ppl": 9.85,
93	      "ste_kl_s456_ppl": 9.64,
94	      "ste_kl_mean_ppl": 9.74,
95	      "ste_kl_std_ppl": 0.09,
96	      "ste_kl_model_sparsity": 0.497,
97	      "ste_kl_vs_gumbel_kl_gap": 0.54,
98	      "ste_kl_vs_bce_only_gap": 18.42,
99	      "gumbel_contribution_pct": 2.8
100	    },
101	    "tables": [
102	      {
103	        "name": "Table 2: Relaxation Method Ablation",
104	        "columns": [
105	          "Condition",
106	          "Relaxation",
107	          "Loss",
108	          "PPL (mean±std)"
109	        ],
110	        "rows": [
111	          [
112	            "Gumbel+KL (ours)",
113	            "Gumbel-sigmoid",
114	            "KL",
115	            "9.20±0.04"
116	          ],
117	          [
118	            "STE+KL",
119	            "Straight-Through",
120	            "KL",
121	            "9.74±0.09"
122	          ],
123	          [
124	            "Gumbel+BCE",
125	            "Gumbel-sigmoid",
126	            "BCE",
127	            "28.16±0.17"
128	          ]
129	        ]
130	      }
131	    ],
132	    "figures": [],
133	    "analysis": "STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是 锦上添花的minor optimization trick。这为理论narrative提供clean experimental support， 且预防了reviewer的alternative explanation attack。\n\n\nSTE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的 smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在 decision boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16）， 说明KL-BCE的18.96 point gap中97%以上来自loss function的gradient coupling property， Gumbel relaxation仅贡献~3%的marginal improvement。这直接排除了reviewer concern \"Gumbel-sigmoid relaxation, not KL, explains gains\"。\n"
134	  },
135	  {
136	    "name": "Iso-Compute BCE vs KL",
137	    "description": "KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。 给BCE同等total FLOPs预算（3.2x steps），排除compute advantage。3 seeds。\n",
138	    "results": {
139	      "kl_steps": 1000,
140	      "kl_flops_per_step_ratio": 3.2,
141	      "kl_total_flops_ratio": 3200,
142	      "bce_standard_steps": 1000,
143	      "bce_extended_steps": 3200,
144	      "bce_extended_total_flops_ratio": 3200,
145	      "bce_extended_s42_ppl": 25.28,
146	      "bce_extended_s123_ppl": 25.83,
147	      "bce_extended_s456_ppl": 25.12,
148	      "bce_extended_mean_ppl": 25.41,
149	      "bce_extended_std_ppl": 0.31,
150	      "bce_standard_mean_ppl": 28.16,
151	      "improvement_from_extended_training": 2.75,
152	      "remaining_gap_vs_kl": 16.21,
153	      "training_wall_clock_kl_hours": 4.2,
154	      "training_wall_clock_bce_extended_hours": 4.1
155	    },
156	    "tables": [
157	      {
158	        "name": "Table 3: Iso-Compute Comparison",
159	        "columns": [
160	          "Condition",
161	          "Steps",
162	          "Total FLOPs (relative)",
163	          "PPL (mean±std)"
164	        ],
165	        "rows": [
166	          [
167	            "KL (Gumbel)",
168	            1000,
169	            "3200x",
170	            "9.20±0.04"
171	          ],
172	          [
173	            "BCE (standard)",
174	            1000,
175	            "1000x",
176	            "28.16±0.17"
177	          ],
178	          [
179	            "BCE (extended)",
180	            3200,
181	            "3200x",
182	            "25.41±0.31"
183	          ]
184	        ]
185	      }
186	    ],
187	    "figures": [],
188	    "analysis": "即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21） 几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。\n\n\nBCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ'(s_j)仅依赖neuron j自身的target， 更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的 （忽略joint interaction）。因此extended training让BCE-only从28.16降到25.41（降2.75）， 收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21 points。 这证明KL的优势是information-theoretic的（loss function的gradient structure差异）， 不是compute-driven的，直接回应reviewer concern \"KL wins only because more compute\"。\n"
189	  },
190	  {
191	    "name": "SPON Reimplementation & Validation",
192	    "description": "在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training）， 在5个QA benchmarks上验证质量以确认实现正确性。\n",
193	    "results": {
194	      "spon_wikitext2_ppl": 10.82,
195	      "spon_model_sparsity": 0.501,
196	      "spon_ppl_increase_vs_dense_pct": 76.9,
197	      "spon_arc_c": 51.2,
198	      "spon_arc_e": 74.5,
199	      "spon_boolq": 79.3,
200	      "spon_piqa": 78.1,
201	      "spon_winogrande": 74.8,
202	      "spon_params_bytes": 1048576,
203	      "spon_training_time_minutes": 12,
204	      "dense_arc_c": 55.2,
205	      "dense_arc_e": 79.4,
206	      "dense_boolq": 83.1,
207	      "dense_piqa": 81.3,
208	      "dense_winogrande": 77.8
209	    },
210	    "tables": [
211	      {
212	        "name": "Table 4: SPON Validation on QA Benchmarks",
213	        "columns": [
214	          "Benchmark",
215	          "Dense",
216	          "SPON",
217	          "Δ (abs)"
218	        ],
219	        "rows": [
220	          [
221	            "ARC-c",
222	            55.2,
223	            51.2,
224	            "−4.0"
225	          ],
226	          [
227	            "ARC-e",
228	            79.4,
229	            74.5,
230	            "−4.9"
231	          ],
232	          [
233	            "BoolQ",
234	            83.1,
235	            79.3,
236	            "−3.8"
237	          ],
238	          [
239	            "PIQA",
240	            81.3,
241	            78.1,
242	            "−3.2"
243	          ],
244	          [
245	            "WinoGrande",
246	            77.8,
247	            74.8,
248	            "−3.0"
249	          ]
250	        ]
251	      }
252	    ],
253	    "figures": [],
254	    "analysis": "SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。 PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim 2 的additivity实验提供可靠的static correction baseline。\n\n\nSPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case 下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理 per-input variation Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82， 是一个meaningful but limited的improvement。QA benchmarks上drops 3-6%符合PPL改善幅度。 SPON的主要价值不在于standalone quality，而是作为composition实验的building block—— 它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input variation） 应当可加。\n"
255	  },
256	  {
257	    "name": "SPON + KL Predictor Composition",
258	    "description": "同时应用SPON bias correction和KL contextual prediction。 测试output-space linearity（interaction residual）和per-layer orthogonality。3 seeds。\n",
259	    "results": {
260	      "spon_kl_s42_ppl": 7.95,
261	      "spon_kl_s123_ppl": 8.12,
262	      "spon_kl_s456_ppl": 7.88,
263	      "spon_kl_mean_ppl": 7.98,
264	      "spon_kl_std_ppl": 0.1,
265	      "spon_kl_model_sparsity": 0.499,
266	      "spon_kl_ppl_increase_vs_dense_pct": 30.4,
267	      "spon_alone_ppl_recovery": 1.68,
268	      "kl_alone_ppl_recovery": 3.3,
269	      "combined_ppl_recovery": 4.52,
270	      "predicted_additive_recovery": 4.98,
271	      "interaction_residual_pct": 6.8,
272	      "logit_interaction_residual_l2_norm": 0.042,
273	      "logit_spon_correction_l2_norm": 0.38,
274	      "logit_kl_correction_l2_norm": 0.61,
275	      "logit_interaction_ratio_pct": 6.8,
276	      "mean_cosine_similarity_spon_kl": 0.11,
277	      "max_cosine_similarity_spon_kl": 0.23,
278	      "layers_with_cosine_gt_0_2": 4
279	    },
280	    "tables": [
281	      {
282	        "name": "Table 5: Composition Additivity Analysis",
283	        "columns": [
284	          "Component",
285	          "PPL Recovery (from TEAL baseline)",
286	          "Predicted Additive",
287	          "Actual",
288	          "Interaction Residual"
289	        ],
290	        "rows": [
291	          [
292	            "SPON only",
293	            1.68,
294	            "-",
295	            "-",
296	            "-"
297	          ],
298	          [
299	            "KL only",
300	            3.3,
301	            "-",
302	            "-",
303	            "-"
304	          ],
305	          [
306	            "SPON+KL",
307	            "-",
308	            4.98,
309	            4.52,
310	            "9.2%"
311	          ]
312	        ]
313	      },
314	      {
315	        "name": "Table 5b: Per-Layer Cosine Similarity Statistics",
316	        "columns": [
317	          "Statistic",
318	          "Value"
319	        ],
320	        "rows": [
321	          [
322	            "Mean cosine",
323	            0.11
324	          ],
325	          [
326	            "Median cosine",
327	            0.08
328	          ],
329	          [
330	            "Max cosine",
331	            0.23
332	          ],
333	          [
334	            "Layers > 0.2",
335	            "4/32"
336	          ]
337	        ]
338	      }
339	    ],
340	    "figures": [],
341	    "analysis": "SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值， per-layer cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition experimentally validated。两种correction address不同error sources的理论预测被定量确认。\n\n\nSPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x) = Δh(x) - E[Δh] （per-input residual variation）。两者在correction space中近似正交——SPON的correction是 constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合 c = c_s + c_θ(x)的interaction residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98， 接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的 error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift 和per-input variation方向部分对齐（如early layers的token-independent patterns）， 但这不影响整体additivity。Claim 2（modular decomposition）直接成立。\n"
342	  },
343	  {
344	    "name": "Training-Free Baselines (TEAL, WINA, R-Sparse)",
345	    "description": "三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。 建立三级hierarchy: training-free < static-learned < contextual-learned。\n",
346	    "results": {
347	      "teal_wikitext2_ppl": 12.48,
348	      "wina_wikitext2_ppl": 14.76,
349	      "rsparse_wikitext2_ppl": 13.62,
350	      "teal_model_sparsity": 0.5,
351	      "wina_model_sparsity": 0.5,
352	      "rsparse_model_sparsity": 0.5,
353	      "teal_ppl_increase_vs_dense_pct": 103.9,
354	      "wina_ppl_increase_vs_dense_pct": 141.3,
355	      "rsparse_ppl_increase_vs_dense_pct": 122.6
356	    },
357	    "tables": [
358	      {
359	        "name": "Table 6: Training-Free Baseline Comparison",
360	        "columns": [
361	          "Method",
362	          "Type",
363	          "WikiText-2 PPL",
364	          "Δ vs Dense"
365	        ],
366	        "rows": [
367	          [
368	            "Dense",
369	            "-",
370	            6.12,
371	            "-"
372	          ],
373	          [
374	            "TEAL",
375	            "Magnitude + greedy",
376	            12.48,
377	            "+104%"
378	          ],
379	          [
380	            "R-Sparse",
381	            "Rank-aware",
382	            13.62,
383	            "+123%"
384	          ],
385	          [
386	            "WINA",
387	            "Weight-informed",
388	            14.76,
389	            "+141%"
390	          ],
391	          [
392	            "SPON",
393	            "Static learned (KL)",
394	            10.82,
395	            "+77%"
396	          ],
397	          [
398	            "KL-only",
399	            "Contextual learned (KL)",
400	            9.2,
401	            "+50%"
402	          ]
403	        ]
404	      }
405	    ],
406	    "figures": [],
407	    "analysis": "三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned (9.2)。 每级提升对应information quality的提高：heuristic → average-case calibration → per-input optimization。 TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies learned approach的overhead。\n\n\nTEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为 magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但 实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed scoring虽然 考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的 correlation比standard FFN更弱（gate和up projection交互），因此表现最差。 所有三种方法PPL都在12-15范围，远逊于learned methods（KL-only 9.2、SPON 10.8）， 建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn per-input neuron importance patterns，只能依赖固定heuristic。\n"
408	  },
409	  {
410	    "name": "Full Benchmark Suite + Latency Profiling",
411	    "description": "所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的 完整evaluation。构建efficiency-accuracy Pareto frontier。\n",
412	    "results": {
413	      "dense_wikitext2_ppl": 6.12,
414	      "teal_wikitext2_ppl": 12.48,
415	      "wina_wikitext2_ppl": 14.76,
416	      "rsparse_wikitext2_ppl": 13.62,
417	      "spon_wikitext2_ppl": 10.82,
418	      "bce_only_wikitext2_ppl": 28.16,
419	      "bce_comp_wikitext2_ppl": 18.64,
420	      "kl_only_wikitext2_ppl": 9.2,
421	      "kl_comp_wikitext2_ppl": 9.02,
422	      "spon_kl_wikitext2_ppl": 7.98,
423	      "dense_c4_ppl": 7.85,
424	      "teal_c4_ppl": 15.12,
425	      "wina_c4_ppl": 17.88,
426	      "rsparse_c4_ppl": 16.31,
427	      "spon_c4_ppl": 13.24,
428	      "bce_only_c4_ppl": 33.42,
429	      "bce_comp_c4_ppl": 22.15,
430	      "kl_only_c4_ppl": 11.38,
431	      "kl_comp_c4_ppl": 11.12,
432	      "spon_kl_c4_ppl": 9.81,
433	      "dense_arc_c": 55.2,
434	      "teal_arc_c": 48.1,
435	      "wina_arc_c": 46.3,
436	      "rsparse_arc_c": 47.2,
437	      "spon_arc_c": 51.2,
438	      "bce_comp_arc_c": 44.8,
439	      "kl_only_arc_c": 54.3,
440	      "spon_kl_arc_c": 54.8,
441	      "dense_winogrande": 77.8,
442	      "teal_winogrande": 72.4,
443	      "wina_winogrande": 70.8,
444	      "rsparse_winogrande": 71.5,
445	      "spon_winogrande": 74.8,
446	      "bce_comp_winogrande": 68.3,
447	      "kl_only_winogrande": 76.9,
448	      "spon_kl_winogrande": 77.2,
449	      "dense_mmlu": 65.8,
450	      "teal_mmlu": 58.2,
451	      "wina_mmlu": 56.4,
452	      "rsparse_mmlu": 57.1,
453	      "spon_mmlu": 60.3,
454	      "bce_comp_mmlu": 54.9,
455	      "kl_only_mmlu": 65.0,
456	      "spon_kl_mmlu": 65.4,
457	      "dense_gsm8k": 53.8,
458	      "teal_gsm8k": 44.2,
459	      "wina_gsm8k": 41.8,
460	      "rsparse_gsm8k": 43.1,
461	      "spon_gsm8k": 46.5,
462	      "bce_comp_gsm8k": 39.7,
463	      "kl_only_gsm8k": 52.8,
464	      "spon_kl_gsm8k": 53.2,
465	      "dense_humaneval": 32.9,
466	      "teal_humaneval": 26.2,
467	      "wina_humaneval": 24.4,
468	      "rsparse_humaneval": 25.6,
469	      "spon_humaneval": 28.1,
470	      "bce_comp_humaneval": 23.8,
471	      "kl_only_humaneval": 32.3,
472	      "spon_kl_humaneval": 32.5,
473	      "kl_only_avg_acc_drop_pct": 1.3,
474	      "spon_kl_avg_acc_drop_pct": 0.7,
475	      "bce_comp_avg_acc_drop_pct": 12.8,
476	      "dense_latency_ms": 16.8,
477	      "teal_latency_ms": 11.2,
478	      "spon_latency_ms": 10.9,
479	      "bce_only_latency_ms": 12.0,
480	      "bce_comp_latency_ms": 13.8,
481	      "kl_only_latency_ms": 12.0,
482	      "kl_comp_latency_ms": 13.8,
483	      "spon_kl_latency_ms": 12.1,
484	      "predictor_params_mb": 24,
485	      "compensation_params_mb": 256,
486	      "spon_params_mb": 1,
487	      "kl_only_speedup_vs_dense_pct": 28.6,
488	      "bce_comp_speedup_vs_dense_pct": 17.9,
489	      "kl_only_speedup_vs_bce_comp_pct": 13.0
490	    },
491	    "tables": [
492	      {
493	        "name": "Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)",
494	        "columns": [
495	          "Method",
496	          "Wiki PPL↓",
497	          "C4 PPL↓",
498	          "ARC-c↑",
499	          "WinoG↑",
500	          "MMLU↑",
501	          "GSM8K↑",
502	          "HumanE↑",
503	          "Avg Δ↓"
504	        ],
505	        "rows": [
506	          [
507	            "Dense",
508	            6.12,
509	            7.85,
510	            55.2,
511	            77.8,
512	            65.8,
513	            53.8,
514	            32.9,
515	            "—"
516	          ],
517	          [
518	            "TEAL",
519	            12.48,
520	            15.12,
521	            48.1,
522	            72.4,
523	            58.2,
524	            44.2,
525	            26.2,
526	            "−7.8"
527	          ],
528	          [
529	            "WINA",
530	            14.76,
531	            17.88,
532	            46.3,
533	            70.8,
534	            56.4,
535	            41.8,
536	            24.4,
537	            "−9.9"
538	          ],
539	          [
540	            "R-Sparse",
541	            13.62,
542	            16.31,
543	            47.2,
544	            71.5,
545	            57.1,
546	            43.1,
547	            25.6,
548	            "−8.8"
549	          ],
550	          [
551	            "SPON",
552	            10.82,
553	            13.24,
554	            51.2,
555	            74.8,
556	            60.3,
557	            46.5,
558	            28.1,
559	            "−5.3"
560	          ],
561	          [
562	            "BCE+comp",
563	            18.64,
564	            22.15,
565	            44.8,
566	            68.3,
567	            54.9,
568	            39.7,
569	            23.8,
570	            "−12.8"
571	          ],
572	          [
573	            "KL-only",
574	            9.2,
575	            11.38,
576	            54.3,
577	            76.9,
578	            65.0,
579	            52.8,
580	            32.3,
581	            "−1.3"
582	          ],
583	          [
584	            "SPON+KL",
585	            7.98,
586	            9.81,
587	            54.8,
588	            77.2,
589	            65.4,
590	            53.2,
591	            32.5,
592	            "−0.7"
593	          ]
594	        ]
595	      },
596	      {
597	        "name": "Table 8: Inference Efficiency Comparison",
598	        "columns": [
599	          "Method",
600	          "Latency (ms/tok)",
601	          "Speedup vs Dense",
602	          "Extra Params (MB)",
603	          "PPL"
604	        ],
605	        "rows": [
606	          [
607	            "Dense",
608	            16.8,
609	            "1.00×",
610	            0,
611	            6.12
612	          ],
613	          [
614	            "TEAL",
615	            11.2,
616	            "1.50×",
617	            0,
618	            12.48
619	          ],
620	          [
621	            "SPON",
622	            10.9,
623	            "1.54×",
624	            1,
625	            10.82
626	          ],
627	          [
628	            "KL-only",
629	            12.0,
630	            "1.40×",
631	            24,
632	            9.2
633	          ],
634	          [
635	            "BCE+comp",
636	            13.8,
637	            "1.22×",
638	            280,
639	            18.64
640	          ],
641	          [
642	            "SPON+KL",
643	            12.1,
644	            "1.39×",
645	            25,
646	            7.98
647	          ]
648	        ]
649	      }
650	    ],
651	    "figures": [],
652	    "analysis": "KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20 vs 18.64）， 更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。 SPON+KL作为our best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。 Taxonomy table的每个cell都有实验数据支撑。\n\n\nDownstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上 接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching， 保留了token-level的prediction quality，而downstream tasks本质上都依赖model的next-token prediction能力。BCE+comp虽然有compensation，但其PPL (18.64)反映的distribution mismatch 在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop 26-28%），因为 这些任务对error compounding更敏感。 Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要 compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto frontier上dominates BCE+comp——更快、更好、更小。\n"
653	  },
654	  {
655	    "name": "7-Level Sparsity Sweep — Quadratic Scaling Test",
656	    "description": "在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed）， 测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。\n",
657	    "results": {
658	      "sparsity_levels": [
659	        0.3,
660	        0.35,
661	        0.4,
662	        0.45,
663	        0.5,
664	        0.55,
665	        0.6
666	      ],
667	      "kl_ppls": [
668	        7.05,
669	        7.42,
670	        7.98,
671	        8.51,
672	        9.2,
673	        10.82,
674	        13.15
675	      ],
676	      "bce_ppls": [
677	        14.55,
678	        17.82,
679	        19.98,
680	        24.71,
681	        28.2,
682	        33.62,
683	        42.65
684	      ],
685	      "kl_bce_deltas": [
686	        7.5,
687	        10.4,
688	        12.0,
689	        16.2,
690	        19.0,
691	        22.8,
692	        29.5
693	      ],
694	      "s2_fit_coefficient_a": 79.2,
695	      "s2_fit_r_squared": 0.97,
696	      "s2_plus_linear_fit_r_squared": 0.99,
697	      "taylor_accuracy_pct": [
698	        96.8,
699	        95.4,
700	        94.1,
701	        92.5,
702	        89.8,
703	        85.6,
704	        80.2
705	      ],
706	      "predicted_deltas_s2_only": [
707	        7.13,
708	        9.7,
709	        12.67,
710	        16.03,
711	        19.8,
712	        23.96,
713	        28.51
714	      ]
715	    },
716	    "tables": [
717	      {
718	        "name": "Table 9: Sparsity Sweep Results",
719	        "columns": [
720	          "Sparsity s",
721	          "s²",
722	          "KL PPL",
723	          "BCE PPL",
724	          "Δ (BCE−KL)",
725	          "Predicted Δ (as²)",
726	          "Taylor Acc %"
727	        ],
728	        "rows": [
729	          [
730	            0.3,
731	            0.09,
732	            7.05,
733	            14.55,
734	            7.5,
735	            7.13,
736	            96.8
737	          ],
738	          [
739	            0.35,
740	            0.123,
741	            7.42,
742	            17.82,
743	            10.4,
744	            9.7,
745	            95.4
746	          ],
747	          [
748	            0.4,
749	            0.16,
750	            7.98,
751	            19.98,
752	            12.0,
753	            12.67,
754	            94.1
755	          ],
756	          [
757	            0.45,
758	            0.203,
759	            8.51,
760	            24.71,
761	            16.2,
762	            16.03,
763	            92.5
764	          ],
765	          [
766	            0.5,
767	            0.25,
768	            9.2,
769	            28.2,
770	            19.0,
771	            19.8,
772	            89.8
773	          ],
774	          [
775	            0.55,
776	            0.303,
777	            10.82,
778	            33.62,
779	            22.8,
780	            23.96,
781	            85.6
782	          ],
783	          [
784	            0.6,
785	            0.36,
786	            13.15,
787	            42.65,
788	            29.5,
789	            28.51,
790	            80.2
791	          ]
792	        ]
793	      },
794	      {
795	        "name": "Table 9b: Scaling Fit Statistics",
796	        "columns": [
797	          "Model",
798	          "R²",
799	          "Parameters"
800	        ],
801	        "rows": [
802	          [
803	            "Δ = as²",
804	            0.97,
805	            "a=79.2"
806	          ],
807	          [
808	            "Δ = as² + bs",
809	            0.99,
810	            "a=68.1, b=5.8"
811	          ],
812	          [
813	            "Δ = as² + bs + c",
814	            0.99,
815	            "a=65.3, b=7.2, c=−0.4"
816	          ]
817	        ]
818	      }
819	    ],
820	    "figures": [],
821	    "analysis": "KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。 Quadratic scaling意味着在高sparsity regime（>50%），KL的优势accelerates—— 这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步 增强理论credibility。Claim 3直接成立。\n\n\nKL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时， 每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为 O(s²D²)。BCE的factorized gradient完全忽略这些interactions。因此KL-BCE quality delta 应当scale as s²（leading term来自pairwise neuron interaction）。 实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%） 下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%） accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent with the theory（Taylor展开在远离展开点时精度下降）。 加入linear term后R²=0.99，说明residual主要是one lower-order correction。 Claim 3（quadratic scaling）定量验证通过。\n"
822	  },
823	  {
824	    "name": "Mistral-7B-v0.3 Cross-Architecture Validation",
825	    "description": "在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上 复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3 seeds each。\n",
826	    "results": {
827	      "mistral_dense_wikitext2_ppl": 5.48,
828	      "mistral_dense_arc_c": 58.1,
829	      "mistral_dense_mmlu": 62.8,
830	      "mistral_kl_s42_ppl": 8.12,
831	      "mistral_kl_s123_ppl": 8.35,
832	      "mistral_kl_s456_ppl": 8.18,
833	      "mistral_kl_mean_ppl": 8.22,
834	      "mistral_kl_std_ppl": 0.1,
835	      "mistral_kl_model_sparsity": 0.498,
836	      "mistral_kl_ppl_increase_vs_dense_pct": 50.0,
837	      "mistral_kl_arc_c": 56.4,
838	      "mistral_kl_mmlu": 61.3,
839	      "mistral_bce_comp_s42_ppl": 12.81,
840	      "mistral_bce_comp_s123_ppl": 13.24,
841	      "mistral_bce_comp_s456_ppl": 12.53,
842	      "mistral_bce_comp_mean_ppl": 12.86,
843	      "mistral_bce_comp_std_ppl": 0.29,
844	      "mistral_bce_comp_model_sparsity": 0.497,
845	      "mistral_bce_comp_arc_c": 50.8,
846	      "mistral_bce_comp_mmlu": 55.9,
847	      "mistral_kl_vs_bce_comp_ppl_gap": 4.64,
848	      "mistral_kl_vs_bce_comp_ppl_gap_pct": 36.1
849	    },
850	    "tables": [
851	      {
852	        "name": "Table 10: Mistral-7B-v0.3 Cross-Architecture Validation",
853	        "columns": [
854	          "Condition",
855	          "Wiki PPL↓",
856	          "ARC-c↑",
857	          "MMLU↑"
858	        ],
859	        "rows": [
860	          [
861	            "Dense",
862	            5.48,
863	            58.1,
864	            62.8
865	          ],
866	          [
867	            "KL-only",
868	            "8.22±0.10",
869	            56.4,
870	            61.3
871	          ],
872	          [
873	            "BCE+comp",
874	            "12.86±0.29",
875	            50.8,
876	            55.9
877	          ],
878	          [
879	            "Gap (KL vs BCE+comp)",
880	            "−4.64",
881	            "+5.6",
882	            "+5.4"
883	          ]
884	        ]
885	      },
886	      {
887	        "name": "Table 10b: Cross-Architecture Consistency",
888	        "columns": [
889	          "Metric",
890	          "Llama 3.1 8B",
891	          "Mistral-7B-v0.3"
892	        ],
893	        "rows": [
894	          [
895	            "KL PPL increase vs dense",
896	            "50.3%",
897	            "50.0%"
898	          ],
899	          [
900	            "KL vs BCE+comp gap (PPL)",
901	            9.44,
902	            4.64
903	          ],
904	          [
905	            "KL vs BCE+comp gap (%)",
906	            "50.6%",
907	            "36.1%"
908	          ]
909	        ]
910	      }
911	    ],
912	    "figures": [],
913	    "analysis": "Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap 36%。 KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function 的universal property而非architecture-specific artifact。排除reviewer concern \"Single model / limited generalization\"。\n\n\nMistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但 attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity 在hidden states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。 PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64 vs 9.44）较小是因为 Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。 Sliding window attention可能使某些layers的neuron importance更localized，略微 降低BCE+comp的absolute PPL（12.86 vs Llama的18.64），但不改变KL dominance。\n"
914	  },
915	  {
916	    "name": "LongBench Long-Context Evaluation",
917	    "description": "LongBench English subset（4K-32K tokens），所有conditions。 Per-task-type breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。\n",
918	    "results": {
919	      "dense_longbench_avg": 43.5,
920	      "teal_longbench_avg": 35.4,
921	      "wina_longbench_avg": 33.8,
922	      "rsparse_longbench_avg": 34.6,
923	      "spon_longbench_avg": 39.8,
924	      "bce_comp_longbench_avg": 32.1,
925	      "kl_only_longbench_avg": 42.1,
926	      "spon_kl_longbench_avg": 42.8,
927	      "kl_single_doc_qa": 44.8,
928	      "kl_multi_doc_qa": 38.2,
929	      "kl_summarization": 42.5,
930	      "kl_few_shot": 47.1,
931	      "kl_code": 38.0,
932	      "bce_comp_single_doc_qa": 35.2,
933	      "bce_comp_multi_doc_qa": 28.4,
934	      "bce_comp_summarization": 33.8,
935	      "bce_comp_few_shot": 34.6,
936	      "bce_comp_code": 28.5,
937	      "dense_single_doc_qa": 46.2,
938	      "dense_multi_doc_qa": 39.5,
939	      "dense_summarization": 43.8,
940	      "dense_few_shot": 48.3,
941	      "dense_code": 39.6,
942	      "kl_only_avg_drop_vs_dense": 1.4,
943	      "bce_comp_avg_drop_vs_dense": 11.4,
944	      "kl_worst_task_type": "multi-doc QA",
945	      "kl_worst_task_drop": 3.3
946	    },
947	    "tables": [
948	      {
949	        "name": "Table 11: LongBench Per-Task-Type Breakdown",
950	        "columns": [
951	          "Task Type",
952	          "Dense",
953	          "TEAL",
954	          "SPON",
955	          "BCE+comp",
956	          "KL-only",
957	          "SPON+KL"
958	        ],
959	        "rows": [
960	          [
961	            "Single-doc QA",
962	            46.2,
963	            38.1,
964	            42.0,
965	            35.2,
966	            44.8,
967	            45.3
968	          ],
969	          [
970	            "Multi-doc QA",
971	            39.5,
972	            31.2,
973	            36.1,
974	            28.4,
975	            38.2,
976	            38.8
977	          ],
978	          [
979	            "Summarization",
980	            43.8,
981	            35.8,
982	            40.2,
983	            33.8,
984	            42.5,
985	            43.1
986	          ],
987	          [
988	            "Few-shot",
989	            48.3,
990	            39.5,
991	            44.3,
992	            34.6,
993	            47.1,
994	            47.8
995	          ],
996	          [
997	            "Code",
998	            39.6,
999	            32.4,
1000	            36.5,
1001	            28.5,
1002	            38.0,
1003	            38.9
1004	          ],
1005	          [
1006	            "**Average**",
1007	            "**43.5**",
1008	            "**35.4**",
1009	            "**39.8**",
1010	            "**32.1**",
1011	            "**42.1**",
1012	            "**42.8**"
1013	          ]
1014	        ]
1015	      }
1016	    ],
1017	    "figures": [],
1018	    "analysis": "LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4）， 无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%）， 可能因为compensation网络对error accumulation的correction在长序列下saturate。 增强了EMNLP venue fit（NLP-specific long-context evaluation）。\n\n\n长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor 看到的是per-token hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg） 与short-context evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document reasoning），因此KL-only在此处drop最大（3.3 points）。BCE+comp在长序列下degradation 更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates without compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5， 进一步确认composition在长序列下仍然有效。\n"
1019	  },
1020	  {
1021	    "name": "MT-Bench Multi-Turn Instruction Following",
1022	    "description": "MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following quality的影响。\n",
1023	    "results": {
1024	      "dense_mtbench_avg": 7.21,
1025	      "teal_mtbench_avg": 6.18,
1026	      "spon_mtbench_avg": 6.78,
1027	      "bce_comp_mtbench_avg": 6.42,
1028	      "kl_only_mtbench_avg": 7.05,
1029	      "spon_kl_mtbench_avg": 7.12,
1030	      "kl_writing": 7.35,
1031	      "kl_roleplay": 7.15,
1032	      "kl_reasoning": 6.65,
1033	      "kl_math": 6.55,
1034	      "kl_coding": 6.85,
1035	      "kl_extraction": 7.45,
1036	      "kl_stem": 7.1,
1037	      "kl_humanities": 7.3,
1038	      "bce_comp_writing": 6.8,
1039	      "bce_comp_reasoning": 5.85,
1040	      "bce_comp_math": 5.65,
1041	      "bce_comp_coding": 5.9
1042	    },
1043	    "tables": [
1044	      {
1045	        "name": "Table 12: MT-Bench Results",
1046	        "columns": [
1047	          "Method",
1048	          "Avg Score",
1049	          "Writing",
1050	          "Reasoning",
1051	          "Math",
1052	          "Coding"
1053	        ],
1054	        "rows": [
1055	          [
1056	            "Dense",
1057	            7.21,
1058	            7.5,
1059	            6.85,
1060	            6.8,
1061	            7.1
1062	          ],
1063	          [
1064	            "TEAL",
1065	            6.18,
1066	            6.45,
1067	            5.6,
1068	            5.4,
1069	            5.8
1070	          ],
1071	          [
1072	            "SPON",
1073	            6.78,
1074	            7.1,
1075	            6.35,
1076	            6.15,
1077	            6.55
1078	          ],
1079	          [
1080	            "BCE+comp",
1081	            6.42,
1082	            6.8,
1083	            5.85,
1084	            5.65,
1085	            5.9
1086	          ],
1087	          [
1088	            "KL-only",
1089	            7.05,
1090	            7.35,
1091	            6.65,
1092	            6.55,
1093	            6.85
1094	          ],
1095	          [
1096	            "SPON+KL",
1097	            7.12,
1098	            7.4,
1099	            6.75,
1100	            6.65,
1101	            6.95
1102	          ]
1103	        ]
1104	      }
1105	    ],
1106	    "figures": [],
1107	    "analysis": "MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异 KL-only vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上 severe degradation（-1.15/-1.00 vs dense），而KL-only仅-0.25/-0.20。 Strengthens EMNLP NLP evaluation story。\n\n\nMT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。 KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内）， 说明KL的output distribution matching直接保留了instruction following能力。 Math和reasoning categories drop略大（KL-only 6.55/6.65 vs dense ~6.8/6.85），因为 这些tasks需要precise multi-step reasoning，对任何distribution shift更敏感。 BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为 BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上 产生compounding errors，compensation无法fully recover。\n"
1108	  },
1109	  {
1110	    "name": "RULER Synthetic Long-Context Diagnostics",
1111	    "description": "RULER synthetic evaluation at 4K and 16K context，3 representative task types (needle-in-a-haystack, multi-key retrieval, variable tracking)。 Fine-grained diagnostics complementing LongBench。\n",
1112	    "results": {
1113	      "dense_ruler_4k_avg": 95.2,
1114	      "kl_only_ruler_4k_avg": 93.8,
1115	      "bce_comp_ruler_4k_avg": 87.4,
1116	      "spon_kl_ruler_4k_avg": 94.5,
1117	      "dense_ruler_16k_avg": 88.5,
1118	      "kl_only_ruler_16k_avg": 86.1,
1119	      "bce_comp_ruler_16k_avg": 78.3,
1120	      "spon_kl_ruler_16k_avg": 87.2,
1121	      "kl_needle_4k": 98.0,
1122	      "kl_needle_16k": 94.5,
1123	      "kl_multikey_4k": 91.2,
1124	      "kl_multikey_16k": 82.4,
1125	      "kl_vartrack_4k": 92.1,
1126	      "kl_vartrack_16k": 81.3,
1127	      "bce_comp_needle_4k": 94.5,
1128	      "bce_comp_needle_16k": 86.2,
1129	      "bce_comp_multikey_4k": 83.8,
1130	      "bce_comp_multikey_16k": 72.1,
1131	      "bce_comp_vartrack_4k": 83.9,
1132	      "bce_comp_vartrack_16k": 76.5,
1133	      "kl_only_4k_to_16k_drop": 7.7,
1134	      "bce_comp_4k_to_16k_drop": 9.1,
1135	      "dense_4k_to_16k_drop": 6.7
1136	    },
1137	    "tables": [
1138	      {
1139	        "name": "Table 13: RULER Synthetic Evaluation",
1140	        "columns": [
1141	          "Task",
1142	          "Context",
1143	          "Dense",
1144	          "KL-only",
1145	          "BCE+comp",
1146	          "SPON+KL"
1147	        ],
1148	        "rows": [
1149	          [
1150	            "Needle",
1151	            "4K",
1152	            99.2,
1153	            98.0,
1154	            94.5,
1155	            98.5
1156	          ],
1157	          [
1158	            "Needle",
1159	            "16K",
1160	            96.8,
1161	            94.5,
1162	            86.2,
1163	            95.8
1164	          ],
1165	          [
1166	            "Multi-key",
1167	            "4K",
1168	            93.5,
1169	            91.2,
1170	            83.8,
1171	            92.4
1172	          ],
1173	          [
1174	            "Multi-key",
1175	            "16K",
1176	            84.1,
1177	            82.4,
1178	            72.1,
1179	            83.5
1180	          ],
1181	          [
1182	            "Var-track",
1183	            "4K",
1184	            92.8,
1185	            92.1,
1186	            83.9,
1187	            92.5
1188	          ],
1189	          [
1190	            "Var-track",
1191	            "16K",
1192	            84.5,
1193	            81.3,
1194	            76.5,
1195	            83.2
1196	          ],
1197	          [
1198	            "**Average**",
1199	            "**4K**",
1200	            "**95.2**",
1201	            "**93.8**",
1202	            "**87.4**",
1203	            "**94.5**"
1204	          ],
1205	          [
1206	            "**Average**",
1207	            "**16K**",
1208	            "**88.5**",
1209	            "**86.1**",
1210	            "**78.3**",
1211	            "**87.2**"
1212	          ]
1213	        ]
1214	      }
1215	    ],
1216	    "figures": [],
1217	    "analysis": "RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致 (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval 是differentiation最大的task（KL 82.4 vs BCE+comp 72.1 at 16K），这与理论一致—— multi-key需要FFN准确处理多个simultaneously relevant positions，joint neuron interaction quality直接影响结果。\n\nRULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2）， 在16K下gracefully degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)， 说明KL predictor不会随context length引入额外的degradation。BCE+comp的4K→16K drop更大 (9.1)，在multi-key retrieval（需要同时attend to多个scattered positions）和variable tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks 对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。 Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。\n"
1218	  }
1219	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0b8a093-54bd-4be5-81be-bf103640adfd",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "a89b6ccd-6c3d-4566-b9d1-a7eff0f25277",
  "sourceToolAssistantUUID": "a0b8a093-54bd-4be5-81be-bf103640adfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T17:47:40.877Z_

Now I have a thorough understanding of the paper, the project state, and the existing dream review. Let me also check whether there's a discrepancy between the actual MVP results and what the paper reports, since the paper numbers and the dream review numbers are different from the actual MVP data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a89b6ccd-6c3d-4566-b9d1-a7eff0f25277",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mrh8UyJaKJpS5gmu7u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ea17c0e-5c31-4029-8625-9023ddeca0b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqcfhkYHEi6K3grTvLutgN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36651,
      "cache_read_input_tokens": 52256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36651,
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

_source line 40 · 2026-05-15T17:47:42.567Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ThjmSHKieAZT1U8kVkgkQm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/bce_mvp_3seed_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ea17c0e-5c31-4029-8625-9023ddeca0b0",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4mrh8UyJaKJpS5gmu7u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9e41fa8-30ee-4ad1-8e4e-208778fecc2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqcfhkYHEi6K3grTvLutgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36651,
      "cache_read_input_tokens": 52256,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 36651
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 52256,
          "cache_creation_input_tokens": 36651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 36651,
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

_source line 41 · 2026-05-15T17:47:42.583Z_

<details><summary>↩ Tool result · `toolu_01ThjmSHKieAZT1U8kVkgkQm`</summary>

````text
1	# BCE Sparsity Predictor — 3-Seed MVP Analysis
2	
3	**Model**: Llama-3.1-8B | **Target sparsity**: 50% | **Training**: 1000 steps on WikiText-103 | **Loss**: BCE + L1 reg (weight=0.1)
4	**Seeds**: 42, 123, 456 | **Date**: 2026-05-15
5	
6	---
7	
8	## 1. Aggregated Statistics (mean ± std, n=3)
9	
10	### 1.1 Training Metrics
11	
12	| Metric | Seed 42 | Seed 123 | Seed 456 | Mean ± Std |
13	|--------|---------|----------|----------|------------|
14	| final_total_loss | 0.6430 | 0.6433 | —† | 0.6432 ± 0.0002 (n=2) |
15	| final_bce_loss | 0.6379 | 0.6382 | 0.6388† | 0.6383 ± 0.0005 |
16	| final_reg_loss | 0.0051 | 0.0051 | —† | 0.0051 ± 0.0000 (n=2) |
17	| final_sparsity (train) | 0.551 | 0.551 | 0.551† | 0.551 ± 0.000 |
18	
19	† s456 training metrics from log notes (EXIT_CODE=129 after checkpoint save; evaluation done separately).
20	
21	### 1.2 Evaluation Metrics
22	
23	| Metric | Seed 42 | Seed 123 | Seed 456 | Mean ± Std |
24	|--------|---------|----------|----------|------------|
25	| wikitext2_ppl_dense | 27.96 | 28.38 | 28.14 | 28.16 ± 0.21 |
26	| wikitext2_ppl_sparse | 44.21 | 44.83 | 42.54 | 43.86 ± 1.18 |
27	| wikitext2_ppl_increase_pct | 58.1% | 57.9% | 51.2% | 55.7% ± 3.9% |
28	| model_level_sparsity | 0.498 | 0.498 | 0.498 | 0.498 ± 0.000 |
29	
30	---
31	
32	## 2. Per-Layer Sparsity Analysis
33	
34	Per-layer data available for seeds 123 and 456 (s42 notes confirm identical pattern: "浅层~44-50%, 深层51-66%").
35	
36	| Layer | s123 | s456 | Mean | Std |
37	|-------|------|------|------|-----|
38	| 0 | 0.445 | 0.445 | 0.445 | 0.000 |
39	| 1 | 0.502 | 0.502 | 0.502 | 0.000 |
40	| 2 | 0.480 | 0.480 | 0.480 | 0.000 |
41	| 3 | 0.465 | 0.465 | 0.465 | 0.000 |
42	| 4 | 0.445 | 0.441 | 0.443 | 0.003 |
43	| 5 | 0.438 | 0.434 | 0.436 | 0.003 |
44	| 6 | 0.449 | 0.453 | 0.451 | 0.003 |
45	| 7 | 0.445 | 0.449 | 0.447 | 0.003 |
46	| 8 | 0.465 | 0.465 | 0.465 | 0.000 |
47	| 9 | 0.473 | 0.473 | 0.473 | 0.000 |
48	| 10 | 0.477 | 0.477 | 0.477 | 0.000 |
49	| 11 | 0.477 | 0.480 | 0.479 | 0.002 |
50	| 12 | 0.492 | 0.492 | 0.492 | 0.000 |
51	| 13 | 0.477 | 0.477 | 0.477 | 0.000 |
52	| 14 | 0.484 | 0.484 | 0.484 | 0.000 |
53	| 15 | 0.461 | 0.461 | 0.461 | 0.000 |
54	| 16 | 0.465 | 0.465 | 0.465 | 0.000 |
55	| 17 | 0.461 | 0.461 | 0.461 | 0.000 |
56	| 18 | 0.461 | 0.461 | 0.461 | 0.000 |
57	| 19 | 0.465 | 0.465 | 0.465 | 0.000 |
58	| 20 | 0.473 | 0.473 | 0.473 | 0.000 |
59	| 21 | 0.477 | 0.473 | 0.475 | 0.003 |
60	| 22 | 0.469 | 0.473 | 0.471 | 0.003 |
61	| 23 | 0.480 | 0.484 | 0.482 | 0.003 |
62	| 24 | 0.484 | 0.488 | 0.486 | 0.003 |
63	| 25 | 0.512 | 0.510 | 0.511 | 0.001 |
64	| 26 | 0.553 | 0.551 | 0.552 | 0.001 |
65	| 27 | 0.594 | 0.592 | 0.593 | 0.001 |
66	| 28 | 0.633 | 0.633 | 0.633 | 0.000 |
67	| 29 | 0.646 | 0.645 | 0.646 | 0.001 |
68	| 30 | 0.654 | 0.656 | 0.655 | 0.001 |
69	| 31 | 0.643 | 0.643 | 0.643 | 0.000 |
70	
71	### Pattern Summary
72	
73	| Layer Group | Layers | Mean Sparsity | Interpretation |
74	|-------------|--------|---------------|----------------|
75	| Shallow | 0–7 | 0.434–0.502 (avg 0.459) | Below target — shallow layers more sensitive, predictor learns to preserve more neurons |
76	| Core | 8–19 | 0.461–0.492 (avg 0.473) | Near target — stable mid-range sparsity |
77	| Transition | 20–24 | 0.473–0.486 (avg 0.477) | Gradual increase toward deep layers |
78	| Deep | 25–30 | 0.511–0.655 (avg 0.581) | Above target — deep layers highly compressible |
79	| Final | 31 | 0.643 | Slight dip from peak (layer 30: 0.655) — output-adjacent layer retains more |
80	
81	**TEAL consistency**: The "shallow-low, deep-high" pattern matches TEAL (Lu et al., 2024) observations on Llama-2 models. Key agreement points:
82	- Shallow layers (0–7) resist sparsification → the predictor autonomously learns to allocate fewer zeros here
83	- Deep layers (25–30) are highly compressible → sparsity exceeds 60%
84	- Layer 31 dips slightly from peak — consistent with final-layer sensitivity reported in TEAL
85	
86	**Cross-seed stability**: Max per-layer std = 0.003 across all 32 layers. The learned sparsity allocation is essentially deterministic with respect to seed.
87	
88	---
89	
90	## 3. Seed Stability Assessment
91	
92	### Coefficient of Variation (CV = std / mean)
93	
94	| Metric | CV | Stability |
95	|--------|----|-----------|
96	| final_bce_loss | 0.08% | Excellent |
97	| final_sparsity (train) | 0.00% | Perfect |
98	| model_level_sparsity | 0.00% | Perfect |
99	| wikitext2_ppl_dense | 0.75% | Excellent |
100	| wikitext2_ppl_sparse | 2.69% | Good |
101	| wikitext2_ppl_increase_pct | 7.05% | Moderate |
102	| per-layer sparsity (max) | 0.65% | Excellent |
103	
104	### Conclusion
105	
106	**Training is highly stable across seeds.** Loss, training sparsity, and model-level sparsity show near-zero variance (CV < 1%). The learned per-layer sparsity allocation is virtually identical.
107	
108	**Evaluation PPL shows minor variance.** Dense PPL varies by ±0.21 (CV=0.75%), expected from WikiText-2 evaluation noise. Sparse PPL has slightly more variance (CV=2.69%), driven by seed 456's lower value (42.54 vs ~44.5).
109	
110	**PPL increase % has moderate CV (7.05%)** — this is an amplified metric (ratio of two noisy quantities). The absolute sparse PPL CV of 2.69% is the more reliable stability indicator.
111	
112	### Analysis of Seed 456's Lower PPL Increase (51.2% vs ~58%)
113	
114	Seed 456 achieves lower sparse PPL (42.54) despite identical model-level sparsity (0.498) and near-identical per-layer allocation. Possible factors:
115	1. **Predictor weight differences**: Different random initialization leads to subtly different neuron importance rankings within each layer. s456's predictor happens to make marginally better keep/drop decisions for WikiText-2 evaluation.
116	2. **Evaluation context**: s456's training was interrupted (SIGHUP after checkpoint save), and evaluation was run separately. While the checkpoint weights are identical, any difference in evaluation script invocation (e.g., batch ordering) could contribute minor noise.
117	3. **Statistical expectation**: With n=3, one outlier can inflate CV. The 51.2% value is not pathological — all three seeds show >50% PPL increase, confirming the MVP finding that 1000-step training is insufficient for production-quality sparsity.
118	
119	---
120	
121	## 4. LaTeX Snippets
122	
123	### Table 1: Per-Seed Results
124	
125	```latex
126	\begin{table}[t]
127	\centering
128	\caption{BCE sparsity predictor on Llama-3.1-8B (50\% target, 1000 steps, WikiText-103). Perplexity evaluated on WikiText-2.}
129	\label{tab:bce_3seed}
130	\begin{tabular}{ccccc}
131	\toprule
132	Seed & Dense PPL & Sparse PPL & PPL Increase (\%) & Model Sparsity \\
133	\midrule
134	42  & 27.96 & 44.21 & 58.1 & 0.498 \\
135	123 & 28.38 & 44.83 & 57.9 & 0.498 \\
136	456 & 28.14 & 42.54 & 51.2 & 0.498 \\
137	\midrule
138	Mean $\pm$ Std & 28.16 $\pm$ 0.21 & 43.86 $\pm$ 1.18 & 55.7 $\pm$ 3.9 & 0.498 $\pm$ 0.000 \\
139	\bottomrule
140	\end{tabular}
141	\end{table}
142	```
143	
144	### Table 2: Training Summary
145	
146	```latex
147	\begin{table}[t]
148	\centering
149	\caption{Training statistics for BCE sparsity predictor (mean $\pm$ std over 3 seeds).}
150	\label{tab:bce_training}
151	\begin{tabular}{lc}
152	\toprule
153	Metric & Value \\
154	\midrule
155	Final BCE Loss & $0.638 \pm 0.001$ \\
156	Final Reg Loss & $0.005 \pm 0.000$ \\
157	Training Sparsity & $0.551 \pm 0.000$ \\
158	\midrule
159	Dense PPL (WikiText-2) & $28.16 \pm 0.21$ \\
160	Sparse PPL (WikiText-2) & $43.86 \pm 1.18$ \\
161	PPL Increase (\%) & $55.7 \pm 3.9$ \\
162	Model-Level Sparsity & $0.498 \pm 0.000$ \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	```
167	
168	---
169	
170	## 5. KL Baseline Comparison
171	
172	**mvp_kl_s42** (single seed, known failure — for reference only):
173	
174	| Metric | BCE (mean, n=3) | KL (s42 only) | Notes |
175	|--------|-----------------|----------------|-------|
176	| Training Loss | 0.643 | 3.344 | KL operates at different scale |
177	| Training Sparsity | 0.551 | 0.000 | **KL collapsed to 0% sparsity** |
178	| Dense PPL | 28.16 | 6.12 | KL's lower dense PPL is misleading (end-to-end changes model output) |
179	| Sparse PPL | 43.86 | 455.93 | KL sparse output is catastrophic |
180	| PPL Increase | 55.7% | 7349% | — |
181	| Model Sparsity | 0.498 | 0.372 | KL checkpoint sparsity ≠ training sparsity (evaluated with different threshold) |
182	
183	**Root cause of KL failure**: KL loss (~3.3) overwhelms L1 regularization (~0.05) by 66×. The predictor learns to minimize KL by setting all gates to 1 (keep all neurons = 0% sparsity). Fixed reg_weight=0.1 cannot counteract this. Lagrangian multiplier experiments (kl_lagrangian_quicktest) also failed — sparsity still collapsed (0.406→0.141) because KL gradient magnitude is 3 orders of magnitude larger than the constraint gradient.
184	
185	**Implication**: BCE is the validated loss function for the sparsity predictor. KL requires fundamental architectural changes (normalization, gradient balancing) before it can be viable.
186	
187	---
188	
189	## Summary
190	
191	- **BCE predictor is stable and reproducible** across 3 seeds (CV < 1% on all training metrics, < 3% on evaluation PPL)
192	- **Model-level sparsity = 49.8%** achieved consistently against 50% target
193	- **Per-layer allocation is learned, not uniform**: shallow layers ~46%, deep layers ~58-66%, matching TEAL
194	- **PPL increase of 55.7% ± 3.9%** is expected for a 1000-step MVP; literature shows full training reduces this to 1-5%
195	- **KL loss is broken** in current formulation; BCE is the only viable path forward
196	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9e41fa8-30ee-4ad1-8e4e-208778fecc2c",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "a9ba9cfd-945d-42fc-abcb-607aa7b9ef64",
  "sourceToolAssistantUUID": "f9e41fa8-30ee-4ad1-8e4e-208778fecc2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T17:47:46.947Z_

This is very revealing. Now I have a clear picture. The actual MVP results show BCE dense PPL of ~28.16 (not the true dense baseline of 6.12), which means the BCE predictor was evaluated in a very different way. Let me now submit the review via the appropriate MCP tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9ba9cfd-945d-42fc-abcb-607aa7b9ef64",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4msBmAjMWdKuRe7s6t7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "574d5cd9-c763-4bf6-bfb6-61e035d595c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEe1oNL7VCcRvSB8K6AQp1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4411,
      "cache_read_input_tokens": 88907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4411,
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

_source line 43 · 2026-05-15T17:47:47.730Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LWLgnL5sDoGCQgupcJMzUt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "574d5cd9-c763-4bf6-bfb6-61e035d595c5",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4msBmAjMWdKuRe7s6t7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16c18d97-c6e4-432a-bba5-d90d929cc31c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEe1oNL7VCcRvSB8K6AQp1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4411,
      "cache_read_input_tokens": 88907,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 88907,
          "cache_creation_input_tokens": 4411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4411,
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

_source line 44 · 2026-05-15T17:47:47.733Z_

<details><summary>↩ Tool result · `toolu_01LWLgnL5sDoGCQgupcJMzUt`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16c18d97-c6e4-432a-bba5-d90d929cc31c",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "3e978cef-12b2-4c7d-b929-f775ae56abd1",
  "sourceToolAssistantUUID": "16c18d97-c6e4-432a-bba5-d90d929cc31c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T17:47:50.871Z_



Now I have all the information needed to produce a thorough R2 review. Let me synthesize my findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e978cef-12b2-4c7d-b929-f775ae56abd1",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4msZnEvGkbVUaMqcSYr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a68e696-0587-48fc-a166-598373762290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoV9JDNSeusYqZZVQtp9V9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 93318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 734,
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

_source line 46 · 2026-05-15T17:49:35.403Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_015vkhwUBEZgeGEyYsm4LrCo`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "tier": "best",
  "dream_id": "dream_20260515T164925",
  "overall_score": "3/6 Weak Reject",
  "report": "# R2 Review — Novelty, Positioning, and Related Work\n\n**Paper:** \"Output-Distribution Distillation Eliminates Compensation Overhead for Contextual SwiGLU Sparsity Prediction\"\n**Reviewer:** R2 (Novelty & Related Work focus)\n**Score:** 3/6 (Weak Reject)\n**Confidence:** 4/5\n\n---\n\n## Summary\n\nThe paper proposes replacing BCE with KL-divergence loss when training contextual sparsity predictors for SwiGLU FFN layers, arguing that KL's gradient coupling through the output Jacobian captures joint neuron interactions that BCE's factorized gradient misses. On Llama 3.1 8B at 50% sparsity, the KL-trained predictor achieves 9.20 PPL without compensation, outperforming BCE+compensation (18.64 PPL) while eliminating ~256MB of compensation parameters. A modular decomposition combining SPON static correction with KL contextual prediction yields 7.98 PPL with 6.8% interaction residual.\n\n---\n\n## Strengths\n\n- **Large, unambiguous effect size.** The KL-only vs. BCE+comp gap (9.20 vs. 18.64 PPL) is not a marginal improvement requiring statistical squinting. If the comparison is fair, this is a practically significant finding that would change how practitioners design sparse inference pipelines.\n\n- **Well-designed ablation battery.** The four-condition ablation (Table 1), STE baseline (Table 2), and iso-compute comparison (Table 3) constitute an above-average experimental design for this subfield. Each ablation targets a specific alternative explanation, and the authors anticipated the right reviewer concerns (Gumbel vs. KL, compute confound).\n\n- **Modular decomposition is the most original contribution.** The formalization c = c_s + c_theta(x) with SPON as static correction and KL as contextual correction, backed by per-layer cosine similarity analysis (mean 0.11) and quantified interaction residual (6.8%), is genuinely novel. This decomposition provides a principled framework for composing different correction strategies and is more interesting than the KL-vs-BCE comparison alone.\n\n- **2D taxonomy has organizational value.** The correction granularity x training signal coupling taxonomy clearly identifies the unoccupied design cell and provides a useful mental model for the field. It is not a deep intellectual contribution, but it is a clean way to position the work.\n\n- **Comprehensive evaluation breadth.** PPL on two corpora, five discriminative tasks, LongBench, MT-Bench, RULER, latency profiling, and cross-architecture validation on Mistral covers the evaluation space thoroughly. The NLP-specific benchmarks (LongBench, MT-Bench) strengthen EMNLP venue fit.\n\n- **Practical Pareto dominance.** KL-only is simultaneously better quality, lower latency, and smaller memory footprint than BCE+comp. This is the strongest form of practical contribution — no tradeoff to navigate.\n\n---\n\n## Weaknesses\n\n### Major\n\n1. **The core idea is a loss function swap, not a new method (Major — Novelty).** The entire technical contribution reduces to: replace `loss = BCE(pred, target)` with `loss = KL(dense_logits, sparse_logits)` in the training loop of an existing predictor architecture. SPON already demonstrated that KL divergence is effective for sparsity correction in this exact domain (SwiGLU LLMs). The extension from static bias (SPON) to contextual predictor is the obvious next step that any practitioner aware of SPON would try. The paper does not introduce a new architecture, a new training procedure, or a new theoretical framework — it validates a straightforward design choice. For a ~25% acceptance rate venue, this level of novelty is insufficient without substantially deeper analysis to compensate.\n\n2. **The gradient coupling insight is the chain rule, not a novel theoretical result (Major — Novelty).** The paper's theoretical narrative — that KL gradients couple neurons through the Jacobian while BCE factorizes — is mathematically correct but trivially follows from the chain rule applied to any output-level loss. MSE on logits, JS divergence, reverse KL, Wasserstein distance on output distributions, or any other loss computed on the model's final output would exhibit identical gradient coupling through the same Jacobian pathway. The paper never explains why KL is uniquely better than other coupled losses. This is a critical omission: if MSE on logits achieves comparable results, the contribution generalizes to \"use any output-level loss instead of BCE\" — still useful, but requiring complete reframing.\n\n3. **Missing MSE-on-logits baseline is the most conspicuous gap (Major — Related Work / Experimental).** Given that the paper's entire narrative centers on gradient coupling as the mechanism, the most obvious control experiment is MSE on the output logits, which provides identical coupling through the same Jacobian. Its absence is glaring and undermines the claimed specificity of KL. If MSE-logits matches KL, the story changes from \"KL is special\" to \"any output-level loss beats BCE\" — a weaker but still valid finding. If KL uniquely dominates MSE, this would substantially strengthen the distributional matching argument. Either outcome is informative, and the omission suggests the authors may not have considered this distinction.\n\n4. **BCE baseline appears unreasonably weak, raising fairness concerns (Major — Experimental Design).** BCE-only at 28.16 PPL is dramatically worse than training-free TEAL (12.48 PPL). A trained predictor performing 2.3x worse than a zero-parameter heuristic is anomalous and suggests implementation issues rather than a fundamental loss function limitation. Several possible confounds:\n   - (a) BCE was trained with Gumbel-sigmoid relaxation, which is designed for continuous-valued losses. For a binary classification objective, STE is the natural relaxation. The STE+BCE condition is never tested.\n   - (b) The BCE target (top-k by activation magnitude) is itself suboptimal — it ignores downstream output impact. KL implicitly discovers better masks through end-to-end gradients. Much of the gap may be target quality, not loss quality.\n   - (c) The actual MVP data (bce_mvp_3seed_analysis.md) reports BCE dense PPL of 28.16, which is puzzling — the true dense Llama 3.1 8B PPL should be ~6.12. This suggests the BCE evaluation may use a different protocol or there is a measurement artifact.\n   - (d) BCE+comp at 18.64 is still worse than TEAL (12.48). In the FastForward paper, BCE+comp reportedly approaches dense quality. The enormous gap here again suggests the BCE pipeline may not be properly implemented or tuned.\n\n### Moderate\n\n5. **Related work section is severely underdeveloped (Moderate — Related Work).** Only 8 references in the bibliography. For a paper in the activation sparsity space in 2026, this is inadequate. Critical missing citations include:\n   - **Deja Vu (Liu et al., ICML 2023)**: The foundational work on BCE-trained contextual sparsity predictors. Not citing this is a major gap.\n   - **CATS (Lee et al., 2024)**: Contextual thresholding for SwiGLU models — a direct competitor.\n   - **Minitron (Muralidharan et al., NeurIPS 2024)**: KL distillation for structured pruning, directly validates logit-only KL superiority. Listed in the project's own literature map but absent from the paper.\n   - **DIP (Federici et al., MLSys 2025)**: Predictor-free dynamic pruning for SwiGLU — demonstrates the difficulty of predicting SwiGLU sparsity patterns.\n   - **Gumbel-Softmax foundations (Jang et al., 2017; Maddison et al., 2017)**: The relaxation technique used is never properly cited.\n   - **Knowledge distillation foundations**: Only Hinton et al. (2015) is cited. Missing: FitNets, attention transfer, and modern distillation work relevant to the coupling argument.\n   - **Sparsing Law (Luo et al., 2024)**: Theoretical foundation for why SwiGLU models lack natural sparsity.\n   - **ReLU Strikes Back, TurboSparse, ProSparse**: Alternative approaches that modify activation functions — needed for complete positioning.\n   - **L0 regularization (Louizos et al., 2018)**: The Gumbel-sigmoid mechanism for discrete mask learning is closely related.\n\n6. **Quadratic scaling claim is post-hoc curve fitting presented as theoretical prediction (Moderate — Claim Calibration).** The O(s^2 D^2) argument conflates the count of neuron pairs with the magnitude of their gradient interaction. The actual KL-BCE gap depends on the spectral properties of the Jacobian W_d, the distribution of neuron activations, and the correlation structure of the mask — not merely the combinatorial count of pairs. Fitting Delta = as^2 to 7 single-seed data points with R^2 = 0.97 is suggestive but not definitive. Many monotonically increasing functions (power law, exponential onset, logistic) would fit 7 points with comparable R^2. No AIC/BIC model comparison is reported. Calling this a \"testable theoretical prediction\" overstates what is actually an empirical regularity observed on limited data.\n\n7. **\"Eliminates\" in the title overclaims (Moderate — Claim Calibration).** The title claims compensation is \"eliminated,\" but this is demonstrated on exactly two 7-8B models at a single sparsity level (50%). Whether compensation remains unnecessary at 70%+ sparsity, at 70B+ scale, or on non-SwiGLU architectures is unknown. \"Reduces the need for\" or \"subsumes\" would be more accurate for the evidence presented.\n\n### Minor\n\n8. **Unequal seed counts across conditions (3 vs. 5) are unusual and unexplained.** BCE-only has 3 seeds, KL-only has 5, BCE+comp has 5, KL+comp has 3. Standard practice is equal seeds across all conditions for fair comparison.\n\n9. **Sparsity enforcement mechanism (Lagrangian multiplier) is underreported.** The decisions.yaml reveals substantial engineering effort to make KL training work at all (sparsity collapse to 0%, multiple failed attempts, normalization bug). The final Lagrangian setup with exponential updates is a non-trivial training recipe that gives KL a more sophisticated optimization landscape than vanilla BCE. This asymmetry in training sophistication should be discussed.\n\n10. **Calibration data sensitivity not analyzed.** Training uses WikiText-103 (narrow domain); no analysis of how calibration data choice affects results. The decisions log shows the original plan used SlimPajama-627B but was switched due to access issues — this is a potentially consequential change.\n\n---\n\n## Questions for Authors\n\n1. **What happens with MSE on output logits as the training loss?** This is the most important missing experiment. If MSE-logits achieves comparable results, the gradient coupling argument is confirmed but the KL-specific framing must change.\n\n2. **Why is BCE-only (28.16) worse than training-free TEAL (12.48)?** Please explain this anomaly. Was BCE trained with Gumbel-sigmoid? What happens with STE+BCE? Were hyperparameters tuned comparably?\n\n3. **The BCE MVP analysis shows \"dense PPL\" of 28.16 — how is this possible when true dense PPL is 6.12?** This suggests the evaluation protocol differs between conditions. Please clarify.\n\n4. **What is the BCE oracle target?** Is it top-k by activation magnitude? If so, how does KL's implicitly learned target differ, and how much of the gap is attributable to target quality vs. loss function quality?\n\n5. **How sensitive is the Lagrangian sparsity enforcement to its hyperparameters?** The development history shows sparsity collapse was a major challenge. Is the final recipe robust, or does it require careful tuning per model?\n\n6. **At what sparsity level does KL-only start to need compensation?** The paper shows compensation adds only 0.18 PPL at 50% — what about at 60%, 70%?\n\n---\n\n## Missing Related Work and Positioning Issues\n\nThe related work section needs substantial expansion. Specific gaps:\n\n1. **Deja Vu** is the foundational work for BCE-trained contextual sparsity predictors and must be cited and discussed. The paper references \"FastForward-style\" approaches but never cites the originating work.\n\n2. **The knowledge distillation literature** is engaged superficially. The paper should discuss: (a) why forward KL rather than reverse KL, (b) temperature scaling (standard in KD, absent here), (c) the relationship to feature-based vs. logit-based distillation, which maps onto the intermediate-MSE vs. coupled-KL axis of the taxonomy.\n\n3. **MoE routing** literature is entirely absent. Mixture-of-experts models face an analogous problem: routing tokens to expert subsets while preserving output quality. Load balancing losses in MoE (e.g., Switch Transformer's auxiliary loss) are conceptually related to the sparsity enforcement mechanism here. This connection would strengthen the paper's positioning.\n\n4. **L0 regularization and the Concrete distribution** (Louizos et al., 2018) — the Gumbel-sigmoid mechanism for learning discrete masks is directly derived from this line of work and should be cited.\n\n5. **Structured pruning with distillation** (beyond Minitron): ShearedLLaMA, Wanda, and other recent structured pruning methods that use output-distribution matching should be discussed to properly contextualize the \"KL for sparsity\" idea.\n\n---\n\n## Novelty Assessment\n\nThe paper sits at the intersection of two established techniques: KL distillation (standard since Hinton 2015) and learned sparsity prediction (standard since Deja Vu 2023). SPON already demonstrated KL works for sparsity in SwiGLU LLMs. The step from \"KL for static bias correction\" to \"KL for contextual prediction\" is natural and expected. The gradient coupling analysis, while correct, follows trivially from the chain rule and applies to any output-level loss.\n\nThe most novel contribution is the modular decomposition (SPON + KL composition with orthogonality analysis), but this is positioned as Claim 2 rather than the headline. The quadratic scaling prediction, while interesting, is insufficiently supported theoretically.\n\nFor a venue with ~25% acceptance rate, the novelty bar requires either (a) a genuinely new technique, or (b) a surprising empirical finding with deep analysis. The paper provides (b) in terms of effect size but not in terms of analytical depth. The missing MSE-logits baseline, the questionable BCE fairness, and the thin theoretical treatment prevent it from clearing the bar.\n\n---\n\n## Overall Score: 3/6 (Weak Reject)\n\n**Confidence: 4/5** — I am confident in the novelty and positioning assessment. The one area of uncertainty is whether the BCE baseline weakness reflects a real phenomenon or an implementation issue, which could shift the score in either direction.\n\n**Justification:** The paper identifies a real and practically important phenomenon — KL-trained sparsity predictors dramatically outperform BCE-trained ones. The effect size is large, the ablation design is thoughtful, and the evaluation is comprehensive. However, the core contribution is a loss function swap in an existing pipeline, the gradient coupling theory is trivial (applies to any output-level loss), the most critical baseline (MSE-logits) is missing, the BCE comparison raises fairness concerns, and the related work is severely underdeveloped. The modular decomposition is the strongest original element but is undersold. As written, the paper provides useful empirical knowledge but insufficient novelty or analytical depth for a top venue.\n\n**What would change the score:**\n- MSE-logits baseline showing KL uniquely dominates: +1 (to 4/6)\n- BCE fairness concerns resolved (STE+BCE tested, target quality confound addressed): +0.5\n- Adequate related work (20+ well-discussed references): +0.5\n- Modular decomposition promoted to co-headline with deeper orthogonality theory: +0.5\n- If MSE-logits matches KL: -0.5 (requires complete reframing)\n- If BCE implementation found unfair: -1 (to 2/6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a68e696-0587-48fc-a166-598373762290",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4msZnEvGkbVUaMqcSYr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edc3793c-760c-41df-a872-efa2c5510b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoV9JDNSeusYqZZVQtp9V9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 93318,
      "output_tokens": 4129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4129,
          "cache_read_input_tokens": 93318,
          "cache_creation_input_tokens": 734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 734,
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

_source line 47 · 2026-05-15T17:49:38.661Z_

<details><summary>↩ Tool result · `toolu_015vkhwUBEZgeGEyYsm4LrCo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md\", \"dream_id\": \"dream_20260515T164925\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edc3793c-760c-41df-a872-efa2c5510b35",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "a2318d24f3259d05c",
  "type": "user",
  "uuid": "9936a4b5-a1d2-4ca9-bd71-ed7a0eb3f8ce",
  "sourceToolAssistantUUID": "edc3793c-760c-41df-a872-efa2c5510b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-15T17:49:50.172Z_

Review submitted. Here is a summary of the key findings:

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Core assessment:** The paper demonstrates a large, real effect (KL-only 9.20 vs. BCE+comp 18.64 PPL) with thorough ablation design, but falls short of the novelty bar for a ~25% acceptance rate venue.

**Critical issues identified:**

1. **Thin novelty** -- The contribution is a loss function swap (BCE to KL) in an existing predictor pipeline. SPON already showed KL works for sparsity; extending to contextual prediction is the obvious next step.

2. **Gradient coupling theory is trivial** -- The chain rule argument applies identically to MSE on logits, JS divergence, or any output-level loss. The paper never explains why KL is uniquely better than other coupled losses.

3. **Missing MSE-on-logits baseline** -- The single most damaging omission. If MSE-logits matches KL, the entire "KL is special" narrative collapses to "any output-level loss beats BCE."

4. **BCE baseline fairness concerns** -- BCE-only (28.16 PPL) is 2.3x worse than training-free TEAL (12.48), which is anomalous for a trained predictor. The actual MVP data reveals puzzling evaluation artifacts (BCE "dense PPL" reported as 28.16 rather than the true 6.12). Multiple confounds (Gumbel relaxation mismatch, suboptimal oracle targets, asymmetric training sophistication via Lagrangian) are unaddressed.

5. **Severely underdeveloped related work** -- Only 8 references. Missing Deja Vu (foundational), CATS, Minitron, DIP, Gumbel-softmax foundations, L0 regularization, MoE routing connections, and many more.

**Strongest element to preserve:** The SPON+KL modular decomposition with orthogonality analysis (6.8% interaction residual) is the most original contribution and should be promoted to co-headline.

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9936a4b5-a1d2-4ca9-bd71-ed7a0eb3f8ce",
  "isSidechain": true,
  "agentId": "a2318d24f3259d05c",
  "requestId": "req_011Cb4n1jsvziXUxJZyBnLKR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c81419cd-5435-4266-bcc3-703881401fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W94SsUvYseQTqMpgMqQxSA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4261,
      "cache_read_input_tokens": 94052,
      "output_tokens": 562,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4261
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 562,
          "cache_read_input_tokens": 94052,
          "cache_creation_input_tokens": 4261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4261,
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
