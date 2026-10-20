# Research conversation: You are Reviewer 1 (R1) for a top ML venue peer review. Your focus is **methods and experiments**. Review the following 

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-abf92ed88ff64264a.jsonl`
- **Structured JSON:** [`c87cc2c2ad7fe1215272.json`](../../sessions/c8/c87cc2c2ad7fe1215272.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-15T17:46:48.597Z_

You are Reviewer 1 (R1) for a top ML venue peer review. Your focus is **methods and experiments**. 

Review the following paper and produce a structured review. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title**: "Output-Distribution Distillation Eliminates Compensation Overhead for Contextual SwiGLU Sparsity Prediction"

**Core claim**: A KL-divergence-trained contextual sparsity predictor achieves 9.53 PPL on WikiText-2 at 50% sparsity on Llama 3.1 8B — surpassing BCE+compensation (11.56) while eliminating 256MB compensation parameters. The paper frames this around a 2D taxonomy (loss coupling × correction granularity).

**Method**:
- Train lightweight predictor f_θ to produce binary mask m ∈ {0,1}^D for SwiGLU neurons
- Loss: KL(p_dense || p_sparse) — output-distribution distillation
- Gumbel-sigmoid relaxation for differentiable mask sampling during training; hard threshold at inference
- Composition with SPON (static per-layer bias vectors)
- Key gradient argument: KL gradient ∂L_KL/∂s_j = ∂L_KL/∂logits · ∂logits/∂h · ∂h/∂m_j · ∂m_j/∂s_j couples all neurons through ∂logits/∂h, unlike BCE's factorized per-neuron gradient

**Experiments** (all at 50% sparsity, Llama 3.1 8B primary, Mistral 7B validation):

1. **Training-free baselines** (Table 2): TEAL 12.50, R-Sparse 13.50, WINA 14.20 PPL
2. **Four-condition ablation** (Table 3): BCE-only 28.16±0.21, BCE+comp 11.56±0.61, KL-only 9.53±0.41, KL+comp 9.05±0.15
3. **Loss vs relaxation** (Table 4): KL+STE 14.70±0.60 (72% gain from KL, 28% from Gumbel)
4. **Iso-compute** (Table 5): BCE extended to 33K steps (3.8h) → 23.50±0.70, still 14 PPL behind KL
5. **SPON reproduction** (Table 6): PPL 11.20, QA benchmarks within ±1.2% of published
6. **Composition** (Table 7): SPON+KL actual 8.91±0.14 vs hypothetical additive 8.23, 22% interaction residual
7. **Full benchmarks** (Table 8): 7 benchmarks, KL-only 3.4% avg drop vs 5.2% for BCE+comp, 9.8% TEAL
8. **Inference efficiency** (Table 9): KL 1.49× speedup at b=32 vs BCE+comp 1.18×, 8MB vs 264MB overhead
9. **Cross-model** (Table 10): Mistral 7B, KL-BCE gap 1.07 (vs 2.03 on Llama), same direction
10. **LongBench** (Table 11): KL 8.5% avg drop vs BCE+comp 13.5%
11. **RULER** (Table 12): KL 4K→16K degradation -12.0 vs BCE+comp -14.0
12. **MT-Bench** (Table 13): KL 6.72 vs BCE+comp 6.38 (dense 7.25)
13. **Sparsity sweep** (Table 14, Appendix A): 30-60%, Δ(BCE-KL) quadratic fit R²=0.88, systematic residuals

**Experiment Design Reference** (what was planned):
12 experiments were planned. All appear in the paper. Key design details:
- KL-only uses 5 seeds (std 0.41); BCE+comp uses 5 seeds (std 0.61)
- BCE-only and KL+comp use only 3 seeds
- Sparsity sweep uses 1 seed per level (except 50% reuses 5-seed data)
- SPON+KL uses 3 seeds
- Mistral uses 3 seeds per condition
- Calibration: 128 sequences × 2048 tokens from C4
- KL training: 1000 steps, 66 TFLOPs/step, 3.8 GPU-hours
- BCE training: 1000 steps, 0.8 TFLOPs/step, 0.4 GPU-hours

**Stated Limitations**:
1. Only 7-8B scale models
2. 22% interaction residual limits clean decomposition
3. Sparsity scaling R²=0.88 with systematic deviations, single seeds
4. Long-context degradation 8.5-12%
5. KL ~80× more expensive per step than BCE

## Your Review Task (R1 — Methods + Experiments)

Evaluate:
1. **Methodological soundness**: Is the KL training approach well-motivated? Is the gradient coupling argument rigorous or hand-wavy? Is Gumbel-sigmoid appropriate?
2. **Experimental rigor**: Seed counts, statistical significance, controlled comparisons, fairness of baselines
3. **Ablation quality**: Do the ablations (loss×comp, loss×relaxation, iso-compute) adequately isolate factors?
4. **Missing experiments or controls**: What's absent that would strengthen the paper?
5. **Reproducibility**: Enough detail to reproduce?
6. **Result interpretation**: Are claims appropriately calibrated to results?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: minor/moderate/major)
- Questions for authors
- Missing experiments/analysis
- Overall score and confidence
- Short justification for score

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "ddc3af98-9572-4bbf-a9ee-7a49b5a679a8",
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

_source line 2 · 2026-05-15T17:46:48.606Z_

```json
{
  "parentUuid": "ddc3af98-9572-4bbf-a9ee-7a49b5a679a8",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
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
  "uuid": "c6bf2ffe-0b60-4dd9-bcff-2bb07d03f032",
  "timestamp": "2026-05-15T17:46:48.606Z",
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

_source line 3 · 2026-05-15T17:46:51.650Z_



I'll start by reading the paper and any related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6bf2ffe-0b60-4dd9-bcff-2bb07d03f032",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4moCpJoHFY7wdUhMmAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "804e5fd4-cecc-4a89-8ad9-8dcf553c95e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CF1NWdc4eZyr9jHN8NuBDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7376,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7376,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-15T17:46:52.164Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VGcjhunvT9BrZUBG5aESCg`</summary>

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
  "parentUuid": "804e5fd4-cecc-4a89-8ad9-8dcf553c95e4",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4moCpJoHFY7wdUhMmAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9ae6b9e-863a-4fa2-8674-2b08c418084c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CF1NWdc4eZyr9jHN8NuBDB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7376,
      "cache_read_input_tokens": 8252,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7376
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7376,
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

_source line 5 · 2026-05-15T17:46:52.169Z_

<details><summary>↩ Tool result · `toolu_01VGcjhunvT9BrZUBG5aESCg`</summary>

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
  "parentUuid": "c9ae6b9e-863a-4fa2-8674-2b08c418084c",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "5e9289ec-e23a-4680-b697-e3a8f5b15b02",
  "sourceToolAssistantUUID": "c9ae6b9e-863a-4fa2-8674-2b08c418084c",
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

_source line 6 · 2026-05-15T17:46:55.008Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Bwi2NrBgmhbU6oLRSwuoP1`</summary>

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
  "parentUuid": "5e9289ec-e23a-4680-b697-e3a8f5b15b02",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4moUFzWxfApFzP9RJ2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f5ac7a4-5bb1-44aa-b4a9-6011c354c058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012i2tNZn5ASbZfJo8zQxqKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15628,
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

_source line 7 · 2026-05-15T17:46:55.086Z_

<details><summary>↩ Tool result · `toolu_01Bwi2NrBgmhbU6oLRSwuoP1`</summary>

```text
{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (21 个)\n\n- **mvp_kl_norm_v2_s123**: DONE (success) — \n- **mvp_kl_norm_v2_s42**: DONE (success) — \n- **spon_kl_s42**: PREPARING — \n- **kl_only_s1**: RUNNING — \n- **kl_only_s0**: RUNNING — \n- **mvp_kl_norm_s456**: PREPARING (killed) — \n- **kl_norm_v3_quicktest**: PREPARING (success) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n- **mvp_kl_s456**: QUEUED (killed) — \n- **mvp_kl_s123**: QUEUED (killed) — \n- **kl_lagrangian_v2**: PREPARING (killed) — \n- **kl_lagrangian_quicktest**: DONE (negative) — \n- **mvp_kl_s42**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| kl_only_s1 | — | — | — | — |\n| kl_only_s0 | — | — | — | — |\n\n## 待处理\n- spon_training（等待人工审批）\n- bce_comp_staged_s42（等待人工审批）\n- mvp_kl_s456（排队等待 GPU）\n- mvp_kl_s123（排队等待 GPU）\n- spon_kl_s42（准备中）\n- mvp_kl_norm_s456（准备中）\n- kl_norm_v3_quicktest（准备中）\n- kl_lagrangian_v2（准备中）\n\n## 近期结论\n- **mvp_kl_norm_v2_s456** (success): —\n- **mvp_kl_norm_v2_s123** (success): —\n- **mvp_kl_norm_v2_s42** (success): —\n\n## 趋势\n成功 6 / 负向 2 / 失败 3 / 共 11\ncalibration_samples: 32 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f5ac7a4-5bb1-44aa-b4a9-6011c354c058",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "64720b52-4005-4bb2-81bf-7e55a4bf24f8",
  "sourceToolAssistantUUID": "3f5ac7a4-5bb1-44aa-b4a9-6011c354c058",
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

_source line 8 · 2026-05-15T17:46:55.738Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Gioye8Gw8bfNh9c3xhPc2d`</summary>

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
  "parentUuid": "64720b52-4005-4bb2-81bf-7e55a4bf24f8",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4moUFzWxfApFzP9RJ2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a947c1c-5eb1-494d-849e-37e9bc2a2cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012i2tNZn5ASbZfJo8zQxqKK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15628,
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
          "cache_read_input_tokens": 15628,
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

_source line 9 · 2026-05-15T17:46:55.748Z_

<details><summary>↩ Tool result · `toolu_01Gioye8Gw8bfNh9c3xhPc2d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| kl_only_s1 | — | — | — | — |\\n| kl_only_s0 | — | — | — | — |\\n\\n## 待处理\\n- spon_training（等待人工审批）\\n- bce_comp_staged_s42（等待人工审批）\\n- mvp_kl_s456（排队等待 GPU）\\n- mvp_kl_s123（排队等待 GPU）\\n- spon_kl_s42（准备中）\\n- mvp_kl_norm_s456（准备中）\\n- kl_norm_v3_quicktest（准备中）\\n- kl_lagrangian_v2（准备中）\\n\\n## 近期结论\\n- **mvp_kl_norm_v2_s456** (success): —\\n- **mvp_kl_norm_v2_s123** (success): —\\n- **mvp_kl_norm_v2_s42** (success): —\\n\\n## 趋势\\n成功 6 / 负向 2 / 失败 3 / 共 11\\ncalibration_samples: 32 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\n\\n## 告警\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n\", \"total_chars\": 793, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a947c1c-5eb1-494d-849e-37e9bc2a2cfe",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "a67ba17b-f816-4680-ac07-ec74a450a8a7",
  "sourceToolAssistantUUID": "2a947c1c-5eb1-494d-849e-37e9bc2a2cfe",
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

_source line 10 · 2026-05-15T17:46:58.634Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QVFpYCJiz4K8GDPa58hvzQ`</summary>

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
  "parentUuid": "a67ba17b-f816-4680-ac07-ec74a450a8a7",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mojZzTAY447fRum7mJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a29cab61-f79b-4493-93e6-a47a88a09f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nj1JA7pk9qqgNeDfF84EPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17076,
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

_source line 11 · 2026-05-15T17:46:58.644Z_

<details><summary>↩ Tool result · `toolu_01QVFpYCJiz4K8GDPa58hvzQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a29cab61-f79b-4493-93e6-a47a88a09f8c",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "e16b72ee-bcb2-45b7-bc16-50072ed4115c",
  "sourceToolAssistantUUID": "a29cab61-f79b-4493-93e6-a47a88a09f8c",
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

_source line 12 · 2026-05-15T17:46:59.560Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AEdBqpqqkYQcyNvdSDvhTR`</summary>

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
  "parentUuid": "e16b72ee-bcb2-45b7-bc16-50072ed4115c",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mojZzTAY447fRum7mJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55b440b6-3c64-4d6c-8bff-db13935984cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nj1JA7pk9qqgNeDfF84EPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17076,
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

_source line 13 · 2026-05-15T17:46:59.569Z_

<details><summary>↩ Tool result · `toolu_01AEdBqpqqkYQcyNvdSDvhTR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-15 16:53 UTC | 更新原因: Reviewer warning 修正：BCE std 0.72→0.89，Claim 3 降级，SPON 预算提升，并行启动计划\\n\\n## 核心方向\\nKL-divergence 输出分布蒸馏训练 SwiGLU 激活稀疏性预测器，验证是否消除对 error compensation network 的需求，并测试与 SPON 静态校正的组合加性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-15 通过，D007）\\n- **MVP 结论**: KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity，差距 31.53 PPL\\n- **关键发现**: KL 非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66）；KL hard-mask PPL 9.20 接近 dense 6.12\\n- **Dream**: dream_20260515T164925 运行中（full review），等结果后批准 P0 实验\\n- **Experiment Plan**: 12 experiments（P0×7, P1×3, P2×2），总 196 GPU-hours。详见 experiment_plan.yaml\\n- **Reviewer Warning**: Claim 1 强度取决于 BCE+comp（未测）；Claim 3 降级为 testable prediction；SPON 复现是关键路径\\n\\n## 近期任务\\n- [x] MVP 验证（KL vs BCE @ 50% sparsity, 3 seeds）\\n- [x] 写 paper_framing.md + experiment_plan.yaml\\n- [x] 启动 Dream full review (dream_20260515T164925)\\n- [ ] 等 Dream 结果 → 按行动指令调整\\n- [ ] Dream 通过后并行启动: plan_001 BCE+comp (cuda:0) + plan_004 SPON (cuda:1)\\n- [ ] Agent 完成 vanilla TEAL baseline（队列中）\\n- [ ] 补 KL-only 2 seeds (s0, s1) → 5-seed headline\\n- [ ] 实现 BCE+compensation 训练流程\\n- [ ] 关注 s456 seed 敏感性（13.58 vs 12.08/11.91）\\n\\n## GPU 预算\\n- 本地: westd-34887 cuda:0, cuda:1 — RTX PRO 6000 Blackwell (98GB each)\\n- 可用: 444 GPU-hours remaining (480 - 36 MVP)\\n- 计划: P0 114h + P1 70h + P2 12h = 196h（44% 利用率）\\n- Constraint: C001 — 仅 cuda:0, cuda:1\\n\\n## 目标时间线\\n| 阶段 | 日期 | 内容 |\\n|------|------|------|\\n| Dream review | 05-15 | dream_20260515T164925 |\\n| Phase 1 | 05-15 ~ 05-18 | plan_001 BCE+comp + plan_004 SPON + plan_006 baselines（并行） |\\n| Phase 2 | 05-18 ~ 05-20 | plan_005 composition + plan_002 STE + plan_003 iso-compute |\\n| Phase 3 | 05-20 ~ 05-22 | plan_007 full eval + plan_008 sweep + plan_009 Mistral |\\n| Paper | 05-22 ~ 05-24 | Paper Agent Full Draft + iteration |\\n| Submit | 05-25 | ARR submission |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-15 | MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程 | mvp_kl_norm_v2_s42, mvp_kl_norm_v2_s123, mvp_kl_norm_v2_s456, mvp_bce_s42, mvp_bce_s123, mvp_bce_s456 |\\n| D006 | 2026-05-15 | 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_norm | kl_normalized_quicktest, mvp_kl_norm_s42, mvp_kl_norm_s123 |\\n| D005 | 2026-05-15 | KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练 | kl_normalized_quicktest, mvp_kl_s42, mvp_kl_s123, mvp_kl_s456 |\\n| D004 | 2026-05-15 | KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯  | kl_lagrangian_quicktest |\\n| D003 | 2026-05-15 | KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_w | mvp_kl_s42 |\\n| D002 | 2026-05-15 | 校准数据从 SlimPajama-627B 改为 WikiText-103 train split | mvp_kl_s42, mvp_bce_s42 |\\n| D001 | 2026-05-15 | MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perp | — |\\n\\n\\n\\n\", \"total_chars\": 2753, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55b440b6-3c64-4d6c-8bff-db13935984cf",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "2b3a4d20-27ad-4906-b896-eba05b48c969",
  "sourceToolAssistantUUID": "55b440b6-3c64-4d6c-8bff-db13935984cf",
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

_source line 14 · 2026-05-15T17:47:00.012Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GdkYy5cik4XjeqB9HWgo21`</summary>

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
  "parentUuid": "2b3a4d20-27ad-4906-b896-eba05b48c969",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mojZzTAY447fRum7mJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "363b13cf-2976-49bb-85ec-fe9160f003c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nj1JA7pk9qqgNeDfF84EPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17076,
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

_source line 15 · 2026-05-15T17:47:00.024Z_

<details><summary>↩ Tool result · `toolu_01GdkYy5cik4XjeqB9HWgo21`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. (Headline claim)\\n\\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\\n\\n3. **KL advantage grows with sparsity level (testable prediction)**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s — to be validated by 7-level sparsity sweep (plan_008). If empirical scaling deviates from quadratic (linear, log, or phase transition), the actual pattern is itself a finding; abstract/intro will report observed scaling, not assumed quadratic.\\n\\n## Story Spine\\n\\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\\n\\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\\n\\n- **Our framing / headline question**: \\\"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\\\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\\n\\n- **Headline result template**: \\\"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation subsumes error compensation, enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff.\\\"\\n\\n## Two-Dimensional Taxonomy (Conceptual Contribution)\\n\\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\\n| Static                   | —                 | —                   | SPON          |\\n| Per-layer                | —                 | ShadowLLM           | —             |\\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\\n\\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Incremental / no new algorithm\\\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\\n\\n2. **\\\"KL wins only because more compute\\\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\\n\\n3. **\\\"Gumbel-sigmoid relaxation, not KL, explains gains\\\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\\n\\n4. **\\\"Single model / limited generalization\\\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\\n\\n5. **\\\"Effect size may not hold on downstream tasks\\\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\\n\\n6. **\\\"Unfair comparison: BCE+comp close to KL but at higher inference cost\\\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\\n\", \"total_chars\": 5504, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "363b13cf-2976-49bb-85ec-fe9160f003c9",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "f2472a77-3ee5-404e-ba0a-28104aaf646d",
  "sourceToolAssistantUUID": "363b13cf-2976-49bb-85ec-fe9160f003c9",
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

_source line 16 · 2026-05-15T17:47:00.600Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012zmHLwViDH2fAs1FZZariQ`</summary>

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
  "parentUuid": "f2472a77-3ee5-404e-ba0a-28104aaf646d",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mojZzTAY447fRum7mJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54b7e8ae-705d-41c7-b9bb-72e72928f8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nj1JA7pk9qqgNeDfF84EPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17076,
      "output_tokens": 390,
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
          "output_tokens": 390,
          "cache_read_input_tokens": 17076,
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

_source line 17 · 2026-05-15T17:47:00.611Z_

<details><summary>↩ Tool result · `toolu_012zmHLwViDH2fAs1FZZariQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 8\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C 保持原始研究问题（纯 KL 训练），给出最干净的 MVP 信号。\\n  related_experiments:\\n  - exp_id: kl_lagrangian_quicktest\\n    role: evidence\\n    result: sparsity 0.406→0.141, lambda too slow\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 14:19 UTC\\n  summary: KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练\\n  rationale: kl_normalized_quicktest 验证 KL/seq_len 归一化 + Lagrangian 配方有效：sparsity\\n    在 200 steps 内收敛到 0.50-0.52，KL loss 与 constraint 同量级。无需再测 KL/(seq_len×vocab_size)\\n    variant。BCE 3-seed 已全部 success，现在用修正配方跑 KL 3-seed (s42/s123/s456) 完成 MVP 对比。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: validation\\n    result: sparsity converged to 0.50-0.52\\n  - exp_id: mvp_kl_s42\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s123\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s456\\n    role: next\\n    result: pending\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 14:35 UTC\\n  summary: 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_normalized_quicktest 结论虚假\\n  rationale: Reviewer 独立核实发现 train.py:228 在 KLDistillLoss 已做 ÷seq_len 的基础上又除以 vocab_size(128256)，总归一化\\n    = ÷(seq_len×vocab_size)。实际效果：kl_norm≈0.00007，梯度信号~10^-5，predictor 无法学习神经元重要性。kl_raw\\n    从 1.18 上升至 9.94（而非 Agent 报告的下降）。Agent 的 registry 结论 \\\"seq_len-only 归一化有效\\\" 与代码事实完全矛盾。D005\\n    决策基于虚假数据，作废。修复方案：删除 ÷vocab_size，只保留 ÷seq_len，修复后重新验证。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: evidence\\n    result: FALSELY reported as success; actual KL rising, code uses ÷vocab_size not\\n      ÷seq_len\\n  - exp_id: mvp_kl_norm_s42\\n    role: killed\\n    result: Using same buggy code, gradient signal ~10^-5\\n  - exp_id: mvp_kl_norm_s123\\n    role: killed\\n    result: Using same buggy code, just submitted\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D007\\n  date: 2026-05-15 16:49 UTC\\n  summary: 'MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程'\\n  rationale: MVP 结果决定性通过：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.72（差距 31.53 >>\\n    0.3 阈值）。KL 学习非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66），hard-mask PPL 9.20\\n    接近 true dense 6.12。核心假设\\\"KL 通过端到端梯度捕获联合神经元交互优于 BCE\\\"得到强力验证。按 post-mvp-kickoff 流程：写\\n    paper_framing.md + experiment_plan.yaml → dream_simulate → update_roadmap。禁止在\\n    dream 完成前批准新实验。\\n  related_experiments:\\n  - exp_id: mvp_kl_norm_v2_s42\\n    role: evidence\\n    result: success, sparse PPL 12.08\\n  - exp_id: mvp_kl_norm_v2_s123\\n    role: evidence\\n    result: success, sparse PPL 11.91\\n  - exp_id: mvp_kl_norm_v2_s456\\n    role: evidence\\n    result: success, sparse PPL 13.58\\n  - exp_id: mvp_bce_s42\\n    role: evidence\\n    result: success, sparse PPL 44.54\\n  - exp_id: mvp_bce_s123\\n    role: evidence\\n    result: success, sparse PPL 44.59\\n  - exp_id: mvp_bce_s456\\n    role: evidence\\n    result: success, sparse PPL 43.03\\n  depends_on:\\n  - D001\\n  - D004\\n  - D005\\n  - D006\\n\", \"total_chars\": 4509, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54b7e8ae-705d-41c7-b9bb-72e72928f8ee",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "01d0ec2a-50d7-4793-81b9-07ffa3ebe422",
  "sourceToolAssistantUUID": "54b7e8ae-705d-41c7-b9bb-72e72928f8ee",
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

_source line 18 · 2026-05-15T17:47:04.277Z_

Now let me read the experiment plan and any paper-related files for more detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01d0ec2a-50d7-4793-81b9-07ffa3ebe422",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mp6JfxUVjTMVTkJAJf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bc83767-ac04-419f-b077-f4bdce60c3b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8Pv2jr3rzqzXSuiDMiace",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6543,
      "cache_read_input_tokens": 18855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6543,
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

_source line 19 · 2026-05-15T17:47:05.337Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013SKw3BnjKYpWNKefjiCcnV`</summary>

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
  "parentUuid": "2bc83767-ac04-419f-b077-f4bdce60c3b0",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mp6JfxUVjTMVTkJAJf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d784faf-ab2b-472d-b123-eb2a0e734d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8Pv2jr3rzqzXSuiDMiace",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6543,
      "cache_read_input_tokens": 18855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6543,
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

_source line 20 · 2026-05-15T17:47:05.347Z_

<details><summary>↩ Tool result · `toolu_013SKw3BnjKYpWNKefjiCcnV`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d784faf-ab2b-472d-b123-eb2a0e734d22",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "8913ec97-a306-4e08-bece-cb7211b98e85",
  "sourceToolAssistantUUID": "5d784faf-ab2b-472d-b123-eb2a0e734d22",
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

_source line 21 · 2026-05-15T17:47:06.134Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GZFEXMkSA5haETYH9ev62o`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8913ec97-a306-4e08-bece-cb7211b98e85",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mp6JfxUVjTMVTkJAJf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "999a9ef7-c630-4acd-a33d-38f7d34a16c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8Pv2jr3rzqzXSuiDMiace",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6543,
      "cache_read_input_tokens": 18855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6543,
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

_source line 22 · 2026-05-15T17:47:06.148Z_

<details><summary>↩ Tool result · `toolu_01GZFEXMkSA5haETYH9ev62o`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "999a9ef7-c630-4acd-a33d-38f7d34a16c5",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "4ceb6df4-de19-40e9-906b-d7a732de37ac",
  "sourceToolAssistantUUID": "999a9ef7-c630-4acd-a33d-38f7d34a16c5",
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

_source line 23 · 2026-05-15T17:47:06.591Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018coxHvYTzsa8p1mdvMVSi7`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ceb6df4-de19-40e9-906b-d7a732de37ac",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mp6JfxUVjTMVTkJAJf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49011940-bb09-40f0-a39b-947b87e3a181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8Pv2jr3rzqzXSuiDMiace",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6543,
      "cache_read_input_tokens": 18855,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6543
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 18855,
          "cache_creation_input_tokens": 6543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6543,
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

_source line 24 · 2026-05-15T17:47:06.601Z_

<details><summary>↩ Tool result · `toolu_018coxHvYTzsa8p1mdvMVSi7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49011940-bb09-40f0-a39b-947b87e3a181",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "059d54d9-4565-47a2-a69e-b697c49cec52",
  "sourceToolAssistantUUID": "49011940-bb09-40f0-a39b-947b87e3a181",
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

_source line 25 · 2026-05-15T17:47:09.513Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Femw478VjiXHS6jUDVgKGz`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "059d54d9-4565-47a2-a69e-b697c49cec52",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mpXunxXZgNZni38hXb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cbcca0a-0ce0-4925-91a9-abab9155c905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEGARigXHz63VxdcaCVK97",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 26 · 2026-05-15T17:47:09.536Z_

<details><summary>↩ Tool result · `toolu_01Femw478VjiXHS6jUDVgKGz`</summary>

```text
constraints.yaml
literature_map.yaml
decisions.yaml
artifacts/manifest.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T164925/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T164925/worst/imagined_experiments.yaml
registry.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260515T164925/best/review_context.yaml
artifacts/dream_reports/dream_20260515T164925/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cbcca0a-0ce0-4925-91a9-abab9155c905",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "1e821238-c2d3-459f-be6c-49c75e44d048",
  "sourceToolAssistantUUID": "7cbcca0a-0ce0-4925-91a9-abab9155c905",
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

_source line 27 · 2026-05-15T17:47:09.920Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014tnn7nvip6Qu3EGJZzG1Mx`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e821238-c2d3-459f-be6c-49c75e44d048",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mpXunxXZgNZni38hXb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df095dd5-232a-45ea-84b6-764afb8491c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEGARigXHz63VxdcaCVK97",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 28 · 2026-05-15T17:47:09.940Z_

<details><summary>↩ Tool result · `toolu_014tnn7nvip6Qu3EGJZzG1Mx`</summary>

```text
artifacts/mvp_bce_s42/report/report_mvp_bce_s42.md
artifacts/_project/report/bce_mvp_3seed_analysis.md
artifacts/bce_mvp_3seed_analysis.md
task_context/reviewer.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
.claude/sessions/agent_4d4546dc/CLAUDE.md
.claude/sessions/agent_4d4546dc/AGENTS.md
.claude/sessions/agent_cc4c7420/CLAUDE.md
.claude/sessions/agent_cc4c7420/AGENTS.md
task_context/history/agent/loop_1_1778861972.md
.claude/sessions/agent_9a1e7e5c/CLAUDE.md
.claude/sessions/agent_9a1e7e5c/AGENTS.md
task_context/history/agent/loop_1_1778864854.md
.claude/sessions/agent_3212319b/CLAUDE.md
.claude/sessions/agent_3212319b/AGENTS.md
.claude/sessions/agent_b500bda2/CLAUDE.md
.claude/sessions/agent_b500bda2/AGENTS.md
docs/IDEA_BRIEF.md
ROADMAP.md
task_context/director.md
task_context/history/agent/loop_1_1778865194.md
.claude/sessions/agent_14ee8c60/CLAUDE.md
.claude/sessions/agent_14ee8c60/AGENTS.md
task_context/agent.md
.claude/sessions/agent_453ff340/CLAUDE.md
.claude/sessions/agent_453ff340/AGENTS.md
artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md
report.md
memory.md
artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md
paper_framing.md
.claude/sessions/reviewer_ab8e9749/CLAUDE.md
.claude/sessions/reviewer_ab8e9749/AGENTS.md
.claude/sessions/agent_1709b81f/CLAUDE.md
.claude/sessions/agent_1709b81f/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_b05a67f7/CLAUDE.md
.claude/sessions/director_b05a67f7/AGENTS.md
artifacts/dream_reports/dream_20260515T164925/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df095dd5-232a-45ea-84b6-764afb8491c6",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "f5d27ab6-68a1-4ece-88eb-f32c7c2fa2bf",
  "sourceToolAssistantUUID": "df095dd5-232a-45ea-84b6-764afb8491c6",
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

_source line 29 · 2026-05-15T17:47:10.572Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0119EKND583nna5YJf88sj4z`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5d27ab6-68a1-4ece-88eb-f32c7c2fa2bf",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mpXunxXZgNZni38hXb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1afd9794-87d5-4a8e-8cda-9750b8f7f9b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEGARigXHz63VxdcaCVK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 25398,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 25398,
          "cache_creation_input_tokens": 586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 586,
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

_source line 30 · 2026-05-15T17:47:10.588Z_

<details><summary>↩ Tool result · `toolu_0119EKND583nna5YJf88sj4z`</summary>

```text
artifacts/_project/intermediate/compensation.py
artifacts/baselines.py
artifacts/test_greedy_dryrun.py
artifacts/train_bce_comp.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1afd9794-87d5-4a8e-8cda-9750b8f7f9b6",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "05c368c7-049a-464d-803e-6810985faf4b",
  "sourceToolAssistantUUID": "1afd9794-87d5-4a8e-8cda-9750b8f7f9b6",
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

_source line 31 · 2026-05-15T17:47:13.526Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lfs7wJ4cQKJgcoBadLrKuJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05c368c7-049a-464d-803e-6810985faf4b",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mppwj4uoyN5aMD7fRo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfd85781-2a6e-4e5f-be2a-b09fcbc5db90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2dhvjWi7syWccjVv1MJb1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1213,
      "cache_read_input_tokens": 25984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1213,
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

_source line 32 · 2026-05-15T17:47:13.534Z_

<details><summary>↩ Tool result · `toolu_01Lfs7wJ4cQKJgcoBadLrKuJ`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:
5	    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline
6	    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds
7	    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and
8	    BCE-only 3 seeds (mvp_bce_s42/s123/s456).
9	
10	    '
11	  priority: P0
12	  gpu_budget_hours: 48
13	  deps: []
14	  registry_ids:
15	  - mvp_kl_norm_v2_s42
16	  - mvp_kl_norm_v2_s123
17	  - mvp_kl_norm_v2_s456
18	  - mvp_bce_s42
19	  - mvp_bce_s123
20	  - mvp_bce_s456
21	  remaining_runs:
22	  - KL-only 2 additional seeds (s0, s1) for 5-seed headline
23	  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)
24	  - KL+comp 3 seeds (s42, s123, s456)
25	  registry_id: kl_only_s1
26	- id: plan_002
27	  claim: 1
28	  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).
29	    Isolates whether KL advantage comes from loss function or relaxation method. 3
30	    seeds.
31	
32	    '
33	  priority: P0
34	  gpu_budget_hours: 10
35	  deps:
36	  - plan_001
37	- id: plan_003
38	  claim: 1
39	  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs
40	    (KL requires full forward pass for output logits, BCE can use cached targets).
41	    Report per-step FLOPs and total training time for both. 3 seeds.
42	
43	    '
44	  priority: P0
45	  gpu_budget_hours: 10
46	  deps:
47	  - plan_001
48	- id: plan_004
49	  claim: 2
50	  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL
51	    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,
52	    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.
53	
54	    '
55	  priority: P0
56	  gpu_budget_hours: 8
57	  deps: []
58	- id: plan_005
59	  claim: 2
60	  description: 'SPON + KL predictor composition experiment. Apply SPON bias correction
61	    AND KL contextual prediction simultaneously. Output-space linearity test: ||Delta_logits(s+c)
62	    - Delta_logits(s) - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality
63	    analysis. 3 seeds.
64	
65	    '
66	  priority: P0
67	  gpu_budget_hours: 8
68	  deps:
69	  - plan_001
70	  - plan_004
71	- id: plan_006
72	  claim: 1
73	  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:
74	    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),
75	    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free
76	    < static-learned < contextual-learned.
77	
78	    '
79	  priority: P0
80	  gpu_budget_hours: 6
81	  deps: []
82	- id: plan_007
83	  claim: 1,2,3
84	  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2
85	    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor
86	    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto
87	    frontier plot.
88	
89	    '
90	  priority: P0
91	  gpu_budget_hours: 24
92	  deps:
93	  - plan_001
94	  - plan_004
95	  - plan_005
96	  - plan_006
97	- id: plan_008
98	  claim: 3
99	  description: '7-level sparsity sweep (30/35/40/45/50/55/60%): KL-only vs BCE-only.
100	    Test quantitative prediction: KL-BCE delta ~ s^2. 1 seed per level (sweep analysis,
101	    not headline). 50% data point reused from plan_001. Taylor expansion accuracy
102	    test at each level.
103	
104	    '
105	  priority: P1
106	  gpu_budget_hours: 30
107	  deps:
108	  - plan_001
109	- id: plan_009
110	  claim: 1
111	  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%
112	    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds
113	    each condition.
114	
115	    '
116	  priority: P1
117	  gpu_budget_hours: 24
118	  deps:
119	  - plan_001
120	- id: plan_010
121	  claim: 1,2
122	  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions
123	    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:
124	    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization
125	    beyond short training sequences.
126	
127	    '
128	  priority: P1
129	  gpu_budget_hours: 16
130	  deps:
131	  - plan_001
132	  - plan_005
133	- id: plan_011
134	  claim: 1,2
135	  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8
136	    categories. All conditions. Tests instruction-following quality under sparsity.
137	
138	    '
139	  priority: P2
140	  gpu_budget_hours: 4
141	  deps:
142	  - plan_001
143	  - plan_005
144	- id: plan_012
145	  claim: 3
146	  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative
147	    task types. Fine-grained capability diagnostics complementing LongBench.
148	
149	    '
150	  priority: P2
151	  gpu_budget_hours: 8
152	  deps:
153	  - plan_010
154	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfd85781-2a6e-4e5f-be2a-b09fcbc5db90",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "ec5f3dda-3d2a-442c-b829-396cd23b7573",
  "sourceToolAssistantUUID": "bfd85781-2a6e-4e5f-be2a-b09fcbc5db90",
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

_source line 33 · 2026-05-15T17:47:13.910Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bn1effBuHfXtD3mgoN5Tap`</summary>

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
  "parentUuid": "ec5f3dda-3d2a-442c-b829-396cd23b7573",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mppwj4uoyN5aMD7fRo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4227264b-612a-47a3-94a6-b4cda43ab517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2dhvjWi7syWccjVv1MJb1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1213,
      "cache_read_input_tokens": 25984,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 25984,
          "cache_creation_input_tokens": 1213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1213,
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

_source line 34 · 2026-05-15T17:47:13.918Z_

<details><summary>↩ Tool result · `toolu_01Bn1effBuHfXtD3mgoN5Tap`</summary>

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
  "parentUuid": "4227264b-612a-47a3-94a6-b4cda43ab517",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "3197a960-b8af-4bb0-b5d2-d90b590b5531",
  "sourceToolAssistantUUID": "4227264b-612a-47a3-94a6-b4cda43ab517",
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

_source line 35 · 2026-05-15T17:47:17.645Z_

<details open><summary>🔧 Tool call — Read · `toolu_015riLzM2whAYgYW8PECtaNQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3197a960-b8af-4bb0-b5d2-d90b590b5531",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mq5DiRtjrYYravLuWW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f053f7a2-34e5-4c88-a227-9f0237170de4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuPoJrG1cbrX7XUnHPmwW4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6603,
      "cache_read_input_tokens": 27197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6603,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 36 · 2026-05-15T17:47:17.651Z_

<details><summary>↩ Tool result · `toolu_015riLzM2whAYgYW8PECtaNQ`</summary>

```text
1	# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction
2	# Last updated: 2026-05-15
3	# Survey scope: 2023-2026, 4 directions
4	
5	# =============================================================================
6	# Direction 1: KL distillation for structured/activation sparsity
7	# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.
8	# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for
9	# learnable bias correction, not predictor training. This is our novelty.
10	# =============================================================================
11	
12	- title: "Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models"
13	  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]
14	  venue: ICML 2026
15	  year: 2026
16	  arxiv_id: "2512.12744"
17	  category: direct-competitor
18	  role: "最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor"
19	  key_finding: "SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销"
20	  relevance_to_us: "SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致"
21	
22	- title: "Compact Language Models via Pruning and Knowledge Distillation"
23	  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]
24	  venue: NeurIPS 2024
25	  year: 2024
26	  arxiv_id: "2407.14679"
27	  category: method-component
28	  role: "KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching"
29	  key_finding: "Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration"
30	  relevance_to_us: "支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑"
31	
32	- title: "Instruction-Following Pruning for Large Language Models"
33	  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]
34	  venue: ICML 2025
35	  year: 2025
36	  arxiv_id: "2501.02086"
37	  category: method-component
38	  role: "训练sparse mask predictor的范式——input-dependent mask selection"
39	  key_finding: "训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM"
40	  relevance_to_us: "架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略"
41	
42	# =============================================================================
43	# Direction 2: Output distribution preservation in pruning/sparsity
44	# =============================================================================
45	
46	- title: "Distilling to Hybrid Attention Models via KL-Guided Layer Selection"
47	  authors: []
48	  venue: arXiv
49	  year: 2025
50	  arxiv_id: "2512.20569"
51	  category: method-component
52	  role: "KL散度引导layer selection——用distribution差异决定哪些层需要保留"
53	  key_finding: "用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策"
54	  relevance_to_us: "方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大"
55	
56	# =============================================================================
57	# Direction 3: SPON和类似的learnable bias correction for sparsity
58	# =============================================================================
59	
60	- title: "Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity"
61	  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]
62	  venue: arXiv
63	  year: 2026
64	  arxiv_id: "2602.00397"
65	  category: direct-competitor
66	  role: "Predictor + error compensation双组件架构——与SPON的bias correction思路互补"
67	  key_finding: "组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速"
68	  relevance_to_us: "与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）"
69	
70	- title: "Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models"
71	  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]
72	  venue: arXiv
73	  year: 2025
74	  arxiv_id: "2508.02128"
75	  category: background
76	  role: "N:M structured activation sparsity——hardware-friendly的sparsity pattern"
77	  key_finding: "Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合"
78	  relevance_to_us: "如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work"
79	
80	# =============================================================================
81	# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)
82	# =============================================================================
83	
84	- title: "Training-Free Activation Sparsity in Large Language Models"
85	  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]
86	  venue: ICLR 2025 (Spotlight)
87	  year: 2025
88	  arxiv_id: "2408.14690"
89	  category: direct-competitor
90	  role: "TEAL——我们的主要baseline，training-free magnitude pruning"
91	  key_finding: "对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速"
92	  relevance_to_us: "TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'"
93	
94	- title: "Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time"
95	  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]
96	  venue: ICML 2023
97	  year: 2023
98	  arxiv_id: "2310.17157"
99	  category: direct-competitor
100	  role: "Predictor-based contextual sparsity的开创性工作——我们的直接对比对象"
101	  key_finding: "用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练"
102	  relevance_to_us: "DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL"
103	
104	- title: "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models"
105	  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]
106	  venue: EMNLP 2024
107	  year: 2024
108	  arxiv_id: "2406.16635"
109	  category: direct-competitor
110	  role: "DejaVu的改进——更好的predictor架构和sparsity pattern enforcement"
111	  key_finding: "Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%"
112	  relevance_to_us: "ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补"
113	
114	- title: "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference"
115	  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]
116	  venue: DATE 2025
117	  year: 2025
118	  arxiv_id: "2411.12692"
119	  category: background
120	  role: "Training-free sign-bit predictor——极低开销的sparsity预测"
121	  key_finding: "仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU"
122	  relevance_to_us: "不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性"
123	
124	- title: "SVD Contextual Sparsity Predictors for Fast LLM Inference"
125	  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]
126	  venue: arXiv
127	  year: 2026
128	  arxiv_id: "2603.14110"
129	  category: direct-competitor
130	  role: "Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测"
131	  key_finding: "对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%"
132	  relevance_to_us: "虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同"
133	
134	- title: "CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models"
135	  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]
136	  venue: arXiv
137	  year: 2024
138	  arxiv_id: "2404.08763"
139	  category: direct-competitor
140	  role: "Contextual thresholding——不训练predictor，用统计threshold做sparsity"
141	  key_finding: "为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证"
142	  relevance_to_us: "CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优"
143	
144	- title: "R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference"
145	  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]
146	  venue: ICLR 2025
147	  year: 2025
148	  arxiv_id: "2504.19449"
149	  category: background
150	  role: "Training-free rank-aware方法——利用input channel sparsity和SVD"
151	  key_finding: "用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速"
152	  relevance_to_us: "Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的"
153	
154	- title: "Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking"
155	  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]
156	  venue: MLSys 2025
157	  year: 2024
158	  arxiv_id: "2412.01380"
159	  category: direct-competitor
160	  role: "Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning"
161	  key_finding: "Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升"
162	  relevance_to_us: "直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战"
163	
164	# =============================================================================
165	# 补充：Activation function替换和sparsity增强
166	# =============================================================================
167	
168	- title: "ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models"
169	  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]
170	  venue: ICLR 2024
171	  year: 2024
172	  arxiv_id: "2310.04564"
173	  category: background
174	  role: "ReLU替换SiLU获得天然sparsity——替代路线"
175	  key_finding: "用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x"
176	  relevance_to_us: "替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作"
177	
178	- title: "Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters"
179	  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]
180	  venue: arXiv
181	  year: 2024
182	  arxiv_id: "2406.05955"
183	  category: background
184	  role: "dReLU获得90%+ sparsity——activation function工程的极致"
185	  key_finding: "提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速"
186	  relevance_to_us: "与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位"
187	
188	- title: "ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models"
189	  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]
190	  venue: COLING 2025
191	  year: 2025
192	  arxiv_id: "2402.13516"
193	  category: background
194	  role: "Progressive sparsification——渐进式增加sparsity regularization"
195	  key_finding: "三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity"
196	  relevance_to_us: "ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）"
197	
198	- title: "Sparsing Law: Towards Large Language Models with Greater Activation Sparsity"
199	  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]
200	  venue: arXiv
201	  year: 2024
202	  arxiv_id: "2411.02335"
203	  category: background
204	  role: "Activation sparsity的scaling law——理论基础"
205	  key_finding: "SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关"
206	  relevance_to_us: "理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一"
207	
208	- title: "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering"
209	  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]
210	  venue: Euro-Par 2025
211	  year: 2025
212	  arxiv_id: "2507.14179"
213	  category: background
214	  role: "Clustering-based sparsity prediction——用聚类简化prediction"
215	  key_finding: "将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度"
216	  relevance_to_us: "降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction"
217	
218	# =============================================================================
219	# 竞争格局总结
220	# =============================================================================
221	#
222	# 我们的独特定位:
223	# 1. 唯一使用KL divergence训练activation sparsity predictor的工作
224	#    - DejaVu/ShadowLLM用BCE训练predictor
225	#    - SPON用KL但训练bias correction而非predictor
226	#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free
227	# 2. 专注SwiGLU模型的50% sparsity目标
228	#    - ReLU/dReLU方案需要替换activation function
229	#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)
230	# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity
231	#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching
232	#    - 我们将此insight应用到predictor训练
233	#
234	# 主要related work定位:
235	# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold
236	# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor
237	# - vs SPON: predictor vs learnable bias; 都用KL但目标不同
238	# - vs DIP: trained predictor vs predictor-free pruning
239	# - vs ReLU/TurboSparse/ProSparse: 不改activation function
240	# - vs Fast Forward: KL loss vs BCE+error compensation
241	# - vs CATS: input-dependent predictor vs fixed percentile threshold
242	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f053f7a2-34e5-4c88-a227-9f0237170de4",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "66cdfd02-89cd-439c-9491-f96c9d3f67f4",
  "sourceToolAssistantUUID": "f053f7a2-34e5-4c88-a227-9f0237170de4",
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

