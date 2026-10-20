# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **Novelty** and **Related Work**. Use a 6-point 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5590f0616c82a5a5.jsonl`
- **Structured JSON:** [`5649a5dc4515364727fd.json`](../../sessions/56/5649a5dc4515364727fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-20T19:38:53.384Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **Novelty** and **Related Work**. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target acceptance rate ~25%.

## Paper Summary

**Title**: "Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR"

The paper studies cross-lingual correctness probe transfer for calibration across 20 languages and 3 architectures (Qwen3-235B-A22B MoE 94L, Llama 4 Scout MoE 48L, Gemma 4 31B Dense 60L). Four claims:

1. **Pareto Frontier Discovery**: Deeper layers yield better EN calibration but degrade cross-lingual zero-shot transfer. Optimal transfer depth ~58-60% of model depth. Spearman ρ=0.82-0.88.
2. **Decomposition**: Correctness signal decomposes into difficulty-shared (68% var, language-agnostic, transfers well) and capability-specific (32% var, language-dependent, drives 87% of transfer degradation).
3. **CaCLR**: A training objective (L_BCE + α·L_SB-ECE + β·L_consistency) that shifts the Pareto frontier outward. +5.2pp AUROC over zero-shot, ~40% ECE reduction vs temp scaling, no target-language labels needed.
4. **Orthogonality**: Correctness-confidence orthogonality (cosine<0.1) persists across all 20 languages, with resource-tier gradient (ρ=-0.68).

## Related Work (as presented in the paper)

The paper positions itself at the intersection of three areas:

**Probe-Based Calibration**: Burns et al. (2023, ICLR) and Marks et al. (2024, COLM) showed linear probes on intermediate activations recover correctness signals. Miao et al. (2026a; CORAL) demonstrated cross-task transfer of such probes. Miao & Ungar (2026b) established orthogonality of correctness and verbalized confidence directions. **All of this work is English-only.**

**Cross-Lingual Representation Transfer**: Xiao et al. (ACL 2025) transferred knowledge-boundary probes (input-level answerability, not output-dependent correctness) across 8 languages, measuring probing accuracy rather than calibration. Civelli et al. transferred difficulty probes cross-lingually, finding language-agnostic difficulty encoding.

**Multilingual Calibration**: LACE (Zhou et al.) uses per-language layer ensembles but requires target-language labels. MKA employs multi-key attention at 5× inference cost. Temperature scaling is the standard output-based baseline. None addresses representation-level cross-lingual calibration transfer.

## Methods Details

- **Probes**: Logistic regression (primary) and 2-layer MLP (comparison), trained on EN correctness labels from GlobalMMLU.
- **Transfer conditions**: Zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR.
- **CaCLR loss**: L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency. α=0.15, β=0.08. L_consistency penalizes divergence between EN and non-EN probe outputs on parallel activations. L_SB-ECE is soft-binned ECE loss.
- **Decomposition**: IRT difficulty probes (Ridge regression), project out difficulty direction, retrain on residuals.
- **Orthogonality**: Cosine similarity between correctness and verbalized confidence directions across 20 languages.

## Key Results (Summary)

- Pareto frontier is consistent across 3 architectures (best transfer at 58-60% depth)
- CaCLR: +5.2pp AUROC, ~40% ECE reduction, no target labels needed
- Decomposition: difficulty-shared 68% var (transfers well), capability-specific 32% (drives 87% degradation)
- Orthogonality: mean cosine 0.052, all <0.1, resource-tier gradient ρ=-0.68
- Generalizes to 52 languages, 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX)

## References Listed

1. Burns et al. (2023) — Discovering latent knowledge, ICLR
2. Marks et al. (2024) — Geometry of truth, COLM
3. Miao et al. (2026a) — CORAL: Cross-task correctness probes
4. Miao & Ungar (2026b) — Orthogonality of correctness and confidence directions
5. Xiao et al. (ACL 2025) — Cross-lingual knowledge boundary probe transfer
6. Civelli et al. (2025) — Cross-lingual difficulty probe transfer
7. Zhou et al. — LACE: Layer-adaptive calibration ensembles
8. Gao et al. (2024) — Quantization effects on probing

## Your Task

Produce a structured review focusing on Novelty and Related Work. Your review must include:

1. **Summary** (2-3 sentences)
2. **Novelty Assessment** — for each of the 4 claims, rate novelty (high/medium/low) and explain what is genuinely new vs incremental extension
3. **Related Work Gaps** — any missing references or comparisons that should be included
4. **Strengths** (bulleted, specific)
5. **Weaknesses** (bulleted, specific, with severity: minor/moderate/major)
6. **Questions for Authors** (numbered)
7. **Preliminary Score** (1-6 with justification)
8. **Confidence** (1-5)

Be rigorous. Consider:
- Is the gap (English-only probe calibration → cross-lingual) genuinely under-explored, or is this an obvious extension?
- How novel is CaCLR compared to existing consistency regularization / domain adaptation losses?
- Is the decomposition (difficulty vs capability) a genuine insight or repackaging of known ideas (IRT is well-established)?
- Is the orthogonality extension (EN → 20 languages) a significant finding or a confirmatory experiment?
- Are there missing related works (e.g., domain adaptation, representation alignment, cross-lingual probing beyond the cited works)?
- Does the paper adequately differentiate from Xiao et al. (2025) and Civelli et al. (2025)?

Note: The paper is a "dream" paper (simulated results), so assess the conceptual novelty and positioning rather than questioning whether experiments were actually run.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "6d42523b-1a22-4a1f-9984-ba31e2f248d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T19:38:53.386Z_

```json
{
  "parentUuid": "6d42523b-1a22-4a1f-9984-ba31e2f248d7",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
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
  "uuid": "dfb88a4b-354a-4efd-b42b-36f4188feb89",
  "timestamp": "2026-05-20T19:38:53.386Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T19:38:56.601Z_



I'll start by loading the project files to understand the full context of this paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfb88a4b-354a-4efd-b42b-36f4188feb89",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPPW6Be8i1gLtQMKEHB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0410afff-4e1f-4dc0-97db-aa20cbc516a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152zjga8KYQWTDUrkv9yvGW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7742,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7742,
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

_source line 4 · 2026-05-20T19:38:57.700Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015fQczSDMMYYortZ6fEm2TF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0410afff-4e1f-4dc0-97db-aa20cbc516a3",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPPW6Be8i1gLtQMKEHB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10d37d3c-2d51-493b-ba1b-47e2a8aef6c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152zjga8KYQWTDUrkv9yvGW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7742,
      "cache_read_input_tokens": 8251,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 144,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7742,
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

_source line 5 · 2026-05-20T19:38:57.704Z_

<details><summary>↩ Tool result · `toolu_015fQczSDMMYYortZ6fEm2TF`</summary>

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
  "parentUuid": "10d37d3c-2d51-493b-ba1b-47e2a8aef6c4",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "730be574-8852-4220-8cee-89a1f77b7d5d",
  "sourceToolAssistantUUID": "10d37d3c-2d51-493b-ba1b-47e2a8aef6c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T19:39:00.706Z_



Let me first read the project's key files to get full context on the paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "730be574-8852-4220-8cee-89a1f77b7d5d",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPPpDbgk1AtjqHFUXsp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f44ad7c-ea03-4ad5-99e2-3328c317d7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMkY7JvjLwGu8yq5mo5RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 15993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2063,
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

_source line 7 · 2026-05-20T19:39:01.854Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RwehcokkFRUknWymRNaRaA`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f44ad7c-ea03-4ad5-99e2-3328c317d7a3",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPPpDbgk1AtjqHFUXsp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b5063c1-ff52-4680-a169-c17f1aba2886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMkY7JvjLwGu8yq5mo5RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 15993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2063,
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

_source line 8 · 2026-05-20T19:39:01.870Z_

<details><summary>↩ Tool result · `toolu_01RwehcokkFRUknWymRNaRaA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_003 | Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_002** (failed): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n\\n## 趋势\\n成功 1 / 负向 0 / 失败 1 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n- mvp_002: 训练失败 — unknown\\n\", \"total_chars\": 1092, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b5063c1-ff52-4680-a169-c17f1aba2886",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "0112b8bc-d5ce-4cc4-987e-5b30b6583835",
  "sourceToolAssistantUUID": "2b5063c1-ff52-4680-a169-c17f1aba2886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T19:39:02.396Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012J53bSWgne5wZhcbrY87Cy`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0112b8bc-d5ce-4cc4-987e-5b30b6583835",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPPpDbgk1AtjqHFUXsp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fdac511-6513-4de9-845b-b9266719dee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMkY7JvjLwGu8yq5mo5RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 15993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2063,
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

_source line 10 · 2026-05-20T19:39:02.405Z_

<details><summary>↩ Tool result · `toolu_012J53bSWgne5wZhcbrY87Cy`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fdac511-6513-4de9-845b-b9266719dee0",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "c8ab542d-be52-412d-a4f6-bf0f6872c50e",
  "sourceToolAssistantUUID": "3fdac511-6513-4de9-845b-b9266719dee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:39:02.640Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PwasrCsfHibiH2e8vQPXoS`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8ab542d-be52-412d-a4f6-bf0f6872c50e",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPPpDbgk1AtjqHFUXsp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "955fb5a8-7552-4401-9100-0dcb7fb7ad6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMkY7JvjLwGu8yq5mo5RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 15993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2063,
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

_source line 12 · 2026-05-20T19:39:02.648Z_

<details><summary>↩ Tool result · `toolu_01PwasrCsfHibiH2e8vQPXoS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "955fb5a8-7552-4401-9100-0dcb7fb7ad6f",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "acafbdb7-dc79-47b7-b1ed-856b477a5a9d",
  "sourceToolAssistantUUID": "955fb5a8-7552-4401-9100-0dcb7fb7ad6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:39:05.809Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019v4KmvoYmsYP7LxtkvtZgj`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acafbdb7-dc79-47b7-b1ed-856b477a5a9d",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPQBr7FoY8T8iXuRXqs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "597e023e-ab7d-4938-ab06-ab02207aef66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vCM4NjUffFYWmYqgjmvGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4088,
      "cache_read_input_tokens": 18056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4088,
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

_source line 14 · 2026-05-20T19:39:05.818Z_

<details><summary>↩ Tool result · `toolu_019v4KmvoYmsYP7LxtkvtZgj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\\n- **Headline template**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak\\\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 6025, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "597e023e-ab7d-4938-ab06-ab02207aef66",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "2ca81740-ce00-4415-9e32-cbf9fa89e27a",
  "sourceToolAssistantUUID": "597e023e-ab7d-4938-ab06-ab02207aef66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T19:39:06.286Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DHnPvaUHeAemBPkvexs3Nx`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ca81740-ce00-4415-9e32-cbf9fa89e27a",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPQBr7FoY8T8iXuRXqs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c205827c-57e1-4178-8f9f-5bc3f0737f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vCM4NjUffFYWmYqgjmvGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4088,
      "cache_read_input_tokens": 18056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4088,
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

_source line 16 · 2026-05-20T19:39:06.294Z_

<details><summary>↩ Tool result · `toolu_01DHnPvaUHeAemBPkvexs3Nx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:00 UTC | 更新原因: Reviewer 修正 mean-shift 叙事 + 标注覆盖度风险 + temp scaling 待确认\\n\\n## 核心方向\\n通过中间层 correctness direction 将英语校准迁移到非英语语言。发现 depth-transferability Pareto frontier，提出 CaCLR 方法联合优化 correctness + 跨语言一致性。详见 paper_framing.md。\\n\\n## 当前进展\\n- 阶段：**Research**（MVP 已通过，D004）\\n- 服务器：westd-13176（4× RTX 6000 PRO 96GB）\\n- MVP 结论：核心假设获强支持（EN AUROC=0.754, 4/5 语言迁移成功, layer-depth 14.3pp, Pareto tradeoff 直接观测）\\n- Mean-shift 不可靠/不一致（部分语言微改善、部分恶化，无系统性）→ motivate CaCLR\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟进行中（dream_20260520T185641）\\n- ⚠️ P1 ECE pass 依赖 post-hoc temp scaling (T=6.21)，需确认是否在 held-out set 上调\\n\\n## 实验计划（详见 experiment_plan.yaml）\\n- **P0**：plan_001(Qwen3-235B) + plan_002(Llama4 Scout) + plan_003(CaCLR) + plan_004(difficulty ablation)\\n- **P1**：plan_005(orthogonality) + plan_006(probe complexity) + plan_007(Belebele/MMLU-ProX) + plan_010(INT8 ablation)\\n- **P2**：plan_008(Gemma4) + plan_009(50+ languages)\\n- **MVP**：mvp_001 ✅ | mvp_002 bug 修复中 | mvp_003 RUNNING (Llama-3.1-8B, cuda:2)\\n- **覆盖风险**：Claims 2/3/4 各仅 1 个实验，需 Dream 反馈后评估是否加备份\\n\\n## 近期任务\\n- [ ] 等待 Dream 回调，按结果调整 framing/plan\\n- [ ] Agent 修复 --layers 默认值 bug（M004）+ mvp_002 重跑\\n- [ ] Agent 确认 temp scaling 是否在 held-out set 上调\\n- [ ] 确认 IRT difficulty scores 数据可获取性（plan_004 硬依赖）\\n- [ ] mvp_003 结果（cross-architecture 验证）\\n- [ ] Dream 通过后批准 P0 实验\\n\\n## GPU 预算\\n**已分配**：westd-13176 4× RTX 6000 PRO 96GB\\n**当前使用**：cuda:0 空闲 | cuda:1 空闲(mvp_002完成) | cuda:2 mvp_003 | cuda:3 空闲\\n**Critical path**：plan_001(Qwen3-235B INT8 ~235GB) 需 3-4 卡，是全计划瓶颈\\n**Fallback**：CaCLR 效果不显著 → paper 退化为 systematic characterization，仍可投但 significance 降级\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n| D002 | 2026-05-20 | MVP 模型固定为 Qwen2.5-7B-Instruct | — |\\n| D001 | 2026-05-20 | MVP 用 7-8B 模型验证核心假设，不直接上 235B | — |\\n\\n\\n\\n\", \"total_chars\": 1996, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c205827c-57e1-4178-8f9f-5bc3f0737f0a",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "02c2787b-aea2-48bc-8a8f-a8e8bd57952d",
  "sourceToolAssistantUUID": "c205827c-57e1-4178-8f9f-5bc3f0737f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:39:06.847Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QLRBoDFPjffsibiMZbwPNJ`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02c2787b-aea2-48bc-8a8f-a8e8bd57952d",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPQBr7FoY8T8iXuRXqs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63655105-650e-4abf-8078-faccd4a56fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vCM4NjUffFYWmYqgjmvGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4088,
      "cache_read_input_tokens": 18056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4088,
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

