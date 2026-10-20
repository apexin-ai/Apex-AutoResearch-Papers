# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty and related work**. Review the following

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0030f3fba786c882.jsonl`
- **Structured JSON:** [`0789efb4313b3b335619.json`](../../sessions/07/0789efb4313b3b335619.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-15T17:40:23.390Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty and related work**. Review the following paper rigorously. Score on a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary
"Output-Distribution Distillation Makes Compensation Networks Obsolete for SwiGLU Activation Sparsity"

The paper proposes replacing BCE loss with KL-divergence distillation for training contextual sparsity predictors in SwiGLU LLMs. Key claims:
1. KL-only predictor (no compensation network) achieves 9.20 PPL vs BCE+compensation 18.64 PPL on Llama 3.1 8B at 50% sparsity
2. Modular decomposition c = c_s + c_θ(x) combining SPON static bias + KL contextual prediction achieves 7.98 PPL with 6.8% interaction residual
3. KL-BCE quality gap scales quadratically with sparsity (R²=0.97)

## Method Details
- SwiGLU FFN sparsity: binary mask m on intermediate neurons h = g ⊙ u
- BCE trains per-neuron predictor with oracle targets (top-k by magnitude). Gradient factorizes: ∂L_BCE/∂s_j depends only on neuron j.
- KL trains same predictor architecture but minimizes KL(p_dense || p_sparse). Gradient couples neurons through Jacobian ∂z/∂h.
- Gumbel-sigmoid relaxation for differentiable mask during training.
- Modular decomposition: c = c_s (SPON static bias) + c_θ(x) (KL contextual). Approximately orthogonal since c_s is constant and c_θ(x) is zero-mean.

## Related Work Section (from paper)
**Training-free activation sparsity:** TEAL [Liu et al., 2024] magnitude thresholding + greedy allocation. WINA [Shen et al., 2024] weight-informed scoring. R-Sparse [Zhang et al., 2024] rank-aware scoring.

**Learned sparsity prediction:** FastForward [Wang et al., 2024] per-layer MLP with BCE + compensation MLP. SPON [Zhou et al., 2024] input-independent per-layer bias via KL distillation. ShadowLLM [Chen et al., 2024] MSE on intermediate representations.

**Knowledge distillation for sparsity:** KL standard in KD [Hinton et al., 2015] but "not applied to train contextual sparsity predictors."

## Discussion Section
Two-dimensional taxonomy: correction granularity (static → per-layer → per-token) × training signal coupling (BCE → MSE → KL). Prior work fills cells; this paper fills (per-token, KL) = Pareto-optimal.

## Full Experimental Results Summary
- 4-condition ablation: KL-only 9.20 vs BCE+comp 18.64 (Table 1)
- STE ablation: STE+KL 9.74 still >> Gumbel+BCE 28.16 (Table 2)
- Iso-compute: BCE extended 3200 steps → 25.41, still 16.21 gap to KL (Table 3)
- Training-free hierarchy: TEAL 12.48, R-Sparse 13.62, WINA 14.76 (Table 4)
- SPON validation: 10.82 PPL, QA drops 3-5 points (Table 5)
- SPON+KL composition: 7.98 PPL, 6.8% interaction residual (Table 6)
- Full benchmarks: KL-only avg drop 1.3%, SPON+KL 0.7%, BCE+comp 12.8% (Table 7)
- Latency: KL-only 12.0 ms/tok vs BCE+comp 13.8 ms/tok (Table 8)
- Sparsity sweep: Δ=as² R²=0.97 (Tables 9-10)
- Mistral-7B-v0.3: KL 8.22 vs BCE+comp 12.86 (Table 11)
- LongBench: KL avg 42.1 vs dense 43.5, BCE+comp 32.1 (Table 12)
- MT-Bench: KL 7.05 vs dense 7.21, BCE+comp 6.42 (Table 13)
- RULER: KL 4K/16K 93.8/86.1 vs BCE+comp 87.4/78.3 (Table 14)

## References in paper
8 references total: Shazeer 2020, Liu 2024, Shen 2024, Zhang 2024, Wang 2024, Zhou 2024, Chen 2024, Hinton 2015.

## Your Review Should Cover:

1. **Novelty assessment**: Is replacing BCE with KL for sparsity predictor training genuinely novel? SPON already uses KL for static correction. The jump to contextual KL prediction seems incremental. How significant is this contribution?

2. **Related work completeness**: Are there missing related works? Consider:
   - Other KD-based sparsity methods
   - Structured pruning with distillation
   - Other gradient-coupling arguments in ML
   - MSE-based distillation alternatives (ShadowLLM uses MSE — is MSE a natural middle ground?)
   - Differentiable pruning / mask learning literature
   - Activation sparsity in non-SwiGLU architectures

3. **Theoretical novelty**: The gradient coupling argument and quadratic scaling prediction — is this genuinely new theory, or a known property reframed? The O(s²D²) scaling argument is informal.

4. **Positioning honesty**: Does the paper fairly represent prior work? Is the comparison to FastForward fair (same predictor architecture, same training data)?

5. **Scope and generalization claims**: Only 7-8B models, only SwiGLU, only 2 architectures.

6. **Writing quality and presentation**: Is the paper well-organized? Are claims properly hedged?

Output your review in this format:
```
## R2 Review: Novelty & Related Work

### Summary
[2-3 sentences]

### Strengths
[Numbered list]

### Weaknesses
[Numbered list, with severity: Major/Minor]

### Questions for Authors
[Numbered list]

### Missing Related Work
[Specific papers/areas not cited]

### Novelty Assessment
[Detailed evaluation of contribution significance]

### Preliminary Score: X/6
### Confidence: X/5
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "e57781ad-59b7-4db9-8cf8-67f12a5a28aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T17:40:23.394Z_

```json
{
  "parentUuid": "e57781ad-59b7-4db9-8cf8-67f12a5a28aa",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
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
  "uuid": "40f29f7a-96d2-40d7-9693-290b2b1a4ec0",
  "timestamp": "2026-05-15T17:40:23.394Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T17:40:26.500Z_



I'll start by reading the project files to understand the full context of this paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40f29f7a-96d2-40d7-9693-290b2b1a4ec0",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mJoqApJwmmRvnVvXry",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81c8203a-9d9b-48c9-93c0-d56408fc5604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyfucKuuw9h3Vv2X91iHh6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7518,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7518,
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

_source line 4 · 2026-05-15T17:40:26.627Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LZYnEBuHZkgA8kpHw4brZi`</summary>

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
  "parentUuid": "81c8203a-9d9b-48c9-93c0-d56408fc5604",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mJoqApJwmmRvnVvXry",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50ff34bf-58c8-4d45-abba-e02ff7fc6baa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyfucKuuw9h3Vv2X91iHh6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7518,
      "cache_read_input_tokens": 8252,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7518,
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

_source line 5 · 2026-05-15T17:40:26.630Z_

<details><summary>↩ Tool result · `toolu_01LZYnEBuHZkgA8kpHw4brZi`</summary>

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
  "parentUuid": "50ff34bf-58c8-4d45-abba-e02ff7fc6baa",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "37abbf76-5052-4922-a5d8-30810636a505",
  "sourceToolAssistantUUID": "50ff34bf-58c8-4d45-abba-e02ff7fc6baa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T17:40:29.801Z_



Let me read the key project files to get full context on the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37abbf76-5052-4922-a5d8-30810636a505",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mK3t1urot38WLLiGQs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ad7f775-0441-401a-96da-972c044a23f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLJKpfc3Bmvd7XCaTWbXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 7 · 2026-05-15T17:40:30.863Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QARKmzykVqAip8o8YnMXSQ`</summary>

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
  "parentUuid": "7ad7f775-0441-401a-96da-972c044a23f2",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mK3t1urot38WLLiGQs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d06b703-44ed-4b02-8a2b-fbc26029f85f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLJKpfc3Bmvd7XCaTWbXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

### Tool result

_source line 8 · 2026-05-15T17:40:30.881Z_

<details><summary>↩ Tool result · `toolu_01QARKmzykVqAip8o8YnMXSQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| kl_only_s1 | — | — | — | — |\\n| kl_only_s0 | — | — | — | — |\\n\\n## 待处理\\n- spon_training（等待人工审批）\\n- bce_comp_staged_s42（等待人工审批）\\n- mvp_kl_s456（排队等待 GPU）\\n- mvp_kl_s123（排队等待 GPU）\\n- spon_kl_s42（准备中）\\n- mvp_kl_norm_s456（准备中）\\n- kl_norm_v3_quicktest（准备中）\\n- kl_lagrangian_v2（准备中）\\n\\n## 近期结论\\n- **mvp_kl_norm_v2_s456** (success): —\\n- **mvp_kl_norm_v2_s123** (success): —\\n- **mvp_kl_norm_v2_s42** (success): —\\n\\n## 趋势\\n成功 6 / 负向 2 / 失败 3 / 共 11\\ncalibration_samples: 32 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\n\\n## 告警\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n\", \"total_chars\": 793, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d06b703-44ed-4b02-8a2b-fbc26029f85f",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "545f3be0-75d3-4499-b1d6-35055d37330d",
  "sourceToolAssistantUUID": "3d06b703-44ed-4b02-8a2b-fbc26029f85f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:40:34.159Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012NpNDT7FsQGqSdZqZh8Gww`</summary>

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
  "parentUuid": "545f3be0-75d3-4499-b1d6-35055d37330d",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mK3t1urot38WLLiGQs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8be9650b-d512-4304-b039-b8092e0d03e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLJKpfc3Bmvd7XCaTWbXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

### Tool result

_source line 10 · 2026-05-15T17:40:34.176Z_

<details><summary>↩ Tool result · `toolu_012NpNDT7FsQGqSdZqZh8Gww`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be9650b-d512-4304-b039-b8092e0d03e2",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "d3b39101-132f-4ed4-a214-d637fb5217c0",
  "sourceToolAssistantUUID": "8be9650b-d512-4304-b039-b8092e0d03e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:40:34.331Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FNivUYvtm2HENfVX3fnje6`</summary>

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
  "parentUuid": "d3b39101-132f-4ed4-a214-d637fb5217c0",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mK3t1urot38WLLiGQs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2690434b-fd1d-47a1-8c08-b1d3fcaa015c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLJKpfc3Bmvd7XCaTWbXi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15770,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 15770,
          "cache_creation_input_tokens": 1293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1293,
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

_source line 12 · 2026-05-15T17:40:34.342Z_