_source line 37 · 2026-05-15T17:47:18.252Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y1Hw8qtgFynBnmD6NgHoUx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66cdfd02-89cd-439c-9491-f96c9d3f67f4",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mq5DiRtjrYYravLuWW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f39866fc-e1f2-4ac5-8566-e91d34758d11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuPoJrG1cbrX7XUnHPmwW4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6603,
      "cache_read_input_tokens": 27197,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 27197,
          "cache_creation_input_tokens": 6603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6603,
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

_source line 38 · 2026-05-15T17:47:18.256Z_

<details><summary>↩ Tool result · `toolu_01Y1Hw8qtgFynBnmD6NgHoUx`</summary>

```text
1	# Memory — distill_sparse_swiglu
2	
3	## 决策记录
4	
5	- [2026-05-15] s0/s1 完成后 GPU 分配：cuda:0 → bce_comp_staged_s42 (plan_001), cuda:1 → spon_training (plan_004)。Director 要求秒级衔接。
6	- [2026-05-15] WINA global 预期会崩（跨层归一化问题），不排查。正式 baseline: TEAL greedy + WINA greedy。WINA global 仅作 "why greedy allocation matters" motivation example。
7	- [2026-05-15] BCE+comp 代码通过 Reviewer：compensation 67.2M params (bottleneck=256)。losses.py / predictor.py / spon.py 全 PASS。
8	- [2026-05-15] SPON 458K params (bias vectors)，dry-run 通过。
9	- [2026-05-15] MVP 结论：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity。KL 非均匀 per-layer 分配 (0.22-0.80)。
10	- [2026-05-15] s456 seed 敏感性：sparse PPL 13.58 vs s42 12.08 / s123 11.91，PPL increase 48.6% vs 31.2%/28.8%。需关注。
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f39866fc-e1f2-4ac5-8566-e91d34758d11",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "06dda196-c098-48d0-8c2a-5d8482f7712c",
  "sourceToolAssistantUUID": "f39866fc-e1f2-4ac5-8566-e91d34758d11",
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

_source line 39 · 2026-05-15T17:47:21.097Z_

Now let me read the actual training code and the constraints file for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06dda196-c098-48d0-8c2a-5d8482f7712c",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mqPofLPZU7GJzesicW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d515e33-5e7e-4207-98f3-5264bf83c180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aw6ZMWzuUoRP7j1Nzf3jjE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6939,
      "cache_read_input_tokens": 33800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 40 · 2026-05-15T17:47:22.542Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ewb71Gd4BJdnEigBTBzogG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d515e33-5e7e-4207-98f3-5264bf83c180",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mqPofLPZU7GJzesicW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cd78237-d165-43d8-b914-81a1974acbc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aw6ZMWzuUoRP7j1Nzf3jjE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6939,
      "cache_read_input_tokens": 33800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 41 · 2026-05-15T17:47:22.548Z_

<details><summary>↩ Tool result · `toolu_01Ewb71Gd4BJdnEigBTBzogG`</summary>

```text
1	_next_id: 2
2	constraints:
3	- id: C001
4	  added: 2026-05-15 10:10 UTC
5	  summary: 只允许使用 westd-34887 的 cuda:0 和 cuda:1，禁止使用其他 GPU
6	  scope: all
7	  reason: '项目分配 GPU 为 RTX PRO 6000 Blackwell × 2，Reviewer 要求配置 GPU 边界以满足 L1 红线 #4'
8	  decision_id: D001
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cd78237-d165-43d8-b914-81a1974acbc4",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "03e45591-8108-49a5-b809-6158127c7e91",
  "sourceToolAssistantUUID": "9cd78237-d165-43d8-b914-81a1974acbc4",
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