_source line 18 · 2026-05-20T19:39:06.856Z_

<details><summary>↩ Tool result · `toolu_01QLRBoDFPjffsibiMZbwPNJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory — xling_calib_direction\\n\\n## 环境配置\\n- **服务器**: westd-13176, 4× RTX 6000 PRO 96GB\\n- **环境**: conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)\\n- **模型路径**: `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct`（symlink `/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`）\\n- **代码路径**: `/root/xling_calib_direction/`\\n- **Qwen2.5-7B-Instruct**: 28 layers (index 0-27), hidden_dim=3584\\n- **网络**: 不要用 `source /etc/network_turbo`（会破坏 HF SSL），用 `HF_ENDPOINT=https://hf-mirror.com`\\n- **模型下载**: 用 ModelScope（AutoDL 上 HF 代理太慢）\\n\\n## 数据集字段差异\\n- cais/mmlu: `choices` (list), `answer` (int 0-3)\\n- CohereForAI/Global-MMLU: `option_a/b/c/d` (str), `answer` (letter \\\"A\\\"-\\\"D\\\")\\n- `normalize_row()` 已处理两种格式\\n\\n## 激活提取速度\\n- Qwen2.5-7B-Instruct, BF16, RTX 6000 PRO 96GB: ~1 sample/s (MMLU 5-shot)\\n- 14K samples × 7 layers × 6 语言 ≈ 2h per GPU\\n\\n## MVP 实验关键发现 (2026-05-20)\\n\\n### Mean-shift alignment 完全无效（方法论发现）\\nMean-shift 对所有样本加同一常数向量 `(mean_en - mean_tgt)`。\\n- **不能改变 AUROC**: 经线性 probe 后等价于 logit 加常数，AUROC（rank-based）不变。\\n- **不能改善 calibration**: ΔECE 测试结果 0/5 语言达标。zh/ar 仅 marginal（<0.4pp），hi/sw 反而大幅恶化（+2.2pp/+6.4pp）。\\n- **结论**: 简单常数平移不足以 align 跨语言 representation。需要非常数方法（CDA/CORAL/Procrustes）。这是论文贡献空间。\\n\\n### Temperature scaling 有效修复 ECE\\n- Layer 24: T=5.36, ECE 0.1982→0.0888\\n- Layer 27: T=6.21, ECE 0.1951→0.0744\\n- T>1 说明 LogisticRegression 过于自信（overconfident），需要 softening\\n\\n### Layer 27 vs Layer 24: 最后一层更 language-specific\\n- EN AUROC: L27=0.7541 > L24=0.7486（最后一层英语 probe 最强）\\n- 但跨语言迁移: L24 全面优于 L27（zh 0.686 vs 0.661, ar 0.651 vs 0.635, hi 0.652 vs 0.626, ko 0.648 vs 0.607）\\n- **解读**: 最后一层 representation 更 language-specific，对 zero-shot transfer 不利。Optimal transfer layer ≠ optimal source-language layer。这是论文可讨论的有趣发现。\\n\\n### Swahili 始终最差\\n- Best zero-shot AUROC: sw=0.560 (L27) / 0.544 (L20)，均 < 0.58 阈值\\n- 与 low-resource 假设一致，论文中作为 expected limitation\\n\\n### 最终 Gate Check (2026-05-20)\\n- P1 ✅ PASS (AUROC=0.7541, ECE=0.0744 with temp scaling)\\n- P2 ✅ PASS (4/5 langs)\\n- P3 ✅ PASS (14.28pp)\\n- P4 ❌ FAIL (mean-shift 无效，0/5)\\n- 无 hard fail\\n- Overall: PARTIAL 3/4, 核心假设获强支持\\n\", \"total_chars\": 2071, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63655105-650e-4abf-8078-faccd4a56fc0",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "1f900e55-ba24-4c2b-80ce-ef29f5c61253",
  "sourceToolAssistantUUID": "63655105-650e-4abf-8078-faccd4a56fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T19:39:09.666Z_

Now let me read the distilled research skill for deeper domain context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f900e55-ba24-4c2b-80ce-ef29f5c61253",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPQVSXFpAcwSosLaYqA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82c336c8-2a3e-4ff8-8673-92f7f0f8432e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WD5UtoULqA6ZUxKj4YV69q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 22144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4814,
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

_source line 20 · 2026-05-20T19:39:10.680Z_

<details open><summary>🔧 Tool call — Read · `toolu_012cYc6iYpYfn5L1ZHEL3kvP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c336c8-2a3e-4ff8-8673-92f7f0f8432e",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPQVSXFpAcwSosLaYqA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80353e88-5413-4d67-9508-8aa317221078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WD5UtoULqA6ZUxKj4YV69q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 22144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4814,
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

_source line 21 · 2026-05-20T19:39:10.686Z_

<details><summary>↩ Tool result · `toolu_012cYc6iYpYfn5L1ZHEL3kvP`</summary>

```text
1	---
2	name: xling-calib-direction-research
3	description: Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Research Patterns (12 papers)
8	
9	## Evaluation Protocol
10	
11	**Metrics**: ECE (8/12) + AUROC (5/12) + Brier (4/12). Always pair calibration with discrimination. Point estimates without CIs is field norm (6/8). High conf.
12	
13	**Benchmarks**: MMLU (5/12), Belebele for multilingual (122 langs), TruthfulQA. Transfer: ARC, HellaSwag, CSQA. High conf.
14	
15	**Models**: 3-6 models. Llama-3.1-8B + Qwen2.5-7B near-universal. Include multilingual-first model (Aya). High conf.
16	
17	## Method Trends
18	
19	**Linear probing of hidden states** (7/12): Linear classifiers suffice. AUC 0.80-0.97. Source: confidence_manifold2026. High conf.
20	
21	**Layer-wise analysis standard** (7/12): Middle-to-late layers (15-29/32) richest for xling/calibration. Final layer suboptimal for non-English. Source: zhou2025lace (24-29), civelli2026shared (xling ~15, monolingual ~30). High conf.
22	
23	**Inference-time steering** (4/12): Extract direction, add to activations, no retraining. Source: ji2025calibrating, miao2026coral, miao2026closing. Med conf.
24	
25	**Training-free methods rising** (3/12): LACE, mean shift, projection. Field moving from fine-tuning. Med conf.
26	
27	**Temperature scaling declining**: Only baseline now. High conf.
28	
29	## Cross-Paper Findings
30	
31	**Non-English ECE 5x English** (23% vs 4.6%). Structural, tied to pretraining data. Source: zhou2025lace. 3/12. High conf.
32	
33	**Cross-lingual reps are linear**: Knowledge/confidence linearly encoded across languages in middle layers. Mean shift/projection enables training-free transfer. Source: xiao2025knowledge. 4/12. High conf.
34	
35	**Correctness distributed not sparse**: SAE neuron ablation negligible (delta ECE 1.25e-4). 3-8D subspace. Source: miao2026coral, confidence_manifold2026. 2/12. Med conf.
36	
37	**Layer-depth Pareto**: English calibration improves monotonically; non-English peaks mid-late then degrades. Source: zhou2025lace, joshi2025calibration. 2/12. High conf.
38	
39	## Competitor Landscape
40	
41	**zhou2025lace** (competitor): Per-language layer ensemble, ECE 22→3%, training-free. No directional methods.
42	**joshi2025calibration** (competitor): Calibration direction in residual stream. Transfers across datasets but NOT across models. Monolingual only.
43	
44	**Our niche**: No paper combines xling transfer + calibration directions + layer-depth Pareto. joshi's direction fails cross-model. civelli shows xling/monolingual optimal layers diverge. Intersection is open.
45	
46	## Gaps
47	
48	- Cross-model direction transfer unsolved (joshi shows failure)
49	- No multilingual verbal uncertainty (ji2025calibrating English-only)
50	- MCQA-only (5/12) → generation calibration open
51	- Instance-level causal validation missing (ravisankar correlation only)
52	- Scale beyond 7-8B untested
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80353e88-5413-4d67-9508-8aa317221078",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "7f84dedb-b9fb-4782-9d57-23d36c3ab419",
  "sourceToolAssistantUUID": "80353e88-5413-4d67-9508-8aa317221078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T19:39:11.202Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01V7hoPy8nBVqx63XrJi8H2n`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f84dedb-b9fb-4782-9d57-23d36c3ab419",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPQVSXFpAcwSosLaYqA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72cfd163-1f19-4084-a96d-1a76fe29e9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WD5UtoULqA6ZUxKj4YV69q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 22144,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 22144,
          "cache_creation_input_tokens": 4814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4814,
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

_source line 23 · 2026-05-20T19:39:11.213Z_

<details><summary>↩ Tool result · `toolu_01V7hoPy8nBVqx63XrJi8H2n`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72cfd163-1f19-4084-a96d-1a76fe29e9db",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "0be15df9-58bc-4547-a673-6366fca1a5b4",
  "sourceToolAssistantUUID": "72cfd163-1f19-4084-a96d-1a76fe29e9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T19:39:14.187Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GnWwfZbcTT6qqiFSC3PeMr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be15df9-58bc-4547-a673-6366fca1a5b4",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPQpAA2U94rhpYBXeWm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c1a3bca-0a5c-4d9b-80d4-c5d276334489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgdcHZfeRY1NnR7JCKghNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1313,
      "cache_read_input_tokens": 26958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1313,
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

_source line 25 · 2026-05-20T19:39:14.192Z_

<details><summary>↩ Tool result · `toolu_01GnWwfZbcTT6qqiFSC3PeMr`</summary>

```text
1	---
2	name: xling-calib-direction-writing
3	description: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Writing Patterns (8 papers)
8	
9	## Narrative
10	
11	**Story type**: "突破局限型" (7/8). Blind spot → reveal → fill. High conf.
12	
13	**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.
14	
15	**Hooks** (pick one):
16	- English-centric gap: "Prior work focuses on English, leaving X unexplored" (xiao, zhou). 2/8.
17	- Name the meta-problem: "Square One Bias" (zhou) — forces acknowledgment.
18	- Cognitive dissonance: "LLMs are surprisingly well-calibrated" (joshi) — contradicts expectation.
19	- Pain narrowing: "most dangerous hallucination — confident wrong answers" (ji).
20	
21	**Tension**: Show standard practice actively fails, not just untried. "Fine-tuning doesn't change alignment" (liu). "Final layer overwrites multilingual signals" (zhou). "Aggregate correlation masks instance-level failure" (ravisankar). 3/8. High conf.
22	
23	## Insight Delivery
24	
25	**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.
26	
27	**Negative-as-evidence** (2/8): "X doesn't work" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).
28	
29	**"Finding the knob"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.
30	
31	## Figures
32	
33	**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.
34	
35	**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.
36	
37	**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.
38	
39	**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.
40	
41	**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.
42	
43	## Tables
44	
45	**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.
46	
47	**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.
48	
49	**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.
50	
51	**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c1a3bca-0a5c-4d9b-80d4-c5d276334489",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "e958ffd8-4d45-458b-9e82-bf274b6155e5",
  "sourceToolAssistantUUID": "1c1a3bca-0a5c-4d9b-80d4-c5d276334489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T19:39:17.205Z_

Now I have comprehensive context. Let me also check if there's an experiment plan for additional details on the claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e958ffd8-4d45-458b-9e82-bf274b6155e5",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPR3WaphWjTzzbN4oCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f989fd4d-4d43-47ba-9fb8-c4dd1ebf0391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RozHEJqetZTRCK4tnkmaFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 28271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1005,
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

_source line 27 · 2026-05-20T19:39:17.657Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01W3W6cyaQBmFcpxnzZYcK2B`</summary>

```json
{
  "pattern": "**/*experiment_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f989fd4d-4d43-47ba-9fb8-c4dd1ebf0391",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPR3WaphWjTzzbN4oCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2ea8e42-4b1c-4609-a09a-1d4495f22681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RozHEJqetZTRCK4tnkmaFh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 28271,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1005
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 28271,
          "cache_creation_input_tokens": 1005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1005,
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

_source line 28 · 2026-05-20T19:39:17.673Z_

<details><summary>↩ Tool result · `toolu_01W3W6cyaQBmFcpxnzZYcK2B`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2ea8e42-4b1c-4609-a09a-1d4495f22681",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "2761c4fa-4b68-4d1f-86e4-79490ec92712",
  "sourceToolAssistantUUID": "c2ea8e42-4b1c-4609-a09a-1d4495f22681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T19:39:20.174Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011Gm2v1CiBm2jRBmdsq2kZU`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "experiment_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2761c4fa-4b68-4d1f-86e4-79490ec92712",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPRHj6epaG387FZh9Eq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e93e7873-9ef1-49dd-b825-f089c2ecce82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013aCLPERPYRGpRNPyWuAZmb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 143,
      "cache_read_input_tokens": 29276,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 143
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 29276,
          "cache_creation_input_tokens": 143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 143,
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

_source line 30 · 2026-05-20T19:39:20.192Z_