<details><summary>↩ Tool result · `toolu_01FNivUYvtm2HENfVX3fnje6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml\", \"content\": \"# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\\n# Last updated: 2026-05-15\\n# Survey scope: 2023-2026, 4 directions\\n\\n# =============================================================================\\n# Direction 1: KL distillation for structured/activation sparsity\\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\\n# learnable bias correction, not predictor training. This is our novelty.\\n# =============================================================================\\n\\n- title: \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\"\\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\\n  venue: ICML 2026\\n  year: 2026\\n  arxiv_id: \\\"2512.12744\\\"\\n  category: direct-competitor\\n  role: \\\"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\\\"\\n  key_finding: \\\"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\\\"\\n  relevance_to_us: \\\"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\\\"\\n\\n- title: \\\"Compact Language Models via Pruning and Knowledge Distillation\\\"\\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv_id: \\\"2407.14679\\\"\\n  category: method-component\\n  role: \\\"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\\\"\\n  key_finding: \\\"Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration\\\"\\n  relevance_to_us: \\\"支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑\\\"\\n\\n- title: \\\"Instruction-Following Pruning for Large Language Models\\\"\\n  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]\\n  venue: ICML 2025\\n  year: 2025\\n  arxiv_id: \\\"2501.02086\\\"\\n  category: method-component\\n  role: \\\"训练sparse mask predictor的范式——input-dependent mask selection\\\"\\n  key_finding: \\\"训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM\\\"\\n  relevance_to_us: \\\"架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略\\\"\\n\\n# =============================================================================\\n# Direction 2: Output distribution preservation in pruning/sparsity\\n# =============================================================================\\n\\n- title: \\\"Distilling to Hybrid Attention Models via KL-Guided Layer Selection\\\"\\n  authors: []\\n  venue: arXiv\\n  year: 2025\\n  arxiv_id: \\\"2512.20569\\\"\\n  category: method-component\\n  role: \\\"KL散度引导layer selection——用distribution差异决定哪些层需要保留\\\"\\n  key_finding: \\\"用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策\\\"\\n  relevance_to_us: \\\"方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大\\\"\\n\\n# =============================================================================\\n# Direction 3: SPON和类似的learnable bias correction for sparsity\\n# =============================================================================\\n\\n- title: \\\"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\\\"\\n  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]\\n  venue: arXiv\\n  year: 2026\\n  arxiv_id: \\\"2602.00397\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor + error compensation双组件架构——与SPON的bias correction思路互补\\\"\\n  key_finding: \\\"组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速\\\"\\n  relevance_to_us: \\\"与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）\\\"\\n\\n- title: \\\"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models\\\"\\n  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]\\n  venue: arXiv\\n  year: 2025\\n  arxiv_id: \\\"2508.02128\\\"\\n  category: background\\n  role: \\\"N:M structured activation sparsity——hardware-friendly的sparsity pattern\\\"\\n  key_finding: \\\"Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合\\\"\\n  relevance_to_us: \\\"如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work\\\"\\n\\n# =============================================================================\\n# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)\\n# =============================================================================\\n\\n- title: \\\"Training-Free Activation Sparsity in Large Language Models\\\"\\n  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]\\n  venue: ICLR 2025 (Spotlight)\\n  year: 2025\\n  arxiv_id: \\\"2408.14690\\\"\\n  category: direct-competitor\\n  role: \\\"TEAL——我们的主要baseline，training-free magnitude pruning\\\"\\n  key_finding: \\\"对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速\\\"\\n  relevance_to_us: \\\"TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'\\\"\\n\\n- title: \\\"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\\\"\\n  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv_id: \\\"2310.17157\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor-based contextual sparsity的开创性工作——我们的直接对比对象\\\"\\n  key_finding: \\\"用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练\\\"\\n  relevance_to_us: \\\"DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL\\\"\\n\\n- title: \\\"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\\\"\\n  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]\\n  venue: EMNLP 2024\\n  year: 2024\\n  arxiv_id: \\\"2406.16635\\\"\\n  category: direct-competitor\\n  role: \\\"DejaVu的改进——更好的predictor架构和sparsity pattern enforcement\\\"\\n  key_finding: \\\"Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%\\\"\\n  relevance_to_us: \\\"ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补\\\"\\n\\n- title: \\\"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference\\\"\\n  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]\\n  venue: DATE 2025\\n  year: 2025\\n  arxiv_id: \\\"2411.12692\\\"\\n  category: background\\n  role: \\\"Training-free sign-bit predictor——极低开销的sparsity预测\\\"\\n  key_finding: \\\"仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU\\\"\\n  relevance_to_us: \\\"不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性\\\"\\n\\n- title: \\\"SVD Contextual Sparsity Predictors for Fast LLM Inference\\\"\\n  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]\\n  venue: arXiv\\n  year: 2026\\n  arxiv_id: \\\"2603.14110\\\"\\n  category: direct-competitor\\n  role: \\\"Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测\\\"\\n  key_finding: \\\"对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%\\\"\\n  relevance_to_us: \\\"虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同\\\"\\n\\n- title: \\\"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\\\"\\n  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2404.08763\\\"\\n  category: direct-competitor\\n  role: \\\"Contextual thresholding——不训练predictor，用统计threshold做sparsity\\\"\\n  key_finding: \\\"为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证\\\"\\n  relevance_to_us: \\\"CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优\\\"\\n\\n- title: \\\"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\\\"\\n  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]\\n  venue: ICLR 2025\\n  year: 2025\\n  arxiv_id: \\\"2504.19449\\\"\\n  category: background\\n  role: \\\"Training-free rank-aware方法——利用input channel sparsity和SVD\\\"\\n  key_finding: \\\"用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速\\\"\\n  relevance_to_us: \\\"Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的\\\"\\n\\n- title: \\\"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\\\"\\n  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]\\n  venue: MLSys 2025\\n  year: 2024\\n  arxiv_id: \\\"2412.01380\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning\\\"\\n  key_finding: \\\"Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升\\\"\\n  relevance_to_us: \\\"直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战\\\"\\n\\n# =============================================================================\\n# 补充：Activation function替换和sparsity增强\\n# =============================================================================\\n\\n- title: \\\"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\\\"\\n  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv_id: \\\"2310.04564\\\"\\n  category: background\\n  role: \\\"ReLU替换SiLU获得天然sparsity——替代路线\\\"\\n  key_finding: \\\"用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x\\\"\\n  relevance_to_us: \\\"替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作\\\"\\n\\n- title: \\\"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\\\"\\n  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2406.05955\\\"\\n  category: background\\n  role: \\\"dReLU获得90%+ sparsity——activation function工程的极致\\\"\\n  key_finding: \\\"提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速\\\"\\n  relevance_to_us: \\\"与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位\\\"\\n\\n- title: \\\"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\\\"\\n  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]\\n  venue: COLING 2025\\n  year: 2025\\n  arxiv_id: \\\"2402.13516\\\"\\n  category: background\\n  role: \\\"Progressive sparsification——渐进式增加sparsity regularization\\\"\\n  key_finding: \\\"三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity\\\"\\n  relevance_to_us: \\\"ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）\\\"\\n\\n- title: \\\"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\\\"\\n  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2411.02335\\\"\\n  category: background\\n  role: \\\"Activation sparsity的scaling law——理论基础\\\"\\n  key_finding: \\\"SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关\\\"\\n  relevance_to_us: \\\"理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一\\\"\\n\\n- title: \\\"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\\\"\\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\\n  venue: Euro-Par 2025\\n  year: 2025\\n  arxiv_id: \\\"2507.14179\\\"\\n  category: background\\n  role: \\\"Clustering-based sparsity prediction——用聚类简化prediction\\\"\\n  key_finding: \\\"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\\\"\\n  relevance_to_us: \\\"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\\\"\\n\\n# =============================================================================\\n# 竞争格局总结\\n# =============================================================================\\n#\\n# 我们的独特定位:\\n# 1. 唯一使用KL divergence训练activation sparsity predictor的工作\\n#    - DejaVu/ShadowLLM用BCE训练predictor\\n#    - SPON用KL但训练bias correction而非predictor\\n#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free\\n# 2. 专注SwiGLU模型的50% sparsity目标\\n#    - ReLU/dReLU方案需要替换activation function\\n#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)\\n# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity\\n#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching\\n#    - 我们将此insight应用到predictor训练\\n#\\n# 主要related work定位:\\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\\n# - vs DIP: trained predictor vs predictor-free pruning\\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\\n# - vs Fast Forward: KL loss vs BCE+error compensation\\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\\n\", \"total_chars\": 13950, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2690434b-fd1d-47a1-8c08-b1d3fcaa015c",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "0c651a0a-68fe-44f2-ad5a-1b9347aa3801",
  "sourceToolAssistantUUID": "2690434b-fd1d-47a1-8c08-b1d3fcaa015c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T17:40:38.075Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YHxDZ5mF1X8chwrtw9cAuk`</summary>

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
  "parentUuid": "0c651a0a-68fe-44f2-ad5a-1b9347aa3801",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mKcud1WoN8G1HDk6kN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0a4cfcf-0189-42f7-851d-ee837995f741",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019w1tTJGH22v5V3L23yGG4g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7561,
      "cache_read_input_tokens": 17063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7561,
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

_source line 14 · 2026-05-15T17:40:38.085Z_

<details><summary>↩ Tool result · `toolu_01YHxDZ5mF1X8chwrtw9cAuk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. (Headline claim)\\n\\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\\n\\n3. **KL advantage grows with sparsity level (testable prediction)**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s — to be validated by 7-level sparsity sweep (plan_008). If empirical scaling deviates from quadratic (linear, log, or phase transition), the actual pattern is itself a finding; abstract/intro will report observed scaling, not assumed quadratic.\\n\\n## Story Spine\\n\\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\\n\\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\\n\\n- **Our framing / headline question**: \\\"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\\\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\\n\\n- **Headline result template**: \\\"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation subsumes error compensation, enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff.\\\"\\n\\n## Two-Dimensional Taxonomy (Conceptual Contribution)\\n\\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\\n| Static                   | —                 | —                   | SPON          |\\n| Per-layer                | —                 | ShadowLLM           | —             |\\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\\n\\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Incremental / no new algorithm\\\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\\n\\n2. **\\\"KL wins only because more compute\\\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\\n\\n3. **\\\"Gumbel-sigmoid relaxation, not KL, explains gains\\\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\\n\\n4. **\\\"Single model / limited generalization\\\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\\n\\n5. **\\\"Effect size may not hold on downstream tasks\\\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\\n\\n6. **\\\"Unfair comparison: BCE+comp close to KL but at higher inference cost\\\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\\n\", \"total_chars\": 5504, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0a4cfcf-0189-42f7-851d-ee837995f741",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "31d6099d-c16d-48b4-8b2a-721f92a3a969",
  "sourceToolAssistantUUID": "c0a4cfcf-0189-42f7-851d-ee837995f741",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T17:40:39.090Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YQWaEC7ki9ZDK8ajcQBYr4`</summary>

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
  "parentUuid": "31d6099d-c16d-48b4-8b2a-721f92a3a969",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mKcud1WoN8G1HDk6kN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edb16281-a0b6-469d-9d7c-674342dd9f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019w1tTJGH22v5V3L23yGG4g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7561,
      "cache_read_input_tokens": 17063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7561,
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

_source line 16 · 2026-05-15T17:40:39.100Z_

<details><summary>↩ Tool result · `toolu_01YQWaEC7ki9ZDK8ajcQBYr4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md\", \"content\": \"# Memory — distill_sparse_swiglu\\n\\n## 决策记录\\n\\n- [2026-05-15] s0/s1 完成后 GPU 分配：cuda:0 → bce_comp_staged_s42 (plan_001), cuda:1 → spon_training (plan_004)。Director 要求秒级衔接。\\n- [2026-05-15] WINA global 预期会崩（跨层归一化问题），不排查。正式 baseline: TEAL greedy + WINA greedy。WINA global 仅作 \\\"why greedy allocation matters\\\" motivation example。\\n- [2026-05-15] BCE+comp 代码通过 Reviewer：compensation 67.2M params (bottleneck=256)。losses.py / predictor.py / spon.py 全 PASS。\\n- [2026-05-15] SPON 458K params (bias vectors)，dry-run 通过。\\n- [2026-05-15] MVP 结论：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity。KL 非均匀 per-layer 分配 (0.22-0.80)。\\n- [2026-05-15] s456 seed 敏感性：sparse PPL 13.58 vs s42 12.08 / s123 11.91，PPL increase 48.6% vs 31.2%/28.8%。需关注。\\n\", \"total_chars\": 729, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edb16281-a0b6-469d-9d7c-674342dd9f07",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "50165250-b761-48d0-bfd5-42087115bbc7",
  "sourceToolAssistantUUID": "edb16281-a0b6-469d-9d7c-674342dd9f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:40:39.623Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01129He11difuViD97qzKGyQ`</summary>

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
  "parentUuid": "50165250-b761-48d0-bfd5-42087115bbc7",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mKcud1WoN8G1HDk6kN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74bae965-3c40-4a4b-9227-a8c0b6f90092",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019w1tTJGH22v5V3L23yGG4g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7561,
      "cache_read_input_tokens": 17063,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7561
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 17063,
          "cache_creation_input_tokens": 7561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7561,
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

_source line 18 · 2026-05-15T17:40:39.632Z_

<details><summary>↩ Tool result · `toolu_01129He11difuViD97qzKGyQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-15 16:53 UTC | 更新原因: Reviewer warning 修正：BCE std 0.72→0.89，Claim 3 降级，SPON 预算提升，并行启动计划\\n\\n## 核心方向\\nKL-divergence 输出分布蒸馏训练 SwiGLU 激活稀疏性预测器，验证是否消除对 error compensation network 的需求，并测试与 SPON 静态校正的组合加性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-15 通过，D007）\\n- **MVP 结论**: KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity，差距 31.53 PPL\\n- **关键发现**: KL 非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66）；KL hard-mask PPL 9.20 接近 dense 6.12\\n- **Dream**: dream_20260515T164925 运行中（full review），等结果后批准 P0 实验\\n- **Experiment Plan**: 12 experiments（P0×7, P1×3, P2×2），总 196 GPU-hours。详见 experiment_plan.yaml\\n- **Reviewer Warning**: Claim 1 强度取决于 BCE+comp（未测）；Claim 3 降级为 testable prediction；SPON 复现是关键路径\\n\\n## 近期任务\\n- [x] MVP 验证（KL vs BCE @ 50% sparsity, 3 seeds）\\n- [x] 写 paper_framing.md + experiment_plan.yaml\\n- [x] 启动 Dream full review (dream_20260515T164925)\\n- [ ] 等 Dream 结果 → 按行动指令调整\\n- [ ] Dream 通过后并行启动: plan_001 BCE+comp (cuda:0) + plan_004 SPON (cuda:1)\\n- [ ] Agent 完成 vanilla TEAL baseline（队列中）\\n- [ ] 补 KL-only 2 seeds (s0, s1) → 5-seed headline\\n- [ ] 实现 BCE+compensation 训练流程\\n- [ ] 关注 s456 seed 敏感性（13.58 vs 12.08/11.91）\\n\\n## GPU 预算\\n- 本地: westd-34887 cuda:0, cuda:1 — RTX PRO 6000 Blackwell (98GB each)\\n- 可用: 444 GPU-hours remaining (480 - 36 MVP)\\n- 计划: P0 114h + P1 70h + P2 12h = 196h（44% 利用率）\\n- Constraint: C001 — 仅 cuda:0, cuda:1\\n\\n## 目标时间线\\n| 阶段 | 日期 | 内容 |\\n|------|------|------|\\n| Dream review | 05-15 | dream_20260515T164925 |\\n| Phase 1 | 05-15 ~ 05-18 | plan_001 BCE+comp + plan_004 SPON + plan_006 baselines（并行） |\\n| Phase 2 | 05-18 ~ 05-20 | plan_005 composition + plan_002 STE + plan_003 iso-compute |\\n| Phase 3 | 05-20 ~ 05-22 | plan_007 full eval + plan_008 sweep + plan_009 Mistral |\\n| Paper | 05-22 ~ 05-24 | Paper Agent Full Draft + iteration |\\n| Submit | 05-25 | ARR submission |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-15 | MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程 | mvp_kl_norm_v2_s42, mvp_kl_norm_v2_s123, mvp_kl_norm_v2_s456, mvp_bce_s42, mvp_bce_s123, mvp_bce_s456 |\\n| D006 | 2026-05-15 | 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_norm | kl_normalized_quicktest, mvp_kl_norm_s42, mvp_kl_norm_s123 |\\n| D005 | 2026-05-15 | KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练 | kl_normalized_quicktest, mvp_kl_s42, mvp_kl_s123, mvp_kl_s456 |\\n| D004 | 2026-05-15 | KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯  | kl_lagrangian_quicktest |\\n| D003 | 2026-05-15 | KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_w | mvp_kl_s42 |\\n| D002 | 2026-05-15 | 校准数据从 SlimPajama-627B 改为 WikiText-103 train split | mvp_kl_s42, mvp_bce_s42 |\\n| D001 | 2026-05-15 | MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perp | — |\\n\\n\\n\\n\", \"total_chars\": 2753, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74bae965-3c40-4a4b-9227-a8c0b6f90092",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "723e353e-ecbe-45f9-a732-6a0f4c9f4860",
  "sourceToolAssistantUUID": "74bae965-3c40-4a4b-9227-a8c0b6f90092",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T17:40:42.592Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WKC52s77x6KMv77ijt6Uoq`</summary>

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
  "parentUuid": "723e353e-ecbe-45f9-a732-6a0f4c9f4860",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mL1URt8HtKumqXegKL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f651c6e-9eae-41b1-8b04-be39fb43faf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsGi4gGWZ6vgneADtRVjpF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 20 · 2026-05-15T17:40:42.601Z_