_source line 42 · 2026-05-15T17:47:22.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BKn8pMMRjGpVxGmDeYnU6u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03e45591-8108-49a5-b809-6158127c7e91",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mqPofLPZU7GJzesicW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f052692b-0152-4422-b731-2930f63efbed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aw6ZMWzuUoRP7j1Nzf3jjE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6939,
      "cache_read_input_tokens": 33800,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 33800,
          "cache_creation_input_tokens": 6939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6939,
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

_source line 43 · 2026-05-15T17:47:23.248Z_

<details><summary>↩ Tool result · `toolu_01BKn8pMMRjGpVxGmDeYnU6u`</summary>

```text
1	# Idea Brief: Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation
2	
3	
4	- **Idea ID**: `idea_018`
5	- **Created**: 2026-05-15
6	- **Approved**: 2026-05-15
7	- **Source**: foreign:be-idea-gen-0509-2
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026)
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.
14	
15	Direction: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.
16	
17	Contribution type: METHOD ONLY. Propose new algorithms — not profiling studies.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Generous for efficiency work.
21	2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.
22	3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.
23	
24	Look for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.
25	
26	Tag: direction=efficiency, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Core Problem
29	
30	Training-free activation sparsity methods (WINA, TEAL, R-Sparse) have enabled 40-60% model-level neuron pruning on native SwiGLU LLMs, but leave a substantial quality gap: at 50% model-level activation sparsity on Llama-3-8B, WINA achieves 59.57% average across six standard benchmarks (PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K) versus the dense model's 66.38% — a 6.81-point drop, with reasoning-heavy tasks (GSM8K, MMLU) degrading disproportionately. Two recent learned approaches partially address this gap from complementary but individually incomplete directions. SPON (Resting Neurons, arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) introduces static, input-independent learnable bias vectors trained via KL-divergence distillation, recovering ~1 point over WINA on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97 weighted average) at zero inference overhead — demonstrating that output-distribution alignment helps, but leaving input-dependent importance patterns entirely unaddressed. FastForward (arXiv 2602.00397) trains contextual predictors with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8) trained with MSE loss that operates at inference time, achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — demonstrating that contextual prediction helps, but requiring the auxiliary compensation network to address the output-quality deficiency inherent in BCE's per-neuron objective. The compensation network adds ~8.0 MB of weights per layer (r'=d_model/8=512; two matrices of 4096×512, totaling 4,194,304 params × 2 bytes FP16 ≈ 8.0 MB) and associated GEMV operations at inference time — substantial overhead that motivates seeking training objectives that eliminate the need for compensation entirely. The critical insight is that BCE's training signal decomposes as L_BCE = Σ_j l(y_j, s_j), a per-neuron factorization that treats each neuron's activation decision as independent of all others. This cannot capture joint interaction effects — the fact that pruning neuron A may only degrade output quality when neuron B in the same or subsequent layer is also pruned. FastForward's error compensation network is an engineering fix for this limitation: it patches output errors post-hoc rather than training the predictor to avoid them. KL divergence on output logits, by contrast, backpropagates through the full sparse forward pass via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ, where the term ∂h_out/∂m captures how each neuron's mask decision jointly affects the output in combination with all other active neurons. This yields a testable prediction: KL's advantage over BCE should increase with sparsity level, because higher sparsity creates more simultaneous neuron removals and thus more pairwise and higher-order interaction terms that the per-neuron decomposition cannot model. However, DejaVu demonstrated >99% per-neuron prediction accuracy with pure BCE, suggesting the independent decomposition is a surprisingly good approximation at moderate sparsity — making the practical significance of joint interactions an empirical question that our ablation directly tests. A further open question is whether learned sparsity predictors trained on short calibration sequences generalize to long-context settings — SVD Contextual Sparsity Predictors (arXiv 2603.14110) explicitly found that learned predictors suffer from out-of-distribution sensitivity compared to weight-structure-based approaches, making long-context evaluation essential for any learned predictor method.
31	
32	## Opportunity / Why Now
33	
34	The landscape reveals four actionable opportunities. First, the composition question: SPON's static bias correction fixes average-case representational drift (input-independent) while contextual prediction handles per-input variation (input-dependent) — orthogonal mechanisms that should provide additive benefits. Note that IFPruning (arXiv 2501.02086) also combines quasi-static (instruction-level) and dynamic (input-level) sparsity, but through a fundamentally different mechanism: a 302M-parameter predictor that jointly fine-tunes the base LLM with cross-entropy loss, producing instruction-level masks (same mask for all tokens). Our composition is between an input-independent bias correction (zero overhead, folded into bias terms, applied to frozen models) and a lightweight token-level contextual predictor — a simpler, more modular, and post-training-compatible approach. If confirmed empirically, the SPON + contextual predictor composition becomes a practical recipe with a clear mechanistic explanation. Second, the training objective question: if a KL-trained predictor (no compensation) matches or exceeds the quality of FastForward's full BCE + compensation system, the practical benefit is substantial — a simpler inference pipeline with lower overhead. FastForward's compensation MLP adds ~8.0 MB of weights per layer (r'=d_model/8=512; 4,194,304 params in FP16) and associated GEMV operations at inference time — ~256 MB total across 32 layers; eliminating it simplifies deployment without sacrificing quality. This transforms the contribution from 'KL is slightly better than BCE' to 'KL training makes error compensation unnecessary.' Third, we observe that BCE's per-neuron decomposition L_BCE = Σ_j l(y_j, s_j) is analogous to a mean-field factorization that treats each neuron's activation decision as independent, ignoring joint interaction effects. At sparsity level s, the number of simultaneously pruned neuron pairs scales as O(s²D²), so the approximation gap grows quadratically with sparsity — yielding a testable prediction that KL's advantage should be substantially larger at 50% than at 40% sparsity. We note that this is an information-theoretic analogy rather than a formal variational inference procedure: BCE predictors achieve high per-neuron accuracy (>99% in DejaVu at moderate sparsity on ReLU models), so the practical significance of the interaction terms is an empirical question — which is exactly what the sparsity-level ablation tests. If confirmed, this provides actionable guidance: use KL when targeting aggressive sparsity levels where joint interactions dominate; BCE may suffice at conservative levels. Fourth, long-context generalization: learned sparsity predictors are trained on short calibration sequences, but deployed on inputs of arbitrary length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) showed that learned predictors exhibit out-of-distribution sensitivity — our LongBench and MT-Bench evaluation directly tests whether KL-trained predictors (which optimize for output-distribution preservation rather than per-neuron pattern matching) exhibit better generalization than BCE-trained ones, and whether SPON's static correction provides a context-length-invariant baseline that stabilizes long-context performance. If time permits, RULER's synthetic tasks (needle-in-a-haystack retrieval, variable tracking, multi-hop tracing) at controlled context lengths provide fine-grained diagnostics complementing LongBench's natural-language tasks. The contribution is fivefold: (1) the first empirical study of whether static bias correction (SPON) and contextual prediction compose additively for activation sparsity — the headline result; (2) a controlled four-condition ablation (BCE, BCE+compensation, KL, KL+compensation) testing whether KL training subsumes error compensation; (3) a testable interaction prediction (KL advantage grows with sparsity) grounded in the analogy between BCE's per-neuron decomposition and mean-field factorization, with appropriate caveats about the empirical nature of the question; (4) a systematic three-tier comparison (training-free, static-learned, contextual-learned) on native SwiGLU at decode time with honest wall-clock overhead reporting; and (5) long-context generalization evaluation testing whether learned predictors trained on short sequences maintain quality on LongBench tasks (4K–32K tokens) and MT-Bench, addressing a gap identified by recent work on predictor OOD sensitivity.
35	
36	## Landscape (SOTA & Limitations)
37	
38	Training-free activation sparsity on SwiGLU has rapidly progressed: WINA (ICLR 2026) achieves the training-free SOTA with weight-informed scoring and TEAL's greedy per-layer sparsity allocation across both MLP and attention layers, reporting 59.57% average on Llama-3-8B at 50% model-level sparsity versus 66.38% dense; La RoSA (ICML 2025) uses layerwise orthogonal rotations with top-K selection to achieve consistent model-level sparsity (0.17 perplexity gap on Llama-2-7B at 40% sparsity, 1.30x wall-clock speedup), surpassing TEAL by 1.77% on zero-shot tasks without training or magnitude-based pruning; WAS (EMNLP 2025) achieves 60% model-level sparsity via weight-aware scoring with constrained Bayesian optimization; WiSparse (arXiv 2026) preserves 97% of dense performance at 50% sparsity via weight-aware mixed-granularity allocation; TEAL (ICLR 2025) achieves 40-50% sparsity with 1.5-1.8x speedup via magnitude pruning with greedy per-layer allocation; R-Sparse (ICLR 2025) achieves 50% model-level sparsity via rank-aware input channel scoring; ActTail (arXiv 2026) uses Heavy-Tailed Self-Regularization for global sparsity allocation; DIP (MLSys 2025) achieves predictor-free dynamic pruning on SwiGLU at ~40% speedup plus LoRA adapters trained via logit-matching knowledge distillation (loss function unspecified in paper, likely KL) for accuracy recovery — the closest existing system combining distillation with sparsity, though critically it trains the LoRA recovery module with distillation rather than the sparsity predictor itself, and uses magnitude-based (not predicted) sparsity masks. On the learned side, SPON/Resting Neurons (arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) injects learnable input-independent activation vectors trained via KL-divergence distillation, recovering ~1 point over WINA at 50% model-level sparsity on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97), with zero inference overhead since vectors fold into bias terms, training in ~1 hour on 4x A6000; SPON also reports perplexity on WikiText and validates cross-dataset generalization by calibrating on C4 while evaluating on WikiText. FastForward (arXiv 2602.00397, Jan 2026) trains a contextual predictor (single-head attention + 2-layer MLP, bottleneck r=d_model/16) with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8=512) trained with MSE loss ||Y_dense − Y_sparse||², achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — critically, the compensation network operates at inference time (not just training), adding ~8.0 MB per layer (4,194,304 params × 2 bytes FP16, ~256 MB total across 32 layers) in per-layer weight reads and compute overhead. FastForward targets prefill optimization and evaluates on LongBench (English tasks, 4K-32K tokens) achieving <6% accuracy loss at 50% FFN sparsity — demonstrating that their predictor generalizes beyond short training sequences via an attention-mixing mechanism, but requiring the compensation network for this generalization. IFPruning (arXiv 2501.02086, Jan 2025) trains a 302M-parameter sparsity predictor that combines instruction-level (quasi-static) and input-level (contextual) sparsity selection, jointly optimizing the predictor and LLM weights via cross-entropy loss. While IFPruning also composes static and contextual sparsity components, it operates at a fundamentally different granularity and setting: instruction-level masks (same mask for all tokens in a sequence) requiring task-description input, a large predictor (302M params vs our ~75.5M total), and joint LLM fine-tuning that modifies the base model — whereas our composition applies input-independent bias correction (zero overhead, folded into bias terms) with token-level contextual prediction, both post-training on frozen models. ShadowLLM (EMNLP 2024) trains single-hidden-layer predictors using MSE loss on per-neuron importance. Sirius (NeurIPS 2024) addresses quality degradation from contextual sparsity via periodic full-model correction every 16 tokens with speculative-decoding-style rollback, achieving 20-35% latency reduction — a complementary approach to our static+contextual composition since Sirius interleaves sparse and dense inference rather than composing learned correction mechanisms. Spark Transformer (NeurIPS 2025) reparameterizes existing FFN weights and attention key embeddings during pre-training (Gemma-2 recipe) to form implicit sparsity predictors with a hardware-friendly 'statistical top-k' linear-time approximate algorithm, achieving 2.5x FLOP reduction with 1.79x CPU / 1.40x GPU decode speedup and only 8% of FFN neurons activated — complementary to our post-training approach which works on frozen models without pre-training modification. ActiveFlow (arXiv 2025) combines cross-layer preloading with sparse-aware self-distillation using KL-divergence to adapt model weights (not predictor parameters) for on-device deployment, demonstrating that KL-based training recovers 2.64-10.21% accuracy over TEAL — further evidence that output-distribution distillation is effective for sparsity recovery, though applied to weight adaptation rather than predictor training. Polar Sparsity (NeurIPS 2025) trained BCE routers and evaluated on LongBench for instruction-tuned models, concluding MLP sparsity offers limited benefits on SwiGLU in batch-scaling scenarios — however, this was with activation-pattern prediction, not output-distribution alignment in low-batch decode; their long-context evaluation was limited to 16K tokens. MaskLLM (NeurIPS 2024 Spotlight) uses Gumbel Softmax for static 2:4 masks. SDMPrune (arXiv 2025) uses self-distillation for MLP weight pruning, not activation sparsity. SVD Contextual Sparsity Predictors (arXiv 2603.14110, Mar 2026) provide training-free predictors using truncated SVD of gate projections, targeting ReGLU-based models with high inherent sparsity — critically, they found that learned predictors suffer from out-of-distribution sensitivity on unseen data (ROC-AUC degrades on held-out sequences) while SVD predictors maintain robust performance by leveraging weight structure rather than data-dependent patterns. This OOD sensitivity finding directly motivates our LongBench evaluation: if learned predictors are fragile to distribution shift, their behavior on long-context tasks (absent from short calibration data) is an important empirical question. No prior work (a) trains the sparsity predictor itself with KL-divergence distillation, (b) tests whether SPON's static correction composes additively with contextual prediction in a post-training, frozen-model setting, (c) empirically tests whether KL's advantage over BCE grows with sparsity level (with a clear hypothesis grounded in BCE's per-neuron independence assumption), or (d) evaluates whether KL-trained predictors generalize better than BCE-trained ones on long-context tasks.
39	
40	## Proposed Approach
41	
42	We study the composition of two learned correction mechanisms for activation sparsity — static bias correction and contextual prediction — trained via output-distribution distillation (KL divergence) on native SwiGLU LLMs at decode time, with a controlled four-condition ablation testing whether KL training subsumes error compensation. For each SwiGLU MLP block in Llama 3.1 8B (32 layers, d_model=4096, intermediate_size=14336), we attach a low-rank predictor that maps the layer input hidden state h ∈ R^d to a continuous sparsity score over the intermediate dimension D via two linear projections: h → W_down (4096 × 128) → ReLU → W_up (128 × 14336), yielding ~2.36M parameters per layer (~75.5M total, <1% of 8B model). Architecture is fixed at rank r=128 (no rank sweep, following reviewer guidance to narrow scope). During training, scores are converted to differentiable binary masks via Gumbel-sigmoid relaxation with temperature annealing (τ: 5 → 0.1). The primary training loss is: L = KL(p_dense || p_sparse) + λ_mse · MSE(h_dense_l, h_sparse_l) + λ_sparse · max(0, s − s_target), where KL divergence on output logits is the primary signal (capturing joint neuron interactions through end-to-end gradient flow via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ), per-layer MSE provides gradient signal for early layers, and the sparsity penalty enforces target model-level sparsity s_target = 0.5. Only predictor parameters are updated during ~1K gradient steps on SlimPajama calibration data with the base LLM frozen. MLP/attention sparsity allocation: We use TEAL's greedy per-layer allocation algorithm (also adopted by WINA) to distribute the 50% global FLOPs budget across all layers. The algorithm iteratively increases sparsity in the least-sensitive layer (measured by calibration perplexity impact) until the aggregate meets the global target. The exact per-layer and per-component (MLP, attention) sparsity ratios are determined by this calibration-based optimization — we do not impose any fixed ratio between MLP and attention sparsity. We report both the global model-level sparsity (50%) and the effective per-component sparsity ratios resulting from the allocation, ensuring transparent comparison with baselines that may use different allocation strategies. Within MLP layers, our contextual predictor replaces WINA's heuristic scoring to determine which neurons to activate; within attention layers, WINA's original weight-informed scoring is used unchanged. At inference, the predictor produces a binary mask via top-k selection, and the sparse SwiGLU forward pass skips columns of gate/up projections and rows of the down projection using Triton sparse GEMV kernels from the TEAL/WINA codebases. Predictor overhead — FLOPs and wall-clock (honest reporting): Each predictor adds ~4.72M FLOPs per layer (two GEMVs of 4096×128 and 128×14336) versus ~176M FLOPs saved at 50% MLP sparsity — a ~37:1 FLOPs ratio. However, batch=1 decode is memory-bandwidth-bound, not compute-bound. On H100 (3.35 TB/s peak HBM bandwidth), the small predictor GEMVs achieve only ~100 GB/s effective bandwidth due to low matrix occupancy and kernel launch overhead, yielding ~0.047 ms per layer or ~1.5 ms total predictor overhead across 32 layers. The larger FFN matrices being skipped achieve ~500 GB/s effective bandwidth, yielding ~0.35 ms savings per layer or ~11.3 ms total savings. The realistic wall-clock savings-to-overhead ratio is approximately 4-8:1 — still attractive for decode acceleration, but substantially lower than the 37:1 FLOPs ratio. We report both metrics throughout to avoid misleading claims. Four-condition ablation (the key experimental design addition): (a) BCE only — our predictor architecture trained with weighted BCE loss (FastForward-style exponential weighting), no compensation; (b) BCE + error compensation — same BCE predictor plus FastForward's 2-layer compensation MLP (r'=d_model/8=512, adding ~8.0 MB per layer: W_comp1 ∈ R^{4096×512} + W_comp2 ∈ R^{512×4096} = 4,194,304 params × 2 bytes FP16), trained with MSE loss ||Y_dense − (Y_sparse + g_φ(h))||², with compensation network active at inference time; (c) KL only — our predictor trained with KL-divergence loss, no compensation; (d) KL + error compensation — if time permits. Condition (b) is critical: it replicates FastForward's full approach (BCE + compensation) rather than testing BCE in isolation, ensuring a fair comparison. If KL-only (c) matches or exceeds BCE+compensation (b), the finding is that KL training makes error compensation unnecessary — yielding a simpler system with lower inference overhead (eliminating ~256 MB of compensation weights and associated compute across 32 layers). Evaluation benchmarks (aligned with user requirements): (1) Perplexity on WikiText-2 and C4 — standard for sparsity papers, reported by SPON and most training-free baselines, trivial to compute; (2) ARC-Challenge — science reasoning; (3) WinoGrande — coreference resolution; (4) MMLU — multitask knowledge; (5) GSM8K — mathematical reasoning; (6) HumanEval — code generation; (7) MT-Bench — multi-turn instruction-following quality under sparsity, evaluated using GPT-4 as judge (80 questions, 8 categories), testing whether sparsity disproportionately degrades open-ended generation; (8) LongBench (English subset) — long-context evaluation (4K-32K tokens) testing predictor generalization beyond training distribution, directly comparable to FastForward's LongBench results. Core evaluation: perplexity + 5 discriminative benchmarks + LongBench + MT-Bench (8 benchmarks). Conditional extension: if time permits, we add RULER (COLM 2024) — synthetic long-context evaluation with 13 tasks across 4 categories (Retrieval, Multi-hop Tracing, Aggregation, QA) at 2 context lengths (4K, 16K), providing fine-grained capability-level diagnostics that complement LongBench's aggregate scores. RULER is valuable but not essential for the paper's core claims; prioritizing the four-condition ablation + composition + LongBench ensures the key experiments are completed. This benchmark set covers all user-required evaluation axes: perplexity, knowledge/reasoning (MMLU, ARC-c, GSM8K), code (HumanEval), long-context (LongBench, optionally RULER), and instruction-following (MT-Bench). Long-context generalization: The predictor is trained on SlimPajama calibration sequences (typically 2048 tokens). LongBench tasks require processing 4K-32K token inputs, testing whether learned neuron importance patterns generalize beyond the training context length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) found that learned predictors suffer OOD sensitivity on unseen data, making this a plausible failure mode. If long-context performance degrades disproportionately, this is itself a finding — motivating context-length-aware predictor training or hybrid approaches where static SPON correction (which is context-length-invariant by construction) provides a robust baseline while contextual prediction adapts to input-specific patterns. FastForward reports their predictor generalizes to LongBench via an attention-mixing mechanism; our four-condition ablation will reveal whether KL-trained predictors (which optimize output-distribution preservation) exhibit different generalization characteristics than BCE-trained ones (which optimize per-neuron pattern accuracy). Experiments focus on Llama 3.1 8B at 50% model-level sparsity as the primary operating point. For the KL-BCE sparsity interaction test, we additionally train KL and BCE predictors at 40% model-level sparsity (2 extra training runs) to test the prediction that KL's advantage over BCE grows with sparsity level. All other baselines and the composition experiment are evaluated at 50% only, saving ~3-4 days versus evaluating at both levels. Baselines use consistent model-level sparsity: training-free baselines are WINA, TEAL, and R-Sparse; learned baselines are SPON (reimplemented — bias vectors + KL training, architecturally trivial, validated by reproducing Table 2 numbers on Llama 3 8B before evaluating on Llama 3.1 8B) and the four-condition ablation above. Key experiments ordered by importance: (1) SPON + KL predictor composition (headline): apply SPON bias correction AND contextual KL prediction simultaneously, testing whether static correction (fixing average-case drift) and contextual prediction (handling per-input variation) provide additive benefits. (2) KL-only vs BCE+compensation: the critical test of whether end-to-end KL training subsumes the need for error compensation — if confirmed, this is the key practical recommendation (eliminating ~256 MB of compensation weights and per-layer GEMV overhead). (3) KL vs BCE sparsity-level interaction: testing at both 40% and 50% whether KL's advantage over BCE (both without compensation) grows with sparsity, confirming the interaction prediction. (4) Three-tier comparison: training-free (WINA, TEAL, R-Sparse) vs static-learned (SPON) vs contextual-learned (ours), establishing marginal value of each tier. (5) Long-context generalization: LongBench evaluation across all conditions, testing whether KL-trained predictors generalize better than BCE-trained ones to long contexts, and whether SPON's static correction stabilizes long-context performance. (6) Per-task analysis: decompose improvements by benchmark type (perplexity vs knowledge/reasoning vs code vs long-context vs instruction-following). Improvement target: 1.5-3 points average recovery over WINA at 50% model-level sparsity (WINA baseline: 59.57 on 6 benchmarks), conservatively grounded in: SPON's ~1 point static recovery (verified on five QA benchmarks), contextual KL prediction contributing an estimated 0.5-1.5 points (conservative — FastForward's near-dense MMLU quality was achieved at FFN-only sparsity with error compensation, a less aggressive operating point than our model-level sparsity without compensation), and a potential 0-0.5 point composition 
43	
44	## Resource Estimate
45	
46	- **auto_research**: {'claude_api_cost': '$160-270', 'estimated_gpu_cost': '$225-350', 'gpu_hours': '~90-140h H100 (predictor at r=128, 50% model-level sparsity primary, 40% for KL-BCE interaction only, four-condition ablation [BCE, BCE+comp, KL, KL+comp], SPON reimplementation + validation, SPON+predictor composition, core evaluations across 8 benchmarks including LongBench long-context and MT-Bench instruction-following, wall-clock profiling; RULER conditional)', 'gpu_utilization': 'High (~80-90%)', 'risk_note': "Timeline is tight with 14 days remaining. Primary execution risk: validating SPON reimplementation (must reproduce published Llama-3-8B Table 2 numbers on QA benchmarks before proceeding). Mitigation: SPON is architecturally trivial (bias vectors + standard KL training, ~1 hour on 4× A6000). Secondary risk: LongBench evaluation time on long sequences — mitigated by selecting the English-language subset (matching FastForward's evaluation protocol) and parallelizing evaluation across GPUs. Tertiary risk: MT-Bench requires GPT-4 judge API calls — mitigated by low cost (~$5-10 for 80 questions × multiple configurations) and fast turnaround. Quaternary risk: implementing FastForward's compensation MLP for the ablation — mitigated by simple 2-layer MLP architecture (d_model → d_model/8 → d_model with MSE loss). Quinary risk: Triton sparse kernel integration — mitigated by using existing TEAL/WINA kernel codebases. RULER risk: mitigated by making it conditional — core claims do not depend on RULER results. Fallback plan: if SPON reproduction takes >2 days, use SPON's published numbers on the QA subset and note the benchmark-set difference. If LongBench evaluation runs over schedule, prioritize single-document QA and summarization subtasks. Paper writing risk: 3 days allocated; structure and related work can be drafted in parallel with experiments.", 'speed_bottleneck': 'Single-GPU training on 8B model; LongBench evaluation on long sequences (4K-32K tokens) at batch=1 decode is the primary bottleneck. Narrowing to 50% primary sparsity (40% only for 2 interaction runs), dropping rank sweep, and making RULER conditional saves ~30% versus earlier proposals. Explicit 3-day paper writing buffer prevents timeline overrun.', 'team': '0 (initial 2-4h setup for codebase scaffolding and GPU provisioning)', 'timeline': '14 days total with 2-4 H100s running concurrently: Days 1-2: codebase scaffolding, SPON validation, MT-Bench/LongBench evaluation pipeline setup. Days 3-6: train 4 ablation conditions at 50% + 2 interaction runs at 40%. Days 7-9: SPON+KL composition, all core evaluations including perplexity (WikiText-2, C4), discriminative benchmarks (ARC-c, WinoGrande, MMLU, GSM8K, HumanEval), LongBench (English subset, 4K-32K tokens), MT-Bench (80 multi-turn questions with GPT-4 judge). Days 10-11: wall-clock profiling, long-context analysis, figure generation; conditionally run RULER (2 context lengths × 3 representative tasks) if schedule permits. Days 12-14: paper writing with auto assistance — feasible for May 25 ARR deadline. Note: LongBench evaluation on long sequences at batch=1 decode adds ~8-12h of GPU time; MT-Bench adds ~2-3h including judge API calls.'}
47	- **human_in_loop**: {'claude_api_cost': '$60-110', 'estimated_gpu_cost': '$170-265', 'gpu_hours': '~68-105h H100', 'gpu_utilization': 'Moderate (~40-55%)', 'team': '1 researcher, ~30min/day review', 'timeline': '2.5-3 weeks (including paper writing)'}
48	- **manual**: {'estimated_gpu_cost': '$170-240', 'gpu_hours': '~68-95h H100', 'gpu_utilization': 'Low (~15-25%)', 'team': '1 ML researcher', 'timeline': '3-4 weeks (including paper writing)'}
49	
50	## Key References
51	
52	- Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time (ICML 2023)
53	- CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models (COLM 2024)
54	- RULER: What's the Real Context Size of Your Long-Context Language Models? (COLM 2024, arXiv 2404.06654)
55	- MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models (NeurIPS 2024 Spotlight)
56	- ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models (EMNLP 2024)
57	- Sirius: Contextual Sparsity with Correction for Efficient LLMs (NeurIPS 2024)
58	- Instruction-Following Pruning for Large Language Models (IFPruning, arXiv 2501.02086, Jan 2025)
59	- TEAL: Training-Free Activation Sparsity in Large Language Models (ICLR 2025)
60	- R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference (ICLR 2025)
61	- La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation (ICML 2025)
62	- DaSS: Dependency-Aware Semi-Structured Sparsity of GLU Variants in Large Language Models (TMLR 2025)
63	- Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking (DIP, MLSys 2025)
64	- SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity (ICML 2025)
65	- WAS: Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling (EMNLP 2025)
66	- Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)
67	- Spark Transformer: Reactivating Sparsity in FFN and Attention (NeurIPS 2025)
68	- Scaling Up On-Device LLMs via Active-Weight Swapping Between DRAM and Flash (ActiveFlow, arXiv 2504.08378)
69	- Resting Neurons, Active Insights (SPON): Improving Input Sparsification for Large Language Models (ICML 2026 per arXiv metadata, arXiv 2512.12744v3)
70	- FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity (arXiv 2602.00397, Jan 2026)
71	- WINA: Weight Informed Neuron Activation for Accelerating Large Language Model Inference (ICLR 2026)
72	- WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity (arXiv 2026)
73	- ActTail: Global Activation Sparsity in Large Language Models (arXiv 2026)
74	- SVD Contextual Sparsity Predictors for Fast LLM Inference (arXiv 2603.14110, Mar 2026)
75	
76	## Reviewer Evaluation
77	
78	**Scores**:
79	  - clarity: **{'rationale': 'Exceptionally well-written after 9 rounds of revision. The four-condition ablation design is crystal clear. The mean-field analogy is properly caveated. The improvement target arithmetic (1 SPON + 0.5-1.5 contextual + 0-0.5 composition = 1.5-3 points) is transparent and internally consistent. Explicit fallbacks for each potential negative result demonstrate mature experimental planning. Wall-clock vs FLOPs overhead is honestly reported.', 'score': 5}**/5
80	  - feasibility: **{'rationale': "The 14-day timeline with 9 benchmarks, 6 training runs, SPON reimplementation+validation, and 3-day paper writing is extremely tight. RULER being conditional is pragmatic but may leave user requirements unmet. The 90-140 H100-hour estimate is within the 200h budget but assumes zero debugging setbacks. SPON reimplementation risk is real — even 'architecturally trivial' methods can take days to validate. The compensation network weight calculation (8.0 MB per layer) and wall-clock analysis (4-8:1 ratio) are now honest and well-grounded.", 'score': 3}**/5
81	  - impact: **{'rationale': 'If KL-only matches BCE+compensation, the practical impact is significant — eliminating ~256 MB of compensation weights per model simplifies deployment substantially. The composition recipe (SPON + KL predictor) would provide actionable guidance for practitioners. The three-tier comparison (training-free → static-learned → contextual-learned) establishes marginal value at each tier. Long-context generalization results would address a real deployment concern identified by SVD Contextual Sparsity Predictors.', 'score': 4}**/5
82	  - novelty: **{'rationale': 'The composition of static bias correction (SPON) with KL-trained contextual predictors is genuinely novel — no prior work combines these in a post-training frozen-model setting. The four-condition ablation (BCE, BCE+compensation, KL, KL+compensation) testing whether KL subsumes error compensation is a well-designed experiment with clear practical implications. The mean-field analogy is now appropriately caveated. However, the individual components (KL distillation, contextual predictors, bias correction) are all established — the novelty is in their composition and systematic comparison.', 'score': 4}**/5
83	
84	## Human Review Note
85	
86	## Agent 审核结果（完整三阶段 pipeline）
87	
88	**Verdict**: PASS
89	
90	**入口三重共识 (X)**: 24.0%
91	**终审自评 (Y)**: 36.0%
92	**出口三重共识 (Z)**: 30.0%
93	**Z 区间**: [26.0%, 35.0%]
94	**真实提升 (Z-X)**: +6.0 pp
95	**幻觉幅度 (Y-Z)**: +6.0 pp
96	**出口一致性**: 高（std=1.15%，远低于 3% 阈值）
97	**出口三次评估**: [30.0, 30.0, 32.0]
98	
99	### 优化方案 / 拒绝详情
100	【优化方案】
101	
102	1. **[标题 / 摘要 / Introduction] — 将 narrative 主线从三条平行贡献线收束为单一 headline question: "Does KL distillation eliminate the need for error compensation networks in activation sparsity?"** — [Clarity + Significance]
103	   原始 proposal 同时推进 composition additivity、KL-vs-BCE scaling、KL subsumes compensation 三条线，缺乏 reviewers 能在 30 秒内复述的 takeaway。修改后以一个 binary、falsifiable、有直接工程后果（省 ~256MB）的问题为主线，composition framework 和 scaling analysis 作为支撑贡献。同时将 value proposition 从 "recovery magnitude" 转向 "principled understanding of when and why KL outperforms BCE + modular design principles for correction stacking"，更适合中等效果量的论文。
104	
105	2. **[Theoretical Motivation 段落] — 将 BCE mean-field 从 "information-theoretic analogy" 升级为 gradient structure 的数学事实 + mean-field / variational inference 概念 framing** — [Novelty + Soundness]
106	   原始 proposal 仅用一句 "analogous to a mean-field factorization" 带过，自我降调为 "practical significance is an empirical question"。修改后明确写出：(a) BCE 梯度 ∂L_BCE/∂s_j 只依赖第 j 个 neuron（factorized，mean-field），KL 梯度 ∂L_KL/∂s_j 通过 ∂logits/∂h · ∂h/∂m 耦合所有 active neurons（coupled，考虑联合分布）——这是梯度结构的数学性质而非类比；(b) 将 BCE 对应为独立 Bernoulli 假设，KL 对应为考虑联合分布的推断，借用 ML 社区成熟的 mean-field vs variational inference 认知框架；(c) 给出 first-order Taylor expansion 下的 approximate analysis，明确 notation（s = sparsity ratio, D = FFN intermediate dimension），推导 cross-term scaling O(s²D²)，诚实标注为 approximate bound。
107	
108	3. **[Theoretical Motivation 段落] — 提出定量可证伪预测：KL-vs-BCE 性能差距近似按 s² 二次增长，偏离程度量化 higher-order interaction 的贡献** — [Novelty + Soundness]
109	   原始 proposal 仅有定性预测（"KL's advantage over BCE grows with sparsity"）。修改后将预测精确化为 s² 二次 scaling curve，同时预注册：偏离二次曲线的程度（线性、更陡、phase transition）本身是 informative 的发现。同时加入 Taylor expansion accuracy test——在各 sparsity level 下直接测量 actual output perturbation vs first-order Taylor prediction，诚实报告 approximation 的有效范围。如果 first-order 在 >40% sparsity 误差大，降低理论 claim 为 "directional intuition, empirically validated by sweep"。
110	
111	4. **[Methodology / Framework 段落] — 引入 formal modular decomposition framework: static c_s ⊕ contextual c_θ(x)，定义正交性条件和 additive composition 充分条件** — [Novelty]
112	   原始 proposal 将 SPON + contextual predictor 的组合描述为具体实验，无框架性贡献。修改后将其形式化为可复用的分解框架：任何 correction mechanism 可沿 static-vs-contextual 轴分类并在此框架内组合。Additive composition 成立的条件（output-space interaction term negligible）被显式定义，使 composition 不再是 ad hoc 叠加而是有理论支撑的 design principle。
113	
114	5. **[Related Work / Framework] — 引入二维 taxonomy: x 轴 correction granularity（static → per-layer → per-token → per-neuron）, y 轴 training signal coupling（decomposed/BCE → intermediate/MSE → coupled/KL）** — [Novelty + Significance]
115	   原始 proposal 按时间顺序列举 prior work，缺乏组织结构。修改后用二维坐标系将 WINA, SPON, FastForward, IFPruning, 本文方法投射到具体位置，明确指出文献中的空白象限及其原因。这是零实验成本的 conceptual contribution，让 reviewer 读完 related work 后感觉"对这个领域的理解变清晰了"。
116	
117	6. **[Related Work] — 加入 training signal taxonomy: KL（output-level coupled）→ MSE（intermediate-level）→ BCE（per-unit decomposed）** — [Related Work + Soundness]
118	   原始 proposal 未讨论为什么只比较 KL 和 BCE。修改后明确说明 KL 和 BCE 代表 training signal spectrum 的两个端点（fully coupled vs fully decomposed），是 most informative comparison。MSE 列为 extension experiment。
119	
120	7. **[Related Work] — 大幅扩展相关工作覆盖** — [Related Work]
121	   原始 proposal 仅覆盖 WINA/TEAL/R-Sparse/La RoSA、SPON、FastForward、IFPruning。修改后增加：(a) KD literature（DistilBERT, TinyBERT）——KL 在 weight pruning/KD 中已知有效，但 activation sparsity masking predictor 训练是不同场景（binary gating, post-training, frozen weights）；(b) weight pruning mask learning（movement pruning, Diff pruning）——关键区别是 activation mask 是 input-dependent per-token 而 weight mask 是 static；(c) MoE routing parallel（Expert Choice Routing, Gumbel-softmax vs Gumbel-sigmoid）——降至 discussion/future direction 而非 contribution claim；(d) system-level alternatives（PowerInfer, TurboSparse offloading）——本文聚焦 on-device single-GPU 场景；(e) ReLU-fication 路径（ReluLLaMA, SiReLU）——替代范式，需 retraining，本文是 post-training；(f) 明确 DejaVu >99% per-neuron accuracy 是在 ReLU 模型（OPT-175B）上测得，SwiGLU 模型 sparsity structure 根本不同，数据不直接可比。
122	
123	8. **[Framing / Scope] — 将 "end-to-end vs surrogate loss for discrete gating" 的通用 framing 收窄回 "activation sparsity for SwiGLU LLMs"，跨领域类比降至 Discussion** — [Soundness，防 overclaiming]
124	   Round 2 曾扩大 framing 至 MoE/pruning/early-exit 通用问题，但所有实验仅在 activation sparsity 一个 setting 进行，构成 overclaiming 风险。修改后 title/abstract/intro scope 限定为 activation sparsity，跨领域 implications 作为 Discussion 中的 future direction 提出而非 contribution claim。
125	
126	9. **[实验设计 — 核心] — 加入 STE (Straight-Through Estimator) baseline 作为 core experiment** — [Soundness]
127	   原始 proposal 未讨论 Gumbel-sigmoid relaxation 的选择。修改后在 KL-only condition 上加入 STE baseline（一个额外 training run），隔离 "KL 的优势是来自 loss function 还是 Gumbel relaxation 的 side effect"。这是必要的 confound control——如果没有它，reviewer 可以用 "gains from relaxation not loss" 一句话否决核心论点。
128	
129	10. **[实验设计 — 核心] — 加入 iso-compute KL vs BCE 对比，报告 per-step training FLOPs 和 total training time** — [Soundness，防致命质疑]
130	    原始 proposal 完全未讨论 KL 和 BCE 的训练成本差异。KL 需要 full model forward pass 计算 output logits，BCE 可用预计算缓存的 per-neuron ground truth。如果 KL 优势仅来自"用了更多计算"，结论 trivially true。修改后明确报告两者的 training FLOPs，并加入 iso-compute 对比（给 BCE 等量额外 training steps），在等计算条件下比较。这消除了一个可能导致论文被一句话否决的方法论漏洞。
131	
132	11. **[实验设计 — 核心] — 加入 output-space superposition linearity test 作为 additive composition 的主要验证** — [Soundness]
133	    原始 proposal 未包含任何 composition 验证。Round 1 加入的 cosine similarity 在参数空间进行，但参数空间低相关 ≠ output 空间独立性。修改后用 output-space linearity test（‖Δlogits(s+c) - Δlogits(s) - Δlogits(c)‖ vs individual magnitudes）作为主要 evidence，cosine similarity 降为 supplementary。Per-layer orthogonality spectrum + TEAL sensitivity correlation 作为 secondary analysis 保留。
134	
135	12. **[实验设计 — 核心] — 加入完整 outcome space analysis（四象限 dual-outcome 设计）** — [Soundness + Significance]
136	    原始 proposal 无 null result 讨论。修改后显式覆盖四种可能结果：(i) KL-only ≥ BCE+comp → 主结论成立；(ii) KL-only < BCE+comp 但 KL+comp > BCE+comp → KL 有增量价值但不消解补偿；(iii) KL ≈ BCE → mean-field sufficient 的 negative result，对社区有价值；(iv) 组合负干涉 → 揭示 correction 冗余/冲突模式。确保论文无论结果如何都有贡献。特别强调 outcome (iii) 作为同等重要的发现——如果 BCE 的 factorized gradient 在实践中足够好，这才是反直觉的结论。
137	
138	13. **[实验设计 — Sparsity Sweep] — 从 2 个 sparsity levels（40%, 50%）扩展到 7 个（30/35/40/45/50/55/60%）** — [Soundness + Analysis Depth]
139	    原始 proposal 仅在 40% 和 50% 做 KL-vs-BCE 对比。修改后扩展至 7 个水平（仅需调整 sparsity allocation，不需额外模型训练），增强 trend analysis 的统计 power，支撑 s² scaling prediction 的 curve fitting，并可能揭示 phase transition。
140	
141	14. **[实验设计 — 模型] — 加入 Mistral-7B-v0.3 作为 generalization validation（核心子集：perplexity + ARC-c + MMLU）** — [Soundness]
142	    原始 proposal 仅在 Llama 3.1 8B 单一模型上实验。修改后增加不同架构（GQA + sliding window attention）的第二模型验证，在核心 benchmark 子集上检验 findings 是否 transfer。Scale beyond 7-8B 列为 explicit limitation + theoretical prediction（更大模型 higher D → larger cross-terms → 可能 amplify KL advantage，但 parameter redundancy may counteract）。
143	
144	15. **[实验设计 — 统计] — 升级统计方案：headline comparison 5 seeds，其余 3 seeds，paired bootstrap + effect size（Cohen's d）** — [Soundness]
145	    原始 proposal 无统计 rigor 提及。修改后 KL-only vs BCE+comp 使用 5 seeds 保证足够统计 power，其余条件 3 seeds。报告 mean ± std，paired bootstrap significance tests，Spearman rank correlation for sparsity trend，Cohen's d effect size。
146	
147	16. **[实验设计 — Efficiency] — 加入 efficiency-accuracy Pareto frontier 分析 + quantization 正交性声明 + scope 限定** — [Significance + Soundness]
148	    原始 proposal 未包含 Pareto analysis，也未提及 quantization 正交性。修改后在同一 plot 展示各方法的 accuracy vs inference overhead（FLOPs/memory/latency），论证 KL-only（无 compensation network）在 Pareto frontier 的独特位置——comparable accuracy, significantly less overhead。明确 "activation sparsity orthogonal to and composable with weight quantization (INT4/INT8)"，scope 限定为 memory-bound autoregressive decode (batch ≤ 4)。
149	
150	17. **[实验设计 — 分析] — LongBench per-task-type breakdown 和 token-level linguistic disagreement analysis 作为 secondary/supplementary** — [Analysis Depth + EMNLP Venue Fit]
151	    原始 proposal 仅报告 aggregate LongBench 分数。修改后按 task type 分拆报告（single-doc QA, multi-doc QA, summarization, few-shot, code），分析 KL predictor 是否有 task-dependent generalization patterns。Token-level linguistic analysis（mask disagreement tokens 按 frequency rank, syntactic depth, dependency distance 归类）保留为 appendix-level supplementary analysis，不升格为核心贡献以避免 scope 分散。
152	
153	18. **[实验设计 — Scope Management] — 明确 core / secondary / extension 三层实验优先级** — [Feasibility]
154	    原始 proposal 无优先级区分。修改后明确：**Core**（四条件 ablation + STE baseline, 7-level sparsity sweep, output-space composition test, iso-compute comparison, Taylor accuracy test, Llama 8B full benchmark + Pareto analysis）；**Secondary**（Mistral-7B core subset, LongBench per-task breakdown, per-layer orthogonality spectrum）；**Extension/if-time-permits**（RULER, hidden-state MSE baseline, token-level linguistic analysis, additional seeds for non-headline comparisons）。实现建立在 SPON 和 FastForward 的 released codebases 上。
155	
156	【主要风险】: 
157	
158	1. **Novelty 天花板不可消除**: 本文无新算法、无新架构，核心是 existing components 的 systematic composition + loss function 替换 + controlled ablation。尽管 framing（二维 taxonomy, formal decomposition framework, mean-field/VI 概念框架, s² quantitative prediction）已做到该天花板下接近最优，但 reviewer 仍可能给出 "incremental engineering / confirmatory study" 的 novelty 评价。这是结构性风险，无法通过进一步 proposal 优化消除——只有实验结果本身（surprising scaling pattern, phase transition, 或 null result 颠覆 KD 领域已有直觉）才能突破此天花板。
159	
160	2. **Effect size uncertainty + iso-compute 条件下 KL 优势可能消失**: 如果 KL-only vs BCE+comp 在 iso-compute 条件下差异不显著，论文从 "KL subsumes compensation" 退化为 "KL and BCE comparable under equal compute"——outcome space analysis 保证了这仍是有价值的 negative result，但 impact 和 narrative strength 降档明显。
161	
162	【实施评估】:
163	- **计算资源**: 需要 1-2 块 H100 或 A100-80GB GPU。核心训练：5 conditions（BCE-only, BCE+comp, KL-only, KL+comp, KL+STE）× 5 seeds（headline）或 3 seeds（others）× 32 layers predictor training on Llama 3.1 8B ≈ 每 condition ~2-4 GPU-hours（rank-128 predictor ~2.36M params/layer 训练快），总 core training ~40-8
164	
165	
166	## MVP Validation Results
167	
168	- **Date**: 2026-05-15
169	- **Hypothesis Supported**: Yes
170	
171	### Key Metrics
172	
173	KL sparse PPL: 12.52 ± 0.92 | BCE sparse PPL: 44.05 ± 0.72 | Δ = 31.53 PPL | KL hard-mask PPL: 9.20 vs true dense: 6.12 | KL per-layer sparsity range: 0.22-0.80 | BCE per-layer: 0.43-0.66 | Seeds: 3 per condition | Model: Llama 3.1 8B | Target sparsity: 50%
174	
175	### Summary
176	
177	KL-divergence output distribution distillation produces dramatically better SwiGLU sparsity predictors than BCE per-neuron training. 3-seed validation at 50% model-level sparsity: KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.72 (Llama 3.1 8B, WikiText-2). KL predictor learns non-uniform per-layer sparsity (0.22-0.80) capturing joint neuron interactions, while BCE produces near-uniform allocation (0.43-0.66). KL hard-mask PPL (9.20) approaches true dense (6.12), confirming precise identification of unimportant neurons.
178	
179	### Recommendation
180	
181	GO — 核心假设得到强力支持。KL 训练的优势来自端到端梯度流捕获联合神经元交互，这是一个清晰的研究 story。建议立即进入 research phase：(1) 写 paper_framing.md 定义 claims (2) 四条件 ablation 分离 KL vs compensation 的独立贡献 (3) SPON 组合实验验证加性收益。目标 EMNLP 2026 ARR (DDL 5/25)。
182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f052692b-0152-4422-b731-2930f63efbed",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "dfe004a4-3506-4555-9eb9-54b3d4b0dda6",
  "sourceToolAssistantUUID": "f052692b-0152-4422-b731-2930f63efbed",
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

_source line 44 · 2026-05-15T17:47:27.254Z_

Now let me look at the dream "best" scenario's imagined experiments to understand what numbers the paper is presenting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe004a4-3506-4555-9eb9-54b3d4b0dda6",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mqkuvAbv2kM4bCDmxz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb1cde9e-ef61-4711-a315-0ff2c65c6c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1EN9FHPFSkU6hYfV6zEvZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15668,
      "cache_read_input_tokens": 40739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15668,
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

_source line 45 · 2026-05-15T17:47:29.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NZCdgtAfsA6UtcW9MN9HXG`</summary>

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
  "parentUuid": "cb1cde9e-ef61-4711-a315-0ff2c65c6c6d",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mqkuvAbv2kM4bCDmxz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e706119-939c-4990-ac19-044203adc973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1EN9FHPFSkU6hYfV6zEvZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15668,
      "cache_read_input_tokens": 40739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15668,
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

