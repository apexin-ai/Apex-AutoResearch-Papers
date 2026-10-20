# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a87b7c9d30836e971.jsonl`
- **Structured JSON:** [`547c578e02396a6d3159.json`](../../sessions/54/547c578e02396a6d3159.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-20T21:06:17.348Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **methods and experiments**.

## Paper Summary
"Cross-Lingual Correctness Probes Reveal a Depth–Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds"

The paper presents the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. Key findings:

1. **Pareto Frontier**: Deeper layers yield higher English AUROC (up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman ρ = −0.52).
2. **CKA Mechanistic Explanation**: Geometric misalignment increases with depth. CKA–transfer correlation r=0.58 (34% variance), vs MMD r=0.25 (6%).
3. **CaCLR Negative Result**: MMD-based consistency loss is inert across 3 OOM (Cohen's d=0.08, p=0.42).
4. **Linear Projection**: +3.5pp AUROC with ~50-100 parallel pairs, succeeds because it learns the rotation MMD cannot.

Additional: correctness–confidence orthogonality persists across 20 languages (cosine < 0.10). Difficulty decomposition shows 65% improvement rate. Cross-benchmark generalization on Belebele and MMLU-ProX.

## Key Tables/Results from the Paper

**Table 1 (Pareto frontier summary):**
- Qwen3-235B: EN_best=0.81 layer72, ZS_med=0.70 xfer_layer48, ρ_med=−0.51, σ_ρ=0.16
- Llama 4 Scout: EN_best=0.79 layer36, ZS_med=0.68 xfer_layer24, ρ_med=−0.54, σ_ρ=0.15
- Gemma 4 31B: EN_best=0.80 layer45, ZS_med=0.69 xfer_layer33, ρ_med=−0.58, σ_ρ=0.12

**Table 2**: Per-language ZS transfer AUROC at best transfer layer (Qwen3). High-resource 0.72-0.74, mid 0.65-0.71, low (sw/bn) 0.57-0.58.

**Table 3 (CKA):** CKA_shallow=0.84 median, CKA_deep=0.52 median. CKA Pearson r=0.58 (34% var), MMD r=0.25 (6% var).

**Table 4 (β sweep):** β=0.001 Δ=+0.002, β=0.01 Δ=+0.001, β=0.1 Δ=−0.001, β=1.0 Δ=−0.003. Overall p=0.42, d=0.08.

**Table 5 (Method comparison):** Mean-shift=0.000, CaCLR α-only=+0.005, CaCLR full=+0.012, Linear proj=+0.035 (p=0.001,d=0.55), Few-shot-25=+0.025, Few-shot-100=+0.045.

**Table 6 (Linear proj sample efficiency):** 10 pairs→+0.012, 50→+0.030, 100→+0.035, 200→+0.036. Knee ~70 pairs.

**Table 7 (Decomposition):** Overall 65% improved, +0.012 AUROC. Deep layers 78%, shallow 50%. Random direction 50% (n.s.).

**Table 8 (Orthogonality):** EN cosine ~0.035-0.038, all langs <0.10, resource-tier gradient (high 0.04, low 0.085).

**Appendices:** INT8 validation (max diff 0.8pp, r=0.997), MLP vs LogReg (MLP +2.5pp EN but 6pp larger transfer gap), cross-benchmark (method rankings consistent), control tasks (88% above 10pp selectivity).

## Experimental Design Reference
The review_context.yaml lists 12 imagined experiments. The paper covers:
- plan_001 (Qwen3 Pareto): ✓ covered in Tables 1-2
- plan_002 (Llama4 Pareto): ✓ covered in Table 1
- plan_003 (CaCLR): ✓ covered in Tables 4-5
- plan_004 (Decomposition): ✓ covered in Table 7
- plan_005 (Orthogonality): ✓ covered in Table 8
- plan_006 (Probe complexity): ✓ Appendix B
- plan_007 (Additional benchmarks): ✓ Appendix C
- plan_008 (Gemma 4 Dense): ✓ Table 1, Section 5.7
- plan_009 (Extended 52 langs): ✓ Section 5.8
- plan_010 (INT8 validation): ✓ Appendix A
- plan_011 (CKA analysis): ✓ Table 3, Section 5.2
- plan_012 (Linear proj sensitivity): ✓ Table 6, Section 5.4
- plan_013 (Control tasks): ✓ Appendix D

## Your Task
Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (methodological rigor, experimental design, statistical reporting)
3. **Weaknesses** (methodological gaps, experimental concerns, missing controls/ablations)
4. **Questions for Authors** (specific, actionable)
5. **Minor Issues** (presentation, clarity)
6. **Overall Assessment** with score (1-6) and confidence (1-5)

Focus areas for R1:
- Is the experimental design sufficient to support the claims?
- Are the statistical methods appropriate (paired permutation tests, bootstrap CIs, Cohen's d)?
- Is the CKA analysis convincing as a mechanistic explanation?
- Is the CaCLR negative result well-controlled?
- Are there missing baselines or ablations?
- Is the linear projection comparison fair?
- How robust are the results across architectures/languages/benchmarks?

Be rigorous but fair. Identify both genuine weaknesses and acknowledge genuine strengths. The review should be 800-1200 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "0b3c58bd-e488-45b4-997b-6629a1a3a376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T21:06:17.355Z_

```json
{
  "parentUuid": "0b3c58bd-e488-45b4-997b-6629a1a3a376",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
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
  "uuid": "509237e2-8e65-4d08-b8f5-d9a9951fa53b",
  "timestamp": "2026-05-20T21:06:17.355Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T21:06:19.643Z_



I'll start by reading the paper and supporting materials to ground my review in the actual content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "509237e2-8e65-4d08-b8f5-d9a9951fa53b",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW43usHR6WnzvTXtqVd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66fb6e05-4911-482d-bc23-f44da2421953",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gU836MGubnj25cnq9NyM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7766,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7766,
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

_source line 4 · 2026-05-20T21:06:20.810Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DfqVfyeKr7t3wTo3yvnXnR`</summary>

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
  "parentUuid": "66fb6e05-4911-482d-bc23-f44da2421953",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW43usHR6WnzvTXtqVd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f79dedc-ae52-4839-a908-8b9f8d148506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gU836MGubnj25cnq9NyM2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7766,
      "cache_read_input_tokens": 8251,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7766
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7766,
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

_source line 5 · 2026-05-20T21:06:20.815Z_

<details><summary>↩ Tool result · `toolu_01DfqVfyeKr7t3wTo3yvnXnR`</summary>

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
  "parentUuid": "2f79dedc-ae52-4839-a908-8b9f8d148506",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "b36a2085-34fe-43e3-990f-22f7143e41d5",
  "sourceToolAssistantUUID": "2f79dedc-ae52-4839-a908-8b9f8d148506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T21:06:30.143Z_



Let me read the key project files to ground the review properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b36a2085-34fe-43e3-990f-22f7143e41d5",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW4K7vQGpVCqSiYhRt2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4990407-9677-479c-8746-e68ecaa083c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCGz3eWStdBmopYqTB61wa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 7 · 2026-05-20T21:06:31.566Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ni8qrgP9uuw9PQwdFFbRws`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "report.md",
  "max_chars": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4990407-9677-479c-8746-e68ecaa083c3",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW4K7vQGpVCqSiYhRt2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dec7699a-68e7-4165-88ee-a8d45e8eed46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCGz3eWStdBmopYqTB61wa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 8 · 2026-05-20T21:06:31.578Z_

<details><summary>↩ Tool result · `toolu_01Ni8qrgP9uuw9PQwdFFbRws`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n- **mvp_002** (success): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1012, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dec7699a-68e7-4165-88ee-a8d45e8eed46",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "abf0b03a-be61-439f-9b29-9a2e71bff1e0",
  "sourceToolAssistantUUID": "dec7699a-68e7-4165-88ee-a8d45e8eed46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T21:06:32.043Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MxJ6UUtPEUJrz9tdWRNkE6`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_framing.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abf0b03a-be61-439f-9b29-9a2e71bff1e0",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW4K7vQGpVCqSiYhRt2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9629b81f-5254-4d5d-b1c5-b9164683def0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCGz3eWStdBmopYqTB61wa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 10 · 2026-05-20T21:06:32.055Z_

<details><summary>↩ Tool result · `toolu_01MxJ6UUtPEUJrz9tdWRNkE6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff is architecture-dependent (strong on Qwen, weak on Llama), explained by architecture-specific CKA cliff steepness. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal an architecture-dependent depth-transferability relationship: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong Pareto); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture-dependence of the Pareto shape is itself a core finding, not merely a qualifier.\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA pilot reveals the mechanistic explanation: correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\"\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA analysis provides two levels of insight: (a) between-language: languages with higher CKA (more aligned to English) show less transfer degradation — resource-tier gradient explained; (b) between-architecture: CKA cliff steepness at deepest layers differs (Qwen drops 50% in last 3 layers vs Llama 19%), explaining why Pareto is strong on Qwen but weak on Llama. Within-language depth effect requires 20-language full-scale analysis for statistical power (pilot n=9 per language insufficient). CKA pilot on 2 models × 5 languages validates the approach.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA pilot reveals correctness direction is a robust low-dimensional subspace feature that persists despite global representation divergence. Not a simple \\\"low CKA → bad transfer\\\" relationship, but a threshold phenomenon: transfer collapses only when CKA drops below critical value (~0.35) at deepest layers.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 12237, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9629b81f-5254-4d5d-b1c5-b9164683def0",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "2e61319a-5669-49da-ad7b-abf4af378f3d",
  "sourceToolAssistantUUID": "9629b81f-5254-4d5d-b1c5-b9164683def0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T21:06:32.620Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011kpVwDHZPoaWa51iEBhQSC`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "decisions.yaml",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e61319a-5669-49da-ad7b-abf4af378f3d",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW4K7vQGpVCqSiYhRt2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e08bf3f5-4663-4565-b920-1a355bc6c31f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCGz3eWStdBmopYqTB61wa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16017,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 16017,
          "cache_creation_input_tokens": 1291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1291,
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

_source line 12 · 2026-05-20T21:06:32.629Z_

<details><summary>↩ Tool result · `toolu_011kpVwDHZPoaWa51iEBhQSC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml\", \"content\": \"_next_id: 9\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 13:49 UTC\\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\\n    的大资源。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 13:53 UTC\\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 18:25 UTC\\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: trigger\\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-20 18:52 UTC\\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: primary\\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-20 20:14 UTC\\n  summary: 'Dream review (3/6 weak reject) processed: 13 confirmed actions, 5 observations,\\n    3 ignores. Framing updated with conditional CaCLR narrative + 6 new reviewer concerns.\\n    3 new P1 experiments added (CKA, linproj sensitivity, control tasks). Proceeding\\n    with re-dream after changes.'\\n  rationale: 'Dream dream_20260520T185641 scored best=4/6 median=3/6 worst=3/6. Key\\n    structural issues identified across all 3 tiers: (1) no statistical tests — added\\n    as cross-cutting requirement; (2) CaCLR framing incoherent — redesigned as conditional\\n    narrative with two paths; (3) missing related work (domain adaptation theory,\\n    alignment literature, probing critiques) — added to paper_framing.md. Two-tier\\n    issues: (4) no mechanistic explanation — added plan_011 CKA analysis; (5) arbitrary\\n    AUROC threshold — added sensitivity analysis requirement; (6) probing methodology\\n    — added plan_013 control tasks. CaCLR consistency loss value is the key data-dependent\\n    risk (O3). Core 4-claim structure preserved; framing strengthened not weakened.\\n    No venue downgrade — issues are addressable via experiments and framing improvements.'\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: affected\\n    result: CaCLR conditional narrative added\\n  - exp_id: plan_011\\n    role: new\\n    result: CKA mechanistic analysis (P1, 5 GPU-hrs)\\n  - exp_id: plan_012\\n    role: new\\n    result: Linear projection sensitivity (P1, 2 GPU-hrs)\\n  - exp_id: plan_013\\n    role: new\\n    result: Probing control tasks (P1, 2 GPU-hrs)\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 20:23 UTC\\n  summary: 'MVP gate re-evaluation after P1 leakage fix: 2/4 PASS, still proceed to\\n    research phase'\\n  rationale: 'M005 reveals temp scaling data leakage — P1 ECE now FAIL (0.2216 > 0.15).\\n    Gate drops from 3/4 to 2/4 PASS. However, the 2 passing criteria (P2: cross-lingual\\n    transfer 4/5 langs, P3: layer depth effect 14.28pp) are the hypothesis-critical\\n    ones that validate \\\"correctness direction exists and transfers cross-lingually.\\\"\\n    P1 ECE failure means raw probes are poorly calibrated — this is exactly the problem\\n    CaCLR is designed to solve, and actually strengthens the paper''s motivation (\\\"probe-based\\n    calibration needs CaCLR because naive probes fail on calibration\\\"). P4 mean-shift\\n    failure was already attributed to criteria design error (D003). Research phase\\n    continues with strengthened CaCLR motivation. The 0.15 ECE threshold for P1 was\\n    always somewhat arbitrary — discrimination (AUROC=0.754) is the primary signal\\n    that correctness information is linearly accessible.'\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: gate_check\\n    result: 2/4 PASS (P2+P3), P1 ECE FAIL after leakage fix\\n  - exp_id: plan_003\\n    role: motivated_by\\n    result: CaCLR motivation strengthened by raw probe calibration failure\\n  depends_on:\\n  - D004\\n  - D005\\n- id: D007\\n  date: 2026-05-20 20:31 UTC\\n  summary: 'mvp_003 (Llama-3.1-8B) cross-architecture validation: 3/4 PASS, Pareto\\n    architecture-dependence confirmed as core finding'\\n  rationale: 'mvp_003 gate 3/4 PASS (P1 PASS without temp scaling, P2 5/5, P3 7.85pp,\\n    P4 FAIL). Cross-architecture validation successful: correctness direction and\\n    transfer both replicate. Key finding: Pareto tradeoff is STRONG on Qwen (4/5 langs\\n    show depth-transfer degradation) but WEAK on Llama (only 2/5 — zh and sw; ar/ko\\n    improve with depth). This elevates architecture-dependence from a qualifier to\\n    a core finding in Claim 1. CKA pilot shows same two-model contrast. Swahili is\\n    model-dependent (fails Qwen, passes Llama). zh@L31 mean-shift anomaly flagged\\n    for investigation.'\\n  related_experiments:\\n  - exp_id: mvp_003\\n    role: validation\\n    result: 3/4 PASS, weak Pareto on Llama\\n  - exp_id: mvp_001\\n    role: comparison\\n    result: 2/4 PASS (post-fix), strong Pareto on Qwen\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-20 20:40 UTC\\n  summary: 'Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4), consistent with mvp_001.\\n    P1 evaluated at best-AUROC layer.'\\n  rationale: 'Reviewer pointed out D007 ambiguity: P1 passes at L0 (AUROC=0.650, ECE=0.148)\\n    but fails at best-AUROC layer L31 (AUROC=0.728, ECE=0.205). P1 should be evaluated\\n    at the best-AUROC layer (the probe we''d actually use), where ECE fails. Both\\n    models are now 2/4 PASS (P2+P3). This is consistent and actually cleaner: discrimination\\n    (P2+P3) confirmed on both architectures, calibration (P1+P4) fails on both → strengthens\\n    CaCLR motivation uniformly. No impact on research phase decision (D006).'\\n  related_experiments:\\n  - exp_id: mvp_003\\n    role: clarification\\n    result: 2/4 PASS (P2+P3), not 3/4\\n  - exp_id: mvp_001\\n    role: comparison\\n    result: 2/4 PASS (P2+P3), consistent\\n  depends_on:\\n  - D007\\n\", \"total_chars\": 6389, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e08bf3f5-4663-4565-b920-1a355bc6c31f",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "13d9c824-bfbc-4beb-9f04-7e39341576eb",
  "sourceToolAssistantUUID": "e08bf3f5-4663-4565-b920-1a355bc6c31f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T21:06:37.400Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011pz7nrJVxrQ1jfcF86RbLm`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_checklist.yaml",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13d9c824-bfbc-4beb-9f04-7e39341576eb",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW5BP7WFQ7qvFq4HfDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eaf3afa-1e65-4778-b64c-a77eb7a0402b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQQFqkheYXYCiZKf4PEssq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7163,
      "cache_read_input_tokens": 17308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7163,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 14 · 2026-05-20T21:06:37.409Z_

<details><summary>↩ Tool result · `toolu_011pz7nrJVxrQ1jfcF86RbLm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eaf3afa-1e65-4778-b64c-a77eb7a0402b",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "cf1729eb-4f85-4fb6-bd6e-4da1ef638db1",
  "sourceToolAssistantUUID": "7eaf3afa-1e65-4778-b64c-a77eb7a0402b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T21:06:37.707Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QPPBmQsxZJ3maK5jsL5GrJ`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "EVALUATION.md",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf1729eb-4f85-4fb6-bd6e-4da1ef638db1",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW5BP7WFQ7qvFq4HfDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc1e3100-4fe0-4c9e-ac5e-4cc148b70fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQQFqkheYXYCiZKf4PEssq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7163,
      "cache_read_input_tokens": 17308,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7163
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 17308,
          "cache_creation_input_tokens": 7163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7163,
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

_source line 16 · 2026-05-20T21:06:37.723Z_

<details><summary>↩ Tool result · `toolu_01QPPBmQsxZJ3maK5jsL5GrJ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc1e3100-4fe0-4c9e-ac5e-4cc148b70fcc",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "a153678e-b812-4d4d-a560-9b46a8cd1ed0",
  "sourceToolAssistantUUID": "fc1e3100-4fe0-4c9e-ac5e-4cc148b70fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T21:06:40.242Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017p3VNawQ154v7B7EXnWJQ7`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ideas.md",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a153678e-b812-4d4d-a560-9b46a8cd1ed0",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW5ZA3a5ZbYsdfyJVYZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d82b01a1-f5fe-4a62-b70c-7734a07435fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFT9QS7ygJKEKkRUE4TV2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 24471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 384,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 18 · 2026-05-20T21:06:40.255Z_

<details><summary>↩ Tool result · `toolu_017p3VNawQ154v7B7EXnWJQ7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d82b01a1-f5fe-4a62-b70c-7734a07435fc",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "36f1d334-3384-416c-9e06-5faffdc70c71",
  "sourceToolAssistantUUID": "d82b01a1-f5fe-4a62-b70c-7734a07435fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T21:06:40.407Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NtsPxZ274qLt5DqveqcjcS`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ROADMAP.md",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36f1d334-3384-416c-9e06-5faffdc70c71",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW5ZA3a5ZbYsdfyJVYZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0743909a-f166-4e2a-b834-3a50145088b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFT9QS7ygJKEKkRUE4TV2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 24471,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 384
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 24471,
          "cache_creation_input_tokens": 384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 384,
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

_source line 20 · 2026-05-20T21:06:40.420Z_

<details><summary>↩ Tool result · `toolu_01NtsPxZ274qLt5DqveqcjcS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-20 20:18 UTC | 更新原因: Reviewer feedback integrated: D12 grid justification, D16 mean-shift formalization, CaCLR Path B geometric theory, per-language rho, CKA pilot\\n\\n## 核心方向\\nCross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier (depth vs transferability). CaCLR tests distributional matching; CKA provides mechanistic explanation. Mean-shift rank-invariance proof as formal theoretical contribution. 详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research phase** — MVP 通过 (D004)，Dream 审稿处理完成 (D005)，Reviewer 反馈已整合。等待 re-dream 验证后批准 P0。\\n\\n## Dream 审稿处理总结\\n- 初审评分: best=4/6, median=3/6, worst=3/6 (weak reject)\\n- 13+2 条确认行动项已执行（Reviewer 补充 D12 grid 理由 + D16 mean-shift 形式化）\\n- CaCLR framing 改为 conditional narrative（Path A method / Path B negative result with geometric explanation）\\n- 新增 3 P1 实验: plan_011 (CKA), plan_012 (linproj sensitivity), plan_013 (probing controls)\\n- 全局统计检验要求 + per-language Pareto rho + threshold sensitivity\\n- 5 条观察项待真实实验\\n\\n## 紧急事项\\n- ⚠️ Temperature scaling T=6.21 数据划分未确认 — Agent 正在检查（data integrity 风险）\\n- Agent 同时跑 CKA pilot（MVP activations，验证 plan_011 pipeline）\\n\\n## 近期任务\\n- [ ] Agent 确认 temp scaling 数据划分 + CKA pilot 结果\\n- [ ] 确认 mvp_003 (Llama-3.1-8B) 结果\\n- [ ] Re-dream 验证 framing/plan 改动（目标: best ≥ weak accept, median ≥ borderline）\\n- [ ] Re-dream 达标后批准 plan_001 + plan_002（P0，可 4 GPU 并行）\\n- [ ] [Dream 观察] O1: plan_002 Llama4 Pareto rho\\n- [ ] [Dream 观察] O3: plan_003 CaCLR consistency loss\\n- [ ] [Dream 观察] O4: plan_005 orthogonality 贡献度\\n\\n## GPU 预算\\n- 分配: 4× RTX 6000 PRO 96GB (westd-13176)\\n- P0: ~155 GPU-hrs | P1: ~39 GPU-hrs (含 Dream 新增 9h) | P2: ~80 GPU-hrs\\n- MVP 已用: ~7 GPU-hrs\\n\\n## 实验计划\\n详见 experiment_plan.yaml。P0: 4 (plan_001-004)。P1: 7 (plan_005-013)。P2: 2 (plan_008-009)。\\nCross-cutting: bootstrap CI + paired test + Cohen's d + AUROC threshold sensitivity + per-language rho。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n| D002 | 2026-05-20 | MVP 模型固定为 Qwen2.5-7B-Instruct | — |\\n| D001 | 2026-05-20 | MVP 用 7-8B 模型验证核心假设，不直接上 235B | — |\\n\\n\", \"total_chars\": 2633, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0743909a-f166-4e2a-b834-3a50145088b8",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "bb059f02-158e-420f-acf8-d88c028df186",
  "sourceToolAssistantUUID": "0743909a-f166-4e2a-b834-3a50145088b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T21:06:42.717Z_

Now let me look at the artifacts directory and any paper-related files for more detail on the experimental setup.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb059f02-158e-420f-acf8-d88c028df186",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW5kh5v3r9XbfYTGCc7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be34b059-61ef-4abc-bd31-e8e870434b21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aCoECUsK8qYWkjhJ5rVkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 24855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1789,
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

_source line 22 · 2026-05-20T21:06:45.117Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015Kw5XDvciis9tNK5zFjGTW`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be34b059-61ef-4abc-bd31-e8e870434b21",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW5kh5v3r9XbfYTGCc7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8370fe9f-88f9-4f23-b06e-db46acd9ebc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aCoECUsK8qYWkjhJ5rVkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 24855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1789,
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

_source line 23 · 2026-05-20T21:06:45.139Z_

<details><summary>↩ Tool result · `toolu_015Kw5XDvciis9tNK5zFjGTW`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T185641/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T185641/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T185641/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json
artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/best/paper.tex
artifacts/dream_reports/dream_20260520T185641/best/paper.aux
artifacts/dream_reports/dream_20260520T185641/best/paper.out
artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
artifacts/dream_reports/dream_20260520T185641/best/paper.log
artifacts/dream_reports/dream_20260520T185641/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json
artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/median/paper.tex
artifacts/dream_reports/dream_20260520T185641/median/paper.aux
artifacts/dream_reports/dream_20260520T185641/median/paper.out
artifacts/dream_reports/dream_20260520T185641/median/paper.pdf
artifacts/dream_reports/dream_20260520T185641/median/paper.log
artifacts/dream_reports/dream_20260520T185641/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/worst/paper.tex
artifacts/dream_reports/dream_20260520T185641/worst/references.bib
artifacts/dream_reports/dream_20260520T185641/worst/paper.bbl
artifacts/dream_reports/dream_20260520T185641/worst/paper.blg
artifacts/dream_reports/dream_20260520T185641/worst/paper.aux
artifacts/dream_reports/dream_20260520T185641/worst/paper.out
artifacts/dream_reports/dream_20260520T185641/worst/paper.pdf
artifacts/dream_reports/dream_20260520T185641/worst/paper.log
artifacts/dream_reports/dream_20260520T185641/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T185641/logs/review_best.log
artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/logs/review_median.log
artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/median/review_report.md
artifacts/dream_reports/dream_20260520T185641/best/review_report.md
artifacts/dream_reports/dream_20260520T185641/worst/review_report.md
artifacts/dream_reports/dream_20260520T185641/logs/review_worst.log
artifacts/dream_reports/dream_20260520T185641/meta.yaml
artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png
artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png
artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png
artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png
artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p10.png
artifacts/review_issues.yaml
artifacts/review_reports/round_0.md
artifacts/dream_reports/dream_20260520T201854/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T201854/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T201854/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T201854/logs/phase2_median_attempt0.log
artifacts/_project/report/cka_vs_degradation_report.md
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260520T201854/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json
artifacts/dream_reports/dream_20260520T201854/best/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/best/references.bib
artifacts/dream_reports/dream_20260520T201854/best/paper.tex
artifacts/dream_reports/dream_20260520T201854/best/paper.aux
artifacts/dream_reports/dream_20260520T201854/best/paper.out
artifacts/dream_reports/dream_20260520T201854/best/paper.pdf
artifacts/dream_reports/dream_20260520T201854/best/paper.log
artifacts/dream_reports/dream_20260520T201854/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/median/experiment_data.json
artifacts/dream_reports/dream_20260520T201854/median/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/median/paper.tex
artifacts/dream_reports/dream_20260520T201854/median/paper.aux
artifacts/dream_reports/dream_20260520T201854/median/paper.out
artifacts/dream_reports/dream_20260520T201854/median/paper.pdf
artifacts/dream_reports/dream_20260520T201854/median/paper.log
artifacts/dream_reports/dream_20260520T201854/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T201854/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/worst/references.bib
artifacts/dream_reports/dream_20260520T201854/worst/paper.tex
artifacts/dream_reports/dream_20260520T201854/worst/paper.bbl
artifacts/dream_reports/dream_20260520T201854/worst/paper.blg
artifacts/dream_reports/dream_20260520T201854/worst/paper.aux
artifacts/dream_reports/dream_20260520T201854/worst/paper.out
artifacts/dream_reports/dream_20260520T201854/worst/paper.pdf
artifacts/dream_reports/dream_20260520T201854/worst/paper.log
artifacts/dream_reports/dream_20260520T201854/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml
artifacts/dream_reports/dream_20260520T201854/best/review_report.md
artifacts/dream_reports/dream_20260520T201854/logs/review_best.log
artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml
artifacts/dream_reports/dream_20260520T201854/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8370fe9f-88f9-4f23-b06e-db46acd9ebc9",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "bae483d5-fcc0-4fee-8ca7-5ba3ae120970",
  "sourceToolAssistantUUID": "8370fe9f-88f9-4f23-b06e-db46acd9ebc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T21:06:45.861Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TthyicvetzPrJazWJAPn3o`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "literature_map.yaml",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bae483d5-fcc0-4fee-8ca7-5ba3ae120970",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW5kh5v3r9XbfYTGCc7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb94af2c-5b51-4911-85a8-c3416d89d19b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aCoECUsK8qYWkjhJ5rVkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 24855,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1789
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 24855,
          "cache_creation_input_tokens": 1789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1789,
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

_source line 25 · 2026-05-20T21:06:45.871Z_

<details><summary>↩ Tool result · `toolu_01TthyicvetzPrJazWJAPn3o`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb94af2c-5b51-4911-85a8-c3416d89d19b",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "e106477c-6c0c-4cff-bd68-0ee43793297d",
  "sourceToolAssistantUUID": "eb94af2c-5b51-4911-85a8-c3416d89d19b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T21:06:48.888Z_

Now let me read the best-case dream paper and review context to understand the exact experimental design and paper content being reviewed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e106477c-6c0c-4cff-bd68-0ee43793297d",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW6A8yVqTdmw4QeCmz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54089a31-5339-41d9-9d9f-fecd0dbb6a47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WtZRYW8tMAt3x2RbLiBM6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5275,
      "cache_read_input_tokens": 26644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5275,
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

_source line 27 · 2026-05-20T21:06:51.891Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MrhwCQmtXpt36pdN8gfA9i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54089a31-5339-41d9-9d9f-fecd0dbb6a47",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW6A8yVqTdmw4QeCmz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aeaceb16-f49d-4aba-b964-e634b82074ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WtZRYW8tMAt3x2RbLiBM6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5275,
      "cache_read_input_tokens": 26644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5275,
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

_source line 28 · 2026-05-20T21:06:52.175Z_

<details><summary>↩ Tool result · `toolu_01MrhwCQmtXpt36pdN8gfA9i`</summary>

```text
1	narrative_guidance: 'Full method contribution paper (Path A). CaCLR consistency loss
2	  provides meaningful gain, confirming distributional matching via MMD helps align
3	  capability-specific signals at mid-depth layers. Causal chain complete: Pareto frontier
4	  discovered on both architectures with architecture-dependent shape → decomposition
5	  explains frontier via difficulty/capability separation → CaCLR shifts frontier by
6	  aligning capability-specific components → orthogonality bounds output-based approaches
7	  across all languages. CKA provides mechanistic glue linking representation geometry
8	  to transfer success. Headline: "CaCLR-trained correctness probes reduce non-English
9	  ECE by 3.5% over temperature scaling with zero target-language labels across 20
10	  languages on Qwen3-235B and Llama 4 Scout."
11	
12	  '
13	imagined_experiments:
14	- name: Full Pareto Frontier — Qwen3-235B-A22B
15	  plan_id: plan_001
16	  description: '94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages,
17	    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
18	    CaCLR).
19	
20	    '
21	  expected_results:
22	    en_best_auroc: 0.838
23	    en_best_layer: 76
24	    en_best_ece_raw: 0.162
25	    en_best_ece_tempcal: 0.048
26	    temp_scaling_T: 4.83
27	    en_auroc_range:
28	    - 0.592
29	    - 0.838
30	    optimal_transfer_layer_median: 56
31	    zs_transfer_auroc_median_20lang: 0.758
32	    zs_transfer_auroc_at_en_optimal_layer76: 0.714
33	    zs_transfer_auroc_at_transfer_optimal_layer56: 0.771
34	    pareto_rho_global: -0.81
35	    pareto_rho_per_lang_median: -0.78
36	    pareto_rho_per_lang_iqr:
37	    - -0.84
38	    - -0.71
39	    zs_langs_above_0p65_out_of_20: 17
40	    best_zs_auroc_by_tier:
41	      HIGH_zh: 0.793
42	      HIGH_es: 0.801
43	      HIGH_fr: 0.798
44	      HIGH_de: 0.784
45	      MID_hi: 0.742
46	      MID_ru: 0.769
47	      MID_ko: 0.751
48	      MID_tr: 0.738
49	      LOW_sw: 0.641
50	      LOW_bn: 0.633
51	    mean_shift_delta_auroc_median: 0.0
52	    linear_proj_delta_auroc_over_zs_median: 0.048
53	    fewshot_25_delta_auroc_over_zs_median: 0.032
54	    fewshot_100_delta_auroc_over_zs_median: 0.055
55	  result_rationale: 'Qwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838，
56	    远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。 Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp
57	    （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。 MoE架构中expert routing在深层更加language-dependent，强化了这一效应。
58	    Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。 17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual
59	    representation—— 仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。 Mean-shift
60	    ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下 mean-shift仅添加常数偏移，不改变rank
61	    order）。 Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。
62	
63	    '
64	  tables:
65	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
66	      Layer'
67	    columns:
68	    - layer
69	    - depth_pct
70	    - en_auroc
71	    - zs_median_auroc
72	    - zs_min_auroc
73	    - zs_max_auroc
74	    - rho_median
75	    rows:
76	    - - 0
77	      - 0
78	      - 0.592
79	      - 0.583
80	      - 0.521
81	      - 0.601
82	      - null
83	    - - 8
84	      - 9
85	      - 0.631
86	      - 0.618
87	      - 0.554
88	      - 0.639
89	      - null
90	    - - 16
91	      - 17
92	      - 0.672
93	      - 0.659
94	      - 0.589
95	      - 0.678
96	      - null
97	    - - 24
98	      - 26
99	      - 0.711
100	      - 0.698
101	      - 0.621
102	      - 0.719
103	      - null
104	    - - 32
105	      - 34
106	      - 0.738
107	      - 0.729
108	      - 0.648
109	      - 0.751
110	      - null
111	    - - 40
112	      - 43
113	      - 0.762
114	      - 0.756
115	      - 0.662
116	      - 0.778
117	      - null
118	    - - 48
119	      - 51
120	      - 0.781
121	      - 0.771
122	      - 0.658
123	      - 0.793
124	      - null
125	    - - 56
126	      - 60
127	      - 0.798
128	      - 0.771
129	      - 0.641
130	      - 0.801
131	      - null
132	    - - 60
133	      - 64
134	      - 0.808
135	      - 0.762
136	      - 0.632
137	      - 0.796
138	      - null
139	    - - 64
140	      - 68
141	      - 0.816
142	      - 0.751
143	      - 0.618
144	      - 0.788
145	      - null
146	    - - 68
147	      - 72
148	      - 0.824
149	      - 0.741
150	      - 0.607
151	      - 0.779
152	      - null
153	    - - 72
154	      - 77
155	      - 0.831
156	      - 0.728
157	      - 0.598
158	      - 0.768
159	      - null
160	    - - 76
161	      - 81
162	      - 0.838
163	      - 0.714
164	      - 0.584
165	      - 0.756
166	      - null
167	    - - 80
168	      - 85
169	      - 0.835
170	      - 0.702
171	      - 0.571
172	      - 0.742
173	      - null
174	    - - 84
175	      - 89
176	      - 0.829
177	      - 0.688
178	      - 0.558
179	      - 0.729
180	      - null
181	    - - 88
182	      - 94
183	      - 0.818
184	      - 0.671
185	      - 0.542
186	      - 0.712
187	      - null
188	    - - 92
189	      - 98
190	      - 0.801
191	      - 0.649
192	      - 0.523
193	      - 0.694
194	      - null
195	  - name: 'Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer
196	      76)'
197	    columns:
198	    - condition
199	    - layer56_median_auroc
200	    - layer76_median_auroc
201	    - delta_vs_zs_l56
202	    - delta_vs_zs_l76
203	    rows:
204	    - - zero-shot
205	      - 0.771
206	      - 0.714
207	      - 0.0
208	      - 0.0
209	    - - mean-shift
210	      - 0.771
211	      - 0.714
212	      - 0.0
213	      - 0.0
214	    - - linear_proj_50pairs
215	      - 0.812
216	      - 0.779
217	      - 0.041
218	      - 0.065
219	    - - fewshot_25
220	      - 0.798
221	      - 0.761
222	      - 0.027
223	      - 0.047
224	    - - fewshot_100
225	      - 0.821
226	      - 0.792
227	      - 0.05
228	      - 0.078
229	    - - CaCLR_full
230	      - 0.828
231	      - 0.788
232	      - 0.057
233	      - 0.074
234	  figures_description:
235	  - 'Fig 1a: Pareto frontier scatter — x-axis EN AUROC, y-axis ZS transfer AUROC median.
236	    Each point is a layer. Clear concave frontier with elbow at ~60% depth. Color
237	    by resource tier shows HIGH langs cluster top-right, LOW langs bottom-left.'
238	  - 'Fig 1b: Heatmap 24 layers × 20 languages, cell color = ZS AUROC. Visible gradient:
239	    warm (high AUROC) at mid-depth for high-resource, shifting to shallower optimum
240	    for low-resource.'
241	  - 'Fig 1c: Per-language Spearman rho distribution (violin plot). Median -0.78, tight
242	    IQR, all languages negative. Annotate sw/bn as outliers with weaker rho.'
243	  analysis: 'Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）—— 此后EN AUROC继续上升但ZS
244	    transfer开始下降。MoE架构的expert routing在深层 更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言
245	    （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多 token coverage，deep-layer
246	    representation与EN的对齐更好。Low-resource（sw/bn） 即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。
247	
248	    '
249	- name: Full Pareto Frontier — Llama 4 Scout
250	  plan_id: plan_002
251	  description: '48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages,
252	    5 transfer conditions.
253	
254	    '
255	  expected_results:
256	    en_best_auroc: 0.821
257	    en_best_layer: 40
258	    en_best_ece_raw: 0.171
259	    en_best_ece_tempcal: 0.053
260	    temp_scaling_T: 5.12
261	    en_auroc_range:
262	    - 0.604
263	    - 0.821
264	    optimal_transfer_layer_median: 24
265	    zs_transfer_auroc_median_20lang: 0.742
266	    zs_transfer_auroc_at_en_optimal_layer40: 0.698
267	    zs_transfer_auroc_at_transfer_optimal_layer24: 0.756
268	    pareto_rho_global: -0.76
269	    pareto_rho_per_lang_median: -0.73
270	    pareto_rho_per_lang_iqr:
271	    - -0.81
272	    - -0.66
273	    zs_langs_above_0p65_out_of_20: 16
274	    best_zs_auroc_by_tier:
275	      HIGH_zh: 0.778
276	      HIGH_es: 0.789
277	      HIGH_fr: 0.781
278	      HIGH_de: 0.772
279	      MID_hi: 0.728
280	      MID_ru: 0.756
281	      MID_ko: 0.739
282	      MID_tr: 0.721
283	      LOW_sw: 0.628
284	      LOW_bn: 0.618
285	    mean_shift_delta_auroc_median: 0.0
286	    linear_proj_delta_auroc_over_zs_median: 0.044
287	  result_rationale: 'Llama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24）， 而Qwen3-235B在60%深度（layer
288	    56）——这就是architecture-dependent shape的关键证据。 Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。
289	    EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。 ZS median 0.742 vs
290	    Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining 数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78，
291	    因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20）， sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim
292	    1的核心发现。
293	
294	    '
295	  tables:
296	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
297	    columns:
298	    - layer
299	    - depth_pct
300	    - en_auroc
301	    - zs_median_auroc
302	    rows:
303	    - - 0
304	      - 0
305	      - 0.604
306	      - 0.592
307	    - - 4
308	      - 8
309	      - 0.638
310	      - 0.624
311	    - - 8
312	      - 17
313	      - 0.674
314	      - 0.661
315	    - - 12
316	      - 25
317	      - 0.712
318	      - 0.701
319	    - - 16
320	      - 33
321	      - 0.741
322	      - 0.738
323	    - - 20
324	      - 42
325	      - 0.768
326	      - 0.756
327	    - - 24
328	      - 50
329	      - 0.788
330	      - 0.756
331	    - - 28
332	      - 58
333	      - 0.801
334	      - 0.742
335	    - - 32
336	      - 67
337	      - 0.811
338	      - 0.726
339	    - - 36
340	      - 75
341	      - 0.818
342	      - 0.711
343	    - - 40
344	      - 83
345	      - 0.821
346	      - 0.698
347	    - - 44
348	      - 92
349	      - 0.814
350	      - 0.679
351	    - - 48
352	      - 100
353	      - 0.798
354	      - 0.654
355	  figures_description:
356	  - 'Fig 2a: Pareto frontiers overlaid — Qwen3-235B (blue) vs Llama 4 Scout (orange).
357	    Both concave but elbow position differs: Qwen at 60% depth, Scout at 50%. Demonstrates
358	    architecture-dependent shape.'
359	  - 'Fig 2b: Architecture comparison heatmap — difference in ZS AUROC (Qwen minus
360	    Scout) by language × normalized depth. Positive (Qwen better) at deep layers for
361	    high-resource; near zero at shallow layers.'
362	  analysis: '两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度， Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE），
363	    而是反映了训练数据分布、expert routing策略和层归一化实现的差异。 Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。
364	    这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。
365	
366	    '
367	- name: CaCLR Implementation and Comparative Evaluation
368	  plan_id: plan_003
369	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。
370	    Path A: β term provides meaningful gain.
371	
372	    '
373	  expected_results:
374	    caclr_optimal_alpha: 1.0
375	    caclr_optimal_beta: 0.1
376	    caclr_beta_delta_auroc_over_alpha_only_median: 0.032
377	    caclr_beta_delta_auroc_over_alpha_only_range:
378	    - 0.018
379	    - 0.051
380	    caclr_full_delta_auroc_over_zeroshot_median: 0.062
381	    caclr_full_delta_auroc_over_zeroshot_range:
382	    - 0.031
383	    - 0.098
384	    caclr_vs_linear_proj_delta_median: 0.014
385	    caclr_vs_fewshot100_delta_median: -0.008
386	    ece_reduction_vs_temp_scaling_median: 0.035
387	    ece_reduction_vs_temp_scaling_range:
388	    - 0.012
389	    - 0.061
390	    beta_sweep_results:
391	      beta_0.001:
392	        delta_auroc_over_alpha_only: 0.008
393	        note: too weak
394	      beta_0.01:
395	        delta_auroc_over_alpha_only: 0.019
396	        note: marginal
397	      beta_0.1:
398	        delta_auroc_over_alpha_only: 0.032
399	        note: optimal
400	      beta_1.0:
401	        delta_auroc_over_alpha_only: 0.021
402	        note: overfitting to distributional match
403	    alpha_sweep_results:
404	      alpha_0.01:
405	        en_ece: 0.068
406	        transfer_auroc_median: 0.779
407	      alpha_0.1:
408	        en_ece: 0.055
409	        transfer_auroc_median: 0.793
410	      alpha_1.0:
411	        en_ece: 0.041
412	        transfer_auroc_median: 0.808
413	      alpha_10.0:
414	        en_ece: 0.038
415	        transfer_auroc_median: 0.791
416	    layer_interaction:
417	      mid_depth_beta_gain: 0.041
418	      deep_layer_beta_gain: 0.024
419	      shallow_layer_beta_gain: 0.018
420	    qwen_results:
421	      layer56_caclr_full_median: 0.828
422	      layer76_caclr_full_median: 0.788
423	    scout_results:
424	      layer24_caclr_full_median: 0.812
425	      layer40_caclr_full_median: 0.771
426	    bootstrap_ci_beta_effect:
427	    - 0.019
428	    - 0.045
429	    paired_permutation_p_beta: 0.003
430	    cohens_d_beta: 0.48
431	  result_rationale: 'CaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only），
432	    支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布， 更高（1.0）则过度约束导致correctness
433	    prediction损失。 β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征 仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。
434	    在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift） 限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。
435	    CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项） 和alignment（β项），而linear
436	    projection仅做alignment。但CaCLR略输于few-shot 100 （-0.8pp），因为100个标注样本提供了直接的target-language
437	    correctness信号。 关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。 ECE reduction vs
438	    temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE， 而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。
439	    Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen''s d=0.48为中等效应量。
440	
441	    '
442	  tables:
443	  - name: 'Table 4: Transfer Method Comparison (Median AUROC across 20 languages,
444	      both models)'
445	    columns:
446	    - method
447	    - labels_needed
448	    - qwen_layer56
449	    - qwen_layer76
450	    - scout_layer24
451	    - scout_layer40
452	    - median_all
453	    rows:
454	    - - zero-shot
455	      - 0
456	      - 0.771
457	      - 0.714
458	      - 0.756
459	      - 0.698
460	      - 0.735
461	    - - mean-shift
462	      - 0
463	      - 0.771
464	      - 0.714
465	      - 0.756
466	      - 0.698
467	      - 0.735
468	    - - CaCLR_alpha_only
469	      - 0 (parallel inputs)
470	      - 0.798
471	      - 0.762
472	      - 0.784
473	      - 0.745
474	      - 0.772
475	    - - CaCLR_full
476	      - 0 (parallel inputs)
477	      - 0.828
478	      - 0.788
479	      - 0.812
480	      - 0.771
481	      - 0.8
482	    - - linear_proj_50
483	      - 50 parallel pairs
484	      - 0.812
485	      - 0.779
486	      - 0.798
487	      - 0.758
488	      - 0.787
489	    - - fewshot_25
490	      - 25
491	      - 0.798
492	      - 0.761
493	      - 0.781
494	      - 0.741
495	      - 0.77
496	    - - fewshot_100
497	      - 100
498	      - 0.821
499	      - 0.792
500	      - 0.808
501	      - 0.778
502	      - 0.8
503	  - name: 'Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)'
504	    columns:
505	    - beta
506	    - delta_auroc_over_alpha_only
507	    - delta_ece_over_alpha_only
508	    - note
509	    rows:
510	    - - 0.001
511	      - 0.008
512	      - -0.003
513	      - negligible distributional constraint
514	    - - 0.01
515	      - 0.019
516	      - -0.008
517	      - marginal improvement
518	    - - 0.1
519	      - 0.032
520	      - -0.014
521	      - optimal — balances alignment and prediction
522	    - - 1.0
523	      - 0.021
524	      - -0.011
525	      - over-regularized — MMD dominates loss
526	  figures_description:
527	  - 'Fig 3a: Bar chart — 5 transfer methods × 2 models at optimal transfer layer.
528	    CaCLR_full highest, followed by fewshot_100, linear_proj, CaCLR_alpha_only, zero-shot.
529	    Error bars = bootstrap 95% CI.'
530	  - 'Fig 3b: β sweep curve — x-axis β (log scale), y-axis ΔAUROC over α-only. Inverted-U
531	    shape peaking at β=0.1. Three lines for shallow/mid/deep layers showing mid-depth
532	    benefits most.'
533	  - 'Fig 3c: Pareto frontier shift — original ZS frontier (dashed) vs CaCLR frontier
534	    (solid) for both architectures. CaCLR pushes frontier up and right, especially
535	    at mid-depth.'
536	  analysis: 'CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致： mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough
537	    language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明 distributional matching存在sweet
538	    spot——太弱无效，太强则牺牲correctness prediction。 CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近
539	    100-label supervised的性能，但不需要任何target-language correctness labels。 统计显著性（p=0.003,
540	    d=0.48）确保β效应不是噪声。
541	
542	    '
543	- name: Difficulty-Controlled Decomposition Ablation
544	  plan_id: plan_004
545	  description: 'IRT difficulty probes → project out difficulty → retrain correctness
546	    probes → evaluate transfer. 10 languages × 8 layers × 2 models.
547	
548	    '
549	  expected_results:
550	    decomposition_transfer_delta_after_difficulty_removal_median: 0.031
551	    decomposition_transfer_delta_range:
552	    - 0.011
553	    - 0.052
554	    difficulty_probe_r2_median: 0.68
555	    difficulty_direction_cosine_with_correctness: 0.34
556	    capability_specific_transfer_degradation_per_depth:
557	      shallow_20pct: 0.008
558	      mid_50pct: 0.024
559	      deep_80pct: 0.048
560	    random_direction_control_delta: 0.002
561	    resource_tier_pattern:
562	      HIGH_delta: 0.022
563	      MID_delta: 0.033
564	      LOW_delta: 0.041
565	    bootstrap_ci_decomposition_delta:
566	    - 0.018
567	    - 0.044
568	    paired_permutation_p: 0.006
569	    cohens_d: 0.41
570	  result_rationale: 'Difficulty direction与correctness direction有中等cosine（0.34），说明两者共享
571	    部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更 "capability-pure"——这个信号在高资源语言间更容易transfer（+2.2pp），
572	    因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp）， 因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布
573	    与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。 深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。
574	    Random-direction control仅+0.2pp，排除了dimensionality reduction artifact—— 是difficulty方向的specific
575	    removal而非arbitrary降维带来的改善。 这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability
576	    alignment （高delta = 高difficulty entanglement = 需要CaCLR/projection）。
577	
578	    '
579	  tables:
580	  - name: 'Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after
581	      difficulty removal)'
582	    columns:
583	    - depth_pct
584	    - HIGH_avg
585	    - MID_avg
586	    - LOW_avg
587	    - random_control
588	    rows:
589	    - - 20
590	      - 0.012
591	      - 0.014
592	      - 0.019
593	      - 0.001
594	    - - 35
595	      - 0.016
596	      - 0.022
597	      - 0.028
598	      - 0.002
599	    - - 50
600	      - 0.021
601	      - 0.031
602	      - 0.038
603	      - 0.002
604	    - - 60
605	      - 0.024
606	      - 0.036
607	      - 0.043
608	      - 0.003
609	    - - 70
610	      - 0.026
611	      - 0.039
612	      - 0.046
613	      - 0.002
614	    - - 80
615	      - 0.028
616	      - 0.041
617	      - 0.048
618	      - 0.003
619	    - - 85
620	      - 0.025
621	      - 0.038
622	      - 0.044
623	      - 0.002
624	    - - 90
625	      - 0.022
626	      - 0.034
627	      - 0.041
628	      - 0.002
629	  figures_description:
630	  - 'Fig 4a: Three-panel heatmap (HIGH/MID/LOW) — 8 layers × decomposition delta.
631	    Gradient intensifies with depth and decreases with resource level.'
632	  - 'Fig 4b: Scatter plot — difficulty-correctness cosine similarity vs decomposition
633	    delta. Each point = language × layer. Clear positive correlation (r=0.71).'
634	  - 'Fig 4c: Bar chart — decomposition delta vs random-direction control delta at
635	    each depth. Orders of magnitude difference confirms specificity.'
636	  analysis: 'Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离， 且分离后capability-specific信号的cross-lingual
637	    transfer一致改善。 关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重，
638	    也从decomposition中获益最多。这为CaCLR提供了theoretical motivation： CaCLR的consistency loss本质上在做distributional
639	    alignment of capability-specific signals。 Random-direction control（~0pp）是关键的methodological
640	    guard rail。
641	
642	    '
643	- name: Cross-Lingual Orthogonality Analysis
644	  plan_id: plan_005
645	  description: 'Correctness-confidence cosine similarity across 20 languages × 2 architectures,
646	    analyzed by resource tier and language family.
647	
648	    '
649	  expected_results:
650	    orthogonality_cosine_mean_across_langs: 0.042
651	    orthogonality_cosine_max_across_langs: 0.062
652	    orthogonality_cosine_min_across_langs: 0.018
653	    orthogonality_cosine_std: 0.013
654	    cosine_by_tier:
655	      HIGH_mean: 0.038
656	      MID_mean: 0.043
657	      LOW_mean: 0.051
658	    cosine_by_architecture:
659	      qwen_mean: 0.039
660	      scout_mean: 0.046
661	    cosine_range_qwen_20lang:
662	    - 0.018
663	    - 0.058
664	    cosine_range_scout_20lang:
665	    - 0.022
666	    - 0.062
667	    all_20_langs_below_0p08: true
668	    bootstrap_ci_mean_cosine:
669	    - 0.035
670	    - 0.049
671	  result_rationale: 'Orthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值）， 确认Miao
672	    & Ungar (2026)的English-only发现是universal structural property。 Low-resource语言cosine略高（0.051
673	    vs HIGH 0.038），因为这些语言的confidence probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的
674	    apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值， 说明output-based calibration在结构上受限不依赖于语言。
675	    Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量 使correctness和confidence能被编码在更分离的子空间中。
676	    这个发现bounds entire output-based calibration approach：无论语言或架构， verbalized confidence不包含correctness信息，motivating
677	    probe-based方法。
678	
679	    '
680	  tables:
681	  - name: 'Table 7: Correctness-Confidence Cosine Similarity by Language'
682	    columns:
683	    - language
684	    - tier
685	    - qwen_cosine
686	    - scout_cosine
687	    - mean
688	    rows:
689	    - - en
690	      - HIGH
691	      - 0.031
692	      - 0.037
693	      - 0.034
694	    - - zh
695	      - HIGH
696	      - 0.035
697	      - 0.041
698	      - 0.038
699	    - - es
700	      - HIGH
701	      - 0.033
702	      - 0.039
703	      - 0.036
704	    - - fr
705	      - HIGH
706	      - 0.034
707	      - 0.04
708	      - 0.037
709	    - - de
710	      - HIGH
711	      - 0.036
712	      - 0.042
713	      - 0.039
714	    - - hi
715	      - MID
716	      - 0.039
717	      - 0.045
718	      - 0.042
719	    - - ru
720	      - MID
721	      - 0.037
722	      - 0.043
723	      - 0.04
724	    - - ko
725	      - MID
726	      - 0.041
727	      - 0.047
728	      - 0.044
729	    - - tr
730	      - MID
731	      - 0.043
732	      - 0.049
733	      - 0.046
734	    - - sw
735	      - LOW
736	      - 0.048
737	      - 0.056
738	      - 0.052
739	    - - bn
740	      - LOW
741	      - 0.052
742	      - 0.058
743	      - 0.055
744	  figures_description:
745	  - 'Fig 5: Dot plot — cosine similarity per language, sorted by resource tier. Horizontal
746	    line at 0.08 threshold. All points below. Color by architecture (Qwen blue, Scout
747	    orange). Visible tier gradient.'
748	  analysis: 'Cross-lingual orthogonality的universal persistence是论文的bounding contribution。
749	    它回答了"为什么需要probe-based calibration"：因为output-based方法在结构上 无法获取correctness信息（cosine<0.08），无论语言。Resource
750	    tier gradient 是nuanced finding但不影响main conclusion。
751	
752	    '
753	- name: Probe Complexity Comparison
754	  plan_id: plan_006
755	  description: 'Logistic regression vs 2-layer MLP across all probed layers, both
756	    models. EN accuracy, cross-lingual transfer degradation, calibration comparison.
757	
758	    '
759	  expected_results:
760	    lr_en_best_auroc_qwen: 0.838
761	    mlp_en_best_auroc_qwen: 0.852
762	    lr_en_best_auroc_scout: 0.821
763	    mlp_en_best_auroc_scout: 0.834
764	    lr_zs_transfer_degradation_median: 0.068
765	    mlp_zs_transfer_degradation_median: 0.104
766	    lr_transfer_advantage_over_mlp_median: 0.022
767	    lr_ece_vs_mlp_ece:
768	    - -0.008
769	    - 0.003
770	    mlp_overfit_indicator_deep_layers: true
771	  result_rationale: 'Linear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上
772	    显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多 overfitting to source
773	    language——这些patterns在target语言中不泛化。 这与probe complexity literature一致（Hewitt & Liang
774	    2019）：更强的probe 在source domain表现更好但generalization更差。Linear probe的inductive bias
775	    （只能学习线性可分方向）恰好与correctness direction的线性结构匹配， 同时限制了对language-specific artifacts的拟合。
776	    在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。 这个结果support使用logistic
777	    regression作为primary probe的选择。
778	
779	    '
780	  tables:
781	  - name: 'Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected
782	      layers)'
783	    columns:
784	    - layer
785	    - lr_en
786	    - mlp_en
787	    - lr_zs_median
788	    - mlp_zs_median
789	    - lr_transfer_advantage
790	    rows:
791	    - - 24
792	      - 0.711
793	      - 0.722
794	      - 0.698
795	      - 0.691
796	      - 0.007
797	    - - 40
798	      - 0.762
799	      - 0.778
800	      - 0.756
801	      - 0.741
802	      - 0.015
803	    - - 56
804	      - 0.798
805	      - 0.814
806	      - 0.771
807	      - 0.752
808	      - 0.019
809	    - - 76
810	      - 0.838
811	      - 0.852
812	      - 0.714
813	      - 0.686
814	      - 0.028
815	  figures_description:
816	  - 'Fig S1: Dual-axis plot — EN AUROC (solid) and ZS transfer AUROC (dashed) vs layer
817	    depth, separate lines for LR and MLP. MLP''s solid line higher but dashed line
818	    lower, scissors gap widens at deep layers.'
819	  analysis: 'Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。 这个结果also间接支持correctness
820	    direction是线性的——linear probe已经捕获了 大部分信号，MLP额外捕获的主要是noise/language-specific artifact。
821	
822	    '
823	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
824	  plan_id: plan_007
825	  description: 'Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。
826	
827	    '
828	  expected_results:
829	    belebele_zs_auroc_median: 0.731
830	    belebele_caclr_auroc_median: 0.789
831	    mmlu_prox_zs_auroc_median: 0.748
832	    mmlu_prox_caclr_auroc_median: 0.801
833	    cross_benchmark_correlation: 0.92
834	    belebele_pareto_rho_median: -0.71
835	    mmlu_prox_pareto_rho_median: -0.75
836	  result_rationale: 'Belebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs
837	    0.758）， 因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在 （rho=-0.71），说明depth-transfer
838	    tradeoff是task-general的。 MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748
839	    vs 0.758）。 CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp）， 说明CaCLR学到的alignment不是GlobalMMLU-specific的。
840	    Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致——
841	    sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。
842	
843	    '
844	  tables:
845	  - name: 'Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)'
846	    columns:
847	    - benchmark
848	    - zs_median
849	    - caclr_median
850	    - pareto_rho
851	    - langs_above_0p65
852	    rows:
853	    - - GlobalMMLU
854	      - 0.758
855	      - 0.808
856	      - -0.78
857	      - 17
858	    - - Belebele
859	      - 0.731
860	      - 0.789
861	      - -0.71
862	      - 15
863	    - - MMLU-ProX
864	      - 0.748
865	      - 0.801
866	      - -0.75
867	      - 16
868	  figures_description:
869	  - 'Fig S2: Scatter — per-language ZS AUROC on GlobalMMLU vs Belebele. High correlation
870	    (r=0.92). Each point labeled with language code.'
871	  analysis: 'Cross-benchmark泛化confirm findings are not benchmark-specific artifact。
872	    Pareto frontier在三个benchmark上一致存在但shape有细微差异—— Belebele更浅的optimal depth可能反映reading
873	    comprehension使用了更浅层的表征。
874	
875	    '
876	- name: INT8 Validation Ablation
877	  plan_id: plan_010
878	  description: 'INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。
879	
880	    '
881	  expected_results:
882	    int8_fp16_auroc_max_diff: 0.006
883	    int8_fp16_auroc_mean_diff: 0.003
884	    int8_fp16_ece_max_diff: 0.008
885	    int8_fp16_direction_cosine_min: 0.987
886	    all_diffs_within_noise: true
887	  result_rationale: 'INT8量化对correctness direction的影响极小（max AUROC差异0.6pp）， 因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度，
888	    而correctness direction在high-variance维度上有强projection。 Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。
889	    ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。 这排除了"INT8 artifact"的reviewer
890	    concern。
891	
892	    '
893	  tables:
894	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)'
895	    columns:
896	    - layer
897	    - int8_auroc
898	    - fp16_auroc
899	    - diff
900	    - direction_cosine
901	    rows:
902	    - - 8
903	      - 0.674
904	      - 0.678
905	      - -0.004
906	      - 0.991
907	    - - 16
908	      - 0.741
909	      - 0.745
910	      - -0.004
911	      - 0.989
912	    - - 24
913	      - 0.788
914	      - 0.791
915	      - -0.003
916	      - 0.992
917	    - - 32
918	      - 0.811
919	      - 0.814
920	      - -0.003
921	      - 0.99
922	    - - 40
923	      - 0.821
924	      - 0.827
925	      - -0.006
926	      - 0.987
927	  figures_description:
928	  - 'Fig S3: Bland-Altman plot — mean of INT8/FP16 AUROC (x) vs difference (y). All
929	    points within ±0.01 band. No systematic bias.'
930	  analysis: 'INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。 Deep层差异略大（layer
931	    40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。 但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。
932	
933	    '
934	- name: CKA Cross-Lingual Representation Similarity
935	  plan_id: plan_011
936	  description: 'CKA (linear kernel) between EN and each target language at every probed
937	    layer, correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.
938	
939	    '
940	  expected_results:
941	    cka_transfer_pearson_r: 0.82
942	    cka_transfer_pearson_r_ci:
943	    - 0.76
944	    - 0.87
945	    cka_transfer_spearman_rho: 0.79
946	    cka_en_zh_by_depth_trend: monotonically decreasing from 0.92 (shallow) to 0.61
947	      (deep)
948	    cka_en_sw_by_depth_trend: monotonically decreasing from 0.84 (shallow) to 0.38
949	      (deep)
950	    cka_resource_tier_gradient:
951	      HIGH_mean_cka_at_optimal_depth: 0.78
952	      MID_mean_cka_at_optimal_depth: 0.71
953	      LOW_mean_cka_at_optimal_depth: 0.58
954	    geometric_misalignment_evidence: 'CKA drop from mid to deep layers exceeds what
955	      mean/covariance shift alone predicts. Subspace angle analysis shows correctness
956	      direction rotates 15-35° across languages at deep layers vs 5-12° at shallow
957	      layers.
958	
959	      '
960	    cka_explains_caclr_beta_limit: 'At layers where CKA < 0.55, β term provides diminishing
961	      returns because geometric misalignment (rotation) dominates distributional shift.
962	
963	      '
964	  result_rationale: 'CKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic
965	    explanation： cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。
966	    这不是trivial的"深层更specific"——CKA量化了具体的相似度数值并与transfer成功率 建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining
967	    data overlap）， 解释了resource tier gradient。 关键insight：deep层的CKA下降不仅是distributional
968	    shift（可被MMD修正）， 还包含geometric misalignment（correctness方向在语言间旋转15-35°）。 这解释了CaCLR
969	    β term在deep层效果减弱——MMD对齐分布但不学习旋转， 而linear projection学习旋转所以在deep层更稳定。 Subspace angle
970	    analysis区分了distributional vs geometric misalignment， 为Path A narrative提供了theoretical
971	    depth：CaCLR works at mid-depth因为 那里的misalignment主要是distributional的。
972	
973	    '
974	  tables:
975	  - name: 'Table 10: CKA by Depth and Resource Tier (Qwen3-235B)'
976	    columns:
977	    - depth_pct
978	    - HIGH_cka
979	    - MID_cka
980	    - LOW_cka
981	    - zs_auroc_median
982	    rows:
983	    - - 10
984	      - 0.93
985	      - 0.89
986	      - 0.84
987	      - 0.618
988	    - - 25
989	      - 0.9
990	      - 0.85
991	      - 0.78
992	      - 0.698
993	    - - 40
994	      - 0.86
995	      - 0.79
996	      - 0.69
997	      - 0.756
998	    - - 50
999	      - 0.82
1000	      - 0.74
1001	      - 0.62
1002	      - 0.771
1003	    - - 60
1004	      - 0.78
1005	      - 0.69
1006	      - 0.55
1007	      - 0.771
1008	    - - 70
1009	      - 0.73
1010	      - 0.63
1011	      - 0.47
1012	      - 0.741
1013	    - - 80
1014	      - 0.67
1015	      - 0.56
1016	      - 0.41
1017	      - 0.714
1018	    - - 90
1019	      - 0.61
1020	      - 0.49
1021	      - 0.35
1022	      - 0.688
1023	  figures_description:
1024	  - 'Fig 6a: Dual-axis — CKA (left y-axis, lines by tier) and ZS AUROC median (right
1025	    y-axis, dashed) vs normalized depth. CKA decrease tracks AUROC decrease after
1026	    elbow.'
1027	  - 'Fig 6b: Scatter — CKA vs ZS transfer AUROC, each point = language × layer. Strong
1028	    linear relationship (r=0.82). Color by resource tier.'
1029	  - 'Fig 6c: Subspace angle between EN and target correctness directions vs depth.
1030	    Angles increase with depth; LOW languages diverge faster.'
1031	  analysis: 'CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier） 与explanation（representation
1032	    geometry变化）和method（CaCLR的作用机制与局限） 连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable
1033	    finding—— 实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。 Geometric vs distributional
1034	    misalignment的区分是theoretical contribution： 它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减，
1035	    而geometric alignment（linear projection）在deep层更稳定。
1036	
1037	    '
1038	- name: Linear Projection Sensitivity Analysis
1039	  plan_id: plan_012
1040	  description: 'Linear projection pair count sweep (10, 20, 50, 100, 200). Both models
1041	    × 5 layers × 20 languages.
1042	
1043	    '
1044	  expected_results:
1045	    linear_proj_min_pairs_for_saturation: 35
1046	    saturation_criterion: 95% of 200-pair performance
1047	    pairs_sweep:
1048	      10:
1049	        median_auroc: 0.762
1050	        pct_of_200: 0.88
1051	      20:
1052	        median_auroc: 0.778
1053	        pct_of_200: 0.94
1054	      50:
1055	        median_auroc: 0.792
1056	        pct_of_200: 0.98
1057	      100:
1058	        median_auroc: 0.796
1059	        pct_of_200: 0.99
1060	      200:
1061	        median_auroc: 0.798
1062	        pct_of_200: 1.0
1063	    low_resource_saturation_later: true
1064	    low_resource_min_pairs: 48
1065	    high_resource_min_pairs: 22
1066	  result_rationale: 'Linear projection在~35 pairs时达到饱和（95% of 200-pair performance），
1067	    因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。 10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric
1068	    transformation。 50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。 Low-resource语言需要slightly
1069	    more pairs（48 vs 22），因为表征空间中 correctness方向的SNR更低，需要更多样本来robustly估计映射。 整体saturation在20-50范围内，support
1070	    "≤50 parallel pairs suffice"的claim。 这建立了linear projection作为practical baseline的地位——
1071	    50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。
1072	
1073	    '
1074	  tables:
1075	  - name: 'Table 11: Linear Projection Data Efficiency (median across 20 langs × 2
1076	      models)'
1077	    columns:
1078	    - n_pairs
1079	    - median_auroc
1080	    - delta_vs_zs
1081	    - pct_of_200pair
1082	    - HIGH_auroc
1083	    - LOW_auroc
1084	    rows:
1085	    - - 10
1086	      - 0.762
1087	      - 0.027
1088	      - 88
1089	      - 0.781
1090	      - 0.638
1091	    - - 20
1092	      - 0.778
1093	      - 0.043
1094	      - 94
1095	      - 0.798
1096	      - 0.651
1097	    - - 50
1098	      - 0.792
1099	      - 0.057
1100	      - 98
1101	      - 0.814
1102	      - 0.664
1103	    - - 100
1104	      - 0.796
1105	      - 0.061
1106	      - 99
1107	      - 0.818
1108	      - 0.668
1109	    - - 200
1110	      - 0.798
1111	      - 0.063
1112	      - 100
1113	      - 0.821
1114	      - 0.671
1115	  figures_description:
1116	  - 'Fig S4: Learning curve — n_pairs (x, log) vs median AUROC (y). Rapid rise, plateau
1117	    at ~50. Separate lines for HIGH/MID/LOW tiers — all plateau but at different levels.'
1118	  analysis: 'Linear projection的data efficiency confirms它作为practical baseline的价值。 50
1119	    pairs的saturation point意味着任何有minimal translation capacity的语言 都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat
1120	    50-pair projection 才能justify its additional complexity（in best tier, CaCLR beats
1121	    by +1.4pp median）。
1122	
1123	    '
1124	- name: Probing Control Tasks (Hewitt & Liang 2019)
1125	  plan_id: plan_013
1126	  description: 'Random-label control probes at each layer. Selectivity = probe AUROC
1127	    - control AUROC. Validates genuine correctness signal.
1128	
1129	    '
1130	  expected_results:
1131	    control_task_auroc_range:
1132	    - 0.502
1133	    - 0.538
1134	    selectivity_median: 0.284
1135	    selectivity_min: 0.192
1136	    selectivity_max: 0.341
1137	    control_task_selectivity_min_across_langs: 0.192
1138	    selectivity_by_depth:
1139	      shallow: 0.218
1140	      mid: 0.294
1141	      deep: 0.312
1142	    selectivity_by_tier:
1143	      HIGH: 0.301
1144	      MID: 0.278
1145	      LOW: 0.234
1146	  result_rationale: 'Control probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284
1147	    远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映 genuine correctness
1148	    direction而非memorized artifacts或probe capacity。 Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness
1149	    信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。 Low-resource语言selectivity最低（0.234）但仍远超threshold，
1150	    说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。 这直接回应Hewitt & Liang probing
1151	    methodology critique—— 我们的probes确实在提取linguistic property而非exploiting high-dimensional
1152	    capacity。
1153	
1154	    '
1155	  tables:
1156	  - name: 'Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)'
1157	    columns:
1158	    - layer
1159	    - en_selectivity
1160	    - zh_selectivity
1161	    - sw_selectivity
1162	    - control_auroc
1163	    rows:
1164	    - - 16
1165	      - 0.248
1166	      - 0.231
1167	      - 0.192
1168	      - 0.512
1169	    - - 32
1170	      - 0.281
1171	      - 0.268
1172	      - 0.218
1173	      - 0.519
1174	    - - 48
1175	      - 0.309
1176	      - 0.292
1177	      - 0.241
1178	      - 0.524
1179	    - - 56
1180	      - 0.318
1181	      - 0.301
1182	      - 0.248
1183	      - 0.521
1184	    - - 76
1185	      - 0.341
1186	      - 0.324
1187	      - 0.262
1188	      - 0.538
1189	  figures_description:
1190	  - 'Fig S5: Paired bar chart — probe AUROC (dark) vs control AUROC (light) at each
1191	    layer. Gap (selectivity) clearly visible and widening with depth. Horizontal line
1192	    at 15pp threshold.'
1193	  analysis: 'Control task validation是methodological necessity。Selectivity最小值19.2pp
1194	    大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer） 也确认probe是在提取genuine
1195	    signal。这让reviewer对所有downstream结果 （Pareto frontier, CaCLR, decomposition）更有信心。
1196	
1197	    '
1198	- name: Gemma 4 31B Dense — Camera-Ready Extension
1199	  plan_id: plan_008
1200	  description: 'Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE
1201	    contrast for camera-ready.
1202	
1203	    '
1204	  expected_results:
1205	    en_best_auroc: 0.809
1206	    en_best_layer: 48
1207	    optimal_transfer_layer: 36
1208	    zs_transfer_auroc_median: 0.738
1209	    pareto_rho_median: -0.69
1210	    pareto_shape: smoother frontier than MoE models — no sharp elbow
1211	    dense_vs_moe_key_finding: 'Dense architecture shows shallower Pareto slope — transfer
1212	      degrades more gradually with depth compared to MoE models. Consistent with hypothesis
1213	      that expert routing accelerates language specialization.
1214	
1215	      '
1216	  result_rationale: 'Gemma 4 31B Dense作为dense对照提供了architectural contrast。 EN AUROC
1217	    0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。 关键发现：dense架构的Pareto
1218	    frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78）， 没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete
1219	    language specialization（某些experts "负责"特定语言），而dense模型的specialization是gradual的。
1220	    这是architecture-dependent Pareto shape claim的strongest evidence。 Optimal transfer在75%深度（layer
1221	    36/48），比Qwen3浅（60%）但比Scout深（50%）， 提供了第三个data point来characterize architecture-depth
1222	    relationship。
1223	
1224	    '
1225	  tables:
1226	  - name: 'Table S3: Three-Architecture Comparison Summary'
1227	    columns:
1228	    - model
1229	    - type
1230	    - params
1231	    - layers
1232	    - en_best_auroc
1233	    - zs_median
1234	    - optimal_transfer_pct
1235	    - pareto_rho
1236	    rows:
1237	    - - Qwen3-235B-A22B
1238	      - MoE
1239	      - 235B
1240	      - 94
1241	      - 0.838
1242	      - 0.758
1243	      - 60
1244	      - -0.78
1245	    - - Llama 4 Scout
1246	      - MoE
1247	      - 109B (17B active)
1248	      - 48
1249	      - 0.821
1250	      - 0.742
1251	      - 50
1252	      - -0.73
1253	    - - Gemma 4 31B Dense
1254	      - Dense
1255	      - 31B
1256	      - 60
1257	      - 0.809
1258	      - 0.738
1259	      - 75
1260	      - -0.69
1261	  figures_description:
1262	  - 'Fig S6: Three Pareto frontiers overlaid on normalized depth axis. MoE models
1263	    show sharper elbows; Dense model is smoother. Annotated with optimal transfer
1264	    depth for each.'
1265	  analysis: 'Three-architecture comparison is the crown jewel of Claim 1。 Dense vs
1266	    MoE对比provides causal insight into WHY frontiers differ—— expert routing is the
1267	    mechanism driving sharp language specialization at depth.
1268	
1269	    '
1270	- name: Extended Language Coverage — Camera-Ready
1271	  plan_id: plan_009
1272	  description: 'Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele
1273	    full sets.
1274	
1275	    '
1276	  expected_results:
1277	    total_languages: 52
1278	    zs_langs_above_0p65: 38
1279	    zs_auroc_median_52lang: 0.721
1280	    new_low_resource_findings: 'Several additional low-resource languages (e.g., Yoruba,
1281	      Hausa, Malagasy) show ZS AUROC 0.58-0.64, confirming resource-tier gradient
1282	      extends to tail.
1283	
1284	      '
1285	    pareto_frontier_robust: true
1286	    caclr_generalizes: true
1287	    caclr_delta_over_zs_52lang_median: 0.058
1288	  result_rationale: '52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758
1289	    降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。 38/52 > 0.65（73%）vs
1290	    17/20（85%），比例下降也反映低资源语言的加入。 Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。
1291	    Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62） 与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp），
1292	    可能因为GlobalMMLU translations provide parallel data that partially bridges the representation
1293	    gap for these extremely low-resource languages.
1294	
1295	    '
1296	  tables:
1297	  - name: 'Table S4: Extended Language Coverage Summary'
1298	    columns:
1299	    - resource_tier
1300	    - n_langs
1301	    - zs_auroc_median
1302	    - caclr_median
1303	    - delta
1304	    rows:
1305	    - - HIGH
1306	      - 12
1307	      - 0.786
1308	      - 0.828
1309	      - 0.042
1310	    - - MID
1311	      - 18
1312	      - 0.741
1313	      - 0.798
1314	      - 0.057
1315	    - - LOW
1316	      - 22
1317	      - 0.648
1318	      - 0.721
1319	      - 0.073
1320	  figures_description:
1321	  - 'Fig S7: World map — ZS AUROC by country/language, color gradient from red (low)
1322	    to green (high). Clear geographic pattern tracking resource availability.'
1323	  analysis: Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。
1324	    Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp）， because these languages have
1325	    the most room for improvement and CaCLR's distributional alignment compensates
1326	    for sparse pretraining representation.
1327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aeaceb16-f49d-4aba-b964-e634b82074ea",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "8002a7aa-8cb0-462c-8a18-6b140a937ec6",
  "sourceToolAssistantUUID": "aeaceb16-f49d-4aba-b964-e634b82074ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T21:06:52.243Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pftauzq85jszczwaW67V97`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8002a7aa-8cb0-462c-8a18-6b140a937ec6",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW6A8yVqTdmw4QeCmz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cea8671-2b19-4bb9-adcc-036717f3e66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WtZRYW8tMAt3x2RbLiBM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5275,
      "cache_read_input_tokens": 26644,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 26644,
          "cache_creation_input_tokens": 5275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5275,
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

_source line 30 · 2026-05-20T21:06:52.249Z_

<details><summary>↩ Tool result · `toolu_01Pftauzq85jszczwaW67V97`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{enumitem}
12	\usepackage[T1]{fontenc}
13	\usepackage[utf8]{inputenc}
14	\usepackage{microtype}
15	\usepackage{tabularx}
16	\usepackage{natbib}
17	\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}
18	
19	\title{Cross-Lingual Calibration via Internal Correctness Directions:\\Pareto Frontiers, Decomposition, and Consistency-Aligned Probes}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Multilingual large language models exhibit substantially worse calibration in non-English languages, yet probe-based calibration methods remain English-only.
28	We present the first systematic study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B-A22B, Llama~4~Scout).
29	We discover a \emph{depth--transferability Pareto frontier}: deeper layers yield higher English probe AUROC but degrade in zero-shot cross-lingual transfer (Spearman $\rho=-0.78$/$-0.73$).
30	The frontier shape is architecture-dependent, with the optimal transfer depth at 60\% for Qwen3 versus 50\% for Scout.
31	We decompose correctness transfer into difficulty-shared and capability-specific components, showing that removing the difficulty direction improves transfer by 3.1~pp (median), with low-resource languages benefiting most (+4.1~pp).
32	We propose CaCLR, a probe training objective combining binary cross-entropy, sample-binned ECE, and an MMD-based cross-lingual consistency loss on parallel activations.
33	CaCLR-trained probes reduce non-English ECE by 3.5\% over temperature scaling with zero target-language labels, matching few-shot (100-label) supervised performance.
34	CKA analysis reveals that cross-lingual representation similarity monotonically decreases with depth ($r=0.82$ with transfer AUROC), mechanistically explaining the Pareto frontier.
35	Finally, we confirm that correctness--confidence orthogonality (cosine $<0.062$) persists universally across all 20 languages, bounding output-based calibration regardless of language.
36	\end{abstract}
37	
38	%---------------------------------------------------------------
39	\section{Introduction}
40	\label{sec:intro}
41	%---------------------------------------------------------------
42	
43	Calibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for deploying language models in high-stakes settings.
44	Recent work has shown that multilingual LLMs suffer from substantially worse calibration in non-English languages, with expected calibration error (ECE) up to 5$\times$ higher than English \cite{}.
45	Output-based calibration methods such as temperature scaling \cite{guo2017calibration} and verbalized confidence extraction \cite{} offer post-hoc corrections but face a structural limitation:
46	\citet{} demonstrated that the internal \emph{correctness direction} (encoding whether the model will answer correctly) is nearly orthogonal to the \emph{confidence direction} (encoding verbalized confidence), with cosine similarity below 0.04 in English.
47	This orthogonality means output-based signals are fundamentally uninformative about actual correctness.
48	
49	Probe-based calibration methods---training linear classifiers on internal representations to predict correctness---offer a principled alternative by directly accessing the correctness direction \cite{}.
50	However, all existing probe-based methods (CORAL, CCPS, Confidence Manifold, correctness steering) operate exclusively in English.
51	The question of whether correctness probes transfer cross-lingually---enabling calibration in languages without correctness labels---remains open.
52	
53	We present the first systematic study of cross-lingual correctness probe transfer.
54	Our contributions form a causal chain:
55	
56	\paragraph{(1) Pareto Frontier Discovery.}
57	We reveal a depth--transferability Pareto frontier: deeper layers produce better English probes (AUROC up to 0.838) but degrade in zero-shot cross-lingual transfer.
58	The frontier shape is architecture-dependent---optimal transfer depth is 60\% for Qwen3-235B versus 50\% for Llama~4~Scout---with MoE expert routing accelerating deep-layer language specialization.
59	
60	\paragraph{(2) Difficulty--Capability Decomposition.}
61	We decompose the correctness signal into a difficulty-shared component (language-agnostic, transferable) and a capability-specific component (language-dependent, driving deep-layer degradation).
62	Removing the difficulty direction improves cross-lingual transfer by 3.1~pp median, with low-resource languages benefiting most (+4.1~pp).
63	
64	\paragraph{(3) CaCLR: Calibration-Consistent Cross-Lingual Regularization.}
65	We propose CaCLR, a probe training objective that jointly optimizes correctness prediction ($\mathcal{L}_\text{BCE}$), calibration ($\alpha \cdot \mathcal{L}_\text{SB-ECE}$), and cross-lingual distributional alignment ($\beta \cdot \mathcal{L}_\text{MMD}$) using parallel activations from translated items.
66	CaCLR requires zero target-language correctness labels and reduces non-English ECE by 3.5\% over temperature scaling across 20 languages.
67	
68	\paragraph{(4) Cross-Lingual Orthogonality.}
69	We confirm that correctness--confidence orthogonality persists across all 20 languages and both architectures (max cosine = 0.062), establishing that output-based calibration is structurally limited regardless of language.
70	
71	CKA representation similarity analysis provides the mechanistic glue: cross-lingual CKA monotonically decreases with depth ($r=0.82$ with transfer AUROC), explaining why deeper layers degrade and why CaCLR's distributional matching is most effective at mid-depth layers where misalignment is distributional rather than geometric.
72	
73	
74	%---------------------------------------------------------------
75	\section{Related Work}
76	\label{sec:related}
77	%---------------------------------------------------------------
78	
79	\paragraph{LLM Calibration.}
80	Temperature scaling \cite{guo2017calibration} remains the dominant post-hoc calibration method.
81	Recent work reveals that multilingual LLMs are substantially worse-calibrated in non-English languages.
82	LACE proposes per-language layer ensembles but requires target-language labels.
83	MKA uses multi-agent knowledge aggregation at 5$\times$ inference cost.
84	
85	\paragraph{Probe-Based Calibration.}
86	CORAL trains cross-task English correctness probes and identifies distribution-shift challenges.
87	CCPS uses clustering on correctness probe activations.
88	Miao \& Ungar discover correctness--confidence orthogonality and propose steering-based calibration, but only for English on 7--8B models.
89	All probe-based methods remain monolingual.
90	
91	\paragraph{Cross-Lingual Probe Transfer.}
92	Xiao et al.\ transfer \emph{knowledge boundary} probes (input-level answerability) across 8 languages.
93	Knowledge boundary is fundamentally different from correctness: answerability is an input property (does the model have relevant knowledge?) while correctness is output-dependent (will the model produce the right answer for this input?).
94	Their success with mean-shift alignment is not expected to transfer to correctness probes, and we formally prove why (Section~\ref{sec:method:transfer}).
95	Civelli et al.\ study cross-lingual \emph{difficulty} probes, which we use as a control in our decomposition analysis.
96	
97	\paragraph{Domain Adaptation Theory.}
98	Ben-David et al.'s $\mathcal{H}$-divergence framework predicts that cross-domain transfer degrades with increasing domain divergence.
99	We derive predictions from this framework and test them: the resource-tier gradient follows theory, but the architecture-dependent Pareto shape and difficulty--capability entanglement are novel findings.
100	
101	\paragraph{Representation Similarity.}
102	CKA \cite{kornblith2019similarity} measures representational similarity between network layers.
103	We use CKA to mechanistically explain the Pareto frontier by quantifying cross-lingual representation divergence at each depth.
104	
105	\paragraph{Cross-Lingual Alignment.}
106	Linear cross-lingual alignment methods (MUSE, VecMap) learn rotation matrices between embedding spaces.
107	Our linear projection baseline is conceptually similar; CaCLR's distributional matching via MMD represents the alternative alignment paradigm.
108	
109	\paragraph{Conformal Prediction.}
110	Distribution-free conformal prediction provides coverage guarantees but requires calibration data per language.
111	Our approach targets zero-label transfer, making the two complementary.
112	
113	
114	%---------------------------------------------------------------
115	\section{Method}
116	\label{sec:method}
117	%---------------------------------------------------------------
118	
119	\subsection{Correctness Probes}
120	\label{sec:method:probes}
121	
122	Given a multilingual LLM with $L$ layers, we extract the hidden representation $\mathbf{h}_\ell \in \mathbb{R}^d$ at layer $\ell$ for each input.
123	A correctness probe $f_\ell: \mathbb{R}^d \to [0,1]$ is a logistic regression classifier trained on English data to predict whether the model's generated answer is correct:
124	\begin{equation}
125	    f_\ell(\mathbf{h}) = \sigma(\mathbf{w}_\ell^\top \mathbf{h} + b_\ell)
126	\end{equation}
127	where $\mathbf{w}_\ell \in \mathbb{R}^d$ defines the \emph{correctness direction} at layer $\ell$.
128	We evaluate probes via AUROC (discrimination) and ECE (calibration).
129	
130	\subsection{Cross-Lingual Transfer}
131	\label{sec:method:transfer}
132	
133	We apply English-trained probes directly to target-language representations (zero-shot transfer).
134	We also evaluate several alignment strategies:
135	
136	\paragraph{Mean-Shift.}
137	Subtract the English mean and add the target-language mean of representations.
138	Under StandardScaler preprocessing + logistic regression, mean-shift adds a constant offset to all logits.
139	Since AUROC is rank-invariant, $\Delta\text{AUROC} \equiv 0$ mathematically---mean-shift cannot improve discrimination under this pipeline.
140	
141	\paragraph{Linear Projection.}
142	Learn a linear map $\mathbf{A} \in \mathbb{R}^{d \times d}$ from parallel English--target representation pairs to align the target-language representations to the English correctness subspace.
143	
144	\paragraph{Few-Shot.}
145	Fine-tune probes with 25 or 100 labeled target-language examples.
146	
147	\subsection{CaCLR: Calibration-Consistent Cross-Lingual Regularization}
148	\label{sec:method:caclr}
149	
150	CaCLR trains correctness probes with a composite loss:
151	\begin{equation}
152	    \mathcal{L}_\text{CaCLR} = \mathcal{L}_\text{BCE} + \alpha \cdot \mathcal{L}_\text{SB-ECE} + \beta \cdot \mathcal{L}_\text{MMD}
153	\end{equation}
154	
155	\noindent where:
156	\begin{itemize}[nosep,leftmargin=*]
157	    \item $\mathcal{L}_\text{BCE}$: binary cross-entropy on English correctness labels.
158	    \item $\mathcal{L}_\text{SB-ECE}$: sample-binned ECE, a differentiable calibration loss.
159	    \item $\mathcal{L}_\text{MMD}$: maximum mean discrepancy between English and target-language \emph{probe activations} on parallel inputs (GlobalMMLU train-split translations). This encourages the probe to produce similar output distributions for semantically equivalent inputs across languages.
160	\end{itemize}
161	
162	The MMD term aligns distributional properties (mean, covariance) of probe activations without requiring target-language correctness labels---only parallel inputs.
163	We set $\alpha=1.0$ and $\beta=0.1$ based on hyperparameter sweeps (Section~\ref{sec:exp:caclr}).
164	
165	\subsection{Difficulty--Capability Decomposition}
166	\label{sec:method:decomp}
167	
168	We hypothesize that the correctness signal mixes two components:
169	(1)~a \emph{difficulty-shared} component reflecting item difficulty (language-agnostic), and
170	(2)~a \emph{capability-specific} component reflecting the model's language-specific ability (drives deep-layer transfer degradation).
171	
172	We operationalize this via IRT difficulty probes: train a probe to predict item difficulty (from IRT parameters), extract the difficulty direction $\mathbf{d}_\ell$, project it out of representations, and retrain correctness probes on the residual.
173	Improved transfer on residual representations confirms that difficulty entanglement degrades cross-lingual transfer.
174	A random-direction control validates that the improvement is specific to difficulty removal, not arbitrary dimensionality reduction.
175	
176	%---------------------------------------------------------------
177	\section{Experimental Setup}
178	\label{sec:setup}
179	%---------------------------------------------------------------
180	
181	\paragraph{Models.}
182	Qwen3-235B-A22B (94 layers, MoE, INT8) and Llama~4~Scout (48 layers, MoE, INT8).
183	We probe every 4th layer: 24 layers for Qwen3, 12 for Scout.
184	
185	\paragraph{Languages.}
186	20 languages spanning three resource tiers: HIGH (en, zh, es, fr, de), MID (hi, ru, ko, tr, and 5 others), LOW (sw, bn, and 8 others).
187	
188	\paragraph{Benchmarks.}
189	Primary: GlobalMMLU (multilingual MCQA).
190	Generalization: Belebele (reading comprehension), MMLU-ProX (knowledge QA).
191	
192	\paragraph{Probes.}
193	Logistic regression with StandardScaler preprocessing.
194	We validate this choice against 2-layer MLPs (Section~\ref{sec:exp:probe}).
195	
196	\paragraph{Evaluation.}
197	AUROC for discrimination, ECE for calibration.
198	All comparisons include bootstrap CIs (1000 resamples) and paired permutation tests.
199	Effect sizes reported with Cohen's $d$.
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cea8671-2b19-4bb9-adcc-036717f3e66d",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "10d4d28b-9d8d-4fc0-818d-4a2c3900cce8",
  "sourceToolAssistantUUID": "8cea8671-2b19-4bb9-adcc-036717f3e66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T21:06:57.537Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RMHR8BNmG7xX4KfbLmUM4F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d4d28b-9d8d-4fc0-818d-4a2c3900cce8",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW6dDQJi7AEY8ciVxry",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "648c33dd-457a-43d5-9c02-961bff1ec92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APY3kH8pKM4ed3MsdsATLy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23540,
      "cache_read_input_tokens": 31919,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 31919,
          "cache_creation_input_tokens": 23540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23540,
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

_source line 32 · 2026-05-20T21:06:57.543Z_

<details><summary>↩ Tool result · `toolu_01RMHR8BNmG7xX4KfbLmUM4F`</summary>

```text
200	
201	\paragraph{Transfer Conditions.}
202	Zero-shot, mean-shift, linear projection (50 parallel pairs), few-shot (25/100 labels), and CaCLR.
203	
204	%---------------------------------------------------------------
205	\section{Results}
206	\label{sec:results}
207	%---------------------------------------------------------------
208	
209	\subsection{Pareto Frontier Discovery}
210	\label{sec:exp:pareto}
211	
212	\begin{table}[t]
213	\centering
214	\small
215	\begin{tabular}{@{}lccccc@{}}
216	\toprule
217	\textbf{Layer} & \textbf{Depth} & \textbf{EN} & \textbf{ZS Med.} & \textbf{ZS Min} & \textbf{ZS Max} \\
218	\midrule
219	\multicolumn{6}{l}{\emph{Qwen3-235B-A22B (94 layers)}} \\
220	\midrule
221	16 & 17\% & .672 & .659 & .589 & .678 \\
222	32 & 34\% & .738 & .729 & .648 & .751 \\
223	48 & 51\% & .781 & .771 & .658 & .793 \\
224	\textbf{56} & \textbf{60\%} & \textbf{.798} & \textbf{.771} & \textbf{.641} & \textbf{.801} \\
225	64 & 68\% & .816 & .751 & .618 & .788 \\
226	76 & 81\% & .838 & .714 & .584 & .756 \\
227	88 & 94\% & .818 & .671 & .542 & .712 \\
228	\midrule
229	\multicolumn{6}{l}{\emph{Llama 4 Scout (48 layers)}} \\
230	\midrule
231	8  & 17\% & .674 & .661 & --- & --- \\
232	16 & 33\% & .741 & .738 & --- & --- \\
233	\textbf{24} & \textbf{50\%} & \textbf{.788} & \textbf{.756} & --- & --- \\
234	32 & 67\% & .811 & .726 & --- & --- \\
235	40 & 83\% & .821 & .698 & --- & --- \\
236	48 & 100\% & .798 & .654 & --- & --- \\
237	\bottomrule
238	\end{tabular}
239	\caption{Pareto frontier across depth for both architectures. Bold rows indicate the optimal zero-shot transfer layer. EN = English AUROC; ZS = zero-shot transfer AUROC (median across 20 languages). Beyond the optimal transfer layer, EN AUROC continues rising while cross-lingual transfer degrades.}
240	\label{tab:pareto}
241	\end{table}
242	
243	Table~\ref{tab:pareto} presents the depth--transferability Pareto frontier on both architectures.
244	On Qwen3-235B, English AUROC peaks at 0.838 (layer~76, 81\% depth), while the optimal zero-shot transfer layer is layer~56 (60\% depth) with median AUROC 0.771 across 20 languages.
245	Moving from the transfer-optimal layer~56 to the English-optimal layer~76, zero-shot transfer drops from 0.771 to 0.714 ($-5.7$~pp) while English AUROC gains only 4.0~pp.
246	The depth--transfer anticorrelation is robust: Spearman $\rho = -0.78$ (per-language median; IQR $[-0.84, -0.71]$).
247	
248	On Llama~4~Scout, the optimal transfer depth shifts to 50\% (layer~24), with a steeper frontier ($\rho = -0.73$).
249	Scout's shallower optimal depth is consistent with MoE expert routing driving faster language specialization in its 48-layer architecture.
250	17/20 languages achieve zero-shot AUROC $> 0.65$ on Qwen3 (16/20 on Scout).
251	
252	The resource tier strongly modulates transfer quality.
253	On Qwen3 at the optimal layer, high-resource languages (zh: 0.793, es: 0.801) substantially outperform low-resource languages (sw: 0.641, bn: 0.633), consistent with $\mathcal{H}$-divergence predictions from domain adaptation theory.
254	
255	\subsection{CaCLR Evaluation}
256	\label{sec:exp:caclr}
257	
258	\begin{table}[t]
259	\centering
260	\small
261	\begin{tabular}{@{}lccccc@{}}
262	\toprule
263	\textbf{Method} & \textbf{Labels} & \textbf{Q-56} & \textbf{Q-76} & \textbf{S-24} & \textbf{S-40} \\
264	\midrule
265	Zero-shot & 0 & .771 & .714 & .756 & .698 \\
266	Mean-shift & 0 & .771 & .714 & .756 & .698 \\
267	CaCLR$_{\alpha}$ & 0$^*$ & .798 & .762 & .784 & .745 \\
268	\textbf{CaCLR} & \textbf{0$^*$} & \textbf{.828} & \textbf{.788} & \textbf{.812} & \textbf{.771} \\
269	Lin.\ proj.\ (50) & 50 pairs & .812 & .779 & .798 & .758 \\
270	Few-shot 25 & 25 & .798 & .761 & .781 & .741 \\
271	Few-shot 100 & 100 & .821 & .792 & .808 & .778 \\
272	\bottomrule
273	\end{tabular}
274	\caption{Transfer method comparison (median AUROC across 20 languages). Q = Qwen3-235B; S = Llama~4~Scout. Numbers after model indicate layer. $^*$Requires parallel inputs but zero target-language correctness labels. CaCLR$_\alpha$ = $\beta=0$ (no consistency loss).}
275	\label{tab:transfer}
276	\end{table}
277	
278	Table~\ref{tab:transfer} compares all transfer methods.
279	CaCLR achieves median AUROC 0.828 at Qwen3 layer~56 and 0.812 at Scout layer~24---surpassing linear projection by +1.4~pp and nearly matching few-shot 100 ($-0.8$~pp), while requiring zero target-language labels.
280	Mean-shift yields exactly $\Delta\text{AUROC} = 0.000$, confirming our theoretical prediction (Section~\ref{sec:method:transfer}).
281	
282	The $\beta$ term (MMD consistency loss) provides a meaningful gain of +3.2~pp over the $\alpha$-only ablation (bootstrap CI: [0.019, 0.045]; paired permutation $p = 0.003$; Cohen's $d = 0.48$).
283	Table~\ref{tab:beta} shows the $\beta$ sensitivity sweep: $\beta = 0.1$ is optimal, with lower values providing insufficient distributional constraint and $\beta = 1.0$ over-regularizing.
284	
285	\begin{table}[t]
286	\centering
287	\small
288	\begin{tabular}{@{}lccc@{}}
289	\toprule
290	$\beta$ & $\Delta$AUROC & $\Delta$ECE & Note \\
291	\midrule
292	0.001 & +0.008 & $-$0.003 & Negligible \\
293	0.01  & +0.019 & $-$0.008 & Marginal \\
294	\textbf{0.1} & \textbf{+0.032} & $\mathbf{-}$\textbf{0.014} & \textbf{Optimal} \\
295	1.0   & +0.021 & $-$0.011 & Over-regularized \\
296	\bottomrule
297	\end{tabular}
298	\caption{$\beta$ sensitivity sweep (Qwen3-235B, layer~56, median across 20 languages). Deltas are relative to $\alpha$-only ($\beta=0$).}
299	\label{tab:beta}
300	\end{table}
301	
302	The $\beta$ gain is largest at mid-depth layers (+4.1~pp) and diminishes at deep layers (+2.4~pp) and shallow layers (+1.8~pp).
303	This pattern is explained by CKA analysis (Section~\ref{sec:exp:cka}): mid-depth layers have sufficient cross-lingual structure for MMD alignment to be effective, while deep-layer misalignment is geometric (directional rotation) rather than merely distributional.
304	
305	CaCLR reduces non-English ECE by a median of 3.5\% over temperature scaling (range: [1.2\%, 6.1\%]).
306	Temperature scaling achieves English ECE of 0.048 (Qwen3) and 0.053 (Scout) from raw ECE of 0.162 and 0.171 respectively, but cannot address cross-lingual representation misalignment.
307	CaCLR directly optimizes calibration during training via the SB-ECE term.
308	
309	\subsection{Difficulty--Capability Decomposition}
310	\label{sec:exp:decomp}
311	
312	\begin{table}[t]
313	\centering
314	\small
315	\begin{tabular}{@{}lcccc@{}}
316	\toprule
317	\textbf{Depth} & \textbf{HIGH} & \textbf{MID} & \textbf{LOW} & \textbf{Random} \\
318	\midrule
319	20\% & +.012 & +.014 & +.019 & +.001 \\
320	35\% & +.016 & +.022 & +.028 & +.002 \\
321	50\% & +.021 & +.031 & +.038 & +.002 \\
322	60\% & +.024 & +.036 & +.043 & +.003 \\
323	80\% & +.028 & +.041 & +.048 & +.003 \\
324	90\% & +.022 & +.034 & +.041 & +.002 \\
325	\bottomrule
326	\end{tabular}
327	\caption{$\Delta$AUROC after difficulty direction removal, by resource tier and depth. Random = random direction control. Difficulty removal consistently improves transfer, especially for low-resource languages at deep layers.}
328	\label{tab:decomp}
329	\end{table}
330	
331	Table~\ref{tab:decomp} shows the decomposition results.
332	Removing the difficulty direction from representations before training correctness probes improves cross-lingual transfer by a median of 3.1~pp (bootstrap CI: [1.8, 4.4]; $p = 0.006$; $d = 0.41$).
333	The difficulty direction has moderate cosine similarity with the correctness direction (0.34), confirming partial signal overlap without full redundancy.
334	The difficulty probe achieves $R^2 = 0.68$, validating that difficulty is linearly accessible in the representation space.
335	
336	Two patterns emerge.
337	First, a resource-tier gradient: low-resource languages benefit most from decomposition (+4.1~pp) versus high-resource (+2.2~pp), because low-resource languages have greater difficulty distribution mismatch with English.
338	Second, a depth gradient: deep-layer benefit (4.8~pp at 80\% depth) exceeds shallow-layer benefit (0.8~pp at 20\%), because deep layers encode more language-specific difficulty information.
339	The random-direction control yields only +0.2~pp, ruling out dimensionality reduction as a confound.
340	
341	\subsection{Cross-Lingual Orthogonality}
342	\label{sec:exp:ortho}
343	
344	\begin{table}[t]
345	\centering
346	\small
347	\begin{tabular}{@{}llccc@{}}
348	\toprule
349	\textbf{Lang} & \textbf{Tier} & \textbf{Qwen3} & \textbf{Scout} & \textbf{Mean} \\
350	\midrule
351	en & HIGH & .031 & .037 & .034 \\
352	zh & HIGH & .035 & .041 & .038 \\
353	es & HIGH & .033 & .039 & .036 \\
354	de & HIGH & .036 & .042 & .039 \\
355	hi & MID  & .039 & .045 & .042 \\
356	ru & MID  & .037 & .043 & .040 \\
357	ko & MID  & .041 & .047 & .044 \\
358	tr & MID  & .043 & .049 & .046 \\
359	sw & LOW  & .048 & .056 & .052 \\
360	bn & LOW  & .052 & .058 & .055 \\
361	\bottomrule
362	\end{tabular}
363	\caption{Correctness--confidence cosine similarity across languages and architectures. All values remain below 0.062, confirming universal near-orthogonality.}
364	\label{tab:ortho}
365	\end{table}
366	
367	Table~\ref{tab:ortho} reports correctness--confidence cosine similarity across languages.
368	All 20 languages on both architectures show cosine similarity below 0.062 (mean = 0.042; bootstrap CI for mean: [0.035, 0.049]).
369	This extends the English-only finding of Miao \& Ungar to a universal structural property: verbalized confidence is uninformative about correctness regardless of language or architecture.
370	
371	A mild resource-tier gradient exists: low-resource languages show slightly higher cosine (0.051 vs.\ 0.038 for high-resource), likely reflecting noisier confidence direction estimates from sparser training data rather than genuine reduction in orthogonality.
372	Qwen3 exhibits slightly stronger orthogonality than Scout (mean 0.039 vs.\ 0.046), possibly because its larger capacity encodes correctness and confidence in more separable subspaces.
373	
374	\subsection{CKA Representation Similarity Analysis}
375	\label{sec:exp:cka}
376	
377	\begin{table}[t]
378	\centering
379	\small
380	\begin{tabular}{@{}lcccc@{}}
381	\toprule
382	\textbf{Depth} & \textbf{HIGH} & \textbf{MID} & \textbf{LOW} & \textbf{ZS AUROC} \\
383	\midrule
384	10\% & .93 & .89 & .84 & .618 \\
385	25\% & .90 & .85 & .78 & .698 \\
386	40\% & .86 & .79 & .69 & .756 \\
387	50\% & .82 & .74 & .62 & .771 \\
388	60\% & .78 & .69 & .55 & .771 \\
389	70\% & .73 & .63 & .47 & .741 \\
390	80\% & .67 & .56 & .41 & .714 \\
391	90\% & .61 & .49 & .35 & .688 \\
392	\bottomrule
393	\end{tabular}
394	\caption{CKA similarity (EN vs.\ target, Qwen3-235B) by depth and resource tier, alongside zero-shot transfer AUROC. CKA monotonically decreases with depth and correlates strongly with transfer success.}
395	\label{tab:cka}
396	\end{table}
397	
398	Table~\ref{tab:cka} presents CKA similarity between English and target-language representations across depth.
399	CKA monotonically decreases with depth across all resource tiers, and correlates strongly with zero-shot transfer AUROC (Pearson $r = 0.82$; CI: [0.76, 0.87]; Spearman $\rho = 0.79$).
400	This provides a mechanistic explanation for the Pareto frontier: deeper layers have progressively less cross-lingual representational overlap, directly causing transfer degradation.
401	
402	The resource-tier gradient in CKA mirrors the transfer gradient: high-resource languages maintain CKA $\geq 0.61$ even at 90\% depth, while low-resource languages drop to 0.35.
403	This reflects pretraining data overlap---languages with more shared tokens develop more similar deep representations.
404	
405	Critically, the CKA analysis reveals why CaCLR's $\beta$ term has depth-dependent effectiveness.
406	At layers where CKA $< 0.55$, the $\beta$ term provides diminishing returns because misalignment becomes \emph{geometric} (the correctness direction rotates 15--35$^\circ$ across languages) rather than merely distributional (mean/covariance shift).
407	MMD corrects distributional shift but cannot learn rotations; this explains why linear projection---which explicitly learns a rotation matrix---remains effective at deep layers.
408	At mid-depth layers (CKA $\approx 0.62$--$0.78$), misalignment is primarily distributional, and CaCLR's MMD term effectively closes the gap.
409	
410	\subsection{Probe Complexity}
411	\label{sec:exp:probe}
412	
413	\begin{table}[t]
414	\centering
415	\small
416	\begin{tabular}{@{}lcccc@{}}
417	\toprule
418	\textbf{Layer} & \textbf{LR-EN} & \textbf{MLP-EN} & \textbf{LR-ZS} & \textbf{MLP-ZS} \\
419	\midrule
420	24 & .711 & .722 & .698 & .691 \\
421	40 & .762 & .778 & .756 & .741 \\
422	56 & .798 & .814 & .771 & .752 \\
423	76 & .838 & .852 & .714 & .686 \\
424	\bottomrule
425	\end{tabular}
426	\caption{Logistic regression (LR) vs.\ 2-layer MLP on Qwen3-235B. MLP achieves higher English AUROC but worse zero-shot transfer, with the gap widening at deeper layers.}
427	\label{tab:probe}
428	\end{table}
429	
430	Table~\ref{tab:probe} compares logistic regression and 2-layer MLP probes.
431	MLPs achieve +1.4~pp higher English AUROC but suffer 3.6~pp worse zero-shot transfer degradation (median), yielding a net transfer advantage of +2.2~pp for logistic regression.
432	The gap widens at deeper layers (LR advantage: +0.7~pp at layer~24 vs.\ +2.8~pp at layer~76), because deep-layer representations are more language-specific and MLP's extra capacity overfits to English-specific patterns.
433	Logistic regression's linear inductive bias matches the linear structure of correctness directions, supporting its use as the default probe.
434	
435	\subsection{Cross-Benchmark Generalization}
436	\label{sec:exp:benchmark}
437	
438	\begin{table}[t]
439	\centering
440	\small
441	\begin{tabular}{@{}lcccc@{}}
442	\toprule
443	\textbf{Benchmark} & \textbf{ZS} & \textbf{CaCLR} & $\rho$ & \textbf{$>$0.65} \\
444	\midrule
445	GlobalMMLU & .758 & .808 & $-$.78 & 17/20 \\
446	Belebele & .731 & .789 & $-$.71 & 15/20 \\
447	MMLU-ProX & .748 & .801 & $-$.75 & 16/20 \\
448	\bottomrule
449	\end{tabular}
450	\caption{Cross-benchmark generalization (Qwen3-235B, optimal transfer layer). ZS = zero-shot median AUROC; $\rho$ = Pareto Spearman correlation; $>$0.65 = languages above 0.65 AUROC.}
451	\label{tab:benchmark}
452	\end{table}
453	
454	Table~\ref{tab:benchmark} shows that all findings generalize across benchmarks.
455	The Pareto frontier persists on Belebele ($\rho = -0.71$) and MMLU-ProX ($\rho = -0.75$).
456	CaCLR provides consistent improvement on both (+5.8~pp on Belebele, +5.3~pp on MMLU-ProX).
457	Cross-benchmark per-language correlation is 0.92, indicating that transfer difficulty is language-inherent rather than benchmark-specific.
458	
459	\subsection{Linear Projection Data Efficiency}
460	\label{sec:exp:linproj}
461	
462	\begin{table}[t]
463	\centering
464	\small
465	\begin{tabular}{@{}lccccc@{}}
466	\toprule
467	\textbf{Pairs} & \textbf{Med.} & $\Delta$\textbf{ZS} & \textbf{\%200} & \textbf{HIGH} & \textbf{LOW} \\
468	\midrule
469	10  & .762 & +.027 & 88\% & .781 & .638 \\
470	20  & .778 & +.043 & 94\% & .798 & .651 \\
471	50  & .792 & +.057 & 98\% & .814 & .664 \\
472	100 & .796 & +.061 & 99\% & .818 & .668 \\
473	200 & .798 & +.063 & 100\% & .821 & .671 \\
474	\bottomrule
475	\end{tabular}
476	\caption{Linear projection data efficiency. Performance saturates at $\sim$35 pairs (95\% of 200-pair performance), with low-resource languages requiring slightly more pairs (48 vs.\ 22 for high-resource).}
477	\label{tab:linproj}
478	\end{table}
479	
480	Linear projection saturates rapidly: 50 parallel pairs achieve 98\% of 200-pair performance (Table~\ref{tab:linproj}).
481	This reflects the low intrinsic dimensionality of the correctness direction---a rotation/scaling matrix between low-dimensional subspaces needs few examples to estimate.
482	Low-resource languages saturate later (48 vs.\ 22 pairs), consistent with noisier correctness direction estimates.
483	CaCLR outperforms 50-pair linear projection by +1.4~pp while requiring no paired data beyond parallel inputs.
484	
485	
486	%---------------------------------------------------------------
487	\section{Discussion}
488	\label{sec:discussion}
489	%---------------------------------------------------------------
490	
491	\paragraph{Why architecture matters.}
492	The architecture-dependent Pareto shape is not predicted by domain adaptation theory alone.
493	MoE models exhibit sharper frontiers because expert routing creates discrete language specialization at depth: specific experts become ``responsible'' for specific languages, accelerating representational divergence.
494	Dense models (Gemma~4~31B; Appendix~\ref{app:gemma}) show smoother frontiers ($\rho = -0.69$, optimal transfer at 75\% depth), confirming that expert routing is the mechanism.
495	
496	\paragraph{When CaCLR works and when it does not.}
497	CaCLR is most effective at mid-depth layers where cross-lingual misalignment is distributional.
498	At deep layers (CKA $< 0.55$), geometric misalignment dominates and linear projection is preferable.
499	This provides a practical guideline: use CKA to predict which layer--language combinations will benefit from CaCLR versus requiring geometric alignment.
500	
501	\paragraph{The role of resource tier.}
502	Low-resource languages consistently show (1)~lower zero-shot transfer, (2)~greater benefit from difficulty decomposition, (3)~greater benefit from CaCLR, and (4)~slightly weaker orthogonality.
503	All patterns are consistent with sparser pretraining representation creating larger distributional gaps that alignment methods can partially close.
504	
505	\paragraph{Limitations.}
506	Our evaluation uses MCQA benchmarks, which enable clean correctness labeling but may not reflect open-ended generation.
507	CaCLR requires parallel inputs (translated items), which are readily available for MCQA but less natural for other tasks.
508	INT8 quantization introduces small but nonzero perturbations (max $\Delta$AUROC = 0.6~pp; Appendix~\ref{app:int8}).
509	
510	%---------------------------------------------------------------
511	\section{Conclusion}
512	\label{sec:conclusion}
513	%---------------------------------------------------------------
514	
515	We presented the first systematic study of cross-lingual correctness probe transfer.
516	Our findings form a coherent causal chain: (1)~a depth--transferability Pareto frontier exists with architecture-dependent shape; (2)~difficulty--capability decomposition explains the frontier and identifies where alignment is needed; (3)~CaCLR shifts the frontier via distributional alignment, reducing non-English ECE by 3.5\% over temperature scaling with zero target-language labels across 20 languages; (4)~correctness--confidence orthogonality universally bounds output-based calibration.
517	CKA analysis provides the mechanistic glue, linking representation geometry to transfer success and explaining CaCLR's depth-dependent effectiveness.
518	These results establish probe-based calibration as viable for multilingual settings and provide actionable guidelines for practitioners: select layers based on the architecture-specific Pareto frontier, apply CaCLR at mid-depth layers, and use linear projection when geometric misalignment dominates.
519	
520	%---------------------------------------------------------------
521	
522	\appendix
523	
524	\section{INT8 Validation}
525	\label{app:int8}
526	
527	\begin{table}[h]
528	\centering
529	\small
530	\begin{tabular}{@{}lcccc@{}}
531	\toprule
532	\textbf{Layer} & \textbf{INT8} & \textbf{FP16} & $\Delta$ & \textbf{Cos.} \\
533	\midrule
534	8  & .674 & .678 & $-$.004 & .991 \\
535	16 & .741 & .745 & $-$.004 & .989 \\
536	24 & .788 & .791 & $-$.003 & .992 \\
537	32 & .811 & .814 & $-$.003 & .990 \\
538	40 & .821 & .827 & $-$.006 & .987 \\
539	\bottomrule
540	\end{tabular}
541	\caption{INT8 vs.\ FP16 on Llama~4~Scout. Cos.\ = cosine similarity between extracted correctness directions. All differences are within bootstrap noise.}
542	\label{tab:int8}
543	\end{table}
544	
545	INT8 quantization has negligible impact on correctness probes (Table~\ref{tab:int8}).
546	Maximum AUROC difference is 0.6~pp (layer~40), and correctness direction cosine similarity exceeds 0.987 at all layers.
547	ECE differences are similarly small (max 0.8~pp).
548	
549	\section{Probing Control Tasks}
550	\label{app:control}
551	
552	\begin{table}[h]
553	\centering
554	\small
555	\begin{tabular}{@{}lcccc@{}}
556	\toprule
557	\textbf{Layer} & \textbf{EN Sel.} & \textbf{ZH Sel.} & \textbf{SW Sel.} & \textbf{Ctrl.} \\
558	\midrule
559	16 & .248 & .231 & .192 & .512 \\
560	32 & .281 & .268 & .218 & .519 \\
561	48 & .309 & .292 & .241 & .524 \\
562	56 & .318 & .301 & .248 & .521 \\
563	76 & .341 & .324 & .262 & .538 \\
564	\bottomrule
565	\end{tabular}
566	\caption{Selectivity (probe AUROC $-$ control AUROC) on Qwen3-235B. Ctrl.\ = control task AUROC (random labels). Minimum selectivity is 0.192, well above the 0.15 threshold.}
567	\label{tab:control}
568	\end{table}
569	
570	Following Hewitt \& Liang (2019), we validate probe selectivity with random-label control tasks (Table~\ref{tab:control}).
571	Control AUROC ranges from 0.502 to 0.538 (near chance).
572	Selectivity (probe AUROC minus control AUROC) has a median of 0.284 and minimum of 0.192, well above the 0.15 threshold.
573	This confirms that probes extract genuine correctness signals rather than exploiting high-dimensional capacity.
574	
575	\section{Three-Architecture Comparison}
576	\label{app:gemma}
577	
578	\begin{table}[h]
579	\centering
580	\small
581	\begin{tabular}{@{}llccccc@{}}
582	\toprule
583	\textbf{Model} & \textbf{Type} & \textbf{EN} & \textbf{ZS} & \textbf{Opt.\%} & $\rho$ \\
584	\midrule
585	Qwen3-235B & MoE & .838 & .758 & 60\% & $-$.78 \\
586	Llama 4 Scout & MoE & .821 & .742 & 50\% & $-$.73 \\
587	Gemma 4 31B & Dense & .809 & .738 & 75\% & $-$.69 \\
588	\bottomrule
589	\end{tabular}
590	\caption{Three-architecture comparison. Dense architecture (Gemma~4) shows a smoother frontier with deeper optimal transfer, consistent with expert routing driving sharper language specialization in MoE models.}
591	\label{tab:arch}
592	\end{table}
593	
594	Adding Gemma~4~31B Dense as a camera-ready extension confirms that MoE architectures produce sharper Pareto frontiers than dense models (Table~\ref{tab:arch}).
595	Gemma's optimal transfer depth is 75\% (vs.\ 60\% and 50\% for the MoE models), and its Pareto $\rho = -0.69$ indicates a smoother frontier with no sharp elbow, consistent with gradual rather than discrete language specialization.
596	
597	\section{Extended Language Coverage}
598	\label{app:extended}
599	
600	\begin{table}[h]
601	\centering
602	\small
603	\begin{tabular}{@{}lcccc@{}}
604	\toprule
605	\textbf{Tier} & $n$ & \textbf{ZS} & \textbf{CaCLR} & $\Delta$ \\
606	\midrule
607	HIGH & 12 & .786 & .828 & +.042 \\
608	MID & 18 & .741 & .798 & +.057 \\
609	LOW & 22 & .648 & .721 & +.073 \\
610	\bottomrule
611	\end{tabular}
612	\caption{Extended coverage (52 languages). CaCLR benefit increases with decreasing resource tier.}
613	\label{tab:extended}
614	\end{table}
615	
616	Expanding to 52 languages confirms all findings at scale (Table~\ref{tab:extended}).
617	CaCLR generalizes across the full language set, with low-resource languages benefiting most (+7.3~pp vs.\ +4.2~pp for high-resource).
618	38/52 languages (73\%) achieve zero-shot AUROC above 0.65; the Pareto frontier and CaCLR improvements remain robust.
619	
620	\bibliographystyle{plainnat}
621	\bibliography{references}
622	
623	\end{document}
624	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "648c33dd-457a-43d5-9c02-961bff1ec92a",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "09c222a6-a25d-4d8b-b076-8ecaf5aab587",
  "sourceToolAssistantUUID": "648c33dd-457a-43d5-9c02-961bff1ec92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T21:07:00.298Z_

Now let me also check the previous dream review reports to understand what issues were already identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09c222a6-a25d-4d8b-b076-8ecaf5aab587",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW71ysXdrxpQirgTiQT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "528f9332-9d1a-4512-b6a2-68b40bbd49fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119c1pZUj3PigyhWjnDqv4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8883,
      "cache_read_input_tokens": 55459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8883,
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

_source line 34 · 2026-05-20T21:07:02.531Z_

<details open><summary>🔧 Tool call — Read · `toolu_013mYGDFmALP4XF8PsWSRYZy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "528f9332-9d1a-4512-b6a2-68b40bbd49fe",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW71ysXdrxpQirgTiQT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ce31cea-9227-4624-bb66-10d56ba36a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119c1pZUj3PigyhWjnDqv4K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8883,
      "cache_read_input_tokens": 55459,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 55459,
          "cache_creation_input_tokens": 8883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8883,
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

_source line 35 · 2026-05-20T21:07:02.536Z_

<details><summary>↩ Tool result · `toolu_013mYGDFmALP4XF8PsWSRYZy`</summary>

```text
1	---
2	dream_id: dream_20260520T201854
3	tier: best
4	overall_score: weak accept (4/6)
5	timestamp: 2026-05-20T21:05:06.249123+00:00
6	---
7	
8	# Dream Review Report — Cross-Lingual Calibration via Internal Correctness Directions
9	
10	**dream_id**: 20260520T201854  
11	**Review mode**: full (2 Reviewers + Roundtable)  
12	**Date**: 2026-05-20
13	
14	---
15	
16	## Panel Summary
17	
18	| Reviewer | Focus | Score | Confidence |
19	|----------|-------|-------|------------|
20	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/5 |
21	| R2 | Novelty + Related Work | 4/6 (Weak Accept) | 4/5 |
22	| **Consensus** | | **4/6 (Weak Accept)** | **4/5** |
23	
24	---
25	
26	## 1. Paper Overview
27	
28	The paper presents the first systematic study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B-A22B, Llama 4 Scout). It discovers a depth–transferability Pareto frontier (architecture-dependent), proposes CaCLR (a consistency-aligned probe training objective), decomposes correctness transfer into difficulty-shared and capability-specific components, and confirms universal correctness–confidence orthogonality. CKA analysis provides mechanistic explanation linking representation geometry to transfer success.
29	
30	---
31	
32	## 2. Strengths (Consensus)
33	
34	**S1. Ambitious scope and thorough experimental design.** The paper covers 20 languages × 2 architectures × multiple transfer conditions × 3 benchmarks, with appropriate ablations (INT8, probe complexity, control tasks, β sweep). The experimental pipeline is comprehensive for a single paper. [Both R1, R2]
35	
36	**S2. Strong analytical contributions.** The difficulty–capability decomposition is methodologically interesting and well-controlled (random-direction control validates specificity). The mean-shift invariance proof (ΔAUROC ≡ 0 under StandardScaler + LR) is a clean theoretical result that corrects prior work's implicit assumption that mean-shift helps. The CKA analysis provides a quantitative bridge between representation geometry and transfer outcomes. [Both R1, R2]
37	
38	**S3. Coherent narrative structure.** The "causal chain" framing (Pareto frontier → decomposition explains frontier → CaCLR shifts frontier → orthogonality bounds alternatives) is well-structured and easy to follow, even if individual links vary in strength. [R2]
39	
40	**S4. Statistical rigor where applied.** Bootstrap CIs, paired permutation tests, and Cohen's d for CaCLR β effect (p=0.003, d=0.48) and decomposition (p=0.006, d=0.41) demonstrate appropriate statistical practice. [R1]
41	
42	**S5. Practical value of mean-shift and orthogonality results.** The mean-shift invariance proof saves practitioners from a common but ineffective alignment attempt. The universal orthogonality finding (cosine < 0.062 across 20 languages) establishes a clear boundary condition for output-based calibration approaches. [Both R1, R2]
43	
44	---
45	
46	## 3. Weaknesses (Consensus + Individual)
47	
48	### Major Weaknesses
49	
50	**W1. CaCLR's practical advantage over linear projection is marginal.** [Both R1, R2]
51	CaCLR beats 50-pair linear projection by only +1.4pp median AUROC while requiring: (a) parallel inputs for all target languages (not just 50 pairs), (b) gradient-based training with a 3-term composite loss, (c) hyperparameter tuning (α, β). Meanwhile, linear projection needs only 50 translated pairs (trivial to obtain) and a simple matrix fit. CaCLR also slightly underperforms few-shot 100 (−0.8pp). The cost-benefit calculus is unfavorable for the headline method contribution.
52	
53	**W2. Architecture-dependence claim is underpowered and confounded.** [Both R1, R2]
54	The three models differ simultaneously in architecture type (MoE vs dense), scale (235B vs 109B vs 31B), depth (94 vs 48 vs 60 layers), active parameters (22B vs 17B vs 31B), and training data. Attributing the Pareto frontier shape to "MoE expert routing" is not supported by the experimental design — no controlled comparison isolates architecture type. The claim that "expert routing accelerates deep-layer language specialization" is speculative without direct evidence (e.g., expert activation analysis, routing entropy by language). Three confounded data points cannot support causal claims about architecture.
55	
56	**W3. Pareto frontier is undersampled in the paper.** [R1]
57	The design planned 24 probed layers for Qwen3 (every 4th), but Table 1 reports only 7. This is sufficient to see the trend but insufficient to precisely locate the frontier elbow or detect non-monotonicity. For Scout, ZS Min/Max columns are omitted entirely. The full 24-layer × 20-language results should be available if the experiments were run — why not report them?
58	
59	**W4. CKA analysis is correlational despite "mechanistic" framing.** [Both R1, R2]
60	The paper claims CKA "mechanistically explains" the Pareto frontier, but the analysis is purely correlational. Depth is a confounder: CKA decreases with depth, and so does transfer AUROC, but both could be driven by the same underlying cause (progressive specialization) rather than CKA causally determining transfer. The r=0.82 correlation likely inflates the true relationship because it pools across resource tiers and depths, mixing between-group and within-group variation. A partial correlation controlling for depth would be more informative. "Mechanistic" implies causal understanding; "correlational evidence consistent with" would be more accurate.
61	
62	**W5. Missing important references and insufficient differentiation.** [R2]
63	- Conneau et al. (2020) "What you can cram into a single $&!#\* vector" — established the depth–language-specificity tradeoff in multilingual transformers. The Pareto frontier is a quantitative refinement of this known phenomenon.
64	- Pires et al. (2019) on mBERT cross-lingual transfer — foundational context missing.
65	- Civelli et al. are cited but insufficiently compared — they already showed architecture-dependent optimal depth for cross-lingual probes.
66	- Gretton et al. (2012) for MMD — the foundational MMD paper should be cited and the kernel choice specified.
67	- DAN, DANN, and other domain adaptation methods using MMD-like losses — CaCLR's MMD term is closely related to these classical approaches.
68	
69	### Minor Weaknesses
70	
71	**W6. Selective statistical reporting.** [R1]
72	Bootstrap CIs are reported for CaCLR β effect and decomposition but not for the Pareto frontier (ρ values), orthogonality measurements, or CKA correlations (except CKA-transfer r). The CKA-transfer CI is reported [0.76, 0.87] but this is a marginal CI that doesn't account for the depth confound. Multiple comparison corrections are absent across the many language × layer × model comparisons.
73	
74	**W7. Orthogonality table is incomplete.** [R1]
75	Table 5 shows only 10 of 20 languages. The claim "all 20 languages below 0.062" is made in text but the evidence is only half-shown. This is a central claim — full data should be in the paper or a detailed appendix.
76	
77	**W8. INT8 validation is incomplete.** [R1]
78	INT8 vs FP16 comparison covers only Scout (5 layers, 5% subset). Qwen3-235B — the primary model — has no quantization validation. Given that Qwen3 is the larger model and quantization effects may scale with model size, this gap weakens claims based on Qwen3 results.
79	
80	**W9. Non-English ECE improvements reported only in relative terms.** [R2]
81	The headline "3.5% ECE reduction over temperature scaling" is not accompanied by absolute ECE values for non-English languages. Without knowing the baseline non-English ECE (after temp scaling), it's impossible to assess practical significance. If non-English temp-scaled ECE is ~0.10, then 3.5pp reduction to 0.065 is meaningful. If it's ~0.30, then 3.5pp is marginal.
82	
83	**W10. Causal chain has a weak link.** [R2]
84	The decomposition (contribution 2) shows difficulty entanglement degrades transfer, but CaCLR (contribution 3) uses MMD distributional alignment, not difficulty removal. The narrative implies decomposition motivates CaCLR, but the connection is indirect — CaCLR doesn't operationalize the decomposition insight. A stronger design would use difficulty-removed representations as input to CaCLR, or compare CaCLR with and without difficulty removal.
85	
86	**W11. Results appear suspiciously clean.** [R1]
87	Mean-shift yields exactly ΔAUROC = 0.000 (the theoretical prediction), orthogonality values are perfectly tiered by resource level with no outliers, the Pareto frontier shows perfectly monotonic trends in most sub-analyses, and the β sweep produces a textbook inverted-U. While individually each is possible, the collective perfection raises concerns about whether results were curated or cherry-picked.
88	
89	---
90	
91	## 4. Experiment Coverage Assessment
92	
93	Comparing the paper against the 11 planned experiments:
94	
95	| Experiment | In Paper? | Completeness |
96	|-----------|-----------|--------------|
97	| plan_001: Qwen3 Pareto | ✓ Table 1 | Partial — 7/24 layers shown |
98	| plan_002: Scout Pareto | ✓ Table 1 | Partial — ZS Min/Max omitted |
99	| plan_003: CaCLR | ✓ Tables 2-3 | Partial — α sweep missing, only 1 layer for β sweep |
100	| plan_004: Decomposition | ✓ Table 4 | Good — 6 depths × 3 tiers + control |
101	| plan_005: Orthogonality | ✓ Table 5 | Partial — 10/20 languages shown |
102	| plan_006: Probe Complexity | ✓ Table 7 | Good — 4 layers, clear pattern |
103	| plan_007: Benchmarks | ✓ Table 8 | Adequate — 3 benchmarks, summary stats |
104	| plan_010: INT8 | ✓ Table 10 | Partial — Scout only, not Qwen3 |
105	| plan_011: CKA | ✓ Table 6 | Good — 8 depths × 3 tiers |
106	| plan_012: Linear Proj | ✓ Table 9 | Good — 5 pair counts × tier breakdown |
107	| plan_013: Control Tasks | ✓ Table 11 | Adequate — 5 layers × 3 languages |
108	| plan_008: Gemma 4 (ext) | ✓ Table 12 | Summary only (appendix) |
109	| plan_009: 52-lang (ext) | ✓ Table 13 | Summary only (appendix) |
110	
111	All planned experiments have corresponding tables, but several are reported at reduced resolution compared to the design. The most significant gap is the Pareto frontier sub-sampling (7/24 layers for Qwen3). The α sweep (planned in plan_003) is absent from the paper despite being designed.
112	
113	---
114	
115	## 5. Questions for Authors
116	
117	1. **Why report only 7/24 probed layers for Qwen3 in Table 1?** If all 24 were probed, the full data should be available. Was there a data issue, or was this a presentation choice? The full layer-wise results would significantly strengthen the frontier claim.
118	
119	2. **Can you provide absolute ECE values for non-English languages?** The "3.5% reduction" headline needs context. What are the per-tier median ECE values before and after CaCLR?
120	
121	3. **What kernel is used for MMD in CaCLR?** Gaussian RBF? Linear? What bandwidth selection? This is essential for reproducibility and affects the distributional vs. geometric alignment distinction.
122	
123	4. **How is CaCLR trained in practice?** The paper states probes are logistic regression, but CaCLR requires gradient-based optimization of a 3-term loss. Is this still a single-layer linear model trained with SGD? What optimizer, learning rate, training epochs?
124	
125	5. **Can you isolate the architecture effect?** E.g., compare two models of similar scale but different architecture type, or analyze expert routing patterns directly (routing entropy by language across depth)?
126	
127	6. **Why does the decomposition not feed into CaCLR?** If difficulty entanglement is the identified problem, why doesn't CaCLR operate on difficulty-removed representations? What is the CaCLR result on decomposed representations?
128	
129	7. **For Table 5, can you show all 20 languages?** The orthogonality claim is central — half the evidence is hidden.
130	
131	8. **How sensitive is the optimal transfer depth to the specific benchmark or prompt template?** The 60% vs 50% numbers are presented as architecture properties, but could they be benchmark-specific?
132	
133	---
134	
135	## 6. Reviewer Discussion and Convergence
136	
137	### Points of Agreement
138	- **Score**: Both R1 and R2 independently scored 4/6 (Weak Accept).
139	- **CaCLR's marginal practical value**: Both reviewers flagged the +1.4pp advantage over linear projection as insufficient to justify CaCLR's complexity.
140	- **Architecture claim underpowered**: Both noted the 3-model comparison confounds architecture with scale, depth, and training data.
141	- **Analytical > methodological strength**: Both agree the paper's strongest contributions are the analytical results (decomposition, CKA, orthogonality, mean-shift proof) rather than CaCLR.
142	- **CKA overclaimed**: Both flag the "mechanistic" framing as overstated for a correlational analysis.
143	
144	### Points of Divergence
145	- **R1** emphasizes experimental reporting gaps (subsampled tables, missing statistical tests, incomplete INT8 validation) and flags suspiciously clean results.
146	- **R2** emphasizes novelty positioning (many findings are quantitative refinements of known phenomena) and missing foundational references.
147	- R1 is more concerned about reproducibility (unspecified MMD details); R2 is more concerned about the causal chain's logical coherence.
148	
149	### Convergence
150	After cross-review, both reviewers maintain 4/6. The paper represents solid empirical work at scale with genuine analytical insights, but the headline method contribution (CaCLR) is underwhelming, and several claims are overstated relative to the evidence. The paper would benefit from: (a) reframing as primarily an analysis/characterization paper, (b) filling reporting gaps, and (c) qualifying the architecture-dependent and "mechanistic" claims.
151	
152	---
153	
154	## 7. Consolidated Assessment
155	
156	### Overall Score: 4/6 (Weak Accept)
157	
158	**Rationale**: The paper tackles a genuinely important problem (multilingual calibration) with impressive scale (20 languages, 2-3 architectures, 3 benchmarks) and produces several analytically valuable findings. The Pareto frontier quantification, difficulty–capability decomposition, universal orthogonality confirmation, and mean-shift invariance proof each contribute to the field's understanding. Statistical testing is applied to key claims. The experimental scope goes well beyond what most papers attempt.
159	
160	However, the headline method contribution (CaCLR) provides only marginal improvement over a simpler baseline (linear projection) at substantially higher cost, the architecture-dependence claim lacks controlled evidence, key results are underreported (7/24 layers, 10/20 languages), and the "mechanistic" framing of correlational CKA analysis is overstated. The paper would be strengthened by: (1) repositioning CaCLR as one tool in a practitioner's toolkit rather than the primary contribution, (2) foregrounding the analytical discoveries, and (3) filling the reporting gaps.
161	
162	**Accept if**: Authors reframe emphasis from CaCLR to analytical contributions, fill reporting gaps (full layer/language tables), qualify architecture-dependence and "mechanistic" claims, and provide absolute ECE values.
163	
164	**Reject if**: Authors insist on CaCLR as the primary contribution without addressing the cost-benefit comparison with linear projection, or if the subsampled results hide problematic patterns in the full data.
165	
166	### Confidence: 4/5
167	Reviewers are familiar with calibration, probing, and cross-lingual transfer literature. Some uncertainty about whether INT8 quantization concerns or CKA confounds would change conclusions if addressed.
168	
169	---
170	
171	## 8. Actionable Recommendations for Revision
172	
173	1. **Report full results**: Show all 24 probed layers for Qwen3, all 12 for Scout, all 20 languages for orthogonality. Move to appendix if space-constrained, but reference explicitly.
174	2. **Provide absolute ECE**: Include per-tier median ECE values (raw, temp-scaled, CaCLR) for non-English languages.
175	3. **Specify MMD details**: Kernel type, bandwidth, optimizer, and training procedure for CaCLR.
176	4. **Qualify architecture claims**: Replace "MoE expert routing causes..." with "consistent with MoE expert routing contributing to..." unless routing analysis is added.
177	5. **Qualify CKA framing**: Replace "mechanistically explains" with "provides correlational evidence consistent with" or add partial correlation controlling for depth.
178	6. **Add α sweep to paper**: The design planned it; its absence is notable.
179	7. **Reframe contributions**: Lead with the analytical discoveries (Pareto frontier, decomposition, orthogonality); position CaCLR as a demonstrated application of the analysis insights rather than the headline.
180	8. **Add missing references**: Conneau et al. (2020), Pires et al. (2019), Gretton et al. (2012), and relevant domain adaptation methods using MMD.
181	9. **Connect decomposition to CaCLR**: Test CaCLR on difficulty-removed representations to close the causal chain link.
182	10. **INT8 validation on Qwen3**: Even a small-scale validation (5 layers, subset) would address concerns about the primary model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ce31cea-9227-4624-bb66-10d56ba36a73",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "59e3667e-5471-4025-bab5-b52387396906",
  "sourceToolAssistantUUID": "5ce31cea-9227-4624-bb66-10d56ba36a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T21:07:06.915Z_

Now I have a thorough understanding of the paper, its experimental design, the review context, and the prior review. Let me now load the submit tool and write my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e3667e-5471-4025-bab5-b52387396906",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW7PPj3sPLJrt5kjpfo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3302a400-dba8-4332-9a79-a0aced23470e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ekw8G5oweALZfPb3rcuVr6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4961,
      "cache_read_input_tokens": 64342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4961,
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

_source line 37 · 2026-05-20T21:07:07.805Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ab7UGJDARsV7ur8JzJZsKH`</summary>

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
  "parentUuid": "3302a400-dba8-4332-9a79-a0aced23470e",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW7PPj3sPLJrt5kjpfo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f297dea-8f05-4cd9-912d-9ffc1ef7f9a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ekw8G5oweALZfPb3rcuVr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4961,
      "cache_read_input_tokens": 64342,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4961
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 64342,
          "cache_creation_input_tokens": 4961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4961,
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

_source line 38 · 2026-05-20T21:07:07.811Z_

<details><summary>↩ Tool result · `toolu_01Ab7UGJDARsV7ur8JzJZsKH`</summary>

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
  "parentUuid": "3f297dea-8f05-4cd9-912d-9ffc1ef7f9a3",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "17181561-56d4-455e-b2c3-fcf79937cb49",
  "sourceToolAssistantUUID": "3f297dea-8f05-4cd9-912d-9ffc1ef7f9a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T21:07:10.581Z_



Now I have all the information needed to write a thorough R1 review focused on methods and experiments. Let me compose and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17181561-56d4-455e-b2c3-fcf79937cb49",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW7mqME47ZYgE9AxMby",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f483456-b7b5-4a34-998f-df0e37a5b514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V22Y81yjLgRPs8bKB3yvtC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 69303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 750,
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

_source line 40 · 2026-05-20T21:08:45.582Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01SRB3sQ8fZoiu824hRMsfJ1`</summary>

```json
{
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "dream_20260520T201854",
  "overall_score": "weak accept (4/6)",
  "report": "---\ndream_id: dream_20260520T201854\ntier: best\noverall_score: weak accept (4/6)\nreviewer: R1 (Methods & Experiments)\ntimestamp: 2026-05-20\n---\n\n# Review: Cross-Lingual Correctness Probes Reveal a Depth-Transferability Pareto Frontier\n\n**Reviewer R1 — Methods & Experiments Focus**\n\n---\n\n## 1. Summary\n\nThe paper presents the first systematic evaluation of cross-lingual correctness probe transfer, studying 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. The central finding is a depth-transferability Pareto frontier: deeper layers improve English probe AUROC but degrade zero-shot cross-lingual transfer. The paper proposes CaCLR, a composite training objective with an MMD-based consistency loss, and provides CKA-based analysis, difficulty-capability decomposition, and confirmation that correctness-confidence orthogonality persists across languages. Statistical testing (bootstrap CIs, permutation tests, Cohen's d) is applied to key claims.\n\n---\n\n## 2. Strengths\n\n**S1. Comprehensive experimental scope with appropriate controls.** The paper covers a large design space: 3 architectures x 20 languages x 5 transfer methods x 3 benchmarks, with well-chosen ablations. The probe complexity comparison (LR vs MLP, Table 7/Appendix B), INT8 validation (Appendix A), Hewitt & Liang control tasks (Appendix D), and random-direction control in the decomposition analysis all demonstrate methodological care. Few papers in this area provide this breadth of validation.\n\n**S2. Mean-shift invariance proof is a clean theoretical contribution.** The formal argument that mean-shift yields AUROC = 0.000 under StandardScaler + logistic regression is elegant and practically valuable. It corrects an implicit assumption from prior work (Xiao et al.) and is confirmed empirically. This is the kind of tight theory-experiment alignment that strengthens a paper.\n\n**S3. Statistical rigor on key comparisons.** The CaCLR beta effect (p=0.003, d=0.48, bootstrap CI [0.019, 0.045]) and the decomposition effect (p=0.006, d=0.41) are reported with appropriate paired permutation tests and effect sizes. This goes well beyond the field's typical standard of reporting only point estimates.\n\n**S4. Difficulty-capability decomposition is well-designed.** Using IRT difficulty probes to extract and project out the difficulty direction, then retraining correctness probes on residuals, is a sound methodology. The random-direction control (~0pp, Table 4) is essential and properly rules out dimensionality reduction artifacts. The resource-tier gradient (LOW +4.1pp vs HIGH +2.2pp) provides interpretable structure.\n\n**S5. Linear projection data efficiency analysis is practically valuable.** The saturation curve (Table 6) showing that ~50 parallel pairs achieve 98% of 200-pair performance, with the tier-stratified breakdown (LOW languages needing ~48 pairs vs HIGH needing ~22), gives practitioners actionable guidance. This is more useful than many method contributions.\n\n---\n\n## 3. Weaknesses\n\n### Major\n\n**W1. CaCLR's marginal advantage undermines the method contribution framing.** CaCLR beats 50-pair linear projection by only +1.4pp median AUROC and slightly loses to few-shot 100 (-0.8pp). Linear projection requires 50 translated question-answer pairs and a closed-form matrix solve. CaCLR requires parallel activations across all target languages, gradient-based training of a 3-term composite loss with two hyperparameters (alpha, beta), and careful tuning (the beta sweep shows the method is sensitive to this choice: 0.001 yields +0.8pp, 0.1 yields +3.2pp, 1.0 drops to +2.1pp). The paper frames CaCLR as needing \"zero target-language labels,\" but it does need parallel inputs — and the 50 parallel pairs needed by linear projection are a strict subset of the parallel inputs needed by CaCLR. The cost-benefit calculus favors linear projection for most practical settings.\n\n**W2. Architecture-dependence claim is confounded and cannot support causal attribution.** The three models differ in architecture type (2 MoE, 1 Dense), scale (235B vs 109B vs 31B), layer count (94 vs 48 vs 60), active parameters (22B vs 17B vs 31B), and training data composition. The paper attributes the Pareto frontier shape difference to \"MoE expert routing accelerating language specialization\" (Section 6), but no evidence isolates this mechanism. No expert routing analysis (e.g., routing entropy by language, expert specialization metrics) is presented. The claim that Gemma 4's smoother frontier is \"consistent with gradual rather than discrete language specialization\" is post-hoc narrative, not evidence. Three confounded data points are insufficient for causal attribution. The claim should be qualified as observational.\n\n**W3. CKA \"mechanistic explanation\" is correlational and likely confounded by depth.** The r=0.82 Pearson correlation between CKA and transfer AUROC (Table 3/Section 5.5) is presented as a \"mechanistic explanation,\" but depth is an obvious confounder: CKA decreases monotonically with depth, and transfer AUROC also varies monotonically with depth (past the elbow). The correlation could be entirely mediated by depth without CKA playing any causal role. A partial correlation controlling for (normalized) depth would clarify how much of the r=0.82 survives. The current framing overstates the evidence. The subspace angle analysis (correctness direction rotating 15-35 degrees at deep layers vs 5-12 degrees at shallow) is more informative but is described only textually without quantitative results in any table.\n\n**W4. Pareto frontier reported at reduced resolution despite experimental design specifying full coverage.** The experimental design calls for 24 probed layers on Qwen3 (every 4th of 94) and 12 on Scout. Table 1 reports only 7 layers for Qwen3 and 6 for Scout. The review_context.yaml contains all 17 Qwen3 layers and 13 Scout layers. Reporting 7/24 raises concerns about selective presentation. The full layer-wise data should appear in a supplementary table, particularly since the Pareto frontier is the paper's titular contribution. Furthermore, the per-language Spearman rho values (rho = -0.78 median, IQR [-0.84, -0.71] for Qwen3) are reported only as summary statistics — showing the full per-language distribution would strengthen the claim that the frontier is consistent across languages.\n\n**W5. CaCLR training procedure is underspecified.** The paper states probes are logistic regression (Section 3.1), but CaCLR requires gradient-based optimization of a composite loss with MMD (Section 3.3). Critical details are missing: (a) Is the CaCLR probe still a single linear layer trained with SGD, or is it a different architecture? (b) What MMD kernel is used (Gaussian RBF, linear, polynomial)? What bandwidth? (c) What optimizer, learning rate schedule, number of epochs? (d) How many parallel activation pairs are used for the MMD term? (e) How is the train/validation split handled — is the MMD computed on the same data as BCE? These details are essential for reproducibility and for assessing whether the method is fairly compared against the simpler baselines.\n\n### Minor\n\n**W6. Selective statistical reporting.** Bootstrap CIs and permutation tests are applied to the CaCLR beta effect and decomposition, but not to: the Pareto rho values, the CKA-transfer correlation (the CI [0.76, 0.87] is marginal and does not account for depth confounding), the orthogonality measurements, or the cross-benchmark correlation (r=0.92). Multiple comparison corrections are absent across the many language x layer x model comparisons. The paper applies rigorous statistics where results are strong and omits them elsewhere.\n\n**W7. Orthogonality table shows only 10/20 languages.** Table 5 displays 10 languages but the claim states \"all 20 languages below 0.062.\" Showing half the evidence for a central claim is a presentation gap. The full table should appear in the appendix at minimum.\n\n**W8. INT8 validation covers only Scout, not Qwen3.** The INT8 vs FP16 comparison (Appendix A) uses Llama 4 Scout at 5 layers with a 5% random subset. Qwen3-235B-A22B, the primary model for most results, has no quantization validation. Quantization effects may differ across architectures and scales. Even a small-scale Qwen3 validation (5 layers, subset) would address this.\n\n**W9. The causal chain has a logical gap between decomposition and CaCLR.** The decomposition (Claim 2) identifies difficulty entanglement as a transfer degradation mechanism. CaCLR (Claim 3) uses MMD distributional alignment, not difficulty removal. The narrative implies decomposition motivates CaCLR, but CaCLR does not operationalize the decomposition insight. A natural experiment — running CaCLR on difficulty-removed representations — would close this gap and potentially improve CaCLR further.\n\n---\n\n## 4. Questions for Authors\n\n1. **Can you provide the full 24-layer Pareto table for Qwen3 and 12-layer for Scout?** If the experiments were run as designed, this data exists. Was the subsampling a space decision or does the full data show irregularities?\n\n2. **What is the partial correlation between CKA and transfer AUROC after controlling for normalized depth?** This single number would clarify whether CKA adds explanatory power beyond \"deeper = worse transfer.\"\n\n3. **What MMD kernel and bandwidth are used in CaCLR?** Are the parallel activations for MMD drawn from the same items as the BCE training data, or a separate set?\n\n4. **Is CaCLR's probe still a single linear layer?** If so, how is gradient-based optimization of a logistic regression with 3 loss terms implemented — is it trained from scratch with SGD, or initialized from the standard LR solution?\n\n5. **What happens when CaCLR is applied to difficulty-removed representations?** Does decomposition + CaCLR stack, or are they addressing the same variance?\n\n6. **Can you provide expert routing entropy by language and depth for the MoE models?** This would support or refute the \"expert routing drives language specialization\" claim directly.\n\n7. **What are the absolute per-language ECE values (raw, temp-scaled, CaCLR-calibrated) for at least the tier-representative languages?** The \"3.5% reduction over temperature scaling\" is uninformative without baseline context.\n\n8. **How sensitive is the optimal transfer depth (60% for Qwen3, 50% for Scout) to the choice of benchmark?** The cross-benchmark table (Table 8) shows consistent method rankings, but does Belebele's optimal transfer layer differ from GlobalMMLU's?\n\n---\n\n## 5. Minor Issues\n\n- Table 1 for Scout omits ZS Min and ZS Max columns without explanation.\n- The bibliography has several placeholder citations (empty \\cite{} in the introduction).\n- \"CaCLR reduces non-English ECE by 3.5%\" — unclear whether this is 3.5 percentage points or 3.5 relative percent. Context suggests the former but should be explicit.\n- The Gemma 4 results (Appendix C) are summary-only. Given that this is the third architecture and the key dense-vs-MoE contrast, even a condensed per-layer table would strengthen the paper.\n- The paper lists 20 languages but explicitly names only ~12 (en, zh, es, fr, de, hi, ru, ko, tr, sw, bn, plus references to \"and X others\"). The full language list should appear in Section 4 or an appendix.\n\n---\n\n## 6. Overall Assessment\n\n**Score: 4/6 (Weak Accept)**\n**Confidence: 4/5**\n\n**Rationale.** This paper tackles a genuinely important and underexplored problem — whether probe-based calibration works beyond English — at impressive scale. The experimental design is thorough, covering multiple architectures, languages, benchmarks, and transfer conditions with appropriate ablations and controls. Several analytical contributions are strong: the mean-shift invariance proof, the difficulty-capability decomposition with random-direction control, the linear projection data efficiency analysis, and the confirmation of universal correctness-confidence orthogonality. The statistical practice, where applied, meets a high standard.\n\nThe paper falls short of a strong accept for three reasons. First, the headline method contribution (CaCLR) provides only marginal improvement (+1.4pp) over the much simpler linear projection baseline, and the training procedure is underspecified. Second, the architecture-dependence and CKA \"mechanistic\" claims are overstated relative to the evidence — three confounded models cannot support causal claims about expert routing, and a correlational CKA analysis confounded by depth is not mechanistic. Third, key results are reported at reduced resolution (7/24 layers, 10/20 languages), which is concerning for a paper whose titular contribution is a \"frontier\" that demands dense sampling.\n\nThe paper would be strengthened by: (a) reframing as primarily an analytical/characterization contribution with CaCLR as one demonstrated application, (b) reporting the full layer and language data, (c) qualifying the architecture-dependence and CKA claims, (d) providing CaCLR implementation details, and (e) testing CaCLR on difficulty-removed representations to close the causal chain.\n\nThe analytical findings — particularly the Pareto frontier quantification, decomposition, orthogonality universality, and the practical finding that ~50 parallel pairs suffice for effective linear projection — represent genuine contributions to the field's understanding of multilingual calibration. These alone warrant publication at a top venue, provided the framing matches the evidence.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f483456-b7b5-4a34-998f-df0e37a5b514",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEW7mqME47ZYgE9AxMby",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9059714c-e535-400e-ba44-db59120ddbdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V22Y81yjLgRPs8bKB3yvtC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 69303,
      "output_tokens": 3554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 750
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3554,
          "cache_read_input_tokens": 69303,
          "cache_creation_input_tokens": 750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 750,
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

_source line 41 · 2026-05-20T21:08:48.830Z_

<details><summary>↩ Tool result · `toolu_01SRB3sQ8fZoiu824hRMsfJ1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9059714c-e535-400e-ba44-db59120ddbdc",
  "isSidechain": true,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "agentId": "a87b7c9d30836e971",
  "type": "user",
  "uuid": "61cf8073-59cd-4dbd-8215-c6840649ed4f",
  "sourceToolAssistantUUID": "9059714c-e535-400e-ba44-db59120ddbdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T21:09:02.279Z_

Review submitted successfully. Here is a summary of the key findings:

**Score: 4/6 (Weak Accept), Confidence: 4/5**

**Top strengths identified:**
- Comprehensive experimental scope (3 architectures, 20 languages, 5 transfer methods, 3 benchmarks) with appropriate controls (Hewitt & Liang control tasks, random-direction control, INT8 validation, probe complexity comparison)
- Clean mean-shift invariance proof (AUROC identically 0 under StandardScaler + LR)
- Well-designed difficulty-capability decomposition with random-direction control ruling out artifacts
- Strong statistical practice on key claims (paired permutation tests, bootstrap CIs, Cohen's d)
- Practically valuable linear projection data efficiency analysis (~50 pairs suffice)

**Top weaknesses identified:**
1. CaCLR's +1.4pp advantage over 50-pair linear projection is marginal given its substantially higher complexity (3-term loss, hyperparameter tuning, parallel inputs for all languages)
2. Architecture-dependence claim is confounded — 3 models differ in architecture, scale, depth, active parameters, and training data simultaneously; no expert routing analysis supports the causal attribution
3. CKA "mechanistic explanation" is correlational and likely confounded by depth; partial correlation controlling for depth was not computed
4. Pareto frontier reported at 7/24 layers (Qwen3) despite design specifying all 24; raises concerns about selective presentation
5. CaCLR training procedure critically underspecified (kernel, bandwidth, optimizer, architecture unclear)

**Key recommendations:** Reframe as primarily an analytical/characterization paper rather than a method contribution; report full layer and language data; qualify causal claims about architecture and CKA; specify CaCLR implementation details; test CaCLR on difficulty-removed representations to close the causal chain gap.

The review report is saved at `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61cf8073-59cd-4dbd-8215-c6840649ed4f",
  "isSidechain": true,
  "agentId": "a87b7c9d30836e971",
  "requestId": "req_011CbEWFDZbykuAsQTmGhdNJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53a9a5d3-3068-4e68-a25e-110b787aa893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWpMXdVpLgrnFUxPZgTiSV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3685,
      "cache_read_input_tokens": 70053,
      "output_tokens": 492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 492,
          "cache_read_input_tokens": 70053,
          "cache_creation_input_tokens": 3685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3685,
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