<details><summary>↩ Tool result · `toolu_01WKC52s77x6KMv77ijt6Uoq`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f651c6e-9eae-41b1-8b04-be39fb43faf4",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "6c62920d-e311-498e-82e3-dc96809ec7b3",
  "sourceToolAssistantUUID": "1f651c6e-9eae-41b1-8b04-be39fb43faf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T17:40:43.378Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NYM6DaWMM87teTakZqdzXY`</summary>

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
  "parentUuid": "6c62920d-e311-498e-82e3-dc96809ec7b3",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mL1URt8HtKumqXegKL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e50bf6b-a392-4655-80e5-fc4121655767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsGi4gGWZ6vgneADtRVjpF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 24624,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 24624,
          "cache_creation_input_tokens": 4289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4289,
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

_source line 22 · 2026-05-15T17:40:43.386Z_

<details><summary>↩ Tool result · `toolu_01NYM6DaWMM87teTakZqdzXY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 8\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C 保持原始研究问题（纯 KL 训练），给出最干净的 MVP 信号。\\n  related_experiments:\\n  - exp_id: kl_lagrangian_quicktest\\n    role: evidence\\n    result: sparsity 0.406→0.141, lambda too slow\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 14:19 UTC\\n  summary: KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练\\n  rationale: kl_normalized_quicktest 验证 KL/seq_len 归一化 + Lagrangian 配方有效：sparsity\\n    在 200 steps 内收敛到 0.50-0.52，KL loss 与 constraint 同量级。无需再测 KL/(seq_len×vocab_size)\\n    variant。BCE 3-seed 已全部 success，现在用修正配方跑 KL 3-seed (s42/s123/s456) 完成 MVP 对比。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: validation\\n    result: sparsity converged to 0.50-0.52\\n  - exp_id: mvp_kl_s42\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s123\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s456\\n    role: next\\n    result: pending\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 14:35 UTC\\n  summary: 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_normalized_quicktest 结论虚假\\n  rationale: Reviewer 独立核实发现 train.py:228 在 KLDistillLoss 已做 ÷seq_len 的基础上又除以 vocab_size(128256)，总归一化\\n    = ÷(seq_len×vocab_size)。实际效果：kl_norm≈0.00007，梯度信号~10^-5，predictor 无法学习神经元重要性。kl_raw\\n    从 1.18 上升至 9.94（而非 Agent 报告的下降）。Agent 的 registry 结论 \\\"seq_len-only 归一化有效\\\" 与代码事实完全矛盾。D005\\n    决策基于虚假数据，作废。修复方案：删除 ÷vocab_size，只保留 ÷seq_len，修复后重新验证。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: evidence\\n    result: FALSELY reported as success; actual KL rising, code uses ÷vocab_size not\\n      ÷seq_len\\n  - exp_id: mvp_kl_norm_s42\\n    role: killed\\n    result: Using same buggy code, gradient signal ~10^-5\\n  - exp_id: mvp_kl_norm_s123\\n    role: killed\\n    result: Using same buggy code, just submitted\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D007\\n  date: 2026-05-15 16:49 UTC\\n  summary: 'MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程'\\n  rationale: MVP 结果决定性通过：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.72（差距 31.53 >>\\n    0.3 阈值）。KL 学习非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66），hard-mask PPL 9.20\\n    接近 true dense 6.12。核心假设\\\"KL 通过端到端梯度捕获联合神经元交互优于 BCE\\\"得到强力验证。按 post-mvp-kickoff 流程：写\\n    paper_framing.md + experiment_plan.yaml → dream_simulate → update_roadmap。禁止在\\n    dream 完成前批准新实验。\\n  related_experiments:\\n  - exp_id: mvp_kl_norm_v2_s42\\n    role: evidence\\n    result: success, sparse PPL 12.08\\n  - exp_id: mvp_kl_norm_v2_s123\\n    role: evidence\\n    result: success, sparse PPL 11.91\\n  - exp_id: mvp_kl_norm_v2_s456\\n    role: evidence\\n    result: success, sparse PPL 13.58\\n  - exp_id: mvp_bce_s42\\n    role: evidence\\n    result: success, sparse PPL 44.54\\n  - exp_id: mvp_bce_s123\\n    role: evidence\\n    result: success, sparse PPL 44.59\\n  - exp_id: mvp_bce_s456\\n    role: evidence\\n    result: success, sparse PPL 43.03\\n  depends_on:\\n  - D001\\n  - D004\\n  - D005\\n  - D006\\n\", \"total_chars\": 4509, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e50bf6b-a392-4655-80e5-fc4121655767",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "19ffc61a-9ff5-4b9e-bb2a-a32b078a4d10",
  "sourceToolAssistantUUID": "1e50bf6b-a392-4655-80e5-fc4121655767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T17:40:46.260Z_

Now let me check the experiment plan and any artifacts for more detail on the experimental setup.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19ffc61a-9ff5-4b9e-bb2a-a32b078a4d10",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mLHX5S84BaRVYhXy3n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f22c7705-0f0b-416b-bf8f-163c3c423227",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193hh38KKGVrgmDxEiGDoKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2916,
      "cache_read_input_tokens": 28913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2916,
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

_source line 24 · 2026-05-15T17:40:47.237Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JT14WTHaeFmv4y8Sv4Cn8X`</summary>

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
  "parentUuid": "f22c7705-0f0b-416b-bf8f-163c3c423227",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mLHX5S84BaRVYhXy3n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29ceae5e-1f84-42de-8a28-9788c7a950d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193hh38KKGVrgmDxEiGDoKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2916,
      "cache_read_input_tokens": 28913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2916,
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

_source line 25 · 2026-05-15T17:40:47.260Z_

<details><summary>↩ Tool result · `toolu_01JT14WTHaeFmv4y8Sv4Cn8X`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29ceae5e-1f84-42de-8a28-9788c7a950d9",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "f51fa70f-d155-4cc4-b77b-8be25284189b",
  "sourceToolAssistantUUID": "29ceae5e-1f84-42de-8a28-9788c7a950d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T17:40:47.604Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Jgip7fN2xJgorDFGhGA7ki`</summary>

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
  "parentUuid": "f51fa70f-d155-4cc4-b77b-8be25284189b",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mLHX5S84BaRVYhXy3n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11b782a1-90f8-4f2b-bdd5-2dde75820994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193hh38KKGVrgmDxEiGDoKM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2916,
      "cache_read_input_tokens": 28913,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 28913,
          "cache_creation_input_tokens": 2916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2916,
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

_source line 27 · 2026-05-15T17:40:47.622Z_

<details><summary>↩ Tool result · `toolu_01Jgip7fN2xJgorDFGhGA7ki`</summary>

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
  "parentUuid": "11b782a1-90f8-4f2b-bdd5-2dde75820994",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "40685b94-4e1c-435c-8b0d-4639a6d1607a",
  "sourceToolAssistantUUID": "11b782a1-90f8-4f2b-bdd5-2dde75820994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T17:40:50.370Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EZ2FmsAqPmDabmS13XHuLa`</summary>

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
  "parentUuid": "40685b94-4e1c-435c-8b0d-4639a6d1607a",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mLba2maQ89JER12MyQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34fc46d2-1828-46ec-ab19-5341fabbc7d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016geZHRNivwkw8oFaxkvwaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 31829,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 433
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 31829,
          "cache_creation_input_tokens": 433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 433,
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

_source line 29 · 2026-05-15T17:40:50.375Z_

<details><summary>↩ Tool result · `toolu_01EZ2FmsAqPmDabmS13XHuLa`</summary>

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
  "parentUuid": "34fc46d2-1828-46ec-ab19-5341fabbc7d3",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "c1cea1a9-d888-47a0-ab90-e9fd8cb28e61",
  "sourceToolAssistantUUID": "34fc46d2-1828-46ec-ab19-5341fabbc7d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T17:40:53.679Z_

Now let me also check the dream review report for any existing critique.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1cea1a9-d888-47a0-ab90-e9fd8cb28e61",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mLoSuXZzoHEdp3ohid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "825c6096-59ad-4cb4-9ff3-8497fd320b9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EL6BXCSbQTb2tKkRHKW4NY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 32262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2130,
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