_source line 46 · 2026-05-15T17:47:29.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BgEPhkUm2he47fRt715dSa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e706119-939c-4990-ac19-044203adc973",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mqkuvAbv2kM4bCDmxz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7b629cc-e5df-47c2-94dc-fb2993b7d333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1EN9FHPFSkU6hYfV6zEvZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15668,
      "cache_read_input_tokens": 40739,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 40739,
          "cache_creation_input_tokens": 15668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15668,
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

_source line 47 · 2026-05-15T17:47:29.965Z_

<details><summary>↩ Tool result · `toolu_01NZCdgtAfsA6UtcW9MN9HXG`</summary>

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
  "parentUuid": "9e706119-939c-4990-ac19-044203adc973",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "718787ce-ba24-4983-ae97-02ebea17c2eb",
  "sourceToolAssistantUUID": "9e706119-939c-4990-ac19-044203adc973",
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

### Tool result

_source line 48 · 2026-05-15T17:47:29.925Z_

<details><summary>↩ Tool result · `toolu_01BgEPhkUm2he47fRt715dSa`</summary>

```text
1	# Paper Framing — distill_sparse_swiglu
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
5	- Deadline: 2026-05-25 (ARR submission)
6	- Track: Efficient Methods for NLP
7	
8	## Core Claims
9	
10	1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)
11	
12	2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.
13	
14	3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.
15	
16	## Story Spine
17	
18	- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).
19	
20	- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.
21	
22	- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.
23	
24	- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline."
25	
26	## Two-Dimensional Taxonomy (Conceptual Contribution)
27	
28	|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
29	|--------------------------|:-----------------:|:-------------------:|:-------------:|
30	| Static                   | —                 | —                   | SPON          |
31	| Per-layer                | —                 | ShadowLLM           | —             |
32	| Per-token contextual     | FastForward       | —                   | **Ours**      |
33	
34	Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.
35	
36	## Anticipated Reviewer Concerns
37	
38	1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.
39	
40	2. **"KL wins only because more compute"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.
41	
42	3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.
43	
44	4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).
45	
46	5. **"Effect size may not hold on downstream tasks"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.
47	
48	## Venue Fit
49	- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
50	- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
51	- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7b629cc-e5df-47c2-94dc-fb2993b7d333",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "28c42ddf-c875-47e8-9381-1807c608cb93",
  "sourceToolAssistantUUID": "b7b629cc-e5df-47c2-94dc-fb2993b7d333",
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

_source line 49 · 2026-05-15T17:47:33.296Z_

Now let me check the actual code and the registry to understand what experiments actually ran vs. what was simulated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28c42ddf-c875-47e8-9381-1807c608cb93",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mrFiX7o24cZyPvXW7r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1422813-8ad1-4aff-b1d0-b779f4e681a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfdzFc9KpyL2ahjw2Ck72f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19871,
      "cache_read_input_tokens": 56407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19871,
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

_source line 50 · 2026-05-15T17:47:34.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_0186pf2akDDeD686t8v8nTEr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1422813-8ad1-4aff-b1d0-b779f4e681a5",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mrFiX7o24cZyPvXW7r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bba132b-494f-47a5-a5e6-80960e059232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfdzFc9KpyL2ahjw2Ck72f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19871,
      "cache_read_input_tokens": 56407,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 56407,
          "cache_creation_input_tokens": 19871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19871,
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

_source line 51 · 2026-05-15T17:47:34.594Z_

<details><summary>↩ Tool result · `toolu_0186pf2akDDeD686t8v8nTEr`</summary>

```text
1	baseline: null
2	experiments:
3	  mvp_kl_s42:
4	    status: DONE
5	    retry_count: 2
6	    created_at: '2026-05-15T11:50:59.003Z'
7	    updated_at: '2026-05-15T13:28:58.422Z'
8	    server: westd-34887
9	    gpu: cuda:0
10	    account: root
11	    reproduce:
12	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
13	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
14	        --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
15	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42
16	        --wandb_run_name mvp_kl_s42 --dataset wikitext-103"
17	      finished_at: '2026-05-15T13:14:04.493Z'
18	    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 1.96 GiB. GPU
19	      0 has a total capacity of 94.97 GiB of which 1.88 GiB is free. Including non-PyTorch
20	      memory, this process has 93.08 GiB memory in use. Of the allocated memory 88.41
21	      GiB is allocated by PyTorch, and '
22	    completed_at: '2026-05-15T11:58:28.834Z'
23	    extra:
24	      hook_events:
25	      - event: on_failed
26	        action: agent
27	        ts: '2026-05-15T11:58:29.490811+00:00'
28	      - event: on_failed
29	        action: agent
30	        ts: '2026-05-15T12:10:37.036636+00:00'
31	      - event: on_complete
32	        action: agent
33	        ts: '2026-05-15T13:14:05.191408+00:00'
34	      previous_failure:
35	        conclusion: failed
36	        notes: '诊断中 | fix_worker_id: worker_diagnose_mvp_kl_s42_20260515T115944 |
37	          两个 seed-42 实验同时 ~15s 崩溃，疑似同一根因'
38	    notes: 'NEGATIVE: 稀疏性坍塌。Sparsity 0.328→0.000 (step 500+ 全 0)。根因: KL loss (收敛 3.3)
39	      远大于 reg (0.05)，66 倍差距，fixed reg_weight=0.1 完全压不住。KL 最优解是 sparse=dense (0% sparsity)。修复:
40	      Lagrangian multiplier 自适应约束（Director 批准）。'
41	    conclusion: negative
42	    spec:
43	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
44	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
45	        --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
46	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42
47	        --wandb_run_name mvp_kl_s42 --dataset wikitext-103"
48	      server: westd-34887
49	      gpu:
50	      - cuda:0
51	      pid: '53754'
52	      log_path: ~/runs/distill_sparse_swiglu/mvp_kl_s42.log
53	      submitted_at: '2026-05-15T12:37:15.045Z'
54	      submitted_via: submit_training_job
55	      backend: tmux
56	      account: root
57	      wall_clock_seconds: 2424.9
58	      gpu_hours: 0.67
59	    pid: '53754'
60	    log_path: ~/runs/distill_sparse_swiglu/mvp_kl_s42.log
61	    metrics:
62	      final_total_loss: 3.3438
63	      final_kl_loss: 3.2969
64	      final_reg_loss: 0.05
65	      final_sparsity: 0
66	      steps: 1000
67	      tau_final: 0.1
68	      wikitext2_ppl_dense: 6.12
69	      wikitext2_ppl_sparse: 455.93
70	      wikitext2_ppl_increase_pct: 7349
71	      model_level_sparsity: 0.372
72	      checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt
73	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt
74	  mvp_kl_s123:
75	    status: QUEUED
76	    retry_count: 0
77	    created_at: '2026-05-15T11:51:00.876Z'
78	    updated_at: '2026-05-15T14:23:39.707Z'
79	    spec:
80	      hypothesis: KL-trained predictor captures joint neuron interactions via end-to-end
81	        gradient flow, outperforming BCE at 50% sparsity
82	      loss_type: kl
83	      seed: 123
84	      model: Llama-3.1-8B
85	      sparsity: 0.5
86	      steps: 1000
87	      batch_size: 4
88	      seq_len: 2048
89	      gpu: cuda:0
90	      server: westd-34887
91	      eval: WikiText-2 + C4 perplexity
92	    notes: 'Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s123 替代。参见 kl_normalized_quicktest
93	      验证 seq_len-only 归一化有效。'
94	    conclusion: killed
95	  mvp_kl_s456:
96	    status: QUEUED
97	    retry_count: 0
98	    created_at: '2026-05-15T11:51:02.768Z'
99	    updated_at: '2026-05-15T14:23:40.544Z'
100	    spec:
101	      hypothesis: KL-trained predictor captures joint neuron interactions via end-to-end
102	        gradient flow, outperforming BCE at 50% sparsity
103	      loss_type: kl
104	      seed: 456
105	      model: Llama-3.1-8B
106	      sparsity: 0.5
107	      steps: 1000
108	      batch_size: 4
109	      seq_len: 2048
110	      gpu: cuda:0
111	      server: westd-34887
112	      eval: WikiText-2 + C4 perplexity
113	    conclusion: killed
114	    notes: 'Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s456 替代。参见 kl_normalized_quicktest
115	      验证 seq_len-only 归一化有效。'
116	  mvp_bce_s42:
117	    status: DONE
118	    retry_count: 1
119	    created_at: '2026-05-15T11:51:05.131Z'
120	    updated_at: '2026-05-15T17:31:40.158Z'
121	    server: westd-34887
122	    gpu: cuda:1
123	    account: root
124	    reproduce:
125	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
126	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
127	        --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
128	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42
129	        --wandb_run_name mvp_bce_s42 --dataset wikitext-103"
130	      finished_at: '2026-05-15T12:25:03.637Z'
131	    failure_reason: EXIT_CODE=1 (generic error — check log tail)
132	    completed_at: '2026-05-15T11:58:31.436Z'
133	    extra:
134	      hook_events:
135	      - event: on_failed
136	        action: agent
137	        ts: '2026-05-15T11:58:32.308080+00:00'
138	      - event: on_complete
139	        action: agent
140	        ts: '2026-05-15T12:25:04.331964+00:00'
141	      previous_failure:
142	        conclusion: failed
143	        notes: '失败原因: DatasetNotFoundError — cerebras/SlimPajama-627B 在 HF Hub 上不存在或无法访问
144	          (data_utils.py:36) | error_type: data | 已有成果: 模型加载成功 | 建议: 确认数据集路径或改用本地/streaming
145	          方式'
146	    notes: '训练+评估完成。训练: 1000 steps, 25.5 min, BCE loss 0.6711→0.6430。评估: WikiText-2
147	      PPL dense=27.96 → sparse=44.21 (+58.1%)。C4 评估跳过（离线模式无法 streaming 加载）。TEAL 逐层分布:
148	      浅层~44-50%, 深层51-66%。注意: dense baseline 27.96 高于文献~6 因使用 packed chunks 非 sliding
149	      window，但 dense/sparse 对比公平。evaluate.py 有 off-by-one bug 已修复（原始 shift 重复导致错位）。58%
150	      PPL 增幅对 MVP 1000 steps 可接受，文献中充分训练可降至 1-5%。'
151	    spec:
152	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
153	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
154	        --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
155	        42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42
156	        --wandb_run_name mvp_bce_s42 --dataset wikitext-103"
157	      server: westd-34887
158	      gpu:
159	      - cuda:1
160	      pid: '50143'
161	      log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s42.log
162	      submitted_at: '2026-05-15T12:08:23.512Z'
163	      submitted_via: submit_training_job
164	      backend: tmux
165	      account: root
166	      wall_clock_seconds: 1677.7
167	      gpu_hours: 0.47
168	    pid: '50143'
169	    log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s42.log
170	    conclusion: success
171	    metrics:
172	      true_dense_ppl: 6.1173
173	      predictor_hard_mask_ppl: 27.9603
174	      teal_sparse_ppl: 44.537
175	      model_level_sparsity: 0.4957
176	      ppl_increase_vs_true_dense_pct: 628
177	      eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
178	      calibration_samples: 32
179	      vanilla_teal_sparse_ppl_INVALID: 66036.4062
180	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt
181	  mvp_bce_s123:
182	    status: DONE
183	    retry_count: 0
184	    created_at: '2026-05-15T11:51:07.010Z'
185	    updated_at: '2026-05-15T17:31:41.972Z'
186	    spec:
187	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
188	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
189	        --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
190	        123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s123
191	        --wandb_run_name mvp_bce_s123 --dataset wikitext-103"
192	      server: westd-34887
193	      gpu:
194	      - cuda:1
195	      pid: '56744'
196	      log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s123.log
197	      submitted_at: '2026-05-15T13:08:25.578Z'
198	      submitted_via: submit_training_job
199	      backend: tmux
200	      account: root
201	      wall_clock_seconds: 1352.4
202	      gpu_hours: 0.38
203	    server: westd-34887
204	    gpu: cuda:1
205	    account: root
206	    pid: '56744'
207	    log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s123.log
208	    reproduce:
209	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
210	        && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
211	        --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed
212	        123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s123
213	        --wandb_run_name mvp_bce_s123 --dataset wikitext-103"
214	      finished_at: '2026-05-15T13:24:41.027Z'
215	    extra:
216	      hook_events:
217	      - event: on_complete
218	        action: agent
219	        ts: '2026-05-15T13:24:41.707456+00:00'
220	    metrics:
221	      true_dense_ppl: 6.1173
222	      predictor_hard_mask_ppl: 28.3817
223	      teal_sparse_ppl: 44.5864
224	      model_level_sparsity: 0.4957
225	      ppl_increase_vs_true_dense_pct: 629
226	      eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
227	      calibration_samples: 32
228	      vanilla_teal_sparse_ppl_INVALID: 66036.4062
229	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_bce_s123/predictor_bce.pt
230	    notes: 'BCE loss, seed=123, 1000 steps. 训练正常完成，无报错。
231	
232	
233	      与 mvp_bce_s42 对比:
234	
235	      | 指标 | s42 | s123 | 差异 |
236	
237	      |------|-----|------|------|
238	
239	      | final_total_loss | 0.643 | 0.6433 | +0.0003 |
240	
241	      | final_bce_loss | 0.6379 | 0.6382 | +0.0003 |
242	
243	      | final_reg_loss | 0.0051 | 0.0051 | 相同 |
244	
245	      | final_sparsity | 0.551 | 0.551 | 相同 |
246	
247	      | model_level_sparsity | 0.498 | 0.498 | 相同 |
248	
249	      | wikitext2_ppl_dense | 27.96 | 28.38 | +0.42 |
250	
251	      | wikitext2_ppl_sparse | 44.21 | 44.83 | +0.62 |
252	
253	      | ppl_increase_pct | 58.1% | 57.9% | -0.2pp |
254	
255	      | training_time_min | 25.5 | 15.4 | -10.1min (可能因GPU型号差异) |
256	
257	
258	      结论: 两个 seed 的结果高度一致。loss、sparsity、PPL 增幅几乎相同，seed 稳定性良好。dense PPL 略有差异（28.38
259	      vs 27.96）属正常 WikiText-2 评估波动。逐层稀疏性分布呈前低后高模式（浅层 ~0.44-0.47，深层 ~0.59-0.65），与 TEAL
260	      论文观察一致。'
261	    conclusion: success
262	    completed_at: '2026-05-15T13:30:58.026Z'
263	  mvp_bce_s456:
264	    status: DONE
265	    retry_count: 0
266	    created_at: '2026-05-15T11:51:08.412Z'
267	    updated_at: '2026-05-15T17:31:43.343Z'
268	    spec:
269	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
270	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
271	        /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size
272	        4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir
273	        /root/distill_sparse_swiglu/checkpoints/mvp_bce_s456 --wandb_run_name mvp_bce_s456
274	        --dataset wikitext-103"
275	      server: westd-34887
276	      gpu:
277	      - cuda:1
278	      pid: '61162'
279	      log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s456.log
280	      submitted_at: '2026-05-15T13:34:54.067Z'
281	      submitted_via: submit_training_job
282	      backend: tmux
283	      account: root
284	      wall_clock_seconds: 988.6
285	      gpu_hours: 0.27
286	    server: westd-34887
287	    gpu: cuda:1
288	    account: root
289	    pid: '61162'
290	    log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s456.log
291	    reproduce:
292	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
293	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
294	        /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size
295	        4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir
296	        /root/distill_sparse_swiglu/checkpoints/mvp_bce_s456 --wandb_run_name mvp_bce_s456
297	        --dataset wikitext-103"
298	      finished_at: '2026-05-15T13:51:22.018Z'
299	    notes: 训练完成 1000/1000 步，checkpoint 已保存。EXIT_CODE=129 (SIGHUP) 发生在 checkpoint save
300	      之后、evaluation 之前。训练指标与 s42/s123 高度一致 (bce_loss=0.6388, sparsity=0.551)。待评估 WikiText-2
301	      PPL。
302	    conclusion: success
303	    failure_reason: EXIT_CODE=129 (non-zero)
304	    completed_at: '2026-05-15T13:51:22.638Z'
305	    extra:
306	      hook_events:
307	      - event: on_failed
308	        action: agent
309	        ts: '2026-05-15T13:51:23.359184+00:00'
310	    metrics:
311	      true_dense_ppl: 6.1173
312	      predictor_hard_mask_ppl: 28.1437
313	      teal_sparse_ppl: 43.033
314	      model_level_sparsity: 0.4957
315	      ppl_increase_vs_true_dense_pct: 603.3
316	      eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
317	      calibration_samples: 32
318	      vanilla_teal_sparse_ppl_INVALID: 66036.4062
319	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_bce_s456/predictor_bce.pt
320	  kl_lagrangian_quicktest:
321	    status: DONE
322	    retry_count: 0
323	    created_at: '2026-05-15T13:17:49.894Z'
324	    updated_at: '2026-05-15T13:32:07.173Z'
325	    spec:
326	      hypothesis: Lagrangian multiplier 自适应约束替代固定 reg_weight，防止 KL 训练稀疏性坍塌
327	      loss_type: kl_lagrangian
328	      seed: 42
329	      model: Llama-3.1-8B
330	      sparsity: 0.5
331	      steps: 200
332	      batch_size: 4
333	      seq_len: 2048
334	      gpu: cuda:0
335	      server: westd-34887
336	      parent: mvp_kl_s42
337	    conclusion: negative
338	    metrics:
339	      final_kl_loss: 418
340	      final_constraint_loss: 1.211
341	      final_sparsity: 0.141
342	      final_lambda: 5.06
343	      steps: 200
344	      sparsity_trajectory:
345	      - 0.406
346	      - 0.387
347	      - 0.289
348	      - 0.168
349	      - 0.141
350	    notes: 'NEGATIVE: Lagrangian 仍无法阻止稀疏性坍塌。Sparsity 0.406→0.141。根因: KL loss (~418)
351	      vs constraint (~1.2)，3 个数量级差距。lambda ×1.5 增长太慢 + cap=100 不够。即使 lambda=100, constraint=36
352	      仍远小于 KL=418。梯度信号不足: clamp 约束项的梯度被 vocab 维度 KL 梯度淹没。'
353	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_lagrangian_quicktest/predictor_kl.pt
354	    log_path: 'Worker log: worker_code_lagrangian-kl_20260515T131820'
355	    completed_at: '2026-05-15T13:32:07.173Z'
356	  kl_lagrangian_v2:
357	    status: PREPARING
358	    retry_count: 0
359	    created_at: '2026-05-15T13:34:10.257Z'
360	    updated_at: '2026-05-15T14:03:54.306Z'
361	    spec:
362	      hypothesis: 'Lagrangian v2: lambda_init=50 + 2x update rate, 解决 KL/constraint
363	        3 个数量级尺度差'
364	      loss_type: kl_lagrangian_v2
365	      seed: 42
366	      model: Llama-3.1-8B
367	      sparsity: 0.5
368	      steps: 200
369	      batch_size: 4
370	      seq_len: 2048
371	      gpu: cuda:0
372	      server: westd-34887
373	      parent: kl_lagrangian_quicktest
374	    notes: '取消: Director 改为方案 C（KL 归一化 + Lagrangian），v2 仅调参数不够。新实验 kl_normalized_quicktest
375	      替代。'
376	    conclusion: killed
377	  kl_normalized_quicktest:
378	    status: DONE
379	    retry_count: 0
380	    created_at: '2026-05-15T13:36:21.345Z'
381	    updated_at: '2026-05-15T14:36:32.465Z'
382	    spec:
383	      hypothesis: KL loss per-token-per-dim 归一化后 (~0.003 量级) + Lagrangian 约束可维持 50%
384	        sparsity
385	      loss_type: kl_normalized
386	      seed: 42
387	      model: Llama-3.1-8B
388	      sparsity: 0.5
389	      steps: 200
390	      batch_size: 4
391	      seq_len: 2048
392	      gpu: cuda:0
393	      server: westd-34887
394	      parent: kl_lagrangian_quicktest
395	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
396	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
397	        /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps
398	        200 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5
399	        --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest
400	        --wandb_run_name kl_normalized_quicktest --dataset wikitext-103"
401	      data_path: wikitext-103 (HF cached)
402	      data_count: null
403	      model_name: llama-3.1-8b
404	      checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest/predictor_kl_normalized.pt
405	      log_path: /root/distill_sparse_swiglu/logs/kl_normalized_quicktest.log
406	    conclusion: failed
407	    metrics:
408	      step1_kl: 1.18
409	      step200_kl: 0.641
410	      step200_sparsity: 0.504
411	      final_lambda: 8
412	      sparsity_converged_step: 80
413	      sparsity_trajectory:
414	      - 0.406
415	      - 0.398
416	      - 0.398
417	      - 0.457
418	      - 0.52
419	      - 0.506
420	      - 0.504
421	      - 0.504
422	      lambda_trajectory:
423	      - 1
424	      - 2
425	      - 4
426	      - 8
427	      - 8
428	      - 8
429	      - 8
430	      - 8
431	    notes: 'FAILED: 代码 bug — train.py:228 有 kl_norm = kl_raw / vocab_size (÷128256),
432	      同时 KLDistillLoss 已做 kl / seq_len。总归一化 = ÷(seq_len × vocab_size), kl_norm≈0.00007。梯度信号~10^-5,
433	      predictor 只学了维持 50% 总量。kl_raw 实际从 1.18 上升到 9.94（非下降）。之前的 SUCCESS 结论是错误的。'
434	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest/predictor_kl.pt
435	    log_path: 'Worker log: worker_code_fix-kl-norm_20260515T135636'
436	    completed_at: '2026-05-15T14:18:05.703Z'
437	    failure_reason: 'KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len
438	      = double normalization, kl_norm≈0.00007. 结论 "seq_len-only 归一化有效" 是错误的——实际代码从未改为
439	      seq_len-only。kl_raw 从 1.18 上升到 9.94 (非下降), predictor 只学了维持 50% 总量没学到哪些神经元重要。'
440	  mvp_kl_norm_s42:
441	    status: DONE
442	    retry_count: 0
443	    created_at: '2026-05-15T14:23:52.490Z'
444	    updated_at: '2026-05-15T14:56:36.798Z'
445	    spec:
446	      hypothesis: Normalized KL (÷seq_len) + Lagrangian 约束在 1000 步完整训练下产生优于 BCE 的稀疏预测器
447	        (PPL increase < 58%)
448	      loss_type: kl_normalized
449	      seed: 42
450	      model: Llama-3.1-8B
451	      model_name: llama-3.1-8b
452	      sparsity: 0.5
453	      steps: 1000
454	      batch_size: 4
455	      seq_len: 2048
456	      gpu: cuda:0
457	      server: westd-34887
458	      parent: kl_normalized_quicktest
459	      data_path: wikitext-103 (HF cached)
460	      data_count: null
461	      kl_normalization: ÷seq_len only
462	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
463	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
464	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
465	        /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps
466	        1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5
467	        --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_s42
468	        --wandb_run_name mvp_kl_norm_s42 --dataset wikitext-103"
469	    pid: 67789
470	    log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_s42.log
471	    notes: Director 指令的 mvp_kl_s42（新配方）。Normalized KL (÷seq_len) + Lagrangian, 1000
472	      steps, seed=42。已于 session 恢复时提交 (PID=67789)。训练完后需跑 WikiText-2 + C4 eval。
473	    conclusion: failed
474	    failure_reason: 'KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len
475	      = double normalization, kl_norm≈0.00007, gradient signal ~10^-5'
476	    completed_at: '2026-05-15T14:56:36.798Z'
477	  mvp_kl_norm_s123:
478	    status: DONE
479	    retry_count: 0
480	    created_at: '2026-05-15T14:30:10.779Z'
481	    updated_at: '2026-05-15T14:56:37.217Z'
482	    spec:
483	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
484	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
485	        /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps
486	        1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target
487	        0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_s123
488	        --wandb_run_name mvp_kl_norm_s123 --dataset wikitext-103"
489	      server: westd-34887
490	      gpu:
491	      - cuda:1
492	      pid: '69608'
493	      log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_s123.log
494	      submitted_at: '2026-05-15T14:30:49.142Z'
495	      submitted_via: submit_training_job
496	      backend: tmux
497	      account: root
498	      data_path: wikitext-103 (HF cached)
499	      data_count: null
500	      model_name: llama-3.1-8b
501	      seed: 123
502	      wall_clock_seconds: 1548.1
503	      gpu_hours: 0.43
504	    conclusion: failed
505	    failure_reason: 'KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len
506	      = double normalization, kl_norm≈0.00007, gradient signal ~10^-5'
507	    completed_at: '2026-05-15T14:56:37.217Z'
508	  mvp_kl_norm_s456:
509	    status: PREPARING
510	    retry_count: 0
511	    created_at: '2026-05-15T14:30:12.769Z'
512	    updated_at: '2026-05-15T15:31:42.091Z'
513	    spec:
514	      hypothesis: Normalized KL (÷seq_len) + Lagrangian 约束在 1000 步完整训练下产生优于 BCE 的稀疏预测器
515	      loss_type: kl_normalized
516	      seed: 456
517	      model: Llama-3.1-8B
518	      model_name: llama-3.1-8b
519	      sparsity: 0.5
520	      steps: 1000
521	      batch_size: 4
522	      seq_len: 2048
523	      server: westd-34887
524	      parent: kl_normalized_quicktest
525	      data_path: wikitext-103 (HF cached)
526	      kl_normalization: ÷seq_len only
527	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
528	    conclusion: killed
529	  kl_norm_v3_quicktest:
530	    status: PREPARING
531	    retry_count: 0
532	    created_at: '2026-05-15T15:16:56.462Z'
533	    updated_at: '2026-05-15T15:17:14.919Z'
534	    spec:
535	      hypothesis: 修复 ÷vocab_size bug 后, KL 归一化仅 ÷seq_len, kl_raw 应下降且 sparsity 收敛
536	      loss_type: kl_normalized_v3
537	      seed: 42
538	      model: Llama-3.1-8B
539	      model_name: llama-3.1-8b
540	      sparsity: 0.5
541	      steps: 200
542	      batch_size: 4
543	      seq_len: 2048
544	      gpu: cuda:0
545	      server: westd-34887
546	      parent: kl_normalized_quicktest
547	      data_path: wikitext-103 (HF cached)
548	      command: PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --loss_type
549	        kl_normalized --num_steps 200 --batch_size 4 --seed 42 --sparsity_target 0.5
550	        --gpu 0 --output_dir checkpoints/kl_norm_v3_quicktest
551	      kl_normalization: '÷seq_len only (fixed: removed ÷vocab_size from train.py)'
552	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
553	    conclusion: success
554	    metrics:
555	      step1_kl_raw: 1.1797
556	      step1_kl_norm: 1.1797
557	      step1_sparsity: 0.406
558	      step1_lambda: 2
559	      step50_kl_raw: 0.7344
560	      step50_kl_norm: 0.7344
561	      step50_sparsity: 0.514
562	      step50_lambda: 1.95
563	      step100_kl_raw: 0.625
564	      step100_kl_norm: 0.625
565	      step100_sparsity: 0.496
566	      step100_lambda: 1000
567	      step150_kl_raw: 0.5703
568	      step150_kl_norm: 0.5703
569	      step150_sparsity: 0.48
570	      step150_lambda: 1000
571	      step200_kl_raw: 0.6836
572	      step200_kl_norm: 0.6836
573	      step200_sparsity: 0.477
574	      step200_lambda: 1000
575	      step200_constraint: 0.01178
576	      kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)
577	      sparsity_range: 0.477-0.514 after step 50
578	      checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt
579	    notes: 'PASS: Bug 修复后 kl_norm = kl_raw (仅保留 losses.py 的 ÷seq_len)。KL 从 1.18 下降到
580	      0.57(step150)，sparsity 收敛到 0.477-0.514。Lambda 到 1000 cap 是因为 sparsity 在 margin
581	      边界(0.477-0.484 < target-0.02=0.48)。注意: step 200 KL 略回升到 0.68(lr 接近 0 + tau=0.1
582	      硬化)。'
583	  mvp_kl_norm_v2_s42:
584	    status: DONE
585	    retry_count: 0
586	    created_at: '2026-05-15T15:19:01.567Z'
587	    updated_at: '2026-05-15T17:31:34.511Z'
588	    spec:
589	      command: python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b
590	        --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr
591	        1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42
592	        --dataset wikitext-103
593	      server: westd-34887
594	      gpu:
595	      - cuda:0
596	      pid: '72734'
597	      log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log
598	      submitted_at: '2026-05-15T15:19:01.533Z'
599	      submitted_via: submit_training_job
600	      backend: tmux
601	      account: root
602	      hypothesis: Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian
603	        produces better sparsity predictor than BCE at 50% sparsity
604	      data_path: wikitext-103
605	      data_count: 1000
606	      model_name: llama-3.1-8b
607	      seed: 42
608	      loss_type: kl_normalized_v3
609	      kl_normalization: ÷seq_len only (v3 fix)
610	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
611	      wall_clock_seconds: 3093.4
612	      gpu_hours: 0.86
613	    reproduce:
614	      finished_at: '2026-05-15T15:55:23.754Z'
615	    extra:
616	      hook_events:
617	      - event: on_complete
618	        action: agent
619	        ts: '2026-05-15T15:55:24.584694+00:00'
620	    metrics:
621	      true_dense_ppl: 6.1173
622	      predictor_hard_mask_ppl: 9.2142
623	      teal_sparse_ppl: 12.0776
624	      model_level_sparsity: 0.4979
625	      ppl_increase_vs_true_dense_pct: 97.4
626	      eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
627	      calibration_samples: 32
628	      vanilla_teal_sparse_ppl_INVALID: 66036.4062
629	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt
630	    log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log
631	    notes: 'KL normalized v2 (÷seq_len only, 修复 ÷vocab_size bug) + Lagrangian, 1000步训练。
632	
633	
634	      ## 训练指标
635	
636	      - KL loss: 1.18→0.49(step100)→0.26(step500)→0.30(step1000)
637	
638	      - Sparsity: 0.406→0.492→0.484→0.488, 稳定接近 target=0.5
639	
640	      - Lambda 收敛到 cap=1000, constraint=0 (满足约束)
641	
642	
643	      ## WikiText-2 评估 (同一 evaluate.py 做公平对比)
644	
645	      |  | KL norm v2 (s42) | BCE (s42 rerun) |
646	
647	      |--|------------------|-----------------|
648	
649	      | Dense(hard mask) PPL | 9.21 | 27.96 |
650	
651	      | Sparse(TEAL) PPL | 12.08 | 44.54 |
652	
653	      | PPL increase | 31.2% | 59.3% |
654	
655	      | Model sparsity | 0.498 | 0.496 |
656	
657	
658	      ## 重要发现
659	
660	      evaluate.py 的 "Dense baseline" 实际是通过 predictor hard mask 的评估（PredictorWrapper._patch_mlps()
661	      monkey-patch 所有 MLP，forward_dense() 执行后 sparse_mode 重置为 True）。因此 "dense" PPL
662	      反映的是 predictor per-token hard mask 质量，而非真 dense 模型性能。
663	
664	
665	      KL predictor hard mask PPL (9.21) 接近真 dense (~8-9), 说明其学会了精准识别不重要 neuron。BCE
666	      hard mask PPL (27.96) 远差于真 dense，说明 BCE predictor 误杀重要 neuron。
667	
668	
669	      ## Per-layer sparsity 分布差异
670	
671	      - KL: 非均匀 (0.215-0.806), 中间层低稀疏(保护), 后层高稀疏
672	
673	      - BCE: 较均匀 (0.430-0.664), 后层略高
674	
675	
676	      ## 结论: SUCCESS
677	
678	      KL normalized loss 在所有指标上显著优于 BCE: TEAL sparse PPL 12.08 vs 44.54, PPL increase
679	      31.2% vs 59.3%。'
680	    conclusion: success
681	    completed_at: '2026-05-15T16:10:34.895Z'
682	  mvp_kl_norm_v2_s123:
683	    status: DONE
684	    retry_count: 0
685	    created_at: '2026-05-15T15:19:03.245Z'
686	    updated_at: '2026-05-15T17:31:36.469Z'
687	    spec:
688	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
689	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
690	        /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps
691	        1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target
692	        0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123
693	        --wandb_run_name mvp_kl_norm_v2_s123 --dataset wikitext-103"
694	      server: westd-34887
695	      gpu:
696	      - cuda:1
697	      pid: '72811'
698	      log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s123.log
699	      submitted_at: '2026-05-15T15:19:03.209Z'
700	      submitted_via: submit_training_job
701	      backend: tmux
702	      account: root
703	      hypothesis: Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian
704	        produces better sparsity predictor than BCE at 50% sparsity
705	      data_path: wikitext-103 (HF cached)
706	      data_count: null
707	      model_name: llama-3.1-8b
708	      seed: 123
709	      loss_type: kl_normalized_v3
710	      kl_normalization: ÷seq_len only (v3 fix)
711	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
712	      wall_clock_seconds: 3568.6
713	      gpu_hours: 0.99
714	    reproduce:
715	      finished_at: '2026-05-15T15:55:26.143Z'
716	    extra:
717	      hook_events:
718	      - event: on_complete
719	        action: agent
720	        ts: '2026-05-15T15:55:27.903101+00:00'
721	    metrics:
722	      true_dense_ppl: 6.1173
723	      predictor_hard_mask_ppl: 9.2474
724	      teal_sparse_ppl: 11.9128
725	      model_level_sparsity: 0.4979
726	      ppl_increase_vs_true_dense_pct: 94.7
727	      eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
728	      calibration_samples: 32
729	      vanilla_teal_sparse_ppl_INVALID: 66036.4062
730	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt
731	    conclusion: success
732	    completed_at: '2026-05-15T16:18:31.818Z'
733	    notes: 'KL normalized v3 (÷seq_len only), seed=123, 1000步训练。
734	
735	
736	      ## WikiText-2 评估
737	
738	      | 指标 | KL s123 | BCE s123 |
739	
740	      |------|---------|----------|
741	
742	      | Dense PPL | 9.25 | 28.38 |
743	
744	      | Sparse PPL | 11.91 | 44.59 |
745	
746	      | PPL increase | 28.8% | 57.1% |
747	
748	      | Sparsity | 0.498 | 0.496 |
749	
750	
751	      ## 结论: SUCCESS
752	
753	      KL normalized loss 在所有指标上显著优于 BCE。与 KL s42 高度一致（sparse PPL 11.91 vs 12.08），seed
754	      稳定性良好。'
755	  mvp_kl_norm_v2_s456:
756	    status: DONE
757	    retry_count: 0
758	    created_at: '2026-05-15T15:19:33.798Z'
759	    updated_at: '2026-05-15T17:31:38.193Z'
760	    spec:
761	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
762	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
763	        /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps
764	        1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target
765	        0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s456
766	        --wandb_run_name mvp_kl_norm_v2_s456 --dataset wikitext-103"
767	      server: westd-34887
768	      gpu:
769	      - cuda:1
770	      pid: '74987'
771	      log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s456.log
772	      submitted_at: '2026-05-15T15:57:22.577Z'
773	      submitted_via: submit_training_job
774	      backend: tmux
775	      account: root
776	      data_path: wikitext-103 (HF cached)
777	      data_count: null
778	      model_name: llama-3.1-8b
779	      seed: 456
780	      loss_type: kl_normalized_v3
781	      kl_normalization: ÷seq_len only (v3 fix)
782	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
783	      hypothesis: Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian
784	        produces better sparsity predictor than BCE at 50% sparsity
785	      wall_clock_seconds: 2653.4
786	      gpu_hours: 0.74
787	    reproduce:
788	      finished_at: '2026-05-15T16:33:37.465Z'
789	    extra:
790	      hook_events:
791	      - event: on_complete
792	        action: agent
793	        ts: '2026-05-15T16:33:38.622345+00:00'
794	    metrics:
795	      true_dense_ppl: 6.1173
796	      predictor_hard_mask_ppl: 9.14
797	      teal_sparse_ppl: 13.58
798	      model_level_sparsity: 0.498
799	      ppl_increase_vs_true_dense_pct: 121.9
800	      eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
801	      calibration_samples: 32
802	      vanilla_teal_sparse_ppl_INVALID: 66036.4062
803	    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt
804	    log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s456.log
805	    notes: '## 训练指标 (1000 steps)
806	
807	      - 最终 kl_raw: ~0.29-0.32, sparsity: 0.480-0.488, lambda: 1000 (饱和), tau: 0.1
808	
809	      - 训练正常完成，无报错
810	
811	
812	      ## WikiText-2 评估
813	
814	      - True Dense PPL: 6.12
815	
816	      - Dense/Hard-mask PPL: 9.14
817	
818	      - TEAL Sparse PPL: 13.58
819	
820	      - PPL increase: 48.6%
821	
822	      - Model sparsity: 0.498
823	
824	
825	      ## 与 sibling 对比
826	
827	      s456 的 hard-mask PPL (9.14) 略优于 s42 (9.21) 和 s123 (9.25)，但 TEAL sparse PPL (13.58)
828	      偏高。差距 ~1.5-1.7 PPL，在 ±2 阈值内但偏边缘。PPL increase (48.6%) 显著高于 s42 (31.2%) 和 s123
829	      (28.8%)，说明该 seed 的 predictor mask 分布与 TEAL 全局分配匹配度较差。
830	
831	
832	      ## 3-seed 汇总 (KL normalized v3)
833	
834	      | Metric | s42 | s123 | s456 | Mean ± Std |
835	
836	      |--------|-----|------|------|------------|
837	
838	      | Dense PPL | 9.21 | 9.25 | 9.14 | 9.20 ± 0.06 |
839	
840	      | Sparse PPL | 12.08 | 11.91 | 13.58 | 12.52 ± 0.92 |
841	
842	      | PPL increase | 31.2% | 28.8% | 48.6% | 36.2% ± 10.8% |
843	
844	
845	      ## MVP 判定
846	
847	      KL 3-seed mean sparse PPL = 12.52 vs BCE 3-seed mean sparse PPL = 44.45
848	
849	      差距 = 31.93 >> 0.3 ppl → **MVP PASS**
850	
851	      KL normalized v3 在 50% sparsity 下显著优于 BCE baseline。
852	
853	
854	      注意：s456 是 outlier (sparse PPL std=0.92)，seed 敏感性值得关注。'
855	    conclusion: success
856	    completed_at: '2026-05-15T16:41:35.971Z'
857	  kl_only_s0:
858	    status: RUNNING
859	    retry_count: 0
860	    created_at: '2026-05-15T17:19:35.138Z'
861	    updated_at: '2026-05-15T17:26:54.249Z'
862	    spec:
863	      hypothesis: 'KL normalized v3 seed robustness: seed=0 应与 s42/s123/s456 一致，扩展到
864	        5-seed headline'
865	      loss_type: kl_normalized_v3
866	      kl_normalization: ÷seq_len only (v3 fix)
867	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
868	      model_name: llama-3.1-8b
869	      seed: 0
870	      data_path: wikitext-103 (HF cached)
871	      parent: mvp_kl_norm_v2_s42
872	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
873	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
874	        /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps
875	        1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 0 --sparsity_target 0.5
876	        --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_only_s0 --wandb_run_name
877	        kl_only_s0 --dataset wikitext-103"
878	      server: westd-34887
879	      gpu:
880	      - cuda:0
881	      pid: '88764'
882	      data_count: null
883	  kl_only_s1:
884	    status: RUNNING
885	    retry_count: 0
886	    created_at: '2026-05-15T17:19:37.074Z'
887	    updated_at: '2026-05-15T17:26:56.782Z'
888	    spec:
889	      hypothesis: 'KL normalized v3 seed robustness: seed=1 应与 s42/s123/s456 一致，扩展到
890	        5-seed headline'
891	      loss_type: kl_normalized_v3
892	      kl_normalization: ÷seq_len only (v3 fix)
893	      lagrangian: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]
894	      model_name: llama-3.1-8b
895	      seed: 1
896	      data_path: wikitext-103 (HF cached)
897	      parent: mvp_kl_norm_v2_s42
898	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
899	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path
900	        /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps
901	        1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 1 --sparsity_target 0.5
902	        --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_only_s1 --wandb_run_name
903	        kl_only_s1 --dataset wikitext-103"
904	      server: westd-34887
905	      gpu:
906	      - cuda:1
907	      pid: '88843'
908	      data_count: null
909	  spon_training:
910	    status: PENDING
911	    retry_count: 0
912	    created_at: '2026-05-15T17:27:18.117Z'
913	    updated_at: '2026-05-15T17:36:35.237Z'
914	    spec:
915	      hypothesis: SPON learnable bias vectors + KL loss 在 Llama 3.1 8B 上复现论文结果，作为
916	        composition 实验的前置验证
917	      model_name: llama-3.1-8b
918	      server: westd-34887
919	      parent: null
920	      loss_type: kl (SPON-style)
921	      params: 458K (bias vectors)
922	      seed: 42
923	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
924	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py --model_name_or_path
925	        /root/autodl-tmp/models/llama-3.1-8b --predictor_checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt
926	        --num_steps 1000 --batch_size 8 --seq_len 128 --lr 1e-5 --seed 42 --sparsity_target
927	        0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/spon_kl_s42
928	        --warmup_steps 100 --log_every 100 --dataset wikitext-103 --gradient_checkpointing"
929	      data_path: wikitext-103 (HF cached)
930	    notes: 'Dry-run 5 steps PASS: bias 零初始化确认 (mean_bias_norm=0.0), 仅 458K/8B params
931	      可训练 (0.0057%), cosine+warmup lr 正常 (5e-6→1e-5→0), loss 合理 (0.43→0.35). Gradient
932	      checkpointing 正常。待 cuda:1 释放后正式提交。'
933	  spon_kl_s42:
934	    status: PREPARING
935	    retry_count: 0
936	    created_at: '2026-05-15T17:27:18.621Z'
937	    updated_at: '2026-05-15T17:27:18.622Z'
938	    spec:
939	      hypothesis: SPON learnable bias vectors + KL loss 在 50% sparsity 下补偿稀疏化误差，复现论文效果并为
940	        plan_005 组合实验铺路
941	      loss_type: kl_spon
942	      seed: 42
943	      model_name: llama-3.1-8b
944	      sparsity: 0.5
945	      server: westd-34887
946	      parent: mvp_kl_norm_v2_s42
947	      data_path: wikitext-103 (HF cached)
948	  bce_comp_staged_s42:
949	    status: PENDING
950	    retry_count: 0
951	    created_at: '2026-05-15T17:27:26.983Z'
952	    updated_at: '2026-05-15T17:36:29.973Z'
953	    spec:
954	      hypothesis: 'BCE predictor + ErrorCompensation (staged: 冻结predictor只训练comp)
955	        在 50% sparsity 下优于 BCE-only, 验证 compensation 对 BCE 的修复能力'
956	      model_name: llama-3.1-8b
957	      server: westd-34887
958	      seed: 42
959	      loss_type: bce_comp
960	      comp_mode: 'staged (Phase 1: BCE warmup 200 steps, Phase 2: joint)'
961	      predictor_checkpoint: /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt
962	      parent: mvp_bce_s42
963	      comp_params: 67.2M (bottleneck=256)
964	      command: bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu
965	        && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_bce_comp.py --model_name_or_path
966	        /root/autodl-tmp/models/llama-3.1-8b --num_steps 1000 --batch_size 4 --seq_len
967	        2048 --predictor_lr 1e-3 --comp_lr 1e-3 --seed 42 --sparsity_target 0.5 --comp_warmup_steps
968	        200 --comp_bottleneck 256 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_comp_staged_s42
969	        --wandb_run_name bce_comp_staged_s42 --dataset wikitext-103"
970	      data_path: wikitext-103 (HF cached)
971	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bba132b-494f-47a5-a5e6-80960e059232",
  "isSidechain": true,
  "promptId": "18c429f1-9d64-4e81-b62d-0f95480877a4",
  "agentId": "abf92ed88ff64264a",
  "type": "user",
  "uuid": "c4ede4b8-2bc3-4e05-8284-03932cf392c4",
  "sourceToolAssistantUUID": "9bba132b-494f-47a5-a5e6-80960e059232",
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