<details><summary>↩ Tool result · `toolu_011Gm2v1CiBm2jRBmdsq2kZU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e93e7873-9ef1-49dd-b825-f089c2ecce82",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "703b2c99-32dc-4250-94df-c7c71131bcee",
  "sourceToolAssistantUUID": "e93e7873-9ef1-49dd-b825-f089c2ecce82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T19:39:22.544Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XZSmBFRzyR4uC7wPS9hugj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "703b2c99-32dc-4250-94df-c7c71131bcee",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPRUQnf7YxHsLptTLis",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfc1993c-79d8-46ef-89cf-05a30423af45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3VVynJLjcihShivXJpLEY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 29419,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 277
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 29419,
          "cache_creation_input_tokens": 277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 277,
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

_source line 32 · 2026-05-20T19:39:22.549Z_

<details><summary>↩ Tool result · `toolu_01XZSmBFRzyR4uC7wPS9hugj`</summary>

```text
1	experiments:
2	  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===
3	
4	  - id: plan_001
5	    claim: 1
6	    description: >
7	      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8):
8	      extract activations at every 4th layer (24 probed layers),
9	      20 typologically diverse languages, train English correctness probes
10	      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions
11	      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
12	    priority: P0
13	    gpu_budget_hours: 80
14	    deps: []
15	    notes: "Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request."
16	
17	  - id: plan_002
18	    claim: 1
19	    description: >
20	      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8):
21	      extract activations at every 4th layer (12 probed layers),
22	      20 languages, 5 transfer conditions. INT8 weight quantization.
23	    priority: P0
24	    gpu_budget_hours: 40
25	    deps: []
26	    notes: "Needs 2× RTX 6000 PRO 96GB at INT8."
27	
28	  - id: plan_003
29	    claim: 3
30	    description: >
31	      CaCLR implementation and comparative evaluation:
32	      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency.
33	      Train CaCLR probes using English labels + unlabeled parallel activations.
34	      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)
35	      across full Pareto frontier for both models × 20 languages.
36	      Hyperparameter tuning (α, β) on held-out English + 5-language validation.
37	    priority: P0
38	    gpu_budget_hours: 20
39	    deps: [plan_001, plan_002]
40	    notes: "CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021."
41	
42	  - id: plan_004
43	    claim: 2
44	    description: >
45	      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression
46	      on human difficulty scores per Civelli et al.), project out difficulty direction
47	      from activations, retrain correctness probes on residuals, evaluate transfer.
48	      10 representative languages × 8 representative layers per model (20-90% depth).
49	    priority: P0
50	    gpu_budget_hours: 15
51	    deps: [plan_001, plan_002]
52	    notes: "Need IRT difficulty scores from GlobalMMLU or external source."
53	
54	  # === P1: Important for strong submission ===
55	
56	  - id: plan_005
57	    claim: 4
58	    description: >
59	      Cross-lingual orthogonality analysis: extract verbalized confidence direction
60	      (prompt model for confidence score, fit probe), compute cosine similarity
61	      with correctness direction across 20 languages × 2 architectures.
62	      Analyze by resource tier (high/mid/low) and language family.
63	    priority: P1
64	    gpu_budget_hours: 10
65	    deps: [plan_001, plan_002]
66	
67	  - id: plan_006
68	    claim: 1
69	    description: >
70	      Probe complexity comparison: logistic regression vs 2-layer MLP
71	      at each probed layer for both models. Compare English accuracy,
72	      cross-lingual transfer degradation, and calibration quality.
73	      Test hypothesis: linear probes transfer better cross-lingually.
74	    priority: P1
75	    gpu_budget_hours: 5
76	    deps: [plan_001, plan_002]
77	    notes: "CPU-bound, uses cached activations."
78	
79	  - id: plan_007
80	    claim: 1
81	    description: >
82	      Additional benchmark evaluation: evaluate best probes + CaCLR
83	      on Belebele (20 languages) and MMLU-ProX (20 languages).
84	      Validates generalization beyond MMLU/GlobalMMLU.
85	    priority: P1
86	    gpu_budget_hours: 30
87	    deps: [plan_001, plan_002, plan_003]
88	
89	  - id: plan_010
90	    claim: 1
91	    description: >
92	      INT8 validation ablation: compare INT8 vs FP16 probing results
93	      at 5 representative layers for Llama 4 Scout on 5% random subset.
94	      Validates that INT8 quantization doesn't distort correctness signals.
95	    priority: P1
96	    gpu_budget_hours: 5
97	    deps: [plan_002]
98	
99	  # === P2: Camera-ready extension ===
100	
101	  - id: plan_008
102	    claim: 1
103	    description: >
104	      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture
105	      for camera-ready. Full Pareto frontier, 20+ languages.
106	      Provides dense vs MoE architectural contrast.
107	    priority: P2
108	    gpu_budget_hours: 30
109	    deps: []
110	
111	  - id: plan_009
112	    claim: 1
113	    description: >
114	      Extended language coverage: expand from 20 to 50+ languages
115	      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.
116	    priority: P2
117	    gpu_budget_hours: 50
118	    deps: [plan_001, plan_002]
119	
120	  # === MVP experiments (completed/running) ===
121	
122	  - id: mvp_validation
123	    claim: 1
124	    description: "MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift"
125	    priority: P0
126	    registry_id: mvp_001
127	    gpu_budget_hours: 2
128	    deps: []
129	
130	  - id: mvp_complementary
131	    claim: 1
132	    description: "MVP robustness: complementary layer set (2,6,10,14,18,22,26)"
133	    priority: P1
134	    registry_id: mvp_002
135	    gpu_budget_hours: 2
136	    deps: [mvp_validation]
137	
138	  - id: mvp_llama_control
139	    claim: 1
140	    description: "MVP cross-architecture: Llama-3.1-8B control experiment"
141	    priority: P1
142	    registry_id: mvp_003
143	    gpu_budget_hours: 3
144	    deps: [mvp_validation]
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfc1993c-79d8-46ef-89cf-05a30423af45",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "ad0c5cf0-821e-4182-b9e2-17abb19c236c",
  "sourceToolAssistantUUID": "dfc1993c-79d8-46ef-89cf-05a30423af45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T19:40:53.195Z_

I now have comprehensive context. Let me compose the review.

---

## Reviewer 2 (R2) — Novelty & Related Work

### 1. Summary

This paper investigates cross-lingual transfer of correctness probes trained on English hidden representations to 20 non-English languages across three architectures (Qwen3-235B, Llama 4 Scout, Gemma 4 31B). It identifies a depth-transferability Pareto frontier, decomposes correctness transfer into difficulty-shared and capability-specific components, proposes CaCLR (a consistency-regularized probe training objective), and extends the correctness-confidence orthogonality finding from English to 20 languages. The central argument is that the entire probe-based calibration research line — previously English-only — generalizes multilingually, and that CaCLR enables effective transfer without target-language labels.

### 2. Novelty Assessment

**Claim 1 — Pareto Frontier (Discovery): Medium Novelty**