_source line 31 · 2026-05-15T17:40:54.017Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014HNMihPmXEr5RpbtZLhSGn`</summary>

```json
{
  "pattern": "**/dream_reports/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "825c6096-59ad-4cb4-9ff3-8497fd320b9a",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mLoSuXZzoHEdp3ohid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea853a87-dcd0-4922-bed5-ba1fc0684030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EL6BXCSbQTb2tKkRHKW4NY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 32262,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2130
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 32262,
          "cache_creation_input_tokens": 2130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2130,
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

_source line 32 · 2026-05-15T17:40:54.033Z_

<details><summary>↩ Tool result · `toolu_014HNMihPmXEr5RpbtZLhSGn`</summary>

```text
artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea853a87-dcd0-4922-bed5-ba1fc0684030",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "9837dd29-3f71-43d9-93d7-d555a1f41791",
  "sourceToolAssistantUUID": "ea853a87-dcd0-4922-bed5-ba1fc0684030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T17:40:57.282Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QYY8mnDpzQRmWuNCfDgrHx`</summary>

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
  "parentUuid": "9837dd29-3f71-43d9-93d7-d555a1f41791",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mM59UMi4QdnjZ7REsC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05dc3eb5-c65a-4ab1-a2b4-84a7ec4f7824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uLhL5X9hHwQaxMsEpEWjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 34392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 203,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 34 · 2026-05-15T17:40:57.292Z_

<details><summary>↩ Tool result · `toolu_01QYY8mnDpzQRmWuNCfDgrHx`</summary>

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
  "parentUuid": "05dc3eb5-c65a-4ab1-a2b4-84a7ec4f7824",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "244b8376-8bf4-4aeb-a82a-e5b4758dbc13",
  "sourceToolAssistantUUID": "05dc3eb5-c65a-4ab1-a2b4-84a7ec4f7824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T17:40:57.797Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AaFd3CEsiKk4NBSiQgQvKq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "244b8376-8bf4-4aeb-a82a-e5b4758dbc13",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mM59UMi4QdnjZ7REsC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebc286fd-9f46-472b-99f7-a853ec3a1fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uLhL5X9hHwQaxMsEpEWjo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 34392,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 203
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 34392,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 203,
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

_source line 36 · 2026-05-15T17:40:57.805Z_

<details><summary>↩ Tool result · `toolu_01AaFd3CEsiKk4NBSiQgQvKq`</summary>

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
  "parentUuid": "ebc286fd-9f46-472b-99f7-a853ec3a1fbc",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "1dff9bde-2a36-44d9-a3e6-84c084d9bcd0",
  "sourceToolAssistantUUID": "ebc286fd-9f46-472b-99f7-a853ec3a1fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T17:41:00.360Z_

Now let me check the dream review context to see how the simulated review went.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dff9bde-2a36-44d9-a3e6-84c084d9bcd0",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mMMHaRbgg1UmzmjWBj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdf7d4fd-050b-4554-9161-7707b4e22166",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRvqHiHSGpXNnNdptvZSyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2928,
      "cache_read_input_tokens": 34595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2928,
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

_source line 38 · 2026-05-15T17:41:02.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DeoN6wRrzrgir6QaaDY7cm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdf7d4fd-050b-4554-9161-7707b4e22166",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mMMHaRbgg1UmzmjWBj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4564cdf8-af9a-4d12-aaf1-6b85a382eba7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRvqHiHSGpXNnNdptvZSyf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2928,
      "cache_read_input_tokens": 34595,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2928
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 34595,
          "cache_creation_input_tokens": 2928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2928,
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

### Tool call

_source line 39 · 2026-05-15T17:41:02.386Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CqAi5SkBYzJoXT3rcJjEFD`</summary>

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
  "parentUuid": "4564cdf8-af9a-4d12-aaf1-6b85a382eba7",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mMMHaRbgg1UmzmjWBj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62f0e372-00be-41fb-a679-9cfc7d543aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRvqHiHSGpXNnNdptvZSyf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2928,
      "cache_read_input_tokens": 34595,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2928
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 34595,
          "cache_creation_input_tokens": 2928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2928,
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

_source line 40 · 2026-05-15T17:41:02.647Z_

<details><summary>↩ Tool result · `toolu_01CqAi5SkBYzJoXT3rcJjEFD`</summary>

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
  "parentUuid": "62f0e372-00be-41fb-a679-9cfc7d543aef",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "a5df721c-0f03-43c5-a3c1-423a3c21a552",
  "sourceToolAssistantUUID": "62f0e372-00be-41fb-a679-9cfc7d543aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T17:41:02.652Z_

<details><summary>↩ Tool result · `toolu_01DeoN6wRrzrgir6QaaDY7cm`</summary>

```text
1	narrative_guidance: 'KL categorically dominates. Headline: ''Output-distribution distillation
2	  makes compensation networks obsolete for SwiGLU sparsity.'' 三线汇聚——理论（gradient coupling解释joint
3	  interaction）、 实验（KL-only vs BCE+comp gap 9+ PPL points）、实践（省256MB compensation weights
4	  + per-layer GEMV）。 所有planned实验均确认三条claims原样成立，无需调整framing。投EMNLP Efficient Methods。
5	
6	  '
7	imagined_experiments:
8	- name: Four-Condition Ablation @ 50% Sparsity
9	  plan_id: plan_001
10	  description: 'KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。 已有数据：KL-only
11	    3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。
12	
13	    '
14	  expected_results:
15	    kl_only_s42_ppl: 9.2142
16	    kl_only_s123_ppl: 9.2474
17	    kl_only_s456_ppl: 9.14
18	    kl_only_s0_ppl: 9.19
19	    kl_only_s1_ppl: 9.23
20	    kl_only_mean_ppl: 9.2
21	    kl_only_std_ppl: 0.04
22	    kl_only_model_sparsity: 0.498
23	    bce_comp_s42_ppl: 18.22
24	    bce_comp_s123_ppl: 18.91
25	    bce_comp_s456_ppl: 18.38
26	    bce_comp_s0_ppl: 18.65
27	    bce_comp_s1_ppl: 19.05
28	    bce_comp_mean_ppl: 18.64
29	    bce_comp_std_ppl: 0.33
30	    bce_comp_model_sparsity: 0.496
31	    kl_comp_s42_ppl: 9.05
32	    kl_comp_s123_ppl: 9.08
33	    kl_comp_s456_ppl: 8.92
34	    kl_comp_mean_ppl: 9.02
35	    kl_comp_std_ppl: 0.07
36	    bce_only_mean_ppl: 28.16
37	    bce_only_std_ppl: 0.17
38	    kl_only_vs_bce_comp_gap: 9.44
39	    kl_only_vs_dense_increase_pct: 50.3
40	    bce_comp_vs_dense_increase_pct: 204.6
41	    comp_benefit_for_bce_ppl: 9.52
42	    comp_benefit_for_kl_ppl: 0.18
43	  result_rationale: 'KL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint
44	    interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12），
45	    compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。 反观BCE的per-neuron
46	    factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint effects——这在50% sparsity下产生巨大误差（PPL
47	    28.2）。Compensation网络虽然能回收~40%的 质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling
48	    information。 5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。 核心结论：compensation对KL是冗余的（0.18
49	    PPL改善 vs 9.44 PPL gap），claims 1成立。
50	
51	    '
52	  tables:
53	  - name: 'Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B,
54	      50% sparsity)'
55	    columns:
56	    - Condition
57	    - Seeds
58	    - PPL (mean±std)
59	    - Δ vs Dense
60	    - Comp Benefit
61	    rows:
62	    - - Dense
63	      - '-'
64	      - '6.12'
65	      - '-'
66	      - '-'
67	    - - BCE-only
68	      - 3
69	      - 28.16±0.17
70	      - +360%
71	      - '-'
72	    - - BCE+comp
73	      - 5
74	      - 18.64±0.33
75	      - +205%
76	      - −9.52
77	    - - KL-only
78	      - 5
79	      - 9.20±0.04
80	      - +50%
81	      - '-'
82	    - - KL+comp
83	      - 3
84	      - 9.02±0.07
85	      - +47%
86	      - −0.18
87	  figures_description:
88	  - 'Box plot: 5-seed PPL distributions for KL-only vs BCE+comp，中位线、IQR和outliers，直观展示两个分布零重叠'
89	  - 'Bar chart: compensation benefit (PPL reduction) for BCE vs KL，量化compensation对两种loss的边际价值'
90	  analysis: 'KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献
91	    0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。 5-seed std=0.04证明高度可复现。Headline
92	    claim直接成立：output-distribution distillation eliminates the need for compensation
93	    networks.
94	
95	    '
96	- name: STE Baseline — Isolating Loss vs Relaxation
97	  plan_id: plan_002
98	  description: '用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。 目的：确认KL优势来自loss
99	    function而非Gumbel relaxation。
100	
101	    '
102	  expected_results:
103	    ste_kl_s42_ppl: 9.72
104	    ste_kl_s123_ppl: 9.85
105	    ste_kl_s456_ppl: 9.64
106	    ste_kl_mean_ppl: 9.74
107	    ste_kl_std_ppl: 0.09
108	    ste_kl_model_sparsity: 0.497
109	    ste_kl_vs_gumbel_kl_gap: 0.54
110	    ste_kl_vs_bce_only_gap: 18.42
111	    gumbel_contribution_pct: 2.8
112	  result_rationale: 'STE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的
113	    smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在 decision
114	    boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16）， 说明KL-BCE的18.96
115	    point gap中97%以上来自loss function的gradient coupling property， Gumbel relaxation仅贡献~3%的marginal
116	    improvement。这直接排除了reviewer concern "Gumbel-sigmoid relaxation, not KL, explains
117	    gains"。
118	
119	    '
120	  tables:
121	  - name: 'Table 2: Relaxation Method Ablation'
122	    columns:
123	    - Condition
124	    - Relaxation
125	    - Loss
126	    - PPL (mean±std)
127	    rows:
128	    - - Gumbel+KL (ours)
129	      - Gumbel-sigmoid
130	      - KL
131	      - 9.20±0.04
132	    - - STE+KL
133	      - Straight-Through
134	      - KL
135	      - 9.74±0.09
136	    - - Gumbel+BCE
137	      - Gumbel-sigmoid
138	      - BCE
139	      - 28.16±0.17
140	  figures_description:
141	  - 'Attribution bar chart: 将KL-BCE总gap分解为loss contribution (97.2%) vs relaxation
142	    contribution (2.8%)'
143	  analysis: 'STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是 锦上添花的minor
144	    optimization trick。这为理论narrative提供clean experimental support， 且预防了reviewer的alternative
145	    explanation attack。
146	
147	    '
148	- name: Iso-Compute BCE vs KL
149	  plan_id: plan_003
150	  description: 'KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。 给BCE同等total
151	    FLOPs预算（3.2x steps），排除compute advantage。3 seeds。
152	
153	    '
154	  expected_results:
155	    kl_steps: 1000
156	    kl_flops_per_step_ratio: 3.2
157	    kl_total_flops_ratio: 3200
158	    bce_standard_steps: 1000
159	    bce_extended_steps: 3200
160	    bce_extended_total_flops_ratio: 3200
161	    bce_extended_s42_ppl: 25.28
162	    bce_extended_s123_ppl: 25.83
163	    bce_extended_s456_ppl: 25.12
164	    bce_extended_mean_ppl: 25.41
165	    bce_extended_std_ppl: 0.31
166	    bce_standard_mean_ppl: 28.16
167	    improvement_from_extended_training: 2.75
168	    remaining_gap_vs_kl: 16.21
169	    training_wall_clock_kl_hours: 4.2
170	    training_wall_clock_bce_extended_hours: 4.1
171	  result_rationale: 'BCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ''(s_j)仅依赖neuron j自身的target，
172	    更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的 （忽略joint interaction）。因此extended
173	    training让BCE-only从28.16降到25.41（降2.75）， 收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21
174	    points。 这证明KL的优势是information-theoretic的（loss function的gradient structure差异）， 不是compute-driven的，直接回应reviewer
175	    concern "KL wins only because more compute"。
176	
177	    '
178	  tables:
179	  - name: 'Table 3: Iso-Compute Comparison'
180	    columns:
181	    - Condition
182	    - Steps
183	    - Total FLOPs (relative)
184	    - PPL (mean±std)
185	    rows:
186	    - - KL (Gumbel)
187	      - 1000
188	      - 3200x
189	      - 9.20±0.04
190	    - - BCE (standard)
191	      - 1000
192	      - 1000x
193	      - 28.16±0.17
194	    - - BCE (extended)
195	      - 3200
196	      - 3200x
197	      - 25.41±0.31
198	  figures_description:
199	  - 'BCE training curve (PPL vs steps): 展示extended training的diminishing returns，标注KL水平线作为reference'
200	  - 'FLOPs-PPL scatter: 三个condition在iso-FLOPs平面上的位置'
201	  analysis: '即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21）
202	    几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。
203	
204	    '
205	- name: SPON Reimplementation & Validation
206	  plan_id: plan_004
207	  description: '在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training），
208	    在5个QA benchmarks上验证质量以确认实现正确性。
209	
210	    '
211	  expected_results:
212	    spon_wikitext2_ppl: 10.82
213	    spon_model_sparsity: 0.501
214	    spon_ppl_increase_vs_dense_pct: 76.9
215	    spon_arc_c: 51.2
216	    spon_arc_e: 74.5
217	    spon_boolq: 79.3
218	    spon_piqa: 78.1
219	    spon_winogrande: 74.8
220	    spon_params_bytes: 1048576
221	    spon_training_time_minutes: 12
222	    dense_arc_c: 55.2
223	    dense_arc_e: 79.4
224	    dense_boolq: 83.1
225	    dense_piqa: 81.3
226	    dense_winogrande: 77.8
227	  result_rationale: 'SPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case
228	    下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理 per-input variation
229	    Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82， 是一个meaningful but limited的improvement。QA
230	    benchmarks上drops 3-6%符合PPL改善幅度。 SPON的主要价值不在于standalone quality，而是作为composition实验的building
231	    block—— 它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input
232	    variation） 应当可加。
233	
234	    '
235	  tables:
236	  - name: 'Table 4: SPON Validation on QA Benchmarks'
237	    columns:
238	    - Benchmark
239	    - Dense
240	    - SPON
241	    - Δ (abs)
242	    rows:
243	    - - ARC-c
244	      - 55.2
245	      - 51.2
246	      - −4.0
247	    - - ARC-e
248	      - 79.4
249	      - 74.5
250	      - −4.9
251	    - - BoolQ
252	      - 83.1
253	      - 79.3
254	      - −3.8
255	    - - PIQA
256	      - 81.3
257	      - 78.1
258	      - −3.2
259	    - - WinoGrande
260	      - 77.8
261	      - 74.8
262	      - −3.0
263	  figures_description:
264	  - 'Radar chart: Dense vs SPON在5个QA tasks上的profile，验证SPON实现没有catastrophic failure'
265	  analysis: 'SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。 PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim
266	    2 的additivity实验提供可靠的static correction baseline。
267	
268	    '
269	- name: SPON + KL Predictor Composition
270	  plan_id: plan_005
271	  description: '同时应用SPON bias correction和KL contextual prediction。 测试output-space
272	    linearity（interaction residual）和per-layer orthogonality。3 seeds。
273	
274	    '
275	  expected_results:
276	    spon_kl_s42_ppl: 7.95
277	    spon_kl_s123_ppl: 8.12
278	    spon_kl_s456_ppl: 7.88
279	    spon_kl_mean_ppl: 7.98
280	    spon_kl_std_ppl: 0.1
281	    spon_kl_model_sparsity: 0.499
282	    spon_kl_ppl_increase_vs_dense_pct: 30.4
283	    spon_alone_ppl_recovery: 1.68
284	    kl_alone_ppl_recovery: 3.3
285	    combined_ppl_recovery: 4.52
286	    predicted_additive_recovery: 4.98
287	    interaction_residual_pct: 6.8
288	    logit_interaction_residual_l2_norm: 0.042
289	    logit_spon_correction_l2_norm: 0.38
290	    logit_kl_correction_l2_norm: 0.61
291	    logit_interaction_ratio_pct: 6.8
292	    mean_cosine_similarity_spon_kl: 0.11
293	    max_cosine_similarity_spon_kl: 0.23
294	    layers_with_cosine_gt_0_2: 4
295	  result_rationale: 'SPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x)
296	    = Δh(x) - E[Δh] （per-input residual variation）。两者在correction space中近似正交——SPON的correction是
297	    constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合 c = c_s + c_θ(x)的interaction
298	    residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98， 接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的
299	    error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift 和per-input
300	    variation方向部分对齐（如early layers的token-independent patterns）， 但这不影响整体additivity。Claim
301	    2（modular decomposition）直接成立。
302	
303	    '
304	  tables:
305	  - name: 'Table 5: Composition Additivity Analysis'
306	    columns:
307	    - Component
308	    - PPL Recovery (from TEAL baseline)
309	    - Predicted Additive
310	    - Actual
311	    - Interaction Residual
312	    rows:
313	    - - SPON only
314	      - 1.68
315	      - '-'
316	      - '-'
317	      - '-'
318	    - - KL only
319	      - 3.3
320	      - '-'
321	      - '-'
322	      - '-'
323	    - - SPON+KL
324	      - '-'
325	      - 4.98
326	      - 4.52
327	      - 9.2%
328	  - name: 'Table 5b: Per-Layer Cosine Similarity Statistics'
329	    columns:
330	    - Statistic
331	    - Value
332	    rows:
333	    - - Mean cosine
334	      - 0.11
335	    - - Median cosine
336	      - 0.08
337	    - - Max cosine
338	      - 0.23
339	    - - Layers > 0.2
340	      - 4/32
341	  figures_description:
342	  - 'Scatter plot: per-layer SPON correction magnitude vs KL correction magnitude，color
343	    by cosine similarity，展示orthogonality'
344	  - 'Logit-space decomposition visualization: ||Δ(s+c)||, ||Δ(s)||, ||Δ(c)||, ||residual||
345	    的bar chart，直观展示linearity'
346	  - 'PPL waterfall chart: Dense → TEAL → +SPON → +KL → SPON+KL，展示每个component的incremental
347	    contribution'
348	  analysis: 'SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值， per-layer
349	    cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition experimentally
350	    validated。两种correction address不同error sources的理论预测被定量确认。
351	
352	    '
353	- name: Training-Free Baselines (TEAL, WINA, R-Sparse)
354	  plan_id: plan_006
355	  description: '三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。 建立三级hierarchy:
356	    training-free < static-learned < contextual-learned。
357	
358	    '
359	  expected_results:
360	    teal_wikitext2_ppl: 12.48
361	    wina_wikitext2_ppl: 14.76
362	    rsparse_wikitext2_ppl: 13.62
363	    teal_model_sparsity: 0.5
364	    wina_model_sparsity: 0.5
365	    rsparse_model_sparsity: 0.5
366	    teal_ppl_increase_vs_dense_pct: 103.9
367	    wina_ppl_increase_vs_dense_pct: 141.3
368	    rsparse_ppl_increase_vs_dense_pct: 122.6
369	  result_rationale: 'TEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为
370	    magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但 实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed
371	    scoring虽然 考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的
372	    correlation比standard FFN更弱（gate和up projection交互），因此表现最差。 所有三种方法PPL都在12-15范围，远逊于learned
373	    methods（KL-only 9.2、SPON 10.8）， 建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn
374	    per-input neuron importance patterns，只能依赖固定heuristic。
375	
376	    '
377	  tables:
378	  - name: 'Table 6: Training-Free Baseline Comparison'
379	    columns:
380	    - Method
381	    - Type
382	    - WikiText-2 PPL
383	    - Δ vs Dense
384	    rows:
385	    - - Dense
386	      - '-'
387	      - 6.12
388	      - '-'
389	    - - TEAL
390	      - Magnitude + greedy
391	      - 12.48
392	      - +104%
393	    - - R-Sparse
394	      - Rank-aware
395	      - 13.62
396	      - +123%
397	    - - WINA
398	      - Weight-informed
399	      - 14.76
400	      - +141%
401	    - - SPON
402	      - Static learned (KL)
403	      - 10.82
404	      - +77%
405	    - - KL-only
406	      - Contextual learned (KL)
407	      - 9.2
408	      - +50%
409	  figures_description:
410	  - 'Horizontal bar chart: 所有methods按PPL排序，color-coded by method type (training-free
411	    / static / contextual)，清晰展示三级hierarchy'
412	  analysis: '三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned
413	    (9.2)。 每级提升对应information quality的提高：heuristic → average-case calibration → per-input
414	    optimization。 TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies
415	    learned approach的overhead。
416	
417	    '
418	- name: Full Benchmark Suite + Latency Profiling
419	  plan_id: plan_007
420	  description: '所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的
421	    完整evaluation。构建efficiency-accuracy Pareto frontier。
422	
423	    '
424	  expected_results:
425	    dense_wikitext2_ppl: 6.12
426	    teal_wikitext2_ppl: 12.48
427	    wina_wikitext2_ppl: 14.76
428	    rsparse_wikitext2_ppl: 13.62
429	    spon_wikitext2_ppl: 10.82
430	    bce_only_wikitext2_ppl: 28.16
431	    bce_comp_wikitext2_ppl: 18.64
432	    kl_only_wikitext2_ppl: 9.2
433	    kl_comp_wikitext2_ppl: 9.02
434	    spon_kl_wikitext2_ppl: 7.98
435	    dense_c4_ppl: 7.85
436	    teal_c4_ppl: 15.12
437	    wina_c4_ppl: 17.88
438	    rsparse_c4_ppl: 16.31
439	    spon_c4_ppl: 13.24
440	    bce_only_c4_ppl: 33.42
441	    bce_comp_c4_ppl: 22.15
442	    kl_only_c4_ppl: 11.38
443	    kl_comp_c4_ppl: 11.12
444	    spon_kl_c4_ppl: 9.81
445	    dense_arc_c: 55.2
446	    teal_arc_c: 48.1
447	    wina_arc_c: 46.3
448	    rsparse_arc_c: 47.2
449	    spon_arc_c: 51.2
450	    bce_comp_arc_c: 44.8
451	    kl_only_arc_c: 54.3
452	    spon_kl_arc_c: 54.8
453	    dense_winogrande: 77.8
454	    teal_winogrande: 72.4
455	    wina_winogrande: 70.8
456	    rsparse_winogrande: 71.5
457	    spon_winogrande: 74.8
458	    bce_comp_winogrande: 68.3
459	    kl_only_winogrande: 76.9
460	    spon_kl_winogrande: 77.2
461	    dense_mmlu: 65.8
462	    teal_mmlu: 58.2
463	    wina_mmlu: 56.4
464	    rsparse_mmlu: 57.1
465	    spon_mmlu: 60.3
466	    bce_comp_mmlu: 54.9
467	    kl_only_mmlu: 65.0
468	    spon_kl_mmlu: 65.4
469	    dense_gsm8k: 53.8
470	    teal_gsm8k: 44.2
471	    wina_gsm8k: 41.8
472	    rsparse_gsm8k: 43.1
473	    spon_gsm8k: 46.5
474	    bce_comp_gsm8k: 39.7
475	    kl_only_gsm8k: 52.8
476	    spon_kl_gsm8k: 53.2
477	    dense_humaneval: 32.9
478	    teal_humaneval: 26.2
479	    wina_humaneval: 24.4
480	    rsparse_humaneval: 25.6
481	    spon_humaneval: 28.1
482	    bce_comp_humaneval: 23.8
483	    kl_only_humaneval: 32.3
484	    spon_kl_humaneval: 32.5
485	    kl_only_avg_acc_drop_pct: 1.3
486	    spon_kl_avg_acc_drop_pct: 0.7
487	    bce_comp_avg_acc_drop_pct: 12.8
488	    dense_latency_ms: 16.8
489	    teal_latency_ms: 11.2
490	    spon_latency_ms: 10.9
491	    bce_only_latency_ms: 12.0
492	    bce_comp_latency_ms: 13.8
493	    kl_only_latency_ms: 12.0
494	    kl_comp_latency_ms: 13.8
495	    spon_kl_latency_ms: 12.1
496	    predictor_params_mb: 24
497	    compensation_params_mb: 256
498	    spon_params_mb: 1
499	    kl_only_speedup_vs_dense_pct: 28.6
500	    bce_comp_speedup_vs_dense_pct: 17.9
501	    kl_only_speedup_vs_bce_comp_pct: 13.0
502	  result_rationale: 'Downstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上
503	    接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching， 保留了token-level的prediction
504	    quality，而downstream tasks本质上都依赖model的next-token prediction能力。BCE+comp虽然有compensation，但其PPL
505	    (18.64)反映的distribution mismatch 在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop
506	    26-28%），因为 这些任务对error compounding更敏感。 Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要
507	    compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto
508	    frontier上dominates BCE+comp——更快、更好、更小。
509	
510	    '
511	  tables:
512	  - name: 'Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)'
513	    columns:
514	    - Method
515	    - Wiki PPL↓
516	    - C4 PPL↓
517	    - ARC-c↑
518	    - WinoG↑
519	    - MMLU↑
520	    - GSM8K↑
521	    - HumanE↑
522	    - Avg Δ↓
523	    rows:
524	    - - Dense
525	      - 6.12
526	      - 7.85
527	      - 55.2
528	      - 77.8
529	      - 65.8
530	      - 53.8
531	      - 32.9
532	      - —
533	    - - TEAL
534	      - 12.48
535	      - 15.12
536	      - 48.1
537	      - 72.4
538	      - 58.2
539	      - 44.2
540	      - 26.2
541	      - −7.8
542	    - - WINA
543	      - 14.76
544	      - 17.88
545	      - 46.3
546	      - 70.8
547	      - 56.4
548	      - 41.8
549	      - 24.4
550	      - −9.9
551	    - - R-Sparse
552	      - 13.62
553	      - 16.31
554	      - 47.2
555	      - 71.5
556	      - 57.1
557	      - 43.1
558	      - 25.6
559	      - −8.8
560	    - - SPON
561	      - 10.82
562	      - 13.24
563	      - 51.2
564	      - 74.8
565	      - 60.3
566	      - 46.5
567	      - 28.1
568	      - −5.3
569	    - - BCE+comp
570	      - 18.64
571	      - 22.15
572	      - 44.8
573	      - 68.3
574	      - 54.9
575	      - 39.7
576	      - 23.8
577	      - −12.8
578	    - - KL-only
579	      - 9.2
580	      - 11.38
581	      - 54.3
582	      - 76.9
583	      - 65.0
584	      - 52.8
585	      - 32.3
586	      - −1.3
587	    - - SPON+KL
588	      - 7.98
589	      - 9.81
590	      - 54.8
591	      - 77.2
592	      - 65.4
593	      - 53.2
594	      - 32.5
595	      - −0.7
596	  - name: 'Table 8: Inference Efficiency Comparison'
597	    columns:
598	    - Method
599	    - Latency (ms/tok)
600	    - Speedup vs Dense
601	    - Extra Params (MB)
602	    - PPL
603	    rows:
604	    - - Dense
605	      - 16.8
606	      - 1.00×
607	      - 0
608	      - 6.12
609	    - - TEAL
610	      - 11.2
611	      - 1.50×
612	      - 0
613	      - 12.48
614	    - - SPON
615	      - 10.9
616	      - 1.54×
617	      - 1
618	      - 10.82
619	    - - KL-only
620	      - 12.0
621	      - 1.40×
622	      - 24
623	      - 9.2
624	    - - BCE+comp
625	      - 13.8
626	      - 1.22×
627	      - 280
628	      - 18.64
629	    - - SPON+KL
630	      - 12.1
631	      - 1.39×
632	      - 25
633	      - 7.98
634	  figures_description:
635	  - 'Pareto frontier plot: x=latency (ms/tok), y=WikiText-2 PPL, 所有conditions标注。KL-only和SPON+KL在frontier上，BCE+comp
636	    dominated'
637	  - 'Grouped bar chart: 5个downstream tasks，每个task所有methods并排，直观展示KL-only接近dense而BCE+comp远逊'
638	  - 'Taxonomy heatmap: 2D table (granularity × coupling) 填入PPL值，our cell (contextual
639	    × KL) 最优'
640	  analysis: 'KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20
641	    vs 18.64）， 更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains
642	    transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。 SPON+KL作为our
643	    best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。 Taxonomy table的每个cell都有实验数据支撑。
644	
645	    '
646	- name: 7-Level Sparsity Sweep — Quadratic Scaling Test
647	  plan_id: plan_008
648	  description: '在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed），
649	    测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。
650	
651	    '
652	  expected_results:
653	    sparsity_levels:
654	    - 0.3
655	    - 0.35
656	    - 0.4
657	    - 0.45
658	    - 0.5
659	    - 0.55
660	    - 0.6
661	    kl_ppls:
662	    - 7.05
663	    - 7.42
664	    - 7.98
665	    - 8.51
666	    - 9.2
667	    - 10.82
668	    - 13.15
669	    bce_ppls:
670	    - 14.55
671	    - 17.82
672	    - 19.98
673	    - 24.71
674	    - 28.2
675	    - 33.62
676	    - 42.65
677	    kl_bce_deltas:
678	    - 7.5
679	    - 10.4
680	    - 12.0
681	    - 16.2
682	    - 19.0
683	    - 22.8
684	    - 29.5
685	    s2_fit_coefficient_a: 79.2
686	    s2_fit_r_squared: 0.97
687	    s2_plus_linear_fit_r_squared: 0.99
688	    taylor_accuracy_pct:
689	    - 96.8
690	    - 95.4
691	    - 94.1
692	    - 92.5
693	    - 89.8
694	    - 85.6
695	    - 80.2
696	    predicted_deltas_s2_only:
697	    - 7.13
698	    - 9.7
699	    - 12.67
700	    - 16.03
701	    - 19.8
702	    - 23.96
703	    - 28.51
704	  result_rationale: 'KL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时，
705	    每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为 O(s²D²)。BCE的factorized
706	    gradient完全忽略这些interactions。因此KL-BCE quality delta 应当scale as s²（leading term来自pairwise
707	    neuron interaction）。 实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%）
708	    下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%） accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent
709	    with the theory（Taylor展开在远离展开点时精度下降）。 加入linear term后R²=0.99，说明residual主要是one lower-order
710	    correction。 Claim 3（quadratic scaling）定量验证通过。
711	
712	    '
713	  tables:
714	  - name: 'Table 9: Sparsity Sweep Results'
715	    columns:
716	    - Sparsity s
717	    - s²
718	    - KL PPL
719	    - BCE PPL
720	    - Δ (BCE−KL)
721	    - Predicted Δ (as²)
722	    - Taylor Acc %
723	    rows:
724	    - - 0.3
725	      - 0.09
726	      - 7.05
727	      - 14.55
728	      - 7.5
729	      - 7.13
730	      - 96.8
731	    - - 0.35
732	      - 0.123
733	      - 7.42
734	      - 17.82
735	      - 10.4
736	      - 9.7
737	      - 95.4
738	    - - 0.4
739	      - 0.16
740	      - 7.98
741	      - 19.98
742	      - 12.0
743	      - 12.67
744	      - 94.1
745	    - - 0.45
746	      - 0.203
747	      - 8.51
748	      - 24.71
749	      - 16.2
750	      - 16.03
751	      - 92.5
752	    - - 0.5
753	      - 0.25
754	      - 9.2
755	      - 28.2
756	      - 19.0
757	      - 19.8
758	      - 89.8
759	    - - 0.55
760	      - 0.303
761	      - 10.82
762	      - 33.62
763	      - 22.8
764	      - 23.96
765	      - 85.6
766	    - - 0.6
767	      - 0.36
768	      - 13.15
769	      - 42.65
770	      - 29.5
771	      - 28.51
772	      - 80.2
773	  - name: 'Table 9b: Scaling Fit Statistics'
774	    columns:
775	    - Model
776	    - R²
777	    - Parameters
778	    rows:
779	    - - Δ = as²
780	      - 0.97
781	      - a=79.2
782	    - - Δ = as² + bs
783	      - 0.99
784	      - a=68.1, b=5.8
785	    - - Δ = as² + bs + c
786	      - 0.99
787	      - a=65.3, b=7.2, c=−0.4
788	  figures_description:
789	  - 'Scatter + fitted curve: x=s², y=KL-BCE delta, 实测点+quadratic fit曲线+95% CI band。R²=0.97标注'
790	  - 'Dual-axis line plot: x=sparsity, 左轴=KL PPL和BCE PPL（两条线），右轴=delta（bar chart），展示gap加速增长'
791	  - 'Taylor accuracy vs sparsity: 展示理论预测precision随sparsity的graceful degradation'
792	  analysis: 'KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。 Quadratic
793	    scaling意味着在高sparsity regime（>50%），KL的优势accelerates—— 这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts
794	    extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步 增强理论credibility。Claim
795	    3直接成立。
796	
797	    '
798	- name: Mistral-7B-v0.3 Cross-Architecture Validation
799	  plan_id: plan_009
800	  description: '在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上
801	    复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3
802	    seeds each。
803	
804	    '
805	  expected_results:
806	    mistral_dense_wikitext2_ppl: 5.48
807	    mistral_dense_arc_c: 58.1
808	    mistral_dense_mmlu: 62.8
809	    mistral_kl_s42_ppl: 8.12
810	    mistral_kl_s123_ppl: 8.35
811	    mistral_kl_s456_ppl: 8.18
812	    mistral_kl_mean_ppl: 8.22
813	    mistral_kl_std_ppl: 0.1
814	    mistral_kl_model_sparsity: 0.498
815	    mistral_kl_ppl_increase_vs_dense_pct: 50.0
816	    mistral_kl_arc_c: 56.4
817	    mistral_kl_mmlu: 61.3
818	    mistral_bce_comp_s42_ppl: 12.81
819	    mistral_bce_comp_s123_ppl: 13.24
820	    mistral_bce_comp_s456_ppl: 12.53
821	    mistral_bce_comp_mean_ppl: 12.86
822	    mistral_bce_comp_std_ppl: 0.29
823	    mistral_bce_comp_model_sparsity: 0.497
824	    mistral_bce_comp_arc_c: 50.8
825	    mistral_bce_comp_mmlu: 55.9
826	    mistral_kl_vs_bce_comp_ppl_gap: 4.64
827	    mistral_kl_vs_bce_comp_ppl_gap_pct: 36.1
828	  result_rationale: 'Mistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但
829	    attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling
830	    property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity 在hidden
831	    states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。 PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64
832	    vs 9.44）较小是因为 Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。
833	    Sliding window attention可能使某些layers的neuron importance更localized，略微 降低BCE+comp的absolute
834	    PPL（12.86 vs Llama的18.64），但不改变KL dominance。
835	
836	    '
837	  tables:
838	  - name: 'Table 10: Mistral-7B-v0.3 Cross-Architecture Validation'
839	    columns:
840	    - Condition
841	    - Wiki PPL↓
842	    - ARC-c↑
843	    - MMLU↑
844	    rows:
845	    - - Dense
846	      - 5.48
847	      - 58.1
848	      - 62.8
849	    - - KL-only
850	      - 8.22±0.10
851	      - 56.4
852	      - 61.3
853	    - - BCE+comp
854	      - 12.86±0.29
855	      - 50.8
856	      - 55.9
857	    - - Gap (KL vs BCE+comp)
858	      - −4.64
859	      - '+5.6'
860	      - '+5.4'
861	  - name: 'Table 10b: Cross-Architecture Consistency'
862	    columns:
863	    - Metric
864	    - Llama 3.1 8B
865	    - Mistral-7B-v0.3
866	    rows:
867	    - - KL PPL increase vs dense
868	      - 50.3%
869	      - 50.0%
870	    - - KL vs BCE+comp gap (PPL)
871	      - 9.44
872	      - 4.64
873	    - - KL vs BCE+comp gap (%)
874	      - 50.6%
875	      - 36.1%
876	  figures_description:
877	  - 'Side-by-side bar chart: Llama和Mistral的KL-only vs BCE+comp PPL，展示cross-architecture
878	    consistency'
879	  analysis: 'Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap
880	    36%。 KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function 的universal
881	    property而非architecture-specific artifact。排除reviewer concern "Single model / limited
882	    generalization"。
883	
884	    '
885	- name: LongBench Long-Context Evaluation
886	  plan_id: plan_010
887	  description: 'LongBench English subset（4K-32K tokens），所有conditions。 Per-task-type
888	    breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。
889	
890	    '
891	  expected_results:
892	    dense_longbench_avg: 43.5
893	    teal_longbench_avg: 35.4
894	    wina_longbench_avg: 33.8
895	    rsparse_longbench_avg: 34.6
896	    spon_longbench_avg: 39.8
897	    bce_comp_longbench_avg: 32.1
898	    kl_only_longbench_avg: 42.1
899	    spon_kl_longbench_avg: 42.8
900	    kl_single_doc_qa: 44.8
901	    kl_multi_doc_qa: 38.2
902	    kl_summarization: 42.5
903	    kl_few_shot: 47.1
904	    kl_code: 38.0
905	    bce_comp_single_doc_qa: 35.2
906	    bce_comp_multi_doc_qa: 28.4
907	    bce_comp_summarization: 33.8
908	    bce_comp_few_shot: 34.6
909	    bce_comp_code: 28.5
910	    dense_single_doc_qa: 46.2
911	    dense_multi_doc_qa: 39.5
912	    dense_summarization: 43.8
913	    dense_few_shot: 48.3
914	    dense_code: 39.6
915	    kl_only_avg_drop_vs_dense: 1.4
916	    bce_comp_avg_drop_vs_dense: 11.4
917	    kl_worst_task_type: multi-doc QA
918	    kl_worst_task_drop: 3.3
919	  result_rationale: '长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution
920	    matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor 看到的是per-token
921	    hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg） 与short-context
922	    evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document reasoning），因此KL-only在此处drop最大（3.3
923	    points）。BCE+comp在长序列下degradation 更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates
924	    without compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5，
925	    进一步确认composition在长序列下仍然有效。
926	
927	    '
928	  tables:
929	  - name: 'Table 11: LongBench Per-Task-Type Breakdown'
930	    columns:
931	    - Task Type
932	    - Dense
933	    - TEAL
934	    - SPON
935	    - BCE+comp
936	    - KL-only
937	    - SPON+KL
938	    rows:
939	    - - Single-doc QA
940	      - 46.2
941	      - 38.1
942	      - 42.0
943	      - 35.2
944	      - 44.8
945	      - 45.3
946	    - - Multi-doc QA
947	      - 39.5
948	      - 31.2
949	      - 36.1
950	      - 28.4
951	      - 38.2
952	      - 38.8
953	    - - Summarization
954	      - 43.8
955	      - 35.8
956	      - 40.2
957	      - 33.8
958	      - 42.5
959	      - 43.1
960	    - - Few-shot
961	      - 48.3
962	      - 39.5
963	      - 44.3
964	      - 34.6
965	      - 47.1
966	      - 47.8
967	    - - Code
968	      - 39.6
969	      - 32.4
970	      - 36.5
971	      - 28.5
972	      - 38.0
973	      - 38.9
974	    - - '**Average**'
975	      - '**43.5**'
976	      - '**35.4**'
977	      - '**39.8**'
978	      - '**32.1**'
979	      - '**42.1**'
980	      - '**42.8**'
981	  figures_description:
982	  - 'Radar chart: 5个task types，Dense/KL-only/BCE+comp/SPON+KL四条线，展示KL-only profile近似dense'
983	  - 'Heatmap: methods × task types，color by score，直观展示BCE+comp在所有task types上consistently差'
984	  analysis: 'LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4），
985	    无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%），
986	    可能因为compensation网络对error accumulation的correction在长序列下saturate。 增强了EMNLP venue
987	    fit（NLP-specific long-context evaluation）。
988	
989	    '
990	- name: MT-Bench Multi-Turn Instruction Following
991	  plan_id: plan_011
992	  description: 'MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following
993	    quality的影响。
994	
995	    '
996	  expected_results:
997	    dense_mtbench_avg: 7.21
998	    teal_mtbench_avg: 6.18
999	    spon_mtbench_avg: 6.78
1000	    bce_comp_mtbench_avg: 6.42
1001	    kl_only_mtbench_avg: 7.05
1002	    spon_kl_mtbench_avg: 7.12
1003	    kl_writing: 7.35
1004	    kl_roleplay: 7.15
1005	    kl_reasoning: 6.65
1006	    kl_math: 6.55
1007	    kl_coding: 6.85
1008	    kl_extraction: 7.45
1009	    kl_stem: 7.1
1010	    kl_humanities: 7.3
1011	    bce_comp_writing: 6.8
1012	    bce_comp_reasoning: 5.85
1013	    bce_comp_math: 5.65
1014	    bce_comp_coding: 5.9
1015	  result_rationale: 'MT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。
1016	    KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内）， 说明KL的output
1017	    distribution matching直接保留了instruction following能力。 Math和reasoning categories drop略大（KL-only
1018	    6.55/6.65 vs dense ~6.8/6.85），因为 这些tasks需要precise multi-step reasoning，对任何distribution
1019	    shift更敏感。 BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为
1020	    BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上
1021	    产生compounding errors，compensation无法fully recover。
1022	
1023	    '
1024	  tables:
1025	  - name: 'Table 12: MT-Bench Results'
1026	    columns:
1027	    - Method
1028	    - Avg Score
1029	    - Writing
1030	    - Reasoning
1031	    - Math
1032	    - Coding
1033	    rows:
1034	    - - Dense
1035	      - 7.21
1036	      - 7.5
1037	      - 6.85
1038	      - 6.8
1039	      - 7.1
1040	    - - TEAL
1041	      - 6.18
1042	      - 6.45
1043	      - 5.6
1044	      - 5.4
1045	      - 5.8
1046	    - - SPON
1047	      - 6.78
1048	      - 7.1
1049	      - 6.35
1050	      - 6.15
1051	      - 6.55
1052	    - - BCE+comp
1053	      - 6.42
1054	      - 6.8
1055	      - 5.85
1056	      - 5.65
1057	      - 5.9
1058	    - - KL-only
1059	      - 7.05
1060	      - 7.35
1061	      - 6.65
1062	      - 6.55
1063	      - 6.85
1064	    - - SPON+KL
1065	      - 7.12
1066	      - 7.4
1067	      - 6.75
1068	      - 6.65
1069	      - 6.95
1070	  figures_description:
1071	  - 'Grouped bar chart per category: Dense vs KL-only vs BCE+comp，8个categories并排'
1072	  analysis: 'MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异 KL-only
1073	    vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上 severe degradation（-1.15/-1.00
1074	    vs dense），而KL-only仅-0.25/-0.20。 Strengthens EMNLP NLP evaluation story。
1075	
1076	    '
1077	- name: RULER Synthetic Long-Context Diagnostics
1078	  plan_id: plan_012
1079	  description: 'RULER synthetic evaluation at 4K and 16K context，3 representative
1080	    task types (needle-in-a-haystack, multi-key retrieval, variable tracking)。 Fine-grained
1081	    diagnostics complementing LongBench。
1082	
1083	    '
1084	  expected_results:
1085	    dense_ruler_4k_avg: 95.2
1086	    kl_only_ruler_4k_avg: 93.8
1087	    bce_comp_ruler_4k_avg: 87.4
1088	    spon_kl_ruler_4k_avg: 94.5
1089	    dense_ruler_16k_avg: 88.5
1090	    kl_only_ruler_16k_avg: 86.1
1091	    bce_comp_ruler_16k_avg: 78.3
1092	    spon_kl_ruler_16k_avg: 87.2
1093	    kl_needle_4k: 98.0
1094	    kl_needle_16k: 94.5
1095	    kl_multikey_4k: 91.2
1096	    kl_multikey_16k: 82.4
1097	    kl_vartrack_4k: 92.1
1098	    kl_vartrack_16k: 81.3
1099	    bce_comp_needle_4k: 94.5
1100	    bce_comp_needle_16k: 86.2
1101	    bce_comp_multikey_4k: 83.8
1102	    bce_comp_multikey_16k: 72.1
1103	    bce_comp_vartrack_4k: 83.9
1104	    bce_comp_vartrack_16k: 76.5
1105	    kl_only_4k_to_16k_drop: 7.7
1106	    bce_comp_4k_to_16k_drop: 9.1
1107	    dense_4k_to_16k_drop: 6.7
1108	  result_rationale: 'RULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability
1109	    (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2）， 在16K下gracefully
1110	    degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)， 说明KL predictor不会随context
1111	    length引入额外的degradation。BCE+comp的4K→16K drop更大 (9.1)，在multi-key retrieval（需要同时attend
1112	    to多个scattered positions）和variable tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks
1113	    对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。 Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。
1114	
1115	    '
1116	  tables:
1117	  - name: 'Table 13: RULER Synthetic Evaluation'
1118	    columns:
1119	    - Task
1120	    - Context
1121	    - Dense
1122	    - KL-only
1123	    - BCE+comp
1124	    - SPON+KL
1125	    rows:
1126	    - - Needle
1127	      - 4K
1128	      - 99.2
1129	      - 98.0
1130	      - 94.5
1131	      - 98.5
1132	    - - Needle
1133	      - 16K
1134	      - 96.8
1135	      - 94.5
1136	      - 86.2
1137	      - 95.8
1138	    - - Multi-key
1139	      - 4K
1140	      - 93.5
1141	      - 91.2
1142	      - 83.8
1143	      - 92.4
1144	    - - Multi-key
1145	      - 16K
1146	      - 84.1
1147	      - 82.4
1148	      - 72.1
1149	      - 83.5
1150	    - - Var-track
1151	      - 4K
1152	      - 92.8
1153	      - 92.1
1154	      - 83.9
1155	      - 92.5
1156	    - - Var-track
1157	      - 16K
1158	      - 84.5
1159	      - 81.3
1160	      - 76.5
1161	      - 83.2
1162	    - - '**Average**'
1163	      - '**4K**'
1164	      - '**95.2**'
1165	      - '**93.8**'
1166	      - '**87.4**'
1167	      - '**94.5**'
1168	    - - '**Average**'
1169	      - '**16K**'
1170	      - '**88.5**'
1171	      - '**86.1**'
1172	      - '**78.3**'
1173	      - '**87.2**'
1174	  figures_description:
1175	  - 'Line plot: x=context length (4K, 16K), y=RULER avg accuracy, 每个method一条线，展示degradation
1176	    rate'
1177	  - 'Heatmap: task × method × context length，诊断哪些capabilities被sparsity影响最大'
1178	  analysis: RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致
1179	    (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval 是differentiation最大的task（KL
1180	    82.4 vs BCE+comp 72.1 at 16K），这与理论一致—— multi-key需要FFN准确处理多个simultaneously relevant
1181	    positions，joint neuron interaction quality直接影响结果。
1182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4564cdf8-af9a-4d12-aaf1-6b85a382eba7",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "e3ad441c-f1b5-461a-a8ba-7d3de0e4d5c1",
  "sourceToolAssistantUUID": "4564cdf8-af9a-4d12-aaf1-6b85a382eba7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T17:41:09.023Z_

I now have comprehensive context. Let me submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ad441c-f1b5-461a-a8ba-7d3de0e4d5c1",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mMhiQ3xs7BfuP9hrPk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "820bf19e-378c-4810-a624-361afdb82421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxQUEUJza1hMDCako4ehEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18285,
      "cache_creation_input_tokens": 18490,
      "cache_read_input_tokens": 37523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18490,
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

_source line 43 · 2026-05-15T17:41:09.519Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PPXRrzkVaxkTkqy5NuQYNp`</summary>

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
  "parentUuid": "820bf19e-378c-4810-a624-361afdb82421",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mMhiQ3xs7BfuP9hrPk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f30ffed6-0fb3-4725-9895-2645a65413ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxQUEUJza1hMDCako4ehEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18285,
      "cache_creation_input_tokens": 18490,
      "cache_read_input_tokens": 37523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18490,
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

_source line 44 · 2026-05-15T17:41:09.521Z_

<details><summary>↩ Tool result · `toolu_01PPXRrzkVaxkTkqy5NuQYNp`</summary>

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
  "parentUuid": "f30ffed6-0fb3-4725-9895-2645a65413ad",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "c68bbdda-4da1-4e63-bc50-8adc729d851e",
  "sourceToolAssistantUUID": "f30ffed6-0fb3-4725-9895-2645a65413ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T17:42:46.036Z_



Now I have all the context needed to write a rigorous R2 review focused on novelty and related work. Let me compose it.

## R2 Review: Novelty & Related Work

### Summary
This paper proposes replacing BCE loss with KL-divergence distillation for training contextual sparsity predictors in SwiGLU-based LLMs, claiming this eliminates the need for error compensation networks. The paper further proposes composing the KL-trained contextual predictor with SPON's static bias correction and argues the KL-BCE quality gap scales quadratically with sparsity. While the empirical results are strong (9.20 vs 18.64 PPL at 50% sparsity on Llama 3.1 8B), the core contribution is essentially swapping one well-known loss function for another in an existing pipeline, and the theoretical framing overstates the novelty of what is a straightforward application of knowledge distillation.

### Strengths

1. **Clear identification of an underexplored design choice**: The two-dimensional taxonomy (correction granularity x training signal coupling) is a genuinely useful organizational contribution. It clearly identifies the (per-token contextual, KL) cell as unoccupied and provides a systematic way to understand the design space. This is the paper's strongest conceptual contribution.

2. **Thorough ablation design**: The STE ablation (Table 2) isolating loss function vs. relaxation method, and the iso-compute comparison (Table 3) ruling out training budget confounds, are well-designed experiments that address the most obvious alternative explanations. This is above-average experimental rigor for this subfield.

3. **Large and consistent effect size**: The KL-BCE gap is not marginal -- 9.20 vs 28.16 (KL-only vs BCE-only) and 9.20 vs 18.64 (KL-only vs BCE+comp) are decisive. Cross-seed variance is low (std=0.04 for KL). This is not a paper where you squint at error bars.

4. **Modular decomposition is a clean contribution**: The SPON+KL composition experiment with quantified interaction residual (6.8%) and per-layer cosine similarity analysis provides actionable engineering insight. The formalization c = c_s + c_theta(x) is simple but useful.

5. **Comprehensive evaluation breadth**: PPL, 5 discriminative benchmarks, LongBench, MT-Bench, RULER, latency profiling, and Pareto frontier analysis across two model families. This is a thorough evaluation for an efficiency paper.

### Weaknesses

1. **(Major) The core novelty is thin -- this is applying standard KD to an existing pipeline.** The paper's headline contribution reduces to: "use KL divergence instead of BCE when training your sparsity predictor." KL-divergence distillation is the standard approach in knowledge distillation since Hinton et al. (2015). SPON already demonstrated KL works well for sparsity correction in this exact domain (SwiGLU activation sparsity). The paper acknowledges KL is "standard in KD" but claims it has "not been applied to train contextual sparsity predictors" -- this is a narrow novelty claim that amounts to filling in a specific cell in the authors' own taxonomy. There is no new algorithm, no new architecture, no new training procedure beyond loss function substitution. The Gumbel-sigmoid relaxation is also standard (Jang et al., 2017; Maddison et al., 2017). This feels like an ablation study elevated to a full paper.

2. **(Major) The gradient coupling argument is a restatement of known properties, not new theory.** The claim that KL gradients couple neurons through the Jacobian while BCE gradients factorize per-neuron is mathematically correct but unremarkable -- this is simply the chain rule applied to different loss functions. Any output-level loss (MSE on logits, contrastive loss, etc.) would exhibit the same coupling property. The paper does not explain why KL specifically is better than other coupled losses (e.g., MSE on logits, JS divergence, reverse KL). The O(s^2 D^2) scaling argument is hand-waving presented as theory -- there is no formal theorem, no proof, no explicit connection between the number of pairwise interactions and the PPL gap. Fitting a quadratic to 7 points and reporting R^2=0.97 is curve-fitting, not a theoretical prediction verified by experiment.

3. **(Major) MSE on logits is the obvious missing baseline.** ShadowLLM uses MSE on intermediate representations. The paper's own taxonomy has an "Intermediate (MSE)" column. MSE on output logits would also provide gradient coupling (same Jacobian pathway as KL). If MSE-on-logits performs comparably to KL, the paper's narrative collapses from "KL's distributional matching is uniquely valuable" to "any output-level loss beats BCE." This is the single most important missing experiment, and its absence is suspicious.

4. **(Major) The BCE baseline appears unreasonably weak, raising fairness concerns.** BCE-only at 28.16 PPL (vs dense 6.12) represents a 360% increase -- this is catastrophic. FastForward (the source of the BCE+compensation architecture) reports much more competitive numbers in their paper. Several possible confounds: (a) BCE uses Gumbel-sigmoid relaxation which is designed for continuous losses, not binary targets -- was BCE trained with the appropriate hard-mask STE? (b) BCE target generation (top-k by magnitude) may not be optimal -- was this the same target scheme FastForward used? (c) The training data (WikiText-103, ~100M tokens) is very small for a calibration dataset. The paper must explicitly confirm that the BCE baseline uses the same predictor architecture, same training data, same number of steps, same optimizer, and same target generation scheme as reported in the source papers, or this comparison is unfair.

5. **(Minor) Only 8 references is alarmingly sparse for a related work section.** The literature map reveals the authors are aware of at least 20 highly relevant papers (DejaVu, CATS, DIP, Sparsing Law, ProSparse, ReLU Strikes Back, TurboSparse, SparseInfer, Minitron, Amber Pruner, SVD-CSP, etc.) but the paper cites only 8. This is insufficient for a venue paper. The related work section reads as if it was written to support the authors' narrative rather than to honestly survey the field.

6. **(Minor) Scope is limited to 7-8B SwiGLU models at 50% sparsity.** Two architectures (Llama 3.1 8B, Mistral-7B-v0.3) with essentially the same FFN structure. No experiments on larger models (13B, 70B) where the efficiency-quality tradeoff is most practically relevant. No experiments on non-SwiGLU architectures (GELU, ReGLU) to test generality of the gradient coupling argument. The sparsity sweep (30-60%) is only single-seed. Claims about "making compensation networks obsolete" are strong language for evidence from two similar-sized models.

7. **(Minor) The quadratic scaling claim is post-hoc curve fitting presented as a theoretical prediction.** The paper claims to "predict" quadratic scaling and then "verify" it. But the prediction is informal (no derivation, just a counting argument about pairwise interactions), and 7 data points (single-seed) with R^2=0.97 for a monotonically increasing function is not strong evidence for a specific functional form. A power law, exponential, or other monotone functions would likely also fit well. The paper should report AIC/BIC comparisons against alternative functional forms.

### Questions for Authors

1. What is the performance of MSE on output logits as the training loss? This is the critical missing comparison. If MSE-logits achieves similar results to KL, the contribution is "use any output-level loss" rather than "use KL specifically."

2. How does the BCE baseline compare to the numbers reported in the FastForward paper? If FastForward reports significantly better BCE+compensation results on similar models, what accounts for the discrepancy? Were the same hyperparameters, target generation, and training procedure used?

3. Was BCE trained with hard-mask STE (its natural relaxation) or with Gumbel-sigmoid? If Gumbel-sigmoid was used for both, this disadvantages BCE, which operates on binary targets and does not benefit from soft relaxation the same way KL does.

4. Why does BCE-only perform so much worse than training-free methods (28.16 vs TEAL's 12.48)? A trained predictor performing 2x worse than a training-free heuristic suggests something is wrong with the BCE training setup, not that BCE is fundamentally flawed.

5. The Lagrangian sparsity enforcement and KL normalization required significant debugging (D003-D006 in decisions log). How sensitive is the KL training to these hyperparameters? What happens with naive KL training (no Lagrangian, standard reduction)?

6. For the quadratic scaling claim: what are the R^2 values for alternative functional forms (linear, power law a*s^b, exponential)? Have you tested whether the data actually distinguishes quadratic from other monotone functions?

7. Training was done on WikiText-103 (~100M tokens). How sensitive are results to calibration data domain and size?

### Missing Related Work

**Critical omissions:**
- **Deja Vu** (Liu et al., ICML 2023): The foundational work on predictor-based contextual sparsity with BCE training. Not citing this while positioning against BCE predictors is a major oversight.
- **CATS** (Lee et al., 2024): Contextual thresholding for SwiGLU sparsity without training -- a direct competitor achieving good results at 50% sparsity.
- **Minitron** (Muralidharan et al., NeurIPS 2024): Demonstrates logit-only KL outperforms intermediate matching for structured pruning distillation -- directly supports the paper's argument and should be cited as prior evidence for KL's effectiveness.
- **DIP** (Federici et al., MLSys 2025): Predictor-free dynamic pruning specifically for SwiGLU, achieving 40% speedup. Argues SwiGLU sparsity patterns are hard to predict.

**Important missing areas:**
- **Differentiable mask learning literature**: Gumbel-softmax for subset selection (Xie & Ermon, 2019), L0 regularization (Louizos et al., 2018), differentiable top-k (Cordonnier et al., 2021). The paper uses Gumbel-sigmoid without citing the foundational work or comparing to alternative differentiable relaxations.
- **Structured pruning + distillation**: Beyond Minitron, works like CoFi (Xia et al., 2022), DistilBERT (Sanh et al., 2019), and Sheared LLaMA (Xia et al., 2023) all use KL/CE distillation for structured compression. The claim "KL not applied to contextual sparsity predictors" is narrowly true but the idea of KL-guided sparsity is well-trodden.
- **Sparsing Law** (Luo et al., 2024): Directly relevant theory on SwiGLU activation sparsity scaling.
- **ReLU Strikes Back** (Mirzadeh et al., ICLR 2024) and **TurboSparse** (Song et al., 2024): Alternative approaches that achieve high sparsity by modifying activation functions. Important for positioning.
- **ProSparse** (Song et al., COLING 2025): Progressive sparsification with distribution matching.
- **SparseInfer** (Shin et al., DATE 2025) and **SVD-CSP** (Serbin et al., 2026): Training-free predictor alternatives.
- **Gradient coupling in other ML contexts**: The observation that end-to-end losses provide better gradient signal than proxy losses is well-known in multi-task learning, neural architecture search, and differentiable programming. No connection is drawn to this broader literature.

### Novelty Assessment

The paper's contribution sits at the intersection of two well-established techniques (KL distillation and learned sparsity prediction) and demonstrates their combination works better than the less principled alternative (BCE). This is useful empirical knowledge, but the novelty is limited:

1. **Loss function swap**: The core idea -- replace BCE with KL -- is a one-line change in the training loop. SPON already demonstrated KL works for sparsity in this domain. Extending from static to contextual is a natural next step, not a conceptual leap.

2. **Theoretical contribution is weak**: The gradient coupling argument is correct but trivial (it is the chain rule). The quadratic scaling claim is curve-fitting on 7 single-seed points without formal derivation. No theorem is stated or proved.

3. **Modular decomposition is the strongest novelty**: The SPON+KL composition with quantified interaction analysis is the most original contribution, but it is Claim 2, not the headline claim.

4. **Engineering value vs. scientific novelty**: The paper has clear practical value (simpler inference pipeline, no compensation network needed) but this is an engineering finding, not a scientific discovery. The result was predictable given SPON's demonstration that KL works for sparsity correction.

5. **Positioning relative to SPON**: The paper's novelty depends entirely on the distinction between "static bias correction" (SPON) and "contextual predictor" (this work). Both use KL to train parameters that improve sparse model quality. The architectural difference (bias vector vs. MLP predictor) is not matched by a conceptual difference in the training methodology.

For a top venue at 25% acceptance rate, I expect either (a) a new method with clear conceptual novelty, (b) a surprising empirical finding that changes how we think about a problem, or (c) rigorous theory that provides new understanding. This paper offers (b) in a weak sense -- the magnitude of the KL advantage is surprising -- but the direction of the result (KL > BCE for this purpose) was predictable. The missing MSE-logits baseline is the most concerning gap: if it works comparably, the paper's framing around KL-specific properties collapses.

### Preliminary Score: 3/6
### Confidence: 4/5

The score reflects: strong empirical results with thorough ablations (positive), but limited novelty in the core technique (loss function swap), weak theoretical contribution (informal argument + curve fitting), critically missing MSE-logits baseline, suspiciously weak BCE baseline, and very sparse related work section. If the MSE-logits baseline shows KL is uniquely effective (not just any output-level loss) AND the BCE baseline fairness concerns are addressed, this could move to a 4. As submitted, the novelty bar for a 25% acceptance rate venue is not met.

---

Now let me submit this review via the dream review report tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c68bbdda-4da1-4e63-bc50-8adc729d851e",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mNEFBfMC1gR8xkRp9Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d068bc16-de2f-4f9a-a78d-87726e5aaecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZHZHKj7TMfJGhnFUovRpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18964,
      "cache_read_input_tokens": 56013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18964,
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

_source line 46 · 2026-05-15T17:43:15.232Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_011w92uujPX8SxGPVQNws6DM`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "tier": "best",
  "dream_id": "dream_20260515T164925",
  "overall_score": "Weak Reject (3/6)",
  "report": "## R2 Review: Novelty & Related Work\n\n### Summary\nThis paper proposes replacing BCE loss with KL-divergence distillation for training contextual sparsity predictors in SwiGLU-based LLMs, claiming this eliminates the need for error compensation networks. The paper further proposes composing the KL-trained contextual predictor with SPON's static bias correction and argues the KL-BCE quality gap scales quadratically with sparsity. While the empirical results are strong (9.20 vs 18.64 PPL at 50% sparsity on Llama 3.1 8B), the core contribution is essentially swapping one well-known loss function for another in an existing pipeline, and the theoretical framing overstates the novelty of what is a straightforward application of knowledge distillation.\n\n### Strengths\n\n1. **Clear identification of an underexplored design choice**: The two-dimensional taxonomy (correction granularity x training signal coupling) is a genuinely useful organizational contribution. It clearly identifies the (per-token contextual, KL) cell as unoccupied and provides a systematic way to understand the design space. This is the paper's strongest conceptual contribution.\n\n2. **Thorough ablation design**: The STE ablation (Table 2) isolating loss function vs. relaxation method, and the iso-compute comparison (Table 3) ruling out training budget confounds, are well-designed experiments that address the most obvious alternative explanations. This is above-average experimental rigor for this subfield.\n\n3. **Large and consistent effect size**: The KL-BCE gap is not marginal -- 9.20 vs 28.16 (KL-only vs BCE-only) and 9.20 vs 18.64 (KL-only vs BCE+comp) are decisive. Cross-seed variance is low (std=0.04 for KL). This is not a paper where you squint at error bars.\n\n4. **Modular decomposition is a clean contribution**: The SPON+KL composition experiment with quantified interaction residual (6.8%) and per-layer cosine similarity analysis provides actionable engineering insight. The formalization c = c_s + c_theta(x) is simple but useful.\n\n5. **Comprehensive evaluation breadth**: PPL, 5 discriminative benchmarks, LongBench, MT-Bench, RULER, latency profiling, and Pareto frontier analysis across two model families. This is a thorough evaluation for an efficiency paper.\n\n### Weaknesses\n\n1. **(Major) The core novelty is thin -- this is applying standard KD to an existing pipeline.** The paper's headline contribution reduces to: \"use KL divergence instead of BCE when training your sparsity predictor.\" KL-divergence distillation is the standard approach in knowledge distillation since Hinton et al. (2015). SPON already demonstrated KL works well for sparsity correction in this exact domain (SwiGLU activation sparsity). The paper acknowledges KL is \"standard in KD\" but claims it has \"not been applied to train contextual sparsity predictors\" -- this is a narrow novelty claim that amounts to filling in a specific cell in the authors' own taxonomy. There is no new algorithm, no new architecture, no new training procedure beyond loss function substitution. The Gumbel-sigmoid relaxation is also standard (Jang et al., 2017; Maddison et al., 2017). This feels like an ablation study elevated to a full paper.\n\n2. **(Major) The gradient coupling argument is a restatement of known properties, not new theory.** The claim that KL gradients couple neurons through the Jacobian while BCE gradients factorize per-neuron is mathematically correct but unremarkable -- this is simply the chain rule applied to different loss functions. Any output-level loss (MSE on logits, contrastive loss, etc.) would exhibit the same coupling property. The paper does not explain why KL specifically is better than other coupled losses (e.g., MSE on logits, JS divergence, reverse KL). The O(s^2 D^2) scaling argument is hand-waving presented as theory -- there is no formal theorem, no proof, no explicit connection between the number of pairwise interactions and the PPL gap. Fitting a quadratic to 7 points and reporting R^2=0.97 is curve-fitting, not a theoretical prediction verified by experiment.\n\n3. **(Major) MSE on logits is the obvious missing baseline.** ShadowLLM uses MSE on intermediate representations. The paper's own taxonomy has an \"Intermediate (MSE)\" column. MSE on output logits would also provide gradient coupling (same Jacobian pathway as KL). If MSE-on-logits performs comparably to KL, the paper's narrative collapses from \"KL's distributional matching is uniquely valuable\" to \"any output-level loss beats BCE.\" This is the single most important missing experiment, and its absence is suspicious.\n\n4. **(Major) The BCE baseline appears unreasonably weak, raising fairness concerns.** BCE-only at 28.16 PPL (vs dense 6.12) represents a 360% increase -- this is catastrophic. FastForward (the source of the BCE+compensation architecture) reports much more competitive numbers in their paper. Several possible confounds: (a) BCE uses Gumbel-sigmoid relaxation which is designed for continuous losses, not binary targets -- was BCE trained with the appropriate hard-mask STE? (b) BCE target generation (top-k by magnitude) may not be optimal -- was this the same target scheme FastForward used? (c) The training data (WikiText-103, ~100M tokens) is very small for a calibration dataset. The paper must explicitly confirm that the BCE baseline uses the same predictor architecture, same training data, same number of steps, same optimizer, and same target generation scheme as reported in the source papers, or this comparison is unfair.\n\n5. **(Minor) Only 8 references is alarmingly sparse for a related work section.** The literature map reveals the authors are aware of at least 20 highly relevant papers (DejaVu, CATS, DIP, Sparsing Law, ProSparse, ReLU Strikes Back, TurboSparse, SparseInfer, Minitron, Amber Pruner, SVD-CSP, etc.) but the paper cites only 8. This is insufficient for a venue paper. The related work section reads as if it was written to support the authors' narrative rather than to honestly survey the field.\n\n6. **(Minor) Scope is limited to 7-8B SwiGLU models at 50% sparsity.** Two architectures (Llama 3.1 8B, Mistral-7B-v0.3) with essentially the same FFN structure. No experiments on larger models (13B, 70B) where the efficiency-quality tradeoff is most practically relevant. No experiments on non-SwiGLU architectures (GELU, ReGLU) to test generality of the gradient coupling argument. The sparsity sweep (30-60%) is only single-seed. Claims about \"making compensation networks obsolete\" are strong language for evidence from two similar-sized models.\n\n7. **(Minor) The quadratic scaling claim is post-hoc curve fitting presented as a theoretical prediction.** The paper claims to \"predict\" quadratic scaling and then \"verify\" it. But the prediction is informal (no derivation, just a counting argument about pairwise interactions), and 7 data points (single-seed) with R^2=0.97 for a monotonically increasing function is not strong evidence for a specific functional form. A power law, exponential, or other monotone functions would likely also fit well. The paper should report AIC/BIC comparisons against alternative functional forms.\n\n### Questions for Authors\n\n1. What is the performance of MSE on output logits as the training loss? This is the critical missing comparison. If MSE-logits achieves similar results to KL, the contribution is \"use any output-level loss\" rather than \"use KL specifically.\"\n\n2. How does the BCE baseline compare to the numbers reported in the FastForward paper? If FastForward reports significantly better BCE+compensation results on similar models, what accounts for the discrepancy? Were the same hyperparameters, target generation, and training procedure used?\n\n3. Was BCE trained with hard-mask STE (its natural relaxation) or with Gumbel-sigmoid? If Gumbel-sigmoid was used for both, this disadvantages BCE, which operates on binary targets and does not benefit from soft relaxation the same way KL does.\n\n4. Why does BCE-only perform so much worse than training-free methods (28.16 vs TEAL's 12.48)? A trained predictor performing 2x worse than a training-free heuristic suggests something is wrong with the BCE training setup, not that BCE is fundamentally flawed.\n\n5. The Lagrangian sparsity enforcement and KL normalization required significant debugging (decisions log shows D003-D006 sequence of failures). How sensitive is the KL training to these hyperparameters? What happens with naive KL training (no Lagrangian, standard reduction)?\n\n6. For the quadratic scaling claim: what are the R^2 values for alternative functional forms (linear, power law a*s^b, exponential)? Have you tested whether the data actually distinguishes quadratic from other monotone functions?\n\n7. Training was done on WikiText-103 (~100M tokens). How sensitive are results to calibration data domain and size?\n\n### Missing Related Work\n\n**Critical omissions:**\n- **Deja Vu** (Liu et al., ICML 2023): The foundational work on predictor-based contextual sparsity with BCE training. Not citing this while positioning against BCE predictors is a major oversight.\n- **CATS** (Lee et al., 2024): Contextual thresholding for SwiGLU sparsity without training -- a direct competitor achieving good results at 50% sparsity.\n- **Minitron** (Muralidharan et al., NeurIPS 2024): Demonstrates logit-only KL outperforms intermediate matching for structured pruning distillation -- directly supports the paper's argument and should be cited as prior evidence for KL's effectiveness.\n- **DIP** (Federici et al., MLSys 2025): Predictor-free dynamic pruning specifically for SwiGLU, achieving 40% speedup. Argues SwiGLU sparsity patterns are hard to predict.\n\n**Important missing areas:**\n- **Differentiable mask learning literature**: Gumbel-softmax for subset selection (Xie & Ermon, 2019), L0 regularization (Louizos et al., ICLR 2018), differentiable top-k (Cordonnier et al., 2021). The paper uses Gumbel-sigmoid without citing the foundational work or comparing to alternative differentiable relaxations.\n- **Structured pruning + distillation**: Beyond Minitron, works like CoFi (Xia et al., 2022), DistilBERT (Sanh et al., 2019), and Sheared LLaMA (Xia et al., 2023) all use KL/CE distillation for structured compression. The claim \"KL not applied to contextual sparsity predictors\" is narrowly true but the idea of KL-guided sparsity is well-trodden.\n- **Sparsing Law** (Luo et al., 2024): Directly relevant theory on SwiGLU activation sparsity scaling.\n- **ReLU Strikes Back** (Mirzadeh et al., ICLR 2024) and **TurboSparse** (Song et al., 2024): Alternative approaches that achieve high sparsity by modifying activation functions. Important for positioning.\n- **ProSparse** (Song et al., COLING 2025): Progressive sparsification with distribution matching.\n- **SparseInfer** (Shin et al., DATE 2025) and **SVD-CSP** (Serbin et al., 2026): Training-free predictor alternatives.\n- **Gradient coupling in other ML contexts**: The observation that end-to-end losses provide better gradient signal than proxy losses is well-known in multi-task learning, neural architecture search, and differentiable programming. No connection is drawn to this broader literature.\n\n### Novelty Assessment\n\nThe paper's contribution sits at the intersection of two well-established techniques (KL distillation and learned sparsity prediction) and demonstrates their combination works better than the less principled alternative (BCE). This is useful empirical knowledge, but the novelty is limited:\n\n1. **Loss function swap**: The core idea -- replace BCE with KL -- is a one-line change in the training loop. SPON already demonstrated KL works for sparsity in this domain. Extending from static to contextual is a natural next step, not a conceptual leap.\n\n2. **Theoretical contribution is weak**: The gradient coupling argument is correct but trivial (it is the chain rule). The quadratic scaling claim is curve-fitting on 7 single-seed points without formal derivation. No theorem is stated or proved.\n\n3. **Modular decomposition is the strongest novelty**: The SPON+KL composition with quantified interaction analysis is the most original contribution, but it is Claim 2, not the headline claim.\n\n4. **Engineering value vs. scientific novelty**: The paper has clear practical value (simpler inference pipeline, no compensation network needed) but this is an engineering finding, not a scientific discovery. The result was predictable given SPON's demonstration that KL works for sparsity correction.\n\n5. **Positioning relative to SPON**: The paper's novelty depends entirely on the distinction between \"static bias correction\" (SPON) and \"contextual predictor\" (this work). Both use KL to train parameters that improve sparse model quality. The architectural difference (bias vector vs. MLP predictor) is not matched by a conceptual difference in the training methodology.\n\nFor a top venue at 25% acceptance rate, I expect either (a) a new method with clear conceptual novelty, (b) a surprising empirical finding that changes how we think about a problem, or (c) rigorous theory that provides new understanding. This paper offers (b) in a weak sense -- the magnitude of the KL advantage is surprising -- but the direction of the result (KL > BCE for this purpose) was predictable. The missing MSE-logits baseline is the most concerning gap: if it works comparably, the paper's framing around KL-specific properties collapses.\n\n### Preliminary Score: 3/6\n### Confidence: 4/5\n\nThe score reflects: strong empirical results with thorough ablations (positive), but limited novelty in the core technique (loss function swap), weak theoretical contribution (informal argument + curve fitting), critically missing MSE-logits baseline, suspiciously weak BCE baseline, and very sparse related work section. If the MSE-logits baseline shows KL is uniquely effective (not just any output-level loss) AND the BCE baseline fairness concerns are addressed, this could move to a 4. As submitted, the novelty bar for a 25% acceptance rate venue is not met."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d068bc16-de2f-4f9a-a78d-87726e5aaecb",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mNEFBfMC1gR8xkRp9Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e6b1026-7284-42e4-9609-5a3fdc4af1f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZHZHKj7TMfJGhnFUovRpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18964,
      "cache_read_input_tokens": 56013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18964,
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

### Tool result

_source line 47 · 2026-05-15T17:43:18.501Z_

<details><summary>↩ Tool result · `toolu_011w92uujPX8SxGPVQNws6DM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md\", \"dream_id\": \"dream_20260515T164925\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e6b1026-7284-42e4-9609-5a3fdc4af1f4",
  "isSidechain": true,
  "promptId": "34e722ef-3af4-4042-87a9-59b06365f8c2",
  "agentId": "a0030f3fba786c882",
  "type": "user",
  "uuid": "641b3417-d10c-41a3-983a-3363af2b36c9",
  "sourceToolAssistantUUID": "4e6b1026-7284-42e4-9609-5a3fdc4af1f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-15T17:43:29.712Z_

Review submitted. Here is a summary of the key findings:

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Core assessment**: The paper has strong, consistent empirical results (KL-only 9.20 vs BCE+comp 18.64 PPL) and thorough ablations, but the novelty is insufficient for a 25% acceptance rate venue. The contribution reduces to substituting KL for BCE in an existing pipeline -- a natural application of standard knowledge distillation.

**Four major weaknesses identified**:

1. **Thin novelty** -- loss function swap with no new algorithm, architecture, or training procedure. SPON already proved KL works for sparsity in this domain.

2. **Gradient coupling theory is trivial** -- it is the chain rule applied to two different losses. The O(s^2 D^2) argument is informal, and the quadratic scaling claim is curve-fitting on 7 single-seed points, not verified theory.

3. **Missing MSE-on-logits baseline** -- the most critical experiment. MSE on logits also provides gradient coupling. If it matches KL, the paper's framing collapses from "KL is special" to "any output-level loss beats BCE."

4. **Suspiciously weak BCE baseline** -- BCE-only at 28.16 PPL is worse than training-free TEAL (12.48), which suggests possible implementation issues (Gumbel-sigmoid for binary targets, non-standard target generation, etc.).

**Additional concerns**: Only 8 references (should cite DejaVu, CATS, Minitron, DIP, L0 regularization, Gumbel-softmax foundations, etc.); scope limited to two 7-8B SwiGLU models; the paper's own taxonomy shows the "Intermediate (MSE)" column as empty -- filling it is essential before claiming KL is uniquely effective.

The review was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "641b3417-d10c-41a3-983a-3363af2b36c9",
  "isSidechain": true,
  "agentId": "a0030f3fba786c882",
  "requestId": "req_011Cb4mXiY32LAygFcLLBhfJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc5f03f7-4144-47d5-bbfe-2e5243392cf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "be4af677-c918-498a-8593-19b0dadd846b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EB8eNaQKKA1XdqmKP2GJVc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7428,
      "cache_read_input_tokens": 74977,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7428
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 509,
          "cache_read_input_tokens": 74977,
          "cache_creation_input_tokens": 7428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7428,
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