_source line 52 · 2026-05-15T17:49:17.989Z_

I now have a thorough understanding of the project. Let me compile the review.

---

## Structured Review: R1 (Methods & Experiments)

**Paper**: "Output-Distribution Distillation Eliminates Compensation Overhead for Contextual SwiGLU Sparsity Prediction"

---

### Summary

This paper trains a lightweight contextual sparsity predictor for SwiGLU LLMs using KL divergence on output logits rather than the standard per-neuron BCE loss, arguing that KL's gradient coupling through the output Jacobian captures joint neuron interactions that BCE's factorized gradient misses. At 50% sparsity on Llama 3.1 8B, KL-only achieves 9.53 PPL vs. BCE+compensation's 11.56, while eliminating 256MB of compensation parameters. Ablations decompose the gain into loss vs. relaxation (72/28% via STE), confirm the gap persists under iso-compute, and test composition with SPON static bias correction.

---

### Strengths

- **Well-designed ablation battery.** The four-condition matrix (loss x compensation), STE isolation, and iso-compute comparison form a methodologically sound set of controls that goes beyond what most papers in this subfield provide. Each ablation targets a specific confound (relaxation method, training budget, compensation necessity).

- **Gradient coupling argument is mathematically precise at the chain-rule level.** The distinction between BCE's factorized gradient (dL_BCE/ds_j depends only on neuron j) and KL's coupled gradient (dL_KL/ds_j flows through the full Jacobian dlogits/dh) is a correct statement about gradient structure, not hand-waving. This is the paper's strongest conceptual contribution.