The observation that middle layers transfer better cross-lingually while deeper layers encode more language-specific information is well-established in the cross-lingual representation literature (Liu & Niehues, ACL 2025; Civelli et al., 2025 for difficulty probes; LACE's layer-ensemble motivation). The distilled research skill itself notes: "English calibration improves monotonically; non-English peaks mid-late then degrades" as a cross-paper finding with high confidence from Zhou et al. and Joshi et al. What is new is systematically charting this tradeoff specifically for *correctness* probes (rather than difficulty or knowledge-boundary probes) across 20 languages and quantifying it as a Pareto frontier with Spearman correlation. However, the conceptual insight — "deeper = more language-specific = worse transfer" — is not surprising given prior work. The contribution is more empirical characterization than conceptual advance.

**Claim 2 — Decomposition (Difficulty vs Capability): Medium-Low Novelty**

The decomposition uses IRT difficulty probes (well-established psychometric tool) as a control variable. Civelli et al. (2025) already demonstrated that difficulty encoding is language-agnostic and transfers well cross-lingually. The novelty here is reframing this as a decomposition of *correctness* transfer: subtracting the difficulty component and showing that the residual (capability-specific) drives 87% of transfer degradation. While this is a clean experimental design, it is essentially an ablation study using known tools rather than a new analytical framework. The "68/32 variance split" and "87% degradation attribution" are useful empirical findings, but the underlying idea — that question difficulty is shared across languages while model capability varies — is not surprising. Any researcher familiar with both IRT and cross-lingual probing would predict this decomposition.

**Claim 3 — CaCLR (Method): Medium Novelty**

CaCLR combines three loss terms: BCE (standard classification), SB-ECE (differentiable calibration loss from Karandikar et al., NeurIPS 2021), and a consistency loss penalizing divergence between EN and non-EN probe outputs on parallel activations. The consistency loss is structurally identical to domain adaptation consistency regularization (e.g., domain-adversarial training, MMD-based alignment, or simpler L2 representation matching). The main novelty is the *application* of this combination to probe-based calibration transfer, not the loss components themselves. The "no target-language labels needed" advantage is meaningful for practical deployment, but the method is a straightforward composition of existing techniques. That said, the +5.2pp AUROC and ~40% ECE reduction over strong baselines, if validated, would be a solid empirical contribution.

**Claim 4 — Cross-Lingual Orthogonality: Low Novelty**

This extends Miao & Ungar (2026b)'s finding (correctness and verbalized confidence directions are orthogonal, cosine < 0.04) from English to 20 languages. The paper reports mean cosine 0.052, all < 0.1, with a resource-tier gradient (rho = -0.68). While this is a useful confirmatory experiment, it is exactly the "obvious extension" one would propose after reading the original paper. The resource-tier gradient is mildly interesting but not deeply surprising (low-resource languages likely have noisier representations). This claim alone would not merit a paper; it is appropriate as a supporting finding but should not be framed as a primary contribution.

### 3. Related Work Gaps

**Missing references (moderate to significant):**

1. **Domain adaptation consistency losses**: The CaCLR consistency loss is closely related to domain adaptation literature. The paper should cite and differentiate from: Ganin & Lempitsky (2015, domain-adversarial neural networks), Long et al. (2015, DAN/MMD), Sun & Saenko (2016, CORAL for domain adaptation — note the name collision with Miao et al.'s CORAL). Without these references, CaCLR appears more novel than it is.

2. **Cross-lingual representation alignment beyond probing**: Conneau et al. (2020, "Emerging Cross-lingual Structure in Pretrained Language Models"), Pires et al. (2019), Chi et al. (2020, "Finding Universal Grammatical Relations in Multilingual BERT"). These establish the theoretical basis for why probe transfer works at all.

3. **Procrustes alignment / CCA for cross-lingual transfer**: Schuster et al. (2019), Conneau et al. (2018, MUSE). The paper tests mean-shift and linear projection but should discuss Procrustes alignment as a natural intermediate method between mean-shift and CaCLR.

4. **Calibration in multilingual NLP beyond LLMs**: Wang et al. (2020, "Inference-time calibration of sequence model predictions"), Desai & Durrett (2020, "Calibration of Pre-trained Transformers"). The related work focuses narrowly on LLM-era work.

5. **CCPS (Khanmohammadi et al., EMNLP 2025)**: Listed in the literature map but apparently not cited in the paper summary. This is a direct competitor — calibration via probing representation stability — and must be discussed.

6. **Ravisankar et al. (EACL 2026, DALI)**: In the literature map as a "foundation" paper providing "strongest causal support" for the hypothesis, but not mentioned in the paper summary's related work section. This should be cited as providing causal evidence via activation patching for the English representations fixing non-English errors.

7. **Joshi et al. (EMNLP 2025)**: In the literature map, describes calibration direction evolution across layers. Directly relevant to Claim 1 but not cited in the paper summary.

**Inadequate differentiation:**

- The differentiation from Xiao et al. (ACL 2025) is clearer in the paper_framing.md than in the review summary. The paper must make the distinction (input-level answerability vs output-dependent correctness) unmistakable in the main text, ideally with a table or explicit comparison experiment.
- The differentiation from Civelli et al. needs strengthening — the paper relies on their difficulty probes for Claim 2 but the paper summary doesn't adequately credit or distinguish from their work.

### 4. Strengths

- **Fills a genuine gap**: The English-only limitation of probe-based calibration is real and well-documented. A systematic cross-lingual evaluation is overdue. The paper's self-characterization as a "field-level viability test" is honest and valuable.
- **Comprehensive experimental design**: 20 languages, 3 architectures (MoE + dense), 5 transfer conditions, multiple benchmarks (GlobalMMLU, Belebele, MMLU-ProX). This is substantially broader than Xiao et al. (8 languages, 1 architecture) and Civelli et al. (difficulty only).
- **Clean claim structure**: The four claims form a logical causal chain (discover frontier → decompose → shift frontier → mechanistic confirmation). Each claim is testable and falsifiable.
- **Practical value of CaCLR**: Zero target-language labels is a strong practical advantage over LACE and few-shot methods. If the +5.2pp AUROC and ~40% ECE reduction hold, this is deployment-ready.
- **MVP evidence is encouraging**: The Qwen2.5-7B-Instruct MVP confirms the core hypothesis (4/5 languages with AUROC >= 0.58, 14.3pp layer-depth effect), providing preliminary but concrete support.
- **Honest about limitations**: The paper acknowledges MCQA-only scope, notes Swahili's consistent underperformance, and includes INT8 validation ablation.

### 5. Weaknesses

- **(Major) CaCLR's novelty is overstated relative to domain adaptation literature.** The consistency loss is a standard domain adaptation technique applied to a new setting. Without citing and differentiating from the domain adaptation literature (DANN, DAN, Deep CORAL), the method contribution appears inflated. The paper should position CaCLR as a well-motivated *application* of consistency regularization rather than a novel loss design.

- **(Major) Claim 4 (orthogonality extension) is too thin for a primary claim.** Extending a single-language finding to 20 languages with the same methodology is confirmatory, not contributory. The resource-tier gradient (rho=-0.68) is the only genuinely new insight, and it is reported without mechanistic explanation. Recommend demoting to a supporting analysis rather than a co-equal claim.

- **(Moderate) The "Pareto frontier" framing may overstate the finding.** A monotonic relationship between layer depth and transfer quality is well-predicted by existing cross-lingual representation literature. Calling it a "Pareto frontier" adds terminological weight to what is, at its core, a depth-performance curve with a known direction. The Spearman correlations (0.82-0.88) quantify a trend everyone expected.

- **(Moderate) Missing related work on domain adaptation weakens positioning.** The paper occupies the intersection of probe transfer and domain adaptation. By citing only the probing and calibration literatures, it misses the opportunity to draw on — and differentiate from — a rich body of work on representation alignment for distribution shift.

- **(Moderate) Decomposition (Claim 2) relies on Civelli et al.'s methodology without sufficient differentiation.** The difficulty probe (Ridge regression on IRT scores) is taken directly from Civelli et al. The novelty is applying it as a *control* in the correctness transfer setting, but this needs clearer framing to avoid appearing derivative.

- **(Minor) Temperature scaling baseline concern.** The project notes flag that "P1 ECE pass depends on post-hoc temp scaling (T=6.21), need to confirm whether tuned on held-out set." If temperature is tuned on the test set, the ECE comparison is invalid. T=6.21 is unusually high (suggesting severe overconfidence), and this should be validated carefully.

- **(Minor) Single probe type dominance.** Logistic regression as the primary probe may underestimate the complexity of correctness signals. The 2-layer MLP comparison (plan_006) is P1 priority — results should appear in the main text, not just the appendix.

### 6. Questions for Authors

1. How does CaCLR's consistency loss differ from standard domain adaptation losses (e.g., MMD, adversarial, or Deep CORAL)? Have you compared against these alternatives? If not, what justifies the specific choice of divergence penalty?

2. The mean-shift alignment "completely fails" (0/5 languages) in your MVP, yet Xiao et al. (2025) report mean-shift success for knowledge-boundary probes. What explains this discrepancy? Is it the difference between input-level answerability and output-dependent correctness, or an artifact of probe/layer selection?

3. For the decomposition (Claim 2), what is the source of IRT difficulty scores? Are they from human annotators or estimated from model responses? If estimated, the difficulty-shared component is partially circular (model-dependent).

4. The orthogonality finding (Claim 4) reports mean cosine 0.052 across 20 languages. Miao & Ungar report <0.04 for English. Is the increase from 0.04 to 0.052 (and up to 0.1 for some languages) statistically significant? Does it suggest the orthogonality is *weaker* in non-English languages, and if so, what are the implications for the claim that "output-based calibration is structurally limited regardless of language"?

5. The optimal transfer depth is reported at 58-60% of model depth across all three architectures. Given that Civelli et al. report architecture-dependent optimal depths (24-49% for difficulty), why is your range so much narrower? Does this suggest correctness probes and difficulty probes access different representation subspaces?

6. For CaCLR, the consistency loss requires "parallel activations" — do these come from parallel translations in GlobalMMLU, or from a separate parallel corpus? What happens when parallel data is unavailable?

7. The Swahili AUROC consistently falls below the 0.58 threshold. At what resource level does probe transfer become unreliable? Have you characterized a minimum pretraining data threshold?

### 7. Preliminary Score: 4 (Weak Accept)

**Justification**: The paper addresses a genuine and timely gap — probe-based calibration has been English-only, and a systematic cross-lingual evaluation is valuable. The experimental design is comprehensive (20 languages, 3 architectures, multiple benchmarks). CaCLR provides a practical method with meaningful improvements (if validated). However, the novelty is moderate: the Pareto frontier is expected from prior work, the decomposition uses known tools, CaCLR is a domain-adaptation consistency loss applied to a new setting, and the orthogonality extension is confirmatory. The related work has significant gaps in domain adaptation and cross-lingual alignment literatures. The paper's strongest contribution is the systematic empirical characterization rather than methodological innovation. This positions it solidly for a venue like EACL but on the borderline — it would benefit from (a) explicitly acknowledging the domain adaptation connection, (b) demoting Claim 4, and (c) deepening the mechanistic analysis of *why* the Pareto frontier exists rather than just documenting it.

### 8. Confidence: 4/5

I am confident in my assessment of the novelty landscape and related work gaps. I have familiarity with the probe-based calibration, cross-lingual representation, and domain adaptation literatures. The main source of uncertainty is whether the full-scale experiments (particularly CaCLR on 235B models) would yield results that substantially change the novelty calculus — e.g., if the Pareto frontier reveals unexpected non-monotonic behavior across architectures, or if the decomposition yields prescriptive insights not predictable from prior work.

---

Now let me submit this review via the dream review report tool. Let me check the dream ID from the ROADMAP.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0c5cf0-821e-4182-b9e2-17abb19c236c",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPReR3i6DavRWkpsWhj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb5a9d3c-e52e-43f7-8c01-bbe545d85f9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRgAyDzkjyNATYnNsoKZ1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2017,
      "cache_read_input_tokens": 29696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2017,
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

_source line 34 · 2026-05-20T19:40:53.618Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NAd6TCowxDFvHgeGwEovye`</summary>

```json
{
  "pattern": "dream_",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb5a9d3c-e52e-43f7-8c01-bbe545d85f9b",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPReR3i6DavRWkpsWhj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2f62e2f-27e1-46fc-a495-05c62c93e6ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRgAyDzkjyNATYnNsoKZ1E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2017,
      "cache_read_input_tokens": 29696,
      "output_tokens": 3709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2017
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3709,
          "cache_read_input_tokens": 29696,
          "cache_creation_input_tokens": 2017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2017,
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

_source line 35 · 2026-05-20T19:40:53.652Z_

<details><summary>↩ Tool result · `toolu_01NAd6TCowxDFvHgeGwEovye`</summary>

```text
&lt;persisted-output>
Output too large (20.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf/tool-results/toolu_01NAd6TCowxDFvHgeGwEovye.txt

Preview (first 2KB):
dream_registry.yaml.bak:2:  dream_20260520T185641:
dream_registry.yaml.bak:3:    dream_id: dream_20260520T185641
ROADMAP.md:13:- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟进行中（dream_20260520T185641）
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:266:[Omitted long matching line]
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:267:[Omitted long matching line]
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:268:[Omitted long matching line]
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:273:[Omitted long matching line]
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:278:{"ts": "2026-05-20T18:56:34.666574+00:00", "role": "tool", "session": "feishu:group:oc_74ae31a7dc5ae9d419ba9a89bccc89c0:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:mcp__agent-ml-research__dream_simulate", "max_results": "1"}}
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:280:[Omitted long matching line]
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:281:{"ts": "2026-05-20T18:56:42.145803+00:00", "role": "tool_result", "session": "feishu:group:oc_74ae31a7dc5ae9d419ba9a89bccc89c0:director", "text": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"dream_id\\\": \\\"dream_20260520T185641\\\", \\\"status\\\": \\\"pending\\\", \\\"error\\\": \\\"\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}", "tool": "mcp__agent-ml-research__dream_simulate", "elapsed_ms": 753}
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:282:[Omitted long matching line]
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:284:[Omitted long matching line]
logs/chats/feishu_group_oc_74ae31a7dc5ae9d419ba9a89bccc89c0_director.jsonl:294:[Omitted long matching line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2f62e2f-27e1-46fc-a495-05c62c93e6ab",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "c58b0dd8-5093-461b-a41c-2eab7b6da2d7",
  "sourceToolAssistantUUID": "a2f62e2f-27e1-46fc-a495-05c62c93e6ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T19:40:56.576Z_

The dream ID is `dream_20260520T185641`. Now let me check what tier this review should be for.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c58b0dd8-5093-461b-a41c-2eab7b6da2d7",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPYMvZ6AbkamAoLSDHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8abd960f-28e2-4b6e-a331-618466608c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HytXsLz865sjtuFrdsW6nv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4739,
      "cache_read_input_tokens": 31713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4739,
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

_source line 37 · 2026-05-20T19:40:57.534Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WF42KxoCrzisGHADvAHLUY`</summary>

```json
{
  "pattern": "**/dream_reports/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8abd960f-28e2-4b6e-a331-618466608c12",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPYMvZ6AbkamAoLSDHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a0c5d76-49fd-4b75-940f-13b6224e0d45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HytXsLz865sjtuFrdsW6nv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4739,
      "cache_read_input_tokens": 31713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4739,
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

_source line 38 · 2026-05-20T19:40:57.550Z_

<details><summary>↩ Tool result · `toolu_01WF42KxoCrzisGHADvAHLUY`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a0c5d76-49fd-4b75-940f-13b6224e0d45",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "3cca7eb8-db2b-4549-a5bf-60103bfc6e74",
  "sourceToolAssistantUUID": "0a0c5d76-49fd-4b75-940f-13b6224e0d45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T19:40:57.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P6me9zrw7bPhVwDXjA765J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml.bak"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cca7eb8-db2b-4549-a5bf-60103bfc6e74",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPYMvZ6AbkamAoLSDHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef53dc6f-fe9a-420a-bb37-5e049b11db80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HytXsLz865sjtuFrdsW6nv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4739,
      "cache_read_input_tokens": 31713,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 31713,
          "cache_creation_input_tokens": 4739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4739,
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

_source line 40 · 2026-05-20T19:40:57.775Z_

<details><summary>↩ Tool result · `toolu_01P6me9zrw7bPhVwDXjA765J`</summary>

```text
1	dreams:
2	  dream_20260520T185641:
3	    dream_id: dream_20260520T185641
4	    project: xling_calib_direction
5	    status: writing
6	    review_mode: full
7	    review_visible: true
8	    writing_visible: true
9	    venue: ''
10	    focus: 'Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout)
11	      × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection;
12	      (2) difficulty-shared vs capability-specific decomposition may not cleanly separate;
13	      (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift
14	      completely fails, Pareto tradeoff directly observed at L24 vs L27.'
15	    what_if: []
16	    pid: 125082
17	    chat_id: oc_74ae31a7dc5ae9d419ba9a89bccc89c0
18	    card_message_id: om_x100b6fd47051f4a0b265b3fe5d1a636
19	    started_at: '2026-05-20T18:56:41+00:00'
20	    updated_at: '2026-05-20T19:37:07+00:00'
21	    stages_completed:
22	    - imagine
23	    - write
24	    error: null
25	    context_hash: abe53e536c904420db4b681d2d0235b9002bdc7eb51dd196e066bb0ebb988b82
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef53dc6f-fe9a-420a-bb37-5e049b11db80",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "caa617d6-abd1-423e-a372-b19630b4cc54",
  "sourceToolAssistantUUID": "ef53dc6f-fe9a-420a-bb37-5e049b11db80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T19:41:00.518Z_

Let me check the review_context.yaml and the existing review to understand where this review fits in the process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caa617d6-abd1-423e-a372-b19630b4cc54",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPYffQRVgnM6Yow4VG9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bedc034-5322-4144-bac3-11e6ad1b6c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6w44NXu6Za8W5pYg3J4zH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 36452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

_source line 42 · 2026-05-20T19:41:00.798Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YNFdj4cPc2FB7sRWNmxmXJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bedc034-5322-4144-bac3-11e6ad1b6c75",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPYffQRVgnM6Yow4VG9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22889491-d7fb-4891-a7cc-5228b6b91ee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6w44NXu6Za8W5pYg3J4zH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 36452,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1544
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 36452,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1544,
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

_source line 43 · 2026-05-20T19:41:01.204Z_

<details><summary>↩ Tool result · `toolu_01YNFdj4cPc2FB7sRWNmxmXJ`</summary>

```text
1	narrative_guidance: 'Original framing stands: "CaCLR shifts the cross-lingual calibration
2	  Pareto frontier." All 4 claims form an unbroken causal chain — discovery → analysis
3	  → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling
4	  with zero target-language labels. Pareto frontier is the organizing principle, CaCLR
5	  is the actionable contribution, decomposition explains why it works, orthogonality
6	  explains why output-based methods can''t.
7	
8	  '
9	imagined_experiments:
10	- name: Full Pareto Frontier — Qwen3-235B-A22B
11	  plan_id: plan_001
12	  description: 'Extract activations at every 4th layer (24 probed layers out of 94),
13	    20 languages, train English correctness probes (logistic regression + 2-layer
14	    MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection,
15	    few-shot 25/100, CaCLR).
16	
17	    '
18	  expected_results:
19	    en_auroc_best_layer: 0.843
20	    en_best_layer_idx: 72
21	    en_auroc_range:
22	    - 0.621
23	    - 0.843
24	    en_ece_raw_best: 0.162
25	    en_ece_tempcal_best: 0.054
26	    temp_scaling_T: 4.87
27	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.762
28	    zs_best_transfer_layer_idx: 56
29	    zs_transfer_drop_from_en_mean_pp: 8.1
30	    zs_auroc_by_tier:
31	      high_resource_mean: 0.791
32	      mid_resource_mean: 0.754
33	      low_resource_mean: 0.683
34	    zs_auroc_by_lang:
35	      en: 0.843
36	      zh: 0.802
37	      de: 0.796
38	      fr: 0.793
39	      es: 0.789
40	      ja: 0.785
41	      ru: 0.782
42	      pt: 0.788
43	      it: 0.786
44	      ar: 0.768
45	      hi: 0.761
46	      ko: 0.755
47	      vi: 0.749
48	      th: 0.743
49	      bn: 0.738
50	      tr: 0.756
51	      nl: 0.79
52	      sw: 0.695
53	      yo: 0.672
54	      ig: 0.681
55	    mean_shift_improvement_count: 2
56	    mean_shift_delta_ece_mean: 1.41
57	    linproj_auroc_mean_19lang: 0.724
58	    fewshot_25_auroc_mean_19lang: 0.748
59	    fewshot_100_auroc_mean_19lang: 0.771
60	    pareto_depth_transfer_rank_corr: 0.88
61	    pareto_frontier_layers:
62	    - 40
63	    - 44
64	    - 48
65	    - 52
66	    - 56
67	    - 60
68	    layers_above_0p5_auroc_count: 22
69	  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE with massive representation
70	    capacity. The jump from MVP''s 7B (en AUROC 0.754) to 235B is expected to yield
71	    ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling
72	    of linear probe accuracy with model parameters (Burns et al., Marks et al.). The
73	    MoE architecture concentrates expert representations, producing cleaner correctness
74	    signals in intermediate layers. The Pareto frontier emerges because deeper layers
75	    (L72+) specialize for English-dominant pretraining data distribution — the model''s
76	    language-specific processing intensifies past ~75% depth, degrading cross-lingual
77	    invariance. The best transfer layer (L56, ~60% depth) sits in the "universal reasoning"
78	    zone before language-specific heads activate. Low-resource languages (sw, yo,
79	    ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural
80	    patterns that even underrepresented languages partially align with in middle layers.
81	    Mean-shift continues to mostly fail because correctness directions are not simply
82	    mean-offset between languages — they require rotation, not translation, which
83	    linear projection and CaCLR address.
84	
85	    '
86	  tables:
87	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
88	      Layer'
89	    columns:
90	    - layer_idx
91	    - layer_depth_pct
92	    - en_auroc
93	    - zs_mean_auroc_19
94	    - zs_drop_pp
95	    - on_pareto
96	    rows:
97	    - - 4
98	      - 4
99	      - 0.621
100	      - 0.608
101	      - 1.3
102	      - false
103	    - - 8
104	      - 9
105	      - 0.648
106	      - 0.637
107	      - 1.1
108	      - false
109	    - - 12
110	      - 13
111	      - 0.689
112	      - 0.671
113	      - 1.8
114	      - false
115	    - - 16
116	      - 17
117	      - 0.712
118	      - 0.698
119	      - 1.4
120	      - false
121	    - - 20
122	      - 21
123	      - 0.738
124	      - 0.724
125	      - 1.4
126	      - false
127	    - - 24
128	      - 26
129	      - 0.756
130	      - 0.742
131	      - 1.4
132	      - false
133	    - - 28
134	      - 30
135	      - 0.771
136	      - 0.755
137	      - 1.6
138	      - false
139	    - - 32
140	      - 34
141	      - 0.784
142	      - 0.764
143	      - 2.0
144	      - false
145	    - - 36
146	      - 38
147	      - 0.795
148	      - 0.771
149	      - 2.4
150	      - false
151	    - - 40
152	      - 43
153	      - 0.803
154	      - 0.776
155	      - 2.7
156	      - true
157	    - - 44
158	      - 47
159	      - 0.81
160	      - 0.774
161	      - 3.6
162	      - true
163	    - - 48
164	      - 51
165	      - 0.816
166	      - 0.77
167	      - 4.6
168	      - true
169	    - - 52
170	      - 55
171	      - 0.822
172	      - 0.765
173	      - 5.7
174	      - true
175	    - - 56
176	      - 60
177	      - 0.827
178	      - 0.762
179	      - 6.5
180	      - true
181	    - - 60
182	      - 64
183	      - 0.831
184	      - 0.753
185	      - 7.8
186	      - true
187	    - - 64
188	      - 68
189	      - 0.835
190	      - 0.741
191	      - 9.4
192	      - false
193	    - - 68
194	      - 72
195	      - 0.839
196	      - 0.728
197	      - 11.1
198	      - false
199	    - - 72
200	      - 77
201	      - 0.843
202	      - 0.712
203	      - 13.1
204	      - false
205	    - - 76
206	      - 81
207	      - 0.841
208	      - 0.694
209	      - 14.7
210	      - false
211	    - - 80
212	      - 85
213	      - 0.838
214	      - 0.671
215	      - 16.7
216	      - false
217	    - - 84
218	      - 89
219	      - 0.832
220	      - 0.643
221	      - 18.9
222	      - false
223	    - - 88
224	      - 94
225	      - 0.819
226	      - 0.611
227	      - 20.8
228	      - false
229	    - - 92
230	      - 98
231	      - 0.791
232	      - 0.574
233	      - 21.7
234	      - false
235	    - - 94
236	      - 100
237	      - 0.762
238	      - 0.541
239	      - 22.1
240	      - false
241	  - name: 'Table 2: Transfer Condition Comparison (at best-transfer layer L56)'
242	    columns:
243	    - condition
244	    - auroc_mean_19
245	    - ece_mean_19
246	    - ece_reduction_vs_tempcal_pct
247	    rows:
248	    - - zero-shot
249	      - 0.762
250	      - 0.098
251	      - 0
252	    - - mean-shift
253	      - 0.758
254	      - 0.101
255	      - -3.1
256	    - - linear_projection
257	      - 0.781
258	      - 0.082
259	      - 16.3
260	    - - few-shot-25
261	      - 0.748
262	      - 0.089
263	      - 9.2
264	    - - few-shot-100
265	      - 0.771
266	      - 0.079
267	      - 19.4
268	    - - CaCLR
269	      - 0.814
270	      - 0.058
271	      - 40.8
272	  figures_description:
273	  - 'Figure 1a: Pareto frontier scatter plot (EN AUROC x-axis vs ZS mean AUROC y-axis),
274	    each point a layer, Pareto-optimal layers highlighted in red. Clear convex frontier
275	    shape from L40-L60.'
276	  - 'Figure 1b: Heatmap of ZS AUROC by language (y-axis, ordered by resource tier)
277	    × layer depth (x-axis). Shows warm band in mid-layers, cooling at extremes, with
278	    low-resource langs cooling earlier.'
279	  analysis: 'The Pareto frontier is crisp and monotonic: 6 layers form the efficient
280	    frontier between L40-L60. The rank correlation (Spearman) between layer depth
281	    and transfer degradation is ρ=0.88 (p<0.001). The frontier''s shape confirms that
282	    the depth- transferability tradeoff is not an artifact of small models — it amplifies
283	    at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56)
284	    is larger than MVP''s ~3-layer gap, consistent with deeper models having more
285	    room for language-specific specialization. All high-resource languages pass AUROC
286	    > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.
287	
288	    '
289	- name: Full Pareto Frontier — Llama 4 Scout
290	  plan_id: plan_002
291	  description: 'Extract activations at every 4th layer (12 probed layers out of 48),
292	    20 languages, 5 transfer conditions. INT8 weight quantization.
293	
294	    '
295	  expected_results:
296	    en_auroc_best_layer: 0.821
297	    en_best_layer_idx: 36
298	    en_auroc_range:
299	    - 0.634
300	    - 0.821
301	    en_ece_raw_best: 0.174
302	    en_ece_tempcal_best: 0.061
303	    temp_scaling_T: 5.34
304	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.741
305	    zs_best_transfer_layer_idx: 28
306	    zs_transfer_drop_from_en_mean_pp: 8.0
307	    zs_auroc_by_tier:
308	      high_resource_mean: 0.771
309	      mid_resource_mean: 0.733
310	      low_resource_mean: 0.661
311	    zs_auroc_by_lang:
312	      en: 0.821
313	      zh: 0.784
314	      de: 0.778
315	      fr: 0.775
316	      es: 0.771
317	      ja: 0.766
318	      ru: 0.762
319	      pt: 0.77
320	      it: 0.768
321	      ar: 0.748
322	      hi: 0.741
323	      ko: 0.735
324	      vi: 0.729
325	      th: 0.722
326	      bn: 0.718
327	      tr: 0.737
328	      nl: 0.772
329	      sw: 0.674
330	      yo: 0.641
331	      ig: 0.667
332	    mean_shift_improvement_count: 1
333	    linproj_auroc_mean_19lang: 0.706
334	    fewshot_25_auroc_mean_19lang: 0.728
335	    fewshot_100_auroc_mean_19lang: 0.752
336	    pareto_depth_transfer_rank_corr: 0.82
337	    pareto_frontier_layers:
338	    - 20
339	    - 24
340	    - 28
341	    - 32
342	  result_rationale: 'Llama 4 Scout has 48 layers (fewer than Qwen3''s 94) and a different
343	    MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active
344	    params, its active compute is smaller than Qwen3-235B''s ~22B active. This yields
345	    ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer
346	    points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but
347	    the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout''s best
348	    transfer layer sits at ~58% depth (L28), remarkably close to Qwen3''s 60%, suggesting
349	    a universal "mid-depth transfer zone" across architectures. The rank correlation
350	    is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant.
351	    Low-resource languages are slightly weaker because Meta''s multilingual pretraining
352	    mix underrepresents African languages compared to Qwen3.
353	
354	    '
355	  tables:
356	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
357	    columns:
358	    - layer_idx
359	    - layer_depth_pct
360	    - en_auroc
361	    - zs_mean_auroc_19
362	    - zs_drop_pp
363	    - on_pareto
364	    rows:
365	    - - 4
366	      - 8
367	      - 0.634
368	      - 0.624
369	      - 1.0
370	      - false
371	    - - 8
372	      - 17
373	      - 0.672
374	      - 0.659
375	      - 1.3
376	      - false
377	    - - 12
378	      - 25
379	      - 0.714
380	      - 0.699
381	      - 1.5
382	      - false
383	    - - 16
384	      - 33
385	      - 0.745
386	      - 0.729
387	      - 1.6
388	      - false
389	    - - 20
390	      - 42
391	      - 0.768
392	      - 0.748
393	      - 2.0
394	      - true
395	    - - 24
396	      - 50
397	      - 0.786
398	      - 0.745
399	      - 4.1
400	      - true
401	    - - 28
402	      - 58
403	      - 0.798
404	      - 0.741
405	      - 5.7
406	      - true
407	    - - 32
408	      - 67
409	      - 0.81
410	      - 0.732
411	      - 7.8
412	      - true
413	    - - 36
414	      - 75
415	      - 0.821
416	      - 0.714
417	      - 10.7
418	      - false
419	    - - 40
420	      - 83
421	      - 0.818
422	      - 0.689
423	      - 12.9
424	      - false
425	    - - 44
426	      - 92
427	      - 0.804
428	      - 0.651
429	      - 15.3
430	      - false
431	    - - 48
432	      - 100
433	      - 0.771
434	      - 0.608
435	      - 16.3
436	      - false
437	  - name: 'Table 4: Cross-Architecture Pareto Frontier Agreement'
438	    columns:
439	    - metric
440	    - qwen3_235b
441	    - llama4_scout
442	    - agreement
443	    rows:
444	    - - best_en_layer_depth_pct
445	      - 77
446	      - 75
447	      - within 2pp
448	    - - best_transfer_layer_depth_pct
449	      - 60
450	      - 58
451	      - within 2pp
452	    - - pareto_zone_depth_range_pct
453	      - 43-64
454	      - 42-67
455	      - overlapping
456	    - - depth_transfer_rank_corr
457	      - 0.88
458	      - 0.82
459	      - both >0.75
460	    - - frontier_shape
461	      - convex monotonic
462	      - convex monotonic
463	      - consistent
464	  figures_description:
465	  - 'Figure 2: Overlaid Pareto frontiers for both architectures (normalized depth
466	    %). Shows near-identical frontier shapes with Qwen3 shifted up-right (better overall)
467	    but same curvature.'
468	  analysis: 'Cross-architecture agreement is high: both models show best transfer
469	    at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank
470	    correlation between depth and transfer degradation exceeds 0.75 in both. The frontier
471	    shape is architecture-invariant — it''s the depth-normalized position, not absolute
472	    layer count, that determines the tradeoff. This validates Claim 1 at scale.
473	
474	    '
475	- name: CaCLR Implementation and Comparative Evaluation
476	  plan_id: plan_003
477	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train
478	    on English labels + unlabeled parallel activations. Compare vs all 5 conditions
479	    across full Pareto frontier, both models × 20 languages. Hyperparameter tuning
480	    (α, β).
481	
482	    '
483	  expected_results:
484	    best_alpha: 0.15
485	    best_beta: 0.08
486	    qwen3_caclr_auroc_mean_19lang: 0.814
487	    qwen3_caclr_ece_mean_19lang: 0.058
488	    qwen3_caclr_vs_linproj_auroc_delta_pp: 3.3
489	    qwen3_caclr_vs_zeroshot_auroc_delta_pp: 5.2
490	    qwen3_caclr_ece_reduction_vs_tempcal_pct: 40.8
491	    qwen3_caclr_best_operating_layer: 64
492	    llama4_caclr_auroc_mean_19lang: 0.793
493	    llama4_caclr_ece_mean_19lang: 0.064
494	    llama4_caclr_vs_linproj_auroc_delta_pp: 3.1
495	    llama4_caclr_vs_zeroshot_auroc_delta_pp: 5.2
496	    llama4_caclr_ece_reduction_vs_tempcal_pct: 38.5
497	    llama4_caclr_best_operating_layer: 32
498	    caclr_vs_linproj_auroc_delta_pp_mean: 3.2
499	    caclr_ece_reduction_vs_tempcal_pct_mean: 39.7
500	    caclr_improvement_pass_rate: 0.92
501	    caclr_pareto_shift_layers: 2
502	    low_resource_caclr_auroc:
503	      sw_qwen3: 0.731
504	      yo_qwen3: 0.709
505	      ig_qwen3: 0.718
506	      sw_llama4: 0.712
507	      yo_llama4: 0.681
508	      ig_llama4: 0.698
509	    low_resource_zs_pass_rate: 1.0
510	  result_rationale: 'CaCLR''s consistency loss (β·L_consistency) directly penalizes
511	    divergence between EN and non-EN probe outputs on parallel/comparable activations,
512	    forcing the probe to learn language-invariant features. This is strictly more
513	    informative than linear projection (which only aligns means and covariances post-hoc)
514	    because it shapes the learned representation during training. The 3.2pp AUROC
515	    gain over linear projection reflects the value of end-to-end optimization: linear
516	    projection corrects first-order distributional mismatch but not the nonlinear
517	    feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE)
518	    provides calibration-aware training that temperature scaling cannot — it directly
519	    optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE
520	    reduction over temperature scaling arises because CaCLR addresses the root cause
521	    (representation misalignment) rather than the symptom (miscalibrated probabilities).
522	    The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper
523	    than the ZS-optimal point while maintaining equivalent or better transfer — it
524	    literally pushes the Pareto frontier outward. Low-resource languages benefit most
525	    from L_consistency because their activation distributions are most misaligned
526	    from EN; the consistency term provides the strongest gradient signal precisely
527	    where the gap is largest.
528	
529	    '
530	  tables:
531	  - name: 'Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)'
532	    columns:
533	    - method
534	    - auroc_mean_19
535	    - ece_mean_19
536	    - requires_target_labels
537	    - params_overhead
538	    rows:
539	    - - zero-shot
540	      - 0.752
541	      - 0.098
542	      - 'no'
543	      - '0'
544	    - - mean-shift
545	      - 0.747
546	      - 0.102
547	      - 'no'
548	      - '0'
549	    - - linear_projection
550	      - 0.77
551	      - 0.082
552	      - 'no'
553	      - d×d matrix
554	    - - few-shot-25
555	      - 0.738
556	      - 0.089
557	      - yes (25)
558	      - '0'
559	    - - few-shot-100
560	      - 0.762
561	      - 0.079
562	      - yes (100)
563	      - '0'
564	    - - CaCLR
565	      - 0.804
566	      - 0.061
567	      - 'no'
568	      - ~1% probe params
569	  - name: 'Table 6: CaCLR Ablation — Loss Component Contributions'
570	    columns:
571	    - configuration
572	    - auroc_mean_19
573	    - ece_mean_19
574	    - delta_vs_full_auroc_pp
575	    rows:
576	    - - L_BCE_only (= zero-shot probe)
577	      - 0.752
578	      - 0.098
579	      - -5.2
580	    - - L_BCE + L_SB-ECE
581	      - 0.768
582	      - 0.072
583	      - -3.6
584	    - - L_BCE + L_consistency
585	      - 0.793
586	      - 0.078
587	      - -1.1
588	    - - L_BCE + L_SB-ECE + L_consistency (full CaCLR)
589	      - 0.804
590	      - 0.061
591	      - 0.0
592	  - name: 'Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)'
593	    columns:
594	    - layer_idx
595	    - zs_auroc_19
596	    - caclr_auroc_19
597	    - shift_pp
598	    - on_shifted_pareto
599	    rows:
600	    - - 40
601	      - 0.776
602	      - 0.798
603	      - 2.2
604	      - false
605	    - - 44
606	      - 0.774
607	      - 0.8
608	      - 2.6
609	      - false
610	    - - 48
611	      - 0.77
612	      - 0.803
613	      - 3.3
614	      - true
615	    - - 52
616	      - 0.765
617	      - 0.806
618	      - 4.1
619	      - true
620	    - - 56
621	      - 0.762
622	      - 0.81
623	      - 4.8
624	      - true
625	    - - 60
626	      - 0.753
627	      - 0.814
628	      - 6.1
629	      - true
630	    - - 64
631	      - 0.741
632	      - 0.814
633	      - 7.3
634	      - true
635	    - - 68
636	      - 0.728
637	      - 0.808
638	      - 8.0
639	      - true
640	    - - 72
641	      - 0.712
642	      - 0.796
643	      - 8.4
644	      - false
645	  figures_description:
646	  - 'Figure 3: Pareto frontier before/after CaCLR. ZS frontier (blue) vs CaCLR frontier
647	    (red), showing outward shift. CaCLR''s optimal operating point is 2 layers deeper
648	    with +5pp transfer AUROC.'
649	  - 'Figure 4: Per-language AUROC improvement from CaCLR over linear projection, grouped
650	    by resource tier. Low-resource languages show largest gains (4-6pp), high-resource
651	    2-3pp.'
652	  - 'Figure 5: Loss component ablation bar chart — stacked contributions of L_SB-ECE
653	    and L_consistency to final AUROC and ECE improvements.'
654	  analysis: 'CaCLR decisively outperforms all baselines. The ablation shows both loss
655	    terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp
656	    alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to
657	    0.061 when added). The interaction is synergistic — joint optimization yields
658	    better results than either term alone. The Pareto shift is the headline result:
659	    at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer
660	    vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation
661	    from "use shallower layers for transfer" to "use CaCLR and operate at deeper,
662	    better-calibrated layers." The improvement pass rate of 92% (35/38 model-lang
663	    pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages
664	    (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and
665	    the consistency loss has minimal signal to exploit.
666	
667	    '
668	- name: Difficulty-Controlled Ablation
669	  plan_id: plan_004
670	  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,
671	    retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers
672	    per model.
673	
674	    '
675	  expected_results:
676	    difficulty_probe_r2_mean: 0.72
677	    difficulty_var_explained_pct_mean: 68.4
678	    difficulty_var_explained_pct_range:
679	    - 58.2
680	    - 79.1
681	    residual_en_auroc_drop_pp: 4.2
682	    residual_zs_transfer_drop_pp: 1.1
683	    capability_specific_var_pct: 31.6
684	    capability_specific_transfer_degradation_pct: 87
685	    difficulty_component_transfer_degradation_pct: 13
686	    decomp_prescriptive_accuracy: 0.81
687	    difficulty_var_by_depth:
688	      shallow_20pct: 0.74
689	      mid_50pct: 0.69
690	      deep_80pct: 0.62
691	    capability_transfer_drop_by_depth:
692	      shallow_20pct: 0.8
693	      mid_50pct: 3.4
694	      deep_80pct: 9.7
695	  result_rationale: 'IRT difficulty is a strong, language-agnostic property — harder
696	    questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72)
697	    because difficulty is linearly encoded in intermediate representations (Civelli
698	    et al. confirmed this). The difficulty component accounts for 68% of explained
699	    variance because GlobalMMLU correctness is heavily driven by item difficulty:
700	    a model gets easy questions right in all languages and hard questions wrong in
701	    all languages. After projecting out difficulty, the residual correctness signal
702	    is "capability-specific" — it captures language-dependent competence differences.
703	    This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp
704	    at 20% depth) because deep layers encode language-specific processing that makes
705	    capability assessments non-transferable. The difficulty component transfers well
706	    at all depths (only 13% of total transfer degradation) because it''s language-invariant
707	    by construction. This decomposition is prescriptive: when difficulty explains
708	    most of a language''s correctness variance, simple zero-shot transfer suffices;
709	    when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy
710	    validates the decomposition as more than descriptive.
711	
712	    '
713	  tables:
714	  - name: 'Table 8: Decomposition Results — Difficulty vs Capability Components'
715	    columns:
716	    - component
717	    - var_explained_pct
718	    - transfer_auroc_mean
719	    - transfer_drop_from_en_pp
720	    - share_of_total_transfer_drop_pct
721	    rows:
722	    - - full_correctness
723	      - 100
724	      - 0.752
725	      - 8.1
726	      - 100
727	    - - difficulty_shared
728	      - 68.4
729	      - 0.738
730	      - 1.1
731	      - 13
732	    - - capability_specific
733	      - 31.6
734	      - 0.614
735	      - 14.2
736	      - 87
737	  - name: 'Table 9: Capability-Specific Transfer Drop by Depth'
738	    columns:
739	    - depth_band
740	    - difficulty_transfer_drop_pp
741	    - capability_transfer_drop_pp
742	    - ratio
743	    rows:
744	    - - 0-30%
745	      - 0.3
746	      - 0.8
747	      - 2.7×
748	    - - 30-60%
749	      - 0.8
750	      - 3.4
751	      - 4.3×
752	    - - 60-90%
753	      - 1.6
754	      - 9.7
755	      - 6.1×
756	  figures_description:
757	  - 'Figure 6: Stacked area chart showing difficulty vs capability variance across
758	    depth. Difficulty dominates at all depths but capability grows at deeper layers.'
759	  - 'Figure 7: Transfer degradation decomposed into difficulty (flat, near-zero) and
760	    capability (exponentially increasing with depth) components.'
761	  analysis: 'The decomposition cleanly separates: difficulty-shared signal is the
762	    majority (68%) of correctness variance and transfers near-perfectly across languages
763	    and depths. The capability-specific residual (32%) drives nearly all transfer
764	    degradation (87%), and this degradation accelerates exponentially with depth.
765	    This explains the Pareto frontier mechanistically: deeper layers have stronger
766	    capability-specific signals that improve EN calibration but impede transfer. CaCLR
767	    works because its consistency loss specifically targets the capability-specific
768	    component — forcing alignment of the non-difficulty residual across languages.
769	    The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms
770	    this is a load-bearing decomposition, not a post-hoc narrative.
771	
772	    '
773	- name: Cross-Lingual Orthogonality Analysis
774	  plan_id: plan_005
775	  description: 'Extract verbalized confidence direction via prompted confidence scores,
776	    compute cosine similarity with correctness direction across 20 languages × 2 architectures.
777	    Analyze by resource tier and language family.
778	
779	    '
780	  expected_results:
781	    orthogonality_cosine_mean_overall: 0.052
782	    orthogonality_cosine_range:
783	    - 0.018
784	    - 0.094
785	    orthogonality_cosine_en: 0.034
786	    qwen3_cosine_mean: 0.048
787	    llama4_cosine_mean: 0.057
788	    high_resource_cosine_mean: 0.041
789	    mid_resource_cosine_mean: 0.054
790	    low_resource_cosine_mean: 0.074
791	    cosine_by_lang:
792	      en: 0.034
793	      zh: 0.038
794	      de: 0.036
795	      fr: 0.039
796	      es: 0.041
797	      ja: 0.044
798	      ru: 0.043
799	      pt: 0.04
800	      it: 0.042
801	      ar: 0.051
802	      hi: 0.055
803	      ko: 0.049
804	      vi: 0.058
805	      th: 0.061
806	      bn: 0.056
807	      tr: 0.052
808	      nl: 0.037
809	      sw: 0.078
810	      yo: 0.094
811	      ig: 0.082
812	    all_langs_below_0p1: true
813	    cosine_resource_tier_correlation: -0.68
814	  result_rationale: 'Miao & Ungar (2026) established correctness-confidence orthogonality
815	    (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger
816	    models. The orthogonality persists universally (all < 0.1) because it reflects
817	    a fundamental architectural property: verbalized confidence is generated by the
818	    language modeling head from surface-level token probabilities, while correctness
819	    is encoded in intermediate representation geometry. These are structurally decoupled
820	    in transformer architectures. The slight increase in cosine for low-resource languages
821	    (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages
822	    have noisier confidence elicitation — the model''s verbalized confidence in Yoruba
823	    is less well-calibrated and leaks some correctness signal, producing weak correlation.
824	    The resource-tier gradient (ρ=-0.68) suggests that better multilingual training
825	    data produces cleaner separation between correctness and confidence representations.
826	    The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this
827	    is not architecture-specific. Llama 4''s slightly higher cosines may reflect its
828	    less aggressive multilingual pretraining compared to Qwen3.
829	
830	    '
831	  tables:
832	  - name: 'Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture'
833	    columns:
834	    - language
835	    - resource_tier
836	    - qwen3_cosine
837	    - llama4_cosine
838	    - mean_cosine
839	    rows:
840	    - - en
841	      - high
842	      - 0.031
843	      - 0.037
844	      - 0.034
845	    - - zh
846	      - high
847	      - 0.035
848	      - 0.041
849	      - 0.038
850	    - - de
851	      - high
852	      - 0.033
853	      - 0.039
854	      - 0.036
855	    - - fr
856	      - high
857	      - 0.036
858	      - 0.042
859	      - 0.039
860	    - - es
861	      - high
862	      - 0.038
863	      - 0.044
864	      - 0.041
865	    - - ja
866	      - high
867	      - 0.041
868	      - 0.047
869	      - 0.044
870	    - - ru
871	      - high
872	      - 0.04
873	      - 0.046
874	      - 0.043
875	    - - pt
876	      - high
877	      - 0.037
878	      - 0.043
879	      - 0.04
880	    - - it
881	      - high
882	      - 0.039
883	      - 0.045
884	      - 0.042
885	    - - nl
886	      - high
887	      - 0.034
888	      - 0.04
889	      - 0.037
890	    - - ar
891	      - mid
892	      - 0.047
893	      - 0.055
894	      - 0.051
895	    - - hi
896	      - mid
897	      - 0.051
898	      - 0.059
899	      - 0.055
900	    - - ko
901	      - mid
902	      - 0.045
903	      - 0.053
904	      - 0.049
905	    - - vi
906	      - mid
907	      - 0.054
908	      - 0.062
909	      - 0.058
910	    - - th
911	      - mid
912	      - 0.057
913	      - 0.065
914	      - 0.061
915	    - - bn
916	      - mid
917	      - 0.052
918	      - 0.06
919	      - 0.056
920	    - - tr
921	      - mid
922	      - 0.048
923	      - 0.056
924	      - 0.052
925	    - - sw
926	      - low
927	      - 0.073
928	      - 0.083
929	      - 0.078
930	    - - yo
931	      - low
932	      - 0.089
933	      - 0.099
934	      - 0.094
935	    - - ig
936	      - low
937	      - 0.077
938	      - 0.087
939	      - 0.082
940	  - name: 'Table 11: Orthogonality Summary Statistics'
941	    columns:
942	    - statistic
943	    - qwen3_235b
944	    - llama4_scout
945	    - both_models
946	    rows:
947	    - - cosine_mean
948	      - 0.048
949	      - 0.057
950	      - 0.052
951	    - - cosine_std
952	      - 0.015
953	      - 0.017
954	      - 0.016
955	    - - cosine_max
956	      - 0.089
957	      - 0.099
958	      - 0.094
959	    - - cosine_min
960	      - 0.031
961	      - 0.037
962	      - 0.018
963	    - - all_below_0.1
964	      - yes (20/20)
965	      - yes (19/20)
966	      - 39/40
967	    - - resource_tier_corr
968	      - -0.71
969	      - -0.65
970	      - -0.68
971	  figures_description:
972	  - 'Figure 8: Cosine similarity violin plots by resource tier, showing clear gradient
973	    from high (tight around 0.04) to low (spread around 0.08). All below 0.1 threshold.'
974	  - 'Figure 9: Scatter plot of cosine similarity vs language resource level (log wiki
975	    size), colored by architecture. Strong negative trend.'
976	  analysis: 'Orthogonality generalizes comprehensively. The mean cosine of 0.052 across
977	    all 40 language-architecture pairs is well within the "near-orthogonal" regime
978	    (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based
979	    calibration methods are not just structurally limited but are *more* limited for
980	    well-resourced languages where the orthogonality is strongest. This strengthens
981	    the motivation for probe-based approaches universally and for CaCLR specifically
982	    in multilingual settings. Yoruba''s 0.094 is the only value approaching the 0.1
983	    threshold (on Llama4 it hits 0.099), which is worth noting but does not break
984	    the claim.
985	
986	    '
987	- name: Probe Complexity Comparison
988	  plan_id: plan_006
989	  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models.
990	    Compare English accuracy, cross-lingual transfer degradation, calibration quality.
991	
992	    '
993	  expected_results:
994	    logreg_en_auroc_best: 0.843
995	    mlp_en_auroc_best: 0.856
996	    mlp_en_auroc_gain_pp: 1.3
997	    logreg_zs_transfer_drop_mean_pp: 8.1
998	    mlp_zs_transfer_drop_mean_pp: 12.4
999	    transfer_degradation_ratio: 1.53
1000	    logreg_ece_mean: 0.054
1001	    mlp_ece_mean: 0.068
1002	    logreg_transfer_advantage_shallow_pp: 2.1
1003	    logreg_transfer_advantage_deep_pp: 6.8
1004	  result_rationale: 'Linear probes transfer better because they learn a single hyperplane
1005	    in activation space — the hyperplane generalizes across languages when the underlying
1006	    geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear
1007	    decision boundaries that fit English-specific feature interactions, gaining ~1.3pp
1008	    EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers
1009	    (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear
1010	    structure that MLPs exploit but logreg ignores. This justifies our choice of linear
1011	    probes for the main results and supports the geometric interpretation of the Pareto
1012	    frontier: it''s about linear subspace alignment, not complex feature interactions.
1013	
1014	    '
1015	  tables:
1016	  - name: 'Table 12: Probe Complexity Comparison'
1017	    columns:
1018	    - probe_type
1019	    - en_auroc_best
1020	    - zs_auroc_mean_19
1021	    - zs_drop_pp
1022	    - ece_mean_19
1023	    rows:
1024	    - - logistic_regression
1025	      - 0.843
1026	      - 0.762
1027	      - 8.1
1028	      - 0.054
1029	    - - mlp_2layer
1030	      - 0.856
1031	      - 0.733
1032	      - 12.4
1033	      - 0.068
1034	  figures_description:
1035	  - 'Figure S1 (supplementary): Transfer drop (pp) vs layer depth for both probe types.
1036	    MLP line diverges sharply from logreg at deep layers.'
1037	  analysis: 'Linear probes are the correct choice for cross-lingual transfer: they
1038	    sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction
1039	    effect is notable — the logreg advantage grows from 2.1pp at shallow layers to
1040	    6.8pp at deep layers, confirming that deep-layer transfer degradation is driven
1041	    by nonlinear, language- specific features. CaCLR + logreg is thus the optimal
1042	    configuration.
1043	
1044	    '
1045	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
1046	  plan_id: plan_007
1047	  description: 'Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX
1048	    (20 languages).
1049	
1050	    '
1051	  expected_results:
1052	    belebele_zs_auroc_mean_19: 0.738
1053	    belebele_caclr_auroc_mean_19: 0.789
1054	    belebele_caclr_vs_zs_pp: 5.1
1055	    belebele_ece_reduction_vs_tempcal_pct: 36.2
1056	    mmlupx_zs_auroc_mean_19: 0.722
1057	    mmlupx_caclr_auroc_mean_19: 0.774
1058	    mmlupx_caclr_vs_zs_pp: 5.2
1059	    mmlupx_ece_reduction_vs_tempcal_pct: 33.8
1060	    caclr_benefit_cross_benchmark_cv: 0.08
1061	  result_rationale: 'Belebele tests reading comprehension (vs GlobalMMLU''s factual
1062	    knowledge), providing domain generalization evidence. Transfer AUROC is slightly
1063	    lower (0.738 vs 0.762) because Belebele''s passage-dependent questions have weaker
1064	    difficulty-shared signal — comprehension difficulty is more language-dependent
1065	    than factual difficulty. CaCLR still provides ~5pp improvement, confirming the
1066	    consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions
1067	    that compress the AUROC distribution (lower base rate of correctness), yielding
1068	    slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark
1069	    CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.
1070	
1071	    '
1072	  tables:
1073	  - name: 'Table 13: Cross-Benchmark Generalization'
1074	    columns:
1075	    - benchmark
1076	    - zs_auroc_mean_19
1077	    - caclr_auroc_mean_19
1078	    - caclr_gain_pp
1079	    - ece_reduction_pct
1080	    rows:
1081	    - - GlobalMMLU
1082	      - 0.752
1083	      - 0.804
1084	      - 5.2
1085	      - 39.7
1086	    - - Belebele
1087	      - 0.738
1088	      - 0.789
1089	      - 5.1
1090	      - 36.2
1091	    - - MMLU-ProX
1092	      - 0.722
1093	      - 0.774
1094	      - 5.2
1095	      - 33.8
1096	  figures_description:
1097	  - 'Figure S2: CaCLR improvement (pp) by benchmark × language, showing consistent
1098	    gains across domains.'
1099	  analysis: 'CaCLR generalizes cleanly across benchmarks. The improvement magnitude
1100	    is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method
1101	    addresses a fundamental representation alignment issue rather than overfitting
1102	    to GlobalMMLU- specific patterns. This is critical for reviewer confidence.
1103	
1104	    '
1105	- name: INT8 Validation Ablation
1106	  plan_id: plan_010
1107	  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for
1108	    Llama 4 Scout on 5% random subset.
1109	
1110	    '
1111	  expected_results:
1112	    int8_fp16_auroc_diff_mean_pp: 0.3
1113	    int8_fp16_auroc_diff_max_pp: 0.7
1114	    int8_fp16_ece_diff_mean_pp: 0.2
1115	    int8_fp16_transfer_drop_diff_pp: 0.4
1116	    int8_fp16_rank_correlation: 0.997
1117	    conclusion: INT8 quantization introduces negligible distortion
1118	  result_rationale: 'INT8 weight-only quantization preserves the 8 most significant
1119	    bits of each weight, introducing per-channel quantization noise of ~0.4% relative
1120	    magnitude. Correctness probing relies on the geometry of activation space (direction
1121	    of correctness signal), not absolute magnitudes. The quantization noise is approximately
1122	    isotropic and thus preserves angular relationships between directions. The 0.3pp
1123	    mean AUROC difference is within random seed variance, and the rank correlation
1124	    of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier
1125	    shape is unaffected. This result is expected given prior work showing that probing
1126	    results are robust to quantization down to INT4 (Gao et al., 2024).
1127	
1128	    '
1129	  tables:
1130	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)'
1131	    columns:
1132	    - layer_idx
1133	    - fp16_auroc
1134	    - int8_auroc
1135	    - diff_pp
1136	    - fp16_zs_auroc_5lang
1137	    - int8_zs_auroc_5lang
1138	    - transfer_diff_pp
1139	    rows:
1140	    - - 8
1141	      - 0.674
1142	      - 0.672
1143	      - 0.2
1144	      - 0.661
1145	      - 0.658
1146	      - 0.3
1147	    - - 16
1148	      - 0.747
1149	      - 0.745
1150	      - 0.2
1151	      - 0.731
1152	      - 0.728
1153	      - 0.3
1154	    - - 24
1155	      - 0.788
1156	      - 0.786
1157	      - 0.2
1158	      - 0.747
1159	      - 0.744
1160	      - 0.3
1161	    - - 32
1162	      - 0.812
1163	      - 0.81
1164	      - 0.2
1165	      - 0.734
1166	      - 0.731
1167	      - 0.3
1168	    - - 40
1169	      - 0.82
1170	      - 0.817
1171	      - 0.3
1172	      - 0.691
1173	      - 0.687
1174	      - 0.4
1175	  figures_description:
1176	  - 'Figure S3: INT8 vs FP16 AUROC scatter plot at all tested layer-language combinations.
1177	    Points fall tightly along y=x diagonal.'
1178	  analysis: 'INT8 quantization is validated as safe for our experimental setup. The
1179	    maximum observed difference (0.7pp at a single layer-language combination) is
1180	    well within the noise floor of probing experiments. The Pareto frontier ordering
1181	    is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer
1182	    concern #5.
1183	
1184	    '
1185	- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)
1186	  plan_id: plan_008
1187	  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages.
1188	    Provides dense vs MoE architectural contrast.
1189	
1190	    '
1191	  expected_results:
1192	    en_auroc_best_layer: 0.812
1193	    en_best_layer_idx: 45
1194	    zs_transfer_auroc_mean_19lang: 0.734
1195	    zs_best_transfer_layer_idx: 36
1196	    zs_transfer_drop_mean_pp: 7.8
1197	    pareto_depth_transfer_rank_corr: 0.86
1198	    caclr_auroc_mean_19lang: 0.786
1199	    caclr_vs_linproj_auroc_delta_pp: 2.9
1200	    dense_vs_moe_transfer_comparison: comparable within 2pp
1201	    pareto_shape: convex monotonic, consistent with MoE models
1202	  result_rationale: 'Gemma 4 31B Dense has fewer total parameters than the MoE models
1203	    but all are active, yielding comparable per-token compute. As a dense model, its
1204	    representations are more uniformly distributed across layers (no expert routing),
1205	    producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches
1206	    both MoE models, confirming this is a universal property of transformer depth,
1207	    not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B
1208	    active params < 22B active with MoE routing benefits. CaCLR improvement is slightly
1209	    lower (2.9pp) on the dense model because the absence of expert routing means less
1210	    language-specific feature fragmentation to correct. This is the ideal third data
1211	    point: different architecture family, consistent findings.
1212	
1213	    '
1214	  tables:
1215	  - name: 'Table 14: Three-Architecture Summary'
1216	    columns:
1217	    - model
1218	    - type
1219	    - layers
1220	    - en_auroc_best
1221	    - zs_auroc_mean_19
1222	    - best_transfer_depth_pct
1223	    - pareto_rank_corr
1224	    - caclr_gain_pp
1225	    rows:
1226	    - - Qwen3-235B-A22B
1227	      - MoE
1228	      - 94
1229	      - 0.843
1230	      - 0.762
1231	      - 60
1232	      - 0.88
1233	      - 3.3
1234	    - - Llama 4 Scout
1235	      - MoE
1236	      - 48
1237	      - 0.821
1238	      - 0.741
1239	      - 58
1240	      - 0.82
1241	      - 3.1
1242	    - - Gemma 4 31B Dense
1243	      - Dense
1244	      - 60
1245	      - 0.812
1246	      - 0.734
1247	      - 60
1248	      - 0.86
1249	      - 2.9
1250	  figures_description:
1251	  - 'Figure 10: Three-architecture Pareto frontiers overlaid (normalized depth). Remarkably
1252	    similar shapes despite architectural differences.'
1253	  analysis: 'The three-architecture comparison is the strongest evidence for the universality
1254	    of the depth-transferability tradeoff. The best-transfer depth converges to 58-60%
1255	    across dense and MoE architectures with 48-94 layers, CaCLR provides consistent
1256	    2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases.
1257	    Dense vs MoE makes minimal difference — the phenomenon is a property of transformer
1258	    depth, not routing architecture.
1259	
1260	    '
1261	- name: Extended Language Coverage (Camera-Ready)
1262	  plan_id: plan_009
1263	  description: 'Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele
1264	    full language sets.
1265	
1266	    '
1267	  expected_results:
1268	    total_languages: 52
1269	    new_languages_added: 32
1270	    zs_auroc_above_0p60_count: 48
1271	    zs_auroc_below_0p55_count: 2
1272	    caclr_improvement_positive_count: 49
1273	    mean_zs_auroc_51lang: 0.72
1274	    mean_caclr_auroc_51lang: 0.77
1275	    pareto_frontier_holds_all_langs: true
1276	    new_language_families_covered:
1277	    - Austronesian
1278	    - Dravidian
1279	    - Niger-Congo B
1280	    - Uralic
1281	    - Kartvelian
1282	  result_rationale: 'Expanding to 50+ languages primarily adds mid-resource languages
1283	    (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has
1284	    moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC
1285	    range, consistent with the mid-resource tier from the 20-language set. A handful
1286	    of extremely low-resource languages (e.g., Amharic script languages with minimal
1287	    pretraining data) may fall below 0.55, but these represent edge cases rather than
1288	    systematic failures. CaCLR continues to improve 96% of languages because the consistency
1289	    loss mechanism is language-agnostic — it aligns activation distributions without
1290	    requiring any language-specific knowledge. The Pareto frontier structure is preserved
1291	    across all 52 languages, confirming it''s a depth property, not a language-set
1292	    artifact.
1293	
1294	    '
1295	  tables:
1296	  - name: 'Table 15: Extended Language Coverage Summary by Resource Tier'
1297	    columns:
1298	    - tier
1299	    - n_langs
1300	    - zs_auroc_mean
1301	    - caclr_auroc_mean
1302	    - caclr_gain_pp
1303	    - pct_above_0p60
1304	    rows:
1305	    - - high
1306	      - 12
1307	      - 0.782
1308	      - 0.812
1309	      - 3.0
1310	      - 100
1311	    - - mid
1312	      - 25
1313	      - 0.738
1314	      - 0.784
1315	      - 4.6
1316	      - 100
1317	    - - low
1318	      - 10
1319	      - 0.661
1320	      - 0.712
1321	      - 5.1
1322	      - 90
1323	    - - very_low
1324	      - 4
1325	      - 0.582
1326	      - 0.638
1327	      - 5.6
1328	      - 50
1329	  figures_description:
1330	  - 'Figure 11: World map with per-language CaCLR AUROC, colored by performance tier.
1331	    Demonstrates broad geographic and typological coverage.'
1332	  analysis: 'The extension to 52 languages confirms all findings at broader scale.
1333	    The resource-tier gradient is smooth and predictable — no language family shows
1334	    anomalous behavior. CaCLR''s benefit is inversely correlated with resource level
1335	    (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the
1336	    consistency loss provides most value where representation misalignment is worst.
1337	    The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language
1338	    labels is the practical headline for camera-ready: usable cross-lingual calibration
1339	    for the vast majority of languages.'
1340	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22889491-d7fb-4891-a7cc-5228b6b91ee6",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "d198284a-b84b-419a-b7ac-27e704d997aa",
  "sourceToolAssistantUUID": "22889491-d7fb-4891-a7cc-5228b6b91ee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T19:41:05.076Z_

I now have thorough understanding of the full paper, its imagined results, and all project context. Let me now submit the review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d198284a-b84b-419a-b7ac-27e704d997aa",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPYv8JZVJchQF2vnK2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba90d7ed-75bf-4100-9f88-3b10e9d63fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JS4Z5JHKpEiTpKJ1f4bH4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17213,
      "cache_read_input_tokens": 37996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17213,
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

_source line 45 · 2026-05-20T19:42:55.865Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01FJWjmu3ZkME8KFgkt5aKks`</summary>

```json
{
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "dream_20260520T185641",
  "overall_score": "4 - Weak Accept",
  "report": "# Reviewer 2 (R2) — Focus: Novelty & Related Work\n\n## 1. Summary\n\nThis paper investigates cross-lingual transfer of English-trained correctness probes to 20 non-English languages across three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense). It identifies a depth-transferability Pareto frontier where deeper layers yield better English calibration but worse cross-lingual transfer, decomposes correctness transfer into difficulty-shared (68% var) and capability-specific (32% var) components, proposes CaCLR — a consistency-regularized probe training objective achieving +5.2pp AUROC and ~40% ECE reduction without target-language labels — and extends the correctness-confidence orthogonality finding from English to 20 languages.\n\n## 2. Novelty Assessment\n\n### Claim 1 — Pareto Frontier (Discovery): MEDIUM\n\nThe observation that middle layers transfer better cross-lingually while deeper layers encode more language-specific information is well-established (Liu & Niehues ACL 2025; Civelli et al. 2025 for difficulty probes; LACE's layer-ensemble motivation; Joshi et al. EMNLP 2025 for calibration direction evolution). The distilled literature itself notes \"English calibration improves monotonically; non-English peaks mid-late then degrades\" as a high-confidence cross-paper finding from Zhou et al. and Joshi et al. What is new is systematically charting this for *correctness* probes specifically (rather than difficulty or knowledge-boundary probes) across 20 languages and 3 architectures, and quantifying it as a Pareto frontier with Spearman correlation. However, the conceptual insight — \"deeper = more language-specific = worse transfer\" — is not surprising. The contribution is solid empirical characterization rather than conceptual advance. The convergence to 58-60% optimal transfer depth across architectures is a useful practical finding.\n\n### Claim 2 — Decomposition (Difficulty vs Capability): MEDIUM-LOW\n\nThe decomposition uses IRT difficulty probes (well-established psychometric tool) as a control. Civelli et al. (2025) already demonstrated that difficulty encoding is language-agnostic and transfers well cross-lingually. The novelty is reframing this as a decomposition of *correctness* transfer: subtracting the difficulty component and attributing 87% of transfer degradation to capability-specific residuals. While the experimental design is clean, it is essentially an ablation using known tools. The 68/32 variance split and 87% degradation attribution are useful quantifications, but the underlying idea — question difficulty is shared across languages while model capability varies by language — would be predicted by anyone familiar with IRT and cross-lingual probing. The \"prescriptive\" framing (81% accuracy predicting when CaCLR is needed) is the strongest novel element, but it is underexplored — how does this work in practice?\n\n### Claim 3 — CaCLR (Method): MEDIUM\n\nCaCLR = L_BCE + alpha * L_SB-ECE + beta * L_consistency. The SB-ECE term is from Karandikar et al. (NeurIPS 2021). The consistency loss penalizing divergence between EN and non-EN probe outputs on parallel activations is structurally identical to standard domain adaptation consistency regularization. The novelty is the *application* to probe-based calibration transfer, not the loss components or their combination. The \"no target-language labels needed\" property is practically valuable. The ablation shows L_consistency provides the bulk of AUROC gain (+4.1pp alone) while L_SB-ECE refines calibration, and their interaction is synergistic — this is a well-executed ablation. If the +5.2pp AUROC and ~40% ECE reduction are validated, the empirical contribution is solid. But as a method, CaCLR is a straightforward composition of existing techniques applied to a new setting.\n\n### Claim 4 — Cross-Lingual Orthogonality: LOW\n\nThis extends Miao & Ungar (2026b)'s finding (cosine < 0.04 for English) to 20 languages, reporting mean cosine 0.052, all < 0.1. This is the \"obvious next experiment\" after the original paper. The resource-tier gradient (rho = -0.68) is mildly interesting — low-resource languages show weaker orthogonality — but receives no mechanistic explanation beyond \"noisier confidence elicitation.\" The finding that Yoruba approaches 0.1 on Llama 4 (0.099) nearly breaks the claim and warrants deeper investigation rather than the dismissive \"does not break the claim\" treatment. This should be a supporting analysis, not a co-equal primary claim.\n\n## 3. Related Work Gaps\n\n### Missing references (moderate to significant):\n\n1. **Domain adaptation consistency losses (MAJOR gap)**: CaCLR's consistency loss is closely related to domain-adversarial neural networks (Ganin & Lempitsky 2015), DAN/MMD (Long et al. 2015), and Deep CORAL (Sun & Saenko 2016). The name \"CaCLR\" even risks confusion with Sun & Saenko's \"CORAL\" and Miao et al.'s \"CORAL.\" Without citing and differentiating from this literature, CaCLR appears significantly more novel than it is. This is the most important missing connection.\n\n2. **Cross-lingual representation alignment foundations**: Conneau et al. (2020, \"Emerging Cross-lingual Structure in Pretrained Language Models\"), Pires et al. (2019), Chi et al. (2020). These establish the theoretical basis for why probe transfer works at intermediate layers. The paper takes this for granted without attribution.\n\n3. **Procrustes alignment / CCA**: Schuster et al. (2019), Conneau et al. (2018, MUSE). The paper tests mean-shift and linear projection but does not discuss Procrustes alignment — the natural intermediate method between these two and CaCLR. Its absence from the transfer condition comparison is a methodological gap.\n\n4. **CCPS (Khanmohammadi et al., EMNLP 2025)**: Present in the project's literature map as a \"direct competitor\" but not cited in the paper. Calibration via probing perturbed representation stability, ~55% ECE reduction. Must be discussed.\n\n5. **DALI (Ravisankar et al., EACL 2026)**: In the literature map as providing \"strongest causal support\" via activation patching showing English middle-layer representations fix non-English errors. This is foundational evidence for the paper's hypothesis — its absence from the related work is puzzling.\n\n6. **Joshi et al. (EMNLP 2025)**: Calibration direction in residual stream, layer evolution. Directly relevant to Claim 1 but not cited.\n\n7. **Pre-LLM multilingual calibration**: The related work focuses narrowly on LLM-era work. Desai & Durrett (2020) and others on calibration of pretrained transformers provide historical context.\n\n### Inadequate differentiation:\n\n- **Xiao et al. (ACL 2025)**: The distinction (input-level answerability vs output-dependent correctness) is crucial but must be made unmistakable in the main text. A direct comparison experiment — running knowledge-boundary probes on the same data and showing different transfer dynamics — would be far more convincing than verbal differentiation.\n\n- **Civelli et al. (2025)**: The paper's Claim 2 methodology is essentially Civelli et al.'s difficulty probes used as controls. The relationship is too close to leave implicit — the paper should explicitly frame the decomposition as \"building on Civelli et al.'s finding that difficulty transfers well, we ask: what about the residual?\"\n\n## 4. Strengths\n\n- **Fills a genuine, well-documented gap**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar) are English-only. The 5x non-English ECE disparity (Zhou et al.) makes cross-lingual extension important and timely.\n\n- **Comprehensive experimental breadth**: 20 languages (expanding to 52), 3 architectures (MoE + dense), 5 transfer conditions, 3 benchmarks. This is substantially broader than Xiao et al. (8 languages, 1 architecture) and provides robust evidence.\n\n- **Clean causal claim structure**: Discovery → analysis → method → mechanism. Each claim builds on the previous. The paper would have a coherent narrative even if individual claims have moderate novelty.\n\n- **CaCLR has genuine practical value**: Zero target-language labels, ~1% parameter overhead, consistent improvement across 92% of language-model pairs. The ablation cleanly separates contributions of L_SB-ECE and L_consistency.\n\n- **Honest about MVP evidence**: The paper acknowledges mean-shift failure (0/5 languages) and uses it to motivate CaCLR rather than hiding it. This builds trust.\n\n- **INT8 ablation preempts a legitimate concern**: Quantization validation (rank correlation 0.997) is a responsible inclusion.\n\n- **Resource-tier analysis**: Systematic analysis by high/mid/low resource tiers, with CaCLR benefit inversely correlated with resource level, provides practical deployment guidance.\n\n## 5. Weaknesses\n\n- **(MAJOR) CaCLR's novelty is overstated without domain adaptation context.** The consistency loss is a standard domain adaptation technique (feature distribution matching) applied to probe training. The paper should cite DANN, DAN, Deep CORAL, and related work, then position CaCLR as a well-motivated *application* of consistency regularization to the specific setting of cross-lingual calibration probe transfer. Without this, the method section claims more novelty than warranted. Severity: major, because it affects how the core method contribution is perceived.\n\n- **(MAJOR) Claim 4 (orthogonality) is too weak for a primary claim.** Confirming cosine < 0.1 across 20 languages with the same probe methodology used for English is incremental. The resource-tier gradient deserves ~1 paragraph, not a full claim. Recommend restructuring as 3 claims + 1 supporting analysis. This matters because a 4-claim paper raises expectations that each claim provides substantial novelty. Severity: major for framing, minor for content (the analysis itself is fine, just misframed).\n\n- **(MODERATE) The \"Pareto frontier\" terminology may invite scrutiny.** In multi-objective optimization, a Pareto frontier implies non-dominated solutions with genuine tradeoffs. Here, the frontier is simply a depth-performance curve where deeper layers monotonically trade transfer for English performance — this is an expected trend, not a surprising tradeoff requiring Pareto analysis. The terminology adds terminological weight to what the cross-lingual representation literature already predicts. If reviewers familiar with the multi-objective optimization literature review this, they may find the framing imprecise.\n\n- **(MODERATE) Missing Procrustes alignment as a transfer condition.** The paper tests mean-shift, linear projection, few-shot, and CaCLR, but Procrustes alignment — the standard method for aligning cross-lingual embedding spaces (Conneau et al. 2018) — is absent. Its omission weakens the comparison, since Procrustes sits naturally between linear projection and CaCLR in terms of complexity and is a well-known baseline in cross-lingual representation alignment.\n\n- **(MODERATE) Decomposition's prescriptive value is underexplored.** The claim that the decomposition is \"prescriptive\" (81% accuracy predicting when CaCLR is needed vs simple transfer) is potentially the most novel aspect of Claim 2, but it receives minimal analysis. How is \"needed\" defined? What is the decision boundary? How would a practitioner use this in deployment? This deserves much more space.\n\n- **(MINOR) Temperature scaling baseline validity.** The project notes flag that T=6.21 may have been tuned on the test set rather than held-out data. If so, the ECE comparison is invalid. T>5 is unusual and suggests severe overconfidence — this should be carefully validated and discussed.\n\n- **(MINOR) Confidence interval / significance testing absence.** The field norm is point estimates without CIs (acknowledged in the literature review), but for a paper with simulated results at this scale, reporting bootstrap CIs or at minimum standard deviations across random seeds would strengthen claims, especially for close comparisons (e.g., few-shot-100 AUROC 0.771 vs CaCLR 0.804 — is 3.3pp significant?).\n\n- **(MINOR) MCQA-only scope.** Acknowledged by the authors, but worth noting: all evaluation is multiple-choice QA. Correctness labeling for free-form generation remains open, limiting practical applicability to the most common deployment scenario.\n\n## 6. Questions for Authors\n\n1. How does CaCLR's consistency loss differ from standard domain adaptation losses (e.g., MMD, adversarial alignment, Deep CORAL)? Have you compared against these alternatives? If not, what justifies the specific divergence penalty choice?\n\n2. The mean-shift alignment \"completely fails\" in your MVP, yet Xiao et al. (ACL 2025) report mean-shift success for knowledge-boundary probes. What explains this discrepancy — is it the target difference (answerability vs correctness), the layer choice, or the probe type?\n\n3. For Claim 2, what is the source of IRT difficulty scores? If estimated from model responses rather than human annotators, the difficulty-shared component is partially circular (model-dependent). How do you address this?\n\n4. Miao & Ungar report cosine < 0.04 for English; you report 0.034 (English) up to 0.094 (Yoruba). Is the increase for low-resource languages statistically significant? Yoruba on Llama 4 hits 0.099 — does this suggest a threshold exists where orthogonality breaks, and what are implications for the \"structurally limited regardless of language\" claim?\n\n5. The optimal transfer depth is 58-60% across all three architectures. Civelli et al. report architecture-dependent optimal depths (24-49%) for difficulty probes. Why is your range so much narrower and more consistent? Does this suggest correctness and difficulty probes access different representation subspaces?\n\n6. CaCLR's consistency loss requires \"parallel activations.\" Do these come from parallel translations in GlobalMMLU, or from a separate corpus? What happens when parallel data is unavailable — e.g., for the 32 additional languages in the camera-ready extension?\n\n7. Why is Procrustes alignment absent from the transfer condition comparison? Given its established role in cross-lingual embedding alignment, its absence is surprising and weakens the baseline comparison.\n\n8. The prescriptive decomposition (81% accuracy) is potentially the most novel element of Claim 2. Can you expand on the decision boundary, failure modes, and how a practitioner would operationalize this?\n\n## 7. Preliminary Score: 4 (Weak Accept)\n\n**Justification**: The paper addresses a genuine and timely gap — probe-based calibration has been exclusively English, and the 5x non-English ECE disparity makes cross-lingual extension both important and practical. The experimental design is comprehensive (20 languages, 3 architectures, 3 benchmarks, 5 transfer conditions). CaCLR provides meaningful improvements with zero target-language labels.\n\nHowever, the novelty is moderate across all four claims: (1) the Pareto frontier is an expected trend, systematically charted; (2) the decomposition uses known tools (IRT probes as controls) to confirm a predictable outcome; (3) CaCLR is a composition of existing losses applied to a new setting; (4) the orthogonality extension is confirmatory. The related work has significant gaps — most critically, the domain adaptation literature that would contextualize CaCLR's loss design.\n\nThe paper's strongest contribution is the systematic empirical characterization combined with a practical method — this positions it solidly for a venue like EACL. To strengthen toward a clear accept: (a) explicitly connect CaCLR to domain adaptation, compare against Procrustes/MMD baselines; (b) restructure to 3 primary claims + 1 supporting analysis; (c) expand the prescriptive decomposition analysis; (d) add 2-3 missing references (CCPS, DALI, Joshi).\n\nAt the 25% acceptance threshold, this paper is on the borderline — it would benefit from the above revisions to move into clear acceptance territory.\n\n## 8. Confidence: 4/5\n\nI have strong familiarity with the probe-based calibration, cross-lingual representation, and domain adaptation literatures. The main uncertainty is whether full-scale experiments (particularly CaCLR on 235B MoE models) would reveal unexpected phenomena — e.g., non-monotonic frontier behavior, architecture-dependent decomposition shifts, or prescriptive insights not predictable from prior work — that substantially change the novelty calculus. The simulated results are \"too clean\" (e.g., CaCLR improvement is exactly 5.2pp on both GlobalMMLU and MMLU-ProX), and real experiments may produce messier but more interesting findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba90d7ed-75bf-4100-9f88-3b10e9d63fe3",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPYv8JZVJchQF2vnK2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "936f03b8-7cab-45c6-9677-61e557c79a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JS4Z5JHKpEiTpKJ1f4bH4R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17213,
      "cache_read_input_tokens": 37996,
      "output_tokens": 4289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4289,
          "cache_read_input_tokens": 37996,
          "cache_creation_input_tokens": 17213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17213,
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

_source line 46 · 2026-05-20T19:42:59.084Z_

<details><summary>↩ Tool result · `toolu_01FJWjmu3ZkME8KFgkt5aKks`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md\", \"dream_id\": \"dream_20260520T185641\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "936f03b8-7cab-45c6-9677-61e557c79a36",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a5590f0616c82a5a5",
  "type": "user",
  "uuid": "4852e0af-7fe2-4b22-bf7b-08b4befcfe42",
  "sourceToolAssistantUUID": "936f03b8-7cab-45c6-9677-61e557c79a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T19:43:09.426Z_

Review submitted. Here is the summary:

**Score: 4 (Weak Accept) | Confidence: 4/5**

Key findings from the review:

**Novelty assessment by claim:**
- Claim 1 (Pareto frontier): Medium — systematic empirical characterization of a predicted trend, not a surprising discovery
- Claim 2 (Decomposition): Medium-Low — clean ablation using known IRT tools to confirm a predictable outcome; prescriptive element (81% accuracy) is underexplored
- Claim 3 (CaCLR): Medium — standard domain adaptation consistency loss applied to a new setting; solid empirical gains (+5.2pp AUROC, ~40% ECE) if validated
- Claim 4 (Orthogonality): Low — confirmatory extension of Miao & Ungar (2026b) from English to 20 languages; should be demoted to supporting analysis

**Critical related work gaps:**
1. Domain adaptation literature (DANN, DAN, Deep CORAL) — most important missing connection for contextualizing CaCLR
2. Procrustes alignment as a baseline transfer condition
3. CCPS (Khanmohammadi, EMNLP 2025), DALI (Ravisankar, EACL 2026), Joshi (EMNLP 2025) — all in the project's literature map but not cited in the paper
4. Cross-lingual representation alignment foundations (Conneau 2020, Pires 2019)

**Actionable recommendations to strengthen toward clear accept:**
1. Connect CaCLR to domain adaptation literature; add Procrustes/MMD baselines
2. Restructure from 4 co-equal claims to 3 + 1 supporting analysis
3. Expand the prescriptive decomposition analysis (strongest novel element of Claim 2)
4. Add missing citations from own literature map

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4852e0af-7fe2-4b22-bf7b-08b4befcfe42",
  "isSidechain": true,
  "agentId": "a5590f0616c82a5a5",
  "requestId": "req_011CbEPhcDXs5Td6VKzdBHVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22f9dc9b-24bb-4dd6-baa5-5a619bd7f5e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RvPcXtmMAbLD1XwffuBGS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4417,
      "cache_read_input_tokens": 55209,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 55209,
          "cache_creation_input_tokens": 4417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4417,
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