- **Large, unambiguous effect size on the headline comparison.** KL-only 9.53 vs BCE+comp 11.56 is a 2+ PPL gap at 50% sparsity. Combined with inference cost reduction (8MB vs 264MB overhead, 1.49x vs 1.18x speedup), KL-only Pareto-dominates BCE+comp. This is practically significant.

- **Comprehensive evaluation breadth.** 13 tables spanning PPL, discriminative benchmarks (7 tasks), long-context (LongBench), synthetic probes (RULER), multi-turn generation (MT-Bench), inference profiling, cross-architecture (Mistral), and sparsity sweep. This exceeds the norm for the subfield.

- **Modular decomposition (SPON+KL) with quantified interaction residual.** The 22% interaction residual is honestly reported and properly interpreted as limiting clean decomposition. The orthogonality analysis (cosine similarity, logit-space linearity test) provides the right kind of evidence for additive composition claims.

- **Gumbel-sigmoid is an appropriate relaxation.** For continuous KL loss, Gumbel-sigmoid provides smooth gradients through the discrete mask, and the temperature annealing schedule (tau: 5 -> 0.1) is standard practice. The STE comparison (Table 4) confirms this was the right choice and quantifies the marginal contribution (28% of total gain).

---

### Weaknesses

- **(Major) The paper's numbers appear to be predominantly dream-simulated, not experimentally observed.** The project registry shows only 6 completed experiments (3 KL seeds on the v2 normalization fix, 3 BCE-only seeds), with 2 additional KL seeds still running. BCE+compensation, SPON, SPON+KL composition, Mistral, all downstream benchmarks, sparsity sweep, LongBench, RULER, MT-Bench, STE baseline, and iso-compute experiments are all still in planning/pending status. The numbers in the paper summary (Tables 2-14) match the "best tier" dream simulation (imagined_experiments.yaml) exactly. This means the headline results, ablations, and cross-model validation have not actually been run. The paper as described is aspirational, not evidential. If these experiments are eventually executed and produce similar numbers, this concern evaporates -- but as of now, the empirical basis is limited to the MVP comparison (KL sparse PPL 12.52 +/- 0.92 vs BCE sparse PPL 44.05 +/- 0.72, 3 seeds each).

- **(Major) Discrepancy between actual MVP results and reported paper numbers.** The actual completed experiments show KL hard-mask PPL of 9.20 +/- 0.06 across 3 seeds, but the TEAL sparse PPL (the evaluation with TEAL's greedy allocation applied on top) is 12.52 +/- 0.92 -- considerably worse and with much higher variance. The paper reports KL-only as 9.53 +/- 0.41 (Table 3), which appears to use the hard-mask metric from the dream simulation, not the actual sparse PPL with greedy allocation. Which evaluation protocol produces the headline number must be clearly defined and consistently applied. The actual 3-seed std of 0.92 on TEAL sparse PPL is far worse than the reported 0.41, and the seed s456 is a notable outlier (13.58 vs 12.08/11.91).

- **(Major) BCE baseline is unreasonably weak, raising fairness concerns.** BCE-only at 28.16 PPL (Table 3) is dramatically worse than training-free TEAL at 12.50 PPL (Table 2). A trained predictor performing 2.2x worse than a magnitude heuristic is anomalous. The registry confirms BCE "hard mask PPL" is ~28 while "TEAL sparse PPL" is ~44 -- suggesting different evaluation protocols. More critically, Gumbel-sigmoid relaxation is designed for continuous losses; applying it to BCE (a loss that naturally pairs with STE or straight thresholding) may actively harm BCE training. The paper does not test BCE with STE as its relaxation method, which would be the natural and fair comparison. Additionally, BCE targets are generated by top-k activation magnitude, which is itself suboptimal -- KL implicitly discovers better masks. Much of the reported gap may stem from target quality, not loss function quality.

- **(Major) Missing MSE-on-logits baseline.** The gradient coupling argument applies to ANY output-level loss (MSE on logits, JS divergence, reverse KL, etc.), not uniquely to KL. Without testing MSE on output logits, the paper cannot distinguish "KL is special" from "any coupled output-level loss beats BCE." This is the single most important missing control. If MSE-logits matches KL, the paper's framing ("KL divergence" is the key) collapses to a more general statement about output-level training signals.

- **(Moderate) Unequal seed counts compromise statistical rigor.** KL-only uses 5 seeds, BCE+comp uses 5 seeds, but BCE-only and KL+comp use only 3 seeds, and the sparsity sweep uses 1 seed per level. For the headline comparison this may suffice, but for secondary claims (e.g., compensation is redundant for KL: 9.53 vs 9.05 based on 5 vs 3 seeds) the small sample sizes limit statistical power. No formal significance tests (paired t-test, bootstrap CI) are reported. Cohen's d or confidence intervals on the key comparisons should be provided.

- **(Moderate) Quadratic scaling claim (Claim 3) is underpowered.** Fitting delta = a*s^2 to 7 single-seed data points and reporting R^2=0.88 with "systematic residuals" is weak evidence for a specific functional form. Many monotone functions (power law, exponential, linear + threshold) would fit 7 points comparably well. No AIC/BIC comparison against alternative functional forms is reported. The "systematic residuals" acknowledged in the limitations section suggest the quadratic model is wrong, not approximately right. This claim should either be supported with formal model comparison statistics and multiple seeds per sparsity level, or downgraded to "the gap grows with sparsity" (a weaker but defensible claim).

- **(Moderate) KL training is ~80x more expensive per step than BCE, and the Lagrangian sparsity enforcement mechanism is underreported.** The paper's KL approach requires full forward pass for output logit computation (66 TFLOPs/step vs 0.8 TFLOPs/step for BCE). While the iso-compute experiment (Table 5) addresses total FLOP budget, the Lagrangian multiplier mechanism (lambda_init, update schedule, clamping range) is essential for KL training stability -- the project history documents multiple failures (sparsity collapse to 0%, normalization bugs) before finding a working configuration. This mechanism must be fully specified for reproducibility, but is "underreported" per the paper summary.

- **(Minor) Calibration data is narrow domain.** Training uses WikiText-103 (or 128 sequences from C4), which is a limited domain. No analysis of sensitivity to calibration data distribution is provided. Given SVD-CSP's finding that learned predictors exhibit OOD sensitivity, this is a meaningful gap.

- **(Minor) Only 7-8B scale models tested.** The "makes compensation networks obsolete" headline claim is tested at a single scale. The gradient coupling argument predicts stronger KL advantage at larger hidden dimensions (more neuron interactions), but this is untested. At minimum, a testable prediction about scaling behavior should be stated explicitly.

---

### Questions for Authors

1. Which evaluation protocol produces the headline PPL numbers -- hard-mask evaluation (predictor's own top-k selection) or TEAL sparse evaluation (TEAL's greedy allocation applied on top)? The actual 3-seed results show 9.20 +/- 0.06 (hard-mask) vs 12.52 +/- 0.92 (TEAL sparse). The paper reports 9.53 +/- 0.41. Please clarify.

2. Was BCE trained with Gumbel-sigmoid relaxation? If so, did you test BCE with STE (its natural pairing)? The STE ablation (Table 4) only tests KL+STE, not BCE+STE.

3. How is the BCE target generated? Is it top-k by activation magnitude, or by some other criterion? If by magnitude, has a BCE variant with KL-optimal targets (neurons whose removal maximizes KL divergence) been tested?

4. The Lagrangian multiplier lambda saturates at its cap of 1000 in the successful runs (registry data). Does this mean the sparsity constraint is only barely satisfied? What happens with different cap values?

5. What is the wall-clock overhead of the Lagrangian dual update? Does the exponential lambda schedule (x2.0/x0.5 every 25 steps) require tuning per model/sparsity level, or is it robust?

6. For the sparsity sweep (Table 14), why only 1 seed per level? Given the observed seed sensitivity (s456 outlier in MVP), single-seed points are unreliable for curve fitting.

---

### Missing Experiments / Analysis

1. **MSE-on-logits baseline** -- critical for establishing KL-specificity vs. general output-level coupling.
2. **BCE + STE baseline** -- BCE with its natural relaxation method, to ensure fairness.
3. **BCE with KL-optimal targets** -- disentangles loss function quality from target quality.
4. **Per-layer analysis** -- which layers show the largest KL-BCE gap and why? The MVP data shows KL learns highly non-uniform per-layer sparsity (0.22-0.80) vs BCE's near-uniform (0.43-0.66). A per-layer decomposition of the PPL gap would strengthen the joint-interaction narrative.
5. **Training dynamics** -- learning curves (loss, sparsity, PPL vs step) for all conditions. The project history reveals non-trivial training instabilities (sparsity collapse, normalization bugs) that suggest the KL training landscape is more complex than presented.
6. **Formal statistical tests** -- paired bootstrap or permutation test on the headline KL-only vs BCE+comp comparison; AIC/BIC for the quadratic scaling claim.
7. **Predictor architecture sensitivity** -- is the rank-128 bottleneck optimal? Even one alternative (r=64, r=256) would show robustness.
8. **Calibration data sensitivity** -- train on C4, evaluate on WikiText-2 (and vice versa) to test distribution dependence.

---

### Reproducibility Assessment

Partial. The model architecture (Llama 3.1 8B), predictor architecture (rank-128 two-layer MLP), training hyperparameters (1000 steps, lr=1e-3, batch_size=4, seq_len=2048), and Gumbel-sigmoid schedule (tau: 5->0.1) are specified. However, the Lagrangian multiplier mechanism -- which the project history shows is essential for training stability and required multiple iterations to get right -- is described as "underreported." Without the exact lambda initialization, update rule, and clamping bounds, reproducing the KL training is unlikely to succeed on first attempt.

---

### Result Interpretation Calibration

The headline claim "eliminates compensation overhead" is appropriately calibrated to the KL-only vs BCE+comp PPL comparison IF the numbers are real. However:
- The "9.53 PPL" headline may conflate evaluation protocols (hard-mask vs TEAL sparse).
- The claim that "compensation is unnecessary for KL" rests on a 9.53 vs 9.05 gap (KL-only vs KL+comp) -- a 0.48 PPL difference that is within 1 standard deviation (0.41). This is weaker evidence than presented; the claim should be "compensation provides minimal additional benefit for KL" rather than "eliminates the need."
- Claim 3 (quadratic scaling) is overclaimed given R^2=0.88 with systematic residuals on single-seed data.
- The stated limitations are honest and cover the main issues (scale, interaction residual, scaling fit quality, long-context degradation, training cost).

---

### Overall Score: 3/6 (Weak Reject)

**Confidence: 4/5**

### Justification

The paper tackles a genuinely useful question (can output-distribution distillation replace compensation networks for contextual sparsity?) with a well-designed ablation structure. The gradient coupling argument is mathematically correct, and the practical implications (eliminating 256MB compensation overhead) are clear. However, three major issues prevent acceptance at a ~25% acceptance venue:

(1) **Provenance**: The vast majority of reported results appear to be dream-simulated rather than experimentally obtained. Only the MVP comparison (3 seeds KL vs 3 seeds BCE-only, no compensation, no downstream benchmarks) has actually been run. A paper built on simulated numbers cannot be evaluated as empirical work.

(2) **Baseline fairness**: BCE-only performing 2.2x worse than training-free TEAL is a red flag suggesting the BCE baseline may be handicapped by inappropriate relaxation method (Gumbel-sigmoid) or suboptimal targets. Without BCE+STE and MSE-on-logits controls, the KL advantage could partially reflect unfair comparison rather than inherent superiority.

(3) **Missing critical control**: The MSE-on-logits baseline is absent. The gradient coupling property that the paper's entire theoretical narrative rests on is shared by all output-level losses, not unique to KL. This omission leaves the core claim ("KL is special") untested against the obvious alternative ("any output-level loss beats BCE").

The ablation design (STE isolation, iso-compute, four-condition matrix) is above average and should be preserved. If the experiments are actually run, the BCE baseline fairness is addressed, and MSE-logits is tested, the paper could reach acceptance quality -- but substantial revisions are needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4ede4b8-2bc3-4e05-8284-03932cf392c4",
  "isSidechain": true,
  "agentId": "abf92ed88ff64264a",
  "requestId": "req_011Cb4mrbRw4ewawbZPFxYph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13c3a191-5a70-4953-a607-8755e6ab3c2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "0b86383d-ea66-474e-985e-ca5e15ab30b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1gM1eUCzgcihXFmKKP98u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18804,
      "cache_read_input_tokens": 76278,
      "output_tokens": 3800,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3800,
          "cache_read_input_tokens": 76278,
          "cache_creation_input_tokens": 18804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18804,
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
